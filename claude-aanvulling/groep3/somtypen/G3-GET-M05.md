# G3-GET-M05 — Sommetjes tot 10 uit het hoofd

Onze omschrijving: Splitsingen/+/− tot 10 uit het hoofd (memoriseren) · in onze bank: 8 items

Claude-vragen gemapt: **124** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + # =

- Items: **28** · Claude-doelen: D1-2 (28) · regel: R12-kale-som
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): een-ernaast (50), verkeerde-bewerking (6)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-004` (Claude D1-2, bank, niveau 2 → toepassen)
    - **Opgave:** 2 + 2 =
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M05-claude-bank-025` (Claude D1-2, bank, niveau 2 → toepassen)
    - **Opgave:** 4 + 3 =
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 8 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Begin bij het grootste getal. Zijn ze even groot? Begin dan bij het eerste. Hoeveel komt erbij?
- **Hint 2 (te schrijven):** Tel vanaf het grootste getal verder, zoveel stappen als het andere getal. Je kunt ook de vingers voor allebei de getallen opsteken en ze samen tellen.
- **Ouderzin:** Je kind oefent plussommen tot 10 uit het hoofd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teken` (fout = verschil van de getallen) → Kijk goed naar het teken. Het is plus: er komt iets bij.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Tel nog eens verder, één voor één.  [nieuw]
- Status: hints klaar

## Somtype 2: # + □ = #

- Items: **28** · Claude-doelen: D3-2 (12), D1-2 (9), D1-6 (7) · regel: R12-kale-som
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): een-ernaast (41), verkeerde-bewerking (10), getal-overgenomen (5)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-035` (Claude D1-2, bank, niveau 3 → toepassen)
    - **Opgave:** 2 + □ = 4
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 6 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-M05-claude-bank-042` (Claude D1-6, bank, niveau 3 → toepassen)
    - **Opgave:** 8 + □ = 10
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 18 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Hoeveel moet er bij het eerste getal om bij het laatste getal te komen?
- **Hint 2 (te schrijven):** Tel verder vanaf het eerste getal tot het laatste getal. Tel hoeveel stappen je zet. Dat aantal komt in het hokje.
- **Ouderzin:** Je kind zoekt het ontbrekende getal in een plussom tot 10.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Zoek hoeveel er nog bij het eerste getal moet om bij het laatste te komen.  [nieuw]
  - `overgenomen` (fout = getal2 (de uitkomst)) → Dat getal staat al na het isgelijkteken. Hoeveel moet er nog bij het eerste getal?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel nog eens verder vanaf het eerste getal, en tel je stappen goed.  [nieuw]
- Status: hints klaar

## Somtype 3: # − # =

- Items: **21** · Claude-doelen: D1-3 (21) · regel: R12-kale-som
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): een-ernaast (34), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-067` (Claude D1-3, bank, niveau 2 → toepassen)
    - **Opgave:** 4 − 2 =
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-M05-claude-bank-062` (Claude D1-3, bank, niveau 2 → toepassen)
    - **Opgave:** 8 − 3 =
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 11 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Het is een minsom. Begin bij het eerste getal en haal het tweede eraf.
- **Hint 2 (te schrijven):** Tel terug vanaf het eerste getal, zoveel stappen als het tweede getal. Of denk aan een plussom: welk getal en het tweede getal maken samen het eerste?
- **Ouderzin:** Je kind oefent minsommen tot 10 uit het hoofd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teken` (fout = getal1 + getal2) → Kijk goed naar het teken. Het is min: er gaat iets af.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Tel nog eens terug, één tegelijk.  [nieuw]
- Status: hints klaar

## Somtype 4: # is # en □

- Items: **19** · Claude-doelen: D1-1 (18), D1-0 (1) · regel: R09-splits-kaal
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): None (28), een-ernaast (10)
- Verschillende Claude-fout-hints: 2 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-078` (Claude D1-0, bank, niveau 2 → toepassen)
    - **Opgave:** 5 is 1 en □
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M05-claude-bank-093` (Claude D1-1, bank, niveau 2 → toepassen)
    - **Opgave:** 9 is 6 en □
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 9 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 5 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Het eerste getal is het hele getal. Eén deel staat er al. Welk deel hoort erbij?
- **Hint 2 (te schrijven):** Tel verder vanaf het deel dat er staat tot het hele getal. Tel hoeveel stappen je zet. Je kunt ook je vingers gebruiken.
- **Ouderzin:** Je kind oefent splitsingen tot 10 (het tweede deel zoeken).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `heel getal` (fout = getal1 (het hele getal)) → Dat is het hele getal. Welk deel hoort er nog bij?  [nieuw]
  - `deel` (fout = getal2 (het deel dat er staat)) → Dat deel staat er al. Zoek het andere deel.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Maar het eerste getal is al het hele getal. Hoeveel hoort er bij het deel dat er staat?  [nieuw]
  - (fout ligt 1 naast het antwoord) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `bijna` (fout ligt 2 naast het antwoord) → Bijna! Tel vanaf het deel dat er staat verder tot het hele getal.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. De twee delen samen moeten het hele getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 5: # is □ en #

