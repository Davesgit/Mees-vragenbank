# G4-GET-M05 — Slim rekenen tot honderd

Onze omschrijving: +/− tot ≥100: rijg- en splitsstrategie (opbouw) · in onze bank: 8 items

Claude-vragen gemapt: **126** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — hele tientallen

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — hele tientallen” (koppeling: claudeId)
- Items: **34** · Claude-doelen: D4-2 (32), D4-4 (2) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 bos/poesjes → dierentuin/vissen (1), #25 bos/wortels → kinderboerderij/wortels (1), #25 gymzaal/stickers → huis/stickers (1), #25 gymzaal/stickers → klas/stickers (1), #25 moeras/tanden → museum/botten (1), #25 museum/tanden → museum/schelpen (1), #25 nest/blaadjes → museum/schelpen (1), #25 nest/eieren → kinderboerderij/eieren (1), #25 nest/schelpen → museum/schelpen (1), #25 stadion/stickers → huis/stickers (1), #25 stadion/stickers → klas/stickers (1), #25 vallei/blaadjes → museum/schelpen (1), #25 vallei/botten → museum/botten (1), #25 vallei/eieren → schuur/eieren (1), #34 shirts → truien (2)
- Denkfouten (Claude): tiental-ernaast (34), verkeerde-bewerking (34), plaatswaarde-verkeerd (32), een-ernaast (2)
- Verschillende Claude-fout-hints: 12 (meest: “Tel de tientallen nog eens: één tiental te veel eraf.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-021` (Claude D4-2, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het museum liggen 35 schelpen. Er gaan er 20 weg. Hoeveel schelpen blijven er over?
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** 33 → Je haalt 2 eraf, maar het zijn 2 tientallen. Dat is 20. · 5 → Tel de tientallen nog eens: één tiental te veel eraf. · 55 → Er gaat weg, dus het getal wordt kleiner.
    - **Uitleg (Claude):** Alleen de tientallen veranderen: 3 tientallen − 2 tientallen = 1 tientallen. De 5 blijft staan: 15.
  - `G4-GET-M05-claude-bank-033` (Claude D4-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de klas liggen 79 stickers. Er gaan er 10 weg. Hoeveel blijven er over?
    - **Antwoord:** 69  (controle: ok)
    - **Fout-hints (Claude):** 79 → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens. · 70 → Ga eerst naar 70, en haal dan 1 eraf. · 89 → Er gaat weg: het getal wordt kleiner.
    - **Uitleg (Claude):** Eerst naar het tiental: 79 − 9 = 70. Dan de rest eraf: 70 − 1 = 69.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Hoeveel tientallen gaan er weg?
- **Hint 2 (te schrijven):** Spring vanaf het eerste getal terug in sprongen van tien: één sprong voor elk tiental dat weggaat. Het cijfer achteraan blijft hetzelfde.
- **Ouderzin:** Je kind haalt hele tientallen af van een getal tot 100, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `een tiental te veel eraf` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel de tientallen die weggaan nog eens.  [Claude, taalfix]
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus het getal wordt kleiner.  [Claude, taalfix]
  - `alleen het cijfer eraf` (alleen het cijfer van de tientallen eraf (tekst per item)) → Je haalt … eraf, maar het zijn … tientallen. Dat is ….  [Claude, ok]
  - `een tiental te weinig eraf` (fout = antwoord + 10) → Dat is te veel. Er moet nog een tiental af.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Bij hele tientallen blijft het cijfer achteraan hetzelfde.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoeveel tientallen er weggaan. Spring zo vaak een tiental terug. Het cijfer achteraan blijft hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel [ding] zijn het er nu? — hele tientallen

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel [ding] zijn het er nu? — hele tientallen” (koppeling: claudeId)
- Items: **32** · Claude-doelen: D4-1 (32) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 bos/poesjes → dierentuin/vissen (1), #25 bos/wortels → dierentuin/wortels (1), #25 dierentuin/poesjes → dierentuin/wortels (1), #25 moeras/blaadjes → museum/schelpen (1), #25 moeras/eieren → kinderboerderij/eieren (1), #25 moeras/schelpen → museum/schelpen (1), #25 moeras/tanden → museum/botten (1), #25 museum/tanden → museum/stenen (1), #25 nest/eieren → schuur/eieren (1), #25 nest/schelpen → museum/schelpen (2), #25 schuur/vissen → dierentuin/vissen (1), #25 veld/kaartjes → stadion/kaartjes (1), #27 negatieve sleutel → positief (12), #34 shirts → truien (1)
- Denkfouten (Claude): plaatswaarde-verkeerd (32), tiental-ernaast (32), verkeerde-bewerking (32)
- Verschillende Claude-fout-hints: 10 (meest: “Tel de tientallen nog eens: één tiental te veel.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-074` (Claude D4-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het museum liggen 47 stenen. Er komen er 20 bij. Hoeveel stenen zijn het er nu?
    - **Antwoord:** 67  (controle: ok)
    - **Fout-hints (Claude):** 49 → Je telt 2 erbij, maar het zijn 2 tientallen. Dat is 20. · 77 → Tel de tientallen nog eens: één tiental te veel. · 27 → Er komt bij, dus het getal wordt groter.
    - **Uitleg (Claude):** Alleen de tientallen veranderen: 4 tientallen + 2 tientallen = 6 tientallen. De 7 blijft staan: 67.
  - `G4-GET-M05-claude-bank-065` (Claude D4-1, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de dierentuin liggen 56 wortels. Er komen er 30 bij. Hoeveel wortels zijn het er nu?
    - **Antwoord:** 86  (controle: ok)
    - **Fout-hints (Claude):** 59 → Je telt 3 erbij, maar het zijn 3 tientallen. Dat is 30. · 96 → Tel de tientallen nog eens: één tiental te veel. · 26 → Er komt bij, dus het getal wordt groter.
    - **Uitleg (Claude):** Alleen de tientallen veranderen: 5 tientallen + 3 tientallen = 8 tientallen. De 6 blijft staan: 86.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Hoeveel tientallen komen erbij?
- **Hint 2 (te schrijven):** Spring vanaf het eerste getal vooruit in sprongen van tien: één sprong voor elk tiental dat erbij komt. Het cijfer achteraan blijft hetzelfde.
- **Ouderzin:** Je kind telt hele tientallen bij een getal tot 100, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets erbij` (fout = antwoord − getal2) → Dat is het getal waarmee je begint. Er komen dingen bij, dus het worden er meer.  [nieuw]
  - `een tiental te veel` (fout = antwoord + 10) → Tel de tientallen nog eens: één tiental te veel.  [Claude, ok]
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het getal wordt groter.  [Claude, taalfix]
  - `alleen het cijfer erbij` (alleen het cijfer van de tientallen erbij (tekst per item)) → Je telt … erbij, maar het zijn … tientallen. Dat is ….  [Claude, ok]
  - `een tiental te weinig` (fout = antwoord − 10) → Dat is te weinig. Er moet nog een tiental bij.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Bij hele tientallen blijft het cijfer achteraan hetzelfde.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoeveel tientallen erbij komen. Spring zo vaak een tiental verder. Het cijfer achteraan blijft hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 3: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — over het tiental

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — over het tiental” (koppeling: claudeId)
- Items: **20** · Claude-doelen: D4-3 (20) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 bos/poesjes → dierentuin/vissen (1), #25 gymzaal/stenen → museum/stenen (1), #25 huis/stenen → museum/stenen (1), #25 kantine/pionnen → stadion/pionnen (1), #25 moeras/schelpen → museum/schelpen (1), #25 moeras/tanden → museum/botten (1), #25 nest/botten → museum/botten (1), #25 nest/schelpen → museum/schelpen (1)
- Denkfouten (Claude): tiental-ernaast (20), een-ernaast (20), verkeerde-bewerking (20)
- Verschillende Claude-fout-hints: 21 (meest: “Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-114` (Claude D4-3, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het museum liggen 73 botten. Er komen er 8 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 81  (controle: ok)
    - **Fout-hints (Claude):** 71 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 80 → Ga eerst naar 80, en tel dan 1 erbij. · 65 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 73 + 7 = 80. Dan de rest erbij: 80 + 1 = 81.
  - `G4-GET-M05-claude-bank-102` (Claude D4-3, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het huis liggen 58 stickers. Er komen er 8 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 66  (controle: ok)
    - **Fout-hints (Claude):** 56 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 65 → Ga eerst naar 60, en tel dan 6 erbij. · 50 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 58 + 2 = 60. Dan de rest erbij: 60 + 6 = 66.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Je komt over een tiental heen.
- **Hint 2 (te schrijven):** Heeft het tweede getal tientallen? Tel die eerst erbij. Tel dan de eenheden erbij: eerst tot het volgende hele tiental, daarna de rest.
- **Ouderzin:** Je kind telt bij een getal tot 100 iets op en gaat daarbij over een tiental heen, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets erbij` (fout = antwoord − getal2) → Dat is het getal waarmee je begint. Er komen dingen bij, dus het worden er meer.  [nieuw]
  - `tiental vergeten` (fout = antwoord − 10) → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens.  [Claude, ok]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Ga eerst naar het volgende hele tiental, en tel dan de rest erbij.  [nieuw]
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het getal wordt groter.  [Claude, taalfix]
  - `een tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Ga eerst naar het volgende hele tiental, en tel dan de rest erbij.  [nieuw]
  - `andere fout` (andere fout) → Heeft het tweede getal tientallen? Tel die eerst erbij. Tel dan de eenheden erbij: eerst tot het hele tiental, daarna de rest.  [nieuw]
- Status: hints klaar

## Somtype 4: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — over het tiental

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — over het tiental” (koppeling: claudeId)
- Items: **18** · Claude-doelen: D4-4 (18) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 bos/vissen → dierentuin/vissen (1), #25 gymzaal/sterren → huis/sterren (1), #25 gymzaal/stickers → klas/stickers (1), #25 kinderboerderij/vissen → dierentuin/vissen (1), #25 moeras/botten → museum/botten (1), #25 nest/blaadjes → museum/schelpen (1), #25 nest/eieren → schuur/eieren (2), #25 vallei/botten → museum/botten (1), #34 shirts → truien (3)
- Denkfouten (Claude): tiental-ernaast (18), een-ernaast (18), verkeerde-bewerking (18), kleinste-van-grootste (13)
- Verschillende Claude-fout-hints: 19 (meest: “Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-043` (Claude D4-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de schuur liggen 22 eieren. Er gaan er 8 weg. Hoeveel blijven er over?
    - **Antwoord:** 14  (controle: ok)
    - **Fout-hints (Claude):** 24 → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens. · 15 → Ga eerst naar 20, en haal dan 6 eraf. · 30 → Er gaat weg: het getal wordt kleiner. · 26 → Bij de eenheden kun je niet zomaar de kleinste van de grootste afhalen. Ga via het tiental.
    - **Uitleg (Claude):** Eerst naar het tiental: 22 − 2 = 20. Dan de rest eraf: 20 − 6 = 14.
  - `G4-GET-M05-claude-bank-049` (Claude D4-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de dierentuin liggen 92 vissen. Er gaan er 4 weg. Hoeveel blijven er over?
    - **Antwoord:** 88  (controle: ok)
    - **Fout-hints (Claude):** 98 → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens. · 89 → Ga eerst naar 90, en haal dan 2 eraf. · 96 → Er gaat weg: het getal wordt kleiner. · 92 → Bij de eenheden kun je niet zomaar de kleinste van de grootste afhalen. Ga via het tiental.
    - **Uitleg (Claude):** Eerst naar het tiental: 92 − 2 = 90. Dan de rest eraf: 90 − 2 = 88.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Je gaat terug over een tiental heen.
- **Hint 2 (te schrijven):** Heeft het tweede getal tientallen? Haal die eerst eraf. Haal dan de eenheden eraf: eerst terug tot het hele tiental, daarna de rest.
- **Ouderzin:** Je kind haalt iets af van een getal tot 100 en gaat daarbij terug over een tiental heen, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `tiental vergeten` (fout = antwoord + 10) → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens.  [Claude, ok]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Ga eerst terug naar het hele tiental, en haal dan de rest eraf.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus het getal wordt kleiner.  [Claude, taalfix]
  - `een tiental te veel eraf` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel de tientallen nog eens.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Ga eerst terug tot het hele tiental, en haal dan de rest eraf.  [nieuw]
  - `kleinste van de grootste` (fout = antwoord + 2 of meer) → Bij de eenheden kun je het kleine cijfer niet zomaar van het grote afhalen. Ga eerst terug tot het hele tiental, en haal dan de rest eraf.  [Claude, taalfix]
  - `andere fout` (andere fout) → Heeft het tweede getal tientallen? Haal die eerst eraf. Haal dan de eenheden eraf: eerst terug tot het hele tiental, daarna de rest.  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — zonder tiental-overschrijding

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over? — zonder tiental-overschrijding” (koppeling: claudeId)
- Items: **12** · Claude-doelen: D4-4 (12) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 kinderboerderij/poesjes → kinderboerderij/eieren (1), #25 stadion/stickers → klas/stickers (1), #25 vallei/eieren → kinderboerderij/eieren (1)
- Denkfouten (Claude): tiental-ernaast (12), een-ernaast (12), verkeerde-bewerking (12)
- Verschillende Claude-fout-hints: 14 (meest: “Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-063` (Claude D4-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het museum liggen 26 schelpen. Er gaan er 11 weg. Hoeveel blijven er over?
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** 25 → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens. · 16 → Ga eerst naar 20, en haal dan 5 eraf. · 37 → Er gaat weg: het getal wordt kleiner.
    - **Uitleg (Claude):** Eerst naar het tiental: 26 − 6 = 20. Dan de rest eraf: 20 − 5 = 15.
  - `G4-GET-M05-claude-bank-064` (Claude D4-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het bos liggen 67 veren. Er gaan er 14 weg. Hoeveel blijven er over?
    - **Antwoord:** 53  (controle: ok)
    - **Fout-hints (Claude):** 63 → Je gaat over het tiental heen, dus er gaat een tiental af. Tel de tientallen nog eens. · 54 → Ga eerst naar 60, en haal dan 7 eraf. · 81 → Er gaat weg: het getal wordt kleiner.
    - **Uitleg (Claude):** Eerst naar het tiental: 67 − 7 = 60. Dan de rest eraf: 60 − 7 = 53.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Splits het tweede getal in tientallen en eenheden.
- **Hint 2 (te schrijven):** Haal eerst de tientallen eraf. Haal daarna de eenheden eraf.
- **Ouderzin:** Je kind haalt een getal boven de tien af van een getal tot 100, zonder terug over een tiental te gaan, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `tientallen vergeten` (fout = antwoord + 10) → Dat is één tiental te veel. Haal ook de tientallen van het tweede getal eraf.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Haal eerst de tientallen eraf, en dan de eenheden.  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus het getal wordt kleiner.  [Claude, taalfix]
  - `een tiental te veel eraf` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel de tientallen nog eens.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Haal eerst de tientallen eraf, en dan de eenheden.  [nieuw]
  - `andere fout` (andere fout) → Haal eerst de tientallen eraf. Haal daarna de eenheden eraf.  [nieuw]
- Status: hints klaar

## Somtype 6: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — zonder tiental-overschrijding

- Sleutel: nrOrigineel **6** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — zonder tiental-overschrijding” (koppeling: claudeId)
- Items: **7** · Claude-doelen: D4-3 (7) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 nest/eieren → kinderboerderij/eieren (1), #25 schuur/vissen → dierentuin/vissen (1), #27 negatieve sleutel → positief (2)
- Denkfouten (Claude): tiental-ernaast (7), een-ernaast (7), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 9 (meest: “Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-120` (Claude D4-3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de kinderboerderij liggen 62 eieren. Er komen er 17 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 79  (controle: ok)
    - **Fout-hints (Claude):** 69 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 78 → Ga eerst naar 70, en tel dan 9 erbij. · 45 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 62 + 8 = 70. Dan de rest erbij: 70 + 9 = 79.
  - `G4-GET-M05-claude-bank-121` (Claude D4-3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het bos liggen 65 noten. Er komen er 13 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 78  (controle: ok)
    - **Fout-hints (Claude):** 68 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 77 → Ga eerst naar 70, en tel dan 8 erbij. · 52 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 65 + 5 = 70. Dan de rest erbij: 70 + 8 = 78.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Splits het tweede getal in tientallen en eenheden.
- **Hint 2 (te schrijven):** Tel eerst de tientallen erbij. Tel daarna de eenheden erbij.
- **Ouderzin:** Je kind telt een getal boven de tien bij een getal tot 100, zonder over een tiental te gaan, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets erbij` (fout = antwoord − getal2) → Dat is het getal waarmee je begint. Er komen dingen bij, dus het worden er meer.  [nieuw]
  - `tientallen vergeten` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel ook de tientallen van het tweede getal erbij.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel eerst de tientallen erbij, en dan de eenheden.  [nieuw]
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het getal wordt groter.  [Claude, taalfix]
  - `een tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel eerst de tientallen erbij, en dan de eenheden.  [nieuw]
  - `andere fout` (andere fout) → Tel eerst de tientallen erbij. Tel daarna de eenheden erbij.  [nieuw]
- Status: hints klaar

## Somtype 7: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — hele tientallen

- Sleutel: nrOrigineel **7** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen? — hele tientallen” (koppeling: claudeId)
- Items: **3** · Claude-doelen: D4-3 (3) · regel: G14-erbij-eraf
- Getallenruimte: 0–100 · type: kale
- Merge-fixlijst: #25 vallei/tanden → museum/botten (1)
- Denkfouten (Claude): tiental-ernaast (3), een-ernaast (3), verkeerde-bewerking (3)
- Verschillende Claude-fout-hints: 5 (meest: “Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G4-GET-M05-claude-bank-098` (Claude D4-3, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het museum liggen 51 botten. Er komen er 10 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 61  (controle: ok)
    - **Fout-hints (Claude):** 51 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 60 → Ga eerst naar 60, en tel dan 1 erbij. · 41 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 51 + 9 = 60. Dan de rest erbij: 60 + 1 = 61.
  - `G4-GET-M05-claude-bank-099` (Claude D4-3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het stadion liggen 51 ballen. Er komen er 20 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 71  (controle: ok)
    - **Fout-hints (Claude):** 61 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 70 → Ga eerst naar 60, en tel dan 11 erbij. · 31 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 51 + 9 = 60. Dan de rest erbij: 60 + 11 = 71.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Hoeveel tientallen komen erbij?
- **Hint 2 (te schrijven):** Spring vanaf het eerste getal vooruit in sprongen van tien: één sprong voor elk tiental dat erbij komt. Het cijfer achteraan blijft hetzelfde.
- **Ouderzin:** Je kind telt hele tientallen bij een getal tot 100, in een verhaaltje.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `niets erbij` (fout = antwoord − getal2) → Dat is het getal waarmee je begint. Er komen dingen bij, dus het worden er meer.  [nieuw]
  - `een tiental te veel` (fout = antwoord + 10) → Tel de tientallen nog eens: één tiental te veel.  [Claude, ok]
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het getal wordt groter.  [Claude, taalfix]
  - `alleen het cijfer erbij` (alleen het cijfer van de tientallen erbij (tekst per item)) → Je telt … erbij, maar het zijn … tientallen. Dat is ….  [Claude, ok]
  - `een tiental te weinig` (fout = antwoord − 10) → Dat is te weinig. Er moet nog een tiental bij.  [nieuw]
  - `bijna` (fout ligt 1 of 2 naast het antwoord) → Bijna! Bij hele tientallen blijft het cijfer achteraan hetzelfde.  [nieuw]
  - `andere fout` (andere fout) → Kijk hoeveel tientallen erbij komen. Spring zo vaak een tiental verder. Het cijfer achteraan blijft hetzelfde.  [nieuw]
- Status: hints klaar
