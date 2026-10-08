#!/usr/bin/env python3
"""Oef-#459 / Z-#711 (Overzicht 8 okt, les 205/206): WARN als in een somtype met minstens 4 meerkeuze-items het goede antwoord in meer
dan 60% van de items op dezelfde plek staat. Plek = rang op waarde (kleinste/middelste/grootste) als elke optie een getal is (de app
husselt de letters, dus 'kies de middelste' is de vuistregel); anders de letter, maar alleen als het item niet gehusseld wordt.
Gebruik: rapport(items) → aantal somtypes met WARN (check_merge_notatie G7/G8)."""
import collections, re
from fractions import Fraction as F
_G = re.compile(r'^[€\s]*(−|-)?(\d+(?:[.,]\d+)?)')
def _waarde(t):
    m = _G.match(str(t))
    if not m or not re.fullmatch(r'[€\s]*[−-]?\d+(?:[.,]\d+)?\s*(%|[a-zA-Z²³]+)?', str(t).strip()): return None
    v = F(m.group(2).replace('.', '').replace(',', '.')) if re.fullmatch(r'\d{1,3}(\.\d{3})+', m.group(2)) else F(m.group(2).replace(',', '.'))
    return -v if m.group(1) else v
def plek(it):
    ops = [o['tekst'] for o in it.get('opties') or []]; goed = (it.get('antwoordDetail') or {}).get('juisteOptieTekst') or str(it.get('antwoord'))
    if goed not in ops: return None
    w = [_waarde(t) for t in ops]
    if all(x is not None for x in w) and len(set(w)) == len(w):
        r = sorted(w).index(w[ops.index(goed)])
        return 'kleinste' if r == 0 else ('grootste' if r == len(w) - 1 else 'midden')
    if it.get('husselen') is True: return None
    return 'letter ' + (it.get('antwoordDetail') or {}).get('juisteOptie', '?')
def fouten(items, min_items=4, grens=0.6):
    per = collections.defaultdict(list)
    for it in items:
        if not it.get('opties') or re.search(r'\b(grootst|kleinst|hoogst|laagst|meeste|minste)\b', it.get('opgave') or ''): continue   # daar is de plek de vraag zelf
        p = plek(it)
        if p: m = it.get('merge') or {}; per[(m.get('doel'), m.get('somtype'))].append(p)
    out = []
    for k, ls in sorted(per.items(), key=str):
        if len(ls) < min_items: continue
        l, n = collections.Counter(ls).most_common(1)[0]
        if n / len(ls) > grens: out.append((k[0], k[1], l, n, len(ls)))
    return out
def rapport(items):
    f = fouten(items)
    print(f"\nOef-#459 plek van het goede antwoord (≥4 items, >60% op één plek): {len(f)} somtypes (WARN)")
    for d, s, l, n, t in f: print(f"  WARN Oef-#459 {d} '{s}': {n} van {t} {l}")
    return len(f)
