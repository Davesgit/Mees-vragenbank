# G5-MEET-E06 — Tijd tot op de minuut

Onze omschrijving: Tijd tot op de minuut; etmaal/60-tallig; tijdsduur; kalenderperiodes · in onze bank: 8 items

Claude-vragen gemapt: **1051** in **24** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Hoeveel minuten duurt het van #.# uur tot #.# uur?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoeveel minuten duurt het van #:# uur tot #:# uur?” (koppeling: claudeId)
- Items: **220** · Claude-doelen: M14 (220) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen-te-weinig (193), tijd-als-kommagetal-te-veel (77), deel-vergeten-bij-splitsen-te-veel (76), kleinste-van-grootste-te-veel (74), uur-te-veel (11), uur-te-weinig (9)
- Verschillende Claude-fout-hints: 2 (meest: “Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-643` (Claude M14, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel minuten duurt het van 7.15 uur tot 8.00 uur?
    - **Antwoord:** 45  (controle: ok)
    - **Fout-hints (Claude):** 60 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G5-MEET-E06-claude-bank-826` (Claude M14, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel minuten duurt het van 8.25 uur tot 9.10 uur?
    - **Antwoord:** 45  (controle: ok)
    - **Fout-hints (Claude):** 85 → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur. · 15 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Tel eerst de minuten tot het volgende hele uur.
- **Hint 2 (te schrijven):** Tel de minuten tot het volgende hele uur, en tel daarna de hele uren erbij, als die er zijn: elk uur is zestig minuten. Tel tot slot de minuten na het laatste hele uur erbij, als die er zijn.
- **Ouderzin:** Je kind rekent uit hoeveel minuten het is van de ene tijd tot de andere, over het hele uur heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te veel` (fout = antwoord + 60) → Dat is zestig minuten te veel: een heel uur. Tel in stukken: eerst de minuten tot het volgende hele uur. Dan de hele uren van zestig minuten, als die er zijn. Dan de minuten die nog over zijn.  [nieuw]
  - `een uur te weinig` (fout = antwoord − 60) → Dat is zestig minuten te weinig: een heel uur. Heb je alle hele uren meegeteld?  [nieuw]
  - `honderd minuten` (Claudes sleutel: tijd-als-kommagetal) → Dat is te veel. Heb je gerekend alsof een uur honderd minuten heeft? Een uur heeft zestig minuten.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Tel in stukken: eerst de minuten tot het volgende hele uur. Dan de hele uren, als die er zijn. Dan de minuten die nog over zijn.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Heb je alle stukken opgeteld? Tel in stukken: eerst de minuten tot het volgende hele uur. Dan de hele uren, als die er zijn. Dan de minuten die nog over zijn.  [nieuw]
  - `andere fout` (andere fout) → Tel in stukken: eerst de minuten tot het volgende hele uur. Dan de hele uren, als die er zijn. Dan de minuten die nog over zijn. Een uur heeft zestig minuten.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Hoeveel minuten duurt het van #:# uur tot #:# uur?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 2: [klokkenrij] Welke klok wijst #:# [ding]? (tijd digitaal)

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[klokkenrij] Welke klok wijst #:# [ding]? (tijd digitaal)” (koppeling: claudeId)
- Items: **115** · Claude-doelen: M7 (115) · regel: G15-klok, FX-G4-45
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 115 items
- Denkfouten (Claude): uur-te-laat (115), 5-minuten-te-laat (103), grote-wijzer-verkeerd (12)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1001` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 8:36 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 9, "minuut": 36}, {"uur": 8, "minuut": 41}, {"uur": 8, "minuut": 36}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1019` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst 1:42 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 42}, {"uur": 1, "minuut": 47}, {"uur": 1, "minuut": 42}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Achter de dubbele punt staan de minuten na het hele uur. Bij de grote wijzer is elk getal vijf minuten: bij de één vijf minuten, bij de twee tien minuten.
- **Hint 2 (te schrijven):** Vóór de dubbele punt staat het uur dat geweest is. Is dat dertien of meer? Haal er dan twaalf af: veertien uur is twee uur op de klok. De kleine wijzer staat tussen dat uur en het volgende uur.
- **Ouderzin:** Je kind zoekt de klok met wijzers die een digitale tijd aanwijst, op de minuut.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. De kleine wijzer staat tussen het uur dat geweest is en het volgende uur. Is het uur dertien of meer? Haal er dan eerst twaalf af.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Tel bij de grote wijzer vijf minuten per getal, en daarna de streepjes: één minuut per streepje.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok eerst naar de grote wijzer: vijf minuten per getal, en één minuut per streepje. Kijk dan naar de kleine wijzer: staat hij tussen het uur dat geweest is en het volgende uur? Is het uur dertien of meer, haal er dan eerst twaalf af.  [nieuw]
- Status: hints klaar

## Somtype 3: Het is #.# uur. Hoe laat is het # minuten later? (Typ als 14.30.)

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Het is #:# uur. Hoe laat is het # minuten later?” (koppeling: claudeId)
- Items: **110** · Claude-doelen: M14 (110) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): grote-wijzer-verkeerd (110), 15-minuten-te-laat (34), 5-minuten-te-laat (24), 10-minuten-te-laat (17), 5-minuten-te-vroeg (16), 10-minuten-te-vroeg (10), 15-minuten-te-vroeg (9)
- Verschillende Claude-fout-hints: 2 (meest: “Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-178` (Claude M14, bank, niveau 2 → toepassen)
    - **Opgave:** Het is 8.40 uur. Hoe laat is het 25 minuten later?
    - **Antwoord:** 9.05 uur  (controle: ok)
    - **Fout-hints (Claude):** 9.00 uur → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 9.40 uur → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.
  - `G5-MEET-E06-claude-bank-271` (Claude M14, bank, niveau 2 → toepassen)
    - **Opgave:** Het is 9.40 uur. Hoe laat is het 45 minuten later?
    - **Antwoord:** 10.25 uur  (controle: ok)
    - **Fout-hints (Claude):** 10.40 uur → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur. · 10.45 uur → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.

- **Hint 1 (te schrijven):** Hoeveel minuten is het nog tot het volgende hele uur? Begin daarmee.
- **Hint 2 (te schrijven):** Tel eerst door tot het hele uur. Hoeveel minuten moet je daarna nog? Tel die verder na het hele uur.
- **Ouderzin:** Je kind rekent uit hoe laat het is een aantal minuten later, over het hele uur heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gestopt bij het hele uur` (Claudes sleutel: deel-vergeten-bij-splitsen) → Je bent gestopt bij het hele uur. Er moeten nog minuten bij: tel verder na het hele uur.  [Claude, taalfix]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. Je gaat over het hele uur heen: dan komt er een uur bij.  [nieuw]
  - `te laat` (Claudes sleutel: tijd-als-kommagetal) → Dat is te laat. Een uur heeft zestig minuten. Tel eerst tot het hele uur en tel daarna de rest verder.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een uur heeft zestig minuten. Tel eerst tot het volgende hele uur. Tel daarna de minuten die nog over zijn verder.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Het is #:# uur. Hoe laat is het # minuten later?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 4: Het is #.# uur. Hoe laat was het # minuten eerder? (Typ als 14.30.)

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Het is #:# uur. Hoe laat was het # minuten eerder?” (koppeling: claudeId)
- Items: **110** · Claude-doelen: M14 (110) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): grote-wijzer-verkeerd (103), 15-minuten-te-vroeg (28), deel-vergeten-bij-splitsen (23), 5-minuten-te-vroeg (18), 5-minuten-te-laat (14), 15-minuten-te-laat (13), 10-minuten-te-vroeg (13), 10-minuten-te-laat (8)
- Verschillende Claude-fout-hints: 2 (meest: “Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-322` (Claude M14, bank, niveau 2 → toepassen)
    - **Opgave:** Het is 9.05 uur. Hoe laat was het 30 minuten eerder?
    - **Antwoord:** 8.35 uur  (controle: ok)
    - **Fout-hints (Claude):** 9.00 uur → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 8.05 uur → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.
  - `G5-MEET-E06-claude-bank-283` (Claude M14, bank, niveau 2 → toepassen)
    - **Opgave:** Het is 9.35 uur. Hoe laat was het 45 minuten eerder?
    - **Antwoord:** 8.50 uur  (controle: ok)
    - **Fout-hints (Claude):** 9.00 uur → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 8.35 uur → Een uur heeft 60 minuten, geen 100. Reken via het volgende hele uur.

- **Hint 1 (te schrijven):** Hoeveel minuten is het na het hele uur? Tel eerst terug tot dat hele uur.
- **Hint 2 (te schrijven):** Tel eerst terug tot het hele uur. Hoeveel minuten moet je vanaf het hele uur nog terug? Tel die er ook af. Een uur heeft zestig minuten.
- **Ouderzin:** Je kind rekent uit hoe laat het was een aantal minuten eerder, over het hele uur heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gestopt bij het hele uur` (Claudes sleutel: deel-vergeten-bij-splitsen) → Je bent gestopt bij het hele uur. Je moet nog verder terug: tel de rest terug vanaf het hele uur.  [Claude, taalfix]
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. Je gaat terug over het hele uur heen: dan gaat er een uur af.  [nieuw]
  - `te vroeg` (Claudes sleutel: tijd-als-kommagetal) → Dat is te vroeg. Een uur heeft zestig minuten. Tel eerst terug tot het hele uur en tel daarna de rest verder terug.  [Claude, taalfix]
  - `andere fout` (andere fout) → Een uur heeft zestig minuten. Tel eerst terug tot het hele uur. Tel daarna de minuten die nog over zijn verder terug.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Het is #:# uur. Hoe laat was het # minuten eerder?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 5: Het is # [ding]. Welke datum is het # dagen later?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Het is # [ding]. Welke datum is het # dagen later?” (koppeling: claudeId)
- Items: **83** · Claude-doelen: M10 (83) · regel: G19-kalender
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): kalender-verkeerd-geteld (126), deel-vergeten-bij-splitsen (40)
- Verschillende Claude-fout-hints: 2 (meest: “Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-058` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 24 maart. Welke datum is het 10 dagen later?
    - **Opties:** A) 3 april · B) 11 april · C) 4 april
    - **Antwoord:** 3 april  (controle: ok)
    - **Fout-hints (Claude):** 4 april → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 11 april → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.
  - `G5-MEET-E06-claude-bank-032` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 20 augustus. Welke datum is het 15 dagen later?
    - **Opties:** A) 5 september · B) 3 september · C) 4 september
    - **Antwoord:** 4 september  (controle: ok)
    - **Fout-hints (Claude):** 5 september → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 3 september → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.

