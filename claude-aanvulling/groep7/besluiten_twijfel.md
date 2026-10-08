# Besluiten twijfelgevallen G7-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `data/twijfel.json` (303 items in 4 categorieën, build van 16.43 uur) en `twijfel_voor_didactiek.md` · Machineleesbaar: `besluiten_twijfel.json` (id → besluit/doel, met nieuwe opties en antwoorden per item)

Referenties:
- SLO-tussendoelen (`leerlijn/rekenen-groep7/tussendoelen.txt`; eind G7 vanaf r. 4223, eind G8 vanaf r. 4839):
  - kommagetallen eind G7: r. 4249 (lezen en schrijven 'tot en met drie cijfers achter de komma'), r. 4263 (vergelijken en ordenen, ook tot en met drie); eind G8 r. 5103 (positiewaarde tot en met duizendsten). Nergens vier decimalen.
  - oppervlakte eind G7: r. 4552 'kan de oppervlakte van driehoeken en rechthoekige veelhoeken berekenen'. Eind G8: r. 5441 (rechthoekige figuren, informeel) en r. 5452 (formule lengte × breedte). Geen driehoek in G8.
  - gemiddelde: eind G7 r. 4398 'kent de betekenis van het begrip gemiddelde, kan een gemiddelde uitrekenen'. Mediaan, modus en kans komen in de tussendoelen niet voor.
  - verhoudingstaal eind G7: r. 4495 ('zoveel op de zoveel', deel van een totaal, als breuk en als percentage; uitleggen of verhoudingen gelijk zijn), r. 4499 (percentage = 1 op 100), r. 4513 (1 : 4 ↔ ¼ deel ↔ 25%). Eind G8: r. 4868–4869 ('zes van de vierentwintig' … 1 op de 4, 1/4 deel, 25%).
- Kerndoelen rekenen-wiskunde 2025/2026 (`leerlijn/rekenen-groep7/bronnen/kerndoelen-rw.txt`, gelijk aan Stb. 2026, 198):
  - r. 393–394 'in het voortgezet onderwijs verder uitgebreid met vergelijkingen en kans'; r. 375–379 'in het voortgezet onderwijs gaat het om de samenhang tussen kansen en verhoudingen';
  - PO kerndoel 11A (r. 592–595): omtrek, oppervlakte en inhoud van 'rechthoekige figuren'; PO kerndoel 12A (r. 613): 'berekenen en interpreteren van een gemiddelde';
  - VO kerndoel 11A (r. 860): 'gemiddelde, modus en mediaan'; VO 11B (r. 882–884): 'kansen weergeven als breuk, verhouding, percentage'.
- `leerlijn/rekenen-groep8/SPINE_G8_v1.md` r. 223 ('Kansrekening formeel' buiten scope) en r. 227 ('Mediaan/modus en andere centrummaten … niet als G8-einddoel').
- `leerlijn/rekenen-groep7/TAXONOMIE_VERH_v0.md` r. 16 (kansrekening out of scope G7) · `TAXONOMIE_v0.md` r. 191 (G7 gemiddelde; mediaan/modus niet gevonden) en r. 295 · `TAXONOMIE_MEET_v0.md` r. 34 (G7-MEET-02 met driehoek).
- G7-bank: `exports/leermees-vragenbank-export/vragenbank_g7.json` + claude-pilot + `data/per_doel/` (gemapte items). Dubbelcontrole tegen alle drie.

Besluitwaarden in de json: `G7` (houden zoals het is, met de voorwaarden), `G8`, `aanpassen` (houden in G7 na een concrete wijziging, die per id in de json staat) en `schrappen`. Alle 303 ids zijn precies één keer gedekt (controle met script). Geen enkel item gaat naar G8.

---

## 1. `vier-decimalen` — 216 items (B4) · G7-GET-02

**Besluit:** **aanpassen (inkorten tot 3 decimalen) — 216 items** naar G7-GET-02. Schrappen 0, naar G8 0.
- INKORT-3DEC: 180 items, antwoord blijft gelijk.
- INKORT-3DEC-ANTWOORD-NIEUW: 36 items, antwoord verandert; de merge moet het antwoord en de fout-hints opnieuw zetten (staat per id in de json): 001 009 010 017 018 020 033 038 053 055 067 070 071 073 076 077 097 098 111 112 132 133 144 159 160 165 167 168 190 191 194 195 197 199 206 207.

