# G3-GET-K05 — Eenvoudig erbij en eraf

Onze omschrijving: +/− context ≤12; splitsproblemen ≤10 (handelend) · in onze bank: 4 items

Claude-vragen gemapt: **144** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Er liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?

- Items: **36** · Claude-doelen: D1-2 (28), D1-6 (8) · regel: R14-context-som
- Getallenruimte: 0–10, 0–12 · type: kale
- Denkfouten (Claude): een-ernaast (62), verkeerde-bewerking (6), tiental-ernaast (4)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-K05-claude-bank-090` (Claude D1-2, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 2 appels. Er komen er 2 bij. Hoeveel appels liggen er nu?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-K05-claude-bank-099` (Claude D1-6, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 5 stiften. Er komen er 7 bij. Hoeveel stiften liggen er nu?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 14 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 2 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Welke plussom hoort bij het verhaal?
- **Hint 2 (te schrijven):** Begin bij het grootste getal. Zijn ze even groot? Begin dan bij het eerste. Tel de rest erbij, één voor één. Je mag je vingers gebruiken.
- **Ouderzin:** Je kind rekent een verhaal uit waarin er dingen bijkomen, tot 12.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = verschil van de getallen) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - (fout = antwoord − 10) → Je bent het tiental kwijt. Tel nog eens rustig verder.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Tel de rest nog eens één voor één erbij.  [nieuw]
- Status: hints klaar

## Somtype 2: Er liggen # [ding]. Er gaan er # weg. Hoeveel liggen er nu?

- Items: **36** · Claude-doelen: D1-3 (21), D3-3 (15) · regel: R14-context-som
- Getallenruimte: 0–10, 0–12 · type: kale
- Denkfouten (Claude): een-ernaast (57), verkeerde-bewerking (11), onthouden-vergeten (4)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-K05-claude-bank-042` (Claude D1-3, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 4 stenen. Er gaan er 2 weg. Hoeveel stenen liggen er nu?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-K05-claude-bank-062` (Claude D3-3, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 11 schelpen. Er gaan er 3 weg. Hoeveel schelpen liggen er nu?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 7 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 10 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus het worden er minder. Welke minsom hoort bij het verhaal?
- **Hint 2 (te schrijven):** Tel terug vanaf het eerste getal. Ga je voorbij de 10? Stop dan eerst bij 10. Haal daarna de rest eraf.
- **Ouderzin:** Je kind rekent een verhaal uit waarin er dingen weggaan, tot 12.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 + getal2) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `tien te veel` (fout = antwoord + 10) → Dat kan niet. Er gaan dingen weg. Dan worden het er minder. Tel nog eens terug vanaf het eerste getal.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Tel nog eens terug, één tegelijk.  [nieuw]
- Status: hints klaar

## Somtype 3: # [ding] over twee [plekken]; in de ene liggen er #. Hoeveel liggen er in de andere?

