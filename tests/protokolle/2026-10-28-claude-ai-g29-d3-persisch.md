# Protokoll: Claude Skill auf claude.ai, 2026-10-28

Native Prüfung der Akzeptanzfälle G29 (`[fa] erklär`) und D3 (Rechts-nach-links) nach dem Wechsel von Urdu zu Persisch, dazu Beobachtungen aus einer zweiten Unterhaltung auf Deutsch. **Kein vollständiger Release-Gate-Lauf.**

| Feld | Wert |
|---|---|
| Oberfläche | Claude Skill auf claude.ai (Aufruf mit `/tutor`) |
| Installationsart / Plattformversion | `tutor-skill.zip` hochgeladen |
| Pluginversion / Marketplace | – |
| Modell (genauer Name) | in den geteilten Unterhaltungen nicht angegeben |
| Datum | 2026-10-28 |
| Commit des geprüften Stands | `cf246ab` (Tag `v0.3.0-rc.4`); die Hilfekarte beider Unterhaltungen nennt `[fa] Persisch`, also den neuen Stand |
| SHA-256 des hochgeladenen ZIP | laut Release `SHA256SUMS.txt`; nicht am hochgeladenen Exemplar nachgeprüft |
| SHA-256 natives Paket | – |
| Durchführung | Lernender (Eingaben), Bewertung durch Claude Code anhand des Seitentexts und der Darstellung der geteilten Unterhaltungen; Endurteil beim Lernenden |

**Abweichung von der Vorlage:** Die Antworten stehen nicht wörtlich hier, sondern in den geteilten Unterhaltungen. Schreibrichtung und Zeichen wurden in der geteilten Seite mit dem Browser gemessen (berechnete CSS-Richtung je Absatz, Zeichenzählung).

## Übersicht

