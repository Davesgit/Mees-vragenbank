# G3-MEET-K03 — Meer of minder erin

Onze omschrijving: Inhoud begrippen; meten met natuurlijke maat · in onze bank: 4 items

Claude-vragen gemapt: **5** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Vergelijken zonder maat — inhoud vergelijken

- Items: **5** · Claude-doelen: M1 (5) · regel: R27-vergelijken
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (7), schatting-verkeerd (3)
- Verschillende Claude-fout-hints: 10 (meest: “Hoeveel bekers water heb je nodig om de emmer helemaal vol te krijgen?”)
- Voorbeelden:
  - `G3-MEET-K03-claude-bank-004` (Claude M1, ai, niveau 1 → basis)
    - **Opgave:** Op het strand heb je een emmer en een beker. Waar kan meer water in?
    - **Opties:** A) In allebei evenveel. · B) In de emmer. · C) In de beker.
    - **Antwoord:** In de emmer.  (controle: n.v.t.)
    - **Fout-hints (Claude):** In de beker. → Hoeveel bekers water heb je nodig om de emmer helemaal vol te krijgen? · In allebei evenveel. → Kijk goed naar de grootte van de emmer en van de beker. Die zijn niet gelijk.
    - **Uitleg (Claude):** Een emmer is veel groter dan een beker. Er passen heel wat bekers water in een emmer. In de emmer kan dus meer.
  - `G3-MEET-K03-claude-bank-001` (Claude M1, ai, niveau 2 → toepassen)
    - **Opgave:** Je vult twee kannen met bekers water. In de rode kan gaan 4 bekers en in de blauwe kan gaan 7 bekers. In welke kan gaat meer water?
    - **Tekening:** `{"soort": "kannen", "kannen": [{"kleur": "rood", "bekers": 4}, {"kleur": "blauw", "bekers": 7}]}`
    - **Opties:** A) In allebei evenveel. · B) In de blauwe kan. · C) In de rode kan.
    - **Antwoord:** In de blauwe kan.  (controle: ok)
    - **Fout-hints (Claude):** In de rode kan. → Vergelijk de aantallen bekers. Is 4 meer of minder dan 7? · In allebei evenveel. → De aantallen bekers zijn niet gelijk. Kijk nog eens naar de getallen.
    - **Uitleg (Claude):** Je gebruikt steeds dezelfde beker. De blauwe kan heeft 7 bekers nodig en de rode kan maar 4. In de blauwe kan gaat dus meer water.

- **Hint 1 (te schrijven):** Waar past meer in? Denk aan hoe groot de dingen zijn.
- **Hint 2 (te schrijven):** Denk aan vullen en leeggieten. Hoe vaak past het kleine ding in het grote? Heb je met bekers gemeten? Waar meer bekers in gaan, past meer in.
- **Ouderzin:** Je kind vergelijkt inhoud zonder maat: waar past meer in?
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
