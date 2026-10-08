# G7-VERH-03 — Verhoudingen en schaalrekenen

Onze omschrijving: Verhoudingen + schaal · in onze bank: 8 items

Claude-vragen gemapt: **642** in **25** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Vul in. # : # = # : ?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Vul in. # : # = # : ?” (koppeling: claudeId)
- Items: **331** · Claude-doelen: V2 (331) · regel: G7-V02-verhouding-ab
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verhoudingstabel-verkeerd (414), grafiek-verkeerd-afgelezen (116), getal-overgenomen (102), verkeerde-bewerking (28)
- Verschillende Claude-fout-hints: 2 (meest: “Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-623` (Claude V2, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 11 : 10 = 33 : ?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G7-VERH-03-claude-bank-401` (Claude V2, bank, niveau 3 → toepassen)
    - **Opgave:** Vul in. 6 : 10 = 24 : ?
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 10 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** De dubbele punt (:) staat hier voor een verhouding. Links en rechts van het isteken (=) horen de getallen op dezelfde manier bij elkaar.
- **Hint 2 (te schrijven):** Vergelijk de getallen vóór de dubbele punt: hoeveel keer zo groot is het getal in de verhouding met het vraagteken? Doe het getal achter de dubbele punt in de verhouding zonder vraagteken evenveel keer.
- **Ouderzin:** Je kind vult een verhouding aan (met een dubbele punt): wat je met het ene getal doet, doe je ook met het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt het getal op de plek van het vraagteken.  [nieuw]
  - `één keer te veel` (fout = antwoord + getal2) → Is dat één keer te veel? Of heb je het verschil erbij opgeteld? Hoeveel keer zo groot wordt het getal vóór de dubbele punt? Doe het getal achter de dubbele punt precies zoveel keer.  [nieuw]
  - `één keer te weinig` (fout = antwoord - getal2) → Is dat één keer te weinig? Of heb je het verschil erbij opgeteld? Hoeveel keer zo groot wordt het getal vóór de dubbele punt? Doe het getal achter de dubbele punt precies zoveel keer.  [nieuw]
  - `gedeeld in plaats van keer` (Claudes sleutel: verkeerde-bewerking) → Heb je gedeeld? Rechts van het isteken is het getal vóór de dubbele punt groter. Dan wordt het getal achter de dubbele punt ook groter: doe keer.  [Claude, taalfix]
  - `verschil van twee getallen` (fout = getal1 - getal2 of getal2 - getal1) → Heb je twee getallen uit de vraag van elkaar afgehaald, of bij elkaar opgeteld? Hoeveel keer zo groot wordt het getal vóór de dubbele punt? Doe het getal achter de dubbele punt precies zoveel keer.  [nieuw]
  - `verschil opgeteld of keer elkaar` (Claudes sleutel: verhoudingstabel-verkeerd) → Heb je het verschil erbij opgeteld, of twee getallen uit de vraag keer elkaar gedaan? Vergelijk de getallen vóór de dubbele punt: hoeveel keer zo groot wordt het? Doe het getal achter de dubbele punt precies zoveel keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Vergelijk de getallen vóór de dubbele punt, en doe het getal erachter evenveel keer.  [nieuw]
- Status: hints klaar

## Somtype 2: # [ding] kosten €#. Hoeveel kosten # [ding]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# [ding] kosten €#. Hoeveel kosten # [ding]?” (koppeling: claudeId)
- Items: **264** · Claude-doelen: V2 (264) · regel: G7-V03-verhoudingstabel
- Getallenruimte: kommagetallen (2 cijfers achter de komma) met € · type: kale
- Denkfouten (Claude): verhoudingstabel-verkeerd (345), getal-overgenomen (101), andere-deel-genomen (82)
- Verschillende Claude-fout-hints: 1 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-038` (Claude V2, bank, niveau 3 → toepassen)
    - **Opgave:** 4 schriften kosten €6. Hoeveel kosten 18 schriften?
    - **Antwoord:** €27  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G7-VERH-03-claude-bank-001` (Claude V2, bank, niveau 3 → toepassen)
    - **Opgave:** 6 pennen kosten €3. Hoeveel kosten 11 pennen?
    - **Antwoord:** €5,50  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Het euroteken (€) betekent euro. Elk stuk kost evenveel: meer stuks kosten meer, minder stuks kosten minder.
- **Hint 2 (te schrijven):** Reken eerst uit wat één kost: deel de prijs door het aantal dat bij die prijs hoort. Doe dat bedrag daarna keer het aantal waar de vraag naar vraagt.
- **Ouderzin:** Je kind rekent met een verhouding uit wat een ander aantal kost, via de prijs van één.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `prijs uit de vraag` (fout = getal2) → Dat is de prijs uit de vraag. Die hoort bij een ander aantal. Wat kost één?  [nieuw]
  - `prijs van één` (Claudes sleutel: andere-deel-genomen) → Dat is de prijs van één. Hoeveel kosten er zoveel als de vraag vraagt?  [Claude, taalfix]
  - `stuk te veel of verschil erbij` (Claudes sleutel: verhoudingstabel-verkeerd) → Heb je één stuk te veel of te weinig betaald? Of heb je het verschil in aantal bij de prijs opgeteld of ervan afgehaald? Reken uit wat één kost, en doe dat keer het aantal waar de vraag naar vraagt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit wat één kost, en doe dat keer het aantal waar de vraag naar vraagt.  [nieuw]
- Status: hints klaar

## Somtype 3: Een tekening van # cm breed wordt # keer zo klein gemaakt. Hoe breed wordt de kleine tekening?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een tekening van # cm breed wordt # keer zo klein gemaakt. Hoe breed wordt de kleine tekening?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: K11 (9) · regel: G7-V12-vergroten
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (18)
- Verschillende Claude-fout-hints: 2 (meest: “Zoveel keer zo klein betekent delen door dat getal, niet dat getal eraf halen.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-287` (Claude K11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een tekening van 8 cm breed wordt 2 keer zo klein gemaakt. Hoe breed wordt de kleine tekening?
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 6 → Zoveel keer zo klein betekent delen door dat getal, niet dat getal eraf halen. · 16 → Verkleinen maakt kleiner. Je moet delen, niet vermenigvuldigen.
    - **Uitleg (Claude):** Verkleinen met factor 2 is delen door 2: 8 : 2 = 4 cm.
  - `G7-VERH-03-claude-bank-283` (Claude K11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een tekening van 12 cm breed wordt 4 keer zo klein gemaakt. Hoe breed wordt de kleine tekening?
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 8 → Zoveel keer zo klein betekent delen door dat getal, niet dat getal eraf halen. · 48 → Verkleinen maakt kleiner. Je moet delen, niet vermenigvuldigen.
    - **Uitleg (Claude):** Verkleinen met factor 4 is delen door 4: 12 : 4 = 3 cm.

- **Hint 1 (te schrijven):** In de vraag staat hoeveel keer zo klein de tekening wordt. Zo klein maken betekent: delen. Deel de breedte door dat aantal keer.
- **Hint 2 (te schrijven):** Deel de breedte door het aantal keer. Controleer: doe je uitkomst keer dat aantal. Krijg je de breedte terug?
- **Ouderzin:** Je kind rekent uit hoe breed een tekening wordt als hij zoveel keer zo klein wordt gemaakt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Heb je het getal eraf gehaald? Zo klein maken betekent: delen, niet eraf halen.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Dat is groter dan de tekening was. Zo klein betekent: delen, niet keer.  [nieuw]
  - `andere fout` (andere fout) → Deel de breedte door het aantal keer.  [nieuw]
- Status: hints klaar

## Somtype 4: [rooster] Een rechthoek is # hokjes breed en # hokjes hoog. Kleur een rechthoek die # keer zo groot is: elke zijde # keer zo lang.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[vak(ken) aantikken op rooster] Een rechthoek is # hokjes breed en # hokjes hoog. Kleur een rechthoek die # keer zo groot is: elke zijde # keer zo lang.” (koppeling: claudeId)
- Items: **9** · Claude-doelen: K11 (9) · regel: G7-V12-vergroten
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (9), optellen-ipv-vermenigvuldigen (8)
- Verschillende Claude-fout-hints: 3 (meest: “Allebei de zijden worden langer, ook de hoogte.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-636` (Claude K11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een rechthoek is 1 hokje breed en 2 hokjes hoog. Kleur een rechthoek die 2 keer zo groot is: elke zijde 2 keer zo lang.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** een rechthoek van 2 hokjes breed en 4 hokjes hoog  (controle: ok)
    - **Fout-hints (Claude):** een rechthoek van 3 hokjes breed en 4 hokjes hoog → 2 keer zo groot is vermenigvuldigen, niet 2 hokjes erbij. · een rechthoek van 2 hokjes breed en 2 hokjes hoog → Allebei de zijden worden langer, ook de hoogte.
    - **Uitleg (Claude):** Elke zijde wordt 2 keer zo lang: 1 × 2 = 2 breed en 2 × 2 = 4 hoog. Tik op de linkerbovenhoek en dan op de rechteronderhoek.
  - `G7-VERH-03-claude-bank-634` (Claude K11, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een rechthoek is 1 hokje breed en 1 hokje hoog. Kleur een rechthoek die 2 keer zo groot is: elke zijde 2 keer zo lang.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** een rechthoek van 2 hokjes breed en 2 hokjes hoog  (controle: ok)
    - **Fout-hints (Claude):** een rechthoek van 3 hokjes breed en 3 hokjes hoog → 2 keer zo groot is vermenigvuldigen, niet 2 hokjes erbij. · een rechthoek van 2 hokjes breed en 1 hokjes hoog → Allebei de zijden worden langer, ook de hoogte.
    - **Uitleg (Claude):** Elke zijde wordt 2 keer zo lang: 1 × 2 = 2 breed en 1 × 2 = 2 hoog. Tik op de linkerbovenhoek en dan op de rechteronderhoek.

- **Hint 1 (te schrijven):** In de vraag staat wat zo groot hier betekent: elke zijde wordt zoveel keer zo lang. Dat geldt voor de breedte én voor de hoogte.
- **Hint 2 (te schrijven):** Doe de breedte keer het aantal keer, en de hoogte ook. Kleur een rechthoek met die nieuwe breedte en die nieuwe hoogte.
- **Ouderzin:** Je kind kleurt een rechthoek waarvan elke zijde zoveel keer zo lang is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `er iets bij opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je ergens iets bij opgeteld? Elke zijde wordt keer dat getal, niet erbij.  [Claude, taalfix]
  - `hoogte niet langer` (Claudes sleutel: deel-vergeten-bij-splitsen) → Is de hoogte ook langer geworden? Elke zijde wordt zoveel keer zo lang: de breedte en de hoogte.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe de breedte en de hoogte allebei keer het aantal keer.  [nieuw]
- Status: hints klaar

## Somtype 5: Een foto is # cm breed en # cm hoog. Hij wordt # keer zo groot afgedrukt. Hoe breed wordt de foto?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Een foto is # cm breed en # cm hoog. Hij wordt # keer zo groot afgedrukt. Hoe breed wordt de foto?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: K11 (7) · regel: G7-V12-vergroten
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (7), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 2 (meest: “Zoveel keer zo groot betekent vermenigvuldigen, niet dat getal erbij optellen.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-270` (Claude K11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een foto is 5 cm breed en 5 cm hoog. Hij wordt 2 keer zo groot afgedrukt. Hoe breed wordt de foto?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 7 → Zoveel keer zo groot betekent vermenigvuldigen, niet dat getal erbij optellen. · 50 → Alleen de breedte is gevraagd: één zijde keer de factor.
    - **Uitleg (Claude):** Elke zijde wordt 2 keer zo lang: 5 × 2 = 10 cm breed (en 5 × 2 = 10 cm hoog).
  - `G7-VERH-03-claude-bank-273` (Claude K11, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een foto is 4 cm breed en 2 cm hoog. Hij wordt 4 keer zo groot afgedrukt. Hoe breed wordt de foto?
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 8 → Zoveel keer zo groot betekent vermenigvuldigen, niet dat getal erbij optellen. · 32 → Alleen de breedte is gevraagd: één zijde keer de factor.
    - **Uitleg (Claude):** Elke zijde wordt 4 keer zo lang: 4 × 4 = 16 cm breed (en 2 × 4 = 8 cm hoog).

- **Hint 1 (te schrijven):** In de vraag staat hoeveel keer zo groot het wordt. Dan wordt elke maat zoveel keer zo lang. De vraag gaat over de breedte.
- **Hint 2 (te schrijven):** Doe de breedte keer het aantal keer. De hoogte heb je voor deze vraag niet nodig.
- **Ouderzin:** Je kind rekent uit hoe breed iets wordt als het zoveel keer zo groot wordt gemaakt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je er iets bij opgeteld? Zo groot betekent: keer.  [Claude, taalfix]
  - `hoogte meegerekend` (Claudes sleutel: verkeerde-bewerking) → Heb je de hoogte ook meegerekend? De vraag gaat alleen over de breedte.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe de breedte keer het aantal keer.  [nieuw]
- Status: hints klaar

## Somtype 6: Elke zijde van een vierkant van # bij # cm wordt # keer zo lang. Hoeveel keer zo groot wordt de oppervlakte?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Een vierkant van # bij # cm wordt # keer zo groot: elke zijde wordt # keer zo lang. Hoeveel keer zo groot wordt de oppervlakte?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: K11 (3) · regel: G7-V12-vergroten
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (3), optellen-ipv-vermenigvuldigen (3)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G7-VERH-03-claude-bank-291` (Claude K11, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elke zijde van een vierkant van 5 bij 5 cm wordt 4 keer zo lang. Hoeveel keer zo groot wordt de oppervlakte?
    - **Antwoord:** 16  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 → De zijden worden zoveel keer zo lang. De oppervlakte groeit in twee richtingen tegelijk. · 8 → Twee richtingen betekent factor keer factor, niet factor plus factor.
    - **Uitleg (Claude):** De oppervlakte was 5 × 5 = 25 cm². Nu is hij 20 × 20 = 400 cm². Dat is 4 × 4 = 16 keer zo groot.
  - `G7-VERH-03-claude-bank-290` (Claude K11, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elke zijde van een vierkant van 3 bij 3 cm wordt 4 keer zo lang. Hoeveel keer zo groot wordt de oppervlakte?
    - **Antwoord:** 16  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 → De zijden worden zoveel keer zo lang. De oppervlakte groeit in twee richtingen tegelijk. · 8 → Twee richtingen betekent factor keer factor, niet factor plus factor.
    - **Uitleg (Claude):** De oppervlakte was 3 × 3 = 9 cm². Nu is hij 12 × 12 = 144 cm². Dat is 4 × 4 = 16 keer zo groot.

- **Hint 1 (te schrijven):** De oppervlakte is lengte keer breedte. Worden alle zijden langer, dan worden de lengte én de breedte langer.
- **Hint 2 (te schrijven):** Leg zoveel kleine vierkanten naast elkaar als het aantal keer dat elke zijde langer wordt. Leg evenveel rijen onder elkaar. Tel ze.
- **Ouderzin:** Je kind ontdekt dat de oppervlakte van een vierkant sneller groeit dan de zijden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen de zijde` (Claudes sleutel: omtrek-oppervlakte-verwisseld) → Dat is hoeveel keer zo lang elke zijde wordt. De oppervlakte groeit meer: de lengte én de breedte worden langer.  [Claude, taalfix]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je opgeteld? De lengte en de breedte worden allebei zoveel keer zo lang. Hoeveel kleine vierkanten passen er dan in het grote?  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel kleine vierkanten passen er in het grote vierkant?  [nieuw]
- Status: hints klaar

## Somtype 7: Een [ding] is # m lang. Je tekent de tuin op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe lang wordt de tuin op de tekening?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een [ding] is # m lang. Je tekent de tuin op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe lang wordt de tuin op de tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken eerst 8 m om naar cm en deel dan door 100.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-265` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een tuin is 8 m lang. Je tekent de tuin op schaal 1 : 100. Dat betekent: 1 cm op de tekening is 100 cm in het echt. Hoe lang wordt de tuin op de tekening?
    - **Opties:** A) 80 cm · B) 8 m · C) 8 cm
    - **Antwoord:** 8 cm  (controle: ok)
    - **Fout-hints (Claude):** 80 cm → Reken eerst 8 m om naar cm en deel dan door 100. · 8 m → Je hebt de echte maat overgenomen. Op de tekening past die lengte niet op papier.
    - **Uitleg (Claude):** 8 m is 800 cm. Op schaal 1 : 100 deel je door 100: 800 : 100 = 8. De tuin wordt dus 8 cm op de tekening.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te lang` (80 cm) → Dat is tien keer te lang. Maak van de echte maat eerst centimeters, en deel dan door het getal achter de dubbele punt.  [nieuw]
  - `de echte maat` (8 m) → Dat is de echte maat. Op de tekening of in het model is alles kleiner dan in het echt.  [nieuw]
  - `andere fout` (andere fout) → Maak van de echte maat centimeters, en deel door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 8: Een [ding] is # m lang. Op een plattegrond met schaal # : # wordt het pad getekend. Hoe lang is het pad op de plattegrond?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een [ding] is # m lang. Op een plattegrond met schaal # : # wordt het pad getekend. Hoe lang is het pad op de plattegrond?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken de 60 m eerst om naar cm en deel dat getal daarna door 1000.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-266` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een fietspad is 60 m lang. Op een plattegrond met schaal 1 : 1000 wordt het pad getekend. Hoe lang is het pad op de plattegrond?
    - **Opties:** A) 60 cm · B) 600 cm · C) 6 cm
    - **Antwoord:** 6 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 60 cm → Reken de 60 m eerst om naar cm en deel dat getal daarna door 1000. · 600 cm → Let goed op het aantal nullen bij het delen door 1000.
    - **Uitleg (Claude):** 60 m is 6000 cm. Op schaal 1 : 1000 deel je door 1000: 6000 : 1000 = 6. Op de plattegrond is het pad 6 cm.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te lang` (60 cm) → Dat is tien keer te lang. Maak van de echte maat eerst centimeters, en deel dan door het getal achter de dubbele punt.  [nieuw]
  - `honderd keer te lang` (600 cm) → Dat is honderd keer te lang. Maak eerst van de meters centimeters, en deel dan door het getal achter de dubbele punt.  [nieuw]
  - `andere fout` (andere fout) → Maak van de echte maat centimeters, en deel door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 9: Een bank is in het echt # cm lang. Op een tekening met schaal # : # wordt de bank getekend. Hoe lang wordt hij?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een bank is in het echt # cm lang. Op een tekening met schaal # : # wordt de bank getekend. Hoe lang wordt hij?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): tiental-ernaast (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt door 10 gedeeld. Lees het tweede getal van de schaal nog eens.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-267` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Een bank is in het echt 300 cm lang. Op een tekening met schaal 1 : 100 wordt de bank getekend. Hoe lang wordt hij?
    - **Opties:** A) 3 cm · B) 30 cm · C) 400 cm
    - **Antwoord:** 3 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 cm → Je hebt door 10 gedeeld. Lees het tweede getal van de schaal nog eens. · 400 cm → Je hebt 100 erbij geteld. Bij schaal reken je met keer of gedeeld door.
    - **Uitleg (Claude):** Op de tekening is alles 100 keer kleiner. Je rekent 300 : 100 = 3. De bank wordt dus 3 cm op de tekening.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te lang` (30 cm) → Dat is tien keer te lang. Deel de echte maat door het getal achter de dubbele punt.  [nieuw]
  - `opgeteld` (400 cm) → Heb je de echte maat en het getal achter de dubbele punt opgeteld? Op de tekening wordt het kleiner: hoe vaak past het getal achter de dubbele punt in de echte maat?  [nieuw]
  - `andere fout` (andere fout) → Deel de echte maat door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 10: Een echte boot is # m lang. Je maakt een model op schaal # : #. Dat betekent: # cm in het model is # cm in het echt. Hoe lang wordt het model?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Een echte boot is # m lang. Je maakt een model op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe lang wordt het model?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt met 20 vermenigvuldigd. Maar het model moet kleiner worden dan de echte boot.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-268` (Claude M19, ai, niveau 3 → toepassen)
    - **Opgave:** Een echte boot is 6 m lang. Je maakt een model op schaal 1 : 20. Dat betekent: 1 cm in het model is 20 cm in het echt. Hoe lang wordt het model?
    - **Opties:** A) 30 cm · B) 120 cm · C) 60 cm
    - **Antwoord:** 30 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 120 cm → Je hebt met 20 vermenigvuldigd. Maar het model moet kleiner worden dan de echte boot. · 60 cm → Je hebt door 10 gedeeld. Kijk nog eens naar het tweede getal van de schaal.
    - **Uitleg (Claude):** 6 m is 600 cm. Op schaal 1 : 20 deel je door 20: 600 : 20 = 30. Het model wordt dus 30 cm lang.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer gedaan` (120 cm) → Heb je keer gedaan? Het model is kleiner dan echt: deel door het getal achter de dubbele punt.  [nieuw]
  - `door een ander getal gedeeld` (60 cm) → Heb je door een ander getal gedeeld? Deel de echte maat in centimeters door het getal achter de dubbele punt.  [nieuw]
  - `andere fout` (andere fout) → Maak van de echte maat centimeters, en deel door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 11: Een muur is in het echt # cm lang. Je tekent hem op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe lang wordt de muur op je tekening?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een muur is in het echt # cm lang. Je tekent hem op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe lang wordt de muur op je tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): tiental-ernaast (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt door 10 gedeeld. Kijk nog eens naar het tweede getal van de schaal.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-276` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een muur is in het echt 500 cm lang. Je tekent hem op schaal 1 : 100. Dat betekent: 1 cm op de tekening is 100 cm in het echt. Hoe lang wordt de muur op je tekening?
    - **Opties:** A) 5 cm · B) 50 cm · C) 500 cm
    - **Antwoord:** 5 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 50 cm → Je hebt door 10 gedeeld. Kijk nog eens naar het tweede getal van de schaal. · 500 cm → Dit is de echte lengte. Op een tekening met schaal wordt alles juist kleiner.
    - **Uitleg (Claude):** Op de tekening is alles 100 keer kleiner. Je rekent 500 : 100 = 5. De muur wordt dus 5 cm op je tekening.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te lang` (50 cm) → Dat is tien keer te lang. Deel de echte maat door het getal achter de dubbele punt.  [nieuw]
  - `de echte maat` (500 cm) → Dat is de echte maat. Op de tekening of in het model is alles kleiner dan in het echt.  [nieuw]
  - `andere fout` (andere fout) → Deel de echte maat door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 12: Een poppenhuis is gemaakt op schaal # : #. Dat betekent: # cm in het model is # cm in het echt. Een echte stoel is # cm hoog. Hoe hoog is de stoel in het poppenhuis?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een poppenhuis is gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Een echte stoel is # cm hoog. Hoe hoog is de stoel in het poppenhuis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt vermenigvuldigd. In een poppenhuis is alles juist kleiner dan echt.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-277` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een poppenhuis is gemaakt op schaal 1 : 10. Dat betekent: 1 cm in het model is 10 cm in het echt. Een echte stoel is 90 cm hoog. Hoe hoog is de stoel in het poppenhuis?
    - **Opties:** A) 900 cm · B) 90 cm · C) 9 cm
    - **Antwoord:** 9 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 900 cm → Je hebt vermenigvuldigd. In een poppenhuis is alles juist kleiner dan echt. · 90 cm → Dit is de echte hoogte. Die moet je nog verkleinen met de schaal.
    - **Uitleg (Claude):** In het poppenhuis is alles 10 keer kleiner. Je rekent 90 : 10 = 9. De stoel is dus 9 cm hoog.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer gedaan` (900 cm) → Heb je keer gedaan? In het model is alles kleiner dan echt: deel door het getal achter de dubbele punt.  [nieuw]
  - `de echte maat` (90 cm) → Dat is de echte maat. Op de tekening of in het model is alles kleiner dan in het echt.  [nieuw]
  - `andere fout` (andere fout) → Deel de echte maat door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 13: Een speelgoedauto is gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. De auto is # cm lang. Hoe lang is de echte auto?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Een speelgoedauto is gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. De auto is # cm lang. Hoe lang is de echte auto?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt gedeeld, maar het echte voorwerp is groter dan het speelgoed.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-278` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een speelgoedauto is gemaakt op schaal 1 : 10. Dat betekent: 1 cm op de tekening is 10 cm in het echt. De auto is 40 cm lang. Hoe lang is de echte auto?
    - **Opties:** A) 400 cm · B) 4 cm · C) 4000 cm
    - **Antwoord:** 400 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 cm → Je hebt gedeeld, maar het echte voorwerp is groter dan het speelgoed. · 4000 cm → Je hebt met 100 gerekend. Kijk nog eens naar het tweede getal van de schaal.
    - **Uitleg (Claude):** Bij schaal 1 : 10 is het echte voorwerp 10 keer zo groot. Je rekent 40 × 10 = 400. De echte auto is 400 cm lang.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Doe de maat op de tekening keer het getal achter de dubbele punt. Zoveel centimeter is het in het echt.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gedeeld` (4 cm) → Heb je gedeeld? Het echte voorwerp is groter dan het model: doe keer het getal achter de dubbele punt.  [nieuw]
  - `tien keer te veel` (4000 cm) → Dat is tien keer te lang. Doe de maat van het model keer het getal achter de dubbele punt.  [nieuw]
  - `andere fout` (andere fout) → Doe de maat van het model keer het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 14: Een tekening heeft schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe groot is het echte voorwerp vergeleken met de tekening?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Een tekening heeft schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoe groot is het echte voorwerp vergeleken met de tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het eerste getal hoort bij de tekening en het tweede bij het echte voorwerp. Welke van de twee is dan groter?”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-279` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Een tekening heeft schaal 1 : 2. Dat betekent: 1 cm op de tekening is 2 cm in het echt. Hoe groot is het echte voorwerp vergeleken met de tekening?
    - **Opties:** A) 2 cm groter · B) 2 keer zo groot · C) 2 keer zo klein
    - **Antwoord:** 2 keer zo groot  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2 keer zo klein → Het eerste getal hoort bij de tekening en het tweede bij het echte voorwerp. Welke van de twee is dan groter? · 2 cm groter → Bij schaal gaat het niet om erbij of eraf, maar om hoeveel keer.
    - **Uitleg (Claude):** Bij 1 : 2 hoort bij 1 cm op de tekening 2 cm in het echt. Het echte voorwerp is dus 2 keer zo groot. De tekening is de kleine versie.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Lees wat één centimeter op de tekening in het echt is. Gaat het om erbij of om keer? En is het echte voorwerp groter of kleiner dan de tekening?
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij in plaats van keer` (2 cm groter) → Bij een schaal is alles in het echt hetzelfde aantal keer zo groot als op de tekening. Hoeveel keer zo groot is het echte voorwerp?  [nieuw]
  - `omgekeerd vergeleken` (2 keer zo klein) → Is het echte voorwerp kleiner dan de tekening? Eén centimeter op de tekening is in het echt meer centimeters.  [nieuw]
  - `andere fout` (andere fout) → Lees wat één centimeter op de tekening in het echt is.  [nieuw]
- Status: hints klaar

## Somtype 15: Een tekening van een fiets heeft schaal # : #. Hoeveel cm is # cm op de tekening in het echt?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Een tekening van een fiets heeft schaal # : #. Hoeveel cm is # cm op de tekening in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): tiental-ernaast (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Lees het tweede getal van de schaal nog eens precies. Hoeveel nullen staan er?”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-289` (Claude M19, ai, niveau 1 → basis)
    - **Opgave:** Een tekening van een fiets heeft schaal 1 : 50. Hoeveel cm is 1 cm op de tekening in het echt?
    - **Opties:** A) 5 cm · B) 51 cm · C) 50 cm
    - **Antwoord:** 50 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 cm → Lees het tweede getal van de schaal nog eens precies. Hoeveel nullen staan er? · 51 cm → Bij schaal tel je niets op. Het tweede getal vertelt hoeveel keer groter het echte is.
    - **Uitleg (Claude):** Het tweede getal van de schaal zegt hoeveel keer groter het echte voorwerp is. Bij 1 : 50 hoort bij 1 cm op de tekening 50 cm echt. Je vermenigvuldigt dus met 50.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Bij een schaal hoort het getal van de tekening bij één centimeter. Zoek het andere getal: zoveel centimeter is het in het echt.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te weinig` (5 cm) → Dat is tien keer te weinig. Kijk welk getal van de schaal bij het echte voorwerp hoort.  [nieuw]
  - `opgeteld` (51 cm) → Heb je de twee getallen van de schaal opgeteld? Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.  [nieuw]
  - `andere fout` (andere fout) → Kijk welk getal van de schaal bij het echte voorwerp hoort.  [nieuw]
- Status: hints klaar

## Somtype 16: In een tabel staat schaal # : #. Bij # cm op de tekening hoort # cm echt. Wat hoort er bij # cm op de tekening?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “In een tabel staat schaal # : #. Bij # cm op de tekening hoort # cm echt. Wat hoort er bij # cm op de tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “In de tabel gaat de tekening van 1 naar 2 cm, dus keer 2. Doe met het andere getal precies hetzelfde.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-293` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** In een tabel staat schaal 1 : 100. Bij 1 cm op de tekening hoort 100 cm echt. Wat hoort er bij 2 cm op de tekening?
    - **Opties:** A) 200 cm echt · B) 101 cm echt · C) 50 cm echt
    - **Antwoord:** 200 cm echt  (controle: n.v.t.)
    - **Fout-hints (Claude):** 101 cm echt → In de tabel gaat de tekening van 1 naar 2 cm, dus keer 2. Doe met het andere getal precies hetzelfde. · 50 cm echt → Je hebt gehalveerd. Maar de tekening werd juist langer, dus het echte wordt ook langer.
    - **Uitleg (Claude):** Van 1 cm naar 2 cm op de tekening is keer 2. Dan doe je met de echte maat hetzelfde: 100 × 2 = 200. Dus bij 2 cm hoort 200 cm echt.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak een verhoudingstabel: hoeveel keer zoveel centimeter is het nu op de tekening? Doe het getal voor in het echt evenveel keer.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (101 cm echt) → Heb je er maar één bij opgeteld? Komt er op de tekening een centimeter bij, dan komt er in het echt het hele getal achter de dubbele punt bij.  [nieuw]
  - `gedeeld` (50 cm echt) → Heb je gedeeld? Meer centimeters op de tekening horen bij meer centimeters in het echt.  [nieuw]
  - `andere fout` (andere fout) → Op de tekening en in het echt doe je keer hetzelfde getal.  [nieuw]
