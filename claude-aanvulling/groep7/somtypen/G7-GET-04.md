# G7-GET-04 — Vermenigvuldigen en delen

Onze omschrijving: Vermenigvuldigen/delen + combinaties · in onze bank: 8 items

Claude-vragen gemapt: **896** in **11** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # : # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# : # =” (koppeling: claudeId)
- Items: **416** · Claude-doelen: B17 (385), C18 (31) · regel: G7-K02-komma-delen, G7-C01-staartdeling
- Getallenruimte: 0–1.000, 0–10.000, kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (633), komma-verschoven (118), tiental-ernaast (28), een-ernaast (25), verkeerde-bewerking (19), deel-vergeten-bij-splitsen (9)
- Verschillende Claude-fout-hints: 6 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-276` (Claude B17, bank, niveau 3 → toepassen)
    - **Opgave:** 0,6 : 3 =
    - **Antwoord:** 0,2  (controle: ok)
    - **Fout-hints (Claude):** 0,02 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 0,21 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G7-GET-04-claude-bank-400` (Claude C18, bank, niveau 3 → toepassen)
    - **Opgave:** 1026 : 18 =
    - **Antwoord:** 57  (controle: ok)
    - **Fout-hints (Claude):** 67 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 47 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: # × # =

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **376** · Claude-doelen: B16 (376) · regel: G7-K01-komma-keer
- Getallenruimte: 0–1.000, kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (576), komma-verschoven (167), verkeerde-bewerking (9)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-833` (Claude B16, bank, niveau 3 → toepassen)
    - **Opgave:** 0,2 × 3 =
    - **Antwoord:** 0,6  (controle: ok)
    - **Fout-hints (Claude):** 0,7 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 0,61 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G7-GET-04-claude-bank-579` (Claude B16, bank, niveau 3 → toepassen)
    - **Opgave:** 2,09 × 5 =
    - **Antwoord:** 10,45  (controle: ok)
    - **Fout-hints (Claude):** 10,35 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 10,44 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: # [ding] worden verdeeld over # [ding]. Hoeveel krijgt [wie]? (Wat overblijft, blijft over.)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# [ding] worden verdeeld over # [ding]. Hoeveel krijgt [wie]? (Wat overblijft, blijft over.)” (koppeling: claudeId)
