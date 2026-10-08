#!/usr/bin/env python3
"""Regressietest voor de gedeelde motor fout_regels.py: draait de oude (pad 1) en de nieuwe motor (pad 2) met dezelfde vlaggen als
apply_hints van de groep over alle items met een hint-entry, en meldt elk item waarvan foutHints, foutRegels of algemeneFoutHint anders is.
Gebruik: python3 motor_regressie.py <groepdir> <oud.py> <nieuw.py>   (leest alleen)"""
import sys, os, json, glob, copy, importlib.util, collections
g, oud, nieuw = sys.argv[1:4]
def laad(p, naam):
    sp = importlib.util.spec_from_file_location(naam, p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sys.path.insert(0, f'{g}/scripts'); AH = laad(f'{g}/scripts/apply_hints.py', 'ah_' + os.path.basename(g))
O, N = laad(oud, 'motor_oud'), laad(nieuw, 'motor_nieuw')
for M in (O, N):
    for k in ("BEREIK_AFRONDEN", "GELD_PUNT", "LIJN_BINNEN", "KOMMA437", "NEG494", "KOLOM_VOOR_DEEL", "ANTWOORD_UIT_WAARDEN"): setattr(M, k, getattr(AH.fout_regels, k, False))
G = json.load(open(f'{g}/data/gemapt.json'))['items']
idx = collections.defaultdict(list)
for it in G: idx[(it['merge']['doel'], it['merge']['somtype'])].append(it)
n = 0; diff = []; erbij = []
for b in sorted(glob.glob(f'{g}/hints/batch*.json')):
    for st in json.load(open(b))['somtypen']:
        for it in idx.get((st['doel'], st.get('somtype')), []):
            a, c = copy.deepcopy(it), copy.deepcopy(it)
            O.pas_toe(a, st, AH.cellen(a)); N.pas_toe(c, st, AH.cellen(c)); n += 1
            if (a['foutHints'], a['foutRegels'], a['algemeneFoutHint']) != (c['foutHints'], c['foutRegels'], c['algemeneFoutHint']):
                diff.append((it['id'], [h['fout'] for h in a['foutHints']], [h['fout'] for h in c['foutHints']]))
                # alleen sleutels erbij? (elke oude fout-hint staat ongewijzigd in de nieuwe, de algemene fout-hint is gelijk, en elke oude regelwaarde staat nog bij dezelfde regel)
                oudw = {(r['regel'], w) for r in a['foutRegels'] for w in (r.get('match') or {}).get('waarden') or []}
                nieuww = {(r['regel'], w) for r in c['foutRegels'] for w in (r.get('match') or {}).get('waarden') or []}
                if all(h in c['foutHints'] for h in a['foutHints']) and a['algemeneFoutHint'] == c['algemeneFoutHint'] and oudw <= nieuww: erbij.append(it['id'])
print(f'{g}: {n} items vergeleken · {len(diff)} anders, waarvan {len(erbij)} alleen met sleutels erbij')
for d in [x for x in diff if x[0] not in erbij][:15]: print('  ANDERS', d)
for d in diff[:15]: print('  ', d)
