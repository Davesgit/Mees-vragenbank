# G5-GET-E09 — Meerdere sommen tot duizend

Onze omschrijving: Relaties tussen bewerkingen; combinaties in context ≤1000 · in onze bank: 8 items

Claude-vragen gemapt: **35** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Wisselgeld: [wie] koopt # [ding] van €# per stuk en betaalt met €#. Hoeveel terug?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Wisselgeld: [wie] koopt # [ding] van €# per stuk en betaalt met €#. Hoeveel terug?” (koppeling: claudeId)
- Items: **27** · Claude-doelen: T8 (27) · regel: G8-T8-meerstaps
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (27), verkeerde-bewerking (27), optellen-ipv-vermenigvuldigen (27)
- Verschillende Claude-fout-hints: 33 (meest: “Dat is wat het kost. Gevraagd is wat hij terugkrijgt.”)
- Voorbeelden:
  - `G5-GET-E09-claude-bank-naar-003` (Claude T8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Ayoub koopt 4 schriften van €3 per stuk en betaalt met €20. Hoeveel geld krijgt hij terug?
    - **Antwoord:** €8  (controle: n.v.t.)
    - **Fout-hints (Claude):** €12 → Dat is wat het kost. Gevraagd is wat hij terugkrijgt. · €97 → Het zijn 4 stickers: reken eerst de totaalprijs uit. · €93 → 4 keer €3: vermenigvuldigen.
    - **Uitleg (Claude):** Stap 1: 4 × €3 = €12. Stap 2: €20 − €12 = €8 terug.
  - `G5-GET-E09-claude-bank-naar-020` (Claude T8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Mila koopt 5 boeken van €7 per stuk en betaalt met €50. Hoeveel geld krijgt ze terug?
    - **Antwoord:** €15  (controle: n.v.t.)
    - **Fout-hints (Claude):** €35 → Dat is wat het kost. Gevraagd is wat hij terugkrijgt. · €93 → Het zijn 5 stickers: reken eerst de totaalprijs uit. · €88 → 5 keer €7: vermenigvuldigen.
    - **Uitleg (Claude):** Stap 1: 5 × €7 = €35. Stap 2: €50 − €35 = €15 terug.

- **Hint 1 (te schrijven):** Reken eerst uit wat alles samen kost. Elk ding kost evenveel: dat is een keersom, het aantal keer de prijs.
- **Hint 2 (te schrijven):** Haal dat dan af van het geld waarmee je betaalt.
- **Ouderzin:** Je kind rekent uit hoeveel geld het terugkrijgt als het een paar dezelfde dingen koopt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `wat het kost` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is wat alles samen kost. De vraag is hoeveel je terugkrijgt. Haal het van het geld waarmee je betaalt af.  [Claude, taalfix]
  - `één ding betaald` (Claudes sleutel: verkeerde-bewerking) → Je hebt de prijs van één ding eraf gehaald. Er worden er meer gekocht. Reken eerst uit wat ze samen kosten.  [Claude, taalfix]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt het aantal en de prijs opgeteld. Elk ding kost evenveel: dat is een keersom.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst uit wat alles samen kost: het aantal keer de prijs. Haal dat dan af van het geld waarmee je betaalt.  [nieuw]
- Status: hints klaar

## Somtype 2: Twee stappen: # keer # [ding], daarna # eraf. Hoeveel nog?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Twee stappen: # keer # [ding], daarna # eraf. Hoeveel nog?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T8 (5), merge-generator G5 ronde 9 (#235) (3) · regel: G8-T8-meerstaps, G5-r9 #235 generator
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (8), optellen-ipv-vermenigvuldigen (8), verkeerde-bewerking (5)
- Verschillende Claude-fout-hints: 6 (meest: “Dat is hoeveel het er samen zijn. Er gaan er nog een paar weg.”)
- Voorbeelden:
  - `G5-GET-E09-claude-bank-naar-001` (Claude T8, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 3 kinderen hebben elk 12 stickers. Ze plakken er samen 7 in een album. Hoeveel stickers hebben ze nog los?
    - **Antwoord:** 29  (controle: n.v.t.)
    - **Fout-hints (Claude):** 36 → Je hebt de tweede stap vergeten: er gaan er nog weg. · 15 → Eerst het totaal uitrekenen met de keersom, en dan pas het weggehaalde eraf. · 8 → Elk evenveel: het totaal is een keersom, geen plussom.
    - **Uitleg (Claude):** Stap 1: 3 × 12 = 36. Stap 2: 36 − 7 = 29.
  - `G5-GET-E09-merge-gen-001` (Claude merge-generator G5 ronde 9 (#235), None, niveau 2 → toepassen)
    - **Opgave:** 4 kinderen hebben elk 9 kaartjes. Ze geven er samen 6 weg. Hoeveel kaartjes hebben ze nog?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** 36 → Je hebt de tweede stap vergeten: er gaan er nog weg. · 15 → Eerst het totaal uitrekenen met de keersom, en dan pas het weggehaalde eraf. · 8 → Elk evenveel: het totaal is een keersom, geen plussom.
    - **Uitleg (Claude):** Stap 1: 4 × 9 = 36. Stap 2: 36 − 6 = 30.

- **Hint 1 (te schrijven):** Reken eerst uit hoeveel het er samen zijn. Het is steeds evenveel: dat is een keersom.
- **Hint 2 (te schrijven):** Haal er daarna af wat weggaat.
- **Ouderzin:** Je kind rekent een verhaaltje in twee stappen uit: eerst een keersom, dan iets eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tweede stap vergeten` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is hoeveel het er eerst waren. Er gaan er nog een paar af. Haal die er nog af.  [Claude, taalfix]
  - `stappen door elkaar` (Claudes sleutel: verkeerde-bewerking) → Reken eerst uit hoeveel het er samen zijn met een keersom. Haal er daarna af wat weggaat.  [Claude, taalfix]
  - `opgeteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt opgeteld. Het is steeds evenveel: dat is een keersom. Reken eerst het totaal uit, en haal er daarna af wat weggaat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst het totaal uit met een keersom. Haal er daarna af wat weggaat.  [nieuw]
- Status: hints klaar
