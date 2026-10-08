"""Oef-#1000 / V-#891 (G8 batch 6, Didactiek 16:54; les 306/317): vol bouwwerk van blokjes (jsRender soort 'bouwsel': diep, hoog, breed; antwoord = d × h × b).
Geen foute route mag het goede antwoord geven. Routes (zoals b6/check): de maten opgeteld, een laag te veel/te weinig, één laag (de bovenkant), drie kanten
(d·b + b·h + d·h: valt op het antwoord bij 3×3×3, 2×4×4 en 2×3×6), de zichtbare blokjes, een rij te weinig (breed of diep). 'De helft' telt niet (is nooit gelijk).
Gebruik: import bouwsel_routes as BR; BR.rapport(items) → aantal FAIL (build-gate); BR.fouten(d, h, b) → lijst; python3 bouwsel_routes.py --mutanten"""
import sys
def routes(d, h, b):
    return {'som': d + h + b, 'laag te veel': d * b * (h + 1), 'laag te weinig': d * b * (h - 1), 'één laag': d * b, 'drie kanten': d * b + b * h + d * h,
            'zichtbaar': d * b + b * h + d * h - d - b - h + 1, 'rij te weinig (breed)': (b - 1) * d * h, 'rij te weinig (diep)': (d - 1) * b * h}
def fouten(d, h, b, antwoord=None):
    a = d * h * b; F = []
    if antwoord is not None and str(antwoord) != str(a): F.append(f'antwoord {antwoord} ≠ {d}×{h}×{b} = {a}')
    if h < 2: F.append('minder dan twee lagen')
    for r, v in routes(d, h, b).items():
        if v == a: F.append(f"route '{r}' geeft het goede antwoord {a} ({d}×{h}×{b})")
    return F
def fouten_item(it):
    jr = (it.get('visual') or {}).get('jsRender') or {}
    if jr.get('soort') != 'bouwsel': return None
    F = fouten(jr['diep'], jr['hoog'], jr['breed'], it.get('antwoord'))
    a = jr['diep'] * jr['hoog'] * jr['breed']; ops = [o.get('tekst') for o in it.get('opties') or []]
    if ops and (len(set(ops)) != len(ops) or str(a) not in ops): F.append(f'opties {ops}: dubbel of zonder het antwoord')
    return F
def rapport(items, toon=True, ernst='FAIL'):
    F = []; n = 0
    for it in items:
        f = fouten_item(it)
        if f is None: continue
        n += 1
        if f: F.append(f"{it['id']}: {'; '.join(f)}")
    if toon:
        print(f"\nBOUWSEL (Oef-#1000/V-#891: vol bouwwerk, geen foute route op het goede antwoord): {len(F)} ({ernst}) · items {n}")
        for x in F[:15]: print(f'  {ernst} BOUWSEL', x)
    return len(F)
MUTANTEN = [('oud 007 (2×6×3)', (2, 6, 3), True), ('oud 047 (4×2×4)', (4, 2, 4), True), ('oud 066 (3×3×3)', (3, 3, 3), True),
            ('nieuw 007 (3×4×3)', (3, 4, 3), False), ('nieuw 066 (2×7×2)', (2, 7, 2), False), ('één laag (3×1×4)', (3, 1, 4), True)]
if __name__ == '__main__' and '--mutanten' in sys.argv:
    ok = 0
    for naam, m, verwacht in MUTANTEN:
        kreeg = bool(fouten(*m)); ok += kreeg == verwacht; print(('ok  ' if kreeg == verwacht else 'MIS ') + f'{naam}: {fouten(*m)}')
    print(f'mutanten BOUWSEL: {ok}/{len(MUTANTEN)}'); sys.exit(0 if ok == len(MUTANTEN) else 1)
