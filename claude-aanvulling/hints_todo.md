# Hints nog te schrijven (somtypes zonder hints)

Gemaakt 2026-10-01 22:58 (Amsterdam) met `tools/maak_hints_todo.py`. De telling is dezelfde als `gN/check_hints.py`: een somtype zonder 'Status: hints klaar' telt als open.
Elke entry in `hints/batch*.json` koppelt op **doel + nrOrigineel** (de sleutel hieronder), niet op het volgnummer. 'Waarvan G8-aanvulling' telt de items die uit de G8-pool kwamen (`aanvulling_uit_g8.json`, inclusief de 46 terug-G7).

**Let op:** de opdracht van 22:34 noemde G5 20 en G6 5 open. Om 22:55 heeft Oefeningen die gesloten (G5 batch 7: GET-E05 13, GET-E07 5 met de nieuwe ×198, GET-E09 2; G6 batch 6: MKU-E01 4, MKU-E03 1). Na de rebuild van 22:5x telt check_hints daar 0 open. Wat nog open staat: G4 4 (GET-E05, de G8-aanvulling), G7 154 en G8 223.

| groep | hints klaar | open somtypes | items in open somtypes |
|---|---|---|---|
| G4 | 93 | 4 | 36 |
| G5 | 140 | 0 | 0 |
| G6 | 95 | 0 | 0 |
| G7 | 0 | 154 | 7661 |
| G8 | 0 | 223 | 1458 |

## G4 — 4 somtypes open · 36 items

### G4-GET-E05 — 4 somtypes · 36 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 2 | Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit. | 12 | 12 | `G4-GET-E05-claude-bank-naar-001`: Hoeveel is 16 + 31 ongeveer? Rond beide getallen af op tientallen en reken dan uit. → **50** |
| 2 | 3 | Hoeveel is # − # [ding]? Rond beide getallen af op tientallen en reken dan uit. | 8 | 8 | `G4-GET-E05-claude-bank-naar-013`: Hoeveel is 44 − 20 ongeveer? Rond beide getallen af op tientallen en reken dan uit. → **20** |
| 3 | 4 | Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? | 8 | 8 | `G4-GET-E05-claude-bank-naar-021`: Kijk zonder uit te rekenen. Welk antwoord bij 39 + 35 kan kloppen? → **74** |
| 4 | 5 | Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen? | 8 | 8 | `G4-GET-E05-claude-bank-naar-029`: Kijk zonder uit te rekenen. Welk antwoord bij 88 − 33 kan kloppen? → **55** |

## G5 — 0 somtypes open · 0 items

## G6 — 0 somtypes open · 0 items

## G7 — 154 somtypes open · 7661 items

### G7-DENK-02 — 14 somtypes · 14 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een moestuin is # meter lang en # meter breed. Je tekent hem als rechthoek. Hoe groot is d | 1 |  | `G7-DENK-02-claude-bank-001`: Een moestuin is 12 meter lang en 5 meter breed. Je tekent hem als rechthoek. Hoe groot is de oppervlakte? → **60 vierkante meter** |
| 2 | 2 | Een sportveld is # meter lang en # meter breed. Je tekent het als rechthoek. Welk getal ho | 1 |  | `G7-DENK-02-claude-bank-002`: Een sportveld is 20 meter lang en 10 meter breed. Je tekent het als rechthoek. Welk getal hoort bij de omtrek? → **60 meter** |
| 3 | 3 | Er zijn # [ding] op het schoolplein. Een derde speelt bij de [ding]. Welke tekening past h | 1 |  | `G7-DENK-02-claude-bank-003`: Er zijn 18 kinderen op het schoolplein. Een derde speelt bij de zandbak. Welke tekening past hier het beste bi… → **3 groepjes van 6, één groepje gekleurd** |
| 4 | 4 | In [plek] zitten # [ding]. De helft gaat met de fiets. Welke tekening past het beste bij d | 1 |  | `G7-DENK-02-claude-bank-004`: In de klas zitten 24 kinderen. De helft gaat met de fiets. Welke tekening past het beste bij deze situatie? → **Een strook van 24 die je in 2 gelijke stukken deelt** |
| 5 | 5 | In een staafdiagram staat hoeveel boeken een klas leest. De staaf van maandag staat precie | 1 |  | `G7-DENK-02-claude-bank-005`: In een staafdiagram staat hoeveel boeken een klas leest. De staaf van maandag staat precies tussen 10 en 20. H… → **15 boeken** |
| 6 | 6 | In een staafdiagram staat hoeveel flesjes water een klas drinkt. De staaf van vrijdag staa | 1 |  | `G7-DENK-02-claude-bank-006`: In een staafdiagram staat hoeveel flesjes water een klas drinkt. De staaf van vrijdag staat precies tussen 40 … → **45 flesjes** |
| 7 | 7 | Je hebt # [ding] en verdeelt ze eerlijk over # [ding]. In je schema geef je [wie] evenveel | 1 |  | `G7-DENK-02-claude-bank-007`: Je hebt 30 stickers en verdeelt ze eerlijk over 4 kinderen. In je schema geef je elk kind evenveel. Hoeveel st… → **7 stickers, 2 over** |
| 8 | 8 | Je koopt # [ding] knikkers. In elk(e) [bak] zitten # [ding]. Welke som hoort bij de tekeni | 1 |  | `G7-DENK-02-claude-bank-008`: Je koopt 4 zakjes knikkers. In elk zakje zitten 6 knikkers. Welke som hoort bij de tekening van 4 rijen met 6 … → **4 × 6** |
| 9 | 9 | Je tekent # [ding] en in elke doos # [ding]. Welke som hoort bij deze tekening? | 1 |  | `G7-DENK-02-claude-bank-009`: Je tekent 5 dozen en in elke doos 8 eieren. Welke som hoort bij deze tekening? → **5 × 8 = 40** |
| 10 | 10 | Je tekent een schema bij deze opgave: Sanne heeft # [ding] en Tim heeft er # keer zoveel.  | 1 |  | `G7-DENK-02-claude-bank-010`: Je tekent een schema bij deze opgave: Sanne heeft 8 kaarten en Tim heeft er 3 keer zoveel. Welke tekening klop… → **Een balkje van 8 en een balkje van 3 keer 8** |
| 11 | 11 | Je verdeelt # [ding] eerlijk over # [ding]. In je schema krijgt [wie] evenveel. Hoeveel kr | 1 |  | `G7-DENK-02-claude-bank-011`: Je verdeelt 26 potloden eerlijk over 5 kinderen. In je schema krijgt elk kind evenveel. Hoeveel krijgt elk kin… → **Elk 5 potloden, 1 over** |
| 12 | 12 | Langs een pad staan # [ding] op een rij. Tussen twee palen zit steeds # meter. Hoe lang is | 1 |  | `G7-DENK-02-claude-bank-012`: Langs een pad staan 7 lantaarnpalen op een rij. Tussen twee palen zit steeds 5 meter. Hoe lang is de rij van d… → **30 meter** |
| 13 | 13 | Lotte heeft # [ding]. Bram heeft er # keer zoveel. Welke tekening klopt bij deze situatie? | 1 |  | `G7-DENK-02-claude-bank-013`: Lotte heeft 6 schelpen. Bram heeft er 4 keer zoveel. Welke tekening klopt bij deze situatie? → **Een strook van 6 en een strook van 24** |
| 14 | 14 | Op een schoolplein staan # [ding] met # [ding] en # [ding] met # [ding]. Hoeveel [ding] zi | 1 | 1 | `G7-DENK-02-claude-bank-naar-001`: Op een schoolplein staan 4 fietsen met 2 wielen en 3 fietsen met 3 wielen. Hoeveel wielen zijn dat samen? → **17 wielen** |

### G7-DENK-03 — 26 somtypes · 26 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Bij gym loop je # [ding] van # minuten en daarna rust je # minuten. Hoelang ben je in tota | 1 |  | `G7-DENK-03-claude-bank-001`: Bij gym loop je 3 rondjes van 4 minuten en daarna rust je 5 minuten. Hoelang ben je in totaal bezig? → **17 minuten** |
| 2 | 2 | Een recept voor # [ding] gebruikt # g meel. Stap #: je kookt voor # [ding]. Stap #: pas de | 1 |  | `G7-DENK-03-claude-bank-002`: Een recept voor 4 personen gebruikt 300 g meel. Stap 1: je kookt voor 8 personen. Stap 2: pas de hoeveelheid m… → **600 g** |
| 3 | 3 | In [plek] staan # [ding] met elk # [ding]. Daarna haal je # [ding] weg. Hoeveel stoelen st | 1 |  | `G7-DENK-03-claude-bank-003`: In de klas staan 6 tafels met elk 4 stoelen. Daarna haal je 3 stoelen weg. Hoeveel stoelen staan er nog? → **21 stoelen** |
| 4 | 25 | In een sportzaal staan # [ding] met elk # [ding]. Noor haalt er # [ding] uit. Hoeveel blij | 1 | 1 | `G7-DENK-03-claude-bank-naar-001`: In een sportzaal staan 7 dozen met elk 24 ballen. Noor haalt er 18 ballen uit. Hoeveel ballen blijven er over? → **150 ballen** |
| 5 | 4 | Je begint bij # en verdubbelt het getal # keer. Welk getal krijg je dan? | 1 |  | `G7-DENK-03-claude-bank-004`: Je begint bij 1 en verdubbelt het getal 4 keer. Welk getal krijg je dan? → **16** |
| 6 | 5 | Je begint bij # op de getallenlijn en zet # [ding] van # [ding]. Bij welk getal kom je uit | 1 |  | `G7-DENK-03-claude-bank-005`: Je begint bij 0 op de getallenlijn en zet 5 stappen van 4 vooruit. Bij welk getal kom je uit? → **20** |
| 7 | 6 | Je geeft een plant # dagen water. Op dag # [ding] je # dl en elke volgende dag # dl meer.  | 1 |  | `G7-DENK-03-claude-bank-006`: Je geeft een plant 4 dagen water. Op dag 1 geef je 2 dl en elke volgende dag 1 dl meer. Hoeveel dl water geef … → **14 dl** |
| 8 | 7 | Je hebt # [ding] sap van elk # liter. Stap #: giet alles in een kan. Stap #: giet er # lit | 1 |  | `G7-DENK-03-claude-bank-007`: Je hebt 3 pakken sap van elk 2 liter. Stap 1: giet alles in een kan. Stap 2: giet er 1 liter uit. Hoeveel lite… → **5 liter** |
| 9 | 8 | Je hebt # [ding] stroken. Je knipt elke strook in # stukken. Hoeveel stukken heb je dan? | 1 |  | `G7-DENK-03-claude-bank-008`: Je hebt 12 papieren stroken. Je knipt elke strook in 2 stukken. Hoeveel stukken heb je dan? → **24 stukken** |
| 10 | 9 | Je hebt # [ding]. Stap #: geef # [ding] weg. Stap #: geef nog eens # [ding] weg. Hoeveel s | 1 |  | `G7-DENK-03-claude-bank-009`: Je hebt 20 stickers. Stap 1: geef 4 stickers weg. Stap 2: geef nog eens 4 stickers weg. Hoeveel stickers heb j… → **12 stickers** |
| 11 | 10 | Je hebt # euro gespaard. Stap #: je krijgt # euro zakgeld. Stap #: je koopt een schrift va | 1 |  | `G7-DENK-03-claude-bank-010`: Je hebt 8 euro gespaard. Stap 1: je krijgt 5 euro zakgeld. Stap 2: je koopt een schrift van 4 euro. Hoeveel eu… → **9 euro** |
| 12 | 11 | Je loopt een route. # m rechtdoor, dan links # m en dan rechts # m. Hoeveel meter heb je i | 1 |  | `G7-DENK-03-claude-bank-011`: Je loopt een route. 200 m rechtdoor, dan links 150 m en dan rechts 250 m. Hoeveel meter heb je in totaal gelop… → **600 m** |
| 13 | 12 | Je rijgt een ketting volgens dit patroon. # [ding] kralen en # [ding] kraal. Je herhaalt h | 1 |  | `G7-DENK-03-claude-bank-012`: Je rijgt een ketting volgens dit patroon. 2 rode kralen en 1 blauwe kraal. Je herhaalt het patroon 5 keer. Hoe… → **15 kralen** |
| 14 | 13 | Je staat op tree # van de trap. Stap #: ga # [ding] omhoog. Stap #: ga # [ding] omlaag. Op | 1 |  | `G7-DENK-03-claude-bank-013`: Je staat op tree 3 van de trap. Stap 1: ga 5 treden omhoog. Stap 2: ga 2 treden omlaag. Op welke tree sta je d… → **Tree 6** |
| 15 | 14 | Je volgt deze stappen: neem #, verdubbel het getal en tel er # bij op. Welke uitkomst krij | 1 |  | `G7-DENK-03-claude-bank-014`: Je volgt deze stappen: neem 6, verdubbel het getal en tel er 3 bij op. Welke uitkomst krijg je? → **15** |
| 16 | 15 | Je vouwt een blad papier # keer dubbel. Na elke vouw wordt het aantal delen # keer zoveel. | 1 |  | `G7-DENK-03-claude-bank-015`: Je vouwt een blad papier 3 keer dubbel. Na elke vouw wordt het aantal delen 2 keer zoveel. In hoeveel delen is… → **8 delen** |
| 17 | 26 | Op een wandeltocht van # km staan om de # meter bordjes, ook bij de start en de finish. Ho | 1 | 1 | `G7-DENK-03-claude-bank-naar-002`: Op een wandeltocht van 12 km staan om de 500 meter bordjes, ook bij de start en de finish. Hoeveel bordjes sta… → **25 bordjes** |
| 18 | 16 | Recept: stap #, pak # [ding]. Stap #: pers voor elk glas # [ding]. Hoeveel sinaasappels pe | 1 |  | `G7-DENK-03-claude-bank-016`: Recept: stap 1, pak 3 glazen. Stap 2: pers voor elk glas 2 sinaasappels. Hoeveel sinaasappels pers je? → **6 sinaasappels** |
| 19 | 17 | Reeks A: neem #, doe keer # en tel er # bij op. Reeks B: neem #, tel er # bij op en doe ke | 1 |  | `G7-DENK-03-claude-bank-017`: Reeks A: neem 5, doe keer 4 en tel er 2 bij op. Reeks B: neem 5, tel er 2 bij op en doe keer 4. Welke reeks ge… → **Reeks B** |
| 20 | 18 | Regel: is het getal even, deel het dan door #. Is het oneven, tel er dan # bij op. Je begi | 1 |  | `G7-DENK-03-claude-bank-018`: Regel: is het getal even, deel het dan door 2. Is het oneven, tel er dan 3 bij op. Je begint bij 10 en doet 3 … → **4** |
| 21 | 19 | Stappen: neem #, deel door #, tel er # bij op en doe keer #. Tim zegt dat de uitkomst # is | 1 |  | `G7-DENK-03-claude-bank-019`: Stappen: neem 48, deel door 6, tel er 5 bij op en doe keer 2. Tim zegt dat de uitkomst 26 is. Klopt dat? → **Ja, 26 klopt** |
| 22 | 20 | Stappen: neem #, doe keer # en haal er # af. Lisa zegt dat de uitkomst # is. Klopt dat? | 1 |  | `G7-DENK-03-claude-bank-020`: Stappen: neem 9, doe keer 3 en haal er 7 af. Lisa zegt dat de uitkomst 20 is. Klopt dat? → **Ja, 20 klopt** |
| 23 | 21 | Stappen: neem #, haal er # af, deel door # en tel er # bij op. Iemand schreef op. #, #, #, | 1 |  | `G7-DENK-03-claude-bank-021`: Stappen: neem 30, haal er 6 af, deel door 4 en tel er 10 bij op. Iemand schreef op. 30, 24, 8, 18. Bij welke s… → **Bij stap 3** |
| 24 | 22 | Verdeel # [ding] eerlijk over # [ding]. De knikkers die overblijven, leg je apart. Hoeveel | 1 |  | `G7-DENK-03-claude-bank-022`: Verdeel 50 knikkers eerlijk over 8 zakjes. De knikkers die overblijven, leg je apart. Hoeveel knikkers liggen … → **2 knikkers** |
| 25 | 23 | Volg deze stappen: neem #, doe keer #, tel er # bij op en deel door #. Wat is de uitkomst? | 1 |  | `G7-DENK-03-claude-bank-023`: Volg deze stappen: neem 7, doe keer 4, tel er 12 bij op en deel door 2. Wat is de uitkomst? → **20** |
| 26 | 24 | Voor # [ding] gebruik je # g boter. Je wilt # [ding] bakken. Iemand zegt dat je dan # g bo | 1 |  | `G7-DENK-03-claude-bank-024`: Voor 6 koekjes gebruik je 120 g boter. Je wilt 18 koekjes bakken. Iemand zegt dat je dan 240 g boter nodig heb… → **Nee, het moet 360 g zijn** |

