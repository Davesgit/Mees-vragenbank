# G5 batch 5: twijfels voor Didactiek

Geschreven op 2026-10-01 om 17:48 (Amsterdam). Batch 5 is MEET-E06 (tijd en kalender): 24 somtypes en 1233 items. Alles is per item nagerekend met de data van de rebuild van ±17:45 (`/workspace/g5work/b5check.py`: 0 afwijkingen).
De klokles van G4 (#45) is gevolgd:
- Bij half staat de kleine wijzer tussen twee getallen.
- 'net voorbij' gebruik ik niet: in batch 5 komt kwart over niet voor.
- De laatste bijzin van een kloktekst noemt geen specifieke fout.
- Er is één vaste tekst per soort klok.
De klokitems uit G4 #45 zitten in #24 (half, 16 items) en #5 (digitaal, 6 items). Ze hebben dezelfde teksten als de rest van hun somtype.
In de opgaven staan geen Engelse woorden (alle woorden nagelopen).

## Per item nagerekend (script)
| Uitspraak | Waar | Klopt bij |
|---|---|---|
| 'Bijna! Dat is één dag te veel/te weinig' (antwoord ± 1), 'te veel/te weinig' (2 of meer) | #1 dagen tussen datums | alle sleutels; geen februari in de items |
| 'Tel eerst de minuten tot het volgende hele uur' (Hint 1) | #2 | 220/220 gaan over het hele uur heen; geen enkele begintijd is een heel uur |
| 'Kom je over het hele uur heen? …' (vraag), Hint 2 als voorwaarde | #15 | 1195 (13:05–13:45) en 1197 (10:05–10:55) gaan niet over het hele uur heen, de andere 10 wel |
| 'Dat is zestig minuten te veel/te weinig: een heel uur' (antwoord ± 60) | #2, #15 | alle sleutels (#2: 220 + 173, #15: 12 + 8) |
| 'Heb je gerekend alsof een uur honderd minuten heeft?' (vraag; Claudes sleutel tijd-als-kommagetal) | #2 (77), #15 (10) | alle sleutels > antwoord. De 12 sleutels van #15 die precies + 60 zijn, krijgen eerst 'een uur te veel' |
| 'Hoeveel minuten is het nog tot het volgende hele uur? Begin daarmee.' / 'Tel eerst terug tot dat hele uur' | #3, #4 | 110/110 en 110/110 gaan over het hele uur heen |
| 'Je bent gestopt bij het hele uur' | #3 (49), #4 (58) | elke sleutel is precies dat hele uur |
| 'Dat is een uur te vroeg / te laat' (motorregel klok ± 1 uur) | #3 (110), #4 (110) | antwoord − 60 / + 60 minuten; alle antwoorden liggen tussen 7 en 12 uur (geen tijd van 13 uur of later) |
| 'Dat is te laat' (#3) / 'Dat is te vroeg' (#4) (Claudes sleutel tijd-als-kommagetal) | #3 (171), #4 (162) | alle sleutels na / vóór het antwoord |
| 'Zestig minuten of meer kan niet achter de dubbele punt' | #21 (5), #23 (3) | alle sleutels hebben 60 of meer minuten |
| 'Je bent gestopt waar de nieuwe maand begint / waar de maand ervoor eindigt' | #6 (40), #7 (37) | elke sleutel is de eerste dag van de nieuwe maand / de laatste dag van de vorige maand |
| 'Bijna! Dat is één dag ernaast' | #6 (83), #7 (82) | dezelfde maand, ± 1 dag |
| Hint 1/2 'over de maandgrens' | #6, #7 | 83/83 en 83/83 |
| 'kleine wijzer een uur te ver/te vroeg … De grote wijzer klopt wel' | #5, #12–#14, #16–#20, #24, #22 | zelfde minuten, uur ± 1 (de klok in de klokkenrij nagelezen) |
| 'grote wijzer niet goed' | #5, #8, #9, #12–#14, #16, #18, #20, #24, #22 | zelfde uur, andere minuten |
| 'Bij tien over wijst de grote wijzer naar de twee' enzovoort (Hint 1 per soort) | klokkenrij in woorden | de goede klok heeft altijd die minuten (12/12, 12/12 …) |
| 'De kleine wijzer staat tussen dat uur en het volgende uur' | #5 | minuten 1–55, nooit een heel uur |
| 'Welk getal is de kleine wijzer voorbij?' | #8, #9 | minuten 1–29 en 31–58, nooit een heel uur |
| 'Tot en met kwart over zeg je over, daarna voor half' | #10 | antwoorden: vijf/tien over (5, 10) en tien/vijf voor half (20, 25) |
| 'over half' en 'voor' noemen het getal waar de kleine wijzer naartoe gaat | #11 | minuten 35, 40, 50 |

Hint 1 en Hint 2 hebben geen cijfers (1233/1233). In geen enkele kindtekst van batch 5 staat een cijfer, een aanhalingsteken of een Engels woord. logs/hint_sleutels.json: 0 problemen.

## Twijfels
1. **'voorbij' zonder 'net' bij vijf over en tien over (#12, #14).** Ik schrijf «De kleine wijzer is dan voorbij het uur uit de vraag». Volgens G4 hoort 'net voorbij' alleen bij kwart over. Is 'voorbij' hier goed, of liever 'een klein stukje voorbij'?
2. **Tien voor en vijf voor (#17, #19):** «bijna bij het uur uit de vraag, maar nog net ervoor» (zoals kwart voor in G4). Goed zo?
3. **#10 en #11 (klok → tijd in woorden, 40 items) hebben alleen Hint 1/2 en 'andere fout'.** De motor leest 'vijf over 5' niet (fixlijst #68). Daardoor krijgen alle 80 sleutels van Claude de algemene tekst. Die is waar, maar niet precies.
4. **Reizen (#21, #23) tot 18:15:** hier gebruik ik geen klokregels. Die rekenen in 12 uur, en '15:10' wordt dan '2:10' (#69). Claudes sleutels 'tiental-ernaast' zijn een uur te vroeg en tien minuten ernaast door elkaar. Ze krijgen een neutrale tekst: «Dat klopt niet helemaal. Tel de uren en de minuten nog eens apart erbij. …» (#71).
5. **Richting bij de klok (#8, #9):** bij een foute minuut ('1:09' of '1:05' bij 1:10) zegt de tekst niet of het te vroeg of te laat is. Er is geen regel 'minuut ernaast' (#70). Wel: «Bij die tijd staat de grote wijzer ergens anders. Tel vijf minuten per getal … daarna de streepjes».
6. **Datum later/eerder (#6, #7):** 90 sleutels die verder dan één dag ernaast liggen (bijvoorbeeld 13 juni bij 3 juni), krijgen 'andere datum' (de G4-tekst). Er is geen regel 'te ver/niet ver genoeg' (#70). 'Eén dag ernaast' zegt ook niet welke kant op.
7. **#22 klok zetten (7 items, 7 verschillende tijden):** er is één tekst voor alle soorten, als vraag («Welk uur hoor je in de tijd, en is de kleine wijzer dat uur al voorbij?»). Claudes teksten zijn vervangen: '"tien over half één" is nog vóór een uur' (aanhalingstekens) en 'De kleine wijzer wijst naar de 5' bij tien voor half zes (dat klopt niet). Zie #73.
8. **Niveau:**
   - Klok op de minuut (#5, #8, #9: 234 items, bijvoorbeeld 1:08 en 1:33). Is dat G5?
   - Dagen tellen tot 102 dagen (#1: van 6 maart tot 16 juni). Is dat G5?
   - Zie #75.
