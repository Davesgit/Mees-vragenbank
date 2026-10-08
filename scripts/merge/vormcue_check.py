"""V-#984 (Didactiek G8 batch 8 deel B, les 372; Z-#984): vormcue in meerkeuze. Het goede antwoord mag niet aan zijn vorm te herkennen zijn.
Per item met getal-opties (een getal met eventueel '%', '€' of een eenheid) drie heuristieken:
  dec   het goede antwoord is de enige optie met zijn aantal decimalen;
  kort  het goede antwoord is strikt de kortste optie (tekens);
  lang  het goede antwoord is strikt de langste optie.
Per somtype (doel + somtypeNr, vanaf MIN_ITEMS items): aandeel items waarin een heuristiek het goede antwoord geeft. FAIL als een aandeel > GRENS
(0,40: Didactiek liet 'ongeveer een derde' xx,5% toe). Oud E06 #1 (96/96 'dec') moet FAIL geven (mutant).
Gebruik: import vormcue_check as VC; VC.rapport(items); python3 vormcue_check.py --mutanten"""
import re, sys, collections
GRENS = 0.40; MIN_ITEMS = 6
RX = re.compile(r'^(?:€ ?)?(\d+(?:\.\d{3})*(?:,(\d+))?)(?: ?(?:%|procent|[a-zA-Z²³]+))?$')
def _dec(t):
    m = RX.match(str(t).strip())
    return None if not m else len(m.group(2) or '')
def cues(it):
    ops = [o.get('tekst') for o in it.get('opties') or []]; goed = str(it.get('antwoord'))
    if it.get('type') != 'meerkeuze' or len(ops) < 3 or goed not in ops or any(_dec(o) is None for o in ops): return None
    d = [_dec(o) for o in ops]; L = [len(str(o)) for o in ops]; i = ops.index(goed)
    return {'dec': d.count(d[i]) == 1, 'kort': L[i] < min(L[:i] + L[i + 1:]), 'lang': L[i] > max(L[:i] + L[i + 1:])}
def per_somtype(items):
    S = collections.defaultdict(list)
    for it in items:
        c = cues(it)
        if c is not None: S[((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNr'))].append(c)
    return S
def fouten(items):
    F = []
    for k, L in per_somtype(items).items():
        if len(L) < MIN_ITEMS: continue
        for h in ('dec', 'kort', 'lang'):
            n = sum(c[h] for c in L)
            if n / len(L) > GRENS: F.append(f'{k[0]} #{k[1]}: {h} geeft het goede antwoord in {n}/{len(L)} items')
    return F
def rapport(items, toon=True, ernst='FAIL'):
    F = fouten(items)
    if toon:
        print(f"\nVORMCUE (V-#984: goede optie niet aan zijn vorm te herkennen, grens {GRENS:.0%} per somtype): {len(F)} ({ernst})")
        for x in F[:12]: print(f'  {ernst} VORMCUE', x)
    return len(F)
def _it(n, goed, ops): return {'type': 'meerkeuze', 'antwoord': goed, 'opties': [{'tekst': o} for o in ops], 'merge': {'doel': 'MUT', 'somtypeNr': n}}
MUTANTEN = [('oud E06 #1: alleen het goede antwoord heeft één decimaal', [_it(1, f'{x},5%', [f'{x},5%', f'{x / 10:.2f}%'.replace('.', ','), f'0,{x}5%']) for x in range(11, 21)], True),
            ('nieuw: hele procenten met een afleider met evenveel decimalen', [_it(2, f'{x}0%', [f'{x}%', f'{x}0%', f'{x}00%']) for x in range(1, 10)], False),
            ('kortste optie is steeds goed', [_it(3, f'{x}%', [f'{x}%', f'{x}0,5%', f'0,{x}55%']) for x in range(11, 21)], True)]
def mutanten_ok(): return all(bool(fouten(L)) == v for _, L, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, L, v in MUTANTEN: print(('ok  ' if bool(fouten(L)) == v else 'MIS ') + n, fouten(L))
    print('mutanten VORMCUE:', sum(bool(fouten(L)) == v for _, L, v in MUTANTEN), '/', len(MUTANTEN)); sys.exit(0 if mutanten_ok() else 1)
