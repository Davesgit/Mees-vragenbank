#!/usr/bin/env python3
"""Les 450 (Overzicht 17:28): scan ALLE G5-data (entry: hints/batch*.json; items: data/per_doel/*.json en data/gemapt.json) op bedrag-weggevers
('een/één/twee/… [eenheid] te …', 'nog … verder/meer/bij', 'Bijna!') en vergelijk met de guard BEDRAG. python3 scan_l450.py <basis> [--lijst]"""
import json, glob, os, re, sys, collections
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [D_, os.path.join(D_, '..', 'z1090', 'r4')]
from bedrag_lib import BEDRAG; from g5pad import g5
TAL = r'(?:één|een|twee|drie|vier|vijf|zes|tien|honderd|duizend|\d+)'
SCAN = re.compile(rf"\b{TAL} (?:\w+ ){{0,2}}te (?:veel|weinig|ver|kort|vroeg|laat|groot|klein|hoog|laag|lang)\b|\bnog {TAL} (?:\w+ ){{0,2}}(?:verder|meer|erbij|bij)\b|\bBijna!", re.I)
G = g5(sys.argv[1]); C = collections.Counter(); W = {}; WAAR = collections.defaultdict(set)
def loop(o, bron, doel):
    if isinstance(o, str):
        for z in re.split(r'(?<=[.?!])\s+|\s+/\s+|\s+·\s+', o):
            m = SCAN.search(z)
            if m: k = (z.strip()[:140]); C[k] += 1; W[k] = bool(BEDRAG.search(z)) or z.strip().startswith('Bijna!') is False and False; WAAR[k].add(f'{bron}:{doel}')
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in ('opgave', 'opgaveStappen', 'bron', 'licentie', 'merge', 'controle', 'ouderzin', 'id', 'antwoord', 'opties', 'optiesTekst', 'antwoordDetail', 'visual', 'husselPlan'): continue
            loop(v, bron, doel)
    elif isinstance(o, list):
        for v in o: loop(v, bron, doel)
for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    for s in json.load(open(p, encoding='utf-8'))['somtypen']:
        if s['doel'].startswith('G5-'): loop({k: s.get(k) for k in ('hint1', 'hint2', 'foutHints')}, 'entry', f"{s['doel']}#{s['nrOrigineel']}")
for p in sorted(glob.glob(os.path.join(G, 'data', 'per_doel', 'G5-*.json'))) + [os.path.join(G, 'data', 'gemapt.json')]:
    for x in json.load(open(p, encoding='utf-8'))['items']:
        if (x.get('doelId') or '').startswith('G5-'): loop(x, 'gemapt' if p.endswith('gemapt.json') else 'per_doel', f"{x['doelId']}#{(x.get('merge') or {}).get('somtypeNrOrigineel')}")
for k in C: W[k] = bool(BEDRAG.search(k)) and not k.startswith('Bijna!')
gev, gez = len(C), sum(1 for k in C if W[k]); print(f"vormen gevonden: {gev} (plekken {sum(C.values())}); guard vangt: {gez} vormen ({sum(C[k] for k in C if W[k])} plekken); niet gevangen: {gev - gez} vormen ({sum(C[k] for k in C if not W[k])} plekken)")
if '--lijst' in sys.argv:
    for k, n in sorted(C.items(), key=lambda a: -a[1]):
        if not W[k]: print(f"MIS {n:5d} {sorted({w.split(':')[1] for w in WAAR[k]})[:4]} | {k}")
