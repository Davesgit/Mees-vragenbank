# G5-VBN-E03 — Patronen herkennen en voortzetten

Onze omschrijving: Patronen in rijen getallen/figuren herkennen & voortzetten · in onze bank: 8 items

Claude-vragen gemapt: **24** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [patroon] patroon in een verhaal of figuur

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[patroon] patroon in een verhaal of figuur” (koppeling: claudeId)
- Items: **15** · Claude-doelen: G11 (15) · regel: G5-V01-patroon
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (1 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): een-ernaast (15), verkeerde-bewerking (5), optellen-ipv-vermenigvuldigen (4), None (3), deel-vergeten-bij-splitsen (2), getal-overgenomen (1)
- Verschillende Claude-fout-hints: 30 (meest: “Je hebt 9 en 6 opgeteld. Elk zakje heeft 6 knikkers, dus je hebt 6 negen keer nodig.”)
- Voorbeelden:
  - `G5-VBN-E03-claude-bank-019` (Claude G11, ai, niveau 1 → basis)
    - **Opgave:** In zakje 1 zitten 6 knikkers, in zakje 2 twaalf knikkers en in zakje 3 achttien knikkers. Zo gaat het verder. Hoeveel knikkers zitten er in zakje 9?
    - **Opties:** A) 54 · B) 15 · C) 48
    - **Antwoord:** 54  (controle: n.v.t.)
    - **Fout-hints (Claude):** 15 → Je hebt 9 en 6 opgeteld. Elk zakje heeft 6 knikkers, dus je hebt 6 negen keer nodig. · 48 → Controleer of je 8 of 9 zakjes hebt geteld.
    - **Uitleg (Claude):** Elk zakje erbij geeft 6 knikkers meer. Bij 9 zakjes hoort 9 keer 6. Dat is 54 knikkers.
  - `G5-VBN-E03-claude-bank-013` (Claude G11, ai, niveau 2 → toepassen)
    - **Opgave:** In je spaarpot zit nu 12 euro. Elke week doe je er 3 euro bij. Hoeveel euro zit er na 10 weken in?
    - **Opties:** A) 39 euro · B) 42 euro · C) 30 euro
    - **Antwoord:** 42 euro  (controle: n.v.t.)
    - **Fout-hints (Claude):** 30 euro → Je bent het geld vergeten dat er nu al in zit. · 39 euro → Kijk nog eens hoeveel weken er precies 3 euro bij komt.
    - **Uitleg (Claude):** In 10 weken komt er 10 keer 3 euro bij, dat is 30 euro. Daar hoort de 12 euro van het begin nog bij. Samen is dat 42 euro.

