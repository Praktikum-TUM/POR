"""Hilfsfunktionen zum Einlesen der POR-Messdaten und für die Auswertung."""
from __future__ import annotations
import os
import re
from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks


CSV_FOLDER = os.path.join(os.path.dirname(__file__), '..', '..', 'Input', 'Daten', 'Neuer Ordner')
XLSX_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'Input', 'POR (1).xlsx')


def _to_float(s: str) -> Optional[float]:
    s = s.strip()
    if not s:
        return None
    return float(s.replace(',', '.'))


@dataclass
class CassyData:
    """Ergebnisse einer Cassy-Messung."""
    file: str
    t_fast: np.ndarray
    u_fast: np.ndarray
    t_slow: np.ndarray
    u_mean: np.ndarray
    phi: np.ndarray
    label: str  # z.B. '0,35 A' oder '0,2 A'


def load_cassy(filename: str) -> CassyData:
    path = os.path.join(CSV_FOLDER, filename)
    with open(path, 'rb') as f:
        text = f.read().decode('utf-8-sig')
    lines = text.split('\n')[1:]
    t_fast, u_fast = [], []
    t_slow, u_mean, phi = [], [], []
    for line in lines:
        fields = line.split(';')
        if len(fields) < 5:
            continue
        tf = _to_float(fields[0])
        uf = _to_float(fields[1])
        if tf is not None and uf is not None:
            t_fast.append(tf)
            u_fast.append(uf)
        ts = _to_float(fields[2])
        um = _to_float(fields[3])
        ph = _to_float(fields[4])
        if ts is not None and ph is not None:
            t_slow.append(ts)
            u_mean.append(um if um is not None else np.nan)
            phi.append(ph)
    label_match = re.search(r'(\d+,?\d*)\s*Amp', filename)
    if label_match:
        label = label_match.group(1).replace('.', ',') + ' A'
    else:
        label = filename
    return CassyData(
        file=filename,
        t_fast=np.array(t_fast),
        u_fast=np.array(u_fast),
        t_slow=np.array(t_slow),
        u_mean=np.array(u_mean),
        phi=np.array(phi),
        label=label,
    )


def detect_release(t: np.ndarray, phi: np.ndarray) -> int:
    """Return the index after which the pendulum oscillates freely.

    Strategy: find the last point near the held maximum, then return the
    following index.  The held maximum is identified as the longest run of
    samples whose absolute deviation from the baseline exceeds 90 % of the
    maximum deviation.
    """
    # Baseline from the first second of data.
    mask_base = t < min(1.0, t[-1] * 0.1)
    if mask_base.sum() < 5:
        mask_base = t < t[0] + 1.0
    baseline = float(np.median(phi[mask_base])) if mask_base.any() else float(np.median(phi[:10]))
    centered = phi - baseline
    abs_c = np.abs(centered)
    threshold = 0.9 * abs_c.max()
    near_max = abs_c > threshold
    if not near_max.any():
        return 0
    # Find longest run of `near_max`.
    runs = []
    in_run = False
    start = 0
    for i, v in enumerate(near_max):
        if v and not in_run:
            in_run = True
            start = i
        elif not v and in_run:
            in_run = False
            runs.append((start, i - 1))
    if in_run:
        runs.append((start, len(near_max) - 1))
    # Choose the earliest run with at least 3 consecutive samples; this is
    # the held maximum, before damping has had time to reduce subsequent
    # peaks below the 0.9 threshold.
    held_run = None
    for s, e in runs:
        if e - s + 1 >= 3:
            held_run = (s, e)
            break
    if held_run is None:
        held_run = max(runs, key=lambda r: r[1] - r[0])
    return min(held_run[1] + 1, len(t) - 1)


def damped_cosine(t, A, lam, omega, phase, offset):
    return A * np.exp(-lam * t) * np.cos(omega * t + phase) + offset


