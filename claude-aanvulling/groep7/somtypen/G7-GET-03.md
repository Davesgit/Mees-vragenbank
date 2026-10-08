# G7-GET-03 — Optellen en aftrekken met komma’s

Onze omschrijving: Optellen/aftrekken helen & decimalen · in onze bank: 8 items

Claude-vragen gemapt: **412** in **4** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: # + # =

- Sleutel: nrOrigineel **1** · somtypeOrigineel “# + # =” (koppeling: claudeId)
- Items: **211** · Claude-doelen: B12 (211) · regel: G7-K05-komma-plusmin
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Uit de G6-park: 211 items
- Denkfouten (Claude): tiende-of-honderdste-ernaast (269), komma-verschoven (73), verkeerde-bewerking (44), verhoudingstabel-verkeerd (36)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G7-GET-03-claude-bank-169` (Claude B12, bank, niveau 3 → toepassen)
    - **Opgave:** 6,47 + 2,5 =
    - **Antwoord:** 8,97  (controle: ok)
    - **Fout-hints (Claude):** 89,7 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 8,98 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G7-GET-03-claude-bank-053` (Claude B12, bank, niveau 3 → toepassen)
    - **Opgave:** 2,9 + 0,4 =
    - **Antwoord:** 3,3  (controle: ok)
    - **Fout-hints (Claude):** 33 → Keer 10: de komma schuift één plek naar rechts. Gedeeld door 10: één plek naar links. · 2,5 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar, met de komma’s precies onder elkaar.
- **Hint 2 (te schrijven):** Heeft een getal minder cijfers achter de komma? Zet er nullen achter. Tel van rechts naar links: eerst de honderdsten, dan de tienden, dan de hele getallen. De komma in de uitkomst staat onder de komma’s.
- **Ouderzin:** Je kind telt kommagetallen op door de komma’s onder elkaar te zetten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiende ernaast` (fout = antwoord ± 0,1) → Dat is een tiende ernaast. Tel de tienden nog eens. Kwamen de honderdsten samen op tien of meer? Dan gaat er precies één tiende mee, anders niets.  [nieuw]
  - `een honderdste ernaast` (fout = antwoord ± 0,01) → Dat is een honderdste ernaast. Tel de honderdsten nog eens. Klopt het?  [nieuw]
  - `min in plaats van plus` (Claudes sleutel: verkeerde-bewerking) → Is dit een plussom of een minsom? Kijk naar het teken.  [Claude, taalfix]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Zet de getallen onder elkaar met de komma’s precies onder elkaar.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zet de komma’s onder elkaar en tel per plek op, van rechts naar links.  [nieuw]
- Status: hints klaar

## Somtype 2: # − # =

- Sleutel: nrOrigineel **2** · somtypeOrigineel “# − # =” (koppeling: claudeId)
- Items: **193** · Claude-doelen: B12 (193) · regel: G7-K05-komma-plusmin
- Getallenruimte: kommagetallen (1 cijfers achter de komma), kommagetallen (2 cijfers achter de komma) · type: kale
- Uit de G6-park: 193 items
- Denkfouten (Claude): tiende-of-honderdste-ernaast (278), komma-verschoven (45), verkeerde-bewerking (43), verhoudingstabel-verkeerd (20)
- Verschillende Claude-fout-hints: 3 (meest: “Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.”)
- Voorbeelden:
  - `G7-GET-03-claude-bank-316` (Claude B12, bank, niveau 3 → toepassen)
    - **Opgave:** 6,47 − 1,75 =
    - **Antwoord:** 4,72  (controle: ok)
    - **Fout-hints (Claude):** 4,82 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 4,73 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na.
  - `G7-GET-03-claude-bank-313` (Claude B12, bank, niveau 3 → toepassen)
    - **Opgave:** 2,9 − 0,4 =
    - **Antwoord:** 2,5  (controle: ok)
    - **Fout-hints (Claude):** 2,51 → Je komma staat goed, maar kijk nog eens naar de cijfers achter de komma. Tel de tienden en de honderdsten apart na. · 3,3 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Zet de getallen onder elkaar, met de komma’s precies onder elkaar.
- **Hint 2 (te schrijven):** Heeft een getal geen of minder cijfers achter de komma? Zet er nullen achter. Haal van rechts naar links af: eerst de honderdsten, dan de tienden, dan de hele getallen. Is het bovenste cijfer te klein? Leen dan één van de plek ervoor: jouw cijfer krijgt er tien bij, en het cijfer op de plek ervoor één minder. Is het cijfer op de plek ervoor een nul? Dan wordt die nul een negen, en leen je verder naar links.
- **Ouderzin:** Je kind trekt kommagetallen van elkaar af door de komma’s onder elkaar te zetten.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een tiende ernaast` (fout = antwoord ± 0,1) → Dat is een tiende ernaast. Haal de tienden nog eens af. Moest je bij de honderdsten lenen? Dan is er bij de tienden één minder, anders niet.  [nieuw]
  - `een honderdste ernaast` (fout = antwoord ± 0,01) → Dat is een honderdste ernaast. Reken de honderdsten nog eens na. Klopt het?  [nieuw]
  - `plus in plaats van min` (Claudes sleutel: verkeerde-bewerking) → Is dit een plussom of een minsom? Kijk naar het teken.  [Claude, taalfix]
  - `komma verschoven` (Claudes sleutel: komma-verschoven) → Staat de komma op de goede plek? Zet de getallen onder elkaar met de komma’s precies onder elkaar.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zet de komma’s onder elkaar en haal per plek af, van rechts naar links.  [nieuw]
