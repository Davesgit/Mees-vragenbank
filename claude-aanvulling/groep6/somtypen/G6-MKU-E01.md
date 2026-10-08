# G6-MKU-E01 — Kaart lezen: schaal, legenda, vakjes, windrichting

Onze omschrijving: Schaal (begrip); legenda; roostercoördinaten; N/O/Z/W · in onze bank: 8 items

Claude-vragen gemapt: **131** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [plattegrond] Wat staat er in vak [vak]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[plattegrond] Wat staat er in vak [vak]?” (koppeling: claudeId)
- Items: **70** · Claude-doelen: K7 (70) · regel: D8-VAKCODE-NAAR-G6
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 126 (meest: “De tent staat in de goede kolom, maar in een andere rij. Kijk bij vak C6 goed naar het cijfer naast de rij.”)
- Voorbeelden:
  - `G6-MKU-E01-claude-bank-naar-062` (Claude K7, bank, niveau 1 → basis)
    - **Opgave:** Wat staat er in vak B4?
    - **Tekening:** `{"rijen": 6, "soort": "plattegrond", "dingen": [{"vak": "B4", "wat": "boom"}, {"vak": "D2", "wat": "huis"}, {"vak": "B3", "wat": "vijver"}, {"vak": "A4", "wat": "put"}, {"vak": "C4", "wat": "vlag"}], "kolommen": 6}`
    - **Opties:** A) boom · B) vijver · C) huis
    - **Antwoord:** boom  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G6-MKU-E01-claude-bank-naar-098` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** Wat staat er in vak A4?
    - **Tekening:** `{"rijen": 6, "soort": "plattegrond", "dingen": [{"vak": "A4", "wat": "hek"}, {"vak": "D1", "wat": "bal"}, {"vak": "A3", "wat": "boom"}, {"vak": "B4", "wat": "huis"}, {"vak": "D5", "wat": "vijver"}], "kolommen": 8}`
    - **Opties:** A) hek · B) huis · C) bal
    - **Antwoord:** hek  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst de letter van het vak langs de rand. Zoek daarna het cijfer.
- **Hint 2 (te schrijven):** Volg vanaf de letter de vakjes recht door. Volg ook vanaf het cijfer de vakjes recht door. Waar die twee elkaar raken, is het vak. Kijk wat daar staat.
- **Ouderzin:** Je kind leest af wat er in een vak van een plattegrond staat. Een vak heeft een letter en een cijfer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `goede letter, ander cijfer` (goede letter, ander cijfer) → Dat staat in een vak met de goede letter, maar met een ander cijfer. Kijk nog eens naar het cijfer.  [nieuw]
  - `goed cijfer, andere letter` (goed cijfer, andere letter) → Dat staat in een vak met het goede cijfer, maar met een andere letter. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid) → Heb je de letter en het cijfer omgedraaid? Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
  - `andere fout` (ander vak) → Dat staat in een ander vak. Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
- Status: hints klaar

## Somtype 2: [plattegrond] In welk vak staat de/het [ding]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[plattegrond] In welk vak staat de/het [ding]?” (koppeling: claudeId)
- Items: **49** · Claude-doelen: K7 (49) · regel: D8-VAKCODE-NAAR-G6
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 52 (meest: “De letter klopt. Kijk nog eens naar het cijfer naast de rij waarin het huis staat.”)
- Voorbeelden:
  - `G6-MKU-E01-claude-bank-naar-001` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** In welk vak staat de bank?
    - **Tekening:** `{"rijen": 7, "soort": "plattegrond", "dingen": [{"vak": "G2", "wat": "bank"}, {"vak": "B7", "wat": "tent"}, {"vak": "G6", "wat": "school"}, {"vak": "F2", "wat": "hek"}, {"vak": "G1", "wat": "bal"}], "kolommen": 7}`
    - **Opties:** A) G6 · B) B7 · C) G2
    - **Antwoord:** G2  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G6-MKU-E01-claude-bank-naar-024` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** In welk vak staat de bal?
    - **Tekening:** `{"rijen": 7, "soort": "plattegrond", "dingen": [{"vak": "F1", "wat": "bal"}, {"vak": "A6", "wat": "boom"}, {"vak": "F7", "wat": "huis"}, {"vak": "G1", "wat": "vijver"}, {"vak": "B4", "wat": "put"}], "kolommen": 7}`
    - **Opties:** A) F1 · B) F7 · C) A6
    - **Antwoord:** F1  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst op de plattegrond het ding uit de vraag.
- **Hint 2 (te schrijven):** Ga vanaf daar recht naar de rand met de letters. Ga daarna recht naar de rand met de cijfers. Eerst de letter, dan het cijfer.
- **Ouderzin:** Je kind zoekt in welk vak van een plattegrond iets staat. Een vak heeft een letter en een cijfer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `goede letter, ander cijfer` (goede letter, ander cijfer) → De letter klopt, maar het cijfer niet. Ga recht naar de rand met de cijfers en kijk nog eens.  [nieuw]
  - `goed cijfer, andere letter` (goed cijfer, andere letter) → Het cijfer klopt, maar de letter niet. Ga recht naar de rand met de letters en kijk nog eens.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid) → Heb je de letter en het cijfer omgedraaid? De letter lees je af bij de rand met de letters, het cijfer bij de rand met de cijfers.  [nieuw]
  - `andere fout` (ander vak) → Dat is een ander vak. Zoek eerst waar het staat. Ga dan recht naar de rand met de letters, en daarna naar de rand met de cijfers.  [nieuw]
