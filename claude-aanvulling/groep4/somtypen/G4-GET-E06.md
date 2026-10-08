# G4-GET-E06 — Verhaaltjes met keer

Onze omschrijving: × ↔ context ≤100; strategieën (herhaald +, verwisselen, verdubbelen) · in onze bank: 8 items

Claude-vragen gemapt: **123** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In/aan elk(e) [bak] zitten # [ding]. Er zijn # [ding]. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In/aan elk(e) [bak] zitten # [ding]. Er zijn # [ding]. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **56** · Claude-doelen: T9 (56) · regel: G07-welke-som
- Getallenruimte: 0–10 · type: meerkeuze
- Merge-fixlijst: #4 aantal groepjes eerst (56), #6 3 groepjes van 2 (2)
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 17 items · rijGroep per item
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (56), verkeerd-getal (56)
- Verschillende Claude-fout-hints: 1 (meest: “Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-039` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In elke doos zitten 2 ballen. Er zijn 3 dozen. Welke som hoort bij dit verhaal?
    - **Opties:** A) 3 × 2 · B) 4 × 2 · C) 3 + 2
    - **Antwoord:** 3 × 2  (controle: ok)
    - **Fout-hints (Claude):** 3 + 2 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.
  - `G4-GET-E06-claude-bank-033` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In elke mand zitten 6 koekjes. Er zijn 4 manden. Welke som hoort bij dit verhaal?
    - **Opties:** A) 4 × 6 · B) 4 + 6 · C) 5 × 6
    - **Antwoord:** 4 × 6  (controle: ok)
    - **Fout-hints (Claude):** 4 + 6 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.

- **Hint 1 (te schrijven):** Lees het verhaal goed. Zie je groepjes die even groot zijn?
- **Hint 2 (te schrijven):** In elk groepje zitten er evenveel. Dat is een keersom. Zoek de som die begint met het aantal groepjes. Daarna komt hoeveel er in één groepje zitten.
- **Ouderzin:** Je kind kiest de keersom die past bij een verhaal met groepjes die even groot zijn.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de plussom` (de plussom) → Dat is een plussom. Maar in het verhaal zijn er groepjes die even groot zijn. Dat is keer.  [nieuw]
  - `ander getal` (de keersom (afleider met één getal anders, zoals (a+1) × b)) → Dat is wel een keersom. Maar één getal klopt niet. Hoeveel groepjes zijn er? En hoeveel zitten er in elk groepje?  [nieuw]
- Status: hints klaar

## Somtype 2: In/aan elk(e) [bak] zitten # [ding]. Hoeveel [ding] zitten er in # [ding]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In/aan elk(e) [bak] zitten # [ding]. Hoeveel [ding] zitten er in # [ding]?” (koppeling: claudeId)
- Items: **38** · Claude-doelen: D5-2 (23), D5-3 (15) · regel: G11-keer-verhaal
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Denkfouten (Claude): een-ernaast (89), optellen-ipv-vermenigvuldigen (25)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-115` (Claude D5-2, bank, niveau 2 → toepassen)
    - **Opgave:** In elk potje zitten 2 kralen. Hoeveel kralen zitten er in 3 potjes?
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 3 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.
  - `G4-GET-E06-claude-bank-125` (Claude D5-3, bank, niveau 3 → toepassen)
    - **Opgave:** In elke mand zitten 3 eieren. Hoeveel eieren zitten er in 4 manden?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 9 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 15 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 16 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Hoeveel groepjes zijn er? En hoeveel zitten er in elk groepje?
- **Hint 2 (te schrijven):** Tel in sprongen. Elke sprong is zo groot als één groepje. Maak zoveel sprongen als er groepjes zijn.
- **Ouderzin:** Je kind rekent uit hoeveel er in een paar even grote groepjes samen zitten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal uit de vraag` (fout = een getal uit de vraag) → Dat getal staat al in de vraag. Je moet er nog mee rekenen. Hoeveel zijn het er in alle groepjes samen?  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Maar elk groepje telt mee. Tel een groepje steeds opnieuw erbij.  [nieuw]
  - `een groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Tel nog eens hoeveel groepjes er zijn, en maak precies zoveel sprongen.  [nieuw]
  - `een groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Heb je alle groepjes meegeteld? Tel je sprongen nog eens.  [nieuw]
  - `elk groepje één te veel` (fout = antwoord + getal2) → Dat is te veel. Kijk nog eens hoeveel er in elk groepje zitten. Tel in sprongen van dat getal.  [nieuw]
  - `elk groepje één te weinig` (fout = antwoord − getal2) → Dat is te weinig. Kijk nog eens hoeveel er in elk groepje zitten. Tel in sprongen van dat getal.  [nieuw]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Tel nog eens in sprongen. Maak zoveel sprongen als er groepjes zijn.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Heb je alle groepjes meegeteld? Tel je sprongen nog eens.  [nieuw]
  - `andere fout` (andere fout) → Tel in sprongen. Elke sprong is één groepje.  [nieuw]
- Status: hints klaar

## Somtype 3: # [ding] hebben elk # [ding]. Dat is evenveel als # [ding] met elk # [ding]. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# [ding] hebben elk # [ding]. Dat is evenveel als # [ding] met elk hoeveel [ding]?” (koppeling: claudeId)
- Items: **15** · Claude-doelen: D5-4 (15) · regel: G13-omdraaien
- Getallenruimte: 0–10 · type: kale
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “# [ding] hebben elk # [ding]. Dat is evenveel als # [ding] met elk hoeveel [ding]?”. Hints nakijken.
- Merge-fixlijst: #12 vraag naar samen (15)
- Bijna dubbel (duplicaatVan, niet in dezelfde sessie): 5 items · rijGroep per item
- Denkfouten (Claude): een-groepje-ernaast (30), optellen-ipv-vermenigvuldigen (15), een-groepje-als-antwoord (12)
- Verschillende Claude-fout-hints: 17 (meest: “Je hebt één groepje te veel geteld.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-011` (Claude D5-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** 7 konijnen hebben elk 6 wortels. Dat is evenveel als 6 konijnen met elk 7 wortels. Hoeveel wortels zijn dat samen?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 42 → 42 is de uitkomst. Gevraagd is het getal dat je met 6 vermenigvuldigt. · 6 → 6 staat er al. Bij omdraaien wisselen de twee getallen van plek. · 13 → Het is een keersom, geen plussom. De twee getallen wisselen alleen van plek.
    - **Uitleg (Claude):** 7 × 6 = 6 × 7 = 42. Omdraaien mag: de uitkomst blijft gelijk.
  - `G4-GET-E06-claude-bank-002` (Claude D5-4, gegenereerd, niveau 1 → basis)
    - **Opgave:** 2 pinguïns hebben elk 9 vissen. Dat is evenveel als 9 pinguïns met elk 2 vissen. Hoeveel vissen zijn dat samen?
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** 18 → 18 is de uitkomst. Gevraagd is het getal dat je met 9 vermenigvuldigt. · 9 → 9 staat er al. Bij omdraaien wisselen de twee getallen van plek. · 11 → Het is een keersom, geen plussom. De twee getallen wisselen alleen van plek.
    - **Uitleg (Claude):** 2 × 9 = 9 × 2 = 18. Omdraaien mag: de uitkomst blijft gelijk.

- **Hint 1 (te schrijven):** De twee zinnen geven evenveel. Kies de zin die je het makkelijkst vindt.
- **Hint 2 (te schrijven):** In die zin staat hoeveel ieder heeft. Tel in sprongen van dat getal. Maak zoveel sprongen als het eerste getal in die zin.
- **Ouderzin:** Je kind rekent een keersom uit en ziet dat je de getallen mag omdraaien. Het mag de makkelijkste som kiezen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één groepje` (fout = getal2 (tekst per item)) → … (eigen tekst per item: "Dat is wat één groepje heeft." of "Je hebt één groepje te weinig geteld.")  [Claude, ok]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Het is een keersom. Kijk hoeveel elk heeft, en tel in sprongen van dat getal.  [Claude, taalfix]
  - `een groepje te veel` (fout = antwoord + getal2) → Je hebt één groepje te veel geteld.  [Claude, ok]
  - `een groepje te weinig` (fout = antwoord − getal2) → Je hebt één groepje te weinig geteld.  [Claude, ok]
  - `ieder één te veel` (fout = antwoord + getal1) → Dat is te veel. Kijk nog eens hoeveel ieder heeft. Tel in sprongen van dat getal.  [nieuw]
  - `ieder één te weinig` (fout = antwoord − getal1) → Dat is te weinig. Kijk nog eens hoeveel ieder heeft. Tel in sprongen van dat getal.  [nieuw]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Kies de zin die je het makkelijkst vindt, en tel in sprongen.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Kies de zin die je het makkelijkst vindt, en tel in sprongen.  [nieuw]
  - `andere fout` (andere fout) → Kies de zin die je het makkelijkst vindt. Tel in sprongen van hoeveel ieder heeft.  [nieuw]
- Status: hints klaar

## Somtype 4: # × # vind je lastig. Draai de som om. Hoeveel is # × #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# × # vind je lastig. Draai de som om. Hoeveel is # × #?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: D5-4 (12) · regel: G13-omdraaien
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Merge-fixlijst: #22 omgedraaid (lastig = tafel buiten G4) (1), #22 × 10 vervangen door × 7 (1), #22 × 10 vervangen door × 8 (1), #22 × 10 vervangen door × 9 (1)
- Denkfouten (Claude): tafelbuur (24), optellen-ipv-vermenigvuldigen (12)
- Verschillende Claude-fout-hints: 11 (meest: “Keer, niet plus.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-025` (Claude D5-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 2 × 9 vind je lastig. Draai de som om. Hoeveel is 9 × 2?
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** 16 → Je zit één stap te laag in de tafel van 2. · 20 → Je zit één stap te hoog in de tafel van 2. · 11 → Keer, niet plus.
    - **Uitleg (Claude):** 2 × 9 = 9 × 2 = 18. De makkelijkste kant kiezen mag.
  - `G4-GET-E06-claude-bank-020` (Claude D5-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 5 × 7 vind je lastig. Draai de som om. Hoeveel is 7 × 5?
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** 45 → Je zit één stap te laag in de tafel van 5. · 55 → Je zit één stap te hoog in de tafel van 5. · 15 → Keer, niet plus.
    - **Uitleg (Claude):** 5 × 7 = 7 × 5 = 35. De makkelijkste kant kiezen mag.

- **Hint 1 (te schrijven):** Bij keer mag je de getallen omdraaien. De uitkomst blijft hetzelfde.
- **Hint 2 (te schrijven):** Reken de nieuwe som uit. Het tweede getal zegt hoe groot de sprong is. Het eerste getal zegt hoeveel sprongen je maakt.
- **Ouderzin:** Je kind leert dat je een keersom mag omdraaien: de uitkomst blijft hetzelfde.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een stap naast in de tafel` (een stap te hoog of te laag in de tafel (tekst per item)) → Je zit één stap te laag (of te hoog) in de tafel van …  [Claude, ok]
  - `plus gedaan` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Het is een keersom: keer, niet plus.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Tel nog eens in sprongen, en tel hoeveel sprongen je maakt.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Heb je alle sprongen gemaakt? Tel ze nog eens.  [nieuw]
  - `andere fout` (andere fout) → Reken de omgedraaide som uit. Tel in sprongen.  [nieuw]
- Status: hints klaar

## Somtype 5: Bij de lunch zijn er # [ding] brood en # [ding] beleg. Hoeveel verschillende boterhammen met één soort brood en één soort beleg kun je maken?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Bij de lunch zijn er # [ding] brood en # [ding] beleg. Hoeveel verschillende boterhammen met één soort brood en één soort beleg kun je maken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je mag niet zomaar optellen. Maak een lijstje van alle boterhammen met het eerste soort brood.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-032` (Claude W1, ai, niveau 2 → toepassen)
    - **Opgave:** Bij de lunch zijn er 3 soorten brood en 2 soorten beleg. Hoeveel verschillende boterhammen met één soort brood en één soort beleg kun je maken?
    - **Opties:** A) 3 · B) 6 · C) 5
    - **Antwoord:** 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5 → Je mag niet zomaar optellen. Maak een lijstje van alle boterhammen met het eerste soort brood. · 3 → Bij elk soort brood passen twee soorten beleg. Tel dus per brood hoeveel keuzes je hebt.
    - **Uitleg (Claude):** Bij elk van de 3 broden kun je 2 soorten beleg kiezen. Dat zijn 3 keer 2 is 6 boterhammen.

