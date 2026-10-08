# G6-GET-E08 — Het gemiddelde uitrekenen

Onze omschrijving: Gemiddelde in eenvoudige situaties · in onze bank: 8 items

Claude-vragen gemapt: **12** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # [wie] verzamelden [ding]. #, #, #, #, #. Hoeveel [ding] is dat gemiddeld per [wie]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# [wie] verzamelden [ding]. #, #, #, #, #. Hoeveel [ding] is dat gemiddeld per [wie]?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: G4 (9) · regel: G6-D04-gemiddelde
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (18), tiental-ernaast (7)
- Verschillende Claude-fout-hints: 11 (meest: “Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal.”)
- Voorbeelden:
  - `G6-GET-E08-claude-bank-007` (Claude G4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 5 dino's verzamelden tanden. Ze hadden er 6, 7, 2, 8 en 2. Hoeveel tanden is dat gemiddeld per dino?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 25 → 25 is het totaal. Gemiddeld betekent: delen door het aantal dino's. · 8 → Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal. · 6 → Controleer het optellen en deel dan precies door 5.
    - **Uitleg (Claude):** Tel alles op: 6 + 7 + 2 + 8 + 2 = 25. Deel door het aantal: 25 : 5 = 5.
  - `G6-GET-E08-claude-bank-005` (Claude G4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 5 poezen verzamelden balletjes. Ze hadden er 8, 3, 9, 5 en 5. Hoeveel balletjes is dat gemiddeld per poes?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 30 → 30 is het totaal. Gemiddeld betekent: delen door het aantal poezen. · 9 → Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal. · 7 → Controleer het optellen en deel dan precies door 5.
    - **Uitleg (Claude):** Tel alles op: 8 + 3 + 9 + 5 + 5 = 30. Deel door het aantal: 30 : 5 = 6.

- **Hint 1 (te schrijven):** Tel eerst alle getallen bij elkaar op.
- **Hint 2 (te schrijven):** Deel dat totaal door het aantal getallen. Zoveel is het gemiddeld.
- **Ouderzin:** Je kind rekent een gemiddelde uit: alles optellen en delen door het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na: het aantal keer jouw antwoord is dan meer dan het totaal.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na: het aantal keer jouw antwoord is dan minder dan het totaal.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Je hebt een van de getallen uit de vraag genomen. Het gemiddelde reken je uit: tel eerst alle getallen op en deel dan door het aantal.  [nieuw]
  - `het totaal` (Claudes sleutel: verkeerde-bewerking) → Dat is alles samen. Deel dat nog door het aantal.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel alle getallen bij elkaar op. Deel dat totaal daarna door het aantal getallen.  [nieuw]
- Status: hints klaar

## Somtype 2: # [wie] verzamelden [ding]. #, #, #, #. Hoeveel [ding] is dat gemiddeld per [wie]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# [wie] verzamelden [ding]. #, #, #, #. Hoeveel [ding] is dat gemiddeld per [wie]?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: G4 (3) · regel: G6-D04-gemiddelde
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (6), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 5 (meest: “Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal.”)
- Voorbeelden:
  - `G6-GET-E08-claude-bank-010` (Claude G4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 4 dino's verzamelden eieren. Ze hadden er 5, 6, 6 en 7. Hoeveel eieren is dat gemiddeld per dino?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 24 → 24 is het totaal. Gemiddeld betekent: delen door het aantal dino's. · 7 → Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal.
    - **Uitleg (Claude):** Tel alles op: 5 + 6 + 6 + 7 = 24. Deel door het aantal: 24 : 4 = 6.
  - `G6-GET-E08-claude-bank-011` (Claude G4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 4 kinderen verzamelden stickers. Ze hadden er 6, 3, 7 en 4. Hoeveel stickers is dat gemiddeld per kind?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 20 → 20 is het totaal. Gemiddeld betekent: delen door het aantal kinderen. · 7 → Het gemiddelde is niet het hoogste getal. Tel alles op en deel door het aantal. · 6 → Controleer het optellen en deel dan precies door 4.
    - **Uitleg (Claude):** Tel alles op: 6 + 3 + 7 + 4 = 20. Deel door het aantal: 20 : 4 = 5.

- **Hint 1 (te schrijven):** Tel eerst alle getallen bij elkaar op.
- **Hint 2 (te schrijven):** Deel dat totaal door het aantal getallen. Zoveel is het gemiddeld.
- **Ouderzin:** Je kind rekent een gemiddelde uit: alles optellen en delen door het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na: het aantal keer jouw antwoord is dan meer dan het totaal.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na: het aantal keer jouw antwoord is dan minder dan het totaal.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Je hebt een van de getallen uit de vraag genomen. Het gemiddelde reken je uit: tel eerst alle getallen op en deel dan door het aantal.  [nieuw]
  - `het totaal` (Claudes sleutel: verkeerde-bewerking) → Dat is alles samen. Deel dat nog door het aantal.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel alle getallen bij elkaar op. Deel dat totaal daarna door het aantal getallen.  [nieuw]
- Status: hints klaar
