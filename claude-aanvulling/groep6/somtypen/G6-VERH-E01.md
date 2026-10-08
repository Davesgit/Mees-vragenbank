# G6-VERH-E01 — Verhoudingstabel gebruiken bij recepten en meer

Onze omschrijving: Verhoudingstabel interpreteren/gebruiken; alledaagse verhoudingen · in onze bank: 8 items

Claude-vragen gemapt: **15** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [schema] verhoudingstabel

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[schema] verhoudingstabel” (koppeling: claudeId)
- Items: **15** · Claude-doelen: merge-generator G6 ronde 9 (#231/#281) (11), W4 (4) · regel: G6-W03-schema-tabel, G6-r9 #231 generator
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (15), verhoudingstabel-verkeerd (9), getal-overgenomen (6)
- Verschillende Claude-fout-hints: 3 (meest: “Heb je er iets bij opgeteld? Kijk hoeveel keer zo groot het aantal in de vraag is.”)
- Voorbeelden:
  - `G6-VERH-E01-claude-bank-004` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** 1 fles is 3 L. Je zet dat in een tabel. Hoeveel liter is 5 van die flessen?
    - **Opties:** A) 15 L · B) 8 L · C) 5 L
    - **Antwoord:** 15 L  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 liter → Elke fles heeft 2 liter. Tel eens 2 liter op voor iedere fles apart. · 2,5 liter → Meer flessen betekent meer liter. Het antwoord wordt dus groter dan 2.
    - **Uitleg (Claude):** In de tabel staat 1 fles bij 3 L. Bij 5 flessen doe je 5 × 3. Dat is 15 L.
  - `G6-VERH-E01-merge-gen-005` (Claude merge-generator G6 ronde 9 (#231/#281), None, niveau 2 → toepassen)
    - **Opgave:** Voor 4 glazen limonade heb je 3 citroenen nodig. Je zet dat in een verhoudingstabel. Hoeveel citroenen heb je nodig voor 12 glazen limonade?
    - **Opties:** A) 11 citroenen · B) 6 citroenen · C) 9 citroenen
    - **Antwoord:** 9 citroenen  (controle: ok)
    - **Fout-hints (Claude):** 9 euro → Kijk hoe vaak 2 kg in 8 kg past. Met datzelfde aantal keer werk je bij de prijs. · 6 euro → Je bent maar tot 4 kg gekomen. Ga verder tot je bij 8 kg bent.
    - **Uitleg (Claude):** Van 4 naar 12 is 3 keer zoveel. Het andere getal ook: 3 citroenen × 3 = 9 citroenen.

- **Hint 1 (te schrijven):** In een verhoudingstabel horen twee getallen bij elkaar. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet?
- **Hint 2 (te schrijven):** Reken uit hoeveel keer zo groot het aantal in de vraag is als het aantal dat je al weet. Doe het andere getal ook zoveel keer. Zo blijft de verhouding gelijk.
- **Ouderzin:** Je kind rekent met een verhoudingstabel. Wordt het ene getal een aantal keer zo groot, dan wordt het andere getal ook zoveel keer zo groot.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = y1 + (x2 − x1)) → Heb je er iets bij opgeteld? Komt er bij het ene getal iets bij, dan komt er bij het andere getal niet vanzelf hetzelfde bij. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [nieuw]
  - `opgeteld` (fout = y1 + x2) → Heb je er iets bij opgeteld? Komt er bij het ene getal iets bij, dan komt er bij het andere getal niet vanzelf hetzelfde bij. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [nieuw]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Heb je er iets bij opgeteld? Komt er bij het ene getal iets bij, dan komt er bij het andere getal niet vanzelf hetzelfde bij. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [Claude, taalfix]
  - `verhouding niet gelijk` (Claudes sleutel: verhoudingstabel-verkeerd) → Ben je al bij het vakje uit de vraag? Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [Claude, taalfix]
  - `getal uit de vraag` (Claudes sleutel: getal-overgenomen) → Je hebt een getal uit de vraag overgenomen. Is dat echt het getal bij het vakje uit de vraag? Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [Claude, taalfix]
  - `gedeeld` (Claudes sleutel: verkeerde-bewerking) → Je hebt gedeeld. Bij een groter aantal hoort ook een groter getal. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer.  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet? Doe het andere getal ook zoveel keer. Zo blijft de verhouding gelijk.  [nieuw]
- Status: hints klaar
