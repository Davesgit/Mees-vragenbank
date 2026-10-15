#!/usr/bin/env python3
"""G8 batch 8 (VERH-E01 #1, VERH-E02 #1, VERH-E03 #1–#11, VERH-E04 #1–#8, VERH-E06 #1–#3, VERH-V01 #1: 25 somtypes, 368 items) nagespeeld op de
toegepaste per_doel-data (zandbak of live). Opzet als b6/b7.
Per item de feiten waar H1/H2/L1 op leunen (DATA, 'eis') en per sleutel een predicaat per soort (les 40/146/191); route-guard (les 306): geen foute
route met een eigen tekst op het goede antwoord. Meerkeuze: antwoord in de opties, husselen, elke foute optie precies één fout-hint, de soort klopt
op de waarde; verklaptoets les 260 / Z-#824 / les 264 op H1 én H2. Teksten: cijfers, optieletters, plekwoorden (les 193), les 217, 'zoveel' vooraan,
les 231, contextwoorden (les 147, [..]-plekken en kopwoorden van somtypes met dezelfde H1/H2; maateenheden mogen), moeilijke woorden, 'Bijna',
V-#764 (45/55 woorden), les 235, les 262, les 271. Les 234: snapshot van de opties (SNAP=1 schrijft hem). Les 353: een item dat de check laat
crashen, geeft een FAIL (geen traceback).
Gebruik: python3 check.py [pad naar g8]   MUT=<naam> voor een mutant (moet FAIL geven)."""
import json, re, sys, os, collections, traceback
from fractions import Fraction as Fr
G8 = sys.argv[1] if len(sys.argv) > 1 else __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..')
MUT = os.environ.get('MUT')
sys.path.insert(0, f'{G8}/scripts'); import fout_regels as FR
CH = open(f'{G8}/check_hints.py', encoding='utf-8').read()
MOEILIJK = re.compile(re.search(r"MOEILIJK=re\.compile\(r'(.*?)',re\.I\)", CH).group(1), re.I)
F, W, I = [], [], []
def fail(m): F.append(m)
E01, E02, E03, E04, E06, V01 = "G8-VERH-E01", "G8-VERH-E02", "G8-VERH-E03", "G8-VERH-E04", "G8-VERH-E06", "G8-VERH-V01"
SEL = {E01: {1}, E02: {1}, E03: set(range(1, 12)), E04: set(range(1, 9)), E06: {1, 2, 3}, V01: {1}}
B = json.load(open(f'{G8}/hints/batch8.json'))
if MUT == 'M_1014': B['somtypen'].append(dict(next(s_ for s_ in B['somtypen'] if s_['doel'] == E04 and s_['nrOrigineel'] == 1), nrOrigineel=99))   # r1d: twee entries op één kop
BT = {(s['doel'], s['nrOrigineel']): s for s in B['somtypen']}
BKOP = {(s['doel'], s.get('somtype')): (s['doel'], s['nrOrigineel']) for s in B['somtypen']}   # r1d (G8_KOP1014): een item hoort bij de entry van zijn kop, niet per se bij zijn nrOrigineel
def EK(x): return BKOP.get((x['doelId'], x['merge']['somtype']), (x['doelId'], x['merge']['somtypeNrOrigineel']))
PUNT = []; VORMCUE = collections.Counter(); EURO = collections.Counter(); AFGEROND = []; GEEN_ROUTE = []
def val(k, noteer=None):
    k = str(k).strip().replace('−', '-')
    k = re.sub(r'^(ongeveer|€)\s*', '', k, flags=re.I); k = re.sub(r'\s*(%|procent|kinderen|km|cm|m)$', '', k)
    if re.fullmatch(r'-?\d+,\d+', k): return Fr(k.replace(',', '.'))
    if re.fullmatch(r'-?(\d{1,3}(?:\.\d{3})+|\d+)', k): return Fr(int(k.replace('.', '')))
    if re.fullmatch(r'\d+\.\d{1,2}', k):          # punt als komma (Claude-sleutel '12.5'): datapunt (zoals Oef-#498)
        if noteer is not None: PUNT.append(noteer)
        return Fr(k)
    return None
def num(t): return Fr(t.replace('.', '').replace(',', '.')) if re.fullmatch(r'\d{1,3}(\.\d{3})+|\d+', t) else Fr(t.replace(',', '.'))
def nums(t): return [num(x) for x in re.findall(r'(?<![\d,.])\d+(?:[.,]\d+)*(?![\d,])', t)]
def past(regel, optie):
    r = FR.norm421(regel.strip()).lower()
    return r in FR.norm421(optie, geld=r.startswith('€')).lower() and FR.lett_past(r, optie)
ITEMS = []
for doel_, nrs_ in SEL.items():
    d = json.load(open(f'{G8}/data/per_doel/{doel_}.json'))
    ITEMS += [x for x in d['items'] if x['merge']['somtypeNrOrigineel'] in nrs_]
def IT(doel, nr): return next(x for x in ITEMS if x['doelId'] == doel and x['nr'] == nr)
# build 18:04: gesplitste koppen (V-#972 plekparen, 'krijgt hij/het') vallen buiten SEL en kregen geen hints: niet stil overslaan (les 374).
ZONDER_ENTRY = [f"{x['doelId'][3:]} nrO{x['merge']['somtypeNrOrigineel']} {x['nr']}" for doel_ in SEL for x in json.load(open(f'{G8}/data/per_doel/{doel_}.json'))['items']
                if x['merge']['somtypeNrOrigineel'] not in SEL[doel_] and x['foutHints'] and not any(f_.get('soort') for f_ in x['foutHints'])]
