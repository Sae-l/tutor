# physik-mathe-tutor

Lern-Tutor für Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln), ausgelegt für Anfänger mit ADHS: erst anschaulich, dann schrittweise Rechnung, Klausur-Lösung auf Deutsch, Übungen mit versteckten Lösungen.

**Sprache:** standardmäßig Deutsch. Umschalten mit einem Signal in der Nachricht: `[ar]` Arabisch, `[tr]` Türkisch, `[uk]` Ukrainisch, `[fr]` Französisch, `[de]` zurück zu Deutsch. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch.

**Modi:** ohne Zusatz = Standard · `kurz` = nur Lösung · `ausführlich` = mit Vertiefung · eigenen Lösungsversuch mitschicken = Fehlerdiagnose zuerst.

## Aufbau

| Pfad | Zweck |
|---|---|
| `physik-mathe-tutor/` | Quelle: Claude-Skill (`SKILL.md` + `references/`) |
| `dist/system-prompt.md` | Erzeugt: eine einzige, selbstständige Prompt-Datei für alle anderen Plattformen |
| `build.py` | Erzeugt `dist/` aus der Quelle |

Änderungen nur in `physik-mathe-tutor/` machen, danach `python build.py` ausführen und beides committen.

## Einrichtung je Plattform

**Claude (App/Web)** – Ordner `physik-mathe-tutor/` als ZIP packen und unter *Einstellungen → Skills* hochladen. Der Skill startet automatisch bei Physik- oder Mathe-Aufgaben.

**Claude Projects** – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**ChatGPT (Projekt)** – Inhalt von `dist/system-prompt.md` in die Projekt-Anweisungen kopieren.

**ChatGPT (Custom GPT)** – Das Anweisungsfeld ist zu kurz für den ganzen Prompt. `dist/system-prompt.md` unter *Wissen* hochladen und als Anweisung eintragen:

> Du bist ein Physik- und Mathe-Tutor. Lies vor jeder Antwort die Datei system-prompt.md im Wissen und befolge sie vollständig, besonders Sprache, Antwortvorlage und LaTeX-Regeln. Standardsprache ist Deutsch.

**Gemini (Gem)** – Neues Gem anlegen, Inhalt von `dist/system-prompt.md` in die Anweisungen kopieren.

**Microsoft Copilot / GitHub Copilot** – Inhalt von `dist/system-prompt.md` als Anweisungen eines eigenen Agenten (bzw. in `.github/copilot-instructions.md`) eintragen. Ist das Feld zu kurz, wie beim Custom GPT vorgehen: Datei hochladen, Kurzanweisung eintragen.

## Grenzen

- Formeln werden nur dann sauber dargestellt, wenn die Plattform `$$ ... $$` rendert. Getestet in Claude und ChatGPT; Gemini und Copilot sind noch nicht geprüft.
- Bei hochgeladenen Wissensdateien (Custom GPT, Copilot) liest das Modell die Datei nicht immer vollständig. Direkt eingefügte Anweisungen sind zuverlässiger.
- Der Tutor kennt keine internen Bewertungskriterien der TH Köln. Ergebnisse mit offiziellen Musterlösungen abgleichen.
