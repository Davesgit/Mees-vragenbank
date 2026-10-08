# G4-MEET-E02 — Lengte schatten en omtrek

Onze omschrijving: Lengte schatten; referentiematen; omtrek bepalen · in onze bank: 8 items

Claude-vragen gemapt: **11** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [referentie] Hoe lang/hoog/breed is … ongeveer? (m of cm)

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[referentie] Hoe lang/hoog/breed is … ongeveer? (m of cm)” (koppeling: claudeId)
- Items: **11** · Claude-doelen: M27 (11) · regel: G20-referentie
- Getallenruimte: n.v.t. · type: meerkeuze
- Merge-fixlijst: #29 kind uit groep 4 (1), #35 '120 m' → '50 m' (1)
- Denkfouten (Claude): tiental-ernaast (8), schatting-verkeerd (5), eenheid-verkeerd-omgerekend (4), verkeerde-maat (3), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 18 (meest: “Denk even na. Een centimeter is ongeveer zo breed als je duim of de nagel van je vinger. Is een deur zo klein?”)
- Voorbeelden:
  - `G4-MEET-E02-claude-bank-004` (Claude M27, ai, niveau 1 → basis)
    - **Opgave:** Hoe hoog is een deur in je klas ongeveer?
    - **Opties:** A) 2 m · B) 2 cm · C) 20 m
    - **Antwoord:** 2 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2 cm → Denk even na. Een centimeter is ongeveer zo breed als je duim of de nagel van je vinger. Is een deur zo klein? · 20 m → 20 m is zo hoog als een flat met veel verdiepingen. Kijk nog eens naar de deur in het lokaal.
    - **Uitleg (Claude):** Een deur is net iets hoger dan een volwassen mens. Een volwassene is ongeveer 1,80 m. Daarom is een deur ongeveer 2 m hoog.
  - `G4-MEET-E02-claude-bank-007` (Claude M27, ai, niveau 2 → toepassen)
    - **Opgave:** Hoe lang is een klaslokaal ongeveer?
    - **Opties:** A) 8 m · B) 80 cm · C) 80 m
    - **Antwoord:** 8 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 80 cm → 80 cm is bijna een meter. Dat is smaller dan een tafel. · 80 m → 80 m is bijna een heel voetbalveld. Zo groot is een lokaal niet.
    - **Uitleg (Claude):** Je kunt een lokaal afstappen met grote stappen van ongeveer 1 meter. Dan doe je er ongeveer acht. Een klaslokaal is dus ongeveer 8 m lang.

- **Hint 1 (te schrijven):** Denk aan iets wat je kent, zoals je hand of je eigen lengte. Is het ding groter of kleiner?
- **Hint 2 (te schrijven):** Kleine dingen meet je in centimeter, grote dingen in meter. Kies eerst de maat. Kies dan een getal dat erbij past.
- **Ouderzin:** Je kind schat hoe lang of hoog iets is, in meter of centimeter.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde schatting` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `te groot` (1000 m) → 1000 m is heel ver. Daar loop je lang over. Een voetbalveld is veel korter.  [nieuw]
  - `te klein` (10 m) → 10 m is veel te kort. Op een voetbalveld kun je heel ver rennen.  [nieuw]
  - `korter dan een meter` (80 cm) → 80 cm is nog geen meter. Zo kort is een klaslokaal niet.  [nieuw]
  - `goed getal, verkeerde maat (45 m)` (45 m) → Het getal klopt, maar de maat niet. Is het centimeter of meter?  [nieuw]
  - `goed getal, verkeerde maat (20 m)` (20 m) → Kijk goed naar de maat. 20 meter is langer dan twee klaslokalen. Een schoen is korter dan een liniaal van dertig centimeter.  [nieuw]
  - `goed getal, verkeerde maat (18 m)` (18 m) → Het getal klopt, maar de maat niet. Is het centimeter of meter?  [nieuw]
  - `korter dan een meter (1 m)` (1 m) → 1 m is langer dan je been. Een schoen is veel korter dan dat.  [nieuw]
  - `half voetbalveld (50 m)` (50 m) → 50 m is zo lang als een half voetbalveld. Een bus is veel korter.  [nieuw]
  - `andere fout` (andere fout) → Denk aan iets wat je kent, zoals je hand of je eigen lengte. Is het langer of korter?  [nieuw]
- Status: hints klaar
