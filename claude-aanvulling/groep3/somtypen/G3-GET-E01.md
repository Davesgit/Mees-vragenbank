# G3-GET-E01 — Getallen op volgorde zetten

Onze omschrijving: Hoeveelheden ≤100 vergelijken/ordenen · in onze bank: 8 items

Claude-vragen gemapt: **1** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [kaartjes op volgorde slepen] Zet de getallen op volgorde van klein naar groot.

- Items: **1** · Claude-doelen: D1-7 (1) · regel: R07-ordenen
- Getallenruimte: 0–100 · type: ordenen
- Denkfouten (Claude): kleinste-van-grootste (1)
- Verschillende Claude-fout-hints: 1 (meest: “Klein naar groot: het kleinste getal eerst.”)
- Voorbeelden:
  - `G3-GET-E01-claude-bank-001` (Claude D1-7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet de getallen op volgorde van klein naar groot.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** 3|17|32|73  (controle: ok)
    - **Fout-hints (Claude):** 73|32|17|3 → Klein naar groot: het kleinste getal eerst.
    - **Uitleg (Claude):** Van klein naar groot: 3, 17, 32, 73.

- **Hint 1 (te schrijven):** Zoek eerst het kleinste getal. Dat kaartje komt vooraan.
- **Hint 2 (te schrijven):** Kijk naar de tientallen. Minder tientallen is kleiner. Een getal met één cijfer is kleiner dan een getal met twee cijfers. Zijn de tientallen gelijk? Kijk dan naar de eenheden.
- **Ouderzin:** Je kind zet getallen tot 100 op volgorde van klein naar groot.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
