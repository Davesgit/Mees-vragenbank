# G7-GET-05 — Breuken en de rekenmachine

Onze omschrijving: Breuken + rekenmachine · in onze bank: 8 items

Claude-vragen gemapt: **567** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Welke breuk is het grootst? Kies uit #/#, #/# of #/#.

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Welke breuk is het grootst? Kies uit #/#, #/# of #/#.” (koppeling: claudeId)
- Items: **190** · Claude-doelen: B5 (190) · regel: G7-B06-vergelijken-gelijknamig
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 18), breuken (noemer tot 20), breuken (noemer tot 21), breuken (noemer tot 22), breuken (noemer tot 24), breuken (noemer tot 8) · type: kale
- Uit de G6-park: 190 items
- Denkfouten (Claude): grotere-noemer-is-groter (296), alleen-noemer-vergeleken (84)
- Verschillende Claude-fout-hints: 1 (meest: “Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-406` (Claude B5, bank, niveau 1 → basis)
    - **Opgave:** Welke breuk is het grootst? Kies uit 1/11, 3/10 of 1/3.
    - **Antwoord:** 1/3  (controle: ok)
    - **Fout-hints (Claude):** 1/11 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 3/10 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?
  - `G7-GET-05-claude-bank-444` (Claude B5, bank, niveau 3 → toepassen)
    - **Opgave:** Welke breuk is het grootst? Kies uit 3/4, 7/20 of 9/14.
    - **Antwoord:** 3/4  (controle: ok)
    - **Fout-hints (Claude):** 7/20 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 9/14 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?

- **Hint 1 (te schrijven):** Hoe groot is elke breuk ongeveer: minder dan een half, ongeveer een half, of bijna één heel?
- **Hint 2 (te schrijven):** Vergelijk elke breuk met een half en met één heel. Twijfel je nog? Maak de noemers gelijk, of schrijf de breuken als kommagetal.
- **Ouderzin:** Je kind zoekt de grootste van drie breuken met verschillende noemers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet de grootste` (Claudes sleutel: grotere-noemer-is-groter) → Is dat echt de grootste breuk? Een grote noemer zegt nog niet dat de breuk groot is: kijk ook naar de teller. Vergelijk de breuken met een half, of maak de noemers gelijk.  [Claude, taalfix]
  - `kleine noemer gekozen` (Claudes sleutel: alleen-noemer-vergeleken) → Is dat echt de grootste breuk? Een kleine noemer zegt nog niet dat de breuk groot is: kijk ook naar de teller. Vergelijk de breuken met een half, of maak de noemers gelijk.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk de breuken met een half en met één heel, en kies de grootste.  [nieuw]
- Status: hints klaar

## Somtype 2: Welke breuk is het kleinst? Kies uit #/#, #/# of #/#.

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Welke breuk is het kleinst? Kies uit #/#, #/# of #/#.” (koppeling: claudeId)
- Items: **128** · Claude-doelen: B5 (128) · regel: G7-B06-vergelijken-gelijknamig
- Getallenruimte: breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 18), breuken (noemer tot 20), breuken (noemer tot 21), breuken (noemer tot 22), breuken (noemer tot 24), breuken (noemer tot 9) · type: kale
- Uit de G6-park: 128 items
- Denkfouten (Claude): grotere-noemer-is-groter (200), alleen-noemer-vergeleken (56)
- Verschillende Claude-fout-hints: 1 (meest: “Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-513` (Claude B5, bank, niveau 1 → basis)
    - **Opgave:** Welke breuk is het kleinst? Kies uit 3/11, 2/7 of 3/4.
    - **Antwoord:** 3/11  (controle: ok)
    - **Fout-hints (Claude):** 3/4 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 2/7 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?
  - `G7-GET-05-claude-bank-549` (Claude B5, bank, niveau 3 → toepassen)
    - **Opgave:** Welke breuk is het kleinst? Kies uit 7/11, 7/14 of 7/16.
    - **Antwoord:** 7/16  (controle: ok)
    - **Fout-hints (Claude):** 8/9 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 2/11 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?

- **Hint 1 (te schrijven):** Hoe groot is elke breuk ongeveer: minder dan een half, ongeveer een half, of bijna één heel?
- **Hint 2 (te schrijven):** Vergelijk elke breuk met een half en met één heel. Twijfel je nog? Maak de noemers gelijk, of schrijf de breuken als kommagetal.
- **Ouderzin:** Je kind zoekt de kleinste van drie breuken met verschillende noemers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet de kleinste` (Claudes sleutel: grotere-noemer-is-groter) → Is dat echt de kleinste breuk? Een kleine noemer zegt nog niet dat de breuk klein is: kijk ook naar de teller. Vergelijk de breuken met een half, of maak de noemers gelijk.  [Claude, taalfix]
  - `grote noemer gekozen` (Claudes sleutel: alleen-noemer-vergeleken) → Is dat echt de kleinste breuk? Een grote noemer zegt nog niet dat de breuk klein is: kijk ook naar de teller. Vergelijk de breuken met een half, of maak de noemers gelijk.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk de breuken met een half en met één heel, en kies de kleinste.  [nieuw]
- Status: hints klaar

## Somtype 3: Reken uit: #/# + #/# = ? Typ een breuk. — uitkomst boven 1

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Reken uit: #/# + #/# = ? Typ een breuk. — uitkomst boven 1” (koppeling: claudeId)
- Items: **76** · Claude-doelen: B7 (76) · regel: G7-B01-breuk-plusmin
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 7), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Uit de G6-park: 76 items
- Denkfouten (Claude): teller-en-noemer-optellen (152)
- Verschillende Claude-fout-hints: 47 (meest: “De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet.”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-132` (Claude B7, bank, niveau 3 → toepassen)
    - **Opgave:** Reken uit: 2/5 + 4/5 = ? Typ een breuk.
    - **Antwoord:** 6/5  (controle: ok)
    - **Fout-hints (Claude):** 6/10 → De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 5/5 → Tel de stukjes nog eens: 2 + 4 = ?
  - `G7-GET-05-claude-bank-126` (Claude B7, bank, niveau 3 → toepassen)
    - **Opgave:** Reken uit: 5/10 + 8/10 = ? Typ een breuk.
    - **Antwoord:** 13/10  (controle: ok)
    - **Fout-hints (Claude):** 13/20 → De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 12/10 → Tel de stukjes nog eens: 5 + 8 = ?

- **Hint 1 (te schrijven):** De noemers zijn gelijk. Wat doe je met de tellers?
- **Hint 2 (te schrijven):** Tel alleen de tellers bij elkaar op. De noemer blijft hetzelfde. Is de teller groter dan de noemer? Dan is de uitkomst meer dan één heel: typ hem gewoon als breuk.
- **Ouderzin:** Je kind telt breuken met dezelfde noemer op, ook als de uitkomst meer dan één heel is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller of noemer anders` (Claudes sleutel: teller-en-noemer-optellen) → Is de noemer hetzelfde gebleven? Je telt alleen de tellers op. Reken die optelling nog eens na.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de tellers op en laat de noemer hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 4: Reken uit: #/# + #/# = ? Typ een breuk.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Reken uit: #/# + #/# = ? Typ een breuk.” (koppeling: claudeId)
- Items: **63** · Claude-doelen: B7 (63) · regel: G7-B01-breuk-plusmin
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 7), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Uit de G6-park: 63 items
- Oefening in wisselen (omgedraaide som, duplicaatVan = origineel): 17 items
- Denkfouten (Claude): teller-en-noemer-optellen (102), verkeerde-bewerking (24)
- Verschillende Claude-fout-hints: 35 (meest: “De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet.”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-085` (Claude B7, bank, niveau 1 → basis)
    - **Opgave:** Reken uit: 2/5 + 2/5 = ? Typ een breuk.
    - **Antwoord:** 4/5  (controle: ok)
    - **Fout-hints (Claude):** 4/10 → De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 5/5 → Tel de stukjes nog eens: 2 + 2 = ?
  - `G7-GET-05-claude-bank-081` (Claude B7, bank, niveau 2 → toepassen)
    - **Opgave:** Reken uit: 5/7 + 1/7 = ? Typ een breuk.
    - **Antwoord:** 6/7  (controle: ok)
    - **Fout-hints (Claude):** 7/7 → Tel de stukjes nog eens: 5 + 1 = ? · 4/7 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** De noemers zijn gelijk. Wat doe je met de tellers?
- **Hint 2 (te schrijven):** Tel alleen de tellers bij elkaar op. De noemer blijft hetzelfde.
- **Ouderzin:** Je kind telt breuken met dezelfde noemer op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller of noemer anders` (Claudes sleutel: teller-en-noemer-optellen) → Is de noemer hetzelfde gebleven? Je telt alleen de tellers op. Reken die optelling nog eens na.  [Claude, taalfix]
  - `min in plaats van plus` (Claudes sleutel: verkeerde-bewerking) → Is het een plussom of een minsom? Kijk naar het teken.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de tellers op en laat de noemer hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 5: Reken uit: #/# − #/# = ? Typ een breuk.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Reken uit: #/# − #/# = ? Typ een breuk.” (koppeling: claudeId)
- Items: **60** · Claude-doelen: B8 (60) · regel: G7-B01-breuk-plusmin
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 7), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Uit de G6-park: 60 items
- Denkfouten (Claude): teller-en-noemer-optellen (80), verkeerde-bewerking (40)
- Verschillende Claude-fout-hints: 24 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-172` (Claude B8, bank, niveau 3 → toepassen)
    - **Opgave:** Reken uit: 3/4 − 2/4 = ? Typ een breuk.
    - **Antwoord:** 1/4  (controle: ok)
    - **Fout-hints (Claude):** 1/8 → De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 5/4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-GET-05-claude-bank-226` (Claude B8, bank, niveau 3 → toepassen)
    - **Opgave:** Reken uit: 8/9 − 3/9 = ? Typ een breuk.
    - **Antwoord:** 5/9  (controle: ok)
    - **Fout-hints (Claude):** 5/18 → De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 11/9 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** De noemers zijn gelijk. Wat doe je met de tellers?
