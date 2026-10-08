# G8-GET-E02 — Schatten, bijstellen en je aanpak checken

Onze omschrijving: Schattend +/−/×÷ met correctie; procedures kritisch beoordelen · in onze bank: 8 items

Claude-vragen gemapt: **254** in **57** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Op welk cijfer eindigt # × #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Op welk cijfer eindigt # × #?” (koppeling: claudeId)
- Items: **53** · Claude-doelen: T3 (53) · regel: G8-T3-laatste-cijfer
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): plaatswaarde-verkeerd (36), een-ernaast (29), optellen-ipv-vermenigvuldigen (20), getal-overgenomen (15), tafelbuur (6)
- Verschillende Claude-fout-hints: 4 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-071` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Op welk cijfer eindigt 12 × 9?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G8-GET-E02-claude-bank-089` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Op welk cijfer eindigt 49 × 7?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Hoeveel is # + # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.

- Sleutel: nrOrigineel **51** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.” (koppeling: claudeId)
- Items: **30** · Claude-doelen: T3 (30) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-131` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 1100 + 8800 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 10.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9800 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 12.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-133` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 6350 + 6944 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 13.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 14.000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 20.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Hoeveel is # × # [ding]? Rond # af op honderdtallen en # op tientallen, en reken dan uit.

- Sleutel: nrOrigineel **52** · somtypeOrigineel “Hoeveel is # × # [ding]? Rond # af op honderdtallen en # op tientallen, en reken dan uit.” (koppeling: claudeId)
- Items: **29** · Claude-doelen: T3 (29) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-191` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 693 × 71 ongeveer? Rond 693 af op honderdtallen en 71 op tientallen, en reken dan uit.
    - **Antwoord:** 49.000  (controle: ok)
    - **Fout-hints (Claude):** 49.203 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 48.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-185` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 273 × 32 ongeveer? Rond 273 af op honderdtallen en 32 op tientallen, en reken dan uit.
    - **Antwoord:** 9000  (controle: ok)
    - **Fout-hints (Claude):** 9600 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 12.000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **53** · somtypeOrigineel “Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **26** · Claude-doelen: T3 (26) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-199` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 20 × 81 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 1600  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 1400 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G8-GET-E02-claude-bank-207` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 399 × 60 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 24.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 23.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 22.000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen?

- Sleutel: nrOrigineel **54** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen?” (koppeling: claudeId)
- Items: **19** · Claude-doelen: T3 (19) · regel: D8-KLOPPEN-MEERKEUZE-G8
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (11), laatste-cijfer (11), bovengrens (10), ondergrens (6)
- Verschillende Claude-fout-hints: 38 (meest: “Rond 179 naar beneden af. 100 × 8 is 800. De uitkomst kan dus niet kleiner zijn dan 800, en 432 is kleiner.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-255` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 179 × 8 kan kloppen?
    - **Opties:** A) 1432 · B) 432 · C) 187
    - **Antwoord:** 1432  (controle: n.v.t.)
    - **Fout-hints (Claude):** 432 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 187 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G8-GET-E02-claude-bank-245` (Claude T3, bank, niveau 2 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 339 × 3 kan kloppen?
    - **Opties:** A) 1017 · B) 1019 · C) 342
    - **Antwoord:** 1017  (controle: n.v.t.)
    - **Fout-hints (Claude):** 342 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit.

- Sleutel: nrOrigineel **55** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit.” (koppeling: claudeId)
- Items: **16** · Claude-doelen: T3 (16) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-163` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 194 + 813 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 1000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1007 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 1013 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-153` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 593 + 766 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 1400  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1359 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 1200 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Hoeveel is # − # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.

- Sleutel: nrOrigineel **56** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op duizendtallen en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-SCHAT-AFSPRAAK-G8
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-227` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 8800 − 1100 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 8000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7700 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 7000 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-228` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 6931 − 1940 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit.
    - **Antwoord:** 5000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4991 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 7000 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: In [plek] liggen # [ding] en er komen # bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding] en er komen # bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): afronden-verkeerde-kant (16), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is precies. Hier vragen we de schatting met ronde getallen.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-023` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het nest liggen 2640 schelpen en er komen 1536 bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.
    - **Antwoord:** 5000  (controle: ok)
    - **Fout-hints (Claude):** 4176 → Dat is precies. Hier vragen we de schatting met ronde getallen. · 6000 → Kijk per getal naar de honderdtallen: onder de 500 rond je naar beneden af. · 4000 → Kijk per getal naar de honderdtallen: vanaf 500 rond je naar boven af.
    - **Uitleg (Claude):** 2640 is ongeveer 3000, 1536 ongeveer 2000. Samen 5000. Precies is het 4176.
  - `G8-GET-E02-claude-bank-024` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Op de kinderboerderij liggen 2839 noten en er komen 2672 bij. Schat het totaal: rond beide getallen af op duizendtallen en tel op.
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 5511 → Dat is precies. Hier vragen we de schatting met ronde getallen. · 7000 → Kijk per getal naar de honderdtallen: onder de 500 rond je naar beneden af. · 5000 → Kijk per getal naar de honderdtallen: vanaf 500 rond je naar boven af.
    - **Uitleg (Claude):** 2839 is ongeveer 3000, 2672 ongeveer 3000. Samen 6000. Precies is het 5511.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?

