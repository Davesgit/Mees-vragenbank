# G6-MEET-E03 — Oppervlakte uitrekenen in cm², dm² en m²

Onze omschrijving: m²/dm²/cm² + herleiden; formule l×b; vorm ≠ vierkant m² · in onze bank: 8 items

Claude-vragen gemapt: **389** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een rechthoek is # cm lang en # cm breed. Hoeveel cm² is de oppervlakte?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een rechthoek is # cm lang en # cm breed. Hoeveel vierkante cm is de oppervlakte?” (koppeling: claudeId)
- Items: **253** · Claude-doelen: M17 (253) · regel: G6-M01-oppervlakte
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): een-ernaast (255), omtrek-oppervlakte-verwisseld (130), deel-vergeten-bij-splitsen (121)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-MEET-E03-claude-bank-308` (Claude M17, bank, niveau 3 → toepassen)
    - **Opgave:** Een sticker is een rechthoek van 4 cm lang en 3 cm breed. Hoeveel cm² is de oppervlakte?
    - **Antwoord:** 12  (controle: n.v.t.)
    - **Fout-hints (Claude):** 14 → Omtrek is de lijn eromheen (optellen). Oppervlakte is wat erbinnen zit (lengte keer breedte). · 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-MEET-E03-claude-bank-219` (Claude M17, bank, niveau 3 → toepassen)
    - **Opgave:** Een vlaggetje is een rechthoek van 18 cm lang en 12 cm breed. Hoeveel cm² is de oppervlakte?
    - **Antwoord:** 216  (controle: n.v.t.)
    - **Fout-hints (Claude):** 60 → Omtrek is de lijn eromheen (optellen). Oppervlakte is wat erbinnen zit (lengte keer breedte). · 198 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** De oppervlakte is wat er binnen de rechthoek zit. Je meet die in cm² (vierkante centimeter): vierkantjes van één centimeter bij één centimeter.
