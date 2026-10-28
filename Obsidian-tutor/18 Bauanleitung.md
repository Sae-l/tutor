---
title: Tutor aus den Quellen bauen und weiterentwickeln
tags: [tutor, build, entwicklung]
updated: 2026-10-28
status: reproduzierbare-anleitung
---

# Bauanleitung

← [[00 Startseite]] · [[03 Umsetzung]] · [[08 Repository-Aufbau]] · [[17 Fehlerdiagnose und Reparatur]]

## Voraussetzungen und Arbeitsort

Git und Python 3.14 sind laut `CONTRIBUTING.md` die geprüften Voraussetzungen. Der Builder verwendet die Standardbibliothek. Für den Bau sind weder API-Schlüssel noch Node, Docker oder eine Datenbank erforderlich. Das Produkt bleibt ein Satz von Skillanweisungen und Paketen.

Alle Befehle beziehen sich auf die Repositorywurzel des eigenen Checkouts. Darunter enthält `tutor/` die Verhaltensquelle und `Obsidian-tutor/` die Wissensbasis.

Für eine neue Kopie die folgenden Befehle in einem leeren, selbst gewählten Zielordner ausführen. Nicht erneut in den vorhandenen Checkout klonen:

```powershell
git clone https://github.com/Sae-l/tutor.git
Set-Location tutor
git rev-parse HEAD
git status --short
python --version
python build.py
python -B -m unittest discover -s tests -v
git diff --exit-code -- dist/
git ls-files --others --exclude-standard -- dist/
```

Erwartung: Python 3.14, erfolgreicher Build und erfolgreiche Tests. Bei identischem Commit und gültigem eingechecktem Build liefert der Diff keinen Unterschied, die letzte Dateiliste bleibt leer. Die Suite umfasst am 2026-10-28 22 Tests; spätere Versionen können die Anzahl ändern. Zusätzlich `python -B Obsidian-tutor/verify_vault.py` ausführen (erwartet `PASS`). Ist `python` nicht verfügbar, den auf dem eigenen Gerät vorhandenen Interpreterpfad verwenden.

Die Suite wurde für diese Dokumentation erneut ausgeführt. Mit Python im eigenen PATH:

```powershell
# Aus der Repositorywurzel ausführen
python -B -m unittest discover -s tests -v
```

## Was der Builder tatsächlich macht

| Schritt | Eingabe und Prüfung | Ergebnis |
|---|---|---|
| Modusliste lesen | Routertabelle, genau elf eindeutige Modulnamen | Fehlende oder doppelte Module brechen den Build ab. |
| Vollprompt zusammenführen | Router, vier Referenzen und elf Modi | `dist/system-prompt.md`; Dateiverweise werden durch Abschnittsverweise ersetzt. |
| Kern extrahieren | Markierte Routerblöcke, vereinfachte Befehlstabelle | `dist/kern.md`, höchstens 4000 Zeichen; Zeichenzahl und UTF-8-Bytezahl sind verschieden. |
| Plugin erzeugen | Geprüftes Manifest, MIT-Lizenz, feste Quelldateiliste | Marketplace unter `dist/chatgpt/` und `dist/tutor-chatgpt.zip`. |
| Deterministisch verpacken | Sortierte Einträge, feste ZIP-Zeitstempel und Attribute | Wiederholbarer ChatGPT-Paketinhalt. |
| Ausgabe ersetzen | Vollständiger Bau im temporären Repositoryordner | Erst nach Validierung Austausch von `dist/`; bei fehlgeschlagenem Austausch Wiederherstellung der bisherigen Ausgabe. |

`dist/` wird vollständig ersetzt. Eigene Dateien gehören außerhalb dieses Ordners. Die Tests prüfen den Build in temporären Projektkopien; für diese Dokumentationsarbeit wurde die tatsächliche Produktausgabe nicht neu geschrieben.

## Aktuelle und geplante Pakete unterscheiden

| Ziel | Heute vorhanden | Bauweg |
|---|---|---|
| ChatGPT Plugin | `dist/tutor-chatgpt.zip` | `python build.py`; Pluginmanifest an der Archivwurzel, Skill unter `skills/tutor/`. |
| ChatGPT Projekt / Gem (auslaufend) | `dist/kern.md`, `dist/system-prompt.md` | Derselbe Builder; Einrichtung getrennt nach [[07 Plattformen]]. |
| Claude Skill und Gemini Skill | Releaseanhang `tutor-skill.zip` | Separater Git-Archivschritt aus dem Commit. Für Gemini zuerst dieses ZIP testen; ein eigenes Gemini-Paket nur bei Fehlschlag des Imports. |

Claude-Paket aus der Repositorywurzel:

```powershell
git archive --format=zip -o tutor-skill.zip HEAD tutor/
Get-FileHash -Algorithm SHA256 tutor-skill.zip
Get-FileHash -Algorithm SHA256 dist\tutor-chatgpt.zip
Get-FileHash -Algorithm SHA256 dist\kern.md
Get-FileHash -Algorithm SHA256 dist\system-prompt.md
```

Dieser Archivbefehl liest HEAD und behält den Pfadkontext für `.gitattributes` (wichtig auf Windows); `build.py` liest den Arbeitsbaum. Für Releasevergleiche muss der Checkout sauber und exakt benannt sein. Änderungen im Arbeitsbaum vor einem Commit sind im Claude-ZIP nicht enthalten. Dateinamen in einer Prüfsummenliste müssen zu den tatsächlichen heruntergeladenen Assetnamen passen; der historische Review fand hier einen Unterschied zwischen `dist/name` und `name`.

## Den Skill schrittweise weiterentwickeln

1. Eine gewünschte Verhaltensänderung mit konkreter Eingabe und erwarteter Ausgabe festlegen; [[06 Modi]] und [[17 Fehlerdiagnose und Reparatur]] lesen.
2. Router, betroffenen Modus und gemeinsame Referenzen vergleichen. Verhaltensregeln nur an ihrer Quelle pflegen; keine unabhängigen Kopien je Plattform anlegen.
3. Struktur-/Buildänderungen mit geeigneten Regressionstests prüfen. Lehrverhalten braucht Beobachtung des Modells, auch wenn der Quelltext die gewünschte Formulierung enthält.
4. Builder ausführen, generierte Dateien mit der Quelle vergleichen, Akzeptanzfälle nach Änderungsumfang wiederholen.
5. Paketversion, Changelog, Anleitung und Statusaussagen abgleichen. Einen stabilen Release erst nach dem geltenden Gate freigeben; keine alten Tags wiederverwenden.

Die gemeinsame Drei-Plattform-Architektur ist in `docs/planung/2026-10-15-plattformen/03-unified-proposal.md` beschrieben. Das heutige Repository-Gate verlangt Claude; der Vorschlag fordert zukünftig dieselben Kernfälle auf allen drei nativen Oberflächen. Diese vorgeschlagene Änderung ist noch kein geltendes Gate.

## README-Animation neu erzeugen

Nur nötig, wenn sich `docs/assets/hero/hero.html` oder Farben und Schriften der Landingpage ändern. Kein Teil von `build.py`. Voraussetzungen: `npm i -g playwright-core`, installiertes Chrome, `winget install Gyan.FFmpeg`. Dann aus der Repositorywurzel `node docs/assets/hero/render.mjs`. Einzelheiten: `docs/assets/hero/README.md`.
