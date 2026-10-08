# Bank rekenen groep 7 — bankregels

Dit bestand bevat alleen gedeelde bankregels (aangemaakt 2026-09-30); de voortgang staat in `../VOORTGANG.md`, sjablonen in `../SJABLONEN.md`.

## Optieletters en Husselen (bankregel G3–G7, 2026-09-30)
De app husselt de meerkeuze-opties. Daarom:
- **Geen optieletters in de kindtekst van Hint, Sterkere hint, Fout-hints en Ouderzin.** Niet 'Alleen B …', '(C)', 'Check A: …', 'Zelfde fout als B'. Noem de inhoud van de optie: 'Het bedrag €1203 …', 'De strook met 3 vakjes …', 'De rij die met 41 begint …'. Verklap het antwoord daarbij niet.
- **Sleutel = metadata.** Het stuk vóór '→' in Fout-hints ('B → …', 'Stap 2 → 18 → …', 'C → A → B → …' bij ordenen) is de sleutel voor de app en mag een letter zijn. Alleen de tekst ná de sleutel moet letter-vrij.
- **Uitzondering tekening-label.** Een letter die in de Opgave of tekening zelf een label is (strook A, bouwplaat B, pijltje C, beker A, kolom D, punt B op de plattegrond, het patroon 'A B C |' bij spiegelen) is inhoud en mag in hints staan. Schrijf er bij meerkeuze bij voorkeur het woord bij ('rechthoek A', niet los 'A').
- **Husselen: nee.** Een meerkeuze-item waarvan de opties vastzitten aan labels in de tekening (opties als 'strook A', 'plaatje B', 'Doos A', 'C', of een tekening/keuzes met regels 'A) …', 'B) …' die met de optieletters samenvallen, ook als de keuzes in de Opgave staan zonder Opties-veld; of een optie die zelf een label-letter noemt, zoals 'C) Nee, B heeft …' of 'A) Beker A …') krijgt een regel `- **Husselen:** nee` op hetzelfde niveau als `Visual:` (bij het item; de build maakt er `shuffle: false` van). `Husselen:` accepteert alleen de waarde `nee`; bij de andere items laat je de regel weg.
- **Controle:** `python3 /workspace/tools/check_optieletters.py` (alle banken G3–G7, of een groep: `… check_optieletters.py 5`). FAIL bij een optieletter in de kindtekst, bij een tekening-label-item zonder `Husselen: nee`, en bij een andere waarde dan `nee`. G6: ook onderdeel van `check_bank.py`.
- **Items met `Husselen: nee` in deze bank:** G7-VERH-05-005.

## Dubbele punt en schaal (G8-regel, besluit Overzicht 2026-09-30)
- ':' staat in de G7-bank alleen in 'schaal 1 : n' (met spaties en het woord *schaal* ervoor), altijd met de uitleg 'Dat betekent: 1 cm op de kaart/tekening is n cm in het echt.' Is de betekenis van de schaal zelf de vraag (VERH-01-004 · VERH-03-006 · VERH-03-007), dan staat de uitleg bij een andere schaal uit hetzelfde item, zodat de opgave het antwoord niet verklapt.
- Een deel van een groep staat als breuk of als '1 op de n' (= 1/n). Een verhouding staat in woorden ('3 delen siroop op 4 delen water', 'bij 3 pannenkoeken horen 2 eieren'). Nooit meer '1:4', 'deel:geheel', 'a:b' of 'schaalverhouding'.
- Geen gewone ':' direct na een schaalgetal ('schaal 1 : 50: …'). Delen schrijft G7 sinds 2026-09-30 12:50 met ':' ('a : b'), net als G4–G8 (zie 'Deelteken' hieronder); in een schaalitem staat delen voluit ('gedeeld door').
- Buiten scope: kloktijden in G7-MEET-04 ('23:40'); die blijven staan.
- Verwerkt 2026-09-30 12:20: patch `reviews/G7-dubbelepunt-rechttrekken-v1.patch` (Didactiek, 71 regels in 17 items: VERH-01 · VERH-03 · VERH-04 · DENK-02). Regellijst: `reviews/G7-dubbelepunt-rechttrekken-didactiek-v1.md`. Backup vooraf: `/tmp/g7_dp_backup_20260930_1219/`.
- Hercheck Didactiek 12:30: VERH-01-002 opgave herschreven (groepjes, sleutel 4 blijft) en VERH-01-006 fout-hint 3/4 erbij; DENK-02 · VERH-01 · VERH-03 · VERH-04 weer `Didactiek-af 2026-09-30. taal: ok.`
- **':' + getal (Didactiek vraag b):** geen gewone ':' direct gevolgd door een getal, %, € of som; wel ':' + woord, 'Stap n:' en 'schaal 1 : n'. Rechtgezet: DENK-03-003 · VERH-03-002 · VERH-05-008.
- **Controle:** `python3 /workspace/tools/check_dubbelepunt.py` (ALLES OK is de eis) en het rg-patroon (0 treffers, MEET-04 uitgesloten). **Sinds 2026-09-30 12:50 (':' = deelteken) geldt het nieuwe patroon**, want het oude `(?<!schaal 1) : ` markeert nu gewone delingen (39 treffers, allemaal 'a : b'): `rg -n --pcre2 -i --max-depth 1 '÷|\b\d+:\d|schaal 1 : [\d.]+:|deel ?: ?geheel|\ba:b\b|\b1:n\b|1:…|schaalverhouding|verhouding\w* \d+ ?: ?\d' -g 'G7-*-[0-9][0-9].md' -g '!G7-MEET-04.md' .`