- Status: hints klaar

## Somtype 17: Je tekent dezelfde boom twee keer: een keer op schaal # : # en een keer op schaal # : #. Welke tekening wordt het grootst?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Je tekent dezelfde boom twee keer: een keer op schaal # : # en een keer op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Welke tekening wordt het grootst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij 1 : 100 wordt de boom 100 keer kleiner gemaakt. Is dat veel of weinig verkleinen?”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-294` (Claude M19, ai, niveau 3 → toepassen)
    - **Opgave:** Je tekent dezelfde boom twee keer: een keer op schaal 1 : 10 en een keer op schaal 1 : 100. Welke tekening wordt het grootst?
    - **Opties:** A) De tekening op schaal 1 : 100 · B) Beide tekeningen zijn even groot · C) De tekening op schaal 1 : 10
    - **Antwoord:** De tekening op schaal 1 : 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** De tekening op schaal 1 : 100 → Bij 1 : 100 wordt de boom 100 keer kleiner gemaakt. Is dat veel of weinig verkleinen? · Beide tekeningen zijn even groot → De schalen zijn niet hetzelfde, dus verklein je ook niet evenveel.
    - **Uitleg (Claude):** Bij 1 : 10 maak je de boom 10 keer kleiner, bij 1 : 100 maak je hem 100 keer kleiner. Hoe groter het tweede getal, hoe kleiner de tekening. Dus 1 : 10 geeft de grootste tekening.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Hoe groter het getal achter de dubbele punt, hoe meer centimeter in het echt bij één centimeter op de tekening hoort.
