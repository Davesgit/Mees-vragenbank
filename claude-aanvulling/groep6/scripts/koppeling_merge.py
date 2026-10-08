#!/usr/bin/env python3
"""Leest hints/koppeling_merge.json (G6, ronde 9: kopie van g5/scripts/koppeling_merge.py): hint-entries die bewust zijn samengevoegd of geparkeerd.
Gebruikt door sync_hint_keys.py, apply_hints.py en check_hints.py. Nooit stil: elke speciale entry staat in de log."""
import json, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = f'{BASE}/hints/koppeling_merge.json'
def laad():
    if not os.path.exists(P): return {}, {}
    D = json.load(open(P, encoding='utf-8'))
    return ({(x['doel'], x['vanNrOrigineel']): x for x in D.get('samengevoegd', [])},
            {(x['doel'], x['nrOrigineel']): x for x in D.get('geparkeerd', [])})
def sleutel(st): return (st.get('doel'), st.get('nrOrigineel'))
def speciaal(st):
    S, G = laad(); k = sleutel(st)
    return 'samengevoegd' if k in S else 'geparkeerd' if k in G else None
def inhoud(st): return (st.get('hint1'), st.get('hint2'), st.get('ouderzin'), tuple((f.get('regel'), f.get('tekst')) for f in st.get('foutHints') or []))
def controleer(entries):
    """-> (problemen, info). entries = alle hint-entries uit hints/batch*.json"""
    S, G = laad(); idx = {sleutel(st): st for st in entries}; prob = []; info = []
    for k, x in S.items():
        van, naar = idx.get(k), idx.get((x['doel'], x['naarNrOrigineel']))
        if van is None: info.append(f"samengevoegd {k[0]} #{k[1]}: geen entry (meer) in de batches"); continue
        if naar is None: prob.append(f"samengevoegd {k[0]} #{k[1]} → #{x['naarNrOrigineel']}: de entry waar hij in opgaat ontbreekt"); continue
        if inhoud(van) != inhoud(naar): prob.append(f"samengevoegd {k[0]} #{k[1]} → #{x['naarNrOrigineel']}: de twee entries zijn niet gelijk (hint1/hint2/ouderzin/regels/teksten); nooit stil samenvoegen")
        else: info.append(f"samengevoegd {k[0]} #{k[1]} → #{x['naarNrOrigineel']} (entries gelijk; {x['reden']})")
    for k, x in G.items():
        info.append(f"geparkeerd {k[0]} #{k[1]} → {x['naar']}" + ('' if k in idx else ' (geen entry in de batches)'))
    return prob, info
