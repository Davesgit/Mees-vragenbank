# G7-VBN-04 — Staaf- en cirkeldiagram

Onze omschrijving: Staaf-/cirkeldiagram · in onze bank: 8 items

Claude-vragen gemapt: **36** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [balk kleuren] Tabel: [rij]. Maak de staaf van [naam]: elk stukje van de balk is #.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[balk kleuren] Tabel: [rij]. Maak de staaf van [naam]: elk stukje van de balk is #.” (koppeling: claudeId)
- Items: **12** · Claude-doelen: G5 (12) · regel: G7-D01-staafdiagram
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (8)
- Verschillende Claude-fout-hints: 1 (meest: “Elk stukje is 5, niet 1.”)
- Voorbeelden:
  - `G7-VBN-04-claude-bank-004` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tabel: mei 10, juni 30, juli 40, aug 45. Maak de staaf van juni: elk stukje van de balk is 5.
    - **UI:** balk kleuren
    - **Antwoord:** 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 → Elk stukje is 5, niet 1.
    - **Uitleg (Claude):** juni heeft 30. Elk stukje is 5, dus 30 : 5 = 6 stukjes.
  - `G7-VBN-04-claude-bank-006` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tabel: mei 40, juni 50, juli 30, aug 40. Maak de staaf van juni: elk stukje van de balk is 5.
    - **UI:** balk kleuren
    - **Antwoord:** 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** juni heeft 50. Elk stukje is 5, dus 50 : 5 = 10 stukjes.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: [tabel] Je maakt een staafdiagram van deze tabel. Welke staaf wordt het hoogst?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[tabel] Je maakt een staafdiagram van deze tabel. Welke staaf wordt het hoogst?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: G5 (9) · regel: G7-D01-staafdiagram
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (18)
- Verschillende Claude-fout-hints: 18 (meest: “wo heeft 30. Is er een groter getal in de tabel?”)
- Voorbeelden:
  - `G7-VBN-04-claude-bank-033` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je maakt een staafdiagram van deze tabel over het aantal bezoekers van het zwembad. Welke staaf wordt het hoogst?
    - **Tekening:** `{"rijen": [{"naam": "bezoekers", "waarden": [60, 30, 30, 80, 50]}], "soort": "tabel", "kolommen": ["", "ma", "di", "wo", "do", "vr"]}`
    - **Opties:** A) vr · B) do · C) wo
    - **Antwoord:** do  (controle: ok)
    - **Fout-hints (Claude):** wo → wo heeft 30. Is er een groter getal in de tabel? · vr → vr heeft 50. Is er een groter getal in de tabel?
    - **Uitleg (Claude):** De hoogste staaf hoort bij het grootste getal in de tabel: 80 bij do.
  - `G7-VBN-04-claude-bank-030` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je maakt een staafdiagram van deze tabel over het aantal verkochte ijsjes. Welke staaf wordt het hoogst?
    - **Tekening:** `{"rijen": [{"naam": "ijsjes", "waarden": [5, 30, 25, 5, 30]}], "soort": "tabel", "kolommen": ["", "mei", "juni", "juli", "aug", "sept"]}`
    - **Opties:** A) juni · B) aug · C) juli
    - **Antwoord:** juni  (controle: n.v.t.)
    - **Fout-hints (Claude):** aug → aug heeft 5. Is er een groter getal in de tabel? · juli → juli heeft 25. Is er een groter getal in de tabel?
    - **Uitleg (Claude):** De hoogste staaf hoort bij het grootste getal in de tabel: 30 bij juni.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: [tabel] Je maakt een staafdiagram van deze tabel. De as loopt in stappen van #. Tot welk tiental moet de as minstens lopen, zodat elke staaf past?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[tabel] Je maakt een staafdiagram van deze tabel. De as loopt in stappen van #. Tot welk tiental moet de as minstens lopen, zodat elke staaf past?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: G5 (8) · regel: G7-D01-staafdiagram
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (16)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar het grootste getal in de tabel: past die staaf nog op deze as?”)
- Voorbeelden:
  - `G7-VBN-04-claude-bank-017` (Claude G5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je tekent een staafdiagram van deze tabel over de regen per week in millimeters. De as loopt in stappen van 10. Tot welk tiental moet de as minstens lopen, zodat elke staaf past?
    - **Tekening:** `{"rijen": [{"naam": "mm", "waarden": [20, 10, 70, 50]}], "soort": "tabel", "kolommen": ["", "week 1", "week 2", "week 3", "week 4"]}`
    - **Opties:** A) 70 · B) 60 · C) 80
    - **Antwoord:** 70  (controle: n.v.t.)
    - **Fout-hints (Claude):** 60 → Kijk naar het grootste getal in de tabel: past die staaf nog op deze as? · 80 → Deze as is langer dan nodig. Welk tiental zit het dichtst boven het grootste getal?
    - **Uitleg (Claude):** Het grootste getal in de tabel is 70. Het eerste tiental daarboven (of precies 70 als dat een tiental is) is 70. Verder hoeft de as niet te lopen.
  - `G7-VBN-04-claude-bank-018` (Claude G5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je tekent een staafdiagram van deze tabel over het aantal verkochte ijsjes. De as loopt in stappen van 10. Tot welk tiental moet de as minstens lopen, zodat elke staaf past?
    - **Tekening:** `{"rijen": [{"naam": "ijsjes", "waarden": [15, 20, 40, 40, 25]}], "soort": "tabel", "kolommen": ["", "mei", "juni", "juli", "aug", "sept"]}`
    - **Opties:** A) 40 · B) 30 · C) 50
    - **Antwoord:** 40  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 → Kijk naar het grootste getal in de tabel: past die staaf nog op deze as? · 50 → Deze as is langer dan nodig. Welk tiental zit het dichtst boven het grootste getal?
    - **Uitleg (Claude):** Het grootste getal in de tabel is 40. Het eerste tiental daarboven (of precies 40 als dat een tiental is) is 40. Verder hoeft de as niet te lopen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: [tabel] Je maakt een staafdiagram van deze tabel. Elk streepje op de as staat voor #. Hoeveel streepjes hoog wordt de staaf van [naam]?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[tabel] Je maakt een staafdiagram van deze tabel. Elk streepje op de as staat voor #. Hoeveel streepjes hoog wordt de staaf van [naam]?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: G5 (7) · regel: G7-D01-staafdiagram
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (7), een-ernaast (7)
- Verschillende Claude-fout-hints: 10 (meest: “Elk streepje is 5, niet 1. Deel de waarde door 5.”)
- Voorbeelden:
  - `G7-VBN-04-claude-bank-025` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je maakt een staafdiagram van deze tabel over de regen per week in millimeters. Elk streepje op de as staat voor 2. Hoeveel streepjes hoog wordt de staaf van week 1?
    - **Tekening:** `{"rijen": [{"naam": "mm", "waarden": [12, 16, 6, 8]}], "soort": "tabel", "kolommen": ["", "week 1", "week 2", "week 3", "week 4"]}`
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 12 → Elk streepje is 2, niet 1. Deel de waarde door 2. · 7 → Reken na. 12 gedeeld door 2.
    - **Uitleg (Claude):** week 1 heeft 12. Elk streepje is 2, dus 12 : 2 = 6 streepjes hoog.
  - `G7-VBN-04-claude-bank-026` (Claude G5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je maakt een staafdiagram van deze tabel over de regen per week in millimeters. Elk streepje op de as staat voor 5. Hoeveel streepjes hoog wordt de staaf van week 1?
    - **Tekening:** `{"rijen": [{"naam": "mm", "waarden": [25, 15, 25, 40]}], "soort": "tabel", "kolommen": ["", "week 1", "week 2", "week 3", "week 4"]}`
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 25 → Elk streepje is 5, niet 1. Deel de waarde door 5. · 6 → Reken na. 25 gedeeld door 5.
    - **Uitleg (Claude):** week 1 heeft 25. Elk streepje is 5, dus 25 : 5 = 5 streepjes hoog.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
