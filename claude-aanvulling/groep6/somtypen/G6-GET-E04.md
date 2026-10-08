# G6-GET-E04 — Plus en min tot 10.000

Onze omschrijving: +/− hele getallen ±10.000: standaard + strategieën + schattend · in onze bank: 8 items

Claude-vragen gemapt: **98** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] lagen # [ding]. Er zijn er # weggehaald. Hoeveel [ding] zijn er nog?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In [plek] lagen # [ding]. Er zijn er # weggehaald. Hoeveel [ding] zijn er nog?” (koppeling: claudeId)
- Items: **32** · Claude-doelen: C14 (32) · regel: G6-C02-cijferend-min
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): nul-fout-tientallen (64), onthouden-vergeten (32), verkeerde-bewerking (32)
- Verschillende Claude-fout-hints: 4 (meest: “Als je over een 0 leent, wordt die 0 een 9 en de kolom links ervan één minder. Tel de honderdtallen nog eens.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-037` (Claude C14, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het magazijn lagen 4004 schriften. Er zijn er 3339 weggehaald. Hoeveel schriften zijn er nog?
    - **Antwoord:** 665  (controle: ok)
    - **Fout-hints (Claude):** 765 → Als je over een 0 leent, wordt die 0 een 9 en de kolom links ervan één minder. Tel de honderdtallen nog eens. · 675 → De 0 in de tientallen werd 9 na het lenen. Reken die kolom opnieuw. · 1665 → Je leende uiteindelijk van de duizendtallen: die worden één minder. · 7343 → Er zijn er weggehaald: een minsom.
    - **Uitleg (Claude):** Bij de eenheden kun je 4 − 9 niet, en de tientallen zijn 0. Leen van de honderdtallen of duizendtallen: de nullen worden 9, en de kolom links ervan één minder. Uitkomst: 665.
  - `G6-GET-E04-claude-bank-046` (Claude C14, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** In het sorteercentrum lagen 6054 pakketten. Er zijn er 2638 weggehaald. Hoeveel pakketten zijn er nog?
    - **Antwoord:** 3416  (controle: ok)
    - **Fout-hints (Claude):** 3516 → Als je over een 0 leent, wordt die 0 een 9 en de kolom links ervan één minder. Tel de honderdtallen nog eens. · 3426 → De 0 in de tientallen werd 9 na het lenen. Reken die kolom opnieuw. · 4416 → Je leende uiteindelijk van de duizendtallen: die worden één minder. · 8692 → Er zijn er weggehaald: een minsom.
    - **Uitleg (Claude):** Bij de eenheden kun je 4 − 8 niet. Leen één tiental: bij de eenheden komt er 10 bij, bij de tientallen staat er één minder. Uitkomst: 3416.

- **Hint 1 (te schrijven):** Er zijn er weggehaald: dat is een minsom. Zet de getallen onder elkaar en begin bij de eenheden.
- **Hint 2 (te schrijven):** Is het bovenste cijfer kleiner dan het onderste? Leen dan één van de kolom links ervan: dat cijfer gaat één omlaag, en jouw cijfer krijgt er tien bij. Staat daar een nul? Dan leen je verder naar links, en die nul wordt een negen.
- **Ouderzin:** Je kind rekent een minsom tot 10.000 onder elkaar uit, met lenen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Er zijn er weggehaald: dat is een minsom.  [nieuw]
  - `tien te veel (geleend)` (fout = antwoord + 10 (geleend bij de tientallen)) → Dat is tien te veel. Kijk naar de tientallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden; een nul wordt een negen.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Reken de tientallen nog eens na.  [nieuw]
  - `honderd te veel (geleend)` (fout = antwoord + 100 (geleend bij de honderdtallen)) → Dat is honderd te veel. Kijk naar de honderdtallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden; een nul wordt een negen.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Reken de honderdtallen nog eens na.  [nieuw]
  - `duizend te veel (geleend)` (fout = antwoord + 1000 (geleend bij de duizendtallen)) → Dat is duizend te veel. Kijk naar de duizendtallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Reken de duizendtallen nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Zet de getallen onder elkaar en begin bij de eenheden. Kun je een cijfer niet afhalen? Leen dan van links. Staat daar een nul? Dan leen je verder naar links.  [nieuw]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding], in [plek] #. Hoeveel zijn het er samen? Reken onder elkaar.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding], in [plek] #. Hoeveel zijn het er samen? Reken onder elkaar.” (koppeling: claudeId)
- Items: **16** · Claude-doelen: C12 (16) · regel: G6-C01-cijferend-plus
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (32), tiental-ernaast (16)
- Verschillende Claude-fout-hints: 3 (meest: “Bij de eenheden kwam je boven de 10: die 1 onthoud je en telt mee bij de tientallen.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-068` (Claude C12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de bouwmarkt liggen 3633 tegels, in het magazijn 5159. Hoeveel zijn het er samen? Reken onder elkaar.
    - **Antwoord:** 8792  (controle: ok)
    - **Fout-hints (Claude):** 8782 → Bij de eenheden kwam je boven de 10: die 1 onthoud je en telt mee bij de tientallen. · 8692 → Kijk bij de tientallen: kwam je boven de 10? Dan hoort er een honderdtal bij. · 8802 → Je hebt te vaak onthouden. Onthoud alleen als een kolom boven de 10 komt.
    - **Uitleg (Claude):** Onder elkaar, van rechts naar links: 3 + 9 = 12, schrijf 2, onthoud 1. Ga zo door per kolom. Uitkomst: 8792.
  - `G6-GET-E04-claude-bank-073` (Claude C12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het sorteercentrum liggen 1830 pakketten, in het postkantoor 3461. Hoeveel zijn het er samen? Reken onder elkaar.
    - **Antwoord:** 5291  (controle: n.v.t.)
    - **Fout-hints (Claude):** 5281 → Bij de eenheden kwam je boven de 10: die 1 onthoud je en telt mee bij de tientallen. · 5191 → Kijk bij de tientallen: kwam je boven de 10? Dan hoort er een honderdtal bij. · 5301 → Je hebt te vaak onthouden. Onthoud alleen als een kolom boven de 10 komt.
    - **Uitleg (Claude):** Onder elkaar, van rechts naar links: 0 + 1 = 1, schrijf 1. Ga zo door per kolom. Uitkomst: 5291.

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar: eenheden onder eenheden, tientallen onder tientallen. Begin rechts.
- **Hint 2 (te schrijven):** Komt een kolom samen op tien of meer? Schrijf dan alleen het laatste cijfer op en neem één mee naar de kolom links ervan.
- **Ouderzin:** Je kind telt twee getallen tot 10.000 onder elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt eraf gehaald. Samen is een plussom: tel de getallen bij elkaar op.  [nieuw]
  - `tien te weinig (onthouden)` (fout = antwoord − 10 (onthouden naar de tientallen)) → Dat is tien te weinig. Kwamen de eenheden samen op tien of meer? Dan gaat er één tiental mee naar de tientallen.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Reken de tientallen nog eens na.  [nieuw]
  - `honderd te weinig (onthouden)` (fout = antwoord − 100 (onthouden naar de honderdtallen)) → Dat is honderd te weinig. Kwamen de tientallen samen op tien of meer? Dan gaat er één honderdtal mee naar de honderdtallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Reken de honderdtallen nog eens na.  [nieuw]
  - `duizend te weinig (onthouden)` (fout = antwoord − 1000 (onthouden naar de duizendtallen)) → Dat is duizend te weinig. Kwamen de honderdtallen samen op tien of meer? Dan gaat er één duizendtal mee naar de duizendtallen.  [nieuw]
  - `duizend te weinig` (fout = antwoord − 1000) → Dat is duizend te weinig. Reken de duizendtallen nog eens na.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Tel de tientallen nog eens. Komen de eenheden samen op tien of meer? Dan neem je precies één mee naar de tientallen, anders niets.  [nieuw]
  - `honderd te veel (met overdracht)` (fout = antwoord + 100 (met overdracht naar de honderdtallen)) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Dat komt op tien of meer. Dan neem je precies één mee naar de honderdtallen, niet meer.  [nieuw]
  - `honderd te veel (zonder overdracht)` (fout = antwoord + 100 (zonder overdracht naar de honderdtallen)) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Dat blijft onder de tien. Dan neem je niets mee naar de honderdtallen.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Is dat tien of meer? Dan neem je precies één mee naar de honderdtallen, anders niets.  [nieuw]
  - `andere fout` (andere fout) → Zet de getallen onder elkaar en tel kolom voor kolom op, van rechts naar links. Komt een kolom op tien of meer? Dan gaat er één mee naar links.  [nieuw]
- Status: hints klaar

## Somtype 3: Hoe reken je # + # handig uit?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Hoe reken je # + # handig uit?” (koppeling: claudeId)
- Items: **13** · Claude-doelen: T10 (13) · regel: G6-T02-handig-plusmin
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerd-stukje (11), verkeerde-bewerking (10), allebei-rond (5)
- Verschillende Claude-fout-hints: 3 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-013` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe reken je 196 + 815 handig uit?
    - **Opties:** A) 200 + 800 − 4 · B) 200 + 815 − 4 · C) 200 + 815 + 4
    - **Antwoord:** 200 + 815 − 4  (controle: ok)
    - **Fout-hints (Claude):** 200 + 815 + 4 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 200 + 800 − 4 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.
  - `G6-GET-E04-claude-bank-010` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe reken je 598 + 407 handig uit?
    - **Opties:** A) 600 + 407 + 2 · B) 600 + 400 − 2 · C) 600 + 407 − 2
    - **Antwoord:** 600 + 407 − 2  (controle: ok)
    - **Fout-hints (Claude):** 600 + 407 + 2 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 600 + 400 − 2 → Schatten is rekenen met ronde getallen. Rond eerst allebei de getallen af, elk naar het dichtstbijzijnde ronde getal, en reken dan.

- **Hint 1 (te schrijven):** Maak het eerste getal rond: welk honderdtal ligt er vlak bij? Het tweede getal blijft zoals het is.
- **Hint 2 (te schrijven):** Was het eerste getal kleiner dan het honderdtal? Dan haal je het stukje er aan het eind weer af. Was het groter? Dan doe je het stukje er weer bij.
- **Ouderzin:** Je kind kiest een handige manier voor een plussom: één getal rond maken en daarna bijstellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerd teken` (Claudes sleutel: verkeerde-bewerking) → Het teken aan het eind klopt niet. Heb je het eerste getal groter gemaakt? Dan haal je het stukje er weer af. Heb je het kleiner gemaakt? Dan doe je het er weer bij.  [Claude, taalfix]
  - `allebei rond` (Claudes sleutel: allebei-rond) → Je hebt allebei de getallen rond gemaakt. Maak alleen het eerste getal rond: het tweede getal blijft zoals het is. Zo komt er precies het goede antwoord uit.  [Claude, taalfix]
  - `verkeerd stukje` (Claudes sleutel: verkeerd-stukje) → Het laatste getal klopt niet. Kijk alleen naar het eerste getal: hoeveel scheelt dat met het honderdtal?  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak het eerste getal rond en laat het tweede getal zoals het is. Hoeveel scheelt het eerste getal met het honderdtal? Dat stukje haal je er weer af of doe je er weer bij.  [nieuw]
- Status: hints klaar

## Somtype 4: Welke som is evenveel als # + #?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Welke som is even veel als # + #?” (koppeling: claudeId)
- Items: **11** · Claude-doelen: T10 (11) · regel: G6-T02-handig-plusmin
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): eerste-getal-klopt-niet (15), verkeerde-bewerking (7)
- Verschillende Claude-fout-hints: 2 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-088` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Welke som is evenveel als 605 + 396?
    - **Opties:** A) 609 + 400 · B) 601 + 400 · C) 605 + 400
    - **Antwoord:** 601 + 400  (controle: ok)
    - **Fout-hints (Claude):** 609 + 400 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 605 + 400 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G6-GET-E04-claude-bank-083` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Welke som is evenveel als 729 + 697?
    - **Opties:** A) 626 + 700 · B) 729 + 700 · C) 726 + 700
    - **Antwoord:** 726 + 700  (controle: ok)
    - **Fout-hints (Claude):** 729 + 700 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 626 + 700 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Maak het tweede getal rond. Hoeveel komt er bij het tweede getal bij?
