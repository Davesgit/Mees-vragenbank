# G4-GET-M02 — Groepen van tien maken

Onze omschrijving: Hoeveelheden ≤100 structureren (groepen van 10) · in onze bank: 8 items

Claude-vragen gemapt: **12** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [tienstaven/blokjes leggen] Leg # [ding] tienstaven en losse blokjes. Hoeveel losse blokjes leg je?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[tienstaven/blokjes leggen] Leg # [ding] tienstaven en losse blokjes. Hoeveel losse blokjes leg je?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: D2-4 (7) · regel: G06-tienstaven
- Getallenruimte: 0–100 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G4-GET-M02-claude-bank-001` (Claude D2-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 98 met tienstaven en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 98 is 9 tien, 8 een. Leg eerst de grootste blokken.
  - `G4-GET-M02-claude-bank-007` (Claude D2-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 32 met tienstaven en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 32 is 3 tien, 2 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Een tienstaaf is tien blokjes. Wat over is, leg je als losse blokjes.
- **Hint 2 (te schrijven):** Het cijfer vooraan zegt hoeveel tienstaven je legt. Het cijfer achteraan zegt hoeveel losse blokjes je legt.
- **Ouderzin:** Je kind legt een getal tot 100 met tienstaven en losse blokjes en zegt hoeveel losse blokjes het zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag is hoeveel losse blokjes je legt, naast de tienstaven.  [nieuw]
  - `bijna` (fout ligt 1 naast het antwoord) → Bijna! Tel de losse blokjes nog eens. Kijk naar het cijfer achteraan.  [nieuw]
  - `andere fout` (andere fout) → Leg eerst zoveel tienstaven als je kunt. Hoeveel losse blokjes heb je dan nog nodig?  [nieuw]
- Status: hints klaar

## Somtype 2: [tienstaven/blokjes leggen] Leg # [ding] tienstaven en losse blokjes. Hoeveel tienstaven leg je?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[tienstaven/blokjes leggen] Leg # [ding] tienstaven en losse blokjes. Hoeveel tienstaven leg je?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: D2-4 (5) · regel: G06-tienstaven
- Getallenruimte: 0–100 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G4-GET-M02-claude-bank-009` (Claude D2-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 39 met tienstaven en losse blokjes. Hoeveel tienstaven leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 39 is 3 tien, 9 een. Leg eerst de grootste blokken.
  - `G4-GET-M02-claude-bank-008` (Claude D2-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 41 met tienstaven en losse blokjes. Hoeveel tienstaven leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 41 is 4 tien, 1 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Een tienstaaf is tien blokjes. Hoeveel tienstaven passen er in het getal?
- **Hint 2 (te schrijven):** Tel in sprongen van tien. Elke sprong is één tienstaaf. Stop als de volgende sprong te ver gaat.
- **Ouderzin:** Je kind legt een getal tot 100 met tienstaven en losse blokjes en zegt hoeveel tienstaven het zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. Eén tienstaaf is tien blokjes. Hoeveel tienstaven heb je nodig?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één tienstaaf te veel. Tel nog eens in sprongen van tien.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één tienstaaf te weinig. Tel nog eens in sprongen van tien.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar het cijfer vooraan. Dat zegt hoeveel tienstaven je legt.  [nieuw]
- Status: hints klaar
