#!/usr/bin/env python3
"""Hook Z-#1147 (r22, Oef-#1077; PATCH COPY, niet geplaatst). python3 zet_z1147.py <basis>. Idempotent.
G5 overal 'gaat er in' → 'gaan er in' (zoals G8): hints/batch*.json (hint1, hint2, ouderzin, algemeneFoutHint, foutHints tekst/tekstSterker) en
somtypen/*.md. De itemdata (data/gemapt.json en per_doel: uitleg, foutHintsTekst, foutRegels; 384 plekken) volgt via sync_hint_keys + apply_hints."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import g5, schrijf
B = sys.argv[1]; G = g5(B); RE = re.compile(r'\bgaat er in\b'); LOG = []
VELD = ('hint1', 'hint2', 'ouderzin', 'algemeneFoutHint')
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        for o, v in [(s, k) for k in VELD] + [(f, k) for f in s['foutHints'] for k in ('tekst', 'tekstSterker')]:
            if isinstance(o.get(v), str) and RE.search(o[v]):
                o[v] = RE.sub('gaan er in', o[v]); LOG.append(f"{os.path.basename(P)} {s['doel']} #{s['nrOrigineel']} {o.get('soort', '-')!r} [{v}]")
    if len(LOG) > n0: schrijf(P, t, D)
for P in sorted(glob.glob(os.path.join(G, 'somtypen', '*.md'))):
    t = open(P, encoding='utf-8').read(); n = len(RE.findall(t))
    if n: open(P, 'w', encoding='utf-8').write(RE.sub('gaan er in', t)); LOG.append(f"{os.path.basename(P)}: {n}")
print(f"{B}: {len(LOG)} wijzigingen (Z-#1147)" + ''.join('\n  ' + l for l in LOG))
