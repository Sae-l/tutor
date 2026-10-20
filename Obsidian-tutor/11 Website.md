---
title: Die Website erklärt
tags: [tutor, website]
updated: 2026-10-19
---

# Die Website

← [[00 Startseite]] · [[09 Besucher und Inhalte]]

Die README verweist auf die [Tutor-Website](https://sae-l.github.io/tutor/). Maßgebliche lokale Quelle ist `tutor/docs/index.html`, nicht die separate Kopie `landing/index.html`. `CLAUDE.md` beschreibt GitHub Pages aus `main` und `/docs`. Beim erneuten HTTPS-Abruf am 2026-10-16 antwortete die Website mit **HTTP 200**; der HTML-Text entspricht nach Vereinheitlichung von CRLF/LF der lokalen Quelle. Das bestätigt den ausgelieferten Text, nicht Darstellung oder Interaktion im Browser. Die Pages-Konfigurations-API antwortete ohne Anmeldung mit 404; daraus wird kein fehlendes Deployment abgeleitet.

## Zweck und Inhalte

Die statische Seite erklärt den Tutor und bietet Downloads. Sie betreibt keinen Chat und führt Tutor nicht im Browser aus. Das Lernen findet nach der Einrichtung auf einer KI-Plattform statt.

| Abschnitt der Quelle | Nutzen für Besucher |
|---|---|
| Einstieg und Download | Zweck, Zielgruppe und Version; Downloadlink auf `v0.2.0` festgelegt; Veröffentlichung separat prüfen. |
| Schrittweise Hilfe | Flowchart „Verstanden?“ mit den Wegen check sowie tipp → voll → kurz, darunter die vier Stufen als Liste. |
| 11 Modi | Befehle vergleichen und auswählen. |
| Sprachbeispiel | Fest hinterlegtes Beispiel in de/ar/tr/fr/en/ur mit deutschen Fachbegriffen. |
| Einrichtung | Claude Skill und experimentelle ChatGPT-/Gemini-Wege. |
| Unter der Haube | Build-Weg von `tutor/` über `build.py` zu den Paketen; Kennzahlen 11 Modi, 6 Erklärsprachen, 30 Modus- und 33 Grenzfälle. |
| Häufige Fragen | Aktivierung, Sprache und Art des Produkts. |
| Ehrlich gesagt | Erste stabile Version ohne Abnahme, Prüfgrenzen und ADHS als Gestaltungsziel. |
| Fußbereich | Marke mit PayPal-Unterstützung, GitHub (Quellcode, Probleme und Wünsche, Changelog, Wissensbasis), Über mich (LinkedIn, Instagram), Datenschutz; Abschlusszeile mit MIT-Lizenz und Version. |

## Gestaltung seit 2026-10-19

```mermaid
flowchart TD
    N["Fester Kopf mit Lesefortschritt und aktivem Abschnitt"] --> H["Einstieg: Karopapier, Skizzen zeichnen sich einmal"]
    H --> A["Ablauf: Flowchart baut sich beim ersten Sichtkontakt auf"]
    A --> M["11 Modi"] --> S["Sprachbeispiel"] --> E["Einrichten"]
    E --> T["Unter der Haube: Build-Weg und Kennzahlen"] --> F["Fragen und Stand"]
```

- Hell- und Dunkelmodus folgen der Systemeinstellung; Farben stehen als CSS-Variablen in `:root`, Inline-SVGs nutzen dieselben Variablen.
- Bewegung nur einmalig und nur mit `transform`, `opacity` und Strichlänge; keine Endlosschleifen. `prefers-reduced-motion` zeigt alles sofort und vollständig.
- Neu: Sprunglink zum Inhalt, Favicon als Daten-URI, Open-Graph-Angaben. Weiterhin keine externen Schriften oder Skripte.
- Die README zeigt einen Ausschnitt der Seite (`docs/assets/hero-light.png`, `hero-dark.png`) und zwei Mermaid-Flowcharts.
- Geprüft: lokale Darstellung in Chrome (hell, dunkel, reduzierte Bewegung, schmale Ansicht) und Strukturtests. Nicht geprüft: das veröffentlichte GitHub-Pages-Deployment.

## Technische Funktionsweise

- HTML, CSS und JavaScript in einer Seite; lokale WOFF2-Schriften und OFL-Lizenzen unter `docs/fonts/`.
- JavaScript wechselt vordefinierte Sprachbeispiele, setzt `lang` und für Arabisch/Urdu `dir` und erzeugt Fachbegriffstabellen mit DOM-Funktionen und `textContent`.
- Kopierknöpfe verwenden `navigator.clipboard` und zeigen einen Fehlerzustand an. Elemente werden mit `IntersectionObserver` eingeblendet; dafür gibt es einen Ersatzpfad bei fehlender Unterstützung.
- Im geprüften Quelltext wurden keine `fetch`-Aufrufe, externen Trackingskripte oder Uploadformulare gefunden. Das ist eine Quelltextbeobachtung, kein Mitschnitt des tatsächlichen Netzwerkverkehrs. GitHub-Hosting und externe Links haben einen eigenen Datenschutzkontext.

## Dokumentierter Synchronisationsbedarf

In rc.3 nennt die Website **30 Modusfälle, 33 Grenzfälle und 12 Schutzregressionen**, verlinkt den öffentlichen Vault und bewahrt den Status „nicht abgenommen“. Die frühere Abweichung 32/33 ist damit in der Quelle korrigiert. Deployment und tatsächlich gelieferte Dateien separat prüfen; historische Live-Nachweise bleiben datiert.

## Website später ändern

1. `docs/index.html` als Quelle ändern; Deutsch als Besuchersprache und die vorhandenen Sprachbeispiele erhalten.
2. Version, Paketlinks, Moduszahl und Prüfstatus mit README und Protokollen abgleichen.
3. Mobilansicht, Tastaturbedienung, Kontrast, Kopieren, Links und RTL prüfen. Beim Sprachwechsel müssen deutsche Überschriften erhalten bleiben.
4. Nach dem Deployment die tatsächliche Website prüfen. Eine lokale Vorschau belegt kein erfolgreiches GitHub-Pages-Deployment.

Diese Notiz erklärt und bewertet die Quelle. Website und Deployment wurden durch die Vault-Aktualisierung nicht geändert. HTTP-Ergebnis und Vergleichshashes stehen in [[Live-Nachweise.json|Live-Nachweise.json]]; eine neue Browser-, Mobil- oder Barrierefreiheitsprüfung fand nicht statt.
