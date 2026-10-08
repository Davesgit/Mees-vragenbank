# G8-MEET-E05 — Temperatuur onder en boven nul

Onze omschrijving: Temperatuur ↔ getallenlijn (onder/boven nul) · in onze bank: 8 items

Claude-vragen gemapt: **229** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Het is # °C. Het wordt # graden kouder. Hoe koud is het dan, in °C?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Het is # °C. Het wordt # graden kouder. Hoe koud is het dan, in °C?” (koppeling: claudeId)
- Items: **149** · Claude-doelen: C20 (149) · regel: D8-NEG-NAAR-TEMPERATUUR, D8-NEG-NAAR-TEMPERATUUR-NIEUW-GETAL
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er 1 naast. Tel op de thermometer nog eens, één streepje per graad. Ga eerst naar 0 en dan verder omlaag.”)
- Voorbeelden:
  - `G8-MEET-E05-claude-bank-076` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 1 °C. Het wordt 3 graden kouder. Hoe koud is het dan, in °C?
    - **Antwoord:** −2  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · −3 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G8-MEET-E05-claude-bank-024` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 5 °C. Het wordt 19 graden kouder. Hoe koud is het dan, in °C?
    - **Antwoord:** −14  (controle: n.v.t.)
    - **Fout-hints (Claude):** 24 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · −15 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** Kouder betekent: de temperatuur gaat omlaag op de thermometer.
- **Hint 2 (te schrijven):** Ga eerst omlaag tot nul. Tel hoeveel graden je daarna nog verder omlaag moet. Het wordt dat aantal graden onder nul: zet er een min voor.
- **Ouderzin:** Je kind rekent met temperaturen onder nul: eerst omlaag tot 0, dan verder omlaag. Onder nul staat er een min voor het getal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `warmer` (fout = getal1 + getal2) → Dat is warmer dan aan het begin. Kouder betekent omlaag op de thermometer.  [nieuw]
  - `min vergeten` (fout = getal1 - getal2 of getal2 - getal1) → Het wordt kouder dan nul. Onder nul zet je een min voor het getal.  [nieuw]
  - `van nul af geteld` (fout = van nul af geteld) → Dat is alleen het aantal graden kouder, gerekend vanaf nul. Je begint boven nul: tel eerst de graden tot nul, en ga dan verder omlaag.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt de temperatuur nadat het kouder is geworden.  [nieuw]
  - `één ernaast` (fout = antwoord ± 1) → Dat is één graad ernaast. Tel nog eens, graad voor graad: eerst omlaag tot nul, dan verder omlaag.  [nieuw]
  - `andere fout` (andere fout) → Tel nog eens, graad voor graad: eerst omlaag tot nul, dan verder omlaag. Onder nul komt er een min voor het getal.  [nieuw]
- Status: hints klaar

## Somtype 2: Het is −# °C. Dat is # graden onder nul. Het wordt # graden kouder. Hoe koud is het dan, in °C?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Het is −# °C. Dat is # graden onder nul. Het wordt # graden kouder. Hoe koud is het dan, in °C?” (koppeling: claudeId)
- Items: **68** · Claude-doelen: C20 (68) · regel: D8-NEG-NAAR-TEMPERATUUR, D8-NEG-NAAR-TEMPERATUUR-NIEUW-GETAL
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er 1 naast. Tel op de thermometer nog eens, één streepje per graad. Ga eerst naar 0 en dan verder omlaag.”)
- Voorbeelden:
  - `G8-MEET-E05-claude-bank-206` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is −4 °C. Dat is 4 graden onder nul. Het wordt 16 graden kouder. Hoe koud is het dan, in °C?
    - **Antwoord:** −20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · −19 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G8-MEET-E05-claude-bank-212` (Claude C20, bank, niveau 3 → toepassen)
    - **Opgave:** Het is −1 °C. Dat is 1 graad onder nul. Het wordt 8 graden kouder. Hoe koud is het dan, in °C?
    - **Antwoord:** −9  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 9 → Teken een getallenlijn met nul in het midden. Waar sta je, waar ga je heen?

- **Hint 1 (te schrijven):** Het is al onder nul. Kouder betekent: nog verder omlaag op de thermometer.
- **Hint 2 (te schrijven):** Tel de graden onder nul en de graden die het kouder wordt bij elkaar op. Zo ver onder nul kom je: zet er een min voor.
- **Ouderzin:** Je kind rekent met temperaturen onder nul: van onder nul nog verder omlaag. Het antwoord krijgt een min ervoor.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teken vergeten` (fout = teken vergeten) → Het was al onder nul en het wordt nog kouder. Dan blijf je onder nul: er hoort een min voor het getal.  [nieuw]
  - `verkeerde richting` (fout = verkeerde richting) → Dat is warmer dan aan het begin. Kouder betekent: nog verder omlaag op de thermometer.  [nieuw]
  - `van nul af geteld` (fout = van nul af geteld) → Dat is alleen het aantal graden kouder, gerekend vanaf nul. Je begint al onder nul: tel de graden onder nul en de graden kouder bij elkaar op.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je zoekt de temperatuur nadat het nog kouder is geworden.  [nieuw]
  - `één ernaast` (fout = antwoord ± 1) → Dat is één graad ernaast. Tel de graden onder nul en de graden die het kouder wordt nog eens bij elkaar op.  [nieuw]
  - `andere fout` (andere fout) → Je begint onder nul en gaat nog verder omlaag. Dan blijf je onder nul: er komt een min voor het getal. Tel de graden nog eens na.  [nieuw]
- Status: hints klaar

## Somtype 3: [stip op getallenlijn zetten] Zet # op de getallenlijn.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[stip op getallenlijn zetten] Zet # op de getallenlijn.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: C20 (12) · regel: G8-P00-park-G7
- Getallenruimte: 0–1.000 · type: kale
- **Visual: nodig — niet live zonder beeld** (12 items): interactief: stip op getallenlijn zetten
- Denkfouten (Claude): None (12)
- Verschillende Claude-fout-hints: 1 (meest: “Let op het minteken: dat is links van de nul.”)
- Voorbeelden:
  - `G8-MEET-E05-claude-bank-006` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet −4 op de getallenlijn.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** −4  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 → Let op het minteken: dat is links van de nul.
    - **Uitleg (Claude):** Links van 0 staan de getallen onder nul. 4 stappen naar links vanaf 0.
  - `G8-MEET-E05-claude-bank-001` (Claude C20, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet −5 op de getallenlijn.
    - **UI:** stip op getallenlijn zetten
    - **Antwoord:** −5  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 → Let op het minteken: dat is links van de nul.
    - **Uitleg (Claude):** Links van 0 staan de getallen onder nul. 5 stappen naar links vanaf 0.

- **Hint 1 (te schrijven):** Getallen onder nul staan links van de nul. Getallen boven nul staan rechts van de nul.
- **Hint 2 (te schrijven):** Staat er een min voor het getal? Ga dan vanaf de nul naar links. Zonder min ga je naar rechts. Tel de stappen.
- **Ouderzin:** Je kind zet een getal op de getallenlijn: met een min ervoor links van de nul, zonder min rechts.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teken vergeten` (fout = teken vergeten) → Kijk goed of er een min voor het getal staat. Met een min hoort het links van de nul, zonder min rechts.  [nieuw]
  - `andere fout` (andere fout) → Kijk of er een min voor het getal staat. Met een min staat het links van de nul, zonder min rechts.  [nieuw]
- Status: hints klaar
