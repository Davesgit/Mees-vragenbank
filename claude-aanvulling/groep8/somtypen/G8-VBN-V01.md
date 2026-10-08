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
    - **Antwoord:** (1, 0)  (controle: n.v.t.)
    - **Fout-hints (Claude):** 0,1 → Het eerste getal is opzij, het tweede omhoog.
    - **Uitleg (Claude):** Eerst 1 opzij (naar rechts), dan 0 omhoog.
  - `G8-VBN-V01-claude-bank-002` (Claude K7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de stip op (2, 4).
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** (2, 4)  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4,2 → Het eerste getal is opzij, het tweede omhoog.
    - **Uitleg (Claude):** Eerst 2 opzij (naar rechts), dan 4 omhoog.

- **Hint 1 (te schrijven):** Bij de stip horen twee getallen tussen haakjes. Welk getal hoort bij opzij, en welk bij omhoog?
- **Hint 2 (te schrijven):** Begin bij nul. Het getal vóór de komma zegt hoeveel stappen je opzij gaat, naar rechts. Het getal na de komma zegt hoeveel stappen je daarna omhoog gaat. Zet daar de stip.
- **Ouderzin:** Je kind zet een punt in een rooster met twee getallen tussen haakjes.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omgewisseld` (Claudes sleutel: getallen omgewisseld) → Daar staan de twee getallen omgewisseld. Het getal vóór de komma gaat opzij, het getal na de komma omhoog.  [Claude, taalfix]
  - `stip op de lijn van nul` (fout = een getal uit de vraag) → Die stip ligt op de lijn van nul. Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.  [nieuw]
  - `andere fout` (andere fout) → Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.  [nieuw]
- Status: hints klaar

## Somtype 2: In een cirkeldiagram staat welke sport [wie] van een klas het liefst doen. De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis. Er zitten # [ding] in [plek]. Hoeveel kinderen kiezen voetbal?

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
    - **Uitleg (Claude):** De helft van de cirkel is voetbal. De helft van 24 is 12. Dus 12 kinderen kiezen voetbal.

- **Hint 1 (te schrijven):** Welk deel van de cirkel hoort bij voetbal?
- **Hint 2 (te schrijven):** Voetbal is de helft van de cirkel. Neem de helft van het aantal in de klas.
- **Ouderzin:** Je kind rekent met een cirkeldiagram uit hoeveel een deel van de klas is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een kwart` (6 kinderen) → Dat hoort bij een kwart van de klas. Voetbal is de helft: dat is meer dan een kwart.  [nieuw]
  - `drie gelijke stukken` (8 kinderen) → Zo deel je de klas in drie gelijke stukken. Maar de stukken van de cirkel verschillen in grootte.  [nieuw]
  - `andere fout` (andere fout) → Welk deel van de cirkel is voetbal? Neem dat deel van de hele klas.  [nieuw]
- Status: hints klaar

## Somtype 3: In een grafiek loopt de as met stappen van #. De staaf van groep # staat precies tussen # en #. Bij welk getal staat de [ding]?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In een grafiek loopt de as met stappen van #. De staaf van groep # [ding] precies tussen # en #. Hoeveel is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VBN-V01
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk hoe groot de stap tussen twee streepjes is en neem daar de helft van.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-015` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een grafiek loopt de as met stappen van 20. De staaf van groep 7 staat precies tussen 60 en 80. Bij welk getal staat de staaf?
    - **Opties:** A) 65 · B) 140 · C) 70
    - **Antwoord:** 70  (controle: n.v.t.)
    - **Fout-hints (Claude):** 65 → Kijk hoe groot de stap tussen twee streepjes is en neem daar de helft van. · 140 → Je hebt de twee getallen opgeteld. De staaf ligt ertussenin.
    - **Uitleg (Claude):** Tussen 60 en 80 zit 20. De helft daarvan is 10. Precies ertussen is dus 60 + 10 = 70.

- **Hint 1 (te schrijven):** Precies tussen twee getallen ligt het getal in het midden.
- **Hint 2 (te schrijven):** Hoeveel is het van het kleinste getal tot het grootste? Neem daar de helft van. Tel die helft op bij het kleinste getal.
- **Ouderzin:** Je kind leest op een as een getal af dat precies tussen twee streepjes ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet in het midden` (65) → Dat ligt niet precies in het midden. Hoe groot is de stap van het kleinste getal naar het grootste? Neem daar de helft van.  [nieuw]
  - `opgeteld` (140) → Dat zijn de twee getallen samen. Het getal dat je zoekt, ligt tussen die twee in.  [nieuw]
  - `andere fout` (andere fout) → Welk getal ligt precies in het midden van de twee getallen?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een grafiek loopt de as met stappen van #. De staaf van groep # [ding] precies tussen # en #. Hoeveel is dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: [lijngrafiek] In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er met de temperatuur tussen # uur en # uur?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er met de temperatuur tussen # uur en # uur?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-GRAFIEK-ERBIJ
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “Kijk of de lijn tussen 12.00 uur en 16.00 uur omhoog of omlaag gaat.”)
- Voorbeelden:
  - `G8-VBN-V01-claude-bank-013` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In de lijngrafiek zie je de temperatuur op een dag, van 8.00 uur tot 16.00 uur. Wat gebeurt er met de temperatuur tussen 12.00 uur en 16.00 uur?
    - **Tekening:** `{"soort": "lijngrafiek", "titel": "Temperatuur op een dag", "punten": [{"naam": "8.00 uur", "waarde": 12}, {"naam": "12.00 uur", "waarde": 18}, {"naam": "16.00 uur", "waarde": 15}], "max": 20, "perstreep": 2, "cijfer_om": 2}`
    - **Opties:** A) De temperatuur daalt met 6 graden · B) De temperatuur daalt met 3 graden · C) De temperatuur stijgt met 3 graden
    - **Antwoord:** De temperatuur daalt met 3 graden  (controle: n.v.t.)
    - **Fout-hints (Claude):** De temperatuur stijgt met 3 graden → Kijk welk getal het grootst is en of de lijn omhoog of omlaag gaat. · De temperatuur daalt met 6 graden → Je gebruikt het verkeerde beginpunt. Begin bij het getal dat bij 12 uur hoort.
    - **Uitleg (Claude):** Om 12 uur is het 18 graden en om 16 uur 15 graden. 18 − 15 = 3. De temperatuur gaat dus 3 graden omlaag.

