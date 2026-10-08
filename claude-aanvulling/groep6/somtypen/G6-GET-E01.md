# G6-GET-E01 — Grote getallen ordenen en afronden

Onze omschrijving: Vergelijken/ordenen/afronden ±100.000; decimale structuur uitleggen · in onze bank: 8 items

Claude-vragen gemapt: **128** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Rond # af op duizendtallen.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Rond # af op duizendtallen.” (koppeling: claudeId)
- Items: **60** · Claude-doelen: C10 (31), C11 (29) · regel: G6-G02-afronden
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Uit de G5-park: 31 items
- Denkfouten (Claude): afronden-verkeerde-kant (99), schatting-verkeerd (20)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-027` (Claude C10, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 2125 af op duizendtallen.
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 3000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 2100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G6-GET-E01-claude-bank-063` (Claude C11, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 10.500 af op duizendtallen.
    - **Antwoord:** 11.000  (controle: ok)
    - **Fout-hints (Claude):** 10.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 10.500 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Welke twee duizendtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de honderdtallen. Is het 5 of meer, dan rond je af naar het duizendtal erboven. Anders naar het duizendtal eronder.
- **Ouderzin:** Je kind rondt een getal tot 100.000 af op duizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op duizendtallen. Kijk naar het cijfer van de honderdtallen.  [nieuw]
  - `verkeerde kant` (fout = het andere duizendtal naast getal1) → Dat is het duizendtal aan de andere kant van het getal. Kijk naar het cijfer van de honderdtallen. Is het 5 of meer, dan ga je naar het duizendtal vlak erboven. Anders naar het duizendtal vlak eronder.  [nieuw]
  - `afgerond op honderdtallen` (fout = getal1 afgerond op honderdtallen) → Je hebt afgerond op honderdtallen. Hier rond je af op duizendtallen. Kijk naar het cijfer van de honderdtallen.  [nieuw]
  - `één stap te ver (omhoog)` (fout = antwoord + 1000) → Je gaat de goede kant op, maar één duizendtal te ver. Kies het duizendtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 1000) → Je gaat de goede kant op, maar één duizendtal te ver. Kies het duizendtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 2000 of meer) → Dat ligt te ver weg. Kies een duizendtal vlak naast het getal: het duizendtal eronder of het duizendtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 2000 of meer) → Dat ligt te ver weg. Kies een duizendtal vlak naast het getal: het duizendtal eronder of het duizendtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op duizendtallen: de laatste drie cijfers van het antwoord zijn dus nullen. Zoek de twee duizendtallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de honderdtallen. Is het 5 of meer, dan kies je het duizendtal erboven. Anders kies je het duizendtal eronder.  [nieuw]
- Status: hints klaar

