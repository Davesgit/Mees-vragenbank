# Claude-merge pilot groep 3 (stap 1–3 + stap 2b)

Gegenereerd door `scripts/build_g3.py` (idempotent; schrijft alleen onder deze map). Bron: read-only clone van https://github.com/Davesgit/leermees-vragenbank @ 7da3257. Bestaande bankbestanden niet aangeraakt.

Licentie/credit per item in `licentie`: CC BY-SA 4.0 — “Leermees open vragenbank, CC BY-SA 4.0, leermees.nl”, `gewijzigd: true` + lijst wijzigingen. Bron in `bron` (claudeId, doel, repo, commit).

## Per G3-doel

| doel | gemapt | somtypen | items zonder hints (somtype open) | geschrapt |
|---|---|---|---|---|
| G3-GET-E01 | 1 | 1 | 0 | 0 |
| G3-GET-E02 | 4 | 3 | 4 | 0 |
| G3-GET-E03 | 5 | 5 | 5 | 3 |
| G3-GET-E04 | 211 | 7 | 0 | 0 |
| G3-GET-E05 | 28 | 2 | 0 | 0 |
| G3-GET-E06 | 11 | 5 | 11 | 0 |
| G3-GET-K01 | 48 | 5 | 0 | 0 |
| G3-GET-K03 | 57 | 1 | 0 | 0 |
| G3-GET-K05 | 144 | 5 | 0 | 0 |
| G3-GET-M01 | 262 | 7 | 30 | 0 |
| G3-GET-M02 | 109 | 4 | 10 | 0 |
| G3-GET-M04 | 28 | 2 | 0 | 0 |
| G3-GET-M05 | 124 | 7 | 1 | 0 |
| G3-GET-M06 | 223 | 6 | 1 | 0 |
| G3-MEET-E01 | 1 | 1 | 0 | 0 |
| G3-MEET-E03 | 1 | 1 | 0 | 0 |
| G3-MEET-E04 | 2 | 1 | 0 | 0 |
| G3-MEET-E05 | 84 | 3 | 0 | 0 |
| G3-MEET-K01 | 7 | 2 | 1 | 0 |
| G3-MEET-K03 | 5 | 1 | 0 | 0 |
| G3-MEET-K04 | 7 | 1 | 0 | 0 |
| G3-MKU-E02 | 109 | 8 | 27 | 0 |
| G3-MKU-E03 | 27 | 1 | 27 | 0 |
| G3-MKU-E04 | 2 | 1 | 2 | 0 |
| G3-MKU-K03 | 11 | 2 | 0 | 7 |
| G3-VBN-E03 | 24 | 1 | 0 | 0 |

Totaal (stand 1 okt 13:50): gemapt 1519 in 83 somtypen, twijfel 0, geparkeerd 626 (G4, `data/geparkeerd.json`, veld `merge.voorstelDoel`), geschrapt 26 (`logs/geschrapt.csv`: 10 besluiten Didactiek + 16 dubbele items: 6 in M01, 10 klok zetten in MEET-E05). Alle 83 somtypen hebben hints (batch1–4).

## Mapregels
Zie `merge.regel` + `merge.reden` per item; regels R01–R27 staan in het script (functie `classify`).

## Let op
- `niveau` is voorlopig (Claude 1 → basis, 2/3 → toepassen; `extraVelden.niveauVoorlopig`).
- `hint`, `sterkereHint`, `ouderzin`: gevuld uit `hints/batch*.json` voor de somtypen met status 'hints klaar'; leeg voor de open somtypen (batch 4).
- 10 dubbele klok-items in G3-MEET-E05 gemarkeerd met `merge.duplicaatVan` (niet verwijderd).

## Bestanden
- `data/gemapt.json`, `data/twijfel.json`, `data/geparkeerd.json`, `data/per_doel/<doel>.json`
- `somtypen/<doel>.md` — somtypen, aantallen, 2 voorbeelden, hint-blokken (of lege regels Hint 1/Hint 2 bij open somtypen)
- `logs/fixes.csv`, `logs/antwoordcontrole.csv`, `logs/stats.json`, `logs/somtypen_overzicht.json`

