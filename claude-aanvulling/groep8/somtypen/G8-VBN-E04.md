# G8-VBN-E04 — Beste diagram kiezen en conclusies checken

Onze omschrijving: Keuze beste diagramtype; kritisch over presentatie & conclusies · in onze bank: 8 items

Claude-vragen gemapt: **43** in **37** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "# kinderen kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: G13 (3) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (6)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-033` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "11 kinderen kozen rekenen." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 55}, {"naam": "taal", "waarde": 15}, {"naam": "gym", "waarde": 10}, {"naam": "tekenen", "waarde": 20}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.
  - `G8-VBN-E04-claude-bank-032` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "7 kinderen kozen tekenen." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "rekenen", "waarde": 30}, {"naam": "taal", "waarde": 30}, {"naam": "gym", "waarde": 5}, {"naam": "tekenen", "waarde": 35}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Ja, dat klopt. · C) Nee, dat klopt niet.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.

- **Hint 1 (te schrijven):** Wat toont het diagram: aantallen of percentages? En wat noemt de zin eronder?
- **Hint 2 (te schrijven):** Een percentage zegt hoeveel van elke honderd. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat ergens bij het diagram?
- **Ouderzin:** Je kind ziet dat een diagram met percentages geen aantallen geeft: zonder het totaal kun je geen aantal uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Het diagram toont percentages, geen aantallen. Hoeveel er in totaal meededen, staat er niet bij. Kun je dan een aantal uitrekenen?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Om te zeggen dat het niet klopt, moet je het aantal kunnen uitrekenen. Het diagram toont alleen percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
  - `andere fout` (andere fout) → Het diagram toont percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar

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
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "fiets", "waarde": 60}, {"naam": "lopend", "waarde": 20}, {"naam": "auto", "waarde": 5}, {"naam": "bus", "waarde": 15}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Nee, dat klopt niet. · C) Dat kun je hier niet zien.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Fiets is 60%. Meer dan de helft is meer dan 50%, dus de bewering klopt.
  - `G8-VBN-E04-claude-bank-026` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest bus." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "fiets", "waarde": 20}, {"naam": "lopend", "waarde": 10}, {"naam": "auto", "waarde": 10}, {"naam": "bus", "waarde": 60}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Nee, dat klopt niet. · C) Dat kun je hier niet zien.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Bus is 60%. Meer dan de helft is meer dan 50%, dus de bewering klopt.

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent.
- **Hint 2 (te schrijven):** Zoek de staaf die in de zin genoemd wordt. Lees af hoe hoog hij komt: elk streepje is tien procent. Komt hij boven de vijftig procent uit?
- **Ouderzin:** Je kind leest een percentage af in een staafdiagram en vergelijkt het met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Lees het percentage van die staaf nog eens af. Komt hij echt boven de vijftig procent uit?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Lees het percentage van die staaf nog eens af. Meer dan de helft is meer dan vijftig procent. Hoe hoog komt de staaf?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → Meer dan de helft is ook een percentage: meer dan vijftig procent. Dat lees je af aan de staaf.  [nieuw]
  - `andere fout` (andere fout) → Lees de staaf af en vergelijk met vijftig procent.  [nieuw]
- Status: hints klaar

## Somtype 3: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "# kinderen kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-028` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "9 kinderen kozen hond." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 45}, {"naam": "kat", "waarde": 25}, {"naam": "konijn", "waarde": 10}, {"naam": "vis", "waarde": 20}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.
  - `G8-VBN-E04-claude-bank-027` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "9 kinderen kozen vis." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 20}, {"naam": "kat", "waarde": 25}, {"naam": "konijn", "waarde": 10}, {"naam": "vis", "waarde": 45}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Dat kun je hier niet zien.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen? · Nee, dat klopt niet. → Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?
    - **Uitleg (Claude):** Het diagram laat percentages zien, niet hoeveel kinderen er in totaal meededen. Zonder dat totaal kun je geen aantal uitrekenen.

- **Hint 1 (te schrijven):** Wat toont het diagram: aantallen of percentages? En wat noemt de zin eronder?
- **Hint 2 (te schrijven):** Een percentage zegt hoeveel van elke honderd. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat ergens bij het diagram?
- **Ouderzin:** Je kind ziet dat een diagram met percentages geen aantallen geeft: zonder het totaal kun je geen aantal uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Het diagram toont percentages, geen aantallen. Hoeveel er in totaal meededen, staat er niet bij. Kun je dan een aantal uitrekenen?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Om te zeggen dat het niet klopt, moet je het aantal kunnen uitrekenen. Het diagram toont alleen percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
  - `andere fout` (andere fout) → Het diagram toont percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar

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
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 60}, {"naam": "kat", "waarde": 20}, {"naam": "konijn", "waarde": 20}, {"naam": "vis", "waarde": 0}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Hond is 60%. Meer dan de helft is meer dan 50%, dus de bewering klopt.
  - `G8-VBN-E04-claude-bank-030` (Claude G13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Meer dan de helft van de kinderen kiest vis." Klopt dat?
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 25}, {"naam": "kat", "waarde": 20}, {"naam": "konijn", "waarde": 20}, {"naam": "vis", "waarde": 35}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Ja, dat klopt. · B) Dat kun je hier niet zien. · C) Nee, dat klopt niet.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** Vis is 35%. Meer dan de helft is meer dan 50%, dus de bewering klopt niet.

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent.
- **Hint 2 (te schrijven):** Zoek de staaf die in de zin genoemd wordt. Lees af hoe hoog hij komt: elk streepje is tien procent. Komt hij boven de vijftig procent uit?
- **Ouderzin:** Je kind leest een percentage af in een staafdiagram en vergelijkt het met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Lees het percentage van die staaf nog eens af. Komt hij echt boven de vijftig procent uit?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Lees het percentage van die staaf nog eens af. Meer dan de helft is meer dan vijftig procent. Hoe hoog komt de staaf?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → Meer dan de helft is ook een percentage: meer dan vijftig procent. Dat lees je af aan de staaf.  [nieuw]
  - `andere fout` (andere fout) → Lees de staaf af en vergelijk met vijftig procent.  [nieuw]
