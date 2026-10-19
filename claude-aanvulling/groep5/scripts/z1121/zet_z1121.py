#!/usr/bin/env python3
"""Hook Z-#1121 (VOORWAARDELIJK, niet geplaatst). python3 zet_z1121.py <basis>. Idempotent.
GET-M03 #1 'aantal munten (3|4)' en MEET-E07 #1 'aantal stuks geld (3|4)' hadden een letterlijke regel '€3' / '€4' ('regel niet te lezen' in apply.log).
Nu één soort per somtype met de leesbare motorregel 'fout = het aantal munten' (#81: het aantal munten en briefjes in visual.jsRender.munten als
euro's, niet als dat het antwoord is): zo klopt de sleutel per item (3 stukken geld → €3, 4 → €4). Tekst ongewijzigd.
De entry gaat vooraan: hij is preciezer dan 'te veel geteld (50 cent) (op de foto)' (check_hints #48: precieze regels eerst).
Vereist de motorhook zet_motor_z1121.py (anders leest de motor de regel niet)."""
import json, os, re, sys, glob, copy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
DOEL = {('G5-GET-M03', 1): 'aantal munten', ('G5-MEET-E07', 1): 'aantal stuks geld'}
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        so = DOEL.get((s['doel'], s['nrOrigineel']))
        if not so: continue
        oud = [i for i, f in enumerate(s['foutHints']) if f['soort'].startswith(so + ' (') and re.fullmatch(r'€\d+', f['regel'])]
        if not oud: continue
        nw = dict(copy.deepcopy(s['foutHints'][oud[0]]), soort=so, regel='fout = het aantal munten')
        s['foutHints'] = [nw] + [f for i, f in enumerate(s['foutHints']) if i not in oud]      # vooraan: preciezer dan 'te veel geteld (… op de foto)' (#48)
        LOG.append(f"{s['doel']} #{s['nrOrigineel']}: {len(oud)} letterlijke regels ('€3', '€4') → {so!r} 'fout = het aantal munten' (vooraan)")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1121)" + ''.join('\n  ' + l for l in LOG))
