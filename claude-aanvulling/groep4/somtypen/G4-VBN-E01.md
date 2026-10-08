# G4-VBN-E01 — Tabellen en staafdiagrammen lezen

Onze omschrijving: Tabel/beeld-/staafdiagram aflezen, interpreteren, bewerkingen · in onze bank: 8 items

Claude-vragen gemapt: **278** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [tabel] Hoeveel [naam] zijn er op [naam]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[tabel] Hoeveel [naam] op [naam]?” (koppeling: claudeId)
- Items: **83** · Claude-doelen: G1 (83) · regel: G25-tabel
- Getallenruimte: 0–10, 0–100, 0–20 · type: meerkeuze
- **Visual: nodig** (83 items): Claude-tekenaar: soort “tabel” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[tabel] Hoeveel [naam] op [naam]?”. Hints nakijken.
- Merge-fixlijst: #46 afleiders ≤ 100 (19), #47 werkwoord in de tabelvraag (83)
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (82), andere-deel-genomen (57)
- Verschillende Claude-fout-hints: 1 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G4-VBN-E01-claude-bank-153` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel peren zijn er op woensdag?
    - **Tekening:** `{"rijen": [{"naam": "appels", "waarden": [9, 3, 7]}, {"naam": "peren", "waarden": [2, 6, 11]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag"]}`
    - **Opties:** A) 7 · B) 2 · C) 11
    - **Antwoord:** 11  (controle: n.v.t.)
    - **Fout-hints (Claude):** —
  - `G4-VBN-E01-claude-bank-185` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel vogels zijn er op donderdag?
    - **Tekening:** `{"rijen": [{"naam": "honden", "waarden": [61, 18, 44, 75]}, {"naam": "katten", "waarden": [12, 37, 68, 23]}, {"naam": "konijnen", "waarden": [31, 61, 18, 44]}, {"naam": "vogels", "waarden": [52, 12, 37, 68]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 75 · B) 23 · C) 68
    - **Antwoord:** 68  (controle: n.v.t.)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag.
- **Hint 2 (te schrijven):** Ga in die rij naar de kolom van de dag uit de vraag. Het getal in dat vak is het antwoord.
- **Ouderzin:** Je kind leest één getal af in een tabel.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere cel` (fout = andere cel) → Dat getal staat in een ander vak. Zoek de rij van het ding en de kolom van de dag. Waar die twee elkaar raken, staat het antwoord.  [nieuw]
  - `som van de rij` (fout = som van de rij) → Je hebt een hele rij bij elkaar opgeteld. De vraag gaat over één dag: kijk alleen in het vak van die dag.  [nieuw]
  - `som van de kolom` (fout = som van de kolom) → Je hebt een hele kolom bij elkaar opgeteld. De vraag gaat over één ding: kijk alleen in het vak van dat ding.  [nieuw]
  - `ander vak of opgeteld` (andere fout) → Zoek de rij van het ding en de kolom van de dag. Waar die twee elkaar raken, staat het antwoord. Je hoeft niets uit te rekenen.  [nieuw]
- Status: hints klaar

