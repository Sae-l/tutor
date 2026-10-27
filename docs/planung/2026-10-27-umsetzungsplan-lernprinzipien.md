# Erklärbogen und Lernprinzipien – Umsetzungsplan

> **Für ausführende Agenten:** Erforderlicher Unter-Skill: `superpowers:subagent-driven-development` (empfohlen) oder `superpowers:executing-plans`, Aufgabe für Aufgabe. Schritte nutzen Checkboxen (`- [ ]`).

**Ziel:** Die Ergebnisse vom 27.10.2026 so in den Skill übernehmen, dass Tutor einen eigenen, prüfbaren Erklärstil bekommt und keine bestehende Regel bricht.

**Architektur:** Nur Moduldateien und Referenzen unter `tutor/` ändern, nie die `<!-- kern -->`-Abschnitte von `tutor/SKILL.md`. Jede Aufgabe endet mit `python build.py`, aktualisierten Vault-Hashes, grünen Tests und eigenem Commit, damit jede Aufgabe einzeln zurückgenommen werden kann.

**Technik:** Markdown-Skillquellen, `build.py`, `unittest`, `Obsidian-tutor/verify_vault.py`.

**Grundlagen:** [`2026-10-27-evidenz-update.md`](2026-10-27-evidenz-update.md), [`2026-10-27-ki-lern-plugins/Bewertung.md`](2026-10-27-ki-lern-plugins/Bewertung.md), [`2026-10-16-wayfinder/Recherche-Lernforschung.md`](2026-10-16-wayfinder/Recherche-Lernforschung.md).

**Status:** Aufgaben 1–5 am 27.10.2026 implementiert (je ein Commit); native Abnahme U07–U12 (Aufgabe 5, Schritt 4) offen. Voraussetzung: PR #73 gemergt.

## Entscheidungen, die dieser Plan festschreibt

| Entscheidung | Begründung |
|---|---|
| Erklärstil als **Mechanismus** („Erklärbogen“), nicht als Nachahmung bestimmter Personen (Feynman, Al-Dahih u. a.) | Personenstil überträgt sich nicht verlässlich auf sechs Sprachen und ist nicht prüfbar; der Mechanismus schon. |
| Einstieg und Bild **nur aus dem Thema der Aufgabe**, keine Anekdoten | Interessante, aber irrelevante Details schaden vor allem Lernenden ohne Vorwissen (Sundararajan & Adesope 2020, Educational Psychology Review 32, 707–734). |
| Grenze der Analogie wird immer genannt | Fachlich ehrlich; unterscheidet Tutor von generischen Erklärungen. |
| Antworten werden nicht länger | Vorgabe aus #67. Der Bogen ersetzt den bisherigen Text in denselben Satzgrenzen. |
| Persönlichkeits- oder Stilwahl kommt **nicht** in diese Runde | Bräuchte neue Befehle und Akzeptanzfälle; geparkt. |

## Globale Grenzen (gelten für jede Aufgabe)

- `dist/kern.md` ≤ 4000 Zeichen (Stand vorher: 3964). `<!-- kern -->`-Abschnitte in `tutor/SKILL.md` nicht ändern.
- Skill-`description` ≤ 1024 Zeichen; genau 11 Moduldateien; kein Hochschul- oder Kursbezug im Skill (`test_skill_is_course_neutral`).
- Überschriften bleiben exakt wie bisher auf Deutsch; keine neuen Emoji-Überschriften. Bogenteile sind Sätze, keine Unterüberschriften.
- Lösungsschutz geht allem vor: Einstieg, Bild, Grenze und Brücke dürfen kein Ergebnis, keinen eingesetzten Wert und keine Auswahlentscheidung der Originalaufgabe verraten.
- `dist/` nur über `python build.py`; nie von Hand.
- Nach jeder Änderung an einer gehashten Datei den Eintrag in `Obsidian-tutor/Quellen.sha256.json` bewusst erneuern (normalisiert `utf8-lf`) und betroffene Vault-Notizen prüfen. CI führt `verify_vault.py` aus.
- Jede Aufgabe: Eintrag unter `## [Unveröffentlicht]` in `CHANGELOG.md`; neue Akzeptanzfälle mit dem Vermerk „nicht nativ geprüft“.

## Prüffokus (nicht durch Strukturtests abgedeckt; nativ prüfen)