- **Hint 1 (te schrijven):** Tel eerst tot de laatste dag van de maand. Hoeveel dagen heeft die maand: dertig of eenendertig?
- **Hint 2 (te schrijven):** Tel eerst tot de laatste dag van de maand, en schrijf op hoeveel dagen dat zijn. Tel de rest verder in de nieuwe maand.
- **Ouderzin:** Je kind telt een aantal dagen verder op de kalender, over het eind van de maand heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gestopt bij de maandgrens` (fout = gestopt op de eerste dag van de maand) → Je bent gestopt waar de nieuwe maand begint. Tel nog verder, tot je alle dagen hebt geteld.  [nieuw]
  - `een dag later` (fout = een dag later) → Bijna! Je bent één dag te ver geteld. Hoeveel dagen heeft de maand: dertig of eenendertig?  [nieuw]
  - `een dag eerder` (fout = een dag eerder) → Bijna! Je bent één dag te kort geteld. Hoeveel dagen heeft de maand: dertig of eenendertig? De dag waarop je begint, tel je niet mee.  [nieuw]
  - `datum later` (fout = datum later dan het antwoord) → Dat is te ver. Tel eerst tot de laatste dag van de maand. Hoeveel dagen heb je dan al geteld? Tel alleen de rest verder in de nieuwe maand.  [nieuw]
  - `andere datum` (andere fout) → Tel eerst tot de laatste dag van de maand. Tel daarna verder in de nieuwe maand. Kijk goed hoeveel dagen de maand heeft: dertig of eenendertig?  [nieuw]
- Status: hints klaar

## Somtype 6: Het is # [ding]. Welke datum was het # dagen eerder?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Het is # [ding]. Welke datum was het # dagen eerder?” (koppeling: claudeId)
- Items: **83** · Claude-doelen: M10 (83) · regel: G19-kalender
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): kalender-verkeerd-geteld (129), deel-vergeten-bij-splitsen (37)
- Verschillende Claude-fout-hints: 2 (meest: “Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-104` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 2 april. Welke datum was het 10 dagen eerder?
    - **Opties:** A) 31 maart · B) 23 maart · C) 24 maart
    - **Antwoord:** 23 maart  (controle: ok)
    - **Fout-hints (Claude):** 24 maart → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 31 maart → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.
  - `G5-MEET-E06-claude-bank-098` (Claude M10, bank, niveau 3 → toepassen)
    - **Opgave:** Het is 3 september. Welke datum was het 15 dagen eerder?
    - **Opties:** A) 19 augustus · B) 20 augustus · C) 31 augustus
    - **Antwoord:** 19 augustus  (controle: ok)
    - **Fout-hints (Claude):** 20 augustus → Tel via de maandgrens: eerst tot het eind van de maand, dan de dagen van de nieuwe maand. En kijk hoeveel dagen die maand echt heeft. · 31 augustus → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Tel eerst terug tot de eerste dag van de maand. Hoeveel dagen heb je dan al teruggeteld?
