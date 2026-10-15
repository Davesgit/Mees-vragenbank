#!/usr/bin/env python3
"""V-#1013 bewijs (les 321): de gates uit de vaste groepscheck vuren op de oude data. VORMCUE (V-#1050–#1055 rang; V-#1040 middelste) erbij.
Oude data: base = merge-base 482a19f (vóór de kloktijdronde), snap = 983900d (r13 vóór deel B); nu = r13-werkmap. Read-only."""
import sys, json, glob, os, subprocess
sys.path.insert(0, '/workspace/claude-merge/tools')
import kloktijd_check as KT, juiste_optie_check as JO, gemiddelde_check as GM, vormcue_check as VC
STANDEN = {'base 482a19f': '/workspace/r13work/base/claude-aanvulling/groep{g}', 'snap 983900d': '/workspace/r13work/snap/claude-aanvulling/groep{g}', 'nu': '/workspace/claude-merge/r13/g{g}'}
uit = {}
for naam, pad in STANDEN.items():
    for g in (3, 4, 5, 6, 7):
        b = pad.format(g=g); its = [i for p in sorted(glob.glob(f'{b}/data/per_doel/G{g}-*.json')) for i in json.load(open(p, encoding='utf-8'))['items']]
        if not its: continue
        Fl, W, _ = GM.analyse(its, b)
        r = {'items': len(its), 'KLOKTIJD': len(KT.treffers(its)), 'TIJDSDUUR': len(KT.duur_treffers(its)), 'KLOKWOORD': len(KT.dubbelepunt_treffers(its)),
             'KLOKSLEUTEL': len(KT.klokvorm_treffers(its)), 'TYPVOORBEELD': len(KT.typvoorbeeld_treffers(its)), 'JUISTE-OPTIE': len(JO.fouten(its)),
             'OPTIESTEKST': len(JO.tekst_fouten(its)), 'OPTIESTEKST-items': len({x.split(':')[0] for x in JO.tekst_fouten(its)}), 'GEMIDDELDE': len(Fl), 'GEMIDDELDE-WARN': len(W), 'GEMIDDELDE-SAMEN': len(GM.samen_treffers(its))}
        vf = VC.fouten(its); r.update({'VORMCUE': len(vf), 'VORMCUE-rang': len([x for x in vf if 'middelste' not in x]), 'VORMCUE-midden': len([x for x in vf if 'middelste' in x]), 'VORMCUE-somtypes': vf})      # V-#1050–#1055 (rang), V-#1040 (middelste)
        uit[f'{naam} G{g}'] = r
mut = {'tijdsduur': f'{KT.mutanten()}/{len(KT.MUTANTEN)}', 'V-#1012': f'{KT.mutanten1012()}/2', 'typvoorbeeld': KT.typvoorbeeld_mutant_ok(),
       'optiesTekst': JO.mutanten_ok(), 'vormcue': f'{sum(VC._mut_ok(n_, L, v) for n_, L, v in VC.MUTANTEN)}/{len(VC.MUTANTEN)}', 'vormcue-zacht': f'{sum(VC.mutanten_z_ok())}/{len(VC.MUTANTEN_Z)}', 'samen': GM.samen_mutanten_ok(), 'gemiddelde': [(n, v, k) for n, v, k in GM.mutanten()]}
v12 = {}
for naam, pad in (('snap 983900d', '/workspace/r13work/snap/claude-aanvulling/groep5'), ('nu', '/workspace/claude-merge/r13/g5')):
    r = subprocess.run([sys.executable, '-B', '/workspace/claude-merge/r13/g5/scripts/check_v1012.py', pad], capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    v12[naam] = (r.stdout.strip().splitlines() or ['?'])[-1]
json.dump({'standen': uit, 'mutanten': mut, 'check_v1012': v12}, open('/workspace/claude-merge/r13/bewijs_v1013.json', 'w'), ensure_ascii=False, indent=1)
K = ['KLOKTIJD', 'TIJDSDUUR', 'KLOKWOORD', 'KLOKSLEUTEL', 'TYPVOORBEELD', 'JUISTE-OPTIE', 'OPTIESTEKST-items', 'GEMIDDELDE', 'GEMIDDELDE-SAMEN', 'VORMCUE-rang', 'VORMCUE-midden']
print('stand'.ljust(18) + ' '.join(k[:12].rjust(12) for k in K))
for n, r in uit.items(): print(n.ljust(18) + ' '.join(str(r[k]).rjust(12) for k in K))
print('mutanten', {k: v for k, v in mut.items() if k != 'gemiddelde'}, 'gemiddelde', sum(v == k for _, v, k in mut['gemiddelde']), '/', len(mut['gemiddelde']))
print('check_v1012', v12)
