#!/usr/bin/env python3
"""Schrijft hints/batch7.json (G8 batch 7: VBN-E04 #6–#31 = 26 somtypes, elk één meerkeuze-item met tekstopties: misleidende grafieken
(assen, plaatjes, schuine of brede tekening, weggelaten gegevens), aflezen (keer duizend, tussen twee getallen, verschil, plaatjesgrafiek),
percentages (cirkeldiagram, klassen die niet even groot zijn, twee staven samen) en onderzoek (te weinig gevraagd, samen stijgen).
8 okt 2026 (17:1x), Oefeningen. Formaat als make_batch7.py. Data: live g8 (build 17:03:20). Lessen: hints/lessen_g8.md t/m les 334.
Analyse en checks: /workspace/g8work/b7/check.py op de zandbak /workspace/g8work/b7/sbx.sh (verse kopie van live).
Keuzes:
- Per foute optie een letterlijke regel met de hele optietekst (G8-2); de tekst klopt voor die optie en noemt het goede antwoord niet.
- #29–#31 delen hun teksten (zelfde vraag als b6 VBN-E04 #34; 'Ja'/'Nee' wisselt per item): neutrale L1 'tel op en vergelijk met vijftig procent'.
- Geen cijfers, geen woorden van de [..]-plekken (les 147), geen plekwoorden (les 193), geen optieletters ('klas A'), geen 'even veel' (#192),
  verklaptoets meerkeuze (les 260/264, Z-#824/les 288).
Na een sync nooit --force: correcties via hints/patch_batch7.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B7_OUT', f'{BASE}/hints/batch7.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch7.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch7.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch7.json bestaat al: patch in place (hints/patch_batch7.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
L = R   # letterlijke regel: 'regel' is de hele tekst van de foute optie
def CL(soort, label, tekst, sterker):
    """labelregel: Claudes sleutels met dit claudeDenkfout-label (geen motorregel die ze pakt, Oef-#490); vaste tekst zonder getallen, per sleutel nagerekend"""
    f = T(soort, f'Claudes sleutel: {label}', tekst, None, 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt (Oef-#490/#494); vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', label)
    f['tekstSterker'] = sterker; return f
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
def LT(soort, optie, tekst, sterker):
    """letterlijke regel: de hele tekst van de foute optie (G8-2)"""
    return R(soort, optie, tekst, sterker)
E04 = "G8-VBN-E04"
def ST(nr, h1, h2, oz, fh):
    E.append((E04, nr, h1, h2, oz, fh))

# #6 (001): as met ongelijke stappen
L2 = 'Op een eerlijke as staan de getallen op gelijke afstand, en komt er telkens evenveel bij. Anders lees je de grafiek verkeerd.'
ST(6, 'Kijk hoe groot de sprong is van het ene getal naar het volgende.',
  'Reken bij elk paar getallen naast elkaar uit hoeveel erbij komt. Op papier is de afstand overal even groot. Komt er dan ook overal evenveel bij?',
  'Je kind ontdekt dat een grafiek misleidt als de getallen bij de as niet in gelijke sprongen oplopen.',
  [LT('eindgetal', 'De as moet altijd bij 100 eindigen.', 'Een as mag bij elk getal ophouden. Kijk naar wat er tussen de getallen gebeurt: komt er overal evenveel bij?', L2),
   LT('te veel getallen', 'Er staan te veel getallen bij de as.', 'Het aantal getallen is geen probleem. Kijk hoeveel er telkens bij komt van het ene getal naar het volgende.', L2),
   ALG('Kijk hoeveel er telkens bij komt van het ene getal naar het volgende. Is dat overal evenveel?', L2)])

# #7 (002): as 'x 1000'
L2 = 'Het getal bij de as is niet het echte aantal. Het tekstje bij de as zegt met hoeveel je het moet nemen: keer duizend.'
ST(7, 'Lees het tekstje bij de as: wat betekent het stukje tussen haakjes?',
  'Bij de as staat dat elk getal keer duizend gaat. Doe het getal waar de staaf stopt keer duizend.',
  'Je kind leest een grafiek waarbij de getallen op de as keer duizend gaan.',
  [LT('getal van de as', '4 bezoekers', 'Dat is alleen het getal bij de as. Lees het tekstje bij de as nog eens: keer hoeveel gaat elk getal?', L2),
   LT('keer honderd', '400 bezoekers', 'Dat is keer honderd. Lees nog eens wat er bij de as staat: keer hoeveel?', L2),
   ALG('Lees het tekstje bij de as. Doe het getal waar de staaf stopt keer het getal tussen haakjes.', L2)])

# #8 (003): tussen twee getallen aflezen
L2 = 'Zoek de twee getallen op de as waar de staaf tussen stopt. Het aantal ligt tussen die twee. Stopt hij halverwege, neem dan ongeveer het midden.'
ST(8, 'Tussen welke twee getallen stopt de staaf? Daar zit het aantal tussen.',
  'De staaf stopt halverwege twee getallen op de as. Zoek wat er ongeveer in het midden ligt. Precies aflezen kan niet, dus je schat.',
  'Je kind schat een waarde die tussen twee getallen op de as ligt.',
  [LT('stukje erboven', 'Ongeveer 2 of 3', 'Zo groot is alleen het stukje boven het lagere getal. De staaf begint bij nul: hoe ver komt hij in totaal?', L2),
   LT('opgeteld', 'Precies 25', 'Dat zijn de twee getallen samen. De staaf stopt tussen die twee getallen in, dus het aantal ligt daartussen.', L2),
   ALG('Zoek de twee getallen waar de staaf tussen stopt, en schat wat er in het midden ligt.', L2)])

# #9 (004): kop 'verdubbeld'
L2 = 'Verdubbelen is keer twee. De kop klopt alleen als het nieuwe getal twee keer het oude is. Reken het na met de getallen.'
ST(9, 'Verdubbeld betekent: twee keer zoveel. Hoeveel is twee keer het getal aan het begin?',
  'Reken uit wat er zou staan als het aantal echt twee keer zo groot was. Vergelijk dat met het getal waar de staaf nu stopt. Is het hetzelfde?',
  'Je kind controleert met de getallen of een kop boven een grafiek klopt.',
  [LT('staaf lijkt hoger', 'Ja, de staaf is twee keer zo hoog.', 'Kijk niet naar hoe hoog de staaf lijkt, maar naar de getallen. Is het nieuwe getal twee keer zo groot als het oude?', L2),
   LT('een paar erbij', 'Ja, er zijn 4 bezoekers bij gekomen.', 'Er komen er wel een paar bij, maar verdubbelen is meer: twee keer zoveel. Is dat hier zo?', L2),
   ALG('Reken uit hoeveel twee keer het oude getal is, en vergelijk dat met het nieuwe getal.', L2)])

# #10 (005): flesje twee keer zo hoog en breed
L2 = 'Twee keer zo hoog en twee keer zo breed: dan past het oude plaatje twee keer twee keer in het nieuwe. Zo lijkt de verkoop veel meer gegroeid dan hij is.'
ST(10, 'Het plaatje is hoger én breder geworden. Wat gebeurt er dan met de ruimte die het inneemt?',
  'Stel je het oude flesje voor als een rechthoek. Maak hem twee keer zo hoog en twee keer zo breed. Hoe vaak past het oude flesje dan in het nieuwe?',
  'Je kind ziet dat een plaatje dat in hoogte én breedte groeit, groter lijkt dan het aantal.',
  [LT('alleen de hoogte', 'Niets, twee keer zo hoog is precies goed.', 'Het flesje is niet alleen hoger, maar ook breder getekend. Kijk naar hoe groot het hele plaatje lijkt.', L2),
   LT('als een doos', 'Het flesje lijkt acht keer zo groot.', 'Een plaatje is plat: het heeft alleen een hoogte en een breedte. Hoe vaak past het oude plaatje in het nieuwe?', L2),
   ALG('Hoe vaak past het oude plaatje in het nieuwe, als het twee keer zo hoog en twee keer zo breed is?', L2)])

# #11 (006): schuin cirkeldiagram
L2 = 'Een schuin getekend cirkeldiagram vertekent: wat dichterbij is, lijkt groter. De percentages blijven hetzelfde.'
ST(11, 'Wat zeggen de percentages bij de twee stukken? En wat zie je met je ogen?',
  'Door de schuine tekening komt een stuk dichterbij. Wat dichterbij is, ziet er breder uit. Vertrouw op de getallen bij de stukken, niet op hoe groot ze eruitzien.',
  'Je kind ziet dat een schuin getekend cirkeldiagram de stukken anders laat lijken dan ze zijn.',
  [LT('echt groter', 'Het voorste stuk is echt groter dan 25%.', 'Bij de stukken staan percentages. Wat zeggen die getallen: is het ene stuk echt groter dan het andere?', L2),
   LT('kleuren', 'Een cirkeldiagram mag geen kleuren hebben.', 'Kleuren helpen juist bij het lezen. Het gaat hier om de schuine tekening.', L2),
   ALG('Kijk naar de percentages bij de stukken, en vergelijk dat met wat je ziet.', L2)])

# #12 (007): geen getallen bij de as
L2 = 'Getallen bij de as vertellen hoe groot elke staaf is. Zonder getallen zie je alleen welke hoger is, niet hoeveel.'
ST(12, 'Wat kun je zonder getallen nog wel zien, en wat niet?',
  'Zonder getallen bij de as zie je nog steeds welke staaf het hoogst is. Maar wat kun je dan niet aflezen?',
  'Je kind ziet dat je zonder getallen bij de as geen aantallen kunt aflezen.',
  [LT('kleuren', 'Je kunt de kleuren niet meer uit elkaar houden.', 'Met de kleuren is niets mis. Het gaat om wat er bij de as hoort te staan.', L2),
   LT('welke hoger', 'Je ziet niet welke staaf hoger is.', 'Welke staaf hoger is, zie je juist wel. Maar kun je ook zeggen hoeveel elke staaf is?', L2),
   ALG('Wat staat er normaal bij de as? Wat weet je niet als dat er niet bij staat?', L2)])

# #13 (008): samen stijgen is geen oorzaak
L2 = 'Als twee dingen tegelijk stijgen, kan er iets anders achter zitten dat ze allebei laat stijgen. Uit een grafiek haal je niet zomaar een oorzaak.'
ST(13, 'Gaan twee dingen samen omhoog, dan hoeft het ene niet door het andere te komen.',
  'Wanneer stijgen beide lijnen? Bedenk wat er in die maanden anders is. Kan dat voor beide de reden zijn?',
  'Je kind leert dat twee lijnen die samen stijgen niet betekenen dat het ene door het andere komt.',
  [LT('dalen', 'Nee, want de lijnen dalen juist samen.', 'Lees nog eens wat er in de warme maanden met de lijnen gebeurt: gaan ze omhoog of omlaag?', L2),
   LT('samen stijgen', 'Ja, want beide lijnen stijgen samen.', 'Twee lijnen die samen stijgen, hoeven niet door elkaar te komen. Wat hebben ze met elkaar gemeen?', L2),
   ALG('Wat is er anders in de maanden waarin beide lijnen stijgen?', L2)])

# #14 (009): alleen de beste maanden
L2 = 'Wie alleen de beste maanden laat zien, laat de verkoop beter lijken dan hij het hele jaar was. Een eerlijke grafiek toont alle maanden.'
ST(14, 'Een jaar heeft twaalf maanden. Welke maanden laat de winkel zien?',
  'De winkel kiest zelf welke maanden in de grafiek komen. Wat gebeurt er met je beeld van het hele jaar als je alleen de beste maanden ziet?',
  'Je kind ziet dat een grafiek misleidt als er gegevens weggelaten zijn.',
  [LT('getallen fout', 'De getallen bij die maanden kloppen niet.', 'De getallen zelf zijn goed gemeten. Denk aan de maanden die er niet bij staan.', L2),
   LT('drie staven', 'Drie staven zijn te weinig om te tekenen.', 'Drie staven mag best. Het gaat erom welke maanden er weggelaten zijn.', L2),
   ALG('Welke maanden staan er niet in de grafiek, en wat betekent dat?', L2)])

# #15 (010): cirkeldiagram samen meer dan honderd
L2 = 'Alle stukken bij elkaar zijn de hele cirkel: honderd procent. Komt het samen op meer uit, dan kan het diagram niet kloppen.'
ST(15, 'Alle stukken van een cirkeldiagram vormen bij elkaar de hele cirkel. Hoeveel procent is dat?',
  'Een hele cirkel is honderd procent. Tel de percentages van de stukken bij elkaar op. Wat valt je op?',
  'Je kind controleert of de stukken van een cirkeldiagram samen honderd procent zijn.',
  [LT('grootste stuk', 'Het grootste stuk moet 100% zijn.', 'Eén stuk is altijd een deel van de cirkel. Hoeveel procent moeten alle stukken bij elkaar zijn?', L2),
   LT('te weinig stukken', 'Er zijn te weinig stukken getekend.', 'Het aantal stukken is geen probleem. Tel de percentages eens bij elkaar op.', L2),
   ALG('Tel de percentages bij elkaar op. Hoeveel procent hoort een hele cirkel te zijn?', L2)])

# #16 (011): omgekeerde as
L2 = 'Bij deze grafiek staan de getallen omgekeerd. Een lijn die omlaag gaat, gaat hier naar de grotere getallen.'
ST(16, 'Kijk eerst welke getallen onderaan en bovenaan de as staan.',
  'Hier staan de hoge getallen onderaan en de lage bovenaan. Loopt de lijn omlaag, naar welke getallen gaat hij dan?',
  'Je kind leest een grafiek waarbij de getallen op de as omgekeerd staan.',
  [LT('omlaag is minder', 'Het aantal wordt steeds kleiner.', 'Meestal betekent omlaag: minder. Maar lees hier eerst de getallen bij de as. Waar staan de hoge getallen?', L2),
   LT('gelijk', 'Het aantal blijft de hele tijd gelijk.', 'De lijn loopt niet recht, dus het aantal verandert. Kijk naar welke getallen de lijn gaat.', L2),
   ALG('Lees eerst de getallen bij de as. Naar welke getallen loopt de lijn?', L2)])

# #17 (012): verschil tussen twee staven
L2 = 'Het verschil reken je uit door het kleine getal van het grote af te halen, of door te tellen van het kleine naar het grote.'
ST(17, 'Hoeveel meer: dan zoek je het verschil tussen de twee getallen.',
  'Tel door van het kleinste getal naar het grootste. Hoeveel stapjes zijn dat? De staven kunnen ver uit elkaar lijken, maar lees de getallen.',
  'Je kind leest twee staven af en rekent het verschil uit.',
  [LT('tiental', '10 meer', 'Tel nog eens rustig door, met stapjes van één. Hoeveel stapjes zijn het?', L2),
   LT('opgeteld', '196 meer', 'Dat zijn de twee getallen samen. Bij hoeveel meer vergelijk je de getallen: trek ze van elkaar af.', L2),
   ALG('Tel door van het kleinste getal naar het grootste. Hoeveel stapjes zijn dat?', L2)])

# #18 (013): afgerond op honderdtallen
L2 = 'Afronden verbergt kleine verschillen. Twee staven die na afronden gelijk zijn, kunnen bij heel andere getallen horen.'
ST(18, 'Welke getallen worden allemaal hetzelfde getal als je afrondt op honderdtallen?',
  'Bij afronden kan een getal omhoog of omlaag gaan. Bedenk twee getallen die niet even groot zijn, maar allebei op hetzelfde honderdtal uitkomen. Wat zegt dat over de staven?',
  'Je kind ziet dat afgeronde getallen in een grafiek kleine verschillen kunnen verbergen.',
  [LT('alleen omhoog', 'Beide aantallen zijn meer dan 300.', 'Bij afronden kun je omhoog en omlaag gaan. Kan een getal onder het honderdtal ook op dat honderdtal uitkomen?', L2),
   LT('precies gelijk', 'De echte aantallen zijn precies gelijk.', 'Denk eens aan alle getallen die afgerond op hetzelfde honderdtal uitkomen. Zijn die allemaal even groot?', L2),
   ALG('Welke getallen komen allemaal op hetzelfde honderdtal uit als je afrondt?', L2)])

# #19 (014): plaatjes van verschillende grootte
L2 = 'Elk plaatje staat voor hetzelfde aantal. Een groter plaatje laat je denken aan een groter aantal, ook al is dat niet zo.'
ST(19, 'Beide plaatjes staan voor hetzelfde aantal. Waar kijken je ogen naar?',
  'Bij een plaatjesgrafiek horen alle plaatjes dezelfde grootte te hebben. Wat denk je als je een groot plaatje naast een klein plaatje ziet?',
  'Je kind ziet dat plaatjes van verschillende grootte in een plaatjesgrafiek misleiden.',
  [LT('echt fruit', 'Peren zijn nu eenmaal groter dan appels.', 'In een grafiek gaat het niet om het echte fruit, maar om de aantallen die de plaatjes laten zien.', L2),
   LT('aantal plaatjes', 'Er staan te weinig plaatjes bij appels.', 'Het aantal plaatjes klopt juist wel. Let op hoe groot de plaatjes getekend zijn.', L2),
   ALG('Staan de plaatjes voor hetzelfde aantal? Kijk hoe groot ze getekend zijn.', L2)])

# #20 (015): plaatjesgrafiek, keer
L2 = 'Elk plaatje telt voor het getal dat erbij staat. Het aantal plaatjes keer dat getal is het echte aantal.'
ST(20, 'Lees eerst voor hoeveel er één plaatje staat.',
  'Eén plaatje staat voor een groepje. Tel de plaatjes en doe dat aantal keer de grootte van het groepje.',
  'Je kind leest een plaatjesgrafiek: het aantal plaatjes keer wat één plaatje betekent.',
  [LT('plaatjes geteld', '6 kinderen', 'Dat is het aantal plaatjes. Eén plaatje staat voor meer dan één: lees nog eens voor hoeveel.', L2),
   LT('opgeteld', '16 kinderen', 'Dat zijn de twee getallen bij elkaar opgeteld. Elk plaatje staat voor een heel groepje: doe keer.', L2),
   ALG('Lees voor hoeveel één plaatje staat. Doe het aantal plaatjes keer dat getal.', L2)])

# #21 (016): plaatjesgrafiek met een half plaatje
L2 = 'Tel de volle plaatjes keer wat één plaatje betekent. Een halve tekening telt voor de helft. Tel alles bij elkaar op.'
ST(21, 'Een halve tekening staat voor de helft van wat één tekening betekent.',
  'Reken eerst de volle plaatjes uit: het aantal keer wat één plaatje betekent. Het halve plaatje is de helft daarvan. Tel die twee bij elkaar op.',
  'Je kind leest een plaatjesgrafiek met een half plaatje: dat telt voor de helft.',
  [LT('halve als volle', '16 honden', 'Zo telt het halve plaatje mee als een vol plaatje. Voor hoeveel staat het halve plaatje?', L2),
   LT('plaatjes geteld', '4 honden', 'Dat getal is het aantal plaatjes, en ook wat één plaatje betekent. Reken uit wat alle plaatjes samen betekenen.', L2),
   ALG('Reken de volle plaatjes uit en tel de helft van één plaatje erbij.', L2)])

# #22 (017): bredere staaf
L2 = 'Alleen de hoogte van een staaf telt. Een bredere staaf ziet er groter uit, maar staat voor hetzelfde. Daarom horen alle staven even breed te zijn.'
ST(22, 'Waaraan zie je in een staafdiagram hoeveel het is: aan de hoogte of aan de breedte?',
  'In een staafdiagram telt alleen de hoogte. Twee staven die even hoog zijn, staan voor evenveel. Wat doet een bredere staaf dan met je ogen?',
  'Je kind ziet dat de breedte van een staaf niets zegt, maar wel kan misleiden.',
  [LT('breed is meer', 'De brede staaf hoort bij meer kinderen.', 'In een staafdiagram vertelt alleen de hoogte hoeveel het is. Wat zegt de breedte dan?', L2),
   LT('naast elkaar', 'Staven mogen nooit naast elkaar staan.', 'Staven naast elkaar is heel gewoon. Let op het verschil in breedte.', L2),
   ALG('Kijk alleen naar de hoogte van de staven. Wat doet de breedte met je ogen?', L2)])

# #23 (018): as begint niet bij nul
L2 = 'Als de as niet bij nul begint, zie je maar een stukje van elke staaf. Een klein verschil lijkt dan groot.'
ST(23, 'Bij welk getal begint de as? Welk stuk van de staven zie je dan niet?',
  'Begint de as niet bij nul, dan zie je van elke staaf alleen het stuk boven het begingetal. Hoe zien kleine verschillen tussen de staven er dan uit?',
  'Je kind ziet dat een as die niet bij nul begint verschillen groter laat lijken.',
  [LT('te dicht', 'De staven staan te dicht bij elkaar.', 'De afstand tussen de staven maakt niets uit. Kijk nog eens bij welk getal de as begint.', L2),
   LT('te weinig geteld', 'Er zijn te weinig boeken geteld.', 'Met de aantallen is niets mis. Kijk naar waar de as begint.', L2),
   ALG('Kijk bij welk getal de as begint. Wat zie je dan van de staven?', L2)])

# #24 (019): percentages van klassen die niet even groot zijn
L2 = 'Een percentage hoort bij een totaal. Bij een grotere klas kan een kleiner percentage toch meer voetballers zijn.'
ST(24, 'Een percentage is een deel van een totaal. Zijn de twee klassen even groot?',
  'Reken voor elke klas uit hoeveel voetballers het zijn: het percentage van het aantal in die klas. Vergelijk daarna de aantallen, niet de percentages.',
  'Je kind vergelijkt aantallen in plaats van percentages als de groepen niet even groot zijn.',
  [LT('percentages vergeleken', 'Klas A, want 50% is meer dan 40%.', 'Een groter percentage hoeft geen groter aantal te zijn. De klassen zijn niet even groot: reken de aantallen uit.', L2),
   LT('evenveel', 'Ze hebben allebei evenveel voetballers.', 'Reken voor allebei de klassen het percentage om naar een echt aantal. Komt er hetzelfde uit?', L2),
   ALG('Reken voor elke klas het aantal voetballers uit, en vergelijk de aantallen.', L2)])

# #25 (020): cirkeldiagram zonder totaal
L2 = 'Een cirkeldiagram toont hoe groot elk stuk is in procenten. Zonder het totaal kun je geen aantal uitrekenen.'
ST(25, 'Een cirkeldiagram toont percentages. Staat er ook bij hoeveel er in totaal meededen?',
  'Een percentage is een deel van het totaal. Om een aantal uit te rekenen, heb je het totaal nodig. Staat dat ergens?',
  'Je kind ziet dat een cirkeldiagram met percentages zonder totaal geen aantallen geeft.',
  [LT('percentage als aantal', '40 kinderen hebben een hond gekozen.', 'Een percentage is geen aantal. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat erbij?', L2),
   LT('tiende', '4 kinderen hebben een hond gekozen.', 'Een percentage is geen aantal, en een tiende ervan ook niet. Zonder het totaal kun je geen aantal uitrekenen.', L2),
   ALG('Een cirkeldiagram toont percentages. Weet je hoeveel er in totaal meededen?', L2)])

# #26 (021): tijdas met ongelijke stappen
L2 = 'Op een tijdas betekent dezelfde afstand ook dezelfde tijd. Zitten er tussen twee punten veel meer jaren, dan klopt de as niet.'
ST(26, 'Hoeveel jaren komen er telkens bij van het ene jaartal naar het volgende?',
  'Op een tijdas hoort dezelfde afstand bij dezelfde tijd. Reken bij elk paar jaartallen naast elkaar uit hoeveel jaar ertussen ligt. Is dat steeds evenveel?',
  'Je kind ziet dat een tijdas misleidt als de jaartallen niet in gelijke stappen oplopen.',
  [LT('volgorde', 'De jaren staan in de verkeerde volgorde.', 'De volgorde van klein naar groot klopt. Kijk naar hoeveel jaar er tussen de jaartallen zit.', L2),
   LT('aantal punten', 'Er horen precies vier punten in een lijngrafiek.', 'Het aantal punten mag je zelf kiezen. Let op hoeveel jaar er tussen twee punten zit.', L2),
   ALG('Reken uit hoeveel jaar er tussen twee jaartallen naast elkaar zit. Is dat steeds evenveel?', L2)])

# #27 (022): twee grafieken met verschillende assen
L2 = 'Je mag twee lijnen alleen vergelijken als de assen hetzelfde zijn. Anders hoort dezelfde steilheid bij heel andere aantallen.'
ST(27, 'Kijk tot welk getal elke as loopt. Zijn de assen hetzelfde?',
  'Een even steile lijn betekent bij een as tot een hoog getal veel meer dan bij een as tot een laag getal. Vergelijk daarom eerst de assen, dan pas de lijnen.',
  'Je kind vergelijkt twee grafieken pas na het vergelijken van de assen.',
  [LT('kleine as', 'De grafiek met de as tot 50 stijgt het meest.', 'Kijk hoeveel elke as per hokje omhoog gaat. Bij welke as hoort bij dezelfde steilheid het grootste aantal?', L2),
   LT('evenveel', 'Beide grafieken stijgen precies evenveel.', 'De lijnen lijken hetzelfde, maar de assen zijn dat niet. Vergelijk de getallen bij de assen.', L2),
   ALG('Vergelijk eerst tot welk getal elke as loopt, en dan pas de lijnen.', L2)])

# #28 (023): te weinig gevraagd
L2 = 'Een handjevol uit één klas zegt weinig over de hele school. Je moet er veel meer vragen, uit verschillende groepen.'
ST(28, 'Hoeveel zijn er gevraagd, en hoeveel zitten er op de hele school?',
  'Een kop over de hele school moet gaan over veel leerlingen uit verschillende klassen. Is dat hier zo?',
  'Je kind ziet dat een onderzoek bij een paar leerlingen uit één klas niets zegt over de hele school.',
  [LT('allemaal rekenen', 'Ja, want alle 5 kozen voor rekenen.', 'Die paar kozen inderdaad rekenen. Maar hoeveel zitten er op de hele school?', L2),
   LT('één klas', 'Ja, één klas lijkt op alle klassen.', 'Denk aan de andere groepen. Zouden die precies hetzelfde kiezen?', L2),
   ALG('Hoeveel zijn er gevraagd? Zegt dat iets over de hele school?', L2)])

# #29/#30/#31: 'X en Y zijn samen meer dan de helft' (Ja of Nee per item; zelfde teksten als b6 VBN-E04 #34)
H1_SA = 'Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.'
H2_SA = 'Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?'
L2_SA = 'Tel de twee percentages op en vergelijk met vijftig procent. Is het samen meer, dan klopt de zin.'
OZ_SA = 'Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).'
LJA = LT('ja', 'Ja, dat klopt.', 'Lees de twee staven nog eens af en tel hun percentages op. Komt dat samen echt boven de vijftig procent uit?', L2_SA)
LNEE = LT('nee', 'Nee, dat klopt niet.', 'Lees de twee staven nog eens af en tel hun percentages op. Is dat samen meer dan vijftig procent?', L2_SA)
LNZ = LT('niet te zien', 'Dat kun je hier niet zien.', 'De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.', L2_SA)
AL_SA = ALG('Tel de twee percentages op en vergelijk met vijftig procent.', L2_SA)
ST(29, H1_SA, H2_SA, OZ_SA, [LNEE, LNZ, AL_SA])
ST(30, H1_SA, H2_SA, OZ_SA, [LJA, LNZ, AL_SA])
ST(31, H1_SA, H2_SA, OZ_SA, [LNEE, LNZ, AL_SA])
# ---------------- schrijven ----------------
def reden(t):
    if re.search(r'\d', t): return 'tekst met getallen uit het item; nu een vaste tekst zonder cijfers (regel nagerekend), met eigen laag 2'
    if re.match(r'Je (hebt|telde|bent|noemde|vergat|deelde|nam|zit)\b', t): return 'zegt zeker wat het kind deed; nu een waardezin of een vraag (les 20/101/161), met eigen laag 2'
    return 'vervangen door een vaste tekst per regel, met eigen laag 2 (les 40)'
def sleutels(doel):
    t = open(f"{os.environ.get('DATA_BASE', BASE)}/somtypen/{doel}.md", encoding='utf-8').read()
    return {int(m[3]): (int(m[1]), m[2].strip(), m[4]) for m in
            re.finditer(r'^## Somtype (\d+): (.*)\n\n?- Sleutel: nrOrigineel \*\*(\d+)\*\* · somtypeOrigineel “(.*?)”', t, re.M)}
data = {}; S = []
for doel, nro, h1, h2, oz, fh in E:
    if doel not in data: data[doel] = json.load(open(f"{os.environ.get('DATA_BASE', BASE)}/data/per_doel/{doel}.json", encoding='utf-8'))['items']
    nr, kop, sto = sleutels(doel)[nro]
    st = {'doel': doel, 'nr': nr, 'somtype': kop, 'nrOrigineel': nro, 'somtypeOrigineel': sto, 'hint1': h1, 'hint2': h2, 'ouderzin': oz, 'foutHints': [dict(f) for f in fh]}
    cv = {}
    for it in data[doel]:
        if it['merge']['somtypeNrOrigineel'] != nro: continue
        dk = {x['fout']: x['denkfout'] for x in it['extraVelden'].get('claudeDenkfouten') or []}
        for f in it['extraVelden'].get('claudeFoutHints') or []:
            cv.setdefault(f['uitleg'], dk.get(f['fout']))
    if cv: st['claudeVervangen'] = [V(t, d, reden(t)) for t, d in cv.items()]
    S.append(st)
D = {'batch': 'batch7', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 7 = VBN-E04 #6–#31: meerkeuze met tekstopties (misleidende grafieken, aflezen, percentages, onderzoek)). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
