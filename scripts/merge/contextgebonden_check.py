#!/usr/bin/env python3
"""Z-#518 (review G7 batch 1, Didactiek 8 okt; les 147): guard voor de vlag 'contextgebonden' in een hint-entry
(bijv. "contextgebonden": {"woorden": ["kinderen", "zandbak"], "aanname": "…"}; de vlag zet Oefeningen, V-#517).
WARN als een gevlagde entry meer dan één item heeft (er kwamen items bij), of als een vlagwoord niet in de opgave van een item staat.
Gebruik: rapport(base) met base = claude-merge/gN; geeft het aantal WARN terug."""
import json, glob, os, collections
def treffers(base):
    items = json.load(open(f'{base}/data/gemapt.json'))['items']
    per = collections.defaultdict(list)
    for it in items:
        if it['merge'].get('status', 'gemapt') == 'gemapt': per[(it['merge']['doel'], it['merge'].get('somtypeNrOrigineel'))].append(it)
    uit, n = [], 0
    for p in sorted(glob.glob(f'{base}/hints/batch*.json')):
        for e in json.load(open(p)).get('somtypen', []):
            cg = e.get('contextgebonden')
            if not cg: continue
            n += 1; its = per.get((e['doel'], e.get('nrOrigineel')), [])
            if len(its) > 1: uit.append((e['doel'], e.get('nrOrigineel'), f'{len(its)} items (gevlagd voor één item)'))
            woorden = cg.get('woorden', []) if isinstance(cg, dict) else []
            for it in its:
                mis = [w for w in woorden if w.lower() not in it['opgave'].lower()]
                if mis: uit.append((e['doel'], e.get('nrOrigineel'), f"{it['id']}: vlagwoord(en) {mis} niet in de opgave"))
    return n, uit
def rapport(base):
    n, uit = treffers(base)
    print(f"\nCONTEXT (Z-#518: entry met 'contextgebonden' krijgt meer items, of een vlagwoord staat niet in de opgave): {len(uit)} (WARN) · gevlagde entries: {n}")
    for x in uit: print('  WARN CONTEXT', *x)
    return len(uit)
