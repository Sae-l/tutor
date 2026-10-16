# Mitarbeit

Persönliches Projekt mit einem Maintainer (siehe README, „Status“). Diese Datei beschreibt den Arbeitsablauf, auch für die eigene Arbeit.

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
2. Gehört eine Regel in den Kern (für Plattformen mit kurzem Anweisungsfeld), sie in `tutor/SKILL.md` innerhalb von `<!-- kern -->` … `<!-- /kern -->` schreiben; der Build bricht ab, wenn `dist/kern.md` über 4000 Zeichen kommt.
3. `python build.py`, Tests ausführen, `tutor/` und `dist/` gemeinsam committen. Der Build ersetzt das gesamte erzeugte `dist/`; dort keine eigenen Dateien ablegen. Paketidentität und -version stehen in `packaging/chatgpt-plugin.json`.
4. README, `CLAUDE.md` und `CHANGELOG.md` nachführen.
5. Änderungen über einen Branch und Pull Request nach `main`; die CI muss grün sein.
6. Betroffene Akzeptanzfälle nach der Wiederholungsregel in `tests/akzeptanz.md` erneut prüfen und protokollieren.

Die deutsche Wissensbasis liegt unter `Obsidian-tutor/`. Nach Änderungen an ihren Quellen die betroffenen Notizen prüfen und `Quellen.sha256.json` bewusst aktualisieren: SHA-256 über UTF-8-Text mit LF-Zeilenenden, ZIP-Dateien über unveränderte Bytes. `python -B Obsidian-tutor/verify_vault.py` prüft Links, Canvas, Modusabdeckung und Quellstand; dieselbe Prüfung läuft in CI auf Linux und Windows. Neue Notizen benötigen eine Verknüpfung von der Startseite und genau eine Canvas-Dateikarte. Persönliche Obsidian-Einstellungen, Chatkennungen und private Kurs-/Testunterlagen bleiben ausgeschlossen.

Neuer Modus: Datei in `tutor/modes/` und Zeile in der Befehlstabelle von `tutor/SKILL.md`; `build.py` liest die Modi aus der Tabelle. Die erwartete Anzahl (11) in `build.py` und `tests/test_build.py` anpassen, Befehlskarte in `modes/hilfe.md` und Akzeptanzfälle ergänzen. Kurspakete gehören nach `kurse/`, nie nach `tutor/`.

Werkzeugzustände (`.claude-flow/`, `.agents/`, `.claude/`, `skills-lock.json`) und Kursunterlagen (`referenzen/`) sind per `.gitignore` ausgeschlossen. Vor jedem Commit mit `git status` prüfen, dass nur gewollte Dateien vorgemerkt sind.

Ausnahme: Der erzeugte Katalog `dist/chatgpt/.agents/plugins/marketplace.json` gehört ins Repository. `.gitattributes` hält Quelle und Paket auf LF, damit die Skillbytes unter Windows und Linux gleich bleiben. Native Installation und Prüfgrenzen: [docs/CHATGPT.md](docs/CHATGPT.md).

## Release

Erst eine Vorabversion (`v0.x.0-rc.N`), eine stabile Version erst, wenn das Release-Gate in `tests/akzeptanz.md` bestanden und protokolliert ist.

1. Aus einem separaten sauberen Checkout des exakten `main`-Commits arbeiten; CI für diesen Commit ist grün, `CHANGELOG.md` und Pluginmanifest nennen die neue Version. `python build.py`, Strukturtests und Vaultprüfung ausführen; `git diff --exit-code -- dist/` muss danach leer sein. Keine lokalen Änderungen oder privaten Protokolle übernehmen.
2. Skill-Paket aus dem Commit bauen, nicht aus dem Arbeitsordner (so gelangen nur versionierte Dateien hinein):

   ```bash
   release_dir=$(mktemp -d)
   git archive --format=zip --prefix=tutor/ -o "$release_dir/tutor-skill.zip" HEAD:tutor
   ```

3. Prüfsummen im separaten Releaseordner erzeugen (Dateinamen ohne `dist/`, damit heruntergeladene Assets direkt prüfbar sind). Die Bash-Befehle laufen in derselben Sitzung von der Repositorywurzel:

   ```bash
   cp dist/tutor-chatgpt.zip dist/system-prompt.md dist/kern.md "$release_dir/"
   (cd "$release_dir" && sha256sum tutor-skill.zip tutor-chatgpt.zip system-prompt.md kern.md > SHA256SUMS.txt && sha256sum -c SHA256SUMS.txt)
   ```

4. Für eine stabile Version: Abnahme mit genau diesem ZIP durchführen, Protokoll in `tests/protokolle/` committen.
5. Tag setzen und Release anlegen; Anhänge: beide ZIPs, beide Promptdateien, `SHA256SUMS.txt`. Das ChatGPT-ZIP ist für den Plugin-Importer, kein Chat-Attachment. Notizen: Commit, Änderungen, geprüfte Plattformen, bekannte Grenzen. Vorabversionen als „Pre-release“ markieren. Vor dem nächsten Release Pluginversion und Releaseversion abstimmen; bestehende Tags nicht neu belegen. Beispiel für rc.3; erst nach grüner CI des zu veröffentlichenden Commits:

   ```bash
   git tag -a v0.2.0-rc.3 -m "v0.2.0-rc.3"
   git push origin v0.2.0-rc.3
   gh release create v0.2.0-rc.3 --verify-tag --prerelease --notes-file docs/releases/v0.2.0-rc.3.md "$release_dir/tutor-skill.zip" "$release_dir/tutor-chatgpt.zip" "$release_dir/system-prompt.md" "$release_dir/kern.md" "$release_dir/SHA256SUMS.txt"
   ```

Nur tatsächlich geprüfte Plattformen als geprüft aufführen.
