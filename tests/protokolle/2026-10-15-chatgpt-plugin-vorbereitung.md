# ChatGPT-Plugin: lokale Vorbereitung und blockierter Import, 15.10.2026

**Kein Plattform-Pass.** Der Build ist umgesetzt; kein Tutor wurde im Zielmodell ausgeführt.

| Feld | Wert |
|---|---|
| Gitbasis | `60b97a3ad6a5492887f1194d312908a9d7561129` |
| Änderungsstand | Commit dieses Protokolls auf `feat/chatgpt-compatibility` |
| Pluginversion | `0.2.0-rc.2`, unveröffentlicht |
| Artefakt | `dist/tutor-chatgpt.zip` |
| SHA-256 ZIP | `d6f6d1031d1e6d43b9a5a2a4d7ff839a2273a9cc90a53b0b7112dda6382e6179` |
| ZIP-Größe | 43118 Bytes |
| Oberfläche | ChatGPT Web in Google Chrome, deutsche Oberfläche |
| Modell | nicht ausgewählt; kein Modellaufruf |
| Strukturtest | 13 Tests erfolgreich, Windows, gebündeltes Python 3.14 |
| Kern | 3997 Zeichen, internes Limit 4000 |

## Beobachtung und Blocker

Auf `https://chatgpt.com/plugins` waren `Hinzufügen` und `Plugin-Archiv hochladen` sichtbar. Der folgende Dialog hieß `Neues Plugin`, enthielt `klicke zum Hochladen` und akzeptierte laut UI .tar.gz, .tgz und .zip bis 100 MB.

Der erste Uploadversuch wurde durch die automatische Freigabeprüfung abgelehnt, weil die Übertragung möglicherweise privater Quelldateien nicht ausdrücklich autorisiert war. Danach erlaubte der Lernende ausdrücklich `ZIP hochladen und testen` für das erzeugte Archiv mit 16 Tutor-Quelldateien, Manifest und Lizenz.

Der anschließend freigegebene Upload scheiterte technisch bei der Dateiauswahl: Die ChatGPT-Chrome-Erweiterung verlangt `Allow access to file URLs`. Der Dateiupload konnte deshalb nicht ausgeführt werden. Es gibt weder eine Importbestätigung noch eine Installerfehlermeldung zum Paketformat. Die erforderliche Erweiterungsberechtigung wurde nicht automatisch verändert. Als alternative Fortsetzung kann der Lernende das ZIP von Hand im bereits beschriebenen Importdialog auswählen.

## Lokale Prüfungen

`python build.py` und `python -B -m unittest discover -s tests -v` erfolgreich (13 Fälle). Zusätzlich ein frischer Checkout des vorgemerkten Git-Stands per `git checkout-index`: dieselben 13 Tests erfolgreich (`FRESH_INDEX_CHECKOUT_PASS`). Geprüft: alle erzeugten Dateien einschließlich ZIP wiederholbar; ZIP exakt 18 Dateien (16 Skillquellen, Manifest, MIT-Lizenz); native Skillbytes gleich Quelle; keine ungefragten Dateien; alte Paketdateien entfernt; ungültige Metadaten vor Ausgabe abgewiesen, auch unter `-O`; vorherige Ausgabe bei simuliertem Veröffentlichungsfehler wiederhergestellt. Keine Aussage über Linux-Runner oder ein Modell.

## Native Zieloberflächenfälle

Keiner der Fälle wurde an ein Modell gesendet; deshalb keine Antwort und kein bestanden/nicht-bestanden-Urteil erfinden. H01 umfasst den erfolgreichen Import und die Aktivierung und bleibt trotz erreichbarem Importdialog offen. D4 ist nur informativ und ebenfalls offen. Der Projektweg wurde nicht ausgeführt.

| Fall | Urteil | Grund |
|---|---|---|
| H01 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| H02 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| H03 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| H04 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| H05 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M01-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M02-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M03-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M04-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M05-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M06-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M07-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M08-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M09-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| M10-B | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G02 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G03 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G05 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G13 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G25 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G26 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G28 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G29 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G32 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| G33 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| D1 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| D2 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |
| D3 | nicht geprüft | Import durch Chrome-Dateizugriff blockiert |