**Reden:**
- SLO eind G7 r. 4249/4263: vergelijken en ordenen tot en met drie decimalen; G8 r. 5103 ook tot duizendsten. Vier decimalen past dus in geen groep, maar de som zelf (kommagetallen vergelijken) is kern-G7.
- Elk item heeft precies één getal met 4 decimalen, één met 3 en één met 2, met hetzelfde gehele deel. Inkorten van dat ene getal is genoeg.

**Regel (mechanisch, `besluiten_twijfel.json` past hem per id toe):**
1. Haal bij het 4-decimale getal a,bcde één cijfer achter de komma weg, zodat er 3 decimalen overblijven. Voorkeursvolgorde: het 2e cijfer (c, zoals 2,7202 → 2,702), dan het 3e (d), dan het 4e (e), dan het 1e (b).
2. Het nieuwe getal mag niet op 0 eindigen (geen 2,720).
3. Na het inkorten moeten de drie opties verschillen in waarde (geen dubbele optie, ook niet 2,72 naast 2,720).
4. Kies uit de geldige kandidaten eerst die waarbij de valkuil 'langer = groter' (kommagetal-als-geheel: de cijfers achter de komma als heel getal vergelijken) een fout antwoord geeft; dan die waarbij het antwoord gelijk blijft; dan de volgorde uit stap 1.

Uitkomst: weggehaald cijfer 2e decimaal 177 · 1e decimaal 19 · 3e decimaal 16 · 4e decimaal 4.

**Blijft het item zinvol? Ja, bij alle 216.**
- Antwoord uniek: ja, bij alle 216 (gecontroleerd op waarde).
- Geen dubbele opties en geen dubbels: 0 binnen de 216, 0 tegen de 228 gemapte GET-02-items, 0 tegen bank en pilot.
- Valkuil 'langer = groter' actief: **144** items (vóór inkorten ook 144; 108 bleven actief, 36 zijn er nieuw bij gekomen).
- **Valkuil weg bij 36 items:** 002 003 004 006 008 013 019 025 026 027 029 030 031 032 034 037 040 043 045 047 048 049 061 064 066 069 074 075 078 080 081 084 095 100 105 108. Met hoogstens 3 decimalen kan de valkuil hier niet meer: het goede antwoord is zelf het langste getal (bij 'grootst'), of geen fout getal is tegelijk korter en groter. Deze items breken niet; ze toetsen nog steeds tienden en honderdsten vergelijken (SLO r. 4263). Totaal zonder valkuil: 72 (36 hadden hem al niet).
- **Geen item breekt** door het inkorten. Er is dus geen schraplijst.
- Antwoordlengte na inkorten: 2 decimalen bij 72 items, 3 decimalen bij 144.
- Mooie bijvangst: 19 keer valt het tiendencijfer weg, dan ontstaan getallen als 0,025, 2,025, 5,079. Dat oefent de 0 op de plaats van de tienden (positiewaarde, r. 4257–4258).

**Voorbeelden:**
- 001 'grootst': 2,7202 · 2,72 · 2,103 → **2,702** · 2,72 · 2,103; antwoord wordt **2,72** (was 2,7202); valkuil actief (wie 702 > 72 denkt, kiest 2,702).
- 005 'grootst': 2,85 · 2,256 · 2,8025 → 2,85 · 2,256 · **2,825**; antwoord 2,85 blijft; valkuil actief.
- 009 'grootst': 2,506 · 2,6425 · 2,58 → 2,506 · **2,425** · 2,58; antwoord wordt **2,58** (de c- en d-kandidaat gaven geen valkuil).
- 110 'kleinst': 0,8475 · 0,606 · 0,88 → **0,875** · 0,606 · 0,88; antwoord 0,606 blijft; valkuil actief.
- 002 'grootst': 0,853 · 0,4802 · 0,48 → 0,853 · **0,402** · 0,48; antwoord 0,853 blijft; valkuil weg.

**Voorwaarden:**
- **Opgave-notatie:** 'Kies uit 2,702, 2,72 of 2,103.' mengt de decimale komma met de komma van de opsomming. Voorstel (staat als `nieuweOpgave` in de json): 'Welk getal is het grootst? Kies uit: 2,702 · 2,72 · 2,103.' Of als meerkeuze met drie knoppen (nu `claudeVorm: open`).
- **Fout-hints:** zet ze opnieuw per nieuwe fout (`nieuweFouten` in de json). Nu is de hint 'Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. **Welke is groter?**' ook gebruikt bij de 108 'kleinst'-items. Daar moet het 'Welke is kleiner?' zijn. Geef de denkfout 'kommagetal-als-geheel' alleen aan een fout die echt uit die valkuil komt (de rest: 'tienden niet vergeleken').
- Bron-doel B4 heet 'Kommagetallen bij geld', maar er is geen geld in de items. Niet erg, maar geen geldcontext toevoegen: geld heeft 2 decimalen.
- Geen plaatje nodig; een getallenlijn als hint mag.

