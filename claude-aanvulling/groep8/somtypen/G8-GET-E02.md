# G8-GET-E02 — Schatten, bijstellen en je aanpak checken

Onze omschrijving: Schattend +/−/×÷ met correctie; procedures kritisch beoordelen · in onze bank: 8 items

Claude-vragen gemapt: **254** in **57** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Op welk cijfer eindigt # × #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Op welk cijfer eindigt # × #?” (koppeling: claudeId)
- Items: **53** · Claude-doelen: T3 (53) · regel: G8-T3-laatste-cijfer
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (36), een-ernaast (29), optellen-ipv-vermenigvuldigen (20), getal-overgenomen (15), tafelbuur (6)
- Verschillende Claude-fout-hints: 4 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-071` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Op welk cijfer eindigt 12 × 9?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G8-GET-E02-claude-bank-089` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Op welk cijfer eindigt 49 × 7?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Je hoeft niet de hele som uit te rekenen. Op welk cijfer de uitkomst eindigt, hangt alleen af van de eenheden: het cijfer helemaal rechts in elk getal.
- **Hint 2 (te schrijven):** Reken alleen de eenheden van de twee getallen keer elkaar. Op welk cijfer eindigt die kleine keersom? Daarop eindigt de hele som ook.
- **Ouderzin:** Je kind zoekt op welk cijfer een keersom eindigt, zonder de hele som uit te rekenen: alleen de eenheden tellen mee.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? Er staat een keerteken (×): reken de eenheden keer elkaar.  [Claude, taalfix]
  - `begincijfer` (Claudes sleutel: getal-overgenomen) → Dat is het cijfer waarmee de uitkomst begint. De vraag gaat over het cijfer waarop de uitkomst eindigt: helemaal rechts.  [Claude, taalfix]
  - `keersom ernaast` (Claudes sleutel: een-ernaast) → Dat hoort bij een keersom ernaast. Kijk nog eens welke eenheden er staan, en reken precies die keer elkaar.  [Claude, taalfix]
  - `tientallencijfer` (Claudes sleutel: tafelbuur) → Dat is het cijfer van de tientallen van de kleine keersom. De uitkomst eindigt op het cijfer helemaal rechts daarvan.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken alleen de eenheden keer elkaar, en kijk op welk cijfer dat eindigt.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoeveel is # + # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.

- Sleutel: nrOrigineel **51** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.” (koppeling: claudeId)
- Items: **30** · Claude-doelen: T3 (30) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-131` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 1100 + 8800 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 10.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9800 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 12.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-133` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 6350 + 6944 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 13.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 14.000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 20.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond eerst allebei de getallen af op duizendtallen, zoals de vraag zegt. Reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af. Tel daarna de twee afgeronde getallen op.
- **Ouderzin:** Je kind schat een plussom: eerst allebei de getallen afronden op duizendtallen, dan met de ronde getallen rekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond allebei de getallen af op duizendtallen. Is het cijfer van de honderdtallen vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `duizend te weinig` (fout = antwoord - 1000) → Dat is duizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te veel` (fout = antwoord + 2000) → Dat is tweeduizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te weinig` (fout = antwoord - 2000) → Dat is tweeduizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst allebei de getallen af op duizendtallen, en reken dan met de afgeronde getallen. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
- Status: hints klaar

## Somtype 3: Hoeveel is # × # [ding]? Rond # af op honderdtallen en # op tientallen, en reken dan uit.

- Sleutel: nrOrigineel **52** · somtypeOrigineel “Hoeveel is # × # [ding]? Rond # af op honderdtallen en # op tientallen, en reken dan uit.” (koppeling: claudeId)
- Items: **29** · Claude-doelen: T3 (29) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-191` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 693 × 71 ongeveer? Rond 693 af op honderdtallen en 71 op tientallen, en reken dan uit.
    - **Antwoord:** 49.000  (controle: ok)
    - **Fout-hints (Claude):** 49.203 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 48.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-185` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 273 × 32 ongeveer? Rond 273 af op honderdtallen en 32 op tientallen, en reken dan uit.
    - **Antwoord:** 9000  (controle: ok)
    - **Fout-hints (Claude):** 9600 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 12.000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond elk getal af zoals de vraag zegt, en reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Bij het getal dat op honderdtallen moet, kijk je naar de tientallen. Bij het getal dat op tientallen moet, kijk je naar de eenheden. Vijf of meer? Dan rond je naar boven af, anders naar beneden. Reken de cijfers zonder de nullen keer elkaar en zet alle nullen erachter.
- **Ouderzin:** Je kind schat een keersom: eerst afronden zoals de vraag zegt, dan de cijfers zonder nullen keer elkaar en de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond eerst af zoals de vraag zegt. Op honderdtallen: kijk naar de tientallen. Op tientallen: kijk naar de eenheden. Vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te groot: er staat een nul te veel achter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te klein: er mist een nul.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst af zoals de vraag zegt, en reken dan keer. Op honderdtallen: kijk naar de tientallen. Op tientallen: kijk naar de eenheden. Vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
- Status: hints klaar

## Somtype 4: Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **53** · somtypeOrigineel “Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **26** · Claude-doelen: T3 (26) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-199` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 20 × 81 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 1600  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 1400 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-207` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 399 × 60 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 24.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 23.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 22.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond elk getal af zoals de vraag zegt, en reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar de eenheden. Is dat vijf of meer? Dan rond je naar boven af op tientallen. Anders rond je naar beneden af. Reken de cijfers zonder de nullen keer elkaar, en zet daarna alle nullen van de afgeronde getallen erachter.
- **Ouderzin:** Je kind schat een keersom: eerst afronden zoals de vraag zegt, dan de cijfers zonder nullen keer elkaar en de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond allebei de getallen af op tientallen. Zijn de eenheden vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te groot: er staat een nul te veel achter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te klein: er mist een nul.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst af zoals de vraag zegt, en reken dan met de afgeronde getallen keer elkaar. Kijk bij elk getal naar de eenheden. Is dat vijf of meer? Dan rond je naar boven af op tientallen. Anders rond je naar beneden af.  [nieuw]
- Status: hints klaar

## Somtype 5: Kijk zonder uit te rekenen. Welk antwoord bij # × # kan kloppen?

- Sleutel: nrOrigineel **54** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen?” (koppeling: claudeId)
- Items: **19** · Claude-doelen: T3 (19) · regel: D8-KLOPPEN-MEERKEUZE-G8
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (11), laatste-cijfer (11), bovengrens (10), ondergrens (6)
- Verschillende Claude-fout-hints: 38 (meest: “Rond 179 naar beneden af. 100 × 8 is 800. De uitkomst kan dus niet kleiner zijn dan 800, en 432 is kleiner.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-255` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 179 × 8 kan kloppen?
    - **Opties:** A) 1432 · B) 432 · C) 187
    - **Antwoord:** 1432  (controle: n.v.t.)
    - **Fout-hints (Claude):** 432 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 187 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G8-GET-E02-claude-bank-245` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 339 × 3 kan kloppen?
    - **Opties:** A) 1019 · B) 342 · C) 1017
    - **Antwoord:** 1017  (controle: n.v.t.)
    - **Fout-hints (Claude):** 342 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Je hoeft niet precies te rekenen. Kijk eerst waarop het antwoord eindigt. Reken alleen de eenheden van de twee getallen keer elkaar. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.
- **Hint 2 (te schrijven):** Blijft er meer dan één antwoord over? Rond het grootste getal naar beneden af op honderdtallen en reken keer: het antwoord is groter. Rond het naar boven af en reken keer: groter kan het antwoord niet zijn.
- **Ouderzin:** Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door te kijken waarop het eindigt en tussen welke ronde getallen het ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus in plaats van keer` (fout = getal1 + getal2) → Heb je opgeteld? Er staat een keerteken (×): het antwoord is veel groter dan de twee getallen samen.  [nieuw]
  - `te groot` (Claudes sleutel: bovengrens) → Dat is te groot. Rond het grootste getal naar boven af op honderdtallen en reken keer: groter kan het antwoord niet zijn.  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Dat is te klein. Rond het grootste getal naar beneden af op honderdtallen en reken keer: kleiner kan het antwoord niet zijn.  [Claude, taalfix]
  - `veel te klein` (Claudes sleutel: orde-van-grootte) → Dat is te klein. Rond het grootste getal naar beneden af op honderdtallen en reken keer: kleiner kan het antwoord niet zijn.  [Claude, taalfix]
  - `eindcijfer` (Claudes sleutel: laatste-cijfer) → Kijk waarop het antwoord moet eindigen. Reken alleen de eenheden van de twee getallen keer elkaar. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst waarop het antwoord eindigt, en daarna tussen welke ronde getallen het ligt.  [nieuw]
- Status: hints klaar

## Somtype 6: Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit.

- Sleutel: nrOrigineel **55** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit.” (koppeling: claudeId)
- Items: **16** · Claude-doelen: T3 (16) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-163` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 194 + 813 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 1000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1007 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 1013 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-153` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 593 + 766 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 1400  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1359 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 1200 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond eerst allebei de getallen af op honderdtallen, zoals de vraag zegt. Reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af. Tel daarna de twee afgeronde getallen op.
- **Ouderzin:** Je kind schat een plussom: eerst allebei de getallen afronden op honderdtallen, dan met de ronde getallen rekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond allebei de getallen af op honderdtallen. Is het cijfer van de tientallen vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af.  [nieuw]
  - `honderd te weinig` (fout = antwoord - 100) → Dat is honderd te weinig. Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweehonderd te veel` (fout = antwoord + 200) → Dat is tweehonderd te veel. Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweehonderd te weinig` (fout = antwoord - 200) → Dat is tweehonderd te weinig. Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst allebei de getallen af op honderdtallen, en reken dan met de afgeronde getallen. Kijk bij elk getal naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af op honderdtallen. Anders rond je naar beneden af.  [nieuw]
- Status: hints klaar

## Somtype 7: Hoeveel is # − # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.

- Sleutel: nrOrigineel **56** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-227` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 8800 − 1100 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 8000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7700 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 7000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-228` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 6931 − 1940 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 5000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4991 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 7000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond eerst allebei de getallen af op duizendtallen, zoals de vraag zegt. Reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af. Haal daarna het kleinere afgeronde getal van het grotere af.
- **Ouderzin:** Je kind schat een minsom: eerst allebei de getallen afronden op duizendtallen, dan met de ronde getallen rekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond allebei de getallen af op duizendtallen. Is het cijfer van de honderdtallen vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `duizend te weinig` (fout = antwoord - 1000) → Dat is duizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te veel` (fout = antwoord + 2000) → Dat is tweeduizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te weinig` (fout = antwoord - 2000) → Dat is tweeduizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst allebei de getallen af op duizendtallen, en reken dan met de afgeronde getallen. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
- Status: hints klaar

## Somtype 8: In [plek] liggen # [ding] en er komen # bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding] en er komen # bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): afronden-verkeerde-kant (16), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is precies. Hier vragen we de schatting met ronde getallen.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-023` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Op het strand liggen 2640 schelpen en er komen 1536 bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.
    - **Antwoord:** 5000  (controle: ok)
    - **Fout-hints (Claude):** 4176 → Dat is precies. Hier vragen we de schatting met ronde getallen. · 6000 → Kijk per getal naar de honderdtallen: onder de 500 rond je naar beneden af. · 4000 → Kijk per getal naar de honderdtallen: vanaf 500 rond je naar boven af.
    - **Uitleg (Claude):** 2640 is ongeveer 3000, 1536 ongeveer 2000. Samen 5000. Precies is het 4176.
  - `G8-GET-E02-claude-bank-024` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Op de kinderboerderij liggen 2839 noten en er komen 2672 bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 5511 → Dat is precies. Hier vragen we de schatting met ronde getallen. · 7000 → Kijk per getal naar de honderdtallen: onder de 500 rond je naar beneden af. · 5000 → Kijk per getal naar de honderdtallen: vanaf 500 rond je naar boven af.
    - **Uitleg (Claude):** 2839 is ongeveer 3000, 2672 ongeveer 3000. Samen 6000. Precies is het 5511.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond eerst allebei de getallen af op duizendtallen, zoals de vraag zegt. Reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af. Tel daarna de twee afgeronde getallen op.
- **Ouderzin:** Je kind schat een totaal: eerst allebei de getallen afronden op duizendtallen, dan optellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond allebei de getallen af op duizendtallen. Is het cijfer van de honderdtallen vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `duizend te weinig` (fout = antwoord - 1000) → Dat is duizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te veel` (fout = antwoord + 2000) → Dat is tweeduizend te veel. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `tweeduizend te weinig` (fout = antwoord - 2000) → Dat is tweeduizend te weinig. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst allebei de getallen af op duizendtallen, en reken dan met de afgeronde getallen. Kijk bij elk getal naar het cijfer van de honderdtallen. Is dat vijf of meer? Dan rond je naar boven af op duizendtallen. Anders rond je naar beneden af.  [nieuw]
- Status: hints klaar

## Somtype 9: Kijk zonder uit te rekenen. Welk antwoord bij # + # kan kloppen?

- Sleutel: nrOrigineel **57** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-MEERKEUZE-G8
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): laatste-cijfer (7), orde-van-grootte (5), bovengrens (4)
- Verschillende Claude-fout-hints: 16 (meest: “Rond allebei naar boven af. 400 + 800 is 1200. De uitkomst kan dus niet groter zijn dan 1200, en 2069 is groter.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-233` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 360 + 709 kan kloppen?
    - **Opties:** A) 2069 · B) 1069 · C) 1071
    - **Antwoord:** 1069  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2069 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-229` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 737 + 776 kan kloppen?
    - **Opties:** A) 1513 · B) 2513 · C) 1511
    - **Antwoord:** 1513  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2513 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Je hoeft niet precies te rekenen. Kijk eerst waarop het antwoord eindigt. Tel alleen de eenheden van de twee getallen op. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.
- **Hint 2 (te schrijven):** Blijft er meer dan één antwoord over? Rond allebei de getallen naar beneden af op honderdtallen en tel op: het antwoord is groter. Rond allebei naar boven af en tel op: groter kan het antwoord niet zijn.
- **Ouderzin:** Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door te kijken waarop het eindigt en tussen welke ronde getallen het ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min in plaats van plus` (fout = getal1 - getal2 of getal2 - getal1) → Heb je min gedaan? Er staat een plus: het antwoord is groter dan allebei de getallen.  [nieuw]
  - `te groot` (Claudes sleutel: bovengrens) → Dat is te groot. Rond allebei de getallen naar boven af op honderdtallen en tel op: groter kan het antwoord niet zijn.  [Claude, taalfix]
  - `veel te klein` (Claudes sleutel: orde-van-grootte) → Dat is te klein. Rond allebei de getallen naar beneden af op honderdtallen en tel op: kleiner kan het antwoord niet zijn.  [Claude, taalfix]
  - `eindcijfer` (Claudes sleutel: laatste-cijfer) → Kijk waarop het antwoord moet eindigen. Tel alleen de eenheden van de twee getallen op. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst waarop het antwoord eindigt, en daarna tussen welke ronde getallen het ligt.  [nieuw]
