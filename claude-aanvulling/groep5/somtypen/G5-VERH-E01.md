# G5-VERH-E01 — Een kwart van iets

Onze omschrijving: ‘Een kwart’ van geheel én van hoeveelheid · in onze bank: 8 items

Claude-vragen gemapt: **3** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] zitten # [ding]. Een kwart ervan is groen. Hoeveel groene knikkers zijn er?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In [plek] liggen # [ding]. Een kwart ervan is groen. Hoeveel groene botten zijn er?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B2 (1) · regel: G5-B02-deel-van
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): verkeerde-bewerking (1), omgekeerd-gedeeld (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is het deel dat níét groen is. Lees de vraag nog eens.”)
- Voorbeelden:
  - `G5-VERH-E01-claude-bank-001` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de doos zitten 76 knikkers. Een kwart ervan is groen. Hoeveel groene knikkers zijn er?
    - **Antwoord:** 19  (controle: ok)
    - **Fout-hints (Claude):** 57 → Dat is het deel dat níét groen is. Lees de vraag nog eens. · 76 → Deel door de noemer (4), niet door de teller.
    - **Uitleg (Claude):** Eerst 1/4: 76 : 4 = 19. Dan 1 keer: 1 × 19 = 19.

- **Hint 1 (te schrijven):** Een kwart is één van vier gelijke delen. Verdeel de knikkers in vier gelijke groepjes.
- **Hint 2 (te schrijven):** Hoeveel knikkers zitten er in één groepje? Je kunt ook eerst de helft nemen, en daarvan weer de helft.
- **Ouderzin:** Je kind rekent uit hoeveel een kwart van een aantal is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alle knikkers` (fout = getal1) → Dat zijn alle knikkers. Je zoekt een kwart: verdeel ze in vier gelijke groepjes. Hoeveel zitten er in één groepje?  [nieuw]
  - `drie kwart` (Claudes sleutel: verkeerde-bewerking) → Dat is drie kwart van de knikkers. Je zoekt één kwart: één van de vier gelijke groepjes.  [Claude, taalfix]
  - `bijna` (fout = antwoord ± 1) → Bijna! Reken het na: vier groepjes van jouw antwoord moeten samen alle knikkers zijn.  [nieuw]
  - `andere fout` (andere fout) → Een kwart is één van vier gelijke delen. Deel het aantal knikkers door vier.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'In [plek] liggen # [ding]. Een kwart ervan is groen. Hoeveel groene botten zijn er?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 2: [groepjes] Er zijn # [ding]. Kleur drie kwart van de koekjes.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[groepjes] Er zijn # [ding]. Kleur drie kwart van de koekjes.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B2 (1) · regel: D-DRIEKWART-G5
- Getallenruimte: 0–10 · type: kale
- Hint-richting: Drie kwart in woorden, geen 3/4. Eerst een kwart van 8 (8 : 4 = 2), dan 3 keer zoveel. Zet '8 : 4' alleen in de hint, niet in de opgave.
- Denkfouten (Claude): None (1)
- Verschillende Claude-fout-hints: 1 (meest: “2 is maar één deel. Je hebt 3 delen nodig.”)
- Voorbeelden:
  - `G5-VERH-E01-claude-bank-003` (Claude B2, gegenereerd, niveau 2 → kritisch)
    - **Opgave:** Er zijn 8 koekjes. Kleur drie kwart van de koekjes.
    - **Tekening:** `{"soort": "groepjes", "aantal": 8, "kleurbaar": true, "perrij": 4}`
    - **UI:** balk kleuren
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 2 → 2 is maar één deel. Je hebt 3 delen nodig.
    - **Uitleg (Claude):** Eerst 8 : 4 = 2, dat is één deel. Dan 3 delen: 3 × 2 = 6.

- **Hint 1 (te schrijven):** Een kwart is één van vier gelijke delen. Verdeel de koekjes in vier gelijke groepjes.
- **Hint 2 (te schrijven):** Verdeel de koekjes in vier gelijke groepjes. Drie kwart is drie van die groepjes. Kleur de koekjes van drie groepjes.
- **Ouderzin:** Je kind kleurt drie kwart van een aantal koekjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alles gekleurd` (fout = getal1) → Je hebt alle koekjes gekleurd. Drie kwart is drie van de vier groepjes: één groepje blijft over.  [nieuw]
  - `één kwart` (fout = een kwart van getal1) → Je hebt één kwart gekleurd: één groepje. Drie kwart is drie van de vier groepjes.  [nieuw]
  - `de helft` (fout = de helft van getal1) → Je hebt de helft gekleurd: twee van de vier groepjes. Drie kwart is drie van de vier groepjes.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één koekje te veel. Verdeel de koekjes in vier gelijke groepjes en kleur drie groepjes.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één koekje te weinig. Verdeel de koekjes in vier gelijke groepjes en kleur drie groepjes.  [nieuw]
  - `andere fout` (andere fout) → Verdeel de koekjes in vier gelijke groepjes. Kleur de koekjes van drie groepjes.  [nieuw]
- Status: hints klaar

## Somtype 3: [groepjes] Er zijn # [ding]. Kleur een kwart van de koekjes.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[groepjes] Er zijn # [ding]. Kleur een kwart van de koekjes.” (koppeling: claudeId)
- Items: **1** · Claude-doelen: B2 (1) · regel: G5-B02-deel-van
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-VERH-E01-claude-bank-002` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Er zijn 8 koekjes. Kleur een kwart van de koekjes.
    - **Tekening:** `{"soort": "groepjes", "aantal": 8, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Eerst 8 : 4 = 2, dat is één deel. Dan 1 delen: 1 × 2 = 2.

- **Hint 1 (te schrijven):** Een kwart is één van vier gelijke delen. Verdeel de koekjes in vier gelijke groepjes.
- **Hint 2 (te schrijven):** Kleur de koekjes van één groepje.
- **Ouderzin:** Je kind kleurt een kwart van een aantal koekjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alles gekleurd` (fout = getal1) → Je hebt alle koekjes gekleurd. Een kwart is één van vier gelijke delen. Kleur alleen de koekjes van één groepje.  [nieuw]
  - `drie kwart` (fout = drie kwart van getal1) → Je hebt drie kwart gekleurd: drie van de vier groepjes. Een kwart is maar één groepje.  [nieuw]
  - `de helft` (fout = de helft van getal1) → Je hebt de helft gekleurd: twee van de vier groepjes. Een kwart is maar één groepje.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één koekje te veel. Verdeel de koekjes in vier gelijke groepjes en kleur één groepje.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één koekje te weinig. Verdeel de koekjes in vier gelijke groepjes en kleur één groepje.  [nieuw]
  - `andere fout` (andere fout) → Verdeel de koekjes in vier gelijke groepjes. Kleur de koekjes van één groepje.  [nieuw]
- Status: hints klaar
