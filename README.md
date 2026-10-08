# Mees-vragenbank

De vragenbank van **LeerMees**: een gratis, rustig en didactisch rekenplatform voor groep 3 tot en met 8, zonder advertenties. Elke vraag helpt het kind stap voor stap: eerst een hint, dan een sterkere hint, en pas daarna een uitleg van de denkfout die bij het foute antwoord past.

Deze repo is de bron om verder te werken, voor mensen en voor AI-tools (ChatGPT, Claude en andere). Alle kindteksten zijn Nederlands.

Stand: 8 oktober 2026. G5 en G6: ronde 10 (gate en rechecks van Didactiek) is verwerkt; alle checks 0 FAIL, 0 WARN (zie [Stand per groep](#stand-per-groep)).

## Mappen

| Map | Inhoud |
|---|---|
| [`bank/groep3`](bank/groep3) … [`bank/groep8`](bank/groep8) | De **canonieke, goedgekeurde vragen**: één Markdown-bestand per leerdoel (`G5-GET-M03.md`), meestal 8 items. `README.md` = bankregels van die groep. `info/leerdoelen.md` = overzicht van leerdoelen, bordtitels en status. `info/VOORTGANG.md` = voortgang en productie-eisen. |
| [`claude-aanvulling/groep3`](claude-aanvulling) … `groep8` | De **samengevoegde items uit de Claude-vragenbank**, met hints en denkfout-uitleg (JSON). Per groep ook `somtypen/`, `hints/`, de besluiten (`besluiten_twijfel.*`) en `merge-fixlijst.md`. |
| [`export-chatgpt`](export-chatgpt) | De export van de canonieke bank als JSON en CSV (1 oktober 2026), met plaatjes en referentiecode. Uitleg van alle velden: [`export-chatgpt/README.md`](export-chatgpt/README.md). |
| [`scripts`](scripts) | Controle- en bouwscripts: de bankchecks, de gedeelde motor voor fout-hints (`fout_regels.py`), `export_bank.js`, `referentiematen.json` en `notatie_machten.md`. |

## Hoe een vraag eruitziet

### In de canonieke bank (`bank/groepN/*.md`)

```markdown
## 001 · basis · kale
- **Opgave:** Welk getal is groter: 45 of 54?
- **Antwoord:** 54
- **Hint:** Kijk eerst naar de tientallen. Welk getal begint met het grootste tiental?
- **Sterkere hint:** 45 begint met 4…, 54 begint met 5…. Vijftig-iets is meer dan veertig-iets.
- **Fout-hints:** 45 → Je keek misschien alleen naar de 5 aan het eind; de tientallen tellen eerst. · even groot → Ze zijn niet even groot; vergelijk 40-iets met 50-iets.
- **Ouderzin:** Je kind vergelijkt 45 en 54 (tientallen eerst).
```

De kop is `## nummer · niveau · type`. Niveau: `basis`, `toepassen` of `kritisch`. In **Fout-hints** staat vóór `→` het foute antwoord (de sleutel) en erna de denkfout-uitleg. Meerkeuze heeft ook `Opties:` (A–D). De optieletters staan nooit in de kindtekst, want de app husselt de opties.

### In de Claude-aanvulling (`claude-aanvulling/groepN/data/per_doel/*.json`)

Dezelfde basisvelden als de export, plus de fout-regels. Een ingekort voorbeeld (`G6-VERH-E01-claude-bank-004`):

```json
{
  "id": "G6-VERH-E01-claude-bank-004",
  "niveau": "basis",
  "type": "meerkeuze",
  "opgave": "1 fles is 2 L. Je zet dat in een tabel. Hoeveel liter is 5 van die flessen?",
  "antwoord": "10 L",
  "hint": "In een verhoudingstabel horen twee getallen bij elkaar. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet?",
  "sterkereHint": "Reken uit hoeveel keer zo groot het aantal in de vraag is als het aantal dat je al weet. Doe het andere getal ook zoveel keer. Zo blijft de verhouding gelijk.",
  "foutRegels": [
    {
      "regel": "fout = y1 + x2",
      "soort": "opgeteld",
      "tekst": "Heb je er iets bij opgeteld? Komt er bij het ene getal iets bij, dan komt er bij het andere getal niet vanzelf hetzelfde bij. …",
      "tekstSterker": null,
      "match": { "waarden": ["7", "7 L"] }
    }
  ],
  "algemeneFoutHint": "Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? …",
  "ouderzin": "Je kind rekent met een verhoudingstabel. …"
}
```

| Wat | Canonieke bank (`.md`) | Claude-aanvulling en export (JSON) |
|---|---|---|
| Opdracht | `Opgave` | `opgave` (bij meerkeuze ook `opties`) |
| Antwoord | `Antwoord` | `antwoord`; ook goed: `antwoordOokGoed`, `geldigeAntwoorden`, `antwoordDetail.accept` |
| Hint 1 | `Hint` | `hint` |
| Hint 2 | `Sterkere hint` | `sterkereHint` (G6: ook `sterkereHintMetPlaatje`, zie de app-eisen) |
| Denkfout-uitleg per fout antwoord | `Fout-hints` (sleutel → uitleg) | `foutRegels[]`: `match.waarden` = de foute antwoorden, **`tekst` = laag 1**, **`tekstSterker` = laag 2**. Per item uitgeschreven in `foutHints[]` (`fout`, `uitleg` = laag 1, `uitlegSterker` = laag 2). Is laag 2 leeg, dan geldt `sterkereHint`. |
| Geen passende sleutel | – | `algemeneFoutHint` |
| Ouderzin | `Ouderzin` | `ouderzin` |

De volgorde van `foutRegels` telt: de app neemt de eerste regel die past.

## Hint-volgorde in de app

Na een fout antwoord:

**hint 1 → opnieuw proberen → hint 2 → opnieuw proberen → denkfout-uitleg** (de fout-regel die bij het gegeven antwoord past, anders `algemeneFoutHint`), met het goede antwoord. Daarna gaat het kind door naar de volgende vraag.

Daarnaast is er altijd een vrijwillige Hint-knop. Die toont eerst hint 1 en dan hint 2, maar nooit het antwoord.

## Notatieregels

- **':' is het deelteken**, met een spatie aan beide kanten: `12 : 4 = 3`. Nooit `÷` in kindtekst. Typt het kind zelf een deelsom, dan gelden `÷`, `:` en `/` als goed.
- Een verhouding staat in woorden ("op elke 2 jongens 3 meisjes"). Schaal staat als `schaal 1 : n` (vanaf G7), met de uitleg "1 cm op de kaart is n cm in het echt".
- **Machten en maten** (zie [`scripts/notatie_machten.md`](scripts/notatie_machten.md)):
  - G3–G5: in woorden (hokjes, tegels, liter), geen ² of ³.
  - G6: cm², dm² en m² als symbool, met per somtype minstens één keer het woord erbij («cm² (vierkante centimeter)»). Nog geen ³.
  - G7–G8: ² en ³ (cm², m², cm³, m³). Bij een maat die nieuw is, staat het woord er één keer bij.
  - Nooit een macht van een getal (10³ wordt «10 × 10 × 10»).
- Getallen van 4 cijfers zonder punt (`8265`), vanaf 10.000 met punt (`12.500`). Nederlandse komma (`3,5`). Liter = `L`.
- **G8-build: volgorde van de patchrondes** (Oef-#493). `scripts/build_g8.py` doet altijd: 1 data schrijven → 2 `sync_hint_keys.py` → 3 alle `hints/patch_batch*.py` (op nummer, idempotent) → 4 opnieuw `sync_hint_keys.py` → 5 `apply_hints.py`. Een patch die van de data afhangt, ziet dus de nieuwe koppen en items. Elke fase staat met tijd in `logs/build_fase.json`; tijdens de build heeft een patch de omgevingsvariabele `G8_BUILD_FASE=na-sync-1` (buiten de build leeg), zodat een ronde daarop kan schakelen.
- **Kloktijden** (besluit Didactiek 8 okt): in lopende tekst '14.30 uur' of '3.00 uur', nooit ':' (ook niet samen met 'uur'). ':' alleen bij een item dat expliciet een digitale klok laat zien; dat item heeft `digitaleKlok: true`. Typ-invoer: de app rekent '14.30', '14:30' en '14.30 uur' als dezelfde tijd (normaliseren vóór het vergelijken, ook met de fout-sleutels); de instructie is «(Typ als 14.30.)». G8 is omgezet; G3–G5 staan op de branch `na-ronde-r13`.
- Ketensommen voluit: `7 × 4 = 28 en 28 + 12 = 40`, nooit `7 × 4 = 28 + 12 = 40`.
- Geen optieletters in hints of uitleg; noem de inhoud van de optie.

## Verschil tussen `bank/` en `claude-aanvulling/`

- **`bank/`** is de canonieke bank: per leerdoel 8 items, geschreven en goedgekeurd door Didactiek (`Status: Didactiek-af … taal: ok`). Dit zijn de items op het leerlijnbord.
- **`claude-aanvulling/`** bevat items uit Daves eigen Claude-vragenbank, per groep ingedeeld bij een LeerMees-leerdoel, op notatie gecontroleerd en per somtype voorzien van hints en denkfout-uitleg. **In de app komen deze items achter de 8 canonieke items van hetzelfde leerdoel.**
- De ruwe Claude-bron staat niet in deze repo, maar in **[Davesgit/leermees-vragenbank](https://github.com/Davesgit/leermees-vragenbank)** (licentie CC BY-SA 4.0). Elk Claude-item verwijst daar via `bron.claudeId` en `bron.commit` naar terug, en heeft een `licentie`-blok met de naamsvermelding.

Per groep in `claude-aanvulling/groepN/`:

| Bestand | Betekenis |
|---|---|
| `data/per_doel/GN-*.json` | De items van deze groep, per leerdoel. Handigste ingang. |
| `data/gemapt.json` | Dezelfde items in één bestand (de build en de checks lezen dit). |
| `data/aanvulling_uit_gX.json`, `terug_*.json`, `geparkeerd_*.json` | Items die tussen groepen verhuizen (te makkelijk of te moeilijk voor de groep waar ze vandaan kwamen). |
| `data/twijfel.json` | Items waar Didactiek nog over beslist (nu overal 0). |
| `somtypen/GN-*.md` | Per leerdoel de somtypen (sjablonen) met hun status, hints en voorbeelden. |
| `hints/batch*.json` | De hint-batches: per somtype hint 1, hint 2, de fout-regels en de ouderzin. |
| `besluiten_twijfel.*`, `twijfel_voor_didactiek.md` | De besluiten van Didactiek en Dave over twijfelgevallen. |
| `merge-fixlijst.md` | Alle reviewpunten en hun status. |
| `README.md` | Hoe de merge van deze groep is gebouwd, met regels en app-eisen. |

Wat nog hints nodig heeft: [`claude-aanvulling/hints_todo.md`](claude-aanvulling/hints_todo.md).

## Stand per groep

| Groep | Canonieke bank | Claude-aanvulling | Somtypen met hints | Stand |
|---|---|---|---|---|
| G3 | 44 leerdoelen · 284 items | 1.519 items · 26 leerdoelen | 83 van 83 | **Klaar** |
| G4 | 46 leerdoelen · 368 items | 1.855 items · 24 leerdoelen | 97 van 97 | **Goedgekeurd** (Didactiek: taal: ok, ook na build 15:46:18 met ronde 1c/1d GET-E05). Checks 0 FAIL · 1 WARN (LES250 bank-059, nieuwe check, voor Oefeningen). |
| G5 | 40 leerdoelen · 320 items | 4.845 items · 22 leerdoelen | 139 van 139 | **Ronde 11 verwerkt** (eindcheck r11 van Didactiek: #530/Oef-#426 bedragen, #531, #540, #543); na-ronde r12 (build 12:47:18): Oef-#427 gen-001 vervangen, motor zonder verschuiving; checks 0 FAIL, 0 WARN. Vaste somtypenummers (`bevroren/somtype_weergave_nr.json`). Open voor Oefeningen/Leerlijn: zie `merge-fixlijst.md`, blokken 'Ronde 10' en 'Ronde 10b' |
| G6 | 44 leerdoelen · 352 items | 4.302 items · 23 leerdoelen | 102 van 102 | **Ronde 11 verwerkt** (build 12:11:42; eindcheck r11 van Didactiek: #532 overdracht, #540, #543; checks 0 FAIL, 0 WARN, FIX6 0). Nieuw: hm (MEET-E01 #7–#10) en dl (MEET-E04 #5–#8). Open voor Oefeningen/Leerlijn: zie `merge-fixlijst.md`, blokken 'Ronde 10' en 'Ronde 10b' |
| G7 | 25 leerdoelen · 200 items (+ 16 in een Claude-set en 12 pilotbestanden) | 7.646 items · 17 leerdoelen | 155 van 155 | **Taal: ok, heel G7** (Didactiek 8 okt, build 15:41:07; geldt ook voor 15:49:23 en 15:52:17). Laatste build 16:20:58: hints batch 1 t/m 6, 155 van 155, checks 0 FAIL · 0 WARN; daarin V-#853/Z-#854 (GET-04 somtype 5: 427, 428, 861, 863, 864 nieuwe data met gelijke som, wacht op een korte nacheck van Didactiek). |
| G8 | 37 leerdoelen · 296 items | 1.458 items · 23 leerdoelen | 121 van 223 | **Hints batch 1–5** (build 16:45:31). Didactiek: batch 1–3 taal: ok (16:06:26 + sync 16:12; 0 verschil op 16:13:53); batch 4 taal: fix (16:25:38) → V-#870/V-#871/Z-#872/Z-#873 zitten erin, ronde 1b/1c van Oefeningen ook; batch 5 (MEET-E03/E05/E06) gesynct, nog niet bekeken. |

**G5 en G6 (ronde 9):** de builds zijn van 8 oktober, G5 10:57:42 en G6 10:58:34 (veld `gegenereerdOp`), met de motor `scripts/fout_regels.py` die hier staat (gelijk in G5–G8). Elk databestand heeft ook `hintsSyncOp` en `hintsBatches` (welke hint-batches erin zitten). Bord, app en rapporten werken op `id`, niet op `nr` of het somtypenummer: die kunnen verschuiven. G5 heeft 139 somtypen, want E07 #6 (TT × TT schatten, 10 items) is naar G6-GET-E06 gegaan. G6 heeft 94 somtypen, want MKU-E01 #3 en #4 zijn samengevoegd met #1 en GET-E06 heeft er één bij.

## App-eisen

Volledig in [`export-chatgpt/README.md`](export-chatgpt/README.md) (§ Productieregels) en [`claude-aanvulling/groep6/README.md`](claude-aanvulling/groep6/README.md) (§ Eisen voor de app). Kort:

1. **Husselen:** de app husselt meerkeuze-opties, behalve bij `Husselen: nee` (`husselen: false`). Goed/fout en fout-hints hangen aan de oorspronkelijke letter.
2. **Eerst goed, dan fout:** beoordeel eerst of het antwoord goed is, en kijk pas daarna naar de fout-sleutels. Het goede antwoord staat nooit in `match.waarden`. Neem de eerste fout-regel die past.
3. **Twee lagen per fout-hint:** `tekst` = laag 1, `tekstSterker` = laag 2.
4. **Invoer tolerant:** grote getallen met punt, spatie of zonder scheiding (46.000 · 46000 · 46 000); komma en punt als decimaalteken; '3,80' en '3,8' zijn dezelfde invoer, en zo ook '2' en '2,0' (een slotnul na de komma verandert de waarde niet; Z-#607). **Uitzondering (Z-#607, besluit Didactiek 8 okt):** vraagt de opgave een aantal cijfers achter de komma ('Rond af op één cijfer achter de komma', 'Rond af op twee cijfers achter de komma'), dan is een antwoord met minder cijfers achter de komma niet goed: bij 2,0 is '2' fout (eigen sleutel 'decimaal-nul weggelaten'); dit geldt in G5–G8; kloktijden 9.00 · 9 · 09.00 · 9 uur; woordantwoorden volgens `accept`.
5. **Eenheden:** de eenheid staat naast het invulvak, dus het getal alleen is goed. De app normaliseert 'm2', 'm^2' en 'vierkante meter' naar m² (zo ook cm³ enzovoort). Een andere eenheid is fout. De screenreader leest m² als "vierkante meter".
6. **Rekenmachine** alleen bij `Rekenmachine: ja` (eenvoudig: 4 bewerkingen en komma).
7. **Plaatjes:** `Visual: ja` is een eis vóór live. Geen antwoorden en geen letters A–D in beeld. Kleur nooit als enig kenmerk (ook patroon of letter). Items met `vereistTekening: true` gaan pas live als de app de getallenlijn echt tekent. De G6-hint `sterkereHintMetPlaatje` (torens met hoogtegetallen) gaat pas live als dat plaatje in de app staat; tot die tijd geldt `sterkereHint`.
8. **Getallenlijn en sorteren** (G6): de stip wordt beoordeeld met banden (veld `beoordeling`); bij sorteren in twee vakken telt de volgorde binnen een vak niet.
9. **'Bijna!'** alleen bij een antwoord vanaf 10 en precies één stap ernaast.
10. **Nakijken:** multi-items per stap; de uitleg via de `rubric`, maar nooit blokkeren op alleen de uitleg; meerdere vakjes per vakje nakijken.
11. **Typografie:** schreefloos lettertype waarin S en Z echt puntsymmetrisch zijn; kleine l niet gelijk aan 1; breuken met een echte breukstreep; gemengde getallen niet afbreken.
12. **Live en volgorde:** alleen items met `Didactiek-af` en `taal: ok` gaan op het bord.

## Controleren

Vanuit de root van de repo (Python 3, geen extra pakketten):

```
python3 scripts/check_optieletters.py      # optieletters en Husselen, G3–G8 (of één groep: … 5)
python3 scripts/check_dubbelepunt.py       # deelteken ':' en schaal
python3 scripts/check_cues.py              # geen vorm- of lengte-cue bij meerkeuze
python3 scripts/check_ketensom.py          # kettingsommen kloppen
python3 scripts/check_notatie.py 7         # grote getallen met punt
python3 scripts/check_bank_g6.py           # G6-bank (ook MC-spreiding)
python3 scripts/check_bank_g8.py           # G8-bank
python3 claude-aanvulling/groep6/check_hints.py           # hints per somtype
python3 claude-aanvulling/groep3/check_merge_notatie.py   # notatie van de Claude-items
```

De paden in deze scripts zijn aangepast aan de repo. Wat niet zomaar overal draait:

- `check_merge_notatie.py` van **G5 en G6** gebruikt ook de merge-buildscripts (`fixlijst_g5b.py`, `fixlijst_g6.py` enzovoort). Die staan niet in deze repo. G3, G4, G7 en G8 draaien wel.
- `scripts/export_bank.js` maakt `export-chatgpt/` opnieuw. Het script gebruikt nog vaste paden (`/workspace/...`) en heeft het LeerMees-prototype en de leerlijnbestanden nodig, die niet in deze repo staan.
- `scripts/fout_regels.py` is de gedeelde motor van G5–G8. G3 en G4 hebben een oudere versie, die niet in deze repo staat.
- `scripts/merge/maak_hints_todo.py` schrijft `claude-aanvulling/hints_todo.md` opnieuw.

## Werken met AI-tools

- Begin bij `bank/groepN/info/leerdoelen.md` voor het overzicht, en bij `bank/groepN/README.md` voor de bankregels.
- Voor de Claude-items: open `claude-aanvulling/groepN/data/per_doel/<leerdoel>.json`. Die bestanden zijn kleiner dan `gemapt.json` (die is tot 45 MB).
- Verander geen item-ID's en geen somtype-nummers: hints en reviews verwijzen ernaar.
- Houd je aan de notatieregels hierboven en draai de checks na een wijziging.