- **Hint 2 (te schrijven):** Na de eerste dag van de maand kom je bij de laatste dag van de maand ervoor. Hoeveel dagen heeft die maand: dertig of eenendertig? Tel daar de rest verder terug.
- **Ouderzin:** Je kind telt een aantal dagen terug op de kalender, over het begin van de maand heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `gestopt bij de maandgrens` (fout = gestopt op de laatste dag van de maand) → Je bent gestopt waar de maand ervoor eindigt. Tel nog verder terug, tot je alle dagen hebt geteld.  [nieuw]
  - `een dag eerder` (fout = een dag eerder) → Bijna! Je bent één dag te ver teruggeteld. Hoeveel dagen heeft de maand ervoor: dertig of eenendertig?  [nieuw]
  - `een dag later` (fout = een dag later) → Bijna! Je bent één dag te kort teruggeteld. Hoeveel dagen heeft de maand ervoor: dertig of eenendertig? De dag waarop je begint, tel je niet mee.  [nieuw]
  - `datum eerder` (fout = datum eerder dan het antwoord) → Dat is te ver terug. Tel eerst terug tot de eerste dag van de maand. Hoeveel dagen heb je dan al teruggeteld? Tel alleen de rest verder terug.  [nieuw]
  - `andere datum` (andere fout) → Na de eerste dag van de maand kom je bij de laatste dag van de maand ervoor. Tel daar verder terug. Kijk goed hoeveel dagen die maand heeft: dertig of eenendertig?  [nieuw]
- Status: hints klaar

## Somtype 7: [klok] Hoe laat is het op deze klok? (opties digitaal) — minuten na het hele uur

- Sleutel: nrOrigineel **8** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties digitaal) — minuten na het hele uur” (koppeling: claudeId)
- Items: **65** · Claude-doelen: M7 (65) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): 5-minuten-te-laat (42), 1-minuut-te-vroeg (32), 1-minuut-te-laat (30), 5-minuten-te-vroeg (23), grote-wijzer-verkeerd (3)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-860` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 6, "soort": "klok", "minuut": 1}`
    - **Opties:** A) 6:01 · B) 6:02 · C) 6:06
    - **Antwoord:** 6:01  (controle: ok)
    - **Fout-hints (Claude):** 6:02 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 6:06 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-883` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 7, "soort": "klok", "minuut": 24}`
    - **Opties:** A) 7:19 · B) 7:24 · C) 7:23
    - **Antwoord:** 7:24  (controle: ok)
    - **Fout-hints (Claude):** 7:23 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 7:19 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de kleine wijzer. Welk getal heeft hij het laatst gehad? Dat getal komt vóór de dubbele punt.
- **Hint 2 (te schrijven):** Kijk voor de minuten naar de grote wijzer. Elk getal is vijf minuten: bij de één vijf minuten, bij de twee tien minuten. Tel vanaf het laatste getal de streepjes erbij: één minuut per streepje.
- **Ouderzin:** Je kind leest een klok met wijzers af op de minuut en kiest de digitale tijd (minuten na het hele uur).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een minuut te laat` (fout = klok een minuut te laat) → Bij die tijd staat de grote wijzer één streepje verder. Tel na het laatste getal de streepjes nog eens: één minuut per streepje.  [nieuw]
  - `een minuut te vroeg` (fout = klok een minuut te vroeg) → Bij die tijd staat de grote wijzer één streepje minder ver. Tel na het laatste getal de streepjes nog eens: één minuut per streepje.  [nieuw]
  - `vijf minuten te laat` (fout = klok vijf minuten te laat) → Bij die tijd staat de grote wijzer één getal verder. Tel vijf minuten per getal, tot het laatste getal vóór de grote wijzer.  [nieuw]
  - `vijf minuten te vroeg` (fout = klok vijf minuten te vroeg) → Bij die tijd staat de grote wijzer één getal minder ver. Tel vijf minuten per getal, tot het laatste getal vóór de grote wijzer.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die tijd staat de grote wijzer ergens anders. Tel vijf minuten per getal tot het laatste getal vóór de grote wijzer. Tel daarna de streepjes erbij: één minuut per streepje.  [nieuw]
  - `andere tijd` (andere fout) → Kijk naar de kleine wijzer: welk getal heeft hij het laatst gehad? Kijk dan naar de grote wijzer: vijf minuten per getal, en één minuut per streepje.  [nieuw]
- Status: hints klaar

## Somtype 8: [klok] Hoe laat is het op deze klok? (opties digitaal) — minuten vóór het hele uur

- Sleutel: nrOrigineel **9** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties digitaal) — minuten vóór het hele uur” (koppeling: claudeId)
- Items: **54** · Claude-doelen: M7 (54) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): 5-minuten-te-laat (27), 1-minuut-te-vroeg (26), 1-minuut-te-laat (26), 5-minuten-te-vroeg (25), grote-wijzer-verkeerd (4)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-907` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 12, "soort": "klok", "minuut": 48}`
    - **Opties:** A) 12:53 · B) 12:48 · C) 12:47
    - **Antwoord:** 12:48  (controle: ok)
    - **Fout-hints (Claude):** 12:47 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 12:53 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-919` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 10, "soort": "klok", "minuut": 48}`
    - **Opties:** A) 10:48 · B) 10:43 · C) 10:49
    - **Antwoord:** 10:48  (controle: ok)
    - **Fout-hints (Claude):** 10:49 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 10:43 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de kleine wijzer. Welk getal heeft hij het laatst gehad? Dat getal komt vóór de dubbele punt.
- **Hint 2 (te schrijven):** Kijk voor de minuten naar de grote wijzer. Elk getal is vijf minuten: bij de één vijf minuten, bij de twee tien minuten. Tel vanaf het laatste getal de streepjes erbij: één minuut per streepje.
- **Ouderzin:** Je kind leest een klok met wijzers af op de minuut en kiest de digitale tijd (na half, tot het hele uur).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een minuut te laat` (fout = klok een minuut te laat) → Bij die tijd staat de grote wijzer één streepje verder. Tel na het laatste getal de streepjes nog eens: één minuut per streepje.  [nieuw]
  - `een minuut te vroeg` (fout = klok een minuut te vroeg) → Bij die tijd staat de grote wijzer één streepje minder ver. Tel na het laatste getal de streepjes nog eens: één minuut per streepje.  [nieuw]
  - `vijf minuten te laat` (fout = klok vijf minuten te laat) → Bij die tijd staat de grote wijzer één getal verder. Tel vijf minuten per getal, tot het laatste getal vóór de grote wijzer.  [nieuw]
  - `vijf minuten te vroeg` (fout = klok vijf minuten te vroeg) → Bij die tijd staat de grote wijzer één getal minder ver. Tel vijf minuten per getal, tot het laatste getal vóór de grote wijzer.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die tijd staat de grote wijzer ergens anders. Tel vijf minuten per getal tot het laatste getal vóór de grote wijzer. Tel daarna de streepjes erbij: één minuut per streepje.  [nieuw]
  - `andere tijd` (andere fout) → Kijk naar de kleine wijzer: welk getal heeft hij het laatst gehad? Kijk dan naar de grote wijzer: vijf minuten per getal, en één minuut per streepje.  [nieuw]
