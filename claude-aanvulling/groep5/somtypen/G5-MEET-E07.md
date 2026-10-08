# G5-MEET-E07 — Betalen met euro-komma

Onze omschrijving: Geld € met komma; wisselgeld tot €100 · in onze bank: 8 items

Claude-vragen gemapt: **302** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [geld] Hoeveel [ding] zie je?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[geld] Hoeveel [ding] zie je?” (koppeling: claudeId)
- Items: **182** · Claude-doelen: B4 (109), M8 (61), M5 (12) · regel: G5-B04-geld, G16-geld
- Getallenruimte: 0–100 euro (met komma) · type: meerkeuze
- Denkfouten (Claude): geld-verkeerd-geteld (185), kommagetal-als-geheel (92), getal-overgenomen (87)
- Verschillende Claude-fout-hints: 2 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op.”)
- Voorbeelden:
  - `G5-MEET-E07-claude-bank-029` (Claude B4, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [200, 100, 50, 20]}`
    - **Opties:** A) €2 · B) €4 · C) €3,70
    - **Antwoord:** €3,70  (controle: ok)
    - **Fout-hints (Claude):** €2 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op.
  - `G5-MEET-E07-claude-bank-129` (Claude M5, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [100, 100, 10]}`
    - **Opties:** A) €2,10 · B) €1 · C) €2
    - **Antwoord:** €2,10  (controle: ok)
    - **Fout-hints (Claude):** €1 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. · €2 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op.

