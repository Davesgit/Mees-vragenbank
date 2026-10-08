# G6-VBN-E02 — Beelddiagram, cirkeldiagram en lijngrafiek aflezen

Onze omschrijving: Beelddiagram (beeld >1); eenvoudige cirkel + lijngrafiek · in onze bank: 8 items

Claude-vragen gemapt: **180** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [lijngrafiek] Hoeveel [ding] kwamen er bij van [maand] naar [maand]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[lijngrafiek] Hoeveel [ding] kwamen er bij van [maand] naar [maand]?” (koppeling: claudeId)
- Items: **60** · Claude-doelen: G3 (60) · regel: G6-D01-lijngrafiek
- Getallenruimte: grafiek tot 200 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (58), getal-overgenomen (32), verkeerde-bewerking (30)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G6-VBN-E02-claude-bank-049` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel kaartjes waren er in maart meer dan in februari?
    - **Tekening:** `{"max": 200, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 30}, {"naam": "februari", "waarde": 80}, {"naam": "maart", "waarde": 110}, {"naam": "april", "waarde": 160}], "cijfer_om": 50, "perstreep": 10, "maxVoor276": 100, "titel": "Verkochte kaartjes per maand"}`
    - **Opties:** A) 3 · B) 30 · C) 20
    - **Antwoord:** 30  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G6-VBN-E02-claude-bank-016` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel broodjes waren er in maart meer dan in februari?
    - **Tekening:** `{"max": 25, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 5}, {"naam": "februari", "waarde": 5}, {"naam": "maart", "waarde": 25}, {"naam": "april", "waarde": 15}], "cijfer_om": 25, "perstreep": 5, "maxVoor276": 75, "titel": "Verkochte broodjes per maand"}`
    - **Opties:** A) 25 · B) 20 · C) 30
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** 130 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek de twee maanden uit de vraag onder de grafiek. Lees bij allebei af hoe hoog de stip staat. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes.
- **Hint 2 (te schrijven):** Hoeveel kwamen er bij? Haal het aantal van de eerste maand af van het aantal van de tweede maand.
- **Ouderzin:** Je kind leest in een lijngrafiek twee maanden af en rekent uit hoeveel er van de ene naar de andere maand bij kwamen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de tweede maand` (Claudes sleutel: getal-overgenomen) → Dat is het aantal in de tweede maand van de vraag. Hoeveel waren het in de eerste maand? Haal het aantal van de eerste maand ervan af: dat is wat erbij kwam.  [Claude, taalfix]
  - `opgeteld` (Claudes sleutel: verkeerde-bewerking) → Je hebt de twee maanden bij elkaar opgeteld. De vraag is hoeveel er bij kwamen. Hoeveel meer is de tweede maand dan de eerste?  [Claude, taalfix]
  - `de tweede maand (regel)` (fout = de tweede maand uit de vraag) → Dat is het aantal in de tweede maand van de vraag. Hoeveel waren het in de eerste maand? Haal het aantal van de eerste maand ervan af: dat is wat erbij kwam.  [nieuw]
  - `streepjes geteld` (fout = antwoord : perstreep) → Is dat het aantal streepjes? Elk streepje is meer dan één. Hoeveel is elk streepje? Reken dan het aantal streepjes keer dat getal.  [nieuw]
  - `één streepje te veel` (fout = antwoord + perstreep) → Dat is één streepje te veel. Lees de twee stippen nog eens af en tel de streepjes goed.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − perstreep) → Dat is één streepje te weinig. Lees de twee stippen nog eens af en tel de streepjes goed.  [nieuw]
  - `anders afgelezen` (Claudes sleutel: grafiek-verkeerd-afgelezen) → Lees de twee stippen nog eens af. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes. Haal dan de eerste maand van de tweede af.  [Claude, taalfix]
  - `andere fout` (andere fout) → Lees de twee maanden uit de vraag af. Haal het aantal van de eerste maand af van het aantal van de tweede maand.  [nieuw]
- Status: hints klaar

## Somtype 2: [lijngrafiek] Hoeveel [ding] waren er in [maand]?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[lijngrafiek] Hoeveel [ding] waren er in [maand]?” (koppeling: claudeId)
- Items: **60** · Claude-doelen: G3 (60) · regel: G6-D01-lijngrafiek
- Getallenruimte: grafiek tot 200 · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (69), klok-verkeerd-gelezen (42), plaatswaarde-verkeerd (9)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G6-VBN-E02-claude-bank-063` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel boeken waren er in februari?
    - **Tekening:** `{"max": 50, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 10}, {"naam": "februari", "waarde": 35}, {"naam": "maart", "waarde": 40}, {"naam": "april", "waarde": 50}], "cijfer_om": 25, "perstreep": 5, "maxVoor276": 75, "titel": "Geleende boeken per maand"}`
    - **Opties:** A) 30 · B) 7 · C) 35
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G6-VBN-E02-claude-bank-109` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel kaartjes waren er in maart?
    - **Tekening:** `{"max": 50, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 15}, {"naam": "februari", "waarde": 30}, {"naam": "maart", "waarde": 35}, {"naam": "april", "waarde": 50}], "cijfer_om": 25, "perstreep": 5, "maxVoor276": 100, "titel": "Verkochte kaartjes per maand"}`
    - **Opties:** A) 50 · B) 35 · C) 40
    - **Antwoord:** 35  (controle: ok)
    - **Fout-hints (Claude):** 15 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Zoek de maand uit de vraag onder de grafiek. Ga recht omhoog naar de stip.
- **Hint 2 (te schrijven):** Zoek het getal langs de zijkant op dezelfde hoogte als de stip, of net eronder. Tel dan de streepjes tot de stip. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes.
- **Ouderzin:** Je kind leest in een lijngrafiek af hoeveel het er in één maand waren.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere maand` (Claudes sleutel: klok-verkeerd-gelezen) → Dat is het aantal bij een andere maand. Zoek eerst de maand uit de vraag onder de grafiek. Ga dan recht omhoog naar de stip.  [Claude, taalfix]
  - `getal onder de stip` (Claudes sleutel: plaatswaarde-verkeerd) → Dat is het getal langs de zijkant net onder de stip. Staat de stip precies op dat getal? Tel de streepjes vanaf dat getal tot de stip.  [Claude, taalfix]
  - `andere maand (regel)` (fout = een andere maand) → Dat is het aantal bij een andere maand. Zoek eerst de maand uit de vraag onder de grafiek. Ga dan recht omhoog naar de stip.  [nieuw]
  - `getal onder de stip (regel)` (fout = het getal onder de stip) → Dat is het getal langs de zijkant net onder de stip. Staat de stip precies op dat getal? Tel de streepjes vanaf dat getal tot de stip.  [nieuw]
  - `getal net boven de stip` (fout = het getal net boven de stip) → Dat is het getal langs de zijkant net boven de stip. Zoek het getal op of net onder de stip en tel de streepjes verder tot de stip.  [nieuw]
  - `streepjes geteld` (fout = antwoord : perstreep) → Is dat het aantal streepjes? Elk streepje is meer dan één. Hoeveel is elk streepje? Reken dan het aantal streepjes keer dat getal.  [nieuw]
  - `één streepje te veel` (fout = antwoord + perstreep) → Dat is één streepje te veel. Tel vanaf het getal langs de zijkant de streepjes tot de stip nog eens.  [nieuw]
  - `één streepje te weinig` (fout = antwoord − perstreep) → Dat is één streepje te weinig. Tel vanaf het getal langs de zijkant de streepjes tot de stip nog eens.  [nieuw]
  - `anders afgelezen` (Claudes sleutel: grafiek-verkeerd-afgelezen) → Lees de stip nog eens af. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes. Tel dan vanaf het getal op of net onder de stip verder.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zoek de maand uit de vraag en ga recht omhoog naar de stip. Tel vanaf het getal langs de zijkant op of net onder de stip de streepjes verder.  [nieuw]
