# G8-VBN-E04 — Beste diagram kiezen en conclusies checken

Onze omschrijving: Keuze beste diagramtype; kritisch over presentatie & conclusies · in onze bank: 8 items

Claude-vragen gemapt: **43** in **37** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: G13 (3) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (6)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-033` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "15 kinderen kozen rekenen." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 55}, {"naam": "taal", "waarde": 15}, {"naam": "gym", "waarde": 10}, {"naam": "tekenen", "waarde": 20}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.
  - `G8-VBN-E04-claude-bank-032` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "15 kinderen kozen tekenen." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 30}, {"naam": "taal", "waarde": 30}, {"naam": "gym", "waarde": 5}, {"naam": "tekenen", "waarde": 35}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-025` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest fiets." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "fiets", "waarde": 55}, {"naam": "lopend", "waarde": 20}, {"naam": "auto", "waarde": 5}, {"naam": "bus", "waarde": 20}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Nee, dat klopt niet. · C) Dat kun je hier niet zien.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Fiets is 55%. Meer dan de helft is meer dan 50%, dus de bewering klopt.
  - `G8-VBN-E04-claude-bank-026` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest bus." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "fiets", "waarde": 20}, {"naam": "lopend", "waarde": 10}, {"naam": "auto", "waarde": 15}, {"naam": "bus", "waarde": 55}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Nee, dat klopt niet. · C) Dat kun je hier niet zien.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Bus is 55%. Meer dan de helft is meer dan 50%, dus de bewering klopt.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-028` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "15 kinderen kozen hond." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 45}, {"naam": "kat", "waarde": 25}, {"naam": "konijn", "waarde": 10}, {"naam": "vis", "waarde": 20}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.
  - `G8-VBN-E04-claude-bank-027` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "12 kinderen kozen vis." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 20}, {"naam": "kat", "waarde": 25}, {"naam": "konijn", "waarde": 10}, {"naam": "vis", "waarde": 45}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-031` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest hond." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 55}, {"naam": "kat", "waarde": 25}, {"naam": "konijn", "waarde": 20}, {"naam": "vis", "waarde": 0}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Hond is 55%. Meer dan de helft is meer dan 50%, dus de bewering klopt.
  - `G8-VBN-E04-claude-bank-030` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest vis." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 25}, {"naam": "kat", "waarde": 20}, {"naam": "konijn", "waarde": 20}, {"naam": "vis", "waarde": 35}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Dat kun je hier niet zien. · C) Nee, dat klopt niet.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Vis is 35%. Meer dan de helft is meer dan 50%, dus de bewering klopt niet.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-038` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "12 kinderen kozen niets." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "water", "waarde": 30}, {"naam": "melk", "waarde": 30}, {"naam": "sap", "waarde": 5}, {"naam": "niets", "waarde": 35}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.
  - `G8-VBN-E04-claude-bank-037` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "30 kinderen kozen water." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "water", "waarde": 50}, {"naam": "melk", "waarde": 15}, {"naam": "sap", "waarde": 5}, {"naam": "niets", "waarde": 30}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Bij de as van een grafiek staan de getallen #, #, #, # en # op gelijke afstand. Waarom is deze grafiek misleidend?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Bij de as van een grafiek staan de getallen #, #, #, # en # op gelijke afstand. Waarom is deze grafiek misleidend?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Vijf getallen is prima. Kijk eens hoe groot elke stap is.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-001` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Bij de as van een grafiek staan de getallen 0, 10, 20, 100 en 200 op gelijke afstand. Waarom is deze grafiek misleidend?
    - **Opties:** A) De as moet altijd bij 100 eindigen. · B) De stapjes op de as zijn niet gelijk. · C) Er staan te veel getallen bij de as.
    - **Antwoord:** De stapjes op de as zijn niet gelijk.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Er staan te veel getallen bij de as. → Vijf getallen is prima. Kijk eens hoe groot elke stap is. · De as moet altijd bij 100 eindigen. → Een as mag bij elk getal eindigen. Vergelijk de sprongen tussen de getallen.
    - **Uitleg (Claude):** Van 0 naar 10 is een stap van 10, maar van 20 naar 100 is een stap van 80. Toch zijn de afstanden op papier even groot. Daardoor lees je de staven helemaal verkeerd.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Bij de as van een grafiek staat: aantal bezoekers (x #). De staaf van zaterdag stopt bij #. Hoeveel [ding] waren er?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Bij de as van een grafiek staat: aantal bezoekers (x #). De staaf van zaterdag stopt bij #. Hoeveel [ding] waren er?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het getal van de as overgenomen. Lees het tekstje bij de as nog eens.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-002` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** Bij de as van een grafiek staat: aantal bezoekers (x 1000). De staaf van zaterdag stopt bij 4. Hoeveel bezoekers waren er?
    - **Opties:** A) 4 bezoekers · B) 400 bezoekers · C) 4000 bezoekers
    - **Antwoord:** 4000 bezoekers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 bezoekers → Je hebt het getal van de as overgenomen. Lees het tekstje bij de as nog eens. · 400 bezoekers → Je hebt met 100 vermenigvuldigd. Kijk goed welk getal er achter het maalteken staat.
    - **Uitleg (Claude):** Bij de as staat dat de getallen keer 1000 gaan. De staaf bij 4 betekent dus 4 keer 1000. Dat zijn 4000 bezoekers.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Bij de as van een staafdiagram staan alleen de getallen #, #, #, # en #. De staaf van woensdag stopt precies tussen # en #. Hoeveel is dat?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Bij de as van een staafdiagram staan alleen de getallen #, #, #, # en #. De staaf van woensdag stopt precies tussen # en #. Hoeveel is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je telde de streepjes in plaats van de getallen. Kijk tussen welke twee getallen de staaf stopt.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-003` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** Bij de as van een staafdiagram staan alleen de getallen 0, 5, 10, 15 en 20. De staaf van woensdag stopt precies tussen 10 en 15. Hoeveel is dat?
    - **Opties:** A) Ongeveer 12 of 13 · B) Ongeveer 2 of 3 · C) Precies 25
    - **Antwoord:** Ongeveer 12 of 13  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ongeveer 2 of 3 → Je telde de streepjes in plaats van de getallen. Kijk tussen welke twee getallen de staaf stopt. · Precies 25 → Je hebt 10 en 15 opgeteld. De staaf stopt ergens tússen die twee getallen.
    - **Uitleg (Claude):** De staaf stopt halverwege 10 en 15. Dat is ongeveer 12 of 13. Bij stapjes van 5 moet je tussenwaarden zelf schatten.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van # naar #. Klopt die kop?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van # naar #. Klopt die kop?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De staaf lijkt misschien veel hoger. Kijk naar de getallen 20 en 24.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-004` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van 20 naar 24. Klopt die kop?
    - **Opties:** A) Ja, de staaf is twee keer zo hoog. · B) Ja, er zijn 4 bezoekers bij gekomen. · C) Nee, 24 is geen dubbel van 20.
    - **Antwoord:** Nee, 24 is geen dubbel van 20.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, de staaf is twee keer zo hoog. → De staaf lijkt misschien veel hoger. Kijk naar de getallen 20 en 24. · Ja, er zijn 4 bezoekers bij gekomen. → Verdubbelen is niet hetzelfde als er een paar bij krijgen. Wat is het dubbele van 20?
    - **Uitleg (Claude):** Het dubbele van 20 is 40, maar er staat 24. De groei is dus maar 4 bezoekers. Een kop boven een grafiek kan flink overdrijven.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: De verkoop van sap is verdubbeld. In de grafiek staat een flesje dat twee keer zo hoog én twee keer zo breed is getekend. Waarom fopt dit je?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “De verkoop van sap is verdubbeld. In de grafiek staat een flesje dat twee keer zo hoog én twee keer zo breed is getekend. Waarom fopt dit je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), schatting-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Het plaatje is niet alleen hoger geworden, maar ook breder. Wat gebeurt er dan met het vlak?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-005` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** De verkoop van sap is verdubbeld. In de grafiek staat een flesje dat twee keer zo hoog én twee keer zo breed is getekend. Waarom fopt dit je?
    - **Opties:** A) Het flesje lijkt vier keer zo groot. · B) Niets, twee keer zo hoog is precies goed. · C) Het flesje lijkt acht keer zo groot.
    - **Antwoord:** Het flesje lijkt vier keer zo groot.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Niets, twee keer zo hoog is precies goed. → Het plaatje is niet alleen hoger geworden, maar ook breder. Wat gebeurt er dan met het vlak? · Het flesje lijkt acht keer zo groot. → Reken met hoogte en breedte samen, dus met twee keer een verdubbeling.
    - **Uitleg (Claude):** Wordt een plaatje twee keer zo hoog en twee keer zo breed, dan past het vier keer in het vlak. Je ogen zien dus vier keer zoveel, terwijl het maar twee keer zoveel is. Daarom hoort alleen de hoogte te veranderen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: Een cirkeldiagram is schuin getekend, alsof het een taart met dikte is. Het voorste stuk is #%, net als het achterste stuk. Wat is het probleem?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Een cirkeldiagram is schuin getekend, alsof het een taart met dikte is. Het voorste stuk is #%, net als het achterste stuk. Wat is het probleem?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “De percentages staan er gewoon bij. Vertrouw je meer op je ogen of op de getallen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-006` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Een cirkeldiagram is schuin getekend, alsof het een taart met dikte is. Het voorste stuk is 25%, net als het achterste stuk. Wat is het probleem?
    - **Opties:** A) Het voorste stuk lijkt groter dan het is. · B) Het voorste stuk is echt groter dan 25%. · C) Een cirkeldiagram mag geen kleuren hebben.
    - **Antwoord:** Het voorste stuk lijkt groter dan het is.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het voorste stuk is echt groter dan 25%. → De percentages staan er gewoon bij. Vertrouw je meer op je ogen of op de getallen? · Een cirkeldiagram mag geen kleuren hebben. → Kleuren helpen juist bij het lezen. Het gaat hier om de schuine tekening.
    - **Uitleg (Claude):** Door de schuine tekening komt het voorste stuk dichterbij en lijkt het breder. Beide stukken zijn toch echt 25%. Kijk daarom naar de getallen en niet naar de vorm.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: Een grafiek laat twee staven zien, maar bij de as staan helemaal geen getallen. Waarom is dat lastig?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Een grafiek laat twee staven zien, maar bij de as staan helemaal geen getallen. Waarom is dat lastig?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Welke staaf hoger is, zie je juist wel. Maar weet je ook hoevéél hoger?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-007` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** Een grafiek laat twee staven zien, maar bij de as staan helemaal geen getallen. Waarom is dat lastig?
    - **Opties:** A) Je kunt de kleuren niet meer uit elkaar houden. · B) Je weet niet hoeveel de staven zijn. · C) Je ziet niet welke staaf hoger is.
    - **Antwoord:** Je weet niet hoeveel de staven zijn.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Je ziet niet welke staaf hoger is. → Welke staaf hoger is, zie je juist wel. Maar weet je ook hoevéél hoger? · Je kunt de kleuren niet meer uit elkaar houden. → Met de kleuren is niets mis. Het gaat om de informatie die bij de as hoort.
    - **Uitleg (Claude):** Zonder getallen bij de as kun je alleen zien welke staaf hoger is. Hoe groot het verschil is, blijft een raadsel. Een eerlijke grafiek heeft altijd een as met getallen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 13: Een grafiek laat zien dat in warme maanden meer ijsjes worden verkocht en ook meer mensen zwemmen. Iemand zegt: door de ijsjes gaan mensen zwemmen. Klopt dat?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Een grafiek laat zien dat in warme maanden meer ijsjes worden verkocht en ook meer mensen zwemmen. Iemand zegt: door de ijsjes gaan mensen zwemmen. Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), grafiek-verkeerd-afgelezen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Twee lijnen die samen stijgen, hoeven elkaar niet te veroorzaken. Wat hebben ze allebei gemeen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-008` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Een grafiek laat zien dat in warme maanden meer ijsjes worden verkocht en ook meer mensen zwemmen. Iemand zegt: door de ijsjes gaan mensen zwemmen. Klopt dat?
    - **Opties:** A) Nee, want de lijnen dalen juist samen. · B) Nee, het komt allebei door de warmte. · C) Ja, want beide lijnen stijgen samen.
    - **Antwoord:** Nee, het komt allebei door de warmte.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, want beide lijnen stijgen samen. → Twee lijnen die samen stijgen, hoeven elkaar niet te veroorzaken. Wat hebben ze allebei gemeen? · Nee, want de lijnen dalen juist samen. → Lees nog eens wat er in de warme maanden met beide lijnen gebeurt.
    - **Uitleg (Claude):** Beide lijnen stijgen omdat het warm is. Het een zorgt niet voor het ander. Uit een grafiek mag je niet zomaar een oorzaak halen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 14: Een klas telt # [ding]. In een staafdiagram over huisdieren zijn de staven samen # [ding]. Wat is hiervoor de beste verklaring?