def FH(x, soort): return next(f for f in x['foutHints'] if f['soort'] == soort)
def FHV(x, fout): return next(f for f in x['foutHints'] if f['fout'] == fout)
def opg(doel, nr, oud, nieuw): x_ = IT(doel, nr); assert oud in x_['opgave'], (nr, oud); x_['opgave'] = x_['opgave'].replace(oud, nieuw)
# ---- data-mutanten (moeten FAIL geven) ----
if MUT == 'M_dschaal': opg(E03, '165', '1 : 200.000', '1 : 250.000')                 # E03 km: antwoord klopt niet meer met de schaal
if MUT == 'M_d5nul': opg(E03, '165', '1 : 200.000', '1 : 20.000'); IT(E03, '165')['antwoord'] = '5'   # H2 'vijf nullen weg' kan niet
if MUT == 'M_dcm': opg(E03, '001', '1000 km', '1100 km')                               # E03 cm
if MUT == 'M_dm': opg(E03, '227', '2 cm', '3 cm')                                      # E03 meter
if MUT == 'M_d100k': opg(E03, '165', '1 : 200.000', '1 : 100.000'); IT(E03, '165')['antwoord'] = '25'   # les 306: cm = antwoord, 'getal uit de vraag' op het antwoord
if MUT == 'M_dkort': opg(E04, '006', '40% korting', '30% korting')
if MUT == 'M_drente': IT(E04, '025')['antwoord'] = '60'
if MUT == 'M_d100e': opg(E04, '025', '€200', '€100'); IT(E04, '025')['antwoord'] = '3'   # les 306: het procent = het antwoord
if MUT == 'M_dfiets': IT(E04, '032')['antwoord'] = '30 kinderen'   # r1b: een optie die niet klopt
if MUT == 'M_dproc': opg(E06, '002', '0,575', '0,57')
if MUT == 'M_dbreuk': opg(E06, '098', '21/40', '21/50')
if MUT == 'M_dkap': IT(E06, '001')['antwoord'] = '1,25'
if MUT == 'M_dv01': opg(V01, '001', '60 van de 200', '60 van de 250')
if MUT == 'M_dkn': opg(E01, '001', '1 groene', '2 groene')
if MUT == 'M_dsap': opg(E02, '001', 'samen €4,50', 'samen €6')
if MUT == 'M_d353': opg(E03, '165', 'De schaal van een kaart is 1 : 200.000.', 'De kaart heeft een schaal.')   # les 353: geen match = FAIL, geen crash
# ---- sleutel-/regelmutanten ----
if MUT == 'M_label': FHV(IT(E03, '165'), '500')['soort'] = 'meters'
if MUT == 'M_label2': FH(IT(E04, '025'), 'bedrag erbij')['soort'] = 'procent als bedrag'   # r1b: op soort (Claudes sleutels zonder '€' sinds 17:47)
if MUT == 'M_label3': FHV(IT(E06, '002'), '5,75%')['soort'] = 'kommagetal met procentteken'
if MUT == 'M_label4': FH(IT(E04, '006'), 'procent van de nieuwe prijs')['soort'] = 'nieuwe prijs'
if MUT == 'M_label5': FHV(IT(E03, '227'), '50')['soort'] = 'nog in centimeters'
if MUT == 'M_label6': FHV(IT(E03, '001'), '1000')['soort'] = 'tien keer te veel'
if MUT == 'M_lett': FH(IT(V01, '001'), 'tien keer te klein')['regel'] = 'procent'
if MUT == 'M_mist': x_ = IT(E01, '001'); x_['foutHints'] = [f for f in x_['foutHints'] if f['fout'] != '3 op de 10']
if MUT == 'M_alg': FHV(IT(E02, '001'), '€6,50')['soort'] = 'andere fout'
if MUT == 'M_antw': x_ = IT(E03, '165'); x_['foutHints'].append(dict(x_['foutHints'][0], fout='50'))
if MUT == 'M_antw2': x_ = IT(E04, '032'); x_['foutHints'].append(dict(x_['foutHints'][0], fout=x_['antwoord'], regel=x_['antwoord']))   # r1b: het antwoord uit de data
if MUT == 'M_L2': IT(E03, '165')['foutHints'][0]['uitlegSterker'] = ''
if MUT == 'M_onb': IT(E03, '227')['foutHints'][0]['soort'] = 'iets nieuws'
if MUT == 'M_hussel': IT(E06, '002')['husselen'] = False
if MUT == 'M_breuk': FHV(IT(E06, '098'), '21%')['soort'] = 'tien keer ernaast'
if MUT == 'M_label7': x_ = IT(E04, '032'); [f.__setitem__('soort', 'procent als aantal') for f in x_['foutHints'] if f['fout'] == '170 kinderen']   # ronde 1b
if MUT == 'M_d1010': opg(E04, '032', 'Van de 200', 'Van de 150'); opg(E04, '032', '30 procent', '60 procent'); x_ = IT(E04, '032'); x_['antwoord'] = '90 kinderen'; [o_.__setitem__('tekst', '90 kinderen') for o_ in x_['opties'] if o_['tekst'] == '60 kinderen']   # les 306: geheel min het procent = het antwoord
if MUT == 'M_971': opg(E03, '093', '1 : 500.000', '1 : 100.000'); IT(E03, '093')['antwoord'] = '29'   # V-#971: 1 : 100.000 = les 306
if MUT == 'M_971r': BT[(E03, 2)]['foutHints'] = [f for f in BT[(E03, 2)]['foutHints'] if f['soort'] != 'getal uit de vraag']   # V-#971: regel ontbreekt
if MUT == 'M_982': [f.__setitem__('soort', 'getal uit de breuk (noemer)') for x_ in ITEMS if x_['doelId'] == E06 and x_['merge']['somtypeNrOrigineel'] == 2 for f in x_['foutHints'] if f['fout'] == '7%']
if MUT == 'M_373': [f.__setitem__('uitleg', 'Dat is een getal uit de breuk met een procentteken erachter. Dat klopt alleen als de noemer honderd is.') for x_ in ITEMS if x_['doelId'] == E06 and x_['merge']['somtypeNrOrigineel'] == 2 for f in x_['foutHints'] if f['fout'] == '7%']
if MUT == 'M_301': opg(V01, '001', '60 van de 200', '3 van de 10')   # les 301: '3 procent' = aantal als procent én tien keer te klein
if MUT == 'M_kv': FHV(IT(E06, '002'), '5,75%')['fout'] = '0,0575%'
# Z-#991 (Didactiek hercheck 18:20:30): de vier mutanten op #8/#11 zelf vast in b8 (M_971/M_971r raken #3/#2)
if MUT == 'M_971b': opg(E03, '218', '1 : 200.000', '1 : 100.000'); IT(E03, '218')['antwoord'] = '9'   # les 306 op #8
if MUT == 'M_971c': opg(E03, '229', '1 : 200.000', '1 : 100.000'); opg(E03, '229', '4 cm', '8 cm'); IT(E03, '229')['antwoord'] = '8'   # les 306 op #11
if MUT == 'M_971r8': BT[(E03, 8)]['foutHints'] = [f for f in BT[(E03, 8)]['foutHints'] if f['soort'] != 'getal uit de vraag']
if MUT == 'M_971r11': BT[(E03, 11)]['foutHints'] = [f for f in BT[(E03, 11)]['foutHints'] if f['soort'] != 'tien keer te weinig']
# ronde 1c V-#1000 / Z-#983: werken op de data van vóór én na V-#1000 (de optie ': 10' of '× 10' van het item wordt '× 10')
def _m1000(nr, soort, uitleg=None):
    x_ = IT(E06, nr); a_ = val(x_['antwoord']); nw_ = f"{str(float(a_ * 10)).rstrip('0').rstrip('.').replace('.', ',')}%"
    for o_ in x_['opties']:
        if val(o_['tekst']) in (a_ / 10, a_ * 10): oud_ = o_['tekst']; o_['tekst'] = nw_
    f_ = FHV(x_, oud_); f_['fout'] = nw_; f_['soort'] = soort
    if uitleg: f_['uitleg'] = uitleg
