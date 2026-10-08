# G3-GET-M04 — Wat plus en min betekenen

Onze omschrijving: +/− betekenis + notatie +, −, =; relatie +/−/splitsen · in onze bank: 8 items

Claude-vragen gemapt: **28** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + # = #. Dan weet je ook hoeveel # − # is. Denk aan # [ding] waarvan er # [ding]. ⏎ # − # = □

- Items: **16** · Claude-doelen: D1-4 (16) · regel: R11-relatie
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): getal-overgenomen (16), verkeerde-bewerking (16), andere-deel-genomen (12)
- Verschillende Claude-fout-hints: 13 (meest: “Dit is een minsom. Het antwoord is kleiner dan het eerste getal.”)
- Voorbeelden:
  - `G3-GET-M04-claude-bank-008` (Claude D1-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 + 2 = 6. Dan weet je ook hoeveel 6 − 4 is. Denk aan 6 botten waarvan er 4 weggaan.
6 − 4 = □
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je haalt 4 eraf. Wat blijft er over? Het andere getal uit de plussom. · 6 → 6 is het geheel. Na het weghalen blijft er minder over. · 10 → Dit is een minsom. Het antwoord is kleiner dan het eerste getal.
    - **Uitleg (Claude):** Plus en min horen bij elkaar. Als 4 + 2 = 6, dan is 6 − 4 = 2.
  - `G3-GET-M04-claude-bank-006` (Claude D1-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 + 1 = 5. Dan weet je ook hoeveel 5 − 4 is. Denk aan 5 poesjes waarvan er 4 weggaan.
5 − 4 = □
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je haalt 4 eraf. Wat blijft er over? Het andere getal uit de plussom. · 5 → 5 is het geheel. Na het weghalen blijft er minder over. · 9 → Dit is een minsom. Het antwoord is kleiner dan het eerste getal.
    - **Uitleg (Claude):** Plus en min horen bij elkaar. Als 4 + 1 = 5, dan is 5 − 4 = 1.

- **Hint 1 (te schrijven):** Kijk naar de plussom. Die drie getallen horen bij elkaar.
- **Hint 2 (te schrijven):** De plussom zegt welke twee delen samen het grootste getal maken. Haal je het ene deel eraf? Dan blijft het andere deel over.
- **Ouderzin:** Je kind gebruikt een plussom tot 10 om de minsom die erbij hoort te maken.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = het getal dat eraf gaat; tekst per item) → Je haalt … eraf. Wat blijft er over? Het andere getal uit de plussom.  [Claude, ok]
  - (fout = het hele getal; tekst per item) → … is het geheel. Na het weghalen blijft er minder over.  [Claude, ok]
  - (fout = getal opgeteld in plaats van eraf) → Dit is een minsom. Het antwoord is kleiner dan het grootste getal.  [Claude, taalfix]
- Status: hints klaar

## Somtype 2: # − # = #. Welke plussom hoort hierbij? # + □ = #

- Items: **12** · Claude-doelen: D1-4 (12) · regel: R11-relatie
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): andere-deel-genomen (12), getal-overgenomen (12)
- Verschillende Claude-fout-hints: 17 (meest: “8 is de uitkomst, niet het getal dat je erbij doet.”)
- Voorbeelden:
  - `G3-GET-M04-claude-bank-018` (Claude D1-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 8 − 7 = 1. Welke plussom hoort hierbij? 1 + □ = 8
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 1 → 1 staat er al. Welk getal ontbreekt uit de familie 1, 7, 8? · 8 → 8 is de uitkomst, niet het getal dat je erbij doet.
    - **Uitleg (Claude):** De drie getallen 1, 7 en 8 horen bij elkaar. 1 + 7 = 8.
  - `G3-GET-M04-claude-bank-021` (Claude D1-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 9 − 6 = 3. Welke plussom hoort hierbij? 3 + □ = 9
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 3 → 3 staat er al. Welk getal ontbreekt uit de familie 3, 6, 9? · 9 → 9 is de uitkomst, niet het getal dat je erbij doet.
    - **Uitleg (Claude):** De drie getallen 3, 6 en 9 horen bij elkaar. 3 + 6 = 9.

- **Hint 1 (te schrijven):** De minsom en de plussom gebruiken dezelfde drie getallen.
- **Hint 2 (te schrijven):** Het grootste getal is alles samen. De twee kleinere getallen zijn de delen. Welk deel mist er nog in de plussom?
- **Ouderzin:** Je kind maakt bij een minsom tot 10 de plussom die erbij hoort.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
