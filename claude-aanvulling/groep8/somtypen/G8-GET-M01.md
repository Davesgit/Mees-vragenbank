# G8-GET-M01 — Miljoenen en miljarden, ook in woorden

Onze omschrijving: Miljoen/miljard; grote getallen in woorden (1,4 miljoen) · in onze bank: 8 items

Claude-vragen gemapt: **12** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] leven # [ding]. Hoeveel is de # in dit getal waard?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In [plek] leven # [ding]. Hoeveel is de # in dit getal waard?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: C22 (5) · regel: G8-P00-park-G7
- Getallenruimte: 0–2.242.000, 0–2.873.000, 0–3.602.000, 0–8.601.000, 0–9.567.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (10)
- Verschillende Claude-fout-hints: 5 (meest: “Een nul te veel. Een miljoen heeft zes nullen.”)
- Voorbeelden:
  - `G8-GET-M01-claude-bank-005` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de vallei leven 2.873.000 insecten. Hoeveel is de 2 in dit getal waard?
    - **Antwoord:** 2.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 200.000 → Tel de cijfers rechts van de 2: zes. Dus zes nullen. · 20.000.000 → Een nul te veel. Een miljoen heeft zes nullen.
    - **Uitleg (Claude):** 2.873.000 lees je als 2 miljoen 873.000. De 2 staat op de plek van de miljoenen: 2.000.000.
  - `G8-GET-M01-claude-bank-001` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de vallei leven 9.567.000 insecten. Hoeveel is de 9 in dit getal waard?
    - **Antwoord:** 9.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 900.000 → Tel de cijfers rechts van de 9: zes. Dus zes nullen. · 90.000.000 → Een nul te veel. Een miljoen heeft zes nullen.
    - **Uitleg (Claude):** 9.567.000 lees je als 9 miljoen 567.000. De 9 staat op de plek van de miljoenen: 9.000.000.

- **Hint 1 (te schrijven):** Hoeveel een cijfer waard is, hangt af van de plek in het getal: eenheden, tientallen, honderdtallen, enzovoort.
- **Hint 2 (te schrijven):** Tel hoeveel cijfers er na dat cijfer komen. Schrijf het cijfer op met evenveel nullen erachter.
- **Ouderzin:** Je kind zoekt wat één cijfer in een groot getal waard is: dat cijfer met een nul voor elke plek die erna komt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt wat dat ene cijfer waard is, op de plek waar het staat.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig: er mist een nul. Tel nog eens hoeveel cijfers er na dat cijfer komen.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel: er staat een nul te veel. Tel nog eens hoeveel cijfers er na dat cijfer komen.  [nieuw]
  - `andere fout` (andere fout) → Tel hoeveel cijfers er na dat cijfer komen. Evenveel nullen komen erachter.  [nieuw]
- Status: hints klaar

## Somtype 2: In een land wonen # miljoen mensen. Schrijf dat als getal.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In een land wonen # [ding] mensen. Schrijf dat als getal.” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C22 (3) · regel: G8-P00-park-G7
- Getallenruimte: 0–2.000.000, 0–6.000.000, 0–7.000.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (6)
- Verschillende Claude-fout-hints: 2 (meest: “Een miljoen heeft zes nullen. Tel ze na.”)
- Voorbeelden:
  - `G8-GET-M01-claude-bank-007` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In een land wonen 6 miljoen mensen. Schrijf dat als getal.
    - **Antwoord:** 6.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 600.000 → Een miljoen heeft zes nullen. Tel ze na. · 6000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 6 miljoen is 6.000.000.
  - `G8-GET-M01-claude-bank-006` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In een land wonen 2 miljoen mensen. Schrijf dat als getal.
    - **Antwoord:** 2.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 200.000 → Een miljoen heeft zes nullen. Tel ze na. · 2000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 2 miljoen is 2.000.000.

- **Hint 1 (te schrijven):** Een miljoen is duizend keer duizend.
- **Hint 2 (te schrijven):** Een miljoen heeft zes nullen. Schrijf het getal uit de vraag op, en zet er zes nullen achter.
- **Ouderzin:** Je kind schrijft een aantal miljoen als getal: het getal met zes nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Er staat miljoen achter: hoeveel nullen horen daarbij?  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig: er mist een nul. Een miljoen heeft zes nullen.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel: er staat een nul te veel. Een miljoen heeft zes nullen.  [nieuw]
  - `duizend keer te weinig` (Claudes sleutel: nul-fout-tientallen) → Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een miljoen is duizend keer duizend: dat zijn zes nullen. Hoeveel nullen heeft jouw getal?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een land wonen # [ding] mensen. Schrijf dat als getal.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: [wie] heeft # miljoen stickers verzameld. Schrijf dat als getal.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[wie] heeft # [ding] stickers verzameld. Schrijf dat als getal.” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C22 (2) · regel: G8-P00-park-G7
