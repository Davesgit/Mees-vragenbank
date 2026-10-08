# G7-MEET-03 — Inhoud en gewicht

Onze omschrijving: Inhoud/gewicht · in onze bank: 8 items

Claude-vragen gemapt: **1702** in **10** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een balk heeft een inhoud van # [ding]. De bodem is # bij # cm. Hoe hoog is de balk in cm?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een balk heeft een inhoud van # [ding]. De bodem is # bij # cm. Hoe hoog is de balk in cm?” (koppeling: claudeId)
- Items: **838** · Claude-doelen: M18 (838) · regel: G7-M04-inhoud-cm3
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Uit de G6-park: 838 items
- Denkfouten (Claude): een-ernaast (1030), optellen-ipv-vermenigvuldigen (646)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-399` (Claude M18, bank, niveau 3 → toepassen)
    - **Opgave:** Een balk heeft een inhoud van 1188 cm³. De bodem is 12 bij 11 cm. Hoe hoog is de balk in cm?
    - **Antwoord:** 9  (controle: ok)
    - **Fout-hints (Claude):** 23 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen. · 8 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G7-MEET-03-claude-bank-538` (Claude M18, bank, niveau 3 → toepassen)
    - **Opgave:** Een balk heeft een inhoud van 308 cm³. De bodem is 7 bij 11 cm. Hoe hoog is de balk in cm?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 18 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen. · 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Een balk is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ is de inhoud?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een balk is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ is de inhoud?” (koppeling: claudeId)
