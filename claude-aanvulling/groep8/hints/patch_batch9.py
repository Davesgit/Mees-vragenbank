#!/usr/bin/env python3
"""Patcht hints/batch9.json IN PLACE (G8 batch 9: VERH-E05 #1–#21, VBN-V01 #1–#5), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch9.json. Na een sync of rebuild nooit make_batch9.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch9.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~18:40): V01 #1 012 (2, 2) had geen sleutel (omwisselen = dezelfde stip; check_hints 'geen fout-hint') ----------
# Regel 'een getal uit de vraag': de sleutel is één getal zonder komma = een stip op de lijn van nul (de data schrijft (x, 0) als 'x', Oef-#1019).
# Tekst waar voor elke waarde: (x, 0), (y, 0) en (0, 0) liggen alle op de lijn van nul. Idempotent (voeg_in op soort).
_V01 = 'G8-VBN-V01'
_fh = huidig(9, _V01, 1)
_nieuw = {'bron': 'nieuw', 'soort': 'stip op de lijn van nul', 'claudeDenkfout': None, 'regel': 'fout = een getal uit de vraag',
          'tekst': 'Die stip ligt op de lijn van nul. Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.',
          'tekstSterker': next(f_ for f_ in _fh if f_['soort'] == 'andere fout')['tekstSterker']}
PATCH.append((_V01, 1, 'foutHints', voeg_in(_fh, 'omgewisseld', [_nieuw]), "Ronde 1b (Oefeningen): 012 (2, 2) kreeg geen fout-hint; 'een getal uit de vraag' = stip op de lijn van nul"))

# ---------- Ronde 1c (Oefeningen 8 okt ~18:50; Didactiek review b9 18:45, V-#1022–#1025): voorwaardelijk uit de data (de build van Overzicht
# met V-#1020/#1021/#1023/#1025/#1026 komt in dezelfde build). Alles twee kanten op: op de oude data blijft de oude stand (of de tekst die voor
# beide klopt), op de nieuwe data de nieuwe. Leest per_doel (fase 3).
import json as _json, re as _re
from fractions import Fraction as _F
E05 = 'G8-VERH-E05'
R1C = 'Ronde 1c (Oefeningen, review b9)'
def _items(doel, nro):
    try: its_ = _json.load(open(os.path.join(patch_lib.BASE, 'data', 'per_doel', f'{doel}.json'), encoding='utf-8'))['items']
    except Exception: return None
    return [i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == nro]
_B9 = {(s_['doel'], s_['nrOrigineel']) for s_ in _json.load(open(os.path.join(patch_lib.BASE, 'hints', 'batch9.json'), encoding='utf-8'))['somtypen']}
# V-#1024 (les 301, twijfel 2): de CL van E05 #1/#18 vangt twee waarden: het verschil in euro én het procent van de nieuwe prijs. «nog geen procent»
# klopt alleen voor de eerste. Eén tekst die voor beide waar is (guard in b9/check: 'nog geen procent' alleen als alle sleutels het verschil zijn).
_T1024 = 'Vergelijk met de oude prijs: die is honderd procent. Hoeveel euro komt erbij, en hoeveel procent van de oude prijs is dat?'
for _n in (1, 18):
    if (E05, _n) in _B9:     # V-#1020 kan #18 met #1 laten samenvallen: dan geen entry meer nodig (patch_lib asserteert er één)
        PATCH.append((E05, _n, ('fh', 'nog geen procent van de oude prijs', {'tekst': _T1024}), None, f'{R1C}: V-#1024 één tekst die klopt voor het verschil in euro én voor de nieuwe prijs als basis'))
# V-#1023 (data Overzicht; les 372): E05 #21 054 wordt 60 → 48 broden, 20 procent, opties 12 / 20 / 25 procent. De letterlijke regels volgen de data:
# de optie = het verschil als procent, en de optie = het procent van het nieuwe aantal (afgerond). Staat zo'n optie er niet, dan blijft de regel staan.
_its21 = _items(E05, 21)
if _its21 and (E05, 21) in _B9:
    _GW = {'tien': 10, 'twintig': 20, 'dertig': 30, 'veertig': 40, 'vijftig': 50, 'zestig': 60, 'zeventig': 70, 'tachtig': 80, 'negentig': 90, 'honderd': 100}
    _r21 = {}
    for x_ in _its21:
        m_ = _re.search(r'verkoopt in (?:week \d+|de \w+ week) (\w+) broden en in (?:week \d+|de \w+ week) (\w+) broden', x_['opgave'])
        if not m_: continue
        o_, n_ = (int(g_) if g_.isdigit() else _GW.get(g_) for g_ in m_.groups())
        if not o_ or not n_ or o_ <= n_: continue
        d_ = o_ - n_; nb_ = _F(d_ * 100, n_)
        for op_ in x_.get('opties') or []:
            t_ = op_['tekst']; mm_ = _re.fullmatch(r'(\d+) procent', t_.strip())
            if not mm_ or t_ == x_['antwoord']: continue
            if int(mm_.group(1)) == d_: _r21.setdefault('verschil als procent', set()).add(t_)
            elif abs(int(mm_.group(1)) - nb_) < 1: _r21.setdefault('nieuwe aantal als basis', set()).add(t_)
    for so_, ts_ in sorted(_r21.items()):
        if len(ts_) == 1: PATCH.append((E05, 21, ('fh', so_, {'regel': next(iter(ts_))}), None, f'{R1C}: V-#1023 letterlijke regel volgt de optie van de data'))
# V-#1025 (data Overzicht; Oef-#1019): het antwoord bij (x, 0) wordt '(x,0)' i.p.v. 'x'. Dan is een sleutel met één getal geen stip op de lijn van
# nul meer, maar één getal waar er twee horen. Voorwaardelijk: pas als geen enkel (x, 0)-item nog 'x' als antwoord heeft. 'Lijn van nul' met
# sleutels 'x,0' en '0,y' kan de motor nog niet maken (letterlijke regels werken alleen op opties): datapunt Oef-#1023.
# Vooraan, vóór de CL 'omgewisseld': die heeft label None en pakt dus elke Claude-sleutel (ook Claudes nieuwe '1'), en zijn tekst klopt daar niet.
_V01 = 'G8-VBN-V01'
_its1 = _items(_V01, 1)
if _its1 and (_V01, 1) in _B9:
    _oud1 = any((m_ := _re.search(r'\((\d+), 0\)', x_['opgave'])) and x_['antwoord'].strip() == m_.group(1) for x_ in _its1)
    _fh1 = huidig(9, _V01, 1); _L0 = next((f_ for f_ in _fh1 if f_['soort'] in ('stip op de lijn van nul', 'maar één getal')), None) or dict(_nieuw)   # eerste run: ronde 1b staat nog niet in het bestand
    if _L0 is not None:
        _L0 = dict(_L0)
        if _oud1: _L0.update(soort='stip op de lijn van nul', tekst='Die stip ligt op de lijn van nul. Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.')
        else: _L0.update(soort='maar één getal', tekst='Dat is maar één getal. Een stip heeft er twee: eerst hoe ver je opzij gaat, dan hoe ver omhoog.')
        _fh1 = [f_ for f_ in _fh1 if f_['soort'] not in ('stip op de lijn van nul', 'maar één getal')]
        PATCH.append((_V01, 1, 'foutHints', voeg_in(_fh1, None, [_L0]), f'{R1C}: V-#1025 sleutel met één getal: ' + ('lijn van nul (oude notatie)' if _oud1 else "'maar één getal' (antwoord '(x,0)')")))
# Z-#1023 (data Overzicht): V01 #2 013 krijgt misschien andere afleiders. De letterlijke regels volgen de opties: een optie met de andere richting en
# hetzelfde getal = 'omhoog in plaats van omlaag'; een optie met het verschil van een ander stuk van de lijn = 'verschil van een ander stuk'.
_its2 = _items(_V01, 2)
if _its2 and (_V01, 2) in _B9:
    _r2 = {}
    for x_ in _its2:
        pt_ = dict((int(h_), int(t_)) for h_, t_ in _re.findall(r'\((\d+)\.00 uur, (-?\d+) °C\)', (x_.get('visual') or {}).get('toelichting') or ''))
        m_ = _re.search(r'tussen (\d+)\.00 uur en (\d+)\.00 uur\?', x_['opgave'])
        if not m_ or int(m_.group(1)) not in pt_ or int(m_.group(2)) not in pt_: continue
        dv_ = pt_[int(m_.group(2))] - pt_[int(m_.group(1))]; hs_ = sorted(pt_)
        ander_ = ({abs(pt_[b_] - pt_[a_]) for a_, b_ in zip(hs_, hs_[1:])} | {abs(pt_[hs_[-1]] - pt_[hs_[0]])}) - {abs(dv_)}
        for op_ in x_.get('opties') or []:
            mm_ = _re.fullmatch(r'De temperatuur (stijgt|daalt) met (\d+) graden', op_['tekst'])
            if not mm_ or op_['tekst'] == x_['antwoord']: continue
            w_ = int(mm_.group(2)) * (1 if mm_.group(1) == 'stijgt' else -1)
            if w_ == -dv_: _r2.setdefault('omhoog in plaats van omlaag', set()).add(op_['tekst'])
            elif abs(w_) in ander_: _r2.setdefault('verschil van een ander stuk', set()).add(op_['tekst'])
    for so_, ts_ in sorted(_r2.items()):
        if len(ts_) == 1: PATCH.append((_V01, 2, ('fh', so_, {'regel': next(iter(ts_))}), None, f'{R1C}: Z-#1023 letterlijke regel volgt de optie van de data'))

# ---------- Ronde 1e (Oefeningen 8 okt ~19:20; Oef-#1023, Didactiek V-#1031, les 318/396) ----------
# V01 #1 rooster. (1) Volgorde nu al: 'omgewisseld' (Claudes sleutel 'y,x') vóór 'maar één getal'. 'maar één getal' pakt via de motor ook een
# 'a,0'-sleutel als het getal a (Oef-#440, KOMMA437): live kreeg 009 de omgewisselde stip '1,0' «Dat is maar één getal» (V-#1031). 'y,x' valt nooit
# samen met een los getal, dus zo krijgt 'maar één getal' alleen nog losse getallen. Alleen als Claude in V01 #1 geen losse-getal-sleutel heeft
# (de CL heeft label None en pakt elke Claude-sleutel); anders blijft de volgorde van ronde 1c.
# (2) De goedgekeurde tekst 'lijn van nul' op de motorregel 'fout = stip op de lijn van nul' (Oef-#1023: sleutels 'x,0' en '0,y', nooit de goede
# stip) gaat pas aan als de motor zelf een stip-sleutel als stip leest (V-#1031 bij Overzicht). Signaal = de motor zelf: op een echt V01 #1-item
# met een proef-entry ['een getal uit de vraag', 'stip op de lijn van nul'] moet 'x,0' onder de stipregel komen en niet onder 'een getal'.
# Dan staat 'lijn van nul' vooraan (meest precieze ware tekst eerst, les 318). Zonder dat signaal, zonder de motorregel of op de oude data: uit.
R1E = 'Ronde 1e (Oefeningen, Oef-#1023/V-#1031)'
def _motor_leest_stip(its_):
    try:
        import importlib, copy as _cp
        sys.dont_write_bytecode = True; sys.path.insert(0, os.path.join(patch_lib.BASE, 'scripts'))
        FR_ = importlib.import_module('fout_regels')
        if 'fout = stip op de lijn van nul' not in open(FR_.__file__, encoding='utf-8').read(): return False
        FR_.KOMMA437 = True; FR_.NEG494 = True      # zoals scripts/apply_hints.py (G7/G8)
        T_ = lambda s, r: {'bron': 'nieuw', 'soort': s, 'claudeDenkfout': None, 'regel': r, 'tekst': 'proef', 'tekstSterker': 'proef'}
        getest_ = 0
        for x_ in its_:
            m_ = _re.fullmatch(r'\((\d+), ?(\d+)\)', x_['antwoord'].strip())
            if not m_ or m_.group(1) == '0' or m_.group(2) == '0': continue
            it_ = _cp.deepcopy(x_)
            FR_.pas_toe(it_, {'foutHints': [T_('getal', 'fout = een getal uit de vraag'), T_('stip', 'fout = stip op de lijn van nul'), T_('andere fout', 'andere fout')], 'claudeVervangen': []})
            so_ = {f_['fout'].replace(' ', '').strip('()'): f_['soort'] for f_ in it_['foutHints'] if f_['fout'].strip('() ') in (f'{m_.group(1)},0', f'{m_.group(1)}, 0')}
            if so_.get(f'{m_.group(1)},0') != 'stip': return False
            getest_ += 1
        return getest_ > 0
    except Exception:
        return False
if _its1 and (_V01, 1) in _B9 and not _oud1 and all(_re.fullmatch(r'\(\d+, ?\d+\)', x_['antwoord'].strip()) for x_ in _its1):
    _fhE = huidig(9, _V01, 1)
    _lijn_aan = _motor_leest_stip(_its1)
    _st2 = next((f_ for f_ in _fhE if f_['soort'] == 'andere fout'), None)
    _lijn0 = {'bron': 'nieuw', 'soort': 'stip op de lijn van nul', 'claudeDenkfout': None, 'regel': 'fout = stip op de lijn van nul',
              'tekst': 'Die stip ligt op de lijn van nul. Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.'}
    if _st2 and _st2.get('tekstSterker'): _lijn0['tekstSterker'] = _st2['tekstSterker']
    _een = next((f_ for f_ in _fhE if f_['soort'] in ('maar één getal', 'stip op de lijn van nul') and f_['regel'].startswith('fout = een getal uit de vraag')), None)
    _een = dict(_een) if _een else None
    if _een: _een.update(soort='maar één getal', tekst='Dat is maar één getal. Een stip heeft er twee: eerst hoe ver je opzij gaat, dan hoe ver omhoog.')
    _rest = [f_ for f_ in _fhE if f_['soort'] not in ('stip op de lijn van nul', 'maar één getal')]
    _cl_los = any(',' not in str(k_.get('fout', '')) for x_ in _its1 for k_ in (x_.get('extraVelden') or {}).get('claudeFoutHints') or [])
    _omg = [f_ for f_ in _rest if f_['soort'] == 'omgewisseld']; _anders = [f_ for f_ in _rest if f_['soort'] != 'omgewisseld']
    _midden = ([_een] if _een else []) + _omg if _cl_los else _omg + ([_een] if _een else [])
    PATCH.append((_V01, 1, 'foutHints', ([_lijn0] if _lijn_aan else []) + _midden + _anders,
                  f"{R1E}: " + ("'lijn van nul' (x,0 / 0,y) vooraan, de motor leest een stip als stip; " if _lijn_aan else "'lijn van nul' nog uit (de motor leest 'x,0' nog als getal, V-#1031); ")
                  + ("'maar één getal' blijft vóór 'omgewisseld' (Claude heeft een losse-getal-sleutel)" if _cl_los else "'omgewisseld' vóór 'maar één getal' (V-#1031: 009 '1,0')")))

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
# ---------- Ronde 1f (Oefeningen 8 okt ~20:25; Z-#1062, Didactiek keuze A met aanpassing, les 318) ----------
# V01 #1: de tekst op de motorregel 'fout = stip op de lijn van nul' noemt geen 'vóór/na de komma' meer (een kind leest '6,0' anders als kommagetal).
# Voorwaarde per sleutel: de stip van het kind heeft een 0 waar het antwoord geen 0 heeft. De motorregel geeft alleen 'x,0' en '0,y' (nooit de goede
# stip), dus dat geldt per constructie; de patch rekent het per item na en zet de tekst alleen als het voor elke sleutel klopt. Anders blijft de
# entry zoals ronde 1e (de sleutel valt dan naar de volgende regel, volgorde les 318). Alleen op de entry met die motorregel (ronde 1e, 'lijn aan');
# de oude stand (regel 'een getal uit de vraag', sleutels zonder komma) houdt zijn tekst. Gaat vanzelf mee voor 003–011 als V-#1030 live gaat.
R1F = 'Ronde 1f (Oefeningen, Z-#1062)'
T1062 = 'Bij jouw stip staat een nul waar een ander getal hoort. Ga eerst opzij zoveel als het eerste getal. Ga dan omhoog zoveel als het tweede getal.'
def _nul_klopt(its_):
    for x_ in its_:
        m_ = _re.fullmatch(r'\((\d+), ?(\d+)\)', x_['antwoord'].strip())
        if not m_: return False
        a_ = (int(m_.group(1)), int(m_.group(2)))
        for k_ in ((a_[0], 0), (0, a_[1])):
            if k_ == a_: continue
            if not any(k_[i_] == 0 and a_[i_] != 0 for i_ in (0, 1)): return False
    return bool(its_)
_laatst = next((p_[3] for p_ in reversed(PATCH) if p_[:3] == (_V01, 1, 'foutHints')), None)
_fhF = _json.loads(_json.dumps(_laatst)) if _laatst is not None else (huidig(9, _V01, 1) if (_V01, 1) in _B9 else [])
_l0 = [f_ for f_ in _fhF if f_['soort'] == 'stip op de lijn van nul' and f_['regel'].startswith('fout = stip op de lijn van nul')]
if _l0 and _its1 and _nul_klopt(_its1) and _l0[0]['tekst'] != T1062:
    _l0[0]['tekst'] = T1062
    PATCH.append((_V01, 1, 'foutHints', _fhF, f"{R1F}: 'lijn van nul' zonder 'vóór/na de komma'; per sleutel nagerekend: een 0 waar het antwoord geen 0 heeft"))
elif _l0 and _its1 and _l0[0]['tekst'] == T1062 and _laatst is not None:
    PATCH.append((_V01, 1, 'foutHints', _fhF, f'{R1F}: tekst staat er al'))

# ---------- Ronde 1g (Oefeningen 8 okt ~20:35; Oef-#1036, Didactiek ja 20:28) ----------
# V01 #1: in een stip met komma '(6, 1)' leest 'het getal vóór/na de komma' als kommagetal. Overal in de entry (hint2, L1, L2): 'het eerste getal' /
# 'het tweede getal'. Mag alleen bij coördinaten (de volgorde in een stip ligt vast; les 193-uitzondering alleen daar, guard in b9/check).
# Voorwaardelijk: alleen als elk item van V01 #1 een stip als antwoord heeft. Idempotent (vervangt alleen wat er nog staat).
R1G = 'Ronde 1g (Oefeningen, Oef-#1036)'
_KOMMA1036 = [('Het getal vóór de komma', 'Het eerste getal'), ('het getal vóór de komma', 'het eerste getal'),
              ('Het getal na de komma', 'Het tweede getal'), ('het getal na de komma', 'het tweede getal')]
def _zonder_komma(t_):
    for o_, n_ in _KOMMA1036: t_ = t_.replace(o_, n_)
    return t_
if _its1 and (_V01, 1) in _B9 and all(_re.fullmatch(r'\(\d+, ?\d+\)', x_['antwoord'].strip()) for x_ in _its1):
    _lG = next((p_[3] for p_ in reversed(PATCH) if p_[:3] == (_V01, 1, 'foutHints')), None)
    _fhG = _json.loads(_json.dumps(_lG)) if _lG is not None else huidig(9, _V01, 1)
    _nwG = [dict(f_, **{k_: _zonder_komma(f_[k_]) for k_ in ('tekst', 'tekstSterker') if isinstance(f_.get(k_), str)}) for f_ in _fhG]
    if _nwG != _fhG or _lG is not None: PATCH.append((_V01, 1, 'foutHints', _nwG, f"{R1G}: L1/L2 'eerste/tweede getal' in plaats van 'getal vóór/na de komma'"))
    _h2G = next((p_[3] for p_ in reversed(PATCH) if p_[:3] == (_V01, 1, 'hint2')), None) or huidig(9, _V01, 1, 'hint2')
    if _zonder_komma(_h2G) != _h2G: PATCH.append((_V01, 1, 'hint2', _zonder_komma(_h2G), f"{R1G}: H2 'eerste/tweede getal' in plaats van 'getal vóór/na de komma'"))

# ---------- Ronde 1h (Oefeningen 8 okt ~20:40; Oef-#1036 stem, Didactiek 20:34) ----------
# V01 #1 'omgewisseld': de tekst spreekt het kind aan op zijn eigen stip. «Daar staan de twee getallen omgewisseld.» → «Bij jouw stip zijn de twee
# getallen omgewisseld.» Na 1g (eerste/tweede getal). Idempotent: vervangt alleen de oude openingszin; werkt op verse data (1g in dezelfde run)
# én op data waar 1g al gedraaid heeft.
R1H = 'Ronde 1h (Oefeningen, Oef-#1036 stem)'
T1036O = 'Bij jouw stip zijn de twee getallen omgewisseld. Het eerste getal gaat opzij, het tweede getal omhoog.'
def _stem1036(f_):
    if f_.get('soort') != 'omgewisseld' or not isinstance(f_.get('tekst'), str): return f_
    t_ = f_['tekst'].replace('Daar staan de twee getallen omgewisseld.', 'Bij jouw stip zijn de twee getallen omgewisseld.')
    return dict(f_, tekst=t_)
if _its1 and (_V01, 1) in _B9 and all(_re.fullmatch(r'\(\d+, ?\d+\)', x_['antwoord'].strip()) for x_ in _its1):
    _lH = next((p_[3] for p_ in reversed(PATCH) if p_[:3] == (_V01, 1, 'foutHints')), None)
    _fhH = _json.loads(_json.dumps(_lH)) if _lH is not None else huidig(9, _V01, 1)
    _nwH = [_stem1036(f_) for f_ in _fhH]
    if _nwH != _fhH or _lH is not None: PATCH.append((_V01, 1, 'foutHints', _nwH, f"{R1H}: 'omgewisseld' «Bij jouw stip zijn de twee getallen omgewisseld.»"))

_kop1014(9, [('G8-VERH-E05', 1, [18]), ('G8-VERH-E05', 2, [4, 20, 9, 10]), ('G8-VERH-E05', 5, [11, 6, 12, 7, 13, 14, 15, 16, 8, 17, 19])])

if __name__ == '__main__':
    patch_lib.run(9, PATCH)
