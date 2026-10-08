# Lessen voor G6 batch 2 (bewerkingen) en verder, uit Didactiek v1 batch 1 (1 okt 20:15). Genoteerd door Oefeningen, 20:27; les 12 gecorrigeerd en 13–15 toegevoegd om 20:53 (recheck Didactiek 20:50).

1. **Elke bewering in een fout-hint is per sleutel waar.** Per item narekenen met een script. Vangt een regel twee oorzaken, dan een vraag («Is dat het goede …?»). Bestaat de precieze regel, dan die eerst; één richting per entry (getal2 + 1 bij 'meer').
2. **Geen 'het dichtst bij' als er een midden kan zijn** (x5, x50, x500 bij schatten/afronden): geef de regel («Kijk naar het cijfer van de …»).
3. **Sjablonen breken niet bij nullen en lengtes:** lenen/inwisselen over meerdere nullen (3.004.050 − 1.236) als vraag ('Is dat cijfer ook een nul?'); een 0 in een splitsing (geen 'de tientallen' als die er niet zijn); deling met rest 0 ('Blijft er iets over?'); 'het cijfer vooraan', geen vaste plek.
4. **Een feit alleen als het in elk item waar is.** Anders een vraag met voorwaarde ('Staat daar een nul? Dan …').
5. **Notatie:** '×' en ':' als deelteken; ':' als leesteken alleen vóór een zin, nooit vóór een getal; geen 'a : b' (verhouding, G7); '−', nooit '-'; 4 cijfers zonder punt, vanaf 5 cijfers met punt, sleutels vanaf 5 cijfers in beide vormen; kommagetallen met komma en zonder slot-nullen (VORM #105); ketensommen voluit; geen machten.
6. **Een voorbeeld in een hint is nooit een antwoord van een item in dat somtype en zit er ook niet in.** Als tekst controleren ('0,25' tegen 0,2) of weglaten. Neutraal mag (68 cm). Let op: check_hints geeft WARN op elk getal in een hint; een drempel 'meer dan 1' en een neutraal voorbeeld ('Zo is …') zijn sinds #157 INFO.
7. **Cijfer of woord:** '5 of meer', 'het cijfer 7' in cijfers; aantallen in lopende tekst ('twee keer', 'drie nullen') en 'een negen/nul' als naam in woorden.
8. **Een term krijgt de eerste keer een korte uitleg** (product, quotiënt, rest, kolomsgewijs, inwisselen/lenen, schatten, 'keer zo veel'). Geen woorden met twee betekenissen in één batch ('teller', 'deel', 'rest', 'verschil'). Geen aanhalingstekens om een woord («Meer dan betekent …»).
9. **'Bijna!' alleen bij één stap ernaast** (± 1, ± 10, ± 0,1); bij 'te veel/te weinig' klopt de richting met de sleutel.
10. **Een algemene regel wint nooit van een precieze.** Volgorde: exacte bewerkingsfouten (verkeerde bewerking, getal2 ± 1, een plek ernaast, nul vergeten bij × 10/100) → ± 1 stap → te ver → andere fout. Claude-sleutels alleen als er geen motorregel is.
11. **Kleur nooit als enige aanwijzing.** Geen optieletters in hints. Geen Engels.
12. **Niveau groep 6 (gecorrigeerd, Didactiek 20:50, #158):** hele getallen **tot 100.000**; wat daarboven ligt, hoort bij G7 (`regels_g6.py`). Geen ouderzin of hint boven die grens, en een ouderzin nooit aanpassen aan data die erboven ligt (dan een niveaupunt voor Overzicht). Binnen G6 ook vermenigvuldigen met een getal van twee cijfers en delen met rest. ~~tot 1.000.000~~ (fout in v1, #156e ingetrokken).
13. **Een vervanggetal blijft binnen de niveaugrens en het bereik van het somtype.** Na elke fix die een getal vervangt opnieuw tegen de grenzen controleren (`regels_g6`). De ouderzin nooit aan de data aanpassen als die data buiten de grens valt.
14. **De context past bij het aantal:** duizenden bezoekers, kaartjes of stappen kan, 6699 eieren in een nest niet. Een vakwoord van dit niveau ('teller', 'noemer', 'product', 'rest') niet als gewoon woord gebruiken, tenzij de zin het meteen uitlegt: het apparaat heet geen 'teller' (in G6 is dat het breukwoord). Nieuwe prompts (M02 #4) zijn data voor Overzicht (#160). **Aanvulling (Didactiek ronde 1c, 21:35):** het losse woord 'teller' nooit als naam voor een apparaat; een samenstelling ('stappenteller') mag wel.
15. **Middengetallen alleen in 'rond af op'**, met de regel '5 of meer' in elke tekst; minstens één per somtype, verder met mate. 'Het dichtst bij' alleen als er geen midden kan zijn. Een schathint ('rond allebei af') past niet bij compenseren: daar maak je één getal rond en is het antwoord exact (#161).
16. **Een label van Claude zegt niet wat de fout is: reken de waarde van elke sleutel na** (Didactiek batch 2, 21:35). 'deel-vergeten' was bij 37 van de 82 sleutels in E06 #1 'cijfers opgeteld' (#190). In breuken: 'teller-en-noemer-optellen' per sleutel narekenen.
17. **'Met de tafel' / 'uit de tafels' alleen als het getal in elk item in de tafel staat** (tot tien keer het groepje). Anders een stap geven («Is het getal te groot voor de tafel? Haal er dan steeds tien groepjes af.», #191). Bij gelijknamig maken en vereenvoudigen ook per item narekenen.
18. **Opgaven gaan ook door een spellingscheck**, niet alleen de hints (evenveel, gelijknamig, één, ieder; #192). Vaste woordenlijst breuken: teller, noemer, breukstreep, gelijknamig, vereenvoudigen, helen.
19. **'Teller', 'noemer' en 'deel' zijn in breuken vakwoorden** (besluit Didactiek 21:32, #175: het blijft 'stuk'). Leg 'teller' en 'noemer' de eerste keer uit ('het getal boven de streep'). Een gelijk deel van het geheel heet in kindteksten een **stuk**; schrijf 'gelijke stukken' waar het ertoe doet dat ze even groot zijn. 'Deel' alleen in vaste vormen («Welk deel van … is …?», «een vierde deel»), en daar bij het eerste gebruik uitleggen: 'een deel = een of meer gelijke stukken van het geheel'. 'Deel' nooit voor de deling (les 8). 'Overblijven' alleen voor wat overblijft (de rest), niet voor 'wat je dan hebt'.
20. **'Dat getal staat al in de vraag' is geen reden waarom iets fout is.** Het goede antwoord kan ook in de vraag staan (E08 bij 7 van de 12 items; gelijkwaardige breuken). Zeg wat het kind deed en hoe het wel moet («Je hebt een van de getallen uit de vraag genomen. …»).
21. **Een strategiehint geeft de hele stap.** Bij lenen ook 'jouw cijfer krijgt er tien bij'; bij breuken bij 'maak de noemers gelijk' ook wat er met de teller gebeurt.

Werkwijze uit ronde 1b: na een fixlijst van Overzicht eerst `scripts/fixlijst_g6.py` lezen (entry-aanpassingen in het geheugen) en die in de patch overnemen, zodat `logs/fixlijst_g6_hints.json` leeg blijft.
22. **Niveau toetsen op het werk, niet op het label** (Didactiek batch 3, 21:40): reken uit welke tussenstap het kind moet maken (bv. de gemeenschappelijke noemer) en vergelijk dat met G6. 'Noemer tot 20' kan toch een kgv van 336 geven (#180).
23. **'Getal uit de vraag': het antwoord hoort nooit in `waarden`.** Kan het antwoord in de vraag staan (antwoord = noemer, teller of geheel), schrijf de tekst dan als vraag («Je hebt een getal uit de vraag overgenomen. Is dat echt …?», #182).
24. **Een benoemde denkfout gaat vóór ± 1:** 'Bijna!' mag geen optel- of aftrekfout overstemmen die toevallig op één ernaast uitkomt (#181). Ook bij oppervlakte: de omtrek kan samenvallen met 'één rij te veel/te weinig' (4 × 2, 3 × 9).
25. **Een uitspraak in de opgave over aantallen** ('er blijft een stuk over') moet per item kloppen, ook in het enkelvoud of meervoud (#183).
26. **Een foute optie moet zonder twijfel fout zijn**, ook vanuit een ander vakgebied (breuk = deling: 'het deeltal' is verdedigbaar, #173).
27. **Vaktermen met hun plek uitleggen:** 'de teller (boven de streep)', 'de noemer (onder de streep)'. Alleen de functie uitleggen zegt nog niet welk getal bedoeld is (#184, #200).
28. **Na een rebuild met nieuwe opgaven alle controles opnieuw draaien**, ook de regex-sjablonen (E03 #6 ging van «… is evenveel als ?/8» naar «3/4 = ?/8»).
29. **Een motorregel kan samenvallen met een goede tussenstap** (Didactiek recheck 2b, 21:40). Kijk bij elke regel of de waarde ook een deel van de goede route is: een los deelproduct, de som van een paar deelproducten, het eerste getal × het ronde stuk (33 × 19 → 330, #196), de breuk na gelijknamig maken of vóór vereenvoudigen. Zo ja, dan krijgt die waarde de neutrale vraagtekst en geen tekst die zegt welke fout het was. Bij omrekenen in stappen van tien is 'één stap te weinig' ook een tussenstap (km → m: keer honderd), dus een vraag («Heb je helemaal omgerekend naar meter?», ronde 4a).
30. **Spellings- en regressiechecks over álle tekstvelden**, ook de ouderzin, H1, H2, ALG en de fout-hints. 'even veel' is een verboden patroon (#197; in b2–b4/check.py en `tools/evenveel_check.py`).

## Lessen 31–36 (Didactiek batch 4, 22:09; in ronde 4b en batch 5 toegepast)
31. **Een tussenstap herken je ook aan het verschil:** is antwoord − waarde precies één vergeten stap (één stuk, één rij, één deelproduct), dan is de waarde een tussenstap: een vraag, geen foutnaam.
32. **Kijk per item of een foute route toch op het goede antwoord uitkomt** (omtrek = oppervlakte bij 6 × 3, #211). Bij verhoudingen vooral optellen in plaats van vermenigvuldigen (2 : 4 = 3 : ? geeft 6 met keer en 5 met erbij). Zet daar een bewaker op.
33. **'Bijna!' alleen bij één vergissing in de laatste stap, en alleen als die stap klein is ten opzichte van het antwoord** (vuistregel ≤ 10 %). + 1 kg bij 6,59 kg is geen 'Bijna!' (#213); ± 1 bij een antwoord onder de tien ook niet (#216). Eén rij ernaast in een verhoudingstabel is geen 'Bijna!'.
34. **Noem hetzelfde stuk met dezelfde woorden als de hint** ('een rij zo lang als de lengte/breedte', #212). 'Rij' en 'kolom' van de verhoudingstabel zijn vakwoorden: één keer uitleggen, daarna steeds zo. Geen 'kolom' waar 'kolom' al de cijferkolom is.
35. **Staat een getal uit de vraag ook op ± 1, dan gaat de benoemde fout eerst, zonder 'Bijna!'** (de zijde die je al weet, #214).
36. **Een verzamelsleutel van Claude kan één vaste fout verbergen:** groepeer de waarden. Volgen ze allemaal hetzelfde patroon (het aantal nullen als factor, 167 van de 167, #215), geef ze een eigen tekst of vraag een motorregel.

## Lessen 41–48 (Didactiek recheck 3b, 22:09; 37–40 gebruikt Didactiek niet)
37. **De context past bij de maat:** koppel de keuze van een context aan een maatbereik (Didactiek, via Dave 22:44).
38. **De bordtitel dekt elk somtype,** met de eenheid en de woorden uit de hints.
39. **Laat geen regel in de data staan die niets raakt of geen tekst heeft.**
40. **Laag 2 voegt een stap toe en herhaalt laag 1 niet** (tekstSterker, #229).
41. **Gebruik de oorspronkelijke somtypenummers** (`nrOrigineel`) in reviews en checks: na parkeren schuiven de nummers (E03 #2 is nu 'met noemer').
42. **Elke strategie heeft tussenstappen; reken ze allemaal na:** de factor (E03 #6), één stuk en een paar stukken (E09), steeds één hele eraf en de rest (M04 #2). Nooit 'Bijna!' of een foutnaam op een tussenstap.
43. **'Getal uit de vraag' komt ná de regels voor tussenstappen:** één stuk of de factor kan gelijk zijn aan de teller of de noemer (#205, #206).
44. **Twee noemers in de vraag: 'de noemer uit de vraag' is onduidelijk.** Gebruik de woorden van H1 ('de oude noemer', 'de nieuwe noemer', #208).
45. **Een regel voor gelijkwaardige breuken vangt ook de breuk uit de vraag zelf (k = 1):** de tekst moet ook dan kloppen ('nog niet de nieuwe noemer').
46. **Leg 'duidelijk meer of minder dan de helft' vast in een getal** en geef het kind een toets met hele getallen: de teller keer twee tegenover de noemer (#222).
47. **Controleer een filter van de motor in de data zelf** (`foutRegels.match.waarden`), niet in het commentaar.
48. **Tel na een selectie de progressie per somtype:** aantal items, niveau, soort vergelijking en de plek van het antwoord (#221).
49. **Schrijft een hint over 'aan die kant', tel dan per item hoeveel breuken er aan die kant liggen** (0, 1, 2 of 3), en of er een precies de helft is. De tekst moet bij elke situatie die voorkomt kloppen (#250).
50. **Het niveau volgt de zwaarste route die het kind echt moet nemen,** niet het label van de bron. Maak een kruistabel van niveau × route (#251).
51. **Zegt de hint 'vergelijk twee aan twee', dan tellen ook de paren zonder het antwoord mee.** Elk paar dat het kind kan kiezen moet binnen de grens liggen, of de hint zegt met welk paar je begint (#254).
52. **Leg de nummerreeks vlak voor het schrijven nog eens naast de fixlijst.**
53. **Bij een verplaatst item ook de kindvelden controleren** (hint, sterkereHint, ouderzin); dat doelId en somtype kloppen, zegt niets over de hints (#253).
54. **Breid het sleutelscript uit met de nieuwe regelsoorten vóórdat je het draait,** anders lijken nieuwe soorten fout of vallen ze stil weg.
60. **Reken een afleesinstructie na met een echt voorbeeld uit de data.** 'Tel de streepjes ertussen' geeft er één te weinig (paaltjes); tel tot en met het streepje bij het volgende getal (#270, `jsRender`: 0 → 25 is 5 streepjes van 5).
61. **Vraag 'Ben je al bij het vakje?' alleen als de waarde echt een vakje van de tabel is.** Reken per sleutel na of het 'hetzelfde erbij' is (y1 + (x2 − x1)) of het andere getal erbij (y1 + x2): dat is de optelfout, met een eigen regel (#271).
62. **Een regel die iets verbiedt, moet in dat vak ook kloppen.** In een verhoudingstabel mag je kolommen optellen; fout is alleen bij het andere getal hetzelfde erbij doen (#272).
63. **Een woordvervanger vervangt het woord op elke plek in de zin.** Het ding in 'Welk deel van een X' is het enkelvoud van wat er verdeeld wordt, en je moet het ook echt kunnen verdelen (#228, #278).
64. **Kijk naar het patroon van gegenereerde data:** de verschillen tussen buurwaarden, de as en de plek van het antwoord. Een vaste stap (altijd twee streepjes) maakt de som te raden (#276).
65. **Een regel in de entry is nog geen sleutel.** Tel per regel hoeveel sleutels hem echt krijgen (les 47); een regel met 0 sleutels terwijl er sleutels met precies die waarde zijn, wijst op een gat (#274).
66. **'Wit' en 'gekleurd' zijn ook kleurwoorden.** Kijk of er een plaatje is (`visual.nodig`) voordat een hint naar het uiterlijk van iets verwijst (#273).
67. **Een terugvallaag moet je los kunnen lezen.** Geen 'die', 'dan' of 'dat' die naar een vorige hint verwijzen, en hij moet bij de fout passen: aflezen bij een afleesfout, rekenen bij een rekenfout (#283).
70. **Bij vakcodes is een 'omgedraaide' afleider een geldig ander, gespiegeld vak** (G2 → B7), geen verkeerde schrijfvolgorde. De fout-hint gaat over de randen, niet over de volgorde (#293).
71. **Speel een ruimtelijke instructie letterlijk na op het rooster.** Vanaf het cijfer kom je onder de letter uit, nooit bij de letter (#292).
72. **Liggen de sleutels boven en onder het antwoord, dan kiest laag 2 van een algemene 'tel nog eens' geen richting.** Tel de sleutels per richting (#294).
73. **Leid de motorregels af uit de families van de bronsleutels:** welke formule geeft elke sleutel? Een regel zonder eigen sleutels is een spookregel, een familie zonder regel een gat (#296: A + aantal torens, 179 sleutels).
74. **Bij overlap gaat de exacte formule voor de brede** (het aantal torens vóór 'antwoord min een torenhoogte'). De andere afleider in het item laat zien welke familie de bron bedoelde (#296c).
75. **Toont een hint een eigen plaatje (`hint2Plaatje`), dan noemt de hinttekst dat plaatje en legt het uit** (#295).
76. **Regels die 'klaar voor de motor' staan, krijgen meteen ook laag 2,** anders valt laag 2 terug op H2 zodra de motor ze leest.
77. **Een uitzondering in een hinttekst (geen ½-zin bij kleinst) leg je vast met een assert in de selectie,** anders breekt de tekst stil als de selectie verandert (recheck 3d/4c).
78. **Is laag 1 herschreven nadat laag 2 werd voorgesteld, controleer laag 2 dan opnieuw op herhaling** (#291).
79. **Gebruik geen woord met twee betekenissen in de bank (kolom = cijferkolom) als een omschrijving net zo helder is** ('de rand met de letters', 'onder de letter', 'naast het cijfer').

*Lessen 80–89 (Didactiek, G5 batch 7) staan in `g5/hints/lessen_g5.md`; ze gelden voor alle groepen.*