- Items: **32** · Claude-doelen: C19 (32) · regel: G7-C02-rest
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): rest-vergeten (32), deel-vergeten-bij-splitsen (32), andere-deel-genomen (32)
- Verschillende Claude-fout-hints: 42 (meest: “Tel alle stappen van de staartdeling bij elkaar op.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-435` (Claude C19, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 400 tanden worden verdeeld over 3 dino's. Hoeveel krijgt elke dino? (Wat overblijft, blijft over.)
    - **Antwoord:** 133  (controle: ok)
    - **Fout-hints (Claude):** 134 → 3 × 134 = 402, dat is meer dan 400. · 123 → Tel alle stappen van de staartdeling bij elkaar op. · 1 → 1 is de rest. Gevraagd is de uitkomst.
    - **Uitleg (Claude):** 3 × 133 = 399, en 400 − 399 = 1 over. Dus 133 rest 1.
  - `G7-GET-04-claude-bank-456` (Claude C19, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 3156 blaadjes worden verdeeld over 9 dino's. Hoeveel krijgt elke dino? (Wat overblijft, blijft over.)
    - **Antwoord:** 350  (controle: ok)
    - **Fout-hints (Claude):** 351 → 9 × 351 = 3159, dat is meer dan 3156. · 340 → Tel alle stappen van de staartdeling bij elkaar op. · 6 → 6 is de rest. Gevraagd is de uitkomst.
    - **Uitleg (Claude):** 9 × 350 = 3150, en 3156 − 3150 = 6 over. Dus 350 rest 6.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Prijs per stuk: # [ding] kosten samen €#. Hoeveel kost één?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Prijs per stuk: # [ding] kosten samen €#. Hoeveel kost één?” (koppeling: claudeId)
- Items: **31** · Claude-doelen: T7 (31) · regel: G8-T7-prijs-per-stuk
- Getallenruimte: kommagetallen (2 cijfers achter de komma) met € · type: kale
- Denkfouten (Claude): komma-verschoven (31), verkeerde-bewerking (31)
- Verschillende Claude-fout-hints: 2 (meest: “Let op de komma: de prijs per stuk is veel kleiner dan de prijs van de hele zak.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-terug-001` (Claude T7, gegenereerd, niveau 1 → basis)
    - **Opgave:** 8 kaartjes voor de bus kosten samen €28. Hoeveel kost één kaartje voor de bus?
    - **Antwoord:** €3,50  (controle: n.v.t.)
    - **Fout-hints (Claude):** €35 → Let op de komma: de prijs per stuk is veel kleiner dan de prijs van de hele zak. · €20 → Per stuk is delen, niet aftrekken.
    - **Uitleg (Claude):** €28 : 8 = €3,50 per bal.
  - `G7-GET-04-claude-bank-terug-017` (Claude T7, gegenereerd, niveau 1 → basis)
    - **Opgave:** 8 schriften kosten samen €44. Hoeveel kost één schrift?
    - **Antwoord:** €5,50  (controle: n.v.t.)
    - **Fout-hints (Claude):** €55 → Let op de komma: de prijs per stuk is veel kleiner dan de prijs van de hele zak. · €36 → Per stuk is delen, niet aftrekken.
    - **Uitleg (Claude):** €44 : 8 = €5,50 per poesje.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: # [ding] hebben #, #, #, #, # [ding]. Hoeveel [ding] hebben ze gemiddeld?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “# [ding] hebben #, #, #, #, # [ding]. Hoeveel [ding] hebben ze gemiddeld?” (koppeling: claudeId)
- Items: **11** · Claude-doelen: G6 (11) · regel: G7-D03-gemiddelde, D-MEDIAAN-NAAR-GEMIDDELDE
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (11), verhoudingstabel-verkeerd (6), middelste-getal (5), totaal-niet-gedeeld (5)
- Verschillende Claude-fout-hints: 9 (meest: “Dat is het middelste getal. Gemiddeld is optellen en delen.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-427` (Claude G6, gegenereerd, niveau 1 → basis)
    - **Opgave:** 5 dino's hebben 15, 11, 12, 9, 13 eieren. Hoeveel eieren hebben ze gemiddeld?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 60 → 60 is het totaal. Voor het gemiddelde deel je door 5. · 15 → Het zijn 5 dino's, dus deel door 5.
    - **Uitleg (Claude):** Tel op: 15 + 11 + 12 + 9 + 13 = 60. Deel door 5: 60 : 5 = 12.
  - `G7-GET-04-claude-bank-862` (Claude G6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 5 dino's hebben 18, 13, 2, 13, 9 blaadjes. Hoeveel blaadjes hebben ze gemiddeld?
    - **Antwoord:** 11  (controle: ok)
    - **Fout-hints (Claude):** 13 → Dat is het middelste getal. Gemiddeld betekent eerlijk verdelen: tel alles op en deel door 5. · 55 → Dat is het totaal. Verdeel het nog eerlijk over de 5.
    - **Uitleg (Claude):** 18 + 13 + 2 + 13 + 9 = 55. 55 : 5 = 11.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: # [ding] gaan in [bakken] van #. Hoeveel blijven er over?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] gaan in [bakken] van #. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C19 (8) · regel: G7-C02-rest
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): rest-vergeten (16)
- Verschillende Claude-fout-hints: 12 (meest: “Dan past er nog een doos van 18 bij. De rest is altijd kleiner dan 18.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-423` (Claude C19, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 1367 stappen gaan in dozen van 18. Hoeveel stappen blijven er over?
    - **Antwoord:** 17  (controle: ok)
    - **Fout-hints (Claude):** 75 → 75 is het aantal dozen. De vraag is hoeveel er óverblijft. · 35 → Dan past er nog een doos van 18 bij. De rest is altijd kleiner dan 18.
    - **Uitleg (Claude):** 18 × 75 = 1350, dat past nog. 1367 − 1350 = 17 over.
  - `G7-GET-04-claude-bank-422` (Claude C19, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 689 veren gaan in dozen van 31. Hoeveel veren blijven er over?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 22 → 22 is het aantal dozen. De vraag is hoeveel er óverblijft. · 38 → Dan past er nog een doos van 31 bij. De rest is altijd kleiner dan 31.
    - **Uitleg (Claude):** 31 × 22 = 682, dat past nog. 689 − 682 = 7 over.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: # kilo/liter [ding] wordt eerlijk verdeeld over # [wie]. Hoeveel krijgt elk(e) [wie]?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# kilo/liter [ding] wordt eerlijk verdeeld over # [wie]. Hoeveel krijgt elk(e) [wie]?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B17 (8) · regel: G7-K02-komma-delen
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma), kommagetallen (3 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (4), tafelbuur (4), rest-vergeten (4), kommagetal-als-geheel (4)
- Verschillende Claude-fout-hints: 12 (meest: “Komma terugzetten: het antwoord heeft één cijfer achter de komma.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-473` (Claude B17, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 4,5 liter water wordt eerlijk verdeeld over 3 tanden. Hoeveel liter krijgt elke tand?
    - **Antwoord:** 1,5  (controle: ok)
    - **Fout-hints (Claude):** 15 → Komma terugzetten: het antwoord heeft één cijfer achter de komma. · 2,5 → Controleer. 3 × jouw antwoord moet 4,5 zijn.
    - **Uitleg (Claude):** Reken zonder komma: 45 : 3 = 15. Zet de komma terug: 1,5.
  - `G7-GET-04-claude-bank-471` (Claude B17, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 241 kilo eieren wordt eerlijk verdeeld over 8 dino's. Hoeveel kilo krijgt elke dino?
    - **Antwoord:** 30,125  (controle: ok)
    - **Fout-hints (Claude):** 30 → Er blijft 1 kilo over. Die verdeel je ook, in stukjes. · 30,1 → De rest 1 is niet zomaar het cijfer achter de komma. Deel de rest ook door 8.
    - **Uitleg (Claude):** 8 × 30 = 240, blijft 1 over. 1 : 8 = 0,125. Samen 30,125.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel krijgt [wie]?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel krijgt [wie]?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C18 (4) · regel: G7-C01-staartdeling
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (8), nul-fout-tientallen (4)
- Verschillende Claude-fout-hints: 12 (meest: “Controleer. 21 × 118 is meer dan 2268.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-432` (Claude C18, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 2268 blaadjes worden eerlijk verdeeld over 21 dino's. Hoeveel krijgt elke dino?
    - **Antwoord:** 108  (controle: ok)
    - **Fout-hints (Claude):** 118 → Controleer. 21 × 118 is meer dan 2268. · 98 → Controleer. 21 × 98 is minder dan 2268. Er blijft dan te veel over. · 1080 → Schat eerst. 21 × 1080 is veel te veel.
    - **Uitleg (Claude):** Hap in stukken. 21 × 100 = 2100: dat past 1 keer. Dan wat overblijft in kleinere happen. Samen 108 keer, dus 2268 : 21 = 108.
  - `G7-GET-04-claude-bank-434` (Claude C18, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 13.020 stickers worden eerlijk verdeeld over 35 kinderen. Hoeveel krijgt elk kind?
    - **Antwoord:** 372  (controle: ok)
    - **Fout-hints (Claude):** 382 → Controleer. 35 × 382 is meer dan 13.020. · 362 → Controleer. 35 × 362 is minder dan 13.020. Er blijft dan te veel over. · 3720 → Schat eerst. 35 × 3720 is veel te veel.
    - **Uitleg (Claude):** Hap in stukken. 35 × 100 = 3500: dat past 3 keer. Dan wat overblijft in kleinere happen. Samen 372 keer, dus 13.020 : 35 = 372.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Een [ding] weegt # gram. Hoeveel gram wegen # [ding]?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een [ding] weegt # gram. Hoeveel gram wegen # [ding]?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B16 (4) · regel: G7-K01-komma-keer
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (8), optellen-ipv-vermenigvuldigen (4)
- Verschillende Claude-fout-hints: 6 (meest: “Keer 10 of 100 maakt het getal groter: de komma gaat naar rechts.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-854` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Eén blaadje weegt 3,7 gram. Hoeveel gram wegen 100 blaadjes?
    - **Antwoord:** 370  (controle: ok)
    - **Fout-hints (Claude):** 0,037 → Keer 10 of 100 maakt het getal groter: de komma gaat naar rechts. · 3700 → Je hebt de komma te ver geschoven. Keer 10 is één plek, keer 100 twee plekken. · 103,7 → 100 blaadjes van elk 3,7 gram. Dat is een keersom.
    - **Uitleg (Claude):** Keer 100: de komma schuift twee plekken naar rechts. 3,7 × 100 = 370.
  - `G7-GET-04-claude-bank-851` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Eén poesje weegt 3,3 gram. Hoeveel gram wegen 100 poesjes?
    - **Antwoord:** 330  (controle: ok)
    - **Fout-hints (Claude):** 0,033 → Keer 10 of 100 maakt het getal groter: de komma gaat naar rechts. · 3300 → Je hebt de komma te ver geschoven. Keer 10 is één plek, keer 100 twee plekken. · 103,3 → 100 poesjes van elk 3,3 gram. Dat is een keersom.
    - **Uitleg (Claude):** Keer 100: de komma schuift twee plekken naar rechts. 3,3 × 100 = 330.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Een [ding] weegt # kg. Hoeveel wegen # [ding]?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een [ding] weegt # kg. Hoeveel wegen # [ding]?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B16 (4) · regel: G7-K01-komma-keer
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (4), deel-vergeten-bij-splitsen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Komma terugzetten: één cijfer achter de komma.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-857` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 2,6 kg. Hoeveel wegen 3 eieren?
    - **Antwoord:** 7,8  (controle: ok)
    - **Fout-hints (Claude):** 78 → Komma terugzetten: één cijfer achter de komma. · 6,6 → Ook de tienden gaan keer het aantal.
    - **Uitleg (Claude):** Zonder komma: 3 × 26 = 78. Komma terug (één cijfer): 7,8.
  - `G7-GET-04-claude-bank-858` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 3,9 kg. Hoeveel wegen 12 poesjes?
    - **Antwoord:** 46,8  (controle: ok)
    - **Fout-hints (Claude):** 468 → Komma terugzetten: één cijfer achter de komma. · 36,9 → Ook de tienden gaan keer het aantal.
    - **Uitleg (Claude):** Zonder komma: 12 × 39 = 468. Komma terug (één cijfer): 46,8.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: In [plek] staan # [ding] met elk # [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “In [plek] staan # [ding] met elk # [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C15 (2) · regel: G7-C05-keer
- Getallenruimte: 0–100.000 · type: kale
- Uit de G6-park: 2 items
- Denkfouten (Claude): deel-vergeten-bij-splitsen (4), onthouden-vergeten (2)
- Verschillende Claude-fout-hints: 5 (meest: “Controleer het optellen van de twee stukken. Een duizendtal te veel?”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-860` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op de kinderboerderij staan 32 kisten met elk 343 poesjes. Hoeveel poesjes zijn dat?
    - **Antwoord:** 10.976  (controle: ok)
    - **Fout-hints (Claude):** 10.290 → 343 × 30 is het grote stuk. Er komt nog 343 × 2 bij. · 10.292 → Ook het kleine stuk is een keersom. 343 × 2. · 11.976 → Controleer het optellen van de twee stukken. Een duizendtal te veel?
    - **Uitleg (Claude):** Splits 32 in 30 en 2. 343 × 30 = 10.290. 343 × 2 = 686. Samen 10.290 + 686 = 10.976.
  - `G7-GET-04-claude-bank-859` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** In de klas staan 34 kisten met elk 364 pakken. Hoeveel pakken zijn dat?
    - **Antwoord:** 12.376  (controle: ok)
    - **Fout-hints (Claude):** 10.920 → 364 × 30 is het grote stuk. Er komt nog 364 × 4 bij. · 10.924 → Ook het kleine stuk is een keersom. 364 × 4. · 13.376 → Controleer het optellen van de twee stukken. Een duizendtal te veel?
    - **Uitleg (Claude):** Splits 34 in 30 en 4. 364 × 30 = 10.920. 364 × 4 = 1456. Samen 10.920 + 1456 = 12.376.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
