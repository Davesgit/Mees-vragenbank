# G6-GET-E09 — Breuken aanvullen tot 1 en deel ván

Onze omschrijving: Breuken: aanvullen tot 1; breuk als operator (informeel) · in onze bank: 8 items

Claude-vragen gemapt: **604** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is #/# van €#?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Hoeveel is #/# van €#?” (koppeling: claudeId)
- Items: **399** · Claude-doelen: B2 (399) · regel: G6-B03-deel-van
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 12), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Uit de G5-park: 399 items
- Denkfouten (Claude): een-ernaast (331), getal-overgenomen (187), deel-vergeten-bij-splitsen (179), andere-deel-genomen (101)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-GET-E09-claude-bank-489` (Claude B2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 3/5 van €6?
    - **Antwoord:** €3,60  (controle: ok)
    - **Fout-hints (Claude):** €1,20 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · €4,80 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-GET-E09-claude-bank-335` (Claude B2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 3/10 van €35?
    - **Antwoord:** €10,50  (controle: ok)
    - **Fout-hints (Claude):** €14 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · €7 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Verdeel het bedrag eerst in zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel is één stuk? Komt dat niet uit in hele euro's? Reken dan met centen.
- **Hint 2 (te schrijven):** Eén stuk is het bedrag gedeeld door de noemer (onder de streep). Neem zoveel stukken als de teller (boven de streep) zegt. Hoeveel is dat samen?
- **Ouderzin:** Je kind rekent een breuk van een bedrag uit: eerst één gelijk stuk, dan zoveel stukken als de teller zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele bedrag` (fout = de prijs) → Dat is het hele bedrag. Verdeel het bedrag eerst in zoveel gelijke stukken als de noemer zegt. Neem dan zoveel stukken als de teller zegt.  [nieuw]
  - `één stuk` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is één stuk. Neem nu zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `wat overblijft` (Claudes sleutel: andere-deel-genomen) → Is dat wat er overblijft? Je zoekt zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `stuk te veel of te weinig` (Claudes sleutel: een-ernaast) → Kijk nog eens naar de teller. Neem je precies zoveel stukken als de teller zegt? Reken eerst uit hoeveel één stuk is.  [Claude, taalfix]
  - `andere fout` (andere fout) → Verdeel het bedrag in zoveel gelijke stukken als de noemer zegt. Neem dan zoveel stukken als de teller zegt. Reken zo nodig met centen.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoeveel is #/# van #?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel is #/# van #?” (koppeling: claudeId)
- Items: **193** · Claude-doelen: B2 (193) · regel: G6-B03-deel-van
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Uit de G5-park: 193 items
- Denkfouten (Claude): een-ernaast (166), getal-overgenomen (86), deel-vergeten-bij-splitsen (81), andere-deel-genomen (53)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-GET-E09-claude-bank-140` (Claude B2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 3/8 van 32?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 8 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-GET-E09-claude-bank-034` (Claude B2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 3/10 van 20?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 14 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** Verdeel het getal eerst in zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel is één stuk?
- **Hint 2 (te schrijven):** Eén stuk is het getal gedeeld door de noemer (onder de streep). Neem zoveel stukken als de teller (boven de streep) zegt. Hoeveel is dat samen?
- **Ouderzin:** Je kind rekent een breuk van een getal uit: eerst één gelijk stuk, dan zoveel stukken als de teller zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één stuk (regel)` (fout = één stuk (het aantal : de noemer)) → Dat is één stuk. Neem nu zoveel stukken als de teller zegt.  [nieuw]
  - `één stuk` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is één stuk. Neem nu zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Is dat een getal uit de vraag? Verdeel het getal eerst in zoveel gelijke stukken als de noemer zegt. Hoeveel is één stuk?  [nieuw]
  - `wat overblijft` (Claudes sleutel: andere-deel-genomen) → Is dat wat er overblijft? Je zoekt zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `stuk te veel of te weinig` (Claudes sleutel: een-ernaast) → Kijk nog eens naar de teller. Neem je precies zoveel stukken als de teller zegt? Reken eerst uit hoeveel één stuk is.  [Claude, taalfix]
  - `andere fout` (andere fout) → Verdeel het getal in zoveel gelijke stukken als de noemer zegt. Neem dan zoveel stukken als de teller zegt.  [nieuw]
- Status: hints klaar

## Somtype 3: [wie] krijgt #/# van # [ding]. Hoeveel [ding] is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[wie] krijgt #/# van # [ding]. Hoeveel [ding] is dat?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: B14 (12) · regel: G6-B14-operator
- Getallenruimte: breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): niet-verdeeld (19), verkeerde-bewerking (11)
- Verschillende Claude-fout-hints: 10 (meest: “Je bent het delen door de noemer vergeten.”)
- Voorbeelden:
  - `G6-GET-E09-claude-bank-599` (Claude B14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sem krijgt 5/8 van 48 stickers. Hoeveel stickers is dat?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** 6 → Dat is 1/8. Vermenigvuldig nog met 5. · 240 → Je bent het delen door de noemer vergeten. · 18 → Dat is wat overblijft. De vraag is wat het kind krijgt.
    - **Uitleg (Claude):** 5/8 × 48 = 5 × 48 : 8. 48 : 8 = 6, keer 5 = 30.
  - `G6-GET-E09-claude-bank-596` (Claude B14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sem krijgt 1/6 van 18 knikkers. Hoeveel knikkers is dat?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 18 → Je bent het delen door de noemer vergeten. · 15 → Dat is wat overblijft. De vraag is wat de dino krijgt.
    - **Uitleg (Claude):** 1/6 × 18 = 1 × 18 : 6. 18 : 6 = 3, keer 1 = 3.

- **Hint 1 (te schrijven):** Verdeel alles eerst in zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel is één stuk?
- **Hint 2 (te schrijven):** Eén stuk is het aantal gedeeld door de noemer (onder de streep). Neem zoveel stukken als de teller (boven de streep) zegt. Hoeveel is dat samen?
- **Ouderzin:** Je kind rekent uit hoeveel iemand krijgt bij een breuk van een aantal: eerst één gelijk stuk, dan zoveel stukken als de teller zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één stuk` (fout = één stuk (het aantal : de noemer)) → Dat is één stuk. Neem nu zoveel stukken als de teller zegt.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Is dat een getal uit de vraag? Verdeel alles eerst in zoveel gelijke stukken als de noemer zegt. Hoeveel is één stuk?  [nieuw]
  - `wat overblijft` (Claudes sleutel: verkeerde-bewerking) → Is dat wat er overblijft? Je zoekt zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `niet verdeeld` (Claudes sleutel: niet-verdeeld) → Kijk nog eens naar de breuk. Heb je alles eerst verdeeld in zoveel gelijke stukken als de noemer zegt? Neem dan zoveel stukken als de teller zegt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Verdeel alles in zoveel gelijke stukken als de noemer zegt. Neem dan zoveel stukken als de teller zegt.  [nieuw]
- Status: hints klaar
