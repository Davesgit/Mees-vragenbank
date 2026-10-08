#!/usr/bin/env python3
"""Z-#520 (review G7 batch 1, Didactiek 8 okt; les 145/146) + Z-#562 (recheck batch 1): eenvoudige rekenroutes op de getallen uit de vraag.
- DUBBEL: een afleider (foute optie) is te bereiken met meer dan één route → laag 1 moet bij elke route passen, of kies andere getallen.
- ZWAK: het goede antwoord is ook te bereiken met een foute route (een denkfout die toevallig klopt).
Routes (getallen in de volgorde van de vraag; labels na 'stap'/'dag' tellen niet): een getal overnemen; a + b, a − b, a × b, a : b;
en voor drie getallen alle vormen (a ∘ b) ∘ c en a ∘ (b ∘ c) met + − ×.
Z-#562 (minder bijvangst, les 160/161): een route telt alleen als hij bij een denkfout-patroon past:
- een getal uit de vraag overnemen;
- bij twee getallen: elke bewerking met die twee (verkeerde bewerking, omgedraaid);
- bij drie getallen: de goede vorm met één andere bewerking (verkeerde bewerking), of de eerste stap van de goede vorm (stap twee vergeten);
  kent de vraag geen goede vorm met alle drie de getallen, dan tellen alle paren.
Losse sommen zonder patroon (4 + 3 bij een keersom-vraag, 2 × 2, a × a) tellen niet. Een tussenstap 1 (bij × of :) of 0 (bij + of −) is geen
route (zoals ×1 en +0). De goede route zelf is geen ZWAK (gebruikt de goede som niet alle getallen, dan telt de goede som met twee); een getal uit de vraag in de
antwoordvorm ('3 op de 5', schaal 1 : 50 → 50 cm) ook niet.
Alleen INFO: de teksten passen we niet zelf aan. Gebruik: rapport(items, toon, log) → lijst (soort, id, opgave, waarde, routes); log = pad
voor een JSON-lijst met alle meldingen per stuk."""
import re, itertools, json
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
def _nut(o, b): return b is not None and not ((o in '+−' and b == 0) or (o in '×:' and b == 1))      # +0, −0, ×1, :1 is geen route
def routes2(ns):
    """{waarde: [(tekst, meta)]}; meta = ('kopie', i) | ('kwadraat', i) | ('paar', i, j, o) | ('drie', vorm, o1, o2)."""
    r = {}
    def zet(v, s, meta):
        if v is not None and v >= 0 and s not in [x[0] for x in r.get(v, [])]: r.setdefault(v, []).append((s, meta))
    for i, a in enumerate(ns):
        if a != 0: zet(a, f'{_f(a)} uit de vraag', ('kopie', i))
        if a > 1: zet(a * a, f'{_f(a)} × {_f(a)}', ('kwadraat', i))
    for (i, a), (j, b) in itertools.permutations(enumerate(ns), 2):
        for o in ('+', '×'):
            if i < j and _nut(o, b) and _nut(o, a): zet(OPS[o](a, b), f'{_f(a)} {o} {_f(b)}', ('paar', i, j, o))
        if _nut('−', b): zet(OPS['−'](a, b), f'{_f(a)} − {_f(b)}', ('paar', i, j, '−'))
        v = OPS[':'](a, b)
        if v is not None and v.denominator == 1 and _nut(':', b): zet(v, f'{_f(a)} : {_f(b)}', ('paar', i, j, ':'))
    if len(ns) == 3:
        a, b, c = ns
        for o1, o2 in itertools.product('+−×', repeat=2):
            t = OPS[o1](a, b)
            if _nut(o1, b) and not (o1 in '+×' and not _nut(o1, a)) and _nut(o2, c) and not (o2 in '+×' and not _nut(o2, t)) and not (o2 == '×' and t == 0):
                zet(OPS[o2](t, c), f'({_f(a)} {o1} {_f(b)}) {o2} {_f(c)}' if o1 in '+−' and o2 == '×' else f'{_f(a)} {o1} {_f(b)} {o2} {_f(c)}', ('drie', 1, o1, o2))
            if (o1, o2) in {('+', '+'), ('+', '−'), ('−', '+'), ('×', '×')}: continue      # gelijk aan de eerste vorm (of a − b − c)
            u = OPS[o2](b, c)
            if _nut(o2, c) and not (o2 in '+×' and not _nut(o2, b)) and _nut(o1, u) and not (o1 in '+×' and not _nut(o1, a)) and not (o1 == '×' and u == 0):
                zet(OPS[o1](a, u), f'{_f(a)} {o1} {_f(b)} × {_f(c)}' if o2 == '×' else f'{_f(a)} {o1} ({_f(b)} {o2} {_f(c)})', ('drie', 2, o1, o2))
    return r
