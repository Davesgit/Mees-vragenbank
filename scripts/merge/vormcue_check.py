"""V-#984 (Didactiek G8 batch 8 deel B, les 372; Z-#984): vormcue in meerkeuze. Het goede antwoord mag niet aan zijn vorm te herkennen zijn.
Z-#1000–#1003 (Didactiek 8 okt 18:35, signalen-buiten-g8-didactiek.md, les 383): 'dec' = één vaste regel over het somtype ('kies de enige optie met k decimalen',
beste k); rang (grootste/kleinste waarde, niet bij een superlatief in de vraag); grens > 50 % én binomiaal p < 0,01 t.o.v. 1/3 (toeval bij weinig items gaat door).
Oorspronkelijk (V-#984): per item met getal-opties (een getal met eventueel '%', '€' of een eenheid) drie heuristieken:
  dec   het goede antwoord is de enige optie met zijn aantal decimalen;
  kort  het goede antwoord is strikt de kortste optie (tekens);
  lang  het goede antwoord is strikt de langste optie.
Per somtype (doel + somtypeNr, vanaf MIN_ITEMS items): aandeel items waarin een heuristiek het goede antwoord geeft. FAIL als een aandeel > GRENS
(0,40: Didactiek liet 'ongeveer een derde' xx,5% toe). Oud E06 #1 (96/96 'dec') moet FAIL geven (mutant).
Gebruik: import vormcue_check as VC; VC.rapport(items); python3 vormcue_check.py --mutanten"""
import re, sys, collections, math
GRENS = 0.50; MIN_ITEMS = 6; P_MAX = 0.01; GRENS_RANG = 0.80      # rang (Z-#1000/#1001): 'altijd de grootste/kleinste' = FAIL vanaf 80 %; > 50 % (en p < 0,01) = WARN      # Z-#1003 (Didactiek 18:35): grens boven 50% én binomiale toets t.o.v. 1/3 (p < 0,01); toeval bij weinig items gaat zo door
RX = re.compile(r'^(?:€ ?)?(\d+(?:\.\d{3})*(?:,(\d+))?)(?: ?(?:%|procent|[a-zA-Z²³]+))?$')
def _dec(t):
    m = RX.match(str(t).strip())
    return None if not m else len(m.group(2) or '')
def _waarde(t):
    m = RX.match(str(t).strip())
    return None if not m else float(m.group(1).replace('.', '').replace(',', '.'))
SUPERLATIEF = re.compile(r'\b(?:grootst|kleinst|hoogst|laagst|meest|minst|langst|kortst|zwaarst|lichtst|duurst|goedkoopst|snelst|traagst|breedst|smalst|dikst|dunst|oudst|jongst)e?\b', re.I)      # 'Welk getal is het grootst?': rang is daar de vraag zelf
def _p_binom(n, k, p=1 / 3): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
def cues(it):
    """per item: dec = {k: 'kies de enige optie met k decimalen' wijst het goede antwoord aan} (Z-#1002, les 383: één vaste regel over het somtype);
    kort/lang = het goede antwoord is strikt de kortste/langste optie; groot/klein = strikt de grootste/kleinste waarde (Z-#1000/#1001)."""
    ops = [o.get('tekst') for o in it.get('opties') or []]; goed = str(it.get('antwoord'))
    if it.get('type') != 'meerkeuze' or len(ops) < 3 or goed not in ops or any(_dec(o) is None for o in ops): return None
    d = [_dec(o) for o in ops]; L = [len(str(o)) for o in ops]; W = [_waarde(o) for o in ops]; i = ops.index(goed); r = L[:i] + L[i + 1:]; w = W[:i] + W[i + 1:]
    sup = bool(SUPERLATIEF.search(str(it.get('opgave') or '')))
    return {'dec': {d[i]} if d.count(d[i]) == 1 else set(), 'kort': L[i] < min(r), 'lang': L[i] > max(r), 'groot': not sup and W[i] > max(w), 'klein': not sup and W[i] < min(w)}
def per_somtype(items):
    S = collections.defaultdict(list)
    for it in items:
        c = cues(it)
        if c is not None: S[((it.get('merge') or {}).get('doel'), (it.get('merge') or {}).get('somtypeNr'))].append(c)
    return S
def tellingen(L):
    """{heuristiek: aantal items waarin hij het goede antwoord geeft}; 'dec' = de beste vaste k over het somtype (bijv. 'kies het bedrag met centen')."""
    ks = collections.Counter(k for c in L for k in c['dec'])
    T = {h: sum(c[h] for c in L) for h in ('kort', 'lang', 'groot', 'klein')}
    T['dec'] = max(ks.values()) if ks else 0
    return T
