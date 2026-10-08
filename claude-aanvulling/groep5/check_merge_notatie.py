#!/usr/bin/env python3
"""Notatiecheck op de G5 Claude-merge (1 okt 2026). Leest alleen, wijzigt niets. G5-versie (Overzicht, 15:15) van g4/check_merge_notatie.py
(Oefeningen, stand 14:33: DP-uitzondering, XSTER, DEELT, MACHT, SOM). G5-regels: ×/: alleen in de ×/:-doelen (KEER en DEEL = FAIL daarbuiten),
komma alleen bij geld ('€3,50') en liter ('0,5 L'), breuken in woorden (BREUK), liter = L (LITER), geen 'Één'.
Bron: data/per_doel/G5-*.json (opgave, opgaveStappen, opties/optiesTekst, antwoord, Claude-fout-hints).
Regels:
  DP    ':' + getal of □ (geen kloktijd, geen deelsom 'a : b', geen 'woord: getal' zoals 'Reken uit: 4 × 7') -> zin splitsen. FAIL
  MIN   '-' (koppelteken) tussen getallen/□/#; moet '−' (U+2212) zijn.                                FAIL
  KEER  '×' of 'x' tussen getallen buiten de tafel-/keerdoelen (M06, E06, E07, E08, E09, VERH-E03/E04). FAIL
  XSTER 'x' of '*' als keerteken, ook in de keerdoelen (moet '×').                                    FAIL
  DEELT '÷' (G4: 'a : b').                                                                             FAIL
  MACHT cijfer + ², ³ of ^.                                                                            FAIL
  SOM   een som met '=' die niet klopt (elke '=' in een kettingsom; □ telt niet mee).                  FAIL
  (DP-uitzondering 'woord: getal', XSTER, DEELT, MACHT en SOM: Oefeningen 1 okt 14:30, G4-notatie uit de opdracht.)
  PUNT  4-cijferig getal met punt (1.000) of ≥10.000 zonder punt.                                       FAIL
  GELD  '€N,-' of '€N,00' (G4: '€N' en '€N,CC').                                                      FAIL
  EEN   'Één' (moet 'Eén').                                                                            FAIL
  KOMMA geldbedrag met komma '€N,CC' (besluit Dave 1 okt: geen komma in G4; '45 cent', '€2').          FAIL
  DEEL  deelsom 'a : b' in kindtekst (Didactiek: deelteken in G4 = twijfel).                           INFO
  KLOK  kloktijd u:mm (G4-MEET-E06 kent digitaal :15/:30/:45).                                           INFO
  ENG   'trainer'/'shirt' ergens in een item (ook extraVelden; niet licentie/merge.*Origineel), ook terug_G4/aanvulling_uit_g6. FAIL
Gebruik: python3 check_merge_notatie.py [--detail] [doelbestand.json ...]"""
import json, glob, os, re, sys, collections
BASE = os.path.dirname(os.path.abspath(__file__))
KEER_DOELEN = {'G5-GET-V03', 'G5-GET-M05', 'G5-GET-M06', 'G5-GET-E07', 'G5-GET-E08', 'G5-GET-E09', 'G5-MEET-E08', 'G5-VERH-E02'}
KLOK = re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
DEEL = re.compile(r'[\d□#]\s:\s[\d□#]')
R = [('DP',   "':' + getal",             re.compile(r':\s*[\d□#€]'), 'FAIL'),
     ('EVEN',  "'even veel' (schrijf 'evenveel')", re.compile(r'\b[Ee]ven veel\b'), 'FAIL'),      # Didactiek 21:25 (G6 #192)
     ('MIN',  "'-' tussen getallen",     re.compile(r'[\d□#]\s*[-–]\s*[\d□#]'), 'FAIL'),
     ('KEER', "'×' buiten keerdoel",     re.compile(r'[\d□#]\s*[×x*]\s*[\d□#]'), 'FAIL'),
     ('PUNT', 'duizendtal-notatie',      re.compile(r'(?<![\d.,])\d\.\d{3}(?![\d.,])|(?<![\d.,:])\d{5,}(?![\d.,:])'), 'FAIL'),
     ('GELD', "'€N,-' / '€N,00'",        re.compile(r'€\s?\d+,(?:-|00\b)'), 'FAIL'),
     ('EEN',  "'Één'",                   re.compile(r'Één'), 'FAIL'),
     ('KOMMA', "komma buiten geld/L",    re.compile(r'(?<![\d,€])(?<!€\s)\d+,\d+(?!\d)(?! L\b)'), 'FAIL'),
     ('BREUK', "breuk n/m",              re.compile(r'(?<![\d/:])\d+/\d+(?![\d/])'), 'FAIL'),
     ('LITER', "'l' (moet 'L')",         re.compile(r'\d l\b'), 'FAIL'),
     ('XSTER',"'x'/'*' als keerteken",   re.compile(r'[\d□#]\s*[x*]\s*[\d□#]'), 'FAIL'),
     ('DEELT',"'÷'",                     re.compile(r'÷'), 'FAIL'),
     ('MACHT','macht',                   re.compile(r'\d\s?[²³]|\d\s?\^'), 'FAIL'),
     ('SOM',  "som klopt niet",          None, 'FAIL'),
     ('DEEL', "deelsom 'a : b' buiten ×/:-doel", DEEL, 'FAIL'),
     ('KLOK', 'kloktijd u:mm',           KLOK, 'INFO')]
