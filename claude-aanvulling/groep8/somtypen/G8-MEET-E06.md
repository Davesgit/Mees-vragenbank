# G8-MEET-E06 — Tijdzones, tijdseenheden en de tijdbalk

Onze omschrijving: Tijd: tijdzones; grote↔kleine eenheden; geschiedenis/tijdbalk · in onze bank: 8 items

Claude-vragen gemapt: **32** in **12** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een vliegtuig vertrekt om #.# uur uit [plek]. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #.#.)

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #:#.)” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M26 (12) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (12), klok-verkeerd-gelezen (12)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de uren nog eens: je zit er een uur naast.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-007` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 8.15 uur uit het museum. De vlucht duurt 5 uur en 45 minuten. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 14.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 13.00 uur → Tel de uren nog eens: je zit er een uur naast. · 13.15 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 8.15 uur + 5 uur = 13.15 uur, + 45 minuten = 14.00 uur.
  - `G8-MEET-E06-claude-bank-004` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 9.00 uur uit de kleedkamer. De vlucht duurt 9 uur en 15 minuten. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 18.15 uur  (controle: ok)
    - **Fout-hints (Claude):** 17.15 uur → Tel de uren nog eens: je zit er een uur naast. · 18.00 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 9.00 uur + 9 uur = 18.00 uur, + 15 minuten = 18.15 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Een vliegtuig vertrekt om #.# uur uit [plek]. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **6** · Claude-doelen: M26 (6) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (6), verkeerde-bewerking (6)
