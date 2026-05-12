# Mechanik: Pohlsches Rad (POR)

**Stand:** 6. August 2021  
**Seite 1**

---

## Pohlsches Rad (POR)
**Themengebiet:** Mechanik

In diesem Versuch wird die Bewegung eines Drehpendels untersucht. Zunächst werden freie gedämpfte Schwingungen des näherungsweise linearen Systems untersucht, anschließend erzwungene Schwingungen.

### 1 Grundlagen

#### 1.1 Lineare Systeme
Unter linearen Systemen versteht man solche, deren Bewegungsgleichung eine lineare Differenzialgleichung ist. Das im Versuch behandelte Drehpendel lässt sich als solches betrachten.

##### 1.1.1 Freie gedämpfte Schwingung eines Drehpendels (ohne externen Antrieb)
Im einfachsten Fall, d.h. ohne Antrieb, lässt sich das System wie folgt beschreiben: Wird das Pendel um einen Winkel $\phi$ ausgelenkt und dann losgelassen, führt es eine gedämpfte Drehschwingung um die Ruhelage $\phi_0$ aus. Diese Schwingung nennt man *gedämpfte Eigenschwingung* des Systems. Aus dem Drehmomentengleichgewicht

$$D_T = D_F + D_D \quad (1)$$

mit

*   $D_T = \Theta \ddot{\phi}$ Trägheitsdrehmoment, $\Theta$: Trägheitsmoment
*   $D_F = -k \phi$ rücktreibendes Moment der Feder, $k$: Winkelrichtgröße
*   $D_D = -\gamma \dot{\phi}$ Dämpfungsmoment, $\gamma$: Dämpfungskoeffizient

kann die Bewegungsgleichung des Systems abgeleitet werden. Man erhält die Differentialgleichung für die gedämpfte Eigenschwingung des Pendels

$$\Theta \ddot{\phi} + \gamma \dot{\phi} + k \phi = 0 \quad (2)$$

Dies ist eine homogene, lineare Differentialgleichung zweiter Ordnung. Mit dem Ansatz

$$\phi(t) = \phi_0 \cdot \exp(\alpha \cdot t)$$

in Gleichung (2) kommt man zur charakteristischen Gleichung zur Bestimmung von $\alpha$

$$\Theta \alpha^2 + \gamma \alpha + k = 0$$

Führt man die Dämpfungskonstante $\lambda$ mit $\lambda = \frac{\gamma}{2\Theta}$ ein, so erhält man die Lösungen

$$\alpha_{1,2} = -\lambda \pm \sqrt{\lambda^2 - \frac{k}{\Theta}} \quad (3)$$

Es lassen sich nun drei Lösungstypen unterscheiden:

---
© TU-München, Physikalisches Praktikum

**Seite 2**

---

### Bildbeschreibung: Abbildung 1
**Titel:** Ausschwingverhalten für schwache Dämpfung, Amplitude gegen die Zeit.
**Beschreibung:** Das Bild zeigt ein Koordinatensystem mit der vertikalen Achse $\phi$ (Winkel) und der horizontalen Achse $t$ (Zeit). Dargestellt ist eine gedämpfte Sinusschwingung, die bei $t=0$ mit der Amplitude $\phi_0$ beginnt. Die Maxima der Schwingung nehmen über die Zeit exponentiell ab. Diese Abnahme wird durch eine gestrichelte Einhüllende (Einhüllende Kurve) verdeutlicht, die mit $e^{-\lambda t}$ beschriftet ist. Markante Punkte auf der $\phi$-Achse sind $\phi_0$ und $\phi_0/e$. Auf der Zeitachse ist das Intervall $\lambda^{-1}$ (entspricht der Abklingzeit $\tau$) eingezeichnet, an dem die Amplitude auf $1/e$ ihres Ausgangswertes gesunken ist.

---

*   $\lambda^2 > \frac{k}{\Theta}$: Kriechfall (starke Dämpfung)
*   $\lambda^2 = \frac{k}{\Theta}$: aperiodischer Grenzfall
*   $\lambda^2 < \frac{k}{\Theta}$: Schwingungsfall (schwache Dämpfung)

Für den in diesem Versuch relevanten Schwingfall lautet die Lösung:

