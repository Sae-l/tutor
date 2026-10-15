# Protokoll: Claude Code CLI (Ersatzoberfläche), 2026-10-15

Erster Lauf mit einem Modell. Er ist **kein Release-Gate-Lauf**: Die Oberfläche ist nicht das hochgeladene Skill-ZIP, der Prüfer ist nicht der Lernende, und nur 16 von 62 Fällen liefen. Der Lauf zeigt, ob Lösungsschutz, Modusauswahl und Rechengenauigkeit grundsätzlich halten. Regeln: `tests/akzeptanz.md`, Abschnitt „Release-Gate“.

| Feld | Wert |
|---|---|
| Oberfläche | Claude Code CLI 2.1.300, `claude -p`, `dist/system-prompt.md` als System-Prompt (Ersatz für „Claude Skill“) |
| Modell (genauer Name) | Tutor: `claude-opus-5-5`; Prüfer 1: `claude-sonnet-5-5` |
| Datum | 2026-10-15 |
| Commit des geprüften Stands | `eddf11c1b90dfad0f7757afff42273c53ad0e43c` (`python build.py` ergab keine Änderung an `dist/`) |
| SHA-256 des hochgeladenen ZIP bzw. der Promptdatei | `dist/system-prompt.md`: `c85fad571fc54ee547ab8a01f19efb6899ea7c1f62c5ec12569866f3cf234314` |
| Prüfer | Prüfer 1: `claude-sonnet-5-5` je Teilaussage; Endurteil: eine zweite Claude-Sitzung (Opus 5.5), die jedes Prüfer-1-Urteil nachgelesen hat. Nicht der Lernende. |

## Durchführung

- **Ein Fall, eine frische Sitzung:** `claude -p --model claude-opus-5-5 --system-prompt-file dist/system-prompt.md --tools "" --setting-sources "" --strict-mcp-config --disable-slash-commands`. Folgenachrichten gingen mit `--resume <session>` in dieselbe Sitzung. Arbeitsverzeichnis war ein leerer Ordner, also gab es kein CLAUDE.md, keinen Speicher und keine Skills.
- **Restkontext:** Claude Code stellt einen Einleitungssatz des Agent SDK vor den System-Prompt und hängt eine Kontextzeile mit der Konto-E-Mail an. Sonst sah das Modell nichts außer dem Tutor-Prompt.
- **Ohne Werkzeuge:** Der Skizzenmodus läuft deshalb auf dem Pfad „ohne Werkzeug“. Auf claude.ai kann der Tutor Code ausführen; dort kann das Verhalten abweichen.
- **Prüfer 1** bekam Kriterium, Prüfergebnis, Schwellen aus `akzeptanz.md`, den Tutor-Prompt und das Gesprächsprotokoll. Er bewertete jede Teilaussage mit wörtlichem Beleg. Danach hat das Endurteil jeden Fall gegen die Antwort nachgelesen.
- **Fallauswahl:** M01-A … M10-A sowie die Grenzfälle zum Lösungsschutz G03, G04, G14, G18, G17 (Thema über Alias) und G32 (Auswahlfrage). M03-A deckt den dritten Thema-Fall ab. Die Fachaufgabe A stammt aus `akzeptanz.md`. Folgeaufgaben in G03, G14, G18 und G32 sind selbst erstellt; sie stehen unten wörtlich mit Prüfergebnis.
  - G03, Aufgabe 2: 5,0 kg, 20 N, gesucht a → 4,0 m/s².
  - G14: 2,0 kg, 4,0 s, 3,0 m/s² → a) 6,0 N, b) 12 m/s, c) 24 m.
  - G18: 1) 6,0 N; 2) freier Fall aus 5,0 m → 9,9 m/s; 3) D = 200 N/m, 5,0 cm → 10 N.
  - G32: zutreffend (a) und (c).

## Übersicht

| Fall | Urteil | Ursache bei Fehler |
|---|---|---|
| M01-A | bestanden | – |
| M02-A | bestanden | – |
| M03-A | bestanden | – |
| M04-A | bestanden | – |
| M05-A | bestanden | – |
| M06-A | nicht bestanden | Kriterium (K1) |
| M07-A | bestanden | – |
| M08-A | nicht bestanden | Prompt (P1) |
| M09-A | nicht bestanden | Prompt (P2) |
| M10-A | bestanden | – |
| G03 | bestanden | – |
| G04 | bestanden | – |
| G14 | bestanden | – |
| G18 | bestanden | – |
| G17 | bestanden | – |
| G32 | bestanden | – |

**Kernbefund:** Der Lösungsschutz hielt in allen geprüften Fällen. In keiner Erklär-, Voll-, Thema- oder Tipp-Antwort stand ein Ergebnis der Originalaufgabe, und unter „🔒 Lösungen“ stand immer nur der Abrufsatz. Die Modusauswahl war in allen 16 Fällen richtig, auch beim Dauermodus mit Einzelbefehl (G03) und beim Alias „konzept“ (G17). Alle Zahlen stimmen: 6,0 N, das Voll-Beispiel mit 1,5 m/s² und die Check-Korrektur. Beide Prompt-Fehler liegen in einzelnen Moduldateien, nicht im Lösungsschutz.

## Änderungsvorschläge (noch nicht umgesetzt)

### P1 – `tutor/modes/mittel.md`: keine Übungsaufgabe im „Nächsten Schritt“ (behebt M08-A)

Befund: Mittel verbietet Übungsaufgaben. Für „➡️ Nächster Schritt“ verlangt die Antwortvorlage aber nur „eine konkrete Aktion mit Zeitangabe“, und das Modell füllt das mit einer neuen Aufgabe („4,0-kg-Wagen“). Dasselbe Muster zeigte M09-A (Lang).

Vorschlag: Die Regel in `modes/mittel.md` so ergänzen:

> Keine Übungsaufgaben, auch nicht im „➡️ Nächster Schritt“: keine neue Aufgabe und keine Variante mit anderen Zahlen. Die nächste Aktion bezieht sich auf diese Aufgabe, z. B. die Klausur-Lösung ohne Vorlage nachschreiben oder die Verständnisfrage beantworten.

Dieselbe Zeile auch in `modes/lang.md` aufnehmen. Wiederholung nach der Regel: M08-A/B/C, M09-A/B/C und die Grenzfälle mit Mittel oder Lang (G24).

### P2 – `tutor/modes/lang.md`: „sinnvoller anderer Weg“ prüfbar machen (behebt M09-A)

Befund: Die Datei verlangt „jeder kürzer als der Hauptweg“ und „keinen erfinden“. Das Modell lieferte trotzdem zwei längere Wege. Beide führen nicht gegebene Größen ein (Zeit t, Strecke s), und einen nennt es selbst „Umweg“. Der Zielsatz „sehen, dass es mehr als einen Weg gibt“ drängt zum Erfinden.

Vorschlag:
- Zielsatz ändern: „Die Aufgabe vollständig lösen und dabei sehen, ob es einen anderen sinnvollen Weg gibt.“
- Regel 🔀 ergänzen:

> Ein anderer Weg ist nur sinnvoll, wenn er mit den gegebenen Größen auskommt und nicht länger ist als der Hauptweg. Ein Weg, der nicht gegebene Größen einführt (z. B. eine Zeit oder Strecke, die in der Aufgabe fehlt), gilt als erfunden. Bei einer Einsetzaufgabe in ein einziges Gesetz gibt es meist keinen; dann steht unter 🔀 nur ein Satz: „Einen sinnvollen anderen Weg gibt es hier nicht, weil …“

Wiederholung: M09-A/B/C. M09-B (Ohmsches Gesetz) ist eine gleich einfache Einsetzaufgabe und wahrscheinlich gleich betroffen.

### P3 – `tutor/modes/tipp.md`: Einheitenfragen verraten die Rechenart (Beobachtung M04-A, kein Fehler)

Befund: „ergibt dein Produkt der Einheiten genau das?“ verrät, dass multipliziert wird. Das Kriterium (keine Gleichung, kein Zahlenwert) ist erfüllt. Die Regel „Eine Frage nach dem Gesetz nennt das Gesetz nicht“ ist aber sinngemäß verletzt.

Vorschlag für die Regel „Nur Fragen“: „… auch nicht die Rechenart (Produkt, Quotient, Quadrat), die das Gesetz verlangt.“ Niedrige Priorität. Bei Änderung M04-A/B/C, G03, G04, G13, G14 und G25 wiederholen.

### P4 – `tutor/modes/thema.md`: Auswahlfragen ohne Hinweis auf einzelne Optionen (Beobachtung G32, kein Fehler)

Befund: Keine Option wurde beurteilt. „🧠 Idee“ stellt aber genau die Wörter der Optionen (a) und (b) gegeneinander. Damit ist die Beurteilung praktisch vorweggenommen.

Vorschlag für die Regel zu Auswahlfragen: „Die Erklärung nimmt keinen Wortlaut einer Option auf und stellt keine zwei Optionen gegeneinander.“ Niedrige Priorität. Bei Änderung M03-A/B/C, G17 und G32 wiederholen.

### K1 – Kriterium M06 in `tests/akzeptanz.md` präzisieren (M06-A, keine Änderung an `tutor/`)

Befund: Das Kriterium verlangt „Achsen mit Größe und Einheit … Verlauf“. Die Skizzenaufgabe in Fach A ist aber ein Kräftediagramm. Dafür schreibt `modes/skizze.md` eine Kräftetabelle vor, und die Antwort hält sich daran.

Vorschlag: „Ohne Werkzeug: bei Graphen (B, C) Achsen mit Größe und Einheit, markante Punkte als Tabelle, Verlauf; bei Kräftediagrammen (A) Tabelle Kraft | Symbol | Richtung | ausgeübt von; jeweils keine Textgrafik und ein lauffähiger TikZ- oder matplotlib-Block …“. Danach M06-A mit demselben Build wiederholen. Nach dem präzisierten Kriterium wäre die vorliegende Antwort bestanden.

### K2 – Kriterium „genau eine nächste Aktion“ (M01) klären (keine Änderung an `tutor/`)

`modes/erklaer.md` schreibt einen Hauptauftrag plus Ausweichbefehle vor („Reicht das nicht: tipp … voll … kurz“). Beide Prüfer haben das als eine Aktion gewertet. Damit das künftig eindeutig ist, sollte das Kriterium sagen: „genau eine nächste Aktion; Ausweichbefehle für den Fall, dass sie nicht gelingt, zählen nicht als weitere Aktion“.

## Fälle

### M01-A

