#!/usr/bin/env python3
"""[G8-kopie 1 okt 18:15 van g7/check_merge_notatie.py: data/per_doel/G8-*.json; MAAT met de G8-regels (machten_check groep 8: ² en ³ ok, 'a' voor are FAIL); REF; ENG ook 'kans'/'mediaan' (VO-stof, buitenBasisschool). Verder gelijk aan G7.] Notatiecheck op de G7 Claude-merge (1 okt 2026). Leest alleen, wijzigt niets. G7-versie (Overzicht, 1 okt) van g6/check_merge_notatie.py
(dat de G6-versie is van g5/ en g4/check_merge_notatie.py van Oefeningen, stand 14:33).
Verschil met G6: procent en 'a : b' als verhouding of schaal mogen (G7, besluit Dave), kommagetallen tot 3 decimalen mogen
(4 of meer = FAIL, zoals de canonieke G7-bank), nieuw FAIL: NEG ('-' als minteken vóór een getal, moet '−': '−4', '−2 graden').
Bron: data/per_doel/G7-*.json (opgave, opgaveStappen, opties/optiesTekst, antwoord, fout-hints).
Regels:
  DP     ':' + getal of □ (geen kloktijd, geen 'a : b' (deling, verhouding, schaal), geen 'woord: getal' zoals 'Reken uit: 4 × 7'). FAIL
  MIN    '-' (koppelteken) tussen getallen/□/#; moet '−' (U+2212) zijn.                                FAIL
  NEG    '-' als minteken vóór een getal ('-4', '-2 graden'); moet '−4'.                               FAIL
  XSTER  'x' of '*' als keerteken (moet '×').                                                         FAIL
  DEELT  '÷' (deelteken is 'a : b').                                                                  FAIL
  MACHT  cijfer + ², ³ of ^, ook met spatie ('10 ³'), gelijk aan G4–G6 (cm³ en m³ mogen: eenheid).      FAIL
  SOM    een som met '=' die niet klopt (elke '=' in een kettingsom; □ telt niet mee).                FAIL
  KETEN  ketensom 'a × b = c + d = e' (doorrekenen na '=' ; voluit schrijven met 'en').               FAIL
  PUNT   4-cijferig getal met punt (1.000, ook vóór een zinseinde) of ≥10.000 zonder punt.            FAIL
  GELD   '€N,-' of '€N,00' ('€N' en '€N,CC').                                                         FAIL
  EEN    'Één' (moet 'Eén').                                                                          FAIL
  KOMMA4 kommagetal met 4 of meer cijfers achter de komma (G8: hoogstens 3, tot duizendsten).        FAIL
  LITER  'l' na een getal of □ (moet 'L').                                                            FAIL
  DEEL   'a : b' (deling, verhouding of schaal; mag in G7).                                           INFO
  KLOK   kloktijd u:mm.                                                                               INFO
Gebruik: python3 check_merge_notatie.py [--detail] [doelbestand.json ...]"""
import json, glob, os, re, sys, collections
BASE = os.path.dirname(os.path.abspath(__file__))
KLOK = re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
DEEL = re.compile(r'[\d□#]\s:\s[\d□#−]')
VERH = re.compile(r'(verhouding|schaal|staat tot|mengen|mengsel)[^.?!]*\d\s*:\s*\d|\d\s*:\s*\d[^.?!]*(verhouding|schaal)', re.I)
R = [('DP',    "':' + getal",             re.compile(r':\s*[\d□#€]'), 'FAIL'),
     ('EVEN',  "'even veel' (schrijf 'evenveel')", re.compile(r'\b[Ee]ven veel\b'), 'FAIL'),      # Didactiek 21:25 (G6 #192)
     ('MIN',   "'-' tussen getallen",     re.compile(r'[\d□#]\s*[-–]\s*[\d□#]'), 'FAIL'),
     ('NEG',   "'-' als minteken",        re.compile(r'(?<![\w\d.,)\]])-\d'), 'FAIL'),
     ('XSTER', "'x'/'*' als keerteken",   re.compile(r'[\d□#]\s*[x*]\s*[\d□#]'), 'FAIL'),
     ('DEELT', "'÷'",                     re.compile(r'÷'), 'FAIL'),
     ('MACHT', 'macht',                   re.compile(r'\d\s?[²³]|\d\s?\^'), 'FAIL'),
     ('SOM',   "som klopt niet",          None, 'FAIL'),
     ('KETEN', "ketensom niet voluit",    re.compile(r'[\d□]\s*[+−×:]\s*[\d□]+\s*=\s*\d+\s*[+−×:]\s*[\d□]+\s*='), 'FAIL'),
     ('PUNT',  'duizendtal-notatie',      re.compile(r'(?<![\d.,])\d\.\d{3}(?!\d|[.,]\d)|(?<![\d.,:])\d{5,}(?![\d.,:])'), 'FAIL'),
     ('GELD',  "'€N,-' / '€N,00'",        re.compile(r'€\s?\d+,(?:-|00\b)'), 'FAIL'),
     ('EEN',   "'Één'",                   re.compile(r'Één'), 'FAIL'),
     ('KOMMA4', "4+ cijfers achter komma", re.compile(r'(?<![\d,])\d+,\d{4,}(?!\d)'), 'FAIL'),
     ('LITER', "'l' (moet 'L')",          re.compile(r'[\d□] l\b'), 'FAIL'),
     ('DEEL',  "'a : b'",                 DEEL, 'INFO'),
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
    files = a or sorted(glob.glob(f'{BASE}/data/per_doel/G8-*.json'))
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
    ENG = re.compile(r'trainer|shirt|\bkans|\bmediaan', re.I); eng = []   # G7: ook 'kans' (Dave 16:59 punt 3) en 'mediaan' (Didactiek: 'het middelste getal')
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
    print(f"\nENG ('trainer'/'shirt'/'kans'/'mediaan' in een item, ook extraVelden): {len(eng)} (FAIL)")
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
    import machten_check as _MC
    # DOELID (G5 merge-fixlijst #122, Didactiek 20:04): elk item heeft het doelId van zijn bestand (FAIL)
    sys.path.insert(0, '/workspace/claude-merge/tools'); import doelid_check as _DI
    fail = (_DI.rapport(files) > 0) or fail
    import evenveel_check as _EV      # #192 (Didactiek 21:25): 'even veel' ook in ouderzin, hints en kop (FAIL)
    fail = (_EV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    fail = (_MC.rapport(8, [_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import geldig_check as _GA      # #360 (G5 gate ronde 9): antwoord ∈ geldigeAntwoorden (FAIL, G5–G8)
    fail = (_GA.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import bijna390_check as _B390      # #390 (G6 gate ronde 9 deel B): getal uit de vraag nooit ±1/'Bijna!' (FAIL, G5–G8)
    fail = (_B390.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import antwoord_in_vraag_check as _AIV      # V-#560 (recheck G7 batch 1, Didactiek 8 okt): procent/breuk, goed antwoord = getal uit de vraag (FAIL, G5–G8)
    fail = (_AIV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import hoofdletter_check as _HL      # V-#608 (review G7 batch 3, Didactiek 8 okt): een vraagzin begint met een hoofdletter (FAIL, G5–G8)
    fail = (_HL.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import spatie_duizend_check as _SD      # V-#705 (review G7 batch 6, Didactiek 8 okt): spatie als duizendtalscheiding (FAIL, G4–G8)
    fail = (_SD.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    fail = (_SD.rapport_bestanden(os.path.dirname(os.path.abspath(__file__))) > 0) or fail      # Oef-#481: ook hintteksten (batch*.json, somtypen)
    # BREUKVORM (G6 merge-fixlijst #170, Dave 21:24; V-#760, Didactiek G8 batch 1, 8 okt): even grote breuk goed, behalve als de opgave een vorm vraagt (FAIL)
    import breukvorm as _BV
    fail = (_BV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    # JUISTE-OPTIE (Oef-#467, 8 okt): antwoordDetail.juisteOptie(Tekst) past bij de opties (FAIL, alleen G8: in G5/G6 staan nog oude mismatches)
    import kloktijd_check as _KT      # Z-#782 (Didactiek G8 batch 2, 8 okt): kloktijd met ':' in een kindtekst (FAIL; typ-invoer 'uu:mm' WARN)
    fail = (_KT.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import gemiddelde_check as _GM      # V-#820/Z-#823/Z-#841/Z-#855 (Didactiek 8 okt): gemiddelde-vragen, vijf foute routes (FAIL ≥ 1/3 of eigen sleutel; anders WARN)
    fail = (len(_GM.rapport([_it for _p in files for _it in json.load(open(_p))['items']], os.path.dirname(os.path.abspath(__file__)))[0]) > 0) or fail
    fail = (_GM.mutanten() and any(_v != _k for _n, _v, _k in _GM.mutanten())) or fail      # Z-#855: mutanten (oude 427/010/002) moeten kloppen
    import e05_routes as _ER      # V-#870/Z-#871/V-#871 (Didactiek batch 4, 16:35): E05-rekenmachineverhalen: geen foute route op het goede antwoord, rest ≥ 3, geen ',5', redelijke maten (FAIL)
    fail = (_ER.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    fail = any(bool(_ER.fouten_item({'id': _n, 'opgave': _o, 'antwoord': _a})) != _v for _n, _o, _a, _v in _ER.MUTANTEN) or fail      # mutanten 9/9
    import juiste_optie_check as _JO
    fail = (_JO.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    import optie_positie_check as _OP      # Oef-#459 (8 okt): goede antwoord >60% op één plek in een somtype met ≥4 items (WARN)
    _OP.rapport([_it for _p in files for _it in json.load(open(_p))['items']])
    print('\nG8 merge-notatie:', 'FAIL' if fail else 'ALLES OK')
    sys.exit(1 if fail else 0)
