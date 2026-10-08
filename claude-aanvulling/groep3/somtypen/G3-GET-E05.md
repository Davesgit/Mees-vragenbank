# G3-GET-E05 — Rekenen net over twintig

Onze omschrijving: +/− tot ≥20 met inzicht + uitleg strategie (wave 1: getallenruimte 0–30; geen tientallige splitsing tot 100) · in onze bank: 8 items

Claude-vragen gemapt: **28** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?

- Items: **14** · Claude-doelen: T9 (14) · regel: R13-welke-som
- Getallenruimte: 0–30 · type: meerkeuze
- Denkfouten (Claude): kleinste-van-grootste (14), verkeerde-bewerking (14)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom.”)
- Voorbeelden:
  - `G3-GET-E05-claude-bank-003` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de kist liggen 25 ballen. Er gaan er 2 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 25 + 2 · B) 2 − 25 · C) 25 − 2
    - **Antwoord:** 25 − 2  (controle: ok)
    - **Fout-hints (Claude):** 2 − 25 → Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom. · 25 + 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-E05-claude-bank-007` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de kist liggen 23 appels. Er gaan er 9 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 9 − 23 · B) 23 + 9 · C) 23 − 9
    - **Antwoord:** 23 − 9  (controle: ok)
    - **Fout-hints (Claude):** 9 − 23 → Kijk goed welk cijfer boven staat en welk onder. Je haalt het onderste van het bovenste af, niet andersom. · 23 + 9 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er gaan dingen uit, dus het worden er minder. Dat is een minsom. Zoek de som die begint bij het getal dat er eerst in lag.
- **Ouderzin:** Je kind kiest de minsom die past bij een verhaal tot 30 waarin er dingen uitgaan.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (de minsom omgedraaid (klein getal min groot getal)) → Die som begint bij het verkeerde getal. Begin bij wat er eerst in lag. Daar gaan er een paar af.  [nieuw]
  - (de plussom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?

- Items: **14** · Claude-doelen: T9 (14) · regel: R13-welke-som
- Getallenruimte: 0–30 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (14), verkeerd-getal (14)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G3-GET-E05-claude-bank-017` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de kist liggen 25 ballen. Er komen er 2 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 25 + 2 · B) 25 + 3 · C) 25 − 2
    - **Antwoord:** 25 + 2  (controle: ok)
    - **Fout-hints (Claude):** 25 − 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G3-GET-E05-claude-bank-018` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de kist liggen 23 appels. Er komen er 9 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 23 − 9 · B) 23 + 8 · C) 23 + 9
    - **Antwoord:** 23 + 9  (controle: ok)
    - **Fout-hints (Claude):** 23 − 9 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er komen dingen bij, dus het worden er meer. Dat is een plussom. Zoek de som met het getal dat er al lag en het getal dat erbij komt.
- **Ouderzin:** Je kind kiest de plussom die past bij een verhaal tot 30 waarin er dingen bijkomen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (de minsom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `plussom, ander getal` (de plussom (merge-afleider a + (b+1); 1 okt)) → Dat is wel een plussom. Maar één getal klopt niet. Hoeveel lagen er al? En hoeveel komen erbij?  [nieuw]
  - (de keersom) → Die som past niet bij het verhaal. Er komen dingen bij. Dat is plus.  [nieuw]
- Status: hints klaar
