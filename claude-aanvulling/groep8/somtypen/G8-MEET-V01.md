# G8-MEET-V01 — Maten, tijd en temperatuur herhalen

Onze omschrijving: Metriek lengte/opp./inhoud/gewicht; tijd; temperatuur (eind G7) · in onze bank: 8 items

Claude-vragen gemapt: **155** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [bouwsel] Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[bouwsel] Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt?” (koppeling: claudeId)
- Items: **151** · Claude-doelen: K8 (151) · regel: D8-BALK-INHOUD-V01, D8-BALK-DUBBEL-NIEUWE-MATEN
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 13 (meest: “Je telde de drie maten op. Het bouwwerk is vol. Reken eerst uit hoeveel blokjes er in één laag liggen, en dan voor alle lagen samen.”)
- Voorbeelden:
  - `G8-MEET-V01-claude-bank-026` (Claude K8, bank, niveau 1 → basis)
    - **Opgave:** Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt?
    - **Tekening:** `{"diep": 3, "hoog": 5, "breed": 2, "soort": "bouwsel"}`
    - **Opties:** A) 36 · B) 31 · C) 30
    - **Antwoord:** 30  (controle: n.v.t.)
    - **Fout-hints (Claude):** 24 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 31 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G8-MEET-V01-claude-bank-045` (Claude K8, bank, niveau 1 → basis)
    - **Opgave:** Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt?
    - **Tekening:** `{"diep": 6, "hoog": 4, "breed": 5, "soort": "bouwsel"}`
    - **Opties:** A) 60 · B) 150 · C) 120
    - **Antwoord:** 120  (controle: n.v.t.)
    - **Fout-hints (Claude):** 60 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 150 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Het bouwwerk is helemaal vol, ook binnenin. Tel eerst hoeveel blokjes er in één laag liggen.
- **Hint 2 (te schrijven):** Tel in één laag de blokjes langs de voorkant en langs de zijkant, en doe die keer elkaar. Tel daarna hoeveel lagen er op elkaar liggen. Doe één laag keer het aantal lagen.
- **Ouderzin:** Je kind rekent uit hoeveel blokjes er in een vol bouwwerk zitten: de blokjes in één laag keer het aantal lagen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `route van Claude` (Claudes sleutels (alle): bouwwerk) → Dat zijn de drie maten bij elkaar opgeteld. Het bouwwerk is vol. Reken uit hoeveel blokjes er in één laag liggen, en dan in alle lagen samen. / Dat is de helft van alle blokjes. Reken eerst één laag uit en doe dat dan keer het aantal lagen. / Dat is een laag te veel. Tel nog eens hoeveel lagen er op elkaar liggen. / Dat zijn de blokjes van drie kanten samen: voorkant, zijkant en bovenkant. Het bouwwerk is vol, dus er zitten ook blokjes binnenin. / Dat is één laag. Er liggen meer lagen op elkaar: doe één laag keer het aantal lagen. / Reken eerst uit hoeveel blokjes er in één laag liggen. Doe dat daarna keer het aantal lagen. / Dat is een laag te weinig. Tel nog eens hoeveel lagen er op elkaar liggen. / Dat is een rij blokjes te weinig. Kijk nog eens hoe breed en hoe diep het bouwwerk is.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst uit hoeveel blokjes er in één laag liggen. Doe dat daarna keer het aantal lagen.  [nieuw]
- Status: hints klaar

## Somtype 2: Een weiland is # hectare. Hoeveel m² is dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een weiland is # [ding]. Hoeveel m² is dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: M25 (3) · regel: G8-M25-hectare
- Getallenruimte: 0–100.000, kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (6)
- Verschillende Claude-fout-hints: 2 (meest: “Een hectare is 100 × 100 meter. Reken dat uit.”)
- Voorbeelden:
  - `G8-MEET-V01-claude-bank-001` (Claude M25, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een weiland is 2 hectare. Hoeveel m² is dat?
    - **Antwoord:** 20.000  (controle: ok)
    - **Fout-hints (Claude):** 2000 → Een hectare is 100 × 100 meter. Reken dat uit. · 200 → Een hectare is 100 × 100 = 10.000 m².
    - **Uitleg (Claude):** 1 hectare = 10.000 m² (100 bij 100 meter). 2 × 10.000 = 20.000 m².
  - `G8-MEET-V01-claude-bank-002` (Claude M25, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een weiland is 4,5 hectare. Hoeveel m² is dat?
    - **Antwoord:** 45.000  (controle: ok)
    - **Fout-hints (Claude):** 4500 → Een hectare is 100 × 100 meter. Reken dat uit. · 450 → Een hectare is 100 × 100 = 10.000 m².
    - **Uitleg (Claude):** 1 hectare = 10.000 m² (100 bij 100 meter). 4,5 × 10.000 = 45.000 m².

- **Hint 1 (te schrijven):** Eén hectare is een vierkant van honderd meter lang en honderd meter breed.
- **Hint 2 (te schrijven):** Reken uit hoeveel vierkante meter één hectare is: honderd keer honderd. Doe dat keer het aantal hectare. Bij een kommagetal schuift de komma mee.
- **Ouderzin:** Je kind rekent hectare om naar vierkante meter: één hectare is honderd keer honderd vierkante meter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat is het aantal hectare. De vraag wil vierkante meters: hoeveel vierkante meter is één hectare?  [nieuw]
  - `nul te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Eén hectare is honderd keer honderd vierkante meter. Tel de nullen nog eens.  [nieuw]
  - `honderd keer te weinig` (fout = antwoord : 100) → Dat is honderd keer te weinig. Eén hectare is niet honderd vierkante meter, maar honderd keer honderd.  [nieuw]
  - `andere fout` (andere fout) → Eén hectare is honderd keer honderd vierkante meter. Doe dat keer het aantal hectare.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een weiland is # [ding]. Hoeveel m² is dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: Een pak met # liter drinken wordt verdeeld over [bakken] van # milliliter. Hoeveel volle bekers krijg je?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een pak met # liter drinken wordt verdeeld over [bakken] van # [ding]. Hoeveel volle bekers krijg je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-MEET
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken de liters eerst om naar milliliter en deel daarna pas.”)
- Voorbeelden:
  - `G8-MEET-V01-claude-bank-004` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Een pak met 1,5 liter drinken wordt verdeeld over bekers van 250 milliliter. Hoeveel volle bekers krijg je?
    - **Opties:** A) 6 bekers · B) 4 bekers · C) 15 bekers
    - **Antwoord:** 6 bekers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 bekers → Reken de liters eerst om naar milliliter en deel daarna pas. · 15 bekers → Kijk goed naar het aantal nullen bij het omrekenen van liter naar milliliter.
    - **Uitleg (Claude):** 1,5 liter is 1500 milliliter. Je deelt 1500 door 250. Dat is 6, dus je krijgt 6 volle bekers.

- **Hint 1 (te schrijven):** Reken eerst om, zodat het pak en een beker in dezelfde maat staan.
- **Hint 2 (te schrijven):** Eén liter is duizend milliliter. Reken het pak om naar milliliter. Deel dat door het aantal milliliter van één beker.
- **Ouderzin:** Je kind rekent liters om naar milliliters (keer duizend) en deelt dan door wat er in één beker gaat.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één liter` (4 bekers) → Zo vul je alleen één liter. Het pak is meer dan één liter: reken het hele pak om naar milliliter.  [nieuw]
  - `nullen` (15 bekers) → Tel de nullen nog eens na, bij het omrekenen én bij het delen. Eén liter is duizend milliliter.  [nieuw]
  - `andere fout` (andere fout) → Reken het pak om naar milliliter en deel door wat er in één beker gaat.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een pak met # liter drinken wordt verdeeld over [bakken] van # [ding]. Hoeveel volle bekers krijg je?'. Nakijken of ze nog passen.
- Status: hints klaar
