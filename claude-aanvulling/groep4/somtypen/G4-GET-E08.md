# G4-GET-E08 — Delen tot honderd

Onze omschrijving: Delen informeel ≤100 (ook niet-opgaand) · in onze bank: 8 items

Claude-vragen gemapt: **43** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Er zijn # [ding]. In/aan elk(e) [bak] zitten # [ding]. Hoeveel [ding] zijn er?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Er zijn # [ding]. In/aan elk(e) [bak] zitten # [ding]. Hoeveel [ding] zijn er?” (koppeling: claudeId)
- Items: **40** · Claude-doelen: D5-2 (22), D5-3 (15), D5-5 (3) · regel: G12-groepjes-maken
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (70), getal-overgenomen (10)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G4-GET-E08-claude-bank-026` (Claude D5-2, bank, niveau 3 → toepassen)
    - **Opgave:** Er zijn 10 eieren. In elke mand zitten 2 eieren. Hoeveel manden zijn er?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G4-GET-E08-claude-bank-040` (Claude D5-3, bank, niveau 3 → toepassen)
    - **Opgave:** Er zijn 12 stiften. In elke koker zitten 3 stiften. Hoeveel kokers zijn er?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Verdeel alles in groepjes die even groot zijn. Hoeveel groepjes kun je maken?
- **Hint 2 (te schrijven):** Tel in sprongen van het aantal in één groepje, tot je bij het totaal bent. Tel hoeveel sprongen je maakt.
- **Ouderzin:** Je kind rekent uit hoeveel even grote groepjes je kunt maken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Maak groepjes en tel hoeveel groepjes het zijn.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt de getallen keer elkaar gedaan. Je moet verdelen: hoeveel groepjes kun je maken?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één groepje te veel. Tel je sprongen nog eens.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één groepje te weinig. Tel je sprongen nog eens.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat zijn te veel groepjes. Doe in elk groepje precies zoveel als in de vraag staat.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat zijn te weinig groepjes. Tel door in sprongen tot alles op is.  [nieuw]
  - `andere fout` (andere fout) → Maak groepjes die even groot zijn. Tel hoeveel groepjes je kunt maken.  [nieuw]
- Status: hints klaar

## Somtype 2: Je hebt # [ding]. In/aan elk(e) [bak] passen # [ding]. Hoeveel doosjes kun je helemaal vullen en hoeveel eieren blijven over?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Je hebt # [ding]. In/aan elk(e) [bak] passen # [ding]. Hoeveel doosjes kun je helemaal vullen en hoeveel eieren blijven over?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): rest-vergeten (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een doosje telt pas mee als het helemaal vol is. Kijk hoeveel eieren er in het laatste doosje zitten.”)
- Voorbeelden:
  - `G4-GET-E08-claude-bank-048` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 17 eieren. In elk doosje passen 6 eieren. Hoeveel doosjes kun je helemaal vullen en hoeveel eieren blijven over?
    - **Opties:** A) 2 doosjes en 3 over · B) 2 doosjes en 5 over · C) 3 doosjes
    - **Antwoord:** 2 doosjes en 5 over  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3 doosjes → Een doosje telt pas mee als het helemaal vol is. Kijk hoeveel eieren er in het laatste doosje zitten. · 2 doosjes en 3 over → Tel eerst hoeveel eieren er in de volle doosjes gaan. Haal dat aantal van 17 af.
    - **Uitleg (Claude):** In 2 volle doosjes gaan 12 eieren. Van 17 blijven er dan 5 over, en dat is te weinig voor een vol doosje.

