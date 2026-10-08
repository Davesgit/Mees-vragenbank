# G7-DENK-03 — Stappenplannen bij rekenen

Onze omschrijving: Algoritmen · in onze bank: 8 items

Claude-vragen gemapt: **26** in **26** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Bij gym loop je # [ding] van # minuten en daarna rust je # minuten. Hoelang ben je in totaal bezig?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Bij gym loop je # [ding] van # minuten en daarna rust je # minuten. Hoelang ben je in totaal bezig?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “De rondjes heb je goed geteld. Er hoort nog een stap bij het plan.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-001` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Bij gym loop je 3 rondjes van 4 minuten en daarna rust je 5 minuten. Hoelang ben je in totaal bezig?
    - **Opties:** A) 12 minuten · B) 27 minuten · C) 17 minuten
    - **Antwoord:** 17 minuten  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 minuten → De rondjes heb je goed geteld. Er hoort nog een stap bij het plan. · 27 minuten → Lees nog eens hoe vaak je rust. Is dat na elk rondje of maar één keer?
    - **Uitleg (Claude):** 3 rondjes van 4 minuten zijn 12 minuten. Daar komt 5 minuten rust bij. Samen is dat 17 minuten.

- **Hint 1 (te schrijven):** Maak een plan in stappen. Hoelang duren alle rondjes samen?
- **Hint 2 (te schrijven):** Doe het aantal rondjes keer de tijd van één rondje. Tel de rusttijd er één keer bij op.
- **Ouderzin:** Je kind rekent een opgave in twee stappen uit: eerst een keersom, dan erbij.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `rust vergeten of alles opgeteld` (12 minuten) → Hoelang duren alle rondjes samen? Dat is het aantal rondjes keer de tijd van één rondje. Hoelang rust je, en tel je dat erbij?  [nieuw]
  - `rust na elk rondje` (27 minuten) → Rust je na elk rondje? Lees nog eens: je rust maar één keer, aan het eind.  [nieuw]
  - `andere fout` (andere fout) → Reken eerst de rondjes samen uit. Tel de rust er één keer bij op.  [nieuw]
- Status: hints klaar

## Somtype 2: Een recept voor # [ding] gebruikt # g meel. Stap #: je kookt voor # [ding]. Stap #: pas de hoeveelheid meel aan. Hoeveel meel heb je nodig?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een recept voor # [ding] gebruikt # g meel. Stap #: je kookt voor # [ding]. Stap #: pas de hoeveelheid meel aan. Hoeveel meel heb je nodig?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je kookt voor meer mensen dan in het recept staat. Heb je dan meer of minder meel nodig?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-002` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Een recept voor 4 personen gebruikt 300 g meel. Stap 1: je kookt voor 8 personen. Stap 2: pas de hoeveelheid meel aan. Hoeveel meel heb je nodig?
    - **Opties:** A) 600 g · B) 150 g · C) 302 g
    - **Antwoord:** 600 g  (controle: n.v.t.)
    - **Fout-hints (Claude):** 150 g → Je kookt voor meer mensen dan in het recept staat. Heb je dan meer of minder meel nodig? · 302 g → Je hebt er een klein getal bij opgeteld. Van 4 naar 8 personen is keer zoveel, niet plus zoveel.
    - **Uitleg (Claude):** 8 personen is 2 keer zoveel als 4 personen. Dus neem je ook 2 keer zoveel meel. 2 keer 300 g is 600 g.

- **Hint 1 (te schrijven):** Kook je voor meer of voor minder personen dan in het recept? Hoeveel keer zoveel personen is dat?
- **Hint 2 (te schrijven):** Deel het nieuwe aantal personen door het aantal uit het recept. De uitkomst zegt hoeveel keer zoveel meel je nodig hebt. Doe het meel uit het recept zoveel keer.
- **Ouderzin:** Je kind past een recept aan voor meer personen: keer zoveel personen is keer zoveel meel.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gedeeld` (150 g) → Heb je minder meel genomen? Je kookt voor meer personen, dus je hebt meer meel nodig.  [nieuw]
  - `opgeteld` (302 g) → Heb je er een klein getal bij opgeteld? Bij keer zoveel personen hoort keer zoveel meel, niet een paar gram erbij.  [nieuw]
  - `andere fout` (andere fout) → Hoeveel keer zoveel personen zijn het? Doe het meel ook zoveel keer.  [nieuw]
- Status: hints klaar

## Somtype 3: In [plek] staan # [ding] met elk # [ding]. Daarna haal je # [ding] weg. Hoeveel stoelen staan er nog?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In [plek] staan # [ding] met elk # [ding]. Daarna haal je # [ding] weg. Hoeveel stoelen staan er nog?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is het aantal na de eerste stap. Er moet nog iets weggehaald worden.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-003` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** In de klas staan 6 tafels met elk 4 stoelen. Daarna haal je 3 stoelen weg. Hoeveel stoelen staan er nog?
    - **Opties:** A) 21 stoelen · B) 24 stoelen · C) 7 stoelen
    - **Antwoord:** 21 stoelen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 24 stoelen → Dat is het aantal na de eerste stap. Er moet nog iets weggehaald worden. · 7 stoelen → Je hebt 6 en 4 opgeteld. Elke tafel heeft 4 stoelen, dus hoeveel keer 4 is dat?
    - **Uitleg (Claude):** 6 tafels met 4 stoelen zijn 6 keer 4, dus 24 stoelen. Daarvan haal je 3 stoelen weg. Er blijven 21 stoelen staan.

- **Hint 1 (te schrijven):** Maak een plan in stappen. Hoeveel stoelen staan er eerst in totaal?
- **Hint 2 (te schrijven):** Doe het aantal tafels keer het aantal stoelen aan één tafel. Haal de stoelen die je weghaalt van dat totaal af.
- **Ouderzin:** Je kind rekent een opgave in twee stappen uit: eerst een keersom, dan eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tweede stap vergeten` (24 stoelen) → Is dat het aantal na de eerste stap? Je haalt er daarna nog een paar weg.  [nieuw]
  - `opgeteld in plaats van keer` (7 stoelen) → Heb je het aantal tafels en het aantal stoelen aan één tafel opgeteld? Elke tafel heeft evenveel stoelen, dus alle stoelen samen is een keersom.  [nieuw]
  - `andere fout` (andere fout) → Reken eerst alle stoelen samen uit met een keersom. Haal de stoelen die je weghaalt daarna eraf.  [nieuw]
- Status: hints klaar

## Somtype 4: In een sportzaal staan # [ding] met elk # [ding]. Noor haalt er # [ding] uit. Hoeveel blijven er over?

- Sleutel: nrOrigineel **25** · somtypeOrigineel “In een sportzaal staan # [ding] met elk # [ding]. Noor haalt er # [ding] uit. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-G7-MEERSTAPS
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): deel-vergeten-bij-splitsen (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt alleen het totaal uitgerekend. Er gingen er nog een aantal uit.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-naar-001` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** In een sportzaal staan 7 dozen met elk 24 ballen. Noor haalt er 18 ballen uit. Hoeveel ballen blijven er over?
    - **Opties:** A) 31 ballen · B) 150 ballen · C) 168 ballen
    - **Antwoord:** 150 ballen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 168 ballen → Je hebt alleen het totaal uitgerekend. Er gingen er nog een aantal uit. · 31 ballen → Je hebt 7 en 24 opgeteld. Elke doos bevat 24 ballen.
    - **Uitleg (Claude):** 7 dozen met 24 ballen zijn 7 x 24 = 168 ballen. Daar gaan 18 ballen af: 168 − 18 = 150. Er blijven 150 ballen over.

