---
title: Abnahme von Verhalten und Darstellung
tags: [tutor, abnahme]
updated: 2026-10-17
status: zieloberflaechen-offen
---

# Abnahmeplan

← [[00 Startseite]] · [[07 Plattformen]] · [[16 Prüfergebnis]]

## Drei Nachweisarten

| Nachweis | Aussage | Keine Aussage über |
|---|---|---|
| Build und Struktur | Quelle und Ausgaben, Dateiliste und explizit geprüfte Regeln stimmen überein | Modellverhalten, Darstellung oder Lernerfolg. |
| Oberflächenabnahme | Verhalten einer bestimmten Version mit benanntem Modell, Oberfläche und Paket | Alle Modelle, spätere Versionen oder Lernen. |
| Lernstudie | Ergebnisse bestimmter Personen, Aufgaben und Messverfahren | Wirksamkeit außerhalb des untersuchten Rahmens. |

## Fallgruppen der aktuellen Quelle

| Oberfläche | Fälle | Voraussetzung für eine Abnahme |
|---|---|---|
| Claude Skill | M01-A…M10-C = 30, G01…G33 = 33, dazu D1…D3 | Jede Teilaussage jedes Falls besteht; Protokoll für den hochgeladenen Skill. Das ist das Release-Gate. |
| ChatGPT Projekt | M01-B…M10-B, G02/G03/G05/G25/G26/G28 und Darstellung | Gilt nur für diesen Weg; keine Übertragung der Pluginbewertung. |
| ChatGPT Plugin | H01…H05, M01-B…M10-B, G02/G03/G05/G13/G25/G26/G28/G29/G32/G33, D1…D3 | Installation, Aktivierung, Verhalten und Darstellung dokumentiert; Build allein genügt nicht. |
| Gemini Gem – **hier neu vorgeschlagen** | Projektgruppe plus G13/G29/G32/G33 sowie Erstellen, Speichern und Aufrufen des Gems | Gruppe noch festlegen und ausführen; die aktuelle Quelle hat kein eigenes Gemini-Gate. |
| Gemini nativer Skill – **Architekturvorschlag** | Dieselben 63 Kernfälle und D1…D3 wie Claude, plus eigene Import-/Aktivierungsfälle | Erst Paket erzeugen und installieren; kein geltendes Repository-Gate und kein ausgeführter Lauf. |

H01…H05 gehören zum Plugin; H01 nicht als Gem-Installationstest umdeuten. D4 zum Aufklappblock ist informativ und kein Gate, da Lösungen ohnehin erst auf Abruf erscheinen. Die Kursfälle K01…K06 sind vom v0.2-Gate getrennt.

## Kurzer Vorabtest

Die selbst erstellte Matrixaufgabe verwenden: ohmscher Widerstand `2,0 kOhm`, Spannung `12 V`. Das Referenzergebnis nicht an Tutor mitsenden.

1. Neues Gespräch: `hilfe`; elf Modi anzeigen, keine Aufgabe lösen.
2. Neues Gespräch: Aufgabe mit `tipp`; Fragen ohne Gleichung oder Ergebnis. Danach `lösung`; nachvollziehbare Rechnung mit richtigen Einheiten.
3. `[ar]`, danach eine Nachricht ohne Sprachsignal; arabische Erklärung und deutsche Überschriften bleiben erhalten. RTL und Formeln tatsächlich ansehen.
4. `!an tipp`, Aufgabe, einmal `kurz`, neue Aufgabe: wieder `tipp`. `!aus` beendet den Dauermodus.
5. `check` ohne Versuch: einmal um die eigene Rechnung bitten, keine Lösung erfinden.
6. Zitierte Aufgabe mit `!kurz`, außerhalb des Zitats `tipp` verlangen: das Zitat ändert den Modus nicht.
7. `skizze`: beschriftetes Bild oder Beschreibung, Tabelle und Code passend zum verfügbaren Werkzeug.

Dieser Vorabtest ersetzt die vollständigen Gate-Fälle nicht.

## Protokoll je Fall

```text
Datum und Zeitzone:
Oberfläche, Anwendungsversion und Installationsweg:
Genauer Modellname:
Paketversion, Commit und SHA-256:
Fall-ID und Kriterien:
Eingabe und bereinigte Originalantwort:
Screenshot bei Darstellungsprüfung:
Urteil: bestanden / nicht bestanden / nicht geprüft, mit Grund:
Prüfer:
```

Jeden Fall in einem neuen Gespräch ohne weiteren Tutor-Prompt beginnen. Mehrere Nachrichten eines Zustandsfalls bleiben im dafür angelegten Gespräch. Ein geteiltes Gespräch belegt kein Ergebnis für ein Paket ohne erfassten Hash.

## Wiederholungsregeln

Nach Quellregel: Bei Änderung einer Modusdatei ihre drei Fachfälle und zugehörige Grenzfälle wiederholen; bei Router- oder Referenzänderungen alle Fälle. Verpackungsänderungen erfordern neue Installationstests, Plattform- oder Formeländerungen neue Darstellungsprüfungen. Modellupdates begründen eine erneute Prüfung kritischer Verhaltensregeln.

Vorhanden sind ein älterer CLI-Teillauf mit 13/16 Erfolgen und ein freier ChatGPT-Test mit Abweichungen; kein Gemini-Protokoll. Hier wird kein vollständiger Erfolg ergänzt. Einzelheiten: [[13 Quellen und Nachweise]].

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
