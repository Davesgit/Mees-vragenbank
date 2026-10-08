# G3-GET-M06 — Slim rekenen tot twintig

Onze omschrijving: +/− tot 20 met strategieën (via 10, bijna dubbel, …) — opbouw · in onze bank: 8 items

Claude-vragen gemapt: **223** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + □ = #

- Items: **117** · Claude-doelen: D1-6 (72), D3-2 (45) · regel: R12-kale-som
- Getallenruimte: 0–12, 0–20 · type: invullen
- Denkfouten (Claude): een-ernaast (189), getal-overgenomen (34), verkeerde-bewerking (11)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-078` (Claude D1-6, bank, niveau 3 → toepassen)
    - **Opgave:** 18 + □ = 20
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 1 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M06-claude-bank-132` (Claude D3-2, bank, niveau 3 → toepassen)
    - **Opgave:** 9 + □ = 12
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 1 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Hoeveel moet er bij het eerste getal om bij het laatste getal te komen?
- **Hint 2 (te schrijven):** Tel verder vanaf het eerste getal tot het laatste getal. Ga je voorbij de 10? Spring dan eerst naar 10. Alle stappen samen komen in het hokje.
- **Ouderzin:** Je kind zoekt het ontbrekende getal in een plussom tot 20, soms met een sprong via 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Zoek hoeveel er nog bij het eerste getal moet om bij het laatste te komen.  [nieuw]
  - `overgenomen` (fout = getal2 (de uitkomst)) → Dat getal staat al na het isgelijkteken. Hoeveel moet er nog bij het eerste getal?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel nog eens verder vanaf het eerste getal, en tel je stappen goed.  [nieuw]
- Status: hints klaar

## Somtype 2: # − # =

- Items: **36** · Claude-doelen: D3-3 (36) · regel: R12-kale-som
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (53), onthouden-vergeten (13), verkeerde-bewerking (6)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-168` (Claude D3-3, bank, niveau 2 → toepassen)
    - **Opgave:** 14 − 9 =
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 7 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M06-claude-bank-165` (Claude D3-3, bank, niveau 2 → toepassen)
    - **Opgave:** 12 − 8 =
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 20 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 14 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.

