# G7-MEET-01 — Lengte en omtrek meten

Onze omschrijving: Lengte/omtrek + metriek · in onze bank: 8 items

Claude-vragen gemapt: **305** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # m = □ km

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# m = □ km” (koppeling: claudeId)
- Items: **71** · Claude-doelen: M20 (40), M9 (31) · regel: G7-M03-herleiden
- Getallenruimte: 0–1.000.000, kommagetallen (1 cijfers achter de komma) · type: invullen
- Uit de G6-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (93), getal-overgenomen (49)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-076` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** 200 m = □ km
    - **Antwoord:** 0,2  (controle: ok)
    - **Fout-hints (Claude):** 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 200 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-01-claude-bank-093` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 110.000 m = □ km
    - **Antwoord:** 110  (controle: ok)
    - **Fout-hints (Claude):** 11 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1100 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén kilometer (km) is duizend meter (m). Wordt het getal in kilometer groter of kleiner?
- **Hint 2 (te schrijven):** Deel door duizend: de komma schuift drie plekken naar links. Staat er geen komma, denk hem dan achter het getal. Een punt in een groot getal is geen komma. Is er geen cijfer meer om voorbij te schuiven? Zet er dan een nul voor. Nullen aan het eind achter de komma vallen weg, en de komma ook als er niets meer achter staat.
- **Ouderzin:** Je kind rekent meter om naar kilometer: delen door duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Dat is het getal dat je moest omrekenen, nog in meter. Hoeveel kilometer is dat?  [nieuw]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén kilometer (km) is duizend meter (m). Van meter naar kilometer deel je door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer (km) is duizend meter (m). Van meter naar kilometer deel je door duizend.  [nieuw]
- Status: hints klaar

## Somtype 2: # mm = □ m

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# mm = □ m” (koppeling: claudeId)
- Items: **71** · Claude-doelen: M20 (40), M9 (31) · regel: G7-M03-herleiden
- Getallenruimte: 0–1.000.000, kommagetallen (1 cijfers achter de komma) · type: invullen
- Uit de G6-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (98), getal-overgenomen (44)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-144` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** 200 mm = □ m
    - **Antwoord:** 0,2  (controle: ok)
    - **Fout-hints (Claude):** 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 200 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-01-claude-bank-157` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 110.000 mm = □ m
    - **Antwoord:** 110  (controle: ok)
    - **Fout-hints (Claude):** 1100 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 110.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén meter (m) is duizend millimeter (mm). Wordt het getal in meter groter of kleiner?
- **Hint 2 (te schrijven):** Deel door duizend: de komma schuift drie plekken naar links. Staat er geen komma, denk hem dan achter het getal. Een punt in een groot getal is geen komma. Is er geen cijfer meer om voorbij te schuiven? Zet er dan een nul voor. Nullen aan het eind achter de komma vallen weg, en de komma ook als er niets meer achter staat.
- **Ouderzin:** Je kind rekent millimeter om naar meter: delen door duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Dat is het getal dat je moest omrekenen, nog in millimeter. Hoeveel meter is dat?  [nieuw]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén meter (m) is duizend millimeter (mm). Van millimeter naar meter deel je door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is duizend millimeter (mm). Van millimeter naar meter deel je door duizend.  [nieuw]
- Status: hints klaar

## Somtype 3: Vul in. # m = ... cm

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Vul in. # m = ... cm” (koppeling: claudeId)
- Items: **43** · Claude-doelen: M20 (43) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (57), getal-overgenomen (21), komma-verschoven (8)
- Verschillende Claude-fout-hints: 4 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-231` (Claude M20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Vul in. 2 m = ... cm
    - **Antwoord:** 200  (controle: ok)
    - **Fout-hints (Claude):** 20 → Van m naar cm schuift de komma 2 plekken. Eén te weinig. · 2000 → Van m naar cm schuift de komma 2 plekken. Eén te veel.
    - **Uitleg (Claude):** 1 m = 100 cm. Keer 100: de komma schuift 2 plekken naar rechts. 2,00 m = 200 cm.
  - `G7-MEET-01-claude-bank-229` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** Vul in. 3,2 m = ... cm
    - **Antwoord:** 320  (controle: ok)
    - **Fout-hints (Claude):** 6,4 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 32 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén meter (m) is honderd centimeter (cm). Wordt het getal in centimeter groter of kleiner?
- **Hint 2 (te schrijven):** Doe keer honderd: de komma schuift twee plekken naar rechts. Staat er geen komma, denk hem dan achter het getal. Vul lege plekken op met nullen.
- **Ouderzin:** Je kind rekent meter om naar centimeter: keer honderd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Hoeveel plekken schuift de komma van meter naar centimeter?  [nieuw]
  - `een nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Hoeveel plekken schuift de komma van meter naar centimeter?  [nieuw]
  - `niet omgerekend` (Claudes sleutel: getal-overgenomen) → Dat is het getal dat je moest omrekenen, nog in meter. Hoeveel centimeter is dat?  [Claude, taalfix]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén meter (m) is honderd centimeter (cm). Van meter naar centimeter doe je keer honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is honderd centimeter (cm). Van meter naar centimeter doe je keer honderd.  [nieuw]