- Sleutel: nrOrigineel **57** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-MEERKEUZE-G8
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): laatste-cijfer (7), orde-van-grootte (5), bovengrens (4)
- Verschillende Claude-fout-hints: 16 (meest: “Rond allebei naar boven af. 400 + 800 is 1200. De uitkomst kan dus niet groter zijn dan 1200, en 2069 is groter.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-233` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 360 + 709 kan kloppen?
    - **Opties:** A) 1069 · B) 2069 · C) 1071
    - **Antwoord:** 1069  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2069 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G8-GET-E02-claude-bank-229` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 737 + 776 kan kloppen?
    - **Opties:** A) 1513 · B) 2513 · C) 1511
    - **Antwoord:** 1513  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2513 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Ongeveer hoeveel is # × #? Rond # af op honderdtallen en # op tientallen, en reken dan uit.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Ongeveer hoeveel is # × #? Rond # af op honderdtallen en # op tientallen, en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (16), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 9 (meest: “Een nul te veel. Tel de nullen van beide ronde getallen.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-054` (Claude T3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Ongeveer hoeveel is 483 × 15? Rond 483 af op honderdtallen en 15 op tientallen, en reken dan uit.
    - **Antwoord:** 10.000  (controle: ok)
    - **Fout-hints (Claude):** 1000 → Tel de nullen. 500 en 20 hebben er samen 3. · 100.000 → Een nul te veel. Tel de nullen van beide ronde getallen. · 7245 → Dat is precies uitgerekend. Hier vragen we een schatting met de ronde getallen.
    - **Uitleg (Claude):** 483 is ongeveer 500, 15 is ongeveer 20. 500 × 20 = 10.000. Het echte antwoord (7245) ligt daar dichtbij.
  - `G8-GET-E02-claude-bank-056` (Claude T3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Ongeveer hoeveel is 138 × 12? Rond 138 af op honderdtallen en 12 op tientallen, en reken dan uit.
    - **Antwoord:** 1000  (controle: ok)
    - **Fout-hints (Claude):** 100 → Tel de nullen. 100 en 10 hebben er samen 3. · 10.000 → Een nul te veel. Tel de nullen van beide ronde getallen. · 1656 → Dat is precies uitgerekend. Hier vragen we een schatting met de ronde getallen.
    - **Uitleg (Claude):** 138 is ongeveer 100, 12 is ongeveer 10. 100 × 10 = 1000. Het echte antwoord (1656) ligt daar dichtbij.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: # [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.” (koppeling: claudeId)
- Items: **3** · Claude-doelen: T3 (3) · regel: G8-T3-schatten-afspraak
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (3), nul-fout-tientallen (3), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 7 (meest: “Precies uitgerekend. Hier vragen we de schatting met het ronde getal.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-002` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 5 dozen met elk 497 tanden. Schat hoeveel dat ongeveer is: rond 497 af op honderdtallen en reken dan uit.
    - **Antwoord:** 2500  (controle: ok)
    - **Fout-hints (Claude):** 2485 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 250 → 500 × 5: tel de nullen goed. · 505 → 5 dozen van elk ongeveer 500: dat is een keersom.
    - **Uitleg (Claude):** 497 is bijna 500. 500 × 5 = 2500. Precies is het 2485, dus de schatting klopt goed.
  - `G8-GET-E02-claude-bank-004` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 5 dozen met elk 297 stickers. Schat hoeveel dat ongeveer is: rond 297 af op honderdtallen en reken dan uit.
    - **Antwoord:** 1500  (controle: ok)
    - **Fout-hints (Claude):** 1485 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 150 → 300 × 5: tel de nullen goed. · 305 → 5 dozen van elk ongeveer 300: dat is een keersom.
    - **Uitleg (Claude):** 297 is bijna 300. 300 × 5 = 1500. Precies is het 1485, dus de schatting klopt goed.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: 's Ochtends is het # graden en 's middags # graden. Hoe reken je uit hoeveel graden het warmer is geworden?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “'s Ochtends is het # graden en 's middags # graden. Hoe reken je uit hoeveel graden het warmer is geworden?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een verschil is hoeveel het gestegen is. Wordt de uitkomst dan groter of juist kleiner dan 11?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-005` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** 's Ochtends is het 3 graden en 's middags 11 graden. Hoe reken je uit hoeveel graden het warmer is geworden?
    - **Opties:** A) Neem het getal 11 over als verschil · B) Trek 3 van 11 af · C) Tel 3 en 11 bij elkaar op
    - **Antwoord:** Trek 3 van 11 af  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 3 en 11 bij elkaar op → Een verschil is hoeveel het gestegen is. Wordt de uitkomst dan groter of juist kleiner dan 11? · Neem het getal 11 over als verschil → De ochtendtemperatuur was niet 0 graden. Die moet je meenemen als je het verschil uitrekent.
    - **Uitleg (Claude):** Het verschil vind je door de laagste temperatuur van de hoogste af te trekken. 11 min 3 is 8. De temperatuur is dus 8 graden gestegen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 13: Bas koopt # [ding] sap van €#. Hij krijgt €# als antwoord. Wat laat zien dat dit niet klopt?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Bas koopt # [ding] sap van €#. Hij krijgt €# als antwoord. Wat laat zien dat dit niet klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (2 cijfers achter de komma) met € · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Schat eerst met een rond bedrag: hoeveel is 6 keer 2 euro ongeveer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-006` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Bas koopt 6 pakken sap van €1,99. Hij krijgt €119,40 als antwoord. Wat laat zien dat dit niet klopt?
    - **Opties:** A) Het klopt, want 6 × 1,99 is bijna 120 · B) 6 pakken kosten ongeveer €12 · C) Het antwoord moet ongeveer €1200 zijn
    - **Antwoord:** 6 pakken kosten ongeveer €12  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het antwoord moet ongeveer €1200 zijn → Schat eerst met een rond bedrag: hoeveel is 6 keer 2 euro ongeveer? · Het klopt, want 6 × 1,99 is bijna 120 → Kijk goed waar de komma staat in €1,99. Eén pak kost nog geen 2 euro.
    - **Uitleg (Claude):** €1,99 is bijna €2. Zes keer 2 euro is ongeveer 12 euro. Een uitkomst van meer dan 100 euro kan dus niet kloppen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 14: Bij een spel krijg je # [ding] voor elk doelpunt. Voor elke misser gaat er # [ding] af. Hoe reken je de score uit?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Bij een spel krijg je # [ding] voor elk doelpunt. Voor elke misser gaat er # [ding] af. Hoe reken je de score uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Elk doelpunt levert 3 punten op. Hoe reken je hetzelfde aantal punten per keer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-007` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Bij een spel krijg je 3 punten voor elk doelpunt. Voor elke misser gaat er 1 punt af. Hoe reken je de score uit?
    - **Opties:** A) Doelpunten plus 3, dan het aantal missers eraf. · B) Doelpunten maal 3, dan het aantal missers erbij. · C) Doelpunten maal 3, dan het aantal missers eraf.
    - **Antwoord:** Doelpunten maal 3, dan het aantal missers eraf.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Doelpunten plus 3, dan het aantal missers eraf. → Elk doelpunt levert 3 punten op. Hoe reken je hetzelfde aantal punten per keer? · Doelpunten maal 3, dan het aantal missers erbij. → Een misser is niet goed voor je score. Wordt het totaal dan groter of kleiner?
    - **Uitleg (Claude):** Per doelpunt krijg je 3 punten, dus vermenigvuldig je het aantal doelpunten met 3. Elke misser kost 1 punt. Die missers haal je van het totaal af.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 15: Bram heeft # [ding] met # [ding]. Hij rekent uit dat er # [ding] zijn. Wat laat zien dat dit niet kan?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Bram heeft # [ding] met # [ding]. Hij rekent uit dat er # [ding] zijn. Wat laat zien dat dit niet kan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Lees nog eens: er zijn 12 zakjes met elk 15 knikkers. Wat doe je dan met die getallen?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-008` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Bram heeft 12 zakjes met 15 knikkers. Hij rekent uit dat er 27 knikkers zijn. Wat laat zien dat dit niet kan?
    - **Opties:** A) Eén zakje heeft al 15, dus 12 zakjes zijn veel meer · B) Niets, 12 en 15 samen is inderdaad 27 · C) Hij had 12 : 15 moeten doen
    - **Antwoord:** Eén zakje heeft al 15, dus 12 zakjes zijn veel meer  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 12 en 15 samen is inderdaad 27 → Lees nog eens: er zijn 12 zakjes met elk 15 knikkers. Wat doe je dan met die getallen? · Hij had 12 : 15 moeten doen → Delen maakt het aantal juist kleiner. Bij groepen van evenveel spullen kies je iets anders.
    - **Uitleg (Claude):** Bij 12 groepen van 15 hoort een vermenigvuldiging. Het antwoord moet dus veel groter zijn dan 15. Een snelle schatting laat zien dat 27 onmogelijk is.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 16: De trein vertrekt om #:# en komt aan om #:#. Hoe reken je handig uit hoe lang de reis duurt?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “De trein vertrekt om #:# en komt aan om #:#. Hoe reken je handig uit hoe lang de reis duurt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een uur heeft 60 minuten, niet 100. Werk in stappen naar een heel uur toe.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-009` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** De trein vertrekt om 14:35 en komt aan om 16:10. Hoe reken je handig uit hoe lang de reis duurt?
    - **Opties:** A) Reken eerst tot 15:00, dan verder tot 16:10. · B) Trek 35 van 10 af en tel de uren erbij. · C) Tel de twee tijden bij elkaar op.
    - **Antwoord:** Reken eerst tot 15:00, dan verder tot 16:10.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Trek 35 van 10 af en tel de uren erbij. → Een uur heeft 60 minuten, niet 100. Werk in stappen naar een heel uur toe. · Tel de twee tijden bij elkaar op. → Je zoekt het verschil tussen vertrek en aankomst, niet een som.
    - **Uitleg (Claude):** Bij tijd reken je handig met stappen naar een heel uur. Van 14:35 naar 15:00 is 25 minuten. Daarna nog 1 uur en 10 minuten, samen 1 uur en 35 minuten.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 17: Een [ding] is # m lang en # m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent # + # + # + # = #. Wat is er fout aan haar aanpak?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent # + # + # + # = #. Wat is er fout aan haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (2)
