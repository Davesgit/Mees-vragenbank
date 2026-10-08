# G6-GET-E03 — Breuken meten, vergelijken en plaatsen

Onze omschrijving: Breuken: maatverfijning; vergelijken/ordenen; getallenlijn · in onze bank: 8 items

Claude-vragen gemapt: **806** in **10** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Schrijf #/# zo eenvoudig mogelijk.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Schrijf #/# zo eenvoudig mogelijk.” (koppeling: claudeId)
- Items: **550** · Claude-doelen: B9 (550) · regel: G6-B10-vereenvoudigen
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 18), breuken (noemer tot 20), breuken (noemer tot 21), breuken (noemer tot 22), breuken (noemer tot 24), breuken (noemer tot 25), breuken (noemer tot 26), breuken (noemer tot 27), breuken (noemer tot 28), breuken (noemer tot 30), breuken (noemer tot 32), breuken (noemer tot 33), breuken (noemer tot 34), breuken (noemer tot 35), breuken (noemer tot 36), breuken (noemer tot 38), breuken (noemer tot 39), breuken (noemer tot 40), breuken (noemer tot 45), breuken (noemer tot 49), breuken (noemer tot 51), breuken (noemer tot 55), breuken (noemer tot 57), breuken (noemer tot 6), breuken (noemer tot 63), breuken (noemer tot 65), breuken (noemer tot 69), breuken (noemer tot 75), breuken (noemer tot 77), breuken (noemer tot 8), breuken (noemer tot 81), breuken (noemer tot 85), breuken (noemer tot 87), breuken (noemer tot 9), breuken (noemer tot 91), breuken (noemer tot 93), breuken (noemer tot 95), breuken (noemer tot 99) · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (556), verkeerde-bewerking (260), omgekeerd-gedeeld (257), nog-niet-eenvoudigst (27)
- Verschillende Claude-fout-hints: 4 (meest: “Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-460` (Claude B9, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 4/6 zo eenvoudig mogelijk.
    - **Antwoord:** 2/3  (controle: ok)
    - **Fout-hints (Claude):** 2/6 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 4/3 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G6-GET-E03-claude-bank-627` (Claude B9, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 42/57 zo eenvoudig mogelijk.
    - **Antwoord:** 14/19  (controle: ok)
    - **Fout-hints (Claude):** 14/57 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 39/54 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek een getal waardoor je de teller (boven de streep) en de noemer (onder de streep) allebei precies kunt delen.
- **Hint 2 (te schrijven):** Deel de teller en de noemer door dat getal. Kun je daarna nog eens allebei door hetzelfde getal delen? Ga door tot dat niet meer kan.
- **Ouderzin:** Je kind schrijft een breuk zo eenvoudig mogelijk: de teller en de noemer door hetzelfde getal delen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één van de twee gedeeld` (Claudes sleutel: deel-vergeten-bij-splitsen) → Je hebt maar één van de twee gedeeld. Deel de teller én de noemer door hetzelfde getal, dan blijft de breuk even groot.  [Claude, taalfix]
  - `omgedraaid` (Claudes sleutel: omgekeerd-gedeeld) → Je hebt de breuk omgedraaid. De teller blijft boven de streep en de noemer blijft onder de streep.  [Claude, taalfix]
  - `hetzelfde eraf gehaald` (Claudes sleutel: verkeerde-bewerking) → Je hebt van de teller en de noemer hetzelfde getal afgehaald. Zo blijft de breuk niet even groot. Deel de teller en de noemer door hetzelfde getal.  [Claude, taalfix]
  - `nog niet eenvoudigst (Claude)` (Claudes sleutel: nog-niet-eenvoudigst) → Die breuk is even groot, maar nog niet zo eenvoudig mogelijk. Kun je de teller en de noemer nog eens door hetzelfde getal delen?  [Claude, taalfix]
  - `nog niet eenvoudigst` (fout = gelijkwaardig maar niet zo eenvoudig mogelijk) → Die breuk is even groot, maar nog niet zo eenvoudig mogelijk. Kun je de teller en de noemer nog eens door hetzelfde getal delen?  [nieuw]
  - `andere fout` (andere fout) → Deel de teller en de noemer door hetzelfde getal. Ga door tot er geen getal meer is waardoor je ze allebei kunt delen.  [nieuw]
- Status: hints klaar

## Somtype 2: Schrijf #/# met noemer #.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Schrijf #/# met noemer #.” (koppeling: claudeId)
- Items: **133** · Claude-doelen: B6 (133) · regel: G6-B07-noemer
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 18), breuken (noemer tot 20), breuken (noemer tot 21), breuken (noemer tot 22), breuken (noemer tot 24), breuken (noemer tot 27), breuken (noemer tot 28), breuken (noemer tot 30), breuken (noemer tot 32), breuken (noemer tot 33), breuken (noemer tot 36), breuken (noemer tot 40), breuken (noemer tot 44), breuken (noemer tot 48), breuken (noemer tot 6), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (130), teller-en-noemer-optellen (85), deel-vergeten-bij-splitsen (38), teller-klopt-niet (13)
- Verschillende Claude-fout-hints: 4 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-165` (Claude B6, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 1/2 met noemer 6.
    - **Antwoord:** 3/6  (controle: ok)
    - **Fout-hints (Claude):** 5/6 → De noemer zegt in hoeveel stukken de taart is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 2/6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-GET-E03-claude-bank-170` (Claude B6, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 4/9 met noemer 18.
    - **Antwoord:** 8/18  (controle: ok)
    - **Fout-hints (Claude):** 13/18 → De noemer zegt in hoeveel stukken de taart is verdeeld. Die verandert niet als je stukken bij elkaar doet. · 12/18 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Hoeveel keer zo groot is de nieuwe noemer als de oude noemer (onder de streep)?
- **Hint 2 (te schrijven):** Doe de teller (boven de streep) ook zoveel keer. Dan blijft de breuk even groot.
- **Ouderzin:** Je kind schrijft een breuk met een grotere noemer: de teller en de noemer allebei keer hetzelfde getal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller hetzelfde gelaten` (Claudes sleutel: deel-vergeten-bij-splitsen) → De noemer is groter geworden, maar de teller niet. Hoeveel keer zo groot is de noemer geworden? Doe de teller ook zoveel keer.  [Claude, taalfix]
  - `hetzelfde erbij gedaan` (Claudes sleutel: teller-en-noemer-optellen) → Je hebt bij de teller hetzelfde erbij gedaan als bij de noemer. Zo blijft de breuk niet even groot. Hoeveel keer zo groot is de noemer geworden? Doe de teller ook zoveel keer.  [Claude, taalfix]
  - `verkeerd keer` (Claudes sleutel: eenheid-verkeerd-omgerekend) → De noemer klopt, maar de teller niet. Hoeveel keer zo groot is de noemer geworden? Doe de teller precies zoveel keer.  [Claude, taalfix]
  - `teller klopt niet` (Claudes sleutel: teller-klopt-niet) → De noemer klopt, maar de teller niet. Hoeveel keer zo groot is de noemer geworden? Doe de teller precies zoveel keer.  [Claude, taalfix]
  - `even groot, andere noemer` (fout = even grote breuk met een andere noemer) → Die breuk is even groot, maar hij heeft nog niet de nieuwe noemer uit de vraag. Hoeveel keer zo groot is de nieuwe noemer als de oude noemer? Doe de teller ook zoveel keer.  [nieuw]
  - `andere fout` (andere fout) → Schrijf de breuk met de nieuwe noemer. Hoeveel keer zo groot is die noemer? Doe de teller precies zoveel keer.  [nieuw]
- Status: hints klaar

## Somtype 3: Welke breuk is het grootst? Kies uit #/#, #/# of #/#.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Welke breuk is het grootst? Kies uit #/#, #/# of #/#. — verschillende tellers en noemers” (koppeling: claudeId)
- Items: **38** · Claude-doelen: B5 (38) · regel: G6-B06-vergelijken
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 18), breuken (noemer tot 20), breuken (noemer tot 5), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Denkfouten (Claude): een-andere-breuk (76)
- Verschillende Claude-fout-hints: 1 (meest: “Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-860` (Claude B5, bank, niveau 1 → kritisch)
    - **Opgave:** Welke breuk is het grootst? Kies uit 4/11, 7/9 of 5/6.
    - **Antwoord:** 5/6  (controle: ok)
    - **Fout-hints (Claude):** 4/11 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 7/9 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?
  - `G6-GET-E03-claude-bank-1128` (Claude B5, bank, niveau 2 → toepassen)
    - **Opgave:** Welke breuk is het grootst? Kies uit 3/5, 5/12 of 1/16.
    - **Antwoord:** 3/5  (controle: ok)
    - **Fout-hints (Claude):** 1/16 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 5/12 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?

- **Hint 1 (te schrijven):** Kijk eerst bij elke breuk: is hij meer dan de helft, minder, of precies de helft? Doe de teller (boven de streep) keer twee en vergelijk met de noemer (onder de streep).
- **Hint 2 (te schrijven):** Is maar één breuk meer dan de helft? Dan is die het grootst. Is geen breuk meer dan de helft, maar wel één precies de helft? Dan is die het grootst. Zijn er meer breuken meer dan de helft? Of liggen ze alle drie onder de helft? Vergelijk ze dan twee aan twee. Hebben ze dezelfde noemer, dan is die met de grootste teller het grootst. Hebben ze dezelfde teller, dan is die met de kleinste noemer het grootst. Is de ene noemer een veelvoud van de andere? Doe dan bij de breuk met de kleinste noemer de teller en de noemer allebei keer hetzelfde getal, zodat de noemers gelijk worden. Vergelijk daarna de tellers. Is dat ook niet zo? Zoek dan een getal waar beide noemers precies in passen. Schrijf de twee breuken met dat getal als noemer en vergelijk de tellers.
- **Ouderzin:** Je kind zoekt de grootste van drie breuken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een andere breuk` (Claudes sleutel: een-andere-breuk) → Er is nog een breuk die groter is. Is jouw breuk meer of minder dan de helft? En de andere twee?  [Claude, taalfix]
  - `andere fout` (andere fout) → Typ de grootste van de drie breuken uit de vraag. Kijk eerst bij elke breuk: meer dan de helft, minder, of precies de helft? Is maar één breuk meer dan de helft, dan is die het grootst. Anders vergelijk je de breuken die nog kunnen winnen twee aan twee.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Welke breuk is het grootst? Kies uit #/#, #/# of #/#. — verschillende tellers en noemers'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: Welke breuk is het kleinst? Kies uit #/#, #/# of #/#.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Welke breuk is het kleinst? Kies uit #/#, #/# of #/#. — verschillende tellers en noemers” (koppeling: claudeId)
- Items: **28** · Claude-doelen: B5 (28) · regel: G6-B06-vergelijken
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 11), breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 15), breuken (noemer tot 16), breuken (noemer tot 19), breuken (noemer tot 20), breuken (noemer tot 5), breuken (noemer tot 7), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Denkfouten (Claude): een-andere-breuk (56)
- Verschillende Claude-fout-hints: 1 (meest: “Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-1152` (Claude B5, bank, niveau 1 → basis)
    - **Opgave:** Welke breuk is het kleinst? Kies uit 5/8, 3/8 of 7/8.
    - **Antwoord:** 3/8  (controle: ok)
    - **Fout-hints (Claude):** 5/8 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 7/8 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?
  - `G6-GET-E03-claude-bank-1051` (Claude B5, bank, niveau 2 → toepassen)
    - **Opgave:** Welke breuk is het kleinst? Kies uit 3/4, 2/7 of 3/14.
    - **Antwoord:** 3/14  (controle: ok)
    - **Fout-hints (Claude):** 3/4 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter? · 2/7 → Stel je een taart voor: verdeel je hem in 8 stukken of in 4 stukken, welk stuk is dan groter?

- **Hint 1 (te schrijven):** Kijk eerst bij elke breuk: is hij meer dan de helft, minder, of precies de helft? Doe de teller (boven de streep) keer twee en vergelijk met de noemer (onder de streep).
- **Hint 2 (te schrijven):** Is maar één breuk minder dan de helft? Dan is die het kleinst. Zijn er meer breuken minder dan de helft? Of liggen ze alle drie boven de helft? Vergelijk ze dan twee aan twee. Hebben ze dezelfde noemer, dan is die met de kleinste teller het kleinst. Hebben ze dezelfde teller, dan is die met de grootste noemer het kleinst. Is de ene noemer een veelvoud van de andere? Doe dan bij de breuk met de kleinste noemer de teller en de noemer allebei keer hetzelfde getal, zodat de noemers gelijk worden. Vergelijk daarna de tellers. Is dat ook niet zo? Zoek dan een getal waar beide noemers precies in passen. Schrijf de twee breuken met dat getal als noemer en vergelijk de tellers.
- **Ouderzin:** Je kind zoekt de kleinste van drie breuken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een andere breuk` (Claudes sleutel: een-andere-breuk) → Er is nog een breuk die kleiner is. Is jouw breuk meer of minder dan de helft? En de andere twee?  [Claude, taalfix]
  - `andere fout` (andere fout) → Typ de kleinste van de drie breuken uit de vraag. Kijk eerst bij elke breuk: meer dan de helft, minder, of precies de helft? Is maar één breuk minder dan de helft, dan is die het kleinst. Anders vergelijk je de breuken die nog kunnen winnen twee aan twee.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Welke breuk is het kleinst? Kies uit #/#, #/# of #/#. — verschillende tellers en noemers'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 5: #/# van de [ding]. Schrijf deze breuk zo eenvoudig mogelijk.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “#/# van de [ding]. Schrijf deze breuk zo eenvoudig mogelijk.” (koppeling: claudeId)
- Items: **16** · Claude-doelen: B3 (16) · regel: G6-B05-gelijkwaardig
- Getallenruimte: breuken (noemer tot 12), breuken (noemer tot 15), breuken (noemer tot 20), breuken (noemer tot 4), breuken (noemer tot 6), breuken (noemer tot 9) · type: kale
- Uit de G5-park: 16 items
- Denkfouten (Claude): deel-van-geheel-verkeerd (32)
- Verschillende Claude-fout-hints: 2 (meest: “Als je de noemer deelt, moet je de teller door hetzelfde getal delen.”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-016` (Claude B3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3/15 van de pionnen op het bord is wit. Schrijf die breuk zo eenvoudig mogelijk.
    - **Antwoord:** 1/5  (controle: ok)
    - **Fout-hints (Claude):** 3/5 → Als je de noemer deelt, moet je de teller door hetzelfde getal delen. · 1/15 → Als je de teller deelt, moet je de noemer door hetzelfde getal delen.
    - **Uitleg (Claude):** Deel teller en noemer allebei door 3: 1/5.
  - `G6-GET-E03-claude-bank-010` (Claude B3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3/6 van de sterren op het blad is al gekleurd. Schrijf die breuk zo eenvoudig mogelijk.
    - **Antwoord:** 1/2  (controle: ok)
    - **Fout-hints (Claude):** 3/2 → Als je de noemer deelt, moet je de teller door hetzelfde getal delen. · 1/6 → Als je de teller deelt, moet je de noemer door hetzelfde getal delen.
    - **Uitleg (Claude):** Deel teller en noemer allebei door 3: 1/2.

- **Hint 1 (te schrijven):** Zoek een getal waardoor je de teller (boven de streep) en de noemer (onder de streep) allebei precies kunt delen.
- **Hint 2 (te schrijven):** Deel de teller en de noemer door dat getal. Kun je daarna nog eens allebei door hetzelfde getal delen? Ga door tot dat niet meer kan.
- **Ouderzin:** Je kind schrijft een breuk van een groep dingen zo eenvoudig mogelijk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één van de twee gedeeld` (Claudes sleutel: deel-van-geheel-verkeerd) → Je hebt maar één van de twee gedeeld. Deel de teller én de noemer door hetzelfde getal, dan blijft de breuk even groot.  [Claude, taalfix]
  - `nog niet eenvoudigst` (fout = gelijkwaardig maar niet zo eenvoudig mogelijk) → Die breuk is even groot, maar nog niet zo eenvoudig mogelijk. Kun je de teller en de noemer nog eens door hetzelfde getal delen?  [nieuw]
  - `andere fout` (andere fout) → Deel de teller en de noemer door hetzelfde getal. Ga door tot er geen getal meer is waardoor je ze allebei kunt delen.  [nieuw]
- Status: hints klaar

## Somtype 6: #/# van een [ding] is evenveel als ?/#. Welk getal hoort op het vraagteken?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “#/# van een [ding] is evenveel als ?/#. Welk getal hoort op het vraagteken?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: B3 (16) · regel: G6-B05-gelijkwaardig
- Getallenruimte: breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5) · type: kale
- Uit de G5-park: 16 items
- Denkfouten (Claude): teller-en-noemer-optellen (16), getal-overgenomen (16), een-ernaast (12)
- Verschillende Claude-fout-hints: 3 (meest: “Je hebt bij de teller opgeteld wat er bij de noemer bij kwam. Je moet allebei met hetzelfde getal vermenigvuldigen.”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-036` (Claude B3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 3/4 van een pizza is evenveel als ?/8. Welk getal hoort op het vraagteken?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 7 → Je hebt bij de teller opgeteld wat er bij de noemer bij kwam. Je moet allebei met hetzelfde getal vermenigvuldigen. · 3 → Kijk hoeveel keer zo groot de noemer werd; de teller wordt precies zoveel keer zo groot.
    - **Uitleg (Claude):** Teller en noemer allebei keer 2: 3 × 2 = 6 en 4 × 2 = 8. Dus 3/4 = 6/8.
  - `G6-GET-E03-claude-bank-035` (Claude B3, gegenereerd, niveau 1 → basis)
    - **Opgave:** 2/5 = ?/15. Welk getal hoort op het vraagteken?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 12 → Je hebt bij de teller opgeteld wat er bij de noemer bij kwam. Je moet allebei met hetzelfde getal vermenigvuldigen. · 2 → Kijk hoeveel keer zo groot de noemer werd; de teller wordt precies zoveel keer zo groot. · 7 → Vermenigvuldig de teller met hetzelfde getal als de noemer, en tel niets extra's op.
    - **Uitleg (Claude):** Teller en noemer allebei keer 3: 2 × 3 = 6 en 5 × 3 = 15. Dus 2/5 = 6/15.

- **Hint 1 (te schrijven):** Hoeveel keer zo groot is de nieuwe noemer (onder de streep) als de oude noemer?
- **Hint 2 (te schrijven):** Doe de teller (boven de streep) ook zoveel keer. Dan blijft de breuk even groot.
- **Ouderzin:** Je kind zoekt een gelijkwaardige breuk: de teller en de noemer allebei keer hetzelfde getal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de factor` (fout = de factor (nieuwe noemer : oude noemer)) → Hoeveel keer zo groot is de noemer geworden? Doe de teller (boven de streep) ook zoveel keer. Dat getal komt op het vraagteken.  [nieuw]
  - `teller overgenomen` (fout = getal1) → Dat is de teller van de eerste breuk. De noemer is groter geworden. Hoeveel keer zo groot? Doe de teller ook zoveel keer.  [nieuw]
  - `hetzelfde erbij gedaan` (Claudes sleutel: teller-en-noemer-optellen) → Je hebt bij de teller hetzelfde erbij gedaan als bij de noemer. Zo blijft de breuk niet even groot. Hoeveel keer zo groot is de noemer geworden? Doe de teller ook zoveel keer.  [Claude, taalfix]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Hoeveel keer zo groot is de noemer geworden? Doe de teller precies zoveel keer.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Hoeveel keer zo groot is de noemer geworden? Doe de teller precies zoveel keer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Je hebt een getal uit de vraag overgenomen. Is dat echt het getal dat op het vraagteken hoort? Hoeveel keer zo groot is de nieuwe noemer? Doe de teller ook zoveel keer.  [nieuw]
  - `andere fout` (andere fout) → Hoeveel keer zo groot is de nieuwe noemer als de oude noemer? Doe de teller ook zoveel keer.  [nieuw]
- Status: hints klaar

## Somtype 7: [stip op getallenlijn zetten] Zet #/# op de lijn van # tot #.

- Sleutel: nrOrigineel **7** · somtypeOrigineel “[stip op getallenlijn zetten] Zet #/# op de lijn van # tot #.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: B5 (12) · regel: G6-B06-vergelijken
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G6-GET-E03-claude-bank-1124` (Claude B5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 3/10 op de lijn van 0 tot 1.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 3/10  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Verdeel de lijn in 10 gelijke stukken. 3/10 is 3 van die stukken vanaf 0.
  - `G6-GET-E03-claude-bank-1118` (Claude B5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet 1/8 op de lijn van 0 tot 1.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** 1/8  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Verdeel de lijn in 8 gelijke stukken. 1/8 is 1 van die stukken vanaf 0.

- **Hint 1 (te schrijven):** De streepjes verdelen de lijn van nul tot één in zoveel gelijke stukken als de noemer (onder de streep) zegt.
- **Hint 2 (te schrijven):** De teller (boven de streep) zegt hoeveel van die stukken je vanaf nul verder gaat.
- **Ouderzin:** Je kind zet een breuk op een getallenlijn van nul tot één.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een stuk te ver` (fout = een stuk te ver) → Bijna! Je bent één stuk te ver. Tel vanaf nul de stukken nog eens.  [nieuw]
  - `een stuk te kort` (fout = een stuk te kort) → Bijna! Je bent één stuk te kort. Tel vanaf nul de stukken nog eens.  [nieuw]
  - `andere fout` (andere fout) → De streepjes verdelen de lijn in zoveel gelijke stukken als de noemer zegt. Ga vanaf nul zoveel stukken verder als de teller zegt.  [nieuw]
- Status: hints klaar

## Somtype 8: #/# van de [wie] heeft een [ding]. Schrijf die breuk zo eenvoudig mogelijk.

- Sleutel: nrOrigineel **8** · somtypeOrigineel “#/# van de [wie] heeft een [ding]. Schrijf die breuk zo eenvoudig mogelijk.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B9 (8) · regel: G6-B10-vereenvoudigen
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 6), breuken (noemer tot 8), breuken (noemer tot 9) · type: kale
- Denkfouten (Claude): een-van-de-twee-gedeeld (16), cijfers-verwisseld (8)
- Verschillende Claude-fout-hints: 3 (meest: “Wat je met de teller doet, doe je ook met de noemer. Allebei delen.”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-024` (Claude B9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 2/8 van de kinderen in de groep heeft een zwemdiploma. Schrijf die breuk zo eenvoudig mogelijk.
    - **Antwoord:** 1/4  (controle: ok)
    - **Fout-hints (Claude):** 1/8 → Wat je met de teller doet, doe je ook met de noemer. Allebei delen. · 2/4 → Deel de teller ook door hetzelfde getal. · 4/1 → Teller boven, noemer onder. Draai ze niet om.
    - **Uitleg (Claude):** Zoek een getal waar teller en noemer allebei door deelbaar zijn: 2. 2 : 2 = 1, 8 : 2 = 4. Dus 1/4.
  - `G6-GET-E03-claude-bank-018` (Claude B9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3/6 van de kinderen in de groep heeft een zwemdiploma. Schrijf die breuk zo eenvoudig mogelijk.
    - **Antwoord:** 1/2  (controle: ok)
    - **Fout-hints (Claude):** 1/6 → Wat je met de teller doet, doe je ook met de noemer. Allebei delen. · 3/2 → Deel de teller ook door hetzelfde getal. · 2/1 → Teller boven, noemer onder. Draai ze niet om.
    - **Uitleg (Claude):** Zoek een getal waar teller en noemer allebei door deelbaar zijn: 3. 3 : 3 = 1, 6 : 3 = 2. Dus 1/2.

- **Hint 1 (te schrijven):** Zoek een getal waardoor je de teller (boven de streep) en de noemer (onder de streep) allebei precies kunt delen.
- **Hint 2 (te schrijven):** Deel de teller en de noemer door dat getal. Kun je daarna nog eens allebei door hetzelfde getal delen? Ga door tot dat niet meer kan.
- **Ouderzin:** Je kind schrijft een breuk van een groep zo eenvoudig mogelijk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één van de twee gedeeld` (Claudes sleutel: een-van-de-twee-gedeeld) → Je hebt maar één van de twee gedeeld. Deel de teller én de noemer door hetzelfde getal, dan blijft de breuk even groot.  [Claude, taalfix]
  - `omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de breuk omgedraaid. De teller blijft boven de streep en de noemer blijft onder de streep.  [Claude, taalfix]
  - `nog niet eenvoudigst` (fout = gelijkwaardig maar niet zo eenvoudig mogelijk) → Die breuk is even groot, maar nog niet zo eenvoudig mogelijk. Kun je de teller en de noemer nog eens door hetzelfde getal delen?  [nieuw]
  - `andere fout` (andere fout) → Deel de teller en de noemer door hetzelfde getal. Ga door tot er geen getal meer is waardoor je ze allebei kunt delen.  [nieuw]
- Status: hints klaar

## Somtype 9: [kaartjes op volgorde slepen] Welke breuken zijn hetzelfde als #/#? Sleep ze naar het goede vak.

- Sleutel: nrOrigineel **9** · somtypeOrigineel “[kaartjes op volgorde slepen] Welke breuken zijn hetzelfde als #/#? Sleep ze naar het goede vak.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B3 (4) · regel: G6-B05-gelijkwaardig
- Getallenruimte: breuken (noemer tot 12), breuken (noemer tot 16), breuken (noemer tot 8) · type: ordenen
- Uit de G5-park: 4 items
- G6-fix: 'wel'-breuk uit de 'niet'-lijst, vervangen door een breuk met dezelfde noemer die niet gelijk is (1108) · 'wel'-breuk uit de 'niet'-lijst, vervangen door een breuk met dezelfde noemer die niet gelijk is (1110) · 'wel'-breuk uit de 'niet'-lijst, vervangen door een breuk met dezelfde noemer die niet gelijk is (1111)
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G6-GET-E03-claude-bank-1111` (Claude B3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welke breuken zijn hetzelfde als 1/3? Sleep ze naar het goede vak.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** wel:2/6,3/9,4/12|niet:1/4,3/6,4/9  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Een breuk blijft hetzelfde als je teller en noemer met hetzelfde getal vermenigvuldigt: 1/3 = 2/6.
  - `G6-GET-E03-claude-bank-1108` (Claude B3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welke breuken zijn hetzelfde als 1/4? Sleep ze naar het goede vak.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** wel:2/8,3/12,4/16|niet:1/5,3/8,4/12  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Een breuk blijft hetzelfde als je teller en noemer met hetzelfde getal vermenigvuldigt: 1/4 = 2/8.

- **Hint 1 (te schrijven):** Een breuk blijft even groot als je de teller (boven de streep) en de noemer (onder de streep) allebei keer hetzelfde getal doet.
- **Hint 2 (te schrijven):** Kijk bij elke breuk: hoeveel keer zo groot is de noemer geworden? Is de teller ook precies zoveel keer zo groot? Dan hoort hij bij hetzelfde.
- **Ouderzin:** Je kind sorteert breuken: even groot als de breuk in de vraag, of niet.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één breuk in het verkeerde vak` (fout = één getal in het verkeerde vak) → Eén breuk staat in het verkeerde vak. Kijk bij elke breuk: zijn de teller en de noemer allebei keer hetzelfde getal gedaan? Dan is hij even groot.  [nieuw]
  - `vakken omgewisseld` (fout = vakken omgewisseld) → Je hebt de vakken omgewisseld. Bij hetzelfde horen de breuken die even groot zijn.  [nieuw]
  - `andere fout` (andere fout) → Kijk bij elke breuk of de teller en de noemer allebei keer hetzelfde getal zijn gedaan. Dan is hij even groot en hoort hij bij hetzelfde. Anders niet.  [nieuw]
- Status: hints klaar

## Somtype 10: [kaartjes op volgorde slepen] Zet de breuken op volgorde van klein naar groot.

- Sleutel: nrOrigineel **10** · somtypeOrigineel “[kaartjes op volgorde slepen] Zet de breuken op volgorde van klein naar groot.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B5 (1) · regel: G6-B06-vergelijken
- Getallenruimte: 0–100 · type: ordenen
- Denkfouten (Claude): grotere-noemer-is-groter (1)
- Verschillende Claude-fout-hints: 1 (meest: “Een grotere noemer betekent kleinere stukken.”)
- Voorbeelden:
  - `G6-GET-E03-claude-bank-1112` (Claude B5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de breuken op volgorde van klein naar groot.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** 3/8|3/5|3/4  (controle: ok)
    - **Fout-hints (Claude):** 3/4|3/5|3/8 → Een grotere noemer betekent kleinere stukken.
    - **Uitleg (Claude):** Van klein naar groot: 3/8, 3/5, 3/4.

- **Hint 1 (te schrijven):** Hebben de breuken dezelfde teller (boven de streep)? Dan kijk je naar de noemer (onder de streep): hoe groter de noemer, hoe kleiner de stukken.
- **Hint 2 (te schrijven):** Zet de kleinste breuk vooraan en de grootste achteraan.
- **Ouderzin:** Je kind zet breuken op volgorde van klein naar groot.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omgedraaid` (volgorde omgedraaid) → Je hebt ze van groot naar klein gezet. Begin met de kleinste breuk.  [nieuw]
  - `andere fout` (andere fout) → Vergelijk de breuken twee aan twee. Hebben ze dezelfde teller? Dan is de breuk met de grootste noemer het kleinst.  [nieuw]
- Status: hints klaar