- Status: hints klaar

## Somtype 3: [lijngrafiek] Hoeveel [ding] waren er in alle maanden samen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[lijngrafiek] Hoeveel [ding] waren er in alle maanden samen?” (koppeling: claudeId)
- Items: **60** · Claude-doelen: G3 (60) · regel: G6-D01-lijngrafiek
- Getallenruimte: grafiek tot 200 · type: meerkeuze
- Denkfouten (Claude): klok-verkeerd-gelezen (48), deel-vergeten-bij-splitsen (26), grafiek-verkeerd-afgelezen (24), getal-overgenomen (22)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G6-VBN-E02-claude-bank-172` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel broodjes waren er in alle maanden samen?
    - **Tekening:** `{"max": 25, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 15}, {"naam": "februari", "waarde": 5}, {"naam": "maart", "waarde": 25}, {"naam": "april", "waarde": 25}], "cijfer_om": 25, "perstreep": 5, "maxVoor276": 75, "titel": "Verkochte broodjes per maand"}`
    - **Opties:** A) 45 · B) 70 · C) 25
    - **Antwoord:** 70  (controle: ok)
    - **Fout-hints (Claude):** 75 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G6-VBN-E02-claude-bank-129` (Claude G3, bank, niveau 3 → toepassen)
    - **Opgave:** Hoeveel kaartjes waren er in alle maanden samen?
    - **Tekening:** `{"max": 600, "soort": "lijngrafiek", "punten": [{"naam": "januari", "waarde": 100}, {"naam": "februari", "waarde": 200}, {"naam": "maart", "waarde": 250}, {"naam": "april", "waarde": 500}, {"naam": "mei", "waarde": 550}], "cijfer_om": 200, "perstreep": 50, "maxVoor276": 500, "titel": "Verkochte kaartjes per maand"}`
    - **Opties:** A) 32 · B) 1400 · C) 1600
    - **Antwoord:** 1600  (controle: ok)
    - **Fout-hints (Claude):** 1000 → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Lees bij elke maand af hoe hoog de stip staat. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes.