- Verschillende Claude-fout-hints: 2 (meest: “Denk aan tegels van 1 bij 1 meter op de bodem. Hoe tel je die het handigst?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-010` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een zwembad is 25 m lang en 10 m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent 25 + 10 + 25 + 10 = 70. Wat is er fout aan haar aanpak?
    - **Opties:** A) Ze rekende de omtrek in plaats van de oppervlakte · B) Niets, 70 vierkante meter klopt · C) Ze moest 25 + 10 doen en dat verdubbelen
    - **Antwoord:** Ze rekende de omtrek in plaats van de oppervlakte  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 70 vierkante meter klopt → Denk aan tegels van 1 bij 1 meter op de bodem. Hoe tel je die het handigst? · Ze moest 25 + 10 doen en dat verdubbelen → Dat geeft weer de lengte van de rand. De vraag gaat over het vlak binnen de rand.
    - **Uitleg (Claude):** Rondom optellen geeft de omtrek. Voor oppervlakte doe je lengte keer breedte: 25 × 10 = 250. De uitkomst is dus 250 vierkante meter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 18: Een [ding] is # m lang en # m breed. Je legt tegels van # vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Je legt tegels van # vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je legt tegels op de hele vloer, niet alleen langs de randen. Denk aan het vlak.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-011` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Een kamer is 5 m lang en 3 m breed. Je legt tegels van 1 vierkante meter. Hoe reken je uit hoeveel tegels je nodig hebt?
    - **Opties:** A) Lengte en breedte bij elkaar optellen · B) Lengte keer breedte doen, dat is het aantal · C) Alle zijden bij elkaar optellen
    - **Antwoord:** Lengte keer breedte doen, dat is het aantal  (controle: n.v.t.)
    - **Fout-hints (Claude):** Alle zijden bij elkaar optellen → Je legt tegels op de hele vloer, niet alleen langs de randen. Denk aan het vlak. · Lengte en breedte bij elkaar optellen → Tel eens hoeveel tegels er in één rij liggen en hoeveel rijen er zijn.
    - **Uitleg (Claude):** De vloer bestaat uit 3 rijen van 5 tegels. Dat zijn 5 keer 3 tegels. Bij een vlak vermenigvuldig je de lengte met de breedte.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 19: Een [ding] is # m lang en # m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent # × # = #. Wat is er fout aan zijn aanpak?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een [ding] is # m lang en # m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent # × # = #. Wat is er fout aan zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een hek gaat langs alle vier de zijden. Keersommen horen bij het vlak binnen de tuin.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-012` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een tuin is 8 m lang en 5 m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent 8 × 5 = 40. Wat is er fout aan zijn aanpak?
    - **Opties:** A) Hij had 8 + 5 moeten doen · B) Hij rekende de oppervlakte in plaats van de omtrek · C) Hij had 8 × 5 × 2 moeten doen
    - **Antwoord:** Hij rekende de oppervlakte in plaats van de omtrek  (controle: n.v.t.)
    - **Fout-hints (Claude):** Hij had 8 × 5 × 2 moeten doen → Een hek gaat langs alle vier de zijden. Keersommen horen bij het vlak binnen de tuin. · Hij had 8 + 5 moeten doen → Je bent nu maar langs twee zijden gelopen. Hoeveel zijden heeft de tuin?
    - **Uitleg (Claude):** Voor een hek tel je alle zijden op: 8 + 5 + 8 + 5 = 26 meter. Met 8 × 5 bereken je hoeveel vierkante meter de tuin groot is. Dat is iets anders.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 20: Een broek van €# wordt # procent goedkoper. Rik rekent uit dat de broek nu €# [ding]. Wat ging er mis?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Een broek van €# wordt # procent goedkoper. Rik rekent uit dat de broek nu €# [ding]. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Procent betekent 'van de honderd'. Reken eerst uit wat 10 procent van 40 is.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-013` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een broek van €40 wordt 10 procent goedkoper. Rik rekent uit dat de broek nu €30 kost. Wat ging er mis?
    - **Opties:** A) Hij haalde €10 eraf in plaats van 10 procent · B) Niets, 10 procent van €40 is €10 · C) Hij moest €10 bij de prijs optellen
    - **Antwoord:** Hij haalde €10 eraf in plaats van 10 procent  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 10 procent van €40 is €10 → Procent betekent 'van de honderd'. Reken eerst uit wat 10 procent van 40 is. · Hij moest €10 bij de prijs optellen → Goedkoper worden betekent dat de prijs daalt. Wat doe je dan met het kortingsbedrag?
    - **Uitleg (Claude):** 10 procent van €40 is €4, niet €10. De nieuwe prijs is dus €36. Rik verwarde procenten met euro's.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 21: Een jas van €# [ding] # procent in prijs omlaag. Milou rekent uit dat de jas nu €# [ding]. Wat ging er mis?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Een jas van €# [ding] # procent in prijs omlaag. Milou rekent uit dat de jas nu €# [ding]. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het percentage hoort bij de oude prijs van de jas, niet bij je tussenantwoord.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-014` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een jas van €60 gaat 25 procent in prijs omlaag. Milou rekent uit dat de jas nu €15 kost. Wat ging er mis?
    - **Opties:** A) €15 is de korting, niet de nieuwe prijs · B) Ze moest 25 procent van 15 nemen · C) De jas kost nu €35
    - **Antwoord:** €15 is de korting, niet de nieuwe prijs  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze moest 25 procent van 15 nemen → Het percentage hoort bij de oude prijs van de jas, niet bij je tussenantwoord. · De jas kost nu €35 → Trek je korting netjes van de oude prijs af en reken het verschil nog eens na.
    - **Uitleg (Claude):** 25 procent van 60 is 15. Dat bedrag gaat eraf, dus de jas kost 60 − 15 = 45 euro. Lees na het rekenen altijd terug wat er gevraagd werd.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 22: Een recept voor # [ding] vraagt # gram rijst. Daan wil koken voor # [ding] en pakt # gram. Klopt zijn aanpak?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Een recept voor # [ding] vraagt # gram rijst. Daan wil koken voor # [ding] en pakt # gram. Klopt zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij een recept groeien de personen en de grammen in dezelfde verhouding mee.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-015` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Een recept voor 4 personen vraagt 300 gram rijst. Daan wil koken voor 8 personen en pakt 600 gram. Klopt zijn aanpak?
    - **Opties:** A) Nee, hij moest 304 gram nemen · B) Ja, hij verdubbelde beide getallen · C) Nee, hij moest 300 + 8 nemen
    - **Antwoord:** Ja, hij verdubbelde beide getallen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, hij moest 300 + 8 nemen → Bij een recept groeien de personen en de grammen in dezelfde verhouding mee. · Nee, hij moest 304 gram nemen → Kijk hoeveel keer zo groot de groep wordt en doe met de rijst hetzelfde.
    - **Uitleg (Claude):** Van 4 naar 8 personen is twee keer zo veel. Dan gaat ook de rijst twee keer zo veel: 2 × 300 is 600 gram. De verhouding blijft gelijk.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 23: Een recept voor # [ding] vraagt # gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor # [ding]?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “Een recept voor # [ding] vraagt # gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor # [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (2)
