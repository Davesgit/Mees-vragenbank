# G8-VERH-E01 — Breuk, procent en 'op de'; ook boven 100%

Onze omschrijving: Notaties koppelen (telling ↔ 1 op n ↔ breuk ↔ %); % >100% · in onze bank: 8 items

Claude-vragen gemapt: **1** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In een bak zitten # [ding], # [ding] en # [ding] knikker. Welk deel van de knikkers is rood?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In een bak zitten # [ding], # [ding] en # [ding] knikker. Welk deel van de knikkers is rood?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-DEEL-VAN-DE-KNIKKERS
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Je zette 6 tegenover de andere knikkers. Tel alle knikkers in de bak, dus ook de 6.”)
- Voorbeelden:
  - `G8-VERH-E01-claude-bank-001` (Claude G9, ai, niveau 1 → basis)
    - **Opgave:** In een bak zitten 6 rode, 3 blauwe en 1 groene knikker. Welk deel van de knikkers is rood?
    - **Opties:** A) 6 op de 10 · B) 6 op de 4 · C) 3 op de 10
    - **Antwoord:** 6 op de 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** Blauw → Kijk van welke kleur er de meeste knikkers in de bak liggen. · Alle kleuren evenveel → De aantallen per kleur zijn niet gelijk. Vergelijk de aantallen nog eens.
    - **Uitleg (Claude):** Er liggen 6 rode, 3 blauwe en 1 groene knikker. Samen zijn dat 10 knikkers. Daarvan zijn er 6 rood. Dus 6 op de 10 knikkers is rood.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
