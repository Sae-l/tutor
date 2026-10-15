# Änderungen

Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/). Versionen erst ab dem ersten Release; Ablauf in CONTRIBUTING.md.

## [Unveröffentlicht]

Öffentliche Version v0.2 (Map #9); Akzeptanzfälle noch nicht ausgeführt.

### Geändert
- Zielgruppe: Studierende im ersten Studienjahr eines deutschsprachigen MINT-Studiengangs statt einer einzelnen Person; ADHS-Freundlichkeit als Gestaltungsprinzip.
- Befehlssatz v0.2 mit 11 Modi: erklär, voll (bisher detail/ausführlich), thema (bisher konzept, plus „So hilft es beim Lösen“), tipp, check, skizze, kurz (jetzt Klausur-Lösung + eine Anmerkung), mittel (bisher standard, ohne Übungen), lang, klausur, hilfe. Eskalation erklär → tipp → voll → kurz.
- Erklärsprachen: Deutsch, Arabisch, Türkisch, Französisch, Englisch, Urdu; `!sprache xx` als Signal.
- `SKILL.md` ist ein schlanker Router; Sprache und Didaktik in `references/sprache.md` und `references/didaktik.md`.
- Kurs MPG1 als optionales Kurspaket `kurse/mpg1.md` außerhalb des Skills; Skill ohne Hochschul- oder Kursbezug.
- Build erzeugt `dist/kern.md` (höchstens 4000 Zeichen) aus markierten Abschnitten von `SKILL.md`.
- Plattformen: Claude Skill (Release-Gate), ChatGPT Projekt und Gemini experimentell.
- Thema beurteilt Begründungs- und Auswahlfragen aus Übungsblättern erst nach „lösung“ (Lösungsschutz); Verständnisfrage auch in Lang laut Didaktik.
- Didaktik: Die Regel „jede Option einzeln beurteilen“ galt „in jedem Modus“ und widersprach dem Lösungsschutz; in Erklär, Voll, Thema und Tipp jetzt erst auf „lösung“.
- README: englische Kurzbeschreibung, `git clone` im Schnellstart, Anzahl der Grenzfälle (32) korrigiert.
- `docs/KONZEPT.md` und Release-Ablauf in `CONTRIBUTING.md` auf v0.2 (`dist/kern.md`) nachgeführt.
- SECURITY.md, PR- und Issue-Vorlage auf v0.2 nachgeführt (öffentliches Repo, Vorabversionen, Kern statt Kurzfassung).

### Hinzugefügt
- Dependabot für die auf SHAs festgelegten GitHub Actions (`.github/dependabot.yml`).
- Modi Skizze, Lang und Klausur; Befehl `!issue` (Feedback-Link ohne Gesprächsinhalt) und Datenschutzhinweis im README.
- Akzeptanzfälle für v0.2: M01-A … M10-C, G01 … G32.

### Entfernt
- Modi Übung, Standard und Lösung als eigene Befehle; „lösung“ bleibt der Abruf zurückgehaltener Lösungen.
- Ukrainisch als Erklärsprache.
- Handgeschriebene Kurzfassung (`dist/system-prompt-kurz.md`) und Custom GPT als Zielplattform.

## [0.1.0-rc.1] – 2026-10-15

Erste Vorabversion; Akzeptanzfälle noch nicht ausgeführt.

### Hinzugefügt
- Modus Hilfe (Befehlskarte) als zehnter Modus.
- Kurzfassung `dist/system-prompt-kurz.md` (höchstens 8000 Zeichen) für Anweisungsfelder mit Längenlimit.
- Kursreferenz `tutor/references/kurs-mpg1.md`: Notation, Stoffumfang, Umgang mit Endantworten.
- Strukturtests in `tests/test_build.py`; Akzeptanzfälle mit stabilen IDs, Release-Gate und Protokollvorlage.
- CI (Linux und Windows): Build, Abgleich von `dist/` mit dem Commit, Strukturtests, Paketinhalt.
- Lizenz MIT (`LICENSE`).
- SECURITY.md, CONTRIBUTING.md, Issue- und PR-Vorlagen, `.gitignore`, `GLOSSARY.md`, `docs/KONZEPT.md`.

### Geändert
- Erklär ohne Beispiel und ohne Lösung; Detail mit vorgerechnetem Beispiel einer anderen Aufgabe; Tipp nur Leitfragen.
- Lösungsschutz: Lösungen von Übungen und Tipp nur auf ausdrücklichen Abruf; Schutzprüfung vor dem Senden.
- Sprache: Aufgabentext immer Deutsch; Erklärsprache wechselt nur per Signal.
- Build bricht bei offenen Dateiverweisen oder zu langer Kurzfassung mit Meldung ab, auch unter `python -O`.

### Entfernt
- Sechs unpassende GitHub-Vorlage-Workflows (Django, Conda, PyPI-Upload, Pylint, Python-App, Python-Package); sie schlugen fehl. Einzige CI ist `ci.yml`.