- **Hint 2 (te schrijven):** Haal de kleinere teller van de grotere af. De noemer blijft hetzelfde.
- **Ouderzin:** Je kind trekt breuken met dezelfde noemer van elkaar af.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller of noemer anders` (Claudes sleutel: teller-en-noemer-optellen) → Is de noemer hetzelfde gebleven? Je haalt alleen de tellers van elkaar af. Reken dat nog eens na.  [Claude, taalfix]
  - `plus in plaats van min` (Claudes sleutel: verkeerde-bewerking) → Is het een plussom of een minsom? Kijk naar het teken.  [Claude, taalfix]
  - `andere fout` (andere fout) → Haal de tellers van elkaar af en laat de noemer hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 6: Schrijf #/# als kommagetal.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Schrijf #/# als kommagetal.” (koppeling: claudeId)
- Items: **45** · Claude-doelen: B13 (45) · regel: G7-B02-breuk-komma
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 2), breuken (noemer tot 20), breuken (noemer tot 25), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Zelfde opgave als onze G7-bank: 1 items
- Denkfouten (Claude): komma-verschoven (46), getal-overgenomen (27), teller-en-noemer-optellen (17)
- Verschillende Claude-fout-hints: 2 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-292` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 1/2 als kommagetal.
    - **Antwoord:** 0,5  (controle: ok)
    - **Fout-hints (Claude):** 0,05 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G7-GET-05-claude-bank-300` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 13/20 als kommagetal.
    - **Antwoord:** 0,65  (controle: ok)
    - **Fout-hints (Claude):** 6,5 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 0,065 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Een breuk is een deling: de teller gedeeld door de noemer.
- **Hint 2 (te schrijven):** Maak een even grote breuk met als noemer tien, honderd of duizend: doe de teller en de noemer keer hetzelfde getal. Tel de nullen van die noemer: zoveel cijfers komen er achter de komma. Heeft de teller minder cijfers? Zet er dan nullen voor. Nullen aan het eind achter de komma vallen weg.
- **Ouderzin:** Je kind schrijft een breuk als kommagetal, via een noemer van tien, honderd of duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Maak eerst een breuk met noemer tien, honderd of duizend. Tel de nullen: zoveel cijfers komen er achter de komma.  [Claude, taalfix]
  - `teller en noemer achter de komma` (Claudes sleutel: teller-en-noemer-optellen) → Heb je de teller en de noemer achter de komma gezet? Een breuk is een deling: teller gedeeld door noemer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel de teller door de noemer, of maak een noemer van tien, honderd of duizend.  [nieuw]
- Status: hints klaar

## Somtype 7: # van de [ding] is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# van de [ding] is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk.” (koppeling: claudeId)
- Items: **5** · Claude-doelen: B13 (5) · regel: G7-B02-breuk-komma
- Getallenruimte: kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (5), cijfers-verwisseld (5)
- Verschillende Claude-fout-hints: 2 (meest: “De cijfers achter de komma zijn tienden of honderdsten. Zet ze boven 10 of 100 en vereenvoudig.”)
- Voorbeelden:
  - `G7-GET-05-claude-bank-001` (Claude B13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 0,6 van de kralen is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk.
    - **Antwoord:** 3/5  (controle: ok)
    - **Fout-hints (Claude):** 6/5 → De cijfers achter de komma zijn tienden of honderdsten. Zet ze boven 10 of 100 en vereenvoudig. · 5/3 → Teller boven, noemer onder.
    - **Uitleg (Claude):** 0,60 is 600/1000. Vereenvoudigen geeft 3/5.
  - `G7-GET-05-claude-bank-004` (Claude B13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 0,5 van de ballonnen is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk.
    - **Antwoord:** 1/2  (controle: ok)
    - **Fout-hints (Claude):** 5/2 → De cijfers achter de komma zijn tienden of honderdsten. Zet ze boven 10 of 100 en vereenvoudig. · 2/1 → Teller boven, noemer onder.
    - **Uitleg (Claude):** 0,50 is 500/1000. Vereenvoudigen geeft 1/2.

- **Hint 1 (te schrijven):** Hoeveel cijfers staan er achter de komma? Staat er één cijfer achter de komma, dan zijn het tienden; bij twee cijfers honderdsten.
- **Hint 2 (te schrijven):** Schrijf het kommagetal als breuk met noemer tien of honderd. Deel daarna de teller en de noemer door hetzelfde getal, tot het niet verder kan.
- **Ouderzin:** Je kind schrijft een kommagetal als een zo eenvoudig mogelijke breuk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller en noemer omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Staan teller en noemer op de goede plek? Het deel staat boven de streep, het geheel eronder.  [Claude, taalfix]
  - `andere breuk` (Claudes sleutel: kommagetal-als-geheel) → Klopt die breuk met het kommagetal? Schrijf het kommagetal eerst als tienden of honderdsten.  [Claude, taalfix]
  - `andere fout` (andere fout) → Schrijf het kommagetal als tienden of honderdsten en maak de breuk zo eenvoudig mogelijk.  [nieuw]
- Status: hints klaar
