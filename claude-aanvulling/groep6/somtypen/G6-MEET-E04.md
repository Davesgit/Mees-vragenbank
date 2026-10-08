# G6-MEET-E04 — Liter omrekenen naar dl, cl en ml

Onze omschrijving: dl/cl + herleiden L↔dl/cl/ml; komma-notatie inhoud · in onze bank: 8 items

Claude-vragen gemapt: **120** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # L = □ cl

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# L = □ cl” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M12 (40) · regel: G6-M04-herleiden
- Getallenruimte: 0–1.000, 0–10.000 · type: invullen
- Uit de G5-park: 40 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (59), getal-overgenomen (21)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E04-claude-bank-011` (Claude M12, bank, niveau 2 → toepassen)
    - **Opgave:** 2 L = □ cl
    - **Antwoord:** 200  (controle: ok)
    - **Fout-hints (Claude):** 4 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 20 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E04-claude-bank-008` (Claude M12, bank, niveau 2 → toepassen)
    - **Opgave:** 22 L = □ cl
    - **Antwoord:** 2200  (controle: ok)
    - **Fout-hints (Claude):** 220 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 22 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén liter (L) is honderd centiliter (cl). Een centiliter is kleiner dan een liter, dus het getal wordt groter.
- **Hint 2 (te schrijven):** Doe het aantal liter keer honderd: schrijf er twee nullen achter.
- **Ouderzin:** Je kind rekent inhoudsmaten om: van liter naar centiliter (keer honderd).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Eén liter is honderd centiliter: doe keer honderd.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Je hebt keer duizend gedaan. Eén liter is honderd centiliter: doe keer honderd.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Heb je helemaal omgerekend naar centiliter? Eén liter is honderd centiliter: doe keer honderd.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Eén liter is honderd centiliter: doe keer honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter (L) is honderd centiliter (cl). Doe het aantal liter keer honderd.  [nieuw]
- Status: hints klaar

## Somtype 2: # cl = □ L

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# cl = □ L” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M12 (40) · regel: G6-M04-herleiden
- Getallenruimte: 0–10.000, 0–100.000 · type: invullen
- Uit de G5-park: 40 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (53), getal-overgenomen (27)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E04-claude-bank-099` (Claude M12, bank, niveau 2 → toepassen)
    - **Opgave:** 2000 cl = □ L
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G6-MEET-E04-claude-bank-075` (Claude M12, bank, niveau 2 → toepassen)
    - **Opgave:** 22.000 cl = □ L
    - **Antwoord:** 220  (controle: ok)
    - **Fout-hints (Claude):** 22 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 22.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén liter (L) is honderd centiliter (cl). Een liter is groter dan een centiliter, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal centiliter door honderd: haal er twee nullen af.
- **Ouderzin:** Je kind rekent inhoudsmaten om: van centiliter naar liter (gedeeld door honderd).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Honderd centiliter is één liter: deel door honderd.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar liter? Honderd centiliter is één liter: deel door honderd.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Je hebt door duizend gedeeld. Honderd centiliter is één liter: deel door honderd.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Honderd centiliter is één liter: deel door honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter (L) is honderd centiliter (cl). Deel het aantal centiliter door honderd.  [nieuw]
- Status: hints klaar

## Somtype 3: # L = □ ml

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# L = □ ml” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M12 (31) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (39), getal-overgenomen (23)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E04-claude-bank-042` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 11 L = □ ml
    - **Antwoord:** 11.000  (controle: ok)
    - **Fout-hints (Claude):** 33 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 11 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G6-MEET-E04-claude-bank-067` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 27 L = □ ml
    - **Antwoord:** 27.000  (controle: ok)
    - **Fout-hints (Claude):** 270.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 27 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén liter (L) is duizend milliliter (ml). Een milliliter is kleiner dan een liter, dus het getal wordt groter.
- **Hint 2 (te schrijven):** Doe het aantal liter keer duizend: schrijf er drie nullen achter.
- **Ouderzin:** Je kind rekent inhoudsmaten om: van liter naar milliliter (keer duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Eén liter is duizend milliliter: doe keer duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Eén liter is duizend milliliter: doe keer duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Heb je helemaal omgerekend naar milliliter? Eén liter is duizend milliliter: doe keer duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Eén liter is duizend milliliter: doe keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter (L) is duizend milliliter (ml). Doe het aantal liter keer duizend.  [nieuw]
- Status: hints klaar

## Somtype 4: # ml = □ L

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# ml = □ L” (koppeling: claudeId)
- Items: **9** · Claude-doelen: M12 (9) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 9 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (13), getal-overgenomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E04-claude-bank-120` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 20.000 ml = □ L
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E04-claude-bank-112` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 70.000 ml = □ L
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 70.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén liter (L) is duizend milliliter (ml). Een liter is groter dan een milliliter, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal milliliter door duizend: haal er drie nullen af.
- **Ouderzin:** Je kind rekent inhoudsmaten om: van milliliter naar liter (gedeeld door duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Duizend milliliter is één liter: deel door duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar liter? Duizend milliliter is één liter: deel door duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Duizend milliliter is één liter: deel door duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Duizend milliliter is één liter: deel door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter (L) is duizend milliliter (ml). Deel het aantal milliliter door duizend.  [nieuw]
- Status: hints klaar