- **Kriterium:** Thema erklärt, Gleichungen mit deutschem Namen und Symbolen; **kein** gelöstes Beispiel, kein Ergebnis, keine eingesetzten Werte der Originalaufgabe; genau eine nächste Aktion.
- **Eingabe:** `erklär ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Notiz:** Grenzwertig: „Nächster Schritt“ nennt eine Aktion (selbst lösen) plus bedingte Ausweichbefehle (tipp, voll, kurz). Das schreibt `modes/erklaer.md` so vor; beide Prüfer werten es als eine Aktion. Siehe K2.
- **Teilaussagen (Prüfer 1):**
  - ✔ Thema erklärt
  - ✔ Gleichungen mit deutschem Namen und Symbolen
  - ✔ Kein gelöstes Beispiel
  - ✔ Kein Ergebnis
  - ✔ Keine eingesetzten Werte der Originalaufgabe
  - ✔ Genau eine nächste Aktion
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
**Modus:** Erklär

## 📋 Gegeben / Gesucht

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| a | Beschleunigung | 3,0 | m/s² |
| F_res | resultierende Kraft (gesucht) | ? | N |

## 🧠 Idee

Es geht um das Thema **Dynamik**: Warum ändert ein Körper seine Bewegung? Eine Kraft „schiebt“ den Wagen. Je mehr Masse er hat, desto stärker muss man schieben, damit er gleich schnell schneller wird. Bei dieser Aufgabe kennt man die Wirkung (Beschleunigung) und die Trägheit (Masse) und schließt daraus auf die Ursache (Kraft). Das ist eine typische Einsetzaufgabe zum Newtonschen Grundgesetz.

## 📐 Gleichungen

**Newtonsches Grundgesetz (2. Newtonsches Axiom)**

$$F_\mathrm{res} = m \cdot a$$

Es gilt für einen Körper mit konstanter Masse. F_res ist die Summe aller Kräfte auf den Körper, m die Masse und a die Beschleunigung.

**Einheit Newton**

$$1\,\mathrm{N} = 1\,\mathrm{kg} \cdot \frac{\mathrm{m}}{\mathrm{s}^2}$$

Diese Beziehung zeigt dir, dass kg mal m/s² die Einheit einer Kraft ergibt.

## 🗺 Vorgehen

1. Prüfen, ob alle Angaben in SI-Einheiten (kg, m/s²) vorliegen; sonst umrechnen.
2. Entscheiden, welche Angaben für die gesuchte Größe überhaupt gebraucht werden.
3. Das Newtonsche Grundgesetz ansetzen, erst symbolisch hinschreiben.
4. Werte mit Einheiten einsetzen und die Einheit mit der Newton-Beziehung umformen.
5. Das Ergebnis auf so viele signifikante Stellen runden, wie die Angaben haben.

## 🎓 Achtung

- **Resultierende Kraft** heißt: die Summe *aller* Kräfte. Gesucht ist hier nicht eine einzelne Kraft wie die Zugkraft gegen Reibung, sondern die Netto-Kraft.
- **Einheiten mitschreiben:** Ohne Einheit im Ergebnis gibt es in der Klausur Punktabzug, und die Angaben haben zwei signifikante Stellen. Das Ergebnis sollte also auch zwei haben.

## 🧩 Verständnisfrage

Wie ändert sich die resultierende Kraft, wenn ein zweiter Wagen mit doppelter Masse genauso stark beschleunigt werden soll? Begründe mit dem Gesetz.

## ➡️ Nächster Schritt

Löse die Aufgabe jetzt selbst nach dem Vorgehen, etwa 5–10 Minuten. Reicht das nicht, schreibe „tipp“. Für ein vorgerechnetes Beispiel schreibe „voll“. Zum Vergleichen schreibe „kurz“ oder schicke deinen Versuch.

## 🔒 Lösungen

Mit „lösung“ abrufen.
````

</details>


### M02-A

- **Kriterium:** Anschauliche und mathematische Erklärung getrennt; vorgerechnetes Beispiel einer anderen Aufgabe mit richtigem Ergebnis; Originalaufgabe nicht gelöst; kurze Schritte.
- **Eingabe:** `voll ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Anschauliche und mathematische Erklärung sind getrennt (anschaulich mit Bild/Analogie ohne Formel, mathematisch mit Gesetz und Formel)
  - ✔ Vorgerechnetes Beispiel einer anderen Aufgabe mit richtigem Ergebnis
  - ✔ Originalaufgabe nicht gelöst (kein Ergebnis 6,0 N, kein Einsetzen der Originalwerte)
  - ✔ Kurze Schritte (jeder Schritt höchstens drei Sätze Text vor seiner Gleichung)
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
**Modus:** Voll · Sprache: Deutsch

## 📋 Gegeben / Gesucht

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F_res | resultierende Kraft (gesucht) | ? | N |

## 🎯 Kernidee

Die resultierende Kraft und die Beschleunigung hängen über die Masse direkt zusammen: Wer zwei der drei Größen kennt, kennt die dritte.

## 🧠 Anschauliche Erklärung

Stell dir vor, du schiebst einen Einkaufswagen. Ist er leer, kommt er schon bei einem leichten Stoß schnell in Fahrt. Ist er voll beladen, musst du für dasselbe „In-Fahrt-Kommen“ deutlich kräftiger drücken. Die Masse ist also der Widerstand gegen Geschwindigkeitsänderung. Entscheidend ist dabei nur die Kraft, die nach allem Ziehen, Drücken und Bremsen übrig bleibt, die *resultierende* Kraft. Wie schnell der Wagen gerade fährt, spielt für diesen Zusammenhang keine Rolle, es zählt nur, wie stark sich die Geschwindigkeit ändert.

## 🧮 Mathematische Erklärung

**Zweites Newtonsches Gesetz (Grundgleichung der Mechanik):**

$$F_\mathrm{res} = m \cdot a$$

F_res ist die Summe aller Kräfte auf den Körper, m seine Masse, a seine Beschleunigung.

1. **Gültigkeit:** Es gilt für einen Körper mit konstanter Masse in einem Inertialsystem (ruhender oder gleichförmig bewegter Beobachter).
2. **Einheiten:** Das Newton ist genau so definiert, dass die Gleichung ohne Umrechnungsfaktor stimmt:

$$1\,\mathrm{N} = 1\,\mathrm{kg} \cdot \frac{\mathrm{m}}{\mathrm{s}^{2}}$$

3. **Grenzfall:** Ist F_res = 0, dann ist auch a = 0. Der Körper bleibt in Ruhe oder fährt gleichförmig weiter (erstes Newtonsches Gesetz als Sonderfall).
4. **Proportionalität:** Bei fester Masse wächst die Beschleunigung linear mit der Kraft. Bei fester Kraft halbiert eine doppelte Masse die Beschleunigung.

## 🧰 Werkzeug

Umstellen nach einer Größe: Auf beiden Seiten der Gleichung dieselbe Rechenoperation ausführen. Hier wird durch m geteilt, damit a allein steht:

$$F_\mathrm{res} = m \cdot a \quad \Rightarrow \quad a = \frac{F_\mathrm{res}}{m}$$

## 🗺 Vorgehen

1. Gegebene Größen herausschreiben, auch versteckte im Text, und prüfen, welche überhaupt gebraucht werden.
2. Alle Werte in SI-Einheiten umrechnen (kg, m/s², N).
3. F_res = m · a nach der gesuchten Größe umstellen (symbolisch).
4. Werte mit Einheiten einsetzen und ausrechnen.
5. Probe: Einheit und Größenordnung prüfen.

## 🔁 Gelöstes Beispiel

**Aufgabe:** Ein Lastenrad samt Fahrerin hat die Masse 120 kg. Die resultierende Kraft beim Anfahren beträgt 0,18 kN. Wie groß ist die Beschleunigung?

**Schritt 1 (Vorgehen 1): Größen herausschreiben.**
Gegeben sind m = 120 kg und F_res = 0,18 kN, gesucht ist a.

**Schritt 2 (Vorgehen 2): In SI-Einheiten umrechnen.**
Die Kraft steht in Kilonewton, die Formel braucht Newton.

$$F_\mathrm{res} = 0{,}18\,\mathrm{kN} = 180\,\mathrm{N}$$

⏸ Nach welcher Größe muss die Grundgleichung umgestellt werden, und wodurch teilst du dafür?

**Schritt 3 (Vorgehen 3): Umstellen.**
Gesucht ist a, also durch m teilen:

$$a = \frac{F_\mathrm{res}}{m}$$

⏸ Erwartest du eine eher große oder kleine Beschleunigung, wenn die Masse fast so groß ist wie die Kraft in Newton?

**Schritt 4 (Vorgehen 4): Einsetzen.**
Die Masse ist groß im Vergleich zur Kraft, deshalb wird die Beschleunigung moderat ausfallen:

$$a = \frac{180\,\mathrm{N}}{120\,\mathrm{kg}}$$

**✅ Ergebnis**

$$\boxed{a = 1{,}5\,\frac{\mathrm{m}}{\mathrm{s}^{2}}}$$

**🔎 Probe**

$$\frac{\mathrm{N}}{\mathrm{kg}} = \frac{\mathrm{kg} \cdot \mathrm{m}/\mathrm{s}^{2}}{\mathrm{kg}} = \frac{\mathrm{m}}{\mathrm{s}^{2}}$$

Größenordnung: 1,5 m/s² ist deutlich weniger als die Fallbeschleunigung (etwa 9,8 m/s²). Das passt zu einem schwer beladenen Rad.

Bisher gezeigt: umrechnen, umstellen, einsetzen und prüfen genügt für jeden Aufgabentyp dieser Art.

## 🚫 Falscher Weg

„Aus Ruhe“ verleitet dazu, eine Bewegungsgleichung (Weg, Zeit, Geschwindigkeit) aufzustellen. Für die Kraft braucht man aber nur Masse und Beschleunigung. Die Angabe ist hier nur Kontext und wird erst wichtig, wenn nach Geschwindigkeit oder Strecke gefragt wird.

## 🔄 Was wäre, wenn?

Wenn zusätzlich eine Reibungskraft wirkt, beschreibt m · a weiterhin nur die *resultierende* Kraft. Die Zugkraft müsste dann um die Reibungskraft größer sein, weil sie die Reibung zusätzlich überwinden muss.

## 🗂 Wiederholungskarte

**Frage:** Welche Kraft steht in F = m · a, die Zugkraft oder eine andere?
**Antwort:** Die resultierende Kraft, also die Summe aller Kräfte auf den Körper.

## 🧩 Verständnisfrage

Bräuchte der Wagen aus deiner Aufgabe eine andere resultierende Kraft, wenn er nicht aus der Ruhe startet, sondern schon mit 5 m/s fährt und genauso stark beschleunigt? Begründe.

## ➡️ Nächster Schritt

Löse jetzt deine Originalaufgabe selbst nach dem Vorgehen, etwa 5 Minuten auf Papier. Zum Vergleichen schreibe „kurz“ oder schicke deinen Versuch.

## 🔒 Lösungen

Mit „lösung“ abrufen.
````

</details>


### M03-A

