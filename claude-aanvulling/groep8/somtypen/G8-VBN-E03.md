# G8-VBN-E03 — Regelmaat vinden in rijen en regels

Onze omschrijving: Regelmaat/verbanden (getal, figuur, eenvoudige rekenregel) · in onze bank: 8 items

Claude-vragen gemapt: **12** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een spaartabel: week # → €#, week # → €#, week # → €#. Wat staat er bij week #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een spaartabel: week # → €#, week # → €#, week # → €#. Wat staat er bij week #?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: G12 (8) · regel: G8-P00-park-G7
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (16), tafelbuur (5)
- Verschillende Claude-fout-hints: 14 (meest: “Je moet tot week 6 doortellen, niet één stap verder dan de tabel.”)
- Voorbeelden:
  - `G8-VBN-E03-claude-bank-007` (Claude G12, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een spaartabel: week 0 → €43, week 1 → €68, week 2 → €93. Wat staat er bij week 6?
    - **Antwoord:** 193  (controle: ok)
    - **Fout-hints (Claude):** €118 → Je moet tot week 6 doortellen, niet één stap verder dan de tabel. · €150 → Vergeet het startbedrag van €43 niet. · €168 → Week 6 betekent 6 keer de stap erbij.
    - **Uitleg (Claude):** Elke week komt er 25 bij: dat is de regel. Week 6: 43 + 6 × 25 = 193.
  - `G8-VBN-E03-claude-bank-003` (Claude G12, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een spaartabel: week 0 → €47, week 1 → €57, week 2 → €67. Wat staat er bij week 4?
    - **Antwoord:** 87  (controle: ok)
    - **Fout-hints (Claude):** €77 → Je moet tot week 4 doortellen, niet één stap verder dan de tabel. · €40 → Vergeet het startbedrag van €47 niet.
    - **Uitleg (Claude):** Elke week komt er 10 bij: dat is de regel. Week 4: 47 + 4 × 10 = 87.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Je spaart voor ballen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Je spaart voor ballen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G12 (1) · regel: G8-P00-park-G7
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), tafelbuur (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je begon al met €38. Die tel je erbij.”)
- Voorbeelden:
  - `G8-VBN-E03-claude-bank-009` (Claude G12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je spaart voor ballen. Je begint met €38 en legt elke week €15 erbij. Hoeveel heb je na 5 weken?
    - **Antwoord:** 113  (controle: n.v.t.)
    - **Fout-hints (Claude):** €75 → Je begon al met €38. Die tel je erbij. · €128 → Na 5 weken heb je 5 keer gespaard, niet 6 keer. · €58 → 5 weken van €15: dat is een keersom.
    - **Uitleg (Claude):** Maak een tabel: week 0 → 38, week 1 → 53, ... Elke week 15 erbij, 5 weken: 5 × 15 = 75. 38 + 75 = 113.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Je spaart voor een fiets. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Je spaart voor een fiets. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G12 (1) · regel: G8-P00-park-G7
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), tafelbuur (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je begon al met €21. Die tel je erbij.”)
- Voorbeelden:
  - `G8-VBN-E03-claude-bank-010` (Claude G12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je spaart voor een fiets. Je begint met €21 en legt elke week €25 erbij. Hoeveel heb je na 8 weken?
    - **Antwoord:** 221  (controle: n.v.t.)
    - **Fout-hints (Claude):** €200 → Je begon al met €21. Die tel je erbij. · €246 → Na 8 weken heb je 8 keer gespaard, niet 9 keer. · €54 → 8 weken van €25: dat is een keersom.
    - **Uitleg (Claude):** Maak een tabel: week 0 → 21, week 1 → 46, ... Elke week 25 erbij, 8 weken: 8 × 25 = 200. 21 + 200 = 221.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Je spaart voor stappen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Je spaart voor stappen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G12 (1) · regel: G8-P00-park-G7
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), tafelbuur (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je begon al met €12. Die tel je erbij.”)
- Voorbeelden:
  - `G8-VBN-E03-claude-bank-011` (Claude G12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je spaart voor stappen. Je begint met €12 en legt elke week €10 erbij. Hoeveel heb je na 8 weken?
    - **Antwoord:** 92  (controle: n.v.t.)
    - **Fout-hints (Claude):** €80 → Je begon al met €12. Die tel je erbij. · €102 → Na 8 weken heb je 8 keer gespaard, niet 9 keer. · €30 → 8 weken van €10: dat is een keersom.
    - **Uitleg (Claude):** Maak een tabel: week 0 → 12, week 1 → 22, ... Elke week 10 erbij, 8 weken: 8 × 10 = 80. 12 + 80 = 92.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Je spaart voor sterren. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Je spaart voor sterren. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # weken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G12 (1) · regel: G8-P00-park-G7
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), tafelbuur (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je begon al met €14. Die tel je erbij.”)
- Voorbeelden:
  - `G8-VBN-E03-claude-bank-012` (Claude G12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je spaart voor sterren. Je begint met €14 en legt elke week €15 erbij. Hoeveel heb je na 6 weken?
    - **Antwoord:** 104  (controle: n.v.t.)
    - **Fout-hints (Claude):** €90 → Je begon al met €14. Die tel je erbij. · €119 → Na 6 weken heb je 6 keer gespaard, niet 7 keer. · €35 → 6 weken van €15: dat is een keersom.
    - **Uitleg (Claude):** Maak een tabel: week 0 → 14, week 1 → 29, ... Elke week 15 erbij, 6 weken: 6 × 15 = 90. 14 + 90 = 104.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
