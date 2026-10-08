# G3-GET-E03 — Nadenken over getallen

Onze omschrijving: Betekenissen van getallen; kritisch redeneren ≤20 · in onze bank: 8 items

Claude-vragen gemapt: **5** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Je knipt een lang touw op # [ding] door. Hoeveel stukken touw heb je dan?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: een lang touw met 3 knipplekken (een schaartje bij elke plek) (Didactiek §4)
- Denkfouten (Claude): getal-overgenomen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Probeer het met één knip. Hoeveel stukken heb je dan al?”)
- Voorbeelden:
  - `G3-GET-E03-claude-bank-003` (Claude W1, ai, niveau 1 → basis)
    - **Opgave:** Je knipt een lang touw op 3 plekken door. Hoeveel stukken touw heb je dan?
    - **Opties:** A) 6 stukken · B) 4 stukken · C) 3 stukken
    - **Antwoord:** 4 stukken  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3 stukken → Probeer het met één knip. Hoeveel stukken heb je dan al? · 6 stukken → Elke knip maakt er één stuk bij, niet twee keer zo veel.
    - **Uitleg (Claude):** Bij één knip krijg je 2 stukken. Elke knip erbij geeft steeds één stuk extra. Bij 3 knippen zijn dat 4 stukken.

- **Hint 1 (te schrijven):** Teken het touw. Zet een streepje op elke plek waar je knipt.
- **Hint 2 (te schrijven):** Tel daarna de stukken tussen de streepjes. Vergeet het stuk aan het begin en het stuk aan het eind niet.
- **Ouderzin:** Je kind denkt na over knippen en stukken: hoeveel stukken krijg je bij een aantal knippen?
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 2: Je knipt een strook papier in # [ding] grote stukken. Hoe vaak moet je knippen?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: een strook papier in 4 even grote stukken, met een stippellijn waar je knipt (Didactiek §4)
- Denkfouten (Claude): getal-overgenomen (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Teken de strook en zet streepjes waar je knipt. Tel daarna pas de streepjes.”)
- Voorbeelden:
  - `G3-GET-E03-claude-bank-004` (Claude W1, ai, niveau 1 → basis)
    - **Opgave:** Je knipt een strook papier in 4 even grote stukken. Hoe vaak moet je knippen?
    - **Opties:** A) 5 keer · B) 3 keer · C) 4 keer
    - **Antwoord:** 3 keer  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 keer → Teken de strook en zet streepjes waar je knipt. Tel daarna pas de streepjes. · 5 keer → Je hoeft aan de uiteinden niet te knippen. Tel alleen de knipplekken tussen de stukken.
    - **Uitleg (Claude):** Bij elke knip komt er één stuk bij. Je begint met 1 stuk en wilt er 4, dus je knipt 3 keer.

- **Hint 1 (te schrijven):** Teken de strook. Verdeel hem in stukken die even groot zijn.
- **Hint 2 (te schrijven):** Zet een streepje tussen elke twee stukken. Tel de streepjes. Zo vaak knip je.
- **Ouderzin:** Je kind denkt na over knippen en stukken: hoe vaak knip je voor een aantal stukken?
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (4 keer) → Teken de strook en zet streepjes waar je knipt. Tel daarna pas de streepjes.  [Claude, ok]
  - (5 keer) → Aan de twee kanten van de strook knip je niet. Tel alleen waar je knipt.  [Claude, taalfix]
- Status: hints klaar

## Somtype 3: De kinderen staan in één rij bij de [ding]. Noor is de vijfde van voren en de tweede van achteren. Hoeveel kinderen staan er in de rij?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: een rij kinderen van opzij, met een pijl "voren" en "achteren"; Noor heeft een rode trui (Didactiek §4)
- Denkfouten (Claude): een-ernaast (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Als je 5 en 2 optelt, tel je Noor twee keer mee. Teken de rij eens met streepjes.”)
- Voorbeelden:
  - `G3-GET-E03-claude-bank-001` (Claude W1, ai, niveau 1 → basis)
    - **Opgave:** De kinderen staan in één rij bij de gymzaal. Noor is de vijfde van voren en de tweede van achteren. Hoeveel kinderen staan er in de rij?
    - **Opties:** A) 7 kinderen · B) 5 kinderen · C) 6 kinderen
    - **Antwoord:** 6 kinderen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 kinderen → Als je 5 en 2 optelt, tel je Noor twee keer mee. Teken de rij eens met streepjes. · 5 kinderen → Achter Noor staat ook nog iemand. Teken de rij en zet Noor op haar plek.
    - **Uitleg (Claude):** Voor Noor staan 4 kinderen en achter haar staat 1 kind. Met Noor erbij zijn dat 6 kinderen.

