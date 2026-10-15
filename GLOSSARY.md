# Tutor

Lern-Agent für MINT-Fächer im ersten Studienjahr, öffentlich nutzbar; ADHS-Freundlichkeit ist Gestaltungsprinzip. Dieses Glossar legt die Wörter fest, mit denen Skill, Prompt, Tests und Planung über ihn sprechen.

## Language

### Beteiligte und Artefakte

**Lernender**:
Die Person, die den Tutor benutzt: Studierende im ersten Studienjahr eines deutschsprachigen MINT-Studiengangs.
_Avoid_: Nutzer, Student, User

**Tutor**:
Der Lern-Agent als Ganzes, unabhängig davon, in welcher Form er läuft.
_Avoid_: Bot, Assistent

**Skill**:
Die gemeinsame Quelle in `tutor/` aus `SKILL.md`, `modes/` und `references/`; einzige Quelle der Wahrheit für Claude, natives ChatGPT-Plugin und System-Prompt.
_Avoid_: Agent-Ordner

**System-Prompt**:
Die aus dem Skill erzeugte Einzeldatei `dist/system-prompt.md` für Plattformen ohne Dateizugriff.
_Avoid_: Universal-Prompt (nur als Beiname), Export

**Kern**:
Die aus markierten Abschnitten des Skills erzeugte Kurzform `dist/kern.md` mit höchstens 4000 Zeichen für Anweisungsfelder; der System-Prompt liegt daneben als Datei.
_Avoid_: Kurzfassung (abgelöst), Mini-Prompt, Light-Version

**Kurspaket**:
Eine optionale Datei mit Notation und Stoffumfang eines bestimmten Kurses, die der Lernende zusätzlich mitgibt; liegt in `kurse/`, nie im Skill.
_Avoid_: Kursreferenz

**ChatGPT-Plugin**:
Das aus der Skillquelle erzeugte Paket mit Manifest und Lizenz unter `dist/chatgpt/plugins/tutor/` und als Importarchiv `dist/tutor-chatgpt.zip`. Der lokale Marketplace unter `dist/chatgpt/` ist ein zusätzlicher Desktop-Installationsweg; er ist keine öffentliche Veröffentlichung.

### Steuerung

**Modus**:
Eine Antwortart des Tutors mit eigener Moduldatei in `tutor/modes/`; es gibt elf (zehn Aufgabenmodi und Hilfe).
_Avoid_: Stufe, Variante

**Befehl**:
Das Wort oder die Wortgruppe, die einen Modus auswählt.
_Avoid_: Kommando, Schalter

**Voreinstellung**:
Der Modus Erklär, wenn weder Einzelbefehl noch Dauermodus noch automatische Wahl greift.
_Avoid_: Standard, Default

**Einzelbefehl**:
Ein Befehl, der nur für die Nachricht gilt, in der er steht.

**Dauermodus**:
Ein mit `!an <befehl>` gesetzter Modus, der für alle folgenden Aufgaben gilt, bis `!aus` kommt.
_Avoid_: Sitzungsmodus

**Eskalation**:
Die empfohlene Folge erklär, tipp, voll, kurz, wenn der Lernende nicht weiterkommt.

**Statuszeile**:
Die Zeile oben in der Antwort, die tatsächlichen Modus, gespeicherten Dauermodus und Sprache nennt.

### Sprache

**Erklärsprache**:
Die Sprache der Erklärtexte (Deutsch, Arabisch, Türkisch, Französisch, Englisch, Urdu); wechselt nur per Sprachsignal.
_Avoid_: Antwortsprache, Sprache der Nachricht

**Sprachsignal**:
Ein Code wie `[ar]` oder eine ausgeschriebene Wendung, die die Erklärsprache umschaltet.

### Antwortaufbau

**Antwortvorlage**:
Der Katalog der nummerierten Abschnitte, aus dem die Moduldateien auswählen.

**Abschnitt**:
Ein Baustein einer Antwort mit festem deutschem Titel und Symbol.
_Avoid_: Block, Kapitel

**Klausur-Lösung**:
Die immer deutsche, knappe Lösung im Stil der Klausur: Ansatz, wesentliche Schritte, Ergebnis.

**Lösungsschutz**:
Die Regel, dass die Tipp-Lösung und Antworten auf Verständnisfragen erst erscheinen, wenn der Lernende „lösung“ schreibt; „lösung“ ist kein Modus.
_Avoid_: Spoiler-Schutz

**Verständnisfrage**:
Die eine Frage vor „➡️ Nächster Schritt“, die Verstehen statt Auswendiglernen prüft; Antwort nur auf Abruf.

**Leitfragen**:
Die 4–6 Fragen im Modus Tipp, die sich der Lernende selbst stellen muss, um zur Lösung zu kommen; nur Fragen, keine Antworten.
_Avoid_: Hinweisleiter, Hinweisstufen

**Aufgabentyp**:
Die Art einer Aufgabe: Rechnung, Nachweis, Skizze, Begründung oder Messdaten; bestimmt, was die Antwortvorlage zeigt.

**Endantwort**:
Die Ergebnisliste am Ende eines Übungsblatts; Aufgabenmaterial, das fehlerhaft sein kann und unabhängig nachgerechnet wird.
_Avoid_: Musterlösung

### Prüfung

**Strukturtest**:
Ein Python-Test in `tests/`, der Build, Dateiverweise und Textregeln prüft, aber nicht das Verhalten eines Modells.
_Avoid_: Test (ohne Zusatz)

**Akzeptanzfall**:
Ein vorbereiteter manueller Fall in `tests/akzeptanz.md`, der ein Modell mit einer Eingabe prüft und protokolliert wird.
_Avoid_: Modelltest, Abnahmetest
