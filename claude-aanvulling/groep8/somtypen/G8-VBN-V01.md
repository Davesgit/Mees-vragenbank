# G8-VBN-V01 — Assen, coördinaten en grafieken herhalen

Onze omschrijving: Assen; coördinaten; lijngrafiek; diagrammen (eind G7 / G7-VBN-01…05) · in onze bank: 8 items

Claude-vragen gemapt: **16** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [vak(ken) aantikken op rooster] Zet de stip op (#, #).

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[vak(ken) aantikken op rooster] Zet de stip op (#, #).” (koppeling: claudeId)
- Items: **12** · Claude-doelen: K7 (12) · regel: G8-K7-coordinaten
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): None (11)
- Verschillende Claude-fout-hints: 1 (meest: “Het eerste getal is opzij, het tweede omhoog.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-003` (Claude K7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de stip op (1, 0).
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** 1  (controle: n.v.t.)
    - **Fout-hints (Claude):** 0,1 → Het eerste getal is opzij, het tweede omhoog.
    - **Uitleg (Claude):** Eerst 1 opzij (naar rechts), dan 0 omhoog.
  - `G8-VBN-V01-claude-bank-002` (Claude K7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de stip op (2, 4).
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** 2,4  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4,2 → Het eerste getal is opzij, het tweede omhoog.
    - **Uitleg (Claude):** Eerst 2 opzij (naar rechts), dan 4 omhoog.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er met de temperatuur tussen # uur en # uur?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er met de temperatuur tussen # uur en # uur?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-GRAFIEK-ERBIJ
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Kijk of de lijn tussen 12.00 uur en 16.00 uur omhoog of omlaag gaat.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-013` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In de lijngrafiek zie je de temperatuur op een dag, van 8.00 uur tot 16.00 uur. Wat gebeurt er met de temperatuur tussen 12.00 uur en 16.00 uur?
    - **Opties:** A) De temperatuur daalt met 6 graden · B) De temperatuur daalt met 3 graden · C) De temperatuur stijgt met 3 graden
    - **Antwoord:** De temperatuur daalt met 3 graden  (controle: n.v.t.)
    - **Fout-hints (Claude):** De temperatuur stijgt met 3 graden → Kijk welk getal het grootst is en of de lijn omhoog of omlaag gaat. · De temperatuur daalt met 6 graden → Je gebruikt het verkeerde beginpunt. Begin bij het getal dat bij 12 uur hoort.
    - **Uitleg (Claude):** Om 12 uur is het 18 graden en om 16 uur 15 graden. 18 − 15 = 3. De temperatuur gaat dus 3 graden omlaag.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: In een cirkeldiagram staat welke sport [wie] van een klas het liefst doen. De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis. Er zitten # [ding] in [plek]. Hoeveel kinderen kiezen voetbal?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In een cirkeldiagram staat welke sport [wie] van een klas het liefst doen. De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis. Er zitten # [ding] in [plek]. Hoeveel kinderen kiezen voetbal?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KLEUR-WEG
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “6 hoort bij een kwart. Voetbal is de helft, en dat is meer dan een kwart.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-014` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een cirkeldiagram staat welke sport de kinderen van een klas het liefst doen. De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis. Er zitten 24 kinderen in de klas. Hoeveel kinderen kiezen voetbal?
    - **Opties:** A) 8 kinderen · B) 12 kinderen · C) 6 kinderen
    - **Antwoord:** 12 kinderen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 kinderen → 6 hoort bij een kwart. Het blauwe deel is groter dan een kwart. · 8 kinderen → Je hebt in drie stukken gedeeld. De delen in de cirkel zijn niet even groot.
    - **Uitleg (Claude):** De helft van de cirkel is blauw. De helft van 24 is 12. Dus 12 kinderen horen bij het blauwe deel.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: In een grafiek loopt de as met stappen van #. De staaf van groep # [ding] precies tussen # en #. Hoeveel is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In een grafiek loopt de as met stappen van #. De staaf van groep # [ding] precies tussen # en #. Hoeveel is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VBN-V01
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk hoe groot de stap tussen twee streepjes is en neem daar de helft van.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-015` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een grafiek loopt de as met stappen van 20. De staaf van groep 7 staat precies tussen 60 en 80. Hoeveel is dat?
    - **Opties:** A) 65 · B) 140 · C) 70
    - **Antwoord:** 70  (controle: n.v.t.)
    - **Fout-hints (Claude):** 65 → Kijk hoe groot de stap tussen twee streepjes is en neem daar de helft van. · 140 → Je hebt de twee getallen opgeteld. De staaf ligt ertussenin.
    - **Uitleg (Claude):** Tussen 60 en 80 zit 20. De helft daarvan is 10. Precies ertussen is dus 60 + 10 = 70.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: [staafdiagram] In het staafdiagram zie je hoeveel boeken er op [naam], [naam] en [naam] zijn geleend. Op welke dag zijn de meeste boeken geleend?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[staafdiagram] In het staafdiagram zie je hoeveel boeken er op [naam], [naam] en [naam] zijn geleend. Op welke dag zijn de meeste boeken geleend?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-ONDER-NIVEAU
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): niet-de-hoogste-staaf (1), laagste-staaf (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar de hoogste staaf. Op welke dag hoort die?”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-016` (Claude G9, ai, niveau 1 → basis)
    - **Opgave:** In het staafdiagram zie je hoeveel boeken er op maandag, dinsdag en woensdag zijn geleend. Op welke dag zijn de meeste boeken geleend?
    - **Tekening:** `{"soort": "staafdiagram", "staven": [{"naam": "maandag", "waarde": 12}, {"naam": "dinsdag", "waarde": 8}, {"naam": "woensdag", "waarde": 15}], "max": 15, "perstreep": 1, "cijfer_om": 5}`
    - **Opties:** A) Woensdag · B) Maandag · C) Dinsdag
    - **Antwoord:** Woensdag  (controle: n.v.t.)
    - **Fout-hints (Claude):** Maandag → Kijk nog eens welke staaf het hoogst is, dus welk getal het grootst is. · Dinsdag → Je hebt de kleinste staaf gekozen. De vraag gaat over de meeste boeken.
    - **Uitleg (Claude):** Je vergelijkt de drie getallen: 12, 8 en 15. Het getal 15 is het grootst. Dus op woensdag zijn de meeste boeken geleend.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
