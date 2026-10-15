# Mitarbeit

Persönliches Projekt mit einem Maintainer (siehe README, „Status und Nutzung“). Diese Datei beschreibt den Arbeitsablauf, auch für die eigene Arbeit.

## Voraussetzungen

- Git
- Python 3.14 (damit geprüft; der Build nutzt nur die Standardbibliothek, kein `pip install` nötig)

Kein Node, Docker, Datenbank oder Agentenwerkzeug nötig.

## Ablauf

```bash
git clone https://github.com/Sae-l/tutor.git
cd tutor
python build.py
python -B -m unittest discover -s tests -v
```

1. Verhalten nur in `tutor/` ändern. `dist/` wird erzeugt und nie von Hand bearbeitet.
2. Ändert sich Verhalten, `tutor/references/kurzfassung.md` von Hand angleichen (sie wird nicht abgeleitet).
3. `python build.py`, Tests ausführen, `tutor/` und `dist/` gemeinsam committen.
4. README, `CLAUDE.md` und `CHANGELOG.md` nachführen.
5. Änderungen über einen Branch und Pull Request nach `main`; die CI muss grün sein.
6. Betroffene Akzeptanzfälle nach der Wiederholungsregel in `tests/akzeptanz.md` erneut prüfen und protokollieren.

Neuer Modus: Datei in `tutor/modes/`, Zeile in der Befehlstabelle von `tutor/SKILL.md`, Name in `MODES` in `build.py`, Zeile in der Kurzfassung.

Werkzeugzustände (`.claude-flow/`, `.agents/`, `skills-lock.json`) und Kursunterlagen (`referenzen/`) sind per `.gitignore` ausgeschlossen. Vor jedem Commit mit `git status` prüfen, dass nur gewollte Dateien vorgemerkt sind.

## Release

Erst eine Vorabversion (`v0.x.0-rc.N`), eine stabile Version erst, wenn das Release-Gate in `tests/akzeptanz.md` bestanden und protokolliert ist.

1. `main` ist sauber, CI grün, `CHANGELOG.md` hat einen Abschnitt für die neue Version.
2. Skill-Paket aus dem Commit bauen, nicht aus dem Arbeitsordner (so gelangen nur versionierte Dateien hinein):

   ```bash
   git archive --format=zip --prefix=tutor/ -o tutor-skill.zip HEAD:tutor
   ```

3. Prüfsummen erzeugen:

   ```bash
   sha256sum tutor-skill.zip dist/system-prompt.md dist/system-prompt-kurz.md > SHA256SUMS.txt
   ```

4. Für eine stabile Version: Abnahme mit genau diesem ZIP durchführen, Protokoll in `tests/protokolle/` committen.
5. Tag setzen und Release anlegen; Anhänge: ZIP, beide Promptdateien, `SHA256SUMS.txt`. Notizen: Commit, Änderungen, geprüfte Plattformen, bekannte Grenzen. Vorabversionen als „Pre-release“ markieren:

   ```bash
   git tag -a v0.1.0-rc.1 -m "v0.1.0-rc.1"
   git push origin v0.1.0-rc.1
   gh release create v0.1.0-rc.1 --prerelease --notes-file notizen.md tutor-skill.zip dist/system-prompt.md dist/system-prompt-kurz.md SHA256SUMS.txt
   ```

Nur tatsächlich geprüfte Plattformen als geprüft aufführen.
