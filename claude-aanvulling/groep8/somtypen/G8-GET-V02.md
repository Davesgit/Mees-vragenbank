# G8-GET-V02 — Rekenen tot 100.000 en rekenmachine herhalen

Onze omschrijving: +/−/×÷ ±100.000; ×÷ decimalen (basis); rekenmachine eenvoudig · in onze bank: 8 items

Claude-vragen gemapt: **4** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een groep van # [ding] heeft gemiddeld # [ding]. Hoeveel knikkers hebben zij samen?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een groep van # [ding] heeft gemiddeld # [ding]. Hoeveel knikkers hebben zij samen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-GEMIDDELDE
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt de getallen opgeteld. Elk kind heeft gemiddeld 5 knikkers.”)
- Voorbeelden:
  - `G8-GET-V02-claude-bank-001` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Een groep van 8 kinderen heeft gemiddeld 5 knikkers. Hoeveel knikkers hebben zij samen?
    - **Opties:** A) 40 knikkers · B) 13 knikkers · C) 1,6 knikkers
    - **Antwoord:** 40 knikkers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 13 knikkers → Je hebt de getallen opgeteld. Elk kind heeft gemiddeld 5 knikkers. · 1,6 knikkers → Bij een gemiddelde reken je terug door te vermenigvuldigen, niet door te delen.
    - **Uitleg (Claude):** Gemiddeld 5 knikkers per kind betekent 8 x 5 knikkers in totaal. 8 x 5 = 40. Samen hebben zij 40 knikkers.

- **Hint 1 (te schrijven):** Gemiddeld betekent: als iedereen in de groep er evenveel had.
- **Hint 2 (te schrijven):** Gemiddeld betekent: ieder evenveel. Doe het aantal in de groep keer wat ieder gemiddeld heeft.
- **Ouderzin:** Je kind rekent terug van een gemiddelde naar het totaal: het aantal keer het gemiddelde.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (13 knikkers) → Dan tel je het aantal in de groep en het gemiddelde bij elkaar op. Maar elk van hen heeft er gemiddeld evenveel: hoeveel zijn dat er samen?  [nieuw]
  - `gedeeld` (1,6 knikkers) → Dat is minder dan wat ieder gemiddeld heeft. Samen hebben ze er juist meer.  [nieuw]
  - `andere fout` (andere fout) → Ieder heeft er gemiddeld evenveel. Hoeveel zijn dat er samen?  [nieuw]
- Status: hints klaar

## Somtype 2: In een zwembad zwemmen op zaterdag # [ding] en op zondag # [ding]. Hoeveel mensen zwommen er dat weekend gemiddeld per dag?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In een zwembad zwemmen op zaterdag # [ding] en op zondag # [ding]. Hoeveel mensen zwommen er dat weekend gemiddeld per dag?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-GEMIDDELDE
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt alleen opgeteld. Er zijn twee dagen, dus je moet nog delen.”)
- Voorbeelden:
  - `G8-GET-V02-claude-bank-002` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een zwembad zwemmen op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er dat weekend gemiddeld per dag?
    - **Opties:** A) 40 mensen · B) 300 mensen · C) 600 mensen
    - **Antwoord:** 300 mensen  (controle: ok)
    - **Fout-hints (Claude):** 600 mensen → Je hebt alleen opgeteld. Er zijn twee dagen, dus je moet nog delen. · 40 mensen → 40 is het verschil tussen de dagen. Een gemiddelde reken je anders uit.
    - **Uitleg (Claude):** Je telt op: 320 + 280 = 600. Daarna deel je door 2 dagen: 600 : 2 = 300. Gemiddeld zwommen er 300 mensen per dag.

- **Hint 1 (te schrijven):** Gemiddeld per dag: als er elke dag evenveel hadden gezwommen, hoeveel was dat dan per dag?
- **Hint 2 (te schrijven):** Tel de aantallen van de twee dagen bij elkaar op: dat is het totaal. Verdeel dat eerlijk: deel het totaal door het aantal dagen.
- **Ouderzin:** Je kind rekent een gemiddelde uit: alles optellen en delen door het aantal dagen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `totaal` (600 mensen) → Dat is het totaal van het weekend. Gemiddeld per dag is dat totaal eerlijk verdeeld over de dagen.  [nieuw]
  - `verschil` (40 mensen) → Dat is het verschil tussen de twee dagen. Een gemiddelde ligt tussen de twee aantallen in.  [nieuw]
  - `andere fout` (andere fout) → Tel alles op en verdeel het eerlijk over de dagen.  [nieuw]
