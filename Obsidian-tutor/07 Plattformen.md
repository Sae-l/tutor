---
title: Claude, ChatGPT und Gemini
tags: [tutor, kompatibilitaet]
updated: 2026-10-27
status: abnahme-offen
---

# Betrieb auf drei Plattformen

← [[00 Startseite]] · [[12 Abnahmeplan]]

> [!warning] Umfang einer Zusicherung
> Textanweisungen garantieren keine Regeltreue über alle Modelle und Oberflächenversionen hinweg. Lokal prüfbar sind Dateigleichheit, Build und festgelegte Strukturregeln. Verhalten und Darstellung benötigen eine Abnahme je Oberfläche, Version und Modell sowie Wiederholungen bei Änderungen.

## Aktueller Nachweisstand

| Weg | Vorhanden | Lokaler Nachweis | Bewertung |
|---|---|---|---|
| Claude Skill | Skillquelle und ZIP-Verpackungsweg | claude.ai-Protokoll vom 2026-10-27: U07…U13 mit `v0.3.0-rc.2` bestanden (U08 mit Anmerkung). Älter: Claude-Code-CLI vom 2026-10-15, 16 Fälle, drei fehlgeschlagen | Teilabnahme; U01…U06, U14 und der A/B-Vergleich (#67) stehen aus, Gate nicht erfüllt. |
| ChatGPT Plugin | `dist/tutor-chatgpt.zip` und lokaler Marketplace | Vorbereitungsprotokoll: automatischer Import nicht abgeschlossen. Separater freier Test: Skill und Plugin verwendet, jedoch Modell, Hash und Installationsversion nicht erfasst | Teilversuch mit Abweichungen; keine Abnahme. |
| ChatGPT Projekt | `dist/kern.md` und `dist/system-prompt.md` | Anleitung und geplante Fälle; kein eigener vollständiger Abnahmelauf gefunden | Experimentell. |
| Gemini Skill (Hauptweg) | Vorhandenes `tutor-skill.zip`; kein eigenes Gemini-Paket | Kein Tutor-Import oder Modellergebnis gefunden | Dokumentiert, experimentell, nicht geprüft. |
| Gemini Gem (auslaufend) | Kern und System-Prompt als Wissen | Kein Gemini-Ausführungsprotokoll gefunden | Nicht geprüft; endet für private Konten ab November 2026, Workspace 2027. |

Das freie ChatGPT-Protokoll war bei der Vault-Erstellung lokal unversioniert; eine Veröffentlichung auf GitHub wird nicht vorausgesetzt. Modellnamen im Claude-Protokoll sind Angaben des damaligen Laufs; ihre heutige Verfügbarkeit wurde nicht geprüft.

Die GitHub-Abfrage vom 2026-10-27 bestätigt die fünf Pakete der [Vorabversion v0.3.0-rc.3](https://github.com/Sae-l/tutor/releases/tag/v0.3.0-rc.3). Sie bestätigt weder die Installation im jeweiligen Konto noch das Verhalten eines Modells. Die Release-Assets wurden für diese Aktualisierung nicht heruntergeladen oder neu ausgeführt.

Stand 2026-10-28: Aktuelle Version ist [v0.3.0-rc.5](https://github.com/Sae-l/tutor/releases/tag/v0.3.0-rc.5) mit Persisch und den Korrekturen aus dem Protokoll G29/D3, auf GitHub als „Latest“ veröffentlicht; die vorherigen Versionen [v0.3.0-rc.4](https://github.com/Sae-l/tutor/releases/tag/v0.3.0-rc.4), [v0.3.0-rc.3](https://github.com/Sae-l/tutor/releases/tag/v0.3.0-rc.3) und [v0.2.1](https://github.com/Sae-l/tutor/releases/tag/v0.2.1) bleiben abrufbar. Ab rc.3 unterscheiden sich die Pakete bei Formelzeichen im Fließtext: `tutor-skill.zip` (Claude, Gemini) setzt einzelne Formelzeichen als `$…$`, `tutor-chatgpt.zip` und die Promptdateien schreiben sie kursiv mit Unicode-Index (*U*₀), weil einfaches `$` in ChatGPT nicht rendert. Grundlage ist ein Darstellungstest vom 2026-10-27; der Akzeptanzfall U14 ist nicht nativ geprüft.

## Claude: Skill einrichten

1. `tutor-skill.zip` aus der vorgesehenen Projektversion beziehen und Inhalt sowie Hash prüfen.
2. Nach der [offiziellen Claude-Anleitung](https://support.claude.com/en/articles/12512180-use-skills-in-claude) Code-Ausführung und Dateierstellung aktivieren; unter Customize → Skills das ZIP mit Skillordner hochladen.
3. Für den Test nur Tutor aktivieren und ein neues Gespräch öffnen. `tutor`, anschließend eine Aufgabe mit `tipp` und danach `lösung` senden.
4. Das vollständige Gate aus `tests/akzeptanz.md` einschließlich Bildern, Formeln und Sprachen ausführen. Einen CLI-Lauf nicht auf Web oder Mobilgerät übertragen.

Bei Bedarf lokal aus dem letzten Commit bauen, aus der Repository-Wurzel:

```powershell
git archive --format=zip -o tutor-skill.zip HEAD tutor/
Get-FileHash -Algorithm SHA256 tutor-skill.zip
```

Dieser Befehl verwendet **HEAD**, ohne uncommittete Änderungen. Die getestete Datei muss zum protokollierten Commit passen; sie bildet einen veränderten Arbeitsbaum nicht automatisch ab.

## ChatGPT: Projekt

1. Ein eigenes, nicht geteiltes Testprojekt anlegen.
2. Den Inhalt von `dist/kern.md` in die Projektanweisungen kopieren und `dist/system-prompt.md` als Datei ergänzen.
3. Im Projekt ein neues Gespräch beginnen; `hilfe`, `tipp`, Sprache und Dauermodus prüfen.
4. Die Projektfälle aus [[12 Abnahmeplan]] ausführen. Die [offizielle Projektanleitung](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) beschreibt Dateien und Anweisungen. Ein Upload beweist nicht, dass alle Abschnitte gelesen wurden.

## ChatGPT: Plugin

`docs/CHATGPT.md` beschreibt den Import von `dist/tutor-chatgpt.zip` als Workspace-Admin-Funktion (für Plus/Pro nicht belegt), einen lokalen Marketplace für ChatGPT Desktop sowie die Installation über `/plugins` in der Codex CLI. Die [offizielle Anleitung Build skills](https://learn.chatgpt.com/docs/build-skills) erläutert die Plattform. Verfügbarkeit hängt von Konto und Oberfläche ab.

Mit `@tutor` auswählen und `hilfe` senden; automatische Aktivierung separat testen. Während der Messung keinen zusätzlichen Tutor-Projektprompt verwenden. Kopierte Dateien oder eine Auswahl über `@` belegen weder automatische Aktivierung noch korrekte Grafiken. Bei der Vault-Erstellung wurden weder Browserrechte verändert noch Dateien hochgeladen.

## Gemini: Skill (Hauptweg)

Die [offizielle Skill-Anleitung](https://support.google.com/gemini/answer/17094296?hl=en) beschreibt den Import unter Einstellungen → Skills → Erstellen: `SKILL.md`, Ordner oder ZIP mit `SKILL.md` im Hauptordner; Name gleich Ordnername, höchstens 100 MB. README und Website nennen dafür das vorhandene `tutor-skill.zip`. Offen ist, ob Gemini das ZIP mit dem Ordner `tutor/` an oberster Stelle annimmt. Erst mit diesem ZIP testen; nur bei Fehlschlag ein eigenes Gemini-Paket bauen.

Voraussetzungen laut Google: 18+, aktiviertes „Keep Activity“, Hochladen nur im Web oder in der Mac-App; Aufruf mit `/` oder `@`, sonst automatische Auswahl. „Keep Activity“ betrifft die Datenentscheidung im eigenen Konto; diese Dokumentation verändert keine Aktivitätseinstellung. Nach der Installation explizite und automatische Aktivierung, Modulzugriff und dieselben Verhaltensfälle getrennt prüfen. Es liegt kein Testergebnis für Tutor vor.

## Gemini: Gem-Weg (auslaufend)

Gems werden laut [Google](https://support.google.com/gemini/answer/18560919) für private Konten ab November 2026 und für Workspace 2027 in Skills umgewandelt. Der Weg bleibt nur bis dahin als Zusatz.

1. In Gemini Gems → New Gem öffnen.
2. `kern.md` als Anweisung und `system-prompt.md` unter Knowledge → Add files hinzufügen; speichern.
3. Den gespeicherten Gem in einem neuen Gespräch prüfen. Automatisches Umschreiben darf den ursprünglichen Kern und seine Schutzregeln nicht unbemerkt ersetzen.
4. Die hier vorgeschlagene Gemini-Fallgruppe aus [[12 Abnahmeplan]] ausführen. Sie ist noch kein bestehendes Repository-Gate.

Anweisungen und Dateiquellen beschreibt die [offizielle Google-Anleitung](https://support.google.com/gemini/answer/15146780?hl=en). Eine bereinigte lokale Datei genügt; eine Google-Drive-Verknüpfung ist dafür nicht erforderlich.

## Unterschiede gezielt prüfen

| Fähigkeit | Erforderlicher Nachweis |
|---|---|
| `$$`-Formeln, ASCII und Einheiten | Tatsächliche Darstellung statt reiner Textprüfung. |
| Arabisch und Persisch mit RTL | Textreihenfolge, deutsche Begriffe und getrennte Formeln; bereinigter Screenshot. |
| Zeichnen | Beschriftetes Bild mit Werkzeug oder Beschreibung, Tabelle und Code ohne Werkzeug; keine unbelegte Ausführung behaupten. |
| Zustand | Sprache und Dauermodus über Nachrichten; Einzelbefehl ändert gespeicherten Zustand nicht. |
| Kontextgrenzen und Speicher | Getrennte Gespräche und Wiederholung; keine unbegrenzte Persistenz annehmen. |

Anleitungen erneut geprüft am 2026-10-16; am 2026-10-20 nach `docs/planung/2026-10-20-plattform-anforderungen.md` angeglichen: Gemini-Skill mit `tutor-skill.zip` als Hauptweg, Gem auslaufend. Zur Vault-Erstellung wurde Tutor auf keiner Plattform im Benutzerkonto ausgeführt. Historie und geplante Architektur: [[19 Entscheidungen und Gesprächskontext]].
