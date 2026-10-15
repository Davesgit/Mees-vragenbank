#!/usr/bin/env python3
"""Schrijft hints/batch8.json (G8 batch 8: VERH-E01 #1, VERH-E02 #1, VERH-E03 #1–#11, VERH-E04 #1–#8, VERH-E06 #1–#3, VERH-V01 #1 = 25 somtypes,
368 items): schaal op een kaart (cm ↔ km/m), korting terugrekenen, rente, procent van een aantal, kommagetal en breuk ↔ procent, deel van een geheel,
prijs per stuk. 8 okt 2026 (17:3x), Oefeningen. Formaat als make_batch7.py. Data: live g8 (build 17:24:12). Lessen: hints/lessen_g8.md t/m les 354.
Analyse en checks: /workspace/g8work/b8/check.py op de zandbak /workspace/g8work/b8/sbx.sh (verse kopie van live).
Keuzes:
- Kaal: motorregels die per item uitkomen (antwoord × 10 / : 10 / × 100 / × 1000, een getal uit de vraag, getal2, antwoord + getal1, kommagetal met
  procentteken); daarna labelregels voor Claudes overige sleutels (Oef-#490), met een tekst die voor elke sleutel van dat label waar is.
- VERH-E06 #1–#3 hebben hetzelfde somtype als G7 VERH-04 #2/#1/#3 (door Didactiek gekeurd): die teksten als basis, aangepast aan drie cijfers achter
  de komma (0,575 → 57,5%) en ingekort tot de G8-grenzen.
- Meerkeuze (E01, E02, E04 #8, E06 #1/#2, V01): per foute optie een letterlijke regel (G8-2) of een regel die precies die optie pakt.
- Geen cijfers, geen woorden van de [..]-plekken (les 147), geen plekwoorden (les 193), geen 'even veel' (#192), verklaptoets meerkeuze (les 260/264
  op H1 én H2, Z-#824), les 350 (H2 spreekt de conclusie niet uit), les 351 (woorden van de opgave).
Na een sync nooit --force: correcties via hints/patch_batch8.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B8_OUT', f'{BASE}/hints/batch8.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch8.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch8.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch8.json bestaat al: patch in place (hints/patch_batch8.py), of --force als er nog geen sync is geweest.')
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
E01, E02, E03, E04, E06, V01 = "G8-VERH-E01", "G8-VERH-E02", "G8-VERH-E03", "G8-VERH-E04", "G8-VERH-E06", "G8-VERH-V01"
def ST(doel, nr, h1, h2, oz, fh):
    E.append((doel, nr, h1, h2, oz, fh))

# ---- VERH-E01 #1 (001): deel van de knikkers ('6 op de 10'), meerkeuze ----
H2 = 'Tel alle knikkers in de bak bij elkaar op, van elke kleur. Tel ook hoeveel er de kleur uit de vraag hebben. Zet dat aantal tegenover alle knikkers samen.'
ST(E01, 1, 'Welk deel van alle knikkers? Tel eerst hoeveel knikkers er samen in de bak zitten.', H2,
   'Je kind schrijft een deel van een groep als zoveel op de zoveel.',
   [LT('zonder het deel', '6 op de 4', "Na 'op de' tel je alle knikkers samen, ook die met de kleur uit de vraag.", H2),
    LT('andere kleur', '3 op de 10', 'Kijk welke kleur de vraag noemt. Hoeveel knikkers hebben die kleur?', H2),
    ALG('Tel alle knikkers samen. Hoeveel daarvan hebben de kleur uit de vraag?', H2)])

# ---- VERH-E02 #1 (001): prijs van meer stuks via één stuk, meerkeuze ----
H2 = 'Deel de prijs door het aantal dat samen zoveel kost: dan weet je wat er één kost. Doe dat keer het aantal dat gevraagd wordt.'
ST(E02, 1, 'Wat kost er één? Reken dat eerst uit.', H2,
   'Je kind rekent via de prijs van één stuk uit wat meer stuks kosten.',
   [LT('een klein bedrag erbij', '€6,50', 'Zo komt er voor de extra stuks maar een klein bedrag bij. Wat kost er één? Doe dat keer het aantal dat gevraagd wordt.', H2),
    LT('keer het nieuwe aantal', '€22,50', 'Dat is de prijs van de hele groep uit de vraag, keer het nieuwe aantal. Reken eerst uit wat er één kost.', H2),
    ALG('Wat kost er één? Doe dat keer het aantal dat gevraagd wordt.', H2)])

# ---- VERH-E03 schaal op een kaart ----
H1_S = 'Bij een schaal staat een dubbele punt tussen de getallen. Eén centimeter op de kaart is in het echt zoveel centimeter als het getal erachter.'
# #1–#3 (cm op de kaart → km), #8/#11 (idem, schaal 1 : 100.000; daar is het aantal cm het antwoord: geen 'getal uit de vraag')
H2_KM = 'Honderdduizend centimeter is één kilometer. Streep bij het getal achter de dubbele punt vijf nullen weg: zoveel kilometer is één centimeter op de kaart. Doe dat keer het aantal centimeter op de kaart.'
OZ_KM = 'Je kind rekent een afstand op een kaart om naar kilometers in het echt, met de schaal.'
KM_M = R('meters', 'fout = antwoord × 1000', 'Dat is het aantal meter. Gevraagd is kilometers: duizend meter is één kilometer.', H2_KM)
KM_10 = R('tien keer te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.', H2_KM)
KM_01 = R('tien keer te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.', H2_KM)
KM_G = R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Reken daarmee verder.', H2_KM)
KM_CL = CL('andere omrekening', 'eenheid-verkeerd-omgerekend', 'Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.', H2_KM)
KM_A = ALG('Hoeveel kilometer is één centimeter op deze kaart? Doe dat keer het aantal centimeter.', H2_KM)
for nr in (1, 2, 3): ST(E03, nr, H1_S, H2_KM, OZ_KM, [KM_M, KM_10, KM_01, KM_G, KM_CL, KM_A])
for nr in (8, 11): ST(E03, nr, H1_S, H2_KM, OZ_KM, [KM_M, KM_10, KM_CL, KM_A])
# #4–#6 (km in het echt → cm op de kaart)
H1_CM = 'Bij een schaal staat een dubbele punt tussen de getallen. Op de kaart is alles veel kleiner dan in het echt. Hoeveel kilometer is één centimeter op de kaart?'
H2_CM = 'Streep bij het getal achter de dubbele punt vijf nullen weg: zoveel kilometer is één centimeter op de kaart. Hoe vaak past dat in de echte afstand? Zoveel centimeter is het op de kaart.'
CM_10 = R('tien keer te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.', H2_CM)
CM_01 = R('tien keer te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Tel de nullen nog eens: honderdduizend centimeter is één kilometer.', H2_CM)
CM_G = R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Op de kaart is de afstand veel kleiner dan in het echt.', H2_CM)
CM_CL = CL('andere omrekening', 'eenheid-verkeerd-omgerekend', 'Dat past niet bij de schaal. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?', H2_CM)
CM_A = ALG('Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?', H2_CM)
for nr in (4, 5, 6): ST(E03, nr, H1_CM, H2_CM, 'Je kind rekent een echte afstand in kilometers om naar centimeters op een kaart, met de schaal.', [CM_10, CM_01, CM_G, CM_CL, CM_A])
# #7, #9, #10 (cm op de kaart → meter)
H2_M = 'Doe het aantal centimeter op de kaart keer het getal achter de dubbele punt: zoveel centimeter is het in het echt. Honderd centimeter is één meter: streep twee nullen weg.'
M_100 = R('nog in centimeters', 'fout = antwoord × 100', 'Dat is het aantal centimeter in het echt. Gevraagd is meters: honderd centimeter is één meter.', H2_M)
M_10 = R('tien keer te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel. Tel de nullen nog eens: honderd centimeter is één meter.', H2_M)
M_01 = R('tien keer te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Tel de nullen nog eens: honderd centimeter is één meter.', H2_M)
M_CL = CL('andere omrekening', 'eenheid-verkeerd-omgerekend', 'Dat past niet bij de schaal. Hoeveel centimeter is het in het echt? Reken dat om naar meters.', H2_M)
M_A = ALG('Hoeveel centimeter is het in het echt? Reken dat om naar meters: honderd centimeter is één meter.', H2_M)
for nr in (7, 9, 10): ST(E03, nr, H1_S, H2_M, 'Je kind rekent een afstand op een kaart om naar meters in het echt, met de schaal.', [M_100, M_10, M_01, M_CL, M_A])

# ---- VERH-E04 ----
# #1/#6: prijs vóór de korting
H2_K = 'Haal het procent van de korting van honderd af: zoveel procent van de oude prijs is de nieuwe prijs. Reken uit hoeveel euro één procent is. Doe dat keer honderd.'
# Claudes sleutels hebben een '€', het antwoord niet (datapunt Oef-#1006): motorregels geven dan sleutels zonder '€' naast Claudes sleutels met '€',
# en Claudes sleutels vallen op 'andere fout'. Daarom labelregels: elke sleutel heeft een Claude-tekst (claudeFoutHints), het label bepaalt de route.
K_FH = [CL('nieuwe prijs', 'getal-overgenomen', 'Dat is de prijs na de korting. Gevraagd is de prijs van vóór de korting: die is hoger.', H2_K),
        CL('procent van de nieuwe prijs', 'procent-verkeerde-basis', 'Heb je het procent van de nieuwe prijs erbij gedaan? De korting ging van de oude prijs af, niet van de nieuwe.', H2_K),
        ALG('De nieuwe prijs is een deel van de oude prijs. Welk procent? Reken daarmee terug naar honderd procent.', H2_K)]
for nr in (1, 6): ST(E04, nr, 'Na de korting betaal je niet meer honderd procent van de oude prijs. Hoeveel procent betaal je nog?', H2_K,
                     'Je kind rekent terug naar de prijs van vóór de korting.', K_FH)
# #2, #3, #4, #5, #7: rente na één jaar
H2_R = 'Deel het bedrag door honderd: dat is één procent. Doe dat keer het procent. Dat krijg je er in één jaar bij.'
R_FH = [CL('tien keer te veel', 'komma-verschoven', 'Dat is tien keer te veel. Eén procent is het bedrag gedeeld door honderd. Doe dat keer het procent.', H2_R),
        CL('bedrag erbij', 'getal-overgenomen', 'Dat is het bedrag op de rekening met wat erbij komt samen. Gevraagd is alleen wat er in één jaar bij komt.', H2_R),
        CL('procent als bedrag', 'procent-verkeerde-basis', 'Dat is het getal van het procent. Wat erbij komt, is een deel van het bedrag: hoeveel euro is dat?', H2_R),
        ALG('Deel het bedrag door honderd en doe dat keer het procent.', H2_R)]
for nr in (2, 3, 4, 5, 7): ST(E04, nr, 'Procent betekent: zoveel van de honderd. Hoeveel euro is één procent van het bedrag op de rekening?', H2_R,
                             'Je kind rekent uit hoeveel geld er in een jaar bij komt met een procent rente.', R_FH)
# #8 (032): procent van een aantal, meerkeuze
H2 = 'Reken uit hoeveel tien procent is: deel het aantal op school door tien. Hoe vaak heb je tien procent nodig?'
ST(E04, 8, 'Procent betekent: zoveel van de honderd. Iedereen op school samen is honderd procent.', H2,
   'Je kind rekent een procent van een aantal uit.',
   [LT('procent als aantal', '60 kinderen', 'Dat is het getal van het procent, nog geen aantal. Hoeveel is dat procent van iedereen op school?', H2),
    LT('te veel', '100 kinderen', 'Dat is te veel. Reken uit hoeveel tien procent van iedereen op school is, en neem dat zo vaak als nodig.', H2),
    ALG('Iedereen op school samen is honderd procent. Hoeveel is tien procent? Hoe vaak heb je dat nodig?', H2)])

# ---- VERH-E06 (zelfde somtypes als G7 VERH-04 #2/#1/#3) ----
# #1: kommagetal (drie cijfers achter de komma) → procent, meerkeuze
H2 = 'Doe het kommagetal keer honderd: de komma schuift twee plekken naar rechts. Zet daarna het procentteken erachter.'
ST(E06, 1, 'Procent betekent: zoveel van de honderd. Eén hele is honderd procent.', H2, 'Je kind schrijft een kommagetal als procent.',
   [R('kommagetal met procentteken', 'fout = kommagetal met procentteken', 'Dat is het kommagetal met een procentteken erachter. Procent is zoveel van de honderd: doe het kommagetal eerst keer honderd.', H2),
    CL('komma verschoven', 'komma-verschoven', 'Staat de komma goed? Bij keer honderd schuift de komma twee plekken naar rechts, niet één of drie.', H2),
    ALG('Doe het kommagetal keer honderd. Staat de komma dan twee plekken verder naar rechts?', H2)])
# #2: breuk (noemer veertig) → procent, meerkeuze
H2 = 'Maak een verhoudingstabel: de noemer hoort bij honderd procent, de teller bij het procent dat je zoekt. Reken de noemer om naar honderd en doe met de teller hetzelfde. Gaat dat niet in één keer? Deel dan eerst allebei door hetzelfde getal.'
ST(E06, 2, 'Procent betekent: zoveel van de honderd. Een breuk met honderd als noemer kun je zo als procent schrijven.', H2, 'Je kind schrijft een breuk als procent.',
   # 'getal-overgenomen' heeft geen Claude-tekst (geen Claude-sleutel): letterlijke regels op de optie (teller of noemer met '%'), één tekst die voor
   # allebei waar is (les 354: geen tekst die alleen voor de teller of alleen voor de noemer klopt)
   [LT('getal uit de breuk', '21%', 'Dat is een getal uit de breuk met een procentteken erachter. Dat klopt alleen als de noemer honderd is.', H2),
    LT('getal uit de breuk (noemer)', '40%', 'Dat is een getal uit de breuk met een procentteken erachter. Dat klopt alleen als de noemer honderd is.', H2),
    CL('tien keer ernaast', 'nul-fout-tientallen', 'Dat is tien keer te groot of te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.', H2),
    ALG('Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.', H2)])
# #3 (001): procent → kommagetal, kaal
H2 = 'Deel het getal van het procent door honderd: de komma schuift twee plekken naar links. Is er geen heel getal? Zet dan een nul voor de komma.'
ST(E06, 3, 'Procent betekent: zoveel van de honderd. Zoveel honderdsten kun je als kommagetal schrijven.', H2, 'Je kind schrijft een procent als kommagetal.',
   [R('tien keer te groot', 'fout = antwoord × 10', 'Dat is tien keer te groot. Procent zijn honderdsten: deel het getal van het procent door honderd.', H2),
    R('procent zonder komma', 'fout = een getal uit de vraag', 'Dat is het getal van het procent. Als kommagetal is het honderd keer zo klein.', H2),
    CL('procent zonder komma (punt)', 'kommagetal-als-geheel', 'Dat is het getal van het procent. Als kommagetal is het honderd keer zo klein.', H2),   # Claudes sleutel '12.5' (punt)
    CL('komma verschoven', 'komma-verschoven', 'Staat de komma goed? Procent zijn honderdsten: de komma schuift twee plekken naar links.', H2),
    ALG('Deel het getal van het procent door honderd.', H2)])

# ---- VERH-V01 #1 (001): hoeveel procent is een deel, meerkeuze ----
H2 = 'Maak een verhoudingstabel: het hele aantal hoort bij honderd procent. Reken uit hoeveel procent bij het deel hoort.'
ST(V01, 1, 'Procent betekent: zoveel van de honderd. Het hele aantal is honderd procent.', H2, 'Je kind rekent uit hoeveel procent een deel van een groep is.',
   [LT('aantal als procent', '40 procent', 'Dat is het aantal uit de vraag, nog geen procent. Hoeveel is dat van de honderd?', H2),
    LT('tien keer te klein', '2 procent', 'Dat is tien keer te klein. Hoe vaak past het deel in het hele aantal? Welk procent hoort daarbij?', H2),
    ALG('Het hele aantal is honderd procent. Hoeveel procent is het deel?', H2)])
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
D = {'batch': 'batch8', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 8 = VERH-E01/E02/E03/E04/E06/V01: schaal, procenten, verhoudingen). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
