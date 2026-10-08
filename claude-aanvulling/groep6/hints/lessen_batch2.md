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

## Lessen 90–94 (Didactiek recheck-ronde5c, G6 ronde 5d/9) en 95–99 (recheck-ronde4d6b)
90. **Een guard test elke route die in de regel staat, en elk vakje van de tabel,** niet alleen de eerste route (#331: y1 + x2 en 'opgeteld' als goed vakje).
91. **Verandert de data de woorden of de volgorde van de opgave, dan gaan de hints in dezelfde ronde mee.** Beschrijf op waarde ('het grootste aantal', 'het kleinste aantal'), niet op volgorde ('eerste', 'tweede'), en leg de volgorde vast met een guard (#330).
92. **Bij 'X meer dan Y' mag het antwoord geen afleeswaarde uit de vraag zijn** (als X = 2 × Y is het antwoord de waarde van Y).
93. **Een build kan veranderen terwijl je naar hem kijkt.** Maak per build een snapshot, vergelijk de inhoud zonder `gegenereerdOp` en rapporteer op de laatste.
94. **Tel de sleutels per build opnieuw.** Een nieuwe invoervorm (een kaal '5' bij 'Typ een breuk') is een nieuwe sleutel; reken hem na zoals zijn broer (x/1).
95. **Een tekst die alleen 'in de entry' staat en niet in het item, bestaat voor de app niet.** Controleer altijd het item zelf (`hint2MetPlaatje` stond eerst alleen in `batch6.json`).
96. **Staat een fixlijstpunt in de code, controleer dan of de functie ook echt bij de items komt.** Tel het veld in de data (`niveau299`: eerst 0/400), niet de functie.
97. **Verandert een opgave, dan veranderen ook alle velden die van het oude antwoord afhangen** (`antwoordOokGoed`, 852). Controleer ze opnieuw tegen het nieuwe antwoord.
98. **Na een nieuwe regelvolgorde tel je per overlap welke soort wint,** en controleer je dat de winnende tekst ook klopt voor de andere formule die de sleutel heeft.
99. **Een FAIL uit een andere stroom (bordtitels, FIX6) noteer je met de oorzaak en de buildtijd.** Hij blokkeert de taalgate niet; kijk na de volgende build of hij weg is. Komen er tijdens een recheck meerdere builds, reken dan elke build opnieuw na.

*Lessen 100–104 (Didactiek, G5 ronde 7b) staan in `g5/hints/lessen_g5.md`; ze gelden voor alle groepen.*

## Lessen 110–114 (Didactiek gate ronde 9, deel A)
110. **Een letterlijke regel met een getal moet exact matchen.** Een match op een stukje tekst ('4 hokjes' in '14 hokjes') geeft een fout-hint die niet bij de waarde past. Test elke letterlijke regel tegen alle sleutels van het somtype (`g6work/r9oef/r9_letterlijk.py`).
111. **'Elk vakje' betekent elk vakje op de weg naar de vraag** (van 1 tot en met x2). Bij een verhouding als 1 : 2 is elk heel getal ergens een vakje; een guard over alle vakjes geeft dan alleen ruis.
112. **Gelijk verdeelde antwoorden zijn niet genoeg tegen raden.** Kijk ook naar de plek van het antwoord tussen de opties (kleinste, middelste, grootste).
113. **Een verbeterde fout-hint gaat pas live als H2 en laag 2 mee veranderen.** Anders spreekt laag 2 de nieuwe hint tegen (VBN #1: 'kleinste van grootste' tegen 'eerste van tweede').
114. **Tel de progressie ook bij oude somtypes opnieuw als er items bijkomen.** Een aanvulling met alleen basis en toepassen laat een somtype zonder kritisch niveau (les 48).

## Lessen 115–119 (Didactiek gate ronde 9, deel B)
115. **Valt één sleutel onder twee regels (± 1 én 'getal uit de vraag'), dan wint de benoemde denkfout.** Toets dat per sleutelwaarde over alle somtypes, niet per somtype (#390; `g6work/r9oef/r9_390.py` en `tools/bijna390_check.py`).
116. **Controleer een samenvoeging van somtypes op vier dingen:** het aantal items per oud nummer, de sleutels per item, of de teksten per byte gelijk zijn aan het doel-somtype, en of het oude nummer in de merge-metadata bewaard is (#235).
117. **Toets een niveauherindeling aan de geschreven regel** (#299), niet aan een eigen eerder voorstel.
118. **Een tekst over een stap die misschien niet bestond (onthouden/lenen, eindpunt van de getallenlijn) hoort een voorwaarde in de motor of de generator te krijgen.** Vraagvorm maakt de hint zachter, maar dan klopt hij nog niet voor het item (#392, #391).
119. **Draai je scripts van anderen op een snapshot, kopieer dan ook `tools/` en `bevroren/`, buig absolute paden om en zet bytecode uit** (`PYTHONDONTWRITEBYTECODE=1`, `python3 -B`); anders schrijven imports in de live map.

## Lessen 125–129 (Didactiek recheck ronde 9 deel A, build 11:21:56; in ronde 10b toegepast)
125. **Een aanvulling op een hoger niveau vraagt een nieuwe check van de hints.** Een hint die bij hele factoren klopt ('hoeveel keer zo groot'), leidt niet naar een route via een tussenvakje (VERH-E01 #1, gen-012/013/014, V-#410).
126. **Beschrijf twee waarden in een hint op grootte ('kleinste/grootste'), niet op volgorde ('eerste/tweede').** Leg in de data vast welke de grootste is (guard).
127. **Test een matcher met randgevallen** (getal in een groter getal, komma, breuk, minteken, €), en test de guard daarnaast. De guard moet even streng zijn als de matcher (`g6work/r10/r10b_410.py`, Z-#411).
128. **Een laag 2 'klaar voor later' (bij 0 sleutels) telt niet als gedaan.** Tel per regel hoeveel sleutels hem echt krijgen (les 47/65).
129. **Bij schatten kan afronden de verkeerde kant op toevallig het goede antwoord geven** (12 × 18 → 20 × 10). Test elke afrondcombinatie tegen het antwoord.

## Lessen 130–134 (Didactiek recheck ronde 9 deel B, build 11:32:19; in ronde 10c toegepast)
130. **Scan elke terugvaltekst op verwijswoorden, gewogen naar het aantal sleutels** (dan, daar, daarna, dat, die, zoveel, evenveel, ook, in de eerste zin). Werk niet uit je hoofd per somtype: de lijst van ronde 9 miste GET-E09 met 2049 sleutels (`g6work/r10/los_l2b.py`, G5–G7).
131. **Vergelijk 'getal uit de vraag' op waarde: n/n telt als 1, een kommagetal als zijn waarde.** Wie alleen hele getallen of tekst vergelijkt, mist precies de eindpunten (D-#416).
132. **Een aangepaste check toetst de verplichte soort, niet 'alles behalve X'.** Anders gaat een terugval naar 'andere fout' stil door de check (FIX6 #203; ook `b5d/check.py` #22 toetst nu de eis, niet één oude tekst).
133. **Controleer de scope aan de data**, met een diff van items en ids, voordat je zegt wat er (nog niet) in een build zit (hm/dl stond al in 11:21:56).
134. **Zet je een benoemde regel vóór andere regels, draai dan ook de checks die de verdrongen regel eisen** (eindpunt vóór 'een stuk ernaast' → #169 moest mee; 'getal uit de vraag' vóór ±1 → de ±1-checks).

## Lessen 135–140 (Didactiek slotcheck ronde 10, G5 11:38:45 en G6 11:39:38)
135. **De los-scan vangt ook "die"/"dat" + een zelfstandig naamwoord dat in dezelfde tekst nog niet genoemd is** ("die rij", "dat getal", "die stap", "die groepjes"), en volgordewoorden als "tot slot". Lees elke terugval-H2 en vraag: wat doet een kind met alleen deze zin?
136. **Toets welke regel een sleutel krijgt door de motor na te spelen over alle sleutels** (eerste passende regel = regel van de sleutel), niet alleen over de sleutels waarvan je weet dat ze verschoven zijn.
137. **Elk label dat zegt dat een waarde bestaat ("andere staaf", "andere rij", "andere cel") krijgt een feitenguard**, niet alleen het label waar de fout gevonden werd.
138. **Een nieuwe zin in een bestaande fout-hint gaat langs de oude lessen van dat onderwerp.** #410 bracht de bewering terug die #272/les 62 eruit had gehaald ("met keer en delen"); een check op die bewering maakt zo een terugval zichtbaar.
139. **Een zin die maar bij een deel van de items past ("Is dat geen heel getal?"), mag de stap voor de andere items niet wegduwen.** Controleer per itemgroep of laag 1 nog een volledige volgende stap geeft.
140. **Een guard leest getallen precies zoals de vergelijking die hij bewaakt** (breuk, komma, punt-duizendtal, €, minteken met en zonder spatie, eenheid met ²). Te streng geeft een vals stopsein, te soepel een vals "goed".

## Lessen 150–155 (Didactiek eindcheck ronde 11, G5 build 11:54:17 en G6 build 11:52:44; in ronde 11 toegepast)
150. **Een guard die een vorm overslaat (bedragen, breuken), meldt dat als "niet gecontroleerd" in plaats van stil 0 te geven.** BIJNA390 gaf 0 omdat `waarde416` bij een € `None` gaf; drie G5-sleutels met «Bijna!» op een bedrag uit de vraag bleven zo onzichtbaar (#530).
151. **Een scan die per tekst telt, noemt elk somtype waarin die tekst staat.** «Tel tot slot de ribben …» stond bij MKU-E02 #2 én #3; de slotcheck noemde alleen het eerste (#531). Zoek een te vervangen zin daarom altijd met `rg` over alle `batchN.json` van G5–G7.
152. **Een voorwaarde voor onthouden telt de één die binnenkomt mee.** Toets op kolommen die pas mét die één op tien komen (tientallen 9 + 1: G6 E04 069 en 078, #532).
153. **Test een check door de foute zin terug te zetten in een kopie**, en zet die mutatietest in de gedeelde checks (`g6work/r11/r11_check.py`): vangt de check de oude zin niet, dan beschermt hij niets.
154. **Een guard die dezelfde functie gebruikt als wat hij bewaakt, beschermt niets.** Leg het gedrag vast in een vaste testtabel met verwachte uitkomsten (r11_check.py: `lett_guard` en `in_vraag390`, met €, breuk, minteken, punt-duizendtal).
155. **Een laag 2 heeft geen halve vergelijking: noem de grootheid zelf.** «net zoveel keer als de noemer» (de helft staat in H1) → «Hoeveel keer zo groot is de nieuwe noemer? Doe de teller ook zoveel keer.»; «met dit aantal» → «met het aantal hokjes uit de vraag» (#541, #533).
