# G8-VERH-E06 — Procenten checken en omzetten uit je hoofd

Onze omschrijving: % niet zomaar optellen; kritische %; relaties VERH↔breuk↔%↔decimaal uit hoofd · in onze bank: 8 items

Claude-vragen gemapt: **104** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Schrijf # in procenten.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Schrijf # in procenten.” (koppeling: claudeId)
- Items: **96** · Claude-doelen: B13 (96) · regel: G8-P00-park-G7
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): komma-verschoven (118), getal-overgenomen (74)
- Verschillende Claude-fout-hints: 1 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-052` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,025 in procenten.
    - **Opties:** A) 25% · B) 0,25% · C) 2,5%
    - **Antwoord:** 2,5%  (controle: ok)
    - **Fout-hints (Claude):** 25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 0,25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G8-VERH-E06-claude-bank-011` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,525 in procenten.
    - **Opties:** A) 0,525% · B) 52,5% · C) 5,25%
    - **Antwoord:** 52,5%  (controle: ok)
    - **Fout-hints (Claude):** 5,25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Schrijf #/# in procenten.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Schrijf #/# in procenten.” (koppeling: claudeId)
- Items: **7** · Claude-doelen: B13 (7) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 40) · type: meerkeuze
- Denkfouten (Claude): nul-fout-tientallen (11), getal-overgenomen (3)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-101` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 11/40 in procenten.
    - **Opties:** A) 2,75% · B) 27,5% · C) 275%
    - **Antwoord:** 27,5%  (controle: n.v.t.)
    - **Fout-hints (Claude):** 275% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · 2,75% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G8-VERH-E06-claude-bank-098` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 21/40 in procenten.
    - **Opties:** A) 5,25% · B) 52,5% · C) 21%
    - **Antwoord:** 52,5%  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5,25% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: #% van de [ding] is kapot. Schrijf dat als kommagetal.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “#% van de [ding] is kapot. Schrijf dat als kommagetal.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B13 (1) · regel: G8-P00-park-G7
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): komma-verschoven (1), kommagetal-als-geheel (1)
- Verschillende Claude-fout-hints: 2 (meest: “Procent is per honderd: de komma schuift twee plekken naar links, niet één.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-001` (Claude B13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 12,5% van de vissen is kapot. Schrijf dat als kommagetal.
    - **Antwoord:** 0,125  (controle: ok)
    - **Fout-hints (Claude):** 1,3 → Procent is per honderd: de komma schuift twee plekken naar links, niet één. · 12.5 → 12.5% is 12.5 van de 100. Als kommagetal deel je door 100.
    - **Uitleg (Claude):** Procent is per honderd: 12,5 : 100 = 0,125.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
