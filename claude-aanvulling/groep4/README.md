# Claude-merge G4 (stap 1–3) — 1 okt 2026

Dit is de G4-merge van de Claude-vragenbank (`/workspace/claude-bank-src`, commit 7da3257, CC BY-SA 4.0) naar LeerMees.
Het sjabloon is de G3-pilot (definitief; scripts van de build van 13:59).
Gelezen wordt alleen uit: `claude-bank-src`, `claude-merge/g3`, `exports/`. Geschreven wordt alleen in deze map.

## Draaien
```
python3 scripts/build_g4.py        # bouwt alles en draait zelf sync_hint_keys.py + apply_hints.py
python3 check_merge_notatie.py     # notatie (exit 1 bij FAIL)
python3 check_hints.py             # hints per somtype (nu: alles 'open')
```
Een rerun is stabiel: ids en somtype-sleutels komen uit `bevroren/`.
Gooi `bevroren/*.json` niet weg nadat er hints geschreven zijn. Bij een nieuwe indeling: maak `somtype_nr_v2.json` en laat v1 staan.

## Pijplijn
| stap | wat | waar |
|---|---|---|
| 1 | Kandidaten: alle items van de Claude-doelen D2-1…D5-5, M6–M10, K5, K6, G1, G10, W1 (G4) en M27, K10, T9, K9, G2 (aangrenzend), plus de 626 door G3 geparkeerde items. Items die al in G3 zitten (gemapt, geschrapt of twijfel) gaan niet mee; ze worden geteld in `logs/stats.json` → `alInG3`. | `build_g4.py` |
| 2 | Per item een G4-doel kiezen met R-regels G01–G27 (`regels_g4.classify`). Een Didactiek-besluit uit G3 met uitkomst "G4" (`g3/besluiten_twijfel.json`) gaat voor. | `regels_g4.py` |
| 2b | Eerst de G3-regels (`merge_g3regels.py` = kopie van `g3/scripts/merge_stap2.py`, 13:52/13:59, alleen BASE → g3 en K10 bij de vakcodes), daarna de G4-regels (`regels_g4.bewerk_g4`). Daarna wordt elk antwoord op de bewerkte vorm opnieuw gecontroleerd (`verify_g4` → `verify2` → G3-`verify`). | |
| 3 | Somtypen per G4-doel, met **nrOrigineel + somtypeOrigineel per somtype vanaf de eerste build** (`bevroren/somtype_nr_v1.json`). | `somtypen/G4-*.md` |

De functies uit `build_g3.py` (convert, fix_text F1–F6, verify, somtype, fmt_item) worden ongewijzigd gebruikt uit
`scripts/g3_basis_1359/`. Dat is een kopie van de G3-scripts van 13:59, met dezelfde md5 als in g3.

## Status per item
- **gemapt**: komt in de G4-bank. Zie `data/gemapt.json` en `data/per_doel/G4-*.json`.
- **twijfel**: Didactiek beslist. Zie `data/twijfel.json`. Na de besluiten van 1 okt is die leeg; zie 'Besluiten Overzicht'.
- **park-G5**: hoort buiten G4. Zie `data/geparkeerd_G5.json`; het voorgestelde G5-doel staat in `merge.voorstelDoel`.
- **terug-G3**: hoort volgens de regels in G3. G3 is definitief, dus deze items worden alleen gelogd in `data/terug_G3.json` en `logs/terug_g3.csv`.
- **geschrapt**: dubbele items. Zelfde doel, opgave, tekening, opties en antwoord: het eerste item blijft staan. Zie `logs/geschrapt.csv`.

