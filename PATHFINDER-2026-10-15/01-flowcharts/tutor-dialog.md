# Tutor-Dialog: Istfluss

Quelle: `tutor/SKILL.md:1–58`, alle elf `tutor/modes/*.md`, `references/sprache.md:1–26`, `didaktik.md:1–41`, `antwortvorlage.md:1–51`, `latex-regeln.md:1–37` und `kurse/mpg1.md:1–40`, jeweils unter der Skillquelle `tutor/`. Statische Discovery, HEAD 75a2cf1.

Das Diagramm beschreibt Modellanweisungen, keinen ausgeführten Parser. Sonderbefehle sind eigene Zweige; ihre Priorität gegenüber gleichzeitig vorkommenden anderen Befehlen ist teilweise unklar.

```mermaid
flowchart TD
    A["Aktivierung für MINT-Aufgabe<br/>tutor/SKILL.md:3"] --> B["Sprache und Eingabe bestimmen<br/>tutor/SKILL.md:15"]
    B --> C{"Entscheidende Angabe unklar?<br/>tutor/SKILL.md:12"}
    C -->|ja| Q["Eine gezielte Rückfrage<br/>tutor/SKILL.md:12"]
    C -->|nein| D{"Sonderbefehl oder normale Moduswahl<br/>tutor/SKILL.md:41"}
    D -->|issue| I["Festen Feedbacklink ausgeben<br/>tutor/SKILL.md:44"]
    D -->|lösung| L["Offene Antwort abrufen, bei Mehrdeutigkeit fragen<br/>tutor/SKILL.md:54"]
    D -->|normal| E["Hilfe, Einzelbefehl, Dauermodus, Automatik<br/>tutor/SKILL.md:42"]
    E --> F["Einen der elf Modi lesen<br/>tutor/SKILL.md:29"]
    F --> G["Antwortvorlage, Sprache und Lehrregeln anwenden<br/>tutor/SKILL.md:21"]
    K["Optionaler Kurskontext<br/>kurse/mpg1.md:5"] --> G
    G --> H{"Skizzenwerkzeug verfügbar?<br/>tutor/modes/skizze.md:8"}
    H -->|ja, bei Skizze| J["Beschriftete Grafik erstellen<br/>tutor/modes/skizze.md:8"]
    H -->|nein, bei Skizze| N["Beschreibung, Tabelle und Code<br/>tutor/modes/skizze.md:9"]
    H -->|anderer Modus| P["Richtigkeit und Darstellung prüfen<br/>tutor/SKILL.md:18"]
    J --> P
    N --> P
    L --> P
    P --> R["Lösungsschutz vor Senden prüfen<br/>tutor/SKILL.md:52"]
    R --> O["Antwort und nächste Aktion<br/>tutor/SKILL.md:57"]
```

## Zustand, Fallback und Effekte

Sprache und Dauermodus werden im Gespräch geführt (`SKILL.md:41–47`, `references/sprache.md:14–16`); kein eigener Speicher. Tipp-Wiederholungen stehen in `modes/tipp.md:32–40`. Check ohne Versuch fordert diesen an (`modes/check.md:14`). Keine direkte Netzwerk-/Dateioperation durch Markdown; das Modell kann bereitgestellte Rechen- und Zeichenwerkzeuge nutzen. `!issue` sendet keine Nachricht.

## Relevante Widersprüche

- Nummernreihenfolge global gegenüber expliziten Moduslisten: `references/antwortvorlage.md:3` versus `modes/kurz.md:6`, `modes/lang.md:6`, `modes/voll.md:8–16`.
- Sperrabschnitt am Ende gegenüber Erklär-Fußteil: `references/antwortvorlage.md:35` versus `modes/erklaer.md:14–15`.
- Verständnisfrage direkt vor nächstem Schritt gegenüber Thema-Reihenfolge: `references/didaktik.md:30`, `references/antwortvorlage.md:34` versus `modes/thema.md:6`.
- `[ar] tipp` ist ein erwarteter Fall (`tests/akzeptanz.md:70`), aber Sprachpräfix vor dem Anfangsbefehl bleibt im Router unpräzise (`tutor/SKILL.md:15,25`). Das ist eine Auslegungsgefahr, kein beobachteter Modellfehler.

Abhängigkeiten: Build liest Modustabelle und Kernmarkierungen; Plattformen stellen Werkzeuge/Renderer; Akzeptanzfälle müssen Verhalten beobachten. Hohe Sicherheit über Quellen, keine Sicherheit über tatsächliche Modellausführung.