- Sleutel: nrOrigineel **35** · somtypeOrigineel “Een klas telt # [ding]. In een staafdiagram over huisdieren zijn de staven samen # [ding]. Wat is hiervoor de beste verklaring?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KRITISCH
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Denk eerst na of er een gewone reden kan zijn waarom een kind twee keer meetelt.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-041` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Een klas telt 25 kinderen. In een staafdiagram over huisdieren zijn de staven samen 30 hoog. Wat is hiervoor de beste verklaring?
    - **Opties:** A) Sommige kinderen hebben meer dan één huisdier · B) De grafiek is fout getekend · C) Er zitten 30 kinderen in de klas
    - **Antwoord:** Sommige kinderen hebben meer dan één huisdier  (controle: n.v.t.)
    - **Fout-hints (Claude):** De grafiek is fout getekend → Denk eerst na of er een gewone reden kan zijn waarom een kind twee keer meetelt. · Er zitten 30 kinderen in de klas → In de vraag staat duidelijk hoeveel kinderen er in de klas zitten. Lees dat nog eens.
    - **Uitleg (Claude):** Een kind kan bij meerdere soorten huisdieren meegeteld worden. Daardoor is het totaal van de staven hoger dan het aantal kinderen. Dat is geen fout in de grafiek.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 15: Een winkel laat een grafiek van de verkoop zien, maar toont alleen de drie beste maanden van het jaar. Waarom is dat misleidend?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Een winkel laat een grafiek van de verkoop zien, maar toont alleen de drie beste maanden van het jaar. Waarom is dat misleidend?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Drie staven mag best. Het gaat erom wélke maanden er zijn weggelaten.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-009` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Een winkel laat een grafiek van de verkoop zien, maar toont alleen de drie beste maanden van het jaar. Waarom is dat misleidend?
    - **Opties:** A) De getallen bij die maanden kloppen niet. · B) De slechte maanden zie je niet. · C) Drie staven zijn te weinig om te tekenen.
    - **Antwoord:** De slechte maanden zie je niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Drie staven zijn te weinig om te tekenen. → Drie staven mag best. Het gaat erom wélke maanden er zijn weggelaten. · De getallen bij die maanden kloppen niet. → De getallen zelf zijn gewoon goed gemeten. Denk aan de maanden die ontbreken.
    - **Uitleg (Claude):** Door alleen de beste maanden te tonen, lijkt de verkoop het hele jaar hoog. De andere negen maanden ontbreken. Een eerlijke grafiek laat alle gegevens zien.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 16: In een cirkeldiagram over lievelingsfruit staan de stukken #%, #% en #%. Wat klopt hier niet?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “In een cirkeldiagram over lievelingsfruit staan de stukken #%, #% en #%. Wat klopt hier niet?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), deel-van-geheel-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Drie stukken mag prima. Tel de percentages eens bij elkaar op.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-010` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** In een cirkeldiagram over lievelingsfruit staan de stukken 50%, 40% en 30%. Wat klopt hier niet?
    - **Opties:** A) Het grootste stuk moet 100% zijn. · B) Samen is het meer dan 100%. · C) Er zijn te weinig stukken getekend.
    - **Antwoord:** Samen is het meer dan 100%.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Er zijn te weinig stukken getekend. → Drie stukken mag prima. Tel de percentages eens bij elkaar op. · Het grootste stuk moet 100% zijn. → Eén stuk is altijd een deel van het geheel. Kijk wat alle stukken samen moeten zijn.
    - **Uitleg (Claude):** Alle stukken van een cirkeldiagram vormen samen het geheel, dus 100%. Hier is 50 + 40 + 30 samen 120%. Dat kan niet in één cirkel passen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 17: In een grafiek staat onderaan de as het getal # en bovenaan het getal #. De lijn loopt naar [richting]. Wat betekent dat?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “In een grafiek staat onderaan de as het getal # en bovenaan het getal #. De lijn loopt naar [richting]. Wat betekent dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je bent gewend dat omhoog meer betekent. Lees hier eerst de getallen bij de as.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-011` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een grafiek staat onderaan de as het getal 100 en bovenaan het getal 0. De lijn loopt naar beneden. Wat betekent dat?
    - **Opties:** A) Het aantal wordt juist groter. · B) Het aantal wordt steeds kleiner. · C) Het aantal blijft de hele tijd gelijk.
    - **Antwoord:** Het aantal wordt juist groter.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het aantal wordt steeds kleiner. → Je bent gewend dat omhoog meer betekent. Lees hier eerst de getallen bij de as. · Het aantal blijft de hele tijd gelijk. → De lijn loopt duidelijk niet recht. Kijk naar de getallen waar de lijn langs gaat.
    - **Uitleg (Claude):** Hier staan de getallen omgekeerd: hoe lager op de as, hoe groter het getal. Een dalende lijn hoort dus bij grotere aantallen. Kijk altijd eerst naar de getallen bij de as.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 18: In een grafiek stopt de staaf van maandag bij # en de staaf van dinsdag bij #. Hoeveel meer waren het er op dinsdag?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “In een grafiek stopt de staaf van maandag bij # en de staaf van dinsdag bij #. Hoeveel meer waren het er op dinsdag?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): tiental-ernaast (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel eens rustig door van 96 naar 100. Hoeveel stapjes zijn dat?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-012` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** In een grafiek stopt de staaf van maandag bij 96 en de staaf van dinsdag bij 100. Hoeveel meer waren het er op dinsdag?
    - **Opties:** A) 10 meer · B) 196 meer · C) 4 meer
    - **Antwoord:** 4 meer  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 meer → Tel eens rustig door van 96 naar 100. Hoeveel stapjes zijn dat? · 196 meer → Bij 'hoeveel meer' vergelijk je twee getallen. Je telt ze niet bij elkaar op.
    - **Uitleg (Claude):** Van 96 naar 100 is een stapje van 4. De staven lijken misschien ver uit elkaar te liggen, maar het echte verschil is klein. Lees daarom altijd de getallen af.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 19: In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei # [ding]. Wat weet je zeker?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei # [ding]. Wat weet je zeker?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), afronden-verkeerde-kant (1)
