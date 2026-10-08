# G6-GET-M03 — Kommagetallen lezen en op de lijn

Onze omschrijving: Decimalen 1–2 cijfers: lezen, betekenis (geld/meten), getallenlijn · in onze bank: 8 items

Claude-vragen gemapt: **32** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [stip op getallenlijn zetten] Zet # op de lijn van # tot #.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[stip op getallenlijn zetten] Zet # op de lijn van # tot #.” (koppeling: claudeId)
- Items: **24** · Claude-doelen: B11 (12), B12 (12) · regel: G6-B12-breuk-komma, G6-K03-komma-lijn
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Uit de G5-park: 12 items
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G6-GET-M03-claude-bank-010` (Claude B11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 0,7 op de lijn van 0 tot 2.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 0,7  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 0,7 is 0 heel en 7 tiende. Elk streepje is een tiende.
  - `G6-GET-M03-claude-bank-021` (Claude B12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 6,7 op de lijn van 0 tot 10.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 6,7  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Zoek eerst het hele getal: 6. Dan nog 7 tiende verder.

- **Hint 1 (te schrijven):** Zoek eerst het hele getal op de lijn. Bij een kommagetal is dat het cijfer vóór de komma.
- **Hint 2 (te schrijven):** Staat er een komma? Het cijfer achter de komma zegt hoeveel tienden je nog verder gaat. Tussen twee hele getallen zitten tien tienden.
- **Ouderzin:** Je kind zet een kommagetal met één cijfer achter de komma op een getallenlijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het hele getal` (fout = het hele getal van het kommagetal) → Dat is alleen het hele getal. Het cijfer achter de komma zegt hoeveel tienden je nog verder gaat.  [nieuw]
  - `cijfer achter de komma als heel getal` (fout = de tienden als heel getal) → Dat is het cijfer achter de komma, als heel getal. Zoek eerst het hele getal op de lijn: het cijfer vóór de komma. Ga dan zoveel tienden verder.  [nieuw]
  - `cijfers omgedraaid` (fout = de cijfers om de komma omgedraaid) → Je hebt de cijfers omgedraaid. Het cijfer vóór de komma is het hele getal. Het cijfer achter de komma zegt hoeveel tienden je verder gaat.  [nieuw]
  - `één tiende te ver` (fout = antwoord + 0,1) → Bijna! Je bent één tiende te ver. Zet je stip een klein stukje terug. Tussen twee hele getallen zitten tien tienden.  [nieuw]
  - `één tiende te kort` (fout = antwoord − 0,1) → Bijna! Je bent één tiende te kort. Zet je stip een klein stukje verder. Tussen twee hele getallen zitten tien tienden.  [nieuw]
  - `een getal uit de vraag` (fout = een getal uit de vraag) → Je stip staat aan het begin of aan het eind van de lijn. Zoek eerst het hele getal op de lijn. Staat er een komma? Ga dan zoveel tienden verder als het cijfer achter de komma zegt.  [nieuw]
  - `andere fout` (andere fout) → Zoek eerst het hele getal op de lijn. Staat er een komma? Ga dan zoveel tienden verder als het cijfer achter de komma zegt.  [nieuw]
- Status: hints klaar

## Somtype 2: Een [ding] is #/# meter lang. Schrijf dat als kommagetal.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een [ding] is #/# meter lang. Schrijf dat als kommagetal.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B11 (8) · regel: G6-B12-breuk-komma
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 2), breuken (noemer tot 4), breuken (noemer tot 5) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (8), kommagetal-als-geheel (6)
- Verschillende Claude-fout-hints: 7 (meest: “Teller gedeeld door noemer, niet andersom.”)
- Voorbeelden:
  - `G6-GET-M03-claude-bank-001` (Claude B11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een stap is 1/2 meter lang. Schrijf dat als kommagetal.
    - **Antwoord:** 0,5  (controle: ok)
    - **Fout-hints (Claude):** 0,10 → Zet niet zomaar de teller achter de komma. 1/2 is 1 gedeeld door 2. · 2,00 → Teller gedeeld door noemer, niet andersom.
    - **Uitleg (Claude):** 1/2 betekent 1 : 2. 1 : 2 = 0,5.
  - `G6-GET-M03-claude-bank-002` (Claude B11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bot is 3/10 meter lang. Schrijf dat als kommagetal.
    - **Antwoord:** 0,3  (controle: ok)
    - **Fout-hints (Claude):** 0,31 → Zet niet zomaar de teller achter de komma. 3/10 is 3 gedeeld door 10. · 3,33 → Teller gedeeld door noemer, niet andersom.
    - **Uitleg (Claude):** 3/10 betekent 3 : 10. 3 : 10 = 0,3.

- **Hint 1 (te schrijven):** Een meter is 100 centimeter. Hoeveel centimeter is dit stuk van een meter? Staat er boven de streep meer dan 1? Reken dan eerst uit hoeveel centimeter één gelijk deel is.
- **Hint 2 (te schrijven):** Schrijf het dan als kommagetal in meters. Het eerste cijfer achter de komma telt de stukken van tien centimeter, het tweede cijfer de losse centimeters. Zo is 68 centimeter 0,68 meter.
- **Ouderzin:** Je kind schrijft een breuk van een meter als kommagetal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet zo omgezet` (Claudes sleutel: kommagetal-als-geheel) → Je hebt het getal boven de streep achter de komma gezet. Zo schrijf je die breuk niet als kommagetal. Reken eerst uit hoeveel centimeter het is: een meter is 100 centimeter.  [Claude, taalfix]
  - `een meter of meer` (Claudes sleutel: omgekeerd-gedeeld) → Dat is een hele meter of meer. Maar het stuk is korter dan een meter: het getal boven de streep is kleiner dan het getal eronder.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoeveel centimeter het stuk is: een meter is 100 centimeter. Schrijf dat dan als deel van een meter, met een komma.  [nieuw]
- Status: hints klaar