- Verschillende Claude-fout-hints: 2 (meest: “Personen en grammen zijn verschillende dingen. Zoek eerst hoeveel rijst één persoon nodig heeft.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-016` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Een recept voor 4 personen vraagt 200 gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor 6 personen?
    - **Opties:** A) Tel 200 en 6 bij elkaar op · B) Doe 200 keer 6 · C) Deel 200 door 4 en doe dat keer 6
    - **Antwoord:** Deel 200 door 4 en doe dat keer 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 200 en 6 bij elkaar op → Personen en grammen zijn verschillende dingen. Zoek eerst hoeveel rijst één persoon nodig heeft. · Doe 200 keer 6 → Zes personen eten niet zes keer zoveel als vier personen. Reken eerst per persoon.
    - **Uitleg (Claude):** Eén persoon krijgt 200 gedeeld door 4, dus 50 gram. Zes personen krijgen dan 6 keer 50 gram. Via één persoon rekenen werkt altijd.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 24: Een stadion heeft # [ding] met # [ding]. Anne schat vooraf ongeveer # [ding] en rekent daarna precies # uit. Wat zegt dit over haar aanpak?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Een stadion heeft # [ding] met # [ding]. Anne schat vooraf ongeveer # [ding] en rekent daarna precies # uit. Wat zegt dit over haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): afronden-verkeerde-kant (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een schatting is een ruwe benadering. Die hoeft niet precies gelijk te zijn aan de echte uitkomst.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-017` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Een stadion heeft 4 vakken met 1980 stoelen. Anne schat vooraf ongeveer 8000 stoelen en rekent daarna precies 7920 uit. Wat zegt dit over haar aanpak?
    - **Opties:** A) Haar schatting was fout, want 4 × 2000 is 800 · B) Haar schatting past goed bij het antwoord · C) Ze rekende fout, want het moet 8000 zijn
    - **Antwoord:** Haar schatting past goed bij het antwoord  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze rekende fout, want het moet 8000 zijn → Een schatting is een ruwe benadering. Die hoeft niet precies gelijk te zijn aan de echte uitkomst. · Haar schatting was fout, want 4 × 2000 is 800 → Reken 4 × 2000 nog eens rustig na en let op het aantal nullen.
    - **Uitleg (Claude):** 1980 is bijna 2000 en 4 × 2000 is 8000. De echte uitkomst 7920 ligt daar vlak onder. De schatting laat dus zien dat het antwoord klopt.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 25: Eva rekent # : # uit en krijgt #. Hoe kan ze snel controleren of dit klopt?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Eva rekent # : # uit en krijgt #. Hoe kan ze snel controleren of dit klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Optellen is niet de omgekeerde bewerking van delen. Welke som maakt delen ongedaan?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-018` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Eva rekent 63 : 7 uit en krijgt 8. Hoe kan ze snel controleren of dit klopt?
    - **Opties:** A) Het antwoord nog een keer overschrijven · B) 7 × 8 uitrekenen en met 63 vergelijken · C) 63 + 7 uitrekenen en kijken of het klopt
    - **Antwoord:** 7 × 8 uitrekenen en met 63 vergelijken  (controle: n.v.t.)
    - **Fout-hints (Claude):** 63 + 7 uitrekenen en kijken of het klopt → Optellen is niet de omgekeerde bewerking van delen. Welke som maakt delen ongedaan? · Het antwoord nog een keer overschrijven → Overschrijven laat een rekenfout gewoon staan. Je hebt een echte controlesom nodig.
    - **Uitleg (Claude):** Delen controleer je met vermenigvuldigen. 7 × 8 is 56 en dat is niet 63, dus het antwoord klopt niet. Zo vind je je fout meteen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 26: Fenna heeft # + # = # [ding]. Hoe kan zij haar antwoord het beste controleren?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Fenna heeft # + # = # [ding]. Hoe kan zij haar antwoord het beste controleren?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Als je dezelfde weg nog eens loopt, maak je vaak dezelfde fout. Zoek een andere weg terug.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-019` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Fenna heeft 234 + 178 = 412 uitgerekend. Hoe kan zij haar antwoord het beste controleren?
    - **Opties:** A) De som nog een keer precies zo uitrekenen · B) 412 + 178 uitrekenen · C) 412 − 178 uitrekenen en kijken of 234 komt
    - **Antwoord:** 412 − 178 uitrekenen en kijken of 234 komt  (controle: n.v.t.)
    - **Fout-hints (Claude):** De som nog een keer precies zo uitrekenen → Als je dezelfde weg nog eens loopt, maak je vaak dezelfde fout. Zoek een andere weg terug. · 412 + 178 uitrekenen → Om terug te gaan naar het begin moet je de bewerking omkeren.
    - **Uitleg (Claude):** Optellen en aftrekken zijn elkaars omgekeerde. Haal je 178 weer van 412 af, dan hoor je op 234 uit te komen. Zo controleer je via een andere weg.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 27: Hoe zie je of een getal deelbaar is door #?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Hoe zie je of een getal deelbaar is door #?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Probeer je stap eens bij 53 en bij 25. Welk cijfer verraadt de deling door 5?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-020` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Hoe zie je of een getal deelbaar is door 5?
    - **Opties:** A) Kijk of het laatste cijfer 0 of 5 is · B) Kijk of het eerste cijfer 0 of 5 is · C) Kijk of het getal even is
    - **Antwoord:** Kijk of het laatste cijfer 0 of 5 is  (controle: n.v.t.)
    - **Fout-hints (Claude):** Kijk of het eerste cijfer 0 of 5 is → Probeer je stap eens bij 53 en bij 25. Welk cijfer verraadt de deling door 5? · Kijk of het getal even is → Probeer je stap eens bij 12 en bij 15. Klopt hij dan nog?
    - **Uitleg (Claude):** Alle veelvouden van 5 eindigen op 0 of 5. Het laatste cijfer bepaalt dus het antwoord. Deze stap werkt bij elk getal.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 28: Hoe zie je of een getal even is?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Hoe zie je of een getal even is?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): plaatswaarde-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij even en oneven telt alleen het cijfer op de plaats van de eenheden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-021` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Hoe zie je of een getal even is?
    - **Opties:** A) Kijk of het laatste cijfer 0, 2, 4, 6 of 8 is. · B) Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is. · C) Kijk of je het getal door 3 kunt delen.
    - **Antwoord:** Kijk of het laatste cijfer 0, 2, 4, 6 of 8 is.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is. → Bij even en oneven telt alleen het cijfer op de plaats van de eenheden. · Kijk of je het getal door 3 kunt delen. → Even betekent dat je het eerlijk in twee gelijke delen kunt splitsen.
    - **Uitleg (Claude):** Een even getal is deelbaar door 2. Daarvoor hoef je alleen naar het cijfer van de eenheden te kijken. Is dat 0, 2, 4, 6 of 8, dan is het getal even.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 29: In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag # graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag # graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De vraag gaat over één bepaalde dag. De hoogste staaf hoort daar niet altijd bij.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-030` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag 14 graden af, maar hij keek per ongeluk bij donderdag. Hoe voorkom je zo'n fout?
    - **Opties:** A) Altijd de hoogste staaf kiezen · B) De getallen links bij elkaar optellen · C) Eerst de naam onder de staaf lezen
    - **Antwoord:** Eerst de naam onder de staaf lezen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Altijd de hoogste staaf kiezen → De vraag gaat over één bepaalde dag. De hoogste staaf hoort daar niet altijd bij. · De getallen links bij elkaar optellen → De getallen links vormen de schaal. Je hoeft ze niet op te tellen om één waarde af te lezen.
    - **Uitleg (Claude):** Onder elke staaf staat bij welke dag hij hoort. Zoek eerst de juiste dag en ga dan omhoog naar de waarde. Zo lees je de goede staaf af.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 30: In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Niet elke dag kwamen er evenveel bezoekers. Kijk naar alle staven apart.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-031` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week?
    - **Opties:** A) Lees elke staaf af en tel alle waarden op · B) Lees de hoogste staaf af en doe die keer 7 · C) Trek de laagste staaf van de hoogste af
    - **Antwoord:** Lees elke staaf af en tel alle waarden op  (controle: n.v.t.)
    - **Fout-hints (Claude):** Lees de hoogste staaf af en doe die keer 7 → Niet elke dag kwamen er evenveel bezoekers. Kijk naar alle staven apart. · Trek de laagste staaf van de hoogste af → Zo vind je een verschil, geen totaal. Wat doe je met alle dagen samen?
    - **Uitleg (Claude):** Elke staaf hoort bij één dag. Voor het totaal heb je alle dagen nodig. Je leest elke staaf af en telt de getallen bij elkaar op.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 31: In een winkel is er op alles # procent korting. Hoe reken je de nieuwe prijs uit?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “In een winkel is er op alles # procent korting. Hoe reken je de nieuwe prijs uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “Met korting betaal je minder dan eerst. Gaat de prijs dan omhoog of omlaag?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-032` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** In een winkel is er op alles 25 procent korting. Hoe reken je de nieuwe prijs uit?
    - **Opties:** A) Bereken 25 procent van de korting en trek dat eraf. · B) Bereken 25 procent van de prijs en trek dat eraf. · C) Bereken 25 procent van de prijs en tel dat erbij op.
    - **Antwoord:** Bereken 25 procent van de prijs en trek dat eraf.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Bereken 25 procent van de prijs en tel dat erbij op. → Met korting betaal je minder dan eerst. Gaat de prijs dan omhoog of omlaag? · Bereken 25 procent van de korting en trek dat eraf. → Let op waarvan je het percentage neemt. Waarvan gaat de 25 procent af?
    - **Uitleg (Claude):** De korting hoort bij de oude prijs, dus daarvan neem je 25 procent. Dat bedrag haal je van de oude prijs af. Zo houd je de nieuwe prijs over.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 32: In groep # [ding] # [ding]. # procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?