### G7-DENK-04 — 6 somtypes · 147 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Zoek het verschil van # en #. Welke som maak je? | 80 |  | `G7-DENK-04-claude-bank-068`: Zoek het verschil van 40 en 27. Welke som maak je? → **40 − 27** |
| 2 | 2 | Hoe heet de # in # − # = #? | 30 |  | `G7-DENK-04-claude-bank-031`: Hoe heet de 8 in 130 − 8 = 122? → **de aftrekker** |
| 3 | 3 | Hoe heet de # in # + # = #? | 15 |  | `G7-DENK-04-claude-bank-001`: Hoe heet de 1325 in 1322 + 3 = 1325? → **de som** |
| 4 | 4 | Hoe heet de # in # : # = #? | 9 |  | `G7-DENK-04-claude-bank-016`: Hoe heet de 6 in 150 : 6 = 25? → **de deler** |
| 5 | 5 | Zoek het quotiënt van # en #. Welke som maak je? | 7 |  | `G7-DENK-04-claude-bank-061`: Zoek het quotiënt van 328 en 8. Welke som maak je? → **328 : 8** |
| 6 | 6 | Hoe heet de # in # × # = #? | 6 |  | `G7-DENK-04-claude-bank-025`: Hoe heet de 10.576 in 1322 × 8 = 10.576? → **het product** |

### G7-GET-01 — 7 somtypes · 668 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | # wordt #. Met hoeveel verandert het getal? | 396 |  | `G7-GET-01-claude-bank-001`: 261.954 wordt 261.854. Met hoeveel verandert het getal? → **100** |
| 2 | 2 | Welk getal is # minder dan #? | 103 |  | `G7-GET-01-claude-bank-579`: Welk getal is 10.000 minder dan 307.701? → **297.701** |
| 3 | 3 | Welk getal is # meer dan #? | 101 |  | `G7-GET-01-claude-bank-472`: Welk getal is 10.000 meer dan 197.356? → **207.356** |
| 4 | 4 | Rond # af op tienduizendtallen. | 53 |  | `G7-GET-01-claude-bank-413`: Rond 967.263 af op tienduizendtallen. → **970.000** |
| 5 | 5 | In [plek] zijn # [ding] geteld, in [plek] #. Typ het grootste getal. | 8 |  | `G7-GET-01-claude-bank-401`: In het veld zijn 467.607 stickers geteld, in de kleedkamer 459.193. Typ het grootste getal. → **467.607** |
| 6 | 6 | Op de teller van [plek] staat # [ding]. Hoeveel is de # in dit getal waard? | 4 |  | `G7-GET-01-claude-bank-409`: Op de teller van het museum staat 642.311 tanden. Hoeveel is de 6 in dit getal waard? → **600.000** |
| 7 | 7 | Welk cijfer staat op de plaats van de tienduizendtallen in #? | 3 |  | `G7-GET-01-claude-bank-466`: Welk cijfer staat op de plaats van de tienduizendtallen in 731.829? → **3** |

### G7-GET-02 — 3 somtypes · 444 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Welk getal is het grootst? | 216 |  | `G7-GET-02-claude-bank-013`: Welk getal is het grootst? → **5,9** |
| 2 | 2 | Welk getal is het kleinst? | 216 |  | `G7-GET-02-claude-bank-121`: Welk getal is het kleinst? → **1,1** |
| 3 | 3 | Een [ding] weegt precies # kg. Rond af op één cijfer achter de komma. | 12 |  | `G7-GET-02-claude-bank-001`: Een pakket weegt precies 2,045 kg. Rond af op één cijfer achter de komma. → **2,0** |

### G7-GET-03 — 4 somtypes · 412 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | # + # = | 211 |  | `G7-GET-03-claude-bank-001`: 4,09 + 0,6 = → **4,69** |
| 2 | 2 | # − # = | 193 |  | `G7-GET-03-claude-bank-227`: 6,47 − 2,5 = → **3,97** |
| 3 | 3 | [plek] heeft # [ding], [plek] heeft er #. Hoeveel [ding] heeft [plek]? | 6 |  | `G7-GET-03-claude-bank-425`: de dierentuin heeft 26.428 vissen, het bos heeft er 6823. Hoeveel meer heeft de dierentuin? → **19.605** |
| 4 | 4 | het huis heeft # [ding], de klas heeft er #. Hoeveel [ding] heeft het huis? | 2 |  | `G7-GET-03-claude-bank-431`: het huis heeft 72.261 stickers, de klas heeft er 9387. Hoeveel meer heeft het huis? → **62.874** |

### G7-GET-04 — 11 somtypes · 896 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | # : # = | 416 |  | `G7-GET-04-claude-bank-001`: 15,03 : 9 = → **1,67** |
| 2 | 2 | # × # = | 376 |  | `G7-GET-04-claude-bank-475`: 2,58 × 9 = → **23,22** |
| 3 | 3 | # [ding] worden verdeeld over # [ding]. Hoeveel krijgt [wie]? (Wat overblijft, blijft over | 32 |  | `G7-GET-04-claude-bank-435`: 400 tanden worden verdeeld over 3 dino's. Hoeveel krijgt elke dino? (Wat overblijft, blijft over.) → **133** |
| 4 | 11 | Prijs per stuk: # [ding] kosten samen €#. Hoeveel kost één? | 31 | 31 | `G7-GET-04-claude-bank-terug-001`: 8 kaartjes voor de bus kosten samen €28. Hoeveel kost één kaartje voor de bus? → **€3,50** |
| 5 | 6 | # [ding] hebben #, #, #, #, # [ding]. Hoeveel [ding] hebben ze gemiddeld? | 11 |  | `G7-GET-04-claude-bank-425`: 5 konijnen hebben 6, 13, 3, 15, 18 wortels. Hoeveel wortels hebben ze gemiddeld? → **11** |
| 6 | 4 | # [ding] gaan in [bakken] van #. Hoeveel blijven er over? | 8 |  | `G7-GET-04-claude-bank-417`: 983 kaartjes gaan in dozen van 18. Hoeveel kaartjes blijven er over? → **11** |
| 7 | 5 | # kilo/liter [ding] wordt eerlijk verdeeld over # [wie]. Hoeveel krijgt elk(e) [wie]? | 8 |  | `G7-GET-04-claude-bank-467`: 115 kilo kaartjes wordt eerlijk verdeeld over 8 spelers. Hoeveel kilo krijgt elke speler? → **14,375** |
| 8 | 7 | # [ding] worden eerlijk verdeeld over # [ding]. Hoeveel krijgt [wie]? | 4 |  | `G7-GET-04-claude-bank-431`: 5364 noten worden eerlijk verdeeld over 36 eekhoorns. Hoeveel krijgt elke eekhoorn? → **149** |
| 9 | 8 | Een [ding] weegt # gram. Hoeveel gram wegen # [ding]? | 4 |  | `G7-GET-04-claude-bank-851`: Eén poesje weegt 3,3 gram. Hoeveel gram wegen 100 poesjes? → **330** |
| 10 | 9 | Een [ding] weegt # kg. Hoeveel wegen # [ding]? | 4 |  | `G7-GET-04-claude-bank-855`: Een pakket weegt 6,3 kg. Hoeveel wegen 10 stenen? → **63** |
| 11 | 10 | In [plek] staan # [ding] met elk # [ding]. Hoeveel [ding] zijn dat? | 2 |  | `G7-GET-04-claude-bank-859`: In de klas staan 34 kisten met elk 364 pakken. Hoeveel pakken zijn dat? → **12.376** |

### G7-GET-05 — 7 somtypes · 567 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 6 | Welke breuk is het grootst? Kies uit #/#, #/# of #/#. | 190 |  | `G7-GET-05-claude-bank-302`: Welke breuk is het grootst? Kies uit 11/24, 4/5 of 15/22. → **4/5** |
| 2 | 7 | Welke breuk is het kleinst? Kies uit #/#, #/# of #/#. | 128 |  | `G7-GET-05-claude-bank-482`: Welke breuk is het kleinst? Kies uit 3/20, 4/5 of 2/11. → **3/20** |
| 3 | 1 | Reken uit: #/# + #/# = ? Typ een breuk. — uitkomst boven 1 | 76 |  | `G7-GET-05-claude-bank-096`: Reken uit: 2/12 + 11/12 = ? Typ een breuk. → **13/12** |
| 4 | 2 | Reken uit: #/# + #/# = ? Typ een breuk. | 63 |  | `G7-GET-05-claude-bank-006`: Reken uit: 2/4 + 1/4 = ? Typ een breuk. → **3/4** |
| 5 | 3 | Reken uit: #/# − #/# = ? Typ een breuk. | 60 |  | `G7-GET-05-claude-bank-172`: Reken uit: 3/4 − 2/4 = ? Typ een breuk. → **1/4** |
| 6 | 4 | Schrijf #/# als kommagetal. | 45 |  | `G7-GET-05-claude-bank-256`: Schrijf 3/5 als kommagetal. → **0,6** |
| 7 | 5 | # van de [ding] is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk. | 5 |  | `G7-GET-05-claude-bank-001`: 0,6 van de botten is blauw. Schrijf dat als een zo eenvoudig mogelijke breuk. → **3/5** |

### G7-MEET-01 — 6 somtypes · 305 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | # m = □ km | 71 |  | `G7-MEET-01-claude-bank-041`: 3100 m = □ km → **3,1** |
| 2 | 2 | # mm = □ m | 71 |  | `G7-MEET-01-claude-bank-112`: 1300 mm = □ m → **1,3** |
| 3 | 3 | Vul in. # m = ... cm | 43 |  | `G7-MEET-01-claude-bank-223`: Vul in. 5,5 m = ... cm → **550** |
| 4 | 4 | # cm = □ m | 40 |  | `G7-MEET-01-claude-bank-001`: 210 cm = □ m → **2,1** |
| 5 | 5 | Vul in. # km = ... m | 40 |  | `G7-MEET-01-claude-bank-183`: Vul in. 1,9 km = ... m → **1900** |
| 6 | 6 | Vul in. # m = ... mm | 40 |  | `G7-MEET-01-claude-bank-267`: Vul in. 1,2 m = ... mm → **1200** |

### G7-MEET-02 — 4 somtypes · 51 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | [driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # m en een hoogte van | 32 |  | `G7-MEET-02-claude-bank-001`: Een driehoekig bloemperk in het park heeft een basis van 7 m en een hoogte van 6 m. Wat is de oppervlakte in m… → **21** |
| 2 | 3 | Een L-vormig hok bestaat uit een rechthoek van # bij # meter en een rechthoek van # bij #  | 8 | 8 | `G7-MEET-02-claude-bank-terug-001`: Een L-vormig hok bestaat uit een rechthoek van 6 bij 5 meter en een rechthoek van 2 bij 4 meter. Hoeveel m² is… → **38** |
| 3 | 4 | Een tuin van # bij # meter heeft een vierkante vijver van # bij # meter. Hoeveel m² gras i | 7 | 7 | `G7-MEET-02-claude-bank-terug-009`: Een tuin van 6 bij 6 meter heeft een vierkante vijver van 2 bij 2 meter. Hoeveel m² gras is er? → **32** |
| 4 | 2 | [driehoek-in-rechthoek] Een driehoekig(e) [ding] heeft een basis van # cm en een hoogte va | 4 |  | `G7-MEET-02-claude-bank-033`: Een driehoekige vlag heeft een basis van 12 cm en een hoogte van 5 cm. Wat is de oppervlakte in cm²? → **30** |

