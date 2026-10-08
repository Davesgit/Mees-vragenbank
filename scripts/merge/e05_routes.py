"""V-#870 / Z-#871 / V-#871a-b (Didactiek G8 batch 4, 8 okt 16:35; les 195/253/315/316): rekenmachine-verhalen in G8-GET-E05.
Een foute route mag nooit het goede antwoord geven, en de maten moeten kloppen.
  'nodig' (antwoord = hele getal + 1): rest ≥ 3 (Z-#871), de rest is niet het antwoord, het antwoord is niet het aantal per stuk of het totaal;
          routes: getal uit de vraag, het hele getal, hele getal + rest, de rest, de cijfers achter de komma.
  'over'  (antwoord = de rest): geen uitkomst op ',5' (per stuk − rest = rest), het antwoord is geen getal uit de vraag en niet het hele getal;
          routes: getal uit de vraag, het hele getal, per stuk − rest, de cijfers achter de komma.
  maten (V-#871a/b): nooit 2 per stuk; een busje heeft 4 tot 8 kinderen; een krat 6, 12 of 24 flesjes (alleen voor nieuwe items, zie PER_STUK).
  De rekenmachine laat een eindig kommagetal zien (hoogstens 3 cijfers achter de komma), en de deling komt nooit precies uit.
Gebruik: import e05_routes as ER; ER.rapport(items) → aantal FAIL (build-gate); ER.genereer(...) → nieuwe (per stuk, totaal) die door het filter komen.
         python3 e05_routes.py --mutanten"""
import re, sys, collections
RX = re.compile(r'^In een (bak|busje|doos|kist|krat|mand|tas|zak) passen (\d+) (\w+)\. Er zijn (\d+) \3\. Op de rekenmachine staat ([\d,]+)\. '
                r'(De volle \w+ gaan weg\. Hoeveel \3 blijven er over\?|Hoeveel \w+ zijn er nodig\?)$')
PER_STUK = {'krat': [6, 12, 24], 'busje': [4, 5, 6, 8]}
PER_STUK_ANDERS = [4, 5, 8, 20, 25, 40, 50]
def scherm(T, p):
    """wat de rekenmachine laat zien ('17,625'); None als de deling niet eindig is binnen 3 decimalen"""
    for k in range(0, 4):
        if (T * 10 ** k) % p == 0:
            q = T * 10 ** k // p; s = str(q).rjust(k + 1, '0')
            return s if k == 0 else f'{s[:-k]},{s[-k:]}'
    return None
def lees(o):
    m = RX.match(o or '')
    if not m: return None
    return {'bak': m.group(1), 'p': int(m.group(2)), 'ding': m.group(3), 'T': int(m.group(4)), 'scherm': m.group(5), 'soort': 'over' if 'over?' in m.group(6) else 'nodig', 'staart': m.group(6)}
def antwoord(p, T, soort): return T // p + 1 if soort == 'nodig' else T % p
def routes(p, T, soort):
    heel, rest = divmod(T, p); sc = scherm(T, p) or ''; achter = int(sc.split(',')[1]) if ',' in sc else None
    R = {'getal uit de vraag (per stuk)': p, 'getal uit de vraag (totaal)': T, 'het hele getal': heel, 'de cijfers achter de komma': achter}
    if soort == 'nodig': R.update({'hele getal + rest': heel + rest, 'de rest': rest})
    else: R.update({'per stuk − rest': p - rest})
    return R
def fouten(p, T, soort, bak=None):
    F = []; heel, rest = divmod(T, p); a = antwoord(p, T, soort)
    if scherm(T, p) is None: F.append('de rekenmachine geeft geen eindig kommagetal (meer dan 3 decimalen)')
    if rest == 0: F.append('de deling komt precies uit (geen kommagetal)')
    if p == 2: F.append("2 per stuk (V-#871a)")
    if bak == 'busje' and not 4 <= p <= 8: F.append(f"een busje met {p} kinderen (V-#871b: 4 tot 8)")
    if soort == 'nodig' and 0 < rest < 3: F.append(f'rest {rest} (Z-#871: rest ≥ 3)')
    if soort == 'over' and 2 * rest == p: F.append("uitkomst op ',5' (per stuk − rest = rest)")
    for r, v in routes(p, T, soort).items():
        if v is not None and v == a: F.append(f"route '{r}' geeft het goede antwoord {a}")
    return F
def fouten_item(it):
    L = lees(it.get('opgave'))
    if not L: return None
    F = fouten(L['p'], L['T'], L['soort'], L['bak'])
    if scherm(L['T'], L['p']) != L['scherm']: F.append(f"de rekenmachine staat er als {L['scherm']}, moet {scherm(L['T'], L['p'])} zijn")
    if str(it.get('antwoord')) != str(antwoord(L['p'], L['T'], L['soort'])): F.append(f"antwoord {it.get('antwoord')} ≠ {antwoord(L['p'], L['T'], L['soort'])}")
    return F
