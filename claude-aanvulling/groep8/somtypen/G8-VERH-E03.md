# G8-VERH-E03 — Rekenen met schaal op de kaart

Onze omschrijving: Schaallijnen + schaalnotatie rekenen · in onze bank: 8 items

Claude-vragen gemapt: **229** in **11** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: De schaal van een kaart is # : #. Twee steden liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “De schaal van een kaart is # : #. Twee steden liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?” (koppeling: claudeId)
- Items: **53** · Claude-doelen: V7 (53) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.000.000, 0–2.500.000, 0–5.000.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (54), getal-overgenomen (52)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-195` (Claude V7, bank, niveau 2 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 200.000. Twee steden liggen op de kaart 7 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 140 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-179` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.500.000. Twee steden liggen op de kaart 7 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 175  (controle: ok)
    - **Fout-hints (Claude):** 1750 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meters` (fout = antwoord × 1000) → Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [nieuw]
- Status: hints klaar

## Somtype 2: De schaal van een kaart is # : #. Twee dorpen liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “De schaal van een kaart is # : #. Twee dorpen liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?” (koppeling: claudeId)
- Items: **52** · Claude-doelen: V7 (52) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.000.000, 0–5.000.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (54), getal-overgenomen (50)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-037` (Claude V7, bank, niveau 2 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.000.000. Twee dorpen liggen op de kaart 7 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 140  (controle: ok)
    - **Fout-hints (Claude):** 1400 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-025` (Claude V7, bank, niveau 2 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 500.000. Twee dorpen liggen op de kaart 30 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 150  (controle: ok)
    - **Fout-hints (Claude):** 1500 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meters` (fout = antwoord × 1000) → Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [nieuw]
- Status: hints klaar

## Somtype 3: De schaal van een kaart is # : #. Twee plaatsen liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “De schaal van een kaart is # : #. Twee plaatsen liggen op de kaart # cm uit elkaar. Hoeveel km is dat in het echt?” (koppeling: claudeId)
- Items: **52** · Claude-doelen: V7 (52) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.500.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (53), getal-overgenomen (51)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-096` (Claude V7, bank, niveau 2 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 500.000. Twee plaatsen liggen op de kaart 7 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** 350 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-135` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.500.000. Twee plaatsen liggen op de kaart 16 cm uit elkaar. Hoeveel km is dat in het echt?
    - **Antwoord:** 400  (controle: ok)
    - **Fout-hints (Claude):** 40 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meters` (fout = antwoord × 1000) → Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [nieuw]
- Status: hints klaar

## Somtype 4: De schaal van een kaart is # : #. Twee dorpen liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “De schaal van een kaart is # : #. Twee dorpen liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?” (koppeling: claudeId)
- Items: **20** · Claude-doelen: V7 (20) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.500.000, 0–5.000.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (30), getal-overgenomen (10)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-013` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.500.000. Twee dorpen liggen in het echt 175 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 4375 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 0,7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-019` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 400.000. Twee dorpen liggen in het echt 64 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 256 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Op de kaart is alles veel kleiner dan in het echt. Hoeveel kilometer is één centimeter op de kaart?
- **Hint 2 (te schrijven):** Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Hoe vaak past dat in de echte afstand? Zoveel centimeter is het op de kaart.
- **Ouderzin:** Je kind rekent een echte afstand in kilometers om naar centimeters op een kaart, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
- Status: hints klaar

## Somtype 5: De schaal van een kaart is # : #. Twee plaatsen liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “De schaal van een kaart is # : #. Twee plaatsen liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?” (koppeling: claudeId)
- Items: **20** · Claude-doelen: V7 (20) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.500.000, 0–5.000.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (24), getal-overgenomen (16)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-089` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 5.000.000. Twee plaatsen liggen in het echt 350 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 70 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-073` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.500.000. Twee plaatsen liggen in het echt 400 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 10.000 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 1,6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Op de kaart is alles veel kleiner dan in het echt. Hoeveel kilometer is één centimeter op de kaart?
- **Hint 2 (te schrijven):** Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Hoe vaak past dat in de echte afstand? Zoveel centimeter is het op de kaart.
- **Ouderzin:** Je kind rekent een echte afstand in kilometers om naar centimeters op een kaart, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
- Status: hints klaar

## Somtype 6: De schaal van een kaart is # : #. Twee steden liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “De schaal van een kaart is # : #. Twee steden liggen in het echt # km uit elkaar. Hoeveel cm is dat op de kaart?” (koppeling: claudeId)
- Items: **20** · Claude-doelen: V7 (20) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000.000, 0–2.500.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (29), getal-overgenomen (11)
- Verschillende Claude-fout-hints: 1 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-164` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 400.000. Twee steden liggen in het echt 28 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 112 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?
  - `G8-VERH-E03-claude-bank-145` (Claude V7, bank, niveau 3 → toepassen)
    - **Opgave:** De schaal van een kaart is 1 : 2.500.000. Twee steden liggen in het echt 425 km uit elkaar. Hoeveel cm is dat op de kaart?
    - **Antwoord:** 17  (controle: ok)
    - **Fout-hints (Claude):** 1,7 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 170 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Op de kaart is alles veel kleiner dan in het echt. Hoeveel kilometer is één centimeter op de kaart?
- **Hint 2 (te schrijven):** Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Hoe vaak past dat in de echte afstand? Zoveel centimeter is het op de kaart.
- **Ouderzin:** Je kind rekent een echte afstand in kilometers om naar centimeters op een kaart, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?  [nieuw]
- Status: hints klaar

## Somtype 7: Op een kaart met schaal # : # is de afstand van [plek] naar [plek] # cm. Hoeveel meter is dat in het echt?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Op een kaart met schaal # : # is de afstand van [plek] naar [plek] # cm. Hoeveel meter is dat in het echt?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: V7 (8) · regel: G8-P00-park-G7
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (16), nul-fout-tientallen (8)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is in centimeters. Reken om naar meters: delen door 100.”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-220` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 25.000 is de afstand van de camping naar het strand 5 cm. Hoeveel meter is dat in het echt?
    - **Antwoord:** 1250  (controle: ok)
    - **Fout-hints (Claude):** 125.000 → Dat is in centimeters. Reken om naar meters: delen door 100. · 125 → Van cm naar m is delen door 100, niet door 1000. · 12.500 → Tel de nullen nog eens. Van cm naar m haal je twee nullen weg.
    - **Uitleg (Claude):** 1 cm op de kaart is 25.000 cm in het echt. 5 cm is 5 × 25.000 = 125.000 cm. Dat is 1250 meter.
  - `G8-VERH-E03-claude-bank-226` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 10.000 is de afstand van de kerk naar het plein 3 cm. Hoeveel meter is dat in het echt?
    - **Antwoord:** 300  (controle: ok)
    - **Fout-hints (Claude):** 30.000 → Dat is in centimeters. Reken om naar meters: delen door 100. · 30 → Van cm naar m is delen door 100, niet door 1000. · 3000 → Tel de nullen nog eens. Van cm naar m haal je twee nullen weg.
    - **Uitleg (Claude):** 1 cm op de kaart is 10.000 cm in het echt. 3 cm is 3 × 10.000 = 30.000 cm. Dat is 300 meter.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Doe het aantal centimeter op de kaart keer het getal achter de dubbele punt: zoveel centimeter is het in het echt. Honderd centimeter is één meter: streep twee nullen weg.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar meters in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nog in centimeters` (fout = antwoord × 100) → Dat is het aantal centimeter in het echt. Gevraagd is meters: honderd centimeter is één meter.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel centimeter is het in het echt? Reken dat om naar meters.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel centimeter is het in het echt? Reken dat om naar meters: honderd centimeter is één meter.  [nieuw]
- Status: hints klaar

## Somtype 8: Op een kaart met schaal # : # is de afstand van de gymzaal naar de school # cm. Hoeveel meter is dat in het echt?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Op een kaart met schaal # : # is de afstand van de gymzaal naar de school # cm. Hoeveel meter is dat in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: V7 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2), nul-fout-tientallen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is in centimeters. Reken om naar meters: delen door 100.”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-227` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 25.000 is de afstand van de gymzaal naar de school 2 cm. Hoeveel meter is dat in het echt?
    - **Antwoord:** 500  (controle: ok)
    - **Fout-hints (Claude):** 50.000 → Dat is in centimeters. Reken om naar meters: delen door 100. · 50 → Van cm naar m is delen door 100, niet door 1000. · 5000 → Tel de nullen nog eens. Van cm naar m haal je twee nullen weg.
    - **Uitleg (Claude):** 1 cm op de kaart is 25.000 cm in het echt. 2 cm is 2 × 25.000 = 50.000 cm. Dat is 500 meter.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Doe het aantal centimeter op de kaart keer het getal achter de dubbele punt: zoveel centimeter is het in het echt. Honderd centimeter is één meter: streep twee nullen weg.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar meters in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nog in centimeters` (fout = antwoord × 100) → Dat is het aantal centimeter in het echt. Gevraagd is meters: honderd centimeter is één meter.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel centimeter is het in het echt? Reken dat om naar meters.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel centimeter is het in het echt? Reken dat om naar meters: honderd centimeter is één meter.  [nieuw]
- Status: hints klaar

## Somtype 9: Op een kaart met schaal # : # is de afstand van school naar huis # cm. Hoeveel meter is dat in het echt?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Op een kaart met schaal # : # is de afstand van de klas naar het huis # cm. Hoeveel meter is dat in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: V7 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2), nul-fout-tientallen (1)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is in centimeters. Reken om naar meters: delen door 100.”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-228` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 100.000 is de afstand van school naar huis 5 cm. Hoeveel meter is dat in het echt?
    - **Antwoord:** 5000  (controle: ok)
    - **Fout-hints (Claude):** 500.000 → Dat is in centimeters. Reken om naar meters: delen door 100. · 500 → Van cm naar m is delen door 100, niet door 1000. · 50.000 → Tel de nullen nog eens. Van cm naar m haal je twee nullen weg.
    - **Uitleg (Claude):** 1 cm op de kaart is 100.000 cm in het echt. 5 cm is 5 × 100.000 = 500.000 cm. Dat is 5000 meter.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Doe het aantal centimeter op de kaart keer het getal achter de dubbele punt: zoveel centimeter is het in het echt. Honderd centimeter is één meter: streep twee nullen weg.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar meters in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nog in centimeters` (fout = antwoord × 100) → Dat is het aantal centimeter in het echt. Gevraagd is meters: honderd centimeter is één meter.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderd centimeter is één meter.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel centimeter is het in het echt? Reken dat om naar meters.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel centimeter is het in het echt? Reken dat om naar meters: honderd centimeter is één meter.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Op een kaart met schaal # : # is de afstand van de klas naar het huis # cm. Hoeveel meter is dat in het echt?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 10: Op een kaart met schaal # : # is het meer # cm van de stad. Hoeveel kilometer is dat in het echt?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Op een kaart met schaal # : # is [plek] # cm van [plek]. Hoeveel kilometer is dat in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: V7 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Dat zijn meters. Een kilometer is 1000 meter.”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-218` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 200.000 is het meer 9 cm van de stad. Hoeveel kilometer is dat in het echt?
    - **Antwoord:** 18  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9000 → Dat zijn meters. Een kilometer is 1000 meter. · 90 → Een nul te veel. 1 cm is hier 1 km.
    - **Uitleg (Claude):** 1 cm op de kaart is 200.000 cm = 2000 m = 2 km in het echt. 9 × 2 = 18 km.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meters` (fout = antwoord × 1000) → Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Op een kaart met schaal # : # is [plek] # cm van [plek]. Hoeveel kilometer is dat in het echt?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 11: Op een kaart met schaal # : # is het pretpark # cm van de school. Hoeveel kilometer is dat in het echt?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Op een kaart met schaal # : # is de klas # cm van de school. Hoeveel kilometer is dat in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: V7 (1) · regel: G8-P00-park-G7
- Getallenruimte: 0–100.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Dat zijn meters. Een kilometer is 1000 meter.”)
- Voorbeelden:
  - `G8-VERH-E03-claude-bank-229` (Claude V7, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Op een kaart met schaal 1 : 200.000 is het pretpark 4 cm van de school. Hoeveel kilometer is dat in het echt?
    - **Antwoord:** 8  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9000 → Dat zijn meters. Een kilometer is 1000 meter. · 90 → Een nul te veel. 1 cm is hier 1 km.
    - **Uitleg (Claude):** 1 cm op de kaart is 200.000 cm = 2000 m = 2 km in het echt. 4 × 2 = 8 km.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.
- **Hint 2 (te schrijven):** Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg (de punten vallen ook weg): zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.
- **Ouderzin:** Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meters` (fout = antwoord × 1000) → Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.  [nieuw]
  - `tien keer te veel` (fout = antwoord × 10) → Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.  [nieuw]
  - `andere omrekening` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Op een kaart met schaal # : # is de klas # cm van de school. Hoeveel kilometer is dat in het echt?'. Nakijken of ze nog passen.
- Status: hints klaar