- Status: hints klaar

## Somtype 5: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "# kinderen kozen [naam]." Klopt dat?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G13 (2) · regel: G8-G13-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 10.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk wat de as laat zien: percentages of aantallen? Kun je daarmee een aantal kinderen uitrekenen?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-038` (Claude G13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "14 kinderen kozen niets." Klopt dat?
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

- **Hint 1 (te schrijven):** Wat toont het diagram: aantallen of percentages? En wat noemt de zin eronder?
- **Hint 2 (te schrijven):** Een percentage zegt hoeveel van elke honderd. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat ergens bij het diagram?
- **Ouderzin:** Je kind ziet dat een diagram met percentages geen aantallen geeft: zonder het totaal kun je geen aantal uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Het diagram toont percentages, geen aantallen. Hoeveel er in totaal meededen, staat er niet bij. Kun je dan een aantal uitrekenen?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Om te zeggen dat het niet klopt, moet je het aantal kunnen uitrekenen. Het diagram toont alleen percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
  - `andere fout` (andere fout) → Het diagram toont percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "# [ding] kozen [naam]." Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Kijk hoe groot de sprong is van het ene getal naar het volgende.
- **Hint 2 (te schrijven):** Reken bij elk paar getallen naast elkaar uit hoeveel erbij komt. Op papier is de afstand overal even groot. Komt er dan ook overal evenveel bij?
- **Ouderzin:** Je kind ontdekt dat een grafiek misleidt als de getallen bij de as niet in gelijke sprongen oplopen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eindgetal` (De as moet altijd bij 100 eindigen.) → Een as mag bij elk getal ophouden. Kijk naar wat er tussen de getallen gebeurt: komt er overal evenveel bij?  [nieuw]
  - `te veel getallen` (Er staan te veel getallen bij de as.) → Het aantal getallen is geen probleem. Kijk hoeveel er telkens bij komt van het ene getal naar het volgende.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoeveel er telkens bij komt van het ene getal naar het volgende. Is dat overal evenveel?  [nieuw]
- Status: hints klaar

## Somtype 7: Bij de as van een grafiek staat: aantal bezoekers (× #). De staaf van zaterdag stopt bij #. Hoeveel bezoekers waren er?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Bij de as van een grafiek staat: aantal bezoekers (x #). De staaf van zaterdag stopt bij #. Hoeveel [ding] waren er?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het getal van de as overgenomen. Lees het tekstje bij de as nog eens.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-002` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** Bij de as van een grafiek staat: aantal bezoekers (× 1000). De staaf van zaterdag stopt bij 4. Hoeveel bezoekers waren er?
    - **Opties:** A) 4 bezoekers · B) 400 bezoekers · C) 4000 bezoekers
    - **Antwoord:** 4000 bezoekers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 bezoekers → Je hebt het getal van de as overgenomen. Lees het tekstje bij de as nog eens. · 400 bezoekers → Je hebt met 100 vermenigvuldigd. Kijk goed welk getal er achter het maalteken staat.
    - **Uitleg (Claude):** Bij de as staat dat de getallen keer 1000 gaan. De staaf bij 4 betekent dus 4 keer 1000. Dat zijn 4000 bezoekers.

- **Hint 1 (te schrijven):** Lees het tekstje bij de as: wat betekent het stukje tussen haakjes?
- **Hint 2 (te schrijven):** Bij de as staat dat elk getal keer duizend gaat. Doe het getal waar de staaf stopt keer duizend.
- **Ouderzin:** Je kind leest een grafiek waarbij de getallen op de as keer duizend gaan.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal van de as` (4 bezoekers) → Dat is alleen het getal bij de as. Lees het tekstje bij de as nog eens: keer hoeveel gaat elk getal?  [nieuw]
  - `keer honderd` (400 bezoekers) → Dat is keer honderd. Lees nog eens wat er bij de as staat: keer hoeveel?  [nieuw]
  - `andere fout` (andere fout) → Lees het tekstje bij de as. Doe het getal waar de staaf stopt keer het getal tussen haakjes.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Bij de as van een grafiek staat: aantal bezoekers (x #). De staaf van zaterdag stopt bij #. Hoeveel [ding] waren er?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Tussen welke twee getallen stopt de staaf? Daar zit het aantal tussen.
- **Hint 2 (te schrijven):** De staaf stopt halverwege twee getallen op de as. Welk getal ligt precies in het midden van die twee? Kies de optie die daar het dichtst bij ligt.
- **Ouderzin:** Je kind schat een waarde die tussen twee getallen op de as ligt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stukje erboven` (Ongeveer 2 of 3) → Zo groot is alleen het stukje boven het lagere getal. De staaf begint bij nul: hoe ver komt hij in totaal?  [nieuw]
  - `opgeteld` (Precies 25) → Dat zijn de twee getallen samen. De staaf stopt tussen die twee getallen in, dus het aantal ligt daartussen.  [nieuw]
  - `andere fout` (andere fout) → Zoek de twee getallen waar de staaf tussen stopt, en schat wat er in het midden ligt.  [nieuw]
- Status: hints klaar