- Status: hints klaar

## Somtype 10: Ongeveer hoeveel is # × #? Rond # af op honderdtallen en # op tientallen, en reken dan uit.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Ongeveer hoeveel is # × #? Rond # af op honderdtallen en # op tientallen, en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (16), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 9 (meest: “Een nul te veel. Tel de nullen van beide ronde getallen.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-054` (Claude T3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Ongeveer hoeveel is 483 × 15? Rond 483 af op honderdtallen en 15 op tientallen, en reken dan uit.
    - **Antwoord:** 10.000  (controle: ok)
    - **Fout-hints (Claude):** 1000 → Tel de nullen. 500 en 20 hebben er samen 3. · 100.000 → Een nul te veel. Tel de nullen van beide ronde getallen. · 7245 → Dat is precies uitgerekend. Hier vragen we een schatting met de ronde getallen.
    - **Uitleg (Claude):** 483 is ongeveer 500, 15 is ongeveer 20. 500 × 20 = 10.000. Het echte antwoord (7245) ligt daar dichtbij.
  - `G8-GET-E02-claude-bank-056` (Claude T3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Ongeveer hoeveel is 138 × 12? Rond 138 af op honderdtallen en 12 op tientallen, en reken dan uit.
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 100 → Tel de nullen. 100 en 10 hebben er samen 3. · 10.000 → Een nul te veel. Tel de nullen van beide ronde getallen. · 1656 → Dat is precies uitgerekend. Hier vragen we een schatting met de ronde getallen.
    - **Uitleg (Claude):** 138 is ongeveer 100, 12 is ongeveer 10. 100 × 10 = 1000. Het echte antwoord (1656) ligt daar dichtbij.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond elk getal af zoals de vraag zegt, en reken daarna met de afgeronde getallen.
- **Hint 2 (te schrijven):** Bij het getal dat op honderdtallen moet, kijk je naar de tientallen. Bij het getal dat op tientallen moet, kijk je naar de eenheden. Vijf of meer? Dan rond je naar boven af, anders naar beneden. Reken de cijfers zonder de nullen keer elkaar en zet alle nullen erachter.
- **Ouderzin:** Je kind schat een keersom: eerst afronden zoals de vraag zegt, dan de cijfers zonder nullen keer elkaar en de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond eerst af zoals de vraag zegt. Op honderdtallen: kijk naar de tientallen. Op tientallen: kijk naar de eenheden. Vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te groot: er staat een nul te veel achter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te klein: er mist een nul.  [nieuw]
  - `andere fout` (andere fout) → Rond eerst af zoals de vraag zegt, en reken dan keer. Op honderdtallen: kijk naar de tientallen. Op tientallen: kijk naar de eenheden. Vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
- Status: hints klaar

## Somtype 11: # [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.” (koppeling: claudeId)
- Items: **3** · Claude-doelen: T3 (3) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (3), nul-fout-tientallen (3), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 7 (meest: “Precies uitgerekend. Hier vragen we de schatting met het ronde getal.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-002` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 5 dozen met elk 497 knikkers. Schat hoeveel dat ongeveer is: rond 497 af op honderdtallen en reken dan uit.
    - **Antwoord:** 2500  (controle: ok)
    - **Fout-hints (Claude):** 2485 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 250 → 500 × 5: tel de nullen goed. · 505 → 5 dozen van elk ongeveer 500: dat is een keersom.
    - **Uitleg (Claude):** 497 is bijna 500. 500 × 5 = 2500. Precies is het 2485, dus de schatting klopt goed.
  - `G8-GET-E02-claude-bank-004` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 5 dozen met elk 297 stickers. Schat hoeveel dat ongeveer is: rond 297 af op honderdtallen en reken dan uit.
    - **Antwoord:** 1500  (controle: ok)
    - **Fout-hints (Claude):** 1485 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 150 → 300 × 5: tel de nullen goed. · 305 → 5 dozen van elk ongeveer 300: dat is een keersom.
    - **Uitleg (Claude):** 297 is bijna 300. 300 × 5 = 1500. Precies is het 1485, dus de schatting klopt goed.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen met ronde getallen. Rond het getal af op honderdtallen, zoals de vraag zegt, en reken dan.
- **Hint 2 (te schrijven):** Rond het getal af op honderdtallen: kijk naar de tientallen. Vijf of meer? Dan naar boven, anders naar beneden. Er staat 'met elk': reken het aantal keer het afgeronde getal. Reken zonder de nullen en zet de nullen van het afgeronde getal erachter.
- **Ouderzin:** Je kind schat een keersom met een verhaal: eerst één getal afronden op honderdtallen, dan keer het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Je hebt precies gerekend, maar de vraag wil een schatting. Rond het getal af op honderdtallen: kijk naar de tientallen. Vijf of meer? Dan naar boven, anders naar beneden.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te groot: er staat een nul te veel achter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te klein: er mist een nul.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? Er staat 'met elk': dan reken je keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond eerst af zoals de vraag zegt, en reken dan met de afgeronde getallen keer elkaar. Kijk bij het getal dat je op honderdtallen afrondt naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af, anders naar beneden.  [nieuw]
- Status: hints klaar

## Somtype 12: 's Ochtends is het # graden en 's middags # graden. Hoe reken je uit hoeveel graden het warmer is geworden?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “'s Ochtends is het # graden en 's middags # graden. Hoe reken je uit hoeveel graden het warmer is geworden?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een verschil is hoeveel het gestegen is. Wordt de uitkomst dan groter of juist kleiner dan 11?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-005` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** 's Ochtends is het 3 graden en 's middags 11 graden. Hoe reken je uit hoeveel graden het warmer is geworden?
    - **Opties:** A) Neem het getal 11 over als verschil · B) Trek 3 van 11 af · C) Tel 3 en 11 bij elkaar op
    - **Antwoord:** Trek 3 van 11 af  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 3 en 11 bij elkaar op → Een verschil is hoeveel het gestegen is. Wordt de uitkomst dan groter of juist kleiner dan 11? · Neem het getal 11 over als verschil → De ochtendtemperatuur was niet 0 graden. Die moet je meenemen als je het verschil uitrekent.
    - **Uitleg (Claude):** Het verschil vind je door de laagste temperatuur van de hoogste af te trekken. 11 min 3 is 8. De temperatuur is dus 8 graden gestegen.

- **Hint 1 (te schrijven):** Hoeveel graden warmer: de vraag gaat over het verschil tussen de twee temperaturen.
- **Hint 2 (te schrijven):** Tel van de temperatuur van 's ochtends door tot die van 's middags: hoeveel graden is dat? Reken dan elke aanpak uit. Welke geeft precies dat getal?
- **Ouderzin:** Je kind kiest hoe je een verschil uitrekent: hoeveel graden is het warmer geworden?
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal overgenomen` (Neem het getal 11 over als verschil) → Dat is de temperatuur van 's middags. Hoeveel graden is dat meer dan 's ochtends?  [nieuw]
  - `opgeteld` (Tel 3 en 11 bij elkaar op) → Bij elkaar optellen geeft geen verschil. Hoeveel graden is het 's middags meer dan 's ochtends?  [nieuw]
  - `andere fout` (andere fout) → Je zoekt het verschil tussen de twee temperaturen.  [nieuw]
- Status: hints klaar

## Somtype 13: Bas koopt # [ding] sap van €#. Hij krijgt €# als antwoord. Wat laat zien dat dit niet klopt?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Bas koopt # [ding] sap van €#. Hij krijgt €# als antwoord. Wat laat zien dat dit niet klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (2 cijfers achter de komma) met € · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Schat eerst met een rond bedrag: hoeveel is 6 keer 2 euro ongeveer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-006` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Bas koopt 6 pakken sap van €1,99. Hij krijgt €119,40 als antwoord. Wat laat zien dat dit niet klopt?
    - **Opties:** A) Het klopt, want 6 × 1,99 is bijna 120 · B) 6 pakken kosten ongeveer €12 · C) Het antwoord moet ongeveer €1200 zijn
    - **Antwoord:** 6 pakken kosten ongeveer €12  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het antwoord moet ongeveer €1200 zijn → Schat eerst met een rond bedrag: hoeveel is 6 keer 2 euro ongeveer? · Het klopt, want 6 × 1,99 is bijna 120 → Kijk goed waar de komma staat in €1,99. Eén pak kost nog geen 2 euro.
    - **Uitleg (Claude):** €1,99 is bijna €2. Zes keer 2 euro is ongeveer 12 euro. Een uitkomst van meer dan 100 euro kan dus niet kloppen.

- **Hint 1 (te schrijven):** Schat het antwoord met ronde getallen. Dan zie je snel of het antwoord van Bas kan kloppen.
- **Hint 2 (te schrijven):** Rond de prijs af op hele euro's. Doe dat keer het aantal. Ligt het antwoord van Bas daar dichtbij?
- **Ouderzin:** Je kind controleert een antwoord met een schatting: ronde prijs keer het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma vergeten` (Het klopt, want 6 × 1,99 is bijna 120) → Kijk naar de komma in de prijs. Rond de prijs af op hele euro's en doe dat keer het aantal: kom je dan ook boven de honderd euro?  [nieuw]
  - `tien keer te groot` (Het antwoord moet ongeveer €1200 zijn) → Dat is nog veel meer dan het antwoord van Bas. Rond de prijs af op hele euro's en doe dat keer het aantal: hoeveel euro is dat ongeveer?  [nieuw]
  - `andere fout` (andere fout) → Rond de prijs af op hele euro's en doe dat keer het aantal.  [nieuw]
- Status: hints klaar

## Somtype 14: Bij een spel krijg je # [ding] voor elk doelpunt. Voor elke misser gaat er # [ding] af. Hoe reken je de score uit?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Bij een spel krijg je # [ding] voor elk doelpunt. Voor elke misser gaat er # [ding] af. Hoe reken je de score uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Elk doelpunt levert 3 punten op. Hoe reken je hetzelfde aantal punten per keer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-007` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Bij een spel krijg je 3 punten voor elk doelpunt. Voor elke misser gaat er 1 punt af. Hoe reken je de score uit?
    - **Opties:** A) Doelpunten plus 3, dan het aantal missers eraf. · B) Doelpunten maal 3, dan het aantal missers erbij. · C) Doelpunten maal 3, dan het aantal missers eraf.
    - **Antwoord:** Doelpunten maal 3, dan het aantal missers eraf.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Doelpunten plus 3, dan het aantal missers eraf. → Elk doelpunt levert 3 punten op. Hoe reken je hetzelfde aantal punten per keer? · Doelpunten maal 3, dan het aantal missers erbij. → Een misser is niet goed voor je score. Wordt het totaal dan groter of kleiner?
    - **Uitleg (Claude):** Per doelpunt krijg je 3 punten, dus vermenigvuldig je het aantal doelpunten met 3. Elke misser kost 1 punt. Die missers haal je van het totaal af.

- **Hint 1 (te schrijven):** Elk doelpunt levert evenveel op. Elke misser kost iets.
- **Hint 2 (te schrijven):** Bedenk een voorbeeld: vier doelpunten en twee missers. Reken de score uit. Reken daarna elke aanpak uit met hetzelfde voorbeeld. Welke geeft dezelfde score?
- **Ouderzin:** Je kind kiest hoe je een score uitrekent: doelpunten keer wat ze opleveren, dan de missers eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus in plaats van keer` (Doelpunten plus 3, dan het aantal missers eraf.) → Elk doelpunt levert evenveel op. Heb je dat voor elk doelpunt meegeteld, of maar één keer?  [nieuw]
  - `missers erbij` (Doelpunten maal 3, dan het aantal missers erbij.) → Een misser kost iets. Komt dat bij de score of gaat het eraf?  [nieuw]
  - `andere fout` (andere fout) → Reken eerst uit wat alle doelpunten samen opleveren. Wat gebeurt er dan met de missers?  [nieuw]
- Status: hints klaar

## Somtype 15: Bram heeft # [ding] met # [ding]. Hij rekent uit dat er # [ding] zijn. Wat laat zien dat dit niet kan?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Bram heeft # [ding] met # [ding]. Hij rekent uit dat er # [ding] zijn. Wat laat zien dat dit niet kan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Lees nog eens: er zijn 12 zakjes met elk 15 knikkers. Wat doe je dan met die getallen?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-008` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Bram heeft 12 zakjes met 15 knikkers. Hij rekent uit dat er 27 knikkers zijn. Wat laat zien dat dit niet kan?
    - **Opties:** A) Eén zakje heeft al 15, dus 12 zakjes zijn veel meer · B) Niets, 12 en 15 samen is inderdaad 27 · C) Hij had 12 : 15 moeten doen
    - **Antwoord:** Eén zakje heeft al 15, dus 12 zakjes zijn veel meer  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 12 en 15 samen is inderdaad 27 → Lees nog eens: er zijn 12 zakjes met elk 15 knikkers. Wat doe je dan met die getallen? · Hij had 12 : 15 moeten doen → Delen maakt het aantal juist kleiner. Bij groepen van evenveel spullen kies je iets anders.
    - **Uitleg (Claude):** Bij 12 groepen van 15 hoort een vermenigvuldiging. Het antwoord moet dus veel groter zijn dan 15. Een snelle schatting laat zien dat 27 onmogelijk is.

- **Hint 1 (te schrijven):** Hoeveel zitten er in één groep? En hoeveel van die groepen heeft Bram?
- **Hint 2 (te schrijven):** Doe het aantal groepen keer het aantal in één groep: dat is het totaal. Is dat veel meer dan het antwoord van Bram?
- **Ouderzin:** Je kind controleert of een antwoord kan: heeft één groep er al zoveel, dan hebben alle groepen samen er veel meer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Niets, 12 en 15 samen is inderdaad 27) → Elke groep heeft er evenveel. Is het totaal dan het aantal groepen plus het aantal in één groep?  [nieuw]
  - `gedeeld` (Hij had 12 : 15 moeten doen) → Met meer groepen wordt het totaal groter. Past delen daarbij?  [nieuw]
  - `andere fout` (andere fout) → Hoeveel zitten er in één groep, en hoeveel groepen zijn er? Wat betekent dat voor het totaal?  [nieuw]
- Status: hints klaar

## Somtype 16: De trein vertrekt om #.# uur en komt aan om #.# uur. Hoe reken je handig uit hoe lang de reis duurt?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “De trein vertrekt om #:# en komt aan om #:#. Hoe reken je handig uit hoe lang de reis duurt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een uur heeft 60 minuten, niet 100. Werk in stappen naar een heel uur toe.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-009` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** De trein vertrekt om 14.35 uur en komt aan om 16.10 uur. Hoe reken je handig uit hoe lang de reis duurt?
    - **Opties:** A) Reken eerst tot 15.00 uur, dan verder tot 16.10 uur. · B) Trek 35 van 10 af en tel de uren erbij. · C) Tel de twee tijden bij elkaar op.
    - **Antwoord:** Reken eerst tot 15.00 uur, dan verder tot 16.10 uur.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Trek 35 van 10 af en tel de uren erbij. → Een uur heeft 60 minuten, niet 100. Werk in stappen naar een heel uur toe. · Tel de twee tijden bij elkaar op. → Je zoekt het verschil tussen vertrek en aankomst, niet een som.
    - **Uitleg (Claude):** Bij tijd reken je handig met stappen naar een heel uur. Van 14.35 uur naar 15.00 uur is 25 minuten. Daarna nog 1 uur en 10 minuten, samen 1 uur en 35 minuten.