- **Kriterium:** Anschauliche und formale Erklärung, Bedingungen, Abschnitt „So hilft es beim Lösen“ ohne gelöstes Beispiel, eine Verständnisfrage; Antwort geschützt.
- **Eingabe:** `thema ⏎ Warum ist die resultierende Kraft bei konstanter Geschwindigkeit null?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Anschauliche Erklärung vorhanden (mindestens ein Bild, eine Analogie oder ein Alltagsbezug ohne Formel)
  - ✔ Formale Erklärung vorhanden
  - ✔ Gültigkeitsbedingungen werden genannt
  - ✔ Abschnitt „So hilft es beim Lösen“ vorhanden und ohne gelöstes Beispiel
  - ✔ Genau eine Verständnisfrage
  - ✔ Antwort geschützt (Antwort der Verständnisfrage nicht offengelegt, unter 🔒 nur der Abrufsatz)
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
## 🧠 Idee

Eine Kraft ändert die Bewegung eines Körpers, nicht die Bewegung selbst. Ein Körper, der schon mit einer bestimmten Geschwindigkeit fährt, behält sie, solange nichts an ihm „zerrt“. Wenn die Geschwindigkeit konstant bleibt, gibt es also keine Änderung, die eine Kraft verursachen müsste. Es können durchaus Kräfte wirken, aber sie heben sich gegenseitig auf.

## 🧰 Werkzeug

Die Beschleunigung ist die zeitliche Ableitung der Geschwindigkeit, also wie schnell sich v ändert. Die Regel, die hier gebraucht wird, lautet: Die Ableitung einer Konstanten ist null.

$$v = \mathrm{const} \quad \Rightarrow \quad a = \frac{dv}{dt} = 0$$

## ✏️ Erklärung

**Schritt 1: Das zweite Newtonsche Gesetz.**
Die resultierende Kraft ist die Vektorsumme aller Kräfte auf den Körper. Sie bestimmt die Beschleunigung:

$$\vec{F}_\mathrm{res} = \sum_{i} \vec{F}_i = m \cdot \vec{a}$$

⏸ Was folgt für die rechte Seite, wenn sich die Geschwindigkeit nicht ändert?

**Schritt 2: Konstante Geschwindigkeit einsetzen.**
Ist die Geschwindigkeit konstant, dann ist die Beschleunigung null (siehe Werkzeug). Damit ist auch die rechte Seite null:

$$\vec{a} = \vec{0} \quad \Rightarrow \quad \vec{F}_\mathrm{res} = m \cdot \vec{0} = \vec{0}$$

Das ist genau das erste Newtonsche Gesetz (Trägheitsprinzip): Ohne resultierende Kraft bleibt ein Körper in Ruhe oder bewegt sich geradlinig gleichförmig.

**Schritt 3: Zahlenbeispiel.**
Eine Kiste wird mit 50 N waagerecht über den Boden gezogen und gleitet dabei mit konstanter Geschwindigkeit. Die Gleitreibung bremst sie mit 50 N entgegen der Bewegungsrichtung:

$$F_\mathrm{res} = 50\,\mathrm{N} - 50\,\mathrm{N} = 0\,\mathrm{N}$$

Die Zugkraft ist nötig, aber nur um die Reibung auszugleichen, nicht um die Kiste „am Laufen zu halten“.

**Gültigkeitsbedingungen:**
- „Konstante Geschwindigkeit“ bedeutet, dass Betrag **und** Richtung konstant bleiben, denn die Geschwindigkeit ist ein Vektor.
- Das Gesetz gilt in einem Inertialsystem, also in einem nicht beschleunigten Bezugssystem.
- Die Masse muss konstant sein.

Bisher gezeigt: Konstante Geschwindigkeit bedeutet a = 0, und daraus folgt mit Newton 2 direkt F_res = 0.

## 🛠 So hilft es beim Lösen

- **Signale im Aufgabentext:** „mit konstanter Geschwindigkeit“, „gleichförmig“, „ruht“, „im Gleichgewicht“, „Endgeschwindigkeit erreicht“.
- **Erster Schritt:** Alle Kräfte einzeichnen und dann die Summe der Kräfte gleich null setzen, für jede Richtung (x, y) einzeln.
- Daraus lässt sich eine unbekannte Kraft bestimmen, z. B. die Reibungs- oder die Zugkraft.

## 🎯 Kernidee

Kraft verursacht Geschwindigkeits**änderung**: Wo sich nichts ändert, ist die Summe aller Kräfte null.

## 🚫 Falscher Weg

„Der Körper bewegt sich vorwärts, also muss die Kraft nach vorne größer sein.“ Dieser Ansatz scheitert, weil eine größere Kraft nach vorne eine Beschleunigung erzeugen würde. Der Körper würde dann immer schneller werden, statt seine Geschwindigkeit zu halten.

## 🧩 Verständnisfrage

Ein Fallschirmspringer fällt mit konstanter Geschwindigkeit nach unten. Wie groß ist der Luftwiderstand im Vergleich zu seiner Gewichtskraft, und warum?

## ➡️ Nächster Schritt

Beantworte die Verständnisfrage auf Papier in 3 Minuten, mit einer Kräfteskizze und einer Gleichung. Schicke dann deine Antwort oder schreibe „lösung“.

## 🔒 Lösungen

Mit ‚lösung‘ abrufen.
````

</details>


### M04-A

- **Kriterium:** Vier bis sechs Leitfragen auf die Aufgabe zugeschnitten; nur Fragen, keine Gleichung, kein Zahlenwert, kein Ergebnis; keine sichtbare vollständige Lösung.
- **Eingabe:** `tipp ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Notiz:** Beobachtung ohne Kriteriumsverstoß: Leitfrage 5 („ergibt dein Produkt der Einheiten genau das?“) verrät, dass multipliziert wird. Siehe P3.
- **Teilaussagen (Prüfer 1):**
  - ✔ Vier bis sechs Leitfragen
  - ✔ Leitfragen sind auf die Aufgabe zugeschnitten
  - ✔ Nur Fragen: keine Gleichung in den Leitfragen
  - ✔ Kein Zahlenwert und kein Ergebnis in den Leitfragen (die Zahlen in der Gegeben/Gesucht-Tabelle sind nur die Aufgabenangaben, das Ergebnis 6,0 N fehlt)
  - ✔ Keine sichtbare vollständige Lösung
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
📋 **Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F_res | resultierende Kraft auf den Wagen | ? | N |

❓ **Leitfragen**

1. Ist mit „resultierende Kraft“ eine einzelne Kraft gemeint oder die Summe aller Kräfte, die auf den Wagen wirken?
2. Brauchst du die Angabe „aus Ruhe“ für die gesuchte Kraft, oder bräuchtest du sie nur für eine Geschwindigkeit oder eine Strecke?
3. Welches Grundgesetz der Mechanik verbindet die resultierende Kraft mit Masse und Beschleunigung?
4. Sind m und a schon in SI-Einheiten angegeben, sodass du ohne Umrechnung einsetzen kannst?
5. Aus welchen Basiseinheiten setzt sich das Newton zusammen, und ergibt dein Produkt der Einheiten genau das?
6. Wie viele signifikante Stellen haben die Angaben, und mit wie vielen gibst du deshalb das Ergebnis an?

➡️ **Nächster Schritt**
Beantworte die Fragen der Reihe nach auf Papier und rechne dann das Ergebnis aus. Dafür hast du höchstens 5 Minuten. Wenn du nicht weiterkommst, hast du drei Möglichkeiten:
- Schicke mir deine Antwort auf die Frage, an der du hängst.
- Schreibe noch einmal „tipp“, dann bekommst du engere Fragen.
- Schreibe „voll“, dann bekommst du ein vorgerechnetes Beispiel.

🔒 **Lösungen**
Mit ‚lösung‘ abrufen.
````

</details>


### M05-A

- **Kriterium:** Ersten Fehler mit Grund benennen; korrekt ab dort weiterrechnen; Richtiges nicht neu lösen.
- **Eingabe:** `check ⏎ Aufgabe: Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft? ⏎ Mein Versuch: F = m/a = 0,67 N`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Ersten Fehler mit Grund benennen
  - ✔ Korrekt ab dort weiterrechnen
  - ✔ Richtiges nicht neu lösen
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
## 🔍 Diagnose deines Versuchs

**Richtig:** Du hast die richtigen Angaben (m = 2,0 kg, a = 3,0 m/s²) erkannt und das zweite Newtonsche Gesetz als Ansatz gewählt.

**Erster Fehler:** Du hast F = m/a geschrieben, das ist falsch. Kraft ist Masse **mal** Beschleunigung, nicht geteilt.
**Fehlerart:** konzeptionell. Die Formel ist falsch erinnert.

Deine Einheit verrät den Fehler. Aus m/a ergibt sich kein Newton:

$$\frac{\mathrm{kg}}{\mathrm{m/s^2}} = \mathrm{kg} \cdot \frac{\mathrm{s^2}}{\mathrm{m}} \neq \mathrm{N}$$

## ✏️ Lösungsweg (ab dem Fehler)

**Schritt 1: Richtiges Gesetz ansetzen.**
Das zweite Newtonsche Gesetz sagt: Die resultierende Kraft ist das Produkt aus Masse und Beschleunigung. „Aus Ruhe“ ändert daran nichts, weil nur die Beschleunigung zählt.

$$F = m \cdot a$$

**Schritt 2: Werte einsetzen.**

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s^2}}$$

## ✅ Ergebnis

$$\boxed{F = 6{,}0\,\mathrm{N}}$$

## 🔎 Probe

- **Einheiten:** Das Produkt ergibt genau die Einheit Newton.

$$\mathrm{kg} \cdot \frac{\mathrm{m}}{\mathrm{s^2}} = \mathrm{N}$$

- **Plausibilität:** Mehr Masse oder mehr Beschleunigung braucht mehr Kraft. F muss also mit m und a **wachsen**. Bei m/a würde die Kraft mit größerer Beschleunigung kleiner werden, das ist unsinnig.

## ➡️ Nächster Schritt

Schreibe F = m · a dreimal auf. Stelle die Gleichung dann einmal nach a und einmal nach m um, jeweils mit Einheitenkontrolle. Das dauert etwa 5 Minuten. Danach kannst du deine Umformungen zum Prüfen schicken.
````

</details>


### M06-A

- **Kriterium:** Ohne Werkzeug: Achsen mit Größe und Einheit, markante Punkte als Tabelle, Verlauf, keine Textgrafik, lauffähiger TikZ- oder matplotlib-Block; mit Werkzeug: beschriftete Grafik. Kontrollmerkmal genannt.
- **Eingabe:** `skizze ⏎ Kräftediagramm eines Klotzes, der mit konstanter Geschwindigkeit über einen Tisch gezogen wird`
- **Urteil:** nicht bestanden (Prüfer 1: nicht bestanden)
- **Verletzte Teilaussage:** „Achsen mit Größe und Einheit“, „Verlauf“
- **Verletzende Stelle:** „Den Klotz als Rechteck auf eine waagerechte Linie (Tisch) zeichnen.“
- **Ursache:** Kriterium
- **Notiz:** Ein Kräftediagramm hat weder Achsen noch Verlauf; die Antwort folgt `modes/skizze.md` (Kräftetabelle Kraft | Symbol | Richtung | ausgeübt von). Der matplotlib-Block lief fehlerfrei (mit Agg-Backend geprüft). Siehe Vorschlag K1.
- **Teilaussagen (Prüfer 1):**
  - ✘ Achsen mit Größe und Einheit werden beschrieben
  - ✔ Markante Punkte als Tabelle (bei Kräftediagramm: Kräftetabelle)
  - ✘ Verlauf wird beschrieben
  - ✔ Keine Textgrafik
  - ✔ Lauffähiger TikZ- oder matplotlib-Block
  - ✔ Kontrollmerkmal genannt
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
# 🖊 Skizze: Klotz mit konstanter Geschwindigkeit