1. **Auswahl- oder Ja/Nein-Aufgabe in `erklär`:** Der Einstieg darf nicht schon die richtige Option nahelegen. Abgedeckt durch U08.
2. **Reine Mathematikaufgabe ohne Alltagsbezug:** Der Bogen darf ein mathematisches Bild nutzen (Fläche, Steigung, Waage) statt einen Alltagsvergleich zu erzwingen. Abgedeckt durch U09.
3. **Erklärsprache Arabisch:** Bogensätze in der Erklärsprache, Überschriften und Gesetzesnamen deutsch, Fachbegriffe in Klammern. Abgedeckt durch U07.
4. **„weiß nicht“ in anderer Sprache** („ما بعرف“, „bilmiyorum“): gleiche Behandlung wie auf Deutsch. Abgedeckt durch U10.
5. **Antwortlänge:** `erklär` passt weiterhin auf etwa zwei Bildschirmseiten; in jedem neuen Fall die Länge mit der Vorfassung vergleichen.

---

### Aufgabe 1: Zu breite Wirksamkeitsaussagen korrigieren

**Dateien:**
- Ändern: `tutor/references/didaktik.md` (Punkt „Lösung nur mit Schranke“)
- Ändern: `docs/KONZEPT.md` (Evidenzspalte der Prinzipientabelle; Zeile „Grundsätzliche Grenze“)
- Test: `tests/test_build.py`

- [ ] **Schritt 1: Fehlschlagenden Test schreiben** – `test_didaktik_makes_no_proven_effect_claim`: liest `tutor/references/didaktik.md` und prüft `assertNotIn("nachweislich", text)`.
- [ ] **Schritt 2:** `python -B -m unittest discover -s tests -v` → dieser Test FAIL.
- [ ] **Schritt 3: Text ersetzen.**
  - Alt: „Freier Zugriff auf fertige Lösungen verbessert das Üben, verschlechtert aber nachweislich das spätere Ergebnis ohne Hilfe. Deshalb ist der Lösungsschutz streng.“
  - Neu: „Unbeschränkter Zugriff auf fertige Lösungen kann gutes Üben und schwaches späteres Können ohne Hilfe auseinanderfallen lassen. Deshalb ist der Lösungsschutz streng.“
  - `KONZEPT.md`, Evidenzspalte: jeden Eintrag „stark“ / „sehr stark“ durch „siehe `docs/planung/2026-10-27-evidenz-update.md`“ ersetzen; in der Zeile „Verteiltes Lernen“ zusätzlich „Wiederholungskarte „nach zwei Tagen““ → „Wiederholungskarte in zwei Stufen“ (passend zu Aufgabe 4).
  - `KONZEPT.md`, „Grundsätzliche Grenze“: „laut Forschung der schwächsten Lernform“ → „das ersetzt keinen eigenen Versuch“.
- [ ] **Schritt 4:** `python build.py` → Tests PASS → Hashes für geänderte Dateien (`tutor/references/didaktik.md`, `docs/KONZEPT.md`, `dist/kern.md`, `dist/system-prompt.md`, `dist/tutor-chatgpt.zip`, `tests/test_build.py`, `CHANGELOG.md`) erneuern → `python -B Obsidian-tutor/verify_vault.py` → `"status": "PASS"`.
- [ ] **Schritt 5: Commit** `fix(tutor): Wirksamkeitsaussagen auf Evidenzstand gebracht`.

### Aufgabe 2: Erklärbogen als eigener Erklärstil

**Dateien:**
- Ändern: `tutor/references/antwortvorlage.md` (Abschnitt 4 „🧠 Idee“)
- Ändern: `tutor/modes/erklaer.md` (Aufbau 2 und 4), `tutor/modes/voll.md` (Aufbau 3 und 4, Regel „Zwei getrennte Erklärungen“), `tutor/modes/thema.md` (Regel „✏️ Erklärung“)
- Ändern: `tests/akzeptanz.md` (U07, U08, U09), `tests/test_build.py`

**Schnittstellen:** Liefert den Begriff **„Erklärbogen“** in `antwortvorlage.md` Abschnitt 4; alle drei Modi verweisen mit genau diesem Wort darauf. Aufgabe 3 verweist für den Zugangswechsel auf das „Bild“ des Erklärbogens.