if MUT == 'M_1000': _m1000('099', 'tien keer ernaast', 'Dat is tien keer te groot of te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.')
if MUT == 'M_1000t': _m1000('098', 'tien keer te groot (525%)', 'Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?')
if MUT == 'M_983': _m1000('100', 'tien keer ernaast', 'Dat is tien keer te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.')
# ---- V-#1060 (Overzicht build 20:05:37, Oefeningen 20:10): E06 #1 005 afleider 925% → 9,25%. De kommatekst «Staat de komma goed? … twee plekken naar
# rechts, niet één of drie» is alleen waar als de sleutel de komma één plek te weinig of te veel verschoven heeft: sleutel = antwoord : 10 of × 10.
# Voor elk E06 #1-item met die tekst; en 005 moet een sleutel met die tekst hebben (de afleider komma-verschoven).
if MUT == 'M_1060': f_ = next(f for f in IT(E06, '005')['foutHints'] if 'niet één of drie' in f['uitleg']); f_['fout'] = '0,0925%'
for x in ITEMS:
    if x['doelId'] != E06 or x['merge']['somtypeNrOrigineel'] != 1: continue
    a_ = val(x['antwoord'])
    for f_ in x['foutHints']:
        if 'niet één of drie' not in f_['uitleg']: continue
        v_ = val(f_['fout'])
        if not a_ or v_ is None or v_ / a_ not in (Fr(1, 10), Fr(10)): fail(f"V-#1060 VERH-E06 #1 {x['nr']} {f_['fout']!r}: tekst 'komma niet één of drie plekken' klopt niet (antwoord {x['antwoord']})")
    if x['nr'] == '005' and not any('niet één of drie' in f_['uitleg'] for f_ in x['foutHints']): fail("V-#1060 VERH-E06 #1 005: geen sleutel met de kommatekst")
# ---- verklaptoets (meerkeuze) ----
if MUT == 'M_260': x_ = IT(E04, '032'); x_['hint'] = {'60 kinderen': 'Zestig', '90 kinderen': 'Negentig'}.get(x_['antwoord'], 'Zestig') + ' is het goede aantal kinderen.'   # r1b: getalwoord bij het antwoord
if MUT == 'M_824': IT(E01, '001')['sterkereHint'] += ' Zes op de tien is rood.'
if MUT == 'M_264': IT(V01, '001')['hint'] = 'Procent betekent: zoveel van de honderd. Denk aan dertig.'
if MUT == 'M_264h2': IT(E06, '002')['sterkereHint'] = 'Doe het kommagetal keer honderd: dan krijg je zevenenvijftig komma vijf, dus 57,5.'   # les 264 op de H2
andere = collections.Counter(); per_soort = collections.Counter(); KOP_DING = {}; pos = collections.Counter()
STOP260 = set('de het een en van dat die dit is je zijn er in op om te met als of aan bij dan doe doen naar door voor wat welke hoe hoeveel niet geen nog ook maar wel zo eerst daarna dezelfde elke elk alle hetzelfde kijk reken uit welk antwoord getal getallen manier aanpak klopt kan moet moest had hij zij ze waar'.split())
GETALWOORD = dict(zip('één twee drie vier vijf zes zeven acht negen tien elf twaalf dertien veertien vijftien zestien zeventien achttien negentien twintig'.split(), map(str, range(1, 21))))
GETALWOORD.update({'dertig': '30', 'veertig': '40', 'vijftig': '50', 'zestig': '60', 'zeventig': '70', 'tachtig': '80', 'negentig': '90', 'honderd': '100', 'duizend': '1000'})
def getallen(t):
    """hele getaltokens (met komma één token: '2,5' is niet '2'); getalwoorden als cijfers (b8: de opties zijn getallen, de teksten hebben geen cijfers)"""
    return set(re.findall(r'\d+(?:,\d+)?', t.replace('.', ''))) | {GETALWOORD[w] for w in re.findall(r'[^\W\d_]+', t.lower()) if w in GETALWOORD}