- Sleutel: nrOrigineel **25** · somtypeOrigineel “In groep # [ding] # [ding]. # procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “Procenten zijn delen van het geheel, geen aantal dat je eraf haalt. Zoek eerst 1 procent.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-033` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** In groep 8 zitten 40 leerlingen. 15 procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat zijn?
    - **Opties:** A) Deel 15 door 100 en doe dat keer 40 procent · B) Deel 40 door 100 en doe dat keer 15 · C) Trek 15 van 40 af
    - **Antwoord:** Deel 40 door 100 en doe dat keer 15  (controle: n.v.t.)
    - **Fout-hints (Claude):** Trek 15 van 40 af → Procenten zijn delen van het geheel, geen aantal dat je eraf haalt. Zoek eerst 1 procent. · Deel 15 door 100 en doe dat keer 40 procent → Let goed op waarvan je het deel wilt weten. Van welk getal bereken je hier de procenten?
    - **Uitleg (Claude):** Eén procent van 40 is 40 gedeeld door 100, dus 0,4. Vijftien procent is 15 keer 0,4. Dat zijn 6 leerlingen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 33: Je doet # kg appels in zakjes van # gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Je doet # kg appels in zakjes van # gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed hoeveel gram er in 1 kg gaat. Wordt het getal dan groter of kleiner?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-034` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je doet 2,5 kg appels in zakjes van 500 gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst?
    - **Opties:** A) Deel 2,5 direct door 500. · B) Reken 2,5 kg om naar 2500 gram. · C) Reken 500 gram om naar 5 kg.
    - **Antwoord:** Reken 2,5 kg om naar 2500 gram.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Reken 500 gram om naar 5 kg. → Kijk goed hoeveel gram er in 1 kg gaat. Wordt het getal dan groter of kleiner? · Deel 2,5 direct door 500. → Je kunt pas rekenen als beide getallen dezelfde eenheid hebben.
    - **Uitleg (Claude):** Je kunt alleen rekenen met dezelfde eenheid. In 1 kg zitten 1000 gram, dus 2,5 kg is 2500 gram. Daarna deel je 2500 door 500.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 34: Je fietst # [ding] in # uur. Hoe reken je uit hoeveel kilometer je in # uur fietst?

- Sleutel: nrOrigineel **27** · somtypeOrigineel “Je fietst # [ding] in # uur. Hoe reken je uit hoeveel kilometer je in # uur fietst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “In één uur fiets je minder ver dan in twee uur. Wordt je antwoord dan groter of kleiner?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-035` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je fietst 24 kilometer in 2 uur. Hoe reken je uit hoeveel kilometer je in 1 uur fietst?
    - **Opties:** A) Deel 24 door 2 · B) Vermenigvuldig 24 met 2 · C) Trek 2 van 24 af
    - **Antwoord:** Deel 24 door 2  (controle: n.v.t.)
    - **Fout-hints (Claude):** Vermenigvuldig 24 met 2 → In één uur fiets je minder ver dan in twee uur. Wordt je antwoord dan groter of kleiner? · Trek 2 van 24 af → Je verdeelt de kilometers over de uren. Welke bewerking hoort bij eerlijk verdelen?
    - **Uitleg (Claude):** Je wilt weten hoeveel kilometer je per uur aflegt. Je verdeelt 24 kilometer over 2 uur. 24 gedeeld door 2 is 12 kilometer per uur.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 35: Je hebt # [ding] en # [ding]. Hoe reken je uit hoeveel koekjes [wie] krijgt en hoeveel er overblijven?

- Sleutel: nrOrigineel **28** · somtypeOrigineel “Je hebt # [ding] en # [ding]. Hoe reken je uit hoeveel koekjes [wie] krijgt en hoeveel er overblijven?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): rest-vergeten (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je kunt geen koekje uitdelen dat er niet is. Wat gebeurt er met de koekjes die overblijven?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-036` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 50 koekjes en 8 kinderen. Hoe reken je uit hoeveel koekjes elk kind krijgt en hoeveel er overblijven?
    - **Opties:** A) Deel 50 door 8 en rond naar boven af · B) Trek 8 van 50 af, dat is het antwoord · C) Deel 50 door 8 en kijk naar de rest
    - **Antwoord:** Deel 50 door 8 en kijk naar de rest  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 50 door 8 en rond naar boven af → Je kunt geen koekje uitdelen dat er niet is. Wat gebeurt er met de koekjes die overblijven? · Trek 8 van 50 af, dat is het antwoord → Eerlijk verdelen over groepjes doe je niet met aftrekken. Welke bewerking hoort bij verdelen?
    - **Uitleg (Claude):** 50 gedeeld door 8 is 6, want 8 keer 6 is 48. Er blijven dan 2 koekjes over. Elk kind krijgt er 6 en er blijven er 2 liggen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 36: Je hebt # [ding] en dozen voor # [ding]. Hoe reken je uit hoeveel volle dozen je kunt maken?

- Sleutel: nrOrigineel **29** · somtypeOrigineel “Je hebt # [ding] en dozen voor # [ding]. Hoe reken je uit hoeveel volle dozen je kunt maken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): afronden-verkeerde-kant (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een doos telt alleen mee als hij helemaal vol is. Wat doe je met de eieren die overblijven?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-037` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Je hebt 40 eieren en dozen voor 6 eieren. Hoe reken je uit hoeveel volle dozen je kunt maken?
    - **Opties:** A) Deel 40 door 6 en rond het antwoord naar boven af. · B) Trek 6 van 40 af en noem dat het aantal dozen. · C) Deel 40 door 6 en gebruik alleen het hele aantal.
    - **Antwoord:** Deel 40 door 6 en gebruik alleen het hele aantal.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 40 door 6 en rond het antwoord naar boven af. → Een doos telt alleen mee als hij helemaal vol is. Wat doe je met de eieren die overblijven? · Trek 6 van 40 af en noem dat het aantal dozen. → Je verdeelt de eieren in groepjes van 6. Welke bewerking maakt groepjes?
    - **Uitleg (Claude):** Je verdeelt de eieren in groepjes van 6, dus je deelt. 40 gedeeld door 6 is 6 met een rest. Alleen de volle dozen tellen, dus je gebruikt het hele aantal.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 37: Je koopt # [ding] van # euro en # [ding] van # euro. Hoe reken je uit hoeveel je in totaal betaalt?

- Sleutel: nrOrigineel **30** · somtypeOrigineel “Je koopt # [ding] van # euro en # [ding] van # euro. Hoe reken je uit hoeveel je in totaal betaalt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “De truien en de petten kosten niet hetzelfde. Reken elke soort eerst apart uit.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-038` (Claude W6, ai, niveau 3 → toepassen)
    - **Opgave:** Je koopt 3 truien van 12 euro en 2 petten van 7 euro. Hoe reken je uit hoeveel je in totaal betaalt?
    - **Opties:** A) Reken 3 maal 12 en tel 2 en 7 erbij op. · B) Reken 3 maal 12 en 2 maal 7 en tel die uitkomsten op. · C) Tel 12 en 7 op en doe dat maal 5.
    - **Antwoord:** Reken 3 maal 12 en 2 maal 7 en tel die uitkomsten op.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel 12 en 7 op en doe dat maal 5. → De truien en de petten kosten niet hetzelfde. Reken elke soort eerst apart uit. · Reken 3 maal 12 en tel 2 en 7 erbij op. → Ook bij de petten koop je er meer dan één van dezelfde prijs.
    - **Uitleg (Claude):** Je rekent eerst per soort het bedrag uit met een vermenigvuldiging. Zo krijg je 36 euro en 14 euro. Die twee bedragen tel je op tot het totaal.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 38: Je koopt een pen van # euro en een gum van # euro. Je betaalt met # euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?

