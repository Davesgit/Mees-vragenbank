# G5-MKU-E02 — Bouwplaat met plakranden

Onze omschrijving: Bouwplaat: plakranden; eenvoudig object ontwerpen · in onze bank: 8 items

Claude-vragen gemapt: **3** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [ruimtefiguur] Een hoekpunt is een punt waar randen samenkomen. ⏎ Dit is een kubus. Hoeveel [ding] heeft een kubus? (Tel ook wat je niet ziet.)

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[ruimtefiguur] Een hoekpunt is een punt waar randen samenkomen. ⏎ Dit is een kubus. Hoeveel [ding] heeft een kubus? (Tel ook wat je niet ziet.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: K5 (1) · regel: D-RIBBEN-HOEKPUNTEN
- Getallenruimte: n.v.t. · type: kale
- **Visual: nodig — niet live zonder beeld** (1 items): tekening van een kubus met een doorzichtige of gestippelde achterkant, zodat het kind ook de ribben en hoekpunten achter kan tellen (Didactiek §4)
- Didactiek-besluit (G4-twijfel, 1 okt): ribben/hoekpunten tellen (ook verborgen) — zie g4/besluiten_twijfel.md + besluit Dave
- Denkfouten (Claude): een-ernaast (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee.”)
- Voorbeelden:
  - `G5-MKU-E02-claude-bank-001` (Claude K5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een hoekpunt is een punt waar randen samenkomen.
Dit is een kubus. Hoeveel hoekpunten heeft een kubus? (Tel ook wat je niet ziet.)
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "kubus"}`
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee. · 9 → Je hebt er een dubbel geteld. Ga systematisch rond: boven, onder, dan de zijkanten.
    - **Uitleg (Claude):** Een kubus heeft 6 vlakken, 8 hoekpunten en 12 ribben.

- **Hint 1 (te schrijven):** Tel eerst de hoekpunten aan de bovenkant van de kubus.
- **Hint 2 (te schrijven):** Tel dan de hoekpunten aan de onderkant erbij. Tel ook de hoekpunten die je niet ziet.
- **Ouderzin:** Je kind telt de hoekpunten van een kubus, ook de hoekpunten die je niet ziet.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is er één te veel. Heb je er één dubbel geteld? Tel eerst de bovenkant, dan de onderkant.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Heb je de hoekpunten dubbel geteld? Tel eerst de bovenkant, dan de onderkant.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is er één te weinig. Heb je ook de hoekpunten geteld die je niet ziet?  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Heb je ook de hoekpunten geteld die je niet ziet? De achterkant en de onderkant tellen ook mee.  [nieuw]
  - `andere fout` (andere fout) → Tel eerst de bovenkant, dan de onderkant. Tel ook de hoekpunten die je niet ziet.  [nieuw]
- Status: hints klaar

## Somtype 2: [ruimtefiguur] Een vlak is een platte kant van de figuur. Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een balk. Hoeveel [ding] heeft een balk? (Tel ook wat je niet ziet.)

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[ruimtefiguur] Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een balk. Hoeveel [ding] heeft een balk? (Tel ook wat je niet ziet.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: K5 (1) · regel: D-RIBBEN-HOEKPUNTEN
- Getallenruimte: n.v.t. · type: kale
- **Visual: nodig — niet live zonder beeld** (1 items): tekening van een balk met een doorzichtige of gestippelde achterkant, zodat het kind ook de ribben en hoekpunten achter kan tellen (Didactiek §4)
- Didactiek-besluit (G4-twijfel, 1 okt): ribben/hoekpunten tellen (ook verborgen) — zie g4/besluiten_twijfel.md + besluit Dave
- Denkfouten (Claude): een-ernaast (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee.”)
- Voorbeelden:
  - `G5-MKU-E02-claude-bank-002` (Claude K5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een vlak is een platte kant van de figuur. Een ribbe is de rand waar twee vlakken tegen elkaar zitten.
Dit is een balk. Hoeveel ribben heeft een balk? (Tel ook wat je niet ziet.)
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "balk"}`
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee. · 13 → Je hebt er een dubbel geteld. Ga systematisch rond: boven, onder, dan de zijkanten.
    - **Uitleg (Claude):** Een balk heeft 6 vlakken, 8 hoekpunten en 12 ribben.

- **Hint 1 (te schrijven):** Tel eerst de ribben van het bovenvlak. Tel dan de ribben van het ondervlak.
- **Hint 2 (te schrijven):** Tel tot slot de ribben die van boven naar beneden lopen. Tel ook de ribben die je niet ziet.
- **Ouderzin:** Je kind telt de ribben van een balk, ook de ribben die je niet ziet.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is er één te veel. Heb je er één dubbel geteld? Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Heb je de ribben dubbel geteld? Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is er één te weinig. Heb je ook de ribben geteld die je niet ziet?  [nieuw]
  - `aantal vlakken` (fout = antwoord − 6) → Dat is te weinig. Zes is het aantal vlakken. Je telt de ribben: de randen waar twee vlakken tegen elkaar zitten.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Heb je ook de ribben geteld die je niet ziet? De achterkant en de onderkant tellen ook mee.  [nieuw]
  - `andere fout` (andere fout) → Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden. Tel ook de ribben die je niet ziet.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor '[ruimtefiguur] Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een balk. Hoeveel [ding] heeft een balk? (Tel ook wat je niet ziet.)'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: [ruimtefiguur] Een vlak is een platte kant van de figuur. Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een kubus. Hoeveel [ding] heeft een kubus? (Tel ook wat je niet ziet.)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[ruimtefiguur] Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een kubus. Hoeveel [ding] heeft een kubus? (Tel ook wat je niet ziet.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: K5 (1) · regel: D-RIBBEN-HOEKPUNTEN
- Getallenruimte: n.v.t. · type: kale
- **Visual: nodig — niet live zonder beeld** (1 items): tekening van een kubus met een doorzichtige of gestippelde achterkant, zodat het kind ook de ribben en hoekpunten achter kan tellen (Didactiek §4)
- Didactiek-besluit (G4-twijfel, 1 okt): ribben/hoekpunten tellen (ook verborgen) — zie g4/besluiten_twijfel.md + besluit Dave
- Denkfouten (Claude): een-ernaast (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee.”)
- Voorbeelden:
  - `G5-MKU-E02-claude-bank-003` (Claude K5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een vlak is een platte kant van de figuur. Een ribbe is de rand waar twee vlakken tegen elkaar zitten.
Dit is een kubus. Hoeveel ribben heeft een kubus? (Tel ook wat je niet ziet.)
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "kubus"}`
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee. · 13 → Je hebt er een dubbel geteld. Ga systematisch rond: boven, onder, dan de zijkanten.
    - **Uitleg (Claude):** Een kubus heeft 6 vlakken, 8 hoekpunten en 12 ribben.

- **Hint 1 (te schrijven):** Tel eerst de ribben van het bovenvlak. Tel dan de ribben van het ondervlak.
- **Hint 2 (te schrijven):** Tel tot slot de ribben die van boven naar beneden lopen. Tel ook de ribben die je niet ziet.
- **Ouderzin:** Je kind telt de ribben van een kubus, ook de ribben die je niet ziet.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is er één te veel. Heb je er één dubbel geteld? Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Heb je de ribben dubbel geteld? Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is er één te weinig. Heb je ook de ribben geteld die je niet ziet?  [nieuw]
  - `aantal vlakken` (fout = antwoord − 6) → Dat is te weinig. Zes is het aantal vlakken. Je telt de ribben: de randen waar twee vlakken tegen elkaar zitten.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Heb je ook de ribben geteld die je niet ziet? De achterkant en de onderkant tellen ook mee.  [nieuw]
  - `andere fout` (andere fout) → Tel eerst het bovenvlak, dan het ondervlak, en dan de ribben van boven naar beneden. Tel ook de ribben die je niet ziet.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor '[ruimtefiguur] Een ribbe is de rand waar twee vlakken tegen elkaar zitten. ⏎ Dit is een kubus. Hoeveel [ding] heeft een kubus? (Tel ook wat je niet ziet.)'. Nakijken of ze nog passen.
- Status: hints klaar
