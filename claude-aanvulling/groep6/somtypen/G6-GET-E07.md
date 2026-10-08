# G6-GET-E07 — Keer met euro's, ook schatten

Onze omschrijving: × (schattend) met geld-decimalen · in onze bank: 8 items

Claude-vragen gemapt: **12** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een [ding] kost €#. Je koopt er #. Hoeveel betaal je?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een [ding] kost €#. Je koopt er #. Hoeveel betaal je?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: B4 (8) · regel: D5-geld-keer
- Getallenruimte: kommagetallen (2 cijfers achter de komma) met € · type: kale
- Uit de G5-park: 8 items
- Denkfouten (Claude): optellen-ipv-vermenigvuldigen (8), deel-vergeten-bij-splitsen (8), onthouden-vergeten (8)
- Verschillende Claude-fout-hints: 5 (meest: “De centen moet je ook keer het aantal doen, niet één keer meetellen.”)
- Voorbeelden:
  - `G6-GET-E07-claude-bank-010` (Claude B4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een pen kost €3,26. Je koopt er 4. Hoeveel betaal je?
    - **Antwoord:** €13,04  (controle: ok)
    - **Fout-hints (Claude):** €7,26 → Je koopt 4 keer hetzelfde. Dat is 4 keer de prijs, niet de prijs plus 4. · €12,26 → De centen moet je ook keer het aantal doen, niet één keer meetellen. · €14,04 → Komen de centen samen boven de 100? Alleen dan gaat er een euro bij.
    - **Uitleg (Claude):** Reken de euro's en de centen apart. 4 × €3 = €12. 4 × 26 cent = 104 cent. Samen €13,04.
  - `G6-GET-E07-claude-bank-005` (Claude B4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een stickervel kost €2,94. Je koopt er 4. Hoeveel betaal je?
    - **Antwoord:** €11,76  (controle: ok)
    - **Fout-hints (Claude):** €6,94 → Je koopt 4 keer hetzelfde. Dat is 4 keer de prijs, niet de prijs plus 4. · €8,94 → De centen moet je ook keer het aantal doen, niet één keer meetellen. · €12,76 → Komen de centen samen boven de 100? Alleen dan gaat er een euro bij.
    - **Uitleg (Claude):** Reken de euro's en de centen apart. 4 × €2 = €8. 4 × 94 cent = 376 cent. Samen €11,76.

- **Hint 1 (te schrijven):** Reken eerst het aantal keer de hele euro's. Reken daarna het aantal keer de centen.
- **Hint 2 (te schrijven):** Zijn de centen samen honderd of meer? Elke honderd cent is één euro. Tel daarna alles bij elkaar op.
- **Ouderzin:** Je kind rekent met geld: een paar keer dezelfde prijs, met euro's en centen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de prijs` (fout = de prijs) → Dat is de prijs van één. Je koopt er meer: reken het aantal keer de prijs.  [nieuw]
  - `aantal erbij geteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt het aantal erbij geteld. Je koopt er een paar van dezelfde prijs: dat is een keersom.  [Claude, taalfix]
  - `centen één keer` (Claudes sleutel: deel-vergeten-bij-splitsen) → De centen kloppen niet. Je hebt het aantal keer de euro's gedaan, maar de centen maar één keer geteld. Reken ook het aantal keer de centen.  [Claude, taalfix]
  - `euro te veel` (fout = antwoord + €1) → Dat is één euro te veel. Reken de centen nog eens na: elke honderd cent is één euro. Hoeveel euro komt er dan bij?  [nieuw]
  - `andere fout` (andere fout) → Reken het aantal keer de euro's en het aantal keer de centen. Elke honderd cent is één euro. Tel daarna alles op.  [nieuw]
- Status: hints klaar

## Somtype 2: # [ding] van elk €#. Hoeveel is dat samen? Reken handig.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# [ding] van elk €#. Hoeveel is dat samen? Reken handig.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: T10 (4) · regel: G6-T03-handig-keerdeel
- Getallenruimte: 0–1.000, 0–10.000 · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (4), tafelbuur (4), optellen-ipv-vermenigvuldigen (4)
- Verschillende Claude-fout-hints: 9 (meest: “Je hebt met het ronde getal gerekend. Haal er nu 6 × 1 af.”)
- Voorbeelden:
  - `G6-GET-E07-claude-bank-003` (Claude T10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 6 steps van elk €199. Hoeveel is dat samen? Reken handig.
    - **Antwoord:** €1194  (controle: ok)
    - **Fout-hints (Claude):** €1200 → Je hebt met het ronde getal gerekend. Haal er nu 6 × 1 af. · €1188 → Hoeveel heb je te veel gerekend? 6 keer het verschil. · €205 → 6 keer dezelfde prijs: een keersom.
    - **Uitleg (Claude):** 199 is bijna 200. 6 × 200 = 1200, dat is 6 te veel. 1200 − 6 = 1194.
  - `G6-GET-E07-claude-bank-001` (Claude T10, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** 4 tenten van elk €199. Hoeveel is dat samen? Reken handig.
    - **Antwoord:** €796  (controle: ok)
    - **Fout-hints (Claude):** €800 → Je hebt met het ronde getal gerekend. Haal er nu 4 × 1 af. · €792 → Hoeveel heb je te veel gerekend? 4 keer het verschil. · €203 → 4 keer dezelfde prijs: een keersom.
    - **Uitleg (Claude):** 199 is bijna 200. 4 × 200 = 800, dat is 4 te veel. 800 − 4 = 796.

- **Hint 1 (te schrijven):** De prijs is bijna een rond bedrag. Reken eerst het aantal keer dat ronde bedrag.
- **Hint 2 (te schrijven):** Met het ronde bedrag reken je voor elk een klein bedrag te veel. Haal dat bedrag er weer af: één keer voor elk.
- **Ouderzin:** Je kind rekent handig met geld: een paar keer een prijs die bijna rond is.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de prijs` (fout = de prijs) → Dat is de prijs van één. Je koopt er meer: reken het aantal keer de prijs.  [nieuw]
  - `aantal erbij geteld` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt het aantal erbij geteld. Je koopt er een paar van dezelfde prijs: dat is een keersom.  [Claude, taalfix]
  - `stukje niet afgehaald` (Claudes sleutel: deel-vergeten-bij-splitsen) → Dat is het aantal keer het ronde bedrag. Maar de prijs is een klein bedrag minder: haal dat bedrag er nog af, één keer voor elk.  [Claude, taalfix]
  - `te veel afgehaald` (Claudes sleutel: tafelbuur) → Dat is te weinig: je hebt te veel afgehaald. Hoeveel is de prijs minder dan het ronde bedrag? Haal precies dat bedrag af, één keer voor elk.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst het aantal keer het ronde bedrag. Haal daarna het kleine bedrag dat je te veel rekende er weer af: één keer voor elk.  [nieuw]
- Status: hints klaar
