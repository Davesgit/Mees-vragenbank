# G5-MEET-E01 — Millimeter tot kilometer

Onze omschrijving: mm, dm, km + relaties; meten tot mm; herleiden m↔dm/cm/km · in onze bank: 8 items

Claude-vragen gemapt: **57** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # m = □ cm

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# m = □ cm” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M11 (31) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (43), getal-overgenomen (19)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E01-claude-bank-032` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 11 m = □ cm
    - **Antwoord:** 1100  (controle: ok)
    - **Fout-hints (Claude):** 110 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 11 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G5-MEET-E01-claude-bank-037` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 27 m = □ cm
    - **Antwoord:** 2700  (controle: ok)
    - **Fout-hints (Claude):** 54 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 270 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén meter (m) is honderd centimeter (cm). Hoeveel meter zijn het?
- **Hint 2 (te schrijven):** Doe het aantal meter keer honderd: zet er twee nullen achter.
- **Ouderzin:** Je kind rekent meters om naar centimeters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén meter is honderd centimeter: zet er twee nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén meter is honderd centimeter: zet er twee nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een centimeter is kleiner dan een meter, dus het worden er meer. Zet er twee nullen achter.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een centimeter is kleiner dan een meter, dus het worden er meer. Zet er twee nullen achter.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén meter is honderd centimeter. Doe het aantal meter keer honderd.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén meter is honderd centimeter. Doe het aantal meter keer honderd.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén meter is honderd centimeter. Doe het aantal meter keer honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter is honderd centimeter. Doe het aantal meter keer honderd: zet er twee nullen achter.  [nieuw]
- Status: hints klaar

## Somtype 2: # cm = □ m

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# cm = □ m” (koppeling: claudeId)
- Items: **9** · Claude-doelen: M11 (9) · regel: G5-M01-omrekenen
- Getallenruimte: 0–1.000, 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (13), getal-overgenomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E01-claude-bank-002` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 200 cm = □ m
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 1000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G5-MEET-E01-claude-bank-003` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 7000 cm = □ m
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 3500 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Honderd centimeter (cm) is één meter (m). Hoe vaak past honderd in het aantal centimeter?
- **Hint 2 (te schrijven):** Deel het aantal centimeter door honderd: haal er twee nullen af.
- **Ouderzin:** Je kind rekent centimeters om naar meters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat nog een nul te veel achter. Honderd centimeter is één meter: haal er twee nullen af.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: je hebt een nul te veel weggehaald. Honderd centimeter is één meter: haal er twee nullen af.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een meter is groter dan een centimeter, dus het worden er minder. Haal er twee nullen af.  [Claude, taalfix]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een meter is groter dan een centimeter, dus het worden er minder. Haal er twee nullen af.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Honderd centimeter is één meter. Deel het aantal centimeter door honderd.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Honderd centimeter is één meter. Deel het aantal centimeter door honderd.  [nieuw]
  - `andere fout` (andere fout) → Honderd centimeter is één meter. Deel het aantal centimeter door honderd: haal er twee nullen af.  [nieuw]
- Status: hints klaar

## Somtype 3: # km = □ m

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# km = □ m” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M9 (8) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (14), getal-overgenomen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E01-claude-bank-012` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 2 km = □ m
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 20.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G5-MEET-E01-claude-bank-011` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 6 km = □ m
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 60.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 6 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén kilometer (km) is duizend meter (m). Hoeveel kilometer zijn het?
- **Hint 2 (te schrijven):** Doe het aantal kilometer keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent kilometers om naar meters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén kilometer is duizend meter: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén kilometer is duizend meter: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een meter is kleiner dan een kilometer, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een meter is kleiner dan een kilometer, dus het worden er meer. Zet er drie nullen achter.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén kilometer is duizend meter. Doe het aantal kilometer keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén kilometer is duizend meter. Doe het aantal kilometer keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén kilometer is duizend meter. Doe het aantal kilometer keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer is duizend meter. Doe het aantal kilometer keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar

## Somtype 4: # m = □ mm

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# m = □ mm” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M9 (8) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (9), getal-overgenomen (7)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E01-claude-bank-056` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 2 m = □ mm
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G5-MEET-E01-claude-bank-050` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 6 m = □ mm
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 60.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 6 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén meter (m) is duizend millimeter (mm). Hoeveel meter zijn het?
- **Hint 2 (te schrijven):** Doe het aantal meter keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent meters om naar millimeters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén meter is duizend millimeter: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén meter is duizend millimeter: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een millimeter is kleiner dan een meter, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een millimeter is kleiner dan een meter, dus het worden er meer. Zet er drie nullen achter.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén meter is duizend millimeter. Doe het aantal meter keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén meter is duizend millimeter. Doe het aantal meter keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén meter is duizend millimeter. Doe het aantal meter keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter is duizend millimeter. Doe het aantal meter keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar

## Somtype 5: [referentie] Hoe lang/hoog/breed is … ongeveer?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[referentie] Hoe lang/hoog/breed is … ongeveer?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M27 (1) · regel: FX-G4-30
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): tiental-ernaast (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “10 m is iets langer dan een klaslokaal. Dan kun je nauwelijks sprinten.”)
- Voorbeelden:
  - `G5-MEET-E01-claude-bank-059` (Claude M27, ai, niveau 2 → toepassen)
    - **Opgave:** Hoe lang is een voetbalveld ongeveer?
    - **Opties:** A) 1000 m · B) 100 m · C) 10 m
    - **Antwoord:** 100 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 m → 10 m is iets langer dan een klaslokaal. Dan kun je nauwelijks sprinten. · 1000 m → 1000 m is een kilometer. Zo ver loop je in ongeveer een kwartier.
    - **Uitleg (Claude):** Een voetbalveld is ongeveer 100 m lang. Als je het afwandelt, ben je ruim een minuut onderweg.

- **Hint 1 (te schrijven):** Denk aan iets dat je kent. Is het langer of korter? Hoeveel grote stappen zou het zijn?
- **Hint 2 (te schrijven):** Een grote stap is ongeveer één meter. Een kilometer is heel ver: daar loop je ongeveer een kwartier over.
- **Ouderzin:** Je kind schat hoe lang iets is, met maten die het kent.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te kort` (10 m) → Dat is te kort. 10 m is iets langer dan een klaslokaal. Een voetbalveld is veel langer.  [nieuw]
  - `te lang (1000 m)` (1000 m) → Dat is te lang. 1000 m is een kilometer. Zo ver loop je in ongeveer een kwartier.  [nieuw]
  - `andere maat` (Claudes sleutel (tekst per item)) → Claudes tekst per foute optie: … is zo groot/zwaar als … (iets dat je kent). Past dat?  [Claude, ok]
  - `andere fout` (andere fout) → Zie het voor je. Vergelijk het met iets dat je kent. Welke maat past het best?  [nieuw]
- Status: hints klaar
