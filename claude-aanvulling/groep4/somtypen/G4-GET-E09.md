# G4-GET-E09 — Meerdere sommen in een verhaal

Onze omschrijving: Combinaties van bewerkingen in context ≤100 · in onze bank: 8 items

Claude-vragen gemapt: **4** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In de wei lopen # [ding] en # [ding]. Hoeveel poten hebben ze samen?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In de wei lopen # [ding] en # [ding]. Hoeveel poten hebben ze samen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): verkeerde-bewerking (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kippen en honden hebben niet evenveel poten. Tel de kippen apart van de honden.”)
- Voorbeelden:
  - `G4-GET-E09-claude-bank-001` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** In de wei lopen 3 kippen en 2 honden. Hoeveel poten hebben ze samen?
    - **Opties:** A) 10 poten · B) 14 poten · C) 20 poten
    - **Antwoord:** 14 poten  (controle: n.v.t.)
    - **Fout-hints (Claude):** 20 poten → Kippen en honden hebben niet evenveel poten. Tel de kippen apart van de honden. · 10 poten → Kijk nog eens naar de honden. Hoeveel poten heeft één hond?
    - **Uitleg (Claude):** Drie kippen hebben 3 keer 2 is 6 poten. Twee honden hebben 2 keer 4 is 8 poten. Samen zijn dat 14 poten.

- **Hint 1 (te schrijven):** Hoeveel poten heeft een kip? En een hond?
- **Hint 2 (te schrijven):** Tel eerst alle poten van de kippen. Tel dan alle poten van de honden. Doe die twee samen.
- **Ouderzin:** Je kind rekent met groepjes van verschillende grootte en telt ze samen.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 2: Je zaagt een plank in # [ding] lange stukken. Elke keer zagen duurt # [ding]. Hoe lang ben je bezig?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Je zaagt een plank in # [ding] lange stukken. Elke zaagsnede duurt # [ding]. Hoe lang ben je bezig?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “Je zaagt een plank in # [ding] lange stukken. Elke zaagsnede duurt # [ding]. Hoe lang ben je bezig?”. Hints nakijken.
- Merge-fixlijst: #10 keer zagen (1)
- Denkfouten (Claude): getal-overgenomen (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel eerst hoe vaak je moet zagen. Dat is minder vaak dan het aantal stukken.”)
- Voorbeelden:
  - `G4-GET-E09-claude-bank-002` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** Je zaagt een plank in 5 even lange stukken. Elke keer zagen duurt 2 minuten. Hoe lang ben je bezig?
    - **Opties:** A) 12 minuten · B) 8 minuten · C) 10 minuten
    - **Antwoord:** 8 minuten  (controle: ok)
    - **Fout-hints (Claude):** 10 minuten → Tel eerst hoe vaak je moet zagen. Dat is minder vaak dan het aantal stukken. · 12 minuten → Teken de plank en zet streepjes op de zaagplekken. Tel daarna die streepjes.
    - **Uitleg (Claude):** Voor 5 stukken zaag je 4 keer. Vier keer 2 minuten is 8 minuten.

- **Hint 1 (te schrijven):** Teken de plank met de stukken. Waar moet je zagen?
- **Hint 2 (te schrijven):** Je zaagt tussen twee stukken. Tel hoe vaak je zaagt. Reken dan uit hoe lang dat samen duurt.
- **Ouderzin:** Je kind ontdekt dat je één keer minder zaagt dan het aantal stukken.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 3: Op het plein staan # [ding] en # [ding]. Hoeveel wielen zijn dat samen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Op het plein staan # [ding] en # [ding]. Hoeveel wielen zijn dat samen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–20 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): verkeerde-bewerking (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een auto heeft meer wielen dan een fiets. Tel eerst de wielen van de auto's apart.”)
- Voorbeelden:
  - `G4-GET-E09-claude-bank-003` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Op het plein staan 2 auto's en 3 fietsen. Hoeveel wielen zijn dat samen?
    - **Opties:** A) 14 wielen · B) 10 wielen · C) 8 wielen
    - **Antwoord:** 14 wielen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 wielen → Een auto heeft meer wielen dan een fiets. Tel eerst de wielen van de auto's apart. · 8 wielen → Je hebt één soort voertuig nog niet meegeteld. Kijk nog eens naar de fietsen.
    - **Uitleg (Claude):** Twee auto's hebben 2 keer 4 wielen, dat is 8. Drie fietsen hebben 3 keer 2 wielen, dat is 6. Samen zijn dat 14.

- **Hint 1 (te schrijven):** Hoeveel wielen heeft een auto? En een fiets?
- **Hint 2 (te schrijven):** Tel eerst alle wielen van de auto's. Tel dan alle wielen van de fietsen. Doe die twee samen.
- **Ouderzin:** Je kind rekent met groepjes van verschillende grootte en telt ze samen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alles even groot` (10 wielen) → Een auto heeft meer wielen dan een fiets. Tel eerst de wielen van de auto's apart.  [Claude, ok]
  - `fietsen vergeten` (8 wielen) → Je bent de fietsen vergeten. Tel hun wielen er ook bij.  [Claude, taalfix]
- Status: hints klaar

## Somtype 4: Treden zijn de stapjes van een trap. ⏎ Van de ene verdieping naar de volgende loop je # [ding]. Hoeveel treden loop je van de #e naar de #e verdieping?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Treden zijn de stapjes van een trap. ⏎ Van de ene verdieping naar de volgende loop je # [ding]. Hoeveel treden loop je van de #e naar de #e verdieping?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-TRAP-PUZZEL
- Getallenruimte: 0–100 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): tekening verplicht: drie verdiepingen met twee trappen ertussen (Didactiek §6)
- Didactiek-besluit (G4-twijfel, 1 okt): trap: tussenruimtes tellen + 2 × 12 — zie besluiten_twijfel.md
- Denkfouten (Claude): None (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel hoeveel trappen er echt tussen de 1e en de 3e verdieping zitten.”)
- Voorbeelden:
  - `G4-GET-E09-claude-bank-004` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** Treden zijn de stapjes van een trap.
Van de ene verdieping naar de volgende loop je 12 treden. Hoeveel treden loop je van de 1e naar de 3e verdieping?
    - **Opties:** A) 12 treden · B) 24 treden · C) 36 treden
    - **Antwoord:** 24 treden  (controle: ok)
    - **Fout-hints (Claude):** 36 treden → Tel hoeveel trappen er echt tussen de 1e en de 3e verdieping zitten. · 12 treden → Je gaat niet één verdieping omhoog, maar verder dan dat.
    - **Uitleg (Claude):** Van 1 naar 2 is één trap en van 2 naar 3 nog een trap. Dat zijn 2 trappen van 12 treden. Samen zijn dat 24 treden.

- **Hint 1 (te schrijven):** Hoeveel trappen loop je? Teken de verdiepingen onder elkaar.
- **Hint 2 (te schrijven):** Tussen twee verdiepingen zit één trap. Tel de trappen tussen de verdiepingen uit de vraag. Reken dan uit hoeveel treden dat samen zijn.
- **Ouderzin:** Je kind telt de trappen tussen verdiepingen en rekent uit hoeveel treden dat zijn.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
