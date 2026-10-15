#!/usr/bin/env python3
"""Schrijft hints/batch3.json (G8 batch 3: GET-E02 #37–#57 + GET-V02 #1–#4 = 25 somtypes van één meerkeuze-item:
aanpak kiezen, een aanpak beoordelen, een omrekening controleren; gemiddelde). 8 okt 2026 (15:4x), Oefeningen. Formaat als make_batch2.py.
Data: live g8 (build 15:36:15). Lessen: hints/lessen_g8.md t/m les 264 (vooral 144/260: H2 laat rekenen of proberen, niet de aanpak noemen;
195/245 afleiders op waarde; 250/255 woordgrenzen; 261 werkt-maar-niet-handig; 263; 264).
Analyse en checks: /workspace/g8work/b3/check.py op de zandbak /workspace/g8work/b3/sbx.sh (verse kopie van live).
Keuzes:
- Elke foute optie krijgt een letterlijke regel: de hele optietekst (fout_regels lett_past: met een cijfer als heel token, '€…' exact),
  zo pakt elke regel precies één optie (les 160/161; check.py rekent het per optie na). 'andere fout' als laatste, met een tekst die voor
  elke optie klopt.
- H1 = waar de vraag over gaat, zonder één optie te laten overblijven (les 264). H2: bij 'hoe reken je / wat ging er mis / wat had handiger
  gekund' laat H2 de situatie uitrekenen of een voorbeeld proberen en elke optie narekenen (les 144/260); de aanpak zelf staat in laag 2.
  GET-V02 (antwoord = een getal): H2 = de rekenstappen (les 144), zonder uitkomst. Geen cijfers, geen
  optieletters, geen plekwoorden (les 193: 'het cijfer helemaal rechts'), geen woorden uit de [ding]-plekken van de kop (les 147),
  geen zin die een bewerking uitsluit (les 217), geen verwijzing naar een andere strategie (les 231), geen tekst die begint met 'zoveel' (les 197).
- Laag 2 ('tekstSterker'): de aanpak in stappen (H2) of een eigen vervolgstap.
LET OP: alleen voor de eerste versie. Na een sync of rebuild NIET opnieuw draaien, ook niet met --force: patch in place met hints/patch_batch3.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B3_OUT', f'{BASE}/hints/batch3.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch3.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch3.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch3.json bestaat al: patch in place (hints/patch_batch3.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
L = R   # letterlijke regel: 'regel' is de hele tekst van de foute optie
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
E2 = 'G8-GET-E02'

V2 = 'G8-GET-V02'
STAP = "Reken elke aanpak uit."

# ---- E02 #37 (nrO 30): totaalprijs van twee soorten ----
L2 = 'Reken per soort: het aantal keer de prijs. Tel daarna die twee bedragen bij elkaar op.'
E.append((E2, 30, 'Je koopt van twee soorten meer dan één stuk, elke soort met een eigen prijs.',
  'Reken eerst zelf uit wat je in totaal betaalt. Reken dan elke aanpak uit. Welke komt op hetzelfde bedrag?',
  'Je kind kiest hoe je een totaalprijs uitrekent: eerst per soort het aantal keer de prijs, dan die bedragen optellen.',
  [L('aantal bij de prijs', 'Reken 3 maal 12 en tel 2 en 7 erbij op.', 'Dan tel je bij één soort het aantal bij de prijs op. Ook van die soort koop je meer dan één stuk van dezelfde prijs: wat kost dat samen?', L2),
   L('prijzen samen', 'Tel 12 en 7 op en doe dat maal 5.', 'Dan reken je alsof elk stuk de twee prijzen samen kost. Elke soort heeft een eigen prijs en een eigen aantal: reken ze apart uit.', L2),
   ALG('Wat kost alles van één soort samen? Doe dat voor allebei de soorten, en tel de bedragen op.', L2)]))

# ---- E02 #38 (nrO 31): wisselgeld ----
L2 = 'Tel eerst de prijzen op: dat is wat alles kost. Haal dat van het betaalde bedrag af. Wat overblijft, krijg je terug.'
E.append((E2, 31, 'Wisselgeld is wat je terugkrijgt, omdat je meer gaf dan alles kost.',
  'Reken eerst zelf uit hoeveel je terugkrijgt. Reken dan elke aanpak uit. Welke komt op hetzelfde bedrag?',
  'Je kind kiest hoe je wisselgeld uitrekent: eerst wat alles kost, dan dat van het betaalde bedrag afhalen.',
  [L('erbij in plaats van eraf', 'Tel de prijzen op, tel die bij het betaalde bedrag op.', 'Dan kom je op meer uit dan je betaalde. Kun je meer terugkrijgen dan je gaf?', L2),
   L('prijs als wisselgeld', 'Tel de prijzen op en noem die uitkomst het wisselgeld.', 'Dat is wat alles samen kost, niet wat je terugkrijgt. Hoeveel heb je meer betaald dan dat?', L2),
   ALG('Wat kost alles samen, en hoeveel heb je meer betaald dan dat?', L2)]))

# ---- E02 #39 (nrO 32): uitleg in de bibliotheek ----
L2 = 'Een goede uitleg zet de stappen in een volgorde die kan. Eerst zoek je op waar het boek staat. Dan loop je erheen, en pas dan pak je het.'
E.append((E2, 32, 'Een goede uitleg werkt altijd, ook voor iemand die de bibliotheek niet kent.',
  'Probeer elke uitleg in gedachten uit, stap voor stap. Kun je elke stap doen op het moment dat hij aan de beurt is? En vind je zo altijd het boek dat je zoekt?',
  'Je kind kiest de duidelijkste uitleg: stappen in een volgorde die altijd werkt.',
  [L('volgorde', 'Pak het boek, zoek de letter, loop naar dat vak.', 'Probeer die stappen in die volgorde. Kun je een boek pakken voordat je weet waar het staat?', L2),
   L('geen aanpak', 'Loop door de bibliotheek tot je iets leuks ziet.', 'Zo vind je misschien wel een boek, maar niet altijd het boek dat je zoekt. Een uitleg moet voor iedereen werken.', L2),
   ALG('Kun je elke stap doen op het moment dat hij aan de beurt is?', L2)]))

# ---- E02 #40 (nrO 33): alfabetische volgorde ----
L2 = 'Zoek steeds het woord dat in het alfabet het eerst komt, en zet dat apart. Doe dat opnieuw met de woorden die over zijn, tot ze allemaal een plek hebben.'
E.append((E2, 33, 'Alfabetische volgorde gaat over de letters. Een aanpak werkt altijd als elk woord zo een plek krijgt.',
  'Probeer elke aanpak uit met een paar woorden, bijvoorbeeld kat, aap en boom. Komt bij elke aanpak elk woord op de goede plek in het alfabet?',
  'Je kind kiest een aanpak om te sorteren die altijd werkt: steeds het woord zoeken dat in het alfabet het eerst komt.',
  [L('lengte', 'Zet de kortste namen vooraan', 'Alfabetische volgorde gaat over de letters, niet over hoe lang een woord is. Waar kijk je dan naar?', L2),
   L('twee vergeleken', 'Vergelijk alleen de eerste en de laatste naam', 'Dan krijgen de woorden daartussen geen plek. Elk woord moet op zijn plek komen.', L2),
   ALG('Krijgt bij die aanpak elk woord een plek, alleen door naar de letters te kijken?', L2)]))

# ---- E02 #41 (nrO 34): sparen ----
L2 = 'Je zoekt hoe vaak het bedrag van één week in het hele bedrag past. Dat reken je uit met delen: het hele bedrag gedeeld door het bedrag per week.'
E.append((E2, 34, 'Elke week komt er evenveel bij. Na hoeveel weken heb je het hele bedrag?',
  'Reken elke aanpak uit. Doe de uitkomst keer het bedrag van één week. Bij welke aanpak kom je precies op het bedrag dat je wilt hebben?',
  'Je kind kiest hoe je uitrekent hoeveel weken sparen nodig is: hoe vaak het weekbedrag in het spaardoel past.',
  [L('keer', 'Doe 45 keer 3', 'Dan krijg je een getal dat groter is dan het bedrag dat je wilt. Hoe vaak past het bedrag van één week in dat bedrag?', L2),
   L('één week eraf', 'Trek 3 van 45 af', 'Dan haal je maar één week sparen van het bedrag af. Hoe vaak past het bedrag van één week in het hele bedrag?', L2),
   ALG('Hoe vaak past het bedrag van één week in het bedrag dat je wilt hebben?', L2)]))

# ---- E02 #42 (nrO 35): sap verdelen (liter en een kleinere maat) ----
L2 = 'Reken eerst de liters om naar de kleine maat: hoeveel daarvan gaan er in één liter? Staan allebei de getallen in dezelfde maat, dan kun je delen.'
E.append((E2, 35, 'De ene maat staat in liter, de andere in een kleinere maat. Kun je die meteen met elkaar delen?',
  'Hoeveel van de kleine maat gaan er in één liter? Reken elke stap na: klopt het omrekenen, en staan daarna allebei de getallen in dezelfde maat?',
  'Je kind ziet dat je eerst dezelfde maat nodig hebt: liter omrekenen naar de kleine maat.',
  [L('direct delen', 'Deel 1,5 meteen door 250', 'Dan deel je liters door een kleinere maat. Maak eerst van allebei dezelfde maat.', L2),
   L('verkeerd omgerekend', 'Reken 1,5 liter om naar 150 milliliter', 'Reken het na: hoeveel van de kleine maat gaan er in één liter? Past dit getal daarbij?', L2),
   ALG('Maak eerst van allebei dezelfde maat. Hoeveel van de kleine maat gaan er in één liter?', L2)]))

# ---- E02 #43 (nrO 36): omtrek van een rechthoekige tuin ----
L2 = 'Een rechthoek heeft twee lange en twee korte zijden. Tel lengte en breedte op: dat is de helft van de weg rondom. Doe dat twee keer.'
E.append((E2, 36, 'De omtrek is de lengte rondom: langs alle zijden van de tuin.',
  'Bedenk een tuin, bijvoorbeeld zes meter lang en vier meter breed. Loop in gedachten rondom en tel alle zijden op. Reken dan elke aanpak uit met die tuin. Welke geeft hetzelfde?',
  'Je kind kiest hoe je de omtrek uitrekent: alle zijden rondom, dus lengte en breedte samen, twee keer.',
  [L('oppervlakte', 'Vermenigvuldig de lengte met de breedte.', 'Lengte keer breedte is de oppervlakte: hoeveel ruimte er in de tuin is. De omtrek is de lengte rondom.', L2),
   L('twee zijden', 'Tel lengte en breedte op en klaar.', 'Dan heb je maar twee zijden. Een rechthoek heeft er vier: hoeveel zijden mis je nog?', L2),
   ALG('De omtrek is de lengte rondom. Tel je alle vier de zijden mee?', L2)]))

# ---- E02 #44 (nrO 37): gemiddelde ----
L2 = 'Tel alle cijfers bij elkaar op: dat is het totaal. Verdeel dat eerlijk: deel het totaal door het aantal cijfers.'
E.append((E2, 37, 'Een gemiddelde is wat je krijgt als je alles eerlijk verdeelt, zodat elk cijfer even groot wordt.',
  'Probeer elke aanpak met drie cijfers: zes, zeven en acht. Het gemiddelde daarvan is zeven. Gebruik drie waar de aanpak het aantal cijfers gebruikt. Welke aanpak komt op zeven uit?',
  'Je kind kiest hoe je een gemiddelde uitrekent: alles optellen en delen door het aantal.',
  [L('erbij', 'Tel alle cijfers op en tel de som bij 5 op.', 'Dan wordt het getal alleen maar groter, groter dan elk cijfer. Een gemiddelde ligt tussen het laagste en het hoogste cijfer.', L2),
   L('hoogste', 'Zoek het hoogste cijfer en deel dat door 5.', 'Dan doet maar één cijfer mee. Bij een gemiddelde tellen alle cijfers mee.', L2),
   ALG('Bij een gemiddelde tellen alle cijfers mee, en verdeel je het totaal eerlijk.', L2)]))

# ---- E02 #45 (nrO 38): Jinte, handig vermenigvuldigen met een rond getal ----
L2 = 'Reken eerst met het ronde getal. Bij elke keer neem je dan een beetje te veel. Haal daarna al dat te veel samen eraf.'
E.append((E2, 38, 'Het getal ligt dicht bij een rond getal. Met een rond getal reken je makkelijker.',
  'Reken de som eerst zelf uit. Reken dan elke aanpak uit. Welke komt op hetzelfde uit, en welke gaat het snelst?',
  'Je kind kiest een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.',
  [L('één keer verbeterd', '5 × 100 doen en er 2 afhalen', 'Bij elke keer reken je een beetje te veel. Hoe vaak reken je dat te veel? Dat moet er allemaal af, niet maar één keer.', L2),
   L('herhaald optellen', '98 vijf keer onder elkaar optellen', 'Dat kan, maar het is niet handig: het kost veel stappen. Ligt het getal dicht bij een rond getal?', L2),
   ALG('Reken met het ronde getal, en haal daarna af wat je bij alle keren samen te veel nam.', L2)]))

# ---- E02 #46 (nrO 39): Kim, keer tien en de helft ----
L2 = 'Vijf is de helft van tien. Reken keer tien uit en neem daarvan de helft: dat is hetzelfde als keer vijf.'
E.append((E2, 39, 'Kijk of de aanpak van Kim op hetzelfde uitkomt als de som zelf.',
  'Reken het zelf uit: wat is vijf keer het getal? Reken dan elke aanpak uit: wat Kim deed, en wat de andere antwoorden zeggen. Welke komt op dezelfde uitkomst?',
  'Je kind controleert een handige aanpak: keer tien en dan de helft is hetzelfde als keer vijf.',
  [L('tien eraf', 'Nee, ze moet er 10 van afhalen', 'Keer tien is twee keer zo groot als keer vijf, niet tien meer. Hoeveel moet er dan af?', L2),
   L('verdubbelen', 'Nee, ze moet 360 verdubbelen', 'Keer vijf is minder dan keer tien. Wordt de uitkomst dan groter of kleiner?', L2),
   ALG('Is vijf de helft van tien? Wat betekent dat voor de uitkomst?', L2)]))

# ---- E02 #47 (nrO 40): Lars en de rest bij inpakken ----
L2 = 'Deel, en kijk dan naar de rest. Moet de rest ook mee, dan heb je er nog één extra nodig.'
E.append((E2, 40, 'Bij een deling in een verhaal kijk je daarna terug in het verhaal: wat betekent de uitkomst?',
  'Reken het na: hoeveel gaat er in het aantal dat Lars opschreef? Is daarmee alles ingepakt? Toets dan elke uitleg aan die berekening. Welke klopt?',
  'Je kind kijkt terug in het verhaal: bij inpakken moet alles mee, dus de rest heeft nog een plek nodig.',
  [L('rest vergeten', 'Niets, 14 dozen is precies goed', 'Reken het na: hoeveel gaat er in dat aantal? Is daarmee alles ingepakt?', L2),
   L('keer', 'Hij moest 148 × 10 doen', 'Dan wordt het getal veel groter dan wat er is. Bij verdelen in groepjes past delen. Wat blijft er bij de deling over?', L2),
   ALG('Wat blijft er bij de deling over, en moet dat ook mee?', L2)]))

# ---- E02 #48 (nrO 41): Mees, herhaald optellen ----
L2 = 'Steeds hetzelfde getal optellen is een keersom. Doe het aantal keer het getal: dat is één stap.'
E.append((E2, 41, 'Zoek een aanpak die klopt en die minder stappen kost dan steeds hetzelfde getal optellen.',
  'Reken elke aanpak uit. Komt die op hetzelfde uit als steeds hetzelfde getal optellen? En welke aanpak die klopt, gaat in de minste stappen?',
  'Je kind ziet dat steeds hetzelfde getal optellen hetzelfde is als een keersom.',
  [L('plus', 'Eerst 250 + 4 uitrekenen', 'Dan tel je het aantal keer bij het getal op. Steeds hetzelfde getal optellen geeft veel meer dan het getal plus het aantal keer.', L2),
   L('onder elkaar', 'De som onder elkaar zetten met een streep', 'Dat kan, maar het is niet handig: je telt dan nog steeds alles op. Het kan in één stap.', L2),
   ALG('Steeds hetzelfde getal optellen: welke som doet dat in één stap?', L2)]))

# ---- E02 #49 (nrO 42): Noor, keersom splitsen ----
L2 = 'Splits het aantal keer in een makkelijk stuk: de helft ervan. Reken die keersom uit en verdubbel daarna de uitkomst.'
E.append((E2, 42, 'Zoek een aanpak die klopt en die sneller gaat dan steeds hetzelfde getal optellen.',
  'Reken elke aanpak uit. Komt die op hetzelfde uit als steeds hetzelfde getal optellen? En welke aanpak die klopt, gaat het snelst?',
  'Je kind kiest een handige aanpak voor een keersom: splitsen in een makkelijke keersom en dan verdubbelen.',
  [L('plus', '25 en 8 bij elkaar optellen', 'Dan tel je het aantal keer bij het getal op. Steeds hetzelfde getal optellen is een keersom. Komt dit daar in de buurt?', L2),
   L('te veel eraf', '25 × 10 doen en er 2 afhalen', 'Met tien keer neem je twee hele keren te veel. Haal je dan twee af, of twee keer het getal?', L2),
   ALG('Kun je het aantal keer splitsen in een makkelijke keersom?', L2)]))

# ---- E02 #50 (nrO 43): Nout, schatting als controle ----
L2 = 'Rond allebei de getallen af op honderdtallen: kijk naar de tientallen, vijf of meer gaat naar boven. Reken de schatting na. Ligt het antwoord daar ver vanaf, dan is er waarschijnlijk een rekenfout: reken de som opnieuw uit.'
E.append((E2, 43, 'Een schatting met ronde getallen is een controle. Ligt het antwoord dicht bij de schatting?',
  'Rond allebei de getallen af op honderdtallen: kijk naar de tientallen, vijf of meer gaat naar boven. Reken de schatting zelf na. Hoe ver ligt het antwoord van Nout ervan af? Bekijk elke aanpak: welke hoort bij wat je ziet?',
  'Je kind gebruikt een schatting als controle: ligt het antwoord ver van de schatting, dan reken je opnieuw.',
  [L('schatting aangepast', 'De schatting aanpassen naar 500', 'Reken de schatting na met ronde getallen. Klopte die? Dan ligt de fout niet in de schatting.', L2),
   L('laten staan', 'Het antwoord 505 gewoon laten staan', 'Het antwoord ligt ver van de schatting af. Dat is een teken dat er iets mis is gegaan.', L2),
   ALG('Ligt het antwoord dicht bij de schatting? Zo niet, waar zit dan de fout?', L2)]))

# ---- E02 #51 (nrO 44) en #57 (nrO 50): kilometer en meter ----
L2 = 'Eén kilometer is duizend meter. Doe het aantal kilometer keer duizend: dat is het aantal meter.'
H1_KM = 'Je controleert een omrekening van kilometer naar meter. Past het getal in meters bij de afstand?'   # les 264: geen groter/kleiner (bij #57 blijft dan alleen het antwoord over)
E.append((E2, 44, H1_KM,
  'Hoeveel meter is één kilometer? Reken uit hoeveel meter de tocht dan ongeveer is. Toets elke uitleg aan dat getal: welke klopt?',
  'Je kind controleert een omrekening met een bekend getal: één kilometer is duizend meter.',
  [L('één stap', 'Het moet 320 meter zijn', 'Reken het na: één kilometer is al duizend meter. Is dit dan genoeg voor de hele tocht?', L2),
   L('komma weg', 'Het klopt, je haalt gewoon de komma weg', 'De komma weghalen is geen omrekenen. Hoeveel meter gaan er in één kilometer?', L2),
   ALG('Eén kilometer is al duizend meter. Hoeveel meter is de tocht dan ongeveer?', L2)]))
E.append((E2, 50, H1_KM,
  'Hoeveel meter is één kilometer? Reken uit hoeveel meter de weg naar school dan ongeveer is. Toets elke uitleg aan dat getal: welke klopt?',
  'Je kind controleert een omrekening met een bekend getal: één kilometer is duizend meter.',
  [L('komma weg', 'Het klopt, want je zet de komma weg', 'De komma weghalen is geen omrekenen. Hoeveel meter gaan er in één kilometer?', L2),
   L('nog kleiner', 'Het moet 25 meter zijn', 'Dat is nog minder. Een kilometer is duizend meter: worden het in meters meer of minder?', L2),
   ALG('Eén kilometer is al duizend meter. Hoeveel meter is de weg naar school dan ongeveer?', L2)]))

# ---- E02 #52 (nrO 45): Roos, splitsen ----
L2 = 'Bij splitsen reken je elk stuk uit en tel je de uitkomsten bij elkaar op. Pas dan heb je de hele keersom.'
E.append((E2, 45, 'Bij splitsen reken je elk stuk apart uit. Wat doe je daarna met de stukken?',
  'Reken het zelf uit: wat zijn de twee stukken, en wat is de hele keersom? Vergelijk dat met wat Roos opschreef. Toets dan elke uitleg: welke klopt?',
  'Je kind ziet dat je bij splitsen alle stukken weer bij elkaar optelt.',
  [L('getal uit de som', 'Ze moest 140 en 24 optellen', 'Dan tel je een getal uit de som erbij, niet de uitkomst van het kleine stuk. Hoeveel is het kleine stuk echt?', L2),
   L('niet splitsen', 'Ze had niet mogen splitsen', 'Splitsen is juist een handige aanpak. Heeft Roos alle stukken gebruikt?', L2),
   ALG('Heeft Roos alle stukken van de keersom bij elkaar opgeteld?', L2)]))

# ---- E02 #53 (nrO 46): Sam, doortellen ----
L2 = 'Liggen de getallen dicht bij elkaar? Tel dan door van het kleine getal naar het grote. Hoeveel stappen zijn dat?'
E.append((E2, 46, 'Zoek een aanpak die klopt en die zonder lenen kan.',
  'Reken elke aanpak uit en vergelijk de uitkomsten. Welke aanpak geeft het verschil tussen de twee getallen, en kost de minste stappen?',
  'Je kind ziet dat je bij twee getallen die dicht bij elkaar liggen, het verschil handig vindt door door te tellen.',
  [L('opgeteld', '1000 en 998 bij elkaar optellen', 'Bij elkaar optellen geeft geen verschil. Kijk welk teken er tussen de getallen staat.', L2),
   L('stuk erbij', 'Eerst 900 eraf en dan 98 erbij', 'Als je een getal in stukken afhaalt, moeten alle stukken eraf. Gaat er bij deze aanpak een stuk bij?', L2),
   ALG('Liggen de getallen dicht bij elkaar? Hoeveel moet je dan doortellen?', L2)]))

# ---- E02 #54 (nrO 47): Sanne, via een rond getal ----
L2 = 'Rekenen met een rond getal is handig. Neem je eerst een beetje te veel, haal dat er daarna weer af.'
E.append((E2, 47, 'Kijk of de aanpak van Sanne op hetzelfde uitkomt als de som zelf.',
  'Reken de som zelf uit, en reken ook na wat Sanne doet. Komt Sanne daarop uit? Kijk dan welke uitleg past bij wat je ziet.',
  'Je kind controleert een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.',
  [L('erbij in plaats van eraf', 'Nee, ze moet er 2 bij optellen', 'Sanne rekende met een getal dat iets te groot is. Moet dat stukje er dan bij, of eraf?', L2),
   L('alleen onder elkaar', 'Nee, je mag alleen onder elkaar rekenen', 'Onder elkaar rekenen kan, maar je mag ook een handige aanpak kiezen. Klopt de uitkomst van Sanne?', L2),
   ALG('Komt de aanpak van Sanne op hetzelfde uit als de som zelf?', L2)]))

# ---- E02 #55 (nrO 48): Tim, via een rond getal ----
L2 = 'Neem het ronde getal dat vlak bij het getal ligt. Tel dat erbij, en haal daarna weg wat je te veel nam.'
E.append((E2, 48, 'Het getal ligt dicht bij een rond getal. Met een rond getal reken je makkelijker.',
  'Reken de som zelf uit, en reken daarna elke aanpak uit. Welke aanpak komt op hetzelfde uit?',
  'Je kind kiest een handige aanpak: rekenen met een rond getal en daarna verbeteren wat je te veel nam.',
  [L('te veel erbij', 'Eerst 100 erbij, dan 1 erbij', 'Met het ronde getal komt er al iets te veel bij. Moet dat stukje er dan nog bij, of eraf?', L2),
   L('ander rond getal', 'Eerst 90 erbij, dan 9 eraf', 'Reken het na: komt deze aanpak op hetzelfde uit als de som? Bij een kleiner rond getal tel je te weinig op. Moet het stukje er dan bij of eraf?', L2),
   ALG('Neem een rond getal, en verbeter daarna wat je te veel of te weinig nam.', L2)]))

# ---- E02 #56 (nrO 49): Lisa en de rest bij vervoer ----
L2 = 'Deel, en kijk dan naar de rest. Moet de rest ook mee, dan heb je er nog één extra nodig.'
E.append((E2, 49, 'Bij een deling in een verhaal kijk je daarna terug in het verhaal: wat betekent de uitkomst?',
  'Reken het na: hoeveel passen er in het aantal dat Lisa opschreef? Kan iedereen dan mee? Toets dan elke uitleg aan die berekening. Welke klopt?',
  'Je kind kijkt terug in het verhaal: iedereen moet mee, dus wie overblijft heeft nog een plek nodig.',
  [L('keer', 'Ze had 50 × 12 moeten doen', 'Dan wordt het getal veel groter dan het aantal dat meegaat. Bij verdelen in groepjes past delen. Wat blijft er bij de deling over?', L2),
   L('één te veel', 'Er zijn 6 busjes nodig', 'Reken het na: kan iedereen al mee met één minder dan dit aantal?', L2),
   ALG('Wat blijft er bij de deling over, en moet dat ook mee?', L2)]))

# ---- V02 #1: totaal uit een gemiddelde ----
H2 = 'Gemiddeld betekent: ieder evenveel. Doe het aantal in de groep keer wat ieder gemiddeld heeft.'
E.append((V2, 1, 'Gemiddeld betekent: als iedereen in de groep er evenveel had.', H2,
  'Je kind rekent terug van een gemiddelde naar het totaal: het aantal keer het gemiddelde.',
  [L('opgeteld', '13 knikkers', 'Dan tel je het aantal in de groep en het gemiddelde bij elkaar op. Maar elk van hen heeft er gemiddeld evenveel: hoeveel zijn dat er samen?', H2),
   L('gedeeld', '1,6 knikkers', 'Dat is minder dan wat ieder gemiddeld heeft. Samen hebben ze er juist meer.', H2),
   ALG('Ieder heeft er gemiddeld evenveel. Hoeveel zijn dat er samen?', H2)]))

# ---- V02 #2: gemiddeld per dag over twee dagen ----
H2 = 'Tel de aantallen van de twee dagen bij elkaar op: dat is het totaal. Verdeel dat eerlijk: deel het totaal door het aantal dagen.'
E.append((V2, 2, 'Gemiddeld per dag: als er elke dag evenveel hadden gezwommen, hoeveel was dat dan per dag?', H2,
  'Je kind rekent een gemiddelde uit: alles optellen en delen door het aantal dagen.',
  [L('totaal', '600 mensen', 'Dat is het totaal van het weekend. Gemiddeld per dag is dat totaal eerlijk verdeeld over de dagen.', H2),
   L('verschil', '40 mensen', 'Dat is het verschil tussen de twee dagen. Een gemiddelde ligt tussen de twee aantallen in.', H2),
   ALG('Tel alles op en verdeel het eerlijk over de dagen.', H2)]))

# ---- V02 #3: gemiddeld cijfer met aantallen ----
H2 = 'Reken uit hoeveel punten alle kinderen samen hebben: elk cijfer keer het aantal kinderen met dat cijfer, en dat bij elkaar. Deel dat door het aantal kinderen.'
E.append((V2, 3, 'Bij een gemiddelde tellen alle cijfers mee, ook als hetzelfde cijfer vaak voorkomt.', H2,
  'Je kind rekent een gemiddelde uit als cijfers vaker voorkomen: elk cijfer telt zo vaak mee als het voorkomt.',
  [L('totaal', '140', 'Dat is het totaal van alle cijfers samen. Verdeel het nog eerlijk over alle kinderen.', H2),
   L('elk cijfer één keer', '21', 'Dan telt elk cijfer maar één keer mee. Elk cijfer telt zo vaak mee als er kinderen zijn met dat cijfer.', H2),
   ALG('Elk cijfer telt zo vaak mee als het voorkomt. Deel het totaal door het aantal kinderen.', H2)]))

# ---- V02 #4: gemiddelde afstand per dag ----
H2 = 'Tel alle afstanden bij elkaar op: dat is het totaal. Deel het totaal door het aantal dagen.'
E.append((V2, 4, 'Gemiddeld per dag: als ze elke dag even ver had gefietst, hoe ver was dat dan?', H2,
  'Je kind rekent een gemiddelde uit: alle afstanden optellen en delen door het aantal dagen.',
  [L('totaal', '16 km', 'Dat is het totaal van alle dagen. Verdeel het nog eerlijk over de dagen.', H2),
   L('langste dag', '5 km', 'Dat is de langste dag. Een gemiddelde ligt tussen de kortste en de langste dag in.', H2),
   ALG('Tel alle afstanden op en deel door het aantal dagen.', H2)]))

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
D = {'batch': 'batch3', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 3 = GET-E02 #37–#57 + GET-V02 #1–#4: meerkeuze (aanpak kiezen en beoordelen, controleren; gemiddelde)). "
                "Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); 'nr' en 'somtype' "
                "houdt scripts/sync_hint_keys.py bij. foutHints: per foute optie een letterlijke regel (de hele optietekst) met een vaste tekst, laag 1 'tekst' en "
                "laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
