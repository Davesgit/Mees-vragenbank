# G7-GET-04 — Vermenigvuldigen en delen

Onze omschrijving: Vermenigvuldigen/delen + combinaties · in onze bank: 8 items

Claude-vragen gemapt: **882** in **11** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # : # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# : # =” (koppeling: claudeId)
- Items: **409** · Claude-doelen: B17 (378), C18 (31) · regel: G7-K02-komma-delen, G7-C01-staartdeling
- Getallenruimte: 0–10.000, kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (623), komma-verschoven (114), tiental-ernaast (28), een-ernaast (25), verkeerde-bewerking (19), deel-vergeten-bij-splitsen (9)
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

- **Hint 1 (te schrijven):** Hoe vaak past het getal waardoor je deelt in het getal dat je deelt? Schat eerst met ronde getallen.
- **Hint 2 (te schrijven):** Splits het getal dat je deelt in stukken die je makkelijk deelt. Deel elk stuk en tel de uitkomsten op. Staat er een komma in het getal? Zet die in je antwoord op dezelfde plek. Blijft er aan het eind iets over? Maak er tienden of honderdsten van en deel verder achter de komma. Reken na met een keersom.
- **Ouderzin:** Je kind deelt, ook met kommagetallen, door te splitsen en na te rekenen met een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiende ernaast` (fout = antwoord ± 0,1) → Dat is een tiende ernaast. Reken de tienden nog eens na. Klopt het?  [nieuw]
  - `een honderdste ernaast` (fout = antwoord ± 0,01) → Dat is een honderdste ernaast. Reken de honderdsten nog eens na. Klopt het?  [nieuw]
  - `één ernaast` (fout = antwoord ± 1) → Dat is één ernaast. Hoe vaak past het getal waardoor je deelt er precies in?  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Klopt het cijfer van de tientallen?  [nieuw]
  - `tien te weinig` (fout = antwoord - 10) → Dat is tien te weinig. Klopt het cijfer van de tientallen?  [nieuw]
  - `stuk vergeten bij splitsen` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is veel te weinig. Heb je de uitkomsten van alle stukken opgeteld?  [Claude, taalfix]
  - `keer in plaats van delen` (Claudes sleutel: verkeerde-bewerking) → Heb je keer gedaan in plaats van gedeeld? Kijk naar het teken.  [Claude, taalfix]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Schat eerst: hoe groot is de uitkomst ongeveer?  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel in stukken die je makkelijk deelt, en reken na met een keersom.  [nieuw]
- Status: hints klaar

## Somtype 2: # × # =

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **369** · Claude-doelen: B16 (369) · regel: G7-K01-komma-keer
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (567), komma-verschoven (163), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-833` (Claude B16, bank, niveau 3 → toepassen)
    - **Opgave:** 0,2 × 3 =
    - **Antwoord:** 0,6  (controle: ok)
    - **Fout-hints (Claude):** 0,7 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 0,61 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G7-GET-04-claude-bank-841` (Claude B16, bank, niveau 3 → toepassen)
    - **Opgave:** 2,02 × 9 =
    - **Antwoord:** 18,18  (controle: ok)
    - **Fout-hints (Claude):** 18,28 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 18,19 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.

- **Hint 1 (te schrijven):** Hoe groot is de uitkomst ongeveer? Schat eerst met ronde getallen.
- **Hint 2 (te schrijven):** Reken eerst zonder de komma. Tel daarna hoeveel cijfers er achter de komma staan in de som, en zet in je antwoord evenveel cijfers achter de komma. Kijk of het past bij je schatting.
- **Ouderzin:** Je kind rekent keersommen met kommagetallen en zet de komma op de goede plek met een schatting.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiende ernaast` (fout = antwoord ± 0,1) → Dat is een tiende ernaast. Reken de tienden nog eens na. Klopt het?  [nieuw]
  - `een honderdste ernaast` (fout = antwoord ± 0,01) → Dat is een honderdste ernaast. Reken de honderdsten nog eens na. Klopt het?  [nieuw]
  - `gedeeld in plaats van keer` (Claudes sleutel: verkeerde-bewerking) → Heb je gedeeld in plaats van keer gedaan? Kijk naar het teken.  [Claude, taalfix]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Schat eerst: hoe groot is de uitkomst ongeveer?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken zonder komma en zet de komma terug met een schatting.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Hoeveel krijgt elk? Wat overblijft, blijft over.
