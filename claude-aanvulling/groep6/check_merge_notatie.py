#!/usr/bin/env python3
"""Notatiecheck op de G6 Claude-merge (1 okt 2026). Leest alleen, wijzigt niets. G6-versie (Overzicht, 1 okt) van g5/check_merge_notatie.py
(dat weer de G5-versie is van g4/check_merge_notatie.py van Oefeningen, stand 14:33).
Verschil met G5: '×' en ':' mogen overal (geen KEER/DEEL-beperking), breuken n/m mogen, kommagetallen mogen (maar 3 of meer cijfers
achter de komma = FAIL, dat is G7), en drie nieuwe G6-regels: PROCENT, VERH ('a : b' als verhouding of schaal, besluit Dave: pas in G7)
en KETEN (ketensom '7 × 4 = 28 + 12' moet voluit: '7 × 4 = 28 en 28 + 12 = 40').
Bron: data/per_doel/G6-*.json (opgave, opgaveStappen, opties/optiesTekst, antwoord, fout-hints).
Regels:
  DP     ':' + getal of □ (geen kloktijd, geen deelsom 'a : b', geen 'woord: getal' zoals 'Reken uit: 4 × 7') -> zin splitsen. FAIL
  MIN    '-' (koppelteken) tussen getallen/□/#; moet '−' (U+2212) zijn.                                FAIL
  XSTER  'x' of '*' als keerteken (moet '×').                                                         FAIL
  DEELT  '÷' (deelteken is 'a : b').                                                                  FAIL
  MACHT  cijfer + ², ³ of ^.                                                                          FAIL
  SOM    een som met '=' die niet klopt (elke '=' in een kettingsom; □ telt niet mee).                FAIL
  KETEN  ketensom 'a × b = c + d = e' (doorrekenen na '=' ; voluit schrijven met 'en').               FAIL
  PUNT   4-cijferig getal met punt (1.000, ook vóór een zinseinde) of ≥10.000 zonder punt.            FAIL
  GELD   '€N,-' of '€N,00' ('€N' en '€N,CC').                                                         FAIL
  EEN    'Één' (moet 'Eén').                                                                          FAIL
  KOMMA3 kommagetal met 3 of meer cijfers achter de komma (G7).                                       FAIL
  LITER  'l' na een getal of □ (moet 'L').                                                            FAIL
  PROCENT '%' of 'procent' (G7-VERH).                                                                 FAIL
  VERH   'a : b' bij verhouding/schaal/mengen ('schaal 1 : 100'): pas in G7 (Verhoudingen).           FAIL
  DEEL   deelsom 'a : b' (mag in G6).                                                                  INFO
  KLOK   kloktijd u:mm.                                                                                INFO
Gebruik: python3 check_merge_notatie.py [--detail] [doelbestand.json ...]"""
import json, glob, os, re, sys, collections
BASE = os.path.dirname(os.path.abspath(__file__))
KLOK = re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
DEEL = re.compile(r'[\d□#]\s:\s[\d□#]')
VERH = re.compile(r'(verhouding|schaal|staat tot|mengen|mengsel)[^.?!]*\d\s*:\s*\d|\d\s*:\s*\d[^.?!]*(verhouding|schaal)', re.I)
R = [('DP',    "':' + getal",             re.compile(r':\s*[\d□#€]'), 'FAIL'),
     ('EVEN',  "'even veel' (schrijf 'evenveel')", re.compile(r'\b[Ee]ven veel\b'), 'FAIL'),      # Didactiek 21:25 (G6 #192)
     ('MIN',   "'-' tussen getallen",     re.compile(r'[\d□#]\s*[-–]\s*[\d□#]'), 'FAIL'),
     ('XSTER', "'x'/'*' als keerteken",   re.compile(r'[\d□#]\s*[x*]\s*[\d□#]'), 'FAIL'),
     ('DEELT', "'÷'",                     re.compile(r'÷'), 'FAIL'),
     ('MACHT', 'macht',                   re.compile(r'\d\s?[²³]|\d\s?\^'), 'FAIL'),
     ('SOM',   "som klopt niet",          None, 'FAIL'),
     ('KETEN', "ketensom niet voluit",    re.compile(r'[\d□]\s*[+−×:]\s*[\d□]+\s*=\s*\d+\s*[+−×:]\s*[\d□]+\s*='), 'FAIL'),
     ('PUNT',  'duizendtal-notatie',      re.compile(r'(?<![\d.,])\d\.\d{3}(?!\d|[.,]\d)|(?<![\d.,:])\d{5,}(?![\d.,:])'), 'FAIL'),
     ('GELD',  "'€N,-' / '€N,00'",        re.compile(r'€\s?\d+,(?:-|00\b)'), 'FAIL'),
     ('EEN',   "'Één'",                   re.compile(r'Één'), 'FAIL'),
     ('KOMMA3', "3+ cijfers achter komma", re.compile(r'(?<![\d,])\d+,\d{3,}(?!\d)'), 'FAIL'),
     ('LITER', "'l' (moet 'L')",          re.compile(r'[\d□] l\b'), 'FAIL'),
     ('PROCENT', "procent",               re.compile(r'%|\bprocent\b', re.I), 'FAIL'),
     ('VERH',  "'a : b' als verhouding",  VERH, 'FAIL'),
     ('DEEL',  "deelsom 'a : b'",         DEEL, 'INFO'),
     ('KLOK',  'kloktijd u:mm',           KLOK, 'INFO')]
