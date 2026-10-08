# G5-GET-M04 — Slim rekenen tot duizend

Onze omschrijving: +/− tot 1000: analogie tientallen/honderdtallen · in onze bank: 8 items

Claude-vragen gemapt: **2** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + # = — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# + # = — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C2 (1) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (1), een-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Je zit er één tiental naast. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G5-GET-M04-claude-bank-001` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 490 + 160 =
    - **Antwoord:** 650  (controle: ok)
    - **Fout-hints (Claude):** 640 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 651 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Hint 2 (te schrijven):** Komen de tientallen samen op tien of meer? Dan komt er een honderdtal bij.
- **Ouderzin:** Je kind telt twee getallen tot 1000 bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Kijk goed naar het teken. Bij + tel je op.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Komen de tientallen samen op tien of meer? Dan komt er een honderdtal bij.  [nieuw]
  - `andere fout` (andere fout) → Begin bij het eerste getal. Tel het tweede getal er in stukjes bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 2: # + □ = #

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# + □ = #” (koppeling: claudeId)
- Items: **1** · Claude-doelen: C2 (1) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: invullen
- Denkfouten (Claude): onthouden-vergeten (1), tiental-ernaast (1)
- Verschillende Claude-fout-hints: 2 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-M04-claude-bank-002` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 130 + □ = 210
    - **Antwoord:** 80  (controle: ok)
    - **Fout-hints (Claude):** 90 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 70 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Welk getal moet je bij het eerste getal optellen om de uitkomst te krijgen?
- **Hint 2 (te schrijven):** Vul aan: spring vanaf het eerste getal naar het volgende hele tiental of honderdtal, en dan verder tot de uitkomst. Tel al je sprongen bij elkaar.
- **Ouderzin:** Je kind zoekt het ontbrekende getal in een plussom tot 1000 (aanvullen).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de uitkomst` (fout = getal2) → Dat is de uitkomst van de som. Welk getal moet je bij het eerste getal optellen om daar te komen?  [nieuw]
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de twee getallen opgeteld. Zoek wat erbij moet: van het eerste getal naar de uitkomst.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `andere fout` (andere fout) → Begin bij het eerste getal en vul aan tot de uitkomst. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
- Status: hints klaar
