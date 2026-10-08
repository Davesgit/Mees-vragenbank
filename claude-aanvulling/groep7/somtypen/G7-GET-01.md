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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