### G7-MEET-03 — 10 somtypes · 1702 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een balk heeft een inhoud van # [ding]. De bodem is # bij # cm. Hoe hoog is de balk in cm? | 838 |  | `G7-MEET-03-claude-bank-1000`: Een balk heeft een inhoud van 504 cm³. De bodem is 6 bij 12 cm. Hoe hoog is de balk in cm? → **7** |
| 2 | 2 | Een balk is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ is de inhoud? | 518 |  | `G7-MEET-03-claude-bank-1057`: Een balk is 5 cm lang, 3 cm breed en 10 cm hoog. Hoeveel cm³ is de inhoud? → **150** |
| 3 | 3 | # g = □ kg | 71 |  | `G7-MEET-03-claude-bank-041`: 360.000 g = □ kg → **360** |
| 4 | 4 | # ml = □ L | 71 |  | `G7-MEET-03-claude-bank-112`: 290.000 ml = □ L → **290** |
| 5 | 5 | Vul in. # L = ... ml | 44 |  | `G7-MEET-03-claude-bank-1616`: Vul in. 3,8 L = ... ml → **3800** |
| 6 | 6 | Vul in. # kg = ... g | 44 |  | `G7-MEET-03-claude-bank-1660`: Vul in. 1,7 kg = ... g → **1700** |
| 7 | 7 | # cl = □ L | 40 |  | `G7-MEET-03-claude-bank-001`: 30 cl = □ L → **0,3** |
| 8 | 8 | Vul in. # L = ... cl | 40 |  | `G7-MEET-03-claude-bank-1576`: Vul in. 3,7 L = ... cl → **370** |
| 9 | 9 | Een bak is # m lang, # m breed en # m hoog. Hoeveel m³ gaat erin? | 32 |  | `G7-MEET-03-claude-bank-187`: Een bak in de kantine is 3 m lang, 4 m breed en 2 m hoog. Hoeveel m³ gaat erin? → **24** |
| 10 | 10 | Een bak is # cm lang, # cm breed en # cm hoog. Hoeveel cm³ gaat erin? | 4 |  | `G7-MEET-03-claude-bank-183`: Een doos voor sterren is 11 cm lang, 4 cm breed en 4 cm hoog. Hoeveel cm³ past erin? → **176** |

### G7-MEET-04 — 7 somtypes · 556 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 7 | Hoeveel dagen duurt het van # [ding] tot # [ding]? | 220 |  | `G7-MEET-04-claude-bank-338`: Hoeveel dagen duurt het van 8 maart tot 14 mei? → **67** |
| 2 | 1 | Het is −# graden. Het wordt # graden warmer. Hoe warm is het dan? | 148 |  | `G7-MEET-04-claude-bank-045`: Het is −2 graden. Het wordt 10 graden warmer. Hoe warm is het dan? → **8** |
| 3 | 2 | Het is −# graden. Later is het # graden. Hoeveel graden is het warmer geworden? | 144 |  | `G7-MEET-04-claude-bank-194`: Het is −4 graden. Later is het 7 graden. Hoeveel graden is het warmer geworden? → **11** |
| 4 | 3 | Het is # graden in [plek]. 's Nachts daalt de temperatuur # graden. Hoeveel graden is het  | 24 |  | `G7-MEET-04-claude-bank-021`: Het is 3 graden in de kantine. 's Nachts daalt de temperatuur 11 graden. Hoeveel graden is het dan? (Typ een m… → **−8** |
| 5 | 4 | 's Nachts is het in [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het war | 9 |  | `G7-MEET-04-claude-bank-001`: 's Nachts was het bij de schuur −12 graden. Overdag werd het 8 graden. Hoeveel graden is het warmer geworden? → **20** |
| 6 | 5 | 's Ochtends is het in [plek] −# graden. 's Middags is het # graden. Hoeveel graden is het  | 8 |  | `G7-MEET-04-claude-bank-013`: 's Ochtends is het in de vallei −6 graden. 's Middags is het 3 graden. Hoeveel graden is het warmer geworden? → **9** |
| 7 | 6 | 's Nachts was het bij [plek] −# graden. Overdag werd het # graden. Hoeveel graden is het w | 3 |  | `G7-MEET-04-claude-bank-010`: 's Nachts was het bij de school −6 graden. Overdag werd het 14 graden. Hoeveel graden is het warmer geworden? → **20** |

### G7-VBN-04 — 4 somtypes · 36 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | [balk kleuren] Tabel: [rij]. Maak de staaf van [naam]: elk stukje van de balk is #. | 12 |  | `G7-VBN-04-claude-bank-001`: Tabel: ma 20, di 45, wo 5, do 5, vr 50. Maak de staaf van wo: elk stukje van de balk is 5. → **1** |
| 2 | 2 | [tabel] Je maakt een staafdiagram van deze tabel. Welke staaf wordt het hoogst? | 9 |  | `G7-VBN-04-claude-bank-028`: Je maakt een staafdiagram van deze tabel over het aantal gelezen boeken per groep. Welke staaf wordt het hoogs… → **groep 5** |
| 3 | 3 | [tabel] Je maakt een staafdiagram van deze tabel. De as loopt in stappen van #. Tot welk t | 8 |  | `G7-VBN-04-claude-bank-013`: Je tekent een staafdiagram van deze tabel over de regen per week in millimeters. De as loopt in stappen van 10… → **20** |
| 4 | 4 | [tabel] Je maakt een staafdiagram van deze tabel. Elk streepje op de as staat voor #. Hoev | 7 |  | `G7-VBN-04-claude-bank-021`: Je maakt een staafdiagram van deze tabel over het aantal gelezen boeken per groep. Elk streepje op de as staat… → **2** |

### G7-VERH-01 — 7 somtypes · 28 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | [balk kleuren] Een pot heeft # [ding]. Kleur #% ervan. Elk stukje is # [ding]. | 12 |  | `G7-VERH-01-claude-bank-006`: Een pot heeft 400 knikkers. Kleur 20% ervan. Elk stukje is 40 knikkers. → **2** |
| 2 | 2 | [balk kleuren] Kleur #% van de balk. | 11 |  | `G7-VERH-01-claude-bank-018`: Kleur 50% van de balk. → **10** |
| 3 | 3 | Bij de schaal # : # [ding] twee getallen. Welk getal hoort bij de [ding]? | 1 |  | `G7-VERH-01-claude-bank-001`: Bij de schaal 1 : 500 horen twee getallen. Welk getal hoort bij de tekening? → **Het getal 1** |
| 4 | 4 | Op een tekening staat schaal # : #. Wat weet je dan over de tekening? | 1 |  | `G7-VERH-01-claude-bank-002`: Op een tekening staat schaal 1 : 1. Wat weet je dan over de tekening? → **De tekening is net zo groot als het echte voorwerp** |
| 5 | 5 | Op een tekening van een huis staat schaal # : #. Wat betekent dat? | 1 |  | `G7-VERH-01-claude-bank-003`: Op een tekening van een huis staat schaal 1 : 100. Wat betekent dat? → **1 cm op de tekening is 100 cm echt** |
| 6 | 6 | Waarom gebruik je een schaal als je een plattegrond van je huis tekent? | 1 |  | `G7-VERH-01-claude-bank-004`: Waarom gebruik je een schaal als je een plattegrond van je huis tekent? → **Omdat het echte huis niet op papier past** |
| 7 | 7 | Welke schrijfwijze is een schaal? | 1 |  | `G7-VERH-01-claude-bank-005`: Welke schrijfwijze is een schaal? → **1 : 25** |

### G7-VERH-02 — 7 somtypes · 1030 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Hoeveel is #% van #? | 534 |  | `G7-VERH-02-claude-bank-006`: Hoeveel is 75% van 192? → **144** |
| 2 | 2 | Hoeveel is #% van €#? | 243 |  | `G7-VERH-02-claude-bank-540`: Hoeveel is 25% van €20? → **€5** |
| 3 | 3 | Hoeveel procent is # van #? | 217 |  | `G7-VERH-02-claude-bank-783`: Hoeveel procent is 36 van 75? → **48%** |
| 4 | 4 | In [plek] liggen # [ding]. #% ervan is rood. Hoeveel rode [ding] zijn er? | 12 |  | `G7-VERH-02-claude-bank-1000`: In het moeras liggen 80 blaadjes. 10% ervan is rood. Hoeveel rode blaadjes zijn er? → **8** |
| 5 | 5 | In [plek] zijn # [ding]. #% is beschadigd. Hoeveel [ding] zijn beschadigd? | 12 |  | `G7-VERH-02-claude-bank-1012`: In het bos zijn 120 veren. 90% is beschadigd. Hoeveel veren zijn beschadigd? → **108** |
| 6 | 6 | Van de # [ding] hebben er # een [ding]. Hoeveel procent is dat? | 7 |  | `G7-VERH-02-claude-bank-1024`: Van de 80 spelers hebben er 4 een pion. Hoeveel procent is dat? → **5** |
| 7 | 7 | Een [ding] kost €#. Er is #% korting. Wat is de nieuwe prijs in euro's? | 5 |  | `G7-VERH-02-claude-bank-001`: Een pet kost €80. Er is 30% korting. Wat is de nieuwe prijs in euro's? → **56** |

### G7-VERH-03 — 25 somtypes · 642 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Vul in. # : # = # : ? | 331 |  | `G7-VERH-03-claude-bank-303`: Vul in. 4 : 9 = 8 : ? → **18** |
| 2 | 2 | # [ding] kosten €#. Hoeveel kosten # [ding]? | 264 |  | `G7-VERH-03-claude-bank-001`: 6 pennen kosten €3. Hoeveel kosten 11 pennen? → **€5,50** |
| 3 | 3 | Een tekening van # cm breed wordt # keer zo klein gemaakt. Hoe breed wordt de kleine teken | 9 |  | `G7-VERH-03-claude-bank-280`: Een tekening van 6 cm breed wordt 3 keer zo klein gemaakt. Hoe breed wordt de kleine tekening? → **2** |
| 4 | 4 | [rooster] Een rechthoek is # hokjes breed en # hokjes hoog. Kleur een rechthoek die # keer | 9 |  | `G7-VERH-03-claude-bank-634`: Een rechthoek is 1 hokje breed en 1 hokje hoog. Kleur een rechthoek die 2 keer zo groot is: elke zijde 2 keer … → **een rechthoek van 2 hokjes breed en 2 hokjes hoog** |
| 5 | 5 | Een foto is # cm breed en # cm hoog. Hij wordt # keer zo groot afgedrukt. Hoe breed wordt  | 7 |  | `G7-VERH-03-claude-bank-269`: Een foto is 3 cm breed en 5 cm hoog. Hij wordt 4 keer zo groot afgedrukt. Hoe breed wordt de foto? → **12** |
| 6 | 6 | Een vierkant van # bij # cm wordt # keer zo groot: elke zijde wordt # keer zo lang. Hoevee | 3 |  | `G7-VERH-03-claude-bank-290`: Een vierkant van 4 bij 4 cm wordt 4 keer zo groot: elke zijde wordt 4 keer zo lang. Hoeveel keer zo groot word… → **16** |
| 7 | 7 | Een [ding] is # m lang. Je tekent de tuin op schaal # : #. Dat betekent: # cm op de tekeni | 1 |  | `G7-VERH-03-claude-bank-265`: Een tuin is 8 m lang. Je tekent de tuin op schaal 1 : 100. Dat betekent: 1 cm op de tekening is 100 cm in het … → **8 cm** |
| 8 | 8 | Een [ding] is # m lang. Op een plattegrond met schaal # : # wordt het pad getekend. Hoe la | 1 |  | `G7-VERH-03-claude-bank-266`: Een fietspad is 60 m lang. Op een plattegrond met schaal 1 : 1000 wordt het pad getekend. Hoe lang is het pad … → **6 cm** |
| 9 | 9 | Een bank is in het echt # cm lang. Op een tekening met schaal # : # wordt de bank getekend | 1 |  | `G7-VERH-03-claude-bank-267`: Een bank is in het echt 300 cm lang. Op een tekening met schaal 1 : 100 wordt de bank getekend. Hoe lang wordt… → **3 cm** |
| 10 | 10 | Een echte boot is # m lang. Je maakt een model op schaal # : #. Dat betekent: # cm op de t | 1 |  | `G7-VERH-03-claude-bank-268`: Een echte boot is 6 m lang. Je maakt een model op schaal 1 : 20. Dat betekent: 1 cm op de tekening is 20 cm in… → **30 cm** |
| 11 | 11 | Een muur is in het echt # cm lang. Je tekent hem op schaal # : #. Dat betekent: # cm op de | 1 |  | `G7-VERH-03-claude-bank-276`: Een muur is in het echt 500 cm lang. Je tekent hem op schaal 1 : 100. Dat betekent: 1 cm op de tekening is 100… → **5 cm** |
| 12 | 12 | Een poppenhuis is gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in he | 1 |  | `G7-VERH-03-claude-bank-277`: Een poppenhuis is gemaakt op schaal 1 : 10. Dat betekent: 1 cm op de tekening is 10 cm in het echt. Een echte … → **9 cm** |
| 13 | 13 | Een speelgoedauto is gemaakt op schaal # : #. Dat betekent: # cm op de tekening is # cm in | 1 |  | `G7-VERH-03-claude-bank-278`: Een speelgoedauto is gemaakt op schaal 1 : 10. Dat betekent: 1 cm op de tekening is 10 cm in het echt. De auto… → **400 cm** |
| 14 | 14 | Een tekening heeft schaal # : #. Dat betekent: # cm op de tekening is # cm in het echt. Ho | 1 |  | `G7-VERH-03-claude-bank-279`: Een tekening heeft schaal 1 : 2. Dat betekent: 1 cm op de tekening is 2 cm in het echt. Hoe groot is het echte… → **2 keer zo groot** |
| 15 | 15 | Een tekening van een fiets heeft schaal # : #. Hoeveel cm is # cm op de tekening in het ec | 1 |  | `G7-VERH-03-claude-bank-289`: Een tekening van een fiets heeft schaal 1 : 50. Hoeveel cm is 1 cm op de tekening in het echt? → **50 cm** |
| 16 | 16 | In een tabel staat schaal # : #. Bij # cm op de tekening hoort # cm echt. Wat hoort er bij | 1 |  | `G7-VERH-03-claude-bank-293`: In een tabel staat schaal 1 : 100. Bij 1 cm op de tekening hoort 100 cm echt. Wat hoort er bij 2 cm op de teke… → **200 cm echt** |
| 17 | 17 | Je tekent dezelfde boom twee keer: een keer op schaal # : # en een keer op schaal # : #. D | 1 |  | `G7-VERH-03-claude-bank-294`: Je tekent dezelfde boom twee keer: een keer op schaal 1 : 10 en een keer op schaal 1 : 100. Dat betekent: 1 cm… → **De tekening op schaal 1 : 10** |
| 18 | 18 | Marit tekent een boom op schaal # : #. Dat betekent: # cm op de tekening is # cm in het ec | 1 |  | `G7-VERH-03-claude-bank-295`: Marit tekent een boom op schaal 1 : 25. Dat betekent: 1 cm op de tekening is 25 cm in het echt. Sem tekent dez… → **Sem** |
| 19 | 19 | Op een kaart van een park staat schaal # : #. Dat betekent: # cm op de kaart is # cm in he | 1 |  | `G7-VERH-03-claude-bank-296`: Op een kaart van een park staat schaal 1 : 1000. Dat betekent: 1 cm op de kaart is 1000 cm in het echt. Hoevee… → **10 m** |
| 20 | 20 | Op een landkaart staat schaal # : # #. Hoeveel is # cm op de kaart in het echt? | 1 |  | `G7-VERH-03-claude-bank-297`: Op een landkaart staat schaal 1 : 100 000. Hoeveel is 1 cm op de kaart in het echt? → **1 km** |
| 21 | 21 | Op een plattegrond staat schaal # : #. Dat betekent: # cm op de tekening is # cm in het ec | 1 |  | `G7-VERH-03-claude-bank-298`: Op een plattegrond staat schaal 1 : 200. Dat betekent: 1 cm op de tekening is 200 cm in het echt. Hoeveel is 1… → **2 m** |
| 22 | 22 | Op een plattegrond van een dierentuin met schaal # : # is een pad # cm lang. Hoe lang is h | 1 |  | `G7-VERH-03-claude-bank-299`: Op een plattegrond van een dierentuin met schaal 1 : 1000 is een pad 5 cm lang. Hoe lang is het pad in het ech… → **50 m** |
| 23 | 23 | Op een tekening met schaal # : # is een deur # cm hoog. Hoe hoog is de deur in het echt? | 1 |  | `G7-VERH-03-claude-bank-300`: Op een tekening met schaal 1 : 50 is een deur 4 cm hoog. Hoe hoog is de deur in het echt? → **200 cm** |
| 24 | 24 | Op een tekening met schaal # : # is een tafel # cm lang. Hoe lang is de tafel in het echt? | 1 |  | `G7-VERH-03-claude-bank-301`: Op een tekening met schaal 1 : 100 is een tafel 3 cm lang. Hoe lang is de tafel in het echt? → **300 cm** |
| 25 | 25 | Van een school wordt een maquette gemaakt op schaal # : #. Dat betekent: # cm op de tekeni | 1 |  | `G7-VERH-03-claude-bank-302`: Van een school wordt een maquette gemaakt op schaal 1 : 100. Dat betekent: 1 cm op de tekening is 100 cm in he… → **25 cm** |

