# LaTeX- und Formatregeln

Diese Regeln stammen aus echten Darstellungsfehlern in der Claude-App und in ChatGPT bei arabischem Text. Sie gelten für jede Antwort dieses Skills.

## Warum
- `\[ ... \]` und `\( ... \)` werden in der Claude-App nicht zuverlässig gerendert: Der Backslash geht verloren, übrig bleiben `[`, `]` und roher Code.
- Inline-Formeln in arabischen Sätzen werden durch die Rechts-nach-links-Richtung umsortiert; Vorzeichen landen auf der falschen Seite.
- Nicht-ASCII-Zeichen wie ß in `\text{}` oder `\mathrm{}` lassen den Renderer scheitern. Das betrifft jede Erklärsprache (Arabisch, Türkisch, Ukrainisch, Französisch, Deutsch).

## Regeln
1. Jede Formel steht zwischen `$$ ... $$` in einer eigenen Zeile, mit Leerzeile davor und danach.
2. Niemals `\[ \]`, `\( \)` oder einfaches `$` verwenden.
3. Im Fließtext kein LaTeX. Einzelne Symbole als normale lateinische Buchstaben schreiben (x, U0, R). Alles mit +, −, = oder einem Bruch kommt in eine eigene $$-Zeile.
4. In LaTeX nur ASCII: keine arabischen oder kyrillischen Buchstaben, kein ß ä ö ü, kein ç ğ ı ş, kein é è à, keine ganzen Wörter in irgendeiner Sprache. Text-Indizes als kurzer lateinischer Buchstabe: A_\mathrm{w}; die Bedeutung im Text erklären („A_w: Fläche der weißen Dreiecke“).
5. Brüche immer mit vollen Klammern: \frac{1}{2}, nie \frac12. Klammern immer ausgeglichen.
6. Endergebnis: \boxed{...} innerhalb von $$ ... $$.
7. DIN 1338 / ISO 80000: Einheit aufrecht mit \mathrm{}, kleines Leerzeichen \, vor der Einheit, Dezimalkomma als {,}.
8. Tabellen enthalten kein LaTeX, nur reinen Text: U0 | 3,5 | V.

## Richtig

$$U = 3{,}5\,\mathrm{V}, \qquad R = \frac{U}{I} \approx 292\,\Omega$$

$$A_\mathrm{w} = 2 \cdot \frac{1}{2}\, y^2 = y^2$$

## Falsch (so ist es kaputtgegangen)

- `\[ A_\mathrm{weiß} = 2 \cdot \frac{1}{2} y^2 \]` → Klammern sichtbar, ß bricht ab.
- `كل مثلث مساحته \(\frac{1}{2}y^2\)` → Rohcode im Satz.
- `يختزل الحدّان +2xy و −2xy` mit Inline-Formel → Vorzeichen vertauscht. Stattdessen:

$$+2xy - 2xy = 0$$

## Letzter Check vor dem Senden
- Kein `\[`, `\(` oder einzelnes `$` im Text?
- Kein ß ä ö ü oder arabisches Zeichen zwischen `$$`?
- Jede `$$`-Zeile hat ausgeglichene Klammern?