## Somtype 2: Rond # af op honderdtallen.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Rond # af op honderdtallen.” (koppeling: claudeId)
- Items: **33** · Claude-doelen: C10 (33) · regel: G6-G02-afronden
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Uit de G5-park: 33 items
- Denkfouten (Claude): afronden-verkeerde-kant (57), schatting-verkeerd (9)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-101` (Claude C10, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 1017 af op honderdtallen.
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 1100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 1020 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G6-GET-E01-claude-bank-102` (Claude C10, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 54.931 af op honderdtallen.
    - **Antwoord:** 54.900  (controle: ok)
    - **Fout-hints (Claude):** 1400 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 1700 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Welke twee honderdtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de tientallen. Is het 5 of meer, dan rond je af naar het honderdtal erboven. Anders naar het honderdtal eronder.
- **Ouderzin:** Je kind rondt een getal tot 100.000 af op honderdtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op honderdtallen. Kijk naar het cijfer van de tientallen.  [nieuw]
  - `verkeerde kant` (fout = het andere honderdtal naast getal1) → Dat is het honderdtal aan de andere kant van het getal. Kijk naar het cijfer van de tientallen. Is het 5 of meer, dan ga je naar het honderdtal vlak erboven. Anders naar het honderdtal vlak eronder.  [Claude, taalfix]
  - `afgerond op tientallen` (fout = getal1 afgerond op tientallen) → Je hebt afgerond op tientallen. Hier rond je af op honderdtallen. Kijk naar het cijfer van de tientallen.  [nieuw]
  - `één stap te ver (omhoog)` (fout = antwoord + 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op honderdtallen: de laatste twee cijfers van het antwoord zijn dus nullen. Zoek de twee honderdtallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de tientallen. Is het 5 of meer, dan kies je het honderdtal erboven. Anders kies je het honderdtal eronder.  [nieuw]
- Status: hints klaar

## Somtype 3: [stip op getallenlijn zetten] Zet # op de getallenlijn van # tot #.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[stip op getallenlijn zetten] Zet # op de getallenlijn van # tot #.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C11 (12) · regel: G6-G03-getallenlijn
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G6-GET-E01-claude-bank-121` (Claude C11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 17.000 op de getallenlijn van 0 tot 100.000.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 17.000  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Elk streepje is 10.000. 17.000 ligt tussen 10.000 en 20.000.
  - `G6-GET-E01-claude-bank-128` (Claude C11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 77.000 op de getallenlijn van 0 tot 100.000.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 77.000  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Elk streepje is 10.000. 77.000 ligt tussen 70.000 en 80.000.

- **Hint 1 (te schrijven):** Tussen welke twee tienduizendtallen ligt het getal? Zoek die eerst op de lijn.
- **Hint 2 (te schrijven):** Begin bij het tienduizendtal onder het getal. Tel vanaf daar verder in stappen van duizend.
- **Ouderzin:** Je kind zet een getal tot 100.000 op een getallenlijn met tienduizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tienduizendtal te ver` (fout = antwoord + 10000) → Dat is één tienduizendtal te ver. Het cijfer vooraan zegt bij welk tienduizendtal je begint.  [nieuw]
  - `tienduizendtal te weinig` (fout = antwoord − 10000) → Dat is één tienduizendtal te weinig. Het cijfer vooraan zegt bij welk tienduizendtal je begint.  [nieuw]
  - `stap te ver` (fout = antwoord + 1000) → Bijna! Dat is één stap van duizend te ver. Tel de stappen na het tienduizendtal nog eens.  [nieuw]
  - `stap te weinig` (fout = antwoord − 1000) → Bijna! Dat is één stap van duizend te weinig. Tel de stappen na het tienduizendtal nog eens.  [nieuw]
  - `andere fout` (andere fout) → Zoek eerst het tienduizendtal van het getal: het cijfer vooraan. Tel dan verder in stappen van duizend tot je bij het getal bent.  [nieuw]
- Status: hints klaar

## Somtype 4: Rond # af op tienduizendtallen.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Rond # af op tienduizendtallen.” (koppeling: claudeId)
- Items: **7** · Claude-doelen: C11 (7) · regel: G6-G02-afronden
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): afronden-verkeerde-kant (12), schatting-verkeerd (2)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-114` (Claude C11, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 36.260 af op tienduizendtallen.
    - **Antwoord:** 40.000  (controle: ok)
    - **Fout-hints (Claude):** 50.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 60.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G6-GET-E01-claude-bank-115` (Claude C11, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 52.671 af op tienduizendtallen.
    - **Antwoord:** 50.000  (controle: ok)
    - **Fout-hints (Claude):** 40.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 30.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Welke twee tienduizendtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de duizendtallen. Is het 5 of meer, dan rond je af naar het tienduizendtal erboven. Anders naar het tienduizendtal eronder.
- **Ouderzin:** Je kind rondt een getal tot 100.000 af op tienduizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op tienduizendtallen. Kijk naar het cijfer van de duizendtallen.  [nieuw]
  - `verkeerde kant` (fout = het andere tienduizendtal naast getal1) → Dat is het tienduizendtal aan de andere kant van het getal. Kijk naar het cijfer van de duizendtallen. Is het 5 of meer, dan ga je naar het tienduizendtal vlak erboven. Anders naar het tienduizendtal vlak eronder.  [nieuw]
  - `afgerond op duizendtallen` (fout = getal1 afgerond op duizendtallen) → Je hebt afgerond op duizendtallen. Hier rond je af op tienduizendtallen. Kijk naar het cijfer van de duizendtallen.  [nieuw]
  - `één stap te ver (omhoog)` (fout = antwoord + 10000) → Je gaat de goede kant op, maar één tienduizendtal te ver. Kies het tienduizendtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 10000) → Je gaat de goede kant op, maar één tienduizendtal te ver. Kies het tienduizendtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 20000 of meer) → Dat ligt te ver weg. Kies een tienduizendtal vlak naast het getal: het tienduizendtal eronder of het tienduizendtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 20000 of meer) → Dat ligt te ver weg. Kies een tienduizendtal vlak naast het getal: het tienduizendtal eronder of het tienduizendtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op tienduizendtallen: de laatste vier cijfers van het antwoord zijn dus nullen. Zoek de twee tienduizendtallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de duizendtallen. Is het 5 of meer, dan kies je het tienduizendtal erboven. Anders kies je het tienduizendtal eronder.  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] zijn precies # [ding]. Rond dit aantal af op honderdtallen.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] zijn precies # [ding]. Rond dit aantal af op honderdtallen.” (koppeling: claudeId)
