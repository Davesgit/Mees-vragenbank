# G3-GET-E06 — Groepjes maken en delen

Onze omschrijving: × via handig tellen ≤20 (context); ÷ informeel ≤20 · in onze bank: 8 items

Claude-vragen gemapt: **11** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [rooster] Er zijn # rijen van # hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? # + # + # = □

- Items: **3** · Claude-doelen: D5-1 (3) · regel: D-rijen × (R24-rooster-keer)
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E06-claude-bank-007` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 3 rijen van 6 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 6 + 6 + 6 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 3, "hokjesPerRij": 6, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 3, "hokjesPerRij": 6, "claudeAntwoord": "6x3", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 18; het rooster is al gekleurd (3 rijen van 6 hokjes)"}`
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 3 rijen van 6. Tel per rij: 6, 12, 18.
  - `G3-GET-E06-claude-bank-006` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 3 rijen van 3 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 3 + 3 + 3 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 3, "hokjesPerRij": 3, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 3, "hokjesPerRij": 3, "claudeAntwoord": "3x3", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 9; het rooster is al gekleurd (3 rijen van 3 hokjes)"}`
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 3 rijen van 3. Tel per rij: 3, 6, 9.

- **Hint 1 (te schrijven):** Kijk naar één gekleurde rij. Hoeveel hokjes zitten erin?
- **Hint 2 (te schrijven):** Tel de volgende rij erbij, en dan de volgende. Ga door tot je alle rijen hebt gehad. Elke rij is één getal in de plussom.
- **Ouderzin:** Je kind telt rijen met evenveel gekleurde hokjes bij elkaar op (herhaald optellen, nog zonder keerteken).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één rij` (fout = getal2) → Dat is één rij. Er zijn meer rijen. Tel ze er allemaal bij.  [nieuw]
  - `rijen en hokjes opgeteld` (fout = getal1 + getal2) → Je hebt de rijen en de hokjes bij elkaar gedaan. Tel alle hokjes: elke rij komt erbij.  [nieuw]
  - `aantal rijen` (fout = getal1) → Dat is het aantal rijen. Hoeveel hokjes zijn er samen gekleurd?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel alle hokjes nog eens, rij voor rij.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de plussom. Tel de getallen één voor één bij elkaar. Je mag ook de gekleurde hokjes tellen.  [nieuw]
- Status: hints klaar

## Somtype 2: [rooster] Er zijn # rijen van # hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? # + # = □

- Items: **3** · Claude-doelen: D5-1 (3) · regel: D-rijen × (R24-rooster-keer)
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E06-claude-bank-009` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 2 rijen van 5 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 5 + 5 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 2, "hokjesPerRij": 5, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 2, "hokjesPerRij": 5, "claudeAntwoord": "5x2", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 10; het rooster is al gekleurd (2 rijen van 5 hokjes)"}`
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 2 rijen van 5. Tel per rij: 5, 10.
  - `G3-GET-E06-claude-bank-011` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 2 rijen van 2 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 2 + 2 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 2, "hokjesPerRij": 2, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 2, "hokjesPerRij": 2, "claudeAntwoord": "2x2", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 4; het rooster is al gekleurd (2 rijen van 2 hokjes)"}`
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 2 rijen van 2. Tel per rij: 2, 4.

- **Hint 1 (te schrijven):** Kijk naar één gekleurde rij. Hoeveel hokjes zitten erin?
- **Hint 2 (te schrijven):** Tel de volgende rij erbij, en dan de volgende. Ga door tot je alle rijen hebt gehad. Elke rij is één getal in de plussom.
- **Ouderzin:** Je kind telt rijen met evenveel gekleurde hokjes bij elkaar op (herhaald optellen, nog zonder keerteken).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één rij` (fout = getal2) → Dat is één rij. Er zijn meer rijen. Tel ze er allemaal bij.  [nieuw]
  - `rijen en hokjes opgeteld` (fout = getal1 + getal2) → Je hebt de rijen en de hokjes bij elkaar gedaan. Tel alle hokjes: elke rij komt erbij.  [nieuw]
  - `aantal rijen` (fout = getal1) → Dat is het aantal rijen. Hoeveel hokjes zijn er samen gekleurd?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel alle hokjes nog eens, rij voor rij.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de plussom. Tel de getallen één voor één bij elkaar. Je mag ook de gekleurde hokjes tellen.  [nieuw]
- Status: hints klaar

## Somtype 3: [rooster] Er zijn # rijen van # hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? # + # + # + # + # = □

- Items: **2** · Claude-doelen: D5-1 (2) · regel: D-rijen × (R24-rooster-keer)
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E06-claude-bank-003` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 5 rijen van 2 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 2 + 2 + 2 + 2 + 2 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 5, "hokjesPerRij": 2, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 5, "hokjesPerRij": 2, "claudeAntwoord": "2x5", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 10; het rooster is al gekleurd (5 rijen van 2 hokjes)"}`
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 5 rijen van 2. Tel per rij: 2, 4, 6, 8, 10.
  - `G3-GET-E06-claude-bank-002` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 5 rijen van 3 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 3 + 3 + 3 + 3 + 3 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 5, "hokjesPerRij": 3, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 5, "hokjesPerRij": 3, "claudeAntwoord": "3x5", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 15; het rooster is al gekleurd (5 rijen van 3 hokjes)"}`
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 5 rijen van 3. Tel per rij: 3, 6, 9, 12, 15.