- Verschillende Claude-fout-hints: 4 (meest: “Later betekent erbij, niet andersom.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-014` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 10.00 uur uit het nest. De vlucht duurt 10 uur en 30 minuten. Op de plek van aankomst is het 1 uur later dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 21.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 20.30 uur → Dat is de tijd thuis. Daar is het 1 uur later. · 19.30 uur → Later betekent erbij, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 20.30 uur. Daar is het 1 uur later: 21.30 uur.
  - `G8-MEET-E06-claude-bank-015` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 11.00 uur uit de kleedkamer. De vlucht duurt 5 uur en 30 minuten. Op de plek van aankomst is het 6 uur later dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 22.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 16.30 uur → Dat is de tijd thuis. Daar is het 6 uur later. · 10.30 uur → Later betekent erbij, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 16.30 uur. Daar is het 6 uur later: 22.30 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Een vliegtuig vertrekt om #.# uur uit [plek]. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M26 (4) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (4), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 3 (meest: “Vroeger betekent eraf, niet andersom.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-022` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 9.00 uur uit het museum. De vlucht duurt 6 uur en 30 minuten. Op de plek van aankomst is het 5 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 10.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 15.30 uur → Dat is de tijd thuis. Daar is het 5 uur vroeger. · 20.30 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 15.30 uur. Daar is het 5 uur vroeger: 10.30 uur.
  - `G8-MEET-E06-claude-bank-021` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 6.30 uur uit het bos. De vlucht duurt 6 uur en 45 minuten. Op de plek van aankomst is het 5 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 8.15 uur  (controle: ok)
    - **Fout-hints (Claude):** 13.15 uur → Dat is de tijd thuis. Daar is het 5 uur vroeger. · 18.15 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 13.15 uur. Daar is het 5 uur vroeger: 8.15 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Een vliegtuig vertrekt om #.# uur uit de school. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #.#.)

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit de school. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #:#.)” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M26 (2) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (2), klok-verkeerd-gelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de uren nog eens: je zit er een uur naast.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-028` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 7.30 uur uit de school. De vlucht duurt 11 uur en 45 minuten. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 19.15 uur  (controle: ok)
    - **Fout-hints (Claude):** 18.15 uur → Tel de uren nog eens: je zit er een uur naast. · 18.30 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 7.30 uur + 11 uur = 18.30 uur, + 45 minuten = 19.15 uur.
  - `G8-MEET-E06-claude-bank-029` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 7.15 uur uit de school. De vlucht duurt 7 uur en 45 minuten. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 15.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 14.00 uur → Tel de uren nog eens: je zit er een uur naast. · 14.15 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 7.15 uur + 7 uur = 14.15 uur, + 45 minuten = 15.00 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Een vliegtuig vertrekt om #.# uur uit [plek]. De vlucht duurt # uur. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 8 uur later.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-023` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 13.45 uur uit het nest. De vlucht duurt 4 uur. Op de plek van aankomst is het 8 uur later dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 1.45 uur  (controle: ok)
    - **Fout-hints (Claude):** 17.45 uur → Dat is de tijd thuis. Daar is het 8 uur later. · 9.45 uur → Later betekent erbij, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 17.45 uur. Daar is het 8 uur later: 1.45 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Een vliegtuig vertrekt om #.# uur uit [plek]. De vlucht duurt # uur. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 6 uur vroeger.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-024` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 9.45 uur uit het museum. De vlucht duurt 8 uur. Op de plek van aankomst is het 6 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 11.45 uur  (controle: ok)
    - **Fout-hints (Claude):** 17.45 uur → Dat is de tijd thuis. Daar is het 6 uur vroeger. · 23.45 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 17.45 uur. Daar is het 6 uur vroeger: 11.45 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Een vliegtuig vertrekt om #.# uur uit de klas. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 2 uur vroeger.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-025` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 9.30 uur uit de klas. De vlucht duurt 7 uur en 30 minuten. Op de plek van aankomst is het 2 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 15.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 17.00 uur → Dat is de tijd thuis. Daar is het 2 uur vroeger. · 19.00 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 17.00 uur. Daar is het 2 uur vroeger: 15.00 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Een vliegtuig vertrekt om #.# uur uit de klas. De vlucht duurt # uur. Hoe laat landt het? (Typ als #.#.)

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur. Hoe laat landt het? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), klok-verkeerd-gelezen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de uren nog eens: je zit er een uur naast.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-026` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 10.00 uur uit de klas. De vlucht duurt 2 uur. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 12.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 11.00 uur → Tel de uren nog eens: je zit er een uur naast. · 11.45 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 10.00 uur + 2 uur = 12.00 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Een vliegtuig vertrekt om #.# uur uit de klas. De vlucht duurt # uur. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 2 uur vroeger.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-027` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 11.45 uur uit de klas. De vlucht duurt 3 uur. Op de plek van aankomst is het 2 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 12.45 uur  (controle: ok)
    - **Fout-hints (Claude):** 14.45 uur → Dat is de tijd thuis. Daar is het 2 uur vroeger. · 16.45 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 14.45 uur. Daar is het 2 uur vroeger: 12.45 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Een vliegtuig vertrekt om #.# uur uit de school. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit de school. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur later dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 1 uur later.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-030` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 14.00 uur uit de school. De vlucht duurt 11 uur en 15 minuten. Op de plek van aankomst is het 1 uur later dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 2.15 uur  (controle: ok)
    - **Fout-hints (Claude):** 1.15 uur → Dat is de tijd thuis. Daar is het 1 uur later. · 0.15 uur → Later betekent erbij, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 1.15 uur. Daar is het 1 uur later: 2.15 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: Een vliegtuig vertrekt om #.# uur uit het huis. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #.#.)

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit het huis. De vlucht duurt # uur en # minuten. Hoe laat landt het? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), klok-verkeerd-gelezen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de uren nog eens: je zit er een uur naast.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-031` (Claude M26, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een vliegtuig vertrekt om 7.15 uur uit het huis. De vlucht duurt 11 uur en 30 minuten. Hoe laat landt het? (Typ als 14.30.)
    - **Antwoord:** 18.45 uur  (controle: ok)
    - **Fout-hints (Claude):** 17.45 uur → Tel de uren nog eens: je zit er een uur naast. · 18.15 uur → Vergeet de minuten niet.
    - **Uitleg (Claude):** 7.15 uur + 11 uur = 18.15 uur, + 30 minuten = 18.45 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: Een vliegtuig vertrekt om #.# uur uit het huis. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #.#.)

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een vliegtuig vertrekt om #:# uit het huis. De vlucht duurt # uur en # minuten. Op de plek van aankomst is het # uur vroeger dan thuis. Hoe laat is het daar bij de [ding]? (Typ als #:#.)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M26 (1) · regel: G8-M26-tijdzones
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tijd-als-kommagetal (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de tijd thuis. Daar is het 5 uur vroeger.”)
- Voorbeelden:
  - `G8-MEET-E06-claude-bank-032` (Claude M26, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een vliegtuig vertrekt om 14.15 uur uit het huis. De vlucht duurt 11 uur en 15 minuten. Op de plek van aankomst is het 5 uur vroeger dan thuis. Hoe laat is het daar bij de landing? (Typ als 14.30.)
    - **Antwoord:** 20.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 1.30 uur → Dat is de tijd thuis. Daar is het 5 uur vroeger. · 6.30 uur → Vroeger betekent eraf, niet andersom.
    - **Uitleg (Claude):** Thuis is het bij de landing 1.30 uur. Daar is het 5 uur vroeger: 20.30 uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