- Verschillende Claude-fout-hints: 2 (meest: “Denk eens aan welke getallen allemaal worden afgerond tot 300.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-013` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei 300 hoog. Wat weet je zeker?
    - **Opties:** A) Beide aantallen zijn meer dan 300. · B) De echte aantallen kunnen verschillen. · C) De echte aantallen zijn precies gelijk.
    - **Antwoord:** De echte aantallen kunnen verschillen.  (controle: n.v.t.)
    - **Fout-hints (Claude):** De echte aantallen zijn precies gelijk. → Denk eens aan welke getallen allemaal worden afgerond tot 300. · Beide aantallen zijn meer dan 300. → Bij afronden kun je omhoog én omlaag gaan. Kan een getal onder 300 ook 300 worden?
    - **Uitleg (Claude):** Getallen van 250 tot en met 349 worden allemaal 300 na afronden. Twee even hoge staven kunnen dus bij 251 en 349 horen. Afronden verbergt kleine verschillen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 20: In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor # [ding]. Waarom fopt dit je?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor # [ding]. Waarom fopt dit je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), grafiek-verkeerd-afgelezen (1)
- Verschillende Claude-fout-hints: 2 (meest: “In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-014` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor 10 stuks. Waarom fopt dit je?
    - **Opties:** A) Het grote plaatje lijkt veel meer stuks. · B) Peren zijn nu eenmaal groter dan appels. · C) Er staan te weinig plaatjes bij appels.
    - **Antwoord:** Het grote plaatje lijkt veel meer stuks.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Peren zijn nu eenmaal groter dan appels. → In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien. · Er staan te weinig plaatjes bij appels. → Het aantal plaatjes klopt juist wel. Let op het verschil in grootte.
    - **Uitleg (Claude):** In een plaatjesgrafiek moet elk plaatje even groot zijn. Anders denk je bij een groot plaatje meteen aan een groot aantal. Hier staan beide plaatjes toch echt voor 10 stuks.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 21: In een plaatjesgrafiek staat een fietsje voor # [ding]. Bij groep # [ding] # [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “In een plaatjesgrafiek staat een fietsje voor # [ding]. Bij groep # [ding] # [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt de plaatjes geteld. Kijk nog eens voor hoeveel kinderen één fietsje staat.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-015` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** In een plaatjesgrafiek staat een fietsje voor 10 kinderen. Bij groep 8 staan 6 fietsjes. Hoeveel kinderen zijn dat?
    - **Opties:** A) 60 kinderen · B) 6 kinderen · C) 16 kinderen
    - **Antwoord:** 60 kinderen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 kinderen → Je hebt de plaatjes geteld. Kijk nog eens voor hoeveel kinderen één fietsje staat. · 16 kinderen → Je hebt 10 en 6 opgeteld. Elk fietsje staat voor een hele groep van 10.
    - **Uitleg (Claude):** Elk fietsje staat voor 10 kinderen, dus 6 fietsjes zijn 6 keer 10. Dat zijn 60 kinderen. Lees altijd eerst wat één plaatje betekent.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 22: In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en # [ding] hondje. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en # [ding] hondje. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het halve plaatje als een heel plaatje geteld. Voor hoeveel honden staat een half hondje?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-016` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** In een plaatjesgrafiek staat één hondje voor 4 honden. Bij het asiel staan 3 hele hondjes en 1 half hondje. Hoeveel honden zijn dat?
    - **Opties:** A) 16 honden · B) 4 honden · C) 14 honden
    - **Antwoord:** 14 honden  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 honden → Je hebt het halve plaatje als een heel plaatje geteld. Voor hoeveel honden staat een half hondje? · 4 honden → Je hebt de plaatjes geteld in plaats van de honden. Elk heel plaatje staat voor meer dan één hond.
    - **Uitleg (Claude):** Drie hele hondjes zijn 3 keer 4, dus 12 honden. Een half hondje is de helft van 4, dus 2 honden. Samen zijn dat 14 honden.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 23: In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “In een staafdiagram vertelt alleen de hoogte het aantal. Wat zegt de breedte dan?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-017` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?
    - **Opties:** A) De brede staaf hoort bij meer kinderen. · B) Staven mogen nooit naast elkaar staan. · C) De brede staaf lijkt een groter aantal.
    - **Antwoord:** De brede staaf lijkt een groter aantal.  (controle: n.v.t.)
    - **Fout-hints (Claude):** De brede staaf hoort bij meer kinderen. → In een staafdiagram vertelt alleen de hoogte het aantal. Wat zegt de breedte dan? · Staven mogen nooit naast elkaar staan. → Staven naast elkaar is heel normaal. Let op het verschil in breedte.
    - **Uitleg (Claude):** In een staafdiagram lees je het aantal af aan de hoogte. Een bredere staaf ziet er groter uit, maar hoort bij hetzelfde aantal. Alle staven horen even breed te zijn.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 24: In een staafdiagram over het aantal gelezen boeken begint de as niet bij #, maar bij #. Waarom kan die grafiek je foppen?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “In een staafdiagram over het aantal gelezen boeken begint de as niet bij #, maar bij #. Waarom kan die grafiek je foppen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “De afstand tussen de staven maakt niets uit. Kijk nog eens naar het getal waar de as begint.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-018` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een staafdiagram over het aantal gelezen boeken begint de as niet bij 0, maar bij 90. Waarom kan die grafiek je foppen?
    - **Opties:** A) De verschillen lijken groter dan ze zijn. · B) De staven staan te dicht bij elkaar. · C) Er zijn te weinig boeken geteld.
    - **Antwoord:** De verschillen lijken groter dan ze zijn.  (controle: n.v.t.)
    - **Fout-hints (Claude):** De staven staan te dicht bij elkaar. → De afstand tussen de staven maakt niets uit. Kijk nog eens naar het getal waar de as begint. · Er zijn te weinig boeken geteld. → Met de aantallen is niets mis. Het probleem zit in de verdeling van de as.
    - **Uitleg (Claude):** Als de as bij 90 begint, zie je alleen het bovenste stukje van elke staaf. Een klein verschil lijkt dan een groot verschil. Begin je bij 0, dan zijn de staven bijna even hoog.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 25: In klas A kiest #% van de # [ding] voor voetbal. In klas B kiest #% van de # [ding] voor voetbal. Welke klas heeft de meeste voetballers?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “In klas A kiest #% van de # [ding] voor voetbal. In klas B kiest #% van de # [ding] voor voetbal. Welke klas heeft de meeste voetballers?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), deel-van-geheel-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een percentage hoort altijd bij een totaal. De klassen zijn niet even groot.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-019` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** In klas A kiest 50% van de 20 kinderen voor voetbal. In klas B kiest 40% van de 40 kinderen voor voetbal. Welke klas heeft de meeste voetballers?
    - **Opties:** A) Klas B, want dat zijn 16 kinderen. · B) Klas A, want 50% is meer dan 40%. · C) Ze hebben allebei evenveel voetballers.
    - **Antwoord:** Klas B, want dat zijn 16 kinderen.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Klas A, want 50% is meer dan 40%. → Een percentage hoort altijd bij een totaal. De klassen zijn niet even groot. · Ze hebben allebei evenveel voetballers. → Reken beide percentages eerst om naar echte aantallen kinderen.
    - **Uitleg (Claude):** 50% van 20 is 10 kinderen en 40% van 40 is 16 kinderen. Het grootste percentage hoort dus niet bij het grootste aantal. Kijk altijd bij welk totaal een percentage hoort.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 26: Je ziet een cirkeldiagram met de stukken hond #%, kat #% en konijn #%. Hoeveel kinderen hebben een hond gekozen?

