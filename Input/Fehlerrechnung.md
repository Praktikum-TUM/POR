# Umgang mit Unsicherheiten (ABW) — Zusammenfassung

Basiert auf: *Hinweise zur Beurteilung von Messungen, Messergebnissen und Messunsicherheiten (ABW)*, Physikalisches Praktikum TU München, Stand 08.03.21.

---

## 1. Grundlagen

### 1.1 Unsicherheit statt „Fehler"
- Messungen können prinzipiell nicht beliebig genau sein. Man spricht daher nicht von **Fehlern**, sondern von **Unsicherheiten** oder **Abweichungen**.
- „Fehler" im eigentlichen Sinn = grobe Vorgehensfehler (z.B. 1,50 V statt 1,05 V abgelesen). Diese werden durch sorgfältiges Arbeiten und Plausibilitätsprüfung ausgeschlossen, **nicht** durch Rechnung.
- Unsicherheiten stammen aus:
  - begrenzter Genauigkeit der Messgeräte,
  - Rückwirkung des Messinstruments auf das System (z.B. Innenwiderstand),
  - echten Schwankungen der Messgröße selbst (z.B. radioaktiver Zerfall).

### 1.2 Schreibweise von Werten und Unsicherheiten
Der Wert `x` wird immer zusammen mit Unsicherheit `u(x)` **und Einheit** angegeben:

$$(x \pm u(x))\ \text{Einheit} \tag{1}$$

**Zulässige Schreibweisen (gleichwertig):**
- `(355,62 ± 0,31) mm`
- `355,62(31) mm` ← bevorzugt in modernen Veröffentlichungen (Ziffern in Klammern = Unsicherheit der letzten Ziffern)

**Regeln:**
- Wert und Unsicherheit: **gleiche Größenordnung, gleiche Einheit**.
- Unsicherheit immer auf **zwei signifikante Stellen**, Wert entsprechend runden.
- **Relative** Unsicherheiten (z.B. `2,53 mV ± 5 %`) sind für Zwischenrechnungen nützlich, **dürfen aber im Endergebnis nicht stehen**.
- Falsch: `(6543,21 ± 50) g` → Richtig: `(6540 ± 50) g` oder `(6,54 ± 0,05) kg`.
- Vorsilben nutzen: nicht `0,003 m`, sondern `3 mm`; nicht `4,66·10⁻⁷ m`, sondern `466 nm`.
- Intern darf mit **einer Stelle mehr** gerechnet werden, damit Rundungsfehler sich nicht aufsummieren.

### 1.3 Unsicherheitstypen (nach GUM)
- **Typ A:** statistisch aus Mehrfachmessung bestimmt.
- **Typ B:** alles andere — Herstellerangaben, Kalibrierscheine, Abschätzungen beim Ablesen.

Die alte Unterscheidung „statistisch / systematisch" wird nicht mehr verwendet.

---

## 2. Verteilungen und ihre Unsicherheiten

| Verteilung       | Anwendung                                            | Unsicherheit                          |
| ---------------- | ---------------------------------------------------- | ------------------------------------- |
| Normal (Gauß)    | Mehrfachmessung, statistische Auswertung             | $u(\bar{x}) = \sigma_x/\sqrt{n}$      |
| Poisson          | Zählexperimente (radioaktiver Zerfall)               | $u(n) = \sqrt{n}$                     |
| Rechteck         | Einzelablesung Digitalanzeige, Schrittweite $a$      | $u(\mu) = a/(2\sqrt{3})$              |
| Dreieck          | Analoganzeige, Abstand zwischen Markierungen $a$     | $u(\mu) = a/(2\sqrt{6})$              |

Gaußsche Normalverteilung:
$$h(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}} \tag{3}$$

Vertrauensniveaus:
- 1 σ → 68,3 %
- 2 σ → 95,5 %
- 3 σ → 99,7 %

---

## 3. Unsicherheiten vom Typ A (statistisch)

### 3.1 Mittelwert
$$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i \tag{11}$$

### 3.2 Standardabweichung des Einzelwertes
$$\sigma_x = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i-\bar{x})^2} \tag{12}$$

