# G5-MEET-E04 — Liter en milliliter

Onze omschrijving: Liter/ml (1 L = 1000 ml); maatbeker; referenties · in onze bank: 8 items

Claude-vragen gemapt: **183** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [maatbeker] Hoeveel milliliter zit er in de beker?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[maatbeker] Hoeveel milliliter zit er in de beker?” (koppeling: claudeId)
- Items: **169** · Claude-doelen: M11 (169) · regel: G5-M02-maatbeker
- Getallenruimte: 0–1.000, 0–10.000, 0–100 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (308), deel-vergeten-bij-splitsen (30)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk bij welk streepje het drinken staat. Hoeveel milliliter is elk streepje?”)
- Voorbeelden:
  - `G5-MEET-E04-claude-bank-083` (Claude M11, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel milliliter zit er in de beker?
    - **Tekening:** `{"max": 200, "tot": 90, "soort": "maatbeker", "cijfer_om": 40, "perstreep": 10}`
    - **Opties:** A) 81 · B) 100 · C) 90
    - **Antwoord:** 90  (controle: ok)
    - **Fout-hints (Claude):** 81 → Kijk bij welk streepje het drinken staat. Hoeveel milliliter is elk streepje? · 100 → Kijk bij welk streepje het drinken staat. Hoeveel milliliter is elk streepje?
  - `G5-MEET-E04-claude-bank-160` (Claude M11, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel milliliter zit er in de beker?
    - **Tekening:** `{"max": 200, "tot": 120, "soort": "maatbeker", "cijfer_om": 50, "perstreep": 10}`
    - **Opties:** A) 100 · B) 120 · C) 102
    - **Antwoord:** 120  (controle: ok)
    - **Fout-hints (Claude):** 100 → Je bent bijna klaar, maar er ontbreekt nog een stap. Kijk wat je al hebt uitgerekend en wat er nog bij moet.

- **Hint 1 (te schrijven):** Kijk waar het drinken ophoudt. Welk getal op de beker staat daar net onder?
- **Hint 2 (te schrijven):** Hoeveel milliliter is één streepje? Tel hoeveel sprongetjes het is van het ene getal naar het volgende getal. Tel dan vanaf het getal verder, streepje voor streepje, tot de bovenkant van het drinken.
- **Ouderzin:** Je kind leest af hoeveel milliliter er in een maatbeker zit.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `streepjes als 1 geteld` (fout = streepjes als 1 geteld) → Eén streepje is niet één milliliter. Hoeveel milliliter is één sprongetje?  [nieuw]
  - `één streepje ernaast` (fout = één streepje ernaast) → Je zit één streepje ernaast. Tel de streepjes nog eens vanaf het getal.  [nieuw]
  - `te veel` (fout = antwoord + 1 of meer) → Dat is te veel. Zoek het getal op de beker dat net onder de bovenkant van het drinken staat. Hoeveel milliliter is één streepje? Tel vanaf dat getal de streepjes tot de bovenkant van het drinken.  [nieuw]
  - `te weinig` (fout = antwoord − 1 of meer) → Dat is te weinig. Zoek het getal op de beker dat net onder de bovenkant van het drinken staat. Hoeveel milliliter is één streepje? Tel de streepjes erboven er nog bij, tot de bovenkant van het drinken.  [nieuw]
  - `andere fout` (andere fout) → Zoek het getal op de beker dat net onder de bovenkant van het drinken staat. Hoeveel milliliter is één streepje? Tel vanaf dat getal de streepjes tot de bovenkant van het drinken.  [nieuw]
- Status: hints klaar

