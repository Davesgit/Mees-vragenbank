#!/usr/bin/env python3
"""Schrijft hints/batch1.json (G8 batch 1: GET-E02 #1–#11 (schatten en laatste cijfer), GET-E03 #1–#5 (volgorde van bewerkingen),
GET-E04 #1–#8 (breuken: delen door een breuk, deel van een deel, optellen) = 24 somtypes, 317 items). 8 okt 2026, Oefeningen.
Formaat als g7/hints/make_batch6.py. Data: build g8 03:08 (live). Lessen: hints/lessen_g8.md (G4–G7 lessen 1–208 + G8-bankregels).
Analyse en checks: /workspace/g8work/b1/check.py op de zandbak /workspace/g8work/b1/sbx.sh.
Keuzes:
- Schatten (GET-E02 #2–#4, #6–#8, #10, #11): de vijf-of-meer-regel in elke afrondtekst, met het cijfer waar je naar kijkt (bij duizendtallen
  het cijfer van de honderdtallen enz.); elke afrondcombinatie tegen het antwoord (les 129, INFO in check.py); eerst de exacte motorregels
  (precies uitgerekend, × 10, : 10, ± een eenheid), dan 'andere fout' met een tekst die voor elke andere waarde klopt (half afgerond, verkeerde kant).
- Meerkeuze (#5, #9): eerst waarop het antwoord eindigt (H1), dan de grenzen (H2), zoals G4 batch 5: een schatting kan dichter bij een afleider liggen.
- Claudes labels met één vaste tekst, per sleutel nagerekend (les 146/161/191); getallen bij hun rol (les 167), geen plekwoorden (les 193).
- ':' = gedeeld door (G8), vaktermen teller/noemer/gelijknamig met uitleg in dezelfde tekst, geen optieletters, geen cijfers in de teksten.
LET OP: alleen voor de eerste versie. Na een sync of rebuild NIET opnieuw draaien, ook niet met --force: patch in place met hints/patch_batch1.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B1_OUT', f'{BASE}/hints/batch1.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch1.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch1.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch1.json bestaat al: patch in place (hints/patch_batch1.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
def CL(soort, label, tekst, sterker):
    f = T(soort, f'Claudes sleutel: {label}', tekst, None, 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt; vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', label)
    f['tekstSterker'] = sterker; return f
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
E2, E3, E4 = 'G8-GET-E02', 'G8-GET-E03', 'G8-GET-E04'

# ================= GET-E02 #1 (nrO 1): Op welk cijfer eindigt a × b? (open, 53 items) =================
EIND_H2 = 'Reken alleen de eenheden van de twee getallen keer elkaar. Op welk cijfer eindigt die kleine keersom? Daarop eindigt de hele som ook.'
E.append((E2, 1, 'Je hoeft niet de hele som uit te rekenen. Op welk cijfer de uitkomst eindigt, hangt alleen af van de eenheden: het cijfer helemaal rechts in elk getal.',
  EIND_H2, 'Je kind zoekt op welk cijfer een keersom eindigt, zonder de hele som uit te rekenen: alleen de eenheden tellen mee.',
  [CL('opgeteld', 'optellen-ipv-vermenigvuldigen', 'Heb je opgeteld? Er staat een keerteken (×): reken de eenheden keer elkaar.', EIND_H2),
   CL('begincijfer', 'getal-overgenomen', 'Dat is het cijfer waarmee de uitkomst begint. De vraag gaat over het cijfer waarop de uitkomst eindigt: helemaal rechts.', EIND_H2),
   CL('keersom ernaast', 'een-ernaast', 'Dat hoort bij een keersom ernaast. Kijk nog eens welke eenheden er staan, en reken precies die keer elkaar.',
      'Schrijf de eenheden van allebei de getallen op. Reken die twee cijfers keer elkaar: op welk cijfer eindigt dat?'),
   CL('tientallencijfer', 'tafelbuur', 'Dat is het cijfer van de tientallen van de kleine keersom. De uitkomst eindigt op het cijfer helemaal rechts daarvan.',
      'Reken de eenheden van de twee getallen keer elkaar. Krijg je een getal met twee cijfers? Dan eindigt de hele som op het cijfer van de eenheden daarvan.'),
   ALG('Reken alleen de eenheden keer elkaar, en kijk op welk cijfer dat eindigt.', EIND_H2)]))

# ================= GET-E02 schatten met een afrondafspraak (open) =================
def afr(eenheid, kijk):
    return f'Kijk bij elk getal naar het cijfer van de {kijk}. Is dat vijf of meer? Dan rond je naar boven af op {eenheid}. Anders rond je naar beneden af.'
SCHAT_H1 = 'Schatten is ongeveer uitrekenen met ronde getallen. Rond eerst allebei de getallen af op {e}, zoals de vraag zegt. Reken daarna met de afgeronde getallen.'
def som_regels(eenheid, kijk, teken, stap, stapwoord, twee):
    """eenheid: duizendtallen/honderdtallen; stap: 1000/100; stapwoord: 'duizend'/'honderd'; twee: 'tweeduizend'/'tweehonderd'"""
    A = afr(eenheid, kijk)
    reken = 'Tel daarna de twee afgeronde getallen op.' if teken == '+' else 'Haal daarna het afgeronde getal achter het minteken van het andere afgeronde getal af.'
    exact = 'fout = getal1 + getal2' if teken == '+' else 'fout = getal1 - getal2 of getal2 - getal1'
    schrijf = 'Schrijf de twee afgeronde getallen op. ' + reken
    def mis(hoeveel, richting):
        return R(f'{hoeveel} te {richting}', f"fout = antwoord {'+' if richting == 'veel' else '-'} {stap * (2 if hoeveel == twee else 1)}",
                 f'Dat is {hoeveel} te {richting}. Kijk nog eens hoe je elk getal afrondt. {A}', A + ' ' + schrijf)
    return A + ' ' + reken, [
        R('precies uitgerekend', exact, f'Je hebt het precies uitgerekend. Dat is goed gerekend, maar de vraag vraagt een schatting: rond eerst allebei de getallen af op {eenheid}. {A}',
          A + ' ' + schrijf),
        mis(stapwoord, 'veel'), mis(stapwoord, 'weinig'), mis(twee, 'veel'), mis(twee, 'weinig'),
        ALG(f'Rond eerst allebei de getallen af op {eenheid}, en reken dan met de afgeronde getallen. {A}', A + ' ' + schrijf)]
OZ_SOM = 'Je kind schat een {s}: eerst allebei de getallen afronden op {e}, dan met de ronde getallen rekenen.'
h2, fh = som_regels('duizendtallen', 'honderdtallen', '+', 1000, 'duizend', 'tweeduizend')
E.append((E2, 51, SCHAT_H1.format(e='duizendtallen'), h2, OZ_SOM.format(s='plussom', e='duizendtallen'), fh))
h2, fh = som_regels('honderdtallen', 'tientallen', '+', 100, 'honderd', 'tweehonderd')
E.append((E2, 55, SCHAT_H1.format(e='honderdtallen'), h2, OZ_SOM.format(s='plussom', e='honderdtallen'), fh))
h2, fh = som_regels('duizendtallen', 'honderdtallen', '-', 1000, 'duizend', 'tweeduizend')
E.append((E2, 56, SCHAT_H1.format(e='duizendtallen'), h2, OZ_SOM.format(s='minsom', e='duizendtallen'), fh))
h2, fh = som_regels('duizendtallen', 'honderdtallen', '+', 1000, 'duizend', 'tweeduizend')
E.append((E2, 2, SCHAT_H1.format(e='duizendtallen'), h2, 'Je kind schat een totaal: eerst allebei de getallen afronden op duizendtallen, dan optellen.', fh))

# keersommen: #3 (nrO 52) en #10 (nrO 3) honderdtallen × tientallen; #4 (nrO 53) beide tientallen; #11 (nrO 4) aantal × honderdtallen
NULLEN = 'Reken de cijfers zonder de nullen keer elkaar, en zet daarna alle nullen van de afgeronde getallen erachter.'
def keer_regels(afr_tekst, met_plus_label=False):
    regels = [R('precies uitgerekend', 'fout = getal1 × getal2', 'Je hebt het precies uitgerekend. Dat is goed gerekend, maar de vraag vraagt een schatting: rond eerst af zoals de vraag zegt. ' + afr_tekst, afr_tekst + ' ' + NULLEN),
              R('nul te veel', 'fout = antwoord × 10', 'Dat is tien keer te groot: er staat een nul te veel achter.',
                'Tel de nullen van de afgeronde getallen samen. Zoveel nullen komen achter de uitkomst van de cijfers zonder nullen.'),
              R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te klein: er mist een nul.',
                'Tel de nullen van de afgeronde getallen samen. Zoveel nullen komen achter de uitkomst van de cijfers zonder nullen.')]
    if met_plus_label:
        regels.append(CL('opgeteld', 'optellen-ipv-vermenigvuldigen', "Heb je opgeteld? Er staat 'met elk': dan reken je keer.", afr_tekst + ' ' + NULLEN))
    regels.append(ALG('Rond eerst af zoals de vraag zegt, en reken dan met de afgeronde getallen keer elkaar. ' + afr_tekst, afr_tekst + ' ' + NULLEN))
    return regels
AFR_HT = ('Bij het getal dat je op honderdtallen afrondt, kijk je naar het cijfer van de tientallen. Bij het getal dat je op tientallen afrondt, '
          'kijk je naar de eenheden. Is dat cijfer vijf of meer? Dan rond je naar boven af, anders naar beneden.')
H1_KEER = 'Schatten is ongeveer uitrekenen met ronde getallen. Rond elk getal af zoals de vraag zegt, en reken daarna met de afgeronde getallen.'
OZ_KEER = 'Je kind schat een keersom: eerst afronden zoals de vraag zegt, dan de cijfers zonder nullen keer elkaar en de nullen erachter.'
E.append((E2, 52, H1_KEER, AFR_HT + ' ' + NULLEN, OZ_KEER, keer_regels(AFR_HT)))
E.append((E2, 3, H1_KEER, AFR_HT + ' ' + NULLEN, OZ_KEER, keer_regels(AFR_HT)))
AFR_TT = afr('tientallen', 'eenheden').replace('het cijfer van de eenheden', 'de eenheden')
E.append((E2, 53, H1_KEER, AFR_TT + ' ' + NULLEN, OZ_KEER, keer_regels(AFR_TT)))
AFR_AANTAL = 'Kijk bij het getal dat je op honderdtallen afrondt naar het cijfer van de tientallen. Is dat vijf of meer? Dan rond je naar boven af, anders naar beneden.'
E.append((E2, 4, 'Schatten is ongeveer uitrekenen met ronde getallen. Rond het getal af op honderdtallen, zoals de vraag zegt, en reken dan.',
  AFR_AANTAL + " Er staat 'met elk': reken het aantal keer het afgeronde getal. " + NULLEN,
  'Je kind schat een keersom met een verhaal: eerst één getal afronden op honderdtallen, dan keer het aantal.', keer_regels(AFR_AANTAL, met_plus_label=True)))

# meerkeuze #5 (nrO 54, ×) en #9 (nrO 57, +)
EIND_KEER = 'Reken alleen de eenheden van de twee getallen keer elkaar. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.'
GRENS_KEER = ('Rond het grootste getal naar beneden af op honderdtallen en reken keer: het antwoord is groter. '
              'Rond het naar boven af en reken keer: groter kan het antwoord niet zijn.')
E.append((E2, 54, 'Je hoeft niet precies te rekenen. Kijk eerst waarop het antwoord eindigt. ' + EIND_KEER,
  'Blijft er meer dan één antwoord over? ' + GRENS_KEER,
  'Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door te kijken waarop het eindigt en tussen welke ronde getallen het ligt.',
  [R('plus in plaats van keer', 'fout = getal1 + getal2', 'Heb je opgeteld? Er staat een keerteken (×): het antwoord is veel groter dan de twee getallen samen.', GRENS_KEER),
   CL('te groot', 'bovengrens', 'Dat is te groot. Rond het grootste getal naar boven af op honderdtallen en reken keer: groter kan het antwoord niet zijn.', GRENS_KEER),
   CL('te klein', 'ondergrens', 'Dat is te klein. Rond het grootste getal naar beneden af op honderdtallen en reken keer: kleiner kan het antwoord niet zijn.', GRENS_KEER),
   CL('veel te klein', 'orde-van-grootte', 'Dat is te klein. Rond het grootste getal naar beneden af op honderdtallen en reken keer: kleiner kan het antwoord niet zijn.', GRENS_KEER),
   CL('eindcijfer', 'laatste-cijfer', 'Kijk waarop het antwoord moet eindigen. ' + EIND_KEER,
      'Doe de eenheden van de twee getallen keer elkaar. Het cijfer helemaal rechts van die uitkomst staat ook helemaal rechts in het antwoord.'),
   ALG('Kijk eerst waarop het antwoord eindigt, en daarna tussen welke ronde getallen het ligt.', GRENS_KEER)]))
EIND_PLUS = 'Tel alleen de eenheden van de twee getallen op. Op welk cijfer eindigt dat? Daarop eindigt het antwoord ook.'
GRENS_PLUS = ('Rond allebei de getallen naar beneden af op honderdtallen en tel op: het antwoord is groter. '
              'Rond allebei naar boven af en tel op: groter kan het antwoord niet zijn.')
E.append((E2, 57, 'Je hoeft niet precies te rekenen. Kijk eerst waarop het antwoord eindigt. ' + EIND_PLUS,
  'Blijft er meer dan één antwoord over? ' + GRENS_PLUS,
  'Je kind kiest zonder precies te rekenen welk antwoord kan kloppen: door te kijken waarop het eindigt en tussen welke ronde getallen het ligt.',
  [R('min in plaats van plus', 'fout = getal1 - getal2 of getal2 - getal1', 'Heb je min gedaan? Er staat een plus: het antwoord is groter dan allebei de getallen.', GRENS_PLUS),
   CL('te groot', 'bovengrens', 'Dat is te groot. Rond allebei de getallen naar boven af op honderdtallen en tel op: groter kan het antwoord niet zijn.', GRENS_PLUS),
   CL('veel te klein', 'orde-van-grootte', 'Dat is te klein. Rond allebei de getallen naar beneden af op honderdtallen en tel op: kleiner kan het antwoord niet zijn.', GRENS_PLUS),
   CL('eindcijfer', 'laatste-cijfer', 'Kijk waarop het antwoord moet eindigen. ' + EIND_PLUS,
      'Tel de eenheden van de twee getallen op. Het cijfer helemaal rechts van die uitkomst staat ook helemaal rechts in het antwoord.'),
   ALG('Kijk eerst waarop het antwoord eindigt, en daarna tussen welke ronde getallen het ligt.', GRENS_PLUS)]))

# ================= GET-E03: volgorde van bewerkingen (open) =================
H2_31 = 'Tel eerst de twee getallen tussen de haakjes op. Doe die uitkomst daarna keer het getal achter de haakjes.'
E.append((E3, 1, 'Wat tussen haakjes staat, reken je altijd eerst uit.', H2_31,
  'Je kind oefent de rekenvolgorde: wat tussen haakjes staat, gaat altijd eerst.',
  [CL('haakjes overgeslagen', 'verkeerde-bewerking', 'Heb je eerst keer gedaan? Wat tussen haakjes staat, reken je eerst uit, ook als er een keerteken staat.', H2_31),
   CL('alles opgeteld', 'optellen-ipv-vermenigvuldigen', 'Heb je alles opgeteld? Achter de haakjes staat een keerteken (×).', H2_31),
   ALG('Reken eerst uit wat tussen de haakjes staat, en doe dat daarna keer het getal achter de haakjes.', H2_31)]))
H2_32 = 'Reken eerst de deelsom uit. Tel daarna het getal achter het plusteken erbij.'
E.append((E3, 2, 'De dubbele punt (:) betekent gedeeld door. Delen gaat vóór optellen, als er geen haakjes staan.', H2_32,
  'Je kind oefent de rekenvolgorde: delen gaat vóór optellen.',
  [CL('volgorde', 'verkeerde-bewerking', 'Let op de volgorde: eerst delen, daarna optellen.', H2_32),
   ALG('Reken eerst de deelsom uit, en tel daarna het getal achter het plusteken erbij.', 'Delen gaat vóór optellen. Je telt dus pas op als de deelsom klaar is.')]))
H2_33 = ('Reken eerst de minsom tussen de haakjes uit. Doe daarna het getal vóór de haakjes keer die uitkomst. '
         'Tel pas daarna het getal vóór het plusteken erbij.')
E.append((E3, 3, 'Eerst reken je uit wat tussen haakjes staat, dan keer, en pas daarna plus.', H2_33,
  'Je kind oefent de rekenvolgorde: eerst haakjes, dan keer, dan plus.',
  [CL('volgorde', 'verkeerde-bewerking', 'Let op de volgorde: eerst wat tussen haakjes staat, dan keer, en pas daarna plus.', H2_33),
   ALG('Eerst haakjes, dan keer, dan plus.', H2_33)]))
H2_34 = 'Reken eerst de keersom uit. Haal die uitkomst daarna af van het getal vóór het minteken.'
E.append((E3, 4, 'Keer gaat vóór min, als er geen haakjes staan.', H2_34,
  'Je kind oefent de rekenvolgorde: keer gaat vóór min.',
  [CL('eerst min', 'verkeerde-bewerking', 'Heb je eerst min gedaan? Keer gaat vóór min.', H2_34),
   CL('opgeteld bij het keerteken', 'optellen-ipv-vermenigvuldigen', 'Heb je de twee getallen bij het keerteken opgeteld? Daar staat keer (×): reken die keersom eerst uit.', H2_34),
   ALG('Reken eerst de keersom uit, en haal die uitkomst daarna af van het getal vóór het minteken.', H2_34)]))
H2_35 = 'Reken eerst de keersom uit. Tel daarna het getal vóór het plusteken erbij.'
E.append((E3, 5, 'Keer gaat vóór plus, als er geen haakjes staan.', H2_35,
  'Je kind oefent de rekenvolgorde: keer gaat vóór plus.',
  [CL('eerst plus', 'verkeerde-bewerking', 'Heb je eerst opgeteld? Keer gaat vóór plus.', H2_35),
   CL('alles opgeteld', 'optellen-ipv-vermenigvuldigen', 'Heb je alles opgeteld? Er staat ook een keerteken (×).', H2_35),
   ALG('Reken eerst de keersom uit, en tel daarna het getal vóór het plusteken erbij.', H2_35)]))

# ================= GET-E04: breuken =================
H2_HEEL = 'In één heel passen zoveel stukken als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal hele.'
def hele_stukken():
    return [R('hele overgenomen', 'fout = getal1', 'Dat is het aantal hele waar je mee begint. Elk heel wordt in stukken verdeeld, dus je krijgt meer stukken.', H2_HEEL),
            CL('opgeteld', 'optellen-ipv-vermenigvuldigen', 'Heb je opgeteld? Elk heel geeft zoveel stukken als de noemer (het getal onder de streep) zegt: reken keer.', H2_HEEL),
            CL('hele (label)', 'omgekeerd-gedeeld', 'Dat is het aantal hele waar je mee begint. Elk heel wordt in stukken verdeeld, dus je krijgt meer stukken.', H2_HEEL),
            ALG('Kijk eerst hoeveel stukken er in één heel passen, en reken dan keer het aantal hele.', H2_HEEL)]
H1_HEEL = 'Je zoekt hoeveel stukken er in totaal zijn. Kijk eerst naar één heel: hoeveel stukken van deze grootte passen erin?'
OZ_HEEL = 'Je kind deelt hele dingen in gelijke stukken (delen door een breuk): in één heel passen zoveel stukken als de noemer zegt.'
for nro in (1, 4, 7):
    E.append((E4, nro, H1_HEEL, H2_HEEL, OZ_HEEL, hele_stukken()))
H2_LITER = 'Uit één liter schenk je zo vaak als de noemer (het getal onder de streep) zegt. Doe dat keer het aantal liters.'
E.append((E4, 2, 'Je zoekt hoe vaak je kunt schenken. Kijk eerst naar één liter: hoe vaak kun je daaruit schenken?', H2_LITER,
  'Je kind deelt liters in gelijke porties (delen door een breuk): uit één liter schenk je zo vaak als de noemer zegt.',
  [R('liters overgenomen', 'fout = getal1', 'Dat is het aantal liters. Uit elke liter schenk je meer dan één keer.', H2_LITER),
   CL('één liter', 'omgekeerd-gedeeld', 'Zo vaak schenk je uit één liter. Er zijn meer liters: reken keer het aantal liters.', H2_LITER),
   ALG('Kijk eerst hoe vaak je uit één liter schenkt, en reken dan keer het aantal liters.', H2_LITER)]))
EENVOUDIG = ('Die breuk is even groot als het antwoord, maar het kan eenvoudiger. Deel de teller (het getal boven de streep) en de noemer '
             '(het getal onder de streep) door hetzelfde getal.')
EENVOUDIG2 = 'Zoek een getal waardoor de teller (boven de streep) en de noemer (onder de streep) allebei te delen zijn, en deel ze allebei. Ga door tot dat niet meer kan.'
H2_DVD = ('Doe teller keer teller en noemer keer noemer (de teller is het getal boven de streep, de noemer het getal onder de streep). '
          'Maak de breuk daarna zo eenvoudig mogelijk.')
E.append((E4, 3, 'Je neemt een deel ván wat er nog is. Een deel van een deel reken je uit met keer.', H2_DVD,
  'Je kind rekent een deel van een deel uit (breuk keer breuk) en maakt de breuk zo eenvoudig mogelijk.',
  [R('niet vereenvoudigd', 'fout = gelijkwaardig maar niet zo eenvoudig mogelijk', EENVOUDIG, EENVOUDIG2),
   CL('opgeteld', 'teller-en-noemer-optellen', 'Heb je de tellers (boven de streep) opgeteld en de noemers (onder de streep) ook? Een deel ván een deel is keer, niet plus.', H2_DVD),
   CL('niet van de hele taart', 'deel-vergeten-bij-splitsen', 'Dat is niet het deel van de hele taart. Neem het deel ván wat er nog is: reken de twee breuken keer elkaar.', H2_DVD),
   ALG('Reken de twee breuken keer elkaar: teller keer teller (boven de streep) en noemer keer noemer (onder de streep).', H2_DVD)]))
H2_PAST = ('Maak de twee breuken gelijknamig: geef ze dezelfde noemer (het getal onder de streep). Hoe vaak past de teller '
           '(het getal boven de streep) van het kleine stuk in de teller van het deel?')
def deel_in_stukken():
    # 'antwoord + 1' maakt geen sleutel als die waarde ook in de vraag staat (031: 4 bij 1/4; 032/037: 2 bij 1/2); daarom ook Claudes label 'een-ernaast'
    return [R('één te veel', 'fout = antwoord + 1', 'Dat is één stuk te veel. Tel nog eens hoe vaak het kleine stuk in het deel past.', H2_PAST),
            CL('één te veel (label)', 'een-ernaast', 'Dat is één stuk te veel. Tel nog eens hoe vaak het kleine stuk in het deel past.', H2_PAST),
            CL('teller overgenomen', 'getal-overgenomen', 'Dat is de teller van het deel (het getal boven de streep). Je zoekt hoe vaak het kleine stuk in het deel past.', H2_PAST),
            ALG('Kijk hoe vaak het kleine stuk in het deel past.', H2_PAST)]
for nro in (5, 8):
    E.append((E4, nro, 'Je zoekt hoe vaak het kleine stuk in het deel past.', H2_PAST,
      'Je kind deelt een breuk in kleinere stukken (breuk gedeeld door breuk): met dezelfde noemer kun je de tellers vergelijken.', deel_in_stukken()))
H2_OPT = ('Maak de breuken gelijknamig: geef ze dezelfde noemer (het getal onder de streep), en verander de tellers (de getallen boven de streep) mee. '
          'Tel daarna alleen de tellers op.')
E.append((E4, 6, 'Breuken kun je pas optellen als ze dezelfde noemer hebben (het getal onder de streep).', H2_OPT,
  'Je kind telt twee breuken op: eerst gelijknamig maken (dezelfde noemer geven), dan de tellers optellen.',
  [R('niet vereenvoudigd', 'fout = gelijkwaardig maar niet zo eenvoudig mogelijk', EENVOUDIG, EENVOUDIG2),
   CL('alles opgeteld', 'teller-en-noemer-optellen', 'Bij breuken optellen tel je alleen de tellers op (boven de streep), en dat kan pas als de noemers (onder de streep) gelijk zijn.', H2_OPT),
   CL('tellers niet mee', 'deel-vergeten-bij-splitsen', 'De noemer (onder de streep) klopt, maar de tellers (boven de streep) moeten mee veranderen als je de noemers gelijk maakt.',
      'Hoeveel keer heb je de noemer (het getal onder de streep) van elke breuk groter gemaakt? Doe de teller (het getal boven de streep) van die breuk evenveel keer. Tel daarna de tellers op.'),
   ALG('Maak de breuken eerst gelijknamig (geef ze dezelfde noemer: het getal onder de streep), en tel dan de tellers (boven de streep) op.', H2_OPT)]))

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
D = {'batch': 'batch1', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 1 = GET-E02 #1–#11 schatten en laatste cijfer, GET-E03 volgorde van bewerkingen, GET-E04 breuken). "
                "Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); 'nr' en 'somtype' "
                "houdt scripts/sync_hint_keys.py bij. foutHints: per sleutel een motorregel of Claudes sleutel (label) met een vaste tekst, laag 1 'tekst' en "
                "laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
