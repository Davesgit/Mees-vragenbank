# G6-GET-M04 — Breuken schrijven: teller en noemer

Onze omschrijving: Breuken: notatie; teller/noemer; stam-/niet-stam-/samengesteld · in onze bank: 8 items

Claude-vragen gemapt: **50** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # #/# = ?/#. Welk getal hoort op het vraagteken?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# #/# = ?/#. Welk getal hoort op het vraagteken?” (koppeling: claudeId)
- Items: **14** · Claude-doelen: B10 (14) · regel: G6-B11-gemengd
- Getallenruimte: breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): teller-en-noemer-optellen (14), deel-vergeten-bij-splitsen (14)
- Verschillende Claude-fout-hints: 20 (meest: “Een hele is 8 8-de delen, niet 1. Vermenigvuldig eerst 3 × 8.”)
- Voorbeelden:
  - `G6-GET-M04-claude-bank-004` (Claude B10, gegenereerd, niveau 1 → basis)
    - **Opgave:** 1 2/4 = ?/4. Welk getal hoort op het vraagteken?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 3 → Een hele is 4 4-de delen, niet 1. Vermenigvuldig eerst 1 × 4. · 4 → Je hebt de 2/4 vergeten op te tellen.
    - **Uitleg (Claude):** 1 hele is 1 × 4 = 4 4-de delen. Plus 2: 6/4.
  - `G6-GET-M04-claude-bank-009` (Claude B10, gegenereerd, niveau 1 → basis)
    - **Opgave:** 1 4/8 = ?/8. Welk getal hoort op het vraagteken?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 5 → Een hele is 8 8-de delen, niet 1. Vermenigvuldig eerst 1 × 8. · 8 → Je hebt de 4/8 vergeten op te tellen.
    - **Uitleg (Claude):** 1 hele is 1 × 8 = 8 8-de delen. Plus 4: 12/8.

- **Hint 1 (te schrijven):** Eén hele bestaat uit zoveel gelijke stukken als de noemer (onder de streep) zegt. Hoeveel stukken zitten er in het hele getal?
- **Hint 2 (te schrijven):** Tel de stukken van de breuk daar nog bij. Dat getal komt boven de streep.
- **Ouderzin:** Je kind schrijft een gemengd getal als één breuk: het hele getal omzetten in stukken en de stukken van de breuk erbij tellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `heel en teller opgeteld` (fout = getal1 + getal2) → Heb je het hele getal en de teller opgeteld? Eén hele bestaat uit zoveel gelijke stukken als de noemer zegt.  [nieuw]
  - `teller niet erbij` (fout = antwoord − getal2) → Je hebt het hele getal omgezet in stukken. Tel de stukken van de breuk er nog bij.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de stukken nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de stukken nog eens na.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Je hebt een getal uit de vraag overgenomen. Is dat echt het getal dat op het vraagteken hoort? Hoeveel gelijke stukken zitten er in het hele getal? Tel daar de stukken van de breuk bij.  [nieuw]
  - `andere fout` (andere fout) → Doe het hele getal keer de noemer: zoveel gelijke stukken zitten er in het hele getal. Tel daar de teller bij.  [nieuw]
- Status: hints klaar

