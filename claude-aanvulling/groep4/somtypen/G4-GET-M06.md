# G4-GET-M06 — Keer-teken en eerste tafels

Onze omschrijving: ×-teken; ‘aantal keer’; tafels 1–5 en 10 (opbouw) · in onze bank: 8 items

Claude-vragen gemapt: **30** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [rooster] Kleur # × # [ding] rechthoek op het rooster.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[rooster] Kleur # × # [ding] rechthoek op het rooster.” (koppeling: claudeId)
- Items: **28** · Claude-doelen: D5-2 (12), D5-3 (12), D5-5 (4) · regel: G10-rooster-keer
- Getallenruimte: 0–10 · type: kale
- **Visual: nodig** (28 items): kleurbaar rooster van 10 × 10 hokjes; het kind kleurt een rechthoek
- Merge-fixlijst: #31 appMoetDoorgeven aantalGekleurd (28)
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G4-GET-M06-claude-bank-010` (Claude D5-2, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 3 × 10 als rechthoek op het rooster.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 3, "hokjesPerRij": 10, "claudeAntwoord": "10x3", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 3 rijen van 10 hokjes (rechthoek); 10 rijen van 3 ook goed (omdraaien mag)", "appMoetDoorgeven": "aantalGekleurd (en liefst ook rijen × hokjes per rij); anders krijgt elk fout antwoord de algemene fout-hint"}`
    - **Antwoord:** 3 rijen van 10 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 3 rijen van 10: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 3 × 10 = 30.
  - `G4-GET-M06-claude-bank-018` (Claude D5-3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 6 × 4 als rechthoek op het rooster.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 6, "hokjesPerRij": 4, "claudeAntwoord": "4x6", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 6 rijen van 4 hokjes (rechthoek); 4 rijen van 6 ook goed (omdraaien mag)", "appMoetDoorgeven": "aantalGekleurd (en liefst ook rijen × hokjes per rij); anders krijgt elk fout antwoord de algemene fout-hint"}`
    - **Antwoord:** 6 rijen van 4 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 6 rijen van 4: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 6 × 4 = 24.

- **Hint 1 (te schrijven):** Het keerteken (×) betekent: zoveel keer. Het eerste getal zegt hoeveel rijen je kleurt. Het tweede getal zegt hoeveel hokjes er in elke rij komen.
- **Hint 2 (te schrijven):** Kleur eerst één rij. Kleur dan de volgende rij recht eronder, net zo lang. Ga door tot je genoeg rijen hebt.
- **Ouderzin:** Je kind kleurt een keersom als rechthoek op een rooster: het eerste getal is het aantal rijen, het tweede het aantal hokjes per rij.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus gedaan` (fout = getal1 + getal2 (aantal gekleurde hokjes)) → Je hebt de getallen opgeteld. Het is een keersom: je kleurt een aantal rijen, en in elke rij evenveel hokjes.  [nieuw]
  - `één kolom` (fout = getal1 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `één rij` (fout = getal2 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `andere fout` (andere fout) → Tel je rijen. Tel de hokjes in elke rij. Kloppen ze met de som?  [nieuw]
- Status: hints klaar

## Somtype 2: [rooster] Kleur # rijen van # hokjes. Dat is # × #.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[rooster] Kleur # rijen van # hokjes. Dat is # × #.” (koppeling: claudeId)
- Items: **2** · Claude-doelen: D5-1 (2) · regel: D-rijen ×
- Getallenruimte: 0–10 · type: kale
- **Visual: nodig** (2 items): kleurbaar rooster; het kind kleurt de rijen en vult het aantal in
- Merge-fixlijst: #31 appMoetDoorgeven aantalGekleurd (2)
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G4-GET-M06-claude-bank-001` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 5 rijen van 5 hokjes. Dat is 5 × 5.
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 5, "hokjesPerRij": 5, "claudeAntwoord": "5x5", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 5 rijen van 5 hokjes (rechthoek)", "appMoetDoorgeven": "aantalGekleurd (en liefst ook rijen × hokjes per rij); anders krijgt elk fout antwoord de algemene fout-hint"}`
    - **Antwoord:** 5 rijen van 5 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 5 rijen van 5: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 5 × 5 = 25.
  - `G4-GET-M06-claude-bank-002` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 4 rijen van 6 hokjes. Dat is 4 × 6.
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 4, "hokjesPerRij": 6, "claudeAntwoord": "6x4", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 4 rijen van 6 hokjes (rechthoek)", "appMoetDoorgeven": "aantalGekleurd (en liefst ook rijen × hokjes per rij); anders krijgt elk fout antwoord de algemene fout-hint"}`
    - **Antwoord:** 4 rijen van 6 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 4 rijen van 6: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 4 × 6 = 24.

- **Hint 1 (te schrijven):** Kleur eerst één rij met zoveel hokjes als in de vraag staat.
- **Hint 2 (te schrijven):** Kleur dan de volgende rij recht eronder, net zo lang. Ga door tot je genoeg rijen hebt. Tel ze na.
- **Ouderzin:** Je kind kleurt rijen met hokjes op een rooster en ziet dat dat een keersom is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus gedaan` (fout = getal1 + getal2 (aantal gekleurde hokjes)) → Je hebt de getallen opgeteld. Het is een keersom: je kleurt een aantal rijen, en in elke rij evenveel hokjes.  [nieuw]
  - `één kolom` (fout = getal1 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `één rij` (fout = getal2 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `andere fout` (andere fout) → Tel je rijen. Tel de hokjes in elke rij. Kloppen ze met de som?  [nieuw]
- Status: hints klaar