### G7-VERH-04 — 6 somtypes · 137 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Schrijf #/# in procenten. | 110 |  | `G7-VERH-04-claude-bank-015`: Schrijf 32/50 in procenten. → **64%** |
| 2 | 4 | Deel van een totaal: welk deel van de [ding] is …? ('zoveel op de zoveel') | 9 |  | `G7-VERH-04-claude-bank-127`: In een doos liggen 20 kaartjes en op 5 kaartjes staat een ster. Welk deel van de kaartjes heeft een ster? → **1 op de 4** |
| 3 | 2 | Schrijf # in procenten. | 8 |  | `G7-VERH-04-claude-bank-007`: Schrijf 0,1 in procenten. → **10%** |
| 4 | 3 | #% van de [ding] is kapot. Schrijf dat als kommagetal. | 6 |  | `G7-VERH-04-claude-bank-001`: 75% van de pakken is kapot. Schrijf dat als kommagetal. → **0,75** |
| 5 | 5 | Deel van een totaal: hoeveel procent van de [ding] is …? | 3 |  | `G7-VERH-04-claude-bank-125`: Bij een loterij wint 1 op de 4 lootjes een prijs. Hoeveel procent van de lootjes wint een prijs? → **25%** |
| 6 | 6 | Deel van een totaal: in welke zak is het deel het grootst? (delen vergelijken) | 1 |  | `G7-VERH-04-claude-bank-133`: In zak A zijn 2 van de 4 knikkers rood. In zak B zijn 3 van de 9 knikkers rood. In welke zak is het deel rode … → **Zak A** |

## G8 — 223 somtypes open · 1458 items

### G8-GET-E02 — 57 somtypes · 254 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Op welk cijfer eindigt # × #? | 53 |  | `G8-GET-E02-claude-bank-061`: Op welk cijfer eindigt 19 × 17? → **3** |
| 2 | 51 | Hoeveel is # + # [ding]? Rond beide getallen af op duizendtallen en reken dan uit. | 30 |  | `G8-GET-E02-claude-bank-120`: Hoeveel is 4250 + 7642 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit. → **12.000** |
| 3 | 52 | Hoeveel is # × # [ding]? Rond # af op honderdtallen en # op tientallen, en reken dan uit. | 29 |  | `G8-GET-E02-claude-bank-166`: Hoeveel is 189 × 61 ongeveer? Rond 189 af op honderdtallen en 61 op tientallen, en reken dan uit. → **12.000** |
| 4 | 53 | Hoeveel is # × # [ding]? Rond beide getallen af op tientallen en reken dan uit. | 26 |  | `G8-GET-E02-claude-bank-195`: Hoeveel is 68 × 72 ongeveer? Rond beide getallen af op tientallen en reken dan uit. → **4900** |
| 5 | 54 | Kijk zonder uit te rekenen. Welk antwoord bij # × # [ding] kloppen? | 19 |  | `G8-GET-E02-claude-bank-237`: Kijk zonder uit te rekenen. Welk antwoord bij 467 × 9 kan kloppen? → **4203** |
| 6 | 55 | Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. | 16 |  | `G8-GET-E02-claude-bank-150`: Hoeveel is 404 + 851 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit. → **1300** |
| 7 | 56 | Hoeveel is # − # [ding]? Rond beide getallen af op duizendtallen en reken dan uit. | 8 |  | `G8-GET-E02-claude-bank-221`: Hoeveel is 4460 − 1324 ongeveer? Rond beide getallen af op duizendtallen en reken dan uit. → **3000** |
| 8 | 2 | In [plek] liggen # [ding] en er komen # bij. Schat het totaal: rond beide getallen af op d | 8 |  | `G8-GET-E02-claude-bank-022`: In het veld liggen 3215 ballen en er komen 1927 bij. Schat het totaal: rond beide getallen af op duizendtallen… → **5000** |
| 9 | 57 | Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? | 8 |  | `G8-GET-E02-claude-bank-229`: Kijk zonder uit te rekenen. Welk antwoord bij 737 + 776 kan kloppen? → **1513** |
| 10 | 3 | Ongeveer hoeveel is # × #? Rond # af op honderdtallen en # op tientallen, en reken dan uit | 8 |  | `G8-GET-E02-claude-bank-052`: Ongeveer hoeveel is 124 × 37? Rond 124 af op honderdtallen en 37 op tientallen, en reken dan uit. → **4000** |
| 11 | 4 | # [ding] met elk # [ding]. Schat hoeveel dat ongeveer is: rond # af op honderdtallen en re | 3 |  | `G8-GET-E02-claude-bank-002`: 5 dozen met elk 497 tanden. Schat hoeveel dat ongeveer is: rond 497 af op honderdtallen en reken dan uit. → **2500** |
| 12 | 5 | 's Ochtends is het # graden en 's middags # graden. Hoe reken je uit hoeveel graden het wa | 1 |  | `G8-GET-E02-claude-bank-005`: 's Ochtends is het 3 graden en 's middags 11 graden. Hoe reken je uit hoeveel graden het warmer is geworden? → **Trek 3 van 11 af** |
| 13 | 6 | Bas koopt # [ding] sap van €#. Hij krijgt €# als antwoord. Wat laat zien dat dit niet klop | 1 |  | `G8-GET-E02-claude-bank-006`: Bas koopt 6 pakken sap van €1,99. Hij krijgt €119,40 als antwoord. Wat laat zien dat dit niet klopt? → **6 pakken kosten ongeveer €12** |
| 14 | 7 | Bij een spel krijg je # [ding] voor elk doelpunt. Voor elke misser gaat er # [ding] af. Ho | 1 |  | `G8-GET-E02-claude-bank-007`: Bij een spel krijg je 3 punten voor elk doelpunt. Voor elke misser gaat er 1 punt af. Hoe reken je de score ui… → **Doelpunten maal 3, dan het aantal missers eraf.** |
| 15 | 8 | Bram heeft # [ding] met # [ding]. Hij rekent uit dat er # [ding] zijn. Wat laat zien dat d | 1 |  | `G8-GET-E02-claude-bank-008`: Bram heeft 12 zakjes met 15 knikkers. Hij rekent uit dat er 27 knikkers zijn. Wat laat zien dat dit niet kan? → **Eén zakje heeft al 15, dus 12 zakjes zijn veel meer** |
| 16 | 9 | De trein vertrekt om #:# en komt aan om #:#. Hoe reken je handig uit hoe lang de reis duur | 1 |  | `G8-GET-E02-claude-bank-009`: De trein vertrekt om 14:35 en komt aan om 16:10. Hoe reken je handig uit hoe lang de reis duurt? → **Reken eerst tot 15:00, dan verder tot 16:10.** |
| 17 | 10 | Een [ding] is # m lang en # m breed. Fleur wil weten hoeveel vierkante meter het bad is en | 1 |  | `G8-GET-E02-claude-bank-010`: Een zwembad is 25 m lang en 10 m breed. Fleur wil weten hoeveel vierkante meter het bad is en rekent 25 + 10 +… → **Ze rekende de omtrek in plaats van de oppervlakte** |
| 18 | 11 | Een [ding] is # m lang en # m breed. Je legt tegels van # vierkante meter. Hoe reken je ui | 1 |  | `G8-GET-E02-claude-bank-011`: Een kamer is 5 m lang en 3 m breed. Je legt tegels van 1 vierkante meter. Hoe reken je uit hoeveel tegels je n… → **Lengte keer breedte doen, dat is het aantal** |
| 19 | 12 | Een [ding] is # m lang en # m breed. Joep wil weten hoeveel meter hek hij nodig heeft en r | 1 |  | `G8-GET-E02-claude-bank-012`: Een tuin is 8 m lang en 5 m breed. Joep wil weten hoeveel meter hek hij nodig heeft en rekent 8 × 5 = 40. Wat … → **Hij rekende de oppervlakte in plaats van de omtrek** |
| 20 | 13 | Een broek van €# wordt # procent goedkoper. Rik rekent uit dat de broek nu €# [ding]. Wat  | 1 |  | `G8-GET-E02-claude-bank-013`: Een broek van €40 wordt 10 procent goedkoper. Rik rekent uit dat de broek nu €30 kost. Wat ging er mis? → **Hij haalde €10 eraf in plaats van 10 procent** |
| 21 | 14 | Een jas van €# [ding] # procent in prijs omlaag. Milou rekent uit dat de jas nu €# [ding]. | 1 |  | `G8-GET-E02-claude-bank-014`: Een jas van €60 gaat 25 procent in prijs omlaag. Milou rekent uit dat de jas nu €15 kost. Wat ging er mis? → **€15 is de korting, niet de nieuwe prijs** |
| 22 | 15 | Een recept voor # [ding] vraagt # gram rijst. Daan wil koken voor # [ding] en pakt # gram. | 1 |  | `G8-GET-E02-claude-bank-015`: Een recept voor 4 personen vraagt 300 gram rijst. Daan wil koken voor 8 personen en pakt 600 gram. Klopt zijn … → **Ja, hij verdubbelde beide getallen** |
| 23 | 16 | Een recept voor # [ding] vraagt # gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt | 1 |  | `G8-GET-E02-claude-bank-016`: Een recept voor 4 personen vraagt 200 gram rijst. Hoe reken je uit hoeveel rijst je nodig hebt voor 6 personen… → **Deel 200 door 4 en doe dat keer 6** |
| 24 | 17 | Een stadion heeft # [ding] met # [ding]. Anne schat vooraf ongeveer # [ding] en rekent daa | 1 |  | `G8-GET-E02-claude-bank-017`: Een stadion heeft 4 vakken met 1980 stoelen. Anne schat vooraf ongeveer 8000 stoelen en rekent daarna precies … → **Haar schatting past goed bij het antwoord** |
| 25 | 18 | Eva rekent # : # uit en krijgt #. Hoe kan ze snel controleren of dit klopt? | 1 |  | `G8-GET-E02-claude-bank-018`: Eva rekent 63 : 7 uit en krijgt 8. Hoe kan ze snel controleren of dit klopt? → **7 × 8 uitrekenen en met 63 vergelijken** |
| 26 | 19 | Fenna heeft # + # = # [ding]. Hoe kan zij haar antwoord het beste controleren? | 1 |  | `G8-GET-E02-claude-bank-019`: Fenna heeft 234 + 178 = 412 uitgerekend. Hoe kan zij haar antwoord het beste controleren? → **412 − 178 uitrekenen en kijken of 234 komt** |
| 27 | 20 | Hoe zie je of een getal deelbaar is door #? | 1 |  | `G8-GET-E02-claude-bank-020`: Hoe zie je of een getal deelbaar is door 5? → **Kijk of het laatste cijfer 0 of 5 is** |
| 28 | 21 | Hoe zie je of een getal even is? | 1 |  | `G8-GET-E02-claude-bank-021`: Hoe zie je of een getal even is? → **Kijk of het laatste cijfer 0, 2, 4, 6 of 8 is.** |
| 29 | 22 | In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag # graden af, maar hi | 1 |  | `G8-GET-E02-claude-bank-030`: In een grafiek staat de temperatuur per dag. Ruben leest bij woensdag 14 graden af, maar hij keek per ongeluk … → **Eerst de naam onder de staaf lezen** |
| 30 | 23 | In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele | 1 |  | `G8-GET-E02-claude-bank-031`: In een staafgrafiek staat het aantal bezoekers per dag. Hoe vind je het totaal van de hele week? → **Lees elke staaf af en tel alle waarden op** |
| 31 | 24 | In een winkel is er op alles # procent korting. Hoe reken je de nieuwe prijs uit? | 1 |  | `G8-GET-E02-claude-bank-032`: In een winkel is er op alles 25 procent korting. Hoe reken je de nieuwe prijs uit? → **Bereken 25 procent van de prijs en trek dat eraf.** |
| 32 | 25 | In groep # [ding] # [ding]. # procent doet mee aan de sportdag. Hoe reken je uit hoeveel l | 1 |  | `G8-GET-E02-claude-bank-033`: In groep 8 zitten 40 leerlingen. 15 procent doet mee aan de sportdag. Hoe reken je uit hoeveel leerlingen dat … → **Deel 40 door 100 en doe dat keer 15** |
| 33 | 26 | Je doet # kg appels in zakjes van # gram. Je wilt weten hoeveel zakjes dat worden. Wat doe | 1 |  | `G8-GET-E02-claude-bank-034`: Je doet 2,5 kg appels in zakjes van 500 gram. Je wilt weten hoeveel zakjes dat worden. Wat doe je eerst? → **Reken 2,5 kg om naar 2500 gram.** |
| 34 | 27 | Je fietst # [ding] in # uur. Hoe reken je uit hoeveel kilometer je in # uur fietst? | 1 |  | `G8-GET-E02-claude-bank-035`: Je fietst 24 kilometer in 2 uur. Hoe reken je uit hoeveel kilometer je in 1 uur fietst? → **Deel 24 door 2** |
| 35 | 28 | Je hebt # [ding] en # [ding]. Hoe reken je uit hoeveel koekjes [wie] krijgt en hoeveel er  | 1 |  | `G8-GET-E02-claude-bank-036`: Je hebt 50 koekjes en 8 kinderen. Hoe reken je uit hoeveel koekjes elk kind krijgt en hoeveel er overblijven? → **Deel 50 door 8 en kijk naar de rest** |
| 36 | 29 | Je hebt # [ding] en dozen voor # [ding]. Hoe reken je uit hoeveel volle dozen je kunt make | 1 |  | `G8-GET-E02-claude-bank-037`: Je hebt 40 eieren en dozen voor 6 eieren. Hoe reken je uit hoeveel volle dozen je kunt maken? → **Deel 40 door 6 en gebruik alleen het hele aantal.** |
| 37 | 30 | Je koopt # [ding] van # euro en # [ding] van # euro. Hoe reken je uit hoeveel je in totaal | 1 |  | `G8-GET-E02-claude-bank-038`: Je koopt 3 truien van 12 euro en 2 petten van 7 euro. Hoe reken je uit hoeveel je in totaal betaalt? → **Reken 3 maal 12 en 2 maal 7 en tel die uitkomsten op.** |
| 38 | 31 | Je koopt een pen van # euro en een gum van # euro. Je betaalt met # euro. Hoe reken je uit | 1 |  | `G8-GET-E02-claude-bank-039`: Je koopt een pen van 2 euro en een gum van 1 euro. Je betaalt met 5 euro. Hoe reken je uit hoeveel wisselgeld … → **Tel de prijzen op, trek die van het betaalde bedrag af.** |
| 39 | 32 | Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg | 1 |  | `G8-GET-E02-claude-bank-040`: Je legt aan een klasgenoot uit hoe je een boek in de schoolbibliotheek vindt. Welke uitleg is het duidelijkst? → **Zoek de letter, loop naar dat vak, pak het boek.** |
| 40 | 33 | Je moet # [ding] op alfabetische volgorde zetten. Welke aanpak werkt altijd? | 1 |  | `G8-GET-E02-claude-bank-041`: Je moet 12 namen op alfabetische volgorde zetten. Welke aanpak werkt altijd? → **Zoek steeds de eerste naam en zet die apart** |
| 41 | 34 | Je spaart elke week # euro en wilt # euro hebben. Hoe reken je uit hoeveel weken je moet s | 1 |  | `G8-GET-E02-claude-bank-042`: Je spaart elke week 3 euro en wilt 45 euro hebben. Hoe reken je uit hoeveel weken je moet sparen? → **Deel 45 door 3** |
| 42 | 35 | Je verdeelt een pak sap van # liter over [bakken] van # [ding]. Je wilt weten hoeveel beke | 1 |  | `G8-GET-E02-claude-bank-043`: Je verdeelt een pak sap van 1,5 liter over bekers van 250 milliliter. Je wilt weten hoeveel bekers je kunt vul… → **Reken 1,5 liter om naar 1500 milliliter** |
| 43 | 36 | Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit? | 1 |  | `G8-GET-E02-claude-bank-044`: Je wilt de omtrek van een rechthoekige tuin weten. Hoe reken je die uit? → **Tel lengte en breedte op en verdubbel die som.** |
| 44 | 37 | Je wilt het gemiddelde van # [ding] weten. Hoe reken je dat uit? | 1 |  | `G8-GET-E02-claude-bank-045`: Je wilt het gemiddelde van 5 rapportcijfers weten. Hoe reken je dat uit? → **Tel alle cijfers op en deel de som door 5.** |
| 45 | 38 | Jinte moet # × # [ding]. Welke aanpak is het handigst? | 1 |  | `G8-GET-E02-claude-bank-046`: Jinte moet 5 × 98 uitrekenen. Welke aanpak is het handigst? → **5 × 100 doen en er 10 afhalen** |
| 46 | 39 | Kim moet # × # [ding]. Ze doet eerst # × # = # en neemt dan de helft. Klopt deze aanpak? | 1 |  | `G8-GET-E02-claude-bank-047`: Kim moet 36 × 5 uitrekenen. Ze doet eerst 36 × 10 = 360 en neemt dan de helft. Klopt deze aanpak? → **Ja, 5 is de helft van 10** |
| 47 | 40 | Lars zet # [ding] jam in [bakken] van #. Hij rekent # : # en schrijft # [ding] op. Wat is  | 1 |  | `G8-GET-E02-claude-bank-048`: Lars zet 148 potjes jam in dozen van 10. Hij rekent 148 : 10 en schrijft 14 dozen op. Wat is er mis met zijn a… → **Er blijven 8 potjes over, dus er is een extra doos nodig** |
| 48 | 41 | Mees moet # × # [ding]. Hij telt # + # + # + # op. Wat had handiger gekund? | 1 |  | `G8-GET-E02-claude-bank-049`: Mees moet 4 × 250 uitrekenen. Hij telt 250 + 250 + 250 + 250 op. Wat had handiger gekund? → **Meteen 4 × 250 vermenigvuldigen** |
| 49 | 42 | Noor moet # × # [ding] en telt acht keer # bij elkaar op. Wat had handiger gekund? | 1 |  | `G8-GET-E02-claude-bank-050`: Noor moet 25 × 8 uitrekenen en telt acht keer 25 bij elkaar op. Wat had handiger gekund? → **25 × 4 doen en dan verdubbelen** |
| 50 | 43 | Nout heeft # − # [ding] elkaar uitgerekend en kreeg #. Hij schatte vooraf ongeveer #. Wat  | 1 |  | `G8-GET-E02-claude-bank-051`: Nout heeft 802 − 397 onder elkaar uitgerekend en kreeg 505. Hij schatte vooraf ongeveer 400. Wat moet hij nu d… → **De som opnieuw uitrekenen, want de schatting past niet** |
| 51 | 44 | Op de fietstocht rijdt Tess # km. Ze schrijft op dat dit # meter is. Hoe merk je dat dit n | 1 |  | `G8-GET-E02-claude-bank-060`: Op de fietstocht rijdt Tess 3,2 km. Ze schrijft op dat dit 32 meter is. Hoe merk je dat dit niet klopt? → **1 km is al 1000 meter, dus het moeten er veel meer zijn** |
| 52 | 45 | Roos rekent # × # uit door # × # en # × # [ding] te doen. Ze schrijft alleen # op. Wat gin | 1 |  | `G8-GET-E02-claude-bank-114`: Roos rekent 7 × 24 uit door 7 × 20 en 7 × 4 apart te doen. Ze schrijft alleen 140 op. Wat ging er mis? → **Ze vergat 28 erbij op te tellen** |
| 53 | 46 | Sam rekent # − # uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekun | 1 |  | `G8-GET-E02-claude-bank-115`: Sam rekent 1000 − 998 uit met een som onder elkaar en moet steeds lenen. Wat had handiger gekund? → **Doortellen van 998 naar 1000** |
| 54 | 47 | Sanne rekent # + # uit door eerst # + # te doen en er daarna # af te halen. Klopt deze aan | 1 |  | `G8-GET-E02-claude-bank-116`: Sanne rekent 198 + 56 uit door eerst 200 + 56 te doen en er daarna 2 af te halen. Klopt deze aanpak? → **Ja, dat is een handige manier** |
| 55 | 48 | Tim rekent # + # uit met een staartsom onder elkaar. Wat is een handigere aanpak? | 1 |  | `G8-GET-E02-claude-bank-117`: Tim rekent 99 + 47 uit met een staartsom onder elkaar. Wat is een handigere aanpak? → **Eerst 100 erbij, dan 1 eraf** |
| 56 | 49 | Voor een uitje gaan # [ding] mee. In een busje passen # [ding]. Lisa rekent # : # en schri | 1 |  | `G8-GET-E02-claude-bank-118`: Voor een uitje gaan 50 kinderen mee. In een busje passen 12 kinderen. Lisa rekent 50 : 12 en schrijft 4 busjes… → **Ze vergat de 2 kinderen die overblijven** |
| 57 | 50 | Yara loopt # km naar school. Ze schrijft op dat dit # meter is. Hoe merk je dat dit niet k | 1 |  | `G8-GET-E02-claude-bank-119`: Yara loopt 2,5 km naar school. Ze schrijft op dat dit 250 meter is. Hoe merk je dat dit niet kan? → **1 km is 1000 meter, dus het zijn er meer** |

