# G8-VBN-E01 — Grafieken vergelijken en voorspellen

Onze omschrijving: Tabellen/grafieken: vergelijken, combineren, trends, voorspellingen · in onze bank: 8 items

Claude-vragen gemapt: **2** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een tabel laat zien hoeveel appels een boom geeft: jaar # geeft # appels, jaar # geeft # appels en jaar # geeft # appels. Hoeveel appels verwacht je in jaar #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een tabel laat zien hoeveel appels een boom geeft: jaar # [ding] # [ding], jaar # [ding] # [ding] en jaar # [ding] # [ding]. Hoeveel appels verwacht je in jaar #?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VBN-E01
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het aantal van jaar 3 herhaald. Kijk naar de stap tussen de jaren.”)
- Voorbeelden:
  - `G8-VBN-E01-claude-bank-001` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Een tabel laat zien hoeveel appels een boom geeft: jaar 1 geeft 40 appels, jaar 2 geeft 50 appels en jaar 3 geeft 60 appels. Hoeveel appels verwacht je in jaar 4?
    - **Opties:** A) Ongeveer 60 appels · B) Ongeveer 120 appels · C) Ongeveer 70 appels
    - **Antwoord:** Ongeveer 70 appels  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ongeveer 60 appels → Je hebt het aantal van jaar 3 herhaald. Kijk naar de stap tussen de jaren. · Ongeveer 120 appels → Je hebt het aantal verdubbeld. Kijk hoeveel er elk jaar bij komt.
    - **Uitleg (Claude):** Elk jaar komen er 10 appels bij: van 40 naar 50 naar 60. Als dat zo doorgaat, komen er in jaar 4 weer 10 bij. Dat is ongeveer 70 appels.

- **Hint 1 (te schrijven):** Kijk hoeveel er elk jaar bij komt.
- **Hint 2 (te schrijven):** Reken uit hoeveel er van het ene jaar naar het volgende bij komt. Komt dat er elk jaar bij? Doe het dan nog één keer erbij, bovenop het grootste aantal uit de tabel.
- **Ouderzin:** Je kind trekt een tabel door: elk jaar komt er hetzelfde aantal bij, dus ook in het jaar daarna.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `jaar ervoor` (Ongeveer 60 appels) → Dat aantal staat al in de tabel, bij het jaar ervoor. Er komt elk jaar nog wat bij.  [nieuw]
  - `verdubbeld` (Ongeveer 120 appels) → Dat is het dubbele. Elk jaar komt er hetzelfde aantal bij; het wordt niet elk jaar twee keer zo veel.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoeveel er elk jaar bij komt, en doe dat nog één keer erbij.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een tabel laat zien hoeveel appels een boom geeft: jaar # [ding] # [ding], jaar # [ding] # [ding] en jaar # [ding] # [ding]. Hoeveel appels verwacht je in jaar #?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 2: Vijf kinderen sprongen ver. Dit zijn hun sprongen: # m · # m · # m · # m · # m. Wat is het verschil tussen de verste en de kortste sprong?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Vijf kinderen sprongen ver. Dit zijn hun sprongen: # m · # m · # m · # m · # m. Wat is het verschil tussen de verste en de kortste sprong?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KOMMA-LIJST
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een verschil vind je door af te trekken, niet door op te tellen.”)
- Voorbeelden:
  - `G8-VBN-E01-claude-bank-002` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Vijf kinderen sprongen ver. Dit zijn hun sprongen: 2,1 m · 2,4 m · 2 m · 2,3 m · 2,2 m. Wat is het verschil tussen de verste en de kortste sprong?
    - **Opties:** A) 4,4 m · B) 0,2 m · C) 0,4 m
    - **Antwoord:** 0,4 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4,4 m → Een verschil vind je door af te trekken, niet door op te tellen. · 0,2 m → Zoek eerst echt de allerkortste sprong op in de rij.
    - **Uitleg (Claude):** De verste sprong is 2,40 m en de kortste is 2,00 m. Je trekt af: 2,40 − 2,00 = 0,40. Het verschil is dus 0,40 m.

- **Hint 1 (te schrijven):** Het verschil is hoeveel de verste sprong verder is dan de kortste.
- **Hint 2 (te schrijven):** Zoek de verste en de kortste sprong. Let op: een sprong zonder komma is precies een hele meter. Trek de kortste van de verste af.
- **Ouderzin:** Je kind zoekt de grootste en de kleinste waarde en trekt ze van elkaar af (het verschil).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (4,4 m) → Dat zijn de verste en de kortste sprong samen. Een verschil reken je uit met aftrekken.  [nieuw]
  - `andere sprongen` (0,2 m) → Dat is het verschil tussen twee andere sprongen. Zoek de verste en de allerkortste sprong. Kijk ook naar de sprong zonder komma.  [nieuw]
  - `andere fout` (andere fout) → Zoek de verste en de kortste sprong, en trek ze van elkaar af.  [nieuw]
- Status: hints klaar
