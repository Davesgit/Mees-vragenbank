# G7-VERH-01 — Breuk, procent en schaal lezen

Onze omschrijving: Notaties & betekenis · in onze bank: 8 items

Claude-vragen gemapt: **28** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [balk kleuren] Een pot heeft # [ding]. Kleur #% ervan. Elk stukje is # [ding].

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[balk kleuren] Een pot heeft # [ding]. Kleur #% ervan. Elk stukje is # [ding].” (koppeling: claudeId)
- Items: **12** · Claude-doelen: V3 (12) · regel: G7-V04-procent-balk
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G7-VERH-01-claude-bank-006` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pot heeft 400 knikkers. Kleur 20% ervan. Elk stukje is 40 knikkers.
    - **UI:** balk kleuren
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 10% van 400 is 40. 20% is 2 keer 40 = 80.
  - `G7-VERH-01-claude-bank-008` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pot heeft 200 knikkers. Kleur 50% ervan. Elk stukje is 20 knikkers.
    - **UI:** balk kleuren
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 10% van 200 is 20. 50% is 5 keer 20 = 100.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Hoeveel is dat procent van alles in de pot?
- **Hint 2 (te schrijven):** Reken eerst uit hoeveel het procent van het hele aantal is. Kijk dan hoe vaak één stukje daarin past. Zoveel stukjes kleur je.
- **Ouderzin:** Je kind kleurt een deel van een balk: hoeveel stukjes horen bij het procent?
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel stukjes je kleurt.  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel het procent is, en hoeveel stukjes dat zijn.  [nieuw]
- Status: hints klaar

## Somtype 2: [balk kleuren] Kleur #% van de balk.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[balk kleuren] Kleur #% van de balk.” (koppeling: claudeId)
- Items: **11** · Claude-doelen: V1 (11) · regel: G7-V04-procent-balk
- Getallenruimte: procenten · type: kale
- Uit de G6-park: 11 items
- Denkfouten (Claude): None (11)
- Verschillende Claude-fout-hints: 1 (meest: “Elk stukje is 5%, niet 10%.”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-020` (Claude V1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 60% van de balk.
    - **UI:** balk kleuren
    - **Antwoord:** 12  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 → Elk stukje is 5%, niet 10%.
    - **Uitleg (Claude):** De hele balk is 100%. Elk stukje is 5%. 60% is 12 stukjes.
  - `G7-VERH-01-claude-bank-023` (Claude V1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 10% van de balk.
    - **UI:** balk kleuren
    - **Antwoord:** 2  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1 → Elk stukje is 5%, niet 10%.
    - **Uitleg (Claude):** De hele balk is 100%. Elk stukje is 5%. 10% is 2 stukjes.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. De hele balk is honderd procent.
- **Hint 2 (te schrijven):** Tel hoeveel stukjes de balk heeft. Reken uit voor hoeveel procent één stukje staat. Hoe vaak past dat in het procent uit de vraag?
- **Ouderzin:** Je kind kleurt een percentage van een balk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `elk stukje tien procent` (Claudes sleutel (alle, zonder label)) → Dat is te weinig. Heb je elk stukje als tien procent geteld? Tel eerst hoeveel stukjes de balk heeft.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de stukjes van de balk, en reken uit hoeveel procent één stukje is.  [nieuw]
- Status: hints klaar

## Somtype 3: Bij de schaal # : # [ding] twee getallen. Welk getal hoort bij de [ding]?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Bij de schaal # : # [ding] twee getallen. Welk getal hoort bij de [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V10-schaal-lezen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): andere-deel-genomen (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het getal achter de dubbele punt hoort bij het echte voorwerp. Welk getal blijft er dan over?”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-001` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Bij de schaal 1 : 500 horen twee getallen. Welk getal hoort bij de tekening?
    - **Opties:** A) Het getal 1 · B) Het getal 500 · C) Het getal 5
    - **Antwoord:** Het getal 1  (controle: ok)
    - **Fout-hints (Claude):** Het getal 500 → Het getal achter de dubbele punt hoort bij het echte voorwerp. Welk getal blijft er dan over? · Het getal 5 → Lees de schaal precies zoals hij er staat. Er staat geen losse 5 in de schaal.
    - **Uitleg (Claude):** Bij een schaal staat vooraan altijd de maat op de tekening. Achter de dubbele punt staat de echte maat. Dus het getal 1 hoort bij de tekening.

