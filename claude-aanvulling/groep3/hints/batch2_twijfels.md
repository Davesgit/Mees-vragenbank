## Twijfels voor Didactiek/Overzicht (nieuw in batch 2)
- **':' + getal in Claude-opgaven:** M04-1 ('Dan weet je ook: 6 − 4 = □') en M05-6 ('Splits 3: 3 is 1 en hoeveel?') botsen met onze G3-regel. De hints volgen de regel wel. De opgaven zelf moeten in de merge herschreven worden, bijvoorbeeld 'Dan weet je ook dat 6 − 4 = □.' en 'Splits 3. 3 is 1 en hoeveel?'.
- **Minteken:** M05-3 schrijft '4 - 2 =' met een streepje (net als de opties in batch 1). Onze bank gebruikt '−'.
- **'Lees de vraag: komt er iets bij of gaat er iets af?'** heb ik bij verhaaltjes laten staan. Bij kale sommen (M05) en bij vóór/na/tussen (M01) heb ik hem vervangen, want daar is geen verhaal. Hetzelfde als in batch 1 (K01).
- **'Via 10' bij K05-1 en -5 weggelaten:** in die somtypes komt 10 soms als antwoord voor, en dan zou 'vul aan tot 10' het antwoord verklappen. De hint is daar 'tel de rest erbij, één voor één'.
- **M01 tot 100:** ✔ Besluit Overzicht/Didactiek. Het is nu 'Eindigt het getal op een 0? Dan eindigt het getal ervoor op een 9.' (vóór) en '… op een 9? Dan eindigt het getal erna op een 0.' (na). Bij tussen staat: 'Eindigt het kleinste getal op een 9? Dan eindigt het getal ertussen op een 0.'
- **M02-2 ('moeten er nog bij om 20 te maken'):** het doel is altijd 20. De hint zegt 'het getal uit de vraag', zodat hij ook werkt als het doel later anders is.
- **M05-4 en -5:** 'Je zit er eentje naast' van Claude blijft staan bij 1 ernaast. Bij 2 ernaast komt een nieuwe 'bijna'-tekst.
- **apply_hints.py** controleert nu of de kop in de md bij de json past. In de data staan de somtypes in een andere volgorde dan in de md; het nummer volgt de md.
