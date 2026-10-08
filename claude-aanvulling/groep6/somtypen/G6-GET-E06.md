# G6-GET-E06 — Keer en delen tot 10.000

Onze omschrijving: ×÷ ±10.000: standaard + strategieën + schattend · in onze bank: 8 items

Claude-vragen gemapt: **294** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # × # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **235** · Claude-doelen: C15 (235) · regel: G6-C03-keer-2x2
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): een-ernaast (172), tiental-ernaast (160), deel-vergeten-bij-splitsen (71), plaatswaarde-verkeerd (49), cijfers-van-getal2-opgeteld (34)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-206` (Claude C15, bank, niveau 3 → toepassen)
    - **Opgave:** 13 × 13 =
    - **Antwoord:** 169  (controle: ok)
    - **Fout-hints (Claude):** 179 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.
  - `G6-GET-E06-claude-bank-080` (Claude C15, bank, niveau 3 → toepassen)
    - **Opgave:** 31 × 34 =
    - **Antwoord:** 1054  (controle: ok)
    - **Fout-hints (Claude):** 1044 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 1055 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Splits het eerste getal in tientallen en eenheden.
- **Hint 2 (te schrijven):** Doe elk stuk keer het tweede getal. Tel de uitkomsten daarna bij elkaar op.
- **Ouderzin:** Je kind rekent een keersom uit met twee getallen van twee cijfers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Kijk naar het teken: het is een keersom.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is tien keer te weinig. Ben je een nul vergeten? Een tiental keer een getal krijgt een nul aan het eind.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken elk stuk nog eens na, en tel alle stukken goed op.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken elk stuk nog eens na, en tel alle stukken goed op.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Reken de stukken nog eens na en tel ze goed op.  [nieuw]
  - `cijfers van het tweede getal opgeteld` (fout = getal1 × (som van de cijfers van getal2)) → Je hebt de cijfers van het tweede getal bij elkaar opgeteld. Zo reken je niet keer het hele getal. Splits het eerste getal in tientallen en eenheden, en doe elk stuk keer het hele tweede getal.  [nieuw]
  - `stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je elk stuk keer het hele tweede getal gedaan, en niet keer één cijfer of keer de cijfers bij elkaar? Tel daarna alle stukken op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het eerste getal in tientallen en eenheden. Doe elk stuk keer het tweede getal en tel alles op.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoe reken je # × # handig uit?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoe reken je # × # handig uit?” (koppeling: claudeId)
- Items: **25** · Claude-doelen: T10 (25) · regel: G6-T03-handig-keerdeel
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): stukje-keer-het-ronde-getal (14), verkeerde-bewerking (13), verkeerd-stukje (13), afronden-verkeerde-kant (10)
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-250` (Claude T10, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe reken je 198 × 7 handig uit?
    - **Opties:** A) 200 × 10 − 2 × 7 · B) 200 × 7 − 2 × 200 · C) 200 × 7 − 2 × 7
    - **Antwoord:** 200 × 7 − 2 × 7  (controle: ok)
    - **Fout-hints (Claude):** 200 × 7 − 2 × 200 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 200 × 10 − 2 × 7 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G6-GET-E06-claude-bank-258` (Claude T10, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe reken je 602 × 4 handig uit?
    - **Opties:** A) 600 × 4 + 2 × 4 · B) 600 × 4 + 2 × 600 · C) 600 × 4 + 3 × 4
    - **Antwoord:** 600 × 4 + 2 × 4  (controle: ok)
    - **Fout-hints (Claude):** 600 × 4 + 2 × 600 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 600 × 4 + 3 × 4 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.

