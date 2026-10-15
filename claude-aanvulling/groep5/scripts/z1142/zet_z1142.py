#!/usr/bin/env python3
"""Hook Z-#1142 (Didactiek; VOORWAARDELIJK, niet geplaatst). python3 zet_z1142.py <basis>. Idempotent.
GET-E06 #1/#2: een sleutel zonder komma (hele euro, '€11' bij '€11,10') krijgt niet «het eerste cijfer achter de komma» maar
«Kijk goed naar de centen: die mis je nog.» (met de richting). ±1 cent met lenen/inwisselen en sleutels waar de euro verandert: ongewijzigd.
(a) motor: fout_regels.compile_regel kent '(sleutel hele euro)' / '(sleutel met centen)' achter een regel (filter op de sleutelwaarde);
(b) data: per entry vóór 'centen te veel/weinig (10 cent)' een soort '… (10 cent, hele euro)' met die regel + tekst."""
import json, os, sys, glob, copy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
# (a) motor
MP = os.path.join(G, 'scripts', 'fout_regels.py'); m = open(MP, encoding='utf-8').read()
OUD = '''    res = _compile_regel(regel, c)
    if res and getattr(c, 'eenheid', None)'''
NIEUW = '''    # Z-#1142: '(sleutel hele euro)' / '(sleutel met centen)' achter een regel: alleen sleutels die een heel eurobedrag zijn (zonder komma), of juist niet
    if (q1142 := re.search(r'\\s*\\(sleutel (hele euro|met centen)\\)\\s*$', regel, re.I)):
        res = compile_regel(regel[:q1142.start()], c); heel = q1142.group(1).lower() == 'hele euro'
        if not res or res.get('alles'): return res
        ok = lambda v: _cent(v) is not None and (',' not in str(v)) == heel
        res = dict(res)
        if res.get('exact') is not None: res['exact'] = {v for v in res['exact'] if ok(v)}
        if res.get('pred'): p0 = res['pred']; res['pred'] = lambda v, p0=p0: p0(v) and ok(v)
        return res
    res = _compile_regel(regel, c)
    if res and getattr(c, 'eenheid', None)'''
if 'Z-#1142' not in m:
    assert OUD in m, 'motorvorm onbekend'; open(MP, 'w', encoding='utf-8').write(m.replace(OUD, NIEUW, 1)); LOG.append('fout_regels.compile_regel: (sleutel hele euro|met centen)')
# (b) data
TX = {'veel': 'Dat is te veel. Kijk goed naar de centen: die mis je nog.', 'weinig': 'Dat is te weinig. Kijk goed naar de centen: die mis je nog.'}
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if s['doel'] != 'G5-GET-E06' or s['nrOrigineel'] not in (1, 2): continue
        for r in ('veel', 'weinig'):
            so = f'centen te {r} (10 cent)'; nso = f'centen te {r} (10 cent, hele euro)'
            if any(f['soort'] == nso for f in s['foutHints']): continue
            i = next((i for i, f in enumerate(s['foutHints']) if f['soort'] == so), None)
            if i is None: continue
            f = s['foutHints'][i]; nw = dict(copy.deepcopy(f), soort=nso, regel=f['regel'] + ' (sleutel hele euro)', tekst=TX[r])
            s['foutHints'].insert(i, nw); LOG.append(f"G5-GET-E06 #{s['nrOrigineel']} + {nso!r}")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1142)" + ''.join('\n  ' + l for l in LOG))