- **Hint 2 (te schrijven):** Splits het aantal dat je verdeelt in stukken die je makkelijk deelt. Deel elk stuk en tel de uitkomsten op. Wat aan het eind overblijft, is de rest: die telt niet mee.
- **Ouderzin:** Je kind verdeelt eerlijk met een deling met rest; de rest blijft over.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Dat is één te veel. Kan iedereen er echt zoveel krijgen?  [nieuw]
  - `tien te weinig` (fout = antwoord - 10) → Dat is tien te weinig. Heb je bij het splitsen een stuk vergeten?  [nieuw]
  - `de rest` (fout = de rest van getal1 : getal2) → Dat is wat er overblijft. Hoeveel krijgt elk?  [nieuw]
  - `andere fout` (andere fout) → Deel eerlijk en laat de rest over.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Alle stuks kosten evenveel. Hoe verdeel je het bedrag?
- **Hint 2 (te schrijven):** Deel het bedrag door het aantal. Blijft er iets over? Maak er centen van en deel verder. Reken na met een keersom.
- **Ouderzin:** Je kind rekent de prijs van één stuk uit door het bedrag te delen, tot op de cent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `bedrag voor alles` (fout = getal2) → Dat is het bedrag voor alles samen. Wat kost één?  [nieuw]
  - `komma verschoven` (fout = antwoord × 10) → Dat is tien keer te veel. Kan één stuk zoveel kosten? Vergelijk met het bedrag voor alles samen.  [nieuw]
  - `aantal eraf gehaald` (Claudes sleutel: verkeerde-bewerking) → Heb je het aantal eraf gehaald? Je wilt weten wat één kost: dan verdeel je het bedrag over alle stuks.  [Claude, taalfix]
  - `komma anders verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Schat eerst: hoeveel euro kost één ongeveer?  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel het bedrag door het aantal, tot op de cent.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Gemiddeld betekent: hoeveel heeft elk als je alles eerlijk verdeelt?
- **Hint 2 (te schrijven):** Tel alle getallen bij elkaar op. Deel de uitkomst door hoeveel getallen het zijn. Dat is het gemiddelde.
- **Ouderzin:** Je kind rekent het gemiddelde uit: alles optellen en delen door het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet gedeeld` (fout = de som van de getallen) → Dat is alles samen. Deel je dat nog door hoeveel getallen het zijn?  [nieuw]
  - `middelste getal` (fout = het middelste getal (op grootte)) → Dat is het middelste getal als je de getallen van klein naar groot zet. Het gemiddelde is iets anders: tel alles op en deel door het aantal.  [nieuw]
  - `niet het gemiddelde` (Claudes sleutel: verhoudingstabel-verkeerd) → Heb je alle getallen opgeteld en daarna gedeeld door het aantal? Reken het na.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel alle getallen op en deel door hoeveel getallen het zijn.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Hoe vaak past het aantal per keer erin? En hoeveel blijven er dan over?