- **Hint 1 (te schrijven):** Een uur heeft zestig minuten, geen honderd. Let daarop bij elke aanpak.
- **Hint 2 (te schrijven):** Probeer elke aanpak met de tijden uit de vraag. Kun je elke stap uitvoeren zonder onder de nul te komen? En kom je uit op een reistijd die kan?
- **Ouderzin:** Je kind kiest een handige aanpak voor een tijdsduur: eerst naar het hele uur, dan verder.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `minuten afgetrokken` (Trek 35 van 10 af en tel de uren erbij.) → De minuten bij aankomst zijn minder dan bij vertrek. Dan kom je onder de nul, en moet je een uur omwisselen voor zestig minuten. Dat kan, maar het is niet handig. Spring liever eerst naar het volgende hele uur.  [nieuw]
  - `tijden opgeteld` (Tel de twee tijden bij elkaar op.) → Twee tijden bij elkaar optellen geeft geen duur. Hoe lang is het van de vertrektijd tot de aankomsttijd?  [nieuw]
  - `andere fout` (andere fout) → Spring van de vertrektijd naar het volgende hele uur, en dan naar de aankomsttijd.  [nieuw]
- Status: hints klaar

## Somtype 17: Een [ding] is # m lang en # m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent # + # + # + # = #. Wat is er fout aan haar aanpak?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent # + # + # + # = #. Wat is er fout aan haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (2)
- Verschillende Claude-fout-hints: 2 (meest: “Denk aan tegels van 1 bij 1 meter op de bodem. Hoe tel je die het handigst?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-010` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een zwembad is 25 m lang en 10 m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent 25 + 10 + 25 + 10 = 70. Wat is er fout aan haar aanpak?
    - **Opties:** A) Ze rekende de omtrek in plaats van de oppervlakte · B) Niets, 70 vierkante meter klopt · C) Ze moest 25 + 10 doen en dat verdubbelen
    - **Antwoord:** Ze rekende de omtrek in plaats van de oppervlakte  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 70 vierkante meter klopt → Denk aan tegels van 1 bij 1 meter op de bodem. Hoe tel je die het handigst? · Ze moest 25 + 10 doen en dat verdubbelen → Dat geeft weer de lengte van de rand. De vraag gaat over het vlak binnen de rand.
    - **Uitleg (Claude):** Rondom optellen geeft de omtrek. Voor oppervlakte doe je lengte keer breedte: 25 × 10 = 250. De uitkomst is dus 250 vierkante meter.

- **Hint 1 (te schrijven):** Vierkante meters gaan over de oppervlakte. Wat rekende Fleur uit: de oppervlakte of de lengte rondom?
- **Hint 2 (te schrijven):** Reken de vierkante meters zelf uit: lengte keer breedte. Komt Fleur daarop uit? Kijk dan welke uitleg past bij wat zij wel uitrekende.
- **Ouderzin:** Je kind ziet het verschil tussen omtrek (de lengte rondom) en oppervlakte (lengte keer breedte).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omtrek goedgekeurd` (Niets, 70 vierkante meter klopt) → Fleur telde alle zijden bij elkaar op. Is dat de oppervlakte of de lengte rondom?  [nieuw]
  - `ook de omtrek` (Ze moest 25 + 10 doen en dat verdubbelen) → Dat is dezelfde som anders opgeschreven: ook dat geeft de lengte rondom. Vierkante meters gaan over de oppervlakte.  [nieuw]
  - `andere fout` (andere fout) → Wat geeft alle zijden bij elkaar optellen: de oppervlakte of de lengte rondom?  [nieuw]
- Status: hints klaar

## Somtype 18: Een [ding] is # m lang en # m breed. Je legt tegels van # vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Je legt tegels van # vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je legt tegels op de hele vloer, niet alleen langs de randen. Denk aan het vlak.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-011` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Een kamer is 5 m lang en 3 m breed. Je legt tegels van 1 vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?
    - **Opties:** A) Lengte en breedte bij elkaar optellen · B) Lengte keer breedte doen, dat is het aantal · C) Alle zijden bij elkaar optellen
    - **Antwoord:** Lengte keer breedte doen, dat is het aantal  (controle: n.v.t.)
    - **Fout-hints (Claude):** Alle zijden bij elkaar optellen → Je legt tegels op de hele vloer, niet alleen langs de randen. Denk aan het vlak. · Lengte en breedte bij elkaar optellen → Tel eens hoeveel tegels er in één rij liggen en hoeveel rijen er zijn.
    - **Uitleg (Claude):** De vloer bestaat uit 3 rijen van 5 tegels. Dat zijn 5 keer 3 tegels. Bij een vlak vermenigvuldig je de lengte met de breedte.

- **Hint 1 (te schrijven):** De tegels bedekken alles. Je zoekt dus de oppervlakte, niet de lengte rondom.
- **Hint 2 (te schrijven):** Denk aan rijen tegels. Hoeveel tegels passen er in één rij, en hoeveel rijen zijn er? Reken uit hoeveel tegels dat samen zijn. Welke aanpak geeft dat aantal?
- **Ouderzin:** Je kind kiest hoe je uitrekent hoeveel tegels er nodig zijn: de oppervlakte, lengte keer breedte.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `lengte plus breedte` (Lengte en breedte bij elkaar optellen) → Dan tel je maar één rij langs de lengte en één rij langs de breedte. De tegels moeten alles bedekken: hoeveel rijen tegels passen er?  [nieuw]
  - `omtrek` (Alle zijden bij elkaar optellen) → Alle zijden bij elkaar optellen geeft de omtrek: de lengte rondom. Tegels bedekken de oppervlakte.  [nieuw]
  - `andere fout` (andere fout) → Tegels bedekken de oppervlakte. Hoeveel rijen zijn er, en hoeveel tegels in één rij?  [nieuw]
- Status: hints klaar

## Somtype 19: Een [ding] is # m lang en # m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent # × # = #. Wat is er fout aan zijn aanpak?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent # × # = #. Wat is er fout aan zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een hek gaat langs alle vier de zijden. Keersommen horen bij het vlak binnen de tuin.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-012` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een tuin is 8 m lang en 5 m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent 8 × 5 = 40. Wat is er fout aan zijn aanpak?
    - **Opties:** A) Hij had 8 + 5 moeten doen · B) Hij rekende de oppervlakte in plaats van de omtrek · C) Hij had 8 × 5 × 2 moeten doen
    - **Antwoord:** Hij rekende de oppervlakte in plaats van de omtrek  (controle: n.v.t.)
    - **Fout-hints (Claude):** Hij had 8 × 5 × 2 moeten doen → Een hek gaat langs alle vier de zijden. Keersommen horen bij het vlak binnen de tuin. · Hij had 8 + 5 moeten doen → Je bent nu maar langs twee zijden gelopen. Hoeveel zijden heeft de tuin?
    - **Uitleg (Claude):** Voor een hek tel je alle zijden op: 8 + 5 + 8 + 5 = 26 meter. Met 8 × 5 bereken je hoeveel vierkante meter de tuin groot is. Dat is iets anders.

- **Hint 1 (te schrijven):** Een hek staat rondom. Je zoekt dus de omtrek: de lengte rondom.
- **Hint 2 (te schrijven):** Hoeveel meter hek is het echt? Tel alle zijden rondom bij elkaar op. Komt Joep daarop uit? Kijk dan welke uitleg past bij wat hij wel uitrekende.
- **Ouderzin:** Je kind ziet het verschil tussen omtrek (de lengte rondom) en oppervlakte (lengte keer breedte).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `twee zijden` (Hij had 8 + 5 moeten doen) → Dat zijn maar twee zijden. Een hek gaat helemaal rondom, langs alle vier de zijden.  [nieuw]
  - `oppervlakte verdubbeld` (Hij had 8 × 5 × 2 moeten doen) → Lengte keer breedte blijft een oppervlakte, ook als je het verdubbelt. Voor een hek tel je de zijden rondom bij elkaar op.  [nieuw]
  - `andere fout` (andere fout) → Een hek staat rondom. Zoekt Joep de omtrek of de oppervlakte?  [nieuw]
- Status: hints klaar

## Somtype 20: Een broek van €# wordt # procent goedkoper. Rik rekent uit dat de broek nu €# kost. Wat ging er mis?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Een broek van €# wordt # procent goedkoper. Rik rekent uit dat de broek nu €# [ding]. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Procent betekent 'van de honderd'. Reken eerst uit wat 10 procent van 40 is.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-013` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een broek van €40 wordt 10 procent goedkoper. Rik rekent uit dat de broek nu €30 kost. Wat ging er mis?
    - **Opties:** A) Hij haalde €10 eraf in plaats van 10 procent · B) Niets, 10 procent van €40 is €10 · C) Hij moest €10 bij de prijs optellen
    - **Antwoord:** Hij haalde €10 eraf in plaats van 10 procent  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 10 procent van €40 is €10 → Procent betekent 'van de honderd'. Reken eerst uit wat 10 procent van 40 is. · Hij moest €10 bij de prijs optellen → Goedkoper worden betekent dat de prijs daalt. Wat doe je dan met het kortingsbedrag?
    - **Uitleg (Claude):** 10 procent van €40 is €4, niet €10. De nieuwe prijs is dus €36. Rik verwarde procenten met euro's.

- **Hint 1 (te schrijven):** Procent betekent: van elke honderd. Hoeveel euro is de korting bij deze prijs?
- **Hint 2 (te schrijven):** Reken uit hoeveel euro de korting is: deel de prijs door honderd en doe dat keer het procent. Haal dat bedrag van de prijs af. Komt er hetzelfde uit als bij Rik?
- **Ouderzin:** Je kind ziet het verschil tussen een procent en een bedrag in euro.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `procent als euro` (Niets, 10 procent van €40 is €10) → Reken het na: deel de prijs door honderd en doe dat keer het procent. Is de korting echt zoveel euro?  [nieuw]
  - `erbij` (Hij moest €10 bij de prijs optellen) → De broek wordt goedkoper. Gaat de korting eraf of komt die erbij?  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel euro de korting is, en haal dat van de prijs af.  [nieuw]
- Status: hints klaar

## Somtype 21: Een jas van €# gaat # procent in prijs omlaag. Milou rekent uit dat de jas nu €# kost. Wat ging er mis?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Een jas van €# [ding] # procent in prijs omlaag. Milou rekent uit dat de jas nu €# [ding]. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het percentage hoort bij de oude prijs van de jas, niet bij je tussenantwoord.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-014` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een jas van €60 gaat 25 procent in prijs omlaag. Milou rekent uit dat de jas nu €15 kost. Wat ging er mis?
    - **Opties:** A) €15 is de korting, niet de nieuwe prijs · B) Ze moest 25 procent van 15 nemen · C) De jas kost nu €35
    - **Antwoord:** €15 is de korting, niet de nieuwe prijs  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze moest 25 procent van 15 nemen → Het percentage hoort bij de oude prijs van de jas, niet bij je tussenantwoord. · De jas kost nu €35 → Trek je korting netjes van de oude prijs af en reken het verschil nog eens na.
    - **Uitleg (Claude):** 25 procent van 60 is 15. Dat bedrag gaat eraf, dus de jas kost 60 − 15 = 45 euro. Lees na het rekenen altijd terug wat er gevraagd werd.

- **Hint 1 (te schrijven):** Bij korting horen twee bedragen: wat eraf gaat, en wat je daarna nog betaalt.
- **Hint 2 (te schrijven):** Reken allebei uit: hoeveel euro gaat er af, en wat kost de jas daarna? Welk van die twee bedragen rekende Milou uit?
- **Ouderzin:** Je kind ziet het verschil tussen de korting en de nieuwe prijs.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `procent van de uitkomst` (Ze moest 25 procent van 15 nemen) → Het procent hoort bij de oude prijs. Waarvan neem je het procent?  [nieuw]
  - `nieuwe prijs` (De jas kost nu €35) → Reken het na. Het procent is geen bedrag in euro: hoeveel euro is de korting? Haal die van de oude prijs af. Komt daar dit bedrag uit?  [nieuw]
  - `andere fout` (andere fout) → Is wat Milou uitrekende de korting of de nieuwe prijs?  [nieuw]
- Status: hints klaar

## Somtype 22: Een recept voor # [ding] vraagt # gram rijst. Daan wil koken voor # [ding] en pakt # gram. Klopt zijn aanpak?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Een recept voor # [ding] vraagt # gram rijst. Daan wil koken voor # [ding] en pakt # gram. Klopt zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij een recept groeien de personen en de grammen in dezelfde verhouding mee.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-015` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Een recept voor 4 personen vraagt 300 gram rijst. Daan wil koken voor 8 personen en pakt 600 gram. Klopt zijn aanpak?
    - **Opties:** A) Nee, hij moest 304 gram nemen · B) Ja, hij verdubbelde beide getallen · C) Nee, hij moest 300 + 8 nemen
    - **Antwoord:** Ja, hij verdubbelde beide getallen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, hij moest 300 + 8 nemen → Bij een recept groeien de personen en de grammen in dezelfde verhouding mee. · Nee, hij moest 304 gram nemen → Kijk hoeveel keer zo groot de groep wordt en doe met de rijst hetzelfde.
    - **Uitleg (Claude):** Van 4 naar 8 personen is twee keer zo veel. Dan gaat ook de rijst twee keer zo veel: 2 × 300 is 600 gram. De verhouding blijft gelijk.

- **Hint 1 (te schrijven):** Bij een recept hoort bij meer mensen ook meer rijst: hoeveel keer zoveel mensen worden het?
- **Hint 2 (te schrijven):** Hoeveel keer zoveel mensen worden het? Dan heb je evenveel keer zoveel rijst nodig. Deed Daan dat?
- **Ouderzin:** Je kind controleert een aanpak met verhoudingen: twee keer zoveel mensen is twee keer zoveel rijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `mensen erbij` (Nee, hij moest 304 gram nemen) → Dan krijgt elke extra persoon maar één gram rijst. Hoeveel keer zoveel mensen worden het, en hoeveel rijst hoort daarbij?  [nieuw]
  - `mensen bij de grammen` (Nee, hij moest 300 + 8 nemen) → Dan tel je het aantal mensen bij de grammen op. Hoeveel keer zoveel mensen worden het?  [nieuw]
  - `andere fout` (andere fout) → Hoeveel keer zoveel mensen worden het? Hoort daar evenveel keer zoveel rijst bij?  [nieuw]
- Status: hints klaar

