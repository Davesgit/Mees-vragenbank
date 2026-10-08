# G5-GET-E06 — Rekenen met euro's

Onze omschrijving: +/− eenvoudige geldbedragen (2 decimalen) · in onze bank: 8 items

Claude-vragen gemapt: **1060** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: €# + €# =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “€# + €# =” (koppeling: claudeId)
- Items: **565** · Claude-doelen: B12 (565) · regel: G5-B05-geldsom
- Getallenruimte: 0–100 euro (met komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (654), komma-verschoven (262), verkeerde-bewerking (132), verhoudingstabel-verkeerd (82)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G5-GET-E06-claude-bank-098` (Claude B12, bank, niveau 2 → toepassen)
    - **Opgave:** €1,05 + €1,55 =
    - **Antwoord:** €2,60  (controle: ok)
    - **Fout-hints (Claude):** €2,70 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · €2,50 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G5-GET-E06-claude-bank-354` (Claude B12, bank, niveau 2 → toepassen)
    - **Opgave:** €2,95 + €4,75 =
    - **Antwoord:** €7,70  (controle: ok)
    - **Fout-hints (Claude):** €7,60 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · €7,69 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.

- **Hint 1 (te schrijven):** Tel eerst de hele euro's bij elkaar op. Tel daarna de centen bij elkaar op.
- **Hint 2 (te schrijven):** Komen de centen samen op honderd cent of meer? Dan komt er een euro bij.
- **Ouderzin:** Je kind telt twee geldbedragen met euro's en centen bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `komma op de verkeerde plek` (Claudes sleutel: komma-verschoven) → De komma staat op de verkeerde plek. Hoeveel hele euro's zijn het ongeveer? Kijk of je antwoord daarbij past.  [Claude, taalfix]
  - `centen ernaast` (Claudes sleutel: tiende-of-honderdste-ernaast) → Bijna! De centen kloppen net niet. Reken de centen achter de komma nog eens na.  [Claude, taalfix]
  - `min gedaan` (Claudes sleutel: verkeerde-bewerking) → Kijk goed naar het teken: het is een plussom. Tel de bedragen bij elkaar op.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel eerst de hele euro's bij elkaar en dan de centen. Honderd cent is één euro.  [nieuw]
- Status: hints klaar

## Somtype 2: €# − €# =

- Sleutel: nrOrigineel **2** · somtypeOrigineel “€# − €# =” (koppeling: claudeId)
- Items: **483** · Claude-doelen: B12 (483) · regel: G5-B05-geldsom
- Getallenruimte: 0–100 euro (met komma) · type: kale
- Denkfouten (Claude): tiende-of-honderdste-ernaast (635), komma-verschoven (203), verkeerde-bewerking (99), verhoudingstabel-verkeerd (29)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G5-GET-E06-claude-bank-663` (Claude B12, bank, niveau 2 → toepassen)
    - **Opgave:** €9,95 − €1,55 =
    - **Antwoord:** €8,40  (controle: ok)
    - **Fout-hints (Claude):** €8,50 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · €8,30 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G5-GET-E06-claude-bank-665` (Claude B12, bank, niveau 2 → toepassen)
    - **Opgave:** €4,25 − €2,40 =
    - **Antwoord:** €1,85  (controle: ok)
    - **Fout-hints (Claude):** €6,65 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Haal eerst de hele euro's eraf. Haal daarna de centen eraf.
- **Hint 2 (te schrijven):** Heeft het eerste bedrag minder centen dan het tweede? Wissel dan een euro in voor honderd cent.
- **Ouderzin:** Je kind haalt een geldbedrag met euro's en centen van een ander bedrag af.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `bedrag dat eraf gaat` (fout = het bedrag dat eraf gaat) → Is dat het bedrag dat eraf gaat? Haal het van het eerste bedrag af.  [nieuw]
  - `komma op de verkeerde plek` (Claudes sleutel: komma-verschoven) → De komma staat op de verkeerde plek. Hoeveel hele euro's zijn het ongeveer? Kijk of je antwoord daarbij past.  [Claude, taalfix]
  - `centen ernaast` (Claudes sleutel: tiende-of-honderdste-ernaast) → Bijna! De centen kloppen net niet. Reken de centen achter de komma nog eens na.  [Claude, taalfix]
  - `opgeteld` (Claudes sleutel: verkeerde-bewerking) → Kijk goed naar het teken: het is een minsom. Haal het tweede bedrag van het eerste af.  [Claude, taalfix]
  - `andere fout` (andere fout) → Haal eerst de hele euro's eraf en dan de centen. Een euro is honderd cent.  [nieuw]
- Status: hints klaar

## Somtype 3: In de winkel kost een [ding] €# en een [ding] €#. Hoeveel betaal je samen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “In de winkel kost een [ding] €# en een [ding] €#. Hoeveel betaal je samen?” (koppeling: claudeId)
- Items: **12** · Claude-doelen: B4 (12) · regel: G5-B04-geld
- Getallenruimte: 0–100 euro (met komma) · type: kale
- Denkfouten (Claude): kommagetal-als-geheel (12), onthouden-vergeten (12), tiental-ernaast (12)
- Verschillende Claude-fout-hints: 3 (meest: “De cijfers achter de komma zijn tienden (dubbeltjes). 5 tienden + 2 tienden is 7 tienden, dus ,70.”)
- Voorbeelden:
  - `G5-GET-E06-claude-bank-001` (Claude B4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de winkel kost een gum €5 en een sticker €3,80. Hoeveel betaal je samen?
    - **Antwoord:** €8,80  (controle: ok)
    - **Fout-hints (Claude):** €8,08 → De cijfers achter de komma zijn tienden (dubbeltjes). 5 tienden + 2 tienden is 7 tienden, dus ,70. · €9,80 → Kijk of de centen samen boven de 100 komen. Zo niet, dan komt er geen euro bij. · €8,70 → Je zit één dubbeltje ernaast. Tel de tienden nog eens na.
    - **Uitleg (Claude):** Tel eerst de hele euro's: 5 + 3 = 8. Dan de centen: 0 + 80 = 80 cent. Samen €8,80.
  - `G5-GET-E06-claude-bank-002` (Claude B4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In de winkel kost een pen €1,80 en een gum €1,70. Hoeveel betaal je samen?
    - **Antwoord:** €3,50  (controle: ok)
    - **Fout-hints (Claude):** €2,15 → De cijfers achter de komma zijn tienden (dubbeltjes). 5 tienden + 2 tienden is 7 tienden, dus ,70. · €4,50 → Kijk of de centen samen boven de 100 komen. Zo niet, dan komt er geen euro bij. · €3,40 → Je zit één dubbeltje ernaast. Tel de tienden nog eens na.
    - **Uitleg (Claude):** Tel eerst de hele euro's: 1 + 1 = 2. Dan de centen: 80 + 70 = 150 cent. Samen €3,50.

- **Hint 1 (te schrijven):** Tel de twee prijzen bij elkaar op. Begin met de hele euro's.
- **Hint 2 (te schrijven):** Tel de hele euro's bij elkaar, en tel de centen bij elkaar. Komen de centen samen op honderd cent of meer? Dan komt er een euro bij.
- **Ouderzin:** Je kind rekent uit hoeveel twee dingen in de winkel samen kosten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `euro te veel` (Claudes sleutel: onthouden-vergeten) → Dat is een euro te veel. Komen de centen samen op honderd cent of meer? Alleen dan komt er een euro bij.  [Claude, taalfix]
  - `tien cent te weinig` (Claudes sleutel: tiental-ernaast) → Dat is tien cent te weinig. Tel de centen nog eens bij elkaar.  [Claude, taalfix]
  - `centen niet goed` (Claudes sleutel: kommagetal-als-geheel) → De centen kloppen niet. Tel de centen apart bij elkaar. Komen ze samen op honderd cent of meer? Dan komt er een euro bij.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel eerst de hele euro's bij elkaar en dan de centen. Honderd cent is één euro.  [nieuw]
- Status: hints klaar
