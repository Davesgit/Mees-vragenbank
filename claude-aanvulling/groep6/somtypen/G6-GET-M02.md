# G6-GET-M02 — Springen tot 100.000 en cijferwaarde

Onze omschrijving: Telrij/sprongen ±100.000; positiewaarde tot tienduizendtallen · in onze bank: 8 items

Claude-vragen gemapt: **356** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # wordt #. Met hoeveel verandert het getal?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# wordt #. Met hoeveel verandert het getal?” (koppeling: claudeId)
- Items: **200** · Claude-doelen: C11 (200) · regel: G6-G05-positiewaarde
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): None (400)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G6-GET-M02-claude-bank-120` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** 12.345 wordt 12.355. Met hoeveel verandert het getal?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 100 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10.000 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G6-GET-M02-claude-bank-107` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** 18.235 wordt 19.235. Met hoeveel verandert het getal?
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10.000 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Vergelijk de twee getallen cijfer voor cijfer. Welk cijfer is anders?
- **Hint 2 (te schrijven):** Op welke plek staat het cijfer dat veranderd is? Het is één groter of één kleiner geworden. Eén op die plek is één tiental, honderdtal, duizendtal of tienduizendtal. Schrijf dat als getal.
- **Ouderzin:** Je kind ziet welk cijfer in een getal tot 100.000 verandert, en hoeveel dat waard is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één plek te ver naar links` (fout = antwoord × 10) → Dat is tien keer te veel. Het cijfer dat anders is, staat één plek verder naar rechts. Welke plek is dat?  [nieuw]
  - `één plek te ver naar rechts` (fout = antwoord : 10) → Dat is tien keer te weinig. Het cijfer dat anders is, staat één plek verder naar links. Welke plek is dat?  [nieuw]
  - `andere fout` (andere fout) → Zoek het cijfer dat anders is. Staat het bij de tientallen, honderdtallen, duizendtallen of tienduizendtallen? Eén op die plek is wat het getal verandert.  [nieuw]
- Status: hints klaar

## Somtype 2: Welk getal is # meer dan #?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Welk getal is # meer dan #?” (koppeling: claudeId)
- Items: **70** · Claude-doelen: C11 (70) · regel: G6-G06-sprongen
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (64), een-ernaast (33), eenheid-verkeerd-omgerekend (27), verkeerde-bewerking (16)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-GET-M02-claude-bank-282` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 100 meer dan 37.992?
    - **Antwoord:** 38.092  (controle: ok)
    - **Fout-hints (Claude):** 38.192 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-GET-M02-claude-bank-252` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 100 meer dan 34.921?
    - **Antwoord:** 35.021  (controle: ok)
    - **Fout-hints (Claude):** 35.121 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Kijk naar het getal vooraan in de vraag. Bij welke plek komt er één bij: de honderdtallen of de duizendtallen?
- **Hint 2 (te schrijven):** Op de plek waar er één bijkomt, staat een negen. Komt er één bij, dan wordt die negen een nul en gaat het cijfer ervoor één omhoog. Is dat cijfer ook een negen? Dan wordt dat ook een nul, en gaat het cijfer daarvoor één omhoog.
- **Ouderzin:** Je kind telt er honderd of duizend bij, over een tienduizendtal of duizendtal heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt eraf gehaald. Meer dan betekent dat er iets bijkomt: het getal wordt groter.  [nieuw]
  - `twee keer erbij` (fout = antwoord + getal1) → Dat is te veel. Er komt maar één bij op die plek. Heb je bij de negen het cijfer ervoor één omhoog gezet, en de negen een nul gemaakt?  [nieuw]
  - `het getal zelf` (fout = getal2) → Dat is het getal uit de vraag. Er moet nog iets bij.  [nieuw]
  - `één erbij gedaan` (fout = getal2 + 1) → Je hebt er maar één bijgedaan. Kijk naar het getal vooraan in de vraag: zoveel komt erbij.  [nieuw]
  - `op de verkeerde plek` (fout = getal2 + getal1 × 10) → Je hebt er wel iets bijgedaan, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek komt er één bij?  [nieuw]
  - `op de verkeerde plek` (fout = getal2 + getal1 : 10) → Je hebt er wel iets bijgedaan, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek komt er één bij?  [nieuw]
  - `op de verkeerde plek` (fout = getal2 + getal1 × 100) → Je hebt er wel iets bijgedaan, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek komt er één bij?  [nieuw]
  - `andere fout` (andere fout) → Kijk bij welke plek er één bijkomt. Staat daar een negen? Dan wordt die een nul en gaat het cijfer ervoor één omhoog.  [nieuw]
- Status: hints klaar

## Somtype 3: Welk getal is # minder dan #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Welk getal is # minder dan #?” (koppeling: claudeId)
- Items: **70** · Claude-doelen: C11 (70) · regel: G6-G06-sprongen
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (59), een-ernaast (38), eenheid-verkeerd-omgerekend (24), verkeerde-bewerking (19)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-GET-M02-claude-bank-330` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 100 minder dan 30.024?
    - **Antwoord:** 29.924  (controle: ok)
    - **Fout-hints (Claude):** 30.124 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G6-GET-M02-claude-bank-318` (Claude C11, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal is 100 minder dan 29.028?
    - **Antwoord:** 28.928  (controle: ok)
    - **Fout-hints (Claude):** 29.128 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 29.027 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Kijk naar het getal vooraan in de vraag. Bij welke plek gaat er één af: de honderdtallen of de duizendtallen?
- **Hint 2 (te schrijven):** Op de plek waar er één afgaat, staat een nul. Dan leen je van het cijfer ervoor: de nul wordt een negen en het cijfer ervoor gaat één omlaag. Is dat cijfer ook een nul? Dan wordt dat ook een negen, en leen je van het cijfer daarvoor.
- **Ouderzin:** Je kind haalt er honderd of duizend af, over een tienduizendtal of duizendtal heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij gedaan` (fout = getal1 + getal2) → Je hebt erbij gedaan. Minder dan betekent dat er iets afgaat: het getal wordt kleiner.  [nieuw]
  - `twee keer eraf` (fout = antwoord − getal1) → Dat is te weinig. Er gaat maar één af op die plek. Heb je bij de nul geleend: de nul een negen gemaakt en het cijfer ervoor één omlaag gezet?  [nieuw]
  - `het getal zelf` (fout = getal2) → Dat is het getal uit de vraag. Er moet nog iets af.  [nieuw]
  - `één eraf gehaald` (fout = getal2 − 1) → Je hebt er maar één afgehaald. Kijk naar het getal vooraan in de vraag: zoveel gaat eraf.  [nieuw]
  - `op de verkeerde plek` (fout = getal2 − getal1 × 10) → Je hebt er wel iets afgehaald, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek gaat er één af?  [nieuw]
  - `op de verkeerde plek` (fout = getal2 − getal1 : 10) → Je hebt er wel iets afgehaald, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek gaat er één af?  [nieuw]
  - `op de verkeerde plek` (fout = getal2 − getal1 × 100) → Je hebt er wel iets afgehaald, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek gaat er één af?  [nieuw]
  - `andere fout` (andere fout) → Kijk bij welke plek er één afgaat. Staat daar een nul? Dan leen je van het cijfer ervoor: de nul wordt een negen.  [nieuw]
