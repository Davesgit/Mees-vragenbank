# G8-GET-E04 — Plus, min, keer en delen met breuken

Onze omschrijving: Breuken: ongelijknamig +/−; × breuk×breuk; ÷ heel÷breuk & breuk÷breuk · in onze bank: 8 items

Claude-vragen gemapt: **45** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # [ding] worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# [ding] worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **14** · Claude-doelen: B15 (14) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (14), optellen-ipv-vermenigvuldigen (14)
- Verschillende Claude-fout-hints: 2 (meest: “Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele?”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-017` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 pannenkoeken worden in stukken van 1/8 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 32  (controle: ok)
    - **Fout-hints (Claude):** 4 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 12 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/8 in 4? In één hele passen 8 stukken, dus 4 × 8 = 32.
  - `G8-GET-E04-claude-bank-004` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 3 pannenkoeken worden in stukken van 1/4 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 3 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 7 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/4 in 3? In één hele passen 4 stukken, dus 3 × 4 = 12.

- **Hint 1 (te schrijven):** Je zoekt hoeveel stukken er in totaal zijn. Kijk eerst naar één hele: hoeveel stukken van deze grootte passen erin?
- **Hint 2 (te schrijven):** In één hele passen zoveel stukken als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal hele.
- **Ouderzin:** Je kind deelt hele dingen in gelijke stukken (delen door een breuk): in één hele passen zoveel stukken als de noemer zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hele overgenomen` (fout = getal1) → Dat is het aantal hele waar je mee begint. Elke hele wordt in stukken verdeeld, dus je krijgt meer stukken.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? Elke hele geeft zoveel stukken als de noemer (het getal onder de streep) zegt: reken keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst hoeveel stukken er in één hele passen, en reken dan keer het aantal hele.  [nieuw]
- Status: hints klaar

## Somtype 2: # liter limonade wordt in [bakken] van #/# liter geschonken. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# liter limonade wordt in [bakken] van #/# liter geschonken. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: B15 (6) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (12)
- Verschillende Claude-fout-hints: 12 (meest: “Elke liter geeft 3 bekers. Dus meer dan 2.”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-028` (Claude B15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 2 liter limonade wordt in bekers van 1/3 liter geschonken. Hoeveel bekers zijn dat?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 2 → Elke liter geeft 3 bekers. Dus meer dan 2. · 3 → 3 bekers uit één liter. Er zijn 2 liter.
    - **Uitleg (Claude):** In 1 liter passen 3 bekers van 1/3. In 2 liter dus 2 × 3 = 6 bekers.
  - `G8-GET-E04-claude-bank-030` (Claude B15, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** 2 liter limonade wordt in bekers van 1/4 liter geschonken. Hoeveel bekers zijn dat?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 2 → Elke liter geeft 4 bekers. Dus meer dan 2. · 4 → 4 bekers uit één liter. Er zijn 2 liter.
    - **Uitleg (Claude):** In 1 liter passen 4 bekers van 1/4. In 2 liter dus 2 × 4 = 8 bekers.

- **Hint 1 (te schrijven):** Je zoekt hoe vaak je kunt schenken. Kijk eerst naar één liter: hoe vaak kun je daaruit schenken?
- **Hint 2 (te schrijven):** Uit één liter schenk je zo vaak als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal liters.
- **Ouderzin:** Je kind deelt liters in gelijke porties (delen door een breuk): uit één liter schenk je zo vaak als de noemer zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `liters overgenomen` (fout = getal1) → Dat is het aantal liters. Uit elke liter schenk je meer dan één keer.  [nieuw]
  - `één liter` (Claudes sleutel: omgekeerd-gedeeld) → Zo vaak schenk je uit één liter. Er zijn meer liters: reken keer het aantal liters.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst hoe vaak je uit één liter schenkt, en reken dan keer het aantal liters.  [nieuw]
- Status: hints klaar

## Somtype 3: Er is nog #/# [ding]. [wie] eet daar #/# deel van. Welk deel van de hele taart is dat? Typ een breuk.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Er is nog #/# [ding]. [wie] eet daar #/# deel van. Welk deel van de hele taart is dat? Typ een breuk.” (koppeling: claudeId)
- Items: **6** · Claude-doelen: B14 (6) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (10), teller-en-noemer-optellen (6)
- Verschillende Claude-fout-hints: 3 (meest: “Een deel ván een deel is vermenigvuldigen, niet optellen.”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-039` (Claude B14, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Er is nog 1/5 taart. Een kind eet daar 1/2 deel van. Welk deel van de hele taart is dat? Typ een breuk.
    - **Antwoord:** 1/10  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2/5 → Een deel ván een deel is vermenigvuldigen, niet optellen. · 1/3 → Vermenigvuldig ook de noemers met elkaar.
    - **Uitleg (Claude):** Deel van een deel: vermenigvuldig tellers en noemers. 1 × 1 = 1, 2 × 5 = 10. Dus 1/10.
  - `G8-GET-E04-claude-bank-041` (Claude B14, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Er is nog 2/3 taart. Een kind eet daar 1/2 deel van. Welk deel van de hele taart is dat? Typ een breuk.
    - **Antwoord:** 1/3  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3/5 → Een deel ván een deel is vermenigvuldigen, niet optellen. · 1/6 → Vermenigvuldig ook de tellers met elkaar. · 2/3 → Vermenigvuldig ook de noemers met elkaar.
    - **Uitleg (Claude):** Deel van een deel: vermenigvuldig tellers en noemers. 1 × 2 = 2, 2 × 3 = 6. Dus 2/6 = 1/3.

- **Hint 1 (te schrijven):** Je neemt een deel ván wat er nog is. Een deel van een deel reken je uit met keer.
- **Hint 2 (te schrijven):** Doe teller keer teller en noemer keer noemer (de teller is het getal boven de streep, de noemer het getal onder de streep). Kan de breuk eenvoudiger? Dat mag, maar het hoeft niet.
- **Ouderzin:** Je kind rekent een deel van een deel uit (breuk keer breuk).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Claudes sleutel: teller-en-noemer-optellen) → Heb je de tellers (boven de streep) opgeteld en de noemers (onder de streep) ook? Een deel ván een deel is keer, niet plus.  [Claude, taalfix]
  - `niet van de hele taart` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is nog niet het deel van de hele taart. Neem het deel ván wat er nog is: doe teller keer teller (boven de streep) en noemer keer noemer (onder de streep).  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de twee breuken keer elkaar: teller keer teller (boven de streep) en noemer keer noemer (onder de streep).  [nieuw]
- Status: hints klaar

## Somtype 4: # [ding] wordt in stukken van #/# [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] wordt in stukken van #/# [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: B15 (5) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (5), optellen-ipv-vermenigvuldigen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele?”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-020` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 1 pizza wordt in stukken van 1/8 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 1 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 9 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/8 in 1? In één hele passen 8 stukken, dus 1 × 8 = 8.
  - `G8-GET-E04-claude-bank-023` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 1 pannenkoek wordt in stukken van 1/4 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 1 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 5 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/4 in 1? In één hele passen 4 stukken, dus 1 × 4 = 4.

- **Hint 1 (te schrijven):** Je zoekt hoeveel stukken er in totaal zijn. Kijk eerst naar één hele: hoeveel stukken van deze grootte passen erin?
- **Hint 2 (te schrijven):** In één hele passen zoveel stukken als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal hele.
- **Ouderzin:** Je kind deelt hele dingen in gelijke stukken (delen door een breuk): in één hele passen zoveel stukken als de noemer zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hele overgenomen` (fout = getal1) → Dat is het aantal hele waar je mee begint. Elke hele wordt in stukken verdeeld, dus je krijgt meer stukken.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? Elke hele geeft zoveel stukken als de noemer (het getal onder de streep) zegt: reken keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst hoeveel stukken er in één hele passen, en reken dan keer het aantal hele.  [nieuw]
- Status: hints klaar

## Somtype 5: #/# [ding] wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “#/# [ding] wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B15 (4) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 4), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): getal-overgenomen (4), een-ernaast (4)
- Verschillende Claude-fout-hints: 6 (meest: “Schrijf 1/2 eerst als ?/4.”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-036` (Claude B15, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 1/2 stokbrood wordt verdeeld in stukken van 1/4. Hoeveel stukken zijn dat?
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 1 → Schrijf 1/2 eerst als ?/4. · 3 → 1/2 is precies 2/4.
    - **Uitleg (Claude):** 1/2 = 2/4, dus er passen 2 stukken van 1/4 in.
  - `G8-GET-E04-claude-bank-037` (Claude B15, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3/6 pizza wordt verdeeld in stukken van 1/2. Hoeveel stukken zijn dat?
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 3 → Schrijf 3/6 eerst als ?/2. · 2 → 3/6 is precies 1/2.
    - **Uitleg (Claude):** 3/6 = 1/2, dus er passen 1 stuk van 1/2 in.

- **Hint 1 (te schrijven):** Je zoekt hoe vaak het kleine stuk in het deel past.
- **Hint 2 (te schrijven):** Maak de twee breuken gelijknamig: geef ze dezelfde noemer (het getal onder de streep). Hoe vaak past de teller (het getal boven de streep) van het kleine stuk in de teller van het deel?
- **Ouderzin:** Je kind deelt een breuk in kleinere stukken (breuk gedeeld door breuk): met dezelfde noemer kun je de tellers vergelijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Dat is één stuk te veel. Tel nog eens hoe vaak het kleine stuk in het deel past.  [nieuw]
  - `noemer van het kleine stuk` (Claudes sleutel: een-ernaast) → Zoveel kleine stukken passen er in een hele. Je verdeelt geen hele, alleen een deel ervan: hoe vaak past het kleine stuk dáárin?  [Claude, taalfix]
  - `teller overgenomen` (Claudes sleutel: getal-overgenomen) → Dat is de teller van het deel (het getal boven de streep). Je zoekt hoe vaak het kleine stuk in het deel past.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk hoe vaak het kleine stuk in het deel past.  [nieuw]
- Status: hints klaar

## Somtype 6: [wie] eet #/# van een pizza, een ander kind #/#. Welk deel is samen op? Typ een breuk.

- Sleutel: nrOrigineel **6** · somtypeOrigineel “[wie] eet #/# van een pizza, een ander kind #/#. Welk deel is samen op? Typ een breuk.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B6 (4) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 12), breuken (noemer tot 14), breuken (noemer tot 24), breuken (noemer tot 6) · type: kale
- Denkfouten (Claude): teller-en-noemer-optellen (8), deel-vergeten-bij-splitsen (4)
- Verschillende Claude-fout-hints: 9 (meest: “Je kunt alleen optellen als de stukken even groot zijn. Maak eerst de noemers gelijk.”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-045` (Claude B6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kind eet 1/3 van een pizza, een ander kind 1/4. Welk deel is samen op? Typ een breuk.
    - **Antwoord:** 7/12  (controle: ok)
    - **Fout-hints (Claude):** 2/7 → Je kunt alleen optellen als de stukken even groot zijn. Maak eerst de noemers gelijk. · 7/144 → De noemer blijft 12 als je 4/12 en 3/12 optelt. · 2/12 → Na het gelijknamig maken zijn de tellers niet meer 1. 1/3 is 4/12.
    - **Uitleg (Claude):** Maak de noemers gelijk: 12 past bij allebei. 1/3 = 4/12 en 1/4 = 3/12. Samen 7/12.
  - `G8-GET-E04-claude-bank-047` (Claude B6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kind eet 1/3 van een pizza, een ander kind 1/8. Welk deel is samen op? Typ een breuk.
    - **Antwoord:** 11/24  (controle: ok)
    - **Fout-hints (Claude):** 2/11 → Je kunt alleen optellen als de stukken even groot zijn. Maak eerst de noemers gelijk. · 11/576 → De noemer blijft 24 als je 8/24 en 3/24 optelt. · 2/24 → Na het gelijknamig maken zijn de tellers niet meer 1. 1/3 is 8/24.
    - **Uitleg (Claude):** Maak de noemers gelijk: 24 past bij allebei. 1/3 = 8/24 en 1/8 = 3/24. Samen 11/24.

- **Hint 1 (te schrijven):** Breuken kun je pas optellen als ze dezelfde noemer hebben (het getal onder de streep).
- **Hint 2 (te schrijven):** Maak de breuken gelijknamig: geef ze dezelfde noemer (het getal onder de streep), en verander de tellers (de getallen boven de streep) mee. Tel daarna alleen de tellers op.
- **Ouderzin:** Je kind telt twee breuken op: eerst gelijknamig maken (dezelfde noemer geven), dan de tellers optellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alles opgeteld` (Claudes sleutel: teller-en-noemer-optellen) → Maak eerst de noemers (onder de streep) gelijk. Tel dan alleen de tellers (boven de streep) op: de noemer blijft hetzelfde.  [Claude, taalfix]
  - `tellers niet mee` (Claudes sleutel: deel-vergeten-bij-splitsen) → De noemer (onder de streep) klopt, maar de tellers (boven de streep) moeten mee veranderen als je de noemers gelijk maakt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak de breuken eerst gelijknamig (geef ze dezelfde noemer: het getal onder de streep), en tel dan de tellers (boven de streep) op.  [nieuw]
- Status: hints klaar

## Somtype 7: # [ding] chocola worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “# [ding] chocola worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: B15 (3) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (3), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 2 (meest: “Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele?”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-003` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 4 repen chocola worden in stukken van 1/6 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 4 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 10 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/6 in 4? In één hele passen 6 stukken, dus 4 × 6 = 24.
  - `G8-GET-E04-claude-bank-002` (Claude B15, gegenereerd, niveau 1 → basis)
    - **Opgave:** 2 repen chocola worden in stukken van 1/8 verdeeld. Hoeveel stukken zijn dat?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 2 → Delen door een breuk maakt groter: hoeveel van die stukken passen er in één hele? · 10 → Elke hele geeft evenveel stukken als de noemer zegt: dat is keer, niet plus.
    - **Uitleg (Claude):** Hoe vaak past 1/8 in 2? In één hele passen 8 stukken, dus 2 × 8 = 16.

- **Hint 1 (te schrijven):** Je zoekt hoeveel stukken er in totaal zijn. Kijk eerst naar één hele: hoeveel stukken van deze grootte passen erin?
- **Hint 2 (te schrijven):** In één hele passen zoveel stukken als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal hele.
- **Ouderzin:** Je kind deelt hele dingen in gelijke stukken (delen door een breuk): in één hele passen zoveel stukken als de noemer zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hele overgenomen` (fout = getal1) → Dat is het aantal hele waar je mee begint. Elke hele wordt in stukken verdeeld, dus je krijgt meer stukken.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? Elke hele geeft zoveel stukken als de noemer (het getal onder de streep) zegt: reken keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk eerst hoeveel stukken er in één hele passen, en reken dan keer het aantal hele.  [nieuw]
- Status: hints klaar

## Somtype 8: #/# [ding] chocola wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “#/# [ding] chocola wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: B15 (3) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): getal-overgenomen (3), een-ernaast (3)
- Verschillende Claude-fout-hints: 6 (meest: “Schrijf 3/6 eerst als ?/2.”)
- Voorbeelden:
  - `G8-GET-E04-claude-bank-032` (Claude B15, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3/6 reep chocola wordt verdeeld in stukken van 1/2. Hoeveel stukken zijn dat?
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 3 → Schrijf 3/6 eerst als ?/2. · 2 → 3/6 is precies 1/2.
    - **Uitleg (Claude):** 3/6 = 1/2, dus er passen 1 stuk van 1/2 in.
  - `G8-GET-E04-claude-bank-031` (Claude B15, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 6/8 reep chocola wordt verdeeld in stukken van 1/4. Hoeveel stukken zijn dat?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 6 → Schrijf 6/8 eerst als ?/4. · 4 → 6/8 is precies 3/4.
    - **Uitleg (Claude):** 6/8 = 3/4, dus er passen 3 stukken van 1/4 in.

- **Hint 1 (te schrijven):** Je zoekt hoe vaak het kleine stuk in het deel past.
- **Hint 2 (te schrijven):** Maak de twee breuken gelijknamig: geef ze dezelfde noemer (het getal onder de streep). Hoe vaak past de teller (het getal boven de streep) van het kleine stuk in de teller van het deel?
- **Ouderzin:** Je kind deelt een breuk in kleinere stukken (breuk gedeeld door breuk): met dezelfde noemer kun je de tellers vergelijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één te veel` (fout = antwoord + 1) → Dat is één stuk te veel. Tel nog eens hoe vaak het kleine stuk in het deel past.  [nieuw]
  - `noemer van het kleine stuk` (Claudes sleutel: een-ernaast) → Zoveel kleine stukken passen er in een hele. Je verdeelt geen hele, alleen een deel ervan: hoe vaak past het kleine stuk dáárin?  [Claude, taalfix]
  - `teller overgenomen` (Claudes sleutel: getal-overgenomen) → Dat is de teller van het deel (het getal boven de streep). Je zoekt hoe vaak het kleine stuk in het deel past.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk hoe vaak het kleine stuk in het deel past.  [nieuw]
- Status: hints klaar
