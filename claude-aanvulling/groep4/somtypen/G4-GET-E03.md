# G4-GET-E03 — Getallenlijn en even of oneven

Onze omschrijving: Interne/externe structuren; getallenlijn ≤100; even/oneven · in onze bank: 8 items

Claude-vragen gemapt: **111** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [getallenlijn] Welk getal ligt precies tussen # en #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Welk getal ligt precies tussen # en #?” (koppeling: claudeId)
- Items: **83** · Claude-doelen: D2-2 (83) · regel: G03-tussen
- Getallenruimte: 0–100 · type: kale
- **Visual: nodig** (83 items): getallenlijn 0–100 met de twee getallen gemarkeerd (fixlijst #14); de hints werken ook zonder lijn
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “Welk getal ligt precies tussen # en #?”. Hints nakijken.
- Merge-fixlijst: #14 getallenlijn (83)
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (66), plaatswaarde-verkeerd (38), verhoudingstabel-verkeerd (36), getal-overgenomen (26)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G4-GET-E03-claude-bank-072` (Claude D2-2, bank, niveau 3 → toepassen)
    - **Opgave:** Welk getal ligt precies tussen 72 en 84?
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 100, "stap": 1, "labels": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "gemarkeerd": [72, 84]}`
    - **Antwoord:** 78  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G4-GET-E03-claude-bank-071` (Claude D2-2, bank, niveau 3 → toepassen)
    - **Opgave:** Welk getal ligt precies tussen 42 en 54?
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 100, "stap": 1, "labels": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "gemarkeerd": [42, 54]}`
    - **Antwoord:** 48  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek de twee getallen op de getallenlijn. Het getal in het midden is van allebei even ver weg.
- **Hint 2 (te schrijven):** Hoe ver liggen de twee getallen uit elkaar? Neem de helft daarvan. Tel die helft verder vanaf het kleinste getal.
- **Ouderzin:** Je kind zoekt het getal dat precies in het midden ligt van twee getallen tot 100.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Zoek het getal dat er precies tussenin ligt.  [nieuw]
  - `het verschil` (fout = verschil van de getallen) → Zo ver liggen de getallen uit elkaar. Neem daar de helft van. Tel die helft verder vanaf het kleinste getal.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Het midden ligt tussen de twee getallen in.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Het midden is van allebei de getallen even ver weg. Reken het na.  [nieuw]
  - `andere fout` (andere fout) → Zoek het getal in het midden. Van daar is het naar allebei de getallen even ver.  [nieuw]
- Status: hints klaar

## Somtype 2: [getallenlijn] Zet # op de getallenlijn.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[getallenlijn] Zet # op de getallenlijn.” (koppeling: claudeId)
- Items: **28** · Claude-doelen: D1-7 (12), D2-1 (8), D2-2 (8) · regel: G02-getallenlijn
- Getallenruimte: 0–100 · type: kale
- **Visual: nodig** (28 items): getallenlijn 0–100 met streepjes per 1, de tientallen benoemd; het kind tikt (zoals Didactiek §9 in G3)
- Denkfouten (Claude): tafelbuur (12)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit een heel tiental ernaast. Kijk naar het cijfer vooraan.”)
- Voorbeelden:
  - `G4-GET-E03-claude-bank-090` (Claude D1-7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet 73 op de getallenlijn.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 100, "stap": 1, "labels": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 73  (controle: ok)
    - **Fout-hints (Claude):** 63 → Je zit een heel tiental ernaast. Kijk naar het cijfer vooraan.
    - **Uitleg (Claude):** Kijk eerst tussen welke tientallen 73 ligt: tussen 70 en 80. Dan tel je de rest erbij.
  - `G4-GET-E03-claude-bank-102` (Claude D2-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet 35 op de getallenlijn.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 100, "stap": 1, "labels": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 35 ligt tussen 30 en 40, dichter bij 40.

- **Hint 1 (te schrijven):** Kijk naar het cijfer vooraan. Bij welk tiental op de lijn hoort het getal?
- **Hint 2 (te schrijven):** Zoek dat tiental op de lijn. Het cijfer achteraan zegt hoeveel streepjes je nog verder gaat.
- **Ouderzin:** Je kind zet een getal tot 100 op de getallenlijn, met de tientallen als houvast.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiental te ver` (fout = antwoord + 10) → Je zit één tiental te ver naar rechts. Kijk naar het cijfer vooraan. Bij welk tiental hoort het getal?  [nieuw]
  - `een tiental te vroeg` (fout = antwoord − 10) → Je zit één tiental te ver naar links. Kijk naar het cijfer vooraan. Bij welk tiental hoort het getal?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Zoek het tiental. Tel vanaf daar de streepjes nog eens, één voor één.  [nieuw]
  - `andere plek` (andere fout) → Zoek eerst het goede tiental op de lijn. Tel dan de streepjes, één voor één.  [nieuw]
- Status: hints klaar
