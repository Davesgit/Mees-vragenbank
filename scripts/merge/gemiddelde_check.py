"""GEMIDDELDE-check (V-#820/Z-#823, les 195; uitgebreid met Z-#841 en Z-#855, besluit Didactiek 8 okt 16:15, g8/gemiddelde-check-didactiek.md).
Bij een gemiddelde-vraag met een getal als antwoord:
  regel 1  het antwoord is een gegeven waarde uit de vraag (WARN per item);
  regel 2  meerkeuze: het antwoord is de middelste optie en alle andere opties liggen buiten kleinste–grootste gegeven waarde (WARN);
           alleen bij 3 of meer gegeven waarden (Z-#841; bij twee waarden is het midden altijd het gemiddelde, les 305);
  Z-#860   twee waarden in een meerkeuze en geen afleider tussen die twee: WARN (schatten beslist; neem drie waarden, les 305).
  routes   (Z-#855, vanaf 3 waarden) vijf foute routes: mediaan (bij een even aantal: elk van de twee middelste en hun gemiddelde),
           meest voorkomend, middelste in de volgorde van de opgave, midden van kleinste en grootste, een gegeven waarde.
           Geeft een route het goede antwoord: WARN per item. FAIL als één route bij ≥ 1/3 van de gemiddelde-items van het somtype raakt,
           of als het somtype een eigen sleutel voor die route heeft (de build laat die sleutel dan stil weg, les 306; bv. 'middelste getal'
           bij G7 427, 'getal uit de vraag' bij G6 008).
Gegeven waarden: een opsomming ('6, 6, 3, 3 en 7', '15, 11, 12, 9, 13 eieren', '2 km, 7 km, 5 km en 2 km'); anders de getallen met hetzelfde
woord erachter als dat minstens twee keer voorkomt ('210 mensen … 320 mensen … 280 mensen'); anders alle getallen (alleen voor regel 1).
Gebruik: import gemiddelde_check as GM; fails, warns = GM.rapport(items, base)   (base = map van de groep, voor de sleutels in hints/batch*.json)
         python3 gemiddelde_check.py --mutanten   (oude data van G7 427, G6 010 en G8 002)"""
import re, json, glob, os, sys, collections
from fractions import Fraction as F
GET = r'\d+(?:\.\d{3})*(?:,\d+)?'
def _f(x): return F(x.replace('.', '').replace(',', '.'))
def _getal(t):
    m = re.search(GET, str(t or '')); return _f(m.group(0)) if m else None
def waarden(o):
    """(lijst, bron): de gegeven waarden in de volgorde van de opgave"""
    U = r'(?: (?!en\b)[a-zà-ÿ]+)?'
    m = re.search(rf'(?<![\d,]){GET}{U}(?:, {GET}{U})+(?:,? en {GET}{U})?|(?<![\d,]){GET}{U} en {GET}{U}(?![\d,])', o)
    if m and len(re.findall(GET, m.group(0))) >= 2: return [_f(x) for x in re.findall(GET, m.group(0))], 'opsomming'
    paren = re.findall(rf'(?<![\d,])({GET}) ([a-zà-ÿ]+)', o); c = collections.Counter(w for _, w in paren)
    if c:
        w, k = c.most_common(1)[0]
        if k >= 2: return [_f(x) for x, ww in paren if ww == w], 'zelfde woord'
    return [_f(x) for x in re.findall(rf'(?<![\d,]){GET}(?![\d,])', o)], 'alle getallen'