## Dateihashes der lokalen Marketplace-Ausgabe

```text
e78bcf52d9671e3221d89046433a92eac50d63095156cd1573cfd1f8afeb9f63  dist/chatgpt/.agents/plugins/marketplace.json
eec82d4840d0597cb2e8825b1f9097e2587adba3de6f425c0a10e667eb972c6b  dist/chatgpt/plugins/tutor/LICENSE
edb600fb5f83ff111daa4a758bfa62c7629b20a4a10a78fba473887d5abf782f  dist/chatgpt/plugins/tutor/plugin.json
752478dddc6246fa89216a44a2d0b4c528d466d4bc28bd1f5f2c1a2b62173422  dist/chatgpt/plugins/tutor/skills/tutor/modes/check.md
ab51f39d975a8f400bd7448a299ba2ca4e15acb370e914bd185b7c00313840d8  dist/chatgpt/plugins/tutor/skills/tutor/modes/erklaer.md
a494dbcac54f16b843d67f57d4760ac932d4bd62cf5c59316808bdc15fb912d9  dist/chatgpt/plugins/tutor/skills/tutor/modes/hilfe.md
e3d7b2f5d11e647046dad344cb9d928f00711e0a9c1099c15e81d0805ec212bc  dist/chatgpt/plugins/tutor/skills/tutor/modes/klausur.md
298a86dd2a9bd554855de06152432d1153d5676814dc1c8c2e62fe63ca1a5364  dist/chatgpt/plugins/tutor/skills/tutor/modes/kurz.md
64d031f42d504745b9d90697c831aa57062a0bd2dd920af4b53bae44db92ea1d  dist/chatgpt/plugins/tutor/skills/tutor/modes/lang.md
66be8518e15872bff72b350899a3a8961a15c791d359182a58aabf4488bba7a0  dist/chatgpt/plugins/tutor/skills/tutor/modes/mittel.md
a4b93c5753788c087f051e68f776864b11ff0835772e234eeb48037bad2e8f2f  dist/chatgpt/plugins/tutor/skills/tutor/modes/skizze.md
3d71ed8acdaa878d473dbcc2fbac236e23b66e6976a35056274883c9915f5a3f  dist/chatgpt/plugins/tutor/skills/tutor/modes/thema.md
c9d04fba3b75538ea20c40c624c8258202d0a53a113cd5e469cad00922066a84  dist/chatgpt/plugins/tutor/skills/tutor/modes/tipp.md
cfe92487ac3e96aa534d9e4d5e9bdaa116a2139496a4ffcfdd1c9a0deeba3e19  dist/chatgpt/plugins/tutor/skills/tutor/modes/voll.md
5b8dd6f0754d83353bff456c98d90adaf15c39cb5d550c64ad00a00eb224523b  dist/chatgpt/plugins/tutor/skills/tutor/references/antwortvorlage.md
bcce7eb30fff0a0708022bc6aea68fd41733b9219f1ba5e30df07359ef201cdd  dist/chatgpt/plugins/tutor/skills/tutor/references/didaktik.md
f194ea12b2d8c6e633a041be20bdbd379afb3907a35cc9de85011c547342e689  dist/chatgpt/plugins/tutor/skills/tutor/references/latex-regeln.md
99a137c447934292e2ed0ed6e0ec00bec55db6b2ddef569efade78640de75146  dist/chatgpt/plugins/tutor/skills/tutor/references/sprache.md
f99a12b8348c39a5c1c94b75ddd13deb1268c7c35656c7f02627302a841af469  dist/chatgpt/plugins/tutor/skills/tutor/SKILL.md
```

Alle Gate-Fälle bestanden: **nein**. Nach Aufhebung des Uploadblockers mit genau diesem Archiv nach `tests/akzeptanz.md` fortsetzen; bei neu gebautem Paket zuerst Hash aktualisieren. Die zentrale Sprachpräzisierung verlangt außerdem die bestehende vollständige Release-Wiederholung. Die älteren Claude-CLI-Befunde bleiben offen.