- **Hint 1 (te schrijven):** Het is een minsom. Begin bij het eerste getal en haal het tweede eraf.
- **Hint 2 (te schrijven):** Kom je onder de 10? Haal er dan eerst zoveel af dat je op 10 uitkomt. Haal daarna de rest eraf.
- **Ouderzin:** Je kind oefent minsommen tot 20, via het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teken` (fout = getal1 + getal2) → Kijk goed naar het teken. Het is min: er gaat iets af.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is te veel. Bij min wordt het minder. Ga eerst terug naar 10 en haal dan de rest eraf.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Ga eerst terug naar 10. Haal dan de rest eraf.  [nieuw]
- Status: hints klaar

## Somtype 3: # + # =

- Items: **31** · Claude-doelen: D1-6 (31) · regel: R12-kale-som
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (55), tiental-ernaast (7)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-010` (Claude D1-6, bank, niveau 2 → toepassen)
    - **Opgave:** 5 + 6 =
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 12 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 13 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M06-claude-bank-020` (Claude D1-6, bank, niveau 2 → toepassen)
    - **Opgave:** 9 + 5 =
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 15 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Begin bij het grootste getal. Zijn ze even groot? Begin dan bij het eerste. Hoeveel komt erbij?
- **Hint 2 (te schrijven):** Vul het getal waar je begint eerst aan tot 10. Tel daarna de rest erbij.
- **Ouderzin:** Je kind oefent plussommen tot 20, via het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = antwoord − 10) → Je bent het tiental kwijt. Het antwoord is meer dan 10.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Vul eerst aan tot 10. Tel dan de rest erbij.  [nieuw]
- Status: hints klaar

## Somtype 4: # is # en □

- Items: **30** · Claude-doelen: D3-1 (30) · regel: D-splitsen (R09-splits-kaal), R09-splits-kaal
- Getallenruimte: 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (46), een-ernaast (14)
- Verschillende Claude-fout-hints: 2 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-216` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** 13 is 10 en □
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 5 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M06-claude-bank-205` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** 12 is 8 en □
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 12 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 8 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Het eerste getal is het hele getal. Eén deel staat er al. Welk deel hoort erbij?
- **Hint 2 (te schrijven):** Tel verder vanaf het deel dat er staat tot het hele getal. Of haal het deel dat er staat van het hele getal af.
- **Ouderzin:** Je kind oefent splitsingen tot 20 (het tweede deel zoeken).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `heel getal` (fout = getal1 (het hele getal)) → Dat is het hele getal. Welk deel hoort er nog bij?  [nieuw]
  - `deel` (fout = getal2 (het deel dat er staat)) → Dat deel staat er al. Zoek het andere deel.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Maar het eerste getal is al het hele getal. Hoeveel hoort er bij het deel dat er staat?  [nieuw]
  - (fout ligt 1 naast het antwoord) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `bijna` (fout ligt 2 naast het antwoord) → Bijna! Tel vanaf het deel dat er staat verder tot het hele getal.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. De twee delen samen moeten het hele getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 5: # is □ en #

- Items: **8** · Claude-doelen: D3-1 (8) · regel: R09-splits-kaal
- Getallenruimte: 0–12, 0–20 · type: invullen
- Denkfouten (Claude): None (8), een-ernaast (6)
- Verschillende Claude-fout-hints: 2 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-210` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** 12 is □ en 10
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 1 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M06-claude-bank-212` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** 16 is □ en 6
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 4 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Het eerste getal is het hele getal. Het tweede deel staat er al. Welk deel hoort er vooraan?
- **Hint 2 (te schrijven):** Leg het hele getal in gedachten met een tienstaaf en losse blokjes. Haal weg wat er al staat. Wat blijft er liggen?
- **Ouderzin:** Je kind splitst een getal tot 20 in een tiental en losse.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `heel getal` (fout = getal1 (het hele getal)) → Dat is het hele getal. Welk deel hoort er nog bij?  [nieuw]
  - `deel` (fout = getal2 (het deel dat er staat)) → Dat deel staat er al. Zoek het andere deel.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Maar het eerste getal is al het hele getal. Hoeveel hoort er bij het deel dat er staat?  [nieuw]
  - (fout ligt 1 naast het antwoord) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `bijna` (fout ligt 2 naast het antwoord) → Bijna! Tel vanaf het deel dat er staat verder tot het hele getal.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. De twee delen samen moeten het hele getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 6: Je denkt aan een getal. Als je er # bij doet, krijg je #. Aan welk getal denk je?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–12 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: getallenlijn of rekenrek tot 12 (Didactiek §4)
- Denkfouten (Claude): verkeerde-bewerking (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je moet terugrekenen, niet erbij doen. Begin bij 12 en ga terug.”)
- Voorbeelden:
  - `G3-GET-M06-claude-bank-223` (Claude W1, ai, niveau 1 → basis)
    - **Opgave:** Je denkt aan een getal. Als je er 5 bij doet, krijg je 12. Aan welk getal denk je?
    - **Opties:** A) 7 · B) 17 · C) 8
    - **Antwoord:** 7  (controle: n.v.t.)
    - **Fout-hints (Claude):** 17 → Je moet terugrekenen, niet erbij doen. Begin bij 12 en ga terug. · 8 → Controleer je antwoord: doe er 5 bij en kijk of je precies 12 krijgt.
    - **Uitleg (Claude):** Je rekent terug vanaf 12. Als je van 12 er 5 afhaalt, houd je 7 over. En 7 plus 5 is inderdaad 12.

- **Hint 1 (te schrijven):** Er kwam iets bij, en toen kreeg je een nieuw getal. Welk getal had je vóórdat er iets bij kwam?
- **Hint 2 (te schrijven):** Begin bij het getal dat je kreeg. Tel terug, zoveel als erbij kwam. Ga je voorbij de 10? Stop dan eerst bij 10.
- **Ouderzin:** Je kind rekent terug: welk getal had je, als je er iets bij hebt gedaan?
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (17) → Je moet terugrekenen, niet erbij doen. Begin bij 12 en ga terug.  [Claude, ok]
  - (8) → Kijk of het klopt: doe er 5 bij. Krijg je dan precies 12?  [Claude, taalfix]
- Status: hints klaar