def routes(v):
    n = len(v); s = sorted(v); R = {}
    R['mediaan'] = {s[n // 2]} if n % 2 else {s[n // 2 - 1], s[n // 2], (s[n // 2 - 1] + s[n // 2]) / 2}
    c = collections.Counter(v); top = max(c.values())
    if top > 1: R['meest voorkomend'] = {x for x in c if c[x] == top}
    R['middelste genoemde'] = {v[n // 2]} if n % 2 else {v[n // 2 - 1], v[n // 2]}
    R['midden van kleinste en grootste'] = {(min(v) + max(v)) / 2}
    R['gegeven waarde'] = set(v)
    return R
SLEUTEL = {'mediaan': r'middelste getal|mediaan', 'meest voorkomend': r'meest voorkomend|vaakst|modus', 'middelste genoemde': r'middelste genoemd',
           'midden van kleinste en grootste': r'kleinste en grootste|midden van|uitersten', 'gegeven waarde': r'getal uit de vraag|gegeven waarde'}
def sleutels(base):
    """(doel, nrOrigineel) → alle regels (kleine letters) van de hint-entry"""
    S = collections.defaultdict(str)
    for p in sorted(glob.glob(os.path.join(base or '', 'hints', 'batch*.json'))):
        for st in json.load(open(p, encoding='utf-8')).get('somtypen', []):
            S[(st['doel'], st.get('nrOrigineel'))] += ' ' + ' '.join(str(f.get('regel') or '') + ' ' + str(f.get('soort') or '') for f in st.get('foutHints') or []).lower()
    return S
def is_gem(it):
    o = it.get('opgave') or ''
    if not re.search(r'\bgemiddeld(e)?\b', o, re.I) or re.search(r'gemiddeld \d', o): return False      # 'heeft gemiddeld 5' = gegeven gemiddelde
    return bool(re.fullmatch(rf'{GET}(?: [a-zà-ÿ]+)?', str(it.get('antwoord') or '').strip()))
def analyse(items, base=None):
    S = sleutels(base) if base else {}
    W = []; per = collections.defaultdict(lambda: {'n': 0, 'hits': collections.Counter(), 'items': collections.defaultdict(list), 'sleutel': set()})
    for it in items:
        if not is_gem(it): continue
        o = it['opgave']; a = _getal(it['antwoord']); v, bron = waarden(o)
        key = ((it.get('merge') or {}).get('doel') or it.get('doelId'), (it.get('merge') or {}).get('somtypeNrOrigineel'))
        P = per[key]; P['n'] += 1
        if a in v and bron == 'alle getallen': W.append(f"{it['id']}: het gemiddelde {it['antwoord']} staat ook als gegeven waarde in de vraag")
        ops = [_getal(x.get('tekst')) for x in it.get('opties') or []]
        if len(v) >= 3 and len(ops) >= 3 and None not in ops:
            lo, hi = min(v), max(v); rest = [x for x in ops if x != a]
            if sorted(ops)[len(ops) // 2] == a and all(x < lo or x > hi for x in rest):
                W.append(f"{it['id']}: het goede antwoord {it['antwoord']} is de middelste optie en de andere opties ({', '.join(str(x.get('tekst')) for x in it['opties'] if _getal(x.get('tekst')) != a)}) liggen buiten {float(lo):g}–{float(hi):g}")
        # Z-#860 (Didactiek recheck gemiddelde, 16:3x; les 305): bij twee waarden in een meerkeuze is het midden altijd het gemiddelde. Ligt geen afleider
        # tussen de twee waarden, dan beslist schatten (het oude probleem van G8 002): WARN 'neem drie waarden'.
        if len(v) == 2 and bron != 'alle getallen' and len(ops) >= 3 and None not in ops:
            lo, hi = min(v), max(v)
            if not any(lo < x < hi for x in ops if x != a):
                W.append(f"{it['id']}: twee waarden ({float(lo):g} en {float(hi):g}) en geen afleider ertussen: schatten beslist; neem drie waarden (Z-#860, les 305)")
        if len(v) >= 3 and bron != 'alle getallen':
            h = [r for r, X in routes(v).items() if a in X]
            for r in h:
                P['hits'][r] += 1; P['items'][r].append(it['id'])
                if S and re.search(SLEUTEL[r], S.get(key, '')): P['sleutel'].add(r)
            if h: W.append(f"{it['id']}: {', '.join(float(x).__format__('g') for x in v)} → {it['antwoord']}: foute route(s) geven het goede antwoord: {', '.join(h)}")
    Fl = []
    for key, P in per.items():
        for r, k in P['hits'].items():
            if 3 * k >= P['n']: Fl.append(f"{key[0]} somtype nrO {key[1]}: route '{r}' geeft het goede antwoord bij {k}/{P['n']} items (≥ 1/3): {', '.join(P['items'][r])}")
            elif r in P['sleutel']: Fl.append(f"{key[0]} somtype nrO {key[1]}: route '{r}' geeft het goede antwoord ({', '.join(P['items'][r])}) en de bank heeft er een eigen sleutel voor (les 306)")
    return Fl, W, per
def treffers(items, base=None):
    Fl, W, _ = analyse(items, base); return Fl + W
def rapport(items, base=None, toon=True, ernst='FAIL'):
    Fl, W, per = analyse(items, base)
    if toon:
        print(f"\nGEMIDDELDE (V-#820/Z-#823/Z-#841/Z-#855: gemiddelde-vragen, vijf foute routes): {len(Fl)} ({ernst}) · {len(W)} (WARN) · somtypes met gemiddelde-items: {len(per)}")
        for x in Fl: print(f'  {ernst} GEMIDDELDE', x)
        for x in W[:15]: print('  WARN GEMIDDELDE', x)
        for key, P in sorted(per.items(), key=lambda kv: str(kv[0])):
            if P['hits']: print(f"  aandeel {key[0]} nrO {key[1]}: " + ', '.join(f"{r} {k}/{P['n']}" for r, k in P['hits'].items()))
    return Fl, W
def samen_treffers(items):
    """V-#1011 (Didactiek r13, les 385): een fout-hint «Dat is alles samen…» / «… is het totaal» alleen als de fout gelijk is aan de som van de gegeven waarden (FAIL).
    Kijkt in foutRegels (tekst + match.waarden) en foutHints (fout + uitleg) van gemiddelde-items."""
    T = []
    for it in items:
        if not is_gem(it): continue
        v, bron = waarden(it.get('opgave') or '')
        if bron != 'opsomming': continue      # gewogen gemiddelde ('Twaalf kinderen hebben een 5, …'): de som is niet de som van de genoemde getallen
        som = sum(v) if v else None
        paren = [(w, f.get('tekst') or '') for f in it.get('foutRegels') or [] for w in ((f.get('match') or {}).get('waarden') or [])]
        paren += [(f.get('fout'), f.get('uitleg') or '') for f in it.get('foutHints') or []]
        for w, t in paren:
            if not re.search(r'alles samen|\bis het totaal\b', t, re.I): continue
            g = _getal(w)
            if som is None or g is None or g != som: T.append(f"{it['id']}: '{w}' krijgt «{t[:40]}…», maar de som is {som}")
    return T
def samen_mutanten_ok():
    oud = {'id': 'mut-G6-E08-011', 'opgave': '4 kinderen verzamelden stickers. Ze hadden er 6, 3, 8 en 3. Hoeveel stickers is dat gemiddeld per kind?', 'antwoord': '5',
           'foutRegels': [{'tekst': 'Dat is alles samen. Deel dat nog door het aantal.', 'match': {'waarden': ['7', '20']}}]}
    nieuw = dict(oud, foutRegels=[{'tekst': 'Dat is alles samen. Deel dat nog door het aantal.', 'match': {'waarden': ['20']}}])
    return bool(samen_treffers([oud])) and not samen_treffers([nieuw])
def _item(id_, o, a, opties=None, doel='MUT', nro=1): return {'id': id_, 'opgave': o, 'antwoord': a, 'opties': [{'tekst': t} for t in opties or []], 'merge': {'doel': doel, 'somtypeNrOrigineel': nro}}
MUTANTEN = [   # (naam, items, verwacht: 'FAIL' / 'WARN' / 'geen')
    ('oud G7 427 (middelste genoemde, mediaan, midden; 1 item = 1/1)', [_item('G7-427-oud', "5 dino's hebben 15, 11, 12, 9, 13 eieren. Hoeveel eieren hebben ze gemiddeld?", '12', doel='G7-GET-04', nro=5)], 'FAIL'),
    ('oud G6 010 (alle vijf routes)', [_item('G6-010-oud', "4 dino's verzamelden eieren. Ze hadden er 5, 6, 6 en 7. Hoeveel eieren is dat gemiddeld per dino?", '6', doel='G6-GET-E08', nro=2)], 'FAIL'),
    ('oud G8 002 (twee waarden, afleiders buiten het bereik: Z-#860 WARN; regel 2 en de routes pas vanaf drie waarden, Z-#841)', [_item('G8-002-oud', 'In een zwembad zwemmen op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er dat weekend gemiddeld per dag?', '300 mensen', ['40 mensen', '300 mensen', '600 mensen'], 'G8-GET-V02', 2)], 'WARN'),
    ('nieuw G8 002 (V-#850)', [_item('G8-002-nieuw', 'In een zwembad zwommen op vrijdag 210 mensen, op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er in die drie dagen gemiddeld per dag?', '270 mensen', ['270 mensen', '265 mensen', '810 mensen'], 'G8-GET-V02', 2)], 'geen'),
    ('G8 002 met 300 in het bereik, afleiders buiten (regel 2)', [_item('G8-002-mut', 'In een zwembad zwommen op vrijdag 300 mensen, op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er in die drie dagen gemiddeld per dag?', '300 mensen', ['40 mensen', '300 mensen', '900 mensen'], 'G8-GET-V02', 2)], 'FAIL'),
    ('nieuw G7 427 (V-#853)', [_item('G7-427-nieuw', "5 dino's hebben 15, 11, 11, 10, 13 eieren. Hoeveel eieren hebben ze gemiddeld?", '12', doel='G7-GET-04', nro=5)], 'geen'),
]
def mutanten():
    uit = []
    for naam, items, verwacht in MUTANTEN:
        Fl, W, _ = analyse(items); kreeg = 'FAIL' if Fl else ('WARN' if W else 'geen')
        uit.append((naam, verwacht, kreeg))
    return uit
if __name__ == '__main__' and '--mutanten' in sys.argv:
    M = mutanten()
    for naam, v, k in M: print(('ok  ' if v == k else 'MIS ') + f'{naam}: verwacht {v}, kreeg {k}')
    print(f"mutanten GEMIDDELDE: {sum(v == k for _, v, k in M)}/{len(M)}"); sys.exit(0 if all(v == k for _, v, k in M) else 1)