## Somtype 2: [tabel] Hoeveel [naam] zijn er op [naam] meer dan op [naam]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[tabel] Hoeveel [naam] meer op [naam] dan op [naam]?” (koppeling: claudeId)
- Items: **58** · Claude-doelen: G1 (58) · regel: G25-tabel
- Getallenruimte: 0–10, 0–100, 0–20 · type: meerkeuze
- **Visual: nodig** (58 items): Claude-tekenaar: soort “tabel” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[tabel] Hoeveel [naam] meer op [naam] dan op [naam]?”. Hints nakijken.
- Merge-fixlijst: #46 afleiders ≤ 100 (16), #47 werkwoord in de tabelvraag (58)
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (35), getal-overgenomen (30), verkeerde-bewerking (21), andere-deel-genomen (14)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G4-VBN-E01-claude-bank-082` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel peren zijn er op maandag meer dan op dinsdag?
    - **Tekening:** `{"rijen": [{"naam": "appels", "waarden": [5, 9, 3]}, {"naam": "peren", "waarden": [8, 2, 6]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag"]}`
    - **Opties:** A) 6 · B) 4 · C) 16
    - **Antwoord:** 6  (controle: n.v.t.)
    - **Fout-hints (Claude):** 16 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G4-VBN-E01-claude-bank-090` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel fietsen zijn er op woensdag meer dan op donderdag?
    - **Tekening:** `{"rijen": [{"naam": "fietsen", "waarden": [75, 31, 61, 18]}, {"naam": "bussen", "waarden": [23, 52, 12, 37]}, {"naam": "treinen", "waarden": [44, 75, 31, 61]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 43 · B) 25 · C) 79
    - **Antwoord:** 43  (controle: n.v.t.)
    - **Fout-hints (Claude):** 79 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag. Zoek in die rij de getallen van de twee dagen.
- **Hint 2 (te schrijven):** Hoeveel meer? Haal het kleinste getal van het grootste af.
- **Ouderzin:** Je kind zoekt twee getallen in een tabel en rekent uit hoeveel meer het ene is dan het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één getal` (fout = andere cel) → Dat is één getal uit de tabel. Je hebt er twee nodig: die van de twee dagen, in de rij van het ding. Haal dan het kleinste getal van het grootste af.  [nieuw]
  - `som van de rij` (fout = som van de rij) → Je hebt een hele rij bij elkaar opgeteld. Je hebt alleen de getallen van de twee dagen nodig. Haal het kleinste getal van het grootste af.  [nieuw]
  - `opgeteld` (fout = som van twee cellen) → Je hebt twee getallen opgeteld. Hoeveel meer? Haal het kleinste getal van het grootste af.  [nieuw]
  - `verkeerde getallen afgetrokken` (fout = verschil van twee cellen) → Je hebt twee andere getallen van elkaar afgehaald. Kijk goed: de rij van het ding, en de twee dagen uit de vraag.  [nieuw]
  - `één getal of opgeteld` (andere fout) → Je hebt twee getallen nodig: die van de twee dagen, in de rij van het ding. Haal dan het kleinste getal van het grootste af.  [nieuw]
- Status: hints klaar

## Somtype 3: [tabel] Hoeveel [naam] zijn er in totaal?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[tabel] Hoeveel [naam] in totaal?” (koppeling: claudeId)
- Items: **54** · Claude-doelen: G1 (54) · regel: G25-tabel
- Getallenruimte: 0–10, 0–100, 0–20 · type: meerkeuze
- **Visual: nodig** (54 items): Claude-tekenaar: soort “tabel” (parameters in jsRender)
- **Kop gewijzigd** (kopGewijzigd, merge-fixlijst): was “[tabel] Hoeveel [naam] in totaal?”. Hints nakijken.
- Merge-fixlijst: #47 werkwoord in de tabelvraag (54)
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (36), andere-deel-genomen (33), deel-vergeten-bij-splitsen (24), getal-overgenomen (15)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G4-VBN-E01-claude-bank-037` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel boeken zijn er in totaal?
    - **Tekening:** `{"rijen": [{"naam": "boeken", "waarden": [9, 19, 6]}, {"naam": "potloden", "waarden": [17, 4, 12]}, {"naam": "stiften", "waarden": [25, 9, 19]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag"]}`
    - **Opties:** A) 34 · B) 25 · C) 51
    - **Antwoord:** 34  (controle: n.v.t.)
    - **Fout-hints (Claude):** 25 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet. · 51 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G4-VBN-E01-claude-bank-036` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel stiften zijn er in totaal?
    - **Tekening:** `{"rijen": [{"naam": "boeken", "waarden": [12, 5]}, {"naam": "potloden", "waarden": [4, 8]}, {"naam": "stiften", "waarden": [7, 12]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag"]}`
    - **Opties:** A) 17 · B) 7 · C) 19
    - **Antwoord:** 19  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag.
