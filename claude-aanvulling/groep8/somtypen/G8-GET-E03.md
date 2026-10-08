# G8-GET-E03 — Welke som eerst? Volgorde en haakjes

Onze omschrijving: Volgorde van bewerkingen + haakjes; eigenschappen bewerkingen · in onze bank: 8 items

Claude-vragen gemapt: **64** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Reken uit: (# + #) × #

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Reken uit: (# + #) × #” (koppeling: claudeId)
- Items: **21** · Claude-doelen: T2 (21) · regel: G8-T2-haakjes
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (21), optellen-ipv-vermenigvuldigen (21)
- Verschillende Claude-fout-hints: 2 (meest: “De haakjes gaan voor: eerst optellen, dan vermenigvuldigen.”)
- Voorbeelden:
  - `G8-GET-E03-claude-bank-063` (Claude T2, gegenereerd, niveau 1 → basis)
    - **Opgave:** Reken uit: (11 + 5) × 4
    - **Antwoord:** 64  (controle: ok)
    - **Fout-hints (Claude):** 31 → De haakjes gaan voor: eerst optellen, dan vermenigvuldigen. · 20 → Na de haakjes komt een keersom.
    - **Uitleg (Claude):** Eerst de haakjes: 11 + 5 = 16. Dan keer: 16 × 4 = 64.
  - `G8-GET-E03-claude-bank-060` (Claude T2, gegenereerd, niveau 1 → basis)
    - **Opgave:** Reken uit: (5 + 7) × 7
    - **Antwoord:** 84  (controle: ok)
    - **Fout-hints (Claude):** 54 → De haakjes gaan voor: eerst optellen, dan vermenigvuldigen. · 19 → Na de haakjes komt een keersom.
    - **Uitleg (Claude):** Eerst de haakjes: 5 + 7 = 12. Dan keer: 12 × 7 = 84.

- **Hint 1 (te schrijven):** Wat tussen haakjes staat, reken je altijd eerst uit.
- **Hint 2 (te schrijven):** Tel eerst de twee getallen tussen de haakjes op. Doe die uitkomst daarna keer het getal achter de haakjes.
- **Ouderzin:** Je kind oefent de rekenvolgorde: wat tussen haakjes staat, gaat altijd eerst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `haakjes overgeslagen` (Claudes sleutel: verkeerde-bewerking) → Heb je eerst keer gedaan? Wat tussen haakjes staat, reken je eerst uit, ook als er een keerteken staat.  [Claude, taalfix]
  - `alles opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je alles opgeteld? Achter de haakjes staat een keerteken (×).  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst uit wat tussen de haakjes staat, en doe dat daarna keer het getal achter de haakjes.  [nieuw]
- Status: hints klaar

## Somtype 2: Reken uit. # : # + #

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Reken uit. # : # + #” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C21 (12) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (13)
- Verschillende Claude-fout-hints: 2 (meest: “Delen gaat vóór plus. Deel eerst, tel daarna op.”)
- Voorbeelden:
  - `G8-GET-E03-claude-bank-026` (Claude C21, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 12 : 3 + 5
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 1,5 → Delen gaat vóór plus. Deel eerst, tel daarna op. · 17 → Er staat een deelteken: eerst delen, dan pas optellen.
    - **Uitleg (Claude):** Eerst delen: 12 : 3 = 4. Dan 4 + 5 = 9.
  - `G8-GET-E03-claude-bank-024` (Claude C21, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 42 : 7 + 9
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** 2,6 → Delen gaat vóór plus. Deel eerst, tel daarna op. · 51 → Er staat een deelteken: eerst delen, dan pas optellen.
    - **Uitleg (Claude):** Eerst delen: 42 : 7 = 6. Dan 6 + 9 = 15.

- **Hint 1 (te schrijven):** De dubbele punt (:) betekent gedeeld door. Delen gaat vóór optellen, als er geen haakjes staan.
- **Hint 2 (te schrijven):** Reken eerst de deelsom uit. Tel daarna het getal achter het plusteken erbij.
- **Ouderzin:** Je kind oefent de rekenvolgorde: delen gaat vóór optellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `volgorde` (Claudes sleutel: verkeerde-bewerking) → Delen gaat vóór optellen: reken eerst de deelsom uit, en tel daarna het getal achter het plusteken erbij.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst de deelsom uit, en tel daarna het getal achter het plusteken erbij.  [nieuw]
- Status: hints klaar

## Somtype 3: Reken uit. # + # × (# − #)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Reken uit. # + # × (# − #)” (koppeling: claudeId)
- Items: **11** · Claude-doelen: T2 (11) · regel: G8-T2-haakjes
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (22)
- Verschillende Claude-fout-hints: 2 (meest: “Alleen wat tussen de haakjes staat reken je eerst. Daarna keer, dan plus.”)
- Voorbeelden:
  - `G8-GET-E03-claude-bank-015` (Claude T2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 3 + 7 × (8 − 5)
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 30 → Alleen wat tussen de haakjes staat reken je eerst. Daarna keer, dan plus. · 54 → De haakjes horen bij elkaar: reken eerst ${d} − ${e} uit.
    - **Uitleg (Claude):** Eerst de haakjes: 8 − 5 = 3. Dan keer: 7 × 3 = 21. Dan plus: 3 + 21 = 24.
  - `G8-GET-E03-claude-bank-020` (Claude T2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 11 + 8 × (6 − 2)
    - **Antwoord:** 43  (controle: ok)
    - **Fout-hints (Claude):** 76 → Alleen wat tussen de haakjes staat reken je eerst. Daarna keer, dan plus. · 57 → De haakjes horen bij elkaar: reken eerst ${d} − ${e} uit.
    - **Uitleg (Claude):** Eerst de haakjes: 6 − 2 = 4. Dan keer: 8 × 4 = 32. Dan plus: 11 + 32 = 43.

- **Hint 1 (te schrijven):** Eerst reken je uit wat tussen haakjes staat, dan keer, en pas daarna plus.
- **Hint 2 (te schrijven):** Reken eerst de minsom tussen de haakjes uit. Doe daarna het getal vóór de haakjes keer die uitkomst. Tel pas daarna het getal vóór het plusteken erbij.
- **Ouderzin:** Je kind oefent de rekenvolgorde: eerst haakjes, dan keer, dan plus.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `volgorde` (Claudes sleutel: verkeerde-bewerking) → Let op de volgorde: eerst wat tussen haakjes staat, dan keer, en pas daarna plus.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eerst haakjes, dan keer, dan plus.  [nieuw]
- Status: hints klaar

## Somtype 4: Reken uit. # − # × #

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Reken uit. # − # × #” (koppeling: claudeId)
- Items: **11** · Claude-doelen: C21 (11) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (11), optellen-ipv-vermenigvuldigen (11)
- Verschillende Claude-fout-hints: 2 (meest: “Keer gaat vóór min. Eerst de keersom, dan pas aftrekken.”)
- Voorbeelden:
  - `G8-GET-E03-claude-bank-040` (Claude C21, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 52 − 5 × 6
    - **Antwoord:** 22  (controle: ok)
    - **Fout-hints (Claude):** 282 → Keer gaat vóór min. Eerst de keersom, dan pas aftrekken. · 41 → Er staat een keerteken: eerst vermenigvuldigen, dan pas aftrekken.
    - **Uitleg (Claude):** Eerst vermenigvuldigen: 5 × 6 = 30. Dan 52 − 30 = 22.
  - `G8-GET-E03-claude-bank-043` (Claude C21, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Reken uit. 28 − 6 × 3
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 66 → Keer gaat vóór min. Eerst de keersom, dan pas aftrekken. · 19 → Er staat een keerteken: eerst vermenigvuldigen, dan pas aftrekken.
    - **Uitleg (Claude):** Eerst vermenigvuldigen: 6 × 3 = 18. Dan 28 − 18 = 10.

- **Hint 1 (te schrijven):** Keer gaat vóór min, als er geen haakjes staan.
- **Hint 2 (te schrijven):** Reken eerst de keersom uit. Haal die uitkomst daarna af van het getal vóór het minteken.
- **Ouderzin:** Je kind oefent de rekenvolgorde: keer gaat vóór min.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eerst min` (Claudes sleutel: verkeerde-bewerking) → Heb je eerst min gedaan? Keer gaat vóór min.  [Claude, taalfix]
  - `opgeteld bij het keerteken` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je de twee getallen bij het keerteken opgeteld? Daar staat keer (×): reken die keersom eerst uit.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst de keersom uit, en haal die uitkomst daarna af van het getal vóór het minteken.  [nieuw]
- Status: hints klaar

## Somtype 5: Reken uit. # + # × #

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Reken uit. # + # × #” (koppeling: claudeId)
- Items: **9** · Claude-doelen: C21 (9) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (9), optellen-ipv-vermenigvuldigen (9)
- Verschillende Claude-fout-hints: 2 (meest: “Keer gaat vóór plus. Reken eerst de keersom uit, ook al staat hij achteraan.”)
- Voorbeelden:
  - `G8-GET-E03-claude-bank-003` (Claude C21, gegenereerd, niveau 1 → basis)
    - **Opgave:** Reken uit. 7 + 7 × 6
    - **Antwoord:** 49  (controle: ok)
    - **Fout-hints (Claude):** 84 → Keer gaat vóór plus. Reken eerst de keersom uit, ook al staat hij achteraan. · 20 → Er staat een keerteken: eerst vermenigvuldigen, dan pas optellen.
    - **Uitleg (Claude):** Eerst vermenigvuldigen, dan optellen: 7 × 6 = 42, dan 7 + 42 = 49.
  - `G8-GET-E03-claude-bank-002` (Claude C21, gegenereerd, niveau 1 → basis)
    - **Opgave:** Reken uit. 6 + 9 × 4
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 60 → Keer gaat vóór plus. Reken eerst de keersom uit, ook al staat hij achteraan. · 19 → Er staat een keerteken: eerst vermenigvuldigen, dan pas optellen.
    - **Uitleg (Claude):** Eerst vermenigvuldigen, dan optellen: 9 × 4 = 36, dan 6 + 36 = 42.

- **Hint 1 (te schrijven):** Keer gaat vóór plus, als er geen haakjes staan.
- **Hint 2 (te schrijven):** Reken eerst de keersom uit. Tel daarna het getal vóór het plusteken erbij.
- **Ouderzin:** Je kind oefent de rekenvolgorde: keer gaat vóór plus.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eerst plus` (Claudes sleutel: verkeerde-bewerking) → Heb je eerst opgeteld? Keer gaat vóór plus.  [Claude, taalfix]
  - `alles opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je alles opgeteld? Er staat ook een keerteken (×).  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst de keersom uit, en tel daarna het getal vóór het plusteken erbij.  [nieuw]
- Status: hints klaar