- **Hint 1 (te schrijven):** Maak het grote getal rond: welk honderdtal ligt er vlak bij? Het kleine getal blijft zoals het is.
- **Hint 2 (te schrijven):** Reken het honderdtal keer het kleine getal. Was het grote getal kleiner dan het honderdtal? Dan haal je het stukje keer het kleine getal eraf. Was het groter? Dan doe je het erbij.
- **Ouderzin:** Je kind kiest een handige manier voor een keersom: het grote getal rond maken en daarna bijstellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerd teken` (Claudes sleutel: verkeerde-bewerking) → Het teken in het midden klopt niet. Was het grote getal kleiner dan het honderdtal? Dan haal je het stukje eraf. Was het groter? Dan doe je het erbij.  [Claude, taalfix]
  - `kleine getal veranderd` (Claudes sleutel: afronden-verkeerde-kant) → Je hebt ook het kleine getal veranderd. Het kleine getal blijft zoals het is: alleen het grote getal maak je rond.  [Claude, taalfix]
  - `stukje keer honderdtal` (Claudes sleutel: stukje-keer-het-ronde-getal) → Het laatste stuk klopt niet. Het stukje doe je keer het kleine getal, net als het honderdtal.  [Claude, taalfix]
  - `verkeerd stukje` (Claudes sleutel: verkeerd-stukje) → Het stukje klopt niet. Hoeveel scheelt het grote getal met het honderdtal?  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak het grote getal rond en doe dat keer het kleine getal. Hoeveel scheelt het grote getal met het honderdtal? Dat stukje keer het kleine getal haal je eraf of doe je erbij.  [nieuw]
- Status: hints klaar

## Somtype 3: In [plek] staan # rijen met # [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In [plek] staan # rijen met # [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C15 (12) · regel: G6-C03-keer-2x2
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (25), optellen-ipv-vermenigvuldigen (12), eenheden-niet-keer-gedaan (10)
- Verschillende Claude-fout-hints: 45 (meest: “Als je allebei de getallen splitst, moet je álle vier de stukjes uitrekenen: ook 4 × 40.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-276` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** In de zaal staan 15 rijen met 32 stoelen. Hoeveel stoelen zijn dat?
    - **Antwoord:** 480  (controle: ok)
    - **Fout-hints (Claude):** 450 → 15 × 30 is het grote stukje. Er komt nog 15 × 2 bij. · 452 → Het kleine stukje is ook een keersom. 15 × 2, niet alleen 2. · 47 → 15 rijen van elk 32. Dat is een keersom. · 330 → Als je allebei de getallen splitst, moet je álle vier de stukjes uitrekenen: ook 5 × 30.
    - **Uitleg (Claude):** Splits 32 in 30 en 2. 15 × 30 = 450. 15 × 2 = 30. Samen: 450 + 30 = 480.
  - `G6-GET-E06-claude-bank-273` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op de parkeerplaats staan 24 rijen met 44 auto's. Hoeveel auto's zijn dat?
    - **Antwoord:** 1056  (controle: ok)
    - **Fout-hints (Claude):** 960 → 24 × 40 is het grote stukje. Er komt nog 24 × 4 bij. · 964 → Het kleine stukje is ook een keersom. 24 × 4, niet alleen 4. · 68 → 24 rijen van elk 44. Dat is een keersom. · 896 → Als je allebei de getallen splitst, moet je álle vier de stukjes uitrekenen: ook 4 × 40.
    - **Uitleg (Claude):** Splits 44 in 40 en 4. 24 × 40 = 960. 24 × 4 = 96. Samen: 960 + 96 = 1056.

