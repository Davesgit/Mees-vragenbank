# G6-MEET-E01 — Lengtematen omrekenen, ook met komma

Onze omschrijving: Hectometer; meetgetallen met komma; herleiden incl. hm · in onze bank: 8 items

Claude-vragen gemapt: **113** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # cm = □ m

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# cm = □ m” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M11 (31) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (41), getal-overgenomen (21)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-027` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 11.000 cm = □ m
    - **Antwoord:** 110  (controle: ok)
    - **Fout-hints (Claude):** 5500 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 11.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G6-MEET-E01-claude-bank-023` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** 27.000 cm = □ m
    - **Antwoord:** 270  (controle: ok)
    - **Fout-hints (Claude):** 27 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén meter (m) is honderd centimeter (cm). Een meter is groter dan een centimeter, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal centimeter door honderd: haal er twee nullen af.
- **Ouderzin:** Je kind rekent lengtematen om: van centimeter naar meter (gedeeld door honderd).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Honderd centimeter is één meter: deel door honderd.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar meter? Honderd centimeter is één meter: deel door honderd.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Je hebt door duizend gedeeld. Honderd centimeter is één meter: deel door honderd.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Honderd centimeter is één meter: deel door honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is honderd centimeter (cm). Deel het aantal centimeter door honderd.  [nieuw]
- Status: hints klaar

## Somtype 2: # km = □ m

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# km = □ m” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M9 (31) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (48), getal-overgenomen (14)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-040` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 11 km = □ m
    - **Antwoord:** 11.000  (controle: ok)
    - **Fout-hints (Claude):** 110.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1100 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E01-claude-bank-033` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 27 km = □ m
    - **Antwoord:** 27.000  (controle: ok)
    - **Fout-hints (Claude):** 81 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén kilometer (km) is duizend meter (m). Een meter is kleiner dan een kilometer, dus het getal wordt groter.
- **Hint 2 (te schrijven):** Doe het aantal kilometer keer duizend: schrijf er drie nullen achter.
- **Ouderzin:** Je kind rekent lengtematen om: van kilometer naar meter (keer duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Eén kilometer is duizend meter: doe keer duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Eén kilometer is duizend meter: doe keer duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Heb je helemaal omgerekend naar meter? Eén kilometer is duizend meter: doe keer duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Eén kilometer is duizend meter: doe keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer (km) is duizend meter (m). Doe het aantal kilometer keer duizend.  [nieuw]
- Status: hints klaar

## Somtype 3: # m = □ mm

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# m = □ mm” (koppeling: claudeId)
- Items: **31** · Claude-doelen: M9 (31) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 31 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (44), getal-overgenomen (18)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-090` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 11 m = □ mm
    - **Antwoord:** 11.000  (controle: ok)
    - **Fout-hints (Claude):** 33 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1100 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G6-MEET-E01-claude-bank-085` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 27 m = □ mm
    - **Antwoord:** 27.000  (controle: ok)
    - **Fout-hints (Claude):** 2700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 27 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén meter (m) is duizend millimeter (mm). Een millimeter is kleiner dan een meter, dus het getal wordt groter.
- **Hint 2 (te schrijven):** Doe het aantal meter keer duizend: schrijf er drie nullen achter.
- **Ouderzin:** Je kind rekent lengtematen om: van meter naar millimeter (keer duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Eén meter is duizend millimeter: doe keer duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Eén meter is duizend millimeter: doe keer duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Heb je helemaal omgerekend naar millimeter? Eén meter is duizend millimeter: doe keer duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Eén meter is duizend millimeter: doe keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is duizend millimeter (mm). Doe het aantal meter keer duizend.  [nieuw]
- Status: hints klaar

## Somtype 4: # m = □ km

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# m = □ km” (koppeling: claudeId)
- Items: **9** · Claude-doelen: M9 (9) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 9 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (12), getal-overgenomen (6)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-064` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 20.000 m = □ km
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 20.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G6-MEET-E01-claude-bank-070` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 70.000 m = □ km
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 70.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén kilometer (km) is duizend meter (m). Een kilometer is groter dan een meter, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal meter door duizend: haal er drie nullen af.
- **Ouderzin:** Je kind rekent lengtematen om: van meter naar kilometer (gedeeld door duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Duizend meter is één kilometer: deel door duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar kilometer? Duizend meter is één kilometer: deel door duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Duizend meter is één kilometer: deel door duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Duizend meter is één kilometer: deel door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer (km) is duizend meter (m). Deel het aantal meter door duizend.  [nieuw]
- Status: hints klaar

## Somtype 5: # mm = □ m

- Sleutel: nrOrigineel **5** · somtypeOrigineel “# mm = □ m” (koppeling: claudeId)
- Items: **9** · Claude-doelen: M9 (9) · regel: G6-M04-herleiden
- Getallenruimte: 0–100.000 · type: invullen
- Uit de G5-park: 9 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (10), getal-overgenomen (8)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-111` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 20.000 mm = □ m
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 200 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 20.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G6-MEET-E01-claude-bank-103` (Claude M9, bank, niveau 3 → toepassen)
    - **Opgave:** 70.000 mm = □ m
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 700 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 70.000 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Eén meter (m) is duizend millimeter (mm). Een meter is groter dan een millimeter, dus het getal wordt kleiner.
- **Hint 2 (te schrijven):** Deel het aantal millimeter door duizend: haal er drie nullen af.
- **Ouderzin:** Je kind rekent lengtematen om: van millimeter naar meter (gedeeld door duizend).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet omgerekend` (fout = getal1) → Je hebt het getal niet omgerekend. Duizend millimeter is één meter: deel door duizend.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Heb je helemaal omgerekend naar meter? Duizend millimeter is één meter: deel door duizend.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Duizend millimeter is één meter: deel door duizend.  [nieuw]
  - `aantal nullen als factor (keer)` (fout = getal1 keer het aantal nullen van de factor) → Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.  [nieuw]
  - `aantal nullen als factor (delen)` (fout = getal1 gedeeld door het aantal nullen van de factor) → Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.  [nieuw]
  - `anders omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken nog eens om. Duizend millimeter is één meter: deel door duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén meter (m) is duizend millimeter (mm). Deel het aantal millimeter door duizend.  [nieuw]
- Status: hints klaar

## Somtype 6: [schema] strook

- Sleutel: nrOrigineel **7** · somtypeOrigineel “[schema] strook” (koppeling: claudeId)
- Items: **2** · Claude-doelen: W4 (2) · regel: G6-W04-schema-strook
- Getallenruimte: 0–10.000 · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2), verkeerde-bewerking (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 4 (meest: “Bedenk eerst hoeveel meter er in 1 km gaan.”)
- Voorbeelden:
  - `G6-MEET-E01-claude-bank-116` (Claude W4, ai, niveau 3 → toepassen)
    - **Opgave:** Je fietst 3 km naar de bibliotheek en daarna 2 km naar huis. Je tekent dit als één lange strook. Hoeveel meter is dat samen?
    - **Opties:** A) 1000 meter · B) 5000 meter · C) 500 meter
    - **Antwoord:** 5000 meter  (controle: n.v.t.)
    - **Fout-hints (Claude):** 500 meter → Bedenk eerst hoeveel meter er in 1 km gaan. · 1000 meter → Je hebt twee stukken gefietst. Tel eerst de kilometers bij elkaar op.
    - **Uitleg (Claude):** Samen fiets je 3 + 2 = 5 km. In 1 km zitten 1000 meter. Dus de strook is 5000 meter lang.
  - `G6-MEET-E01-claude-bank-117` (Claude W4, ai, niveau 3 → toepassen)
    - **Opgave:** Je wandelt eerst 2 km en daarna nog 1500 meter. Je tekent alles als één lange strook in meters. Hoeveel meter is dat samen?
    - **Opties:** A) 3,5 meter · B) 3500 meter · C) 1700 meter
    - **Antwoord:** 3500 meter  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1700 meter → Reken de kilometers eerst goed om. 1 km is veel meer dan 100 meter. · 3,5 meter → Let op de eenheid. De strook gaat over meters, niet over kilometers.
    - **Uitleg (Claude):** 2 km is 2000 meter. Samen met 1500 meter wordt de strook 2000 + 1500 meter. Dat is 3500 meter.

- **Hint 1 (te schrijven):** Maak eerst van alles meters: één kilometer is duizend meter.
- **Hint 2 (te schrijven):** Tel daarna alle stukken bij elkaar op. Zo lang is de hele strook.
- **Ouderzin:** Je kind tekent afstanden als één strook en rekent kilometers om naar meters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet goed omgerekend` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Reken de kilometers goed om naar meters: één kilometer is duizend meter. Tel daarna alles bij elkaar op.  [Claude, taalfix]
  - `in kilometers` (Claudes sleutel: plaatswaarde-verkeerd) → Dat is het aantal kilometer. Hoeveel meter is dat? Eén kilometer is duizend meter.  [Claude, taalfix]
  - `afgehaald` (Claudes sleutel: verkeerde-bewerking) → Je hebt de stukken van elkaar afgehaald. De strook is alles samen: tel de stukken bij elkaar op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak van alle stukken meters: één kilometer is duizend meter. Tel de stukken daarna bij elkaar op.  [nieuw]
- Status: hints klaar