- **Hint 1 (te schrijven):** Maak een plan in stappen. Hoeveel ballen zitten er eerst in alle dozen samen?
- **Hint 2 (te schrijven):** Doe het aantal dozen keer het aantal ballen in één doos. Haal de ballen die Noor eruit haalt van dat totaal af.
- **Ouderzin:** Je kind rekent een opgave in twee stappen uit: eerst een keersom, dan eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tweede stap vergeten` (168 ballen) → Is dat het aantal ballen in alle dozen samen? Noor haalt er nog een paar uit.  [nieuw]
  - `opgeteld in plaats van keer` (31 ballen) → Heb je het aantal dozen en het aantal ballen in één doos opgeteld? In elke doos zitten evenveel ballen. Hoeveel keer dat aantal is het?  [nieuw]
  - `andere fout` (andere fout) → Reken eerst alle ballen samen uit met een keersom. Haal de ballen van Noor daarna eraf.  [nieuw]
- Status: hints klaar

## Somtype 5: Je begint bij # en verdubbelt het getal # keer. Welk getal krijg je dan?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Je begint bij # en verdubbelt het getal # keer. Welk getal krijg je dan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): een-ernaast (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Schrijf het getal na elke verdubbeling op. Heb je echt 4 keer verdubbeld?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-004` (Claude W5, ai, niveau 3 → toepassen)
    - **Opgave:** Je begint bij 3 en verdubbelt het getal 4 keer. Welk getal krijg je dan?
    - **Opties:** A) 24 · B) 11 · C) 48
    - **Antwoord:** 48  (controle: n.v.t.)
    - **Fout-hints (Claude):** 24 → Schrijf het getal na elke verdubbeling op. Heb je echt 4 keer verdubbeld? · 11 → Verdubbelen is niet steeds er 2 bij optellen. Wat gebeurt er met een getal als het 2 keer zoveel wordt?
    - **Uitleg (Claude):** Je krijgt na elke stap 6, 12, 24 en 48. Dat zijn vier verdubbelingen. De uitkomst is 48.

- **Hint 1 (te schrijven):** Verdubbelen is keer twee. Schrijf na elke stap het nieuwe getal op.
- **Hint 2 (te schrijven):** Begin bij het getal uit de vraag en doe het keer twee. Doe de uitkomst weer keer twee. Houd met streepjes bij hoe vaak je verdubbelt, tot het aantal keer uit de vraag.
- **Ouderzin:** Je kind verdubbelt een getal een paar keer achter elkaar en houdt bij hoe vaak.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een keer te weinig` (8) → Heb je echt zo vaak verdubbeld als de vraag zegt? Schrijf na elke verdubbeling het getal op en tel de stappen.  [nieuw]
  - `steeds twee erbij` (9) → Heb je steeds twee erbij gedaan? Verdubbelen is keer twee: het getal wordt twee keer zo groot.  [nieuw]
  - `andere fout` (andere fout) → Verdubbelen is keer twee. Doe dat zo vaak als de vraag zegt.  [nieuw]
- Status: hints klaar

## Somtype 6: Je begint bij # op de getallenlijn en zet # [ding] van # [ding]. Bij welk getal kom je uit?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Je begint bij # op de getallenlijn en zet # [ding] van # [ding]. Bij welk getal kom je uit?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): een-ernaast (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Tel je stappen nog eens na. Hoeveel sprongen van 4 heb je precies gemaakt?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-005` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Je begint bij 0 op de getallenlijn en zet 5 stappen van 4 vooruit. Bij welk getal kom je uit?
    - **Opties:** A) 20 · B) 16 · C) 9
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 → Tel je stappen nog eens na. Hoeveel sprongen van 4 heb je precies gemaakt? · 9 → Je hebt 4 en 5 bij elkaar opgeteld. Elke stap is 4 groot, dus hoeveel keer 4 loop je?
    - **Uitleg (Claude):** Elke stap is 4 groot en je zet er 5. Dus 5 keer 4 is 20. Je komt uit bij 20.

- **Hint 1 (te schrijven):** Elke stap is even groot. Hoeveel stappen zet je, en hoe groot is één stap?
- **Hint 2 (te schrijven):** Doe het aantal stappen keer de grootte van één stap. Zo ver spring je. Tel dat op bij het getal waar je begint.
- **Ouderzin:** Je kind springt in gelijke stappen over de getallenlijn: het aantal stappen keer de grootte van één stap, vanaf het begingetal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een stap te weinig` (16) → Heb je alle stappen gezet? Tel je sprongen nog eens, vanaf het getal waar je begint. Tel bij elke sprong één.  [nieuw]
  - `opgeteld` (9) → Heb je het aantal stappen en de grootte van een stap opgeteld? Elke stap is even groot. Hoe vaak zet je zo'n stap?  [nieuw]
  - `andere fout` (andere fout) → Doe het aantal stappen keer de grootte van één stap. Tel dat op bij het getal waar je begint.  [nieuw]
- Status: hints klaar

## Somtype 7: Je geeft een plant # dagen water. Op dag # [ding] je # dl en elke volgende dag # dl meer. Hoeveel dl water geef je in totaal?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Je geeft een plant # dagen water. Op dag # [ding] je # dl en elke volgende dag # dl meer. Hoeveel dl water geef je in totaal?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Schrijf de vier dagen onder elkaar op. Heb je elke dag meegeteld?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-006` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je geeft een plant 4 dagen water. Op dag 1 geef je 2 dl en elke volgende dag 1 dl meer. Hoeveel dl water geef je in totaal?
    - **Opties:** A) 11 dl · B) 8 dl · C) 14 dl
    - **Antwoord:** 14 dl  (controle: n.v.t.)
    - **Fout-hints (Claude):** 11 dl → Schrijf de vier dagen onder elkaar op. Heb je elke dag meegeteld? · 8 dl → De hoeveelheid wordt elke dag groter. Je kunt dus niet 4 keer dezelfde hoeveelheid nemen.
    - **Uitleg (Claude):** De dagen zijn 2, 3, 4 en 5 dl. Die tel je allemaal bij elkaar op. Samen is dat 14 dl.

