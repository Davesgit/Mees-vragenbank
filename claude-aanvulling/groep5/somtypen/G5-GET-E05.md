# G5-GET-E05 — Plus en min tot duizend

Onze omschrijving: +/− ≤1000: rijg/splits/kolom/cijferen + strategieën + schattend · in onze bank: 8 items

Claude-vragen gemapt: **507** in **32** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + □ = #

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# + □ = #” (koppeling: claudeId)
- Items: **77** · Claude-doelen: C2 (77) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: invullen
- Denkfouten (Claude): een-ernaast (58), tiental-ernaast (41), getal-overgenomen (26), onthouden-vergeten (24), verkeerde-bewerking (5)
- Verschillende Claude-fout-hints: 5 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-104` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 130 + □ = 501
    - **Antwoord:** 371  (controle: ok)
    - **Fout-hints (Claude):** 361 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 370 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-E05-claude-bank-123` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 335 + □ = 609
    - **Antwoord:** 274  (controle: ok)
    - **Fout-hints (Claude):** 264 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 273 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

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
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
  - `andere fout` (andere fout) → Begin bij het eerste getal en vul aan tot de uitkomst. Reken na: het eerste getal plus jouw getal moet precies de uitkomst zijn.  [nieuw]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel liggen er nu?” (koppeling: claudeId)
- Items: **51** · Claude-doelen: C1 (51) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (46), een-ernaast (42), verkeerde-bewerking (7), tiental-ernaast (7)
- Verschillende Claude-fout-hints: 4 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-328` (Claude C1, bank, niveau 3 → toepassen)
    - **Opgave:** In de bak liggen 120 kaarten. Er komen er 91 bij. Hoeveel kaarten liggen er nu?
    - **Antwoord:** 211  (controle: ok)
    - **Fout-hints (Claude):** 111 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 221 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.
  - `G5-GET-E05-claude-bank-359` (Claude C1, bank, niveau 3 → toepassen)
    - **Opgave:** In de bak liggen 342 kralen. Er komen er 91 bij. Hoeveel kralen liggen er nu?
    - **Antwoord:** 433  (controle: ok)
    - **Fout-hints (Claude):** 443 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 434 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Tel de twee getallen bij elkaar op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt in een verhaal iets bij een getal tot 1000 op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het worden er meer.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Zijn de eenheden samen tien of meer? Dan komt er een tiental bij.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. De tientallen komen samen op tien of meer: dan komt er een honderdtal bij.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 3: # − # = — met overschrijding van het tiental

- Sleutel: nrOrigineel **3** · somtypeOrigineel “# − # = — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **44** · Claude-doelen: C3 (44) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (42), een-ernaast (24), kleinste-van-grootste (16), verkeerde-bewerking (6)
- Verschillende Claude-fout-hints: 3 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-142` (Claude C3, bank, niveau 3 → toepassen)
    - **Opgave:** 231 − 68 =
    - **Antwoord:** 163  (controle: ok)
    - **Fout-hints (Claude):** 173 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.
  - `G5-GET-E05-claude-bank-165` (Claude C3, bank, niveau 3 → toepassen)
    - **Opgave:** 672 − 399 =
    - **Antwoord:** 273  (controle: ok)
    - **Fout-hints (Claude):** 283 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 274 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Hint 2 (te schrijven):** Bij de eenheden en bij de tientallen ga je over een heel tiental of honderdtal heen. Ga eerst terug naar het hele tiental of honderdtal, en haal dan de rest eraf.
- **Ouderzin:** Je kind haalt een getal af van een getal tot 1000, met overschrijding van het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Kijk goed naar het teken. Bij − haal je eraf.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Bij de eenheden ga je over een heel tiental heen: dan gaat er nog een tiental af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Bij de tientallen ga je over een heel honderdtal heen: dan gaat er nog een honderdtal af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Reken na: jouw antwoord plus het tweede getal moet het eerste getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 4: # + # = — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **4** · somtypeOrigineel “# + # = — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **30** · Claude-doelen: C2 (30) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (24), een-ernaast (19), tiental-ernaast (11), verkeerde-bewerking (6)
- Verschillende Claude-fout-hints: 4 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-045` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 120 + 91 =
    - **Antwoord:** 211  (controle: ok)
    - **Fout-hints (Claude):** 201 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na. · 210 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-E05-claude-bank-030` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 342 + 183 =
    - **Antwoord:** 525  (controle: ok)
    - **Fout-hints (Claude):** 425 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 515 → Je zit er één tiental naast. Tel de tientallen nog eens rustig na.

- **Hint 1 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Hint 2 (te schrijven):** De tientallen komen samen op tien of meer. Dan komt er een honderdtal bij.
- **Ouderzin:** Je kind telt twee getallen tot 1000 op. De eenheden gaan niet over het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Kijk goed naar het teken. Bij + tel je op.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. De tientallen komen samen op tien of meer: dan komt er een honderdtal bij.  [nieuw]
  - `andere fout` (andere fout) → Begin bij het eerste getal. Tel het tweede getal er in stukjes bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 5: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **30** · Claude-doelen: C6 (30) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (60), een-ernaast (30)
