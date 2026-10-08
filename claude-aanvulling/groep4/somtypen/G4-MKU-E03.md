# G4-MKU-E03 — Voor-, zij- en bovenaanzicht

Onze omschrijving: Voor-/zij-/bovenaanzicht; bouwplaten kubus/balk/piramide; object van bouwplaat · in onze bank: 8 items

Claude-vragen gemapt: **4** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [ruimtefiguur] Een vlak is een platte kant. ⏎ Dit is een [figuur]. Hoeveel vlakken heeft een [figuur]? (Tel ook wat je niet ziet.)

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[ruimtefiguur] Een vlak is een platte kant. ⏎ Dit is een [figuur]. Hoeveel vlakken heeft een [figuur]? (Tel ook wat je niet ziet.)” (koppeling: claudeId)
- Items: **3** · Claude-doelen: K5 (3) · regel: D-VLAKKEN, D-VLAKKEN-PIRAMIDE
- Getallenruimte: n.v.t. · type: kale
- **Visual: nodig — niet live zonder beeld** (3 items): tekening van een balk met doorzichtige of gestippelde achterkant (verplicht: 'tel ook wat je niet ziet') — de Claude-tekenaar kent geen ruimtefiguur · tekening van een kubus met doorzichtige of gestippelde achterkant (verplicht: 'tel ook wat je niet ziet') — de Claude-tekenaar kent geen ruimtefiguur · tekening van een piramide met doorzichtige of gestippelde achterkant (verplicht: 'tel ook wat je niet ziet'); met een vierkant grondvlak, anders klopt 5 niet — de Claude-tekenaar kent geen ruimtefiguur
- Didactiek-besluit (G4-twijfel, 1 okt): vlakken kubus/balk (= 6 vlakjes bouwplaat), vlakken piramide (= stukken bouwplaat) — zie besluiten_twijfel.md
- Denkfouten (Claude): een-ernaast (6)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee.”)
- Voorbeelden:
  - `G4-MKU-E03-claude-bank-001` (Claude K5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een vlak is een platte kant.
Dit is een balk. Hoeveel vlakken heeft een balk? (Tel ook wat je niet ziet.)
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "balk"}`
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee. · 7 → Je hebt er een dubbel geteld. Ga systematisch rond: boven, onder, dan de zijkanten.
    - **Uitleg (Claude):** Een balk heeft 6 vlakken, 8 hoekpunten en 12 ribben.
  - `G4-MKU-E03-claude-bank-003` (Claude K5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Een vlak is een platte kant.
Dit is een piramide. Hoeveel vlakken heeft een piramide? (Tel ook wat je niet ziet.)
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "piramide"}`
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 3 → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee. · 6 → Je hebt er een dubbel geteld. Ga systematisch rond: boven, onder, dan de zijkanten.
    - **Uitleg (Claude):** Een piramide heeft 5 vlakken, 5 hoekpunten en 8 ribben.

- **Hint 1 (te schrijven):** Een vlak is een platte kant. Draai de figuur in je hoofd rond: ook achter en onder zitten vlakken.
- **Hint 2 (te schrijven):** Tel eerst de vlakken die je ziet. Tel dan de vlakken aan de achterkant en de onderkant erbij.
- **Ouderzin:** Je kind telt de vlakken (platte kanten) van een ruimtefiguur, ook die je niet ziet.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen wat je ziet` (fout = antwoord − 2 of meer) → Je telt alleen wat je ziet. De achterkant en de onderkant tellen ook mee.  [Claude, ok]
  - `dubbel geteld` (fout = antwoord + 1) → Je hebt er één dubbel geteld. Wijs elke platte kant maar één keer aan.  [Claude, taalfix]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Je mist er één. Vergeet de onderkant niet.  [nieuw]
  - `andere fout` (andere fout) → Wijs elke platte kant één keer aan. Vergeet de achterkant en de onderkant niet.  [nieuw]
- Status: hints klaar

## Somtype 2: [ruimtefiguur] Hoe heet deze ruimtelijke figuur?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[ruimtefiguur] Hoe heet deze ruimtelijke figuur?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: K5 (1) · regel: D-PIRAMIDE-NAAM
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): tekening van een piramide verplicht (Didactiek §5) — de Claude-tekenaar kent geen ruimtefiguur
- Didactiek-besluit (G4-twijfel, 1 okt): piramide herkennen (naam staat in E03) — zie besluiten_twijfel.md
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een balk ziet er anders uit: denk aan een schoenendoos.”)
- Voorbeelden:
  - `G4-MKU-E03-claude-bank-004` (Claude K5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Hoe heet deze ruimtelijke figuur?
    - **Tekening:** `{"soort": "ruimtefiguur", "figuur": "piramide"}`
    - **Opties:** A) bol · B) piramide · C) balk
    - **Antwoord:** piramide  (controle: ok)
    - **Fout-hints (Claude):** balk → Een balk ziet er anders uit: denk aan een schoenendoos. · bol → Een bol ziet er anders uit: denk aan een voetbal.
    - **Uitleg (Claude):** Dit is een piramide. Denk aan een tent met een punt.

- **Hint 1 (te schrijven):** Kijk naar de onderkant en naar de bovenkant van de figuur.
- **Hint 2 (te schrijven):** Hij lijkt op een tent met een punt bovenaan. Welke naam hoort daarbij?
- **Ouderzin:** Je kind herkent een piramide.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere figuur` (Claudes tekst bij de foute optie (tekst per item)) → … (eigen tekst per item)  [Claude, ok]
  - `andere fout` (andere fout) → Kijk naar de bovenkant. Welke figuur heeft een punt?  [nieuw]
- Status: hints klaar