## Somtype 23: Een recept voor # [ding] vraagt # gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor # [ding]?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “Een recept voor # [ding] vraagt # gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor # [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (2)
- Verschillende Claude-fout-hints: 2 (meest: “Personen en grammen zijn verschillende dingen. Zoek eerst hoeveel rijst één persoon nodig heeft.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-016` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Een recept voor 4 personen vraagt 200 gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor 6 personen?
    - **Opties:** A) Tel 200 en 6 bij elkaar op · B) Doe 200 keer 6 · C) Deel 200 door 4 en doe dat keer 6
    - **Antwoord:** Deel 200 door 4 en doe dat keer 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 200 en 6 bij elkaar op → Personen en grammen zijn verschillende dingen. Zoek eerst hoeveel rijst één persoon nodig heeft. · Doe 200 keer 6 → Zes personen eten niet zes keer zoveel als vier personen. Reken eerst per persoon.
    - **Uitleg (Claude):** Eén persoon krijgt 200 gedeeld door 4, dus 50 gram. Zes personen krijgen dan 6 keer 50 gram. Via één persoon rekenen werkt altijd.

- **Hint 1 (te schrijven):** Reken eerst uit hoeveel rijst één persoon nodig heeft.
- **Hint 2 (te schrijven):** Reken het uit: hoeveel rijst is er voor één persoon, en hoeveel dan voor alle mensen waarvoor je kookt? Reken ook elke aanpak uit. Welke geeft hetzelfde?
- **Ouderzin:** Je kind kiest de aanpak via één: eerst hoeveel rijst voor één persoon, dan voor iedereen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `mensen bij de grammen` (Tel 200 en 6 bij elkaar op) → Dan tel je mensen bij grammen op. Hoeveel rijst is er voor één persoon?  [nieuw]
  - `hele recept per persoon` (Doe 200 keer 6) → Dan krijgt elke persoon de rijst van het hele recept. Het recept is al voor meer mensen: hoeveel is er voor één persoon?  [nieuw]
  - `andere fout` (andere fout) → Hoeveel rijst heeft één persoon nodig?  [nieuw]
- Status: hints klaar

## Somtype 24: Een stadion heeft # [ding] met # [ding]. Anne schat vooraf ongeveer # [ding] en rekent daarna precies # uit. Wat zegt dit over haar aanpak?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Een stadion heeft # [ding] met # [ding]. Anne schat vooraf ongeveer # [ding] en rekent daarna precies # uit. Wat zegt dit over haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): afronden-verkeerde-kant (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een schatting is een ruwe benadering. Die hoeft niet precies gelijk te zijn aan de echte uitkomst.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-017` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een stadion heeft 4 vakken met 1980 stoelen. Anne schat vooraf ongeveer 8000 stoelen en rekent daarna precies 7920 uit. Wat zegt dit over haar aanpak?
    - **Opties:** A) Haar schatting was fout, want 4 × 2000 is 800 · B) Haar schatting past goed bij het antwoord · C) Ze rekende fout, want het moet 8000 zijn
    - **Antwoord:** Haar schatting past goed bij het antwoord  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze rekende fout, want het moet 8000 zijn → Een schatting is een ruwe benadering. Die hoeft niet precies gelijk te zijn aan de echte uitkomst. · Haar schatting was fout, want 4 × 2000 is 800 → Reken 4 × 2000 nog eens rustig na en let op het aantal nullen.
    - **Uitleg (Claude):** 1980 is bijna 2000 en 4 × 2000 is 8000. De echte uitkomst 7920 ligt daar vlak onder. De schatting laat dus zien dat het antwoord klopt.

- **Hint 1 (te schrijven):** Een schatting is ongeveer. Ligt het precieze antwoord dicht bij de schatting?
- **Hint 2 (te schrijven):** Reken de schatting na met ronde getallen. Kijk dan hoe ver het precieze antwoord ervan af ligt. Is dat weinig, dan past de schatting.
- **Ouderzin:** Je kind beoordeelt een schatting: een schatting hoeft niet precies te kloppen, wel ongeveer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul vergeten` (Haar schatting was fout, want 4 × 2000 is 800) → Reken het na en tel de nullen. Hoeveel nullen heeft het ronde getal, en hoeveel heeft de uitkomst?  [nieuw]
  - `schatting als antwoord` (Ze rekende fout, want het moet 8000 zijn) → Een schatting is ongeveer, niet precies. Het precieze antwoord mag een beetje van de schatting afwijken.  [nieuw]
  - `andere fout` (andere fout) → Ligt het precieze antwoord dicht bij de schatting?  [nieuw]
- Status: hints klaar

## Somtype 25: Eva rekent # : # uit en krijgt #. Hoe kan ze snel controleren of dit klopt?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Eva rekent # : # uit en krijgt #. Hoe kan ze snel controleren of dit klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Optellen is niet de omgekeerde bewerking van delen. Welke som maakt delen ongedaan?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-018` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Eva rekent 63 : 7 uit en krijgt 8. Hoe kan ze snel controleren of dit klopt?
    - **Opties:** A) Het antwoord nog een keer overschrijven · B) 7 × 8 uitrekenen en met 63 vergelijken · C) 63 + 7 uitrekenen en kijken of het klopt
    - **Antwoord:** 7 × 8 uitrekenen en met 63 vergelijken  (controle: n.v.t.)
    - **Fout-hints (Claude):** 63 + 7 uitrekenen en kijken of het klopt → Optellen is niet de omgekeerde bewerking van delen. Welke som maakt delen ongedaan? · Het antwoord nog een keer overschrijven → Overschrijven laat een rekenfout gewoon staan. Je hebt een echte controlesom nodig.
    - **Uitleg (Claude):** Delen controleer je met vermenigvuldigen. 7 × 8 is 56 en dat is niet 63, dus het antwoord klopt niet. Zo vind je je fout meteen.

- **Hint 1 (te schrijven):** Een deling controleer je met de omgekeerde som.
- **Hint 2 (te schrijven):** Reken elke manier uit met de getallen van Eva. Bij welke manier zie je echt of haar antwoord goed is? Een goede controle laat ook een fout zien.
- **Ouderzin:** Je kind controleert een deelsom met de omgekeerde keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overschrijven` (Het antwoord nog een keer overschrijven) → Overschrijven controleert niets: een fout schrijf je zo ook over. Welke som is het omgekeerde van gedeeld door?  [nieuw]
  - `plus` (63 + 7 uitrekenen en kijken of het klopt) → Plus is niet het omgekeerde van gedeeld door. Welke som hoort andersom bij gedeeld door?  [nieuw]
  - `andere fout` (andere fout) → Wat is het omgekeerde van gedeeld door?  [nieuw]
- Status: hints klaar

## Somtype 26: Fenna heeft # + # = # uitgerekend. Hoe kan zij haar antwoord het beste controleren?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Fenna heeft # + # = # [ding]. Hoe kan zij haar antwoord het beste controleren?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Als je dezelfde weg nog eens loopt, maak je vaak dezelfde fout. Zoek een andere weg terug.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-019` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Fenna heeft 234 + 178 = 412 uitgerekend. Hoe kan zij haar antwoord het beste controleren?
    - **Opties:** A) De som nog een keer precies zo uitrekenen · B) 412 + 178 uitrekenen · C) 412 − 178 uitrekenen en kijken of 234 komt
    - **Antwoord:** 412 − 178 uitrekenen en kijken of 234 komt  (controle: n.v.t.)
    - **Fout-hints (Claude):** De som nog een keer precies zo uitrekenen → Als je dezelfde weg nog eens loopt, maak je vaak dezelfde fout. Zoek een andere weg terug. · 412 + 178 uitrekenen → Om terug te gaan naar het begin moet je de bewerking omkeren.
    - **Uitleg (Claude):** Optellen en aftrekken zijn elkaars omgekeerde. Haal je 178 weer van 412 af, dan hoor je op 234 uit te komen. Zo controleer je via een andere weg.

- **Hint 1 (te schrijven):** Een plussom controleer je het best met de omgekeerde som.
- **Hint 2 (te schrijven):** Een goede controle rekent anders dan de som zelf, en geeft een getal dat je kunt vergelijken. Reken elke manier uit met de getallen van Fenna. Welke manier doet dat?
- **Ouderzin:** Je kind controleert een plussom met de omgekeerde minsom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nog een keer hetzelfde` (De som nog een keer precies zo uitrekenen) → Dan maak je misschien dezelfde fout nog eens. Met de omgekeerde som controleer je op een andere manier.  [nieuw]
  - `nog meer erbij` (412 + 178 uitrekenen) → Nog meer erbij doen controleert de plussom niet. Wat is het omgekeerde van plus?  [nieuw]
  - `andere fout` (andere fout) → Wat is het omgekeerde van plus?  [nieuw]
- Status: hints klaar

## Somtype 27: Hoe zie je of een getal deelbaar is door 5?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Hoe zie je of een getal deelbaar is door #?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Probeer je stap eens bij 53 en bij 25. Welk cijfer verraadt de deling door 5?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-020` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Hoe zie je of een getal deelbaar is door 5?
    - **Opties:** A) Kijk of het laatste cijfer 0 of 5 is · B) Kijk of het eerste cijfer 0 of 5 is · C) Kijk of het getal even is
    - **Antwoord:** Kijk of het laatste cijfer 0 of 5 is  (controle: n.v.t.)
    - **Fout-hints (Claude):** Kijk of het eerste cijfer 0 of 5 is → Probeer je stap eens bij 53 en bij 25. Welk cijfer verraadt de deling door 5? · Kijk of het getal even is → Probeer je stap eens bij 12 en bij 15. Klopt hij dan nog?
    - **Uitleg (Claude):** Alle veelvouden van 5 eindigen op 0 of 5. Het laatste cijfer bepaalt dus het antwoord. Deze stap werkt bij elk getal.

- **Hint 1 (te schrijven):** Schrijf een paar uitkomsten uit de tafel van dat getal op. Wat zie je steeds terugkomen?
- **Hint 2 (te schrijven):** Neem een paar getallen uit de tafel van dat getal, en een paar die er niet in zitten. Probeer elke manier uit. Welke manier klopt bij al die getallen?
- **Ouderzin:** Je kind weet hoe je ziet of een getal in de tafel van vijf zit: kijk naar het cijfer van de eenheden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfer links` (Kijk of het eerste cijfer 0 of 5 is) → De uitkomsten van de tafel beginnen met allerlei cijfers. Kijk naar het laatste cijfer, bij de eenheden.  [nieuw]
  - `even` (Kijk of het getal even is) → In die tafel zitten ook oneven getallen, en niet elk even getal zit erin. Kijk naar het laatste cijfer, bij de eenheden.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar het laatste cijfer, bij de eenheden. Op welke cijfers eindigt de tafel?  [nieuw]
- Status: hints klaar

## Somtype 28: Hoe zie je of een getal even is?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Hoe zie je of een getal even is?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij even en oneven telt alleen het cijfer op de plaats van de eenheden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-021` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Hoe zie je of een getal even is?
    - **Opties:** A) Kijk of het laatste cijfer 0, 2, 4, 6 of 8 is. · B) Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is. · C) Kijk of je het getal door 3 kunt delen.
    - **Antwoord:** Kijk of het laatste cijfer 0, 2, 4, 6 of 8 is.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is. → Bij even en oneven telt alleen het cijfer op de plaats van de eenheden. · Kijk of je het getal door 3 kunt delen. → Even betekent dat je het eerlijk in twee gelijke delen kunt splitsen.
    - **Uitleg (Claude):** Een even getal is deelbaar door 2. Daarvoor hoef je alleen naar het cijfer van de eenheden te kijken. Is dat 0, 2, 4, 6 of 8, dan is het getal even.

- **Hint 1 (te schrijven):** Even getallen zitten in de tafel van twee: je kunt ze eerlijk in tweeën verdelen.
- **Hint 2 (te schrijven):** Neem een paar even en een paar oneven getallen, ook grote. Probeer elke manier uit. Welke manier klopt bij al die getallen?
- **Ouderzin:** Je kind weet hoe je ziet of een getal even is: kijk naar het cijfer van de eenheden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfer links` (Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is.) → Het eerste cijfer zegt niet of een getal even is. Kijk naar het laatste cijfer, bij de eenheden.  [nieuw]
  - `tafel van drie` (Kijk of je het getal door 3 kunt delen.) → Even betekent: in de tafel van twee, niet in de tafel van drie.  [nieuw]
  - `andere fout` (andere fout) → Even betekent: in de tafel van twee. Kijk naar het laatste cijfer, bij de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 29: In een staafgrafiek staat de temperatuur per dag. Ruben leest bij woensdag # graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag # graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De vraag gaat over één bepaalde dag. De hoogste staaf hoort daar niet altijd bij.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-030` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** In een staafgrafiek staat de temperatuur per dag. Ruben leest bij woensdag 14 graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?
    - **Opties:** A) Altijd de hoogste staaf kiezen · B) De getallen links bij elkaar optellen · C) Eerst de naam onder de staaf lezen
    - **Antwoord:** Eerst de naam onder de staaf lezen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Altijd de hoogste staaf kiezen → De vraag gaat over één bepaalde dag. De hoogste staaf hoort daar niet altijd bij. · De getallen links bij elkaar optellen → De getallen links vormen de schaal. Je hoeft ze niet op te tellen om één waarde af te lezen.
    - **Uitleg (Claude):** Onder elke staaf staat bij welke dag hij hoort. Zoek eerst de juiste dag en ga dan omhoog naar de waarde. Zo lees je de goede staaf af.

- **Hint 1 (te schrijven):** Ruben keek bij de verkeerde dag. Hoe weet je bij welke dag een staaf hoort?
- **Hint 2 (te schrijven):** Onder elke staaf staat bij welke dag die hoort. Lees dat eerst, en kijk dan pas hoe hoog de staaf is.
- **Ouderzin:** Je kind leert een grafiek nauwkeurig aflezen: eerst kijken bij welke dag een staaf hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hoogste staaf` (Altijd de hoogste staaf kiezen) → De hoogste staaf hoort bij één dag, en dat hoeft woensdag niet te zijn. Hoe zie je bij welke dag een staaf hoort?  [nieuw]
  - `schaal opgeteld` (De getallen links bij elkaar optellen) → De getallen langs de kant zijn de schaal om af te lezen. Hoe zie je bij welke dag een staaf hoort?  [nieuw]
  - `andere fout` (andere fout) → Hoe zie je bij welke dag een staaf hoort?  [nieuw]
- Status: hints klaar

## Somtype 30: In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Niet elke dag kwamen er evenveel bezoekers. Kijk naar alle staven apart.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-031` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?
    - **Opties:** A) Lees elke staaf af en tel alle waarden op · B) Lees de hoogste staaf af en doe die keer 7 · C) Trek de laagste staaf van de hoogste af
    - **Antwoord:** Lees elke staaf af en tel alle waarden op  (controle: n.v.t.)
    - **Fout-hints (Claude):** Lees de hoogste staaf af en doe die keer 7 → Niet elke dag kwamen er evenveel bezoekers. Kijk naar alle staven apart. · Trek de laagste staaf van de hoogste af → Zo vind je een verschil, geen totaal. Wat doe je met alle dagen samen?
    - **Uitleg (Claude):** Elke staaf hoort bij één dag. Voor het totaal heb je alle dagen nodig. Je leest elke staaf af en telt de getallen bij elkaar op.