- **Hint 1 (te schrijven):** Vul de doosjes één voor één. Hoeveel doosjes worden er helemaal vol?
- **Hint 2 (te schrijven):** Tel in sprongen van het aantal dat in één doosje past. Stop voor je over het totaal heen gaat. Hoeveel eieren houd je dan nog over?
- **Ouderzin:** Je kind verdeelt in groepjes en kijkt wat er overblijft.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 3: Je hebt # [ding]. In/aan elk(e) [bak] passen # [ding]. Hoeveel zakjes kun je helemaal vullen en hoeveel knikkers blijven over?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Je hebt # [ding]. In/aan elk(e) [bak] passen # [ding]. Hoeveel zakjes kun je helemaal vullen en hoeveel knikkers blijven over?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Merge-fixlijst: #11 labels gelijk (1)
- Denkfouten (Claude): rest-vergeten (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk of het laatste zakje echt vol is. Er moeten 4 knikkers in.”)
- Voorbeelden:
  - `G4-GET-E08-claude-bank-049` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 13 knikkers. In elk zakje passen 4 knikkers. Hoeveel zakjes kun je helemaal vullen en hoeveel knikkers blijven over?
    - **Opties:** A) 4 zakjes en 0 over · B) 3 zakjes en 2 over · C) 3 zakjes en 1 over
    - **Antwoord:** 3 zakjes en 1 over  (controle: ok)
    - **Fout-hints (Claude):** 4 zakjes en 0 over → Kijk of het laatste zakje echt vol is. Er moeten 4 knikkers in. · 3 zakjes en 2 over → Tel nog eens hoeveel knikkers er in 3 volle zakjes zitten.
    - **Uitleg (Claude):** Drie volle zakjes zijn 3 keer 4 is 12 knikkers. Je had er 13, dus blijft er 1 over. Dat ene zakje is niet vol.

- **Hint 1 (te schrijven):** Vul de zakjes één voor één. Hoeveel zakjes worden er helemaal vol?
- **Hint 2 (te schrijven):** Tel in sprongen van het aantal dat in één zakje past. Stop voor je over het totaal heen gaat. Hoeveel knikkers houd je dan nog over?
- **Ouderzin:** Je kind verdeelt in groepjes en kijkt wat er overblijft.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rest vergeten` (4 zakjes en 0 over) → Kijk of het laatste zakje echt vol is. Er moeten 4 knikkers in.  [Claude, ok]
  - `rest fout` (3 zakjes en 2 over) → 3 volle zakjes klopt. Hoeveel knikkers zitten daarin? Hoeveel houd je dan over van de 13?  [nieuw]
- Status: hints klaar

## Somtype 4: [getallenlijn] Je springt op de getallenlijn van # naar # [ding] sprongen van #. Hoeveel sprongen maak je?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Je springt op de getallenlijn van # naar # [ding] stappen van #. Hoeveel sprongen maak je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): getallenlijn 0–20 met 3 en 15 gemarkeerd (fixlijst #14)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “Je springt op de getallenlijn van # naar # [ding] stappen van #. Hoeveel sprongen maak je?”. Hints nakijken.
- Merge-fixlijst: #14 getallenlijn (1), #24 sprongen (1)
- Denkfouten (Claude): een-ernaast (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het getal waar je start, telt niet als sprong. Noem de getallen hardop waar je landt.”)
- Voorbeelden:
  - `G4-GET-E08-claude-bank-050` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Je springt op de getallenlijn van 3 naar 15 met sprongen van 3. Hoeveel sprongen maak je?
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 20, "stap": 1, "labels": [0, 5, 10, 15, 20], "gemarkeerd": [3, 15]}`
    - **Opties:** A) 4 sprongen · B) 5 sprongen · C) 12 sprongen
    - **Antwoord:** 4 sprongen  (controle: ok)
    - **Fout-hints (Claude):** 5 sprongen → Het getal waar je start, telt niet als sprong. Noem de getallen hardop waar je landt. · 12 sprongen → 12 is het verschil tussen de getallen, niet het aantal sprongen. Elke sprong is 3 groot.
    - **Uitleg (Claude):** Je landt op 6, 9, 12 en 15. Dat zijn 4 sprongen van 3.

- **Hint 1 (te schrijven):** Begin bij het eerste getal. Waar kom je na één sprong?
- **Hint 2 (te schrijven):** Spring steeds even ver, tot je bij het laatste getal bent. Tel alleen de sprongen, niet het getal waar je begint.
- **Ouderzin:** Je kind telt hoeveel even grote sprongen er passen tussen twee getallen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `begin meegeteld` (5 sprongen) → Het getal waar je start, telt niet als sprong. Noem de getallen hardop waar je landt.  [Claude, ok]
  - `het verschil` (12 sprongen) → Van 3 naar 15 is 12 verder. Dat is niet het aantal sprongen. Elke sprong is 3 groot.  [nieuw]
- Status: hints klaar