$$\phi(t) = \underbrace{\phi_0 \exp(-\lambda t)}_{\text{Dämpfung}} \cdot \underbrace{\exp[i(\omega_d t + \beta)]}_{\text{Schwingung}} \quad (4)$$

Das Ergebnis der Messung entspricht dem Realteil dieses Ausdrucks. Man kann also schreiben

$$\phi(t) = \phi_0 \exp(-\lambda t) \cdot \cos(\omega_d t + \beta) \quad (5)$$

mit $\omega_d = \sqrt{\frac{k}{\Theta} - \lambda^2}$ als Kreisfrequenz und $\beta$ als Phasenverschiebung. Die Eigenfrequenz des ungedämpften Pendels ist $\omega_0 = \sqrt{\frac{k}{\Theta}}$.

Die Lösung ist die in Abbildung 1 gezeigte Schwingung, deren Amplitude mit der Zeit exponentiell abklingt. Sie ist durch die Abklingzeit $\tau = \frac{1}{\lambda}$ und die Eigenfrequenz $f = \frac{\omega_d}{2\pi}$ charakterisiert.

Besonders hervorzuheben ist, dass die Eigenfrequenz *nicht* von der Schwingungsamplitude abhängt. Dies ist eine wichtige Besonderheit harmonischer Oszillatoren, die stets durch lineare Bewegungsgleichungen beschrieben werden.

---
© TU-München, Physikalisches Praktikum

**Seite 3**

---

##### 1.1.2 Erzwungene Schwingung (mit externem Antrieb)
Wird über den Antrieb zusätzlich ein äußeres periodisches Drehmoment $M_0 \sin(\omega t)$ auf das Pendel gegeben, erhält man eine erzwungene Schwingung. Nach einer Einschwingzeit ist die Frequenz des Pendels mit der Frequenz $\omega$ des Antriebs identisch. Die Bewegungsgleichung des ungestörten Systems (Gleichung 2) ändert sich nun zu

$$\Theta \ddot{\phi} + \gamma \dot{\phi} + k \phi = M_0 \sin(\omega t). \quad (6)$$

Dies ist eine *inhomogene*, lineare Differentialgleichung zweiter Ordnung. Die allgemeine Lösung der Differentialgleichung (6) setzt sich zusammen aus der Lösung der homogenen Differentialgleichung (2) und einer partikulären Lösung der inhomogenen (Gl. (6)). Eine partikuläre Lösung erhält man mit dem Ansatz

$$\phi_P(t) = A(\omega) \cdot \sin(\omega t - \Phi) \quad (7)$$

Die allgemeine Lösung der Differentialgleichung (6) erhält man, indem man zu dieser Lösung die Lösung der homogenen Differentialgleichung (Gl. 5) addiert.

$$\phi(t) = A(\omega) \cdot \sin(\omega t - \Phi) + C \cdot \exp(-\lambda t) \cdot \cos(\omega_d t - \beta) \quad (8)$$

Die Schwingungen des ungestörten und des angetriebenen Systems überlagern einander.

Nach einer Einschwingzeit verschwindet in Gleichung (8) der Term mit der Eigenfrequenz $\omega_d$ aufgrund der exponentiellen Dämpfung. Das Pendel schwingt nun nur noch mit der Frequenz $\omega$ des Antriebs, jedoch mit einer Phasenverschiebung $\Phi$ gegenüber der Erregerschwingung.

Durch Einsetzen der Lösung in Gleichung (6) ergibt sich für die Amplitude in Abhängigkeit der Antriebsfrequenz $\omega$

$$A(\omega) = \frac{M_0}{\sqrt{\Theta^2 \cdot (\omega_0^2 - \omega^2)^2 + \gamma^2 \cdot \omega^2}} = \frac{M_0/\Theta}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\lambda^2 \cdot \omega^2}}, \quad (9)$$

wobei $\omega_0 = \sqrt{\frac{k}{\Theta}}$ die Eigenfrequenz des nicht angetriebenen, ungedämpften Systems bedeutet. Für die Phasendifferenz $\Phi$ gilt

$$\tan(\Phi(\omega)) = \frac{\omega \cdot \gamma}{\Theta \cdot (\omega_0^2 - \omega^2)} = \frac{2\omega \cdot \lambda}{(\omega_0^2 - \omega^2)} \quad (10)$$

