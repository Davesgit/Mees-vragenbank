# G5 Claude-merge (1 okt 2026, build 15:13; rebuilds 16:13, 16:40 en 17:10)

Gebouwd op de G4-scripts van 14:35 (`scripts/g4_basis_1435/`, met `g3_basis_1359/`), in het G4-formaat (data, somtypen, logs, bevroren).
Script: `python3 scripts/build_g5.py`. Dat draait ook `sync_hint_keys.py` en `apply_hints.py`. Controle: `python3 check_merge_notatie.py` en `python3 check_hints.py` (de G5-versies van de G4-checkers van Oefeningen).

## Pool
- Claude-doelen G5: D5-6…9, C1–C10, B1–B4, M11–M16, M27, K9, G2, plus B12 en G11.
- Daarbij `g4/data/geparkeerd_G5.json` (1563): daarin de 134 G4-twijfelitems met een besluit en de 28 items uit de G4-fixlijst (26 uit #1–#24, 2 uit #30: kat '400 g' → G5-MEET-E05, voetbalveld '1000 m' → G5-MEET-E01) (`merge.fixlijstG4`; G5 neemt het doel over).
- Niet in de pool: wat in G3 of G4 gemapt, geschrapt, twijfel of terug-G3 is (134 binnen de kandidaatdoelen).
- Pool 7463 → gemapt 4842, twijfel 9, park-G6 2305, terug-G4 300, dubbel 7 (build 1 okt 15:58: +22 klokkenrij-items uit G4-fixlijst #45, kloktijd op x:20/x:35/x:50 → G5-MEET-E06).

## Afspraken
- **Getallen:** G5 = tot 1000.
  - Boven 1000 → `data/geparkeerd_G6.json`, met een voorstel voor een G6-doel.
  - Onder het G5-niveau → `data/terug_G4.json` en `logs/terug_g4.csv`. Items die goed in G4 passen staan ook in `g4/data/aanvulling_uit_g5.json` (300). De G4-build is daarvoor niet aangepast.
- **× en : alleen in** GET-V03, M05, M06, E07, E08, E09, MEET-E08 en VERH-E02.
- **Notatie:**
  - breuken in woorden (de helft, een kwart, drie kwart);
  - geld: '€8', '€3,50'; liter: '0,5 L';
  - delen: '20 : 4 = 5'; rest: '3 rest 2'.
- **Regels:** `scripts/regels_g5.py`:
  - `classify_g5`: G4-fixlijst en G4-besluit gaan voor; breuken B1/B2/B3; geld B4/B12; kale sommen; maten; afronden; patronen G11.
  - `bewerk_g5`: W8–W12 context, N9–N16 notatie, D20–D26 Didactiek.
  - `verify_g5`, `notatie_check_g5`.
- **G4-fixlijst ook in G5:** `scripts/g4_basis_1435/fixlijst_g4.py` (`tekst_fix`) op de 28 fixlijst-items. Dat zijn: groepjes eerst (5 × 15); 'kinderen gaan eten / op stap', zonder kommagetallen.
- **Bevroren:** `bevroren/ids_v1.json` en `somtype_nr_v1.json` (eerste build 15:13); `somtype_nr_v2.json` (15:25) met één nieuw somtype, G5-MEET-E01 #5 '[referentie] Hoe lang/hoog/breed is … ongeveer?' (voetbalveld uit G4 #30). `somtype_nr_v3.json` (15:58) met één nieuw somtype, G5-MEET-E06 #24 '[klokkenrij] Welke klok wijst half # [ding]? (tijd in woorden)' (de 22 klokken uit G4 #45). Hints koppelen op nrOrigineel/somtypeOrigineel.

## Stand na de rebuilds van 1 okt (besluiten Didactiek 16:11 en fixlijst 16:31)
- **Pool 7.463 → gemapt 4.843 · twijfel 0 · park-G6 2.313 · terug-G4 300 · geschrapt dubbel 7.** 0 FOUT in gemapt. 121 somtypen (64 hints klaar: batch 1, taal: ok, en batch 2; 57 open).
- **Didactiek (twijfel 9 → 0, `besluiten_twijfel_didactiek.md/.json`, `scripts/besluiten_g5.py`):**
  - de 8 geld-keer-items → park-G6 met voorstel **G6-GET-E07** (item -004 niveau basis, de rest toepassen; '€7,88'; context 'een zak wortels' / 'een stickervel'); de G6-build neemt ze op;
  - drie kwart (1) blijft in **G5-VERH-E01** op kritisch: 'drie kwart' in woorden, 4 zichtbare gelijke groepjes, '8 : 4' alleen in de hint. Nieuw somtype G5-VERH-E01#3 → `bevroren/somtype_nr_v4.json`.
- **Merge-fixlijst #12–#18, #20, #22** (`merge-fixlijst.md`, `scripts/fixlijst_g5.py`, code `G5-FX*` in `logs/fixes.csv`, veld `merge.fixlijstG5`):
  - **#12** motor: nieuwe fout_regel `fout = het andere tiental/honderdtal naast getal1` (ook `fout = het andere buurtiental` / `het andere buurhonderdtal`), bv. 166 → 160 als 170 goed is. In `scripts/fout_regels.py` (en de kopieën in g4/g6/g7). Nog door geen hint gebruikt: Oefeningen kan 'verkeerde kant' nu splitsen.
  - **#1/#13** geen fout-sleutel boven 1000 bij afronden (`fout_regels.BEREIK_AFRONDEN = 1000`, gezet in `scripts/apply_hints.py`): de sleutel 1100 is weg bij E02 #2 004, 014, 020 en 027.
  - **#14** geen fout-sleutel buiten de getallenlijn (`fout_regels.LIJN_BINNEN = True`, alleen G5): 1060 (106) en 1010 (107) zijn weg. In G4 staat deze schakelaar uit (zou 48 GET-E03-items raken, die sleutels > 100 op de lijn 0–100 hebben; G4 is al goedgekeurd).
  - **#15** alleen informatie. **#16** blijft open voor Didactiek (G4-niveau in E05 #11 en E02 #3: bewuste opstap?); niets veranderd.
  - **#17** E04 #4: 'De kinderen delen een taart in 4 gelijke stukken. Een kind eet er 1 op.' (geen dino's bij taart/pannenkoek).
  - **#18** splits-sjabloon: `hints/make_batch1.py` P_SPLITS/M_SPLITS zeggen nu 'honderdtallen (als het die heeft)', en `check_hints.py` geeft FAIL als een hint 'Splits het tweede getal in honderdtallen' zegt terwijl een item van het somtype een tweede getal onder de 100 heeft. Nu 0 FAIL.
  - **#20** E06 #4 ('een zak noten', 1 item) is geen kopie, maar een 12e item van #3 met een eigen kop: samengevoegd in #3 (12 items, geen duplicaatVan nodig). Het tweede ding wisselt nu (sticker, gum, pen, liniaal; vast per item).
  - **#22** E07 #6–#17 (12 somtypes met elk 1 item) → 2 context-somtypes: 'Keersom in een verhaal: splits het grootste getal' (8 items, sleutel E07#8) en 'Keersom in een verhaal: een rond tiental' (4 items, sleutel E07#9).
  - **Bevroren sleutels:** geen nieuwe vN. De samengevoegde somtypes houden een bestaande sleutel (koppeling op claudeId).
  - **Fout van de rebuild van 16:39 (Didactiek batch 2 V1, merge-punt #30):** `sync_hint_keys.py` zette de 12 oude E07-entries (en E06 #3/#4) stil op 2 koppen. Daardoor kregen 8 + 4 items de hints van één oud somtype (Hint 1 'trainen' / 'club koopt dozen'), en vielen 5 sleutels op 'andere fout' (419 '180', 421 '182', 424 '116', 438 '18', 440 '248'). `check_hints` zei toch ALLES OK. Herstel: Oefeningen schreef om 16:50–16:55 één entry per nieuw somtype (`hints/patch_batch2.py` ronde 2b: E07 entry 8 → nieuw #6, entry 9 → nieuw #7, E06 #4 weg); de samenvoeging blijft dus (`SAMENVOEGEN_E07 = True` in `scripts/fixlijst_g5.py`; op False = terug naar 12 somtypes, de oude entries staan in `_backup/g5_1648/hints/batch2.json`). Na de rebuild van 17:10 per item nagekeken: alle 12 items hebben de nieuwe Hint 1, en de 5 sleutels hebben weer hun eigen regel (keer tien, cijfers omgedraaid, eenheden-stuk fout). 0 sleutels op 'andere fout'.

## Rebuild 17:10 / 17:06 (Didactiek batch 2, `review-batch2-didactiek-v1.md`; opdracht Dave 16:46 en 17:01; bouwt voort op ronde 2b van Oefeningen, hun hints/ niet overschreven)
- **#30 nooit stil samenvoegen.** `scripts/sync_hint_keys.py` rekent eerst per entry de nieuwe kop uit. Vallen twee of meer entries op één kop, dan blijven die entries **ongewijzigd** en staat het als probleem in `logs/hint_sleutels.json`. `check_hints.py` geeft nu FAIL bij: elk probleem in die log; een log die niet bij de somtype-indeling van `data/gemapt.json` hoort (vingerafdruk `indeling`); twee entries op één kop; een entry waarvan nr/kop niet in `somtypen/<doel>.md` staat. Getest met een nagemaakte dubbele entry: 2 FAIL. Dezelfde sync en check staan ook in g6 en g7 (nog geen batches). G4 niet: daar staat al een oud probleem in de log (G4-GET-E08 'gaan op stap … nodig?': geen items meer met dit somtype), dat zou de goedgekeurde G4 op FAIL zetten. Beslissing voor Oefeningen/Dave.
- **#34** `check_hints.py`: FAIL als een foute optie geen eigen fout-hint heeft (sleutel = de optietekst). Nu 0.
- **#23/#34 E07 #2** (58 items): het aantal groepjes eerst. 48 items van '42 × 16' → **16 × 42**, de plussom in dezelfde volgorde (**16 + 42**), de deelsom blijft '42 : 16'. De omgekeerde keersom is nergens een optie (0/58). De regel 'de plussom' leest '+' in de optie en past dus nog (58/58 met eigen tekst). Antwoordcontrole: `fixlijst_g5.verify` (G × P), 0 FOUT.
- **#29 motor** (`scripts/fout_regels.py`, ook g4/g6/g7): `fout = antwoord × 10` en `fout = antwoord : 10` (exact; ': 10' alleen als het antwoord op 0 eindigt; vanaf 10.000 beide vormen als sleutel, met en zonder punt; bij een geldantwoord het bedrag × 10 / : 10). Nog door geen hint gebruikt. Daarmee kan V3/V4 ('nul te veel', 'keer tien') op een exacte regel en weer een uitspraak zijn (Oefeningen).
- **#32 / #19 motor:** geldregels `fout = antwoord ± 1 cent`, `± 10 cent`, `± €1` (ook alleen + of −). Bedragen worden in centen gelezen (`_cent`: '€21,95' → 2195, '€3' → 300). Nog door geen hint gebruikt: Oefeningen kan de 649 '± 1 cent'-sleutels in E06 nu een eigen tekst geven ('Kijk naar het laatste cijfer: de prijzen eindigen op 0 of 5') of ze weglaten.
- **#33 geldinvoer:** een geldsleutel raakt dezelfde invoer met en zonder '€', met spaties, met en zonder ',00', en '8,8' = '8,80' (`fout_regels.geld_norm`). Elk open item met een geldantwoord (1072: E06 1060, MEET-E07 12) heeft het app-veld **`geldInvoer`**: `sleutel` (huisnotatie '€8,80' / '€4'), `accepteer` (bv. '€8,80', '8,80', '€ 8,80', '€8,8', '8,8'; bij hele euro's '€4', '4', '€ 4', '€4,00', '4,00', '€ 4,00'), en `punt` ('8.80' is geen bedrag: tekst 'Bij geld schrijf je een komma.'). De app normaliseert de invoer zo vóór het zoeken van de fout-sleutel. Meerkeuze heeft geen invoer en dus geen veld.
- **#21** 'trainer' → 'kind', 'shirt' → 'trui' (23 items, ook in Claudes fout-hint-teksten): E07 029 '… over 7 kinderen. Hoeveel kaartjes krijgt elk kind?', 435 'Een kind heeft 36 stickers. Er zijn 7 kinderen.', 436 'Een kind heeft 38 knikkers. Er zijn 6 kinderen.', 447 'Een boer verzamelt elke dag 300 eieren', 448 '60 knikkers', E06 011 'een muts €3,30' (een trui van €3,30 is geen echte prijs), MEET-E07 011 'drie mutsen', MEET-E07 001 'Een trui kost €15,36', E04 003 en MEET-E06 1193 'De kinderen …', E05 (7) en M06 (6) 'truien' / 'kinderen'. Nu 0 keer 'trainer' of 'shirt' in opgave, opties of fout-hints. ('speler', 'sticker', 'club' blijven.)
- **#21 E07 436 (opdracht Dave 17:01):** 'Een kind heeft 38 truien. Er zijn 6 kinderen.' (Didactiek V6 had 'knikkers'; Dave koos truien). 447 eieren, 448 knikkers, E06 011 muts, 029/435/436 kind.
- **#42 M06** (7 items: 022, 026, 047, 048, 056 'trainers' → 'kinderen', 'elke trainer' → 'elk kind'; 048 en 060 'shirts' → 'truien'): zelfde regel als #21.
- **#23 check:** `check_hints.py` geeft FAIL als de omgedraaide keersom van het antwoord (42 × 16 bij 16 × 42) als foute optie staat. Nu 0. '42 : 16' blijft.
- **#31 E07 #1 kale keersom:** volgens het voorstel blijven de 328 bestaande items 'groot × klein' (13 × 3). Regel voor nieuwe items (generator): 'klein × groot' (3 × 13) met Hint 2 'Splits het tweede getal …'. Niets veranderd in de data.
- **#33 punt bij geld:** `fout_regels.GELD_PUNT = True` (G5, in `apply_hints.py`): bij open geldvragen staat als eerste regel 'fout = punt in plaats van komma (geld)' met de tekst **'Bij geld schrijf je een komma.'** en de sleutels '8.80', '€8.80' (en '8.8', '€8.8'); de regel vangt elke invoer als '8.80' / '€ 8.8' (984 E06-items; niet bij hele euro's). Staat ook in `geldInvoer.punt`.
- **#35 motor:** (a) staat [getal1]/[getal2]/[antwoord] in de tekst van 'andere fout', dan wordt de per item ingevulde tekst de `algemeneFoutHint` (was None); (b) een leesbare regel met zo'n tekst voegt bij open vragen ook zijn eigen sleutels toe (bv. 'fout = getal1 + getal2' bij E07 #4–#7 en M05). Nu 0 items zonder algemeneFoutHint. Daarmee kan S3 'andere fout' aan (`S3_ANDERS = True` in `hints/patch_batch2.py`, aan Oefeningen). G4 heeft geen zulke teksten: geen verschil.
- **#36 munt-tekening:** elk item met `jsRender.soort = 'geld'` (M03 28, MEET-E07 290) heeft `visual.eisen`: 'waarde op elke munt en elk briefje (bv. 50 c, €1, €2, €5)' en 'kleur (koper, goud, zilver) niet het enige kenmerk'.
- **#27 M03:** de 28 items (munten tot €1,90) staan op niveau **basis / Opwarmen** (was toepassen/Oefenen). **Uitbreiden tot €10/€20 kan niet met nieuwe Claude-items:** in de hele Claude-bank (23.285 vragen) staat geen enkele geldvraag met briefjes in de tekst, vergelijken ('Wat is meer?') of 'Kun je … betalen met'. De enige bestaande tel-items boven €2 ('Hoeveel geld zie je?', €2,05–€12,50, 182 items, 52 met een briefje van €5) zitten al in **G5-MEET-E07** (Claude B4/M5/M8). Niets verplaatst en niets verzonnen. Geen keersommen met geld in M03 (0 items met '×'). **Werk voor Oefeningen:** nieuwe M03-items tot €10/€20 (briefjes van 5 en 10, centen zoals €4,95/€12,35), vergelijken ('€7,05 of €6,95: wat is meer?'), 'Kun je €4,95 betalen met 6 munten/briefjes?', en een eigen fout-hint voor 'getal-overgenomen' (aantal munten; nu de letterlijke regels '€3'/'€4', INFO 'regel niet te lezen'). Beslissing Dave/Didactiek: of de 182 tel-items boven €2 van MEET-E07 naar M03 moeten.
- Batch 1 (27 somtypes, 522 items) is taal: ok en zit in deze build. Batch 2 (14 entries na ronde 2b van Oefeningen) zit erin; de taalcheck van ronde 2b is nog open.
- **Stand 17:10:** pool 7.463 → gemapt 4.843 · twijfel 0 · park-G6 2.313 · terug-G4 300 · dubbel 7; 0 FOUT in gemapt (12 bekende FOUT in park-G6). check_hints: 64 klaar · 57 open · 0 FAIL · 0 WARN · 2 INFO. check_merge_notatie: ALLES OK. `logs/hint_sleutels.json`: 0 problemen. Bevroren sleutels en ids ongewijzigd.

## Bestanden
- Data:
  - `data/gemapt.json`, `data/per_doel/G5-*.json`;
  - `data/twijfel.json` (leeg sinds de besluiten van Didactiek, 16:11);
  - `data/geparkeerd_G6.json`, `data/terug_G4.json`.
- Somtypen: `somtypen/G5-*.md`, 121 somtypen.
- Logs:
  - `logs/fixes.csv`, `antwoordcontrole.csv`, `geschrapt.csv`, `terug_g4.csv`;
  - `zelfde_als_bank.csv` (tegen `exports/vragenbank_g5.json`);
  - `stats.json`, `somtypen_overzicht.json`.
- Let op:
  - 12 park-G6-items geven FOUT in de G5-controle: G6-GET-E03 033–036 (in de G6-build opgelost, G6-D1) en de 8 geld-keer-items (de G5-controle verwacht '€'; in de G6-build opgelost: '€7,88').
  - Klokitems in MEET-E06 (KLOK = INFO).

## Rebuild 17:16 (Didactiek 17:12: #21/436, #44, #45, #46)
- **436 (#21):** «Een kind heeft 38 knikkers. Er zijn 6 kinderen. Hoeveel knikkers zijn dat samen?» Antwoord 228 en sleutels (180 · 48 · 44 · 188) blijven gelijk.
- **#44 (check_hints):** FAIL als een item van een somtype met een 'andere fout'-regel geen algemeneFoutHint heeft. FAIL als 'te veel'/'te weinig' niet past bij de sleutel
  of bij de regel (vanaf / tot en met / kleiner dan / waarden), ook bij geld (in centen). De regels gelden van boven naar beneden: een waarde die een hogere regel al vangt,
  telt bij een lagere regel niet mee. Zo vangt 'nul te veel' bij E07 #5/#7 de ×10-sleutels eerst, ook al staan ze in de waarden van Claudes 'nul-fout-tientallen'
  ('te weinig'). Dat is nu geen fout, maar het hangt wel af van de volgorde (S10: daarom moeten ×10 / :10 naar de vaste regels van #29).
- **#45:** merge-fixlijst #21 bijgewerkt volgens de data. #35 noemt nu de huidige regelnummers (fout_regels.py r. 384–385 algemeneFoutHint, r. 329–330 kand).
- **#46:** bij een samengevoegd somtype (E07 #6/#7, E06 #3 item 012) toont merge.somtypeOrigineel het eigen oude sjabloon van het item, met
  merge.somtypeNrOrigineelEigen. De sleutel waar de hint op koppelt, staat in merge.somtypeSleutel (nrOrigineel + somtypeOrigineel) en in merge.somtypeNrOrigineel.
  Het gaat om 11 items: 10 in E07 en 1 in E06. Hint-koppeling: 0 problemen.
- check_hints: 79 klaar · 42 open · 0 FAIL · 0 WARN. merge-notatie: ALLES OK.

## Rebuild 17:27 (review-batch3-didactiek-v1.md, opdracht Dave 17:17, fixlijst #39 en #47–#51)
- **#39 M06 #8:** 243 : 25 → 52 : 8 (busje, 7), 82 : 12 → 43 : 6 (busje, 8), 40 : 12 → 34 : 4 (boot, 9). Sleutels per item: q (één te weinig), q,r (rest achter de komma), getal1 − getal2, getal1 × getal2. Somtype en hint-sleutel blijven gelijk. Controle: 'naar boven afronden' (ook 'In elk busje').
- **#47 restsommen:** 'keer gedaan' (#3, #6) en 'afgetrokken' (#3, #4, #6, #7, #8) in `hints/patch_batch3_merge.py`. Draai die **na** `patch_batch3.py`. Hij laat de fout-hints van Oefeningen staan en zet alleen de nieuwe ertussen. De nieuwe teksten hebben nog een taalcheck nodig.
- **#48:** check_hints FAIL als een algemenere regel een sleutel eerst vangt (Claudes sleutels tellen niet mee). Nu 0.
- **#49:** FX21 in alle extraVelden + foutHintsTekst/optiesTekst. 'Élke trainer' → 'Élk kind'. check_merge_notatie ENG = FAIL. G5: 0 hits. aanvulling_uit_g6.json (G6-build): 6 hits, die gaan weg in de G6-rebuild.
- **#50:** denkfout 'rest-achter-komma'; motor: 'fout = quotiënt,rest' en 'fout = een kommagetal'.
- **#51:** check_hints FAIL op 'tafel' als tafel van vermenigvuldiging bij eettafels. Nu 0 (Oefeningen had S1 al gedaan).

## Rebuild 17:47 (review-batch4-didactiek-v1.md #59–#63, recheck-rondes-2c-1d-3b-didactiek.md #64–#67)
- **Motor (#52/#60):** `_int`/`_nums` lezen '10.000' als 10000. Elke sleutel van 5 of meer cijfers staat in beide vormen ('10000' en '10.000').
  **De app moet allebei goed rekenen** (of de invoer normaliseren: punt tussen groepjes van 3 weg). Dezelfde fout_regels.py in g6/g7 (G4 niet aangeraakt).
- **#60:** geen 10.000 meer: 900 cm = □ m (9), 1 km = □ m, 1 m = □ mm, 1 L = □ ml, 1 kg = □ g (1000). Waarden 2–9 bestonden al in die somtypes.
  Claude-sleutels herrekend per denkfout; id en somtype blijven. Antwoord ≥ 10.000 in G5: 0.
- **#61:** E01 #2 verkleind: 2000/4000/6000/8000 cm → 200/400/600/800 cm (2/4/6/8 m). Geen Claude-items met hele meters onder 2000 cm
  in de pool. Decimeter: geen Claude-items → werk voor Oefeningen (generator).
- **#59:** E02 223 6 × 3 (oppervlakte = omtrek) → 26 × 3 (58; oppervlakte 78). Alle paren tot 25 cm lang waren al gebruikt.
  check_merge_notatie OPP (G3–G7): FAIL als bij een omtrekvraag lengte × breedte = omtrek.
- **#62/#54:** motorregels 'fout = streepjes als 1 geteld' en 'fout = één streepje ernaast' (jsRender maatbeker); **#64:** 'fout = getal1
  afgerond op tientallen'. Ze staan in batch1.json (E02 #2) en batch4.json (E04 #1) via `hints/patch_merge_batch1_4.py`. Draai dat script
  **na** patch_batch1.py/patch_batch4.py van Oefeningen en vóór de build. Het is idempotent, en de teksten komen van Didactiek.
- **#63:** haak `/workspace/claude-merge/tools/referentiematen_check.py` in check_merge_notatie G3–G7: leest referentiematen.json (WARN REF / REF-zacht, nooit FAIL).
  G5 059 claudeUitleg (voetbalveld 'sprint … iets meer dan een minuut') aangepast (FX63). G5 nu 0; G4 5 WARN (niet aangepast, G4 goedgekeurd).
- **#67:** E07 #4 'Elk kind / Elke dino … heeft' (12 items); somtype en hint blijven.
- Aantallen: pool 7463 · gemapt 4843 · park-G6 2313 · terug-G4 300 · controle gemapt|ok 4813, n.v.t. 30, park-G6|FOUT 12 (opgelost in G6).
- check_hints: 103 klaar · 18 open · 0 FAIL (met batch5 van Oefeningen). merge-notatie: ALLES OK (ENG 0, OPP 0, REF 0).

## Notatie van maten (machten) aangezet (18:05, notatie_machten.md van Didactiek)
- `check_merge_notatie.py` gebruikt de gedeelde haak `/workspace/claude-merge/tools/machten_check.py` (regel MAAT; G8 gebruikt dezelfde haak).
  - In elke groep FAIL: MACHT (macht van een getal), ASCII ('m2', 'cm3', 'm^2'), MENG ('vierkante cm', 'kubieke cm').
  - G3–G5: geen ² of ³ (OPP2 en INH3 zijn FAIL); 'vierkante meter', 'kubieke', 'kuub' en 'hectare' geven WARN.
- Stand: MAAT 0 FAIL · 0 WARN.
- **App-eis bij antwoorden met een eenheid (gekozen in plaats van extra vormen in de merge-data):**
  - De eenheid staat naast het invulvak (`unitHint`), dus het getal alleen is goed.
  - De app normaliseert de invoer op één plek, voor alle items:
    - spaties weg, kleine letters;
    - 'm2', 'm^2' en 'm²' worden m², 'cm3', 'cm^3' en 'cm³' worden cm³ (zo ook voor mm, dm, dam, hm, km);
    - 'vierkante (centi/deci/kilo…)meter' en 'kubieke …meter' worden het symbool, net als de mengvormen 'vierkante cm' en 'kubieke cm' (bij invoer mogen die);
    - 'kuub' wordt m³ (vanaf G7) en 'hectare' wordt ha;
    - komma en punt als decimaalteken, en een duizendpunt mag.
  - Goed is: het getal klopt, en de eenheid ontbreekt of is na normalisatie gelijk aan de gevraagde eenheid. Een andere eenheid is fout.
  - De screenreader leest het symbool als woord voor (aria-label: m² → «vierkante meter», cm³ → «kubieke centimeter», km² → «vierkante kilometer»).
  - De merge-data krijgen daarom geen extra antwoordvormen; zie notatie_machten.md §6 (Didactiek).

## Rebuild 18:01 (merge-fixlijst #68–#74, Oefeningen 17:50)
- **Motor** (`scripts/fout_regels.py`; gekopieerd naar G6/G7, daar identiek):
  - #68: kloktijd in woorden ('vijf over 5', 'tien voor half 11').
  - #69: 24 uur vanaf 13:00.
  - #70: `fout = klok een minuut / vijf minuten / tien minuten / een kwartier te laat` (en `te vroeg`), `een dag later`, `een dag eerder`, `datum later dan het antwoord`, `datum eerder dan het antwoord`.
  - #72: `fout = over en voor verwisseld`.
- **#71 (fixlijst_g5.py, MEET-E06):**
  - 1635 Claude-denkfouten hebben nu het label van hun echte verschil met het antwoord (uur-te-laat, 5-minuten-te-vroeg, over-en-voor-verwisseld, uur-te-veel …). Claudes label staat in `denkfoutClaude`.
  - Een Claude-regel op het oude label blijft werken tot de entry een regel voor het nieuwe label heeft.
- **#73:** de 7 klok-zetten-items (#22, nu #23) hebben `antwoordDetail.invoer = 'h:mm'`; de app geeft de gezette tijd door als 'h:mm'. Niet gesplitst (5 + 2 items, een somtype zonder hints). Het bevroren nummer van de split, G5-MEET-E06 #25 (`bevroren/somtype_nr_v5.json`), blijft staan als 'vervallen, geen somtype' (`logs/bevroren_vervallen.json`, besluit Dave 18:08). Het wordt niet opnieuw gebruikt. Meer items per soort tijd is generatorwerk.
- **#74:** 16 + 6 = 22 klokitems van G4 #45 (regel FX-G4-45) nageteld.
- **Tellingen gelijk:** gemapt 4843 · park-G6 2313 · terug-G4 300.
- **notatie:** ALLES OK, ook MAAT 0.
- **check_hints:**
  - MEET-E06: 0 FAIL.
  - De FAILs nu (1089) komen allemaal uit de nieuwe `hints/batch6.json` van Oefeningen (MEET-E07 526, VBN-E01 554, MKU-E02 6, VERH-E01 3). Die batch is nog in bewerking (18:00).
- **Algemene tekst:**
  - 245 Claude-sleutels vallen op 'andere …'. 232 daarvan zitten in batch 1–5; dat aantal is gelijk aan het aantal vóór de rebuild, want de entries gebruiken de nieuwe regels nog niet.
  - Gebruikt Oefeningen de nieuwe regels in de entries, dan vallen er 173 weg en blijven er 72 over (zie merge-fixlijst, blok '#68–#74').

## Rebuild 18:39 (batch 6 en Didactiek 18:15, merge-fixlijst #75–#88)

- Nieuw: `scripts/fixlijst_g5b.py` (#75, #78, #79, #83–#87), `scripts/park_g7_hints.py`, `scripts/koppeling_merge.py` met `hints/koppeling_merge.json`, en `hints/patch_merge_batch6.py` (#77).
- Volgorde: patch_batch*.py (Oefeningen) → `hints/patch_batch3_merge.py`, `patch_merge_batch1_4.py`, `patch_merge_batch6.py` → `python3 scripts/build_g5.py` → `check_hints.py`, `check_merge_notatie.py`.
- Nieuwe status **park-G7** met `data/geparkeerd_G7.json` (MEET-E06 #1, dagen tussen datums, 220 items). De hints komen van batch 5 #1. De G7-build leest dit bestand en mapt de items op G7-MEET-04.
- Generator-somtype #84 (`G5-MEET-E06-merge-gen-001..020`, nrOrigineel 26, nieuw in `bevroren/somtype_nr_v6.json`).
- Generator #100 (`G5-MEET-E06-merge-gen-021..038`): 18 extra items voor klok zetten (nrOrigineel 22, nu #9), ten minste 5 per soort tijd. Ze staan in het bestaande somtype en hebben de hints van ronde 5b.
- `hints/koppeling_merge.json`: een entry die bewust samengevoegd (E07 #5 → #3) of geparkeerd (E06 #1) is. sync, apply en check_hints slaan die over, maar controleren hem wel (nooit stil). Zie `logs/hint_sleutels.json` 'speciaal' en `logs/bevroren_vervallen.json`.
- 19:03: #102–#109 (zie merge-fixlijst.md, blok 'Didactiek 18:54'). Er zijn nieuwe gedeelde checkers in `../tools/`: `antwoordvormen_check.py` (VORM, FAIL, G3–G8) en `verklapper_check.py` (VERKLAP, WARN, G4/G5).
- Cijfers (18:51): gemapt 4657 (4639 + 18 van #100) · park-G6 2313 · park-G7 220 · terug-G4 300. Controle: gemapt|ok 4626, n.v.t. 31, FOUT 0. check_hints: 120 klaar, 0 open, 0 FAIL, 0 WARN. Notatie: ALLES OK.
- 18:39: merge-fixlijst #90–#99 (Didactiek batch 6). Motor #92 (tabel: eerst de gevraagde rij en kolom), #93 en #94. Data #90 (bijkomt), #96 (E07-prijzen), #98 en #99 in `fixlijst_g5b.py`. Checker #90/#91 in `check_hints.py`. Zie het blok "Batch 6 Didactiek 18:31" in merge-fixlijst.md.
- **Stand 19:18 (#151, #114, #113, #118):** gemapt 4657 · park-G6 2313 · park-G7 220 · terug-G4 300. 120 somtypen. Controle: FOUT 0. check_hints: 0 FAIL · 8 WARN (#113, MEET-E06 #9 klok zetten, wacht op Oefeningen ronde 5e) · 3 INFO. check_merge_notatie: ALLES OK, met nieuw GEN (#151, `scripts/check_generator_sleutels.py`). Vervangen: gen-006/008/013/014/018/020 en MEET-E07 claude-bank-282/287. Zie het fixlijst-blok '19:14–19:16'. #111 vervalt door #114.
- **Stand 19:47 (rebuild met ronde 5e-2 van Oefeningen; nieuwe regel #113 van 19:42/19:46):** gemapt 4657 · park-G6 2313 · park-G7 220 · terug-G4 300. 120 somtypen. Controle FOUT 0. check_hints: 0 FAIL · 0 WARN · 130 INFO (127 #113). check_merge_notatie: ALLES OK.
- **Stand 20:18:14 (#120–#122; eerst 'stand 20:40' genoemd):** gemapt 4657 · park-G6 2313 · park-G7 220 · terug-G4 300. 120 somtypen. Controle FOUT 0. check_hints: 0 FAIL · 0 WARN · 130 INFO. check_merge_notatie: ALLES OK (nieuw: R121, DOELID). 27 items vervangen (#121), doelId van gen-001…020 gezet (#122), checker #113 aangescherpt (#120). Zie het fixlijst-blok '#120–#122'.
- **Stand 22:31:36 (#123–#125 en E02-001):** gemapt 4827 (170 uit G8, waaronder «4 dozen met elk 198 vissen» in GET-E07, nieuw somtype 12 / sleutel 22, bevroren v8) · park-G6 2313 · park-G7 220 · terug-G4 300. check_hints: 120 klaar · 20 open · 0 FAIL · 0 WARN. #123 (7 opties 'één vergeten' terug naar rij − één cel), #124 (KOLOM_VOOR_DEEL), #125 (2 getallenruimtes). Zie het fixlijst-blok '#123–#125'. Open somtypes per doel: `../hints_todo.md`.
