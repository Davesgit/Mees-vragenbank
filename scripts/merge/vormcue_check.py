"""V-#984 (Didactiek G8 batch 8 deel B, les 372; Z-#984): vormcue in meerkeuze. Het goede antwoord mag niet aan zijn vorm te herkennen zijn.
Z-#1000–#1003 (Didactiek 8 okt 18:35, signalen-buiten-g8-didactiek.md, les 383): 'dec' = één vaste regel over het somtype ('kies de enige optie met k decimalen',
beste k); rang (grootste/kleinste waarde, niet bij een superlatief in de vraag); grens > 50 % én binomiaal p < 0,01 t.o.v. 1/3 (toeval bij weinig items gaat door).
Oorspronkelijk (V-#984): per item met getal-opties (een getal met eventueel '%', '€' of een eenheid) drie heuristieken:
  dec   het goede antwoord is de enige optie met zijn aantal decimalen;
  kort  het goede antwoord is strikt de kortste optie (tekens);
  lang  het goede antwoord is strikt de langste optie.
Per somtype (doel + somtypeNr, vanaf MIN_ITEMS items): aandeel items waarin een heuristiek het goede antwoord geeft. FAIL als een aandeel > GRENS
(0,40: Didactiek liet 'ongeveer een derde' xx,5% toe). Oud E06 #1 (96/96 'dec') moet FAIL geven (mutant).
V-#1050–#1055 (Didactiek 8 okt 19:35, 'Vormcue 50% (19:17)'): FAIL in de gates G3–G7. Zacht: Z-#1050 bedragen in centen vergelijken (€x = 100x cent);
Z-#1051 WARN bij > 60 % en n ≥ 8, ook als p ≥ 0,01 (les 407); Z-#1052 INFO 'nooit de grootste/kleinste' (n ≥ 8, zwakkere cue: wegstrepen geeft 50 %).
Didactiek 19:57 (besluit 'middelste'): één regel voor alle drie de posities. Positie = rang van het goede antwoord onder de opties
(kleinste / middelste / grootste; middelste alleen bij precies 3 opties met 3 verschillende waarden; niet bij een superlatief in de vraag).
Geen positie > 50 % met binomiaal p < 0,01 (kans 1/3) = FAIL; de drempel blijft. Per positie een FAIL-mutant en een grensmutant (precies 50 %).
Gebruik: import vormcue_check as VC; VC.rapport(items); VC.posities(items); python3 vormcue_check.py --mutanten"""
import re, sys, collections, math
GRENS = 0.50; MIN_ITEMS = 6; P_MAX = 0.01; GRENS_RANG = GRENS; POSITIES = ('klein', 'midden', 'groot');      # 19:57: één regel voor alle posities (GRENS_RANG = GRENS)
GRENS_RANG = GRENS; GRENS_WARN = 0.60; MIN_WARN = 8      # Z-#1051: WARN boven 60 % bij n ≥ 8 (ook p ≥ 0,01); V-#1032 (Didactiek 19:09, lijn V-#984/#1000): rang > 50 % én p < 0,01 = FAIL (was WARN tot 80 %); rang (Z-#1000/#1001): 'altijd de grootste/kleinste' = FAIL vanaf 80 %; > 50 % (en p < 0,01) = WARN      # Z-#1003 (Didactiek 18:35): grens boven 50% én binomiale toets t.o.v. 1/3 (p < 0,01); toeval bij weinig items gaat zo door
RX = re.compile(r'^(?:€ ?)?(\d+(?:\.\d{3})*(?:,(\d+))?)(?: ?(?:%|procent|[a-zA-Z²³]+))?$')
def _dec(t):
    m = RX.match(str(t).strip())
    return None if not m else len(m.group(2) or '')
def _waarde(t):
    """Z-#1050 (les 406): bedragen in één eenheid: '€3' = 300 cent, '40 cent' = 40 cent (anders is '€3' < '40 cent')"""
    t = str(t).strip(); m = RX.match(t)
    if not m: return None
    w = float(m.group(1).replace('.', '').replace(',', '.'))
    return w * 100 if t.startswith('€') else w