WOORD_DP = re.compile(r'(?<=[A-Za-zÀ-ÿ)]): (?=(?:€\s?)?[\d□#])')
NUM = r'\d+(?:,\d+)?'
EXPR = rf'{NUM}(?:\s*[+−×:-]\s*{NUM})*'
KETEN = re.compile(rf'(?<![\d,□])({EXPR})((?:\s*=\s*{EXPR})+)(?![\d,]|\s*[+−×:-]\s*\d)')
def _eval(e):
    e = e.replace('−', '-').replace('×', '*').replace(':', '/').replace(',', '.')
    if not re.fullmatch(r'[\d.\s+\-*/]+', e): return None
    try: return eval(e)
    except Exception: return None
def som_fout(txt):
    t = KLOK.sub(' ', txt)
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
                for code, _, rx, _ in R:
                    t = txt
                    if code == 'DP': t = WOORD_DP.sub(' ', DEEL.sub(' ', KLOK.sub('', t)))
                    if code in ('KEER', 'DEEL') and doel in KEER_DOELEN: continue
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
    files = a or sorted(glob.glob(f'{BASE}/data/per_doel/G5-*.json'))
    tel, per_st, voorb, alle = check(files)
    codes = [c for c, *_ in R]; ernst = {c: e for c, _, _, e in R}
    print(f'{len(files)} doelbestanden, {sum(len(json.load(open(p))["items"]) for p in files)} items')
    print(f"{'doel':14} " + ' '.join(f'{c:>6}' for c in codes))
    tot = collections.Counter()
    for d in sorted({d for d, _, _ in tel}):
        cel = []
        for c in codes: n = alle.get((d, c), 0); tot[c] += n; cel.append(str(n) if n else '-')
        print(f"{d:14} " + ' '.join(f'{x:>6}' for x in cel))
    print('Totaal:', ' · '.join(f"{c} {tot[c]} ({ernst[c]})" for c in codes))
    print('\nPer somtype (items met hit · voorbeeld):')
    for (d, st, c), ids in sorted(per_st.items()):
        if detail or ernst[c] == 'FAIL': print(f"  {ernst[c]:4} {c:4} {d} '{st[:48]}': {len(ids)} · {voorb[(d, st, c)]}")
    fail = any(tot[c] for c in codes if ernst[c] == 'FAIL')
    # ENG (fixlijst #21/#49, Didactiek batch 3 #46): 'trainer' en 'shirt' nergens in een item, ook niet in extraVelden (claudeUitleg …),
    # foutHintsTekst/optiesTekst, merge.somtype; niet in de wijzigingslog (licentie) en de bevroren oude sleutels (merge.*Origineel). FAIL
    ENG = re.compile(r'trainer|shirt', re.I); eng = []
    def _walk(v, pad, it, bron):
        if isinstance(v, str):
            if ENG.search(v): eng.append(f"{bron} {it.get('id')} {pad}: «{v[:80]}»")
        elif isinstance(v, list): [_walk(x, pad, it, bron) for x in v]
        elif isinstance(v, dict): [_walk(x, f'{pad}.{k}', it, bron) for k, x in v.items()]
    extra = [f for f in (f'{BASE}/data/terug_G4.json', f'{BASE}/data/aanvulling_uit_g6.json') if os.path.exists(f) and not a]
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
    # VERKLAP (G5 merge-fixlijst #107, Didactiek 18:54): fout-hint noemt het goede antwoord (getal + eenheid) bij meerkeuze = WARN
    import verklapper_check as _VK
    _VK.rapport([_it for _p in files for _it in json.load(open(_p))['items']])
    # GEN (merge-fixlijst #151, Dave 19:14): bij een generator-item geen sleutel onder twee regels van de entry (FAIL)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))
    import check_generator_sleutels as _GS
    _gs = _GS.treffers()
    print(f"\nGEN (generator-items: twee regels op één sleutel, #151): {len(_gs)} (FAIL)")
    for _x in _gs[:20]: print('  FAIL GEN', *_x)
    fail = fail or bool(_gs)
    import machten_check as _MC
    # R121 (G5 merge-fixlijst #121, besluit Dave 20:04): een foute route geeft niet het goede antwoord (FAIL)
    sys.path.insert(0, os.path.join(BASE, 'scripts')); import check_121 as _C121
    _r121 = _C121.run(); print(f"\nR121 (tabel/verdelen: een foute route of regelwaarde geeft het goede antwoord, #121): {len(_r121)} (FAIL)")
    for _x in _r121[:20]: print('  FAIL R121', _x)
    fail = bool(_r121) or fail
    # DOELID (G5 merge-fixlijst #122, Didactiek 20:04): elk item heeft het doelId van zijn bestand (FAIL)
    sys.path.insert(0, '/workspace/claude-merge/tools'); import doelid_check as _DI
    fail = (_DI.rapport(files) > 0) or fail
    import evenveel_check as _EV      # #192 (Didactiek 21:25): 'even veel' ook in ouderzin, hints en kop (FAIL)
    fail = (_EV.rapport([_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    fail = (_MC.rapport(5, [_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
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
    print('\nG5 merge-notatie:', 'FAIL' if fail else 'ALLES OK')
    sys.exit(1 if fail else 0)