- **Hint 1 (te schrijven):** Kijk wat er elke keer bijkomt, of wat er steeds terugkomt. Kijk ook waarmee het begint.
- **Hint 2 (te schrijven):** Ga vanaf het begin stap voor stap verder tot je bij de plek uit de vraag bent. Of reken het uit: hoeveel stappen zijn het, en hoeveel komt er per stap bij?
- **Ouderzin:** Je kind zoekt de regel in een patroon (een verhaal, figuur of herhaling) en gaat ermee verder.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde bewerking (per item)` (Claudes sleutel: verkeerde-bewerking) → Je hebt 12 en 3 bij elkaar opgeteld. Bedenk hoe vaak er 3 blokken bijkomen. / Je hebt 6 en 8 opgeteld. Reken eerst uit hoeveel de plant in 8 weken groeit. / Alleen voor de eerste driehoek heb je 3 stokjes nodig. Voor de volgende driehoeken heb je minder nodig. / Je hebt 10 en 2 bij elkaar opgeteld. Kijk nog eens hoeveel blokken er per plek bijkomen. / Alleen voor het eerste vierkant heb je 4 lucifers nodig. De vierkanten erna delen een lucifer.  [Claude, taalfix]
  - `één stap ernaast (per item)` (Claudes sleutel: een-ernaast) → Bij plek 1 begin je met 1 stip, niet met 2. Kijk hoeveel stappen van 2 erbij komen. / Je hebt één stap van 2 te ver gezet. Tel de stappen vanaf plek 1 nog eens. / Controleer of je bij plek 11 of bij plek 12 bent uitgekomen. / Kijk nog eens hoeveel weken er precies 3 euro bijkomt. / De bus van 8:00 uur is al de eerste. Tel daarna nog vier keer 15 minuten. / Je bent één bus te vroeg gestopt. Tel nog eens welke bus de vijfde is. / Tel de 11 extra driehoeken van 2 stokjes en vergeet de eerste driehoek niet. / Kijk bij welke rij 40 tegels horen. Ga daarna nog één rij verder. / Reken na welke plek bij 18 blokken hoort. Ga daarna nog één stap verder. / Elke groep van drie eindigt met dezelfde kleur. Kijk of 12 precies een groep afmaakt. / Controleer of je 8 of 9 zakjes hebt geteld. / Kijk bij welk getal de herhaling van drie precies rond is. Daarna tel je verder in het patroon. / Op alle oneven plekken staat steeds dezelfde vrucht. Kijk of 25 even of oneven is. / Kijk bij hoeveel tafels 56 stoelen horen. Er staat nog een tafel meer. / Reken na bij welke ronde 95 punten horen. Er komt nog een ronde bij.  [Claude, taalfix]
  - `optellen in plaats van keer (per item)` (Claudes sleutel: optellen-ipv-vermenigvuldigen) → Je hebt 9 en 5 opgeteld. In elke rij zitten steeds 5 tegels meer dan in de rij ervoor. / Je hebt 9 en 6 opgeteld. Er komen elke keer 6 knikkers bij. Je rekent dus 9 keer 6. / Je hebt 15 en 4 opgeteld. Elke tafel heeft zelf al 4 stoelen nodig. / Je hebt 20 en 5 opgeteld. Bedenk dat je elke ronde opnieuw 5 punten krijgt.  [Claude, taalfix]
  - `per item` (Claudes sleutel (tekst per item)) → Claudes tekst per foute optie (nagekeken: noemt de fout of wijst de weg bij dit item)  [Claude, ok]
  - `andere fout` (andere fout) → Kijk wat er elke keer bijkomt, of wat er steeds terugkomt. Kijk ook waarmee het begint. Ga dan stap voor stap verder.  [nieuw]
- Status: hints klaar

## Somtype 2: [patroon] getallenrij

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[patroon] getallenrij” (koppeling: claudeId)
- Items: **9** · Claude-doelen: G11 (9) · regel: G5-V01-patroon
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig — niet live zonder beeld** (2 items): de vraag verwijst naar een plaatje, maar Claude gaf geen tekening (Visual: nodig)
- Denkfouten (Claude): een-ernaast (9), verkeerde-bewerking (5), None (2), getal-overgenomen (2)
- Verschillende Claude-fout-hints: 18 (meest: “Kijk hoeveel je elke keer verder springt van het ene getal naar het volgende.”)
- Voorbeelden:
  - `G5-VBN-E03-claude-bank-003` (Claude G11, ai, niveau 1 → basis)
    - **Opgave:** Een rij getallen gaat zo. 3, 6, 9, 12, 15. Welk getal komt op plek 6?
    - **Opties:** A) 18 · B) 16 · C) 21
    - **Antwoord:** 18  (controle: ok)
    - **Fout-hints (Claude):** 16 → Kijk hoeveel je elke keer verder springt van het ene getal naar het volgende. · 21 → Je bent één plek te ver gegaan. Tel vanaf 15 maar één stap verder.
    - **Uitleg (Claude):** Elke stap wordt het getal 3 groter. Na 15 komt dus 15 + 3. Dat is 18.
  - `G5-VBN-E03-claude-bank-005` (Claude G11, ai, niveau 2 → toepassen)
    - **Opgave:** Een rij getallen gaat zo. 7, 14, 21, 28. Welk getal staat op plek 9?
    - **Opties:** A) 63 · B) 56 · C) 70
    - **Antwoord:** 63  (controle: ok)
    - **Fout-hints (Claude):** 56 → Tel goed hoeveel stappen je nog moet zetten na plek 4. Plek 8 is nog niet plek 9. · 70 → Je bent één stap te ver gegaan. Kijk nog eens welk getal precies bij plek 9 hoort.
    - **Uitleg (Claude):** Elke plek komt er 7 bij. Het getal op een plek is dus 7 keer het plaatsnummer. 9 keer 7 is 63.

- **Hint 1 (te schrijven):** Kijk van het ene getal naar het volgende. Wat gebeurt er elke keer: komt er iets bij, gaat er iets af, of wordt het getal dubbel?
- **Hint 2 (te schrijven):** Kijk welke stap er elke keer gebeurt, en doe die stap steeds opnieuw. Wordt er naar een plek gevraagd? Tel de plekken mee tot je bij die plek bent.
- **Ouderzin:** Je kind zoekt de regel in een getallenrij en gaat ermee verder.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `één stap ernaast (per item)` (Claudes sleutel: een-ernaast) → 70 staat op plek 4. Ga van daaruit verder naar plek 6. / Je hebt een stap te ver gezet. Stop precies bij plek 6. / Tel hoeveel stappen van 8 terug je vanaf plek 1 zet om bij plek 8 te komen. / Je hebt één stap te ver gezet. Stop precies bij plek 8. / Kijk hoeveel je elke keer verder springt van het ene getal naar het volgende. / Tel goed hoeveel stappen je nog moet zetten na plek 4. Plek 8 is nog niet plek 9. / Je bent één stap te ver gegaan. Kijk nog eens welk getal precies bij plek 9 hoort. / Tel de plekken goed mee. 50 staat op plek 1. Ga door tot plek 7. / Reken het verschil tussen 2 en 9 nog eens na op de getallenlijn.  [Claude, taalfix]
  - `getal overgenomen (per item)` (Claudes sleutel: getal-overgenomen) → Je hebt 2 opgeteld bij het laatste getal. Kijk of het getal misschien elke keer dubbel zo groot wordt. / Je hebt naar het tweede getal gekeken. Reken het verschil uit tussen 4 en 7.  [Claude, taalfix]
  - `verkeerde bewerking (per item)` (Claudes sleutel: verkeerde-bewerking) → Kijk nog eens: de sprong van 4 naar 8 is niet even groot als die van 8 naar 16. / Kijk of er steeds hetzelfde getal bijkomt, of dat de sprongen groter worden. / Vergelijk 6 met 3 en 12 met 6. Wat gebeurt er met het getal? / Kijk of 3 keer 1 echt 4 is. Probeer of erbij optellen beter past. / Kijk of 9 het dubbele van 2 is. Zo niet, dan past keer 2 niet.  [Claude, taalfix]
  - `per item` (Claudes sleutel (tekst per item)) → Claudes tekst per foute optie (nagekeken: noemt de fout of wijst de weg bij dit item)  [Claude, ok]
  - `andere fout` (andere fout) → Kijk van het ene getal naar het volgende: wat gebeurt er elke keer? Doe die stap steeds opnieuw en tel de plekken mee.  [nieuw]
- Status: hints klaar
