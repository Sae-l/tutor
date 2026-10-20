# Lernwissenschaftliche Grundlagen und Aussagegrenzen

Stand: 2026-10-16 · Forschungsnotiz, keine Produktfreigabe und kein Studienergebnis.

Kontext: [Research: Lernwissenschaftliche Grundlagen und Aussagegrenzen bewerten](https://github.com/Sae-l/tutor/issues/36), Teil der [Wayfinder-Karte](https://github.com/Sae-l/tutor/issues/33). Untersuchte Codebasis: [`main` bei `122a7f9`](https://github.com/Sae-l/tutor/tree/122a7f960b85328bfd8cba7804c34079c4b8bfa5). Die spätere Entscheidung über öffentliche Aussagen und das Versuchsprotokoll bleibt offen.

## Ergebnis für die Planung

Die vorhandene Literatur liefert Gründe für aktiven Abruf, eigene Erklärungen, geeignete Beispiele und spätere Wiederholung. Daraus folgt keine Wirksamkeitsbescheinigung für diesen Tutor. Ein erzeugter Denkpunkt belegt eine Texteigenschaft; erst die tatsächlich selbst erarbeitete Antwort zeigt eine Lernhandlung. Ob daraus später selbstständiges Können entsteht, muss unabhängig geprüft werden.

Die entscheidenden Übertragungen sind derzeit Hypothesen: eine selbst gewählte Modusfolge als Fading, eine Wiederholung nach genau zwei Tagen, die Schutzwirkung reiner Promptregeln und die Gleichwertigkeit auf drei Plattformen. Für klinische Aussagen oder eine spezifische Wirksamkeit bei ADHS wurde hier keine Evidenz geprüft. In den untersuchten Projektquellen liegt kein eigener kontrollierter Wirksamkeitsnachweis für Tutor vor.

Technische Abnahme auf Claude, ChatGPT und Gemini und eine spätere Lernstudie benötigen getrennte Ergebnisse. Auch drei technisch bestandene Plattformprüfungen wären kein Nachweis verbesserten Lernens.

## Umfang und Prüftiefe

Gezielte Prüfung der bereits in `docs/KONZEPT.md`, `Obsidian-tutor/04 Wissenschaftliche Grundlagen.md` und `CLAUDE.md` genannten Literatur. Keine systematische Suche, keine Metaanalyse, keine vollständige Lektüre aller Arbeiten, keine Neuauswertung ihrer Rohdaten und keine Durchführung eines Experiments.

Geprüfte Regeln: `tutor/SKILL.md`, `tutor/references/didaktik.md`, `tutor/modes/voll.md` und `tutor/modes/check.md`. Die Zuordnung unten beschreibt deren Anforderungen im Quelltext; sie bestätigt keine tatsächlich beobachtete Regeltreue eines Modells.

Zugriffsstand dieser Recherche:

| Zugang | Tatsächlich geprüfte Inhalte |
|---|---|
| Abrufbarer Originaltext | Roediger/Karpicke: Abstract, Methoden und zentrale Ergebnisse; Chi 1994: Abstract, Methoden und ausgewählte Ergebnisstellen; Bastani: Autorenfassung, Versuchsaufbau, Tabelle 1 und Ergebnisinterpretation; Kestin: Verlagsvolltext, Methoden, Ergebnisse und Grenzen. Keine vollständige Prüfung aller Anhänge. |
| Verlagsabstract oder indexierter Originalauszug | Dunlosky: Verlagszusammenfassung und Nutzenbewertungen; Chi 1989: Verlagsabstract; Kalyuga und Renkl/Atkinson: indexierte Verlagsabstracts. Direkter Taylor-&-Francis-Abruf scheiterte mit HTTP 403. |
| Begrenzter Originalzugang | Cepeda: indexierter Auszug der Autorenfassung; direkter PDF-Abruf scheiterte. Sweller/Cooper: Publikationsdaten und kurzer indexierter Verlagsauszug; vollständige Methoden und Ergebnisdetails nicht geprüft. |
| Originalartikel nicht zugänglich | Slamecka/Graf: DOI und Titel bestätigt, APA-Zugang durch robots.txt gesperrt. Inhaltlich nur Slameckas eigener Rückblick von 1992 verwendet; dieser ersetzt den Originalartikel nicht. Stichprobe und Einzelexperimente bleiben ungeprüft. |

Suchauszüge stammen, soweit inhaltlich verwendet, aus Verlagsseiten oder Autorenfassungen. Sekundäre Presseartikel, Blogs und Suchmaschinenzusammenfassungen dienen nicht als Ergebnisbeleg. Online-Digitalisierungsdaten von 2009/2010 werden nicht mit den ursprünglichen Erscheinungsjahren 1985/2003 verwechselt.

## Was die einzelnen Arbeiten tragen

Die folgenden Einordnungen sind keine neue Evidenzhierarchie. Sie halten Design, Gegenstand und Grenzen auseinander; pauschale Bewertungen wie „stark“ werden daraus nicht automatisch übernommen.

| Quelle | Design, Population und Ergebnis innerhalb des geprüften Zugangs | Grenze der Übertragung auf Tutor |
|---|---|---|
| [Dunlosky et al. 2013](https://doi.org/10.1177/1529100612453266) | Forschungsübersicht zu zehn Lerntechniken, keine einzelne Produktstudie. Übungstests und verteiltes Lernen erhalten hohe, Selbsterklärung eine mittlere Nutzenbewertung. Berücksichtigt werden unterschiedliche Materialien, Altersgruppen, Lernbedingungen und Zieltests. | Die Bewertungen gelten für Techniken unter ihren Bedingungen. Sie bewerten weder diesen Skill noch jede automatisch erzeugte Frage. „Mittlerer Nutzen“ bedeutet keine generelle Nutzlosigkeit; auch „geringer Nutzen“ ist keine Aussage, Wiederlesen sei immer wirkungslos. |
| [Roediger & Karpicke 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x) | Zwei Experimente mit 120 beziehungsweise 180 Studierenden, 18–24 Jahre, an der Washington University. Kurze Sachtexte wurden erneut gelesen oder ohne Feedback frei abgerufen. Wiederlesen war nach fünf Minuten besser; Abruf war bei verzögerten Tests nach zwei Tagen beziehungsweise einer Woche überlegen. | Freier Textabruf ist keine mehrschrittige Physikrechnung. Ein sofort richtiger Chatbeitrag ersetzt keinen verzögerten Test. Der Befund begründet einen Abrufversuch vor dem Anzeigen der Antwort, nicht eine garantierte Verbesserung jeder MINT-Leistung. Originalartikel: [Hochschulablage](https://www.hendrix.edu/uploadedFiles/Academics/Faculty_Resources/Faculty_Development_Newsletters/Testing%20effect.pdf), besonders S. 250–253. |
| [Chi et al. 1989](https://doi.org/10.1207/s15516709cog1302_1) | Analyse von Lautdenkprotokollen beim Lernen aus ausgearbeiteten Mechanikbeispielen und anschließendem Problemlösen. Erfolgreichere Lernende erzeugten mehr prinzipienbezogene Erklärungen und waren weniger von Beispielen abhängig. Der Verlagsabstract beschreibt Gruppenunterschiede; er belegt keine randomisierte Zuweisung zu „guten“ und „schlechten“ Lernenden. | Zusammenhang und Intervention auseinanderhalten. Wenn das Modell jeden Schritt selbst erklärt, erklärt sich der Lernende dadurch noch nichts selbst. Der [Autoren-PDF-Scan](https://education.asu.edu/sites/g/files/litvpz656/files/lcl/chibassoklewisreimannglaser_0.pdf) war abrufbar, ließ sich hier aber nicht als Text auswerten; seine Methoden wurden nicht vollständig nachgeprüft. |
| [Chi, de Leeuw, Chiu & LaVancher 1994](https://doi.org/10.1207/s15516709cog1803_3) | Vergleich von 14 Achtklässlern mit Aufforderungen zur Selbsterklärung und zehn Kontrollpersonen, die denselben Text zum menschlichen Kreislauf zweimal lasen. Vor- und Nachtest; größere Lernzuwächse bei den aufgeforderten Lernenden, einschließlich anspruchsvoller Verständnisfragen. | Kleine Stichprobe, Biologietext statt Hochschulaufgaben im Chat. Der Befund zu angeleiteten Erklärungen ergänzt den beobachtenden Ansatz von 1989. Keine Plattform-, Langzeit- oder ADHS-Validierung für Tutor. [Autorenfassung](https://education.asu.edu/sites/g/files/litvpz656/files/lcl/chideleeuwchiulavancher_3.pdf). |
| [Cepeda et al. 2006](https://doi.org/10.1037/0033-2909.132.3.354) | Quantitative Übersicht zu verbalem Abruf: 839 Bewertungen aus 317 Experimenten in 184 Artikeln. Lernabstand und Zeit bis zum Abschlusstest wirken gemeinsam; der günstigste Abstand hängt vom gewünschten Behaltenszeitraum ab. | Keine einzelne Population und keine Prüfung eines Chat-Wiederholungsplaners. Ein universelles Optimum „nach zwei Tagen“ folgt nicht daraus. Der Transfer auf selbstständiges MINT-Problemlösen bleibt zusätzlich zu prüfen. [Autorenfassung, hier indexierter Auszug](https://laplab.ucsd.edu/articles/Cepeda_etal_2006.pdf). |
| [Sweller & Cooper 1985](https://doi.org/10.1207/s1532690xci0201_3) | Der indexierte Verlagsauszug beschreibt fünf Experimente zu Algebra, kognitiven Repräsentationen und dem Einsatz ausgearbeiteter Beispiele. Vollständige Methoden, Stichprobengrößen und Transferbedingungen wurden wegen der Zugriffsgrenze nicht nachgeprüft. [Verlagseintrag](https://www.tandfonline.com/doi/abs/10.1207/s1532690xci0201_3). | Als ursprünglicher Bezug des Worked-Example-Ansatzes belegbar; ein pauschaler Satz „Anfänger lernen immer mehr als beim eigenen Probieren“ ist damit hier nicht abgesichert. Vor präzisen Effekt- oder Transferbehauptungen Originaltext prüfen. Das andere Beispiel in `voll` ist eine Gestaltungsübertragung. |
| [Kalyuga et al. 2003](https://doi.org/10.1207/S15326985EP3801_4) | Übersicht zur Wechselwirkung von Instruktion und Vorwissen, keine einzelne Studie mit einer Gesamtstichprobe. Für Unerfahrene hilfreiche Instruktionen können bei Erfahrenen ihren Nutzen verlieren oder nachteilig werden. Bewertungsbasis: [Verlagsabstract](https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_4). | „Vollständige Lösungen schaden mit wachsendem Können“ ist zu undifferenziert. Aufgabenschwierigkeit und Vorwissen zählen. Eine Auswahl verschiedener Modi ist noch keine geprüfte Anpassung an Kompetenz. |
| [Renkl & Atkinson 2003](https://doi.org/10.1207/S15326985EP3801_3) | Theoretische Analyse mit zusammengefasster empirischer Unterstützung: Lösungsanteile werden allmählich aus Beispielen entfernt, bis selbstständiges Problemlösen verlangt wird. Keine einzelne, hier vollständig überprüfte Versuchspopulation. Bewertungsbasis: [Verlagsabstract](https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_3). | Die Lernendenfolge `erklär → tipp → voll → kurz` erhöht zunächst Hilfe und endet in einer sichtbaren Lösung. Sie ist kein Nachweis des beschriebenen schrittweisen Ausblendens. Ein eigenes adaptives Fading wäre eine spätere Produktentscheidung. |
| [Slamecka & Graf 1978](https://doi.org/10.1037/0278-7393.4.6.592) | Laut [Slameckas Rückblick von 1992](https://garfield.library.upenn.edu/classics1992/A1992HN61400001.pdf) verglichen fünf Experimente das Gedächtnis für selbst erzeugte und gelesene Wörter. Selbst erzeugte Wörter wurden besser erinnert; der Autor beschreibt zugleich Abhängigkeiten von Material und Versuchsdesign. Originalstichproben hier nicht verifiziert. | Aus Wortgenerierung folgt keine Garantie für selbst erzeugte Rechenwege, Vorhersagen oder mehrsprachige MINT-Erklärungen. Der Denkpunkt ist eine plausible Anwendungsidee. Keine vollständige Neubewertung des Originaleffekts behaupten. |
| [Bastani et al. 2025](https://doi.org/10.1073/pnas.2422633122) | Feldexperiment an einer türkischen weiterführenden Schule, rund 1.000 Lernende der Klassen 9–11, vier Mathematiksitzungen. Vergleich: ohne KI, GPT Base, GPT Tutor mit Schutzvorgaben und aufgabenspezifischen Lehrkraftinformationen. Nach KI-gestütztem Üben lag GPT Base im Test ohne Hilfe rund 17 % relativ unter der Kontrolle, entsprechend 5,4 Prozentpunkten der normierten Skala. GPT Tutor war dort statistisch nicht von der Kontrolle unterscheidbar. [Autorenfassung](https://hamsabastani.github.io/education_llm.pdf), Aufbau und Tabelle 1, PDF-S. 5–10. | Kein Beweis, dass jeder freie Lösungszugriff schadet oder Tutor durch eine Sperrformulierung besseres Lernen erzeugt. Unterschiede umfassen mehrere Komponenten; der isolierte Effekt einer Antwortsperre ist nicht bestimmt. Nichtsignifikanz beweist weder Gleichwertigkeit noch langfristige Unschädlichkeit. |
| [Kestin et al. 2025](https://doi.org/10.1038/s41598-025-97652-6) | Randomisierte Crossover-Studie in Harvard-Einführungsphysik, 194 eingeschlossene Studierende; zwei Themen in aufeinanderfolgenden Wochen. Vergleich des speziell gebauten KI-Systems mit aktivem Präsenzlernen; höhere unmittelbare Nachtestleistung in der KI-Bedingung. Die Plattform nutzte unter anderem schrittweise Aufgabenführung und vorgegebene Lösungen. [Verlagsvolltext](https://www.nature.com/articles/s41598-025-97652-6), Methods sowie Context, limitations, and future directions. | Kein Vergleich eines beliebigen Skill-Prompts mit Unterricht. Das Maßnahmenbündel isoliert den Prompt nicht. Kein hier berichteter langfristiger Retentionsnachweis; keine allgemeine Überlegenheit auf anderen Fächern, Aufgaben oder Plattformen. Die dort benannte Unzuverlässigkeit reiner Promptsteuerung ist für Tutor eine Prüfaufgabe. |

Vollständige bibliografische Angaben stehen in den verlinkten Verlagsdatensätzen und der vorhandenen Vault-Bibliografie. Die bisher unvollständige Angabe „Chi 1994“ lässt sich konkretisieren als *Eliciting Self-Explanations Improves Understanding*, Cognitive Science, 18(3), 439–477. Die Zugriffsgrenzen bei den älteren Arbeiten werden durch vorhandene DOI-Angaben nicht aufgehoben.

## Evidenz → bestehende Regel → beobachtbarer Test

Die Tests in dieser Tabelle sind Vorschläge für spätere Prüfungen. Sie wurden hier nicht ausgeführt. Eine technische Beobachtung prüft die beabsichtigte Gelegenheit zum Lernen; die letzte Spalte braucht tatsächliche Lernhandlungen oder unabhängige Aufgabenbearbeitung.

| Forschungsbezug | Regel in der aktuellen Quelle | Beobachtbare technische Prüfung | Davon getrennte Lernbeobachtung |
|---|---|---|---|
| Dunlosky; Roediger/Karpicke | Verständnisfrage vor dem nächsten Schritt; Antwort nur auf Abruf (`didaktik.md`, `SKILL.md`). | Frage ist beantwortbar, verrät kein Originalergebnis; die Antwort fehlt bis zum zulässigen Abruf auch in Bildern, Diagrammen und erzeugten Dateien. | Eigene Antwort vor Lösungssicht; späterer Abruf desselben Prinzips ohne Chat. |
| Chi 1989/1994 | Begründungen, Denkpunkte und Prüfung des eigenen Versuchs (`voll.md`, `check.md`). | Frage verlangt einen Grund oder eine Vorhersage; `check` erfindet keinen Fehler und identifiziert den ersten tatsächlichen Fehler. | Lernender begründet einen Schritt selbst und kann seine Begründung in einer neuen Aufgabe anwenden. Eine Begründung des Modells zählt nicht als Selbsterklärung. |
| Sweller/Cooper; Renkl/Atkinson | Anderes vollständig gerechnetes Beispiel in `voll`; danach Originalaufgabe selbst lösen. | Zahlen und Einkleidung unterscheiden sich; keine Originalzwischenwerte; Methode bleibt fachlich passend. | Eigenständiger Lösungsversuch nach dem Beispiel, danach ähnliche Aufgabe ohne Beispiel. Reines Abschreiben separat erkennbar halten. |
| Kalyuga; Renkl/Atkinson | Mehrere vom Lernenden wählbare Hilfestufen. | Moduswechsel funktionieren; Beschreibung behauptet keine automatische Kompetenzdiagnose. | Bedarf an Hinweisen bei vergleichbaren Aufgaben und Vorwissen beobachten. Eine abnehmende Hintzahl allein beweist keinen Lernerfolg. |
| Cepeda | Wiederholungskarte mit späterem Zeitpunkt (`voll.md`, Antwortvorlage). | Karte enthält eine konkrete Abrufaufgabe, keinen behaupteten universell optimalen Zeitabstand und kein Versprechen automatischer Erinnerung. | Tatsächliche Wiederholung und Leistung nach dokumentiertem Abstand. Eine ausgegebene Karte zählt nicht als absolvierte Wiederholung. |
| Slamecka/Graf, indirekter Bezug | Vorhersage vor dem Weiterlesen (Denkpunkte in `voll`). | Aufforderung erscheint vor dem zugehörigen Schritt. Ein Pausensymbol wird nicht als technisch erzwungene Pause beschrieben. | Vorhersage wird vor dem Aufdecken festgehalten; keine Gleichsetzung mit dem ursprünglichen Wortgedächtnisexperiment. |
| Bastani; Kestin | Lösungsschutz und geführte Hilfen. | Regressionsfälle für unbeabsichtigten Lösungsverrat über alle Ausgabekanäle; fachlich richtige Hilfen, zulässiger Abruf und lösende Modi separat testen. | Übungsleistung mit Hilfe und Leistung ohne Hilfe getrennt auswerten; subjektive Zufriedenheit nur ergänzend. |

Die aktuellen Regeln erlauben sichtbare Lösungen in `kurz`, `mittel`, `lang` und `klausur`; `lösung` ist ein ausdrücklicher Abruf. Der Schutz verhindert nach seinem Zweck unbeabsichtigte Preisgabe in geschützten Modi. Er verhindert keine bewusste Wahl eines lösenden Modus und erzwingt keine Lernhandlung. Auch ein formal anderer Zahlenwert im Beispiel genügt didaktisch nicht, wenn der Lernende das Original ohne Verstehen direkt einsetzen kann.

## Präzisierungen für eine spätere Dokumentationsentscheidung

Diese Recherche ändert keine Produktdateien. Folgende Formulierungen sollten im späteren HITL-Ticket entschieden und anschließend konsistent durch Quellen, generierte Hüllen, Website und Vault gezogen werden:

| Aktuelle Aussage oder Annahme | Forschungsseitige Grenze und mögliche präzisere Aussage |
|---|---|
| `didaktik.md`: „Freier Zugriff auf fertige Lösungen verbessert das Üben, verschlechtert aber nachweislich das spätere Ergebnis ohne Hilfe.“ | Unzulässig breit. Vorschlag: „Unbeschränkte KI-Hilfe kann Übungsleistung und späteres selbstständiges Können auseinanderfallen lassen. Deshalb fördern wir eigene Versuche und prüfen Leistung ohne Hilfe.“ Quelle und Kontext ergänzen; keine universelle Schadensregel. |
| `KONZEPT.md`: pauschale Evidenzspalten und Anfänger-/Expertensatz | Quelle, Population und Übertragungsgrenze statt ungeprüfter Stärkeskala. Geeignete Beispiele können Anleitung bieten; ihr Nutzen hängt von Vorwissen und Aufgabe ab. |
| `KONZEPT.md`: „reines Lesen von Lösungen, laut Forschung der schwächsten Lernform“ | Keine hier geprüfte Quelle begründet diese universelle Rangfolge. Sinnvolle Beispiele und passives Abschreiben unterscheiden. |
| Eskalation wird mit „Expertise-Reversal / Fading“ zusammengeführt | Freiwillige Hilfeauswahl beschreiben. Kein automatisches Fading und keine Kompetenzmessung behaupten. |
| Wiederholung „nach zwei Tagen“ | Als praktikablen Vorschlag kennzeichnen; tatsächlichen Abstand erfassen. Kein individuelles Optimum behaupten. |
| ADHS-freundliche Gestaltung | Als Gestaltung mit kurzen, wiedererkennbaren Schritten beschreiben. Keine klinische Behandlung, Diagnostik oder nachgewiesene ADHS-spezifische Lernwirkung ableiten. |
| Bezug auf KI-Tutor-RCTs | Wissenschaftlich angeregte Gestaltung benennen. Ergebnisse fremder, umfangreicherer Systeme weder als Tutor-Ergebnis noch als Drei-Plattform-Freigabe ausgeben. |

Pólya, sokratisches Fragen, „Feynman-Technik“, Fehlkonzeptarbeit und UDL sind weitere im Konzept genannte Bezüge. Für daraus abgeleitete konkrete Wirksamkeits-, Überlegenheits- oder klinische Aussagen fehlt in dieser begrenzten Prüfung eine eigene Bewertung. Sie werden nicht nachträglich als empirisch validiert eingestuft.

## Optionen für einen späteren begrenzten Lernversuch

Das Folgende ist ein Protokollentwurf zur Entscheidung, kein freigegebener oder gestarteter Versuch. Keine Teilnehmenden anwerben und keine Lern-, Chat- oder Gesundheitsdaten für dieses Forschungsticket erheben.

### Zuerst die Fragestellung wählen

1. **Machbarkeit:** Verstehen Lernende die Bedienung, entstehen eigene Versuche, funktionieren die Testaufgaben? Eine einzelne freiwillige Erprobung kann Ablaufprobleme aufdecken. Sie trägt keinen kausalen Wirksamkeits- oder Gruppenvergleich.
2. **Lernwirkung des Gesamtpakets:** Unterstützt ein festgelegter Tutor-Stand späteres selbstständiges Problemlösen gegenüber einer klar beschriebenen vorhandenen Lernhilfe? Randomisierte Gruppen oder ein gegenbalancierter Wechsel über vergleichbare Themen wären Optionen. Ein Wechsel ist kleiner organisierbar, aber Übertragung zwischen Themen und Reihenfolge können ihn verzerren.
3. **Wirkung einer einzelnen Regel:** Erzeugt beispielsweise eine Abrufaufforderung einen Unterschied? Dafür müsste bei sonst gleichen Bedingungen genau diese Komponente variiert werden. Ein Gesamtpaketvergleich beantwortet diese Frage nicht. Kein absichtliches Brechen des bestehenden Lösungsschutzes ohne gesonderte Entscheidung.

Die erste Option eignet sich zur Vorbereitung. Ob danach ein Gruppenversuch sinnvoll ist, welche Vergleichshilfe fair ist und welches Ergebnis praktisch relevant wäre, muss vor Beginn entschieden werden. Keine willkürliche kleine Stichprobe als hinreichend für einen Wirksamkeitsnachweis ausgeben; nötige Fallzahl und Auswertung hängen von Zielgröße, Vergleich und gewünschter Präzision ab.

### Messfolge und Grenzen

| Zeitpunkt | Kleine mögliche Messung | Worauf vor Beginn festlegen? |
|---|---|---|
| Vortest ohne KI | Wenige Aufgaben zu Ausgangswissen und Zielprinzipien; Rechenweg und Begründung. | Passende Schwierigkeit, Zeit, erlaubte Hilfsmittel, Bewertung. Kein Training an den später identisch verwendeten Testaufgaben. |
| Lernphase | Festgelegte Aufgaben mit Tutor oder Vergleichshilfe; verfügbare Zeit gleich begrenzen oder Zeitunterschiede ausdrücklich zum Untersuchungsgegenstand machen. | Paket-Commit/Hash, Plattform, Modellbezeichnung, Datum, Modus, Werkzeuge und Hilfen. Aufgaben und Rückmeldungen fachlich vorprüfen. |
| Unmittelbarer Nachtest ohne KI | Neue, vergleichbare Aufgaben: Ansatz, Schritte, Ergebnis und Begründung bewerten. | Primäre Zielgröße vorher benennen; keine Bewertung nur nach Endzahl. Testaufgaben nicht an das Modell der Lernphase geben. |
| Verzögerter Test ohne KI | Beispielsweise nach einer Woche, mit Parallelaufgaben und tatsächlichem Zeitabstand. | Zeitraum ist eine organisatorische Option, kein aus den Studien bestimmtes Optimum. Zwischenzeitliches Lernen kurz erfassen; Ausfälle berichten. |
| Transfer | Aufgabe mit anderer Oberfläche beziehungsweise geändertem gesuchten Zusammenhang, die das gelernte Prinzip braucht. | Definieren, was daran neu ist. Zahlenersatz allein nicht als weitreichenden Transfer ausgeben. Ergebnisse zu naher und weiter entfernten Anwendung trennen. |

Der unmittelbare Nachtest ist selbst eine Abrufübung und kann die spätere Leistung beeinflussen. Bei gleichem Ablauf in beiden Bedingungen ist dieser Einfluss Teil des Versuchs; der verzögerte Wert misst dann Behalten nach Unterricht **und** erstem Test. Für eine isolierte Frage nach Testwirkung wäre ein anderes Design nötig.

Vorab Aufgaben und Bewertungsrubrik festschreiben; Testfragen möglichst unabhängig von der Tutor-Erstellung prüfen lassen. Wenn möglich, Arbeiten ohne Kenntnis der Bedingung bewerten. Zeit, Fehlerarten, Lösungssicht vor dem eigenen Versuch und fehlende Tests dokumentieren. Explorative Nebenbefunde als solche ausweisen; Unsicherheit und Größenordnung berichten, nicht nur Signifikanz oder Zufriedenheit.

Ein Vergleich auf drei Plattformen wäre ein eigener Faktor und vergrößert den nötigen Aufwand. Die technische Abnahme kann zunächst für jede Plattform dieselben Kernfälle prüfen. Für einen kleinen Lernversuch einen genau benannten Stand festhalten; dessen Lernresultat nicht still auf die anderen Modelle übertragen. Modelländerungen während der Erhebung gesondert behandeln.

### Daten und Abbruch

Ein späterer Ablauf braucht eine verständliche Zustimmung, freiwillige Teilnahme, festgelegte Verantwortlichkeit, Speicherort, Löschfrist und gegebenenfalls die Prüfung durch die zuständige Einrichtung. Das ist hier nur als Planungspunkt benannt, keine rechtliche Freigabe. Zur Fragestellung sind keine Diagnose-, Gesundheits-, Klarnamen- oder Kontodaten nötig. Öffentliche Berichte enthalten nur ausreichend aggregierte Ergebnisse; keine persönlichen Chats, Arbeitsblätter mit Identifikatoren oder Kontoverknüpfungen. Rohdialoge nur erfassen, wenn die gewählte Frage sie erfordert und dies gesondert geklärt wurde.

Bei fachlich falscher Hilfestellung, unbeabsichtigter Lösungsoffenlegung in einem geschützten Modus oder technischen Ausfällen: Ereignis nach dem vorab definierten Verfahren dokumentieren, die betroffene Lernphase unterbrechen und Unterstützung anbieten. Ausschluss- und Wiederholungsregeln vor der Erhebung bestimmen; Fehler nicht nachträglich aus dem Erfolgsbericht entfernen.

## Offene Entscheidungen für die Karte

- Welche öffentlichen Formulierungen werden übernommen, und welche unbelegten Verallgemeinerungen werden ersetzt?
- Soll der erste Versuch ausschließlich die Machbarkeit prüfen, oder ist bereits ein ausreichend vorbereiteter Vergleich möglich?
- Welche Zielgruppe, welches einzelne Themenfeld, welche Vergleichshilfe und welche vorab definierte unabhängige Zielgröße passen zur beabsichtigten Aussage?
- Wer prüft die Aufgaben, das Protokoll und den datensparsamen Ablauf, bevor tatsächlich Personen teilnehmen?
- Welche älteren Volltexte sind vor weitergehenden Effektbehauptungen noch einzusehen, insbesondere Sweller/Cooper und Slamecka/Graf?

Diese Fragen bleiben Entscheidungen mit menschlicher Beteiligung. Die vorliegende Recherche klärt Quellenlage und Grenzen; sie implementiert keine Regeländerung und erteilt keine Veröffentlichung einer Wirksamkeitsbehauptung.
