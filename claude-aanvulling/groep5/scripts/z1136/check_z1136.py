#!/usr/bin/env python3
"""Check Z-#1136. [MUT=..] [SNAP=1] python3 check_z1136.py <basis>
- GET-E06 #1/#2: geen 'Bijna!'; per item: 'te veel' ⇔ sleutel > antwoord, 'te weinig' ⇔ sleutel < antwoord; '1 cent'-soort = laatste cijfer, '10 cent' = eerste cijfer;
- GET-M06: geen 'hele ronde' / 'nog een ronde bij';
- bedrag-guard (bedrag_lib v5 BEDRAG + 'hele ronde', 'heel uur te') in entry- en itemteksten van GET-E06, GET-M06, MEET-E06, MEET-E07;
- SNAP per regel."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1091'), os.path.join(D_, '..', 'z1090', 'r4')]
from bedrag_lib import BEDRAG; from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
DOELEN = ('G5-GET-E06', 'G5-GET-M06', 'G5-MEET-E06', 'G5-MEET-E07')
EXTRA = re.compile(r'\bnog een hele ronde\b|\been heel uur te\b|\b(?:één|een|tien|twee) (?:euro|cent) te (?:veel|weinig)\b', re.I)
def guard(t): return BEDRAG.search(t) or EXTRA.search(t)
ENT = [s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'] in DOELEN]
def cent(v):
    m = re.fullmatch(r'\s*€?\s*(\d+)(?:,(\d{1,2}))?\s*', str(v)); return int(m.group(1)) * 100 + int((m.group(2) or '0').ljust(2, '0')) if m else None
X6 = [(k, x) for k in (('G5-GET-E06', 1), ('G5-GET-E06', 2)) for x in I.get(k, [])]
if MUT == 'M_richting':
    h_ = next(h for _, x in X6 for h in x['foutHints'] if h['soort'].startswith('centen te veel')); h_['uitleg'] = h_['uitleg'].replace('te veel', 'te weinig', 1)
if MUT == 'M_bijna':
    h_ = next(h for _, x in X6 for h in x['foutHints'] if h['soort'].startswith('centen te')); h_['uitleg'] = 'Bijna! De centen kloppen net niet.'
if MUT == 'M_ronde':
    f_ = next(f for s in ENT if s['doel'] == 'G5-GET-M06' for f in s['foutHints'] if f['soort'] == 'nog een ronde'); f_['tekst'] = f_['tekst'].replace('Daar kun je nog verder mee verdelen.', 'Daar past nog een hele ronde bij.')
if MUT == 'M_euro':
    f_ = next(f for s in ENT if s['doel'] == 'G5-MEET-E07' for f in s['foutHints'] if 'euro te veel' in f['soort']); f_['tekst'] = 'Dat is één euro te veel. ' + f_['tekst']
if MUT == 'M_plek':      # 1-cent-soort met de kijkzin van 10 cent
    h_ = next(h for _, x in X6 for h in x['foutHints'] if '(1 cent)' in h['soort']); h_['uitleg'] = h_['uitleg'].replace('laatste cijfer', 'eerste cijfer')
n_r = 0
for (d, n), x in X6:
    a = cent(x['antwoord'])
    for h in x['foutHints']:
        t = h.get('uitleg') or ''
        if t.startswith('Bijna'): F.append(f"bijna {d} #{n} {x['nr']} sleutel {h['fout']!r}: {t[:60]}")
        if not h['soort'].startswith('centen te'): continue
        v = cent(h['fout']); n_r += 1
        if a is None or v is None: F.append(f"richting {d} #{n} {x['nr']} sleutel {h['fout']!r}: bedrag niet te lezen"); continue
        hi, lo = t.startswith('Dat is te veel'), t.startswith('Dat is te weinig')
        if not ((hi and v > a) or (lo and v < a)): F.append(f"richting {d} #{n} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {t[:50]}")
        stap = abs(v - a); plek = 'laatste cijfer' if stap == 1 else 'eerste cijfer' if stap == 10 else None
        if plek is None or plek not in t: F.append(f"plek {d} #{n} {x['nr']} sleutel {h['fout']!r} (verschil {stap} cent): {t[:70]}")
for s in ENT:
    for f in [s] + s['foutHints']:
        for v in (('hint1', 'hint2') if f is s else ('tekst', 'tekstSterker')):
            t = f.get(v) or ''
            if guard(t): F.append(f"bedrag {s['doel']} #{s['nrOrigineel']} {f.get('soort', '-')!r} [{v}]: {t[:70]}")
            if s['doel'] in ('G5-GET-E06',) and t.startswith('Bijna'): F.append(f"bijna {s['doel']} #{s['nrOrigineel']} {f.get('soort')!r}")
for (d, n), xs in I.items():
    if d not in DOELEN: continue
    for x in xs:
        for h in x['foutHints']:
            t = (h.get('uitleg') or '') + ' ' + (h.get('uitlegSterker') or '')
            if guard(t): F.append(f"weggever {d} #{n} {x['nr']} sleutel {h['fout']!r}: {t.strip()[:70]}")
SNAPF = os.path.join(D_, 'snap_z1136.json')
snap = {f"{s['doel']}#{s['nrOrigineel']} {f['soort']}": [f.get('tekst'), f.get('tekstSterker')] for s in ENT if s['doel'] in ('G5-GET-E06', 'G5-GET-M06') for f in s['foutHints']
        if f['soort'].startswith('centen') or f['soort'] == 'nog een ronde'}
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0] + ' Kijk goed.', snap[k_][1]]
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1136 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)][:20]
else: F.append('SNAP Z-#1136 ontbreekt')
print(f"INFO Z-#1136: {len(ENT)} entries; GET-E06 {len(X6)} items, richting/plek nagekeken bij {n_r} sleutels; SNAP {len(snap)} regels")
for f in F[:30]: print('FAIL', f)
print(f"check Z-#1136: FAIL {len(F)}" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