Beantwortet: *Wie weit weicht ein einzelner Messwert typisch vom Mittelwert ab?*

### 3.3 Standardabweichung des Mittelwertes
$$\sigma_{\bar{x}} = \frac{1}{\sqrt{n}}\,\sigma_x \tag{13}$$

Beantwortet: *Wie weit weicht der Mittelwert vom wahren Wert ab?* Das ist die **Typ-A-Unsicherheit**:
$$u_\mathrm{A}(x) = \sigma_{\bar{x}} \tag{14}$$

### 3.4 Korrektur für wenige Messwerte (Student-t)
Bei kleinem `n` ist die Normalverteilung ungenügend — es wird ein Korrekturfaktor `t` eingeführt:
$$u(\bar{x}) = \frac{t}{\sqrt{n}}\,\sigma_x = t\cdot\sigma_{\bar{x}} \tag{15}$$

Werte aus Tabelle 2 (Auszug):

| n   | 68,2 % (t/√n) | 95 % (t/√n) | 99,7 % (t/√n) |
| --: | ------------: | ----------: | ------------: |
| 2   | 1,30          | 9,88        | 166,7         |
| 3   | 0,76          | 2,61        | 11,09         |
| 5   | 0,51          | 1,28        | 2,96          |
| 10  | 0,34          | 0,73        | 1,29          |
| ∞   | 1/√n          | 2/√n        | 3/√n          |

---

## 4. Unsicherheiten vom Typ B

Quellen: Herstellerangaben, Kalibrierscheine, Handbücher, Erfahrung.

### 4.1 Einzelquellen bei Messgeräten
- **Auflösung** `d` der Anzeige:
  - Digital → Rechteckverteilung: $u_\mathrm{B} = d/(2\sqrt{3})$.
  - Analog → Dreieckverteilung: $u_\mathrm{B} = d/(2\sqrt{6})$.
- **Reproduzierbarkeit:** maximaler Unterschied bei Wiederholmessungen unter gleichen Bedingungen.
- **Skalierungsunsicherheit:** proportional zum Messwert (meist in %).
- **Nullpunktsunsicherheit:** meist korrigierbar, Restanteil einrechnen.
- **Nichtlinearität:** Abweichung zwischen Null- und Endwertkalibrierung.
- **Unsicherheitsklasse:** z.B. Klasse 1 = 1 % vom Vollausschlag.

Typische Herstellerangabe:
$$\text{Unsicherheit} = A\,\% \cdot x + B\ \text{Digit}$$

### 4.2 Abschätzung bei Einzelmessungen
- Reaktionszeit mit Stoppuhr: 0,2 – 0,3 s bei unvorhergesehenen Ereignissen.
- Ablesen paralleler Striche: halbe bis ganze Strichbreite.
- Typ-B-Abschätzungen werden **nur** verwendet, wenn keine Typ-A-Unsicherheiten vorliegen.

---

## 5. Fortpflanzung der Unsicherheiten (Gaußsche Fehlerfortpflanzung)

Für eine berechnete Größe $g = g(x_1,\dots,x_N)$:

$$\bar{g} = g(\bar{x}_1,\dots,\bar{x}_N) \tag{17}$$

**Unkorrelierte Unsicherheiten:**
$$u(\bar{g}) = \sqrt{\sum_{i=1}^N \left(\frac{\partial g}{\partial x_i}\right)^2 u^2(\bar{x}_i)} \tag{19}$$

### 5.1 Mehrere Unsicherheiten pro Eingangsgröße
Typ A und mehrere Typ B werden zur Gesamtunsicherheit der Eingangsgröße zusammengefasst:
$$\Delta x = \sqrt{u_\mathrm{A}^2(x) + u_{\mathrm{B1}}^2(x) + u_{\mathrm{B2}}^2(x) + \dots} \tag{20}$$

### 5.2 Spezialfälle

**Summen / Differenzen** ($g = \sum \pm x_i$):
$$\Delta \bar{g} = \sqrt{\sum_{i=1}^N u^2(x_i)} \tag{21}$$
→ absolute Unsicherheiten werden quadratisch addiert.

