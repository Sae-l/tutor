# Mitarbeit

Persönliches Projekt mit einem Maintainer (siehe README, „Stand und Grenzen“). Diese Datei beschreibt den Arbeitsablauf, auch für die eigene Arbeit.

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

Erst eine Vorabversion (`v0.x.0-rc.N`), eine stabile Version erst, wenn das Release-Gate in `tests/akzeptanz.md` bestanden und protokolliert ist. Ausnahme: v0.2.0 wurde am 2026-10-20 auf Entscheidung des Maintainers ohne bestandenes Gate stabil veröffentlicht (#32 offen); für spätere stabile Versionen gilt die Regel wieder. Am 2026-10-28 wurde die Vorabversion v0.3.0-rc.3 auf Entscheidung des Maintainers als „Latest“ markiert; sie bleibt eine Vorabversion ohne bestandenes Gate. Am selben Tag folgte v0.3.0-rc.4 (Persisch statt Urdu) ebenfalls als „Latest“, damit die Website die aktuelle Fassung herunterlädt. Ebenso v0.3.0-rc.5 mit den Korrekturen aus dem Protokoll G29/D3.

1. Aus einem separaten sauberen Checkout des exakten `main`-Commits arbeiten; CI für diesen Commit ist grün, `CHANGELOG.md` und Pluginmanifest nennen die neue Version. `python build.py`, Strukturtests und Vaultprüfung ausführen; `git diff --exit-code -- dist/` muss danach leer sein. Keine lokalen Änderungen oder privaten Protokolle übernehmen.
2. Skill-Paket aus dem Commit bauen, nicht aus dem Arbeitsordner (so gelangen nur versionierte Dateien hinein):

   ```bash
   release_dir=$(mktemp -d)
   git archive --format=zip -o "$release_dir/tutor-skill.zip" HEAD tutor/
   ```

   Den Pfad `HEAD tutor/` verwenden, damit die `.gitattributes` der Repositorywurzel gelten. `HEAD:tutor` verliert diesen Pfadkontext und kann bei `core.autocrlf=true` andere Paketbytes erzeugen.

3. Prüfsummen im separaten Releaseordner erzeugen (Dateinamen ohne `dist/`, damit heruntergeladene Assets direkt prüfbar sind). Die Bash-Befehle laufen in derselben Sitzung von der Repositorywurzel:

   ```bash
   cp dist/tutor-chatgpt.zip dist/system-prompt.md dist/kern.md "$release_dir/"
   (cd "$release_dir" && sha256sum tutor-skill.zip tutor-chatgpt.zip system-prompt.md kern.md > SHA256SUMS.txt && sha256sum -c SHA256SUMS.txt)
   ```

4. Für eine stabile Version: Abnahme mit genau diesem ZIP durchführen, Protokoll in `tests/protokolle/` committen.
5. Tag setzen und Release anlegen; Anhänge: beide ZIPs, beide Promptdateien, `SHA256SUMS.txt`. Das ChatGPT-ZIP ist für den Plugin-Importer, kein Chat-Attachment. Notizen: Commit, Änderungen, geprüfte Plattformen, bekannte Grenzen. Vorabversionen mit `--prerelease`, stabile Versionen mit `--latest` veröffentlichen. Vor dem nächsten Release Pluginversion und Releaseversion abstimmen; bestehende Tags nicht neu belegen. Beispiel für v0.2.0; erst nach grüner CI des zu veröffentlichenden Commits:

   ```bash
   git tag -a v0.2.0 -m "v0.2.0"
   git push origin v0.2.0
   gh release create v0.2.0 --verify-tag --latest --notes-file docs/releases/v0.2.0.md "$release_dir/tutor-skill.zip" "$release_dir/tutor-chatgpt.zip" "$release_dir/system-prompt.md" "$release_dir/kern.md" "$release_dir/SHA256SUMS.txt"
   ```

Nur tatsächlich geprüfte Plattformen als geprüft aufführen.

## Offizielle Verzeichnisse

Für ChatGPT/Codex wird `dist/chatgpt/plugins/tutor/` gebaut, für Claude Code `dist/claude/plugins/tutor/`. Das Claude-Code-Paket behält die bisherigen Bytes; die frühere Prüfung mit `claude plugin validate --strict` ist ein historischer Nachweis, kein neuer Validierungslauf. Die Einreichung braucht das Konto des Maintainers und geht nicht über das Repository. Gemini hat kein öffentliches Skill-Verzeichnis; dort ist der Upload von `tutor-skill.zip` der offizielle Weg.

- **Claude** ([Checkliste](https://claude.com/docs/plugins/pre-submission-checklist)): bezahlter claude.ai-Tarif. In [claude.ai/directory/manage](https://claude.ai/directory/manage) „Submit new“ → „Plugin bundle“, Repository `Sae-l/tutor`, Pluginpfad `dist/claude/plugins/tutor`, „Validate“, Befunde mit „Blocking“ beheben, einreichen. Der Name `tutor` ist allgemein und kann für eine Prüfung durch Anthropic zurückgehalten werden.
- **ChatGPT und Codex** ([Einreichung](https://developers.openai.com/plugins/deploy/submission)): Identität in den Organisationseinstellungen auf platform.openai.com verifizieren. Unter [Plugins](https://platform.openai.com/plugins) „Upload new or existing plugin“ wählen, `tutor-chatgpt.zip` hochladen, „Metadata & Skills“ prüfen, „Submit for review“ wählen und nach der Freigabe „Publish plugin“. `interface.developerName` muss zur verifizierten Identität passen.
- Jede neue Version erst nach Erhöhen von `version` in `packaging/chatgpt-plugin.json` und im Claude-Marketplace-Eintrag einreichen.
