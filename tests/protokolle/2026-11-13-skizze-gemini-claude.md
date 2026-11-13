# Protokoll: `skizze` auf Gemini und Claude, Auswertung der Meldungen #110, #111, #113

Ausgewertet am 2026-11-13 anhand von Bildschirmfotos, die der Maintainer im Chat geschickt hat (nicht öffentlich hochgeladen). Kein Gate-Lauf.

| Fall | Quelle | Oberfläche, Stand | Ergebnis |
|---|---|---|---|
| A | Gemini-Chat „Hydrogen Hoch“, 13.11.2026 18:05, Folgebefehl `Skizze` zu einer Motorboot-Leistungsaufgabe (v₁ = 4,0 km/h, P₁ = 7,5 kW, v₂ = 12 km/h, P₂ gesucht, F_W = k·v) | Gemini-App Android, Tutor rc.5 | **Nicht bestanden** |
| B | Geteilter Gemini-Chat vom 5.11.2026 (#110/#111), `Skizze` zu „Körper 5,0 kg hängt an einem Seil … Kräftediagramm, Reaktionskräfte“ | Gemini-App, Tutor rc.5 | Regelkonform; Erwartung des Lernenden nicht erfüllt |
| C | Gleicher Chat, zweite Antwort mit TikZ statt matplotlib | wie B | Regelkonform; Erwartung nicht erfüllt |
| D | #113 „skizze Claude“: gerenderte Skizze zu einer Relativitätsaufgabe (Zug mit Marschall, v = 50 m/s, Männer A und B, Δx = 50 m) | claude.ai (Visualisierung sichtbar) | Keine Regelverletzung erkennbar; Meldungstext leer |

## Befunde

**A (Regelverstoß):**
1. Die Skizze ist eine ASCII-Zeichnung in einem ```` ```text ````-Block (Pfeile `<-------`, Kasten `[=====]`). `skizze.md` verbietet Textgrafik aus Zeichen; das Modell hielt den Codeblock offenbar für erlaubt.
2. Unter der Zeichnung steht „Kräftegleichgewicht … F_Zug − F_W = 0 ⟹ F_Zug = F_W = k · v“. Das ist der entscheidende Schritt der Aufgabe (mit P = F·v folgt P ∝ v², also P₂ = 67,5 kW) und hätte im Modus `skizze` nicht erscheinen dürfen. Die Vorlage nannte „Kräftegleichgewicht“ ausdrücklich als Beispiel für die Kontrolle; das hat die Gleichung begünstigt.
3. „Gegebene Betriebszustände“ und Formeldarstellung sind korrekt; 🔒 Lösungen folgt.

**B, C (regelkonform, aber unbefriedigend):** Gemini sagt in einem Satz, dass keine Bildanzeige möglich ist, und liefert Kräftetabelle plus lauffähigen matplotlib- bzw. TikZ-Code ohne Lösungsverrat. Der Lernende fragte danach „warum wird das graphische skizze …“ (nicht angezeigt). Die Gemini-App führt Python laut Google-Hilfe nur in bestimmten Tarifen aus; ein sichtbares Bild ist dort nicht garantiert.

**D:** Die Skizze ist als Bild sichtbar und zeigt nur Gegebenes (Δt′ = 0 im Zugsystem, v = 50 m/s, Δx = 50 m, Lage von A und B). Ohne Beschreibung des Melders ist kein Fehler bestimmbar.

## Änderungen

- `skizze.md`: keine Textgrafik „auch nicht in einem Codeblock“; Kontrolle in Worten ohne Gleichung aus der Originalaufgabe (Beispiel „Kräftegleichgewicht“ ersetzt); Verbot aufgestellter Gleichungen (Kräftegleichgewicht, Energie- oder Bewegungsgleichungen) in Skizze und Begleittext; bei fehlender Bildanzeige ein Satz, wie der Lernende das Bild aus dem Code selbst erzeugt.
- Verhaltens-Eval: Fall `R-LS02-Skizze` mit derselben Bootaufgabe, Muster gegen ASCII-Pfeile/-Kästen, `F_Zug = F_W` und 67,5 kW, dazu Bewertung durch Claude.

## Offen

- D: Melder von #113 nach dem erwarteten Verhalten fragen.
- B/C: Entscheidung, ob für Gemini ein anderer sichtbarer Weg erlaubt werden soll (z. B. Gemini-Canvas); nicht geprüft.
- Nachtest von A mit neuem Skill-Stand auf Gemini.

## Nachtrag: Recherche und Prototyp (13.11.2026 abends)

**Sichtbare Wege laut offiziellen Hilfeseiten:**
- Claude: Eigene Visualisierungen im Chat nur auf Web und Desktop, in den Apps für iOS und Android nur Text ([Anthropic](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork)). Skills setzen Code-Ausführung voraus ([Anthropic](https://support.claude.com/en/articles/12512180-use-skills-in-claude)); Code-Ausführung und Dateien gibt es auch mobil ([Anthropic](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)).
- ChatGPT: Python im Jupyter-Umfeld erzeugt statische Diagramme als Bild ([OpenAI](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)); Code Interpreter auch in der Mobil-App ([OpenAI](https://developers.openai.com/api/docs/guides/tools-code-interpreter)).
- Gemini: Canvas erzeugt HTML und zeigt es über „Vorschau“, auch auf Android und iOS ([Google](https://support.google.com/gemini/answer/16047321?hl=en&co=GENIE.Platform%3DAndroid)); Vorschau laut Nutzerberichten nicht immer zuverlässig.

**Fachbegriff und Regeln:** Freikörperbild (Freischneiden), Lageplan getrennt; ein Körper, alle äußeren Kräfte, unbekannte mit angenommener Richtung, Angriffspunkt je Konvention (Physik: Massenpunkt üblich; Technische Mechanik: Kontaktpunkt, Gewicht im Schwerpunkt).

**Prototyp:** Klotz ruhend auf schiefer Ebene (30°) als SVG aus berechneten Koordinaten (Python), mit Playwright gerendert. Erster Versuch: Klotz steckte in der Ebene, F_G-Beschriftung abgeschnitten, Indizes als „_“. Zweiter Versuch geometrisch richtig, aber Haftreibung hangabwärts (physikalisch falsch für einen ruhenden Klotz). Dritter Versuch korrekt: F_G senkrecht am Schwerpunkt, F_N senkrecht zur Ebene am Kontaktpunkt, F_H hangaufwärts, Winkelbogen, Koordinatensystem; etwa 1 700 Zeichen SVG. Folge: Regeln „Lage aus der Geometrie berechnen“, „Richtungen physikalisch prüfen“ und „Endbild prüfen“ in `skizze.md`.