- **Hint 1 (te schrijven):** Schrijf voor elke dag op hoeveel water de plant krijgt.
- **Hint 2 (te schrijven):** Op de eerste dag krijgt de plant de hoeveelheid uit de vraag. Elke volgende dag doe je er de extra hoeveelheid bij. Schrijf alle dagen onder elkaar en tel ze bij elkaar op.
- **Ouderzin:** Je kind maakt een rijtje dat elke dag wat groter wordt, en telt het op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `meer dan dag één of dag vergeten` (11 dl) → Dat is te weinig. Heb je elke dag meegeteld, met de goede hoeveelheid? Elke volgende dag krijgt de plant meer dan de dag ervoor.  [nieuw]
  - `elke dag hetzelfde` (8 dl) → Krijgt de plant elke dag evenveel? Elke volgende dag krijgt hij meer. Schrijf de dagen onder elkaar.  [nieuw]
  - `andere fout` (andere fout) → Schrijf alle dagen onder elkaar, met elke dag wat meer. Tel alle dagen bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 8: Je hebt # [ding] sap van elk # dl. Stap #: giet alles in een kan. Stap #: giet er # dl uit. Hoeveel dl zit er nog in de kan?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Je hebt # [ding] sap van elk # liter. Stap #: giet alles in een kan. Stap #: giet er # liter uit. Hoeveel liter zit er nog in de kan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Na stap 1 zit dat erin. Maar stap 2 moet je ook nog uitvoeren.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-007` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 3 flesjes sap van elk 3 dl. Stap 1: giet alles in een kan. Stap 2: giet er 2 dl uit. Hoeveel dl zit er nog in de kan?
    - **Opties:** A) 4 dl · B) 7 dl · C) 9 dl
    - **Antwoord:** 7 dl  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 dl → Na stap 1 zit dat erin. Maar stap 2 moet je ook nog uitvoeren. · 4 dl → Je hebt 3 en 3 opgeteld. Elk flesje heeft 3 dl, dus hoeveel keer 3 dl is dat?
    - **Uitleg (Claude):** 3 flesjes van 3 dl is 9 dl. Daar gaat 2 dl af. Er blijft 7 dl in de kan.

- **Hint 1 (te schrijven):** Volg de stappen. Hoeveel deciliter giet je bij stap één in de kan?
- **Hint 2 (te schrijven):** Doe het aantal flesjes keer de deciliters in één flesje: zoveel zit er na stap één in de kan. Haal bij stap twee de deciliters die je eruit giet eraf.
- **Ouderzin:** Je kind volgt een plan in twee stappen: eerst een keersom, dan eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stand na stap één` (9 dl) → Dat is wat er na stap één in de kan zit. Bij stap twee giet je er nog iets uit. Hoeveel blijft er dan in de kan?  [nieuw]
  - `opgeteld in plaats van keer` (4 dl) → Heb je het aantal flesjes en de deciliters van één flesje opgeteld? Elk flesje heeft evenveel sap, dus alle deciliters samen is een keersom.  [nieuw]
  - `andere fout` (andere fout) → Reken eerst uit hoeveel deciliter er in de kan zit. Haal daarna af wat je eruit giet.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Je hebt # [ding] sap van elk # liter. Stap #: giet alles in een kan. Stap #: giet er # liter uit. Hoeveel liter zit er nog in de kan?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 9: Je hebt # [ding] stroken. Je knipt elke strook in # stukken. Hoeveel stukken heb je dan?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Je hebt # [ding] stroken. Je knipt elke strook in # stukken. Hoeveel stukken heb je dan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt 2 bij 12 opgeteld. Elke strook wordt 2 stukken, dus hoeveel keer 2 krijg je?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-008` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Je hebt 12 papieren stroken. Je knipt elke strook in 2 stukken. Hoeveel stukken heb je dan?
    - **Opties:** A) 14 stukken · B) 6 stukken · C) 24 stukken
    - **Antwoord:** 24 stukken  (controle: ok)
    - **Fout-hints (Claude):** 14 stukken → Je hebt 2 bij 12 opgeteld. Elke strook wordt 2 stukken, dus hoeveel keer 2 krijg je? · 6 stukken → Door knippen krijg je meer stukken, niet minder. Kijk nog eens wat er met elke strook gebeurt.
    - **Uitleg (Claude):** Elke strook wordt 2 stukken. Bij 12 stroken doe je 12 keer 2. Dat zijn 24 stukken.

- **Hint 1 (te schrijven):** Elke strook wordt een paar stukken. Krijg je meer of minder stukken dan stroken?
- **Hint 2 (te schrijven):** Elke strook geeft hetzelfde aantal stukken. Doe het aantal stroken keer het aantal stukken per strook.
- **Ouderzin:** Je kind ziet dat knippen meer stukken geeft: een keersom.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (14 stukken) → Heb je het aantal stukken per strook erbij opgeteld? Elke strook wordt zoveel stukken. Hoe vaak gebeurt dat?  [nieuw]
  - `gedeeld` (6 stukken) → Heb je gedeeld? Door te knippen krijg je meer stukken, niet minder.  [nieuw]
  - `andere fout` (andere fout) → Doe het aantal stroken keer het aantal stukken per strook.  [nieuw]
- Status: hints klaar

## Somtype 10: Je hebt # [ding]. Stap #: geef # [ding] weg. Stap #: geef nog eens # [ding] weg. Hoeveel stickers heb je dan nog?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Je hebt # [ding]. Stap #: geef # [ding] weg. Stap #: geef nog eens # [ding] weg. Hoeveel stickers heb je dan nog?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Er staan twee stappen. Heb je de tweede stap ook echt uitgevoerd?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-009` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Je hebt 20 stickers. Stap 1: geef 4 stickers weg. Stap 2: geef nog eens 4 stickers weg. Hoeveel stickers heb je dan nog?
    - **Opties:** A) 16 stickers · B) 28 stickers · C) 12 stickers
    - **Antwoord:** 12 stickers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 stickers → Er staan twee stappen. Heb je de tweede stap ook echt uitgevoerd? · 28 stickers → Let goed op wat je met de stickers doet: je geeft ze weg. Worden het er dan meer of minder?
    - **Uitleg (Claude):** Van 20 haal je eerst 4 af, dan houd je 16 over. Daarna haal je er nog 4 af. Zo blijven er 12 stickers over.