## Somtype 2: Je hebt #/# [ding]. Hoeveel hele pizza's zijn dat? Niet alle stukken passen in hele pizza's. Typ alleen het aantal hele pizza's.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Je hebt #/# [ding]. Hoeveel hele pizza's zijn dat? Er blijft ook nog een stuk over. Typ alleen het aantal hele pizza's.” (koppeling: claudeId)
- Items: **14** · Claude-doelen: B10 (14) · regel: G6-B11-gemengd
- Getallenruimte: breuken (noemer tot 2), breuken (noemer tot 3), breuken (noemer tot 4), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Denkfouten (Claude): rest-vergeten (14), verkeerde-bewerking (14)
- Verschillende Claude-fout-hints: 2 (meest: “Eén hele meer past niet: de teller is daarvoor niet groot genoeg.”)
- Voorbeelden:
  - `G6-GET-M04-claude-bank-034` (Claude B10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je hebt 15/4 pizza. Hoeveel hele pizza's zijn dat? Niet alle stukken passen in hele pizza's. Typ alleen het aantal hele pizza's.
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Eén hele meer past niet: de teller is daarvoor niet groot genoeg. · 11 → Hoe vaak past de noemer in de teller? Dat is delen, niet aftrekken.
    - **Uitleg (Claude):** 15 : 4 = 3 rest 3. Dus 15/4 = 3 3/4.
  - `G6-GET-M04-claude-bank-043` (Claude B10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je hebt 13/8 pizza. Hoeveel hele pizza's zijn dat? Niet alle stukken passen in hele pizza's. Typ alleen het aantal hele pizza's.
    - **Antwoord:** 1  (controle: ok)
    - **Fout-hints (Claude):** 2 → Eén hele meer past niet: de teller is daarvoor niet groot genoeg. · 5 → Hoe vaak past de noemer in de teller? Dat is delen, niet aftrekken.
    - **Uitleg (Claude):** 13 : 8 = 1 rest 5. Dus 13/8 = 1 5/8.

- **Hint 1 (te schrijven):** De noemer (onder de streep) zegt hoeveel gelijke stukken er in één hele pizza zitten.
- **Hint 2 (te schrijven):** Hoe vaak past de noemer in de teller (boven de streep)? Zoveel hele pizza's zijn het.
- **Ouderzin:** Je kind rekent uit hoeveel hele pizza's er in een breuk zitten die groter is dan één.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `noemer eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt de noemer van de teller afgehaald. Zo weet je hoeveel stukken er na één hele pizza nog zijn. Hoe vaak past de noemer in de teller?  [nieuw]
  - `de rest` (fout = de rest van getal1 : getal2) → Zijn dat de stukken die overblijven? De vraag is hoeveel hele pizza's het zijn. Hoe vaak past de noemer in de teller?  [nieuw]
  - `steeds een hele eraf` (fout = getal1 − j × getal2 (j ≥ 2)) → Heb je steeds een hele pizza van de stukken afgehaald? Ga door tot dat niet meer kan, en tel hoe vaak het lukte.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Dat is één hele pizza te veel. Zoveel stukken zijn er niet.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Dat is één hele pizza te weinig. De noemer past nog één keer meer in de teller.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Je hebt een getal uit de breuk overgenomen. Is dat echt het aantal hele pizza's? Hoe vaak past de noemer in de teller?  [nieuw]
  - `andere fout` (andere fout) → Hoe vaak past de noemer in de teller? Zoveel hele pizza's zijn het.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Je hebt #/# [ding]. Hoeveel hele pizza's zijn dat? Er blijft ook nog een stuk over. Typ alleen het aantal hele pizza's.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 3: Hoe heet de # in #/#?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoe heet de # in #/#?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: W2 (12) · regel: G6-W01-teller-noemer
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): teller-en-noemer-verwisseld (12), uitkomst-gekozen (12)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G6-GET-M04-claude-bank-023` (Claude W2, bank, niveau 1 → basis)
    - **Opgave:** Hoe heet de 2 in 2/6?
    - **Opties:** A) het deeltal · B) de noemer · C) de teller
    - **Antwoord:** de teller  (controle: ok)
    - **Fout-hints (Claude):** de noemer → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het deeltal → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G6-GET-M04-claude-bank-028` (Claude W2, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe heet de 4 in 4/9?
    - **Opties:** A) het deeltal · B) de noemer · C) de teller
    - **Antwoord:** de teller  (controle: ok)
    - **Fout-hints (Claude):** de noemer → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het deeltal → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Kijk waar het getal staat: boven de streep of onder de streep?
- **Hint 2 (te schrijven):** Het getal onder de streep zegt in hoeveel gelijke stukken het geheel is verdeeld. Het getal boven de streep zegt hoeveel van die stukken je neemt.
- **Ouderzin:** Je kind leert de namen van de getallen in een breuk: de teller staat boven de streep, de noemer eronder.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `teller gekozen` (de teller) → De teller staat boven de streep. Dit getal staat onder de streep.  [nieuw]
  - `noemer gekozen` (de noemer) → De noemer staat onder de streep. Dit getal staat boven de streep.  [nieuw]
  - `uitkomst gekozen` (de uitkomst) → De uitkomst krijg je pas als je iets uitrekent. Dit getal staat in de breuk zelf. Kijk waar het staat: boven of onder de streep? Hoe heet het getal op die plek?  [nieuw]
  - `andere fout` (andere fout) → Kijk waar het getal staat: boven de streep of onder de streep? Hoe heet het getal op die plek?  [nieuw]
