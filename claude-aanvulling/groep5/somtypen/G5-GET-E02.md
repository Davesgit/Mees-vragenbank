# G5-GET-E02 — Getallenlijn en afronden

Onze omschrijving: Structuren ≤1000; getallenlijn; afronden op honderdtallen · in onze bank: 8 items

Claude-vragen gemapt: **111** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Rond # af op tientallen.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Rond # af op tientallen.” (koppeling: claudeId)
- Items: **60** · Claude-doelen: C10 (60) · regel: G5-G01-afronden
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): afronden-verkeerde-kant (92), schatting-verkeerd (28)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G5-GET-E02-claude-bank-081` (Claude C10, bank, niveau 2 → toepassen)
    - **Opgave:** Rond 162 af op tientallen.
    - **Antwoord:** 160  (controle: ok)
    - **Fout-hints (Claude):** 170 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 180 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E02-claude-bank-063` (Claude C10, bank, niveau 2 → toepassen)
    - **Opgave:** Rond 55 af op tientallen.
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** 100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 80 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Welke twee tientallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer achter de plek van de tientallen. Is het 5 of meer, dan rond je af naar het tiental erboven. Anders naar het tiental eronder.
- **Ouderzin:** Je kind rondt een getal tot 1000 af op tientallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het af: welk tiental ligt er het dichtst bij?  [nieuw]
  - `verkeerde kant` (fout = het andere tiental naast getal1) → Dat is het tiental aan de andere kant van het getal. Kijk naar het cijfer achter de plek van de tientallen. Is het 5 of meer, dan ga je naar het tiental vlak erboven. Anders naar het tiental vlak eronder.  [Claude, taalfix]
  - `één stap te ver (omhoog)` (fout = antwoord + 10) → Je gaat de goede kant op, maar één tiental te ver. Kies het tiental dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 10) → Je gaat de goede kant op, maar één tiental te ver. Kies het tiental dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 20 of meer) → Dat ligt te ver weg. Kies een tiental vlak naast het getal: het tiental eronder of het tiental erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 20 of meer) → Dat ligt te ver weg. Kies een tiental vlak naast het getal: het tiental eronder of het tiental erboven.  [nieuw]
  - `andere fout` (andere fout) → Zoek de twee tientallen vlak onder en vlak boven het getal. Kies het tiental dat er het dichtst bij ligt. Ligt het getal precies in het midden? Dan kies je het tiental erboven.  [nieuw]
- Status: hints klaar