- Sleutel: nrOrigineel **25** · somtypeOrigineel “Je ziet een cirkeldiagram met de stukken hond #%, kat #% en konijn #%. Hoeveel kinderen hebben een hond gekozen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “40% is een deel van het totaal. Staat het totale aantal kinderen er wel bij?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-020` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Je ziet een cirkeldiagram met de stukken hond 40%, kat 35% en konijn 25%. Hoeveel kinderen hebben een hond gekozen?
    - **Opties:** A) 40 kinderen hebben een hond gekozen. · B) 4 kinderen hebben een hond gekozen. · C) Dat kun je niet zien.
    - **Antwoord:** Dat kun je niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** 40 kinderen hebben een hond gekozen. → 40% is een deel van het totaal. Staat het totale aantal kinderen er wel bij? · 4 kinderen hebben een hond gekozen. → Een percentage is geen aantal. Je hebt eerst het totaal nodig.
    - **Uitleg (Claude):** Een cirkeldiagram laat alleen delen van het geheel zien. Zonder het totale aantal kinderen kun je geen aantallen berekenen. 40% van 20 is heel iets anders dan 40% van 200.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 27: Op de onderste as van een lijngrafiek staan #, #, # en # op gelijke afstand van elkaar. Waarom klopt dat niet?

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Op de onderste as van een lijngrafiek staan #, #, # en # op gelijke afstand van elkaar. Waarom klopt dat niet?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “De volgorde van klein naar groot klopt. Kijk naar de afstand tussen de jaartallen.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-021` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Op de onderste as van een lijngrafiek staan 2010, 2011, 2012 en 2020 op gelijke afstand van elkaar. Waarom klopt dat niet?
    - **Opties:** A) De jaren staan in de verkeerde volgorde. · B) Er horen precies vier punten in een lijngrafiek. · C) Tussen 2012 en 2020 zitten veel meer jaren.
    - **Antwoord:** Tussen 2012 en 2020 zitten veel meer jaren.  (controle: n.v.t.)
    - **Fout-hints (Claude):** De jaren staan in de verkeerde volgorde. → De volgorde van klein naar groot klopt. Kijk naar de afstand tussen de jaartallen. · Er horen precies vier punten in een lijngrafiek. → Het aantal punten mag je zelf kiezen. Let op hoeveel jaren er tussen twee punten zitten.
    - **Uitleg (Claude):** Op een tijdas hoort gelijke afstand ook gelijke tijd te betekenen. Tussen 2012 en 2020 zitten acht jaar, tussen 2010 en 2011 maar één jaar. De lijn geeft daardoor een vertekend beeld.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 28: Sanne vraagt alleen aan kinderen van de schaakclub wat hun favoriete spel is. Bijna iedereen zegt schaken. Wat is er mis met haar onderzoek?

