# G5 batch 2: twijfels voor Didactiek

Geschreven op 2026-10-01 om 16:28 (Amsterdam). Batch 2 bestaat uit GET-E06, GET-E07, GET-M02 en GET-M03: 25 somtypes en 1551 items. Alles is per item nagekeken met de data van de rebuild van 16:13 (132 somtypes, 4843 items). In batch 2 zitten geen klokitems: de klokitems uit G4 #45 staan in G5-MEET-E06 (batch 5).

## Les 1b, per somtype nagerekend
| Uitspraak | Waar | Klopt bij |
|---|---|---|
| 'Splits het eerste getal: honderdtallen, tientallen en eenheden (als het die heeft)' en 'Doe elk stuk keer het tweede getal' | E07 #1 | 328/328. Getal1 ligt tussen 13 en 322 (31 items van 100 of meer, 3 items met een rond tiental). Getal2 ligt tussen 3 en 9. |
| 'Splits het grootste getal in tientallen en eenheden. Doe allebei keer het andere getal' | E07 #4, #6, #8, #11–#13, #15–#17 | Bij alle items is het grootste getal 10 of meer en eindigt het niet op 0. Het andere getal is kleiner dan 10. |
| 'Reken eerst zonder de nullen. Zet de nullen er daarna weer achter.' | E07 #5, #7, #9, #10, #14 | Bij alle items eindigt minstens één getal op 0. Bij #5 is getal1 30–300 en bij #10 is het 20 × 40. Daarom staat er 'nullen' en niet 'één nul'. |
| 'Begin met tien keer' | E07 #3 | Alle antwoorden liggen tussen 11 en 29. |
| Centen over de honderd of lenen | E06 #1, #2, #3 | Dit staat er alleen als vraag ('Komen de centen samen op honderd cent of meer?', 'Heeft het eerste bedrag minder centen …?'). Bij #1 gaat het in 358 van de 565 items zo, bij #2 in 234 van de 483. |
| 'Kijk naar het eerste, middelste of laatste cijfer' | M02 | Alle getallen hebben 3 cijfers (131–885). |
| 'munten tot twee euro' | M03 | Het hoogste antwoord is €1,90. |

'één' staat overal met accenten. Er zitten geen afrondregels in deze batch, dus het cijfer 5 komt niet voor.