- **Hint 1 (te schrijven):** Volg de stappen één voor één. Hoeveel heb je na stap één nog?
- **Hint 2 (te schrijven):** Haal bij stap één de stickers die je weggeeft van het begin af. Haal bij stap twee nog eens af wat je weggeeft.
- **Ouderzin:** Je kind volgt een plan in twee stappen en haalt twee keer iets af.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stand na stap één` (16 stickers) → Dat is wat je na stap één nog hebt. Bij stap twee geef je er nog een paar weg. Hoeveel houd je dan over?  [nieuw]
  - `erbij in plaats van eraf` (28 stickers) → Heb je de stickers die je weggeeft opgeteld? Weggeven is eraf halen: je houdt er minder over.  [nieuw]
  - `andere fout` (andere fout) → Haal bij elke stap af wat je weggeeft.  [nieuw]
- Status: hints klaar

## Somtype 11: Je hebt # euro gespaard. Stap #: je krijgt # euro zakgeld. Stap #: je koopt een schrift van # euro. Hoeveel euro heb je dan?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Je hebt # euro gespaard. Stap #: je krijgt # euro zakgeld. Stap #: je koopt een schrift van # euro. Hoeveel euro heb je dan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt stap 1 goed gedaan. Wat gebeurt er bij stap 2 met je geld?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-010` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt 8 euro gespaard. Stap 1: je krijgt 5 euro zakgeld. Stap 2: je koopt een schrift van 3 euro. Hoeveel euro heb je dan?
    - **Opties:** A) 16 euro · B) 10 euro · C) 13 euro
    - **Antwoord:** 10 euro  (controle: n.v.t.)
    - **Fout-hints (Claude):** 13 euro → Je hebt stap 1 goed gedaan. Wat gebeurt er bij stap 2 met je geld? · 16 euro → Als je een schrift koopt, gaat er geld af. Tel je dat er dan bij op?
    - **Uitleg (Claude):** 8 euro plus 5 euro is 13 euro. Daar gaat 3 euro af voor het schrift. Je houdt 10 euro over.

- **Hint 1 (te schrijven):** Volg de stappen één voor één. Hoeveel geld heb je na stap één?
- **Hint 2 (te schrijven):** Tel bij stap één het zakgeld op bij wat je gespaard had. Haal bij stap twee de prijs van het schrift ervan af.
- **Ouderzin:** Je kind volgt een plan in twee stappen: eerst erbij, dan eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tweede stap vergeten` (13) → Is dat wat je na stap één hebt? Bij stap twee koop je nog een schrift.  [nieuw]
  - `prijs erbij opgeteld` (17) → Heb je de prijs van het schrift erbij opgeteld? Als je iets koopt, heb je minder geld.  [nieuw]
  - `andere fout` (andere fout) → Tel het zakgeld erbij op en haal de prijs van wat je koopt eraf.  [nieuw]
- Status: hints klaar

## Somtype 12: Je loopt een route. # m rechtdoor, dan links # m en dan rechts # m. Hoeveel meter heb je in totaal gelopen?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “Je loopt een route. # m rechtdoor, dan links # m en dan rechts # m. Hoeveel meter heb je in totaal gelopen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), eenheid-verkeerd-omgerekend (1)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de route vanaf het begin. Heb je het eerste stuk ook meegeteld?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-011` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je loopt een route. 200 m rechtdoor, dan links 150 m en dan rechts 250 m. Hoeveel meter heb je in totaal gelopen?
    - **Opties:** A) 400 m · B) 6 km · C) 600 m
    - **Antwoord:** 600 m  (controle: n.v.t.)
    - **Fout-hints (Claude):** 400 m → Lees de route vanaf het begin. Heb je het eerste stuk ook meegeteld? · 6 km → Kijk nog eens naar de eenheid. Hoeveel meter zit er in 1 km?
    - **Uitleg (Claude):** Je telt alle stukken op: 200 m, 150 m en 250 m. Samen is dat 600 m. Alle drie de stappen horen erbij.

- **Hint 1 (te schrijven):** De route bestaat uit een paar stukken. Hoeveel meter is elk stuk?
- **Hint 2 (te schrijven):** Schrijf de meters van alle stukken onder elkaar, ook het eerste stuk rechtdoor. Tel ze bij elkaar op. Kijk tot slot of de eenheid klopt: meter of kilometer.
- **Ouderzin:** Je kind telt de stukken van een route bij elkaar op en let op de eenheid.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eerste stuk vergeten` (400 m) → Heb je alle stukken van de route meegeteld, ook het eerste stuk rechtdoor?  [nieuw]
  - `meter als kilometer` (6 km) → Klopt de eenheid? Een kilometer is duizend meter. Is de route echt zo lang?  [nieuw]
  - `andere fout` (andere fout) → Tel de meters van alle stukken van de route bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 13: Je rijgt een ketting volgens dit patroon. # [ding] kralen en # [ding] kraal. Je herhaalt het patroon # keer. Hoeveel [ding] zitten er in de ketting?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “Je rijgt een ketting volgens dit patroon. # [ding] kralen en # [ding] kraal. Je herhaalt het patroon # keer. Hoeveel [ding] zitten er in de ketting?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): getal-overgenomen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is één keer het patroon. Maar hoe vaak herhaal je het?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-012` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je rijgt een ketting volgens dit patroon. 2 rode kralen en 1 blauwe kraal. Je herhaalt het patroon 5 keer. Hoeveel kralen zitten er in de ketting?
    - **Opties:** A) 3 kralen · B) 10 kralen · C) 15 kralen
    - **Antwoord:** 15 kralen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3 kralen → Dat is één keer het patroon. Maar hoe vaak herhaal je het? · 10 kralen → Je hebt alleen de rode kralen geteld. De blauwe kralen horen er ook bij.
    - **Uitleg (Claude):** Eén patroon is 2 plus 1, dus 3 kralen. Je doet dat 5 keer, dus 5 keer 3. Dat zijn 15 kralen.

- **Hint 1 (te schrijven):** Hoeveel kralen zitten er in één keer het patroon?
- **Hint 2 (te schrijven):** Tel de kralen van één patroon: alle soorten kralen samen. Doe dat aantal keer het aantal keer dat je het patroon herhaalt.
- **Ouderzin:** Je kind rekent uit hoeveel kralen een ketting heeft als een patroon een paar keer terugkomt: eerst één patroon, dan keer.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één keer het patroon` (3 kralen) → Is dat één keer het patroon? Je herhaalt het patroon een paar keer.  [nieuw]
  - `één soort kraal` (10 kralen) → Heb je de andere kraal uit het patroon ook meegeteld? Elk patroon heeft twee soorten kralen.  [nieuw]
  - `andere fout` (andere fout) → Tel de kralen van één patroon en doe dat keer het aantal keer.  [nieuw]
- Status: hints klaar

## Somtype 14: Je staat op tree # van de trap. Stap #: ga # [ding] omhoog. Stap #: ga # [ding] omlaag. Op welke tree sta je dan?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “Je staat op tree # van de trap. Stap #: ga # [ding] omhoog. Stap #: ga # [ding] omlaag. Op welke tree sta je dan?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Na stap 1 sta je goed. Kijk nog eens naar stap 2: die moet je ook nog doen.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-013` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Je staat op tree 3 van de trap. Stap 1: ga 5 treden omhoog. Stap 2: ga 2 treden omlaag. Op welke tree sta je dan?
    - **Opties:** A) Tree 6 · B) Tree 8 · C) Tree 10
    - **Antwoord:** Tree 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** Tree 8 → Na stap 1 sta je goed. Kijk nog eens naar stap 2: die moet je ook nog doen. · Tree 10 → Omlaag gaan is niet erbij optellen. Wat doe je met het getal als je daalt?
    - **Uitleg (Claude):** Van tree 3 ga je 5 omhoog, dan sta je op tree 8. Daarna ga je 2 omlaag. Dan sta je op tree 6.