- Sleutel: nrOrigineel **36** · somtypeOrigineel “Sanne vraagt alleen aan kinderen van de schaakclub wat hun favoriete spel is. Bijna iedereen zegt schaken. Wat is er mis met haar onderzoek?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KRITISCH
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Stel je voor dat zij honderd schakers vraagt. Zou de uitkomst dan eerlijker zijn?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-042` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Sanne vraagt alleen aan kinderen van de schaakclub wat hun favoriete spel is. Bijna iedereen zegt schaken. Wat is er mis met haar onderzoek?
    - **Opties:** A) Zij vroeg het aan een eenzijdige groep · B) Zij vroeg het aan te weinig kinderen · C) Er is niets mis met haar onderzoek
    - **Antwoord:** Zij vroeg het aan een eenzijdige groep  (controle: n.v.t.)
    - **Fout-hints (Claude):** Zij vroeg het aan te weinig kinderen → Stel je voor dat zij honderd schakers vraagt. Zou de uitkomst dan eerlijker zijn? · Er is niets mis met haar onderzoek → Bedenk of deze groep wel lijkt op alle kinderen van de school.
    - **Uitleg (Claude):** Kinderen van een schaakclub houden al van schaken. Die groep lijkt niet op alle kinderen. Daardoor geeft de uitkomst geen eerlijk beeld.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 29: Tim meet vijf keer zijn plant. # cm, # cm, # cm, # cm en # cm. Welke meting klopt waarschijnlijk niet?

- Sleutel: nrOrigineel **37** · somtypeOrigineel “Tim meet vijf keer zijn plant. # cm, # cm, # cm, # cm en # cm. Welke meting klopt waarschijnlijk niet?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KRITISCH
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): andere-deel-genomen (1), schatting-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “De kleinste waarde past hier goed bij de rest. Kijk naar de waarde die er ver naast ligt.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-043` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Tim meet vijf keer zijn plant. 10 cm, 12 cm, 13 cm, 15 cm en 60 cm. Welke meting klopt waarschijnlijk niet?
    - **Opties:** A) 10 cm · B) 15 cm · C) 60 cm
    - **Antwoord:** 60 cm  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 cm → De kleinste waarde past hier goed bij de rest. Kijk naar de waarde die er ver naast ligt. · 15 cm → 15 cm ligt dicht bij de andere metingen. Zoek de waarde die er heel sterk uit springt.
    - **Uitleg (Claude):** De eerste vier metingen liggen dicht bij elkaar, tussen 10 en 15 cm. De meting van 60 cm ligt daar heel ver vandaan. Zo'n uitschieter is waarschijnlijk een meetfout.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 30: Twee grafieken staan naast elkaar. Bij de ene loopt de as tot #, bij de andere tot #. Beide lijnen lijken even steil. Wat weet je nu?