SUPERLATIEF = re.compile(r'\b(?:grootst|kleinst|hoogst|laagst|meest|minst|langst|kortst|zwaarst|lichtst|duurst|goedkoopst|snelst|traagst|breedst|smalst|dikst|dunst|oudst|jongst)e?\b', re.I)      # 'Welk getal is het grootst?': rang is daar de vraag zelf
def _notatie(t):
    t = str(t).strip(); return '€' if t.startswith('€') else ('cent' if t.endswith('cent') else '')
def _p_binom(n, k, p=1 / 3): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
def cues(it):
    """per item: dec = {k: 'kies de enige optie met k decimalen' wijst het goede antwoord aan} (Z-#1002, les 383: één vaste regel over het somtype);
    kort/lang = het goede antwoord is strikt de kortste/langste optie; groot/klein = strikt de grootste/kleinste waarde (Z-#1000/#1001)."""
    ops = [o.get('tekst') for o in it.get('opties') or []]; goed = str(it.get('antwoord'))
    if it.get('type') != 'meerkeuze' or len(ops) < 3 or goed not in ops or any(_dec(o) is None for o in ops): return None
    d = [_dec(o) for o in ops]; L = [len(str(o)) for o in ops]; W = [_waarde(o) for o in ops]; i = ops.index(goed); r = L[:i] + L[i + 1:]; w = W[:i] + W[i + 1:]
    sup = bool(SUPERLATIEF.search(str(it.get('opgave') or '')))
    nt = [_notatie(o) for o in ops]; z = [W[j] for j in range(len(ops)) if j != i and nt[j] == nt[i]]      # Z-#1050: rang binnen dezelfde notatie (G4-MEET-E07: 'kies het grootste centbedrag')
    ge, ke = (not sup and bool(z) and W[i] > max(z)), (not sup and bool(z) and W[i] < min(z))
    mid = not sup and len(ops) == 3 and len(set(W)) == 3 and min(w) < W[i] < max(w)      # V-#1040 (les 400): rang 'middelste'
    return {'midden': mid, 'groot_e': ge, 'klein_e': ke, 'sup': sup, 'dec': {d[i]} if d.count(d[i]) == 1 else set(), 'kort': L[i] < min(r), 'lang': L[i] > max(r), 'groot': not sup and W[i] > max(w), 'klein': not sup and W[i] < min(w)}
