#!/usr/bin/env python3
"""G8 batch 6 (MEET-E07 #1–#4, MEET-V01 #1–#3, VBN-E01 #1–#2, VBN-E03 #1–#5, VBN-E04 #1–#5 en #32–#37: 25 somtypes, 193 items) nagespeeld op de
toegepaste per_doel-data (zandbak of live).
Kaal (MEET-E07, MEET-V01 #1, VBN-E03): per item de feiten waar H1/H2/L1 op leunen (DATA) en per sleutel een predicaat per soort (les 40/146/191);
'andere fout' per route geteld; Claude-sleutels met een punt als komma ('147.5', datapunt Oef-#498).
Meerkeuze (MEET-V01 #2/#3, VBN-E01, VBN-E04): het antwoord staat in de opties; elke foute optie heeft precies één fout-hint; een letterlijke regel pakt
alleen die optie (G8-2, les 160/161); de soort klopt op de waarde of de bewering van het item (VBN-E04: uit jsRender.staven); MEET-V01 #2: per sleutel
de route op de maten (diep × hoog × breed) en de gekozen tekst moet bij die route horen. Verklaptoets H1/H2: les 260 (o), Z-#824/les 288, les 264.
Les 306: geen foute route op het antwoord. Teksten: als b5 (cijfers, optieletters, ':' bij een getal, plekwoorden les 193, les 217, 'zoveel',
les 231, contextwoorden les 147 op alle [..]-plekken en gedeelde kopwoorden, moeilijke woorden, 'Bijna', V-#764, les 235, les 262) + les 271.
Les 234: snapshot van de opties (SNAP=1 schrijft hem).
Gebruik: python3 check.py [pad naar g8]   MUT=<naam> voor een mutant (moet FAIL geven)."""
import json, re, sys, os, collections
from fractions import Fraction as Fr
G8 = sys.argv[1] if len(sys.argv) > 1 else __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..')
MUT = os.environ.get('MUT')
sys.path.insert(0, f'{G8}/scripts'); import fout_regels as FR
CH = open(f'{G8}/check_hints.py', encoding='utf-8').read()
MOEILIJK = re.compile(re.search(r"MOEILIJK=re\.compile\(r'(.*?)',re\.I\)", CH).group(1), re.I)
F, W, I = [], [], []
def fail(m): F.append(m)
E7, V1, E01, E03, E04 = "G8-MEET-E07", "G8-MEET-V01", "G8-VBN-E01", "G8-VBN-E03", "G8-VBN-E04"
SEL = {E7: {1, 2, 3, 4}, V1: {1, 2, 3}, E01: {1, 2}, E03: {1, 2, 3, 4, 5}, E04: {1, 2, 3, 4, 5, 32, 33, 34, 35, 36, 37}}
B = json.load(open(f'{G8}/hints/batch6.json'))
BT = {(s['doel'], s['nrOrigineel']): s for s in B['somtypen']}
PUNT = []
def val(k, noteer=None):
    k = str(k).strip().replace('−', '-')
    k = re.sub(r'^(ongeveer|€)\s*', '', k, flags=re.I); k = re.sub(r'\s*(m|cm|bekers|appels|km)$', '', k)
    if re.fullmatch(r'-?\d+,\d+', k): return Fr(k.replace(',', '.'))
    if re.fullmatch(r'-?(\d{1,3}(?:\.\d{3})+|\d+)', k): return Fr(int(k.replace('.', '')))
    if re.fullmatch(r'\d+\.\d{1,2}', k):          # punt als komma (Claude-sleutel '147.5'): datapunt Oef-#498
        if noteer is not None: PUNT.append(noteer)
        return Fr(k)
    return None
def nums(t): return [Fr(x.replace(',', '.')) for x in re.findall(r'(?<![\d,])\d+(?:,\d+)?(?![\d,])', t)]
def past(regel, optie):
    """dezelfde voorwaarde als fout_regels (letterlijke optie): substring na norm421 én lett_past"""
    r = FR.norm421(regel.strip()).lower()
    return r in FR.norm421(optie, geld=r.startswith('€')).lower() and FR.lett_past(r, optie)
ITEMS = []
for doel_, nrs_ in SEL.items():
    d = json.load(open(f'{G8}/data/per_doel/{doel_}.json'))
    ITEMS += [x for x in d['items'] if x['merge']['somtypeNrOrigineel'] in nrs_]
def IT(doel, nr): return next(x for x in ITEMS if x['doelId'] == doel and x['nr'] == nr)
def FH(x, soort): return next(f for f in x['foutHints'] if f['soort'] == soort)
def opg(doel, nr, oud, nieuw): x_ = IT(doel, nr); assert oud in x_['opgave'], (nr, oud); x_['opgave'] = x_['opgave'].replace(oud, nieuw)
def staaf(nr, naam, w): next(s_ for s_ in IT(E04, nr)['visual']['jsRender']['staven'] if s_['naam'] == naam)['waarde'] = w
BWT = [f_ for s_ in B['somtypen'] if (s_['doel'], s_['nrOrigineel']) == (V1, 2) for f_ in s_['foutHints'] if f_['regel'].startswith('Claudes sleutels (alle)')][0]['tekst'].split(' / ')
# ---- data-mutanten (moeten FAIL geven) ----
if MUT == 'M_dsn': IT(E7, '001')['antwoord'] = '50'
if MUT == 'M_dhalf': opg(E7, '001', 'in 2,5 uur', 'in 3 uur'); IT(E7, '001')['antwoord'] = '50'
if MUT == 'M_dafst': IT(E7, '007')['antwoord'] = '160'
if MUT == 'M_dha': opg(V1, '001', '2 hectare', '2 are')
if MUT == 'M_dbw': IT(V1, '005')['visual']['jsRender']['hoog'] += 1
if MUT == 'M_dbw1': x_ = IT(V1, '005'); j_ = x_['visual']['jsRender']; j_['hoog'] = 1; x_['antwoord'] = str(j_['diep'] * j_['breed'])
if MUT == 'M_dbek': opg(V1, '004', '250 milliliter', '300 milliliter')
if MUT == 'M_dtab': opg(E01, '001', 'jaar 3 geeft 60', 'jaar 3 geeft 65')
if MUT == 'M_dspr': opg(E01, '002', '2 m · 2,3', '2,05 m · 2,3')
if MUT == 'M_dst1': opg(E03, '001', 'week 2 → €108', 'week 2 → €110')
if MUT == 'M_dst0': opg(E03, '001', 'week 0 → €58, week 1 → €83, week 2 → €108', 'week 1 → €58, week 2 → €83, week 3 → €108')
if MUT == 'M_dsv': IT(E03, '009')['antwoord'] = '128'
if MUT == 'M_dpa': IT(E04, '032')['antwoord'] = 'Nee, dat klopt niet.'
if MUT == 'M_dhe': staaf('025', 'fiets', 45); staaf('025', 'lopend', 30)
if MUT == 'M_dkz': staaf('036', 'taal', 8); staaf('036', 'rekenen', 32)
if MUT == 'M_dsa': staaf('040', 'water', 15); staaf('040', 'niets', 50)
if MUT == 'M_d100': staaf('030', 'vis', 45)
if MUT == 'M_dstreep': opg(E04, '030', 'Elk streepje is 10.', 'Elk streepje is 5.')
if MUT == 'M_dhd': opg(E04, '041', 'telt 25 kinderen', 'telt 35 kinderen')
if MUT == 'M_dmf': opg(E04, '043', '15 cm en 60 cm', '15 cm en 17 cm')
# ---- sleutel-/regelmutanten ----
# ronde 1b (Didactiek review-batch6): datamutanten die op de huidige data een NIEUWE FAIL geven (een item dat nu goed is)
def _ok_bw(x_):
    j_ = x_['visual']['jsRender']; d_, h_, b_ = j_['diep'], j_['hoog'], j_['breed']; return d_ * b_ + b_ * h_ + d_ * h_ != d_ * h_ * b_