- [ ] **Schritt 1: Fehlschlagenden Test schreiben** – `test_explaining_modes_use_erklaerbogen`: `antwortvorlage.md` enthält „Erklärbogen“ und „Grenze“ und nicht mehr „Feynman-Stil“; `erklaer.md`, `voll.md`, `thema.md` enthalten je „Erklärbogen“.
- [ ] **Schritt 2:** Test → FAIL.
- [ ] **Schritt 3: Abschnitt 4 der Antwortvorlage ersetzen** (exakter Text):

  > 4. **🧠 Idee** – der **Erklärbogen** in 3–5 Sätzen ohne Formeln, in dieser Reihenfolge: (1) **Einstieg:** eine überraschende Frage oder Beobachtung, die genau zum Thema der Aufgabe gehört; (2) **Bild:** genau eine Analogie oder Anschauung, die bis zum Ende beibehalten wird, bei reiner Mathematik ein mathematisches Bild (Fläche, Steigung, Waage); (3) **Grenze:** ein Satz, wo das Bild nicht mehr stimmt; (4) **Kernsatz:** die Idee in einem Satz, den der Lernende selbst wiederholen kann. Folgt danach eine Gleichung, verbindet zuerst ein **Brückensatz** jedes Symbol mit einem Teil des Bildes. Keine Anekdoten, Nebenthemen oder Nachahmung bestimmter Personen; nichts davon verrät ein Ergebnis oder eine Auswahl der Aufgabe.

- [ ] **Schritt 4: Modi anpassen** (nur Verweise, gleiche Satzgrenzen):
  - `erklaer.md` Aufbau 2: „**🧠 Idee** – Erklärbogen (Antwortvorlage, Abschnitt 4) in 3–5 Sätzen; der Einstieg benennt zugleich, welche Art von Aufgabe das ist.“ Aufbau 4: vor dem ersten Gesetz der Brückensatz.
  - `voll.md` Aufbau 3: „**🧠 Anschauliche Erklärung** – Erklärbogen in 4–6 Sätzen ohne Formeln; Bild aus Alltag oder Elektronik, wo es passt.“ Aufbau 4 beginnt mit dem Brückensatz. Regel „Zwei getrennte Erklärungen“ ergänzen: „außer dem einen Brückensatz am Anfang von Abschnitt 4“.
  - `thema.md` Regel „✏️ Erklärung“: „anschaulich als Erklärbogen, dann formal mit Brückensatz, dann ein Zahlen- oder Alltagsbeispiel ohne Originalrechnung.“
- [ ] **Schritt 5: Akzeptanzfälle U07–U09** in `tests/akzeptanz.md` unter „Lernfluss und Fachkonventionen“:

  | ID | Eingabe | Erwartung |
  |---|---|---|
  | U07 | `[ar]` + `erklär`: Kondensator wird über einen Widerstand aufgeladen, Zeit bis 63 % gesucht | Erklärbogen vollständig (Einstieg, ein Bild, Grenze, Kernsatz), Sätze auf Arabisch, Überschriften und Gesetzesname deutsch; Brückensatz vor der Gleichung; kein Zahlenergebnis. |
  | U08 | `erklär`: Auswahlaufgabe „Welche Aussagen zur gleichförmigen Kreisbewegung treffen zu?“ | Einstieg und Grenze beurteilen keine Option; keine Option als richtig nahegelegt. |
  | U09 | `voll`: Fläche unter y = x² von 0 bis 2 | Mathematisches Bild statt erzwungenem Alltagsvergleich; Abschnitt 3 ohne Formel, Abschnitt 4 beginnt mit Brückensatz; anderes Beispiel, Original nicht gelöst. |

- [ ] **Schritt 6:** `python build.py`; Tests PASS; `dist/kern.md` unverändert; Hashes erneuern; `verify_vault.py` PASS; Vault-Notiz `06 Modi` prüfen (Beschreibung von `erklär` und `voll` passt weiter, sonst einen Satz ergänzen).
- [ ] **Schritt 7: Commit** `feat(tutor): Erklärbogen als gemeinsamer Erklärstil`.

### Aufgabe 3: „weiß nicht“ in `tipp` und eine Warum-Leitfrage

**Dateien:** `tutor/modes/tipp.md`, `tests/akzeptanz.md` (U10, U11), `tests/test_build.py`

**Schnittstellen:** Nutzt das „Bild“ des Erklärbogens aus Aufgabe 2.

- [ ] **Schritt 1: Fehlschlagenden Test schreiben** – `test_tipp_handles_dont_know_and_asks_why`: `tipp.md` enthält „weiß nicht“ und „Warum gilt“.
- [ ] **Schritt 2:** Test → FAIL.
- [ ] **Schritt 3: Regeln ergänzen.**
  - Unter „## Regeln“ nach „Auf die Aufgabe zugeschnitten“: „**Mindestens eine Warum-Frage:** Eine der Leitfragen fragt nach dem Grund (Typ 3 oder 4, z. B. „Warum gilt hier …?“), nicht nur nach dem Vorgehen.“
  - Unter „## Wenn der Lernende antwortet“ als neuer letzter Punkt: „**„weiß nicht“, „?“ oder eine sehr kurze Antwort ohne Inhalt** (in jeder Sprache): ein Satz Entlastung ohne Lob (sinngemäß „Diese Stelle ist für viele schwer“), dann ein anderer Zugang zur selben Leitfrage: ein Bild im Sinne des Erklärbogens, ein kleines Zahlenbeispiel ohne Originalwerte oder eine kleinere Teilfrage. Beim zweiten Mal hintereinander auf „voll“ verweisen. Keine Lösung, kein Zahlenergebnis.“
