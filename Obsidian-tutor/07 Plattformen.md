---
title: Claude, ChatGPT und Gemini
tags: [tutor, kompatibilitaet]
updated: 2026-10-16
status: abnahme-offen
---

# Betrieb auf drei Plattformen

← [[00 Startseite]] · [[12 Abnahmeplan]]

> [!warning] Umfang einer Zusicherung
> Textanweisungen garantieren keine Regeltreue über alle Modelle und Oberflächenversionen hinweg. Lokal prüfbar sind Dateigleichheit, Build und festgelegte Strukturregeln. Verhalten und Darstellung benötigen eine Abnahme je Oberfläche, Version und Modell sowie Wiederholungen bei Änderungen.

## Aktueller Nachweisstand

| Weg | Vorhanden | Lokaler Nachweis | Bewertung |
|---|---|---|---|
| Claude Skill | Skillquelle und ZIP-Verpackungsweg | Claude-Code-CLI-Protokoll vom 2026-10-15: 16 Fälle, 13 bestanden und drei fehlgeschlagen, älterer Commit | Erfüllt nicht das Gate für einen auf claude.ai hochgeladenen Skill. |
| ChatGPT Plugin | `dist/tutor-chatgpt.zip` und lokaler Marketplace | Vorbereitungsprotokoll: automatischer Import nicht abgeschlossen. Separater freier Test: Skill und Plugin verwendet, jedoch Modell, Hash und Installationsversion nicht erfasst | Teilversuch mit Abweichungen; keine Abnahme. |
| ChatGPT Projekt | `dist/kern.md` und `dist/system-prompt.md` | Anleitung und geplante Fälle; kein eigener vollständiger Abnahmelauf gefunden | Experimentell. |
| Gemini Gem | Kern und System-Prompt als Wissen | Kein Gemini-Ausführungsprotokoll gefunden | Nicht geprüft. |
| Gemini nativer Skill | In der Plattformplanung vorgesehen; noch kein `dist/tutor-gemini.zip` | Kein Tutor-Import oder Modellergebnis gefunden | Vorgeschlagen, nicht implementiert oder abgenommen. |

Das freie ChatGPT-Protokoll war bei der Vault-Erstellung lokal unversioniert; eine Veröffentlichung auf GitHub wird nicht vorausgesetzt. Modellnamen im Claude-Protokoll sind Angaben des damaligen Laufs; ihre heutige Verfügbarkeit wurde nicht geprüft.

