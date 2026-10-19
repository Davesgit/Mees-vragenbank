#!/usr/bin/env python3
"""Check V-#1145. [MUT=..] [SNAP=1] python3 check_v1145.py <basis>. Altijd FAIL N (totaal); exit 1 bij FAIL.
G5-GET-E07 #22 'nul vergeten': entry-tekst precies «Dat is te weinig. Tel de nullen van het ronde getal goed mee.», tekstSterker zoals in de basis;
per item: de sleutel is het antwoord gedeeld door tien (dus kleiner: 'te weinig' klopt) en de uitleg is die tekst; SNAP van alle foutHints van #22."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G); K = ('G5-GET-E07', 22)
T = 'Dat is te weinig. Tel de nullen van het ronde getal goed mee.'
TS = 'Reken eerst zonder de nullen. Zet daarna evenveel nullen achter je antwoord als het ronde getal heeft.'
ENT = next(s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if (s['doel'], s['nrOrigineel']) == K)
XS = I.get(K, [])
if MUT == 'M_methode': next(f for f in ENT['foutHints'] if f['soort'] == 'nul vergeten')['tekst'] = 'Dat is te weinig.'
if MUT == 'M_sterker': next(f for f in ENT['foutHints'] if f['soort'] == 'nul vergeten')['tekstSterker'] += ' Tel goed.'
if MUT == 'M_richting': h_ = next(h for h in XS[0]['foutHints'] if h['soort'] == 'nul vergeten'); h_['fout'] = str(int(XS[0]['antwoord']) * 10)
if MUT == 'M_item': h_ = next(h for h in XS[-1]['foutHints'] if h['soort'] == 'nul vergeten'); h_['uitleg'] = 'Tel de nullen van het ronde getal goed mee.'
fs = [f for f in ENT['foutHints'] if f['soort'] == 'nul vergeten']
if len(fs) != 1 or fs[0]['tekst'] != T: F.append(f"entry G5-GET-E07 #22 'nul vergeten': {[f['tekst'] for f in fs]}")
elif fs[0].get('tekstSterker') != TS: F.append(f"sterker G5-GET-E07 #22: {fs[0].get('tekstSterker')!r}")
n = 0
for x in XS:
    hs = [h for h in x['foutHints'] if h['soort'] == 'nul vergeten']
    for h in hs:
        n += 1
        if not (h['fout'].isdigit() and str(x['antwoord']).isdigit() and int(h['fout']) * 10 == int(x['antwoord'])): F.append(f"richting G5-GET-E07 #22 {x['nr']}: sleutel {h['fout']!r} is niet antwoord : 10 ({x['antwoord']})")
        if h['uitleg'] != T: F.append(f"item G5-GET-E07 #22 {x['nr']} sleutel {h['fout']!r}: {h['uitleg'][:60]}")
if n != 8: F.append(f"aantal: {n} sleutels 'nul vergeten' in #22, verwacht 8")
SNAPF = os.path.join(D_, 'snap_v1145.json')
snap = {x['nr']: [[h['fout'], h['soort'], h['uitleg'], h.get('uitlegSterker')] for h in x['foutHints']] for x in XS}
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = snap[k_][1:]
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP V-#1145 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP V-#1145 ontbreekt')
print(f"INFO V-#1145: {len(XS)} items, {n} sleutels 'nul vergeten'")
for f in F[:30]: print('FAIL', f)
print(f"check V-#1145: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