## Somtype 9: Boven een staafdiagram staat: "Het aantal bezoekers is verdubbeld." De staaf gaat van # naar #. Klopt die kop?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van # naar #. Klopt die kop?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De staaf lijkt misschien veel hoger. Kijk naar de getallen 20 en 24.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-004` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** Boven een staafdiagram staat: "Het aantal bezoekers is verdubbeld." De staaf gaat van 20 naar 24. Klopt die kop?
    - **Opties:** A) Ja, de staaf is twee keer zo hoog. · B) Ja, er zijn 4 bezoekers bij gekomen. · C) Nee, 24 is geen dubbel van 20.
    - **Antwoord:** Nee, 24 is geen dubbel van 20.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, de staaf is twee keer zo hoog. → De staaf lijkt misschien veel hoger. Kijk naar de getallen 20 en 24. · Ja, er zijn 4 bezoekers bij gekomen. → Verdubbelen is niet hetzelfde als er een paar bij krijgen. Wat is het dubbele van 20?
    - **Uitleg (Claude):** Het dubbele van 20 is 40, maar er staat 24. De groei is dus maar 4 bezoekers. Een kop boven een grafiek kan flink overdrijven.

- **Hint 1 (te schrijven):** Verdubbeld betekent: twee keer zoveel. Hoeveel is twee keer het getal aan het begin?
- **Hint 2 (te schrijven):** Reken uit wat er zou staan als het aantal echt twee keer zo groot was. Vergelijk dat met het getal waar de staaf nu stopt. Is het hetzelfde?
- **Ouderzin:** Je kind controleert met de getallen of een kop boven een grafiek klopt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `staaf lijkt hoger` (Ja, de staaf is twee keer zo hoog.) → Kijk niet naar hoe hoog de staaf lijkt, maar naar de getallen. Is het nieuwe getal twee keer zo groot als het oude?  [nieuw]
  - `een paar erbij` (Ja, er zijn 4 bezoekers bij gekomen.) → Er komen er wel een paar bij, maar verdubbelen is meer: twee keer zoveel. Is dat hier zo?  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel twee keer het oude getal is, en vergelijk dat met het nieuwe getal.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van # naar #. Klopt die kop?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Het plaatje is hoger én breder geworden. Wat gebeurt er dan met de ruimte die het inneemt?
- **Hint 2 (te schrijven):** Stel je het oude flesje voor als een rechthoek. Maak hem twee keer zo hoog en twee keer zo breed. Hoe vaak past het oude flesje dan in het nieuwe?
- **Ouderzin:** Je kind ziet dat een plaatje dat in hoogte én breedte groeit, groter lijkt dan het aantal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen de hoogte` (Niets, twee keer zo hoog is precies goed.) → Het flesje is niet alleen hoger, maar ook breder getekend. Kijk naar hoe groot het hele plaatje lijkt.  [nieuw]
  - `als een doos` (Het flesje lijkt acht keer zo groot.) → Een plaatje is plat: het heeft alleen een hoogte en een breedte. Hoe vaak past het oude plaatje in het nieuwe?  [nieuw]
  - `andere fout` (andere fout) → Hoe vaak past het oude plaatje in het nieuwe, als het twee keer zo hoog en twee keer zo breed is?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wat zeggen de percentages bij de twee stukken? En wat zie je met je ogen?
- **Hint 2 (te schrijven):** Stel je een taart voor die schuin voor je staat. Welk stuk neemt in de tekening de meeste ruimte in? Past dat bij de percentages?
- **Ouderzin:** Je kind ziet dat een schuin getekend cirkeldiagram de stukken anders laat lijken dan ze zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `echt groter` (Het voorste stuk is echt groter dan 25%.) → Bij de stukken staan percentages. Wat zeggen die getallen: is het ene stuk echt groter dan het andere?  [nieuw]
  - `kleuren` (Een cirkeldiagram mag geen kleuren hebben.) → Kleuren helpen juist bij het lezen. Het gaat hier om de schuine tekening.  [nieuw]
  - `andere fout` (andere fout) → Kijk naar de percentages bij de stukken, en vergelijk dat met wat je ziet.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wat kun je zonder getallen nog wel zien, en wat niet?
- **Hint 2 (te schrijven):** Zonder getallen bij de as zie je nog steeds welke staaf het hoogst is. Maar wat kun je dan niet aflezen?
- **Ouderzin:** Je kind ziet dat je zonder getallen bij de as geen aantallen kunt aflezen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleuren` (Je kunt de kleuren niet meer uit elkaar houden.) → Met de kleuren is niets mis. Het gaat om wat er bij de as hoort te staan.  [nieuw]
  - `welke hoger` (Je ziet niet welke staaf hoger is.) → Welke staaf hoger is, zie je juist wel. Maar kun je ook zeggen hoeveel elke staaf is?  [nieuw]
  - `andere fout` (andere fout) → Wat staat er normaal bij de as? Wat weet je niet als dat er niet bij staat?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wanneer gaan beide lijnen omhoog? Wat is er in die maanden anders?
- **Hint 2 (te schrijven):** Stijgen twee lijnen tegelijk, dan kan er één reden zijn voor beide. Welke reden past bij de maanden waarin ze stijgen?
- **Ouderzin:** Je kind leert dat twee lijnen die samen stijgen niet betekenen dat het ene door het andere komt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `dalen` (Nee, want de lijnen dalen juist samen.) → Lees nog eens wat er in de warme maanden met de lijnen gebeurt: gaan ze omhoog of omlaag?  [nieuw]
  - `samen stijgen` (Ja, want beide lijnen stijgen samen.) → Twee lijnen die samen stijgen, hoeven niet door elkaar te komen. Wat hebben ze met elkaar gemeen?  [nieuw]
  - `andere fout` (andere fout) → Wat is er anders in de maanden waarin beide lijnen stijgen?  [nieuw]
- Status: hints klaar

## Somtype 14: Een klas telt # kinderen. In een staafdiagram over huisdieren tellen de staven samen op tot #. Wat is hiervoor de beste verklaring?

