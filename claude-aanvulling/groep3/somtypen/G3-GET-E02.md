# G3-GET-E02 — Getallen op een lijn zetten

Onze omschrijving: Getallen ≤20 op getallenlijn; dichtbij/verder in rij ≤20 · in onze bank: 8 items

Claude-vragen gemapt: **4** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [getallenlijn] Zet # op de getallenlijn.

- Items: **2** · Claude-doelen: D2-1 (2) · regel: D-getallenlijn (R06-getallenlijn)
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E02-claude-bank-004` (Claude D2-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet 11 op de getallenlijn.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 20, "stap": 1, "labels": [0, 10, 20], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 11  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 11 ligt tussen 10 en 20, dichter bij 10.
  - `G3-GET-E02-claude-bank-003` (Claude D2-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet 18 op de getallenlijn.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 20, "stap": 1, "labels": [0, 10, 20], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 18  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 18 ligt tussen 10 en 20, dichter bij 20.

- **Hint 1 (te schrijven):** Zoek eerst de 10 op de lijn. Komt het getal vóór de 10 of erna?
- **Hint 2 (te schrijven):** Tel vanaf de 10 verder, streepje voor streepje, tot je bij het getal bent. Ligt het dicht bij de 20? Dan kun je ook terugtellen vanaf de 20.
- **Ouderzin:** Je kind zet een getal tot 20 op de getallenlijn, met 0, 10 en 20 als houvast.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien vergeten` (fout = antwoord − 10) → Kijk goed waar de 10 staat. Het getal is groter dan 10. Tel vanaf de 10 verder.  [nieuw]
  - `bijna` (fout ligt 1 naast het antwoord) → Bijna! Tel de streepjes nog eens, één voor één.  [nieuw]
  - `andere plek` (andere fout) → Zoek eerst de 10 op de lijn. Tel dan streepje voor streepje tot het getal.  [nieuw]
- Status: hints klaar

## Somtype 2: [getallenlijn] Waar hoort #? Zet de stip op de lijn.

- Items: **1** · Claude-doelen: D2-2 (1) · regel: D-getallenlijn (R06-getallenlijn)
- Getallenruimte: 0–12 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E02-claude-bank-001` (Claude D2-2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Waar hoort 12? Zet de stip op de lijn.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 20, "stap": 1, "labels": [0, 10, 20], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 12  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Zoek eerst het tiental ervoor: 10. Dan nog 2 verder.

- **Hint 1 (te schrijven):** Zoek eerst de 10 op de lijn. Komt het getal vóór de 10 of erna?
- **Hint 2 (te schrijven):** Tel vanaf de 10 verder, streepje voor streepje, tot je bij het getal bent. Zet daar de stip.
- **Ouderzin:** Je kind zet een getal tot 20 op de getallenlijn, met 0, 10 en 20 als houvast.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien vergeten` (fout = antwoord − 10) → Kijk goed waar de 10 staat. Het getal is groter dan 10. Tel vanaf de 10 verder.  [nieuw]
  - `bijna` (fout ligt 1 naast het antwoord) → Bijna! Tel de streepjes nog eens, één voor één.  [nieuw]
  - `andere plek` (andere fout) → Zoek eerst de 10 op de lijn. Tel dan streepje voor streepje tot het getal.  [nieuw]
- Status: hints klaar

## Somtype 3: [getallenlijn] Welk getal ligt precies tussen # en #?

- Items: **1** · Claude-doelen: D2-2 (1) · regel: D-getallenlijn (R03-precies-tussen)
- Getallenruimte: 0–20 · type: kale
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), plaatswaarde-verkeerd (1)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E02-claude-bank-002` (Claude D2-2, bank, niveau 3 → toepassen)
    - **Opgave:** Welk getal ligt precies tussen 12 en 20?
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 20, "stap": 1, "labels": [0, 10, 20], "kindTikt": true, "gemarkeerd": [12, 20]}`
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek de twee getallen uit de vraag op de lijn.
- **Hint 2 (te schrijven):** Zet een vinger op elk getal. Schuif je vingers tegelijk één streepje naar elkaar toe. Doe dat tot ze bij hetzelfde streepje zijn.
- **Ouderzin:** Je kind zoekt op de getallenlijn het getal dat precies in het midden van twee getallen ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Zoek het getal dat er precies tussenin ligt.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel de streepjes vanaf allebei de kanten. Aan beide kanten moet het even ver zijn.  [nieuw]
  - `andere plek` (andere fout) → Zet een vinger op elk getal. Schuif ze tegelijk naar elkaar toe, tot ze elkaar raken.  [nieuw]
- Status: hints klaar