Die erneute GitHub-Abfrage bestätigt die vorhandenen Pakete der [Vorabversion v0.2.0-rc.2](https://github.com/Sae-l/tutor/releases/tag/v0.2.0-rc.2). Sie bestätigt weder die Installation im jeweiligen Konto noch das Verhalten eines Modells. Die Release-Assets wurden für diese Aktualisierung nicht heruntergeladen oder neu ausgeführt.

## Claude: Skill einrichten

1. `tutor-skill.zip` aus der vorgesehenen Projektversion beziehen und Inhalt sowie Hash prüfen.
2. Nach der [offiziellen Claude-Anleitung](https://support.claude.com/en/articles/12512180-use-skills-in-claude) Code-Ausführung und Dateierstellung aktivieren; unter Customize → Skills das ZIP mit Skillordner hochladen.
3. Für den Test nur Tutor aktivieren und ein neues Gespräch öffnen. `tutor`, anschließend eine Aufgabe mit `tipp` und danach `lösung` senden.
4. Das vollständige Gate aus `tests/akzeptanz.md` einschließlich Bildern, Formeln und Sprachen ausführen. Einen CLI-Lauf nicht auf Web oder Mobilgerät übertragen.

Bei Bedarf lokal aus dem letzten Commit bauen, aus der Repository-Wurzel:

```powershell
git archive --format=zip --prefix=tutor/ -o tutor-skill.zip HEAD:tutor
Get-FileHash -Algorithm SHA256 tutor-skill.zip
```

Dieser Befehl verwendet **HEAD**, ohne uncommittete Änderungen. Die getestete Datei muss zum protokollierten Commit passen; sie bildet einen veränderten Arbeitsbaum nicht automatisch ab.

## ChatGPT: Projekt

1. Ein eigenes, nicht geteiltes Testprojekt anlegen.
2. Den Inhalt von `dist/kern.md` in die Projektanweisungen kopieren und `dist/system-prompt.md` als Datei ergänzen.
3. Im Projekt ein neues Gespräch beginnen; `hilfe`, `tipp`, Sprache und Dauermodus prüfen.
4. Die Projektfälle aus [[12 Abnahmeplan]] ausführen. Die [offizielle Projektanleitung](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) beschreibt Dateien und Anweisungen. Ein Upload beweist nicht, dass alle Abschnitte gelesen wurden.

## ChatGPT: Plugin

`docs/CHATGPT.md` beschreibt den Import von `dist/tutor-chatgpt.zip` über Plugins, sofern im Konto verfügbar, sowie einen lokalen Marketplace über Codex Desktop. Die [offizielle Anleitung Build skills](https://learn.chatgpt.com/docs/build-skills) erläutert die Plattform. Verfügbarkeit hängt von Konto und Oberfläche ab.

Mit `@tutor` auswählen und `hilfe` senden; automatische Aktivierung separat testen. Während der Messung keinen zusätzlichen Tutor-Projektprompt verwenden. Kopierte Dateien oder eine Auswahl über `@` belegen weder automatische Aktivierung noch korrekte Grafiken. Bei der Vault-Erstellung wurden weder Browserrechte verändert noch Dateien hochgeladen.

## Gemini: nativer Skill

Die [offizielle Skill-Anleitung](https://support.google.com/gemini/answer/17094296?hl=en) beschreibt den Import unter Customize → Skills → Upload: `SKILL.md` im Hauptordner sowie Referenzen gemeinsam hochladen. Für Tutor ist ein entsprechendes ZIP mit unveränderten Quellen geplant; `build.py` erzeugt es noch nicht. Claude- und ChatGPT-Archive nicht ungeprüft als Gemini-Paket bezeichnen.

Google nennt aktuell ein aktiviertes „Keep Activity“ als Voraussetzung. Das betrifft die Datenentscheidung im eigenen Konto; diese Dokumentation verändert keine Aktivitätseinstellung. Nach verfügbarer Installation explizite und automatische Aktivierung, Modulzugriff und dieselben Verhaltensfälle getrennt prüfen. Es liegt kein Testergebnis für Tutor vor.

## Gemini: bisheriger Gem-Weg

1. In Gemini Gems → New Gem öffnen.
2. `kern.md` als Anweisung und `system-prompt.md` unter Knowledge → Add files hinzufügen; speichern.
3. Den gespeicherten Gem in einem neuen Gespräch prüfen. Automatisches Umschreiben darf den ursprünglichen Kern und seine Schutzregeln nicht unbemerkt ersetzen.
4. Die hier vorgeschlagene Gemini-Fallgruppe aus [[12 Abnahmeplan]] ausführen. Sie ist noch kein bestehendes Repository-Gate.

Anweisungen und Dateiquellen beschreibt die [offizielle Google-Anleitung](https://support.google.com/gemini/answer/15146780?hl=en). Eine bereinigte lokale Datei genügt; eine Google-Drive-Verknüpfung ist dafür nicht erforderlich.

## Unterschiede gezielt prüfen

| Fähigkeit | Erforderlicher Nachweis |
|---|---|
| `$$`-Formeln, ASCII und Einheiten | Tatsächliche Darstellung statt reiner Textprüfung. |
| Arabisch und Urdu mit RTL | Textreihenfolge, deutsche Begriffe und getrennte Formeln; bereinigter Screenshot. |
| Zeichnen | Beschriftetes Bild mit Werkzeug oder Beschreibung, Tabelle und Code ohne Werkzeug; keine unbelegte Ausführung behaupten. |
| Zustand | Sprache und Dauermodus über Nachrichten; Einzelbefehl ändert gespeicherten Zustand nicht. |
| Kontextgrenzen und Speicher | Getrennte Gespräche und Wiederholung; keine unbegrenzte Persistenz annehmen. |

Anleitungen erneut geprüft am 2026-10-16; nativen Gemini-Skillweg ergänzt. Zur Vault-Erstellung wurde Tutor auf keiner Plattform im Benutzerkonto ausgeführt. Historie und geplante Architektur: [[19 Entscheidungen und Gesprächskontext]].
