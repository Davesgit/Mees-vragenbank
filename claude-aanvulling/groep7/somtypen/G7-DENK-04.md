# G7-DENK-04 — Wiskundewoorden en hulpmiddelen

Onze omschrijving: Wiskundetaal & instrumenten · in onze bank: 8 items

Claude-vragen gemapt: **147** in **6** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Zoek het verschil van # en #. Welke som maak je?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Zoek het verschil van # en #. Welke som maak je?” (koppeling: claudeId)
- Items: **80** · Claude-doelen: W2 (80) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 80 items
- Denkfouten (Claude): omgekeerd-gedeeld (80), verkeerde-bewerking (80)
- Verschillende Claude-fout-hints: 2 (meest: “Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel.”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-069` (Claude W2, bank, niveau 1 → basis)
    - **Opgave:** Zoek het verschil van 28 en 12. Welke som maak je?
    - **Opties:** A) 28 + 12 · B) 28 − 12 · C) 12 − 28
    - **Antwoord:** 28 − 12  (controle: n.v.t.)
    - **Fout-hints (Claude):** 12 − 28 → Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel. · 28 + 12 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-076` (Claude W2, bank, niveau 2 → toepassen)
    - **Opgave:** Zoek het verschil van 780 en 81. Welke som maak je?
    - **Opties:** A) 780 − 81 · B) 81 − 780 · C) 780 + 81
    - **Antwoord:** 780 − 81  (controle: n.v.t.)
    - **Fout-hints (Claude):** 81 − 780 → Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel. · 780 + 81 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Wat betekent het verschil van twee getallen? Hoeveel ligt het ene getal boven het andere?
- **Hint 2 (te schrijven):** Reken zelf uit hoeveel het ene getal meer is dan het andere. Lees dan elke som precies zoals hij er staat. Welke som geeft die uitkomst?
- **Ouderzin:** Je kind kiest de som bij 'het verschil': een minsom met het grootste getal vooraan.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `kleinste getal vooraan` (de minsom omgedraaid) → Kun je het grootste getal van het kleinste afhalen? Bij het verschil haal je het kleinste getal van het grootste af.  [nieuw]
  - `plussom` (de plussom) → Komt er bij het verschil iets bij? Het verschil zegt hoeveel het ene getal meer is dan het andere.  [nieuw]
  - `andere fout` (andere fout) → Hoeveel is het ene getal meer dan het andere? Welke som rekent dat uit?  [nieuw]
- Status: hints klaar

## Somtype 2: Hoe heet de # in # − # = #?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Hoe heet de # in # − # = #?” (koppeling: claudeId)
- Items: **30** · Claude-doelen: W2 (30) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 30 items
- Denkfouten (Claude): verkeerde-bewerking (60)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-044` (Claude W2, bank, niveau 1 → basis)
    - **Opgave:** Hoe heet de 16 in 28 − 12 = 16?
    - **Opties:** A) het aftrektal · B) de som · C) het verschil
    - **Antwoord:** het verschil  (controle: n.v.t.)
    - **Fout-hints (Claude):** het aftrektal → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · de som → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-057` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe heet de 141 in 141 − 32 = 109?
    - **Opties:** A) het aftrektal · B) de aftrekker · C) de eerste term
    - **Antwoord:** het aftrektal  (controle: n.v.t.)
    - **Fout-hints (Claude):** de aftrekker → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · de eerste term → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek het getal waar de vraag over gaat in de minsom. Staat het vooraan, achter het minteken of achter het isgelijkteken?
- **Hint 2 (te schrijven):** Bij een minsom horen de namen aftrektal, aftrekker en verschil. De namen term en som horen bij een plussom. Welke naam past bij de plek van het getal waar de vraag over gaat?
- **Ouderzin:** Je kind kent de namen van de getallen in een minsom: aftrektal, aftrekker en verschil.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `plus-naam (tweede term)` (de tweede term) → Hoort het woord term bij een minsom? Term hoort bij een plussom.  [nieuw]
  - `plus-naam (eerste term)` (de eerste term) → Hoort het woord term bij een minsom? Term hoort bij een plussom.  [nieuw]
  - `plus-naam (som)` (de som) → Hoort de naam som bij een minsom? De naam som hoort bij de uitkomst van een plussom.  [nieuw]
  - `uitkomst gekozen` (het verschil) → Is het getal waar de vraag over gaat de uitkomst van de minsom? Het verschil staat achter het isgelijkteken.  [nieuw]
  - `getal vooraan gekozen` (het aftrektal) → Staat het getal waar de vraag over gaat vooraan in de minsom? Het aftrektal is het getal waar je iets van afhaalt.  [nieuw]
  - `getal dat eraf gaat gekozen` (de aftrekker) → Gaat het getal waar de vraag over gaat eraf? De aftrekker is het getal achter het minteken.  [nieuw]
  - `andere fout` (andere fout) → Waar staat het getal waar de vraag over gaat: vooraan, achter het minteken of achter het isgelijkteken? Welke naam van een minsom hoort bij die plek?  [nieuw]