- Sleutel: nrOrigineel **35** · somtypeOrigineel “Een klas telt # [ding]. In een staafdiagram over huisdieren zijn de staven samen # [ding]. Wat is hiervoor de beste verklaring?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-KRITISCH
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Denk eerst na of er een gewone reden kan zijn waarom een kind twee keer meetelt.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-041` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Een klas telt 25 kinderen. In een staafdiagram over huisdieren tellen de staven samen op tot 30. Wat is hiervoor de beste verklaring?
    - **Opties:** A) Sommige kinderen hebben meer dan één huisdier · B) De grafiek is fout getekend · C) Er zitten 30 kinderen in de klas
    - **Antwoord:** Sommige kinderen hebben meer dan één huisdier  (controle: n.v.t.)
    - **Fout-hints (Claude):** De grafiek is fout getekend → Denk eerst na of er een gewone reden kan zijn waarom een kind twee keer meetelt. · Er zitten 30 kinderen in de klas → In de vraag staat duidelijk hoeveel kinderen er in de klas zitten. Lees dat nog eens.
    - **Uitleg (Claude):** Een kind kan bij meerdere soorten huisdieren meegeteld worden. Daardoor is het totaal van de staven hoger dan het aantal kinderen. Dat is geen fout in de grafiek.

- **Hint 1 (te schrijven):** Tel je alle staven op, dan kom je boven het aantal in de klas uit. Hoe kan dat?
- **Hint 2 (te schrijven):** Elke staaf telt de kinderen met dat dier. Wat moet er gebeuren om samen boven het aantal in de klas uit te komen? Kies de uitleg die dat kan verklaren zonder dat er iets fout is.
- **Ouderzin:** Je kind zoekt een gewone verklaring voor een diagram dat optelt tot meer dan het aantal in de klas.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `fout getekend` (De grafiek is fout getekend) → Een diagram dat samen hoger uitkomt dan de klas, hoeft niet fout te zijn. Kan iemand bij twee staven meetellen?  [nieuw]
  - `getal uit het diagram` (Er zitten 30 kinderen in de klas) → Hoeveel er in de klas zitten, staat al in de vraag. Dat is minder dan de staven samen. Hoe kan dat dan?  [nieuw]
  - `andere fout` (andere fout) → Lees de vraag nog eens: hoeveel zitten er in de klas? Kan iemand bij twee staven meetellen?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een klas telt # [ding]. In een staafdiagram over huisdieren zijn de staven samen # [ding]. Wat is hiervoor de beste verklaring?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Een jaar heeft twaalf maanden. Welke maanden laat de winkel zien?
- **Hint 2 (te schrijven):** De winkel kiest zelf welke maanden in de grafiek komen. Wat gebeurt er met je beeld van het hele jaar als je alleen de beste maanden ziet?
- **Ouderzin:** Je kind ziet dat een grafiek misleidt als er gegevens weggelaten zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getallen fout` (De getallen bij die maanden kloppen niet.) → De getallen zelf kunnen best kloppen. Denk aan de maanden die er niet bij staan.  [nieuw]
  - `drie staven` (Drie staven zijn te weinig om te tekenen.) → Drie staven mag best. Het gaat erom welke maanden er weggelaten zijn.  [nieuw]
  - `andere fout` (andere fout) → Welke maanden staan er niet in de grafiek, en wat betekent dat?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Alle stukken van een cirkeldiagram vormen bij elkaar de hele cirkel. Hoeveel procent is dat?
- **Hint 2 (te schrijven):** Een hele cirkel is honderd procent. Tel de percentages van de stukken bij elkaar op. Wat valt je op?
- **Ouderzin:** Je kind controleert of de stukken van een cirkeldiagram samen honderd procent zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `grootste stuk` (Het grootste stuk moet 100% zijn.) → Eén stuk is altijd een deel van de cirkel. Hoeveel procent moeten alle stukken bij elkaar zijn?  [nieuw]
  - `te weinig stukken` (Er zijn te weinig stukken getekend.) → Het aantal stukken is geen probleem. Tel de percentages eens bij elkaar op.  [nieuw]
  - `andere fout` (andere fout) → Tel de percentages bij elkaar op. Hoeveel procent hoort een hele cirkel te zijn?  [nieuw]
- Status: hints klaar

## Somtype 17: In een grafiek staat onderaan de as het getal # en bovenaan het getal #. De lijn loopt naar [richting]. Wat betekent dat?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “In een grafiek staat onderaan de as het getal # en bovenaan het getal #. De lijn loopt naar [richting]. Wat betekent dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je bent gewend dat omhoog meer betekent. Lees hier eerst de getallen bij de as.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-011` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een grafiek staat onderaan de as het getal 100 en bovenaan het getal 0. De lijn loopt naar beneden. Wat betekent dat?
    - **Opties:** A) Het aantal wordt groter. · B) Het aantal wordt steeds kleiner. · C) Het aantal blijft de hele tijd gelijk.
    - **Antwoord:** Het aantal wordt groter.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Het aantal wordt steeds kleiner. → Je bent gewend dat omhoog meer betekent. Lees hier eerst de getallen bij de as. · Het aantal blijft de hele tijd gelijk. → De lijn loopt duidelijk niet recht. Kijk naar de getallen waar de lijn langs gaat.
    - **Uitleg (Claude):** Hier staan de getallen omgekeerd: hoe lager op de as, hoe groter het getal. Een dalende lijn hoort dus bij grotere aantallen. Kijk altijd eerst naar de getallen bij de as.

