# Skizzenarten

Regeln für Skizzen außer dem Freikörperbild (das steht im Modus Skizze). Nur den passenden Abschnitt anwenden. Ein Kurspaket hat bei Symbolen und Bezeichnungen Vorrang.

**Immer:** Bezeichnungen wie in der Aufgabe. Positive Richtung oder Bezugssystem festlegen und einzeichnen. Nur Gegebenes und Gesuchtes, nichts Berechnetes. „Prüfen“ am Ende jedes Abschnitts heißt: diese Punkte am Endbild kontrollieren, bevor es gesendet wird.

| Aufgabe handelt von … | Abschnitt |
|---|---|
| Verlauf einer Größe, Messreihe, Diagramm, Kreisprozess | Graph |
| Widerständen, Quellen, Knoten, Maschen | Schaltplan |
| Wechselstrom, Phasenverschiebung, Impedanz | Zeigerdiagramm |
| Linse, Spiegel, Brechung, Reflexion | Strahlengang |
| Ladungen, Kondensator, Magnet, stromdurchflossenem Leiter | Feldlinien |
| Stoß, Wurf, Kreisbewegung, Relativbewegung | Bewegungsskizze |
| Atom, Spektrallinien, Photonen | Energieniveauschema |

## Graph
- **Achsen:** jede Achse mit Größe und Einheit, als *t* in s oder *t*/s; die Einheit nie in eckige oder runde Klammern (DIN 461, DIN 1313). Lineare Teilung mit gleichen Abständen, außer die Aufgabe verlangt logarithmisch. Abhängige Größe nach oben.
- **Kurve:** markante Punkte (Achsenschnitte, Extrema, Knicke, Sprünge) markieren; Asymptoten und Ablesehilfen gestrichelt. Mehrere Kurven beschriften, nicht nur über Farbe unterscheiden.
- **Messwerte:** als Punkte ohne Verbindungslinie; eine Ausgleichskurve glatt durch die Punktwolke, nicht durch jeden Punkt.
- **p-V-Diagramm:** Zustände nummerieren, Prozessrichtung mit Pfeilen auf der Kurve. Isobare waagerecht, Isochore senkrecht, Isotherme als Hyperbel, Adiabate steiler als die Isotherme durch denselben Punkt. Rechtslaufender Kreisprozess = Wärmekraftmaschine.
- **Prüfen:** Achsen vollständig beschriftet; Steigung und Fläche haben die richtige Bedeutung (Steigung im s-t-Diagramm = Geschwindigkeit, Fläche unter v-t = Weg, umschlossene Fläche im p-V-Diagramm = Arbeit); abgelesene Werte nicht als exakt ausgeben.

## Schaltplan
- **Symbole nach DIN EN 60617:** Widerstand als Rechteck (kein Zickzack, das ist US-Norm); ideale Spannungsquelle als Kreis, durch den die Leitung läuft; ideale Stromquelle als Kreis mit Strich quer zur Leitung; Batterie: langer dünner Strich = Pluspol; Kondensator zwei parallele Striche; Messgeräte als Kreis mit A oder V.
- **Leitungen:** nur waagerecht und senkrecht. Verbundener Knoten mit Punkt; Kreuzung ohne Punkt ist keine Verbindung.
- **Zählpfeile:** jede gegebene oder gesuchte Spannung und jeden Strom als benannten Pfeil. Am Verbraucher Verbraucher-Zählpfeilsystem (*U* und *I* gleich gerichtet), an der Quelle meist Erzeuger-Zählpfeilsystem; das gewählte System in einem Satz nennen. Richtung unbekannter Größen frei wählen; negatives Ergebnis = Gegenrichtung.
- **Bezeichnung:** *R*₁, *U*₁, *I*₁; Knoten mit Buchstaben, Maschen mit Umlaufpfeil.
- **Prüfen:** Amperemeter in Reihe, Voltmeter parallel; jeder Zählpfeil benannt; keine offenen Leitungsenden außer Klemmen.

## Zeigerdiagramm
- **Bezugszeiger** waagerecht nach rechts: bei Reihenschaltung der gemeinsame Strom, bei Parallelschaltung die gemeinsame Spannung.
- **Drehsinn** positiv gegen den Uhrzeigersinn. Phasenwinkel φ als Bogen zwischen den Zeigern, mit Pfeilspitze.
- **Bauteile:** Widerstand: *U* und *I* in Phase. Spule: *U* eilt *I* um 90° voraus. Kondensator: *I* eilt *U* um 90° voraus.
- **Addition:** Zeiger aneinanderhängen (Spitze an Fuß); Summe vom ersten Fuß zur letzten Spitze. Durchgehend Effektivwerte oder durchgehend Scheitelwerte; Maßstab nur bei quantitativer Zeichnung, dann angeben.
- **Prüfen:** Bezugszeiger passend gewählt; Drehrichtung der 90° bei Spule und Kondensator richtig; Summenzeiger schließt das Polygon.