**Produkte / Quotienten** ($g = \prod x_i^{m_i}$):
$$u(\bar{g}) = \bar{g}\cdot\sqrt{\sum_{i=1}^N \left(m_i\,\frac{u(\bar{x}_i)}{\bar{x}_i}\right)^2} \tag{22}$$
→ **relative** Unsicherheiten werden gewichtet quadratisch addiert.

Allgemeiner, falls $\partial g/\partial x_i = c_i\cdot g/x_i$:
$$u(\bar{g}) = \bar{g}\cdot\sqrt{\sum \left(c_i\,\frac{u(\bar{x}_i)}{\bar{x}_i}\right)^2} \tag{24}$$

### 5.3 Korrelierte Unsicherheiten
Korrelationen entstehen, wenn dieselbe Messapparatur, dasselbe Netzgerät oder dasselbe Kalibriernormal benutzt wird.
- Typ-A-Unsicherheiten sind **nicht** korreliert.
- Auflösung, Reproduzierbarkeit, Nichtlinearität: **nicht** korreliert.
- **Skalierungs-** und **Nullpunktsunsicherheit**: können korreliert sein.

Bei voller Korrelation für $g = f(\dots)(x_1 \pm x_2)$:
$$u^2(x_1)+u^2(x_2)\longrightarrow (u(x_1)\pm u(x_2))^2 \tag{26}$$

Für Quotienten $x_1/x_2$ bei voller Korrelation:
$$\left(\frac{u(x_1)}{x_1}\right)^2+\left(\frac{u(x_2)}{x_2}\right)^2 \longrightarrow \left(\frac{u(x_1)}{x_1}-\frac{u(x_2)}{x_2}\right)^2 \tag{28}$$

→ Bei Differenz/Quotient: prozentuale Skalierungsunsicherheit entfällt.

---

## 6. Gewichteter Mittelwert (Werte unterschiedlicher Genauigkeit)

$$\bar{x} = \frac{\sum w_i x_i}{\sum w_i}, \qquad w_i = \frac{1}{u(x_i)^2} \tag{29,30}$$

**Innere Unsicherheit** (aus den Einzelunsicherheiten):
$$u_\mathrm{int}(\bar{x}) = \sqrt{\frac{1}{\sum w_i}} \tag{31}$$

**Äußere Unsicherheit** (aus der Streuung):
$$u_\mathrm{ext}(\bar{x}) = \sqrt{\frac{\sum w_i(x_i-\bar{x})^2}{(n-1)\sum w_i}} \tag{32}$$

Als Gesamtunsicherheit verwendet man **das Maximum** aus $u_\mathrm{int}$ und $u_\mathrm{ext}$. Weicht $u_\mathrm{ext}$ stark ab, wurden vermutlich Einflüsse übersehen.

---

## 7. Graphische Darstellung und Ausgleichsgerade

### 7.1 Wichtige Regeln beim Plotten

1. **Datenpunkte als Symbole** darstellen (z.B. `•`, `■`, `◄`), unterschiedliche Symbole für unterschiedliche Messreihen.
2. **Datenpunkte nicht verbinden** — außer bei sehr dichten Daten oder wenn keine Theoriefunktion vorliegt.
3. **Fehlerbalken** an (mindestens einigen) Datenpunkten einzeichnen.
4. **Achsen beschriften** mit Größe **und Einheit**.
5. **Wertebereich ausnutzen** — keine leeren Bereiche.
6. **Legende** nur bei mehreren Datensätzen; bei einem Datensatz + Fit keine Legende.
7. **Nummerierung + Bildunterschrift** + Textverweis („Abbildung 1 zeigt…", **nicht** „folgende Abbildung").

### 7.2 Plausibilitätsprüfung: Liegen die Fehlerbalken auf der Geraden?

Dies ist der **zentrale Test** dafür, ob der angenommene lineare Zusammenhang gerechtfertigt ist:

