# LeerMees vragenbank — export rekenen groep 3 t/m 8

Gegenereerd: 2026-10-01T18:54:53+02:00 (Europe/Amsterdam) · 1996 items · schema `leermees-vragenbank-export/v1`

Dit is een **letterlijke export** van de LeerMees-rekenbank (`/workspace/rekenen-groepN/bank/GN-*.md`). Alle kindteksten zijn Nederlands en staan er precies zoals in de bank; er is niets herschreven. Opnieuw maken (overschrijft deze map en de zip van vandaag):

```
node /workspace/tools/export_bank.js                  # alles, incl. G7 Claude-pilotbestanden
node /workspace/tools/export_bank.js --zonder-pilots  # zonder *-claude-pilot.md
```

## Bestanden

| Bestand | Inhoud |
|---|---|
| `vragenbank_g3.json` … `vragenbank_g8.json` | één groep: groep → domeinen → doelen → items |
| `vragenbank_alles.json` | alle groepen samen (`groepen[]`), met tellingen |
| `vragenbank_alles.csv` | platte lijst, één rij per item, hoofdvelden; meerdere hints/opties gescheiden door ` \| ` |
| `validatie.json` | tellingen, controles en de lijst met aandachtspunten (anomalieën) |
| `assets/svg-doelen/` | statische SVG-plaatjes per doel (G3-starters uit het prototype) |
| `assets/svg-items/` | SVG's die het prototype per item met JavaScript tekent, hier vooraf gerenderd |
| `referentie-js/` | referentiecode uit het prototype: `visuals.js` (tekeningen), `mc-shuffle.js` (husselen), `order-cards.js` (ordenen-kaartjes) |

Alle bestanden zijn UTF-8 (zonder BOM). Tekens als × : → € □ ë staan er letterlijk in.

## Tellingen

| Groep | Doelen | Items | Canoniek | Claude-live | Claude-pilot | Op het bord |
|---|---|---|---|---|---|---|
| G3 | 44 | 284 | 284 | 0 | 0 | 284 |
| G4 | 46 | 368 | 368 | 0 | 0 | 368 |
| G5 | 40 | 320 | 320 | 0 | 0 | 320 |
| G6 | 44 | 352 | 352 | 0 | 0 | 352 |
| G7 | 25 | 376 | 200 | 16 | 160 | 200 |
| G8 | 37 | 296 | 296 | 0 | 0 | 296 |

"Op het bord" = items die `build-bank.js` nu op het leerlijnbord zet. Elke itemtelling is gecontroleerd tegen een directe telling van de `## NNN ·`-koppen in de bankbestanden.

## Opbouw van de JSON

```
groep            3..8
telling          aantallen
domeinen[]       code (GET, VERH, MEET, MKU, VBN, DENK), naam
  doelen[]       één leerdoel (tegel op het bord)
    items[]            de oefeningen van dit doel (canonieke bank)
    claudeVarianten[]  alleen G7: parallelle Claude-sets, elk met eigen items[]
```

Domeinen: GET Getallen · VERH Verhoudingen · MEET Meten (G7: Meten & meetkunde) · MKU Meetkunde · VBN Verbanden · DENK Denken & handelen (alleen G7). Doelen staan per domein op fase (start → midden → eind) en daarna op ID.

### Velden van een doel

| Veld | Betekenis |
|---|---|
| `id` | doel-ID, bv. `G5-GET-M03` (G = groep, domein, K/V = start, M = midden, E = eind, nummer). G7 gebruikt `G7-GET-01` |
| `domein` | domeincode |
| `bordtitel` | titel zoals het bord hem toont (bank `Bordtitel:`, anders de bordpagina); `bordtitelBron` zegt waar hij vandaan komt |
| `korteNaam` | vakinhoudelijke korte naam uit de spine/leerlijn |
| `beschrijving` | omschrijving uit de kop van het bankbestand |
| `voorbeeld` | voorbeeldvraag voor het bord (bank `Bordvoorbeeld:` of BORDTITELS) |
| `fase` | `start` (instroom/onderhoud), `midden` (opbouw) of `eind` (beheersen) |
| `nieuw2026` | `true` = badge "nieuw 2026" (G3-VERH-E01, G3-VBN-E03, G7-DENK-01…05); `false` = geen badge |
| `label` | spinelabel: KLEUTER, VORIG, G5-nieuw, G5-verdieping … |
| `status` / `statusTekst` / `taalOk` | `Didactiek-af` of `concept`, de volledige statusregel, en of er "taal: ok" in staat |
| `notitie` | didactische notitie voor makers (geen kindtekst) |
| `meta` | overige kopregels (Bron, Prereq, Doel, KD-ref, Visual-needed, Bron-slug …) |
| `bronBestand` | het bankbestand |
| `inBank` / `opBord` | heeft een bankbestand / staat nu op het bord |
| `aantalItems` / `niveaus` | aantal items en verdeling basis/toepassen/kritisch |
| `visualAssets` | statische plaatjes voor dit doel (zie Visuals) of `null` |