## Stap 2b (1 okt 2026): besluiten Didactiek, fixes, hints

**Pijplijn** (alles rerunbaar; altijd eerst `rm -rf data somtypen logs`):
1. `python3 scripts/build_g3.py`: mapt, past de twijfelbesluiten toe (`besluiten_twijfel.json`: G3 → gemapt, G4 → geparkeerd, schrappen → `logs/geschrapt.csv`), doet de fixes (`scripts/merge_stap2.py`, functie `bewerk`), controleert de antwoorden opnieuw op de bewerkte vorm (`controle.*`; de controle op Claudes vorm staat in `controle.claudeVorm`), en schrijft `data/`, `somtypen/`, `logs/`. Item-ids blijven stabiel via `bevroren/ids_v1.json`; nieuwe items krijgen het volgende vrije nummer (`merge.vorigId` = het oude twijfel-id).
2. `scripts/sync_hint_keys.py` (start build_g3.py zelf): zet `nr` en `somtype` in `hints/batch*.json` gelijk aan de koppen in de nieuwe md. De oorspronkelijke waarden blijven staan als `nrOrigineel` / `somtypeOrigineel`. batch1–3 worden gekoppeld via `bevroren/somtype_nr_v1.json` (de md-nummers van toen). Een latere batch (batch4 …) koppelt op `somtype`; zonder `somtype` op het `nr` van de md van dat moment. Geef in batch4 dus graag het veld `somtype` mee. Problemen staan in `logs/hint_sleutels.json`. Backup van de batches vóór de eerste sync: `../_backup/hints_v1/`.
3. `scripts/apply_hints.py` (start build_g3.py zelf; los te draaien, ook voor één batch): schrijft de hint-blokken in de md (formaat en kopcontrole van Oefeningen; bron-tags `[nieuw]`, `[Claude, ok]`, `[Claude, taalfix]`; een onbekende bron stopt het script). Zet per item `hint`, `sterkereHint`, `ouderzin` en de fout-hints (`scripts/fout_regels.py`). De basis is `extraVelden.claudeFoutHints`, dus opnieuw draaien geeft hetzelfde. Herschrijft `data/gemapt.json` en `data/per_doel/*.json`. Oefeningens versie: `../_backup/apply_hints_oefeningen_1300.py`.
4. Checks: `python3 check_merge_notatie.py` en `python3 check_hints.py`.

**Fout-hints per item** (`fout_regels.py`): de regels per somtype gelden van boven naar beneden; de eerste die past, wint. Kandidaten zijn bij meerkeuze de foute opties, bij tikvragen alle vakken van het raster, bij invullen Claudes fout-antwoorden plus de waarden die een regel opsomt. 'tekst per item' houdt Claudes eigen tekst. Sjablonen zoals '[uur in woorden]' worden per item ingevuld. Bij ' / ' (twee teksten van Claude, ook bij een taalfix) kiest het script de tekst die bij het item hoort. In het item staan `foutHints` (met `regel`/`bron`), `foutRegels` (de matchers, voor de app) en `algemeneFoutHint`. Velden: `controle.zonderFoutHints` en `controle.claudeUitlegInKindtekst` (meldt een zin uit claudeUitleg in een kindveld; er wordt niets weggehaald).

**Vakken: één afspraak voor de hele bank: letter = rij (A bovenaan), cijfer = kolom (1 links).** Claude gebruikte letter = kolom (A links) en cijfer = rij (1 onderaan). Alle codes in opgave, opties, antwoord, fout-hints en tekening zijn omgerekend (`V1` in `logs/fixes.csv`; rasters tot 12 kolommen). Spiegelen en de G3-routes zijn tikvragen geworden: het kind tikt op het vak en kiest geen code (`antwoordDetail.tikVak`). Claudes tekening staat in `extraVelden.claudeBeeld`; de oude uitleg met codes in `extraVelden.claudeUitlegOudeVakcode` (intern). Waar Claude geen tekening gaf, is het raster aangenomen (`jsRender.rasterAangenomen`): K4 = 5 kolommen × 4 rijen, K9 = 6 × 5 (met een vlag als startpunt).