- **Hint 2 (te schrijven):** Stel: het echte voorwerp is tweeduizend centimeter. Reken voor elke schaal uit hoe lang het op de tekening wordt. Welke tekening is groter?
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere schaal gekozen` (De tekening op schaal 1 : 100) → Bij die schaal hoort bij één centimeter op de tekening juist meer in het echt. Wordt de tekening dan groter of kleiner?  [nieuw]
  - `even groot` (Beide tekeningen zijn even groot) → Het is hetzelfde voorwerp, maar de schalen zijn verschillend. Dan worden de tekeningen ook verschillend groot.  [nieuw]
  - `andere fout` (andere fout) → Reken voor elke schaal uit hoe lang de tekening wordt.  [nieuw]
- Status: hints klaar

## Somtype 18: Marit tekent een boom op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Sem tekent dezelfde boom op schaal # : #. Wie krijgt de kleinste tekening?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Marit tekent een boom op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Sem tekent dezelfde boom op schaal # : #. Wie krijgt de kleinste tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verkeerde-bewerking (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij 1 : 25 verklein je 25 keer en bij 1 : 50 verklein je 50 keer. Welke verkleining is sterker?”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-295` (Claude M19, ai, niveau 3 → toepassen)
    - **Opgave:** Marit tekent een boom op schaal 1 : 25. Dat betekent: 1 cm op de tekening is 25 cm in het echt. Sem tekent dezelfde boom op schaal 1 : 50. Wie krijgt de kleinste tekening?
    - **Opties:** A) Sem · B) Marit · C) Ze krijgen even grote tekeningen
    - **Antwoord:** Sem  (controle: n.v.t.)
    - **Fout-hints (Claude):** Marit → Bij 1 : 25 verklein je 25 keer en bij 1 : 50 verklein je 50 keer. Welke verkleining is sterker? · Ze krijgen even grote tekeningen → De twee schalen zijn verschillend, dus de tekeningen worden ook niet even groot.
    - **Uitleg (Claude):** Bij schaal 1 : 50 maak je de boom 50 keer kleiner, bij 1 : 25 maar 25 keer. Hoe groter het tweede getal, hoe kleiner de tekening. Sem krijgt dus de kleinste tekening.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Hoe groter het getal achter de dubbele punt, hoe meer centimeter in het echt bij één centimeter op de tekening hoort.