- Items: **30** · Claude-doelen: D1-1 (16), D1-0 (14) · regel: R10-splits-context
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): een-ernaast (22), None (18), getal-overgenomen (14), andere-deel-genomen (7)
- Verschillende Claude-fout-hints: 16 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-K05-claude-bank-006` (Claude D1-0, gegenereerd, niveau 1 → basis)
    - **Opgave:** 3 knopen liggen in het huis en de school. In het huis ligt er 1. Hoeveel liggen er in de school?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 3 → Niet alles ligt in de school. Een deel ligt al in het huis; hoeveel blijven er dan over? · 1 → Dat is het deel dat je al kent. Het andere deel is gevraagd.
    - **Uitleg (Claude):** 3 splits je in 1 en 2, want 1 + 2 = 3.
  - `G3-GET-K05-claude-bank-029` (Claude D1-1, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 7 kralen in twee dozen. In de voorste doos liggen er 3. Hoeveel liggen er in de achterste doos?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 6 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.

- **Hint 1 (te schrijven):** Het eerste getal is alles samen. Hoeveel er op de ene plek liggen, weet je al. Hoeveel blijven er dan over voor de andere?
- **Hint 2 (te schrijven):** Tel verder vanaf het getal dat je weet, tot je bij alles samen bent. Tel hoeveel stappen je zet. Je mag je vingers gebruiken.
- **Ouderzin:** Je kind zoekt het andere deel als alles samen en één deel bekend zijn (splitsen tot 10).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 (alles samen); tekst per item) → Niet alles ligt in [plek]. Een deel ligt al in [andere plek]; hoeveel blijven er dan over?  [Claude, ok]
  - (fout = getal2 (het deel dat je weet)) → Dat is het deel dat je al kent. Het andere deel is gevraagd.  [Claude, ok]
  - (fout ligt 1 naast het antwoord (twee teksten van Claude, allebei ok)) → Tel na: de twee delen moeten samen precies het hele getal zijn. / Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.  [Claude, ok]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen bij elkaar gedaan. Maar het eerste getal is al alles samen. Hoeveel moet er nog bij het deel dat je weet?  [nieuw]
  - `bijna` (fout ligt 2 naast het antwoord, of een andere fout) → Dat klopt nog niet. Tel verder vanaf het deel dat je weet, tot alles samen. Tel je stappen goed.  [nieuw]
- Status: hints klaar

## Somtype 4: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?

- Items: **22** · Claude-doelen: D1-5 (17), D3-4 (5) · regel: R14-context-som
- Getallenruimte: 0–10, 0–12 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (22), een-ernaast (22), kleinste-van-grootste (5)
- Verschillende Claude-fout-hints: 6 (meest: “Er gaan er weg, dus het worden er minder. Dit is een minsom.”)
- Voorbeelden:
  - `G3-GET-K05-claude-bank-116` (Claude D1-5, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het nest liggen 10 botten. Er gaan er 7 weg. Hoeveel botten blijven er over?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 17 → Er gaan er weg, dus het worden er minder. Dit is een minsom. · 2 → Tel nog eens terug, één tegelijk.
    - **Uitleg (Claude):** Er gaat weg, dus je trekt af: 10 − 7 = 3.
  - `G3-GET-K05-claude-bank-124` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de vallei liggen 11 blaadjes. Er gaan er 8 weg. Hoeveel blijven er over?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 19 → Er gaan er weg: dat is een minsom. · 4 → Ga eerst naar de 10 (11 − 1), en haal dan de rest eraf. · 7 → Je hebt de getallen omgedraaid. Begin bij het grote getal en tel terug.
    - **Uitleg (Claude):** Eerst naar de 10: 11 − 1 = 10. Dan de rest eraf: 10 − 7 = 3.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Welke minsom past bij het verhaal?
- **Hint 2 (te schrijven):** Tel terug vanaf het eerste getal. Ga je voorbij de 10? Stop dan eerst bij 10. Haal daarna de rest eraf.
- **Ouderzin:** Je kind rekent uit hoeveel er overblijven als er dingen weggaan, tot 12.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 + getal2 (twee teksten van Claude, allebei ok)) → Er gaan dingen weg, dus het worden er minder. Dit is een minsom. / Er gaan dingen weg. Dat is een minsom.  [Claude, taalfix]
  - (fout = antwoord − 1) → Tel nog eens terug, één tegelijk.  [Claude, ok]
  - (fout = antwoord + 1 (tekst per item, met de stap naar 10)) → Ga eerst naar de 10 (… − …), en haal dan de rest eraf.  [Claude, ok]
  - `cijfers omgedraaid` (fout = getal2 − de eenheden van getal1) → Je hebt de cijfers omgedraaid. Begin bij het hele eerste getal. Ga eerst terug naar 10 en haal dan de rest eraf.  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?

- Items: **20** · Claude-doelen: D1-5 (15), D3-4 (5) · regel: R14-context-som
- Getallenruimte: 0–10, 0–12 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (20), een-ernaast (20), tiental-ernaast (2)
- Verschillende Claude-fout-hints: 8 (meest: “Er komt bij, dus het worden er meer. Dit is een plussom.”)
- Voorbeelden:
  - `G3-GET-K05-claude-bank-136` (Claude D1-5, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het nest liggen 5 botten. Er komt er 1 bij. Hoeveel botten liggen er nu?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 4 → Er komt bij, dus het worden er meer. Dit is een plussom. · 7 → Tel nog eens na op je vingers.
    - **Uitleg (Claude):** Er komt bij, dus je telt op: 5 + 1 = 6.
  - `G3-GET-K05-claude-bank-143` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het moeras liggen 5 stappen. Er komen er 7 bij. Hoeveel zijn het er nu?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 2 → Er komt bij: dat is een plussom. · 11 → Ga eerst naar de 10 (5 + 5), en tel dan de rest erbij.
    - **Uitleg (Claude):** Eerst naar de 10: 5 + 5 = 10. Dan de rest erbij: 10 + 2 = 12.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Welke plussom past bij het verhaal?
- **Hint 2 (te schrijven):** Begin bij het grootste getal. Zijn ze even groot? Begin dan bij het eerste. Tel de rest erbij, één voor één. Je mag je vingers gebruiken.
- **Ouderzin:** Je kind rekent uit hoeveel het er samen zijn als er dingen bijkomen, tot 12.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = verschil van de getallen (twee teksten van Claude, allebei ok)) → Er komt iets bij, dus het worden er meer. Dit is een plussom. / Er komt iets bij. Dat is een plussom.  [Claude, taalfix]
  - (fout = antwoord + 1) → Tel nog eens na op je vingers.  [Claude, ok]
  - (fout = antwoord − 1 (tekst per item, met de stap naar 10)) → Ga eerst naar de 10 (… + …), en tel dan de rest erbij.  [Claude, ok]
  - (fout = antwoord − 10) → Je bent het tiental kwijt. Het antwoord is meer dan 10.  [Claude, ok]
- Status: hints klaar
