#!/usr/bin/env python3
"""Schrijft hints/batch6.json (G8 batch 6: MEET-E07 #1–#4 (snelheid en afstand), MEET-V01 #1–#3 (hectare, bouwwerk van blokjes, bekers),
VBN-E01 #1–#2 (tabel doortrekken, verschil), VBN-E03 #1–#5 (spaartabel), VBN-E04 #1–#5 en #32–#37 (staafdiagram met percentages, onderzoek,
meetfout) = 25 somtypes, 193 items: 31 kaal, 162 meerkeuze).
8 okt 2026 (16:4x), Oefeningen. Formaat als make_batch6.py. Data: live g8 (build 16:25:38/40). Lessen: hints/lessen_g8.md t/m les 307.
Analyse en checks: /workspace/g8work/b6/check.py op de zandbak /workspace/g8work/b6/sbx.sh (verse kopie van live).
Keuzes:
- Kale items: rekenregels uit scripts/fout_regels.py waar de motor de route kent ('getal1 × getal2', 'getal1 + getal2', 'getal1 - getal2 of …',
  'antwoord : 10' / ': 100' (Oef-#490), 'een getal uit de vraag'); daarna labelregels voor Claudes sleutels zonder motorregel (les 270), 'andere fout' als laatste.
- Meerkeuze met tekstopties: per foute optie een letterlijke regel met de hele optietekst (G8-2); de tekst moet kloppen voor elk item waar de optie
  fout is (VBN-E04: 'Ja'/'Nee' wisselen per item).
- MEET-V01 #2 (151 bouwwerken, getalopties): de motor kent geen route op de maten van het bouwwerk. Eén regel op alle Claude-sleutels met een tekst per
  route ('a / b / …'): de motor kiest per sleutel de tekst die het meest lijkt op Claudes tekst (taalfix met twee of meer teksten). b6/check rekent
  per sleutel de route na op de maten (diep × hoog × breed) en eist dat de gekozen tekst bij die route hoort.
- Geen cijfers, geen woorden van de [ding]/[wie]/[naam]/[plek]-plekken (les 147; uitzondering TOEGESTAAN in check.py: 'hectare', 'milliliter'),
  geen plekwoorden (les 193), geen 'zoveel' vooraan (les 197/272), geen kloktijden (les 262), verklaptoets meerkeuze (les 260/264/288).
Na een sync nooit --force: correcties via hints/patch_batch6.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B6_OUT', f'{BASE}/hints/batch6.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch6.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch6.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch6.json bestaat al: patch in place (hints/patch_batch6.py), of --force als er nog geen sync is geweest.')
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
def CLV(soort, naam, teksten, sterker):
    """regel op alle Claude-sleutels (geen label) met een tekst per route: de motor kiest per sleutel de tekst die het meest op Claudes tekst lijkt"""
    f = T(soort, f'Claudes sleutels (alle): {naam}', ' / '.join(teksten), None,
          'geen motorregel op de maten van het bouwwerk; per route een eigen tekst, per sleutel gekozen op Claudes tekst en in b6/check op de maten nagerekend', None)
    f['tekstSterker'] = sterker; return f
E7, V1, E01, E03, E04 = "G8-MEET-E07", "G8-MEET-V01", "G8-VBN-E01", "G8-VBN-E03", "G8-VBN-E04"


# ================= MEET-E07 #1/#3: snelheid (km per uur) uit afstand en tijd; de tijd is een half uur meer dan hele uren =================
H2_SN = 'Deel de kilometers door het aantal uur. Met een half uur is dat lastig: maak dan eerst allebei twee keer zo groot. Dan deel je door een heel getal.'
FH_SN = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt hoeveel kilometer er in één uur gaat.', H2_SN),
         R('keer de tijd', 'fout = getal1 × getal2', 'Dat is de afstand keer de tijd. Per uur betekent: hoeveel kilometer in één uur? Deel de afstand door het aantal uur.', H2_SN),
         R('tijd eraf', 'fout = getal1 - getal2 of getal2 - getal1', 'Dat is de afstand min de tijd. Snelheid is de afstand gedeeld door de tijd: hoeveel kilometer in één uur?', H2_SN),
         CL('alleen hele uren', 'deel-vergeten-bij-splitsen', 'Dan deel je alleen door de hele uren. Het halve uur hoort er ook bij: deel door het hele aantal uur.', H2_SN),
         ALG('Deel de kilometers door het aantal uur. Kijk of het klopt: je antwoord keer het aantal uur moet de afstand geven.', H2_SN)]
for n_ in (1, 3):
    E.append((E7, n_, 'Per uur betekent: hoe ver kom je in één uur? Deel de afstand door het aantal uur.', H2_SN,
              'Je kind rekent een snelheid uit: de afstand gedeeld door de tijd. Bij een half uur helpt het om eerst allebei te verdubbelen.', FH_SN))

# ================= MEET-E07 #2/#4: afstand uit tijd en snelheid =================
H2_AF = 'Reken eerst de hele uren: de snelheid keer het aantal hele uren. Een half uur is de helft van de snelheid. Tel die twee bij elkaar op.'
FH_AF = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt hoeveel kilometer het in die hele tijd is.', H2_AF),
         R('tijd erbij', 'fout = getal1 + getal2', 'Dat is de tijd plus de snelheid. Elk uur komt de snelheid erbij: doe de snelheid keer het aantal uur.', H2_AF),
         CL('alleen hele uren', 'deel-vergeten-bij-splitsen', 'Daar zitten alleen de hele uren in. Het halve uur moet er ook nog bij: dat is de helft van de snelheid.', H2_AF),
         ALG('Doe de snelheid keer het aantal uur. Een half uur is de helft van de snelheid.', H2_AF)]
for n_ in (2, 4):
    E.append((E7, n_, 'Elk uur kom je zo ver als de snelheid. Doe de snelheid keer het aantal uur.', H2_AF,
              'Je kind rekent een afstand uit: de snelheid keer de tijd. Een half uur is de helft van de snelheid.', FH_AF))

# ================= MEET-V01 #1: hectare → m² (kaal) =================
H2_HA = 'Reken uit hoeveel vierkante meter één hectare is: honderd keer honderd. Doe dat keer het aantal hectare. Bij een kommagetal schuift de komma mee.'
E.append((V1, 1, 'Eén hectare is een vierkant van honderd meter lang en honderd meter breed.', H2_HA,
          'Je kind rekent hectare om naar vierkante meter: één hectare is honderd keer honderd vierkante meter.',
          [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat is het aantal hectare. De vraag wil vierkante meters: hoeveel vierkante meter is één hectare?', H2_HA),
           R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Eén hectare is honderd keer honderd vierkante meter. Tel de nullen nog eens.', H2_HA),
           R('honderd keer te weinig', 'fout = antwoord : 100', 'Dat is honderd keer te weinig. Eén hectare is niet honderd vierkante meter, maar honderd keer honderd.', H2_HA),
           ALG('Eén hectare is honderd keer honderd vierkante meter. Doe dat keer het aantal hectare.', H2_HA)]))

# ================= MEET-V01 #2: vol bouwwerk van blokjes (151 items, getalopties) =================
H2_BW = 'Tel in één laag de blokjes langs de voorkant en langs de zijkant, en doe die keer elkaar. Tel daarna hoeveel lagen er op elkaar liggen. Doe één laag keer het aantal lagen.'
BW = ['Dat zijn de drie maten bij elkaar opgeteld. Het bouwwerk is vol. Reken uit hoeveel blokjes er in één laag liggen, en dan in alle lagen samen.',
      'Dat is de helft van alle blokjes. Reken eerst één laag uit en doe dat dan keer het aantal lagen.',
      'Dat is een laag te veel. Tel nog eens hoeveel lagen er op elkaar liggen.',
      'Dat zijn de blokjes van drie kanten samen: voorkant, zijkant en bovenkant. Het bouwwerk is vol, dus er zitten ook blokjes binnenin.',
      'Dat is één laag. Er liggen meer lagen op elkaar: doe één laag keer het aantal lagen.',
      'Reken eerst uit hoeveel blokjes er in één laag liggen. Doe dat daarna keer het aantal lagen.',
      'Dat is een laag te weinig. Tel nog eens hoeveel lagen er op elkaar liggen.',
      'Dat is een rij blokjes te weinig. Kijk nog eens hoe breed en hoe diep het bouwwerk is.']
L2_BW = 'Een vol bouwwerk heeft in elke laag evenveel blokjes. Reken één laag uit: blokjes langs de voorkant keer blokjes langs de zijkant. Doe dat keer het aantal lagen.'
E.append((V1, 2, 'Het bouwwerk is helemaal vol, ook binnenin. Tel eerst hoeveel blokjes er in één laag liggen.', H2_BW,
          'Je kind rekent uit hoeveel blokjes er in een vol bouwwerk zitten: de blokjes in één laag keer het aantal lagen.',
          [CLV('route van Claude', 'bouwwerk', BW, L2_BW),
           ALG('Reken eerst uit hoeveel blokjes er in één laag liggen. Doe dat daarna keer het aantal lagen.', L2_BW)]))

# ================= MEET-V01 #3: pak drinken verdelen over bekers (meerkeuze) =================
H2_BK = 'Eén liter is duizend milliliter. Reken het pak om naar milliliter. Deel dat door het aantal milliliter van één beker.'
E.append((V1, 3, 'Reken eerst om, zodat het pak en een beker in dezelfde maat staan.', H2_BK,
          'Je kind rekent liters om naar milliliters (keer duizend) en deelt dan door wat er in één beker gaat.',
          [LT('één liter', '4 bekers', 'Zo vul je alleen één liter. Het pak is meer dan één liter: reken het hele pak om naar milliliter.', H2_BK),
           LT('nullen', '15 bekers', 'Tel de nullen nog eens na bij het omrekenen. Eén liter is duizend milliliter.', H2_BK),
           ALG('Reken het pak om naar milliliter en deel door wat er in één beker gaat.', H2_BK)]))

# ================= VBN-E01 #1: tabel doortrekken (meerkeuze) =================
H2_TB = 'Reken uit hoeveel er van het ene jaar naar het volgende bij komt. Komt dat er elk jaar bij? Doe het dan nog één keer erbij, bovenop het grootste aantal uit de tabel.'
E.append((E01, 1, 'Kijk hoeveel er elk jaar bij komt.', H2_TB,
          'Je kind trekt een tabel door: elk jaar komt er hetzelfde aantal bij, dus ook in het jaar daarna.',
          [LT('jaar ervoor', 'Ongeveer 60 appels', 'Dat aantal staat al in de tabel, bij het jaar ervoor. Er komt elk jaar nog wat bij.', H2_TB),
           LT('verdubbeld', 'Ongeveer 120 appels', 'Dat is het dubbele. Elk jaar komt er hetzelfde aantal bij; het wordt niet elk jaar twee keer zo veel.', H2_TB),
           ALG('Kijk hoeveel er elk jaar bij komt, en doe dat nog één keer erbij.', H2_TB)]))

# ================= VBN-E01 #2: verschil tussen de verste en de kortste sprong (meerkeuze) =================
H2_SP = 'Zoek de verste en de kortste sprong. Let op: een sprong zonder komma is precies een hele meter. Trek de kortste van de verste af.'
E.append((E01, 2, 'Het verschil is hoeveel de verste sprong verder is dan de kortste.', H2_SP,
          'Je kind zoekt de grootste en de kleinste waarde en trekt ze van elkaar af (het verschil).',
          [LT('opgeteld', '4,4 m', 'Dat zijn de verste en de kortste sprong samen. Een verschil reken je uit met aftrekken.', H2_SP),
           LT('andere sprongen', '0,2 m', 'Dat is het verschil tussen twee andere sprongen. Zoek de verste en de allerkortste sprong. Kijk ook naar de sprong zonder komma.', H2_SP),
           ALG('Zoek de verste en de kortste sprong, en trek ze van elkaar af.', H2_SP)]))

# ================= VBN-E03 #1: spaartabel doortrekken (kaal) =================
H2_ST = 'Reken de stap uit: het verschil tussen twee weken naast elkaar. Begin bij het bedrag van week nul. Doe de stap erbij, zo vaak als het nummer van de week uit de vraag.'
E.append((E03, 1, 'Kijk hoeveel er van week tot week bij komt. Dat is elke week hetzelfde.', H2_ST,
          'Je kind trekt een spaartabel door: het startbedrag plus voor elke week hetzelfde bedrag.',
          [CL('niet bij die week', 'deel-vergeten-bij-splitsen', 'Klopt dat bedrag bij de week uit de vraag? Begin bij het bedrag van week nul en doe er voor elke week de stap bij.', H2_ST),
           CL('een week te weinig', 'tafelbuur', 'Dat is één week te weinig. Tel nog eens hoe vaak de stap erbij komt: één keer voor elke week.', H2_ST),
           ALG('Begin bij het bedrag van week nul. Doe er voor elke week de stap bij, tot je bij de week uit de vraag bent.', H2_ST)]))

# ================= VBN-E03 #2–#5: sparen met een startbedrag (kaal) =================
H2_SV = 'Reken eerst uit hoeveel er in al die weken bij komt: het weekbedrag keer het aantal weken. Tel daar het startbedrag bij op.'
FH_SV = [CL('startbedrag vergeten', 'deel-vergeten-bij-splitsen', 'Dat is alleen wat er in die weken bij komt. Het startbedrag hoort er ook nog bij.', H2_SV),
         CL('een week te veel', 'tafelbuur', 'Dat is één week te veel. Tel nog eens: voor elke week komt het weekbedrag er één keer bij.', H2_SV),
         CL('alles opgeteld', 'optellen-ipv-vermenigvuldigen', 'Dat zijn de getallen uit de vraag bij elkaar opgeteld. Elke week komt hetzelfde bedrag bij: dat is een keersom.', H2_SV),
         ALG('Doe het weekbedrag keer het aantal weken. Tel daar het startbedrag bij op.', H2_SV)]
for n_ in (2, 3, 4, 5):
    E.append((E03, n_, 'Je begint niet bij nul: er is al een startbedrag. Daarna komt er elke week hetzelfde bedrag bij.', H2_SV,
              'Je kind rekent uit hoeveel er gespaard is: het startbedrag plus het weekbedrag keer het aantal weken.', FH_SV))

# ================= VBN-E04 #1/#3/#5: aantal uit een diagram met percentages (antwoord: niet te zien) =================
H2_PA = 'Een percentage zegt hoeveel van elke honderd. Om een aantal te vinden, moet je weten hoeveel er in totaal meededen. Staat dat ergens bij het diagram?'
FH_PA = [LT('ja', 'Ja, dat klopt.', 'Het diagram toont percentages, geen aantallen. Hoeveel er in totaal meededen, staat er niet bij. Kun je dan een aantal uitrekenen?',
            'Een percentage is een deel van het totaal. Zonder het totaal kun je geen aantal uitrekenen, en dus ook niet zeggen of het klopt.'),
         LT('nee', 'Nee, dat klopt niet.', 'Om te zeggen dat het niet klopt, moet je het aantal kunnen uitrekenen. Het diagram toont alleen percentages. Weet je hoeveel er in totaal meededen?',
            'Een percentage is een deel van het totaal. Zonder het totaal kun je geen aantal uitrekenen, en dus ook niet zeggen of het klopt.'),
         ALG('Het diagram toont percentages. Weet je hoeveel er in totaal meededen?', H2_PA)]
for n_ in (1, 3, 5):
    E.append((E04, n_, 'Het diagram toont percentages. De zin onder het diagram noemt een aantal.', H2_PA,
              'Je kind ziet dat een diagram met percentages geen aantallen geeft: zonder het totaal kun je geen aantal uitrekenen.', FH_PA))

# ================= VBN-E04 #2/#4/#33: 'Meer dan de helft kiest …' (Ja of Nee per item) =================
H2_HE = 'Zoek de staaf die in de zin genoemd wordt. Lees af hoe hoog hij komt: elk streepje is tien procent. Komt hij boven de vijftig procent uit?'
L2_HE = 'De helft is vijftig procent. Lees de staaf af en vergelijk: is hij hoger dan vijftig procent, dan klopt de zin. Is hij niet hoger, dan klopt de zin niet.'
FH_HE = [LT('ja', 'Ja, dat klopt.', 'Lees het percentage van die staaf nog eens af. Komt hij echt boven de vijftig procent uit?', L2_HE),
         LT('nee', 'Nee, dat klopt niet.', 'Lees het percentage van die staaf nog eens af. Meer dan de helft is meer dan vijftig procent. Hoe hoog komt de staaf?', L2_HE),
         LT('niet te zien', 'Dat kun je hier niet zien.', 'Meer dan de helft is ook een percentage: meer dan vijftig procent. Dat lees je af aan de staaf.', L2_HE),
         ALG('Lees de staaf af en vergelijk met vijftig procent.', L2_HE)]
for n_ in (2, 4, 33):
    E.append((E04, n_, 'Meer dan de helft betekent: meer dan vijftig procent.', H2_HE,
              'Je kind leest een percentage af in een staafdiagram en vergelijkt het met de helft (vijftig procent).', FH_HE))

# ================= VBN-E04 #32: 'Tekenen is precies … keer zo vaak gekozen als …' =================
H2_KZ = 'Lees de staaf van tekenen en de andere staaf uit de zin af. Doe de andere staaf keer het getal uit de zin. Komt dat precies uit op de staaf van tekenen?'
L2_KZ = 'Vergelijk de twee staven: hoeveel keer past de kleine staaf in de staaf van tekenen? Is dat precies het getal uit de zin, dan klopt het.'
E.append((E04, 32, 'Lees de twee staven af die in de zin staan.', H2_KZ,
          'Je kind leest twee percentages af en controleert of het ene precies een aantal keer zo groot is als het andere.',
          [LT('ja', 'Ja, dat klopt.', 'Reken het na: doe de andere staaf keer het getal uit de zin. Komt dat precies uit op tekenen?', L2_KZ),
           LT('niet te zien', 'Dat kun je hier niet zien.', 'De twee percentages staan in het diagram. Dan kun je ze vergelijken: lees ze af en reken het na.', L2_KZ),
           ALG('Lees de twee staven af en reken na of het klopt.', L2_KZ)]))

# ================= VBN-E04 #34: 'Water en … zijn samen meer dan de helft' =================
H2_SA = 'Lees de twee staven af die in de zin staan. Tel hun percentages op. Is dat samen meer dan vijftig procent?'
L2_SA = 'Tel de twee percentages op en vergelijk met vijftig procent. Is het samen meer, dan klopt de zin.'
E.append((E04, 34, 'Meer dan de helft betekent: meer dan vijftig procent. Het gaat om twee staven samen.', H2_SA,
          'Je kind telt twee percentages op en vergelijkt de som met de helft (vijftig procent).',
          [LT('nee', 'Nee, dat klopt niet.', 'Kijk naar de twee staven samen, niet naar één staaf. Tel hun percentages op.', L2_SA),
           LT('niet te zien', 'Dat kun je hier niet zien.', 'De twee percentages staan in het diagram. Tel ze op en vergelijk met vijftig procent.', L2_SA),
           ALG('Tel de twee percentages op en vergelijk met vijftig procent.', L2_SA)]))

# ================= VBN-E04 #35: staven samen hoger dan het aantal in de klas =================
H2_HD = 'Elk dier in het diagram hoort bij iemand uit de klas. Kan iemand bij twee staven meetellen? Lees ook de vraag nog eens: hoeveel zitten er in de klas?'
L2_HD = 'Iemand met een hond en een kat telt bij twee staven mee. Zo worden de staven samen hoger dan het aantal in de klas, zonder dat er iets fout is.'
E.append((E04, 35, 'Tel je alle staven op, dan kom je boven het aantal in de klas uit. Hoe kan dat?', H2_HD,
          'Je kind zoekt een gewone verklaring voor een diagram dat optelt tot meer dan het aantal in de klas.',
          [LT('fout getekend', 'De grafiek is fout getekend', 'Een diagram dat samen hoger uitkomt dan de klas, hoeft niet fout te zijn. Kan iemand bij twee staven meetellen?', L2_HD),
           LT('getal uit het diagram', 'Er zitten 30 kinderen in de klas', 'Hoeveel er in de klas zitten, staat al in de vraag. Dat is minder dan de staven samen. Hoe kan dat dan?', L2_HD),
           ALG('Lees de vraag nog eens: hoeveel zitten er in de klas? Kan iemand bij twee staven meetellen?', L2_HD)]))

# ================= VBN-E04 #36: onderzoek bij een eenzijdige groep =================
H2_ON = 'Stel dat Sanne het aan alle kinderen van de school vraagt. Zou dan ook zo goed als iedereen schaken zeggen? Kies de uitleg die past bij dat verschil.'
L2_ON = 'Een eerlijk onderzoek vraagt het aan kinderen die lijken op iedereen. Kinderen van een schaakclub kiezen vaak schaken, omdat ze daar al van houden.'
E.append((E04, 36, 'Wie vroeg Sanne het? Houden die kinderen net zo veel van schaken als de rest van de school?', H2_ON,
          'Je kind ziet dat een onderzoek alleen eerlijk is als je het vraagt aan kinderen die lijken op iedereen.',
          [LT('te weinig', 'Zij vroeg het aan te weinig kinderen', 'Stel dat ze honderd schakers vraagt. Zou de uitkomst dan eerlijker zijn? Lijken die kinderen op alle kinderen van de school?', L2_ON),
           LT('niets mis', 'Er is niets mis met haar onderzoek', 'Op een schaakclub zitten kinderen die graag schaken. Lijken zij op alle kinderen van de school?', L2_ON),
           ALG('Lijken de kinderen die Sanne vroeg op alle kinderen van de school?', L2_ON)]))

# ================= VBN-E04 #37: meetfout (uitschieter) =================
H2_MF = 'Zet de metingen op volgorde. Kijk hoe groot de stap is tussen twee metingen naast elkaar. Waar is die stap veel groter dan de rest?'
L2_MF = 'Metingen die kloppen, liggen dicht bij elkaar. Een meting die ver van de rest af ligt, is waarschijnlijk fout gemeten.'
E.append((E04, 37, 'Een plant groeit langzaam. Metingen die kloppen, liggen dicht bij elkaar.', H2_MF,
          'Je kind zoekt de meting die ver van de andere af ligt (een uitschieter): die is waarschijnlijk fout gemeten.',
          [LT('kleinste', '10 cm', 'Die meting ligt dicht bij de andere. Zoek de meting die er ver vandaan ligt.', L2_MF),
           LT('dichtbij', '15 cm', 'Die meting past bij de andere: het verschil is klein. Zoek de meting die er ver vandaan ligt.', L2_MF),
           ALG('Zoek de meting die ver van de andere af ligt.', L2_MF)]))
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
D = {'batch': 'batch6', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 6 = MEET-E07 #1–#4 + MEET-V01 #1–#3 + VBN-E01 #1–#2 + VBN-E03 #1–#5 + VBN-E04 #1–#5 en #32–#37: "
                "kaal en meerkeuze (snelheid; hectare, bouwwerk, bekers; tabel en verschil; spaartabel; staafdiagram, onderzoek, meetfout)). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
