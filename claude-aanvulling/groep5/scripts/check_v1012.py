#!/usr/bin/env python3
"""V-#1012 (review-r13, G5): nagespeeld op een toegepaste G5-kopie (per_doel na apply_hints).
- 'dubbele punt' in een kindtekst (hint, sterkereHint, algemeneFoutHint, foutHints uitleg/uitlegSterker) van een item zonder digitaleKlok = FAIL (les 387).
- MEET-E06 'zestig minuten of meer': de L1 is de V-#1012-tekst (≤ 45 woorden); elke sleutel is de overloop van het antwoord (uur − 1, minuten + 60, ≥ 60);
  de sleutel staat in de waarden van zijn regel. Voorwaardelijk (motor Overzicht, _klok_vormen bij minuten ≥ 60): dan horen '12.85 uur', '12.85' en '12:85'
  alle drie in de waarden (FAIL); zonder die motorwijziging INFO.
- les 234: snapshot van de sleutels van deze items (SNAP=1 schrijft hem). MUT=<naam> voor een mutant.
Gebruik: python3 check_v1012.py <g5-map>"""
import json, re, sys, os, glob
G5 = sys.argv[1]; MUT = os.environ.get('MUT'); F, W, I = [], [], []
sys.path.insert(0, f'{G5}/scripts'); import fout_regels as FR
NIEUW = 'Achter de punt staan de minuten. Dat kunnen er niet zestig of meer zijn: een uur heeft zestig minuten. Dan komt er een uur bij.'
MOTOR = len(FR._klok_vormen('12:85')) == 3
ITEMS = [x for p in sorted(glob.glob(f'{G5}/data/per_doel/*.json')) for x in json.load(open(p, encoding='utf-8'))['items']]
def IT(nr): return next(x for x in ITEMS if x['doelId'] == 'G5-MEET-E06' and x['nr'] == nr)
def FH(x, soort): return next(f for f in x['foutHints'] if f['soort'] == soort)
def RG(x, soort): return next(r for r in x.get('foutRegels') or [] if r.get('soort') == soort)
# ---- mutanten ----
if MUT == 'M_dubbel': FH(IT('1200'), 'zestig minuten of meer')['uitleg'] = 'Zestig minuten of meer kan niet achter de dubbele punt. Een uur heeft zestig minuten: dan komt er een uur bij.'
if MUT == 'M_dubbelH': IT('1204')['hint'] = 'Achter de dubbele punt staan de minuten.'
if MUT == 'M_punt': FH(IT('1200'), 'zestig minuten of meer')['fout'] = '12.85'; RG(IT('1200'), 'zestig minuten of meer')['match']['waarden'] = ['12:85']   # puntvorm buiten de waarden
if MUT == 'M_punt3': RG(IT('1201'), 'zestig minuten of meer')['match']['waarden'] = ['16:80'] if MOTOR else ['16:80', '16.80']   # motor aan: vorm ontbreekt; uit: niet-motorvorm
if MUT == 'M_waar': f_ = FH(IT('1203'), 'zestig minuten of meer'); f_['fout'] = '17:65'; RG(IT('1203'), 'zestig minuten of meer')['match']['waarden'] = FR._klok_vormen('17:65') if MOTOR else ['17:65']
if MUT == 'M_45': FH(IT('1205'), 'zestig minuten of meer')['uitleg'] = NIEUW + ' Tel nog eens goed.' * 10
if MUT == 'M_hmm': RG(next(x for x in ITEMS if x['doelId'] == 'G5-VBN-E03' and x['nr'] == '014'), 'één stap ernaast (per item)')['match']['waarden'].remove('8.45')
if MUT == 'M_afl': IT('1206')['extraVelden']['claudeDenkfouten'][0]['fout'] = '8:61'
# ---- 'dubbele punt' in kindteksten ----
VELDEN = ('hint', 'sterkereHint', 'algemeneFoutHint', 'foutHintsTekst', 'optiesTekst', 'sterkereHintMetPlaatje', 'appMoetTonen')   # Z-#1018: ook de velden die kloktijd_check overslaat
for x in ITEMS:
    if x.get('digitaleKlok'): continue
    tt = [(k, x.get(k)) for k in VELDEN] + [(f"L1 {f.get('soort')}", f.get('uitleg')) for f in x.get('foutHints') or []] + [(f"L2 {f.get('soort')}", f.get('uitlegSterker')) for f in x.get('foutHints') or []]
    for k, t in tt:
        if isinstance(t, str) and re.search(r'dubbele ?punt', t, re.I): F.append(f"V-#1012 {x['doelId']} {x['nr']} [{k}]: 'dubbele punt' zonder digitaleKlok: {t[:90]}")
