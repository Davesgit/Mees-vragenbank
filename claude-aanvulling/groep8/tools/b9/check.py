#!/usr/bin/env python3
"""G8 batch 9 (VERH-E05 #1–#21, VBN-V01 #1–#5: 26 somtypes, 70 items) nagespeeld op de toegepaste per_doel-data (zandbak of live). Opzet als b8.
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
E05, V01 = "G8-VERH-E05", "G8-VBN-V01"
SEL = {E05: set(range(1, 22)), V01: {1, 2, 3, 4, 5}}
RENTE, PRIJS = {2, 4, 9, 10, 20}, set(range(5, 18)) - {9, 10} | {19}
B = json.load(open(f'{G8}/hints/batch9.json'))
if MUT == 'M_1014': B['somtypen'].append(dict(next(s_ for s_ in B['somtypen'] if s_['doel'] == E05 and s_['nrOrigineel'] == 1), nrOrigineel=99))   # r1d: twee entries op één kop
BT = {(s['doel'], s['nrOrigineel']): s for s in B['somtypen']}
BKOP = {(s['doel'], s.get('somtype')): (s['doel'], s['nrOrigineel']) for s in B['somtypen']}   # r1d (G8_KOP1014): een item hoort bij de entry van zijn kop, niet per se bij zijn nrOrigineel
def EK(x): return BKOP.get((x['doelId'], x['merge']['somtype']), (x['doelId'], x['merge']['somtypeNrOrigineel']))
PUNT = []; VORMCUE = collections.Counter(); EURO = collections.Counter(); AFGEROND = []; GEEN_ROUTE = []; ZELFST = []; NUL_WEG = []
def val(k, noteer=None):
    k = str(k).strip().replace('−', '-')
    if (mc_ := re.fullmatch(r'\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)', k)): k = f'{mc_.group(1)},{mc_.group(2)}'   # V-#1025: '(1,0)' = '1,0'
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
K1024 = []
NIEUW1025 = not any((m0_ := re.search(r'\((\d+), 0\)', x['opgave'])) and x['antwoord'].strip() == m0_.group(1) for x in ITEMS if x['doelId'] == V01 and x['merge']['somtypeNrOrigineel'] == 1)
ZONDER_ENTRY = [f"{x['doelId'][3:]} nrO{x['merge']['somtypeNrOrigineel']} {x['nr']}" for doel_ in SEL for x in json.load(open(f'{G8}/data/per_doel/{doel_}.json'))['items']
                if x['merge']['somtypeNrOrigineel'] not in SEL[doel_] and x['foutHints'] and not any(f_.get('soort') for f_ in x['foutHints'])]
def FH(x, soort): return next(f for f in x['foutHints'] if f['soort'] == soort)
def FHV(x, fout): return next(f for f in x['foutHints'] if f['fout'] in (fout, fout.lstrip('€')))   # r1c: ook na V-#1026 (sleutels zonder '€')
# V-#1041 (Didactiek 19:16:10, Z-#961): E05-mutanten kiezen hun item op claudeId, niet op somtype-nummer of nr (KOP1014 nummert om)
CID_E05 = {'001': '16bb998e', '004': '086e3e19', '019': '87a69781', '041': '0783648d', '054': '7fec68da'}
def ITC(c8): return next(x for x in ITEMS if x['doelId'] == E05 and (x.get('bron') or {}).get('claudeId', '').startswith(c8))
def opg(doel, nr, oud, nieuw): x_ = IT(doel, nr); assert oud in x_['opgave'], (nr, oud); x_['opgave'] = x_['opgave'].replace(oud, nieuw)
# ---- data-mutanten (moeten FAIL geven) ----
if MUT == 'M_dprijs': opg(E05, ITC(CID_E05['004'])['nr'], 'kost nu €120', 'kost nu €130')
if MUT == 'M_drente': ITC(CID_E05['001'])['antwoord'] = '410'
if MUT == 'M_dstijg': opg(E05, ITC(CID_E05['019'])['nr'], '20%', '25%')
if MUT == 'M_daantal': opg(E05, ITC(CID_E05['041'])['nr'], 'nu 44', 'nu 46')
if MUT == 'M_ddaal': opg(E05, ITC(CID_E05['054'])['nr'], *(('vijftig broden', 'zestig broden') if 'vijftig broden' in ITC(CID_E05['054'])['opgave'] else ('48 broden', '50 broden')))   # r1c: oude en nieuwe data (V-#1023)
if MUT == 'M_drooster': opg(V01, '001', '(6, 1)', '(6, 2)')
if MUT == 'M_dlijn': opg(V01, '013', 'tussen 12.00 uur en 16.00 uur', 'tussen 8.00 uur en 16.00 uur')
if MUT == 'M_dcirkel': opg(V01, '014', '24 kinderen', '28 kinderen')
if MUT == 'M_das': opg(V01, '015', 'tussen 60 en 80', 'tussen 60 en 100')
if MUT == 'M_dstaaf': [s_.__setitem__('waarde', 5) for s_ in IT(V01, '016')['visual']['jsRender']['staven'] if s_['naam'] == 'woensdag']
if MUT == 'M_1022': opg(E05, ITC(CID_E05['004'])['nr'], '€80 en kost nu €120', '€50 en kost nu €75')   # V-#1022: antwoord 50 = de oude prijs (route 'getal uit de vraag')
if MUT == 'M_1024': FHV(ITC(CID_E05['004']), next(f_['fout'] for f_ in ITC(CID_E05['004'])['foutHints'] if f_['soort'] == 'nog geen procent van de oude prijs' and val(f_['fout']) != 40))['uitleg'] = 'Dat is nog geen procent van de oude prijs. De oude prijs is honderd procent: hoeveel procent komt erbij?'
if MUT == 'M_1031': FHV(IT(V01, '009'), '1,0')['soort'] = 'maar één getal'   # r1e V-#1031: live 1c-stand, de omgewisselde stip onder 'maar één getal'
if MUT == 'M_1023':   # r1e: een sleutel 'lijn van nul' ontbreekt (of, zonder die regel in de entry: de regel staat er wel, de sleutels niet)
    x_ = IT(V01, '001')
    if any(f_['soort'] == 'stip op de lijn van nul' and ',' in f_['fout'] for f_ in x_['foutHints']): x_['foutHints'] = [f_ for f_ in x_['foutHints'] if not (f_['soort'] == 'stip op de lijn van nul' and ',' in f_['fout'])]
    else: BT[(V01, 1)]['foutHints'].append({'soort': 'stip op de lijn van nul (mutant)', 'regel': 'fout = stip op de lijn van nul', 'tekst': 'x'})
if MUT == 'M_318':   # r1e les 318: 'getal uit de vraag' vooraan in de entry
    fl_ = BT[(V01, 1)]['foutHints']; fl_.sort(key=lambda f_: 0 if f_['regel'].startswith('fout = een getal uit de vraag') else 1)
if MUT == 'M_dec':   # r1e: de motor leest een stip-sleutel 'a,0' als het getal a (V-#1031 terug): 'maar één getal' op die sleutel
    for x_ in ITEMS:
        if x_['doelId'] == V01 and x_['merge']['somtypeNrOrigineel'] == 1 and (q_ := re.search(r'\((\d+), (\d+)\)', x_['opgave'])):
            for f_ in x_['foutHints']:
                if (k_ := re.fullmatch(r'\(?(\d+), ?0\)?', f_['fout'].strip())) and k_.group(1) in q_.groups(): f_['soort'] = 'maar één getal'
if MUT == 'M_1024k':   # r1e Oef-#1024: de kommasleutel '33,3' op 'andere fout' terwijl '33' een eigen regel heeft
    x_ = ITC(CID_E05['004']); x_['foutHints'] = [f_ for f_ in x_['foutHints'] if f_['fout'] != '33,3'] + [dict(x_['foutHints'][0], fout='33,3', soort='andere fout', regel='andere fout')]
if MUT == 'M_1062p': next(f_ for f_ in BT[(V01, 1)]['foutHints'] if f_['soort'] == 'stip op de lijn van nul')['tekst'] = 'Bij jouw stip staat een nul waar een ander getal hoort. Kijk naar de onderste rij. Ga dan omhoog zoveel als het tweede getal.'   # Z-#1062: de uitzondering op les 193 geldt alleen voor de tekst van Didactiek
if MUT == 'M_1025': [f_.__setitem__('soort', 'maar één getal' if f_['soort'] == 'stip op de lijn van nul' else 'stip op de lijn van nul' if f_['soort'] == 'maar één getal' else f_['soort']) for x_ in ITEMS if x_['doelId'] == V01 for f_ in x_['foutHints']]
if MUT == 'M_306': opg(E05, ITC(CID_E05['004'])['nr'], '€80 en kost nu €120', '€100 en kost nu €150')   # les 306: het verschil = het antwoord (50)
if MUT == 'M_d353': opg(E05, ITC(CID_E05['019'])['nr'], 'De prijs stijgt met 20%.', 'De prijs stijgt.')   # les 353: geen match = FAIL, geen crash
# ---- sleutel-/regelmutanten ----
if MUT == 'M_label': FHV(ITC(CID_E05['001']), '€8')['soort'] = 'tien keer te veel rente'
if MUT == 'M_label2': FHV(ITC(CID_E05['019']), '€24')['soort'] = 'procent als euro'
if MUT == 'M_label3': FHV(ITC(CID_E05['004']), '€40')['fout'] = '€41'
if MUT == 'M_label4': FHV(ITC(CID_E05['041']), '4')['soort'] = 'nieuwe aantal als basis'
if MUT == 'M_label5': FHV(IT(V01, '001'), '1,6')['fout'] = '1,5'
if MUT == 'M_lijn0': FHV(IT(V01, '001'), '6')['fout'] = '6,2'   # r1b: 'stip op de lijn van nul' met een komma
if MUT == 'M_label6': FHV(ITC(CID_E05['001']), '€392')['soort'] = 'alleen de rente'
if MUT == 'M_lijn2': FHV(IT(V01, '013'), 'De temperatuur daalt met 6 graden')['soort'] = 'omhoog in plaats van omlaag'
if MUT == 'M_staaf2': FHV(IT(V01, '016'), 'Maandag')['soort'] = 'de laagste staaf'
if MUT == 'M_lett': FH(IT(V01, '016'), 'de laagste staaf')['regel'] = 'dag'
if MUT == 'M_mist': x_ = IT(V01, '015'); x_['foutHints'] = [f for f in x_['foutHints'] if f['fout'] != '140']
if MUT == 'M_alg': FH(ITC(CID_E05['054']), 'verschil als procent')['soort'] = 'andere fout'
if MUT == 'M_antw': x_ = ITC(CID_E05['001']); x_['foutHints'].append(dict(x_['foutHints'][0], fout=x_['antwoord']))
if MUT == 'M_L2': ITC(CID_E05['019'])['foutHints'][0]['uitlegSterker'] = ''
if MUT == 'M_onb': ITC(CID_E05['041'])['foutHints'][0]['soort'] = 'iets nieuws'
if MUT == 'M_hussel': IT(V01, '013')['husselen'] = False
# ---- verklaptoets (meerkeuze) ----
if MUT == 'M_260': IT(V01, '014')['hint'] = 'Twaalf kinderen kiezen voetbal.'
if MUT == 'M_824': IT(V01, '013')['sterkereHint'] += ' De temperatuur daalt met drie graden.'
if MUT == 'M_264': ITC(CID_E05['054'])['hint'] = 'Het is ongeveer zo.' if 'ongeveer' in ITC(CID_E05['054'])['antwoord'].lower() else f"Het is {ITC(CID_E05['054'])['antwoord']}."   # r1c: na V-#1023 geen 'ongeveer' meer
if MUT == 'M_264h2': IT(V01, '015')['sterkereHint'] = 'Het antwoord is zeventig.'

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
for x in ITEMS:
  doel = x['doelId']; nro = x['merge']['somtypeNrOrigineel']; o = x['opgave'].replace('\n', ' '); nid = f"{doel[3:]} #{nro} {x['nr']}"
  try:
    ops = [p['tekst'] for p in x.get('opties') or []]; mk = x['type'] == 'meerkeuze'
    if not x.get('hint') or not x.get('sterkereHint'): fail(f'{nid}: H1/H2 leeg'); continue   # geen hints (kop gesplitst): verder niets te checken, geen crash-regel (mutrun)
    def eis(c, m):
        if not c: fail(f'{nid} data: {m} — klopt niet voor {o!r} => {x["antwoord"]}')
    for veld_, w_ in [('opgave', o), ('antwoord', x['antwoord'])] + [('optie', p) for p in ops]:
        if re.search(r'\b\d{1,2}:\d{2}\b', w_): fail(f"les 262 {nid} {veld_}: kloktijd met ':' ({w_!r}); G8: 15.00 uur")
    a = val(x['antwoord']); g = nums(o); ok = {}; routes = {}; okstr = False
    dk = {f_['fout']: f_['denkfout'] for f_ in x['extraVelden'].get('claudeDenkfouten') or []}
    for f_ in dk:
        if f_.startswith('€') and not x['antwoord'].strip().startswith('€'): EURO[(doel[3:], nro)] += 1
    if mk:
        if x['antwoord'] not in ops: fail(f'{nid}: antwoord niet in de opties'); continue
        if not x.get('husselen'): fail(f'{nid}: meerkeuze zonder husselen')
        pos[ops.index(x['antwoord'])] += 1
    elif ops: fail(f'{nid}: kaal item met opties')
    if doel == E05 and nro in (1, 18):
        m_ = re.fullmatch(r'Een (.+?) kostte €(\d+) en kost nu €(\d+)\. Met hoeveel procent is de prijs gestegen\?', o); eis(m_ is not None, "H1/H2: oude en nieuwe prijs in euro, 'gestegen'")
        if m_ is None: continue
        O_, N_ = Fr(int(m_.group(2))), Fr(int(m_.group(3))); d_ = N_ - O_
        eis(N_ > O_ and a == d_ * 100 / O_, "H2: 'nieuwe min oude prijs; de oude prijs is honderd procent' = het antwoord")
        eis(not x['antwoord'].strip().startswith('€'), 'antwoord is een procent (geen bedrag)')
        nb_ = d_ * 100 / N_
        def _nb(v, nb_=nb_, nr=x['nr']):
            if v == nb_: return True
            if v != nb_ and abs(v - nb_) < 1 and v.denominator == 1: AFGEROND.append(f"E05 #{nro} {nr}: {float(nb_):.2f} → {v}"); return True
            if v.denominator in (2, 5, 10) and v == Fr(round(nb_ * 10), 10): return True   # Z-#1021: de kommavorm op één decimaal ('33,3')
            return False
        ok = {'nog geen procent van de oude prijs': lambda v, d_=d_, f_=_nb: v == d_ or f_(v)}
        routes = {'verschil in euro': d_, 'nieuwe prijs als basis': nb_, 'oude prijs uit de vraag': O_, 'nieuwe prijs uit de vraag': N_}   # V-#1022 (les 392)
        for fh_ in x['foutHints']:   # V-#1024: 'nog geen procent' alleen als de sleutel het verschil in euro is; 'niet de nieuwe prijs' alleen bij de nieuwe prijs als basis
            v_ = val(fh_['fout'])
            if fh_['soort'] != 'nog geen procent van de oude prijs' or v_ is None: continue
            if re.search(r'nog geen procent', fh_['uitleg'] or '', re.I) and v_ != d_: fail(f"V-#1024 {nid} {fh_['fout']!r}: L1 «nog geen procent» klopt niet: de sleutel is geen verschil in euro ({fh_['uitleg'][:60]})")
            if re.search(r'niet de nieuwe prijs', fh_['uitleg'] or '', re.I) and v_ == d_: fail(f"V-#1024 {nid} {fh_['fout']!r}: L1 «niet de nieuwe prijs» klopt niet bij het verschil in euro")
    elif doel == E05 and nro == 3:
        m_ = re.fullmatch(r'Vorig jaar waren er (\d+) (.+?), nu (\d+)\. Met hoeveel procent is dat gestegen\?', o); eis(m_ is not None, "H1/H2: oud en nieuw aantal, 'gestegen'")
        if m_ is None: continue
        O_, N_ = Fr(int(m_.group(1))), Fr(int(m_.group(3))); d_ = N_ - O_
        eis(N_ > O_ and a == d_ * 100 / O_, "H2: 'nieuw min oud aantal; het oude aantal is honderd procent' = het antwoord")
        nb_ = d_ * 100 / N_
        def _nb(v, nb_=nb_, nr=x['nr']):
            if v == nb_: return True
            if abs(v - nb_) < 1 and v.denominator == 1: AFGEROND.append(f"E05 #3 {nr}: {float(nb_):.2f} → {v}"); return True
            if v.denominator in (2, 5, 10) and v == Fr(round(nb_ * 10), 10): return True   # Z-#1021
            return False
        ok = {'verschil': lambda v, d_=d_: v == d_, 'nieuwe aantal als basis': _nb}
        routes = {'verschil': d_, 'nieuwe aantal als basis': nb_, 'oud aantal uit de vraag': O_, 'nieuw aantal uit de vraag': N_}   # V-#1022
    elif doel == E05 and nro in RENTE:
        m_ = re.fullmatch(r'(.+?) zet €(\d+) op een spaarrekening met (\d+)% rente per jaar\. Hoeveel staat er na één jaar op de rekening\?', o)
        eis(m_ is not None, "H1/H2: bedrag op de rekening, procent rente, één jaar, totaal gevraagd")
        if m_ is None: continue
        B_, p_ = Fr(int(m_.group(2))), Fr(int(m_.group(3))); r_ = B_ * p_ / 100
        eis(a == B_ + r_, "H2: 'bedrag : honderd × procent = rente; rente erbij' = het antwoord")
        ok = {'alleen de rente': lambda v, r_=r_: v == r_, 'tien keer te veel rente': lambda v, B_=B_, r_=r_: v == B_ + 10 * r_, 'rente eraf': lambda v, B_=B_, r_=r_: v == B_ - r_}
        routes = {'alleen de rente': r_, 'tien keer te veel rente': B_ + 10 * r_, 'rente eraf': B_ - r_}
    elif doel == E05 and nro in PRIJS:
        m_ = re.fullmatch(r'Een (.+?) kostte €(\d+)\. De prijs stijgt met (\d+)%\. Wat kost (?:de|het) (.+?) nu\?', o)
        eis(m_ is not None, "H1/H2: oude prijs in euro, procent erbij")
        if m_ is None: continue
        O_, p_ = Fr(int(m_.group(2))), Fr(int(m_.group(3))); d_ = O_ * p_ / 100
        eis(a == O_ + d_, "H2: 'oude prijs : honderd × procent erbij' = het antwoord")
        if m_.group(4) not in m_.group(1) and m_.group(1) not in m_.group(4): ZELFST.append(f"{x['nr']} '{m_.group(1)}'→'{m_.group(4)}'")
        ok = {'alleen wat erbij komt': lambda v, d_=d_: v == d_, 'eraf': lambda v, O_=O_, d_=d_: v == O_ - d_, 'procent als euro': lambda v, O_=O_, p_=p_: v == O_ + p_}
        routes = {'alleen wat erbij komt': d_, 'eraf': O_ - d_, 'procent als euro': O_ + p_}
    elif doel == E05 and nro == 21:
        m_ = re.fullmatch(r'Een winkel verkoopt in (week \d+|de eerste week) (\w+) broden en in (week \d+|de tweede week) (\w+) broden\. Met hoeveel procent is de verkoop gedaald\?', o)
        gw_ = lambda g: int(g) if g.isdigit() else int(GETALWOORD[g]) if g in GETALWOORD else None   # V-#1023: cijfers (nieuw) of getalwoorden (oud)
        eis(m_ is not None and gw_(m_.group(2)) and gw_(m_.group(4)), "H1/H2: twee aantallen, 'gedaald'")
        if m_ is None or not gw_(m_.group(2)) or not gw_(m_.group(4)): continue
        O_, N_ = Fr(gw_(m_.group(2))), Fr(gw_(m_.group(4))); d_ = O_ - N_; ex_ = d_ * 100 / O_
        eis(O_ > N_ and abs(a - ex_) < Fr(1, 2) and (x['antwoord'].lower().startswith('ongeveer') == (ex_.denominator != 1)), "H2: 'oud min nieuw; het oude aantal is honderd procent' = het antwoord")
        ok = {'verschil als procent': lambda v, d_=d_: val(v) == d_, 'nieuwe aantal als basis': lambda v, d_=d_, N_=N_: abs(val(v) - d_ * 100 / N_) < 1}
        routes = {'verschil als procent': d_, 'nieuwe aantal als basis': d_ * 100 / N_, 'oud aantal uit de vraag': O_, 'nieuw aantal uit de vraag': N_}   # V-#1022
    elif doel == V01 and nro == 1:
        m_ = re.search(r'Zet de stip op \((\d+), (\d+)\)\.', o); eis(m_ is not None, "H1/H2: twee getallen tussen haakjes, met een komma")
        if m_ is None: continue
        X_, Y_ = m_.group(1), m_.group(2)
        an_ = re.sub(r'^\(\s*(\d+)\s*,\s*(\d+)\s*\)$', r'\1,\2', x['antwoord'].strip())   # V-#1025: '(x,0)'
        eis(an_ in (f'{X_},{Y_}', X_ if Y_ == '0' else None), "H2: 'vóór de komma opzij, na de komma omhoog' = het antwoord")
        if x['antwoord'].strip().startswith('('):   # V-#1025: '(1,0)' is op waarde gelijk aan '1': vergelijk als stip (tekst), niet als getal
            a = None
            for fh_ in x['foutHints']:
                if re.sub(r'^\(\s*(\d+)\s*,\s*(\d+)\s*\)$', r'\1,\2', fh_['fout'].strip()) == an_: fail(f"{nid}: fout-hint {fh_['fout']!r} = het antwoord (als stip)")
        if Y_ == '0' and x['antwoord'] == X_: NUL_WEG.append(f"{x['nr']} ({X_}, 0) → {x['antwoord']!r}")
        # r1e (V-#1031, les 396): in het rooster is 'a,b' een stip, geen kommagetal: de soorten worden op de sleuteltekst gecontroleerd (okstr),
        # niet op de waarde (val('1,0') = 1 liet 009 '1,0' onder 'maar één getal' door).
        okstr = True; NS_ = lambda k: re.sub(r'\s', '', re.sub(r'^\(\s*(.*?)\s*\)$', r'\1', k.strip()))
        ok = {'omgewisseld': lambda k, X_=X_, Y_=Y_: X_ != Y_ and NS_(k) == f'{Y_},{X_}',
              'stip op de lijn van nul': lambda k, X_=X_, Y_=Y_: (NS_(k) in {f'{X_},0', f'0,{Y_}'} - {f'{X_},{Y_}'}) if NIEUW1025 else (NS_(k).isdigit() and int(NS_(k)) in (int(X_), int(Y_))),   # r1e: Oef-#1023 'x,0'/'0,y'; r1b oude notatie: één getal
              'maar één getal': lambda k, X_=X_, Y_=Y_: NIEUW1025 and NS_(k).isdigit() and int(NS_(k)) in (int(X_), int(Y_))}   # r1c V-#1025: alleen een los getal (geen komma)
        st1_ = BT.get((V01, 1)) or {'foutHints': []}
        if any(f_['regel'].startswith('fout = stip op de lijn van nul') for f_ in st1_['foutHints']):   # r1e Oef-#1023: de motorregel staat in de entry → beide stippen zijn sleutel
            for k_ in [f'{X_},0', f'0,{Y_}']:
                if k_ != f'{X_},{Y_}' and not any(NS_(f_['fout']) == k_ and f_['soort'] == 'stip op de lijn van nul' for f_ in x['foutHints']):
                    fail(f"Oef-#1023 {nid}: sleutel {k_!r} staat niet onder 'stip op de lijn van nul'")
        routes = {'omgewisseld': val(f'{Y_},{X_}')} if X_ != Y_ else {}
        if X_ == Y_: I.append(f"INFO V01 #1 {x['nr']} ({X_}, {Y_}): omwisselen geeft dezelfde stip; geen sleutel (check_hints 'geen fout-hint', datapunt motor)")
    elif doel == V01 and nro == 2:
        m_ = re.search(r'van (\d+)\.00 uur tot (\d+)\.00 uur\. Wat gebeurt er met de temperatuur tussen (\d+)\.00 uur en (\d+)\.00 uur\?', o)
        pt_ = dict((int(h), int(t)) for h, t in re.findall(r'\((\d+)\.00 uur, (-?\d+) °C\)', (x.get('visual') or {}).get('toelichting') or ''))
        eis(m_ is not None and len(pt_) >= 3, 'H1/H2: twee tijden uit de vraag, punten van de lijn (visual)')
        if m_ is None or len(pt_) < 3: continue
        t1, t2 = int(m_.group(3)), int(m_.group(4)); eis(t1 in pt_ and t2 in pt_, 'de tijden uit de vraag staan op de lijn')
        if t1 not in pt_ or t2 not in pt_: continue
        dv_ = pt_[t2] - pt_[t1]; zin_ = lambda d: f"De temperatuur {'stijgt' if d > 0 else 'daalt'} met {abs(d)} graden"
        eis(dv_ != 0 and x['antwoord'] == zin_(dv_), "H2: 'lees af bij de twee tijden; omhoog of omlaag' = het antwoord")
        hs_ = sorted(pt_); ander_ = {abs(pt_[b] - pt_[a_]) for a_, b in zip(hs_, hs_[1:]) if (a_, b) != (t1, t2)} | {abs(pt_[hs_[-1]] - pt_[hs_[0]])} - {abs(dv_)}
        ok = {'omhoog in plaats van omlaag': lambda v, dv_=dv_: v == zin_(-dv_),
              'verschil van een ander stuk': lambda v, ander_=ander_: (mm_ := re.fullmatch(r'De temperatuur (?:stijgt|daalt) met (\d+) graden', v)) is not None and int(mm_.group(1)) in ander_}
        routes = {}
    elif doel == V01 and nro == 3:
        m_ = re.search(r'De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis\. Er zitten (\d+) kinderen in de klas\. Hoeveel kinderen kiezen voetbal\?', o)
        eis(m_ is not None, "H1/H2: voetbal is de helft, aantal in de klas")
        if m_ is None: continue
        N_ = Fr(int(m_.group(1))); eis(a == N_ / 2, "H2: 'de helft van het aantal in de klas' = het antwoord")
        ok = {'een kwart': lambda v, N_=N_: val(v) == N_ / 4, 'drie gelijke stukken': lambda v, N_=N_: val(v) == N_ / 3}
        routes = {'een kwart': N_ / 4, 'drie gelijke stukken': N_ / 3}
        cu_ = x['extraVelden'].get('claudeUitleg') or ''
        if re.search(r'\b(blauw|rood|groen|geel)', cu_): I.append(f"INFO V01 #3 {x['nr']}: claudeUitleg noemt een kleur ({cu_!r}), de visual heeft namen van sporten (datapunt Oef-#1020, les 369)")
    elif doel == V01 and nro == 4:
        m_ = re.search(r'loopt de as met stappen van (\d+)\. De staaf van groep \d+ staat precies tussen (\d+) en (\d+)\.', o)
        eis(m_ is not None, "H1/H2: precies tussen twee getallen op de as")
        if m_ is None: continue
        st_, lo_, hi_ = (Fr(int(g_)) for g_ in m_.groups()); eis(hi_ - lo_ == st_ and a == (lo_ + hi_) / 2, "H2: 'kleinste tot grootste, de helft erbij' = het antwoord")
        ok = {'niet in het midden': lambda v, lo_=lo_, hi_=hi_, a=a: lo_ < val(v) < hi_ and val(v) != a, 'opgeteld': lambda v, lo_=lo_, hi_=hi_: val(v) == lo_ + hi_}
        routes = {'opgeteld': lo_ + hi_}
    elif doel == V01 and nro == 5:
        jr_ = (x.get('visual') or {}).get('jsRender') or {}; sv_ = {s_['naam'].lower(): s_['waarde'] for s_ in jr_.get('staven') or []}
        eis(len(sv_) >= 3 and all(d_ in o for d_ in sv_), 'H1/H2: staven met de dagen uit de vraag (jsRender)')
        if len(sv_) < 3: continue
        hoog_ = max(sv_.values()); laag_ = min(sv_.values())
        eis([d_ for d_, w_ in sv_.items() if w_ == hoog_] == [x['antwoord'].lower()], "H1/H2: 'de hoogste staaf' = het antwoord (één hoogste)")
        ok = {'niet de hoogste staaf': lambda v, sv_=sv_: sv_.get(v.lower(), hoog_) < hoog_ and sv_.get(v.lower()) != laag_, 'de laagste staaf': lambda v, sv_=sv_: sv_.get(v.lower()) == laag_}
        routes = {}
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
            f_ = ok.get(s)
            if f_ is None: fail(f"{nid} {fh['fout']!r}: soort {s!r} heeft geen check"); continue
            if not f_(fh['fout']): fail(f"{nid} {fh['fout']!r}: soort {s!r} klopt niet bij deze optie (antwoord {x['antwoord']!r})")
            continue
        v = val(fh['fout'], noteer=(doel, nro, x['nr'], fh['fout'], s))
        if v is None and not okstr: fail(f"{nid} sleutel {fh['fout']!r}: niet te lezen"); continue   # r1e: stip-sleutels ('(6, 0)', Z-#1032) worden als tekst gecontroleerd
        if v is not None and v == a: fail(f"{nid}: sleutel {fh['fout']!r} = het antwoord (op waarde)"); continue
        if s == 'andere fout':
            r_ = next((r for r, w in routes.items() if w == v), 'overig'); andere[(doel[3:], nro, r_)] += 1; continue
        f_ = ok.get(s)
        if f_ is None: fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} heeft geen check"); continue
        if not (f_(fh['fout']) if okstr else f_(v)): fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} klopt niet (antwoord {x['antwoord']})")
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
    # r1e Oef-#1024 (Z-#1021, les 397): een kommasleutel ('33,3') hoort bij dezelfde regel als zijn afgeronde vorm ('33'), niet op 'andere fout'
    if doel == E05 and nro in (1, 3, 18):
        fh_soort_ = {fh_['fout'].lstrip('€'): fh_['soort'] for fh_ in x['foutHints']}
        cfh_ = {k_['fout'].lstrip('€') for k_ in x['extraVelden'].get('claudeFoutHints') or []}
        for d_ in x['extraVelden'].get('claudeDenkfouten') or []:
            k_ = str(d_.get('fout') or '').lstrip('€')
            if not re.fullmatch(r'\d+,\d+', k_): continue
            r_ = str(int(Fr(k_.replace(',', '.')) + Fr(1, 2))); sr_ = fh_soort_.get(r_)
            if sr_ in (None, 'andere fout'): continue
            if k_ in fh_soort_:
                if fh_soort_[k_] != sr_: fail(f"Oef-#1024 {nid} sleutel {k_!r}: soort {fh_soort_[k_]!r}, de afgeronde vorm {r_!r} heeft {sr_!r}")
            elif k_ in cfh_: fail(f"Oef-#1024 {nid} sleutel {k_!r}: staat in claudeFoutHints maar niet in de fout-hints (les 397)")
            else: K1024.append(f"{x['nr']} {k_}")
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
I.append(f"INFO E05 prijs: zelfstandig naamwoord in de vraag ≠ dat van de opgave (datapunt Oef-#1014): {len(ZELFST)} {ZELFST}")
I.append(f"INFO V01 #1: antwoord zonder ',0' bij (x, 0) (datapunt Oef-#1019): {NUL_WEG}")
if K1024: W.append(f"Oef-#1024 (data Overzicht): {len(K1024)} kommasleutels staan alleen in claudeDenkfouten, niet in claudeFoutHints, dus geen sleutel (les 397): {K1024}")
# ---- r1e les 318 / V-#1031: volgorde V01 #1 (meest precieze ware tekst eerst) ----
if (V01, 1) in BT:
    rg_ = [f_['regel'] for f_ in BT[(V01, 1)]['foutHints']]
    i_ = lambda pre: next((j for j, r in enumerate(rg_) if r.startswith(pre)), None)
    ig_, il_, io_ = i_('fout = een getal uit de vraag'), i_('fout = stip op de lijn van nul'), i_('Claudes sleutel')
    cl_los_ = any(',' not in str(k_.get('fout', '')) for x in ITEMS if x['doelId'] == V01 and x['merge']['somtypeNrOrigineel'] == 1 for k_ in x['extraVelden'].get('claudeFoutHints') or [])
    if il_ is not None and ig_ is not None and il_ > ig_: fail("les 318 V01 #1: 'stip op de lijn van nul' staat na 'een getal uit de vraag' (die pakt 'x,0' als getal, V-#1031)")
    if io_ is not None and ig_ is not None and io_ > ig_ and not cl_los_ and NIEUW1025: fail("les 318 V01 #1: 'omgewisseld' staat na 'een getal uit de vraag' (die pakt 'y,0' als getal, V-#1031)")
# ---- teksten ----
TOEGESTAAN = {}
EENHEID = {'procent', 'euro', 'graden'}
COORD = {k_ for k_ in {EK(x) for x in ITEMS} if all(re.fullmatch(r'\(\d+, ?\d+\)', x['antwoord'].strip()) for x in ITEMS if EK(x) == k_)}   # Oef-#1036: entries met alleen stippen als antwoord
TXT = []
for s in B['somtypen']:
    k_ = (s['doel'], s['nrOrigineel'])
    TXT += [(k_, 'H1', s['hint1']), (k_, 'H2', s['hint2']), (k_, 'OZ', s['ouderzin'])]
    for f in s['foutHints']:
        for i_, t_ in enumerate(f['tekst'].split(' / ')): TXT.append((k_, f"L1 {f['soort']}" + (f' ({i_})' if ' / ' in f['tekst'] else ''), t_))
        TXT.append((k_, f"L2 {f['soort']}", f.get('tekstSterker') or ''))
        if not f.get('tekstSterker'): fail(f"{k_} {f['soort']}: geen tekstSterker")
    if s['foutHints'][-1]['soort'] != 'andere fout': fail(f"{k_}: 'andere fout' niet als laatste")
MUTS = {'M_cijfer': ((E05, 2), 'Deel door 100.'), 'M_letter': ((V01, 2), 'Kies optie B.'), 'M_plek': ((V01, 1), 'Kijk naar de eerste rij.'), 'M_1036c': ((V01, 2), 'Kijk naar het eerste getal.'), 'M_zoveel': ((E05, 5), 'Zoveel komt erbij.'),
        'M_217': ((E05, 5), 'Hier mag je niet optellen.'), 'M_231': ((V01, 4), 'Doe het zoals bij de vorige som.'),
        'M_ctx': ((E05, 4) if (E05, 4) in BT else (E05, 2), 'Hoeveel heeft Daan?'), 'M_ctx2': ((E05, 5), 'Wat kost de knuffel?'), 'M_ctx3': ((E05, 3), 'Tel de wortels.'), 'M_ctx4': ((E05, 3), f"Denk aan de {sorted(KOP_DING.get((E05, 3)) or ['wortels'])[0]}."),
        'M_ctx5': ((V01, 5), 'Kijk bij maandag.'), 'M_ctx6': ((E05, 19), 'Hoeveel kost een zak?') if (E05, 19) in BT else ((E05, 5), f"Hoeveel kost een {sorted(KOP_DING.get((E05, 5)) or ['jas'])[0]}?"),
        'M_moeilijk': ((E05, 2), 'Vermenigvuldig het getal.'), 'M_Bijna': ((V01, 4), 'Bijna goed!'), 'M_woorden': ((E05, 1), 'Haal de prijzen van elkaar af en reken verder. ' * 8),
        'M_235': ((V01, 5), 'Zoek de staaf. Zoek de staaf.'), 'M_klokw': ((V01, 2), 'Om twaalf uur is het warm.'), 'M_deel': ((E05, 2), 'Reken 800 : 100 uit.'), 'M_192': ((V01, 3), 'De stukken zijn even veel.'),
        'M_ongev': ((E05, 21), 'Het verschil is ongeveer een derde.')}
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
    if re.search(r'\b(eerste|tweede|derde|laatste|vooraan|achteraan|bovenste|onderste)\b(?! cijfer\b)', t, re.I) and not (k_ in COORD and not re.search(r'\b(eerste|tweede|derde|laatste|vooraan|achteraan|bovenste|onderste)\b(?! cijfer\b)', re.sub(r'\b(eerste|tweede) getal\b', '', t), re.I)): fail(f'les 193 {tag}: plekwoord: {t}')   # Oef-#1036/Z-#1062 (Didactiek 20:28): 'eerste/tweede getal' mag alleen in een coördinaat-entry (vaste volgorde in de stip); elk ander plekwoord blijft FAIL
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
    if re.search(r'\bongeveer\b', t, re.I) and lab != 'OZ': fail(f"les 372 {tag}: 'ongeveer' (vormcue: alleen de goede optie van E05 #21 heeft het): {t}")
    nw_ = len(t.split()); max_ = 55 if lab.startswith(('H2', 'L2')) else 45 if lab.startswith(('H1', 'L1')) else None
    if max_ and nw_ > max_: fail(f'V-#764 {tag}: {nw_} woorden (maximaal {max_}): {t[:80]}')
    zz_ = [z.strip() for z in re.split(r'(?<=[.?!])\s+', t) if z.strip()]
    if len(zz_) != len(set(zz_)): fail(f'les 235 {tag}: dezelfde zin twee keer: {t[:80]}')
    lang = [z for z in zz_ if len(z.split()) > 25]
    if lang: W.append(f'{tag}: lange zin ({len(lang[0].split())} woorden): {lang[0]}')
I.append('INFO contextwoorden: ' + '; '.join(f'{k[0][3:]} nrO{k[1]} {sorted(v)}' for k, v in sorted(KOP_DING.items()) if v))
# ---- Z-#1062 (ronde 1f, Didactiek A met aanpassing): 'lijn van nul' zonder 'vóór/na de komma'; per sleutel: een 0 waar het antwoord geen 0 heeft ----
T1062 = 'Bij jouw stip staat een nul waar een ander getal hoort. Ga eerst opzij zoveel als het eerste getal. Ga dan omhoog zoveel als het tweede getal.'
_ns1062 = lambda k: re.sub(r'\s', '', re.sub(r'^\(\s*(.*?)\s*\)$', r'\1', str(k).strip()))
X1 = [x for x in ITEMS if x['doelId'] == V01 and EK(x) == (V01, 1)]
if MUT == 'M_1062n': x_ = IT(V01, '008'); x_['foutHints'].append(dict(FHV(x_, '0,0'), fout='3,0'))      # antwoord (6, 0): de 0 staat op dezelfde plek als in het antwoord
if MUT == 'M_1062t': next(f_ for f_ in BT[(V01, 1)]['foutHints'] if f_['soort'] == 'stip op de lijn van nul')['tekst'] = 'Die stip ligt op de lijn van nul. Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.'
if MUT == 'M_1062s': x_ = IT(V01, '001'); x_['foutHints'] = [f_ for f_ in x_['foutHints'] if _ns1062(f_['fout']) != '6,0']
def _nul1062(k, a):
    mk_, ma_ = re.fullmatch(r'\(?\s*(\d+)\s*,\s*(\d+)\s*\)?', str(k).strip()), re.fullmatch(r'\((\d+), ?(\d+)\)', a.strip())
    return bool(mk_ and ma_) and any(int(mk_.group(i_)) == 0 and int(ma_.group(i_)) != 0 for i_ in (1, 2))
_e1062 = [f_ for f_ in (BT.get((V01, 1)) or {}).get('foutHints', []) if f_['soort'] == 'stip op de lijn van nul' and f_['regel'].startswith('fout = stip op de lijn van nul')]
if _e1062 and _e1062[0]['tekst'] != T1062: fail(f"Z-#1062 V01 #1 entry 'stip op de lijn van nul': niet de tekst van Didactiek (vóór/na de komma?): {_e1062[0]['tekst'][:70]}")
Z1062 = {}
for x in X1:
    for f_ in x['foutHints']:
        if f_.get('uitleg') == T1062 or f_['soort'] == 'stip op de lijn van nul' and _e1062:
            ok_ = _nul1062(f_['fout'], x['antwoord']); Z1062[f"{x['nr']} {_ns1062(f_['fout'])}"] = [x['antwoord'], ok_]
            if not ok_: fail(f"Z-#1062 VBN-V01 #1 {x['nr']} sleutel {f_['fout']!r}: tekst 'een nul waar een ander getal hoort', maar het antwoord {x['antwoord']} heeft daar ook een 0 (of geen stip)")
SNAP1062 = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/z1062_snapshot.json'
if _e1062 and os.environ.get('SNAP') == '1': json.dump(Z1062, open(SNAP1062, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO Z-#1062: snapshot per sleutel geschreven ({len(Z1062)})')
elif _e1062 and os.path.exists(SNAP1062):
    oud_ = json.load(open(SNAP1062))
    for k_ in sorted(set(oud_) | set(Z1062)):
        if oud_.get(k_) != Z1062.get(k_): fail(f"Z-#1062 snapshot V01 #1 {k_}: {oud_.get(k_)} → {Z1062.get(k_)} (voorwaarde per sleutel nalopen, dan SNAP=1)")
I.append(f"INFO Z-#1062: {len(Z1062)} sleutels 'lijn van nul', voorwaarde waar: {sum(v_[1] for v_ in Z1062.values())}" + ('' if _e1062 else ' (entry zonder motorregel: uit)'))
# ---- Oef-#1036 (ronde 1g): geen 'vóór/na de komma' in V01 #1; verklaptoets (les 300): geen hintlaag geeft de stip; SNAP van de teksten ----
WOORD1036 = {0: 'nul', 1: 'één', 2: 'twee', 3: 'drie', 4: 'vier', 5: 'vijf', 6: 'zes', 7: 'zeven', 8: 'acht', 9: 'negen', 10: 'tien'}
S1036 = BT.get((V01, 1))
if MUT == 'M_1036k': S1036['foutHints'][-1]['tekstSterker'] = 'Begin bij nul. Het getal vóór de komma zegt hoeveel stappen je opzij gaat.'
if MUT == 'M_1036v': x_ = IT(V01, '001'); x_['sterkereHint'] = (x_.get('sterkereHint') or '') + ' De stip staat bij zes, één.'
if MUT == 'M_1036s': S1036['hint1'] = S1036['hint1'] + ' Kijk goed.'
if MUT == 'M_1036o': next(f_ for f_ in S1036['foutHints'] if f_['soort'] == 'omgewisseld')['tekst'] = 'Daar staan de twee getallen omgewisseld. Het eerste getal gaat opzij, het tweede getal omhoog.'
if S1036:
    T36 = [('H1', S1036['hint1']), ('H2', S1036['hint2'])] + [(f"L{j_} {f_['soort']}", f_.get(k_) or '') for f_ in S1036['foutHints'] for j_, k_ in ((1, 'tekst'), (2, 'tekstSterker'))]
    for x in [x for x in ITEMS if EK(x) == (V01, 1)]:
        T36 += [(f"{x['nr']} hint", x.get('hint') or ''), (f"{x['nr']} sterkereHint", x.get('sterkereHint') or '')] + [(f"{x['nr']} {f_['fout']} {k_}", f_.get(k_) or '') for f_ in x['foutHints'] for k_ in ('uitleg', 'uitlegSterker')]
        m_ = re.fullmatch(r'\((\d+), ?(\d+)\)', x['antwoord'].strip())
        if m_:
            a_, b_ = int(m_.group(1)), int(m_.group(2)); wa_, wb_ = WOORD1036.get(a_, str(a_)), WOORD1036.get(b_, str(b_))
            for lab_, t_ in [(l, t) for l, t in T36 if l.startswith(x['nr']) or not l[0].isdigit()]:
                if re.search(rf'\(?\s*\b{a_}\s*,\s*{b_}\b|\(?\s*\b{wa_}\b\s*(,|en)\s*\b{wb_}\b', t_, re.I):
                    fail(f"les 300 Oef-#1036 VBN-V01 #1 {x['nr']} [{lab_[:40]}]: hint geeft de stip {x['antwoord']}: {t_[:80]}")
    for lab_, t_ in T36:
        if re.search(r'(vóór|voor|na) de komma', t_, re.I): fail(f"Oef-#1036 VBN-V01 #1 [{lab_[:40]}]: 'vóór/na de komma' (leest als kommagetal): {t_[:80]}")
    Z36 = {l: t for l, t in T36 if not l[0].isdigit()}
    for f_ in S1036['foutHints']:   # Oef-#1036 stem (Didactiek 20:34, ronde 1h): 'omgewisseld' spreekt het kind aan op zijn eigen stip
        if f_['soort'] == 'omgewisseld' and not (f_.get('tekst') or '').startswith('Bij jouw stip zijn de twee getallen omgewisseld.'): fail(f"Oef-#1036 VBN-V01 #1 'omgewisseld': niet «Bij jouw stip zijn de twee getallen omgewisseld.»: {(f_.get('tekst') or '')[:80]}")
    SNAP1036 = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/z1036_snapshot.json'
    if os.environ.get('SNAP') == '1': json.dump(Z36, open(SNAP1036, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO Oef-#1036: tekstsnapshot V01 #1 geschreven ({len(Z36)})')
    elif os.path.exists(SNAP1036):
        oud_ = json.load(open(SNAP1036))
        for k_ in sorted(set(oud_) | set(Z36)):
            if oud_.get(k_) != Z36.get(k_): fail(f"Oef-#1036 snapshot V01 #1 [{k_[:40]}]: tekst veranderd (verklaptoets les 300 nalopen, dan SNAP=1)")
    I.append(f"INFO Oef-#1036: V01 #1 {len(T36)} hintteksten nagekeken (komma, les 300)")
SNAP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/opties_snapshot.json'
OPTS = {f"{x['doelId']} {x['nr']}": sorted(o_['tekst'] for o_ in (x.get('opties') or [])) for x in ITEMS if x.get('opties')}
if MUT == 'M_afl': k0_ = sorted(OPTS)[0]; OPTS[k0_] = OPTS[k0_][:-1] + ['iets anders']
_EPK = collections.Counter((s_['doel'], s_.get('somtype')) for s_ in B['somtypen'])   # r1d (Oef-#1014, sync #30): elke kop van een item heeft precies één entry
for k_ in sorted({(x['doelId'], x['merge']['somtype']) for x in ITEMS}):
    if _EPK[k_] != 1: fail(f"Oef-#1014 {k_[0][3:]} kop '{k_[1][:70]}': {_EPK[k_]} hint-entries (verwacht 1; sync_hint_keys voegt niet stil samen, apply_hints stopt)")
if ZONDER_ENTRY: fail(f'b9-doelen: {len(ZONDER_ENTRY)} items zonder hint-entry (kop gesplitst? datapunt Overzicht): {ZONDER_ENTRY}')
if os.environ.get('SNAP') == '1': json.dump(OPTS, open(SNAP, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO les 234: snapshot geschreven ({len(OPTS)} items)')
elif os.path.exists(SNAP):
    oud_ = json.load(open(SNAP))
    for k_ in sorted(set(oud_) | set(OPTS)):
        if oud_.get(k_) != OPTS.get(k_): fail(f'les 234 item {k_}: opties veranderd: routes, letterlijke regels en verklaptoets (les 300) nalopen, dan SNAP=1')
else: W.append('les 234: geen snapshot (SNAP=1 python3 check.py)')
for m in I: print(m)
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))); from l271 import les271
for m_ in les271(G8, 9, B): fail(m_)
for m in W: print('WARN', m)
for m in F: print('FAIL', m)
print(f'G8 b9: {len(ITEMS)} items · {sum(len(x["foutHints"]) for x in ITEMS)} sleutels · FAIL {len(F)} · WARN {len(W)} · INFO {len(I)}')
sys.exit(1 if F else 0)