## Twijfels
1. **Geld (E06, M03): alles gaat via de sleutels van Claude.**
   - fout_regels rekent niet met bedragen. '€21,95' is geen getal en `_nums` knipt bij de komma.
   - Daarom krijgt elke denkfout één vaste tekst op de sleutels van Claude (#48). De bron heet dan 'claude-taalfix', ook als de tekst helemaal nieuw is, omdat de motor dat zo vraagt. In de telling vallen die teksten daardoor onder 'taalfix' en niet onder 'nieuw'.
   - **E06 #1/#2 'centen ernaast':** de sleutels zijn ± 10 cent en ± 1 cent door elkaar, dus de richting is niet te zeggen. De tekst is «Bijna! Je zit er tien cent of één cent naast. Reken de centen achter de komma nog eens na.» Is dat goed genoeg, totdat er geldregels komen (fixlijst #19)? Bij 80 van de 1289 sleutels verschillen ook de hele euro's, dus 'de euro's kloppen' kon niet.
   - **E06 'komma op de verkeerde plek':** de sleutels zijn tien keer te groot of tien keer te klein. Claudes «Keer 10: de komma schuift …» past daar niet bij. De nieuwe tekst is «De komma staat op de verkeerde plek. Hoeveel hele euro's zijn het ongeveer? Kijk of je antwoord daarbij past.»
   - **E06 #3/#4:**
     - 'euro te veel' is altijd + €1.
     - 'tien cent te weinig' is altijd − 10 cent.
     - 'centen niet goed' vervangt Claudes vaste voorbeeld ('5 tienden + 2 tienden … ,70'), dat bij geen enkel item past.
     - 'dubbeltje' en 'tienden' zijn weg.
2. **E07 #6–#17 (12 somtypes met 1 item): één tekst per denkfout, niet per item.**
   - Claudes teksten noemden per item de stukken, bijvoorbeeld «5 × 10 = 50 klopt …» of «80 + 48, wat komt daar uit?». Dat verklapt het antwoord bijna. Ze staan nu in claudeVervangen.
   - De teksten die ervoor in de plaats komen:
     - **Een stuk vergeten** (alle sleutels te weinig): «Dat is te weinig. Je bent iets vergeten. Splits het grootste getal …»
     - **Nul** in twee richtingen:
       - te veel, via de leesbare regel 'fout = antwoord + 2 of meer': «Dat is te veel: er staat een nul te veel achter. …»
       - te weinig, op de sleutels van Claude: «Dat is te weinig: er mist een nul. …»
     - **Cijfers omgedraaid:** «Je hebt de goede cijfers, maar in een andere volgorde. …»
     - **Tafelbuur (#15):** «Dat is te weinig. Reken het stuk met de eenheden nog eens na.»
   - **'opgeteld' (#4–#17):** sjabloon met [getal1]/[getal2], dat fout_regels per item invult: «Je hebt [getal1] en [getal2] opgeteld. Maar het is steeds hetzelfde aantal, een paar keer: dat is een keersom.» Dat noemt alleen de getallen uit de vraag en niet het antwoord.
   - **#6 apart:** de sleutel 180 bij 18 × 5 is 18 × 10. Claude noemde het 'nul-fout'. De tekst is nu «Dat is te veel. Je hebt keer tien gedaan, maar het zijn er minder. Lees nog eens hoeveel je er ziet.»
   - **Hint 1:** per somtype met de woorden die in de kop vast staan (hok, touw, minuut, uur, vakantie, rondjes …). Ik begin steeds bij het aantal groepjes en eindig met 'Dat is een keersom'. Is dat te sturend? Het verklapt de som niet.
3. **E07 #2 'welke som': volgorde '42 × 16'.**
   - Het verhaal is 'In elke doos 42 appels, 16 dozen' en het antwoord is '42 × 16'. In de Nederlandse didactiek is het meestal 'aantal groepjes × grootte' (16 × 42).
   - De hints noemen geen volgorde en geen teken. Hint 2 is «Steeds hetzelfde aantal, een paar keer: welke som past daarbij?» Dit is een besluit voor Didactiek (fixlijst #23).
   - Bij de foute optie ':' hoort een eigen tekst ('er wordt niets verdeeld'). Daarvoor gebruik ik de letterlijke regel ':'.
4. **E07 #1 'iets vergeten' (onthouden-vergeten, 70 sleutels).**
   - Alle sleutels zijn te weinig, maar de waarden lopen uiteen: antwoord − 100, maar ook '5' (getal2) of '55' (getal1).
   - Claudes «als die boven de 10 komen, hoort er een 1 bij de tientallen» gaat over plussommen. De nieuwe tekst is «Dat is te weinig. Reken elk stuk apart uit. Tel daarna alle stukken bij elkaar op, en vergeet er geen.»
5. **E07 #3 verdelen.** Claude gebruikte 'deler', en dat vind ik een moeilijk woord. De nieuwe tekst is 'het aantal waarover je verdeelt' / 'het aantal dat verdeeld wordt'. Is dat duidelijk genoeg?
6. **M02 (MAB, 4 items per somtype): Claude heeft geen fout-hints en geen denkfouten.**
   - Eigen regels zijn 'fout = getal1' (het hele getal) en 'fout = eenheden van getal1' (bij #1 en #3: het aantal losse blokjes).
   - Andere foute invoer valt onder 'andere fout'.
   - Hint 2 noemt de plek van het cijfer (eerste, middelste of laatste cijfer). Is dat niet te veel weggegeven? Het getal zelf wordt niet genoemd.
7. **M03 (geld tellen, meerkeuze):**
   - '€3' en '€4' zijn letterlijke regels voor 'aantal munten' (13 opties). Claude heeft daar wel een denkfout ('getal-overgenomen'), maar geen tekst.
   - apply_hints meldt 'regel niet te lezen' bij items die die optie niet hebben. Dat is alleen informatie.
   - 'munten vergeten' en 'euro en cent door elkaar' zijn een taalfix van Claudes tekst, met 'te weinig' of 'veel te veel' erbij. Alle sleutels liggen aan die kant.
8. **Engelse woorden (in de opgaven, niet in onze hints).**
   - 'shirt(s)' komt voor in E06 #3 item 011 ('een shirt') en in E07 #4 item 436 en #5 items 447 en 448. Mijn voorstel is **'trui'** (truien). Dit staat in de opgave, dus dat doet Overzicht of de generator (fixlijst #21).
   - 'sticker(s)', 'club' en 'trainer' heb ik laten staan, omdat het gangbaar Nederlands is. In onze hints staat geen van deze woorden.
9. **Grammatica van Claude:** «Élke kind heeft …» (E07 #4). Die tekst is vervangen.
