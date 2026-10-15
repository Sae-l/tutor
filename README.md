# tutor – MINT-Lern-Tutor als Claude-Skill und System-Prompt

Lern-Tutor für Aufgaben aus dem ersten Studienjahr in MINT-Fächern (Physik, Mathematik, E-Technik) an deutschsprachigen Hochschulen. Erst verstehen, dann selbst lösen: Erklärung ohne fertige Lösung, Leitfragen, Fehlerdiagnose des eigenen Versuchs, Klausur-Lösung auf Deutsch, Lösungen erst auf Abruf. Erklärungen auf Deutsch oder auf Wunsch in Arabisch, Türkisch, Französisch, Englisch oder Urdu. ADHS-freundlich gestaltet (kurze Schritte, feste Struktur; Designziel, keine nachgewiesene Wirkung). Kein Programm, kein Dienst: Der Tutor läuft als Anweisung in Claude oder ChatGPT.

> **In English:** A study tutor for first-year STEM exercises (physics, maths, electrical engineering) at German-speaking universities, packaged as a Claude Skill plus a generated system prompt for other chatbots. It explains and asks guiding questions before revealing solutions. Answers are in German by default; Arabic, Turkish, French, English or Urdu on request. The docs are in German because the target audience studies in German.

## Status

- **Vorabstand v0.2, nicht abgenommen.** Build und Strukturtests laufen; die Abnahme des Lehrverhaltens mit einem Modell ([tests/akzeptanz.md](tests/akzeptanz.md)) ist vorbereitet, aber noch nicht ausgeführt.
- **Rechte:** [MIT-Lizenz](LICENSE).
- **Feedback:** [Issue anlegen](https://github.com/Sae-l/tutor/issues/new) oder im Tutor `!issue` schreiben. Issues sind öffentlich: keine Aufgabentexte, Namen oder Fotos mit persönlichen Daten einfügen.

## Welche Variante?

| Plattform | Dateien | Stand |
|---|---|---|
| **Claude Skill** (empfohlen) | Ordner `tutor/` als ZIP | primär; Release-Gate mit allen Akzeptanzfällen |
| ChatGPT Projekt | Anweisung `dist/kern.md`, Datei `dist/system-prompt.md` | experimentell; Teilabnahme vorgesehen |
| Gemini (Gem bzw. Gemini-Skill) | wie ChatGPT Projekt | experimentell, nicht geprüft |

Custom GPTs werden von OpenAI für neue private Konten eingestellt und sind nicht mehr vorgesehen; Gemini-Gems werden zu „Gemini skills“ ([Recherche](https://github.com/Sae-l/tutor/issues/11)).

## Schnellstart (Claude Skill)

Voraussetzung: ein Claude-Konto. Laut [Claude-Hilfe](https://support.claude.com/en/articles/12512180-use-skills-in-claude) gibt es Skills in allen Tarifen (Free, Pro, Max, Team, Enterprise); sie brauchen eingeschaltete Code-Ausführung. Menünamen hier wie in der englischen Oberfläche; in der deutschen können sie anders heißen.

1. [`tutor-skill.zip`](https://github.com/Sae-l/tutor/releases/download/v0.2.0-rc.1/tutor-skill.zip) aus dem [aktuellen Release](https://github.com/Sae-l/tutor/releases) herunterladen. Nicht entpacken.
2. Auf [claude.ai](https://claude.ai) unter *Settings → Capabilities* „Code execution and file creation“ einschalten. Team und Enterprise: Das schaltet die Administration unter *Organization settings → Plugins & skills* frei.
3. Unter *Customize → Skills* auf „+“ → „Create skill“ → „Upload a skill“ klicken und `tutor-skill.zip` hochladen. Der Skill „tutor“ muss eingeschaltet sein.
4. **Testen:** In einem neuen Chat nur `tutor` schreiben. Erscheint die Befehlskarte, ist der Tutor aktiv.
5. Lernen: Foto der Aufgabe schicken, optional mit einem Befehlswort. Für ein Kurspaket ein Projekt „Tutor“ anlegen (siehe unten).

Beispiel: Foto einer Aufgabe + `tipp` → vier bis sechs Leitfragen, keine Lösung. Danach eigener Rechenweg als Nachricht → Fehlerdiagnose (Check). Zum Vergleichen: `kurz`.

**Aktualisieren:** Neue `tutor-skill.zip` herunterladen, unter *Customize → Skills* den Skill „tutor“ öffnen, ausschalten, über „…“ → „Delete“ löschen und die neue Datei hochladen. Änderungen stehen im [CHANGELOG](CHANGELOG.md).

**Selbst bauen** (statt Download, z. B. für einen ungeprüften Stand von `main`):

```bash
git clone https://github.com/Sae-l/tutor.git
cd tutor
git archive --format=zip --prefix=tutor/ -o tutor-skill.zip HEAD:tutor
```

### Fehlerbehebung

| Problem | Lösung |
|---|---|
| Hochladen schlägt fehl | ZIP unverändert hochladen. Neu gepackte Archive haben oft nicht den Ordner `tutor/` an oberster Stelle; dann erkennt Claude den Skill nicht. |
| `tutor` zeigt keine Befehlskarte | Code-Ausführung und Skill „tutor“ eingeschaltet? Neuen Chat öffnen. Sonst Skill löschen und neu hochladen. |
| Formeln erscheinen als `$$…$$` | Die Plattform rendert kein LaTeX. In Claude im Browser normalerweise kein Problem; ChatGPT und Gemini sind nicht geprüft. |
| Antwort verrät die Lösung zu früh | Fehler im Lösungsschutz: bitte als [Issue](https://github.com/Sae-l/tutor/issues/new) melden, ohne Aufgabentext oder persönliche Daten. |
| Handy-App | Den Skill einmal im Browser hochladen. Ob er in der Claude-App genauso greift, ist nicht geprüft. |

## Bedienung

**Sprache:** standardmäßig Deutsch, auch wenn du in einer anderen Sprache schreibst. Umschalten mit `[ar]` Arabisch, `[tr]` Türkisch, `[fr]` Französisch, `[en]` Englisch, `[ur]` Urdu, `[de]` zurück, oder `!sprache ar` usw. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch, damit das Prüfungsvokabular mitgelernt wird.

**Befehle:** ein Befehlswort am Nachrichtenanfang (z. B. Foto + „tipp“) oder mit `!` irgendwo in der eigenen Anweisung. `hilfe` zeigt die Befehlskarte. Empfohlene Reihenfolge: **erklär → tipp → voll → kurz**.

| Befehl | Wirkung |
|---|---|
| (keiner) / `erklär` | Thema und nötige Gleichungen, **ohne** Beispiel und **ohne** Lösung |
| `voll` | anschaulich und mathematisch, mit vorgerechnetem Beispiel einer anderen Aufgabe |
| `thema` | Begriff oder Gesetz verstehen und wie es beim Lösen hilft |
| `tipp` | Leitfragen, die man sich selbst stellt; Lösung zurückgehalten |
| `check` | Fehlerdiagnose des eigenen Versuchs (automatisch, wenn ein Versuch mitkommt) |
| `skizze` | Skizze, Diagramm oder Graph (mit Zeichenwerkzeug als Bild, sonst Beschreibung + TikZ/matplotlib) |
| `kurz` | Klausur-Lösung auf Deutsch plus eine Anmerkung |
| `mittel` | Erklärung mittlerer Tiefe mit vollständiger Lösung |
| `lang` | vollständige Lösung plus bis zu zwei andere Lösungswege |
| `klausur` | schnelle Lösung mit Tipps für volle Punktzahl |
| `hilfe` | Befehlskarte |
| `!issue` | Link für Feedback |

**Dauermodus:** `!an tipp` (oder ein anderer Befehl) gilt für alle folgenden Aufgaben, bis `!aus` kommt.

**Lösungsschutz:** Die Lösung nach `tipp` und Antworten auf Verständnisfragen kommen erst mit `lösung`. Das Symbol 🔒 allein versteckt keinen Text.

**Kurspaket (optional):** Eine Markdown-Datei mit Notation und Stoffumfang eines bestimmten Kurses, z. B. [kurse/mpg1.md](kurse/mpg1.md). In Claude ein Projekt anlegen, die Datei dort als Projektwissen hochladen und in diesem Projekt lernen. Sie gehört nicht zum Skill; bei Bezeichnungen und Stoffumfang hat sie Vorrang.

## Einrichtung auf anderen Plattformen (experimentell)

`kern.md` und `system-prompt.md` aus dem [aktuellen Release](https://github.com/Sae-l/tutor/releases) herunterladen (identisch mit `dist/`).

- **ChatGPT Projekt:** neues Projekt anlegen, in den Projekteinstellungen den Inhalt von `kern.md` in die Anweisungen kopieren und `system-prompt.md` als Projektdatei hinzufügen.
- **Gemini:** neuen Gem anlegen, `kern.md` in die Anweisungen kopieren und `system-prompt.md` als Wissen hochladen.

`kern.md` hat höchstens 4000 Zeichen (vom Build geprüft). Menünamen können abweichen; Feldgrenzen, Formeldarstellung und Aufklappblöcke sind dort nicht offiziell dokumentiert und nicht geprüft.

## Datenschutz

Der Tutor speichert nichts selbst; Gespräche liegen beim jeweiligen Anbieter (Anthropic, OpenAI, Google) nach dessen Bedingungen. `!issue` erzeugt nur einen Link mit festem Titel und schickt keine Gesprächsinhalte. Was du in ein GitHub-Issue schreibst, ist öffentlich.

## Aufbau

| Pfad | Zweck |
|---|---|
| `tutor/` | Quelle: Claude-Skill (`SKILL.md` als Router + `modes/` + `references/`) |
| `kurse/` | optionale Kurspakete, nicht Teil des Skills |
| `dist/system-prompt.md` | Erzeugt: alles in einer Datei, für andere Plattformen |
| `dist/kern.md` | Erzeugt: Kern aus den `<!-- kern -->`-Abschnitten von `SKILL.md`, höchstens 4000 Zeichen |
| `build.py` | Erzeugt `dist/` aus der Quelle |
| `tests/` | Strukturtests, Akzeptanzfälle, Protokolle der Abnahme |
| `docs/KONZEPT.md` | Hintergrund: Ziel, Lernprinzipien, Architekturentscheidungen |
| `docs/index.html` | Landingpage für GitHub Pages (eine Datei, ohne Build); Schriften lokal in `docs/fonts/` (SIL OFL) |
| `GLOSSARY.md` | Festgelegte Begriffe |

## Entwicklung

Voraussetzung: Git und Python 3.14 (nur Standardbibliothek).

```bash
python build.py
```

```bash
python -B -m unittest discover -s tests -v
```

Änderungen nur in `tutor/` machen, danach `python build.py` ausführen und beides committen. Die Tests prüfen den reproduzierbaren Build, dass Befehlstabelle und Moduldateien übereinstimmen (11 Modi), Kurs-Neutralität des Skills, Länge und Inhalt des Kerns, Formel-Beispiele und den Erhalt der bisherigen Ausgabe bei fehlerhaften Quellen (auch unter `python -O`). Die CI führt dasselbe auf Linux und Windows aus.

[tests/akzeptanz.md](tests/akzeptanz.md) enthält das Release-Gate, 30 Modusfälle und 32 Zustands- und Grenzfälle, je mit stabiler ID. Bestandene Strukturtests belegen kein korrektes Tutorverhalten.

Ablauf, Release-Checkliste und Paketbau: [CONTRIBUTING.md](CONTRIBUTING.md). Sicherheit: [SECURITY.md](SECURITY.md). Änderungen: [CHANGELOG.md](CHANGELOG.md).

## Grenzen

- Formeln werden nur dann sauber dargestellt, wenn die Plattform `$$ ... $$` rendert; nur informell beobachtet, nicht protokolliert.
- Hochgeladene Dateien liest das Modell nicht immer vollständig; deshalb stehen die wichtigsten Regeln im Kern.
- Der Tutor kennt keine Bewertungskriterien einzelner Hochschulen. Ergebnisse mit offiziellen Musterlösungen abgleichen.
- Die Lernprinzipien in [docs/KONZEPT.md](docs/KONZEPT.md) begründen das Design, belegen aber keine Wirksamkeit dieses Tutors, auch nicht für ADHS.
