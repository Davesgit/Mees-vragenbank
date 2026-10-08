#!/usr/bin/env python3
"""Z-#520 (review G7 batch 1, Didactiek 8 okt; les 145/146): eenvoudige rekenroutes op de getallen uit de vraag.
- DUBBEL: een afleider (foute optie) is te bereiken met meer dan één route → laag 1 moet bij elke route passen, of kies andere getallen.
- ZWAK: het goede antwoord is te bereiken met twee routes, of met a × a of een getal uit de vraag (een denkfout die toevallig klopt).
Routes (getallen in de volgorde van de vraag; labels na 'stap'/'dag' tellen niet): een getal overnemen; a + b, a − b, a × b, a : b;
a × a; en voor drie getallen alle vormen (a ∘ b) ∘ c en a ∘ (b ∘ c) met + − ×. Alleen INFO: de teksten passen we niet zelf aan.
Gebruik: rapport(items) → lijst (soort, id, opgave, waarde, routes)."""
import re, itertools
from fractions import Fraction as F
OPS = {'+': lambda a, b: a + b, '−': lambda a, b: a - b, '×': lambda a, b: a * b, ':': lambda a, b: a / b if b else None}
def getallen(opgave):
    o = re.sub(r'\b([Ss]tap|[Dd]ag)\s+\d+', '', opgave)
    o = re.sub(r'(\d)\.(\d{3})\b', r'\1\2', o)
    return [F(x.replace(',', '.')) for x in re.findall(r'\d+(?:,\d+)?', o)]
def waarde(t):
    t = str(t)
    if '=' in t: t = t.split('=')[-1]
    elif re.search(r'[×−+:]| over\b', t): return None          # een som of 'zoveel, zoveel over' is geen getal
    m = re.match(r'\s*(?:Elk\s+)?(\d+(?:,\d+)?)', str(t))
    return F(m.group(1).replace(',', '.')) if m else None
def _f(x): return str(int(x)) if x.denominator == 1 else str(float(x))
def routes(ns):
    r = {}
    def zet(v, s):
        if v is not None and v >= 0: r.setdefault(v, []).append(s)
    def nut(o, b): return not ((o in '+−' and b == 0) or (o in '×:' and b == 1))      # +0, −0, ×1, :1 is geen route
    for a in dict.fromkeys(ns):
        if a != 0: zet(a, f'{_f(a)} uit de vraag')
        if a > 1: zet(a * a, f'{_f(a)} × {_f(a)}')
    for a, b in itertools.permutations(ns, 2):
        if 0 in (a, b) and False: pass
        for o in ('+', '×'):
            if (ns.index(a) < ns.index(b) or a == b) and nut(o, b) and nut(o, a): zet(OPS[o](a, b), f'{_f(a)} {o} {_f(b)}')
        if nut('−', b): zet(OPS['−'](a, b), f'{_f(a)} − {_f(b)}')
        v = OPS[':'](a, b)
        if v is not None and v.denominator == 1 and nut(':', b): zet(v, f'{_f(a)} : {_f(b)}')
    if len(ns) == 3:
        a, b, c = ns
        for o1, o2 in itertools.product('+−×', repeat=2):
            if nut(o1, b) and nut(o2, c) and not (o1 in '+×' and not nut(o1, a)):
                zet(OPS[o2](OPS[o1](a, b), c), f'({_f(a)} {o1} {_f(b)}) {o2} {_f(c)}' if o1 in '+−' and o2 == '×' else f'{_f(a)} {o1} {_f(b)} {o2} {_f(c)}')
            if (o1, o2) in {('+', '+'), ('+', '−'), ('−', '+'), ('×', '×')}: continue      # gelijk aan de eerste vorm (of a − b − c)
            if nut(o2, c) and nut(o1, OPS[o2](b, c)) and not (o1 in '+×' and not nut(o1, a)):
                zet(OPS[o1](a, OPS[o2](b, c)), f'{_f(a)} {o1} {_f(b)} × {_f(c)}' if o2 == '×' else f'{_f(a)} {o1} ({_f(b)} {o2} {_f(c)})')
    return {k: list(dict.fromkeys(v)) for k, v in r.items()}
def _zwak(rs): return len(rs) > 1 or any(x.endswith('uit de vraag') or re.fullmatch(r'(\S+) × \1', x) for x in rs)
def rapport(items, toon=True):
    uit = []
    for it in items:
        if it.get('type') != 'meerkeuze' or not it.get('opties'): continue
        ns = getallen(it['opgave'])
        if not ns or len(ns) > 3: continue
        R = routes(ns); goed = waarde(it['antwoord'])
        for o in it['opties']:
            v = waarde(o['tekst'])
            if v is None: continue
            rs = R.get(v, [])
            if o['tekst'] == it['antwoord']:
                if _zwak(rs): uit.append(('ZWAK', it['id'], it['opgave'], o['tekst'], rs))
            elif len(rs) > 1: uit.append(('DUBBEL', it['id'], it['opgave'], o['tekst'], rs))
    if toon:
        print(f"\nROUTES (Z-#520: twee routes op één afleider / een foute route op het goede antwoord): DUBBEL {sum(1 for x in uit if x[0] == 'DUBBEL')} · ZWAK {sum(1 for x in uit if x[0] == 'ZWAK')} (INFO)")
        for x in uit: print(f"  INFO {x[0]} {x[1]} '{x[3]}': {' / '.join(x[4])}")
    return uit