- Status: hints klaar

## Somtype 3: Hoe heet de # in # + # = #?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoe heet de # in # + # = #?” (koppeling: claudeId)
- Items: **15** · Claude-doelen: W2 (15) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 15 items
- Denkfouten (Claude): verkeerde-bewerking (30)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-008` (Claude W2, bank, niveau 1 → basis)
    - **Opgave:** Hoe heet de 12 in 12 + 3 = 15?
    - **Opties:** A) de tweede term · B) de eerste term · C) het aftrektal
    - **Antwoord:** de eerste term  (controle: n.v.t.)
    - **Fout-hints (Claude):** de tweede term → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het aftrektal → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-007` (Claude W2, bank, niveau 1 → basis)
    - **Opgave:** Hoe heet de 18 in 16 + 2 = 18?
    - **Opties:** A) de som · B) de eerste term · C) het verschil
    - **Antwoord:** de som  (controle: n.v.t.)
    - **Fout-hints (Claude):** de eerste term → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het verschil → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek het getal waar de vraag over gaat in de plussom. Staat het vooraan, achter het plusteken of achter het isgelijkteken?
- **Hint 2 (te schrijven):** Bij een plussom horen de namen term en som. Aftrektal, aftrekker en verschil horen bij een minsom. Welke naam past bij de plek van het getal waar de vraag over gaat?
- **Ouderzin:** Je kind kent de namen van de getallen in een plussom: eerste term, tweede term en som.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min-naam (verschil)` (het verschil) → Hoort het verschil bij een plussom? Het verschil is de uitkomst van een minsom.  [nieuw]
  - `min-naam (aftrekker)` (de aftrekker) → Hoort de aftrekker bij een plussom? Bij een plussom haal je niets af.  [nieuw]
  - `min-naam (aftrektal)` (het aftrektal) → Hoort het aftrektal bij een plussom? Bij een plussom haal je niets af.  [nieuw]
  - `getal vooraan gekozen` (de eerste term) → Staat het getal waar de vraag over gaat vooraan in de plussom? De eerste term is het getal vooraan.  [nieuw]
  - `getal achter het plusteken gekozen` (de tweede term) → Staat het getal waar de vraag over gaat achter het plusteken? De tweede term is het getal dat je erbij optelt.  [nieuw]
  - `uitkomst gekozen` (de som) → Is het getal waar de vraag over gaat de uitkomst van de plussom? Alleen het getal achter het isgelijkteken heet de som.  [nieuw]
  - `andere fout` (andere fout) → Waar staat het getal waar de vraag over gaat: vooraan, achter het plusteken of achter het isgelijkteken? Welke naam van een plussom hoort bij die plek?  [nieuw]
- Status: hints klaar

## Somtype 4: Hoe heet de # in # : # = #?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Hoe heet de # in # : # = #?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: W2 (9) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 9 items
- Denkfouten (Claude): verkeerde-bewerking (18)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-021` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe heet de 185 in 185 : 5 = 37?
    - **Opties:** A) de eerste factor · B) het deeltal · C) de deler
    - **Antwoord:** het deeltal  (controle: n.v.t.)
    - **Fout-hints (Claude):** de deler → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · de eerste factor → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-017` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe heet de 38 in 304 : 8 = 38?
    - **Opties:** A) het quotiënt · B) het deeltal · C) het product
    - **Antwoord:** het quotiënt  (controle: n.v.t.)
    - **Fout-hints (Claude):** het deeltal → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het product → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek het getal waar de vraag over gaat in de deelsom. Staat het vooraan, achter het deelteken of achter het isgelijkteken?
- **Hint 2 (te schrijven):** Bij een deelsom horen de namen deeltal, deler en quotiënt. Factor en product horen bij een keersom. Welke naam past bij de plek van het getal waar de vraag over gaat?
- **Ouderzin:** Je kind kent de namen van de getallen in een deelsom: deeltal, deler en quotiënt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keer-naam (tweede factor)` (de tweede factor) → Hoort het woord factor bij een deelsom? Factor hoort bij een keersom.  [nieuw]
  - `keer-naam (eerste factor)` (de eerste factor) → Hoort het woord factor bij een deelsom? Factor hoort bij een keersom.  [nieuw]
  - `keer-naam (product)` (het product) → Hoort het product bij een deelsom? Het product is de uitkomst van een keersom.  [nieuw]
  - `uitkomst gekozen` (het quotiënt) → Is het getal waar de vraag over gaat de uitkomst van de deelsom? Het quotiënt staat achter het isgelijkteken.  [nieuw]
  - `getal vooraan gekozen` (het deeltal) → Staat het getal waar de vraag over gaat vooraan in de deelsom? Het deeltal is het getal dat je verdeelt.  [nieuw]
  - `getal achter het deelteken gekozen` (de deler) → Deel je door het getal waar de vraag over gaat? De deler is het getal achter het deelteken.  [nieuw]
  - `andere fout` (andere fout) → Waar staat het getal waar de vraag over gaat: vooraan, achter het deelteken of achter het isgelijkteken? Welke naam van een deelsom hoort bij die plek?  [nieuw]
