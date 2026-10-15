"""les 271 (Z-#790): L2's (tekstSterker) die een kopie zijn van een óúde H2 (uit hints/wijzigingen_batchN.json) of er sterk op lijken
(SequenceMatcher > 0.75 en meer dan op de huidige H2). Uitgezonderd: een H2-wijziging waarbij de oude H2 bewust laag 2 bleef
(waarom bevat 'oude H2 blijft laag 2', V-#780 in b2). Gebruik in een check: from l271 import les271; fails += les271(G8, n[, D]).
Los: python3 l271.py [G8-map] [1,2,3]."""
import json, os, re, sys, difflib
def _norm(t): return re.sub(r'\s+', ' ', (t or '').strip().lower())
def les271(G8, n, D=None):
    P = f'{G8}/hints/batch{n}.json'; L = f'{G8}/hints/wijzigingen_batch{n}.json'
    if D is None:
        if not os.path.exists(P): return []
        D = json.load(open(P, encoding='utf-8'))
    log = json.load(open(L, encoding='utf-8')) if os.path.exists(L) else []
    oud, bewust = {}, set()
    for e in log:
        if e.get('veld') == 'hint2' and isinstance(e.get('was'), str):
            k = (e['doel'], e['nrOrigineel']); oud.setdefault(k, set()).add(_norm(e['was']))
            if 'oude H2 blijft laag 2' in (e.get('waarom') or ''): bewust.add((k, _norm(e['was'])))
    out = []
    for s in D['somtypen']:
        k = (s['doel'], s['nrOrigineel']); nu = _norm(s['hint2'])
        for f in s['foutHints']:
            l2 = _norm(f.get('tekstSterker'))
            if not l2 or l2 == nu: continue
            for o in sorted(oud.get(k, set()) - {nu}):
                if (k, o) in bewust: continue
                r = difflib.SequenceMatcher(None, l2, o).ratio(); rn = difflib.SequenceMatcher(None, l2, nu).ratio()
                if l2 == o or (r > 0.75 and r > rn):
                    out.append(f"les 271 b{n} {k[0]} nrO{k[1]} [{f['soort']}]: L2 is een kopie van een oude H2 ({'gelijk' if l2 == o else f'lijkt {r:.2f}, op de huidige H2 {rn:.2f}'}): {f['tekstSterker'][:90]}")
                    break
    return out
if __name__ == '__main__':
    G = sys.argv[1] if len(sys.argv) > 1 else __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..')
    tot = 0
    for n in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['1', '2', '3']):
        for m in les271(G, n): print(m); tot += 1
    print(f'les 271: {tot}')