- Sleutel: nrOrigineel **27** · somtypeOrigineel “Twee grafieken staan naast elkaar. Bij de ene loopt de as tot #, bij de andere tot #. Beide lijnen lijken even steil. Wat weet je nu?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “De lijnen lijken hetzelfde, maar de assen zijn dat niet. Vergelijk de getallen.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-022` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** Twee grafieken staan naast elkaar. Bij de ene loopt de as tot 50, bij de andere tot 500. Beide lijnen lijken even steil. Wat weet je nu?
    - **Opties:** A) De grafiek met de as tot 50 stijgt het meest. · B) De stijging is niet even groot. · C) Beide grafieken stijgen precies evenveel.
    - **Antwoord:** De stijging is niet even groot.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Beide grafieken stijgen precies evenveel. → De lijnen lijken hetzelfde, maar de assen zijn dat niet. Vergelijk de getallen. · De grafiek met de as tot 50 stijgt het meest. → Kijk hoeveel elke as per hokje omhoog gaat voordat je kiest.
    - **Uitleg (Claude):** Als de assen verschillende stapjes hebben, mag je de lijnen niet zomaar vergelijken. Dezelfde steilheid hoort dan bij heel verschillende aantallen. Vergelijk altijd eerst de assen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 31: Voor een onderzoek over het lievelingsvak zijn # [ding] uit één klas gevraagd. De kop zegt: de hele school kiest rekenen. Klopt dat?

