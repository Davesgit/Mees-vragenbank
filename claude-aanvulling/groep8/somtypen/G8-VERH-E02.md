# G8-VERH-E02 — Lastige verhoudingssommen oplossen

Onze omschrijving: Complexe verhoudingsproblemen (relatie niet direct zichtbaar) · in onze bank: 8 items

Claude-vragen gemapt: **1** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In een winkel kosten # [ding] sap samen €#. Hoeveel kosten # van die pakken sap?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In een winkel kosten # [ding] sap samen €#. Hoeveel kosten # van die pakken sap?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VERH-GELD
- Getallenruimte: kommagetallen (2 cijfers achter de komma) · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Je deed er €2 bij. Reken eerst uit wat één pak kost.”)
- Voorbeelden:
  - `G8-VERH-E02-claude-bank-001` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een winkel kosten 3 pakken sap samen €4,50. Hoeveel kosten 5 van die pakken sap?
    - **Opties:** A) €6,50 · B) €22,50 · C) €7,50
    - **Antwoord:** €7,50  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6,5 euro → Je hebt er 2 euro bij gedaan. Reken eerst uit wat één pak kost. · 22,5 euro → Je hebt de totaalprijs met 5 vermenigvuldigd. Ga eerst terug naar één pak.
    - **Uitleg (Claude):** Eén pak sap kost 4,50 : 3 = 1,50 euro. Dan kosten 5 pakken 5 × 1,50 = 7,50 euro.

- **Hint 1 (te schrijven):** Wat kost er één? Reken dat eerst uit.
- **Hint 2 (te schrijven):** Deel de prijs door het aantal dat samen zoveel kost: dan weet je wat er één kost. Doe dat keer het aantal dat gevraagd wordt.
- **Ouderzin:** Je kind rekent via de prijs van één stuk uit wat meer stuks kosten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een klein bedrag erbij` (€6,50) → Je deed het verschil in aantal erbij, alsof elk extra stuk één euro kost. Wat kost er één? Doe dat keer het aantal dat gevraagd wordt.  [nieuw]
  - `keer het nieuwe aantal` (€22,50) → Dat is de prijs van de hele groep uit de vraag, keer het nieuwe aantal. Reken eerst uit wat er één kost.  [nieuw]
  - `andere fout` (andere fout) → Wat kost er één? Doe dat keer het aantal dat gevraagd wordt.  [nieuw]
- Status: hints klaar