def stems260(t): return {w[:5] for w in re.findall(r'[^\W\d_]{3,}', t.lower()) if w not in STOP260 and w not in GETALWOORD} | getallen(t)
def woorden824(t): return [GETALWOORD.get(w, w) for w in re.findall(r'[^\W\d_]+|\d+(?:,\d+)?', t.lower())]
def t264(t): return stems260(t) | ({'helft'} if re.search(r'\bhelft\b', t, re.I) else set())
KM_GROEP, CM_GROEP, M_GROEP = {1, 2, 3, 8, 11}, {4, 5, 6}, {7, 9, 10}
for x in ITEMS:
  doel = x['doelId']; nro = x['merge']['somtypeNrOrigineel']; o = x['opgave'].replace('\n', ' '); nid = f"{doel[3:]} #{nro} {x['nr']}"
  try:
    ops = [p['tekst'] for p in x.get('opties') or []]; mk = x['type'] == 'meerkeuze'
    if not x.get('hint') or not x.get('sterkereHint'): fail(f'{nid}: H1/H2 leeg'); continue   # geen hints (kop gesplitst): verder niets te checken, geen crash-regel (mutrun)
    def eis(c, m):
        if not c: fail(f'{nid} data: {m} — klopt niet voor {o!r} => {x["antwoord"]}')
    for veld_, w_ in [('opgave', o), ('antwoord', x['antwoord'])] + [('optie', p) for p in ops]:
        if re.search(r'\b\d{1,2}:\d{2}\b', w_): fail(f"les 262 {nid} {veld_}: kloktijd met ':' ({w_!r}); G8: 15.00 uur")
    a = val(x['antwoord']); g = nums(o); ok = {}; routes = {}
    dk = {f_['fout']: f_['denkfout'] for f_ in x['extraVelden'].get('claudeDenkfouten') or []}
    for f_ in dk:
        if f_.startswith('€') and not x['antwoord'].strip().startswith('€'): EURO[(doel[3:], nro)] += 1
    if mk:
        if x['antwoord'] not in ops: fail(f'{nid}: antwoord niet in de opties'); continue
        if not x.get('husselen'): fail(f'{nid}: meerkeuze zonder husselen')
        pos[ops.index(x['antwoord'])] += 1
    elif ops: fail(f'{nid}: kaal item met opties')
    if doel == E03:
        m_ = re.search(r'schaal (?:van een kaart is |)1 : (\d{1,3}(?:\.\d{3})*)(?!\d)', o)
        eis(m_ is not None, "H1/H2: 'de schaal met een dubbele punt'")
        if m_ is None: continue
        S = num(m_.group(1)); eis(S % 100 == 0, "H2: 'streep nullen weg' (de schaal eindigt op nullen)")
        if nro in KM_GROEP | M_GROEP:
            mc = re.search(r'(\d+) cm\b', o); eis(mc is not None and 'op de kaart' in o or 'Op een kaart' in o, 'afstand op de kaart in cm')
            cm = Fr(int(mc.group(1))) if mc else None
        if nro in KM_GROEP:
            eis(re.search(r'Hoeveel (km|kilometer) is dat in het echt\?', o) is not None, 'vraag in km')
            eis(S % 100000 == 0, "H2: 'streep vijf nullen weg: zoveel kilometer is één centimeter'")
            k1 = S / 100000; eis(a == cm * k1, "H2: 'één cm = de schaal zonder vijf nullen, keer het aantal cm' = het antwoord")
            ok = {'meters': lambda v: v == a * 1000, 'tien keer te veel': lambda v: v == a * 10, 'tien keer te weinig': lambda v: v * 10 == a,
                  'getal uit de vraag': lambda v: v in g, 'andere omrekening': lambda v: v in (a * 10, a / 10, cm / k1)}
            routes = {'meters': a * 1000, 'tien keer te veel': a * 10, 'tien keer te weinig': a / 10}
            routes.update({'getal uit de vraag (cm)': cm})     # V-#971 (les 306/365): ook bij #8/#11; 1 : 100.000 geeft hier een FAIL (data V-#970)
            if k1 != 1: routes.update({'gedeeld door de km per cm': cm / k1})
            if cm != a:   # V-#971: kan het getal uit de vraag niet op het antwoord vallen, dan dezelfde regels als #1–#3
                mist_ = {'getal uit de vraag', 'tien keer te weinig'} - {f_['soort'] for f_ in BT[EK(x)]['foutHints']}
                if mist_: fail(f"V-#971 {nid}: regels {sorted(mist_)} ontbreken (zelfde regels als #1–#3)")
        elif nro in CM_GROEP:
            mk_ = re.search(r'in het echt (\d+) km uit elkaar\. Hoeveel cm is dat op de kaart\?', o); eis(mk_ is not None, 'echte afstand in km, vraag in cm op de kaart')
            if mk_ is None: continue
            km = Fr(int(mk_.group(1))); eis(S % 100000 == 0, "H2: 'streep vijf nullen weg'"); k1 = S / 100000
            eis(a == km / k1, "H2: 'hoe vaak past de km per cm in de echte afstand' = het antwoord")
            ok = {'tien keer te veel': lambda v: v == a * 10, 'tien keer te weinig': lambda v: v * 10 == a, 'getal uit de vraag': lambda v: v in g,
                  'andere omrekening': lambda v: v in (a * 10, a / 10, km * k1)}
            routes = {'tien keer te veel': a * 10, 'tien keer te weinig': a / 10, 'getal uit de vraag (km)': km, 'keer de km per cm': km * k1}
        else:
            eis(re.search(r'Hoeveel meter is dat in het echt\?', o) is not None, 'vraag in meter')
            eis(a == cm * S / 100, "H2: 'cm keer de schaal, dan twee nullen weg' = het antwoord")
            ok = {'nog in centimeters': lambda v: v == a * 100, 'tien keer te veel': lambda v: v == a * 10, 'tien keer te weinig': lambda v: v * 10 == a,
                  'andere omrekening': lambda v: v in (a * 100, a * 10, a / 10)}
            routes = {'nog in centimeters': a * 100, 'tien keer te veel': a * 10, 'tien keer te weinig': a / 10}
    elif doel == E04 and nro in (1, 6):
        m_ = re.search(r'kost na (\d+)% korting €(\d+)\. Wat was de prijs vóór de korting\?', o); eis(m_ is not None, "H1/H2: korting in procent, nieuwe prijs in euro")
        if m_ is None: continue
        p_, n_ = int(m_.group(1)), Fr(int(m_.group(2))); eis(0 < p_ < 100 and a == n_ * 100 / (100 - p_), "H2: 'honderd min het procent = de nieuwe prijs; één procent keer honderd' = het antwoord")
        erbij = n_ * (100 + p_) / 100
        def _erbij(v, erbij=erbij, nr=x['nr']):
            if v == erbij: return True
            if abs(v - erbij) < 1 and v.denominator == 1: AFGEROND.append(f"{nr}: {float(erbij):g} → {v}"); return True
            return False
        ok = {'nieuwe prijs': lambda v: v == n_, 'procent van de nieuwe prijs': _erbij}
        routes = {'nieuwe prijs': n_, 'procent van de nieuwe prijs': erbij}
    elif doel == E04 and nro in (2, 3, 4, 5, 7):
        m_ = re.search(r'zet €(\d+) op een spaarrekening met (\d+)% rente per jaar\. Hoeveel rente krijgt (?:hij|ze|het) na één jaar\?', o)
        eis(m_ is not None, "H1/H2: bedrag op de rekening, procent rente, één jaar")
        if m_ is None: continue
        B_, p_ = Fr(int(m_.group(1))), Fr(int(m_.group(2))); eis(a == B_ * p_ / 100, "H2: 'bedrag gedeeld door honderd, keer het procent' = het antwoord")
        ok = {'tien keer te veel': lambda v: v == a * 10, 'bedrag erbij': lambda v: v == B_ + a, 'procent als bedrag': lambda v: v == p_}
        routes = dict((k_, w_) for k_, w_ in (('tien keer te veel', a * 10), ('bedrag erbij', B_ + a), ('procent als bedrag', p_)))
    elif doel == E04 and nro == 8:
        m_ = re.search(r'Van de (\d+) kinderen op school komt (\d+) procent met de fiets\.', o); eis(m_ is not None, "H1/H2: aantal op school, procent")
        if m_ is None: continue
        N_, p_ = int(m_.group(1)), int(m_.group(2)); eis(a == Fr(N_ * p_, 100) and N_ % 10 == 0, "H2: 'tien procent = het aantal gedeeld door tien; zo vaak als nodig' = het antwoord")
        ok = {'procent als aantal': lambda v: v == f'{p_} kinderen', 'te veel': lambda v: val(v) > a, 'geheel min het procent': lambda v: v == f'{N_ - p_} kinderen'}
        routes = {'procent als aantal': Fr(p_), 'geheel min het procent': Fr(N_ - p_)}   # ronde 1b (Oef-#1010, build 17:47)
        if N_ - p_ == a: fail(f"les 306 {nid}: de foute route 'geheel min het procent' ({N_} − {p_}) geeft het goede antwoord (datapunt Oef-#1010: andere getallen)")
        for p in ops:
            if p != x['antwoord'] and val(p) not in (Fr(p_), Fr(N_ - p_)): GEEN_ROUTE.append(f'{nid} {p!r}')
    elif doel == E06 and nro == 1:
        m_ = re.fullmatch(r'Schrijf (\d+,\d+) in procenten\.', o); eis(m_ is not None, "H2: 'het kommagetal keer honderd'")
        if m_ is None: continue
        k_ = Fr(m_.group(1).replace(',', '.')); eis(a == k_ * 100 and x['antwoord'].endswith('%'), "H2: 'keer honderd, procentteken erachter' = het antwoord")
        ok = {'kommagetal met procentteken': lambda v: v == f'{m_.group(1)}%', 'komma verschoven': lambda v: val(v) in (a * 10, a / 10)}
        routes = {'kommagetal met procentteken': k_, 'één plek': a / 10, 'drie plekken': a * 10}
    elif doel == E06 and nro == 2:
        m_ = re.fullmatch(r'Schrijf (\d+)/(\d+) in procenten\.', o); eis(m_ is not None, "H1/H2: een breuk")
        if m_ is None: continue
        t_, n_ = int(m_.group(1)), int(m_.group(2)); eis(a == Fr(t_ * 100, n_), "H2: 'noemer naar honderd, teller hetzelfde' = het antwoord")
        eis(n_ != 100, "L1 'dat klopt alleen als de noemer honderd is' (de noemer is geen honderd)")
        gb = lambda v: val(v) in (t_, n_) and v.endswith('%')
        ok = {'getal uit de breuk': lambda v: val(v) == t_ and v.endswith('%'), 'getal uit de breuk (kommaprocent)': lambda v: val(v) == t_ and v.endswith('%'), 'getal uit de breuk (noemer)': lambda v: val(v) == n_ and v.endswith('%'),   # V-#982: teller en noemer apart
              'tien keer ernaast': lambda v: val(v) in (a * 10, a / 10), 'tien keer te groot': lambda v: val(v) == a * 10 and v.endswith('%')}   # 1c: V-#1000
        for p in ops:   # V-#1000 (ronde 1c): een optie '× 10' hoort op de eigen regel 'tien keer te groot'
            if p != x['antwoord'] and val(p) == a * 10 and not (len([f_ for f_ in x['foutHints'] if f_['fout'] == p]) == 1 and next(f_['soort'] for f_ in x['foutHints'] if f_['fout'] == p).startswith('tien keer te groot')):
                fail(f"V-#1000 {nid} {p!r}: optie '× 10' niet op 'tien keer te groot' ({[f_['soort'] for f_ in x['foutHints'] if f_['fout'] == p]})")
        for fh_ in x['foutHints']:
            if 'Een breuk kleiner dan één' in fh_['uitleg'] and not (t_ < n_ and val(fh_['fout']) > 100 and 100 % n_ == 0):
                fail(f"V-#1000 tekst {nid} {fh_['fout']!r}: 'breuk kleiner dan één / de noemer past in honderd' klopt niet voor {t_}/{n_}")
            if fh_['uitleg'].startswith('Dat is tien keer te klein') and val(fh_['fout']) * 10 != a: fail(f"Z-#983 {nid} {fh_['fout']!r}: tekst 'tien keer te klein', maar de sleutel is geen antwoord : 10")
            if fh_['uitleg'].startswith('Dat is tien keer te groot.') and val(fh_['fout']) != a * 10: fail(f"Z-#983 {nid} {fh_['fout']!r}: tekst 'tien keer te groot', maar de sleutel is geen antwoord × 10")
        for fh_ in x['foutHints']:   # les 373: de tekst zegt of het de teller of de noemer is
            if fh_['soort'] == 'getal uit de breuk (noemer)' and not fh_['uitleg'].startswith('Dat is de noemer'): fail(f"les 373 {nid} {fh_['fout']!r}: tekst noemt de noemer niet: {fh_['uitleg']}")
            if fh_['soort'] in ('getal uit de breuk', 'getal uit de breuk (kommaprocent)') and not fh_['uitleg'].startswith('Dat is de teller'): fail(f"les 373 {nid} {fh_['fout']!r}: tekst noemt de teller niet: {fh_['uitleg']}")
        routes = {'teller': Fr(t_), 'noemer': Fr(n_), 'tien keer groter': a * 10, 'tien keer kleiner': a / 10}
    elif doel == E06 and nro == 3:
        m_ = re.fullmatch(r'(\d+(?:,\d+)?)% van de [\w ]+ is (?:kapot|rot|\w+)\. Schrijf dat als kommagetal\.', o)   # Oef-#1008 (build 17:47): '… van de appels in de kist is rot'; eis(m_ is not None, "H2: 'het getal van het procent door honderd'")
        if m_ is None: continue
        P_ = Fr(m_.group(1).replace(',', '.')); eis(a == P_ / 100, "H2: 'door honderd' = het antwoord"); eis(a < 1, "H2: 'geen heel getal? zet een nul voor de komma'")
        def _kv(v, a=a, nr=x['nr']):
            if v in (a * 10, a / 10): return True
            if abs(v - a * 10) <= Fr(5, 100) and v != a * 10: AFGEROND.append(f"E06 #3 {nr}: {float(a * 10):g} → {float(v):g} (afgerond, geen schuif)"); return True
            return False
        ok = {'tien keer te groot': lambda v: v == a * 10, 'procent zonder komma': lambda v: v == P_, 'procent zonder komma (punt)': lambda v: v == P_, 'komma verschoven': _kv}
        routes = {'tien keer te groot': a * 10, 'procent zonder komma': P_}
    elif doel == V01:
        m_ = re.search(r'zeggen (\d+) van de (\d+) kinderen dat', o); eis(m_ is not None, "H1/H2: deel en hele aantal")
        if m_ is None: continue
        d_, N_ = int(m_.group(1)), int(m_.group(2)); eis(a == Fr(d_ * 100, N_), "H2: 'verhoudingstabel, het hele aantal bij honderd procent' = het antwoord")
        ok = {'aantal als procent': lambda v: v == f'{d_} procent', 'tien keer te klein': lambda v: val(v) * 10 == a}
        routes = {'aantal als procent': Fr(d_), 'tien keer te klein': a / 10}
    elif doel == E01:
        m_ = re.fullmatch(r'In een bak zitten (\d+) (\w+), (\d+) (\w+) en (\d+) (\w+) knikker\. Welk deel van de knikkers is (\w+)\?', o)
        eis(m_ is not None, "H1/H2: drie kleuren, de vraag noemt er één")
        if m_ is None: continue
        def _bijv(w): return {w + 'e', re.sub(r'([aeou])\1(\w)$', r'\1\2', w) + 'e', w + w[-1:] + 'e', w}   # rood → rode, wit → witte, oranje
        kl = {m_.group(2): int(m_.group(1)), m_.group(4): int(m_.group(3)), m_.group(6): int(m_.group(5))}; tot = sum(kl.values())
        r_ = next((n for k, n in kl.items() if k in _bijv(m_.group(7))), None)
        eis(r_ is not None and x['antwoord'] == f'{r_} op de {tot}', "H2: 'het aantal met die kleur tegenover alle knikkers' = het antwoord")
        ok = {'zonder het deel': lambda v: v == f'{r_} op de {tot - r_}', 'andere kleur': lambda v: any(v == f'{n} op de {tot}' for k, n in kl.items() if n != r_)}
    elif doel == E02:
        m_ = re.search(r'kosten (\d+) pakken sap samen €(\d+,\d+)\. Hoeveel kosten (\d+) van die pakken sap\?', o); eis(m_ is not None, "H1/H2: prijs van een aantal, nieuw aantal")
        if m_ is None: continue
        n_, P_, m2 = int(m_.group(1)), Fr(m_.group(2).replace(',', '.')), int(m_.group(3)); eis(a == P_ / n_ * m2, "H2: 'prijs gedeeld door het aantal, keer het nieuwe aantal' = het antwoord")
        ok = {'een klein bedrag erbij': lambda v: P_ < val(v) < a, 'keer het nieuwe aantal': lambda v: val(v) == P_ * m2}
        routes = {'keer het nieuwe aantal': P_ * m2}
        cu_ = x['extraVelden'].get('claudeUitleg') or ''
        if re.search(r'\bpet\b', cu_) or re.search(r'\d x \d', cu_): I.append(f"INFO {nid}: claudeUitleg {cu_!r}: 'pet' in plaats van 'pak', 'x' in plaats van '×' (datapunt Oef-#1011)")
    else:
        fail(f'{nid}: geen check voor dit somtype')
    if mk:   # les 301/371 (Z-#984): één foute optie hoort bij hoogstens één route
        for p in ops:
            rr_ = [r_ for r_, w_ in routes.items() if p != x['antwoord'] and w_ is not None and val(p) == w_]
            if len(rr_) > 1: fail(f'les 301 {nid} {p!r}: hoort bij twee routes {rr_}')
        nd_ = lambda p: len(re.search(r'(?:,(\d+))?\D*$', p).group(1) or '')
        if [nd_(p) for p in ops].count(nd_(x['antwoord'])) == 1: VORMCUE[(doel[3:], nro)] += 1
    for r_, w_ in routes.items():   # les 306
        if w_ is not None and a is not None and w_ == a: fail(f'les 306 {nid}: de foute route {r_!r} geeft het goede antwoord')
    # ---- sleutels ----
    gedekt = collections.Counter()
    for fh in x['foutHints']:
        s = fh['soort']; per_soort[(doel[3:], nro, s)] += 1
        if not fh.get('uitlegSterker'): fail(f"{nid} {fh['fout']!r}: geen laag 2")
        if fh['fout'] == x['antwoord']: fail(f'{nid}: fout-hint op het goede antwoord'); continue
        if mk:
            if fh['fout'] not in ops: fail(f"{nid}: fout-hint {fh['fout']!r} is geen optie"); continue
            if s == 'andere fout': fail(f"{nid} {fh['fout']!r}: meerkeuze-optie op 'andere fout' (verwacht: een eigen regel)"); continue
            if not fh['regel'].startswith(('fout = ', 'Claudes sleutel')):
                pakt = [p for p in ops if past(fh['regel'], p)]
                if pakt != [fh['fout']]: fail(f"{nid} regel {fh['regel']!r}: pakt {pakt} in plaats van alleen {fh['fout']!r} (les 160/161)")
            gedekt[fh['fout']] += 1
            f_ = ok.get(s) or (ok.get('tien keer te groot') if s.startswith('tien keer te groot (') else None)   # 1c: soort per optie
            if f_ is None: fail(f"{nid} {fh['fout']!r}: soort {s!r} heeft geen check"); continue
            if not f_(fh['fout']): fail(f"{nid} {fh['fout']!r}: soort {s!r} klopt niet bij deze optie (antwoord {x['antwoord']!r})")
            continue
        v = val(fh['fout'], noteer=(doel, nro, x['nr'], fh['fout'], s))
        if v is None: fail(f"{nid} sleutel {fh['fout']!r}: niet te lezen"); continue
        if v == a: fail(f"{nid}: sleutel {fh['fout']!r} = het antwoord (op waarde)"); continue
        if s == 'andere fout':
            r_ = next((r for r, w in routes.items() if w == v), 'overig'); andere[(doel[3:], nro, r_)] += 1; continue
        f_ = ok.get(s)
        if f_ is None: fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} heeft geen check"); continue
        if not f_(v): fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} klopt niet (antwoord {x['antwoord']})")
    if mk:
        for p in ops:
            if p != x['antwoord'] and gedekt[p] != 1: fail(f'{nid}: foute optie {p!r} heeft {gedekt[p]} fout-hints (verwacht 1)')
        for L_, h_ in (('H1', x['hint']), ('H2', x['sterkereHint'])):
            sc_ = {p: len(stems260(p) & stems260(h_)) for p in ops}
            if sc_[x['antwoord']] >= 2 and sc_[x['antwoord']] > max(v_ for p, v_ in sc_.items() if p != x['antwoord']): fail(f"les 260 {nid} {L_}: beschrijft het goede antwoord: {h_}")
        eigen_ = stems260(x['antwoord']) - set().union(*[stems260(p) for p in ops if p != x['antwoord']]) - stems260(o)
        wa_ = woorden824(x['antwoord'])
        for L_, h_ in (('H1', x['hint']), ('H2', x['sterkereHint'])):
            if len(eigen_ & stems260(h_)) >= 2: fail(f"Z-#824 {nid} {L_}: noemt {sorted(eigen_ & stems260(h_))} uit het goede antwoord (alleen daar): {h_}")
            wh_ = ' '.join(woorden824(h_)); k_ = min(5, len(wa_))
            if len(wa_) >= 2 and any(' '.join(wa_[i:i + k_]) in wh_ for i in range(len(wa_) - k_ + 1)): fail(f"Z-#824 {nid} {L_}: neemt een stuk van het goede antwoord letterlijk over: {h_}")
            for w_ in t264(h_) - t264(o):      # les 264 op H1 én H2 (b7 ronde 1b)
                if [p for p in ops if w_ in t264(p)] == [x['antwoord']]: fail(f"les 264 {nid} {L_}: {w_!r} staat alleen in het goede antwoord: {h_}")
    # [..]-woorden uit de opgave (les 147)
    kop = re.sub(r'^\[(?!(?:wie|ding|plek|naam)\])[^\]]+\]\s*', '', x['merge']['somtype']).replace(' ⏎ ', ' '); vast = set(re.findall(r'\w+', re.sub(r'\[\w+\]', ' ', kop).lower()))
    pat = re.sub(r'\\\[\w+\\\]', '(.+?)', re.escape(kop).replace(r'\#', r'[\d.,]+'))
    pat = re.sub(r'krijgt\\\\? (?:hij|het|ze|zij)\b', r'krijgt\\ (?:hij|het|ze|zij)', pat)   # Z-#985: 'Een kind … het' en '[wie] … hij' onder één kop
    m = re.fullmatch(pat, o)
    if m is None and '[' in kop: W.append(f'{nid}: kop past niet op de opgave (contextwoorden niet bepaald)')
    KOP_DING.setdefault(EK(x), set()).update({w for grp in (m.groups() if m else ()) for w in re.findall(r'[^\W\d]{3,}', grp.lower())} - vast - {'een', 'het', 'der', 'bij', 'van', 'aan', 'met', 'voor', 'naar', 'uit'})
  except Exception as e_:      # les 353: een predicaat crasht niet, het geeft een FAIL
    fail(f'les 353 {nid}: de check crasht op dit item ({type(e_).__name__}: {e_})')