- **Hint 1 (te schrijven):** Volg de stappen één voor één. Op welke tree sta je na stap één?
- **Hint 2 (te schrijven):** Omhoog is erbij, omlaag is eraf. Tel bij stap één de treden omhoog op bij de tree waar je begint. Haal bij stap twee de treden omlaag eraf.
- **Ouderzin:** Je kind volgt twee stappen op een trap: omhoog is erbij, omlaag is eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `stand na stap één` (tree 8) → Waar sta je na stap één? Bij stap twee ga je nog een paar treden omlaag.  [nieuw]
  - `omlaag als omhoog` (tree 10) → Ga je bij stap twee omhoog of omlaag? Omlaag gaan is eraf, niet erbij.  [nieuw]
  - `andere fout` (andere fout) → Tel de treden omhoog erbij en haal de treden omlaag eraf.  [nieuw]
- Status: hints klaar

## Somtype 15: Je volgt deze stappen: neem #, verdubbel het getal en tel er # bij op. Welke uitkomst krijg je?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “Je volgt deze stappen: neem #, verdubbel het getal en tel er # bij op. Welke uitkomst krijg je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), None (1)
- Verschillende Claude-fout-hints: 2 (meest: “Verdubbelen is niet 2 erbij optellen. Wat gebeurt er met 6 als je het verdubbelt?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-014` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Je volgt deze stappen: neem 6, verdubbel het getal en tel er 3 bij op. Welke uitkomst krijg je?
    - **Opties:** A) 15 · B) 11 · C) 12
    - **Antwoord:** 15  (controle: n.v.t.)
    - **Fout-hints (Claude):** 11 → Verdubbelen is niet 2 erbij optellen. Wat gebeurt er met 6 als je het verdubbelt? · 12 → Je bent goed begonnen, maar lees de laatste stap nog eens. Heb je alle drie de stappen gedaan?
    - **Uitleg (Claude):** Eerst verdubbel je 6, dat is 12. Daarna tel je er 3 bij op. Zo kom je op 15.

- **Hint 1 (te schrijven):** Wat betekent verdubbelen? Doe de stappen één voor één.
- **Hint 2 (te schrijven):** Verdubbelen is keer twee: het getal wordt twee keer zo groot. Schrijf na elke stap het nieuwe getal op. Tel er bij de laatste stap het getal uit de vraag bij op.
- **Ouderzin:** Je kind volgt een rij stappen: eerst verdubbelen (keer twee), dan erbij.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `twee erbij in plaats van verdubbelen` (11) → Heb je twee erbij gedaan bij verdubbelen? Verdubbelen is keer twee: het getal wordt twee keer zo groot.  [nieuw]
  - `laatste stap vergeten` (12) → Is dat het getal na het verdubbelen? Er is nog een stap: er komt nog iets bij.  [nieuw]
  - `andere fout` (andere fout) → Verdubbel het getal en tel er het getal van de laatste stap bij op.  [nieuw]
- Status: hints klaar

## Somtype 16: Je vouwt een blad papier # keer dubbel. Na elke vouw wordt het aantal delen # keer zoveel. In hoeveel delen is het blad verdeeld?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Je vouwt een blad papier # keer dubbel. Na elke vouw wordt het aantal delen # keer zoveel. In hoeveel delen is het blad verdeeld?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt er steeds 2 bij opgeteld. Maar bij elke vouw wordt het aantal delen 2 keer zoveel.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-015` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Je vouwt een blad papier 3 keer dubbel. Na elke vouw wordt het aantal delen 2 keer zoveel. In hoeveel delen is het blad verdeeld?
    - **Opties:** A) 8 delen · B) 6 delen · C) 4 delen
    - **Antwoord:** 8 delen  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 delen → Je hebt er steeds 2 bij opgeteld. Maar bij elke vouw wordt het aantal delen 2 keer zoveel. · 4 delen → Tel je vouwen na. Hoeveel keer heb je het blad dubbelgevouwen?
    - **Uitleg (Claude):** Na 1 vouw zijn er 2 delen en na 2 vouwen 4 delen. Na de derde vouw is dat weer 2 keer zoveel. Dat zijn 8 delen.

- **Hint 1 (te schrijven):** Hoeveel delen heb je na één vouw? En na twee vouwen?
- **Hint 2 (te schrijven):** Begin met één heel blad. Bij elke vouw wordt het aantal delen twee keer zo groot. Schrijf na elke vouw het aantal delen op, tot je zo vaak gevouwen hebt als de vraag zegt.
- **Ouderzin:** Je kind ziet dat het aantal delen bij elke vouw verdubbelt, en houdt bij hoe vaak.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij of keer het aantal vouwen` (6 delen) → Wordt het aantal delen bij elke vouw twee keer zo groot? Schrijf na elke vouw op hoeveel delen er zijn.  [nieuw]
  - `een vouw te weinig` (4 delen) → Heb je zo vaak verdubbeld als je vouwt? Tel je vouwen na.  [nieuw]
  - `andere fout` (andere fout) → Verdubbel het aantal delen bij elke vouw, zo vaak als je vouwt.  [nieuw]
- Status: hints klaar

## Somtype 17: Op een wandeltocht van # km staan om de # meter bordjes, ook bij de start en de finish. Hoeveel bordjes staan er?

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Op een wandeltocht van # km staan om de # meter bordjes, ook bij de start en de finish. Hoeveel bordjes staan er?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-G7-MEERSTAPS
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): een-ernaast (1), eenheid-verkeerd-omgerekend (1)
- Verschillende Claude-fout-hints: 2 (meest: “Vergeet het bordje bij de start niet mee te tellen.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-naar-002` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Op een wandeltocht van 12 km staan om de 500 meter bordjes, ook bij de start en de finish. Hoeveel bordjes staan er?
    - **Opties:** A) 6 bordjes · B) 25 bordjes · C) 24 bordjes
    - **Antwoord:** 25 bordjes  (controle: n.v.t.)
    - **Fout-hints (Claude):** 24 bordjes → Vergeet het bordje bij de start niet mee te tellen. · 6 bordjes → Reken de 12 km eerst om naar meters voordat je deelt.
    - **Uitleg (Claude):** 12 km is 12.000 meter. 12.000 : 500 = 24 stukken. Met het bordje bij de start erbij zijn dat 25 bordjes.