- Verschillende Claude-fout-hints: 56 (meest: “Je gaat onder 300, dus het honderdtal wordt één minder.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-263` (Claude C6, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het nest liggen 604 botten. Er gaan er 6 weg. Hoeveel blijven er over?
    - **Antwoord:** 598  (controle: ok)
    - **Fout-hints (Claude):** 608 → Na 600 kom je in de 500-en. 600 − 2 eindigt op 98. · 698 → Je gaat onder 600, dus het honderdtal wordt één minder. · 597 → Ga eerst precies naar 600 (dat is 4 eraf), en dan de rest.
    - **Uitleg (Claude):** Ga eerst naar het ronde getal: 604 − 4 = 600. Dan de rest eraf: 600 − 2 = 598.
  - `G5-GET-E05-claude-bank-278` (Claude C6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het nest liggen 204 eieren. Er gaan er 19 weg. Hoeveel blijven er over?
    - **Antwoord:** 185  (controle: ok)
    - **Fout-hints (Claude):** 195 → Na 200 kom je in de 100-en. 200 − 15 eindigt op 85. · 285 → Je gaat onder 200, dus het honderdtal wordt één minder. · 184 → Ga eerst precies naar 200 (dat is 4 eraf), en dan de rest.
    - **Uitleg (Claude):** Ga eerst naar het ronde getal: 204 − 4 = 200. Dan de rest eraf: 200 − 15 = 185.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Je gaat onder het hele honderdtal. Ga eerst terug naar het hele honderdtal, en haal daarna de rest eraf.
- **Ouderzin:** Je kind haalt een getal af van een getal tot 1000, over een heel honderdtal heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het getal dat weggaat. De vraag is hoeveel er nog over zijn.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `onder het honderdtal (tiental)` (fout = antwoord + 10) → Dat is te veel. Je gaat onder het hele honderdtal. Ga eerst terug naar het hele honderdtal, en haal dan de rest eraf.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `onder het honderdtal` (fout = antwoord + 100) → Dat is één honderdtal te veel. Je gaat onder het hele honderdtal, dus het honderdtal wordt één minder.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 6: In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel liggen er nu?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # weg. Hoeveel liggen er nu?” (koppeling: claudeId)
- Items: **30** · Claude-doelen: C1 (30) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (27), een-ernaast (19), verkeerde-bewerking (8), kleinste-van-grootste (6)
- Verschillende Claude-fout-hints: 3 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-305` (Claude C1, bank, niveau 3 → toepassen)
    - **Opgave:** In de bak liggen 231 stiften. Er gaan er 45 weg. Hoeveel stiften liggen er nu?
    - **Antwoord:** 186  (controle: ok)
    - **Fout-hints (Claude):** 185 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-E05-claude-bank-314` (Claude C1, bank, niveau 3 → toepassen)
    - **Opgave:** In de bak liggen 379 kaarten. Er gaan er 91 weg. Hoeveel kaarten liggen er nu?
    - **Antwoord:** 288  (controle: ok)
    - **Fout-hints (Claude):** 278 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 470 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er liggen er nu minder. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Ouderzin:** Je kind haalt in een verhaal iets af van een getal tot 1000.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het getal dat weggaat. De vraag is hoeveel er nog over zijn.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Ga je bij de eenheden over een heel tiental heen? Dan gaat er nog een tiental af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Bij de tientallen ga je over een heel honderdtal heen: dan gaat er nog een honderdtal af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 7: In [plek] lagen # [ding]. Er zijn er # [ding]. Hoeveel [ding] liggen er nog?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “In [plek] lagen # [ding]. Er zijn er # [ding]. Hoeveel [ding] liggen er nog?” (koppeling: claudeId)
- Items: **29** · Claude-doelen: C5 (29) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (58), verkeerde-bewerking (29), kleinste-van-grootste (15)
- Verschillende Claude-fout-hints: 4 (meest: “Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-196` (Claude C5, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het moeras lagen 344 schelpen. Er zijn er 226 weggehaald. Hoeveel schelpen liggen er nog?
    - **Antwoord:** 118  (controle: ok)
    - **Fout-hints (Claude):** 218 → Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens. · 128 → Bij het lenen van een tiental wordt het tiental één minder. Tel de tientallen nog eens. · 570 → Er zijn er weggehaald: dit is een minsom.
    - **Uitleg (Claude):** Haal eerst de honderdtallen eraf: 344 − 200 = 144. Dan de tientallen: − 20 = 124. Dan de eenheden: − 6 = 118.
  - `G5-GET-E05-claude-bank-214` (Claude C5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het moeras lagen 423 botten. Er zijn er 195 weggehaald. Hoeveel botten liggen er nog?
    - **Antwoord:** 228  (controle: ok)
    - **Fout-hints (Claude):** 328 → Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens. · 238 → Bij het lenen van een tiental wordt het tiental één minder. Tel de tientallen nog eens. · 618 → Er zijn er weggehaald: dit is een minsom. · 372 → Je mag niet zomaar de kleinste van de grootste afhalen per kolom. Leen van de kolom ernaast.
    - **Uitleg (Claude):** Haal eerst de honderdtallen eraf: 423 − 100 = 323. Dan de tientallen: − 90 = 233. Dan de eenheden: − 5 = 228.

- **Hint 1 (te schrijven):** Er zijn dingen weggehaald, dus er liggen er minder. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Ouderzin:** Je kind rekent uit hoeveel er nog liggen als er iets is weggehaald (tot 1000).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er zijn er weggehaald: dit is een minsom.  [Claude, ok]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er zijn dingen weggehaald, dus er liggen er minder.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het aantal dat is weggehaald. De vraag is hoeveel er nog liggen.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Ga je bij de eenheden over een heel tiental heen? Dan gaat er nog een tiental af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Ga je bij de tientallen over een heel honderdtal heen? Dan gaat er nog een honderdtal af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `kleinste van de grootste` (fout = antwoord + 2 of meer) → Dat is te veel. Is bij een plek het cijfer van het tweede getal groter? Ga dan eerst terug tot het hele tiental of honderdtal. Reken na: jouw antwoord plus wat er weggaat, moet het eerste getal zijn.  [Claude, taalfix]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 8: In [plek] liggen # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “In [plek] liggen # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **28** · Claude-doelen: C4 (28) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (56), tiental-ernaast (28), verkeerde-bewerking (28)
- Verschillende Claude-fout-hints: 4 (meest: “Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-224` (Claude C4, gegenereerd, niveau 1 → basis)
    - **Opgave:** In het museum liggen 490 schelpen en in het moeras 451. Hoeveel schelpen zijn dat samen?
    - **Antwoord:** 941  (controle: ok)
    - **Fout-hints (Claude):** 841 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 931 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 951 → Controleer de tientallen: je hebt er een te veel. · 39 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 400 + 400 = 800, 90 + 50 = 140, 0 + 1 = 1. Samen: 800 + 140 + 1 = 941.
  - `G5-GET-E05-claude-bank-229` (Claude C4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het nest liggen 601 blaadjes en in de vallei 119. Hoeveel blaadjes zijn dat samen?
    - **Antwoord:** 720  (controle: ok)
    - **Fout-hints (Claude):** 620 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 710 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 730 → Controleer de tientallen: je hebt er een te veel. · 482 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 600 + 100 = 700, 0 + 10 = 10, 1 + 9 = 10. Samen: 700 + 10 + 10 = 720.

- **Hint 1 (te schrijven):** Samen betekent: bij elkaar optellen. Tel de twee getallen op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt twee aantallen tot 1000 bij elkaar op.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Samen betekent optellen.  [Claude, ok]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Controleer de tientallen: je hebt er één te veel.  [Claude, taalfix]
  - `tiental te weinig` (fout = antwoord − 10) → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij.  [Claude, ok]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.  [Claude, ok]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen, de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 9: # + # = — met overschrijding van het tiental

- Sleutel: nrOrigineel **9** · somtypeOrigineel “# + # = — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **19** · Claude-doelen: C2 (19) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): een-ernaast (18), onthouden-vergeten (14), verkeerde-bewerking (4), tiental-ernaast (2)
- Verschillende Claude-fout-hints: 4 (meest: “Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-010` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 157 + 45 =
    - **Antwoord:** 202  (controle: ok)
    - **Fout-hints (Claude):** 201 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers. · 112 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E05-claude-bank-014` (Claude C2, bank, niveau 3 → toepassen)
    - **Opgave:** 268 + 252 =
    - **Antwoord:** 520  (controle: ok)
    - **Fout-hints (Claude):** 530 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 521 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.

- **Hint 1 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Hint 2 (te schrijven):** De eenheden komen samen op tien of meer: dan komt er een tiental bij. Bij de tientallen gebeurt dat ook: dan komt er een honderdtal bij.
- **Ouderzin:** Je kind telt twee getallen tot 1000 op, met overschrijding van het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Kijk goed naar het teken. Bij + tel je op.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. De eenheden zijn samen tien of meer: dan komt er een tiental bij.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. De tientallen komen samen op tien of meer: dan komt er een honderdtal bij.  [nieuw]
  - `andere fout` (andere fout) → Begin bij het eerste getal. Tel het tweede getal er in stukjes bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 10: # − # = — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **10** · somtypeOrigineel “# − # = — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **18** · Claude-doelen: C3 (18) · regel: G5-K01-kaal-plusmin
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (16), een-ernaast (9), verkeerde-bewerking (6), kleinste-van-grootste (5)
- Verschillende Claude-fout-hints: 3 (meest: “Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-176` (Claude C3, bank, niveau 3 → toepassen)
    - **Opgave:** 231 − 91 =
    - **Antwoord:** 140  (controle: ok)
    - **Fout-hints (Claude):** 130 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 139 → Je zit er eentje naast. Tel nog eens rustig, en zet elk stapje op papier of op je vingers.
  - `G5-GET-E05-claude-bank-177` (Claude C3, bank, niveau 3 → toepassen)
    - **Opgave:** 379 − 91 =
    - **Antwoord:** 288  (controle: ok)
    - **Fout-hints (Claude):** 298 → Controleer de eenheden: als die boven de 10 komen, hoort er een 1 bij de tientallen. · 470 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Hint 2 (te schrijven):** Bij de tientallen ga je over een heel honderdtal heen. Ga eerst terug naar het hele honderdtal, en haal dan de rest eraf.
- **Ouderzin:** Je kind haalt een getal af van een getal tot 1000. De eenheden gaan niet over het tiental.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Kijk goed naar het teken. Bij − haal je eraf.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Haal de tientallen nog eens af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Bij de tientallen ga je over een heel honderdtal heen: dan gaat er nog een honderdtal af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Reken na: jouw antwoord plus het tweede getal moet het eerste getal zijn.  [nieuw]
- Status: hints klaar

## Somtype 11: In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **11** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **14** · Claude-doelen: T9 (14) · regel: FX-G4-7, G07-welke-som
- Getallenruimte: 0–1.000, 0–100 · type: meerkeuze
- Denkfouten (Claude): kleinste-van-grootste (14), verkeerde-bewerking (14)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-258` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de zak liggen 97 ballen. Er gaan er 5 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 97 − 5 · B) 5 − 97 · C) 97 + 5
    - **Antwoord:** 97 − 5  (controle: ok)
    - **Fout-hints (Claude):** 97 + 5 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E05-claude-bank-255` (Claude T9, bank, niveau 2 → toepassen)
    - **Opgave:** In de mand liggen 106 ballen. Er gaan er 8 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 106 − 8 · B) 106 + 8 · C) 8 − 106
    - **Antwoord:** 106 − 8  (controle: ok)
    - **Fout-hints (Claude):** 106 + 8 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal: komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Gaan er dingen uit? Dan is het een minsom. Je begint met het getal dat er eerst in ligt.
- **Ouderzin:** Je kind kiest de som die bij een verhaaltje hoort.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `omgedraaid` (de minsom omgedraaid) → Je begint met wat er eerst in ligt. Daar haal je af wat eruit gaat.  [nieuw]
  - `plussom` (de plussom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `andere fout` (andere fout) → Zoek in het verhaal de twee getallen. Er gaan dingen uit: haal het tweede getal af van wat er eerst in ligt.  [nieuw]
- Status: hints klaar

## Somtype 12: In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **12** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **14** · Claude-doelen: T9 (14) · regel: FX-G4-7, G07-welke-som
- Getallenruimte: 0–1.000, 0–100 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (14), verkeerd-getal (14)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-386` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de zak liggen 97 ballen. Er komen er 5 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 97 + 5 · B) 97 − 5 · C) 97 + 6
    - **Antwoord:** 97 + 5  (controle: ok)
    - **Fout-hints (Claude):** 97 − 5 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E05-claude-bank-389` (Claude T9, bank, niveau 2 → toepassen)
    - **Opgave:** In de mand liggen 106 ballen. Er komen er 8 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 106 − 8 · B) 106 + 8 · C) 106 + 9
    - **Antwoord:** 106 + 8  (controle: ok)
    - **Fout-hints (Claude):** 106 − 8 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal: komen er dingen bij, of gaan er dingen af?
- **Hint 2 (te schrijven):** Komen er dingen bij? Dan is het een plussom. Kijk ook of de getallen in de som dezelfde zijn als in het verhaal.
- **Ouderzin:** Je kind kiest de som die bij een verhaaltje hoort.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `minsom` (de minsom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `ander getal` (andere fout) → Kijk goed welke getallen in het verhaal staan. Gebruik precies die getallen in de som.  [nieuw]
- Status: hints klaar

## Somtype 13: Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit. — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **20** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit. — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **11** · Claude-doelen: T3 (11) · regel: D8-SCHAT-NAAR-G5
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 11 (meest: “Rond af op tientallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-015` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 62 + 85 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 150  (controle: n.v.t.)
    - **Fout-hints (Claude):** 100 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 90 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
    - **Uitleg (Claude):** 62 wordt 60 en 85 wordt 90. 60 + 90 = 150.
  - `G5-GET-E05-claude-bank-naar-023` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 52 + 86 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 140  (controle: n.v.t.)
    - **Fout-hints (Claude):** 200 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 160 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op tientallen. Kijk bij elk getal naar de eenheden: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Tel ze bij elkaar op.
- **Ouderzin:** Je kind schat een plussom: eerst beide getallen afronden op tientallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de eenheden.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de eenheden.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op tientallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op tientallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 14: Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **9** · Claude-doelen: T3 (9) · regel: D8-KLOPPEN-NAAR-G5
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): laatste-cijfer (7), orde-van-grootte (6), bovengrens (3), ondergrens (2)
- Verschillende Claude-fout-hints: 18 (meest: “Rond eerst af. 50 + 60 is 110. Ligt 13 daar dichtbij?”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-054` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 53 + 60 kan kloppen?
    - **Opties:** A) 113 · B) 13 · C) 111
    - **Antwoord:** 113  (controle: n.v.t.)
    - **Fout-hints (Claude):** 13 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G5-GET-E05-claude-bank-naar-060` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 71 + 35 kan kloppen?
    - **Opties:** A) 106 · B) 6 · C) 104
    - **Antwoord:** 106  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond beide getallen af en tel ze op. Zo weet je ongeveer hoe groot de uitkomst is.
- **Hint 2 (te schrijven):** Kijk daarna naar de laatste cijfers. Op welk cijfer moet de uitkomst eindigen? Kies het antwoord dat in de buurt ligt en op dat cijfer eindigt.
- **Ouderzin:** Je kind kiest zonder uit te rekenen welk antwoord bij een plussom kan kloppen: afronden en naar het laatste cijfer kijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te ver weg` (Claudes sleutel: orde-van-grootte) → Rond eerst af en reken dat uit. Ligt dit antwoord daar in de buurt?  [Claude, taalfix]
  - `ander laatste cijfer` (Claudes sleutel: laatste-cijfer) → Tel de laatste cijfers van de twee getallen bij elkaar op. Op welk cijfer eindigt dat? Eindigt dit antwoord daarop?  [Claude, taalfix]
  - `te groot` (Claudes sleutel: bovengrens) → Rond allebei naar boven af en tel ze op. Groter dan dat kan de uitkomst niet zijn. Is dit antwoord groter?  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Rond allebei naar beneden af en tel ze op. Kleiner dan dat kan de uitkomst niet zijn. Is dit antwoord kleiner?  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af en tel ze op. Zo weet je ongeveer hoe groot de uitkomst is. Kijk daarna naar de laatste cijfers.  [nieuw]
