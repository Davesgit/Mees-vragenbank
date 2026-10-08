# G6-GET-M06 — Keer en delen met grotere getallen

Onze omschrijving: ×÷ ±10.000: 1×2/3-cijferig / 2–3÷1-cijferig (opbouw) · in onze bank: 8 items

Claude-vragen gemapt: **322** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # × # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **284** · Claude-doelen: C7 (284) · regel: G6-C07-keer
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 284 items
- Denkfouten (Claude): tiental-ernaast (225), een-ernaast (223), optellen-ipv-vermenigvuldigen (66), onthouden-vergeten (54)
- Verschillende Claude-fout-hints: 4 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-293` (Claude C7, bank, niveau 3 → toepassen)
    - **Opgave:** 113 × 9 =
    - **Antwoord:** 1017  (controle: ok)
    - **Fout-hints (Claude):** 997 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 1016 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-GET-M06-claude-bank-045` (Claude C7, bank, niveau 3 → toepassen)
    - **Opgave:** 588 × 3 =
    - **Antwoord:** 1764  (controle: ok)
    - **Fout-hints (Claude):** 1774 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 591 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.

- **Hint 1 (te schrijven):** Splits het eerste getal in honderdtallen, tientallen en eenheden. Staat er een nul? Dan is dat stuk nul.
- **Hint 2 (te schrijven):** Doe elk stuk keer het tweede getal. Tel de uitkomsten daarna bij elkaar op.
- **Ouderzin:** Je kind rekent een keersom uit: een getal van drie cijfers keer een getal onder de tien.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Kijk naar het teken: het is een keersom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken elk stuk nog eens na, en tel alle stukken goed op.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken elk stuk nog eens na, en tel alle stukken goed op.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `alleen laatste cijfer` (Claudes sleutel: onthouden-vergeten) → Je hebt bij elk cijfer alleen het laatste cijfer van die keersom opgeschreven. Komt een keersom op tien of meer? Dan gaan de tientallen mee naar de plek links ervan.  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het eerste getal in honderdtallen, tientallen en eenheden. Doe elk stuk keer het tweede getal en tel alles op.  [nieuw]
- Status: hints klaar