- Getallenruimte: 0–2.000.000, 0–6.000.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Een miljoen heeft zes nullen. Tel ze na.”)
- Voorbeelden:
  - `G8-GET-M01-claude-bank-011` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind heeft 6 miljoen stickers verzameld. Schrijf dat als getal.
    - **Antwoord:** 6.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 600.000 → Een miljoen heeft zes nullen. Tel ze na. · 6000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 6 miljoen is 6.000.000.
  - `G8-GET-M01-claude-bank-010` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind heeft 2 miljoen stickers verzameld. Schrijf dat als getal.
    - **Antwoord:** 2.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 200.000 → Een miljoen heeft zes nullen. Tel ze na. · 2000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 2 miljoen is 2.000.000.

- **Hint 1 (te schrijven):** Een miljoen is duizend keer duizend.
- **Hint 2 (te schrijven):** Een miljoen heeft zes nullen. Schrijf het getal uit de vraag op, en zet er zes nullen achter.
- **Ouderzin:** Je kind schrijft een aantal miljoen als getal: het getal met zes nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Er staat miljoen achter: hoeveel nullen horen daarbij?  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig: er mist een nul. Een miljoen heeft zes nullen.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel: er staat een nul te veel. Een miljoen heeft zes nullen.  [nieuw]
  - `duizend keer te weinig` (Claudes sleutel: nul-fout-tientallen) → Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een miljoen is duizend keer duizend: dat zijn zes nullen. Hoeveel nullen heeft jouw getal?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] heeft # [ding] stickers verzameld. Schrijf dat als getal.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: [wie] heeft # miljoen knikkers verzameld. Schrijf dat als getal.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[wie] heeft # [ding] knikkers verzameld. Schrijf dat als getal.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C22 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–3.000.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een miljoen heeft zes nullen. Tel ze na.”)
- Voorbeelden:
  - `G8-GET-M01-claude-bank-009` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind heeft 3 miljoen knikkers verzameld. Schrijf dat als getal.
    - **Antwoord:** 3.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 300.000 → Een miljoen heeft zes nullen. Tel ze na. · 3000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 3 miljoen is 3.000.000.

- **Hint 1 (te schrijven):** Een miljoen is duizend keer duizend.
- **Hint 2 (te schrijven):** Een miljoen heeft zes nullen. Schrijf het getal uit de vraag op, en zet er zes nullen achter.
- **Ouderzin:** Je kind schrijft een aantal miljoen als getal: het getal met zes nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Er staat miljoen achter: hoeveel nullen horen daarbij?  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig: er mist een nul. Een miljoen heeft zes nullen.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel: er staat een nul te veel. Een miljoen heeft zes nullen.  [nieuw]
  - `duizend keer te weinig` (Claudes sleutel: nul-fout-tientallen) → Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een miljoen is duizend keer duizend: dat zijn zes nullen. Hoeveel nullen heeft jouw getal?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] heeft # [ding] knikkers verzameld. Schrijf dat als getal.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 5: [wie] heeft # miljoen truien verzameld. Schrijf dat als getal.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[wie] heeft # [ding] truien verzameld. Schrijf dat als getal.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C22 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–7.000.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een miljoen heeft zes nullen. Tel ze na.”)
- Voorbeelden:
  - `G8-GET-M01-claude-bank-012` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind heeft 7 miljoen truien verzameld. Schrijf dat als getal.
    - **Antwoord:** 7.000.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 700.000 → Een miljoen heeft zes nullen. Tel ze na. · 7000 → Dat is duizend. Een miljoen is duizend keer duizend.
    - **Uitleg (Claude):** Een miljoen is 1.000.000: een 1 met zes nullen. 7 miljoen is 7.000.000.

- **Hint 1 (te schrijven):** Een miljoen is duizend keer duizend.
- **Hint 2 (te schrijven):** Een miljoen heeft zes nullen. Schrijf het getal uit de vraag op, en zet er zes nullen achter.
- **Ouderzin:** Je kind schrijft een aantal miljoen als getal: het getal met zes nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Er staat miljoen achter: hoeveel nullen horen daarbij?  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig: er mist een nul. Een miljoen heeft zes nullen.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel: er staat een nul te veel. Een miljoen heeft zes nullen.  [nieuw]
  - `duizend keer te weinig` (Claudes sleutel: nul-fout-tientallen) → Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een miljoen is duizend keer duizend: dat zijn zes nullen. Hoeveel nullen heeft jouw getal?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] heeft # [ding] truien verzameld. Schrijf dat als getal.'. Nakijken of ze nog passen.
- Status: hints klaar