- **Hint 1 (te schrijven):** Het totaal van de week is alle dagen bij elkaar.
- **Hint 2 (te schrijven):** Bedenk een week waarin het niet elke dag even druk is. Telt elke manier elke dag mee, met het eigen aantal van die dag?
- **Ouderzin:** Je kind leest een staafgrafiek af en telt de waarden van alle dagen op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hoogste keer de week` (Lees de hoogste staaf af en doe die keer 7) → Dan doe je alsof het elke dag even druk was als op de drukste dag. Lees elke staaf apart af.  [nieuw]
  - `verschil` (Trek de laagste staaf van de hoogste af) → Dat is het verschil tussen de drukste en de rustigste dag, niet het totaal.  [nieuw]
  - `andere fout` (andere fout) → Het totaal van de week is alle dagen bij elkaar.  [nieuw]
- Status: hints klaar

## Somtype 31: In een winkel is er op alles # procent korting. Hoe reken je de nieuwe prijs uit?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “In een winkel is er op alles # procent korting. Hoe reken je de nieuwe prijs uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “Met korting betaal je minder dan eerst. Gaat de prijs dan omhoog of omlaag?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-032` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** In een winkel is er op alles 25 procent korting. Hoe reken je de nieuwe prijs uit?
    - **Opties:** A) Bereken 25 procent van de korting en trek dat eraf. · B) Bereken 25 procent van de prijs en trek dat eraf. · C) Bereken 25 procent van de prijs en tel dat erbij op.
    - **Antwoord:** Bereken 25 procent van de prijs en trek dat eraf.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Bereken 25 procent van de prijs en tel dat erbij op. → Met korting betaal je minder dan eerst. Gaat de prijs dan omhoog of omlaag? · Bereken 25 procent van de korting en trek dat eraf. → Let op waarvan je het percentage neemt. Waarvan gaat de 25 procent af?
    - **Uitleg (Claude):** De korting hoort bij de oude prijs, dus daarvan neem je 25 procent. Dat bedrag haal je van de oude prijs af. Zo houd je de nieuwe prijs over.

- **Hint 1 (te schrijven):** Korting gaat van de prijs af. Waarvan neem je het procent?
- **Hint 2 (te schrijven):** Bedenk een prijs, bijvoorbeeld honderd euro. Reken uit wat je met de korting nog betaalt. Reken elke manier uit met die prijs. Welke geeft hetzelfde?
- **Ouderzin:** Je kind kiest hoe je een prijs met korting uitrekent: het procent van de prijs, en dat eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `procent van de korting` (Bereken 25 procent van de korting en trek dat eraf.) → De korting weet je nog niet: die reken je juist uit. Het procent hoort bij de prijs.  [nieuw]
  - `erbij` (Bereken 25 procent van de prijs en tel dat erbij op.) → Met korting wordt het goedkoper. Gaat de korting eraf of komt die erbij?  [nieuw]
  - `andere fout` (andere fout) → Neem het procent van de prijs. Gaat dat eraf of erbij?  [nieuw]
- Status: hints klaar

## Somtype 32: In groep # zitten # leerlingen. # procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?

- Sleutel: nrOrigineel **25** · somtypeOrigineel “In groep # [ding] # [ding]. # procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “Procenten zijn delen van het geheel, geen aantal dat je eraf haalt. Zoek eerst 1 procent.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-033` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** In groep 8 zitten 40 leerlingen. 15 procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?
    - **Opties:** A) Deel 100 door 40 en doe dat keer 15 · B) Deel 40 door 100 en doe dat keer 15 · C) Trek 15 van 40 af
    - **Antwoord:** Deel 40 door 100 en doe dat keer 15  (controle: n.v.t.)
    - **Fout-hints (Claude):** Trek 15 van 40 af → Procenten zijn delen van het geheel, geen aantal dat je eraf haalt. Zoek eerst 1 procent. · Deel 15 door 100 en doe dat keer 40 procent → Let goed op waarvan je het deel wilt weten. Van welk getal bereken je hier de procenten?
    - **Uitleg (Claude):** Eén procent van 40 is 40 gedeeld door 100, dus 0,4. Vijftien procent is 15 keer 0,4. Dat zijn 6 leerlingen.

- **Hint 1 (te schrijven):** Procent betekent: van elke honderd. Alle leerlingen samen zijn honderd procent.
- **Hint 2 (te schrijven):** Reken het uit: hoeveel leerlingen is één procent, en hoeveel is dan het procent uit de vraag? Reken ook elke manier uit. Welke geeft hetzelfde aantal leerlingen?
- **Ouderzin:** Je kind kiest hoe je een procent van een aantal uitrekent: eerst één procent, dan keer het procent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `honderd door het aantal gedeeld` (Deel 100 door 40 en doe dat keer 15) → Dan deel je honderd door het aantal leerlingen. Hoeveel leerlingen is één procent: welk getal deel je door honderd?  [nieuw]
  - `afgetrokken` (Trek 15 van 40 af) → Het procent is geen aantal leerlingen. Hoeveel leerlingen is één procent van alle leerlingen?  [nieuw]
  - `andere fout` (andere fout) → Hoeveel leerlingen is één procent? Doe dat keer het procent.  [nieuw]
- Status: hints klaar

## Somtype 33: Je doet # kg appels in zakjes van # gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Je doet # kg appels in zakjes van # gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed hoeveel gram er in 1 kg gaat. Wordt het getal dan groter of kleiner?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-034` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je doet 2,5 kg appels in zakjes van 500 gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?
    - **Opties:** A) Deel 2,5 direct door 500. · B) Reken 2,5 kg om naar 2500 gram. · C) Reken 500 gram om naar 5 kg.
    - **Antwoord:** Reken 2,5 kg om naar 2500 gram.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Reken 500 gram om naar 5 kg. → Kijk goed hoeveel gram er in 1 kg gaat. Wordt het getal dan groter of kleiner? · Deel 2,5 direct door 500. → Je kunt pas rekenen als beide getallen dezelfde eenheid hebben.
    - **Uitleg (Claude):** Je kunt alleen rekenen met dezelfde eenheid. In 1 kg zitten 1000 gram, dus 2,5 kg is 2500 gram. Daarna deel je 2500 door 500.

- **Hint 1 (te schrijven):** De ene maat staat in kilogram, de andere in gram. Maak eerst van allebei dezelfde maat.
- **Hint 2 (te schrijven):** Eén kilogram is duizend gram. Reken elke stap na: klopt het omrekenen, en staan daarna allebei de getallen in dezelfde maat?
- **Ouderzin:** Je kind ziet dat je eerst dezelfde maat nodig hebt: kilogram omrekenen naar gram.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `direct delen` (Deel 2,5 direct door 500.) → Kilogram en gram zijn verschillende maten. Maak eerst van allebei dezelfde maat.  [nieuw]
  - `verkeerd omgerekend` (Reken 500 gram om naar 5 kg.) → Reken het na: duizend gram is één kilogram. Dan is dit minder dan één kilogram.  [nieuw]
  - `andere fout` (andere fout) → Maak eerst van allebei dezelfde maat: één kilogram is duizend gram.  [nieuw]
- Status: hints klaar

## Somtype 34: Je fietst # [ding] in # uur. Hoe reken je uit hoeveel kilometer je in # uur fietst?

- Sleutel: nrOrigineel **27** · somtypeOrigineel “Je fietst # [ding] in # uur. Hoe reken je uit hoeveel kilometer je in # uur fietst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “In één uur fiets je minder ver dan in twee uur. Wordt je antwoord dan groter of kleiner?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-035` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je fietst 24 kilometer in 2 uur. Hoe reken je uit hoeveel kilometer je in 1 uur fietst?
    - **Opties:** A) Deel 24 door 2 · B) Vermenigvuldig 24 met 2 · C) Trek 2 van 24 af
    - **Antwoord:** Deel 24 door 2  (controle: n.v.t.)
    - **Fout-hints (Claude):** Vermenigvuldig 24 met 2 → In één uur fiets je minder ver dan in twee uur. Wordt je antwoord dan groter of kleiner? · Trek 2 van 24 af → Je verdeelt de kilometers over de uren. Welke bewerking hoort bij eerlijk verdelen?
    - **Uitleg (Claude):** Je wilt weten hoeveel kilometer je per uur aflegt. Je verdeelt 24 kilometer over 2 uur. 24 gedeeld door 2 is 12 kilometer per uur.

- **Hint 1 (te schrijven):** Elk uur fiets je even ver. Hoeveel kilometer is dat in één uur?
- **Hint 2 (te schrijven):** Elk uur fiets je even ver. Reken elke aanpak uit en doe de uitkomst keer het aantal uren. Bij welke aanpak kom je weer op alle kilometers uit?
- **Ouderzin:** Je kind kiest de aanpak via één: hoeveel kilometer in één uur.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer` (Vermenigvuldig 24 met 2) → Dan krijg je de kilometers van meer uren, niet van één uur.  [nieuw]
  - `uren eraf` (Trek 2 van 24 af) → Je haalt dan uren van kilometers af. Elk uur fiets je even ver: hoeveel kilometer is dat in één uur?  [nieuw]
  - `andere fout` (andere fout) → Elk uur fiets je even ver. Hoeveel kilometer is dat in één uur?  [nieuw]
- Status: hints klaar

## Somtype 35: Je hebt # [ding] en # [ding]. Hoe reken je uit hoeveel koekjes [wie] krijgt en hoeveel er overblijven?

- Sleutel: nrOrigineel **28** · somtypeOrigineel “Je hebt # [ding] en # [ding]. Hoe reken je uit hoeveel koekjes [wie] krijgt en hoeveel er overblijven?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): rest-vergeten (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je kunt geen koekje uitdelen dat er niet is. Wat gebeurt er met de koekjes die overblijven?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-036` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 50 koekjes en 8 kinderen. Hoe reken je uit hoeveel koekjes elk kind krijgt en hoeveel er overblijven?
    - **Opties:** A) Deel 50 door 8 en rond naar boven af · B) Trek 8 van 50 af, dat is het antwoord · C) Deel 50 door 8 en kijk naar de rest
    - **Antwoord:** Deel 50 door 8 en kijk naar de rest  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 50 door 8 en rond naar boven af → Je kunt geen koekje uitdelen dat er niet is. Wat gebeurt er met de koekjes die overblijven? · Trek 8 van 50 af, dat is het antwoord → Eerlijk verdelen over groepjes doe je niet met aftrekken. Welke bewerking hoort bij verdelen?
    - **Uitleg (Claude):** 50 gedeeld door 8 is 6, want 8 keer 6 is 48. Er blijven dan 2 koekjes over. Elk kind krijgt er 6 en er blijven er 2 liggen.

- **Hint 1 (te schrijven):** Eerlijk verdelen is delen. Soms blijft er iets over.
- **Hint 2 (te schrijven):** Reken het uit: hoeveel koekjes krijgt ieder, en hoeveel blijven er over? Reken dan elke aanpak uit. Welke aanpak geeft allebei?
- **Ouderzin:** Je kind kiest hoe je eerlijk verdeelt: delen, en kijken wat er overblijft.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `naar boven` (Deel 50 door 8 en rond naar boven af) → Naar boven afronden geeft koekjes die er niet zijn. De vraag wil ook weten hoeveel er overblijven: kijk naar de rest.  [nieuw]
  - `afgetrokken` (Trek 8 van 50 af, dat is het antwoord) → Dan krijgt ieder maar één koekje. Bij eerlijk verdelen deel je het aantal koekjes door het aantal mensen.  [nieuw]
  - `andere fout` (andere fout) → Eerlijk verdelen is delen. Hoeveel krijgt ieder, en wat blijft er over?  [nieuw]
- Status: hints klaar

## Somtype 36: Je hebt # [ding] en dozen voor # [ding]. Hoe reken je uit hoeveel volle dozen je kunt maken?

- Sleutel: nrOrigineel **29** · somtypeOrigineel “Je hebt # [ding] en dozen voor # [ding]. Hoe reken je uit hoeveel volle dozen je kunt maken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): afronden-verkeerde-kant (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een doos telt alleen mee als hij helemaal vol is. Wat doe je met de eieren die overblijven?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-037` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Je hebt 40 eieren en dozen voor 6 eieren. Hoe reken je uit hoeveel volle dozen je kunt maken?
    - **Opties:** A) Deel 40 door 6 en rond het antwoord naar boven af. · B) Trek 6 van 40 af en noem dat het aantal dozen. · C) Deel 40 door 6 en gebruik alleen het hele aantal.
    - **Antwoord:** Deel 40 door 6 en gebruik alleen het hele aantal.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 40 door 6 en rond het antwoord naar boven af. → Een doos telt alleen mee als hij helemaal vol is. Wat doe je met de eieren die overblijven? · Trek 6 van 40 af en noem dat het aantal dozen. → Je verdeelt de eieren in groepjes van 6. Welke bewerking maakt groepjes?
    - **Uitleg (Claude):** Je verdeelt de eieren in groepjes van 6, dus je deelt. 40 gedeeld door 6 is 6 met een rest. Alleen de volle dozen tellen, dus je gebruikt het hele aantal.

- **Hint 1 (te schrijven):** Alleen dozen die helemaal vol zijn tellen mee. Hoe vaak past de inhoud van één doos in het totaal?
- **Hint 2 (te schrijven):** Vul in gedachten de dozen een voor een. Hoeveel worden er helemaal vol? Reken dan elke aanpak uit. Welke geeft hetzelfde aantal?
- **Ouderzin:** Je kind kiest hoe je uitrekent hoeveel volle dozen het worden: delen en alleen het hele getal gebruiken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `naar boven` (Deel 40 door 6 en rond het antwoord naar boven af.) → Dan tel je een doos mee die niet vol is. De vraag gaat over volle dozen.  [nieuw]
  - `afgetrokken` (Trek 6 van 40 af en noem dat het aantal dozen.) → Dan haal je maar één doos eraf. Hoe vaak past de inhoud van één doos in het totaal?  [nieuw]
  - `andere fout` (andere fout) → Hoe vaak past de inhoud van één doos in het totaal? Alleen volle dozen tellen.  [nieuw]
- Status: hints klaar

## Somtype 37: Je koopt # [ding] van # euro en # [ding] van # euro. Hoe reken je uit hoeveel je in totaal betaalt?

- Sleutel: nrOrigineel **30** · somtypeOrigineel “Je koopt # [ding] van # euro en # [ding] van # euro. Hoe reken je uit hoeveel je in totaal betaalt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “De truien en de petten kosten niet hetzelfde. Reken elke soort eerst apart uit.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-038` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Je koopt 3 truien van 12 euro en 2 petten van 7 euro. Hoe reken je uit hoeveel je in totaal betaalt?
    - **Opties:** A) Reken 3 maal 12 en tel 2 en 7 erbij op. · B) Reken 3 maal 12 en 2 maal 7 en tel die uitkomsten op. · C) Tel 12 en 7 op en doe dat maal 5.
    - **Antwoord:** Reken 3 maal 12 en 2 maal 7 en tel die uitkomsten op.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 12 en 7 op en doe dat maal 5. → De truien en de petten kosten niet hetzelfde. Reken elke soort eerst apart uit. · Reken 3 maal 12 en tel 2 en 7 erbij op. → Ook bij de petten koop je er meer dan één van dezelfde prijs.
    - **Uitleg (Claude):** Je rekent eerst per soort het bedrag uit met een vermenigvuldiging. Zo krijg je 36 euro en 14 euro. Die twee bedragen tel je op tot het totaal.

