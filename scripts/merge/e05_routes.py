"""V-#870 / Z-#871 / V-#871a-b (Didactiek G8 batch 4, 8 okt 16:35; les 195/253/315/316): rekenmachine-verhalen in G8-GET-E05.
Een foute route mag nooit het goede antwoord geven, en de maten moeten kloppen.
  'nodig' (antwoord = hele getal + 1): rest ≥ 3 (Z-#871), de rest is niet het antwoord, het antwoord is niet het aantal per stuk of het totaal;
          routes: getal uit de vraag, het hele getal, hele getal + rest, de rest, de cijfers achter de komma.
  'over'  (antwoord = de rest): geen uitkomst op ',5' (per stuk − rest = rest), het antwoord is geen getal uit de vraag en niet het hele getal;
          routes: getal uit de vraag, het hele getal, per stuk − rest, de cijfers achter de komma.
  maten (V-#871a/b): nooit 2 per stuk; een busje heeft 4 tot 8 kinderen; een krat 6, 12 of 24 flesjes (Z-#880: voor elk item in die context, niet alleen
  de items met nieuwe getallen); V-#880: hoogstens 15 busjes per item (93 kinderen in busjes van 8 → 11,625 → 12).
  De rekenmachine laat een eindig kommagetal zien (hoogstens 3 cijfers achter de komma), en de deling komt nooit precies uit.
Gebruik: import e05_routes as ER; ER.rapport(items) → aantal FAIL (build-gate); ER.genereer(...) → nieuwe (per stuk, totaal) die door het filter komen.
         python3 e05_routes.py --mutanten"""
import re, sys, collections
RX = re.compile(r'^In een (bak|busje|doos|kist|krat|mand|tas|zak) passen (\d+) (\w+)\. Er zijn (\d+) \3\. Op de rekenmachine staat ([\d,]+)\. '
                r'(De volle \w+ gaan weg\. Hoeveel \3 blijven er over\?|Hoeveel \w+ zijn er nodig\?)$')
