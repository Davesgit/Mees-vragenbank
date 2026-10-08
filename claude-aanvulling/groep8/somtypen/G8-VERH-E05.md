# G8-VERH-E05 — Hoeveel procent erbij of eraf?

Onze omschrijving: % toename/afname/winst/verlies (ook >100%, lastige getallen + RM) · in onze bank: 8 items

Claude-vragen gemapt: **54** in **21** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een [ding] kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een [ding] kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?” (koppeling: claudeId)
- Items: **15** · Claude-doelen: T5 (15) · regel: G8-T5-procent-erbij
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (30)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat?”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-017` (Claude T5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kaart kostte €60 en kost nu €72. Met hoeveel procent is de prijs gestegen?
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** €12 → Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat? · €17 → Reken de stijging uit ten opzichte van de oude prijs, niet de nieuwe.
    - **Uitleg (Claude):** De stijging is 72 − 60 = 12. 12 van 60 is 20%.
  - `G8-VERH-E05-claude-bank-014` (Claude T5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een knuffel kostte €80 en kost nu €88. Met hoeveel procent is de prijs gestegen?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** €8 → Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat? · €9 → Reken de stijging uit ten opzichte van de oude prijs, niet de nieuwe.
    - **Uitleg (Claude):** De stijging is 88 − 80 = 8. 8 van 80 is 10%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: [wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T6 (8) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (8), komma-verschoven (8), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 6 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-047` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kind zet €400 op een spaarrekening met 4% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 416  (controle: ok)
    - **Fout-hints (Claude):** €16 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €560 → 1% van 400 is 4. · €384 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 4% van 400 = €16. Erbij: 400 + 16 = €416.
  - `G8-VERH-E05-claude-bank-049` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kind zet €300 op een spaarrekening met 4% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 312  (controle: ok)
    - **Fout-hints (Claude):** €12 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €420 → 1% van 300 is 3. · €288 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 4% van 300 = €12. Erbij: 300 + 12 = €312.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Vorig jaar waren er # [ding], nu #. Met hoeveel procent is dat gestegen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Vorig jaar waren er # [ding], nu #. Met hoeveel procent is dat gestegen?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: T5 (5) · regel: G8-T5-procent-erbij
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (10)
- Verschillende Claude-fout-hints: 5 (meest: “Vergelijk met het oude aantal (100%), niet met het nieuwe.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-044` (Claude T5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Vorig jaar waren er 20 eieren, nu 30. Met hoeveel procent is dat gestegen?
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 10 → 10 is de toename in aantal. De vraag is hoeveel procent dat van 20 is. · 33 → Vergelijk met het oude aantal (100%), niet met het nieuwe.
    - **Uitleg (Claude):** Erbij gekomen: 30 − 20 = 10. Dat vergelijk je met het oude aantal: 10 van 20 is 50%.
  - `G8-VERH-E05-claude-bank-041` (Claude T5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Vorig jaar waren er 40 wortels, nu 44. Met hoeveel procent is dat gestegen?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 4 → 4 is de toename in aantal. De vraag is hoeveel procent dat van 40 is. · 9 → Vergelijk met het oude aantal (100%), niet met het nieuwe.
    - **Uitleg (Claude):** Erbij gekomen: 44 − 40 = 4. Dat vergelijk je met het oude aantal: 4 van 40 is 10%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: T6 (3) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (3), komma-verschoven (3), verkeerde-bewerking (3)
- Verschillende Claude-fout-hints: 5 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-003` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Daan zet €1000 op een spaarrekening met 5% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 1050  (controle: ok)
    - **Fout-hints (Claude):** €50 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €1500 → 1% van 1000 is 10. · €950 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 5% van 1000 = €50. Erbij: 1000 + 50 = €1050.
  - `G8-VERH-E05-claude-bank-001` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Daan zet €400 op een spaarrekening met 2% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 408  (controle: ok)
    - **Fout-hints (Claude):** €8 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €480 → 1% van 400 is 4. · €392 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 2% van 400 = €8. Erbij: 400 + 8 = €408.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de bal nu?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de bal nu?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T5 (2) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), verkeerde-bewerking (2), procent-verkeerde-basis (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-020` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een bal kostte €120. De prijs stijgt met 10%. Wat kost de bal nu?
    - **Antwoord:** 132  (controle: ok)
    - **Fout-hints (Claude):** €12 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €108 → De prijs stijgt: erbij, niet eraf. · €130 → 10% is een deel van €120, niet €10.
    - **Uitleg (Claude):** 10% van 120 = 12. Erbij: 120 + 12 = €132.
  - `G8-VERH-E05-claude-bank-019` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een bal kostte €120. De prijs stijgt met 20%. Wat kost de bal nu?
    - **Antwoord:** 144  (controle: ok)
    - **Fout-hints (Claude):** €24 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €96 → De prijs stijgt: erbij, niet eraf. · €140 → 20% is een deel van €120, niet €20.
    - **Uitleg (Claude):** 20% van 120 = 24. Erbij: 120 + 24 = €144.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knuffel nu?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knuffel nu?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T5 (2) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), verkeerde-bewerking (2), procent-verkeerde-basis (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-022` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een knuffel kostte €40. De prijs stijgt met 5%. Wat kost de knuffel nu?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €38 → De prijs stijgt: erbij, niet eraf. · €45 → 5% is een deel van €40, niet €5.
    - **Uitleg (Claude):** 5% van 40 = 2. Erbij: 40 + 2 = €42.
  - `G8-VERH-E05-claude-bank-023` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een knuffel kostte €20. De prijs stijgt met 10%. Wat kost de knuffel nu?
    - **Antwoord:** 22  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €18 → De prijs stijgt: erbij, niet eraf. · €30 → 10% is een deel van €20, niet €10.
    - **Uitleg (Claude):** 10% van 20 = 2. Erbij: 20 + 2 = €22.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de steen nu?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de steen nu?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T5 (2) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), verkeerde-bewerking (2), procent-verkeerde-basis (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-025` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een knikker kostte €80. De prijs stijgt met 20%. Wat kost de steen nu?
    - **Antwoord:** 96  (controle: ok)
    - **Fout-hints (Claude):** €16 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €64 → De prijs stijgt: erbij, niet eraf. · €100 → 20% is een deel van €80, niet €20.
    - **Uitleg (Claude):** 20% van 80 = 16. Erbij: 80 + 16 = €96.
  - `G8-VERH-E05-claude-bank-026` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een knikker kostte €20. De prijs stijgt met 10%. Wat kost de steen nu?
    - **Antwoord:** 22  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €18 → De prijs stijgt: erbij, niet eraf. · €30 → 10% is een deel van €20, niet €10.
    - **Uitleg (Claude):** 10% van 20 = 2. Erbij: 20 + 2 = €22.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het ei nu?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het ei nu?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T5 (2) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), procent-verkeerde-basis (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-032` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een ei kostte €200. De prijs stijgt met 25%. Wat kost het ei nu?
    - **Antwoord:** 250  (controle: ok)
    - **Fout-hints (Claude):** €50 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €150 → De prijs stijgt: erbij, niet eraf. · €225 → 25% is een deel van €200, niet €25.
    - **Uitleg (Claude):** 25% van 200 = 50. Erbij: 200 + 50 = €250.
  - `G8-VERH-E05-claude-bank-031` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een ei kostte €120. De prijs stijgt met 50%. Wat kost het ei nu?
    - **Antwoord:** 180  (controle: ok)
    - **Fout-hints (Claude):** €60 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €170 → 50% is een deel van €120, niet €50.
    - **Uitleg (Claude):** 50% van 120 = 60. Erbij: 120 + 60 = €180.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Milan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Milan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T6 (2) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), komma-verschoven (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-038` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Milan zet €200 op een spaarrekening met 3% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 206  (controle: ok)
    - **Fout-hints (Claude):** €6 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €260 → 1% van 200 is 2. · €194 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 3% van 200 = €6. Erbij: 200 + 6 = €206.
  - `G8-VERH-E05-claude-bank-037` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Milan zet €300 op een spaarrekening met 3% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 309  (controle: ok)
    - **Fout-hints (Claude):** €9 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €390 → 1% van 300 is 3. · €291 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 3% van 300 = €9. Erbij: 300 + 9 = €309.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T6 (2) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (2), komma-verschoven (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-039` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sanne zet €1500 op een spaarrekening met 2% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 1530  (controle: ok)
    - **Fout-hints (Claude):** €30 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €1800 → 1% van 1500 is 15. · €1470 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 2% van 1500 = €30. Erbij: 1500 + 30 = €1530.
  - `G8-VERH-E05-claude-bank-040` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sanne zet €200 op een spaarrekening met 3% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 206  (controle: ok)
    - **Fout-hints (Claude):** €6 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €260 → 1% van 200 is 2. · €194 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 3% van 200 = €6. Erbij: 200 + 6 = €206.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knoop nu?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knoop nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-021` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een schrift kostte €80. De prijs stijgt met 5%. Wat kost de knoop nu?
    - **Antwoord:** 84  (controle: ok)
    - **Fout-hints (Claude):** €4 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €76 → De prijs stijgt: erbij, niet eraf. · €85 → 5% is een deel van €80, niet €5.
    - **Uitleg (Claude):** 5% van 80 = 4. Erbij: 80 + 4 = €84.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de stap nu?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de stap nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-024` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een bal kostte €40. De prijs stijgt met 5%. Wat kost de stap nu?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €38 → De prijs stijgt: erbij, niet eraf. · €45 → 5% is een deel van €40, niet €5.
    - **Uitleg (Claude):** 5% van 40 = 2. Erbij: 40 + 2 = €42.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 13: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de sticker nu?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de sticker nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-027` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een sticker kostte €80. De prijs stijgt met 25%. Wat kost de sticker nu?
    - **Antwoord:** 100  (controle: ok)
    - **Fout-hints (Claude):** €20 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €60 → De prijs stijgt: erbij, niet eraf. · €105 → 25% is een deel van €80, niet €25.
    - **Uitleg (Claude):** 25% van 80 = 20. Erbij: 80 + 20 = €100.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 14: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de trui nu?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de trui nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-028` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een trui kostte €40. De prijs stijgt met 5%. Wat kost de trui nu?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €38 → De prijs stijgt: erbij, niet eraf. · €45 → 5% is een deel van €40, niet €5.
    - **Uitleg (Claude):** 5% van 40 = 2. Erbij: 40 + 2 = €42.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 15: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de wortel nu?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de wortel nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-029` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een wortel kostte €120. De prijs stijgt met 25%. Wat kost de wortel nu?
    - **Antwoord:** 150  (controle: ok)
    - **Fout-hints (Claude):** €30 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €90 → De prijs stijgt: erbij, niet eraf. · €145 → 25% is een deel van €120, niet €25.
    - **Uitleg (Claude):** 25% van 120 = 30. Erbij: 120 + 30 = €150.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 16: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het bot nu?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het bot nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-030` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een bot kostte €40. De prijs stijgt met 10%. Wat kost het bot nu?
    - **Antwoord:** 44  (controle: ok)
    - **Fout-hints (Claude):** €4 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €36 → De prijs stijgt: erbij, niet eraf. · €50 → 10% is een deel van €40, niet €10.
    - **Uitleg (Claude):** 10% van 40 = 4. Erbij: 40 + 4 = €44.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 17: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het kaartje nu?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het kaartje nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-033` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kaartje kostte €60. De prijs stijgt met 10%. Wat kost het kaartje nu?
    - **Antwoord:** 66  (controle: ok)
    - **Fout-hints (Claude):** €6 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €54 → De prijs stijgt: erbij, niet eraf. · €70 → 10% is een deel van €60, niet €10.
    - **Uitleg (Claude):** 10% van 60 = 6. Erbij: 60 + 6 = €66.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 18: Een winkel verkoopt in week # [ding] broden en in week # [ding] broden. Met hoeveel procent is de verkoop gedaald?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Een winkel verkoopt in week # [ding] broden en in week # [ding] broden. Met hoeveel procent is de verkoop gedaald?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VERH
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “20 is het verschil in broden. Je moet dat verschil nog vergelijken met het beginaantal.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-054` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Een winkel verkoopt in week 1 zeventig broden en in week 2 vijftig broden. Met hoeveel procent is de verkoop gedaald?
    - **Opties:** A) 40 procent · B) Ongeveer 29 procent · C) 20 procent
    - **Antwoord:** Ongeveer 29 procent  (controle: n.v.t.)
    - **Fout-hints (Claude):** 20 procent → 20 is het verschil in broden. Je moet dat verschil nog vergelijken met het beginaantal. · 40 procent → Je vergelijkt met het nieuwe aantal. Bij een daling reken je met het begingetal.
    - **Uitleg (Claude):** Het verschil is 70 − 50 = 20 broden. Je vergelijkt 20 met het begingetal 70. 20 van de 70 is ongeveer 29 procent.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 19: Een zak noten kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Een zak noten kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (2)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat?”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-034` (Claude T5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een zak noten kostte €40 en kost nu €60. Met hoeveel procent is de prijs gestegen?
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** €20 → Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat? · €33 → Reken de stijging uit ten opzichte van de oude prijs, niet de nieuwe.
    - **Uitleg (Claude):** De stijging is 60 − 40 = 20. 20 van 40 is 50%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 20: Een zak noten kostte €#. De prijs stijgt met #%. Wat kost de noot nu?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Een zak noten kostte €#. De prijs stijgt met #%. Wat kost de noot nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T5 (1) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-035` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een zak noten kostte €200. De prijs stijgt met 10%. Wat kost de noot nu?
    - **Antwoord:** 220  (controle: ok)
    - **Fout-hints (Claude):** €20 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €180 → De prijs stijgt: erbij, niet eraf. · €210 → 10% is een deel van €200, niet €10.
    - **Uitleg (Claude):** 10% van 200 = 20. Erbij: 200 + 20 = €220.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 21: Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: T6 (1) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (1), komma-verschoven (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-036` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Fatima zet €2000 op een spaarrekening met 1% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 2020  (controle: ok)
    - **Fout-hints (Claude):** €20 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €2200 → 1% van 2000 is 20. · €1980 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 1% van 2000 = €20. Erbij: 2000 + 20 = €2020.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