- Status: hints klaar

## Somtype 9: [klok-zetten (wijzers slepen)] Zet de klok op [tijd].

- Sleutel: nrOrigineel **22** · somtypeOrigineel “[klok-zetten (wijzers slepen)] Zet de klok op [tijd].” (koppeling: claudeId)
- Items: **25** · Claude-doelen: merge-generator #100 (18), M7 (7) · regel: G15-klok, G5-FX100 generator
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): uur-te-laat (7)
- Verschillende Claude-fout-hints: 7 (meest: “"tien over half één" is nog vóór een uur. De kleine wijzer is nog niet bij de 1.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-827` (Claude M7, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Zet de klok op tien over half één.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 12.40 uur  (controle: ok)
    - **Fout-hints (Claude):** 1.40 uur → "tien over half één" is nog vóór een uur. De kleine wijzer is nog niet bij de 1.
    - **Uitleg (Claude):** De grote wijzer geeft de minuten: elke streep is 5 minuten. 40 minuten is bij de 8. De kleine wijzer staat na de 12.
  - `G5-MEET-E06-merge-gen-027` (Claude merge-generator #100, None, niveau None → toepassen)
    - **Opgave:** Zet de klok op vijf voor drie.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 2.55 uur  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zet eerst de grote wijzer. Hoeveel minuten is het na het hele uur? Elk getal is vijf minuten.
- **Hint 2 (te schrijven):** Zet na de grote wijzer de kleine wijzer. Hoor je 'half' of 'voor' in de tijd? Dan staat hij nog vóór het uur uit de tijd. Anders staat hij net voorbij dat uur.
- **Ouderzin:** Je kind zet de wijzers van een klok op een tijd in woorden.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → De kleine wijzer staat een uur te ver. De grote wijzer staat goed. Welk uur hoor je in de tijd? Hoor je 'half' of 'voor'? Dan staat de kleine wijzer nog vóór dat uur. Anders staat hij net voorbij dat uur.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → De grote wijzer staat niet goed. Hoeveel minuten na het hele uur is het? Elk getal is vijf minuten.  [nieuw]
  - `andere fout` (andere fout) → Zet eerst de grote wijzer: hoeveel minuten na het hele uur? Zet dan de kleine wijzer. Hoor je 'half' of 'voor' in de tijd? Dan staat hij nog vóór het uur dat je hoort. Anders staat hij net voorbij dat uur.  [nieuw]
- Status: hints klaar

## Somtype 10: [klok] Hoe laat is het op deze klok? (opties in woorden) — minuten na het hele uur

- Sleutel: nrOrigineel **10** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties in woorden) — minuten na het hele uur” (koppeling: claudeId)
- Items: **23** · Claude-doelen: M7 (23) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): uur-te-laat (16), 5-minuten-te-laat (13), klok-verkeerd-gelezen (11), uur-te-vroeg (6)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-973` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 5}`
    - **Opties:** A) vijf over 2 · B) vijf over 3 · C) tien over 2
    - **Antwoord:** vijf over 2  (controle: ok)
    - **Fout-hints (Claude):** tien over 2 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · vijf over 3 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-964` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 6, "soort": "klok", "minuut": 10}`
    - **Opties:** A) 2 uur · B) tien over 6 · C) tien over 7
    - **Antwoord:** tien over 6  (controle: ok)
    - **Fout-hints (Claude):** 2 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · tien over 7 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer: hoeveel minuten is het na het hele uur? Tot en met kwart over zeg je 'over'. Daarna zeg je 'voor half'.
- **Hint 2 (te schrijven):** Kijk voor het uur naar de kleine wijzer: welk getal heeft hij het laatst gehad? Bij 'over' noem je dat uur. Bij 'voor half' noem je het volgende uur.
- **Ouderzin:** Je kind leest een klok met wijzers af en kiest de tijd in woorden (vijf over, tien over, tien voor half …).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Het uur klopt niet. Kijk naar de kleine wijzer: welk getal heeft hij het laatst gehad? Bij 'over' noem je dat uur. Bij 'voor half' noem je het volgende uur.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Het uur klopt niet. Kijk naar de kleine wijzer: welk getal heeft hij het laatst gehad? Bij 'over' noem je dat uur. Bij 'voor half' noem je het volgende uur.  [nieuw]
  - `grote wijzer een getal te ver` (fout = klok vijf minuten te laat) → De minuten kloppen niet. Bij die tijd staat de grote wijzer één getal verder. Kijk hoeveel minuten na het hele uur het is: elk getal is vijf minuten.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Heb je de grote wijzer als uur gelezen? Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk naar de grote wijzer: hoeveel minuten na het hele uur is het? Kijk dan naar de kleine wijzer: welk getal heeft hij het laatst gehad? Bij 'over' noem je dat uur, bij 'voor half' het volgende uur.  [nieuw]
  - `andere tijd` (andere fout) → Kijk naar de grote wijzer: hoeveel minuten na het hele uur is het? Kijk dan naar de kleine wijzer: welk getal heeft hij het laatst gehad? Bij 'over' noem je dat uur, bij 'voor half' het volgende uur.  [nieuw]
- Status: hints klaar

## Somtype 11: Hoeveel dagen duurt het van # [maand] tot # [maand]? — één maandgrens (generator #84)

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Hoeveel dagen duurt het van # [maand] tot # [maand]? — één maandgrens (generator #84)” (koppeling: claudeId)
- Items: **20** · Claude-doelen: merge-generator #84 (20) · regel: G5-FX84 generator
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G5-MEET-E06-merge-gen-001` (Claude merge-generator #84, None, niveau None → toepassen)
    - **Opgave:** Hoeveel dagen duurt het van 23 mei tot 13 juni?
    - **Antwoord:** 21  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G5-MEET-E06-merge-gen-011` (Claude merge-generator #84, None, niveau None → toepassen)
    - **Opgave:** Hoeveel dagen duurt het van 9 mei tot 6 juni?
    - **Antwoord:** 28  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Tel eerst de dagen tot het eind van de eerste maand. Hoeveel dagen heeft die maand? Kijk op de kalender of tel op je knokkels. De dag waarop je begint, tel je niet mee.
- **Hint 2 (te schrijven):** Tel de dagen tot het eind van de eerste maand; de dag waarop je begint, tel je niet mee. Tel daarna de dagen in de nieuwe maand, tot en met de dag waarop het eindigt. Tel de twee stukken bij elkaar op.
- **Ouderzin:** Je kind rekent uit hoeveel dagen het is van de ene datum tot de andere, over het eind van de maand heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getallen afgetrokken` (fout = getal1 - getal2 of getal2 - getal1) → Heb je de twee getallen uit de vraag van elkaar afgetrokken? Je gaat over het eind van de maand heen. Tel eerst de dagen tot het eind van de eerste maand: hoeveel dagen heeft die maand? Tel daarna de dagen in de nieuwe maand erbij.  [nieuw]
  - `alleen de nieuwe maand` (fout = getal2) → Dat is te weinig. Heb je alleen de dagen in de nieuwe maand geteld? Tel eerst de dagen tot het eind van de eerste maand. Tel daarna de dagen in de nieuwe maand erbij.  [nieuw]
  - `alleen de eerste maand` (fout = antwoord − getal2) → Dat is te weinig. Heb je de dagen in de nieuwe maand ook erbij geteld? Kijk ook hoeveel dagen de eerste maand heeft. Tel tot en met de dag waarop het eindigt.  [nieuw]
  - `één dag te veel` (fout = antwoord + 1) → Bijna! Dat is één dag te veel. Heb je de dag waarop je begint meegeteld? Die tel je niet mee. Kijk ook hoeveel dagen de eerste maand heeft.  [nieuw]
  - `één dag te weinig` (fout = antwoord − 1) → Bijna! Dat is één dag te weinig. Hoeveel dagen heeft de eerste maand? Tel in de nieuwe maand tot en met de dag waarop het eindigt.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. De dag waarop je begint, tel je niet mee. Tel in twee stukken: eerst de dagen tot het eind van de eerste maand, dan de dagen in de nieuwe maand.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Heb je allebei de stukken geteld? Tel eerst de dagen tot het eind van de eerste maand, en daarna de dagen in de nieuwe maand.  [nieuw]
  - `andere fout` (andere fout) → Tel in twee stukken: eerst de dagen tot het eind van de eerste maand, dan de dagen in de nieuwe maand. De dag waarop je begint, tel je niet mee. Tel de twee stukken bij elkaar op.  [nieuw]
- Status: hints klaar

## Somtype 12: [klok] Hoe laat is het op deze klok? (opties in woorden) — minuten vóór het hele uur

- Sleutel: nrOrigineel **11** · somtypeOrigineel “[klok] Hoe laat is het op deze klok? (opties in woorden) — minuten vóór het hele uur” (koppeling: claudeId)
- Items: **17** · Claude-doelen: M7 (17) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- Denkfouten (Claude): uur-te-laat (10), klok-verkeerd-gelezen (8), 5-minuten-te-laat (8), uur-te-vroeg (6), grote-wijzer-verkeerd (2)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-981` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 35}`
    - **Opties:** A) vijf over half 4 · B) 7 uur · C) vijf over half 3
    - **Antwoord:** vijf over half 3  (controle: ok)
    - **Fout-hints (Claude):** 7 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · vijf over half 4 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-991` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 7, "soort": "klok", "minuut": 40}`
    - **Opties:** A) tien over half 8 · B) 8 uur · C) tien over half 9
    - **Antwoord:** tien over half 8  (controle: ok)
    - **Fout-hints (Claude):** 8 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · tien over half 9 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk eerst naar de grote wijzer: hoeveel minuten is het na het hele uur? Na half zeg je 'over half'. Vanaf kwart voor zeg je 'voor'.
