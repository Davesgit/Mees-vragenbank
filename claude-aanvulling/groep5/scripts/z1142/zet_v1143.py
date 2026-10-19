#!/usr/bin/env python3
"""Hook V-#1143 (les 458; VOORWAARDELIJK, niet geplaatst). python3 zet_v1143.py <basis>. Idempotent.
GET-E06 #1/#2: de ±1- en ±10-cent-regels zonder filter krijgen '(sleutel met centen)', zodat ze nooit een sleutel zonder komma pakken,
ook niet als de volgorde van de entries verandert (de '(sleutel hele euro)'-soort staat nu toevallig vóór de 10-cent-soort)."""
import json, os, re, sys, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
RX = re.compile(r'^fout = antwoord [+−-] (?:1|10) cent$')
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if s['doel'] != 'G5-GET-E06' or s['nrOrigineel'] not in (1, 2): continue
        for f in s['foutHints']:
            if f['soort'].startswith('centen te') and RX.match(f['regel']):
                f['regel'] += ' (sleutel met centen)'; LOG.append(f"G5-GET-E06 #{s['nrOrigineel']} {f['soort']!r}: {f['regel']}")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (V-#1143)" + ''.join('\n  ' + l for l in LOG))