- **Hint 1 (te schrijven):** Hoeveel meter is de hele tocht? Reken de kilometers om naar meter.
- **Hint 2 (te schrijven):** Een kilometer is duizend meter. Deel de lengte van de tocht in meter door de afstand tussen twee bordjes: zoveel stukken zijn er. Aan het begin van elk stuk staat een bordje, en bij de finish staat er nog één.
- **Ouderzin:** Je kind rekent kilometers om naar meter en telt bij bordjes langs een route ook het bordje bij de finish mee.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `start of finish vergeten` (24 bordjes) → Heb je het bordje bij de start én het bordje bij de finish meegeteld? Er is één bordje meer dan er stukken zijn.  [nieuw]
  - `niet omgerekend` (6 bordjes) → Hoeveel keer past de afstand tussen twee bordjes in de hele tocht? Reken de tocht eerst om naar meter.  [nieuw]
  - `andere fout` (andere fout) → Reken de tocht om naar meter, deel door de afstand tussen de bordjes en tel er één bordje bij.  [nieuw]
- Status: hints klaar

## Somtype 18: Recept. Stap #: pak # [ding]. Stap #: pers voor elk glas # [ding]. Hoeveel sinaasappels pers je?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “Recept: stap #, pak # [ding]. Stap #: pers voor elk glas # [ding]. Hoeveel sinaasappels pers je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt de getallen bij elkaar opgeteld. Elk glas krijgt 2 sinaasappels, dus hoeveel keer 2 heb je nodig?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-016` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Recept. Stap 1: pak 3 glazen. Stap 2: pers voor elk glas 2 sinaasappels. Hoeveel sinaasappels pers je?
    - **Opties:** A) 3 sinaasappels · B) 6 sinaasappels · C) 5 sinaasappels
    - **Antwoord:** 6 sinaasappels  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 sinaasappels → Je hebt de getallen bij elkaar opgeteld. Elk glas krijgt 2 sinaasappels, dus hoeveel keer 2 heb je nodig? · 3 sinaasappels → Je noemde het aantal glazen. Kijk nog eens hoeveel sinaasappels er in één glas gaan.
    - **Uitleg (Claude):** Elk glas heeft 2 sinaasappels nodig. Bij 3 glazen doe je 3 keer 2. Dat zijn 6 sinaasappels.

- **Hint 1 (te schrijven):** Hoeveel sinaasappels pers je voor één glas? En voor hoeveel glazen?
- **Hint 2 (te schrijven):** Voor elk glas pers je evenveel sinaasappels. Doe het aantal glazen keer het aantal sinaasappels voor één glas.
- **Ouderzin:** Je kind volgt een recept in twee stappen en ziet dat 'voor elk glas' een keersom is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen de glazen` (3 sinaasappels) → Is dat het aantal glazen? De vraag is hoeveel sinaasappels je perst.  [nieuw]
  - `opgeteld` (5 sinaasappels) → Heb je het aantal glazen en het aantal sinaasappels opgeteld? Voor elk glas pers je evenveel sinaasappels. Hoe vaak gebeurt dat?  [nieuw]
  - `andere fout` (andere fout) → Doe het aantal glazen keer het aantal sinaasappels voor één glas.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Recept: stap #, pak # [ding]. Stap #: pers voor elk glas # [ding]. Hoeveel sinaasappels pers je?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 19: Reeks A: neem #, doe keer # en tel er # bij op. Reeks B: neem #, tel er # bij op en doe keer #. Welke reeks geeft het grootste getal?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “Reeks A: neem #, doe keer # en tel er # bij op. Reeks B: neem #, tel er # bij op en doe keer #. Welke reeks geeft het grootste getal?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Reken beide reeksen helemaal uit. Vergelijk daarna de twee uitkomsten.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-017` (Claude W5, ai, niveau 3 → toepassen)
    - **Opgave:** Reeks A: neem 5, doe keer 4 en tel er 2 bij op. Reeks B: neem 5, tel er 2 bij op en doe keer 4. Welke reeks geeft het grootste getal?
    - **Opties:** A) Ze geven hetzelfde getal · B) Reeks B · C) Reeks A
    - **Antwoord:** Reeks B  (controle: n.v.t.)
    - **Fout-hints (Claude):** Reeks A → Reken beide reeksen helemaal uit. Vergelijk daarna de twee uitkomsten. · Ze geven hetzelfde getal → De volgorde van de stappen is anders. Werkt keer 4 dan wel op hetzelfde getal?
    - **Uitleg (Claude):** Reeks A geeft 20 plus 2, dus 22. Reeks B geeft 7 keer 4, dus 28. Reeks B geeft het grootste getal.

- **Hint 1 (te schrijven):** Reken elke reeks helemaal uit, stap voor stap. Welke uitkomst is groter?
- **Hint 2 (te schrijven):** Schrijf bij de eerste reeks na elke stap het getal op. Doe hetzelfde bij de tweede reeks. Vergelijk de twee uitkomsten.
- **Ouderzin:** Je kind rekent twee reeksen stappen uit en vergelijkt de uitkomsten; de volgorde van de stappen kan uitmaken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `volgorde maakt niet uit` (ze geven hetzelfde getal) → Maakt de volgorde hier niets uit? Reken beide reeksen uit en kijk of de uitkomsten echt gelijk zijn.  [nieuw]
  - `eerste reeks gekozen` (reeks a) → Heb je beide reeksen helemaal uitgerekend? Welke uitkomst is echt het grootst?  [nieuw]
  - `andere fout` (andere fout) → Reken beide reeksen stap voor stap uit en vergelijk de uitkomsten.  [nieuw]
- Status: hints klaar

## Somtype 20: Regel: is het getal even, deel het dan door #. Is het oneven, tel er dan # bij op. Je begint bij # en doet # [ding]. Welk getal krijg je?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Regel: is het getal even, deel het dan door #. Is het oneven, tel er dan # bij op. Je begint bij # en doet # [ding]. Welk getal krijg je?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): een-ernaast (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt de regel goed gebruikt. Tel na hoeveel stappen je al hebt gedaan.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-018` (Claude W5, ai, niveau 3 → toepassen)
    - **Opgave:** Regel: is het getal even, deel het dan door 2. Is het oneven, tel er dan 3 bij op. Je begint bij 10 en doet 3 stappen. Welk getal krijg je?
    - **Opties:** A) 19 · B) 4 · C) 8
    - **Antwoord:** 4  (controle: n.v.t.)
    - **Fout-hints (Claude):** 8 → Je hebt de regel goed gebruikt. Tel na hoeveel stappen je al hebt gedaan. · 19 → Kijk bij elk getal eerst of het even of oneven is. Bij een even getal geldt een andere regel.
    - **Uitleg (Claude):** 10 is even, dus wordt het 5. 5 is oneven, dus wordt het 8. 8 is even, dus wordt het 4.

- **Hint 1 (te schrijven):** Is het begingetal even of oneven? Welke regel hoort daarbij?
- **Hint 2 (te schrijven):** Kijk bij elke stap opnieuw of het getal even of oneven is, en gebruik de regel die daarbij hoort. Schrijf na elke stap het nieuwe getal op met een streepje erbij. Stop als je zoveel streepjes hebt als de vraag zegt.
- **Ouderzin:** Je kind past een regel een paar keer toe en kijkt bij elke stap opnieuw of het getal even of oneven is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `steeds dezelfde regel` (19) → Heb je bij elke stap gekeken of het getal even of oneven is? Bij een even getal hoort een andere regel.  [nieuw]
  - `een stap te weinig` (8) → Hoeveel stappen heb je gedaan? Tel ze na: de vraag noemt het aantal stappen.  [nieuw]
  - `andere fout` (andere fout) → Kijk bij elke stap of het getal even of oneven is, en doe precies zoveel stappen als de vraag zegt.  [nieuw]
