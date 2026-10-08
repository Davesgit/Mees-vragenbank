# G3-GET-K01 — Tellen tot twintig

Onze omschrijving: Telrij tot ≥20; verder/terug (terug <10) · in onze bank: 4 items

Claude-vragen gemapt: **48** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Tel de [ding]. #, #, #, □. Welk getal komt erna?

- Items: **11** · Claude-doelen: D0-1 (11) · regel: R04-telrij
- Getallenruimte: 0–10, 0–12 · type: invullen
- Denkfouten (Claude): een-ernaast (22), verkeerde-bewerking (11)
- Verschillende Claude-fout-hints: 3 (meest: “Dat getal staat er al. Tel nog één verder.”)
- Voorbeelden:
  - `G3-GET-K01-claude-bank-016` (Claude D0-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel de blaadjes. 5, 6, 7, □. Welk getal komt erna?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 7 → Dat getal staat er al. Tel nog één verder. · 9 → Je hebt er een overgeslagen. Tel één tegelijk. · 6 → De rij gaat omhoog. Welk getal komt ná het laatste?
    - **Uitleg (Claude):** Je telt steeds één verder. Na 7 komt 8.
  - `G3-GET-K01-claude-bank-013` (Claude D0-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tel de vissen. 9, 10, 11, □. Welk getal komt erna?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 11 → Dat getal staat er al. Tel nog één verder. · 13 → Je hebt er een overgeslagen. Tel één tegelijk. · 10 → De rij gaat omhoog. Welk getal komt ná het laatste?
    - **Uitleg (Claude):** Je telt steeds één verder. Na 11 komt 12.

- **Hint 1 (te schrijven):** De getallen gaan steeds één omhoog. Kijk naar het laatste getal.
- **Hint 2 (te schrijven):** Zeg de rij hardop. Tel daarna nog één stap verder. Dat getal komt in het hokje.
- **Ouderzin:** Je kind telt één verder in een telrij tot 12.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 2: Er liggen [ding] op een rij. #, □, #. Welk getal hoort in het midden?

- Items: **11** · Claude-doelen: D0-1 (11) · regel: R04-telrij
- Getallenruimte: 0–10, 0–12 · type: invullen
- Denkfouten (Claude): een-ernaast (11), verkeerde-bewerking (11)
- Verschillende Claude-fout-hints: 8 (meest: “De rij gaat omhoog. Welk getal komt na het eerste?”)
- Voorbeelden:
  - `G3-GET-K01-claude-bank-011` (Claude D0-1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Er liggen blaadjes op een rij. 4, □, 6. Welk getal hoort in het midden?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 7 → Het getal moet tussen 4 en 6 liggen. · 3 → De rij gaat omhoog. Welk getal komt na het eerste?
    - **Uitleg (Claude):** Tussen 4 en 6 zit 5.
  - `G3-GET-K01-claude-bank-003` (Claude D0-1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Er liggen poesjes op een rij. 10, □, 12. Welk getal hoort in het midden?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 13 → Het getal moet tussen 10 en 12 liggen. · 9 → De rij gaat omhoog. Welk getal komt na het eerste?
    - **Uitleg (Claude):** Tussen 10 en 12 zit 11.

- **Hint 1 (te schrijven):** Het hokje zit tussen twee getallen. Het getal moet daar precies tussen passen.
- **Hint 2 (te schrijven):** Begin bij het eerste getal en tel één verder. Tel daarna nog één verder. Kom je dan bij het laatste getal? Dan klopt het.
- **Ouderzin:** Je kind vult het ontbrekende getal in een telrij tot 12 in.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 3: Welk getal komt na #?

- Items: **9** · Claude-doelen: D2-1 (9) · regel: R01-buurgetal
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): tiental-ernaast (11), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G3-GET-K01-claude-bank-037` (Claude D2-1, bank, niveau 1 → basis)
    - **Opgave:** Welk getal komt na 17?
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** 28 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 27 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G3-GET-K01-claude-bank-040` (Claude D2-1, bank, niveau 1 → basis)
    - **Opgave:** Welk getal komt na 11?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 10 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 22 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Na betekent: één verder tellen.
- **Hint 2 (te schrijven):** Zeg het getal hardop en tel één stap verder. Op de getallenlijn ga je één streepje naar rechts.
- **Ouderzin:** Je kind noemt het getal dat na een getal tot 20 komt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `terug` (fout kleiner dan het getal in de vraag) → Je bent teruggegaan. Na betekent: één verder.  [nieuw]
  - `tien te ver` (fout = getal + 10 of antwoord + 10) → Dat is veel te ver. Na betekent: maar één stap verder.  [nieuw]
- Status: hints klaar

## Somtype 4: Welk getal hoort tussen # en #?

- Items: **9** · Claude-doelen: D2-2 (9) · regel: R02-tussen-buren
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): tiental-ernaast (8), verkeerde-bewerking (6), getal-overgenomen (4)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G3-GET-K01-claude-bank-024` (Claude D2-2, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal hoort tussen 10 en 12?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking. · 9 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-K01-claude-bank-026` (Claude D2-2, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal hoort tussen 15 en 17?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 15 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking. · 14 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Het goede getal ligt tussen de twee getallen in.
- **Hint 2 (te schrijven):** Begin bij het kleinste getal en tel één verder. Is het getal daarna het grootste getal? Dan heb je het goede getal.
- **Ouderzin:** Je kind zoekt het getal dat tussen twee getallen tot 20 ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Zoek het getal dat ertussen ligt.  [nieuw]
  - `ervoor` (fout kleiner dan het kleinste getal) → Dat getal komt vóór de twee getallen. Het goede getal ligt ertussen.  [nieuw]
  - `tien te ver` (fout = antwoord + 9 of + 10) → Dat is veel te ver. Het goede getal ligt tussen de twee getallen in.  [nieuw]
- Status: hints klaar

## Somtype 5: Welk getal komt vóór #?

- Items: **8** · Claude-doelen: D0-1 (8) · regel: R01-buurgetal
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), een-ernaast (8)
- Verschillende Claude-fout-hints: 6 (meest: “Je bent er twee teruggegaan. Ga precies één terug.”)
- Voorbeelden:
  - `G3-GET-K01-claude-bank-044` (Claude D0-1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welk getal komt vóór 8? Denk aan het tellen van de blaadjes.
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 9 → Vóór 8 betekent één minder, niet één meer. · 6 → Je bent er twee teruggegaan. Ga precies één terug.
    - **Uitleg (Claude):** Tel terug: vóór 8 komt 7.
  - `G3-GET-K01-claude-bank-048` (Claude D0-1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welk getal komt vóór 7? Denk aan het tellen van de wortels.
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 8 → Vóór 7 betekent één minder, niet één meer. · 5 → Je bent er twee teruggegaan. Ga precies één terug.
    - **Uitleg (Claude):** Tel terug: vóór 7 komt 6.

- **Hint 1 (te schrijven):** Vóór betekent: één terug tellen.
- **Hint 2 (te schrijven):** Zeg het getal hardop en tel één stap terug. Op de getallenlijn ga je één streepje naar links.
- **Ouderzin:** Je kind noemt het getal dat vóór een getal tot 10 komt.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