- Status: hints klaar

## Somtype 5: Zoek het quotiënt van # en #. Welke som maak je?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Zoek het quotiënt van # en #. Welke som maak je?” (koppeling: claudeId)
- Items: **7** · Claude-doelen: W2 (7) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 7 items
- Denkfouten (Claude): omgekeerd-gedeeld (7), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 2 (meest: “Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel.”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-062` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Zoek het quotiënt van 140 en 10. Welke som maak je?
    - **Opties:** A) 10 : 140 · B) 140 : 10 · C) 140 × 10
    - **Antwoord:** 140 : 10  (controle: n.v.t.)
    - **Fout-hints (Claude):** 10 : 140 → Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel. · 140 × 10 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-065` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Zoek het quotiënt van 288 en 9. Welke som maak je?
    - **Opties:** A) 288 × 9 · B) 9 : 288 · C) 288 : 9
    - **Antwoord:** 288 : 9  (controle: n.v.t.)
    - **Fout-hints (Claude):** 9 : 288 → Wat wil je weten, en waar deel je dan door? Zet het in een verhoudingstabel. · 288 × 9 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Wat betekent het quotiënt? Bij welk soort som hoort dat woord?
- **Hint 2 (te schrijven):** Het quotiënt is de uitkomst van een deelsom. Kijk bij elke som welk teken erin staat. Kijk ook welk getal vooraan staat, en vergelijk dat met de volgorde in de vraag.
- **Ouderzin:** Je kind kiest de som bij 'het quotiënt': een deelsom, met het eerste getal uit de vraag vooraan.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `keersom` (de keersom) → Doe je keer bij het quotiënt? Het quotiënt is de uitkomst van een deling.  [nieuw]
  - `deelsom omgedraaid` (de deelsom omgedraaid) → Staat het goede getal vooraan? Bij het quotiënt van twee getallen deel je het eerste getal door het tweede.  [nieuw]
  - `andere fout` (andere fout) → Welke som geeft het quotiënt? Zoek het deelteken, en kijk welk getal vooraan staat.  [nieuw]
- Status: hints klaar

## Somtype 6: Hoe heet de # in # × # = #?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Hoe heet de # in # × # = #?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: W2 (6) · regel: G7-W01-wiskundewoorden
- Getallenruimte: n.v.t. · type: meerkeuze
- Uit de G6-park: 6 items
- Denkfouten (Claude): verkeerde-bewerking (12)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G7-DENK-04-claude-bank-027` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe heet de 1035 in 115 × 9 = 1035?
    - **Opties:** A) het product · B) het quotiënt · C) de eerste factor
    - **Antwoord:** het product  (controle: n.v.t.)
    - **Fout-hints (Claude):** de eerste factor → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het quotiënt → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G7-DENK-04-claude-bank-030` (Claude W2, bank, niveau 3 → toepassen)
    - **Opgave:** Hoe heet de 4200 in 1050 × 4 = 4200?
    - **Opties:** A) het product · B) de eerste factor · C) het quotiënt
    - **Antwoord:** het product  (controle: n.v.t.)
    - **Fout-hints (Claude):** de eerste factor → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · het quotiënt → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zoek het getal waar de vraag over gaat in de keersom. Staat het vooraan, achter het keerteken of achter het isgelijkteken?
- **Hint 2 (te schrijven):** Bij een keersom horen de namen factor en product. Deeltal, deler en quotiënt horen bij een deelsom. Welke naam past bij de plek van het getal waar de vraag over gaat?
- **Ouderzin:** Je kind kent de namen van de getallen in een keersom: eerste factor, tweede factor en product.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `getal vooraan gekozen` (de eerste factor) → Staat het getal waar de vraag over gaat vooraan in de keersom? De eerste factor is het getal vooraan.  [nieuw]
  - `deel-naam (quotiënt)` (het quotiënt) → Hoort het quotiënt bij een keersom? Het quotiënt is de uitkomst van een deelsom.  [nieuw]
  - `andere fout` (andere fout) → Waar staat het getal waar de vraag over gaat: vooraan, achter het keerteken of achter het isgelijkteken? Welke naam van een keersom hoort bij die plek?  [nieuw]
- Status: hints klaar