- Status: hints klaar

## Somtype 21: Stap #: neem #. Stap #: haal er # af. Stap #: deel door #. Stap #: tel er # bij op. Iemand schreef na elke stap het getal op: #, #, #, #. Bij welke stap ging het mis?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Stappen: neem #, haal er # af, deel door # en tel er # bij op. Iemand schreef op. #, #, #, #. Bij welke stap ging het mis?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Reken stap 2 na. 30 min 6. Klopt het getal dat er staat?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-021` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Stap 1: neem 30. Stap 2: haal er 6 af. Stap 3: deel door 4. Stap 4: tel er 10 bij op. Iemand schreef na elke stap het getal op: 30, 24, 8, 18. Bij welke stap ging het mis?
    - **Opties:** A) Bij stap 3 · B) Bij stap 2 · C) Bij stap 4
    - **Antwoord:** Bij stap 3  (controle: n.v.t.)
    - **Fout-hints (Claude):** Bij stap 2 → Reken stap 2 na. 30 min 6. Klopt het getal dat er staat? · Bij stap 4 → Kijk of de stap ervoor al goed ging. Wat is 24 gedeeld door 4?
    - **Uitleg (Claude):** 30 min 6 is 24, dat klopt nog. Maar 24 gedeeld door 4 is 6 en niet 8. De fout zit dus in stap 3.

- **Hint 1 (te schrijven):** Reken de stappen zelf uit. Vergelijk na elke stap jouw getal met het opgeschreven getal.
- **Hint 2 (te schrijven):** Het begingetal nemen is de eerste stap. Schrijf jouw getallen onder de opgeschreven getallen. De eerste plek waar ze verschillen, is de stap waar het misging.
- **Ouderzin:** Je kind rekent een rij stappen na en zoekt de eerste stap waar het misging.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `goede stap gekozen of anders geteld` (bij stap 2) → Klopt het getal na het eraf halen? Reken het na. Let op: het begingetal nemen is de eerste stap.  [nieuw]
  - `laatste stap gekozen` (bij stap 4) → Ging het in de stap ervoor al goed? Reken elke stap na vanaf het begin.  [nieuw]
  - `andere fout` (andere fout) → Reken elke stap zelf uit en zoek de eerste stap waar het opgeschreven getal anders is.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Stappen: neem #, haal er # af, deel door # en tel er # bij op. Iemand schreef op. #, #, #, #. Bij welke stap ging het mis?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 22: Stappen: neem #, deel door #, tel er # bij op en doe keer #. Tim zegt dat de uitkomst # is. Klopt dat?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Stappen: neem #, deel door #, tel er # bij op en doe keer #. Tim zegt dat de uitkomst # is. Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (1), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Er zijn vier stappen. Heb je de stap met plus 5 ook gedaan?”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-019` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Stappen: neem 48, deel door 6, tel er 5 bij op en doe keer 2. Tim zegt dat de uitkomst 26 is. Klopt dat?
    - **Opties:** A) Nee, het moet 15 zijn · B) Ja, 26 klopt · C) Nee, het moet 16 zijn
    - **Antwoord:** Ja, 26 klopt  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, het moet 16 zijn → Er zijn vier stappen. Heb je de stap met plus 5 ook gedaan? · Nee, het moet 15 zijn → In de laatste stap staat keer 2. Dat is iets anders dan er 2 bij optellen.
    - **Uitleg (Claude):** 48 gedeeld door 6 is 8, plus 5 is 13. Daarna is 13 keer 2 is 26. Tim heeft het goed gedaan.

- **Hint 1 (te schrijven):** Reken de stappen zelf uit, één voor één. Wat krijg jij?
- **Hint 2 (te schrijven):** Schrijf na elke stap het getal op: na het delen, na het erbij tellen en na de keer-stap. Vergelijk jouw laatste getal met wat Tim zegt.
- **Ouderzin:** Je kind rekent een rij stappen na en controleert of een uitkomst klopt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer als plus` (nee, het moet 15 zijn) → Wat staat er in de laatste stap: keer of plus? Keer twee is iets anders dan twee erbij.  [nieuw]
  - `plus-stap vergeten` (nee, het moet 16 zijn) → Heb je alle stappen gedaan? Er is ook een stap waarin je iets erbij telt.  [nieuw]
  - `andere fout` (andere fout) → Reken alle stappen zelf uit, in de goede volgorde, en vergelijk met de uitkomst van Tim.  [nieuw]
- Status: hints klaar

## Somtype 23: Stappen: neem #, doe keer # en haal er # af. Lisa zegt dat de uitkomst # is. Klopt dat?

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Stappen: neem #, doe keer # en haal er # af. Lisa zegt dat de uitkomst # is. Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk nog eens naar stap 2. Daar staat keer 3, niet plus 3.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-020` (Claude W5, ai, niveau 1 → basis)
    - **Opgave:** Stappen: neem 9, doe keer 3 en haal er 7 af. Lisa zegt dat de uitkomst 20 is. Klopt dat?
    - **Opties:** A) Nee, het moet 34 zijn · B) Ja, 20 klopt · C) Nee, het moet 5 zijn
    - **Antwoord:** Ja, 20 klopt  (controle: n.v.t.)
    - **Fout-hints (Claude):** Nee, het moet 5 zijn → Kijk nog eens naar stap 2. Daar staat keer 3, niet plus 3. · Nee, het moet 34 zijn → Bij stap 3 haal je 7 af. Wordt de uitkomst dan groter of kleiner?
    - **Uitleg (Claude):** Eerst 9 keer 3, dat is 27. Daarna haal je er 7 af. Dat is 20, dus Lisa heeft gelijk.

- **Hint 1 (te schrijven):** Reken de stappen zelf uit. Wat krijg jij?
- **Hint 2 (te schrijven):** Schrijf na elke stap het getal op: na de keer-stap en na het eraf halen. Vergelijk jouw laatste getal met wat Lisa zegt.
- **Ouderzin:** Je kind rekent een rij stappen na en controleert of een uitkomst klopt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `erbij in plaats van eraf` (nee, het moet 34 zijn) → Wat doe je in de laatste stap: erbij of eraf? Als je iets eraf haalt, wordt het getal kleiner.  [nieuw]
  - `plus in plaats van keer` (nee, het moet 5 zijn) → Wat staat er in de tweede stap: keer of plus? Keer is iets anders dan erbij.  [nieuw]
  - `andere fout` (andere fout) → Doe de keer-stap en haal er het laatste getal af. Vergelijk met de uitkomst van Lisa.  [nieuw]
- Status: hints klaar