# ---- elke h:mm-waarde ook in de '.'-vorm (review §6 V-#1012-guard), items met de puntvorm, zonder digitaleKlok ----
nhm = 0
for x in ITEMS:
    if x.get('digitaleKlok') or not FR._klok_heeft_punt(x): continue
    for r in x.get('foutRegels') or []:
        wd = (r.get('match') or {}).get('waarden') or []
        for w in wd:
            m = re.fullmatch(r'(\d{1,2}):(\d{2})', w) if isinstance(w, str) else None
            if not m: continue
            nhm += 1
            if int(m.group(2)) >= 60 and not MOTOR: continue      # zonder de motorwijziging blijft de overloop ':'-only (INFO hieronder)
            if f'{m.group(1)}.{m.group(2)}' not in wd: F.append(f"V-#1012 hmm {x['doelId']} {x['nr']} [{r.get('soort')}]: '{w}' zonder de '.'-vorm in de waarden {wd}")
I.append(f'INFO h:mm-waarden bij puntvorm-items: {nhm}')
# ---- MEET-E06 overloop ----
SNAPD = {}; n = 0
for x in ITEMS:
    if x['doelId'] != 'G5-MEET-E06': continue
    for f in x.get('foutHints') or []:
        if f.get('soort') != 'zestig minuten of meer': continue
        n += 1; nid = f"MEET-E06 {x['nr']}"; SNAPD.setdefault(x['nr'], []).append(f['fout'])
        if f['uitleg'] != NIEUW: F.append(f"V-#1012 {nid}: L1 is niet de nieuwe tekst: {f['uitleg'][:80]}")
        if len(f['uitleg'].split()) > 45: F.append(f"V-#764 {nid}: L1 {len(f['uitleg'].split())} woorden")
        ma = re.fullmatch(r'(\d{1,2})\.(\d{2}) uur', x['antwoord']); mk = re.fullmatch(r'(\d{1,2})[:.](\d{2})(?: uur)?', f['fout'].strip())
        if not ma or not mk: F.append(f"V-#1012 {nid}: antwoord {x['antwoord']!r} of sleutel {f['fout']!r} niet te lezen"); continue
        if not (int(mk.group(2)) >= 60 and int(mk.group(1)) == int(ma.group(1)) - 1 and int(mk.group(2)) == int(ma.group(2)) + 60):
            F.append(f"V-#1012 {nid}: sleutel {f['fout']!r} is niet de overloop van {x['antwoord']!r} (uur − 1, minuten + 60): 'Dan komt er een uur bij' klopt niet")
        try: r = RG(x, 'zestig minuten of meer')
        except StopIteration: F.append(f'V-#1012 {nid}: geen foutRegel'); continue
        wd = set((r.get('match') or {}).get('waarden') or [])
        if f['fout'] not in wd: F.append(f"V-#1012 vorm {nid}: sleutel {f['fout']!r} staat niet in de waarden van zijn regel {sorted(wd)}")
        h_, m_ = mk.groups(); drie = {f'{h_}.{m_} uur', f'{h_}.{m_}', f'{h_}:{m_}'}
        if MOTOR and not drie <= wd: F.append(f"V-#1012 vorm {nid}: motor maakt drie vormen, regel heeft {sorted(wd)} (mist {sorted(drie - wd)})")
        elif not MOTOR and (wd & {f'{h_}.{m_} uur', f'{h_}.{m_}'}): F.append(f"V-#1012 vorm {nid}: puntvorm in de waarden {sorted(wd)} zonder de motorwijziging (andere bron?)")
        elif not MOTOR: I.append(f"INFO {nid}: wacht op de motor (_klok_vormen bij minuten ≥ 60): waarden {sorted(wd)}")
I.append(f'INFO motor _klok_vormen bij minuten ≥ 60: {"aan" if MOTOR else "uit"}; {n} sleutels zestig minuten of meer')
SNAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snap_v1012.json')
SNAPD = {k: sorted(v) for k, v in SNAPD.items()}
for x in ITEMS:
    if x['doelId'] == 'G5-MEET-E06' and x['merge']['somtypeNrOrigineel'] in (21, 23):
        SNAPD.setdefault(x['nr'] + ' claude', sorted(d['fout'] for d in x['extraVelden'].get('claudeDenkfouten') or []))
if os.environ.get('SNAP') == '1': json.dump(SNAPD, open(SNAP, 'w'), indent=0, sort_keys=True, ensure_ascii=False); I.append(f'INFO les 234: snapshot geschreven ({len(SNAPD)})')
elif os.path.exists(SNAP):
    oud = json.load(open(SNAP))
    for k in sorted(set(oud) | set(SNAPD)):
        if oud.get(k) != SNAPD.get(k): F.append(f'les 234 {k}: sleutels veranderd ({oud.get(k)} → {SNAPD.get(k)}): nalopen, dan SNAP=1')
else: W.append('les 234: geen snapshot')
for m in I: print(m)
for m in W: print('WARN', m)
for m in F: print('FAIL', m)
print(f'G5 V-#1012: {len(ITEMS)} items · {n} overloop-sleutels · FAIL {len(F)} · WARN {len(W)}')
sys.exit(1 if F else 0)
