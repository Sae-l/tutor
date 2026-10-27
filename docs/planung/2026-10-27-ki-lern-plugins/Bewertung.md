# Bewertung: „KI-Lern-Plugins auf GitHub im Vergleich“

Stand: 2026-10-27 · Planungsnotiz, keine Produktfreigabe. Untersuchte Codebasis: `main` bei `ae16a03`. Originalbericht unverändert in [`Bericht-Original.txt`](Bericht-Original.txt) (KI-erzeugt, mit Exportresten wie `[span_…]` und defekten LaTeX-Pfeilen).

## Kurzurteil

Der Bericht ist als **Landkarte brauchbar, als Rangliste nicht**. Die Beschreibungen der fünf für Tutor wichtigsten Repositories stimmen in der Stichprobe weitgehend. Die Platzierung hat kein genanntes Kriterium; Tutor steht ohne Begründung auf Platz 1. Für Tutor folgt daraus wenig Neues: Die meisten übertragbaren Prinzipien sind bereits umgesetzt. Echte Lücken sind (1) der Umgang mit „weiß nicht“ in `tipp`, (2) Wiederholung über die Sitzung hinaus. Der größte Hebel bleibt unverändert die offene native Abnahme (`CLAUDE.md`, Offene Punkte 1).

## Stichprobe gegen die Quelle (2026-10-27, öffentliche GitHub-Seiten)

| Repository | Bericht | Geprüft | Abweichung |
|---|---|---|---|
| kirilxd/claude-tutor | 142 ★, SM-2, Dashboard, PreToolUse-Hooks | 138 ★, MIT, SM-2 (1 d → 6 d → 15 d), Dashboard auf localhost, PreToolUse- und SessionStart-Hooks, Daten in `~/.claude/learning/` | Sternzahl leicht abweichend |
| Bhala-Srinivash/agent-tutor-skill | 11 ★, 5-Stufen-Schleife, FSRS, `~/.learn/` | 8 ★, MIT; Schleife, FSRS, Zero-Hint-Quiz und Badges bestätigt | Sternzahl |
| WSE-research/guided-learning-skill | HTWK Leipzig, 3 Durchläufe, 3 d → 7 d → 21 d, 6 Tags, 18 Formate | 6 ★, MIT; alles bestätigt, dazu: „unscharf“ hält das Intervall, „leer“ setzt auf 3 d zurück | keine |
| mordor-forge/study-skill | 46 ★, FSRS-6, ADHS-Sitzungen, v2 „Lamplight“ ohne NotebookLM | 46 ★, MIT; FSRS-6 und ADHS-Funktionen bestätigt; **v2 noch auf einem Branch, `main` ist v1** | v2 als fertig dargestellt |
| deniz-miro/claude-learn-skill | Think-Articulate-Reflect, Frustrationserkennung, Teach Mode, Journal | 13 ★, MIT; alles bestätigt | keine |

Nicht geprüft: die übrigen 25 Einträge, insbesondere große Zahlen wie „über 23.000 Skills“ (CoPaper.AI) und alle Moodle-/ILIAS-Angaben.

## Schwächen des Berichts

- **Rangfolge ohne Maßstab.** Weder Sterne, Aktivität noch Qualität erklären die Reihenfolge; Tutor (ohne Nutzungsdaten) vor kirilxd/claude-tutor (138 ★).
- **Tutor falsch beschrieben.** „Sitzungsbasierte Aufgabenführung“ und Copilot als Plattform; Copilot ist eingefroren. Es fehlen die tatsächlichen Merkmale: Lösungsschutz, 11 Modi, 6 Erklärsprachen, ChatGPT-Plugin und Gemini-Skill.
- **Platz 8 leer.** Der Bericht stellt selbst fest, dass `Dooc-Nuken/teaching-skills` so nicht existiert, und füllt den Platz mit anderen Repositories.
- **Entwicklungsstände überzeichnet** (mordor-forge v2) und Sternzahlen ohne Abrufdatum.
- **Rhetorik statt Beleg.** „Humboldtsches Bildungsideal“, „deutscher Sonderweg“, „eines der weltweit ausgereiftesten Modelle“ sind Wertungen ohne Messung.
- **Lernforschung nur indirekt.** Fluency Illusion, Retrieval Practice und Desirable Difficulty werden über Repository-READMEs und einen Blogbeitrag zitiert, nicht über Primärliteratur. Die Primärquellen dazu sind in [`Obsidian-tutor/04 Wissenschaftliche Grundlagen.md`](../../../Obsidian-tutor/04%20Wissenschaftliche%20Grundlagen.md) bereits geprüft.

