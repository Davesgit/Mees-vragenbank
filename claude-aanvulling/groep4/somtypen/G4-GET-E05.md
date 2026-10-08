# G4-GET-E05 — Schatten met plus en min

Onze omschrijving: Schattend +/− ≤100; kritisch redeneren +/− · in onze bank: 8 items

Claude-vragen gemapt: **37** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: T3 (12) · regel: D8-SCHAT-NAAR-G4
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-001` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 16 + 31 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 50  (controle: n.v.t.)
    - **Fout-hints (Claude):** 51 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 60 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G4-GET-E05-claude-bank-naar-007` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 18 + 58 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 80  (controle: n.v.t.)
    - **Fout-hints (Claude):** 76 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 100 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen. Je maakt eerst van elk getal een rond getal: een getal dat eindigt op een nul.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Tel daarna de twee ronde getallen op.
- **Ouderzin:** Je kind schat een plussom: eerst van allebei de getallen een rond getal maken (op tientallen), dan die optellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Dat is precies uitgerekend. Maak eerst van allebei de getallen een rond getal, zoals de vraag zegt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de ronde getallen.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `tien te weinig` (fout = antwoord - 10) → Dat is tien te weinig. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `twintig te veel` (fout = antwoord + 20) → Dat is twintig te veel. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `twintig te weinig` (fout = antwoord - 20) → Dat is twintig te weinig. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `andere fout` (andere fout) → Maak eerst van allebei de getallen een rond getal, zoals de vraag zegt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Tel daarna de twee ronde getallen op.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoeveel is # − # [ding]? Rond beide getallen af op tientallen en reken dan uit.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op tientallen en reken dan uit.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-SCHAT-NAAR-G4
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 4 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-013` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 44 − 20 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 40 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G4-GET-E05-claude-bank-naar-017` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 54 − 32 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 22 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 40 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Schatten is ongeveer uitrekenen. Je maakt eerst van elk getal een rond getal: een getal dat eindigt op een nul.
- **Hint 2 (te schrijven):** Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Haal daarna het tweede ronde getal van het eerste af.
- **Ouderzin:** Je kind schat een minsom: eerst van allebei de getallen een rond getal maken (op tientallen), dan het ene van het andere afhalen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 - getal2 of getal2 - getal1) → Dat is precies uitgerekend. Maak eerst van allebei de getallen een rond getal, zoals de vraag zegt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de ronde getallen.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `tien te weinig` (fout = antwoord - 10) → Dat is tien te weinig. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `twintig te veel` (fout = antwoord + 20) → Dat is twintig te veel. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `twintig te weinig` (fout = antwoord - 20) → Dat is twintig te weinig. Kijk nog eens hoe je van elk getal een rond getal maakt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Reken dan met de twee ronde getallen.  [nieuw]
  - `andere fout` (andere fout) → Maak eerst van allebei de getallen een rond getal, zoals de vraag zegt. Kijk bij elk getal naar de eenheden. Zijn het er minder dan vijf? Dan houd je alleen de tientallen. Zijn het er vijf of meer? Dan neem je één tiental meer. Haal daarna het tweede ronde getal van het eerste af.  [nieuw]
- Status: hints klaar

## Somtype 3: Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-NAAR-G4
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (7), bovengrens (4), laatste-cijfer (3), ondergrens (2)
- Verschillende Claude-fout-hints: 16 (meest: “Rond allebei naar boven af. 40 + 40 is 80. De uitkomst kan dus niet groter zijn dan 80, en 84 is groter.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-021` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 39 + 35 kan kloppen?
    - **Opties:** A) 74 · B) 84 · C) 4
    - **Antwoord:** 74  (controle: n.v.t.)
    - **Fout-hints (Claude):** 84 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G4-GET-E05-claude-bank-naar-025` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 41 + 32 kan kloppen?
    - **Opties:** A) 73 · B) 730 · C) 71
    - **Antwoord:** 73  (controle: n.v.t.)
    - **Fout-hints (Claude):** 83 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Je hoeft niet precies te rekenen. Kijk eerst naar het laatste cijfer. Tel alleen de eenheden op. Op welk cijfer eindigt dat? Daar eindigt het antwoord ook op.
