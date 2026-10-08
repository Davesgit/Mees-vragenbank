# G3-MKU-E03 — Nabouwen en vouwen

Onze omschrijving: Groter bouwsel nabouwen; vouwwerk; patroon ontwerpen · in onze bank: 8 items

Claude-vragen gemapt: **27** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [vorm] Vouw het blad dicht over de rode lijn. Waar komt de stip?

- Items: **27** · Claude-doelen: K3 (22), K6 (5) · regel: D-spiegelen (R21-spiegelen)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): een-ernaast (28), spiegelen-verkeerd (26)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-MKU-E03-claude-bank-022` (Claude K3, bank, niveau 2 → toepassen)
    - **Opgave:** Vouw het blad dicht over de rode lijn. Waar komt de stip?
    - **Tekening:** `{"as": "verticaal", "stip": "D1", "rijen": 4, "soort": "vorm", "asplek": 2, "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** D4  (controle: ok)
    - **Fout-hints (Claude):** D5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · D6 → Een spiegel draait de figuur om. Wat links staat komt rechts, even ver van de lijn.
  - `G3-MKU-E03-claude-bank-024` (Claude K6, bank, niveau 2 → toepassen)
    - **Opgave:** Vouw het blad dicht over de rode lijn. Waar komt de stip?
    - **Tekening:** `{"as": "verticaal", "stip": "B1", "rijen": 5, "soort": "vorm", "asplek": 2, "kolommen": 7, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** B4  (controle: ok)
    - **Fout-hints (Claude):** B5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · B7 → Een spiegel draait de figuur om. Wat links staat komt rechts, even ver van de lijn.

- **Hint 1 (te schrijven):** Vouw het blad in gedachten dicht over de rode lijn. De stip gaat mee naar de andere kant.
- **Hint 2 (te schrijven):** Tel de hokjes van de stip tot de rode lijn. Tel het hokje van de stip mee. Tel aan de andere kant van de lijn net zo veel. Blijf in dezelfde rij.
- **Ouderzin:** Je kind vouwt in gedachten een blad dicht over een lijn en zoekt waar een stip terechtkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stip niet verplaatst` (stip niet verplaatst (fout = het vak van de stip)) → Daar staat de stip nu. Vouw het blad in je hoofd dicht over de rode lijn. Waar komt de stip dan?  [nieuw]
  - `goede rij, verkeerd hokje` (goede letter, ander cijfer) → Je zit in de goede rij. Tel de hokjes van de stip tot de rode lijn, met het hokje van de stip erbij. Tel aan de andere kant net zo veel.  [nieuw]
  - `andere rij` (goed cijfer, andere letter) → Bij het vouwen blijft de stip in dezelfde rij. Ga recht opzij over de rode lijn.  [nieuw]
  - `ander vak` (ander vak) → Zoek eerst de rij van de stip. Ga dan recht opzij over de rode lijn, net zo ver als de stip van de lijn af is.  [nieuw]
- Status: hints klaar
