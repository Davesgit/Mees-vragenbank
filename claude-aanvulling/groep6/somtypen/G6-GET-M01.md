# G6-GET-M01 — Grote getallen tot 100.000 lezen

Onze omschrijving: Getallen ±100.000 lezen/schrijven (punt/spatie) · in onze bank: 8 items

Claude-vragen gemapt: **5** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Er zijn # [ding] geteld. # = # + # + ? + #. Welk getal hoort op het vraagteken?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Er zijn # [ding] geteld. # = # + # + ? + #. Welk getal hoort op het vraagteken?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C11 (4) · regel: G6-G07-lezen
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (4), nul-fout-tientallen (4)
- Verschillende Claude-fout-hints: 8 (meest: “De 2 staat op de plek van de tientallen. Hoeveel is 2 tientallen waard?”)
- Voorbeelden:
  - `G6-GET-M01-claude-bank-003` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 8229 tanden geteld. 8229 = 8000 + 200 + ? + 9. Welk getal hoort op het vraagteken?
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2 → De 2 staat op de plek van de tientallen. Hoeveel is 2 tientallen waard? · 200 → Het zijn tientallen, geen honderdtallen. 2 tientallen is 2 keer 10.
    - **Uitleg (Claude):** 8229 bestaat uit 8 duizendtallen, 2 honderdtallen, 2 tientallen en 9 eenheden. 2 tientallen is 20.
  - `G6-GET-M01-claude-bank-002` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 1793 vissen geteld. 1793 = 1000 + 700 + ? + 3. Welk getal hoort op het vraagteken?
    - **Antwoord:** 90  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 → De 9 staat op de plek van de tientallen. Hoeveel is 9 tientallen waard? · 900 → Het zijn tientallen, geen honderdtallen. 9 tientallen is 9 keer 10.
    - **Uitleg (Claude):** 1793 bestaat uit 1 duizendtallen, 7 honderdtallen, 9 tientallen en 3 eenheden. 9 tientallen is 90.

- **Hint 1 (te schrijven):** Splits het getal: duizendtallen, honderdtallen, tientallen en eenheden. Welk deel staat er nog niet?
- **Hint 2 (te schrijven):** Het vraagteken hoort bij de tientallen. Kijk welk cijfer op de plek van de tientallen staat. Hoeveel is dat aantal tientallen waard?
- **Ouderzin:** Je kind splitst een getal tot 10.000 in duizendtallen, honderdtallen, tientallen en eenheden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het cijfer` (fout = antwoord : 10) → Je hebt alleen het cijfer opgeschreven. Dat cijfer staat op de plek van de tientallen. Hoeveel zijn die tientallen samen waard?  [nieuw]
  - `honderdtallen` (fout = antwoord × 10) → Dat zijn honderdtallen. Het cijfer staat op de plek van de tientallen, en één tiental is tien.  [nieuw]
  - `andere fout` (andere fout) → Splits het getal in duizendtallen, honderdtallen, tientallen en eenheden. Welk deel ontbreekt er nog in de som?  [nieuw]
- Status: hints klaar

## Somtype 2: [kaartjes op volgorde slepen] Zet de getallen op volgorde van klein naar groot.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[kaartjes op volgorde slepen] Zet de getallen op volgorde van klein naar groot.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C11 (1) · regel: G6-G07-lezen
- Getallenruimte: 0–100.000 · type: ordenen
- Denkfouten (Claude): kleinste-van-grootste (1)
- Verschillende Claude-fout-hints: 1 (meest: “Klein naar groot: het kleinste getal eerst.”)
- Voorbeelden:
  - `G6-GET-M01-claude-bank-005` (Claude C11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de getallen op volgorde van klein naar groot.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** 45.409|66.342|72.430|89.693  (controle: ok)
    - **Fout-hints (Claude):** 89.693|72.430|66.342|45.409 → Klein naar groot: het kleinste getal eerst.
    - **Uitleg (Claude):** Van klein naar groot: 45.409, 66.342, 72.430, 89.693.

- **Hint 1 (te schrijven):** Vergelijk eerst het cijfer vooraan: de tienduizendtallen. Het getal met het kleinste cijfer vooraan komt eerst.
- **Hint 2 (te schrijven):** Is het cijfer vooraan bij twee getallen gelijk? Kijk dan naar het cijfer erna. Zet zo alle getallen van klein naar groot.
- **Ouderzin:** Je kind zet getallen tot 100.000 op volgorde van klein naar groot.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `van groot naar klein` (volgorde omgedraaid) → Je hebt de getallen van groot naar klein gezet. Begin met het kleinste getal.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk de getallen van links naar rechts: eerst het cijfer vooraan, dan het cijfer erna. Het kleinste getal komt eerst.  [nieuw]
- Status: hints klaar