- **Hint 1 (te schrijven):** Je koopt van twee soorten meer dan één stuk, elke soort met een eigen prijs.
- **Hint 2 (te schrijven):** Reken eerst zelf uit wat je in totaal betaalt. Reken dan elke aanpak uit. Welke komt op hetzelfde bedrag?
- **Ouderzin:** Je kind kiest hoe je een totaalprijs uitrekent: eerst per soort het aantal keer de prijs, dan die bedragen optellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `aantal bij de prijs` (Reken 3 maal 12 en tel 2 en 7 erbij op.) → Dan tel je bij één soort het aantal bij de prijs op. Ook van die soort koop je meer dan één stuk van dezelfde prijs: wat kost dat samen?  [nieuw]
  - `prijzen samen` (Tel 12 en 7 op en doe dat maal 5.) → Dan reken je alsof elk stuk de twee prijzen samen kost. Elke soort heeft een eigen prijs en een eigen aantal: reken ze apart uit.  [nieuw]
  - `andere fout` (andere fout) → Wat kost alles van één soort samen? Doe dat voor allebei de soorten, en tel de bedragen op.  [nieuw]
- Status: hints klaar

## Somtype 38: Je koopt een pen van # euro en een gum van # euro. Je betaalt met # euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?

- Sleutel: nrOrigineel **31** · somtypeOrigineel “Je koopt een pen van # euro en een gum van # euro. Je betaalt met # euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je krijgt geld terug, dus het bedrag wordt kleiner. Welke bewerking hoort daarbij?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-039` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je koopt een pen van 2 euro en een gum van 1 euro. Je betaalt met 5 euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?
    - **Opties:** A) Tel de prijzen op, trek die van het betaalde bedrag af. · B) Tel de prijzen op, tel die bij het betaalde bedrag op. · C) Tel de prijzen op en noem die uitkomst het wisselgeld.
    - **Antwoord:** Tel de prijzen op, trek die van het betaalde bedrag af.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel de prijs op, tel die bij het betaalde bedrag op. → Je krijgt geld terug, dus het bedrag wordt kleiner. Welke bewerking hoort daarbij? · Tel de prijs op en noem die uitkomst het wisselgeld. → Het wisselgeld is niet de prijs zelf. Je moet de prijs nog met het betaalde bedrag vergelijken.
    - **Uitleg (Claude):** Eerst bepaal je het totaal van wat je koopt. Dat totaal haal je van het betaalde bedrag af. Wat overblijft, is het wisselgeld.

- **Hint 1 (te schrijven):** Wisselgeld is wat je terugkrijgt, omdat je meer gaf dan alles kost.
- **Hint 2 (te schrijven):** Reken eerst zelf uit hoeveel je terugkrijgt. Reken dan elke aanpak uit. Welke komt op hetzelfde bedrag?
- **Ouderzin:** Je kind kiest hoe je wisselgeld uitrekent: eerst wat alles kost, dan dat van het betaalde bedrag afhalen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij in plaats van eraf` (Tel de prijzen op, tel die bij het betaalde bedrag op.) → Dan kom je op meer uit dan je betaalde. Kun je meer terugkrijgen dan je gaf?  [nieuw]
  - `prijs als wisselgeld` (Tel de prijzen op en noem die uitkomst het wisselgeld.) → Dat is wat alles samen kost, niet wat je terugkrijgt. Hoeveel heb je meer betaald dan dat?  [nieuw]
  - `andere fout` (andere fout) → Wat kost alles samen, en hoeveel heb je meer betaald dan dat?  [nieuw]
- Status: hints klaar

## Somtype 39: Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?

- Sleutel: nrOrigineel **32** · somtypeOrigineel “Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Let op de volgorde. Je kunt een boek pas pakken als je weet waar het staat.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-040` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?
    - **Opties:** A) Pak het boek, zoek de letter, loop naar dat vak. · B) Loop door de bibliotheek tot je iets leuks ziet. · C) Zoek de letter, loop naar dat vak, pak het boek.
    - **Antwoord:** Zoek de letter, loop naar dat vak, pak het boek.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Pak het boek, zoek de letter, loop naar dat vak. → Let op de volgorde. Je kunt een boek pas pakken als je weet waar het staat. · Loop door de bibliotheek tot je iets leuks ziet. → Een goede uitleg werkt altijd, ook voor iemand anders. Zomaar rondlopen leidt niet steeds naar het juiste boek.
    - **Uitleg (Claude):** Een goede uitleg zet de stappen in de juiste volgorde. Eerst zoek je waar het boek hoort, dan loop je erheen. Pas daarna kun je het boek pakken.

- **Hint 1 (te schrijven):** Een goede uitleg werkt altijd, ook voor iemand die de bibliotheek niet kent.
- **Hint 2 (te schrijven):** Probeer elke uitleg in gedachten uit, stap voor stap. Kun je elke stap doen op het moment dat hij aan de beurt is? En vind je zo altijd het boek dat je zoekt?
- **Ouderzin:** Je kind kiest de duidelijkste uitleg: stappen in een volgorde die altijd werkt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `volgorde` (Pak het boek, zoek de letter, loop naar dat vak.) → Probeer die stappen in die volgorde. Kun je een boek pakken voordat je weet waar het staat?  [nieuw]
  - `geen aanpak` (Loop door de bibliotheek tot je iets leuks ziet.) → Zo vind je misschien wel een boek, maar niet altijd het boek dat je zoekt. Een uitleg moet voor iedereen werken.  [nieuw]
  - `andere fout` (andere fout) → Kun je elke stap doen op het moment dat hij aan de beurt is?  [nieuw]
- Status: hints klaar

## Somtype 40: Je moet # [ding] op alfabetische volgorde zetten. Welke aanpak werkt altijd?

- Sleutel: nrOrigineel **33** · somtypeOrigineel “Je moet # [ding] op alfabetische volgorde zetten. Welke aanpak werkt altijd?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Alfabetische volgorde gaat niet over lengte. Waar kijk je dan wel naar?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-041` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je moet 12 namen op alfabetische volgorde zetten. Welke aanpak werkt altijd?
    - **Opties:** A) Vergelijk alleen de eerste en de laatste naam · B) Zoek steeds de eerste naam en zet die apart · C) Zet de kortste namen vooraan
    - **Antwoord:** Zoek steeds de eerste naam en zet die apart  (controle: n.v.t.)
    - **Fout-hints (Claude):** Zet de kortste namen vooraan → Alfabetische volgorde gaat niet over lengte. Waar kijk je dan wel naar? · Vergelijk alleen de eerste en de laatste naam → Alle namen moeten op hun plek komen. Elke naam moet dus een keer vergeleken worden.
    - **Uitleg (Claude):** Je zoekt telkens de naam die alfabetisch het eerst komt. Die zet je op de volgende plaats in de rij. Zo komen alle namen een keer aan de beurt.

- **Hint 1 (te schrijven):** Alfabetische volgorde gaat over de letters. Een aanpak werkt altijd als elk woord zo een plek krijgt.
- **Hint 2 (te schrijven):** Probeer elke aanpak uit met een paar woorden, bijvoorbeeld kat, aap en boom. Komt bij elke aanpak elk woord op de goede plek in het alfabet?
- **Ouderzin:** Je kind kiest een aanpak om te sorteren die altijd werkt: steeds het woord zoeken dat in het alfabet het eerst komt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `lengte` (Zet de kortste namen vooraan) → Alfabetische volgorde gaat over de letters, niet over hoe lang een woord is. Waar kijk je dan naar?  [nieuw]
  - `twee vergeleken` (Vergelijk alleen de eerste en de laatste naam) → Dan krijgen de woorden daartussen geen plek. Elk woord moet op zijn plek komen.  [nieuw]
  - `andere fout` (andere fout) → Krijgt bij die aanpak elk woord een plek, alleen door naar de letters te kijken?  [nieuw]
- Status: hints klaar

## Somtype 41: Je spaart elke week # euro en wilt # euro hebben. Hoe reken je uit hoeveel weken je moet sparen?

- Sleutel: nrOrigineel **34** · somtypeOrigineel “Je spaart elke week # euro en wilt # euro hebben. Hoe reken je uit hoeveel weken je moet sparen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het aantal weken kan niet groter zijn dan het aantal euro's. Denk aan groepjes van 3 euro.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-042` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je spaart elke week 3 euro en wilt 45 euro hebben. Hoe reken je uit hoeveel weken je moet sparen?
    - **Opties:** A) Deel 45 door 3 · B) Doe 45 keer 3 · C) Trek 3 van 45 af
    - **Antwoord:** Deel 45 door 3  (controle: n.v.t.)
    - **Fout-hints (Claude):** Doe 45 keer 3 → Het aantal weken kan niet groter zijn dan het aantal euro's. Denk aan groepjes van 3 euro. · Trek 3 van 45 af → Je wilt weten hoe vaak 3 euro in 45 euro past. Welke bewerking hoort daarbij?
    - **Uitleg (Claude):** Je zoekt hoe vaak 3 euro in 45 euro past. Dat doe je met delen. 45 gedeeld door 3 is 15 weken.

- **Hint 1 (te schrijven):** Elke week komt er evenveel bij. Na hoeveel weken heb je het hele bedrag?
- **Hint 2 (te schrijven):** Reken elke aanpak uit. Doe de uitkomst keer het bedrag van één week. Bij welke aanpak kom je precies op het bedrag dat je wilt hebben?
- **Ouderzin:** Je kind kiest hoe je uitrekent hoeveel weken sparen nodig is: hoe vaak het weekbedrag in het spaardoel past.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer` (Doe 45 keer 3) → Dan krijg je een getal dat groter is dan het bedrag dat je wilt. Hoe vaak past het bedrag van één week in dat bedrag?  [nieuw]
  - `één week eraf` (Trek 3 van 45 af) → Dan haal je maar één week sparen van het bedrag af. Hoe vaak past het bedrag van één week in het hele bedrag?  [nieuw]
  - `andere fout` (andere fout) → Hoe vaak past het bedrag van één week in het bedrag dat je wilt hebben?  [nieuw]
- Status: hints klaar

## Somtype 42: Je verdeelt een pak sap van # liter over [bakken] van # [ding]. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?

- Sleutel: nrOrigineel **35** · somtypeOrigineel “Je verdeelt een pak sap van # liter over [bakken] van # [ding]. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je rekent nu met twee verschillende eenheden. Maak ze eerst gelijk.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-043` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je verdeelt een pak sap van 1,5 liter over bekers van 250 milliliter. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?
    - **Opties:** A) Deel 1,5 meteen door 250 · B) Reken 1,5 liter om naar 150 milliliter · C) Reken 1,5 liter om naar 1500 milliliter
    - **Antwoord:** Reken 1,5 liter om naar 1500 milliliter  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 1,5 meteen door 250 → Je rekent nu met twee verschillende eenheden. Maak ze eerst gelijk. · Reken 1,5 liter om naar 150 milliliter → Kijk nog eens hoeveel milliliter er in één liter gaan. Dat zijn er meer dan honderd.
    - **Uitleg (Claude):** In 1 liter zitten 1000 milliliter, dus 1,5 liter is 1500 milliliter. Met dezelfde eenheid kun je pas goed delen. Daarna deel je 1500 door 250.

- **Hint 1 (te schrijven):** De ene maat staat in liter, de andere in een kleinere maat. Kun je die meteen met elkaar delen?
- **Hint 2 (te schrijven):** Hoeveel van de kleine maat gaan er in één liter? Reken elke stap na: klopt het omrekenen, en staan daarna allebei de getallen in dezelfde maat?
- **Ouderzin:** Je kind ziet dat je eerst dezelfde maat nodig hebt: liter omrekenen naar de kleine maat.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `direct delen` (Deel 1,5 meteen door 250) → Dan deel je liters door een kleinere maat. Maak eerst van allebei dezelfde maat.  [nieuw]
  - `verkeerd omgerekend` (Reken 1,5 liter om naar 150 milliliter) → Reken het na: hoeveel van de kleine maat gaan er in één liter? Past dit getal daarbij?  [nieuw]
  - `andere fout` (andere fout) → Maak eerst van allebei dezelfde maat. Hoeveel van de kleine maat gaan er in één liter?  [nieuw]
- Status: hints klaar

## Somtype 43: Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?

- Sleutel: nrOrigineel **36** · somtypeOrigineel “Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Denk aan een hek rondom de tuin. Je loopt langs alle vier de zijden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-044` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?
    - **Opties:** A) Tel lengte en breedte op en verdubbel die som. · B) Vermenigvuldig de lengte met de breedte. · C) Tel lengte en breedte op en klaar.
    - **Antwoord:** Tel lengte en breedte op en verdubbel die som.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Vermenigvuldig de lengte met de breedte. → Denk aan een hek rondom de tuin. Je loopt langs alle vier de zijden. · Tel lengte en breedte op en klaar. → Een rechthoek heeft vier zijden. Hoeveel zijden heb je nu geteld?
    - **Uitleg (Claude):** De omtrek is de som van alle vier de zijden. Lengte en breedte komen elk twee keer voor. Dus tel je ze op en verdubbel je die som.

- **Hint 1 (te schrijven):** De omtrek is de lengte rondom: langs alle zijden van de tuin.
- **Hint 2 (te schrijven):** Bedenk een tuin, bijvoorbeeld zes meter lang en vier meter breed. Loop in gedachten rondom en tel alle zijden op. Reken dan elke aanpak uit met die tuin. Welke geeft hetzelfde?
- **Ouderzin:** Je kind kiest hoe je de omtrek uitrekent: alle zijden rondom, dus lengte en breedte samen, twee keer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `oppervlakte` (Vermenigvuldig de lengte met de breedte.) → Lengte keer breedte is de oppervlakte: hoeveel ruimte er in de tuin is. De omtrek is de lengte rondom.  [nieuw]
  - `twee zijden` (Tel lengte en breedte op en klaar.) → Dan heb je maar twee zijden. Een rechthoek heeft er vier: hoeveel zijden mis je nog?  [nieuw]
  - `andere fout` (andere fout) → De omtrek is de lengte rondom. Tel je alle vier de zijden mee?  [nieuw]
- Status: hints klaar

## Somtype 44: Je wilt het gemiddelde van # [ding] weten. Hoe reken je dat uit?

- Sleutel: nrOrigineel **37** · somtypeOrigineel “Je wilt het gemiddelde van # [ding] weten. Hoe reken je dat uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij een gemiddelde verdeel je het totaal eerlijk over alle cijfers. Welke bewerking verdeelt?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-045` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je wilt het gemiddelde van 5 rapportcijfers weten. Hoe reken je dat uit?
    - **Opties:** A) Tel alle cijfers op en tel de som bij 5 op. · B) Zoek het hoogste cijfer en deel dat door 5. · C) Tel alle cijfers op en deel de som door 5.
    - **Antwoord:** Tel alle cijfers op en deel de som door 5.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel alle cijfers op en tel de som bij 5 op. → Bij een gemiddelde verdeel je het totaal eerlijk over alle cijfers. Welke bewerking verdeelt? · Zoek het hoogste cijfer en deel dat door 5. → Bij een gemiddelde doen alle cijfers mee, niet alleen één cijfer.
    - **Uitleg (Claude):** Een gemiddelde vind je door alles samen te nemen en het dan eerlijk te verdelen. Je telt de 5 cijfers op tot een totaal. Dat totaal deel je door het aantal cijfers, dus door 5.