def genereer(bak, p_oud, T_oud, soort, seed=0, bezet=()):
    """nieuwe (per stuk, totaal) dicht bij het oude item die door het filter komen; liefst met alle routewaarden verschillend (les 315)"""
    toegestaan = PER_STUK.get(bak, PER_STUK_ANDERS)
    ps = [p_oud] if p_oud in toegestaan else [toegestaan[(seed + i) % len(toegestaan)] for i in range(len(toegestaan))]
    for streng in (True, False):
        for p in ps:
            mid = max(3 * p + 3, round(T_oud * p / p_oud)); bereik = max(30, mid // 3)
            for d in range(0, bereik):
                for T in ((mid + d, mid - d) if d else (mid,)):
                    if T <= 3 * p or (bak, p, T) in bezet or fouten(p, T, soort, bak): continue
                    if streng:
                        v = [x for x in routes(p, T, soort).values() if x is not None] + [antwoord(p, T, soort)]
                        if len(set(v)) != len(v): continue
                    return p, T
    raise ValueError(('E05: geen nieuw item gevonden', bak, p_oud, T_oud, soort))
def rapport(items, toon=True, ernst='FAIL'):
    F = []; per = collections.defaultdict(lambda: [0, 0])
    for it in items:
        f = fouten_item(it)
        if f is None: continue
        k = ((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNrOrigineel')); per[k][0] += 1
        if f: per[k][1] += 1; F.append(f"{it['id']}: {it['opgave'][:70]}… → {it.get('antwoord')}: {'; '.join(f)}")
    S = [f"{k[0]} nrO {k[1]}: {n_f}/{n} items met een fout (≥ 1/3)" for k, (n, n_f) in per.items() if 3 * n_f >= n and n_f]
    if toon:
        print(f"\nE05-ROUTES (V-#870/Z-#871/V-#871: rekenmachine-verhaal, geen foute route op het goede antwoord, redelijke maten): {len(F)} ({ernst}) · items {sum(n for n, _ in per.values())} · somtypes {len(per)}")
        for x in S: print(f'  {ernst} E05-AANDEEL', x)
        for x in F[:15]: print(f'  {ernst} E05-ROUTES', x)
    return len(F)
MUTANTEN = [  # (naam, opgave, antwoord, verwacht aantal fouten > 0)
    ('rest 1 (nodig)', 'In een bak passen 8 potjes. Er zijn 145 potjes. Op de rekenmachine staat 18,125. Hoeveel bakken zijn er nodig?', '19', True),
    ('rest 2 (nodig, Z-#871)', 'In een bak passen 8 potjes. Er zijn 146 potjes. Op de rekenmachine staat 18,25. Hoeveel bakken zijn er nodig?', '19', True),
    (",5 (over)", 'In een doos passen 40 eieren. Er zijn 900 eieren. Op de rekenmachine staat 22,5. De volle dozen gaan weg. Hoeveel eieren blijven er over?', '20', True),
    ('antwoord = per stuk (nodig, 059)', 'In een kist passen 25 boeken. Er zijn 624 boeken. Op de rekenmachine staat 24,96. Hoeveel kisten zijn er nodig?', '25', True),
    ('rest = antwoord (nodig, 092)', 'In een mand passen 40 peren. Er zijn 1518 peren. Op de rekenmachine staat 37,95. Hoeveel manden zijn er nodig?', '38', True),
    ('2 per stuk', 'In een krat passen 2 flesjes. Er zijn 45 flesjes. Op de rekenmachine staat 22,5. Hoeveel kratten zijn er nodig?', '23', True),
    ('busje met 20', 'In een busje passen 20 kinderen. Er zijn 147 kinderen. Op de rekenmachine staat 7,35. Hoeveel busjes zijn er nodig?', '8', True),
    ('goed (nodig)', 'In een bak passen 8 potjes. Er zijn 141 potjes. Op de rekenmachine staat 17,625. Hoeveel bakken zijn er nodig?', '18', False),
    ('goed (over)', 'In een bak passen 8 potjes. Er zijn 141 potjes. Op de rekenmachine staat 17,625. De volle bakken gaan weg. Hoeveel potjes blijven er over?', '5', False),
]
if __name__ == '__main__' and '--mutanten' in sys.argv:
    ok = 0
    for naam, o, a, verwacht in MUTANTEN:
        f = fouten_item({'id': naam, 'opgave': o, 'antwoord': a}); kreeg = bool(f)
        ok += kreeg == verwacht; print(('ok  ' if kreeg == verwacht else 'MIS ') + f'{naam}: {f}')
    print(f'mutanten E05-ROUTES: {ok}/{len(MUTANTEN)}'); sys.exit(0 if ok == len(MUTANTEN) else 1)