- **Hint 2 (te schrijven):** Stel: het echte voorwerp is tweeduizend centimeter. Reken voor elke schaal uit hoe lang het op de tekening wordt. Welke tekening is kleiner?
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere schaal gekozen` (Marit) → Bij die schaal hoort bij één centimeter op de tekening minder in het echt. Wordt de tekening dan groter of kleiner?  [nieuw]
  - `even groot` (Ze krijgen even grote tekeningen) → Het is hetzelfde voorwerp, maar de schalen zijn verschillend. Dan worden de tekeningen ook verschillend groot.  [nieuw]
  - `andere fout` (andere fout) → Reken voor elke schaal uit hoe lang de tekening wordt.  [nieuw]
- Status: hints klaar

## Somtype 19: Op een kaart van een park staat schaal # : #. Dat betekent: # cm op de kaart is # cm in het echt. Hoeveel meter is # cm op die kaart in het echt?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Op een kaart van een park staat schaal # : #. Dat betekent: # cm op de kaart is # cm in het echt. Hoeveel meter is # cm op die kaart in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): getal-overgenomen (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “1 cm is 1000 cm echt. Reken die centimeters nog om naar meters.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-296` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Op een kaart van een park staat schaal 1 : 1000. Dat betekent: 1 cm op de kaart is 1000 cm in het echt. Hoeveel meter is 1 cm op die kaart in het echt?
    - **Opties:** A) 100 m · B) 10 m · C) 1000 m
    - **Antwoord:** 10 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1000 m → 1 cm is 1000 cm echt. Reken die centimeters nog om naar meters. · 100 m → Denk eraan. 100 cm is 1 m. Hoeveel meter zit er dan in 1000 cm?
    - **Uitleg (Claude):** Bij 1 : 1000 hoort bij 1 cm op de kaart 1000 cm echt. 1000 cm is 10 m. Dus 1 cm op de kaart is 10 m in het park.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Eén centimeter op de kaart of plattegrond is in het echt zoveel centimeter als het getal achter de dubbele punt. Reken dat om: honderd centimeter is één meter, duizend meter is één kilometer.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `centimeters als meters` (1000 m) → Kijk naar de maat. Het getal achter de dubbele punt is een aantal centimeters, geen meters. Reken het om: honderd centimeter is één meter.  [nieuw]
  - `tien keer te veel` (100 m) → Dat is tien keer te veel. Honderd centimeter is één meter: hoeveel meter is het?  [nieuw]
  - `andere fout` (andere fout) → Reken de centimeters om naar meters.  [nieuw]