- **Hint 2 (te schrijven):** Tel de aantallen van alle maanden bij elkaar op. Tel elke maand precies één keer.
- **Ouderzin:** Je kind leest in een lijngrafiek alle maanden af en telt ze bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één maand` (Claudes sleutel: getal-overgenomen) → Is dat het aantal van één maand? De vraag gaat over alle maanden samen. Tel de aantallen van alle maanden bij elkaar op.  [Claude, taalfix]
  - `een paar maanden` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is nog niet alles. Heb je elke maand precies één keer meegeteld? Tel de aantallen van alle maanden bij elkaar op.  [Claude, taalfix]
  - `niet elke maand één keer` (Claudes sleutel: klok-verkeerd-gelezen) → Tel nog eens. Heb je elke maand precies één keer meegeteld? Tel de aantallen van alle maanden bij elkaar op.  [Claude, taalfix]
  - `maand vergeten (regel)` (fout = alle maanden samen min één maand) → Tel nog eens. Heb je elke maand precies één keer meegeteld? Tel de aantallen van alle maanden bij elkaar op.  [nieuw]
  - `maand dubbel (regel)` (fout = alle maanden samen plus één maand) → Tel nog eens. Heb je elke maand precies één keer meegeteld? Tel de aantallen van alle maanden bij elkaar op.  [nieuw]
  - `één maand (regel)` (fout = de waarde van één maand) → Is dat het aantal van één maand? De vraag gaat over alle maanden samen. Tel de aantallen van alle maanden bij elkaar op.  [nieuw]
  - `streepjes geteld` (fout = antwoord : perstreep) → Is dat het aantal streepjes? Elk streepje is meer dan één. Hoeveel is elk streepje? Lees zo bij elke maand af hoeveel het er waren, en tel die aantallen op.  [nieuw]
  - `anders afgelezen` (Claudes sleutel: grafiek-verkeerd-afgelezen) → Lees bij elke maand de stip goed af. Hoeveel is elk streepje? Neem twee getallen langs de zijkant die vlak boven elkaar staan. Tel vanaf het onderste getal de streepjes omhoog, tot en met het streepje bij het bovenste getal. Hoeveel meer is het bovenste getal? Deel dat door het aantal streepjes. Tel daarna alle maanden op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Lees bij elke maand het aantal af en tel alle maanden bij elkaar op.  [nieuw]
- Status: hints klaar