- Sleutel: nrOrigineel **28** · somtypeOrigineel “Voor een onderzoek over het lievelingsvak zijn # [ding] uit één klas gevraagd. De kop zegt: de hele school kiest rekenen. Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Die 5 kinderen kozen inderdaad rekenen. Maar hoeveel kinderen zitten er op de hele school?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-023` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** Voor een onderzoek over het lievelingsvak zijn 5 kinderen uit één klas gevraagd. De kop zegt: de hele school kiest rekenen. Klopt dat?
    - **Opties:** A) Ja, want alle 5 kozen voor rekenen. · B) Ja, één klas lijkt op alle klassen. · C) Nee, 5 kinderen zijn te weinig.
    - **Antwoord:** Nee, 5 kinderen zijn te weinig.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, want alle 5 kozen voor rekenen. → Die 5 kinderen kozen inderdaad rekenen. Maar hoeveel kinderen zitten er op de hele school? · Ja, één klas lijkt op alle klassen. → Denk eens aan de andere groepen. Zouden die precies hetzelfde kiezen?
    - **Uitleg (Claude):** Vijf kinderen uit één klas zeggen niets over de hele school. Je hebt veel meer kinderen uit verschillende groepen nodig. Anders is de conclusie niet betrouwbaar.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 32: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" en toont percentages. Eronder staat: "Fiets en [naam] zijn samen meer dan de helft." Klopt dat?

