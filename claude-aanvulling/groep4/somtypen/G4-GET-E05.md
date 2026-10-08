# G4-GET-E05 — Schatten met plus en min

Onze omschrijving: Schattend +/− ≤100; kritisch redeneren +/− · in onze bank: 8 items

Claude-vragen gemapt: **37** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: T3 (12) · regel: D8-SCHAT-NAAR-G4
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-001` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 16 + 31 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 50  (controle: n.v.t.)
    - **Fout-hints (Claude):** 51 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 60 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G4-GET-E05-claude-bank-naar-007` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 18 + 58 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 80  (controle: n.v.t.)
    - **Fout-hints (Claude):** 76 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Hoeveel is # − # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-SCHAT-NAAR-G4
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-013` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 44 − 20 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 40 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G4-GET-E05-claude-bank-naar-017` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 54 − 32 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 22 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 40 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-NAAR-G4
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (7), bovengrens (4), laatste-cijfer (3), ondergrens (2)
- Verschillende Claude-fout-hints: 16 (meest: “Rond allebei naar boven af. 40 + 40 is 80. De uitkomst kan dus niet groter zijn dan 80, en 84 is groter.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-021` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 39 + 35 kan kloppen?
    - **Opties:** A) 74 · B) 84 · C) 4
    - **Antwoord:** 74  (controle: n.v.t.)
    - **Fout-hints (Claude):** 84 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G4-GET-E05-claude-bank-naar-025` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 41 + 32 kan kloppen?
    - **Opties:** A) 73 · B) 730 · C) 71
    - **Antwoord:** 73  (controle: n.v.t.)
    - **Fout-hints (Claude):** 83 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-NAAR-G4
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): bovengrens (6), laatste-cijfer (6), orde-van-grootte (4)
- Verschillende Claude-fout-hints: 16 (meest: “Rond 88 naar boven af en 33 naar beneden. 90 − 30 is 60. De uitkomst kan dus niet groter zijn dan 60, en 65 is groter.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-029` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 88 − 33 kan kloppen?
    - **Opties:** A) 55 · B) 65 · C) 57
    - **Antwoord:** 55  (controle: n.v.t.)
    - **Fout-hints (Claude):** 65 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G4-GET-E05-claude-bank-naar-033` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 71 − 29 kan kloppen?
    - **Opties:** A) 42 · B) 44 · C) 100
    - **Antwoord:** 42  (controle: n.v.t.)
    - **Fout-hints (Claude):** 100 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: In twee dozen zitten samen # [ding]. In de ene doos zitten # [ding] meer dan in de andere. Hoeveel [ding] zitten er in elke doos?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In twee dozen zitten samen # [ding]. In de ene doos zitten # [ding] meer dan in de andere. Hoeveel [ding] zitten er in elke doos?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): None (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar het verschil tussen de twee getallen. Dat moet precies 3 zijn.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-001` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** In twee dozen zitten samen 15 ballen. In de ene doos zitten 3 ballen meer dan in de andere. Hoeveel ballen zitten er in elke doos?
    - **Opties:** A) 12 en 3 · B) 8 en 7 · C) 9 en 6
    - **Antwoord:** 9 en 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 en 3 → Kijk goed naar het verschil tussen de twee getallen. Dat moet precies 3 zijn. · 8 en 7 → Tel het verschil tussen jouw twee getallen. Is dat echt 3?
    - **Uitleg (Claude):** Samen moeten de getallen 15 zijn en het verschil moet 3 zijn. Bij 9 en 6 klopt allebei: 9 plus 6 is 15 en 9 min 6 is 3.

- **Hint 1 (te schrijven):** Er zijn twee dozen. Samen is het hele aantal. In de ene doos zitten er een paar meer dan in de andere.
- **Hint 2 (te schrijven):** Kies twee getallen die samen het hele aantal zijn. Het verschil is hoeveel meer het ene getal is dan het andere. Is het verschil te groot of te klein? Schuif er dan één van de ene doos naar de andere.
- **Ouderzin:** Je kind zoekt twee getallen die samen een bepaald aantal zijn en een bepaald verschil hebben.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
