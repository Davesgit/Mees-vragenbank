## Twijfels en keuzes (batch 3), ter beoordeling door Didactiek
1. **Rooster (GET-M06): de fout-sleutels zijn een aantal hokjes.** Het antwoord is '7 rijen van 2 hokjes' en er zijn geen opties en geen Claude-fout-hints. Daarom gaan de regels over het aantal gekleurde hokjes: getal1 + getal2 betekent 'plus gedaan', getal1 of getal2 betekent 'nog niet genoeg hokjes'. Dat werkt pas als de app dat aantal doorgeeft (fixlijst #31). Tot die tijd krijgt het kind de tekst bij 'andere fout'. Hint 1 legt het keerteken (×) uit: eerst het aantal rijen, dan het aantal hokjes per rij. Dat is de afspraak 'eerst het aantal groepjes'.
2. **Kleuren in de vraag.** 'De rode strook' (MEET-E01) en 'de rode lijn' (MKU-E05) staan in de opgave. De hints zeggen alleen 'de strook' en 'de lijn' (fixlijst #28). Mijn checker telt nu alleen kleurnamen. Het werkwoord 'kleuren' telt niet meer mee, want dat is de opdracht bij GET-M06.
3. **GET-M05: de contexten (fixlijst #25) heb ik niet in de hints opgelost.** De hints noemen geen plek en geen ding. Ze zeggen 'Er gaan dingen weg' en 'Er komen dingen bij' (les G3), dus ze blijven kloppen als Overzicht de contexten vervangt.
4. **GET-M05: een andere uitleg per somtype.** Bij hele tientallen (#1, #2, #7): 'Spring in sprongen van tien. Het cijfer achteraan blijft hetzelfde.' Over het tiental (#3, #4): 'eerst tot het hele tiental, daarna de rest'. Zonder overgang (#5, #6): 'eerst de tientallen, daarna de eenheden'. De tekst van Claude 'Je gaat over het tiental heen' blijft alleen staan waar dat ook echt zo is (#3, #4).
   - Claudes 'Tel de tientallen nog eens: één tiental te veel eraf.' (#1) is nu 'Dat is één tiental te weinig.' 'Te veel' bij een antwoord dat te laag is, verwart.
   - Bij #4 is 'de kleinste van de grootste afhalen' (13 items, de sleutels verschillen per item) de tekst bij 'andere fout' geworden, in gewone woorden.
5. **MEET-E02 / E05 / MKU-E02 / E03 #2 / E04: Claudes teksten blijven per item.** Ze passen bij het voorwerp, dus ik heb alleen vervangen wat niet klopt: 'kilometer' (met '1000 m', boven 100, en een tijdsduur schatten; 'kwartier' zelf is wél G4, correctie 15:30), 'sprinten', 'nauwelijks', 'smaller dan een tafel' en 'kind uit groep 5' (taalfix).
   - Er ontbraken 3 fout-hints voor 'goed getal, verkeerde maat' (45 m, 25 m en 18 m). Die heb ik toegevoegd.
   - Hint 1 van MEET-E02 noemt geen maten, want 'een liniaal is dertig centimeter' en 'een deur is twee meter' zijn zelf antwoorden (005, 004).
   - De regels '45 m', '3 euro' enzovoort zijn letterlijke opties. apply_hints meldt ze als 'niet te lezen' in de items waar die optie niet staat. Dat is verwacht.
6. **MEET-E07: '3 euro' en '4 euro' zijn het aantal munten** (alle 7 items nagekeken). Die krijgen een eigen tekst: 'Je hebt de munten geteld …'. De hints gebruiken geen komma en geen 'teruggeven'.
7. **MKU-E05: de spiegellijn staat rechtop of ligt.** De teksten werken dus voor beide richtingen. Er staat niet 'links' of 'rechts', maar 'ga recht over de lijn, net zo ver'. Claudes 'Wat links staat komt rechts' en 'eentje naast' zijn vervangen.
8. **MKU-E01: Claudes 'hokjes omhoog'** klopt niet als de route naar beneden gaat. Ik heb het vervangen door 'naar boven of beneden'.
9. **MKU-E03 #1: 'systematisch' en 'boven, onder, dan de zijkanten'** passen niet bij een piramide. Het wordt 'Wijs elke platte kant maar één keer aan.' Ik noem geen ribben en geen hoekpunten.
10. **Niet aangeraakt:** GET-E08 #5 ('stappen' of 'sprongen') laat ik zoals het is, tot Didactiek en Overzicht beslissen.


## Ronde 3b (2026-10-01 15:30, Amsterdam): na review Didactiek batch 3 v1
6. **GET-M05 #4 'kleinste van de grootste':** de zin staat nu alleen bij die Claude-sleutels (eigen regel, per item, Claudes tekst). Een taalfix per item kan niet: als de tekst anders moet, moet het een vaste tekst worden.
7. **GET-M05 #3/#4 'één te weinig/te veel':** de tekst is vast en noemt geen getal meer. Per item een tiental invullen kan niet, want vul_in kent alleen uren.
8. **MEET-E02 '1 m' en '50 m'** zijn letterlijke regels. Ze vangen alleen items waar die optie staat. Bij '50 m' is dat pas na de rebuild van #35 (tot dan meldt apply_hints 'niet te lezen').
9. **MEET-E07:** de opties staan sinds de rebuild van 15:23 in €-notatie. Claudes teksten komen nu per denkfout en niet meer via een letterlijke regel. '€4' als letterlijke regel zou ook '€40' en '€45' vangen, maar die staan eerder per item. 005 heeft '€1 en 50 cent' naast '€2' en '€3': daar doen centen mee, dus dat is goed.
10. **MKU-E05 'letter/cijfer':** dit hangt af van de app (merge-punt #37). De alternatieve tekst staat klaar (`ALT_AAN` in `hints/patch_batch3b.py`).