- Status: hints klaar

## Somtype 4: # cm = □ m

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# cm = □ m” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M20 (40) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (59), getal-overgenomen (21)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-020` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** 20 cm = □ m
    - **Antwoord:** 0,2  (controle: ok)
    - **Fout-hints (Claude):** 0,02 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G7-MEET-01-claude-bank-038` (Claude M20, bank, niveau 2 → toepassen)
    - **Opgave:** 240 cm = □ m
    - **Antwoord:** 2,4  (controle: ok)
    - **Fout-hints (Claude):** 120 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 24 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén meter (m) is honderd centimeter (cm). Wordt het getal in meter groter of kleiner?
- **Hint 2 (te schrijven):** Deel door honderd: de komma schuift twee plekken naar links. Staat er geen komma, denk hem dan achter het getal. Is er geen cijfer meer om voorbij te schuiven? Zet er dan een nul voor. Nullen aan het eind achter de komma vallen weg, en de komma ook als er niets meer achter staat.
- **Ouderzin:** Je kind rekent centimeter om naar meter: delen door honderd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Dat is het getal dat je moest omrekenen, nog in centimeter. Hoeveel meter is dat?  [nieuw]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén meter (m) is honderd centimeter (cm). Van centimeter naar meter deel je door honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is honderd centimeter (cm). Van centimeter naar meter deel je door honderd.  [nieuw]
- Status: hints klaar

## Somtype 5: Vul in. # km = ... m

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Vul in. # km = ... m” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M20 (40) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (58), getal-overgenomen (22)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-196` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 1,2 km = ... m
    - **Antwoord:** 1200  (controle: ok)
    - **Fout-hints (Claude):** 12.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1,2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-01-claude-bank-206` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 3,4 km = ... m
    - **Antwoord:** 3400  (controle: ok)
    - **Fout-hints (Claude):** 340 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 3,4 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén kilometer (km) is duizend meter (m). Wordt het getal in meter groter of kleiner?
- **Hint 2 (te schrijven):** Doe keer duizend: de komma schuift drie plekken naar rechts. Vul lege plekken op met nullen.
- **Ouderzin:** Je kind rekent kilometer om naar meter: keer duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Hoeveel plekken schuift de komma van kilometer naar meter?  [nieuw]
  - `een nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Hoeveel plekken schuift de komma van kilometer naar meter?  [nieuw]
  - `niet omgerekend` (Claudes sleutel: getal-overgenomen) → Dat is het getal dat je moest omrekenen, nog in kilometer. Hoeveel meter is dat?  [Claude, taalfix]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén kilometer (km) is duizend meter (m). Van kilometer naar meter doe je keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer (km) is duizend meter (m). Van kilometer naar meter doe je keer duizend.  [nieuw]
- Status: hints klaar

## Somtype 6: Vul in. # m = ... mm

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Vul in. # m = ... mm” (koppeling: claudeId)
- Items: **40** · Claude-doelen: M20 (40) · regel: G7-M03-herleiden
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (54), getal-overgenomen (26)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G7-MEET-01-claude-bank-267` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 1,2 m = ... mm
    - **Antwoord:** 1200  (controle: ok)
    - **Fout-hints (Claude):** 120 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1,2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G7-MEET-01-claude-bank-289` (Claude M20, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 3,4 m = ... mm
    - **Antwoord:** 3400  (controle: ok)
    - **Fout-hints (Claude):** 10,2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 340 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén meter (m) is duizend millimeter (mm). Wordt het getal in millimeter groter of kleiner?
- **Hint 2 (te schrijven):** Doe keer duizend: de komma schuift drie plekken naar rechts. Vul lege plekken op met nullen.
- **Ouderzin:** Je kind rekent meter om naar millimeter: keer duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een nul te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Hoeveel plekken schuift de komma van meter naar millimeter?  [nieuw]
  - `een nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Hoeveel plekken schuift de komma van meter naar millimeter?  [nieuw]
  - `niet omgerekend` (Claudes sleutel: getal-overgenomen) → Dat is het getal dat je moest omrekenen, nog in meter. Hoeveel millimeter is dat?  [Claude, taalfix]
  - `verkeerd omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Klopt het omrekenen? Eén meter (m) is duizend millimeter (mm). Van meter naar millimeter doe je keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is duizend millimeter (mm). Van meter naar millimeter doe je keer duizend.  [nieuw]
- Status: hints klaar
