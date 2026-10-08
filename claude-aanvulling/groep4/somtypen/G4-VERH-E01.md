# G4-VERH-E01 — Dubbel zoveel zeggen

Onze omschrijving: Eenvoudige verhoudingen verwoorden (dubbele hoeveelheid) · in onze bank: 8 items

Claude-vragen gemapt: **1** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Op een weegschaal weegt # [ding] net zo veel als # [ding]. Hoeveel pruimen wegen net zo veel als # [ding]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Op een weegschaal weegt # [ding] net zo veel als # [ding]. Hoeveel pruimen wegen net zo veel als # [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Merge-fixlijst: #44 VERH-E01 heeft maar 1 item (gelogd; geen nieuwe items gemaakt) (1)
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Elke appel hoort bij twee pruimen. Reken per appel apart.”)
- Voorbeelden:
  - `G4-VERH-E01-claude-bank-001` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** Op een weegschaal weegt 1 appel net zo veel als 2 pruimen. Hoeveel pruimen wegen net zo veel als 3 appels?
    - **Opties:** A) 6 pruimen · B) 5 pruimen · C) 3 pruimen
    - **Antwoord:** 6 pruimen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 pruimen → Elke appel hoort bij twee pruimen. Reken per appel apart. · 3 pruimen → Een pruim is lichter dan een appel. Je hebt er dus meer nodig dan 3.
    - **Uitleg (Claude):** Bij elke appel horen 2 pruimen. Bij 3 appels zijn dat 3 keer 2 is 6 pruimen.

- **Hint 1 (te schrijven):** Kijk hoeveel pruimen er bij één appel horen.
- **Hint 2 (te schrijven):** Teken de appels. Zet bij elke appel net zo veel pruimen als in de eerste zin. Tel dan alle pruimen.
- **Ouderzin:** Je kind rekent met een weegschaal uit hoeveel pruimen net zo zwaar zijn als een aantal appels.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Claudes sleutel: getallen opgeteld (tekst per item)) → Elke appel hoort bij twee pruimen. Reken per appel apart.  [Claude, ok]
  - `getal overgenomen` (Claudes sleutel: getal uit de vraag (tekst per item)) → Een pruim is lichter dan een appel. Je hebt er dus meer nodig dan 3.  [Claude, ok]
  - `andere fout` (andere fout) → Zet bij elke appel net zo veel pruimen als in de eerste zin. Tel dan alle pruimen bij elkaar.  [nieuw]
- Status: hints klaar