## Deelteken ':' (besluit Overzicht 2026-09-30)
- ':' is het deelteken (zoals in Nederlandse methodes), kaal met een spatie aan beide kanten: '12 : 4 = 3'. Als operator (verhoudingstabel, pijl) ook ': 2', net als '× 2'. Nooit meer '÷' (op 2026-09-30 12:50 overal vervangen).
- Blijven zoals ze zijn: kloktijden (uu:mm), de labels 'Stap n:' · 'rij n:' · 'week n:' aan het begin van een regel of zin (midden in een zin niet: 'Na stap 1: 3 blokjes' → 'Na stap 1 zijn er 3 blokjes.'), '1 op de n' en 'schaal 1 : n'. Een verhouding staat in woorden ('3 tot 4', 'op elke 2 jongens 3 meisjes'), nooit als 'a : b' of 'a:b'.
- Invoer: typt het kind zelf een deelsom, dan accepteert de app '÷', ':' en '/' (in de bank: '(accept: 63 : 9 = 7 · 63 ÷ 9 = 7 · 63/9 = 7)', scheider '·', want '/' is hier een deelteken). Zo'n item krijgt de itemregel `- **Invoer:** ÷ : /` (na Getallenruimte/Context, zoals `- **Husselen:** nee`); build-bank maakt daar `divisionInput: true` van. Nu: G5-GET-M05-008 · G5-GET-E07-008 · G6-GET-M05-008. De checkers slaan die regel over.
- Controle: `python3 /workspace/tools/check_dubbelepunt.py` (G4–G8; verbiedt '÷', n:m zonder spaties, deel:geheel, ':' als verhouding en ':' direct na een schaalgetal). Hercheck-patroon (0 treffers, kloktijden uitgezonderd): `rg -n '÷|\b\d+:\d|deel ?: ?geheel|schaalverhouding|verhouding\w* \d+ ?: ?\d|schaal 1 : [\d.]+:' rekenen-groep{4,5,6,7,8}/bank/G*-*.md`

## Cues in meerkeuze (Didactiek S7 / Overzicht 2026-09-30)
- Het goede antwoord valt niet op door vorm of lengte. Begint één optie met 'Ja'/'Nee', dan alle opties, met een komma ('Ja, …' / 'Nee, …'), en de goede optie is niet de enige 'Ja' of de enige 'Nee'.
- Afleiders krijgen een korte, kloppende reden, of het goede antwoord wordt korter. Sleutels, A/B/C/D-verdeling en Husselen-vlaggen blijven gelijk; geen optieletters in hints.
- Controle: `python3 /workspace/tools/check_cues.py` (G3–G8): waarschuwt als de goede optie de enige met een Ja/Nee-vorm is, of duidelijk de langste (≥ 8 tekens én ≥ 25% langer dan de langste afleider), en vergelijkt per bank hoe vaak de goede optie de langste is met de kans bij toeval.

## Kettingsommen (Didactiek 2026-09-30 12:56)
- Geen keten die niet klopt, zoals '5 × 8 = 40 − 10 = 30'. Schrijf twee zinnen: '5 × 8 = 40. Dan 40 − 10 = 30.' Of twee regels. Geen '·' als scheider tussen sommen.
- Ook elke tussenstap moet van links naar rechts kloppen (Didactiek 13:12): niet '9 × 6 = 60 − 6 = 54' (9 × 6 is geen 60), maar '9 × 6 = 10 × 6 − 6 = 60 − 6 = 54'.
- In orde: gelijkheidsketens van gelijke waarden ('0,5 = 1/2 = 50%', '1 : 100 = 1/100 = 0,01 = 1%') en stappen die van links naar rechts kloppen ('9 + 7 = 9 + 1 + 6 = 10 + 6'). Bewust foute ketens (fout zoeken, foute afleiders) staan op `BEWUST_FOUT` in de checker.
- Controle: `python3 /workspace/tools/check_ketensom.py` (G3–G8).

## Notatie grote getallen (besluit Overzicht 2026-09-30 13:23)
- 4 cijfers zonder punt (1000, 4116, 3500); vanaf 10.000 met punt (10.000, 300.000, 1.005.000). Dat geldt voor alle kindtekst: Opgave, Opties, Antwoord, Hint, Sterkere hint, Fout-hints (ook de sleutel) en Ouderzin.
- Accept-lijsten en Invoer accepteren beide vormen: `300.000 (accept: 300.000 / 300000)`. Een invul-antwoord ≥ 10.000 krijgt altijd zo'n accept-lijst.
- Geen punt: kloktijden, jaartallen, postcodes, kommagetallen.
- Controle: `python3 /workspace/tools/check_notatie.py 7` (WARN; ook onderaan `check_optieletters.py`). Sleutels van fout-hints en accept-lijsten tellen niet mee.

## Live bestanden (check-regel 2026-09-30 13:23)
- De gedeelde checkers (check_cues, check_dubbelepunt, check_ketensom, check_notatie; check_optieletters kijkt naar alle *.md) nemen de bestanden zoals build-bank.js: *.md in deze map, geen README, geen `*-claude-pilot*`, alleen bestanden met items (`## NNN ·`). Zie `tools/bankfiles.py`. Zo tellen G7-GET-01-claude.md en G7-GET-03-claude.md mee; de bijvul-bestanden (zonder items) niet.
- Let op: de claude-bestanden hebben dezelfde Leerdoel-ID als G7-GET-01.md en G7-GET-03.md. build-bank.js schrijft `data[id]`, dus het hoofdbestand (komt later in de sortering) overschrijft het claude-bestand.