- **Hint 2 (te schrijven):** Leg de vierkantjes in rijen. Een rij zo lang als de lengte heeft zoveel vierkantjes als de lengte, en er passen zoveel rijen als de breedte. Met rijen zo lang als de breedte gaat het ook. Reken de lengte keer de breedte.
- **Ouderzin:** Je kind rekent de oppervlakte van een rechthoek uit in cm²: de lengte keer de breedte.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de lengte en de breedte opgeteld. Voor de oppervlakte reken je de lengte keer de breedte.  [nieuw]
  - `omtrek in plaats van oppervlakte` (fout = (getal1 + getal2) × 2) → Dat is de omtrek: de lengte van de rand eromheen. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte.  [nieuw]
  - `oppervlakte verdubbeld` (fout = antwoord × 2) → Je hebt de oppervlakte verdubbeld. De lengte keer de breedte is al de hele oppervlakte.  [nieuw]
  - `rij van de lengte te veel` (fout = antwoord + getal1) → Dat is precies één rij te veel: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de lengte te weinig` (fout = antwoord − getal1) → Dat is precies één rij te weinig: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te veel` (fout = antwoord + getal2) → Dat is precies één rij te veel: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te weinig` (fout = antwoord − getal2) → Dat is precies één rij te weinig: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `omtrek` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Dat is de omtrek: de lengte van de rand eromheen. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de lengte keer de breedte. Zoveel vierkantjes van één centimeter bij één centimeter passen erin.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Een rechthoek is # cm lang en # cm breed. Hoeveel vierkante cm is de oppervlakte?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 2: De oppervlakte van een rechthoek is # cm². Eén zijde is # cm. Hoe lang is de andere zijde in cm?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “De oppervlakte van een rechthoek is # vierkante cm. Eén zijde is # cm. Hoe lang is de andere zijde in cm?” (koppeling: claudeId)
- Items: **132** · Claude-doelen: M17 (132) · regel: G6-M01-oppervlakte
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): een-ernaast (172), verkeerde-bewerking (92)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G6-MEET-E03-claude-bank-131` (Claude M17, bank, niveau 3 → toepassen)
    - **Opgave:** De oppervlakte van een rechthoek is 6 cm². Eén zijde is 2 cm. Hoe lang is de andere zijde in cm?
    - **Antwoord:** 3  (controle: n.v.t.)
    - **Fout-hints (Claude):** 8 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G6-MEET-E03-claude-bank-006` (Claude M17, bank, niveau 3 → toepassen)
    - **Opgave:** De oppervlakte van een rechthoek is 105 cm². Eén zijde is 5 cm. Hoe lang is de andere zijde in cm?
    - **Antwoord:** 21  (controle: n.v.t.)
    - **Fout-hints (Claude):** 22 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 20 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** De oppervlakte in cm² (vierkante centimeter) is de ene zijde keer de andere zijde.
- **Hint 2 (te schrijven):** Welk getal keer de zijde die je weet, is de oppervlakte? Deel de oppervlakte door de zijde die je weet.
- **Ouderzin:** Je kind zoekt de andere zijde van een rechthoek als de oppervlakte en één zijde bekend zijn: de oppervlakte gedeeld door de zijde.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `zijde uit de vraag` (fout = getal2) → Is dat de zijde die je al weet? Je zoekt de andere zijde: deel de oppervlakte door de zijde die je weet. Reken na: jouw antwoord keer die zijde is de oppervlakte.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de oppervlakte en de zijde opgeteld. De oppervlakte is de ene zijde keer de andere: deel de oppervlakte door de zijde die je weet.  [nieuw]
  - `afgehaald` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt de zijde van de oppervlakte afgehaald. Deel de oppervlakte door de zijde die je weet.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt de oppervlakte keer de zijde gedaan. Je zoekt de andere zijde: deel de oppervlakte door de zijde die je weet.  [nieuw]
  - `één te veel` (fout = antwoord + 1 (antwoord vanaf 10)) → Bijna! Dat is één te veel. Reken na: jouw antwoord keer de zijde is dan meer dan de oppervlakte.  [nieuw]
  - `één te veel` (fout = antwoord + 1 (antwoord onder 10)) → Dat is één te veel. Reken na: jouw antwoord keer de zijde is dan meer dan de oppervlakte.  [nieuw]
  - `één te weinig` (fout = antwoord − 1 (antwoord vanaf 10)) → Bijna! Dat is één te weinig. Reken na: jouw antwoord keer de zijde is dan minder dan de oppervlakte.  [nieuw]
  - `één te weinig` (fout = antwoord − 1 (antwoord onder 10)) → Dat is één te weinig. Reken na: jouw antwoord keer de zijde is dan minder dan de oppervlakte.  [nieuw]
  - `andere fout` (andere fout) → Deel de oppervlakte door de zijde die je weet. Reken na: jouw antwoord keer die zijde moet precies de oppervlakte zijn.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'De oppervlakte van een rechthoek is # vierkante cm. Eén zijde is # cm. Hoe lang is de andere zijde in cm?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: Bij [plek] ligt een [veld] van # meter lang en # meter breed. Hoeveel m² is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Bij [plek] ligt een [veld] van # meter lang en # meter breed. Hoeveel vierkante meter is dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: M17 (3) · regel: G6-M01-oppervlakte
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (6), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 5 (meest: “Dat is de omtrek: de lijn eromheen. Oppervlakte is wat erbinnen zit: lengte × breedte.”)
- Voorbeelden:
  - `G6-MEET-E03-claude-bank-003` (Claude M17, gegenereerd, niveau 1 → basis)
    - **Opgave:** Bij de schuur ligt een tuin van 11 meter lang en 4 meter breed. Hoeveel m² is dat?
    - **Antwoord:** 44  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 → Dat is de omtrek: de lijn eromheen. Oppervlakte is wat erbinnen zit: lengte × breedte. · 15 → Stel je 4 rijen van 11 tegels voor. Hoeveel tegels zijn dat? Dat is een keersom. · 88 → Bij oppervlakte hoef je niet te verdubbelen. Dat doe je alleen bij de omtrek.
    - **Uitleg (Claude):** Oppervlakte is lengte × breedte. 11 × 4 = 44 m². Denk aan 4 rijen van 11 tegels van één meter.
  - `G6-MEET-E03-claude-bank-002` (Claude M17, gegenereerd, niveau 1 → basis)
    - **Opgave:** Bij de schuur ligt een veld van 12 meter lang en 11 meter breed. Hoeveel m² is dat?
    - **Antwoord:** 132  (controle: n.v.t.)
    - **Fout-hints (Claude):** 46 → Dat is de omtrek: de lijn eromheen. Oppervlakte is wat erbinnen zit: lengte × breedte. · 23 → Stel je 11 rijen van 12 tegels voor. Hoeveel tegels zijn dat? Dat is een keersom. · 264 → Bij oppervlakte hoef je niet te verdubbelen. Dat doe je alleen bij de omtrek.
    - **Uitleg (Claude):** Oppervlakte is lengte × breedte. 12 × 11 = 132 m². Denk aan 11 rijen van 12 tegels van één meter.

- **Hint 1 (te schrijven):** De oppervlakte is wat erbinnen zit. Je meet die hier in m² (vierkante meter): vierkanten van één meter bij één meter.
- **Hint 2 (te schrijven):** Leg de vierkanten van één meter bij één meter in rijen. Een rij is zo lang als de lengte, en er passen zoveel rijen als de breedte. Met rijen zo lang als de breedte gaat het ook. Reken de lengte keer de breedte.
- **Ouderzin:** Je kind rekent de oppervlakte van een rechthoekig stuk grond uit in m²: de lengte keer de breedte.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de lengte en de breedte opgeteld. Voor de oppervlakte reken je de lengte keer de breedte.  [nieuw]
  - `omtrek in plaats van oppervlakte` (fout = (getal1 + getal2) × 2) → Dat is de omtrek: de lengte van de rand eromheen. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte.  [nieuw]
  - `oppervlakte verdubbeld` (fout = antwoord × 2) → Je hebt de oppervlakte verdubbeld. De lengte keer de breedte is al de hele oppervlakte.  [nieuw]
  - `rij van de lengte te veel` (fout = antwoord + getal1) → Dat is precies één rij te veel: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de lengte te weinig` (fout = antwoord − getal1) → Dat is precies één rij te weinig: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te veel` (fout = antwoord + getal2) → Dat is precies één rij te veel: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te weinig` (fout = antwoord − getal2) → Dat is precies één rij te weinig: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `omtrek of verdubbeld` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Dat is niet de oppervlakte. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte. Je hoeft niets op te tellen of te verdubbelen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de lengte keer de breedte. Zoveel vierkanten van één meter bij één meter passen erin.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Bij [plek] ligt een [veld] van # meter lang en # meter breed. Hoeveel vierkante meter is dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: Bij het huis ligt een tuin van # meter lang en # meter breed. Hoeveel m² is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Bij het huis ligt een tuin van # meter lang en # meter breed. Hoeveel vierkante meter is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M17 (1) · regel: G6-M01-oppervlakte
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (2), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is de omtrek: de lijn eromheen. Oppervlakte is wat erbinnen zit: lengte × breedte.”)
- Voorbeelden:
  - `G6-MEET-E03-claude-bank-004` (Claude M17, gegenereerd, niveau 1 → basis)
    - **Opgave:** Bij het huis ligt een tuin van 12 meter lang en 3 meter breed. Hoeveel m² is dat?
    - **Antwoord:** 36  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 → Dat is de omtrek: de lijn eromheen. Oppervlakte is wat erbinnen zit: lengte × breedte. · 15 → Stel je 3 rijen van 12 tegels voor. Hoeveel tegels zijn dat? Dat is een keersom. · 72 → Bij oppervlakte hoef je niet te verdubbelen. Dat doe je alleen bij de omtrek.
    - **Uitleg (Claude):** Oppervlakte is lengte × breedte. 12 × 3 = 36 m². Denk aan 3 rijen van 12 tegels van één meter.