- Sleutel: nrOrigineel **31** · somtypeOrigineel “Je koopt een pen van # euro en een gum van # euro. Je betaalt met # euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je krijgt geld terug, dus het bedrag wordt kleiner. Welke bewerking hoort daarbij?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-039` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je koopt een pen van 2 euro en een gum van 1 euro. Je betaalt met 5 euro. Hoe reken je uit hoeveel wisselgeld je terugkrijgt?
    - **Opties:** A) Tel de prijzen op, trek die van het betaalde bedrag af. · B) Tel de prijzen op, tel die bij het betaalde bedrag op. · C) Tel de prijzen op en noem die uitkomst het wisselgeld.
    - **Antwoord:** Tel de prijzen op, trek die van het betaalde bedrag af.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel de prijs op, tel die bij het betaalde bedrag op. → Je krijgt geld terug, dus het bedrag wordt kleiner. Welke bewerking hoort daarbij? · Tel de prijs op en noem die uitkomst het wisselgeld. → Het wisselgeld is niet de prijs zelf. Je moet de prijs nog met het betaalde bedrag vergelijken.
    - **Uitleg (Claude):** Eerst bepaal je het totaal van wat je koopt. Dat totaal haal je van het betaalde bedrag af. Wat overblijft, is het wisselgeld.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 39: Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?

- Sleutel: nrOrigineel **32** · somtypeOrigineel “Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Let op de volgorde. Je kunt een boek pas pakken als je weet waar het staat.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-040` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst?
    - **Opties:** A) Pak het boek, zoek de letter, loop naar dat vak. · B) Loop door de bibliotheek tot je iets leuks ziet. · C) Zoek de letter, loop naar dat vak, pak het boek.
    - **Antwoord:** Zoek de letter, loop naar dat vak, pak het boek.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Pak het boek, zoek de letter, loop naar dat vak. → Let op de volgorde. Je kunt een boek pas pakken als je weet waar het staat. · Loop door de bibliotheek tot je iets leuks ziet. → Een goede uitleg werkt altijd, ook voor iemand anders. Zomaar rondlopen leidt niet steeds naar het juiste boek.
    - **Uitleg (Claude):** Een goede uitleg zet de stappen in de juiste volgorde. Eerst zoek je waar het boek hoort, dan loop je erheen. Pas daarna kun je het boek pakken.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 40: Je moet # [ding] op alfabetische volgorde zetten. Welke aanpak werkt altijd?

- Sleutel: nrOrigineel **33** · somtypeOrigineel “Je moet # [ding] op alfabetische volgorde zetten. Welke aanpak werkt altijd?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Alfabetische volgorde gaat niet over lengte. Waar kijk je dan wel naar?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-041` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je moet 12 namen op alfabetische volgorde zetten. Welke aanpak werkt altijd?
    - **Opties:** A) Vergelijk alleen de eerste en de laatste naam · B) Zoek steeds de eerste naam en zet die apart · C) Zet de kortste namen vooraan
    - **Antwoord:** Zoek steeds de eerste naam en zet die apart  (controle: n.v.t.)
    - **Fout-hints (Claude):** Zet de kortste namen vooraan → Alfabetische volgorde gaat niet over lengte. Waar kijk je dan wel naar? · Vergelijk alleen de eerste en de laatste naam → Alle namen moeten op hun plek komen. Elke naam moet dus een keer vergeleken worden.
    - **Uitleg (Claude):** Je zoekt telkens de naam die alfabetisch het eerst komt. Die zet je op de volgende plaats in de rij. Zo komen alle namen een keer aan de beurt.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 41: Je spaart elke week # euro en wilt # euro hebben. Hoe reken je uit hoeveel weken je moet sparen?

- Sleutel: nrOrigineel **34** · somtypeOrigineel “Je spaart elke week # euro en wilt # euro hebben. Hoe reken je uit hoeveel weken je moet sparen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het aantal weken kan niet groter zijn dan het aantal euro's. Denk aan groepjes van 3 euro.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-042` (Claude W6, ai, niveau 1 → basis)
    - **Opgave:** Je spaart elke week 3 euro en wilt 45 euro hebben. Hoe reken je uit hoeveel weken je moet sparen?
    - **Opties:** A) Deel 45 door 3 · B) Doe 45 keer 3 · C) Trek 3 van 45 af
    - **Antwoord:** Deel 45 door 3  (controle: n.v.t.)
    - **Fout-hints (Claude):** Doe 45 keer 3 → Het aantal weken kan niet groter zijn dan het aantal euro's. Denk aan groepjes van 3 euro. · Trek 3 van 45 af → Je wilt weten hoe vaak 3 euro in 45 euro past. Welke bewerking hoort daarbij?
    - **Uitleg (Claude):** Je zoekt hoe vaak 3 euro in 45 euro past. Dat doe je met delen. 45 gedeeld door 3 is 15 weken.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 42: Je verdeelt een pak sap van # liter over [bakken] van # [ding]. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?

- Sleutel: nrOrigineel **35** · somtypeOrigineel “Je verdeelt een pak sap van # liter over [bakken] van # [ding]. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je rekent nu met twee verschillende eenheden. Maak ze eerst gelijk.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-043` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je verdeelt een pak sap van 1,5 liter over bekers van 250 milliliter. Je wilt weten hoeveel bekers je kunt vullen. Wat doe je eerst?
    - **Opties:** A) Deel 1,5 meteen door 250 · B) Reken 1,5 liter om naar 150 milliliter · C) Reken 1,5 liter om naar 1500 milliliter
    - **Antwoord:** Reken 1,5 liter om naar 1500 milliliter  (controle: n.v.t.)
    - **Fout-hints (Claude):** Deel 1,5 meteen door 250 → Je rekent nu met twee verschillende eenheden. Maak ze eerst gelijk. · Reken 1,5 liter om naar 150 milliliter → Kijk nog eens hoeveel milliliter er in één liter gaan. Dat zijn er meer dan honderd.
    - **Uitleg (Claude):** In 1 liter zitten 1000 milliliter, dus 1,5 liter is 1500 milliliter. Met dezelfde eenheid kun je pas goed delen. Daarna deel je 1500 door 250.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 43: Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?

- Sleutel: nrOrigineel **36** · somtypeOrigineel “Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Denk aan een hek rondom de tuin. Je loopt langs alle vier de zijden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-044` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit?
    - **Opties:** A) Tel lengte en breedte op en verdubbel die som. · B) Vermenigvuldig de lengte met de breedte. · C) Tel lengte en breedte op en klaar.
    - **Antwoord:** Tel lengte en breedte op en verdubbel die som.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Vermenigvuldig de lengte met de breedte. → Denk aan een hek rondom de tuin. Je loopt langs alle vier de zijden. · Tel lengte en breedte op en klaar. → Een rechthoek heeft vier zijden. Hoeveel zijden heb je nu geteld?
    - **Uitleg (Claude):** De omtrek is de som van alle vier de zijden. Lengte en breedte komen elk twee keer voor. Dus tel je ze op en verdubbel je die som.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 44: Je wilt het gemiddelde van # [ding] weten. Hoe reken je dat uit?

- Sleutel: nrOrigineel **37** · somtypeOrigineel “Je wilt het gemiddelde van # [ding] weten. Hoe reken je dat uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W6 (1) · regel: G8-W6-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij een gemiddelde verdeel je het totaal eerlijk over alle cijfers. Welke bewerking verdeelt?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-045` (Claude W6, ai, niveau 2 → toepassen)
    - **Opgave:** Je wilt het gemiddelde van 5 rapportcijfers weten. Hoe reken je dat uit?
    - **Opties:** A) Tel alle cijfers op en tel de som bij 5 op. · B) Zoek het hoogste cijfer en deel dat door 5. · C) Tel alle cijfers op en deel de som door 5.
    - **Antwoord:** Tel alle cijfers op en deel de som door 5.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tel alle cijfers op en tel de som bij 5 op. → Bij een gemiddelde verdeel je het totaal eerlijk over alle cijfers. Welke bewerking verdeelt? · Zoek het hoogste cijfer en deel dat door 5. → Bij een gemiddelde doen alle cijfers mee, niet alleen één cijfer.
    - **Uitleg (Claude):** Een gemiddelde vind je door alles samen te nemen en het dan eerlijk te verdelen. Je telt de 5 cijfers op tot een totaal. Dat totaal deel je door het aantal cijfers, dus door 5.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 45: Jinte moet # × # [ding]. Welke aanpak is het handigst?