def per_somtype(items):
    S = collections.defaultdict(list)
    for it in items:
        c = cues(it)
        if c is not None: S[((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNr'))].append(c)
    return S
def tellingen(L):
    """{heuristiek: aantal items waarin hij het goede antwoord geeft}; 'dec' = de beste vaste k over het somtype (bijv. 'kies het bedrag met centen')."""
    ks = collections.Counter(k for c in L for k in c['dec'])
    T = {h: sum(c[h] for c in L) for h in ('kort', 'lang', 'groot', 'klein', 'groot_e', 'klein_e', 'midden')}
    for h in ('groot', 'klein'):
        if T[h + '_e'] == T[h]: del T[h + '_e']      # zonder gemengde notatie is het dezelfde cue
    T['dec'] = max(ks.values()) if ks else 0
    return T
def fail_regel(n, m):
    """De ene regel (Didactiek 19:57): meer dan 50 % én binomiaal p < 0,01 t.o.v. 1/3."""
    return n >= MIN_ITEMS and m / n > GRENS and _p_binom(n, m) < P_MAX
def posities(items):
    """Per somtype: {'n': items met getal-opties, 'klein'/'midden'/'groot': aantal keer goed op die positie, 'geen': geen positie
    (superlatief, gelijke waarden, of bij 4+ opties niet de kleinste/grootste)}."""
    U = {}
    for k, L in per_somtype(items).items():
        t = {h: sum(1 for c in L if c[h]) for h in POSITIES}; t['n'] = len(L); t['geen'] = len(L) - sum(t[h] for h in POSITIES); U[k] = t
    return U
def min_wissel(t, ondergrens=0.10, strikt=False):
    """Minimaal aantal items dat van de dominante positie naar een andere moet (één afleider per item vervangen), zodat de regel niet meer
    vuurt (strikt=True: aandeel < 50 %), en geen positie onder ~10 % zakt (Z-#1052). Verplaatsen gaat eerst naar een positie onder de ondergrens,
    daarna naar de laagste. Geeft (aantal, verdeling na)."""
    n = t['n']; v = {h: t[h] for h in POSITIES}; d = max(POSITIES, key=lambda h: v[h]); s = 0
    def ok(): return (v[d] / n < GRENS if strikt else not fail_regel(n, v[d])) and all(v[h] >= ondergrens * n for h in POSITIES if h != d)
    while not ok() and v[d] > 0:
        laag = [h for h in POSITIES if h != d and v[h] < ondergrens * n]
        h = laag[0] if laag else min((h for h in POSITIES if h != d), key=lambda h: v[h])
        v[d] -= 1; v[h] += 1; s += 1
    return s, v
def _oordeel(items):
    F, W = [], []
    naam = {'dec': 'de enige optie met dat aantal decimalen', 'kort': 'de kortste optie', 'lang': 'de langste optie', 'groot': 'de grootste optie', 'klein': 'de kleinste optie', 'groot_e': 'het grootste bedrag in dezelfde notatie (cent/€)', 'klein_e': 'het kleinste bedrag in dezelfde notatie (cent/€)', 'midden': 'de middelste optie'}
    for k, L in per_somtype(items).items():
        n = len(L)
        if n < MIN_ITEMS: continue
        for h, m in tellingen(L).items():
            x = f'{k[0]} #{k[1]}: goed = {naam[h]} in {m}/{n} items'
            if not fail_regel(n, m):
                if m / n > GRENS_WARN and n >= MIN_WARN: W.append(x + ' (Z-#1051: > 60 %, p ≥ 0,01)')
                continue
            F.append(x)      # 19:57: dezelfde regel voor vorm (dec/kort/lang) en voor elke positie (kleinste/middelste/grootste)
    return F, W
def nooit(items):
    """Z-#1052 (zacht): 'nooit de grootste/kleinste' per somtype (n ≥ 8, items zonder superlatief) — wegstrepen geeft het kind 50 % in plaats van 33 %"""
    I = []
    for k, L in per_somtype(items).items():
        L = [c for c in L if not c['sup']]
        if len(L) < MIN_WARN: continue
        for h, nm in (('groot', 'grootste'), ('midden', 'middelste'), ('klein', 'kleinste')):      # 19:57: alle drie de posities (zacht)
            if h == 'midden' and not any(c['groot'] or c['klein'] or c['midden'] for c in L): continue
            if not any(c[h] for c in L): I.append(f'{k[0]} #{k[1]}: goed is nooit de {nm} (0/{len(L)})')
    return I
def fouten(items): return _oordeel(items)[0]
def waarschuwingen(items): return _oordeel(items)[1]
def rapport(items, toon=True, ernst='FAIL'):
    F, W = _oordeel(items)
    if toon:
        print(f"\nVORMCUE (V-#984/Z-#1000–#1003/V-#1040: goede optie niet aan vorm of rang (grootste/middelste/kleinste) te herkennen; per somtype > {GRENS:.0%} en binomiaal p < {P_MAX} t.o.v. 1/3; één regel voor vorm en voor elke positie, besluit 19:57): {len(F)} ({ernst}) · {len(W)} (WARN)")
        for x in F[:12]: print(f'  {ernst} VORMCUE', x)
        for x in W[:12]: print('  WARN VORMCUE', x)
        N = nooit(items)
        if N: print(f'  INFO VORMCUE-NOOIT (Z-#1052, zacht): {len(N)} · ' + ' · '.join(N[:8]))
    return len(F)
def _it(n, goed, ops): return {'type': 'meerkeuze', 'antwoord': goed, 'opties': [{'tekst': o} for o in ops], 'merge': {'doel': 'MUT', 'somtypeNr': n}}
MUTANTEN = [('oud E06 #1: alleen het goede antwoord heeft één decimaal', [_it(1, f'{x},5%', [f'{x},5%', f'{x / 10:.2f}%'.replace('.', ','), f'0,{x}5%']) for x in range(11, 21)], True),
            ('nieuw: hele procenten met een afleider met evenveel decimalen (rang gespreid: V-#1040 telt nu ook de middelste)', [_it(2, f'{x}0%', [[f'{x}%', f'{x}0%', f'{x}00%'], [f'{x}0%', f'{x}00%', f'{x}000%'], [f'{x}0%', f'{x}%', f'{x * 5}%']][x % 3]) for x in range(1, 10)], False),
            ('kortste optie is steeds goed', [_it(3, f'{x}%', [f'{x}%', f'{x}0,5%', f'0,{x}55%']) for x in range(11, 21)], True),
            ('Z-#1000: oud G8 E06 #2, goede antwoord steeds de grootste optie', [_it(4, g, o) for g, o in [('52,5%', ['5,25%', '52,5%', '21%']), ('35%', ['7%', '35%', '3,5%']), ('36%', ['9%', '3,6%', '36%']), ('26%', ['26%', '13%', '2,6%']), ('15%', ['6%', '15%', '1,5%']), ('55%', ['11%', '5,5%', '55%']), ('72%', ['72%', '18%', '7,2%'])]], True),
            ('Z-#1000: nieuw G8 E06 #2 (× 10 in 4 items)', [_it(5, g, o) for g, o in [('52,5%', ['5,25%', '52,5%', '21%']), ('35%', ['7%', '35%', '350%']), ('36%', ['9%', '3,6%', '36%']), ('26%', ['26%', '13%', '260%']), ('15%', ['6%', '15%', '1,5%']), ('55%', ['11%', '550%', '55%']), ('72%', ['72%', '18%', '720%'])]], False),
            ('Z-#1002: alle drie de opties een ander aantal decimalen (G7-GET-02-vorm), goede antwoord verdeeld 1/2/3 decimalen', [_it(6, g, o) for g, o in [('0,5', ['0,5', '0,45', '0,125']), ('0,45', ['0,5', '0,45', '0,125']), ('0,125', ['0,5', '0,45', '0,125'])] * 4], False),
            ('V-#1001: G5-MEET-E07-vorm, alleen het goede antwoord heeft centen (66%)', [_it(8, g, o) for g, o in [('€7,50', ['€5', '€7,50', '€7'])] * 12 + [('€5', ['€5', '€4,50', '€6'])] * 6], True),
            ('superlatief: «Welk getal is het grootst?» (rang is de vraag)', [dict(_it(9, g, o), opgave='Welk getal is het grootst?') for g, o in [('5,9', ['5,38', '5,9', '5,103']), ('0,403', ['0,12', '0,3', '0,403']), ('1,603', ['1,22', '1,603', '1,5'])] * 3], False),
            ('V-#1040: G8-MEET-V01 #1 na V-#1032, goed = middelste in 78/151', [_it(14, g, o) for g, o in [('12', ['16', '12', '7'])] * 78 + [('20', ['20', '9', '16'])] * 69 + [('6', ['6', '9', '12'])] * 4], True),
            ('V-#1040: na de datafix middelste 74/151 (49 %)', [_it(15, g, o) for g, o in [('12', ['16', '12', '7'])] * 74 + [('20', ['20', '9', '16'])] * 69 + [('6', ['6', '9', '12'])] * 8], False),
            # 19:57: per positie een FAIL-mutant (32/60 = 53 %, p < 0,01) en een grensmutant (30/60 = 50 %: niet boven 50 %, geen FAIL)
            ('19:57 kleinste 32/60', [_it(20, g, o) for g, o in [('3', ['3', '5', '9'])] * 32 + [('5', ['3', '5', '9'])] * 14 + [('9', ['3', '5', '9'])] * 14], True),
            ('19:57 middelste 32/60', [_it(21, g, o) for g, o in [('5', ['3', '5', '9'])] * 32 + [('3', ['3', '5', '9'])] * 14 + [('9', ['3', '5', '9'])] * 14], True),
            ('19:57 grootste 32/60', [_it(22, g, o) for g, o in [('9', ['3', '5', '9'])] * 32 + [('3', ['3', '5', '9'])] * 14 + [('5', ['3', '5', '9'])] * 14], True),
            ('19:57 grens kleinste 30/60', [_it(23, g, o) for g, o in [('3', ['3', '5', '9'])] * 30 + [('5', ['3', '5', '9'])] * 15 + [('9', ['3', '5', '9'])] * 15], False),
            ('19:57 grens middelste 30/60', [_it(24, g, o) for g, o in [('5', ['3', '5', '9'])] * 30 + [('3', ['3', '5', '9'])] * 15 + [('9', ['3', '5', '9'])] * 15], False),
            ('19:57 grens grootste 30/60', [_it(25, g, o) for g, o in [('9', ['3', '5', '9'])] * 30 + [('3', ['3', '5', '9'])] * 15 + [('5', ['3', '5', '9'])] * 15], False),
            ('Z-#1003: langste optie in 5/11 (toeval, G4-MEET-E02-vorm)', [_it(7, g, o) for g, o in [('15 cm', ['15 cm', '15 m', '1 m'])] * 5 + [('2 m', ['2 m', '20 cm', '200 cm'])] * 6], False)]
MUTANTEN_Z = [('Z-#1050 M6: 12× [€1, 90 cent, 50 cent], goed = €1 (echt de grootste)', [_it(10, '€1', ['€1', '90 cent', '50 cent'])] * 12, 'de grootste optie'),
              ('Z-#1050 M5: 12× [40 cent, €3, €40], goed = 40 cent (echt de kleinste)', [_it(11, '40 cent', ['40 cent', '€3', '€40'])] * 12, 'de kleinste optie'),
              ('Z-#1050: G4-MEET-E07-vorm, goed = grootste centbedrag naast een €-afleider', [_it(13, g, o) for g, o in [('80 cent', ['75 cent', '€80', '80 cent']), ('60 cent', ['€6', '50 cent', '60 cent'])] * 6], 'het grootste bedrag'),
              ('Z-#1051 M3-vorm: grootste 11/18 (p ≈ 0,014) → WARN', [_it(12, '9', ['9', '5', '3'])] * 11 + [_it(12, '5', ['9', '5', '3'])] * 7, 'WARN')]
def mutanten_z_ok():
    uit = []
    for n, L, v in MUTANTEN_Z:
        F, W = _oordeel(L)
        uit.append(any('Z-#1051' in x for x in W) if v == 'WARN' else any(v in x for x in F))
    return uit
def _mut_ok(n, L, v):
    F = fouten(L)
    if bool(F) != v: return False
    pos = next((p for p in ('kleinste', 'middelste', 'grootste') if n.startswith('19:57 ' + p)), None)      # 19:57: de FAIL noemt de juiste positie
    return not (v and pos) or any(f'de {pos} optie' in x for x in F)
def mutanten_ok(): return all(_mut_ok(n, L, v) for n, L, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, L, v in MUTANTEN: print(('ok  ' if _mut_ok(n, L, v) else 'MIS ') + n, fouten(L))
    print('mutanten VORMCUE:', sum(_mut_ok(n, L, v) for n, L, v in MUTANTEN), '/', len(MUTANTEN), '· zacht Z-#1050/#1051:', sum(mutanten_z_ok()), '/', len(MUTANTEN_Z)); sys.exit(0 if mutanten_ok() and all(mutanten_z_ok()) else 1)
