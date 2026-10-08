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
| Z-#521, Z-#525 | Overzicht (data) | contexten (lantaarnpalen, eierdoos, sportveld, fietsen met 3 wielen); 'gekleurd' in de opties van DENK-02 #3 | ✓ build 13:31:47 (Oef-#432/#433) |
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

## Oefeningen ronde 1c (8 okt, na build 12:16:26; Z-#520 vervolg, V-#516, Z-#525)
| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#516 | Oefeningen | DENK-03 nrO 7 stond al in flesjes/deciliter sinds ronde 1b (H1, H2, ouderzin, ALG, regels '9 dl'/'4 dl'); de build las nog de oude batch1.json. Verpakkingstoets (les 149): alleen 'flesje(s)', 'deciliter' en 'kan' in de teksten | ✓ `hints/patch_batch1.py` (schrijver per fout-hint nu één: de _hernoem van ronde 1c) |
| Z-#520 | Oefeningen | Twee routes, laag 1 en laag 2 kloppen voor beide (les 146): DENK-03 nrO 3 '7 stoelen' (6 + 4 − 3 / 4 + 3) → soort 'geen keersom voor alle stoelen', nieuwe laag 1; nrO 7 '9 dl' (3 × 3 / 3 + 3 × 2) en nrO 9 '16 stickers' (20 − 4 / 4 × 4) → soort 'stand na stap één', laag 1 een waarde-uitspraak ('Dat is wat …'); nrO 7 '4 dl' (3 + 3 − 2 / 2 × 2) → soort 'geen keersom voor alle flesjes', nieuwe laag 1. DENK-02 #5 '10' en DENK-03 nrO 1 '12' waren al goed (ronde 1b, nagelopen) | ✓ 'Ronde 1c'. `g7work/b1/check.py` rekent per afleider beide routes na |
| Oef-#428 | Overzicht (data) | Zwakke treffers op het goede antwoord (les 145): DENK-03 nrO 4 (16 = 4 × 4) en nrO 10 (9 = 5 + 4). Geen tekst noemt of goedpraat die route (guard in b1/check). Getallenvoorstel: nrO 4 begingetal 3 (48; afleiders 24 een keer te weinig, 11 steeds twee erbij); nrO 10 '8 gespaard, 5 zakgeld, schrift 3' (10; afleiders 13, 16; 5 + 3 = 8). Bij andere getallen passen wij de regels '13'/'17' aan (omweg euro) | open (Overzicht) |
| Z-#525 | Oefeningen | VERH-04 #4 en het nieuwe #7 (rad, tekening verplicht): nog geen G7-hints voor VERH-04 (laatste in hints_todo). #7 krijgt bij die batch een eigen entry (rad: vakjes tellen op de tekening); genoteerd in `hints/batches.md` | genoteerd |

Checks (zandbak, build 12:16:26 + ronde 1c): check_hints 25 klaar · 130 open · 0 FAIL · 0 WARN · 0 INFO; notatie ALLES OK; apply 0 'LET OP'; b1/check FAIL 0 (mutant: oude laag 1 '9 dl' en een tekst met de foute route bij nrO 4 → FAIL, les 153); verklap FAIL 0; los-scan 0; tweede run 0 wijzigingen.

## Oefeningen batch 2 (8 okt): DENK-03 nrO 11–24, 26 + DENK-04 #1–#6
| # | Wie | Wat | Stand |
|---|---|---|---|
| batch 2 | Oefeningen | 21 somtypes, 162 items, 324 sleutels; alle sleutels op een eigen regel met eigen laag 2. Review: `review-batch2.md` | ✓ `hints/make_batch2.py`, `hints/batch2.json`, `hints/patch_batch2.py` (ronde 1a) |
| Oef-#429 | Overzicht (motor) | Regel 'de deelsom omgedraaid' (pred: 'a : b' met a en b omgewisseld t.o.v. het antwoord), naast 'de minsom omgedraaid'. Nodig voor DENK-04 #5 '8 : 328' (7 items), nu op 'andere fout' met een eigen laag 2 | open |
| Oef-#430 | Overzicht (data) | DENK-03 nrO 21: de stappen in de opgave nummeren ('Stap 1: neem 30. Stap 2: …'). Nu kan 'Bij stap 2' ook 'anders geteld' zijn | open |
| info | Overzicht | Apply meldt 12× 'LET OP regel niet te lezen' bij DENK-04: letterlijke naamregels lezen alleen bij items met die foute naam. Klopt zo; regels_onleesbaar.json en check_hints (0 WARN) zien het goed | – |
| info | Overzicht | Zwakke treffers op het goede antwoord in batch 2: DENK-03 nrO 13 'Tree 6' = 2 × 3, nrO 24 '360 g' = 120 + 240. Weinig waarschijnlijk; geen tekst noemt ze. Andere getallen alleen als jullie dat willen | – |

Checks (zandbak): check_hints 46 klaar · 109 open · 0 FAIL · 0 WARN · 0 INFO; notatie ALLES OK; b2/check FAIL 0 (mutanten → FAIL); b1/check FAIL 0; verklap FAIL 0 (batch 1 en 2); los-scan 0; tweede run 0 wijzigingen. Lessen O1–O2 (eerst 156–157): `hints/lessen_g7.md`.