- Status: hints klaar

## Somtype 3: In groep # [ding] # [ding] een cijfer voor een toets. Tien kinderen hebben een #, vijf kinderen een # en vijf kinderen een #. Wat is het gemiddelde cijfer?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In groep # [ding] # [ding] een cijfer voor een toets. Tien kinderen hebben een #, vijf kinderen een # en vijf kinderen een #. Wat is het gemiddelde cijfer?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-MODUS-NAAR-GEMIDDELDE
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Dat is het totaal van alle cijfers. Verdeel het nog eerlijk over de 20 kinderen.”)
- Voorbeelden:
  - `G8-GET-V02-claude-bank-003` (Claude G9, ai, niveau 1 → basis)
    - **Opgave:** In groep 8 hebben 20 kinderen een cijfer voor een toets. Tien kinderen hebben een 7, vijf kinderen een 8 en vijf kinderen een 6. Wat is het gemiddelde cijfer?
    - **Opties:** A) 7 · B) 140 · C) 21
    - **Antwoord:** 7  (controle: n.v.t.)
    - **Fout-hints (Claude):** 8 → Kijk niet naar het hoogste cijfer, maar naar hoeveel kinderen elk cijfer hebben. · 20 → 20 is het aantal kinderen in de klas en geen cijfer van een toets.
    - **Uitleg (Claude):** Je telt hoe vaak elk cijfer voorkomt. De 7 komt 10 keer voor, de 8 en de 6 allebei 5 keer. Dus de 7 komt het vaakst voor.

- **Hint 1 (te schrijven):** Bij een gemiddelde tellen alle cijfers mee, ook als hetzelfde cijfer vaak voorkomt.
- **Hint 2 (te schrijven):** Reken uit hoeveel punten alle kinderen samen hebben: elk cijfer keer het aantal kinderen met dat cijfer, en dat bij elkaar. Deel dat door het aantal kinderen.
- **Ouderzin:** Je kind rekent een gemiddelde uit als cijfers vaker voorkomen: elk cijfer telt zo vaak mee als het voorkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `totaal` (140) → Dat is het totaal van alle cijfers samen. Verdeel het nog eerlijk over alle kinderen.  [nieuw]
  - `elk cijfer één keer` (21) → Dan telt elk cijfer maar één keer mee. Elk cijfer telt zo vaak mee als er kinderen zijn met dat cijfer.  [nieuw]
  - `andere fout` (andere fout) → Elk cijfer telt zo vaak mee als het voorkomt. Deel het totaal door het aantal kinderen.  [nieuw]
- Status: hints klaar

## Somtype 4: Mila fietst vier dagen naar school. # km, # km, # km en # km. Hoeveel kilometer fietst zij gemiddeld per dag?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Mila fietst vier dagen naar school. # km, # km, # km en # km. Hoeveel kilometer fietst zij gemiddeld per dag?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-GEMIDDELDE
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt alles opgeteld. Daarna moet je nog delen door het aantal dagen.”)
- Voorbeelden:
  - `G8-GET-V02-claude-bank-004` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Mila fietst vier dagen naar school. 3 km, 5 km, 4 km en 4 km. Hoeveel kilometer fietst zij gemiddeld per dag?
    - **Opties:** A) 4 km · B) 16 km · C) 5 km
    - **Antwoord:** 4 km  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 km → Je hebt alles opgeteld. Daarna moet je nog delen door het aantal dagen. · 5 km → 5 km is de langste dag. Een gemiddelde ligt tussen de kleinste en de grootste waarde.
    - **Uitleg (Claude):** Je telt de afstanden op: 3 + 5 + 4 + 4 = 16. Daarna deel je door 4 dagen: 16 : 4 = 4. Het gemiddelde is 4 km per dag.

- **Hint 1 (te schrijven):** Gemiddeld per dag: als ze elke dag even ver had gefietst, hoe ver was dat dan?
- **Hint 2 (te schrijven):** Tel alle afstanden bij elkaar op: dat is het totaal. Deel het totaal door het aantal dagen.
- **Ouderzin:** Je kind rekent een gemiddelde uit: alle afstanden optellen en delen door het aantal dagen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `totaal` (16 km) → Dat is het totaal van alle dagen. Verdeel het nog eerlijk over de dagen.  [nieuw]
  - `langste dag` (5 km) → Dat is de langste dag. Een gemiddelde ligt tussen de kortste en de langste dag in.  [nieuw]
  - `andere fout` (andere fout) → Tel alle afstanden op en deel door het aantal dagen.  [nieuw]
- Status: hints klaar