def fit_damped(t: np.ndarray, phi: np.ndarray, sigma_phi: Optional[float] = None,
               t_max: Optional[float] = None):
    """Fit phi(t) = A*exp(-lam*t)*cos(omega*t+phase)+offset.

    Returns dict with parameters and standard uncertainties.
    """
    rel_idx = detect_release(t, phi)
    t_rel = t[rel_idx]
    if t_max is None:
        t_max = t[-1]
    mask = (t >= t_rel) & (t <= t_max)
    t_fit = t[mask] - t_rel
    phi_fit = phi[mask]
    if len(t_fit) < 20:
        raise ValueError(f'Too few points for fit: {len(t_fit)}')

    # Initial guesses.
    baseline = float(np.median(phi[t < min(1.0, t[-1] * 0.1)])) if (t < 1.0).any() else float(np.median(phi[:10]))
    A0 = float(np.max(np.abs(phi_fit - baseline)))
    # Frequency estimate via peak distance.
    try:
        peaks, _ = find_peaks(phi_fit - baseline, distance=5)
        if len(peaks) >= 2:
            T_est = float(np.mean(np.diff(t_fit[peaks])))
            omega0 = 2 * np.pi / T_est
        else:
            omega0 = 3.0
    except Exception:
        omega0 = 3.0
    # Damping estimate from envelope.
    try:
        peaks, _ = find_peaks(np.abs(phi_fit - baseline), distance=5)
        if len(peaks) >= 3:
            env_t = t_fit[peaks]
            env_a = np.abs(phi_fit - baseline)[peaks]
            # Avoid log of zero.
            mask_pos = env_a > 0
            if mask_pos.sum() >= 3:
                coeffs = np.polyfit(env_t[mask_pos], np.log(env_a[mask_pos]), 1)
                lam0 = -coeffs[0]
            else:
                lam0 = 0.1
        else:
            lam0 = 0.1
    except Exception:
        lam0 = 0.1
    # Sign of A may be negative; allow curve_fit to find it.
    sign = np.sign(phi_fit[0] - baseline) if abs(phi_fit[0] - baseline) > 0.1 else 1.0
    p0 = [sign * A0, max(lam0, 0.001), omega0, 0.0, baseline]

    sigma_arr = None
    if sigma_phi is not None:
        sigma_arr = np.full_like(phi_fit, sigma_phi)

    # Two-pass fit: first pass for parameter values, then rescale sigma to the
    # residual standard deviation so parameter uncertainties reflect the actual
    # model–data scatter rather than the pre-release sensor noise.
    popt, pcov = curve_fit(damped_cosine, t_fit, phi_fit, p0=p0, sigma=sigma_arr,
                           absolute_sigma=False, maxfev=20000)
    perr = np.sqrt(np.diag(pcov))
    return {
        'A': popt[0], 'u_A': perr[0],
        'lambda': abs(popt[1]), 'u_lambda': perr[1],
        'omega_d': abs(popt[2]), 'u_omega_d': perr[2],
        'phase': popt[3], 'u_phase': perr[3],
        'offset': popt[4], 'u_offset': perr[4],
        't_release': t_rel,
        'rel_idx': rel_idx,
        't_fit': t_fit + t_rel,
        'phi_fit': phi_fit,
        'mask': mask,
        'popt': popt,
        'pcov': pcov,
    }


def noise_std(t: np.ndarray, phi: np.ndarray, t_window: float = 1.0) -> float:
    """Estimate phi uncertainty from quiet pre-release segment."""
    mask = t < t_window
    if mask.sum() < 5:
        mask = t < t[0] + t_window
    if mask.sum() < 5:
        return 0.05
    return float(np.std(phi[mask], ddof=1))


def format_value(value: float, uncertainty: float, unit: str = '') -> str:
    """Format value+/-uncertainty with two significant digits on uncertainty (German comma)."""
    if uncertainty <= 0 or not np.isfinite(uncertainty):
        return f'{value:g} {unit}'.strip().replace('.', ',')
    # Determine the exponent of the uncertainty.
    exp_u = int(np.floor(np.log10(uncertainty)))
    # Round uncertainty to 2 sig figs.
    factor = 10 ** (exp_u - 1)
    u_round = round(uncertainty / factor) * factor
    # Round value to same decimal.
    if exp_u - 1 >= 0:
        decimals = 0
    else:
        decimals = -(exp_u - 1)
    fmt = f'{{:.{decimals}f}}'
    val_str = fmt.format(value)
    unc_str = fmt.format(u_round)
    # Replace '.' with ',' for German.
    val_str = val_str.replace('.', ',')
    unc_str = unc_str.replace('.', ',')
    if unit:
        return f'({val_str} \\pm {unc_str})\\,\\mathrm{{{unit}}}'
    return f'({val_str} \\pm {unc_str})'


def student_t_factor(n: int, confidence: str = '68') -> float:
    """t/sqrt(n) factor from the Fehlerrechnung table."""
    table_68 = {2: 1.30, 3: 0.76, 5: 0.51, 10: 0.34}
    table_95 = {2: 9.88, 3: 2.61, 5: 1.28, 10: 0.73}
    if confidence == '68':
        if n in table_68:
            return table_68[n]
        # interpolate or use 1/sqrt(n) for large n.
        return 1.0 / np.sqrt(n)
    if confidence == '95':
        if n in table_95:
            return table_95[n]
        return 2.0 / np.sqrt(n)
    raise ValueError(confidence)