I.append('INFO sleutels per soort: ' + '; '.join(f'{k[0]} #{k[1]} {k[2]}={n}' for k, n in sorted(per_soort.items())))
I.append("INFO 'andere fout' per route (datapunt): " + '; '.join(f'{k[0]} #{k[1]} {k[2]}={n}' for k, n in sorted(andere.items())))
I.append(f'INFO Claude-sleutels met een punt als komma (datapunt): {len(PUNT)} ' + '; '.join(f'{p[0][3:]} #{p[1]} {p[2]} {p[3]!r}→{p[4]}' for p in PUNT))
I.append(f"INFO Claude-sleutels met '€' bij een antwoord zonder '€' (datapunt Oef-#1006): " + '; '.join(f'{k[0]} #{k[1]}={n}' for k, n in sorted(EURO.items())))
I.append(f'INFO afgeronde Claude-sleutels (datapunt Oef-#1006): {len(AFGEROND)} {AFGEROND}')
I.append(f'INFO foute opties zonder route (les 317, datapunt): {GEEN_ROUTE}')
I.append('INFO vormcue (les 372, Z-#984/V-#984 Overzicht): alleen de goede optie heeft dit aantal decimalen: ' + '; '.join(f'{k[0]} #{k[1]}={n}' for k, n in sorted(VORMCUE.items())))
I.append(f'INFO meerkeuze: plek van het goede antwoord in de data {dict(sorted(pos.items()))}')
# ---- teksten ----
TOEGESTAAN = {}
EENHEID = {'kilometer', 'meter', 'centimeter', 'km', 'cm'}   # maateenheden zijn geen contextwoorden (kop #8/#11 'kilometer', #1–#3 'km')
TXT = []
for s in B['somtypen']:
    k_ = (s['doel'], s['nrOrigineel'])
    TXT += [(k_, 'H1', s['hint1']), (k_, 'H2', s['hint2']), (k_, 'OZ', s['ouderzin'])]
    for f in s['foutHints']:
        for i_, t_ in enumerate(f['tekst'].split(' / ')): TXT.append((k_, f"L1 {f['soort']}" + (f' ({i_})' if ' / ' in f['tekst'] else ''), t_))
        TXT.append((k_, f"L2 {f['soort']}", f.get('tekstSterker') or ''))
        if not f.get('tekstSterker'): fail(f"{k_} {f['soort']}: geen tekstSterker")
    if s['foutHints'][-1]['soort'] != 'andere fout': fail(f"{k_}: 'andere fout' niet als laatste")