- **Hint 1 (te schrijven):** Zoek op de lijn de twee tijden uit de vraag. Gaat de lijn daartussen omhoog of omlaag?
- **Hint 2 (te schrijven):** Lees de temperatuur af bij de tijd waar het stuk begint en bij de tijd waar het stopt. Hoeveel graden is het verschil? Kijk ook of de lijn omhoog of omlaag gaat.
- **Ouderzin:** Je kind leest in een lijngrafiek af hoe de temperatuur verandert.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omhoog in plaats van omlaag` (De temperatuur stijgt met 3 graden) → Kijk of de lijn tussen die twee tijden omhoog of omlaag gaat.  [nieuw]
  - `verschil van een ander stuk` (De temperatuur daalt met 6 graden) → Dat verschil hoort bij een ander stuk van de lijn. Lees de temperatuur af bij de twee tijden uit de vraag.  [nieuw]
  - `andere fout` (andere fout) → Lees de temperatuur af bij de twee tijden uit de vraag. Gaat de lijn omhoog of omlaag?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er met de temperatuur tussen # uur en # uur?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Zoek de hoogste staaf.
- **Hint 2 (te schrijven):** Vergelijk de staven: welke komt het hoogst? Lees af bij welke dag die staaf hoort.
- **Ouderzin:** Je kind leest in een staafdiagram af waar het meeste bij hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niet de hoogste staaf` (Maandag) → Die staaf is niet de hoogste. Welke staaf komt het hoogst? Bij welke dag hoort die?  [nieuw]
  - `de laagste staaf` (Dinsdag) → Dat is de laagste staaf. De meeste boeken horen bij de hoogste staaf.  [nieuw]
  - `andere fout` (andere fout) → Zoek de hoogste staaf. Bij welke dag hoort die?  [nieuw]
- Status: hints klaar
