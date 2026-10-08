# G5-MEET-E02 — Omtrek van vierkant en rechthoek

Onze omschrijving: Omtrek vierkant/rechthoek (rooster/gegeven zijden); grillig bij benadering · in onze bank: 8 items

Claude-vragen gemapt: **282** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een rechthoek is # cm lang en # cm breed. Hoeveel cm is de omtrek?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een rechthoek is # cm lang en # cm breed. Hoeveel cm is de omtrek?” (koppeling: claudeId)
- Items: **274** · Claude-doelen: M15 (274) · regel: G5-M04-omtrek
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (261), deel-vergeten-bij-splitsen (150), omtrek-oppervlakte-verwisseld (137)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G5-MEET-E02-claude-bank-085` (Claude M15, bank, niveau 3 → toepassen)
    - **Opgave:** Een rechthoek is 4 cm lang en 2 cm breed. Hoeveel cm is de omtrek?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 10 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-MEET-E02-claude-bank-044` (Claude M15, bank, niveau 3 → toepassen)
    - **Opgave:** Een rechthoek is 19 cm lang en 5 cm breed. Hoeveel cm is de omtrek?
    - **Antwoord:** 48  (controle: ok)
    - **Fout-hints (Claude):** 95 → Omtrek is de lijn eromheen (optellen). Oppervlakte is wat erbinnen zit (lengte keer breedte). · 67 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** De omtrek is de lijn om de rechthoek heen. Hoeveel zijden (kanten) heeft een rechthoek?
- **Hint 2 (te schrijven):** Tel alle vier de zijden bij elkaar op: twee keer de lengte en twee keer de breedte.
- **Ouderzin:** Je kind rekent de omtrek van een rechthoek uit: alle zijden bij elkaar.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `twee zijden` (fout = getal1 + getal2) → Je hebt de lengte en de breedte één keer opgeteld. Maar er zijn vier zijden: twee lange en twee korte.  [nieuw]
  - `oppervlakte` (fout = getal1 × getal2) → Heb je keer gedaan? Dan heb je de oppervlakte: wat erbinnen zit. De omtrek is de lijn eromheen: tel de zijden op.  [nieuw]
  - `korte zijde vergeten` (fout = antwoord − getal2) → Dat is te weinig. Je bent een korte zijde vergeten. Tel alle vier de zijden: twee lange en twee korte.  [nieuw]
  - `lange zijde vergeten` (fout = antwoord − getal1) → Dat is te weinig. Je bent een lange zijde vergeten. Tel alle vier de zijden: twee lange en twee korte.  [nieuw]
  - `lange zijde te veel` (fout = antwoord + getal1) → Dat is te veel. Je hebt een lange zijde te veel geteld. Er zijn twee lange en twee korte zijden.  [nieuw]
  - `korte zijde te veel` (fout = antwoord + getal2) → Dat is te veel. Je hebt een korte zijde te veel geteld. Er zijn twee lange en twee korte zijden.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de vier zijden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de vier zijden nog eens bij elkaar.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Tel alle vier de zijden bij elkaar: twee lange en twee korte.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Tel alle vier de zijden bij elkaar: twee lange en twee korte.  [nieuw]
  - `andere fout` (andere fout) → De omtrek is de lijn eromheen. Tel alle vier de zijden bij elkaar: twee keer de lengte en twee keer de breedte.  [nieuw]
- Status: hints klaar

## Somtype 2: Om een [veld] van # bij # meter komt een hek. Hoeveel meter hek is dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Om een [veld] van # bij # meter komt een hek. Hoeveel meter hek is dat?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M15 (8) · regel: G5-M04-omtrek
- Getallenruimte: 0–100, 0–20 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (16), omtrek-oppervlakte-verwisseld (8)
- Verschillende Claude-fout-hints: 3 (meest: “Dat is de oppervlakte: wat erbinnen zit. Een hek staat eromheen, dus tel de zijden op.”)
- Voorbeelden:
  - `G5-MEET-E02-claude-bank-278` (Claude M15, gegenereerd, niveau 1 → basis)
    - **Opgave:** Om een tuin van 11 bij 8 meter komt een hek. Hoeveel meter hek is dat?
    - **Antwoord:** 38  (controle: ok)
    - **Fout-hints (Claude):** 88 → Dat is de oppervlakte: wat erbinnen zit. Een hek staat eromheen, dus tel de zijden op. · 19 → Een rechthoek heeft vier zijden. Je hebt er maar twee geteld. · 30 → Tel alle vier de zijden: twee lange en twee korte.
    - **Uitleg (Claude):** Omtrek is alle zijden bij elkaar. 11 + 8 + 11 + 8 = 38 meter. Of: 2 × (11 + 8) = 38.
  - `G5-MEET-E02-claude-bank-280` (Claude M15, gegenereerd, niveau 1 → basis)
    - **Opgave:** Om een tuin van 6 bij 4 meter komt een hek. Hoeveel meter hek is dat?
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 24 → Dat is de oppervlakte: wat erbinnen zit. Een hek staat eromheen, dus tel de zijden op. · 10 → Een rechthoek heeft vier zijden. Je hebt er maar twee geteld. · 16 → Tel alle vier de zijden: twee lange en twee korte.
    - **Uitleg (Claude):** Omtrek is alle zijden bij elkaar. 6 + 4 + 6 + 4 = 20 meter. Of: 2 × (6 + 4) = 20.

- **Hint 1 (te schrijven):** Het hek gaat er helemaal omheen. Dat is de omtrek. Hoeveel kanten zijn er?
- **Hint 2 (te schrijven):** Tel alle vier de kanten bij elkaar op: twee lange en twee korte.
- **Ouderzin:** Je kind rekent uit hoe lang een hek om een rechthoekig stuk grond is (de omtrek).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `twee zijden` (fout = getal1 + getal2) → Je hebt de lengte en de breedte één keer opgeteld. Maar er zijn vier kanten: twee lange en twee korte.  [nieuw]
  - `oppervlakte` (fout = getal1 × getal2) → Heb je keer gedaan? Dan heb je de oppervlakte: wat erbinnen zit. De omtrek is de lijn eromheen: tel de kanten op.  [nieuw]
  - `korte zijde vergeten` (fout = antwoord − getal2) → Dat is te weinig. Je bent een korte kant vergeten. Tel alle vier de kanten: twee lange en twee korte.  [nieuw]
  - `lange zijde vergeten` (fout = antwoord − getal1) → Dat is te weinig. Je bent een lange kant vergeten. Tel alle vier de kanten: twee lange en twee korte.  [nieuw]
  - `lange zijde te veel` (fout = antwoord + getal1) → Dat is te veel. Je hebt een lange kant te veel geteld. Er zijn twee lange en twee korte kanten.  [nieuw]
  - `korte zijde te veel` (fout = antwoord + getal2) → Dat is te veel. Je hebt een korte kant te veel geteld. Er zijn twee lange en twee korte kanten.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de vier kanten nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de vier kanten nog eens bij elkaar.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Tel alle vier de kanten bij elkaar: twee lange en twee korte.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Tel alle vier de kanten bij elkaar: twee lange en twee korte.  [nieuw]
  - `andere fout` (andere fout) → De omtrek is de lijn eromheen. Tel alle vier de kanten bij elkaar: twee keer de lengte en twee keer de breedte.  [nieuw]
- Status: hints klaar