Die Amplitude der erzwungenen Schwingung erreicht bei der *Resonanzfrequenz*

$$\omega_R = \sqrt{\frac{k}{\Theta} - 2\lambda^2}$$

einen Maximalwert von

$$A(\omega_R) = \frac{M_0}{2\Theta \cdot \lambda \cdot \omega_d}$$

Für schwache Dämpfungen (und nur dafür) gilt

$$\omega_R \approx \omega_0 \approx \sqrt{\frac{k}{\Theta}}$$

---
© TU-München, Physikalisches Praktikum

**Seite 4**

---

### Bildbeschreibung: Abbildung 2
**Titel:** Resonanzkurve des Drehpendels.
**Beschreibung:** Die Abbildung zeigt ein Diagramm der Amplitude $A(\omega)$ über der Erregerfrequenz $\omega$. Die Kurve hat einen glockenförmigen Verlauf, der bei $\omega = 0$ einen endlichen Wert $A(0) = M_0/\Theta$ besitzt. Die Kurve steigt an bis zu einem Maximum $A_{max}$ bei der Resonanzfrequenz $\omega_R$. Danach fällt die Kurve für große Frequenzen asymptotisch gegen Null ab. Die Kurve ist nicht symmetrisch bezüglich $\omega_R$. Eingezeichnet ist die Halbwertsbreite $2\Delta\omega$ auf der Höhe von $A_{max}/\sqrt{2}$.

---

Die anderen Grenzwerte von Gleichung (6) sind

$$A(0) = \frac{M_0}{\Theta} \quad \text{und} \quad A(\infty) = 0$$

Trägt man $A(\omega)$ gegen $\omega$ auf, so erhält man die *Resonanzkurve*, wie sie in Abbildung 2 gezeigt ist. Man sieht, dass die Kurve bezüglich der Resonanzfrequenz nicht symmetrisch ist. Sie weist eine endliche Halbwertsbreite¹ $2 \cdot \Delta\omega$ um die Resonanzfrequenz $\omega_R$ auf. Zwischen der Halbwertsbreite $\Delta\omega$ der Resonanzkurve und der Dämpfungskonstanten $\lambda$ gilt für schwache Dämpfung nun die sehr wichtige Beziehung²

$$\Delta\omega = \lambda \quad \text{bzw.} \quad \tau \cdot \Delta\omega = 1 \quad (11)$$

Die Dämpfung dissipiert die vom Antrieb in das System gesteckte Energie. Je kleiner die Dämpfung des getriebenen Oszillators ist, umso größer wird im Resonanzfall seine Schwingungsamplitude. Für verschwindende Dämpfung führt dies zur *Resonanzkatastrophe*.

Betrachtet man die Phasenverschiebung, stellt man fest, dass die Schwingung dem Antrieb immer hinterherhinkt. Nach Gleichung (10) gilt also $0 \le \Phi \le \pi$.

#### 1.2 Wirbelstrombremse
Ein geschwindigkeitsabhängiges Dämpfungsmoment, wie es in Gleichung (2) vorkommt, lässt sich mit einer Wirbelstrombremse realisieren. Bewegt sich eine Leiterplatte in einem inhomogenen oder sich ändernden Magnetfeld senkrecht zu den Magnetfeldlinien, so werden im Leiter Wirbelströme induziert. Ein inhomogenes

---
¹ Man betrachtet meist die energetische Halbwertsbreite und demnach die $\frac{1}{\sqrt{2}}$-Breite der Amplitude. In der hier verwendeten Nomenklatur ist die halbe Breite (HWHM) gemeint. Einige Lehrbücher verwenden eine andere Nomenklatur.  
² Diese Beziehung erhält man mit einigen vereinfachenden Annahmen. Gleichung (11) soll hier nicht hergeleitet werden.

© TU-München, Physikalisches Praktikum

**Seite 5**

---

Magnetfeld hat man z.B. auch an den Grenzen eines endlich ausgedehnten Magneten. Die Stärke der Wirbelströme hängt von der Flussdichteänderung (und damit von der maximalen Flussdichte durch den Magneten) und der Geschwindigkeit der Relativbewegung ab.

