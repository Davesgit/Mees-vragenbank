# G7-VERH-04 — Breuk, procent en verhouding koppelen

Onze omschrijving: Breuk ↔ % ↔ verhouding · in onze bank: 8 items

Claude-vragen gemapt: **137** in **7** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Schrijf #/# in procenten.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Schrijf #/# in procenten.” (koppeling: claudeId)
- Items: **110** · Claude-doelen: B13 (110) · regel: G7-V01-breuk-procent
- Getallenruimte: breuken (noemer tot 10), breuken (noemer tot 2), breuken (noemer tot 20), breuken (noemer tot 25), breuken (noemer tot 4), breuken (noemer tot 40), breuken (noemer tot 5), breuken (noemer tot 50), breuken (noemer tot 8) · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (109), nul-fout-tientallen (100), omgekeerd-gedeeld (11)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-091` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 1/2 in procenten.
    - **Opties:** A) 5% · B) 50% · C) 500%
    - **Antwoord:** 50%  (controle: ok)
    - **Fout-hints (Claude):** 500% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan. · 5% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.
  - `G7-VERH-04-claude-bank-022` (Claude B13, bank, niveau 3 → toepassen)
    - **Opgave:** Schrijf 14/40 in procenten.
    - **Opties:** A) 350% · B) 35% · C) 40%
    - **Antwoord:** 35%  (controle: ok)
    - **Fout-hints (Claude):** 350% → Kijk goed naar de nullen. Reken eerst de tafelsom, plak daarna de nul(len) er weer aan.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Een breuk met honderd als noemer kun je zo als procent schrijven.
- **Hint 2 (te schrijven):** Maak een verhoudingstabel. Zet de noemer bij honderd procent en de teller bij het procent dat je zoekt. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde. Lukt dat niet in één keer? Deel dan eerst de teller en de noemer door hetzelfde getal, tot de noemer wel in één keer naar honderd gaat.
- **Ouderzin:** Je kind schrijft een breuk als procent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer ernaast` (Claudes sleutel: nul-fout-tientallen) → Dat is tien keer te groot of te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.  [Claude, taalfix]
  - `noemer door teller` (Claudes sleutel: omgekeerd-gedeeld) → Heb je de noemer door de teller gedeeld? De teller is het deel: die hoort bij het procent dat je zoekt.  [Claude, taalfix]
  - `teller met procentteken` (fout = het deel zelf (als %)) → Dat is de teller met een procentteken. Dat klopt alleen als de noemer honderd is. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.  [nieuw]
  - `noemer met procentteken` (Claudes sleutel: getal-overgenomen) → Dat is de noemer. Die hoort bij honderd procent. Welk procent hoort bij de teller?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.  [nieuw]
- Status: hints klaar

## Somtype 2: Schrijf # in procenten.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Schrijf # in procenten.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B13 (8) · regel: G7-V01-breuk-procent
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): komma-verschoven (12), getal-overgenomen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-007` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,1 in procenten.
    - **Opties:** A) 100% · B) 1% · C) 10%
    - **Antwoord:** 10%  (controle: ok)
    - **Fout-hints (Claude):** 100% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 1% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G7-VERH-04-claude-bank-008` (Claude B13, bank, niveau 2 → toepassen)
    - **Opgave:** Schrijf 0,5 in procenten.
    - **Opties:** A) 50% · B) 0,5% · C) 5%
    - **Antwoord:** 50%  (controle: ok)
    - **Fout-hints (Claude):** 500% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 5% → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Het cijfer direct achter de komma geeft de tienden, het cijfer daarna de honderdsten.
- **Hint 2 (te schrijven):** Procent zijn honderdsten. Zet een nul achter het cijfer na de komma: dan lees je hoeveel honderdsten het zijn.
- **Ouderzin:** Je kind schrijft een kommagetal als procent.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma goed? Procent zijn honderdsten: hoeveel honderdsten is het kommagetal?  [Claude, taalfix]
  - `kommagetal met procentteken` (fout = kommagetal met procentteken) → Dat is het kommagetal met een procentteken erachter. Procent zijn honderdsten: hoeveel honderdsten is het kommagetal?  [nieuw]
  - `andere fout` (andere fout) → Procent zijn honderdsten: hoeveel honderdsten is het kommagetal?  [nieuw]