- Items: **19** · Claude-doelen: D1-1 (18), D1-0 (1) · regel: R09-splits-kaal
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): None (23), een-ernaast (15)
- Verschillende Claude-fout-hints: 2 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-097` (Claude D1-0, bank, niveau 2 → toepassen)
    - **Opgave:** 5 is □ en 1
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-M05-claude-bank-100` (Claude D1-1, bank, niveau 2 → toepassen)
    - **Opgave:** 9 is □ en 6
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Het eerste getal is het hele getal. Het tweede deel staat er al. Welk deel hoort er vooraan?
- **Hint 2 (te schrijven):** Tel verder vanaf het deel dat er staat tot het hele getal. Tel hoeveel stappen je zet. Je kunt ook je vingers gebruiken.
- **Ouderzin:** Je kind oefent splitsingen tot 10 (het eerste deel zoeken).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `heel getal` (fout = getal1 (het hele getal)) → Dat is het hele getal. Welk deel hoort er nog bij?  [nieuw]
  - `deel` (fout = getal2 (het deel dat er staat)) → Dat deel staat er al. Zoek het andere deel.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Maar het eerste getal is al het hele getal. Hoeveel hoort er bij het deel dat er staat?  [nieuw]
  - (fout ligt 1 naast het antwoord) → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `bijna` (fout ligt 2 naast het antwoord) → Bijna! Tel vanaf het deel dat er staat verder tot het hele getal.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. De twee delen samen moeten het hele getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 6: Splits #. # is # en □.

- Items: **8** · Claude-doelen: D1-0 (8) · regel: R09-splits-kaal
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), een-ernaast (8)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt op, maar je moet splitsen: de twee delen samen zijn het hele getal.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-122` (Claude D1-0, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Splits 3. 3 is 1 en □.
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je telt op, maar je moet splitsen: de twee delen samen zijn het hele getal. · 1 → Tel na: het bekende deel en jouw getal moeten samen het hele getal zijn.
    - **Uitleg (Claude):** 1 + 2 = 3, dus 3 is 1 en 2.
  - `G3-GET-M05-claude-bank-119` (Claude D1-0, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Splits 4. 4 is 1 en □.
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je telt op, maar je moet splitsen: de twee delen samen zijn het hele getal. · 2 → Tel na: het bekende deel en jouw getal moeten samen het hele getal zijn.
    - **Uitleg (Claude):** 1 + 3 = 4, dus 4 is 1 en 3.

- **Hint 1 (te schrijven):** Splitsen is: het getal in twee delen verdelen. Eén deel weet je al.
- **Hint 2 (te schrijven):** Tel verder vanaf het deel dat je weet tot het hele getal. Het aantal stappen is het andere deel.
- **Ouderzin:** Je kind splitst een getal tot 10 in twee delen.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 7: Twee getallen. Samen #. Het ene is # meer. Welke twee getallen zijn het?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: twee rijtjes kralen (Didactiek §4)
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Het verschil tussen die twee is te groot. Zoek getallen die dichter bij elkaar liggen.”)
- Voorbeelden:
  - `G3-GET-M05-claude-bank-124` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** Twee getallen. Samen 10. Het ene is 2 meer. Welke twee getallen zijn het?
    - **Opties:** A) 8 en 2 · B) 7 en 3 · C) 6 en 4
    - **Antwoord:** 6 en 4  (controle: n.v.t.)
    - **Fout-hints (Claude):** 8 en 2 → Het verschil tussen die twee is te groot. Zoek getallen die dichter bij elkaar liggen. · 7 en 3 → Samen klopt het wel, maar kijk nog eens hoeveel het ene getal groter is.
    - **Uitleg (Claude):** Probeer paren die samen 10 zijn: 5 en 5, 6 en 4, 7 en 3. Bij 6 en 4 is het verschil precies 2. Dus dat is het goede paar.

- **Hint 1 (te schrijven):** Kijk bij elk antwoord: maken de twee getallen samen het getal dat na 'Samen' staat?
- **Hint 2 (te schrijven):** Kijk dan hoeveel het ene getal meer is dan het andere. Tel van het kleine getal naar het grote getal.
- **Ouderzin:** Je kind zoekt twee getallen die samen een getal maken en een bepaald aantal verschillen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (8 en 2) → Die twee getallen liggen te ver uit elkaar. Zoek getallen die dichter bij elkaar liggen.  [Claude, taalfix]
  - (7 en 3) → Samen klopt het wel, maar kijk nog eens hoeveel het ene getal groter is.  [Claude, ok]
- Status: hints klaar