## Somtype 2: # L = □ ml

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# L = □ ml” (koppeling: claudeId)
- Items: **8** · Claude-doelen: M12 (8) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: invullen
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (13), getal-overgenomen (3)
- Verschillende Claude-fout-hints: 2 (meest: “Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?”)
- Voorbeelden:
  - `G5-MEET-E04-claude-bank-006` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 2 L = □ ml
    - **Antwoord:** 2000  (controle: ok)
    - **Fout-hints (Claude):** 6 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 2 → Dat getal staat al in de som. Wat moet je ermee dóén? Lees de vraag nog eens en zoek de bewerking.
  - `G5-MEET-E04-claude-bank-004` (Claude M12, bank, niveau 3 → toepassen)
    - **Opgave:** 6 L = □ ml
    - **Antwoord:** 6000  (controle: ok)
    - **Fout-hints (Claude):** 18 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het? · 600 → Gebruik de maattrap: elke stap is keer 10 of gedeeld door 10. Hoeveel stappen zijn het?

- **Hint 1 (te schrijven):** Eén liter (L) is duizend milliliter (ml). Hoeveel liter zijn het?
- **Hint 2 (te schrijven):** Doe het aantal liter keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent liters om naar milliliters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén liter is duizend milliliter: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén liter is duizend milliliter: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `het getal uit de som (sleutel)` (Claudes sleutel: getal-overgenomen) → Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.  [Claude, taalfix]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter is duizend milliliter. Doe het aantal liter keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar

## Somtype 3: [referentie] Hoeveel gaat er ongeveer in …?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[referentie] Hoeveel gaat er ongeveer in …?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: M27 (4) · regel: G5-M06-referentie
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): tiental-ernaast (4), eenheid-verkeerd-omgerekend (2), schatting-verkeerd (1), plaatswaarde-verkeerd (1)
- Verschillende Claude-fout-hints: 8 (meest: “1 ml is maar een paar druppels. Kijk nog eens hoe groot een pak melk is.”)
- Voorbeelden:
  - `G5-MEET-E04-claude-bank-185` (Claude M27, ai, niveau 1 → basis)
    - **Opgave:** Hoeveel drinken zit er ongeveer in een gewoon pak melk uit de winkel?
    - **Opties:** A) 1 ml · B) 10 L · C) 1 L
    - **Antwoord:** 1 L  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1 ml → 1 ml is maar een paar druppels. Kijk nog eens hoe groot een pak melk is. · 10 L → 10 L is een volle emmer water. Past dat in een pak dat je met één hand vasthoudt?
    - **Uitleg (Claude):** In een gewoon pak melk zit 1 liter. Je kunt er ongeveer vijf glazen mee vullen. De liter is de bekende maat voor drinken.
  - `G5-MEET-E04-claude-bank-186` (Claude M27, ai, niveau 2 → toepassen)
    - **Opgave:** Hoeveel drinken gaat er ongeveer in een gewoon glas?
    - **Opties:** A) 20 ml · B) 200 ml · C) 2 L
    - **Antwoord:** 200 ml  (controle: n.v.t.)
    - **Fout-hints (Claude):** 2 L → 2 L zijn twee pakken melk. Past dat allemaal in één glas? · 20 ml → 20 ml is maar een paar slokjes uit een lepel. Denk aan een vol glas.
    - **Uitleg (Claude):** In een glas gaat ongeveer 200 ml. Uit een pak melk van 1 liter vul je dus ongeveer vijf glazen. Milliliters passen goed bij kleine hoeveelheden drinken.