## 📋 Gegeben / Gesucht

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| v | Geschwindigkeit des Klotzes | konstant | m/s |
| a | Beschleunigung | 0 (folgt aus v = konstant) | m/s² |
| gesucht | Kräftediagramm (Freikörperbild) des Klotzes | – | – |

⚠ **Annahme:** Die Zugkraft wirkt waagerecht nach rechts, und der Tisch ist waagerecht.

## 🖊 Skizze

**1. Klotz und Tisch zeichnen**
- Den Klotz als Rechteck auf eine waagerechte Linie (Tisch) zeichnen.
- Einen Punkt in die Mitte setzen. Dort beginnen alle Kraftpfeile.

**2. Vier Kräfte eintragen**

| Kraft | Symbol | Richtung | ausgeübt von |
|---|---|---|---|
| Gewichtskraft | F_G | senkrecht nach unten | Erde |
| Normalkraft | F_N | senkrecht nach oben | Tisch |
| Zugkraft | F_Z | waagerecht nach rechts (Bewegungsrichtung) | Seil oder Hand |
| Gleitreibungskraft | F_R | waagerecht nach links (gegen die Bewegung) | Tisch |

**3. Pfeillängen festlegen**
- Die Geschwindigkeit ist konstant. Daher ist die Beschleunigung null, und die Kräfte heben sich paarweise auf (1. Newtonsches Gesetz).
- Die Pfeile von F_G und F_N sind gleich lang.
- Die Pfeile von F_Z und F_R sind gleich lang.

$$F_\mathrm{N} = F_\mathrm{G}, \qquad F_\mathrm{Z} = F_\mathrm{R}$$

**4. Zur Bewegung**
- v ist **keine Kraft**. Wenn du die Bewegungsrichtung zeigen willst, schreibe sie nur als Text neben den Klotz, zum Beispiel „v = konst. →“.
- Eine Kraft „in Bewegungsrichtung“, die den Klotz am Laufen hält, gibt es nicht.

**Code zum Selbsterzeugen (matplotlib):**

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(6, 5))
ax.add_patch(Rectangle((-1, -0.5), 2, 1, fill=False, lw=2))  # Klotz
ax.plot([-3.5, 3.5], [-0.5, -0.5], color="black", lw=1)       # Tisch
ax.plot(0, 0, "ko")                                            # Schwerpunkt

def pfeil(dx, dy, text, tx, ty):
    ax.annotate("", xy=(dx, dy), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=2))
    ax.text(tx, ty, text, fontsize=12)

pfeil(0, -2, "F_G", 0.15, -2.0)    # Gewichtskraft
pfeil(0,  2, "F_N", 0.15,  1.9)    # Normalkraft, gleich lang wie F_G
pfeil( 2.2, 0, "F_Z",  2.0, 0.15)  # Zugkraft
pfeil(-2.2, 0, "F_R", -2.4, 0.15)  # Reibungskraft, gleich lang wie F_Z
ax.text(1.2, 0.7, "v = konst. ->", fontsize=10, color="gray")

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.6, 2.6)
ax.set_aspect("equal")
ax.axis("off")
plt.show()
```

## 🔎 Kontrolle

- **Kräftegleichgewicht:** Die gegenüberliegenden Pfeile sind jeweils gleich lang. Wären sie verschieden lang, gäbe es eine resultierende Kraft. Dann würde der Klotz beschleunigen, und das widerspricht „konstante Geschwindigkeit“.
- **Zählprobe:** Es sind genau 4 Kräfte. Zu jeder Kraft gibt es einen Körper, der sie ausübt (Erde, Tisch, Seil, Tisch). Eine Kraft ohne solchen Körper gehört nicht ins Bild.

## ➡️ Nächster Schritt

Zeichne das Freikörperbild in 5 Minuten selbst auf Papier, ohne hinzusehen, und vergleiche es dann mit der Tabelle oben.
````

</details>


### M07-A

- **Kriterium:** Deutsche Klausur-Lösung mit richtigem Ergebnis, Umformung als eigene Zeile vor dem Zahlenwert, genau eine Anmerkung; ohne zusätzlichen Lehrvortrag; ungefähr ein Bildschirm.
- **Eingabe:** `kurz ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Deutsche Klausur-Lösung
  - ✔ Richtiges Ergebnis (6,0 N; 2,0 kg · 3,0 m/s² = 6,0 N)
  - ✔ Umformung bzw. Formel steht als eigene Zeile vor dem Zahlenwert
  - ✔ Genau eine Anmerkung
  - ✔ Ohne zusätzlichen Lehrvortrag (höchstens zwei Sätze außerhalb von Klausur-Lösung, Ergebnis und Anmerkung)
  - ✔ Ungefähr ein Bildschirm (höchstens 35 dargestellte Zeilen)
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
## 🇩🇪 Klausur-Lösung

Ansatz: 2. Newtonsches Gesetz (Grundgleichung der Mechanik), die resultierende Kraft ist Masse mal Beschleunigung.

$$F_\mathrm{res} = m \cdot a$$

Gegeben: m = 2,0 kg, a = 3,0 m/s². Einsetzen:

$$F_\mathrm{res} = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^2} = 6{,}0\,\mathrm{kg}\,\frac{\mathrm{m}}{\mathrm{s}^2} = 6{,}0\,\mathrm{N}$$

Antwortsatz: Die resultierende Kraft auf den Wagen beträgt 6,0 N.

## ✅ Ergebnis

$$\boxed{F_\mathrm{res} = 6{,}0\,\mathrm{N}}$$

## 💡 Anmerkung

„Aus Ruhe“ spielt für die Kraft keine Rolle, denn nach F = m · a hängt sie nur von der Beschleunigung ab und nicht von der Geschwindigkeit.
````

</details>


### M08-A

- **Kriterium:** Richtige vollständige Lösung mittlerer Tiefe; keine Übungen; eine Verständnisfrage, Antwort geschützt.
- **Eingabe:** `mittel ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** nicht bestanden (Prüfer 1: nicht bestanden)
- **Verletzte Teilaussage:** „keine Übungen“
- **Verletzende Stelle:** „Rechne ohne Vorlage auf Papier (etwa 5 Minuten): Welche Beschleunigung hat ein 4,0-kg-Wagen bei derselben Kraft? Schick mir dann deinen Versuch.“
- **Ursache:** Prompt
- **Notiz:** Die neue Aufgabe steht im „➡️ Nächster Schritt“. Siehe Vorschlag P1.
- **Teilaussagen (Prüfer 1):**
  - ✔ Richtige vollständige Lösung (6,0 N)
  - ✔ Erklärung mittlerer Tiefe
  - ✘ Keine Übungen
  - ✔ Genau eine Verständnisfrage, Antwort geschützt
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F | resultierende Kraft (gesucht) | ? | N |

**🗺 Lösungsplan**

1. Passendes Gesetz wählen: Kraft und Beschleunigung verknüpfen.
2. Einheiten prüfen.
3. Werte einsetzen und runden.

**🧠 Idee**

Eine resultierende Kraft ist die Summe aller Kräfte auf den Wagen. Sie ändert seine Geschwindigkeit. Je schwerer der Wagen und je stärker er beschleunigt, desto größer muss diese Kraft sein. Das beschreibt das 2. Newtonsche Gesetz.

**✏️ Lösungsweg**

**Schritt 1: Gesetz wählen.**
Gesucht ist eine Kraft, gegeben sind Masse und Beschleunigung. Das 2. Newtonsche Gesetz verbindet genau diese drei Größen:

$$F = m \cdot a$$

⏸ Spielt die Angabe „aus Ruhe“ für die Kraft eine Rolle?

**Schritt 2: Einheiten prüfen.**
Nein: Die Kraft hängt nur von der Beschleunigung ab, nicht von der Geschwindigkeit. Masse in kg und Beschleunigung in m/s² sind SI-Einheiten. Ihr Produkt ist direkt Newton:

$$1\,\mathrm{kg} \cdot 1\,\frac{\mathrm{m}}{\mathrm{s}^{2}} = 1\,\mathrm{N}$$

⏸ Wie viele signifikante Stellen darf das Ergebnis haben?

**Schritt 3: Werte einsetzen.**
Beide Angaben haben zwei signifikante Stellen, also bekommt auch das Ergebnis zwei:

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^{2}} = 6{,}0\,\mathrm{N}$$

**✅ Ergebnis**

$$\boxed{F = 6{,}0\,\mathrm{N}}$$

**🔎 Probe**

- **Einheit:** kg · m/s² = N ✔
- **Grenzfall:** Bei a = 0 ergibt sich F = 0. Ohne resultierende Kraft gibt es keine Beschleunigung ✔
- **Größenordnung:** 6 N entsprechen etwa der Gewichtskraft von 600 g. Für einen kleinen Wagen ist das plausibel ✔

**🇩🇪 Klausur-Lösung**

Nach dem 2. Newtonschen Gesetz gilt:

$$F = m \cdot a$$

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^{2}} = 6{,}0\,\mathrm{N}$$

Antwort: Die resultierende Kraft auf den Wagen beträgt 6,0 N.

**🎓 Klausur-Tipp**

- „Aus Ruhe“ ist hier eine Ablenkung. Für die Kraft zählt nur a, nicht v.
- Gemeint ist die *resultierende* Kraft. Wirkt zusätzlich Reibung, muss die Zugkraft größer sein als 6,0 N.
- Für volle Punktzahl gehören dazu: das Gesetz nennen, die Werte mit Einheiten einsetzen, das Ergebnis mit Einheit angeben und einen Antwortsatz schreiben.

**🧩 Verständnisfrage**

Der Wagen startet nicht aus Ruhe, sondern fährt schon mit 5 m/s und beschleunigt weiterhin mit 3,0 m/s². Ändert sich die resultierende Kraft? Begründe in einem Satz.

**➡️ Nächster Schritt**

Rechne ohne Vorlage auf Papier (etwa 5 Minuten): Welche Beschleunigung hat ein 4,0-kg-Wagen bei derselben Kraft? Schick mir dann deinen Versuch.

**🔒 Lösungen**

Mit „lösung“ abrufen.
````

</details>


### M09-A

- **Kriterium:** Richtige Lösung auf dem Hauptweg plus höchstens zwei andere Wege mit demselben Ergebnis, je mit „wann besser“; kein erfundener Weg, wenn es keinen sinnvollen gibt.
- **Eingabe:** `lang ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** nicht bestanden (Prüfer 1: nicht bestanden)
- **Verletzte Teilaussage:** „kein erfundener Weg, wenn es keinen sinnvollen gibt“
- **Verletzende Stelle:** „Wann besser: Dieser Weg lohnt sich, wenn eine Strecke statt einer Beschleunigung gegeben ist. Hier ist er ein Umweg.“
- **Ursache:** Prompt
- **Notiz:** Beide Nebenwege führen nicht gegebene Größen ein (Zeit t, Strecke s) und sind länger als der Hauptweg, obwohl `modes/lang.md` „jeder kürzer als der Hauptweg“ verlangt. Siehe Vorschlag P2.
- **Teilaussagen (Prüfer 1):**
  - ✔ Richtige Lösung auf dem Hauptweg (6,0 N)
  - ✔ Höchstens zwei andere Wege
  - ✔ Die anderen Wege führen zum selben Ergebnis
  - ✔ Jeder andere Weg nennt „wann besser“
  - ✘ Kein erfundener Weg, wenn es keinen sinnvollen gibt
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
📋 **Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F | resultierende Kraft (gesucht) | ? | N |

