#!/usr/bin/env python3
"""Hook Z-#1091 per somtype (VOORWAARDELIJK, niet geplaatst; bovenop 379fab1 + r2). Gebruik: python3 zet_z1091.py <somtype, bv. G5-GET-M05> <basis>
Herschrijft in dat somtype tekst/tekstSterker van de fout-hints (bedrag → richting + waar kijken, zie bedrag_lib.REGELS); in G5-VBN-E03 alleen V-#1052.
Idempotent (de regels vangen alleen de oude zinnen)."""
import json, os, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [D_, os.path.join(D_, '..', 'z1090', 'r4')]
from bedrag_lib import *; from g5pad import *
DOEL, B = sys.argv[1], sys.argv[2]; assert DOEL in SCOPE, DOEL
G = g5(B); LOG = []
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if s['doel'] != DOEL: continue
        for f in [s] + s['foutHints']:      # ook hint1/hint2 van de entry (M06 #8 hint2 'Dan is er nog één nodig.')
            for v in (('hint1', 'hint2') if f is s else ('tekst', 'tekstSterker')):
                nw = herschrijf(f.get(v), DOEL)
                if nw != f.get(v): LOG.append(f"{DOEL} #{s['nrOrigineel']} {f.get('soort', '-')!r} [{v}]: {nw[:100]}"); f[v] = nw
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1091 {DOEL})" + ''.join('\n  ' + l for l in LOG))
