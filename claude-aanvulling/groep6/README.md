# G6 Claude-merge (1 okt 2026, stap 1–3)

De G6-merge van de Claude-vragenbank (`/workspace/claude-bank-src`, CC BY-SA 4.0) naar LeerMees, met dezelfde aanpak als G4 en G5.
Gelezen wordt alleen uit: `claude-bank-src`, `claude-merge/g3`, `g4`, `g5` en `exports/`. Geschreven wordt in deze map en in `g5/data/aanvulling_uit_g6.json`. De G7-build schrijft `data/aanvulling_uit_g7.json` (764 terug-G6-items, alleen ter aanvulling; deze build is daarvoor niet aangepast).
De canonieke `rekenen-groepN/bank/` is niet aangeraakt. De sleutels zijn bevroren (`bevroren/ids_v1.json`, `bevroren/somtype_nr_v1.json`; aanvulling `somtype_nr_v2.json` (16:17) met 3 nieuwe somtypen: G6-GET-E07#2 geld-keer uit G5, G6-GET-E09#3 breuk als operator (12), G6-VERH-E02#5 taartverhalen (10)).

## Draaien
```
python3 scripts/build_g6.py        # bouwt alles en draait zelf sync_hint_keys.py + apply_hints.py
python3 check_merge_notatie.py     # notatie (exit 1 bij FAIL)
python3 check_hints.py             # hints per somtype (nu: alles 'open')
```
Een rerun is stabiel: alleen de tijdstempel verschilt. Gooi `bevroren/*.json` niet weg zodra er hints zijn. Een nieuw somtype komt in `somtype_nr_v2.json` (v1 blijft staan).

## Pool
- De Claude-items van de G6-doelen (rekenleerweg groep 6). B12 en G11 doen niet mee, want die zaten al in de G5-pool.
- Daarbij de 2.305 items die de G5-merge voor G6 parkeerde (`g5/data/geparkeerd_G6.json`).
- Niet mee: alles wat al in G3, G4 of G5 zit (gemapt, geschrapt, twijfel, terug). Dat waren 12 items (K10, gemapt in G4).
- Pool 7.200 → gemapt 3.950, twijfel 188, park-G7 2.886, terug-G5 169, dubbel 7. 0 FOUT.

**Stand na de rebuild met de besluiten van Didactiek en Dave (1 okt 16:17):** pool 7.220 → **gemapt 3.980 · twijfel 0 · park-G7 3.060 · terug-G5 169**. Geschrapt: 4 (Didactiek: 2 DUBBEL-BANK, 2 DUBBEL-VERHAAL) + 7 dubbel. 90 somtypen. Notatie ALLES OK, hints 0 FAIL. 0 FOUT.
- +30 gemapt: 8 geld-keer uit de G5-twijfel (G6-GET-E07, '€7,88', 'een zak wortels'/'een stickervel', -004 basis), 10 taartverhalen (G6-VERH-E02, met plaatje), 12 breuk-als-operator uit de G7-pool (G6-GET-E09).
- park-G7 2.886 → 3.060: +146 kale breuksommen (G7-GET-05) en +28 omgedraaide dubbels (oefening in wisselen, besluit Dave).
- Zie `twijfel_voor_didactiek.md` (de lijst, de besluiten en wat ermee gedaan is), `besluiten_twijfel.md/.json` en `scripts/besluiten_g6.py`.

## Bestemmingen (`scripts/regels_g6.py`, classify_g6)
| status | betekenis | bestand |
|---|---|---|
| gemapt | in een G6-doel | `data/gemapt.json`, `data/per_doel/G6-*.json`, `somtypen/G6-*.md` |
| twijfel | Didactiek beslist (1 categorie: `breuken-plus-min`) | `data/twijfel.json` |
| park-G7 | te moeilijk voor G6; voorstel-G7-doel in `merge.voorstelDoel` | `data/geparkeerd_G7.json`, `logs/park_g7.csv` |
| terug-G5 | te makkelijk voor G6; met een G5-doel | `data/terug_G5.json`, `logs/terug_g5.csv` en `g5/data/aanvulling_uit_g6.json` |

Grenzen: getallen tot 100.000 (meer → G7-GET-01), cijferen tot 10.000 (meer → G7-GET-03/04), +/− en ×/: tot 1000 → terug-G5,
kommagetallen met meer dan 2 cijfers achter de komma → G7-GET-02, kale kommasommen zonder geld → G7-GET-03, procent → G7-VERH-02,
inhoud in kubieke cm (l × b × h) → G7-MEET-03, schaal '1 : 100' → G7-VERH-03.

## Notatie en afspraken G6
- '×' en ':' mogen overal; ':' is het deelteken ('12 : 4'). **'4 : 5' als verhouding of schaal hoort niet in G6** (besluit Dave: pas in G7, Verhoudingen). Die items staan in park-G7.
- **Ketensommen voluit:** '7 × 4 = 28 en 28 + 12 = 40', nooit '7 × 4 = 28 + 12 = 40' (G6-N1).
- Breuken in cijfers (3/4). Kommagetallen mogen, maar met hoogstens 2 cijfers achter de komma.
- 4 cijfers zonder punt (8265), vanaf 10.000 met punt (12.500). Geld '€6,60', '€21'. Liter = 'L'. 'Eén', niet 'Één'.
- G5-regels in G6-modus (`scripts/g5_basis/regels_g5.py`, `G6_MODUS = True`): breuken niet in woorden, 'Typ een breuk' blijft, geen ':'-uitleg.
- Geldantwoorden met € ook in G6-GET-V02, E05, E07, MEET-V01, E08.

## G6-bewerkingen (`regels_g6.bewerk_g6`, codes in `logs/fixes.csv`)
- **G6-D1 (de 4 FOUT in G6-GET-E03 033–036 uit de G5-park):** bij 033, 035 en 036 stonden twee 'wel'-breuken ook in de 'niet'-lijst (bv. hetzelfde als 1/4: niet 2/8, 3/12). Die zijn vervangen door een breuk met dezelfde noemer en teller ± 1 (3/8, 4/12), gelogd in `merge.g6Fix`. Nu G6-GET-E03-claude-bank-1108, 1110 en 1111. **034 was een vals alarm:** de G3-check las het sleepvak als 'ordenen'. De nieuwe check (wel = gelijk, niet = ongelijk) keurt 034 goed (nu 1109).
- G6-N2: 'Welke breuk is het kleinst. 3/4, 2/5 of 3/11?' → 'Welke breuk is het kleinst? Kies uit 3/4, 2/5 of 3/11.' (816). De G3-regel had de ':' al in een punt veranderd.
- G6-N4: 'groepjes van 10: 150, 154, …?' → 'Je kunt kiezen uit 150, 154, 144 en 156. Welk aantal …?' (32; een ':' na een getal leest als deelteken).
- G6-N3: liter = L, ook na □ (80). G6-F2c: 4 cijfers zonder punt, ook vlak voor een punt (185 items; de G3-regel sloeg 'er 8.265.' over).
- G6-W2: 'Vereenvoudig 4/6.' → 'Schrijf 4/6 zo eenvoudig mogelijk.' (550).
- G6-W3 t/m W7 (rare dingen weg): '3 2/8 stappen' → '3 2/8 = ?/8' (18), '15/4 stappen' → '15/4 pizza' (14), '3/5 van een vis is een deelsom' → 'De breuk 3/5 …' (15), 'Kleur 1/3 deel van' → 'Kleur 1/3 van' (8), 'In een tabel staat. …' (2). G6-F1: 'een ander konijn' (10).
- Herverificatie op de bewerkte vorm: `verify_g6` → `verify_g5` → `verify_g4` → `verify2` → G3-`verify`.

## Twijfel (voor Didactiek)
**Beslist (0 open), zie `twijfel_voor_didactiek.md`.** Was: `breuken-plus-min` (188: B7 104, B8 84): breuken met dezelfde noemer optellen of aftrekken, uitkomst ≤ 1 ('2/4 + 1/4 =', 'Een konijn eet 1/5 van een taart en een ander konijn eet 1/5. Welk deel is samen op?'). Voorstel G6-GET-E09; de G6-spine noemt optellen van breuken niet, alternatief G7-GET-05.

## Caveats
- G6-GET-E03 is groot (1.124): ook vereenvoudigen (B9, 558) en 'met noemer' (B6) staan daar, omdat de G6-spine geen eigen doel heeft voor gelijkwaardige breuken.
- M18 (1.361, inhoud l × b × h) en V1 (182, procent) gaan helemaal naar G7. M19 schaal (24) is geparkeerd vanwege de notatie '1 : 100'.
- Kale kommasommen zonder geld (B12, 432) gaan naar G7-GET-03.
- Claude schreef duizendtallen soms met een komma; F1 maakt daar een punt van (240 items).
- De 169 terug-G5-items hebben allemaal een G5-doel (G5-GET-E05 82, E07 75, VBN-E01 12). De G5-build is hiervoor niet aangepast.
- 24 gemapte items hebben geen automatische controle ('n.v.t.'), vooral W4-schema's en tekstopties.

## Bestanden
- `scripts/build_g6.py` (build), `scripts/regels_g6.py` (classify, bewerk, verify, notatie G6), `scripts/g5_basis/` (kopie G5-regels met G6_MODUS, plus `g4_basis_1435/` met de G4- en G3-keten).
- `scripts/apply_hints.py`, `sync_hint_keys.py`, `fout_regels.py`: zoals in G4/G5 (fout_regels = de G4-versie van 1 okt 16:00, met #38–#42 en #48; sinds 16:38 ook G4 #49 en G5 #12/#14).
- `scripts/besluiten_g6.py`: de besluiten van Didactiek en Dave (classify, voorwaarden, taart, E09).
- `check_hints.py` en `check_merge_notatie.py`: G6-versies (zie de docstring).
- `logs/`: stats, fixes, geschrapt (dubbel), antwoordcontrole, terug_g5, park_g7, zelfde_als_bank, hint_sleutels.

## Rebuild 17:32 (opdracht Dave 17:17)
- **FX21 (G5-fixlijst #21/#49)** staat nu ook in G6 (`scripts/fx21.py`): 'trainer'/'shirt' → 'kind'/'trui' in alle kindvelden, extraVelden, foutHintsTekst en optiesTekst, vóór de somtype-indeling. Er waren hits in 17 opgaven, 4 fout-hints en 4 extraVelden (gemapt), plus terug_G5 en park-G7. Nu 0, ook in g5/data/aanvulling_uit_g6.json.
- check_merge_notatie: ENG = FAIL (zoals in G5).
- Tellingen: gemapt 3980 · park-G7 3060 · terug-G5 169 · twijfel 0. check_hints 0 FAIL (90 open), notatie ALLES OK.

## Rebuild 17:47 (motor en checkers uit G5 #59–#64)
- scripts/fout_regels.py = die van G5: '10.000' wordt als 10000 gelezen, en sleutels van 5 of meer cijfers staan in beide vormen ('10000' en '10.000'). De app moet allebei accepteren.
  Nieuwe regels (maatbeker, afgerond op tientallen) zijn alleen actief als een hint-entry ze gebruikt.
- check_merge_notatie: OPP (FAIL: oppervlakte = omtrek bij een omtrekvraag) en REF (haak /workspace/claude-merge/tools/referentiematen_check.py, WARN). Nu 0 en 0.
- Opnieuw gebouwd; de aantallen zijn gelijk gebleven.

## Notatie van maten (machten) aangezet (18:05, notatie_machten.md van Didactiek)
- `check_merge_notatie.py` gebruikt de gedeelde haak `/workspace/claude-merge/tools/machten_check.py` (regel MAAT; G8 gebruikt dezelfde haak).
  - In elke groep FAIL: MACHT (macht van een getal), ASCII ('m2', 'cm3', 'm^2'), MENG ('vierkante cm', 'kubieke cm').
  - G6: cm², dm² en m² ok; km², hm², dam² en mm² WARN; ³ FAIL; 'a' voor are FAIL; 'kubieke', 'kuub' en 'hectare' WARN. INTRO: WARN per somtype met cm², dm² of m² waar het woord niet in de opgave, Hint 1 of Hint 2 staat. HA: WARN.
- Stand na de rebuild van 18:06 (zelfde aantallen: gemapt 3980 · park-G7 3060 · terug-G5 169):
  - MAAT 0 FAIL;
  - INTRO 4 WARN, allemaal in MEET-E03. Het woord moet nog in Hint 1. Dat doet Oefeningen, bijvoorbeeld «cm² is een vierkante centimeter: een vierkantje van 1 cm bij 1 cm.».
- **G6-W8 (regels_g6.py):** in de opgave, de opties, het antwoord en de fout-hints wordt 'vierkante cm' cm² (385 keer in MEET-E03) en 'vierkante meter' m² (4 items: opgave, antwoord en opties; 398 vervangingen in logs/fixes.csv). De somtype-koppen houden cm² en m² (NIET_DING). Er is geen nieuw bevroren nummer bijgekomen.
- **App-eis getallenlijn met kommagetallen (G6-fixlijst #7, 20:10; aangescherpt #153, Didactiek 20:15, besluit Dave 20:16):** GET-M03 #1 ('Zet 6,7 op de lijn van 0 tot 10', 24 items 009–032). (1) **Teken de lijn van 0 tot 10 ook met een streepje per tiende**, net als 0–2: `visual.getallenlijn.streepjePer` = '0,1' en `streepjesPerTiende` = true bij alle 24 items. (2) **Beoordeel de stip met banden** (veld `beoordeling`, soort 'banden'): goed als |x − antwoord| < 0,05; 'één tiende ernaast' als 0,05 ≤ |x − antwoord| < 0,15, met de richting (groter = 'één tiende te ver', kleiner = 'één tiende te kort'); een fout-sleutel s geldt als |x − s| < 0,05. (3) Er staan geen sleutels buiten [van, tot] (de motor laat ze weg). Fout-sleutels bij kommagetallen hebben een komma en geen slot-nullen; de invoer normaliseert punt naar komma en haalt slot-nullen weg (VORM #105). (4) Open (#153e): begint de stip van de app op 0, dan hoort 'beginpunt' een eigen regel en tekst te krijgen (Oefeningen).
- **Stand 20:08 (G6-fixlijst #1–#7):** gemapt 3980 · park-G7 3060 · terug-G5 169. check_hints 17 klaar · 0 FAIL · 0 WARN. check_merge_notatie ALLES OK (nieuw: FIX6). Zie merge-fixlijst.md.
- **Stand 20:40 (ronde 2: #152–#157):** gemapt 3980 · park-G7 3060 · terug-G5 169 · geschrapt 11. check_hints 17 klaar · 73 open · 0 FAIL · 0 WARN · 9 INFO. check_merge_notatie ALLES OK (FIX6 0, DOELID 0). 26 E01-items met een nieuw getal (#152), M03 #1 024 → 8,6, 16 M02-opgaven rechtgezet (#156g). Zie merge-fixlijst.md.
- **App-eis sorteren in twee vakken (G6-fixlijst #195, Didactiek 21:25, besluit Dave 21:25):** GET-M05 #3 ('Sleep elk getal naar het goede vak: deelbaar door N of niet.'), veld `beoordeling` (soort 'sorteren') bij elk item. (1) **Vergelijk elk vak als verzameling**: de volgorde binnen een vak telt niet (de antwoorden en sleutels staan als 'wel:…|niet:…' met de getallen gesorteerd als tekst). (2) Precies één getal verkeerd: de sleutel met de richting (#193): 'fout = een deelbaar getal bij niet' of 'fout = een niet-deelbaar getal bij deelbaar'; vangnet 'fout = één getal in het verkeerde vak' (#163). (3) Alle getallen in het andere vak: 'fout = vakken omgewisseld'. (4) **Twee of meer getallen verkeerd: 'andere fout'** (algemeneFoutHint). De sorteersom zelf en #163 blijven zoals ze zijn. Dezelfde app-regel geldt voor E03 #9 (breuken sorteren; Didactiek recheck 2b, #199).
- **Pas live met een getekende lijn (G6-fixlijst #186, Didactiek batch 3 21:42):** de 12 items van GET-E03 #7 ('Zet 3/5 op de lijn van 0 tot 1') hebben `vereistTekening: true`. Ze gaan pas live als de app de getallenlijn echt tekent (`visual.getallenlijn`: streepje per 1/noemer, alleen 0 en 1 erbij; `jsRender` is nog leeg). Eén stuk te kort heet nu 'tellen vanaf 1 in plaats van 0' (motorregel `fout = tellen vanaf 1 in plaats van 0`), één stuk te ver blijft 'één stuk ernaast'.
- **Niveau breuken vergelijken (G6-fixlijst #180, Didactiek batch 3 21:42):** in GET-E03 #2/#3 ('Welke breuk is het grootst/kleinst? Kies uit …') blijven alleen items waarin elke vergelijking met het antwoord kan met dezelfde teller, dezelfde noemer, een noemer die een veelvoud is van de andere, een kleinste gemeenschappelijke noemer van hoogstens 24, of met de helft. De rest (306 items) gaat naar park-G7 (G7-GET-05, regel 'G6-B06-vergelijken-niveau180'). Bewaker: `fixlijst_g6.fix180` (assert in de build) en FIX6 ronde 5.
- **App-eis breuk op de getallenlijn (G6-fixlijst #169, besluit Dave 21:24):** GET-E03 #7 ('Zet 3/5 op de lijn van 0 tot 1'), veld `beoordeling` (soort 'banden'), net als #153: een streepje per stuk (noemer), goed binnen een half stuk, 'één stuk ernaast' (met richting) tussen een half en anderhalf stuk. 2/4 en 1/2 zijn dezelfde plek.
- **Even grote breuk is goed (G6-fixlijst #170, besluit Dave 21:24; `tools/breukvorm.py`):** bij een breukantwoord staan de even grote breuken in `antwoordOokGoed` en `breukGelijkwaardigGoed` = true, behalve als de opgave een vorm vraagt ('zo eenvoudig mogelijk', 'met noemer N', '?/N') of een plek op de lijn. Dan is het antwoord streng en is de even grote breuk de sleutel 'fout = gelijkwaardig maar niet zo eenvoudig mogelijk'. check_merge_notatie: BREUKVORM (FAIL).
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
- Rebuild 18:06 ook met de motor van G5 #68–#72 (scripts/fout_regels.py, gelijk aan G5): kloktijd in woorden, 24 uur, regels met richting voor minuten en datums, 'over en voor verwisseld'. Ze werken pas als een hint-entry ze gebruikt.

## Eisen voor de app (Oefeningen/app-bouwer; stand na ronde 7, build 22:29:55)
Deze eisen volgen uit de merge-punten. De merge-data voldoen eraan, en de genoemde guard bewaakt dat bij elke build. De app moet ze ook zelf aanhouden.
1. **Het goede antwoord is nooit een foutsleutel** (#223). In `foutRegels.match.waarden` staat het antwoord nooit, ook niet buiten tabellen (`ANTWOORD_UIT_WAARDEN = True` in `scripts/apply_hints.py`). Guard: assert in de motor en in FIX6. De app beoordeelt eerst 'goed' en pas daarna de sleutels.
2. **'Bijna!' alleen bij een antwoord vanaf 10** (#216). Een regel kan eindigen op '(antwoord vanaf N)' of '(antwoord onder N)'. In MEET-E03 #2 is ± 1 zo gesplitst: vanaf 10 'Bijna! ' + de tekst, onder 10 zonder 'Bijna!'. Guard: assert op alle 'Bijna!' in G6-MEET. In de bredere regel (G6 algemeen): 'Bijna!' alleen bij precies één stap.
3. **Kommagetallen normaliseren mag** (#218). De app mag '3,80' en '3,8' als dezelfde invoer zien. De data bevatten bij een sleutel met een slotnul ook de vorm zonder (114: '3,80' en '3,8'). **'3,8' is dan een foutsleutel, geen goed antwoord**: het goede antwoord van 114 is 12,53, dus er is geen antwoordOokGoed.
4. **Komt er later een plaatje bij E03 #5, dan mag kleur niet het enige kenmerk zijn** (#227, les 11). Nu is `visual.nodig = false`. De eis staat per item in `visual.eisAlsErEenPlaatjeKomt`.
5. **Bordtitels en spine** (#217): de merge-titels staan in `data/per_doel` en `somtypen/*.md`, de oude in `bordtitelBank`. Het canonieke bord (`rekenen-groep6/bank/`) en de spine worden alleen via Oefeningen/Leerlijn aangepast, nooit vanuit de merge.
6. **Volgorde van de regels telt** (#214): in MEET-E03 #2 staat 'zijde uit de vraag' (`fout = getal2`) vóór 'afgehaald' en ± 1. De app neemt de eerste regel die past. Guard: `_e214_216` in `scripts/fixlijst_g6.py`.
7. **Twee lagen per fout-hint** (#229, ronde 8): zie het blok 'Ronde 8' hieronder.

**Guards van ronde 7 (in de build, `scripts/fixlijst_g6.py`, en in `check_fixlijst_g6.py` → `ronde7()`):**
- #211: in elk MEET-E03-item met lengte × breedte is 2 × (l + b) ≠ l × b (en l + b ≠ l × b). 285 is daarom 7 × 3.
- #180/#221: noemer ≤ 20 in elk grootst/kleinst-item (`regels_g6.niveau180` en `fix180`). '½ duidelijk' = |breuk − ½| ≥ 1/20 en 2 × teller ≠ noemer. 814: 1/22 → 1/12 vóór de indeling (`voor_classify221`). 24 #180-items die naar G7 zouden gaan, vullen aan (`NIEUW221`, vaste keuze per hash).
- #210: 'eenheden niet keer gedaan' en 'cijfers opgeteld' slaan een waarde over die een deelproduct is (`fout_regels.deelproducten`). Assert per sleutel in FIX6.
- #216: elke 'Bijna!' in G6-MEET hoort bij een antwoord ≥ 10.
- #223: het antwoord staat in geen enkele `match.waarden`.
- #158: geen G6-GET- of G6-MEET-item boven 100.000 (getal en antwoord), ook ná de fixlijst (`grens158`, FAIL in FIX6).

**Nog uit ronde 2–4 (in de fixlijst al beschreven, hier samengevat):**
- **#156d (besluit Dave 20:38) en #159b:** de vraag in de kindtekst beslist. Alle afrondsomtypen in E01 vragen 'Rond … af op …' en hebben 1 à 2 middengetallen (TERUG156, MIDDEN156; ook x5 bij tientallen). Hint 2 noemt de regel '5 of meer, dan rond je af naar het … erboven'. 'het dichtst bij' en 'dichtst' komen niet voor in een somtype met een middengetal. FAIL in FIX6 (`check_fixlijst_g6.py`).
- **#158:** G6 = hele getallen tot 100.000. `_bereik` in fix152 kiest bij duizendtallen n ≥ 10.000, bij tienduizendtallen 10.000–99.999. E01 #1 049/055/057/058/060/066/068/076 hebben een nieuw getal van 5 cijfers. De ouderzinnen noemen 'tot 100.000'. Guard: assert in de build en FAIL in FIX6.
- **#159c (Dave 20:49):** de helft van de #152-getallen (11 van de 21) heeft een nul binnenin, de andere helft niet (`NUL152`).
- **#160:** M02 #4 (201–208) heeft geen 'de teller' in de opgave, en de aantallen kunnen echt. Bij E01 #5/#7/#8 past de context bij het aantal (`bewerk_na`). Geen kindtekst noemt 'teller' in M02 #4.


## Ronde 9 (8 okt 2026, build 10:58:34; Didactiek recheck-ronde5c, recheck-ronde4d6b; uitgevoerd door Overzicht)
- Draaien: `bash keten_r8.sh` (build → sync → apply → check_hints → check_merge_notatie met FIX6). G6 leest `../g5/data/geparkeerd_G6.json`: eerst G5 bouwen.
- Cijfers: gemapt 4227 (4193 + 10 uit G5 + 24 generator). check_hints: 0 open · 0 FAIL · 0 WARN · 9 INFO. check_merge_notatie: ALLES OK. FIX6 (ronde 3–9): 0 FAIL. motor_regressie: 4227 items, 0 anders.
- **#331 (verplicht):** VERH-E01 001–004 met de getallen van Didactiek (10 kg → €15; 6 broden → €8; 6 pakken → 24 glazen; 5 flessen → 15 L) en hun opties. Guard `guard331` in de build en `ronde9()` in FIX6.
- **#231/#281:** aanvulling (niet samenvoegen) van de dunne VERH-somtypes: 24 generator-items (VERH-E01 #1: 11, VERH-E02 strook: 6, VERH-E02 deel van een hoeveelheid: 7). Guards: VERH-E01 #1 heeft 12–15 items, VERH-E02 #3 en #4 elk ≥ 9, #3 in beide richtingen, geen 'schaal'. `na_alle` stopt met een FAIL als `aanvul231` ontbreekt.
- **#321:** 10 items uit G5-GET-E07 #6 → `G6-GET-E06-claude-bank-uitg5-NNN` (toepassen, getallenruimte 0–10.000, nieuw somtype nrO 8 in `bevroren/somtype_nr_v5.json`, hints via `hints/batch7.json`).
- **#235:** MKU-E01 #3 (vak G#) en #4 (vak H#) samengevoegd met #1 ('[plattegrond] Wat staat er in vak [vak]?'), 12 items, ook de items uit de aanvulling uit G8. `hints/koppeling_merge.json`: samengevoegd 3 → 1 en 4 → 1 (entries gelijk, gecontroleerd).
- **#276/#332:** VBN-E02 #1: elk aantal streepjes (1–5) komt 12 keer voor (`bevroren/vbn276_streepjes_v1.json`, haalbaar per item); het antwoord is nooit een waarde van een van de twee maanden uit de vraag. Bordtitel VBN-E02 in de merge: 'Lijngrafiek aflezen'.
- **#333:** VBN #1 en #3 met de nieuwe motorregels 'fout = de andere maand uit de vraag' en 'fout = de som van een deel van de maanden'.
- **#344:** MKU-E03 'basis' alleen met minder dan 3 torens achter een hogere: 14 items uit 'basis' (13 naar 'kritisch' door tekeneis B, 1 naar 'toepassen').

## Eisen voor de app, aanvulling ronde 9
8. **Breukplaatje (#277):** komt er een plaatje bij een breuk, dan is kleur niet het enige kenmerk (ook arcering of een lijn), net als #227.
9. **Plattegrond met hoogtegetallen (#295):** de H2-tekst `hint2MetPlaatje` (MKU-E03 #1) gaat pas live als er een echt plaatje bij Hint 2 is. Tot dan toont de app de gewone Hint 2. De plattegrond is geen knop: het kind tikt niet op vakjes, het antwoord gaat via de invoer.
10. **Op `id`, niet op `nr`** (G5 #329): somtypenummers schuiven als er een somtype bijkomt (ronde 9: GET-E06).

## Ronde 10 (8 okt 2026, build 11:21:56; Didactiek gate-ronde9-deelA en -deelB, uitgevoerd door Overzicht)
- Zie `merge-fixlijst.md` (ronde 10).
- Volgorde in de keten: `bash keten_r8.sh` → `python3 hints/patch_batch4.py` (de hm/dl-entries komen pas in batch4 als de items er zijn) → `scripts/sync_hint_keys.py` → `scripts/apply_hints.py` → checks.
- Nieuwe somtypes: MEET-E01 #8–#11 (hm) en MEET-E04 #5–#8 (dl), bevroren in `somtype_nr_v6.json`.
- Motor: #380 (letterlijke regels alleen op het hele getal, plus de regel 'de helft van het aantal hokjes') en #390 (een getal uit de vraag krijgt nooit ±1 of 'Bijna!').
