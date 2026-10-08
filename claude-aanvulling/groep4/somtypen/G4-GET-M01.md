# G4-GET-M01 — Springen met 2, 5 en 10

Onze omschrijving: Tellen/terug ±100 met sprongen 2, 5, 10 · in onze bank: 8 items

Claude-vragen gemapt: **306** in **23** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 2

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 2” (koppeling: claudeId)
- Items: **40** · Claude-doelen: D2-3 (40) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 39 items · rijGroep per item
- Denkfouten (Claude): None (80)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-160` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 96, 94, 92, 90, □
    - **Antwoord:** 88  (controle: ok)
    - **Fout-hints (Claude):** 86 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 90 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-138` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 62, 60, 58, 56, □
    - **Antwoord:** 54  (controle: ok)
    - **Fout-hints (Claude):** 55 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 52 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 2) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 2: Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 2

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 2” (koppeling: claudeId)
- Items: **40** · Claude-doelen: D1-7 (40) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 40 items · rijGroep per item
- Denkfouten (Claude): None (80)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-371` (Claude D1-7, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 14, □, 18, 20, 22
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 22 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 18 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-271` (Claude D1-7, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 32, □, 36, 38, 40
    - **Antwoord:** 34  (controle: ok)
    - **Fout-hints (Claude):** 40 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 36 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omhoog, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord − 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 3: Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 2

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 2” (koppeling: claudeId)
- Items: **40** · Claude-doelen: D2-3 (40) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 40 items · rijGroep per item
- Denkfouten (Claude): None (80)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-470` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 100, □, 96, 94, 92
    - **Antwoord:** 98  (controle: ok)
    - **Fout-hints (Claude):** 99 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 100 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-480` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 60, 58, □, 54, 52
    - **Antwoord:** 56  (controle: ok)
    - **Fout-hints (Claude):** 57 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 58 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omlaag, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij die terugtelt met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord + 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 4: Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 2

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 2” (koppeling: claudeId)
- Items: **39** · Claude-doelen: D1-7 (38), D0-3 (1) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Denkfouten (Claude): None (78)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-070` (Claude D0-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 14, 16, 18, 20, □
    - **Antwoord:** 22  (controle: ok)
    - **Fout-hints (Claude):** 24 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 18 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-106` (Claude D1-7, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 32, 34, 36, 38, □
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 39 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 38 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 2) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 5: Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 10

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 10” (koppeling: claudeId)
- Items: **24** · Claude-doelen: D2-3 (18), D1-7 (6) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 21 items · rijGroep per item
- Denkfouten (Claude): None (48)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-201` (Claude D1-7, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 10, □, 30, 40, 50
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 11 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-210` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 6, 16, □, 36, 46
    - **Antwoord:** 26  (controle: ok)
    - **Fout-hints (Claude):** 6 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 20 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omhoog, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord − 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 6: Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 10

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 10” (koppeling: claudeId)
- Items: **20** · Claude-doelen: D2-3 (15), D1-7 (5) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 2 items · rijGroep per item
- Denkfouten (Claude): None (40)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-052` (Claude D1-7, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 10, 20, 30, 40, □
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 60 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 30 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-068` (Claude D2-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 6, 16, 26, 36, □
    - **Antwoord:** 46  (controle: ok)
    - **Fout-hints (Claude):** 37 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 56 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 10) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 7: Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 5

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — sprongen van 5” (koppeling: claudeId)
- Items: **16** · Claude-doelen: D1-7 (16) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 16 items · rijGroep per item
- Denkfouten (Claude): None (32)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-415` (Claude D1-7, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 25, 30, □, 40, 45
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** 45 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 40 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-393` (Claude D1-7, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 45, 50, 55, □, 65
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** 50 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 65 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omhoog, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord − 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 8: Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 5

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 5” (koppeling: claudeId)
- Items: **16** · Claude-doelen: D2-3 (16) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 16 items · rijGroep per item
- Denkfouten (Claude): None (32)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-592` (Claude D2-3, bank, niveau 2 → kritisch)
    - **Opgave:** Welk getal past op de lege plek? 100, □, 90, 85, 80
    - **Antwoord:** 95  (controle: ok)
    - **Fout-hints (Claude):** 99 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 100 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-575` (Claude D2-3, bank, niveau 2 → kritisch)
    - **Opgave:** Welk getal past op de lege plek? 60, 55, □, 45, 40
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 60 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 45 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omlaag, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij die terugtelt met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord + 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 9: Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 5

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — sprongen van 5” (koppeling: claudeId)
- Items: **15** · Claude-doelen: D1-7 (14), D0-3 (1) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 2 items · rijGroep per item
- Denkfouten (Claude): None (30)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-109` (Claude D0-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 5, 10, 15, 20, □
    - **Antwoord:** 25  (controle: ok)
    - **Fout-hints (Claude):** 30 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 15 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-110` (Claude D1-7, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 35, 40, 45, 50, □
    - **Antwoord:** 55  (controle: ok)
    - **Fout-hints (Claude):** 51 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 50 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel komt er steeds bij?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 5) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 10: Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 5

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 5” (koppeling: claudeId)
- Items: **15** · Claude-doelen: D2-3 (15) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 14 items · rijGroep per item
- Denkfouten (Claude): None (30)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-169` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 100, 95, 90, 85, □
    - **Antwoord:** 80  (controle: ok)
    - **Fout-hints (Claude):** 75 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 85 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-172` (Claude D2-3, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal past op de lege plek? 60, 55, 50, 45, □
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 44 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 50 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 5) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 11: Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 2

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 2” (koppeling: claudeId)
- Items: **7** · Claude-doelen: D0-3 (5), G10 (2) · regel: D-sprongen
- Getallenruimte: 0–10, 0–20 · type: invullen
- Denkfouten (Claude): None (10), een-ernaast (4), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-017` (Claude D0-3, bank, niveau 3 → basis)
    - **Opgave:** Tel terug met sprongen van 2. 20, 18, 16, 14, □
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 13 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-021` (Claude G10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel terug met sprongen van 2. 10, 8, 6, 4, □
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 6 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 1 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 3 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** Je springt steeds 2 omlaag. Na 4 komt 2.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 1) → Je bent maar een klein stapje teruggegaan. Kijk hoe groot de sprongen in de rij zijn.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 2) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord − 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 12: Tel terug met sprongen van #. [rij, □ ertussen] — terug sprongen van 2

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ ertussen] — terug sprongen van 2” (koppeling: claudeId)
- Items: **6** · Claude-doelen: D0-3 (6) · regel: D-sprongen
- Getallenruimte: 0–10, 0–20 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 6 items · rijGroep per item
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-046` (Claude D0-3, bank, niveau 3 → basis)
    - **Opgave:** Tel terug met sprongen van 2. 20, 18, 16, □, 12
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 18 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 16 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-043` (Claude D0-3, bank, niveau 3 → basis)
    - **Opgave:** Tel terug met sprongen van 2. 10, □, 6, 4, 2
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 9 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 12 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omlaag, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij die terugtelt met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord + 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 13: Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 10

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ ertussen] — terug sprongen van 10” (koppeling: claudeId)
- Items: **6** · Claude-doelen: D2-3 (6) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 6 items · rijGroep per item
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-428` (Claude D2-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 100, 90, 80, □, 60
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 80 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 60 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-436` (Claude D2-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 70, 60, 50, □, 30
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 60 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 50 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het getal vóór de lege plek. Maak één sprong omlaag, net zo groot als de andere sprongen. Met nog zo'n sprong kom je op het getal na de lege plek. Zo kun je het controleren. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind vult het getal in dat ontbreekt in een rij die terugtelt met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het getal vóór de lege plek. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `verkeerde kant op` (fout = antwoord + 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het getal vóór de lege plek precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 14: Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 10

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Welk getal past op de lege plek? [rij, □ achteraan] — terug sprongen van 10” (koppeling: claudeId)
- Items: **5** · Claude-doelen: D2-3 (5) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 4 items · rijGroep per item
- Denkfouten (Claude): None (10)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-125` (Claude D2-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 100, 90, 80, 70, □
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** 80 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 70 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G4-GET-M01-claude-bank-126` (Claude D2-3, bank, niveau 2 → basis)
    - **Opgave:** Welk getal past op de lege plek? 70, 60, 50, 40, □
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** 39 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 20 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Kijk naar de getallen in de rij. Hoeveel gaat er steeds af?
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [nieuw]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 10) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 15: Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 10

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 10” (koppeling: claudeId)
- Items: **4** · Claude-doelen: G10 (4) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 1 items · rijGroep per item
- Denkfouten (Claude): een-ernaast (8), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-011` (Claude G10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel terug met sprongen van 10. 50, 40, 30, 20, □
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 30 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 9 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 19 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 10 omlaag. Na 20 komt 10.
  - `G4-GET-M01-claude-bank-015` (Claude G10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Tel terug met sprongen van 10. 44, 34, 24, 14, □
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 24 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 3 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 13 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 10 omlaag. Na 14 komt 4.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 10) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord − 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 16: Tel met sprongen van #. [rij, □ achteraan] — sprongen van 4

- Sleutel: nrOrigineel **16** · somtypeOrigineel “Tel met sprongen van #. [rij, □ achteraan] — sprongen van 4” (koppeling: claudeId)
- Items: **3** · Claude-doelen: G10 (3) · regel: D-sprongen, G01-sprongen
- Getallenruimte: 0–100, 0–20 · type: invullen
- Merge-fixlijst: #19 rij +2 verschoven naar de tafelrij (2), #19 rij +9 verschoven naar de tafelrij (1)
- Denkfouten (Claude): een-ernaast (6), verkeerde-bewerking (3)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-006` (Claude G10, gegenereerd, niveau 2 → kritisch)
    - **Opgave:** Tel met sprongen van 4. 4, 8, 12, 16, □
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 10 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 19 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 15 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 4 omhoog. Het getal op de lege plek is 20.
  - `G4-GET-M01-claude-bank-007` (Claude G10, gegenereerd, niveau 2 → kritisch)
    - **Opgave:** Tel met sprongen van 4. 8, 12, 16, 20, □
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 14 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 23 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 19 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 4 omhoog. Het getal op de lege plek is 24.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omhoog.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 4.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 8) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 3) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 4) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord + 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 17: Tel met sprongen van #. [rij, □ achteraan] — sprongen van 10

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Tel met sprongen van #. [rij, □ achteraan] — sprongen van 10” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G10 (2) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Denkfouten (Claude): een-ernaast (4), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-001` (Claude G10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel met sprongen van 10. 10, 20, 30, 40, □
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 30 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 51 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 41 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 10 omhoog. Na 40 komt 50.
  - `G4-GET-M01-claude-bank-002` (Claude G10, gegenereerd, niveau 2 → basis)
    - **Opgave:** Tel met sprongen van 10. 5, 15, 25, 35, □
    - **Antwoord:** 45  (controle: ok)
    - **Fout-hints (Claude):** 25 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 46 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 36 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 10 omhoog. Na 35 komt 45.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omhoog.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen. Het cijfer achteraan blijft steeds hetzelfde.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 20) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 9) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 10) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord + 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 18: Tel met sprongen van #. [rij, □ achteraan] — sprongen van 2

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Tel met sprongen van #. [rij, □ achteraan] — sprongen van 2” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G10 (2) · regel: D-sprongen
- Getallenruimte: 0–20 · type: invullen
- Denkfouten (Claude): een-ernaast (4), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-004` (Claude G10, gegenereerd, niveau 2 → basis)
    - **Opgave:** Tel met sprongen van 2. 5, 7, 9, 11, □
    - **Antwoord:** 13  (controle: ok)
    - **Fout-hints (Claude):** 9 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 14 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 12 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** Je springt steeds 2 omhoog. Na 11 komt 13.
  - `G4-GET-M01-claude-bank-003` (Claude G10, gegenereerd, niveau 2 → basis)
    - **Opgave:** Tel met sprongen van 2. 3, 5, 7, 9, □
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 7 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 12 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 10 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** Je springt steeds 2 omhoog. Na 9 komt 11.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omhoog.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 2.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 4) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 1) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 2) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord + 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 19: Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 5

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 5” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G10 (2) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Merge-fixlijst: #19 rij +1 verschoven naar de tafelrij (1)
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 1 items · rijGroep per item
- Denkfouten (Claude): een-ernaast (4), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-030` (Claude G10, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** Tel terug met sprongen van 5. 25, 20, 15, 10, □
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 15 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 4 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 9 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 5 omlaag. Na 10 komt 5.
  - `G4-GET-M01-claude-bank-029` (Claude G10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Tel terug met sprongen van 5. 30, 25, 20, 15, □
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 19 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 8 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 13 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 5 omlaag. Het getal op de lege plek is 10.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 5) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord − 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 20: Tel met sprongen van #. [rij, □ achteraan] — sprongen van 3

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Tel met sprongen van #. [rij, □ achteraan] — sprongen van 3” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G10 (1) · regel: D-sprongen
- Getallenruimte: 0–20 · type: invullen
- Merge-fixlijst: #19 rij -2 verschoven naar de tafelrij (1)
- Denkfouten (Claude): een-ernaast (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-005` (Claude G10, gegenereerd, niveau 2 → kritisch)
    - **Opgave:** Tel met sprongen van 3. 3, 6, 9, 12, □
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** 11 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 18 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 15 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 3 omhoog. Het getal op de lege plek is 15.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omhoog.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 3.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 6) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 2) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 3) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord + 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 21: Tel met sprongen van #. [rij, □ achteraan] — sprongen van 5

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Tel met sprongen van #. [rij, □ achteraan] — sprongen van 5” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G10 (1) · regel: G01-sprongen
- Getallenruimte: 0–100 · type: invullen
- Denkfouten (Claude): een-ernaast (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-009` (Claude G10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel met sprongen van 5. 5, 10, 15, 20, □
    - **Antwoord:** 25  (controle: ok)
    - **Fout-hints (Claude):** 15 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omhoog. · 26 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 21 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** De rij gaat steeds 5 omhoog. Na 20 komt 25.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omhoog.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omhoog, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij met sprongen van 5.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord − 10) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omhoog. Spring dus ook omhoog.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omhoog.  [nieuw]
  - `sprong van 1` (fout = antwoord − 4) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord + 5) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord + 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 22: Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 3

- Sleutel: nrOrigineel **22** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 3” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G10 (1) · regel: D-sprongen
- Getallenruimte: 0–20 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 1 items · rijGroep per item
- Denkfouten (Claude): een-ernaast (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-024` (Claude G10, gegenereerd, niveau 1 → kritisch)
    - **Opgave:** Tel terug met sprongen van 3. 15, 12, 9, 6, □
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 9 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 2 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 5 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** Je springt steeds 3 omlaag. Na 6 komt 3.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 3.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 6) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 2) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 3) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord − 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar

## Somtype 23: Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 4

- Sleutel: nrOrigineel **23** · somtypeOrigineel “Tel terug met sprongen van #. [rij, □ achteraan] — terug sprongen van 4” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G10 (1) · regel: D-sprongen
- Getallenruimte: 0–20 · type: invullen
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 1 items · rijGroep per item
- Denkfouten (Claude): een-ernaast (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag.”)
- Voorbeelden:
  - `G4-GET-M01-claude-bank-025` (Claude G10, gegenereerd, niveau 1 → kritisch)
    - **Opgave:** Tel terug met sprongen van 4. 20, 16, 12, 8, □
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 12 → Kijk of de rij omhoog of omlaag gaat. Deze gaat omlaag. · 3 → Kijk hoe groot de sprong tussen twee getallen naast elkaar is, en maak vanaf het laatste getal precies zo'n sprong. · 7 → De sprong is niet 1. Kijk naar het verschil tussen twee getallen in de rij.
    - **Uitleg (Claude):** Je springt steeds 4 omlaag. Na 8 komt 4.

- **Hint 1 (te schrijven):** In de vraag staat hoe groot elke sprong is. De rij gaat omlaag.
- **Hint 2 (te schrijven):** Begin bij het laatste getal. Maak nog één sprong omlaag, net zo groot als de andere sprongen.
- **Ouderzin:** Je kind zoekt het volgende getal in een rij die terugtelt met sprongen van 4.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde kant op` (fout = antwoord + 8) → Kijk of de rij omhoog of omlaag gaat. Deze rij gaat omlaag. Spring dus ook omlaag.  [Claude, taalfix]
  - `getal vóór de lege plek` (fout = laatste getal van de rij) → Dat is het laatste getal van de rij. Maak vanaf dat getal nog één sprong omlaag.  [nieuw]
  - `sprong van 1` (fout = antwoord + 3) → De sprong is niet 1. Kijk hoe groot de sprong is van het ene getal naar het volgende.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort op de lege plek?  [nieuw]
  - `een sprong te ver` (fout = antwoord − 4) → Dat is een sprong te ver. Maak vanaf het laatste getal maar één sprong.  [nieuw]
  - `net naast` (fout = antwoord − 1) → Bijna! Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens hoe groot de sprong is. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoe groot de sprong is van het ene getal naar het volgende. Maak vanaf het laatste getal precies zo'n sprong.  [nieuw]
- Status: hints klaar
