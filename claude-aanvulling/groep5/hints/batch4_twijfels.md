# G5 batch 4: twijfels voor Didactiek

Geschreven op 2026-10-01 om 17:12 (Amsterdam). Batch 4 bestaat uit MEET-E01 (lengte), E02 (omtrek), E03 (oppervlakte op het rooster), E04 (inhoud) en E05 (gewicht): 15 somtypes en 553 items. Alles is per item nagekeken met de data van de rebuild van 16:55 (121 somtypes; de rebuild van ±17:03 gaf dezelfde aantallen).
De nieuwe motorregels worden gebruikt waar ze passen: 'fout = antwoord × 10' ('er staat een nul te veel achter') en 'fout = antwoord : 10' ('er mist een nul') bij alle omrekensommen. In batch 4 staan geen geldsommen.
Er staan geen Engelse woorden in de opgaven van batch 4. De klokitems uit G4 #45 (MEET-E06) zitten niet in batch 4 maar in batch 5.

## Per item nagerekend (script)
| Uitspraak | Waar | Klopt bij |
|---|---|---|
| 'er staat een nul te veel achter' (antwoord × 10) / 'er mist een nul' (antwoord : 10) | E01 #1–#4, E04 #2 en #4, E05 #1 en #3 | Alle sleutels: de waarde is precies antwoord × 10 of antwoord : 10 |
| 'Je hebt het getal uit de som overgenomen' (getal1 en Claudes sleutel getal-overgenomen) | idem | Alle sleutels: de waarde is het getal uit de opgave. Bij E01 #2 eerst via Claudes sleutel (5), omdat '10.000' als 10 wordt gelezen. |
| 'Een centimeter is kleiner dan een meter, dus het worden er meer' / cm → m: 'het worden er minder' | idem | Klopt altijd (richting van het omrekenen) |
| 'Dat is te veel' / 'Dat is te weinig' (2 of meer ernaast) | alle omrekensommen, E02, E04 #1 | Alle sleutels: groter of kleiner dan het antwoord |
| 'Je hebt de lengte en de breedte één keer opgeteld' (getal1 + getal2) | E02 #1 (274), #2 (8) | 282/282 |
| 'Je hebt keer gedaan. Dat is de oppervlakte' (getal1 × getal2) | E02 | 281/282. Bij 1 item is lengte × breedte gelijk aan de omtrek (6 × 3 = 18); daar is het het antwoord en dus geen fout. |
| 'een korte/lange zijde vergeten' (antwoord − breedte / − lengte), 'een lange/korte zijde te veel' (antwoord + lengte / + breedte) | E02 | Alle sleutels. De lengte (getal1) is in alle 282 items groter dan de breedte. Valt een waarde samen met een eerdere regel (bijvoorbeeld 4 × 2 = 8 = 4 + 2 + 2), dan wint de eerdere regel en klopt die uitspraak ook. |
| 'Bijna! Dat is één te veel/te weinig' | E02 | Alle sleutels antwoord ± 1. Bij breedte 1 wint 'een korte zijde te veel/vergeten'; dat klopt ook. |
| 'Welk getal op de beker staat daar net onder?' (Hint 1) | E04 #1 | 169/169: het drinken staat nooit precies op een getal, en altijd boven het eerste getal |
| 'Je hebt één hokje te veel gekleurd' / 'te weinig hokjes' | E03 | Regels op het aantal gekleurde hokjes (getal + 1 / kleiner dan het getal) |
| Hint 2 omrekenen: 'zet er twee/drie nullen achter' / 'haal er twee nullen af' | omrekensommen | Bij cm → m (E01 #2) zijn alle aantallen centimeter honderdtallen (2000 tot 10.000) |

Elke Claude-sleutel heeft een fout-hint (0 op 'andere fout'); algemeneFoutHint staat bij alle 553 items. Hint 1 en Hint 2 hebben geen cijfers; 'één' staat overal met accenten. logs/hint_sleutels.json: 0 problemen.

## Twijfels
1. **Referentiematen (E01 #5, E04 #3, E05 #2): Claudes tekst per foute optie blijft.** Die teksten vergelijken met iets dat het kind kent ('1 L is één pak melk', '5 kg is zo zwaar als vijf pakken suiker') en zijn goed. Twee zijn verbeterd: '10 m … Dan kun je nauwelijks sprinten' werd «Dat is te kort. 10 m is iets langer dan een klaslokaal. Een voetbalveld is veel langer.», en '15 g … lucifersdoosje' werd «Dat is te licht. 15 g is zo licht als een paar knikkers. Voelt een appel zo licht aan?». De andere teksten zeggen niet altijd of het te veel of te weinig is ('Past dat?'). Mag dat bij schatten?
2. **Maatbeker (E04 #1, 169 items): alleen 'te veel' en 'te weinig'.** De foute opties zijn vaak één streepje ernaast (97), het laatste getal plus het aantal streepjes (72, bijvoorbeeld 502) of alleen het laatste getal. De motor heeft daar geen regel voor. De tekst zegt nu te veel of te weinig en legt uit hoe je de streepjes telt. Zie fixlijst #54.
3. **Rooster (E03, 10 items): geen sleutels van Claude.** De regels tellen de gekleurde hokjes (één te veel, te weinig). Een vorm die geen rechthoek is, valt op 'andere fout' («Is het een rechthoek: alle rijen even lang en recht onder elkaar?»). Zie fixlijst #55.
4. **Antwoorden '10.000' (E01 017 en 058, E04 003, E05 005).** De motor leest '10.000' niet als getal. Daar werken de regels × 10, : 10 en 'te veel/te weinig' niet; Claudes sleutels krijgen de neutrale tekst «Dat klopt niet. Eén … is duizend …». Typt een kind '10000' zonder punt, dan is de vraag of de app dat goed rekent. Zie fixlijst #52.
5. **'kilogram' of 'kilo'.** Ik schrijf overal 'kilogram' (ook «Een pak suiker weegt één kilogram»). Is 'kilo' voor groep 5 beter?
6. **G5-niveau.** Bij E01 #1 gaat het tot 41 m = 4100 cm, bij E01 #2 tot 10.000 cm = 100 m. Is dat G5?
7. **E01 #5 heeft maar 1 item** (voetbalveld). Zie fixlijst #56.
8. **Omtrek: 'zijde' (E02 #1) en 'kant' (E02 #2, het hek).** Bij de rechthoek staat 'zijde' in de opgave; bij het veld heb ik 'kant' gebruikt. Liever overal 'kant'?