- **Hint 1 (te schrijven):** Een schaal heeft twee getallen met een dubbele punt (:) ertussen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Op de tekening is alles kleiner dan echt. Welk getal hoort dan bij de tekening?
- **Ouderzin:** Je kind leert wat een schaal (zoals op een plattegrond) betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal van het echte voorwerp` (Het getal 500) → Dat getal hoort bij het echte voorwerp. Op de tekening is alles kleiner.  [nieuw]
  - `getal niet uit de schaal` (Het getal 5) → Dat getal staat niet in de schaal. Kijk naar de twee getallen van de schaal.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de twee getallen van de schaal.  [nieuw]
- Status: hints klaar

## Somtype 4: Op een tekening staat schaal # : #. Wat weet je dan over de tekening?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Op een tekening staat schaal # : #. Wat weet je dan over de tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V10-schaal-lezen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eens naar de twee getallen van deze schaal. Zijn ze verschillend of gelijk?”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-002` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Op een tekening staat schaal 1 : 1. Wat weet je dan over de tekening?
    - **Opties:** A) De tekening is 100 keer zo klein · B) De tekening is net zo groot als het echte voorwerp · C) De tekening is 2 keer zo klein
    - **Antwoord:** De tekening is net zo groot als het echte voorwerp  (controle: n.v.t.)
    - **Fout-hints (Claude):** De tekening is 2 keer zo klein → Kijk eens naar de twee getallen van deze schaal. Zijn ze verschillend of gelijk? · De tekening is 100 keer zo klein → Je denkt aan de schaal 1 : 100. Lees nog eens welk getal hier achter de dubbele punt staat.
    - **Uitleg (Claude):** Bij schaal 1 : 1 hoort bij 1 cm op de tekening ook 1 cm in het echt. Er wordt dus niets kleiner of groter gemaakt. De tekening is precies even groot als het echte voorwerp.

- **Hint 1 (te schrijven):** Een schaal vergelijkt de tekening met het echte voorwerp. Een op tien betekent: één centimeter op de tekening is tien centimeter echt.
- **Hint 2 (te schrijven):** Kijk naar de twee getallen van deze schaal. Zijn ze gelijk? Hoeveel keer zo groot is het echte voorwerp dan?
- **Ouderzin:** Je kind leert wat een schaal (zoals op een plattegrond) betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `past bij een andere schaal` (De tekening is 100 keer zo klein) → Dat past bij een schaal van een op honderd. Kijk naar de getallen van deze schaal.  [nieuw]
  - `past bij een andere schaal (twee)` (De tekening is 2 keer zo klein) → Dat past bij een schaal van een op twee. Kijk naar de getallen van deze schaal.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de twee getallen van deze schaal.  [nieuw]
- Status: hints klaar

## Somtype 5: Op een tekening van een huis staat schaal # : #. Wat betekent dat?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Op een tekening van een huis staat schaal # : #. Wat betekent dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V10-schaal-lezen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): tiental-ernaast (1), eenheid-verkeerd-omgerekend (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk nog eens goed naar het tweede getal van de schaal. Staat er 10 of staat er meer?”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-003` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Op een tekening van een huis staat schaal 1 : 100. Wat betekent dat?
    - **Opties:** A) 1 cm op de tekening is 100 cm echt · B) 1 cm op de tekening is 10 cm echt · C) 1 cm op de tekening is 100 m echt
    - **Antwoord:** 1 cm op de tekening is 100 cm echt  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1 cm op de tekening is 10 cm echt → Kijk nog eens goed naar het tweede getal van de schaal. Staat er 10 of staat er meer? · 1 cm op de tekening is 100 m echt → Bij schaal hoort links en rechts dezelfde eenheid. Begin je met cm, dan blijf je bij cm.
    - **Uitleg (Claude):** Bij schaal 1 : 100 hoort bij 1 stukje op de tekening 100 van dezelfde stukjes in het echt. Meet je in cm, dan is 1 cm op papier 100 cm in het echt. De tekening is dus 100 keer kleiner.

