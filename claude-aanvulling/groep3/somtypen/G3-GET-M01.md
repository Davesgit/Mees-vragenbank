# G3-GET-M01 — Tellen tot honderd

Onze omschrijving: Telrij tot ≥100; verder/terug vanaf elk getal · in onze bank: 8 items

Claude-vragen gemapt: **256** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Welk getal komt vóór #?

- Items: **81** · Claude-doelen: D2-1 (79), D0-1 (2) · regel: R01-buurgetal
- Getallenruimte: 0–100, 0–12, 0–20, 0–30 · type: kale
- Denkfouten (Claude): tiental-ernaast (112), verkeerde-bewerking (48), een-ernaast (2)
- Verschillende Claude-fout-hints: 5 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-152` (Claude D0-1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welk getal komt vóór 11? Denk aan het tellen van de botten.
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 12 → Vóór 11 betekent één minder, niet één meer. · 9 → Je bent er twee teruggegaan. Ga precies één terug.
    - **Uitleg (Claude):** Tel terug: vóór 11 komt 10.
  - `G3-GET-M01-claude-bank-183` (Claude D2-1, bank, niveau 1 → basis)
    - **Opgave:** Welk getal komt vóór 59?
    - **Antwoord:** 58  (controle: ok)
    - **Fout-hints (Claude):** 48 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 49 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Vóór betekent: één terug tellen.
- **Hint 2 (te schrijven):** Zeg het getal hardop en tel één stap terug. Eindigt het getal op een 0? Dan eindigt het getal ervoor op een 9.
- **Ouderzin:** Je kind noemt het getal dat vóór een getal tot 100 komt.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien te ver` (fout = getal − 10 of antwoord − 10) → Dat is veel te ver terug. Vóór betekent: maar één stap terug.  [nieuw]
  - `verder` (fout = getal + 1) → Je bent verder geteld. Vóór betekent: één terug.  [nieuw]
  - (fout = getal + 1 (alleen bij 2 items; tekst per item)) → Vóór … betekent één minder, niet één meer.  [Claude, ok]
  - (fout = antwoord − 1) → Je bent er twee teruggegaan. Ga precies één terug.  [Claude, ok]
- Status: hints klaar

## Somtype 2: Welk getal hoort tussen # en #?

- Items: **79** · Claude-doelen: D2-2 (79) · regel: R02-tussen-buren
- Getallenruimte: 0–100, 0–30 · type: kale
- Denkfouten (Claude): tiental-ernaast (76), getal-overgenomen (43), verkeerde-bewerking (39)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-061` (Claude D2-2, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal hoort tussen 42 en 44?
    - **Antwoord:** 43  (controle: ok)
    - **Fout-hints (Claude):** 53 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 52 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G3-GET-M01-claude-bank-065` (Claude D2-2, bank, niveau 2 → toepassen)
    - **Opgave:** Welk getal hoort tussen 28 en 30?
    - **Antwoord:** 29  (controle: ok)
    - **Fout-hints (Claude):** 28 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking. · 39 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Het goede getal ligt tussen de twee getallen in.
- **Hint 2 (te schrijven):** Begin bij het kleinste getal en tel één verder. Is het getal daarna het grootste getal? Dan heb je het goede getal. Eindigt het kleinste getal op een 9? Dan eindigt het getal ertussen op een 0.
- **Ouderzin:** Je kind zoekt het getal dat tussen twee getallen tot 100 ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Zoek het getal dat ertussen ligt.  [nieuw]
  - `ervoor` (fout kleiner dan het kleinste getal) → Dat getal komt vóór de twee getallen. Het goede getal ligt ertussen.  [nieuw]
  - `tien te ver` (fout = antwoord + 9 of + 10) → Dat is veel te ver. Het goede getal ligt tussen de twee getallen in.  [nieuw]
- Status: hints klaar

## Somtype 3: Welk getal komt na #?

- Items: **72** · Claude-doelen: D2-1 (72) · regel: R01-buurgetal
- Getallenruimte: 0–100, 0–30 · type: kale
- Denkfouten (Claude): tiental-ernaast (109), verkeerde-bewerking (35)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-113` (Claude D2-1, bank, niveau 1 → basis)
    - **Opgave:** Welk getal komt na 21?
    - **Antwoord:** 22  (controle: ok)
    - **Fout-hints (Claude):** 32 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 31 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G3-GET-M01-claude-bank-082` (Claude D2-1, bank, niveau 1 → basis)
    - **Opgave:** Welk getal komt na 65?
    - **Antwoord:** 66  (controle: ok)
    - **Fout-hints (Claude):** 76 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 75 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Na betekent: één verder tellen.
- **Hint 2 (te schrijven):** Zeg het getal hardop en tel één stap verder. Eindigt het getal op een 9? Dan eindigt het getal erna op een 0.
- **Ouderzin:** Je kind noemt het getal dat na een getal tot 100 komt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `terug` (fout kleiner dan het getal in de vraag) → Je bent teruggegaan. Na betekent: één verder.  [nieuw]
  - `tien te ver` (fout = getal + 10 of antwoord + 10) → Dat is veel te ver. Na betekent: maar één stap verder.  [nieuw]