- **Hint 2 (te schrijven):** Kijk voor het uur naar de kleine wijzer. Hij staat tussen twee getallen. Bij 'over half' en bij 'voor' noem je het getal waar hij naartoe gaat.
- **Ouderzin:** Je kind leest een klok met wijzers af en kiest de tijd in woorden (vijf over half, tien voor …).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Het uur klopt niet. De kleine wijzer staat tussen twee getallen. Bij 'over half' en bij 'voor' noem je het getal waar hij naartoe gaat.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Het uur klopt niet. De kleine wijzer staat tussen twee getallen. Bij 'over half' en bij 'voor' noem je het getal waar hij naartoe gaat.  [nieuw]
  - `grote wijzer een getal te ver` (fout = klok vijf minuten te laat) → De minuten kloppen niet. Bij die tijd staat de grote wijzer één getal verder. Kijk hoeveel minuten na het hele uur het is: elk getal is vijf minuten.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Heb je de grote wijzer als uur gelezen? Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk naar de grote wijzer: hoeveel minuten na het hele uur is het? De kleine wijzer staat tussen twee getallen: noem het getal waar hij naartoe gaat.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → De minuten kloppen niet. Kijk naar de grote wijzer: hoeveel minuten na het hele uur is het? Elk getal is vijf minuten.  [nieuw]
  - `andere tijd` (andere fout) → Kijk naar de grote wijzer: hoeveel minuten na het hele uur is het? De kleine wijzer staat tussen twee getallen: noem het getal waar hij naartoe gaat.  [nieuw]
- Status: hints klaar

## Somtype 13: [klokkenrij] Welke klok wijst half # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **24** · somtypeOrigineel “[klokkenrij] Welke klok wijst half # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **16** · Claude-doelen: M7 (16) · regel: FX-G4-45
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 16 items
- Denkfouten (Claude): uur-te-vroeg (16), 5-minuten-te-laat (16)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1231` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst half 6 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 5, "minuut": 30}, {"uur": 4, "minuut": 30}, {"uur": 5, "minuut": 35}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1233` (Claude M7, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst half 12 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 10, "minuut": 30}, {"uur": 11, "minuut": 35}, {"uur": 11, "minuut": 30}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij half wijst de grote wijzer recht naar beneden. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Half betekent: een half uur vóór het hele uur. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die half … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij half wijst hij recht naar beneden.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij recht naar beneden? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 14: [klokkenrij] Welke klok wijst tien over # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **12** · somtypeOrigineel “[klokkenrij] Welke klok wijst tien over # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M7 (12) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 12 items
- Denkfouten (Claude): uur-te-laat (12), over-en-voor-verwisseld (6), klok-verkeerd-gelezen (5), 10-minuten-te-vroeg (1)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1104` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien over 1 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 12, "minuut": 50}, {"uur": 2, "minuut": 10}, {"uur": 1, "minuut": 10}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1102` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien over 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 0}, {"uur": 2, "minuut": 10}, {"uur": 3, "minuut": 10}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij tien over wijst de grote wijzer naar de twee. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Tien over betekent: tien minuten na het hele uur. De kleine wijzer is dan net voorbij het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die tien over … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij tien over is de kleine wijzer net voorbij het uur uit de vraag.  [nieuw]
  - `over en voor verwisseld` (fout = over en voor verwisseld) → Bij die klok is het tien voor, en niet tien over. Bij tien over is de grote wijzer net voorbij de twaalf: hij wijst naar de twee.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Bij die klok is het een heel uur. Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk bij die klok naar de grote wijzer: wijst hij naar de twee? Kijk dan naar de kleine wijzer: is hij net voorbij het uur uit de vraag?  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij tien over wijst hij naar de twee.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de twee? Kijk dan naar de kleine wijzer: is hij net voorbij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 15: [klokkenrij] Welke klok wijst tien voor half # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **13** · somtypeOrigineel “[klokkenrij] Welke klok wijst tien voor half # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M7 (12) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 12 items
