# G3-GET-E04 — Verhaaltjes worden sommen

Onze omschrijving: Formele +/− ↔ context ≤20 · in onze bank: 8 items

Claude-vragen gemapt: **211** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?

- Items: **63** · Claude-doelen: T9 (63) · regel: R13-welke-som
- Getallenruimte: 0–10, 0–12, 0–20 · type: meerkeuze
- Denkfouten (Claude): kleinste-van-grootste (63), verkeerde-bewerking (63)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-119` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de doos liggen 3 ballen. Er gaan er 2 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 3 + 2 · B) 2 − 3 · C) 3 − 2
    - **Antwoord:** 3 − 2  (controle: ok)
    - **Fout-hints (Claude):** 2 − 3 → Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom. · 3 + 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-E04-claude-bank-066` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de trommel liggen 11 knikkers. Er gaan er 2 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 11 + 2 · B) 2 − 11 · C) 11 − 2
    - **Antwoord:** 11 − 2  (controle: ok)
    - **Fout-hints (Claude):** 2 − 11 → Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom. · 11 + 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er gaan dingen uit, dus het worden er minder. Dat is een minsom. Zoek de som die begint bij het getal dat er eerst in lag.
- **Ouderzin:** Je kind kiest de minsom die past bij een verhaal waarin er dingen uitgaan.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (de minsom omgedraaid (klein getal min groot getal)) → Die som begint bij het verkeerde getal. Begin bij wat er eerst in lag. Daar gaan er een paar af.  [nieuw]
  - (de plussom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?

- Items: **63** · Claude-doelen: T9 (63) · regel: R13-welke-som
- Getallenruimte: 0–10, 0–12, 0–20 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (63), verkeerd-getal (63)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-205` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de doos liggen 3 ballen. Er komen er 2 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 3 + 3 · B) 3 − 2 · C) 3 + 2
    - **Antwoord:** 3 + 2  (controle: ok)
    - **Fout-hints (Claude):** 3 − 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-E04-claude-bank-191` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de trommel liggen 15 koekjes. Er komen er 4 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 15 − 4 · B) 15 + 4 · C) 15 + 5
    - **Antwoord:** 15 + 4  (controle: ok)
    - **Fout-hints (Claude):** 15 − 4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er komen dingen bij, dus het worden er meer. Dat is een plussom. Zoek de som met het getal dat er al lag en het getal dat erbij komt.