- Status: hints klaar

## Somtype 4: [wie] snijden een [eten] in # gelijke stukken. [wie] eet er # op. Welk deel van de [eten] is dat? Typ een breuk, zoals #/#.

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[wie] delen een [eten] in # gelijke stukken. [wie] eet er # op. Welk deel is dat? Typ een breuk, zoals #/#.” (koppeling: claudeId)
- Items: **10** · Claude-doelen: B1 (10) · regel: G6-B02-notatie
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 5), breuken (noemer tot 8) · type: kale
- Uit de G5-park: 10 items
- Denkfouten (Claude): getallen-op-de-verkeerde-plek (20), verkeerde-bewerking (10)
- Verschillende Claude-fout-hints: 10 (meest: “Het getal onder de streep is het aantal stukken van het hele ding. Het getal erboven is wat je neemt.”)
- Voorbeelden:
  - `G6-GET-M04-claude-bank-050` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** De dino's snijden een pizza in 10 gelijke stukken. Een dino eet er 1 op. Welk deel van de pizza is dat? Typ een breuk, zoals 3/7.
    - **Antwoord:** 1/10  (controle: ok)
    - **Fout-hints (Claude):** 10/1 → Het getal onder de streep is het aantal stukken van het hele ding. Het getal erboven is wat je neemt. · 9/10 → Dat is het deel dat óverblijft. De vraag is welk deel de dino opeet. · 1/9 → Onder de streep komt het totale aantal stukken. 10, niet wat er overblijft.
    - **Uitleg (Claude):** De noemer (onder) zegt in hoeveel stukken het geheel is verdeeld: 10. De teller (boven) zegt hoeveel stukken je neemt: 1. Dus 1/10.
  - `G6-GET-M04-claude-bank-054` (Claude B1, gegenereerd, niveau 1 → basis)
    - **Opgave:** De kinderen snijden een taart in 8 gelijke stukken. Een kind eet er 1 op. Welk deel van de taart is dat? Typ een breuk, zoals 3/7.
    - **Antwoord:** 1/8  (controle: ok)
    - **Fout-hints (Claude):** 8/1 → Het getal onder de streep is het aantal stukken van het hele ding. Het getal erboven is wat je neemt. · 7/8 → Dat is het deel dat óverblijft. De vraag is welk deel het kind opeet. · 1/7 → Onder de streep komt het totale aantal stukken. 8, niet wat er overblijft.
    - **Uitleg (Claude):** De noemer (onder) zegt in hoeveel stukken het geheel is verdeeld: 8. De teller (boven) zegt hoeveel stukken je neemt: 1. Dus 1/8.

- **Hint 1 (te schrijven):** Een deel is een of meer gelijke stukken van het geheel. In hoeveel gelijke stukken is het geheel verdeeld? Dat getal komt onder de streep: de noemer.
- **Hint 2 (te schrijven):** Hoeveel stukken worden er opgegeten? Dat getal komt boven de streep: de teller.
- **Ouderzin:** Je kind schrijft als breuk welk deel er is opgegeten: de noemer is het aantal gelijke stukken, de teller het aantal opgegeten stukken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `wat overblijft` (Claudes sleutel: verkeerde-bewerking) → Dat zijn de stukken die overblijven. De vraag is hoeveel er is opgegeten: dat getal komt boven de streep.  [Claude, taalfix]
  - `getallen op de verkeerde plek` (Claudes sleutel: getallen-op-de-verkeerde-plek) → Staan de getallen op de goede plek? Onder de streep, bij de noemer, komt het aantal gelijke stukken van het geheel. Boven de streep, bij de teller, komt hoeveel stukken er zijn opgegeten.  [Claude, taalfix]
  - `andere fout` (andere fout) → Onder de streep komt het aantal gelijke stukken van het geheel. Boven de streep komt hoeveel stukken er zijn opgegeten.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor '[wie] delen een [eten] in # gelijke stukken. [wie] eet er # op. Welk deel is dat? Typ een breuk, zoals #/#.'. Nakijken of ze nog passen.
- Status: hints klaar
