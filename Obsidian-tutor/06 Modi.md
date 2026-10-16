---
title: Die elf Tutor-Modi
tags: [tutor, modi]
updated: 2026-10-16
---

# Die elf Modi

← [[00 Startseite]] · [[02 Funktionsweise]]

Die Befehlsnamen gehören zur Bedienoberfläche und werden unverändert verwendet. Beschrieben sind die Vorgaben aus `tutor/modes/`, keine garantierte Regeltreue jedes Modells.

| Befehl und Datei | Verhalten | Lösung der Originalaufgabe | Geeigneter Einsatz |
|---|---|---|---|
| `erklär` — `erklaer.md` | Idee, deutsch benannte Gesetze, allgemeines Vorgehen, Verständnisfrage und nächste Handlung. Kein gelöstes Beispiel. | Zurückgehalten; keine eingesetzten Werte oder entscheidende Umstellung. | Erster Zugang zur Aufgabe; Voreinstellung. |
| `voll` — `voll.md` | Anschauliche und mathematische Erklärung; anderes Beispiel mit anderen Zahlen und anderem Kontext; falscher Weg und Wiederholungskarte. | Original zurückgehalten; anderes Beispiel sichtbar gelöst. | Die Methode vor dem eigenen Versuch sehen. |
| `thema` — `thema.md` | Begriff, Gesetz oder Beweis; Bedingungen, Nutzen beim Lösen und Verständnisfrage. | Antwort der eigentlichen Aufgabe zurückgehalten; Auswahlaufgaben erst auf Abruf entscheiden. | Konzeptfrage oder Beweis ohne anderen Befehl. |
| `tipp` — `tipp.md` | Vier bis sechs passende Leitfragen; weder Gesetz noch Ergebnis in einer Frage verstecken. | Bis `lösung` zurückgehalten. | Selbst lösen, mit Anleitung. |
| `check` — `check.md` | Zuerst Richtiges nennen, dann den ersten Fehler mit Grund und ab dort korrigieren. Bei korrektem Versuch keinen Fehler erfinden. | Korrektur ab dem Fehler sichtbar. | Eigenen Versuch schicken; automatische Wahl ohne höherrangigen Befehl. |
| `skizze` — `skizze.md` | Mit Werkzeug beschriftete Grafik; sonst Beschreibung, Punktetabelle und TikZ- oder matplotlib-Code. | Auf die Skizze beschränkt; restliche Rechenaufgabe nicht lösen. | Kräfte oder eine Funktion darstellen. |
| `kurz` — `kurz.md` | Deutsche Klausur-Lösung mit Ansatz, Umformungen vor Zahlen, Ergebnis und genau einer Anmerkung. Keine Übungen oder Verständnisfrage. | Sichtbar. | Nach eigenem Versuch vergleichen. |
| `mittel` — `mittel.md` | Erklärung mittlerer Tiefe und vollständige Lösung; kurze Schritte, Denkpunkte und Verständnisfrage, keine Zusatzübungen. | Lösung sichtbar; Antwort auf Verständnisfrage zurückgehalten. | Erklärung zusammen mit dem Lösungsweg. |
| `lang` — `lang.md` | Vollständiger Hauptweg und bis zu zwei sinnvolle Alternativen mit Angabe, wann sie besser sind. | Sichtbar; keine nutzlosen Alternativen erfinden. | Lösungswege vergleichen. |
| `klausur` — `klausur.md` | Kompakte Lösung, typische Fehler, schnelle Kontrolle, Zeitangabe und allgemeine Hinweise zur Darstellung. | Sichtbar. | Zeit und Klausurdarstellung üben; keine behaupteten lokalen Bewertungskriterien. |
| `hilfe` — `hilfe.md` | Karte mit elf Befehlen sowie Sprache, Dauermodus, Lösungsabruf und Feedback. | Keine Aufgabe lösen. | Befehl wählen oder Aktivierung prüfen. |

## Steuerbefehle sind keine zusätzlichen Modi

| Signal | Wirkung |
|---|---|
| `lösung` | Zurückgehaltene Lösung oder Antwort abrufen; Dauermodus unverändert. Bei mehreren offenen Aufgaben nach der Nummer fragen. |
| `!an tipp` | Modus für folgende Aufgaben speichern. Ein Einzelbefehl überschreibt ihn nur für eine Nachricht. `hilfe` ist kein Dauermodus. |
| `!aus` | Dauermodus beenden, Sprache beibehalten. |
| `[ar]` oder `!sprache ar` | Arabisch erklären; Überschriften, Aufgabentext und Klausur-Lösung bleiben Deutsch. `[de]` wechselt zurück. |
| `!issue` | Festen Feedback-Link mit Datenschutzhinweis ausgeben; kein Gespräch übertragen. |

## Selbst erstelltes Bedienbeispiel

```text
tipp: An einem ohmschen Widerstand von 2,0 kOhm liegen 12 V. Berechne den Strom.
```

Erwartet werden Fragen ohne Ergebnis. Erst in einer späteren Nachricht `lösung` schicken. Ein zweites `tipp` liefert engere Fragen; beim dritten wird auf `voll` verwiesen. Weitere Fälle: [[12 Abnahmeplan]].

> [!note] Lösung auf Wunsch
> Auch `kurz`, `mittel`, `lang` und `klausur` sind ausdrückliche Wünsche nach einer Lösung. Der Abruf ist nicht auf das Wort `lösung` beschränkt. Ein 🔒-Symbol schützt keinen darunter geschriebenen Text.