- **Ouderzin:** Je kind kiest de plussom die past bij een verhaal waarin er dingen bijkomen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (de minsom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `plussom, ander getal` (de plussom (merge-afleider a + (b+1); 1 okt)) → Dat is wel een plussom. Maar één getal klopt niet. Hoeveel lagen er al? En hoeveel komen erbij?  [nieuw]
  - (de keersom) → Die som past niet bij het verhaal. Er komen dingen bij. Dat is plus.  [nieuw]
- Status: hints klaar

## Somtype 3: # [ding] over twee [plekken]; in de ene liggen er #. Hoeveel liggen er in de andere?

- Items: **23** · Claude-doelen: D3-1 (23) · regel: R10-splits-context
- Getallenruimte: 0–12, 0–20 · type: kale
- Denkfouten (Claude): None (35), een-ernaast (11)
- Verschillende Claude-fout-hints: 2 (meest: “Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-009` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 12 kaarten in twee dozen. In de voorste doos liggen er 3. Hoeveel liggen er in de achterste doos?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 12 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 11 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap.
  - `G3-GET-E04-claude-bank-002` (Claude D3-1, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 14 appels in twee zakken. In de groene zak liggen er 6. Hoeveel liggen er in de gele zak?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 14 → Dat klopt nog niet. Lees de som nog eens rustig en probeer het stap voor stap. · 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Het eerste getal is alles samen. Hoeveel er in de ene liggen, weet je al. Hoeveel blijven er dan over voor de andere?
- **Hint 2 (te schrijven):** Tel verder vanaf het getal dat je weet, tot je bij alles samen bent. Tel hoeveel stappen je zet. Je kunt ook rekenen: alles samen min het getal dat je weet.
- **Ouderzin:** Je kind zoekt het andere deel als alles samen en één deel bekend zijn (splitsen tot 20).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `totaal` (fout = getal1 (alles samen)) → Dat zijn ze allemaal samen. Hoeveel liggen er alleen in de andere?  [nieuw]
  - `deel` (fout = getal2 (het deel dat je weet)) → Zoveel liggen er in de ene. De vraag gaat over de andere.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen bij elkaar gedaan. Maar het eerste getal is al alles samen. Hoeveel moet er nog bij het deel dat je weet?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel nog eens precies verder vanaf het getal dat je weet, tot alles samen.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. Het eerste getal is alles samen. Haal het getal dat je weet eraf.  [nieuw]
- Status: hints klaar

## Somtype 4: Er liggen # [ding]. Er gaan er # weg. Hoeveel liggen er nu?

- Items: **21** · Claude-doelen: D3-3 (21) · regel: R14-context-som
- Getallenruimte: 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (35), onthouden-vergeten (5), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-024` (Claude D3-3, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 15 stenen. Er gaan er 9 weg. Hoeveel stenen liggen er nu?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 8 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-E04-claude-bank-038` (Claude D3-3, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 14 blokjes. Er gaan er 6 weg. Hoeveel blokjes liggen er nu?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus het worden er minder. Welke minsom hoort bij het verhaal?
- **Hint 2 (te schrijven):** Begin bij het eerste getal. Haal er eerst zoveel af dat je op 10 uitkomt. Haal daarna de rest eraf.
- **Ouderzin:** Je kind rekent een verhaal uit waarin er dingen weggaan, tot 20 en over de 10.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 + getal2) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `tien te veel` (fout = antwoord + 10) → Dat kan niet. Er gaan dingen weg. Dan worden het er minder. Ga eerst terug naar 10 en haal dan de rest eraf.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Ga eerst terug naar 10. Haal dan de rest eraf.  [nieuw]
  - `overig` (andere fout) → Dat klopt nog niet. Begin bij het eerste getal. Haal het tweede getal eraf, via 10.  [nieuw]
- Status: hints klaar

## Somtype 5: Er liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?

- Items: **19** · Claude-doelen: D1-6 (19) · regel: R14-context-som
- Getallenruimte: 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (34), tiental-ernaast (3), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-058` (Claude D1-6, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 5 stenen. Er komen er 8 bij. Hoeveel stenen liggen er nu?
    - **Antwoord:** 13  (controle: ok)
    - **Fout-hints (Claude):** 14 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 15 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G3-GET-E04-claude-bank-059` (Claude D1-6, bank, niveau 2 → toepassen)
    - **Opgave:** Er liggen 7 appels. Er komen er 8 bij. Hoeveel appels liggen er nu?
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 17 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Welke plussom hoort bij het verhaal?
- **Hint 2 (te schrijven):** Begin bij het grootste getal. Zijn ze even groot? Begin dan bij het eerste. Vul eerst aan tot 10. Doe daarna de rest erbij.
- **Ouderzin:** Je kind rekent een verhaal uit waarin er dingen bijkomen, tot 20 en over de 10.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 − getal2 of getal2 − getal1) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - (fout = antwoord − 10) → Je bent het tiental kwijt. Het antwoord is meer dan 10.  [Claude, taalfix]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Je zit er net naast. Vul eerst aan tot 10. Tel dan de rest erbij.  [nieuw]
- Status: hints klaar

## Somtype 6: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?

- Items: **11** · Claude-doelen: D3-4 (11) · regel: R14-context-som
- Getallenruimte: 0–20 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (11), een-ernaast (11), kleinste-van-grootste (11)
- Verschillende Claude-fout-hints: 7 (meest: “Er gaan er weg: dat is een minsom.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-135` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de vallei liggen 16 stappen. Er gaan er 9 weg. Hoeveel blijven er over?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 25 → Er gaan er weg: dat is een minsom. · 8 → Ga eerst naar de 10 (16 − 6), en haal dan de rest eraf. · 3 → Je hebt de getallen omgedraaid. Begin bij het grote getal en tel terug.
    - **Uitleg (Claude):** Eerst naar de 10: 16 − 6 = 10. Dan de rest eraf: 10 − 3 = 7.
  - `G3-GET-E04-claude-bank-136` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de schuur liggen 18 noten. Er gaan er 9 weg. Hoeveel blijven er over?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 27 → Er gaan er weg: dat is een minsom. · 10 → Ga eerst naar de 10 (18 − 8), en haal dan de rest eraf. · 1 → Je hebt de getallen omgedraaid. Begin bij het grote getal en tel terug.
    - **Uitleg (Claude):** Eerst naar de 10: 18 − 8 = 10. Dan de rest eraf: 10 − 1 = 9.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Welke minsom past bij het verhaal?
- **Hint 2 (te schrijven):** Begin bij het eerste getal. Ga eerst terug naar 10. Haal daarna de rest eraf.
- **Ouderzin:** Je kind rekent uit hoeveel er overblijven als er dingen weggaan, tot 20 en over de 10.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = getal1 + getal2) → Er gaan dingen weg. Dat is een minsom.  [Claude, taalfix]
  - (fout = antwoord + 1 (tekst per item, met de stap naar 10)) → Ga eerst naar de 10 (… − …), en haal dan de rest eraf.  [Claude, ok]
  - `cijfers omgedraaid` (fout = getal2 − de eenheden van getal1) → Je hebt de cijfers omgedraaid. Begin bij het hele eerste getal. Ga eerst terug naar 10 en haal dan de rest eraf.  [nieuw]
- Status: hints klaar

## Somtype 7: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?

- Items: **11** · Claude-doelen: D3-4 (11) · regel: R14-context-som
- Getallenruimte: 0–20 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (11), een-ernaast (11), tiental-ernaast (7)
- Verschillende Claude-fout-hints: 7 (meest: “Er komt bij: dat is een plussom.”)
- Voorbeelden:
  - `G3-GET-E04-claude-bank-141` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het museum liggen 5 stappen. Er komen er 9 bij. Hoeveel zijn het er nu?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 4 → Er komt bij: dat is een plussom. · 13 → Ga eerst naar de 10 (5 + 5), en tel dan de rest erbij.
    - **Uitleg (Claude):** Eerst naar de 10: 5 + 5 = 10. Dan de rest erbij: 10 + 4 = 14.
  - `G3-GET-E04-claude-bank-144` (Claude D3-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de schuur liggen 9 wortels. Er komen er 5 bij. Hoeveel zijn het er nu?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 4 → Er komt bij: dat is een plussom. · 13 → Ga eerst naar de 10 (9 + 1), en tel dan de rest erbij.
    - **Uitleg (Claude):** Eerst naar de 10: 9 + 1 = 10. Dan de rest erbij: 10 + 4 = 14.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Welke plussom past bij het verhaal?
- **Hint 2 (te schrijven):** Vul het eerste getal eerst aan tot 10. Tel daarna de rest erbij.
- **Ouderzin:** Je kind rekent uit hoeveel het er samen zijn als er dingen bijkomen, tot 20 en over de 10.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = verschil van de getallen) → Er komt iets bij. Dat is een plussom.  [Claude, taalfix]
  - (fout = antwoord − 1 (tekst per item, met de stap naar 10)) → Ga eerst naar de 10 (… + …), en tel dan de rest erbij.  [Claude, ok]
  - (fout = antwoord − 10) → Je bent het tiental kwijt. Het antwoord is meer dan 10.  [Claude, ok]
- Status: hints klaar