### Velden van een item

| Veld | Banklabel | Betekenis |
|---|---|---|
| `id` | kop | item-ID = bestandsnaam + nummer, bv. `G3-GET-M01-004`; zelfde ID als op het bord. Claude-sets: `G7-GET-01-claude-003`, `G7-GET-01-claude-pilot-003` |
| `nr`, `doelId` | kop | volgnummer (`"001"`) en doel |
| `niveau` / `niveauKind` | kop | `basis` / `toepassen` / `kritisch`; kindlabel Opwarmen / Oefenen / Uitdaging |
| `type` | kop | itemtype, zie hieronder |
| `opgave` | Opgave | de vraag (kindtekst). `□` = invulvakje; een blok tussen ``` is een ASCII-schets van de tekening |
| `opgaveStappen` | Opgave | alleen `multi`: `{inleiding, stappen:[{stap, tekst}]}` |
| `opties` / `optiesTekst` | Opties | meerkeuze: `[{letter, tekst}]` in bankvolgorde, en de ruwe tekst |
| `antwoord` | Antwoord | het goede antwoord, letterlijk. Dit veld is leidend |
| `antwoordDetail` | Antwoord | automatisch afgeleid: `juisteOptie`/`juisteOptieTekst` (meerkeuze), `accept` (ook goed te rekenen invoer), `acceptToelichting` (feedbackzinnen bij een variant), `rubric` (nakijkregel voor uitleg), `stappen` (multi: per stap), `koppelingen` (verslepen: van → naar), `volgorde` (ordenen), `acceptPerStap` (deelsom-items, zoals `acceptSteps` in data.json) |
| `hint` | Hint | hint 1 (kindtekst, verklapt het antwoord niet) |
| `sterkereHint` | Sterkere hint | hint 2, sterker |
| `foutHints` / `foutHintsTekst` | Fout-hints | per fout antwoord de denkfout-uitleg: `[{stap, fout, uitleg}]`. `fout` = de sleutel (optieletter, fout getal, of bij verslepen/ordenen de foute koppeling); `uitleg` = kindtekst. Plus de ruwe tekst |
| `ouderzin` | Ouderzin | één zin voor de ouder: wat oefent het kind |
| `getallenruimte` | Getallenruimte | getalbereik (bv. `0–100`) |
| `context` | Context | hoeveel verhaal/context: `laag` of `midden` |
| `visual` | Visual | `{nodig, toelichting, asciiSchets, jsRender, svgBestanden}`; `nodig: null` = geen Visual-regel |
| `husselen` | Husselen | meerkeuze: `false` bij `Husselen: nee`, anders `true`; `null` bij andere types |
| `husselPlan` | – | wat `mc-shuffle.js` doet: `appHusselt`, `reden`, `vasteOpties` |
| `rekenmachine` | Rekenmachine | `true` = eenvoudige rekenmachine tonen (alleen bij `Rekenmachine: ja`) |
| `deelsomInvoer` | Invoer | `true` = kind typt een deelsom; ÷, : en / gelden als hetzelfde deelteken |
| `subfocus`, `ui` | Subfocus, UI | zeldzame extra's (subthema; UI-aanwijzing) |
| `bronVariant` | kop | alleen Claude-sets: oorspronkelijke variant-slug (`bron: …` in de kop) |
| `extraVelden` | – | onbekende labels (nu leeg) |
| `bron` | – | `{bestand, type}`; type = `canoniek`, `claude-live` of `claude-pilot` |
| `opBord` | – | `true` als dit item nu op het bord staat |

### Itemtypes (`type`)

| Type | Wat het kind doet |
|---|---|
| `kale` | kale som: korte vraag, typt een getal of woord |
| `invullen` | vult het vakje □ in een zin of som in (soms meer vakjes: per vakje nakijken) |
| `meerkeuze` | kiest één van (meestal) 4 opties; opties worden gehusseld, behalve bij Husselen: nee |
| `verslepen` | sleept kaartjes naar vakjes/labels (koppelen). Antwoord `X → Y · …`; afleider-kaartjes mogen overblijven |
| `ordenen` | zet kaartjes op volgorde. Antwoord `a → b → c` |
| `multi` | meerstaps (kritisch): 2–3 stappen, per stap nakijken; vaak stap 3 = ja/nee + korte uitleg (rubric) |
| `schattend` | schatten: kiest/typt een schatting ("ongeveer 400") |
| `verhaal` | alleen in G7-Claude-pilot: verhaaltjessom, typt het antwoord |

### Schrijfwijze in de tekstvelden

- In `antwoord` en `foutHintsTekst` is ` · ` de scheider tussen delen (structuur voor de app). In kindtekst staat tussen sommen het woord "en".
- In fout-hints is het stuk vóór `→` de sleutel (metadata, mag een optieletter zijn); ná de laatste `→` staat de kindtekst. Kindteksten noemen nooit een optieletter, want de opties worden gehusseld.
- `(accept: …)` = ook goed te rekenen invoer; `(rubric: …)` = nakijkregel voor een uitleg; "canoniek" + "correctiezin" = goed rekenen maar netjes verbeteren.
- `antwoordDetail` en `foutHints` zijn automatisch afgeleid. Bij twijfel gelden `antwoord` en `foutHintsTekst`.

## Bron van de items (G7 Claude-bestanden)

- **canoniek**: de gewone bank; staat in `items[]`. Gebruik dit voor de website.
- **claude-live** (`G7-GET-01-claude.md`, `G7-GET-03-claude.md`): parallelle Claude-set, in VOORTGANG G7 "live Claude-bestand" genoemd en meegenomen in de fixes van 30-09. Staat níét op het bord (build-bank toont voor hetzelfde doel de canonieke set). In `claudeVarianten[]`.
- **claude-pilot** (`*-claude-pilot.md`): parallelle concept-track ("geen merge zonder Overzicht"); niet op het bord en **niet** meegenomen in de deelteken-fix van 30-09 (sommige bevatten nog ÷). G7-VBN-01/02-pilot zijn concept. In `claudeVarianten[]`; weglaten kan met `--zonder-pilots`.
- De eerste 8 items van `GET-01/03-claude-pilot` zijn (bijna) dezelfde als `GET-01/03-claude`.
- Niet geëxporteerd: `G7-VBN.md` (overzicht, geen items), `*-claude-bijvulN.md` (verwijzingen; items staan al in de pilot), `*.bak-*`, `drafts/` en `_backup_compact/`.

## Visuals

- `Visual: ja` = er hoort een tekening bij, en die is een productie-eis vóór live. Het ASCII-blok in de opgave is de schets en de terugval, niet het eindplaatje. Er staan geen antwoorden en geen letters A–D in een plaatje (de opties worden gehusseld).
- `visual.jsRender`: bij 17 items tekent het prototype het plaatje met `referentie-js/visuals.js` (turven, grafieken, patronen, bouwplaten). De data staat in `jsRender`; de SVG's staan kant-en-klaar in `assets/svg-items/` (`visual.svgBestanden`). Bij turven vervangt de SVG het stuk ASCII uit `jsRender.marks[].ascii` in het genoemde veld.
- `assets/svg-doelen/` (9 bestanden): G3-starterplaatjes per doel; het doel verwijst ernaar via `visualAssets`. `hergebruikPrototype` verwijst naar een interactieve pagina in het prototype (niet gekopieerd).
- Alle andere items met `Visual: ja` hebben nog geen plaatje: de website moet dat tekenen of maken op basis van de opgave en de `toelichting`.

## Productieregels

Nagelopen in `rekenen-groepN/VOORTGANG.md` (✓ = staat daar; ⚠ = staat daar niet, bron erbij).

1. **Husselen** ✓ (G6, Productie-eisen en Optieletters): de app husselt meerkeuze-opties, behalve bij `Husselen: nee` (`husselen: false`; 14 items: opties hangen aan labels in de tekening). Goed/fout en fout-hints hangen aan de oorspronkelijke letter. Aanvulling uit `mc-shuffle.js` (niet in VOORTGANG): ook opties als "even groot"/"allebei", oplopende getallenrijen en opties met letterlabels blijven staan; zie `husselPlan`.
2. **Rekenmachine** ✓ (G8, Productie-eisen): een eenvoudige rekenmachine (4 bewerkingen en komma, rekent van links naar rechts, geen haakjes of geheugen), alleen bij `Rekenmachine: ja` (G8-GET-E05-001, G8-GET-E05-008, G8-GET-V02-008, G8-VERH-E05-008). Bij een multi-item geldt hij voor alle stappen. De opgave zegt dan ook "Je mag de rekenmachine gebruiken". Open besluit Dave: in de app bouwen of een echte rekenmachine toestaan.
3. **Dubbele punt, verhouding, schaal** ✓ (G8 Deelteken G4–G8 en Keuzes; G7-bankregels): `:` betekent "gedeeld door", met een spatie aan beide kanten (`12 : 4 = 3`); nooit ÷ in kindtekst. Een verhouding staat in woorden ("op elke 2 jongens 3 meisjes"); "1 op de 4" is een deel van een groep. Schaal staat altijd als `schaal 1 : n`, met de uitleg "1 cm op de kaart is n cm in het echt"; in een schaalitem is `:` nooit een deelteken ("gedeeld door" voluit). Blijven staan: kloktijden (`23:40`) en labels als "Stap 1:". G3 schrijft geen deelsommen. Typt het kind zelf een deelsom (`deelsomInvoer: true`), dan gelden ÷, : en / als goed.
4. **Mees-hintflow** ⚠ (niet in VOORTGANG; opgegeven door Dave, past bij "hint-first" en de Hint-knop in `leermees-prototype-v1/PROTOTYPE_STATUS.md`). Na een fout antwoord: `hint` → opnieuw proberen → `sterkereHint` → opnieuw proberen → de denkfout-uitleg (`foutHints`-regel waarvan `fout` past bij het gegeven antwoord; zonder passende sleutel een algemene zin) met het goede `antwoord` → door naar de volgende vraag. Daarnaast is er altijd een vrijwillige Hint-knop (toont eerst `hint`, daarna `sterkereHint`, nooit het antwoord). De bank heeft geen apart veld "denkfout-uitleg": dat zijn de fout-hints.
5. **Lettertype** ✓ (G8, Productie-eisen, Lettertype symmetrie): een schreefloos lettertype waarin S en Z echt puntsymmetrisch zijn en H, T, O en V echt lijnsymmetrisch (G8-MKU-V01-007/008, G8-MKU-E03-005/007). Ook (G6): letter A schreefloos, kleine l niet gelijk aan 1 ("1,5 l").
6. **Tekendoelen** ⚠ (niet in VOORTGANG; wel in de bank-notities van G6-VBN-E03 "'Tekenen' is in de app vertaald naar kiezen en slepen van lijnvormen (productie: eventueel later een tekenvak)" en G6-MKU-E02 "'ontwerpen' vertaald naar kiezen, aanvullen en slepen"): symmetrie, vlakvulling en een lijngrafiek tekenen zijn voorlopig kiezen of slepen; later is een tekenvak nodig.

Overige regels uit VOORTGANG:

7. **Plaatjes** (G4, G6, G8): `Visual: ja` = productie-eis vóór live; geen antwoordlabels en geen letters A–D in beeld; kleuren ook met patroon of letter (kleurenblind). Blocker: G8-MKU-E02-005 niet live zonder de vier bouwplaten.
8. **Invoer tolerant** (G6, G8): grote getallen met punt, spatie of zonder scheiding (46.000 · 46000 · 46 000); temperatuur met − of -; kloktijd 9.00 · 9 · 09.00 · 9 uur; woordantwoorden volgens `accept`; getalwoorden spelling-tolerant.
9. **Nakijken** (G6, G8): multi per stap; ja/nee automatisch, de uitleg via de `rubric` (kernwoorden), nooit blokkeren op de uitleg alleen; meerdere vakjes per vakje nakijken met een fout-hint per vakje; accept-varianten met een feedbackzin goed rekenen; doorwerkfout bij G8-GET-V02-008 stap 2.
10. **Verslepen** (G6): afleider-kaartjes mogen overblijven; fout-hints alleen op bestaande kaartjes, anders een algemene hint; veel kaartjes op mobiel in 2 rijen van 4 zonder scrollen.
11. **Typografie en notatie** (G6, G8): gemengde getallen getypografeerd of met vaste spatie (nooit afbreken tussen 1 en 1/3); breukkaartjes met echte breukstreep; verhoudingstabel als echte tabel; hele getallen van 4 cijfers zonder punt, vanaf 10.000 met punt; Nederlandse komma.
12. **Live en volgorde**: build-bank zet G6 en G8 alleen op het bord met `Didactiek-af` + `taal: ok`; G6-GET-M05/M06 vóór of samen met G6-GET-E04/E06; G8-MEET-V01 vóór G8-MEET-E01. G3-K-doelen zijn instroom-diagnostiek: 4 items (2 basis, 1 toepassen, 1 kritisch), geen mastery.

## Controle (deze run)

- Items per groep = directe telling van de koppen in de bank: ja, overal gelijk.
- Items zonder antwoord: 0. Parserfouten: 0. Elk veld is ook vergeleken met de parser van het bord (`build-bank.js`): geen verschillen.
- Aandachtspunten: 17 × let op · 4 × info. De volledige lijst staat in `validatie.json` (`anomalieen`); er is geen item weggelaten.
