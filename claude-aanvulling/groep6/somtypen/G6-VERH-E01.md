# G6-VERH-E01 — Verhoudingstabel gebruiken bij recepten en meer

Onze omschrijving: Verhoudingstabel interpreteren/gebruiken; alledaagse verhoudingen · in onze bank: 8 items

Claude-vragen gemapt: **4** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [schema] verhoudingstabel

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[schema] verhoudingstabel” (koppeling: claudeId)
- Items: **4** · Claude-doelen: W4 (4) · regel: G6-W03-schema-tabel
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (3), optellen-ipv-vermenigvuldigen (2), verkeerde-bewerking (2), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 8 (meest: “Elke fles heeft 2 L. Tel eens 2 L op voor iedere fles apart.”)
- Voorbeelden:
  - `G6-VERH-E01-claude-bank-004` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** 1 fles is 2 L. Je zet dat in een tabel. Hoeveel liter is 5 van die flessen?
    - **Opties:** A) 10 L · B) 7 L · C) 2,5 L
    - **Antwoord:** 10 L  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 liter → Elke fles heeft 2 liter. Tel eens 2 liter op voor iedere fles apart. · 2,5 liter → Meer flessen betekent meer liter. Het antwoord wordt dus groter dan 2.
    - **Uitleg (Claude):** In de tabel staat 1 fles bij 2 L. Bij 5 flessen doe je 5 x 2. Dat is 10 L.
  - `G6-VERH-E01-claude-bank-002` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Voor 3 broden betaal je €6. Je vult een verhoudingstabel in. Wat hoort er in het vakje bij 6 broden?
    - **Opties:** A) €12 · B) €9 · C) €6
    - **Antwoord:** €12  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 euro → Het aantal broden wordt twee keer zo groot. Doe met de prijs precies hetzelfde. · 6 euro → Je hebt het getal 6 uit de vraag overgenomen. Kijk eerst hoeveel 6 broden meer zijn dan 3.
    - **Uitleg (Claude):** Van 3 broden naar 6 broden is keer 2. In de tabel doe je met de prijs hetzelfde. Dus €6 keer 2 is €12.

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