- **Hint 2 (te schrijven):** Blijven er twee over? Neem van allebei de getallen alleen de tientallen en tel op. Het antwoord is groter dan dat. Maak van allebei de getallen het tiental erboven en tel op. Is een getal al rond? Dan blijft het zo. Groter kan het antwoord niet zijn.
- **Ouderzin:** Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door naar het laatste cijfer te kijken en te schatten hoe groot het is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min in plaats van plus` (fout = getal1 - getal2 of getal2 - getal1) → Heb je min gedaan? Er staat een plus: er komt iets bij. Het antwoord is dus groter dan allebei de getallen.  [nieuw]
  - `veel te groot` (fout = antwoord × 10) → Dat is veel te groot. Schat eerst: maak van allebei de getallen een rond getal en reken daarmee. Het antwoord ligt daar dichtbij.  [nieuw]
  - `te groot` (Claudes sleutel: bovengrens) → Dat is te groot. Maak van allebei de getallen het tiental erboven en tel op. Is een getal al rond? Dan blijft het zo. Groter dan dat kan het antwoord niet zijn.  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Dat is te klein. Neem van allebei de getallen alleen de tientallen en tel op. Kleiner dan dat kan het antwoord niet zijn.  [Claude, taalfix]
  - `laatste cijfer` (Claudes sleutel: laatste-cijfer) → Kijk naar het laatste cijfer. Tel alleen de eenheden op. Op welk cijfer eindigt dat? Daar eindigt het antwoord ook op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk naar het laatste cijfer. Tel alleen de eenheden op. Op welk cijfer eindigt dat? Daar eindigt het antwoord ook op. Kijk dan of het antwoord niet te groot en niet te klein is.  [nieuw]
- Status: hints klaar

## Somtype 4: Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-KLOPPEN-NAAR-G4
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): bovengrens (6), laatste-cijfer (6), orde-van-grootte (4)
- Verschillende Claude-fout-hints: 16 (meest: “Rond 88 naar boven af en 33 naar beneden. 90 − 30 is 60. De uitkomst kan dus niet groter zijn dan 60, en 65 is groter.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-naar-029` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 88 − 33 kan kloppen?
    - **Opties:** A) 55 · B) 65 · C) 57
    - **Antwoord:** 55  (controle: n.v.t.)
    - **Fout-hints (Claude):** 65 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G4-GET-E05-claude-bank-naar-033` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 71 − 29 kan kloppen?
    - **Opties:** A) 42 · B) 44 · C) 100
    - **Antwoord:** 42  (controle: n.v.t.)
    - **Fout-hints (Claude):** 100 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Je hoeft niet precies te rekenen. Kijk eerst naar het laatste cijfer. Haal de eenheden van elkaar af. Is het laatste cijfer van het eerste getal kleiner? Doe er dan eerst tien bij. Wat je krijgt, is het laatste cijfer van het antwoord.
- **Hint 2 (te schrijven):** Blijven er twee over? Maak van het eerste getal het tiental erboven. Is het al rond? Dan blijft het zo. Neem van het tweede getal alleen de tientallen, en haal dat ervan af. Groter kan het antwoord niet zijn.
- **Ouderzin:** Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door naar het laatste cijfer te kijken en te schatten hoe groot het is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus in plaats van min` (fout = getal1 + getal2) → Heb je plus gedaan? Er staat een min: er gaat iets af. Het antwoord is dus kleiner dan het eerste getal.  [nieuw]
  - `veel te groot` (fout = antwoord × 10) → Dat is veel te groot. Schat eerst: maak van allebei de getallen een rond getal en reken daarmee. Het antwoord ligt daar dichtbij.  [nieuw]
  - `te groot` (Claudes sleutel: bovengrens) → Dat is te groot. Maak van het eerste getal het tiental erboven. Is het al rond? Dan blijft het zo. Neem van het tweede getal alleen de tientallen, en haal dat ervan af. Groter dan dat kan het antwoord niet zijn.  [Claude, taalfix]
  - `laatste cijfer` (Claudes sleutel: laatste-cijfer) → Kijk naar het laatste cijfer. Haal de eenheden van elkaar af. Is het laatste cijfer van het eerste getal kleiner? Doe er dan eerst tien bij. Wat je krijgt, is het laatste cijfer van het antwoord.  [Claude, taalfix]
  - `andere fout` (andere fout) → Kijk naar het laatste cijfer. Haal de eenheden van elkaar af. Is het laatste cijfer van het eerste getal kleiner? Doe er dan eerst tien bij. Wat je krijgt, is het laatste cijfer van het antwoord. Kijk dan of het antwoord niet te groot is.  [nieuw]
- Status: hints klaar

## Somtype 5: In twee dozen zitten samen # [ding]. In de ene doos zitten # [ding] meer dan in de andere. Hoeveel [ding] zitten er in elke doos?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In twee dozen zitten samen # [ding]. In de ene doos zitten # [ding] meer dan in de andere. Hoeveel [ding] zitten er in elke doos?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): None (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar het verschil tussen de twee getallen. Dat moet precies 3 zijn.”)
- Voorbeelden:
  - `G4-GET-E05-claude-bank-001` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** In twee dozen zitten samen 15 ballen. In de ene doos zitten 3 ballen meer dan in de andere. Hoeveel ballen zitten er in elke doos?
    - **Opties:** A) 12 en 3 · B) 8 en 7 · C) 9 en 6
    - **Antwoord:** 9 en 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 en 3 → Kijk goed naar het verschil tussen de twee getallen. Dat moet precies 3 zijn. · 8 en 7 → Tel het verschil tussen jouw twee getallen. Is dat echt 3?
    - **Uitleg (Claude):** Samen moeten de getallen 15 zijn en het verschil moet 3 zijn. Bij 9 en 6 klopt allebei: 9 plus 6 is 15 en 9 min 6 is 3.

- **Hint 1 (te schrijven):** Er zijn twee dozen. Samen is het hele aantal. In de ene doos zitten er een paar meer dan in de andere.
- **Hint 2 (te schrijven):** Kies twee getallen die samen het hele aantal zijn. Het verschil is hoeveel meer het ene getal is dan het andere. Is het verschil te groot of te klein? Schuif er dan één van de ene doos naar de andere.
- **Ouderzin:** Je kind zoekt twee getallen die samen een bepaald aantal zijn en een bepaald verschil hebben.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