- **Hint 1 (te schrijven):** Teken de rij met streepjes. Zet Noor op haar plek.
- **Hint 2 (te schrijven):** Tel de kinderen vóór Noor en de kinderen achter Noor. Tel Noor zelf er één keer bij.
- **Ouderzin:** Je kind redeneert over een plek in de rij, van voren en van achteren geteld.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 4: De kinderen staan in één rij. Sam is de derde van voren en ook de vierde van achteren. Hoeveel kinderen staan er in de rij?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: een rij kinderen van opzij, met een pijl "voren" en "achteren"; Sam heeft een gele pet (Didactiek §4)
- Denkfouten (Claude): None (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt Sam misschien twee keer geteld. Sam staat maar op één plek in de rij.”)
- Voorbeelden:
  - `G3-GET-E03-claude-bank-002` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** De kinderen staan in één rij. Sam is de derde van voren en ook de vierde van achteren. Hoeveel kinderen staan er in de rij?
    - **Opties:** A) 6 kinderen · B) 7 kinderen · C) 5 kinderen
    - **Antwoord:** 6 kinderen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 kinderen → Je hebt Sam misschien twee keer geteld. Sam staat maar op één plek in de rij. · 5 kinderen → Teken de rij met streepjes en zet Sam erin. Tel daarna alle streepjes.
    - **Uitleg (Claude):** Voor Sam staan 2 kinderen en achter Sam staan 3 kinderen. Samen met Sam zelf zijn dat 6 kinderen. Sam tel je maar één keer.

- **Hint 1 (te schrijven):** Teken de rij met streepjes. Zet Sam op zijn plek.
- **Hint 2 (te schrijven):** Tel de kinderen vóór Sam en de kinderen achter Sam. Tel Sam zelf er één keer bij.
- **Ouderzin:** Je kind redeneert over een plek in de rij, van voren en van achteren geteld.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 5: Langs een pad staat een hek van # [ding]. Hoeveel palen staan er?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: een hek langs een pad: 5 vakken met de palen ertussen en aan de uiteinden (Didactiek §4)
- Denkfouten (Claude): getal-overgenomen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Elk vak heeft aan beide kanten een paal. Vergeet de laatste paal aan het eind niet.”)
- Voorbeelden:
  - `G3-GET-E03-claude-bank-005` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Langs een pad staat een hek van 5 vakken. Hoeveel palen staan er?
    - **Opties:** A) 5 palen · B) 10 palen · C) 6 palen
    - **Antwoord:** 6 palen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 palen → Elk vak heeft aan beide kanten een paal. Vergeet de laatste paal aan het eind niet. · 10 palen → Twee vakken naast elkaar delen samen één paal. Die paal tel je maar één keer.
    - **Uitleg (Claude):** Teken 5 vakken naast elkaar. Bij elk vak komt links een paal en aan het eind nog één. Dat zijn 6 palen.

- **Hint 1 (te schrijven):** Teken het hek: eerst de vakken naast elkaar.
- **Hint 2 (te schrijven):** Zet daarna de palen. Tussen twee vakken staat één paal. Aan het begin en aan het eind staat ook een paal. Tel alle palen één voor één.
- **Ouderzin:** Je kind denkt na over een hek: hoeveel palen horen bij een aantal vakken?
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `paal vergeten` (5 palen) → Bijna! Aan het begin en aan het eind staat ook een paal. Tel de palen nog eens, één voor één.  [nieuw]
  - `dubbel geteld` (10 palen) → Tussen twee vakken staat maar één paal. Tel elke paal maar één keer.  [nieuw]
- Status: hints klaar
