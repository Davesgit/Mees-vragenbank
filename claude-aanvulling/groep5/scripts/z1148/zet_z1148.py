#!/usr/bin/env python3
"""Hook Z-#1148 (r22, Oef-#1077; PATCH COPY, niet geplaatst). python3 zet_z1148.py <basis>. Idempotent. Na Z-#1147.
G5 maatvragen (hint1 begint met een feitzin «Eén meter (m) is honderd centimeter (cm).» of «Honderd centimeter (cm) is één meter (m).»; 8 entries
in MEET-E01/E04/E05): hint1 wordt alleen «Hoeveel <kleine maat> gaan er in één <grote maat>?». De feitzin gaat niet verloren: staat hij nog niet in
hint2 (de sterkere hint), dan komt hij letterlijk vóór hint2 («Eén meter (m) is honderd centimeter (cm). Doe het aantal meter keer honderd: …»).
Stopt (MELD, niets gezet) als de twee maten niet uit één reeks komen of de grote niet groter is."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import g5, schrijf
B = sys.argv[1]; G = g5(B); LOG, MELD = [], []
MAAT = {'kilometer': ('l', 1000000), 'meter': ('l', 1000), 'centimeter': ('l', 10), 'millimeter': ('l', 1), 'liter': ('v', 1000), 'milliliter': ('v', 1), 'kilogram': ('m', 1000), 'gram': ('m', 1)}
TAL = {'tien': 10, 'honderd': 100, 'duizend': 1000}
FEIT = re.compile(r'^(Eén (\w+) \(\w+\) is (\w+) (\w+) \(\w+\)\.|(\w+) (\w+) \(\w+\) is één (\w+) \(\w+\)\.)\s*', re.I)
def maten(m):
    if m.group(2): gr, n, kl = m.group(2), m.group(3), m.group(4)
    else: n, kl, gr = m.group(5), m.group(6), m.group(7)
    return kl.lower(), gr.lower(), TAL.get(n.lower())
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        m = FEIT.match(s.get('hint1') or '')
        if not m: continue
        kl, gr, n = maten(m)
        if kl not in MAAT or gr not in MAAT or MAAT[kl][0] != MAAT[gr][0] or n is None or MAAT[gr][1] != n * MAAT[kl][1]: MELD.append(f"{s['doel']} #{s['nrOrigineel']}: feitzin niet herkend: {m.group(1)}"); continue
        feit = m.group(1); s['hint1'] = f'Hoeveel {kl} gaan er in één {gr}?'
        if feit not in s['hint2']: s['hint2'] = f"{feit} {s['hint2']}"
        LOG.append(f"{s['doel']} #{s['nrOrigineel']}: hint1 «{s['hint1']}»; hint2 «{s['hint2'][:80]}…»")
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1148)" + ''.join('\n  ' + l for l in LOG))
