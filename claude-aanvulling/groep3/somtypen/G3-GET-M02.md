# G3-GET-M02 — Snel zien hoeveel er zijn

Onze omschrijving: Hoeveelheden ≤20 vlot overzien/verkort tellen (vijfstructuur) · in onze bank: 8 items

Claude-vragen gemapt: **109** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [groepjes] Hoeveel [ding] zie je?

- Items: **56** · Claude-doelen: D0-2 (56) · regel: R15-groepjes
- Getallenruimte: 0–20 · type: meerkeuze
- Denkfouten (Claude): een-ernaast (53), grafiek-verkeerd-afgelezen (30), deel-vergeten-bij-splitsen (29)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M02-claude-bank-084` (Claude D0-2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel rechthoeken zie je?
    - **Tekening:** `{"vorm": "rechthoek", "soort": "groepjes", "aantal": 13, "perrij": 10}`
    - **Opties:** A) 20 · B) 13 · C) 12
    - **Antwoord:** 13  (controle: ok)
    - **Fout-hints (Claude):** 12 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M02-claude-bank-075` (Claude D0-2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel driehoeken zie je?
    - **Tekening:** `{"vorm": "driehoek", "soort": "groepjes", "aantal": 17, "perrij": 10}`
    - **Opties:** A) 17 · B) 16 · C) 18
    - **Antwoord:** 17  (controle: ok)
    - **Fout-hints (Claude):** 18 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Kijk naar de rijen. Hoeveel staan er in een volle rij?
- **Hint 2 (te schrijven):** Tel eerst de volle rijen. Tel daarna de rest één voor één erbij. Wijs elke vorm maar één keer aan.
- **Ouderzin:** Je kind telt vormen in rijtjes tot 20 handig: eerst de volle rijen, dan de rest.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = antwoord ± 1) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `te veel` (fout = antwoord + 2 of meer) → Dat zijn er te veel. Wijs elke vorm maar één keer aan. Tel eerst de volle rijen en dan de rest.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Je bent er een paar vergeten. Tel ook de losse vormen erbij.  [nieuw]
- Status: hints klaar

## Somtype 2: [groepjes] Hoeveel [ding] moeten er nog bij om # te maken?

- Items: **43** · Claude-doelen: D0-2 (43) · regel: R15-groepjes
- Getallenruimte: 0–20 · type: meerkeuze
- Denkfouten (Claude): een-ernaast (52), getal-overgenomen (29), grafiek-verkeerd-afgelezen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M02-claude-bank-013` (Claude D0-2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel cirkels moeten er nog bij om 20 te maken?
    - **Tekening:** `{"vorm": "cirkel", "soort": "groepjes", "aantal": 12, "perrij": 5}`
    - **Opties:** A) 9 · B) 3 · C) 8
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M02-claude-bank-017` (Claude D0-2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel vierkanten moeten er nog bij om 20 te maken?
    - **Tekening:** `{"vorm": "vierkant", "soort": "groepjes", "aantal": 13, "perrij": 10}`
    - **Opties:** A) 7 · B) 6 · C) 13
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 13 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking. · 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Hoeveel zie je er al? En hoeveel moeten er dan nog bij tot het getal uit de vraag?
- **Hint 2 (te schrijven):** Tel eerst hoeveel er al zijn. Tel dan verder tot het getal uit de vraag, en houd bij hoeveel stappen je zet. Een volle rij helpt je bij het tellen.
- **Ouderzin:** Je kind zoekt hoeveel er nog bij moeten om tot 20 aan te vullen, met een plaatje in rijtjes.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = antwoord ± 1) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `al geteld` (fout = het aantal in de tekening) → Zoveel zie je er al. De vraag is hoeveel er nog bij moeten.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat zijn er te weinig. Tel eerst hoeveel er al zijn. Tel dan verder tot het getal uit de vraag.  [nieuw]
- Status: hints klaar

## Somtype 3: [tienstaven/blokjes leggen] Leg # [ding] een tienstaaf en losse blokjes. Hoeveel losse blokjes leg je?

- Items: **9** · Claude-doelen: D0-4 (9) · regel: D-tien plus enen (R08-tientallen)
- Getallenruimte: 0–12, 0–20 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-M02-claude-bank-101` (Claude D0-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 18 met een tienstaaf en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 18 is 1 tien, 8 een. Leg eerst de grootste blokken.
  - `G3-GET-M02-claude-bank-100` (Claude D0-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 11 met een tienstaaf en losse blokjes. Hoeveel losse blokjes leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 11 is 1 tien, 1 een. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Het getal is een tien en losse. De tien leg je met de tienstaaf.
- **Hint 2 (te schrijven):** Kijk naar het laatste cijfer van het getal. Zoveel losse blokjes leg je naast de tienstaaf.
- **Ouderzin:** Je kind ziet hoeveel enen (losse blokjes) er naast de tien (tienstaaf) horen in een getal tot 20.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien vergeten` (fout = getal1) → Dat is het hele getal. De tienstaaf is al tien. Hoeveel losse blokjes leg je erbij?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Kijk nog eens naar het laatste cijfer van het getal.  [nieuw]
  - `andere fout` (andere fout) → Je legt één tienstaaf. Dat is de tien. Hoeveel losse blokjes leg je er nog naast? Kijk naar het laatste cijfer.  [nieuw]
- Status: hints klaar

## Somtype 4: [tienstaven/blokjes leggen] Leg # [ding] tienstaven. Hoeveel tienstaven leg je?

- Items: **1** · Claude-doelen: D0-4 (1) · regel: D-tien plus enen (R08-tientallen)
- Getallenruimte: 0–20 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-M02-claude-bank-109` (Claude D0-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Leg 20 met tienstaven. Hoeveel tienstaven leg je?
    - **UI:** tienstaven/blokjes leggen
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 20 is 2 tien. Leg eerst de grootste blokken.

- **Hint 1 (te schrijven):** Een tienstaaf is een tien. Hoeveel tienen zitten er in het getal?
- **Hint 2 (te schrijven):** Tel met tienen: bij elke staaf komt er tien bij. Stop als je bij het getal bent. Hoeveel staven heb je dan?
- **Ouderzin:** Je kind ziet hoeveel tienen (tienstaven) er in een rond getal tot 20 zitten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één tien` (fout = getal1) → Dat is het hele getal. Elke tienstaaf is tien. Hoeveel tienstaven heb je nodig?  [nieuw]
  - `tien te veel` (fout = antwoord + 8 (één tienstaaf = tien)) → Dat is één tienstaaf. Leg er nog een bij en tel met tienen.  [nieuw]
  - `andere fout` (andere fout) → Tel met tienen tot je bij het getal bent. Hoeveel tienstaven heb je dan gelegd?  [nieuw]
- Status: hints klaar
