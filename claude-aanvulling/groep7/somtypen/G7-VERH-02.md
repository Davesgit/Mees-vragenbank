# G7-VERH-02 — Procenten van een geheel

Onze omschrijving: % als deel–geheel · in onze bank: 8 items

Claude-vragen gemapt: **1030** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel is #% van #?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Hoeveel is #% van #?” (koppeling: claudeId)
- Items: **534** · Claude-doelen: V3 (375), V1 (159) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Uit de G6-park: 159 items
- Denkfouten (Claude): getal-overgenomen (456), andere-deel-genomen (357), nul-fout-tientallen (255)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-112` (Claude V1, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 25% van 112?
    - **Antwoord:** 28  (controle: ok)
    - **Fout-hints (Claude):** 280 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-239` (Claude V3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel is 40% van 335?
    - **Antwoord:** 134  (controle: ok)
    - **Fout-hints (Claude):** 295 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Welk deel van het getal is dat procent?
- **Hint 2 (te schrijven):** Reken eerst uit hoeveel tien procent van het getal is. Neem daarvan zo vaak als nodig. Vijftig procent is de helft, vijfentwintig procent een kwart.
- **Ouderzin:** Je kind rekent uit hoeveel een percentage van een getal is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele getal` (fout = getal2) → Dat is het hele getal: honderd procent. Je zoekt maar een deel ervan.  [nieuw]
  - `het procent` (fout = getal1) → Dat is het procent uit de vraag. Je zoekt dat deel van het getal.  [nieuw]
  - `tien keer te groot` (fout = antwoord × 10) → Dat is tien keer te groot. Reken het na: hoeveel is tien procent van het getal?  [nieuw]
  - `tien keer te klein` (fout = antwoord : 10) → Dat is tien keer te klein. Reken het na: hoeveel is tien procent van het getal?  [nieuw]
  - `verschil van de getallen` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het verschil van de twee getallen. Maar procent betekent: zoveel van de honderd.  [nieuw]
  - `het andere deel` (Claudes sleutel: andere-deel-genomen) → Dat is het andere deel: wat overblijft. Je zoekt het deel dat bij het procent uit de vraag hoort.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoeveel tien procent van het getal is, en ga van daaruit verder.  [nieuw]
- Status: hints klaar

## Somtype 2: Hoeveel is #% van €#?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel is #% van €#?” (koppeling: claudeId)
- Items: **243** · Claude-doelen: V3 (243) · regel: G7-V05-procent-van
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): nul-fout-tientallen (246), getal-overgenomen (148), andere-deel-genomen (92)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-593` (Claude V3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 40% van €36?
    - **Antwoord:** €14,40  (controle: ok)
    - **Fout-hints (Claude):** €144 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · €1,44 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-582` (Claude V3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel is 15% van €48?
    - **Antwoord:** €7,20  (controle: ok)
    - **Fout-hints (Claude):** €0,72 → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Welk deel van het bedrag is dat procent?
- **Hint 2 (te schrijven):** Reken eerst uit hoeveel tien procent van het bedrag is. Neem daarvan zo vaak als nodig. Vijftig procent is de helft, vijfentwintig procent een kwart.
- **Ouderzin:** Je kind rekent uit hoeveel een percentage van een geldbedrag is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het hele bedrag` (fout = getal2) → Dat is het hele bedrag: honderd procent. Je zoekt maar een deel ervan.  [nieuw]
  - `tien keer te groot` (fout = antwoord × 10) → Dat is tien keer te groot. Reken het na: hoeveel is tien procent van het bedrag?  [nieuw]
  - `tien keer te klein` (fout = antwoord : 10) → Dat is tien keer te klein. Reken het na: hoeveel is tien procent van het bedrag?  [nieuw]
  - `het andere deel` (Claudes sleutel: andere-deel-genomen) → Dat is het andere deel: wat overblijft. Je zoekt het deel dat bij het procent uit de vraag hoort.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoeveel tien procent van het bedrag is, en ga van daaruit verder.  [nieuw]
- Status: hints klaar

## Somtype 3: Hoeveel procent is # van #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoeveel procent is # van #?” (koppeling: claudeId)
- Items: **217** · Claude-doelen: V4 (217) · regel: G7-V06-hoeveel-procent
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): andere-deel-genomen (140), verhoudingstabel-verkeerd (108), getal-overgenomen (105), nul-fout-tientallen (81)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-988` (Claude V4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel procent is 1 van 20?
    - **Opties:** A) 95% · B) 5% · C) 50%
    - **Antwoord:** 5%  (controle: ok)
    - **Fout-hints (Claude):** 95% → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten? · 50% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-02-claude-bank-993` (Claude V4, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel procent is 63 van 105?
    - **Opties:** A) 60% · B) 63% · C) 42%
    - **Antwoord:** 60%  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Welk deel van het geheel is het?