- **Gut (Abb. 1a):** Datenpunkte streuen **gleichmäßig** um die Ausgleichsgerade. Die Gerade verläuft durch die Fehlerbalken der meisten Punkte. → linearer Zusammenhang plausibel.
- **Schlecht (Abb. 1b):** Punkte am linken und rechten Rand liegen **alle oberhalb** der Geraden, in der Mitte **alle darunter** (oder umgekehrt). Selbst wenn mehr als 67 % der Fehlerbalken die Gerade schneiden, deutet dieses **systematische Muster** darauf hin, dass der Zusammenhang nicht linear ist (z.B. parabolisch).

**Merksatz:** Es reicht nicht, dass die Fehlerbalken die Gerade treffen — die **Abweichungen müssen zufällig verteilt** sein (mal oben, mal unten), **nicht** systematisch strukturiert.

Erkennbar durch eine Gerade-durch-die-Punkte nicht legbar → mögliche Ursachen:
- kein linearer Zusammenhang,
- **Ausreißer** (einzelne Punkte weit weg, Rest passt zur Geraden) — Ausreißer bleiben in der Graphik, werden markiert, aber **nicht** in die Regression einbezogen,
- unerkannte systematische Abweichungen.

### 7.3 Logarithmische Darstellung
- Basis **10** verwenden (auch für e-Funktionen).
- Basis 2 nur zulässig, wenn der Wertebereich keine ganze Größenordnung umfasst.
- **Niemals** logarithmierte Werte auf linearer Skala auftragen — das führt zu Einheiten-Problemen.

---

## 8. Lineare Regression (Methode der kleinsten Quadrate)

Annahme: `x` genau bekannt, `y` fehlerbehaftet. Minimiere
$$S = \sum_{i=1}^n (y_i - (a_0+a_1 x_i))^2.$$

Mit der Koeffizientendeterminante
$$D = n\sum x_i^2 - \left(\sum x_i\right)^2$$

folgen Achsenabschnitt und Steigung:
$$a_0 = \frac{\sum x_i^2 \sum y_i - \sum x_i \sum y_i x_i}{D}, \qquad
a_1 = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{D} \tag{34}$$

Streuung der $y$-Werte um die Gerade:
$$\sigma_y = \sqrt{\frac{\sum (y_i-(a_0+a_1 x_i))^2}{n-2}}$$

(Normierung $1/(n-2)$ wegen zwei Freiheitsgraden der Geraden.)

Unsicherheiten der Parameter:
$$u(a_0) = \sigma_y\sqrt{\frac{\sum x_i^2}{D}}, \qquad u(a_1) = \sigma_y\sqrt{\frac{n}{D}} \tag{35}$$

**Wichtig:** Pro Datensatz gibt es **zwei** Regressionsgeraden (je nachdem, welche Variable als unabhängig gilt). Sie fallen nur zusammen, wenn alle Punkte exakt auf einer Geraden liegen.

### 8.1 Gewichtete lineare Regression
Wenn die $y_i$ unterschiedliche Unsicherheiten haben, Wichtung mit
$$w_i = \frac{1}{u^2(y_i)}$$

$$D = \sum w_i \sum w_i x_i^2 - \left(\sum w_i x_i\right)^2$$

$$a_0 = \frac{\sum w_i x_i^2 \sum w_i y_i - \sum w_i x_i \sum w_i y_i x_i}{D}, \quad
a_1 = \frac{\sum w_i \sum w_i x_i y_i - \sum w_i x_i \sum w_i y_i}{D}$$

- Konstante **absolute** Unsicherheit → normale Regression (alle $w_i$ gleich).
- Konstante **relative** Unsicherheit → $w_i = 1/y_i^2$.
- **Korrelierte** Unsicherheiten aus der Regression herauslassen und anschließend per Fortpflanzung einrechnen.

### 8.2 Allgemeine Regression
Nichtlineare Zusammenhänge $y = f(x)$ entweder per Variablentransformation linearisieren oder numerisch anpassen:
$$S = \sum (y_i - f(x_i))^2 \to \min \tag{36}$$

In der Praxis: fertige Software (z.B. SciDAVis, gnuplot, Python `scipy.optimize.curve_fit`, Origin).

