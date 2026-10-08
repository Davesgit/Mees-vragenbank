# G7 merge-fixlijst

Aangemaakt door Oefeningen (8 okt 2026) voor G7 hints batch 1. Elk team schrijft in een eigen sectie. Nummering (les 124): Oefeningen Oef-#NNN (eigen reeks onder #500; volgende vrije: Oef-#423), Didactiek #500 en hoger, Overzicht houdt zijn eigen nummers.

## Oefeningen batch 1 (8 okt 2026; build 2026-10-01 22:54:27)
| # | Wie | Wat | Stand |
|---|---|---|---|
| batch 1 | Oefeningen | DENK-02 #1–#14 en DENK-03 nrO 1, 2, 3, 25, 4–10: 25 somtypes, 25 items, 50 sleutels, alle met eigen laag 2. `hints/batch1.json` (eerste versie `make_batch1.py`), patches in `hints/patch_batch1.py`. Review: `review-batch1.md` | ✓ |
| Oef-#421 | **Overzicht (motor)** | Een letterlijke regel met '−' past nooit: `_compile_regel` maakt van '−' in de regel '-', maar de optietekst houdt '−' ('6 − 4', '8 − 5 = 3' in DENK-02 #8/#9: 'LET OP regel niet te lezen'). Nu opgelost met 'Claudes sleutel: verkeerde-bewerking'. Voorstel: vergelijk de letterlijke regel met de optietekst met dezelfde normalisatie (of normaliseer niet bij een letterlijke regel). Zelfde soort als Z-#411 (G6) | open (Overzicht) |
| Oef-#422 | **Overzicht (motor)** | Een letterlijke regel '13 euro' wordt '€13' (fixlijst #32, G4-geld), en past dan niet op de G7-optie '13 euro'. Nu opgelost met alleen het getal ('13', exact als heel getal). Voorstel: lees '€N' ook als 'N euro' bij de vergelijking met de optie | open (Overzicht) |
| G5 MEET-E06 #1 | info | De 220 items van G5 MEET-E06 #1 (dagen tussen twee datums, claude-bank-387 t/m -606) staan in G7: **G7-MEET-04 nrO 7** ('Hoeveel dagen duurt het van # [ding] tot # [ding]?', 220 items, `G7-MEET-04-claude-bank-park-…`). Hints komen in de batch met MEET-04 (basis: G5 batch 5 #1). De G5-entry MEET-E06 nrO 1 staat nog in g5/hints/batch5.json | voor een latere batch |
| #101 | Oefeningen | G7 MEET-03 #1, #2, #9 en #10: symbool + woord in H1. Niet in batch 1 (MEET-03 komt later); staat klaar als eis | voor een latere batch |
| checks | Oefeningen | zandbak: check_hints 25 klaar, 129 open, 0 FAIL, 0 WARN; notatie ALLES OK; BIJNA390 0; `g7work/b1/check.py` FAIL 0; los-scan 0; tweede run 0 wijzigingen | ✓ |


## Ronde 10 (8 okt 2026, Overzicht; Didactiek slotcheck r10 #503)
| # | Wie | Stand |
|---|---|---|
| 'getal uit de vraag' | Oefeningen | open: de geparkeerde G5-MEET-E06 #1 (220 items, dagen tussen twee datums): de entry (batch5 #1) heeft geen regel 'getal uit de vraag'. Na #390 krijgt een sleutel die een getal uit de vraag is geen ±1/'Bijna!' meer en valt hij op 'andere fout' (bijv. G5 gen-001 '24'). Voorstel: een regel 'fout = een getal uit de vraag' (als vraag) vóór ± 1 |

