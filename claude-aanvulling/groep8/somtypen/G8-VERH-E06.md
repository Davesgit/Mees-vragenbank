# G8-VERH-E06 — Procenten checken en omzetten uit je hoofd

Onze omschrijving: % niet zomaar optellen; kritische %; relaties VERH↔breuk↔%↔decimaal uit hoofd · in onze bank: 8 items

Claude-vragen gemapt: **104** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Schrijf # in procenten.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Schrijf # in procenten.” (koppeling: claudeId)
- Items: **96** · Claude-doelen: B13 (96) · regel: G8-P00-park-G7
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): komma-verschoven (102), getal-overgenomen (90)
- Verschillende Claude-fout-hints: 1 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-052` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,52 in procenten.
    - **Opties:** A) 0,52% · B) 520% · C) 52%
    - **Antwoord:** 52%  (controle: ok)
    - **Fout-hints (Claude):** 25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 0,25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G8-VERH-E06-claude-bank-011` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,525 in procenten.
    - **Opties:** A) 0,525% · B) 52,5% · C) 5,25%
    - **Antwoord:** 52,5%  (controle: ok)
    - **Fout-hints (Claude):** 5,25% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Procent betekent: zoveel van de honderd. Eén hele is honderd procent.
- **Hint 2 (te schrijven):** Doe het kommagetal keer honderd: de komma schuift dan naar rechts, één plek voor elke nul van honderd. Zet daarna het procentteken erachter.
- **Ouderzin:** Je kind schrijft een kommagetal als procent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kommagetal met procentteken` (fout = kommagetal met procentteken) → Dat is het kommagetal met een procentteken erachter. Procent is zoveel van de honderd: doe het kommagetal eerst keer honderd.  [nieuw]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma goed? Bij keer honderd schuift de komma twee plekken naar rechts, niet één of drie.  [Claude, taalfix]
  - `andere fout` (andere fout) → Doe het kommagetal keer honderd. Staat de komma dan twee plekken verder naar rechts?  [nieuw]
- Status: hints klaar

## Somtype 2: Schrijf #/# in procenten.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Schrijf #/# in procenten.” (koppeling: claudeId)
- Items: **7** · Claude-doelen: B13 (7) · regel: G8-P00-park-G7
- Getallenruimte: breuken (noemer tot 40) · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (7), nul-fout-tientallen (7)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-101` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 13/50 in procenten.
    - **Opties:** A) 26% · B) 13% · C) 260%
    - **Antwoord:** 26%  (controle: ok)
    - **Fout-hints (Claude):** 275% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · 2,75% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G8-VERH-E06-claude-bank-098` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 21/40 in procenten.
    - **Opties:** A) 5,25% · B) 52,5% · C) 21%
    - **Antwoord:** 52,5%  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5,25% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** Procent betekent: zoveel van de honderd. Een breuk met honderd als noemer kun je zo als procent schrijven.
- **Hint 2 (te schrijven):** Maak een verhoudingstabel: de noemer hoort bij honderd procent, de teller bij het procent dat je zoekt. Reken de noemer om naar honderd en doe met de teller hetzelfde. Gaat dat niet in één keer? Deel dan eerst allebei door hetzelfde getal.
- **Ouderzin:** Je kind schrijft een breuk als procent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de breuk` (fout = het deel zelf (als %)) → Dat is de teller met een procentteken erachter. Dat klopt alleen als de noemer honderd is. Reken de noemer eerst om naar honderd.  [nieuw]
  - `tien keer te groot (260%)` (260%) → Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?  [nieuw]
  - `tien keer te groot (350%)` (350%) → Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?  [nieuw]
  - `tien keer te groot (550%)` (550%) → Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?  [nieuw]
  - `tien keer te groot (720%)` (720%) → Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?  [nieuw]
  - `getal uit de breuk (kommaprocent)` (21%) → Dat is de teller met een procentteken erachter. Dat klopt alleen als de noemer honderd is. Reken de noemer eerst om naar honderd.  [nieuw]
  - `tien keer ernaast` (Claudes sleutel: nul-fout-tientallen) → Dat is tien keer te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 3: #% van de appels in [plek] is rot. Schrijf dat als kommagetal.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “#% van de [ding] is kapot. Schrijf dat als kommagetal.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B13 (1) · regel: G8-P00-park-G7
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): komma-verschoven (1), kommagetal-als-geheel (1)
- Verschillende Claude-fout-hints: 2 (meest: “Procent is per honderd: de komma schuift twee plekken naar links, niet één.”)
- Voorbeelden:
  - `G8-VERH-E06-claude-bank-001` (Claude B13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 12,5% van de appels in de kist is rot. Schrijf dat als kommagetal.
    - **Antwoord:** 0,125  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1,3 → Procent is per honderd: de komma schuift twee plekken naar links, niet één. · 12.5 → 12.5% is 12.5 van de 100. Als kommagetal deel je door 100.
    - **Uitleg (Claude):** Procent is per honderd: 12,5 : 100 = 0,125.

- **Hint 1 (te schrijven):** Procent betekent: zoveel van de honderd. Zoveel honderdsten kun je als kommagetal schrijven.
- **Hint 2 (te schrijven):** Deel het getal van het procent door honderd: de komma schuift twee plekken naar links. Is er geen heel getal? Zet dan een nul voor de komma.
- **Ouderzin:** Je kind schrijft een procent als kommagetal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te groot` (fout = antwoord × 10) → Dat is tien keer te groot. Procent zijn honderdsten: deel het getal van het procent door honderd.  [nieuw]
  - `procent zonder komma` (fout = een getal uit de vraag) → Dat is het getal van het procent. Als kommagetal is het honderd keer zo klein.  [nieuw]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma goed? Procent zijn honderdsten: de komma schuift twee plekken naar links.  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel het getal van het procent door honderd.  [nieuw]
- Status: hints klaar
