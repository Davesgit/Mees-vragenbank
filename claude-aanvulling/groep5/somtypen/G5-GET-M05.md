# G5-GET-M05 — Alle tafels tot tien

Onze omschrijving: Alle tafels ≤10 + deeltafels (opbouw) · in onze bank: 8 items

Claude-vragen gemapt: **129** in **12** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # : # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# : # =” (koppeling: claudeId)
- Items: **70** · Claude-doelen: D5-7 (38), D5-8 (32) · regel: G5-K03-kaal-deel
- Getallenruimte: 0–10, 0–100, 0–20 · type: kale
- Uitleg bij het eerste gebruik (kindtekst, veld begripUitleg): “':' betekent gedeeld door.”
- Denkfouten (Claude): een-ernaast (124), getal-overgenomen (16)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-015` (Claude D5-7, bank, niveau 3 → toepassen)
    - **Opgave:** 6 : 2 =
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 5 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-M05-claude-bank-068` (Claude D5-8, bank, niveau 3 → toepassen)
    - **Opgave:** 12 : 6 =
    - **Antwoord:** 2  (controle: ok)
    - **Fout-hints (Claude):** 4 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 6 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.

- **Hint 1 (te schrijven):** Bij delen kijk je hoe vaak het ene getal in het andere past. Hoe vaak past het tweede getal in het eerste getal?
- **Hint 2 (te schrijven):** Denk aan de keersom: welk getal keer het tweede getal is het eerste getal?
- **Ouderzin:** Je kind rekent een deelsom uit met de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het getal waardoor je deelt` (fout = getal2) → Dat is het getal waardoor je deelt. De vraag is hoe vaak het in het eerste getal past.  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Kijk naar het teken: het is een deelsom. Hoe vaak past het tweede getal in het eerste?  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na met de keersom: jouw antwoord keer het tweede getal is meer dan het eerste getal.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na met de keersom: jouw antwoord keer het tweede getal is minder dan het eerste getal.  [nieuw]
  - `twee te veel` (fout = antwoord + 2) → Dat is twee te veel. Reken na met de keersom: jouw antwoord keer het tweede getal is meer dan het eerste getal.  [nieuw]
  - `twee te weinig` (fout = antwoord − 2) → Dat is twee te weinig. Reken na met de keersom: jouw antwoord keer het tweede getal is minder dan het eerste getal.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel van het tweede getal op, tot je bij het eerste getal bent. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar

## Somtype 2: # : # = □. Denk aan de keersom # × □ = #.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# : # = □. Denk aan de keersom # × □ = #.” (koppeling: claudeId)
- Items: **15** · Claude-doelen: D5-9 (15) · regel: G5-K04-deel-keersom
- Getallenruimte: 0–10, 0–100, 0–20 · type: invullen
- Uitleg bij het eerste gebruik (kindtekst, veld begripUitleg): “':' betekent gedeeld door.”
- Denkfouten (Claude): tafelbuur (15), verkeerde-bewerking (15), andere-deel-genomen (13)
- Verschillende Claude-fout-hints: 3 (meest: “Zeg de tafel op tot je precies bij het totaal bent, niet erover en niet eronder.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-085` (Claude D5-9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 49 : 7 = □. Denk aan de keersom 7 × □ = 49.
    - **Antwoord:** 7  (controle: ok)
    - **Fout-hints (Claude):** 6 → Zeg de tafel op tot je precies bij het totaal bent, niet erover en niet eronder. · 343 → Delen maakt kleiner, niet groter.
    - **Uitleg (Claude):** 7 × 7 = 49, dus 49 : 7 = 7.
  - `G5-GET-M05-claude-bank-072` (Claude D5-9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 20 : 5 = □. Denk aan de keersom 5 × □ = 20.
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 3 → Zeg de tafel op tot je precies bij het totaal bent, niet erover en niet eronder. · 100 → Delen maakt kleiner, niet groter. · 5 → Dat is het getal waardoor je deelt, niet de uitkomst.
    - **Uitleg (Claude):** 5 × 4 = 20, dus 20 : 5 = 4.

- **Hint 1 (te schrijven):** Kijk naar de keersom in de vraag. Welk getal hoort op het hokje?
- **Hint 2 (te schrijven):** Zeg de tafel op tot je precies bij het eerste getal bent. Hoeveel stappen zijn het?
- **Ouderzin:** Je kind rekent een deelsom uit met de keersom die erbij hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het getal waardoor je deelt` (fout = getal2) → Dat is het getal waardoor je deelt. Welk getal hoort op het hokje in de keersom?  [nieuw]
  - `keer gedaan` (fout = getal1 × getal2) → Je hebt keer gedaan. Het is een deelsom. Welk getal hoort op het hokje in de keersom?  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Zeg de tafel op tot je precies bij het eerste getal bent.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Zeg de tafel op tot je precies bij het eerste getal bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel van het tweede getal op, tot je bij het eerste getal bent. Hoeveel stappen zijn het?  [nieuw]
- Status: hints klaar

## Somtype 3: # × # =

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# × # =” (koppeling: claudeId)
- Items: **12** · Claude-doelen: D5-6 (12) · regel: G5-K02-kaal-keer
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (24)
- Verschillende Claude-fout-hints: 1 (meest: “Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-091` (Claude D5-6, bank, niveau 2 → toepassen)
    - **Opgave:** 7 × 6 =
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 48 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 56 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.
  - `G5-GET-M05-claude-bank-087` (Claude D5-6, bank, niveau 3 → toepassen)
    - **Opgave:** 6 × 8 =
    - **Antwoord:** 48  (controle: ok)
    - **Fout-hints (Claude):** 56 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 60 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.

- **Hint 1 (te schrijven):** Een keersom is groepjes van hetzelfde aantal. Hoeveel groepjes zijn het, en hoeveel zitten er in elk?
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind oefent de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één stap te ver` (fout = antwoord + getal1) → Dat is één stap te ver in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te weinig` (fout = antwoord − getal1) → Dat is één stap te weinig in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te ver (andere tafel)` (fout = antwoord + getal2) → Dat is één stap te ver in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te weinig (andere tafel)` (fout = antwoord − getal2) → Dat is één stap te weinig in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 4: Er staan # [ding]. In elk(e) [bak] zitten # [ding]. Hoeveel [ding] zijn er samen?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Er staan # [ding]. In elk(e) [bak] zitten # [ding]. Hoeveel [ding] zijn er samen?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: D5-6 (12) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (33), optellen-ipv-vermenigvuldigen (3)
- Verschillende Claude-fout-hints: 2 (meest: “Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-105` (Claude D5-6, bank, niveau 2 → toepassen)
    - **Opgave:** Er staan 7 bakken. In elke bak zitten 6 ballen. Hoeveel ballen zijn er samen?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 49 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 30 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 56 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn.
  - `G5-GET-M05-claude-bank-112` (Claude D5-6, bank, niveau 3 → toepassen)
    - **Opgave:** Er staan 6 tassen. In elke tas zitten 8 boeken. Hoeveel boeken zijn er samen?
    - **Antwoord:** 48  (controle: ok)
    - **Fout-hints (Claude):** 56 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 36 → Bijna! Je zit één groepje ernaast. Tel nog eens goed hoeveel groepjes het zijn. · 14 → Let op het teken: het is een keersom. Keer betekent: zoveel groepjes van. Probeer het groepje steeds opnieuw erbij te tellen.

- **Hint 1 (te schrijven):** Hoeveel staan er? En hoeveel zitten er in elk? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal2) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal2) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal1) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal1) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 5: [rooster] Kleur # × # [ding] rechthoek op het rooster.

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[rooster] Kleur # × # [ding] rechthoek op het rooster.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: D5-5 (8) · regel: G10-rooster-keer
- Getallenruimte: 0–10 · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-GET-M05-claude-bank-119` (Claude D5-5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Kleur 7 × 9 als rechthoek op het rooster.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 7, "hokjesPerRij": 9, "claudeAntwoord": "9x7", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 7 rijen van 9 hokjes (rechthoek); 9 rijen van 7 ook goed (omdraaien mag)"}`
    - **Antwoord:** 7 rijen van 9 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 7 rijen van 9: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 7 × 9 = 63.
  - `G5-GET-M05-claude-bank-123` (Claude D5-5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Kleur 8 × 6 als rechthoek op het rooster.
    - **Tekening:** `{"soort": "rooster", "rijen": 10, "kolommen": 10, "kleurbaar": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord intern (niet tonen):** `{"soort": "roostervorm", "rijen": 8, "hokjesPerRij": 6, "claudeAntwoord": "6x8", "claudeNotatie": "kolommen x rijen", "nakijken": "gekleurd: 8 rijen van 6 hokjes (rechthoek); 6 rijen van 8 ook goed (omdraaien mag)"}`
    - **Antwoord:** 8 rijen van 6 hokjes  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** 8 rijen van 6: tik op de linkerbovenhoek en dan op de rechteronderhoek. Tel na: 8 × 6 = 48.

- **Hint 1 (te schrijven):** Het keerteken (×) betekent: zoveel keer. Het eerste getal zegt hoeveel rijen je kleurt. Het tweede getal zegt hoeveel hokjes er in elke rij komen.
- **Hint 2 (te schrijven):** Kleur eerst één rij. Kleur dan de volgende rij recht eronder, net zo lang. Ga door tot je genoeg rijen hebt.
- **Ouderzin:** Je kind kleurt een keersom als rechthoek op een rooster: het eerste getal is het aantal rijen, het tweede het aantal hokjes per rij.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus gedaan` (fout = getal1 + getal2 (aantal gekleurde hokjes)) → Je hebt de getallen opgeteld. Het is een keersom: je kleurt een aantal rijen, en in elke rij evenveel hokjes.  [nieuw]
  - `één rij` (fout = getal2 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `één kolom` (fout = getal1 (aantal gekleurde hokjes)) → Je hebt nog niet genoeg hokjes gekleurd. Kleur alle rijen, recht onder elkaar. In elke rij evenveel hokjes.  [nieuw]
  - `andere fout` (andere fout) → Tel je rijen. Tel de hokjes in elke rij. Kloppen ze met de som?  [nieuw]
- Status: hints klaar

## Somtype 6: # × # [ding] je lastig. Draai de som om. Hoeveel is # × #?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “# × # [ding] je lastig. Draai de som om. Hoeveel is # × #?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: D5-4 (4) · regel: FX-G4-22
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (8), optellen-ipv-vermenigvuldigen (4)
- Verschillende Claude-fout-hints: 5 (meest: “Keer, niet plus.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-099` (Claude D5-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 7 × 9 vind je lastig. Draai de som om. Hoeveel is 9 × 7?
    - **Antwoord:** 63  (controle: ok)
    - **Fout-hints (Claude):** 56 → Je zit één stap te laag in de tafel van 7. · 70 → Je zit één stap te hoog in de tafel van 7. · 16 → Keer, niet plus.
    - **Uitleg (Claude):** 7 × 9 = 9 × 7 = 63. De makkelijkste kant kiezen mag.
  - `G5-GET-M05-claude-bank-100` (Claude D5-4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 6 × 9 vind je lastig. Draai de som om. Hoeveel is 9 × 6?
    - **Antwoord:** 54  (controle: ok)
    - **Fout-hints (Claude):** 48 → Je zit één stap te laag in de tafel van 6. · 60 → Je zit één stap te hoog in de tafel van 6. · 15 → Keer, niet plus.
    - **Uitleg (Claude):** 6 × 9 = 9 × 6 = 54. De makkelijkste kant kiezen mag.

- **Hint 1 (te schrijven):** Bij een keersom mag je de getallen omdraaien. De uitkomst blijft hetzelfde.
- **Hint 2 (te schrijven):** Kies de tafel die je het best kent, en zeg hem op tot het goede aantal stappen.
- **Ouderzin:** Je kind draait een keersom om, zodat het een tafel kan gebruiken die het kent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Kijk naar het teken: het is een keersom.  [nieuw]
  - `één stap te ver` (fout = antwoord + getal1) → Dat is één stap te ver in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te weinig` (fout = antwoord − getal1) → Dat is één stap te weinig in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te ver (andere tafel)` (fout = antwoord + getal2) → Dat is één stap te ver in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `één stap te weinig (andere tafel)` (fout = antwoord − getal2) → Dat is één stap te weinig in de tafel. Zeg de tafel nog eens op en tel de stappen.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 7: [wie] heeft # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “[wie] heeft # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: D5-6 (3) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (6), optellen-ipv-vermenigvuldigen (3), cijfers-verwisseld (2)
- Verschillende Claude-fout-hints: 10 (meest: “Je hebt de goede cijfers, maar draai ze om.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-127` (Claude D5-6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elke dino heeft 9 tanden. Er zijn 9 dino's. Hoeveel tanden zijn dat samen?
    - **Antwoord:** 81  (controle: ok)
    - **Fout-hints (Claude):** 18 → 9 + 9 telt de tanden en de dino's op. Maar élke dino heeft 9 tanden. Tel 9 steeds opnieuw erbij, 9 keer. · 72 → Dat zijn 8 dino's. Er is er nog één met 9 tanden. · 90 → Dat is één dino te veel. Het zijn er 9.
    - **Uitleg (Claude):** 9 × 9 betekent 9 keer een groepje van 9. 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 = 81.
  - `G5-GET-M05-claude-bank-126` (Claude D5-6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Elke eekhoorn heeft 9 noten. Er zijn 8 eekhoorns. Hoeveel noten zijn dat samen?
    - **Antwoord:** 72  (controle: ok)
    - **Fout-hints (Claude):** 17 → 9 + 8 telt de noten en de eekhoorns op. Maar élke eekhoorn heeft 9 noten. Tel 9 steeds opnieuw erbij, 8 keer. · 63 → Dat zijn 7 eekhoorns. Er is er nog één met 9 noten. · 81 → Dat is één eekhoorn te veel. Het zijn er 8. · 27 → Je hebt de goede cijfers, maar draai ze om.
    - **Uitleg (Claude):** 8 × 9 betekent 8 keer een groepje van 9. 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 = 72.

- **Hint 1 (te schrijven):** Ze hebben allemaal evenveel. Hoeveel zijn het er? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal2) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal2) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `cijfers omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in een andere volgorde. Kijk goed welk cijfer op welke plek hoort.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 8: Een spin heeft # [ding]. In [plek] zitten # [ding]. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een spin heeft # [ding]. In [plek] zitten # [ding]. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: D5-6 (1) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (2), optellen-ipv-vermenigvuldigen (1), cijfers-verwisseld (1)
- Verschillende Claude-fout-hints: 4 (meest: “8 + 7 is één spin plus het aantal spinnen. Maar élke spin heeft 8 poten, en er zijn 7 spinnen.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-102` (Claude D5-6, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een spin heeft 8 poten. In de schuur zitten 7 spinnen. Hoeveel poten zijn dat samen?
    - **Antwoord:** 56  (controle: ok)
    - **Fout-hints (Claude):** 15 → 8 + 7 is één spin plus het aantal spinnen. Maar élke spin heeft 8 poten, en er zijn 7 spinnen. · 48 → Dat zijn 6 spinnen. Er is nog een zevende spin met 8 poten. · 64 → Dat is 8 × 8, een spin te veel. Het zijn 7 spinnen. · 65 → Je hebt de goede cijfers, maar draai ze om. 8 × 7 is zes-en-...?
    - **Uitleg (Claude):** 7 spinnen met elk 8 poten: 8 × 7. Je mag omdraaien: 7 × 8. 7 × 7 = 49, en nog een groepje van 7 erbij: 56.

- **Hint 1 (te schrijven):** Elke spin heeft evenveel poten. Hoeveel spinnen zijn er? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal2) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal2) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `cijfers omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in een andere volgorde. Kijk goed welk cijfer op welke plek hoort.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 9: In [plek] van een dino liggen # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat?

- Sleutel: nrOrigineel **9** · somtypeOrigineel “In [plek] van een dino liggen # [ding]. Er zijn # [ding]. Hoeveel [ding] zijn dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: D5-6 (1) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (2), optellen-ipv-vermenigvuldigen (1), cijfers-verwisseld (1)
- Verschillende Claude-fout-hints: 4 (meest: “7 + 6 telt de nesten en de eieren op. Maar in élk nest liggen 6 eieren, en er zijn 7 nesten.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-115` (Claude D5-6, handmatig, niveau 2 → toepassen)
    - **Opgave:** In het nest van een dino liggen 6 eieren. Er zijn 7 nesten. Hoeveel eieren zijn dat?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** 13 → 7 + 6 telt de nesten en de eieren op. Maar in élk nest liggen 6 eieren, en er zijn 7 nesten. · 36 → Dat is 6 × 6. Er zijn 7 nesten, dus nog 6 eieren erbij. · 48 → Dat is 8 × 6. Het zijn 7 nesten, dus 6 eieren minder. · 24 → Je hebt de goede cijfers, maar in de verkeerde volgorde. 7 × 6 is twee-en-...?
    - **Uitleg (Claude):** 7 nesten met 6 eieren: 7 × 6. 7 × 5 = 35, dat is de tafel van 5. Nog een groepje van 7 erbij: 35 + 7 = 42.

- **Hint 1 (te schrijven):** In elk nest liggen evenveel. Hoeveel nesten zijn er? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal2) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal2) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `cijfers omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in een andere volgorde. Kijk goed welk cijfer op welke plek hoort.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 10: Op de tribune staan # rijen met # [ding]. Hoeveel [ding] zijn er?

- Sleutel: nrOrigineel **10** · somtypeOrigineel “Op de tribune staan # rijen met # [ding]. Hoeveel [ding] zijn er?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: D5-6 (1) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (2), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 3 (meest: “6 + 9 telt de rijen en de stoelen op. Maar elke rij heeft 9 stoelen, en er zijn 6 van die rijen.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-116` (Claude D5-6, handmatig, niveau 2 → toepassen)
    - **Opgave:** Op de tribune staan 6 rijen met 9 stoelen. Hoeveel stoelen zijn er?
    - **Antwoord:** 54  (controle: ok)
    - **Fout-hints (Claude):** 15 → 6 + 9 telt de rijen en de stoelen op. Maar elke rij heeft 9 stoelen, en er zijn 6 van die rijen. · 45 → Dat is 5 rijen. Er zijn 6 rijen, dus nog een rij van 9 erbij. · 56 → Heel dichtbij! Reken via 6 × 10 = 60 en haal er dan 6 af.
    - **Uitleg (Claude):** 6 rijen van 9 stoelen: 6 × 9. 6 × 10 = 60, dat is één stoel per rij te veel. 60 − 6 = 54.

- **Hint 1 (te schrijven):** Hoeveel rijen zijn er, en hoeveel zitten er in elke rij? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal2) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal2) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal1) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal1) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `twee te veel` (fout = antwoord + 2) → Bijna! Dat is twee te veel. Reken de tafel nog eens na.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 11: [wie] eet # kilo vlees per dag. Hoeveel kilo eet hij in # dagen?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “[wie] eet # kilo vlees per dag. Hoeveel kilo eet hij in # dagen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: D5-6 (1) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (2), optellen-ipv-vermenigvuldigen (1), cijfers-verwisseld (1)
- Verschillende Claude-fout-hints: 4 (meest: “Je hebt 7 en 8 bij elkaar opgeteld. Maar de dino eet 8 dagen lang élke dag 7 kilo. Dus 7 + 7 + 7 ... acht keer.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-125` (Claude D5-6, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een dino eet 7 kilo vlees per dag. Hoeveel kilo eet hij in 8 dagen?
    - **Antwoord:** 56  (controle: ok)
    - **Fout-hints (Claude):** 15 → Je hebt 7 en 8 bij elkaar opgeteld. Maar de dino eet 8 dagen lang élke dag 7 kilo. Dus 7 + 7 + 7 ... acht keer. · 49 → Bijna! 7 × 7 = 49, maar het zijn 8 dagen. Doe er nog één dag van 7 kilo bij. · 63 → Dat is 7 × 9. Het zijn maar 8 dagen, dus één groepje van 7 minder. · 65 → Je hebt de goede cijfers, maar draai ze eens om. 7 × 8 is zes-en-...?
    - **Uitleg (Claude):** 7 × 8 betekent 8 keer 7. 7 × 7 = 49, dat weet je misschien al. Nog een groepje van 7 erbij: 49 + 7 = 56.

- **Hint 1 (te schrijven):** Elke dag eet hij evenveel kilo. Hoeveel dagen zijn het? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal2) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal2) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `cijfers omgedraaid` (Claudes sleutel: cijfers-verwisseld) → Je hebt de goede cijfers, maar in een andere volgorde. Kijk goed welk cijfer op welke plek hoort.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar

## Somtype 12: [wie] ziet elke dag # [ding] in de tuin. Hoeveel [ding] zijn dat in # dagen?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “[wie] ziet elke dag # [ding] in de tuin. Hoeveel [ding] zijn dat in # dagen?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: D5-6 (1) · regel: G5-C01-keer-context
- Getallenruimte: 0–100 · type: kale
- Denkfouten (Claude): tafelbuur (3), optellen-ipv-vermenigvuldigen (1)
- Verschillende Claude-fout-hints: 4 (meest: “9 + 6 telt de dagen bij de vogels op. Maar élke dag ziet hij 9 vogels, 6 dagen lang.”)
- Voorbeelden:
  - `G5-GET-M05-claude-bank-129` (Claude D5-6, handmatig, niveau 2 → toepassen)
    - **Opgave:** Een kind ziet elke dag 9 vogels in de tuin. Hoeveel vogels zijn dat in 6 dagen?
    - **Antwoord:** 54  (controle: ok)
    - **Fout-hints (Claude):** 15 → 9 + 6 telt de dagen bij de vogels op. Maar élke dag ziet hij 9 vogels, 6 dagen lang. · 48 → Dat is 8 × 6. Het zijn 9 vogels per dag, dus nog een groepje van 6 erbij. · 45 → Dat is 9 × 5. Het zijn 6 dagen, dus nog een dag met 9 erbij. · 60 → 60 is 10 × 6. Het zijn maar 9 per dag, dus haal er 6 af.
    - **Uitleg (Claude):** 6 dagen met elk 9 vogels: 9 × 6. 9 × 6 is hetzelfde als 6 × 9. 6 × 10 = 60, dat is er één te veel per dag: 60 − 6 = 54.

- **Hint 1 (te schrijven):** Elke dag ziet het kind evenveel. Hoeveel dagen zijn het? Dat is een keersom.
- **Hint 2 (te schrijven):** Weet je het niet meteen? Begin bij een som die je wel weet, zoals vijf keer of tien keer. Reken van daar verder of terug.
- **Ouderzin:** Je kind lost een verhaaltje op met een keersom uit de tafels.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal: dat is een keersom.  [nieuw]
  - `één groepje te veel` (fout = antwoord + getal1) → Dat is één groepje te veel. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `één groepje te weinig` (fout = antwoord − getal1) → Dat is één groepje te weinig. Lees nog eens hoeveel groepjes het zijn.  [nieuw]
  - `in elk groepje één te veel` (fout = antwoord + getal2) → Dan zit er in elk groepje één te veel. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `in elk groepje één te weinig` (fout = antwoord − getal2) → Dan zit er in elk groepje één te weinig. Lees nog eens hoeveel er in elk zitten.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Zeg de tafel nog eens op, stap voor stap, tot je bij het goede aantal groepjes bent.  [nieuw]
  - `andere fout` (andere fout) → Zeg de tafel op, stap voor stap. Tel de stappen tot je bij het goede aantal groepjes bent.  [nieuw]
- Status: hints klaar