- **Hint 2 (te schrijven):** Wat je bij het tweede getal erbij doet, haal je bij het eerste getal evenveel eraf. Dan blijft de uitkomst gelijk.
- **Ouderzin:** Je kind kiest een plussom met dezelfde uitkomst: bij het ene getal erbij, bij het andere evenveel eraf.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `bij allebei erbij` (Claudes sleutel: verkeerde-bewerking) → Je hebt bij het eerste getal ook iets erbij gedaan. Dan wordt de uitkomst groter. Wat er bij het tweede getal bijkomt, haal je bij het eerste getal eraf.  [Claude, taalfix]
  - `eerste getal klopt niet` (Claudes sleutel: eerste-getal-klopt-niet) → Het eerste getal klopt niet. Wat er bij het tweede getal bijkomt, haal je bij het eerste getal evenveel eraf.  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak het tweede getal rond. Hoeveel kwam erbij? Haal precies zoveel van het eerste getal af.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Welke som is even veel als # + #?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 5: Hoe reken je # − # handig uit?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Hoe reken je # − # handig uit?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: T10 (9) · regel: G6-T02-handig-plusmin
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): verkeerd-stukje (9), allebei-rond (5), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 3 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-026` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe reken je 602 − 497 handig uit?
    - **Opties:** A) 602 − 500 − 3 · B) 602 − 500 + 3 · C) 602 − 500 + 2
    - **Antwoord:** 602 − 500 + 3  (controle: ok)
    - **Fout-hints (Claude):** 602 − 500 − 37 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 602 − 500 + 2 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.
  - `G6-GET-E04-claude-bank-030` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe reken je 697 − 396 handig uit?
    - **Opties:** A) 697 − 400 + 100 · B) 697 − 400 + 4 · C) 697 − 400 + 3
    - **Antwoord:** 697 − 400 + 4  (controle: ok)
    - **Fout-hints (Claude):** 697 − 400 + 100 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag. · 697 − 400 + 3 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. Bij teruggeven: vul aan vanaf de prijs tot het betaalde bedrag.

- **Hint 1 (te schrijven):** Maak het getal dat eraf gaat rond, naar een honderdtal. Het eerste getal blijft zoals het is.
- **Hint 2 (te schrijven):** Haal je met het ronde getal meer af dan nodig? Dan doe je het stukje er weer bij. Haal je minder af? Dan haal je het stukje er nog af.
- **Ouderzin:** Je kind kiest een handige manier voor een minsom: het getal dat eraf gaat rond maken en daarna bijstellen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerd teken` (Claudes sleutel: verkeerde-bewerking) → Het teken aan het eind klopt niet. Heb je meer afgehaald dan nodig? Dan doe je het stukje er weer bij. Heb je minder afgehaald? Dan haal je het stukje er nog af.  [Claude, taalfix]
  - `allebei rond` (Claudes sleutel: allebei-rond) → Je hebt ook het eerste getal rond gemaakt. Maak alleen het getal dat eraf gaat rond: het eerste getal blijft zoals het is. Zo komt er precies het goede antwoord uit.  [Claude, taalfix]
  - `verkeerd stukje` (Claudes sleutel: verkeerd-stukje) → Het laatste getal klopt niet. Kijk naar het getal dat eraf gaat: hoeveel scheelt dat met het honderdtal?  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak het getal dat eraf gaat rond. Hoeveel scheelt dat? Dat stukje doe je er daarna weer bij, of je haalt het er nog af.  [nieuw]
