#!/usr/bin/env python3
"""Hook Z-#1146 (Didactiek; VOORWAARDELIJK, niet geplaatst). python3 zet_z1146.py <basis>. Idempotent.
G5: «Hoeveel keer zo klein is een <kleine maat> als een <grote maat>?» en «Hoeveel keer zo groot is een <grote maat> als een <kleine maat>?»
→ «Hoeveel <kleine maat> gaat er in één <grote maat>?» (bv. «Hoeveel centimeter gaat er in één meter?»). Alleen bij twee maten uit dezelfde reeks
(km/m/cm/mm, L/ml, kg/g) waarvan de grote echt groter is; anders MELD en niets. Velden: hint1, hint2, tekst, tekstSterker."""
import json, os, re, sys, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG, MELD = [], []
MAAT = {'kilometer': ('l', 1000000), 'meter': ('l', 1000), 'centimeter': ('l', 10), 'millimeter': ('l', 1), 'liter': ('v', 1000), 'milliliter': ('v', 1), 'kilogram': ('m', 1000), 'gram': ('m', 1)}
OUD = re.compile(r'Hoeveel keer zo (klein|groot) is een (\w+) als een (\w+)\?')
def nieuw(m):
    r, a, b = m.groups(); kl, gr = (a, b) if r == 'klein' else (b, a)
    if kl not in MAAT or gr not in MAAT or MAAT[kl][0] != MAAT[gr][0] or not MAAT[gr][1] > MAAT[kl][1]: MELD.append(f"niet gezet: {m.group(0)}"); return m.group(0)
    return f'Hoeveel {kl} gaat er in één {gr}?'
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        for o, v in [(s, 'hint1'), (s, 'hint2')] + [(f, k) for f in s['foutHints'] for k in ('tekst', 'tekstSterker')]:
            if isinstance(o.get(v), str) and OUD.search(o[v]):
                nw = OUD.sub(nieuw, o[v])
                if nw != o[v]: LOG.append(f"{s['doel']} #{s['nrOrigineel']} {o.get('soort', '-')!r} [{v}]: {OUD.search(o[v]).group(0)} → {nw[:110]}"); o[v] = nw
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1146)" + ''.join('\n  ' + l for l in LOG))