### G8-GET-E03 — 5 somtypes · 64 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Reken uit: (# + #) × # | 21 |  | `G8-GET-E03-claude-bank-044`: Reken uit: (12 + 2) × 5 → **70** |
| 2 | 2 | Reken uit. # : # + # | 12 |  | `G8-GET-E03-claude-bank-021`: Reken uit. 27 : 3 + 11 → **20** |
| 3 | 3 | Reken uit. # + # × (# − #) | 11 |  | `G8-GET-E03-claude-bank-010`: Reken uit. 9 + 4 × (3 − 1) → **17** |
| 4 | 4 | Reken uit. # − # × # | 11 |  | `G8-GET-E03-claude-bank-033`: Reken uit. 26 − 5 × 2 → **16** |
| 5 | 5 | Reken uit. # + # × # | 9 |  | `G8-GET-E03-claude-bank-001`: Reken uit. 4 + 4 × 2 → **12** |

### G8-GET-E04 — 8 somtypes · 45 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | # [ding] worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat? | 14 |  | `G8-GET-E04-claude-bank-004`: 3 pannenkoeken worden in stukken van 1/4 verdeeld. Hoeveel stukken zijn dat? → **12** |
| 2 | 2 | # liter limonade wordt in [bakken] van #/# liter geschonken. Hoeveel [ding] zijn dat? | 6 |  | `G8-GET-E04-claude-bank-025`: 4 liter limonade wordt in bekers van 1/5 liter geschonken. Hoeveel bekers zijn dat? → **20** |
| 3 | 3 | Er is nog #/# [ding]. [wie] eet daar #/# deel van. Welk deel van de hele taart is dat? Typ | 6 |  | `G8-GET-E04-claude-bank-039`: Er is nog 1/3 taart. Een kind eet daar 1/2 deel van. Welk deel van de hele taart is dat? Typ een breuk. → **1/6** |
| 4 | 4 | # [ding] wordt in stukken van #/# [ding]. Hoeveel [ding] zijn dat? | 5 |  | `G8-GET-E04-claude-bank-019`: 1 pizza wordt in stukken van 1/6 verdeeld. Hoeveel stukken zijn dat? → **6** |
| 5 | 5 | #/# [ding] wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat? | 4 |  | `G8-GET-E04-claude-bank-034`: 1/2 pannenkoek wordt verdeeld in stukken van 1/4. Hoeveel stukken zijn dat? → **2** |
| 6 | 6 | [wie] eet #/# van een pizza, een ander kind #/#. Welk deel is samen op? Typ een breuk. | 4 |  | `G8-GET-E04-claude-bank-045`: Een kind eet 1/3 van een pizza, een ander kind 1/4. Welk deel is samen op? Typ een breuk. → **7/12** |
| 7 | 7 | # [ding] chocola worden in stukken van #/# [ding]. Hoeveel [ding] zijn dat? | 3 |  | `G8-GET-E04-claude-bank-001`: 3 repen chocola worden in stukken van 1/5 verdeeld. Hoeveel stukken zijn dat? → **15** |
| 8 | 8 | #/# [ding] chocola wordt verdeeld in stukken van #/#. Hoeveel [ding] zijn dat? | 3 |  | `G8-GET-E04-claude-bank-031`: 6/8 reep chocola wordt verdeeld in stukken van 1/4. Hoeveel stukken zijn dat? → **3** |

