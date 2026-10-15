#!/usr/bin/env python3
"""Hook Oef-#1056 (Didactiek 17:20; VOORWAARDELIJK, niet geplaatst; les 369) op de BRON: VBN-E03 #2 item 007 «Ga na plek 5 nog twee stappen verder.» →
«Dat is niet ver genoeg. Tel de stappen nog eens.» (geen bedrag, geen cijfer; dezelfde vorm als de andere VBN-E03-foutreacties). Vervangt de zin in
per_doel (uitleg + afgeleide velden foutHintsTekst, foutRegels) en in data/gemapt.json. Idempotent. Gebruik: python3 zet_bron_1056.py <basis>"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
PAREN = [('Je bent te vroeg gestopt. Ga na plek 5 nog twee stappen verder.', 'Dat is niet ver genoeg. Tel de stappen nog eens.'),
         ('Je bent één plek te ver gegaan. Tel vanaf 15 maar één stap verder.', 'Je bent te ver gegaan. Tel de stappen vanaf 15 nog eens.')]      # les 450-scan (17:28): item 003
B = sys.argv[1]; G = g5(B); LOG = []
def vervang(x):
    s = json.dumps(x, ensure_ascii=False); s0 = s
    for OUD, NW in PAREN: s = s.replace(OUD, NW)
    return x if s == s0 else json.loads(s)
for naam in ('per_doel/G5-VBN-E03.json', 'gemapt.json'):
    P = os.path.join(G, 'data', naam); t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    if naam.startswith('per_doel'):
        for x in D['items']:
            if x['merge'].get('somtypeNrOrigineel') != 2: continue
            nw = vervang(x)
            if nw != x: LOG.append(f"per_doel {x['id']}: bronzin vervangen"); x.update(nw)
    else:
        for x in D['items']:
            if not (x.get('id') or '').startswith('G5-VBN-E03'): continue
            nw = vervang(x)
            if nw != x: LOG.append(f"gemapt {x['id']}: bronzin vervangen"); x.update(nw)
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Oef-#1056 bron)" + ''.join('\n  ' + l for l in LOG))
