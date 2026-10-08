# G5-VBN-E01 — Tabellen en staven begrijpen

Onze omschrijving: Tabel/beeld/staaf: aflezen, interpreteren, bewerkingen · in onze bank: 8 items

Claude-vragen gemapt: **338** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er?” (koppeling: claudeId)
- Items: **115** · Claude-doelen: G2 (115) · regel: D-SCHAAL-AS10, G26-staaf, D-SCHAAL-AS25
- Getallenruimte: 0–1.000, 0–10, 0–100, 0–20 · type: meerkeuze
- Didactiek-besluit (G4-twijfel, 1 okt): getal om de 10, 1 streep = 5, getal om de 25, 1 streep = 5 — zie g4/besluiten_twijfel.md + besluit Dave
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 5.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (218), plaatswaarde-verkeerd (12)
- Verschillende Claude-fout-hints: 1 (meest: “Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.”)
- Voorbeelden:
  - `G5-VBN-E01-claude-bank-166` (Claude G2, bank, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 5.
Hoeveel druiven zijn er?
    - **Tekening:** `{"max": 30, "soort": "staafdiagram", "staven": [{"naam": "druiven", "waarde": 5}, {"naam": "kersen", "waarde": 15}, {"naam": "pruimen", "waarde": 25}], "cijfer_om": 10, "perstreep": 5}`
    - **Opties:** A) 15 · B) 1 · C) 5
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 1 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is. · 15 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.
  - `G5-VBN-E01-claude-bank-127` (Claude G2, bank, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 20.
Hoeveel peren zijn er?
    - **Tekening:** `{"max": 200, "soort": "staafdiagram", "staven": [{"naam": "peren", "waarde": 60}, {"naam": "bananen", "waarde": 120}, {"naam": "druiven", "waarde": 160}, {"naam": "kersen", "waarde": 200}, {"naam": "pruimen", "waarde": 20}], "cijfer_om": 100, "perstreep": 20}`
    - **Opties:** A) 60 · B) 3 · C) 40
    - **Antwoord:** 60  (controle: ok)
    - **Fout-hints (Claude):** 3 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is. · 40 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.

- **Hint 1 (te schrijven):** Zoek de staaf van het ding uit de vraag. Welk getal hoort bij de top van de staaf? Staat daar geen getal, zoek dan het getal vlak eronder.
- **Hint 2 (te schrijven):** Zoek het getal vlak onder de top van de staaf. Kijk in de vraag hoeveel elk streepje is, en tel vanaf dat getal zo veel per streepje verder tot de top.
- **Ouderzin:** Je kind leest een staafdiagram af. Elk streepje is meer dan één.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `streepjes geteld` (fout = antwoord gedeeld door getal1) → Je hebt de streepjes geteld. Kijk in de vraag hoeveel elk streepje is. Tel bij elk streepje zo veel verder.  [nieuw]
  - `getal vlak onder de top` (fout = het getal vlak onder de top) → Dat is het getal vlak onder de top. Tel de streepjes erboven er nog bij: kijk in de vraag hoeveel elk streepje is.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Is dat wat één streepje waard is? De vraag gaat over de hele staaf. Hoeveel streepjes hoog is de staaf?  [nieuw]
  - `één streepje te veel` (fout = antwoord + getal1) → Bijna! Dat is één streepje te veel. Kijk goed waar de top van de staaf is.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − getal1) → Bijna! Dat is één streepje te weinig. Kijk goed waar de top van de staaf is.  [nieuw]
  - `andere staaf` (Claudes sleutel: grafiek-verkeerd-afgelezen) → Dat is een andere staaf. Zoek de staaf van het ding uit de vraag.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zoek de staaf van het ding uit de vraag. Staat er een getal bij de top? Dan is dat het antwoord. Staat er geen getal, zoek dan het getal vlak eronder. Tel de streepjes erboven erbij: kijk in de vraag hoeveel elk streepje is.  [nieuw]
- Status: hints klaar