- **Hint 1 (te schrijven):** Een gemiddelde is wat je krijgt als je alles eerlijk verdeelt, zodat elk cijfer even groot wordt.
- **Hint 2 (te schrijven):** Probeer elke aanpak met drie cijfers: zes, zeven en acht. Het gemiddelde daarvan is zeven. Gebruik drie waar de aanpak het aantal cijfers gebruikt. Welke aanpak komt op zeven uit?
- **Ouderzin:** Je kind kiest hoe je een gemiddelde uitrekent: alles optellen en delen door het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij` (Tel alle cijfers op en tel de som bij 5 op.) → Dan wordt het getal alleen maar groter, groter dan elk cijfer. Een gemiddelde ligt tussen het laagste en het hoogste cijfer.  [nieuw]
  - `hoogste` (Zoek het hoogste cijfer en deel dat door 5.) → Dan doet maar één cijfer mee. Bij een gemiddelde tellen alle cijfers mee.  [nieuw]
  - `andere fout` (andere fout) → Bij een gemiddelde tellen alle cijfers mee, en verdeel je het totaal eerlijk.  [nieuw]
- Status: hints klaar

## Somtype 45: Jinte moet # × # [ding]. Welke aanpak is het handigst?

- Sleutel: nrOrigineel **38** · somtypeOrigineel “Jinte moet # × # [ding]. Welke aanpak is het handigst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt vijf keer 2 te veel gerekend, niet één keer. Hoeveel is dat bij elkaar?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-046` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Jinte moet 5 × 98 uitrekenen. Welke aanpak is het handigst?
    - **Opties:** A) 5 × 100 doen en er 2 afhalen · B) 98 vijf keer onder elkaar optellen · C) 5 × 100 doen en er 10 afhalen
    - **Antwoord:** 5 × 100 doen en er 10 afhalen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 × 100 doen en er 2 afhalen → Je hebt vijf keer 2 te veel gerekend, niet één keer. Hoeveel is dat bij elkaar? · 98 vijf keer onder elkaar optellen → Dat mag wel, maar het kost veel stappen. 98 ligt heel dicht bij een rond getal.
    - **Uitleg (Claude):** 98 is 2 minder dan 100. Bij 5 keer reken je dus 5 × 2 = 10 te veel. Daarom haal je 10 van 500 af.

- **Hint 1 (te schrijven):** Het getal ligt dicht bij een rond getal. Met een rond getal reken je makkelijker.
- **Hint 2 (te schrijven):** Reken de som eerst zelf uit. Reken dan elke aanpak uit. Welke komt op hetzelfde uit, en welke gaat het snelst?
- **Ouderzin:** Je kind kiest een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één keer verbeterd` (5 × 100 doen en er 2 afhalen) → Bij elke keer reken je een beetje te veel. Hoe vaak reken je dat te veel? Dat moet er allemaal af, niet maar één keer.  [nieuw]
  - `herhaald optellen` (98 vijf keer onder elkaar optellen) → Dat kan, maar het is niet handig: het kost veel stappen. Ligt het getal dicht bij een rond getal?  [nieuw]
  - `andere fout` (andere fout) → Reken met het ronde getal, en haal daarna af wat je bij alle keren samen te veel nam.  [nieuw]
- Status: hints klaar

## Somtype 46: Kim moet # × # [ding]. Ze doet eerst # × # = # en neemt dan de helft. Klopt deze aanpak?

- Sleutel: nrOrigineel **39** · somtypeOrigineel “Kim moet # × # [ding]. Ze doet eerst # × # = # en neemt dan de helft. Klopt deze aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vijf keer iets is minder dan tien keer iets. Wat doe je dan met de uitkomst van 36 × 10?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-047` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Kim moet 36 × 5 uitrekenen. Ze doet eerst 36 × 10 = 360 en neemt dan de helft. Klopt deze aanpak?
    - **Opties:** A) Nee, ze moet er 10 van afhalen · B) Ja, 5 is de helft van 10 · C) Nee, ze moet 360 verdubbelen
    - **Antwoord:** Ja, 5 is de helft van 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, ze moet 360 verdubbelen → Vijf keer iets is minder dan tien keer iets. Wat doe je dan met de uitkomst van 36 × 10? · Nee, ze moet er 10 van afhalen → Je kijkt naar het verschil tussen 5 en 10 als getal. Kijk liever hoe die twee zich tot elkaar verhouden.
    - **Uitleg (Claude):** Keer 10 gaat heel makkelijk. Omdat 5 de helft van 10 is, halveer je daarna de uitkomst. 360 gedeeld door 2 is 180.

- **Hint 1 (te schrijven):** Kijk of de aanpak van Kim op hetzelfde uitkomt als de som zelf.
- **Hint 2 (te schrijven):** Reken het zelf uit: wat is vijf keer het getal? Reken dan elke aanpak uit: wat Kim deed, en wat de andere antwoorden zeggen. Welke komt op dezelfde uitkomst?
- **Ouderzin:** Je kind controleert een handige aanpak: keer tien en dan de helft is hetzelfde als keer vijf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien eraf` (Nee, ze moet er 10 van afhalen) → Keer tien is twee keer zo groot als keer vijf, niet tien meer. Hoeveel moet er dan af?  [nieuw]
  - `verdubbelen` (Nee, ze moet 360 verdubbelen) → Keer vijf is minder dan keer tien. Wordt de uitkomst dan groter of kleiner?  [nieuw]
  - `andere fout` (andere fout) → Is vijf de helft van tien? Wat betekent dat voor de uitkomst?  [nieuw]
- Status: hints klaar

## Somtype 47: Lars zet # [ding] jam in [bakken] van #. Hij rekent # : # en schrijft # [ding] op. Wat is er mis met zijn aanpak?

- Sleutel: nrOrigineel **40** · somtypeOrigineel “Lars zet # [ding] jam in [bakken] van #. Hij rekent # : # en schrijft # [ding] op. Wat is er mis met zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): rest-vergeten (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken na hoeveel potjes er in 14 volle dozen passen. Blijft er dan nog iets over?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-048` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Lars zet 148 potjes jam in dozen van 10. Hij rekent 148 : 10 en schrijft 14 dozen op. Wat is er mis met zijn aanpak?
    - **Opties:** A) Niets, 14 dozen is precies goed · B) Hij moest 148 × 10 doen · C) Er blijven 8 potjes over, dus er is een extra doos nodig
    - **Antwoord:** Er blijven 8 potjes over, dus er is een extra doos nodig  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 14 dozen is precies goed → Reken na hoeveel potjes er in 14 volle dozen passen. Blijft er dan nog iets over? · Hij moest 148 × 10 doen → Vermenigvuldigen maakt het aantal juist groter. Bij verdelen in gelijke groepen kies je iets anders.
    - **Uitleg (Claude):** In 14 dozen passen 140 potjes. Er blijven dan 8 potjes over en die moeten ook mee. Daarom zijn er 15 dozen nodig.

- **Hint 1 (te schrijven):** Bij een deling in een verhaal kijk je daarna terug in het verhaal: wat betekent de uitkomst?
- **Hint 2 (te schrijven):** Reken het na: hoeveel gaat er in het aantal dat Lars opschreef? Is daarmee alles ingepakt? Toets dan elke uitleg aan die berekening. Welke klopt?
- **Ouderzin:** Je kind kijkt terug in het verhaal: bij inpakken moet alles mee, dus de rest heeft nog een plek nodig.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rest vergeten` (Niets, 14 dozen is precies goed) → Reken het na: hoeveel gaat er in dat aantal? Is daarmee alles ingepakt?  [nieuw]
  - `keer` (Hij moest 148 × 10 doen) → Dan wordt het getal veel groter dan wat er is. Bij verdelen in groepjes past delen. Wat blijft er bij de deling over?  [nieuw]
  - `andere fout` (andere fout) → Wat blijft er bij de deling over, en moet dat ook mee?  [nieuw]
- Status: hints klaar

## Somtype 48: Mees moet # × # [ding]. Hij telt # + # + # + # op. Wat had handiger gekund?

- Sleutel: nrOrigineel **41** · somtypeOrigineel “Mees moet # × # [ding]. Hij telt # + # + # + # op. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vier groepen van 250 is niet hetzelfde als 250 en 4 samen. Kijk nog eens naar het maalteken.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-049` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Mees moet 4 × 250 uitrekenen. Hij telt 250 + 250 + 250 + 250 op. Wat had handiger gekund?
    - **Opties:** A) Eerst 250 + 4 uitrekenen · B) De som onder elkaar zetten met een streep · C) Meteen 4 × 250 vermenigvuldigen
    - **Antwoord:** Meteen 4 × 250 vermenigvuldigen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Eerst 250 + 4 uitrekenen → Vier groepen van 250 is niet hetzelfde als 250 en 4 samen. Kijk nog eens naar het maalteken. · De som onder elkaar zetten met een streep → Onder elkaar zetten kost hier veel tijd. 250 is een mooi getal om mee te vermenigvuldigen.
    - **Uitleg (Claude):** Vier keer hetzelfde getal optellen is precies vermenigvuldigen. Met 4 × 250 ben je in één stap klaar. Dat scheelt tijd en je maakt minder fouten.

- **Hint 1 (te schrijven):** Zoek een aanpak die klopt en die minder stappen kost dan steeds hetzelfde getal optellen.
- **Hint 2 (te schrijven):** Reken elke aanpak uit. Komt die op hetzelfde uit als steeds hetzelfde getal optellen? En welke aanpak die klopt, gaat in de minste stappen?
- **Ouderzin:** Je kind ziet dat steeds hetzelfde getal optellen hetzelfde is als een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus` (Eerst 250 + 4 uitrekenen) → Dan tel je het aantal keer bij het getal op. Steeds hetzelfde getal optellen geeft veel meer dan het getal plus het aantal keer.  [nieuw]
  - `onder elkaar` (De som onder elkaar zetten met een streep) → Dat kan, maar het is niet handig: je telt dan nog steeds alles op. Het kan in één stap.  [nieuw]
  - `andere fout` (andere fout) → Steeds hetzelfde getal optellen: welke som doet dat in één stap?  [nieuw]
- Status: hints klaar

## Somtype 49: Noor moet # × # [ding] en telt acht keer # bij elkaar op. Wat had handiger gekund?

- Sleutel: nrOrigineel **42** · somtypeOrigineel “Noor moet # × # [ding] en telt acht keer # bij elkaar op. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Let op het teken in de som. Optellen en keer doen geven heel andere antwoorden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-050` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Noor moet 25 × 8 uitrekenen en telt acht keer 25 bij elkaar op. Wat had handiger gekund?
    - **Opties:** A) 25 en 8 bij elkaar optellen · B) 25 × 10 doen en er 2 afhalen · C) 25 × 4 doen en dan verdubbelen
    - **Antwoord:** 25 × 4 doen en dan verdubbelen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 25 en 8 bij elkaar optellen → Let op het teken in de som. Optellen en keer doen geven heel andere antwoorden. · 25 × 10 doen en er 2 afhalen → Als je met 10 rekent in plaats van met 8, haal je hele groepen van 25 te veel weg.
    - **Uitleg (Claude):** Je mag een keersom in stappen splitsen. 25 × 4 is 100 en dat verdubbel je tot 200. Dat gaat veel sneller dan acht keer optellen.

- **Hint 1 (te schrijven):** Zoek een aanpak die klopt en die sneller gaat dan steeds hetzelfde getal optellen.
- **Hint 2 (te schrijven):** Reken elke aanpak uit. Komt die op hetzelfde uit als steeds hetzelfde getal optellen? En welke aanpak die klopt, gaat het snelst?
- **Ouderzin:** Je kind kiest een handige aanpak voor een keersom: splitsen in een makkelijke keersom en dan verdubbelen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus` (25 en 8 bij elkaar optellen) → Dan tel je het aantal keer bij het getal op. Steeds hetzelfde getal optellen is een keersom. Komt dit daar in de buurt?  [nieuw]
  - `te veel eraf` (25 × 10 doen en er 2 afhalen) → Met tien keer neem je twee hele keren te veel. Haal je dan twee af, of twee keer het getal?  [nieuw]
  - `andere fout` (andere fout) → Kun je het aantal keer splitsen in een makkelijke keersom?  [nieuw]
- Status: hints klaar

## Somtype 50: Nout heeft # − # [ding] elkaar uitgerekend en kreeg #. Hij schatte vooraf ongeveer #. Wat moet hij nu doen?

- Sleutel: nrOrigineel **43** · somtypeOrigineel “Nout heeft # − # [ding] elkaar uitgerekend en kreeg #. Hij schatte vooraf ongeveer #. Wat moet hij nu doen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): schatting-verkeerd (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een schatting met ronde getallen is meestal betrouwbaar. Reken 800 − 400 nog eens na.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-051` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Nout heeft 802 − 397 onder elkaar uitgerekend en kreeg 505. Hij schatte vooraf ongeveer 400. Wat moet hij nu doen?
    - **Opties:** A) De schatting aanpassen naar 500 · B) Het antwoord 505 gewoon laten staan · C) De som opnieuw uitrekenen, want de schatting past niet
    - **Antwoord:** De som opnieuw uitrekenen, want de schatting past niet  (controle: n.v.t.)
    - **Fout-hints (Claude):** De schatting aanpassen naar 500 → Een schatting met ronde getallen is meestal betrouwbaar. Reken 800 − 400 nog eens na. · Het antwoord 505 gewoon laten staan → Je schatting waarschuwt je juist voor een fout. Negeer dat signaal niet.
    - **Uitleg (Claude):** 800 − 400 is ongeveer 400, dus 505 ligt er ver naast. Zo'n groot verschil wijst op een rekenfout. Het echte antwoord is 405.

- **Hint 1 (te schrijven):** Een schatting met ronde getallen is een controle. Ligt het antwoord dicht bij de schatting?
- **Hint 2 (te schrijven):** Rond allebei de getallen af op honderdtallen: kijk naar de tientallen, vijf of meer gaat naar boven. Reken de schatting zelf na. Hoe ver ligt het antwoord van Nout ervan af? Bekijk elke aanpak: welke hoort bij wat je ziet?
- **Ouderzin:** Je kind gebruikt een schatting als controle: ligt het antwoord ver van de schatting, dan reken je opnieuw.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `schatting aangepast` (De schatting aanpassen naar 500) → Reken de schatting na met ronde getallen. Klopte die? Dan ligt de fout niet in de schatting.  [nieuw]
  - `laten staan` (Het antwoord 505 gewoon laten staan) → Het antwoord ligt ver van de schatting af. Dat is een teken dat er iets mis is gegaan.  [nieuw]
  - `andere fout` (andere fout) → Ligt het antwoord dicht bij de schatting? Zo niet, waar zit dan de fout?  [nieuw]