- Status: hints klaar

## Somtype 15: Hoeveel is # − # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — met overschrijding van het tiental

- Sleutel: nrOrigineel **31** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **8** · Claude-doelen: merge-generator G5 ronde 9 (#235) (6), T3 (2) · regel: D8-SCHAT-NAAR-G5, G5-r9 #235 generator
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 10 (meest: “Rond af op honderdtallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-036` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 850 − 194 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 700  (controle: n.v.t.)
    - **Fout-hints (Claude):** 706 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E05-merge-gen-008` (Claude merge-generator G5 ronde 9 (#235), None, niveau 1 → basis)
    - **Opgave:** Hoeveel is 913 − 386 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 500  (controle: ok)
    - **Fout-hints (Claude):** 706 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
    - **Uitleg (Claude):** 913 wordt 900 en 386 wordt 400. 900 − 400 = 500.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op honderdtallen. Kijk bij elk getal naar de tientallen: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Haal het tweede ronde getal van het eerste af.
- **Ouderzin:** Je kind schat een minsom: eerst beide getallen afronden op honderdtallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op honderdtallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op honderdtallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 16: Hoeveel is # − # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **22** · somtypeOrigineel “Hoeveel is # − # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T3 (8) · regel: D8-SCHAT-NAAR-G5
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-032` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 567 − 152 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 400  (controle: n.v.t.)
    - **Fout-hints (Claude):** 500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 200 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E05-claude-bank-naar-037` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 407 − 131 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 300  (controle: n.v.t.)
    - **Fout-hints (Claude):** 400 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven. · 500 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op honderdtallen. Kijk bij elk getal naar de tientallen: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Haal het tweede ronde getal van het eerste af.
- **Ouderzin:** Je kind schat een minsom: eerst beide getallen afronden op honderdtallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 - getal2 of getal2 - getal1) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op honderdtallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op honderdtallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 17: Zoveel bezoekers kwamen er bij [plek]: maandag #, dinsdag #, woensdag # en donderdag #. Hoeveel bezoekers waren er in die vier dagen samen?

- Sleutel: nrOrigineel **32** · somtypeOrigineel “In een tabel staat het aantal bezoekers van [plek]: maandag #, dinsdag #, woensdag # en donderdag #. Hoeveel bezoekers waren er in die vier dagen samen?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: merge-generator G5 ronde 9 (#235) (7), G9 (1) · regel: D8-STAT-NAAR-G5, G5-r9 #235 generator
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): tiental-ernaast (8), getal-overgenomen (8)
- Verschillende Claude-fout-hints: 4 (meest: “Dat is tien te weinig. Let goed op de tientallen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-053` (Claude G9, ai, niveau 2 → toepassen)
    - **Opgave:** Zoveel bezoekers kwamen er bij de kinderboerderij: maandag 45, dinsdag 38, woensdag 92 en donderdag 55. Hoeveel bezoekers waren er in die vier dagen samen?
    - **Opties:** A) 220 bezoekers · B) 92 bezoekers · C) 230 bezoekers
    - **Antwoord:** 230 bezoekers  (controle: n.v.t.)
    - **Fout-hints (Claude):** 220 bezoekers → Tel de getallen nog een keer rustig op. Let goed op de tientallen. · 92 bezoekers → 92 hoort bij één dag. De vraag gaat over alle vier de dagen samen.
    - **Uitleg (Claude):** Je telt alle dagen op: 45 + 38 = 83 en 92 + 55 = 147. Samen is dat 83 + 147 = 230 bezoekers.
  - `G5-GET-E05-merge-gen-015` (Claude merge-generator G5 ronde 9 (#235), None, niveau 2 → toepassen)
    - **Opgave:** Zoveel bezoekers kwamen er bij het museum: maandag 48, dinsdag 63, woensdag 57 en donderdag 39. Hoeveel bezoekers waren er in die vier dagen samen?
    - **Opties:** A) 207 bezoekers · B) 197 bezoekers · C) 63 bezoekers
    - **Antwoord:** 207 bezoekers  (controle: ok)
    - **Fout-hints (Claude):** 220 bezoekers → Tel de getallen nog een keer rustig op. Let goed op de tientallen. · 92 bezoekers → 92 hoort bij één dag. De vraag gaat over alle vier de dagen samen.
    - **Uitleg (Claude):** 48 + 63 + 57 + 39 = 207.

- **Hint 1 (te schrijven):** Tel de getallen van alle dagen bij elkaar op.
- **Hint 2 (te schrijven):** Tel eerst twee dagen bij elkaar. Tel daar steeds de volgende dag bij, tot je alle dagen hebt gehad.
- **Ouderzin:** Je kind telt de bezoekers van vier dagen bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `tiental te veel` (fout = antwoord + 10) → Dat is tien te veel. Tel de getallen nog eens op. Let goed op de tientallen: tel je het tiental dat je onthoudt maar één keer mee?  [nieuw]
  - `tiental te weinig` (Claudes sleutel: tiental-ernaast) → Dat is tien te weinig. Tel de getallen nog eens op. Let goed op de tientallen.  [Claude, taalfix]
  - `één dag` (Claudes sleutel: getal-overgenomen) → Dat is het getal van één dag. De vraag gaat over alle dagen samen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de getallen van alle dagen bij elkaar op.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'In een tabel staat het aantal bezoekers van [plek]: maandag #, dinsdag #, woensdag # en donderdag #. Hoeveel bezoekers waren er in die vier dagen samen?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 18: Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen? — met overschrijding van het tiental

- Sleutel: nrOrigineel **30** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen? — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **8** · Claude-doelen: merge-generator G5 ronde 9 (#235) (5), T3 (3) · regel: D8-KLOPPEN-NAAR-G5, G5-r9 #235 generator
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): laatste-cijfer (6), ondergrens (5), bovengrens (4), orde-van-grootte (1)
- Verschillende Claude-fout-hints: 16 (meest: “Rond 700 naar boven af en 273 naar beneden. 700 − 200 is 500. De uitkomst kan dus niet groter zijn dan 500, en 527 is groter.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-070` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 700 − 273 kan kloppen?
    - **Opties:** A) 427 · B) 527 · C) 973
    - **Antwoord:** 427  (controle: n.v.t.)
    - **Fout-hints (Claude):** 527 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 973 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G5-GET-E05-merge-gen-002` (Claude merge-generator G5 ronde 9 (#235), None, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 813 − 456 kan kloppen?
    - **Opties:** A) 355 · B) 357 · C) 257
    - **Antwoord:** 357  (controle: ok)
    - **Fout-hints (Claude):** 527 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 973 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Rond beide getallen af en haal het tweede van het eerste af. Zo weet je ongeveer hoe groot de uitkomst is.
- **Hint 2 (te schrijven):** Kijk daarna naar de laatste cijfers. Op welk cijfer moet de uitkomst eindigen? Kies het antwoord dat in de buurt ligt en op dat cijfer eindigt.
- **Ouderzin:** Je kind kiest zonder uit te rekenen welk antwoord bij een minsom kan kloppen: afronden en naar het laatste cijfer kijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te ver weg` (Claudes sleutel: orde-van-grootte) → Rond eerst af en reken dat uit. Ligt dit antwoord daar in de buurt?  [Claude, taalfix]
  - `ander laatste cijfer` (Claudes sleutel: laatste-cijfer) → Haal het laatste cijfer van het tweede getal af van het laatste cijfer van het eerste. Kan dat niet? Doe er dan eerst tien bij. Eindigt dit antwoord op dat cijfer?  [Claude, taalfix]
  - `te groot` (Claudes sleutel: bovengrens) → Rond het eerste getal naar boven af en het tweede naar beneden. Haal ze van elkaar af. Groter dan dat kan de uitkomst niet zijn. Is dit antwoord groter?  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Rond het eerste getal naar beneden af en het tweede naar boven. Haal ze van elkaar af. Kleiner dan dat kan de uitkomst niet zijn. Is dit antwoord kleiner?  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af en haal het tweede van het eerste af. Zo weet je ongeveer hoe groot de uitkomst is. Kijk daarna naar de laatste cijfers.  [nieuw]
