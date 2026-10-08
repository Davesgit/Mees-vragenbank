# G3-GET-K03 — In één oogopslag tellen

Onze omschrijving: Subitizing ≤6; verkort tellen ≤12 (patronen) · in onze bank: 4 items

Claude-vragen gemapt: **57** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [groepjes] Hoeveel [ding] zie je?

- Items: **57** · Claude-doelen: D0-2 (57) · regel: R15-groepjes
- Getallenruimte: 0–10, 0–12 · type: meerkeuze
- Denkfouten (Claude): een-ernaast (67), grafiek-verkeerd-afgelezen (33), deel-vergeten-bij-splitsen (14)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-K03-claude-bank-030` (Claude D0-2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel cirkels zie je?
    - **Tekening:** `{"vorm": "cirkel", "soort": "groepjes", "aantal": 7, "perrij": 5}`
    - **Opties:** A) 5 · B) 6 · C) 7
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G3-GET-K03-claude-bank-056` (Claude D0-2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel rechthoeken zie je?
    - **Tekening:** `{"vorm": "rechthoek", "soort": "groepjes", "aantal": 12, "perrij": 5}`
    - **Opties:** A) 10 · B) 12 · C) 11
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 11 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 10 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Wijs elke vorm aan en tel. Wijs elke vorm maar één keer aan.
- **Hint 2 (te schrijven):** Is een rij helemaal vol? Dan weet je dat aantal al. Tel daarna de rest één voor één erbij.
- **Ouderzin:** Je kind telt vormen in rijtjes en wijst elke vorm één keer aan.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = antwoord ± 1) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `te veel` (fout = antwoord + 2 of meer) → Dat zijn er te veel. Is elke rij wel helemaal vol? Wijs elke vorm één keer aan.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Je bent er een paar vergeten. Tel ook de losse vormen erbij.  [nieuw]
- Status: hints klaar
