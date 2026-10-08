"""V-#975 (Didactiek G8 b8 deel A, les 369): extraVelden.claudeKaleSom moet bij het item horen. Een generator die de opgave vervangt, moet de kale som meenemen.
Leesbare kale sommen:
  - 'Op welk cijfer eindigt a × b?'  → moet gelijk zijn aan de opgave (GET-E02 #1) en uitkomen op het antwoord;
  - een kale rekensom met alleen getallen en + − × : ( ), eventueel met '= n' erachter → uitkomst (en n) = het antwoord (als het antwoord een getal is).
Z-#992: ook eenheden, breuken, punt als duizendtal, ':' tussen maten, '≈', procenten, 'regel: …'. Niet gelezen: woorden en doelcodes zoals 'B13'. FAIL bij een leesbare kale som die niet klopt.
Gebruik: import kalesom_check as KS; KS.rapport(items); python3 kalesom_check.py --mutanten"""
import re, sys
from fractions import Fraction as F
EIND = re.compile(r'^Op welk cijfer eindigt (\d+) × (\d+)\?$')
SOM = re.compile(r'^[\d.,()+−×: ]+(?:= ?[\d.,]+)?$')
def _getal(t):
    t = str(t).strip()
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', t): t = t.replace('.', '')
    if re.fullmatch(r'\d+(?:,\d+)?', t): return F(t.replace(',', '.'))
    return None
def _reken(expr):
    e = expr.replace('×', '*').replace(':', '/').replace('−', '-')
    e = re.sub(r'(\d{1,3})\.(\d{3})(?!\d)', r'\1\2', e); e = re.sub(r'(\d),(\d)', r'\1.\2', e)
    if not re.fullmatch(r'[\d.()+\-*/ ]+', e): return None
    e = re.sub(r'(\d+(?:\.\d+)?)', r'F("\1")', e)
    try: return eval(e, {'F': F, '__builtins__': {}})
    except Exception: return None
# Z-#992 (Didactiek 18:35): ook vormen met eenheden ('8 cm × 10.000', '16 GB : 800 MB', '8,1 km = ? m'), breuken ('1/3 × 3/4', '4 : 1/4'),
# punt als duizendtal, '≈' (schatten: rechts van ≈ = het antwoord), procenten ('3% van 2000', '200 + 25%') en 'regel: a + week × b, week n'.
EENH = {'mm': ('L', F(1, 1000)), 'cm': ('L', F(1, 100)), 'dm': ('L', F(1, 10)), 'm': ('L', F(1)), 'dam': ('L', F(10)), 'hm': ('L', F(100)), 'km': ('L', F(1000)),
        'mg': ('M', F(1, 1000)), 'g': ('M', F(1)), 'kg': ('M', F(1000)), 'ton': ('M', F(10 ** 6)),
        'ml': ('V', F(1, 1000)), 'cl': ('V', F(1, 100)), 'dl': ('V', F(1, 10)), 'l': ('V', F(1)), 'L': ('V', F(1)), 'liter': ('V', F(1)), 'hl': ('V', F(100)),
        'cm³': ('V', F(1, 1000)), 'dm³': ('V', F(1)), 'm³': ('V', F(1000)), 'mm²': ('A', F(1, 10 ** 6)), 'cm²': ('A', F(1, 10 ** 4)), 'dm²': ('A', F(1, 100)), 'm²': ('A', F(1)),
        'are': ('A', F(100)), 'ha': ('A', F(10 ** 4)), 'km²': ('A', F(10 ** 6)), 'KB': ('B', F(1, 1000)), 'MB': ('B', F(1)), 'GB': ('B', F(1000)), 'TB': ('B', F(10 ** 6))}
