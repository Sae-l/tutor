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
