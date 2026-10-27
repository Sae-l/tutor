# tutor – Konzept und Begründung

## 1. Kontext und Ziel

**Zielgruppe:** Studierende eines MINT-Fachs an einer deutschsprachigen Hochschule, Schwerpunkt Studienbeginn, auch höhere Semester (#64), Klausuren auf Deutsch; ADHS-freundlich gestaltet. Entstanden ist der Tutor für einen einzelnen Erstsemester in E-Technik mit ADHS. Lange Gedankenketten im Arbeitsgedächtnis zu halten fällt schwer; der Einstieg ins Lernen muss leicht sein.

**Ziel des Agenten:** nicht Aufgaben für den Lernenden lösen, sondern ihn so führen, dass er **die nächste Aufgabe dieses Typs allein lösen kann**. Praktisch: einmal einrichten, danach nur noch Foto plus ein Befehlswort schicken.

**Entstehung:** Ausgangspunkt war ein einzelner Prompt („Professor für Physik und E-Technik“). Er wurde schrittweise erweitert:
1. Echte Darstellungsfehler (LaTeX in ChatGPT und Claude) führten zu festen Formatregeln.
2. Die Frage, ob das Format das eigene Denken fördert, führte zu den lernwissenschaftlichen Elementen.
3. Bedienungswünsche führten zu Modi, Ein-Wort-Befehlen, Dauermodus und mehreren Erklärsprachen.

## 2. Wissenschaftliche Grundlagen

Einschränkung vorweg: Es wurde **keine eigene systematische Literaturrecherche** durchgeführt. Die Prinzipien stammen aus gut etablierter Lernforschung und sind aus dem Gedächtnis zitiert. Sie belegen die **Prinzipien**, nicht die Wirksamkeit dieses Agenten; der Agent selbst ist noch nicht empirisch getestet. Vor einer Weitergabe des Projekts sind die Quellen mit vollständigen Angaben (Zeitschrift, DOI) nachzuweisen und die Evidenzspalte zu prüfen.

| Prinzip | Kernaussage | Quelle (bekannte Arbeit) | Umsetzung im Agenten | Evidenz |
|---|---|---|---|---|
| Worked-Example-Effekt | Anfänger lernen aus vollständig gelösten Beispielen mehr als aus eigenem Probieren ohne Anleitung | Sweller & Cooper 1985; Cognitive Load Theory (Sweller) | vorgerechnetes Beispiel einer anderen Aufgabe in `voll` | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Expertise-Reversal / Fading | Mit wachsendem Können schaden vollständige Lösungen eher; Hilfe schrittweise ausblenden | Kalyuga u. a. 2003; Renkl & Atkinson 2003 | Eskalation erklär → tipp → voll → kurz; Lösung nur auf Abruf | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Abruf-/Testeffekt | Aktives Abrufen festigt stärker als Wiederlesen | Roediger & Karpicke 2006; Übersicht Dunlosky u. a. 2013 | ⏸-Denkpunkte, Verständnisfrage, Lösungen nur auf Abruf | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Generierungseffekt | Selbst Erzeugtes bleibt besser haften | Slamecka & Graf 1978 | erst vorhersagen, dann weiterlesen (⏸) | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Selbsterklärung | Wer Schritte selbst begründet, versteht tiefer | Chi u. a. 1989/1994 | „warum“ zu jedem Schritt; `check` diagnostiziert den eigenen Versuch | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Verteiltes Lernen | Wiederholen über Tage schlägt Massenlernen | Cepeda u. a. 2006 | Wiederholungskarte in zwei Stufen | siehe `docs/planung/2026-10-27-evidenz-update.md` |
| Problemlöse-Heuristik | Verstehen → planen → ausführen → prüfen | Pólya, *How to Solve It*, 1945 | Gegeben/Gesucht → Lösungsplan → Lösungsweg → Probe | etablierte Didaktik, wenig experimentell |
| Sokratische Methode | Gezielte Fragen statt fertiger Antworten | Didaktik-Tradition; Fragetypen nach Paul & Elder | 4–6 Leitfragen in `tipp`, die sich der Lernende selbst stellt | Praxiswissen, gemischte Evidenz |
| Fehlkonzepte konfrontieren | Falsche Vorstellungen müssen ausdrücklich widerlegt werden | Physikdidaktik (z. B. Hestenes, Force Concept Inventory) | Abschnitt „Falscher Weg“ | gut belegt in Physik |
| Feynman-Technik | Erst anschaulich, dann formal | didaktische Faustregel, keine Studie | Abschnitt „Idee“ vor jeder Rechnung | Heuristik |
| Universal Design for Learning | Was für Lernende mit Einschränkungen hilft, hilft meist allen | CAST (UDL-Rahmen) | eine Struktur für alle statt einer Sonderversion für ADHS | Rahmenmodell, Wirksamkeitsbelege gemischt |

**ADHS-Anpassungen** beruhen nicht auf ADHS-Interventionsstudien, sondern auf der Selbstbeschreibung des Lernenden (Arbeitsgedächtnis, schwieriger Einstieg, externe Struktur hilft) und auf den Prinzipien des Skills `i-have-adhd`:
- kleine Schritte;
- gleichbleibende Überschriften;
- Lösungsplan vorab zur Entlastung des Arbeitsgedächtnisses;
- „Bisher gezeigt“-Zeilen;
- genau eine nächste Aktion mit Zeitangabe;
- kein Lob, keine Floskeln.

Diese Annahmen sind plausibel, für diesen Agenten aber nicht geprüft.

## 3. Funktionen

### Modi
| Befehl | Zweck | Gibt die Lösung der Originalaufgabe? |
|---|---|---|
| (keiner) / `erklär` | Thema und nötige Gleichungen erklären, **ohne** Beispiel | nein |
| `voll` | anschaulich und mathematisch, mit vorgerechnetem Beispiel einer **anderen** Aufgabe | nein |
| `thema` | Begriff, Gesetz oder Beweis verstehen und wie es beim Lösen hilft | nein, nur auf Abruf |
| `tipp` | 4–6 Leitfragen, die sich der Lernende selbst stellt | nein, nur auf Abruf |
| `check` | prüft den eigenen Versuch: was stimmt, **erster** Fehler mit Grund | ab dem Fehler |
| `skizze` | Skizze, Diagramm oder Graph erstellen bzw. beschreiben | – |
| `kurz` | Klausur-Lösung plus eine Anmerkung | ja |
| `mittel` | Erklärung mittlerer Tiefe mit vollständiger Lösung | ja |
| `lang` | Hauptweg plus höchstens zwei andere Lösungswege | ja |
| `klausur` | schnelle Lösung mit Klausur-Tipps | ja |
| `hilfe` | Befehlskarte mit einer Erklärung je Befehl | – |

`lösung` ist kein Modus, sondern ruft zurückgehaltene Lösungen ab.

**Empfohlene Lernkette:** `erklär` → bei Hängen `tipp` → `voll` → `kurz`; eigenen Versuch jederzeit schicken (`check`).

### Weitere Funktionen
- **Ein-Wort-Befehle:** als erstes Wort oder als ganze Nachricht (z. B. Foto + „tipp“); mit `!` auch mitten im Text. Normale Wörter im Aufgabentext lösen so keinen Befehl aus.
- **Dauermodus:** `!an tipp` gilt für alle folgenden Aufgaben, `!aus` schaltet zurück. Eine Statuszeile zeigt den Zustand, damit er in langen Chats nicht verloren geht.
- **Hilfe:** „tutor“, „hilfe“ oder „help“ als ganze Nachricht zeigt die Befehlskarte: elf Befehle mit je einer Erklärung.
- **Sprachen:** Standard Deutsch; `[ar]`, `[tr]`, `[fr]`, `[en]`, `[ur]` oder `!sprache xx` wechseln die Erklärsprache. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer Deutsch (Prüfungsvokabular); in anderen Sprachen kommen deutsche Fachbegriffe in Klammern und eine Begriffstabelle dazu.
- **Foto/PDF:** Der Aufgabentext wird zuerst abgeschrieben; Unleserliches wird als [unleserlich] markiert statt geraten.
- **Genauigkeit:**
  - keine erfundenen Werte;
  - Konstanten nach CODATA;
  - Annahmen mit ⚠;
  - Rechnungen wenn möglich mit Rechenwerkzeug geprüft;
  - keine Behauptungen über Bewertungskriterien einer bestimmten Hochschule.
- **Formelsatz:** DIN 1338 (Dezimalkomma, aufrechte Einheiten). Formeln nur in `$$…$$`, nur ASCII in LaTeX, weil `\[`, Umlaute und Formeln im arabischen Fließtext nachweislich falsch dargestellt wurden.
- **Lehrhaltung:**
  - ehrlich bewerten (richtig / teilweise / falsch mit Grund);
  - an Vorhandenes anknüpfen;
  - anders erklären statt lauter wiederholen;
  - Methode vor Ergebnis.

## 4. Architektur

```
tutor/
├── SKILL.md                 Router: Zweck, Ablauf, Befehle → Moduldatei, Lösungsschutz; kern-Abschnitte
├── modes/                   ein Modus pro Datei (11 Dateien)
└── references/
    ├── antwortvorlage.md    Katalog der Abschnitte 0–19 (Moduldateien wählen per Nummer)
    ├── didaktik.md          Aufgabentypen, Lehrhaltung, Lernprinzipien, ADHS, Genauigkeit
    ├── sprache.md           Erklärsprachen und Signale
    └── latex-regeln.md      Formatregeln mit Fehlbeispielen
kurse/                       optionale Kurspakete (z. B. mpg1.md), nicht Teil des Skills
build.py                     erzeugt dist/ und bricht bei offenen Verweisen ab
dist/system-prompt.md        alles in einer Datei (Wissensdatei für ChatGPT Projekt, Gemini)
dist/kern.md                 Kern für Anweisungsfelder (≤ 4000 Zeichen), aus SKILL.md erzeugt
tests/                       Strukturtests, Akzeptanzfälle, Protokolle
```

**Begründung:**
- **Ein Skill als Router statt elf Einzelskills:** Der Befehl wählt die Moduldatei eindeutig. Elf Skills würde das Modell oft falsch auswählen, und die gemeinsamen Regeln müssten elffach gepflegt werden.
- **Progressive Offenlegung:** Pro Antwort wird nur die nötige Moduldatei gelesen. Das spart Tokens und erhöht die Regeltreue.
- **Eine Quelle, zwei Ausgaben:** Andere Plattformen können keine Dateien nachladen. `build.py` fügt alles zusammen und prüft, dass kein Dateiverweis übrig bleibt.
- **Zustand nur im Chat:** Dauermodus und Sprache stehen im Gesprächsverlauf, daher die Statuszeile.

## 5. Stand und Grenzen

- **Geprüft:** Strukturtests (`tests/test_build.py`, auch in der CI): reproduzierbarer Build, alle Befehle zeigen auf existierende Moduldateien, keine offenen Dateiverweise, Länge des Kerns.
- **Nicht geprüft:**
  - Lehrverhalten mit einem Modell (Akzeptanzfälle in `tests/akzeptanz.md` sind vorbereitet, nicht ausgeführt);
  - Formeldarstellung in Gemini und Copilot;
  - Wirksamkeit für das Lernen, auch nicht für ADHS.
- **Grundsätzliche Grenze:** Der Lerneffekt entsteht nur, wenn Denkpunkte und Leitfragen wirklich selbst bearbeitet werden. Wer immer sofort `lösung` nutzt, landet beim reinen Lesen von Lösungen, das ersetzt keinen eigenen Versuch.