GETAL = r'\d{1,3}(?:\.\d{3})+(?!\d)|\d+(?:,\d+)?'
U_RX = '|'.join(sorted(map(re.escape, EENH), key=len, reverse=True))
def _antw(a):
    """antwoord als getal (zonder €, eenheid, %, 'uur'); breuk 'a/b' mag. None als het geen getal is."""
    t = re.sub(r'^€ ?', '', str(a).strip()); t = re.sub(r' ?(?:%|procent|' + U_RX + r')$', '', t).strip()
    if (m := re.fullmatch(r'(\d+)/(\d+)', t)): return F(int(m.group(1)), int(m.group(2)))
    if t.startswith('−') and _getal(t[1:]) is not None: return -_getal(t[1:])
    return _getal(t)
def _reken_eenheid(expr):
    """rekensom met getallen, breuken en eenheden → (waarde, dimensie of None). Eenheden worden naar de basismaat omgezet; bij ':' tussen
    twee gelijke dimensies valt de eenheid weg. None als het niet te lezen is."""
    dims = []
    def sub(m):
        g, u = m.group(1), m.group(2)
        w = _getal(g)
        if u: d_, f_ = EENH[u]; dims.append(d_); w = w * f_
        return f'F({w.numerator},{w.denominator})'
    br = []
    e = re.sub(r'(\d+)/(\d+)', lambda m: (br.append(F(int(m.group(1)), int(m.group(2)))), f'§{len(br) - 1}§')[1], expr.strip())
    e = re.sub(r'€ ?', '', e)
    e = re.sub(r'(?<![§\d])(' + GETAL + r')(?![§\d])(?: ?(' + U_RX + r')(?![A-Za-z²³]))?', sub, e)
    e = re.sub(r'§(\d+)§', lambda m: f'F({br[int(m.group(1))].numerator},{br[int(m.group(1))].denominator})', e)
    e = e.replace('×', '*').replace(':', '/').replace('−', '-')
    if not re.fullmatch(r'(?:F\(\d+,\d+\)|[()+\-*/ ])+', e): return None
    try: w = eval(e, {'F': F, '__builtins__': {}})
    except Exception: return None
    dim = None
    if dims:
        if '/' in e and len(dims) == 2 and dims[0] == dims[1] and not re.search(r'[+\-]', e): dim = None      # 16 GB : 800 MB → 20
        elif len(set(dims)) == 1: dim = dims[0]
        else: return None
    return w, dim
def _klopt(w, dim, a):
    """past waarde w (in de basismaat van dim) bij het antwoord? Met een dimensie: in een van de eenheden van die dimensie."""
    if dim is None: return w == a
    return any(w / f_ == a for d_, f_ in EENH.values() if d_ == dim)