- **Hint 2 (te schrijven):** Reken uit hoe vaak het aantal per keer erin past. Doe dat keer het aantal per keer, en haal de uitkomst van het totaal af. Wat overblijft, is het antwoord.
- **Ouderzin:** Je kind rekent uit hoeveel er overblijft na een deling met rest.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een keer te weinig gevuld` (fout = antwoord + getal2) → Dat is te veel. Er past nog een volle keer in. Wat blijft er dan over?  [nieuw]
  - `hoe vaak het past` (Claudes sleutel: rest-vergeten) → Dat is hoe vaak het past. De vraag is hoeveel er overblijven.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoe vaak het past, en haal dat stuk van het totaal af.  [nieuw]
- Status: hints klaar

## Somtype 7: # kilo/liter [ding] wordt eerlijk verdeeld over # [wie]. Hoeveel krijgt elk(e) [wie]?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# kilo/liter [ding] wordt eerlijk verdeeld over # [wie]. Hoeveel krijgt elk(e) [wie]?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B17 (8) · regel: G7-K02-komma-delen
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (4), tafelbuur (4), rest-vergeten (4), kommagetal-als-geheel (4)
- Verschillende Claude-fout-hints: 12 (meest: “Komma terugzetten: het antwoord heeft één cijfer achter de komma.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-473` (Claude B17, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 4,5 liter limonade wordt eerlijk verdeeld over 3 kannen. Hoeveel liter krijgt elke kan?
    - **Antwoord:** 1,5  (controle: ok)
    - **Fout-hints (Claude):** 15 → Komma terugzetten: het antwoord heeft één cijfer achter de komma. · 2,5 → Controleer. 3 × jouw antwoord moet 4,5 zijn.
    - **Uitleg (Claude):** Reken zonder komma: 45 : 3 = 15. Zet de komma terug: 1,5.
  - `G7-GET-04-claude-bank-471` (Claude B17, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 242 kilo appels wordt eerlijk verdeeld over 8 kratten. Hoeveel kilo krijgt elke krat?
    - **Antwoord:** 30,25  (controle: ok)
    - **Fout-hints (Claude):** 30 → Er blijft 1 kilo over. Die verdeel je ook, in stukjes. · 30,1 → De rest 1 is niet zomaar het cijfer achter de komma. Deel de rest ook door 8.
    - **Uitleg (Claude):** 8 × 30 = 240, blijft 2 over. 2 : 8 = 0,25. Samen 30,25.

- **Hint 1 (te schrijven):** Verdeel eerst het hele getal. Wat overblijft, verdeel je verder achter de komma.
- **Hint 2 (te schrijven):** Deel eerst het hele getal. Blijft er iets over? Maak er tienden van en deel die ook. Blijft er weer iets over, maak er dan honderdsten van.
- **Ouderzin:** Je kind deelt eerlijk tot achter de komma: wat overblijft, wordt tienden en honderdsten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het hele getal` (fout = het hele getal van het kommagetal) → Dat is alleen het hele getal. Wat overblijft, kun je ook verdelen. Reken je verder achter de komma?  [nieuw]
  - `één ernaast` (fout = antwoord ± 1) → Dat is één ernaast. Hoe vaak past het getal waardoor je deelt erin?  [nieuw]
  - `rest achter de komma` (Claudes sleutel: kommagetal-als-geheel) → Is dat de rest achter de komma gezet? Wat overblijft, deel je verder.  [Claude, taalfix]
  - `één te veel` (Claudes sleutel: tafelbuur) → Dat is één te veel. Hoe vaak past het getal waardoor je deelt in het hele getal?  [Claude, taalfix]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Schat eerst: hoe groot is de uitkomst ongeveer?  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel eerst het hele getal en verdeel wat overblijft verder achter de komma.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Hoe vaak past het getal waardoor je deelt in het grote getal? Schat eerst met ronde getallen.
- **Hint 2 (te schrijven):** Haal steeds een groot stuk af dat je makkelijk uitrekent, bijvoorbeeld honderd keer of tien keer het getal waardoor je deelt. Schrijf op hoe vaak je het afhaalt. Tel aan het eind alle keren op.
- **Ouderzin:** Je kind deelt een groot getal door een getal van twee cijfers, met handige stukken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Hoe vaak heb je tien keer het getal waardoor je deelt eraf gehaald?  [nieuw]
  - `tien te weinig` (fout = antwoord - 10) → Dat is tien te weinig. Hoe vaak heb je tien keer het getal waardoor je deelt eraf gehaald?  [nieuw]
  - `een nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je een nul te veel opgeschreven?  [nieuw]
  - `andere fout` (andere fout) → Haal handige stukken af en tel op hoe vaak je het getal waardoor je deelt eraf haalt.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wat weegt één? En hoeveel stuks zijn het? Alle stuks samen is een keersom.
- **Hint 2 (te schrijven):** Bij keer tien schuift de komma één plek naar rechts, bij keer honderd twee plekken. Tel de nullen van het aantal en schuif de komma zoveel plekken. Is er geen cijfer meer om voorbij te schuiven? Zet er dan een nul bij.
- **Ouderzin:** Je kind rekent een gewicht keer een rond aantal door de komma te verschuiven, en zet er een nul bij als er geen cijfer meer is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma een plek te ver` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen van het aantal: zoveel plekken schuift de komma.  [nieuw]
  - `komma de verkeerde kant op` (Claudes sleutel: komma-verschoven) → Is de uitkomst groter of kleiner dan het gewicht van één? Bij keer wordt het meer.  [Claude, taalfix]
  - `aantal erbij opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je het aantal erbij opgeteld? Je wilt weten wat al die stuks samen wegen: dat is keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe het gewicht van één keer het aantal: schuif de komma.  [nieuw]
- Status: hints klaar

## Somtype 10: Een [ding] weegt # kg. Hoeveel wegen # [ding]?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een [ding] weegt # kg. Hoeveel wegen # [ding]?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B16 (4) · regel: G7-K01-komma-keer
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (4), deel-vergeten-bij-splitsen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Komma terugzetten: één cijfer achter de komma.”)
- Voorbeelden:
  - `G7-GET-04-claude-bank-857` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 2,6 kg. Hoeveel wegen 3 pakketten?
    - **Antwoord:** 7,8  (controle: ok)
    - **Fout-hints (Claude):** 78 → Komma terugzetten: één cijfer achter de komma. · 6,6 → Ook de tienden gaan keer het aantal.
    - **Uitleg (Claude):** Zonder komma: 3 × 26 = 78. Komma terug (één cijfer): 7,8.
  - `G7-GET-04-claude-bank-858` (Claude B16, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pakket weegt 3,9 kg. Hoeveel wegen 12 pakketten?
    - **Antwoord:** 46,8  (controle: ok)
    - **Fout-hints (Claude):** 468 → Komma terugzetten: één cijfer achter de komma. · 36,9 → Ook de tienden gaan keer het aantal.
    - **Uitleg (Claude):** Zonder komma: 12 × 39 = 468. Komma terug (één cijfer): 46,8.

- **Hint 1 (te schrijven):** Wat weegt één? Hoeveel stuks zijn het? Schat eerst hoe zwaar alles samen ongeveer is.
- **Hint 2 (te schrijven):** Splits het gewicht in het hele getal en het stuk achter de komma. Doe beide keer het aantal. Tel de uitkomsten bij elkaar op.
- **Ouderzin:** Je kind rekent een kommagetal keer een aantal door het te splitsen in het hele getal en de tienden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Staat de komma op de goede plek?  [nieuw]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Schat eerst: hoe zwaar is het ongeveer?  [Claude, taalfix]
  - `stuk achter de komma niet keer gedaan` (Claudes sleutel: deel-vergeten-bij-splitsen) → Heb je ook het stuk achter de komma keer gedaan?  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het gewicht, doe beide stukken keer het aantal en tel op.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Alle groepjes zijn even groot. Welke keersom maak je?
- **Hint 2 (te schrijven):** Splits het kleinste getal in tientallen en eenheden. Doe elk stuk keer het grote getal. Tel de twee uitkomsten bij elkaar op.
- **Ouderzin:** Je kind rekent keer een getal van twee cijfers door het te splitsen in tientallen en eenheden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Tel de uitkomsten van de stukken nog eens op, kolom voor kolom.  [nieuw]
  - `stuk vergeten bij splitsen` (Claudes sleutel: deel-vergeten-bij-splitsen) → Heb je beide stukken keer het grote getal gedaan? Tel daarna beide uitkomsten op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Splits het kleinste getal, doe elk stuk keer het grote getal en tel op.  [nieuw]
- Status: hints klaar
