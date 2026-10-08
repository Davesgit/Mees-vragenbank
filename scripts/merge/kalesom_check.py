"""V-#975 (Didactiek G8 b8 deel A, les 369): extraVelden.claudeKaleSom moet bij het item horen. Een generator die de opgave vervangt, moet de kale som meenemen.
Leesbare kale sommen:
  - 'Op welk cijfer eindigt a × b?'  → moet gelijk zijn aan de opgave (GET-E02 #1) en uitkomen op het antwoord;
  - een kale rekensom met alleen getallen en + − × : ( ), eventueel met '= n' erachter → uitkomst (en n) = het antwoord (als het antwoord een getal is).
Andere kale sommen (met eenheden, woorden of doelcodes zoals 'B13') worden niet gelezen. FAIL bij een leesbare kale som die niet klopt.
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
def fout_item(it):
    ks = ((it.get('extraVelden') or {}).get('claudeKaleSom') or '').strip(); a = str(it.get('antwoord'))
    if not ks: return None
    m = EIND.match(ks)
    if m:
        if ks != (it.get('opgave') or '').strip(): return f'kale som {ks!r} ≠ opgave {it.get("opgave")!r}'
        if str(int(m.group(1)) * int(m.group(2)) % 10) != a: return f'kale som {ks!r} geeft niet het antwoord {a}'
        return None
    if not SOM.match(ks) or not re.search(r'[+−×:]', ks): return None
    links, _, rechts = ks.partition('=')
    w = _reken(links); ga = _getal(a)
    if w is None or ga is None: return None
    if w != ga: return f'kale som {ks!r} = {float(w):g}, antwoord {a}'
    if rechts.strip() and _getal(rechts) != ga: return f'kale som {ks!r}: na het = staat niet het antwoord {a}'
    return None
def fouten(items): return [f"{it['id']}: {f}" for it in items if (f := fout_item(it))]
def rapport(items, toon=True, ernst='FAIL'):
    F_ = fouten(items)
    if toon:
        print(f"\nKALESOM (V-#975: claudeKaleSom hoort bij de opgave en komt uit op het antwoord): {len(F_)} ({ernst})")
        for x in F_[:12]: print(f'  {ernst} KALESOM', x)
    return len(F_)
def _it(o, a, ks): return {'id': 'mut', 'opgave': o, 'antwoord': a, 'extraVelden': {'claudeKaleSom': ks}}
MUTANTEN = [('061 oud: kale som 19 × 17 bij opgave 29 × 17', _it('Op welk cijfer eindigt 29 × 17?', '3', 'Op welk cijfer eindigt 19 × 17?'), True),
            ('064 oud: 112 × 12 (ander antwoord)', _it('Op welk cijfer eindigt 112 × 14?', '8', 'Op welk cijfer eindigt 112 × 12?'), True),
            ('kale som klopt', _it('Op welk cijfer eindigt 29 × 17?', '3', 'Op welk cijfer eindigt 29 × 17?'), False),
            ('E03 #2 oude som bij nieuwe opgave', _it('Reken uit. 20 : 4 + 7', '12', '15 : 3 + 6 = 11'), True),
            ('E03 #2 klopt', _it('Reken uit. 20 : 4 + 7', '12', '20 : 4 + 7 = 12'), False),
            ('doelcode wordt niet gelezen', _it('Schrijf 0,4 in procenten.', '40%', 'B13'), False)]
def mutanten_ok(): return all(bool(fout_item(it)) == v for _, it, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, it, v in MUTANTEN: print(('ok  ' if bool(fout_item(it)) == v else 'MIS ') + n, fout_item(it))
    print('mutanten KALESOM:', sum(bool(fout_item(it)) == v for _, it, v in MUTANTEN), '/', len(MUTANTEN)); sys.exit(0 if mutanten_ok() else 1)