- Status: hints klaar

## Somtype 3: [plek] heeft # [ding], [plek] heeft er #. Hoeveel [ding] heeft [plek]?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[plek] heeft # [ding], [plek] heeft er #. Hoeveel [ding] heeft [plek]?” (koppeling: claudeId)
- Items: **6** · Claude-doelen: C13 (6) · regel: G7-C04-cijferend-min
- Getallenruimte: 0–100.000 · type: kale
- Uit de G6-park: 6 items
- Denkfouten (Claude): onthouden-vergeten (6), verkeerde-bewerking (6), kleinste-van-grootste (5)
- Verschillende Claude-fout-hints: 3 (meest: “Heb je ergens geleend? Dan is de kolom links één minder.”)
- Voorbeelden:
  - `G7-GET-03-claude-bank-427` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Het moeras heeft 86.204 blaadjes, de vallei heeft er 9778. Hoeveel meer heeft het moeras?
    - **Antwoord:** 76.426  (controle: ok)
    - **Fout-hints (Claude):** 77.426 → Heb je ergens geleend? Dan is de kolom links één minder. · 95.982 → Hoeveel méér is het verschil. Aftrekken. · 83.574 → Per kolom haal je het onderste van het bovenste af. Lukt dat niet, dan leen je.
    - **Uitleg (Claude):** Schat eerst: 86.000 − 10.000 is ongeveer 76.000. Reken dan precies, kolom voor kolom met lenen: 76.426.
  - `G7-GET-03-claude-bank-430` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Het veld heeft 84.888 ballen, de kleedkamer heeft er 9111. Hoeveel meer heeft het veld?
    - **Antwoord:** 75.777  (controle: ok)
    - **Fout-hints (Claude):** 76.777 → Heb je ergens geleend? Dan is de kolom links één minder. · 93.999 → Hoeveel méér is het verschil. Aftrekken. · 85.777 → Per kolom haal je het onderste van het bovenste af. Lukt dat niet, dan leen je.
    - **Uitleg (Claude):** Schat eerst: 85.000 − 9000 is ongeveer 76.000. Reken dan precies, kolom voor kolom met lenen: 75.777.

- **Hint 1 (te schrijven):** Hoeveel meer: dat is het verschil tussen de twee getallen. Welke som maak je?
- **Hint 2 (te schrijven):** Zet het grootste getal bovenaan en het kleinste eronder, met de cijfers precies onder elkaar. Haal per kolom af, van rechts naar links. Is het bovenste cijfer kleiner? Leen dan één van de kolom ervoor: jouw cijfer krijgt er tien bij, en het cijfer in de kolom ervoor één minder. Is het cijfer in de kolom ervoor een nul? Dan wordt die nul een negen, en leen je verder naar links.
- **Ouderzin:** Je kind rekent uit hoeveel meer de een heeft dan de ander, met getallen tot honderdduizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Komt er iets bij of gaat er iets af? De vraag is hoeveel meer de een heeft dan de ander.  [nieuw]
  - `geleend maar niet afgehaald` (fout = antwoord + 1000 (geleend bij de duizendtallen)) → Dat is duizend te veel. Je hebt bij de duizendtallen geleend. Heb je daar de één afgehaald?  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Reken de duizendtallen nog eens na.  [nieuw]
  - `kleinste cijfer van het grootste` (Claudes sleutel: kleinste-van-grootste) → Heb je bij elke kolom het kleinste cijfer van het grootste afgehaald? Bij een minsom haal je altijd het onderste cijfer van het bovenste af.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zet het grootste getal bovenaan en haal het kleinste eraf, kolom voor kolom.  [nieuw]