WOORD_DP = re.compile(r'(?<=[A-Za-zÀ-ÿ)?]): (?=(?:€\s?)?[\d□#])')
NUM = r'\d+(?:,\d+)?'
EXPR = rf'{NUM}(?:\s*[+−×:-]\s*{NUM})*'
KETEN = re.compile(rf'(?<![\d,□])({EXPR})((?:\s*=\s*{EXPR})+)(?![\d,]|\s*[+−×:-]\s*[\d?□])')     # G6: ook '?' als plaatshouder ('6158 = 6000 + 100 + ? + 8')
def _eval(e):
    e = e.replace('−', '-').replace('×', '*').replace(':', '/').replace(',', '.')
    if not re.fullmatch(r'[\d.\s+\-*/]+', e): return None
    try: return eval(e)
    except Exception: return None
def som_fout(txt):
    t = KLOK.sub(' ', re.sub(r'(?<=\d)\.(?=\d{3}\b)', '', txt))
    for m in KETEN.finditer(t):
        if re.search(r'[□#\d]\s*[+−×:-]\s*$', t[:m.start()]): continue
        delen = [m.group(1)] + re.split(r'\s*=\s*', m.group(2).strip())[1:]
        w = [_eval(d) for d in delen]
        if None in w: continue
        if any(abs(x - w[0]) > 1e-9 for x in w): return m.group(0).strip()
    return None
def velden(it):
    yield 'opgave', it.get('opgave') or ''
    for s in it.get('opgaveStappen') or []: yield 'opgave', s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    for o in it.get('opties') or []: yield 'opties', o.get('tekst', '') if isinstance(o, dict) else str(o)
    yield 'antwoord', str(it.get('antwoord') or '')
    for f in it.get('foutHints') or []: yield 'fout-hint', (f.get('uitleg') or '')
def check(files):
    tel = collections.defaultdict(set); per_st = collections.defaultdict(set); voorb = {}
    for p in files:
        D = json.load(open(p)); doel = D['doelId']
        for it in D['items']:
            st = (it.get('merge') or {}).get('somtype', '?')
            for veld, txt in velden(it):
                if veld == 'antwoord' and re.fullmatch(r'wel:[^|]*\|niet:.*', txt): continue    # sleepvak-sleutel, geen kindtekst
                for code, _, rx, _ in R:
                    t = txt
                    if code == 'DP': t = WOORD_DP.sub(' ', DEEL.sub(' ', KLOK.sub('', t)))
                    if code == 'SOM':
                        fout = som_fout(t)
                        if fout: tel[(doel, code, veld)].add(it['id']); per_st[(doel, st, code)].add(it['id']); voorb.setdefault((doel, st, code), f"{it['nr']} [{veld}] …{fout}…")
                        continue
                    if m := rx.search(t):
                        tel[(doel, code, veld)].add(it['id']); per_st[(doel, st, code)].add(it['id'])
                        voorb.setdefault((doel, st, code), f"{it['nr']} [{veld}] …{t[max(0, m.start() - 25):m.end() + 12]}…")
    alle = {}
    for (d, c, v), ids in tel.items(): alle.setdefault((d, c), set()).update(ids)
    return tel, per_st, voorb, {k: len(v) for k, v in alle.items()}
