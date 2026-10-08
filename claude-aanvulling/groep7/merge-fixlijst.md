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
| Oef-#431 | Overzicht (data) | DENK-02 #2: zet 'omtrek' vast in de kop in plaats van [ding] (voorstel Didactiek Z-#563) | open |
| Z-#565 | Oefeningen | DENK-03 nrO 6 '8 dl' laag 2 in twee zinnen | ✓ 'Ronde 1d' |
| Z-#525 | Oefeningen | DENK-02 #3: 'gekleurd' (H2) en 'Kleur er één' (laag 2 'alle groepjes') weg. H2 «… Tel bij elke tekening hoeveel kinderen er bij de zandbak horen.» Regel 'alle groepjes gekleurd' → 'alle groepjes' (past ook bij 'omcirkeld'); soort 'alle groepjes'. Kleur-guard in b1/check, ook op omschrijvingen (les 158) | ✓ 'Ronde 1d'; verklap 0 FAIL |
| Oef-#432 | Overzicht (data) | DENK-02 #3 opties zonder kleur: «3 groepjes van 6, één groepje omcirkeld» · «3 groepjes van 6, alle groepjes omcirkeld» · «2 groepjes van 9, één groepje omcirkeld». Onze regels ('alle groepjes', '2 groepjes van 9') blijven passen | open |
| Oef-#433 (Z-#521) | Overzicht (data) | Contexten, alleen in de opgaven (onze teksten noemen geen aantallen). **DENK-02 #12** lantaarnpalen 5 m uit elkaar: (A) 20 m → antwoord 120 meter, afleiders 140 meter (palen in plaats van stukken) en 100 meter (stuk te weinig); of (B) 'hekpaaltjes' met 5 m (getallen blijven; wij zetten dan 'palen' → 'paaltjes' in de teksten). **DENK-02 #9** eierdoos van 8: 6 eieren → '5 × 6 = 30', afleiders '5 + 6 = 11' en '6 − 5 = 1' (Claudes label 'verkeerde-bewerking' houden op die optie). **DENK-02 #2** 'sportveld' van 20 bij 10 m → 'speelveld' (getallen en regels blijven; onze teksten zeggen 'veld'). **DENK-02 #14** 'fietsen met 3 wielen' → 'bakfietsen met 3 wielen' (onze teksten passen). De regelwijzigingen voor #12 (A) en #9 staan klaar in 'Ronde 1d' (als commentaar) | open |
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
| Oef-#435 | Overzicht (motor) | Regels 'fout = antwoord × 100 / × 1000 / : 100 / : 1000' (nu alleen × 10 / : 10). GET-01 #1: 593 sleutels (×100, ×1000, : 100, : 1000) vallen nu op 'antwoord ± 1 of meer' met een algemene tekst. Laag prioriteit | open |
| Oef-#436 | Overzicht (motor) | 'fout = antwoord ± 0,1 / ± 0,01' geeft geen sleutel bij een heel antwoord ('4,6 + 0,4 = 5' → '4,9'). GET-03 #1/#2 4 sleutels, GET-04 #1/#2 24 sleutels staan daarom op Claudes label 'net ernaast (heel antwoord)'. Voorstel: de regel ook bij een heel antwoord | open |
| Oef-#437 | Overzicht (motor) | _nums leest '8,4' als twee getallen (8 en 4). getal1/getal2-regels zijn bij kommagetallen in de vraag onbruikbaar (bv. 'quotiënt,rest' bij GET-04 #5 '7,6 liter … over 4' zou '1,1' geven). Voorstel: kommagetal als één getal lezen, of een eigen 'kommagetal1' | open |
| Oef-#438 | Overzicht (data) | GET-04 nrO 9 (alle 4 items): «Een pakket weegt 6,3 kg. Hoeveel wegen 10 stenen?»: het ding wisselt. Voorstel: hetzelfde ding in beide zinnen ('Een pakket weegt 6,3 kg. Hoeveel wegen 10 pakketten?'). GET-04 nrO 5: '7,6 liter water … over 4 stickers', '… over 3 tanden', '… over 6 sterren', '115 kilo kaartjes', '81 kilo stickers': verdelen over iets dat kan krijgen (kinderen, teams, emmers) en kilo bij iets dat je weegt (zand, appels). Onze teksten noemen geen ding en blijven | open |
| Oef-#439 | Overzicht/Didactiek | GET-04 nrO 6 (gemiddeld): Claudes label 'verhoudingstabel-verkeerd' op 6 sleutels zonder herkenbare route (14 bij 6, 13, 3, 15, 18 → 11; 15 bij 15, 11, 12, 9, 13 → 12). Label 'verkeerde-bewerking' dekt zowel de som (55) als het middelste getal (13). Voorstel: afleiders uit echte denkfouten (som, middelste getal, som : 4) | open |
Stand (les 164): build 2026-10-08 12:44:21 met hint-sync 12:44:24 bevat batch1.json 1106695c9148 (t/m ronde 1e), batch2.json 8c699cd7b0a1 (t/m ronde 2b) en batch3.json 27ee48fd8a5d (eerste versie, nu gesynct: alleen nog patch_batch3.py). Hint-inhoud live = zandbak (0 verschillen op DENK-02/03/04 en GET-01..04); tweede run van patch_batch1/2/3: 0 wijzigingen.

## Overzicht 8 okt: motor (build 12:44:21, met batch 1 ronde 1e, batch 2 ronde 2b, batch 3)
| # | Wie | Wat | Stand |
|---|---|---|---|
| Oef-#421/#422 | Overzicht (motor) | `norm421` in fout_regels.py: letterlijke regels en opties met één notatie: '−', '-' (tussen getallen/spaties) en '–' zijn één minteken; '3 euro'/'€ 3' → '€3', maar alleen als de regel zelf een bedrag is (een regel '16' leest '16 euro' zoals vroeger). Ook 'de minsom' en 'de minsom omgedraaid'. Zelftest `_zelftest421` bij elke import. Regressie oud ↔ nieuw (tools/motor_regressie.py): G5 4845 · G6 4302 · G7 2607 items · 0 anders | ✓ · Oefeningen kan de workarounds in DENK-02 #8/#9 weghalen |
| Oef-#429 | Overzicht (motor) | Regel 'de deelsom omgedraaid': antwoord 'a : b' → alleen de optie 'b : a'; is het antwoord een getal en noemt de vraag 'a : b', dan b/a op waarde. Proef met DENK-04 #5: alle 7 items ('8 : 328' …) krijgen de sleutel, de keersom blijft 'de keersom' | ✓ motor · regel in batch 2: Oefeningen |