## Besluiten Overzicht
Besluiten van Dave (1 okt 2026, 14:28) op de open vragen van Didactiek in `besluiten_twijfel.md`. Machineleesbaar in `besluiten_overzicht.json`; `scripts/besluiten_g4.py` legt ze over `besluiten_twijfel.json`.
1. **Centen-notatie: geen komma in G4.** De 28 items van 1 tot 2 euro (`CENT-1TOT2`) gaan naar **G5-GET-M03**. De 24 andere (22 onder €1, 2 hele euro's) blijven in G4-MEET-E07, met "45 cent" en "€2".
2. **Schaal:** streepje = 2 (83 items) blijft in **G4-VBN-E01**. Streepje = 5 (44 items, getal om de 10) gaat naar **G5-VBN-E01**, net als de 18 met getal om de 25.
3. **Ribben en hoekpunten** (3 items) gaan naar **G5-MKU-E02**, met uitleg van de begrippen.
4. **Centen-tweelingen:** het M5-item blijft staan en het M8-item vervalt, zoals Didactiek besliste (51 items, plus 1 M8-tweeling die eerder als 'dubbel' wegviel; zelfde regel).

Uitkomst van de 297 twijfelitems: **G4 112** (VBN-E01 83, MEET-E07 24, MKU-E03 4, GET-E09 1), **naar G5 134** (GET-M06 41, VBN-E01 62, GET-M03 28, MKU-E02 3; staan in `data/geparkeerd_G5.json` met `merge.didactiekG4`), **geschrapt 51** (+1 tweeling).

Voorwaarden uit `besluiten_twijfel.md`, toegepast op de G4-items (fixes B1–B6 in `logs/fixes.csv`):
- **B1/B2 schaal:** "Elk streepje is 2." staat boven de vraag; niveau toepassen (niet basis); `getallenruimte` volgt uit `max`; de visual-toelichting vraagt om de getallen om de 10; hint-richting staat in de md.
- **B3 geld zonder komma:** "45 cent" / "€2"; een heel bedrag als afleider bij een centenantwoord wordt "40 euro". `begripUitleg`: "100 cent is 1 euro." (bij het eerste gebruik). Tekening verplicht.
- **B4 fout-hints munten:** de zin "Bij teruggeven: …" is weg; een komma-hint ("eerste cijfer achter de komma") is vervangen.
- **B5 vlakken:** "Een vlak is een platte kant." staat boven de vraag. Tekening met doorzichtige of gestippelde achterkant verplicht; bij de piramide een vierkant grondvlak.
- **B6 trap:** "Treden zijn de stapjes van een trap." staat boven de vraag; "van de 1e naar de 3e verdieping"; tekening (3 verdiepingen, 2 trappen) verplicht. Het antwoord wordt nu automatisch gecontroleerd.
- Piramide herkennen (MKU-E03): tekening verplicht.

Sleutels: de bestaande 88 somtype-sleutels (`bevroren/somtype_nr_v1.json`) zijn niet veranderd. De 6 nieuwe somtypen hebben een nieuwe sleutel in **`bevroren/somtype_nr_v2.json`** (alleen aanvullingen; v1 blijft ongewijzigd). De build leest v1 + v2 en schrijft bij nieuwe somtypen een volgende aanvulling (v3, …). Items die van twijfel naar gemapt/park gingen hebben een nieuw id; het oude id staat in `bevroren/ids_v1.json` → `vorigeIds` en in `merge.vorigId`.
Nieuwe somtypen voor Oefeningen: G4-VBN-E01 #4 en #5 (streepje = 2: aflezen, meer dan), G4-MEET-E07 #1 (munten tellen in centen), G4-MKU-E03 #1 (vlakken tellen) en #2 (piramide herkennen), G4-GET-E09 #4 (trap).

## Splitsregels (R-codes)
- G01 rijen/sprongen: stap 2/5/10 (en 3/4, zoals in Didactiek G3 §2) tot 100 → G4-GET-M01. Stap 1 → G3-GET-M01. Andere stap → G5-VBN-E03. Boven 100 → G5-GET-M01.
- G02 getallenlijn: tot 20 → G3-GET-E02; tot 100 → G4-GET-E03 (getallenlijn 0–100, het kind tikt).
- G03 "precies tussen": tot 100 → G4-GET-E03.
- G05 tientallen/eenheden → G4-GET-E02.
- G06 tienstaven → G4-GET-M02 (er wordt gevraagd naar het aantal tienstaven of losse blokjes).
- G07 "Welke som hoort bij dit verhaal": +/− tot 100 → E04; × tot 100 → E06; deelsom → twijfel `deelteken`. G08 "op stap" (naar boven afronden) → E08.
- G09 kale tafels: tafel van 1–5 of 10 → E07, anders G5-GET-M05.
- G10 rooster × → M06.
- G11/G13 keer in context en omdraaien → E06. G12 groepjes maken → E08.
- G14 erbij/eraf in context tot 100 → M05 (subsleutel: hele tientallen / over het tiental / zonder overschrijding).
- G15 klok: hele uren → G3-MEET-E05; half en kwart → G4-MEET-E06; op de minuut → G5-MEET-E06.
- G16 geld: hele euro's tot €20 → G3, tot €100 → G4-MEET-E07; centen tot €2 → twijfel `centen` (besloten: zie 'Besluiten Overzicht'); meer → G5.
- G17 liniaal → MEET-E01. G18 km/mm → G5-MEET-E01.
- G19 kalender: tot 7 dagen verder → MEET-E06; verder of een tijdsduur → G5-MEET-E06.
- G20 referentiematen: m/cm → MEET-E02; kg → MEET-E05; g of l → G5.
- G21 kijklijn → MKU-E02. G22 route kiezen → MKU-E01. G23 spiegelen → MKU-E05.
- G24 ruimtefiguren: kubus/balk/bol/cilinder → MKU-E04; tellen (ribben/vlakken/hoekpunten) en piramide → twijfel.
- G25 tabel tot 100 → VBN-E01.
- G26 staafdiagram: schaal 1 → VBN-E01; 1 streep = 2 of 5 (tot 50) → twijfel `schaal`; meer → G5.
- G27 W1-puzzel zonder besluit → twijfel `puzzel`.

## G4-fixes (bovenop de G3-fixes F1–F6, W1, D1–D16, N1–N5, V1)
- **W5** woorden: zonnepanelen, robots, astronauten, dino-namen en keepers vervangen.
- **W6** "liggen … stappen" → schelpen.
- **W7** passende dingen bij "hebben elk".
- **W4** piramide/kegel als afleider vervangen.
- **F6b** geldnotatie €N / €N,CC.
- **F7** tikfouten (tafetafel/bussbus/dozdoos).
- **F8** "op de kinderboerderij".
- **F9** aan de tafel / met de bus.
- **N1** ':' in fout-hints.
- **N6** klokafleiders in kwartiertaal, in dezelfde notatie als het antwoord.
- **N7** ':'-afleider vervangen door een keersom ernaast.
- **N8** maatafleider zonder mm of komma.
- **V2** geen vakcode in de opgave (K9/K10).
- **V3** kijklijn-hints zonder Claude-rijnummer.
- **D12** Claude-fout-hints van een ander sjabloon vervallen.
- **D14/D17/D18/D19** de opgave verraadt het antwoord niet, en er is één handeling per vraag. Het rooster-antwoord staat in `antwoordIntern`.

Alle fixes staan in `logs/fixes.csv` en worden geteld in `logs/stats.json`.
`claudeUitleg` blijft intern (`extraVelden`); `controle.claudeUitlegInKindtekst` controleert dat.

## Bestanden
- Data:
  - `data/gemapt.json` en `data/per_doel/G4-*.json`;
  - `data/twijfel.json`;
  - `data/geparkeerd_G5.json`;
  - `data/terug_G3.json`.
- Somtypen: `somtypen/G4-*.md`.
  - Per somtype: een regel **Sleutel** (nrOrigineel/somtypeOrigineel) en lege regels Hint 1/Hint 2.
  - Zonder beeld: "Visual: nodig — niet live zonder beeld".
- Logs in `logs/`:
  - `fixes.csv`, `antwoordcontrole.csv` (ook de controle op de Claude-vorm);
  - `geschrapt.csv`, `terug_g3.csv`, `zelfde_als_bank.csv`;
  - `stats.json`, `somtypen_overzicht.json`, `somtype_indeling_huidig.json`, `hint_sleutels.json`.
- Bevroren: `bevroren/ids_v1.json` (met `vorigeIds`), `bevroren/somtype_nr_v1.json` en de aanvulling `somtype_nr_v2.json`.
- Besluiten: `besluiten_twijfel.md/.json` (Didactiek), `besluiten_overzicht.json` (Dave), `scripts/besluiten_g4.py`.
- Scripts:
  - `scripts/build_g4.py`, `regels_g4.py`, `merge_g3regels.py`;
  - `sync_hint_keys.py` (koppelt op claudeId, daarna op de kop), `apply_hints.py`, `fout_regels.py` (G3-kopieën);
  - `scripts/g3_basis_1359/` (G3-scripts van 13:59, alleen lezen);
  - `check_merge_notatie.py` en `check_hints.py` (G4-versies).

## Merge-fixlijst (1 okt, build 15:10)
Uitgevoerd: `merge-fixlijst.md` #1–#24 (Oefeningen en Didactiek), met de besluiten van Dave (14:51 en 14:59; Didactiek-variant uit `review-batch2-didactiek-v1.md` voor #17–#19 en #24). Script: `scripts/fixlijst_g4.py`, aangeroepen door `build_g4.py`. Fixes `X1`–`X25` staan in `logs/fixes.csv`, de tellingen in `logs/stats.json` → `fixlijst`.
- **Naar de G5-pool (26)**, met `merge.fixlijstG4` (de G5-merge neemt het doel over):
  - #2/#23 E08 #2 (7, tafel van 8 en 12) → G5-GET-M06;
  - #5 E06 #1 (10, groepjes of aantal >10) → G5-GET-E07;
  - #22 E06 #3 (4, 6×7, 7×9, 6×9, 7×8) → G5-GET-M05;
  - #7 E04 (5, uitkomst of afleider >100) → G5-GET-E05.
- **Geschrapt (306)**, in `logs/geschrapt.csv`, groep 'bijna dubbel (fixlijst)':
  - #17: M01 'ertussen', één item per rij per somtype, met de lege plek om de beurt op plek 2/3/4 (296). M01 gaat van 602 naar 306.
  - #13: E04 dezelfde som met alleen een andere zak/bak (10).
- **Gemarkeerd** met `merge.duplicaatVan` + `bijnaDuplicaat: true` + `rijGroep`: M01 dezelfde rij in een ander somtype (210), E06 #1 (17) en E06 #4 (5). Deze items blijven staan; de app moet ze niet in dezelfde sessie tonen.
- **Herschreven:**
  - #4/#6: E06 #1 heeft het aantal groepjes eerst (4 × 6); de afleiders zijn 4 + 6 en 5 × 6 (bij 10 groepjes 9 × b); 6 × 4 is nooit een foute optie; 2 en 2 wordt 3 groepjes van 2.
  - #22: E06 #3 heeft de lastige som buiten de G4-tafels: 3×10 → 3×9, 4×10 → 4×8, 5×10 → 5×7, en 9×10 → 10 × 9 is lastig, je rekent 9 × 10.
  - #12/#9: E06 #4 heet nu '… Dat is evenveel als 10 kinderen met elk 6 knikkers. Hoeveel knikkers zijn dat samen?'. Trainers wordt teams, kinderen met shirts krijgen sportschoenen, dino's met botten worden konijnen met wortels.
  - #8 manieren, #10 'Elke keer zagen', #11 '3 zakjes en 1 over', #24 'met sprongen van 3'.
  - #14: getallenlijn bij E03 #1 (0–100) en E08 #5 (0–20), met `gemarkeerd`.
  - MEET-E07 #1: €101 wordt €3 (het aantal munten; zie #32 hieronder).
  - #1/#3: E08 #2 'kinderen gaan eten / op stap', zonder kommagetallen.
  - #19: rijen met sprongen van 3/4 liggen op de tafelrij (5-8-11-14 → 3-6-9-12, 2-6-10-14 → 4-8-12-16, 6-10-14-18 → 8-12-16-20, 3-7-11-15 → 12-16-20-24), op kritisch. 29-24-19-14 wordt 30-25-20-15.
- **#18 niveau M01:** basis = achteraan omhoog, rijen tot 20 en sprongen van 10 op tientallen. Kritisch = sprongen van 3/4, en ertussen omlaag bij oneven rijen of rijen die niet op een tiental beginnen. De rest is toepassen. Uitkomst: 110 / 142 / 54 (36/46/18%).
- **Kop gewijzigd** (`merge.kopGewijzigd`; sync zet `kopGewijzigd` in de batch): E03 #1, E06 nrOrig 4, E06 #6, E08 nrOrig 5, E09 #2. Er zijn geen nieuwe somtype-sleutels (geen v3). Het somtype E08 nrOrig 2 heeft in G4 geen items meer.
- **fout_regels.py:** nieuwe regeltypes `fout = antwoord ± getal1` (ook `+`/`−`, `getal2`), `fout = eenheden als antwoord`, `fout = eenheden van getal1/2` en `fout = getal1 × getal2`.

### Merge-fixlijst #25–#33 (besluiten Dave 1 okt 15:16)
Ook in `scripts/fixlijst_g4.py` (functie `batch3`, alleen G4), fixes `X32`/`X33a`–`X33e` in `logs/fixes.csv`. Item-markering in `merge.fixlijst` (punt 25–33).
- **#25 GET-M05 plek en ding (50 items, nummers uit de lijst van Oefeningen):** past het ding bij een plek uit de lijst, dan krijgt het die plek (om de beurt). Past het ding nergens (tanden, blaadjes, poesjes) en is de plek goed, dan krijgt het een ding van die plek. Anders tanden → botten (museum), blaadjes → schelpen (museum), poesjes → vissen (dierentuin). 'Op de kinderboerderij', 'Op het veld', anders 'In de/het …'. Nest, vallei, moeras en bos komen niet meer voor bij deze 50. De kop blijft 'In [plek] liggen # [ding] …'.
- **#26:** geen actie (info).
- **#27 negatieve sleutels (14: M05 #2 12×, #6 2×):** '-33' (17 − 50) wordt 33 (de min andersom). Er botste niets met het antwoord of met een bestaande sleutel, dus er is niets geschrapt.
- **#28 (kleur 'rode strook/lijn'):** opgelost in ronde #34–#47 (zie hieronder).
- **#29:** 'kind uit groep 5' wordt 'kind uit groep 4' (MEET-E02 010, MEET-E05 001).
- **#30 naar de G5-pool (2):** MEET-E05 kat (afleider '400 g') → G5-MEET-E05, MEET-E02 voetbalveld (afleider '1000 m') → G5-MEET-E01. Samen met de 26 van #1–#24 zijn dat er 28, allemaal met `merge.fixlijstG4`; de G5-build neemt ze op.
- **#31 rooster (GET-M06 #1/#2, 30 items):** veld `appMoetDoorgeven: "aantalGekleurd"` (ook in `merge` en `antwoordIntern`). **De app moet het aantal gekleurde hokjes doorgeven** (liefst ook het aantal rijen en de hokjes per rij). Zonder dat getal kan geen enkele fout-regel ('getal1 + getal2', 'getal1', 'getal2') raken en krijgt elk fout antwoord de algemene fout-hint. Deze zin moet ook in de README van de export.
- **#32 geld:** in G4 één notatie, `€4` (euroteken, geen spatie, geen komma), in vraag, opties, antwoord en fout-sleutels (12 items, alle in MEET-E07; '1 euro en 50 cent' → '€1 en 50 cent'). Centen blijven 'N cent'. €101 → €3 (voorstel Oefeningen: het kind telt de munten). `fout_regels.py`: een letterlijke regel '3 euro' leest ook '€3', en een regel met een euroteken moet precies kloppen ('€3' raakt niet '€30').
- **#33:** 'kijkt recht naar rechts/links' wordt 'kijkt naar …' (MKU-E02 #1/#2, 12 items). **Kop gewijzigd** bij MKU-E02 #1 en #2 (`kopGewijzigd` + LET OP in `somtypen/G4-MKU-E02.md`).

### Merge-fixlijst #34–#48 (opdracht Dave 1 okt 15:51 en 15:56)
In `scripts/fixlijst_g4.py` (functie `batch4`, alleen G4; #45 in `pas_toe`), fixes `X34a`–`X34h` in `logs/fixes.csv`, markering in `merge.fixlijst`.
- **#28 + kleurregel Didactiek** (kleur alleen in een opgave als de app hem tekent, en nooit als enige aanwijzing): 'de rode strook' → 'de strook' (MEET-E01, 127), 'de rode lijn' → 'de lijn' (MKU-E05, 83). **Kop gewijzigd** (LET OP in de md).
- **#34:** GET-M05 'shirts' → 'truien' (6 items).
- **#35:** MEET-E02 012 stadsbus: afleider '120 m' → '50 m'; Claudes tekst bij '120 m' is weg, de letterlijke regel '50 m' van Oefeningen geeft de tekst.
- **#36:** MKU-E04 005 'een blokje uit een blokkendoos' → 'een dobbelsteen'.
- **#37 rooster MKU-E05 (83):** veld `appMoetTonen: "rijlettersEnKolomnummers"` (ook in `merge`). **De app moet bij het rooster rijletters (A bovenaan) en kolomnummers (1 links) tonen**, anders kloppen de fout-hints 'De letter klopt, maar het cijfer niet' niet. Toont de app ze niet, zet dan `ALT_AAN = True` in `hints/patch_batch4d.py` (Oefeningen; dit is de enige schakelaar, `patch_batch3b.py` doet er niets meer mee) en draai 4d en daarna 4e opnieuw: dan worden het de reserveteksten `MKU_ALT` «Je zit in de goede rij, maar niet in het goede hokje. …» en «Je zit recht boven of onder het goede hokje. …». Deze zin moet ook in de README van de export.
- **#38, #40–#42 (fout_regels.py, nieuwe regels):** `fout = klok een uur te laat` / `fout = klok een uur te vroeg` (zelfde minuten, ook half en kwart; leest `jsRender.klokken` of de tekst), `fout = grote wijzer verkeerd` (uur klopt, minuten niet), `fout = antwoord gedeeld door getal1` (streepjes geteld), `fout = een dag ernaast`, `fout = gestopt bij de laatste of eerste dag van de maand`, `fout = andere cel`, `fout = som van de rij`, `fout = som van de kolom`, `fout = som van twee cellen`, `fout = verschil van twee cellen` (uit `jsRender.rijen`). De teksten schrijft Oefeningen (hints/patch_batch4.py).
- **#39:** de klokken op 1:06, 2:06, 1:03, 2:03, 2:09 en 1:09 (MEET-E06 #12–#14, 6 items) worden het hele uur (bv. 1:00); Claudes fout-hint bij die klok is weg.
- **#43:** '"half één" is nog vóór een uur.' → 'Half één is nog vóór één uur.' (060, 071; zonder aanhalingstekens).
  Rest (review-batch4cd-didactiek-v1 §3, 1 okt 16:31): ook de andere Claude-teksten die met een woord tussen dubbele aanhalingstekens beginnen, zonder aanhalingstekens en met een hoofdletter: MEET-E06 #8 (055–059, 061, 062: «Half twaalf is nog vóór twaalf uur. …») en #10 (069, 070, 072, 073: «Kwart voor vier is nog vóór vier uur. …»), plus 1 item elders; in `foutHints` én `claudeFoutHints` (fixlijst_g4.py, X34f). Nu 0 dubbele aanhalingstekens in de fout-hints van G4.
- **#44:** VERH-E01 heeft maar 1 item (weegschaal). Gelogd (`merge.fixlijst` punt 44); er zijn geen items bijgemaakt.
- **#45 (opdracht Dave):** klokkenrij-items met een klok op x:20, x:35 of x:50 (22 items) gaan naar de G5-pool (G5-MEET-E06 'Tijd tot op de minuut'). Let op: de fixlijst stelde voor die klok te vervangen (zoals #39); hier is de opdracht van Dave gevolgd.
- **#46:** VBN-E01 tabel: afleiders boven 100 (35 items) → afleiders ≤ 100 uit de tabel zelf (andere cel in dezelfde kolom of rij, dan rij- of kolomsom ≤ 100, dan antwoord ± 10). De oude fout-hints bij die afleiders zijn weg.
- **#47:** tabelvragen met een werkwoord: 'Hoeveel peren zijn er op dinsdag?', 'Hoeveel peren zijn er op maandag meer dan op dinsdag?', 'Hoeveel appels zijn er in totaal?' (195 items). **Kop gewijzigd** bij VBN-E01 #1–#3.
- **Streepje = 5:** komt in G4 niet meer voor (besluit 2: naar G5-VBN-E01).
- **#48 (fout_regels.py):** (1) een `claude-taalfix` met een onleesbare regel en een vaste tekst (zonder '…') zet nu die vaste tekst op de Claude-sleutels (`claudeDenkfout`), in plaats van Claudes eigen tekst per item. (2) `vul_in` vult ook `[getal1]`, `[getal2]` en `[antwoord]` per item in (ook als `{getal1}`), bv. «Het is een keersom: [getal1] keer [getal2].» → «… 6 keer 10.». In de huidige hints veranderde dat geen enkele kindtekst (getest met een proefregel); `foutRegels` geeft nu ook de vaste tekst mee.

- **#49 (nieuw, review 4cd §3; fout_regels.py):** de regel 'fout = gestopt bij de laatste of eerste dag van de maand' is gesplitst in **'fout = gestopt op de eerste dag van de maand'** (de 1e van de latere maand) en **'fout = gestopt op de laatste dag van de maand'** (de laatste dag van de vroegste maand), elk met een eigen tekst. MEET-E06 #3 (later) gebruikt nu 'eerste dag' (15/15 sleutels), #4 (eerder) 'laatste dag' (12/12); aangepast in `hints/batch4.json` en `GRENS` in `hints/patch_batch4d.py` (de teksten van 4e blijven). De oude gecombineerde regel blijft werken (beide datums). Zelfde motor-update in de kopieën in g5/, g6/ en g7/scripts/fout_regels.py.

**Patchvolgorde hints (vast, 1 okt 16:35):** `python3 hints/patch_batch4d.py` en **daarna** `python3 hints/patch_batch4e.py` (anders zet 4d velden van 4e terug), dan `python3 scripts/build_g4.py` (draait zelf `sync_hint_keys.py` en `apply_hints.py`). Staat ook in de docstring van `scripts/build_g4.py`. Ronde 4e: taal: ok (16:35).

**Stand build 1 okt 16:33 (na #43-rest en #49, hints ronde 4c/4d/4e):** 3.433 rijen: gemapt 1.819 · park-G5 1.585 · terug-G3 29; 0 FOUT. Hints 93/93 klaar, `check_hints` 0 FAIL / 0 WARN / 2 INFO, `check_merge_notatie` ALLES OK. Bevroren sleutels ongewijzigd (geen nieuwe vN).

**Stand definitieve build (1 okt, na #48):** 3.433 rijen: gemapt 1.819 · park-G5 1.585 · terug-G3 29; 0 FOUT. Hints 93/93 klaar, `check_hints` 0 FAIL / 0 WARN / 2 INFO, `check_merge_notatie` ALLES OK.


## Rebuild 17:55 (#63 referentiematen; opdracht 1 okt 17:50)
- scripts/referentie_g4.py (in build_g4.py na FX.pas_toe): referentie-teksten uit /workspace/claude-merge/referentiematen_treffers.md in de merge-data.
  MEET-E02 004 ('zo breed als twee duimen naast elkaar'), 006 ('de hand van een volwassene'), 008 ('iets langer dan je pink'), 012 claudeUitleg ('ongeveer anderhalf klaslokaal').
- **SLEUTELWIJZIGING MEET-E02 010 (gymschoen):** antwoord 25 cm → **20 cm**, opties 25 cm · 25 m · 1 m → **20 cm · 20 m · 1 m**, Claude-sleutel 25 m → 20 m, claudeUitleg nieuw.
  Gelogd in merge.sleutelWijziging en logs/fixes.csv ('G4-REF63 … SLEUTELWIJZIGING'). Hint-regel '25 m' → '20 m' (tekst gelijk) via hints/patch_ref_63.py (log: wijzigingen_batch3.json).
- Verder niets veranderd (semantische diff met de build van 16:40: alleen MEET-E02 001–012; 001–003/005/007/011 alleen foutRegels van de gedeelde entry).
- check_merge_notatie: REF (checkPatronen = FAIL, zacht = WARN): 0 · 0. check_hints: 93 klaar · 0 FAIL. De canonieke G4-bank (MEET-E05 #004/#008) is niet aangeraakt.

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