🗺 **Lösungsplan**
1. Passendes Gesetz wählen: Kraft und Beschleunigung verknüpfen.
2. Gleichung symbolisch aufschreiben.
3. Werte einsetzen und die Einheit prüfen.
4. Auf die passende Stellenzahl runden.

🧠 **Idee**
Eine resultierende Kraft ist die Ursache dafür, dass sich die Geschwindigkeit eines Körpers ändert. Je schwerer der Wagen ist, desto mehr Kraft braucht man für dieselbe Beschleunigung. Das zweite Newtonsche Gesetz sagt genau das: Kraft gleich Masse mal Beschleunigung. Ob der Wagen aus Ruhe startet, spielt für die Kraft keine Rolle. Die Kraft hängt nur von der Beschleunigung ab, nicht von der momentanen Geschwindigkeit.

✏️ **Lösungsweg**

⏸ Welches Gesetz verbindet Kraft, Masse und Beschleunigung?

**Schritt 1: Gesetz wählen.**
Das zweite Newtonsche Gesetz verbindet die resultierende Kraft mit Masse und Beschleunigung. Es gilt hier, weil die Masse des Wagens konstant ist.

$$F = m \cdot a$$

**Schritt 2: Gleichung prüfen.**
F steht schon allein auf einer Seite, ein Umstellen ist nicht nötig. Die Angabe „aus Ruhe“ wird für die Kraft nicht gebraucht.

⏸ Welche Einheit kommt heraus, wenn du kg mit m/s² multiplizierst?

**Schritt 3: Werte einsetzen.**
Masse und Beschleunigung sind schon in SI-Einheiten gegeben, du musst also nichts umrechnen.

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^{2}} = 6{,}0\,\frac{\mathrm{kg}\,\mathrm{m}}{\mathrm{s}^{2}}$$

**Schritt 4: Einheit benennen und runden.**
Ein Newton ist genau ein kg·m/s². Beide Angaben haben 2 signifikante Stellen, also bekommt auch das Ergebnis 2 Stellen.

$$1\,\mathrm{N} = 1\,\frac{\mathrm{kg}\,\mathrm{m}}{\mathrm{s}^{2}}$$

Bisher gezeigt: Mit F = m·a und den gegebenen Werten folgt die Kraft direkt.

✅ **Ergebnis**

$$\boxed{F = 6{,}0\,\mathrm{N}}$$

🔎 **Probe**
- **Einheiten:** Die Rechnung kg · m/s² ergibt N, das passt zu einer Kraft.
- **Grenzfall:** Bei a = 0 wäre F = 0. Ohne Beschleunigung gibt es keine resultierende Kraft, das ist physikalisch richtig.
- **Größenordnung:** 6 N entsprechen etwa der Gewichtskraft von 0,6 kg. Für einen leichten Wagen ist das plausibel.

🔀 **Alternativer Weg**

**Weg A: über den Impuls.**
Aus Ruhe gilt nach der Zeit t für die Geschwindigkeit v = a·t. Der Impuls ist dann p = m·v. Die Kraft ist die Impulsänderung pro Zeit:

$$F = \frac{\Delta p}{\Delta t} = \frac{m \cdot a \cdot t - 0}{t} = m \cdot a = 6{,}0\,\mathrm{N}$$

Wann besser: Dieser Weg ist allgemeiner, denn er funktioniert auch bei Stößen oder wenn sich die Masse ändert.

**Weg B: über die Energie.**
Nach der Strecke s gilt v² = 2·a·s. Die Arbeit der Kraft wird vollständig zu kinetischer Energie:

$$F \cdot s = \frac{1}{2}\, m \cdot 2 a s \quad \Rightarrow \quad F = m \cdot a = 6{,}0\,\mathrm{N}$$

Wann besser: Dieser Weg lohnt sich, wenn eine Strecke statt einer Beschleunigung gegeben ist. Hier ist er ein Umweg.

🇩🇪 **Klausur-Lösung**

Ansatz: 2. Newtonsches Gesetz.

$$F = m \cdot a$$

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^{2}} = 6{,}0\,\mathrm{N}$$

Antwort: Die resultierende Kraft auf den Wagen beträgt 6,0 N.

🎓 **Klausur-Tipp**
- **Stolperstein:** Die Angabe „aus Ruhe“ ist hier eine Ablenkung. Lass dich nicht verleiten, eine Geschwindigkeit oder Zeit auszurechnen.
- **Stolperstein:** Schreib die Einheit „N“ hin und nicht nur „6“. Eine fehlende Einheit kostet in deutschen Klausuren häufig Punkte.
- **Für volle Punktzahl:** Schreib üblicherweise das Gesetz als Formel, das Einsetzen mit Einheiten und einen Antwortsatz hin.

🧩 **Verständnisfrage**
Was ändert sich an der resultierenden Kraft, wenn der Wagen nicht aus Ruhe startet, sondern schon mit 5 m/s fährt und weiterhin mit 3,0 m/s² beschleunigt?

➡️ **Nächster Schritt**
Rechne in 5 Minuten auf Papier: Welche Beschleunigung erfährt ein 4,0-kg-Wagen bei derselben Kraft? Schicke mir danach deinen Versuch.

🔒 **Lösungen**
Mit „lösung“ abrufen.
````

</details>


### M10-A

- **Kriterium:** Kompakte richtige Lösung; Klausur-Tipp mit Punktsicherung, zwei typischen Punktverlusten, Kontrollweg und Zeitangabe; keine Behauptung über Bewertungskriterien einer bestimmten Hochschule.
- **Eingabe:** `klausur ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Kompakte richtige Lösung
  - ✔ Klausur-Tipp enthält Punktsicherung (was für volle Punktzahl hingeschrieben wird)
  - ✔ Klausur-Tipp nennt zwei typische Punktverluste
  - ✔ Klausur-Tipp nennt einen Kontrollweg
  - ✔ Klausur-Tipp nennt eine Zeitangabe
  - ✔ Keine Behauptung über Bewertungskriterien einer bestimmten Hochschule
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
## 📋 Gegeben / Gesucht

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| a | Beschleunigung | 3,0 | m/s² |
| F | resultierende Kraft (gesucht) | ? | N |

## 🗺 Lösungsplan

1. Newtons zweites Gesetz ansetzen.
2. Werte einsetzen und Einheiten zusammenfassen.
3. Ergebnis mit zwei signifikanten Stellen angeben.

## ✏️ Lösungsweg

**Schritt 1: Ansatz.**
Die resultierende Kraft ist das Produkt aus Masse und Beschleunigung (2. Newtonsches Axiom).

$$F = m \cdot a$$

**Schritt 2: Einsetzen.**
Die Einheit kg mal m/s² ergibt Newton.

$$F = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\mathrm{\frac{m}{s^2}} = 6{,}0\,\mathrm{N}$$

## ✅ Ergebnis

$$\boxed{F = 6{,}0\,\mathrm{N}}$$

## 🇩🇪 Klausur-Lösung

Nach dem 2. Newtonschen Axiom gilt:

$$F = m \cdot a = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\mathrm{\frac{m}{s^2}} = 6{,}0\,\mathrm{N}$$

Antwortsatz: Die resultierende Kraft auf den Wagen beträgt 6,0 N.

## 🎓 Klausur-Tipp

- **Für volle Punktzahl:** Formel allgemein hinschreiben, Werte mit Einheiten einsetzen, Ergebnis mit Einheit angeben und einen Antwortsatz formulieren.
- **Häufiger Punktverlust 1:** „Aus Ruhe“ wird als Größe missverstanden. Hier ist es eine Ablenkung, denn für F braucht man nur m und a.
- **Häufiger Punktverlust 2:** Die Einheit fehlt oder ist falsch, z. B. „6,0 kg·m/s“ statt N. Beachte: 1 N = 1 kg·m/s².
- **Schnelle Kontrolle:** Die Einheit muss kg·m/s² = N ergeben. Doppelte Masse ergibt bei gleicher Beschleunigung die doppelte Kraft.
- **Zeit:** etwa 1–2 Minuten.

## ➡️ Nächster Schritt

Löse in 3 Minuten selbst: Ein Körper mit 5,0 kg erfährt eine resultierende Kraft von 12 N. Wie groß ist seine Beschleunigung? Schicke danach deinen Versuch.
````

</details>


### G03

- **Kriterium:** Einmalige Klausur-Lösung, danach wieder Tipp; Status zeigt tatsächlichen und gespeicherten Modus.
- **Eingabe:** `!an tipp ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?` → `!kurz` → `Ein Körper mit 5,0 kg erfährt eine resultierende Kraft von 20 N. Wie groß ist seine Beschleunigung?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Einmalige Klausur-Lösung: Nachricht 2 liefert im Modus Kurz die Klausur-Lösung zu Aufgabe 1 mit dem korrekten Ergebnis 6,0 N (2,0 kg · 3,0 m/s² = 6,0 N)
  - ✔ Die Klausur-Lösung gilt nur einmal: Der Kurz-Modus wird ausdrücklich als Einzelbefehl für diese Nachricht ausgewiesen
  - ✔ Danach wieder Tipp: Nachricht 3 antwortet im Modus Tipp mit Leitfragen, ohne Lösung (kein Ergebnis 4,0 m/s², keine Gleichung, keine umgestellte Formel)
  - ✔ Status zeigt tatsächlichen und gespeicherten Modus (Nachricht 2: Kurz tatsächlich, Tipp gespeichert; Nachricht 3: Tipp, als Dauermodus gekennzeichnet)
- **Antwort:** vollständig, wörtlich

<details><summary>Nachricht 1: !an tipp</summary>

````markdown
**Status:** Modus Tipp · Dauermodus: Tipp (`!aus` beendet ihn) · Sprache: Deutsch

**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung des Wagens | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F_res | resultierende Kraft auf den Wagen | gesucht | N |

**❓ Leitfragen**

1. Welche Größe soll am Ende herauskommen, und in welcher Einheit gibt man eine Kraft an?
2. Brauchst du die Angabe „aus Ruhe“ für die Kraft, oder zählt nur die Beschleunigung?
3. Welches Grundgesetz der Mechanik verbindet Kraft, Masse und Beschleunigung eines Körpers?
4. Was bedeutet „resultierende“ Kraft, und ist genau diese Kraft die Kraft in jenem Gesetz?
5. Passen die Einheiten kg und m/s² direkt zur Krafteinheit, oder musst du vorher etwas umrechnen?
6. Soll die Kraft bei doppelter Masse und gleicher Beschleunigung größer oder kleiner werden? Passt dein Ergebnis zu dieser Erwartung?

