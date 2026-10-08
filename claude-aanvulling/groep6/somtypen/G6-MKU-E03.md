# G6-MKU-E03 — Blokken bouwen en plattegrond met getallen

Onze omschrijving: Blokkenbouwsel ↔ plattegrond met hoogtegetallen · in onze bank: 8 items

Claude-vragen gemapt: **400** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [bouwvorm] Dit bouwwerk bestaat uit torens van blokjes. Elke toren staat op de grond, er zitten geen gaten onder. Hoeveel blokjes zijn er gebruikt?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[bouwvorm] Dit bouwwerk bestaat uit torens van blokjes. Elke toren staat op de grond, er zitten geen gaten onder. Hoeveel blokjes zijn er gebruikt?” (koppeling: claudeId)
- Items: **400** · Claude-doelen: K8 (400) · regel: D8-BOUWVORM-NAAR-G6
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “Tel toren voor toren hoeveel blokjes er op elkaar staan. Tel die aantallen daarna op.”)
- Voorbeelden:
  - `G6-MKU-E03-claude-bank-naar-001` (Claude K8, bank, niveau 1 → toepassen)
    - **Opgave:** Dit bouwwerk bestaat uit torens van blokjes. Elke toren staat op de grond, er zitten geen gaten onder. Hoeveel blokjes zijn er gebruikt?
    - **Tekening:** `{"diep": 5, "breed": 5, "soort": "bouwvorm", "stapels": [[0, 3, 0, 0, 0], [3, 1, 1, 3, 3], [0, 1, 0, 0, 0], [0, 3, 0, 0, 0], [0, 3, 0, 0, 0]]}`
    - **Opties:** A) 18 · B) 21 · C) 9
    - **Antwoord:** 21  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 18 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G6-MKU-E03-claude-bank-naar-201` (Claude K8, bank, niveau 2 → kritisch)
    - **Opgave:** Dit bouwwerk bestaat uit torens van blokjes. Elke toren staat op de grond, er zitten geen gaten onder. Hoeveel blokjes zijn er gebruikt?
    - **Tekening:** `{"diep": 5, "breed": 4, "soort": "bouwvorm", "stapels": [[1, 4, 5, 5], [5, 0, 0, 1], [5, 0, 0, 2], [5, 0, 0, 3], [5, 0, 0, 3]]}`
    - **Opties:** A) 43 · B) 12 · C) 44
    - **Antwoord:** 44  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 43 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Het bouwwerk bestaat uit torens. Een toren is een stapel blokjes op één vakje van de grond. Tel toren voor toren.
- **Hint 2 (te schrijven):** Kijk bij elke toren hoe hoog hij is. De blokjes onder het bovenste blokje zie je niet altijd, maar ze zijn er wel. Tel de aantallen van alle torens bij elkaar op.
- **Ouderzin:** Je kind telt de blokjes van een bouwwerk van torens. Ook de blokjes die je niet ziet, tellen mee.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `aantal torens` (fout = het aantal torens) → Is dat het aantal torens? Een toren kan hoger zijn dan één blokje. Tel bij elke toren hoeveel blokjes er op elkaar staan. Tel die aantallen daarna op.  [nieuw]
  - `alle torens even hoog` (fout = de hoogste toren keer het aantal torens) → Zijn alle torens even hoog? Tel elke toren apart en tel de aantallen daarna op.  [nieuw]
  - `volle balk` (fout = de hoogste toren keer het aantal vakjes van de grond) → Is het bouwwerk een volle balk? Er zijn lege vakjes en lagere torens. Tel alleen de blokjes die er echt staan.  [nieuw]
  - `elke toren één te veel` (fout = het antwoord plus het aantal torens) → Heb je bij elke toren één blokje te veel geteld? Tel bij elke toren van het onderste tot het bovenste blokje.  [nieuw]
  - `een toren vergeten` (fout = het antwoord min één toren) → Heb je elke toren meegeteld? Tel toren voor toren, en sla er geen over.  [nieuw]
  - `anders geteld` (Claudes sleutel (zonder label)) → Tel nog eens. Tel bij elke toren hoeveel blokjes er op elkaar staan. Tel die aantallen daarna op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel bij elke toren hoeveel blokjes er op elkaar staan. Tel die aantallen daarna op.  [nieuw]
- Status: hints klaar