def lees(it):
    """(gelezen, fout): gelezen = de kale som is in een bekende vorm; fout = tekst als hij niet klopt bij opgave/antwoord."""
    ks = ((it.get('extraVelden') or {}).get('claudeKaleSom') or '').strip(); a = str(it.get('antwoord'))
    if not ks: return False, None
    m = EIND.match(ks)
    if m:
        if ks != (it.get('opgave') or '').strip(): return True, f'kale som {ks!r} ≠ opgave {it.get("opgave")!r}'
        if str(int(m.group(1)) * int(m.group(2)) % 10) != a: return True, f'kale som {ks!r} geeft niet het antwoord {a}'
        return True, None
    ga = _antw(a)
    if ga is None: return False, None
    if (m := re.fullmatch(r'(' + GETAL + r') ?% van (' + GETAL + r')', ks)):      # 3% van 2000
        w = _getal(m.group(1)) * _getal(m.group(2)) / 100
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if (m := re.fullmatch(r'€?(' + GETAL + r') ([+−]) (' + GETAL + r') ?%', ks)):      # 200 + 25%
        b = _getal(m.group(1)); w = b * (100 + (1 if m.group(2) == '+' else -1) * _getal(m.group(3))) / 100
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if (m := re.fullmatch(r'regel: (' + GETAL + r') \+ week × (' + GETAL + r'), week (\d+)', ks)):
        w = _getal(m.group(1)) + _getal(m.group(2)) * int(m.group(3))
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if (m := re.fullmatch(r'(.+?) = (?:\?|_+) ?(' + U_RX + r')', ks)):      # 8,1 km = ? m · 32 GB = __ MB
        r_ = _reken_eenheid(m.group(1))
        if r_ is None or r_[1] is None or EENH[m.group(2)][0] != r_[1]: return False, None
        w = r_[0] / EENH[m.group(2)][1]
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if (m := re.fullmatch(r'na (' + GETAL + r') ?% korting €?(' + GETAL + r'), was\?', ks)):      # na 20% korting €120, was?
        w = _getal(m.group(2)) * 100 / (100 - _getal(m.group(1)))
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if (m := re.fullmatch(r'van (' + GETAL + r') naar (' + GETAL + r') = \+_+ ?%', ks)):      # van 80 naar 120 = +__%
        x_, y_ = _getal(m.group(1)), _getal(m.group(2)); w = (y_ - x_) * 100 / x_
        return True, (None if w == ga else f'kale som {ks!r} = {float(w):g}, antwoord {a}')
    if ks.count('=') == 1 and len(re.findall(r'\?|_+', ks)) == 1:      # vergelijking met één onbekende ('9 : 5 = 18 : ?', '6158 = 6000 + 100 + ? + 8'): vul het antwoord in
        e_ = re.sub(r'\?|_+', f'{ga.numerator}/{ga.denominator}' if ga.denominator != 1 else str(ga.numerator), ks)
        if ga < 0 or re.search(r'[A-Za-z]', re.sub(U_RX, '', e_)): return False, None
        L_, R_ = (_reken_eenheid(x) for x in e_.split('='))
        if L_ is None or R_ is None: return False, None
        vast = [_reken_eenheid(x) for x in ks.split('=') if not re.search(r'\?|_+', x)]      # '6 × 10 = 10 × __' bij antwoord 60: de kant zonder vakje is het antwoord
        return True, (None if L_[0] == R_[0] or (vast and vast[0] and vast[0][0] == ga) else f'kale som {ks!r} klopt niet met het antwoord {a} (niet op de plek van de ?, niet als uitkomst)')
    if '≈' in ks:      # 497 × 5 ≈ 500 × 5: de schatting (rechts) is het antwoord
        r_ = _reken_eenheid(ks.split('≈')[-1])
        if r_ is None: return False, None
        return True, (None if _klopt(*r_, ga) else f'kale som {ks!r}: schatting = {float(r_[0]):g}, antwoord {a}')
    if not re.search(r'[+−×:]', ks) or re.search(r'[A-Za-z]', re.sub(U_RX, '', ks)): return False, None
    links, _, rechts = ks.partition('=')
    r_ = _reken_eenheid(links)
    if r_ is None: return False, None
    if not _klopt(*r_, ga): return True, f'kale som {ks!r} = {float(r_[0]):g}, antwoord {a}'
    if rechts.strip() and _antw(rechts) is not None and _antw(rechts) != ga: return True, f'kale som {ks!r}: na het = staat niet het antwoord {a}'
    return True, None
def fout_item(it): return lees(it)[1]
def telling(items):
    """(met kale som, gelezen, doelcodes) — Z-#992"""
    ks = [((it.get('extraVelden') or {}).get('claudeKaleSom') or '').strip() for it in items]
    return sum(map(bool, ks)), sum(lees(it)[0] for it in items), sum(bool(re.fullmatch(r'[A-Z]{1,2}\d{1,2}', k)) for k in ks)
def fouten(items): return [f"{it['id']}: {f}" for it in items if (f := fout_item(it))]
def rapport(items, toon=True, ernst='FAIL'):
    F_ = fouten(items)
    if toon:
        n, g, dc = telling(items)
        print(f"\nKALESOM (V-#975/Z-#992: claudeKaleSom hoort bij de opgave en komt uit op het antwoord; gelezen {g}/{n}, waarvan doelcodes {dc} niet): {len(F_)} ({ernst})")
        for x in F_[:12]: print(f'  {ernst} KALESOM', x)
    return len(F_)