- Denkfouten (Claude): over-en-voor-verwisseld (12), uur-te-vroeg (6), uur-te-laat (6)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1135` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien voor half 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 20}, {"uur": 1, "minuut": 40}, {"uur": 12, "minuut": 20}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1138` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien voor half 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 20}, {"uur": 2, "minuut": 40}, {"uur": 3, "minuut": 20}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij tien voor half wijst de grote wijzer naar de vier. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Tien voor half betekent: tien minuten vóór half. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die tien voor half … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij tien voor half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij tien voor half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij tien voor half wijst hij naar de vier.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de vier? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 16: [klokkenrij] Welke klok wijst vijf over # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **14** · somtypeOrigineel “[klokkenrij] Welke klok wijst vijf over # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M7 (12) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 12 items
- Denkfouten (Claude): uur-te-laat (12), over-en-voor-verwisseld (6), klok-verkeerd-gelezen (5), 5-minuten-te-vroeg (1)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1150` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf over 1 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 12, "minuut": 55}, {"uur": 2, "minuut": 5}, {"uur": 1, "minuut": 5}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1156` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf over 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 5}, {"uur": 1, "minuut": 0}, {"uur": 3, "minuut": 5}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij vijf over wijst de grote wijzer naar de één. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Vijf over betekent: vijf minuten na het hele uur. De kleine wijzer is dan net voorbij het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die vijf over … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij vijf over is de kleine wijzer net voorbij het uur uit de vraag.  [nieuw]
  - `over en voor verwisseld` (fout = over en voor verwisseld) → Bij die klok is het vijf voor, en niet vijf over. Bij vijf over is de grote wijzer net voorbij de twaalf: hij wijst naar de één.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Bij die klok is het een heel uur. Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk bij die klok naar de grote wijzer: wijst hij naar de één? Kijk dan naar de kleine wijzer: is hij net voorbij het uur uit de vraag?  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij vijf over wijst hij naar de één.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de één? Kijk dan naar de kleine wijzer: is hij net voorbij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 17: [wie] beginnen om #.# uur en zijn klaar om #.# uur. Hoeveel minuten duurde het?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “[wie] beginnen om #:# en zijn klaar om #:#. Hoeveel minuten duurde het?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: M14 (12) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): uur-te-veel (12), tijd-als-kommagetal-te-veel (10), uur-te-weinig (8), tiental-ernaast-te-veel (4)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit een heel uur te hoog. Tel de uren nog eens na.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1197` (Claude M14, gegenereerd, niveau 1 → basis)
    - **Opgave:** De kinderen beginnen om 10.05 uur en zijn klaar om 10.55 uur. Hoeveel minuten duurde het?
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 110 → Je zit een heel uur te hoog. Tel de uren nog eens na. · 60 → Tel de minuten tot het hele uur, en dan de minuten daarna. Controleer allebei de stukjes.
    - **Uitleg (Claude):** Van 10.05 uur tot 10.55 uur is 50 minuten. Je gaat niet over het hele uur heen.
  - `G5-MEET-E06-claude-bank-1192` (Claude M14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** De spelers beginnen om 11.15 uur en zijn klaar om 12.40 uur. Hoeveel minuten duurde het?
    - **Antwoord:** 85  (controle: ok)
    - **Fout-hints (Claude):** 125 → Een uur heeft 60 minuten, geen 100. Je kunt de tijden niet zomaar van elkaar aftrekken. Reken via het hele uur. · 145 → Je zit een heel uur te hoog. Tel de uren nog eens na. · 25 → Tel de minuten tot het hele uur, en dan de minuten daarna. Controleer allebei de stukjes.
    - **Uitleg (Claude):** Reken via het hele uur. Van 11.15 uur tot 12.00 uur is 45 minuten. Van 12.00 uur tot 12.40 uur is 40 minuten. Samen: 45 + 40 = 85 minuten.

- **Hint 1 (te schrijven):** Kom je over het hele uur heen? Tel dan eerst de minuten tot het hele uur.
- **Hint 2 (te schrijven):** Ga je niet over het hele uur heen? Tel dan gewoon van de begintijd tot de eindtijd. Ga je er wel overheen? Tel dan de hele uren erbij als die er zijn, elk uur is zestig minuten. Tel tot slot de minuten na het laatste hele uur erbij.
- **Ouderzin:** Je kind rekent uit hoe lang iets duurt in minuten, van de begintijd tot de eindtijd.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een uur te veel` (fout = antwoord + 60) → Dat is zestig minuten te veel: een heel uur. Tel in stukken: eerst tot het hele uur, dan de hele uren van zestig minuten als die er zijn, dan de minuten erna.  [nieuw]
  - `een uur te weinig` (fout = antwoord − 60) → Dat is zestig minuten te weinig: een heel uur. Heb je alle hele uren meegeteld?  [nieuw]
  - `honderd minuten` (Claudes sleutel: tijd-als-kommagetal) → Dat is te veel. Heb je gerekend alsof een uur honderd minuten heeft? Een uur heeft zestig minuten.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Tel van de begintijd tot de eindtijd. Ga je over het hele uur heen? Tel dan in stukken: eerst tot het hele uur, dan de hele uren als die er zijn, dan de minuten erna.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Heb je alle stukken opgeteld? Tel van de begintijd tot de eindtijd. Ga je over het hele uur heen? Tel dan in stukken: eerst tot het hele uur, dan de hele uren als die er zijn, dan de minuten erna.  [nieuw]
  - `andere fout` (andere fout) → Tel van de begintijd tot de eindtijd. Ga je over het hele uur heen? Tel dan in stukken: eerst tot het hele uur, dan de hele uren als die er zijn, dan de minuten erna. Een uur heeft zestig minuten.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] beginnen om #:# en zijn klaar om #:#. Hoeveel minuten duurde het?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 18: [klokkenrij] Welke klok wijst tien over half # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **16** · somtypeOrigineel “[klokkenrij] Welke klok wijst tien over half # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M7 (10) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 10 items
- Denkfouten (Claude): over-en-voor-verwisseld (10), uur-te-vroeg (5), uur-te-laat (5)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1118` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien over half 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 20}, {"uur": 1, "minuut": 40}, {"uur": 12, "minuut": 40}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1122` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien over half 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 40}, {"uur": 2, "minuut": 20}, {"uur": 3, "minuut": 40}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij tien over half wijst de grote wijzer naar de acht. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Tien over half betekent: tien minuten na half. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die tien over half … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij tien over half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij tien over half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij tien over half wijst hij naar de acht.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de acht? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 19: [klokkenrij] Welke klok wijst tien voor # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **17** · somtypeOrigineel “[klokkenrij] Welke klok wijst tien voor # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M7 (10) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 10 items
- Denkfouten (Claude): uur-te-laat (10), over-en-voor-verwisseld (5), klok-verkeerd-gelezen (5)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1127` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien voor 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 10}, {"uur": 2, "minuut": 50}, {"uur": 1, "minuut": 50}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1125` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst tien voor 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 50}, {"uur": 10, "minuut": 0}, {"uur": 3, "minuut": 50}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij tien voor wijst de grote wijzer naar de tien. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Tien voor betekent: tien minuten vóór het hele uur. De kleine wijzer is dan bijna bij het uur uit de vraag, maar nog net ervoor.
- **Ouderzin:** Je kind zoekt de klok met wijzers die tien voor … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij tien voor is de kleine wijzer bijna bij het uur uit de vraag.  [nieuw]
  - `over en voor verwisseld` (fout = over en voor verwisseld) → Bij die klok is het tien over, en niet tien voor. Bij tien voor moet de grote wijzer nog naar de twaalf: hij wijst naar de tien.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Bij die klok is het een heel uur. Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk bij die klok naar de grote wijzer: wijst hij naar de tien? Kijk dan naar de kleine wijzer: is hij bijna bij het uur uit de vraag?  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de tien? Kijk dan naar de kleine wijzer: is hij bijna bij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 20: [klokkenrij] Welke klok wijst vijf over half # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **18** · somtypeOrigineel “[klokkenrij] Welke klok wijst vijf over half # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M7 (10) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 10 items
- Denkfouten (Claude): over-en-voor-verwisseld (10), uur-te-vroeg (5), uur-te-laat (5)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1158` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf over half 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 25}, {"uur": 1, "minuut": 35}, {"uur": 12, "minuut": 35}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1164` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf over half 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 35}, {"uur": 2, "minuut": 25}, {"uur": 3, "minuut": 35}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij vijf over half wijst de grote wijzer naar de zeven. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Vijf over half betekent: vijf minuten na half. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die vijf over half … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij vijf over half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij vijf over half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij vijf over half wijst hij naar de zeven.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de zeven? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 21: [klokkenrij] Welke klok wijst vijf voor # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **19** · somtypeOrigineel “[klokkenrij] Welke klok wijst vijf voor # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M7 (10) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 10 items
- Denkfouten (Claude): uur-te-laat (10), over-en-voor-verwisseld (5), klok-verkeerd-gelezen (5)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1172` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf voor 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 55}, {"uur": 2, "minuut": 5}, {"uur": 2, "minuut": 55}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1173` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf voor 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 11, "minuut": 0}, {"uur": 2, "minuut": 55}, {"uur": 3, "minuut": 55}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij vijf voor wijst de grote wijzer naar de elf. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Vijf voor betekent: vijf minuten vóór het hele uur. De kleine wijzer is dan bijna bij het uur uit de vraag, maar nog net ervoor.
- **Ouderzin:** Je kind zoekt de klok met wijzers die vijf voor … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij vijf voor is de kleine wijzer bijna bij het uur uit de vraag.  [nieuw]
  - `over en voor verwisseld` (fout = over en voor verwisseld) → Bij die klok is het vijf over, en niet vijf voor. Bij vijf voor moet de grote wijzer nog naar de twaalf: hij wijst naar de elf.  [nieuw]
  - `grote wijzer als uur gelezen` (fout = grote wijzer als uur gelezen) → Bij die klok is het een heel uur. Het uur lees je af aan de kleine wijzer, de minuten aan de grote wijzer. Kijk bij die klok naar de grote wijzer: wijst hij naar de elf? Kijk dan naar de kleine wijzer: is hij bijna bij het uur uit de vraag?  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de elf? Kijk dan naar de kleine wijzer: is hij bijna bij het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 22: [klokkenrij] Welke klok wijst vijf voor half # [ding]? (tijd in woorden)

- Sleutel: nrOrigineel **20** · somtypeOrigineel “[klokkenrij] Welke klok wijst vijf voor half # [ding]? (tijd in woorden)” (koppeling: claudeId)
- Items: **10** · Claude-doelen: M7 (10) · regel: G15-klok
- Getallenruimte: tijd tot op de minuut; kalender · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 10 items
- Denkfouten (Claude): over-en-voor-verwisseld (10), uur-te-vroeg (5), uur-te-laat (5)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1184` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf voor half 2 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 1, "minuut": 25}, {"uur": 1, "minuut": 35}, {"uur": 12, "minuut": 25}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** A  (controle: ok)
    - **Fout-hints (Claude):** B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G5-MEET-E06-claude-bank-1178` (Claude M7, bank, niveau 3 → toepassen)
    - **Opgave:** Welke klok wijst vijf voor half 3 aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 2, "minuut": 35}, {"uur": 3, "minuut": 25}, {"uur": 2, "minuut": 25}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** C  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · B → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij vijf voor half wijst de grote wijzer naar de vijf. Zoek eerst de klokken waarbij dat zo is.
- **Hint 2 (te schrijven):** Vijf voor half betekent: vijf minuten vóór half. De kleine wijzer staat dan tussen het uur ervoor en het uur uit de vraag.
- **Ouderzin:** Je kind zoekt de klok met wijzers die vijf voor half … aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleine wijzer een uur te ver` (fout = klok een uur te laat) → Bij die klok staat de kleine wijzer een uur te ver. De grote wijzer klopt wel. Bij vijf voor half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `kleine wijzer een uur te vroeg` (fout = klok een uur te vroeg) → Bij die klok staat de kleine wijzer een uur te vroeg. De grote wijzer klopt wel. Bij vijf voor half staat de kleine wijzer tussen het uur ervoor en het uur uit de vraag.  [nieuw]
  - `grote wijzer verkeerd` (fout = grote wijzer verkeerd) → Bij die klok staat de grote wijzer niet goed. Bij vijf voor half wijst hij naar de vijf.  [nieuw]
  - `andere klok` (andere fout) → Kijk bij die klok naar de grote wijzer: wijst hij naar de vijf? Kijk dan naar de kleine wijzer: staat hij tussen het uur ervoor en het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 23: [wie] vertrekken om #.# uur. De reis duurt # uur en # minuten. Hoe laat komen ze aan? (Typ als 14.30.)