## Oefeningen ronde 1d (8 okt; Didactiek recheck batch 1 op build 12:16:26)
Stand: build 12:25:41 (hint-sync 12:25:44) heeft batch1.json md5 057fc28c9508 (= ronde 1c) en batch2.json md5 1470df18f281 (eerste versie). Nog niet in een build: batch2 ronde 1a (12:27:29) en batch1 ronde 1d (12:30:10) (les 164).
| # | Wie | Wat | Stand |
|---|---|---|---|
| Z-#561 | Oefeningen | '7 stoelen' en '4 dl': één echte route (les 160/161), dus laag 1 vraagt weer naar het optellen, met het keersom-zinnetje (tekst Didactiek; '4 dl' op dezelfde manier). Soortnaam terug naar 'opgeteld in plaats van keer'. b1/check rekent alleen de echte route na en eist bij deze soort een vraag naar het optellen | ✓ `hints/patch_batch1.py` 'Ronde 1d' |
| Z-#563 | Oefeningen | DENK-02 #2: H1, H2, ouderzin en ALG weer alleen omtrek; vlag blijft (aanname: alle teksten gaan uit van een omtrekvraag) | ✓ 'Ronde 1d' |
| Oef-#431 | Overzicht (data) | DENK-02 #2: zet 'omtrek' vast in de kop in plaats van [ding] (voorstel Didactiek Z-#563) | ✓ build 13:31:47 (kop «… Welk getal hoort bij de omtrek?») |
| Z-#565 | Oefeningen | DENK-03 nrO 6 '8 dl' laag 2 in twee zinnen | ✓ 'Ronde 1d' |
| Z-#525 | Oefeningen | DENK-02 #3: 'gekleurd' (H2) en 'Kleur er één' (laag 2 'alle groepjes') weg. H2 «… Tel bij elke tekening hoeveel kinderen er bij de zandbak horen.» Regel 'alle groepjes gekleurd' → 'alle groepjes' (past ook bij 'omcirkeld'); soort 'alle groepjes'. Kleur-guard in b1/check, ook op omschrijvingen (les 158) | ✓ 'Ronde 1d'; verklap 0 FAIL |
| Oef-#432 | Overzicht (data) | DENK-02 #3 opties zonder kleur: «3 groepjes van 6, één groepje omcirkeld» · «3 groepjes van 6, alle groepjes omcirkeld» · «2 groepjes van 9, één groepje omcirkeld». Onze regels ('alle groepjes', '2 groepjes van 9') blijven passen | ✓ build 13:31:47 |
| Oef-#433 (Z-#521) | Overzicht (data) | Contexten, alleen in de opgaven (onze teksten noemen geen aantallen). **DENK-02 #12** lantaarnpalen 5 m uit elkaar: (A) 20 m → antwoord 120 meter, afleiders 140 meter (palen in plaats van stukken) en 100 meter (stuk te weinig); of (B) 'hekpaaltjes' met 5 m (getallen blijven; wij zetten dan 'palen' → 'paaltjes' in de teksten). **DENK-02 #9** eierdoos van 8: 6 eieren → '5 × 6 = 30', afleiders '5 + 6 = 11' en '6 − 5 = 1' (Claudes label 'verkeerde-bewerking' houden op die optie). **DENK-02 #2** 'sportveld' van 20 bij 10 m → 'speelveld' (getallen en regels blijven; onze teksten zeggen 'veld'). **DENK-02 #14** 'fietsen met 3 wielen' → 'bakfietsen met 3 wielen' (onze teksten passen). De regelwijzigingen voor #12 (A) en #9 staan klaar in 'Ronde 1d' (als commentaar) | ✓ data build 13:31:47 (#2 speelveld, #9 6 eieren, #12 (A) 20 m, #14 bakfietsen); regels #9/#12: Oefeningen (Ronde 1d-commentaar) |
| info | Overzicht | check_merge_notatie op de zandbak: FAIL komt alleen van ANTWVRAAG (V-#560, 12 items in GET-05/VERH-02/VERH-04, data); niets in onze hints | – |

Checks (zandbak, live + ronde 1d): check_hints 46 klaar · 109 open · 0 FAIL · 0 WARN · 0 INFO; b1/check FAIL 0 (mutanten: oude laag 1 '7 stoelen', 'gekleurde', 'Kleur er één' → FAIL); b2/check FAIL 0; verklap 0 (batch 1 en 2); los-scan 0; tweede run 0 wijzigingen. Lessen 156–165 in `hints/lessen_g7.md`; 156–159 in `g5/hints/lessen_g5.md` en `g6/hints/lessen_batch2.md`. Onze eigen lessen 156–157 in lessen_g7.md heten nu O1–O2 (botsing met de nummers van Didactiek).

## Overzicht 8 okt (build 12:36:53): batch 1 ronde 1b–1d + batch 2 ronde 1a, recheck batch 1 en review batch 2 Didactiek
| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#560 | Overzicht (data) | Procentitems waar het goede antwoord de noemer uit de vraag is (n = N² : 100). Didactiek's getallen (6/30, 12/40, 3/20, 20/50, 14/40) bestaan al als ander item in hetzelfde doel (de G7-bank heeft 0 dubbele opgaven per doel), dus vergelijkbare nieuwe paren, afleiders uit dezelfde denkfouten: VERH-02 bank-814 '24 van 30' → 80% (20% andere deel, 8% nul-fout) · bank-897 '28 van 40' → 70% (7%, 28% overgenomen) · bank-983 '14 van 20' → 70% (30%, 7%) · VERH-04 bank-040 '3/15' → 20% (3%, 2%) · bank-064 '9/45' → 20% (500% omgekeerd, 200% nul-fout) · bank-101 '14/35' → 40% (250%, 400%). Nagerekend met routes_check: geen route op het goede antwoord | ✓ `scripts/fixlijst_g7.py` (V560) |
| V-#560 (check) | Overzicht | Nieuwe check ANTWVRAAG (`tools/antwoord_in_vraag_check.py`, FAIL in check_merge_notatie G5–G8): procent (ook teller/noemer van een breuk in de vraag) en breuk; niet bij kies- en plaatsvragen ('Kies uit', 'het grootst/kleinst', 'op de lijn'). G5 0 · G6 0 · G8 0 · G7 12 vóór de fix → 0 | ✓ |
| V-#560 (GET-05) | Overzicht (data) | De check vond ook 6 typitems in GET-05 #3 'a/n − b/n' met a = 2b (het afgetrokken stuk = het goede antwoord): 181 '6/8 − 4/8', 195 '6/10 − 2/10', 199 '8/11 − 6/11' (niet 8/11 − 5/11: dat is bank-229, dan schuift de elfden-spreiding), 201 '10/12 − 6/12', 231 '8/9 − 5/9', 248 '6/7 − 4/7'. Sleutels opnieuw: (a − b)/2n 'noemers opgeteld' en (a + b)/n 'erbij gedaan', met de bestaande getalloze teksten | ✓ fixlijst_g7 (V560) |
| Oef-#428 | Overzicht (data) | nrO 4 'begin bij 3' → 48 (24, 11); nrO 10 'schrift van 3 euro' → 10 euro (13, 16). Nagerekend: geen route op het goede antwoord. Regels '9' en '17' lezen nu niet (2 ONLEESBAAR-WARN) tot Oefeningen ze omzet | ✓ data · regels: Oefeningen |
| Oef-#430 + Z-#581 | Overzicht (data) | nrO 21: 'Stap 1: neem 30. Stap 2: … Iemand schreef na elke stap het getal op: 30, 24, 8, 18.' | ✓ |
| Z-#574 | Overzicht (data) | nrO 16: 'Recept. Stap 1: pak 3 glazen. Stap 2: …' | ✓ |
| Z-#575 | Overzicht (data) | nrO 24: 12 koekjes 60 g → 36 koekjes; bewering 120 g; goed 'Nee, het moet 180 g zijn', afleiders 'Ja, 120 g klopt' en 'Nee, het moet 20 g zijn'. Regels 'Ja, 240 g klopt' en 'Nee, het moet 40 g zijn' lezen nu niet (2 ONLEESBAAR-WARN) tot Oefeningen ze omzet | ✓ data · regels: Oefeningen |
| Z-#576 | Overzicht (data) | DENK-03 bank-014 en bank-023: visual niet nodig (tekstitems), nietLiveZonderBeeld weg | ✓ |
| Z-#562 | Overzicht (tool) | routes_check: alleen routes met een denkfout-patroon (getal overnemen; bij twee getallen elke bewerking; bij drie de goede vorm met één andere bewerking of de eerste stap). Losse sommen (4 + 3, 2 × 2, a × a) en tussenstap 1/0 tellen niet; de goede som is geen ZWAK, ook niet als hij niet alle getallen gebruikt (begin bij 0, schaal 1 : n); 'op de'-antwoorden niet. Heel G7 per stuk in check_merge_notatie en `logs/routes.json`: 31 → 6 meldingen | ✓ |
| taak 4 | Overzicht | VERH-04: md-kop = nrOrigineel (`NR_IS_NRO` in build_g7): rad = Somtype 7, 'in welke zak' = 6, 3 ↔ 4. In 51 andere somtypes (DENK-03, GET-04, GET-05, MEET-02, …) verschilt de weergave nog van nrOrigineel; niet aangepast (verwijzingen '#n' van Didactiek/Oefeningen) | ✓ VERH-04 |

## Oefeningen ronde 1e (batch 1) + ronde 2b (batch 2) (8 okt, op data 12:36:53; Didactiek review-batch2-didactiek.md, build 12:32:32)
Bestanden: `hints/patch_batch1.py` (blok 'Ronde 1e') → `hints/batch1.json`; `hints/patch_batch2.py` (blok 'Ronde 2b') → `hints/batch2.json`; `hints/lessen_g7.md` (166–170); checks `g7work/b2/check.py` (les 167/168/169-guards). Back-ups: /tmp/g7_hints_1e_1236/, /tmp/g7_hints_2b_1238/. Tweede run beide 0 wijzigingen.
| # | Wat | Stand |
|---|---|---|
| Oef-#428 (regels) | DENK-03 nrO 4: regels '8' → '24' (een keer te weinig), '9' → '11' (steeds twee erbij); nrO 10: '17' → '16' (prijs erbij; '13' blijft). H2 nrO 4 'het getal uit de vraag' → 'het begingetal' (les 167). Teksten verder ongewijzigd (geen getallen). Routes: 24 = 3 → 6 → 12 → 24, 11 = 3 + 2 × 4, 16 = 8 + 5 + 3, 13 = 8 + 5; geen route op het goede antwoord | ✓ (ONLEESBAAR-WARN weg) |
| V-#571 | nrO 20: 'het laatste getal' → 'het getal van de min-stap' in laag 2 van '34' (tekst Didactiek) en '5', en laag 1 'andere fout' | ✓ |
| Z-#570 | nrO 11 '6 km' laag 2: «… is de route langer of korter dan dat?» | ✓ |
| Z-#571 | nrO 14 H2: «… het getal bij op dat in die stap staat.» | ✓ |
| Z-#572 | nrO 19 laag 1 «Keer een getal is iets anders dan dat getal erbij.»; nrO 23 laag 1 «… Dat hele getal deel je in de laatste stap.» Scan op getallen in woorden in batch 1/2: de rest is vast (stapnamen, dubbel vouwen, twee reeksen, vier stappen, drie kolommen, twee soorten fietsen; 'twee rijtjes' bij nrO 12 hangt aan de vlag-aanname) | ✓ guard b2/check |
| Z-#573 | nrO 26: soort 'niet omgerekend' → 'helft genomen in plaats van hoe vaak het past'; laag 1 «Hoe vaak past de afstand tussen twee bordjes in één kilometer? Zoveel stukken liggen er in elke kilometer van de tocht.» Laag 2 blijft | ✓ |
| Z-#575 (regels) | nrO 24: regels 'ja, 120 g klopt' (bewering, 60 × 2) en 'nee, het moet 20 g zijn' (60 : 3). Teksten en vlag 'koekjes' blijven | ✓ |
| Z-#581 | nrO 21: «Het begingetal nemen is de eerste stap» weg uit H2 en uit de fout-hint; soort 'stap die nog klopte', laag 1/2 van Didactiek | ✓ |
| Z-#577 | DENK-04 #1 H2: «… Lees dan elke som precies zoals hij er staat. Welke som geeft die uitkomst?» | ✓ |
| Z-#578 | DENK-04 #2 'de som': «Hoort de naam som bij een minsom? …», laag 2 «De naam som hoort niet …»; H2 «De namen term en som …»; #3 'uitkomst gekozen' «Alleen het getal achter het isgelijkteken heet de som.» | ✓ |
| Z-#579 | DENK-04 #1–#4, #6 'andere fout': laag 1 een vraag, de koppelzin in laag 2 | ✓ |
| Z-#580 | DENK-04 #2/#3/#4/#6: 'het getal uit de vraag' → 'het getal waar de vraag over gaat' (H1, H2, fout-hints) | ✓ |
| twijfel 2 | DENK-04 #5 'andere fout' = tussenstap: assert in b2/check (7 sleutels, alle de omgedraaide deelsom). Zodra Oef-#429 er is: beide lagen naar die regel, 'andere fout' weer algemeen | ✓ assert |
Checks (zandbak = live 12:36:53 + deze patches): check_hints 0 FAIL / 0 WARN; notatie ALLES OK; b1/check FAIL 0 (25/50); b2/check FAIL 0 (162/324); verklap batch 1 en 2 FAIL 0; los-scan 0; mutanten ('het laatste getal', 'keer drie', 'het getal uit de vraag' in DENK-04) gevangen.

## Oefeningen batch 3 (8 okt): GET-01 #1–#7, GET-02 #1–#3, GET-03 #1–#4, GET-04 #1–#11 (25 somtypes, 2420 items, 10452 sleutels), zie `review-batch3.md`
Bestanden: `hints/make_batch3.py` → `hints/batch3.json` (eerste versie), `hints/patch_batch3.py` (ronde 1 leeg; tweede run 0 wijzigingen); checks `g7work/b3/check.py`, `g7work/b3/keys.py`, `g7work/b3/sbx3.sh`. Back-up vooraf: /tmp/g7_hints_b3_1233/.
| # | Wie | Wat | Stand |
|---|---|---|---|
| Oef-#434 | Overzicht (data) | GET-01 #7 bank-468 ('736.125', antwoord 3) heeft geen sleutels van Claude (claudeFoutHints leeg; claudeDenkfouten '2' grafiek-verkeerd-afgelezen en '5' getal-overgenomen, zonder tekst). Nu krijgt het alleen onze sleutel 'het hele getal' (getal1). Voorstel: sleutels '7' en '6' (de cijfers naast de tienduizendtallen, label 'een-ernaast'), zoals bank-466/469; of motorregel 'fout = het cijfer op de plek ernaast' | open |
| Oef-#435 | Overzicht (motor) | Regels 'fout = antwoord × 100 / × 1000 / : 100 / : 1000' (nu alleen × 10 / : 10). GET-01 #1: 593 sleutels (×100, ×1000, : 100, : 1000) vallen nu op 'antwoord ± 1 of meer' met een algemene tekst. Laag prioriteit | ✓ gesloten (Didactiek review batch 3, twijfel 1: de algemene regel is waar bij alle 593 sleutels) |
| Oef-#436 | Overzicht (motor) | 'fout = antwoord ± 0,1 / ± 0,01' geeft geen sleutel bij een heel antwoord ('4,6 + 0,4 = 5' → '4,9'). GET-03 #1/#2 4 sleutels, GET-04 #1/#2 24 sleutels staan daarom op Claudes label 'net ernaast (heel antwoord)'. Voorstel: de regel ook bij een heel antwoord | open |
| Oef-#437 | Overzicht (motor) | _nums leest '8,4' als twee getallen (8 en 4). getal1/getal2-regels zijn bij kommagetallen in de vraag onbruikbaar (bv. 'quotiënt,rest' bij GET-04 #5 '7,6 liter … over 4' zou '1,1' geven). Voorstel: kommagetal als één getal lezen, of een eigen 'kommagetal1' | open |
| Oef-#438 | Overzicht (data) | GET-04 nrO 9 (alle 4 items): «Een pakket weegt 6,3 kg. Hoeveel wegen 10 stenen?»: het ding wisselt. Voorstel: hetzelfde ding in beide zinnen ('Een pakket weegt 6,3 kg. Hoeveel wegen 10 pakketten?'). GET-04 nrO 5: '7,6 liter water … over 4 stickers', '… over 3 tanden', '… over 6 sterren', '115 kilo kaartjes', '81 kilo stickers': verdelen over iets dat kan krijgen (kinderen, teams, emmers) en kilo bij iets dat je weegt (zand, appels). Onze teksten noemen geen ding en blijven | open |
| Oef-#439 | Overzicht/Didactiek | GET-04 nrO 6 (gemiddeld): Claudes label 'verhoudingstabel-verkeerd' op 6 sleutels zonder herkenbare route (14 bij 6, 13, 3, 15, 18 → 11; 15 bij 15, 11, 12, 9, 13 → 12). Label 'verkeerde-bewerking' dekt zowel de som (55) als het middelste getal (13). Voorstel: afleiders uit echte denkfouten (som, middelste getal, som : 4) | ✓ gesloten (Didactiek review batch 3, twijfel 3: geen echte route, de algemene vraag blijft; de 11 sleutels onder verkeerde-bewerking → Oef-#442) |
Stand (les 164): build 2026-10-08 12:44:21 met hint-sync 12:44:24 bevat batch1.json 1106695c9148 (t/m ronde 1e), batch2.json 8c699cd7b0a1 (t/m ronde 2b) en batch3.json 27ee48fd8a5d (eerste versie, nu gesynct: alleen nog patch_batch3.py). Hint-inhoud live = zandbak (0 verschillen op DENK-02/03/04 en GET-01..04); tweede run van patch_batch1/2/3: 0 wijzigingen.

## Overzicht 8 okt: motor (build 12:44:21, met batch 1 ronde 1e, batch 2 ronde 2b, batch 3)
| # | Wie | Wat | Stand |
|---|---|---|---|
| Oef-#421/#422 | Overzicht (motor) | `norm421` in fout_regels.py: letterlijke regels en opties met één notatie: '−', '-' (tussen getallen/spaties) en '–' zijn één minteken; '3 euro'/'€ 3' → '€3', maar alleen als de regel zelf een bedrag is (een regel '16' leest '16 euro' zoals vroeger). Ook 'de minsom' en 'de minsom omgedraaid'. Zelftest `_zelftest421` bij elke import. Regressie oud ↔ nieuw (tools/motor_regressie.py): G5 4845 · G6 4302 · G7 2607 items · 0 anders | ✓ · Oefeningen kan de workarounds in DENK-02 #8/#9 weghalen |
| Oef-#429 | Overzicht (motor) | Regel 'de deelsom omgedraaid': antwoord 'a : b' → alleen de optie 'b : a'; is het antwoord een getal en noemt de vraag 'a : b', dan b/a op waarde. Proef met DENK-04 #5: alle 7 items ('8 : 328' …) krijgen de sleutel, de keersom blijft 'de keersom' | ✓ motor · regel in batch 2: Oefeningen |

## Overzicht 8 okt: datapunten Oefeningen op build 12:44:21 (motor; build 12:52:39)
| # | Wie | Wat | Stand |
|---|---|---|---|
| Oef-#437 | Overzicht (motor) | `_nums` leest '8,4' als één getal (Fraction, sleutel '8,4' via _kg); 'komma + spatie' blijft opsomming, '3,5,7' blijven drie getallen. Alleen met de vlag `KOMMA437 = True` (apply_hints G7/G8): in G6 zou het 24 items in GET-M03 ('Zet 1,4 op de lijn') een andere foutRegels-waarde geven ('4' weg, '1,4' erbij), dus G5/G6 blijven gelijk. 'fout = een getal uit de vraag' slaat een kommagetal = het antwoord over. Regressie G5 0 · G6 0 · G7 0 anders (geen huidige G7-regel rekent met een kommagetal) | ✓ · Oefeningen kan getal1/getal2-regels nu bij kommagetallen gebruiken |
| Oef-#436 | Overzicht (motor) | 'fout = antwoord ± 0,1 / ± 0,01' geeft ook sleutels bij een heel antwoord, als de vraag een kommagetal heeft ('4,6 + 0,4 = 5' → 4,9 · 5,1 · 4,99 · 5,01). Zonder die voorwaarde kregen 45 hele antwoorden zonder kommagetal (gemiddelde, GET-04 #6) ook '47,9'-sleutels. G7: 7 items met extra sleutels (GET-03 140/379/404, GET-04 511/561/668/744); G5/G6 0 anders | ✓ · de sleutels op Claudes label 'net ernaast (heel antwoord)' kunnen naar deze regel |
| Oef-#434 | Overzicht (motor) | Regel 'fout = het cijfer op de plek ernaast': bij 'Welk cijfer staat op de plaats van de X in N?' de cijfers links en rechts van die plaats (bank-468 → 7 en 6; 466 → 7 en 1; 469 → 7 en 9). Proef met de entry van GET-01 #7 | ✓ motor · regel in batch 3 (in plaats van 'Claudes sleutel: een-ernaast'): Oefeningen |

## Oefeningen 8 okt: ronde 2c + batch 4
Stand (les 164): build 12:52:39 bevat ronde 2c (batch1.json caa201bcf1a0, batch2.json 844a9b9f8428, batch3.json afdde4a2ff39; live DENK-04 #5 = {'deelsom omgedraaid': 7, 'keersom': 7}, DENK-02 #8/#9 'afgehaald' op de letterlijke opties). batch4.json (8d8af6e27596, 12:53:35) is nieuw en nog niet gesynct. Tweede run patch_batch1..4: 0 wijzigingen.

| # | Wie | Wat | Stand |
|---|---|---|---|
| ronde 2c (Oef-#429) | Oefeningen | DENK-04 #5: de tussenstap van les 168 vervalt. Beide lagen van 'andere fout' naar de nieuwe regel 'de deelsom omgedraaid' (soort 'deelsom omgedraaid'); 'andere fout' krijgt een algemene laag 1 als vraag («Welke som geeft het quotiënt? …») en laag 2. Assert in g7work/b2/check.py omgezet: 0 sleutels op 'andere fout', 7 op 'deelsom omgedraaid'. `hints/patch_batch2.py` | ✓ live in build 12:52:39 |
| ronde 2c (Oef-#421/#422) | Oefeningen | Omwegen weg: DENK-02 #8/#9 'afgehaald' van Claudes label 'verkeerde-bewerking' naar de letterlijke optie ('6 − 4', '8 − 5 = 3'); DENK-03 nrO 10 regels '13' → '13 euro' en '16' → '16 euro'. Teksten ongewijzigd. b1/check FAIL 0. `hints/patch_batch1.py` | ✓ live in build 12:52:39 |
| Oef-#426 | Overzicht (motor) | Gesloten: in de motor sinds G5-build 12:13 (ook in g5/merge-fixlijst.md op ✓ gezet) | ✓ gesloten |
| batch 4 | Oefeningen | GET-05, MEET-01, MEET-02, MEET-03 (27 somtypes, 2625 items, 9173 sleutels): `hints/make_batch4.py`, `hints/batch4.json`, `hints/patch_batch4.py` (ronde 1 leeg), `review-batch4.md`; checks `g7work/b4/check.py`, `mut.py`, `sbx4.sh` | wacht op sync |
| Oef-#440 | Overzicht (motor of data) | MEET-03 #9 (bak in m³, hoogte 0,5/1,5/2,5 m): 42 sleutels staan als '8,0', '300,0', '16,0'. De motor leest die niet (zelfde oorzaak als Oef-#437: '8,0' wordt 8 en 0), dus 'fout = getal1 × getal2' en 'fout = antwoord × 10' missen ze. Nu gevangen via Claudes labels ('omtrek-oppervlakte-verwisseld', 'komma-verschoven', 'kommagetal-als-geheel'). Voorstel: sleutels zonder ',0' in de data ('8'), of #437 in de motor. Daarna laten we 'tien keer te veel' (komma-verschoven) vallen in patch_batch4 ronde 1b | ✓ klaar (motor + data, build 13:13:00; Z-#639) |
| Oef-#441 | Overzicht (data) | MEET-03 #1 kop «Een balk heeft een inhoud van # [ding].»: [ding] is in alle 838 items de eenheid 'cm³' en geen ding. Voorstel: 'cm³' vast in de kop (onze H1 zegt al «De inhoud staat in cm³»). Klein; geen invloed op de hints | open |

Nummering: volgende vrije Oef-#442.

## Oefeningen 8 okt: ronde 3b (batch 3), 1f (batch 1), 2d (batch 2), 1b (batch 4)
Stand (les 164): build 13:04:53 bevat alles hieronder (batch1.json a6a31a9daae0, batch2.json 8a55fa5ee9b7, batch3.json 8b808f435b7c, batch4.json 5b5e44fc7a53). Tweede run patch_batch1..4: 0 wijzigingen. Zandbak = live: check_hints 0 FAIL / 0 WARN (98 klaar · 57 open), notatie ALLES OK, b1/b2/b3/b4-check FAIL 0.

| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#600/#601/#602/#605/#606 | Oefeningen | batch 3, zie review-batch3.md 'Ronde 3b'. V-#602: 10 sleutels op 'geleend bij de duizendtallen', 6 op het vangnet | ✓ build 13:04:53 |
| V-#603 / V-#604 (nrO 5) | Overzicht (data) | tafelsommen weg, 115 : 8 en 241 : 8 vervangen (build 13:02:22). Onze komma-teksten blijven; 'net ernaast (heel antwoord)' bij GET-04 nrO 1/2 weg (0 sleutels) | ✓ |
| V-#604 (nrO 1) | Oefeningen | H2 met de rest achter de komma | ✓ |
| V-#607 / V-#608 / Z-#609 | Overzicht (data) | in build 13:02:22/13:04:53. Nagekeken in de zandbak: nrO 9 'Een pakket … 12 pakketten', nrO 5 nieuwe getallen, hoofdletters. In 13:02:22 splitste de hoofdletter de kop van GET-03 nrO 3 in 6 somtypes (check_hints FAIL hint-koppeling); in 13:04:53 weer één somtype, 0 FAIL | ✓ |
| Z-#585, Z-#586 | Oefeningen | ronde 1f (patch_batch1.py) | ✓ |
| Z-#587, Z-#588, Z-#589 | Oefeningen | ronde 2d (patch_batch2.py); alle zinnen met 'het getal waar de vraag over gaat' teruggelezen (les 171) | ✓ |
| Z-#590 | Oefeningen | g7work/b2/check.py: les 167 overal (ook 'de hoeveelheid uit de vraag'), samengestelde getalwoorden (vijfhonderd), assert → FAIL. Mutanten M5/M6 nu gevangen | ✓ |
| batch 4 ronde 1b | Oefeningen | hercheck les 180–185, zie review-batch4.md | ✓ build 13:04:53 |
| Oef-#435, Oef-#439 | – | gesloten (Didactiek, twijfel 1 en 3) | ✓ |
| Oef-#442 | Overzicht (motor) | Z-#603: regels 'fout = de som van de getallen' en 'fout = het middelste getal (op grootte)' voor GET-04 nrO 6 (gemiddeld). Nu staan 6 totalen en 5 middelste getallen onder Claudes 'verkeerde-bewerking' met een vraag die bij beide past. Met de regels krijgen ze de scherpere teksten van 'niet gedeeld' en 'middelste getal' | open |
| Oef-#443 | Overzicht (data, [ding]) | MEET-03 #10 «Een doos voor poesjes/sterren is … Hoeveel cm³ past erin?» en #9 «Een bak in het bos/moeras/nest»: [ding]/[plek] maken geen echte vraag (les 184). Voorstel: dingen die je in een doos doet (knikkers, blokjes), plekken waar een bak staat (tuin, schuur) | ✓ klaar (build 13:13:00; rest V-#631 in de build van ronde r4; Z-#639) |
| Oef-#440 | Overzicht | nog 42 sleutels met ',0' in MEET-03 #9 (build 13:04:53). Daarna: 'tien keer te veel' eruit (patch_batch4 ronde 1c) | ✓ (build 13:13:00, ronde 1c) |

Nummering: volgende vrije Oef-#444 (zie onder: #452).

## Overzicht 8 okt: review batch 3 (Didactiek), batch 4 (Oef-#440/#441), Oef-#442/#443 (build 13:13:00)
Builds 13:02:22 → 13:05:00 → 13:10:18 → **13:13:00** (eindstand). Checks G7: check_hints 0 FAIL / 0 WARN (98 klaar · 57 open), merge-notatie ALLES OK. G5/G6/G8 merge-notatie ALLES OK met de nieuwe FAIL-checks; G5 #121 0, generator 0; G6 FIX6 0 FAIL. Motorregressie (tools/motor_regressie.py, oud = vóór #440): G5 0 en G6 0 van 4845/4302 items anders.

| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#603 | Overzicht (data) | 14 tafelsommen uit GET-04 nrO 1/2 geschrapt (`bevroren/geschrapt_v603.json` met reden; build: geschrapt 'besluit Didactiek: V-#603' 14, assert alle 14 gevonden). De uitzondering '12 : 4' stond alleen als commentaar in Oefeningen' make_batch3.py en is met de items weg | ✓ |
| V-#607 / Z-#609 | Overzicht (data) | `fixlijst_g7.V607`: nrO 9 'Een pakket weegt … Hoeveel wegen N pakketten?' (4); nrO 5 logische contexten (zand/zakken, appels/kratten, aarde/bakken, water/flessen/emmers, limonade/kannen) en 114 : 8 = 14,25, 242 : 8 = 30,25; Z-#609 '18 liter … 3 drinkbakken' = 6 (sleutel '7', geen '7,0') en GET-03 '1,4 − 0,6' = 0,8 | ✓ |
| V-#608 | Overzicht (data + check) | `_v608`: hoofdletter aan het begin (8 items GET-03). De kop blijft gelijk (regel in somtype_g7: '^(De\|Het) … heeft # [ding], [plek] heeft er #'). Check `tools/hoofdletter_check.py` (FAIL in G5–G8): opgave of zin na '. ? !' met kleine letter; niet na '...' (invulplek), afkortingen of 'getal.' G5/G6/G7/G8: 0 | ✓ |
| Z-#606 | Overzicht (check) | WARN Z606 in g7/check_merge_notatie: aantal in GET-04 nrO 8 is 10/100/1000. Nu 4 items, allemaal 100. De ouderzin «keer tien, honderd of duizend» belooft meer dan de items laten zien (Oefeningen/Didactiek). Ook: «Eén poesje weegt 3,3 gram» is geen logische context | ✓ (melding) |
| Z-#607 | Overzicht (README) | Slotnul: '3,80' = '3,8' stond al in README (Invoer tolerant); '2' bij antwoord '2,0' er nu bij (README repo + g7/README §App-eis). Let op: GET-02 001/006 «Rond af op één cijfer achter de komma» → 2,0: Didactiek beslist of '2' daar goed is | ✓ |
| Z-#609 (check) | Overzicht (check) | `antwoord_in_vraag_check`: ook 'som': het antwoord is een getal uit een som 'a ∘ b' met een kommagetal, of 'verdeeld over n' met antwoord n (FAIL). Hele getallen ('4 : 2 = 2', 'a : b = c : ?') alleen INFO: G5 GET-M05 073/085, G7 VERH-03 318/352/518/531/545/620. Kloktijden, duizendpunten en 'Op welk cijfer eindigt' tellen niet | ✓ |
| Oef-#440 | Overzicht (motor + data) | Motor (alleen met KOMMA437, G7/G8): antwoord '8,0' = 8; een sleutel '8,0' past op regelwaarde 8; 'antwoord × 10 / : 10' werkt bij een kommagetal-antwoord (1,1 → 11 / 0,11; was 'regel niet te lezen' in MEET-03 #3/#4/#9, 162×). Data (`_v440`): Claude-sleutels 'n,0' → 'n' (MEET-03 #9 16 items, VERH-04 #3 4), dubbel weg; niet bij afronden. Nu 0 fout-sleutels op ',0'. 'tien keer te veel' kan eruit (Oefeningen). Tekst 'een nul te veel' bij 1,1 → 11 past niet goed (komma verschoven): Oefeningen | ✓ |
| Oef-#441 | Overzicht (data) | cm³/m³/dm³/mm³ en cm²/m²/dm²/mm²/km² in NIET_DING: MEET-03 #1 kop «Een balk heeft een inhoud van # cm³. …» (838 items). INTRO-WARN cm³: 0 | ✓ |
| Oef-#442 | Overzicht (motor) | Nieuwe regels 'fout = de som van de getallen' en 'fout = het middelste getal (op grootte)': de langste rij getallen (', ' / ' en '), alleen als de waarde ≠ antwoord, middelste alleen bij een oneven aantal. GET-04 nrO 6 (11 items): som 11×, middelste 10× (bij '9, 11, 12, 13, 15' = 12 = antwoord: geen sleutel). Oefeningen zet ze in de entry | ✓ motor |
| Oef-#443 | Overzicht (data) | `_v443`: MEET-03 #9 (32) 'Een bak in het bos/nest …' → naar de hoogte: ≤ 1 m zandbak (5), ≤ 2 m aquarium in de dierentuin (11) / waterbak op de kinderboerderij (1, zelfde getallen), hoger container (15). #10: sterren → knikkers, poesjes → blokjes. Koppen ongewijzigd ('Een bak is …'). Ouderzin «inhoud van een bak» kan blijven of naar 'bak of doos' (Oefeningen) | ✓ |
| V-#560 | Overzicht (data) | zes procentitems (VERH-02 #3 814/897/983, VERH-04 #1 040/064/101) staan al in de data sinds build 12:36:53 (commit c6afde5) | ✓ |
| – | melding | VERH-04 #3 «50% van de poesjes is kapot» is geen logische context (batch 5) | open |

## Oefeningen 8 okt: ronde 3c (batch 3) + ronde 1d (batch 4), recheck/review Didactiek op build 13:13:00
Zandbak = live build 13:13:00 + patches t/m 3c/1d (+ batch5_wip): check_hints 0 FAIL / 0 WARN (122 klaar · 33 open), merge-notatie ALLES OK; b1 FAIL 0 (50), b2 FAIL 0 (324), b3 FAIL 0 (2406 items, 10.471 sleutels, 0 op 'andere fout'), b4 FAIL 0 (2625 items, 9219 sleutels, 0 op 'andere fout'). Tweede run patch_batch1–4: 0 wijzigingen.

| # | Wie | Wat | Stand |
|---|---|---|---|
| V-#615 | Oefeningen | GET-03 nrO 2/3/4, H2 + elke 'Leen dan'-laag 2: «… jouw cijfer krijgt er tien bij, en het cijfer op de plek (kolom) ervoor één minder. Is het cijfer op de plek (kolom) ervoor een nul? Dan wordt die nul een negen, en leen je verder naar links.» (6 tekstplekken). GET-01 nrO 2/3 ongewijzigd: daar is 'het cijfer ervoor' het laatst genoemde cijfer (niet dubbelzinnig, Didactiek V-#600 ✓). `patch_batch3.py` ronde 3c | ✓ |
| Z-#617 | Oefeningen | GET-04 nrO 5: 'komma verschoven' (Claudes label, 4 sleutels, alle antwoord × 10, ook 60 bij 18 : 3) → motorregel 'tien keer te veel' (fout = antwoord × 10) met «Dat is tien keer te veel. Schat eerst: hoe groot is de uitkomst ongeveer?» en een laag 2 zonder komma | ✓ |
| Z-#618 | Oefeningen | guards3b: lenen over een nul ook in GET-03 nrO 2, gerekend met de aangevulde getallen (les 189): 2 + 1 + 0 items (8 − 1,75, 8 − 3,05, 86.204 − 9778); eist de zin van V-#615; FAIL op «Is dat cijfer» na «jouw cijfer». Mutanten M2b en 'oude zin' gevangen | ✓ |
| Z-#619 | Oefeningen | b2/check regel 176 met re.I; M5, M6, M7 gevangen | ✓ |
| Oef-#442 | Oefeningen | GET-04 nrO 6: 'niet gedeeld' → 'fout = de som van de getallen', 'middelste getal' → 'fout = het middelste getal (op grootte)' (zelfde teksten); 'optellen en delen' had daarna 0 sleutels en is weg (les 183) | ✓ gesloten |
| Oef-#434 | Oefeningen | GET-01 #7 'cijfer ernaast' → 'fout = het cijfer op de plek ernaast' (bank-468 krijgt nu 7 en 6) | ✓ gesloten |
| Z-#606 | Oefeningen | ouderzin GET-04 nrO 8: «… een gewicht keer tien, honderd of duizend …» (past bij H2; nu 4 items × 100) | ✓ |
| Oef-#429 | – | al gedaan in ronde 2c (DENK-04 #5 'deelsom omgedraaid', 7 sleutels) | ✓ gesloten |
| Oef-#431/#432/#433 | Overzicht (data) | nog niet in build 13:13:00 (sportveld, 'gekleurd', eierdoos 8, lantaarnpalen staan er nog). Regels voor #433 staan klaar als commentaar in patch_batch1 ronde 1d | ✓ build 13:31:47 |
| V-#630 | Oefeningen | GET-05 nrO 6/7 (grootst/kleinst): «Een grotere noemer betekent kleinere stukken» weg uit H2; laag 1 «Is dat echt de grootste (kleinste) breuk? Een grote (kleine) noemer zegt nog niet dat de breuk groot (klein) is: kijk ook naar de teller. Vergelijk …». Guard: geen vuistregel over de noemer; telt eenzijdigheid (nu 190/190 en 128/128, Z-#630) | ✓ (hercheck na Z-#630) |
| V-#632 | Oefeningen | GET-05 nrO 1/2/3 laag 1 'teller of noemer anders' als vraag naar de noemer | ✓ |
| V-#633 | Oefeningen | GET-05 nrO 4 H2 + laag 2: «… Heeft de teller minder cijfers? Zet er dan nullen voor. Nullen aan het eind achter de komma vallen weg.»; laag 1 'komma verschoven' nieuw. Guard speelt elk item na (les 192) | ✓ |
| V-#634 | Oefeningen | GET-05 nrO 3: «Haal de kleinere teller van de grotere af.» (H2 + twee lagen 2). Guard toetst het woord (eerste/tweede/derde/laatste/bovenste/onderste/middelste/vooraan/achteraan) over alle teksten van batch 4 (les 193) | ✓ |
| Z-#634 / #636 / #637 / #638 | Oefeningen | MEET-03 #1 'net ernaast' weg; GET-05 nrO 5 H1 + laag 2 'Staat er één cijfer achter de komma, dan …'; MEET-03 #9 laag 2 'Is een maat een kommagetal'; MEET-01 #1/#2 en MEET-03 #3/#4 H2 + laag 2 «Een punt in een groot getal is geen komma.» (guard) | ✓ |
| Oef-#440 | – | in build 13:13:00 (0 ',0'-sleutels); tijdelijke regel weg in ronde 1c. Kommagetal-antwoorden op '× 10' hebben overal een tekst met 'tien keer te veel' of de komma, nergens 'een nul te veel' | ✓ gesloten |
| Oef-#443 | Overzicht + Oefeningen | data in 13:13:00; ouderzin MEET-03 #9/#10 zonder 'bak', laag 2 'De buitenkant tel je niet.' Rest: V-#631 (doos voor truien/eieren) | ✓ klaar (V-#631 in de build van ronde r4; Z-#639) |
| hercheck | Oefeningen | na de volgende build van Overzicht: V-#631, Z-#630 (laag 1 van V-#630 bij gelijke tellers en 7/8 tegen 2/3), Z-#631, Z-#632/#633 (motorregel 'je gaf de bodem' → MEET-03 #1 labelregel erheen), Z-#635–#637 (contexten), Z-#616 (bedragen met €, GET-04 #11) | ✓ gedaan op build 13:26:46/13:31:47 (ronde 1e batch 4) |

## Oefeningen 8 okt: batch 5 (MEET-04, VBN-04, VERH-01, VERH-02; 25 somtypes), datapunten
| # | Wie | Wat | Stand |
|---|---|---|---|
| Oef-#444 | Overzicht (motor/data) | Minteken: claudeFoutHints hebben '-8' (koppelteken), claudeDenkfouten '−8'. In pas_toe valt een labelregel ('Claudes sleutel: …') dan nooit op die sleutel (vergelijking d['fout'] == k['fout']). 295 sleutels in batch 5 staan daardoor op 'andere fout' (MEET-04 #1 147, #2 111, #3 24, #5 8; VERH-02 #4 4, #7 1). Voorstel: norm421 op beide kanten, of claudeFoutHints.fout met '−'. Daarna gaan ze vanzelf naar de klaarstaande regels | omweg ✓ (ronde 1b batch 5: Claude-regel zonder label, tekst over de waarde; 0 op 'andere fout'); fix in de motor blijft wenselijk | ✓ build 13:48:53: motor (KOMMA437) zet Claudes sleutels in huisnotatie vóór de labelvergelijking ('-3' en '–3' vooraan → '−3', ook tussen getallen via norm421). Nu 295 sleutels met '−' (MEET-04 290, VERH-02 5), 0 met koppelteken. Getest zonder de tijdelijke regel 'Claudes sleutel (alle, zonder label)': VERH-02 #4/#7 en MEET-04 nrO 1/3/5 0 op 'andere fout' → regel kan daar weg; MEET-04 nrO 2 nog 35 sleutels met label 'nul-fout-tientallen' (−4 en 2 → '−2') waar geen labelregel voor is → daar eerst een regel 'Claudes sleutel: nul-fout-tientallen', dan kan de tijdelijke weg. G5/G6 regressie 0 anders |
| Oef-#445 | Overzicht (data/motor) | VERH-02 #3 (meerkeuze, opties '36%'): bij 33 items geen claudeFoutHints en bij 147 maar één van de twee; de labelregels bereiken de andere optie niet (213 sleutels op 'andere fout'). 'fout = getal1' leest '36%' niet (waarde416 haalt '%' niet weg). Voorstel: labelregel op claudeDenkfouten, of '%' in waarde416 | ✓ build 13:52:49: motorregels 'fout = het deel zelf (als %)' ('D%') en 'fout = geheel min deel' ('(G − D)%'), alleen bij antwoord met '%' en 'D van G' in de vraag, geen sleutel ≤ 0 of = antwoord. Entry nrO 3 (patch_batch5, blok Oef-#445): de labelregels getal-overgenomen/verhoudingstabel-verkeerd worden die motorregels, tekst en laag 2 van Oefeningen blijven. 'andere fout' 213 → 0 (het deel zelf 105, verschil van de getallen 108). G5/G6 0 anders |
| Oef-#446 | Overzicht (data) | Kommagetal-sleutels met een punt: '7.5', '2.5', '0.5' (VERH-01 #2, en een half stukje kun je niet kleuren), '4.4', '9.6' (VERH-02 #4), '6.7' (VERH-02 #6, 40 : 6). Huisnotatie met komma, of weg | ✓ build 13:59:15 (= Z-#668): fixlijst _z668 zet Claudes sleutels '\d+.\d{1,2}' om naar komma (VERH-02 nrO 4 '4,4'/'9,6'/'2,8'/'4,8'/'2,4', nrO 6 '6,7'); 0 sleutels met punt over. Balk kleuren VERH-01 nrO 2: 75% → 70% (14, sleutel 7), 25% → 100% (20, sleutel 10); 5% geschrapt (fe3199aa, bevroren/geschrapt_review5.json: geen hele route, 70/100 al gebruikt, de rest bestaat al) |
| Oef-#447 | Overzicht (data) | VBN-04 #2 'Welke staaf wordt het hoogst?': bank-032 juli en sept allebei 40, 'sept' is een optie en staat als fout; bank-030 juni en sept allebei 30 (sept geen optie, maar de vraag heeft twee antwoorden) | ✓ build 14:07:01 (= V-#665): bank-032 sept 40 → 35, bank-030 sept 30 → 20; nieuwe check staaf_gelijk_check (in g7/check_merge_notatie: FAIL bij gelijke hoogste/laagste staaf als de vraag daarnaar vraagt; G5/G6/G8 0) |
| Oef-#448 | Overzicht (data) | VERH-02 #7: antwoord '56' zonder €, sleutels '€24', '€104' met € (een kind dat '24' typt, raakt geen sleutel). Eén notatie (de vraag zegt 'in euro's') | ✓ build 14:08:50: VERH-02 #7 antwoorden met € (alle 5: '€56', '€42', en de drie nieuwe) |
| Oef-#449 | Overzicht (data) | 'Balk kleuren' (VBN-04 #1, VERH-01 #1/#2): jsRender null, het aantal stukjes staat nergens (VERH-01 #2 gaat uit van twintig). Graag in de data, dan kan de check het nalopen | ✓ build 14:08:50 (= V-#667): jsRender {'soort': 'balk', 'delen': n, 'kleurbaar': True} (G5-vorm): VERH-01 #2 20, VERH-01 #1 10, VBN-04 #1 10 (assert: grootste getal : stukje ≤ 10); kop blijft '[balk kleuren]' |
| Oef-#450 | Overzicht (data) | VBN-04 #1: Claudes sleutel '10' bij 4 items zonder route (bv. ma 45, stukje 5 → 9). Weghalen of een route | deels: ronde 1b batch 5 geeft '± 1' (één item: '10' bij antwoord negen); 3 over: bank-009 '10' = de staaf van ma (andere dag), bank-010/011 '10' zonder route | ✓ build 14:08:50: bank-010/011 sleutel '10' (geen route) weg, '± 1' en 'getal uit de vraag' blijven; bank-009 '10' (staaf van ma) blijft tot Oefeningen een regel 'andere dag' heeft (Z-#670) |
| Oef-#451 | Overzicht (data, les 195) | Toevallige treffer: 'getal min procent' of 'som/verschil' geeft het antwoord: VERH-02 #1 50% van 100, 80% van 400, 60% van 150; #3 5 van 25, 5 van 20, 90 van 150. Andere getallen | ✓ build 14:17:46 (+ Z-#665, Z-#666 #6): VERH-02 #1 50% van 100 → 290, 80% van 400 → 450, 60% van 150 → 450, 'x% van 100' (Z-#665) 30/20/40% → van 70, 90% → 450, 80/60% → 460; #3 5 van 25 → 7 van 35, 5 van 20 → 4 van 16, 90 van 150 → 30 van 50 (zelfde antwoord, opties opnieuw); #6 20 van 200 → 60 van 300 (20%), 2 van 20 → 3 van 20 (15%). Claudes sleutels per label opnieuw; scan op treffers (procent, geheel, geheel min procent/deel, som, omgekeerd delen) in #1/#3/#6: 0 |
| Oef-#427 | – | G5 MEET-E06 #1 gen-001 komt in G7 MEET-04 nrO 7 niet voor (220 claude-bank-items); niets te doen | ✓ gesloten (G7) |

Nummering: volgende vrije Oef-#452.

## Overzicht 8 okt: review batch 4 Didactiek, ronde r4 (build 13:26:46)
Build **13:26:46** (met batch 5 van Oefeningen; patch_batch1..5: 0 wijzigingen). Checks: G7 check_hints 0 FAIL / 0 WARN (123 klaar · 32 open), merge-notatie ALLES OK; G5/G6/G8 merge-notatie ALLES OK, G5 #121 0, generator 0, G6 FIX6 0 FAIL. Motorregressie (oud = vóór r4): G5 0 en G6 0 van 4845/4302 items anders. Code: `fixlijst_g7` blok 'Review batch 4' (+ `pas_toe_av8` voor de aanvulling uit G8), `bevroren/z630_ids.json`.

| # | Wie | Wat (data per somtype) | Stand |
|---|---|---|---|
| V-#631 | Overzicht (data) | MEET-03 nr 10 (nrO 10): doos voor truien (7×6×4) → kralen, eieren (10×3×2) → krijtjes; knikkers (11×4×4) en blokjes (10×8×6) passen. Maten en antwoorden gelijk | ✓ |
| Z-#637 | Overzicht (data + kop) | MEET-03 nr 9: de waterbak (5×4×1,5 = 30 m³) → «Een vijver in het park is 5 m lang, 4 m breed en 1,5 m diep. Hoeveel m³ water gaat erin?» (kop blijft 'Een bak is …'). Kop nr 10 → «Een doos is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ past erin?» (sync: kopGewijzigd in batch4.json) | ✓ |
| Z-#630 | Overzicht (data) | GET-05 nr 1/2 (nrO 6/7): 105 van 318 items nieuw (elk derde op id). Een derde gelijke tellers (grootst 21, kleinst 14; Claude-label 'grotere-noemer-is-groter' → 'niet de grootste/kleinste'), twee derde waar de noemer-truc fout gaat (grootst 42: de breuk met de grootste noemer is het grootst; kleinst 28: die met de kleinste noemer is het kleinst; nieuw Claude-label **'alleen-noemer-vergeleken'**, 140 sleutels nu op 'andere fout'). Echte breuken, zelfde noemerbereik, verschil ≥ 1/24, alles met Fraction nagerekend. Truc 'kleinste noemer' bij grootst nu 148/190 (78%), 'grootste noemer' bij kleinst 100/128 (78%) | ✓ (regel: Oefeningen) |
| Z-#631 | Overzicht (data) | MEET-02 nr 3 (nrO 4): vijvers 2×2 → 6×6 met 3×3 (27), 12×6 met 5×5 (47), 9×7 met 3×3 (54), 9×6 met 5×5 (29); sleutels tuin / tuin − zijde / tuin + vijver opnieuw | ✓ |
| Z-#632 | Overzicht (data) | MEET-02 nr 1: driehoek 6×3 (b+h = 9 = antwoord) → 6×9 (27); 4×3 ('twee erbij' 14 = omtrek) → 4×6 (12). Niet 6×5 (= 014 omgedraaid) en niet 3×6 (b+h = 9 = antwoord). jsRender basis/hoogte mee | ✓ |
| Z-#633 | Overzicht (data + motor) | MEET-03 nr 1: 30 cm³ op 2×3 / 3×2 (l+b = 5 = hoogte) → 78 cm³ op 2×3 (13) en 84 cm³ op 3×2 (14); geen treffer met l+b, l×b, l, b (ook niet ±1). Motorregel **'fout = de bodem (l × b)'**: zeker, gaat vóór '± 1' (ook als hij later in de entry staat). Met een proef-entry: 830 sleutels, waarvan 14 eerder op '± 1' | ✓ (entry: Oefeningen) |
| Z-#635 | Overzicht (data) | MEET-02 nr 2 (nrO 3): «Een L-vormig hok … Hoeveel m² is het hok?» → «Een L-vormige tuin … Hoeveel m² is de tuin?» (8). Kop gewijzigd (sync); H1/L1 'Het hok' → 'De tuin' is voor Oefeningen | ✓ |
| Z-#636 | Overzicht (data) | GET-05 nr 7 (nrO 5): botten → kralen / knikkers, noten → ballonnen, sterren → kralen (4 items; kaartjes blijft) | ✓ |
| Z-#616 | Overzicht (motor) | 'fout = getal1 / getal2' geeft bij een geldantwoord een bedrag als het getal in de vraag een bedrag is ('€28', '€45,60'); alleen G7/G8 (KOMMA437). GET-04 nrO 11: 31/31 sleutels in geldnotatie; de 9 '€58'-sleutels (aantal 10) staan nu op 'bedrag voor alles' | ✓ |
| VERH-04 nrO 3 | Overzicht (data) | «50% van de poesjes is kapot» → lampjes, «75% van de stappen is kapot» → ballonnen (antwoord 0,5 / 0,75 nagerekend) | ✓ |
| Z-#639 | Overzicht | Oef-#440 en Oef-#443 hierboven op klaar gezet | ✓ |


## Overzicht 8 okt: open punten batch 1 (Oef-#431/#432/#433, Z-#521/#525) en GET-04 nrO 8 (build 13:31:47)
Build **13:31:47**. Checks: G7 check_hints 0 FAIL / 4 WARN (123 klaar · 32 open; de 4 WARN zijn de oude letterlijke regels van DENK-02 #9/#12, zie hieronder), merge-notatie ALLES OK; G5/G6/G8 ALLES OK (G5 #121 0, generator 0, G6 FIX6 0 FAIL). Motor ongewijzigd (md5 c9b001a68fc7), G5/G6-data ongewijzigd. Code: `fixlijst_g7._r5` en `_r5_av8`, kopregel Oef-#431 in `build_g7.somtype_g7`.

| # | Somtype | Wat er in de data veranderd is | Regels (Oefeningen) |
|---|---|---|---|
| Oef-#431 + Oef-#433 | DENK-02 #2 (nrO 2) | Kop nu «Een speelveld is # meter lang en # meter breed. Je tekent het als rechthoek. Welk getal hoort bij de omtrek?» (was [ding] en 'sportveld'; sync: kopGewijzigd). Opgave: sportveld → speelveld (20 bij 10 m). Antwoord 60 meter (2 × (20 + 10)) nagerekend; opties 30 / 60 / 200 meter blijven | geen wijziging nodig ('200 meter', '30 meter' passen) |
| Oef-#432 (Z-#525) | DENK-02 #3 (nrO 3) | Opties «3 groepjes van 6, één groepje omcirkeld» (goed) · «3 groepjes van 6, alle groepjes omcirkeld» · «2 groepjes van 9, één groepje omcirkeld»; Claude-sleutels mee | geen ('alle groepjes', '2 groepjes van 9' passen) |
| Oef-#433 (Z-#521) | DENK-02 #9 (nrO 9) | «Je tekent 5 dozen en in elke doos 6 eieren.» Opties «5 + 6 = 11» · «6 − 5 = 1» · «5 × 6 = 30» (goed). Claude-labels: optellen-ipv-vermenigvuldigen / verkeerde-bewerking | **'5 + 8 = 13' → '5 + 6 = 11', '8 − 5 = 3' → '6 − 5 = 1'** (nu WARN ONLEESBAAR, sleutels op 'andere fout') |
| Oef-#433 (Z-#521) | DENK-02 #12 (nrO 12) | Variant (A): «Tussen twee palen zit steeds 20 meter.» 7 palen → 6 × 20 = 120 meter (goed); opties 140 meter (palen in plaats van stukken, 7 × 20) en 100 meter (stuk te weinig, 5 × 20) | **'35 meter' → '140 meter', '25 meter' → '100 meter'** (nu WARN ONLEESBAAR) |
| Oef-#433 (Z-#521) | DENK-02 #14 (nrO 14) | «4 fietsen met 2 wielen en 3 bakfietsen met 3 wielen» (getallen, opties en antwoord 17 wielen blijven) | geen; tekst 'alleen de fietsen' mag 'fietsen en bakfietsen' worden |
| melding Z-#606 | GET-04 nrO 8 | 851: «Eén poesje weegt 3,3 gram» → «Eén knikker weegt 3,3 gram. Hoeveel gram wegen 100 knikkers?» (antwoord 330; Claude-uitleg mee) | geen |

## Oefeningen 8 okt: aanpassen op build 13:26:46 en 13:31:47 (les 194)
Zandbak = live build 13:31:47 + alle patches: check_hints 0 FAIL / 0 WARN / 0 INFO (123 klaar · 32 open), merge-notatie ALLES OK; b1 FAIL 0 (50), b2 FAIL 0 (324),
b3 FAIL 0 (2406 items, 10.462 sleutels), b4 FAIL 0 (2625, 10.039), b5 FAIL 0 (1650, 7125; op 'andere fout' alleen VERH-02 #3 213 = Oef-#445 en VBN-04 #1 3 = Oef-#450).
Tweede run patch_batch1–5: 0 wijzigingen. Alle mutanten gevangen (b2 M5–M7, b3 M2b/Mjouw/M617/M434 + Z-#606 oude ouderzin, b4 mut/mut1d/mut1e, b5 mut/mut1b).
Ronde 3c (V-#615, Z-#617, Z-#618, Z-#619, Oef-#434, Oef-#442, Z-#606) en ronde 1d (V-#630, V-#632–#634, Z-#634, Z-#636–#638, Oef-#443) staan in de builds van 13:26:46 en 13:31:47 (teksten in somtypen/*.md).

| # | Wie | Wat | Stand |
|---|---|---|---|
| Z-#630 | Oefeningen | batch 4 ronde 1e: GET-05 nrO 6/7 labelregel 'alleen-noemer-vergeleken' ('kleine noemer gekozen' / 'grote noemer gekozen', 84 + 56 sleutels), laag 1 gespiegeld aan V-#630; guard: sleutelnoemer kleiner/groter dan die van het antwoord (alle 296/84/200/56) | ✓ |
| Z-#633 | Oefeningen | batch 4 ronde 1e: MEET-03 #1 regel 'fout = de bodem (l × b)' («Dat is de bodem: één laagje. Hoeveel laagjes passen er in de inhoud?»), 830 sleutels | ✓ |
| Z-#635 | Oefeningen | batch 4 ronde 1e: MEET-02 nrO 3 'Het hok' → 'De tuin' (H1 en laag 1); guard: geen 'hok'/'bak' in een tekst als geen vraag het noemt | ✓ |
| Z-#637 | Oefeningen | batch 4 ronde 1e: MEET-03 #9 H2 «Doe dat keer de hoogte (of de diepte).» (de vijver); #10 nieuwe kop: teksten noemen geen bak meer | ✓ |
| V-#631, Z-#631, Z-#632, Z-#636, Z-#616 | Oefeningen | nagelopen op live data: regels en teksten passen (b3/b4 FAIL 0); GET-05 nrO 5 noemt geen context | ✓ |
| Oef-#433 | Oefeningen | batch 1 ronde 1g: DENK-02 #9 '5 + 6 = 11' / '6 − 5 = 1', #12 '140 meter' / '100 meter' (de 4 WARN ONLEESBAAR weg); #14 laag 1 «Is dat het aantal fietsen en bakfietsen?», laag 2 zonder 'eerste/tweede soort', vlag 'bakfietsen' | ✓ gesloten |
| Oef-#431 / #432 | Oefeningen | DENK-02 #2 (speelveld) en #3 (omcirkeld): regels passen, geen 'gekleurd'/'sportveld' in de teksten | ✓ gesloten |
| Z-#606 | Oefeningen | batch 3 ronde 3d: ouderzin GET-04 nrO 8 «… keer honderd door de komma twee plekken te verschuiven, en zet er een nul bij …» (alle 4 items keer honderd met één decimaal); guard in b3/check | ✓ |
| batch 5 | Oefeningen | ronde 1b: 297 van de 513 sleutels op 'andere fout' naar regels (zie Oef-#444/#450); VERH-02 #3 (213) wacht op Oef-#445: de sleutels '36%' (het deel, 105), 'n − d' (100) en 8 losse staan niet in claudeFoutHints, en geen motorregel leest '%' | deels |


### Review batch 5 (Didactiek, build 13:48:53, taal: fix; review-batch5-didactiek.md)

| # | Wat | Status |
|---|---|---|
| LET OP MEET-04 #5 | 'teken-vergeten' stuurde naar de verkeerde temperatuur | ✓ eerst tijdelijk uit (13:55), daarna Oefeningen ronde 1c V-#660/Z-#660 (13:57), build 13:59:15 |
| V-#668 | 81 'tien keer ernaast' kregen bij een motor zonder #445 de tekst van 'het deel zelf' | ✓ eigen motorregel 'fout = tien keer het procent (als %)' (antwoord × 10 of : 10, sluit het deel en geheel min deel uit) + ronde 1c (bron nieuw, volgorde); build 13:59:15: 81/105/108/140 elk op de eigen soort |
| Z-#668 | punt als komma, geen halve stukjes | ✓ build 13:59:15 (zie Oef-#446) |

## Oefeningen 8 okt: ronde 1f (batch 4), 1h (batch 1), 3e (batch 3), 1c-deel 1 (batch 5): recheck-batch3-4 en review-batch5 van Didactiek
- **V-#660 ✓** (patch_batch5 R1C): MEET-04 #5 'onder nul' (teken-vergeten) is terug met laag 1 «Dat is onder nul. Hoeveel graden het warmer is geworden, is een aantal graden: dat is nooit onder nul. Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.» Laag 2: «Van de temperatuur onder nul tot nul zijn evenveel graden als het getal na de min. Tel daar de graden van nul tot de nieuwe temperatuur bij op.» Het tijdelijke blok van Overzicht (13:55) is vervangen; de labelloze 'aantal met een min' is in #5 weg (Z-#660, les 183). Guard b5: 'zonder min' alleen bij sleutel = −antwoord.
- **V-#668 ✓** (patch_batch5 R1C): VERH-02 #3, de drie motorregels van Oef-#445 hebben nu bron 'nieuw' (een motor zonder Oef-#445 leest ze niet → 0 sleutels in plaats van 'alle vrije Claude-sleutels'), en 'tien keer ernaast' staat vóór 'het deel zelf'. Getest met motor 13:47:51 en de huidige. Guard b5: 'het deel zelf' nooit antwoord × 10 of : 10.
- **V-#645 ✓** (patch_batch4 R1F): MEET-03 #9/#10 laag 2 'alleen de bodem' → «De bodem is één laag. De hoogte (of de diepte) zegt hoeveel lagen er op elkaar liggen. Doe de bodem keer de hoogte: dat is de inhoud.» (#10 zonder 'of de diepte'). Eigen vondst (les 197): dezelfde 'keer …: zoveel laagjes' in MEET-03 #2 (H2, laag 2 'maten opgeteld', laag 2 'een laagje ernaast'), ook herschreven. Guard b4: 'zoveel lagen/laagjes' na 'keer' in dezelfde zin is FAIL.
- **Z-#646 ✓** (b4/check): guard op betekenis: een zin in GET-05 nrO 6/7 met 'noemer' + groot/klein/groter/grootste/kleiner/kleinste/meeste/minste is FAIL, behalve 'noemers gelijk' en 'zegt nog niet'. Mutanten A4, A4b en een derde omschrijving: gevangen.
- **Z-#647 ✓** (patch_batch3 R3E): GET-03 nrO 3/4 «in de kolom ervoor» (H2 en laag 2). De V-#615-zin leest: «…, en het cijfer in de kolom ervoor één minder. Is het cijfer in de kolom ervoor een nul? Dan wordt die nul een negen, en leen je verder naar links.» Guard b3: geen 'op de kolom'.
- **Z-#648 ✓** (R1F): MEET-03 #9, elke tekst die de hoogte noemt, noemt ook de diepte (laag 1, laag 2, ouderzin). Guard b4 over alle teksten.
- **Z-#649 ✓** (patch_batch1 R1H): DENK-02 #9 «Heb je het aantal eieren in één doos en het aantal dozen bij elkaar opgeteld? …» (als vraag, les 161). Dezelfde zin in DENK-02 #8 («één rij en het aantal rijen») gevonden met de nieuwe guard en ook herschreven («het aantal knikkers in één rij»).
- **Z-#650 ✓** (R1F): GET-05 nrO 4, H2 en beide laag-2-stappenplannen: «Is er geen heel getal? Zet dan een nul voor de komma.» Guard b4 per item (antwoord onder één).
- Lessen 196–200 (recheck-batch3-4) en 201–208 (review-batch5, daar 200–207) staan in hints/lessen_g7.md.

## Oefeningen 8 okt: batch 5 ronde 1c, vervolg (V-#661–#663, Z-#660–#671; data build 14:04:32/14:05:43)
- **V-#661 ✓** MEET-04 #1 '± 1' laag 1: «Je zit er één graad naast. Tel eerst omhoog tot nul. Hoeveel graden blijven er dan nog over? Zoveel graden boven nul wordt het.» Alle items van #1 tellen omhoog door nul (les 181-check), dus geen splitsing nodig. Guard (les 201): geen 'tel ze (dan/bij elkaar) op' in #1/#3.
- **V-#662 ✓** VERH-02 #1/#2 H2 + laag 2: «Vijf procent is de helft van tien procent» / «Vijf procent is daar de helft van». Ook #5 (75%, Z-#669: voorbeeld nu 'twintig procent is twee keer tien procent') en #7 (25/30/50%: «tien procent is een tiende deel van de prijs; neem dat zo vaak als nodig. Vijftig procent is de helft, vijfentwintig procent een kwart.»). Guard b5 per item (les 203): het procent uit de vraag moet te maken zijn met de stukken die H2 en elke stappen-laag 2 noemen (#1, #2, #4, #5, #7).
- **V-#663 ✓** VERH-01 #7: H1 van Didactiek; laag 1 keersom/plussom/andere fout van Didactiek. H2 noemt de dubbele punt NIET (les 144: dan blijft één optie over), maar schrapt alleen het plusteken: «Bij een schaal tel je niets op: het teken is geen plusteken. Welk van de andere tekens staat er tussen de twee getallen?» → keerteken en dubbele punt blijven. Laag 2 noemt de dubbele punt.
- **Z-#660 ✓** labelloze regels weg in MEET-04 #1/#3/#5 en VERH-02 #4/#7; MEET-04 #2: 'de twee temperaturen opgeteld' (35 sleutels, −p + q), waardetekst «Dat is onder nul. …».
- **Z-#661/#662 ✓** MEET-04 #7 laag 1 'twee dagen te weinig' (dubbele vraag) en laag 2 'hele beginmaand' («de maand waarin je begint»).
- **Z-#663 ✓** VERH-01 #3 H2 milder. **Z-#664 ✓** VERH-01 #4/#5 voorbeeld 'een op vijftig'; #4 H2 «Hoeveel centimeter echt hoort bij één centimeter op de tekening?». Guard les 207 (voorbeeld ≠ getal in een afleider).
- **Z-#665 ✓** VERH-02 #2 'het procent uit de vraag' (fout = getal1, als vraag) vóór 'tien keer te groot'. **Z-#671 ✓** VERH-02 #1 soort 'wat overblijft (het hele getal min het goede deel)', volgorde gelijk.
- **Z-#670 niet gedaan:** bank-009 van VBN-04 #1 heeft geen eigen route in de data die alleen dat item raakt (een letterlijke '10' raakt ook bank-010/011). Wacht op Overzicht (Oef-#450).
- **Datapunten (Overzicht):**
  - **Oef-#456** VERH-01 #4 opties «De tekening is 100/2 keer zo klein» (Z-#664): data, beter «Het echte voorwerp is … keer zo groot».
  - **Oef-#457** build 14:05:43: nog 6 items MEET-04 #3/#5 met vorst binnen (bank-015, 019, 021, 023, 024 kleedkamer, 025 huis; V-#666, les 208).
  - **Oef-#458** check_merge_notatie FAIL V-#665: VBN-04 bank-032 heeft nog gelijke hoogste staven (40, 40) in 14:05:43.
| V-#664 | MEET-04 #3 bank-044 antwoord = voorbeeld | ✓ build 14:08:50: 5 en 9 → −4 (sleutels '4', '−5') |
| V-#665 | VBN-04 #2 gelijke hoogste staaf | ✓ build 14:07:01 (zie Oef-#447) + check |
| V-#666 | contexten | ✓ build 14:08:50: MEET-04 nrO 3/5 16 items binnen → in het bos/park/de tuin/het veld (kop houdt 'in [plek]'); VERH-02 #4 tanden → ballonnen (klas); #5 tanden → kopjes, vissen → emmers, blaadjes → bekers, eieren → vazen; #7 wortel → jas (€60 25%, €70 30%) |
| V-#667 | balk kleuren stukjes | ✓ build 14:08:50 (zie Oef-#449) |
| Z-#666 (#7) | 50% korting | ✓ build 14:08:50: jas €60 50% → 25% (€45), pion €20 50% → puzzel €20 25% (€15) |
| Z-#607 (besluit) | GET-02 'Rond af op één cijfer achter de komma', '2' bij 2,0 | ✓ build 14:12:17: motorregel 'fout = decimaal-nul weggelaten' (alleen bij 'Rond af … op één/twee/drie cijfer(s) achter de komma' en een antwoord dat op 0 eindigt; de sleutel blijft ondanks gelijke waarde; alleen die regel past; 'Bijna!' mag, BIJNA390 slaat de regel over). GET-02 #3 (batch 3, patch_batch3 blok Z-#607): regel vooraan, teksten letterlijk van Didactiek. Raakt in G5–G8: 12 items met zo'n vraag (alle G7 GET-02 #3), 2 met antwoord op 0 (bank-001, bank-006 → sleutel '2'); G5/G6/G8 0 items, G5/G6 regressie 0 anders. README (repo §Invoer tolerant en g7/README §App-eis): uitzondering erbij |
| Z-#665 (#1) / Z-#666 (#6) | x% van 100; omgekeerd delen | ✓ build 14:17:46 (zie Oef-#451) |
| Z-#667 | vuistregels in eenzijdige data | ✓ build 14:22:08: VBN-04 #3 opties bij 4 van 8 items anders (bank-014/019: antwoord, +10, +20 → goed = kleinste; bank-015/017: −20, −10, antwoord → goed = grootste); '± 20' valt nog op 'andere fout' (voorstel Oefeningen: regel 'twee tientallen te hoog/te laag'). VERH-01 #1 bij 5 van 12 items een ander stukje (200/70%/10 → 14 van 20; 300/40%/60 → 2 van 5; 500/20%/25 → 4 van 20; 200/60%/40 → 3 van 5; 400/75%/100 → 3 van 4), jsRender 'delen' = N : M |
| Z-#651 | GET-05 #1/#2 noemer-truc | ✓ build 14:22:08: nog 89 items (bevroren/z651_ids.json: grootst 53, kleinst 36) als tegenvoorbeeld via de Z-#630-maker; truc werkt nu in 95/190 (grootst) en 64/128 (kleinst) = 50% |
| Z-#664 (Overzicht-deel) | VERH-01 #4 opties «… keer zo klein» | ✓ build 14:25:42: bank-002 (enige item met deze opties; #5 heeft ze niet): «De tekening is 100/2 keer zo klein» → «Het echte voorwerp is 100/2 keer zo groot», goed antwoord → «Het echte voorwerp is net zo groot als de tekening» (zelfde zinsbegin, geen opvallende optie); literal-regels in de entry mee (patch_batch5, blok Z-#664), teksten van Oefeningen ongewijzigd |

## Oefeningen 8 okt: batch 5 ronde 1d en batch 6 (live build 14:22:08 / 14:25:42, les 194)
**Batch 5 ronde 1d** (`hints/patch_batch5.py`, blok R1D; log 42, tweede run 0):
- **Z-#667 / VBN-04 #3:** 'twee tientallen te laag' (fout = antwoord − 20, laag 1 «Dan past de hoogste staaf er niet op …») en 'twee tientallen te hoog' (fout = antwoord + 20, «Dan past alles wel, maar het kan lager. …») na 'een tiental te hoog': 2 + 2 sleutels, 0 op 'andere fout'.
- **Z-#660 ✓ (helemaal):** MEET-04 #2 'de twee temperaturen opgeteld' is nu een benoemde regel: Claudes label van precies die 35 sleutels (−p + q) is 'nul-fout-tientallen' (naam past niet, waarde wel); de labelloze regel is weg. Een motorregel kan het niet: de motor laat negatieve waarden vallen. Geen labelloze regel meer in batch 5 behalve VERH-01 #2 ('elk stukje tien procent', de helft).
- **Z-#670 ✓:** VBN-04 #1 'andere dag' (Claudes 'grafiek-verkeerd-afgelezen'; de andere '10'-sleutels met dat label pakken 'getal uit de vraag' en '± 1' eerder): alleen bank-009 '10' (ma 50 : 5). Laag 1 «Dat zijn de stukjes van een andere staaf uit de tabel. Zoek het getal bij de staaf uit de vraag.» (zonder 'dag': ook maanden). Oef-#450 is daarmee klaar.
- **VERH-01 #1 H1 (les 147):** 'van alles in de pot' → «van het hele aantal» (alle items zijn potten). Geen vast aantal stukjes in de teksten (balken van 20/5/4: H2 rekent per item, nagespeeld).
- **Z-#607 (Overzicht):** de regel 'decimaal-nul weggelaten' in GET-02 #3 botst niet met mijn regels (eigen sleutel, staat vooraan); b3/check heeft er een check voor (2 sleutels, mutant gevangen).
- **Data nagekeken:** V-#664 (bank-044 5 en 9 → −4) ✓; V-#665 (bank-030/032) ✓, merge-notatie ALLES OK, **Oef-#458 klaar**; GET-05 nrO 6/7 (Z-#651): truc in 95/190 en 64/128, V-#630/Z-#630/Z-#646-guards FAIL 0. **Oef-#457:** nog 3 items MEET-04 #3/#5 met vorst in de schuur (bank-016, 022, 040); een schuur kan vriezen, dus voor mij goed, Didactiek beslist (les 208).

**Batch 6** (`hints/make_batch6.py`, `hints/batch6.json` in de sync sinds build 14:22:08, `hints/patch_batch6.py` ronde 1b; zie `review-batch6.md`):
- Ronde 1b (Overzicht 14:26, letterlijke regels lezen niet bij de andere items): VERH-04 #5 nu Claudes labels ('getal-overgenomen' = het deel zelf, 'procent-verkeerde-basis' = het hele aantal, 'andere-deel-genomen' = het andere deel); alleen '14%' blijft letterlijk (label 'getal-overgenomen', maar '1 op de 4' → '14' is geen getal uit de vraag). De %-regels van Oef-#445 helpen hier niet: ze vragen 'D van G' in de vraag ('1 op de 4', '5 daarvan', 'Schrijf 0,7 in procenten' hebben dat niet). VERH-04 #2 '0,7%'/'0,9%'/'0,3%' blijven letterlijk: die sleutels staan niet in claudeFoutHints (Oef-#453).
- **Datapunten (Overzicht/Leerlijn):**

| nr | voor | wat | stand |
|---|---|---|---|
| Oef-#452 | Overzicht (data) | VERH-03 #1/#2: veel claudeDenkfouten staan niet in claudeFoutHints (530 van 662 en 446 van 528), dus routes als b × c, erbij optellen en ± de prijs van één worden nooit sleutels | ✓ build 14:35:51: oorzaak G4-regel D12b (sjabloontekst «Maak een verhoudingstabel.» / «Dat getal staat al in de som.» viel weg, en daarmee de sleutel). fixlijst_g7 _v452 zet 976 sleutels in VERH-03 terug (uitleg None). 547 daarvan (label 'verhoudingstabel-verkeerd': €8 bij 6 pennen €3 → 11, 72 bij 4:9=8:?) staan nu op 'andere fout': Oefeningen kan een regel 'Claudes sleutel: verhoudingstabel-verkeerd' maken |
| Oef-#453 | Overzicht (data/motor) | VERH-04 #1 (109) en #2 ('0,7%', '0,9%', '0,3%'): Claudes '%'-sleutels met 'getal-overgenomen' staan niet in claudeFoutHints; de motor leest geen '%' buiten 'D van G'. Nu 'andere fout' (#1, algemene aanpak) en letterlijke regels (#2). Voorstel: sleutels in claudeFoutHints, of 'tien keer het procent (als %)' en een regel 'kommagetal met procentteken' ook zonder 'D van G' | ✓ build 14:41:45: zelfde oorzaak als #452 (D12b); _v452 zet ook in VERH-04 de sleutels terug (109 in #1, 3 in #2). Motor (alleen KOMMA437, G5/G6 0 anders): #445-regels lezen ook 'D/G' ('32/50' → het deel zelf 32%, geheel min deel 18%), 'tien keer het procent (als %)' ook zonder deel; nieuw 'fout = kommagetal met procentteken' en 'fout = getallen achter elkaar (als %)'. patch_batch6 (blok Overzicht): #2 drie letterlijke regels → één motorregel, #5 '14%' → motorregel; tekst ongewijzigd. 'regel niet te lezen' in VERH-04 weg. Open voor Oefeningen: VERH-04 #1 '32%' staat op 'andere fout' (109): een regel 'fout = het deel zelf (als %)' met eigen tekst pakt ze nu |
| Oef-#454 | Didactiek/Overzicht | VERH-03 #4/#6: «k keer zo groot» = elke zijde k keer zo lang, terwijl de oppervlakte in #6 k × k groeit; VERH-03 #17 legt alleen 1 : 100 uit, maar vergelijkt 1 : 10 en 1 : 100 | ✓ build 14:58:27: #6 via V-#704 («Elke zijde van een vierkant van z bij z cm wordt k keer zo lang. …»; 3×3/k4 → 16, 5×5/k4 → 16, 4×4/k3 → 9; kop mee). #4 blijft (Didactiek: goed). #17 via Z-#704 (geen 'Dat betekent'-zin meer) |
| Oef-#455 | Overzicht (data) | VERH-04 #5 bank-125: optie '40%' zonder Claude-route (geen denkfout); blijft op 'andere fout' | ✓ build 14:58:27: bank-125 '40%' → '4%' (het hele aantal als procent, label procent-verkeerde-basis; soort 'het hele aantal') |
| Oef-#459 | Overzicht (data, les 206) | VERH-04 #2: in 5 van 8 items is het antwoord de middelste optie (opties × 10 en : 10); VERH-03 #13/#15/#20/#22/#23 (één item) ook | ✓ build 14:58:27: VERH-04 #2 bank-008 '500%' → '0,5%' (nu 4 van 8 midden, 4 grootste); VERH-04 nrO 4/7 via Z-#564; VERH-03 #13/#15/#20/#22/#23 (één item per somtype) niet: Didactiek Z-#711 'data hoeft nu niet'. Nieuwe check tools/optie_positie_check.py (WARN, G7/G8): plek op waarde, of de letter als het item niet husselt; vraagzinnen met grootst/kleinst tellen niet. G7 0 WARN; G8 2 WARN (MEET-V01, VERH-E06), G4/G5/G6 niet aangehaakt (ter info 2/6/2) |
| Z-#564 | Leerlijn (optie b, steering 14:33) | VERH-04 nrO 4/7: getelde vorm is goed. bank-127: A 5 op de 15 · B 5 op de 20 (goed) · C 1 op de 5; bank-136 (rad): A 3 op de 12 (goed) · B 1 op de 3 · C 3 op de 9; «1 op de 4» weg (blijft geldig antwoord, zoals bij 131/137); claudeUitleg geteld; uitleg bij 1 op de 5 / 1 op de 3 (ging over vereenvoudigen) → None. De andere items hadden al de getelde vorm. Posities (Oef-#459): bank-131 → C, bank-137 → B; nrO 4 nu A2 · B3 · C2, nrO 7 A1 · B1. bank-134 '2 op de 10' en bank-135 '1 op de 6' hebben geen Claude-route | ✓ build 14:44:30 (fixlijst_g7 _z564); Oefeningen kan #4/#7 schrijven |
| – | Leerlijn | VERH-04 #4 (deel van een totaal) en #7 (rad) wachtten op Z-#564 | klaar (batch 6; Z-#751) |

Nummering: volgende vrije Oef-#460 (zie onder: Oef-#460–#463 staan in g4/merge-fixlijst.md).


### Oefeningen 8 okt: batch 5 ronde 1e
- Geen nieuw punt: Z-#664 laag 2 van VERH-01 #4 zonder de gelijk-regel (review-batch5.md, ronde 1e).
- Oef-#460–#463 gebruikt in g4/merge-fixlijst.md (G4 batch 5, GET-E05). Nummering: volgende vrije Oef-#464.

## Oefeningen 8 okt: batch 6 ronde 1d (review-batch6-didactiek.md, taal: fix) en batch 4/5 zacht (recheck-batch4-5-didactiek.md)
- Live build 14:41:45 (en 14:44:30, batch6.json gelijk): b6/check **660 FAIL** → na ronde 1d in de zandbak (kopie live + patch, sync/apply): **FAIL 0**, check_hints 153 klaar · 0 FAIL · 0 WARN, merge-notatie ALLES OK, hint-sync = live batch6.json; tweede run patch_batch6 = 0. Mutanten 87, gemist 0 (nieuw: M215, M216, M217, M218, M220, MV700, MV700b; les 223).
- **V-#700 ✓** VERH-03 #1 labelregel 'verhoudingstabel-verkeerd' (202: b + c − a of b × c, vraagtekst); VERH-03 #2 labelregel (345: antwoord ± prijs van één, prijs ± verschil in aantal; let op: 14 sleutels zijn *prijs − verschil* bij minder stuks, daarom «opgeteld of ervan afgehaald»); VERH-04 #1 'fout = het deel zelf (als %)' (57, teller%) en label 'getal-overgenomen' (52, noemer%). Elk met eigen laag 2. b6/check telt 57/52; VERH-04 #1 van de WACHT-lijst (les 221); checks voor R453-regels erbij.
- **V-#701 ✓** 'één keer te veel/te weinig' als vraag (ook de additieve route); laag 2 zonder 'niet één keer meer/minder'. Guard les 216: stellige ±-tekst op een additieve sleutel = FAIL.
- **V-#702 ✓** 'opgeteld' in #9/#15/#23/#24 zonder uitgesloten bewerking; #14 'erbij in plaats van keer' ook zonder «niet om erbij»; G7 batch 5 VERH-01 #7 H2 «Bij een schaal tel je niets op» → «Het teken bij een schaal is geen plusteken.» (patch_batch5 ronde 1f). Guard les 217 in b5- en b6-check. #19/#21 «in centimeters, niet in meters»: waar volgens de vraag; laag 1 nu met de omrekening.
- **Zacht ✓:** Z-#702 (#16), Z-#703 (tweeduizend; guard les 220 op tussenuitkomsten), Z-#705 (H2 #1 via de rol: 'in de verhouding met/zonder vraagteken'), Z-#706 (H1 #2), Z-#707 (H2 #15), Z-#708 (#6 laag 2 en H2; #14 laag 2), Z-#709 ('geeft de tienden'), Z-#710 (tussenstap: «Deel dan eerst de teller en de noemer door hetzelfde getal, tot de noemer wel in één keer naar honderd gaat»; per item nagerekend, 21 items). Z-#700/#701/#704/#711/#712: Overzicht.
- **Wacht op data (Overzicht):** V-#703 (6 items antwoord uit de vraag; b6/check WACHT met eigen reden-toets, les 215), V-#704 (#6 vraagzin), V-#705 (bank-297 '100 000'; WACHT, les 218). Na hun build: b6/check op live opnieuw.
- **Batch 4/5 zacht:** Z-#680 ✓ (b4/check: stam-guard noemer + 'getal onderaan/onder de streep'; 'zoveel lagen' over de hele tekst, laatste bewerking telt; N3/N4/N5/L2 nu gevangen, baseline FAIL 0). Z-#681 ✓ (b5/check les 195 ook #2: bank-540 → INFO). Z-#682 ✓ (gelijk-guard re.I, H1/H2/L1/L2, hetzelfde/evenveel/even groot/net zo groot; VERH-01 #7 telt opties na H1 + H2; contextwoorden ook uit de data als INFO-lijst, les 212). Mutanten G1/G2/G3/S7/U1 gevangen.

| # | Voor | Wat | Status |
|---|---|---|---|
| Oef-#464 | Overzicht (README) | Z-#683: g7/README §App-eis keurt bij «Rond af op één cijfer achter de komma» alleen *minder* cijfers af; '2,00' / '3,80' tellen als goed (les 214). Niet ons bestand. | **✓ Overzicht 15:14:** README §App-eis: alleen precies het gevraagde aantal cijfers achter de komma is goed (minder én meer fout); '2,00'/'3,80' krijgen nu de algemene fout-hint (eigen sleutel kan Oefeningen nog voorstellen). |

| Oef-#465 | Overzicht (sync/bevroren) | **VERH-04 #4/#7 (Z-#564) klaar, maar niet in batch6.json.** `bevroren/somtype_nr_v2.json` heeft onder `G7-VERH-04#4` nog 9 claudeIds, waarvan de 2 rad-items (bank-136/137) sinds v6 onder `#7` staan. sync_hint_keys kiest de eerste passende versie (v2) → «items verdeeld over {#4: 7, #7: 2}» → check_hints FAIL (regel #30). Voorstel: v2-entry #4 zonder de 2 rad-ids, of sync laat ids die een latere versie aan een ander nrOrigineel geeft weg. patch_batch6 ronde 1c toetst dit zelf (alleen lezen) en zet de entries erin bij de eerste run nadat het is opgelost. In de zandbak (entries erin): b6/check #4/#7 FAIL 0 (4 labels nagerekend, 2× algemene tekst), alleen check_hints FAIL op de koppeling. | **✓ Overzicht 15:10:** opgelost in `bevroren/somtype_nr_v2.json`: entry `G7-VERH-04#4` zonder de 2 rad-ids (573dac2a…, 75a6fe75… = bank-136/137), met veld `correctie` en een regel in de uitleg; sync_hint_keys ongewijzigd (een algemene regel 'latere versie wint' klopt niet: 35 andere ids staan in een latere versie onder een ander nummer, maar zitten nu weer onder hun oude nrO). README §Sleutels bevroren bijgewerkt. Build 15:10:21: patch_batch6 zette de entries #4/#7 erin (24 wijzigingen), check_hints **155 klaar · 0 open · 0 FAIL · 0 WARN**, b6/check op live 779 items · 3130 sleutels · FAIL 0. Geen item van somtype verschoven. |
| Oef-#466 | Overzicht (data, les 195) | VERH-03 #1 na V-#703 (build 14:58:38): in 3 items is het verschil van de twee getallen vóór en achter de eerste dubbele punt het antwoord: 8 : 2 = 24 : ? (6), 10 : 2 = 40 : ? (8), 6 : 2 = 12 : ? (4). Een kind dat aftrekt is daar toevallig goed. | **✓ Overzicht 15:13 (build 15:13:54):** fixlijst_g7 `R6_466`, zelfde k, nieuwe drietallen die nog niet in de bank staan: bank-423 → 12 : 5 = 36 : ? (15; sleutels 180 = c × b, 36), bank-559 → 12 : 5 = 48 : ? (20; 41 = b + c − a, 12), bank-590 → 4 : 12 = 8 : ? (24; 4, 6 = b : k gedeeld). a − b is nergens het antwoord of een Claude-sleutel. **Oefeningen: hints van VERH-03 #1 opnieuw syncen/nakijken voor deze 3 items.** |

Na build 14:58:38 (V-#703/#704/#705, Z-#704): koppen VERH-03 #4/#6/#10/#12/#17/#20/#25 nagekeken (kopNagekeken), #12 laag 2 'in het model'; nieuwe regel 'verschil van twee getallen' in VERH-03 #1 (bank-352 «8 : 5 = 16 : ?»: Claudes label is daar 8 − 5, een derde route; de motor maakt het verschil nu bij elk item tot sleutel, 291). b6/check op een verse kopie van live: 770 items · 3112 sleutels · FAIL 0, geen WACHT meer (V-#703/#705 opgelost, VERH-04 #5 zonder 'andere fout'); check_hints 153 klaar · 2 open (VERH-04 #4/#7, Oef-#465) · 0 FAIL; mutanten 88, gemist 0.

Na Overzichts fix van Oef-#465 (build 15:10:21), nagekeken door Oefeningen op een verse kopie van live: patch_batch6 0 wijzigingen (de entries VERH-04 #4/#7 stonden er al), check_hints **155 klaar · 0 open · 0 FAIL · 0 WARN**, b6/check 779 items · 3135 sleutels · FAIL 0, mutanten 95 · gemist 0. runmut.sh slaat nu regels zonder sleutel over (REV is daar niet te toetsen): VERH-04 #7 'deel verkeerd geteld' heeft na de koppeling geen sleutel (geen item met label een-ernaast in #7); de regel blijft staan en doet niets.

Nummering (tot 15:20): volgende vrije Oef-#481 (Oef-#467–#480 staan in g8/merge-fixlijst.md, G8 batch 1 en 2).

## Oefeningen: G7 batch 6 ronde 1e (recheck-batch6-didactiek.md, taal: ok, build 15:13:54), 8 okt 15:3x

`hints/patch_batch6.py` ronde 1e: Z-#742 (VERH-03 #15 H2 met een echte stap, les 244), Z-#743 (#14 'erbij in plaats van keer' L1), Z-#740 (VERH-03 #1 'verschil van twee getallen' als vraag met beide routes: in bank-333 en bank-441 is het verschil ook de som van twee getallen uit de vraag), VERH-04 #7 'deel verkeerd geteld' weg (geen sleutel). Eerste run 4 wijzigingen, tweede run 0.
Checks: z-#741 gedeelde guard `/workspace/g7work/huis_checks.py` (les 217, bredere regex) in b1–b6/check.py; b6/check les 216 breder (elke sleutel die ook c − a + b of de som van twee getallen uit de vraag is, op 'één keer te veel/te weinig', 'verschil van twee getallen' en 'gedeeld': laag 1 = vraag die de optelroute noemt). Mutanten D216a/b, D217a–c erbij. Verse kopie van live (build 15:13:54) + sync/apply: check_hints 155 klaar · 0 open · 0 FAIL · 0 WARN; merge-notatie ALLES OK; b6/check 779 items · 3135 sleutels · FAIL 0; b1–b5/check FAIL 0; runmut 100 mutanten, 0 gemist, 0 ONGEBRUIKT.

| # | Voor | Wat | Status |
|---|---|---|---|
| Oef-#481 | Overzicht (data, Z-#744) | VERH-03 #1: (a) toevallige treffers (les 195/241): in 39 items is een som of verschil van twee getallen het antwoord (b+c 10, a+c 8, c−b 7, c−a 7, a+b 7), ook in twee vervangers uit V-#703: bank-318 (9 : 6 = 18 : ? → 12 = 18 − 6) en bank-620 (3 : 4 = 12 : ? → 16 = 4 + 12). Voorstel Didactiek: vervang minstens de 14 verschil-gevallen en 318/620. (b) In somtypen/G7-VERH-03.md staan op 2 plekken nog Claudes oude fout-hints met '1 cm is 100 000 cm echt…'; in gemapt.json 3× '100 000' (geschiedenis, origineel veld, reden). Een kind ziet het niet; opruimen is netjes. (c) Bij een vervanging: b6/check les 216 toetst elke nieuwe som/verschil-treffer op de teksten. | open |

Nieuw gevonden met de gedeelde les-217-guard (buiten G7, ter info): G4 GET-E06 #5 «Je mag niet zomaar optellen.» en #6 «Je moet de kleren niet bij elkaar optellen.» (laag 1 'opgeteld'). Bij combinaties is herhaald optellen een geldige route; tekst nog niet aangepast (volgt na akkoord, G4 hoort niet bij deze ronde).

Nummering: volgende vrije Oef-#485 (Oef-#482–#484 staan in g8/merge-fixlijst.md, G8 batch 1 ronde 1b).


## Review batch 6 (Didactiek 8 okt, build 14:41:45; review-batch6-didactiek.md) — door Overzicht, build 14:58:27

`scripts/fixlijst_g7.py` → `_r6` (+ `_opt_vervang`). G5/G6 0 verschil (checks ALLES OK). **Oefeningen synct na deze build** (V-#700/#701/#702 zijn tekst).

| # | Wat | Gedaan |
|---|---|---|
| 'Kleur 5%' (VERH-01 #2) | Didactiek akkoord met schrappen | ✓ bevroren/geschrapt_review5.json is definitief |
| V-#703 | VERH-03 #1, antwoord = getal uit de vraag (6 items) | ✓ bank-318 9 : 3 = 27 → 9 : 6 = 18 (12) · 352 8 : 2 = 32 → 8 : 5 = 16 (10) · 518 10 : 2 = 50 → 4 : 3 = 8 (6) · 531 4 : 2 = 8 → 7 : 5 = 14 (10) · 545 6 : 2 = 18 → 5 : 3 = 10 (6) · 620 8 : 4 = 16 → 3 : 4 = 12 (16); geen van zessen al in de bank; Claudes sleutels mee met hun route. Guard: tools/antwoord_in_vraag_check.py 'verhouding' (FAIL, G5–G8; G5/G6/G8 0) |
| V-#704 (= Oef-#454) | VERH-03 #6 vraagzin | ✓ zie Oef-#454; zijde en oppervlakte nooit k of k × k (assert) |
| V-#705 | VERH-03 #20 bank-297 «1 : 100 000» | ✓ «1 : 100.000» in opgave, claudeUitleg en Claudes fout-hint. Nieuwe check tools/spatie_duizend_check.py (FAIL) in check_merge_notatie G4–G8: overal 0 |
| Z-#681 | VERH-02 #2 bank-540 25% van €20 = 25 − 20 | ✓ 25% van €80 = €20 (sleutels €80, €2; antwoordOokGoed 20,00) |
| Z-#700 | vaste motorregels voor de routes bij verhoudingen | niet gedaan (motor + G5/G6-regressie; volgende ronde) |
| Z-#701 | toevallige treffers VERH-03 #2/#4/#5, VERH-04 bank-089 | niet gedaan (volgende dataronde) |
| Z-#704 | schaal: #17 één schaal uitgelegd; #10/#12/#25 'tekening' bij een model | ✓ #17 zonder 'Dat betekent'-zin; bank-268/277/302 «1 cm in het model» (koppen mee, sync op claudeId) |
| Z-#710 | noemers 15/35/45 VERH-04 #1 | niet gedaan |
| Z-#711 | middelste optie / eenzijdige data | deels: VERH-04 #2 (Oef-#459); VERH-03 #1 'c > a' niet |
| Z-#712 | VERH-04 #3 'kapot' | ✓ pakken → kopjes, kaartjes → tegels, stickers → borden, knopen → glazen, ballonnen → ruiten (lampjes blijft) |
| Oef-#457 | MEET-04 bank-016/022/040 vorst in de schuur | ✓ naar buiten (park, bos, tuin), zoals V-#666 |

### Na-ronde G7 (Overzicht, build 15:31:04)
Batch 6 is taal: ok (Didactiek, build 15:13:54); VERH-04 #4/#7 wacht nog op Didactiek.
| punt | wat | stand |
|---|---|---|
| V-#745 | bank-136 (#7, rad): '1 op de 3' en '3 op de 9' zijn even groot (deel : rest) | **✓ Leerlijn akkoord (8 okt 15:25).** fixlijst_g7 Z564/LAB745: A '3 op de 12' (goed) · B **'9 op de 12'** (andere-deel-genomen → 'het andere deel') · C '3 op de 9' (deel op rest). Waarden 1/4, 3/4, 1/3. |
| Z-#747 | bank-127 (#4): '1 op de 5' kwam uit het vereenvoudig-ontwerp | **✓ Leerlijn akkoord (8 okt 15:25).** A '5 op de 15' (deel op rest) · B '5 op de 20' (goed) · C **'15 op de 20'** (het andere deel). Elke afleider hoort nu bij één fout ('deel op rest' of 'het andere deel'); geen vereenvoudigde vorm meer in een optie (de vereenvoudigde vorm blijft wel in geldigeAntwoorden). 'deel achter op de' heeft in #4/#7 nu 0 sleutels (Z-#749: Oefeningen beslist). |
| Z-#744 (a) | VERH-03 #1: in 39 items is het antwoord een getal uit de vraag of de som/het verschil van twee getallen (ook bank-318/620 van V-#703) | **✓** fixlijst_g7 `R6_744` (_z744, na V-#703 en Oef-#466): 39 nieuwe drietallen met dezelfde k, niet in de bank, zonder zo'n treffer; Claudes sleutels met hun route (c × b, b + c − a, c, b, a, b : k, b × k ± b). Bij bank-318 viel de route b : k weg (geen heel getal). Nieuwe check `tools/som_verschil_check.py` (SOMVERSCHIL, WARN) in check_merge_notatie G7: **0**. |
| Z-#744 (b) | '100 000' in de oude Claude-fout-hints in somtypen/G7-VERH-03.md | **open** (niet zichtbaar voor een kind; opruimen bij de volgende ronde) |
| V-#746 | claudeStrategie 'deel vereenvoudigen' bij bank-127/136 | **✓ build 15:41:07** (zat niet in 15:31:04): `fix_g7 _r7` → 'gunstig van totaal' (zoals 129/131/132/137); de oude waarde staat in merge.extraVeldenVoorBesluit. |
| sleutels 3.130 / 3.135 | Oefeningen telde 3.135, Overzicht meldde 3.130 | **Uitgezocht:** zelfde telmethode (b6/check.py telt de foutHints van VERH-03/04). 3.130 was gemeten op build 15:10:21, vóór Oef-#466; 3.135 op build 15:13:54, ná Oef-#466. De drie nieuwe items (bank-423/559/590) hebben 7 + 7 + 5 = 19 sleutels tegen 5 + 5 + 4 = 14 ervoor: +5. Geen sync-verschil. Na deze build: **3.166**. |

Checks build 15:31:04: check_hints **155 klaar · 0 open · 0 FAIL · 0 WARN**, merge-notatie ALLES OK (SOMVERSCHIL 0), b6/check 779 items · 3.166 sleutels · FAIL 0. 41 items anders (VERH-03 #1: 39, VERH-04 #4: 1, #7: 1); verder niets verschoven.
**Oefeningen opnieuw syncen:** VERH-03 #1 (39 items nieuwe getallen) en VERH-04 #4/#7 (bank-127/136 nieuwe afleider 'het andere deel').

### Na-ronde G7 (2): recheck VERH-04 #4/#7 (review-verh04-4-7-didactiek.md, steering 15:37) — build 15:41:07
| punt | zat in 15:31:04? | stand |
|---|---|---|
| V-#746 | nee (stond open) | **✓** claudeStrategie bank-127/136 → 'gunstig van totaal'; oude waarde in merge.extraVeldenVoorBesluit. |
| Z-#748 | nee | **✓** bank-134 (ea6380a4): «… een getal groter dan 7?» → **3 op de 10**; opties A 4 op de 10 (een-ernaast) · B 7 op de 10 (het andere deel) · C 3 op de 10 (goed). bank-135 (a502ea00): «… de letter N?» → **2 op de 6**; opties A 2 op de 6 (goed) · B 1 op de 6 (2 ernaast, label andere-fout: b6/check telt 'een-ernaast' alleen bij ±1) · C 4 op de 6 (het andere deel). De goede optie blijft op dezelfde plek. Nieuwe check `tools/helft_deel_check.py` (HELFT, WARN) in check_merge_notatie G7: **0**. |
| Z-#750 | nee | **✓** bank-136 en bank-137: visual.nietLiveZonderBeeld = True (les 248). |
| Z-#751 | nee | **✓** bank-125 claudeUitleg «1 op 4 betekent» → «1 op de 4 betekent»; etiket '#4 (vereenvoudigen)' weg in hints/batches.md (rij 7, nu klaar), hints/make_batch6.py en merge-fixlijst rij 348. |

Checks build 15:41:07: check_hints **155 klaar · 0 open · 0 FAIL · 0 WARN**, merge-notatie ALLES OK (HELFT 0, SOMVERSCHIL 0), b6/check FAIL 0. 4 items anders (bank-125/134/135/136/137: 125 alleen de uitleg, 127 alleen de strategie, 134/135 opgave+opties, 136/137 de vlag).
**Oefeningen opnieuw syncen:** VERH-04 #4 bank-134 en bank-135 (nieuwe opgave, antwoord en afleiders) en #7 (nietLiveZonderBeeld; geen tekstwijziging).

## Oefeningen: G7 batch 6 ronde 1f (8 okt 15:4x; review-verh04-4-7, build 15:31:04/15:41:10)
- **Nagekeken (V-#745/Z-#747 in de data):** bank-136 '9 op de 12' → 'het andere deel' («Dat is het andere deel. … tel die vakjes.»), bank-127 '15 op de 20' → 'het andere deel'. Allebei kloppen ze, met het label andere-deel-genomen.
- **patch_batch6 ronde 1f:** de labelregels van VERH-04 #4/#7 blijven alleen staan als hun Claude-label nog in de items van dat somtype voorkomt. Daardoor is 'deel achter op de' (getal-overgenomen) weg in #4 en #7: na V-#745/Z-#747 had die geen sleutel meer. 'deel verkeerd geteld' blijft in #4 (134 '4 op de 10') en blijft weg in #7 (sinds 1e; Z-#748 raakt #7 niet).
  - De G7-build van 15:40/15:41 heeft dit al gedraaid. Live tweede run: 0.
- **Z-#749 wacht** op de volgende G7-build (V-#746, Z-#748), vlag `Z749_WACHT = True` in ronde 1f. Daarna komen er letterlijke regels 'deel verkeerd geteld (optie)' voor foute opties zonder label met 'k op de [totaal]' (k ≠ deel, k ≠ rest), berekend uit de data. Nu zijn dat 134 '2 op de 10' en 135 '1 op de 6'.
  - In de zandbak getoetst: beide landen op die soort, met predicaat + mutant M749.
- **Nieuw in b6/check.py:** les 245 (geen twee even grote 'k op de n'-opties, mutant M245) en een predicaat voor 'deel verkeerd geteld (optie)'. De les-216-mutanten (M216/D216a/D216b) maken nu zelf hun randgeval, want de build van 15:31 had geen additieve-route-sleutel meer (les 233).
- **Checks (verse kopie van live 15:41:10):** check_hints 155 klaar · 0 FAIL · 0 WARN; merge-notatie ALLES OK; b6/check 779 items · 3166 sleutels · FAIL 0; b1–b5 FAIL 0; runmut 99 mutanten · 0 gemist · 0 ongebruikt.

### Ronde 1e/1f (Oefeningen patch_batch6 15:40) + Z-#749 + Oef-#481 — Overzicht, build 15:52:17
- **Z-#749:** `Z749_WACHT = False` in patch_batch6 (na V-#746/Z-#748 in build 15:41:07). bank-135 '1 op de 6' heeft in de data geen Claude-label meer (Z-#748), dus de letterlijke regel 'deel verkeerd geteld (optie)' landt daar; bank-134 '4 op de 10' blijft op 'deel verkeerd geteld' (label een-ernaast). #7 heeft geen optie die erbij past (lijst leeg).
- **Oef-#481:** de oude Claude-fout-hint «1 cm is 100 000 cm echt» → '100.000' in de data (fixlijst `_z481`), in somtypen/G7-VERH-03.md (build_g7 schrijft de somtypen met punt) en in hints/batch6.json (claudeTekst). `spatie_duizend_check.rapport_bestanden` kijkt nu ook in hints/batch*.json en somtypen/*.md (FAIL, in check_merge_notatie G4–G8): overal **0**.
- Checks: check_hints **155 klaar · 0 open · 0 FAIL · 0 WARN** (ook LES250 0), merge-notatie ALLES OK, b6/check 779 items · 3.166 sleutels · FAIL 0.

### Oefeningen: Z-#749 nagekeken (8 okt 15:5x, build 15:52)
- Live (verse kopie 15:53): batch6 #4 heeft 'deel verkeerd geteld' (label een-ernaast) en 'deel verkeerd geteld (optie)' met de letterlijke regel '1 op de 6'; #7 alleen 'niet met het totaal', 'het andere deel', 'andere fout'. bank-134 '4 op de 10' → 'deel verkeerd geteld' (labelregel), bank-135 '1 op de 6' → 'deel verkeerd geteld (optie)'. Beide krijgen de tekst «Het totaal klopt. Tel het deel waar de vraag over gaat nog eens precies.»
- check_hints 155 klaar · 0 FAIL · 0 WARN; merge-notatie ALLES OK; b6/check 779 items · 3166 sleutels · **FAIL 0**; patch_batch6 op de kopie 0 wijzigingen. M749 staat weer in runmut.sh, nu op bank-135 (134 draagt sinds Z-#748 een label): **101 mutanten · 0 gemist · 0 ONGEBRUIKT**.
- Nummering: Oef-#485–#488 staan in g8/merge-fixlijst.md (G8 batch 3); volgende vrije Oef-#489, na #499 verder met Oef-#1000.

### Oefeningen: ronde 1g, alleen guards (8 okt ~16:05; recheck2-batch6-didactiek Z-#811/Z-#812)
- **Z-#811 (les 280):** b6/check les 216 eist nu 'erbij opgeteld' of 'bij elkaar opgeteld' in de vraag (niet alleen het trefwoord), en draait op elk somtype met de soorten ±1/verschil/gedeeld, niet alleen VERH-03 #1. Mutant **E216d** («Komt er nog iets erbij? …») in mut.py/runmut.sh: gevangen met kenmerk 'les 216'. b6/check FAIL 0; runmut **102 mutanten · 0 gemist · 0 ONGEBRUIKT**.
- **Z-#812a:** huis_checks.py UITSLUIT + de vier patronen van Didactiek («Je hoeft niets op te tellen», «Optellen is hier fout», «Gebruik geen plus» / «Dit is geen plussom», «Er komt niets bij»). Zelftest `python3 huis_checks.py --zelftest`: **11/11 gevangen, 0 vals alarm** (de 5 toegestane zinnen blijven vrij). Over alle 6 batches (zandbak én live): les 217 FAIL 0.
- **Z-#812c (les 281):** b1–b4 gaven hun batch niet goed door (b1/b2: dict per sleutel, b3/b4: D3). Nu geven b1–b6 allemaal de batch in het geheugen door (`{'somtypen': …}` of D3/D). Mutant per batch `HUIS217MUT=1` (zin in hint1 in het geheugen): in **alle 6 batches gevangen**, basis FAIL 0.
- **Z-#812b → Oef-#489 (Overzicht, tools/):** huis_checks staat nog in /workspace/g7work, dus de build-gate draait hem niet. Voorstel: `tools/huis_checks.py` (UITSLUIT + zelftest) en in de build-gate `les217()` over alle hints/batch*.json van G4–G8. Ik verander niets in tools/. **Open.**
  - 16:09: Oefeningen nam de patronen van Z-#824 op (G8 review-batch3, m7: 'is niet goed' en 'mag niet' bij aftrekken/eraf/delen/erbij, 'je mag hier niet optellen'). Zelftest 15/15, 0 vals alarm, G7 b1–b6 FAIL 0. Wat Overzicht doet (blijft **open**): `/workspace/g7work/huis_checks.py` overnemen als `tools/huis_checks.py`, met `--zelftest` in de gate. De batches geven hun data in het geheugen door, via `les217(batch_dict)`. In G8 b3 staat dezelfde uitbreiding als LES217B.
- Geen patch nodig: patch_batch6 blijft gelijk (tweede run 0).
- Nummering: volgende vrije Oef-#490 (na #499: Oef-#1000).

### Zacht (Didactiek 15:58) — Overzicht, build 16:02:05
- **Z-#810 ✓** somtypen/G7-VERH-04.md toont bij 127/136 (en elk item dat de fixlijst opnieuw opzet) de huidige Claude-sleutels: `_zet` zet nu ook foutHintsTekst (stond nog '1 op de 5 → … Kijk hoe vaak 5 in 20 past'). Alleen de md verandert; in de data zet apply_hints foutHintsTekst toch opnieuw.
- **Z-#812 ✓** `tools/les217_check.py` (kopie van g7work/huis_checks.py van Oefeningen, met de vijf nieuwe bewoordingen en de zelftest 11/11) zit in de build-gate check_hints: **FAIL in G7/G8** (0), **WARN in G3–G6** (goedgekeurd; alleen gemeld): G4 GET-E06 #5/#6 'niet zomaar optellen' / 'niet bij elkaar optellen' (2), G5 GET-E05 #13 'Aftrekken, niet optellen.' (1), G6 MEET-E03 #3/#4 'niets op te tellen', VBN-E02 #1 H2 'tel je de twee maanden niet bij elkaar op' (3). G3: 0.
- **Z-#744 (bank-318/620):** al in build 15:31:04 (R6_744): 318 = 9 : 5 = 18 : ? → 10, 620 = 2 : 12 = 8 : ? → 48; geen getal uit de vraag en geen som/verschil (SOMVERSCHIL 0).
Checks: check_hints 155 klaar · 0 FAIL · 0 WARN, merge-notatie ALLES OK, b6/check FAIL 0.

### GEMIDDELDE (Didactiek 8 okt 16:15, g8/gemiddelde-check-didactiek.md) — Overzicht, build 16:20:58
| punt | stand |
|---|---|
| V-#853 | **✓** GET-04 somtype 5 (nrO 6), gelijke som (les 307), in `fixlijst_g7._v853` (assert: som gelijk, antwoord gelijk, geen route geeft het antwoord): 427 «15, 11, 12, 9, 13» → **15, 11, 11, 10, 13** (60/12; mediaan 11, meest 11, middelste genoemde 11, midden 12,5; de sleutel 'middelste getal' komt terug: **11**), 861 → **14, 18, 7, 8, 3** (50/10), 863 → **11, 9, 15, 3, 2** (40/8), 864 → **3, 12, 14, 5, 11** (45/9). claudeUitleg: alleen de optelling. |
| Z-#854 | **✓** 428 «10, 9, 5, 19, 7» → **11, 8, 5, 19, 7** (50/10; mediaan 8, midden 12, middelste genoemde 5). Claudes mediaan-sleutel 9 → **8** (regel 'middelste getal' geeft nu 8). |
| Z-#855 | **✓** `tools/gemiddelde_check.py` met de vijf routes en het aandeel per somtype, in check_merge_notatie G7 (FAIL). Vóór: FAIL 2 (midden 4/11; 427 mediaan op de eigen sleutel 'middelste getal'), WARN 5. Na: **0 FAIL · 0 WARN**. |
Alleen deze 5 items zijn veranderd (vergeleken met de repo: 5 items anders, verder niets). check_hints 155 klaar · 0 FAIL · 0 WARN, merge-notatie ALLES OK. **Didactiek:** korte nacheck. **Oefeningen:** niets te syncen (de regels rekenen zichzelf opnieuw uit; L1's blijven waar).
