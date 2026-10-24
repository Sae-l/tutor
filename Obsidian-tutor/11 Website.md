---
title: Die Website erklärt
tags: [tutor, website]
updated: 2026-10-24
---

# Die Website

← [[00 Startseite]] · [[09 Besucher und Inhalte]]

Die [Tutor-Website](https://sae-l.github.io/tutor/) ist eine statische Besucherseite. Sie führt keinen Chat aus. Die maßgeblichen Quellen sind `docs/index.html`, `docs/styles.css` und `docs/site.js` im Repository. GitHub Pages veröffentlicht aus `main`, Ordner `/docs`; es ist kein Website-Build nötig.

## Besucherführung

| Abschnitt | Nutzen |
|---|---|
| Einstieg | Zielgruppe, Vorabversion und direkter Weg zur Einrichtung |
| Beispielansicht | Redaktionelles Physikbeispiel mit technischer SVG-Skizze; erklär, tipp und check per Radioknopf vergleichen |
| Lernweg | Vier abgestufte Hilfen; check für einen eigenen Versuch |
| Moduswahl | Vom Anliegen zum Befehl; alle elf Modi samt Lösungsgrenzen aufklappbar |
| Sprachen | Sechs Erklärsprachen, deutsche Voreinstellung und ausdrücklicher Wechsel |
| Einrichtung | Claude-Webweg mit direktem Release-Download; andere Plattformen mit Anleitungen und Prüfgrenzen |
| Transparenz und Fragen | Technische Nachweise, offene native Abnahme, Datenschutz und Feedback |
| Fußbereich | Dokumentation, Wissensbasis, Quellcode, Lizenz und Kontakt |

Die README ist der kurze Repositoryeinstieg; `docs/README.md` führt zu Plattformanleitungen, Konzept, Nachweisen und Entwicklung. Quellordner wurden nicht verschoben. Bestehende Abschnittsanker bleiben erhalten.

## Gestaltung und Bedienung

- Lokale Geist- und Monospace-Schriften, Arabisch und Urdu mit eigenen lokalen Schriftdateien samt OFL-Lizenzen. Keine externen Skripte oder Schriften.
- Ruhige Typografie, klare Abstände, Grün auf heller oder dunkler Fläche. Das Farbschema folgt dem System.
- Native Radioknöpfe und Details-Blöcke, Sprunglink, sichtbarer Tastaturfokus und mobile Navigation mit Escape-Rückkehr.
- Keine automatisch laufende Animation. Der kurze Antwortwechsel wird nur ohne Wunsch nach reduzierter Bewegung animiert.
- Ohne JavaScript bleiben Einstieg, Standardbeispiel, Modusliste, Einrichtung, FAQ und Links nutzbar; Kopier- und Wechselknöpfe erscheinen erst mit JavaScript.
- Kopieren meldet Erfolg oder eine manuelle Alternative. Die Beispieltexte sind ausdrücklich redaktionell, kein Live-Chat und kein Beleg für eine Modellantwort.

## Nachweise und Grenzen

Die datierten Release-Nachweise in [[Veröffentlichung-v0.3.0-rc.1.json|Veröffentlichung-v0.3.0-rc.1.json]] gehören zum veröffentlichten Paketstand. Die neue Besucherseite ändert keine Tutor-Pakete und ist separat zu prüfen. Historische Abrufvergleiche bleiben datiert.

Die aktuelle Websiteprüfung steht in `tests/protokolle/2026-10-24-website.md`. Sie unterscheidet lokale Browserprüfung und späteren Pages-Abruf. Keine formale Barrierefreiheitszertifizierung und keine Tutor-Modellabnahme daraus ableiten.

## Bei späteren Änderungen

1. HTML, CSS und JavaScript gemeinsam betrachten; Beispiele und Downloadversion mit README und Release abgleichen.
2. Mobile Breiten, Tastatur, Fokus, RTL, Kopierfehler und Verhalten ohne JavaScript prüfen.
3. Quellhashes nach Bewertung der betroffenen Notizen erneuern.
4. Nach Veröffentlichung HTML und Ressourcen von GitHub Pages erneut abrufen. Lokale Vorschau ist kein Deploymentnachweis.
