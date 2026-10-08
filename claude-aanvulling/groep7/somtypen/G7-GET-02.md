# G7-GET-02 — Kommagetallen tot drie cijfers

Onze omschrijving: Decimalen t/m 3 · in onze bank: 8 items

Claude-vragen gemapt: **444** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Welk getal is het grootst?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Welk getal is het grootst? Kies uit #, # of #.” (koppeling: claudeId)
- Items: **216** · Claude-doelen: B4 (216) · regel: G7-K03-komma-3, D-INKORT-3DEC, D-INKORT-3DEC-ANTWOORD-NIEUW
- Getallenruimte: kommagetallen (3 cijfers achter de komma), kommagetallen (4 cijfers achter de komma) · type: meerkeuze
- Uit de G6-park: 216 items
- Denkfouten (Claude): tienden-niet-vergeleken (306), kommagetal-als-geheel (126)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?”)
- Voorbeelden:
  - `G7-GET-02-claude-bank-021` (Claude B4, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is het grootst?
    - **Opties:** A) 2,603 · B) 2,5 · C) 2,45
    - **Antwoord:** 2,603  (controle: ok)
    - **Fout-hints (Claude):** 2,5 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 2,45 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?
  - `G7-GET-02-claude-bank-246` (Claude B4, bank, niveau 3 → toepassen)
    - **Opgave:** Welk getal is het grootst?
    - **Opties:** A) 1,92 · B) 1,103 · C) 1,902
    - **Antwoord:** 1,92  (controle: ok)
    - **Fout-hints (Claude):** 1,103 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 1,902 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar, met de komma’s onder elkaar.
- **Hint 2 (te schrijven):** Vergelijk eerst de hele getallen. Zijn die gelijk? Vergelijk dan de tienden, daarna de honderdsten. Een getal met meer cijfers achter de komma is niet vanzelf groter.
- **Ouderzin:** Je kind zoekt het grootste van drie kommagetallen door eerst de tienden te vergelijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tienden niet vergeleken` (Claudes sleutel: tienden-niet-vergeleken) → Is dat echt het grootste getal? Vergelijk eerst de tienden, dan de honderdsten.  [Claude, taalfix]
  - `langer is groter` (Claudes sleutel: kommagetal-als-geheel) → Is een getal met meer cijfers achter de komma ook groter? Vergelijk eerst de tienden: het cijfer vlak achter de komma.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk eerst de tienden, dan de honderdsten.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Welk getal is het grootst? Kies uit #, # of #.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 2: Welk getal is het kleinst?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Welk getal is het kleinst? Kies uit #, # of #.” (koppeling: claudeId)
- Items: **216** · Claude-doelen: B4 (216) · regel: G7-K03-komma-3, D-INKORT-3DEC-ANTWOORD-NIEUW, D-INKORT-3DEC
- Getallenruimte: kommagetallen (3 cijfers achter de komma), kommagetallen (4 cijfers achter de komma) · type: meerkeuze
- Uit de G6-park: 216 items
- Denkfouten (Claude): tienden-niet-vergeleken (270), kommagetal-als-geheel (162)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is kleiner?”)
- Voorbeelden:
  - `G7-GET-02-claude-bank-194` (Claude B4, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is het kleinst?
    - **Opties:** A) 1,403 · B) 1,8 · C) 1,25
    - **Antwoord:** 1,25  (controle: ok)
    - **Fout-hints (Claude):** 1,403 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is kleiner? · 1,8 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is kleiner?
  - `G7-GET-02-claude-bank-436` (Claude B4, bank, niveau 3 → toepassen)
    - **Opgave:** Welk getal is het kleinst?
    - **Opties:** A) 1,68 · B) 1,375 · C) 1,656
    - **Antwoord:** 1,375  (controle: ok)
    - **Fout-hints (Claude):** 1,68 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is kleiner? · 1,656 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is kleiner?

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar, met de komma’s onder elkaar.
- **Hint 2 (te schrijven):** Vergelijk eerst de hele getallen. Zijn die gelijk? Vergelijk dan de tienden, daarna de honderdsten. Een getal met minder cijfers achter de komma is niet vanzelf kleiner.
- **Ouderzin:** Je kind zoekt het kleinste van drie kommagetallen door eerst de tienden te vergelijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tienden niet vergeleken` (Claudes sleutel: tienden-niet-vergeleken) → Is dat echt het kleinste getal? Vergelijk eerst de tienden, dan de honderdsten.  [Claude, taalfix]
  - `korter is kleiner` (Claudes sleutel: kommagetal-als-geheel) → Is een getal met minder cijfers achter de komma ook kleiner? Vergelijk eerst de tienden: het cijfer vlak achter de komma.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk eerst de tienden, dan de honderdsten.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Welk getal is het kleinst? Kies uit #, # of #.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: Een [ding] weegt precies # kg. Rond af op één cijfer achter de komma.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een [ding] weegt precies # kg. Rond af op één cijfer achter de komma.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: B12 (12) · regel: G7-K04-komma-afronden
- Getallenruimte: kommagetallen (3 cijfers achter de komma) · type: kale
- Uit de G6-park: 12 items
- Denkfouten (Claude): afronden-verkeerde-kant (12), plaatswaarde-verkeerd (12)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer direct na de tienden. Vanaf 5 ga je naar boven.”)
- Voorbeelden:
  - `G7-GET-02-claude-bank-012` (Claude B12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt precies 1,878 kg. Rond af op één cijfer achter de komma.
    - **Antwoord:** 1,9  (controle: ok)
    - **Fout-hints (Claude):** 1,8 → Kijk naar het cijfer direct na de tienden. Vanaf 5 ga je naar boven. · 1,88 → Eén cijfer achter de komma, dus je rondt af op tienden.
    - **Uitleg (Claude):** Kijk naar het tweede cijfer achter de komma: 7. Is dat 5 of meer, dan rond je naar boven af. Anders naar beneden. 1,878 wordt 1,9.
  - `G7-GET-02-claude-bank-006` (Claude B12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt precies 1,974 kg. Rond af op één cijfer achter de komma.
    - **Antwoord:** 2,0  (controle: ok)
    - **Fout-hints (Claude):** 1,9 → Kijk naar het cijfer direct na de tienden. Vanaf 5 ga je naar boven. · 1,97 → Eén cijfer achter de komma, dus je rondt af op tienden.
    - **Uitleg (Claude):** Kijk naar het tweede cijfer achter de komma: 7. Is dat 5 of meer, dan rond je naar boven af. Anders naar beneden. 1,974 wordt 2,0.

- **Hint 1 (te schrijven):** Welke twee getallen met één cijfer achter de komma liggen vlak bij het gewicht?
- **Hint 2 (te schrijven):** Kijk naar het tweede cijfer achter de komma, de honderdsten. Is het vijf of meer, dan gaan de tienden één omhoog. Anders blijven de tienden gelijk. Schrijf maar één cijfer achter de komma.
- **Ouderzin:** Je kind rondt een kommagetal af op één cijfer achter de komma.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiende ernaast` (fout = antwoord ± 0,1) → Dat is een tiende ernaast. Kijk naar het tweede cijfer achter de komma: is het vijf of meer, of minder dan vijf?  [nieuw]
  - `te veel cijfers achter de komma` (Claudes sleutel: plaatswaarde-verkeerd) → Hoeveel cijfers staan er achter de komma? Je rondt af op één cijfer achter de komma, dus op tienden.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond af op tienden: kijk naar het tweede cijfer achter de komma.  [nieuw]
- Status: hints klaar
