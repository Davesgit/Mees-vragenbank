#!/usr/bin/env python3
"""Hook Oef-#1040 (Didactiek 15 okt 16:40, VOORWAARDELIJK, niet geplaatst; na Z-#1090 op na-ronde-z1090):
G5-GET-E05 #17 'honderdtal vergeten' met regel 'fout = antwoord − 10' (377 → 99, 378 → 97) heet voortaan 'tiental te weinig' met
«Dat is te weinig. Tel de tientallen nog eens bij elkaar.» (geen bedrag; Z-#1090-patroon). Voorwaarden: regel precies 'fout = antwoord − 10',
er is nog geen soort 'tiental te weinig' in de entry, elk item is een plussom (twee getallen samen = antwoord) en elke sleutel ligt onder het
antwoord. Anders MELD en niets. Idempotent. Gebruik: python3 zet_oef1040.py <basis>"""
import json, os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g5pad import *; from lenen_lib import som, ant
B = sys.argv[1]; G = g5(B); I = items(G); LOG, MELD = [], []
T1040 = 'Dat is te weinig. Tel de tientallen nog eens bij elkaar.'
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if (s['doel'], s['nrOrigineel']) != ('G5-GET-E05', 17): continue
        f = next((f for f in s['foutHints'] if f['soort'] == 'honderdtal vergeten'), None)
        if f is None: continue
        its = I.get(('G5-GET-E05', 17), [])
        ks = [(x, k) for x in its for k in x['foutHints'] if k['soort'] == 'honderdtal vergeten']
        if f['regel'].replace('-', '−').strip() != 'fout = antwoord − 10': MELD.append(f"regel {f['regel']!r}"); continue
        if any(g['soort'] == 'tiental te weinig' for g in s['foutHints']): MELD.append("er is al een 'tiental te weinig'"); continue
        if not ks or any((som(x) or ('',))[0] != '+' or not int(re.match(r'\d+', k['fout']).group(0)) < ant(x) for x, k in ks): MELD.append('niet elk item een plussom met de sleutel onder het antwoord'); continue
        f['soort'] = 'tiental te weinig'; f['tekst'] = T1040
        LOG.append(f"G5-GET-E05 #17 'honderdtal vergeten' → 'tiental te weinig' ({len(ks)} sleutels: {', '.join(x['nr'] + ' ' + k['fout'] for x, k in ks)})")
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD Oef-#1040', m)
print(f"{B}: {len(LOG)} wijzigingen (Oef-#1040)" + ''.join('\n  ' + l for l in LOG))