---

## 2. `oppervlakte-driehoek` — 36 items (M21) · G7-MEET-02

**Besluit (split):**
- **G7 (houden) — 10 items** (DRIEHOEK-G7): 001 003 004 (vlag, cm) · 005 (veld) · 011 015 018 019 023 036 (dierentuin, kinderboerderij, bos).
- **Aanpassen, blijft G7-MEET-02 — 20 items** (DRIEHOEK-G7-FIX):
  - 19 met een vreemde context (zie Voorwaarden);
  - 002: fout-hint '31.5' → '31,5' (punt als decimaalteken).
- **Schrappen — 6 items** (DUBBEL-MATEN): dezelfde basis, hoogte en eenheid als een eerder item, alleen een ander verhaal (laagste nr blijft, `duplicaatVan` in de json):
  - 024 (12 m × 5 m) = 018 · 026 (4 × 12) = 023 · 027 en 035 (6 × 3) = 011 · 032 en 033 (6 × 10) = 007.
- Naar G8: 0.

**Reden:**
- SLO eind G7 r. 4552 noemt de oppervlakte van driehoeken letterlijk. G7-MEET-02 (TAXONOMIE_MEET r. 34; TAXONOMIE_v0 r. 295 'Oppervlakte driehoeken en rechthoekige veelhoeken') is het doel. In de G8-tussendoelen staat geen driehoek (r. 5441, 5452), dus G8 is geen optie.
- Spanning: het nieuwe PO-kerndoel 11A (kerndoelen 2026, r. 592–595) noemt alleen 'rechthoekige figuren'. De tussendoelen (en onze spine) gaan voor; met het plaatje 'driehoek = helft van de rechthoek eromheen' blijft het dicht bij rechthoekige figuren.
- Geen dubbel met bank of pilot: G7-MEET-02 heeft daar alleen rechthoeken en L-vormen. Deze items vullen dus een gat.
- Omgedraaide maten (bv. 016 basis 10, hoogte 12 en 028 basis 12, hoogte 10) houd ik: dat is een andere driehoek in het plaatje. 001 (12 cm × 5 cm) en 018 (12 m × 5 m) verschillen in eenheid en blijven ook.

**Voorwaarden (alle 30 die blijven):**
- **Visual: ja (productie-eis).** Nu staat `visual.nodig` op false. Teken de driehoek in de rechthoek eromheen, met basis en hoogte erbij (de hoogte als stippellijn, loodrecht op de basis). Kleur mag niet het enige kenmerk zijn: arcering of een label 'de helft'.
- Uitleg in de hint: 'basis × hoogte is de rechthoek eromheen; de driehoek is de helft daarvan'.
- Eenheid m² en cm² zijn eenheden, geen machten (mag volgens de README-notatie).
- **Contexten vervangen** (staat per id in `wijzigingen`): 'in de kantine' → 'op het schoolplein' · 'in de klas' → 'in de schooltuin' · 'in de kleedkamer' → 'bij het sportpark' · 'in de gymzaal' → 'in de speeltuin' · 'in het huis' → 'in de achtertuin' · 'in het museum' → 'in de museumtuin' · 'in het nest' → 'in het park' · 'in het moeras' → 'in het natuurgebied' · 'in de vallei' → 'in het weiland' · 'in het stadion' → 'naast het stadion' · 'in de schuur' → 'op het erf'. Een stuk grond binnen in een gebouw (of in een nest) is onzin.
- Fout-hints: '60 = de hele rechthoek' en '17 = plus in plaats van keer' zijn goed. De derde hint 'Delen door 2, niet optellen' (bij 62 = rechthoek + 2) is een zwakke afleider; mag blijven.

**Voorbeelden:** 001 (vlag 12 cm × 5 cm, G7) · 006 (kantine → schoolplein, aanpassen) · 024 (= 018, schrappen).

---

## 3. `mediaan` — 26 items (Claude G6) · voorstel G7-VBN-05

**Besluit (split):**
- **Schrappen — 21 items** (MEDIAAN-NIET-PO).
- **Aanpassen → G7-GET-04 (gemiddelde) — 5 items** (MEDIAAN-NAAR-GEMIDDELDE): 004, 013, 017, 019, 022. Hun getallen zijn samen deelbaar door 5, dus het gemiddelde is een heel getal.
- Naar G8: 0.

