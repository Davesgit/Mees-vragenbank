# G4-MKU-E05 — Spiegelbeeld en schaduwen

Onze omschrijving: Spiegelbeeld van patroon; schaduwen herkennen · in onze bank: 8 items

Claude-vragen gemapt: **83** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [vorm] Spiegel de stip in de lijn. Tik op het vak waar hij komt.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[vorm] Spiegel de stip in de rode lijn. Tik op het vak waar hij komt.” (koppeling: claudeId)
- Items: **83** · Claude-doelen: K6 (83) · regel: D-spiegelen
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- **Visual: nodig** (83 items): tekenaar “vorm”: rooster met rode lijn en stip; het kind tikt op het vak (Didactiek §1)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[vorm] Spiegel de stip in de rode lijn. Tik op het vak waar hij komt.”. Hints nakijken.
- Merge-fixlijst: #28 geen kleur in de vraag (83), #37 appMoetTonen rijlettersEnKolomnummers (anders ALT_AAN = True in hints/patch_batch3b.py) (83)
- Denkfouten (Claude): een-ernaast (91), spiegelen-verkeerd (75)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G4-MKU-E05-claude-bank-077` (Claude K6, bank, niveau 2 → toepassen)
    - **Opgave:** Spiegel de stip in de lijn. Tik op het vak waar hij komt.
    - **Tekening:** `{"as": "verticaal", "stip": "F1", "rijen": 6, "soort": "vorm", "asplek": 2, "kolommen": 7, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** F4  (controle: ok)
    - **Fout-hints (Claude):** F5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · F7 → Een spiegel draait de figuur om. Wat links staat komt rechts, even ver van de lijn.
  - `G4-MKU-E05-claude-bank-027` (Claude K6, bank, niveau 3 → toepassen)
    - **Opgave:** Spiegel de stip in de lijn. Tik op het vak waar hij komt.
    - **Tekening:** `{"as": "verticaal", "stip": "B1", "rijen": 6, "soort": "vorm", "asplek": 3, "kolommen": 8, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** B6  (controle: ok)
    - **Fout-hints (Claude):** B1 → Een spiegel draait de figuur om. Wat links staat komt rechts, even ver van de lijn. · B8 → Een spiegel draait de figuur om. Wat links staat komt rechts, even ver van de lijn.

- **Hint 1 (te schrijven):** Stel je voor dat de lijn een spiegel is. De stip komt aan de andere kant, net zo ver van de lijn.
- **Hint 2 (te schrijven):** Tel de hokjes van de stip tot de lijn. Tel het hokje van de stip mee. Ga recht over de lijn en tel aan de andere kant net zo veel.
- **Ouderzin:** Je kind spiegelt een stip in een lijn op een rooster.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stip niet verplaatst` (stip niet verplaatst (fout = het vak van de stip)) → Daar staat de stip nu. Spiegel hem: aan de andere kant van de lijn, net zo ver van de lijn.  [nieuw]
  - `goede letter, ander cijfer` (goede letter, ander cijfer) → De letter klopt, maar het cijfer niet. Ga recht over de lijn, en tel aan de andere kant net zo veel hokjes als de stip van de lijn af is.  [nieuw]
  - `goed cijfer, andere letter` (goed cijfer, andere letter) → Het cijfer klopt, maar de letter niet. Ga recht over de lijn, en tel aan de andere kant net zo veel hokjes als de stip van de lijn af is.  [nieuw]
  - `ander vak` (ander vak) → Dat is een ander vak. Ga vanaf de stip recht naar de lijn, en dan net zo ver door aan de andere kant.  [nieuw]
- Status: hints klaar
