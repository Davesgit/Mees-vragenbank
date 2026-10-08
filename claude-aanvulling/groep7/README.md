# G7 Claude-merge (1 okt 2026, stap 1–3; rebuild 17:10 met de besluiten van Didactiek en Dave)

Dit is de G7-merge van de Claude-vragenbank (`/workspace/claude-bank-src`, CC BY-SA 4.0) naar LeerMees. De aanpak is dezelfde als bij G4, G5 en G6.
- **Gelezen** wordt alleen uit `claude-bank-src`, `claude-merge/g3`–`g6` en `exports/`. De G7-bank en de G7-Claude-pilots worden alleen gelezen via `exports/leermees-vragenbank-export/vragenbank_g7.json`.
- **Geschreven** wordt in deze map en in `g6/data/aanvulling_uit_g7.json`.
- **De canonieke `rekenen-groepN/bank/` is niet aangeraakt.** De checksums zijn vóór en na gelijk.
- **Sleutels zijn bevroren:** `bevroren/ids_v1.json`, `bevroren/somtype_nr_v1.json` (140 somtypen) en `somtype_nr_v2.json` (17:10: 5 nieuwe somtypen voor de besluit-items: G7-MEET-02 #1 driehoek m², #2 driehoek cm²; G7-VERH-04 #4 'welk deel', #5 'hoeveel procent', #6 'delen vergelijken'). 145 somtypen.

## Draaien
```
python3 scripts/build_g7.py        # bouwt alles en draait zelf sync_hint_keys.py + apply_hints.py
python3 check_merge_notatie.py     # notatie (exit 1 bij FAIL) — nu ALLES OK
python3 check_hints.py             # hints per somtype (nu: alles 'open') — nu ALLES OK
```
Een rerun is stabiel: ids en somtypen veranderen niet, alleen de tijdstempel verschilt. Gooi `bevroren/*.json` niet weg zodra er hints zijn. Een nieuw somtype komt in `somtype_nr_v2.json`; v1 blijft staan. Eén correctie in v2 (8 okt, Oef-#465): `G7-VERH-04#4` zonder de 2 rad-items bank-136/137. Die staan sinds v6 onder `#7` ([rad]; Leerlijn: het rad hoort bij nrO 7). sync_hint_keys koppelt op de eerste passende versie; met de rad-ids in v2 gaf dat 'items verdeeld over #4: 7, #7: 2' (check_hints FAIL). De weggehaalde ids staan in het veld `correctie` van die entry. Regel: verhuist een item later naar een ander somtype, haal het dan ook uit de oudere versie die er nog naar verwijst, met een `correctie`-veld.

## Pool
- Alle Claude-items van de G7-doelen (rekenleerweg groep 7).
- Plus de items die de G6-merge voor G7 parkeerde (`g6/data/geparkeerd_G7.json`). Dat zijn er **3.060**, niet 2.886: na de G6-rebuild van 16:17 kwamen er de 146 kale breuksommen en de 28 omgedraaide dubbels uit de G6-twijfel bij (besluit Didactiek en Dave).
- Niet mee: wat al in G3–G6 zit (gemapt, geschrapt, twijfel of terug). Dat waren 12 items: de B14-operatoritems die G6 voor G6-GET-E09 uit de G7-pool haalde.
- **Stand 17:10: pool 8.650 → gemapt 7.074 · twijfel 0 · park-G8 688 · terug-G6 764.** Geschrapt: 124 (dubbel 4, dubbel-pilot 36, elfden begrensd 51, besluit Didactiek mediaan 21, kans 12). 0 FOUT; 283 gemapt 'n.v.t.' (vooral DENK-meerkeuze in woorden). Vóór de besluiten (16:43): gemapt 6.804 · twijfel 303.

## Bestemmingen (`scripts/regels_g7.py`, classify_g7)
| status | betekenis | bestand |
|---|---|---|
| gemapt | in een G7-doel | `data/gemapt.json`, `data/per_doel/G7-*.json`, `somtypen/G7-*.md` |
| twijfel | Didactiek beslist (4 categorieën); sinds 17:10 leeg | `data/twijfel.json`, `twijfel_voor_didactiek.md`, besluiten in `besluiten_twijfel.md/.json` |
| park-G8 | te moeilijk voor G7; voorstel-G8-doel in `merge.voorstelDoel` | `data/geparkeerd_G8.json`, `logs/park_g8.csv` |
| terug-G6 | te makkelijk voor G7; met een G6-doel | `data/terug_G6.json`, `logs/terug_g6.csv` en `g6/data/aanvulling_uit_g7.json` |

**Te makkelijk → terug-G6:**
- delen door 1 cijfer tot 1000 (G6-GET-M06) of tot 10.000 (G6-GET-E06);
- prijs/aantal met een hele factor (G6-VERH-E01, 546);
- deel ↔ totaal met een breuk (G6-VERH-E04);
- korting als aftreksom (G6-GET-V02);
- snelheid in hele uren (G6-MEET-E09);
- geld × 1 cijfer (G6-GET-E07).

**Te moeilijk → park-G8:**
- boven 1 miljoen (G8-GET-M01);
- volgorde van bewerkingen (G8-GET-E03);
- breuk × breuk, heel : breuk en ongelijknamige breuken (G8-GET-E04);
- procent met komma (G8-VERH-E06);
- terugrekenen na korting (G8-VERH-E04);
- kaartschaal boven 1 : 1000 (G8-VERH-E03; alle V7);
- negatieve getallen zonder temperatuur (G8-MEET-E05);
- snelheid met halve uren (G8-MEET-E07);
- rekenregel/spaartabel (G8-VBN-E03).

## Notatie en afspraken G7 (besluit Dave)
- 'a : b' mag in G7 voor verhouding en schaal. ':' is het deelteken, nooit '÷' (G7-N1). Procent mag.
- Ketensommen schrijf je voluit.
- Duizendtallen zoals de canonieke G7-bank: 4 cijfers zonder punt, vanaf 10.000 met punt.
- Kommagetallen zoals de G7-bank: Nederlandse komma, zo kort mogelijk (4,50 → 4,5; G7-K1, niet bij geld en niet bij 'Rond af op') en hoogstens 3 decimalen. Met 4 decimalen → twijfel.
- Minteken '−', ook bij een negatief getal ('−4 graden', G7-N2). Geld '€37,50' (G7-F1). Liter 'L'. cm³ en m³ in plaats van 'kubieke cm' en 'kubieke meter' (G7-W1).
- Schaal met uitleg zoals de G7-bank: 'Dat betekent: 1 cm op de tekening is n cm in het echt.' (G7-S1, 11).
- **Didactiek-voorwaarden voor de 123 breuksommen uit de G6-twijfel** (`scripts/g6_basis/besluiten_g6.py`):
  - breuken in cijfers, '−' en 'Typ een breuk.';
  - 'het geheel' in plaats van 'de taart';
  - 'Tel de stukjes nog eens' bij een telfout in de teller;
  - geen vereenvoudiging nodig.
  Dezelfde vorm geldt voor de 76 B7-sommen uit de G6-park.
- **Elfden (besluit Dave):** hoogstens 12, gespreid over de somtypen: 6 plus en 6 min. De andere 51 zijn geschrapt als 'elfden begrensd': 40 sommen en 11 omgedraaide elfden-dubbels.
- **Omgedraaide dubbels (besluit Dave):** de 17 die over zijn, blijven als oefening in wisselen (`merge.wisselOefening`, `duplicaatVan` = het origineel).

## Besluiten twijfel (Didactiek `besluiten_twijfel.md/.json`, 303 items; Dave 16:59) · `scripts/besluiten_g7.py`, codes D7-* in `logs/fixes.csv`, veld `merge.didactiekG7`
- **Vier decimalen (216 → G7-GET-02):** het 4-decimale getal is ingekort volgens de regel van Didactiek (per id uit de json; 180 met hetzelfde antwoord, **36 met een nieuw antwoord**, `didactiekG7.antwoordWas`). Fout-hints opnieuw per nieuwe fout. Denkfout 'kommagetal-als-geheel' alleen bij de fout die uit de valkuil 'langer = groter' komt (**144** items, zoals Didactiek telde), de rest 'tienden-niet-vergeleken' (`merge.decimalenMC`).
- **Echte meerkeuze (Dave 5):** alle 432 'Welk getal is het grootst/kleinst?'-items in GET-02 (216 uit de twijfel + 216 die al gemapt waren) hebben de drie getallen als opties; de vraag staat zonder 'Kies uit'. Voor de dubbelcontrole (pilot/bank) geldt de oude vorm met de getallen (`merge.opgaveVoorMC`).
- **'Welke is kleiner?'** bij alle 216 'kleinst'-items (108 uit de twijfel + 108 gemapt); daar stond 'Welke is groter?'. Nu 0 keer 'groter' bij 'kleinst'.
- **Driehoek (36 → G7-MEET-02):** 10 houden, 20 aanpassen: de context per id uit `wijzigingen` ('in de kantine' → 'op het schoolplein', 'in de vallei' → 'in het weiland', …); 002 fout-sleutel '31.5' → '31,5'. **De 6 dubbele maten blijven (Dave 1)** met een nieuwe basis, hoogte en een nieuw verhaal, nagerekend (alle 36 controle ok): 024 bloemperk in het park 7 × 6 m → 21 · 026 stuk weiland 9 × 8 → 36 · 027 zandvak op het schoolplein 13 × 6 → 39 · 032 moestuintje in de schooltuin 14 × 9 → 63 · 033 grasveld bij de speeltuin 18 × 5 → 45 · 035 stuk grond op het erf 7 × 10 → 35 (fout-sleutels: de rechthoek, plus, twee keer gedeeld). Geen paar komt twee keer voor, ook niet omgedraaid. **Plaatje verplicht:** `visual.nodig = true`, `jsRender {soort: 'driehoek-in-rechthoek', basis, hoogte, eenheid, hoogteStippellijn, arcering, label 'de helft'}`. Voor de hint (`merge.hintEis`): 'basis × hoogte is de rechthoek eromheen; de driehoek is de helft daarvan'.
- **Mediaan (26):** 21 geschrapt (Dave 2). 004, 013, 017, 019, 022 → **'gemiddeld'-vragen in G7-GET-04** (opgave, antwoord en fout-hints uit de json; 019 'trainers' → 'teams'). In de kindhints van GET-04 425–430: 'Dat is het middelste getal (de mediaan)' → 'Dat is het middelste getal'. Nu 0 keer 'mediaan', 'trainer' of 'shirt' in een G7-item.
- **Kans (25):** 12 geschrapt (KANS-VO, ook dobbelsteen en munt, Dave 3). 13 → **G7-VERH-04** als 'Welk deel van de … is …?' of 'Hoeveel procent van de … is …?' (opgave, opties en antwoord uit de json; opties 'zoveel op de zoveel', met 'de'). Fout-hints zonder 'kans' en zonder 'onder de streep' (bv. 003 '2 op de 6' → 'Tel alle vakjes van het rad, ook de groene.'). Rad 002/003: `visual.nodig = true`, `jsRender {soort: 'rad', vakjes, gemarkeerd: {kleur, letter R/G, patroon 'gestreept'}}` (kleur niet het enige kenmerk). Het woord 'kans' staat in geen enkel G7-item meer. Eigen narekening van het deel (onafhankelijk van Didactiek, op gelijkwaardigheid): 13/13 ok.
- **Geldige antwoorden (Dave 4):** `antwoordDetail.geldigeAntwoorden` = het antwoord + Didactiek 'ookGoed' (003 '1 op de 4', 009 '2 op de 5', 011 '1 op de 3', 024 en 025 '1 op de 2'). De checker gebruikt deze vaste lijst. **Later moet de engine gelijkwaardige verhoudingen zelf accepteren** ('2 op de 8' = '1 op de 4' = '1/4' = '25%'); de vaste lijst is een tussenstap.
- **G7-VBN-05 nagekeken (Dave 6):** in de hele merge stonden alleen de 26 mediaan-items op VBN-05 (`voorstelDoel`, regel G7-D02-mediaan, allemaal twijfel). Er was geen enkel gemapt item, ook geen park- of terug-item. Na de besluiten staat er niets meer op VBN-05; niets te verplaatsen. De regel in `classify_g7` stuurt een nieuw mediaan-item nog naar twijfel; die zou nu bij Didactiek 'schrappen' zijn.
- Canonieke banken: checksum vóór en na gelijk.

## Ontdubbelen
- Binnen de merge: zelfde doel, opgave, tekening, opties en antwoord → de eerste blijft (4 geschrapt).
- **Tegen de G7-Claude-pilots** (`claudeVarianten` in de export, 160 pilot-items; alleen gelezen):
  - een gelijke opgave na normalisatie (÷/:, −/-, punten, spaties, 'Reken uit:') wordt geschrapt als 'dubbel-pilot';
  - een gelijke som (getallen + bewerking) bij hetzelfde doel ook (36 in totaal: 20 GET-03, 14 GET-01, 1 MEET-04, 1 MEET-03);
  - zelfde getallen zonder dezelfde som → alleen de vlag `merge.lijktOpPilot` (1).
- Tegen onze G7-bank: `merge.zelfdeOpgaveAlsOnzeBank` (1). Tegen de G6-merge: `zelfdeAlsG6` (0). Zie `logs/zelfde_als_bank.csv`.

## G7-bewerkingen (`regels_g7.bewerk_g7`, codes in `logs/fixes.csv`)
- N2 '−' bij een negatief getal (1.778 vervangingen) · W1 cm³/m³ (1.373) · K1 kommagetal zo kort mogelijk (27) · S1 schaaluitleg (11)
- W3 'Een ei meet 7,19 l. Hoeveel ml is dat?' → 'Vul in. 7,19 L = ... ml' (12; een onzinnige meetcontext)
- R1 rooster-antwoord '2x2' → 'een rechthoek van 2 hokjes breed en 2 hokjes hoog' (9, zoals G4/G5), met een kleurbaar rooster
- N3 'x' → '×' in een optie (2) · W2 '0,6 deel van' → '0,6 van' (5) · F1 '€ 37.5' → '€37,50' (2)
- Daarvoor de hele keten G3 → G4 → G5 (G6_MODUS) → G6 (`scripts/g6_basis/`). Herverificatie op de bewerkte vorm: `verify_g7` → `verify_g6` → `verify_g5` → `verify_g4` → `verify2` → G3-`verify`. Nieuw in `verify_g7`: staafdiagram uit de tabel, temperatuur, procent, verhouding, schaal, maten herleiden, inhoud, afronden op decimalen en delen met rest.

## Caveats
- **De app** moet een gelijkwaardige breuk goed rekenen (1/2 = 2/4) en '-' als '−' accepteren bij het typen van een negatief getal.
- Het taartbeeld (`jsRender soort 'taart'`) is een nieuw prototype; dat speelt in G6-VERH-E02. In G7 zijn 9 rooster-items `nietLiveZonderBeeld`.
- **MEET-03 is groot (1.702):** M18, inhoud l × b × h, heeft 1.360 items (838 'inhoud → hoogte' en 518 'l × b × h').
- V7 (kaartschaal, 229) gaat helemaal naar G8-VERH-E03. C20 'negatief zonder temperatuur' (229) gaat naar G8-MEET-E05.
- Voor G6-GET-E09 'aanvullen tot 1' zijn er geen Claude-items. Breuk als operator: 12, opgenomen in G6.
- Veel Claude-fout-hints zijn algemeen en passen niet bij het somtype (zie `hints/README.md`). Dat lossen de hints per somtype op.
- DENK-03 (24 items in 24 somtypen) en DENK-02 (13 in 13) zijn losse verhaalsommen. Elk somtype heeft 1 item.

## Bestanden
- `scripts/build_g7.py` (build), `scripts/regels_g7.py` (classify, bewerk, verify, notatie G7).
- `scripts/g6_basis/`: kopie van `regels_g6.py` en `besluiten_g6.py` na de rebuild van 16:17, plus `g5_basis/` met de G5-, G4- en G3-keten.
- `scripts/apply_hints.py`, `sync_hint_keys.py` en `fout_regels.py`: zoals in G4–G6 (fout_regels met G4 #49 en G5 #12).
- `check_merge_notatie.py` en `check_hints.py`: de G7-versies. Procent en verhouding mogen. FAIL bij KOMMA4, NEG ('-' als minteken), '÷' en 'x' als keerteken. WARN in de hints boven 1.000.000.
- `logs/`: stats, fixes, geschrapt (dubbel, dubbel-pilot, elfden begrensd), antwoordcontrole, terug_g6, park_g8, zelfde_als_bank, hint_sleutels en somtype_indeling_huidig.

## Rebuild 17:32 (opdracht Dave 17:17)
- Twijfel en besluiten van 16:59 waren al verwerkt (rebuild 17:10). Nagekeken na deze rebuild:
  - **vier-decimalen:** 216 items, alle 444 'Kies uit'-items van GET-02 zijn meerkeuze, met de opties in het optieveld en de vraag zonder 'Kies uit'. 0 keer 'Welke is groter?' bij 'kleinst'. De 12 andere GET-02-items gaan over afronden (open vraag).
  - **driehoek:** 36/36 met een verplicht plaatje. De 6 dubbels hebben een nieuwe basis, hoogte en verhaal.
  - **mediaan:** 5 → GET-04 (gemiddelde), 21 geschrapt. 'het middelste getal' bij 425–430.
  - **kans:** 13 → VERH-04 met antwoordDetail.geldigeAntwoorden (13/13), 12 geschrapt. VBN-05 heeft geen items meer.
- **Nieuw:** FX21 (`scripts/fx21.py`) in alle kindvelden en extraVelden. In G7 waren er 0 hits in opgaven en 1 in extraVelden (terug_G6).
- **Nieuw:** 'kans' en 'mediaan' ook uit extraVelden. Bij 12 kans-items stond 'De kans is …' in claudeUitleg, en 'kans vereenvoudigen'/'kansen vergelijken' in claudeStrategie. Bij de 5 gemiddelde-items stonden claudeKaleSom, claudeStrategie en claudeUitleg nog op mediaan; die zijn herschreven naar de som en de deling (nagerekend). Het oude staat in merge.extraVeldenVoorBesluit. claudeFoutHintsVoorBesluit staat nu in merge in plaats van in extraVelden.
- check_merge_notatie ENG: FAIL bij 'trainer', 'shirt', 'kans' of 'mediaan' ergens in een item (niet in bron, licentie of de bevroren oude sleutels). Nu 0.
- Tellingen: gemapt 7074 · park-G8 688 · terug-G6 764 · geschrapt: mediaan 21, kans 12, dubbel 4, dubbel-pilot 36, elfden begrensd 51. check_hints 0 FAIL (145 open), notatie ALLES OK.

## Rebuild 17:47 (motor en checkers uit G5 #59–#64)
- scripts/fout_regels.py = die van G5: '10.000' wordt als 10000 gelezen, en sleutels van 5 of meer cijfers staan in beide vormen ('10000' en '10.000'). De app moet allebei accepteren.
  Nieuwe regels (maatbeker, afgerond op tientallen) zijn alleen actief als een hint-entry ze gebruikt.
- check_merge_notatie: OPP (FAIL: oppervlakte = omtrek bij een omtrekvraag) en REF (haak /workspace/claude-merge/tools/referentiematen_check.py, WARN). Nu 0 en 0.
- Opnieuw gebouwd; de aantallen zijn gelijk gebleven.

## Notatie van maten (machten) aangezet (18:05, notatie_machten.md van Didactiek)
- `check_merge_notatie.py` gebruikt de gedeelde haak `/workspace/claude-merge/tools/machten_check.py` (regel MAAT; G8 gebruikt dezelfde haak).
  - In elke groep FAIL: MACHT (macht van een getal), ASCII ('m2', 'cm3', 'm^2'), MENG ('vierkante cm', 'kubieke cm').
  - G7: ² en ³ ok, 'kuub' ok, 'a' voor are FAIL. INTRO: WARN per somtype met cm³, dm³, m³, km² of ha zonder het woord in de opgave, Hint 1 of Hint 2. MACHT in de R-lijst is nu gelijk aan G4–G6 (`\d\s?[²³]`).
- Stand na de rebuild van 18:06 (zelfde aantallen: gemapt 7074 · park-G8 688 · terug-G6 764):
  - MAAT 0 FAIL;
  - INTRO 4 WARN, allemaal in MEET-03: 4, 32, 838 en 518 items. Het woord moet nog in Hint 1 van #1, #2, #9 en #10. Dat doet Oefeningen (notatie_machten.md §7).
  - Niets teruggedraaid: de 1373 vervangingen van G7-W1 ('kubieke cm' → cm³) blijven.
- **De G7-pilots gaan niet live** (Overzicht 18:00). De `claudeVarianten` in de canonieke G7-bank worden vervangen door deze merge. Overzicht laat ze bij de volgende export vervallen of markeert ze. De canonieke bank is niet aangeraakt. Hun MENG-hits ('vierkante cm' in G7-MEET-02-claude-pilot 004, 'kubieke cm' in G7-MEET-03-claude-pilot 004) hoeven daarom niet opgelost te worden.
- **App-eis bij antwoorden met een eenheid (gekozen in plaats van extra vormen in de merge-data):**
  - De eenheid staat naast het invulvak (`unitHint`), dus het getal alleen is goed.
  - De app normaliseert de invoer op één plek, voor alle items:
    - spaties weg, kleine letters;
    - 'm2', 'm^2' en 'm²' worden m², 'cm3', 'cm^3' en 'cm³' worden cm³ (zo ook voor mm, dm, dam, hm, km);
    - 'vierkante (centi/deci/kilo…)meter' en 'kubieke …meter' worden het symbool, net als de mengvormen 'vierkante cm' en 'kubieke cm' (bij invoer mogen die);
    - 'kuub' wordt m³ (vanaf G7) en 'hectare' wordt ha;
    - komma en punt als decimaalteken, en een duizendpunt mag;
    - een slotnul na de komma verandert de waarde niet (Z-#607): bij antwoord 7,8 is '7,80' goed, bij antwoord 2,0 is '2' goed (en '2,00'), bij €3,50 ook '3,5'. Vergelijk dus op waarde, niet op tekst.
    - uitzondering (Z-#607, besluit Didactiek 8 okt): vraagt de opgave een aantal cijfers achter de komma ('Rond af op één/twee cijfer(s) achter de komma'), dan is alleen precies dat aantal cijfers achter de komma goed: minder én meer cijfers zijn niet goed (Z-#683). Bij 2,0 is '2' dan fout; die invoer heeft een eigen sleutel 'decimaal-nul weggelaten' (motorregel, 'Bijna!' mag). Bij «één cijfer achter de komma» zijn ook '2,00' (antwoord 2,0) en '3,80' (antwoord 3,8) fout: dat is geen notatie volgens de opdracht. Daarvoor is er nog geen eigen sleutel; die invoer krijgt de algemene fout-hint. Geldt in G5–G8; nu alleen G7 GET-02 #3 (12 items, 2 met antwoord op 0: bank-001 en bank-006).
  - Goed is: het getal klopt, en de eenheid ontbreekt of is na normalisatie gelijk aan de gevraagde eenheid. Een andere eenheid is fout.
  - De screenreader leest het symbool als woord voor (aria-label: m² → «vierkante meter», cm³ → «kubieke centimeter», km² → «vierkante kilometer»).
  - De merge-data krijgen daarom geen extra antwoordvormen; zie notatie_machten.md §6 (Didactiek).
- Rebuild 18:06 ook met de motor van G5 #68–#72 (scripts/fout_regels.py, gelijk aan G5): kloktijd in woorden, 24 uur, regels met richting voor minuten en datums, 'over en voor verwisseld'. Ze werken pas als een hint-entry ze gebruikt.

## Rebuild 18:39: kalender uit G5 (G5-fixlijst #75)

- `scripts/build_g7.py` leest ook `g5/data/geparkeerd_G7.json`: 220 items 'Hoeveel dagen duurt het van … tot …?'. Dagen tellen tussen twee datums is G7 (Didactiek 18:15). De items zijn gemapt op G7-MEET-04, regel G7-G5P7-dagen-tussen-datums, en alle 220 zijn ok.
- De hints van G5 (batch 5 #1) gaan mee: hint1, hint2 en ouderzin, en de fout-hints via dezelfde motor (`merge.hintsUitG5`, `merge.g5Park`).
- Motor `scripts/fout_regels.py` is gelijk aan die van G5 (#76/#77/#81/#82). Cijfers: gemapt 7294 · park-G8 688 · terug-G6 764.

## Vanuit G8 (1 okt 19:05)
- `data/aanvulling_uit_g8.json`: de G8-merge (`g8/scripts/build_g8.py`) zet hier 46 items neer die terug moeten naar G7 en een G7-doel hebben (DENK-02/03, GET-04, MEET-02). De G7-build is daarvoor niet aangepast.
- `scripts/fout_regels.py` is gelijk aan die van G5 (#92–#94, #103, #104). Rebuild 19:05: 7294 · 688 · 764, niet veranderd, ALLES OK. Na-ronde 2 (build 15:41:07): V-#746 (strategie 'gunstig van totaal'), Z-#748 (bank-134 'groter dan 7' = 3 op de 10, bank-135 letter N = 2 op de 6; HELFT-check WARN 0), Z-#750 (nietLiveZonderBeeld op de rad-items), Z-#751 ('1 op de 4' bij bank-125; etiket '#4 (vereenvoudigen)' weg).
