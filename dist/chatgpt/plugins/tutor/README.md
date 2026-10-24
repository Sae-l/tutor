# Tutor

Lern-Tutor für MINT-Aufgaben im ersten Studienjahr an deutschsprachigen Hochschulen: Physik, Mathematik und Elektrotechnik. Der Tutor erklärt das Thema, stellt Leitfragen, prüft eigene Rechenwege und hält die vollständige Lösung zurück, bis du sie ausdrücklich verlangst. So übst du selbst, statt abzuschreiben.

## Installation

- Claude Code: `/plugin install tutor --marketplace Sae-l/tutor`
- Codex: `codex plugin marketplace add Sae-l/tutor`, danach in Codex `/plugins` öffnen und Tutor installieren.
- claude.ai, ChatGPT und Gemini: Anleitung auf https://sae-l.github.io/tutor/#einrichten

## Benutzung

Schreib eine Aufgabe und davor einen der elf Befehle, zum Beispiel `erklär`, `tipp`, `check`, `voll` oder `klausur`. `hilfe` zeigt alle Befehle mit kurzer Erklärung. Ohne Befehl erklärt der Tutor zuerst das Thema.

Erklärsprache ist Deutsch. Auf Wunsch erklärt er auf Arabisch, Türkisch, Französisch, Englisch oder Urdu; Überschriften, Aufgabentext und Fachbegriffe bleiben Deutsch.

## Was das Plugin tut

Das Plugin enthält nur einen Skill aus Markdown-Dateien. Es führt keine Programme aus, ruft keine Server auf und speichert nichts. Gespräche bleiben beim jeweiligen Anbieter. Der Befehl `!issue` erzeugt nur einen Link zu GitHub-Issues; Gesprächsinhalte werden nicht gesendet.

## Mehr

- Website und Anleitung: https://sae-l.github.io/tutor/
- Quellcode, Fragen und Fehlermeldungen: https://github.com/Sae-l/tutor
- Lizenz: MIT
