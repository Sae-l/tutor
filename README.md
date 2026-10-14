# tutor

Lern-Tutor für Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln), ausgelegt für Anfänger mit ADHS: erst anschaulich, dann schrittweise Rechnung, Klausur-Lösung auf Deutsch, Übungen mit versteckten Lösungen.

**Sprache:** standardmäßig Deutsch. Umschalten mit einem Signal in der Nachricht: `[ar]` Arabisch, `[tr]` Türkisch, `[uk]` Ukrainisch, `[fr]` Französisch, `[de]` zurück zu Deutsch. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch.

**Befehle:** ein Befehlswort oder eine aufgeführte Wortgruppe am Nachrichtenanfang (z. B. Foto + „tipp“), oder mit `!` in der eigenen Anweisung; kombinierbar mit dem Sprachcode, z. B. `tipp [ar]` oder `[ar] tipp`. „tutor“ oder „hilfe“ zeigt die Befehlskarte. Empfohlene Reihenfolge beim Lernen: **erklär → tipp → lösung**.

| Befehl | Wirkung |
|---|---|
| (keiner) / `erklär` | Erklärung + ähnliches gelöstes Beispiel, **ohne** Lösung der Aufgabe |
| `standard` | Erklärung mittlerer Tiefe mit Lösung + zwei Übungen |
| `!detail` | ausführlich, mit Vertiefung |
| `!kurz` | knappe Erklärung |
| `!lösung` | direkt die Klausur-Lösung |
| `!tipp` | drei Hinweisstufen, Lösung versteckt |
| `!check` | Fehlerdiagnose des eigenen Versuchs (automatisch, wenn ein Versuch mitkommt) |
| `!übung` | drei neue Aufgaben desselben Typs |
| `!konzept` | Begriff oder Satz verstehen, ohne Rechenaufgabe |

Die Befehle verstehen auch natürliche Wörter in allen fünf Sprachen (z. B. „kurz“, „سريع“, „hızlı“).

**Dauermodus:** `!an tipp` (oder ein anderer Befehl) gilt für alle folgenden Aufgaben, bis `!aus` kommt. Ein Einzelbefehl überschreibt ihn nur für diese eine Nachricht. Jede Antwort zeigt dann oben den aktiven Modus und die Sprache.

**Lösungsschutz:** Ohne geprüfte Aufklappfunktion bleiben Übungs- und Tipp-Lösungen bis zum ausdrücklichen Abruf zurückgehalten. `lösung Übung 2` zeigt gezielt die zweite Lösung. Das Symbol 🔒 allein versteckt keinen Text. Im Erklärmodus bleiben auch bei mehreren Aufgaben die Originalergebnisse zurückgehalten.

## Aufbau

| Pfad | Zweck |
|---|---|
| `tutor/` | Quelle: Claude-Skill (`SKILL.md` + `references/`) |
| `dist/system-prompt.md` | Erzeugt: eine einzige, selbstständige Prompt-Datei für alle anderen Plattformen |
| `tutor/references/kurzfassung.md` | Quelle: handgeschriebene Kurzfassung (höchstens 8000 Zeichen, Build bricht sonst ab) |
| `dist/system-prompt-kurz.md` | Erzeugt: Kurzfassung für Felder mit Zeichenlimit (Custom GPT: 8000; Gemini und Copilot nicht geprüft, 8000 als vorsichtiger Wert) |
| `build.py` | Erzeugt `dist/` aus der Quelle |

Die Kurzfassung ist eine eigene Textquelle und wird **nicht** automatisch aus den Moduldateien abgeleitet. Ändert sich Verhalten in `tutor/`, die Kurzfassung von Hand angleichen; die Tests prüfen nur Länge, Befehle, Sprachcodes und Kernregeln.

Änderungen nur in `tutor/` machen, danach `python build.py` ausführen und beides committen.

## Prüfung

`python -B -m unittest discover -s tests -v` prüft den reproduzierbaren Build, die neun Modusdateien, offene Dateiverweise, Formel-Beispiele und den Erhalt der bisherigen Ausgabe bei fehlenden Quellen.

[tests/akzeptanz.md](tests/akzeptanz.md) enthält 27 vorbereitete Fach-/Modusfälle und 18 Zustands- und Grenzfälle. Diese Modelltests sind noch nicht ausgeführt; bestandene Strukturtests belegen kein korrektes Tutorverhalten. Die Testdaten sind selbst erstellte Aufgaben.

## Einrichtung je Plattform

**Claude (App/Web)** – Ordner `tutor/` als ZIP packen und unter *Einstellungen → Skills* hochladen. Am besten ein Projekt „Tutor“ anlegen und dort lernen: einmal betreten, dann nur noch Foto + ein Befehlswort schicken.

**Claude Projects** – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**ChatGPT (Projekt)** – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**ChatGPT (Custom GPT)** – Das Anweisungsfeld ist zu kurz für den ganzen Prompt. `dist/system-prompt.md` unter *Wissen* hochladen und als Anweisung eintragen:

> Du bist ein Physik- und Mathe-Tutor. Lies vor jeder Antwort die Datei system-prompt.md im Wissen und befolge sie vollständig, besonders Sprache, Antwortvorlage und LaTeX-Regeln. Standardsprache ist Deutsch.

**Gemini (Gem)** – Neues Gem anlegen, Inhalt von `dist/system-prompt.md` in die Anweisungen kopieren.

**Microsoft Copilot / GitHub Copilot** – Inhalt von `dist/system-prompt.md` als Anweisungen eines eigenen Agenten (bzw. in `.github/copilot-instructions.md`) eintragen. Ist das Feld zu kurz, wie beim Custom GPT vorgehen: Datei hochladen, Kurzanweisung eintragen.

## Grenzen

- Formeln werden nur dann sauber dargestellt, wenn die Plattform `$$ ... $$` rendert. Getestet in Claude und ChatGPT; Gemini und Copilot sind noch nicht geprüft.
- Bei hochgeladenen Wissensdateien (Custom GPT, Copilot) liest das Modell die Datei nicht immer vollständig. Direkt eingefügte Anweisungen sind zuverlässiger.
- Der Tutor kennt keine internen Bewertungskriterien der TH Köln. Ergebnisse mit offiziellen Musterlösungen abgleichen.