PER_STUK = {'krat': [6, 12, 24], 'busje': [4, 5, 6, 8]}
PER_STUK_ANDERS = [4, 5, 8, 20, 25, 40, 50]
MAX_BUSJES = 15      # V-#880 (Didactiek batch 4-hercheck, 16:54)
MIN_BUSJES = 5       # V-#910 (Didactiek hercheck 17:11): aantal busjes gespreid over 5–15
MAX_GELIJK = 2       # V-#910: per somtype hoogstens 2 items met hetzelfde antwoord en 2 met hetzelfde hele getal op de rekenmachine
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
    if bak == 'busje' and -(-T // p) > MAX_BUSJES: F.append(f"{-(-T // p)} busjes (V-#880: hoogstens {MAX_BUSJES})")
    if bak == 'krat' and p not in PER_STUK['krat']: F.append(f"een krat met {p} flesjes (Z-#880: 6, 12 of 24)")
    if soort == 'nodig' and 0 < rest < 3: F.append(f'rest {rest} (Z-#871: rest ≥ 3)')
    if soort == 'over' and 2 * rest == p: F.append("uitkomst op ',5' (per stuk − rest = rest)")
    if (p * 100) % T == 0: F.append(f"omgekeerde deling {p} : {T} komt precies uit (Z-#911)")
    if soort == 'nodig' and a + 1 == p: F.append(f"antwoord + 1 = per stuk ({p}) (Z-#912)")
    if soort == 'over' and heel == p: F.append(f"hele getal = per stuk ({p}) (Z-#912)")
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
def past_spreiding(p, T, soort, tel):
    """V-#910: tel = {'antwoord': Counter, 'heel': Counter} van het somtype tot nu toe"""
    return tel is None or (tel['antwoord'][antwoord(p, T, soort)] < MAX_GELIJK and tel['heel'][T // p] < MAX_GELIJK)
def genereer(bak, p_oud, T_oud, soort, seed=0, bezet=(), tel=None):
    """nieuwe (per stuk, totaal) dicht bij het oude item die door het filter komen; liefst met alle routewaarden verschillend (les 315).
    V-#910: tel (per somtype) houdt de spreiding bij; een busje krijgt een aantal busjes uit 5–15, per item een ander startpunt (seed)."""
    toegestaan = PER_STUK.get(bak, PER_STUK_ANDERS)
    ps = [toegestaan[(seed + i) % len(toegestaan)] for i in range(len(toegestaan))]
    if p_oud in toegestaan: ps = [p_oud] + [x for x in ps if x != p_oud]      # eerst het oude aantal per stuk; lukt de spreiding niet, dan een ander
    if bak == 'busje':
        ns = list(range(MIN_BUSJES, MAX_BUSJES + 1)); k = seed % len(ns); ns = ns[k:] + ns[:k]
        for streng in (True, False):
            for n in ns:
                for p in ps:
                    for rest in range(3, p):
                        T = (n - 1) * p + rest if soort == 'nodig' else n * p + rest      # 'nodig': n busjes; 'over': n volle busjes
                        if T <= 3 * p or (bak, p, T) in bezet or fouten(p, T, soort, bak) or not past_spreiding(p, T, soort, tel): continue
                        if streng:
                            v = [x for x in routes(p, T, soort).values() if x is not None] + [antwoord(p, T, soort)]
                            if len(set(v)) != len(v): continue
                        return p, T
    for streng in (True, False):
        for p in ps:
            mid = max(3 * p + 3, round(T_oud * p / p_oud))
            if bak == 'busje': mid = min(mid, (MAX_BUSJES - 3) * p + p // 2)      # V-#880: rond de 12 busjes, nooit meer dan 15
            bereik = max(30, mid // 3)
            for d in range(0, bereik):
                for T in ((mid + d, mid - d) if d else (mid,)):
                    if T <= 3 * p or (bak, p, T) in bezet or fouten(p, T, soort, bak) or not past_spreiding(p, T, soort, tel): continue
                    if streng:
                        v = [x for x in routes(p, T, soort).values() if x is not None] + [antwoord(p, T, soort)]
                        if len(set(v)) != len(v): continue
                    return p, T
    raise ValueError(('E05: geen nieuw item gevonden', bak, p_oud, T_oud, soort))
def spreiding(items):
    """V-#910: per somtype (doel, nrOrigineel) hoogstens MAX_GELIJK items met hetzelfde antwoord en met hetzelfde hele getal op de rekenmachine; busjes 5–15"""
    G = collections.defaultdict(list); F = []
    for it in items:
        L = lees(it.get('opgave'))
        if L: G[((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNrOrigineel'), L['bak'], L['soort'])].append((it, L))
    for k, v in G.items():
        for naam, f in (('antwoord', lambda it, L: str(it.get('antwoord'))), ('hele getal op de rekenmachine', lambda it, L: L['T'] // L['p'])):
            c = collections.Counter(f(it, L) for it, L in v)
            for w, n in c.items():
                if n > MAX_GELIJK: F.append(f"{k[0]} nrO {k[1]} ({k[2]}, {k[3]}): {n} items met {naam} {w} (V-#910: hoogstens {MAX_GELIJK})")
        for it, L in v:
            if L['bak'] == 'busje' and not MIN_BUSJES <= -(-L['T'] // L['p']) <= MAX_BUSJES: F.append(f"{it['id']}: {-(-L['T'] // L['p'])} busjes (V-#910: 5–15)")
    return F
def rapport(items, toon=True, ernst='FAIL'):
    F = []; per = collections.defaultdict(lambda: [0, 0])
    for it in items:
        f = fouten_item(it)
        if f is None: continue
        k = ((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNrOrigineel')); per[k][0] += 1
        if f: per[k][1] += 1; F.append(f"{it['id']}: {it['opgave'][:70]}… → {it.get('antwoord')}: {'; '.join(f)}")
    S = [f"{k[0]} nrO {k[1]}: {n_f}/{n} items met een fout (≥ 1/3)" for k, (n, n_f) in per.items() if 3 * n_f >= n and n_f]
    SP = spreiding(items); F += [f'SPREIDING {x}' for x in SP]
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
    ('busje 136 (V-#880)', 'In een busje passen 4 kinderen. Er zijn 543 kinderen. Op de rekenmachine staat 135,75. Hoeveel busjes zijn er nodig?', '136', True),
    ('busje 16 (V-#880)', 'In een busje passen 8 kinderen. Er zijn 125 kinderen. Op de rekenmachine staat 15,625. Hoeveel busjes zijn er nodig?', '16', True),
    ('krat met 5 (Z-#880)', 'In een krat passen 5 flesjes. Er zijn 63 flesjes. Op de rekenmachine staat 12,6. Hoeveel kratten zijn er nodig?', '13', True),
    ('goed busje (V-#880)', 'In een busje passen 8 kinderen. Er zijn 93 kinderen. Op de rekenmachine staat 11,625. Hoeveel busjes zijn er nodig?', '12', False),
    ('omgekeerde deling exact (029, Z-#911)', 'In een busje passen 8 kinderen. Er zijn 100 kinderen. Op de rekenmachine staat 12,5. Hoeveel busjes zijn er nodig?', '13', True),
    ('antwoord + 1 = per stuk (079, Z-#912)', 'In een krat passen 12 flesjes. Er zijn 129 flesjes. Op de rekenmachine staat 10,75. Hoeveel kratten zijn er nodig?', '11', True),
    ('goed (nodig)', 'In een bak passen 8 potjes. Er zijn 141 potjes. Op de rekenmachine staat 17,625. Hoeveel bakken zijn er nodig?', '18', False),
    ('goed (over)', 'In een bak passen 8 potjes. Er zijn 141 potjes. Op de rekenmachine staat 17,625. De volle bakken gaan weg. Hoeveel potjes blijven er over?', '5', False),
]
def _sp_mutant(antw):
    return [{'id': f'm{i}', 'opgave': f'In een busje passen 8 kinderen. Er zijn {T} kinderen. Op de rekenmachine staat {scherm(T, 8)}. Hoeveel busjes zijn er nodig?',
             'antwoord': str(T // 8 + 1), 'merge': {'doel': 'M', 'somtypeNrOrigineel': 6}} for i, T in enumerate(antw)]
SP_MUTANTEN = [('zes keer 13 (V-#910)', [99, 101, 102, 99, 101, 102], True), ('gespreid', [77, 93, 59, 101, 45, 83], False)]
def sp_mutanten_ok(): return all(bool(spreiding(_sp_mutant(a))) == v for _, a, v in SP_MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    ok = 0
    for naam, o, a, verwacht in MUTANTEN:
        f = fouten_item({'id': naam, 'opgave': o, 'antwoord': a}); kreeg = bool(f)
        ok += kreeg == verwacht; print(('ok  ' if kreeg == verwacht else 'MIS ') + f'{naam}: {f}')
    for naam, a, v in SP_MUTANTEN:
        kreeg = bool(spreiding(_sp_mutant(a))); ok += kreeg == v; print(('ok  ' if kreeg == v else 'MIS ') + f'{naam}: {spreiding(_sp_mutant(a))[:2]}')
    n = len(MUTANTEN) + len(SP_MUTANTEN); print(f'mutanten E05-ROUTES: {ok}/{n}'); sys.exit(0 if ok == n else 1)