- **Hint 1 (te schrijven):** Kijk eerst welke getallen onderaan en bovenaan de as staan.
- **Hint 2 (te schrijven):** Hier staan de hoge getallen onderaan en de lage bovenaan. Loopt de lijn omlaag, naar welke getallen gaat hij dan?
- **Ouderzin:** Je kind leest een grafiek waarbij de getallen op de as omgekeerd staan.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omlaag is minder` (Het aantal wordt steeds kleiner.) → Meestal betekent omlaag: minder. Maar lees hier eerst de getallen bij de as. Waar staan de hoge getallen?  [nieuw]
  - `gelijk` (Het aantal blijft de hele tijd gelijk.) → De lijn loopt niet recht, dus het aantal verandert. Kijk naar welke getallen de lijn gaat.  [nieuw]
  - `andere fout` (andere fout) → Lees eerst de getallen bij de as. Naar welke getallen loopt de lijn?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Hoeveel meer: dan zoek je het verschil tussen de twee getallen.
- **Hint 2 (te schrijven):** Tel door van het kleinste getal naar het grootste. Hoeveel stapjes zijn dat? De staven kunnen ver uit elkaar lijken, maar lees de getallen.
- **Ouderzin:** Je kind leest twee staven af en rekent het verschil uit.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tiental` (10 meer) → Tel nog eens rustig door, met stapjes van één. Hoeveel stapjes zijn het?  [nieuw]
  - `opgeteld` (196 meer) → Dat zijn de twee getallen samen. Bij hoeveel meer vergelijk je de getallen: trek ze van elkaar af.  [nieuw]
  - `andere fout` (andere fout) → Tel door van het kleinste getal naar het grootste. Hoeveel stapjes zijn dat?  [nieuw]
- Status: hints klaar

## Somtype 19: In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei # hoog. Wat weet je zeker?

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

- **Hint 1 (te schrijven):** Welke getallen worden allemaal hetzelfde getal als je afrondt op honderdtallen?
- **Hint 2 (te schrijven):** Bij afronden kan een getal omhoog of omlaag gaan. Bedenk twee getallen die niet even groot zijn, maar allebei op hetzelfde honderdtal uitkomen. Wat zegt dat over de staven?
- **Ouderzin:** Je kind ziet dat afgeronde getallen in een grafiek kleine verschillen kunnen verbergen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen omhoog` (Beide aantallen zijn meer dan 300.) → Bij afronden kun je omhoog en omlaag gaan. Kan een getal onder het honderdtal ook op dat honderdtal uitkomen?  [nieuw]
  - `precies gelijk` (De echte aantallen zijn precies gelijk.) → Denk eens aan alle getallen die afgerond op hetzelfde honderdtal uitkomen. Zijn die allemaal even groot?  [nieuw]
  - `andere fout` (andere fout) → Welke getallen komen allemaal op hetzelfde honderdtal uit als je afrondt?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei # [ding]. Wat weet je zeker?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 20: In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor # stuks. Waarom fopt dit je?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor # [ding]. Waarom fopt dit je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (1), grafiek-verkeerd-afgelezen (1)
- Verschillende Claude-fout-hints: 2 (meest: “In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-014` (Claude G8, ai, niveau 1 → basis)
    - **Opgave:** In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor 10 stuks. Waarom fopt dit je?
    - **Opties:** A) Het grote plaatje lijkt voor veel meer stuks te staan. · B) Peren zijn nu eenmaal groter dan appels. · C) Er staan te weinig plaatjes bij appels.
    - **Antwoord:** Het grote plaatje lijkt voor veel meer stuks te staan.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Peren zijn nu eenmaal groter dan appels. → In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien. · Er staan te weinig plaatjes bij appels. → Het aantal plaatjes klopt juist wel. Let op het verschil in grootte.
    - **Uitleg (Claude):** In een plaatjesgrafiek moet elk plaatje even groot zijn. Anders denk je bij een groot plaatje meteen aan een groot aantal. Hier staan beide plaatjes toch echt voor 10 stuks.

- **Hint 1 (te schrijven):** Beide plaatjes staan voor hetzelfde aantal. Waar kijken je ogen naar?
- **Hint 2 (te schrijven):** Bij een plaatjesgrafiek horen alle plaatjes dezelfde grootte te hebben. Wat denk je als je een groot plaatje naast een klein plaatje ziet?
- **Ouderzin:** Je kind ziet dat plaatjes van verschillende grootte in een plaatjesgrafiek misleiden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `echt fruit` (Peren zijn nu eenmaal groter dan appels.) → In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien.  [nieuw]
  - `aantal plaatjes` (Er staan te weinig plaatjes bij appels.) → Het aantal plaatjes klopt juist wel. Let op hoe groot de plaatjes getekend zijn.  [nieuw]
  - `andere fout` (andere fout) → Staan de plaatjes voor hetzelfde aantal? Kijk hoe groot ze getekend zijn.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan voor # [ding]. Waarom fopt dit je?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 21: In een plaatjesgrafiek staat een fietsje voor # kinderen. Bij groep # staan # fietsjes. Hoeveel kinderen zijn dat?

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

- **Hint 1 (te schrijven):** Lees eerst voor hoeveel er één plaatje staat.
- **Hint 2 (te schrijven):** Eén plaatje staat voor een groepje. Tel de plaatjes en doe dat aantal keer de grootte van het groepje.
- **Ouderzin:** Je kind leest een plaatjesgrafiek: het aantal plaatjes keer wat één plaatje betekent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plaatjes geteld` (6 kinderen) → Dat is het aantal plaatjes. Eén plaatje staat voor meer dan één: lees nog eens voor hoeveel.  [nieuw]
  - `opgeteld` (16 kinderen) → Dat is het aantal plaatjes plus het getal bij één plaatje. Elk plaatje staat voor een heel groepje: doe keer.  [nieuw]
  - `andere fout` (andere fout) → Lees voor hoeveel één plaatje staat. Doe het aantal plaatjes keer dat getal.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een plaatjesgrafiek staat een fietsje voor # [ding]. Bij groep # [ding] # [ding]. Hoeveel [ding] zijn dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 22: In een plaatjesgrafiek staat één hondje voor # [ding]. [Plek] staan # hele hondjes en # half hondje. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en # [ding] hondje. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het halve plaatje als een heel plaatje geteld. Voor hoeveel honden staat een half hondje?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-016` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** In een plaatjesgrafiek staat één hondje voor 6 honden. Bij het asiel staan 3 hele hondjes en 1 half hondje. Hoeveel honden zijn dat?
    - **Opties:** A) 24 honden · B) 4 honden · C) 21 honden
    - **Antwoord:** 21 honden  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 honden → Je hebt het halve plaatje als een heel plaatje geteld. Voor hoeveel honden staat een half hondje? · 4 honden → Je hebt de plaatjes geteld in plaats van de honden. Elk heel plaatje staat voor meer dan één hond.
    - **Uitleg (Claude):** Drie hele hondjes zijn 3 keer 6, dus 18 honden. Een half hondje is de helft van 6, dus 3 honden. Samen zijn dat 21 honden.

