# G7-MEET-02 — Oppervlakte berekenen

Onze omschrijving: Oppervlakte · in onze bank: 8 items

Claude-vragen gemapt: **51** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # m en een hoogte van # m. Wat is de oppervlakte in m²?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # m en een hoogte van # m. Wat is de oppervlakte in m²?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: M21 (32) · regel: D-DUBBEL-MATEN, D-DRIEHOEK-G7-FIX, D-DRIEHOEK-G7
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (32), omtrek-oppervlakte-verwisseld (26), verkeerde-bewerking (26), deel-vergeten-bij-splitsen (12)
- Verschillende Claude-fout-hints: 6 (meest: “Dat is de oppervlakte van de rechthoek eromheen. Een driehoek is de helft: deel door 2.”)
- Voorbeelden:
  - `G7-MEET-02-claude-bank-029` (Claude M21, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een driehoekig stuk grond op het erf heeft een basis van 7 m en een hoogte van 10 m. Wat is de oppervlakte in m²?
    - **Tekening:** `{"soort": "driehoek-in-rechthoek", "basis": 7, "hoogte": 10, "eenheid": "m", "hoogteStippellijn": true, "arcering": "driehoek", "label": "de helft"}`
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** 70 → Dat is de hele rechthoek. Een driehoek is de helft. · 17 → Oppervlakte is keer, niet plus. · 17,5 → Eén keer delen door 2 is genoeg.
    - **Uitleg (Claude):** Oppervlakte driehoek = basis × hoogte : 2 = 6 × 3 : 2 = 18 : 2 = 9 m².
  - `G7-MEET-02-claude-bank-019` (Claude M21, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een driehoekig stuk grond in de speeltuin heeft een basis van 8 m en een hoogte van 5 m. Wat is de oppervlakte in m²?
    - **Tekening:** `{"soort": "driehoek-in-rechthoek", "basis": 8, "hoogte": 5, "eenheid": "m", "hoogteStippellijn": true, "arcering": "driehoek", "label": "de helft"}`
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 40 → Dat is de oppervlakte van de rechthoek eromheen. Een driehoek is de helft: deel door 2. · 13 → Oppervlakte is vermenigvuldigen: basis × hoogte, en dan delen door 2. · 42 → Delen door 2, niet optellen.
    - **Uitleg (Claude):** Oppervlakte driehoek = basis × hoogte : 2 = 8 × 5 : 2 = 40 : 2 = 20 m².

- **Hint 1 (te schrijven):** Een driehoek is de helft van een rechthoek met dezelfde basis en hoogte. De oppervlakte reken je in m² (vierkante meter).
- **Hint 2 (te schrijven):** Reken eerst de rechthoek uit: basis keer hoogte. Neem daarvan de helft. Dat is de oppervlakte van de driehoek.
- **Ouderzin:** Je kind rekent de oppervlakte van een driehoek uit: basis keer hoogte, en daarvan de helft (in m²).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rechthoek niet gehalveerd` (fout = getal1 × getal2) → Dat is de hele rechthoek. Hoeveel is de driehoek daarvan?  [nieuw]
  - `basis en hoogte opgeteld` (fout = getal1 + getal2) → Heb je de basis en de hoogte opgeteld? Oppervlakte reken je met keer.  [nieuw]
  - `twee keer gehalveerd` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je twee keer door twee gedeeld?  [Claude, taalfix]
  - `twee erbij in plaats van halveren` (Claudes sleutel: verkeerde-bewerking) → Heb je er twee bij opgeteld in plaats van door twee te delen?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken basis keer hoogte en neem daarvan de helft.  [nieuw]
- Status: hints klaar

## Somtype 2: Een L-vormige tuin bestaat uit een rechthoek van # bij # meter en een rechthoek van # bij # meter. Hoeveel m² is de tuin?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een L-vormig hok bestaat uit een rechthoek van # bij # meter en een rechthoek van # bij # meter. Hoeveel m² is het hok?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M24 (8) · regel: G8-M24-samengesteld
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (8), omtrek-oppervlakte-verwisseld (8), optellen-ipv-vermenigvuldigen (8)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is één rechthoek. De andere hoort er ook bij.”)
- Voorbeelden:
  - `G7-MEET-02-claude-bank-terug-001` (Claude M24, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een L-vormige tuin bestaat uit een rechthoek van 6 bij 5 meter en een rechthoek van 2 bij 4 meter. Hoeveel m² is de tuin?
    - **Antwoord:** 38  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 → Dat is één rechthoek. De andere hoort er ook bij. · 72 → Een L-vorm is geen grote rechthoek. Reken de twee delen apart en tel ze op. · 17 → Oppervlakte is lengte keer breedte, per rechthoek.
    - **Uitleg (Claude):** Knip de figuur in twee rechthoeken. 6 × 5 = 30 m² en 2 × 4 = 8 m². Samen 38 m².
  - `G7-MEET-02-claude-bank-terug-005` (Claude M24, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een L-vormige tuin bestaat uit een rechthoek van 7 bij 6 meter en een rechthoek van 2 bij 2 meter. Hoeveel m² is de tuin?
    - **Antwoord:** 46  (controle: n.v.t.)
    - **Fout-hints (Claude):** 42 → Dat is één rechthoek. De andere hoort er ook bij. · 72 → Een L-vorm is geen grote rechthoek. Reken de twee delen apart en tel ze op. · 17 → Oppervlakte is lengte keer breedte, per rechthoek.
    - **Uitleg (Claude):** Knip de figuur in twee rechthoeken. 7 × 6 = 42 m² en 2 × 2 = 4 m². Samen 46 m².

- **Hint 1 (te schrijven):** De tuin bestaat uit twee rechthoeken. Hoeveel m² (vierkante meter) is elke rechthoek?
- **Hint 2 (te schrijven):** Reken elke rechthoek uit: lengte keer breedte. Tel de twee uitkomsten bij elkaar op.
- **Ouderzin:** Je kind rekent de oppervlakte van een L-vorm uit door hem in twee rechthoeken te splitsen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één rechthoek` (fout = getal1 × getal2) → Dat is maar één van de twee rechthoeken. Hoeveel m² is de andere?  [nieuw]
  - `één grote rechthoek` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Dat is te veel. Heb je van de twee stukken één grote rechthoek gemaakt? De tuin is een L.  [Claude, taalfix]
  - `maten opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je alle maten opgeteld? Oppervlakte reken je met keer: lengte keer breedte.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken elke rechthoek uit en tel de twee uitkomsten op.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een L-vormig hok bestaat uit een rechthoek van # bij # meter en een rechthoek van # bij # meter. Hoeveel m² is het hok?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: Een tuin van # bij # meter heeft een vierkante vijver van # bij # meter. Hoeveel m² gras is er?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een tuin van # bij # meter heeft een vierkante vijver van # bij # meter. Hoeveel m² gras is er?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: M24 (7) · regel: G8-M24-samengesteld
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (7), omtrek-oppervlakte-verwisseld (7), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 3 (meest: “De vijver is geen gras. Haal die eraf.”)
- Voorbeelden:
  - `G7-MEET-02-claude-bank-terug-009` (Claude M24, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een tuin van 6 bij 6 meter heeft een vierkante vijver van 3 bij 3 meter. Hoeveel m² gras is er?
    - **Antwoord:** 27  (controle: n.v.t.)
    - **Fout-hints (Claude):** 36 → De vijver is geen gras. Haal die eraf. · 34 → De vijver is 2 × 2 m², niet 2 m². · 40 → De vijver gaat eraf, niet erbij.
    - **Uitleg (Claude):** Hele tuin: 6 × 6 = 36 m². Vijver: 3 × 3 = 9 m². Gras: 36 − 9 = 27 m².
  - `G7-MEET-02-claude-bank-terug-013` (Claude M24, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een tuin van 9 bij 6 meter heeft een vierkante vijver van 5 bij 5 meter. Hoeveel m² gras is er?
    - **Antwoord:** 29  (controle: n.v.t.)
    - **Fout-hints (Claude):** 54 → De vijver is geen gras. Haal die eraf. · 52 → De vijver is 2 × 2 m², niet 2 m². · 58 → De vijver gaat eraf, niet erbij.
    - **Uitleg (Claude):** Hele tuin: 9 × 6 = 54 m². Vijver: 5 × 5 = 25 m². Gras: 54 − 25 = 29 m².

- **Hint 1 (te schrijven):** Hoeveel m² (vierkante meter) is de hele tuin? En hoeveel is de vijver?
- **Hint 2 (te schrijven):** Reken de tuin uit: lengte keer breedte. Reken de vijver uit: zijde keer zijde. Haal de vijver van de tuin af.
- **Ouderzin:** Je kind rekent uit hoeveel gras er is: de tuin min de vijver.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `vijver niet afgehaald` (fout = getal1 × getal2) → Dat is de hele tuin. Waar de vijver ligt, groeit geen gras. Wat moet er nog af?  [nieuw]
  - `zijde afgehaald` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Heb je alleen de zijde van de vijver afgetrokken? De vijver is een vierkant: zijde keer zijde.  [Claude, taalfix]
  - `vijver erbij` (Claudes sleutel: verkeerde-bewerking) → Heb je de vijver erbij opgeteld? Waar de vijver ligt, groeit geen gras: haal hem eraf.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de tuin uit en haal de vijver eraf.  [nieuw]
- Status: hints klaar

## Somtype 4: [driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # cm en een hoogte van # cm. Wat is de oppervlakte in cm²?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # cm en een hoogte van # cm. Wat is de oppervlakte in cm²?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M21 (4) · regel: D-DRIEHOEK-G7, D-DRIEHOEK-G7-FIX
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (8), optellen-ipv-vermenigvuldigen (4)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is de hele rechthoek. Een driehoek is de helft.”)
- Voorbeelden:
  - `G7-MEET-02-claude-bank-033` (Claude M21, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een driehoekige vlag heeft een basis van 12 cm en een hoogte van 5 cm. Wat is de oppervlakte in cm²?
    - **Tekening:** `{"soort": "driehoek-in-rechthoek", "basis": 12, "hoogte": 5, "eenheid": "cm", "hoogteStippellijn": true, "arcering": "driehoek", "label": "de helft"}`
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** 60 → Dat is de hele rechthoek. Een driehoek is de helft. · 17 → Oppervlakte is keer, niet plus. · 15 → Eén keer delen door 2 is genoeg.
    - **Uitleg (Claude):** Een driehoek is de helft van een rechthoek. 12 × 5 = 60, gedeeld door 2 = 30 cm².
  - `G7-MEET-02-claude-bank-034` (Claude M21, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een driehoekige vlag heeft een basis van 18 cm en een hoogte van 7 cm. Wat is de oppervlakte in cm²?
    - **Tekening:** `{"soort": "driehoek-in-rechthoek", "basis": 18, "hoogte": 7, "eenheid": "cm", "hoogteStippellijn": true, "arcering": "driehoek", "label": "de helft"}`
    - **Antwoord:** 63  (controle: ok)
    - **Fout-hints (Claude):** 126 → Dat is de hele rechthoek. Een driehoek is de helft. · 25 → Oppervlakte is keer, niet plus. · 31,5 → Eén keer delen door 2 is genoeg.
    - **Uitleg (Claude):** Een driehoek is de helft van een rechthoek. 18 × 7 = 126, gedeeld door 2 = 63 cm².

- **Hint 1 (te schrijven):** Een driehoek is de helft van een rechthoek met dezelfde basis en hoogte. De oppervlakte reken je in cm² (vierkante centimeter).
- **Hint 2 (te schrijven):** Reken eerst de rechthoek uit: basis keer hoogte. Neem daarvan de helft. Dat is de oppervlakte van de driehoek.
- **Ouderzin:** Je kind rekent de oppervlakte van een driehoek uit: basis keer hoogte, en daarvan de helft (in cm²).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rechthoek niet gehalveerd` (fout = getal1 × getal2) → Dat is de hele rechthoek. Hoeveel is de driehoek daarvan?  [nieuw]
  - `basis en hoogte opgeteld` (fout = getal1 + getal2) → Heb je de basis en de hoogte opgeteld? Oppervlakte reken je met keer.  [nieuw]
  - `twee keer gehalveerd` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je twee keer door twee gedeeld?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken basis keer hoogte en neem daarvan de helft.  [nieuw]
- Status: hints klaar
