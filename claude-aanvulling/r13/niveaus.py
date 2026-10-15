"""r13 (Leerlijn-besluit ronde 10, BESLUIT_R9-4_R10_NIVEAUS.md §B): niveau uit een kenmerk dat in de opgave (of visual.jsRender) staat.
classificeer(it, doel, nrO) → ('basis' | 'toepassen' | None, kenmerk). None = het kenmerk zegt niets duidelijks: het niveau blijft."""
import re
from fractions import Fraction as F

def _int(s): return int(str(s).replace('.', ''))
def _getallen(o): return [x for x in re.findall(r'(?<![\d,])\d{1,3}(?:\.\d{3})+(?![\d,])|(?<![\d,.])\d+(?:,\d+)?(?![\d.])', o)]
MAAND = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']

def _leent(a, b):
    """aantal kolommen waarin geleend wordt bij a − b, en of het aftrektal een nul heeft"""
    n = 0; br = 0; A = str(a)[::-1]; B = str(b)[::-1]
    for k in range(len(A)):
        x = int(A[k]) - br; y = int(B[k]) if k < len(B) else 0
        if x < y: n += 1; br = 1
        else: br = 0
    return n, '0' in str(a)
def _onthoudt(a, m):
    """aantal kolommen met onthouden bij a × m (m één cijfer)"""
    n = 0; c = 0
    for d in str(a)[::-1]:
        p = int(d) * m + c; c = p // 10
        if c: n += 1
    return n

def kale_omreken(o):
    return re.fullmatch(r'[\d.,]+ \w+ = □ \w+', o.strip()) is not None