if MUT == 'M_891':    # V-#891: een V01 #2-item krijgt de maten van het oude 007 (2×6×3 = 36, drie kanten = 36)
    x_ = next(x for x in ITEMS if x['doelId'] == V1 and x['merge']['somtypeNrOrigineel'] == 2 and _ok_bw(x) and x['antwoord'] == '36')
    x_['visual']['jsRender'].update(diep=2, hoog=6, breed=3)
if MUT == 'M_891t':   # V-#891/Z-#890: een sleutel met één eigen routetekst krijgt de algemene tekst
    f_ = next(f for x in ITEMS if x['doelId'] == V1 for f in x['foutHints'] if f['uitleg'] == BWT[0]); f_['uitleg'] = BWT[5]   # V-#1032: 005 heeft geen 'som' meer
def _beslis(x_):
    o_ = x_['opgave']; sv_ = {s_['naam']: s_['waarde'] for s_ in x_['visual']['jsRender']['staven']}
    m_ = re.search(r'"Meer dan de helft van [\w ]+ kiest (\w+)\."', o_); return (m_.group(1), sv_) if m_ else (None, sv_)
if MUT == 'M_893':    # V-#893: een beslissende staaf op 55 (som blijft 100, antwoord blijft Ja)
    x_ = next(x for x in ITEMS if x['doelId'] == E04 and x['merge']['somtypeNrOrigineel'] in (2, 4, 33) and _beslis(x)[0] and not 40 < _beslis(x)[1][_beslis(x)[0]] < 60)
    nm_, sv_ = _beslis(x_); w_ = 55 if sv_[nm_] >= 60 else 45; ander_ = next(k for k in sv_ if k != nm_ and sv_[k] + sv_[nm_] - w_ >= 0)
    staaf(x_['nr'], ander_, sv_[ander_] + sv_[nm_] - w_); staaf(x_['nr'], nm_, w_)
if MUT == 'M_894':    # V-#894: het genoemde aantal past bij geen heel totaal (zoals 027: 12 bij 45 %)
    for x_ in ITEMS:
        if x_['doelId'] != E04 or x_['merge']['somtypeNrOrigineel'] not in (1, 3, 5): continue
        m_ = re.search(r'"(\d+) kinderen kozen (\w+)\."', x_['opgave']); p_ = {s_['naam']: s_['waarde'] for s_ in x_['visual']['jsRender']['staven']}.get(m_.group(2))
        if (int(m_.group(1)) * 100) % p_ == 0:
            n_ = next(n for n in range(int(m_.group(1)) + 1, 200) if (n * 100) % p_); x_['opgave'] = x_['opgave'].replace(f'"{m_.group(1)} kinderen', f'"{n_} kinderen'); break
if MUT == 'M_z891':   # Z-#891: één item meer met het antwoord als grootste optie
    x_ = next(x for x in ITEMS if x['doelId'] == V1 and x['merge']['somtypeNrOrigineel'] == 2 and val(x['antwoord']) < max(val(p['tekst']) for p in x['opties']))
    for p in x_['opties']:
        if val(p['tekst']) > val(x_['antwoord']): p['tekst'] = str(int(val(x_['antwoord'])) - 1)
if MUT == 'M_920': IT(E04, '041')['sterkereHint'] = 'In een staaf tel je de kinderen die dat dier hebben. Wat moet er gebeuren om samen meer te tellen dan er kinderen in de klas zitten? Kies de uitleg die dat kan verklaren zonder dat er iets fout is.'   # Z-#920: de oude H2 (ronde 1b) is zonder uitzondering FAIL
if MUT == 'M_824b': IT(E04, '041')['sterkereHint'] += ' Sommige kinderen hebben er een.'   # Z-#824-uitzondering: één woord meer ('sommi') blijft FAIL
if MUT == 'M_bw': f_ = next(f for x in ITEMS if x['doelId'] == V1 for f in x['foutHints'] if f['uitleg'] == BWT[0]); f_['uitleg'] = BWT[2]   # V-#1032: eerste item met een 'som'-sleutel
if MUT == 'M_1040':   # V-#1040 (Didactiek 19:16:15): de nieuwe afleider boven het antwoord krijgt de algemene tekst; zonder die data: de eerste 'laag te veel'-sleutel
    V1040_ = {'018': '18', '026': '36', '035': '16', '080': '26'}
    f_ = next((f for x in ITEMS if x['doelId'] == V1 and x['merge']['somtypeNrOrigineel'] == 2 and x['nr'] in V1040_ for f in x['foutHints'] if f['fout'] == V1040_[x['nr']]), None) \
         or next(f for x in ITEMS if x['doelId'] == V1 for f in x['foutHints'] if f['uitleg'] == BWT[2])
    f_['uitleg'] = BWT[5]