- Status: hints klaar

## Somtype 20: Op een landkaart staat schaal # : #. Hoeveel is # cm op de kaart in het echt?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Op een landkaart staat schaal # : # #. Hoeveel is # cm op de kaart in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “1 cm is 100.000 cm echt. Reken dat eerst om naar meters en kijk dan of het al kilometers zijn.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-297` (Claude M19, ai, niveau 3 → toepassen)
    - **Opgave:** Op een landkaart staat schaal 1 : 100.000. Hoeveel is 1 cm op de kaart in het echt?
    - **Opties:** A) 100 m · B) 10 km · C) 1 km
    - **Antwoord:** 1 km  (controle: n.v.t.)
    - **Fout-hints (Claude):** 100 m → 1 cm is 100.000 cm echt. Reken dat eerst om naar meters en kijk dan of het al kilometers zijn. · 10 km → Tel de nullen nog eens rustig na bij het omrekenen van cm naar km.
    - **Uitleg (Claude):** 1 cm op de kaart is 100.000 cm in het echt. 100.000 cm is 1000 m, en 1000 m is 1 km. Dus 1 cm op de kaart is 1 km.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Eén centimeter op de kaart of plattegrond is in het echt zoveel centimeter als het getal achter de dubbele punt. Reken dat om: honderd centimeter is één meter, duizend meter is één kilometer.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te weinig` (100 m) → Dat is tien keer te weinig. Reken de centimeters eerst om naar meters, en dan naar kilometers.  [nieuw]
  - `tien keer te veel` (10 km) → Dat is tien keer te veel. Honderd centimeter is één meter, en duizend meter is één kilometer.  [nieuw]
  - `andere fout` (andere fout) → Reken de centimeters om naar meters, en dan naar kilometers.  [nieuw]
- Status: hints klaar

## Somtype 21: Op een plattegrond staat schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoeveel is # cm op die plattegrond in het echt?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Op een plattegrond staat schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Hoeveel is # cm op die plattegrond in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “1 cm is 200 cm echt. Reken nu rustig van cm naar m. 100 cm is 1 m.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-298` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Op een plattegrond staat schaal 1 : 200. Dat betekent: 1 cm op de tekening is 200 cm in het echt. Hoeveel is 1 cm op die plattegrond in het echt?
    - **Opties:** A) 200 m · B) 2 m · C) 20 m
    - **Antwoord:** 2 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 20 m → 1 cm is 200 cm echt. Reken nu rustig van cm naar m. 100 cm is 1 m. · 200 m → Je hebt het getal van de schaal gewoon overgenomen, maar de eenheid verandert nog van cm naar m.
    - **Uitleg (Claude):** Bij 1 : 200 hoort bij 1 cm op papier 200 cm in het echt. En 200 cm is hetzelfde als 2 m. Dus 1 cm op de plattegrond is 2 m echt.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het ene getal hoort bij de tekening, het andere bij het echte voorwerp.
