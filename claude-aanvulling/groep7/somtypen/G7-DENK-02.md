# G7-DENK-02 — Een situatie in een som zetten

Onze omschrijving: Modelleren · in onze bank: 8 items

Claude-vragen gemapt: **14** in **14** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een moestuin is # meter lang en # meter breed. Je tekent hem als rechthoek. Hoe groot is de oppervlakte?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een moestuin is # meter lang en # meter breed. Je tekent hem als rechthoek. Hoe groot is de oppervlakte?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt nu de lengte van de rand uitgerekend. De oppervlakte gaat over het vlak binnen de rand.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-001` (Claude W4, ai, niveau 3 → toepassen)
    - **Opgave:** Een moestuin is 12 meter lang en 5 meter breed. Je tekent hem als rechthoek. Hoe groot is de oppervlakte?
    - **Opties:** A) 17 vierkante meter · B) 60 vierkante meter · C) 34 vierkante meter
    - **Antwoord:** 60 vierkante meter  (controle: n.v.t.)
    - **Fout-hints (Claude):** 34 vierkante meter → Je hebt nu de lengte van de rand uitgerekend. De oppervlakte gaat over het vlak binnen de rand. · 17 vierkante meter → Bij oppervlakte tel je de zijden niet op. Denk aan rijen hokjes van 1 bij 1 meter.
    - **Uitleg (Claude):** De oppervlakte vind je met lengte × breedte. 12 × 5 is 60. Dat zijn 60 vierkante meter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Een sportveld is # meter lang en # meter breed. Je tekent het als rechthoek. Welk getal hoort bij de [ding]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een sportveld is # meter lang en # meter breed. Je tekent het als rechthoek. Welk getal hoort bij de [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): omtrek-oppervlakte-verwisseld (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “De omtrek is de lijn helemaal rondom je tekening, niet het vlak erbinnen.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-002` (Claude W4, ai, niveau 3 → toepassen)
    - **Opgave:** Een sportveld is 20 meter lang en 10 meter breed. Je tekent het als rechthoek. Welk getal hoort bij de omtrek?
    - **Opties:** A) 30 meter · B) 60 meter · C) 200 meter
    - **Antwoord:** 60 meter  (controle: n.v.t.)
    - **Fout-hints (Claude):** 200 meter → De omtrek is de lijn helemaal rondom je tekening, niet het vlak erbinnen. · 30 meter → Een rechthoek heeft vier zijden. Ben je er alle vier langsgelopen?
    - **Uitleg (Claude):** Je loopt rond de rechthoek: 20 + 10 + 20 + 10. Dat is samen 60 meter. De omtrek is dus 60 meter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Er zijn # [ding] op het schoolplein. Een derde speelt bij de [ding]. Welke tekening past hier het beste bij?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Er zijn # [ding] op het schoolplein. Een derde speelt bij de [ding]. Welke tekening past hier het beste bij?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): deel-van-geheel-verkeerd (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een derde betekent dat maar één van de gelijke groepjes telt.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-003` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Er zijn 18 kinderen op het schoolplein. Een derde speelt bij de zandbak. Welke tekening past hier het beste bij?
    - **Opties:** A) 3 groepjes van 6, één groepje gekleurd · B) 3 groepjes van 6, alle groepjes gekleurd · C) 2 groepjes van 9, één groepje gekleurd
    - **Antwoord:** 3 groepjes van 6, één groepje gekleurd  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3 groepjes van 6, alle groepjes gekleurd → Een derde betekent dat maar één van de gelijke groepjes telt. · 2 groepjes van 9, één groepje gekleurd → Bij een derde teken je drie even grote groepjes, niet twee.
    - **Uitleg (Claude):** Bij een derde verdeel je 18 kinderen in 3 gelijke groepjes. Elk groepje heeft 6 kinderen. Eén groepje speelt bij de zandbak.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: In [plek] zitten # [ding]. De helft gaat met de fiets. Welke tekening past het beste bij deze situatie?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In [plek] zitten # [ding]. De helft gaat met de fiets. Welke tekening past het beste bij deze situatie?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): deel-van-geheel-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij de helft knip je de strook één keer doormidden.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-004` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** In de klas zitten 24 kinderen. De helft gaat met de fiets. Welke tekening past het beste bij deze situatie?
    - **Opties:** A) Een strook van 24 die je in 4 gelijke stukken deelt · B) Twee stroken van 24 naast elkaar · C) Een strook van 24 die je in 2 gelijke stukken deelt
    - **Antwoord:** Een strook van 24 die je in 2 gelijke stukken deelt  (controle: n.v.t.)
    - **Fout-hints (Claude):** Een strook van 24 die je in 4 gelijke stukken deelt → Bij de helft knip je de strook één keer doormidden. · Twee stroken van 24 naast elkaar → De klas wordt niet groter, hij wordt alleen verdeeld.
    - **Uitleg (Claude):** De hele klas is één strook van 24. De helft betekent: in 2 gelijke stukken. Elk stuk is dan 12 kinderen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: In een staafdiagram staat hoeveel boeken een klas leest. De staaf van maandag staat precies tussen # en #. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In een staafdiagram staat hoeveel boeken een klas leest. De staaf van maandag staat precies tussen # en #. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De staaf stopt niet bij het streepje van 10, maar een stuk hoger.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-005` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** In een staafdiagram staat hoeveel boeken een klas leest. De staaf van maandag staat precies tussen 10 en 20. Hoeveel boeken zijn dat?
    - **Opties:** A) 10 boeken · B) 30 boeken · C) 15 boeken
    - **Antwoord:** 15 boeken  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 boeken → De staaf stopt niet bij het streepje van 10, maar een stuk hoger. · 30 boeken → Je hoeft de twee getallen niet op te tellen. Zoek het getal dat er precies tussenin ligt.
    - **Uitleg (Claude):** Tussen 10 en 20 ligt precies 15. De staaf stopt in het midden van die twee streepjes. Het zijn dus 15 boeken.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: In een staafdiagram staat hoeveel flesjes water een klas drinkt. De staaf van vrijdag staat precies tussen # en #. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “In een staafdiagram staat hoeveel flesjes water een klas drinkt. De staaf van vrijdag staat precies tussen # en #. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “De staaf stopt niet bij een streepje, maar er precies tussenin. Zoek het getal in het midden.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-006` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** In een staafdiagram staat hoeveel flesjes water een klas drinkt. De staaf van vrijdag staat precies tussen 40 en 50. Hoeveel flesjes zijn dat?
    - **Opties:** A) 40 flesjes · B) 90 flesjes · C) 45 flesjes
    - **Antwoord:** 45 flesjes  (controle: n.v.t.)
    - **Fout-hints (Claude):** 40 flesjes → De staaf stopt niet bij een streepje, maar er precies tussenin. Zoek het getal in het midden. · 90 flesjes → Je hoeft de twee getallen niet op te tellen. Zoek het getal dat er precies tussenin ligt.
    - **Uitleg (Claude):** De staaf staat precies in het midden van 40 en 50. Het getal in het midden is 45. De klas drinkt dus 45 flesjes.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Je hebt # [ding] en verdeelt ze eerlijk over # [ding]. In je schema geef je [wie] evenveel. Hoeveel [ding] krijgt [wie] en hoeveel blijven er over?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Je hebt # [ding] en verdeelt ze eerlijk over # [ding]. In je schema geef je [wie] evenveel. Hoeveel [ding] krijgt [wie] en hoeveel blijven er over?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): rest-vergeten (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel eens na hoeveel stickers je hebt uitgedeeld. Kijk of je er dan precies 30 kwijt bent.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-007` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 30 stickers en verdeelt ze eerlijk over 4 kinderen. In je schema geef je elk kind evenveel. Hoeveel stickers krijgt elk kind en hoeveel blijven er over?
    - **Opties:** A) 7 stickers, niets over · B) 8 stickers, 2 over · C) 7 stickers, 2 over
    - **Antwoord:** 7 stickers, 2 over  (controle: ok)
    - **Fout-hints (Claude):** 7 stickers, niets over → Tel eens na hoeveel stickers je hebt uitgedeeld. Kijk of je er dan precies 30 kwijt bent. · 8 stickers, 2 over → Reken na. 4 keer jouw aantal mag niet meer dan 30 zijn.
    - **Uitleg (Claude):** Je tekent 4 vakjes en deelt steeds rond. Elk kind krijgt 7 stickers, want 4 x 7 is 28. Er blijven dan 2 stickers over.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Je koopt # [ding] knikkers. In elk(e) [bak] zitten # [ding]. Welke som hoort bij de tekening van # rijen met # [ding]?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Je koopt # [ding] knikkers. In elk(e) [bak] zitten # [ding]. Welke som hoort bij de tekening van # rijen met # [ding]?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Er zijn meerdere rijen die allemaal even lang zijn. Wat doe je dan met de getallen?”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-008` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** Je koopt 4 zakjes knikkers. In elk zakje zitten 6 knikkers. Welke som hoort bij de tekening van 4 rijen met 6 knikkers?
    - **Opties:** A) 6 − 4 · B) 4 × 6 · C) 4 + 6
    - **Antwoord:** 4 × 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 + 6 → Er zijn meerdere rijen die allemaal even lang zijn. Wat doe je dan met de getallen? · 6 − 4 → Er gaat niets weg. Er komen juist steeds 6 knikkers bij.
    - **Uitleg (Claude):** Je tekent 4 rijen en in elke rij 6 knikkers. Zo'n rooster hoort bij een keersom. Dus 4 x 6 is 24 knikkers.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Je tekent # [ding] en in elke doos # [ding]. Welke som hoort bij deze tekening?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Je tekent # [ding] en in elke doos # [ding]. Welke som hoort bij deze tekening?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “In elke doos zitten evenveel eieren. Dan tel je niet één keer op, maar steeds hetzelfde aantal erbij.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-009` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** Je tekent 5 dozen en in elke doos 8 eieren. Welke som hoort bij deze tekening?
    - **Opties:** A) 5 + 8 = 13 · B) 8 − 5 = 3 · C) 5 × 8 = 40
    - **Antwoord:** 5 × 8 = 40  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 + 8 = 13 → In elke doos zitten evenveel eieren. Dan tel je niet één keer op, maar steeds hetzelfde aantal erbij. · 8 − 5 = 3 → Je haalt niets weg. Je hebt juist meerdere dozen met eieren samen.
    - **Uitleg (Claude):** Er zijn 5 dozen met elk 8 eieren. Dat is 8 + 8 + 8 + 8 + 8, en dat is hetzelfde als 5 × 8. Samen zijn dat 40 eieren.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 10: Je tekent een schema bij deze opgave: Sanne heeft # [ding] en Tim heeft er # keer zoveel. Welke tekening klopt?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Je tekent een schema bij deze opgave: Sanne heeft # [ding] en Tim heeft er # keer zoveel. Welke tekening klopt?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Bij 3 keer zoveel leg je hetzelfde balkje meerdere keren achter elkaar.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-010` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Je tekent een schema bij deze opgave: Sanne heeft 8 kaarten en Tim heeft er 3 keer zoveel. Welke tekening klopt?
    - **Opties:** A) Een balkje van 8 en een balkje van 3 keer 8 · B) Een balkje van 8 en een balkje van 8 plus 3 · C) Twee balkjes van allebei 8
    - **Antwoord:** Een balkje van 8 en een balkje van 3 keer 8  (controle: n.v.t.)
    - **Fout-hints (Claude):** Een balkje van 8 en een balkje van 8 plus 3 → Bij 3 keer zoveel leg je hetzelfde balkje meerdere keren achter elkaar. · Twee balkjes van allebei 8 → Tim heeft niet evenveel als Sanne. Hij heeft er meer.
    - **Uitleg (Claude):** Sanne is één balkje van 8. Bij Tim leg je dat balkje 3 keer neer. Tim heeft dus 24 kaarten.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 11: Je verdeelt # [ding] eerlijk over # [ding]. In je schema krijgt [wie] evenveel. Hoeveel krijgt [wie] en hoeveel blijven er over?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Je verdeelt # [ding] eerlijk over # [ding]. In je schema krijgt [wie] evenveel. Hoeveel krijgt [wie] en hoeveel blijven er over?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): rest-vergeten (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel in je schema na hoeveel potloden je hebt verdeeld. Zijn dat er echt 26?”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-011` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Je verdeelt 26 potloden eerlijk over 5 kinderen. In je schema krijgt elk kind evenveel. Hoeveel krijgt elk kind en hoeveel blijven er over?
    - **Opties:** A) Elk 5 potloden, niets over · B) Elk 6 potloden, 4 over · C) Elk 5 potloden, 1 over
    - **Antwoord:** Elk 5 potloden, 1 over  (controle: ok)
    - **Fout-hints (Claude):** Elk 5 potloden, niets over → Tel in je schema na hoeveel potloden je hebt verdeeld. Zijn dat er echt 26? · Elk 6 potloden, 4 over → Kijk of je wel genoeg potloden hebt om iedereen er 6 te geven.
    - **Uitleg (Claude):** 5 kinderen × 5 potloden is 25 potloden. Je had er 26, dus blijft er 1 over. Die kun je niet eerlijk verdelen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 12: Langs een pad staan # [ding] op een rij. Tussen twee palen zit steeds # meter. Hoe lang is de rij van de eerste tot de laatste paal?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Langs een pad staan # [ding] op een rij. Tussen twee palen zit steeds # meter. Hoe lang is de rij van de eerste tot de laatste paal?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): een-ernaast (2)