- Status: hints klaar

## Somtype 51: Op de fietstocht rijdt Tess # km. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet klopt?

- Sleutel: nrOrigineel **44** · somtypeOrigineel “Op de fietstocht rijdt Tess # km. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “De komma verplaatsen is niet hetzelfde als omrekenen. Hoeveel meter zit er in 1 kilometer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-060` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Op de fietstocht rijdt Tess 3,2 km. Ze schrijft op dat dit 32 meter is. Hoe merk je dat dit niet klopt?
    - **Opties:** A) Het moet 320 meter zijn · B) 1 km is al 1000 meter, dus het moeten er veel meer zijn · C) Het klopt, je haalt gewoon de komma weg
    - **Antwoord:** 1 km is al 1000 meter, dus het moeten er veel meer zijn  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het klopt, je haalt gewoon de komma weg → De komma verplaatsen is niet hetzelfde als omrekenen. Hoeveel meter zit er in 1 kilometer? · Het moet 320 meter zijn → Je bent één stap te vroeg gestopt. Reken eerst uit hoeveel meter 3 km is.
    - **Uitleg (Claude):** Eén kilometer is 1000 meter. 3,2 km is dus 3200 meter. Met 32 meter kom je nog niet eens de straat uit.

- **Hint 1 (te schrijven):** Je controleert een omrekening van kilometer naar meter. Past het getal in meters bij de afstand?
- **Hint 2 (te schrijven):** Hoeveel meter is één kilometer? Reken uit hoeveel meter de tocht dan ongeveer is. Toets elke uitleg aan dat getal: welke klopt?
- **Ouderzin:** Je kind controleert een omrekening met een bekend getal: één kilometer is duizend meter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één stap` (Het moet 320 meter zijn) → Reken het na: één kilometer is al duizend meter. Is dit dan genoeg voor de hele tocht?  [nieuw]
  - `komma weg` (Het klopt, je haalt gewoon de komma weg) → De komma weghalen is geen omrekenen. Hoeveel meter gaan er in één kilometer?  [nieuw]
  - `andere fout` (andere fout) → Eén kilometer is al duizend meter. Hoeveel meter is de tocht dan ongeveer?  [nieuw]
- Status: hints klaar

## Somtype 52: Roos rekent # × # uit door # × # en # × # [ding] te doen. Ze schrijft alleen # op. Wat ging er mis?

- Sleutel: nrOrigineel **45** · somtypeOrigineel “Roos rekent # × # uit door # × # en # × # [ding] te doen. Ze schrijft alleen # op. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Splitsen is juist een slimme aanpak. Kijk nog eens of ze alle stukjes heeft gebruikt.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-114` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Roos rekent 7 × 24 uit door 7 × 20 en 7 × 4 apart te doen. Ze schrijft alleen 140 op. Wat ging er mis?
    - **Opties:** A) Ze moest 140 en 24 optellen · B) Ze vergat 28 erbij op te tellen · C) Ze had niet mogen splitsen
    - **Antwoord:** Ze vergat 28 erbij op te tellen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze had niet mogen splitsen → Splitsen is juist een slimme aanpak. Kijk nog eens of ze alle stukjes heeft gebruikt. · Ze moest 140 en 24 optellen → Het tweede stukje was 7 × 4, niet 24. Reken dat stukje eerst uit.
    - **Uitleg (Claude):** Bij splitsen reken je beide delen uit en tel je ze op. 140 en 28 samen is 168. Roos stopte te vroeg met haar aanpak.

- **Hint 1 (te schrijven):** Bij splitsen reken je elk stuk apart uit. Wat doe je daarna met de stukken?
- **Hint 2 (te schrijven):** Reken het zelf uit: wat zijn de twee stukken, en wat is de hele keersom? Vergelijk dat met wat Roos opschreef. Toets dan elke uitleg: welke klopt?
- **Ouderzin:** Je kind ziet dat je bij splitsen alle stukken weer bij elkaar optelt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de som` (Ze moest 140 en 24 optellen) → Dan tel je een getal uit de som erbij, niet de uitkomst van het kleine stuk. Hoeveel is het kleine stuk echt?  [nieuw]
  - `niet splitsen` (Ze had niet mogen splitsen) → Splitsen is juist een handige aanpak. Heeft Roos alle stukken gebruikt?  [nieuw]
  - `andere fout` (andere fout) → Heeft Roos alle stukken van de keersom bij elkaar opgeteld?  [nieuw]
- Status: hints klaar

## Somtype 53: Sam rekent # − # uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?

- Sleutel: nrOrigineel **46** · somtypeOrigineel “Sam rekent # − # uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk nog eens welk teken er tussen de getallen staat.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-115` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Sam rekent 1000 − 998 uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?
    - **Opties:** A) 1000 en 998 bij elkaar optellen · B) Eerst 900 eraf en dan 98 erbij · C) Doortellen van 998 naar 1000
    - **Antwoord:** Doortellen van 998 naar 1000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1000 en 998 bij elkaar optellen → Kijk nog eens welk teken er tussen de getallen staat. · Eerst 900 eraf en dan 98 erbij → Als je een deel van een aftreksom afhaalt, moet je het andere deel er ook afhalen.
    - **Uitleg (Claude):** De getallen liggen heel dicht bij elkaar. Vanaf 998 tel je maar 2 stapjes door tot 1000. Onder elkaar rekenen is dan onnodig werk.

- **Hint 1 (te schrijven):** Zoek een aanpak die klopt en die zonder lenen kan.
- **Hint 2 (te schrijven):** Reken elke aanpak uit en vergelijk de uitkomsten. Welke aanpak geeft het verschil tussen de twee getallen, en kost de minste stappen?
- **Ouderzin:** Je kind ziet dat je bij twee getallen die dicht bij elkaar liggen, het verschil handig vindt door door te tellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (1000 en 998 bij elkaar optellen) → Bij elkaar optellen geeft geen verschil. Kijk welk teken er tussen de getallen staat.  [nieuw]
  - `stuk erbij` (Eerst 900 eraf en dan 98 erbij) → Als je een getal in stukken afhaalt, moeten alle stukken eraf. Gaat er bij deze aanpak een stuk bij?  [nieuw]
  - `andere fout` (andere fout) → Liggen de getallen dicht bij elkaar? Hoeveel moet je dan doortellen?  [nieuw]
- Status: hints klaar

## Somtype 54: Sanne rekent # + # uit door eerst # + # te doen en er daarna # af te halen. Klopt deze aanpak?

- Sleutel: nrOrigineel **47** · somtypeOrigineel “Sanne rekent # + # uit door eerst # + # te doen en er daarna # af te halen. Klopt deze aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Ze heeft eerst een groter getal gebruikt dan 198. Wat doe je dan achteraf met dat verschil?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-116` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Sanne rekent 198 + 56 uit door eerst 200 + 56 te doen en er daarna 2 af te halen. Klopt deze aanpak?
    - **Opties:** A) Ja, dat is een handige manier · B) Nee, ze moet er 2 bij optellen · C) Nee, je mag alleen onder elkaar rekenen
    - **Antwoord:** Ja, dat is een handige manier  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, ze moet er 2 bij optellen → Ze heeft eerst een groter getal gebruikt dan 198. Wat doe je dan achteraf met dat verschil? · Nee, je mag alleen onder elkaar rekenen → Een som onder elkaar mag altijd, maar soms kan het slimmer. Denk aan mooie ronde getallen.
    - **Uitleg (Claude):** 198 ligt vlak bij 200, dus rekenen met 200 gaat makkelijk. Omdat je 2 te veel gebruikte, haal je er achteraf 2 af. Zo krijg je hetzelfde antwoord, maar sneller.

- **Hint 1 (te schrijven):** Kijk of de aanpak van Sanne op hetzelfde uitkomt als de som zelf.
- **Hint 2 (te schrijven):** Reken de som zelf uit, en reken ook na wat Sanne doet. Komt Sanne daarop uit? Kijk dan welke uitleg past bij wat je ziet.
- **Ouderzin:** Je kind controleert een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij in plaats van eraf` (Nee, ze moet er 2 bij optellen) → Sanne rekende met een getal dat iets te groot is. Moet dat stukje er dan bij, of eraf?  [nieuw]
  - `alleen onder elkaar` (Nee, je mag alleen onder elkaar rekenen) → Onder elkaar rekenen kan, maar je mag ook een handige aanpak kiezen. Klopt de uitkomst van Sanne?  [nieuw]
  - `andere fout` (andere fout) → Komt de aanpak van Sanne op hetzelfde uit als de som zelf?  [nieuw]
- Status: hints klaar

## Somtype 55: Tim rekent # + # uit met een staartsom onder elkaar. Wat is een handigere aanpak?

- Sleutel: nrOrigineel **48** · somtypeOrigineel “Tim rekent # + # uit met een staartsom onder elkaar. Wat is een handigere aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): een-ernaast (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je deed er 1 te veel bij. Bedenk wat je moet doen als je eerst een te groot getal pakt.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-117` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Tim rekent 99 + 47 uit met een staartsom onder elkaar. Wat is een handigere aanpak?
    - **Opties:** A) Eerst 100 erbij, dan 1 eraf · B) Eerst 100 erbij, dan 1 erbij · C) Eerst 90 erbij, dan 9 eraf
    - **Antwoord:** Eerst 100 erbij, dan 1 eraf  (controle: n.v.t.)
    - **Fout-hints (Claude):** Eerst 100 erbij, dan 1 erbij → Je deed er 1 te veel bij. Bedenk wat je moet doen als je eerst een te groot getal pakt. · Eerst 90 erbij, dan 9 eraf → Kijk nog eens goed hoe dicht 99 bij een rond honderdtal ligt.
    - **Uitleg (Claude):** 99 ligt vlak bij 100. Je telt er eerst 100 bij op en haalt daarna de 1 die je te veel nam er weer af. Zo hoef je niet onder elkaar te rekenen.

- **Hint 1 (te schrijven):** Het getal ligt dicht bij een rond getal. Met een rond getal reken je makkelijker.
- **Hint 2 (te schrijven):** Reken de som zelf uit, en reken daarna elke aanpak uit. Welke aanpak komt op hetzelfde uit?
- **Ouderzin:** Je kind kiest een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te veel erbij` (Eerst 100 erbij, dan 1 erbij) → Met het ronde getal komt er al iets te veel bij. Moet dat stukje er dan nog bij, of eraf?  [nieuw]
  - `ander rond getal` (Eerst 90 erbij, dan 9 eraf) → Reken het na: komt deze aanpak op hetzelfde uit als de som? Bij een kleiner rond getal tel je te weinig op. Moet het stukje er dan bij of eraf?  [nieuw]
  - `andere fout` (andere fout) → Neem een rond getal, en verbeter daarna wat je te veel of te weinig nam.  [nieuw]
- Status: hints klaar

## Somtype 56: Voor een uitje gaan # [ding] mee. In een busje passen # [ding]. Lisa rekent # : # en schrijft # [ding] op. Wat is er mis met haar aanpak?

- Sleutel: nrOrigineel **49** · somtypeOrigineel “Voor een uitje gaan # [ding] mee. In een busje passen # [ding]. Lisa rekent # : # en schrijft # [ding] op. Wat is er mis met haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je verdeelt kinderen over busjes. Welke bewerking hoort bij verdelen?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-118` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Voor een uitje gaan 50 kinderen mee. In een busje passen 12 kinderen. Lisa rekent 50 : 12 en schrijft 4 busjes op. Wat is er mis met haar aanpak?
    - **Opties:** A) Ze vergat de 2 kinderen die overblijven · B) Ze had 50 × 12 moeten doen · C) Er zijn 6 busjes nodig
    - **Antwoord:** Ze vergat de 2 kinderen die overblijven  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze had 50 × 12 moeten doen → Je verdeelt kinderen over busjes. Welke bewerking hoort bij verdelen? · Er zijn 6 busjes nodig → Reken na hoeveel kinderen er in 5 busjes passen. Zijn dat er genoeg?
    - **Uitleg (Claude):** In 4 busjes passen 48 kinderen. Er blijven er 2 over en die moeten ook mee. Daarom is er nog een extra busje nodig.

- **Hint 1 (te schrijven):** Bij een deling in een verhaal kijk je daarna terug in het verhaal: wat betekent de uitkomst?
- **Hint 2 (te schrijven):** Reken het na: hoeveel passen er in het aantal dat Lisa opschreef? Kan iedereen dan mee? Toets dan elke uitleg aan die berekening. Welke klopt?
- **Ouderzin:** Je kind kijkt terug in het verhaal: iedereen moet mee, dus wie overblijft heeft nog een plek nodig.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer` (Ze had 50 × 12 moeten doen) → Dan wordt het getal veel groter dan het aantal dat meegaat. Bij verdelen in groepjes past delen. Wat blijft er bij de deling over?  [nieuw]
  - `één te veel` (Er zijn 6 busjes nodig) → Reken het na: kan iedereen al mee met één minder dan dit aantal?  [nieuw]
  - `andere fout` (andere fout) → Wat blijft er bij de deling over, en moet dat ook mee?  [nieuw]
- Status: hints klaar

## Somtype 57: Yara loopt # km naar school. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet kan?

- Sleutel: nrOrigineel **50** · somtypeOrigineel “Yara loopt # km naar school. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet kan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een komma weghalen is niet hetzelfde als omrekenen. Kijk hoeveel meter er in 1 kilometer gaan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-119` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Yara loopt 2,5 km naar school. Ze schrijft op dat dit 250 meter is. Hoe merk je dat dit niet kan?
    - **Opties:** A) 1 km is 1000 meter, dus het zijn er meer · B) Het klopt, want je zet de komma weg · C) Het moet 25 meter zijn
    - **Antwoord:** 1 km is 1000 meter, dus het zijn er meer  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het klopt, want je zet de komma weg → Een komma weghalen is niet hetzelfde als omrekenen. Kijk hoeveel meter er in 1 kilometer gaan. · Het moet 25 meter zijn → 25 meter is korter dan een schoolplein. Vergelijk dat eens met 2,5 kilometer lopen.
    - **Uitleg (Claude):** In 1 kilometer gaan 1000 meter. 2,5 × 1000 is 2500 meter. Bij omrekenen let je altijd op de juiste stap.

- **Hint 1 (te schrijven):** Je controleert een omrekening van kilometer naar meter. Past het getal in meters bij de afstand?
- **Hint 2 (te schrijven):** Hoeveel meter is één kilometer? Reken uit hoeveel meter de weg naar school dan ongeveer is. Toets elke uitleg aan dat getal: welke klopt?
- **Ouderzin:** Je kind controleert een omrekening met een bekend getal: één kilometer is duizend meter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma weg` (Het klopt, want je zet de komma weg) → De komma weghalen is geen omrekenen. Hoeveel meter gaan er in één kilometer?  [nieuw]
  - `nog kleiner` (Het moet 25 meter zijn) → Dat is nog minder. Een kilometer is duizend meter: worden het in meters meer of minder?  [nieuw]
  - `andere fout` (andere fout) → Eén kilometer is al duizend meter. Hoeveel meter is de weg naar school dan ongeveer?  [nieuw]
- Status: hints klaar