- Status: hints klaar

## Somtype 19: Verhaalsom min: # [ding], er gaan er # weg. Hoeveel nog?

- Sleutel: nrOrigineel **23** · somtypeOrigineel “Verhaalsom min: # [ding], er gaan er # weg. Hoeveel nog?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T1 (8) · regel: G8-T1-door-elkaar
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), onthouden-vergeten (8)
- Verschillende Claude-fout-hints: 2 (meest: “Weg is aftrekken.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-043` (Claude T1, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de winkel liggen 795 appels. Er worden er 34 verkocht. Hoeveel appels liggen er nog?
    - **Antwoord:** 761  (controle: n.v.t.)
    - **Fout-hints (Claude):** 829 → Weg is aftrekken. · 771 → Kijk of je moest lenen bij de tientallen.
    - **Uitleg (Claude):** 795 − 34 = 761.
  - `G5-GET-E05-claude-bank-naar-049` (Claude T1, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de sporthal zitten 445 mensen. Er gaan er 107 naar huis. Hoeveel mensen zitten er nog?
    - **Antwoord:** 338  (controle: n.v.t.)
    - **Fout-hints (Claude):** 552 → Weg is aftrekken. · 348 → Kijk of je moest lenen bij de tientallen.
    - **Uitleg (Claude):** 445 − 107 = 338.

- **Hint 1 (te schrijven):** Er gaat een deel weg, dus er blijven er minder over. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Ouderzin:** Je kind haalt in een verhaal iets af van een getal tot 1000.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er gaat een deel weg, dus er blijven er minder over. Haal het tweede getal van het eerste af.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Haal de tientallen nog eens af. Ga je bij de eenheden over een heel tiental heen? Dan gaat er nog een tiental af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 20: Verhaalsom plus: # [ding], er komen er # bij. Hoeveel nu?

- Sleutel: nrOrigineel **24** · somtypeOrigineel “Verhaalsom plus: # [ding], er komen er # bij. Hoeveel nu?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: T1 (8) · regel: G8-T1-door-elkaar
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): verkeerde-bewerking (8), tiental-ernaast (8)
- Verschillende Claude-fout-hints: 2 (meest: “Erbij is optellen.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-042` (Claude T1, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de winkel liggen 505 appels. Er komen er 90 bij. Hoeveel appels liggen er nu?
    - **Antwoord:** 595  (controle: ok)
    - **Fout-hints (Claude):** 415 → Erbij is optellen. · 585 → Tel de tientallen nog eens.
    - **Uitleg (Claude):** 505 + 90 = 595.
  - `G5-GET-E05-claude-bank-naar-051` (Claude T1, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de zaal zitten 188 mensen. Er komen er 74 bij. Hoeveel mensen zitten er nu?
    - **Antwoord:** 262  (controle: ok)
    - **Fout-hints (Claude):** 114 → Erbij is optellen. · 252 → Tel de tientallen nog eens.
    - **Uitleg (Claude):** 188 + 74 = 262.

- **Hint 1 (te schrijven):** Er komen er nog bij, dus het worden er meer. Tel de twee getallen bij elkaar op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt in een verhaal iets bij een getal tot 1000 op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen er nog bij, dus het worden er meer. Tel de twee getallen bij elkaar op.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Zijn de eenheden samen tien of meer? Dan komt er een tiental bij.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukken bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 21: [wie] heeft # [ding] en geeft er # weg. Hoeveel [ding] houdt [wie] over?

- Sleutel: nrOrigineel **13** · somtypeOrigineel “[wie] heeft # [ding] en geeft er # weg. Hoeveel [ding] houdt [wie] over?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C3 (8) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (16), verkeerde-bewerking (8), kleinste-van-grootste (7)
- Verschillende Claude-fout-hints: 11 (meest: “Je zit één tiental te hoog. Vul aan tot het volgende honderdtal en tel dan verder.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-402` (Claude C3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een dino heeft 400 blaadjes en geeft er 113 weg. Hoeveel blaadjes houdt de dino over?
    - **Antwoord:** 287  (controle: ok)
    - **Fout-hints (Claude):** 297 → Je zit één tiental te hoog. Vul aan tot het volgende honderdtal en tel dan verder. · 277 → Je zit één tiental te laag. Vul aan tot het volgende honderdtal en tel dan verder. · 313 → Je mag niet zomaar per cijfer het kleinste van het grootste afhalen. Vul liever aan vanaf het kleine getal. · 513 → Er gaan blaadjes weg, dus het worden er minder. Aftrekken, niet optellen.
    - **Uitleg (Claude):** Vul aan vanaf 113: 113 + 87 = 200. Dan nog 200 erbij tot 400. Samen: 87 + 200 = 287.
  - `G5-GET-E05-claude-bank-401` (Claude C3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een konijn heeft 300 wortels en geeft er 112 weg. Hoeveel wortels houdt het konijn over?
    - **Antwoord:** 188  (controle: ok)
    - **Fout-hints (Claude):** 198 → Je zit één tiental te hoog. Vul aan tot het volgende honderdtal en tel dan verder. · 178 → Je zit één tiental te laag. Vul aan tot het volgende honderdtal en tel dan verder. · 212 → Je mag niet zomaar per cijfer het kleinste van het grootste afhalen. Vul liever aan vanaf het kleine getal. · 412 → Er gaan wortels weg, dus het worden er minder. Aftrekken, niet optellen.
    - **Uitleg (Claude):** Vul aan vanaf 112: 112 + 88 = 200. Dan nog 100 erbij tot 300. Samen: 88 + 100 = 188.

- **Hint 1 (te schrijven):** Er worden dingen weggegeven, dus er blijven er minder over. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** In plaats van eraf halen kun je ook aanvullen: spring vanaf het kleinste getal eerst naar het volgende hele tiental of honderdtal, en dan door naar het grootste getal. Hoe groot zijn je sprongen samen?
- **Ouderzin:** Je kind rekent uit hoeveel er overblijft als er iets wordt weggegeven (tot 1000).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2 (tekst per item)) → Er gaan … weg, dus het worden er minder. Aftrekken, niet optellen.  [Claude, ok]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er worden dingen weggegeven, dus er blijven er minder over.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het aantal dat wordt weggegeven. De vraag is hoeveel er nog over zijn.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Je zit één tiental te hoog. Vul aan tot het volgende honderdtal en tel dan verder.  [Claude, ok]
  - `tiental te weinig` (fout = antwoord − 10) → Je zit één tiental te laag. Vul aan tot het volgende honderdtal en tel dan verder.  [Claude, ok]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Bij de tientallen ga je over een heel honderdtal heen: dan gaat er nog een honderdtal af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `kleinste van de grootste` (fout = antwoord + 2 of meer) → Dat is te veel. Je kunt niet per plek het kleine cijfer van het grote afhalen. Vul liever aan: spring vanaf het tweede getal naar het eerste getal.  [Claude, taalfix]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 22: Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **25** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **7** · Claude-doelen: T3 (7) · regel: D8-SCHAT-NAAR-G5
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 7 (meest: “Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-001` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 131 + 362 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 500  (controle: n.v.t.)
    - **Fout-hints (Claude):** 470 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 400 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
    - **Uitleg (Claude):** 131 wordt 100 en 362 wordt 400. 100 + 400 = 500.
  - `G5-GET-E05-claude-bank-naar-010` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 113 + 780 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 900  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1100 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 800 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
    - **Uitleg (Claude):** 113 wordt 100 en 780 wordt 800. 100 + 800 = 900.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op honderdtallen. Kijk bij elk getal naar de tientallen: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Tel ze bij elkaar op.
- **Ouderzin:** Je kind schat een plussom: eerst beide getallen afronden op honderdtallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op honderdtallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op honderdtallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 23: Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit. — met overschrijding van het tiental

- Sleutel: nrOrigineel **26** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op tientallen en reken dan uit. — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **7** · Claude-doelen: T3 (7) · regel: D8-SCHAT-NAAR-G5
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “Dat is het precieze antwoord. Hier maak je een schatting. Rond eerst af zoals in de vraag staat.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-014` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 84 + 87 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 170  (controle: n.v.t.)
    - **Fout-hints (Claude):** 171 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 200 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E05-claude-bank-naar-026` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 34 + 77 ongeveer? Rond beide getallen af op tientallen en reken dan uit.
    - **Antwoord:** 110  (controle: n.v.t.)
    - **Fout-hints (Claude):** 107 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 100 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op tientallen. Kijk bij elk getal naar de eenheden: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Tel ze bij elkaar op.
- **Ouderzin:** Je kind schat een plussom: eerst beide getallen afronden op tientallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de eenheden.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de eenheden.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op tientallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op tientallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 24: Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — met overschrijding van het tiental

- Sleutel: nrOrigineel **27** · somtypeOrigineel “Hoeveel is # + # [ding]? Rond beide getallen af op honderdtallen en reken dan uit. — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T3 (6) · regel: D8-SCHAT-NAAR-G5
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 6 (meest: “Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-002` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 278 + 598 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 900  (controle: n.v.t.)
    - **Fout-hints (Claude):** 876 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 800 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.
  - `G5-GET-E05-claude-bank-naar-006` (Claude T3, bank, niveau 1 → basis)
    - **Opgave:** Hoeveel is 131 + 259 ongeveer? Rond beide getallen af op honderdtallen en reken dan uit.
    - **Antwoord:** 400  (controle: n.v.t.)
    - **Fout-hints (Claude):** 300 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 600 → Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan ga je naar boven.

- **Hint 1 (te schrijven):** Rond eerst beide getallen af op honderdtallen. Kijk bij elk getal naar de tientallen: vijf of meer? Dan rond je naar boven af. Minder dan vijf? Dan naar beneden.
- **Hint 2 (te schrijven):** Reken dan uit met de ronde getallen. Tel ze bij elkaar op.
- **Ouderzin:** Je kind schat een plussom: eerst beide getallen afronden op honderdtallen, dan uitrekenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `precies uitgerekend` (fout = getal1 + getal2) → Dat is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst beide getallen af, en reken dan uit.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Heb je elk getal goed afgerond? Kijk bij elk getal naar de tientallen.  [nieuw]
  - `anders afgerond` (Claudes sleutel (zonder label)) → Rond beide getallen af op honderdtallen, zoals de vraag zegt. Reken daarna uit met de ronde getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af op honderdtallen. Reken daarna uit met de ronde getallen.  [nieuw]
- Status: hints klaar

## Somtype 25: Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? — met overschrijding van het tiental

- Sleutel: nrOrigineel **28** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # + # [ding] kloppen? — met overschrijding van het tiental” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T3 (6) · regel: D8-KLOPPEN-NAAR-G5
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (6), laatste-cijfer (4), bovengrens (1), ondergrens (1)
- Verschillende Claude-fout-hints: 12 (meest: “Rond eerst af. 200 + 300 is 500. Ligt 48 daar dichtbij?”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-058` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 215 + 268 kan kloppen?
    - **Opties:** A) 483 · B) 48 · C) 485
    - **Antwoord:** 483  (controle: n.v.t.)
    - **Fout-hints (Claude):** 583 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G5-GET-E05-claude-bank-naar-065` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 47 + 76 kan kloppen?
    - **Opties:** A) 123 · B) 23 · C) 125
    - **Antwoord:** 123  (controle: n.v.t.)
    - **Fout-hints (Claude):** 23 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond beide getallen af en tel ze op. Zo weet je ongeveer hoe groot de uitkomst is.
- **Hint 2 (te schrijven):** Kijk daarna naar de laatste cijfers. Op welk cijfer moet de uitkomst eindigen? Kies het antwoord dat in de buurt ligt en op dat cijfer eindigt.
- **Ouderzin:** Je kind kiest zonder uit te rekenen welk antwoord bij een plussom kan kloppen: afronden en naar het laatste cijfer kijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te ver weg` (Claudes sleutel: orde-van-grootte) → Rond eerst af en reken dat uit. Ligt dit antwoord daar in de buurt?  [Claude, taalfix]
  - `ander laatste cijfer` (Claudes sleutel: laatste-cijfer) → Tel de laatste cijfers van de twee getallen bij elkaar op. Op welk cijfer eindigt dat? Eindigt dit antwoord daarop?  [Claude, taalfix]
  - `te groot` (Claudes sleutel: bovengrens) → Rond allebei naar boven af en tel ze op. Groter dan dat kan de uitkomst niet zijn. Is dit antwoord groter?  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Rond allebei naar beneden af en tel ze op. Kleiner dan dat kan de uitkomst niet zijn. Is dit antwoord kleiner?  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af en tel ze op. Zo weet je ongeveer hoe groot de uitkomst is. Kijk daarna naar de laatste cijfers.  [nieuw]
- Status: hints klaar

## Somtype 26: Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen? — zonder overschrijding van het tiental

- Sleutel: nrOrigineel **29** · somtypeOrigineel “Kijk zonder uit te rekenen. Welk antwoord bij # − # [ding] kloppen? — zonder overschrijding van het tiental” (koppeling: claudeId)
- Items: **6** · Claude-doelen: T3 (6) · regel: D8-KLOPPEN-NAAR-G5
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): orde-van-grootte (5), laatste-cijfer (4), bovengrens (2), ondergrens (1)
- Verschillende Claude-fout-hints: 12 (meest: “Rond eerst af. 700 − 600 is 100. Ligt 48 daar dichtbij?”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-naar-069` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 708 − 560 kan kloppen?
    - **Opties:** A) 148 · B) 48 · C) 150
    - **Antwoord:** 148  (controle: n.v.t.)
    - **Fout-hints (Claude):** 48 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G5-GET-E05-claude-bank-naar-074` (Claude T3, bank, niveau 1 → toepassen)
    - **Opgave:** Kijk zonder uit te rekenen. Welk antwoord bij 302 − 240 kan kloppen?
    - **Opties:** A) 62 · B) 620 · C) 6
    - **Antwoord:** 62  (controle: n.v.t.)
    - **Fout-hints (Claude):** 72 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan. · 52 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Rond beide getallen af en haal het tweede van het eerste af. Zo weet je ongeveer hoe groot de uitkomst is.
