# G4-MEET-E05 — Wegen in kilogrammen

Onze omschrijving: Gewicht: kg; weegschaal; schatten; referenties · in onze bank: 8 items

Claude-vragen gemapt: **2** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [referentie] Hoe zwaar is … ongeveer?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[referentie] Hoe zwaar is … ongeveer?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M27 (1) · regel: G20-referentie
- Getallenruimte: n.v.t. · type: meerkeuze
- Merge-fixlijst: #29 kind uit groep 4 (1)
- Denkfouten (Claude): tiental-ernaast (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “3 kg is zo zwaar als drie pakken suiker. Dat is veel te licht voor een kind.”)
- Voorbeelden:
  - `G4-MEET-E05-claude-bank-001` (Claude M27, ai, niveau 2 → toepassen)
    - **Opgave:** Hoe zwaar is een kind uit groep 4 ongeveer?
    - **Opties:** A) 3 kg · B) 300 kg · C) 30 kg
    - **Antwoord:** 30 kg  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3 kg → 3 kg is zo zwaar als drie pakken suiker. Dat is veel te licht voor een kind. · 300 kg → 300 kg is zwaarder dan een pony. Denk nog eens aan de weegschaal thuis.
    - **Uitleg (Claude):** Een kind van 8 of 9 jaar weegt meestal ongeveer 30 kilogram. Een volwassene weegt ongeveer 75 kilogram. Een kind is dus een stuk lichter.

- **Hint 1 (te schrijven):** Denk aan iets wat je kent. Een pak suiker weegt één kilo (1 kg).
- **Hint 2 (te schrijven):** Is het lichter of zwaarder dan een pak suiker? Hoeveel pakken suiker zou het ongeveer zijn?
- **Ouderzin:** Je kind schat hoe zwaar iets is.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde schatting` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `te zwaar` (40 kg) → 40 kg is zwaarder dan een kind uit jouw klas. Dat is te veel voor een kat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Denk aan een pak suiker. Is het lichter of zwaarder? Hoeveel keer zo zwaar?  [nieuw]
- Status: hints klaar

## Somtype 2: [referentie] Welk voorwerp weegt ongeveer # kg?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[referentie] Welk voorwerp weegt ongeveer # kg?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M27 (1) · regel: G20-referentie
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): schatting-verkeerd (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een potlood voel je bijna niet in je hand. Zoek iets wat echt zwaar aanvoelt.”)
- Voorbeelden:
  - `G4-MEET-E05-claude-bank-003` (Claude M27, ai, niveau 1 → basis)
    - **Opgave:** Welk voorwerp weegt ongeveer 1 kg?
    - **Opties:** A) Een potlood · B) Een tafel · C) Een pak suiker
    - **Antwoord:** Een pak suiker  (controle: n.v.t.)
    - **Fout-hints (Claude):** Een potlood → Een potlood voel je bijna niet in je hand. Zoek iets wat echt zwaar aanvoelt. · Een tafel → Een tafel til je niet zomaar met één hand op. Denk aan iets uit de keukenkast.
    - **Uitleg (Claude):** Een pak suiker weegt 1 kilogram. Dat is even zwaar als een fles water van 1 liter. Zo'n pak is een handige maat om mee te vergelijken.

- **Hint 1 (te schrijven):** Til in gedachten elk ding op. Is het heel licht, heel zwaar, of daartussen?
- **Hint 2 (te schrijven):** Een kilo (1 kg) voel je echt in je hand. Toch kun je het met één hand optillen.
- **Ouderzin:** Je kind zoekt een voorwerp dat ongeveer één kilo weegt.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde schatting` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere fout` (andere fout) → Til in gedachten de dingen op. Welke is niet heel licht en niet heel zwaar?  [nieuw]
- Status: hints klaar