def _it(o, a, ks): return {'id': 'mut', 'opgave': o, 'antwoord': a, 'extraVelden': {'claudeKaleSom': ks}}
MUTANTEN = [('061 oud: kale som 19 × 17 bij opgave 29 × 17', _it('Op welk cijfer eindigt 29 × 17?', '3', 'Op welk cijfer eindigt 19 × 17?'), True),
            ('064 oud: 112 × 12 (ander antwoord)', _it('Op welk cijfer eindigt 112 × 14?', '8', 'Op welk cijfer eindigt 112 × 12?'), True),
            ('kale som klopt', _it('Op welk cijfer eindigt 29 × 17?', '3', 'Op welk cijfer eindigt 29 × 17?'), False),
            ('E03 #2 oude som bij nieuwe opgave', _it('Reken uit. 20 : 4 + 7', '12', '15 : 3 + 6 = 11'), True),
            ('E03 #2 klopt', _it('Reken uit. 20 : 4 + 7', '12', '20 : 4 + 7 = 12'), False),
            ('Z-#992: schaal met eenheid en punt, klopt', _it('Op een kaart met schaal 1 : 100.000 is iets 5 cm. Hoeveel meter?', '5000', '5 cm × 100.000'), False),
            ('Z-#992: schaal met eenheid, verkeerd getal', _it('… 5 cm … Hoeveel meter?', '4000', '5 cm × 100.000'), True),
            ('Z-#992: GB : MB klopt', _it('…', '20', '16 GB : 800 MB'), False),
            ('V-#901 oud: GB : MB van een ander item', _it('…', '20', '32 GB : 500 MB'), True),
            ('Z-#992: omrekenen 8,1 km = ? m', _it('…', '8100', '8,1 km = ? m'), False),
            ('Z-#992: omrekenen fout', _it('…', '810', '8,1 km = ? m'), True),
            ('Z-#992: breuk : breuk', _it('…', '16', '4 : 1/4'), False),
            ('Z-#992: schatting ≈ klopt niet', _it('…', '2500', '497 × 5 ≈ 400 × 5'), True),
            ('Z-#992: procent van', _it('…', '60', '3% van 2000'), False),
            ('V-#1003 oud G7-MEET-02 001: kale som bij oude maten', _it('…', '21', '10 × 6 : 2'), True),
            ('Z-#992: verhouding met ? klopt', _it('Vul in. 9 : 5 = 18 : ?', '10', '9 : 5 = 18 : ?'), False),
            ('Z-#992: verhouding met ? fout', _it('Vul in. 9 : 5 = 18 : ?', '12', '9 : 5 = 18 : ?'), True),
            ('Z-#992: splitsen met ? klopt', _it('…', '50', '6158 = 6000 + 100 + ? + 8'), False),
            ('Z-#992: korting terugrekenen', _it('…', '150', 'na 20% korting €120, was?'), False),
            ('Z-#992: breuk × breuk fout', _it('…', '1/5', '1/3 × 3/4'), True),
            ('Z-#992: omdraaien met vakje, antwoord = de vaste kant', _it('…', '60', '6 × 10 = 10 × __'), False),
            ('Z-#992: omdraaien met vakje, verkeerd antwoord', _it('…', '50', '6 × 10 = 10 × __'), True),
            ('doelcode wordt niet gelezen', _it('Schrijf 0,4 in procenten.', '40%', 'B13'), False)]
def mutanten_ok(): return all(bool(fout_item(it)) == v for _, it, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, it, v in MUTANTEN: print(('ok  ' if bool(fout_item(it)) == v else 'MIS ') + n, fout_item(it))
    print('mutanten KALESOM:', sum(bool(fout_item(it)) == v for _, it, v in MUTANTEN), '/', len(MUTANTEN)); sys.exit(0 if mutanten_ok() else 1)
