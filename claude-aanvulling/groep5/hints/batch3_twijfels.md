# G5 batch 3: twijfels voor Didactiek

Geschreven op 2026-10-01 om 16:58 (Amsterdam). Batch 3 bestaat uit GET-M04, GET-M05 en GET-M06: 23 somtypes en 314 items. Alles is per item nagekeken met de data van de rebuild van 16:55 (121 somtypes, 4843 items; batch 3 is in die rebuilds niet veranderd).
De lessen uit de review van batch 2 zitten er al in: 'een aantal keer' (S4), «Ze hebben allemaal evenveel» (S5), geen [getal] in 'andere fout' (#35), en uitspraken alleen als ze bij elke sleutel kloppen.

## Per item nagerekend (script)
| Uitspraak | Waar | Klopt bij |
|---|---|---|
| Er blijft altijd iets over (rest groter dan 0): 'Het komt niet precies uit: er blijft iets over', 'Dan heeft niet iedereen een plek', 'Dan kan niet iedereen mee' | M06 #3 (16), #4 (16), #6 (8), #7 (5), #8 (3) | 48/48 rest > 0 |
| De deelsom komt precies uit ('Zeg de tafel op tot je **precies** bij …'; 'Ze hebben allemaal evenveel') | M06 #2 (32), #5 (10), #9 (3); M05 #1 (70), #2 (15) | 130/130 rest 0 |
| 'nog een ronde' (regel antwoord + getal2): «Daar past nog een hele ronde bij … De rest is altijd kleiner dan het aantal waarover je verdeelt.» | M06 #3, #6 | 24/24 sleutels zijn rest + getal2. Bij 3 sleutels is dat toevallig ook het quotiënt; de tekst klopt dan nog steeds (te veel, en er past nog een ronde bij). |
| 'wat ieder krijgt' (Claudes sleutel andere-deel-genomen) | M06 #3 | 13/13 sleutels zijn het quotiënt |
| 'niets over' (Claudes sleutel rest-vergeten) | M06 #3 | 16/16 sleutels zijn 0 |
| 'de rest' (Claudes sleutel andere-deel-genomen) | M06 #4 | 16/16 sleutels zijn de rest |
| 'één te veel': «Eén stap hoger in de tafel kom je boven het totaal uit.» | M06 #4 | 16/16 (quotiënt + 1, en (q + 1) × getal2 is meer dan getal1) |
| 'één tafel te weinig' / 'één te weinig' (antwoord − 1 = het quotiënt) | M06 #7, #8 | 8/8 |
| 'keer gedaan' (getal1 × getal2) | M05 #1, #2; M06 #2, #5, #9 | 130/130. Het product is nooit het antwoord. |
| 'het getal waardoor je deelt' / 'het aantal in elk' / 'het totaal' (getal2) | M05 #1, #2; M06 #2, #5 | Bij elke sleutel is de waarde getal2. Bij M06 #2 dekt dit Claudes sleutel getal-overgenomen (161, 167, 172 en 180 vielen eerst weg). |
| 'De getallen staan andersom' (Claudes sleutel omgekeerd-gedeeld) | M06 #1 | 90/90: de optie is 'b : a' |
| 'één groepje te veel/te weinig' = antwoord ± de grootte van een groepje; 'in elk groepje één te veel/te weinig' = antwoord ± het aantal groepjes | M05 #4 en #10 (groepjes = getal1); #7, #8, #9, #11, #12 (groepjes = getal2) | 20/20, per item gelezen uit de opgave ('Er staan 8 trommels. In elke trommel 6' tegenover 'Elke eekhoorn heeft 9 noten. Er zijn 8 eekhoorns') |
| 'Komen de tientallen samen op tien of meer?' (vraag) | M04 #1 | 1/1 (490 + 160: 9 + 6 tientallen) |
| 'Weet je het niet meteen? Begin bij een som die je wel weet, zoals tien keer' | M05 #3, #4, #7–#12 | Alle getallen zijn 9 of kleiner |

'één' staat overal met accenten. Er zijn geen afrondregels, dus het cijfer 5 komt niet voor. Er staat geen ':' direct voor een getal in een kindtekst (check_merge_notatie: 0).

## Twijfels
1. **'Keer gedaan' bij deelsommen is een eigen regel, geen sleutel van Claude.**
   - Claude heeft alleen bij M05 #2 een sleutel voor 'keer in plaats van delen' (15/15). Bij M05 #1 (70), M06 #2 (32), #5 (10) en #9 (3) is er geen. Ik heb de regel 'fout = getal1 × getal2' overal gezet, want het kind typt het antwoord.
   - Bij M06 #2 stond eerst een tekst met [getal1]/[getal2]. Daardoor voegde de regel bij typen geen sleutel toe (0/32, fixlijst #35). Nu staat er «Je hebt keer gedaan. Kijk hoeveel er in elk gaan. Hoe vaak past dat in het totaal?»
2. **'Getallen omgedraaid' kan alleen bij M06 #1 (welke som).**
   - Bij de deelsommen die je typt, is 'b : a' geen heel getal. Claude heeft er daar ook geen sleutel voor. Bij M06 #1 is '5 : 60' een foute optie (90/90), met de tekst «De getallen staan andersom. Wat verdeel je? Dat getal komt vóór het deelteken.»
   - Is 'deelteken' een goed woord voor groep 5? 'deler' heb ik vermeden.
3. **Restsommen (M06 #3, #4, #6, #7, #8).**
   - **#3 en #6** vragen naar de rest. Claudes 'rest-vergeten' is bij #3 altijd 0 ('niets over'). Bij #6 zijn het allerlei waarden (7× het quotiënt, 7× iets anders), dus de tekst is algemeen: «Dat is niet wat er overblijft …».
   - **#4** vraagt wat ieder krijgt. '(De rest blijft over.)' staat in de opgave.
   - **#7 en #8** gaan over naar boven afronden (tafels, bussen). Claudes sleutel is daar altijd het quotiënt (antwoord − 1), en dat staat erin als 'één te weinig' met de reden.
   - Mag een Hint 2 bij #7/#8 zeggen «Blijft er na het verdelen nog iemand over? Dan is er nog … nodig»? Het is een vraag, maar hij geeft de strategie weg.
4. **M06 #8: 243 : 25 (1 van de 3 items) valt buiten de tafels.** Het antwoord is 10 bussen. Dat is G5-stof als schatten, maar niet als tafel. Zie fixlijst #39.
5. **M05 #5 (rooster, 8 items): geen sleutels van Claude.** De regels tellen de gekleurde hokjes (getal1 + getal2, één rij, één kolom). Dat werkt zoals in G4 M06, als de app het aantal gekleurde hokjes doorgeeft. 'één rij' en 'één kolom' hebben dezelfde tekst, met opzet: het kind hoeft niet te weten wat een kolom is.
6. **Bron 'claude-taalfix' voor herschreven teksten op Claudes sleutels.** Net als in batch 2: de motor vraagt het zo (#48), ook als de tekst helemaal nieuw is. In de telling van review-batch3.md is dat 12 keer.
7. **'opgeteld' met [getal1]/[getal2] (M05 #4, #7–#12).** Die raakt alleen Claudes sleutels (3 van de 12 items in #4, en de items met 1 voorbeeld). Andere invoer van 'getal1 + getal2' krijgt dan de tekst 'te veel/te weinig'. Dat is niet fout, maar minder precies. Zie fixlijst #35 (b).
8. **Engelse woorden in de opgaven (niet in onze hints):** 'trainer(s)' in M06 022, 026, 047, 048 en 056, en 'shirts' in M06 048 en 060. Mijn voorstel is hetzelfde als V6 van batch 2: kinderen/juffen en truien/knikkers (fixlijst #42). 'sticker' blijft.
9. **Somtypes met 1 item** (M04 #1 en #2; M05 #8–#12) en met 3 of 4 items (M05 #6, #7; M06 #7, #8, #9). De hints zijn per denkfout gelijk aan die van de grote broer, met alleen een eigen Hint 1 voor de context. Samenvoegen zoals #22 ligt voor de hand (fixlijst #40). Als dat gebeurt, krijgen ze één Hint 1 zoals in ronde 2b.
10. **M04 #1: de kop klopt maar half** (zoals #4): 'zonder overschrijding van het tiental' klopt voor de eenheden (0 + 0), maar 490 + 160 gaat wel over het honderdtal. Hint 2 zegt dat als vraag. Zie fixlijst #37.
