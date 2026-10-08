# G6-VERH-E03 — Eerlijk verdelen en aanvullen tot geheel

Onze omschrijving: Verdelen in gelijke delen; complement tot geheel · in onze bank: 8 items

Claude-vragen gemapt: **29** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # [ding] worden eerlijk verdeeld over # [ding]. Welk deel van een [ding] krijgt [wie]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Welk deel van een [ding] krijgt [wie]?” (koppeling: claudeId)
- Items: **17** · Claude-doelen: B18 (17) · regel: G6-B13-breuk-deling
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (17), deel-van-geheel-verkeerd (17)
- Verschillende Claude-fout-hints: 27 (meest: “Je deelt 4 door 5: het getal dat je verdeelt komt boven.”)
- Voorbeelden:
  - `G6-VERH-E03-claude-bank-002` (Claude B18, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 blaadjes worden eerlijk verdeeld over 6 dino's. Welk deel van een blaadje krijgt elke dino?
    - **Antwoord:** 4/6  (controle: ok)
    - **Fout-hints (Claude):** 6/4 → Je deelt 4 door 6: het getal dat je verdeelt komt boven. · 1/6 → Er zijn 4 blaadjes, niet één. Elke dino krijgt van elk blaadje een 6-de deel.
    - **Uitleg (Claude):** Delen is een breuk: 4 : 6 = 4/6. Elke dino krijgt 4/6 blaadje.
  - `G6-VERH-E03-claude-bank-013` (Claude B18, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 taarten worden eerlijk verdeeld over 6 kinderen. Welk deel van een taart krijgt elk kind?
    - **Antwoord:** 4/6  (controle: ok)
    - **Fout-hints (Claude):** 6/4 → Je deelt 4 door 6: het getal dat je verdeelt komt boven. · 1/6 → Er zijn 4 kaartjes, niet één. Elk kind krijgt van elk kaartje een 6-de deel.
    - **Uitleg (Claude):** Delen is een breuk: 4 : 6 = 4/6. Elk kind krijgt 4/6 taart.

- **Hint 1 (te schrijven):** Een deel is een of meer gelijke stukken van een geheel. Eerlijk verdelen is een deling: wat je verdeelt, gedeeld door het aantal dat iets krijgt.
- **Hint 2 (te schrijven):** Eerlijk verdelen kun je als breuk schrijven. Wat je verdeelt, komt boven de streep. Dat is de teller. Over hoeveel je verdeelt, komt onder de streep. Dat is de noemer.
- **Ouderzin:** Je kind schrijft eerlijk verdelen als breuk. Het aantal dat verdeeld wordt, gedeeld door het aantal dat iets krijgt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omgedraaid` (Claudes sleutel: omgekeerd-gedeeld) → Je hebt de breuk omgedraaid. Wat je verdeelt, komt boven de streep (de teller). Over hoeveel je verdeelt, komt onder de streep (de noemer).  [Claude, taalfix]
  - `van één ervan` (Claudes sleutel: deel-van-geheel-verkeerd) → Zoveel krijgt ieder van één ervan. Maar er wordt meer dan één verdeeld. Van elk krijgt ieder zo'n stuk. Hoeveel stukken zijn dat samen?  [Claude, taalfix]
  - `andere fout` (andere fout) → Schrijf de deling als breuk. Wat je verdeelt, komt boven de streep. Over hoeveel je verdeelt, komt onder de streep.  [nieuw]
- Status: hints klaar

## Somtype 2: De breuk #/# is hetzelfde als een deelsom. Welke? # : □

- Sleutel: nrOrigineel **2** · somtypeOrigineel “De breuk #/# is hetzelfde als een deelsom. Welke? # : □” (koppeling: claudeId)
- Items: **12** · Claude-doelen: B18 (12) · regel: G6-B13-breuk-deling
- Getallenruimte: breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: invullen
- Denkfouten (Claude): omgekeerd-gedeeld (12), verkeerde-bewerking (12)
- Verschillende Claude-fout-hints: 2 (meest: “De noemer (onder de streep) is het getal waardoor je deelt.”)
- Voorbeelden:
  - `G6-VERH-E03-claude-bank-027` (Claude B18, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** De breuk 2/3 is hetzelfde als een deelsom. Welke? 2 : □
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 2 → De noemer (onder de streep) is het getal waardoor je deelt. · 1 → Niet aftrekken: de breukstreep is een deelteken.
    - **Uitleg (Claude):** De breukstreep betekent delen: 2/3 = 2 : 3.
  - `G6-VERH-E03-claude-bank-025` (Claude B18, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** De breuk 1/6 is hetzelfde als een deelsom. Welke? 1 : □
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 1 → De noemer (onder de streep) is het getal waardoor je deelt. · 5 → Niet aftrekken: de breukstreep is een deelteken.
    - **Uitleg (Claude):** De breukstreep betekent delen: 1/6 = 1 : 6.

- **Hint 1 (te schrijven):** Een breuk is ook een deling. De streep betekent gedeeld door. De teller (boven de streep) gedeeld door de noemer (onder de streep).
- **Hint 2 (te schrijven):** Het teken tussen de getallen in de som betekent gedeeld door. Vóór dat teken staat de teller. Welk getal komt erna? Kijk onder de streep.
- **Ouderzin:** Je kind schrijft een breuk als deelsom, de teller gedeeld door de noemer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller ingevuld` (fout = getal1) → Je hebt de teller ingevuld. De teller staat vóór het teken. Gedeeld door welk getal? Kijk onder de streep.  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt de teller van de noemer afgehaald. De breukstreep betekent gedeeld door. De teller gedeeld door de noemer.  [nieuw]
  - `andere fout` (andere fout) → De breukstreep betekent gedeeld door. Vóór het teken komt de teller, erna het getal onder de streep.  [nieuw]
- Status: hints klaar
