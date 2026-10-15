#!/usr/bin/env python3
"""Les 450-scan (Z-#1136): zichtbare kindteksten (entry hint1/hint2/tekst/tekstSterker + item uitleg/uitlegSterker) van heel G5 op bedragresten. python3 scan_z1136.py <basis>"""
import json, os, re, sys, glob, collections
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1091_v5'), os.path.join(D_, '..', 'z1090', 'r4')]
from bedrag_lib import BEDRAG; from g5pad import *
P = {'bedrag-guard': BEDRAG,
     'een/één/twee/tien X te …': re.compile(r'\b(?:een|één|twee|drie|tien|honderd)(?: hele?)? (?:\w+ )?te (?:veel|weinig|ver|kort|hoog|laag|vroeg|laat|zwaar|licht)\b', re.I),
     'nog … verder (met getal)': re.compile(r'\bnog (?:\d+|een|één|twee|drie|tien) (?:\w+ )?verder\b', re.I),
     'Bijna!': re.compile(r'^Bijna!'), 'hele ronde / heel uur': re.compile(r'\bhele ronde\b|\been heel uur\b', re.I)}
G = g5(sys.argv[1]); c = collections.Counter(); ex = {}
def zie(w, d, t):
    for k, r in P.items():
        m = r.search(t)
        if m: c[(k, d, m.group(0).lower(), w)] += 1; ex.setdefault((k, d, m.group(0).lower(), w), t[:100])
for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    for s in json.load(open(p, encoding='utf-8'))['somtypen']:
        for f in [s] + s['foutHints']:
            for v in ('hint1', 'hint2', 'tekst', 'tekstSterker'): zie('entry', s['doel'], f.get(v) or '')
for (d, n), xs in items(G).items():
    for x in xs:
        for h in x['foutHints']:
            for v in ('uitleg', 'uitlegSterker'): zie('item', d, h.get(v) or '')
for k, v in sorted(c.items()): print(f"{v:5d}  {k[0]:26s} {k[1]:12s} {k[3]:5s} {k[2]!r:34s} | {ex[k]}")
print(f"totaal: {sum(c.values())} plekken, {len(c)} vormen")