- Status: hints klaar

## Somtype 4: Het huis heeft # [ding], de klas heeft er #. Hoeveel [ding] heeft het huis?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “het huis heeft # [ding], de klas heeft er #. Hoeveel [ding] heeft het huis?” (koppeling: claudeId)
- Items: **2** · Claude-doelen: C13 (2) · regel: G7-C04-cijferend-min
- Getallenruimte: 0–100.000 · type: kale
- Uit de G6-park: 2 items
- Denkfouten (Claude): onthouden-vergeten (2), verkeerde-bewerking (2), kleinste-van-grootste (2)
- Verschillende Claude-fout-hints: 3 (meest: “Heb je ergens geleend? Dan is de kolom links één minder.”)
- Voorbeelden:
  - `G7-GET-03-claude-bank-432` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Het huis heeft 38.592 stenen, de klas heeft er 12.834. Hoeveel meer heeft het huis?
    - **Antwoord:** 25.758  (controle: ok)
    - **Fout-hints (Claude):** 26.758 → Heb je ergens geleend? Dan is de kolom links één minder. · 51.426 → Hoeveel méér is het verschil. Aftrekken. · 26.362 → Per kolom haal je het onderste van het bovenste af. Lukt dat niet, dan leen je.
    - **Uitleg (Claude):** Schat eerst: 39.000 − 13.000 is ongeveer 26.000. Reken dan precies, kolom voor kolom met lenen: 25.758.
  - `G7-GET-03-claude-bank-431` (Claude C13, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Het huis heeft 72.261 stickers, de klas heeft er 9387. Hoeveel meer heeft het huis?
    - **Antwoord:** 62.874  (controle: ok)
    - **Fout-hints (Claude):** 63.874 → Heb je ergens geleend? Dan is de kolom links één minder. · 81.648 → Hoeveel méér is het verschil. Aftrekken. · 77.126 → Per kolom haal je het onderste van het bovenste af. Lukt dat niet, dan leen je.
    - **Uitleg (Claude):** Schat eerst: 72.000 − 9000 is ongeveer 63.000. Reken dan precies, kolom voor kolom met lenen: 62.874.

- **Hint 1 (te schrijven):** Hoeveel meer: dat is het verschil tussen de twee getallen. Welke som maak je?
- **Hint 2 (te schrijven):** Zet het grootste getal bovenaan en het kleinste eronder, met de cijfers precies onder elkaar. Haal per kolom af, van rechts naar links. Is het bovenste cijfer kleiner? Leen dan één van de kolom ervoor: jouw cijfer krijgt er tien bij, en het cijfer in de kolom ervoor één minder. Is het cijfer in de kolom ervoor een nul? Dan wordt die nul een negen, en leen je verder naar links.
- **Ouderzin:** Je kind rekent uit hoeveel meer de een heeft dan de ander, met getallen tot honderdduizend.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Komt er iets bij of gaat er iets af? De vraag is hoeveel meer de een heeft dan de ander.  [nieuw]
  - `geleend maar niet afgehaald` (fout = antwoord + 1000 (geleend bij de duizendtallen)) → Dat is duizend te veel. Je hebt bij de duizendtallen geleend. Heb je daar de één afgehaald?  [nieuw]
  - `duizend te veel` (fout = antwoord + 1000) → Dat is duizend te veel. Reken de duizendtallen nog eens na.  [nieuw]
  - `kleinste cijfer van het grootste` (Claudes sleutel: kleinste-van-grootste) → Heb je bij elke kolom het kleinste cijfer van het grootste afgehaald? Bij een minsom haal je altijd het onderste cijfer van het bovenste af.  [Claude, taalfix]
  - `andere fout` (andere fout) → Zet het grootste getal bovenaan en haal het kleinste eraf, kolom voor kolom.  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'het huis heeft # [ding], de klas heeft er #. Hoeveel [ding] heeft het huis?'. Nakijken of ze nog passen.
- Status: hints klaar
