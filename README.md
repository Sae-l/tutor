# tutor – Physik- und Mathe-Tutor als Claude-Skill und System-Prompt

Prompt- und Skill-Sammlung für einen Lern-Tutor in Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln). Ausgelegt für Anfänger mit ADHS (Designziel, keine nachgewiesene Wirkung): erst anschaulich, dann schrittweise Rechnung, Klausur-Lösung auf Deutsch, Lösungen von Übungen erst auf Abruf. Kein Programm, kein Dienst: Der Tutor läuft als Anweisung in Claude oder ChatGPT.

## Status und Nutzung

- **Status: Vorabstand, nicht abgenommen.** Build und Strukturtests laufen; die Abnahme des Lehrverhaltens mit einem Modell ([tests/akzeptanz.md](tests/akzeptanz.md)) ist vorbereitet, aber noch nicht ausgeführt. Releases sind bis dahin Vorabversionen (`v0.x.0-rc.N`).
- **Nutzung:** persönliches Projekt eines einzelnen Lernenden; Weitergabe an andere wird nicht unterstützt ([Issue #2](https://github.com/Sae-l/tutor/issues/2)).
- **Rechte:** [MIT-Lizenz](LICENSE). Kursunterlagen des Dozenten gehören nicht zum Projekt und werden nicht versioniert (`referenzen/` ist ausgeschlossen).

## Welche Variante?

Freigabematrix nach [Issue #4](https://github.com/Sae-l/tutor/issues/4):

| Plattform | Datei | Stand |
|---|---|---|
| **Claude Skill** (empfohlen) | Ordner `tutor/` als ZIP | primär; Abnahme mit allen Akzeptanzfällen vorgesehen |
| ChatGPT Projekt | `dist/system-prompt.md` | sekundär; Teilabnahme vorgesehen |
| Claude Projekt, Gemini Gem, Copilot | `dist/system-prompt.md` | experimentell, nicht geprüft |
| ChatGPT Custom GPT | `dist/system-prompt-kurz.md` | experimentell, nicht geprüft |

## Schnellstart (Claude Skill)

1. Skill-Paket aus dem Repository bauen (nur versionierte Dateien, keine lokalen Werkzeugdaten):

   ```bash
   git archive --format=zip --prefix=tutor/ -o tutor-skill.zip HEAD:tutor
   ```

2. In Claude unter *Einstellungen → Skills* `tutor-skill.zip` hochladen.
3. Projekt „Tutor“ anlegen und dort lernen: Foto der Aufgabe schicken, optional mit einem Befehlswort.

Beispiel: Foto einer Aufgabe + `tipp` → vier bis sechs Leitfragen, keine Lösung. Danach eigener Rechenweg als Nachricht → Fehlerdiagnose (Check). Fertig gelöst: `lösung`.

Den Ordner `tutor/` nicht direkt aus dem Arbeitsordner zippen: Dort können lokale Werkzeugzustände liegen (z. B. `.claude-flow/`), die nicht hochgeladen werden sollen.

## Bedienung

**Sprache:** standardmäßig Deutsch. Umschalten mit einem Signal in der Nachricht: `[ar]` Arabisch, `[tr]` Türkisch, `[uk]` Ukrainisch, `[fr]` Französisch, `[de]` zurück zu Deutsch. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch.

**Befehle:** ein Befehlswort oder eine aufgeführte Wortgruppe am Nachrichtenanfang (z. B. Foto + „tipp“), oder mit `!` in der eigenen Anweisung; kombinierbar mit dem Sprachcode, z. B. `tipp [ar]` oder `[ar] tipp`. `hilfe` oder `help` (allein oder als `!hilfe`) zeigt die Befehlskarte mit einer Erklärung je Befehl. Empfohlene Reihenfolge beim Lernen: **erklär → tipp → ausführlich → lösung**. Lösungen von Übungen, Tipp-Aufgabe und Verständnisfrage stehen nie sichtbar in derselben Antwort, sondern kommen erst mit `lösung`.

| Befehl | Wirkung |
|---|---|
| (keiner) / `erklär` | Thema und nötige Gleichungen erklärt, **ohne** Beispiel und **ohne** Lösung der Aufgabe |
| `standard` | Erklärung mittlerer Tiefe mit Lösung + zwei Übungen |
| `!ausführlich` (oder `!detail`) | anschaulich und mathematisch erklärt, mit vorgerechnetem Beispiel einer ähnlichen Aufgabe |
| `!kurz` | kurze Erklärung, dann vereinfachte Lösung |
| `!lösung` | direkt die Klausur-Lösung |
| `!tipp` | Leitfragen, die man sich selbst stellt, um zur Lösung zu kommen; Lösung zurückgehalten |
| `!check` | Fehlerdiagnose des eigenen Versuchs (automatisch, wenn ein Versuch mitkommt) |
| `!übung` | drei neue Aufgaben desselben Typs |
| `!konzept` | Begriff oder Satz verstehen, ohne Rechenaufgabe |
| `!hilfe` | diese Befehlsliste |

Die Befehle verstehen auch natürliche Wörter in allen fünf Sprachen (z. B. „kurz“, „سريع“, „hızlı“).

**Dauermodus:** `!an tipp` (oder ein anderer Befehl) gilt für alle folgenden Aufgaben, bis `!aus` kommt. Ein Einzelbefehl überschreibt ihn nur für diese eine Nachricht. Jede Antwort zeigt dann oben den aktiven Modus und die Sprache.

**Lösungsschutz:** Ohne geprüfte Aufklappfunktion bleiben Übungs- und Tipp-Lösungen bis zum ausdrücklichen Abruf zurückgehalten. `lösung Übung 2` zeigt gezielt die zweite Lösung. Das Symbol 🔒 allein versteckt keinen Text. Im Erklär- und im Ausführlich-Modus bleiben auch bei mehreren Aufgaben die Originalergebnisse zurückgehalten.

## Einrichtung auf anderen Plattformen

**ChatGPT (Projekt)** – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**Claude Projekt** (experimentell) – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**ChatGPT (Custom GPT)** (experimentell) – Das Anweisungsfeld fasst höchstens 8000 Zeichen. Zwei Wege, beide nicht geprüft:
- Inhalt von `dist/system-prompt-kurz.md` als Anweisung eintragen (passt ins Feld, enthält aber weniger Einzelregeln), oder
- `dist/system-prompt.md` unter *Wissen* hochladen und als Anweisung eintragen:

  > Du bist ein Physik- und Mathe-Tutor. Lies vor jeder Antwort die Datei system-prompt.md im Wissen und befolge sie vollständig, besonders Sprache, Antwortvorlage und LaTeX-Regeln. Standardsprache ist Deutsch.

**Gemini (Gem), Microsoft Copilot, GitHub Copilot** (experimentell) – Inhalt von `dist/system-prompt.md` in die Anweisungen eintragen; ist das Feld zu kurz, `dist/system-prompt-kurz.md` verwenden. Feldgrenzen, Formeldarstellung und Aufklappblöcke dieser Plattformen sind nicht geprüft.

## Aufbau

| Pfad | Zweck |
|---|---|
| `tutor/` | Quelle: Claude-Skill (`SKILL.md` + `modes/` + `references/`) |
| `tutor/references/kurs-mpg1.md` | Kursnotation MPG1, Stoffumfang, Regeln zu Endantworten der Übungsblätter (eigene Zusammenfassung) |
| `tutor/references/kurzfassung.md` | Quelle: handgeschriebene Kurzfassung (höchstens 8000 Zeichen, Build bricht sonst ab) |
| `dist/system-prompt.md` | Erzeugt: eine einzige, selbstständige Prompt-Datei für alle anderen Plattformen |
| `dist/system-prompt-kurz.md` | Erzeugt: Kurzfassung für Felder mit Zeichenlimit |
| `build.py` | Erzeugt `dist/` aus der Quelle |
| `tests/` | Strukturtests, Akzeptanzfälle, Protokolle der Abnahme |
| `docs/KONZEPT.md` | Hintergrund: Ziel, Lernprinzipien, Architekturentscheidungen |
| `GLOSSARY.md` | Festgelegte Begriffe |

Die Kurzfassung ist eine eigene Textquelle und wird **nicht** automatisch aus den Moduldateien abgeleitet. Ändert sich Verhalten in `tutor/`, die Kurzfassung von Hand angleichen; die Tests prüfen nur Länge, Befehle, Sprachcodes und Kernregeln.

## Entwicklung

Voraussetzung: Git und Python 3.14 (damit geprüft; nur Standardbibliothek).

```bash
python build.py
```

```bash
python -B -m unittest discover -s tests -v
```

Änderungen nur in `tutor/` machen, danach `python build.py` ausführen und beides committen. Die Tests prüfen den reproduzierbaren Build, die zehn Modusdateien, offene Dateiverweise (auch unter `python -O`), Formel-Beispiele und den Erhalt der bisherigen Ausgabe bei fehlerhaften Quellen. Die CI ([.github/workflows/ci.yml](.github/workflows/ci.yml)) führt dasselbe auf Linux und Windows aus.

[tests/akzeptanz.md](tests/akzeptanz.md) enthält das Release-Gate, 27 Modusfälle, 27 Zustands- und Grenzfälle und 6 Kursaufgaben aus MPG1, je mit stabiler ID; Protokolle nach [tests/protokolle/VORLAGE.md](tests/protokolle/VORLAGE.md). Bestandene Strukturtests belegen kein korrektes Tutorverhalten.

Ablauf, Release-Checkliste und Paketbau: [CONTRIBUTING.md](CONTRIBUTING.md). Sicherheit und Meldeweg: [SECURITY.md](SECURITY.md). Änderungen: [CHANGELOG.md](CHANGELOG.md).

## Grenzen

- Formeln werden nur dann sauber dargestellt, wenn die Plattform `$$ ... $$` rendert. In Claude und ChatGPT bisher nur informell beobachtet, nicht protokolliert; Gemini und Copilot sind nicht geprüft.
- Bei hochgeladenen Wissensdateien (Custom GPT, Copilot) liest das Modell die Datei nicht immer vollständig. Direkt eingefügte Anweisungen sind zuverlässiger.
- Der Tutor kennt keine internen Bewertungskriterien der TH Köln. Ergebnisse mit offiziellen Musterlösungen abgleichen.
- Die Lernprinzipien in [docs/KONZEPT.md](docs/KONZEPT.md) sind aus dem Gedächtnis zitiert und nicht nachrecherchiert. Sie begründen das Design, belegen aber keine Wirksamkeit dieses Tutors, auch nicht für ADHS.
