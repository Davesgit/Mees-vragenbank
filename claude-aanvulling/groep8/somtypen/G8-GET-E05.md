# G8-GET-E05 — Rekenmachine slim gebruiken, of juist niet

Onze omschrijving: Rekenmachine: reeksen; wanneer RM vs hoofd/papier · in onze bank: 8 items

Claude-vragen gemapt: **125** in **16** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **13** · Claude-doelen: T4 (13) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (20), andere-deel-genomen (6)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-053` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een kist passen 2 boeken. Er zijn 45 boeken. Op de rekenmachine staat 22,5. Hoeveel kisten zijn er nodig?
    - **Antwoord:** 23  (controle: ok)
    - **Fout-hints (Claude):** 24 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-059` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een kist passen 25 boeken. Er zijn 624 boeken. Op de rekenmachine staat 24,96. Hoeveel kisten zijn er nodig?
    - **Antwoord:** 25  (controle: ok)
    - **Fout-hints (Claude):** 26 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 48 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: T4 (12) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (16), andere-deel-genomen (8)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-045` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een doos passen 4 eieren. Er zijn 37 eieren. Op de rekenmachine staat 9,25. Hoeveel dozen zijn er nodig?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 9 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-047` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een doos passen 20 eieren. Er zijn 762 eieren. Op de rekenmachine staat 38,1. Hoeveel dozen zijn er nodig?
    - **Antwoord:** 39  (controle: ok)
    - **Fout-hints (Claude):** 38 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 40 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **11** · Claude-doelen: T4 (11) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (18), andere-deel-genomen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-090` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een mand passen 4 peren. Er zijn 33 peren. Op de rekenmachine staat 8,25. Hoeveel manden zijn er nodig?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 8 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 10 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?
  - `G8-GET-E05-claude-bank-096` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een mand passen 20 peren. Er zijn 348 peren. Op de rekenmachine staat 17,4. Hoeveel manden zijn er nodig?
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** 25 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 8 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **10** · Claude-doelen: T4 (10) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (13), andere-deel-genomen (7)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-118` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een zak passen 2 appels. Er zijn 27 appels. Op de rekenmachine staat 13,5. Hoeveel zakken zijn er nodig?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 13 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-124` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een zak passen 8 appels. Er zijn 463 appels. Op de rekenmachine staat 57,875. Hoeveel zakken zijn er nodig?
    - **Antwoord:** 58  (controle: ok)
    - **Fout-hints (Claude):** 57 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 7 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: T4 (9) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (13), andere-deel-genomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-015` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een bak passen 4 potjes. Er zijn 95 potjes. Op de rekenmachine staat 23,75. Hoeveel bakken zijn er nodig?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 23 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 3 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-012` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een bak passen 8 potjes. Er zijn 532 potjes. Op de rekenmachine staat 66,5. Hoeveel bakken zijn er nodig?
    - **Antwoord:** 67  (controle: ok)
    - **Fout-hints (Claude):** 68 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 70 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: T4 (9) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (12), andere-deel-genomen (6)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-024` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een busje passen 2 kinderen. Er zijn 21 kinderen. Op de rekenmachine staat 10,5. Hoeveel busjes zijn er nodig?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 10 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-031` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een busje passen 4 kinderen. Er zijn 249 kinderen. Op de rekenmachine staat 62,25. Hoeveel busjes zijn er nodig?
    - **Antwoord:** 63  (controle: ok)
    - **Fout-hints (Claude):** 62 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle bakken gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle bakken gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T4 (8) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): andere-deel-genomen (10), kommagetal-als-geheel (6)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-003` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een bak passen 5 potjes. Er zijn 29 potjes. Op de rekenmachine staat 5,8. De volle bakken gaan weg. Hoeveel potjes blijven er over?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 8 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 5 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?
  - `G8-GET-E05-claude-bank-007` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een bak passen 8 potjes. Er zijn 285 potjes. Op de rekenmachine staat 35,625. De volle bakken gaan weg. Hoeveel potjes blijven er over?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten? · 8 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T4 (8) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (11), andere-deel-genomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-074` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een krat passen 4 flesjes. Er zijn 23 flesjes. Op de rekenmachine staat 5,75. Hoeveel kratten zijn er nodig?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 5 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 7 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?
  - `G8-GET-E05-claude-bank-077` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een krat passen 5 flesjes. Er zijn 258 flesjes. Op de rekenmachine staat 51,6. Hoeveel kratten zijn er nodig?
    - **Antwoord:** 52  (controle: ok)
    - **Fout-hints (Claude):** 54 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 3 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle manden gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle manden gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T4 (8) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): andere-deel-genomen (10), kommagetal-als-geheel (6)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-083` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een mand passen 8 peren. Er zijn 150 peren. Op de rekenmachine staat 18,75. De volle manden gaan weg. Hoeveel peren blijven er over?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 2 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten? · 8 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-086` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een mand passen 20 peren. Er zijn 348 peren. Op de rekenmachine staat 17,4. De volle manden gaan weg. Hoeveel peren blijven er over?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 4 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 12 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T4 (8) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): rest-vergeten (9), andere-deel-genomen (7)
- Verschillende Claude-fout-hints: 2 (meest: “Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-102` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een tas passen 2 knikkers. Er zijn 31 knikkers. Op de rekenmachine staat 15,5. Hoeveel tassen zijn er nodig?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 15 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-101` (Claude T4, bank, niveau 2 → toepassen)
    - **Opgave:** In een tas passen 25 knikkers. Er zijn 3063 knikkers. Op de rekenmachine staat 122,52. Hoeveel tassen zijn er nodig?
    - **Antwoord:** 123  (controle: ok)
    - **Fout-hints (Claude):** 124 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in? · 135 → Reken terug: klopt het als je de deling omdraait? Blijft er iets over? En moet dat wat overblijft ook nog ergens in?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle zakken gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle zakken gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: T4 (7) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (8), andere-deel-genomen (6)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-110` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een zak passen 5 appels. Er zijn 23 appels. Op de rekenmachine staat 4,6. De volle zakken gaan weg. Hoeveel appels blijven er over?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 6 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 4 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?
  - `G8-GET-E05-claude-bank-115` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een zak passen 25 appels. Er zijn 417 appels. Op de rekenmachine staat 16,68. De volle zakken gaan weg. Hoeveel appels blijven er over?
    - **Antwoord:** 17  (controle: ok)
    - **Fout-hints (Claude):** 16 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 8 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle busjes gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle busjes gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T4 (6) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): andere-deel-genomen (7), kommagetal-als-geheel (5)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-022` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een busje passen 5 kinderen. Er zijn 49 kinderen. Op de rekenmachine staat 9,8. De volle busjes gaan weg. Hoeveel kinderen blijven er over?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 8 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-021` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een busje passen 20 kinderen. Er zijn 371 kinderen. Op de rekenmachine staat 18,55. De volle busjes gaan weg. Hoeveel kinderen blijven er over?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 18 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 9 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 13: In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kratten gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kratten gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T4 (6) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): andere-deel-genomen (9), kommagetal-als-geheel (3)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-067` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een krat passen 4 flesjes. Er zijn 23 flesjes. Op de rekenmachine staat 5,75. De volle kratten gaan weg. Hoeveel flesjes blijven er over?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 1 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten? · 4 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-070` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een krat passen 25 flesjes. Er zijn 210 flesjes. Op de rekenmachine staat 8,4. De volle kratten gaan weg. Hoeveel flesjes blijven er over?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 8 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 25 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 14: In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kisten gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kisten gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: T4 (5) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (5), andere-deel-genomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-052` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een kist passen 4 boeken. Er zijn 27 boeken. Op de rekenmachine staat 6,75. De volle kisten gaan weg. Hoeveel boeken blijven er over?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 6 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 4 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-049` (Claude T4, bank, niveau 2 → toepassen)
    - **Opgave:** In een kist passen 40 boeken. Er zijn 2033 boeken. Op de rekenmachine staat 50,825. De volle kisten gaan weg. Hoeveel boeken blijven er over?
    - **Antwoord:** 33  (controle: ok)
    - **Fout-hints (Claude):** 50 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 7 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 15: In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle dozen gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle dozen gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: T4 (3) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (3), andere-deel-genomen (3)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-035` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een doos passen 25 eieren. Er zijn 739 eieren. Op de rekenmachine staat 29,56. De volle dozen gaan weg. Hoeveel eieren blijven er over?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 56 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 11 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-034` (Claude T4, bank, niveau 2 → toepassen)
    - **Opgave:** In een doos passen 50 eieren. Er zijn 2445 eieren. Op de rekenmachine staat 48,9. De volle dozen gaan weg. Hoeveel eieren blijven er over?
    - **Antwoord:** 45  (controle: ok)
    - **Fout-hints (Claude):** 48 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 5 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 16: In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle tassen gaan weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle tassen gaan weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T4 (2) · regel: G8-T4-rekenmachine
- Getallenruimte: kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (2), andere-deel-genomen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter?”)
- Voorbeelden:
  - `G8-GET-E05-claude-bank-100` (Claude T4, bank, niveau 1 → basis)
    - **Opgave:** In een tas passen 8 knikkers. Er zijn 325 knikkers. Op de rekenmachine staat 40,625. De volle tassen gaan weg. Hoeveel knikkers blijven er over?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 40 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 8 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G8-GET-E05-claude-bank-099` (Claude T4, bank, niveau 2 → toepassen)
    - **Opgave:** In een tas passen 50 knikkers. Er zijn 3681 knikkers. Op de rekenmachine staat 73,62. De volle tassen gaan weg. Hoeveel knikkers blijven er over?
    - **Antwoord:** 31  (controle: ok)
    - **Fout-hints (Claude):** 73 → Kijk eerst naar het eerste cijfer achter de komma: dat zijn de tienden. Welke is groter? · 19 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