- Status: hints klaar

## Somtype 6: Er waren # [ding] in [plek]. Nu zijn er nog #. Hoeveel [ding] zijn er weg?

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Er waren # [ding] in [plek]. Nu zijn er nog #. Hoeveel [ding] zijn er weg?” (koppeling: claudeId)
- Items: **8** · Claude-doelen: C13 (8) · regel: G6-C02-cijferend-min
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): kleinste-van-grootste (8), onthouden-vergeten (8), verkeerde-bewerking (8)
- Verschillende Claude-fout-hints: 3 (meest: “Je haalt altijd het onderste cijfer van het bovenste af. Is het bovenste kleiner, dan leen je 10 van de kolom links.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-003` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Er waren 9617 kranten in de drukkerij. Nu zijn er nog 7678. Hoeveel kranten zijn er weg?
    - **Antwoord:** 1939  (controle: ok)
    - **Fout-hints (Claude):** 2061 → Je haalt altijd het onderste cijfer van het bovenste af. Is het bovenste kleiner, dan leen je 10 van de kolom links. · 2039 → Als je hebt geleend, is de kolom links ervan één minder geworden. Vergeet dat niet. · 17.295 → Je zoekt hoeveel er weg zijn: het verschil. Dat is aftrekken.
    - **Uitleg (Claude):** Zet de getallen onder elkaar en begin rechts. Kun je een cijfer niet afhalen? Leen dan 10 van de kolom links ervan. 9617 − 7678 = 1939.
  - `G6-GET-E04-claude-bank-007` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Er waren 9598 pakketten in het sorteercentrum. Nu zijn er nog 3149. Hoeveel pakketten zijn er weg?
    - **Antwoord:** 6449  (controle: ok)
    - **Fout-hints (Claude):** 6451 → Je haalt altijd het onderste cijfer van het bovenste af. Is het bovenste kleiner, dan leen je 10 van de kolom links. · 6549 → Als je hebt geleend, is de kolom links ervan één minder geworden. Vergeet dat niet. · 12.747 → Je zoekt hoeveel er weg zijn: het verschil. Dat is aftrekken.
    - **Uitleg (Claude):** Zet de getallen onder elkaar en begin rechts. Kun je een cijfer niet afhalen? Leen dan 10 van de kolom links ervan. 9598 − 3149 = 6449.

- **Hint 1 (te schrijven):** Hoeveel zijn er weg? Haal het getal van nu van het getal van eerst af. Zet ze onder elkaar en begin bij de eenheden.
- **Hint 2 (te schrijven):** Is het bovenste cijfer kleiner dan het onderste? Leen dan één van de kolom links ervan: dat cijfer gaat één omlaag, en jouw cijfer krijgt er tien bij.
- **Ouderzin:** Je kind rekent uit hoeveel er weg zijn: een minsom tot 10.000 onder elkaar.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Er zijn er weg: haal het getal van nu af van het getal van eerst.  [nieuw]
  - `kleinste van grootste` (Claudes sleutel: kleinste-van-grootste) → Je hebt per kolom het kleinste cijfer van het grootste afgehaald. Het onderste cijfer gaat altijd van het bovenste af. Is het bovenste kleiner? Dan leen je van links.  [Claude, taalfix]
  - `tien te veel (geleend)` (fout = antwoord + 10 (geleend bij de tientallen)) → Dat is tien te veel. Kijk naar de tientallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Reken de tientallen nog eens na.  [nieuw]
  - `honderd te veel (geleend)` (fout = antwoord + 100 (geleend bij de honderdtallen)) → Dat is honderd te veel. Kijk naar de honderdtallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Reken de honderdtallen nog eens na.  [nieuw]
  - `duizend te veel (geleend)` (fout = antwoord + 1000 (geleend bij de duizendtallen)) → Dat is duizend te veel. Kijk naar de duizendtallen. Heb je daar geleend? Dan is dat cijfer één kleiner geworden.  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Reken de duizendtallen nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Zet het getal van eerst bovenaan en het getal van nu eronder. Reken kolom voor kolom, van rechts naar links. Is het bovenste cijfer kleiner? Dan leen je van links.  [nieuw]
- Status: hints klaar

## Somtype 7: Welke som is evenveel als # − #?

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Welke som is even veel als # − #?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: T10 (5) · regel: G6-T02-handig-plusmin
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): eerste-getal-klopt-niet (6), verkeerde-bewerking (4)
- Verschillende Claude-fout-hints: 2 (meest: “Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-096` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Welke som is evenveel als 812 − 197?
    - **Opties:** A) 815 − 200 · B) 809 − 200 · C) 915 − 200
    - **Antwoord:** 815 − 200  (controle: ok)
    - **Fout-hints (Claude):** 809 − 200 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 915 − 200 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.
  - `G6-GET-E04-claude-bank-098` (Claude T10, bank, niveau 2 → toepassen)
    - **Opgave:** Welke som is evenveel als 639 − 397?
    - **Opties:** A) 639 − 400 · B) 636 − 400 · C) 642 − 400
    - **Antwoord:** 642 − 400  (controle: ok)
    - **Fout-hints (Claude):** 636 − 400 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af? · 639 − 400 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links.