- Items: **5** · Claude-doelen: C10 (5) · regel: G6-G02-afronden
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 5 items
- Denkfouten (Claude): afronden-verkeerde-kant (5), plaatswaarde-verkeerd (5)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar wat er na de honderdtallen komt. Is dat minder dan de helft van 100, dan rond je naar beneden af. Anders naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-009` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Bij de wedstrijd waren precies 2837 toeschouwers. Rond dit aantal af op honderdtallen.
    - **Antwoord:** 2800  (controle: ok)
    - **Fout-hints (Claude):** 2900 → Kijk naar wat er na de honderdtallen komt. Is dat minder dan de helft van 100, dan rond je naar beneden af. Anders naar boven. · 3000 → Je hebt op de verkeerde plek afgerond. Het moet op honderdtallen.
    - **Uitleg (Claude):** 2837 ligt tussen 2800 en 2900. Kijk naar de rest: 37. Dat is minder dan de helft van 100, dus je rondt naar beneden af: 2800.
  - `G6-GET-E01-claude-bank-010` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Het museum had deze maand precies 6453 bezoekers. Rond dit aantal af op honderdtallen.
    - **Antwoord:** 6500  (controle: ok)
    - **Fout-hints (Claude):** 6400 → Kijk naar wat er na de honderdtallen komt. Is dat minder dan de helft van 100, dan rond je naar beneden af. Anders naar boven. · 6000 → Je hebt op de verkeerde plek afgerond. Het moet op honderdtallen.
    - **Uitleg (Claude):** 6453 ligt tussen 6400 en 6500. Kijk naar de rest: 53. Dat is meer dan de helft van 100, dus je rondt naar boven af: 6500.

- **Hint 1 (te schrijven):** Welke twee honderdtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de tientallen. Is het 5 of meer, dan rond je af naar het honderdtal erboven. Anders naar het honderdtal eronder.
- **Ouderzin:** Je kind rondt een aantal tot 10.000 af op honderdtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op honderdtallen. Kijk naar het cijfer van de tientallen.  [nieuw]
  - `verkeerde kant` (fout = het andere honderdtal naast getal1) → Dat is het honderdtal aan de andere kant van het getal. Kijk naar het cijfer van de tientallen. Is het 5 of meer, dan ga je naar het honderdtal vlak erboven. Anders naar het honderdtal vlak eronder.  [Claude, taalfix]
  - `afgerond op tientallen` (fout = getal1 afgerond op tientallen) → Je hebt afgerond op tientallen. Hier rond je af op honderdtallen. Kijk naar het cijfer van de tientallen.  [nieuw]
  - `afgerond op duizendtallen` (fout = getal1 afgerond op duizendtallen) → Je hebt afgerond op duizendtallen. Hier rond je af op honderdtallen. Kijk naar het cijfer van de tientallen.  [Claude, taalfix]
  - `één stap te ver (omhoog)` (fout = antwoord + 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op honderdtallen: de laatste twee cijfers van het antwoord zijn dus nullen. Zoek de twee honderdtallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de tientallen. Is het 5 of meer, dan kies je het honderdtal erboven. Anders kies je het honderdtal eronder.  [nieuw]
- Status: hints klaar

## Somtype 6: In [plek] liggen # [ding]. In [plek] liggen er #. Typ het grootste getal.

- Sleutel: nrOrigineel **6** · somtypeOrigineel “In [plek] liggen # [ding]. In [plek] liggen er #. Typ het grootste getal.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C11 (4) · regel: G6-G04-vergelijken
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (4), cijfers-verwisseld (4)
- Verschillende Claude-fout-hints: 2 (meest: “Vergelijk van links naar rechts: eerst de duizendtallen, dan de honderdtallen, dan de tientallen.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-002` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de gymzaal liggen 8596 stenen. In het huis liggen er 8299. Typ het grootste getal.
    - **Antwoord:** 8596  (controle: ok)
    - **Fout-hints (Claude):** 8299 → Vergelijk van links naar rechts: eerst de duizendtallen, dan de honderdtallen, dan de tientallen. · 6958 → Je hebt de goede cijfers, maar in de verkeerde volgorde. Typ het getal precies zoals het er staat.
    - **Uitleg (Claude):** Kijk eerst naar de duizendtallen: allebei 8. Kijk dan naar de honderdtallen: 5 tegenover 2. 8596 is groter dan 8299.
  - `G6-GET-E01-claude-bank-003` (Claude C11, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de schuur liggen 5246 noten. In het bos liggen er 5376. Typ het grootste getal.
    - **Antwoord:** 5376  (controle: ok)
    - **Fout-hints (Claude):** 5246 → Vergelijk van links naar rechts: eerst de duizendtallen, dan de honderdtallen, dan de tientallen. · 6735 → Je hebt de goede cijfers, maar in de verkeerde volgorde. Typ het getal precies zoals het er staat.
    - **Uitleg (Claude):** Kijk eerst naar de duizendtallen: allebei 5. Kijk dan naar de honderdtallen: 3 tegenover 2. 5376 is groter dan 5246.

- **Hint 1 (te schrijven):** Vergelijk de getallen van links naar rechts. Begin bij de duizendtallen.
- **Hint 2 (te schrijven):** Zijn de duizendtallen gelijk? Kijk dan naar de honderdtallen. Zijn die ook gelijk? Kijk dan naar de tientallen. Het eerste cijfer dat verschilt, beslist.
- **Ouderzin:** Je kind zegt welk van twee getallen tot 10.000 het grootst is.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het kleinste getal` (fout = een getal uit de vraag) → Dat is het kleinste getal. Je zoekt het grootste. Vergelijk van links naar rechts: eerst de duizendtallen, dan de honderdtallen.  [Claude, taalfix]
  - `cijfers verwisseld` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in de verkeerde volgorde. Typ het getal precies zoals het er staat.  [Claude, ok]
  - `andere fout` (andere fout) → Typ een van de twee getallen uit de vraag: het grootste. Vergelijk ze van links naar rechts, eerst de duizendtallen.  [nieuw]
- Status: hints klaar

## Somtype 7: In [plek] zijn precies # [ding]. Rond dit aantal af op duizendtallen.

- Sleutel: nrOrigineel **7** · somtypeOrigineel “In [plek] zijn precies # [ding]. Rond dit aantal af op duizendtallen.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C10 (4) · regel: G6-G02-afronden
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 4 items
- Denkfouten (Claude): afronden-verkeerde-kant (4), plaatswaarde-verkeerd (3)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar wat er na de duizendtallen komt. Is dat minder dan de helft van 1000, dan rond je naar beneden af. Anders naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-007` (Claude C10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Sem heeft deze week precies 5347 stappen gezet. Rond dit aantal af op duizendtallen.
    - **Antwoord:** 5000  (controle: ok)
    - **Fout-hints (Claude):** 6000 → Kijk naar wat er na de duizendtallen komt. Is dat minder dan de helft van 1000, dan rond je naar beneden af. Anders naar boven. · 5300 → Je hebt op de verkeerde plek afgerond. Het moet op duizendtallen.
    - **Uitleg (Claude):** 5347 ligt tussen 5000 en 6000. Kijk naar de rest: 347. Dat is minder dan de helft van 1000, dus je rondt naar beneden af: 5000.
  - `G6-GET-E01-claude-bank-006` (Claude C10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Voor het concert zijn precies 2500 kaartjes verkocht. Rond dit aantal af op duizendtallen.
    - **Antwoord:** 3000  (controle: ok)
    - **Fout-hints (Claude):** 3000 → Kijk naar wat er na de duizendtallen komt. Is dat minder dan de helft van 1000, dan rond je naar beneden af. Anders naar boven. · 2300 → Je hebt op de verkeerde plek afgerond. Het moet op duizendtallen.
    - **Uitleg (Claude):** 2500 ligt tussen 2000 en 3000. Kijk naar de rest: 500. Dat is precies de helft van 1000, dus je rondt naar boven af: 3000.

- **Hint 1 (te schrijven):** Welke twee duizendtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de honderdtallen. Is het 5 of meer, dan rond je af naar het duizendtal erboven. Anders naar het duizendtal eronder.
- **Ouderzin:** Je kind rondt een aantal tot 10.000 af op duizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op duizendtallen. Kijk naar het cijfer van de honderdtallen.  [nieuw]
  - `verkeerde kant` (fout = het andere duizendtal naast getal1) → Dat is het duizendtal aan de andere kant van het getal. Kijk naar het cijfer van de honderdtallen. Is het 5 of meer, dan ga je naar het duizendtal vlak erboven. Anders naar het duizendtal vlak eronder.  [Claude, taalfix]
  - `afgerond op honderdtallen` (fout = getal1 afgerond op honderdtallen) → Je hebt afgerond op honderdtallen. Hier rond je af op duizendtallen. Kijk naar het cijfer van de honderdtallen.  [Claude, taalfix]
  - `één stap te ver (omhoog)` (fout = antwoord + 1000) → Je gaat de goede kant op, maar één duizendtal te ver. Kies het duizendtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 1000) → Je gaat de goede kant op, maar één duizendtal te ver. Kies het duizendtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 2000 of meer) → Dat ligt te ver weg. Kies een duizendtal vlak naast het getal: het duizendtal eronder of het duizendtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 2000 of meer) → Dat ligt te ver weg. Kies een duizendtal vlak naast het getal: het duizendtal eronder of het duizendtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op duizendtallen: de laatste drie cijfers van het antwoord zijn dus nullen. Zoek de twee duizendtallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de honderdtallen. Is het 5 of meer, dan kies je het duizendtal erboven. Anders kies je het duizendtal eronder.  [nieuw]