- Verschillende Claude-fout-hints: 2 (meest: “Teken de palen als streepjes en tel de tussenruimtes. Dat zijn er minder dan het aantal palen.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-012` (Claude W4, ai, niveau 3 → toepassen)
    - **Opgave:** Langs een pad staan 7 lantaarnpalen op een rij. Tussen twee palen zit steeds 5 meter. Hoe lang is de rij van de eerste tot de laatste paal?
    - **Opties:** A) 30 meter · B) 35 meter · C) 25 meter
    - **Antwoord:** 30 meter  (controle: n.v.t.)
    - **Fout-hints (Claude):** 35 meter → Teken de palen als streepjes en tel de tussenruimtes. Dat zijn er minder dan het aantal palen. · 25 meter → Tel de tussenruimtes in je tekening nog eens na.
    - **Uitleg (Claude):** Bij 7 palen op een rij zitten 6 tussenruimtes. Elke tussenruimte is 5 meter. 6 × 5 is 30 meter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 13: Lotte heeft # [ding]. Bram heeft er # keer zoveel. Welke tekening klopt bij deze situatie?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Lotte heeft # [ding]. Bram heeft er # keer zoveel. Welke tekening klopt bij deze situatie?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W4 (1) · regel: G7-W02-modelleren
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vier keer zoveel is niet vier erbij. Teken de strook van Lotte vier keer achter elkaar.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-013` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Lotte heeft 6 schelpen. Bram heeft er 4 keer zoveel. Welke tekening klopt bij deze situatie?
    - **Opties:** A) Een strook van 6 en een strook van 24 · B) Een strook van 6 en een strook van 10 · C) Een strook van 6 en een strook van 4
    - **Antwoord:** Een strook van 6 en een strook van 24  (controle: n.v.t.)
    - **Fout-hints (Claude):** Een strook van 6 en een strook van 10 → Vier keer zoveel is niet vier erbij. Teken de strook van Lotte vier keer achter elkaar. · Een strook van 6 en een strook van 4 → Het getal 4 zegt hoe vaak je de strook van Lotte neemt.
    - **Uitleg (Claude):** Bram heeft 4 keer de strook van Lotte. 4 × 6 is 24. Dus zijn strook is 24 lang.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 14: Op een schoolplein staan # [ding] met # [ding] en # [ding] met # [ding]. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Op een schoolplein staan # [ding] met # [ding] en # [ding] met # [ding]. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-G7-SOM
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), deel-vergeten-bij-splitsen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt alleen de fietsen geteld. Elke fiets heeft meerdere wielen.”)
- Voorbeelden:
  - `G7-DENK-02-claude-bank-naar-001` (Claude G9, ai, niveau 1 → basis)
    - **Opgave:** Op een schoolplein staan 4 fietsen met 2 wielen en 3 fietsen met 3 wielen. Hoeveel wielen zijn dat samen?
    - **Opties:** A) 17 wielen · B) 7 wielen · C) 14 wielen
    - **Antwoord:** 17 wielen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 wielen → Je hebt alleen de fietsen geteld. Elke fiets heeft meerdere wielen. · 14 wielen → Reken beide soorten fietsen apart uit en tel de uitkomsten daarna op.
    - **Uitleg (Claude):** 4 fietsen met 2 wielen zijn 8 wielen. 3 fietsen met 3 wielen zijn 9 wielen. Samen is dat 8 + 9 = 17 wielen.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
