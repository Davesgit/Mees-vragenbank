# G5-GET-E04 — Heel, half, kwart en deel

Onze omschrijving: Begrippen heel/half/kwart/deel–geheel (Getallen; VERH voor verhouding) · in onze bank: 8 items

Claude-vragen gemapt: **4** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [balk] Kleur drie kwart van de balk.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[balk] Kleur drie kwart van de balk.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B1 (1) · regel: G5-B01-breuk
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): None (1)
- Verschillende Claude-fout-hints: 1 (meest: “Kleur 3 stukken, niet 1.”)
- Voorbeelden:
  - `G5-GET-E04-claude-bank-001` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur drie kwart van de balk.
    - **Tekening:** `{"soort": "balk", "delen": 4, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 1 → Kleur 3 stukken, niet 1.
    - **Uitleg (Claude):** De balk heeft 4 gelijke stukken. 3/4 betekent: 3 van die 4 stukken.

- **Hint 1 (te schrijven):** De balk is verdeeld in vier gelijke stukken. Elk stuk is een kwart.
- **Hint 2 (te schrijven):** Drie kwart is drie keer een kwart. Hoeveel stukken kleur je dan?
- **Ouderzin:** Je kind kleurt drie kwart van een balk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een kwart gekleurd` (fout = antwoord − 2) → Je hebt één stuk gekleurd: dat is een kwart. Drie kwart is drie keer zo veel.  [nieuw]
  - `andere fout` (andere fout) → De balk heeft vier gelijke stukken. Een kwart is één stuk. Drie kwart is drie keer een kwart.  [nieuw]
- Status: hints klaar

## Somtype 2: [balk] Kleur een kwart van de balk.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[balk] Kleur een kwart van de balk.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B1 (1) · regel: G5-B01-breuk
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): None (1)
- Verschillende Claude-fout-hints: 1 (meest: “Kleur 1 stuk, niet 3.”)
- Voorbeelden:
  - `G5-GET-E04-claude-bank-002` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur een kwart van de balk.
    - **Tekening:** `{"soort": "balk", "delen": 4, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 3 → Kleur 1 stuk, niet 3.
    - **Uitleg (Claude):** De balk heeft 4 gelijke stukken. 1/4 betekent: 1 van die 4 stukken.

- **Hint 1 (te schrijven):** De balk is verdeeld in vier gelijke stukken.
- **Hint 2 (te schrijven):** Een kwart is één van de vier gelijke stukken.
- **Ouderzin:** Je kind kleurt een kwart van een balk.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `drie kwart gekleurd` (fout = antwoord + 2) → Je hebt drie stukken gekleurd: dat is drie kwart. Een kwart is veel minder.  [nieuw]
  - `andere fout` (andere fout) → De balk heeft vier gelijke stukken. Een kwart is één zo'n stuk.  [nieuw]
- Status: hints klaar

## Somtype 3: [wie] delen een pannenkoek in # gelijke stukken. [wie] eet er # op. Welk deel is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[wie] delen een pannenkoek in # gelijke stukken. [wie] eet er # op. Welk deel is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B1 (1) · regel: G5-B01-breuk
- Getallenruimte: 0–10 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 1 (meest: “Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op?”)
- Voorbeelden:
  - `G5-GET-E04-claude-bank-003` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** De kinderen delen een pannenkoek in 4 gelijke stukken. Een kind eet er 1 op. Welk deel is dat?
    - **Opties:** A) de helft · B) een kwart · C) drie kwart
    - **Antwoord:** een kwart  (controle: ok)
    - **Fout-hints (Claude):** de helft → Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op? · drie kwart → Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op?
    - **Uitleg (Claude):** De noemer (onder) zegt in hoeveel stukken het geheel is verdeeld: 4. De teller (boven) zegt hoeveel stukken je neemt: 1. Dus 1/4.

- **Hint 1 (te schrijven):** In hoeveel gelijke stukken is de pannenkoek verdeeld? Hoeveel stukken worden er opgegeten?
- **Hint 2 (te schrijven):** Er zijn vier stukken en er wordt er één opgegeten. Hoe heet één van de vier gelijke stukken?
- **Ouderzin:** Je kind zegt welk deel van een pannenkoek is opgegeten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de helft` (de helft) → De helft is twee van de vier stukken. Er wordt maar één stuk opgegeten.  [nieuw]
  - `drie kwart` (drie kwart) → Drie kwart is drie van de vier stukken. Er wordt maar één stuk opgegeten.  [nieuw]
  - `andere fout` (andere fout) → De pannenkoek is in vier gelijke stukken verdeeld. Er wordt één stuk opgegeten. Welk deel is één van de vier?  [nieuw]
- Status: hints klaar

## Somtype 4: [wie] delen een taart in # gelijke stukken. [wie] eet er # op. Welk deel is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[wie] delen een taart in # gelijke stukken. [wie] eet er # op. Welk deel is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B1 (1) · regel: G5-B01-breuk
- Getallenruimte: 0–10 · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 1 (meest: “Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op?”)
- Voorbeelden:
  - `G5-GET-E04-claude-bank-004` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** De kinderen delen een taart in 4 gelijke stukken. Een kind eet er 1 op. Welk deel is dat?
    - **Opties:** A) de helft · B) een kwart · C) drie kwart
    - **Antwoord:** een kwart  (controle: ok)
    - **Fout-hints (Claude):** de helft → Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op? · drie kwart → Tel in hoeveel gelijke stukken het eten is verdeeld. Hoeveel stukken eet het kind op?
    - **Uitleg (Claude):** De noemer (onder) zegt in hoeveel stukken het geheel is verdeeld: 4. De teller (boven) zegt hoeveel stukken je neemt: 1. Dus 1/4.

- **Hint 1 (te schrijven):** In hoeveel gelijke stukken is de taart verdeeld? Hoeveel stukken worden er opgegeten?
- **Hint 2 (te schrijven):** Er zijn vier stukken en er wordt er één opgegeten. Hoe heet één van de vier gelijke stukken?
- **Ouderzin:** Je kind zegt welk deel van een taart is opgegeten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de helft` (de helft) → De helft is twee van de vier stukken. Er wordt maar één stuk opgegeten.  [nieuw]
  - `drie kwart` (drie kwart) → Drie kwart is drie van de vier stukken. Er wordt maar één stuk opgegeten.  [nieuw]
  - `andere fout` (andere fout) → De taart is in vier gelijke stukken verdeeld. Er wordt één stuk opgegeten. Welk deel is één van de vier?  [nieuw]
- Status: hints klaar