MUTS = {'M_cijfer': ((E03, 1), 'Deel door 100.000.'), 'M_letter': ((V01, 1), 'Kies optie B.'), 'M_plek': ((E01, 1), 'Kijk naar het eerste getal.'), 'M_zoveel': ((E04, 2), 'Zoveel krijg je erbij.'),
        'M_217': ((E04, 1), 'Hier tel je niets op, je doet alleen keer.'), 'M_231': ((E06, 1), 'Doe het zoals bij de vorige som.'),
        'M_ctx': ((E04, 2), 'Hoeveel krijgt Sanne erbij?'), 'M_ctx2': ((E06, 3), 'Kijk in de kist.'), 'M_ctx3': ((E01, 1), 'Tel de rode knikkers.'), 'M_ctx4': ((E04, 3), 'Daan krijgt er geld bij.'),
        'M_ctx5': ((E03, 7), 'Hoe ver is de gymzaal?'), 'M_ctx6': ((E03, 1), 'Hoe ver liggen de steden uit elkaar?'), 'M_ctx7': ((E04, 1), 'Wat kostte de trui eerst?'),
        'M_moeilijk': ((E03, 4), 'Vermenigvuldig het getal.'), 'M_Bijna': ((E06, 2), 'Bijna goed!'), 'M_woorden': ((E03, 2), 'Streep de nullen weg en reken verder. ' * 8),
        'M_235': ((E01, 1), 'Tel de knikkers. Tel de knikkers.'), 'M_klokw': ((E04, 7), 'Om half drie ben je klaar.'), 'M_deel': ((E04, 2), 'Reken 800 : 100 uit.'), 'M_192': ((E02, 1), 'Elk kost even veel.')}
