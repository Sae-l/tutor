# Sicherheit

## Geltungsbereich

Der Tutor ist eine Sammlung von Prompt- und Skill-Dateien plus ein Build-Skript ohne Fremdpakete. Relevante Risiken sind vor allem:

- Prompt-Injection über Aufgabentexte, Fotos oder PDFs, die den Lösungsschutz oder die Modusregeln aushebeln;
- versehentlich mitversionierte oder mitgepackte private Daten (Werkzeugzustände, Kursunterlagen, Aufgabenfotos);
- GitHub-Actions-Workflows.

## Unterstützte Versionen

Bisher gibt es nur Vorabversionen (`v0.x.0-rc.N`). Unterstützt wird nur der aktuelle Stand von `main`; ältere Vorabversionen bekommen keine Korrekturen.

## Meldeweg

Das Repository ist öffentlich und hat einen Maintainer (GitHub: [@Sae-l](https://github.com/Sae-l)). Ein eigener privater Meldekanal (z. B. GitHubs private Schwachstellenmeldung) ist **noch nicht eingerichtet**.

- Nicht vertrauliche Funde: Issue mit der Vorlage „Fehler im Tutorverhalten“.
- Vertrauliche Funde (Zugangsdaten, private Daten im Verlauf, Umgehung des Lösungsschutzes mit Missbrauchspotenzial): im Issue nur „vertraulicher Sicherheitsfund, bitte Kontakt“ schreiben, ohne Details. Der Maintainer meldet sich über einen privaten Weg.

## Aufgabenbilder und Kursunterlagen

Keine Fotos von Prüfungen, keine Kursunterlagen des Dozenten und keine personenbezogenen Daten in Issues, PRs, Protokollen oder Commits. Kursunterlagen liegen nur lokal in `referenzen/` (per `.gitignore` ausgeschlossen). Für Abnahmeprotokolle selbst erstellte Aufgaben verwenden oder bei Kursaufgaben nur Blatt und Nummer nennen.

## Workflows

Workflows erhalten nur Leserechte (`permissions: contents: read`), Actions sind auf vollständige Commit-SHAs festgelegt, Checkout ohne gespeicherte Zugangsdaten. Kein fremder PR-Code mit privilegiertem Token (`pull_request_target`). Dependabot schlägt Aktualisierungen der festgelegten SHAs vor (`.github/dependabot.yml`).