- **Hint 1 (te schrijven):** De oppervlakte is wat erbinnen zit. Je meet die hier in m² (vierkante meter): vierkanten van één meter bij één meter.
- **Hint 2 (te schrijven):** Leg de vierkanten van één meter bij één meter in rijen. Een rij is zo lang als de lengte, en er passen zoveel rijen als de breedte. Met rijen zo lang als de breedte gaat het ook. Reken de lengte keer de breedte.
- **Ouderzin:** Je kind rekent de oppervlakte van een rechthoekig stuk grond uit in m²: de lengte keer de breedte.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de lengte en de breedte opgeteld. Voor de oppervlakte reken je de lengte keer de breedte.  [nieuw]
  - `omtrek in plaats van oppervlakte` (fout = (getal1 + getal2) × 2) → Dat is de omtrek: de lengte van de rand eromheen. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte.  [nieuw]
  - `oppervlakte verdubbeld` (fout = antwoord × 2) → Je hebt de oppervlakte verdubbeld. De lengte keer de breedte is al de hele oppervlakte.  [nieuw]
  - `rij van de lengte te veel` (fout = antwoord + getal1) → Dat is precies één rij te veel: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de lengte te weinig` (fout = antwoord − getal1) → Dat is precies één rij te weinig: een rij zo lang als de lengte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te veel` (fout = antwoord + getal2) → Dat is precies één rij te veel: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `rij van de breedte te weinig` (fout = antwoord − getal2) → Dat is precies één rij te weinig: een rij zo lang als de breedte. Reken de lengte keer de breedte nog eens na.  [nieuw]
  - `omtrek of verdubbeld` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Dat is niet de oppervlakte. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte. Je hoeft niets op te tellen of te verdubbelen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de lengte keer de breedte. Zoveel vierkanten van één meter bij één meter passen erin.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Bij het huis ligt een tuin van # meter lang en # meter breed. Hoeveel vierkante meter is dat?'. Nakijken of ze nog passen.
- Status: hints klaar