---

## 9. Praktisches Kochrezept für die Fehlerrechnung

1. **Eingangsgrößen identifizieren:** Welche Messgrößen gehen in das Ergebnis ein?
2. **Für jede Messgröße Unsicherheiten sammeln:**
   - Typ A aus Mehrfachmessung ($\sigma_{\bar{x}}$, ggf. mit Student-t korrigiert).
   - Typ B: Auflösung, Reproduzierbarkeit, Skalierung, Nullpunkt, Nichtlinearität (getrennt behandeln!).
3. **Gesamt-Unsicherheit pro Eingangsgröße:** quadratische Summe aller zugehörigen Typ-A- und Typ-B-Anteile (Gl. 20).
4. **Partielle Ableitungen** der Zielgröße nach jeder Eingangsgröße bilden.
5. **Korrelationen prüfen:** dasselbe Gerät, Netzteil, Kalibriernormal? Falls ja, Skalierungs- und Nullpunktsanteile getrennt behandeln.
6. **Fortpflanzung anwenden** (Gl. 19, oder Spezialfälle Gl. 21 / 22 / 24).
7. **Ergebnis runden:** Unsicherheit auf 2 signifikante Stellen, Wert auf dieselbe Stelle.
8. **Schreibweise prüfen:** $(x \pm u(x))$ Einheit, gleiche Größenordnung, richtige Stellenzahl.

---

## 10. Längenmessung (Praktikumsgeräte)

**Meterstäbe / Messlineale:** $u(l) = a + b\cdot L$ (L auf nächsten vollen Meter aufgerundet)

| Klasse | a (mm) | b (mm/m) | Beispiel im Praktikum        |
| :----: | :----: | :------: | ---------------------------- |
| I      | 0,1    | 0,1      | —                            |
| II     | 0,3    | 0,2      | Stahllineale, Dreieckschienen|
| III    | 0,6    | 0,4      | Holz-Meterstäbe, Klebelineal |

**Messschieber:**

| Messbereich         | Unsicherheit | Ablesung  |
| ------------------- | :----------: | :-------: |
| $l < 50$ mm         | ± 0,05 mm    | ± 0,05 mm |
| $50 \le l \le 100$  | ± 0,06 mm    | ± 0,05 mm |
| $l > 100$ mm        | ± 0,07 mm    | ± 0,07 mm |

---

## 11. Digitalmultimeter — Unsicherheit

Typische Herstellerangabe: „$A\% + B$ Digit" mit Auflösung $C$.

Da Garantiegrenzen → **Rechteckverteilung**:
$$u_\mathrm{B1}(x) = \frac{A\%\cdot x}{\sqrt{3}}, \quad
u_\mathrm{B2}(x) = \frac{B\cdot C}{\sqrt{3}}, \quad
u_\mathrm{B3}(x) = \frac{C}{\sqrt{3}}$$

Gesamt:
$$u_\mathrm{B}(x) = \sqrt{\left(\frac{A\%\cdot x}{\sqrt{3}}\right)^2 + (B^2+1)\left(\frac{C}{\sqrt{3}}\right)^2} \tag{39}$$

---

## 12. Verbotene Praktiken (Kurzfassung)

1. Zahlenwerte **in Formeln einsetzen** (insbesondere mit Unsicherheiten).
2. Ergebnisse mit **falscher Stellenzahl**.
3. Abbildungen/Tabellen ohne Textverweis und Beschreibung.
4. Datenpunkte in Plots **verbinden** (wenn Theoriefunktion vorliegt).
5. Logarithmierte Werte auf linearer Skala auftragen.
6. Rohdaten-Tabellen im Fließtext statt im Anhang.
7. Wikipedia als Quelle.
8. **Reine relative Unsicherheit** beim Endergebnis.
9. Offensichtlich falsches Ergebnis ohne Diskussion stehenlassen.

---

*Quelle: Physikalisches Praktikum TU München, „Hinweise zur Beurteilung von Messungen, Messergebnissen und Messunsicherheiten" (ABW), Stand 08.03.2021.*