- Status: hints klaar

## Somtype 3: #% van de [ding] is kapot. Schrijf dat als kommagetal.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “#% van de [ding] is kapot. Schrijf dat als kommagetal.” (koppeling: claudeId)
- Items: **6** · Claude-doelen: B13 (6) · regel: G7-V01-breuk-procent
- Getallenruimte: procenten · type: kale
- Denkfouten (Claude): komma-verschoven (6), kommagetal-als-geheel (6)
- Verschillende Claude-fout-hints: 5 (meest: “Procent is per honderd: de komma schuift twee plekken naar links, niet één.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-004` (Claude B13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 50% van de borden is kapot. Schrijf dat als kommagetal.
    - **Antwoord:** 0,5  (controle: ok)
    - **Fout-hints (Claude):** 5 → Procent is per honderd: de komma schuift twee plekken naar links, niet één. · 50 → 50% is 50 van de 100. Als kommagetal deel je door 100.
    - **Uitleg (Claude):** Procent is per honderd: 50 : 100 = 0,50.
  - `G7-VERH-04-claude-bank-002` (Claude B13, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 50% van de lampjes is kapot. Schrijf dat als kommagetal.
    - **Antwoord:** 0,5  (controle: ok)
    - **Fout-hints (Claude):** 5 → Procent is per honderd: de komma schuift twee plekken naar links, niet één. · 50 → 50% is 50 van de 100. Als kommagetal deel je door 100.
    - **Uitleg (Claude):** Procent is per honderd: 50 : 100 = 0,50.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Zoveel honderdsten kun je als kommagetal schrijven.
- **Hint 2 (te schrijven):** Procent zijn honderdsten. Schrijf het als kommagetal: het cijfer direct achter de komma geeft de tienden, het cijfer daarna de honderdsten. Is er geen heel getal? Zet dan een nul voor de komma. Een nul aan het eind achter de komma mag weg.
- **Ouderzin:** Je kind schrijft een procent als kommagetal.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tien keer te groot` (fout = antwoord × 10) → Dat is tien keer te groot. Procent zijn honderdsten: deel het getal van het procent door honderd.  [nieuw]
  - `procent zonder komma` (fout = een getal uit de vraag) → Dat is het getal van het procent. Als kommagetal is het honderd keer zo klein.  [nieuw]
  - `andere fout` (andere fout) → Deel het getal van het procent door honderd.  [nieuw]
- Status: hints klaar

## Somtype 4: Deel van een totaal: welk deel van de [ding] is …? ('zoveel op de zoveel')

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Deel van een totaal: welk deel van de [ding] is …? ('zoveel op de zoveel')” (koppeling: claudeId)
- Items: **7** · Claude-doelen: G7 (7) · regel: D-KANS-NAAR-DEEL
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-van-geheel-verkeerd (6), andere-deel-genomen (4), getal-overgenomen (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 10 (meest: “Kijk goed naar welke kleur er in de vraag wordt gevraagd.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-132` (Claude G7, ai, niveau 1 → basis)
    - **Opgave:** In een zakje zitten 3 rode en 7 blauwe knikkers. Welk deel van de knikkers is rood?
    - **Opties:** A) 7 op de 10 · B) 3 op de 10 · C) 3 op de 7
    - **Antwoord:** 3 op de 10  (controle: ok)
    - **Fout-hints (Claude):** 7 op de 10 → Kijk goed naar welke kleur er in de vraag wordt gevraagd. · 3 op de 7 → Je moet het aantal rode knikkers vergelijken met alle knikkers samen, niet met de blauwe.
    - **Uitleg (Claude):** In het zakje zitten samen 3 + 7 = 10 knikkers. Daarvan zijn er 3 rood. Dat is dus 3 op de 10.
  - `G7-VERH-04-claude-bank-127` (Claude G7, ai, niveau 2 → toepassen)
    - **Opgave:** In een doos liggen 20 kaartjes en op 5 kaartjes staat een ster. Welk deel van de kaartjes heeft een ster?
    - **Opties:** A) 5 op de 15 · B) 5 op de 20 · C) 1 op de 5
    - **Antwoord:** 5 op de 20  (controle: ok)
    - **Fout-hints (Claude):** 5 op de 15 → Vergelijk de sterkaartjes met alle kaartjes, niet met de kaartjes zonder ster. · 1 op de 5 → Het aantal sterren is niet meteen het antwoord. Kijk hoe vaak 5 in 20 past.
    - **Uitleg (Claude):** Er zijn in totaal 20 kaartjes. Op 5 daarvan staat een ster. Dat is dus 5 op de 20.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Deel van een totaal: hoeveel procent van de [ding] is …?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Deel van een totaal: hoeveel procent van de [ding] is …?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: G7 (3) · regel: D-KANS-NAAR-DEEL
- Getallenruimte: procenten · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (3), procent-verkeerde-basis (2), andere-deel-genomen (1)
- Verschillende Claude-fout-hints: 4 (meest: “Het aantal rode ballen is niet meteen het percentage. Denk aan hoeveel ballen er in totaal zijn.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-126` (Claude G7, ai, niveau 2 → toepassen)
    - **Opgave:** In een bak liggen 10 ballen en 5 daarvan zijn rood. Hoeveel procent van de ballen is rood?
    - **Opties:** A) 50% · B) 5% · C) 10%
    - **Antwoord:** 50%  (controle: ok)
    - **Fout-hints (Claude):** 5% → Het aantal rode ballen is niet meteen het percentage. Denk aan hoeveel ballen er in totaal zijn. · 10% → Kijk welk deel van de tien ballen rood is en zet dat om naar procenten.
    - **Uitleg (Claude):** 5 van de 10 ballen is rood, dus de helft. De helft is 50%. Dat is dus 50%.
  - `G7-VERH-04-claude-bank-130` (Claude G7, ai, niveau 2 → toepassen)
    - **Opgave:** In een pot zitten 30 lootjes en 6 daarvan geven een prijs. Hoeveel procent van de lootjes geeft een prijs?
    - **Opties:** A) 24% · B) 20% · C) 6%
    - **Antwoord:** 20%  (controle: ok)
    - **Fout-hints (Claude):** 24% → Je hebt gerekend met de lootjes zonder prijs. Lees nog eens wat er gevraagd wordt. · 6% → Het aantal prijslootjes is niet meteen het percentage. Kijk naar het deel van het totaal.
    - **Uitleg (Claude):** 6 van de 30 lootjes geeft een prijs. 30 : 6 = 5, dus dat is een vijfde deel. Een vijfde van 100 is 20, dus 20%.

- **Hint 1 (te schrijven):** Procent (%) betekent: zoveel van de honderd. Het hele aantal is honderd procent.
- **Hint 2 (te schrijven):** Maak een verhoudingstabel: het hele aantal hoort bij honderd procent. Reken uit hoeveel procent bij het deel hoort.
- **Ouderzin:** Je kind rekent uit hoeveel procent een deel van het geheel is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getallen achter elkaar` (fout = getallen achter elkaar (als %)) → Heb je de getallen achter elkaar gezet? Samen zeggen ze welk deel van het hele aantal het is. Hoeveel is dat van de honderd?  [nieuw]
  - `het deel zelf` (Claudes sleutel: getal-overgenomen) → Dat is het aantal van het deel. Procent is zoveel van de honderd: hoeveel procent is dat deel?  [Claude, taalfix]
  - `het hele aantal` (Claudes sleutel: procent-verkeerde-basis) → Dat is het hele aantal. Het hele aantal is honderd procent. Hoeveel procent is het deel?  [Claude, taalfix]
  - `het andere deel` (Claudes sleutel: andere-deel-genomen) → Dat is het aantal van het andere deel. Hoeveel procent is het deel waar de vraag over gaat?  [Claude, taalfix]
  - `andere fout` (andere fout) → Het hele aantal is honderd procent. Hoeveel procent is het deel?  [nieuw]
- Status: hints klaar

## Somtype 6: Deel van een totaal: in welke zak is het deel het grootst? (delen vergelijken)

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Deel van een totaal: in welke zak is het deel het grootst? (delen vergelijken)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G7 (1) · regel: D-KANS-NAAR-DEEL
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verhoudingstabel-verkeerd (1), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 2 (meest: “Reken voor allebei uit welk deel van de knikkers rood is en vergelijk die delen.”)
- Voorbeelden:
  - `G7-VERH-04-claude-bank-133` (Claude G7, ai, niveau 2 → toepassen)
    - **Opgave:** In zak A zijn 2 van de 4 knikkers rood. In zak B zijn 3 van de 9 knikkers rood. In welke zak is het deel rode knikkers het grootst?
    - **Opties:** A) Even groot · B) Zak A · C) Zak B
    - **Antwoord:** Zak A  (controle: ok)
    - **Fout-hints (Claude):** Even groot → Reken voor allebei uit welk deel van de knikkers rood is en vergelijk die delen. · Zak B → Kijk niet alleen naar het aantal rode knikkers, maar ook naar het totaal in de zak.
    - **Uitleg (Claude):** In zak A is 2 van de 4 rood, dat is de helft. In zak B is 3 van de 9 rood, dat is een derde. De helft is meer dan een derde, dus zak A.

- **Hint 1 (te schrijven):** Een deel vergelijk je met het hele aantal: hoeveel is het van het geheel?
- **Hint 2 (te schrijven):** Schrijf elk deel als breuk: het deel boven de streep, het hele aantal eronder. Welke breuk is groter? Je kunt elke breuk vergelijken met een half.
- **Ouderzin:** Je kind vergelijkt twee delen die bij een verschillend totaal horen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen het deel` (Zak B) → Heb je alleen naar het deel gekeken? Vergelijk het deel met het hele aantal in elke zak.  [nieuw]
  - `even groot` (Even groot) → Reken het na: schrijf elk deel als breuk. Zijn de breuken even groot?  [nieuw]
  - `andere fout` (andere fout) → Vergelijk het deel met het hele aantal in elke zak.  [nieuw]
- Status: hints klaar

## Somtype 7: [rad] Deel van een totaal: welk deel van de vakjes is …? ('zoveel op de zoveel')

- Sleutel: nrOrigineel **7** · somtypeOrigineel “[rad] Deel van een totaal: welk deel van de vakjes is …? ('zoveel op de zoveel')” (koppeling: claudeId)
- Items: **2** · Claude-doelen: G7 (2) · regel: D-KANS-NAAR-DEEL
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): deel-van-geheel-verkeerd (2), andere-deel-genomen (1), getal-overgenomen (1)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G7-VERH-04-claude-bank-137` (Claude G7, ai, niveau 1 → basis)
    - **Opgave:** Een rad heeft 8 even grote vakjes. Twee vakjes zijn groen. Welk deel van de vakjes is groen?
    - **Tekening:** `{"soort": "rad", "vakjes": 8, "gemarkeerd": {"aantal": 2, "kleur": "groen", "letter": "G", "patroon": "gestreept"}, "pijl": false}`
    - **Opties:** A) 6 op de 8 · B) 2 op de 8 · C) 2 op de 6
    - **Antwoord:** 2 op de 8  (controle: ok)
    - **Fout-hints (Claude):** 2 op de 6 → Tel alle vakjes van het rad, ook de groene. · 6 op de 8 → Je hebt de vakjes geteld die niet groen zijn. Lees nog eens wat er gevraagd wordt.
    - **Uitleg (Claude):** Het rad heeft in totaal 8 vakjes. Daarvan zijn er 2 groen. Dat is dus 2 op de 8.
  - `G7-VERH-04-claude-bank-136` (Claude G7, ai, niveau 3 → toepassen)
    - **Opgave:** Een rad heeft 12 even grote vakjes en 3 daarvan zijn rood. Welk deel van de vakjes is rood?
    - **Tekening:** `{"soort": "rad", "vakjes": 12, "gemarkeerd": {"aantal": 3, "kleur": "rood", "letter": "R", "patroon": "gestreept"}, "pijl": false}`
    - **Opties:** A) 3 op de 12 · B) 1 op de 3 · C) 3 op de 9
    - **Antwoord:** 3 op de 12  (controle: ok)
    - **Fout-hints (Claude):** 1 op de 3 → Het aantal rode vakjes is niet meteen het antwoord. Kijk hoe vaak 3 in 12 past. · 3 op de 9 → Tel alle vakjes van het rad, ook de rode.
    - **Uitleg (Claude):** Het rad heeft in totaal 12 vakjes. Daarvan zijn er 3 rood. Dat is dus 3 op de 12.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
