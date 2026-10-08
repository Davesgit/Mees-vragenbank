# G5-MEET-E05 — Gram en kilogram wegen

Onze omschrijving: Gram (1000 g = 1 kg); weegschaal tot gram · in onze bank: 8 items

Claude-vragen gemapt: **17** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # kg = □ g

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# kg = □ g” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M13 (8) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (11), getal-overgenomen (5)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E05-claude-bank-007` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 2 kg = □ g
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G5-MEET-E05-claude-bank-009` (Claude M13, bank, niveau 3 → toepassen)
    - **Opgave:** 6 kg = □ g
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 60.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 600 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén kilogram (kg) is duizend gram (g). Hoeveel kilogram zijn het?
- **Hint 2 (te schrijven):** Doe het aantal kilogram keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent kilogrammen om naar grammen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén kilogram is duizend gram: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén kilogram is duizend gram: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar

## Somtype 2: [referentie] Hoe zwaar is … ongeveer?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[referentie] Hoe zwaar is … ongeveer?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: M27 (6) · regel: G5-M06-referentie, FX-G4-30
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): tiental-ernaast (6), eenheid-verkeerd-omgerekend (5), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 12 (meest: “12 g is zo licht als een doosje paperclips. Een banaan voelt zwaarder aan.”)
- Voorbeelden:
  - `G5-MEET-E05-claude-bank-015` (Claude M27, ai, niveau 1 → basis)
    - **Opgave:** Hoe zwaar is een banaan ongeveer?
    - **Opties:** A) 120 g · B) 12 g · C) 1 kg
    - **Antwoord:** 120 g  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 g → 12 g is zo licht als een doosje paperclips. Een banaan voelt zwaarder aan. · 1 kg → 1 kg is een heel pak suiker. Vergelijk een banaan eens met een appel.
    - **Uitleg (Claude):** Een banaan weegt bijna net zo veel als een appel. Een appel weegt 150 gram, een banaan ongeveer 120 gram. Fruit weeg je dus in grammen.
  - `G5-MEET-E05-claude-bank-016` (Claude M27, ai, niveau 2 → toepassen)
    - **Opgave:** Hoe zwaar is een dik schoolboek ongeveer?
    - **Opties:** A) 500 g · B) 5 g · C) 5 kg
    - **Antwoord:** 500 g  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 g → 5 g is zo licht als een paar blaadjes papier. Een heel boek is zwaarder. · 5 kg → 5 kg is zo zwaar als vijf pakken suiker. Dat kun je bijna niet met één hand vasthouden.
    - **Uitleg (Claude):** Een dik schoolboek weegt ongeveer een halve kilo, dus 500 gram. Dat is net zo zwaar als drie appels. Twee van die boeken samen zijn ongeveer 1 kilo.

- **Hint 1 (te schrijven):** Stel je voor dat je het in je hand hebt. Is het licht of zwaar?
- **Hint 2 (te schrijven):** Een pak suiker weegt één kilogram. Een gram is heel licht, zo licht als een paperclip. Welke maat past het best?
- **Ouderzin:** Je kind schat hoe zwaar iets is, met maten die het kent.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te licht (6 g)` (6 g) → Dat is te licht. 6 g is ongeveer zo licht als een velletje papier. Een ei voelt zwaarder aan.  [nieuw]
  - `te zwaar (600 g)` (600 g) → Dat is te zwaar. 600 g is bijna een heel brood. Vergelijk een ei eens met een appel.  [nieuw]
  - `te licht (12 g)` (12 g) → Dat is te licht. 12 g is zo licht als een stuk of twaalf paperclips. Een banaan voelt zwaarder aan.  [nieuw]
  - `te zwaar (1 kg)` (1 kg) → Dat is te zwaar. 1 kg is een heel pak suiker. Vergelijk een banaan eens met een appel.  [nieuw]
  - `te licht (appel)` (15 g) → Dat is te licht. 15 g is zo licht als een paar knikkers. Voelt een appel zo licht aan?  [nieuw]
  - `te licht (5 g)` (5 g) → Dat is te licht. 5 g is zo licht als een velletje papier. Een heel boek is zwaarder.  [nieuw]
  - `te zwaar (5 kg)` (5 kg) → Dat is veel te zwaar voor een boek. 5 kg is zo zwaar als vijf pakken suiker.  [nieuw]
  - `te zwaar (8 kg)` (8 kg) → Dat is veel te zwaar. 8 kg is zo zwaar als acht pakken suiker. Dat draag je niet zomaar in één hand.  [nieuw]
  - `te licht (80 g)` (80 g) → Dat is te licht. 80 g is nog lichter dan een appel. Til in gedachten een heel brood op.  [nieuw]
  - `te zwaar (150 kg)` (150 kg) → Dat is veel te zwaar. 150 kg is zo zwaar als twee volwassen mensen samen. Til in gedachten een appel eens op.  [nieuw]
  - `te licht (400 g)` (400 g) → Dat is te licht. 400 g is minder dan een brood. Til in gedachten een kat eens op.  [nieuw]
  - `te zwaar (40 kg)` (40 kg) → Dat is veel te zwaar. 40 kg is zwaarder dan een kind uit groep 5. Zo zwaar is een kat niet.  [nieuw]
  - `andere maat` (Claudes sleutel (tekst per item)) → Claudes tekst per foute optie: … is zo groot/zwaar als … (iets dat je kent). Past dat?  [Claude, ok]
  - `andere fout` (andere fout) → Zie het voor je. Vergelijk het met iets dat je kent. Welke maat past het best?  [nieuw]
- Status: hints klaar

## Somtype 3: Een [ding] is # kg zwaar. Hoeveel g is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een [ding] is # kg zwaar. Hoeveel g is dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: M13 (3) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (9)
- Verschillende Claude-fout-hints: 3 (meest: “Een nul te weinig. 1 kg is 1000 g.”)
- Voorbeelden:
  - `G5-MEET-E05-claude-bank-013` (Claude M13, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een pakket is 8 kg zwaar. Hoeveel g is dat?
    - **Antwoord:** 8000  (controle: ok)
    - **Fout-hints (Claude):** 800 → Een nul te weinig. 1 kg is 1000 g. · 80.000 → Een nul te veel. 1 kg is 1000 g. · 8 → Het getal verandert als de eenheid verandert. Van kg naar g is keer 1.000.
    - **Uitleg (Claude):** 1 kg = 1000 g. Dus 8 kg = 8 × 1000 = 8000 g.
  - `G5-MEET-E05-claude-bank-010` (Claude M13, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een pakket is 9 kg zwaar. Hoeveel g is dat?
    - **Antwoord:** 9000  (controle: ok)
    - **Fout-hints (Claude):** 900 → Een nul te weinig. 1 kg is 1000 g. · 90.000 → Een nul te veel. 1 kg is 1000 g. · 9 → Het getal verandert als de eenheid verandert. Van kg naar g is keer 1.000.
    - **Uitleg (Claude):** 1 kg = 1000 g. Dus 9 kg = 9 × 1000 = 9000 g.

- **Hint 1 (te schrijven):** Eén kilogram (kg) is duizend gram (g). Hoeveel kilogram is het?
- **Hint 2 (te schrijven):** Doe het aantal kilogram keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent kilogrammen om naar grammen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén kilogram is duizend gram: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén kilogram is duizend gram: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar
