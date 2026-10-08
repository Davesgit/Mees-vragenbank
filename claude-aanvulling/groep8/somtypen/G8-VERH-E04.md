# G8-VERH-E04 — Procenten uitrekenen: 1%-regel en korting

Onze omschrijving: 1%-regel; % via breuk/decimaal; korting oud↔nieuw · in onze bank: 8 items

Claude-vragen gemapt: **32** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een [ding] kost na #% korting €#. Wat was de prijs vóór de korting?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een [ding] kost na #% korting €#. Wat was de prijs vóór de korting?” (koppeling: claudeId)
- Items: **14** · Claude-doelen: V6 (14) · regel: G8-P00-park-G7
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (14), getal-overgenomen (14)
- Verschillende Claude-fout-hints: 12 (meest: “Dat is de prijs ná de korting. Gevraagd is de prijs ervoor.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-010` (Claude V6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kaart kost na 20% korting €48. Wat was de prijs vóór de korting?
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** €58 → De 20% ging van de óude prijs af, niet van €48. €48 is 80%. · €48 → Dat is de prijs ná de korting. Gevraagd is de prijs ervoor.
    - **Uitleg (Claude):** €48 is 80% van de oude prijs. 1% is 48 : 80 = 0,60, dus 100% is €60.
  - `G8-VERH-E04-claude-bank-011` (Claude V6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een trui kost na 10% korting €54. Wat was de prijs vóór de korting?
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** €59 → De 10% ging van de óude prijs af, niet van €54. €54 is 90%. · €54 → Dat is de prijs ná de korting. Gevraagd is de prijs ervoor.
    - **Uitleg (Claude):** €54 is 90% van de oude prijs. 1% is 54 : 90 = 0,60, dus 100% is €60.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: [wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T6 (8) · regel: G8-T6-rente
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): komma-verschoven (8), getal-overgenomen (8), procent-verkeerde-basis (8)
- Verschillende Claude-fout-hints: 15 (meest: “Gevraagd is alleen de rente, niet het hele bedrag op de rekening.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-029` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind zet €2000 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt hij na één jaar?
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** €600 → 1% van 2000 is 20, niet 200. · €2060 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €3 → 3% is een deel van €2.000, niet €3.
    - **Uitleg (Claude):** 1% van 2000 is 20. 3% is 3 × 20 = €60.
  - `G8-VERH-E04-claude-bank-030` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind zet €500 op een spaarrekening met 1% rente per jaar. Hoeveel rente krijgt hij na één jaar?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** €50 → 1% van 500 is 5, niet 50. · €505 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €1 → 1% is een deel van €500, niet €1.
    - **Uitleg (Claude):** 1% van 500 is 5. 1% is 1 × 5 = €5.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: T6 (4) · regel: G8-T6-rente
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): komma-verschoven (4), getal-overgenomen (4), procent-verkeerde-basis (4)
- Verschillende Claude-fout-hints: 9 (meest: “Gevraagd is alleen de rente, niet het hele bedrag op de rekening.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-004` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Daan zet €200 op een spaarrekening met 1% rente per jaar. Hoeveel rente krijgt hij na één jaar?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** €20 → 1% van 200 is 2, niet 20. · €202 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €1 → 1% is een deel van €200, niet €1.
    - **Uitleg (Claude):** 1% van 200 is 2. 1% is 1 × 2 = €2.
  - `G8-VERH-E04-claude-bank-005` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Daan zet €400 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt hij na één jaar?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** €120 → 1% van 400 is 4, niet 40. · €412 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €3 → 3% is een deel van €400, niet €3.
    - **Uitleg (Claude):** 1% van 400 is 4. 3% is 3 × 4 = €12.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één jaar?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één jaar?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T6 (2) · regel: G8-T6-rente
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): komma-verschoven (2), getal-overgenomen (2), procent-verkeerde-basis (2)
- Verschillende Claude-fout-hints: 5 (meest: “Gevraagd is alleen de rente, niet het hele bedrag op de rekening.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-021` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Fatima zet €800 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt ze na één jaar?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** €240 → 1% van 800 is 8, niet 80. · €824 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €3 → 3% is een deel van €800, niet €3.
    - **Uitleg (Claude):** 1% van 800 is 8. 3% is 3 × 8 = €24.
  - `G8-VERH-E04-claude-bank-022` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Fatima zet €2000 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt ze na één jaar?
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** €600 → 1% van 2000 is 20, niet 200. · €2060 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €3 → 3% is een deel van €2.000, niet €3.
    - **Uitleg (Claude):** 1% van 2000 is 20. 3% is 3 × 20 = €60.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Bram zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Bram zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één jaar?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T6 (1) · regel: G8-T6-rente
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): komma-verschoven (1), getal-overgenomen (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “1% van 1500 is 15, niet 150.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-001` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Bram zet €1500 op een spaarrekening met 2% rente per jaar. Hoeveel rente krijgt hij na één jaar?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** €300 → 1% van 1500 is 15, niet 150. · €1530 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €2 → 2% is een deel van €1.500, niet €2.
    - **Uitleg (Claude):** 1% van 1500 is 15. 2% is 2 × 15 = €30.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Een zak noten kost na #% korting €#. Wat was de prijs vóór de korting?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Een zak noten kost na #% korting €#. Wat was de prijs vóór de korting?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: V6 (1) · regel: G8-P00-park-G7
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “De 50% ging van de óude prijs af, niet van €75. €75 is 50%.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-020` (Claude V6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een zak noten kost na 50% korting €75. Wat was de prijs vóór de korting?
    - **Antwoord:** 150  (controle: ok)
    - **Fout-hints (Claude):** €113 → De 50% ging van de óude prijs af, niet van €75. €75 is 50%. · €75 → Dat is de prijs ná de korting. Gevraagd is de prijs ervoor.
    - **Uitleg (Claude):** €75 is 50% van de oude prijs. 1% is 75 : 50 = 1,50, dus 100% is €150.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één jaar?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één jaar?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T6 (1) · regel: G8-T6-rente
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): komma-verschoven (1), getal-overgenomen (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “1% van 400 is 4, niet 40.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-023` (Claude T6, gegenereerd, niveau 1 → basis)
    - **Opgave:** Sanne zet €400 op een spaarrekening met 1% rente per jaar. Hoeveel rente krijgt ze na één jaar?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** €40 → 1% van 400 is 4, niet 40. · €404 → Gevraagd is alleen de rente, niet het hele bedrag op de rekening. · €1 → 1% is een deel van €400, niet €1.
    - **Uitleg (Claude):** 1% van 400 is 4. 1% is 1 × 4 = €4.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Van de # [ding] op school komt # procent met de fiets. Hoeveel kinderen komen er met de fiets?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Van de # [ding] op school komt # procent met de fiets. Hoeveel kinderen komen er met de fiets?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VERH
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “60 is het percentage en niet het aantal kinderen. Reken het uit met 150.”)
- Voorbeelden:
  - `G8-VERH-E04-claude-bank-032` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Van de 150 kinderen op school komt 60 procent met de fiets. Hoeveel kinderen komen er met de fiets?
    - **Opties:** A) 60 kinderen · B) 100 kinderen · C) 90 kinderen
    - **Antwoord:** 90 kinderen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 60 kinderen → 60 is het percentage en niet het aantal kinderen. Reken het uit met 150. · 100 kinderen → Je rekent met 100 kinderen. De school heeft een ander aantal leerlingen.
    - **Uitleg (Claude):** 10 procent van 150 is 15 kinderen. 60 procent is dan 6 x 15 = 90. Dus 90 kinderen komen met de fiets.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
