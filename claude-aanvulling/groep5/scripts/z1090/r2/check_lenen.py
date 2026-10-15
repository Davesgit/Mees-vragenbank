#!/usr/bin/env python3
"""Check Z-#1090 ronde 2 (lenen/onthouden per item, Oef-#1045/#1046) + Oef-#1040 op een G5-kopie. [MUT=..] [SNAP=1] python3 check_lenen.py <basis>
L: elke itemsleutel met een uitleg over lenen (uitleg/uitlegSterker) hoort bij een item waar a − b echt leent bij de eenheden; O: «eenheden samen tien of
meer» alleen waar de eenheden samen ≥ 10 zijn, «tientallen samen op tien of meer» alleen waar de tientallen (met wat meekomt) ≥ 100 halen.
Het item wordt los van de motor gelezen (lenen_lib.som). 1040: G5-GET-E05 #17 geen 'honderdtal vergeten' meer; 99/97 = 'tiental te weinig' met de
tekst zonder bedrag. SNAP per item (snap_lenen.json): sleutel → soort, lenen/onthouden waar, uitleg."""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g5pad import *; from lenen_lib import *
def _zelfde1092(o, n):
    """Z-#1092 bovenop: een SNAP-tekst mag alleen verschillen doordat zet_z1092 een plekwoord door een rol verving"""
    if o == n: return True
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1092')); from plek_lib import vervang
    except ImportError: return False
    def m(x, rs): return vervang(x, rs) if isinstance(x, str) else [m(y, rs) for y in x] if isinstance(x, list) else x
    return o is not None and any(m(o, rs) == n for rs in ('aanvul', 'groot'))
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); G = g5(B); I = items(G); F, INFO = [], []
SNAPF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snap_lenen.json'); FN = {n: (rx, fn) for n, rx, fn, *_ in SOORTEN}
ENT = {}
for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    for s in json.load(open(p, encoding='utf-8'))['somtypen']: ENT[(s['doel'], s['nrOrigineel'])] = s
E05 = I.get(('G5-GET-E05', 6), [])
def eerste(fn, waarde, soortdeel):
    return next((x, k) for (d, n), xs in sorted(I.items(), key=lambda kv: str(kv[0])) if d.startswith('G5-GET') for x in xs if fn(x) is waarde for k in x['foutHints'] if soortdeel in k['soort'])
if MUT == 'M_leen': x_, k_ = eerste(lambda x: leent(x), False, 'tiental te veel'); k_['uitleg'] = 'Dat is te veel. Ga je bij de eenheden over een heel tiental heen? Dan gaat er nog een tiental af.'
if MUT == 'M_onth': x_, k_ = eerste(lambda x: onthoudt(x), False, 'tiental te weinig'); k_['uitleg'] = 'Dat is te weinig. De eenheden zijn samen tien of meer: dan komt er een tiental bij.'
if MUT == 'M_onthH': x_, k_ = eerste(lambda x: onthoudt(x, 100), False, 'honderdtal te weinig'); k_['uitlegSterker'] = 'Komen de tientallen samen op tien of meer? Dan komt er een honderdtal bij.'
if MUT == 'M_1040': next(k for x in I[('G5-GET-E05', 17)] for k in x['foutHints'] if k['fout'] in ('99', '97'))['soort'] = 'honderdtal vergeten'
if MUT == 'M_1040t': next(k for x in I[('G5-GET-E05', 17)] for k in x['foutHints'] if k['fout'] in ('99', '97'))['uitleg'] = 'Dat is één tiental te weinig. Tel de tientallen nog eens bij elkaar.'
if MUT == 'M_cijfer': x_, k_ = eerste(lambda x: onthoudt(x), True, '(onthouden)'); k_['uitleg'] = 'Tel de eenheden nog eens: als ze samen 10 of meer zijn, komt er een tiental bij.'
if MUT == 'M_snap': x_, k_ = eerste(lambda x: leent(x), True, '(geleend)'); k_['uitleg'] = (k_.get('uitleg') or '') + ' Reken goed.'
snap, n_l, n_o, mis = {}, 0, 0, []
for (d, n), xs in I.items():
    if not d.startswith('G5-'): continue
    for x in xs:
        for k in x['foutHints']:
            for v in ('uitleg', 'uitlegSterker'):
                t = k.get(v) or ''
                for naam, (rx, fn) in FN.items():
                    if not rx.search(t): continue
                    if re.search(r'\d', t): F.append(f"cijfer in leen-/onthoudzin (Oef-#1049) {d} #{n} {x['nr']} sleutel {k['fout']!r} [{v}]: {t[:70]}")
                    w = fn(x); snap[f"{d}#{n} {x['nr']} {k['fout']} {v} {naam}"] = [k['soort'], w, t]
                    n_l += naam == 'leen'; n_o += naam != 'leen'
                    if w is not True: F.append(f"{'lenen' if naam == 'leen' else 'onthouden'} {d} #{n} {x['nr']} sleutel {k['fout']!r} [{v}]: {'geen ' + ('lenen' if naam == 'leen' else 'onthouden') if w is False else 'som niet te lezen'} ({x['opgave'][:50]} → {x['antwoord']}): {t[:70]}")
            # gemist: item leent/onthoudt wel, maar de sleutel kreeg de tekst zonder uitleg (motor las de som anders) → INFO
            if k['soort'].endswith(('tiental te veel', 'tiental te weinig')) and d.startswith('G5-GET-E05'):
                e = ENT.get((d, n)); 
                if e and any(f['soort'] == k['soort'] + ' (geleend)' or f['soort'] == k['soort'] + ' (onthouden)' for f in e['foutHints']):
                    if (leent(x) if 'veel' in k['soort'] else onthoudt(x)): mis.append(f"{d} #{n} {x['nr']} {k['fout']}")
# Oef-#1040
e17 = ENT.get(('G5-GET-E05', 17))
if e17 is not None:
    if any(f['soort'] == 'honderdtal vergeten' for f in e17['foutHints']): F.append("Oef-#1040 G5-GET-E05 #17: entry heeft nog 'honderdtal vergeten'")
    for x in I.get(('G5-GET-E05', 17), []):
        for k in x['foutHints']:
            if k['fout'] in ('99', '97') and (k['soort'] != 'tiental te weinig' or k.get('uitleg') != 'Dat is te weinig. Tel de tientallen nog eens bij elkaar.'):
                F.append(f"Oef-#1040 G5-GET-E05 #17 {x['nr']} sleutel {k['fout']}: {k['soort']!r} {k.get('uitleg')!r}")
            if k['fout'] in ('99', '97') and not int(k['fout']) < ant(x): F.append(f"Oef-#1040 {x['nr']}: richting")
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP lenen {k}: {oud.get(k)} → {snap.get(k)}" for k in sorted(set(oud) | set(snap)) if not _zelfde1092(oud.get(k), snap.get(k))][:20]
print(f"INFO {n_l} sleutelteksten met lenen, {n_o} met onthouden nagerekend; {len(mis)} sleutels lenen/onthouden echt maar kregen de tekst zonder uitleg (motor las de som anders): {mis[:6]}")
for f in F: print('FAIL', f)
print(f"check Z-#1090 lenen/onthouden + Oef-#1040: FAIL {len(F)}" + (f' (MUT={MUT})' if MUT else ''))