**Andere fixes** (soorten en aantallen in `logs/stats.json`, per veld in `logs/fixes.csv`): minteken '−' in opgave, opties en antwoord; ':' + getal wordt een punt of een zin (K01, M04, M05-6, fout-hint E06); de ×-afleider in E04-2/E05-2 is vervangen door a + (b+1); rijen kleuren met het antwoord intern (`antwoordIntern`); woorden (merge-fixlijst + Didactiek); kan A/B wordt de rode/blauwe kan; klokkenrij: opties A, B, C in de volgorde van de kloklabels en `Husselen: nee`; M06-5: het gevraagde deel wisselt (4 van de 8 items vragen nu de losse, bijvoorbeeld '16 is □ en 10'); ongepaste Claude-fout-hints zijn vervallen (D12). `claudeUitleg` blijft intern in `extraVelden` en gaat nergens naar het kind.

## Laatste ronde (1 okt 13:38, Oefeningen)
- M06-5: het tiental wordt gegeven bij 12, 15, 17 en 18 (antwoord = de losse); bij 13, 14, 16 en 19 blijft 10 het antwoord. 2 even en 2 oneven per groep, niet om en om (`M06_5_LOSSE`).
- De ×-afleider wordt a + (b+1); bij b = 9 wordt het a + (b−1). Nooit een 10 in de afleider.
- M05-6: 'Splits 3. 3 is 1 en □.' (notatie als M05-4).
- M02 tienstaven: 'Leg 18 met een tienstaaf en losse blokjes. Hoeveel losse blokjes leg je?' (antwoord 8); 'Leg 20 met tienstaven. Hoeveel tienstaven leg je?' (antwoord 2). Claudes fout-hints bij het oude antwoord zijn vervallen.
- Puzzels (E03 1–5, E06-5, M05-7, M06-6): `visual.nietLiveZonderBeeld = true` plus een korte beschrijving; in de md staat 'Visual: nodig — niet live zonder beeld'.
- M01: van de 5 items '2, 4, 6, 8, □' blijft er 1 (`…-235`); 4 staan in `logs/geschrapt.csv` (groep 'dubbel').
- MEET-K01-2: 'Op tafel liggen een boek en één blaadje papier. Wat is dikker?'.
- MKU-E03: regel 'stip niet verplaatst' (fout = het vak van de stip) staat vóór de algemene regels. Zolang Oefeningen geen tekst heeft, staat er een plaatshouder (`controle.foutHintPlaceholder`, in de md '[merge, plaatshouder]'). Met een regel 'stip niet verplaatst …' in de batch vervalt de plaatshouder vanzelf.
- E06 rooster: het rooster is al gekleurd (`jsRender.gekleurd`, `kleurbaar: false`); het kind vult alleen het getal in.
- Koppeling hints ↔ koppen: `bevroren/somtype_nr_v2.json` = de md waarop batch4 geschreven is. sync_hint_keys.py koppelt eerst via de bevroren indeling (op claudeId) en daarna via de kop. Verandert een kop door een fix, dan krijgt de entry `kopGewijzigd` en zet apply_hints.py een 'LET OP kop gewijzigd' in de md.
- MKU-E02 #4–8 (routes, 27 items; Didactiek 13:51): elke kaart heeft het startpunt plus 3 andere dingen (`jsRender.dingen`, extra dingen met `afleider: true`). De extra dingen staan op typische foutvakken (alleen de eerste stap, een stap de verkeerde kant op, een hokje te ver of te kort); alleen de route komt bij het antwoord uit. De antwoorden zijn ongewijzigd en worden gecontroleerd (fix D16).

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
