# G5-GET-E07 — Keer en delen tot duizend

Onze omschrijving: × ÷ ≤1000: standaard + strategieën; veelvouden van 10; schattend × · in onze bank: 8 items

Claude-vragen gemapt: **504** in **11** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # × # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **328** · Claude-doelen: C7 (328) · regel: G5-K02-kaal-keer
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): tiental-ernaast (253), een-ernaast (247), optellen-ipv-vermenigvuldigen (86), onthouden-vergeten (70)
- Verschillende Claude-fout-hints: 4 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-175` (Claude C7, bank, niveau 3 → toepassen)
    - **Opgave:** 13 × 3 =
    - **Antwoord:** 39  (controle: ok)
    - **Fout-hints (Claude):** 40 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 38 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-E07-claude-bank-303` (Claude C7, bank, niveau 3 → toepassen)
    - **Opgave:** 59 × 7 =
    - **Antwoord:** 413  (controle: ok)
    - **Fout-hints (Claude):** 423 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 414 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Splits het eerste getal: honderdtallen, tientallen en eenheden (als het die heeft).
- **Hint 2 (te schrijven):** Doe elk stuk keer het tweede getal. Tel de uitkomsten daarna bij elkaar op.
- **Ouderzin:** Je kind rekent een keersom uit: een groot getal keer een getal onder de 10 (uitkomst tot 1000).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Kijk naar het teken: het is een keersom.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Heeft het eerste getal eenheden? Reken dan het stuk met de eenheden nog eens na. Tel daarna alle stukken goed op.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Heeft het eerste getal eenheden? Reken dan het stuk met de eenheden nog eens na. Tel daarna alle stukken goed op.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `iets vergeten` (Claudes sleutel: onthouden-vergeten) → Dat is te weinig. Reken elk stuk apart uit. Tel daarna alle stukken bij elkaar op, en vergeet er geen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het eerste getal in stukken. Doe elk stuk keer het tweede getal en tel alles op.  [nieuw]
- Status: hints klaar

## Somtype 2: In elk(e) [bak] zitten # [ding]. Er zijn # [ding]. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In elk(e) [bak] zitten # [ding]. Er zijn # [ding]. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **58** · Claude-doelen: T9 (58) · regel: FX-G4-5, G07-welke-som
- Getallenruimte: 0–100, 0–20 · type: meerkeuze
- Uitleg bij het eerste gebruik (kindtekst, veld begripUitleg): “':' betekent gedeeld door.”
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (58), verkeerde-bewerking (58)
- Verschillende Claude-fout-hints: 2 (meest: “Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-413` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In elke mand zitten 14 ballen. Er zijn 7 manden. Welke som hoort bij dit verhaal?
    - **Opties:** A) 14 : 7 · B) 7 + 14 · C) 7 × 14
    - **Antwoord:** 7 × 14  (controle: ok)
    - **Fout-hints (Claude):** 7 + 14 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen. · 14 : 7 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E07-claude-bank-380` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In elke bak zitten 25 appels. Er zijn 11 bakken. Welke som hoort bij dit verhaal?
    - **Opties:** A) 25 : 11 · B) 11 × 25 · C) 11 + 25
    - **Antwoord:** 11 × 25  (controle: ok)
    - **Fout-hints (Claude):** 11 + 25 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen. · 25 : 11 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Hoeveel zijn er? En hoeveel zitten er in elk?
