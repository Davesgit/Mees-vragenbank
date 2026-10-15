#!/usr/bin/env python3
"""Les 450 (V-#1130): tel ALLE vormen van leen- en onthoudzinnen in G5 (entryteksten en itemteksten) en vergelijk met wat de guard ziet.
python3 inventaris_l450.py <basis>"""
import json, glob, re, collections, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lenen_lib import *; from g5pad import *
BREED = re.compile(r'komt er een (tiental|honderdtal) bij|komen er (tientallen|honderdtallen) bij|gaat er (nog )?een (tiental|honderdtal) af|onthou|\bleen|geleend'
                   r'|samen (op )?(tien|honderd|10|100) of meer|over een heel (tiental|honderdtal) heen|wordt het (tiental|honderdtal) één minder', re.I)
def guard(t): return any(rx.search(t) for _, rx, *_r in SOORTEN)
G = g5(sys.argv[1]); I = items(G); vorm = collections.Counter(); ziet = {}; ent = [0, 0]; it = [0, 0]
def zinnen(t): return [z for z in re.split(r'(?<=[.?!])\s+(?=[A-Z])', t) if BREED.search(z)]
for P in sorted(glob.glob(G + '/hints/batch*.json')):
    for s in json.load(open(P, encoding='utf-8'))['somtypen']:
        if not s['doel'].startswith('G5-'): continue
        for f in [s] + s['foutHints']:
            for k in ('hint1', 'hint2', 'tekst', 'tekstSterker'):
                t = f.get(k) or ''
                if BREED.search(t): ent[0] += 1; ent[1] += guard(t)
                for z in zinnen(t): vorm[z] += 1; ziet[z] = guard(t) and guard(z + ' ' + t[t.find(z) + len(z):][:80])
for k_, xs in I.items():
    if not k_[0].startswith('G5-'): continue
    for x in xs:
        for h in x['foutHints']:
            for v in ('uitleg', 'uitlegSterker'):
                t = h.get(v) or ''
                if BREED.search(t): it[0] += 1; it[1] += guard(t)
print(f"vormen (zinnen) in entryteksten: {len(vorm)}, guard ziet {sum(ziet.values())}")
print(f"entryteksten met leen/onthoud: {ent[0]}, guard ziet {ent[1]}; itemteksten: {it[0]}, guard ziet {it[1]}")
for z, c in vorm.most_common(): print(('   ' if ziet[z] else 'MIS'), c, z[:130])