- **Hint 1 (te schrijven):** Stel je voor dat je het vult. Past er een beetje in, of heel veel?
- **Hint 2 (te schrijven):** Een pak melk is één liter. Een milliliter is heel weinig: in een theelepel gaat al ongeveer vijf milliliter. Welke maat past het best?
- **Ouderzin:** Je kind schat hoeveel er in iets past, met maten die het kent.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te weinig (15 L)` (15 L) → Dat is te weinig. 15 L is anderhalve emmer. Daarmee is een bad niet vol.  [nieuw]
  - `te veel (1500 L)` (1500 L) → Dat is veel te veel. Zoveel water is een klein zwembad vol. Tel eens hoeveel emmers er in een bad passen.  [nieuw]
  - `te veel (100 L)` (100 L) → Dat is veel te veel. In 100 L zit al meer dan een half bad. Een emmer kun je nog tillen.  [nieuw]
  - `te weinig (1 L)` (1 L) → Dat is te weinig. 1 L is één pak melk. Zo weinig water staat er niet in een volle emmer.  [nieuw]
  - `te weinig (1 ml)` (1 ml) → Dat is veel te weinig. 1 ml is nog minder dan een theelepel. Kijk nog eens hoe groot een pak melk is.  [nieuw]
  - `te veel (10 L)` (10 L) → Dat is veel te veel. 10 L is een volle emmer water. Past dat in een pak dat je met één hand vasthoudt?  [nieuw]
  - `te weinig (20 ml)` (20 ml) → Dat is te weinig. 20 ml is maar een paar lepels vol. Denk aan een vol glas.  [nieuw]
  - `te veel (2 L)` (2 L) → Dat is veel te veel. 2 L zijn twee pakken melk. Past dat allemaal in één glas?  [nieuw]
  - `andere maat` (Claudes sleutel (tekst per item)) → Claudes tekst per foute optie: … is zo groot/zwaar als … (iets dat je kent). Past dat?  [Claude, ok]
  - `andere fout` (andere fout) → Zie het voor je. Vergelijk het met iets dat je kent. Welke maat past het best?  [nieuw]
- Status: hints klaar

## Somtype 4: Een emmer bevat # L. Hoeveel ml is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een emmer bevat # L. Hoeveel ml is dat?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: M12 (2) · regel: G5-M01-omrekenen
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (6)
- Verschillende Claude-fout-hints: 3 (meest: “Een nul te weinig. 1 L is 1000 ml.”)
- Voorbeelden:
  - `G5-MEET-E04-claude-bank-012` (Claude M12, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een emmer bevat 5 L. Hoeveel ml is dat?
    - **Antwoord:** 5000  (controle: ok)
    - **Fout-hints (Claude):** 500 → Een nul te weinig. 1 L is 1000 ml. · 50.000 → Een nul te veel. 1 L is 1000 ml. · 5 → Het getal verandert als de eenheid verandert. Van l naar ml is keer 1.000.
    - **Uitleg (Claude):** 1 L = 1000 ml. Dus 5 L = 5 × 1000 = 5000 ml.
  - `G5-MEET-E04-claude-bank-010` (Claude M12, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een emmer bevat 8 L. Hoeveel ml is dat?
    - **Antwoord:** 8000  (controle: ok)
    - **Fout-hints (Claude):** 800 → Een nul te weinig. 1 L is 1000 ml. · 80.000 → Een nul te veel. 1 L is 1000 ml. · 8 → Het getal verandert als de eenheid verandert. Van l naar ml is keer 1.000.
    - **Uitleg (Claude):** 1 L = 1000 ml. Dus 8 L = 8 × 1000 = 8000 ml.

- **Hint 1 (te schrijven):** Eén liter (L) is duizend milliliter (ml). Hoeveel liter zit er in de emmer?
- **Hint 2 (te schrijven):** Doe het aantal liter keer duizend: zet er drie nullen achter.
- **Ouderzin:** Je kind rekent liters om naar milliliters.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nul te veel` (fout = antwoord × 10) → Dat is te veel: er staat een nul te veel achter. Eén liter is duizend milliliter: zet er drie nullen achter.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is te weinig: er mist een nul. Eén liter is duizend milliliter: zet er drie nullen achter.  [nieuw]
  - `het getal uit de som` (fout = getal1) → Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.  [nieuw]
  - `te veel` (fout = antwoord + 2 of meer) → Dat is te veel. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [nieuw]
  - `te weinig` (fout = antwoord − 2 of meer) → Dat is te weinig. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [nieuw]
  - `anders omgerekend (sleutel)` (Claudes sleutel: eenheid-verkeerd-omgerekend) → Dat klopt niet. Eén liter is duizend milliliter. Doe het aantal liter keer duizend.  [Claude, taalfix]
  - `andere fout` (andere fout) → Eén liter is duizend milliliter. Doe het aantal liter keer duizend: zet er drie nullen achter.  [nieuw]
- Status: hints klaar