## Somtype 2: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: C16 (32) · regel: G6-C04-delen-happen
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (64), deel-vergeten-bij-splitsen (32)
- Verschillende Claude-fout-hints: 65 (meest: “Tel alle happen bij elkaar op. Je bent er een hap van 10 kwijt.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-007` (Claude C16, gegenereerd, niveau 1 → basis)
    - **Opgave:** 136 tanden worden eerlijk verdeeld over 4 dino's. Hoeveel tanden krijgt elke dino?
    - **Antwoord:** 34  (controle: ok)
    - **Fout-hints (Claude):** 24 → Tel alle happen bij elkaar op. Je bent er een hap van 10 kwijt. · 35 → Controleer. 4 × 35 = 140, dat is meer dan 136. · 33 → Controleer. 4 × 33 = 132, dat is minder dan 136.
    - **Uitleg (Claude):** Hap eerst 30 keer 4 eraf: 136 − 120 = 16. Dan nog 4 keer 4: 16 − 16 = 0. Samen 30 + 4 = 34 happen.
  - `G6-GET-M06-claude-bank-004` (Claude C16, gegenereerd, niveau 1 → basis)
    - **Opgave:** 96 stickers worden eerlijk verdeeld over 3 kinderen. Hoeveel stickers krijgt elk kind?
    - **Antwoord:** 32  (controle: ok)
    - **Fout-hints (Claude):** 22 → Tel alle happen bij elkaar op. Je bent er een hap van 10 kwijt. · 33 → Controleer. 3 × 33 = 99, dat is meer dan 96. · 31 → Controleer. 3 × 31 = 93, dat is minder dan 96.
    - **Uitleg (Claude):** Hap eerst 30 keer 3 eraf: 96 − 90 = 6. Dan nog 2 keer 3: 6 − 6 = 0. Samen 30 + 2 = 32 happen.

- **Hint 1 (te schrijven):** Eerlijk verdelen is een deelsom. Hoeveel krijgt ieder?
- **Hint 2 (te schrijven):** Splits het totaal in stukken die je makkelijk kunt verdelen. Verdeel elk stuk en tel op wat ieder krijgt.
- **Ouderzin:** Je kind verdeelt eerlijk: een deelsom die precies uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het aantal waarover je verdeelt` (fout = getal2) → Dat is het aantal waarover je verdeelt. De vraag is hoeveel ieder krijgt.  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt eerlijk verdeeld: dat is een deelsom.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er wordt eerlijk verdeeld: dat is een deelsom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom. [getal2] keer jouw antwoord is meer dan [getal1].  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom. [getal2] keer jouw antwoord is minder dan [getal1].  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Ben je een stuk vergeten? Reken na met een keersom. [getal2] keer jouw antwoord is minder dan [getal1].  [nieuw]
  - `andere fout` (andere fout) → Reken na met een keersom: het aantal waarover je verdeelt keer jouw antwoord moet precies het totaal zijn.  [nieuw]
- Status: hints klaar

## Somtype 3: [wie] verzamelt elke dag # [ding]. Hoeveel [ding] zijn dat in # dagen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[wie] verzamelt elke dag # [ding]. Hoeveel [ding] zijn dat in # dagen?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C7 (3) · regel: G6-C07-keer
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 3 items
- Denkfouten (Claude): nul-fout-tientallen (6), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 8 (meest: “Dat is een nul te veel. 900 heeft twee nullen, dus het antwoord krijgt er ook twee.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-322` (Claude C7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een tuinder verzamelt elke dag 900 tomaten. Hoeveel tomaten zijn dat in 6 dagen?
    - **Antwoord:** 5400  (controle: ok)
    - **Fout-hints (Claude):** 540 → Reken eerst 6 × 9. Plak daarna twee nullen er weer aan. Je mist er één. · 54.000 → Dat is een nul te veel. 900 heeft twee nullen, dus het antwoord krijgt er ook twee. · 906 → Elke dag 900 erbij, 6 dagen lang. Dat is een keersom.
    - **Uitleg (Claude):** 6 × 900 lijkt op 6 × 9. 6 × 9 = 54. De twee nullen van 900 er weer aan: 5400.
  - `G6-GET-M06-claude-bank-320` (Claude C7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kippenboer verzamelt elke dag 400 eieren. Hoeveel eieren zijn dat in 9 dagen?
    - **Antwoord:** 3600  (controle: ok)
    - **Fout-hints (Claude):** 360 → Reken eerst 9 × 4. Plak daarna twee nullen er weer aan. Je mist er één. · 36.000 → Dat is een nul te veel. 400 heeft twee nullen, dus het antwoord krijgt er ook twee. · 409 → Elke dag 400 erbij, 9 dagen lang. Dat is een keersom.
    - **Uitleg (Claude):** 9 × 400 lijkt op 9 × 4. 9 × 4 = 36. De twee nullen van 400 er weer aan: 3600.

- **Hint 1 (te schrijven):** Elke dag komt er evenveel bij: dat is een keersom. Het aantal dagen keer het aantal per dag.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet daarna de nullen van het ronde getal erachter.
- **Ouderzin:** Je kind rekent een keersom met een rond getal: eerst zonder de nullen, dan de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Elke dag komt er evenveel bij: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is een nul te veel. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is een nul te weinig. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nullen vergeten` (Claudes sleutel: nul-fout-tientallen) → Er missen nullen. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen: een keersom uit de tafels. Zet daarna de nullen van het ronde getal erachter.  [nieuw]
- Status: hints klaar

## Somtype 4: Een raket verbruikt bij de start # liter brandstof per seconde. Hoeveel liter is dat in # seconden?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een raket verbruikt bij de start # liter brandstof per seconde. Hoeveel liter is dat in # seconden?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C7 (1) · regel: G6-C07-keer
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 1 items
- Denkfouten (Claude): nul-fout-tientallen (2), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “700 heeft twee nullen. Je hebt er maar één aan 28 geplakt.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-317` (Claude C7, handmatig, niveau 3 → toepassen)
    - **Opgave:** Een raket verbruikt bij de start 700 liter brandstof per seconde. Hoeveel liter is dat in 4 seconden?
    - **Antwoord:** 2800  (controle: ok)
    - **Fout-hints (Claude):** 280 → 700 heeft twee nullen. Je hebt er maar één aan 28 geplakt. · 28 → 4 × 7 = 28 is de eerste stap. Maar het was 700 liter per seconde. Plak de nullen er weer aan. · 704 → 4 + 700 telt de seconden bij de liters op. Maar élke seconde gaan er 700 liter doorheen.
    - **Uitleg (Claude):** 4 × 700 lijkt op 4 × 7. 4 × 7 = 28. De twee nullen van 700 er weer aan: 2800.

- **Hint 1 (te schrijven):** Elke seconde gaat er evenveel doorheen: dat is een keersom. Het aantal seconden keer het aantal liter per seconde.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet daarna de nullen van het ronde getal erachter.
- **Ouderzin:** Je kind rekent een keersom met een rond getal: eerst zonder de nullen, dan de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Elke seconde gaat er evenveel doorheen: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is een nul te veel. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is een nul te weinig. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nullen vergeten` (Claudes sleutel: nul-fout-tientallen) → Er missen nullen. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen: een keersom uit de tafels. Zet daarna de nullen van het ronde getal erachter.  [nieuw]
- Status: hints klaar

## Somtype 5: Een satelliet draait # keer per dag om de aarde. Hoeveel [ding] zijn dat in # dagen?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Een satelliet draait # keer per dag om de aarde. Hoeveel [ding] zijn dat in # dagen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C7 (1) · regel: G6-C07-keer
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 1 items
- Denkfouten (Claude): nul-fout-tientallen (2), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Bijna! 400 heeft twee nullen. Je hebt er maar één aan 24 geplakt.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-318` (Claude C7, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een satelliet draait 6 keer per dag om de aarde. Hoeveel rondjes zijn dat in 400 dagen?
    - **Antwoord:** 2400  (controle: ok)
    - **Fout-hints (Claude):** 240 → Bijna! 400 heeft twee nullen. Je hebt er maar één aan 24 geplakt. · 24 → 6 × 4 = 24 is de eerste stap. Maar het waren 400 dagen, niet 4. Plak de nullen er weer aan. · 406 → Elke dag 6 rondjes, 400 dagen lang. Dat is een keersom, geen plussom.
    - **Uitleg (Claude):** 6 × 400 lijkt op 6 × 4. 6 × 4 = 24. Nu de twee nullen van 400 er weer aan: 2400.

- **Hint 1 (te schrijven):** Elke dag evenveel rondjes: dat is een keersom. Het aantal dagen keer het aantal rondjes per dag.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet daarna de nullen van het ronde getal erachter.
- **Ouderzin:** Je kind rekent een keersom met een rond getal: eerst zonder de nullen, dan de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Elke dag gaat het evenveel keer rond: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is een nul te veel. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is een nul te weinig. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nullen vergeten` (Claudes sleutel: nul-fout-tientallen) → Er missen nullen. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen: een keersom uit de tafels. Zet daarna de nullen van het ronde getal erachter.  [nieuw]
- Status: hints klaar

## Somtype 6: Het stadion heeft # [ding] met in elk vak # [ding]. Hoeveel [ding] zitten er in [plek]?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Het stadion heeft # [ding] met in elk vak # [ding]. Hoeveel [ding] zitten er in [plek]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C7 (1) · regel: G6-C07-keer
- Getallenruimte: 0–10.000 · type: kale
- Uit de G5-park: 1 items
- Denkfouten (Claude): nul-fout-tientallen (2), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “300 heeft twee nullen. Je hebt er maar één aan 24 geplakt.”)
- Voorbeelden:
  - `G6-GET-M06-claude-bank-319` (Claude C7, handmatig, niveau 2 → toepassen)
    - **Opgave:** Het stadion heeft 8 vakken met in elk vak 300 mensen. Hoeveel mensen zitten er in het stadion?
    - **Antwoord:** 2400  (controle: ok)
    - **Fout-hints (Claude):** 240 → 300 heeft twee nullen. Je hebt er maar één aan 24 geplakt. · 24 → 8 × 3 = 24 is de eerste stap. Het waren vakken van 300 mensen, niet van 3. · 308 → 8 + 300 is één vak plus het aantal vakken. Maar in élk van de 8 vakken zitten 300 mensen.
    - **Uitleg (Claude):** 8 × 300 lijkt op 8 × 3. 8 × 3 = 24. De twee nullen van 300 er weer aan: 2400.

- **Hint 1 (te schrijven):** In elk vak zitten evenveel mensen: dat is een keersom. Het aantal vakken keer het aantal in elk vak.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet daarna de nullen van het ronde getal erachter.
- **Ouderzin:** Je kind rekent een keersom met een rond getal: eerst zonder de nullen, dan de nullen erachter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. In elk vak zitten evenveel mensen: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is een nul te veel. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is een nul te weinig. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [nieuw]
  - `nullen vergeten` (Claudes sleutel: nul-fout-tientallen) → Er missen nullen. Tel de nullen van het ronde getal: zoveel nullen zet je erachter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen: een keersom uit de tafels. Zet daarna de nullen van het ronde getal erachter.  [nieuw]
- Status: hints klaar