**Reden:**
- SLO noemt alleen het gemiddelde: eind G6 r. 3991 (betekenis), eind G7 r. 4398 (uitrekenen en uitleggen), eind G8 r. 5246. Mediaan en modus staan nergens in de tussendoelen; PO-kerndoel 12A (r. 613) noemt alleen 'een gemiddelde'. Mediaan, modus en gemiddelde samen staan pas in VO-kerndoel 11A (r. 860). De G8-spine sluit ze uit (r. 227).
- **G7-VBN-05 klopt niet als doel:** dat is 'Data vergelijken en checken' (oorzaak, legenda, schalen), geen centrummaten. Gemiddelde zit in G7-GET-04.
- Zelfde datasets zijn geen dubbel met bank of gemapte GET-04-items (425–430 hebben andere getallen).

**Nieuwe items (staan in de json als `nieuweOpgave` / `nieuwAntwoord` / `nieuweFoutHints`):**
| id | getallen | nieuw antwoord (gemiddeld) | oude antwoord (middelste) |
|---|---|---:|---:|
| 004 | 15, 17, 7, 8, 3 vissen (pinguïns) | 10 | 8 |
| 013 | 18, 13, 2, 13, 9 blaadjes (dino's) | 11 | 13 |
| 017 | 12, 9, 14, 3, 2 vissen (pinguïns) | 8 | 9 |
| 019 | 4, 11, 14, 5, 11 ballen ('trainers' → 'teams') | 9 | 11 |
| 022 | 17, 6, 17, 13, 17 stickers (kinderen) | 14 | 17 |

- Opgave in het somtype van GET-04: '5 pinguïns hebben 15, 17, 7, 8, 3 vissen. Hoeveel vissen hebben ze gemiddeld?'
- Fout-hints: het middelste getal → 'Dat is het middelste getal. Gemiddeld betekent eerlijk verdelen: tel alles op en deel door 5.'; het totaal → 'Dat is het totaal. Verdeel het nog eerlijk over de 5.' Het woord 'mediaan' niet gebruiken.

**Taal (geldt ook als Overzicht toch iets houdt):** 'trainers' (002, 005, 019) en 'shirts' (005) zijn Engels; 'dino's met botten/blaadjes' is een vreemde context.

---

## 4. `kans` — 25 items (Claude G7) · voorstel G7-VERH-04

**Besluit (split):**
- **Aanpassen → G7-VERH-04 — 13 items** (KANS-NAAR-DEEL): 001 002 003 004 007 008 009 010 011 012 013 024 025. Het woord 'kans' gaat eruit; de vraag wordt 'Welk deel van de … is …?' of 'Hoeveel procent van de … is …?'. Nieuwe opgave, opties en antwoord per id in de json.
- **Schrappen — 12 items** (KANS-VO): 005 (kans gelijk maken), 006 en 017 (zeker/onmogelijk), 014 en 015 (verwachte aantallen bij 60/100 worpen), 016 018 019 020 (munt en dobbelsteen: uitkomstruimte, geen totaal gegeven), 021 (twee munten), 022 (gokkersdenkfout), 023 (welke kleur 'meeste kans': gewoon tellen, onder G7-niveau).
- Naar G8: 0. Ook in G8 staat geen kans (SLO eind G8 niet; G8-spine r. 223 'Kansrekening formeel' buiten scope).

**Reden:**
- Kans is VO: kerndoelen r. 375–379 en 393–394, VO-kerndoel 11B r. 882–884. De G7-VERH-taxonomie sluit kansrekening uit (TAXONOMIE_VERH r. 16).
- Wat wel G7 is: 'verhoudingen benoemen en schrijven als zoveel op de zoveel, deel van een totaal, als breuk en als percentage … uitleggen waarom de ene verhouding wel of niet gelijk is aan de andere' (r. 4495) en '1 : 4 ↔ ¼ deel ↔ 25%' (r. 4513). De 13 items hebben een gegeven totaal (rad, bak, pot, zak, kaartjes), dus de rekenkern is deel-van-het-geheel. Dat is precies VERH-04.

**Niveau en het antwoord '2 op 8':**
- Niveau: G7 (VERH-04), zie hierboven.
- **Beide vormen goed rekenen.** '2 op de 8' is een juiste telling ('zes van de vierentwintig', r. 4868–4869) en gelijk aan '1 op de 4' (r. 4495: gelijke verhoudingen). Niet verplicht vereenvoudigen; vereenvoudigen is geen eis van VERH-04. In de json: `ookGoed` (003 → '1 op de 4'; 011 → '1 op de 3'; 024 → '1 op de 2'; 025 → '1 op de 2'; 009 → '2 op de 5').
- Meerkeuze-eis: er mag nooit een tweede optie staan die gelijk is aan het antwoord (dan zijn er twee goede). Gecontroleerd: bij de 13 items is dat nu zo.
- Notatie zoals de bank: '1 op de 4' (met 'de'), niet '1 op 4' (bank G7-VERH-04-003 '1 op de 5 = ___ %').

**Voorbeelden (nieuwe opgave):**
- 003: 'Een rad heeft 8 even grote vakjes. Twee vakjes zijn groen. Welk deel van de vakjes is groen?' · opties 2 op de 8 · 2 op de 6 · 6 op de 8 · antwoord 2 op de 8 (ook goed: 1 op de 4).
- 001: 'Bij een loterij wint 1 op de 4 lootjes een prijs. Hoeveel procent van de lootjes wint een prijs?' · 25%.
- 013: 'In zak A zijn 2 van de 4 knikkers rood. In zak B zijn 3 van de 9 knikkers rood. In welke zak is het deel rode knikkers het grootst?' · Zak A (vergelijken van verhoudingen, r. 4495).

**Voorwaarden:**
- **Visual: ja** bij de rad-items (002, 003): een rad met even grote vakjes. Kleur mag niet het enige kenmerk zijn: zet ook een patroon of letter (G = groen, R = rood) in de vakjes.
- 009: 'Je pakt in het donker één sok' gaat eruit (dat is de kansvraag).
- Breuknotatie (1/4) mag in VERH-04 als optie of als 'ook goed', want het doel koppelt breuk, procent en verhouding.
- Fout-hints herschrijven zonder 'kans', bv. bij '2 op de 6': 'Tel alle vakjes van het rad, ook de groene.'
- 001 lijkt op bank G7-VERH-04-008 stap 2 ('1 op de 4' als procent). Geen exacte dubbel (los item, andere context), dus houden.

---

## Samenvatting

| Categorie | Aantal | G7 (houden) | Aanpassen (G7) | G8 | Schrappen |
|---|---:|---:|---:|---:|---:|
| vier-decimalen (GET-02) | 216 | 0 | 216 (36 met nieuw antwoord) | 0 | 0 |
| oppervlakte-driehoek (MEET-02) | 36 | 10 | 20 (19 context, 1 notatie) | 0 | 6 (dubbele maten) |
| mediaan (→ GET-04) | 26 | 0 | 5 (naar gemiddelde) | 0 | 21 |
| kans (VERH-04) | 25 | 0 | 13 (naar deel van totaal) | 0 | 12 |
| **Totaal** | **303** | **10** | **254** | **0** | **39** |

Bijvangst (los van deze 303):
- De gemapte GET-04-gemiddelde-items (somtype 6, 425–430) hebben de fout-hint 'Dat is het middelste getal (de mediaan)'. 'Mediaan' is geen PO-woord: maak er 'het middelste getal' van.
- De hint 'Welke is groter?' bij 'kleinst'-items zit ook in de gemapte GET-02-items: alle 108 'kleinst'-items daar hebben hem (gecontroleerd). Graag meenemen in de hints-batch.

## Open vragen voor Dave/Overzicht
1. **Dubbele maten bij de driehoeken (6):** ik schrap ze, net als DUBBEL-VERHAAL in G6. Wil Overzicht meer oefening, dan kunnen ze blijven met een nieuw verhaal (`duplicaatVan` staat in de json).
2. **Mediaan:** akkoord met 5 items naar gemiddelde (GET-04) en 21 schrappen? Of alle 26 schrappen, of alle 26 met nieuwe getallen omzetten naar gemiddelde?
3. **Kans:** akkoord dat het woord 'kans' helemaal uit G7 gaat (13 items als 'deel van'), of mag 'kans' blijven als context bij een gegeven totaal? De 4 dobbelsteen/munt-items (016, 018–020) kunnen eventueel ook als deel-vraag ('Op hoeveel van de 6 vlakken …?'), maar dat voelt geforceerd.
4. **'1 op de n' goed rekenen:** kan de checker gelijkwaardige verhoudingen ('2 op de 8' = '1 op de 4', ook '1/4' en '25%') goed rekenen, of moet `ookGoed` als vaste lijst?
5. **Opgave-vorm B4:** 'Kies uit: 2,702 · 2,72 · 2,103' (open) of echte meerkeuze? De huidige komma-opsomming is verwarrend.
6. **Doel-ID's in `voorstelDoel`:** mediaan stond op G7-VBN-05 (data checken). Klopt de rest van de mapping naar VBN-05 in de merge wel?
