# G4-GET-E02 — Wat tientallen en eenheden zijn

Onze omschrijving: Positiewaarde; tientallige structuur uitleggen ≤100 · in onze bank: 8 items

Claude-vragen gemapt: **83** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is # [ding] en # [ding]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Hoeveel is # [ding] en # [ding]?” (koppeling: claudeId)
- Items: **55** · Claude-doelen: D2-4 (55) · regel: G05-tientallen
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tiental-ernaast (43), cijfers-verwisseld (26), getal-overgenomen (23), plaatswaarde-verkeerd (18)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G4-GET-E02-claude-bank-083` (Claude D2-4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 2 tientallen en 4 eenheden?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 42 → Je hebt de goede cijfers, maar kijk nog eens naar de volgorde. Welk cijfer hoort bij de tientallen? · 34 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G4-GET-E02-claude-bank-055` (Claude D2-4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 5 tientallen en 7 eenheden?
    - **Antwoord:** 57  (controle: ok)
    - **Fout-hints (Claude):** 75 → Je hebt de goede cijfers, maar kijk nog eens naar de volgorde. Welk cijfer hoort bij de tientallen? · 67 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Een tiental is tien. Hoeveel tientallen zijn er? En hoeveel losse eenheden?
- **Hint 2 (te schrijven):** Tel eerst in sprongen van tien, zo vaak als er tientallen zijn. Tel daarna de eenheden erbij, één voor één.
- **Ouderzin:** Je kind maakt een getal tot 100 uit tientallen en eenheden.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfers omgedraaid` (cijfers omgedraaid (tekst per item)) → Je hebt de goede cijfers, maar kijk nog eens naar de volgorde. Welk cijfer hoort bij de tientallen?  [Claude, ok]
  - `een tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Hoeveel tientallen staan er in de vraag?  [nieuw]
  - `een tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Hoeveel tientallen staan er in de vraag?  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Maar een tiental is tien, niet één. Tel in sprongen van tien.  [nieuw]
  - `alleen de eenheden` (fout = getal2) → Dat zijn alleen de eenheden. Vergeet de tientallen niet.  [nieuw]
  - `andere fout` (andere fout) → Begin met de tientallen. Tel in sprongen van tien. Tel daarna de eenheden erbij.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoeveel [ding] zitten er in #?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel [ding] zitten er in #?” (koppeling: claudeId)
- Items: **28** · Claude-doelen: D2-4 (28) · regel: G05-tientallen
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tiental-ernaast (29), getal-overgenomen (27)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G4-GET-E02-claude-bank-016` (Claude D2-4, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel tientallen zitten er in 22?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 1 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G4-GET-E02-claude-bank-020` (Claude D2-4, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel tientallen zitten er in 59?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 4 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Een tiental is een groepje van tien. Hoeveel van die groepjes passen er in het getal?
- **Hint 2 (te schrijven):** Tel in sprongen van tien. Stop als de volgende sprong te ver gaat. Hoeveel sprongen heb je gemaakt?
- **Ouderzin:** Je kind zoekt hoeveel tientallen er in een getal tot 100 zitten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eenheden als antwoord` (fout = eenheden van getal1) → Dat is het cijfer achteraan: de losse eenheden. De vraag is hoeveel tientallen erin zitten.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één tiental te veel. Tel nog eens in sprongen van tien.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één tiental te weinig. Tel nog eens in sprongen van tien.  [nieuw]
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag is hoeveel tientallen erin zitten.  [nieuw]
  - `andere fout` (andere fout) → Tel in sprongen van tien. Stop als de volgende sprong te ver gaat. Tel je sprongen.  [nieuw]
- Status: hints klaar