- **Hint 2 (te schrijven):** Tel alle getallen in die rij bij elkaar. Sla er geen over.
- **Ouderzin:** Je kind telt alle getallen in één rij van een tabel bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere rij` (fout = som van de rij) → Dat is het totaal van een andere rij. Zoek eerst de rij van het ding uit de vraag.  [nieuw]
  - `kolom opgeteld` (fout = som van de kolom) → Je hebt een kolom opgeteld. Tel de getallen in de rij van het ding uit de vraag bij elkaar.  [nieuw]
  - `één getal` (fout = andere cel) → Dat is maar één getal. In totaal betekent: tel alle getallen in de rij bij elkaar.  [nieuw]
  - `niet alles opgeteld` (fout = som van twee cellen) → Je hebt niet alles opgeteld. Tel alle getallen in de rij bij elkaar. Sla er geen over.  [nieuw]
  - `afgetrokken` (fout = verschil van twee cellen) → Je hebt getallen van elkaar afgehaald. In totaal betekent: alles bij elkaar optellen.  [nieuw]
  - `andere rij of niet alles` (andere fout) → Tel alle getallen in de rij van het ding uit de vraag bij elkaar: van elke dag één. Tel de andere rijen niet mee.  [nieuw]
- Status: hints klaar

## Somtype 4: [staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er?” (koppeling: claudeId)
- Items: **42** · Claude-doelen: G2 (42) · regel: D-SCHAAL-AS10
- Getallenruimte: 0–20, 0–30, 0–40 · type: meerkeuze
- **Visual: nodig** (42 items): Claude-tekenaar: staafdiagram tot 20; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1) · Claude-tekenaar: staafdiagram tot 30; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1) · Claude-tekenaar: staafdiagram tot 40; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1)
- Didactiek-besluit (G4-twijfel, 1 okt): getal om de 10, 1 streep = 2 — zie besluiten_twijfel.md
- Hint-richting (Didactiek): Zoek het getal vlak onder de staaf. Spring dan verder met 2.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (76), plaatswaarde-verkeerd (8)
- Verschillende Claude-fout-hints: 1 (meest: “Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.”)
- Voorbeelden:
  - `G4-VBN-E01-claude-bank-271` (Claude G2, bank, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 2.
Hoeveel peren zijn er?
    - **Tekening:** `{"max": 20, "soort": "staafdiagram", "staven": [{"naam": "appels", "waarde": 2}, {"naam": "peren", "waarde": 6}, {"naam": "bananen", "waarde": 10}], "cijfer_om": 10, "perstreep": 2}`
    - **Opties:** A) 3 · B) 6 · C) 4
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 3 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is. · 4 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.
  - `G4-VBN-E01-claude-bank-251` (Claude G2, bank, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 2.
Hoeveel bananen zijn er?
    - **Tekening:** `{"max": 30, "soort": "staafdiagram", "staven": [{"naam": "peren", "waarde": 2}, {"naam": "bananen", "waarde": 16}, {"naam": "druiven", "waarde": 20}, {"naam": "kersen", "waarde": 26}], "cijfer_om": 10, "perstreep": 2}`
    - **Opties:** A) 16 · B) 8 · C) 10
    - **Antwoord:** 16  (controle: ok)
    - **Fout-hints (Claude):** 8 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.

- **Hint 1 (te schrijven):** Zoek de staaf van het ding uit de vraag. Zoek het getal vlak onder de top van de staaf.
- **Hint 2 (te schrijven):** Elk streepje is twee. Spring vanaf dat getal verder met twee voor elk streepje, tot de top van de staaf.
- **Ouderzin:** Je kind leest een staafdiagram af waarin elk streepje twee is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één streepje te veel` (fout = antwoord + getal1) → Bijna! Dat is één streepje te veel. Kijk goed waar de top van de staaf is.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − getal1) → Bijna! Dat is één streepje te weinig. Kijk goed waar de top van de staaf is.  [nieuw]
  - `streepjes geteld` (fout = antwoord gedeeld door getal1) → Je hebt de streepjes geteld. Maar elk streepje is twee. Spring bij elk streepje twee verder.  [nieuw]
  - `streepjes geteld of andere staaf` (andere fout) → Zoek de staaf van het ding uit de vraag. Tel niet alleen de streepjes: spring bij elk streepje twee verder. Waar kom je bij de top van de staaf?  [nieuw]