- **Hint 1 (te schrijven):** Een half plaatje staat voor de helft van wat één plaatje betekent.
- **Hint 2 (te schrijven):** Reken eerst de volle plaatjes uit: het aantal keer wat één plaatje betekent. Het halve plaatje is de helft daarvan. Tel die twee bij elkaar op.
- **Ouderzin:** Je kind leest een plaatjesgrafiek met een half plaatje: dat telt voor de helft.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `halve als volle` (24 honden) → Zo telt het halve plaatje mee als een vol plaatje. Voor hoeveel staat het halve plaatje?  [nieuw]
  - `plaatjes geteld` (4 honden) → Dat is het aantal plaatjes. Eén plaatje staat voor meer dan één: reken uit wat alle plaatjes samen betekenen.  [nieuw]
  - `andere fout` (andere fout) → Reken de volle plaatjes uit en tel de helft van één plaatje erbij.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en # [ding] hondje. Hoeveel [ding] zijn dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 23: In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “In een staafdiagram vertelt alleen de hoogte het aantal. Wat zegt de breedte dan?”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-017` (Claude G8, ai, niveau 2 → toepassen)
    - **Opgave:** In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom kan dat je foppen?
    - **Opties:** A) De brede staaf hoort bij meer kinderen. · B) Staven mogen nooit naast elkaar staan. · C) De brede staaf lijkt bij een groter aantal te horen.
    - **Antwoord:** De brede staaf lijkt bij een groter aantal te horen.  (controle: n.v.t.)
    - **Fout-hints (Claude):** De brede staaf hoort bij meer kinderen. → In een staafdiagram vertelt alleen de hoogte het aantal. Wat zegt de breedte dan? · Staven mogen nooit naast elkaar staan. → Staven naast elkaar is heel normaal. Let op het verschil in breedte.
    - **Uitleg (Claude):** In een staafdiagram lees je het aantal af aan de hoogte. Een bredere staaf ziet er groter uit, maar hoort bij hetzelfde aantal. Alle staven horen even breed te zijn.

- **Hint 1 (te schrijven):** Waaraan zie je in een staafdiagram hoeveel het is: aan de hoogte of aan de breedte?
- **Hint 2 (te schrijven):** In een staafdiagram telt alleen de hoogte. Twee staven die even hoog zijn, staan voor evenveel. Wat doet een bredere staaf dan met je ogen?
- **Ouderzin:** Je kind ziet dat de breedte van een staaf niets zegt, maar wel kan misleiden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `breed is meer` (De brede staaf hoort bij meer kinderen.) → In een staafdiagram vertelt alleen de hoogte hoeveel het is. Wat zegt de breedte dan?  [nieuw]
  - `naast elkaar` (Staven mogen nooit naast elkaar staan.) → Staven naast elkaar is heel gewoon. Let op het verschil in breedte.  [nieuw]
  - `andere fout` (andere fout) → Kijk alleen naar de hoogte van de staven. Wat doet de breedte met je ogen?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Bij welk getal begint de as? Welk stuk van de staven zie je dan niet?