def classificeer(it, doel, nro):
    o = it['opgave'].strip(); a = str(it['antwoord']); jr = it['visual'].get('jsRender') or {}
    key = (doel, nro)
    if key == ('G6-GET-E01', 1) or key == ('G6-GET-E01', 2):
        n = _int(re.search(r'Rond ([\d.]+) af', o).group(1)); stap = 1000 if nro == 1 else 100
        cijfer = (n // (stap // 10)) % 10; r = _int(a)
        groot = 10000 if nro == 1 else 1000
        over = n // groot != r // groot
        if 1000 <= n <= 9999 and cijfer != 5 and not over: return 'basis', f'4 cijfers, {"honderd" if nro == 1 else "tien"}talcijfer {cijfer}, geen overgang'
        return 'toepassen', ('5 cijfers' if n >= 10000 else (f'cijfer 5' if cijfer == 5 else 'overgang'))
    if key == ('G6-GET-E03', 4):
        m = re.fullmatch(r'Schrijf (\d+)/(\d+) met noemer (\d+)\.', o); f = int(m.group(3)) // int(m.group(2))
        return ('basis', 'factor 2') if f == 2 else ('toepassen', f'factor {f}')
    if key == ('G6-GET-E04', 1):
        x, y = [_int(g) for g in re.findall(r'(\d+) \w+\. Er zijn er (\d+) weggehaald', o)[0]]
        n, nul = _leent(x, y)
        if n <= 1 and not nul: return 'basis', f'{n}× lenen, geen nul'
        if n >= 2 or nul: return 'toepassen', f'{n}× lenen' + (', nul in het aftrektal' if nul else '')
    if key == ('G6-GET-E09', 1):
        m = re.fullmatch(r'Hoeveel is (\d+)/(\d+) van €(\d+)\?', o); t, nn, x = map(int, m.groups())
        return ('basis', 'één deel is een heel bedrag') if x % nn == 0 else ('toepassen', 'één deel heeft centen')
    if key == ('G6-GET-E09', 2):
        m = re.fullmatch(r'Hoeveel is (\d+)/(\d+) van (\d+)\?', o); t, nn, x = map(int, m.groups())
        if x <= 100 and x % nn == 0 and x // nn <= 10: return 'basis', 'getal ≤ 100, één deel uit de tafel'
        if x > 100: return 'toepassen', 'getal > 100'
        return None, 'getal ≤ 100 maar één deel niet uit de tafel'
    if key == ('G6-GET-M02', 1):
        m = re.fullmatch(r'([\d.]+) wordt ([\d.]+)\. .*', o); x, y = str(_int(m.group(1))), str(_int(m.group(2)))
        dif = sum(1 for p, q in zip(x.zfill(6), y.zfill(6)) if p != q)
        return ('basis', 'één cijfer verandert') if dif == 1 else ('toepassen', f'{dif} cijfers veranderen (overgang)')
    if key in (('G6-GET-M02', 2), ('G6-GET-M02', 3)):
        m = re.fullmatch(r'Welk getal is ([\d.]+) (meer|minder) dan ([\d.]+)\?', o); s, x = _int(m.group(1)), _int(m.group(3)); y = _int(a)
        dif = sum(1 for p, q in zip(str(x).zfill(6), str(y).zfill(6)) if p != q)
        return ('basis', 'één cijfer verandert') if dif == 1 else ('toepassen', 'met ' + ('overgang' if nro == 2 else 'lenen'))
    if key == ('G6-GET-M03', 1):
        m = re.fullmatch(r'Zet ([\d,]+) op de lijn van (\d+) tot (\d+)\.', o)
        if not m: return None, 'andere vorm'
        g, tot = m.group(1), int(m.group(3)); dec = len(g.split(',')[1]) if ',' in g else 0
        if tot <= 2 and dec == 1: return 'basis', f'lijn 0–{tot}, 1 decimaal'
        if tot == 10 or dec == 2: return 'toepassen', f'lijn 0–{tot}' + (', 2 decimalen' if dec == 2 else '')
        return None, 'geen kenmerk'
    if key == ('G6-GET-M06', 1):
        m = re.fullmatch(r'(\d+) × (\d) =', o); x, f = int(m.group(1)), int(m.group(2)); n = _onthoudt(x, f)
        if x % 10 == 0 or n == 0: return 'basis', 'rond getal' if x % 10 == 0 else 'zonder onthouden'
        if n >= 2: return 'toepassen', f'onthouden in {n} kolommen'
        return None, 'onthouden in 1 kolom (tussenvorm, blijft)'
    if key == ('G6-GET-E06', 1):
        m = re.fullmatch(r'(\d+) × (\d+) =', o); x, y = int(m.group(1)), int(m.group(2))
        if x % 10 == 0 or y % 10 == 0 or min(x, y) <= 12: return 'basis', 'een factor is een tiental of ≤ 12'
        return 'toepassen', 'beide factoren niet rond en > 12'
    if doel in ('G6-MEET-E01', 'G6-MEET-E04', 'G6-MEET-E05'):        # Regel M
        m = re.fullmatch(r'([\d.,]+) (\w+) = □ (\w+)', o)
        if not m: return 'toepassen', 'contextzin (Regel M)'
        q = m.group(1); groot = q if _groter(m.group(2), m.group(3)) else a
        w = F(groot.replace('.', '').replace(',', '.'))
        if w.denominator == 1 and w <= 20: return 'basis', f'grootste maat {groot} (heel, ≤ 20), kale vorm (Regel M)'
        return 'toepassen', f'grootste maat {groot} ' + ('met komma' if w.denominator != 1 else '> 20') + ' (Regel M)'
    if key == ('G6-MEET-E03', 1):
        m = re.search(r'(\d+) cm lang en (\d+) cm breed', o); l, b = int(m.group(1)), int(m.group(2))
        ctx = not re.match(r'Een (?:rechthoek is|\w+ is een rechthoek van) ', o)      # 'Een tegel is een rechthoek van …' is alleen een naam, geen context (zo telt Leerlijn: Nu 33/220/0)
        if l <= 10 and b <= 10 and not ctx: return 'basis', 'beide zijden ≤ 10, kale vorm'
        return 'toepassen', ('een zijde > 10' if max(l, b) > 10 else 'context')
    if key == ('G6-MEET-E03', 2):
        z = _int(a)
        return ('basis', 'andere zijde ≤ 10') if z <= 10 else ('toepassen', 'andere zijde > 10')
    if key == ('G6-VBN-E02', 1):
        ms = [x for x in re.findall(r'\b(' + '|'.join(MAAND) + r')\b', o)]
        if len(ms) != 2 or not jr.get('perstreep'): return None, 'geen kenmerk'
        naast = abs(MAAND.index(ms[0]) - MAAND.index(ms[1])) == 1
        if naast and jr['perstreep'] == 10: return 'basis', 'maanden naast elkaar, 10 per streepje'
        return 'toepassen', ('maanden niet naast elkaar' if not naast else f"{jr['perstreep']} per streepje")
    if key == ('G6-VBN-E02', 2):
        if not jr.get('cijfer_om'): return None, 'geen kenmerk'
        return ('basis', 'stip op een genummerde lijn') if _int(a) % jr['cijfer_om'] == 0 else ('toepassen', 'stip op een tussenstreepje')
    if key == ('G6-VBN-E02', 3):
        n = len(jr.get('punten') or []); ps = jr.get('perstreep')
        if n in (3, 4) and ps == 10: return 'basis', f'{n} maanden, 10 per streepje'
        return 'toepassen', (f'{n} maanden' if n >= 5 else f'{ps} per streepje')
    if key == ('G6-VERH-E02', 2):
        m = re.search(r'Er zijn (\d+) koekjes\. Kleur (\d+)/(\d+)', o); n, t = int(m.group(1)), int(m.group(2))
        if t == 1 and n <= 12: return 'basis', 'stambreuk, ≤ 12 koekjes'
        return 'toepassen', ('niet-stambreuk' if t != 1 else '> 12 koekjes')
    if key == ('G6-VERH-E03', 1):
        m = re.match(r'(\d+) .+? worden eerlijk verdeeld over (\d+)', o); x, n = int(m.group(1)), int(m.group(2))
        if x == 1: return 'basis', 'één ding (stambreuk)'
        if x < n and not jr and not it['visual'].get('type'): return 'toepassen', 'a < n zonder plaatje'
        return None, 'geen kenmerk'
    if key in (('G6-VERH-E02', 1), ('G6-VERH-E02', 5)): return 'basis', 'alleen basis (besluit)'
    return None, 'geen regel'

_MATEN = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km', 'ml', 'cl', 'dl', 'L', 'g', 'kg']
_RANG = {'mm': 1, 'cm': 2, 'dm': 3, 'm': 4, 'hm': 6, 'km': 7, 'ml': 1, 'cl': 2, 'dl': 3, 'L': 4, 'g': 1, 'kg': 4}
def _groter(u, v): return _RANG[u] > _RANG[v]
