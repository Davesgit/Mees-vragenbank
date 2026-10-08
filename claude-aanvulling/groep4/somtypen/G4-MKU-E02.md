# G4-MKU-E02 — Wat je vanaf hier ziet

Onze omschrijving: Wat iemand wel/niet ziet vanaf standpunt · in onze bank: 8 items

Claude-vragen gemapt: **12** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [plattegrond] Je staat bij de vlag en kijkt naar [richting]. Welk ding kun je niet zien, omdat er iets voor staat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[plattegrond] Je staat bij de vlag en kijkt recht naar [richting]. Welk ding kun je niet zien, omdat er iets voor staat?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: K10 (7) · regel: G21-kijklijn
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig** (7 items): Claude-tekenaar: soort “plattegrond” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[plattegrond] Je staat bij de vlag en kijkt recht naar [richting]. Welk ding kun je niet zien, omdat er iets voor staat?”. Hints nakijken.
- Merge-fixlijst: #33 kijkt naar (7)
- Denkfouten (Claude): None (14)
- Verschillende Claude-fout-hints: 9 (meest: “De bank staat in een andere rij; daar kijk je niet langs.”)
- Voorbeelden:
  - `G4-MKU-E02-claude-bank-002` (Claude K10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vlag en kijkt naar rechts. Welk ding kun je niet zien, omdat er iets voor staat?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "B1", "wat": "vlag"}, {"vak": "B4", "wat": "bal"}, {"vak": "B5", "wat": "vijver"}, {"vak": "A5", "wat": "bank"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) bal · B) bank · C) vijver
    - **Antwoord:** vijver  (controle: ok)
    - **Fout-hints (Claude):** bal → De bal is juist het eerste wat je ziet. Wat staat er achter? · bank → De bank staat in een andere rij; daar kijk je niet langs.
  - `G4-MKU-E02-claude-bank-006` (Claude K10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vlag en kijkt naar links. Welk ding kun je niet zien, omdat er iets voor staat?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "A6", "wat": "vlag"}, {"vak": "A4", "wat": "put"}, {"vak": "A1", "wat": "boom"}, {"vak": "B5", "wat": "bank"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) boom · B) put · C) bank
    - **Antwoord:** boom  (controle: ok)
    - **Fout-hints (Claude):** put → De put is juist het eerste wat je ziet. Wat staat er achter? · bank → De bank staat in een andere rij; daar kijk je niet langs.

- **Hint 1 (te schrijven):** Je kijkt recht vooruit, langs de rij van de vlag. Welke dingen staan in die rij?
- **Hint 2 (te schrijven):** Het eerste ding dat je tegenkomt, zie je. Wat daarachter staat, zie je niet.
- **Ouderzin:** Je kind zoekt op een plattegrond welk ding achter een ander ding verstopt staat.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerd ding` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere rij` (andere fout) → Dat staat niet in dezelfde rij als de vlag. Blijf in de rij van de vlag: welk ding staat achter een ander ding?  [nieuw]
- Status: hints klaar

## Somtype 2: [plattegrond] Je staat bij de vlag en kijkt naar [richting]. Welk ding zie je als eerste?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[plattegrond] Je staat bij de vlag en kijkt recht naar [richting]. Welk ding zie je als eerste?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: K10 (5) · regel: G21-kijklijn
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig** (5 items): Claude-tekenaar: soort “plattegrond” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[plattegrond] Je staat bij de vlag en kijkt recht naar [richting]. Welk ding zie je als eerste?”. Hints nakijken.
- Merge-fixlijst: #33 kijkt naar (5)
- Denkfouten (Claude): None (10)
- Verschillende Claude-fout-hints: 7 (meest: “De bal staat niet op dezelfde rij als de vlag. Je kijkt recht langs de rij.”)
- Voorbeelden:
  - `G4-MKU-E02-claude-bank-009` (Claude K10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je staat bij de vlag en kijkt naar links. Welk ding zie je als eerste?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "A6", "wat": "vlag"}, {"vak": "A4", "wat": "huis"}, {"vak": "A1", "wat": "boom"}, {"vak": "B5", "wat": "bal"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) bal · B) huis · C) boom
    - **Antwoord:** huis  (controle: ok)
    - **Fout-hints (Claude):** boom → De boom staat wel in dezelfde rij, maar er staat iets vóór. Wat kom je het eerst tegen? · bal → De bal staat niet op dezelfde rij als de vlag. Je kijkt recht langs de rij.
  - `G4-MKU-E02-claude-bank-008` (Claude K10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je staat bij de vlag en kijkt naar rechts. Welk ding zie je als eerste?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "D1", "wat": "vlag"}, {"vak": "D3", "wat": "vijver"}, {"vak": "D6", "wat": "bank"}, {"vak": "C2", "wat": "tent"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) tent · B) vijver · C) bank
    - **Antwoord:** vijver  (controle: ok)
    - **Fout-hints (Claude):** bank → De bank staat wel in dezelfde rij, maar er staat iets vóór. Wat kom je het eerst tegen? · tent → De tent staat niet op dezelfde rij als de vlag. Je kijkt recht langs de rij.

- **Hint 1 (te schrijven):** Je kijkt recht vooruit, langs de rij van de vlag. Welke dingen staan in die rij?
- **Hint 2 (te schrijven):** Ga vanaf de vlag hokje voor hokje in de richting waar je kijkt. Wat kom je het eerst tegen?
- **Ouderzin:** Je kind zoekt op een plattegrond welk ding het als eerste ziet.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerd ding` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere rij` (andere fout) → Dat staat niet in dezelfde rij als de vlag. Je kijkt alleen langs de rij van de vlag.  [nieuw]
- Status: hints klaar