- Sleutel: nrOrigineel **38** · somtypeOrigineel “Jinte moet # × # [ding]. Welke aanpak is het handigst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt vijf keer 2 te veel gerekend, niet één keer. Hoeveel is dat bij elkaar?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-046` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Jinte moet 5 × 98 uitrekenen. Welke aanpak is het handigst?
    - **Opties:** A) 5 × 100 doen en er 2 afhalen · B) 98 vijf keer onder elkaar optellen · C) 5 × 100 doen en er 10 afhalen
    - **Antwoord:** 5 × 100 doen en er 10 afhalen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 × 100 doen en er 2 afhalen → Je hebt vijf keer 2 te veel gerekend, niet één keer. Hoeveel is dat bij elkaar? · 98 vijf keer onder elkaar optellen → Dat mag wel, maar het kost veel stappen. 98 ligt heel dicht bij een rond getal.
    - **Uitleg (Claude):** 98 is 2 minder dan 100. Bij 5 keer reken je dus 5 × 2 = 10 te veel. Daarom haal je 10 van 500 af.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 46: Kim moet # × # [ding]. Ze doet eerst # × # = # en neemt dan de helft. Klopt deze aanpak?

- Sleutel: nrOrigineel **39** · somtypeOrigineel “Kim moet # × # [ding]. Ze doet eerst # × # = # en neemt dan de helft. Klopt deze aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vijf keer iets is minder dan tien keer iets. Wat doe je dan met de uitkomst van 36 × 10?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-047` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Kim moet 36 × 5 uitrekenen. Ze doet eerst 36 × 10 = 360 en neemt dan de helft. Klopt deze aanpak?
    - **Opties:** A) Nee, ze moet er 10 van afhalen · B) Ja, 5 is de helft van 10 · C) Nee, ze moet 360 verdubbelen
    - **Antwoord:** Ja, 5 is de helft van 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, ze moet 360 verdubbelen → Vijf keer iets is minder dan tien keer iets. Wat doe je dan met de uitkomst van 36 × 10? · Nee, ze moet er 10 van afhalen → Je kijkt naar het verschil tussen 5 en 10 als getal. Kijk liever hoe die twee zich tot elkaar verhouden.
    - **Uitleg (Claude):** Keer 10 gaat heel makkelijk. Omdat 5 de helft van 10 is, halveer je daarna de uitkomst. 360 gedeeld door 2 is 180.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 47: Lars zet # [ding] jam in [bakken] van #. Hij rekent # : # en schrijft # [ding] op. Wat is er mis met zijn aanpak?

- Sleutel: nrOrigineel **40** · somtypeOrigineel “Lars zet # [ding] jam in [bakken] van #. Hij rekent # : # en schrijft # [ding] op. Wat is er mis met zijn aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): rest-vergeten (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken na hoeveel potjes er in 14 volle dozen passen. Blijft er dan nog iets over?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-048` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Lars zet 148 potjes jam in dozen van 10. Hij rekent 148 : 10 en schrijft 14 dozen op. Wat is er mis met zijn aanpak?
    - **Opties:** A) Niets, 14 dozen is precies goed · B) Hij moest 148 × 10 doen · C) Er blijven 8 potjes over, dus er is een extra doos nodig
    - **Antwoord:** Er blijven 8 potjes over, dus er is een extra doos nodig  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, 14 dozen is precies goed → Reken na hoeveel potjes er in 14 volle dozen passen. Blijft er dan nog iets over? · Hij moest 148 × 10 doen → Vermenigvuldigen maakt het aantal juist groter. Bij verdelen in gelijke groepen kies je iets anders.
    - **Uitleg (Claude):** In 14 dozen passen 140 potjes. Er blijven dan 8 potjes over en die moeten ook mee. Daarom zijn er 15 dozen nodig.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 48: Mees moet # × # [ding]. Hij telt # + # + # + # op. Wat had handiger gekund?

- Sleutel: nrOrigineel **41** · somtypeOrigineel “Mees moet # × # [ding]. Hij telt # + # + # + # op. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vier groepen van 250 is niet hetzelfde als 250 en 4 samen. Kijk nog eens naar het maalteken.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-049` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Mees moet 4 × 250 uitrekenen. Hij telt 250 + 250 + 250 + 250 op. Wat had handiger gekund?
    - **Opties:** A) Eerst 250 + 4 uitrekenen · B) De som onder elkaar zetten met een streep · C) Meteen 4 × 250 vermenigvuldigen
    - **Antwoord:** Meteen 4 × 250 vermenigvuldigen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Eerst 250 + 4 uitrekenen → Vier groepen van 250 is niet hetzelfde als 250 en 4 samen. Kijk nog eens naar het maalteken. · De som onder elkaar zetten met een streep → Onder elkaar zetten kost hier veel tijd. 250 is een mooi getal om mee te vermenigvuldigen.
    - **Uitleg (Claude):** Vier keer hetzelfde getal optellen is precies vermenigvuldigen. Met 4 × 250 ben je in één stap klaar. Dat scheelt tijd en je maakt minder fouten.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 49: Noor moet # × # [ding] en telt acht keer # bij elkaar op. Wat had handiger gekund?

- Sleutel: nrOrigineel **42** · somtypeOrigineel “Noor moet # × # [ding] en telt acht keer # bij elkaar op. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Let op het teken in de som. Optellen en keer doen geven heel andere antwoorden.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-050` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Noor moet 25 × 8 uitrekenen en telt acht keer 25 bij elkaar op. Wat had handiger gekund?
    - **Opties:** A) 25 en 8 bij elkaar optellen · B) 25 × 10 doen en er 2 afhalen · C) 25 × 4 doen en dan verdubbelen
    - **Antwoord:** 25 × 4 doen en dan verdubbelen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 25 en 8 bij elkaar optellen → Let op het teken in de som. Optellen en keer doen geven heel andere antwoorden. · 25 × 10 doen en er 2 afhalen → Als je met 10 rekent in plaats van met 8, haal je hele groepen van 25 te veel weg.
    - **Uitleg (Claude):** Je mag een keersom in stappen splitsen. 25 × 4 is 100 en dat verdubbel je tot 200. Dat gaat veel sneller dan acht keer optellen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 50: Nout heeft # − # [ding] elkaar uitgerekend en kreeg #. Hij schatte vooraf ongeveer #. Wat moet hij nu doen?

- Sleutel: nrOrigineel **43** · somtypeOrigineel “Nout heeft # − # [ding] elkaar uitgerekend en kreeg #. Hij schatte vooraf ongeveer #. Wat moet hij nu doen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): schatting-verkeerd (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een schatting met ronde getallen is meestal betrouwbaar. Reken 800 − 400 nog eens na.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-051` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Nout heeft 802 − 397 onder elkaar uitgerekend en kreeg 505. Hij schatte vooraf ongeveer 400. Wat moet hij nu doen?
    - **Opties:** A) De schatting aanpassen naar 500 · B) Het antwoord 505 gewoon laten staan · C) De som opnieuw uitrekenen, want de schatting past niet
    - **Antwoord:** De som opnieuw uitrekenen, want de schatting past niet  (controle: n.v.t.)
    - **Fout-hints (Claude):** De schatting aanpassen naar 500 → Een schatting met ronde getallen is meestal betrouwbaar. Reken 800 − 400 nog eens na. · Het antwoord 505 gewoon laten staan → Je schatting waarschuwt je juist voor een fout. Negeer dat signaal niet.
    - **Uitleg (Claude):** 800 − 400 is ongeveer 400, dus 505 ligt er ver naast. Zo'n groot verschil wijst op een rekenfout. Het echte antwoord is 405.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 51: Op de fietstocht rijdt Tess # km. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet klopt?

- Sleutel: nrOrigineel **44** · somtypeOrigineel “Op de fietstocht rijdt Tess # km. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “De komma verplaatsen is niet hetzelfde als omrekenen. Hoeveel meter zit er in 1 kilometer?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-060` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Op de fietstocht rijdt Tess 3,2 km. Ze schrijft op dat dit 32 meter is. Hoe merk je dat dit niet klopt?
    - **Opties:** A) Het moet 320 meter zijn · B) 1 km is al 1000 meter, dus het moeten er veel meer zijn · C) Het klopt, je haalt gewoon de komma weg
    - **Antwoord:** 1 km is al 1000 meter, dus het moeten er veel meer zijn  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het klopt, je haalt gewoon de komma weg → De komma verplaatsen is niet hetzelfde als omrekenen. Hoeveel meter zit er in 1 kilometer? · Het moet 320 meter zijn → Je bent één stap te vroeg gestopt. Reken eerst uit hoeveel meter 3 km is.
    - **Uitleg (Claude):** Eén kilometer is 1000 meter. 3,2 km is dus 3200 meter. Met 32 meter kom je nog niet eens de straat uit.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 52: Roos rekent # × # uit door # × # en # × # [ding] te doen. Ze schrijft alleen # op. Wat ging er mis?