- Status: hints klaar

## Somtype 4: De teller staat op # [ding]. Er komt er één bij. Op welk getal staat de teller nu?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “De teller staat op # [ding]. Er komt er één bij. Op welk getal staat de teller nu?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C11 (8) · regel: G6-G06-sprongen
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (8), plaatswaarde-verkeerd (8), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 3 (meest: “Er komt er maar één bij, geen tien. Tel één verder.”)
- Voorbeelden:
  - `G6-GET-M02-claude-bank-206` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Op het festival zijn 6699 bandjes uitgedeeld. Er komt er nog één bij. Hoeveel bandjes zijn het nu?
    - **Antwoord:** 6700  (controle: ok)
    - **Fout-hints (Claude):** 6709 → Er komt er maar één bij, geen tien. Tel één verder. · 6800 → Als 99 vol is, wordt het 00 en gaat alleen het honderdtal één omhoog. · 6698 → Er komt er één bij, dus je telt vooruit, niet terug.
    - **Uitleg (Claude):** Na 6699 komt 6700. De 99 wordt 00, en het honderdtal gaat één omhoog.
  - `G6-GET-M02-claude-bank-202` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Voor het concert zijn 1599 kaartjes verkocht. Er wordt er nog één verkocht. Hoeveel kaartjes zijn het nu?
    - **Antwoord:** 1600  (controle: ok)
    - **Fout-hints (Claude):** 1609 → Er komt er maar één bij, geen tien. Tel één verder. · 1700 → Als 99 vol is, wordt het 00 en gaat alleen het honderdtal één omhoog. · 1598 → Er komt er één bij, dus je telt vooruit, niet terug.
    - **Uitleg (Claude):** Na 1599 komt 1600. De 99 wordt 00, en het honderdtal gaat één omhoog.