Die Wirbelströme erzeugen ihrerseits ein Magnetfeld, das der Änderung des Magnetfeldes entgegenwirkt und linear von der Stärke der Wirbelströme abhängt. Die Wechselwirkung des ursprünglich angelegten Magnetfeldes und des durch die Wirbelströme induzierten führt zu einer Bremswirkung, die vom Produkt dieser beiden Magnetfelder abhängt. Daraus ergibt sich, dass die Bremswirkung letztendlich quadratisch von der magnetischen Flussdichte $B$ des Magneten und linear von der Relativgeschwindigkeit $v$ der Metallplatte und dem Magneten abhängt.

$$F \propto -v \cdot B^2 \quad (12)$$

Die Flussdichte $B$ in einer Spule hängt wiederum linear vom Strom $I$ durch die Spule ab. Übersetzt auf ein Drehpendel bedeutet dies, dass die Dämpfungskonstante $\lambda$ mit einer Wirbelstrombremse proportional zum Quadrat des Stroms durch die Spule ist:

$$\lambda \propto I^2 \quad (13)$$

### 2 Versuchsaufbau

#### 2.1 Drehpendel
Das hier verwendete Drehpendel³ besteht aus einer kreisförmigen Kupferscheibe, die um eine Achse durch den Schwerpunkt drehbar gelagert ist. Die Ruhelage wird durch eine Spiralfeder vorgegeben. Die Auslenkung des Pendels kann über eine kreisförmige Skala abgelesen werden. Das Pendel wird über eine Wirbelstrombremse gedämpft. Durch Variation des Stromes durch einen Elektromagneten können verschiedene Dämpfungsparameter eingestellt werden. Die Bremskraft ist proportional zur aktuellen Geschwindigkeit und zum Quadrat der magnetischen Flussdichte.

Das Drehpendel kann durch einen drehzahlgeregelten Schrittmotor über einen Exzenter und eine Getriebestange angetrieben werden. Die Drehfrequenz des Schrittmotors wird dabei über die Frequenz des Schrittgebers, in diesem Fall ein Signalgenerator, geregelt. Dabei entsprechen 3200 Schritte einer Umdrehung des Motors, eine Frequenz von 3200 Hz am Frequentgenerator entspricht also einer Antriebsfrequenz von 1 Hz.

Durch einen berührungsfreien Winkelsensor kann die Bewegung des Drehpendels ausgelesen werden. Hierbei wird die Richtung der Magnetfeldlinien der an der Kupferscheibe angebrachten Magnete detektiert. Das ausgegebene Spannungssignal ist linear vom Winkel abhängig.

Mit einem Kraftsensor, der über eine Feder mit dem Antrieb verbunden ist, kann dessen Auslenkung aufgenommen werden. Durch Vergleich der Auslenkung des Antriebs und des Pendels lässt sich die Phase bestimmen.

---
³ Das Pohlsche Rad ist eine spezielle Bauform des Drehpendels, die für die Schattenprojektion geeignet ist. Für diesen Versuch spielt das aber keine Rolle.

© TU-München, Physikalisches Praktikum

**Seite 6**

---

### 3 Durchführung

**Aufgabe 1: Eigenfrequenz**  
Wählen Sie den Dämpfungsstrom der Wirbelstrombremse im Bereich 0,3 - 0,6 A. Der Dämpfungsstrom bleibt für die folgenden Messungen konstant!  
Lenken Sie das Pendel aus und messen Sie mit Hilfe einer Stoppuhr die Zeit über 10 Schwingungen. Wiederholen Sie diesen Vorgang etwa fünf mal. Notieren Sie Unsicherheiten, die während dieser Messung auftreten können und berücksichtigt werden müssen!

**Aufgabe 2: Dämpfungskonstante**  
Lenken Sie nun das Pendel aus und notieren Sie nach jeder Schwingung die Amplitude. Schätzen Sie Ihre Unsicherheit bei der Bestimmung der Amplitudenmaxima.  
Die Idee hinter diesem Versuch ist, ein Gefühl dafür zu bekommen, wie gut die Messung mit dem Auge im Vergleich zur folgenden Computermessung ist.