- **Hint 1 (te schrijven):** Een schaal vergelijkt de tekening met het echte voorwerp. Een op tien betekent: één centimeter op de tekening is tien centimeter echt.
- **Hint 2 (te schrijven):** Bij een schaal horen beide getallen bij dezelfde maat, bijvoorbeeld centimeter. Welk getal hoort bij het echte huis?
- **Ouderzin:** Je kind leert wat een schaal (zoals op een plattegrond) betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `past bij een andere schaal` (1 cm op de tekening is 10 cm echt) → Dat past bij een schaal van een op tien. Kijk welk getal in deze schaal staat.  [nieuw]
  - `andere maat` (1 cm op de tekening is 100 m echt) → Kijk naar de maat. Bij een schaal horen beide getallen bij dezelfde maat: centimeter op de tekening is centimeter echt.  [nieuw]
  - `andere fout` (andere fout) → Kijk welk getal in de schaal staat, en welke maat erbij hoort.  [nieuw]
- Status: hints klaar

## Somtype 6: Waarom gebruik je een schaal als je een plattegrond van je huis tekent?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Waarom gebruik je een schaal als je een plattegrond van je huis tekent?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V10-schaal-lezen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een tekening verandert niets aan het echte huis. Denk aan wat er op het papier past.”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-004` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Waarom gebruik je een schaal als je een plattegrond van je huis tekent?
    - **Opties:** A) Omdat het huis dan echt kleiner wordt · B) Omdat je dan niet hoeft te meten · C) Omdat het echte huis niet op papier past
    - **Antwoord:** Omdat het echte huis niet op papier past  (controle: n.v.t.)
    - **Fout-hints (Claude):** Omdat het huis dan echt kleiner wordt → Een tekening verandert niets aan het echte huis. Denk aan wat er op het papier past. · Omdat je dan niet hoeft te meten → Voor een plattegrond op schaal moet je de echte maten juist wel weten.
    - **Uitleg (Claude):** Een huis is veel te groot voor een blaadje papier. Met een schaal maak je alle maten net zoveel kleiner. Zo blijft de tekening toch kloppen.

- **Hint 1 (te schrijven):** Wat verandert er door een schaal: het echte huis, of de tekening?
- **Hint 2 (te schrijven):** Met een schaal teken je alles evenveel keer kleiner. Het echte huis blijft zoals het is. Waarom maak je de tekening kleiner?
- **Ouderzin:** Je kind leert wat een schaal (zoals op een plattegrond) betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `huis wordt kleiner` (Omdat het huis dan echt kleiner wordt) → Het echte huis blijft even groot. Alleen de tekening is kleiner.  [nieuw]
  - `niet meten` (Omdat je dan niet hoeft te meten) → Je meet juist wel: je meet het huis, en rekent de maten om voor de tekening.  [nieuw]
  - `andere fout` (andere fout) → Denk aan het echte huis en aan het papier.  [nieuw]
- Status: hints klaar

## Somtype 7: Welke schrijfwijze is een schaal?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Welke schrijfwijze is een schaal?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V10-schaal-lezen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “Bij een schaal staat er geen plusteken tussen de getallen.”)
- Voorbeelden:
  - `G7-VERH-01-claude-bank-005` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Welke schrijfwijze is een schaal?
    - **Opties:** A) 1 × 25 · B) 1 : 25 · C) 1 + 25
    - **Antwoord:** 1 : 25  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1 + 25 → Bij een schaal staat er geen plusteken tussen de getallen. · 1 × 25 → Bij een schaal staat er een ander teken tussen de twee getallen dan een maalteken.
    - **Uitleg (Claude):** Een schaal schrijf je met een dubbele punt tussen twee getallen. Vooraan staat de maat op de tekening, achteraan de echte maat. Daarom is 1 : 25 de schaal.

- **Hint 1 (te schrijven):** Een schaal is geen som: je rekent er niets mee uit. Welk teken past daarbij?
- **Hint 2 (te schrijven):** Een schaal schrijf je met een dubbele punt (:) tussen de twee getallen. Welke schrijfwijze heeft dat teken?
- **Ouderzin:** Je kind leert wat een schaal (zoals op een plattegrond) betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keersom` (1 × 25) → Dat is een keersom. Een schaal is geen som.  [nieuw]
  - `plussom` (1 + 25) → Dat is een plussom. Een schaal is geen som.  [nieuw]
  - `andere fout` (andere fout) → Een schaal is geen som.  [nieuw]
- Status: hints klaar