def _oordeel(items):
    F, W = [], []
    naam = {'dec': 'de enige optie met dat aantal decimalen', 'kort': 'de kortste optie', 'lang': 'de langste optie', 'groot': 'de grootste optie', 'klein': 'de kleinste optie'}
    for k, L in per_somtype(items).items():
        n = len(L)
        if n < MIN_ITEMS: continue
        for h, m in tellingen(L).items():
            if not (m / n > GRENS and _p_binom(n, m) < P_MAX): continue
            x = f'{k[0]} #{k[1]}: goed = {naam[h]} in {m}/{n} items'
            (W if h in ('groot', 'klein') and m / n < GRENS_RANG else F).append(x)
    return F, W
def fouten(items): return _oordeel(items)[0]
def waarschuwingen(items): return _oordeel(items)[1]
def rapport(items, toon=True, ernst='FAIL'):
    F, W = _oordeel(items)
    if toon:
        print(f"\nVORMCUE (V-#984/Z-#1000–#1003: goede optie niet aan vorm of rang te herkennen; per somtype > {GRENS:.0%} en binomiaal p < {P_MAX} t.o.v. 1/3; rang FAIL vanaf {GRENS_RANG:.0%}): {len(F)} ({ernst}) · {len(W)} (WARN)")
        for x in F[:12]: print(f'  {ernst} VORMCUE', x)
        for x in W[:12]: print('  WARN VORMCUE', x)
    return len(F)
def _it(n, goed, ops): return {'type': 'meerkeuze', 'antwoord': goed, 'opties': [{'tekst': o} for o in ops], 'merge': {'doel': 'MUT', 'somtypeNr': n}}
MUTANTEN = [('oud E06 #1: alleen het goede antwoord heeft één decimaal', [_it(1, f'{x},5%', [f'{x},5%', f'{x / 10:.2f}%'.replace('.', ','), f'0,{x}5%']) for x in range(11, 21)], True),
            ('nieuw: hele procenten met een afleider met evenveel decimalen', [_it(2, f'{x}0%', [f'{x}%', f'{x}0%', f'{x}00%']) for x in range(1, 10)], False),
            ('kortste optie is steeds goed', [_it(3, f'{x}%', [f'{x}%', f'{x}0,5%', f'0,{x}55%']) for x in range(11, 21)], True),
            ('Z-#1000: oud G8 E06 #2, goede antwoord steeds de grootste optie', [_it(4, g, o) for g, o in [('52,5%', ['5,25%', '52,5%', '21%']), ('35%', ['7%', '35%', '3,5%']), ('36%', ['9%', '3,6%', '36%']), ('26%', ['26%', '13%', '2,6%']), ('15%', ['6%', '15%', '1,5%']), ('55%', ['11%', '5,5%', '55%']), ('72%', ['72%', '18%', '7,2%'])]], True),
            ('Z-#1000: nieuw G8 E06 #2 (× 10 in 4 items)', [_it(5, g, o) for g, o in [('52,5%', ['5,25%', '52,5%', '21%']), ('35%', ['7%', '35%', '350%']), ('36%', ['9%', '3,6%', '36%']), ('26%', ['26%', '13%', '260%']), ('15%', ['6%', '15%', '1,5%']), ('55%', ['11%', '550%', '55%']), ('72%', ['72%', '18%', '720%'])]], False),
            ('Z-#1002: alle drie de opties een ander aantal decimalen (G7-GET-02-vorm), goede antwoord verdeeld 1/2/3 decimalen', [_it(6, g, o) for g, o in [('0,5', ['0,5', '0,45', '0,125']), ('0,45', ['0,5', '0,45', '0,125']), ('0,125', ['0,5', '0,45', '0,125'])] * 4], False),
            ('V-#1001: G5-MEET-E07-vorm, alleen het goede antwoord heeft centen (66%)', [_it(8, g, o) for g, o in [('€7,50', ['€5', '€7,50', '€7'])] * 12 + [('€5', ['€5', '€4,50', '€6'])] * 6], True),
            ('superlatief: «Welk getal is het grootst?» (rang is de vraag)', [dict(_it(9, g, o), opgave='Welk getal is het grootst?') for g, o in [('5,9', ['5,38', '5,9', '5,103']), ('0,403', ['0,12', '0,3', '0,403']), ('1,603', ['1,22', '1,603', '1,5'])] * 3], False),
            ('Z-#1003: langste optie in 5/11 (toeval, G4-MEET-E02-vorm)', [_it(7, g, o) for g, o in [('15 cm', ['15 cm', '15 m', '1 m'])] * 5 + [('2 m', ['2 m', '20 cm', '200 cm'])] * 6], False)]
def mutanten_ok(): return all(bool(fouten(L)) == v for _, L, v in MUTANTEN)
if __name__ == '__main__' and '--mutanten' in sys.argv:
    for n, L, v in MUTANTEN: print(('ok  ' if bool(fouten(L)) == v else 'MIS ') + n, fouten(L))
    print('mutanten VORMCUE:', sum(bool(fouten(L)) == v for _, L, v in MUTANTEN), '/', len(MUTANTEN)); sys.exit(0 if mutanten_ok() else 1)
