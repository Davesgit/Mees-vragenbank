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