### G8-GET-E05 — 16 somtypes · 125 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding]  | 13 |  | `G8-GET-E05-claude-bank-053`: In een kist passen 2 boeken. Er zijn 45 boeken. Op de rekenmachine staat 22,5. Hoeveel kisten zijn er nodig? → **23** |
| 2 | 2 | In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding]  | 12 |  | `G8-GET-E05-claude-bank-036`: In een doos passen 25 eieren. Er zijn 371 eieren. Op de rekenmachine staat 14,84. Hoeveel dozen zijn er nodig? → **15** |
| 3 | 3 | In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding]  | 11 |  | `G8-GET-E05-claude-bank-088`: In een mand passen 4 peren. Er zijn 65 peren. Op de rekenmachine staat 16,25. Hoeveel manden zijn er nodig? → **17** |
| 4 | 4 | In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] z | 10 |  | `G8-GET-E05-claude-bank-116`: In een zak passen 25 appels. Er zijn 3681 appels. Op de rekenmachine staat 147,24. Hoeveel zakken zijn er nodi… → **148** |
| 5 | 5 | In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] z | 9 |  | `G8-GET-E05-claude-bank-009`: In een bak passen 25 potjes. Er zijn 854 potjes. Op de rekenmachine staat 34,16. Hoeveel bakken zijn er nodig? → **35** |
| 6 | 6 | In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] | 9 |  | `G8-GET-E05-claude-bank-024`: In een busje passen 2 kinderen. Er zijn 21 kinderen. Op de rekenmachine staat 10,5. Hoeveel busjes zijn er nod… → **11** |
| 7 | 7 | In een bak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle bakken  | 8 |  | `G8-GET-E05-claude-bank-001`: In een bak passen 8 potjes. Er zijn 141 potjes. Op de rekenmachine staat 17,625. De volle bakken gaan weg. Hoe… → **5** |
| 8 | 8 | In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding]  | 8 |  | `G8-GET-E05-claude-bank-072`: In een krat passen 25 flesjes. Er zijn 1106 flesjes. Op de rekenmachine staat 44,24. Hoeveel kratten zijn er n… → **45** |
| 9 | 9 | In een mand passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle manden | 8 |  | `G8-GET-E05-claude-bank-080`: In een mand passen 20 peren. Er zijn 532 peren. Op de rekenmachine staat 26,6. De volle manden gaan weg. Hoeve… → **12** |
| 10 | 10 | In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. Hoeveel [ding] z | 8 |  | `G8-GET-E05-claude-bank-101`: In een tas passen 25 knikkers. Er zijn 3063 knikkers. Op de rekenmachine staat 122,52. Hoeveel tassen zijn er … → **123** |
| 11 | 11 | In een zak passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle zakken  | 7 |  | `G8-GET-E05-claude-bank-109`: In een zak passen 40 appels. Er zijn 2754 appels. Op de rekenmachine staat 68,85. De volle zakken gaan weg. Ho… → **34** |
| 12 | 12 | In een busje passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle busje | 6 |  | `G8-GET-E05-claude-bank-018`: In een busje passen 8 kinderen. Er zijn 159 kinderen. Op de rekenmachine staat 19,875. De volle busjes gaan we… → **7** |
| 13 | 13 | In een krat passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kratte | 6 |  | `G8-GET-E05-claude-bank-066`: In een krat passen 25 flesjes. Er zijn 394 flesjes. Op de rekenmachine staat 15,76. De volle kratten gaan weg.… → **19** |
| 14 | 14 | In een kist passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle kisten | 5 |  | `G8-GET-E05-claude-bank-048`: In een kist passen 20 boeken. Er zijn 831 boeken. Op de rekenmachine staat 41,55. De volle kisten gaan weg. Ho… → **11** |
| 15 | 15 | In een doos passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle dozen  | 3 |  | `G8-GET-E05-claude-bank-033`: In een doos passen 40 eieren. Er zijn 900 eieren. Op de rekenmachine staat 22,5. De volle dozen gaan weg. Hoev… → **20** |
| 16 | 16 | In een tas passen # [ding]. Er zijn # [ding]. Op de rekenmachine staat #. De volle tassen  | 2 |  | `G8-GET-E05-claude-bank-099`: In een tas passen 50 knikkers. Er zijn 3681 knikkers. Op de rekenmachine staat 73,62. De volle tassen gaan weg… → **31** |

### G8-GET-M01 — 5 somtypes · 12 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | In [plek] leven # [ding]. Hoeveel is de # in dit getal waard? | 5 |  | `G8-GET-M01-claude-bank-001`: In de vallei leven 9.567.000 insecten. Hoeveel is de 9 in dit getal waard? → **9.000.000** |
| 2 | 2 | In een land wonen # [ding] mensen. Schrijf dat als getal. | 3 |  | `G8-GET-M01-claude-bank-006`: In een land wonen 2 miljoen mensen. Schrijf dat als getal. → **2.000.000** |
| 3 | 3 | [wie] heeft # [ding] stickers verzameld. Schrijf dat als getal. | 2 |  | `G8-GET-M01-claude-bank-010`: Een kind heeft 2 miljoen stickers verzameld. Schrijf dat als getal. → **2.000.000** |
| 4 | 4 | [wie] heeft # [ding] knikkers verzameld. Schrijf dat als getal. | 1 |  | `G8-GET-M01-claude-bank-009`: Een kind heeft 3 miljoen knikkers verzameld. Schrijf dat als getal. → **3.000.000** |
| 5 | 5 | [wie] heeft # [ding] truien verzameld. Schrijf dat als getal. | 1 |  | `G8-GET-M01-claude-bank-012`: Een kind heeft 7 miljoen truien verzameld. Schrijf dat als getal. → **7.000.000** |

### G8-GET-V02 — 4 somtypes · 4 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een groep van # [ding] heeft gemiddeld # [ding]. Hoeveel knikkers hebben zij samen? | 1 |  | `G8-GET-V02-claude-bank-001`: Een groep van 8 kinderen heeft gemiddeld 5 knikkers. Hoeveel knikkers hebben zij samen? → **40 knikkers** |
| 2 | 2 | In een zwembad zwemmen op zaterdag # [ding] en op zondag # [ding]. Hoeveel mensen zwommen  | 1 |  | `G8-GET-V02-claude-bank-002`: In een zwembad zwemmen op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er dat weekend g… → **300 mensen** |
| 3 | 3 | In groep # [ding] # [ding] een cijfer voor een toets. Tien kinderen hebben een #, vijf kin | 1 |  | `G8-GET-V02-claude-bank-003`: In groep 8 hebben 20 kinderen een cijfer voor een toets. Tien kinderen hebben een 7, vijf kinderen een 8 en vi… → **7** |
| 4 | 4 | Mila fietst vier dagen naar school. # km, # km, # km en # km. Hoeveel kilometer fietst zij | 1 |  | `G8-GET-V02-claude-bank-004`: Mila fietst vier dagen naar school. 3 km, 5 km, 4 km en 4 km. Hoeveel kilometer fietst zij gemiddeld per dag? → **4 km** |

### G8-MEET-E01 — 2 somtypes · 4 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een wandelaar loopt # km. Hoeveel meter is dat? | 2 |  | `G8-MEET-E01-claude-bank-001`: Een wandelaar loopt 6,7 km. Hoeveel meter is dat? → **6700** |
| 2 | 2 | [wie] loopt # km. Hoeveel meter is dat? | 2 |  | `G8-MEET-E01-claude-bank-003`: Een kind loopt 8 km. Hoeveel meter is dat? → **8000** |

### G8-MEET-E03 — 9 somtypes · 32 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 5 | Een filmpje is # MB. De geheugenkaart is # GB (# GB = # MB). Hoeveel van die filmpjes pass | 16 |  | `G8-MEET-E03-claude-bank-006`: Een filmpje is 250 MB. De geheugenkaart is 64 GB (1 GB = 1000 MB). Hoeveel van die filmpjes passen erop? → **256** |
| 2 | 6 | Een harde schijf heeft # TB. Hoeveel GB is dat? (# TB = # GB) | 5 |  | `G8-MEET-E03-claude-bank-028`: Een harde schijf heeft 3 TB. Hoeveel GB is dat? (1 TB = 1000 GB) → **3000** |
| 3 | 7 | Een foto is # MB. Hoeveel KB is dat? (# MB = # KB) | 3 |  | `G8-MEET-E03-claude-bank-022`: Een foto is 3 MB. Hoeveel KB is dat? (1 MB = 1000 KB) → **3000** |
| 4 | 8 | Een geheugenkaart heeft # GB. Hoeveel MB is dat? (# GB = # MB) | 3 |  | `G8-MEET-E03-claude-bank-025`: Een geheugenkaart heeft 4 GB. Hoeveel MB is dat? (1 GB = 1000 MB) → **4000** |
| 5 | 1 | Een bak voor knopen heeft een inhoud van # [ding]. Hoeveel liter is dat? | 1 |  | `G8-MEET-E03-claude-bank-001`: Een bak voor knopen heeft een inhoud van 3 m³. Hoeveel liter is dat? → **3000** |
| 6 | 2 | Een bak voor tanden heeft een inhoud van # [ding]. Hoeveel liter is dat? | 1 |  | `G8-MEET-E03-claude-bank-002`: Een bak voor tanden heeft een inhoud van 1,5 m³. Hoeveel liter is dat? → **1500** |
| 7 | 3 | Een bak voor truien heeft een inhoud van # [ding]. Hoeveel liter is dat? | 1 |  | `G8-MEET-E03-claude-bank-003`: Een bak voor truien heeft een inhoud van 3 m³. Hoeveel liter is dat? → **3000** |
| 8 | 4 | Een bak voor wortels heeft een inhoud van # [ding]. Hoeveel liter is dat? | 1 |  | `G8-MEET-E03-claude-bank-004`: Een bak voor wortels heeft een inhoud van 3 m³. Hoeveel liter is dat? → **3000** |
| 9 | 9 | Een film is # GB. Hoeveel MB is dat? (# GB = # MB) | 1 |  | `G8-MEET-E03-claude-bank-005`: Een film is 3 GB. Hoeveel MB is dat? (1 GB = 1000 MB) → **3000** |

### G8-MEET-E05 — 3 somtypes · 229 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 2 | Het is # °C. Het wordt # graden kouder. Hoe koud is het dan, in °C? | 149 |  | `G8-MEET-E05-claude-bank-013`: Het is 7 °C. Het wordt 16 graden kouder. Hoe koud is het dan, in °C? → **−9** |
| 2 | 3 | Het is −# °C. Dat is # graden onder nul. Het wordt # graden kouder. Hoe koud is het dan, i | 68 |  | `G8-MEET-E05-claude-bank-162`: Het is −3 °C. Dat is 3 graden onder nul. Het wordt 15 graden kouder. Hoe koud is het dan, in °C? → **−18** |
| 3 | 1 | [stip op getallenlijn zetten] Zet # op de getallenlijn. | 12 |  | `G8-MEET-E05-claude-bank-001`: Zet −5 op de getallenlijn. → **−5** |

