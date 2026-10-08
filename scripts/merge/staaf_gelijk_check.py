#!/usr/bin/env python3
"""V-#665 (review batch 5 Didactiek): vraagt een item naar de hoogste/laagste staaf (of het grootste/kleinste getal in een tabel of staafdiagram),
dan moet die waarde uniek zijn. FAIL bij een gelijke hoogste of laagste waarde. Gebruik: staaf_gelijk_check.py <gemapt.json> [--info]
(--info: alleen tellen, geen FAIL; voor de goedgekeurde G5/G6)."""
import json, re, sys
HOOG = re.compile(r'\b(hoogst|hoogste|grootste|meeste)\b', re.I); LAAG = re.compile(r'\b(laagst|laagste|kleinste|minste)\b', re.I)
def waarden(jr):
    if not isinstance(jr, dict): return None
    if jr.get('soort') == 'staafdiagram':
        return [s.get('waarde') for s in jr.get('staven') or [] if isinstance(s, dict) and isinstance(s.get('waarde'), (int, float))]
    if jr.get('soort') == 'tabel' and len(jr.get('rijen') or []) == 1:
        return [v for v in jr['rijen'][0].get('waarden') or [] if isinstance(v, (int, float))]
    return None
def fouten(items):
    out = []
    for it in items:
        o = it.get('opgave') or ''
        w = waarden((it.get('visual') or {}).get('jsRender'))
        if not w or len(w) < 2: continue
        for rx, f, naam in ((HOOG, max, 'hoogste'), (LAAG, min, 'laagste')):
            if rx.search(o) and w.count(f(w)) > 1: out.append((it['id'], naam, f(w), w))
    return out
if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); items = d['items'] if isinstance(d, dict) else d
    f = fouten(items); info = '--info' in sys.argv
    for x in f: print(('INFO' if info else 'FAIL'), 'V-#665 gelijke %s staaf: %s (waarde %s in %s)' % (x[1], x[0], x[2], x[3]))
    print(f"V-#665 staaf-check: {len(f)} {'(INFO)' if info else '(FAIL)'}")
    sys.exit(1 if f and not info else 0)