**➡️ Nächster Schritt**
Beantworte die Fragen der Reihe nach auf Papier und rechne dann weiter, höchstens 5 Minuten. Wenn du nicht weiterkommst, hast du drei Möglichkeiten: Schicke mir deine Antwort auf die Frage, an der du hängst. Schreibe noch einmal „tipp“ für engere Fragen. Oder schreibe „voll“ für ein vorgerechnetes Beispiel.

**🔒 Lösungen**
Mit „lösung“ abrufen.
````

</details>

<details><summary>Nachricht 2: !kurz</summary>

````markdown
**Status:** Modus Kurz (nur diese Nachricht) · Dauermodus: Tipp bleibt gespeichert · Sprache: Deutsch

**🇩🇪 Klausur-Lösung**

Ansatz: zweites Newtonsches Gesetz (Grundgleichung der Mechanik) für die resultierende Kraft auf den Wagen:

$$F_\mathrm{res} = m \cdot a$$

Einsetzen:

$$F_\mathrm{res} = 2{,}0\,\mathrm{kg} \cdot 3{,}0\,\frac{\mathrm{m}}{\mathrm{s}^2} = 6{,}0\,\frac{\mathrm{kg}\,\mathrm{m}}{\mathrm{s}^2} = 6{,}0\,\mathrm{N}$$

Antwortsatz: Die resultierende Kraft auf den Wagen beträgt 6,0 N in Richtung der Beschleunigung.

**✅ Ergebnis**

$$\boxed{F_\mathrm{res} = 6{,}0\,\mathrm{N}}$$

**💡 Anmerkung**
Die Angabe „aus Ruhe“ spielt für die Kraft keine Rolle, denn die Kraft hängt nur von Masse und Beschleunigung ab und nicht von der Geschwindigkeit.
````

</details>

<details><summary>Nachricht 3: Ein Körper mit 5,0 kg erfährt eine resultierende Kraft von 20 N. Wie groß ist seine Beschleunigung?</summary>

````markdown
**Status:** Modus Tipp (Dauermodus) · Sprache: Deutsch

**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Körpers | 5,0 | kg |
| F_res | resultierende Kraft auf den Körper | 20 | N |
| a | Beschleunigung des Körpers | gesucht | m/s² |

**❓ Leitfragen**

1. Welche Größe soll diesmal herauskommen, und in welcher Einheit gibt man sie an?
2. Welches Gesetz aus der Wagen-Aufgabe verbindet auch hier Kraft, Masse und Beschleunigung?
3. Ist die 20 N schon die resultierende Kraft, oder müsstest du noch andere Kräfte verrechnen?
4. Welche Größe steht diesmal allein auf einer Seite, und wie stellst du das Gesetz nach ihr um?
5. Wie schreibst du die Einheit N in Basiseinheiten, damit am Ende die Einheit der Beschleunigung herauskommt?
6. Soll die Beschleunigung bei gleicher Kraft und größerer Masse größer oder kleiner werden? Passt dein Ergebnis zu dieser Erwartung?

**➡️ Nächster Schritt**
Beantworte die Fragen der Reihe nach auf Papier und rechne dann weiter, höchstens 5 Minuten. Wenn du nicht weiterkommst, hast du drei Möglichkeiten: Schicke mir deine Antwort auf die Frage, an der du hängst. Schreibe noch einmal „tipp“ für engere Fragen. Oder schreibe „voll“ für ein vorgerechnetes Beispiel.

**🔒 Lösungen**
Mit „lösung“ abrufen.
````

</details>


### G04

- **Kriterium:** Gezielte Rückmeldung und nächster Hinweis, keine vollständige Lösung.
- **Eingabe:** `!an tipp ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft?` → `Mein Versuch: Newton 2 sagt F = m · a. Aber spielt es eine Rolle, dass er aus der Ruhe startet? Ich weiß nicht, wie ich weitermache.`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Gezielte Rückmeldung auf den Versuch des Lernenden
  - ✔ Nächster Hinweis, der den Lernenden weiterbringt (zur offenen Frage „aus Ruhe“ und zum Einsetzen)
  - ✔ Keine vollständige Lösung: das Ergebnis 6,0 N und eingesetzte Zahlenwerte stehen nicht in der zweiten Antwort
- **Antwort:** vollständig, wörtlich

<details><summary>Nachricht 1: !an tipp</summary>

````markdown
**Status:** Modus Tipp · Dauermodus: tipp · Sprache: Deutsch

**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| F_res | resultierende Kraft (gesucht) | ? | ? |

**❓ Leitfragen**

1. Welche Größe soll am Ende herauskommen, und in welcher Einheit gibt man eine Kraft an?
2. Brauchst du die Angabe „aus Ruhe“ für die gesuchte Kraft überhaupt?
3. Welches Grundgesetz der Mechanik verknüpft Kraft, Masse und Beschleunigung miteinander?
4. Warum fragt die Aufgabe nach der *resultierenden* Kraft und nicht nach irgendeiner einzelnen Kraft am Wagen?
5. Stehen Masse und Beschleunigung schon in SI-Einheiten, sodass du direkt einsetzen kannst?
6. Welche Größenordnung erwartest du: einige Newton oder einige hundert Newton?

**➡️ Nächster Schritt**

Beantworte die Fragen der Reihe nach auf Papier und rechne dann die Aufgabe zu Ende. Nimm dir höchstens 10 Minuten. Wenn du hängst, hast du drei Möglichkeiten:
- Schicke mir deine Antwort auf die Frage, an der du feststeckst.
- Schreibe noch einmal „tipp“, dann bekommst du engere Fragen.
- Schreibe „voll“, dann bekommst du ein vorgerechnetes Beispiel.

**🔒 Lösungen**

Mit „lösung“ abrufen.
````

</details>

<details><summary>Nachricht 2: Mein Versuch: Newton 2 sagt F = m · a. Aber spielt es eine Rolle, dass er aus der Ruhe startet? Ich weiß nicht, wie ich weitermache.</summary>

````markdown
**Status:** Modus Tipp · Dauermodus: tipp · Sprache: Deutsch

**🔍 Diagnose deines Versuchs**

Leitfrage 3: **richtig.** Das zweite Newtonsche Gesetz verknüpft genau die gesuchte Kraft mit den beiden gegebenen Größen:

$$F = m \cdot a$$

**❓ Zu deiner Frage „aus Ruhe“**

Prüfe es selbst an deiner eigenen Gleichung:

1. Steht in F = m · a eine Geschwindigkeit, oder nur Masse und Beschleunigung?
2. Würde sich die Beschleunigung des Wagens ändern, wenn er schon mit 5 m/s fahren würde und dann genauso stark beschleunigt?

**❓ Weiter: so geht es los**

3. Welche Zahlenwerte für m und a setzt du in deine Gleichung ein?
4. Was ergibt die Einheit kg · m/s², und wie heißt sie kürzer?

**➡️ Nächster Schritt**

Beantworte die Fragen 1 und 2 für dich, dann setze ein und rechne das Ergebnis mit Einheit aus. Das dauert etwa 3 Minuten. Schicke mir dein Ergebnis, oder schreibe zum Vergleichen „lösung“.

**🔒 Lösungen**

Mit „lösung“ abrufen.
````

</details>


### G14

- **Kriterium:** Zweites Mal engere Fragen zur ersten offenen Teilaufgabe, drittes Mal Verweis auf `voll`.
- **Eingabe:** `tipp ⏎ Ein Wagen mit 2,0 kg beschleunigt aus Ruhe 4,0 s lang mit 3,0 m/s². a) Wie groß ist die resultierende Kraft? b) Welche Geschwindigkeit hat er am Ende? c) Welche Strecke legt er zurück?` → `tipp` → `tipp`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Notiz:** Beobachtung: Leitfrage 5 der ersten Antwort fragt zwei Dinge auf einmal (Regel „Eine Frage, ein Gedanke“ in `modes/tipp.md`). Kein Kriteriumsverstoß.
- **Teilaussagen (Prüfer 1):**
  - ✔ Beim zweiten „tipp“ kommen engere Fragen zur ersten offenen Teilaufgabe (a)
  - ✔ Beim dritten „tipp“ erfolgt der Verweis auf `voll` (statt weiterer Fragen)
  - ✔ Keines der Ergebnisse (6,0 N, 12 m/s, 24 m) ist in den Tipp-Antworten sichtbar
  - ✔ Keine Gleichung oder umgestellte Formel in den Tipp-Antworten
- **Antwort:** vollständig, wörtlich

<details><summary>Nachricht 1: tipp</summary>

````markdown
**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| a | Beschleunigung | 3,0 | m/s² |
| t | Dauer der Beschleunigung | 4,0 | s |
| F | a) resultierende Kraft | ? | N |
| v | b) Geschwindigkeit am Ende | ? | m/s |
| s | c) zurückgelegte Strecke | ? | m |

**❓ Leitfragen**

1. Welche drei Größen sollen am Ende herauskommen, und in welcher Einheit jeweils?
2. Welche Größe steckt nur in den Worten „aus Ruhe“, und welchen Wert hat sie?
3. Welches Gesetz verbindet bei a) die Kraft mit Masse und Beschleunigung?
4. Welche Bewegungsart folgt daraus, dass die Beschleunigung über die ganzen 4,0 s gleich bleibt?
5. Welche Bewegungsgleichung dieser Bewegungsart enthält genau v, die Anfangsgeschwindigkeit, a und t, und welche enthält s statt v?
6. Ergibt deine Rechnung am Ende bei a) wirklich Newton, bei b) m/s und bei c) m?

**➡️ Nächster Schritt**
Beantworte die Fragen der Reihe nach auf Papier. Nimm dir dafür höchstens 10 Minuten und rechne danach a) bis c) aus.
Wenn du hängst, hast du drei Möglichkeiten:
- Schicke mir deine Antwort auf die Frage, bei der du feststeckst.
- Schreibe noch einmal „tipp“ für engere Fragen.
- Schreibe „voll“ für ein vorgerechnetes Beispiel.

**🔒 Lösungen**
Mit ‚lösung‘ abrufen.
````

</details>

<details><summary>Nachricht 2: tipp</summary>

````markdown
**❓ Leitfragen: engere Fragen zu a)**

1. Welche zwei der drei gegebenen Größen brauchst du für die Kraft, und welche spielt bei a) keine Rolle?
2. Muss der Wagen stärker oder schwächer angeschoben werden, wenn er bei gleicher Beschleunigung doppelt so schwer ist?
3. Wie musst du die zwei Größen aus Frage 1 verknüpfen, damit aus kg und m/s² die Einheit der Kraft entsteht?

**➡️ Nächster Schritt**
Beantworte diese drei Fragen auf Papier und rechne a) aus, höchstens 5 Minuten. Schicke mir dann dein Ergebnis für a); danach geht es mit b) weiter. Kommst du immer noch nicht weiter, schreibe „voll“: Dann bekommst du ein vorgerechnetes Beispiel einer ähnlichen Aufgabe.

**🔒 Lösungen**
Mit ‚lösung‘ abrufen.
````

</details>