## Somtype 2: Rond # af op honderdtallen.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Rond # af op honderdtallen.” (koppeling: claudeId)
- Items: **27** · Claude-doelen: C10 (27) · regel: G5-G01-afronden
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): afronden-verkeerde-kant (44), schatting-verkeerd (7)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.”)
- Voorbeelden:
  - `G5-GET-E02-claude-bank-010` (Claude C10, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 234 af op honderdtallen.
    - **Antwoord:** 200  (controle: ok)
    - **Fout-hints (Claude):** 100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 400 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E02-claude-bank-005` (Claude C10, bank, niveau 3 → toepassen)
    - **Opgave:** Rond 650 af op honderdtallen.
    - **Antwoord:** 700  (controle: ok)
    - **Fout-hints (Claude):** 600 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Welke twee honderdtallen liggen vlak bij het getal? Eén ligt eronder en één ligt erboven.
- **Hint 2 (te schrijven):** Kijk naar het cijfer achter de plek van de honderdtallen. Is het 5 of meer, dan rond je af naar het honderdtal erboven. Anders naar het honderdtal eronder.
- **Ouderzin:** Je kind rondt een getal tot 1000 af op honderdtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet afgerond` (fout = getal1) → Dat is het getal zelf. Rond het af: welk honderdtal ligt er het dichtst bij?  [nieuw]
  - `verkeerde kant` (fout = het andere honderdtal naast getal1) → Dat is het honderdtal aan de andere kant van het getal. Kijk naar het cijfer achter de plek van de honderdtallen. Is het 5 of meer, dan ga je naar het honderdtal vlak erboven. Anders naar het honderdtal vlak eronder.  [Claude, taalfix]
  - `afgerond op tientallen` (fout = getal1 afgerond op tientallen) → Je hebt afgerond op tientallen. Hier rond je af op honderdtallen: welk honderdtal ligt er het dichtst bij?  [nieuw]
  - `één stap te ver (omhoog)` (fout = antwoord + 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `één stap te ver (omlaag)` (fout = antwoord − 100) → Je gaat de goede kant op, maar één honderdtal te ver. Kies het honderdtal dat vlak naast het getal ligt.  [nieuw]
  - `te ver (omhoog)` (fout = antwoord + 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `te ver (omlaag)` (fout = antwoord − 200 of meer) → Dat ligt te ver weg. Kies een honderdtal vlak naast het getal: het honderdtal eronder of het honderdtal erboven.  [nieuw]
  - `andere fout` (andere fout) → Zoek de twee honderdtallen vlak onder en vlak boven het getal. Kies het honderdtal dat er het dichtst bij ligt. Ligt het getal precies in het midden? Dan kies je het honderdtal erboven.  [nieuw]
- Status: hints klaar

## Somtype 3: [getallenlijn] Rond # af op tientallen. Sleep de stip naar het tiental dat het dichtst bij # [ding].

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[getallenlijn] Rond # af op tientallen. Sleep de stip naar het tiental dat het dichtst bij # [ding].” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C10 (12) · regel: G5-G01-afronden
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 12 (meest: “Kijk naar het laatste cijfer van 91: is het 5 of meer?”)
- Voorbeelden:
  - `G5-GET-E02-claude-bank-099` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Rond 91 af op tientallen. Sleep de stip naar het tiental dat het dichtst bij 91 ligt.
    - **Tekening:** `{"soort": "getallenlijn", "van": 90, "tot": 100, "stap": 1, "labels": [90, 100], "stip": 91, "kindSleept": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 90  (controle: ok)
    - **Fout-hints (Claude):** 100 → Kijk naar het laatste cijfer van 91: is het 5 of meer?
    - **Uitleg (Claude):** 91 ligt tussen 90 en 100. Het cijfer 1 is kleiner dan 5, dus naar beneden: 90.
  - `G5-GET-E02-claude-bank-092` (Claude C10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Rond 16 af op tientallen. Sleep de stip naar het tiental dat het dichtst bij 16 ligt.
    - **Tekening:** `{"soort": "getallenlijn", "van": 10, "tot": 20, "stap": 1, "labels": [10, 20], "stip": 16, "kindSleept": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 10 → Kijk naar het laatste cijfer van 16: is het 5 of meer?
    - **Uitleg (Claude):** 16 ligt tussen 10 en 20. Het cijfer 6 is 5 of meer, dus naar boven: 20.

- **Hint 1 (te schrijven):** De stip staat tussen twee tientallen. Bij welk tiental staat hij het dichtst?
- **Hint 2 (te schrijven):** Tel de stapjes van de stip naar het ene tiental en naar het andere. Sleep de stip naar het tiental met de minste stapjes.
- **Ouderzin:** Je kind rondt op de getallenlijn een getal af op tientallen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde tiental` (Claudes sleutel: het andere tiental (tekst per item)) → Kijk naar het laatste cijfer van …: is het 5 of meer?  [Claude, ok]
  - `andere fout` (andere fout) → Kijk naar het laatste cijfer van het getal. Is het 5 of meer, dan ga je naar het tiental erboven. Anders naar het tiental eronder.  [nieuw]
- Status: hints klaar

## Somtype 4: [getallenlijn] Zet # op de getallenlijn van # [ding] #.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[getallenlijn] Zet # op de getallenlijn van # [ding] #.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C1 (12) · regel: G5-G02-getallenlijn
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-GET-E02-claude-bank-102` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 660 op de getallenlijn van 0 tot 1000.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 1000, "stap": 10, "labels": [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 660  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Elk streepje is 100. 660 ligt tussen 600 en 700.
  - `G5-GET-E02-claude-bank-104` (Claude C1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 860 op de getallenlijn van 0 tot 1000.
    - **Tekening:** `{"soort": "getallenlijn", "van": 0, "tot": 1000, "stap": 10, "labels": [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], "kindTikt": true}`
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 860  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Elk streepje is 100. 860 ligt tussen 800 en 900.

- **Hint 1 (te schrijven):** Zoek eerst het honderdtal: tussen welke twee honderdtallen ligt het getal?
- **Hint 2 (te schrijven):** Tel dan vanaf dat honderdtal verder in stapjes van tien.
- **Ouderzin:** Je kind zet een getal tot 1000 op een getallenlijn met honderdtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `honderdtal te ver` (fout = antwoord + 100) → Dat is één honderdtal te ver. Het cijfer vooraan zegt bij welk honderdtal je begint.  [nieuw]
  - `honderdtal niet ver genoeg` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Het cijfer vooraan zegt bij welk honderdtal je begint.  [nieuw]
  - `stapje te ver` (fout = antwoord + 10) → Bijna! Dat is één stapje van tien te ver. Tel de stapjes na het honderdtal nog eens.  [nieuw]
  - `stapje niet ver genoeg` (fout = antwoord − 10) → Bijna! Dat is één stapje van tien te weinig. Tel de stapjes na het honderdtal nog eens.  [nieuw]
  - `andere fout` (andere fout) → Zoek eerst het honderdtal van het getal. Tel dan verder in stapjes van tien tot je bij het getal bent.  [nieuw]
- Status: hints klaar