- **Hint 1 (te schrijven):** Kijk naar één gekleurde rij. Hoeveel hokjes zitten erin?
- **Hint 2 (te schrijven):** Tel de volgende rij erbij, en dan de volgende. Ga door tot je alle rijen hebt gehad. Elke rij is één getal in de plussom.
- **Ouderzin:** Je kind telt rijen met evenveel gekleurde hokjes bij elkaar op (herhaald optellen, nog zonder keerteken).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één rij` (fout = getal2) → Dat is één rij. Er zijn meer rijen. Tel ze er allemaal bij.  [nieuw]
  - `rijen en hokjes opgeteld` (fout = getal1 + getal2) → Je hebt de rijen en de hokjes bij elkaar gedaan. Tel alle hokjes: elke rij komt erbij.  [nieuw]
  - `aantal rijen` (fout = getal1) → Dat is het aantal rijen. Hoeveel hokjes zijn er samen gekleurd?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel alle hokjes nog eens, rij voor rij.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de plussom. Tel de getallen één voor één bij elkaar. Je mag ook de gekleurde hokjes tellen.  [nieuw]
- Status: hints klaar

## Somtype 4: [rooster] Er zijn # rijen van # hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? # + # + # + # = □

- Items: **2** · Claude-doelen: D5-1 (2) · regel: D-rijen × (R24-rooster-keer)
- Getallenruimte: 0–10 · type: invullen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-GET-E06-claude-bank-005` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 4 rijen van 5 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 5 + 5 + 5 + 5 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 4, "hokjesPerRij": 5, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 4, "hokjesPerRij": 5, "claudeAntwoord": "5x4", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 20; het rooster is al gekleurd (4 rijen van 5 hokjes)"}`
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 4 rijen van 5. Tel per rij: 5, 10, 15, 20.
  - `G3-GET-E06-claude-bank-004` (Claude D5-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Er zijn 4 rijen van 4 hokjes gekleurd. Hoeveel hokjes zijn er gekleurd? 4 + 4 + 4 + 4 = □
    - **Tekening:** `{"soort": "rooster", "rijen": 5, "kolommen": 10, "kleurbaar": false, "gekleurd": {"rijen": 4, "hokjesPerRij": 4, "vanaf": "linksboven"}}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 4, "hokjesPerRij": 4, "claudeAntwoord": "4x4", "claudeNotatie": "kolommen x rijen", "nakijken": "getal 16; het rooster is al gekleurd (4 rijen van 4 hokjes)"}`
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 4 rijen van 4. Tel per rij: 4, 8, 12, 16.

- **Hint 1 (te schrijven):** Kijk naar één gekleurde rij. Hoeveel hokjes zitten erin?
- **Hint 2 (te schrijven):** Tel de volgende rij erbij, en dan de volgende. Ga door tot je alle rijen hebt gehad. Elke rij is één getal in de plussom.
- **Ouderzin:** Je kind telt rijen met evenveel gekleurde hokjes bij elkaar op (herhaald optellen, nog zonder keerteken).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één rij` (fout = getal2) → Dat is één rij. Er zijn meer rijen. Tel ze er allemaal bij.  [nieuw]
  - `rijen en hokjes opgeteld` (fout = getal1 + getal2) → Je hebt de rijen en de hokjes bij elkaar gedaan. Tel alle hokjes: elke rij komt erbij.  [nieuw]
  - `aantal rijen` (fout = getal1) → Dat is het aantal rijen. Hoeveel hokjes zijn er samen gekleurd?  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Tel alle hokjes nog eens, rij voor rij.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de plussom. Tel de getallen één voor één bij elkaar. Je mag ook de gekleurde hokjes tellen.  [nieuw]
- Status: hints klaar

## Somtype 5: Je springt met stappen van # [ding] # naar #. Hoeveel sprongen maak je?

- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels (R25-puzzel)
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: getallenlijn 0–10 met een boogje voor elke sprong van 2 (Didactiek §4)
- Denkfouten (Claude): getal-overgenomen (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je springt niet steeds één stap vooruit, maar twee tegelijk.”)
- Voorbeelden:
  - `G3-GET-E06-claude-bank-001` (Claude W1, ai, niveau 1 → basis)
    - **Opgave:** Je springt met stappen van 2 vanaf 0 naar 10. Hoeveel sprongen maak je?
    - **Opties:** A) 5 sprongen · B) 10 sprongen · C) 6 sprongen
    - **Antwoord:** 5 sprongen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 sprongen → Je springt niet steeds één stap vooruit, maar twee tegelijk. · 6 sprongen → Schrijf de getallen op waar je landt. Eerst 2, dan 4, dan 6. Tel dan hoe vaak je landt.
    - **Uitleg (Claude):** Je landt op 2, 4, 6, 8 en 10. Dat zijn vijf landingen, dus vijf sprongen. Elke sprong is 2 erbij.

- **Hint 1 (te schrijven):** Spring in gedachten op een getallenlijn. Tel hoe vaak je springt.
- **Hint 2 (te schrijven):** Begin bij het getal waar je vanaf springt. Spring steeds even ver als de stap. Tel elke sprong. Stop als je bij het laatste getal bent.
- **Ouderzin:** Je kind telt hoeveel sprongen van gelijke grootte je nodig hebt om ergens te komen.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