- **Hint 1 (te schrijven):** Elke rij heeft evenveel: dat is een keersom. Het aantal rijen keer het aantal in elke rij.
- **Hint 2 (te schrijven):** Splits het aantal rijen in tientallen en eenheden (als het die heeft). Doe elk stuk keer het aantal in elke rij en tel de uitkomsten op.
- **Ouderzin:** Je kind rekent uit hoeveel er in een aantal rijen staan: een keersom met twee getallen van twee cijfers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. In elke rij staan er evenveel: dat is een keersom.  [nieuw]
  - `eenheden niet keer gedaan` (fout = getal1 × tientallen(getal2) + eenheden(getal2)) → Je hebt de eenheden er alleen bijgezet. Doe ook de eenheden keer het andere getal, en tel daarna alle stukken op.  [nieuw]
  - `stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je elk stuk keer het hele andere getal gedaan, ook de eenheden? Tel daarna alle stukken op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken het aantal rijen keer het aantal in elke rij. Splits een getal in tientallen en eenheden (als het die heeft), en tel de stukken op.  [nieuw]
- Status: hints klaar

## Somtype 4: Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **10** · Claude-doelen: T3 (10) · regel: G6-r9 #321 (uit G5)
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-uitg5-001` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Hoeveel is 18 × 54 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 1000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1200 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 800 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G6-GET-E06-claude-bank-uitg5-006` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Hoeveel is 18 × 21 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 400  (controle: n.v.t.)
    - **Fout-hints (Claude):** 378 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 600 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond beide getallen af op tientallen. Kijk bij elk getal naar de eenheden: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Reken eerst zonder de nullen en zet de nullen er daarna weer achter.
- **Ouderzin:** Je kind schat een keersom: eerst beide getallen afronden op tientallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 × getal2) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Heb je beide getallen goed afgerond op tientallen? Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op tientallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 5: Welke som is evenveel als # × #?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Welke som is even veel als # × #?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T10 (6) · regel: G6-T03-handig-keerdeel
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): tweede-getal-klopt-niet (8), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 2 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-284` (Claude T10, bank, niveau 3 → toepassen)
    - **Opgave:** Welke som is evenveel als 32 × 45?
    - **Opties:** A) 16 × 45 · B) 64 × 90 · C) 16 × 90
    - **Antwoord:** 16 × 90  (controle: ok)
    - **Fout-hints (Claude):** 64 × 90 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 16 × 45 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G6-GET-E06-claude-bank-282` (Claude T10, bank, niveau 3 → toepassen)
    - **Opgave:** Welke som is evenveel als 40 × 35?
    - **Opties:** A) 80 × 70 · B) 20 × 70 · C) 20 × 140
    - **Antwoord:** 20 × 70  (controle: ok)
    - **Fout-hints (Claude):** 80 × 70 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 20 × 140 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Neem de helft van het eerste getal.
- **Hint 2 (te schrijven):** Is het ene getal de helft geworden? Dan moet het andere getal twee keer zo groot worden. Zo blijft de uitkomst gelijk.
- **Ouderzin:** Je kind kiest een keersom met dezelfde uitkomst: de helft van het ene getal, en het andere getal twee keer zo groot.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `allebei groter` (Claudes sleutel: verkeerde-bewerking) → Je hebt allebei de getallen groter gemaakt. Dan wordt de uitkomst ook groter. Neem de helft van het eerste getal en maak het tweede getal twee keer zo groot.  [Claude, taalfix]
  - `tweede getal klopt niet` (Claudes sleutel: tweede-getal-klopt-niet) → De helft klopt, maar het tweede getal niet. Het tweede getal moet precies twee keer zo groot worden.  [Claude, taalfix]
  - `andere fout` (andere fout) → Neem de helft van het eerste getal en maak het tweede getal twee keer zo groot. Dan blijft de uitkomst gelijk.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Welke som is even veel als # × #?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 6: # [ding] met # [ding]. Hoeveel [ding]? Reken handig.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# [ding] met # [ding]. Hoeveel [ding]? Reken handig.” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T10 (2) · regel: G6-T03-handig-keerdeel
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (4), optellen-ipv-vermenigvuldigen (2)
- Verschillende Claude-fout-hints: 3 (meest: “Tel de nullen nog eens. Denk aan 4 × 25 = 100.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-001` (Claude T10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 8 dozen met 250 punaises. Hoeveel punaises? Reken handig.
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 200 → Tel de nullen nog eens. Denk aan 4 × 25 = 100. · 20.000 → Een nul te veel. Denk aan 4 × 25 = 100. · 258 → Dozen keer inhoud is een keersom.
    - **Uitleg (Claude):** 250 past mooi in 1000 (4 keer). 8 × 250 = 2000.
  - `G6-GET-E06-claude-bank-002` (Claude T10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 12 dozen met 250 paperclips. Hoeveel paperclips? Reken handig.
    - **Antwoord:** 3000  (controle: ok)
    - **Fout-hints (Claude):** 200 → Tel de nullen nog eens. Denk aan 4 × 25 = 100. · 20.000 → Een nul te veel. Denk aan 4 × 25 = 100. · 258 → Dozen keer inhoud is een keersom.
    - **Uitleg (Claude):** 250 past mooi in 1000 (4 keer). 12 × 250 = 3000.

- **Hint 1 (te schrijven):** In elke doos zitten er evenveel: dat is een keersom.
- **Hint 2 (te schrijven):** Reken handig: splits het grote getal in ronde stukken, of verdubbel steeds.
- **Ouderzin:** Je kind rekent een keersom met een rond getal handig uit.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. In elke doos zitten er evenveel: dat is een keersom.  [nieuw]
  - `nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: hoeveel nullen horen er aan het eind?  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is tien keer te weinig. Ben je een nul vergeten? Tel de nullen nog eens.  [nieuw]
  - `andere fout` (andere fout) → Reken het aantal dozen keer hoeveel er in elke doos zitten. Splits het grote getal in ronde stukken, of verdubbel steeds.  [nieuw]
- Status: hints klaar

## Somtype 7: Er zijn # [ding]. Ze gaan eerlijk over # [ding]. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Er zijn # [ding]. Ze gaan eerlijk over # [ding]. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: T9 (2) · regel: G6-C06-deel
- Getallenruimte: 0–10.000 · type: meerkeuze
- Uit de G5-park: 2 items
- Denkfouten (Claude): omgekeerd-gedeeld (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 2 (meest: “Wat verdeel je? Dat getal komt vóór het deelteken.”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-239` (Claude T9, bank, niveau 2 → toepassen)
    - **Opgave:** Er zijn 1040 appels. Ze worden eerlijk verdeeld over 20 borden. Welke som hoort bij dit verhaal?
    - **Opties:** A) 1040 : 20 · B) 1040 × 20 · C) 20 : 1040
    - **Antwoord:** 1040 : 20  (controle: ok)
    - **Fout-hints (Claude):** 20 : 1040 → Wat verdeel je? Dat getal komt vóór het deelteken. · 1040 × 20 → Je verdeelt. Is dat keer of gedeeld door?
  - `G6-GET-E06-claude-bank-238` (Claude T9, bank, niveau 2 → toepassen)
    - **Opgave:** Er zijn 1200 ballen. Ze worden eerlijk verdeeld over 15 tafels. Welke som hoort bij dit verhaal?
    - **Opties:** A) 1200 × 15 · B) 1200 : 15 · C) 15 : 1200
    - **Antwoord:** 1200 : 15  (controle: ok)
    - **Fout-hints (Claude):** 15 : 1200 → Wat verdeel je? Dat getal komt vóór het deelteken. · 1200 × 15 → Je verdeelt. Is dat keer of gedeeld door?

