# tutor

Lern-Tutor für Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln), ausgelegt für Anfänger mit ADHS: erst anschaulich, dann schrittweise Rechnung, Klausur-Lösung auf Deutsch, Übungen mit versteckten Lösungen.

**Sprache:** standardmäßig Deutsch. Umschalten mit einem Signal in der Nachricht: `[ar]` Arabisch, `[tr]` Türkisch, `[uk]` Ukrainisch, `[fr]` Französisch, `[de]` zurück zu Deutsch. Überschriften, Aufgabentext und Klausur-Lösung bleiben immer deutsch.

**Befehle:** ein Wort als erstes Wort oder als ganze Nachricht (z. B. Foto + „tipp“), oder mit `!` irgendwo; kombinierbar mit dem Sprachcode, z. B. `tipp [ar]`. „tutor“ oder „hilfe“ zeigt die Befehlskarte. Empfohlene Reihenfolge beim Lernen: **erklär → tipp → lösung**.

| Befehl | Wirkung |
|---|---|
| (keiner) / `erklär` | Erklärung + ähnliches gelöstes Beispiel, **ohne** Lösung der Aufgabe |
| `standard` | Erklärung mittlerer Tiefe mit Lösung + zwei Übungen |
| `!detail` | ausführlich, mit Vertiefung |
| `!kurz` | knappe Erklärung |
| `!lösung` | direkt die Klausur-Lösung |
| `!tipp` | drei Hinweisstufen, Lösung versteckt |
| `!check` | Fehlerdiagnose des eigenen Versuchs (automatisch, wenn ein Versuch mitkommt) |
| `!übung` | drei neue Aufgaben desselben Typs |
| `!konzept` | Begriff oder Satz verstehen, ohne Rechenaufgabe |

Die Befehle verstehen auch natürliche Wörter in allen fünf Sprachen (z. B. „kurz“, „سريع“, „hızlı“).

**Dauermodus:** `!an tipp` (oder ein anderer Befehl) gilt für alle folgenden Aufgaben, bis `!aus` kommt. Ein Einzelbefehl überschreibt ihn nur für diese eine Nachricht. Jede Antwort zeigt dann oben den aktiven Modus und die Sprache.

## Aufbau

| Pfad | Zweck |
|---|---|
| `tutor/` | Quelle: Claude-Skill (`SKILL.md` + `references/`) |
| `dist/system-prompt.md` | Erzeugt: eine einzige, selbstständige Prompt-Datei für alle anderen Plattformen |
| `build.py` | Erzeugt `dist/` aus der Quelle |

Änderungen nur in `tutor/` machen, danach `python build.py` ausführen und beides committen.

## Einrichtung je Plattform

**Claude (App/Web)** – Ordner `tutor/` als ZIP packen und unter *Einstellungen → Skills* hochladen. Am besten ein Projekt „Tutor“ anlegen und dort lernen: einmal betreten, dann nur noch Foto + ein Befehlswort schicken.

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