- **Hint 2 (te schrijven):** Eén centimeter op de kaart of plattegrond is in het echt zoveel centimeter als het getal achter de dubbele punt. Reken dat om: honderd centimeter is één meter, duizend meter is één kilometer.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `centimeters als meters` (200 m) → Kijk naar de maat. Het getal achter de dubbele punt is een aantal centimeters, geen meters. Reken het om: honderd centimeter is één meter.  [nieuw]
  - `tien keer te veel` (20 m) → Dat is tien keer te veel. Honderd centimeter is één meter: hoeveel meter is het?  [nieuw]
  - `andere fout` (andere fout) → Reken de centimeters om naar meters.  [nieuw]
- Status: hints klaar

## Somtype 22: Op een plattegrond van een dierentuin met schaal # : # is een pad # cm lang. Hoe lang is het pad in het echt?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “Op een plattegrond van een dierentuin met schaal # : # is een pad # cm lang. Hoe lang is het pad in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “5 × 1000 geeft centimeters, geen meters. Reken die centimeters nog om.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-299` (Claude M19, ai, niveau 3 → toepassen)
    - **Opgave:** Op een plattegrond van een dierentuin met schaal 1 : 1000 is een pad 5 cm lang. Hoe lang is het pad in het echt?
    - **Opties:** A) 5000 m · B) 5 m · C) 50 m
    - **Antwoord:** 50 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5000 m → 5 × 1000 geeft centimeters, geen meters. Reken die centimeters nog om. · 5 m → Je bent de vermenigvuldiging met de schaal bijna vergeten. Reken eerst 5 × 1000 uit.
    - **Uitleg (Claude):** Elke cm op de plattegrond is 1000 cm echt, dus 5 cm is 5000 cm. 5000 cm is 50 m. Het pad is dus 50 m lang.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Doe de maat op de tekening keer het getal achter de dubbele punt. Zoveel centimeter is het in het echt. Maak van die centimeters daarna meters: honderd centimeter is één meter.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `centimeters als meters` (5000 m) → Kijk naar de maat. Keer het getal achter de dubbele punt geeft centimeters, nog geen meters.  [nieuw]
  - `tien keer te weinig` (5 m) → Dat is tien keer te weinig. Reken eerst uit hoeveel centimeter het echt is, en maak daar meters van.  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel centimeter het echt is, en maak daar meters van.  [nieuw]