- **Hint 1 (te schrijven):** Lees het verhaal: wat wordt er verdeeld, en over hoeveel?
- **Hint 2 (te schrijven):** Eerlijk verdelen is een deelsom. Welk getal wordt er verdeeld?
- **Ouderzin:** Je kind kiest de deelsom die bij een verhaaltje hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keersom` (de keersom) → Je kiest een keersom, maar er wordt eerlijk verdeeld. Verdelen is een deelsom.  [nieuw]
  - `getallen omgedraaid` (Claudes sleutel: omgekeerd-gedeeld) → De getallen staan andersom. Wat verdeel je? Dat getal komt vóór het deelteken.  [Claude, taalfix]
  - `andere fout` (andere fout) → Wat wordt er verdeeld? Dat getal komt vóór het deelteken. Over hoeveel? Dat getal komt erachter.  [nieuw]
- Status: hints klaar

## Somtype 8: In [plek] staan # [ding] met elk # [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “In [plek] staan # [ding] met elk # [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C15 (2) · regel: G6-C03-keer-2x2
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (2), eenheden-niet-keer-gedaan (2), onthouden-vergeten (2)
- Verschillende Claude-fout-hints: 5 (meest: “Controleer het optellen van de twee stukken. Een duizendtal te veel?”)
- Voorbeelden:
  - `G6-GET-E06-claude-bank-265` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** In de drukkerij staan 15 dozen met elk 485 folders. Hoeveel folders zijn dat?
    - **Antwoord:** 7275  (controle: ok)
    - **Fout-hints (Claude):** 4850 → 485 × 10 is het grote stuk. Er komt nog 485 × 5 bij. · 4855 → Ook het kleine stuk is een keersom. 485 × 5. · 8275 → Controleer het optellen van de twee stukken. Een duizendtal te veel?
    - **Uitleg (Claude):** Splits 15 in 10 en 5. 485 × 10 = 4850. 485 × 5 = 2425. Samen 4850 + 2425 = 7275.
  - `G6-GET-E06-claude-bank-266` (Claude C15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** In de drukkerij staan 17 dozen met elk 433 folders. Hoeveel folders zijn dat?
    - **Antwoord:** 7361  (controle: ok)
    - **Fout-hints (Claude):** 4330 → 433 × 10 is het grote stuk. Er komt nog 433 × 7 bij. · 4337 → Ook het kleine stuk is een keersom. 433 × 7. · 8361 → Controleer het optellen van de twee stukken. Een duizendtal te veel?
    - **Uitleg (Claude):** Splits 17 in 10 en 7. 433 × 10 = 4330. 433 × 7 = 3031. Samen 4330 + 3031 = 7361.

- **Hint 1 (te schrijven):** In elke doos zitten er evenveel: dat is een keersom. Reken het aantal dozen keer hoeveel er in elke doos zitten.
- **Hint 2 (te schrijven):** Splits het getal van twee cijfers in tientallen en eenheden (als het die heeft). Doe elk stuk keer het grote getal en tel de uitkomsten op.
- **Ouderzin:** Je kind rekent een keersom uit: een getal van twee cijfers keer een getal van drie cijfers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. In elke doos zitten er evenveel: dat is een keersom.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Tel de stukken nog eens goed bij elkaar op. Neem je alleen één mee als een kolom op tien of meer komt?  [nieuw]
  - `eenheden niet keer gedaan` (fout = getal1 × tientallen(getal2) + eenheden(getal2)) → Je hebt de eenheden er alleen bijgezet. Doe ook de eenheden keer het andere getal, en tel daarna alle stukken op.  [nieuw]
  - `stuk vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is te weinig. Heb je elk stuk keer het hele andere getal gedaan, ook de eenheden? Tel daarna alle stukken op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het getal van twee cijfers in tientallen en eenheden (als het die heeft). Doe elk stuk keer het grote getal en tel alles op.  [nieuw]
- Status: hints klaar