- Status: hints klaar

## Somtype 3: [plattegrond] Wat staat er in vak G#?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[plattegrond] Wat staat er in vak G#?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: K7 (9) · regel: D8-VAKCODE-NAAR-G6
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 18 (meest: “De bal staat in de goede rij, maar in een andere kolom. Kijk bij vak G1 goed naar de letter boven de kolom.”)
- Voorbeelden:
  - `G6-MKU-E01-claude-bank-naar-050` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** Wat staat er in vak G1?
    - **Tekening:** `{"rijen": 7, "soort": "plattegrond", "dingen": [{"vak": "G1", "wat": "tent"}, {"vak": "A7", "wat": "school"}, {"vak": "G7", "wat": "hek"}, {"vak": "F1", "wat": "bal"}, {"vak": "A2", "wat": "boom"}], "kolommen": 7}`
    - **Opties:** A) tent · B) bal · C) hek
    - **Antwoord:** tent  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
  - `G6-MKU-E01-claude-bank-naar-055` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** Wat staat er in vak G3?
    - **Tekening:** `{"rijen": 7, "soort": "plattegrond", "dingen": [{"vak": "G3", "wat": "hek"}, {"vak": "C7", "wat": "bal"}, {"vak": "G5", "wat": "boom"}, {"vak": "F3", "wat": "huis"}, {"vak": "F6", "wat": "vijver"}], "kolommen": 7}`
    - **Opties:** A) boom · B) huis · C) hek
    - **Antwoord:** hek  (controle: n.v.t.)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst de letter van het vak langs de rand. Zoek daarna het cijfer.
- **Hint 2 (te schrijven):** Volg vanaf de letter de vakjes recht door. Volg ook vanaf het cijfer de vakjes recht door. Waar die twee elkaar raken, is het vak. Kijk wat daar staat.
- **Ouderzin:** Je kind leest af wat er in een vak van een plattegrond staat. Een vak heeft een letter en een cijfer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `goede letter, ander cijfer` (goede letter, ander cijfer) → Dat staat in een vak met de goede letter, maar met een ander cijfer. Kijk nog eens naar het cijfer.  [nieuw]
  - `goed cijfer, andere letter` (goed cijfer, andere letter) → Dat staat in een vak met het goede cijfer, maar met een andere letter. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid) → Heb je de letter en het cijfer omgedraaid? Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
  - `andere fout` (ander vak) → Dat staat in een ander vak. Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
- Status: hints klaar

## Somtype 4: [plattegrond] Wat staat er in vak H#?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[plattegrond] Wat staat er in vak H#?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: K7 (3) · regel: D8-VAKCODE-NAAR-G6
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “De school staat in de goede rij, maar in een andere kolom. Kijk bij vak H6 goed naar de letter boven de kolom.”)
- Voorbeelden:
  - `G6-MKU-E01-claude-bank-naar-059` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** Wat staat er in vak H6?
    - **Tekening:** `{"rijen": 6, "soort": "plattegrond", "dingen": [{"vak": "H6", "wat": "bank"}, {"vak": "H1", "wat": "tent"}, {"vak": "G6", "wat": "school"}, {"vak": "A1", "wat": "hek"}], "kolommen": 8}`
    - **Opties:** A) school · B) bank · C) tent
    - **Antwoord:** bank  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
  - `G6-MKU-E01-claude-bank-naar-061` (Claude K7, bank, niveau 2 → toepassen)
    - **Opgave:** Wat staat er in vak H4?
    - **Tekening:** `{"rijen": 6, "soort": "plattegrond", "dingen": [{"vak": "H4", "wat": "boom"}, {"vak": "H3", "wat": "huis"}, {"vak": "G4", "wat": "vijver"}, {"vak": "A1", "wat": "put"}], "kolommen": 8}`
    - **Opties:** A) vijver · B) boom · C) huis
    - **Antwoord:** boom  (controle: n.v.t.)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst de letter van het vak langs de rand. Zoek daarna het cijfer.
- **Hint 2 (te schrijven):** Volg vanaf de letter de vakjes recht door. Volg ook vanaf het cijfer de vakjes recht door. Waar die twee elkaar raken, is het vak. Kijk wat daar staat.
- **Ouderzin:** Je kind leest af wat er in een vak van een plattegrond staat. Een vak heeft een letter en een cijfer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `goede letter, ander cijfer` (goede letter, ander cijfer) → Dat staat in een vak met de goede letter, maar met een ander cijfer. Kijk nog eens naar het cijfer.  [nieuw]
  - `goed cijfer, andere letter` (goed cijfer, andere letter) → Dat staat in een vak met het goede cijfer, maar met een andere letter. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid) → Heb je de letter en het cijfer omgedraaid? Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
  - `andere fout` (ander vak) → Dat staat in een ander vak. Zoek de letter bij de rand met de letters, en het cijfer bij de rand met de cijfers.  [nieuw]
- Status: hints klaar
