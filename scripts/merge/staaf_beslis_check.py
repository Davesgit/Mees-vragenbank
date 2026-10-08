"""V-#893 / V-#894 (Didactiek G8 batch 6, 16:54): staafdiagram met percentages (jsRender soort 'staafdiagram', perstreep 10) en een bewering eronder.
V-#893  'Meer dan de helft … kiest X' / 'Water en X zijn samen meer dan de helft': het antwoord mag niet afhangen van het aflezen van een half streepje.
        Elke beslissende staaf tussen twee streepjes wordt naar beneden én naar boven afgelezen; alle uitkomsten moeten aan dezelfde kant van 50 liggen
        geven (meer dan 50 of niet) (FAIL). Zo vallen 55 (50/60) en water 25 + melk 30 (50/60) af, en blijven 35 (030: 30/40) en 65 (60/70) staan, zoals
        Didactiek 030 en 039 'duidelijk genoeg' vond; halve streepjes bij staven die niet beslissen mogen.
        Les 326 (Oefeningen b7, Oef-#1003): staat een beslissende staaf op een half streepje, dan mag geen aflezing minder dan een streepje van 50 liggen
        (029 hond 25 + kat 15 = 40 → 30/40/50: FAIL).
V-#894  '"N kinderen kozen X." Klopt dat?' (antwoord 'Dat kun je hier niet zien.'): N × 100 / percentage van X is een heel getal (anders is 'Nee' af te leiden) (FAIL).
Gebruik: import staaf_beslis_check as SB; SB.rapport(items) → aantal FAIL; python3 staaf_beslis_check.py --mutanten"""
import re, sys, copy, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import g8_b7_vlag as _B7VLAG; LES326 = _B7VLAG.ACTIEF      # les 326 gaat live met de b7-data (V-#945)
except ImportError: LES326 = True
from fractions import Fraction as Fr
def fouten_item(it):
    jr = (it.get('visual') or {}).get('jsRender') or {}
    if jr.get('soort') != 'staafdiagram' or 'toont percentages' not in (it.get('opgave') or ''): return None
    sv = {s['naam']: s['waarde'] for s in jr.get('staven') or []}; ps = jr.get('perstreep') or 10; o = it['opgave']; F = []
    m1 = re.search(r'"Meer dan de helft van [\w ]+ kiest (\w+)\."', o); m2 = re.search(r'"(\w+) en (\w+) zijn samen meer dan de helft\."', o)
    m3 = re.search(r'"(\d+) kinderen kozen (\w+)\."', o)
    if m1 or m2:
        namen = [m1.group(1)] if m1 else [m2.group(1).lower(), m2.group(2)]
        ws = [sv.get(x) for x in namen]
        if any(w is None for w in ws): F.append('beslissende staaf niet gevonden')
        else:
            import itertools
            lezingen = [{w} if w % ps == 0 else {w - w % ps, w - w % ps + ps} for w in ws]
            uit = {sum(c) for c in itertools.product(*lezingen)}
            if len({u > 50 for u in uit}) > 1: F.append(f"beslissende waarde {'+'.join(map(str, ws))} = {sum(ws)}: met een half streepje anders afgelezen {sorted(uit)} (V-#893)")
            elif LES326 and any(w % ps for w in ws) and any(abs(u - 50) < ps for u in uit): F.append(f"beslissende waarde {'+'.join(map(str, ws))} = {sum(ws)}: met een half streepje afgelezen {sorted(uit)}, een aflezing ligt minder dan een streepje van 50 (les 326, Oef-#1003)")
    if m3:
        n, x = int(m3.group(1)), m3.group(2); p = sv.get(x)
        if not p: F.append(f'staaf {x!r} niet gevonden of 0')
        elif (Fr(n * 100, p)).denominator != 1: F.append(f'{n} kinderen bij {p}% geeft totaal {float(Fr(n * 100, p)):.1f}: geen heel totaal (V-#894)')
    return F
def rapport(items, toon=True, ernst='FAIL'):
    F = []; n = 0
    for it in items:
        f = fouten_item(it)
        if f is None: continue
        n += 1
        if f: F.append(f"{it['id']}: {'; '.join(f)}")
    if toon:
        print(f"\nSTAAF-BESLIS (V-#893 beslissende staaf op een heel streepje, V-#894 aantal bij een heel totaal): {len(F)} ({ernst}) · items {n}")
        for x in F[:15]: print(f'  {ernst} STAAF-BESLIS', x)
    return len(F)
def _it(o, staven): return {'id': 'mut', 'opgave': 'Elk streepje is 10.\nDit staafdiagram heet "X" en toont percentages. Eronder staat: ' + o, 'visual': {'jsRender': {'soort': 'staafdiagram', 'perstreep': 10, 'staven': [{'naam': k, 'waarde': v} for k, v in staven.items()]}}}
MUTANTEN = [('025 fiets 55', _it('"Meer dan de helft van de kinderen kiest fiets." Klopt dat?', {'fiets': 55, 'lopend': 20, 'auto': 5, 'bus': 20}), True),
            ('025 fiets 60', _it('"Meer dan de helft van de kinderen kiest fiets." Klopt dat?', {'fiets': 60, 'lopend': 20, 'auto': 5, 'bus': 15}), False),
            ('040 water 25 + melk 30', _it('"Water en melk zijn samen meer dan de helft." Klopt dat?', {'water': 25, 'melk': 30, 'sap': 5, 'niets': 40}), True),
            ('029 hond 25 + kat 15 (les 326)', _it('"Hond en kat zijn samen meer dan de helft." Klopt dat?', {'hond': 25, 'kat': 15, 'konijn': 15, 'vis': 45}), LES326),
            ('029 hond 30 + kat 10 (V-#945)', _it('"Hond en kat zijn samen meer dan de helft." Klopt dat?', {'hond': 30, 'kat': 10, 'konijn': 15, 'vis': 45}), False),
            ('030 35 (Didactiek: duidelijk genoeg)', _it('"Meer dan de helft van de kinderen kiest fiets." Klopt dat?', {'fiets': 35, 'lopend': 30, 'auto': 15, 'bus': 20}), False),
            ('027 terug naar 12', _it('"12 kinderen kozen vis." Klopt dat?', {'hond': 20, 'kat': 25, 'konijn': 10, 'vis': 45}), True),
            ('027 wordt 9', _it('"9 kinderen kozen vis." Klopt dat?', {'hond': 20, 'kat': 25, 'konijn': 10, 'vis': 45}), False)]
if __name__ == '__main__' and '--mutanten' in sys.argv:
    ok = 0
    for naam, it, verwacht in MUTANTEN:
        f = fouten_item(it); kreeg = bool(f); ok += kreeg == verwacht; print(('ok  ' if kreeg == verwacht else 'MIS ') + f'{naam}: {f}')
    print(f'mutanten STAAF-BESLIS: {ok}/{len(MUTANTEN)}'); sys.exit(0 if ok == len(MUTANTEN) else 1)