## Somtype 24: Verdeel # [ding] eerlijk over # [ding]. De knikkers die overblijven, leg je apart. Hoeveel [ding] liggen er apart?

- Sleutel: nrOrigineel **22** · somtypeOrigineel “Verdeel # [ding] eerlijk over # [ding]. De knikkers die overblijven, leg je apart. Hoeveel [ding] liggen er apart?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): andere-deel-genomen (1), rest-vergeten (1)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is het aantal in één zakje. De vraag gaat over de knikkers die niet meer passen.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-022` (Claude W5, ai, niveau 3 → toepassen)
    - **Opgave:** Verdeel 50 knikkers eerlijk over 8 zakjes. De knikkers die overblijven, leg je apart. Hoeveel knikkers liggen er apart?
    - **Opties:** A) 6 knikkers · B) Geen enkele · C) 2 knikkers
    - **Antwoord:** 2 knikkers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 knikkers → Dat is het aantal in één zakje. De vraag gaat over de knikkers die niet meer passen. · Geen enkele → Kijk of 50 precies in 8 gelijke groepen gaat. Blijft er echt niets over?
    - **Uitleg (Claude):** In elk zakje gaan 6 knikkers, want 8 keer 6 is 48. Van de 50 knikkers blijven er dan 2 over. Die leg je apart.

- **Hint 1 (te schrijven):** Hoeveel knikkers krijgt elk zakje als je eerlijk verdeelt? Blijft er iets over?
- **Hint 2 (te schrijven):** Zoek het grootste aantal dat in elk zakje kan, zonder dat je knikkers tekortkomt. Doe dat aantal keer het aantal zakjes. Haal die uitkomst van alle knikkers af: wat overblijft, ligt apart.
- **Ouderzin:** Je kind deelt met rest en kijkt hoeveel er overblijft.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `aantal per zakje` (6 knikkers) → Is dat het aantal in één zakje? De vraag is hoeveel knikkers er overblijven.  [nieuw]
  - `rest vergeten` (geen enkele) → Gaat het precies op? Doe het aantal per zakje keer het aantal zakjes en vergelijk met alle knikkers.  [nieuw]
  - `andere fout` (andere fout) → Verdeel eerlijk, kijk hoeveel er in de zakjes zitten en haal dat van alle knikkers af.  [nieuw]
- Status: hints klaar

## Somtype 25: Volg deze stappen: neem #, doe keer #, tel er # bij op en deel door #. Wat is de uitkomst?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “Volg deze stappen: neem #, doe keer #, tel er # bij op en deel door #. Wat is de uitkomst?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): None (2)
- Verschillende Claude-fout-hints: 2 (meest: “Je bent tot stap 3 goed gekomen. Er staat nog een vierde stap.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-023` (Claude W5, ai, niveau 2 → toepassen)
    - **Opgave:** Volg deze stappen: neem 7, doe keer 4, tel er 12 bij op en deel door 2. Wat is de uitkomst?
    - **Opties:** A) 26 · B) 20 · C) 40
    - **Antwoord:** 20  (controle: n.v.t.)
    - **Fout-hints (Claude):** 40 → Je bent tot stap 3 goed gekomen. Er staat nog een vierde stap. · 26 → Let op de volgorde van de stappen. Delen doe je pas nadat je hebt opgeteld.
    - **Uitleg (Claude):** 7 keer 4 is 28 en 12 erbij is 40. Daarna deel je 40 door 2. De uitkomst is 20.

- **Hint 1 (te schrijven):** Doe de stappen in de volgorde van de vraag. Welk getal heb je na elke stap?
- **Hint 2 (te schrijven):** Schrijf na elke stap het getal op: na de keer-stap, na de plus-stap en na de deel-stap. Doe de deel-stap als laatste, met het getal dat je na de plus-stap hebt.
- **Ouderzin:** Je kind volgt een rij van vier stappen precies in de goede volgorde.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `deel-stap niet op het getal na de plus-stap` (26) → Welk getal heb je na de plus-stap? Dat hele getal deel je in de laatste stap door twee.  [nieuw]
  - `laatste stap vergeten` (40) → Is dat het getal na de plus-stap? Er is nog een laatste stap: delen.  [nieuw]
  - `andere fout` (andere fout) → Doe alle stappen in de volgorde van de vraag, de deel-stap als laatste.  [nieuw]
- Status: hints klaar

## Somtype 26: Voor # [ding] gebruik je # g boter. Je wilt # [ding] bakken. Iemand zegt dat je dan # g boter nodig hebt. Klopt dat?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “Voor # [ding] gebruik je # g boter. Je wilt # [ding] bakken. Iemand zegt dat je dan # g boter nodig hebt. Klopt dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W5 (1) · regel: G7-W03-stappenplan
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 1 items
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk hoe vaak 6 in 18 past. Met 240 g bak je niet genoeg koekjes.”)
- Voorbeelden:
  - `G7-DENK-03-claude-bank-024` (Claude W5, ai, niveau 3 → toepassen)
    - **Opgave:** Voor 12 koekjes gebruik je 60 g boter. Je wilt 36 koekjes bakken. Iemand zegt dat je dan 120 g boter nodig hebt. Klopt dat?
    - **Opties:** A) Nee, het moet 180 g zijn · B) Ja, 120 g klopt · C) Nee, het moet 20 g zijn
    - **Antwoord:** Nee, het moet 180 g zijn  (controle: n.v.t.)
    - **Fout-hints (Claude):** Ja, 120 g klopt → Kijk hoe vaak 6 in 18 past. Met 240 g bak je niet genoeg koekjes. · Nee, het moet 20 g zijn → Je bakt meer koekjes dan in het recept staat. Heb je dan meer of minder boter nodig?
    - **Uitleg (Claude):** 36 koekjes is 3 keer zoveel als 12 koekjes. Dus neem je ook 3 keer 60 g boter. Dat is 180 g.

- **Hint 1 (te schrijven):** Je wilt meer koekjes bakken. Hoeveel keer zoveel koekjes zijn dat?
- **Hint 2 (te schrijven):** Deel het aantal koekjes dat je wilt bakken door het aantal koekjes uit de eerste zin. De uitkomst zegt hoeveel keer zoveel boter je nodig hebt. Reken het uit en vergelijk met wat iemand zegt.
- **Ouderzin:** Je kind vergroot een hoeveelheid: hoeveel keer zoveel koekjes, zoveel keer zoveel boter.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `bewering overgenomen` (ja, 240 g klopt) → Heb je het zelf nagerekend? Hoeveel keer past het aantal koekjes uit de eerste zin in het aantal dat je wilt bakken?  [nieuw]
  - `gedeeld in plaats van keer` (nee, het moet 40 g zijn) → Bak je meer of minder koekjes dan in de eerste zin? Heb je dan meer of minder boter nodig?  [nieuw]
  - `andere fout` (andere fout) → Reken uit hoeveel keer zoveel koekjes je bakt, en doe de boter ook zoveel keer.  [nieuw]
- Status: hints klaar