- Sleutel: nrOrigineel **45** · somtypeOrigineel “Roos rekent # × # uit door # × # en # × # [ding] te doen. Ze schrijft alleen # op. Wat ging er mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): None (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Splitsen is juist een slimme aanpak. Kijk nog eens of ze alle stukjes heeft gebruikt.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-114` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Roos rekent 7 × 24 uit door 7 × 20 en 7 × 4 apart te doen. Ze schrijft alleen 140 op. Wat ging er mis?
    - **Opties:** A) Ze moest 140 en 24 optellen · B) Ze vergat 28 erbij op te tellen · C) Ze had niet mogen splitsen
    - **Antwoord:** Ze vergat 28 erbij op te tellen  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze had niet mogen splitsen → Splitsen is juist een slimme aanpak. Kijk nog eens of ze alle stukjes heeft gebruikt. · Ze moest 140 en 24 optellen → Het tweede stukje was 7 × 4, niet 24. Reken dat stukje eerst uit.
    - **Uitleg (Claude):** Bij splitsen reken je beide delen uit en tel je ze op. 140 en 28 samen is 168. Roos stopte te vroeg met haar aanpak.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 53: Sam rekent # − # uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?

- Sleutel: nrOrigineel **46** · somtypeOrigineel “Sam rekent # − # uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk nog eens welk teken er tussen de getallen staat.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-115` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Sam rekent 1000 − 998 uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund?
    - **Opties:** A) 1000 en 998 bij elkaar optellen · B) Eerst 900 eraf en dan 98 erbij · C) Doortellen van 998 naar 1000
    - **Antwoord:** Doortellen van 998 naar 1000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1000 en 998 bij elkaar optellen → Kijk nog eens welk teken er tussen de getallen staat. · Eerst 900 eraf en dan 98 erbij → Als je een deel van een aftreksom afhaalt, moet je het andere deel er ook afhalen.
    - **Uitleg (Claude):** De getallen liggen heel dicht bij elkaar. Vanaf 998 tel je maar 2 stapjes door tot 1000. Onder elkaar rekenen is dan onnodig werk.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 54: Sanne rekent # + # uit door eerst # + # te doen en er daarna # af te halen. Klopt deze aanpak?

- Sleutel: nrOrigineel **47** · somtypeOrigineel “Sanne rekent # + # uit door eerst # + # te doen en er daarna # af te halen. Klopt deze aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Ze heeft eerst een groter getal gebruikt dan 198. Wat doe je dan achteraf met dat verschil?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-116` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Sanne rekent 198 + 56 uit door eerst 200 + 56 te doen en er daarna 2 af te halen. Klopt deze aanpak?
    - **Opties:** A) Ja, dat is een handige manier · B) Nee, ze moet er 2 bij optellen · C) Nee, je mag alleen onder elkaar rekenen
    - **Antwoord:** Ja, dat is een handige manier  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, ze moet er 2 bij optellen → Ze heeft eerst een groter getal gebruikt dan 198. Wat doe je dan achteraf met dat verschil? · Nee, je mag alleen onder elkaar rekenen → Een som onder elkaar mag altijd, maar soms kan het slimmer. Denk aan mooie ronde getallen.
    - **Uitleg (Claude):** 198 ligt vlak bij 200, dus rekenen met 200 gaat makkelijk. Omdat je 2 te veel gebruikte, haal je er achteraf 2 af. Zo krijg je hetzelfde antwoord, maar sneller.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 55: Tim rekent # + # uit met een staartsom onder elkaar. Wat is een handigere aanpak?

- Sleutel: nrOrigineel **48** · somtypeOrigineel “Tim rekent # + # uit met een staartsom onder elkaar. Wat is een handigere aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): een-ernaast (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je deed er 1 te veel bij. Bedenk wat je moet doen als je eerst een te groot getal pakt.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-117` (Claude W3, ai, niveau 1 → basis)
    - **Opgave:** Tim rekent 99 + 47 uit met een staartsom onder elkaar. Wat is een handigere aanpak?
    - **Opties:** A) Eerst 100 erbij, dan 1 eraf · B) Eerst 100 erbij, dan 1 erbij · C) Eerst 90 erbij, dan 9 eraf
    - **Antwoord:** Eerst 100 erbij, dan 1 eraf  (controle: n.v.t.)
    - **Fout-hints (Claude):** Eerst 100 erbij, dan 1 erbij → Je deed er 1 te veel bij. Bedenk wat je moet doen als je eerst een te groot getal pakt. · Eerst 90 erbij, dan 9 eraf → Kijk nog eens goed hoe dicht 99 bij een rond honderdtal ligt.
    - **Uitleg (Claude):** 99 ligt vlak bij 100. Je telt er eerst 100 bij op en haalt daarna de 1 die je te veel nam er weer af. Zo hoef je niet onder elkaar te rekenen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 56: Voor een uitje gaan # [ding] mee. In een busje passen # [ding]. Lisa rekent # : # en schrijft # [ding] op. Wat is er mis met haar aanpak?

- Sleutel: nrOrigineel **49** · somtypeOrigineel “Voor een uitje gaan # [ding] mee. In een busje passen # [ding]. Lisa rekent # : # en schrijft # [ding] op. Wat is er mis met haar aanpak?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je verdeelt kinderen over busjes. Welke bewerking hoort bij verdelen?”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-118` (Claude W3, ai, niveau 2 → toepassen)
    - **Opgave:** Voor een uitje gaan 50 kinderen mee. In een busje passen 12 kinderen. Lisa rekent 50 : 12 en schrijft 4 busjes op. Wat is er mis met haar aanpak?
    - **Opties:** A) Ze vergat de 2 kinderen die overblijven · B) Ze had 50 × 12 moeten doen · C) Er zijn 6 busjes nodig
    - **Antwoord:** Ze vergat de 2 kinderen die overblijven  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ze had 50 × 12 moeten doen → Je verdeelt kinderen over busjes. Welke bewerking hoort bij verdelen? · Er zijn 6 busjes nodig → Reken na hoeveel kinderen er in 5 busjes passen. Zijn dat er genoeg?
    - **Uitleg (Claude):** In 4 busjes passen 48 kinderen. Er blijven er 2 over en die moeten ook mee. Daarom is er nog een extra busje nodig.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 57: Yara loopt # km naar school. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet kan?

- Sleutel: nrOrigineel **50** · somtypeOrigineel “Yara loopt # km naar school. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet kan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W3 (1) · regel: G8-W3-aanpak
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een komma weghalen is niet hetzelfde als omrekenen. Kijk hoeveel meter er in 1 kilometer gaan.”)
- Voorbeelden:
  - `G8-GET-E02-claude-bank-119` (Claude W3, ai, niveau 3 → toepassen)
    - **Opgave:** Yara loopt 2,5 km naar school. Ze schrijft op dat dit 250 meter is. Hoe merk je dat dit niet kan?
    - **Opties:** A) 1 km is 1000 meter, dus het zijn er meer · B) Het klopt, want je zet de komma weg · C) Het moet 25 meter zijn
    - **Antwoord:** 1 km is 1000 meter, dus het zijn er meer  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het klopt, want je zet de komma weg → Een komma weghalen is niet hetzelfde als omrekenen. Kijk hoeveel meter er in 1 kilometer gaan. · Het moet 25 meter zijn → 25 meter is korter dan een schoolplein. Vergelijk dat eens met 2,5 kilometer lopen.
    - **Uitleg (Claude):** In 1 kilometer gaan 1000 meter. 2,5 × 1000 is 2500 meter. Bij omrekenen let je altijd op de juiste stap.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
