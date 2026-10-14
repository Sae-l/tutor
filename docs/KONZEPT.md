# tutor – Konzept und Begründung

## 1. Kontext und Ziel

**Zielgruppe:** Erstsemester im berufsbegleitenden B.Eng. Elektrotechnik an der TH Köln, Klausuren auf Deutsch, Lernende mit ADHS. Lange Gedankenketten im Arbeitsgedächtnis zu halten fällt schwer; der Einstieg ins Lernen muss leicht sein.

**Ziel des Agenten:** nicht Aufgaben für den Lernenden lösen, sondern ihn so führen, dass er **die nächste Aufgabe dieses Typs allein lösen kann**. Praktisch: einmal einrichten, danach nur noch Foto plus ein Befehlswort schicken.

**Entstehung:** Ausgangspunkt war ein einzelner Prompt („Professor für Physik und E-Technik“). Er wurde schrittweise erweitert:
1. Echte Darstellungsfehler (LaTeX in ChatGPT und Claude) führten zu festen Formatregeln.
2. Die Frage, ob das Format das eigene Denken fördert, führte zu den lernwissenschaftlichen Elementen.
3. Bedienungswünsche führten zu Modi, Ein-Wort-Befehlen, Dauermodus und fünf Sprachen.

## 2. Wissenschaftliche Grundlagen

Einschränkung vorweg: Es wurde **keine eigene systematische Literaturrecherche** durchgeführt. Die Prinzipien stammen aus gut etablierter Lernforschung und sind aus dem Gedächtnis zitiert. Sie belegen die **Prinzipien**, nicht die Wirksamkeit dieses Agenten; der Agent selbst ist noch nicht empirisch getestet.

| Prinzip | Kernaussage | Quelle (bekannte Arbeit) | Umsetzung im Agenten | Evidenz |
|---|---|---|---|---|
| Worked-Example-Effekt | Anfänger lernen aus vollständig gelösten Beispielen mehr als aus eigenem Probieren ohne Anleitung | Sweller & Cooper 1985; Cognitive Load Theory (Sweller) | ähnliches gelöstes Beispiel in `erklär` | stark |
| Expertise-Reversal / Fading | Mit wachsendem Können schaden vollständige Lösungen eher; Hilfe schrittweise ausblenden | Kalyuga u. a. 2003; Renkl & Atkinson 2003 | Übungen halb gelöst → ungelöst; Eskalation erklär → tipp → lösung | stark |
| Abruf-/Testeffekt | Aktives Abrufen festigt stärker als Wiederlesen | Roediger & Karpicke 2006; Übersicht Dunlosky u. a. 2013 | ⏸-Denkpunkte, Übungen, Wiederholungskarte, Lösungen unter 🔒 | sehr stark |
| Generierungseffekt | Selbst Erzeugtes bleibt besser haften | Slamecka & Graf 1978 | erst vorhersagen, dann weiterlesen (⏸) | stark |
| Selbsterklärung | Wer Schritte selbst begründet, versteht tiefer | Chi u. a. 1989/1994 | „warum“ zu jedem Schritt; `check` diagnostiziert den eigenen Versuch | stark |
| Verteiltes Lernen | Wiederholen über Tage schlägt Massenlernen | Cepeda u. a. 2006 | Wiederholungskarte „nach zwei Tagen“ | sehr stark |
| Interleaving | Gemischte Aufgabentypen verbessern das Erkennen des Lösungswegs | Rohrer & Taylor 2007 | `übung` verändert die Aufgabe wesentlich, nicht nur die Zahlen | mittel bis stark |
| Problemlöse-Heuristik | Verstehen → planen → ausführen → prüfen | Pólya, *How to Solve It*, 1945 | Gegeben/Gesucht → Lösungsplan → Lösungsweg → Probe | etablierte Didaktik, wenig experimentell |
| Sokratische Methode | Gezielte Fragen statt fertiger Antworten | Didaktik-Tradition; Fragetypen nach Paul & Elder | Hinweisleiter in `tipp` (Klärung → Werkzeug → erster Schritt) | Praxiswissen, gemischte Evidenz |
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
| Befehl | Zweck | Gibt die Lösung? |
|---|---|---|
| (keiner) / `erklär` | Gesetze, Gültigkeit, Vorgehen und ein **ähnliches gelöstes Beispiel** | nein |
| `tipp` | drei Hinweisstufen (Orientierung → Werkzeug → erster Schritt) | versteckt |
| `lösung` | Ergebnis + Klausur-Lösung zum Vergleichen | ja |
| `kurz` | knapper Weg bei wenig Zeit | ja |
| `check` | prüft den eigenen Versuch: was stimmt, **erster** Fehler mit Fehlerart | ab dem Fehler |
| `übung` | drei neue Aufgaben (leicht, mittel, klausurnah) | versteckt |
| `konzept` | Begriff, Gesetz oder Beweis verstehen | – |
| `standard` | Erklärung mit vollständiger Lösung + zwei Übungen | ja |
| `detail` | wie `standard` + Vertiefung (Kernidee, Falscher Weg, Was wäre wenn, Alternativweg) | ja |