- **Hint 2 (te schrijven):** Begint de as niet bij nul, dan zie je van elke staaf alleen het stuk boven het begingetal. Stel dat de ene staaf maar een klein beetje hoger is dan de andere. Hoe ziet dat er dan uit?
- **Ouderzin:** Je kind ziet dat een as die niet bij nul begint verschillen groter laat lijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te dicht` (De staven staan te dicht bij elkaar.) → De afstand tussen de staven maakt niets uit. Kijk nog eens bij welk getal de as begint.  [nieuw]
  - `te weinig geteld` (Er zijn te weinig boeken geteld.) → Met de aantallen is niets mis. Kijk naar waar de as begint.  [nieuw]
  - `andere fout` (andere fout) → Kijk bij welk getal de as begint. Wat zie je dan van de staven?  [nieuw]
- Status: hints klaar

## Somtype 25: In klas A kiest #% van de # kinderen voor voetbal. In klas B kiest #% van de # kinderen voor voetbal. Welke klas heeft de meeste voetballers?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “In klas A kiest #% van de # [ding] voor voetbal. In klas B kiest #% van de # [ding] voor voetbal. Welke klas heeft de meeste voetballers?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G8 (1) · regel: G8-G8-kritisch
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): procent-verkeerde-basis (1), deel-van-geheel-verkeerd (1)
- Verschillende Claude-fout-hints: 2 (meest: “Een percentage hoort altijd bij een totaal. De klassen zijn niet even groot.”)
- Voorbeelden:
  - `G8-VBN-E04-claude-bank-019` (Claude G8, ai, niveau 3 → toepassen)
    - **Opgave:** In klas A kiest 50% van de 20 kinderen voor voetbal. In klas B kiest 40% van de 30 kinderen voor voetbal. Welke klas heeft de meeste voetballers?
    - **Opties:** A) Klas B, want dat zijn 12 kinderen. · B) Klas A, want 50% is meer dan 40%. · C) Ze hebben allebei evenveel voetballers.
    - **Antwoord:** Klas B, want dat zijn 12 kinderen.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Klas A, want 50% is meer dan 40%. → Een percentage hoort altijd bij een totaal. De klassen zijn niet even groot. · Ze hebben allebei evenveel voetballers. → Reken beide percentages eerst om naar echte aantallen kinderen.
    - **Uitleg (Claude):** 50% van 20 is 10 kinderen en 40% van 30 is 12 kinderen. Het grootste percentage hoort dus niet bij het grootste aantal. Kijk altijd bij welk totaal een percentage hoort.

- **Hint 1 (te schrijven):** Een percentage is een deel van een totaal. Zijn de twee klassen even groot?
- **Hint 2 (te schrijven):** Reken voor elke klas uit hoeveel voetballers het zijn: het percentage van het aantal in die klas. Vergelijk daarna de aantallen, niet de percentages.
- **Ouderzin:** Je kind vergelijkt aantallen in plaats van percentages als de groepen niet even groot zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `percentages vergeleken` (Klas A, want 50% is meer dan 40%.) → Een groter percentage hoeft geen groter aantal te zijn. De klassen zijn niet even groot: reken de aantallen uit.  [nieuw]
  - `evenveel` (Ze hebben allebei evenveel voetballers.) → Reken voor allebei de klassen het percentage om naar een echt aantal. Komt er hetzelfde uit?  [nieuw]
  - `andere fout` (andere fout) → Reken voor elke klas het aantal voetballers uit, en vergelijk de aantallen.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In klas A kiest #% van de # [ding] voor voetbal. In klas B kiest #% van de # [ding] voor voetbal. Welke klas heeft de meeste voetballers?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wat toont een cirkeldiagram: aantallen of percentages? En wat wordt er gevraagd?
- **Hint 2 (te schrijven):** Een percentage is een deel van het totaal. Om een aantal uit te rekenen, heb je het totaal nodig. Staat dat ergens?
- **Ouderzin:** Je kind ziet dat een cirkeldiagram met percentages zonder totaal geen aantallen geeft.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `percentage als aantal` (40 kinderen hebben een hond gekozen.) → Een percentage is geen aantal. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat erbij?  [nieuw]
  - `tiende` (4 kinderen hebben een hond gekozen.) → Een percentage is geen aantal, en een tiende ervan ook niet. Zonder het totaal kun je geen aantal uitrekenen.  [nieuw]
  - `andere fout` (andere fout) → Een cirkeldiagram toont percentages. Weet je hoeveel er in totaal meededen?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Hoeveel jaren komen er telkens bij van het ene jaartal naar het volgende?
- **Hint 2 (te schrijven):** Op een tijdas hoort dezelfde afstand bij dezelfde tijd. Reken bij elk paar jaartallen naast elkaar uit hoeveel jaar ertussen ligt. Is dat steeds evenveel?
- **Ouderzin:** Je kind ziet dat een tijdas misleidt als de jaartallen niet in gelijke stappen oplopen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `volgorde` (De jaren staan in de verkeerde volgorde.) → De volgorde van klein naar groot klopt. Kijk naar hoeveel jaar er tussen de jaartallen zit.  [nieuw]
  - `aantal punten` (Er horen precies vier punten in een lijngrafiek.) → Het aantal punten mag je zelf kiezen. Let op hoeveel jaar er tussen twee punten zit.  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel jaar er tussen twee jaartallen naast elkaar zit. Is dat steeds evenveel?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Wie vroeg Sanne het? Houden die kinderen net zo veel van schaken als de rest van de school?
- **Hint 2 (te schrijven):** Stel dat Sanne het aan alle kinderen van de school vraagt. Zou dan ook zo goed als iedereen schaken zeggen? Kies de uitleg die past bij dat verschil.
- **Ouderzin:** Je kind ziet dat een onderzoek alleen eerlijk is als je het vraagt aan kinderen die lijken op iedereen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te weinig` (Zij vroeg het aan te weinig kinderen) → Stel dat ze honderd schakers vraagt. Zou de uitkomst dan eerlijker zijn? Lijken die kinderen op alle kinderen van de school?  [nieuw]
  - `niets mis` (Er is niets mis met haar onderzoek) → Op een schaakclub zitten kinderen die graag schaken. Lijken zij op alle kinderen van de school?  [nieuw]
  - `andere fout` (andere fout) → Lijken de kinderen die Sanne vroeg op alle kinderen van de school?  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Een plant groeit langzaam. Metingen die kloppen, liggen dicht bij elkaar.
- **Hint 2 (te schrijven):** Zet de metingen op volgorde. Kijk hoe groot de stap is tussen twee metingen naast elkaar. Waar is die stap veel groter dan de rest?
- **Ouderzin:** Je kind zoekt de meting die ver van de andere af ligt (een uitschieter): die is waarschijnlijk fout gemeten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleinste` (10 cm) → Die meting ligt dicht bij de andere. Zoek de meting die er ver vandaan ligt.  [nieuw]
  - `dichtbij` (15 cm) → Die meting past bij de andere: het verschil is klein. Zoek de meting die er ver vandaan ligt.  [nieuw]
  - `andere fout` (andere fout) → Zoek de meting die ver van de andere af ligt.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Kijk tot welk getal elke as loopt. Zijn de assen hetzelfde?
- **Hint 2 (te schrijven):** Stel dat beide lijnen van onderaan tot halverwege hun as stijgen. Hoeveel is dat bij de ene as, en hoeveel bij de andere?
- **Ouderzin:** Je kind vergelijkt twee grafieken pas na het vergelijken van de assen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine as` (De grafiek met de as tot 50 stijgt het meest.) → Kijk hoeveel elke as per hokje omhoog gaat. Bij welke as hoort bij dezelfde steilheid het grootste aantal?  [nieuw]
  - `evenveel` (Beide grafieken stijgen precies evenveel.) → De lijnen lijken hetzelfde, maar de assen zijn dat niet. Vergelijk de getallen bij de assen.  [nieuw]
  - `andere fout` (andere fout) → Vergelijk eerst tot welk getal elke as loopt, en dan pas de lijnen.  [nieuw]