## Somtype 2: [staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er meer dan [naam]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[staafdiagram] Elk streepje is #. ⏎ Hoeveel [naam] zijn er meer dan [naam]?” (koppeling: claudeId)
- Items: **106** · Claude-doelen: G2 (106) · regel: D-SCHAAL-AS10, D-SCHAAL-AS25, G26-staaf
- Getallenruimte: 0–1.000, 0–10, 0–100, 0–20 · type: meerkeuze
- Didactiek-besluit (G4-twijfel, 1 okt): getal om de 10, 1 streep = 5, getal om de 25, 1 streep = 5 — zie g4/besluiten_twijfel.md + besluit Dave
- Hint-richting: Zoek het getal vlak onder de staaf. Spring dan verder met 5.
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (122), verkeerde-bewerking (47), andere-deel-genomen (42), streepjes-geteld (1)
- Verschillende Claude-fout-hints: 3 (meest: “Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.”)
- Voorbeelden:
  - `G5-VBN-E01-claude-bank-040` (Claude G2, bank, niveau 2 → toepassen)
    - **Opgave:** Elk streepje is 5.
Hoeveel vissen zijn er meer dan vogels?
    - **Tekening:** `{"max": 30, "soort": "staafdiagram", "staven": [{"naam": "vogels", "waarde": 15}, {"naam": "vissen", "waarde": 25}, {"naam": "paarden", "waarde": 5}], "cijfer_om": 10, "perstreep": 5}`
    - **Opties:** A) 40 · B) 25 · C) 10
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 40 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 25 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G5-VBN-E01-claude-bank-007` (Claude G2, bank, niveau 3 → toepassen)
    - **Opgave:** Elk streepje is 20.
Hoeveel stiften zijn er meer dan potloden?
    - **Tekening:** `{"max": 200, "soort": "staafdiagram", "staven": [{"naam": "boeken", "waarde": 140}, {"naam": "potloden", "waarde": 20}, {"naam": "stiften", "waarde": 60}, {"naam": "pennen", "waarde": 100}], "cijfer_om": 100, "perstreep": 20}`
    - **Opties:** A) 20 · B) 2 · C) 40
    - **Antwoord:** 40  (controle: ok)
    - **Fout-hints (Claude):** 2 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is. · 20 → Leg je vinger op de rij of staaf uit de vraag en schuif hem naar de as. Kijk hoeveel elk streepje waard is.

- **Hint 1 (te schrijven):** Zoek de twee staven uit de vraag. Lees bij allebei af hoeveel het er zijn. Kijk in de vraag hoeveel elk streepje is.
- **Hint 2 (te schrijven):** Hoeveel meer? Haal het kleinste getal van het grootste af.
- **Ouderzin:** Je kind leest twee staven af in een staafdiagram en rekent uit hoeveel meer het ene is dan het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (Claudes sleutel: verkeerde-bewerking) → Je hebt de twee staven opgeteld. De vraag is hoeveel meer: haal het kleinste getal van het grootste af.  [Claude, taalfix]
  - `één staaf` (Claudes sleutel: andere-deel-genomen) → Dat is wat één staaf laat zien. De vraag is hoeveel meer: lees beide staven af en haal het kleinste getal van het grootste af.  [Claude, taalfix]
  - `streepjes geteld` (fout = antwoord gedeeld door getal1) → Je hebt geteld hoeveel streepjes de ene staaf hoger is. Kijk in de vraag hoeveel elk streepje is. Tel per streepje zo veel verder.  [nieuw]
  - `getal uit de vraag` (fout = een getal uit de vraag) → Is dat wat één streepje waard is? De vraag is hoeveel meer. Lees allebei de staven af.  [nieuw]
  - `één streepje te veel` (fout = antwoord + getal1) → Bijna! Dat is één streepje te veel. Kijk nog eens goed waar de toppen van de twee staven zijn.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − getal1) → Bijna! Dat is één streepje te weinig. Kijk nog eens goed waar de toppen van de twee staven zijn.  [nieuw]
  - `andere fout` (andere fout) → Lees de twee staven uit de vraag af. Kijk hoeveel elk streepje is. Hoeveel meer? Haal het kleinste getal van het grootste af.  [nieuw]
- Status: hints klaar

## Somtype 3: [tabel] Hoeveel [naam] in totaal?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[tabel] Hoeveel [naam] in totaal?” (koppeling: claudeId)
- Items: **57** · Claude-doelen: G1 (57) · regel: G25-tabel
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (31), grafiek-verkeerd-afgelezen (30), deel-vergeten-bij-splitsen (27), andere-deel-genomen (26)
- Verschillende Claude-fout-hints: 2 (meest: “Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.”)
- Voorbeelden:
  - `G5-VBN-E01-claude-bank-278` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel druiven in totaal?
    - **Tekening:** `{"rijen": [{"naam": "appels", "waarden": [75, 31, 61, 18]}, {"naam": "peren", "waarden": [23, 52, 12, 37]}, {"naam": "bananen", "waarden": [44, 75, 31, 61]}, {"naam": "druiven", "waarden": [68, 23, 52, 12]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 68 · B) 128 · C) 155
    - **Antwoord:** 155  (controle: ok)
    - **Fout-hints (Claude):** 128 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G5-VBN-E01-claude-bank-228` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel stiften in totaal?
    - **Tekening:** `{"rijen": [{"naam": "boeken", "waarden": [125, 215, 85, 175]}, {"naam": "potloden", "waarden": [190, 60, 150, 250]}, {"naam": "stiften", "waarden": [35, 125, 215, 85]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 460 · B) 600 · C) 375
    - **Antwoord:** 460  (controle: ok)
    - **Fout-hints (Claude):** 375 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag. Een rij loopt van links naar rechts.
- **Hint 2 (te schrijven):** Zoek de rij van het ding uit de vraag. Tel alle getallen in die rij bij elkaar. Sla er geen over.
- **Ouderzin:** Je kind telt alle getallen in één rij van een tabel bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere rij` (fout = som van de rij) → Dat is het totaal van een andere rij. Zoek eerst de rij van het ding uit de vraag.  [nieuw]
  - `kolom opgeteld` (fout = som van de kolom) → Je hebt een kolom opgeteld. Tel de getallen in de rij van het ding uit de vraag bij elkaar.  [nieuw]
  - `één getal` (fout = andere cel) → Heb je maar één getal uit de tabel genomen? In totaal betekent: tel alle getallen in de rij bij elkaar.  [nieuw]
  - `niet alles opgeteld` (fout = som van twee cellen) → Je hebt niet alles opgeteld. Tel alle getallen in de rij bij elkaar. Sla er geen over.  [nieuw]
  - `niet alles opgeteld (één vergeten)` (Claudes sleutel: deel-vergeten-bij-splitsen) → Je hebt niet alles opgeteld. Tel alle getallen in de rij bij elkaar. Sla er geen over.  [Claude, taalfix]
  - `afgetrokken` (fout = verschil van twee cellen) → Je hebt getallen van elkaar afgehaald. In totaal betekent: alles bij elkaar optellen.  [nieuw]
  - `andere fout` (andere fout) → Tel alle getallen in de rij van het ding uit de vraag bij elkaar: van elke dag één. Tel de andere rijen niet mee.  [nieuw]
- Status: hints klaar

## Somtype 4: [tabel] Hoeveel [naam] meer op [naam] dan op [naam]?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “[tabel] Hoeveel [naam] meer op [naam] dan op [naam]?” (koppeling: claudeId)
- Items: **30** · Claude-doelen: G1 (30) · regel: G25-tabel
- Getallenruimte: 0–1.000, 0–100 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (19), grafiek-verkeerd-afgelezen (14), andere-deel-genomen (14), getal-overgenomen (13)
- Verschillende Claude-fout-hints: 2 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G5-VBN-E01-claude-bank-307` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel konijnen meer op donderdag dan op woensdag?
    - **Tekening:** `{"rijen": [{"naam": "honden", "waarden": [250, 85, 110, 125]}, {"naam": "katten", "waarden": [150, 60, 215, 110]}, {"naam": "konijnen", "waarden": [85, 150, 35, 125]}, {"naam": "vogels", "waarden": [150, 190, 250, 215]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 155 · B) 90 · C) 125
    - **Antwoord:** 90  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G5-VBN-E01-claude-bank-293` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel stiften meer op maandag dan op donderdag?
    - **Tekening:** `{"rijen": [{"naam": "boeken", "waarden": [85, 175, 35, 125]}, {"naam": "potloden", "waarden": [150, 250, 110, 190]}, {"naam": "stiften", "waarden": [215, 85, 175, 35]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 180 · B) 510 · C) 40
    - **Antwoord:** 180  (controle: ok)
    - **Fout-hints (Claude):** 510 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag. Een rij loopt van links naar rechts. Zoek in die rij de getallen van de twee dagen.
- **Hint 2 (te schrijven):** Hoeveel meer? Haal het kleinste getal van het grootste af.
- **Ouderzin:** Je kind zoekt twee getallen in een tabel en rekent uit hoeveel meer het ene is dan het andere.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één getal` (fout = andere cel) → Heb je één getal uit de tabel genomen? Je hebt er twee nodig: die van de twee dagen, in de rij van het ding. Haal dan het kleinste getal van het grootste af.  [nieuw]
  - `som van de rij` (fout = som van de rij) → Je hebt een hele rij bij elkaar opgeteld. Je hebt alleen de getallen van de twee dagen nodig. Haal het kleinste getal van het grootste af.  [nieuw]
  - `opgeteld` (fout = som van twee cellen) → Je hebt twee getallen opgeteld. Hoeveel meer? Haal het kleinste getal van het grootste af.  [nieuw]
  - `verkeerde getallen afgetrokken` (fout = verschil van twee cellen) → Je hebt twee andere getallen van elkaar afgehaald. Kijk goed: de rij van het ding, en de twee dagen uit de vraag.  [nieuw]
  - `andere fout` (andere fout) → Je hebt twee getallen nodig: die van de twee dagen, in de rij van het ding. Haal dan het kleinste getal van het grootste af.  [nieuw]
- Status: hints klaar

## Somtype 5: [tabel] Hoeveel [naam] op [naam]?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “[tabel] Hoeveel [naam] op [naam]?” (koppeling: claudeId)
- Items: **30** · Claude-doelen: G1 (30) · regel: G25-tabel
- Getallenruimte: 0–1.000, 0–100 · type: meerkeuze
- Denkfouten (Claude): andere-deel-genomen (38), grafiek-verkeerd-afgelezen (22)
- Verschillende Claude-fout-hints: 1 (meest: “Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?”)
- Voorbeelden:
  - `G5-VBN-E01-claude-bank-336` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel appels op vrijdag?
    - **Tekening:** `{"rijen": [{"naam": "appels", "waarden": [60, 150, 250, 110, 190]}, {"naam": "peren", "waarden": [125, 215, 85, 175, 35]}, {"naam": "bananen", "waarden": [190, 60, 150, 250, 110]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]}`
    - **Opties:** A) 190 · B) 760 · C) 60
    - **Antwoord:** 190  (controle: ok)
    - **Fout-hints (Claude):** 760 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?
  - `G5-VBN-E01-claude-bank-314` (Claude G1, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel bussen op donderdag?
    - **Tekening:** `{"rijen": [{"naam": "fietsen", "waarden": [190, 60, 150, 250]}, {"naam": "bussen", "waarden": [35, 125, 215, 85]}, {"naam": "treinen", "waarden": [110, 190, 60, 150]}], "soort": "tabel", "kolommen": ["maandag", "dinsdag", "woensdag", "donderdag"]}`
    - **Opties:** A) 85 · B) 150 · C) 460
    - **Antwoord:** 85  (controle: ok)
    - **Fout-hints (Claude):** 460 → Je hebt het andere stuk uitgerekend. Lees de vraag nog eens: wat wil die precies weten?

- **Hint 1 (te schrijven):** Zoek in de tabel de rij van het ding uit de vraag. Een rij loopt van links naar rechts.
- **Hint 2 (te schrijven):** Zoek de rij van het ding uit de vraag. Ga in die rij naar de kolom van de dag uit de vraag. Een kolom loopt van boven naar beneden. Het getal in dat vak is het antwoord.
- **Ouderzin:** Je kind leest één getal af in een tabel.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere cel` (fout = andere cel) → Dat getal staat in een ander vak. Zoek de rij van het ding en de kolom van de dag. Waar die twee elkaar raken, staat het antwoord.  [nieuw]
  - `som van de rij` (fout = som van de rij) → Je hebt een hele rij bij elkaar opgeteld. De vraag gaat over één dag: kijk alleen in het vak van die dag.  [nieuw]
  - `som van de kolom` (fout = som van de kolom) → Je hebt een hele kolom bij elkaar opgeteld. De vraag gaat over één ding: kijk alleen in het vak van dat ding.  [nieuw]
  - `andere fout` (andere fout) → Zoek de rij van het ding en de kolom van de dag. Waar die twee elkaar raken, staat het antwoord. Je hoeft niets uit te rekenen.  [nieuw]
- Status: hints klaar
