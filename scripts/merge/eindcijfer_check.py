"""Z-#765 (Didactiek G8 batch 1; recheck Overzicht 17:39): G8-GET-E02 #1 «Op welk cijfer eindigt a × b?». Een bekende foute route mag niet op het
goede eindcijfer uitkomen: het antwoord (eindcijfer van a × b) is niet het begincijfer van het product, niet het tientallencijfer van het product
en niet (u1 + u2) mod 10 (de eenheden opgeteld) (FAIL).
Generator: zoek(a, b, ...) geeft nieuwe factoren met evenveel cijfers als het oude item, dezelfde eenheden (dus hetzelfde antwoord en dezelfde
eenheid-routes), zo dicht mogelijk bij het oude; lukt dat niet met dezelfde eenheden (064: 2 + 2 = 4 = 2 × 2), dan mag de eenheid van b anders.
'houd' = posities (factor, cijfer vanaf rechts) die gelijk moeten blijven omdat een Claude-sleutel 'getal-overgenomen' dat cijfer is.
Gebruik: import eindcijfer_check as EC; EC.fouten(a, b); EC.rapport(items); EC.zoek(a, b, bezet, houd)."""
import re, sys
RX = re.compile(r'^Op welk cijfer eindigt (\d+) × (\d+)\?$')
def fouten(a, b):
    p = a * b; ant = p % 10; s = str(p); F = []
    if int(s[0]) == ant: F.append(f'begincijfer van {p} = {ant}')
    if len(s) >= 2 and int(s[-2]) == ant: F.append(f'tientallencijfer van {p} = {ant}')
    if (a % 10 + b % 10) % 10 == ant: F.append(f'eenheden opgeteld ({a % 10} + {b % 10}) eindigt op {ant}')
    return F
def lees(it):
    m = RX.match((it.get('opgave') or '').strip())
    return (int(m.group(1)), int(m.group(2))) if m else None
def _ok_houd(a, b, a0, b0, houd):
    for f, k in houd:
        x, x0 = (a, a0) if f == 0 else (b, b0)
        if str(x).zfill(4)[-1 - k] != str(x0).zfill(4)[-1 - k]: return False
    return True
def zoek(a0, b0, bezet=(), houd=()):
    la, lb = len(str(a0)), len(str(b0))
    def kandidaten(zelfde_eenheid_b):
        for a in range(10 ** (la - 1) if la > 1 else 2, 10 ** la):
            if a % 10 != a0 % 10: continue
            for b in range(10 ** (lb - 1) if lb > 1 else 2, 10 ** lb):
                if zelfde_eenheid_b and b % 10 != b0 % 10: continue
                if b % 10 in (0, 1) or a % 10 in (0, 1): continue
                yield a, b
    for zelfde in (True, False):
        best = None
        for a, b in kandidaten(zelfde):
            if (a, b) in bezet or (b, a) in bezet or fouten(a, b) or not _ok_houd(a, b, a0, b0, houd): continue
            d = abs(a - a0) / a0 + abs(b - b0) / b0
            if best is None or d < best[0]: best = (d, a, b)
        if best: return best[1], best[2]
    raise ValueError(('Z-#765: geen nieuwe factoren', a0, b0))
def rapport(items, toon=True, ernst='FAIL'):
    F = []; n = 0
    for it in items:
        ab = lees(it)
        if not ab or (it.get('merge') or {}).get('doel') not in (None, 'G8-GET-E02'): continue
        n += 1
        if str(it.get('antwoord')) != str(ab[0] * ab[1] % 10): F.append(f"{it['id']}: antwoord {it.get('antwoord')} ≠ {ab[0] * ab[1] % 10}")
        if (f := fouten(*ab)): F.append(f"{it['id']}: {ab[0]} × {ab[1]}: {'; '.join(f)}")
    if toon:
        print(f"\nEINDCIJFER (Z-#765: geen foute route op het eindcijfer van a × b): {len(F)} ({ernst}) · items {n}")
        for x in F[:12]: print(f'  {ernst} EINDCIJFER', x)
    return len(F)
MUTANTEN = [('061 oud 19 × 17 (begincijfer)', (19, 17), True), ('065 oud 19 × 7 (tientallen)', (19, 7), True), ('064 oud 112 × 12 (u1 + u2)', (112, 12), True),
            ('019 × 27', (19, 27), False), ('063 12 × 7', (12, 7), False)]
def mutanten_ok(): return all(bool(fouten(*ab)) == v for _, ab, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, ab, v in MUTANTEN: print(('ok  ' if bool(fouten(*ab)) == v else 'MIS ') + n, fouten(*ab))
    print('mutanten EINDCIJFER:', sum(bool(fouten(*ab)) == v for _, ab, v in MUTANTEN), '/', len(MUTANTEN)); sys.exit(0 if mutanten_ok() else 1)
