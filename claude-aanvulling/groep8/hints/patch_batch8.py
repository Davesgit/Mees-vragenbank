#!/usr/bin/env python3
"""Patcht hints/batch8.json IN PLACE (G8 batch 8: VERH-E01/E02/E03/E04/E06/V01), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch8.json. Na een sync of rebuild nooit make_batch8.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch8.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~17:55): Overzichts b8-data in build 17:47:17 (Oef-#1010) ----------
# E04 #8 (032) kreeg nieuwe getallen: «Van de 200 kinderen op school komt 30 procent met de fiets.» → 60 kinderen; opties 30 / 170 / 60.
# Oude regels: '60 kinderen' (procent als aantal) is nu het goede antwoord en '100 kinderen' bestaat niet meer (check_hints WARN ONLEESBAAR).
# VOORWAARDELIJK en twee kanten op (les 361, zoals Z-#960): nieuwe opties → '30 kinderen' (procent als aantal) en '170 kinderen'
# (geheel min het procent); oude opties (60/100/90) → de regels van ronde 1; andere data → niets (b8/check en check_hints vallen dan op).
import json as _json
R1B = 'Ronde 1b (Oefeningen 8 okt; Overzichts b8-data 17:47/17:49 en Didactiek review-batch8a/8b)'
E04 = 'G8-VERH-E04'
_L2_8 = 'Reken uit hoeveel tien procent is: deel het aantal op school door tien. Hoe vaak heb je tien procent nodig?'
def _r(soort, regel, tekst): return {'bron': 'nieuw', 'soort': soort, 'claudeDenkfout': None, 'regel': regel, 'tekst': tekst, 'tekstSterker': _L2_8}
_PROC = 'Dat is het getal van het procent, nog geen aantal. Hoeveel is dat procent van iedereen op school?'
_ALG8 = _r('andere fout', 'andere fout', 'Iedereen op school samen is honderd procent. Hoeveel is tien procent? Hoe vaak heb je dat nodig?')
def _stand032():
    try: its_ = _json.load(open(os.path.join(patch_lib.BASE, 'data', 'per_doel', f'{E04}.json'), encoding='utf-8'))['items']
    except Exception: return None
    x_ = [i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == 8]
    if len(x_) != 1: return None
    st_ = (x_[0]['antwoord'], sorted(o_['tekst'] for o_ in x_[0].get('opties') or []))
    if st_ == ('60 kinderen', ['170 kinderen', '30 kinderen', '60 kinderen']): return 'nieuw'
    if st_ == ('90 kinderen', ['100 kinderen', '60 kinderen', '90 kinderen']): return 'oud'
    return None
_ST032 = _stand032()
if _ST032 == 'nieuw':
    PATCH.append((E04, 8, 'foutHints', [_r('procent als aantal', '30 kinderen', _PROC),
        _r('geheel min het procent', '170 kinderen', 'Dat is iedereen op school min het getal van het procent. Het procent is geen aantal kinderen: hoeveel is dat procent van iedereen op school?'),
        _ALG8], f"{R1B}: nieuwe opties 30/170, teksten van Didactiek (V-#981); oude regels '60'/'100 kinderen' weg"))
elif _ST032 == 'oud':
    PATCH.append((E04, 8, 'foutHints', [_r('procent als aantal', '60 kinderen', _PROC),
        _r('te veel', '100 kinderen', 'Dat is te veel. Reken uit hoeveel tien procent van iedereen op school is, en neem dat zo vaak als nodig.'),
        _ALG8], f'{R1B}: oude opties (data terug): regels van ronde 1'))

# E06 #3: kop in build 17:47:17 «#% van de appels in [plek] is rot. Schrijf dat als kommagetal.» (Oef-#1008). Teksten nagekeken: ze noemen
# geen ding en geen plek ('het getal van het procent', 'honderdsten'), dus ze passen. Alleen deze kop wordt als nagekeken gemarkeerd (een latere kop niet).
_KOP_E06_3 = '#% van de appels in [plek] is rot. Schrijf dat als kommagetal.'
_s63 = next((s_ for s_ in _json.load(open(os.path.join(patch_lib.BASE, 'hints', 'batch8.json'), encoding='utf-8'))['somtypen']
             if s_['doel'] == 'G8-VERH-E06' and s_['nrOrigineel'] == 3), {})
if (_s63.get('kopGewijzigd') or {}).get('naar') == _KOP_E06_3 or _s63.get('kopNagekeken'):
    PATCH.append(('G8-VERH-E06', 3, 'kopNagekeken', None, f'{R1B}: kop nagekeken (Oef-#1008), teksten passen'))

# E06 #3: Oef-#1008 (build 17:47/17:49) zette Claudes sleutel '12.5' om naar '12,5'; die valt nu op de motorregel 'getal uit de vraag'.
# De omweg (CL 'kommagetal-als-geheel', soort 'procent zonder komma (punt)') vangt niets meer: weg. Alleen als die sleutel echt weg is.
def _e06_3_punt():
    try: its_ = _json.load(open(os.path.join(patch_lib.BASE, 'data', 'per_doel', 'G8-VERH-E06.json'), encoding='utf-8'))['items']
    except Exception: return True
    import re as _re   # Z-#990 (ronde 1c): alleen Claudes sleutels zelf (extraVelden); die zet de build in fase 1 om, dus fase 3 en na de apply zien hetzelfde.
    # Vóór 1c keek dit naar het hele item (ook velden die de apply nog overschrijft): in fase 3 'ja', na de build 'nee' → tweede run op live gaf 1.
    return any(_re.fullmatch(r'\d+\.\d{1,2}', str(d_.get('fout', '')).strip()) for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == 3
               for k_ in ('claudeDenkfouten', 'claudeFoutHints') for d_ in (i_.get('extraVelden') or {}).get(k_) or [])
_fh63 = huidig(8, 'G8-VERH-E06', 3)
if not _e06_3_punt() and any(f_['soort'] == 'procent zonder komma (punt)' for f_ in _fh63):
    PATCH.append(('G8-VERH-E06', 3, 'foutHints', [f_ for f_ in _fh63 if f_['soort'] != 'procent zonder komma (punt)'],
                  f"{R1B}: omweg voor '12.5' weg (Oef-#1008: nu '12,5', motorregel 'getal uit de vraag')"))
elif _e06_3_punt() and not any(f_['soort'] == 'procent zonder komma (punt)' for f_ in _fh63):   # data terug (les 361): omweg terug
    PATCH.append(('G8-VERH-E06', 3, 'foutHints', voeg_in(_fh63, 'procent zonder komma', [{'bron': 'claude-taalfix', 'soort': 'procent zonder komma (punt)', 'claudeDenkfout': 'kommagetal-als-geheel', 'regel': 'Claudes sleutel: kommagetal-als-geheel', 'tekst': 'Dat is het getal van het procent. Als kommagetal is het honderd keer zo klein.', 'claudeTekst': None, 'waarom': 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt (Oef-#490/#494); vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', 'tekstSterker': 'Deel het getal van het procent door honderd: de komma schuift twee plekken naar links. Is er geen heel getal? Zet dan een nul voor de komma.'}]),
                  f"{R1B}: sleutel met punt terug in de data: omweg terug"))

# ---- Didactiek review-batch8a/8b (17:45–17:55) ----
# V-#982 (les 373): E06 #2 aparte teksten voor de teller ('21%') en de noemer ('40%').
# Z-#974: E02 L1 bij €6,50 (het verschil in aantal als euro's erbij).
PATCH.append(('G8-VERH-E02', 1, ('fh', 'een klein bedrag erbij', {'tekst': 'Je deed het verschil in aantal erbij, alsof elk extra stuk één euro kost. Wat kost er één? Doe dat keer het aantal dat gevraagd wordt.'}), None,
              f'{R1B}: Z-#974'))
# E03 (schaal):
# Z-#972 (les 367): '(de punten vallen ook weg)' in de H2 waar vijf nullen wegvallen (km #1–#3/#8/#11, cm #4–#6), ook in de laag 2 (= de H2).
# Z-#971: #4–#6 L1 'getal uit de vraag' (sleutel '1' uit '1 :'; de oude zin stuurde bij 1 cm de verkeerde kant op).
# V-#971 (VOORWAARDELIJK op Overzichts V-#970, zoals #493): #8/#11 krijgen dezelfde regels als #1–#3 zodra geen getal uit de opgave het antwoord is;
# staat de schaal nog op 1 : 100.000 (cm = antwoord), dan blijven 'getal uit de vraag' en ': 10' weg (b8/check geeft dan les 306 = data). Twee kanten op (les 361).
E03 = 'G8-VERH-E03'
def _z972(t): return t if '(de punten vallen ook weg)' in t else t.replace('vijf nullen weg:', 'vijf nullen weg (de punten vallen ook weg):')
def _getal_is_antwoord(nro):
    try: its_ = _json.load(open(os.path.join(patch_lib.BASE, 'data', 'per_doel', f'{E03}.json'), encoding='utf-8'))['items']
    except Exception: return None
    x_ = [i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == nro]
    if not x_: return None
    import re as _re
    norm_ = lambda w: w.replace('.', '')
    return any(norm_(x['antwoord']) in [norm_(g) for g in _re.findall(r'\d+(?:\.\d{3})*', x['opgave'])] for x in x_)
_E03 = {n_: huidig(8, E03, n_) for n_ in range(1, 12)}
_H2 = {n_: huidig(8, E03, n_, 'hint2') for n_ in range(1, 12)}
_Z971 = 'Dat getal staat al in de vraag. Hoeveel kilometer is één centimeter op deze kaart? Hoe vaak past dat in de echte afstand?'
for n_ in range(1, 12):
    if n_ in (7, 9, 10): continue
    h2_ = _z972(_H2[n_])
    if n_ in (8, 11):
        g_ = _getal_is_antwoord(n_)
        if g_ is None: fh_ = _E03[n_]
        else: fh_ = [dict(f_) for f_ in _E03[1] if not (g_ and f_['soort'] in ('getal uit de vraag', 'tien keer te weinig'))]   # #1 is de bron (zelfde teksten)
    else: fh_ = [dict(f_) for f_ in _E03[n_]]
    for f_ in fh_:
        if f_.get('tekstSterker'): f_['tekstSterker'] = _z972(f_['tekstSterker'])
        if n_ in (4, 5, 6) and f_['soort'] == 'getal uit de vraag': f_['tekst'] = _Z971
    PATCH.append((E03, n_, 'hint2', h2_, f'{R1B}: Z-#972 (les 367)'))
    PATCH.append((E03, n_, 'foutHints', fh_, f'{R1B}: Z-#972' + ('; Z-#971' if n_ in (4, 5, 6) else '') + ('; V-#971 voorwaardelijk (V-#970)' if n_ in (8, 11) else '')))

# ---- Build 18:04:11 (Overzicht: nieuwe opties E06 #1/#2 en V01, V-#970) ----
import re as _re2
def _items(doel, nro):
    try: its_ = _json.load(open(os.path.join(patch_lib.BASE, 'data', 'per_doel', f'{doel}.json'), encoding='utf-8'))['items']
    except Exception: return None
    return [i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == nro]
# V-#982 (les 373) + 18:04: E06 #2 de teller-optie zit nu in elk item ('7%' bij 7/20): regel 'fout = het deel zelf (als %)' (motor, Oef-#453) i.p.v. de
# letterlijke '21%'. De noemer-route ('40%') alleen zolang een item de noemer als optie heeft (voorwaardelijk, twee kanten op; regel = die optie).
E06 = 'G8-VERH-E06'
_TELLER = 'Dat is de teller met een procentteken erachter. Dat klopt alleen als de noemer honderd is. Reken de noemer eerst om naar honderd.'
_NOEMER = 'Dat is de noemer met een procentteken erachter. De noemer hoort bij honderd procent. Welk procent hoort dan bij de teller?'
_its062 = _items(E06, 2)
if _its062:
    _noem = []
    for x_ in _its062:
        m_ = _re2.search(r'(\d+)/(\d+)', x_['opgave'])
        if m_ and any(o_['tekst'].replace(' ', '') == f'{m_.group(2)}%' for o_ in x_['opties'] or []): _noem.append(f'{m_.group(2)}%')
    _l062 = [dict(f_) for f_ in huidig(8, E06, 2)]
    _tel = next(f_ for f_ in _l062 if f_['soort'] == 'getal uit de breuk')
    _tel.update(regel='fout = het deel zelf (als %)', tekst=_TELLER)
    _l062 = [f_ for f_ in _l062 if f_['soort'] != 'getal uit de breuk (noemer)']
    # De motorregel leest alleen een heel procent als antwoord ('35%'); bij een kommaprocent (21/40 = 52,5%) de teller-optie letterlijk
    # (eigen soort, zelfde tekst; voorwaardelijk: valt weg als zo'n item er niet meer is). Datapunt voor Overzicht (motor Oef-#453 ook bij '52,5%').
    _kp = []
    for x_ in _its062:
        m_ = _re2.search(r'(\d+)/(\d+)', x_['opgave'])
        if m_ and ',' in x_['antwoord'] and any(o_['tekst'].replace(' ', '') == f'{m_.group(1)}%' for o_ in x_['opties'] or []): _kp.append(f'{m_.group(1)}%')
    _l062 = [f_ for f_ in _l062 if f_['soort'] != 'getal uit de breuk (kommaprocent)']
    if _kp: _l062 = voeg_in(_l062, 'getal uit de breuk', [dict(_tel, soort='getal uit de breuk (kommaprocent)', regel=_kp[0])])
    if _noem: _l062 = voeg_in(_l062, 'getal uit de breuk', [dict(_tel, soort='getal uit de breuk (noemer)', regel=_noem[0], tekst=_NOEMER)])
    # ---- Ronde 1c (Oefeningen 8 okt ~18:40; Didactiek hercheck 18:20:30): V-#1000 + Z-#983, voorwaardelijk uit de data (#493-patroon) ----
    # V-#1000 (data Overzicht): in 4 items wordt de afleider ': 10' → '× 10' (350%, 260%, 550%, 720%). Zo'n optie krijgt een eigen regel vóór de CL
    # (die vangt alle 'nul-fout-tientallen'-sleutels), met een tekst die per item klopt: breuk kleiner dan één → minder dan honderd procent, en de
    # noemer past in honderd. Klopt dat niet voor elk item, dan de algemene tekst. Z-#983: de CL krijgt 'te klein' zolang al zijn sleutels antwoord : 10 zijn.
    def _pv(t):
        t = str(t).strip().replace(' ', '')
        return _F1c(t[:-1].replace(',', '.')) if _re2.fullmatch(r'\d+(?:,\d+)?%', t) else None
    from fractions import Fraction as _F1c
    _x10, _x10_waar, _klein = [], True, True
    for x_ in _its062:
        m_ = _re2.search(r'(\d+)/(\d+)', x_['opgave']); a_ = _pv(x_['antwoord'])
        if not m_ or a_ is None: continue
        t_, n_ = int(m_.group(1)), int(m_.group(2))
        for o_ in x_['opties'] or []:
            if _pv(o_['tekst']) == a_ * 10:
                _x10.append(o_['tekst']); _x10_waar = _x10_waar and t_ < n_ and a_ * 10 > 100 and 100 % n_ == 0
        dk_ = {d_['fout'] for d_ in x_['extraVelden'].get('claudeDenkfouten') or [] if d_.get('denkfout') == 'nul-fout-tientallen'}
        if any(_pv(k_) is None or (_pv(k_) * 10 != a_ and _pv(k_) != a_ * 10) for k_ in dk_): _klein = False
    _X10_SPEC = 'Dat is tien keer te groot. Een breuk kleiner dan één is minder dan honderd procent. Hoe vaak past de noemer in honderd?'
    _X10_ALG = 'Dat is tien keer te groot. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.'
    _CL_KLEIN = 'Dat is tien keer te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.'
    _CL_ALG = 'Dat is tien keer te groot of te klein. Reken de noemer om naar honderd, en doe met de teller precies hetzelfde.'
    _cl10 = next(f_ for f_ in _l062 if f_['soort'] == 'tien keer ernaast')
    _cl10['tekst'] = _CL_KLEIN if _klein else _CL_ALG
    _l062 = [f_ for f_ in _l062 if not f_['soort'].startswith('tien keer te groot')]
    if _x10:   # de motor leest 'fout = antwoord × 10' niet bij een procent-antwoord (WARN ONLEESBAAR): per optie een letterlijke regel (G8-2), eigen soort
        _l062 = voeg_in(_l062, 'getal uit de breuk', [{'bron': 'nieuw', 'soort': f'tien keer te groot ({o_})', 'claudeDenkfout': None, 'regel': o_,
                                                     'tekst': _X10_SPEC if _x10_waar else _X10_ALG, 'tekstSterker': _cl10['tekstSterker']} for o_ in sorted(set(_x10), key=lambda t: _pv(t))])
    PATCH.append((E06, 2, 'foutHints', _l062, f"{R1B}: V-#982 (les 373); teller via de motor (build 18:04, elk item){'; kommaprocent letterlijk ' + _kp[0] if _kp else ''}; noemer-route {'regel ' + _noem[0] if _noem else 'weg (geen noemer-optie meer)'}; 1c: × 10 {('regel ' + ', '.join(_x10)) if _x10 else 'geen optie'}, CL {'te klein' if _klein else 'te groot of te klein'}"))
# E06 #1 H2 (les 264, build 18:04: 0,02 → 2%): 'twee plekken' verklapt het antwoord 2; ook in de laag 2 van elke fout-hint.
_H2_061o = 'de komma schuift twee plekken naar rechts.'
_H2_061n = 'de komma schuift dan naar rechts, één plek voor elke nul van honderd.'
PATCH.append((E06, 1, 'hint2', huidig(8, E06, 1, 'hint2').replace(_H2_061o, _H2_061n), f'{R1B}: les 264 (build 18:04, item 004)'))
_l061 = [dict(f_) for f_ in huidig(8, E06, 1)]
for f_ in _l061:
    if f_.get('tekstSterker'): f_['tekstSterker'] = f_['tekstSterker'].replace(_H2_061o, _H2_061n)
PATCH.append((E06, 1, 'foutHints', _l061, f'{R1B}: les 264, laag 2 = H2'))
# V01 #1 (build 18:04: '60 van de 200' → opties '60 procent' en '3 procent'): letterlijke regels uit de data (het deel; antwoord : 10), niet meer vast.
V01 = 'G8-VERH-V01'
_itsv = _items(V01, 1)
if _itsv:
    x_ = _itsv[0]; m_ = _re2.search(r'(\d+) van de (\d+)', x_['opgave']); a_ = _re2.match(r'(\d+)', x_['antwoord'])
    if m_ and a_:
        a_ = int(a_.group(1)); tien_ = f'{a_ // 10} procent' if a_ % 10 == 0 else f"{str(a_ / 10).replace('.', ',')} procent"
        _lv = [dict(f_) for f_ in huidig(8, V01, 1)]
        for f_ in _lv:
            if f_['soort'] == 'aantal als procent': f_['regel'] = f'{m_.group(1)} procent'
            if f_['soort'] == 'tien keer te klein':
                f_['regel'] = tien_; f_['tekst'] = 'Dat is tien keer te klein. Het hele aantal is honderd procent. Welk procent hoort dan bij het deel?'
        PATCH.append((V01, 1, 'foutHints', _lv, f'{R1B}: regels uit de data (build 18:04); tekst tien keer te klein zonder \'hoe vaak past\' (200 : 60 is geen heel getal)'))

# ---------- Ronde 1d (Oefeningen 8 okt ~19:05; Oef-#1014/#1015, Z-#1022, Overzicht punt 7): één hint-entry per samengevoegde kop (G8_KOP1014) ----------
# Met G8_KOP1014=1 vallen de entries van een groep op één kop; sync_hint_keys voegt nooit stil samen (#30) en apply_hints stopt. Voorwaardelijk uit de
# data (gemapt.json, fase 1), twee kanten op:
#  - één kop voor de hele groep: de andere entries weg (hun teksten zijn gelijk aan die van de blijver, nagerekend per item in bN/check); de blijver
#    krijgt de samengevoegde kop als somtypeOrigineel (geen 'kopGewijzigd'); patches op de weggehaalde entries vallen weg;
#  - weer gesplitst (vlag uit): de weggehaalde entries komen terug als kopie van de blijver (nieuwEntry, somtypeOrigineel uit bevroren v1), en elke
#    patch op de blijver geldt dan ook voor hen; de blijver krijgt zijn bevroren kop terug.
def _kop1014(nb, groepen):
    import json as _j, copy as _c, collections as _co
    why = 'Ronde 1d (Oefeningen): Oef-#1014/#1015, één entry per samengevoegde kop (G8_KOP1014)'
    try: gem_ = _j.load(open(os.path.join(patch_lib.BASE, 'data', 'gemapt.json'), encoding='utf-8'))['items']
    except Exception: return
    snap_ = _j.load(open(os.path.join(patch_lib.BASE, 'bevroren', 'somtype_nr_v1.json'), encoding='utf-8'))['sleutels']
    B_ = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _j.load(open(os.path.join(patch_lib.BASE, 'hints', f'batch{nb}.json'), encoding='utf-8'))['somtypen']}
    voor_, na_, weg_, dup_ = [], [], set(), _co.defaultdict(list)
    for doel_, surv_, rest_ in groepen:
        if (doel_, surv_) not in B_: print(f'LET OP ronde 1d: blijver {doel_} #{surv_} ontbreekt'); continue
        kv_ = _co.defaultdict(set)
        for it_ in gem_:
            m_ = it_['merge']
            if m_.get('status') == 'gemapt' and m_.get('doel') == doel_: kv_[m_.get('somtypeNrOrigineel')].add(m_.get('somtype'))
        koppen_ = set().union(*(kv_[n_] for n_ in [surv_] + rest_))
        if len(koppen_) == 1:
            kop_ = next(iter(koppen_))
            for n_ in rest_:
                weg_.add((doel_, n_))
                if (doel_, n_) in B_: na_.append((doel_, n_, 'weg', None, why))
            if B_[(doel_, surv_)]['somtypeOrigineel'] != kop_:
                na_ += [(doel_, surv_, 'somtypeOrigineel', kop_, why), (doel_, surv_, 'somtype', kop_, why)]
        else:
            orig_ = snap_[f'{doel_}#{surv_}']['somtypeOrigineel']
            if B_[(doel_, surv_)]['somtypeOrigineel'] != orig_:
                na_ += [(doel_, surv_, 'somtypeOrigineel', orig_, why), (doel_, surv_, 'somtype', orig_, why)]
            for n_ in rest_:
                if (doel_, n_) not in B_:
                    o_ = snap_[f'{doel_}#{n_}']['somtypeOrigineel']
                    basis_ = {k_: _c.deepcopy(B_[(doel_, surv_)][k_]) for k_ in ('hint1', 'hint2', 'ouderzin', 'foutHints', 'claudeVervangen') if k_ in B_[(doel_, surv_)]}
                    voor_.append((doel_, n_, 'nieuwEntry', dict(doel=doel_, nrOrigineel=n_, somtypeOrigineel=o_, somtype=o_, **basis_), why))
                dup_[(doel_, surv_)].append(n_)
    uit_ = list(voor_)
    for p_ in PATCH:
        if (p_[0], p_[1]) in weg_ and p_[2] != 'weg': continue
        uit_.append(p_)
        if p_[2] not in ('weg', 'nieuwEntry'):
            for n_ in dup_.get((p_[0], p_[1]), []): uit_.append((p_[0], n_, _c.deepcopy(p_[2]), _c.deepcopy(p_[3]), p_[4]))
    PATCH[:] = uit_ + na_
_kop1014(8, [('G8-VERH-E04', 1, [6])])

if __name__ == '__main__':
    patch_lib.run(8, PATCH)