| Fall | Unterhaltung | Urteil | Kurzbefund |
|---|---|---|---|
| G29 | [1](https://claude.ai/share/17b2f14d-ba41-45a3-8105-3a998a4f9b23) #3 | bestanden mit Anmerkungen | Persischer Text, deutsche Überschriften und Aufgabentext, Formeln als eigene Zeilen, Fachbegriffe deutsch in Klammern, Begriffstabelle; aber persische Ziffern und 🔒 vor ➡️ |
| D3 | [1](https://claude.ai/share/17b2f14d-ba41-45a3-8105-3a998a4f9b23) #3, #4, #5 | bestanden mit Anmerkung | 33 persische Absätze rechts nach links, keine Formel im persischen Satz; Zeilen mit deutschem Anfangswort laufen links nach rechts |
| – | [2](https://claude.ai/share/d8609e78-5607-4069-8884-91b6fb1a67ed) #2 | Befund | „📋 Gegeben / Gesucht“ als Codeblock statt Tabelle |

## Fälle

### G29 – `fa erklär` nach Aufgabenfoto, Flächennachweis mit x und y

- **Eingabe:** Foto (Folie 6, drei Quadrate, A₁ = x(2y + x), A₂ = x² + y², A₃ = ½ (x + y)²), erst `erklär` auf Deutsch, dann `fa erklär`.
- **Antwort:** Unterhaltung 1, Nachricht 3.
- **Urteil:** bestanden mit Anmerkungen.
- **Belege:** Statuszeile „Sprache: Persisch (fa)“. Abschnittsüberschriften und Aufgabentext Deutsch, Spalte „Bedeutung“ Persisch. Erklärbogen vollständig (Bild Blech, Grenze, Kernsatz, Brückensatz). Fachbegriffe beim ersten Auftreten mit deutschem Begriff in Klammern, z. B. مثلث قائم‌الزاویه (rechtwinkliges Dreieck); Abschnitt „📚 Fachbegriffe“ mit sieben Begriffen. Gesetzesnamen Deutsch („Flächeninhalt eines Quadrats“). Keine Lösung der Originalaufgabe. Persische Schreibregel eingehalten: in den persischen Absätzen 287 × ی und 150 × ک, kein arabisches ي oder ك, 114 Halbabstände (ZWNJ).
- **Anmerkungen:**
  1. **Persische Ziffern:** Nummerierung und Zeitangaben stehen als ۱، ۲، ۱۰ تا ۱۵ (18 Absätze und Zellen in #3 und #4), obwohl `sprache.md` lateinische Ziffern verlangt. Die arabische Antwort derselben Unterhaltung (#5) schreibt 1, 2, 2 bis 3.
  2. **Reihenfolge:** „🔒 Lösungen“ steht vor „➡️ Nächster Schritt“; die Vorlage verlangt 18 vor 19. Gleich in #2 (Deutsch), #4 und #5. Unterhaltung 2 hält die Reihenfolge ein.
  3. **Signal ohne Klammern:** `fa erklär` und später `ar` wurden als Sprachwunsch erkannt. Die Signaltabelle nennt nur `[fa]`, `!sprache fa` und Wortsignale; das Verhalten ist sinnvoll, aber nicht festgelegt.

### Zusatz G29 – `voll` auf Persisch, dann `ar`

- **Antwort:** Unterhaltung 1, Nachricht 4 (Persisch) und 5 (Arabisch, Modus `voll` beibehalten).
- **Belege:** Anderes Beispiel (Rechteck 3c × 2c), Rechnung geprüft: weiße Dreiecke ½ c² + c² + ½ c² + c² = 3 c², grau 6 c² − 3 c² = 3 c², für c = 2 cm 12 cm². Originalaufgabe nicht gelöst.
- **Anmerkung:** Die persische „Probe“ enthält einen abgebrochenen Satz, der auf einen nicht genannten „bekannten Satz“ verweist („… (فقط برای همین چیدمان) —“). Die arabische Fassung ersetzt ihn durch eine saubere Einzelrechnung für c = 1.

### D3 – Rechts-nach-links

- **Messung in Unterhaltung 1:** 47 Absätze, Listenpunkte und Tabellenzellen mit persischem Text; 33 laufen rechts nach links. Links nach rechts laufen die Tabellenzellen (Tabelle als Ganzes links nach rechts) und Zeilen, die mit einem deutschen Wort beginnen: „➡️ Nächster Schritt: …“, „Probe: …“, „Erste binomische Formel – …“. Keine Formel steht in einem persischen Absatz; alle Gleichungen sind eigene Zeilen.
- **Urteil:** bestanden mit Anmerkung. claude.ai legt die Richtung nach dem ersten Wort fest; Mischzeilen mit deutschem Anfang sind deshalb links ausgerichtet. Das gilt genauso für Arabisch.

### Unterhaltung 2 – `erklär` und `skizze` auf Deutsch, Arbeit an einer Skulptur

- **Antwort:** Unterhaltung 2, Nachricht 2 und 3.
- **Befund Tabelle:** „📋 Gegeben / Gesucht“ steht als Codeblock mit senkrechten Strichen in Festbreitenschrift, nicht als Tabelle. In Unterhaltung 1 erscheint derselbe Abschnitt als Tabelle. Ursache vermutlich `antwortvorlage.md` Abschnitt 2: „Tabelle als reiner Text: Symbol | Bedeutung | Wert | Einheit“. „Reiner Text“ ist dort als „ohne LaTeX“ gemeint (LaTeX-Regel 8), lässt sich aber als „Text ohne Tabellenformat“ lesen.
- **Sonst:** Reihenfolge ➡️ vor 🔒 eingehalten. Annahme zum Winkel (zur Horizontalen) als ⚠ markiert. Skizze zeigt nur Gegebenes (m, F, α, s), keine berechneten Größen; die Annahme Ziehen statt Schieben ist offen genannt.

## Vorschläge (nicht umgesetzt)

1. `antwortvorlage.md`, Abschnitt 2: „Markdown-Tabelle mit Kopf- und Trennzeile, Zellen ohne LaTeX, nie als Codeblock“.
2. `sprache.md`: bei Persisch und Arabisch ausdrücklich „lateinische Ziffern 0–9, keine ۰–۹ oder ٠–٩“.
3. Reihenfolge ➡️ vor 🔒 prüfen: in vier von fünf Antworten mit beiden Abschnitten vertauscht; eventuell in der Schutzprüfung vor dem Senden nennen.
4. Entscheiden, ob blanke Codes (`fa`, `ar`) als Sprachsignal gelten sollen, und dann in der Signaltabelle festhalten.