if MUT in MUTS: TXT.append((MUTS[MUT][0], 'L1 mutant', MUTS[MUT][1]))
LES217B = re.compile(r"\b(optellen|aftrekken|plus|min|keer|delen|erbij|eraf|vermenigvuldigen)\b[^.?!]{0,20}\b(is\s+(hier\s+)?niet\s+goed|mag\s+(hier\s+)?niet)\b"
                     r"|\b(mag|mogen)\s+(je\s+)?(hier\s+)?niet\s+(op\s*tellen|optellen|aftrekken|plus|erbij|keer|delen)\b|\b(niets|niet|nooit|geen)\b[^.?!]{0,25}\bop\s+te\s+tellen\b", re.I)
KOPS = collections.defaultdict(dict)
for x in ITEMS: KOPS[x['doelId']][EK(x)[1]] = x['merge']['somtype']
GROEP_VERBODEN = {}
for doel_, kops_ in KOPS.items():
    grp = collections.defaultdict(list)
    for n_ in kops_: grp[(BT[(doel_, n_)]['hint1'], BT[(doel_, n_)]['hint2'])].append(n_)
    for ns_ in grp.values():
        if len(ns_) < 2: continue
        ws_ = [set(re.findall(r'[^\W\d]{3,}', re.sub(r'\[[^\]]+\]', ' ', kops_[n_]).lower())) for n_ in ns_]
        for n_ in ns_: GROEP_VERBODEN[(doel_, n_)] = set.union(*ws_) - set.intersection(*ws_) - STOP260 - EENHEID
