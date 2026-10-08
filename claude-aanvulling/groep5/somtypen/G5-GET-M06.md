# G5-GET-M06 — Delen met rest

Onze omschrijving: Deelteken; verdelen in/over; rest · in onze bank: 8 items

Claude-vragen gemapt: **183** in **9** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Er zijn # [ding]. Ze gaan eerlijk over # [ding]. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Er zijn # [ding]. Ze gaan eerlijk over # [ding]. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **90** · Claude-doelen: T9 (90) · regel: G07-welke-som, D-DEELTEKEN-FORMEEL
- Getallenruimte: 0–1.000, 0–10, 0–100, 0–20 · type: meerkeuze
- Didactiek-besluit (G4-twijfel, 1 okt): verhaal → formele deelsom met ‘:’ — zie g4/besluiten_twijfel.md
- Uitleg bij het eerste gebruik (kindtekst, veld begripUitleg): “':' betekent gedeeld door.”
- Denkfouten (Claude): omgekeerd-gedeeld (90), verkeerde-bewerking (90)
- Verschillende Claude-fout-hints: 2 (meest: “Wat verdeel je? Dat getal komt vóór het deelteken.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-075` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** Er zijn 315 appels. Ze gaan eerlijk over 7 borden. Welke som hoort bij dit verhaal?
    - **Opties:** A) 315 × 7 · B) 7 : 315 · C) 315 : 7
    - **Antwoord:** 315 : 7  (controle: ok)
    - **Fout-hints (Claude):** 7 : 315 → Wat verdeel je? Dat getal komt vóór het deelteken. · 315 × 7 → Je verdeelt. Is dat keer of gedeeld door?
  - `G5-GET-M06-claude-bank-143` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** Er zijn 84 appels. Ze gaan eerlijk over 6 zakken. Welke som hoort bij dit verhaal?
    - **Opties:** A) 84 : 6 · B) 84 × 6 · C) 6 : 84
    - **Antwoord:** 84 : 6  (controle: ok)
    - **Fout-hints (Claude):** 6 : 84 → Wat verdeel je? Dat getal komt vóór het deelteken. · 84 × 6 → Je verdeelt. Is dat keer of gedeeld door?

- **Hint 1 (te schrijven):** Lees het verhaal: wat wordt er verdeeld, en over hoeveel?
- **Hint 2 (te schrijven):** Eerlijk verdelen is een deelsom. Welk getal wordt er verdeeld?
- **Ouderzin:** Je kind kiest de deelsom die bij een verhaaltje hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keersom` (de keersom) → Je kiest een keersom, maar er wordt eerlijk verdeeld. Verdelen is een deelsom.  [nieuw]
  - `getallen omgedraaid` (Claudes sleutel: omgekeerd-gedeeld) → De getallen staan andersom. Wat verdeel je? Dat getal komt vóór het deelteken (:).  [Claude, taalfix]
  - `andere fout` (andere fout) → Wat wordt er verdeeld? Dat getal komt vóór het deelteken (:). Over hoeveel? Dat getal komt erachter.  [nieuw]
- Status: hints klaar

## Somtype 2: Er zijn # [ding]. Ze gaan in [bakken] van #. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Er zijn # [ding]. Ze gaan in [bakken] van #. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: D5-6 (32) · regel: G5-C02-verdelen
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (60), getal-overgenomen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-167` (Claude D5-6, bank, niveau 3 → toepassen)
    - **Opgave:** Er zijn 12 knikkers. Ze gaan in dozen van 6. Hoeveel dozen zijn dat?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 1 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-M06-claude-bank-175` (Claude D5-6, bank, niveau 3 → toepassen)
    - **Opgave:** Er zijn 70 ballen. Ze gaan in bakken van 7. Hoeveel bakken zijn dat?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 11 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 12 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Hoeveel gaan er in elk? Hoe vaak past dat in het totaal?
- **Hint 2 (te schrijven):** Denk aan de keersom: hoeveel keer het aantal in elk is het totaal?
- **Ouderzin:** Je kind rekent uit hoeveel groepjes je kunt maken (deelsom die precies uitkomt).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het aantal in elk` (fout = getal2) → Dat is het aantal in elk. De vraag is hoe vaak dat in het totaal past.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Kijk hoeveel er in elk gaan. Hoe vaak past dat in het totaal?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom: dan heb je er meer nodig dan er zijn.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom: dan blijven er nog over.  [nieuw]
  - `twee te veel` (fout = antwoord + 2) → Dat is twee te veel. Reken na met een keersom: dan heb je er meer nodig dan er zijn.  [nieuw]
  - `twee te weinig` (fout = antwoord − 2) → Dat is twee te weinig. Reken na met een keersom: dan blijven er nog over.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op van het aantal in elk, tot je bij het totaal bent. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar

## Somtype 3: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel blijven er over?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: C8 (16) · regel: G5-C03-rest
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): rest-vergeten (30), andere-deel-genomen (15)
- Verschillende Claude-fout-hints: 7 (meest: “Het komt niet precies uit: er blijft iets over.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-036` (Claude C8, gegenereerd, niveau 1 → basis)
    - **Opgave:** 64 tanden worden eerlijk verdeeld over 7 dino's. Hoeveel tanden blijven er over?
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 9 → Dat is wat elke dino krijgt. Gevraagd is wat er overblijft. · 8 → Er past nog een hele ronde bij. De rest is altijd kleiner dan het aantal waarover je verdeelt. · 0 → Het komt niet precies uit: er blijft iets over.
    - **Uitleg (Claude):** 7 × 9 = 63, dat is het meeste dat past. 64 − 63 = 1 over.
  - `G5-GET-M06-claude-bank-034` (Claude C8, gegenereerd, niveau 1 → basis)
    - **Opgave:** 19 stickers worden eerlijk verdeeld over 3 spelers. Hoeveel stickers blijven er over?
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 6 → Dat is wat elke speler krijgt. Gevraagd is wat er overblijft. · 4 → Er past nog een hele ronde bij. De rest is altijd kleiner dan het aantal waarover je verdeelt. · 0 → Het komt niet precies uit: er blijft iets over.
    - **Uitleg (Claude):** 3 × 6 = 18, dat is het meeste dat past. 19 − 18 = 1 over.

- **Hint 1 (te schrijven):** Verdeel eerlijk: iedereen krijgt evenveel. Hoeveel krijgt ieder, en hoeveel blijven er over?
- **Hint 2 (te schrijven):** Zoek de grootste keersom met het aantal waarover je verdeelt, die niet boven het totaal komt. Wat er daarna nog over is, is de rest.
- **Ouderzin:** Je kind verdeelt eerlijk en rekent uit hoeveel er overblijft (de rest).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `wat ieder krijgt` (Claudes sleutel: andere-deel-genomen) → Dat is wat ieder krijgt. De vraag is hoeveel er overblijft.  [Claude, taalfix]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er wordt verdeeld: dat is een deelsom. Hoeveel blijft er over?  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt verdeeld: dat is een deelsom.  [nieuw]
  - `nog een ronde` (fout = antwoord + getal2) → Dat is te veel. Daar past nog een hele ronde bij: iedereen kan er nog één krijgen. Wat overblijft, de rest, is altijd kleiner dan het aantal waarover je verdeelt.  [Claude, taalfix]
  - `niets over` (Claudes sleutel: rest-vergeten) → Het komt niet precies uit: er blijft iets over.  [Claude, ok]
  - `andere fout` (andere fout) → Reken eerst uit hoeveel ieder krijgt. Hoeveel heb je dan uitgedeeld? Wat er nog over is, is de rest.  [nieuw]
- Status: hints klaar

## Somtype 4: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel krijgt [wie]? (De rest blijft over.)

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel krijgt [wie]? (De rest blijft over.)” (koppeling: claudeId)
- Items: **16** · Claude-doelen: C8 (16) · regel: G5-C03-rest
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): rest-vergeten (16), andere-deel-genomen (16)
- Verschillende Claude-fout-hints: 7 (meest: “Eén stap hoger in de tafel kom je boven het totaal uit. Dat past niet.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-043` (Claude C8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 67 eieren worden eerlijk verdeeld over 7 dino's. Hoeveel krijgt elke dino? (De rest blijft over.)
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 8 → Eén stap hoger in de tafel kom je boven het totaal uit. Dat past niet. · 1 → Dat is de rest. Gevraagd is hoeveel elke dino krijgt.
    - **Uitleg (Claude):** Zoek in de tafel van 7: 7 × 9 = 63 past nog, 7 × 10 = 70 niet. Dus 9, rest 4.
  - `G5-GET-M06-claude-bank-040` (Claude C8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 14 stickers worden eerlijk verdeeld over 3 kinderen. Hoeveel krijgt elk kind? (De rest blijft over.)
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Eén stap hoger in de tafel kom je boven het totaal uit. Dat past niet. · 2 → Dat is de rest. Gevraagd is hoeveel elk kind krijgt.
    - **Uitleg (Claude):** Zoek in de tafel van 3: 3 × 4 = 12 past nog, 3 × 5 = 15 niet. Dus 4, rest 2.

- **Hint 1 (te schrijven):** Verdeel eerlijk: iedereen krijgt evenveel. Wat er overblijft, heet de rest. Die krijgt niemand.
- **Hint 2 (te schrijven):** Zoek de grootste keersom met het aantal waarover je verdeelt, die niet boven het totaal komt.
- **Ouderzin:** Je kind verdeelt eerlijk en rekent uit hoeveel ieder krijgt (er blijft iets over).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het aantal waarover je verdeelt` (fout = getal2) → Dat is het aantal waarover je verdeelt. De vraag is hoeveel ieder krijgt.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er wordt eerlijk verdeeld: dat is een deelsom.  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt verdeeld: dat is een deelsom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Dat is één te veel. Eén stap hoger in de tafel kom je boven het totaal uit.  [Claude, taalfix]
  - `de rest` (Claudes sleutel: andere-deel-genomen) → Dat is wat er overblijft: de rest. De vraag is hoeveel ieder krijgt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zeg de tafel op van het aantal waarover je verdeelt. Stop vlak voordat je boven het totaal komt. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar

## Somtype 5: # [ding] hebben samen # [ding], allemaal evenveel. Hoeveel [ding] heeft [wie]?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# [ding] hebben samen # [ding], allemaal evenveel. Hoeveel [ding] heeft [wie]?” (koppeling: claudeId)
- Items: **10** · Claude-doelen: D5-9 (10) · regel: G5-C02-verdelen
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): tafelbuur (10), verkeerde-bewerking (10), getal-overgenomen (10)
- Verschillende Claude-fout-hints: 12 (meest: “Zeg de tafel op tot je precies bij het totaal bent, niet erover.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-016` (Claude D5-9, gegenereerd, niveau 1 → basis)
    - **Opgave:** 9 dino's hebben samen 63 tanden, allemaal evenveel. Hoeveel tanden heeft elke dino?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 8 → Zeg de tafel op tot je precies bij het totaal bent, niet erover. · 54 → Verdelen is delen, niet aftrekken. · 63 → 63 is het totaal. Gevraagd is hoeveel elke dino krijgt.
    - **Uitleg (Claude):** Keer en deel horen bij elkaar: 9 × 7 = 63, dus 63 : 9 = 7.
  - `G5-GET-M06-claude-bank-018` (Claude D5-9, gegenereerd, niveau 1 → basis)
    - **Opgave:** 6 kinderen hebben samen 12 stickers, allemaal evenveel. Hoeveel stickers heeft elk kind?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Zeg de tafel op tot je precies bij het totaal bent, niet erover. · 6 → Verdelen is delen, niet aftrekken. · 12 → 12 is het totaal. Gevraagd is hoeveel elk kind krijgt.
    - **Uitleg (Claude):** Keer en deel horen bij elkaar: 6 × 2 = 12, dus 12 : 6 = 2.

- **Hint 1 (te schrijven):** Ze hebben allemaal evenveel. Verdeel het totaal eerlijk over iedereen.
- **Hint 2 (te schrijven):** Denk aan de keersom: hoeveel keer het aantal waarover je verdeelt, is het totaal?
- **Ouderzin:** Je kind verdeelt een totaal eerlijk (deelsom die precies uitkomt).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het totaal` (fout = getal2) → Dat is het totaal. De vraag is hoeveel ieder heeft.  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Ze verdelen: dat is een deelsom.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Ze verdelen: dat is een deelsom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom: dan kom je boven het totaal.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom: dan kom je onder het totaal.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op van het aantal waarover je verdeelt, tot je bij het totaal bent. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar

## Somtype 6: # [ding] worden verdeeld over # [ding]. [wie] krijgt evenveel. Hoeveel blijven er over?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “# [ding] worden verdeeld over # [ding]. [wie] krijgt evenveel. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C8 (8) · regel: G5-C03-rest
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): rest-vergeten (22)
- Verschillende Claude-fout-hints: 21 (meest: “11 is wat elke dino krijgt. De vraag is hoeveel er óverblijft.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-054` (Claude C8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 94 blaadjes worden verdeeld over 8 dino's. Elke dino krijgt evenveel. Hoeveel blaadjes blijven er over?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 11 → 11 is wat elke dino krijgt. De vraag is hoeveel er óverblijft. · 2 → Reken terug. 8 × 11 = 88. Hoeveel is 94 meer dan dat? · 14 → Als er 14 overblijven, kan elke dino er nog één krijgen. De rest is altijd kleiner dan 8.
    - **Uitleg (Claude):** 8 × 11 = 88, dat past nog in 94. 8 × 12 = 96, dat is te veel. Dus elke dino krijgt 11, en 94 − 88 = 6 blijft over.
  - `G5-GET-M06-claude-bank-061` (Claude C8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 29 balletjes worden verdeeld over 7 poezen. Elke poes krijgt evenveel. Hoeveel balletjes blijven er over?
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 4 → 4 is wat elke poes krijgt. De vraag is hoeveel er óverblijft. · 6 → Reken terug. 7 × 4 = 28. Hoeveel is 29 meer dan dat? · 8 → Als er 8 overblijven, kan elke poes er nog één krijgen. De rest is altijd kleiner dan 7.
    - **Uitleg (Claude):** 7 × 4 = 28, dat past nog in 29. 7 × 5 = 35, dat is te veel. Dus elke poes krijgt 4, en 29 − 28 = 1 blijft over.

- **Hint 1 (te schrijven):** Verdeel eerlijk: iedereen krijgt evenveel. Hoeveel krijgt ieder, en hoeveel blijven er over?
- **Hint 2 (te schrijven):** Zoek de grootste keersom met het aantal waarover je verdeelt, die niet boven het totaal komt. Wat er daarna nog over is, is de rest.
- **Ouderzin:** Je kind verdeelt eerlijk en rekent uit hoeveel er overblijft (de rest).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er wordt verdeeld: dat is een deelsom. Hoeveel blijft er over?  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt verdeeld: dat is een deelsom.  [nieuw]
  - `nog een ronde` (fout = antwoord + getal2) → Dat is te veel. Daar past nog een hele ronde bij: iedereen kan er nog één krijgen. Wat overblijft, de rest, is altijd kleiner dan het aantal waarover je verdeelt.  [Claude, taalfix]
  - `niet de rest` (Claudes sleutel: rest-vergeten) → Dat is niet wat er overblijft. Reken eerst uit hoeveel ieder krijgt. Reken dan terug: hoeveel is er nog over na het verdelen?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst uit hoeveel ieder krijgt. Hoeveel heb je dan uitgedeeld? Wat er nog over is, is de rest.  [nieuw]
- Status: hints klaar

## Somtype 7: # [ding] gaan eten. Aan elke tafel passen er #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “# [ding] gaan eten. Aan elke tafel passen er #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: T9 (5) · regel: FX-G4-2/23
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): rest-vergeten (5)
- Verschillende Claude-fout-hints: 4 (meest: “Dan blijven er eekhoorns staan. Die moeten ook mee, dus je hebt er een extra nodig.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-004` (Claude T9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 50 kinderen gaan eten. Aan elke tafel passen er 8. Hoeveel tafels zijn er nodig?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 6 → Dan blijven er dino's staan. Die moeten ook mee, dus je hebt er een extra nodig. · 6,2 → Je kunt geen halve bus nemen. Rond naar boven af.
    - **Uitleg (Claude):** 50 : 8 = 6 rest 2. De rest moet ook mee, dus je hebt er een extra nodig: 7.
  - `G5-GET-M06-claude-bank-002` (Claude T9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 58 kinderen gaan eten. Aan elke tafel passen er 8. Hoeveel tafels zijn er nodig?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 7 → Dan blijven er eekhoorns staan. Die moeten ook mee, dus je hebt er een extra nodig. · 7,2 → Je kunt geen halve bus nemen. Rond naar boven af.
    - **Uitleg (Claude):** 58 : 8 = 7 rest 2. De rest moet ook mee, dus je hebt er een extra nodig: 8.

- **Hint 1 (te schrijven):** Hoeveel passen er aan één tafel? Hoe vaak past dat in het totaal?
- **Hint 2 (te schrijven):** Blijft er na het verdelen nog iemand over? Dan is er nog een tafel nodig.
- **Ouderzin:** Je kind rekent uit hoeveel tafels er nodig zijn, ook voor wie overblijft (naar boven afronden).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er moet verdeeld worden: hoe vaak past het aantal aan één tafel in het totaal?  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt verdeeld: dat is een deelsom.  [nieuw]
  - `één tafel te weinig` (fout = antwoord − 1) → Dat is één tafel te weinig. Dan heeft niet iedereen een plek. Voor wie overblijft, is nog een tafel nodig.  [nieuw]
  - `andere fout` (andere fout) → Spring in sprongen van het aantal aan één tafel, tot je bij het totaal komt. Blijft er iemand over? Ook die heeft een plek nodig.  [nieuw]
- Status: hints klaar

## Somtype 8: # [ding] gaan op stap. In elk(e) [bak] passen er #. Hoeveel [ding] zijn er nodig?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “# [ding] gaan op stap. In elk(e) [bak] passen er #. Hoeveel [ding] zijn er nodig?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: T9 (3) · regel: G08-op-stap, FX-G4-2/23
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): rest-vergeten (3), rest-achter-komma (3)
- Verschillende Claude-fout-hints: 3 (meest: “Dan blijven er kinderen staan. Die moeten ook mee, dus je hebt er een extra nodig.”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-006` (Claude T9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 52 kinderen gaan op stap. In elk busje passen er 8. Hoeveel busjes zijn er nodig?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 9 → Dan blijven er kinderen staan. Die moeten ook mee, dus je hebt er een extra nodig. · 9,18 → Je kunt geen halve bus nemen. Rond naar boven af.
    - **Uitleg (Claude):** 52 : 8 = 6 rest 4. De rest moet ook mee, dus je hebt er een extra nodig: 7.
  - `G5-GET-M06-claude-bank-008` (Claude T9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 34 kinderen gaan op stap. In elke boot passen er 4. Hoeveel boten zijn er nodig?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 3 → Dan blijven er kinderen staan. Die moeten ook mee, dus je hebt er een extra nodig. · 3,4 → Je kunt geen halve bus nemen. Rond naar boven af.
    - **Uitleg (Claude):** 34 : 4 = 8 rest 2. De rest moet ook mee, dus je hebt er een extra nodig: 9.

- **Hint 1 (te schrijven):** Hoeveel passen er in elk? Hoe vaak past dat in het totaal?
- **Hint 2 (te schrijven):** Blijft er na het verdelen nog iemand over? Dan is er nog één nodig.
- **Ouderzin:** Je kind rekent uit hoeveel er nodig zijn, ook voor wie overblijft (naar boven afronden).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er moet verdeeld worden: hoe vaak past het aantal in elk in het totaal?  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Er wordt verdeeld: dat is een deelsom.  [nieuw]
  - `rest achter de komma` (fout = quotiënt,rest) → Je schreef de rest achter een komma. De vraag is hoeveel er nodig zijn.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Dat is één te weinig. Dan kan niet iedereen mee. Voor wie overblijft, is er nog één nodig.  [nieuw]
  - `kommagetal` (fout = een kommagetal) → Een kommagetal kan hier niet: je kunt geen stukje nemen. Hoeveel heb je er nodig, zodat iedereen mee kan?  [nieuw]
  - `andere fout` (andere fout) → Hoe vaak past het aantal in elk in het totaal? Blijft er iemand over? Ook die moet mee.  [nieuw]
- Status: hints klaar

## Somtype 9: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C9 (3) · regel: G5-C02-verdelen
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (6), verkeerde-bewerking (3)
- Verschillende Claude-fout-hints: 7 (meest: “Verdelen is delen, niet aftrekken. Hoe vaak past de groep erin?”)
- Voorbeelden:
  - `G5-GET-M06-claude-bank-020` (Claude C9, gegenereerd, niveau 1 → basis)
    - **Opgave:** 72 blaadjes worden eerlijk verdeeld over 8 dino's. Hoeveel blaadjes krijgt elke dino?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 10 → Controleer. 8 × 10 = 80. Dat is te veel. · 8 → Controleer. 8 × 8 = 64. Dan blijft er over. · 64 → Verdelen is delen, niet aftrekken. Hoe vaak past de groep erin?
    - **Uitleg (Claude):** Denk aan de tafel van 8: 8 × ? = 72. 8 × 9 = 72, dus 72 : 8 = 9.
  - `G5-GET-M06-claude-bank-019` (Claude C9, gegenereerd, niveau 1 → basis)
    - **Opgave:** 42 knikkers worden eerlijk verdeeld over 6 kinderen. Hoeveel knikkers krijgt elk kind?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 8 → Controleer. 6 × 8 = 48. Dat is te veel. · 6 → Controleer. 6 × 6 = 36. Dan blijft er over. · 36 → Verdelen is delen, niet aftrekken. Hoe vaak past de groep erin?
    - **Uitleg (Claude):** Denk aan de tafel van 6: 6 × ? = 42. 6 × 7 = 42, dus 42 : 6 = 7.

- **Hint 1 (te schrijven):** Verdeel eerlijk: iedereen krijgt evenveel. Hoeveel krijgt ieder?
- **Hint 2 (te schrijven):** Denk aan de keersom: hoeveel keer het aantal waarover je verdeelt, is het totaal?
- **Ouderzin:** Je kind verdeelt eerlijk (deelsom die precies uitkomt).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het aantal waarover je verdeelt` (fout = getal2) → Dat is het aantal waarover je verdeelt. De vraag is hoeveel ieder krijgt.  [nieuw]
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de getallen van elkaar afgehaald? Verdelen is een deelsom.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Er wordt eerlijk verdeeld: dat is een deelsom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom: dan kom je boven het totaal.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom: dan kom je onder het totaal.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op van het aantal waarover je verdeelt, tot je bij het totaal bent. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar
