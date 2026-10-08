# G4-MEET-E06 — Half en kwart op de klok

Onze omschrijving: Tijd: kwartier/half; hele/halve/kwartieren klok; maanden/seizoenen; kalender; lineair/cyclisch · in onze bank: 8 items

Claude-vragen gemapt: **209** in **17** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — half

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — half” (koppeling: claudeId)
- Items: **39** · Claude-doelen: M4 (22), M7 (17) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 39 items
- **Visual: nodig** (39 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (78)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-152` (Claude M4, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst half 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 30}, {"uur": 2, "minuut": 30}, {"uur": 6, "minuut": 0}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-180` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst half 1 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 12, "minuut": 30}, {"uur": 11, "minuut": 30}, {"uur": 6, "minuut": 0}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij half wijst de grote wijzer recht naar beneden. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Half betekent: een half uur vóór het hele uur. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind kiest de klok die een half uur aanwijst, zoals half vier.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij half wijst hij recht naar beneden.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij recht naar beneden? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 2: [klok] Hoe laat is het op deze klok? (opties in woorden) — half

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties in woorden) — half” (koppeling: claudeId)
- Items: **28** · Claude-doelen: M7 (18), M3 (10) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (28 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (56)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-084` (Claude M3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 8, "soort": "klok", "minuut": 30}`
    - **Opties:** A) half 11 · B) 8 uur · C) half 9
    - **Antwoord:** half 9  (controle: ok)
    - **Fout-hints (Claude):** 8 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · half 11 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-100` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 3, "soort": "klok", "minuut": 30}`
    - **Opties:** A) half 4 · B) half 5 · C) 6 uur
    - **Antwoord:** half 4  (controle: ok)
    - **Fout-hints (Claude):** 6 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · half 5 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij recht naar beneden, dan is het half.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Hij staat tussen twee getallen. Neem het getal waar hij naartoe gaat: het is half van dat uur.
- **Ouderzin:** Je kind leest een half uur af op een klok met wijzers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. Kijk naar de kleine wijzer: naar welk uur gaat hij nu? Het is half van dat uur.  [nieuw]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. Bij half kijk je naar het uur waar de kleine wijzer naartoe gaat, niet naar het uur dat net geweest is.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Kijk nog eens naar de grote wijzer. Hij wijst recht naar beneden: dan is het half.  [nieuw]
  - `andere klok` (andere fout) → Bij half wijst de grote wijzer recht naar beneden. Kijk naar de kleine wijzer: naar welk uur gaat hij? Het is half van dat uur.  [nieuw]
- Status: hints klaar

## Somtype 3: Het is # [ding]. Welke datum is het # [ding] later?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Het is # [ding]. Welke datum is het # [ding] later?” (koppeling: claudeId)
- Items: **27** · Claude-doelen: M10 (27) · regel: G19-kalender
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- Denkfouten (Claude): kalender-verkeerd-geteld (39), deel-vergeten-bij-splitsen (15)
- Verschillende Claude-fout-hints: 2 (meest: “Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-016` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 29 maart. Welke datum is het 5 dagen later?
    - **Opties:** A) 3 april · B) 6 april · C) 1 april
    - **Antwoord:** 3 april  (controle: ok)
    - **Fout-hints (Claude):** 1 april → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 6 april → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.
  - `G4-MEET-E06-claude-bank-026` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 30 juli. Welke datum is het 5 dagen later?
    - **Opties:** A) 3 augustus · B) 6 augustus · C) 4 augustus
    - **Antwoord:** 4 augustus  (controle: ok)
    - **Fout-hints (Claude):** 3 augustus → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 6 augustus → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.

- **Hint 1 (te schrijven):** Tel de dagen verder, één voor één. Tel op je vingers of op een kalender.
- **Hint 2 (te schrijven):** Tel eerst tot de laatste dag van de maand. Hoeveel dagen moet je dan nog? Tel die verder in de nieuwe maand.
- **Ouderzin:** Je kind telt een aantal dagen verder op de kalender, over het eind van de maand heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een dag ernaast` (fout = een dag ernaast) → Bijna! Dat is één dag ernaast. Tel de dagen nog eens, één voor één.  [nieuw]
  - `gestopt bij de maandgrens` (fout = gestopt op de eerste dag van de maand) → Je bent gestopt waar de nieuwe maand begint. Tel nog verder, tot je alle dagen hebt geteld.  [nieuw]
  - `andere datum` (andere fout) → Tel eerst tot de laatste dag van de maand. Tel daarna verder in de nieuwe maand. Kijk goed hoeveel dagen de maand heeft: dertig of eenendertig?  [nieuw]
- Status: hints klaar

## Somtype 4: Het is # [ding]. Welke datum was het # [ding] eerder?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Het is # [ding]. Welke datum was het # [ding] eerder?” (koppeling: claudeId)
- Items: **27** · Claude-doelen: M10 (27) · regel: G19-kalender
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- Denkfouten (Claude): kalender-verkeerd-geteld (42), deel-vergeten-bij-splitsen (12)
- Verschillende Claude-fout-hints: 2 (meest: “Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-040` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 2 april. Welke datum was het 5 dagen eerder?
    - **Opties:** A) 26 maart · B) 28 maart · C) 29 maart
    - **Antwoord:** 28 maart  (controle: ok)
    - **Fout-hints (Claude):** 29 maart → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 26 maart → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.
  - `G4-MEET-E06-claude-bank-046` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 3 juni. Welke datum was het 7 dagen eerder?
    - **Opties:** A) 26 mei · B) 27 mei · C) 24 mei
    - **Antwoord:** 27 mei  (controle: ok)
    - **Fout-hints (Claude):** 26 mei → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 24 mei → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.

- **Hint 1 (te schrijven):** Tel de dagen terug, één voor één. Tel op je vingers of op een kalender.
- **Hint 2 (te schrijven):** Tel terug tot de eerste dag van de maand. Daarna kom je bij de laatste dag van de maand ervoor. Tel daar verder terug.
- **Ouderzin:** Je kind telt een aantal dagen terug op de kalender, over het begin van de maand heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een dag ernaast` (fout = een dag ernaast) → Bijna! Dat is één dag ernaast. Tel de dagen nog eens, één voor één.  [nieuw]
  - `gestopt bij de maandgrens` (fout = gestopt op de laatste dag van de maand) → Je bent gestopt waar de maand ervoor eindigt. Tel nog verder terug, tot je alle dagen hebt geteld.  [nieuw]
  - `andere datum` (andere fout) → Na de eerste dag van de maand kom je bij de laatste dag van de maand ervoor. Tel daar verder terug. Kijk goed hoeveel dagen die maand heeft: dertig of eenendertig?  [nieuw]
- Status: hints klaar

## Somtype 5: [klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — kwart voor

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — kwart voor” (koppeling: claudeId)
- Items: **22** · Claude-doelen: M6 (22) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 22 items
- **Visual: nodig** (22 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (44)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-229` (Claude M6, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst kwart voor 1 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 9, "minuut": 0}, {"uur": 12, "minuut": 45}, {"uur": 1, "minuut": 45}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-223` (Claude M6, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst kwart voor 7 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 9, "minuut": 0}, {"uur": 6, "minuut": 45}, {"uur": 7, "minuut": 45}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij kwart voor wijst de grote wijzer naar de negen. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Kwart voor betekent: een kwartier vóór het hele uur. De kleine wijzer is dan bijna bij het uur uit de vraag, maar nog net ervoor.
- **Ouderzin:** Je kind kiest de klok die kwart voor een heel uur aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij kwart voor is de kleine wijzer bijna bij het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij kwart voor wijst hij naar de negen.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de negen? Kijk dan naar de kleine wijzer: is hij bijna bij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 6: [klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — kwart over

- Sleutel: nrOrigineel **6** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd in woorden) — kwart over” (koppeling: claudeId)
- Items: **20** · Claude-doelen: M6 (20) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 20 items
- **Visual: nodig** (20 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (40)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-209` (Claude M6, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst kwart over 7 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 7, "minuut": 15}, {"uur": 3, "minuut": 0}, {"uur": 8, "minuut": 15}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-191` (Claude M6, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst kwart over 5 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 3, "minuut": 0}, {"uur": 5, "minuut": 15}, {"uur": 6, "minuut": 15}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij kwart over wijst de grote wijzer naar de drie. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Kwart over betekent: een kwartier na het hele uur. De kleine wijzer is dan net voorbij het uur uit de vraag.
- **Ouderzin:** Je kind kiest de klok die kwart over een heel uur aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij kwart over is de kleine wijzer net voorbij het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij kwart over wijst hij naar de drie.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de drie? Kijk dan naar de kleine wijzer: is hij net voorbij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 7: [klok] Hoe laat is het op deze klok? (opties in woorden) — kwart over

- Sleutel: nrOrigineel **7** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties in woorden) — kwart over” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M7 (12) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (12 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (24)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-117` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 15}`
    - **Opties:** A) kwart over 2 · B) kwart over 3 · C) 3 uur
    - **Antwoord:** kwart over 2  (controle: ok)
    - **Fout-hints (Claude):** 3 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · kwart over 3 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-119` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 12, "soort": "klok", "minuut": 15}`
    - **Opties:** A) kwart over 1 · B) kwart over 12 · C) 3 uur
    - **Antwoord:** kwart over 12  (controle: ok)
    - **Fout-hints (Claude):** 3 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · kwart over 1 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij naar de drie, dan is het kwart over.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Welk getal is hij net voorbij? Het is kwart over dat uur.