- [ ] **Schritt 4: Akzeptanzfälle**

  | ID | Eingabe / Folge | Erwartung |
  |---|---|---|
  | U10 | `tipp` + Aufgabe → „weiß nicht“ → „ما بعرف“ | Erst Entlastung und anderer Zugang zur selben Leitfrage, kein Ergebnis; beim zweiten Mal Verweis auf `voll`; Sprache folgt der Erklärsprache. |
  | U11 | `tipp` + Mechanikaufgabe | Mindestens eine Leitfrage fragt „Warum …?“; weiterhin keine Gleichung und kein Gesetzesname in den Fragen. |

- [ ] **Schritt 5:** Build, Tests, Hashes, `verify_vault.py` PASS.
- [ ] **Schritt 6: Commit** `feat(tutor): tipp reagiert auf „weiß nicht“ und fragt nach dem Warum`.

### Aufgabe 4: Verständnisfrage und Wiederholungskarte präzisieren

**Dateien:** `tutor/references/didaktik.md` (Punkt „🧩 Verständnisfrage“), `tutor/references/antwortvorlage.md` (Abschnitt 15), `tests/akzeptanz.md` (U12), `tests/test_build.py`

- [ ] **Schritt 1: Fehlschlagenden Test schreiben** – `test_review_card_has_two_stages`: `antwortvorlage.md` enthält nicht „nach zwei Tagen“ und enthält „etwa einer Woche“.
- [ ] **Schritt 2:** Test → FAIL.
- [ ] **Schritt 3: Text ändern.**
  - Abschnitt 15 neu: „**🗂 Wiederholungskarte** – eine Frage, eine kurze Antwort; zum Wiederholen in 2–3 Tagen und erneut nach etwa einer Woche. Kein behaupteter Optimalabstand.“
  - Didaktik, Punkt Verständnisfrage, nach „(Vorhersage, Begründung oder „Was ändert sich, wenn …?“)“ einfügen: „Sie prüft ein Prinzip, keine vollständige Rechnung.“
- [ ] **Schritt 4: Akzeptanzfall** U12: `voll` + Aufgabe → Wiederholungskarte nennt zwei Zeitpunkte; Verständnisfrage verlangt keine mehrschrittige Rechnung.
- [ ] **Schritt 5:** Build, Tests, Hashes, `verify_vault.py` PASS.
- [ ] **Schritt 6: Commit** `feat(tutor): Wiederholung zweistufig, Verständnisfrage prüft Prinzip`.

### Aufgabe 5: Dokumentation und Abschluss

**Dateien:** `CLAUDE.md` (neuer Stand-Abschnitt; Anzahl der U-Fälle), `Obsidian-tutor/14 Arbeitsplan.md` (Status je Zeile), `Obsidian-tutor/19 Entscheidungen und Gesprächskontext.md` (Status „implementiert“), `Obsidian-tutor/04 Wissenschaftliche Grundlagen.md` (Hinweis auf behobene Überbehauptungen).

- [ ] **Schritt 1:** Texte aktualisieren; Quellhash für `CLAUDE.md` erneuern.
- [ ] **Schritt 2:** `python -B -m unittest discover -s tests -v` und `python -B Obsidian-tutor/verify_vault.py` PASS.
- [ ] **Schritt 3: Commit** `docs: Umsetzung Erklärbogen und Lernprinzipien dokumentiert`; PR gegen `main`.
- [ ] **Schritt 4 (Mensch):** U07–U12 nativ auf Claude ausführen und in `tests/protokolle/` protokollieren. Erst danach Status „geprüft“.

## Bewusst nicht in diesem Plan

Wählbare Persönlichkeiten oder Stile, Interleaving, Lernstand-Block, Anki-Export, Vergleich „erst Ansatz, dann `erklär`“, Recherche zur Erstsprache. Sie bleiben in `Obsidian-tutor/14 Arbeitsplan.md` unter „Später“ oder „Optional“.

## Rücknahme

Jede Aufgabe ist ein eigener Commit mit eigenem Build. Bei Problemen in der nativen Abnahme genau diesen Commit mit `git revert` zurücknehmen, danach `python build.py` und Hashes prüfen.