## Abgleich: Was Tutor davon schon hat

| Idee aus dem Bericht | Quelle | In Tutor |
|---|---|---|
| Kein „verstanden“ ohne eigene Leistung | agent-tutor-skill | 🧩 Verständnisfrage, Antwort erst nach eigenem Abrufversuch |
| Transfer auf neue Situation | agent-tutor-skill, WSE | 🔄 „Was wäre, wenn?“ in `voll` |
| Fehler kategorisieren | WSE (Struggle Tags) | `check`: Fehlerart konzeptionell / Rechenfehler / Einheiten / Vorzeichen |
| Bei Nichtverstehen Zugang wechseln | claude-learn-skill | `didaktik.md`: „Anders erklären statt lauter wiederholen“ |
| Keine Lösung vorwegnehmen | alle sokratischen Skills | Lösungsschutz, `tipp` nur Fragen |
| Spätere Wiederholung | alle SRS-Skills | 🗂 Wiederholungskarte, fest „nach zwei Tagen“ |

Alleinstellung von Tutor in dieser Stichprobe: kein anderes Projekt verbindet deutschsprachige MINT-Erstsemesteraufgaben, harten Lösungsschutz, Arabisch/Türkisch/Urdu als Erklärsprache und denselben Skill auf Claude, ChatGPT und Gemini. Das ist eine Beobachtung über 30 Einträge, keine Marktanalyse.

## Ableitungen für Tutor

Randbedingung: Tutor läuft zustandslos in Chatoberflächen ohne Dateisystem und muss auf drei Plattformen gleich wirken. Alles, was Dateien, Server, Hooks oder Dashboards braucht (FSRS-Speicher, MCP, Obsidian-Vault, Web-Dashboard), passt nicht in den Kern.

### Jetzt sinnvoll (nur Prompt, kein neuer Modus)

1. **„weiß nicht“ in `tipp` und nach der Verständnisfrage.** Heute regelt `tipp` richtig/falsch und wiederholtes „tipp“, nicht aber „keine Ahnung“, „?“ oder sehr kurze Antworten. Vorschlag nach claude-learn-skill: einen Satz Entlastung („Diese Stelle ist für viele schwer“), dann Zugang wechseln (konkretes Zahlenbeispiel, Skizze, Teilfrage kleiner) statt dieselbe Frage umzuformulieren; beim zweiten Mal auf `voll` verweisen. Passt zum ADHS-Ziel. Ort: `tutor/modes/tipp.md`, Abschnitt „Wenn der Lernende antwortet“. Neuer Akzeptanzfall nötig.
   *Fertig, wenn:* Regel ergänzt, Build und Tests grün, Fall in `tests/akzeptanz.md`.

### Später empfohlen (Entscheidung als Issue)

2. **Wiederholung über Sitzungen ohne Speicher.** Die feste Zwei-Tage-Karte ist laut eigener Literaturprüfung nicht belegt. Alternative nach WSE: Karte mit Stufen 3 d → 7 d → 21 d; „unscharf“ hält, „leer“ setzt zurück. Der Lernende trägt den Stand selbst als kurzen kopierbaren **Lernstand-Block** in die nächste Sitzung. Plattformunabhängig, datensparsam, aber mehr Text pro Antwort; Abwägung gegen „keine längeren Antworten“ nötig.
3. **Optionaler Anki-Export** der Wiederholungskarten als zweispaltiger Text (Frage; Antwort). Kein MCP nötig, Import in Anki funktioniert per Textdatei.

### Optional / geparkt

- Interaktive HTML-Simulationen mit Schiebereglern (WSE) für `skizze`: nur auf Claude mit Artifacts möglich, widerspricht gleichem Verhalten auf drei Plattformen.
- Altklausur-Analyse und Grenznutzen-Lernplan (study-planner, claude-exam-prep-skill): eher Kurspaket in `kurse/` als Skill, wegen der Regel „kein Kursbezug im Skill“.
- ILIAS als Verbreitungsweg (surlabs/AIChatForILIAS): institutionell, nur mit Hochschule umsetzbar.
- Persistenz, FSRS, Dashboard, Hooks: nur für eine spätere Claude-Code-Variante denkbar.

## Stoppregel

Keine weiteren Einträge des Berichts prüfen, bevor Punkt 1 umgesetzt und die native Abnahme (Offene Punkte 1) begonnen ist; die übrigen Repositories ändern keine der obigen Ableitungen.