- **Hint 2 (te schrijven):** Steeds hetzelfde aantal: welke som past daarbij?
- **Ouderzin:** Je kind kiest de som die bij een verhaaltje hoort (een keersom).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plussom` (de plussom) → Je telt de twee getallen op. Maar in elk zitten er evenveel, een aantal keer: dat is een keersom.  [nieuw]
  - `deelsom` (:) → Je kiest een deelsom, maar er wordt niets verdeeld. In elk zitten er evenveel, een aantal keer: dat is een keersom.  [nieuw]
  - `andere fout` (andere fout) → In elk zitten er evenveel, en dat een aantal keer. Welke som hoort daarbij?  [nieuw]
- Status: hints klaar

## Somtype 3: # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# [ding] worden eerlijk verdeeld over # [ding]. Hoeveel [ding] krijgt [wie]?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: C9 (32) · regel: G5-C02-verdelen
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (64), deel-vergeten-bij-splitsen (32)
- Verschillende Claude-fout-hints: 3 (meest: “Je bent het deel van tien vergeten: splits eerst tien keer de deler af, en deel dan de rest.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-004` (Claude C9, gegenereerd, niveau 1 → basis)
    - **Opgave:** 84 botten worden eerlijk verdeeld over 6 dino's. Hoeveel botten krijgt elke dino?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je bent het deel van tien vergeten: splits eerst tien keer de deler af, en deel dan de rest. · 15 → Controleer met de keersom: jouw getal keer de deler komt boven het totaal uit. · 13 → Controleer met de keersom: jouw getal keer de deler blijft onder het totaal.
    - **Uitleg (Claude):** Splits 84 in 60 en 24. 60 : 6 = 10 en 24 : 6 = 4. Samen 14.
  - `G5-GET-E07-claude-bank-030` (Claude C9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 138 tanden worden eerlijk verdeeld over 6 dino's. Hoeveel tanden krijgt elke dino?
    - **Antwoord:** 23  (controle: ok)
    - **Fout-hints (Claude):** 13 → Je bent het deel van tien vergeten: splits eerst tien keer de deler af, en deel dan de rest. · 24 → Controleer met de keersom: jouw getal keer de deler komt boven het totaal uit. · 22 → Controleer met de keersom: jouw getal keer de deler blijft onder het totaal.
    - **Uitleg (Claude):** Splits 138 in 60 en 78. 60 : 6 = 10 en 78 : 6 = 13. Samen 23.

- **Hint 1 (te schrijven):** Eerlijk verdelen is een deelsom. Hoeveel krijgt ieder?
- **Hint 2 (te schrijven):** Zoek een keersom die je kent: hoeveel keer het aantal waarover je verdeelt, is het totaal? Begin met tien keer.
- **Ouderzin:** Je kind verdeelt een aantal eerlijk (deelsom, de uitkomst ligt tussen 10 en 30).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom. [getal2] keer jouw antwoord is meer dan [getal1].  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom. [getal2] keer jouw antwoord is minder dan [getal1].  [nieuw]
  - `tien vergeten` (fout = antwoord − 10) → Dat is tien te weinig. Heb je ieder eerst tien gegeven? Verdeel eerst tien keer, en daarna de rest.  [nieuw]
  - `andere fout` (andere fout) → Reken na met een keersom: jouw antwoord keer het aantal waarover je verdeelt, moet het totaal zijn.  [nieuw]
- Status: hints klaar

## Somtype 4: Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen?” (koppeling: claudeId)
- Items: **29** · Claude-doelen: T3 (29) · regel: D8-KLOPPEN-NAAR-G5
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (28), laatste-cijfer (16), bovengrens (11), ondergrens (3)
- Verschillende Claude-fout-hints: 57 (meest: “Rond eerst af. 40 × 4 is 160. Ligt 48 daar dichtbij?”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-naar-027` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 25 × 5 kan kloppen?
    - **Opties:** A) 125 · B) 225 · C) 30
    - **Antwoord:** 125  (controle: n.v.t.)
    - **Fout-hints (Claude):** 225 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 30 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E07-claude-bank-naar-042` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 36 × 8 kan kloppen?
    - **Opties:** A) 288 · B) 388 · C) 290
    - **Antwoord:** 288  (controle: n.v.t.)
    - **Fout-hints (Claude):** 388 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond het grootste getal af en reken uit. Zo weet je ongeveer hoe groot de uitkomst is.