- Sleutel: nrOrigineel **21** · somtypeOrigineel “[wie] vertrekken om #:#. De reis duurt # uur en # minuten. Hoe laat komen ze aan? Typ de tijd, zoals #:#.” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M14 (8) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): uur-te-vroeg (8), 10-minuten-te-laat (7), tijd-als-kommagetal (5), over-en-voor-verwisseld (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit een uur te vroeg. Tel de uren nog eens na.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1204` (Claude M14, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** De kinderen vertrekken om 8.10 uur. De reis duurt 1 uur en 20 minuten. Hoe laat komen ze aan? (Typ als 14.30.)
    - **Antwoord:** 9.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 8.30 uur → Je zit een uur te vroeg. Tel de uren nog eens na. · 9.40 uur → Tel de minuten tot het hele uur en de minuten daarna apart.
    - **Uitleg (Claude):** Tel eerst 1 uur erbij: 9.10 uur. Nog 20 minuten verder: 9.30 uur.
  - `G5-MEET-E06-claude-bank-1210` (Claude M14, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** De spelers vertrekken om 8.40 uur. De reis duurt 2 uur en 50 minuten. Hoe laat komen ze aan? (Typ als 14.30.)
    - **Antwoord:** 11.30 uur  (controle: ok)
    - **Fout-hints (Claude):** 10:90 → Een uur heeft 60 minuten. Komen de minuten boven de 60, dan gaat er een uur bij. · 10.30 uur → Je zit een uur te vroeg. Tel de uren nog eens na. · 11.40 uur → Tel de minuten tot het hele uur en de minuten daarna apart.
    - **Uitleg (Claude):** Ga via het hele uur. Van 8.40 uur tot 9.00 uur is 20 minuten. Dan 2 uur: 11.00 uur. Nog 30 minuten verder: 11.30 uur.

- **Hint 1 (te schrijven):** Tel eerst de hele uren erbij. Tel daarna de minuten erbij.
- **Hint 2 (te schrijven):** Komen de minuten op zestig of meer? Dan is dat een uur erbij. Een uur heeft zestig minuten.
- **Ouderzin:** Je kind rekent uit hoe laat iets aankomt als de reis uren en minuten duurt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `zestig minuten of meer` (Claudes sleutel: tijd-als-kommagetal) → Achter de punt staan de minuten. Dat kunnen er niet zestig of meer zijn: een uur heeft zestig minuten. Dan komt er een uur bij.  [Claude, taalfix]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg. Heb je alle hele uren van de reis erbij geteld?  [nieuw]
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. Tel de hele uren van de reis nog eens.  [nieuw]
  - `tien minuten te laat` (fout = klok tien minuten te laat) → De minuten kloppen niet. Tel de minuten van de reis nog eens erbij. Kom je over het hele uur heen?  [nieuw]
  - `tien minuten te vroeg` (fout = klok tien minuten te vroeg) → De minuten kloppen niet. Tel de minuten van de reis nog eens erbij. Kom je over het hele uur heen?  [nieuw]
  - `uren of minuten ernaast` (Claudes sleutel: tiental-ernaast) → Dat klopt niet helemaal. Tel de uren en de minuten nog eens apart erbij. Kijk of je over het hele uur heen gaat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel eerst de hele uren erbij, en daarna de minuten. Een uur heeft zestig minuten: kom je over het hele uur heen, dan komt er een uur bij.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] vertrekken om #:#. De reis duurt # uur en # minuten. Hoe laat komen ze aan? Typ de tijd, zoals #:#.'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 24: [wie] vertrekken om #.# uur. De reis duurt # minuten. Hoe laat komen ze aan? (Typ als 14.30.)