- Items: **518** · Claude-doelen: M18 (518) · regel: G7-M04-inhoud-cm3
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Uit de G6-park: 518 items
- Denkfouten (Claude): een-ernaast (562), deel-vergeten-bij-splitsen (298), optellen-ipv-vermenigvuldigen (176)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-1445` (Claude M18, bank, niveau 3 → toepassen)
    - **Opgave:** Een balk is 2 cm lang, 3 cm breed en 4 cm hoog. Hoeveel cm³ is de inhoud?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 6 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 9 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.
  - `G7-MEET-03-claude-bank-1238` (Claude M18, bank, niveau 3 → toepassen)
    - **Opgave:** Een balk is 11 cm lang, 12 cm breed en 8 cm hoog. Hoeveel cm³ is de inhoud?
    - **Antwoord:** 1056  (controle: ok)
    - **Fout-hints (Claude):** 1188 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 924 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: # g = □ kg

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# g = □ kg” (koppeling: claudeId)
- Items: **71** · Claude-doelen: M20 (40), M13 (31) · regel: G7-M03-herleiden
- Getallenruimte: 0–1.000.000, kommagetallen (1 cijfers achter de komma) · type: invullen
- Uit de G6-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (90), getal-overgenomen (52)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-054` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 110.000 g = □ kg
    - **Antwoord:** 110  (controle: ok)
    - **Fout-hints (Claude):** 1100 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 110.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-03-claude-bank-086` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** 700 g = □ kg
    - **Antwoord:** 0,7  (controle: ok)
    - **Fout-hints (Claude):** 7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 700 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: # ml = □ L

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# ml = □ L” (koppeling: claudeId)
- Items: **71** · Claude-doelen: M20 (40), M12 (31) · regel: G7-M03-herleiden
- Getallenruimte: 0–1.000.000, kommagetallen (1 cijfers achter de komma) · type: invullen
- Uit de G6-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (90), getal-overgenomen (52)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-141` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 110.000 ml = □ L
    - **Antwoord:** 110  (controle: ok)
    - **Fout-hints (Claude):** 11 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 110.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-03-claude-bank-169` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** 700 ml = □ L
    - **Antwoord:** 0,7  (controle: ok)
    - **Fout-hints (Claude):** 7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 700 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Vul in. # L = ... ml

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Vul in. # L = ... ml” (koppeling: claudeId)
- Items: **44** · Claude-doelen: M20 (44) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (49), getal-overgenomen (31), komma-verschoven (8)
- Verschillende Claude-fout-hints: 4 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-1654` (Claude M20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Vul in. 7,19 L = ... ml
    - **Antwoord:** 7190  (controle: ok)
    - **Fout-hints (Claude):** 719 → Van l naar ml schuift de komma 3 plekken. Eén te weinig. · 71.900 → Van l naar ml schuift de komma 3 plekken. Eén te veel.
    - **Uitleg (Claude):** 1 L = 1000 ml. Keer 1000: de komma schuift 3 plekken naar rechts. 7,19 L = 7190 ml.
  - `G7-MEET-03-claude-bank-1644` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 3,2 L = ... ml
    - **Antwoord:** 3200  (controle: ok)
    - **Fout-hints (Claude):** 9,6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 320 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Vul in. # kg = ... g

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Vul in. # kg = ... g” (koppeling: claudeId)
- Items: **44** · Claude-doelen: M20 (44) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (54), getal-overgenomen (26), komma-verschoven (8)
- Verschillende Claude-fout-hints: 4 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-1686` (Claude M20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Vul in. 6,14 kg = ... g
    - **Antwoord:** 6140  (controle: ok)
    - **Fout-hints (Claude):** 614 → Van kg naar g schuift de komma 3 plekken. Eén te weinig. · 61.400 → Van kg naar g schuift de komma 3 plekken. Eén te veel.
    - **Uitleg (Claude):** 1 kg = 1000 g. Keer 1000: de komma schuift 3 plekken naar rechts. 6,14 kg = 6140 g.
  - `G7-MEET-03-claude-bank-1670` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 3,2 kg = ... g
    - **Antwoord:** 3200  (controle: ok)
    - **Fout-hints (Claude):** 32.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 3,2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: # cl = □ L

- Sleutel: nrOrigineel **7** · somtypeOrigineel “# cl = □ L” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M20 (40) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (57), getal-overgenomen (23)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-011` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** 20 cl = □ L
    - **Antwoord:** 0,2  (controle: ok)
    - **Fout-hints (Claude):** 10 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 0,02 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G7-MEET-03-claude-bank-029` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** 240 cl = □ L
    - **Antwoord:** 2,4  (controle: ok)
    - **Fout-hints (Claude):** 24 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 240 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Vul in. # L = ... cl

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Vul in. # L = ... cl” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M20 (40) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (56), getal-overgenomen (24)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-1611` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** Vul in. 1,2 L = ... cl
    - **Antwoord:** 120  (controle: ok)
    - **Fout-hints (Claude):** 2,4 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1,2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-03-claude-bank-1604` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** Vul in. 3,4 L = ... cl
    - **Antwoord:** 340  (controle: ok)
    - **Fout-hints (Claude):** 3400 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 34 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Een bak is # m lang, # m breed en # m hoog. Hoeveel m³ gaat erin?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een bak is # m lang, # m breed en # m hoog. Hoeveel m³ gaat erin?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: M22 (32) · regel: G7-M05-inhoud-m3
- Getallenruimte: 0–1.000, kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (42), kommagetal-als-geheel (16), komma-verschoven (16), optellen-ipv-vermenigvuldigen (14)
- Verschillende Claude-fout-hints: 8 (meest: “Dit is de oppervlakte van de bodem. Voor de inhoud vermenigvuldig je ook met de hoogte.”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-206` (Claude M22, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een bak in het moeras is 7 m lang, 2 m breed en 3 m hoog. Hoeveel m³ gaat erin?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 14 → Dit is de oppervlakte van de bodem. Voor de inhoud vermenigvuldig je ook met de hoogte. · 12 → Inhoud bereken je door te vermenigvuldigen, niet op te tellen. · 82 → Dat is de buitenkant. Inhoud is lengte × breedte × hoogte.
    - **Uitleg (Claude):** Inhoud = lengte × breedte × hoogte = 7 × 2 × 3 = 42 m³.
  - `G7-MEET-03-claude-bank-217` (Claude M22, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bak in de vallei is 2 m lang, 2 m breed en 1,5 m hoog. Hoeveel m³ gaat erin?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 4 → De hoogte is 1,5, niet 1. Reken de halve meter mee. · 60 → Let op de komma bij het vermenigvuldigen met de hoogte.
    - **Uitleg (Claude):** 2 × 2 = 4 m² bodem. 4 × 1,5 = 6,0 m³.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Een bak is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ gaat erin?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Een bak is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ gaat erin?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M18 (4) · regel: G7-M04-inhoud-cm3
- Getallenruimte: 0–1.000 · type: kale
- Uit de G6-park: 4 items
- Denkfouten (Claude): deel-vergeten-bij-splitsen (4), optellen-ipv-vermenigvuldigen (4), omtrek-oppervlakte-verwisseld (4)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is de bodem. Er zijn nog lagen erbovenop: keer de hoogte.”)
- Voorbeelden:
  - `G7-MEET-03-claude-bank-184` (Claude M18, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een doos voor eieren is 10 cm lang, 3 cm breed en 2 cm hoog. Hoeveel cm³ past erin?
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** 30 → Dat is de bodem. Er zijn nog lagen erbovenop: keer de hoogte. · 15 → Inhoud is keer, keer, keer. Niet optellen. · 112 → Dat is de oppervlakte van alle zijkanten. Inhoud is wat erin past.
    - **Uitleg (Claude):** Inhoud is lengte × breedte × hoogte. Eerst de bodem: 10 × 3 = 30 cm². Dan 2 lagen: 30 × 2 = 60 cm³.
  - `G7-MEET-03-claude-bank-186` (Claude M18, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een doos voor poesjes is 10 cm lang, 8 cm breed en 6 cm hoog. Hoeveel cm³ past erin?
    - **Antwoord:** 480  (controle: ok)
    - **Fout-hints (Claude):** 80 → Dat is de bodem. Er zijn nog lagen erbovenop: keer de hoogte. · 24 → Inhoud is keer, keer, keer. Niet optellen. · 376 → Dat is de oppervlakte van alle zijkanten. Inhoud is wat erin past.
    - **Uitleg (Claude):** Inhoud is lengte × breedte × hoogte. Eerst de bodem: 10 × 8 = 80 cm². Dan 6 lagen: 80 × 6 = 480 cm³.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