- Status: hints klaar

## Somtype 8: In [plek] zijn precies # [ding]. Rond dit aantal af op tientallen.

- Sleutel: nrOrigineel **8** · somtypeOrigineel “In [plek] zijn precies # [ding]. Rond dit aantal af op tientallen.” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C10 (3) · regel: G6-G02-afronden
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 3 items
- Denkfouten (Claude): afronden-verkeerde-kant (3), plaatswaarde-verkeerd (3)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar wat er na de tientallen komt. Is dat minder dan de helft van 10, dan rond je naar beneden af. Anders naar boven.”)
- Voorbeelden:
  - `G6-GET-E01-claude-bank-014` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Vandaag zijn precies 4025 fietsers over de brug gereden. Rond dit aantal af op tientallen.
    - **Antwoord:** 4030  (controle: ok)
    - **Fout-hints (Claude):** 4020 → Kijk naar wat er na de tientallen komt. Is dat minder dan de helft van 10, dan rond je naar beneden af. Anders naar boven. · 4000 → Je hebt op de verkeerde plek afgerond. Het moet op tientallen.
    - **Uitleg (Claude):** 4025 ligt tussen 4020 en 4030. Kijk naar de rest: 5. Dat is precies de helft van 10, dus je rondt naar boven af: 4030.
  - `G6-GET-E01-claude-bank-015` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de kantine zijn dit jaar precies 8081 broodjes verkocht. Rond dit aantal af op tientallen.
    - **Antwoord:** 8080  (controle: ok)
    - **Fout-hints (Claude):** 8090 → Kijk naar wat er na de tientallen komt. Is dat minder dan de helft van 10, dan rond je naar beneden af. Anders naar boven. · 8100 → Je hebt op de verkeerde plek afgerond. Het moet op tientallen.
    - **Uitleg (Claude):** 8081 ligt tussen 8080 en 8090. Kijk naar de rest: 1. Dat is minder dan de helft van 10, dus je rondt naar beneden af: 8080.