- **Hint 2 (te schrijven):** Kijk daarna naar de laatste cijfers. Op welk cijfer moet de uitkomst eindigen? Kies het antwoord dat in de buurt ligt en op dat cijfer eindigt.
- **Ouderzin:** Je kind kiest zonder uit te rekenen welk antwoord bij een keersom kan kloppen: afronden en naar het laatste cijfer kijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te ver weg` (Claudes sleutel: orde-van-grootte) → Rond eerst af en reken dat uit. Ligt dit antwoord daar in de buurt?  [Claude, taalfix]
  - `ander laatste cijfer` (Claudes sleutel: laatste-cijfer) → Doe de laatste cijfers van de twee getallen keer elkaar. Op welk cijfer eindigt dat? Eindigt dit antwoord daarop?  [Claude, taalfix]
  - `te groot` (Claudes sleutel: bovengrens) → Rond het grootste getal naar boven af en reken uit. Groter dan dat kan de uitkomst niet zijn. Is dit antwoord groter?  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Rond het grootste getal naar beneden af en reken uit. Kleiner dan dat kan de uitkomst niet zijn. Is dit antwoord kleiner?  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond het grootste getal af en reken uit. Zo weet je ongeveer hoe groot de uitkomst is. Kijk daarna naar de laatste cijfers.  [nieuw]
- Status: hints klaar

## Somtype 5: [wie] heeft # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[wie] heeft # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C7 (12) · regel: G5-C01-keer-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (36), optellen-ipv-vermenigvuldigen (12)
- Verschillende Claude-fout-hints: 47 (meest: “Je hebt 6 erbij gedaan, maar het moet 7 × 6 zijn: ook het kleine stukje is een keersom.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-426` (Claude C7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elke dino heeft 16 eieren. Er zijn 9 dino's. Hoeveel eieren zijn dat samen?
    - **Antwoord:** 144  (controle: ok)
    - **Fout-hints (Claude):** 90 → 9 × 10 = 90 klopt. Maar het waren 16 eieren, niet 10. Wat komt er nog bij? · 54 → 9 × 6 = 54 is het kleine stukje. Het grote stukje 9 × 10 ontbreekt nog. · 25 → Élke dino heeft 16 eieren, en er zijn er 9. Dat is een keersom. · 96 → Je hebt 6 erbij gedaan, maar het moet 9 × 6 zijn: ook het kleine stukje is een keersom.
    - **Uitleg (Claude):** Knip 16 in 10 en 6. 9 × 10 = 90. 9 × 6 = 54. Samen: 90 + 54 = 144.
  - `G5-GET-E07-claude-bank-435` (Claude C7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk kind heeft 36 stickers. Er zijn 7 kinderen. Hoeveel stickers zijn dat samen?
    - **Antwoord:** 252  (controle: ok)
    - **Fout-hints (Claude):** 210 → 7 × 30 = 210 klopt. Maar het waren 36 stickers, niet 30. Wat komt er nog bij? · 42 → 7 × 6 = 42 is het kleine stukje. Het grote stukje 7 × 30 ontbreekt nog. · 43 → Élk kind heeft 36 stickers, en er zijn er 7. Dat is een keersom. · 216 → Je hebt 6 erbij gedaan, maar het moet 7 × 6 zijn: ook het kleine stukje is een keersom.
    - **Uitleg (Claude):** Knip 36 in 30 en 6. 7 × 30 = 210. 7 × 6 = 42. Samen: 210 + 42 = 252.

- **Hint 1 (te schrijven):** Ze hebben allemaal evenveel. Hoeveel zijn het er? Dat is een keersom.
- **Hint 2 (te schrijven):** Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `een stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je allebei de stukken keer het andere getal gedaan? Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken het in stukken uit en tel de stukken op. Kijk of je antwoord past: het is een keersom.  [nieuw]
- Status: hints klaar

## Somtype 6: [wie] verzamelt elke dag # [ding]. Hoeveel [ding] zijn dat in # dagen?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[wie] verzamelt elke dag # [ding]. Hoeveel [ding] zijn dat in # dagen?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: C7 (9) · regel: G5-C01-keer-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (18), optellen-ipv-vermenigvuldigen (9)
- Verschillende Claude-fout-hints: 25 (meest: “Dat is een nul te veel. 30 heeft één nul, dus het antwoord krijgt er ook één.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-444` (Claude C7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een poes verzamelt elke dag 70 balletjes. Hoeveel balletjes zijn dat in 5 dagen?
    - **Antwoord:** 350  (controle: ok)
    - **Fout-hints (Claude):** 35 → Reken eerst 5 × 7. Plak daarna één nul er weer aan. Je mist er één. · 3500 → Dat is een nul te veel. 70 heeft één nul, dus het antwoord krijgt er ook één. · 75 → Elke dag 70 erbij, 5 dagen lang. Dat is een keersom.
    - **Uitleg (Claude):** 5 × 70 lijkt op 5 × 7. 5 × 7 = 35. De één nul van 70 er weer aan: 350.
  - `G5-GET-E07-claude-bank-449` (Claude C7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een dino verzamelt elke dag 30 eieren. Hoeveel eieren zijn dat in 9 dagen?
    - **Antwoord:** 270  (controle: ok)
    - **Fout-hints (Claude):** 27 → Reken eerst 9 × 3. Plak daarna één nul er weer aan. Je mist er één. · 2700 → Dat is een nul te veel. 30 heeft één nul, dus het antwoord krijgt er ook één. · 39 → Elke dag 30 erbij, 9 dagen lang. Dat is een keersom.
    - **Uitleg (Claude):** 9 × 30 lijkt op 9 × 3. 9 × 3 = 27. De één nul van 30 er weer aan: 270.

- **Hint 1 (te schrijven):** Elke dag komt er evenveel bij. Hoeveel dagen zijn het? Dat is een keersom.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet de nullen er daarna weer achter.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Reken eerst zonder de nullen en zet ze er daarna weer achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Reken eerst zonder de nullen en zet ze er daarna allemaal weer achter.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Staat er een nul te veel achter? Reken eerst zonder de nullen en zet ze er daarna weer achter.  [nieuw]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen en zet ze er daarna weer achter. Kijk of je antwoord past: het is een keersom.  [nieuw]
- Status: hints klaar

## Somtype 7: # [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.

- Sleutel: nrOrigineel **22** · somtypeOrigineel “# [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: merge-generator G5 ronde 9 (#235) (7), T3 (1) · regel: G8-T3-schatten-afspraak, G5-r9 #235 generator
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), nul-fout-tientallen (8), optellen-ipv-vermenigvuldigen (8)
- Verschillende Claude-fout-hints: 12 (meest: “Tel de nullen goed mee.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-naar-057` (Claude T3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 dozen met elk 198 knikkers. Schat hoeveel dat ongeveer is: rond 198 af op honderdtallen en reken dan uit.
    - **Antwoord:** 800  (controle: ok)
    - **Fout-hints (Claude):** 792 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 80 → 200 × 4: tel de nullen goed. · 204 → 4 dozen van elk ongeveer 200: dat is een keersom.
    - **Uitleg (Claude):** 198 is bijna 200. 200 × 4 = 800. Precies is het 792, dus de schatting klopt goed.
  - `G5-GET-E07-merge-gen-004` (Claude merge-generator G5 ronde 9 (#235), None, niveau 1 → basis)
    - **Opgave:** 5 dozen met elk 104 potloden. Schat hoeveel dat ongeveer is: rond 104 af op honderdtallen en reken dan uit.
    - **Antwoord:** 500  (controle: ok)
    - **Fout-hints (Claude):** 792 → Precies uitgerekend. Hier vragen we de schatting met het ronde getal. · 80 → 200 × 4: tel de nullen goed. · 204 → 4 dozen van elk ongeveer 200: dat is een keersom.
    - **Uitleg (Claude):** 104 is ongeveer 100. 5 × 100 = 500.

- **Hint 1 (te schrijven):** Rond eerst af zoals in de vraag staat.
- **Hint 2 (te schrijven):** Reken dan uit met het ronde getal.
- **Ouderzin:** Je kind schat een keersom door eerst af te ronden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Dat is precies uitgerekend. De vraag is hoeveel het ongeveer is. Rond eerst af en reken dan uit met het ronde getal.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Tel de nullen van het ronde getal goed mee.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt opgeteld. In elke doos zitten er evenveel: dat is een keersom.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond eerst af zoals in de vraag staat. Reken dan uit met het ronde getal.  [nieuw]
- Status: hints klaar

## Somtype 8: Keersom in een verhaal: splits het grootste getal

- Sleutel: nrOrigineel **8** · somtypeOrigineel “[wie] eet # [ding] per dag. In [plek] wonen # [ding]. Hoeveel [ding] zijn dat per dag?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C7 (8) · regel: G5-C01-keer-context
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (14), optellen-ipv-vermenigvuldigen (8), cijfers-verwisseld (3), nul-fout-tientallen (1), tafelbuur (1)
- Verschillende Claude-fout-hints: 27 (meest: “6 × 10 = 60 klopt. Maar het waren 14 rondjes per speler. Wat moet je er nog bij doen?”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-441` (Claude C7, handmatig, niveau 1 → basis)
    - **Opgave:** Elke speler loopt 14 rondjes om het veld. Er zijn 6 spelers. Hoeveel rondjes lopen ze samen?
    - **Antwoord:** 84  (controle: ok)
    - **Fout-hints (Claude):** 60 → 6 × 10 = 60 klopt. Maar het waren 14 rondjes per speler. Wat moet je er nog bij doen? · 24 → 6 × 4 = 24 is het kleine stukje. Het grote stukje 6 × 10 ontbreekt nog. · 20 → 6 + 14 telt spelers en rondjes op. Maar élke speler loopt 14 rondjes, en er zijn 6 spelers.
    - **Uitleg (Claude):** Knip 14 in 10 en 4. 6 × 10 = 60. 6 × 4 = 24. Samen: 60 + 24 = 84.
  - `G5-GET-E07-claude-bank-442` (Claude C7, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een speler traint 4 dagen per week, elke dag 45 minuten. Hoeveel minuten traint hij per week?
    - **Antwoord:** 180  (controle: ok)
    - **Fout-hints (Claude):** 160 → 4 × 40 = 160 klopt. Maar het waren 45 minuten per dag. Wat moet je er nog bij doen? · 20 → 4 × 5 = 20 is het kleine stukje. Vergeet 4 × 40 niet. · 49 → 4 + 45 is niet genoeg: hij traint 4 dagen, élke dag 45 minuten.
    - **Uitleg (Claude):** Knip 45 in 40 en 5. 4 × 40 = 160. 4 × 5 = 20. Samen: 160 + 20 = 180.

- **Hint 1 (te schrijven):** Hoeveel is het elke keer, en hoe vaak? Steeds hetzelfde aantal: dat is een keersom.
- **Hint 2 (te schrijven):** Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `een stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je allebei de stukken keer het andere getal gedaan? Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.  [Claude, taalfix]
  - `cijfers omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in een andere volgorde. Kijk goed welk cijfer op welke plek hoort.  [Claude, taalfix]
  - `eenheden-stuk fout` (Claudes sleutel: tafelbuur) → Dat is te weinig. Reken het stuk met de eenheden nog eens na.  [Claude, taalfix]
  - `keer tien` (Claudes sleutel: nul-fout-tientallen) → Dat is te veel. Je hebt keer tien gedaan. Lees nog eens hoe vaak het is.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken het in stukken uit en tel de stukken op. Kijk of je antwoord past: het is een keersom.  [nieuw]
- Status: hints klaar

## Somtype 9: Verhaalsom delen: # [ding] eerlijk verdeeld over # [ding]. Hoeveel elk?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Verhaalsom delen: # [ding] eerlijk verdeeld over # [ding]. Hoeveel elk?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T1 (8) · regel: G8-T1-door-elkaar
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), tafelbuur (8)
- Verschillende Claude-fout-hints: 9 (meest: “Eerlijk verdelen is delen.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-naar-001` (Claude T1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 308 kinderen worden eerlijk verdeeld over 7 groepen. Hoeveel kinderen komen er in elke groep?
    - **Antwoord:** 44  (controle: n.v.t.)
    - **Fout-hints (Claude):** 301 → Eerlijk verdelen is delen. · 45 → 7 × 45 = 315, dat is te veel.
    - **Uitleg (Claude):** 308 : 7 = 44, want 7 × 44 = 308.
  - `G5-GET-E07-claude-bank-naar-007` (Claude T1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 132 kaartjes worden eerlijk verdeeld over 4 klassen. Hoeveel kaartjes krijgt elke klas?
    - **Antwoord:** 33  (controle: ok)
    - **Fout-hints (Claude):** 128 → Eerlijk verdelen is delen. · 34 → 4 × 34 = 136, dat is te veel.
    - **Uitleg (Claude):** 132 : 4 = 33, want 4 × 33 = 132.

- **Hint 1 (te schrijven):** Eerlijk verdelen is een deelsom. Overal komt evenveel: hoeveel is dat?
- **Hint 2 (te schrijven):** Zoek een keersom die je kent: hoeveel keer het aantal waarover je verdeelt, is het totaal? Begin met tien keer.
- **Ouderzin:** Je kind lost een verhaaltje op met een deelsom (eerlijk verdelen).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt het ene getal van het andere afgehaald. Eerlijk verdelen is delen. Overal komt evenveel: hoeveel is dat?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met een keersom. [getal2] keer jouw antwoord is meer dan [getal1].  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met een keersom. [getal2] keer jouw antwoord is minder dan [getal1].  [nieuw]
  - `tien vergeten` (fout = antwoord − 10) → Dat is tien te weinig. Heb je alle stukken van je verdeling bij elkaar opgeteld? Verdeel eerst tien keer, en daarna de rest.  [nieuw]
  - `andere fout` (andere fout) → Reken na met een keersom: jouw antwoord keer het aantal waarover je verdeelt, moet het totaal zijn.  [nieuw]
- Status: hints klaar

## Somtype 10: Verhaalsom keer: # groepjes met elk # [ding]. Hoeveel samen?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Verhaalsom keer: # groepjes met elk # [ding]. Hoeveel samen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T1 (8) · regel: G8-T1-door-elkaar
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (8), deel-vergeten-bij-splitsen (8)
- Verschillende Claude-fout-hints: 8 (meest: “Elk evenveel en samen: dat is keer.”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-naar-002` (Claude T1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3 kinderen hebben elk 13 knikkers. Hoeveel knikkers zijn dat samen?
    - **Antwoord:** 39  (controle: ok)
    - **Fout-hints (Claude):** 16 → Elk evenveel en samen: dat is keer. · 30 → Je vergat 3 × 3.
    - **Uitleg (Claude):** 3 × 13 = 3 × 10 + 3 × 3 = 30 + 9 = 39.
  - `G5-GET-E07-claude-bank-naar-024` (Claude T1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In 6 dozen zitten elk 38 potloden. Hoeveel potloden zijn dat samen?
    - **Antwoord:** 228  (controle: ok)
    - **Fout-hints (Claude):** 44 → Elk evenveel en samen: dat is keer. · 180 → Je vergat 6 × 8.
    - **Uitleg (Claude):** 6 × 38 = 6 × 30 + 6 × 8 = 180 + 48 = 228.

- **Hint 1 (te schrijven):** Het is steeds evenveel. Hoeveel zijn het er samen? Dat is een keersom.
- **Hint 2 (te schrijven):** Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `een stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je alle stukken bij elkaar opgeteld? Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal en tel de stukken op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken het in stukken uit en tel de stukken op. Kijk of je antwoord past: het is een keersom.  [nieuw]
- Status: hints klaar

## Somtype 11: Keersom in een verhaal: een rond tiental

- Sleutel: nrOrigineel **9** · somtypeOrigineel “[wie] eet # kilo bladeren per uur. Hoeveel kilo eet hij in # uur?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C7 (4) · regel: G5-C01-keer-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (8), optellen-ipv-vermenigvuldigen (4)
- Verschillende Claude-fout-hints: 12 (meest: “7 × 3 = 21 klopt, maar het waren dozen van 30. Waar is de nul gebleven?”)
- Voorbeelden:
  - `G5-GET-E07-claude-bank-439` (Claude C7, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een club koopt 7 dozen met 30 ballen. Hoeveel ballen zijn dat?
    - **Antwoord:** 210  (controle: ok)
    - **Fout-hints (Claude):** 21 → 7 × 3 = 21 klopt, maar het waren dozen van 30. Waar is de nul gebleven? · 2100 → Dat zijn wel heel veel ballen. 30 heeft één nul, dus 21 krijgt er ook één nul bij. · 37 → 7 + 30 is één doos plus het aantal dozen. Maar er zijn 7 dozen van elk 30 ballen.
    - **Uitleg (Claude):** 7 × 30 lijkt op 7 × 3. 7 × 3 = 21. Nu de nul van 30 er weer aan: 210.
  - `G5-GET-E07-claude-bank-422` (Claude C7, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een dino eet 40 kilo bladeren per uur. Hoeveel kilo eet hij in 6 uur?
    - **Antwoord:** 240  (controle: ok)
    - **Fout-hints (Claude):** 24 → 6 × 4 = 24 klopt, maar het was 40 kilo per uur. Plak de nul er weer aan. · 2400 → Dat is een nul te veel. 40 heeft één nul, dus 24 krijgt er ook maar één. · 46 → 6 + 40 telt de uren bij de kilo's op. Maar elk uur eet hij 40 kilo, 6 uur lang.
    - **Uitleg (Claude):** 6 × 40 lijkt op 6 × 4. 6 × 4 = 24. De nul van 40 er weer aan: 240.

- **Hint 1 (te schrijven):** Hoeveel is het elke keer, en hoe vaak? Steeds hetzelfde aantal: dat is een keersom.
- **Hint 2 (te schrijven):** Reken eerst zonder de nullen. Zet de nullen er daarna weer achter.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Reken eerst zonder de nullen en zet ze er daarna weer achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Reken eerst zonder de nullen en zet ze er daarna allemaal weer achter.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Staat er een nul te veel achter? Reken eerst zonder de nullen en zet ze er daarna weer achter.  [nieuw]
  - `andere fout` (andere fout) → Reken eerst zonder de nullen en zet ze er daarna weer achter. Kijk of je antwoord past: het is een keersom.  [nieuw]
- Status: hints klaar