- **Hint 2 (te schrijven):** Kijk daarna naar de laatste cijfers. Op welk cijfer moet de uitkomst eindigen? Kies het antwoord dat in de buurt ligt en op dat cijfer eindigt.
- **Ouderzin:** Je kind kiest zonder uit te rekenen welk antwoord bij een minsom kan kloppen: afronden en naar het laatste cijfer kijken.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `te ver weg` (Claudes sleutel: orde-van-grootte) → Rond eerst af en reken dat uit. Ligt dit antwoord daar in de buurt?  [Claude, taalfix]
  - `ander laatste cijfer` (Claudes sleutel: laatste-cijfer) → Haal het laatste cijfer van het tweede getal af van het laatste cijfer van het eerste. Kan dat niet? Doe er dan eerst tien bij. Eindigt dit antwoord op dat cijfer?  [Claude, taalfix]
  - `te groot` (Claudes sleutel: bovengrens) → Rond het eerste getal naar boven af en het tweede naar beneden. Haal ze van elkaar af. Groter dan dat kan de uitkomst niet zijn. Is dit antwoord groter?  [Claude, taalfix]
  - `te klein` (Claudes sleutel: ondergrens) → Rond het eerste getal naar beneden af en het tweede naar boven. Haal ze van elkaar af. Kleiner dan dat kan de uitkomst niet zijn. Is dit antwoord kleiner?  [Claude, taalfix]
  - `andere fout` (andere fout) → Rond beide getallen af en haal het tweede van het eerste af. Zo weet je ongeveer hoe groot de uitkomst is. Kijk daarna naar de laatste cijfers.  [nieuw]
