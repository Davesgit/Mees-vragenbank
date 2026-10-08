# G7-VERH-02 — Procenten van een geheel

Onze omschrijving: % als deel–geheel · in onze bank: 8 items

Claude-vragen gemapt: **1030** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is #% van #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Hoeveel is #% van #?” (koppeling: claudeId)
- Items: **534** · Claude-doelen: V3 (375), V1 (159) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Uit de G6-park: 159 items
- Denkfouten (Claude): getal-overgenomen (456), andere-deel-genomen (357), nul-fout-tientallen (255)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-112` (Claude V1, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 25% van 112?
    - **Antwoord:** 28  (controle: ok)
    - **Fout-hints (Claude):** 280 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-239` (Claude V3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 40% van 335?
    - **Antwoord:** 134  (controle: ok)
    - **Fout-hints (Claude):** 295 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Hoeveel is #% van €#?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel is #% van €#?” (koppeling: claudeId)
- Items: **243** · Claude-doelen: V3 (243) · regel: G7-V05-procent-van
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): nul-fout-tientallen (246), getal-overgenomen (148), andere-deel-genomen (92)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-593` (Claude V3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 40% van €36?
    - **Antwoord:** €14,40  (controle: ok)
    - **Fout-hints (Claude):** €144 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · €1,44 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-582` (Claude V3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 15% van €48?
    - **Antwoord:** €7,20  (controle: ok)
    - **Fout-hints (Claude):** €0,72 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Hoeveel procent is # van #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoeveel procent is # van #?” (koppeling: claudeId)
- Items: **217** · Claude-doelen: V4 (217) · regel: G7-V06-hoeveel-procent
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): andere-deel-genomen (140), verhoudingstabel-verkeerd (108), getal-overgenomen (105), nul-fout-tientallen (81)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-988` (Claude V4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel procent is 1 van 20?
    - **Opties:** A) 95% · B) 5% · C) 50%
    - **Antwoord:** 5%  (controle: ok)
    - **Fout-hints (Claude):** 95% → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten? · 50% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-993` (Claude V4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel procent is 63 van 105?
    - **Opties:** A) 60% · B) 63% · C) 42%
    - **Antwoord:** 60%  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: In [plek] liggen # [ding]. #% ervan is rood. Hoeveel rode [ding] zijn er?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In [plek] liggen # [ding]. #% ervan is rood. Hoeveel rode [ding] zijn er?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: V1 (12) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Uit de G6-park: 12 items
