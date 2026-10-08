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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

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

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
