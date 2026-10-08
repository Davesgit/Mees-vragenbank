# G8-MEET-E01 — Het systeem van lengtematen doorzien

Onze omschrijving: Lengte: metriek als systeem; nut maatverfijning · in onze bank: 8 items

Claude-vragen gemapt: **4** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een wandelaar loopt # km. Hoeveel meter is dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een wandelaar loopt # km. Hoeveel meter is dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M25 (2) · regel: G8-M25-km
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (2), kommagetal-als-geheel (2)
- Verschillende Claude-fout-hints: 2 (meest: “Van km naar m is drie plekken, niet twee.”)
- Voorbeelden:
  - `G8-MEET-E01-claude-bank-002` (Claude M25, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een wandelaar loopt 8,1 km. Hoeveel meter is dat?
    - **Antwoord:** 8100  (controle: ok)
    - **Fout-hints (Claude):** 810 → Van km naar m is drie plekken, niet twee. · 81 → Haal niet zomaar de komma weg. Keer 1000.
    - **Uitleg (Claude):** 1 km = 1000 m. De komma schuift drie plekken. 8,1 km = 8100 m.
  - `G8-MEET-E01-claude-bank-001` (Claude M25, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een wandelaar loopt 6,7 km. Hoeveel meter is dat?
    - **Antwoord:** 6700  (controle: ok)
    - **Fout-hints (Claude):** 670 → Van km naar m is drie plekken, niet twee. · 67 → Haal niet zomaar de komma weg. Keer 1000.
    - **Uitleg (Claude):** 1 km = 1000 m. De komma schuift drie plekken. 6,7 km = 6700 m.

- **Hint 1 (te schrijven):** Een kilometer is duizend meter.
- **Hint 2 (te schrijven):** Doe het aantal kilometer keer duizend. Bij een kommagetal schuift de komma dan drie plekken op. Vul aan met nullen.
- **Ouderzin:** Je kind rekent kilometer om naar meter: keer duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat is het getal in kilometer. De vraag wil meters: hoeveel meter is één kilometer?  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [nieuw]
  - `keer tien gedaan` (fout = antwoord : 100) → Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [nieuw]
  - `honderd keer te weinig` (Claudes sleutel: kommagetal-als-geheel) → Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer is duizend meter. Hoeveel meter is dan het aantal kilometer uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 2: [wie] loopt # km. Hoeveel meter is dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[wie] loopt # km. Hoeveel meter is dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M25 (2) · regel: G8-M25-km
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): komma-verschoven (2), kommagetal-als-geheel (2)
- Verschillende Claude-fout-hints: 2 (meest: “Van km naar m is drie plekken, niet twee.”)
- Voorbeelden:
  - `G8-MEET-E01-claude-bank-003` (Claude M25, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind loopt 8 km. Hoeveel meter is dat?
    - **Antwoord:** 8000  (controle: ok)
    - **Fout-hints (Claude):** 800 → Van km naar m is drie plekken, niet twee. · 80 → Haal niet zomaar de komma weg. Keer 1000.
    - **Uitleg (Claude):** 1 km = 1000 m. 8 km = 8000 m.
  - `G8-MEET-E01-claude-bank-004` (Claude M25, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind loopt 8,2 km. Hoeveel meter is dat?
    - **Antwoord:** 8200  (controle: ok)
    - **Fout-hints (Claude):** 820 → Van km naar m is drie plekken, niet twee. · 82 → Haal niet zomaar de komma weg. Keer 1000.
    - **Uitleg (Claude):** 1 km = 1000 m. De komma schuift drie plekken. 8,2 km = 8200 m.

- **Hint 1 (te schrijven):** Een kilometer is duizend meter.
- **Hint 2 (te schrijven):** Doe het aantal kilometer keer duizend. Bij een kommagetal schuift de komma dan drie plekken op. Vul aan met nullen.
- **Ouderzin:** Je kind rekent kilometer om naar meter: keer duizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat is het getal in kilometer. De vraag wil meters: hoeveel meter is één kilometer?  [nieuw]
  - `tien keer te weinig` (fout = antwoord : 10) → Dat is tien keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [nieuw]
  - `keer tien gedaan` (fout = antwoord : 100) → Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [nieuw]
  - `honderd keer te weinig` (Claudes sleutel: kommagetal-als-geheel) → Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén kilometer is duizend meter. Hoeveel meter is dan het aantal kilometer uit de vraag?  [nieuw]
- Status: hints klaar