- Denkfouten (Claude): deel-van-geheel-verkeerd (24), verkeerde-bewerking (12)
- Verschillende Claude-fout-hints: 21 (meest: “50% is de helft: delen door 2.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1010` (Claude V1, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het moeras liggen 48 stenen. 50% ervan is rood. Hoeveel rode stenen zijn er?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 12 → 50% is de helft: delen door 2. · 4.8 → Kijk goed. 50%, dus de helft van 48. · −2 → Procent is een deel van het geheel, niet iets wat je eraf haalt. 50% van 48 betekent de helft van 48.
    - **Uitleg (Claude):** 50% is de helft. 48 : 2 = 24.
  - `G7-VERH-02-claude-bank-1005` (Claude V1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de gymzaal liggen 120 stenen. 10% ervan is rood. Hoeveel rode stenen zijn er?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 60 → 10% is een tiende: delen door 10. · 30 → Kijk goed. 10%, dus een tiende van 120. · 110 → Procent is een deel van het geheel, niet iets wat je eraf haalt. 10% van 120 betekent een tiende van 120.
    - **Uitleg (Claude):** 10% is een tiende. 120 : 10 = 12.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: In [plek] zijn # [ding]. #% is beschadigd. Hoeveel [ding] zijn beschadigd?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] zijn # [ding]. #% is beschadigd. Hoeveel [ding] zijn beschadigd?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: V3 (12) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (12), procent-verkeerde-basis (12), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 14 (meest: “Procent is per honderd. Deel door 100, of ga via 10%.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1015` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de school zijn 80 knopen. 30% is beschadigd. Hoeveel knopen zijn beschadigd?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 8 → 8 is 10%. Je hebt 30% nodig, dus 3 keer zoveel. · 56 → Dat is het deel dat niet beschadigd is. De vraag is hoeveel wél. · 2400 → Procent is per honderd. Deel door 100, of ga via 10%.
    - **Uitleg (Claude):** Eerst 10%: 80 : 10 = 8. Dan 30% = 3 × 8 = 24.
  - `G7-VERH-02-claude-bank-1021` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het stadion zijn 160 truien. 75% is beschadigd. Hoeveel truien zijn beschadigd?
    - **Antwoord:** 120  (controle: ok)
    - **Fout-hints (Claude):** 16 → 16 is 10%. Je hebt 75% nodig, dus 7.5 keer zoveel. · 40 → Dat is het deel dat niet beschadigd is. De vraag is hoeveel wél. · 12.000 → Procent is per honderd. Deel door 100, of ga via 10%.
    - **Uitleg (Claude):** Eerst 10%: 160 : 10 = 16. Dan 75% = 7.5 × 16 = 120. (5% is de helft van 10%: 8.)

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Van de # [ding] hebben er # een [ding]. Hoeveel procent is dat?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Van de # [ding] hebben er # een [ding]. Hoeveel procent is dat?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: V4 (7) · regel: G7-V06-hoeveel-procent
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (7), verkeerde-bewerking (7), omgekeerd-gedeeld (5)
- Verschillende Claude-fout-hints: 8 (meest: “Dat is het aantal zonder. Zet om naar per 100.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1030` (Claude V4, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Van de 40 dino's hebben er 2 een blaadje. Hoeveel procent is dat?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 2 → 2 is het aantal, niet het percentage. Zet het om naar per 100. · 38 → Dat is het aantal zonder. Zet om naar per 100. · 20 → Deel het deel door het geheel, niet andersom.
    - **Uitleg (Claude):** Maak er 100 van: 40 → 100 is keer 2.5. 2 × 2.5 = 5. Dus 5%.
  - `G7-VERH-02-claude-bank-1028` (Claude V4, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Van de 20 eekhoorns hebben er 2 een noot. Hoeveel procent is dat?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 2 → 2 is het aantal, niet het percentage. Zet het om naar per 100. · 18 → Dat is het aantal zonder. Zet om naar per 100.
    - **Uitleg (Claude):** Maak er 100 van: 20 → 100 is keer 5. 2 × 5 = 10. Dus 10%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Een [ding] kost €#. Er is #% korting. Wat is de nieuwe prijs in euro's?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een [ding] kost €#. Er is #% korting. Wat is de nieuwe prijs in euro's?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: V5 (5) · regel: G7-V07-korting
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), procent-verkeerde-basis (5)
- Verschillende Claude-fout-hints: 7 (meest: “Korting gaat eraf, niet erbij.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-002` (Claude V5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bal kost €60. Er is 30% korting. Wat is de nieuwe prijs in euro's?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €18 → 18 is de korting. De vraag is wat je nog betaalt. · €30 → 30% is niet 30 euro. Reken eerst uit hoeveel 30% van 60 is. · €78 → Korting gaat eraf, niet erbij.
    - **Uitleg (Claude):** Korting: 30% van 60 = 18. Nieuwe prijs: 60 − 18 = €42.
  - `G7-VERH-02-claude-bank-003` (Claude V5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een wortel kost €60. Er is 50% korting. Wat is de nieuwe prijs in euro's?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** €10 → 50% is niet 50 euro. Reken eerst uit hoeveel 50% van 60 is. · €90 → Korting gaat eraf, niet erbij.
    - **Uitleg (Claude):** Korting: 50% van 60 = 30. Nieuwe prijs: 60 − 30 = €30.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
