# G5-MEET-E03 — Oppervlakte op het rooster

Onze omschrijving: Opp. vierkant/rechthoek/grillig op rooster; omvormen behoudt opp. · in onze bank: 8 items

Claude-vragen gemapt: **10** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [rooster] Kleur een rechthoek met een oppervlakte van # hokjes.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[rooster] Kleur een rechthoek met een oppervlakte van # hokjes.” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M16 (10) · regel: G5-M05-oppervlakte
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-MEET-E03-claude-bank-002` (Claude M16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Kleur een rechthoek met een oppervlakte van 12 hokjes.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm-oppervlakte", "hokjes": 12, "claudeAntwoord": "4x3", "goed": ["2 × 6", "3 × 4", "4 × 3", "6 × 2"], "nakijken": "elke gekleurde rechthoek van 12 hokjes is goed (2 × 6, 3 × 4, 4 × 3, 6 × 2)"}`
    - **Antwoord:** een rechthoek van 12 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Zoek twee getallen die vermenigvuldigd 12 geven, bijvoorbeeld 4 bij 3.
  - `G5-MEET-E03-claude-bank-004` (Claude M16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Kleur een rechthoek met een oppervlakte van 24 hokjes.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm-oppervlakte", "hokjes": 24, "claudeAntwoord": "4x6", "goed": ["3 × 8", "4 × 6", "6 × 4", "8 × 3"], "nakijken": "elke gekleurde rechthoek van 24 hokjes is goed (3 × 8, 4 × 6, 6 × 4, 8 × 3)"}`
    - **Antwoord:** een rechthoek van 24 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Zoek twee getallen die vermenigvuldigd 24 geven, bijvoorbeeld 4 bij 6.

- **Hint 1 (te schrijven):** De oppervlakte is hoeveel hokjes er binnen de rechthoek zitten. Hoeveel hokjes moet je kleuren?
- **Hint 2 (te schrijven):** Bedenk een keersom met dit aantal als uitkomst. Het eerste getal is het aantal rijen, het tweede hoeveel hokjes er in elke rij komen. Kleur de rijen recht onder elkaar.
- **Ouderzin:** Je kind kleurt een rechthoek met een gegeven oppervlakte (aantal hokjes) op een rooster.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één hokje te veel` (fout = getal + 1 (aantal gekleurde hokjes)) → Je hebt één hokje te veel gekleurd. Tel de hokjes nog eens.  [nieuw]
  - `te weinig hokjes` (fout kleiner dan het getal in de vraag (aantal gekleurde hokjes)) → Je hebt te weinig hokjes gekleurd. Tel ze nog eens: hoeveel moeten het er zijn?  [nieuw]
  - `andere fout` (andere fout) → Tel je hokjes. Zijn het er precies genoeg? Is het een rechthoek: alle rijen even lang en recht onder elkaar?  [nieuw]
- Status: hints klaar
