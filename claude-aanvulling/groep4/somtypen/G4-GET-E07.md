# G4-GET-E07 — Tafels 1 tot 5 en 10

Onze omschrijving: Tafels 1,2,3,4,5,10 uit het hoofd · in onze bank: 8 items

Claude-vragen gemapt: **82** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # × # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **42** · Claude-doelen: D5-5 (24), D5-2 (11), D5-3 (7) · regel: G09-tafel
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Denkfouten (Claude): tafelbuur (84)
- Verschillende Claude-fout-hints: 1 (meest: “Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.”)
- Voorbeelden:
  - `G4-GET-E07-claude-bank-001` (Claude D5-2, bank, niveau 2 → toepassen)
    - **Opgave:** 10 × 2 =
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 10 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 24 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.
  - `G4-GET-E07-claude-bank-020` (Claude D5-5, bank, niveau 2 → toepassen)
    - **Opgave:** 6 × 5 =
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** 25 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 35 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.

- **Hint 1 (te schrijven):** Keer betekent: groepjes die even groot zijn.
- **Hint 2 (te schrijven):** Het eerste getal zegt hoeveel groepjes er zijn. Het tweede getal zegt hoeveel er in elk groepje zitten. Tel in sprongen.
- **Ouderzin:** Je kind oefent de tafels van 1 tot en met 5 en de tafel van 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de som` (fout = een getal uit de vraag) → Dat getal staat al in de som. Reken de som uit met sprongen.  [nieuw]
  - `plus gedaan` (fout = getal1 + getal2) → Je hebt plus gedaan. Bij keer tel je hetzelfde getal steeds opnieuw erbij.  [nieuw]
  - `een groepje te veel` (fout = antwoord + getal2) → Dat is één groepje te veel. Het eerste getal zegt hoeveel groepjes er zijn. Tel je sprongen nog eens.  [nieuw]
  - `een groepje te weinig` (fout = antwoord − getal2) → Dat is één groepje te weinig. Het eerste getal zegt hoeveel groepjes er zijn. Tel je sprongen nog eens.  [nieuw]
  - `elk groepje één te veel` (fout = antwoord + getal1) → Dat is te veel. Het tweede getal zegt hoeveel er in elk groepje zitten. Tel in sprongen van dat getal.  [nieuw]
  - `elk groepje één te weinig` (fout = antwoord − getal1) → Dat is te weinig. Het tweede getal zegt hoeveel er in elk groepje zitten. Tel in sprongen van dat getal.  [nieuw]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Tel nog eens in sprongen. Tel ook hoeveel sprongen je maakt.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Heb je alle sprongen gemaakt? Tel ze nog eens.  [nieuw]
  - `andere fout` (andere fout) → Reken de som uit met sprongen. Het tweede getal is de sprong. Het eerste getal zegt hoe vaak.  [nieuw]
- Status: hints klaar

## Somtype 2: □ × # = #

- Sleutel: nrOrigineel **2** · somtypeOrigineel “□ × # = #” (koppeling: claudeId)
- Items: **40** · Claude-doelen: D5-2 (24), D5-3 (16) · regel: G09-tafel
- Getallenruimte: 0–10, 0–100, 0–20 · type: invullen
- Denkfouten (Claude): een-ernaast (73), getal-overgenomen (7)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G4-GET-E07-claude-bank-043` (Claude D5-2, bank, niveau 3 → toepassen)
    - **Opgave:** □ × 2 = 6
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G4-GET-E07-claude-bank-082` (Claude D5-3, bank, niveau 3 → toepassen)
    - **Opgave:** □ × 3 = 12
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Hoe vaak past het getal achter het keerteken (×) in de uitkomst?
- **Hint 2 (te schrijven):** Tel in sprongen van het getal achter het keerteken, tot je bij de uitkomst bent. Tel hoeveel sprongen je maakt.
- **Ouderzin:** Je kind zoekt het getal dat ontbreekt in een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de som` (fout = een getal uit de vraag) → Dat getal staat al in de som. Zoek het getal op de lege plek: tel in sprongen tot de uitkomst.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt de twee getallen keer elkaar gedaan. Zoek het getal op de lege plek: hoe vaak past het getal achter het keerteken in de uitkomst?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één sprong te veel. Tel je sprongen nog eens.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één sprong te weinig. Tel je sprongen nog eens.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Tel in sprongen tot de uitkomst. Tel hoeveel sprongen je maakt.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Tel door in sprongen tot je bij de uitkomst bent. Tel hoeveel sprongen je maakt.  [nieuw]
  - `andere fout` (andere fout) → Tel in sprongen van het getal achter het keerteken, tot de uitkomst. Tel hoeveel sprongen je maakt.  [nieuw]
- Status: hints klaar
