# G5-GET-M02 — Honderdtallen, tientallen, eenheden

Onze omschrijving: Honderdtallen–tientallen–eenheden; positiewaarde ≤1000 · in onze bank: 8 items

Claude-vragen gemapt: **12** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel honderdplaten leg je?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel honderdplaten leg je?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C1 (4) · regel: G5-G03-mab
- Getallenruimte: 0–1.000 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-GET-M02-claude-bank-004` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 192 met honderdplaten, tienstaven en losse blokjes. Hoeveel honderdplaten leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 192 is 1 honderd, 9 tien, 2 een. Leg eerst de grootste blokken.
  - `G5-GET-M02-claude-bank-002` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 864 met honderdplaten, tienstaven en losse blokjes. Hoeveel honderdplaten leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 864 is 8 honderd, 6 tien, 4 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Een honderdplaat is honderd blokjes. Hoeveel honderdtallen zitten er in het getal?
- **Hint 2 (te schrijven):** Kijk naar het eerste cijfer van het getal: dat zijn de honderdtallen.
- **Ouderzin:** Je kind legt een getal tot 1000 met honderdplaten, tienstaven en losse blokjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag is hoeveel honderdplaten je legt.  [nieuw]
  - `losse blokjes` (fout = eenheden van getal1) → Dat is het aantal losse blokjes. Een honderdplaat is honderd blokjes: kijk naar de honderdtallen.  [nieuw]
  - `andere fout` (andere fout) → Een honderdplaat is honderd blokjes. Kijk naar het cijfer van de honderdtallen: dat is het eerste cijfer.  [nieuw]
- Status: hints klaar

## Somtype 2: [tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel losse blokjes leg je?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel losse blokjes leg je?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C1 (4) · regel: G5-G03-mab
- Getallenruimte: 0–1.000 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-GET-M02-claude-bank-005` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 734 met honderdplaten, tienstaven en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 734 is 7 honderd, 3 tien, 4 een. Leg eerst de grootste blokken.
  - `G5-GET-M02-claude-bank-008` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 833 met honderdplaten, tienstaven en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 833 is 8 honderd, 3 tien, 3 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Eerst leg je de honderdplaten en de tienstaven. Hoeveel losse blokjes blijven er dan over?
- **Hint 2 (te schrijven):** Kijk naar het laatste cijfer van het getal: dat zijn de eenheden.
- **Ouderzin:** Je kind legt een getal tot 1000 met honderdplaten, tienstaven en losse blokjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag is hoeveel losse blokjes je legt.  [nieuw]
  - `andere fout` (andere fout) → Losse blokjes zijn de eenheden. Kijk naar het cijfer van de eenheden: dat is het laatste cijfer.  [nieuw]
- Status: hints klaar

## Somtype 3: [tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel tienstaven leg je?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[tienstaven/blokjes leggen] Leg # [ding] honderdplaten, tienstaven en losse blokjes. Hoeveel tienstaven leg je?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C1 (4) · regel: G5-G03-mab
- Getallenruimte: 0–1.000 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-GET-M02-claude-bank-011` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 658 met honderdplaten, tienstaven en losse blokjes. Hoeveel tienstaven leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 658 is 6 honderd, 5 tien, 8 een. Leg eerst de grootste blokken.
  - `G5-GET-M02-claude-bank-010` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Leg 172 met honderdplaten, tienstaven en losse blokjes. Hoeveel tienstaven leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 172 is 1 honderd, 7 tien, 2 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Een tienstaaf is tien blokjes. Eerst leg je de honderdplaten. Hoeveel tienstaven heb je daarna nog nodig?
- **Hint 2 (te schrijven):** Kijk naar het middelste cijfer van het getal: dat zijn de tientallen.
- **Ouderzin:** Je kind legt een getal tot 1000 met honderdplaten, tienstaven en losse blokjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag is hoeveel tienstaven je legt.  [nieuw]
  - `losse blokjes` (fout = eenheden van getal1) → Dat is het aantal losse blokjes. Een tienstaaf is tien blokjes: kijk naar de tientallen.  [nieuw]
  - `andere fout` (andere fout) → Een tienstaaf is tien blokjes. Kijk naar het cijfer van de tientallen: dat is het middelste cijfer.  [nieuw]
- Status: hints klaar
