#!/usr/bin/env python3
"""Didactiek 19:57: stand per somtype voor de positieregel (kleinste/middelste/grootste, > 50 % met p < 0,01 = FAIL).
Per somtype: n, aantal goed op elke positie, zonder positie, en het minimale aantal items dat moet wisselen (één afleider vervangen) om
(a) de regel niet meer te laten vuren en (b) strikt onder 50 % te komen, zonder dat een andere positie onder ~10 % zakt (Z-#1052).
Gebruik: python3 vormcue_posities.py <groepmap> [<groepmap> ...] [--alle]   (zonder --alle alleen somtypen met een positie-FAIL)"""
import json, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import vormcue_check as VC
NM = {'klein': 'kleinste', 'midden': 'middelste', 'groot': 'grootste'}
def rijen(base, alle=False):
    items = [x for p in sorted(glob.glob(os.path.join(base, 'data', 'per_doel', '*.json'))) for x in json.load(open(p, encoding='utf-8'))['items']]
    uit = []
    for k, t in sorted(VC.posities(items).items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
        f = [h for h in VC.POSITIES if VC.fail_regel(t['n'], t[h])]
        if not (f or alle): continue
        uit.append((k, t, f, VC.min_wissel(t, ondergrens=0), VC.min_wissel(t), VC.min_wissel(t, ondergrens=0, strikt=True), VC.min_wissel(t, strikt=True)))
    return uit
if __name__ == '__main__':
    alle = '--alle' in sys.argv
    for base in [a for a in sys.argv[1:] if not a.startswith('--')]:
        for k, t, f, r0, r1, s0, s1 in rijen(base, alle):
            n = t['n']; pc = lambda m: f'{m}/{n} ({100 * m / n:.1f} %)'
            print(f"{k[0]} #{k[1]}: n={n} · kleinste {pc(t['klein'])} · middelste {pc(t['midden'])} · grootste {pc(t['groot'])} · geen positie {t['geen']}"
                  + (f" · FAIL: {', '.join(NM[h] for h in f)}" if f else ' · geen FAIL'))
            if f:
                v = lambda r: f"{r[0]} items → {' / '.join(f'{NM[h]} {r[1][h]}' for h in VC.POSITIES)}"
                print(f"   tot ≤ 50 % (regel vuurt niet meer): zonder ondergrens {v(r0)} · met elke positie ≥ 10 % {v(r1)}")
                print(f"   tot < 50 % (strikt):                zonder ondergrens {v(s0)} · met elke positie ≥ 10 % {v(s1)}")
