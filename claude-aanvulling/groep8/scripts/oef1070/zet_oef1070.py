#!/usr/bin/env python3
"""Hook Oef-#1070 (G8; Overzicht akkoord 19 okt; VOORWAARDELIJK, niet geplaatst). python3 zet_oef1070.py <basis>. Idempotent.
G8-GET-M01 #1–#5 en G8-MEET-E03 #1–#9, soorten 'nul te veel' (regel 'fout = antwoord × 10') en 'nul te weinig' ('fout = antwoord : 10'):
«Dat is tien keer te veel[: er staat een nul te veel].» → «Dat is tien keer te groot.», «Dat is tien keer te weinig[: er mist een nul].» → «Dat is tien keer te klein.»;
de zin erachter blijft. Niet: 'duizend keer te weinig' (GET-M01) en 'nul te weinig' met 'fout = een nul te weinig (afgekapt)' (MEET-E03 #5). Alleen veld 'tekst'.
G8-motor (0d5393e8) ongewijzigd: de sleutels komen uit de regel, niet uit de tekst."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g8pad import *
B = sys.argv[1]; G = g8(B); LOG = []
DOEL = {'G8-GET-M01': range(1, 6), 'G8-MEET-E03': range(1, 10)}
VERV = {('nul te veel', 'fout = antwoord × 10'): (re.compile(r'^Dat is tien keer te veel(?:: er staat een nul te veel)?\.'), 'Dat is tien keer te groot.'),
        ('nul te weinig', 'fout = antwoord : 10'): (re.compile(r'^Dat is tien keer te weinig(?:: er mist een nul)?\.'), 'Dat is tien keer te klein.')}
P_ = sorted({P for P, s in entries(G) if s['doel'] in DOEL})
for P in P_:
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if s['nrOrigineel'] not in DOEL.get(s['doel'], ()): continue
        for f in s['foutHints']:
            v = VERV.get((f['soort'], f['regel']))
            if not v: continue
            nw = v[0].sub(v[1], f['tekst'], count=1)
            if nw != f['tekst']: LOG.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']!r}: {nw}"); f['tekst'] = nw
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Oef-#1070)" + ''.join('\n  ' + l for l in LOG))
