# Indeling hints-batches G4 (Oefeningen, 1 okt 2026 14:45, stand build 14:34: 94 somtypes, 2.175 items)
Regel: ongeveer 22 somtypes per batch, een bestand wordt nooit gesplitst, GET-M01 (23 somtypes) is zelf een batch.
Na de build van 14:31 kwamen er somtypes bij (GET-E09 #4, MEET-E07 #1, MKU-E03 #1–#2, VBN-E01 #4–#5); de indeling is daarop aangepast.

| batch | bestanden | somtypes | items | status |
|---|---|---|---|---|
| batch1 | GET-E02, E03, E04, E05, E06, E07, E08, E09 | 24 | 613 | klaar, review-batch1.md; review Didactiek v1 verwerkt (14:49), review-batch1b.md |
| batch2 | GET-M01 | 23 | 602 | klaar (14:49), review-batch2.md |
| batch3 | GET-M02, M05, M06, MEET-E01, E02, E05, E07, MKU-E01, E02, E03, E04, E05 | 24 | 448 | klaar (15:06); ronde 3b (Didactiek b3 v1) 15:30, review-batch3b.md; review-batch3.md · twijfels: hints/batch3_twijfels.md · fixlijst #25–33 · Claude ok 24 · taalfix 10 · vervangen 16 · nieuw 67 |
| batch4 | MEET-E06, VBN-E01, VERH-E01 | 23 | 510 | klaar (15:36), review-batch4.md · twijfels: hints/batch4_twijfels.md · fixlijst #38–44 · Claude ok 4 · taalfix 0 · vervangen 30 · nieuw 27 |
| batch5 | GET-E05 nrO 2–5 (G8-aanvulling 'naar G4', 8 okt) | 4 | 36 | klaar (8 okt, Oefeningen), review-batch5.md · twijfels: hints/batch5_twijfels.md · fixlijst Oef-#460–#463 · Claude ok 0 · vervangen 3 · nieuw 23 (waarvan 5 vaste tekst op Claude-labels) · nog niet gesynct (volgende build_g4.py) |

## Besluiten Didactiek (besluiten_twijfel.md) en Overzicht (README 'Besluiten Overzicht'): welke somtypes ze raken
Stand build 14:34. Overzicht heeft de opgaven al aangepast (fixes B1–B6 in `logs/fixes.csv`). Hieronder staat wat de **hints** nog moeten doen.

| besluit | somtype (batch) | items | wat de hints moeten doen |
|---|---|---|---|
| Centen zonder komma ('45 cent', '€2'). Uitleg '100 cent is 1 euro.' Zin 'Bij teruggeven …' weg | **MEET-E07 #1** '[geld] Hoeveel [ding] zie je? — met centen' (batch3) | 24 | Geen komma en geen '€1,20' in de hints. Schrijf 'cent' en 'euro' (van 1 tot 2 euro: '1 euro en 20 cent'; die items gingen naar G5-GET-M03). Gebruik nergens 'teruggeven'. Al nagekeken: geen enkele kindtekst in MEET-E07 heeft nog 'teruggeven' (B4, 24 items). Fout-hint 'euro of cent' bij de afleider '40 euro'. Hint-richting: eerst de grote munten, daarna de kleine. Voor de fixlijst bij batch 3: '€2' heeft de afleiders '1 euro en 50 cent' en '€101' (onzin, en boven 100). Verder is er vaak de afleider '3 euro' (het aantal munten): 12 items hebben een optie met 'euro'. |
| Schaal: 'Elk streepje is 2.' boven de vraag. Streepje = 5 gaat naar G5 | **VBN-E01 #4** 'Elk streepje is #. Hoeveel [naam] zijn er?' (42) en **#5** '… meer dan [naam]?' (41) (batch4) | 83 | Hint-richting van Didactiek: 'Zoek het getal vlak onder de staaf. Spring dan verder met 2.' Noem geen getal om de 10 dat bij een ander item het antwoord is (checker). Fout-hints: 'streepjes geteld in plaats van verder gesprongen' (antwoord = de helft), 'één streepje te veel of te weinig' (± 2). VBN-E01 #1–#3 (tabel) zijn niet geraakt. |
| Deelteken ':' naar G5 (G5-GET-M06, 41 items) | geen G4-somtype meer | 0 | Niets in G4. Let op: ':' alleen in 'a : b', nooit in een G4-opgave. In GET-E08 #2 staat 'a : b' nog in `claudeUitleg` (intern, 2 keer). |
| Vlakken uitleggen: 'Een vlak is een platte kant.' Ribben en hoekpunten gaan naar G5 | **MKU-E03 #1** vlakken tellen (3) en **#2** piramide herkennen (1) (batch3) | 4 | Gebruik in de hints alleen 'vlak' of 'platte kant', niet 'ribbe' of 'hoekpunt'. Hint: 'Tel ook de kanten die je niet ziet: achter en onder.' Piramide: 'denk aan een tent met een punt' (Didactiek: goed). Bij de piramide het vierkante grondvlak meetellen. |
| Trap: 'Treden zijn de stapjes van een trap.' | GET-E09 #4 (batch1, klaar) | 1 | Klaar in batch 1. De hint gebruikt 'trappen' en 'treden', en de uitleg staat boven de vraag. |

**Rebuild 15:06 (gezien om 15:08 door Oefeningen).** De sync schreef 'koppeling' in batch1, 2 en 3, en 'kopGewijzigd' in batch1 bij E03 #1, E06 #4, E06 #6, E08 #5, E09 #2 en E09 #3. Batch 3 is daarna in place opnieuw toegepast (apply_hints): 450 items, 0 zonder fout-hint, check_hints 0 FAIL / 0 WARN. make_batch3.py weigert nu te draaien, want batch3.json is gesynct.
Open voor de volgende ronde:
- E06 #6: de regels '5 sets' en '3 sets' moeten '5 manieren' en '3 manieren' worden.
- E08 #5: de vraag zegt nu 'sprongen', de hints zeggen 'stappen'.
- E06 #4: de vraag is nu 'Hoeveel … zijn dat samen?'.
- E08 #2 heeft geen items meer (naar G5).
- Nieuwe regels 'antwoord ± getal1' (E06 #2, E07 #1) en 'eenheden als antwoord' (E02 #2) staan nu in fout_regels.py (15:05).

**Stand 15:36 (Oefeningen).**
- Alle 4 batches zijn klaar. check_hints: 93 klaar, 0 open, 0 FAIL, 2 WARN. De 2 WARN zijn MEET-E05 '(1 kg)', een vals alarm (zie batch4_twijfels punt 8). check_merge_notatie: ALLES OK.
- Ronde 2b staat in review-batch2b.md, ronde 3b in review-batch3b.md.
- VBN-E01 #4/#5 volgt de hint-richting van Didactiek ('vlak onder de top van de staaf', 'spring verder met twee'). 'één streepje te veel/te weinig' = 'antwoord ± getal1'. 'streepjes geteld' heeft nog geen regel (fixlijst #40).

- **Batch 5 ronde 1b (8 okt, Oefeningen):** review-batch5-didactiek (taal: fix) verwerkt in patch_batch5.py: V-#720, V-#721, tientallen-H2 (twijfel 1), Z-#720, Z-#722, Z-#723, Z-#724; check FAIL 0, zie merge-fixlijst.md.
- **Batch 5 ronde 1c (8 okt 15:2x, Oefeningen):** Didactiek taal ok (build 15:08:46). patch_batch5.py ronde 1c: Z-#730 (H1 min), Z-#733 (ouderzin MC); lessen 233–235 als guards (g4work/b5/check.py, runmut.sh 14 mutanten). check_hints 97 klaar · 0 FAIL; tweede patch-run 0.