if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]; detail = '--detail' in sys.argv
    files = a or sorted(glob.glob(f'{BASE}/data/per_doel/G6-*.json'))
    tel, per_st, voorb, alle = check(files)
    codes = [c for c, *_ in R]; ernst = {c: e for c, _, _, e in R}
    print(f'{len(files)} doelbestanden, {sum(len(json.load(open(p))["items"]) for p in files)} items')
    print(f"{'doel':14} " + ' '.join(f'{c:>7}' for c in codes))
    tot = collections.Counter()
    for d in sorted({d for d, _, _ in tel}):
        cel = []
        for c in codes: n = alle.get((d, c), 0); tot[c] += n; cel.append(str(n) if n else '-')
        print(f"{d:14} " + ' '.join(f'{x:>7}' for x in cel))
    print('Totaal:', ' · '.join(f"{c} {tot[c]} ({ernst[c]})" for c in codes))
    print('\nPer somtype (items met hit · voorbeeld):')
    for (d, st, c), ids in sorted(per_st.items()):
        if detail or ernst[c] == 'FAIL': print(f"  {ernst[c]:4} {c:5} {d} '{st[:48]}': {len(ids)} · {voorb[(d, st, c)]}")
    fail = any(tot[c] for c in codes if ernst[c] == 'FAIL')
    # ENG (fixlijst #21/#49, Didactiek batch 3 #46): 'trainer' en 'shirt' nergens in een item, ook niet in extraVelden (claudeUitleg …),
    # foutHintsTekst/optiesTekst, merge.somtype; niet in de wijzigingslog (licentie) en de bevroren oude sleutels (merge.*Origineel). FAIL
    ENG = re.compile(r'trainer|shirt', re.I); eng = []
    def _walk(v, pad, it, bron):
        if isinstance(v, str):
            if ENG.search(v): eng.append(f"{bron} {it.get('id')} {pad}: «{v[:80]}»")
        elif isinstance(v, list): [_walk(x, pad, it, bron) for x in v]
        elif isinstance(v, dict): [_walk(x, f'{pad}.{k}', it, bron) for k, x in v.items()]
    extra = [] if a else sorted(glob.glob(f'{BASE}/data/terug_*.json') + glob.glob(f'{BASE}/data/aanvulling_*.json'))
    for p in files + extra:
        for it in json.load(open(p))['items']:
            for k, v in it.items():
                if k in ('licentie', 'bron'): continue   # herkomst-metadata (claudeDoelTitel e.d.)
                if k == 'merge': _walk(v.get('somtype'), 'merge.somtype', it, os.path.basename(p)); continue
                _walk(v, k, it, os.path.basename(p))
    print(f"\nENG ('trainer'/'shirt' in een item, ook extraVelden): {len(eng)} (FAIL)")
    for x in eng[:20]: print('  FAIL ENG', x)
    fail = fail or bool(eng)
    # OPP (G5 fixlijst #59, Didactiek batch 4): omtrek-item van een rechthoek waar oppervlakte = omtrek (6 × 3, 4 × 4): FAIL
    _opp = []
    for _p in files:
        for _it in json.load(open(_p))['items']:
            _o = (_it.get('opgave') or '').replace('\n', ' ')
            _m = re.search(r'(\d+) (?:cm|m|mm|dm|km) lang en (\d+) (?:cm|m|mm|dm|km) breed', _o) or re.search(r'(?:rechthoek|veld|tuin|[\wà-ÿ]+) van (\d+) bij (\d+) (?:cm|m|mm|dm|km)?', _o)
            if _m and 'omtrek' in _o.lower() + ' ' + ('hek' if ' hek' in _o else ''):
                _l, _b = int(_m.group(1)), int(_m.group(2))
                if _l * _b == 2 * (_l + _b): _opp.append(f"{_it.get('id')}: {_l} × {_b} (oppervlakte = omtrek = {_l * _b})")
            elif _m and ' hek' in _o:
                _l, _b = int(_m.group(1)), int(_m.group(2))
                if _l * _b == 2 * (_l + _b): _opp.append(f"{_it.get('id')}: {_l} × {_b} (oppervlakte = omtrek = {_l * _b})")
    print(f"\nOPP (rechthoek met oppervlakte = omtrek bij een omtrekvraag, #59): {len(_opp)} (FAIL)")
    for _x in _opp[:20]: print('  FAIL OPP', _x)
    fail = fail or bool(_opp)
    # REF (G5 fixlijst #63): referentiematen uit /workspace/claude-merge/referentiematen.json: checkPatronen = FAIL, checkPatronenZacht = WARN
    sys.path.insert(0, '/workspace/claude-merge/tools')
    import referentiematen_check as _RC
    fail = (_RC.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail      # checkPatronen = FAIL, zacht = WARN
    # MAAT (notatie_machten.md, Didactiek 18:00; aangezet 18:05): ²/³ per groep, mengvorm 'vierkante cm', m2/cm3, 'a' voor are, INTRO per somtype
    # VORM (G5 merge-fixlijst #105, Didactiek 18:54): antwoordOokGoed en geldInvoer moeten bij het antwoord passen (FAIL)
    import antwoordvormen_check as _AV
    fail = (_AV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    # G6-fixlijst #1–#6 (Dave 19:58): scripts/check_fixlijst_g6.py (FAIL)
    sys.path.insert(0, os.path.join(BASE, 'scripts')); import check_fixlijst_g6 as _FX6
    _f6 = _FX6.run(); print(f"\nFIX6 (G6-fixlijst #1–#6: buurgetal, één cijfer, kommasleutels, getal2 ± 1): {len(_f6)} (FAIL)")
    for _x in _f6[:20]: print('  FAIL FIX6', _x)
    fail = bool(_f6) or fail
    import machten_check as _MC
    # BREUKVORM (G6 merge-fixlijst #170, Dave 21:24): even grote breuk goed, behalve als de opgave een vorm vraagt (FAIL)
    sys.path.insert(0, '/workspace/claude-merge/tools'); import breukvorm as _BV
    fail = (_BV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    # DOELID (G5 merge-fixlijst #122, Didactiek 20:04): elk item heeft het doelId van zijn bestand (FAIL)
    sys.path.insert(0, '/workspace/claude-merge/tools'); import doelid_check as _DI
    fail = (_DI.rapport(files) > 0) or fail
    import evenveel_check as _EV      # #192 (Didactiek 21:25): 'even veel' ook in ouderzin, hints en kop (FAIL)
    fail = (_EV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    fail = (_MC.rapport(6, [_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    # OPT230 (G6 merge-fixlijst #230, Oefeningen 22:36): een breukwoord-optie met een hoofdletter ('Een kwart') past niet bij de regels in kleine letters
    # ('regel niet te lezen'); een kommagetal met een punt ('37.2') in een optie, het antwoord of een fout-sleutel (FAIL)
    _BW = re.compile(r'^(Een|De|Het|Twee|Drie|Vier|Vijf|Zes) (kwart|derde|helft|vierde|vijfde|zesde|achtste|tiende|twaalfde|zestiende|hele)\b')
    _PT = re.compile(r'^€?\d+\.\d{1,2}$')
    _o230 = []
    for _p in files:
        for _it in json.load(open(_p))['items']:
            for _o in _it.get('opties') or []:
                if _BW.match(_o['tekst']): _o230.append(f"{_it.get('id')}: optie '{_o['tekst']}' met hoofdletter")
            for _v in [str(_it.get('antwoord'))] + [str(_o['tekst']) for _o in _it.get('opties') or []] + [f['fout'] for f in _it.get('foutHints') or []] + [f['fout'] for f in (_it.get('extraVelden') or {}).get('claudeFoutHints') or []]:
                if _PT.match(_v.strip()): _o230.append(f"{_it.get('id')}: '{_v}' met een punt in plaats van een komma")
    print(f"\nOPT230 (#230: breukwoord-optie met hoofdletter, kommagetal met punt): {len(_o230)} (FAIL)")
    for _x in _o230[:20]: print('  FAIL OPT230', _x)
    fail = fail or bool(_o230)
    print('\nG6 merge-notatie:', 'FAIL' if fail else 'ALLES OK')
    sys.exit(1 if fail else 0)
