# Änderungen

Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/). Versionen erst ab dem ersten Release; Ablauf in CONTRIBUTING.md.

## [Unveröffentlicht]

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