- **Ouderzin:** Je kind leest kwart over af op een klok met wijzers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. De kleine wijzer is net voorbij een getal: het is kwart over dat uur, niet over het volgende.  [nieuw]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. Welk getal is de kleine wijzer net voorbij? Het is kwart over dat uur.  [nieuw]
  - `andere klok` (andere fout) → Bij kwart over wijst de grote wijzer naar de drie. De kleine wijzer is net voorbij een getal: het is kwart over dat uur.  [nieuw]
- Status: hints klaar

## Somtype 8: [klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — half

- Sleutel: nrOrigineel **8** · somtypeOrigineel “[klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — half” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M4 (5), M6 (3) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: kale
- Merge-fixlijst: #43 aanhalingstekens weg (7), #43 vóór één uur (1)
- Denkfouten (Claude): klok-verkeerd-gelezen (8)
- Verschillende Claude-fout-hints: 8 (meest: “Half twee is nog vóór twee uur. De kleine wijzer is nog niet bij de 2.”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-059` (Claude M4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet de klok op half twee.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 1:30  (controle: ok)
    - **Fout-hints (Claude):** 2:30 → "half twee" is nog vóór twee uur. De kleine wijzer is nog niet bij de 2.
    - **Uitleg (Claude):** Half twee: de grote wijzer op de 6, de kleine wijzer tussen de 1 en de 2.
  - `G4-MEET-E06-claude-bank-060` (Claude M6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op half één.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 12:30  (controle: ok)
    - **Fout-hints (Claude):** 1:30 → "half één" is nog vóór een uur. De kleine wijzer is nog niet bij de 1.
    - **Uitleg (Claude):** Half een: de grote wijzer op de 6, de kleine wijzer tussen de 12 en de 1.

- **Hint 1 (te schrijven):** Bij half zet je de grote wijzer recht naar beneden.
- **Hint 2 (te schrijven):** Half betekent: een half uur vóór het hele uur. Zet de kleine wijzer tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zet de wijzers van een klok op een half uur.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (Claudes sleutel: een uur te laat (tekst per item)) → "half …" is nog vóór … uur. De kleine wijzer is nog niet bij de ….  [Claude, ok]
  - `andere klok` (andere fout) → Bij half wijst de grote wijzer recht naar beneden. De kleine wijzer staat tussen het uur ervoor en het uur uit de vraag.  [nieuw]
- Status: hints klaar

## Somtype 9: [klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — kwart over

- Sleutel: nrOrigineel **9** · somtypeOrigineel “[klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — kwart over” (koppeling: claudeId)
- Items: **5** · Claude-doelen: M7 (3), M6 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: kale
- Denkfouten (Claude): klok-verkeerd-gelezen (5)
- Verschillende Claude-fout-hints: 5 (meest: “De kleine wijzer wijst naar de 8.”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-065` (Claude M6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op kwart over acht.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 8:15  (controle: ok)
    - **Fout-hints (Claude):** 9:15 → De kleine wijzer wijst naar de 8.
    - **Uitleg (Claude):** De grote wijzer geeft de minuten: elke streep is 5 minuten. 15 minuten is bij de 3. De kleine wijzer staat na de 8.
  - `G4-MEET-E06-claude-bank-067` (Claude M7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op kwart over één.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 1:15  (controle: ok)
    - **Fout-hints (Claude):** 2:15 → De kleine wijzer wijst naar de 1.
    - **Uitleg (Claude):** De grote wijzer geeft de minuten: elke streep is 5 minuten. 15 minuten is bij de 3. De kleine wijzer staat na de 1.

- **Hint 1 (te schrijven):** Bij kwart over zet je de grote wijzer naar de drie.
- **Hint 2 (te schrijven):** Kwart over betekent: een kwartier na het hele uur. Zet de kleine wijzer net voorbij het uur uit de vraag.
- **Ouderzin:** Je kind zet de wijzers van een klok op kwart over.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → De kleine wijzer staat een uur te ver. Bij kwart over zet je hem net voorbij het uur uit de vraag.  [nieuw]
  - `andere klok` (andere fout) → Bij kwart over wijst de grote wijzer naar de drie. De kleine wijzer staat net voorbij het uur uit de vraag.  [nieuw]
- Status: hints klaar

## Somtype 10: [klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — kwart voor

- Sleutel: nrOrigineel **10** · somtypeOrigineel “[klok-zetten (wijzers slepen)] Zet de klok op [tijd]. — kwart voor” (koppeling: claudeId)
- Items: **5** · Claude-doelen: M6 (4), M7 (1) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: kale
- Merge-fixlijst: #43 aanhalingstekens weg (4), #43 vóór één uur (1)
- Denkfouten (Claude): klok-verkeerd-gelezen (5)
- Verschillende Claude-fout-hints: 5 (meest: “Kwart voor vier is nog vóór vier uur. De kleine wijzer is nog niet bij de 4.”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-069` (Claude M6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op kwart voor vier.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 3:45  (controle: ok)
    - **Fout-hints (Claude):** 4:45 → "kwart voor vier" is nog vóór vier uur. De kleine wijzer is nog niet bij de 4.
    - **Uitleg (Claude):** De grote wijzer geeft de minuten: elke streep is 5 minuten. 45 minuten is bij de 9. De kleine wijzer staat na de 3.
  - `G4-MEET-E06-claude-bank-073` (Claude M7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op kwart voor tien.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 9:45  (controle: ok)
    - **Fout-hints (Claude):** 10:45 → "kwart voor tien" is nog vóór tien uur. De kleine wijzer is nog niet bij de 10.
    - **Uitleg (Claude):** De grote wijzer geeft de minuten: elke streep is 5 minuten. 45 minuten is bij de 9. De kleine wijzer staat na de 9.

- **Hint 1 (te schrijven):** Bij kwart voor zet je de grote wijzer naar de negen.
- **Hint 2 (te schrijven):** Kwart voor betekent: een kwartier vóór het hele uur. Zet de kleine wijzer bijna bij het uur uit de vraag, maar nog net ervoor.
- **Ouderzin:** Je kind zet de wijzers van een klok op kwart voor.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (Claudes sleutel: een uur te laat (tekst per item)) → "kwart voor …" is nog vóór … uur. De kleine wijzer is nog niet bij de ….  [Claude, ok]
  - `andere klok` (andere fout) → Bij kwart voor wijst de grote wijzer naar de negen. De kleine wijzer staat bijna bij het uur uit de vraag, maar nog net ervoor.  [nieuw]
- Status: hints klaar

## Somtype 11: [klok] Hoe laat is het op deze klok? (opties in woorden) — kwart voor

- Sleutel: nrOrigineel **11** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties in woorden) — kwart voor” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M7 (4) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (4 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (8)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-122` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 9, "soort": "klok", "minuut": 45}`
    - **Opties:** A) kwart voor 10 · B) 9 uur · C) kwart voor 11
    - **Antwoord:** kwart voor 10  (controle: ok)
    - **Fout-hints (Claude):** 9 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · kwart voor 11 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-121` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 11, "soort": "klok", "minuut": 45}`
    - **Opties:** A) kwart voor 12 · B) 9 uur · C) kwart voor 1
    - **Antwoord:** kwart voor 12  (controle: ok)
    - **Fout-hints (Claude):** 9 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · kwart voor 1 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij naar de negen, dan is het kwart voor.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Bij welk getal is hij bijna? Het is kwart voor dat uur.
- **Ouderzin:** Je kind leest kwart voor af op een klok met wijzers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. Bij welk getal is de kleine wijzer bijna? Het is kwart voor dat uur.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Kijk nog eens naar de grote wijzer. Hij wijst naar de negen: dan is het kwart voor.  [nieuw]
  - `andere klok` (andere fout) → Bij kwart voor wijst de grote wijzer naar de negen. De kleine wijzer is bijna bij het volgende getal: het is kwart voor dat uur.  [nieuw]
- Status: hints klaar

## Somtype 12: [klok] Hoe laat is het op deze klok? (opties digitaal) — half

- Sleutel: nrOrigineel **15** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties digitaal) — half” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-074` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 1, "soort": "klok", "minuut": 30}`
    - **Opties:** A) 1:30 · B) 2:30 · C) 12:30
    - **Antwoord:** 1:30  (controle: ok)
    - **Fout-hints (Claude):** 2:30 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 12:30 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-075` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 30}`
    - **Opties:** A) 3:30 · B) 1:30 · C) 2:30
    - **Antwoord:** 2:30  (controle: ok)
    - **Fout-hints (Claude):** 1:30 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 3:30 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij recht naar beneden, dan is het dertig minuten na het hele uur.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Welk getal is hij voorbij? Dat getal komt vóór de dubbele punt.
- **Ouderzin:** Je kind leest een half uur af op een klok met wijzers en kiest de digitale tijd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. De kleine wijzer is nog niet bij dat getal. Vóór de dubbele punt komt het getal dat hij voorbij is.  [nieuw]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. De kleine wijzer is al verder. Vóór de dubbele punt komt het getal dat hij voorbij is.  [nieuw]
  - `andere klok` (andere fout) → De kleine wijzer staat tussen twee getallen. Vóór de dubbele punt komt het getal dat hij voorbij is.  [nieuw]
- Status: hints klaar

## Somtype 13: [klok] Hoe laat is het op deze klok? (opties digitaal) — kwart over

- Sleutel: nrOrigineel **16** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties digitaal) — kwart over” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-076` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 1, "soort": "klok", "minuut": 15}`
    - **Opties:** A) 2:15 · B) 1:15 · C) 12:15
    - **Antwoord:** 1:15  (controle: ok)
    - **Fout-hints (Claude):** 12:15 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 2:15 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-077` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 15}`
    - **Opties:** A) 3:15 · B) 2:15 · C) 1:15
    - **Antwoord:** 2:15  (controle: ok)
    - **Fout-hints (Claude):** 3:15 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 1:15 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij naar de drie, dan is het vijftien minuten na het hele uur.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Welk getal is hij net voorbij? Dat getal komt vóór de dubbele punt.
- **Ouderzin:** Je kind leest kwart over af op een klok met wijzers en kiest de digitale tijd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. De kleine wijzer is nog niet bij dat getal. Vóór de dubbele punt komt het getal dat hij net voorbij is.  [nieuw]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. De kleine wijzer is al verder. Vóór de dubbele punt komt het getal dat hij net voorbij is.  [nieuw]
  - `andere klok` (andere fout) → De kleine wijzer is net voorbij een getal. Dat getal komt vóór de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 14: [klok] Hoe laat is het op deze klok? (opties digitaal) — kwart voor

- Sleutel: nrOrigineel **17** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties digitaal) — kwart voor” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klok” (parameters in jsRender)
- Denkfouten (Claude): klok-verkeerd-gelezen (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-079` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 1, "soort": "klok", "minuut": 45}`
    - **Opties:** A) 2:45 · B) 12:45 · C) 1:45
    - **Antwoord:** 1:45  (controle: ok)
    - **Fout-hints (Claude):** 12:45 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 2:45 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-078` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 45}`
    - **Opties:** A) 2:45 · B) 3:45 · C) 1:45
    - **Antwoord:** 2:45  (controle: ok)
    - **Fout-hints (Claude):** 3:45 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 1:45 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer. Wijst hij naar de negen, dan is het vijfenveertig minuten na het hele uur.
- **Hint 2 (te schrijven):** Kijk dan naar de kleine wijzer. Hij is bijna bij het volgende getal, maar nog niet. Vóór de dubbele punt komt het getal dat hij voorbij is.
- **Ouderzin:** Je kind leest kwart voor af op een klok met wijzers en kiest de digitale tijd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. De kleine wijzer is bijna bij dat getal, maar nog niet. Vóór de dubbele punt komt het getal dat hij al voorbij is.  [nieuw]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. De kleine wijzer is al verder. Vóór de dubbele punt komt het getal dat hij al voorbij is.  [nieuw]
  - `andere klok` (andere fout) → Bij kwart voor is de kleine wijzer bijna bij het volgende getal. Vóór de dubbele punt komt het getal dat hij al voorbij is.  [nieuw]
- Status: hints klaar

## Somtype 15: [klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — half

- Sleutel: nrOrigineel **12** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — half” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 2 items
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Merge-fixlijst: #39 klok 1:06 → 1:00 (1), #39 klok 2:06 → 2:00 (1)
- Denkfouten (Claude): klok-verkeerd-gelezen (2)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-127` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 2:30 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 0}, {"uur": 2, "minuut": 30}, {"uur": 3, "minuut": 30}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-125` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 1:30 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 0}, {"uur": 2, "minuut": 30}, {"uur": 1, "minuut": 30}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Achter de dubbele punt staat hoeveel minuten na het hele uur het is. Dertig minuten is een half uur: de grote wijzer wijst recht naar beneden.
- **Hint 2 (te schrijven):** Vóór de dubbele punt staat het uur dat geweest is. De kleine wijzer staat dan tussen dat uur en het volgende uur.
- **Ouderzin:** Je kind kiest de klok met wijzers die bij een digitale tijd met dertig minuten hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. De kleine wijzer staat tussen het uur vóór de dubbele punt en het volgende uur.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij dertig minuten wijst hij recht naar beneden.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok eerst naar de grote wijzer: bij dertig minuten wijst hij recht naar beneden. De kleine wijzer staat tussen het uur vóór de dubbele punt en het volgende uur.  [nieuw]
- Status: hints klaar

## Somtype 16: [klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — kwart over

- Sleutel: nrOrigineel **13** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — kwart over” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 2 items
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Merge-fixlijst: #39 klok 1:03 → 1:00 (1), #39 klok 2:03 → 2:00 (1)
- Denkfouten (Claude): klok-verkeerd-gelezen (2)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-130` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 2:15 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 0}, {"uur": 3, "minuut": 15}, {"uur": 2, "minuut": 15}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-128` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 1:15 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 15}, {"uur": 1, "minuut": 0}, {"uur": 2, "minuut": 15}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Achter de dubbele punt staat hoeveel minuten na het hele uur het is. Vijftien minuten is een kwartier: de grote wijzer wijst naar de drie.
- **Hint 2 (te schrijven):** Vóór de dubbele punt staat het uur. De kleine wijzer is dan net voorbij dat uur.
- **Ouderzin:** Je kind kiest de klok met wijzers die bij een digitale tijd met vijftien minuten hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. De kleine wijzer is net voorbij het uur vóór de dubbele punt.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij vijftien minuten wijst hij naar de drie.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok eerst naar de grote wijzer: bij vijftien minuten wijst hij naar de drie. De kleine wijzer is net voorbij het uur vóór de dubbele punt.  [nieuw]
- Status: hints klaar

## Somtype 17: [klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — kwart voor

- Sleutel: nrOrigineel **14** · somtypeOrigineel “[klokkenrij] Welke klok wijst [tijd] aan? (tijd digitaal) — kwart voor” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M7 (2) · regel: G15-klok
- Getallenruimte: hele/halve uren, kwartieren; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 2 items
- **Visual: nodig** (2 items): Claude-tekenaar: soort “klokkenrij” (parameters in jsRender)
- Merge-fixlijst: #39 klok 1:09 → 1:00 (1), #39 klok 2:09 → 2:00 (1)
- Denkfouten (Claude): klok-verkeerd-gelezen (2)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G4-MEET-E06-claude-bank-134` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 1:45 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 0}, {"uur": 2, "minuut": 45}, {"uur": 1, "minuut": 45}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G4-MEET-E06-claude-bank-132` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 2:45 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 0}, {"uur": 2, "minuut": 45}, {"uur": 3, "minuut": 45}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Achter de dubbele punt staat hoeveel minuten na het hele uur het is. Bij vijfenveertig minuten is het kwart voor het volgende uur: de grote wijzer wijst naar de negen.
- **Hint 2 (te schrijven):** Vóór de dubbele punt staat het uur dat geweest is. De kleine wijzer is dan bijna bij het volgende uur.
- **Ouderzin:** Je kind kiest de klok met wijzers die bij een digitale tijd met vijfenveertig minuten hoort.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. De kleine wijzer is bijna bij het volgende uur, maar nog net ervoor.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij vijfenveertig minuten wijst hij naar de negen.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok eerst naar de grote wijzer: bij vijfenveertig minuten wijst hij naar de negen. De kleine wijzer is bijna bij het volgende uur, maar nog net ervoor.  [nieuw]
- Status: hints klaar