- **Hint 1 (te schrijven):** Er komt er één bij. Welk getal komt direct na dit getal?
- **Hint 2 (te schrijven):** Het getal eindigt op negens. Komt er één bij, dan worden die negens nullen en gaat het cijfer ervoor één omhoog.
- **Ouderzin:** Je kind telt één verder, over een honderdtal of duizendtal heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien erbij` (fout = antwoord + 9) → Er komt er maar één bij, geen tien. Tel één verder.  [Claude, taalfix]
  - `honderd te veel` (fout = antwoord + 100) → Dat is te veel. Er komt er maar één bij: de negens worden nullen en het cijfer ervoor gaat één omhoog.  [nieuw]
  - `terug geteld` (fout = antwoord − 2) → Er komt er één bij, dus je telt verder, niet terug.  [Claude, taalfix]
  - `niet verder geteld` (fout = getal1) → Dat is het getal uit de vraag. Er komt er nog één bij.  [nieuw]
  - `andere fout` (andere fout) → Tel één verder dan het getal in de vraag. De negens aan het eind worden nullen en het cijfer ervoor gaat één omhoog.  [nieuw]
- Status: hints klaar

## Somtype 5: Op het bord staat # [ding]. Hoeveel is de # in dit getal waard?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Op het bord staat # [ding]. Hoeveel is de # in dit getal waard?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C11 (8) · regel: G6-G05-positiewaarde
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (15), plaatswaarde-verkeerd (8)
- Verschillende Claude-fout-hints: 7 (meest: “Eén nul te veel. Tel de plekken rechts van het cijfer: zoveel nullen krijg je.”)
- Voorbeelden:
  - `G6-GET-M02-claude-bank-212` (Claude C11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op het bord staat het getal 8785. Hoeveel is de 7 in dit getal waard?
    - **Antwoord:** 700  (controle: ok)
    - **Fout-hints (Claude):** 7 → Een cijfer is meer waard als het verder naar links staat. Op welke plek staat de 7? · 7000 → Eén nul te veel. Tel de plekken rechts van het cijfer: zoveel nullen krijg je. · 70 → Eén nul te weinig. Tel de plekken rechts van het cijfer: zoveel nullen krijg je.
    - **Uitleg (Claude):** In 8785 staat de 7 op de plek van de honderdtallen. Dus die is 700 waard.
  - `G6-GET-M02-claude-bank-213` (Claude C11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op het bord staat het getal 1579. Hoeveel is de 5 in dit getal waard?
    - **Antwoord:** 500  (controle: ok)
    - **Fout-hints (Claude):** 5 → Een cijfer is meer waard als het verder naar links staat. Op welke plek staat de 5? · 5000 → Eén nul te veel. Tel de plekken rechts van het cijfer: zoveel nullen krijg je. · 50 → Eén nul te weinig. Tel de plekken rechts van het cijfer: zoveel nullen krijg je.
    - **Uitleg (Claude):** In 1579 staat de 5 op de plek van de honderdtallen. Dus die is 500 waard.

- **Hint 1 (te schrijven):** Op welke plek staat het cijfer: bij de duizendtallen, de honderdtallen, de tientallen of de eenheden?
- **Hint 2 (te schrijven):** Tel hoeveel cijfers er rechts van het cijfer uit de vraag staan. Zoveel nullen zet je achter het cijfer.
- **Ouderzin:** Je kind zegt hoeveel een cijfer in een getal tot 10.000 waard is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het cijfer` (fout = getal2) → Dat is alleen het cijfer. Een cijfer is meer waard als het verder naar links staat. Op welke plek staat het?  [Claude, taalfix]
  - `één nul te veel` (fout = antwoord × 10) → Eén nul te veel. Tel hoeveel cijfers er rechts van het cijfer staan: zoveel nullen krijg je.  [Claude, taalfix]
  - `één nul te weinig` (fout = antwoord : 10) → Eén nul te weinig. Tel hoeveel cijfers er rechts van het cijfer staan: zoveel nullen krijg je.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zoek op welke plek het cijfer staat. Tel de cijfers rechts ervan: zoveel nullen komen er achter het cijfer.  [nieuw]
- Status: hints klaar