**Aufgabe 3: Eigenfrequenz- und Dämpfungskonstantenbestimmung mit dem PC**  
Laden Sie von der Praktikumswebseite das Template (POR-Cassy.labx) für den Versuch und öffnen Sie es mit dem Programm CassyLab.  
Starten Sie die Messung in der Ruhelage des Pendels. Dadurch können Sie Abweichungen des Nullpunktes herausfinden und korrigieren. Lenken Sie das Pendel aus, das Programm misst die Schwingungsamplitude gegen die Zeit.

**Aufgabe 4: Resonanzkurve**  
Treiben Sie das Pendel mit dem Motor an.  
Nach dem Einschwingprozess lesen Sie mit dem Auge die Maximalamplitude ab. Notieren Sie Amplitude und zugehörige Frequenz. Dies führen Sie für verschiedene (mindestens 15) unterschiedliche Frequenzen durch. Wählen Sie die Frequenzen so, dass Sie eine gut auswertbare Resonanzkurve erhalten. Wählen Sie kleinere Schrittweiten in der Nähe der Resonanzfrequenz.  
Zeichnen Sie bereits im Praktikum direkt bei der Messung die Resonanzkurve um zu sehen, ob die Werte für eine Auswertung ausreichen.

**Aufgabe 5: Abhängigkeit der Dämpfungskonstanten vom Dämpfungsstrom**  
Diese Messung wird wieder ohne den Antrieb durchgeführt. Das Vorgehen ist wie in der Aufgabe 3, wobei nun diese Messung für verschiedene Ströme durch die Wirbelstrombremse (0,2 A bis 1,5 A in 0,1 A Schritten) durchgeführt wird.

---
© TU-München, Physikalisches Praktikum

**Seite 7**

---

### 4 Auswertung

#### 4.1 Stromabhängigkeit der Dämpfungskonstanten

**Aufgabe 6: Dämpfungskonstante**  
Führen Sie für die Messungen aller Dämpfungsströme eine Datenanpassung (Fit) mit der Gleichung (5) durch. Aus dem Fit bekommen Sie dann Werte für $\omega_d$ und $\lambda$.  
Tragen Sie die ermittelte Dämpfungskonstante $\lambda$ gegen den Dämpfungsstrom durch den Magneten auf. Vergleichen Sie die Abhängigkeit mit der für eine Wirbelstrombremse zu erwartenden (Gleichung (13)).

**Aufgabe 7: Eigenfrequenz**  
Tragen Sie die aus der Datenanpassung ermittelte Eigenfrequenz $\omega_d$ gegen die Dämpfungskonstante $\lambda$ auf. Vergleichen Sie das Verhalten mit dem theoretisch zu erwartenden.

#### 4.2 Untersuchung des Verhaltens bei dem gewählten Dämpfungsstrom

**Aufgabe 8: Eigenfrequenz**  
Bestimmen Sie aus Ihren Zeitmessungen die Eigenfrequenz des Pendels mit Unsicherheiten. Bestimmen Sie separat die Eigenfrequenz aus Ihren Computerdaten. Vergleichen Sie Ihre Ergebnisse samt Unsicherheit und Diskutieren Sie ihr Ergebnis!

**Aufgabe 9: Dämpfungskonstante**  
Erstellen Sie einen Graphen, bei dem die Amplituden der Schwingung halblogarithmisch gegen die Zeit aufgetragen werden. Ermitteln Sie die Dämpfungskonstante $\lambda$ samt Unsicherheit und die Abklingzeit $\tau$. Analog dazu werten Sie Ihre Computermessung aus. Vergleichen und Diskutieren Sie Ihre Ergebnisse!

**Aufgabe 10: Resonanzkurve**  
Tragen Sie die Maximalamplitude gegen die Anregungsfrequenz in einem Graphen auf und führen Sie eine Datenanpassung mit Gleichung (9) durch⁴. Ermitteln Sie die Resonanzfrequenz und die Halbwertsbreite der Resonanzkurve. Überprüfen Sie die Bedingung aus Gleichung (11).

---
⁴ Sie dürfen nur drei freie Parameter zum Datenanpassung verwenden, $\omega_0$, $\lambda$ und ($M_0/\Theta$).

© TU-München, Physikalisches Praktikum