- Status: hints klaar

## Somtype 31: Voor een onderzoek over het lievelingsvak zijn # kinderen uit één klas gevraagd. De kop zegt: de hele school kiest rekenen. Klopt dat?

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

- **Hint 1 (te schrijven):** Hoeveel zijn er gevraagd, en hoeveel zitten er op de hele school?
- **Hint 2 (te schrijven):** Een kop over de hele school moet gaan over veel leerlingen uit verschillende klassen. Is dat hier zo?
- **Ouderzin:** Je kind ziet dat een onderzoek bij een paar leerlingen uit één klas niets zegt over de hele school.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `allemaal rekenen` (Ja, want alle 5 kozen voor rekenen.) → Die paar kozen inderdaad rekenen. Maar hoeveel zitten er op de hele school?  [nieuw]
  - `één klas` (Ja, één klas lijkt op alle klassen.) → Denk aan de andere klassen. Zouden die precies hetzelfde kiezen?  [nieuw]
  - `andere fout` (andere fout) → Hoeveel zijn er gevraagd? Zegt dat iets over de hele school?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Voor een onderzoek over het lievelingsvak zijn # [ding] uit één klas gevraagd. De kop zegt: de hele school kiest rekenen. Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.
- **Hint 2 (te schrijven):** Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?
- **Ouderzin:** Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nee` (Nee, dat klopt niet.) → Lees de twee staven nog eens af en tel hun percentages op. Is dat samen meer dan vijftig procent?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee percentages op en vergelijk met vijftig procent.  [nieuw]
- Status: hints klaar

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
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "hond", "waarde": 30}, {"naam": "kat", "waarde": 10}, {"naam": "konijn", "waarde": 15}, {"naam": "vis", "waarde": 45}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Dat kun je hier niet zien. · B) Nee, dat klopt niet. · C) Ja, dat klopt.
    - **Antwoord:** Nee, dat klopt niet.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, dat klopt. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 30% + 10% = 40%. Dat is niet meer dan 50%.

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.
- **Hint 2 (te schrijven):** Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?
- **Ouderzin:** Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Lees de twee staven nog eens af en tel hun percentages op. Komt dat samen echt boven de vijftig procent uit?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee percentages op en vergelijk met vijftig procent.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.
- **Hint 2 (te schrijven):** Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?
- **Ouderzin:** Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nee` (Nee, dat klopt niet.) → Lees de twee staven nog eens af en tel hun percentages op. Is dat samen meer dan vijftig procent?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee percentages op en vergelijk met vijftig procent.  [nieuw]
- Status: hints klaar

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

- **Hint 1 (te schrijven):** Lees de twee staven af die in de zin staan.
- **Hint 2 (te schrijven):** Lees de staaf van tekenen en de andere staaf uit de zin af. Doe de andere staaf keer het getal uit de zin. Komt dat precies uit op de staaf van tekenen?
- **Ouderzin:** Je kind leest twee percentages af en controleert of het ene precies een aantal keer zo groot is als het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Reken het na: doe de andere staaf keer het getal uit de zin. Komt dat precies uit op tekenen?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → De twee percentages staan in het diagram. Dan kun je ze vergelijken: lees ze af en reken het na.  [nieuw]
  - `andere fout` (andere fout) → Lees de twee staven af en reken na of het klopt.  [nieuw]
- Status: hints klaar

## Somtype 36: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?

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

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent.
- **Hint 2 (te schrijven):** Zoek de staaf die in de zin genoemd wordt. Lees af hoe hoog hij komt: elk streepje is tien procent. Komt hij boven de vijftig procent uit?
- **Ouderzin:** Je kind leest een percentage af in een staafdiagram en vergelijkt het met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ja` (Ja, dat klopt.) → Lees het percentage van die staaf nog eens af. Komt hij echt boven de vijftig procent uit?  [nieuw]
  - `nee` (Nee, dat klopt niet.) → Lees het percentage van die staaf nog eens af. Meer dan de helft is meer dan vijftig procent. Hoe hoog komt de staaf?  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → Meer dan de helft is ook een percentage: meer dan vijftig procent. Dat lees je af aan de staaf.  [nieuw]
  - `andere fout` (andere fout) → Lees de staaf af en vergelijk met vijftig procent.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Meer dan de helft van [wie] kiest [naam]." Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 37: [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder staat: "Water en [naam] zijn samen meer dan de helft." Klopt dat?

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
    - **Tekening:** `{"max": 60, "soort": "staafdiagram", "staven": [{"naam": "water", "waarde": 30}, {"naam": "melk", "waarde": 30}, {"naam": "sap", "waarde": 10}, {"naam": "niets", "waarde": 30}], "cijfer_om": 1, "perstreep": 10}`
    - **Opties:** A) Nee, dat klopt niet. · B) Dat kun je hier niet zien. · C) Ja, dat klopt.
    - **Antwoord:** Ja, dat klopt.  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, dat klopt niet. → Lees de percentages van de staven af en reken de bewering na. · Dat kun je hier niet zien. → Alles wat je nodig hebt staat in het diagram: lees de percentages af en reken na.
    - **Uitleg (Claude):** 30% + 30% = 60%. Dat is meer dan 50%.

- **Hint 1 (te schrijven):** Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.
- **Hint 2 (te schrijven):** Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?
- **Ouderzin:** Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nee` (Nee, dat klopt niet.) → Kijk naar de twee staven samen, niet naar één staaf. Tel hun percentages op.  [nieuw]
  - `niet te zien` (Dat kun je hier niet zien.) → De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee percentages op en vergelijk met vijftig procent.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [ding]?" en toont percentages. Eronder staat: "Water en [naam] zijn samen meer dan de helft." Klopt dat?'. Nakijken of ze nog passen.
- Status: hints klaar