- Status: hints klaar

## Somtype 5: [staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er meer dan [naam]?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er meer dan [naam]?” (koppeling: claudeId)
- Items: **41** · Claude-doelen: G2 (41) · regel: D-SCHAAL-AS10
- Getallenruimte: 0–20, 0–30, 0–40 · type: meerkeuze
- **Visual: nodig** (41 items): Claude-tekenaar: staafdiagram tot 20; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1) · Claude-tekenaar: staafdiagram tot 30; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1) · Claude-tekenaar: staafdiagram tot 40; elk streepje = 2; de getallen om de 10 langs de as moeten zichtbaar zijn (cijfer_om 10, Didactiek §1)
- Didactiek-besluit (G4-twijfel, 1 okt): getal om de 10, 1 streep = 2 — zie besluiten_twijfel.md
- Hint-richting (Didactiek): Zoek het getal vlak onder de staaf. Spring dan verder met 2.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (37), verkeerde-bewerking (28), andere-deel-genomen (17)
- Verschillende Claude-fout-hints: 3 (meest: “Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.”)
- Voorbeelden:
  - `G4-VBN-E01-claude-bank-221` (Claude G2, bank, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 2.
Hoeveel boten zijn er meer dan treinen?
    - **Tekening:** `{"max": 20, "soort": "staafdiagram", "staven": [{"naam": "bussen", "waarde": 2}, {"naam": "treinen", "waarde": 6}, {"naam": "boten", "waarde": 14}], "cijfer_om": 10, "perstreep": 2}`
    - **Opties:** A) 20 · B) 6 · C) 8
    - **Antwoord:** 8  (controle: ok)
    - **Fout-hints (Claude):** 20 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 6 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.
  - `G4-VBN-E01-claude-bank-234` (Claude G2, bank, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 2.
Hoeveel bananen zijn er meer dan peren?
    - **Tekening:** `{"max": 40, "soort": "staafdiagram", "staven": [{"naam": "peren", "waarde": 8}, {"naam": "bananen", "waarde": 18}, {"naam": "druiven", "waarde": 4}], "cijfer_om": 10, "perstreep": 2}`
    - **Opties:** A) 26 · B) 18 · C) 10
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 26 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 18 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** Zoek de twee staven uit de vraag. Lees bij allebei af hoeveel het er zijn. Elk streepje is twee.
- **Hint 2 (te schrijven):** Hoeveel meer? Haal het kleinste getal van het grootste af. Of tel hoeveel streepjes de ene staaf hoger is, en spring per streepje twee verder.
- **Ouderzin:** Je kind leest twee staven af in een staafdiagram en rekent uit hoeveel meer het ene is dan het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één streepje te veel` (fout = antwoord + getal1) → Bijna! Dat is één streepje te veel. Kijk nog eens goed waar de toppen van de twee staven zijn.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − getal1) → Bijna! Dat is één streepje te weinig. Kijk nog eens goed waar de toppen van de twee staven zijn.  [nieuw]
  - `streepjes geteld` (fout = antwoord gedeeld door getal1) → Je hebt geteld hoeveel streepjes de ene staaf hoger is. Maar elk streepje is twee. Spring per streepje twee verder.  [nieuw]
  - `opgeteld of één staaf` (andere fout) → Lees de twee staven uit de vraag af. Elk streepje is twee. Hoeveel meer? Haal het kleinste getal van het grootste af.  [nieuw]
- Status: hints klaar