## Strahlengang
- **Aufbau:** optische Achse als Strich-Punkt-Linie. Dünne Linse als senkrechter Strich: Sammellinse mit Pfeilspitzen nach außen, Zerstreuungslinse nach innen. Brennpunkte *F* und *F*′ im Abstand *f* auf beiden Seiten. Gegenstand *G* als Pfeil auf der Achse.
- **Konstruktion:** mindestens zwei der drei Hauptstrahlen von der Spitze des Gegenstands: Parallelstrahl wird Brennpunktstrahl; Mittelpunktstrahl geht ungebrochen durch; Brennpunktstrahl wird Parallelstrahl. Brechung an der Mittelebene der Linse. Der dritte Strahl dient zur Kontrolle.
- **Bild:** *B* dort, wo sich die Strahlen schneiden. Schneiden sich nur die rückwärtigen Verlängerungen, ist das Bild virtuell; Verlängerungen gestrichelt.
- **Grenzfläche und Spiegel:** Lot gestrichelt; alle Winkel zum Lot messen. Beim Übergang ins optisch dichtere Medium zum Lot hin. Reflexion: Einfallswinkel = Reflexionswinkel. Totalreflexion nur beim Übergang ins dünnere Medium oberhalb des Grenzwinkels.
- **Prüfen:** Strahlen mit Richtungspfeil; alle Hauptstrahlen treffen sich im selben Bildpunkt; Winkel am Lot, nicht an der Fläche.

## Feldlinien
- **Elektrisch:** Linien beginnen auf positiven und enden auf negativen Ladungen, mit Richtungspfeil; stehen senkrecht auf Leiteroberflächen; schneiden sich nie; ihre Dichte zeigt die Feldstärke. Plattenkondensator: innen parallel und gleich dicht, am Rand gebogen. Äquipotentiallinien gestrichelt und senkrecht zu den Feldlinien.
- **Magnetisch:** Linien geschlossen, außerhalb des Magneten von N nach S, innen von S nach N. Gerader Leiter: konzentrische Kreise, Richtung nach der Rechte-Hand-Regel (Daumen in Stromrichtung). Spule: innen parallel wie beim Stabmagneten. In die Zeichenebene ⊗, aus ihr heraus ⊙.
- **Prüfen:** elektrische Linien beginnen und enden nicht im leeren Raum; magnetische Linien sind geschlossen; die Symmetrie der Anordnung ist im Bild sichtbar.

## Bewegungsskizze
- **Stoß:** Zustand vor und nach dem Stoß in zwei getrennten Skizzen; Geschwindigkeiten mit Index (*v*₁, *v*₁′); eine positive Richtung als Pfeil festlegen.
- **Wurf:** Bahn, Abwurfpunkt, Koordinatensystem mit Ursprung im Abwurfpunkt; Geschwindigkeit tangential zur Bahn, *v*ₓ konstant, *v*ᵧ ändert sich; *g* nach unten.
- **Kreisbewegung:** Geschwindigkeit tangential, Zentripetalbeschleunigung zum Mittelpunkt. Zentrifugalkraft nur im mitrotierenden Bezugssystem und dann ausdrücklich so benannt.
- **Vektoraddition:** Pfeile aneinanderhängen; Resultierende vom Anfang des ersten zur Spitze des letzten; Winkel zu einer benannten Bezugsrichtung.
- **Prüfen:** Geschwindigkeits-, Beschleunigungs- und Kraftpfeile sichtbar unterschiedlich (Pfeilart oder Farbe mit Legende); Bezugssystem genannt.

## Energieniveauschema
- Waagerechte Linien, Energie nach oben, Achse mit *E* in eV. Nullpunkt angeben; meist ist die Ionisierungsgrenze *E* = 0 und gebundene Zustände sind negativ. Niveaus mit der Quantenzahl *n* beschriften; Abstände qualitativ, außer Werte sind gegeben.
- Übergänge als senkrechte Pfeile: Emission nach unten, Absorption nach oben.
- **Prüfen:** beim Wasserstoff werden die Abstände nach oben kleiner; Pfeilrichtung passt zu Emission oder Absorption.