**Empfohlene Lernkette:** `erklär` → bei Hängen `tipp` → zum Vergleichen `lösung` oder eigenen Versuch schicken (`check`).

### Weitere Funktionen
- **Ein-Wort-Befehle:** als erstes Wort oder als ganze Nachricht (z. B. Foto + „tipp“); mit `!` auch mitten im Text. Normale Wörter im Aufgabentext lösen so keinen Befehl aus.
- **Dauermodus:** `!an tipp` gilt für alle folgenden Aufgaben, `!aus` schaltet zurück. Eine Statuszeile zeigt den Zustand, damit er in langen Chats nicht verloren geht.
- **Hilfe:** „tutor“ oder „hilfe“ zeigt eine Befehlskarte mit höchstens 10 Zeilen.
- **Sprachen:** Standard Deutsch; `[ar]`, `[tr]`, `[uk]`, `[fr]` wechseln die Erklärsprache. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer Deutsch (Prüfungsvokabular); in anderen Sprachen kommen deutsche Fachbegriffe in Klammern und eine Begriffstabelle dazu.
- **Foto/PDF:** Der Aufgabentext wird zuerst abgeschrieben; Unleserliches wird als [unleserlich] markiert statt geraten.
- **Genauigkeit:**
  - keine erfundenen Werte;
  - Konstanten nach CODATA;
  - Annahmen mit ⚠;
  - Rechnungen wenn möglich mit Rechenwerkzeug geprüft;
  - keine Behauptungen über Bewertungskriterien der TH Köln.
- **Formelsatz:** DIN 1338 (Dezimalkomma, aufrechte Einheiten). Formeln nur in `$$…$$`, nur ASCII in LaTeX, weil `\[`, Umlaute und Formeln im arabischen Fließtext nachweislich falsch dargestellt wurden.
- **Lehrhaltung:**
  - ehrlich bewerten (richtig / teilweise / falsch mit Grund);
  - an Vorhandenes anknüpfen;
  - anders erklären statt lauter wiederholen;
  - Methode vor Ergebnis.

## 4. Architektur

```
tutor/
├── SKILL.md                 Router: Sprache, Befehle → Moduldatei, gemeinsame Regeln
├── modes/                   ein Modus pro Datei (9 Dateien)
└── references/
    ├── antwortvorlage.md    Katalog der Abschnitte 0–19 (Moduldateien wählen per Nummer)
    └── latex-regeln.md      Formatregeln mit Fehlbeispielen
build.py                     erzeugt dist/system-prompt.md
dist/system-prompt.md        alles in einer Datei für ChatGPT, Gemini, Copilot
```

**Begründung:**
- **Ein Skill als Router statt neun Einzelskills:** Der Befehl wählt die Moduldatei eindeutig. Neun Skills würde das Modell oft falsch auswählen, und die gemeinsamen Regeln müssten neunfach gepflegt werden.
- **Progressive Offenlegung:** Pro Antwort wird nur die nötige Moduldatei gelesen. Das spart Tokens und erhöht die Regeltreue.
- **Eine Quelle, zwei Ausgaben:** Andere Plattformen können keine Dateien nachladen. `build.py` fügt alles zusammen und prüft, dass kein Dateiverweis übrig bleibt.
- **Zustand nur im Chat:** Dauermodus und Sprache stehen im Gesprächsverlauf, daher die Statuszeile.

## 5. Stand und Grenzen

- **Geprüft:** Skill-Validierung; Konsistenzskript (alle 9 Befehle zeigen auf existierende Moduldateien, alle Abschnittsnummern existieren).
- **Nicht geprüft:**
  - echte Aufgaben in den einzelnen Modi;
  - Formeldarstellung in Gemini und Copilot;
  - ob der Universal-Prompt (ca. 23 000 Zeichen) in alle Anweisungsfelder passt.
- **Grundsätzliche Grenze:** Der Lerneffekt entsteht nur, wenn Denkpunkte und Übungen wirklich selbst bearbeitet werden. Wer immer sofort `lösung` nutzt, landet beim reinen Lesen von Lösungen, laut Forschung der schwächsten Lernform.
