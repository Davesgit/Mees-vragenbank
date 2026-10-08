# G8-VERH-V01 — Procenten, breuken en schaal herhalen

Onze omschrijving: Verhouding/breuk/%-taal; eenvoudige %; schaalbegrip (eind G7) · in onze bank: 8 items

Claude-vragen gemapt: **1** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Bij een enquête zeggen # van de # [ding] dat zij het liefst voetballen. Hoeveel procent van [wie] is dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Bij een enquête zeggen # van de # [ding] dat zij het liefst voetballen. Hoeveel procent van [wie] is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VERH
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het getal 40 is het aantal kinderen en nog geen percentage. Vergelijk het met 200.”)
- Voorbeelden:
  - `G8-VERH-V01-claude-bank-001` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Bij een enquête zeggen 40 van de 200 kinderen dat zij het liefst voetballen. Hoeveel procent van de kinderen is dat?
    - **Opties:** A) 40 procent · B) 2 procent · C) 20 procent
    - **Antwoord:** 20 procent  (controle: n.v.t.)
    - **Fout-hints (Claude):** 40 procent → Het getal 40 is het aantal kinderen en nog geen percentage. Vergelijk het met 200. · 2 procent → Reken na hoeveel keer 40 in 200 past en maak daar een percentage van.
    - **Uitleg (Claude):** Je vergelijkt 40 met 200. 40 van de 200 is hetzelfde als 20 van de 100. Dus het is 20 procent.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
