#!/usr/bin/env python3
"""Schrijft hints/batch2.json (G8 batch 2: GET-E02 #12–#36 = 25 somtypes van één meerkeuze-item met tekstopties: aanpak kiezen,
een antwoord controleren, de fout in een aanpak vinden). 8 okt 2026, Oefeningen. Formaat als hints/make_batch1.py.
Data: live g8 (build 03:08 + sync 15:05). Lessen: hints/lessen_g8.md (G4–G7 lessen 1–232 + G8-bankregels).
Analyse en checks: /workspace/g8work/b2/check.py op de zandbak /workspace/g8work/b2/sbx.sh (verse kopie van live).
Keuzes:
- Elke foute optie krijgt een letterlijke regel: de hele optietekst (fout_regels lett_past: met een cijfer als heel token, '€…' exact),
  zo pakt elke regel precies één optie (les 160/161; check.py rekent het per optie na). 'andere fout' als laatste, met een tekst die voor
  elke optie klopt.
- H1 = waar de vraag over gaat, H2 = de aanpak zelf (kennisvraag: H2 mag het goede antwoord aanwijzen, les 144). Geen cijfers, geen
  optieletters, geen plekwoorden (les 193: 'het cijfer helemaal rechts'), geen woorden uit de [ding]-plekken van de kop (les 147),
  geen zin die een bewerking uitsluit (les 217), geen verwijzing naar een andere strategie (les 231), geen tekst die begint met 'zoveel' (les 197).
- Laag 2 ('tekstSterker'): de aanpak in stappen (H2) of een eigen vervolgstap.
LET OP: alleen voor de eerste versie. Na een sync of rebuild NIET opnieuw draaien, ook niet met --force: patch in place met hints/patch_batch2.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B2_OUT', f'{BASE}/hints/batch2.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch2.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch2.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch2.json bestaat al: patch in place (hints/patch_batch2.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
L = R   # letterlijke regel: 'regel' is de hele tekst van de foute optie
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
E2 = 'G8-GET-E02'

# ---- #12 (nrO 5): hoeveel graden warmer ----
H2 = 'Het verschil tussen twee getallen vind je door het kleinste van het grootste af te halen.'
E.append((E2, 5, 'Hoeveel graden warmer: de vraag gaat over het verschil tussen de twee temperaturen.', H2,
  'Je kind kiest hoe je een verschil uitrekent: hoeveel graden is het warmer geworden?',
  [L('getal overgenomen', 'Neem het getal 11 over als verschil', "Dat is de temperatuur van 's middags. Hoeveel graden is dat meer dan 's ochtends?", H2),
   L('opgeteld', 'Tel 3 en 11 bij elkaar op', "Bij elkaar optellen geeft geen verschil. Hoeveel graden is het 's middags meer dan 's ochtends?", H2),
   ALG('Je zoekt het verschil tussen de twee temperaturen.', H2)]))

# ---- #13 (nrO 6): klopt het antwoord van Bas? ----
H2 = "Rond de prijs af op hele euro's. Doe dat keer het aantal. Ligt het antwoord van Bas daar dichtbij?"
E.append((E2, 6, 'Schat het antwoord met ronde getallen. Dan zie je snel of het antwoord van Bas kan kloppen.', H2,
  'Je kind controleert een antwoord met een schatting: ronde prijs keer het aantal.',
  [L('komma vergeten', 'Het klopt, want 6 × 1,99 is bijna 120', "Kijk naar de komma in de prijs. Rond de prijs af op hele euro's en doe dat keer het aantal: kom je dan ook boven de honderd euro?", H2),
   L('tien keer te groot', 'Het antwoord moet ongeveer €1200 zijn', "Dat is nog veel meer. Rond de prijs af op hele euro's en doe dat keer het aantal: hoeveel euro is dat ongeveer?", H2),
   ALG("Rond de prijs af op hele euro's en doe dat keer het aantal.", H2)]))

# ---- #14 (nrO 7): de score ----
H2 = 'Doe het aantal doelpunten keer wat één doelpunt oplevert. Haal daarna af wat de missers kosten.'
E.append((E2, 7, 'Elk doelpunt levert evenveel op. Elke misser kost iets.', H2,
  'Je kind kiest hoe je een score uitrekent: doelpunten keer wat ze opleveren, dan de missers eraf.',
  [L('plus in plaats van keer', 'Doelpunten plus 3, dan het aantal missers eraf.', 'Elk doelpunt levert evenveel op. Heb je dat voor elk doelpunt meegeteld, of maar één keer?', H2),
   L('missers erbij', 'Doelpunten maal 3, dan het aantal missers erbij.', 'Een misser kost iets. Komt dat bij de score of gaat het eraf?', H2),
   ALG('Reken eerst uit wat alle doelpunten samen opleveren. Wat gebeurt er dan met de missers?', H2)]))

# ---- #15 (nrO 8): Bram ----
H2 = 'Doe het aantal groepen keer het aantal in één groep: dat is het totaal. Is dat veel meer dan het antwoord van Bram?'
E.append((E2, 8, 'Hoeveel zitten er in één groep? En hoeveel van die groepen heeft Bram?', H2,
  'Je kind controleert of een antwoord kan: heeft één groep er al zoveel, dan hebben alle groepen samen er veel meer.',
  [L('opgeteld', 'Niets, 12 en 15 samen is inderdaad 27', 'Elke groep heeft er evenveel. Is het totaal dan het aantal groepen plus het aantal in één groep?', H2),
   L('gedeeld', 'Hij had 12 : 15 moeten doen', 'Met meer groepen wordt het totaal groter. Past delen daarbij?', H2),
   ALG('Hoeveel zitten er in één groep, en hoeveel groepen zijn er? Wat betekent dat voor het totaal?', H2)]))

# ---- #16 (nrO 9): hoe lang duurt de reis ----
H2 = 'Spring eerst van de vertrektijd naar het volgende hele uur. Spring dan verder naar de aankomsttijd. Tel de sprongen bij elkaar op.'
E.append((E2, 9, 'Een uur heeft zestig minuten, geen honderd. Daarom reken je met tijden in sprongen.', H2,
  'Je kind kiest een handige aanpak voor een tijdsduur: eerst naar het hele uur, dan verder.',
  [L('minuten afgetrokken', 'Trek 35 van 10 af en tel de uren erbij.', 'De minuten bij aankomst zijn minder dan bij vertrek. Zo aftrekken loopt vast, want een uur heeft zestig minuten. Spring liever eerst naar het volgende hele uur.', H2),
   L('tijden opgeteld', 'Tel de twee tijden bij elkaar op.', 'Twee tijden bij elkaar optellen geeft geen duur. Hoe lang is het van de vertrektijd tot de aankomsttijd?', H2),
   ALG('Spring van de vertrektijd naar het volgende hele uur, en dan naar de aankomsttijd.', H2)]))

# ---- #17 (nrO 10): Fleur ----
H2 = 'Alle zijden bij elkaar optellen geeft de omtrek: de lengte rondom. Vierkante meters gaan over de oppervlakte: lengte keer breedte.'
E.append((E2, 10, 'Vierkante meters gaan over de oppervlakte. Wat rekende Fleur uit: de oppervlakte of de lengte rondom?', H2,
  'Je kind ziet het verschil tussen omtrek (de lengte rondom) en oppervlakte (lengte keer breedte).',
  [L('omtrek goedgekeurd', 'Niets, 70 vierkante meter klopt', 'Fleur telde alle zijden bij elkaar op. Is dat de oppervlakte of de lengte rondom?', H2),
   L('ook de omtrek', 'Ze moest 25 + 10 doen en dat verdubbelen', 'Dat is dezelfde som anders opgeschreven: ook dat geeft de lengte rondom. Vierkante meters gaan over de oppervlakte.', H2),
   ALG('Wat geeft alle zijden bij elkaar optellen: de oppervlakte of de lengte rondom?', H2)]))

# ---- #18 (nrO 11): tegels ----
H2 = 'Denk aan rijen tegels. Hoeveel tegels passen er in één rij, en hoeveel rijen zijn er? Doe die twee keer elkaar.'
E.append((E2, 11, 'De tegels bedekken alles. Je zoekt dus de oppervlakte, niet de lengte rondom.', H2,
  'Je kind kiest hoe je uitrekent hoeveel tegels er nodig zijn: de oppervlakte, lengte keer breedte.',
  [L('lengte plus breedte', 'Lengte en breedte bij elkaar optellen', 'Dan tel je maar één rij langs de lengte en één rij langs de breedte. De tegels moeten alles bedekken: hoeveel rijen tegels passen er?', H2),
   L('omtrek', 'Alle zijden bij elkaar optellen', 'Alle zijden bij elkaar optellen geeft de omtrek: de lengte rondom. Tegels bedekken de oppervlakte.', H2),
   ALG('Tegels bedekken de oppervlakte. Hoeveel rijen zijn er, en hoeveel tegels in één rij?', H2)]))

# ---- #19 (nrO 12): Joep en het hek ----
H2 = 'De omtrek is alle zijden bij elkaar opgeteld. Lengte keer breedte is de oppervlakte. Wat rekende Joep uit?'
E.append((E2, 12, 'Een hek staat rondom. Je zoekt dus de omtrek: de lengte rondom.', H2,
  'Je kind ziet het verschil tussen omtrek (de lengte rondom) en oppervlakte (lengte keer breedte).',
  [L('twee zijden', 'Hij had 8 + 5 moeten doen', 'Dat zijn maar twee zijden. Een hek gaat helemaal rondom, langs alle vier de zijden.', H2),
   L('oppervlakte verdubbeld', 'Hij had 8 × 5 × 2 moeten doen', 'Lengte keer breedte blijft een oppervlakte, ook als je het verdubbelt. Voor een hek tel je de zijden rondom bij elkaar op.', H2),
   ALG('Een hek staat rondom. Zoekt Joep de omtrek of de oppervlakte?', H2)]))

# ---- #20 (nrO 13): Rik en de broek ----
H2 = 'Reken uit hoeveel euro de korting is: deel de prijs door honderd en doe dat keer het procent. Haal dat bedrag van de prijs af. Komt er hetzelfde uit als bij Rik?'
E.append((E2, 13, 'Procent betekent: van elke honderd. Hoeveel euro is de korting bij deze prijs?', H2,
  'Je kind ziet het verschil tussen een procent en een bedrag in euro.',
  [L('procent als euro', 'Niets, 10 procent van €40 is €10', 'Reken het na: deel de prijs door honderd en doe dat keer het procent. Is de korting echt zoveel euro?', H2),
   L('erbij', 'Hij moest €10 bij de prijs optellen', 'De broek wordt goedkoper. Gaat de korting eraf of komt die erbij?', H2),
   ALG('Reken uit hoeveel euro de korting is, en haal dat van de prijs af.', H2)]))

# ---- #21 (nrO 14): Milou en de jas ----
H2 = 'De korting is het bedrag dat eraf gaat. De nieuwe prijs is de oude prijs min de korting. Welke van de twee rekende Milou uit?'
E.append((E2, 14, 'Kijk goed wat Milou uitrekende: de korting of de nieuwe prijs?', H2,
  'Je kind ziet het verschil tussen de korting en de nieuwe prijs.',
  [L('procent van de uitkomst', 'Ze moest 25 procent van 15 nemen', 'Het procent hoort bij de oude prijs. Waarvan neem je het procent?', H2),
   L('nieuwe prijs', 'De jas kost nu €35', 'Reken het na. Het procent is geen bedrag in euro: hoeveel euro is de korting? Haal die van de oude prijs af. Komt daar dit bedrag uit?', H2),
   ALG('Is wat Milou uitrekende de korting of de nieuwe prijs?', H2)]))

# ---- #22 (nrO 15): Daan en de rijst ----
H2 = 'Hoeveel keer zoveel mensen worden het? Dan heb je evenveel keer zoveel rijst nodig. Deed Daan dat?'
E.append((E2, 15, 'Bij een recept hoort bij meer mensen ook meer rijst: hoeveel keer zoveel mensen worden het?', H2,
  'Je kind controleert een aanpak met verhoudingen: twee keer zoveel mensen is twee keer zoveel rijst.',
  [L('mensen erbij', 'Nee, hij moest 304 gram nemen', 'Dan krijgt elke extra persoon maar één gram rijst. Hoeveel keer zoveel mensen worden het, en hoeveel rijst hoort daarbij?', H2),
   L('mensen bij de grammen', 'Nee, hij moest 300 + 8 nemen', 'Dan tel je het aantal mensen bij de grammen op. Hoeveel keer zoveel mensen worden het?', H2),
   ALG('Hoeveel keer zoveel mensen worden het? Hoort daar evenveel keer zoveel rijst bij?', H2)]))

# ---- #23 (nrO 16): rijst voor meer mensen ----
H2 = 'Deel de rijst door het aantal mensen van het recept: dat is voor één persoon. Doe dat keer het aantal mensen waarvoor je kookt.'
E.append((E2, 16, 'Reken eerst uit hoeveel rijst één persoon nodig heeft.', H2,
  'Je kind kiest de aanpak via één: eerst hoeveel rijst voor één persoon, dan voor iedereen.',
  [L('mensen bij de grammen', 'Tel 200 en 6 bij elkaar op', 'Dan tel je mensen bij grammen op. Hoeveel rijst is er voor één persoon?', H2),
   L('hele recept per persoon', 'Doe 200 keer 6', 'Dan krijgt elke persoon de rijst van het hele recept. Het recept is al voor meer mensen: hoeveel is er voor één persoon?', H2),
   ALG('Hoeveel rijst heeft één persoon nodig?', H2)]))

# ---- #24 (nrO 17): de schatting van Anne ----
H2 = 'Reken de schatting na met ronde getallen. Kijk dan hoe ver het precieze antwoord ervan af ligt. Is dat weinig, dan past de schatting.'
E.append((E2, 17, 'Een schatting is ongeveer. Ligt het precieze antwoord dicht bij de schatting?', H2,
  'Je kind beoordeelt een schatting: een schatting hoeft niet precies te kloppen, wel ongeveer.',
  [L('nul vergeten', 'Haar schatting was fout, want 4 × 2000 is 800', 'Reken het na en tel de nullen. Hoeveel nullen heeft het ronde getal, en hoeveel heeft de uitkomst?', H2),
   L('schatting als antwoord', 'Ze rekende fout, want het moet 8000 zijn', 'Een schatting is ongeveer, niet precies. Het precieze antwoord mag een beetje van de schatting afwijken.', H2),
   ALG('Ligt het precieze antwoord dicht bij de schatting?', H2)]))

# ---- #25 (nrO 18): Eva controleert een deling ----
H2 = 'Gedeeld door en keer horen bij elkaar. Doe het antwoord keer het getal waardoor je deelt. Komt het getal eruit dat je deelde?'
E.append((E2, 18, 'Een deling controleer je met de omgekeerde som.', H2,
  'Je kind controleert een deelsom met de omgekeerde keersom.',
  [L('overschrijven', 'Het antwoord nog een keer overschrijven', 'Overschrijven controleert niets: een fout schrijf je zo ook over. Welke som is het omgekeerde van gedeeld door?', H2),
   L('plus', '63 + 7 uitrekenen en kijken of het klopt', 'Plus is niet het omgekeerde van gedeeld door. Welke som hoort andersom bij gedeeld door?', H2),
   ALG('Wat is het omgekeerde van gedeeld door?', H2)]))

# ---- #26 (nrO 19): Fenna controleert een plussom ----
H2 = 'Min is het omgekeerde van plus. Haal van de uitkomst een van de twee getallen af. Komt het andere getal eruit?'
E.append((E2, 19, 'Een plussom controleer je het best met de omgekeerde som.', H2,
  'Je kind controleert een plussom met de omgekeerde minsom.',
  [L('nog een keer hetzelfde', 'De som nog een keer precies zo uitrekenen', 'Dan maak je misschien dezelfde fout nog eens. Met de omgekeerde som controleer je op een andere manier.', H2),
   L('nog meer erbij', '412 + 178 uitrekenen', 'Nog meer erbij doen controleert de plussom niet. Wat is het omgekeerde van plus?', H2),
   ALG('Wat is het omgekeerde van plus?', H2)]))

# ---- #27 (nrO 20): deelbaar door vijf ----
H2 = 'Kijk naar het cijfer helemaal rechts, bij de eenheden. Op welke cijfers eindigen de uitkomsten van die tafel?'
E.append((E2, 20, 'Schrijf een paar uitkomsten uit de tafel van dat getal op. Wat zie je steeds terugkomen?', H2,
  'Je kind weet hoe je ziet of een getal in de tafel van vijf zit: kijk naar het cijfer van de eenheden.',
  [L('cijfer links', 'Kijk of het eerste cijfer 0 of 5 is', 'De uitkomsten van de tafel beginnen met allerlei cijfers. Kijk naar het cijfer helemaal rechts, bij de eenheden.', H2),
   L('even', 'Kijk of het getal even is', 'In die tafel zitten ook oneven getallen, en niet elk even getal zit erin. Kijk naar het cijfer helemaal rechts.', H2),
   ALG('Kijk naar het cijfer helemaal rechts. Op welke cijfers eindigt de tafel?', H2)]))

# ---- #28 (nrO 21): even ----
H2 = 'Kijk naar het cijfer helemaal rechts, bij de eenheden. Is dat cijfer even, dan is het hele getal even.'
E.append((E2, 21, 'Even getallen zitten in de tafel van twee: je kunt ze eerlijk in tweeën verdelen.', H2,
  'Je kind weet hoe je ziet of een getal even is: kijk naar het cijfer van de eenheden.',
  [L('cijfer links', 'Kijk of het eerste cijfer 0, 2, 4, 6 of 8 is.', 'Het cijfer helemaal links zegt niet of een getal even is. Kijk naar het cijfer helemaal rechts.', H2),
   L('tafel van drie', 'Kijk of je het getal door 3 kunt delen.', 'Even betekent: in de tafel van twee, niet in de tafel van drie.', H2),
   ALG('Even betekent: in de tafel van twee. Kijk naar het cijfer helemaal rechts.', H2)]))

# ---- #29 (nrO 22): Ruben en de grafiek ----
H2 = 'Onder elke staaf staat bij welke dag die hoort. Lees dat eerst, en kijk dan pas hoe hoog de staaf is.'
E.append((E2, 22, 'Ruben keek bij de verkeerde dag. Hoe weet je bij welke dag een staaf hoort?', H2,
  'Je kind leert een grafiek nauwkeurig aflezen: eerst kijken bij welke dag een staaf hoort.',
  [L('hoogste staaf', 'Altijd de hoogste staaf kiezen', 'De hoogste staaf hoort bij één dag, en dat hoeft woensdag niet te zijn. Hoe zie je bij welke dag een staaf hoort?', H2),
   L('schaal opgeteld', 'De getallen links bij elkaar optellen', 'De getallen langs de kant zijn de schaal om af te lezen. Hoe zie je bij welke dag een staaf hoort?', H2),
   ALG('Hoe zie je bij welke dag een staaf hoort?', H2)]))

# ---- #30 (nrO 23): totaal van de week ----
H2 = 'Lees bij elke dag af hoe hoog de staaf is. Tel al die aantallen bij elkaar op.'
E.append((E2, 23, 'Het totaal van de week is alle dagen bij elkaar.', H2,
  'Je kind leest een staafgrafiek af en telt de waarden van alle dagen op.',
  [L('hoogste keer de week', 'Lees de hoogste staaf af en doe die keer 7', 'Dan doe je alsof het elke dag even druk was als op de drukste dag. Lees elke staaf apart af.', H2),
   L('verschil', 'Trek de laagste staaf van de hoogste af', 'Dat is het verschil tussen de drukste en de rustigste dag, niet het totaal.', H2),
   ALG('Het totaal van de week is alle dagen bij elkaar.', H2)]))

# ---- #31 (nrO 24): korting ----
H2 = 'Reken het procent uit van de oude prijs: dat is de korting in euro. Haal die van de oude prijs af.'
E.append((E2, 24, 'Korting gaat van de prijs af. Waarvan neem je het procent?', H2,
  'Je kind kiest hoe je een prijs met korting uitrekent: het procent van de prijs, en dat eraf.',
  [L('procent van de korting', 'Bereken 25 procent van de korting en trek dat eraf.', 'De korting weet je nog niet: die reken je juist uit. Het procent hoort bij de prijs.', H2),
   L('erbij', 'Bereken 25 procent van de prijs en tel dat erbij op.', 'Met korting wordt het goedkoper. Gaat de korting eraf of komt die erbij?', H2),
   ALG('Neem het procent van de prijs. Gaat dat eraf of erbij?', H2)]))

# ---- #32 (nrO 25): procent van de leerlingen ----
H2 = 'Reken uit hoeveel leerlingen één procent is: deel het aantal leerlingen door honderd. Doe dat keer het procent.'
E.append((E2, 25, 'Procent betekent: van elke honderd. Alle leerlingen samen zijn honderd procent.', H2,
  'Je kind kiest hoe je een procent van een aantal uitrekent: eerst één procent, dan keer het procent.',
  [L('procent als uitkomst', 'Deel 15 door 100 en doe dat keer 40 procent', 'Kijk naar het woord procent aan het eind: zo krijg je weer een procent, geen aantal leerlingen. Hoeveel leerlingen is één procent?', H2),
   L('afgetrokken', 'Trek 15 van 40 af', 'Het procent is geen aantal leerlingen. Hoeveel leerlingen is één procent van alle leerlingen?', H2),
   ALG('Hoeveel leerlingen is één procent? Doe dat keer het procent.', H2)]))

# ---- #33 (nrO 26): kilogram en gram ----
H2 = 'Eén kilogram is duizend gram. Reken de kilogrammen om naar grammen, dan kun je delen.'
E.append((E2, 26, 'De ene maat staat in kilogram, de andere in gram. Maak eerst van allebei dezelfde maat.', H2,
  'Je kind ziet dat je eerst dezelfde maat nodig hebt: kilogram omrekenen naar gram.',
  [L('direct delen', 'Deel 2,5 direct door 500.', 'Kilogram en gram zijn verschillende maten. Maak eerst van allebei dezelfde maat.', H2),
   L('verkeerd omgerekend', 'Reken 500 gram om naar 5 kg.', 'Reken het na: duizend gram is één kilogram. Dan is dit minder dan één kilogram.', H2),
   ALG('Maak eerst van allebei dezelfde maat: één kilogram is duizend gram.', H2)]))

# ---- #34 (nrO 27): fietsen ----
H2 = 'Deel de kilometers door het aantal uren. Dan weet je hoeveel kilometer je in één uur fietst.'
E.append((E2, 27, 'Elk uur fiets je even ver. Hoeveel kilometer is dat in één uur?', H2,
  'Je kind kiest de aanpak via één: hoeveel kilometer in één uur.',
  [L('keer', 'Vermenigvuldig 24 met 2', 'Dan krijg je de kilometers van meer uren, niet van één uur.', H2),
   L('uren eraf', 'Trek 2 van 24 af', 'Je haalt dan uren van kilometers af. Elk uur fiets je even ver: hoeveel kilometer is dat in één uur?', H2),
   ALG('Elk uur fiets je even ver. Hoeveel kilometer is dat in één uur?', H2)]))

# ---- #35 (nrO 28): koekjes verdelen ----
H2 = 'Deel het aantal koekjes door het aantal mensen. Het hele getal is wat ieder krijgt. Wat overblijft is de rest.'
E.append((E2, 28, 'Eerlijk verdelen is delen. Soms blijft er iets over.', H2,
  'Je kind kiest hoe je eerlijk verdeelt: delen, en kijken wat er overblijft.',
  [L('naar boven', 'Deel 50 door 8 en rond naar boven af', 'Naar boven afronden geeft koekjes die er niet zijn. De vraag wil ook weten hoeveel er overblijven: kijk naar de rest.', H2),
   L('afgetrokken', 'Trek 8 van 50 af, dat is het antwoord', 'Dan krijgt ieder maar één koekje. Bij eerlijk verdelen deel je het aantal koekjes door het aantal mensen.', H2),
   ALG('Eerlijk verdelen is delen. Hoeveel krijgt ieder, en wat blijft er over?', H2)]))

# ---- #36 (nrO 29): volle dozen ----
H2 = 'Deel het totaal door wat er in één doos past. Het hele getal is het aantal volle dozen. De rest past niet in een volle doos.'
E.append((E2, 29, 'Alleen dozen die helemaal vol zijn tellen mee. Hoe vaak past de inhoud van één doos in het totaal?', H2,
  'Je kind kiest hoe je uitrekent hoeveel volle dozen het worden: delen en alleen het hele getal gebruiken.',
  [L('naar boven', 'Deel 40 door 6 en rond het antwoord naar boven af.', 'Dan tel je een doos mee die niet vol is. De vraag gaat over volle dozen.', H2),
   L('afgetrokken', 'Trek 6 van 40 af en noem dat het aantal dozen.', 'Dan haal je maar één doos eraf. Hoe vaak past de inhoud van één doos in het totaal?', H2),
   ALG('Hoe vaak past de inhoud van één doos in het totaal? Alleen volle dozen tellen.', H2)]))

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
D = {'batch': 'batch2', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 2 = GET-E02 #12–#36: meerkeuze met tekstopties (aanpak kiezen, controleren, fout vinden)). "
                "Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); 'nr' en 'somtype' "
                "houdt scripts/sync_hint_keys.py bij. foutHints: per foute optie een letterlijke regel (de hele optietekst) met een vaste tekst, laag 1 'tekst' en "
                "laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