def routes(ns): return {k: [s for s, _ in v] for k, v in routes2(ns).items()}
def _goed(R2, g, n):
    """De goede vorm(en): routes op het goede antwoord die alle getallen gebruiken."""
    return [m for s, m in R2.get(g, []) if (n == 3 and m[0] == 'drie') or (n == 2 and m[0] == 'paar') or (n == 1 and m[0] == 'kopie')]
def _patroon(m, goed, n):
    if m[0] == 'kopie': return True
    if m[0] == 'kwadraat': return False
    if n == 2: return m[0] == 'paar'
    if n == 3:
        drie = [gm for gm in goed if gm[0] == 'drie']
        if not drie: return m[0] == 'paar'
        for gm in drie:
            if m[0] == 'drie' and m[1] == gm[1] and (m[2] != gm[2]) + (m[3] != gm[3]) == 1: return True
            if m[0] == 'paar' and m[3] == gm[2] and ((gm[1] == 1 and m[1:3] == (0, 1)) or (gm[1] == 2 and m[1:3] == (1, 2))): return True
    return False
def meldingen(it):
    uit = []
    if it.get('type') != 'meerkeuze' or not it.get('opties'): return uit
    ns = getallen(it['opgave'])
    if not ns or len(ns) > 3: return uit
    R2 = routes2(ns); g = waarde(it['antwoord'])
    goed = _goed(R2, g, len(ns)) if g is not None else []
    if g is not None and not goed: goed = [m for s, m in R2.get(g, []) if m[0] == 'paar']      # de goede som gebruikt niet alle getallen (begin bij 0, schaal 1 : n)
    sch = re.search(r'schaal 1\s?:\s?(\d+)', it['opgave'])
    if g is not None and sch and F(sch.group(1)) == g: goed = goed + [m for s, m in R2.get(g, []) if m[0] == 'kopie']      # schaal 1 : n → 1 cm is n cm: de antwoordvorm
    for o in it['opties']:
        v = waarde(o['tekst'])
        if v is None: continue
        rs = [s for s, m in R2.get(v, []) if _patroon(m, goed, len(ns))]
        if o['tekst'] == it['antwoord']:
            if re.search(r'\bop de\b', o['tekst']): continue      # antwoordvorm 'zoveel op de zoveel': het getal uit de vraag hoort erbij
            fout = [s for s, m in R2.get(v, []) if _patroon(m, goed, len(ns)) and m not in goed]
            if fout: uit.append(('ZWAK', it['id'], it['opgave'], o['tekst'], fout))
        elif len(rs) > 1: uit.append(('DUBBEL', it['id'], it['opgave'], o['tekst'], rs))
    return uit
def rapport(items, toon=True, log=None, kop='ROUTES'):
    uit = [x for it in items for x in meldingen(it)]
    if log: json.dump([{'soort': x[0], 'id': x[1], 'opgave': x[2], 'optie': x[3], 'routes': x[4]} for x in uit], open(log, 'w'), ensure_ascii=False, indent=1)
    if toon:
        print(f"\n{kop} (Z-#520/Z-#562: twee routes op één afleider / een foute route op het goede antwoord): DUBBEL {sum(1 for x in uit if x[0] == 'DUBBEL')} · ZWAK {sum(1 for x in uit if x[0] == 'ZWAK')} (INFO)")
        for x in uit: print(f"  INFO {x[0]} {x[1]} '{x[3]}': {' / '.join(x[4])}")
    return uit