- Status: hints klaar

## Somtype 27: In [plek] liggen # [ding]. Er komen # [ding] bij. Hoeveel liggen er nu?

- Sleutel: nrOrigineel **14** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen # [ding] bij. Hoeveel liggen er nu?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C2 (4) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (8), verkeerde-bewerking (4), onthouden-vergeten (2)
- Verschillende Claude-fout-hints: 7 (meest: “Je zit één tiental te hoog. Tel de tientallen nog eens rustig na.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-325` (Claude C2, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de vallei liggen 593 stenen. Er komen 290 stenen bij. Hoeveel stenen liggen er nu?
    - **Antwoord:** 883  (controle: ok)
    - **Fout-hints (Claude):** 893 → Je zit één tiental te hoog. Tel de tientallen nog eens rustig na. · 873 → Je zit één tiental te laag. Tel de tientallen nog eens rustig na. · 783 → Als de tientallen samen boven de 100 komen, gaat er een honderdtal bij. Vergeet die niet. · 303 → Er komen stenen bij, dus je telt op. Niet aftrekken.
    - **Uitleg (Claude):** Rijg in stappen: eerst de honderdtallen, dan de tientallen. 593 + 200 = 793, dan + 90 = 883.
  - `G5-GET-E05-claude-bank-323` (Claude C2, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In het bos liggen 146 dennenappels. Er komen 140 dennenappels bij. Hoeveel dennenappels liggen er nu?
    - **Antwoord:** 286  (controle: ok)
    - **Fout-hints (Claude):** 296 → Je zit één tiental te hoog. Tel de tientallen nog eens rustig na. · 276 → Je zit één tiental te laag. Tel de tientallen nog eens rustig na. · 6 → Er komen dennenappels bij, dus je telt op. Niet aftrekken.
    - **Uitleg (Claude):** Rijg in stappen: eerst de honderdtallen, dan de tientallen. 146 + 100 = 246, dan + 40 = 286.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Tel de twee getallen bij elkaar op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt in een verhaal iets bij een getal tot 1000 op.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1 (tekst per item)) → Er komen … bij, dus je telt op. Niet aftrekken.  [Claude, ok]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Je zit één tiental te hoog. Tel de tientallen nog eens rustig na.  [Claude, ok]
  - `tiental te weinig` (fout = antwoord − 10) → Je zit één tiental te laag. Tel de tientallen nog eens rustig na.  [Claude, ok]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Komen de tientallen samen op tien of meer? Dan komt er een honderdtal bij. Vergeet dat niet.  [Claude, taalfix]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen, de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 28: Op [plek] lagen # [ding]. Er zijn er # [ding]. Hoeveel [ding] liggen er nog?

- Sleutel: nrOrigineel **15** · somtypeOrigineel “Op [plek] lagen # [ding]. Er zijn er # [ding]. Hoeveel [ding] liggen er nog?” (koppeling: claudeId)
- Items: **3** · Claude-doelen: C5 (3) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (6), verkeerde-bewerking (3)
- Verschillende Claude-fout-hints: 3 (meest: “Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-394` (Claude C5, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** Op de kinderboerderij lagen 378 veren. Er zijn er 143 weggehaald. Hoeveel veren liggen er nog?
    - **Antwoord:** 235  (controle: ok)
    - **Fout-hints (Claude):** 335 → Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens. · 245 → Bij het lenen van een tiental wordt het tiental één minder. Tel de tientallen nog eens. · 521 → Er zijn er weggehaald: dit is een minsom.
    - **Uitleg (Claude):** Haal eerst de honderdtallen eraf: 378 − 100 = 278. Dan de tientallen: − 40 = 238. Dan de eenheden: − 3 = 235.
  - `G5-GET-E05-claude-bank-393` (Claude C5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de kinderboerderij lagen 456 veren. Er zijn er 127 weggehaald. Hoeveel veren liggen er nog?
    - **Antwoord:** 329  (controle: ok)
    - **Fout-hints (Claude):** 429 → Bij het lenen van een honderdtal wordt het honderdtal één minder. Tel de honderdtallen nog eens. · 339 → Bij het lenen van een tiental wordt het tiental één minder. Tel de tientallen nog eens. · 583 → Er zijn er weggehaald: dit is een minsom.
    - **Uitleg (Claude):** Haal eerst de honderdtallen eraf: 456 − 100 = 356. Dan de tientallen: − 20 = 336. Dan de eenheden: − 7 = 329.

- **Hint 1 (te schrijven):** Er zijn dingen weggehaald, dus er liggen er minder. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Haal ze één voor één van het eerste getal af.
- **Ouderzin:** Je kind rekent uit hoeveel er nog liggen als er iets is weggehaald (tot 1000).
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er zijn er weggehaald: dit is een minsom.  [Claude, ok]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er zijn dingen weggehaald, dus er liggen er minder.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het aantal dat is weggehaald. De vraag is hoeveel er nog liggen.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Ga je bij de eenheden over een heel tiental heen? Dan gaat er nog een tiental af.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Haal de honderdtallen nog eens af.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar

## Somtype 29: In [plek] liggen # [ding] en op [plek] #. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **16** · somtypeOrigineel “In [plek] liggen # [ding] en op [plek] #. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C4 (2) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (4), tiental-ernaast (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-247` (Claude C4, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** In de dierentuin liggen 528 ballen en op de kinderboerderij 248. Hoeveel ballen zijn dat samen?
    - **Antwoord:** 776  (controle: ok)
    - **Fout-hints (Claude):** 676 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 766 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 786 → Controleer de tientallen: je hebt er een te veel. · 280 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 500 + 200 = 700, 20 + 40 = 60, 8 + 8 = 16. Samen: 700 + 60 + 16 = 776.
  - `G5-GET-E05-claude-bank-246` (Claude C4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het bos liggen 644 noten en op de kinderboerderij 296. Hoeveel noten zijn dat samen?
    - **Antwoord:** 940  (controle: ok)
    - **Fout-hints (Claude):** 840 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 930 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 950 → Controleer de tientallen: je hebt er een te veel. · 348 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 600 + 200 = 800, 40 + 90 = 130, 4 + 6 = 10. Samen: 800 + 130 + 10 = 940.

- **Hint 1 (te schrijven):** Samen betekent: bij elkaar optellen. Tel de twee getallen op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt twee aantallen tot 1000 bij elkaar op.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Samen betekent optellen.  [Claude, ok]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Controleer de tientallen: je hebt er één te veel.  [Claude, taalfix]
  - `tiental te weinig` (fout = antwoord − 10) → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij.  [Claude, ok]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.  [Claude, ok]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen, de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 30: In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen?

- Sleutel: nrOrigineel **17** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Hoeveel zijn het er samen?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: D4-3 (2) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (2), een-ernaast (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-377` (Claude D4-3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de vallei liggen 87 stenen. Er komen er 22 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 109  (controle: ok)
    - **Fout-hints (Claude):** 99 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 108 → Ga eerst naar 90, en tel dan 19 erbij. · 65 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 87 + 3 = 90. Dan de rest erbij: 90 + 19 = 109.
  - `G5-GET-E05-claude-bank-378` (Claude D4-3, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de schuur liggen 81 noten. Er komen er 26 bij. Hoeveel zijn het er samen?
    - **Antwoord:** 107  (controle: ok)
    - **Fout-hints (Claude):** 97 → Je gaat over het tiental heen, dus er komt een tiental bij. Tel de tientallen nog eens. · 106 → Ga eerst naar 90, en tel dan 17 erbij. · 55 → Er komt bij: het getal wordt groter.
    - **Uitleg (Claude):** Eerst naar het tiental: 81 + 9 = 90. Dan de rest erbij: 90 + 17 = 107.

- **Hint 1 (te schrijven):** Er komen dingen bij, dus het worden er meer. Tel de twee getallen bij elkaar op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen (als het die heeft), tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt in een verhaal iets bij een getal tot 1000 op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Er komen dingen bij, dus het worden er meer.  [Claude, taalfix]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Dat is één tiental te veel. Tel de tientallen nog eens bij elkaar.  [nieuw]
  - `honderdtal vergeten` (fout = antwoord − 10) → Dat is één tiental te weinig. De tientallen komen samen op tien of meer: dan komt er een honderdtal bij.  [nieuw]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. De tientallen komen samen op tien of meer: dan komt er een honderdtal bij.  [nieuw]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen (als het die heeft), de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 31: Op [plek] liggen # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **18** · somtypeOrigineel “Op [plek] liggen # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C4 (2) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (4), tiental-ernaast (2), verkeerde-bewerking (2)
- Verschillende Claude-fout-hints: 4 (meest: “Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-397` (Claude C4, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** Op de kinderboerderij liggen 337 noten en in het bos 479. Hoeveel noten zijn dat samen?
    - **Antwoord:** 816  (controle: ok)
    - **Fout-hints (Claude):** 716 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 806 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 826 → Controleer de tientallen: je hebt er een te veel. · 142 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 300 + 400 = 700, 30 + 70 = 100, 7 + 9 = 16. Samen: 700 + 100 + 16 = 816.
  - `G5-GET-E05-claude-bank-396` (Claude C4, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Op de kinderboerderij liggen 633 wortels en in de schuur 215. Hoeveel wortels zijn dat samen?
    - **Antwoord:** 848  (controle: ok)
    - **Fout-hints (Claude):** 748 → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij. · 838 → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij. · 858 → Controleer de tientallen: je hebt er een te veel. · 418 → Samen betekent optellen.
    - **Uitleg (Claude):** Per positie: 600 + 200 = 800, 30 + 10 = 40, 3 + 5 = 8. Samen: 800 + 40 + 8 = 848.

- **Hint 1 (te schrijven):** Samen betekent: bij elkaar optellen. Tel de twee getallen op.
- **Hint 2 (te schrijven):** Splits het tweede getal in honderdtallen, tientallen en eenheden. Tel ze één voor één bij het eerste getal.
- **Ouderzin:** Je kind telt twee aantallen tot 1000 bij elkaar op.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `min gedaan` (fout = getal1 - getal2 of getal2 - getal1) → Samen betekent optellen.  [Claude, ok]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Tel de eenheden nog eens bij elkaar.  [nieuw]
  - `tiental te veel` (fout = antwoord + 10) → Controleer de tientallen: je hebt er één te veel.  [Claude, taalfix]
  - `tiental te weinig` (fout = antwoord − 10) → Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij.  [Claude, ok]
  - `honderdtal te veel` (fout = antwoord + 100) → Dat is één honderdtal te veel. Tel de honderdtallen nog eens bij elkaar.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Tel de tientallen nog eens: als ze samen 100 of meer zijn, komt er een honderdtal bij.  [Claude, ok]
  - `andere fout` (andere fout) → Tel de twee getallen uit het verhaal bij elkaar. Tel het tweede getal er in stukjes bij: de honderdtallen, de tientallen en de eenheden.  [nieuw]
- Status: hints klaar

## Somtype 32: Op [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?

- Sleutel: nrOrigineel **19** · somtypeOrigineel “Op [plek] liggen # [ding]. Er gaan er # weg. Hoeveel blijven er over?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C6 (2) · regel: G5-C04-plusmin-context
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (4), een-ernaast (2)
- Verschillende Claude-fout-hints: 6 (meest: “Na 500 kom je in de 400-en. 500 − 4 eindigt op 96.”)
- Voorbeelden:
  - `G5-GET-E05-claude-bank-399` (Claude C6, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** Op de kinderboerderij liggen 502 noten. Er gaan er 6 weg. Hoeveel blijven er over?
    - **Antwoord:** 496  (controle: ok)
    - **Fout-hints (Claude):** 506 → Na 500 kom je in de 400-en. 500 − 4 eindigt op 96. · 596 → Je gaat onder 500, dus het honderdtal wordt één minder. · 495 → Ga eerst precies naar 500 (dat is 2 eraf), en dan de rest.
    - **Uitleg (Claude):** Ga eerst naar het ronde getal: 502 − 2 = 500. Dan de rest eraf: 500 − 4 = 496.
  - `G5-GET-E05-claude-bank-398` (Claude C6, gegenereerd, niveau 1 → toepassen)
    - **Opgave:** Op de kinderboerderij liggen 304 eieren. Er gaan er 9 weg. Hoeveel blijven er over?
    - **Antwoord:** 295  (controle: ok)
    - **Fout-hints (Claude):** 305 → Na 300 kom je in de 200-en. 300 − 5 eindigt op 95. · 395 → Je gaat onder 300, dus het honderdtal wordt één minder. · 294 → Ga eerst precies naar 300 (dat is 4 eraf), en dan de rest.
    - **Uitleg (Claude):** Ga eerst naar het ronde getal: 304 − 4 = 300. Dan de rest eraf: 300 − 5 = 295.

- **Hint 1 (te schrijven):** Er gaan dingen weg, dus er blijven er minder over. Haal het tweede getal van het eerste af.
- **Hint 2 (te schrijven):** Je gaat onder het hele honderdtal. Ga eerst terug naar het hele honderdtal, en haal daarna de rest eraf.
- **Ouderzin:** Je kind haalt een getal af van een getal tot 1000, over een heel honderdtal heen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `niets eraf` (fout = antwoord + getal2) → Dat is het getal waarmee je begint. Er gaan dingen weg, dus er blijven er minder over.  [nieuw]
  - `het getal dat weggaat` (fout = getal2) → Dat is het getal dat weggaat. De vraag is hoeveel er nog over zijn.  [nieuw]
  - `één te veel` (fout = antwoord + 1) → Bijna! Dat is één te veel. Reken de eenheden nog eens na.  [nieuw]
  - `één te weinig` (fout = antwoord − 1) → Bijna! Dat is één te weinig. Reken de eenheden nog eens na.  [nieuw]
  - `onder het honderdtal (tiental)` (fout = antwoord + 10) → Dat is te veel. Je gaat onder het hele honderdtal. Ga eerst terug naar het hele honderdtal, en haal dan de rest eraf.  [nieuw]
  - `tiental te weinig` (fout = antwoord − 10) → Dat is één tiental te weinig. Haal de tientallen nog eens af.  [nieuw]
  - `onder het honderdtal` (fout = antwoord + 100) → Dat is één honderdtal te veel. Je gaat onder het hele honderdtal, dus het honderdtal wordt één minder.  [nieuw]
  - `honderdtal te weinig` (fout = antwoord − 100) → Dat is één honderdtal te weinig. Haal de honderdtallen nog eens af.  [nieuw]
  - `andere fout` (andere fout) → Haal het tweede getal van het eerste af. Reken na: jouw antwoord plus wat er weggaat, moet het getal zijn waarmee je begint.  [nieuw]
- Status: hints klaar
