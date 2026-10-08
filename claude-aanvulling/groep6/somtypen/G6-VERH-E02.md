# G6-VERH-E02 — Een breuk is een deel van iets

Onze omschrijving: Breuk = deel van hoeveelheid én van geheel · in onze bank: 8 items

Claude-vragen gemapt: **34** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [taart] [wie] eet #/# van een taart en een ander(e) [wie] eet #/#. Welk deel is samen op? Typ een breuk.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[taart] [wie] eet #/# van een taart en een ander(e) [wie] eet #/#. Welk deel is samen op? Typ een breuk.” (koppeling: claudeId)
- Items: **10** · Claude-doelen: B7 (10) · regel: D-VERHAAL-PLAATJE
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- **Visual: nodig — niet live zonder beeld** (10 items): taart (cirkel) in 10 gelijke stukken; 5 stukken in kleur 1 en 2 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 4 gelijke stukken; 1 stukken in kleur 1 en 1 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 4 gelijke stukken; 2 stukken in kleur 1 en 1 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 5 gelijke stukken; 1 stukken in kleur 1 en 1 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 5 gelijke stukken; 1 stukken in kleur 1 en 2 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 5 gelijke stukken; 2 stukken in kleur 1 en 2 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 6 gelijke stukken; 2 stukken in kleur 1 en 3 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 6 gelijke stukken; 3 stukken in kleur 1 en 1 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 8 gelijke stukken; 3 stukken in kleur 1 en 2 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05) · taart (cirkel) in 8 gelijke stukken; 5 stukken in kleur 1 en 1 stukken in kleur 2 (Didactiek: plaatje verplicht; zonder plaatje → G7-GET-05)
- Denkfouten (Claude): teller-en-noemer-optellen (20), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 12 (meest: “De noemer verandert niet: de taart blijft in evenveel stukken verdeeld. Tel alleen de tellers op.”)
- Voorbeelden:
  - `G6-VERH-E02-claude-bank-027` (Claude B7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind eet 1/4 van een taart en een ander kind eet 1/4. Welk deel is samen op? Typ een breuk.
    - **Tekening:** `{"soort": "taart", "delen": 4, "kleurdelen": [1, 1]}`
    - **Antwoord:** 2/4  (controle: ok)
    - **Fout-hints (Claude):** 2/8 → De noemer verandert niet: de taart blijft in evenveel stukken verdeeld. Tel alleen de tellers op. · 2/1 → Je hebt 2 stukken, maar van welke grootte? Zet 4 onder de streep.
    - **Uitleg (Claude):** De stukken zijn even groot (allebei 4-en), dus je telt alleen de stukken op. 1 + 1 = 2 stukken, en het blijven 4-en: 2/4.
  - `G6-VERH-E02-claude-bank-026` (Claude B7, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een kind eet 3/6 van een taart en een ander kind eet 1/6. Welk deel is samen op? Typ een breuk.
    - **Tekening:** `{"soort": "taart", "delen": 6, "kleurdelen": [3, 1]}`
    - **Antwoord:** 4/6  (controle: ok)
    - **Fout-hints (Claude):** 4/12 → De noemer verandert niet: de taart blijft in evenveel stukken verdeeld. Tel alleen de tellers op. · 4/1 → Je hebt 4 stukken, maar van welke grootte? Zet 6 onder de streep. · 2/6 → Samen op betekent optellen, niet aftrekken.
    - **Uitleg (Claude):** De stukken zijn even groot (allebei 6-en), dus je telt alleen de stukken op. 3 + 1 = 4 stukken, en het blijven 6-en: 4/6.

- **Hint 1 (te schrijven):** Een deel is een of meer gelijke stukken van het geheel. De taart is in gelijke stukken verdeeld. De noemer (onder de streep) zegt in hoeveel.
- **Hint 2 (te schrijven):** Tel de stukken van allebei bij elkaar op. Dat getal komt boven de streep, als teller. De noemer blijft hetzelfde.
- **Ouderzin:** Je kind telt twee breuken van een taart op die dezelfde noemer hebben.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het aantal stukken` (fout = de stukken samen met noemer één) → Dat is alleen het aantal stukken. Zo lijkt het alsof er hele taarten op zijn. Zet onder de streep in hoeveel gelijke stukken de taart verdeeld is.  [nieuw]
  - `noemer veranderd` (Claudes sleutel: teller-en-noemer-optellen) → De taart blijft in evenveel gelijke stukken verdeeld. Onder de streep blijft dus de noemer staan. Boven de streep komt hoeveel stukken er samen op zijn.  [Claude, taalfix]
  - `afgehaald` (Claudes sleutel: verkeerde-bewerking) → Je hebt de stukken van elkaar afgehaald. Samen op betekent dat je de stukken van allebei bij elkaar optelt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de stukken van allebei op en zet dat boven de streep. De noemer blijft hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 2: [balk] Kleur #/# van de balk.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[balk] Kleur #/# van de balk.” (koppeling: claudeId)
- Items: **9** · Claude-doelen: B1 (9) · regel: G6-B01-deel-geheel
- Getallenruimte: breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 6), breuken (noemer tot 8) · type: kale
- Uit de G5-park: 9 items
- Denkfouten (Claude): None (6)
- Verschillende Claude-fout-hints: 6 (meest: “Kleur 1 stuk, niet 2.”)
- Voorbeelden:
  - `G6-VERH-E02-claude-bank-008` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 1/3 van de balk.
    - **Tekening:** `{"soort": "balk", "delen": 3, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 2 → Kleur 1 stuk, niet 2.
    - **Uitleg (Claude):** De balk heeft 3 gelijke stukken. 1/3 betekent: 1 van die 3 stukken.
  - `G6-VERH-E02-claude-bank-011` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kleur 5/6 van de balk.
    - **Tekening:** `{"soort": "balk", "delen": 6, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 1 → Kleur 5 stukken, niet 1.
    - **Uitleg (Claude):** De balk heeft 6 gelijke stukken. 5/6 betekent: 5 van die 6 stukken.

- **Hint 1 (te schrijven):** De noemer (onder de streep) zegt in hoeveel gelijke stukken de balk verdeeld is. Die stukken staan er al.
- **Hint 2 (te schrijven):** De teller (boven de streep) zegt hoeveel gelijke stukken van de balk je kleurt.
- **Ouderzin:** Je kind kleurt een breuk van een balk die al in gelijke stukken verdeeld is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `wat overblijft` (fout = getal1 - getal2 of getal2 - getal1) → Zijn dat de stukken die niet gekleurd moeten worden? Kleur zoveel stukken als de teller zegt.  [nieuw]
  - `hele balk` (fout = getal2) → Je hebt de hele balk gekleurd. De noemer zegt in hoeveel stukken de balk verdeeld is. De teller zegt hoeveel je er kleurt.  [nieuw]
  - `één stuk te veel` (fout = antwoord + 1) → Je hebt één stuk te veel gekleurd. Kleur zoveel stukken als de teller zegt.  [nieuw]
  - `één stuk te weinig` (fout = antwoord − 1) → Je hebt één stuk te weinig gekleurd. Kleur zoveel stukken als de teller zegt.  [nieuw]
  - `andere fout` (andere fout) → Kleur zoveel stukken als de teller (boven de streep) zegt.  [nieuw]
- Status: hints klaar

## Somtype 3: [groepjes] Er zijn # [ding]. Kleur #/# van de koekjes.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[groepjes] Er zijn # [ding]. Kleur #/# van de koekjes.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B2 (8) · regel: G6-B04-deel-hoeveelheid
- Getallenruimte: breuken (noemer tot 3), breuken (noemer tot 6) · type: kale
- Uit de G5-park: 8 items
- Denkfouten (Claude): None (5)
- Verschillende Claude-fout-hints: 4 (meest: “2 is maar één deel. Je hebt 2 delen nodig.”)
- Voorbeelden:
  - `G6-VERH-E02-claude-bank-017` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Er zijn 18 koekjes. Kleur 1/6 van de koekjes.
    - **Tekening:** `{"soort": "groepjes", "aantal": 18, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Eerst 18 : 6 = 3, dat is één deel. Dan 1 delen: 1 × 3 = 3.
  - `G6-VERH-E02-claude-bank-013` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Er zijn 12 koekjes. Kleur 1/3 van de koekjes.
    - **Tekening:** `{"soort": "groepjes", "aantal": 12, "kleurbaar": true}`
    - **UI:** balk kleuren
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Eerst 12 : 3 = 4, dat is één deel. Dan 1 delen: 1 × 4 = 4.

- **Hint 1 (te schrijven):** Verdeel de koekjes eerst in zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel koekjes zitten er in één stuk?
- **Hint 2 (te schrijven):** In elk gelijk stuk zitten evenveel koekjes. Kleur zoveel van die stukken als de teller (boven de streep) zegt.
- **Ouderzin:** Je kind kleurt een breuk van een aantal koekjes. Eerst verdeelt het de koekjes in gelijke stukken (gedeeld door de noemer), dan kleurt het zoveel stukken als de teller zegt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alle koekjes` (fout = getal1) → Je hebt alle koekjes gekleurd. Kleur alleen zoveel gelijke stukken als de teller zegt. Verdeel de koekjes eerst in zoveel gelijke stukken als de noemer zegt.  [nieuw]
  - `één stuk` (Claudes sleutel (zonder label)) → Dat is één gelijk stuk. Hoeveel van die stukken zegt de teller? Kleur die allemaal.  [Claude, taalfix]
  - `teller als aantal` (fout = getal2) → Je hebt zoveel koekjes gekleurd als de teller zegt. De teller zegt hoeveel gelijke stukken je kleurt. Hoeveel koekjes zitten er in één stuk?  [nieuw]
  - `andere fout` (andere fout) → Verdeel de koekjes in zoveel gelijke stukken als de noemer zegt. Kleur dan zoveel stukken als de teller zegt.  [nieuw]
- Status: hints klaar

## Somtype 4: [schema] strook

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[schema] strook” (koppeling: claudeId)
- Items: **4** · Claude-doelen: W4 (4) · regel: G6-W04-schema-strook
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): deel-van-geheel-verkeerd (5), getal-overgenomen (2), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 8 (meest: “Kijk hoeveel groepjes van 4 hokjes er in de hele strook passen.”)
- Voorbeelden:
  - `G6-VERH-E02-claude-bank-023` (Claude W4, ai, niveau 1 → basis)
    - **Opgave:** Je hebt een strook van 16 hokjes. Je kleurt er 4 in. Welk deel van de strook is gekleurd?
    - **Opties:** A) de helft · B) een kwart · C) een zestiende
    - **Antwoord:** een kwart  (controle: n.v.t.)
    - **Fout-hints (Claude):** een zestiende → Kijk hoeveel groepjes van 4 hokjes er in de hele strook passen. · de helft → Bij de helft zou je precies 8 hokjes kleuren. Tel nog eens hoeveel je er echt kleurt.
    - **Uitleg (Claude):** De strook heeft 16 hokjes. Je kunt hem in 4 gelijke stukken van 4 hokjes verdelen. Jij kleurt 1 van die 4 stukken, dus een kwart.
  - `G6-VERH-E02-claude-bank-021` (Claude W4, ai, niveau 2 → toepassen)
    - **Opgave:** Je hebt een strook van 12 hokjes. Je kleurt er 3 in. Welk deel van de strook is gekleurd?
    - **Opties:** A) een kwart · B) een derde · C) drie hele stroken
    - **Antwoord:** een kwart  (controle: n.v.t.)
    - **Fout-hints (Claude):** Een derde → Kijk hoe vaak 3 hokjes in de hele strook van 12 passen. · Drie hele stroken → Je kleurt maar een stukje van één strook. Het antwoord is dus kleiner dan de hele strook.
    - **Uitleg (Claude):** De strook heeft 12 hokjes. In 12 passen 4 groepjes van 3. Dus 3 hokjes is een kwart van de strook.

- **Hint 1 (te schrijven):** De hele strook is het geheel. Een deel is een of meer gelijke stukken van het geheel.
- **Hint 2 (te schrijven):** Verdeel de strook in gelijke stukken. Hoeveel hokjes zitten er in één stuk, en hoeveel van die stukken horen bij de vraag?
- **Ouderzin:** Je kind gebruikt een strook met hokjes om een deel van een geheel te vinden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `hele stroken` (drie hele stroken) → Er is maar één strook. Je kleurt alleen een paar hokjes ervan, dus het antwoord is een deel van die ene strook.  [nieuw]
  - `verkeerd deel (een derde)` (een derde) → Hoe vaak passen de gekleurde hokjes in de hele strook? Zoveel gelijke stukken heeft het geheel, en één daarvan is gekleurd.  [nieuw]
  - `verkeerd deel (een zestiende)` (een zestiende) → Hoe vaak passen de gekleurde hokjes in de hele strook? Zoveel gelijke stukken heeft het geheel, en één daarvan is gekleurd.  [nieuw]
  - `de helft gekozen` (de helft) → Bij de helft zijn er evenveel gekleurde als niet-gekleurde hokjes. Hoe vaak passen de gekleurde hokjes in de hele strook? Zoveel gelijke stukken heeft het geheel, en één daarvan is gekleurd.  [nieuw]
  - `helft van de hokjes (twaalf)` (12 hokjes) → Dat is de helft van de strook. Een derde is minder dan de helft. Verdeel de strook in drie gelijke stukken. Hoeveel hokjes zitten er in één stuk?  [nieuw]
  - `helft van de hokjes (tien)` (10 hokjes) → Dat is de helft van de strook. Een kwart is minder dan de helft. Verdeel de strook in vier gelijke stukken. Hoeveel hokjes zitten er in één stuk?  [nieuw]
  - `aantal stukken (drie)` (3 hokjes) → Een derde betekent: verdeel de strook in drie gelijke stukken. Drie is het aantal stukken, niet het aantal hokjes. Hoeveel hokjes zitten er in één stuk?  [nieuw]
  - `aantal stukken (vier)` (4 hokjes) → Een kwart betekent: verdeel de strook in vier gelijke stukken. Vier is het aantal stukken, niet het aantal hokjes. Hoeveel hokjes zitten er in één stuk?  [nieuw]
  - `andere fout` (andere fout) → Verdeel de strook in gelijke stukken. Hoeveel hokjes zitten er in één stuk, en hoeveel van die stukken horen bij de vraag?  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] liggen # [ding]. #/# [ding] is groen. Hoeveel groene [ding] zijn er?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In [plek] liggen # [ding]. #/# [ding] is groen. Hoeveel groene [ding] zijn er?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: B2 (3) · regel: G6-B04-deel-hoeveelheid
- Getallenruimte: breuken (noemer tot 6) · type: kale
- Uit de G5-park: 3 items
- Denkfouten (Claude): omgekeerd-gedeeld (3), deel-vergeten-bij-splitsen (2), verkeerde-bewerking (1)
- Verschillende Claude-fout-hints: 4 (meest: “Deel door de noemer (6), niet door de teller.”)
- Voorbeelden:
  - `G6-VERH-E02-claude-bank-001` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de camping staan 354 tenten. 1/6 ervan is nieuw. Hoeveel nieuwe tenten zijn er?
    - **Antwoord:** 59  (controle: ok)
    - **Fout-hints (Claude):** 295 → Dat is het deel dat níét groen is. Lees de vraag nog eens. · 354 → Deel door de noemer (6), niet door de teller.
    - **Uitleg (Claude):** Eerst 1/6: 354 : 6 = 59. Dan 1 keer: 1 × 59 = 59.
  - `G6-VERH-E02-claude-bank-003` (Claude B2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In een doos zitten 312 knikkers. 5/6 ervan is van glas. Hoeveel knikkers zijn van glas?
    - **Antwoord:** 260  (controle: ok)
    - **Fout-hints (Claude):** 52 → 52 is 1/6. Je hebt 5 van die delen nodig. · 62.4 → Deel door de noemer (6), niet door de teller.
    - **Uitleg (Claude):** Eerst 1/6: 312 : 6 = 52. Dan 5 keer: 5 × 52 = 260.

- **Hint 1 (te schrijven):** Verdeel alles eerst in zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel is één stuk?
- **Hint 2 (te schrijven):** Eén gelijk stuk is het hele aantal gedeeld door de noemer. Neem zoveel van die stukken als de teller (boven de streep) zegt. Hoeveel is dat samen?
- **Ouderzin:** Je kind rekent een breuk van een aantal uit. Eerst één gelijk stuk (gedeeld door de noemer), dan keer de teller.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alles` (fout = getal1) → Dat is het hele aantal. De vraag gaat alleen over zoveel gelijke stukken als de teller zegt. Deel eerst door de noemer.  [nieuw]
  - `één stuk` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is één gelijk stuk. Hoeveel van die stukken zegt de teller? Hoeveel is dat samen?  [Claude, taalfix]
  - `door de teller gedeeld` (Claudes sleutel: omgekeerd-gedeeld) → Je hebt gedeeld door de teller. Deel door de noemer, dan heb je één gelijk stuk. Doe dat daarna keer de teller.  [Claude, taalfix]
  - `wat overblijft` (Claudes sleutel: verkeerde-bewerking) → Is dat wat er overblijft? Je zoekt zoveel gelijke stukken als de teller zegt.  [Claude, taalfix]
  - `andere fout` (andere fout) → Deel eerst door de noemer. Dat is één gelijk stuk. Doe dat keer de teller.  [nieuw]
- Status: hints klaar