if MUT == 'M_bw2': f_ = next(f for x in ITEMS if x['doelId'] == V1 for f in x['foutHints'] if f['uitleg'] == BWT[4]); f_['uitleg'] = BWT[6]
if MUT == 'M_label': FH(IT(E03, '009'), 'een week te veel')['soort'] = 'startbedrag vergeten'
if MUT == 'M_label2': FH(IT(E7, '001'), 'keer de tijd')['soort'] = 'tijd eraf'
if MUT == 'M_label3': FH(IT(E03, '002'), 'een week te weinig')['soort'] = 'niet bij die week'
if MUT == 'M_label4': FH(IT(E04, '025'), 'nee')['soort'] = 'niet te zien'
if MUT == 'M_lett': FH(IT(E04, '032'), 'ja')['regel'] = 'dat klopt'
if MUT == 'M_mist': IT(E04, '043')['foutHints'].pop()
if MUT == 'M_alg': FH(IT(E01, '001'), 'verdubbeld')['soort'] = 'andere fout'
if MUT == 'M_antw': x_ = IT(E7, '001'); x_['foutHints'].append(dict(x_['foutHints'][0], fout='60'))
if MUT == 'M_antw2': x_ = IT(E04, '043'); x_['foutHints'].append(dict(x_['foutHints'][0], fout='60 cm', regel='60 cm'))
if MUT == 'M_L2': IT(E03, '010')['foutHints'][0]['uitlegSterker'] = ''
if MUT == 'M_onb': IT(V1, '001')['foutHints'][0]['soort'] = 'iets nieuws'
if MUT == 'M_hussel': IT(E04, '042')['husselen'] = False
if MUT == 'M_klok': opg(E7, '002', 'in 1,5 uur', 'in 1,5 uur, vanaf 10:15')
if MUT == 'M_824': IT(E04, '042')['sterkereHint'] += ' Het was een eenzijdige groep.'
if MUT == 'M_264': IT(E04, '041')['hint'] = 'Wat als iemand thuis meer dan een dier heeft?'
if MUT == 'M_260': IT(E04, '042')['hint'] = 'Zij vroeg het aan een groep die eenzijdig is.'