- **Hint 1 (te schrijven):** Maak het getal dat eraf gaat rond. Hoeveel komt erbij?
- **Hint 2 (te schrijven):** Doe bij het eerste getal evenveel erbij als bij het tweede getal. Dan blijft de uitkomst gelijk.
- **Ouderzin:** Je kind kiest een minsom met dezelfde uitkomst: bij allebei de getallen evenveel erbij.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eerste getal eraf` (Claudes sleutel: verkeerde-bewerking) → Je hebt bij het eerste getal iets afgehaald. Bij een minsom doe je bij allebei de getallen evenveel erbij; dan blijft de uitkomst gelijk.  [Claude, taalfix]
  - `eerste getal klopt niet` (Claudes sleutel: eerste-getal-klopt-niet) → Het eerste getal klopt niet. Doe er precies evenveel bij als bij het getal dat eraf gaat.  [Claude, taalfix]
  - `andere fout` (andere fout) → Maak het getal dat eraf gaat rond. Hoeveel kwam erbij? Doe precies zoveel bij het eerste getal.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-01): de hints zijn geschreven voor 'Welke som is even veel als # − #?'. Nakijken of ze nog passen.
- Status: hints klaar

## Somtype 8: In [plek] zijn # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “In [plek] zijn # [ding] en in [plek] #. Hoeveel [ding] zijn dat samen?” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C12 (4) · regel: G6-C01-cijferend-plus
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): onthouden-vergeten (8), plaatswaarde-verkeerd (3)
- Verschillende Claude-fout-hints: 3 (meest: “Ergens kwam een kolom boven de 10. Dan schrijf je één cijfer op en onthoud je 1 voor de volgende kolom.”)
- Voorbeelden:
  - `G6-GET-E04-claude-bank-082` (Claude C12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In het sorteercentrum zijn 4071 pakketten en in het postkantoor 2548. Hoeveel pakketten zijn dat samen?
    - **Antwoord:** 6619  (controle: n.v.t.)
    - **Fout-hints (Claude):** 6519 → Ergens kwam een kolom boven de 10. Dan schrijf je één cijfer op en onthoud je 1 voor de volgende kolom. · 6719 → Je hebt ergens een 1 te veel onthouden. Loop de kolommen nog eens langs. · 5619 → Vergeet de duizendtallen niet mee te tellen, helemaal links.
    - **Uitleg (Claude):** Zet de getallen onder elkaar en begin rechts. Eenheden: 1 + 8 = 9. Zo verder met tientallen, honderdtallen en duizendtallen. Samen: 6619.
  - `G6-GET-E04-claude-bank-080` (Claude C12, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** In de bibliotheek zijn 5790 boeken en in het depot 2068. Hoeveel boeken zijn dat samen?
    - **Antwoord:** 7858  (controle: n.v.t.)
    - **Fout-hints (Claude):** 7758 → Ergens kwam een kolom boven de 10. Dan schrijf je één cijfer op en onthoud je 1 voor de volgende kolom. · 7958 → Je hebt ergens een 1 te veel onthouden. Loop de kolommen nog eens langs. · 6858 → Vergeet de duizendtallen niet mee te tellen, helemaal links.
    - **Uitleg (Claude):** Zet de getallen onder elkaar en begin rechts. Eenheden: 0 + 8 = 8. Zo verder met tientallen, honderdtallen en duizendtallen. Samen: 7858.

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar: eenheden onder eenheden, tientallen onder tientallen. Begin rechts.
- **Hint 2 (te schrijven):** Komt een kolom samen op tien of meer? Schrijf dan alleen het laatste cijfer op en neem één mee naar de kolom links ervan.
- **Ouderzin:** Je kind telt twee getallen tot 10.000 bij elkaar op.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `eraf gehaald` (fout = getal1 - getal2 of getal2 - getal1) → Je hebt eraf gehaald. Samen is een plussom: tel de getallen bij elkaar op.  [nieuw]
  - `tien te weinig (onthouden)` (fout = antwoord − 10 (onthouden naar de tientallen)) → Dat is tien te weinig. Kwamen de eenheden samen op tien of meer? Dan gaat er één tiental mee naar de tientallen.  [nieuw]
  - `tien te weinig` (fout = antwoord − 10) → Dat is tien te weinig. Reken de tientallen nog eens na.  [nieuw]
  - `honderd te weinig (onthouden)` (fout = antwoord − 100 (onthouden naar de honderdtallen)) → Dat is honderd te weinig. Kwamen de tientallen samen op tien of meer? Dan gaat er één honderdtal mee naar de honderdtallen.  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Reken de honderdtallen nog eens na.  [nieuw]
  - `duizend te weinig (onthouden)` (fout = antwoord − 1000 (onthouden naar de duizendtallen)) → Dat is duizend te weinig. Kwamen de honderdtallen samen op tien of meer? Dan gaat er één duizendtal mee naar de duizendtallen.  [nieuw]
  - `duizend te weinig` (fout = antwoord − 1000) → Dat is duizend te weinig. Reken de duizendtallen nog eens na.  [nieuw]
  - `tien te veel` (fout = antwoord + 10) → Dat is tien te veel. Tel de tientallen nog eens. Komen de eenheden samen op tien of meer? Dan neem je precies één mee naar de tientallen, anders niets.  [nieuw]
  - `honderd te veel (met overdracht)` (fout = antwoord + 100 (met overdracht naar de honderdtallen)) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Dat komt op tien of meer. Dan neem je precies één mee naar de honderdtallen, niet meer.  [nieuw]
  - `honderd te veel (zonder overdracht)` (fout = antwoord + 100 (zonder overdracht naar de honderdtallen)) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Dat blijft onder de tien. Dan neem je niets mee naar de honderdtallen.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. Is dat tien of meer? Dan neem je precies één mee naar de honderdtallen, anders niets.  [nieuw]
  - `andere fout` (andere fout) → Zet de getallen onder elkaar en tel kolom voor kolom op, van rechts naar links. Komt een kolom op tien of meer? Dan gaat er één mee naar links.  [nieuw]
- Status: hints klaar
