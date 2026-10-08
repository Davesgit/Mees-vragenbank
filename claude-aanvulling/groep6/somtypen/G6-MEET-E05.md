# G6-MEET-E05 — Kilo en gram vergelijken en omrekenen

Onze omschrijving: Gewicht: kg↔g vergelijken/ordenen/schatten · in onze bank: 8 items

Claude-vragen gemapt: **44** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # kg = □ g

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# kg = □ g” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M13 (31) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (43), getal-overgenomen (19)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E05-claude-bank-032` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 11 kg = □ g
    - **Antwoord:** 11.000  (controle: ok)
    - **Fout-hints (Claude):** 33 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 110.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E05-claude-bank-029` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 27 kg = □ g
    - **Antwoord:** 27.000  (controle: ok)
    - **Fout-hints (Claude):** 81 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 27 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén kilogram (kg) is duizend gram (g). Een gram is kleiner dan een kilogram, dus het getal wordt groter.
- **Hint 2 (te schrijven):** Doe het aantal kilogram keer duizend: schrijf er drie nullen achter.
- **Ouderzin:** Je kind rekent gewichtsmaten om: van kilogram naar gram (keer duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Eén kilogram is duizend gram: doe keer duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Eén kilogram is duizend gram: doe keer duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Heb je helemaal omgerekend naar gram? Eén kilogram is duizend gram: doe keer duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Eén kilogram is duizend gram: doe keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilogram (kg) is duizend gram (g). Doe het aantal kilogram keer duizend.  [nieuw]
- Status: hints klaar

## Somtype 2: # g = □ kg

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# g = □ kg” (koppeling: claudeId)
- Items: **9** · Claude-doelen: M13 (9) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 9 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (11), getal-overgenomen (7)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E05-claude-bank-005` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 20.000 g = □ kg
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E05-claude-bank-008` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 70.000 g = □ kg
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 70.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén kilogram (kg) is duizend gram (g). Een kilogram is groter dan een gram, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal gram door duizend: haal er drie nullen af.
- **Ouderzin:** Je kind rekent gewichtsmaten om: van gram naar kilogram (gedeeld door duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Duizend gram is één kilogram: deel door duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar kilogram? Duizend gram is één kilogram: deel door duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Duizend gram is één kilogram: deel door duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Duizend gram is één kilogram: deel door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilogram (kg) is duizend gram (g). Deel het aantal gram door duizend.  [nieuw]
- Status: hints klaar

## Somtype 3: Een pakket weegt # kg, een ander # kg. Hoeveel kg wegen ze samen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een pakket weegt # kg, een ander # kg. Hoeveel kg wegen ze samen?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B12 (4) · regel: G6-K04-meetgetal
- Getallenruimte: kommagetallen (2 cijfers achter de komma) · type: kale
- Uit de G5-park: 4 items
- Denkfouten (Claude): kommagetal-als-geheel (5), onthouden-vergeten (4), tiental-ernaast (4)
- Verschillende Claude-fout-hints: 5 (meest: “Alleen als de tienden samen boven de 10 komen, gaat er een hele bij.”)
- Voorbeelden:
  - `G6-MEET-E05-claude-bank-041` (Claude B12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 1,39 kg, een ander 5,2 kg. Hoeveel kg wegen ze samen?
    - **Antwoord:** 6,59  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1,91 → 5,2 is 5,20: zet de komma's recht onder elkaar, niet de laatste cijfers. · 7,59 → Alleen als de tienden samen boven de 10 komen, gaat er een hele bij. · 6,49 → Tel de tienden nog eens na.
    - **Uitleg (Claude):** Zet de komma's onder elkaar: 1,39 + 5,20. Tel de honderdsten, tienden en helen apart, met onthouden als het nodig is. Samen 6,59.
  - `G6-MEET-E05-claude-bank-044` (Claude B12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 8,05 kg, een ander 6,6 kg. Hoeveel kg wegen ze samen?
    - **Antwoord:** 14,65  (controle: n.v.t.)
    - **Fout-hints (Claude):** 8,71 → 6,6 is 6,60: zet de komma's recht onder elkaar, niet de laatste cijfers. · 15,65 → Alleen als de tienden samen boven de 10 komen, gaat er een hele bij. · 14,55 → Tel de tienden nog eens na.
    - **Uitleg (Claude):** Zet de komma's onder elkaar: 8,05 + 6,60. Tel de honderdsten, tienden en helen apart, met onthouden als het nodig is. Samen 14,65.

- **Hint 1 (te schrijven):** Zet de komma's recht onder elkaar. Heeft één getal minder cijfers achter de komma? Schrijf er dan een nul achter.
- **Hint 2 (te schrijven):** Tel op van rechts naar links: eerst de honderdsten, dan de tienden, dan de hele kilogrammen. Komt een kolom op tien of meer? Dan gaat er één mee naar links.
- **Ouderzin:** Je kind telt twee gewichten met een komma op: de komma's recht onder elkaar.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rechts tegen elkaar` (Claudes sleutel: kommagetal-als-geheel) → Je hebt de getallen rechts tegen elkaar gezet. Zet de komma's recht onder elkaar. Schrijf een nul achter het getal met minder cijfers achter de komma.  [Claude, taalfix]
  - `één te veel` (fout = antwoord + 1,0) → Dat is één kilogram te veel. Tel de hele kilogrammen nog eens na. Er gaat alleen één mee als de tienden samen op tien of meer komen, en dan maar één keer.  [nieuw]
  - `een tiende te weinig` (fout = antwoord − 0,1) → Bijna! Dat is een tiende te weinig. Tel de tienden nog eens na.  [nieuw]
  - `een tiende te veel` (fout = antwoord + 0,1) → Bijna! Dat is een tiende te veel. Tel de tienden nog eens na. Gaat er alleen één mee als de honderdsten samen op tien of meer komen?  [nieuw]
  - `andere fout` (andere fout) → Zet de komma's recht onder elkaar en schrijf zo nodig een nul erachter. Tel op van rechts naar links en zet de komma in je antwoord recht eronder.  [nieuw]
- Status: hints klaar