def robuust(boven, ws):
    """V-#893 (les 326): elke aflezing op een heel streepje (naar beneden of naar boven, per beslissende staaf) ligt minstens één streepje (10) aan
    dezelfde kant van 50. Didactiek noemt 'veelvoud van 10'; 035 en 039 (35/40, Nee) keurt Didactiek goed, dus de guard toetst de aflezing."""
    import itertools
    for comb in itertools.product(*[{w // 10 * 10, -(-w // 10) * 10} for w in ws]):
        t_ = sum(comb)
        if (t_ >= 60) != boven or 40 < t_ < 60: return False
    return True
hits891 = []; hits893 = []; hits894 = []; groot891 = []
# Z-#824-uitzondering: H2 van VBN-E04 #35 is de letterlijke tekst van Didactiek (V-#895): 'hebben' (de kinderen die dat dier hebben) en 'meer'
# (samen meer tellen) noemen de optie niet; twijfel in review-batch6.md ronde 1b. Andere woorden uit het goede antwoord blijven FAIL.
Z824_OK = {}   # Z-#920 (ronde 1d): de uitzondering (E04, 35) {'hebbe', 'meer'} is vervallen (les 340)
andere = collections.Counter(); per_soort = collections.Counter(); KOP_DING = {}; pos = collections.Counter(); bwroute = collections.Counter()
STOP260 = set('de het een en van dat die dit is je zijn er in op om te met als of aan bij dan doe doen naar door voor wat welke hoe hoeveel niet geen nog ook maar wel zo eerst daarna dezelfde elke elk alle hetzelfde kijk reken uit welk antwoord getal getallen manier aanpak klopt kan moet moest had hij zij ze waar'.split())
def stems260(t): return {w[:5] for w in re.findall(r'[^\W\d_]{3,}', t.lower()) if w not in STOP260}
def t264(t): return stems260(t) | {v for w, v in (('tien', '10'), ('honderd', '100'), ('duizend', '1000'), ('helft', 'helft')) if re.search(rf'\b{w}\b|\b{v}\b', t, re.I)}
for x in ITEMS:
    doel = x['doelId']; nro = x['merge']['somtypeNrOrigineel']; o = x['opgave'].replace('\n', ' '); nid = f"{doel[3:]} #{nro} {x['nr']}"
    ops = [p['tekst'] for p in x.get('opties') or []]; mk = x['type'] == 'meerkeuze'
    h1, h2 = BT[(doel, nro)]['hint1'], BT[(doel, nro)]['hint2']
    if not x.get('hint') or not x.get('sterkereHint'): fail(f'{nid}: H1/H2 leeg')
    def eis(c, m):
        if not c: fail(f'{nid} data: {m} — klopt niet voor {o!r} => {x["antwoord"]}')
    for veld_, w_ in [('opgave', o), ('antwoord', x['antwoord'])] + [('optie', p) for p in ops]:
        if re.search(r'\b\d{1,2}:\d{2}\b', w_): fail(f"les 262 {nid} {veld_}: kloktijd met ':' ({w_!r}); G8: 15.00 uur")
    a = val(x['antwoord']); g = nums(o); ok = {}; routes = {}; tekstok = None
    if mk:
        if x['antwoord'] not in ops: fail(f'{nid}: antwoord niet in de opties'); continue
        if not x.get('husselen'): fail(f'{nid}: meerkeuze zonder husselen')
        pos[ops.index(x['antwoord'])] += 1
    elif ops: fail(f'{nid}: kaal item met opties')
    if doel == E7 and nro in (1, 3):
        d_, t_ = g[0], g[1]; eis(re.search(r'legt \d+ km af in \d+(,\d+)? uur\. Hoeveel kilometer per uur', o) is not None, 'afstand in km, tijd in uur, vraag per uur')
        eis(a == d_ / t_, "H1/H2: 'de kilometers gedeeld door het aantal uur' = het antwoord")
        eis(t_ % 1 == Fr(1, 2), "H2: 'met een half uur … maak allebei twee keer zo groot' (de tijd is hele uren + een half uur)")
        heel = Fr(int(t_))
        ok = {'getal uit de vraag': lambda v: v in g, 'keer de tijd': lambda v: v == d_ * t_, 'tijd eraf': lambda v: v == d_ - t_, 'alleen hele uren': lambda v: heel > 0 and v == d_ / heel}
        routes = {'keer de tijd': d_ * t_, 'tijd eraf': d_ - t_, 'alleen hele uren': d_ / heel if heel else None, 'tijd gedeeld door afstand': t_ / d_}
    elif doel == E7:
        t_, s_ = g[0], g[1]; eis(re.search(r'\d+(,\d+)? uur met [^.]*?\d* ?(km per uur|de trein)\.( De trein rijdt \d+ km per uur\.)? Hoeveel kilometer', o) is not None and len(g) == 2, 'tijd in uur, snelheid in km per uur')   # Z-#893 (build 17:03): ook '… met de trein. De trein rijdt # km per uur.'
        eis(a == s_ * t_, "H1/H2: 'de snelheid keer het aantal uur' = het antwoord"); eis(t_ % 1 == Fr(1, 2), "H2: 'een half uur is de helft van de snelheid'")
        heel = Fr(int(t_))
        ok = {'getal uit de vraag': lambda v: v in g, 'tijd erbij': lambda v: v == t_ + s_, 'alleen hele uren': lambda v: v == s_ * heel}
        routes = {'tijd erbij': t_ + s_, 'alleen hele uren': s_ * heel, 'gedeeld': s_ / t_}
    elif doel == V1 and nro == 1:
        ha = g[0]; eis(re.search(r'\d+(,\d+)? hectare\. Hoeveel m² is dat\?', o) is not None, "H1/H2 en TOEGESTAAN 'hectare': de maat in de vraag is hectare")
        eis(a == ha * 10000, "H2: 'honderd keer honderd, keer het aantal hectare' = het antwoord")
        ok = {'getal uit de vraag': lambda v: v == ha, 'nul te weinig': lambda v: v * 10 == a, 'honderd keer te weinig': lambda v: v * 100 == a}
        routes = {'keer duizend': ha * 1000, 'keer honderd': ha * 100, 'keer honderdduizend': ha * 100000}
    elif doel == V1 and nro == 2:
        j_ = x['visual']['jsRender']; dp, hg, br = j_['diep'], j_['hoog'], j_['breed']
        eis(j_.get('soort') == 'bouwsel' and a == dp * hg * br, "H1/H2: 'één laag keer het aantal lagen' = het antwoord (diep × hoog × breed)")
        eis(hg >= 2, "L1 'Er liggen meer lagen op elkaar' (minstens twee lagen)")
        R_ = {'som': dp + hg + br, 'helft': Fr(a, 2), 'laag+': dp * br * (hg + 1), 'laag-': dp * br * (hg - 1), 'laag': dp * br,
              '3vlak': dp * br + br * hg + dp * hg, 'zicht': dp * br + br * hg + dp * hg - dp - br - hg + 1, 'b-': (br - 1) * dp * hg, 'd-': (dp - 1) * br * hg}
        TOE = {BWT[0]: {'som'}, BWT[1]: {'helft'}, BWT[2]: {'laag+'}, BWT[3]: {'3vlak'}, BWT[4]: {'laag'}, BWT[5]: set(R_), BWT[6]: {'laag-'}, BWT[7]: {'b-', 'd-'}}
        tekstok = (R_, TOE); routes = {k_: v_ for k_, v_ in R_.items() if k_ != 'helft'}
        if all(val(p_['tekst']) <= a for p_ in x['opties']): groot891.append(x['nr'])
    elif doel == V1 and nro == 3:
        m_ = re.search(r'pak met (\d+(?:,\d+)?) liter drinken wordt verdeeld over bekers van (\d+) milliliter\. Hoeveel volle bekers', o)
        eis(m_ is not None, "H2 en TOEGESTAAN 'milliliter': pak in liter, beker in milliliter")
        if m_:
            L_, ml = Fr(m_.group(1).replace(',', '.')), int(m_.group(2)); eis(a == L_ * 1000 / ml, "H2: 'pak in milliliter gedeeld door één beker' = het antwoord")
            eis(L_ > 1, "L1 'Het pak is meer dan één liter'")
            ok = {'één liter': lambda v: v == Fr(1000, ml), 'nullen': lambda v: v in (L_ * 10, L_ * 100, L_ * 1000 / 100, a * 10, a / 10)}
            routes = {'één liter': Fr(1000, ml), 'komma weg': L_ * 10}
    elif doel == E01 and nro == 1:
        js = [int(v_) for v_ in re.findall(r'geeft (\d+) appels', o)]; m_ = re.search(r'verwacht je in jaar (\d+)', o)
        eis(len(js) == 3 and js[1] - js[0] == js[2] - js[1] and js[1] > js[0], "H1/H2: 'elk jaar komt er hetzelfde aantal bij'")
        if len(js) == 3:
            st_ = js[1] - js[0]; eis(m_ is not None and int(m_.group(1)) == 4 and a == js[2] + st_, "H2: 'nog één keer erbij, bovenop het grootste aantal' = het antwoord")
            ok = {'jaar ervoor': lambda v: v == js[2], 'verdubbeld': lambda v: v == 2 * js[2]}
            routes = {'jaar ervoor': js[2], 'verdubbeld': 2 * js[2]}
    elif doel == E01 and nro == 2:
        sp = [Fr(v_.replace(',', '.')) for v_ in re.findall(r'(\d+(?:,\d+)?) m\b', o)]
        eis(len(sp) == 5 and a == max(sp) - min(sp), "H1/H2: 'de verste min de kortste' = het antwoord")
        eis(any(',' not in v_ for v_ in re.findall(r'(\d+(?:,\d+)?) m\b', o)) and min(sp) == min(v_ for v_ in sp if v_.denominator == 1), "H2/L1: 'een sprong zonder komma is een hele meter' (en dat is de kortste)")
        ok = {'opgeteld': lambda v: v == max(sp) + min(sp), 'andere sprongen': lambda v: v != a and any(abs(p_ - q_) == v for p_ in sp for q_ in sp)}
        routes = {'opgeteld': max(sp) + min(sp)}
    elif doel == E03 and nro == 1:
        m_ = re.fullmatch(r'Een spaartabel: week 0 → €(\d+), week 1 → €(\d+), week 2 → €(\d+)\. Wat staat er bij week (\d+)\?', o)
        eis(m_ is not None, "H2: 'begin bij het bedrag van week nul' (de tabel begint bij week 0)")
        if m_:
            S_, y1, y2, n_ = (int(v_) for v_ in m_.groups()); p_ = y1 - S_
            eis(y2 - y1 == p_ and n_ > 2 and a == S_ + n_ * p_, "H1/H2: 'elke week dezelfde stap; week nul plus de stap zo vaak als de week' = het antwoord")
            ok = {'niet bij die week': lambda v: v in (y2 + p_, n_ * p_), 'een week te weinig': lambda v: v == S_ + (n_ - 1) * p_}
            routes = {'volgende in de tabel': y2 + p_, 'startbedrag vergeten': n_ * p_, 'een week te weinig': S_ + (n_ - 1) * p_, 'een week te veel': S_ + (n_ + 1) * p_}
    elif doel == E03:
        m_ = re.fullmatch(r'Je spaart voor [\w ]+\. Je begint met €(\d+) en legt elke week €(\d+) erbij\. Hoeveel heb je na (\d+) weken\?', o)
        eis(m_ is not None, "H1/H2: startbedrag, weekbedrag, aantal weken")
        if m_:
            S_, p_, n_ = (int(v_) for v_ in m_.groups()); eis(S_ > 0 and a == S_ + n_ * p_, "H2: 'weekbedrag keer weken, plus het startbedrag' = het antwoord")
            ok = {'startbedrag vergeten': lambda v: v == n_ * p_, 'een week te veel': lambda v: v == S_ + (n_ + 1) * p_, 'alles opgeteld': lambda v: v == S_ + p_ + n_}
            routes = {'startbedrag vergeten': n_ * p_, 'een week te veel': S_ + (n_ + 1) * p_, 'een week te weinig': S_ + (n_ - 1) * p_, 'alles opgeteld': S_ + p_ + n_}
    elif doel == E04 and nro in (1, 2, 3, 4, 5, 32, 33, 34):
        j_ = x['visual']['jsRender']; sv = {s_['naam']: s_['waarde'] for s_ in j_.get('staven') or []}
        eis(j_.get('soort') == 'staafdiagram' and j_.get('perstreep') == 10 and 'Elk streepje is 10.' in o, "H2: 'elk streepje is tien procent'")
        eis(sum(sv.values()) == 100 and 'toont percentages' in o, "H1/H2/L1: het diagram toont percentages (samen honderd)")
        JA, NEE, NZ = 'Ja, dat klopt.', 'Nee, dat klopt niet.', 'Dat kun je hier niet zien.'
        eis(sorted(ops) == sorted([JA, NEE, NZ]), 'de drie opties Ja / Nee / Dat kun je hier niet zien')
        if nro in (1, 3, 5):
            eis(re.search(r'"\d+ kinderen kozen \w+\."', o) is not None and x['antwoord'] == NZ, "H1/L1: de zin noemt een aantal; zonder totaal niet te zien")
            ok = {'ja': lambda v: v == JA, 'nee': lambda v: v == NEE}
            # V-#894 (les 325): het genoemde aantal past bij een heel totaal (aantal × 100 / percentage), anders is 'Nee' strikt af te leiden
            m_ = re.search(r'"(\d+) kinderen kozen (\w+)\."', o); p_ = sv.get(m_.group(2)) if m_ else None
            if m_ and p_ and (int(m_.group(1)) * 100) % p_:
                fail(f"V-#894 {nid}: {m_.group(1)} kinderen bij {p_} % geeft totaal {int(m_.group(1)) * 100 / p_:.1f}, geen heel getal (dan is 'Nee' af te leiden)"); hits894.append(x['nr'])
        elif nro in (2, 4, 33):
            m_ = re.search(r'"Meer dan de helft van [\w ]+ kiest (\w+)\."', o); w_ = sv.get(m_.group(1)) if m_ else None
            eis(w_ is not None and x['antwoord'] == (JA if w_ > 50 else NEE), "H1/H2: 'meer dan de helft = boven vijftig procent' beslist het antwoord")
            ok = {'ja': lambda v: v == JA, 'nee': lambda v: v == NEE, 'niet te zien': lambda v: v == NZ}
            if w_ is not None: eis(w_ != 50, 'de staaf staat niet precies op vijftig procent (H2 boven/niet boven)')
            if w_ is not None and not robuust(w_ > 50, [w_]): fail(f"V-#893 {nid}: de beslissende staaf {m_.group(1)} staat op {w_}; afgelezen op een heel streepje kan het antwoord omslaan (les 326)"); hits893.append(x['nr'])
        elif nro == 32:
            m_ = re.search(r'"Tekenen is precies (\d+) keer zo vaak gekozen als (\w+)\."', o)
            eis(m_ is not None and 'tekenen' in sv and x['antwoord'] == (JA if sv['tekenen'] == int(m_.group(1)) * sv.get(m_.group(2), -1) else NEE), "H2: 'de andere staaf keer het getal = tekenen?' beslist het antwoord")
            ok = {'ja': lambda v: v == JA, 'niet te zien': lambda v: v == NZ}
        else:
            m_ = re.search(r'"Water en (\w+) zijn samen meer dan de helft\."', o)
            eis(m_ is not None and x['antwoord'] == (JA if sv.get('water', 0) + sv.get(m_.group(1), 0) > 50 else NEE), "H2: 'twee staven samen, meer dan vijftig procent?' beslist het antwoord")
            ok = {'nee': lambda v: v == NEE, 'niet te zien': lambda v: v == NZ}
            if m_ and not robuust(sv.get('water', 0) + sv.get(m_.group(1), 0) > 50, [sv.get('water', 0), sv.get(m_.group(1), 0)]):
                fail(f"V-#893 {nid}: water {sv.get('water')} + {m_.group(1)} {sv.get(m_.group(1))}: afgelezen op hele streepjes kan het antwoord omslaan (les 326)"); hits893.append(x['nr'])
        if any(v_ % 10 for v_ in sv.values()): I.append(f'INFO {nid}: staven tussen twee streepjes ({sorted(sv.values())}; perstreep 10): halve streepjes aflezen (datapunt)')
    elif doel == E04 and nro == 35:
        m_ = re.search(r'Een klas telt (\d+) kinderen\. In een staafdiagram over huisdieren (?:zijn de staven samen|tellen de staven samen op tot) (\d+)\b', o)   # Z-#894 (build 17:36): 'tellen … op tot #' i.p.v. '# hoog'
        eis(m_ is not None and int(m_.group(2)) > int(m_.group(1)), "H1/L1: 'de staven samen komen boven het aantal in de klas uit'")
        ok = {'fout getekend': lambda v: v == 'De grafiek is fout getekend', 'getal uit het diagram': lambda v: m_ is not None and m_.group(2) in v and 'in de klas' in v}
    elif doel == E04 and nro == 36:
        eis('schaakclub' in o and 'schaken' in o, "H1/H2/L1: de groep is een schaakclub")
        ok = {'te weinig': lambda v: 'te weinig' in v, 'niets mis': lambda v: 'niets mis' in v}
    elif doel == E04 and nro == 37:
        ms = [int(v_) for v_ in re.findall(r'(\d+) cm', o)]; srt = sorted(ms); med = srt[len(srt) // 2]
        uit = max(ms, key=lambda v_: abs(v_ - med)); rest_ = [v_ for v_ in ms if v_ != uit]
        eis(a == uit and max(rest_) - min(rest_) <= 5 and abs(uit - med) >= 4 * (max(rest_) - min(rest_)), "H1/H2/L2: 'vier liggen dicht bij elkaar, één ligt ver weg' = het antwoord")
        ok = {'kleinste': lambda v: v == min(ms) and v in rest_, 'dichtbij': lambda v: v in rest_}
    else:
        fail(f'{nid}: geen check voor dit somtype')
    for r_, w_ in routes.items():   # les 306
        if w_ is not None and a is not None and w_ == a:
            if tekstok and not any(r_ in TOE[t_] for t_ in TOE if t_ != BWT[5]): W.append(f'les 317 {nid}: Claudes route {r_!r} ({"×".join(map(str, (dp, hg, br)))}) geeft toevallig het goede antwoord; geen sleutel, geen hint op die route (datapunt)')
            elif tekstok: fail(f'V-#891 les 306/327 {nid}: de route {r_!r} ({"×".join(map(str, (dp, hg, br)))}) geeft het goede antwoord, en die misvatting heeft een eigen tekst in het somtype'); hits891.append(x['nr'])
            else: fail(f'les 306 {nid}: de foute route {r_!r} geeft het goede antwoord')
    # ---- sleutels ----
    gedekt = collections.Counter()
    for fh in x['foutHints']:
        s = fh['soort']; per_soort[(doel[3:], nro, s)] += 1
        if not fh.get('uitlegSterker'): fail(f"{nid} {fh['fout']!r}: geen laag 2")
        if fh['fout'] == x['antwoord']: fail(f'{nid}: fout-hint op het goede antwoord'); continue
        if mk and not (doel == V1 and nro == 2):
            if fh['fout'] not in ops: fail(f"{nid}: fout-hint {fh['fout']!r} is geen optie"); continue
            if s == 'andere fout': fail(f"{nid} {fh['fout']!r}: meerkeuze-optie op 'andere fout' (verwacht: een letterlijke regel)"); continue
            pakt = [p for p in ops if past(fh['regel'], p)]
            if pakt != [fh['fout']]: fail(f"{nid} regel {fh['regel']!r}: pakt {pakt} in plaats van alleen {fh['fout']!r} (les 160/161)")
            gedekt[fh['fout']] += 1
            f_ = ok.get(s); w_ = val(fh['fout']) if doel in (V1, E01) or nro == 37 else fh['fout']
            if f_ is None: fail(f"{nid} {fh['fout']!r}: soort {s!r} heeft geen check"); continue
            if not f_(w_): fail(f"{nid} {fh['fout']!r}: soort {s!r} klopt niet (antwoord {x['antwoord']})")
            continue
        v = val(fh['fout'], noteer=(doel, nro, x['nr'], fh['fout'], s))
        if v is None: fail(f"{nid} sleutel {fh['fout']!r}: niet te lezen"); continue
        if v == a: fail(f"{nid}: sleutel {fh['fout']!r} = het antwoord (op waarde)"); continue
        if tekstok:
            R_, TOE = tekstok; rs_ = {k_ for k_, w_ in R_.items() if w_ == v}
            if fh['fout'] not in ops: fail(f"{nid}: sleutel {fh['fout']!r} is geen optie"); continue
            gedekt[fh['fout']] += 1
            if fh['uitleg'] not in TOE: fail(f"{nid} {fh['fout']!r}: tekst is geen van de routeteksten: {fh['uitleg'][:60]}"); continue
            if not (rs_ & TOE[fh['uitleg']]): fail(f"{nid} {fh['fout']!r}: routetekst «{fh['uitleg'][:45]}…» past niet; routes van deze waarde: {sorted(rs_) or 'geen'}")
            # V-#891/Z-#890: routetekst op waarde. Is er een eigen tekst die voor alle routes van deze waarde waar is, dan niet de algemene tekst
            eigen_ = [t_ for t_ in TOE if t_ != BWT[5] and rs_ and rs_ <= TOE[t_]]
            if eigen_ and fh['uitleg'] == BWT[5]: fail(f"V-#891 {nid} {fh['fout']!r}: krijgt de algemene tekst, maar de route {sorted(rs_)} heeft een eigen tekst («{eigen_[0][:40]}…»)")
            bwroute[(BWT.index(fh['uitleg']), tuple(sorted(rs_)))] += 1; continue
        if s == 'andere fout':
            r_ = next((r for r, w in routes.items() if w == v), 'overig'); andere[(doel[3:], nro, r_)] += 1; continue
        f_ = ok.get(s)
        if f_ is None: fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} heeft geen check"); continue
        if not f_(v): fail(f"{nid} sleutel {fh['fout']!r}: soort {s!r} klopt niet (antwoord {x['antwoord']})")
    if mk:
        for p in ops:
            if p != x['antwoord'] and gedekt[p] != 1: fail(f'{nid}: foute optie {p!r} heeft {gedekt[p]} fout-hints (verwacht 1)')
        # verklaptoets (les 260 (o), Z-#824 / les 288, les 264)
        for L_, h_ in (('H1', x['hint']), ('H2', x['sterkereHint'])):
            sc_ = {p: len(stems260(p) & stems260(h_)) for p in ops}
            if sc_[x['antwoord']] >= 2 and sc_[x['antwoord']] > max(v_ for p, v_ in sc_.items() if p != x['antwoord']): fail(f"les 260 {nid} {L_}: beschrijft het goede antwoord: {h_}")
        eigen_ = stems260(x['antwoord']) - set().union(*[stems260(p) for p in ops if p != x['antwoord']]) - stems260(o)
        wa_ = re.findall(r'[^\W\d_]+|\d+', x['antwoord'].lower())
        for L_, h_ in (('H1', x['hint']), ('H2', x['sterkereHint'])):
            if len((eigen_ & stems260(h_)) - Z824_OK.get((doel, nro), set())) >= 2: fail(f"Z-#824 {nid} {L_}: noemt {sorted(eigen_ & stems260(h_))} uit het goede antwoord (alleen daar): {h_}")
            wh_ = ' '.join(re.findall(r'[^\W\d_]+|\d+', h_.lower())); k_ = min(5, len(wa_))
            if len(wa_) >= 2 and any(' '.join(wa_[i:i + k_]) in wh_ for i in range(len(wa_) - k_ + 1)): fail(f"Z-#824 {nid} {L_}: neemt een stuk van het goede antwoord letterlijk over: {h_}")
        for w_ in t264(x['hint']) - t264(o):
            if [p for p in ops if w_ in t264(p)] == [x['antwoord']]: fail(f"les 264 {nid} H1: {w_!r} staat alleen in het goede antwoord: {x['hint']}")
    # [..]-woorden uit de opgave (les 147): elke plek tussen haken, behalve de tekening vooraan
    kop = re.sub(r'^\[[^\]]+\]\s*', '', x['merge']['somtype']).replace(' ⏎ ', ' '); vast = set(re.findall(r'\w+', re.sub(r'\[\w+\]', ' ', kop).lower()))
    pat = re.sub(r'\\\[\w+\\\]', '(.+?)', re.escape(kop).replace(r'\#', r'[\d.,]+'))
    m = re.fullmatch(pat, o)
    if m is None and '[' in kop: W.append(f'{nid}: kop past niet op de opgave (contextwoorden niet bepaald)')
    KOP_DING.setdefault((doel, nro), set()).update({w for grp in (m.groups() if m else ()) for w in re.findall(r'[^\W\d]{3,}', grp.lower())} - vast - {'een', 'het', 'der', 'geeft', 'erbij'})
I.append('INFO sleutels per soort: ' + '; '.join(f'{k[0]} #{k[1]} {k[2]}={n}' for k, n in sorted(per_soort.items())))
I.append("INFO 'andere fout' per route (datapunt): " + '; '.join(f'{k[0]} #{k[1]} {k[2]}={n}' for k, n in sorted(andere.items())))
# V-#1061 (Didactiek, verplicht; Oefeningen b6 ronde 1e): de oude 'drie kanten'-tekst zei 'er zitten ook blokjes binnenin' (= te weinig geteld), maar bij
# 9 van de 33 sleutels ligt drie kanten BOVEN het antwoord. Die tekst mag nergens terugkomen: niet in een kindtekst van een item, niet in de entry.
OUD1061 = 'er zitten ook blokjes binnenin'
if MUT == 'M_1061': f_ = next(f for x in ITEMS if x['doelId'] == V1 for f in x['foutHints'] if 'drie kanten' in f['uitleg']); f_['uitleg'] = 'Dat zijn de blokjes van drie kanten samen: voorkant, zijkant en bovenkant. Het bouwwerk is vol, dus er zitten ook blokjes binnenin.'
if MUT == 'M_1061e': next(f for s_ in B['somtypen'] if (s_['doel'], s_['nrOrigineel']) == (V1, 2) for f in s_['foutHints'])['tekstSterker'] += ' Het bouwwerk is vol, dus er zitten ook blokjes binnenin.'
for x in ITEMS:
    if x['doelId'] != V1: continue
    for f_ in x['foutHints']:
        if OUD1061 in (f_.get('uitleg') or '') + ' ' + (f_.get('uitlegSterker') or ''): fail(f"V-#1061 MEET-V01 #{x['merge']['somtypeNrOrigineel']} {x['nr']} {f_['fout']!r}: oude tekst 'binnenin' (richting die niet voor elk item klopt)")
for s_ in B['somtypen']:
    if s_['doel'] != V1: continue
    for f_ in s_['foutHints']:
        if OUD1061 in f_['tekst'] + ' ' + (f_.get('tekstSterker') or ''): fail(f"V-#1061 entry MEET-V01 nrO{s_['nrOrigineel']} '{f_['soort']}': oude tekst 'binnenin'")
I.append(f'INFO V-#891 (drie kanten = antwoord, FAIL): {len(hits891)} {sorted(hits891)}')
I.append(f'INFO V-#893 (beslissende staaf niet op een heel streepje / te dicht bij 50): {len(hits893)} {sorted(hits893)}')
I.append(f'INFO V-#894 (aantal past bij geen heel totaal): {len(hits894)} {sorted(hits894)}')
Z891_MAX = 69   # Z-#891 (Oef-#459): het antwoord is de grootste optie; ratel 94 → 69 van de 151 na V-#1032 (build 19:14:01); mag niet stijgen
I.append(f'INFO Z-#891: het goede antwoord is de grootste optie bij {len(groot891)} van de V01 #2-items (ratel {Z891_MAX})')
if len(groot891) > Z891_MAX: fail(f'Z-#891 MEET-V01 #2: het goede antwoord is de grootste optie bij {len(groot891)} items (meer dan {Z891_MAX}; geef vaker een afleider boven het antwoord)')
I.append('INFO MEET-V01 #2 routetekst → routes van de waarde: ' + '; '.join(f'tekst {k[0]} {list(k[1])}={n}' for k, n in sorted(bwroute.items())))
I.append(f'INFO Claude-sleutels met een punt als komma (datapunt Oef-#498): {len(PUNT)} ' + '; '.join(f'{p[0][3:]} #{p[1]} {p[2]} {p[3]!r}→{p[4]}' for p in PUNT))
I.append(f'INFO meerkeuze: plek van het goede antwoord in de data {dict(sorted(pos.items()))}')
# ---- teksten ----
TOEGESTAAN = {(V1, 1): {'hectare'}, (V1, 3): {'milliliter'}, (E04, 35): {'kinderen'}}   # #35 (1 item): de data-eis vraagt 'Een klas telt # kinderen' (H2 V-#895 van Didactiek)
TXT = []
for s in B['somtypen']:
    k_ = (s['doel'], s['nrOrigineel'])
    TXT += [(k_, 'H1', s['hint1']), (k_, 'H2', s['hint2']), (k_, 'OZ', s['ouderzin'])]
    for f in s['foutHints']:
        for i_, t_ in enumerate(f['tekst'].split(' / ')): TXT.append((k_, f"L1 {f['soort']}" + (f' ({i_})' if ' / ' in f['tekst'] else ''), t_))
        TXT.append((k_, f"L2 {f['soort']}", f.get('tekstSterker') or ''))
        if not f.get('tekstSterker'): fail(f"{k_} {f['soort']}: geen tekstSterker")
    if s['foutHints'][-1]['soort'] != 'andere fout': fail(f"{k_}: 'andere fout' niet als laatste")
MUTS = {'M_cijfer': ((E7, 1), 'Deel door 2,5.'), 'M_letter': ((E04, 36), 'Kies optie B.'), 'M_plek': ((E01, 2), 'Kijk naar de eerste sprong.'), 'M_zoveel': ((E03, 2), 'Zoveel weken spaar je.'),
        'M_217': ((E7, 2), 'Hier tel je niets op, je doet alleen keer.'), 'M_217b': ((E7, 1), 'Aftrekken is hier niet goed.'), 'M_231': ((V1, 1), 'Doe het zoals bij de vorige som.'),
        'M_ctx': ((E04, 1), 'Kijk naar de staaf van rekenen.'), 'M_ctx2': ((E04, 3), 'Kijk naar het lievelingsvak.'), 'M_ctx3': ((E7, 1), 'De bus rijdt hard.'), 'M_ctx4': ((E04, 34), 'Kijk naar de melk.'),
        'M_moeilijk': ((V1, 1), 'Vermenigvuldig het getal.'), 'M_Bijna': ((E03, 1), 'Bijna goed!'), 'M_woorden': ((E04, 37), 'Zoek de meting die ver weg ligt. ' * 9),
        'M_235': ((E01, 1), 'Kijk naar de tabel. Kijk naar de tabel.'), 'M_klokw': ((E7, 2), 'Om half drie ben je er.'), 'M_deel': ((E7, 1), 'Reken 150 : 2,5 uit.')}
if MUT in MUTS: TXT.append((MUTS[MUT][0], 'L1 mutant', MUTS[MUT][1]))
LES217B = re.compile(r"\b(optellen|aftrekken|plus|min|keer|delen|erbij|eraf|vermenigvuldigen)\b[^.?!]{0,20}\b(is\s+(hier\s+)?niet\s+goed|mag\s+(hier\s+)?niet)\b"
                     r"|\b(mag|mogen)\s+(je\s+)?(hier\s+)?niet\s+(op\s*tellen|optellen|aftrekken|plus|erbij|keer|delen)\b|\b(niets|niet|nooit|geen)\b[^.?!]{0,25}\bop\s+te\s+tellen\b", re.I)
# les 147 ook voor vaste kopwoorden van somtypes met dezelfde H1/H2 (b5): woorden die maar in een deel van die koppen staan (zonder stopwoorden)
KOPS = collections.defaultdict(dict)
for x in ITEMS: KOPS[x['doelId']][x['merge']['somtypeNrOrigineel']] = x['merge']['somtype']
GROEP_VERBODEN = {}
for doel_, kops_ in KOPS.items():
    grp = collections.defaultdict(list)
    for n_ in kops_: grp[(BT[(doel_, n_)]['hint1'], BT[(doel_, n_)]['hint2'])].append(n_)
    for ns_ in grp.values():
        if len(ns_) < 2: continue
        ws_ = [set(re.findall(r'[^\W\d]{3,}', re.sub(r'\[[^\]]+\]', ' ', kops_[n_]).lower())) for n_ in ns_]
        for n_ in ns_: GROEP_VERBODEN[(doel_, n_)] = set.union(*ws_) - set.intersection(*ws_) - STOP260
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
    if lab != 'OZ':
        for w in KOP_DING.get(k_, ()):
            if w in TOEGESTAAN.get(k_, ()): continue
            stam = re.sub(r'(jes|en|s)$', '', w); stam = stam if len(stam) >= 5 else w; stam2 = re.sub(r'([aeou])([^aeiou\W])$', r'\1\1\2', stam)
            if re.search(rf'\b({re.escape(w)}|({re.escape(stam)}|{re.escape(stam2)})(je|jes|en|s)?)\b', t, re.I): fail(f'les 147 {tag}: contextwoord {w!r} uit een [..]-plek: {t}')
        for (d2, n2), ws in KOP_DING.items():
            if d2 != k_[0] or n2 == k_[1] or BT[(d2, n2)]['hint2'] != BT[k_]['hint2']: continue
            for w in ws - TOEGESTAAN.get(k_, set()):
                if re.search(rf'\b{re.escape(w)}\b', t, re.I): fail(f'les 147 {tag}: contextwoord {w!r} uit somtype nrO{n2} (zelfde teksten): {t}')
    if (m := MOEILIJK.search(t)): fail(f'{tag}: moeilijk woord {m.group(1)!r}: {t}')
    if re.search(r'\bbijna\b', t, re.I) and lab != 'OZ': fail(f"{tag}: 'Bijna': {t}")
    nw_ = len(t.split()); max_ = 55 if lab.startswith(('H2', 'L2')) else 45 if lab.startswith(('H1', 'L1')) else None
    if max_ and nw_ > max_: fail(f'V-#764 {tag}: {nw_} woorden (maximaal {max_}): {t[:80]}')
    zz_ = [z.strip() for z in re.split(r'(?<=[.?!])\s+', t) if z.strip()]
    if len(zz_) != len(set(zz_)): fail(f'les 235 {tag}: dezelfde zin twee keer: {t[:80]}')
    lang = [z for z in zz_ if len(z.split()) > 25]
    if lang: W.append(f'{tag}: lange zin ({len(lang[0].split())} woorden): {lang[0]}')
I.append('INFO contextwoorden: ' + '; '.join(f'{k[0][3:]} nrO{k[1]} {sorted(v)}' for k, v in sorted(KOP_DING.items()) if v))
# les 234: snapshot van de opties
SNAP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/opties_snapshot.json'
OPTS = {f"{x['doelId']} {x['nr']}": sorted(o_['tekst'] for o_ in (x.get('opties') or [])) for x in ITEMS if x.get('opties')}
if MUT == 'M_afl': k0_ = sorted(OPTS)[0]; OPTS[k0_] = OPTS[k0_][:-1] + ['iets anders']
if os.environ.get('SNAP') == '1': json.dump(OPTS, open(SNAP, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO les 234: snapshot geschreven ({len(OPTS)} items)')
elif os.path.exists(SNAP):
    oud_ = json.load(open(SNAP))
    for k_ in sorted(set(oud_) | set(OPTS)):
        if oud_.get(k_) != OPTS.get(k_): fail(f'les 234 item {k_}: opties veranderd: routes, letterlijke regels en verklaptoets (les 300) nalopen, dan SNAP=1')
else: W.append('les 234: geen snapshot (SNAP=1 python3 check.py)')
for m in I: print(m)
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))); from l271 import les271
for m_ in les271(G8, 6, B): fail(m_)
for m in W: print('WARN', m)
for m in F: print('FAIL', m)
print(f'G8 b6: {len(ITEMS)} items · {sum(len(x["foutHints"]) for x in ITEMS)} sleutels · FAIL {len(F)} · WARN {len(W)} · INFO {len(I)}')
sys.exit(1 if F else 0)