KLOKWOORD = re.compile(r'\bhalf (een|één|twee|drie|vier|vijf|zes|zeven|acht|negen|tien|elf|twaalf)\b|\bkwart (over|voor)\b|\b(twee|drie|vier|vijf|zes|zeven|acht|negen|tien|elf|twaalf) uur\b', re.I)
for k_, lab, t in TXT:
    tag = f'{k_[0][3:]} nrO{k_[1]} [{lab}]'
    if KLOKWOORD.search(t): fail(f'les 262 {tag}: kloktijd in woorden in een kindtekst: {t}')
    for w in GROEP_VERBODEN.get(k_, ()):
        if lab != 'OZ' and re.search(rf'\b{re.escape(w)}\b', t, re.I): fail(f'les 147 {tag}: kopwoord {w!r} geldt niet voor elk somtype met deze tekst: {t}')
    if lab != 'OZ' and re.search(r'\d', t): fail(f'{tag}: cijfer in de tekst: {t}')
    if re.search(r'\b(optie|antwoord) [A-D]\b|\b[A-D]\)|(?<![\w’\'])[A-D](?![\w’\'])', t): fail(f'{tag}: optieletter: {t}')
    if '÷' in t or re.search(r'\d\s*:\s*[€−]?\d|\d%?: ', t): fail(f'{tag}: deelteken of dubbele punt bij een getal: {t}')
    if re.search(r'\b(eerste|tweede|derde|laatste|vooraan|achteraan|bovenste|onderste)\b(?! cijfer\b)', t, re.I): fail(f'les 193 {tag}: plekwoord: {t}')
    if re.search(r"(tel je niets op|je telt niets op|niets op ?tellen|niet optellen|alleen keer|niet om erbij|nooit (optellen|erbij)|geen plus doen)", t, re.I) or LES217B.search(t): fail(f'les 217 {tag}: sluit een bewerking uit: {t}')
    if re.match(r'\s*zoveel\b', t, re.I): fail(f"les 197/272 {tag}: 'zoveel' vooraan: {t}")
    if re.search(r'\b(zoals bij|net als bij|de vorige (som|vraag|opgave)|andere strategie|die strategie)\b', t, re.I): fail(f'les 231 {tag}: verwijst naar een andere som of strategie: {t}')
    if re.search(r'\beven ?veel\b', t, re.I) and lab != 'OZ': fail(f"#192 {tag}: 'even veel': {t}")
    if lab != 'OZ':
        for w in KOP_DING.get(k_, ()):
            if w in TOEGESTAAN.get(k_, ()): continue
            stam = re.sub(r'(jes|en|s)$', '', w); stam = stam if len(stam) >= 4 else w; stam2 = re.sub(r'([aeou])([^aeiou\W])$', r'\1\1\2', stam)
            if re.search(rf'\b({re.escape(w)}|({re.escape(stam)}|{re.escape(stam2)})(je|jes|en|s|e)?)\b', t, re.I): fail(f'les 147 {tag}: contextwoord {w!r} uit een [..]-plek: {t}')
    if (m := MOEILIJK.search(t)): fail(f'{tag}: moeilijk woord {m.group(1)!r}: {t}')
    if re.search(r'\bbijna\b', t, re.I) and lab != 'OZ': fail(f"{tag}: 'Bijna': {t}")
    nw_ = len(t.split()); max_ = 55 if lab.startswith(('H2', 'L2')) else 45 if lab.startswith(('H1', 'L1')) else None
    if max_ and nw_ > max_: fail(f'V-#764 {tag}: {nw_} woorden (maximaal {max_}): {t[:80]}')
    zz_ = [z.strip() for z in re.split(r'(?<=[.?!])\s+', t) if z.strip()]
    if len(zz_) != len(set(zz_)): fail(f'les 235 {tag}: dezelfde zin twee keer: {t[:80]}')
    lang = [z for z in zz_ if len(z.split()) > 25]
    if lang: W.append(f'{tag}: lange zin ({len(lang[0].split())} woorden): {lang[0]}')
I.append('INFO contextwoorden: ' + '; '.join(f'{k[0][3:]} nrO{k[1]} {sorted(v)}' for k, v in sorted(KOP_DING.items()) if v))
SNAP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/opties_snapshot.json'
OPTS = {f"{x['doelId']} {x['nr']}": sorted(o_['tekst'] for o_ in (x.get('opties') or [])) for x in ITEMS if x.get('opties')}
if MUT == 'M_afl': k0_ = sorted(OPTS)[0]; OPTS[k0_] = OPTS[k0_][:-1] + ['iets anders']
# Z-#973 (Didactiek b8 deel A): na de motorwijziging (fout_regels 'Z-#973', Overzicht 17:56) horen Claude-sleutels = antwoord : 10 op 'tien keer te weinig',
# niet meer op CL 'andere omrekening'. Voorwaardelijk: zonder de motorwijziging alleen INFO (dan is CL de enige tekst).
MOTOR973 = 'Z-#973' in open(os.path.join(G8, 'scripts', 'fout_regels.py'), encoding='utf-8').read()
if MUT == 'M_973': next(f for f in IT('G8-VERH-E03', '167')['foutHints'] if f['fout'] == '2,4')['soort'] = 'andere omrekening'
Z973 = []
for x in ITEMS:
    if x['doelId'] != 'G8-VERH-E03' or not re.fullmatch(r'\d+', x['antwoord'].replace('.', '')) or x['antwoord'].replace('.', '').endswith('0'): continue
    w_ = Fr(int(x['antwoord'].replace('.', '')), 10)
    for f in x['foutHints']:
        try: v_ = num(f['fout'].replace(' km', '').replace(' cm', '').strip())
        except Exception: continue
        if v_ == w_ and f['soort'] != 'tien keer te weinig': Z973.append(f"{x['nr']} {f['fout']!r}→{f['soort']}")
if MOTOR973 and Z973: fail(f'Z-#973 VERH-E03: sleutel = antwoord : 10 niet op \'tien keer te weinig\': {len(Z973)} {Z973[:6]}')
elif Z973: I.append(f'INFO Z-#973 (wacht op de motor): {len(Z973)} sleutels = antwoord : 10 op een andere soort')
else: I.append(f'INFO Z-#973: motor {"aan" if MOTOR973 else "uit"}, 0 sleutels = antwoord : 10 buiten \'tien keer te weinig\'')
_EPK = collections.Counter((s_['doel'], s_.get('somtype')) for s_ in B['somtypen'])   # r1d (Oef-#1014, sync #30): elke kop van een item heeft precies één entry
for k_ in sorted({(x['doelId'], x['merge']['somtype']) for x in ITEMS}):
    if _EPK[k_] != 1: fail(f"Oef-#1014 {k_[0][3:]} kop '{k_[1][:70]}': {_EPK[k_]} hint-entries (verwacht 1; sync_hint_keys voegt niet stil samen, apply_hints stopt)")
if ZONDER_ENTRY: fail(f'b8-doelen: {len(ZONDER_ENTRY)} items zonder hint-entry (kop gesplitst? datapunt Overzicht): {ZONDER_ENTRY}')
if os.environ.get('SNAP') == '1': json.dump(OPTS, open(SNAP, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO les 234: snapshot geschreven ({len(OPTS)} items)')
elif os.path.exists(SNAP):
    oud_ = json.load(open(SNAP))
    for k_ in sorted(set(oud_) | set(OPTS)):
        if oud_.get(k_) != OPTS.get(k_): fail(f'les 234 item {k_}: opties veranderd: routes, letterlijke regels en verklaptoets (les 300) nalopen, dan SNAP=1')
else: W.append('les 234: geen snapshot (SNAP=1 python3 check.py)')
for m in I: print(m)
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))); from l271 import les271
for m_ in les271(G8, 8, B): fail(m_)
for m in W: print('WARN', m)
for m in F: print('FAIL', m)
print(f'G8 b8: {len(ITEMS)} items · {sum(len(x["foutHints"]) for x in ITEMS)} sleutels · FAIL {len(F)} · WARN {len(W)} · INFO {len(I)}')
sys.exit(1 if F else 0)