- Sleutel: nrOrigineel **23** · somtypeOrigineel “[wie] vertrekken om #:#. De reis duurt # minuten. Hoe laat komen ze aan? Typ de tijd, zoals #:#.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M14 (4) · regel: G5-M03-tijdsduur
- Getallenruimte: tijd tot op de minuut; kalender · type: kale
- Denkfouten (Claude): uur-te-vroeg (4), tijd-als-kommagetal (3), 10-minuten-te-laat (2), grote-wijzer-verkeerd (1), over-en-voor-verwisseld (1)
- Verschillende Claude-fout-hints: 3 (meest: “Je zit een uur te vroeg. Tel de uren nog eens na.”)
- Voorbeelden:
  - `G5-MEET-E06-claude-bank-1201` (Claude M14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** De kinderen vertrekken om 16.45 uur. De reis duurt 35 minuten. Hoe laat komen ze aan? (Typ als 14.30.)
    - **Antwoord:** 17.20 uur  (controle: ok)
    - **Fout-hints (Claude):** 16:80 → Een uur heeft 60 minuten. Komen de minuten boven de 60, dan gaat er een uur bij. · 16.20 uur → Je zit een uur te vroeg. Tel de uren nog eens na. · 17.30 uur → Tel de minuten tot het hele uur en de minuten daarna apart.
    - **Uitleg (Claude):** Ga via het hele uur. Van 16.45 uur tot 17.00 uur is 15 minuten. Nog 20 minuten verder: 17.20 uur.
  - `G5-MEET-E06-claude-bank-1203` (Claude M14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** De spelers vertrekken om 17.50 uur. De reis duurt 25 minuten. Hoe laat komen ze aan? (Typ als 14.30.)
    - **Antwoord:** 18.15 uur  (controle: ok)
    - **Fout-hints (Claude):** 17:75 → Een uur heeft 60 minuten. Komen de minuten boven de 60, dan gaat er een uur bij. · 17.15 uur → Je zit een uur te vroeg. Tel de uren nog eens na. · 18.25 uur → Tel de minuten tot het hele uur en de minuten daarna apart.
    - **Uitleg (Claude):** Ga via het hele uur. Van 17.50 uur tot 18.00 uur is 10 minuten. Nog 15 minuten verder: 18.15 uur.

- **Hint 1 (te schrijven):** Tel de minuten erbij. Kom je over het hele uur heen?
- **Hint 2 (te schrijven):** Ga je over het hele uur heen? Tel dan eerst tot het hele uur, en daarna de minuten die nog over zijn. Een uur heeft zestig minuten.
- **Ouderzin:** Je kind rekent uit hoe laat iets aankomt als de reis een aantal minuten duurt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `zestig minuten of meer` (Claudes sleutel: tijd-als-kommagetal) → Achter de punt staan de minuten. Dat kunnen er niet zestig of meer zijn: een uur heeft zestig minuten. Dan komt er een uur bij.  [Claude, taalfix]
  - `een uur te vroeg` (fout = klok een uur te vroeg) → Dat is een uur te vroeg: dan kom je aan vóór je vertrekt. Kom je over het hele uur heen? Dan komt er een uur bij.  [nieuw]
  - `een uur te laat` (fout = klok een uur te laat) → Dat is een uur te laat. De reis duurt korter dan een uur. Er komt alleen een uur bij als je over het hele uur heen gaat.  [nieuw]
  - `tien minuten te laat` (fout = klok tien minuten te laat) → De minuten kloppen niet. Tel de minuten van de reis nog eens erbij. Kom je over het hele uur heen?  [nieuw]
  - `tien minuten te vroeg` (fout = klok tien minuten te vroeg) → De minuten kloppen niet. Tel de minuten van de reis nog eens erbij. Kom je over het hele uur heen?  [nieuw]
  - `uren of minuten ernaast` (Claudes sleutel: tiental-ernaast) → Dat klopt niet helemaal. Tel de uren en de minuten nog eens apart erbij. Kijk of je over het hele uur heen gaat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de minuten erbij. Een uur heeft zestig minuten: kom je over het hele uur heen, dan komt er een uur bij.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor '[wie] vertrekken om #:#. De reis duurt # minuten. Hoe laat komen ze aan? Typ de tijd, zoals #:#.'. Nakijken of ze nog passen.
- Status: hints klaar