- **Hint 2 (te schrijven):** Maak een verhoudingstabel: het geheel hoort bij honderd procent. Reken uit hoeveel procent bij het deel hoort.
- **Ouderzin:** Je kind rekent uit hoeveel procent een deel van een geheel is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het andere deel` (Claudes sleutel: andere-deel-genomen) → Dat is het andere deel: wat overblijft tot honderd procent. Je zoekt het procent van het deel uit de vraag.  [Claude, taalfix]
  - `het deel zelf` (fout = het deel zelf (als %)) → Dat is het deel uit de vraag, nog geen procent. Hoeveel is dat van de honderd?  [Claude, taalfix]
  - `tien keer ernaast` (Claudes sleutel: nul-fout-tientallen) → Dat is tien keer te groot of tien keer te klein. Reken het na met een verhoudingstabel.  [Claude, taalfix]
  - `verschil van de getallen` (fout = geheel min deel) → Dat is het verschil van de twee getallen, nog geen procent. Welk deel van het geheel is het deel?  [Claude, taalfix]
  - `andere fout` (andere fout) → Het geheel is honderd procent. Hoeveel procent is het deel?  [nieuw]
- Status: hints klaar

## Somtype 4: In [plek] liggen # [ding]. #% ervan is rood. Hoeveel rode [ding] zijn er?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “In [plek] liggen # [ding]. #% ervan is rood. Hoeveel rode [ding] zijn er?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: V1 (12) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Uit de G6-park: 12 items
- Denkfouten (Claude): deel-van-geheel-verkeerd (24), verkeerde-bewerking (12)
- Verschillende Claude-fout-hints: 21 (meest: “50% is de helft: delen door 2.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1010` (Claude V1, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het moeras liggen 48 stenen. 50% ervan is rood. Hoeveel rode stenen zijn er?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 12 → 50% is de helft: delen door 2. · 4.8 → Kijk goed. 50%, dus de helft van 48. · −2 → Procent is een deel van het geheel, niet iets wat je eraf haalt. 50% van 48 betekent de helft van 48.
    - **Uitleg (Claude):** 50% is de helft. 48 : 2 = 24.
  - `G7-VERH-02-claude-bank-1005` (Claude V1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de gymzaal liggen 120 stenen. 10% ervan is rood. Hoeveel rode stenen zijn er?
    - **Antwoord:** 12  (controle: ok)
    - **Fout-hints (Claude):** 60 → 10% is een tiende: delen door 10. · 30 → Kijk goed. 10%, dus een tiende van 120. · 110 → Procent is een deel van het geheel, niet iets wat je eraf haalt. 10% van 120 betekent een tiende van 120.
    - **Uitleg (Claude):** 10% is een tiende. 120 : 10 = 12.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Welk deel van het hele aantal is dat procent?
- **Hint 2 (te schrijven):** Vijftig procent is de helft, vijfentwintig procent een kwart, tien procent een tiende deel. Neem dat deel van het hele aantal.
- **Ouderzin:** Je kind rekent uit hoeveel een percentage van een aantal is (de helft, een kwart, een tiende deel).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `ander deel` (Claudes sleutel: deel-van-geheel-verkeerd) → Dat is een ander deel van het hele aantal. Welk deel hoort bij het procent uit de vraag?  [Claude, taalfix]
  - `procent eraf` (Claudes sleutel: verkeerde-bewerking) → Dat is het hele aantal min het procent. Maar procent betekent: zoveel van de honderd.  [Claude, taalfix]
  - `hele aantal min het procent` (Claudes sleutel (alle, zonder label)) → Dat is het hele aantal min het procent. Maar procent betekent: zoveel van de honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Welk deel van het hele aantal is het procent uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] zijn # [ding]. #% is beschadigd. Hoeveel [ding] zijn beschadigd?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] zijn # [ding]. #% is beschadigd. Hoeveel [ding] zijn beschadigd?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: V3 (12) · regel: G7-V05-procent-van
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (12), procent-verkeerde-basis (12), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 14 (meest: “Procent is per honderd. Deel door 100, of ga via 10%.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1015` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de school zijn 80 knopen. 30% is beschadigd. Hoeveel knopen zijn beschadigd?
    - **Antwoord:** 24  (controle: ok)
    - **Fout-hints (Claude):** 8 → 8 is 10%. Je hebt 30% nodig, dus 3 keer zoveel. · 56 → Dat is het deel dat niet beschadigd is. De vraag is hoeveel wél. · 2400 → Procent is per honderd. Deel door 100, of ga via 10%.
    - **Uitleg (Claude):** Eerst 10%: 80 : 10 = 8. Dan 30% = 3 × 8 = 24.
  - `G7-VERH-02-claude-bank-1021` (Claude V3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het stadion zijn 160 truien. 75% is beschadigd. Hoeveel truien zijn beschadigd?
    - **Antwoord:** 120  (controle: ok)
    - **Fout-hints (Claude):** 16 → 16 is 10%. Je hebt 75% nodig, dus 7.5 keer zoveel. · 40 → Dat is het deel dat niet beschadigd is. De vraag is hoeveel wél. · 12.000 → Procent is per honderd. Deel door 100, of ga via 10%.
    - **Uitleg (Claude):** Eerst 10%: 160 : 10 = 16. Dan 75% = 7.5 × 16 = 120. (5% is de helft van 10%: 8.)

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Hoeveel is tien procent van het hele aantal?
- **Hint 2 (te schrijven):** Tien procent is een tiende deel: deel het hele aantal door tien. Neem dat zo vaak als nodig: zeventig procent is zeven keer tien procent. Vijfentwintig procent is een kwart.
- **Ouderzin:** Je kind rekent uit hoeveel een percentage van een aantal is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer het procent` (fout = getal1 × getal2) → Dat is meer dan het hele aantal. Procent betekent: zoveel van de honderd, dus deel ook door honderd.  [nieuw]
  - `alleen tien procent` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is tien procent. Het procent uit de vraag is meer: reken verder.  [Claude, taalfix]
  - `het andere deel` (Claudes sleutel: verkeerde-bewerking) → Dat is het andere deel: wat niet beschadigd is. Je zoekt het deel dat beschadigd is.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoeveel tien procent van het hele aantal is, en ga van daaruit verder.  [nieuw]
- Status: hints klaar

## Somtype 6: Van de # [ding] hebben er # een [ding]. Hoeveel procent is dat?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Van de # [ding] hebben er # een [ding]. Hoeveel procent is dat?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: V4 (7) · regel: G7-V06-hoeveel-procent
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (7), verkeerde-bewerking (7), omgekeerd-gedeeld (5)
- Verschillende Claude-fout-hints: 8 (meest: “Dat is het aantal zonder. Zet om naar per 100.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-1030` (Claude V4, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Van de 40 dino's hebben er 2 een blaadje. Hoeveel procent is dat?
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 2 → 2 is het aantal, niet het percentage. Zet het om naar per 100. · 38 → Dat is het aantal zonder. Zet om naar per 100. · 20 → Deel het deel door het geheel, niet andersom.
    - **Uitleg (Claude):** Maak er 100 van: 40 → 100 is keer 2.5. 2 × 2.5 = 5. Dus 5%.
  - `G7-VERH-02-claude-bank-1028` (Claude V4, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Van de 20 eekhoorns hebben er 2 een noot. Hoeveel procent is dat?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 2 → 2 is het aantal, niet het percentage. Zet het om naar per 100. · 18 → Dat is het aantal zonder. Zet om naar per 100.
    - **Uitleg (Claude):** Maak er 100 van: 20 → 100 is keer 5. 2 × 5 = 10. Dus 10%.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Welk deel van het hele aantal is het?
- **Hint 2 (te schrijven):** Maak een verhoudingstabel: het hele aantal hoort bij honderd procent. Reken uit hoeveel procent bij het deel hoort.
- **Ouderzin:** Je kind rekent uit hoeveel procent een deel van een groep is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `het aantal zelf` (fout = getal2) → Dat is het aantal uit de vraag, nog geen procent. Hoeveel is dat van de honderd?  [nieuw]
  - `de rest` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het aantal dat het niet heeft. Je zoekt welk deel het wel heeft, in procent.  [nieuw]
  - `omgekeerd gedeeld` (Claudes sleutel: omgekeerd-gedeeld) → Dat is het hele aantal gedeeld door het deel. Het moet andersom: welk deel van het hele aantal is het?  [Claude, taalfix]
  - `andere fout` (andere fout) → Het hele aantal is honderd procent. Hoeveel procent is het deel?  [nieuw]
- Status: hints klaar

## Somtype 7: Een [ding] kost €#. Er is #% korting. Wat is de nieuwe prijs in euro's?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een [ding] kost €#. Er is #% korting. Wat is de nieuwe prijs in euro's?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: V5 (5) · regel: G7-V07-korting
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), procent-verkeerde-basis (5)
- Verschillende Claude-fout-hints: 7 (meest: “Korting gaat eraf, niet erbij.”)
- Voorbeelden:
  - `G7-VERH-02-claude-bank-002` (Claude V5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bal kost €60. Er is 30% korting. Wat is de nieuwe prijs in euro's?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €18 → 18 is de korting. De vraag is wat je nog betaalt. · €30 → 30% is niet 30 euro. Reken eerst uit hoeveel 30% van 60 is. · €78 → Korting gaat eraf, niet erbij.
    - **Uitleg (Claude):** Korting: 30% van 60 = 18. Nieuwe prijs: 60 − 18 = €42.
  - `G7-VERH-02-claude-bank-003` (Claude V5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een wortel kost €60. Er is 50% korting. Wat is de nieuwe prijs in euro's?
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** €10 → 50% is niet 50 euro. Reken eerst uit hoeveel 50% van 60 is. · €90 → Korting gaat eraf, niet erbij.
    - **Uitleg (Claude):** Korting: 50% van 60 = 30. Nieuwe prijs: 60 − 30 = €30.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Hoeveel euro is de korting?
- **Hint 2 (te schrijven):** Reken eerst uit hoeveel euro de korting is: tien procent is een tiende deel van de prijs. Haal de korting daarna van de oude prijs af.
- **Ouderzin:** Je kind rekent een nieuwe prijs uit na korting in procenten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `procent van de prijs afgehaald` (Claudes sleutel: procent-verkeerde-basis) → Dat is de prijs min het procent. Maar de korting is een deel van de prijs: zoveel van de honderd.  [Claude, taalfix]
  - `korting niet goed verwerkt` (Claudes sleutel: verkeerde-bewerking) → Reken eerst de korting in euro uit. Haal je die daarna van de oude prijs af?  [Claude, taalfix]
  - `prijs min het procent` (Claudes sleutel (alle, zonder label)) → Dat is de prijs min het procent. Maar de korting is een deel van de prijs: zoveel van de honderd.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de korting in euro uit, en haal die van de oude prijs af.  [nieuw]
- Status: hints klaar