- **Hint 1 (te schrijven):** Begin bij het geld dat het meest waard is.
- **Hint 2 (te schrijven):** Tel de rest er één voor één bij. Een euro is honderd cent.
- **Ouderzin:** Je kind telt munten en briefjes bij elkaar en kiest het bedrag.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te weinig geteld` (Claudes sleutel: geld-verkeerd-geteld) → Dat is te weinig. Leg het geld op volgorde van groot naar klein en tel het één voor één op.  [Claude, taalfix]
  - `euro en cent door elkaar` (Claudes sleutel: kommagetal-als-geheel) → Dat is te veel. Kijk goed naar elke munt: is het een munt van cent of van euro? Honderd cent is één euro.  [Claude, taalfix]
  - `aantal stuks geld (3)` (€3) → Je hebt geteld hoeveel stukken geld er zijn. De vraag is hoeveel geld het samen is. Kijk wat elk stuk waard is.  [nieuw]
  - `aantal stuks geld (4)` (€4) → Je hebt geteld hoeveel stukken geld er zijn. De vraag is hoeveel geld het samen is. Kijk wat elk stuk waard is.  [nieuw]
  - `andere fout` (andere fout) → Leg het geld op volgorde van groot naar klein. Tel het één voor één bij elkaar. Een euro is honderd cent.  [nieuw]
- Status: hints klaar

## Somtype 2: [geld] Je hebt dit geld. Je koopt iets van €#. Hoeveel houd je over?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[geld] Je hebt dit geld. Je koopt iets van €#. Hoeveel houd je over?” (koppeling: claudeId)
- Items: **108** · Claude-doelen: B4 (108) · regel: G5-B04-geld
- Getallenruimte: 0–100 euro (met komma) · type: meerkeuze
- Denkfouten (Claude): geld-verkeerd-geteld (90), verkeerde-bewerking (63), kommagetal-als-geheel (63)
- Verschillende Claude-fout-hints: 3 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.”)
- Voorbeelden:
  - `G5-MEET-E07-claude-bank-237` (Claude B4, bank, niveau 3 → toepassen)
    - **Opgave:** Je hebt dit geld. Je koopt iets van €4. Hoeveel houd je over?
    - **Tekening:** `{"soort": "geld", "munten": [500, 50, 50]}`
    - **Opties:** A) €101 · B) €10 · C) €2
    - **Antwoord:** €2  (controle: ok)
    - **Fout-hints (Claude):** €10 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · €101 → Tel eerst al het geld. Is een munt cent of euro? Haal dan de prijs eraf.
  - `G5-MEET-E07-claude-bank-294` (Claude B4, bank, niveau 3 → toepassen)
    - **Opgave:** Je hebt dit geld. Je koopt iets van €6. Hoeveel houd je over?
    - **Tekening:** `{"soort": "geld", "munten": [500, 100, 100, 20]}`
    - **Opties:** A) €13,20 · B) €1,20 · C) €21
    - **Antwoord:** €1,20  (controle: ok)
    - **Fout-hints (Claude):** €13,20 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · €21 → Tel eerst al het geld. Is een munt cent of euro? Haal dan de prijs eraf.

- **Hint 1 (te schrijven):** Tel eerst al het geld. Begin bij het geld dat het meest waard is.
- **Hint 2 (te schrijven):** Tel al het geld, en haal de prijs ervan af. Een euro is honderd cent.
- **Ouderzin:** Je kind telt munten en briefjes en rekent uit hoeveel er overblijft na een aankoop.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `prijs erbij gedaan` (Claudes sleutel: verkeerde-bewerking) → Je hebt de prijs bij het geld opgeteld. Je koopt iets: dan gaat het geld eraf.  [Claude, taalfix]
  - `de prijs` (fout = de prijs) → Dat is de prijs. De vraag is hoeveel geld je overhoudt. Tel eerst al het geld. Haal dan de prijs eraf.  [nieuw]
  - `euro en cent door elkaar` (Claudes sleutel: kommagetal-als-geheel) → Dat is te veel. Kijk goed naar elke munt: is het een munt van cent of van euro? Honderd cent is één euro.  [Claude, taalfix]
  - `te weinig` (Claudes sleutel: geld-verkeerd-geteld) → Dat is te weinig. Heb je al het geld geteld? Leg het op volgorde van groot naar klein en tel het één voor één op. Haal dan de prijs eraf.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel eerst al het geld, van groot naar klein. Haal dan de prijs eraf. Een euro is honderd cent.  [nieuw]
- Status: hints klaar

## Somtype 3: Je koopt drie [ding]. Ze kosten €# en €# en €#. Je betaalt met €#. Hoeveel krijg je terug?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Je koopt drie [ding] van €#, €# en €#. Je betaalt met €#. Hoeveel krijg je terug?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B12 (8) · regel: G5-B04-geld
- Getallenruimte: 0–100 euro (met komma) · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), onthouden-vergeten (8), tiental-ernaast (7)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-MEET-E07-claude-bank-007` (Claude B12, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Je koopt drie pionnen. Ze kosten €1,15 en €0,90 en €1,25. Je betaalt met €5. Hoeveel krijg je terug?
    - **Antwoord:** €1,70  (controle: ok)
    - **Fout-hints (Claude):** €9,74 → €9,74 is wat het kost. De vraag is wat je terugkrijgt. · €1,26 → Vul aan tot de hele euro en tel dan de euro's tot het betaalde bedrag. · €0,16 → Tel de centen nog eens na.
    - **Uitleg (Claude):** Eerst optellen: 1,15 + 0,90 + 1,25 = 3,30. Dan aanvullen tot 5: 1,70.
  - `G5-MEET-E07-claude-bank-012` (Claude B12, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Je koopt drie zakken noten. Ze kosten €2,49 en €1,85 en €3,20. Je betaalt met €10. Hoeveel krijg je terug?
    - **Antwoord:** €2,46  (controle: ok)
    - **Fout-hints (Claude):** €7,56 → €7,56 is wat het kost. De vraag is wat je terugkrijgt. · €3,44 → Vul aan tot de hele euro en tel dan de euro's tot het betaalde bedrag. · €2,34 → Tel de centen nog eens na.
    - **Uitleg (Claude):** Eerst optellen: 2,49 + 1,85 + 3,20 = 7,54. Dan aanvullen tot 10: 2,46.

- **Hint 1 (te schrijven):** Tel eerst de drie prijzen bij elkaar op. Dan weet je wat het samen kost.
- **Hint 2 (te schrijven):** Vul aan van wat het samen kost tot het geld waarmee je betaalt: eerst tot de volgende hele euro. Ben je er dan nog niet? Tel dan de hele euro's erbij.
- **Ouderzin:** Je kind rekent uit hoeveel geld het terugkrijgt als het drie dingen koopt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `wat het kost` (Claudes sleutel: verkeerde-bewerking) → Dat is wat alles samen kost. De vraag is hoeveel je terugkrijgt. Haal het van het geld waarmee je betaalt af.  [Claude, taalfix]
  - `de prijs van één ding` (fout = de prijs) → Dat is de prijs van één ding. Tel eerst de drie prijzen bij elkaar op. Haal dat dan van het geld waarmee je betaalt af.  [nieuw]
  - `één euro te veel` (fout = antwoord + €1) → Dat is één euro te veel. Vul eerst aan tot de volgende hele euro. Ben je er dan nog niet? Tel dan de hele euro's erbij tot het geld waarmee je betaalt.  [nieuw]
  - `één euro te weinig` (fout = antwoord − €1) → Dat is één euro te weinig. Tel de hele euro's nog eens: van de hele euro tot het geld waarmee je betaalt.  [nieuw]
  - `tien cent te weinig` (fout = antwoord − 10 cent) → Bijna! Dat is tien cent te weinig. Tel de centen nog eens na.  [nieuw]
  - `tien cent te veel` (fout = antwoord + 10 cent) → Bijna! Dat is tien cent te veel. Tel de centen nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Tel eerst de prijzen bij elkaar op. Vul dan aan: eerst tot de volgende hele euro. Ben je er dan nog niet? Tel dan de hele euro's erbij tot het geld waarmee je betaalt.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Je koopt drie [ding] van €#, €# en €#. Je betaalt met €#. Hoeveel krijg je terug?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: Een [ding] kost €#. Je betaalt met €#. Hoeveel krijg je terug?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een [ding] kost €#. Je betaalt met €#. Hoeveel krijg je terug?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: B4 (4) · regel: G5-B04-geld
- Getallenruimte: 0–100 euro (met komma) · type: kale
- Denkfouten (Claude): onthouden-vergeten (4), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk of je bij het aanvullen tot de hele euro al een euro hebt gebruikt. Die tel je niet dubbel.”)
- Voorbeelden:
  - `G5-MEET-E07-claude-bank-003` (Claude B4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een schrift kost €2,35. Je betaalt met €5. Hoeveel krijg je terug?
    - **Antwoord:** €2,65  (controle: ok)
    - **Fout-hints (Claude):** €9,60 → Kijk of je bij het aanvullen tot de hele euro al een euro hebt gebruikt. Die tel je niet dubbel. · €31,40 → Terugkrijgen is het verschil tussen wat je betaalt en wat het kost. Dat is aftrekken.
    - **Uitleg (Claude):** Vul aan tot het volgende hele bedrag. Van €2,35 naar €3 is 65 cent. Van €3 naar €5 is €2. Samen: €2,65.
  - `G5-MEET-E07-claude-bank-001` (Claude B4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een trui kost €14,95. Je betaalt met €20. Hoeveel krijg je terug?
    - **Antwoord:** €5,05  (controle: ok)
    - **Fout-hints (Claude):** €5,64 → Kijk of je bij het aanvullen tot de hele euro al een euro hebt gebruikt. Die tel je niet dubbel. · €35,36 → Terugkrijgen is het verschil tussen wat je betaalt en wat het kost. Dat is aftrekken.
    - **Uitleg (Claude):** Vul aan tot het volgende hele bedrag. Van €14,95 naar €15 is 5 cent. Van €15 naar €20 is €5. Samen: €5,05.

- **Hint 1 (te schrijven):** Hoeveel is het van de prijs tot de volgende hele euro? Begin daarmee.
- **Hint 2 (te schrijven):** Tel vanaf de prijs eerst tot de volgende hele euro. Tel daarna de hele euro's erbij tot het geld waarmee je betaalt.
- **Ouderzin:** Je kind rekent uit hoeveel geld het terugkrijgt bij één aankoop.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Claudes sleutel: verkeerde-bewerking) → Je hebt de prijs en het geld waarmee je betaalt bij elkaar opgeteld. Terugkrijgen is het verschil: haal de prijs van het geld af.  [Claude, taalfix]
  - `de prijs` (fout = de prijs) → Dat is de prijs. De vraag is hoeveel je terugkrijgt. Haal de prijs van het geld waarmee je betaalt af.  [nieuw]
  - `één euro te veel` (fout = antwoord + €1) → Dat is één euro te veel. Vul eerst aan tot de volgende hele euro. Ben je er dan nog niet? Tel dan de hele euro's erbij tot het geld waarmee je betaalt.  [nieuw]
  - `één euro te weinig` (fout = antwoord − €1) → Dat is één euro te weinig. Tel de hele euro's nog eens: van de hele euro tot het geld waarmee je betaalt.  [nieuw]
  - `tien cent te weinig` (fout = antwoord − 10 cent) → Bijna! Dat is tien cent te weinig. Tel de centen nog eens na.  [nieuw]
  - `tien cent te veel` (fout = antwoord + 10 cent) → Bijna! Dat is tien cent te veel. Tel de centen nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Vul aan van de prijs tot de volgende hele euro. Tel dan de hele euro's erbij tot het geld waarmee je betaalt.  [nieuw]
- Status: hints klaar
