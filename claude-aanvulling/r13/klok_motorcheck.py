#!/usr/bin/env python3
"""r13: draait de motor (met KLOK_PUNT) opnieuw over elk item met een tijd in de huisvorm en vergelijkt foutHints/foutRegels/algemeneFoutHint
met wat klok_r13.py schreef. Plus: rekent '14.30 uur', '14.30' en '14:30' goed (geldigeAntwoorden). Gebruik: python3 r13/klok_motorcheck.py r13/g5"""
import sys, os, json, glob, copy, importlib.util, collections
g = sys.argv[1]; sys.path.insert(0, f'{g}/scripts')
sp = importlib.util.spec_from_file_location('ah', f'{g}/scripts/apply_hints.py'); AH = importlib.util.module_from_spec(sp); sp.loader.exec_module(AH)
M = AH.fout_regels
items = [it for p in sorted(glob.glob(f'{g}/data/per_doel/*.json')) for it in json.load(open(p))['items']]
idx = collections.defaultdict(list)
for it in items: idx[(it['merge']['doel'], it['merge']['somtype'])].append(it)
n = gelijk = 0; anders = []; ga_fout = []
for b in sorted(glob.glob(f'{g}/hints/batch*.json')):
    for st in json.load(open(b))['somtypen']:
        for it in idx.get((st['doel'], st.get('somtype')), []):
            if not M._klok_heeft_punt(it): continue
            c = copy.deepcopy(it); M.pas_toe(c, st, AH.cellen(c)); n += 1
            if {h['fout'] for h in c['foutHints']} == {h['fout'] for h in it['foutHints']}: gelijk += 1
            else: anders.append((it['id'], sorted(h['fout'] for h in it['foutHints']), sorted(h['fout'] for h in c['foutHints'])))
for it in items:
    a = str(it.get('antwoord'))
    if it.get('type') != 'meerkeuze' and a.endswith(' uur') and a[:-4].replace('.', '').isdigit():
        h, m = a[:-4].split('.')
        if not {f'{h}.{m} uur', f'{h}.{m}', f'{h}:{m}'} <= set(it.get('geldigeAntwoorden') or []): ga_fout.append(it['id'])
print(f'{g}: {n} items met tijd in huisvorm opnieuw door de motor · sleutels gelijk {gelijk} · anders {len(anders)} · open tijd-antwoorden zonder de drie vormen: {len(ga_fout)}')
for x in anders[:8]: print('  ANDERS', x)
for x in ga_fout[:5]: print('  GELDIG', x)