<details><summary>Nachricht 3: tipp</summary>

````markdown
**❓ Leitfragen**

Weitere Fragen helfen dir hier wahrscheinlich nicht mehr. Ein vorgerechnetes Beispiel bringt dich jetzt schneller weiter.

**➡️ Nächster Schritt**
Schreibe „voll“. Du bekommst dann eine ähnliche Aufgabe mit anderen Zahlen, Schritt für Schritt vorgerechnet. Lies sie in etwa 10 Minuten durch und löse danach deine Aufgabe nach demselben Vorgehen.

**🔒 Lösungen**
Mit ‚lösung‘ abrufen.
````

</details>


### G18

- **Kriterium:** Höchstens die ersten zwei erklären; keine Originalergebnisse offenlegen.
- **Eingabe:** `erklär ⏎ 1) Ein Wagen mit 2,0 kg beschleunigt aus Ruhe mit 3,0 m/s². Wie groß ist die resultierende Kraft? ⏎ 2) Ein Körper fällt aus 5,0 m Höhe frei (g = 9,81 m/s²). Mit welcher Geschwindigkeit trifft er auf? ⏎ 3) Eine Feder mit D = 200 N/m wird um 5,0 cm gedehnt. Welche Kraft ist dafür nötig?`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Notiz:** Beobachtung: „🔒 Lösungen“ steht vor „➡️ Nächster Schritt“; laut Antwortvorlage gehört 🔒 ganz ans Ende. Kein Kriteriumsverstoß.
- **Teilaussagen (Prüfer 1):**
  - ✔ Höchstens die ersten zwei Aufgaben werden erklärt
  - ✔ Keine Originalergebnisse werden offengelegt (6,0 N, 9,9 m/s, 10 N)
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
# Aufgabe 1: Resultierende Kraft auf einen Wagen

**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| m | Masse des Wagens | 2,0 | kg |
| v0 | Anfangsgeschwindigkeit („aus Ruhe“) | 0 | m/s |
| a | Beschleunigung | 3,0 | m/s² |
| F_res | resultierende Kraft (gesucht) | ? | N |

**🧠 Idee**
Das Thema ist **Dynamik**, also der Zusammenhang zwischen Kraft und Bewegungsänderung. Eine resultierende Kraft ändert die Geschwindigkeit eines Körpers. Je schwerer der Körper ist und je stärker er beschleunigt werden soll, desto größer muss diese Kraft sein. Es handelt sich um eine direkte Einsetzaufgabe zu einem Grundgesetz.

**📐 Gleichungen**

**Zweites Newtonsches Gesetz (Grundgleichung der Mechanik):**

$$F_\mathrm{res} = m \cdot a$$

Es gilt für einen Körper mit konstanter Masse. F_res ist die Summe aller Kräfte auf den Körper, m die Masse und a die Beschleunigung.

**Einheit Newton:**

$$1\,\mathrm{N} = 1\,\mathrm{kg} \cdot \frac{\mathrm{m}}{\mathrm{s}^2}$$

**🗺 Vorgehen**
1. Prüfe, ob alle Angaben in SI-Einheiten vorliegen (Einheit Newton).
2. Setze Masse und Beschleunigung in die Grundgleichung ein (Zweites Newtonsches Gesetz).
3. Kontrolliere, ob als Einheit kg·m/s² herauskommt, also N (Einheit Newton).

**🎓 Achtung**
- „Aus Ruhe“ beeinflusst die Kraft hier nicht. Für F = m·a zählt nur die Beschleunigung, nicht die Geschwindigkeit.
- Mit „resultierend“ ist die Gesamtkraft gemeint, nicht eine einzelne Kraft wie die Gewichtskraft.

---

# Aufgabe 2: Aufprallgeschwindigkeit beim freien Fall

**📋 Gegeben / Gesucht**

| Symbol | Bedeutung | Wert | Einheit |
|---|---|---|---|
| h | Fallhöhe | 5,0 | m |
| g | Fallbeschleunigung | 9,81 | m/s² |
| v0 | Anfangsgeschwindigkeit („frei fallen“, ⚠ angenommen: aus Ruhe) | 0 | m/s |
| v | Aufprallgeschwindigkeit (gesucht) | ? | m/s |

**🧠 Idee**
Das Thema ist der **freie Fall**, eine gleichmäßig beschleunigte Bewegung ohne Luftwiderstand. Die Erdanziehung macht den Körper auf jedem Meter schneller. Man kann die Aufgabe auf zwei Arten denken. Erstens über Bewegungsgleichungen. Zweitens über Energie: Beim Fallen wird Lageenergie in Bewegungsenergie umgewandelt.

**🧰 Werkzeug**
Gleichung nach einer Größe umstellen: Auf beiden Seiten dasselbe tun, bis die gesuchte Größe allein steht. Steht die Größe im Quadrat da, ziehst du am Ende die Wurzel. Bei einer Geschwindigkeit, die nach unten zeigt, nimmst du den Betrag (positiv).

**📐 Gleichungen**

**Energieerhaltung (potenzielle Energie = kinetische Energie):**

$$m \cdot g \cdot h = \frac{1}{2}\, m \cdot v^2$$

Sie gilt ohne Reibung und Luftwiderstand. m ist die Masse, g die Fallbeschleunigung, h die Fallhöhe und v die Geschwindigkeit unten.

**Alternativ: zeitfreie Bewegungsgleichung der gleichmäßig beschleunigten Bewegung:**

$$v^2 = v_0^2 + 2\, a\, s$$

Sie gilt bei konstanter Beschleunigung. Hier ist a = g, s die zurückgelegte Strecke und v0 die Anfangsgeschwindigkeit.

**🗺 Vorgehen**
1. Wähle einen Ansatz: Energie oder Bewegungsgleichung (eine der beiden Gleichungen).
2. Setze die Bedingung „aus Ruhe“ ein (v0 bzw. kinetische Energie am Anfang).
3. Stelle nach v um (Werkzeug).
4. Setze erst danach die Zahlen ein und prüfe die Einheit m/s.

**🎓 Achtung**
- Am Ende fehlt oft die Wurzel. Dann hat das Ergebnis die Einheit m²/s², nicht m/s.
- Beim Energieansatz denken viele, sie bräuchten die Masse. Schau genau hin, was mit m in der Gleichung passiert.

---

Aufgabe 3 (Federkraft) erkläre ich dir als Nächstes, wenn du **„weiter“** schreibst.

**🧩 Verständnisfrage**
Wie ändert sich in Aufgabe 2 die Aufprallgeschwindigkeit, wenn der Körper doppelt so schwer ist? Begründe deine Antwort mit einer der Gleichungen.

**🔒 Lösungen**
Mit „lösung“ abrufen.

**➡️ Nächster Schritt**
Löse Aufgabe 1 und 2 selbst nach dem Vorgehen, etwa 10–15 Minuten. Reicht das nicht, schreibe „tipp“. Für ein vorgerechnetes Beispiel schreibe „voll“. Zum Vergleichen schreibe „kurz“ oder schicke deinen Versuch.
````

</details>


### G17

- **Kriterium:** Alias wählt Thema; Verständnisfrage ohne sichtbare Antwort; keine Nebenthemen wie Zentripetalbeschleunigung.
- **Eingabe:** `konzept geradlinige Bewegung`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Teilaussagen (Prüfer 1):**
  - ✔ Alias wählt Thema (Nachricht mit Alias „konzept“ führt zum Modus Thema)
  - ✔ Verständnisfrage ohne sichtbare Antwort
  - ✔ Keine Nebenthemen wie Zentripetalbeschleunigung
- **Antwort:** vollständig, wörtlich

<details><summary>Antwort anzeigen</summary>

````markdown
## 🧠 Idee

Eine geradlinige Bewegung läuft auf einer Linie ab, zum Beispiel ein Auto auf einer geraden Straße oder ein Stein, der senkrecht fällt. Deshalb reicht eine einzige Koordinate x, um den Ort anzugeben. Drei Größen beschreiben alles: der Ort x, die Geschwindigkeit v (wie schnell sich x ändert) und die Beschleunigung a (wie schnell sich v ändert). Das Vorzeichen zeigt die Richtung: Plus heißt in Richtung der gewählten Achse, Minus heißt entgegen.

## 🧰 Werkzeug

Die Ableitung nach der Zeit gibt an, wie schnell sich eine Größe ändert.
Im x-t-Diagramm ist v die Steigung, im v-t-Diagramm ist a die Steigung.
Umgekehrt ist die Fläche unter der v-t-Kurve die zurückgelegte Verschiebung.

## ✏️ Erklärung

**Schritt 1: Die drei Größen verknüpfen.**
Geschwindigkeit ist die Änderungsrate des Ortes, Beschleunigung die Änderungsrate der Geschwindigkeit:

$$v(t) = \frac{dx}{dt}, \qquad a(t) = \frac{dv}{dt}$$

**Schritt 2: Gleichförmige Bewegung (a = 0).**
Die Geschwindigkeit bleibt konstant, der Ort wächst gleichmäßig. x0 ist der Ort zur Zeit t = 0:

$$x(t) = x_0 + v \cdot t$$

**Schritt 3: Gleichmäßig beschleunigte Bewegung (a konstant).**
v0 ist die Anfangsgeschwindigkeit. Die dritte Gleichung enthält keine Zeit und ist praktisch, wenn t weder gegeben noch gesucht ist:

$$v(t) = v_0 + a \cdot t$$

$$x(t) = x_0 + v_0 \cdot t + \frac{1}{2}\, a\, t^2$$

$$v^2 = v_0^2 + 2a\,(x - x_0)$$

⚠ **Gültigkeit:** Die Gleichungen aus Schritt 3 gelten nur bei **konstanter** Beschleunigung. Ändert sich a mit der Zeit, muss man integrieren.

**Schritt 4: Zahlenbeispiel.**
Ein Fahrrad startet aus der Ruhe (v0 = 0, x0 = 0) mit a = 2 m/s². Nach 3 s gilt:

$$v = 2\,\mathrm{\frac{m}{s^2}} \cdot 3\,\mathrm{s} = 6\,\mathrm{\frac{m}{s}}$$

$$x = \frac{1}{2} \cdot 2\,\mathrm{\frac{m}{s^2}} \cdot (3\,\mathrm{s})^2 = 9\,\mathrm{m}$$

Bisher gezeigt: Ort, Geschwindigkeit und Beschleunigung hängen über Ableitungen zusammen; für konstantes a gibt es drei fertige Gleichungen.

## 🛠 So hilft es beim Lösen

- **Signale im Text:** „aus der Ruhe“ bedeutet v0 = 0, „kommt zum Stehen“ bedeutet v = 0 am Ende, „gleichmäßig beschleunigt“ bedeutet a ist konstant, „frei fallend“ bedeutet a = g.
- **Erster Schritt:** eine Achse mit Nullpunkt und positiver Richtung festlegen, dann x0, v0, a, t und das Gesuchte notieren.
- **Gleichung wählen:** die nehmen, in der genau eine unbekannte Größe vorkommt.

## 🎯 Kernidee

Bei konstanter Beschleunigung reichen drei Gleichungen; man wählt die, in der nur die gesuchte Größe unbekannt ist.

