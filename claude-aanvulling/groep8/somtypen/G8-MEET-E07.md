# G8-MEET-E07 — Wisselkoers, inwoners per km² en snelheid

Onze omschrijving: Wisselkoersen (schattend); bevolkingsdichtheid; km/u, m/s, prijs/m³ · in onze bank: 8 items

Claude-vragen gemapt: **7** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een [wie] legt # km af in # uur. Hoeveel kilometer per uur is dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een [wie] legt # km af in # uur. Hoeveel kilometer per uur is dat?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M23 (4) · regel: G8-P00-park-G7
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (4), deel-vergeten-bij-splitsen (4), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 4 (meest: “Per uur betekent delen door de tijd, niet keer.”)
- Voorbeelden:
  - `G8-MEET-E07-claude-bank-002` (Claude M23, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een bus legt 60 km af in 1,5 uur. Hoeveel kilometer per uur is dat?
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 90 → Per uur betekent delen door de tijd, niet keer. · 60 → Deel door 1,5 uur, niet door 1. · 58.5 → Snelheid is afstand gedeeld door tijd.
    - **Uitleg (Claude):** Snelheid is afstand per uur: 60 : 1,5 = 40 km per uur. Controle: 40 × 1,5 = 60.
  - `G8-MEET-E07-claude-bank-004` (Claude M23, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een fietser legt 50 km af in 2,5 uur. Hoeveel kilometer per uur is dat?
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 125 → Per uur betekent delen door de tijd, niet keer. · 25 → Deel door 2,5 uur, niet door 2. · 47.5 → Snelheid is afstand gedeeld door tijd.
    - **Uitleg (Claude):** Snelheid is afstand per uur: 50 : 2,5 = 20 km per uur. Controle: 20 × 2,5 = 50.

- **Hint 1 (te schrijven):** Per uur betekent: hoe ver kom je in één uur? Deel de afstand door het aantal uur.
- **Hint 2 (te schrijven):** Deel de kilometers door het aantal uur. Met een half uur is dat lastig: maak dan eerst allebei twee keer zo groot. Dan deel je door een heel getal.
- **Ouderzin:** Je kind rekent een snelheid uit: de afstand gedeeld door de tijd. Bij een half uur helpt het om eerst allebei te verdubbelen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel kilometer er in één uur gaat.  [nieuw]
  - `keer de tijd` (fout = getal1 × getal2) → Dat is de afstand keer de tijd. Per uur betekent: hoeveel kilometer in één uur? Deel de afstand door het aantal uur.  [nieuw]
  - `tijd eraf` (fout = getal1 - getal2 of getal2 - getal1) → Dat is de afstand min de tijd. Snelheid is de afstand gedeeld door de tijd: hoeveel kilometer in één uur?  [nieuw]
  - `alleen hele uren` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dan deel je alleen door de hele uren. Het halve uur hoort er ook bij: deel door de hele tijd, met het halve uur erbij.  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel de kilometers door het aantal uur. Kijk of het klopt: je antwoord keer het aantal uur moet de afstand geven.  [nieuw]
- Status: hints klaar

## Somtype 2: Een auto rijdt # uur met # km per uur. Hoeveel kilometer is dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een auto rijdt # uur met # km per uur. Hoeveel kilometer is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M23 (1) · regel: G8-P00-park-G7
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het halve uur telt ook mee: nog een halve keer de snelheid erbij.”)
- Voorbeelden:
  - `G8-MEET-E07-claude-bank-005` (Claude M23, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een auto rijdt 1,5 uur met 90 km per uur. Hoeveel kilometer is dat?
    - **Antwoord:** 135  (controle: n.v.t.)
    - **Fout-hints (Claude):** 90 → Het halve uur telt ook mee: nog een halve keer de snelheid erbij. · 91.5 → Elk uur komt er 90 km bij. Dat is keer.
    - **Uitleg (Claude):** Per uur 90 km. In 1,5 uur: 90 × 1,5 = 135 km. (Half uur is de helft: 45 km.)

- **Hint 1 (te schrijven):** Elk uur kom je zo ver als de snelheid. Doe de snelheid keer het aantal uur.
- **Hint 2 (te schrijven):** Reken eerst de hele uren: de snelheid keer het aantal hele uren. Een half uur is de helft van de snelheid. Tel die twee bij elkaar op.
- **Ouderzin:** Je kind rekent een afstand uit: de snelheid keer de tijd. Een half uur is de helft van de snelheid.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel kilometer het in die hele tijd is.  [nieuw]
  - `tijd erbij` (fout = getal1 + getal2) → Dat is de tijd plus de snelheid. Elk uur komt de snelheid erbij: doe de snelheid keer het aantal uur.  [nieuw]
  - `alleen hele uren` (Claudes sleutel: deel-vergeten-bij-splitsen) → Daar zitten alleen de hele uren in. Het halve uur moet er ook nog bij: dat is de helft van de snelheid.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe de snelheid keer het aantal uur. Een half uur is de helft van de snelheid.  [nieuw]
- Status: hints klaar

## Somtype 3: [wie] legt # km af in # uur. Hoeveel kilometer per uur is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[wie] legt # km af in # uur. Hoeveel kilometer per uur is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M23 (1) · regel: G8-P00-park-G7
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): omgekeerd-gedeeld (1), deel-vergeten-bij-splitsen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 3 (meest: “Per uur betekent delen door de tijd, niet keer.”)
- Voorbeelden:
  - `G8-MEET-E07-claude-bank-006` (Claude M23, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een kind legt 30 km af in 1,5 uur. Hoeveel kilometer per uur is dat?
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 45 → Per uur betekent delen door de tijd, niet keer. · 30 → Deel door 1,5 uur, niet door 1. · 28.5 → Snelheid is afstand gedeeld door tijd.
    - **Uitleg (Claude):** Snelheid is afstand per uur: 30 : 1,5 = 20 km per uur. Controle: 20 × 1,5 = 30.

- **Hint 1 (te schrijven):** Per uur betekent: hoe ver kom je in één uur? Deel de afstand door het aantal uur.
- **Hint 2 (te schrijven):** Deel de kilometers door het aantal uur. Met een half uur is dat lastig: maak dan eerst allebei twee keer zo groot. Dan deel je door een heel getal.
- **Ouderzin:** Je kind rekent een snelheid uit: de afstand gedeeld door de tijd. Bij een half uur helpt het om eerst allebei te verdubbelen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel kilometer er in één uur gaat.  [nieuw]
  - `keer de tijd` (fout = getal1 × getal2) → Dat is de afstand keer de tijd. Per uur betekent: hoeveel kilometer in één uur? Deel de afstand door het aantal uur.  [nieuw]
  - `tijd eraf` (fout = getal1 - getal2 of getal2 - getal1) → Dat is de afstand min de tijd. Snelheid is de afstand gedeeld door de tijd: hoeveel kilometer in één uur?  [nieuw]
  - `alleen hele uren` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dan deel je alleen door de hele uren. Het halve uur hoort er ook bij: deel door de hele tijd, met het halve uur erbij.  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel de kilometers door het aantal uur. Kijk of het klopt: je antwoord keer het aantal uur moet de afstand geven.  [nieuw]
- Status: hints klaar

## Somtype 4: [wie] reist # uur met de trein. De trein rijdt # km per uur. Hoeveel kilometer is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[wie] reist # uur met # km per uur. Hoeveel kilometer is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M23 (1) · regel: G8-P00-park-G7
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het halve uur telt ook mee: nog een halve keer de snelheid erbij.”)
- Voorbeelden:
  - `G8-MEET-E07-claude-bank-007` (Claude M23, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kind reist 2,5 uur met de trein. De trein rijdt 80 km per uur. Hoeveel kilometer is dat?
    - **Antwoord:** 200  (controle: n.v.t.)
    - **Fout-hints (Claude):** 160 → Het halve uur telt ook mee: nog een halve keer de snelheid erbij. · 82.5 → Elk uur komt er 80 km bij. Dat is keer.
    - **Uitleg (Claude):** Per uur 80 km. In 2,5 uur: 80 × 2,5 = 200 km. (Half uur is de helft: 40 km.)

- **Hint 1 (te schrijven):** Elk uur kom je zo ver als de snelheid. Doe de snelheid keer het aantal uur.
- **Hint 2 (te schrijven):** Reken eerst de hele uren: de snelheid keer het aantal hele uren. Een half uur is de helft van de snelheid. Tel die twee bij elkaar op.
- **Ouderzin:** Je kind rekent een afstand uit: de snelheid keer de tijd. Een half uur is de helft van de snelheid.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt hoeveel kilometer het in die hele tijd is.  [nieuw]
  - `tijd erbij` (fout = getal1 + getal2) → Dat is de tijd plus de snelheid. Elk uur komt de snelheid erbij: doe de snelheid keer het aantal uur.  [nieuw]
  - `alleen hele uren` (Claudes sleutel: deel-vergeten-bij-splitsen) → Daar zitten alleen de hele uren in. Het halve uur moet er ook nog bij: dat is de helft van de snelheid.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe de snelheid keer het aantal uur. Een half uur is de helft van de snelheid.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] reist # uur met # km per uur. Hoeveel kilometer is dat?'. Nakijken of ze nog passen.
- Status: hints klaar