- **Hint 1 (te schrijven):** Welke twee tientallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer van de eenheden. Is het 5 of meer, dan rond je af naar het tiental erboven. Anders naar het tiental eronder.
- **Ouderzin:** Je kind rondt een aantal tot 10.000 af op tientallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het nog af op tientallen. Kijk naar het cijfer van de eenheden.  [nieuw]
  - `verkeerde kant` (fout = het andere tiental naast getal1) → Dat is het tiental aan de andere kant van het getal. Kijk naar het cijfer van de eenheden. Is het 5 of meer, dan ga je naar het tiental vlak erboven. Anders naar het tiental vlak eronder.  [Claude, taalfix]
  - `afgerond op honderdtallen` (fout = getal1 afgerond op honderdtallen) → Je hebt afgerond op honderdtallen. Hier rond je af op tientallen. Kijk naar het cijfer van de eenheden.  [Claude, taalfix]
  - `één stap te ver (omhoog)` (fout = antwoord + 10) → Je gaat de goede kant op, maar één tiental te ver. Kies het tiental dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 10) → Je gaat de goede kant op, maar één tiental te ver. Kies het tiental dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 20 of meer) → Dat ligt te ver weg. Kies een tiental vlak naast het getal: het tiental eronder of het tiental erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 20 of meer) → Dat ligt te ver weg. Kies een tiental vlak naast het getal: het tiental eronder of het tiental erboven.  [nieuw]
  - `andere fout` (andere fout) → Je rondt af op tientallen: het laatste cijfer van het antwoord is dus een nul. Zoek de twee tientallen vlak onder en vlak boven het getal. Kijk dan naar het cijfer van de eenheden. Is het 5 of meer, dan kies je het tiental erboven. Anders kies je het tiental eronder.  [nieuw]
- Status: hints klaar