- Status: hints klaar

## Somtype 4: Tel met sprongen van #. #, #, #, □, #

- Items: **6** · Claude-doelen: D0-3 (6) · regel: D-sprongen (R05-sprongen)
- Getallenruimte: 0–10, 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-248` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 6, 8, 10, □, 14
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 8 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 14 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M01-claude-bank-249` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 4, 6, 8, □, 12
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 8 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 12 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Zeg de getallen van de rij hardop. Hoe ver spring je steeds?
- **Hint 2 (te schrijven):** Kijk naar het getal vóór de lege plek. Spring één keer net zo ver. Klopt het getal ná de lege plek dan ook?
- **Ouderzin:** Je kind vult een getal in een rij met sprongen van 2 tot 20 in.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort tussen het getal vóór en het getal ná de lege plek?  [nieuw]
  - `sprong van 1` (fout ligt 1 naast het antwoord) → Bijna! Kijk hoe ver je steeds springt, en spring precies zo ver.  [nieuw]
  - `andere fout` (andere fout) → Tel hardop mee met de sprongen, vanaf het eerste getal. Welk getal hoort op de lege plek?  [nieuw]
- Status: hints klaar

## Somtype 5: Tel met sprongen van #. #, #, #, #, □

- Items: **6** · Claude-doelen: D0-3 (6) · regel: D-sprongen (R05-sprongen)
- Getallenruimte: 0–10, 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-238` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 6, 8, 10, 12, □
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 16 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M01-claude-bank-236` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 4, 6, 8, 10, □
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 14 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 8 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Zeg de getallen van de rij hardop. Hoe ver spring je steeds?
- **Hint 2 (te schrijven):** Begin bij het laatste getal van de rij. Spring nog één keer net zo ver. Dat getal hoort op de lege plek.
- **Ouderzin:** Je kind telt verder met sprongen van 2 tot 20.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Spring vanaf het laatste getal nog één sprong verder.  [nieuw]
  - `sprong van 1` (fout ligt 1 naast het antwoord) → Bijna! Kijk hoe ver je steeds springt, en spring precies zo ver.  [nieuw]
  - `sprong te veel` (fout = antwoord + 2 of meer) → Je bent te ver gesprongen. Spring vanaf het laatste getal maar één keer.  [nieuw]
  - `andere fout` (andere fout) → Tel hardop mee met de sprongen, vanaf het eerste getal. Welk getal komt er daarna?  [nieuw]
- Status: hints klaar

## Somtype 6: Tel met sprongen van #. #, □, #, #, #

- Items: **6** · Claude-doelen: D0-3 (6) · regel: D-sprongen (R05-sprongen)
- Getallenruimte: 0–10, 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-259` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 8, □, 12, 14, 16
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 9 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 8 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M01-claude-bank-262` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 2, □, 6, 8, 10
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 6 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Zeg de getallen van de rij hardop. Hoe ver spring je steeds?
- **Hint 2 (te schrijven):** Kijk naar het getal vóór de lege plek. Spring één keer net zo ver. Klopt het getal ná de lege plek dan ook?
- **Ouderzin:** Je kind vult een getal in een rij met sprongen van 2 tot 20 in.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort tussen het getal vóór en het getal ná de lege plek?  [nieuw]
  - `sprong van 1` (fout ligt 1 naast het antwoord) → Bijna! Kijk hoe ver je steeds springt, en spring precies zo ver.  [nieuw]
  - `andere fout` (andere fout) → Tel hardop mee met de sprongen, vanaf het eerste getal. Welk getal hoort op de lege plek?  [nieuw]
- Status: hints klaar

## Somtype 7: Tel met sprongen van #. #, #, □, #, #

- Items: **6** · Claude-doelen: D0-3 (6) · regel: D-sprongen (R05-sprongen)
- Getallenruimte: 0–10, 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M01-claude-bank-252` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 8, 10, □, 14, 16
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 16 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M01-claude-bank-253` (Claude D0-3, bank, niveau 2 → toepassen)
    - **Opgave:** Tel met sprongen van 2. 4, 6, □, 10, 12
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 12 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Zeg de getallen van de rij hardop. Hoe ver spring je steeds?
- **Hint 2 (te schrijven):** Kijk naar het getal vóór de lege plek. Spring één keer net zo ver. Klopt het getal ná de lege plek dan ook?
- **Ouderzin:** Je kind vult een getal in een rij met sprongen van 2 tot 20 in.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `overgenomen` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Welk getal hoort tussen het getal vóór en het getal ná de lege plek?  [nieuw]
  - `sprong van 1` (fout ligt 1 naast het antwoord) → Bijna! Kijk hoe ver je steeds springt, en spring precies zo ver.  [nieuw]
  - `andere fout` (andere fout) → Tel hardop mee met de sprongen, vanaf het eerste getal. Welk getal hoort op de lege plek?  [nieuw]
- Status: hints klaar