- Sleutel: nrOrigineel **29** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" en toont percentages. Eronder staat: "Fiets en [naam] zijn samen meer dan de helft." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-024` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder staat: "Fiets en lopend zijn samen meer dan de helft." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "fiets", "waarde": 50}, {"naam": "lopend", "waarde": 15}, {"naam": "auto", "waarde": 5}, {"naam": "bus", "waarde": 30}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 50% + 15% = 65%. Dat is meer dan 50%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 33: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "Hond en [naam] zijn samen meer dan de helft." Klopt dat?

- Sleutel: nrOrigineel **30** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "Hond en [naam] zijn samen meer dan de helft." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-029` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Hond en kat zijn samen meer dan de helft." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 25}, {"naam": "kat", "waarde": 15}, {"naam": "konijn", "waarde": 15}, {"naam": "vis", "waarde": 45}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Nee, dat klopt niet. · C) Ja, dat klopt.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 25% + 15% = 40%. Dat is niet meer dan 50%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 34: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "Rekenen en [naam] zijn samen meer dan de helft." Klopt dat?

- Sleutel: nrOrigineel **31** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "Rekenen en [naam] zijn samen meer dan de helft." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-035` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "Rekenen en taal zijn samen meer dan de helft." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 35}, {"naam": "taal", "waarde": 30}, {"naam": "gym", "waarde": 5}, {"naam": "tekenen", "waarde": 30}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 35% + 30% = 65%. Dat is meer dan 50%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 35: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "Tekenen is precies # keer zo vaak gekozen als [naam]." Klopt dat?

- Sleutel: nrOrigineel **32** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "Tekenen is precies # keer zo vaak gekozen als [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-036` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "Tekenen is precies 5 keer zo vaak gekozen als taal." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 30}, {"naam": "taal", "waarde": 10}, {"naam": "gym", "waarde": 20}, {"naam": "tekenen", "waarde": 40}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Dat kun je hier niet zien. · C) Nee, dat klopt niet.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Tekenen is 40% en taal is 10%. 5 × 10 = 50, dus de bewering klopt niet.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 36: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?

- Sleutel: nrOrigineel **33** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-039` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest water." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "water", "waarde": 40}, {"naam": "melk", "waarde": 15}, {"naam": "sap", "waarde": 15}, {"naam": "niets", "waarde": 30}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Dat kun je hier niet zien. · C) Nee, dat klopt niet.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Water is 40%. Meer dan de helft is meer dan 50%, dus de bewering klopt niet.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 37: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Water en [naam] zijn samen meer dan de helft." Klopt dat?

- Sleutel: nrOrigineel **34** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Water en [naam] zijn samen meer dan de helft." Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G13 (1) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (2)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de percentages van de staven af en reken de bewering na.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-040` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "Water en melk zijn samen meer dan de helft." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "water", "waarde": 25}, {"naam": "melk", "waarde": 30}, {"naam": "sap", "waarde": 5}, {"naam": "niets", "waarde": 40}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 25% + 30% = 55%. Dat is meer dan 50%.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