### G8-MEET-E06 — 12 somtypes · 32 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Hoe laat lan | 12 |  | `G8-MEET-E06-claude-bank-001`: Een vliegtuig vertrekt om 6:15 uit de dierentuin. De vlucht duurt 5 uur en 45 minuten. Hoe laat landt het? (Ty… → **12:00** |
| 2 | 2 | Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Op de plek v | 6 |  | `G8-MEET-E06-claude-bank-013`: Een vliegtuig vertrekt om 11:45 uit de dierentuin. De vlucht duurt 8 uur en 30 minuten. Op de plek van aankoms… → **21:15** |
| 3 | 3 | Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur en # minuten. Op de plek v | 4 |  | `G8-MEET-E06-claude-bank-019`: Een vliegtuig vertrekt om 6:45 uit het stadion. De vlucht duurt 10 uur en 30 minuten. Op de plek van aankomst … → **15:15** |
| 4 | 4 | Een vliegtuig vertrekt om #:# uit de school. De vlucht duurt # uur en # minuten. Hoe laat  | 2 |  | `G8-MEET-E06-claude-bank-028`: Een vliegtuig vertrekt om 7:30 uit de school. De vlucht duurt 11 uur en 45 minuten. Hoe laat landt het? (Typ a… → **19:15** |
| 5 | 5 | Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur. Op de plek van aankomst i | 1 |  | `G8-MEET-E06-claude-bank-023`: Een vliegtuig vertrekt om 13:45 uit het nest. De vlucht duurt 4 uur. Op de plek van aankomst is het 8 uur late… → **1:45** |
| 6 | 6 | Een vliegtuig vertrekt om #:# uit [plek]. De vlucht duurt # uur. Op de plek van aankomst i | 1 |  | `G8-MEET-E06-claude-bank-024`: Een vliegtuig vertrekt om 9:45 uit het museum. De vlucht duurt 8 uur. Op de plek van aankomst is het 6 uur vro… → **11:45** |
| 7 | 7 | Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur en # minuten. Op de plek  | 1 |  | `G8-MEET-E06-claude-bank-025`: Een vliegtuig vertrekt om 9:30 uit de klas. De vlucht duurt 7 uur en 30 minuten. Op de plek van aankomst is he… → **15:00** |
| 8 | 8 | Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur. Hoe laat landt het? (Typ | 1 |  | `G8-MEET-E06-claude-bank-026`: Een vliegtuig vertrekt om 10:00 uit de klas. De vlucht duurt 2 uur. Hoe laat landt het? (Typ als 14:30.) → **12:00** |
| 9 | 9 | Een vliegtuig vertrekt om #:# uit de klas. De vlucht duurt # uur. Op de plek van aankomst  | 1 |  | `G8-MEET-E06-claude-bank-027`: Een vliegtuig vertrekt om 11:45 uit de klas. De vlucht duurt 3 uur. Op de plek van aankomst is het 2 uur vroeg… → **12:45** |
| 10 | 10 | Een vliegtuig vertrekt om #:# uit de school. De vlucht duurt # uur en # minuten. Op de ple | 1 |  | `G8-MEET-E06-claude-bank-030`: Een vliegtuig vertrekt om 14:00 uit de school. De vlucht duurt 11 uur en 15 minuten. Op de plek van aankomst i… → **2:15** |
| 11 | 11 | Een vliegtuig vertrekt om #:# uit het huis. De vlucht duurt # uur en # minuten. Hoe laat l | 1 |  | `G8-MEET-E06-claude-bank-031`: Een vliegtuig vertrekt om 7:15 uit het huis. De vlucht duurt 11 uur en 30 minuten. Hoe laat landt het? (Typ al… → **18:45** |
| 12 | 12 | Een vliegtuig vertrekt om #:# uit het huis. De vlucht duurt # uur en # minuten. Op de plek | 1 |  | `G8-MEET-E06-claude-bank-032`: Een vliegtuig vertrekt om 14:15 uit het huis. De vlucht duurt 11 uur en 15 minuten. Op de plek van aankomst is… → **20:30** |

### G8-MEET-E07 — 4 somtypes · 7 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een [wie] legt # km af in # uur. Hoeveel kilometer per uur is dat? | 4 |  | `G8-MEET-E07-claude-bank-001`: Een bus legt 150 km af in 2,5 uur. Hoeveel kilometer per uur is dat? → **60** |
| 2 | 2 | Een auto rijdt # uur met # km per uur. Hoeveel kilometer is dat? | 1 |  | `G8-MEET-E07-claude-bank-005`: Een auto rijdt 1,5 uur met 90 km per uur. Hoeveel kilometer is dat? → **135** |
| 3 | 3 | [wie] legt # km af in # uur. Hoeveel kilometer per uur is dat? | 1 |  | `G8-MEET-E07-claude-bank-006`: Een kind legt 30 km af in 1,5 uur. Hoeveel kilometer per uur is dat? → **20** |
| 4 | 4 | [wie] reist # uur met # km per uur. Hoeveel kilometer is dat? | 1 |  | `G8-MEET-E07-claude-bank-007`: Een kind reist 2,5 uur met 80 km per uur. Hoeveel kilometer is dat? → **200** |

### G8-MEET-V01 — 3 somtypes · 155 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 2 | [bouwsel] Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt? | 151 |  | `G8-MEET-V01-claude-bank-005`: Dit bouwwerk is helemaal vol. Hoeveel blokjes zijn er gebruikt? → **120** |
| 2 | 1 | Een weiland is # [ding]. Hoeveel m² is dat? | 3 |  | `G8-MEET-V01-claude-bank-001`: Een weiland is 2 hectare. Hoeveel m² is dat? → **20.000** |
| 3 | 3 | Een pak met # liter drinken wordt verdeeld over [bakken] van # [ding]. Hoeveel volle beker | 1 |  | `G8-MEET-V01-claude-bank-004`: Een pak met 1,5 liter drinken wordt verdeeld over bekers van 250 milliliter. Hoeveel volle bekers krijg je? → **6 bekers** |

### G8-VBN-E01 — 2 somtypes · 2 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een tabel laat zien hoeveel appels een boom geeft: jaar # [ding] # [ding], jaar # [ding] # | 1 |  | `G8-VBN-E01-claude-bank-001`: Een tabel laat zien hoeveel appels een boom geeft: jaar 1 geeft 40 appels, jaar 2 geeft 50 appels en jaar 3 ge… → **Ongeveer 70 appels** |
| 2 | 2 | Vijf kinderen sprongen ver. Dit zijn hun sprongen: # m · # m · # m · # m · # m. Wat is het | 1 |  | `G8-VBN-E01-claude-bank-002`: Vijf kinderen sprongen ver. Dit zijn hun sprongen: 2,1 m · 2,4 m · 2 m · 2,3 m · 2,2 m. Wat is het verschil tu… → **0,4 m** |

### G8-VBN-E03 — 5 somtypes · 12 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een spaartabel: week # → €#, week # → €#, week # → €#. Wat staat er bij week #? | 8 |  | `G8-VBN-E03-claude-bank-001`: Een spaartabel: week 0 → €58, week 1 → €83, week 2 → €108. Wat staat er bij week 4? → **158** |
| 2 | 2 | Je spaart voor ballen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na # w | 1 |  | `G8-VBN-E03-claude-bank-009`: Je spaart voor ballen. Je begint met €38 en legt elke week €15 erbij. Hoeveel heb je na 5 weken? → **113** |
| 3 | 3 | Je spaart voor een fiets. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na  | 1 |  | `G8-VBN-E03-claude-bank-010`: Je spaart voor een fiets. Je begint met €21 en legt elke week €25 erbij. Hoeveel heb je na 8 weken? → **221** |
| 4 | 4 | Je spaart voor stappen. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na #  | 1 |  | `G8-VBN-E03-claude-bank-011`: Je spaart voor stappen. Je begint met €12 en legt elke week €10 erbij. Hoeveel heb je na 8 weken? → **92** |
| 5 | 5 | Je spaart voor sterren. Je begint met €# en legt elke week €# [ding]. Hoeveel heb je na #  | 1 |  | `G8-VBN-E03-claude-bank-012`: Je spaart voor sterren. Je begint met €14 en legt elke week €15 erbij. Hoeveel heb je na 6 weken? → **104** |

### G8-VBN-E04 — 37 somtypes · 43 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en to | 3 |  | `G8-VBN-E04-claude-bank-032`: Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "15 … → **Dat kun je hier niet zien.** |
| 2 | 2 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" e | 2 |  | `G8-VBN-E04-claude-bank-025`: Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder s… → **Ja, dat klopt.** |
| 3 | 3 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont  | 2 |  | `G8-VBN-E04-claude-bank-027`: Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "12 kin… → **Dat kun je hier niet zien.** |
| 4 | 4 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont  | 2 |  | `G8-VBN-E04-claude-bank-030`: Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Meer d… → **Nee, dat klopt niet.** |
| 5 | 5 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [di | 2 |  | `G8-VBN-E04-claude-bank-037`: Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder s… → **Dat kun je hier niet zien.** |
| 6 | 6 | Bij de as van een grafiek staan de getallen #, #, #, # en # op gelijke afstand. Waarom is  | 1 |  | `G8-VBN-E04-claude-bank-001`: Bij de as van een grafiek staan de getallen 0, 10, 20, 100 en 200 op gelijke afstand. Waarom is deze grafiek m… → **De stapjes op de as zijn niet gelijk.** |
| 7 | 7 | Bij de as van een grafiek staat: aantal bezoekers (x #). De staaf van zaterdag stopt bij # | 1 |  | `G8-VBN-E04-claude-bank-002`: Bij de as van een grafiek staat: aantal bezoekers (x 1000). De staaf van zaterdag stopt bij 4. Hoeveel bezoeke… → **4000 bezoekers** |
| 8 | 8 | Bij de as van een staafdiagram staan alleen de getallen #, #, #, # en #. De staaf van woen | 1 |  | `G8-VBN-E04-claude-bank-003`: Bij de as van een staafdiagram staan alleen de getallen 0, 5, 10, 15 en 20. De staaf van woensdag stopt precie… → **Ongeveer 12 of 13** |
| 9 | 9 | Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van # naar | 1 |  | `G8-VBN-E04-claude-bank-004`: Boven een staafdiagram staat: Het aantal bezoekers is verdubbeld. De staaf gaat van 20 naar 24. Klopt die kop? → **Nee, 24 is geen dubbel van 20.** |
| 10 | 10 | De verkoop van sap is verdubbeld. In de grafiek staat een flesje dat twee keer zo hoog én  | 1 |  | `G8-VBN-E04-claude-bank-005`: De verkoop van sap is verdubbeld. In de grafiek staat een flesje dat twee keer zo hoog én twee keer zo breed i… → **Het flesje lijkt vier keer zo groot.** |
| 11 | 11 | Een cirkeldiagram is schuin getekend, alsof het een taart met dikte is. Het voorste stuk i | 1 |  | `G8-VBN-E04-claude-bank-006`: Een cirkeldiagram is schuin getekend, alsof het een taart met dikte is. Het voorste stuk is 25%, net als het a… → **Het voorste stuk lijkt groter dan het is.** |
| 12 | 12 | Een grafiek laat twee staven zien, maar bij de as staan helemaal geen getallen. Waarom is  | 1 |  | `G8-VBN-E04-claude-bank-007`: Een grafiek laat twee staven zien, maar bij de as staan helemaal geen getallen. Waarom is dat lastig? → **Je weet niet hoeveel de staven zijn.** |
| 13 | 13 | Een grafiek laat zien dat in warme maanden meer ijsjes worden verkocht en ook meer mensen  | 1 |  | `G8-VBN-E04-claude-bank-008`: Een grafiek laat zien dat in warme maanden meer ijsjes worden verkocht en ook meer mensen zwemmen. Iemand zegt… → **Nee, het komt allebei door de warmte.** |
| 14 | 35 | Een klas telt # [ding]. In een staafdiagram over huisdieren zijn de staven samen # [ding]. | 1 |  | `G8-VBN-E04-claude-bank-041`: Een klas telt 25 kinderen. In een staafdiagram over huisdieren zijn de staven samen 30 hoog. Wat is hiervoor d… → **Sommige kinderen hebben meer dan één huisdier** |
| 15 | 14 | Een winkel laat een grafiek van de verkoop zien, maar toont alleen de drie beste maanden v | 1 |  | `G8-VBN-E04-claude-bank-009`: Een winkel laat een grafiek van de verkoop zien, maar toont alleen de drie beste maanden van het jaar. Waarom … → **De slechte maanden zie je niet.** |
| 16 | 15 | In een cirkeldiagram over lievelingsfruit staan de stukken #%, #% en #%. Wat klopt hier ni | 1 |  | `G8-VBN-E04-claude-bank-010`: In een cirkeldiagram over lievelingsfruit staan de stukken 50%, 40% en 30%. Wat klopt hier niet? → **Samen is het meer dan 100%.** |
| 17 | 16 | In een grafiek staat onderaan de as het getal # en bovenaan het getal #. De lijn loopt naa | 1 |  | `G8-VBN-E04-claude-bank-011`: In een grafiek staat onderaan de as het getal 100 en bovenaan het getal 0. De lijn loopt naar beneden. Wat bet… → **Het aantal wordt juist groter.** |
| 18 | 17 | In een grafiek stopt de staaf van maandag bij # en de staaf van dinsdag bij #. Hoeveel mee | 1 |  | `G8-VBN-E04-claude-bank-012`: In een grafiek stopt de staaf van maandag bij 96 en de staaf van dinsdag bij 100. Hoeveel meer waren het er op… → **4 meer** |
| 19 | 18 | In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei # [d | 1 |  | `G8-VBN-E04-claude-bank-013`: In een grafiek zijn alle getallen afgerond op honderdtallen. Twee staven zijn allebei 300 hoog. Wat weet je ze… → **De echte aantallen kunnen verschillen.** |
| 20 | 19 | In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Be | 1 |  | `G8-VBN-E04-claude-bank-014`: In een plaatjesgrafiek staat bij appels een klein appeltje en bij peren een grote peer. Beide plaatjes staan v… → **Het grote plaatje lijkt veel meer stuks.** |
| 21 | 20 | In een plaatjesgrafiek staat een fietsje voor # [ding]. Bij groep # [ding] # [ding]. Hoeve | 1 |  | `G8-VBN-E04-claude-bank-015`: In een plaatjesgrafiek staat een fietsje voor 10 kinderen. Bij groep 8 staan 6 fietsjes. Hoeveel kinderen zijn… → **60 kinderen** |
| 22 | 21 | In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en | 1 |  | `G8-VBN-E04-claude-bank-016`: In een plaatjesgrafiek staat één hondje voor 4 honden. Bij het asiel staan 3 hele hondjes en 1 half hondje. Ho… → **14 honden** |
| 23 | 22 | In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel bred | 1 |  | `G8-VBN-E04-claude-bank-017`: In een staafdiagram is de staaf van zwemmen net zo hoog als die van turnen, maar veel breder getekend. Waarom … → **De brede staaf lijkt een groter aantal.** |
| 24 | 23 | In een staafdiagram over het aantal gelezen boeken begint de as niet bij #, maar bij #. Wa | 1 |  | `G8-VBN-E04-claude-bank-018`: In een staafdiagram over het aantal gelezen boeken begint de as niet bij 0, maar bij 90. Waarom kan die grafie… → **De verschillen lijken groter dan ze zijn.** |
| 25 | 24 | In klas A kiest #% van de # [ding] voor voetbal. In klas B kiest #% van de # [ding] voor v | 1 |  | `G8-VBN-E04-claude-bank-019`: In klas A kiest 50% van de 20 kinderen voor voetbal. In klas B kiest 40% van de 40 kinderen voor voetbal. Welk… → **Klas B, want dat zijn 16 kinderen.** |
| 26 | 25 | Je ziet een cirkeldiagram met de stukken hond #%, kat #% en konijn #%. Hoeveel kinderen he | 1 |  | `G8-VBN-E04-claude-bank-020`: Je ziet een cirkeldiagram met de stukken hond 40%, kat 35% en konijn 25%. Hoeveel kinderen hebben een hond gek… → **Dat kun je niet zien.** |
| 27 | 26 | Op de onderste as van een lijngrafiek staan #, #, # en # op gelijke afstand van elkaar. Wa | 1 |  | `G8-VBN-E04-claude-bank-021`: Op de onderste as van een lijngrafiek staan 2010, 2011, 2012 en 2020 op gelijke afstand van elkaar. Waarom klo… → **Tussen 2012 en 2020 zitten veel meer jaren.** |
| 28 | 36 | Sanne vraagt alleen aan kinderen van de schaakclub wat hun favoriete spel is. Bijna iedere | 1 |  | `G8-VBN-E04-claude-bank-042`: Sanne vraagt alleen aan kinderen van de schaakclub wat hun favoriete spel is. Bijna iedereen zegt schaken. Wat… → **Zij vroeg het aan een eenzijdige groep** |
| 29 | 37 | Tim meet vijf keer zijn plant. # cm, # cm, # cm, # cm en # cm. Welke meting klopt waarschi | 1 |  | `G8-VBN-E04-claude-bank-043`: Tim meet vijf keer zijn plant. 10 cm, 12 cm, 13 cm, 15 cm en 60 cm. Welke meting klopt waarschijnlijk niet? → **60 cm** |
| 30 | 27 | Twee grafieken staan naast elkaar. Bij de ene loopt de as tot #, bij de andere tot #. Beid | 1 |  | `G8-VBN-E04-claude-bank-022`: Twee grafieken staan naast elkaar. Bij de ene loopt de as tot 50, bij de andere tot 500. Beide lijnen lijken e… → **De stijging is niet even groot.** |
| 31 | 28 | Voor een onderzoek over het lievelingsvak zijn # [ding] uit één klas gevraagd. De kop zegt | 1 |  | `G8-VBN-E04-claude-bank-023`: Voor een onderzoek over het lievelingsvak zijn 5 kinderen uit één klas gevraagd. De kop zegt: de hele school k… → **Nee, 5 kinderen zijn te weinig.** |
| 32 | 29 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Hoe komen [wie] naar school?" e | 1 |  | `G8-VBN-E04-claude-bank-024`: Elk streepje is 10.
Dit staafdiagram heet "Hoe komen de kinderen naar school?" en toont percentages. Eronder s… → **Ja, dat klopt.** |
| 33 | 30 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Huisdieren in [plek]" en toont  | 1 |  | `G8-VBN-E04-claude-bank-029`: Elk streepje is 10.
Dit staafdiagram heet "Huisdieren in de klas" en toont percentages. Eronder staat: "Hond e… → **Nee, dat klopt niet.** |
| 34 | 31 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en to | 1 |  | `G8-VBN-E04-claude-bank-035`: Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "Rek… → **Ja, dat klopt.** |
| 35 | 32 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Lievelingsvak in groep #" en to | 1 |  | `G8-VBN-E04-claude-bank-036`: Elk streepje is 10.
Dit staafdiagram heet "Lievelingsvak in groep 8" en toont percentages. Eronder staat: "Tek… → **Nee, dat klopt niet.** |
| 36 | 33 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [di | 1 |  | `G8-VBN-E04-claude-bank-039`: Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder s… → **Nee, dat klopt niet.** |
| 37 | 34 | [staafdiagram] Elk streepje is #. ⏎ Dit staafdiagram heet "Wat drinken kinderen bij de [di | 1 |  | `G8-VBN-E04-claude-bank-040`: Elk streepje is 10.
Dit staafdiagram heet "Wat drinken kinderen bij de lunch?" en toont percentages. Eronder s… → **Ja, dat klopt.** |

### G8-VBN-V01 — 5 somtypes · 16 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | [vak(ken) aantikken op rooster] Zet de stip op (#, #). | 12 |  | `G8-VBN-V01-claude-bank-001`: Zet de stip op (6, 1). → **6,1** |
| 2 | 2 | In de lijngrafiek zie je de temperatuur op een dag, van # uur tot # uur. Wat gebeurt er me | 1 |  | `G8-VBN-V01-claude-bank-013`: In de lijngrafiek zie je de temperatuur op een dag, van 8.00 uur tot 16.00 uur. Wat gebeurt er met de temperat… → **De temperatuur daalt met 3 graden** |
| 3 | 3 | In een cirkeldiagram staat welke sport [wie] van een klas het liefst doen. De helft kiest  | 1 |  | `G8-VBN-V01-claude-bank-014`: In een cirkeldiagram staat welke sport de kinderen van een klas het liefst doen. De helft kiest voetbal, een k… → **12 kinderen** |
| 4 | 4 | In een grafiek loopt de as met stappen van #. De staaf van groep # [ding] precies tussen # | 1 |  | `G8-VBN-V01-claude-bank-015`: In een grafiek loopt de as met stappen van 20. De staaf van groep 7 staat precies tussen 60 en 80. Hoeveel is … → **70** |
| 5 | 5 | [staafdiagram] In het staafdiagram zie je hoeveel boeken er op [naam], [naam] en [naam] zi | 1 |  | `G8-VBN-V01-claude-bank-016`: In het staafdiagram zie je hoeveel boeken er op maandag, dinsdag en woensdag zijn geleend. Op welke dag zijn d… → **Woensdag** |

### G8-VERH-E01 — 1 somtypes · 1 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | In een bak zitten # [ding], # [ding] en # [ding] knikker. Welk deel van de knikkers is roo | 1 |  | `G8-VERH-E01-claude-bank-001`: In een bak zitten 6 rode, 3 blauwe en 1 groene knikker. Welk deel van de knikkers is rood? → **6 op de 10** |

### G8-VERH-E02 — 1 somtypes · 1 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | In een winkel kosten # [ding] sap samen €#. Hoeveel kosten # van die pakken sap? | 1 |  | `G8-VERH-E02-claude-bank-001`: In een winkel kosten 3 pakken sap samen €4,50. Hoeveel kosten 5 van die pakken sap? → **€7,50** |

### G8-VERH-E03 — 11 somtypes · 229 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | De schaal van een kaart is # : #. Twee steden liggen op de kaart # cm uit elkaar. Hoeveel  | 53 |  | `G8-VERH-E03-claude-bank-165`: De schaal van een kaart is 1 : 200.000. Twee steden liggen op de kaart 25 cm uit elkaar. Hoeveel km is dat in … → **50** |
| 2 | 2 | De schaal van een kaart is # : #. Twee dorpen liggen op de kaart # cm uit elkaar. Hoeveel  | 52 |  | `G8-VERH-E03-claude-bank-021`: De schaal van een kaart is 1 : 500.000. Twee dorpen liggen op de kaart 28 cm uit elkaar. Hoeveel km is dat in … → **140** |
| 3 | 3 | De schaal van een kaart is # : #. Twee plaatsen liggen op de kaart # cm uit elkaar. Hoevee | 52 |  | `G8-VERH-E03-claude-bank-093`: De schaal van een kaart is 1 : 500.000. Twee plaatsen liggen op de kaart 29 cm uit elkaar. Hoeveel km is dat i… → **145** |
| 4 | 4 | De schaal van een kaart is # : #. Twee dorpen liggen in het echt # km uit elkaar. Hoeveel  | 20 |  | `G8-VERH-E03-claude-bank-001`: De schaal van een kaart is 1 : 5.000.000. Twee dorpen liggen in het echt 1000 km uit elkaar. Hoeveel cm is dat… → **20** |
| 5 | 5 | De schaal van een kaart is # : #. Twee plaatsen liggen in het echt # km uit elkaar. Hoevee | 20 |  | `G8-VERH-E03-claude-bank-073`: De schaal van een kaart is 1 : 2.500.000. Twee plaatsen liggen in het echt 400 km uit elkaar. Hoeveel cm is da… → **16** |
| 6 | 6 | De schaal van een kaart is # : #. Twee steden liggen in het echt # km uit elkaar. Hoeveel  | 20 |  | `G8-VERH-E03-claude-bank-145`: De schaal van een kaart is 1 : 2.500.000. Twee steden liggen in het echt 425 km uit elkaar. Hoeveel cm is dat … → **17** |
| 7 | 7 | Op een kaart met schaal # : # is de afstand van [plek] naar [plek] # cm. Hoeveel meter is  | 8 |  | `G8-VERH-E03-claude-bank-219`: Op een kaart met schaal 1 : 10.000 is de afstand van het stadion naar de kleedkamer 8 cm. Hoeveel meter is dat… → **800** |
| 8 | 8 | Op een kaart met schaal # : # is [plek] # cm van [plek]. Hoeveel kilometer is dat in het e | 1 |  | `G8-VERH-E03-claude-bank-218`: Op een kaart met schaal 1 : 100.000 is het moeras 9 cm van het museum. Hoeveel kilometer is dat in het echt? → **9** |
| 9 | 9 | Op een kaart met schaal # : # is de afstand van de gymzaal naar de school # cm. Hoeveel me | 1 |  | `G8-VERH-E03-claude-bank-227`: Op een kaart met schaal 1 : 25.000 is de afstand van de gymzaal naar de school 2 cm. Hoeveel meter is dat in h… → **500** |
| 10 | 10 | Op een kaart met schaal # : # is de afstand van de klas naar het huis # cm. Hoeveel meter  | 1 |  | `G8-VERH-E03-claude-bank-228`: Op een kaart met schaal 1 : 100.000 is de afstand van de klas naar het huis 5 cm. Hoeveel meter is dat in het … → **5000** |
| 11 | 11 | Op een kaart met schaal # : # is de klas # cm van de school. Hoeveel kilometer is dat in h | 1 |  | `G8-VERH-E03-claude-bank-229`: Op een kaart met schaal 1 : 100.000 is de klas 9 cm van de school. Hoeveel kilometer is dat in het echt? → **9** |

### G8-VERH-E04 — 8 somtypes · 32 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een [ding] kost na #% korting €#. Wat was de prijs vóór de korting? | 14 |  | `G8-VERH-E04-claude-bank-006`: Een ei kost na 50% korting €30. Wat was de prijs vóór de korting? → **60** |
| 2 | 2 | [wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één  | 8 |  | `G8-VERH-E04-claude-bank-024`: Een speler zet €800 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt hij na één jaar? → **24** |
| 3 | 3 | Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één j | 4 |  | `G8-VERH-E04-claude-bank-002`: Daan zet €500 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt hij na één jaar? → **15** |
| 4 | 4 | Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één  | 2 |  | `G8-VERH-E04-claude-bank-021`: Fatima zet €800 op een spaarrekening met 3% rente per jaar. Hoeveel rente krijgt ze na één jaar? → **24** |
| 5 | 5 | Bram zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt hij na één j | 1 |  | `G8-VERH-E04-claude-bank-001`: Bram zet €1500 op een spaarrekening met 2% rente per jaar. Hoeveel rente krijgt hij na één jaar? → **30** |
| 6 | 6 | Een zak noten kost na #% korting €#. Wat was de prijs vóór de korting? | 1 |  | `G8-VERH-E04-claude-bank-020`: Een zak noten kost na 50% korting €75. Wat was de prijs vóór de korting? → **150** |
| 7 | 7 | Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel [ding] krijgt ze na één j | 1 |  | `G8-VERH-E04-claude-bank-023`: Sanne zet €400 op een spaarrekening met 1% rente per jaar. Hoeveel rente krijgt ze na één jaar? → **4** |
| 8 | 8 | Van de # [ding] op school komt # procent met de fiets. Hoeveel kinderen komen er met de fi | 1 |  | `G8-VERH-E04-claude-bank-032`: Van de 150 kinderen op school komt 60 procent met de fiets. Hoeveel kinderen komen er met de fiets? → **90 kinderen** |

### G8-VERH-E05 — 21 somtypes · 54 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Een [ding] kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen? | 15 |  | `G8-VERH-E05-claude-bank-004`: Een sticker kostte €80 en kost nu €120. Met hoeveel procent is de prijs gestegen? → **50** |
| 2 | 2 | [wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op d | 8 |  | `G8-VERH-E05-claude-bank-046`: Een kind zet €1000 op een spaarrekening met 1% rente per jaar. Hoeveel staat er na één jaar op de rekening? → **1010** |
| 3 | 3 | Vorig jaar waren er # [ding], nu #. Met hoeveel procent is dat gestegen? | 5 |  | `G8-VERH-E05-claude-bank-041`: Vorig jaar waren er 40 wortels, nu 44. Met hoeveel procent is dat gestegen? → **10** |
| 4 | 4 | Daan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de | 3 |  | `G8-VERH-E05-claude-bank-001`: Daan zet €400 op een spaarrekening met 2% rente per jaar. Hoeveel staat er na één jaar op de rekening? → **408** |
| 5 | 5 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de bal nu? | 2 |  | `G8-VERH-E05-claude-bank-019`: Een bal kostte €120. De prijs stijgt met 20%. Wat kost de bal nu? → **144** |
| 6 | 6 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knuffel nu? | 2 |  | `G8-VERH-E05-claude-bank-022`: Een knuffel kostte €40. De prijs stijgt met 5%. Wat kost de knuffel nu? → **42** |
| 7 | 7 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de steen nu? | 2 |  | `G8-VERH-E05-claude-bank-025`: Een knikker kostte €80. De prijs stijgt met 20%. Wat kost de steen nu? → **96** |
| 8 | 8 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het ei nu? | 2 |  | `G8-VERH-E05-claude-bank-031`: Een ei kostte €120. De prijs stijgt met 50%. Wat kost het ei nu? → **180** |
| 9 | 9 | Milan zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op d | 2 |  | `G8-VERH-E05-claude-bank-037`: Milan zet €300 op een spaarrekening met 3% rente per jaar. Hoeveel staat er na één jaar op de rekening? → **309** |
| 10 | 10 | Sanne zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op d | 2 |  | `G8-VERH-E05-claude-bank-039`: Sanne zet €1500 op een spaarrekening met 2% rente per jaar. Hoeveel staat er na één jaar op de rekening? → **1530** |
| 11 | 11 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de knoop nu? | 1 |  | `G8-VERH-E05-claude-bank-021`: Een schrift kostte €80. De prijs stijgt met 5%. Wat kost de knoop nu? → **84** |
| 12 | 12 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de stap nu? | 1 |  | `G8-VERH-E05-claude-bank-024`: Een bal kostte €40. De prijs stijgt met 5%. Wat kost de stap nu? → **42** |
| 13 | 13 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de sticker nu? | 1 |  | `G8-VERH-E05-claude-bank-027`: Een sticker kostte €80. De prijs stijgt met 25%. Wat kost de sticker nu? → **100** |
| 14 | 14 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de trui nu? | 1 |  | `G8-VERH-E05-claude-bank-028`: Een trui kostte €40. De prijs stijgt met 5%. Wat kost de trui nu? → **42** |
| 15 | 15 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost de wortel nu? | 1 |  | `G8-VERH-E05-claude-bank-029`: Een wortel kostte €120. De prijs stijgt met 25%. Wat kost de wortel nu? → **150** |
| 16 | 16 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het bot nu? | 1 |  | `G8-VERH-E05-claude-bank-030`: Een bot kostte €40. De prijs stijgt met 10%. Wat kost het bot nu? → **44** |
| 17 | 17 | Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het kaartje nu? | 1 |  | `G8-VERH-E05-claude-bank-033`: Een kaartje kostte €60. De prijs stijgt met 10%. Wat kost het kaartje nu? → **66** |
| 18 | 21 | Een winkel verkoopt in week # [ding] broden en in week # [ding] broden. Met hoeveel procen | 1 |  | `G8-VERH-E05-claude-bank-054`: Een winkel verkoopt in week 1 zeventig broden en in week 2 vijftig broden. Met hoeveel procent is de verkoop g… → **Ongeveer 29 procent** |
| 19 | 18 | Een zak noten kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen? | 1 |  | `G8-VERH-E05-claude-bank-034`: Een zak noten kostte €40 en kost nu €60. Met hoeveel procent is de prijs gestegen? → **50** |
| 20 | 19 | Een zak noten kostte €#. De prijs stijgt met #%. Wat kost de noot nu? | 1 |  | `G8-VERH-E05-claude-bank-035`: Een zak noten kostte €200. De prijs stijgt met 10%. Wat kost de noot nu? → **220** |
| 21 | 20 | Fatima zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op  | 1 |  | `G8-VERH-E05-claude-bank-036`: Fatima zet €2000 op een spaarrekening met 1% rente per jaar. Hoeveel staat er na één jaar op de rekening? → **2020** |

### G8-VERH-E06 — 3 somtypes · 104 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Schrijf # in procenten. | 96 |  | `G8-VERH-E06-claude-bank-002`: Schrijf 0,575 in procenten. → **57,5%** |
| 2 | 2 | Schrijf #/# in procenten. | 7 |  | `G8-VERH-E06-claude-bank-098`: Schrijf 21/40 in procenten. → **52,5%** |
| 3 | 3 | #% van de [ding] is kapot. Schrijf dat als kommagetal. | 1 |  | `G8-VERH-E06-claude-bank-001`: 12,5% van de vissen is kapot. Schrijf dat als kommagetal. → **0,125** |

### G8-VERH-V01 — 1 somtypes · 1 items

| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |
|---|---|---|---|---|---|
| 1 | 1 | Bij een enquête zeggen # van de # [ding] dat zij het liefst voetballen. Hoeveel procent va | 1 |  | `G8-VERH-V01-claude-bank-001`: Bij een enquête zeggen 40 van de 200 kinderen dat zij het liefst voetballen. Hoeveel procent van de kinderen i… → **20 procent** |