- Status: hints klaar

## Somtype 23: Op een tekening met schaal # : # is een deur # cm hoog. Hoe hoog is de deur in het echt?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “Op een tekening met schaal # : # is een deur # cm hoog. Hoe hoog is de deur in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), eenheid-verkeerd-omgerekend (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt 4 en 50 opgeteld. Bij schaal hoort een keerbewerking.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-300` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Op een tekening met schaal 1 : 50 is een deur 4 cm hoog. Hoe hoog is de deur in het echt?
    - **Opties:** A) 20 m · B) 200 cm · C) 54 cm
    - **Antwoord:** 200 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 54 cm → Je hebt 4 en 50 opgeteld. Bij schaal hoort een keerbewerking. · 20 m → Reken 4 × 50 uit in centimeters en kijk daarna hoeveel meter dat is.
    - **Uitleg (Claude):** Elke cm op de tekening is 50 cm echt. Je rekent 4 × 50 = 200. De deur is dus 200 cm hoog, en dat is 2 m.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Doe de maat op de tekening keer het getal achter de dubbele punt. Zoveel centimeter is het in het echt.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (54 cm) → Heb je de maat op de tekening en het getal achter de dubbele punt opgeteld? Elke centimeter op de tekening is in het echt zoveel centimeter als het getal achter de dubbele punt.  [nieuw]
  - `tien keer te veel` (20 m) → Dat is tien keer te veel. Reken de centimeters goed om: honderd centimeter is één meter.  [nieuw]
  - `andere fout` (andere fout) → Doe de maat op de tekening keer het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 24: Op een tekening met schaal # : # is een tafel # cm lang. Hoe lang is de tafel in het echt?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “Op een tekening met schaal # : # is een tafel # cm lang. Hoe lang is de tafel in het echt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt 3 en 100 bij elkaar opgeteld. Bij schaal hoort een keerbewerking.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-301` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Op een tekening met schaal 1 : 100 is een tafel 3 cm lang. Hoe lang is de tafel in het echt?
    - **Opties:** A) 30 cm · B) 300 cm · C) 103 cm
    - **Antwoord:** 300 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 103 cm → Je hebt 3 en 100 bij elkaar opgeteld. Bij schaal hoort een keerbewerking. · 30 cm → Je hebt met 10 gerekend. Kijk nog eens welk getal achter de dubbele punt staat.
    - **Uitleg (Claude):** Elke cm op de tekening is 100 cm echt. Bij 3 cm reken je 3 × 100. Dat is 300 cm.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Doe de maat op de tekening keer het getal achter de dubbele punt. Zoveel centimeter is het in het echt.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te weinig` (30 cm) → Dat is tien keer te weinig. Doe de maat op de tekening keer het getal achter de dubbele punt.  [nieuw]
  - `opgeteld` (103 cm) → Heb je de maat op de tekening en het getal achter de dubbele punt opgeteld? Elke centimeter op de tekening is in het echt zoveel centimeter als het getal achter de dubbele punt.  [nieuw]
  - `andere fout` (andere fout) → Doe de maat op de tekening keer het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 25: Van een school wordt een maquette gemaakt op schaal # : #. Dat betekent: # cm in het model is # cm in het echt. De school is # m lang. Hoe lang wordt de maquette?

- Sleutel: nrOrigineel **25** · somtypeOrigineel “Van een school wordt een maquette gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. De school is # m lang. Hoe lang wordt de maquette?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M19 (1) · regel: G7-V11-schaal-rekenen
- Getallenruimte: 0–1.000 · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): tiental-ernaast (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken 25 m eerst om naar cm en let dan goed op de nullen bij het delen door 100.”)
- Voorbeelden:
  - `G7-VERH-03-claude-bank-302` (Claude M19, ai, niveau 2 → toepassen)
    - **Opgave:** Van een school wordt een maquette gemaakt op schaal 1 : 100. Dat betekent: 1 cm in het model is 100 cm in het echt. De school is 25 m lang. Hoe lang wordt de maquette?
    - **Opties:** A) 25 m · B) 25 cm · C) 250 cm
    - **Antwoord:** 25 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 250 cm → Reken 25 m eerst om naar cm en let dan goed op de nullen bij het delen door 100. · 25 m → Dit is de echte lengte van de school. Een maquette is veel kleiner.
    - **Uitleg (Claude):** 25 m is 2500 cm. Op schaal 1 : 100 deel je door 100: 2500 : 100 = 25. De maquette wordt dus 25 cm lang.

- **Hint 1 (te schrijven):** Bij een schaal staat een dubbele punt (:) tussen de getallen. Het getal achter de dubbele punt zegt hoeveel keer zo groot het in het echt is.
- **Hint 2 (te schrijven):** Maak van de echte maat eerst centimeters, als dat nog moet. Deel dan door het getal achter de dubbele punt. Zoveel centimeter wordt het op de tekening of in het model.
- **Ouderzin:** Je kind rekent met een schaal (zoals op een plattegrond) tussen de tekening en het echte voorwerp.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de echte maat` (25 m) → Dat is de echte maat. Op de tekening of in het model is alles kleiner dan in het echt.  [nieuw]
  - `tien keer te lang` (250 cm) → Dat is tien keer te lang. Maak van de echte maat eerst centimeters, en deel dan door het getal achter de dubbele punt.  [nieuw]
  - `andere fout` (andere fout) → Maak van de echte maat centimeters, en deel door het getal achter de dubbele punt.  [nieuw]
- Status: hints klaar
