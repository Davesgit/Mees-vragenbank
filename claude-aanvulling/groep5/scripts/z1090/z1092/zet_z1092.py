#!/usr/bin/env python3
"""Hook Z-#1092 (Didactiek, zacht; VOORWAARDELIJK, niet geplaatst; bovenop na-ronde-z1090 379fab1 + r2): G5-teksten noemen een getal bij zijn rol, niet
bij zijn plek (les 193): 'het eerste/tweede getal' → 'het grootste/kleinste getal' (min, plus, keer, gedeeld, geld) of 'het getal dat er al staat'
(aanvullen, □). Per entry: elk item moet dezelfde soort som hebben en de twee getallen moeten verschillen (bij min/gedeeld: het eerste is het grootste);
anders MELD en niets. Niet: MEET-E06 (tijd, kalender, klok), VBN-E03 (rijen) en het rooster (M05 #5, MEET-E03 #1): daar ligt de volgorde vast.
Velden: hint1, hint2, en tekst/tekstSterker van elke fout-hint. Idempotent. Gebruik: python3 zet_z1092.py <basis>"""
import json, os, sys, glob, re
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D_); sys.path.insert(0, os.path.join(D_, '..', 'r4'))
from plek_lib import *; from g5pad import *
B = sys.argv[1]; G = g5(B); I = items(G); LOG, MELD = [], []
def item_ok(x, rs):
    so, n = soort_item(x)
    if rs == 'aanvul': return so == 'aanvul'
    return so is not None and so != 'aanvul' and len(n) >= 2 and n[0] != n[1] and (so not in ('min', 'geldmin', 'gedeeld') or n[0] > n[1])
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        k_ = (s['doel'], s['nrOrigineel'])
        if s['doel'] in UIT or k_ in UIT_ENTRY: continue
        if k_ in ROOSTER:      # Oef-#1052
            its = I.get(k_, [])
            if not its or not all(rooster_ok(k_, x) for x in its): MELD.append(f"{s['doel']} #{s['nrOrigineel']}: rooster niet waar per item: niet gezet"); continue
            for v in ('hint1', 'hint2'):
                for a_, b_ in ROOSTER[k_]:
                    if isinstance(s.get(v), str) and a_ in s[v]: s[v] = s[v].replace(a_, b_); LOG.append(f"{s['doel']} #{s['nrOrigineel']} [{v}] (rooster): {b_}")
        velden = [(s, k) for k in ('hint1', 'hint2')] + [(f, k) for f in s['foutHints'] for k in ('tekst', 'tekstSterker')]
        hits = [(o, k) for o, k in velden if isinstance(o.get(k), str) and PLEK.search(o[k])]
        if not hits: continue
        its = I.get(k_, []); rs = rolsoort([soort_item(x)[0] for x in its])
        if rs is None or not its or not all(item_ok(x, rs) for x in its):
            MELD.append(f"{s['doel']} #{s['nrOrigineel']}: soort som niet eenduidig of getallen gelijk/omgekeerd ({len(hits)} plekken): niet gezet"); continue
        for o, k in hits:
            nw = vervang(o[k], rs)
            if PLEK.search(nw): MELD.append(f"{s['doel']} #{s['nrOrigineel']} [{k}]: plekwoord blijft: {nw[:80]}")
            if nw != o[k]: LOG.append(f"{s['doel']} #{s['nrOrigineel']} [{k}] ({rs}): {nw[:90]}"); o[k] = nw
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1092)" + ''.join('\n  ' + l for l in LOG))
