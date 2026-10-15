# tutor – MINT-Lern-Tutor als Claude-Skill und System-Prompt

Lern-Tutor für Aufgaben aus dem ersten Studienjahr in MINT-Fächern (Physik, Mathematik, E-Technik) an deutschsprachigen Hochschulen. Erst verstehen, dann selbst lösen: Erklärung ohne fertige Lösung, Leitfragen, Fehlerdiagnose des eigenen Versuchs, Klausur-Lösung auf Deutsch, Lösungen erst auf Abruf. Erklärungen auf Deutsch oder auf Wunsch in Arabisch, Türkisch, Französisch, Englisch oder Urdu. ADHS-freundlich gestaltet (kurze Schritte, feste Struktur; Designziel, keine nachgewiesene Wirkung). Kein Programm, kein Dienst: Der Tutor läuft als Anweisung in Claude oder ChatGPT.

## Status

- **Vorabstand v0.2, nicht abgenommen.** Build und Strukturtests laufen; die Abnahme des Lehrverhaltens mit einem Modell ([tests/akzeptanz.md](tests/akzeptanz.md)) ist vorbereitet, aber noch nicht ausgeführt.
- **Rechte:** [MIT-Lizenz](LICENSE).
- **Feedback:** [Issue anlegen](https://github.com/Sae-l/tutor/issues/new) oder im Tutor `!issue` schreiben. Issues sind öffentlich: keine Aufgabentexte, Namen oder Fotos mit persönlichen Daten einfügen.

## Welche Variante?

| Plattform | Dateien | Stand |
|---|---|---|
| **Claude Skill** (empfohlen) | Ordner `tutor/` als ZIP | primär; Release-Gate mit allen Akzeptanzfällen |
| ChatGPT Projekt | Anweisung `dist/kern.md`, Datei `dist/system-prompt.md` | experimentell; Teilabnahme vorgesehen |
| Gemini (Gem bzw. Gemini-Skill) | wie ChatGPT Projekt | experimentell, nicht geprüft |

Custom GPTs werden von OpenAI für neue private Konten eingestellt und sind nicht mehr vorgesehen; Gemini-Gems werden zu „Gemini skills“ ([Recherche](https://github.com/Sae-l/tutor/issues/11)).

## Schnellstart (Claude Skill)

1. Skill-Paket aus dem Repository bauen (nur versionierte Dateien, keine lokalen Werkzeugdaten):

   ```bash
   git archive --format=zip --prefix=tutor/ -o tutor-skill.zip HEAD:tutor
   ```

2. In Claude unter *Einstellungen → Skills* `tutor-skill.zip` hochladen.
3. Ein Projekt „Tutor“ anlegen und dort lernen: Foto der Aufgabe schicken, optional mit einem Befehlswort.

Beispiel: Foto einer Aufgabe + `tipp` → vier bis sechs Leitfragen, keine Lösung. Danach eigener Rechenweg als Nachricht → Fehlerdiagnose (Check). Zum Vergleichen: `kurz`.

## Bedienung

**Sprache:** standardmäßig Deutsch, auch wenn du in einer anderen Sprache schreibst. Umschalten mit `[ar]` Arabisch, `[tr]` Türkisch, `[fr]` Französisch, `[en]` Englisch, `[ur]` Urdu, `[de]` zurück, oder `!sprache ar` usw. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch, damit das Prüfungsvokabular mitgelernt wird.

**Befehle:** ein Befehlswort am Nachrichtenanfang (z. B. Foto + „tipp“) oder mit `!` irgendwo in der eigenen Anweisung. `hilfe` zeigt die Befehlskarte. Empfohlene Reihenfolge: **erklär → tipp → voll → kurz**.

| Befehl | Wirkung |
|---|---|
| (keiner) / `erklär` | Thema und nötige Gleichungen, **ohne** Beispiel und **ohne** Lösung |
| `voll` | anschaulich und mathematisch, mit vorgerechnetem Beispiel einer anderen Aufgabe |
| `thema` | Begriff oder Gesetz verstehen und wie es beim Lösen hilft |
| `tipp` | Leitfragen, die man sich selbst stellt; Lösung zurückgehalten |
| `check` | Fehlerdiagnose des eigenen Versuchs (automatisch, wenn ein Versuch mitkommt) |
| `skizze` | Skizze, Diagramm oder Graph (mit Zeichenwerkzeug als Bild, sonst Beschreibung + TikZ/matplotlib) |
| `kurz` | Klausur-Lösung auf Deutsch plus eine Anmerkung |
| `mittel` | Erklärung mittlerer Tiefe mit vollständiger Lösung |
| `lang` | vollständige Lösung plus bis zu zwei andere Lösungswege |
| `klausur` | schnelle Lösung mit Tipps für volle Punktzahl |
| `hilfe` | Befehlskarte |
| `!issue` | Link für Feedback |

**Dauermodus:** `!an tipp` (oder ein anderer Befehl) gilt für alle folgenden Aufgaben, bis `!aus` kommt.

**Lösungsschutz:** Die Lösung nach `tipp` und Antworten auf Verständnisfragen kommen erst mit `lösung`. Das Symbol 🔒 allein versteckt keinen Text.

**Kurspaket (optional):** Eine Datei mit Notation und Stoffumfang eines bestimmten Kurses kann zusätzlich hochgeladen werden, z. B. [kurse/mpg1.md](kurse/mpg1.md) als Beispiel. Sie gehört nicht zum Skill.

## Einrichtung auf anderen Plattformen (experimentell)

**ChatGPT Projekt / Gemini:** Inhalt von `dist/kern.md` (höchstens 4000 Zeichen, vom Build geprüft) in die Anweisungen kopieren und `dist/system-prompt.md` als Datei hochladen. Feldgrenzen, Formeldarstellung und Aufklappblöcke sind dort nicht offiziell dokumentiert und nicht geprüft.

## Datenschutz

Der Tutor speichert nichts selbst; Gespräche liegen beim jeweiligen Anbieter (Anthropic, OpenAI, Google) nach dessen Bedingungen. `!issue` erzeugt nur einen Link mit festem Titel und schickt keine Gesprächsinhalte. Was du in ein GitHub-Issue schreibst, ist öffentlich.

## Aufbau

| Pfad | Zweck |
|---|---|
| `tutor/` | Quelle: Claude-Skill (`SKILL.md` als Router + `modes/` + `references/`) |
| `kurse/` | optionale Kurspakete, nicht Teil des Skills |
| `dist/system-prompt.md` | Erzeugt: alles in einer Datei, für andere Plattformen |
| `dist/kern.md` | Erzeugt: Kern aus den `<!-- kern -->`-Abschnitten von `SKILL.md`, höchstens 4000 Zeichen |
| `build.py` | Erzeugt `dist/` aus der Quelle |
| `tests/` | Strukturtests, Akzeptanzfälle, Protokolle der Abnahme |
| `docs/KONZEPT.md` | Hintergrund: Ziel, Lernprinzipien, Architekturentscheidungen |
| `GLOSSARY.md` | Festgelegte Begriffe |

## Entwicklung

Voraussetzung: Git und Python 3.14 (nur Standardbibliothek).

```bash
python build.py
```

```bash
python -B -m unittest discover -s tests -v
```

Änderungen nur in `tutor/` machen, danach `python build.py` ausführen und beides committen. Die Tests prüfen den reproduzierbaren Build, dass Befehlstabelle und Moduldateien übereinstimmen (11 Modi), Kurs-Neutralität des Skills, Länge und Inhalt des Kerns, Formel-Beispiele und den Erhalt der bisherigen Ausgabe bei fehlerhaften Quellen (auch unter `python -O`). Die CI führt dasselbe auf Linux und Windows aus.

[tests/akzeptanz.md](tests/akzeptanz.md) enthält das Release-Gate, 30 Modusfälle und 31 Zustands- und Grenzfälle, je mit stabiler ID. Bestandene Strukturtests belegen kein korrektes Tutorverhalten.

Ablauf, Release-Checkliste und Paketbau: [CONTRIBUTING.md](CONTRIBUTING.md). Sicherheit: [SECURITY.md](SECURITY.md). Änderungen: [CHANGELOG.md](CHANGELOG.md).

## Grenzen

- Formeln werden nur dann sauber dargestellt, wenn die Plattform `$$ ... $$` rendert; nur informell beobachtet, nicht protokolliert.
- Hochgeladene Dateien liest das Modell nicht immer vollständig; deshalb stehen die wichtigsten Regeln im Kern.
- Der Tutor kennt keine Bewertungskriterien einzelner Hochschulen. Ergebnisse mit offiziellen Musterlösungen abgleichen.
- Die Lernprinzipien in [docs/KONZEPT.md](docs/KONZEPT.md) begründen das Design, belegen aber keine Wirksamkeit dieses Tutors, auch nicht für ADHS.
