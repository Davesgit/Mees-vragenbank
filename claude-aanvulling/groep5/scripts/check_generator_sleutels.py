#!/usr/bin/env python3
"""G5 merge-fixlijst #151 (besluit Dave 19:14): bij een generator-item (bron.type = merge-generator) mag een fout-sleutel niet onder twee
regels van de entry vallen (twee sleutels op hetzelfde getal → de tekst is dubbelzinnig). Regels zonder vaste sleutels ('andere fout',
'antwoord ± 2 of meer': alleen een pred) tellen niet mee. Exit 1 bij een treffer. Draai vanuit claude-merge/g5 (na de build)."""
import json, glob, os, sys, collections
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(BASE, 'scripts'))
import fout_regels as FR
entries = {}
for p in glob.glob(f'{BASE}/hints/batch*.json'):
    for st in json.load(open(p))['somtypen']: entries[(st['doel'], st['somtype'])] = st
def treffers():
    uit = []
    for it in json.load(open(f'{BASE}/data/gemapt.json'))['items']:
        if it['bron'].get('type') != 'merge-generator': continue
        st = entries.get((it['merge']['doel'], it['merge']['somtype']))
        if not st: uit.append((it['id'], it['opgave'], 'geen entry')); continue
        c = FR.Ctx(it); per = collections.defaultdict(list)
        for f in st['foutHints']:
            comp = FR.compile_regel(f['regel'], c)
            if not comp or comp.get('alles') or not comp.get('exact'): continue
            for v in comp['exact']:
                if v != c.ans: per[v].append(f['regel'])
        for v, rs in per.items():
            if len(rs) > 1: uit.append((it['id'], it['opgave'], f"sleutel {v}: {' / '.join(rs)}"))
    return uit
if __name__ == '__main__':
    t = treffers(); n = sum(1 for it in json.load(open(f'{BASE}/data/gemapt.json'))['items'] if it['bron'].get('type') == 'merge-generator')
    print(f'Generator-items: {n} · twee regels op één sleutel: {len(t)} (FAIL)')
    for x in t: print('  FAIL', *x)
    sys.exit(1 if t else 0)