- **Hint 1 (te schrijven):** Neem eerst één soort brood. Met welk beleg kan dat allemaal?
- **Hint 2 (te schrijven):** Elk soort brood kan met elk soort beleg. Maak een rijtje voor elk soort brood. Tel daarna alle boterhammen.
- **Ouderzin:** Je kind telt hoeveel verschillende boterhammen je kunt maken: elk soort brood met elk soort beleg.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar

## Somtype 6: Je hebt # [ding] en # [ding]. Op hoeveel manieren kun je een trui en een broek kiezen?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Je hebt # [ding] en # [ding]. Hoeveel verschillende sets van een trui en een broek kun je maken?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: W1 (1) · regel: D-puzzels
- Getallenruimte: 0–10 · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): plaatje nodig: tekening bij het verhaal (Didactiek §4)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “Je hebt # [ding] en # [ding]. Hoeveel verschillende sets van een trui en een broek kun je maken?”. Hints nakijken.
- Merge-fixlijst: #8 manieren (1)
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (1), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je telt de kleren niet bij elkaar op. Kijk hoeveel broeken bij één trui passen.”)
- Voorbeelden:
  - `G4-GET-E06-claude-bank-137` (Claude W1, ai, niveau 3 → toepassen)
    - **Opgave:** Je hebt 2 truien en 3 broeken. Op hoeveel manieren kun je een trui en een broek kiezen?
    - **Opties:** A) 6 manieren · B) 5 manieren · C) 3 manieren
    - **Antwoord:** 6 manieren  (controle: ok)
    - **Fout-hints (Claude):** 5 manieren → Je telt de kleren niet bij elkaar op. Kijk hoeveel broeken bij één trui passen. · 3 manieren → Vergeet de tweede trui niet. Die kan ook met elke broek.
    - **Uitleg (Claude):** Bij de eerste trui passen 3 broeken. Bij de tweede trui passen ook 3 broeken. Samen zijn dat 6 sets.

- **Hint 1 (te schrijven):** Neem eerst één trui. Met welke broeken kan die allemaal?
- **Hint 2 (te schrijven):** Elke trui kan met elke broek. Maak een rijtje voor elke trui. Tel daarna alles bij elkaar.
- **Ouderzin:** Je kind telt op hoeveel manieren je een trui en een broek kunt kiezen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (5 manieren) → Je moet de kleren niet bij elkaar optellen. Kijk hoeveel broeken er bij één trui passen.  [Claude, taalfix]
  - `één trui geteld` (3 manieren) → Vergeet de tweede trui niet. Die kan ook met elke broek.  [Claude, ok]
- Status: hints klaar
