---
title: Die Website erklärt
tags: [tutor, website]
updated: 2026-10-16
---

# Die Website

← [[00 Startseite]] · [[09 Besucher und Inhalte]]

Die README verweist auf die [Tutor-Website](https://sae-l.github.io/tutor/). Maßgebliche lokale Quelle ist `tutor/docs/index.html`, nicht die separate Kopie `landing/index.html`. `CLAUDE.md` beschreibt GitHub Pages aus `main` und `/docs`. Beim erneuten HTTPS-Abruf am 2026-10-16 antwortete die Website mit **HTTP 200**; der HTML-Text entspricht nach Vereinheitlichung von CRLF/LF der lokalen Quelle. Das bestätigt den ausgelieferten Text, nicht Darstellung oder Interaktion im Browser. Die Pages-Konfigurations-API antwortete ohne Anmeldung mit 404; daraus wird kein fehlendes Deployment abgeleitet.

## Zweck und Inhalte

Die statische Seite erklärt den Tutor und bietet Downloads. Sie betreibt keinen Chat und führt Tutor nicht im Browser aus. Das Lernen findet nach der Einrichtung auf einer KI-Plattform statt.

| Abschnitt der Quelle | Nutzen für Besucher |
|---|---|
| Einstieg und Download | Zweck, Zielgruppe und Version; lokaler Downloadlink auf `v0.2.0-rc.2` festgelegt. |
| Schrittweise Hilfe | Übergang zwischen Verständnis, Leitfragen, Beispiel und Lösung. |
| 11 Modi | Befehle vergleichen und auswählen. |
| Sprachbeispiel | Fest hinterlegtes Beispiel in de/ar/tr/fr/en/ur mit deutschen Fachbegriffen. |
| Einrichtung | Claude Skill und experimentelle ChatGPT-/Gemini-Wege. |
| Häufige Fragen | Aktivierung, Sprache und Art des Produkts. |
| Ehrlich gesagt | Vorabversion, Prüfgrenzen und ADHS als Gestaltungsziel. |
| Fußbereich | Datenschutz, GitHub, Feedback und MIT. |

## Technische Funktionsweise

- HTML, CSS und JavaScript in einer Seite; lokale WOFF2-Schriften und OFL-Lizenzen unter `docs/fonts/`.
- JavaScript wechselt vordefinierte Sprachbeispiele, setzt `lang` und für Arabisch/Urdu `dir` und erzeugt Fachbegriffstabellen mit DOM-Funktionen und `textContent`.
- Kopierknöpfe verwenden `navigator.clipboard` und zeigen einen Fehlerzustand an. Elemente werden mit `IntersectionObserver` eingeblendet; dafür gibt es einen Ersatzpfad bei fehlender Unterstützung.
- Im geprüften Quelltext wurden keine `fetch`-Aufrufe, externen Trackingskripte oder Uploadformulare gefunden. Das ist eine Quelltextbeobachtung, kein Mitschnitt des tatsächlichen Netzwerkverkehrs. GitHub-Hosting und externe Links haben einen eigenen Datenschutzkontext.

## Dokumentierter Synchronisationsbedarf

Der lokale und der erneut abgerufene öffentliche Statusabschnitt nennen **30 Modusfälle und 32 Grenzfälle**. Die aktuelle `tests/akzeptanz.md` enthält **30 + 33** sowie Darstellungs- und Pluginfälle. Auch spätere Teilversuche sind dort nicht vollständig abgebildet. Ein korrigierter Zähler rechtfertigt keine Änderung von „nicht abgenommen“ zu „garantiert“.

## Website später ändern

1. `docs/index.html` als Quelle ändern; Deutsch als Besuchersprache und die vorhandenen Sprachbeispiele erhalten.
2. Version, Paketlinks, Moduszahl und Prüfstatus mit README und Protokollen abgleichen.
3. Mobilansicht, Tastaturbedienung, Kontrast, Kopieren, Links und RTL prüfen. Beim Sprachwechsel müssen deutsche Überschriften erhalten bleiben.
4. Nach dem Deployment die tatsächliche Website prüfen. Eine lokale Vorschau belegt kein erfolgreiches GitHub-Pages-Deployment.

Diese Notiz erklärt und bewertet die Quelle. Website und Deployment wurden durch die Vault-Aktualisierung nicht geändert. HTTP-Ergebnis und Vergleichshashes stehen in [[Live-Nachweise.json|Live-Nachweise.json]]; eine neue Browser-, Mobil- oder Barrierefreiheitsprüfung fand nicht statt.