## Oefeningen ronde 1b (8 okt 2026, 12:10–12:30; Didactiek review-batch1-didactiek.md; G7 build 12:00:13 + zandbak), zie `review-batch1b.md`
Nummering: Oefeningen Oef-#NNN onder #500 (volgende vrije: Oef-#427); Didactiek #500+; Overzicht ongewijzigd.
| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#515 | Oefeningen | Verklappers bij meerkeuze: DENK-02 #3 (H2), #4 (H1+H2), #8 (H2), #9 (H2), #10 (H1+H2): teksten van Didactiek. #13 blijft | ✓ `hints/patch_batch1.py` 'Ronde 1b'. `g7work/b1b/verklap.py` (les 144): oud 7 FAIL, nieuw 0 |
| V-#517 | Oefeningen | Vlag 'contextgebonden' (woorden + aanname) in 13 entries; guard in `g7work/b1/check.py` + `g7work/b1b/context.py` (één item, vlagwoord in de opgave, elk contextwoord in de vlag). DENK-02 #2: H1/H2/ALG/ouderzin voor omtrek én oppervlakte. DENK-03 nrO 5: 'vanaf nul' weg (H2, ouderzin, ALG, laag 1 '16', laag 2 '9') | ✓ 'Ronde 1b'. 13 gevlagd, guard FAIL 0 |
| Z-#518 | Overzicht | Guard voor `contextgebonden` in check_hints (WARN bij > 1 item of een vlagwoord dat niet in de opgave staat). Onze guard staat in `g7work/b1/check.py` | open (Overzicht) |
| V-#516 | Overzicht (data ✓ 12:00:13) + Oefeningen | DENK-03 nrO 7 in flesjes en deciliter: H1, H2, ALG, regels '9 dl'/'4 dl' met laag 1/laag 2. Routes samen nagerekend (les 145): geen verkeerde route op 7 | ✓ 'Ronde 1b'. 2 sleutels; 'LET OP regel niet te lezen' weg |
| Z-#519 | Oefeningen | DENK-03 nrO 6 '11 dl': soort 'meer dan dag één of dag vergeten', laag 2 korter | ✓ 'Ronde 1b'; b1/check rekent beide routes na |
| Z-#520 | Oefeningen (tekst); getallen: Overzicht | DENK-02 #5 '10' en DENK-03 nrO 1 '12': laag 1 past bij beide routes; soortnamen noemen beide. Getallenvoorstel van Didactiek (20/30; rust 7; DENK-03 nrO 4 begingetal 3, zwakke treffer nrO 10) blijft voor Overzicht | ✓ tekst; getallen open (Overzicht) |
| Z-#522 | Oefeningen | Laag 2 ≈ H2 bij DENK-02 #14 '7 wielen', #1 '17', DENK-03 nrO 2 '302 g': nieuwe stap | ✓ 'Ronde 1b' |
| Z-#523 | Oefeningen | 'dan' in laag 2 bij DENK-03 #3 en nrO 25 | ✓ 'Ronde 1b' |
| Z-#524 | Oefeningen | DENK-03 nrO 2 H2, DENK-02 #10 'veel meer', DENK-02 #7/#11 zin over tekort | ✓ 'Ronde 1b' |
| Z-#521, Z-#525 | Overzicht (data) | contexten (lantaarnpalen, eierdoos, sportveld, fietsen met 3 wielen); 'gekleurd' in de opties van DENK-02 #3 | genoteerd; de teksten noemen geen aantallen uit die contexten |
| Oef-#421/#422 | Overzicht (motor) | Normalisatie '−'/'-' en 'euro'/'€' (Z-#411): nog niet in de motor van 12:11:17 (`compile_regel('6 − 4')` en `'13 euro'` → None). Omwegen blijven | open |
| los-scan | Oefeningen | G7 met de uitgebreide los-scan (les 135): 3 vondsten (DENK-02 #1, #8, #9) opgelost | ✓ 0 |

Checks (zandbak): check_hints 25 klaar · 130 open · 0 FAIL · 0 WARN · 0 INFO; notatie ALLES OK; b1/check FAIL 0; verklap FAIL 0; los-scan 0; tweede run 0 wijzigingen. Lessen 144–149: `hints/lessen_g7.md`.

## Review batch 1 Didactiek (8 okt; build 12:16:26, Overzicht)
| # | Wie | Stand |
|---|---|---|
| V-#516 | Overzicht (data) + Oefeningen (tekst) | ✓ DENK-03 nrO 7: «Je hebt 3 flesjes sap van elk 3 dl. … giet er 2 dl uit.» Antwoord 7 dl, afleiders 9 dl (stap twee vergeten) en 4 dl (3 + 3 − 2). `scripts/fixlijst_g7.py`, aangeroepen in build_g7 na FX21. Routes nagerekend (tools/routes_check.py): 7 komt alleen uit 3 × 3 − 2. Kop van 'liter' naar 'dl' (kopGewijzigd; nrOrigineel 7 blijft via claudeId). Teksten in dl: Oefeningen ronde 1b ✓ |
| V-#515, V-#517 | Oefeningen | ✓ ronde 1b (patch_batch1.py): H1/H2 zonder verklapper; vlag 'contextgebonden' in 13 entries |
| Z-#518 | Overzicht | ✓ CONTEXT-guard in check_merge_notatie (tools/contextgebonden_check.py): WARN als een gevlagde entry meer dan één item krijgt of een vlagwoord niet in de opgave staat. Nu 13 gevlagd, 0 WARN |
| Z-#520 | Overzicht (check) → Oefeningen/Didactiek (tekst/getallen) | ✓ ROUTES (INFO, tools/routes_check.py): DUBBEL DENK-02 #5 '10' (10 uit de vraag / 20 − 10), DENK-03 nrO 1 '12' (3 × 4 / 3 + 4 + 5), DENK-03 #3 '7' (4 + 3 / 6 + 4 − 3), DENK-03 #9 '16' (4 × 4 / 20 − 4), DENK-03 nrO 7 '9 dl' (3 × 3 / 3 + 3 × 2) en '4 dl' (3 + 3 − 2 / 2 × 2); ZWAK DENK-03 nrO 4 '16' (4 × 4) en nrO 10 '9' (5 + 4). Heel G7: 31 INFO-treffers. Teksten niet aangepast |
| Z-#525 | Overzicht | ✓ DENK-02 #3 en #8 ('welke tekening/som') op visual.nodig + nietLiveZonderBeeld zoals #4/#9/#10/#13; #3 met eis 'niet alleen kleur'. VERH-04 #4 mengde rad (tekening verplicht) en zonder tekening → rad als eigen somtype (VERH-04 #7, bevroren v6). VISUAL-check: 0 WARN |
| Z-#521, 'gekleurd' DENK-02 #3 | Oefeningen | open |
| ONLEESBAAR | Overzicht (G5–G8) | ✓ apply_hints schrijft logs/regels_onleesbaar.json; check_hints geeft WARN als een regel bij geen enkel item van zijn somtype te lezen is (G5 0, G6 0, G7 0, G8 0) |
