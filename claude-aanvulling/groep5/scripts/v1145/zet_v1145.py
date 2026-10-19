#!/usr/bin/env python3
"""Hook V-#1145 (Didactiek; VOORWAARDELIJK, niet geplaatst). python3 zet_v1145.py <basis>. Idempotent.
G5-GET-E07 #22 'nul vergeten' (fout = antwoord : 10; schatten met een rond getal): «Tel de nullen van het ronde getal goed mee.» krijgt de richting vooraan:
«Dat is te weinig. Tel de nullen van het ronde getal goed mee.» (de methodezin blijft). tekstSterker ongewijzigd."""
import json, os, sys, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
OUD, NIEUW = 'Tel de nullen van het ronde getal goed mee.', 'Dat is te weinig. Tel de nullen van het ronde getal goed mee.'
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if (s['doel'], s['nrOrigineel']) != ('G5-GET-E07', 22): continue
        for f in s['foutHints']:
            if f['soort'] == 'nul vergeten' and f['regel'] == 'fout = antwoord : 10' and f['tekst'] == OUD:
                f['tekst'] = NIEUW; LOG.append(f"G5-GET-E07 #22 'nul vergeten': {NIEUW}")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (V-#1145)" + ''.join('\n  ' + l for l in LOG))
