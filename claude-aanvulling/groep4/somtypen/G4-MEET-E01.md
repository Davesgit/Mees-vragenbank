# G4-MEET-E01 — Meten met meter en centimeter

Onze omschrijving: Standaardmaten m/cm (1 m = 100 cm); liniaal/meetlint · in onze bank: 8 items

Claude-vragen gemapt: **127** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [liniaal] Hoeveel centimeter is de strook?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[liniaal] Hoeveel centimeter is de rode strook?” (koppeling: claudeId)
- Items: **127** · Claude-doelen: M2 (127) · regel: G17-liniaal
- Getallenruimte: 0–10, 0–20 · type: meerkeuze
- **Visual: nodig** (127 items): Claude-tekenaar: soort “liniaal” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[liniaal] Hoeveel centimeter is de rode strook?”. Hints nakijken.
- Merge-fixlijst: #28 geen kleur in de vraag (127)
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (189), een-ernaast (65)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G4-MEET-E01-claude-bank-050` (Claude M2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel centimeter is de strook?
    - **Tekening:** `{"eind": 6, "soort": "liniaal", "start": 2, "lengte": 10}`
    - **Opties:** A) 6 · B) 3 · C) 4
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G4-MEET-E01-claude-bank-070` (Claude M2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel centimeter is de strook?
    - **Tekening:** `{"eind": 14, "soort": "liniaal", "start": 2, "lengte": 15}`
    - **Opties:** A) 12 · B) 14 · C) 13
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** De strook begint niet bij nul. Kijk waar hij begint en waar hij ophoudt.
- **Hint 2 (te schrijven):** Tel de centimeters van het begin tot het eind van de strook. Tel de stukjes tussen de streepjes, niet de streepjes zelf.
- **Ouderzin:** Je kind meet een strook op een liniaal die niet bij nul begint.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één centimeter te veel. Tel de stukjes tussen de streepjes, niet de streepjes.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één centimeter te weinig. Tel van het begin tot het eind van de strook.  [nieuw]
  - `veel te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Kijk goed waar de strook begint. Tel vanaf daar de centimeters tot het eind.  [nieuw]
  - `veel te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Kijk waar de strook begint en waar hij ophoudt. Tel de centimeters daartussen.  [nieuw]
  - `andere fout` (andere fout) → Kijk waar de strook begint en waar hij ophoudt. Tel de centimeters daartussen.  [nieuw]
- Status: hints klaar