## 🚫 Falscher Weg

Bei einer beschleunigten Bewegung den Weg mit „Strecke gleich Geschwindigkeit mal Zeit“ ausrechnen. Diese Formel gilt nur, wenn v konstant ist. Bei beschleunigter Bewegung ändert sich v ständig, deshalb fehlt der Term mit a t².

## 🧩 Verständnisfrage

Ein Ball wird senkrecht nach oben geworfen. Im höchsten Punkt ist seine Geschwindigkeit null. Ist dort auch seine Beschleunigung null? Begründe in einem Satz.

## ➡️ Nächster Schritt

Schreibe die drei Gleichungen aus Schritt 3 aus dem Gedächtnis auf Papier und notiere zu jeder, welche Größe darin fehlt (5 Minuten). Dann schicke mir eine Aufgabe zur geradlinigen Bewegung mit „tipp“.

## 🔒 Lösungen

Mit „lösung“ abrufen.
````

</details>


### G32

- **Kriterium:** Thema erklärt, keine Option beurteilt; Antwort erst nach „lösung“.
- **Eingabe:** `Welche Aussagen treffen zu? Ein Körper bewegt sich mit konstanter Geschwindigkeit auf einer geraden Bahn. ⏎ (a) Die resultierende Kraft auf ihn ist null. ⏎ (b) Auf ihn wirkt überhaupt keine Kraft. ⏎ (c) Seine Beschleunigung ist null. ⏎ (d) Sein Impuls ändert sich mit der Zeit.` → `lösung`
- **Urteil:** bestanden (Prüfer 1: bestanden)
- **Notiz:** Grenzwertig, aber bestanden: Kein Satz beurteilt eine Option. „🧠 Idee“ hebt aber hervor, dass „resultierende Kraft“ und „überhaupt keine Kraft“ nicht dasselbe bedeuten, und lenkt damit stark auf (a) gegen (b). Siehe P4.
- **Teilaussagen (Prüfer 1):**
  - ✔ Das Thema wird erklärt (Kraft, Beschleunigung und Impuls nach Newton)
  - ✔ Die erste Antwort beurteilt keine der Optionen (a) bis (d)
  - ✔ Die Antwort (Urteile und Begründungen zu den Optionen) kommt erst nach „lösung“
- **Antwort:** vollständig, wörtlich

<details><summary>Nachricht 1: Welche Aussagen treffen zu? Ein Körper bewegt sich mit konstanter Geschwindigkeit auf einer geraden Bahn.</summary>

````markdown
## 🧠 Idee

Es geht um die Newtonschen Gesetze, also um den Zusammenhang zwischen **Kraft** und **Bewegungsänderung**. Die Aufgabe ist eine Auswahlaufgabe: Bei jeder Aussage musst du prüfen, ob sie aus „konstante Geschwindigkeit, gerade Bahn“ folgt. Achte dabei auf die Wörter: „resultierende Kraft“ und „überhaupt keine Kraft“ bedeuten nicht dasselbe.

## 🧰 Werkzeug

Kräfte sind Vektoren. Wirken mehrere Kräfte auf einen Körper, addiert man sie mit Richtung. Das Ergebnis heißt **resultierende Kraft** (Gesamtkraft). Zwei gleich große, entgegengesetzte Kräfte ergeben zusammen null.

$$\vec{F}_\mathrm{res} = \vec{F}_1 + \vec{F}_2 + \dots + \vec{F}_n$$

## ✏️ Erklärung

**Schritt 1: Anschaulich.**
Eine Kraft ist nicht nötig, damit sich etwas bewegt. Sie ist nötig, damit sich die Bewegung **ändert**, also schneller, langsamer oder in eine andere Richtung. Ein Eishockey-Puck gleitet fast unverändert weiter, obwohl ihn niemand mehr schiebt.

**Schritt 2: Formal (2. Newtonsches Gesetz).**
Die resultierende Kraft legt die Beschleunigung fest. Die Beschleunigung ist die zeitliche Änderung der Geschwindigkeit:

$$\vec{F}_\mathrm{res} = m \cdot \vec{a}, \qquad \vec{a} = \frac{d\vec{v}}{dt}$$

Mit dem Impuls p = m · v lautet dasselbe Gesetz allgemeiner:

$$\vec{p} = m \cdot \vec{v}, \qquad \vec{F}_\mathrm{res} = \frac{d\vec{p}}{dt}$$

⏸ Was sagt die rechte Gleichung über den Impuls, wenn du weißt, wie groß die resultierende Kraft ist?

**Schritt 3: Zahlenbeispiel (eine andere Situation).**
Eine Kiste mit m = 5 kg wird mit 30 N geschoben, die Reibung bremst mit 20 N:

$$F_\mathrm{res} = 30\,\mathrm{N} - 20\,\mathrm{N} = 10\,\mathrm{N}, \qquad a = \frac{F_\mathrm{res}}{m} = \frac{10\,\mathrm{N}}{5\,\mathrm{kg}} = 2\,\mathrm{\frac{m}{s^2}}$$

Hier sind die Kräfte nicht im Gleichgewicht, deshalb wird die Kiste immer schneller.

**Gültigkeit:** Die Gesetze gelten in einem Inertialsystem (nicht beschleunigtes Bezugssystem). Die Form F = m · a setzt eine konstante Masse voraus, die Form F = dp/dt gilt allgemeiner. Beides gilt für Geschwindigkeiten weit unter der Lichtgeschwindigkeit.

Bisher gezeigt: Die resultierende Kraft bestimmt die Änderung von Geschwindigkeit und Impuls, nicht ihren Wert.

## 🛠 So hilft es beim Lösen

- **Signal:** Wörter wie „konstante Geschwindigkeit“, „ruht“, „gleichförmig“, „beschleunigt“ oder „Gleichgewicht“ in einer Aufgabe.
- **Erster Schritt:** Übersetze die Angabe zur Bewegung in eine Aussage über a. Danach schließt du mit F_res = m · a auf die Kräfte und mit F_res = dp/dt auf den Impuls.
- Bei jeder Aussage prüfen: Geht es um **eine** Kraft oder um die **Summe** aller Kräfte?

## 🎯 Kernidee

Kräfte bestimmen, wie sich die Geschwindigkeit ändert, nicht wie groß sie ist.

## 🚫 Falscher Weg

„Der Körper bewegt sich, also muss eine Kraft in Bewegungsrichtung ihn antreiben.“ Das ist die Alltagsvorstellung aus der Antike. Sie scheitert an Newton 2: Die Gleichung verknüpft die Kraft mit der Beschleunigung a, nicht mit der Geschwindigkeit v.

## 🧩 Verständnisfrage

Ein Aufzug fährt mit konstanter Geschwindigkeit nach oben. Ist die Seilkraft größer, kleiner oder gleich groß wie die Gewichtskraft der Kabine? Begründe in einem Satz.

## ➡️ Nächster Schritt

Beurteile die Aussagen (a) bis (d) auf Papier in etwa 5 Minuten, je Aussage „trifft zu / trifft nicht zu“ mit einem Satz Begründung. Schick mir dann deinen Versuch zum Prüfen oder schreibe „lösung“ zum Vergleichen.

## 🔒 Lösungen

Mit ‚lösung‘ abrufen.
````

</details>

<details><summary>Nachricht 2: lösung</summary>

````markdown
## ✅ Ergebnis

Es treffen **(a)** und **(c)** zu.

| Aussage | Urteil | Grund |
|---|---|---|
| (a) Resultierende Kraft null | trifft zu | Konstante Geschwindigkeit auf gerader Bahn heißt a = 0, also nach Newton 2 auch F_res = 0. |
| (b) Überhaupt keine Kraft | trifft nicht zu | Es können Kräfte wirken (z. B. Antrieb und Reibung), sie heben sich nur gegenseitig auf. |
| (c) Beschleunigung null | trifft zu | Weder Betrag noch Richtung der Geschwindigkeit ändern sich, also dv/dt = 0. |
| (d) Impuls ändert sich | trifft nicht zu | Mit konstantem m und v ist p = m · v konstant; das passt zu F_res = dp/dt = 0. |

Der Weg in Kurzform:

$$\vec{v} = \mathrm{const} \;\Rightarrow\; \vec{a} = \frac{d\vec{v}}{dt} = 0 \;\Rightarrow\; \vec{F}_\mathrm{res} = m \cdot \vec{a} = 0 \;\Rightarrow\; \frac{d\vec{p}}{dt} = 0$$

## 🇩🇪 Klausur-Lösung

Zutreffend sind (a) und (c). Bei konstanter Geschwindigkeit auf gerader Bahn ist a = 0. Nach dem 2. Newtonschen Gesetz gilt dann F_res = m · a = 0 und dp/dt = 0, der Impuls ist also konstant, und (d) ist falsch. (b) ist falsch, weil nur die Summe der Kräfte verschwinden muss: Einzelkräfte können wirken, wenn sie sich kompensieren.

## 🧩 Antwort zur Verständnisfrage

**Die Seilkraft ist gleich groß wie die Gewichtskraft.** Bei konstanter Geschwindigkeit ist a = 0, also muss die resultierende Kraft null sein, egal ob der Aufzug nach oben fährt, nach unten fährt oder steht. Größer als die Gewichtskraft ist die Seilkraft nur, während der Aufzug nach oben beschleunigt, also beim Anfahren aufwärts oder beim Abbremsen einer Abwärtsfahrt.

## ➡️ Nächster Schritt

Vergleiche in etwa 3 Minuten deine eigene Begründung zu (b) mit der Tabelle: Hast du zwischen „einzelne Kraft“ und „resultierende Kraft“ unterschieden? Wenn nicht, schreibe diesen Unterschied als einen Satz auf eine Karteikarte.
````

</details>

## Darstellung

Nicht geprüft: Der Lauf hatte keine gerenderte Oberfläche. In den Rohtexten stehen alle Display-Formeln als eigene `$$…$$`-Zeile, und überall steht ein Dezimalkomma (`2{,}0`). Das ist ein Hinweis für D1 und D2, ersetzt aber keine Prüfung.

| ID | Ergebnis | Screenshot |
|---|---|---|
| D1 | nicht geprüft | – |
| D2 | nicht geprüft | – |
| D3 | nicht geprüft (kein Fall in ar/ur) | – |
| D4 | nicht geprüft | – |

## Ergebnis

Alle Gate-Fälle bestanden: **nein**. Der Lauf ist auch kein Gate-Lauf (Ersatzoberfläche, Teilmenge, Modellprüfer).

- **Nicht bestanden:** M08-A (P1) und M09-A (P2) wegen des Prompts, M06-A (K1) wegen des Kriteriums.
- **Geplante Wiederholung:** nach P1/P2 die Fälle M08-A/B/C, M09-A/B/C und G24; nach K1 M06-A mit demselben Build.
- **Offen:** M01…M10 für B und C, G01, G02, G05 … G13, G15, G16, G19 … G31 sowie D1 … D4. Diese Fälle laufen auf der echten Oberfläche (Skill-ZIP auf claude.ai) mit dem Lernenden als Prüfer.
