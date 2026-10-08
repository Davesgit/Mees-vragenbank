# G4-MKU-E04 — Kubus, balk, bol en cilinder

Onze omschrijving: Begrippen recht/schuin/hoek/…; kubus/balk/bol/cilinder · in onze bank: 8 items

Claude-vragen gemapt: **8** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Welke ruimtelijke figuur heeft de vorm van een [voorwerp]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Welke ruimtelijke figuur heeft de vorm van een [voorwerp]?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: K5 (5) · regel: G24-ruimtefiguur
- Getallenruimte: n.v.t. · type: meerkeuze
- Merge-fixlijst: #36 dobbelsteen (1)
- Denkfouten (Claude): None (10)
- Verschillende Claude-fout-hints: 6 (meest: “Een bol is helemaal rond, zoals een bal.”)
- Voorbeelden:
  - `G4-MKU-E04-claude-bank-002` (Claude K5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welke ruimtelijke figuur heeft de vorm van een pak melk?
    - **Opties:** A) cilinder · B) balk · C) bol
    - **Antwoord:** balk  (controle: ok)
    - **Fout-hints (Claude):** bol → Een bol lijkt op een voetbal. Is dat hetzelfde? · cilinder → Een cilinder lijkt op een blik soep. Is dat hetzelfde?
    - **Uitleg (Claude):** Een pak melk heeft de vorm van een balk.
  - `G4-MKU-E04-claude-bank-004` (Claude K5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Welke ruimtelijke figuur heeft de vorm van een kaars?
    - **Opties:** A) cilinder · B) bol · C) balk
    - **Antwoord:** cilinder  (controle: ok)
    - **Fout-hints (Claude):** bol → Een bol is helemaal rond, zoals een bal. · balk → Een balk is lang en heeft rechte kanten, zoals een schoenendoos.
    - **Uitleg (Claude):** Een kaars heeft de vorm van een cilinder.

- **Hint 1 (te schrijven):** Denk aan de vorm van het voorwerp. Kan het rollen? Heeft het platte kanten?
- **Hint 2 (te schrijven):** Zijn alle kanten even groot? Is het helemaal rond, of rond met twee platte kanten?
- **Ouderzin:** Je kind zoekt welke ruimtefiguur bij een voorwerp past.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere figuur` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere fout` (andere fout) → Kijk nog eens naar de vorm. Kan het rollen? Heeft het platte kanten?  [nieuw]
- Status: hints klaar

## Somtype 2: [ruimtefiguur] Hoe heet deze ruimtelijke figuur?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[ruimtefiguur] Hoe heet deze ruimtelijke figuur?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: K5 (3) · regel: G24-ruimtefiguur
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (3 items): tekening van een balk nodig: de Claude-tekenaar kent geen soort 'ruimtefiguur' (Visual: nodig) · tekening van een bol nodig: de Claude-tekenaar kent geen soort 'ruimtefiguur' (Visual: nodig) · tekening van een cilinder nodig: de Claude-tekenaar kent geen soort 'ruimtefiguur' (Visual: nodig)
- Denkfouten (Claude): None (6)
- Verschillende Claude-fout-hints: 4 (meest: “Een bol is helemaal rond, zoals een bal.”)
- Voorbeelden:
  - `G4-MKU-E04-claude-bank-007` (Claude K5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Hoe heet deze ruimtelijke figuur?
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "cilinder"}`
    - **Opties:** A) bol · B) balk · C) cilinder
    - **Antwoord:** cilinder  (controle: ok)
    - **Fout-hints (Claude):** bol → Een bol is helemaal rond, zoals een bal. · balk → Een balk is lang en heeft rechte kanten, zoals een schoenendoos.
    - **Uitleg (Claude):** Dit is een cilinder. Denk aan een blik soep.
  - `G4-MKU-E04-claude-bank-008` (Claude K5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Hoe heet deze ruimtelijke figuur?
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "bol"}`
    - **Opties:** A) bol · B) kubus · C) balk
    - **Antwoord:** bol  (controle: ok)
    - **Fout-hints (Claude):** kubus → Een kubus ziet er anders uit: denk aan een dobbelsteen. · balk → Een balk is lang en heeft rechte kanten, zoals een schoenendoos.
    - **Uitleg (Claude):** Dit is een bol. Denk aan een voetbal.

- **Hint 1 (te schrijven):** Kijk goed naar de figuur. Kan hij rollen? Heeft hij platte kanten?
- **Hint 2 (te schrijven):** Denk aan dingen die je kent, zoals een bal, een blik, een doos of een dobbelsteen. Op welk ding lijkt deze figuur?
- **Ouderzin:** Je kind herkent en benoemt een ruimtefiguur.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere figuur` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere fout` (andere fout) → Kijk nog eens naar de vorm. Kan hij rollen? Heeft hij platte kanten?  [nieuw]
- Status: hints klaar
