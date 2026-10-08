# G7-GET-01 — Grote getallen lezen

Onze omschrijving: Hele getallen ±1 miljoen · in onze bank: 8 items

Claude-vragen gemapt: **668** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # wordt #. Met hoeveel verandert het getal?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# wordt #. Met hoeveel verandert het getal?” (koppeling: claudeId)
- Items: **396** · Claude-doelen: C22 (396) · regel: G7-G03-positiewaarde
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): None (792)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-348` (Claude C22, bank, niveau 2 → toepassen)
    - **Opgave:** 314.586 wordt 313.586. Met hoeveel verandert het getal?
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 100 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10.000 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G7-GET-01-claude-bank-254` (Claude C22, bank, niveau 3 → toepassen)
    - **Opgave:** 283.971 wordt 284.971. Met hoeveel verandert het getal?
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 100 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10.000 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Vergelijk de twee getallen cijfer voor cijfer. Welk cijfer is anders?
- **Hint 2 (te schrijven):** Zoek de plek van het cijfer dat anders is: honderdtallen, duizendtallen, tienduizendtallen of honderdduizendtallen. Dat cijfer is één groter of één kleiner geworden. Het getal verandert dus met één van die plek: honderd, duizend, tienduizend of honderdduizend.
- **Ouderzin:** Je kind ziet welk cijfer in een getal tot een miljoen verandert, en hoeveel dat waard is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één plek te ver naar links` (fout = antwoord × 10) → Dat is tien keer te veel. Het cijfer dat anders is, staat één plek verder naar rechts. Welke plek is dat?  [nieuw]
  - `één plek te ver naar rechts` (fout = antwoord : 10) → Dat is tien keer te weinig. Het cijfer dat anders is, staat één plek verder naar links. Welke plek is dat?  [nieuw]
  - `verder naar links` (fout = antwoord + 1 of meer) → Dat is te veel. Het cijfer dat anders is, staat verder naar rechts. Op welke plek staat het?  [nieuw]
  - `verder naar rechts` (fout = antwoord - 1 of meer) → Dat is te weinig. Het cijfer dat anders is, staat verder naar links. Op welke plek staat het?  [nieuw]
  - `andere fout` (andere fout) → Zoek het cijfer dat anders is. Op welke plek staat het? Eén van die plek is wat het getal verandert.  [nieuw]
- Status: hints klaar

## Somtype 2: Welk getal is # minder dan #?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Welk getal is # minder dan #?” (koppeling: claudeId)
- Items: **103** · Claude-doelen: C22 (103) · regel: G7-G04-sprongen
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (88), een-ernaast (53), verkeerde-bewerking (38), eenheid-verkeerd-omgerekend (27)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-682` (Claude C22, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 1000 minder dan 200.312?
    - **Antwoord:** 199.312  (controle: ok)
    - **Fout-hints (Claude):** 201.312 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-GET-01-claude-bank-616` (Claude C22, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 1000 minder dan 270.517?
    - **Antwoord:** 269.517  (controle: ok)
    - **Fout-hints (Claude):** 271.517 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Kijk naar het getal dat eraf gaat. Bij welke plek gaat er één af?
- **Hint 2 (te schrijven):** Zoek in het grote getal de plek waar er één afgaat. Staat daar een nul? Dan leen je van het cijfer ervoor: de nul wordt een negen en het cijfer ervoor gaat één omlaag. Is dat cijfer ook een nul? Dan wordt dat ook een negen, en leen je verder naar links.
- **Ouderzin:** Je kind haalt een rond getal, zoals duizend of tienduizend, af van een getal tot een miljoen, ook als daar een nul staat.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij gedaan` (fout = getal1 + getal2) → Komt er iets bij of gaat er iets af? Minder dan betekent dat het getal kleiner wordt.  [nieuw]
  - `twee keer eraf` (fout = antwoord - getal1) → Dat is te weinig. Er gaat maar één keer iets af. Bij welke plek?  [nieuw]
  - `één eraf gehaald` (fout = getal2 - 1) → Dat is maar één minder. Hoeveel gaat er volgens de vraag af?  [nieuw]
  - `het getal zelf` (fout = getal2) → Dat is het grote getal uit de vraag. Er moet nog iets af. Hoeveel?  [nieuw]
  - `andere fout` (andere fout) → Zoek de plek uit de vraag in het grote getal en haal daar één af.  [nieuw]
- Status: hints klaar

## Somtype 3: Welk getal is # meer dan #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Welk getal is # meer dan #?” (koppeling: claudeId)
- Items: **101** · Claude-doelen: C22 (101) · regel: G7-G04-sprongen
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (89), een-ernaast (48), eenheid-verkeerd-omgerekend (36), verkeerde-bewerking (29)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-556` (Claude C22, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 10.000 meer dan 191.444?
    - **Antwoord:** 201.444  (controle: ok)
    - **Fout-hints (Claude):** 191.445 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 211.444 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G7-GET-01-claude-bank-513` (Claude C22, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 1000 meer dan 379.889?
    - **Antwoord:** 380.889  (controle: ok)
    - **Fout-hints (Claude):** 381.889 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Kijk naar het getal dat erbij komt. Bij welke plek komt er één bij?
- **Hint 2 (te schrijven):** Zoek in het grote getal de plek waar er één bijkomt. Staat daar een negen? Dan wordt de negen een nul en gaat het cijfer ervoor één omhoog. Is dat cijfer ook een negen? Dan wordt dat ook een nul, en ga je verder naar links.
- **Ouderzin:** Je kind telt een rond getal, zoals duizend of tienduizend, op bij een getal tot een miljoen, ook als daar een negen staat.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Komt er iets bij of gaat er iets af? Meer dan betekent dat het getal groter wordt.  [nieuw]
  - `twee keer erbij` (fout = antwoord + getal1) → Dat is te veel. Er komt maar één keer iets bij. Bij welke plek?  [nieuw]
  - `één erbij gedaan` (fout = getal2 + 1) → Dat is maar één meer. Hoeveel komt er volgens de vraag bij?  [nieuw]
  - `het getal zelf` (fout = getal2) → Dat is het grote getal uit de vraag. Er moet nog iets bij. Hoeveel?  [nieuw]
  - `andere fout` (andere fout) → Zoek de plek uit de vraag in het grote getal en doe daar één bij.  [nieuw]
- Status: hints klaar

## Somtype 4: Rond # af op tienduizendtallen.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Rond # af op tienduizendtallen.” (koppeling: claudeId)
- Items: **53** · Claude-doelen: C11 (53) · regel: G7-G02-afronden
- Getallenruimte: 0–1.000.000 · type: kale
- Uit de G6-park: 53 items
- Denkfouten (Claude): afronden-verkeerde-kant (97), schatting-verkeerd (9)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-442` (Claude C11, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 215.991 af op tienduizendtallen.
    - **Antwoord:** 220.000  (controle: ok)
    - **Fout-hints (Claude):** 240.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 200.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G7-GET-01-claude-bank-422` (Claude C11, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 117.920 af op tienduizendtallen.
    - **Antwoord:** 120.000  (controle: ok)
    - **Fout-hints (Claude):** 140.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 100.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Welke twee tienduizendtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de duizendtallen. Is het vijf of meer, dan rond je af naar het tienduizendtal erboven. Anders rond je af naar het tienduizendtal eronder. De laatste vier cijfers worden nullen.
- **Ouderzin:** Je kind rondt een getal tot een miljoen af op tienduizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond je het nog af op tienduizendtallen? Kijk naar het cijfer van de duizendtallen.  [nieuw]
  - `verkeerde kant` (fout = het andere tienduizendtal naast getal1) → Dat is het tienduizendtal aan de andere kant van het getal. Is het cijfer van de duizendtallen vijf of meer, of minder dan vijf?  [nieuw]
  - `afgerond op duizendtallen` (fout = getal1 afgerond op duizendtallen) → Dat is afgerond op duizendtallen. Op welke plek rond je hier af?  [nieuw]
  - `één stap te ver (omhoog)` (fout = antwoord + 10000) → Dat ligt te ver weg. Welke twee tienduizendtallen liggen vlak naast het getal?  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord - 10000) → Dat ligt te ver weg. Welke twee tienduizendtallen liggen vlak naast het getal?  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 20000 of meer) → Dat ligt te ver weg. Welke twee tienduizendtallen liggen vlak naast het getal?  [nieuw]
  - `te ver (omlaag)` (fout = antwoord - 20000 of meer) → Dat ligt te ver weg. Welke twee tienduizendtallen liggen vlak naast het getal?  [nieuw]
  - `andere fout` (andere fout) → Kies het tienduizendtal vlak onder of vlak boven het getal. Het cijfer van de duizendtallen beslist.  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] zijn # [ding] geteld, in [plek] #. Typ het grootste getal.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] zijn # [ding] geteld, in [plek] #. Typ het grootste getal.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C22 (8) · regel: G7-G05-lezen
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (8), cijfers-verwisseld (8)
- Verschillende Claude-fout-hints: 2 (meest: “Vergelijk van links naar rechts, cijfer voor cijfer. Bij het eerste verschil weet je welk getal groter is.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-405` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het nest zijn 614.806 botten geteld, in het museum 613.878. Typ het grootste getal.
    - **Antwoord:** 614.806  (controle: ok)
    - **Fout-hints (Claude):** 613.878 → Vergelijk van links naar rechts, cijfer voor cijfer. Bij het eerste verschil weet je welk getal groter is. · 608.416 → Typ het getal precies over, zonder de punten.
    - **Uitleg (Claude):** Vergelijk van links naar rechts: eerst de honderdduizendtallen, dan de tienduizendtallen, enzovoort. 614.806 is groter dan 613.878.
  - `G7-GET-01-claude-bank-406` (Claude C22, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het bos zijn 884.401 wortels geteld, in de schuur 877.364. Typ het grootste getal.
    - **Antwoord:** 884.401  (controle: ok)
    - **Fout-hints (Claude):** 877.364 → Vergelijk van links naar rechts, cijfer voor cijfer. Bij het eerste verschil weet je welk getal groter is. · 104.488 → Typ het getal precies over, zonder de punten.
    - **Uitleg (Claude):** Vergelijk van links naar rechts: eerst de honderdduizendtallen, dan de tienduizendtallen, enzovoort. 884.401 is groter dan 877.364.

- **Hint 1 (te schrijven):** Vergelijk de getallen van links naar rechts. Begin bij de honderdduizendtallen.
- **Hint 2 (te schrijven):** Zijn de honderdduizendtallen gelijk? Kijk dan naar de tienduizendtallen, dan naar de duizendtallen, enzovoort. Het eerste cijfer dat verschilt, beslist. Typ het grootste getal precies over.
- **Ouderzin:** Je kind zegt welk van twee getallen tot een miljoen het grootst is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het kleinste getal` (fout = een getal uit de vraag) → Dat is het kleinste van de twee getallen. Welk cijfer verschilt als eerste, als je van links naar rechts kijkt?  [nieuw]
  - `cijfers verwisseld` (Claudes sleutel: cijfers-verwisseld) → Staan de cijfers in de goede volgorde? Typ het getal precies zoals het in de vraag staat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Typ een van de twee getallen uit de vraag: het grootste. Vergelijk ze van links naar rechts.  [nieuw]
- Status: hints klaar

## Somtype 6: Op de teller van [plek] staat # [ding]. Hoeveel is de # in dit getal waard?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Op de teller van [plek] staat # [ding]. Hoeveel is de # in dit getal waard?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C22 (4) · regel: G7-G03-positiewaarde
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (12)
- Verschillende Claude-fout-hints: 6 (meest: “Tel de plekken rechts van het cijfer: zoveel nullen krijgt de waarde. Je zit er één naast.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-409` (Claude C22, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de teller van het museum staat 642.311 tanden. Hoeveel is de 6 in dit getal waard?
    - **Antwoord:** 600.000  (controle: ok)
    - **Fout-hints (Claude):** 60.000 → Tel de plekken rechts van het cijfer: zoveel nullen krijgt de waarde. Je zit er één naast. · 6.000.000 → Tel de plekken rechts van het cijfer: zoveel nullen krijgt de waarde. Je hebt er één te veel. · 6 → Een cijfer links in een getal is veel meer waard dan zichzelf. Kijk op welke plek de 6 staat.
    - **Uitleg (Claude):** In 642.311 staat de 6 op de plek van de honderdduizendtallen. Dus die is 600.000 waard.
  - `G7-GET-01-claude-bank-412` (Claude C22, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de teller van de klas staat 252.891 pakken. Hoeveel is de 8 in dit getal waard?
    - **Antwoord:** 800  (controle: ok)
    - **Fout-hints (Claude):** 80 → Tel de plekken rechts van het cijfer: zoveel nullen krijgt de waarde. Je zit er één naast. · 8000 → Tel de plekken rechts van het cijfer: zoveel nullen krijgt de waarde. Je hebt er één te veel. · 8 → Een cijfer links in een getal is veel meer waard dan zichzelf. Kijk op welke plek de 8 staat.
    - **Uitleg (Claude):** In 252.891 staat de 8 op de plek van de honderdtallen. Dus die is 800 waard.

- **Hint 1 (te schrijven):** Op welke plek staat het cijfer waar de vraag over gaat? Tel de plekken van rechts naar links.
- **Hint 2 (te schrijven):** De plekken van rechts naar links zijn: eenheden, tientallen, honderdtallen, duizendtallen, tienduizendtallen, honderdduizendtallen. Staat het cijfer bij de duizendtallen, dan is het zoveel duizend waard.
- **Ouderzin:** Je kind zegt hoeveel een cijfer in een getal tot een miljoen waard is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het cijfer` (fout = getal2) → Dat is alleen het cijfer. Een cijfer is meer waard als het verder naar links staat. Op welke plek staat het?  [nieuw]
  - `één nul te veel` (fout = antwoord × 10) → Eén nul te veel. Hoeveel cijfers staan er rechts van het cijfer?  [nieuw]
  - `één nul te weinig` (fout = antwoord : 10) → Eén nul te weinig. Hoeveel cijfers staan er rechts van het cijfer?  [nieuw]
  - `andere fout` (andere fout) → Zoek het cijfer waar de vraag over gaat. Tel de cijfers rechts ervan: zoveel nullen komen erachter.  [nieuw]
- Status: hints klaar

## Somtype 7: Welk cijfer staat op de plaats van de tienduizendtallen in #?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Welk cijfer staat op de plaats van de tienduizendtallen in #?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C22 (3) · regel: G7-G03-positiewaarde
- Getallenruimte: 0–1.000.000 · type: kale
- Denkfouten (Claude): getal-overgenomen (3), een-ernaast (2), grafiek-verkeerd-afgelezen (1)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G7-GET-01-claude-bank-469` (Claude C22, bank, niveau 3 → toepassen)
    - **Opgave:** Welk cijfer staat op de plaats van de tienduizendtallen in 729.681?
    - **Antwoord:** 2  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G7-GET-01-claude-bank-468` (Claude C22, bank, niveau 3 → toepassen)
    - **Opgave:** Welk cijfer staat op de plaats van de tienduizendtallen in 736.125?
    - **Antwoord:** 3  (controle: n.v.t.)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Tel de plekken van rechts naar links: eenheden, tientallen, honderdtallen, duizendtallen, tienduizendtallen.
- **Hint 2 (te schrijven):** Wijs vanaf rechts elk cijfer aan en zeg de naam van zijn plek. Het cijfer dat je aanwijst bij tienduizendtallen, is het antwoord.
- **Ouderzin:** Je kind zoekt het cijfer op een plek in een getal tot een miljoen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal1) → Dat is het hele getal. De vraag zoekt één cijfer: het cijfer bij de tienduizendtallen. Welk cijfer is dat?  [nieuw]
  - `cijfer ernaast` (Claudes sleutel: een-ernaast) → Staat dat cijfer bij de tienduizendtallen? Tel de plekken van rechts: eenheden, tientallen, honderdtallen, duizendtallen, tienduizendtallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de plekken van rechts naar links tot je bij de tienduizendtallen bent.  [nieuw]
- Status: hints klaar
