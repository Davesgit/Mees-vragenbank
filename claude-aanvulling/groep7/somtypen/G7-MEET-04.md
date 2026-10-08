# G7-MEET-04 — Tijd en temperatuur

Onze omschrijving: Tijd en temperatuur · in onze bank: 8 items

Claude-vragen gemapt: **556** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel dagen duurt het van # [ding] tot # [ding]?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Hoeveel dagen duurt het van # [ding] tot # [ding]?” (koppeling: claudeId)
- Items: **220** · Claude-doelen: M10 (220) · regel: G7-G5P7-dagen-tussen-datums
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): kalender-verkeerd-geteld (334), deel-vergeten-bij-splitsen (106)
- Verschillende Claude-fout-hints: 4 (meest: “Bijna! Dat is één dag te veel. De dag waarop je begint, tel je niet mee. Kijk ook hoeveel dagen elke maand heeft.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-427` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel dagen duurt het van 6 mei tot 16 juli?
    - **Antwoord:** 71  (controle: ok)
    - **Fout-hints (Claude):** 55 → Dat is te weinig. Heb je alle stukken opgeteld? Tel de dagen tot het eind van de eerste maand, de hele maanden ertussen, en de dagen in de laatste maand. · 72 → Bijna! Dat is één dag te veel. De dag waarop je begint, tel je niet mee. Kijk ook hoeveel dagen elke maand heeft. · 70 → Bijna! Dat is één dag te weinig. Kijk hoeveel dagen elke maand heeft: dertig of eenendertig? Tel tot en met de laatste dag.
  - `G7-MEET-04-claude-bank-552` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel dagen duurt het van 6 augustus tot 20 oktober?
    - **Antwoord:** 75  (controle: ok)
    - **Fout-hints (Claude):** 81 → Dat is te veel. Tel in stukken: de dagen tot het eind van de eerste maand, de hele maanden ertussen, en de dagen in de laatste maand. · 76 → Bijna! Dat is één dag te veel. De dag waarop je begint, tel je niet mee. Kijk ook hoeveel dagen elke maand heeft. · 74 → Bijna! Dat is één dag te weinig. Kijk hoeveel dagen elke maand heeft: dertig of eenendertig? Tel tot en met de laatste dag.

- **Hint 1 (te schrijven):** Begin bij de maand waarin je start. Hoeveel dagen heeft die maand: dertig of eenendertig? Tel de dagen tot het eind van die maand.
- **Hint 2 (te schrijven):** De begindag tel je niet mee. Tel daarna de hele maanden ertussen erbij, als die er zijn. Tel tot slot de dagen in de maand van de einddag erbij, tot en met die dag.
- **Ouderzin:** Je kind telt hoeveel dagen het is van de ene datum tot de andere, over een paar maanden heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hele beginmaand geteld` (fout = antwoord + getal1) → Dat is te veel. Tel in de maand waarin je begint alleen de dagen na de begindag.  [nieuw]
  - `maand van de einddag vergeten` (fout = antwoord - getal2) → Dat is te weinig. Tel je de dagen in de maand van de einddag ook mee?  [nieuw]
  - `twee dagen te weinig` (fout = antwoord - 2) → Dat is twee dagen te weinig. Kijk bij elke maand: heeft hij dertig of eenendertig dagen?  [nieuw]
  - `één dag ernaast` (fout = antwoord ± 1) → Je zit er één dag naast. Kijk bij elke maand: dertig of eenendertig dagen? De begindag tel je niet mee, de einddag wel.  [nieuw]
  - `dag uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel dagen het duurt.  [nieuw]
  - `andere fout` (andere fout) → Tel de dagen tot het eind van de maand waarin je begint, de hele maanden ertussen, en de dagen in de maand van de einddag.  [nieuw]
- Status: hints klaar

## Somtype 2: Het is −# graden. Het wordt # graden warmer. Hoe warm is het dan?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Het is −# graden. Het wordt # graden warmer. Hoe warm is het dan?” (koppeling: claudeId)
- Items: **148** · Claude-doelen: C20 (148) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (149), teken-vergeten (75), verkeerde-bewerking (72)
- Verschillende Claude-fout-hints: 3 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-141` (Claude C20, bank, niveau 2 → toepassen)
    - **Opgave:** Het is −11 graden. Het wordt 14 graden warmer. Hoe warm is het dan?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** −3 → Teken een getallenlijn met nul in het midden. Waar sta je, waar ga je heen? · 4 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-MEET-04-claude-bank-193` (Claude C20, bank, niveau 2 → toepassen)
    - **Opgave:** Het is −6 graden. Het wordt 14 graden warmer. Hoe warm is het dan?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** −8 → Teken een getallenlijn met nul in het midden. Waar sta je, waar ga je heen? · −20 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. Het wordt warmer, dus je telt omhoog.
- **Hint 2 (te schrijven):** Tel eerst omhoog tot nul: dat zijn evenveel graden als het onder nul was. Hoeveel graden moet je dan nog verder? Zoveel graden boven nul wordt het.
- **Ouderzin:** Je kind rekent met temperaturen onder nul: het wordt een aantal graden warmer, hoe warm wordt het dan?
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `onder nul gebleven` (Claudes sleutel: teken-vergeten) → Dat is onder nul. Het wordt zoveel warmer dat je boven nul uitkomt: typ dan geen min.  [Claude, taalfix]
  - `kouder in plaats van warmer` (Claudes sleutel: verkeerde-bewerking) → Dat is nog kouder dan het was. Het wordt warmer: de temperatuur gaat omhoog.  [Claude, taalfix]
  - `één graad ernaast` (fout = antwoord ± 1) → Je zit er één graad naast. Tel de stappen tot nul en de stappen vanaf nul apart, en tel ze dan op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt de temperatuur als het warmer is geworden.  [nieuw]
  - `onder nul uitgekomen` (Claudes sleutel (alle, zonder label)) → Dat is onder nul. Het wordt zoveel warmer dat je boven nul uitkomt. Tel eerst omhoog tot nul, en dan verder boven nul.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel omhoog tot nul, en dan verder boven nul.  [nieuw]
- Status: hints klaar

## Somtype 3: Het is −# graden. Later is het # graden. Hoeveel graden is het warmer geworden?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Het is −# graden. Later is het # graden. Hoeveel graden is het warmer geworden?” (koppeling: claudeId)
- Items: **144** · Claude-doelen: C20 (144) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (212), teken-vergeten (76)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-253` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is −12 graden. Later is het 1 graad. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 13  (controle: n.v.t.)
    - **Fout-hints (Claude):** −11 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · 14 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-MEET-04-claude-bank-247` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is −6 graden. Later is het 1 graad. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 7  (controle: n.v.t.)
    - **Fout-hints (Claude):** −5 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · 6 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. Hoeveel stappen zijn het van de koude temperatuur naar de warme?
- **Hint 2 (te schrijven):** Tel de graden van de temperatuur onder nul tot nul. Tel daarna de graden van nul tot de nieuwe temperatuur. Tel die twee aantallen bij elkaar op.
- **Ouderzin:** Je kind rekent uit hoeveel graden het warmer is geworden, van onder nul naar boven nul.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `met een min` (Claudes sleutel: teken-vergeten) → Hoeveel graden het warmer is geworden, is een aantal graden. Dat typ je zonder min.  [Claude, taalfix]
  - `de nieuwe temperatuur` (fout = getal2) → Dat is de nieuwe temperatuur. De vraag is hoeveel graden het warmer is geworden: tel ook de graden onder nul mee.  [nieuw]
  - `verschil van de getallen` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het verschil van de twee getallen. Maar je gaat eerst omhoog tot nul en dan verder: dat zijn twee stukken.  [nieuw]
  - `één graad ernaast` (fout = antwoord ± 1) → Je zit er één graad naast. Tel de stappen tot nul en de stappen vanaf nul apart, en tel ze dan op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel graden het warmer is geworden.  [nieuw]
  - `aantal met een min` (Claudes sleutel (alle, zonder label)) → Hoeveel graden het warmer is geworden, is een aantal graden: dat is nooit onder nul. Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 4: Het is # graden in [plek]. 's Nachts daalt de temperatuur # graden. Hoeveel graden is het dan? (Typ een min voor een getal onder nul, bijvoorbeeld −#.)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Het is # graden in [plek]. 's Nachts daalt de temperatuur # graden. Hoeveel graden is het dan? (Typ een min voor een getal onder nul, bijvoorbeeld −#.)” (koppeling: claudeId)
- Items: **24** · Claude-doelen: M28 (24) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): teken-vergeten (24), een-ernaast (24)
- Verschillende Claude-fout-hints: 25 (meest: “Je komt onder nul: het antwoord heeft een min ervoor.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-031` (Claude M28, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Het is 7 graden in de vallei. 's Nachts daalt de temperatuur 17 graden. Hoeveel graden is het dan? (Typ een min voor een getal onder nul, bijvoorbeeld −3.)
    - **Antwoord:** −10  (controle: ok)
    - **Fout-hints (Claude):** 10 → Je komt onder nul: het antwoord heeft een min ervoor. · −11 → Van 7 naar 0 is 7 graden, dan nog 10.
    - **Uitleg (Claude):** Van 7 naar 0 is 7 graden. Dan nog 10 graden verder onder nul: −10.
  - `G7-MEET-04-claude-bank-038` (Claude M28, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Het is 2 graden op de kinderboerderij. 's Nachts daalt de temperatuur 9 graden. Hoeveel graden is het dan? (Typ een min voor een getal onder nul, bijvoorbeeld −3.)
    - **Antwoord:** −7  (controle: ok)
    - **Fout-hints (Claude):** 7 → Je komt onder nul: het antwoord heeft een min ervoor. · −8 → Van 2 naar 0 is 2 graden, dan nog 7.
    - **Uitleg (Claude):** Van 2 naar 0 is 2 graden. Dan nog 7 graden verder onder nul: −7.

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. De temperatuur daalt, dus je telt omlaag.
- **Hint 2 (te schrijven):** Tel eerst omlaag tot nul: dat zijn evenveel graden als het boven nul was. Hoeveel graden moet je dan nog verder omlaag? Zoveel graden onder nul wordt het: typ een min voor dat getal.
- **Ouderzin:** Je kind rekent uit hoe koud het wordt als de temperatuur onder nul zakt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min vergeten` (fout = getal1 - getal2 of getal2 - getal1) → Je komt onder nul uit. Typ dan een min voor het getal.  [nieuw]
  - `één graad te koud` (Claudes sleutel: een-ernaast) → Dat is één graad te koud. Tel eerst de stappen tot nul. Ook van nul naar min één is een stap.  [Claude, taalfix]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt de temperatuur nadat hij is gedaald.  [nieuw]
  - `één graad te koud (alle)` (Claudes sleutel (alle, zonder label)) → Dat is één graad te koud. Tel eerst de stappen tot nul. Ook van nul naar min één is een stap.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel omlaag tot nul, en dan verder onder nul.  [nieuw]
- Status: hints klaar

## Somtype 5: 's Nachts is het in [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het warmer geworden?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “'s Nachts is het in [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het warmer geworden?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: C20 (9) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): teken-vergeten (18), tiental-ernaast (9)
- Verschillende Claude-fout-hints: 11 (meest: “Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-009` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 's Nachts was het bij het nest −4 graden. Overdag werd het 6 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 2 → Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul. · 6 → 6 is de temperatuur overdag. De vraag is hoeveel het gestegen is, vanaf −4. · 11 → Tel de stappen naar nul en de stappen vanaf nul apart, en tel ze dan op.
    - **Uitleg (Claude):** Ga via nul. Van −4 naar 0 is 4 graden. Van 0 naar 6 is 6 graden. Samen 4 + 6 = 10 graden.
  - `G7-MEET-04-claude-bank-004` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 's Nachts was het bij de kantine −4 graden. Overdag werd het 4 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 0 → Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul. · 4 → 4 is de temperatuur overdag. De vraag is hoeveel het gestegen is, vanaf −4. · 9 → Tel de stappen naar nul en de stappen vanaf nul apart, en tel ze dan op.
    - **Uitleg (Claude):** Ga via nul. Van −4 naar 0 is 4 graden. Van 0 naar 4 is 4 graden. Samen 4 + 4 = 8 graden.

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. Hoeveel stappen zijn het van de koude temperatuur naar de warme?
- **Hint 2 (te schrijven):** Tel de graden van de temperatuur onder nul tot nul. Tel daarna de graden van nul tot de nieuwe temperatuur. Tel die twee aantallen bij elkaar op.
- **Ouderzin:** Je kind rekent uit hoeveel graden het warmer is geworden, van onder nul naar boven nul.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de nieuwe temperatuur` (fout = getal2) → Dat is de nieuwe temperatuur. De vraag is hoeveel graden het warmer is geworden: tel ook de graden onder nul mee.  [nieuw]
  - `verschil van de getallen` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het verschil van de twee getallen. Maar je gaat eerst omhoog tot nul en dan verder: dat zijn twee stukken.  [nieuw]
  - `één graad ernaast` (fout = antwoord ± 1) → Je zit er één graad naast. Tel de stappen tot nul en de stappen vanaf nul apart, en tel ze dan op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel graden het warmer is geworden.  [nieuw]
  - `andere fout` (andere fout) → Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 6: 's Ochtends is het in [plek] −# graden. 's Middags is het # graden. Hoeveel graden is het warmer geworden?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “'s Ochtends is het in [plek] −# graden. 's Middags is het # graden. Hoeveel graden is het warmer geworden?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M28 (8) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): teken-vergeten (16)
- Verschillende Claude-fout-hints: 9 (meest: “Je hebt de min bij het begingetal genegeerd. Onder nul telt ook mee.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-013` (Claude M28, gegenereerd, niveau 1 → basis)
    - **Opgave:** 's Ochtends is het in de vallei −6 graden. 's Middags is het 3 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** −3 → Het begint onder nul. Tel eerst tot 0 (6 graden) en dan verder tot 3. · 3 → Je hebt de min bij het begingetal genegeerd. Onder nul telt ook mee.
    - **Uitleg (Claude):** Van −6 naar 0 is 6 graden. Van 0 naar 3 is 3 graden. Samen 6 + 3 = 9 graden.
  - `G7-MEET-04-claude-bank-016` (Claude M28, gegenereerd, niveau 1 → basis)
    - **Opgave:** 's Ochtends is het in de schuur −3 graden. 's Middags is het 2 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** −1 → Het begint onder nul. Tel eerst tot 0 (3 graden) en dan verder tot 2. · 1 → Je hebt de min bij het begingetal genegeerd. Onder nul telt ook mee.
    - **Uitleg (Claude):** Van −3 naar 0 is 3 graden. Van 0 naar 2 is 2 graden. Samen 3 + 2 = 5 graden.

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. Hoeveel stappen zijn het van de koude temperatuur naar de warme?
- **Hint 2 (te schrijven):** Tel de graden van de temperatuur onder nul tot nul. Tel daarna de graden van nul tot de nieuwe temperatuur. Tel die twee aantallen bij elkaar op.
- **Ouderzin:** Je kind rekent uit hoeveel graden het warmer is geworden, van onder nul naar boven nul.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de nieuwe temperatuur` (fout = getal2) → Dat is de nieuwe temperatuur. De vraag is hoeveel graden het warmer is geworden: tel ook de graden onder nul mee.  [nieuw]
  - `verschil van de getallen` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het verschil van de twee getallen. Maar je gaat eerst omhoog tot nul en dan verder: dat zijn twee stukken.  [nieuw]
  - `onder nul` (Claudes sleutel: teken-vergeten) → Dat is onder nul. Hoeveel graden het warmer is geworden, is een aantal graden: dat is nooit onder nul. Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [Claude, taalfix]
  - `één graad ernaast` (fout = antwoord ± 1) → Je zit er één graad naast. Tel de stappen tot nul en de stappen vanaf nul apart, en tel ze dan op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel graden het warmer is geworden.  [nieuw]
  - `andere fout` (andere fout) → Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 7: 's Nachts was het bij [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het warmer geworden?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “'s Nachts was het bij [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het warmer geworden?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C20 (3) · regel: G7-M01-temperatuur
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): teken-vergeten (6), tiental-ernaast (3)
- Verschillende Claude-fout-hints: 5 (meest: “Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul.”)
- Voorbeelden:
  - `G7-MEET-04-claude-bank-011` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 's Nachts was het bij de school −10 graden. Overdag werd het 3 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 13  (controle: ok)
    - **Fout-hints (Claude):** 7 → Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul. · 3 → 3 is de temperatuur overdag. De vraag is hoeveel het gestegen is, vanaf −10. · 14 → Tel de stappen naar nul en de stappen vanaf nul apart, en tel ze dan op.
    - **Uitleg (Claude):** Ga via nul. Van −10 naar 0 is 10 graden. Van 0 naar 3 is 3 graden. Samen 10 + 3 = 13 graden.
  - `G7-MEET-04-claude-bank-012` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 's Nachts was het bij de gymzaal −3 graden. Overdag werd het 8 graden. Hoeveel graden is het warmer geworden?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 5 → Onder nul telt ook mee. Van onder nul naar boven nul is verder dan je denkt. Ga via nul. · 8 → 8 is de temperatuur overdag. De vraag is hoeveel het gestegen is, vanaf −3. · 12 → Tel de stappen naar nul en de stappen vanaf nul apart, en tel ze dan op.
    - **Uitleg (Claude):** Ga via nul. Van −3 naar 0 is 3 graden. Van 0 naar 8 is 8 graden. Samen 3 + 8 = 11 graden.

- **Hint 1 (te schrijven):** Een min (−) voor een getal betekent: zoveel graden onder nul. Hoeveel stappen zijn het van de koude temperatuur naar de warme?
- **Hint 2 (te schrijven):** Tel de graden van de temperatuur onder nul tot nul. Tel daarna de graden van nul tot de nieuwe temperatuur. Tel die twee aantallen bij elkaar op.
- **Ouderzin:** Je kind rekent uit hoeveel graden het warmer is geworden, van onder nul naar boven nul.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de nieuwe temperatuur` (fout = getal2) → Dat is de nieuwe temperatuur. De vraag is hoeveel graden het warmer is geworden: tel ook de graden onder nul mee.  [nieuw]
  - `verschil van de getallen` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het verschil van de twee getallen. Maar je gaat eerst omhoog tot nul en dan verder: dat zijn twee stukken.  [nieuw]
  - `één graad ernaast` (fout = antwoord ± 1) → Je zit er één graad naast. Tel de stappen tot nul en de stappen vanaf nul apart, en tel ze dan op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel graden het warmer is geworden.  [nieuw]
  - `andere fout` (andere fout) → Tel de graden tot nul en de graden vanaf nul, en tel ze bij elkaar op.  [nieuw]
- Status: hints klaar
