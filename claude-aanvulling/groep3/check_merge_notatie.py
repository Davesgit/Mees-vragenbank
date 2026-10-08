#!/usr/bin/env python3
"""Notatiecheck op de G3 Claude-merge (Didactiek 2026-10-01). Leest alleen, wijzigt niets.
Bron: data/per_doel/G3-*.json (opgave, opgaveStappen, opties/optiesTekst, antwoord, Claude-fout-hints).
Regels (zelfde lijn als check_dubbelepunt G7/G8 en check_hints G3):
  DP   ':' + getal of □ (G3 leest ':' als deelteken) -> zin splitsen of 'hoeveel … is'.      FAIL
  MIN  '-' (koppelteken) tussen getallen/□/#; moet '−' (U+2212) zijn.                       FAIL
  KEER '×' of 'x' tussen getallen; in G3 alleen bij echt vermenigvuldigen (geen gemapt somtype). FAIL
  KLOK kloktijd u:mm (alleen in antwoord/intern toegestaan; in tekst voor het kind 'uur'/'half'). INFO
Gebruik: python3 check_merge_notatie.py [--detail] [doelbestand.json ...]"""
import json,glob,os,re,sys,collections
BASE=os.path.dirname(os.path.abspath(__file__))
KLOK=re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
R=[('DP',  "':' + getal",            re.compile(r':\s*[\d□#]'),'FAIL'),
   ('EVEN',"'even veel' (schrijf 'evenveel')", re.compile(r'\b[Ee]ven veel\b'),'FAIL'),      # Didactiek 21:25 (G6 #192)
   ('MIN', "'-' tussen getallen",    re.compile(r'[\d□#]\s*[-–]\s*[\d□#]'),'FAIL'),
   ('KEER',"'×' tussen getallen",    re.compile(r'[\d□#]\s*[×x*]\s*[\d□#]'),'FAIL'),
   ('KLOK',"kloktijd u:mm",          KLOK,'INFO')]
def velden(it):
    yield 'opgave',it.get('opgave') or ''
    for s in it.get('opgaveStappen') or []: yield 'opgave',s if isinstance(s,str) else json.dumps(s,ensure_ascii=False)
    for o in it.get('opties') or []: yield 'opties',o.get('tekst','') if isinstance(o,dict) else str(o)
    if not it.get('opties') and it.get('optiesTekst'): yield 'opties',it['optiesTekst']
    yield 'antwoord',str(it.get('antwoord') or '')
    for f in it.get('foutHints') or []: yield 'fout-hint',(f.get('uitleg') or '')
def check(files,detail=False):
    tel=collections.defaultdict(set); per_st=collections.defaultdict(set); voorb={}
    for p in files:
        D=json.load(open(p)); doel=D['doelId']
        for it in D['items']:
            st=(it.get('merge') or {}).get('somtype','?')
            for veld,txt in velden(it):
                for code,_,rx,_ in R:
                    t=txt
                    if code=='DP': t=KLOK.sub('',t)                     # kloktijd telt bij KLOK
                    if m:=rx.search(t):
                        tel[(doel,code,veld)].add(it['id']); per_st[(doel,st,code)].add(it['id'])
                        voorb.setdefault((doel,st,code),f"{it['nr']} [{veld}] …{t[max(0,m.start()-25):m.end()+12]}…")
    alle={}
    for (d,c,v),ids in tel.items(): alle.setdefault((d,c),set()).update(ids)
    return ({k:len(v) for k,v in tel.items()},{k:len(v) for k,v in per_st.items()},voorb,{k:len(v) for k,v in alle.items()})
if __name__=='__main__':
    a=[x for x in sys.argv[1:] if not x.startswith('--')]; detail='--detail' in sys.argv
    files=a or sorted(glob.glob(f'{BASE}/data/per_doel/G3-*.json'))
    tel,per_st,voorb,alle=check(files)
    codes=[c for c,*_ in R]; ernst={c:e for c,_,_,e in R}
    print('Items met hit per doelbestand: totaal (per veld: opg=opgave, opt=opties, ant=antwoord, fou=Claude-fout-hint)')
    print(f"{'doel':14} "+' '.join(f'{c:>22}' for c in codes))
    doelen=sorted({d for d,_,_ in tel}); tot=collections.Counter()
    for d in doelen:
        cel=[]
        for c in codes:
            parts={v:tel.get((d,c,v),0) for v in ('opgave','opties','antwoord','fout-hint') if tel.get((d,c,v))}
            n=alle.get((d,c),0); tot[c]+=n; cel.append((f"{n} ("+'/'.join(f"{v[:3]}{k}" for v,k in parts.items())+')') if n else '-')
        print(f"{d:14} "+' '.join(f'{x:>22}' for x in cel))
    print('Totaal:',' · '.join(f"{c} {tot[c]} ({ernst[c]})" for c in codes))
    print('\nPer somtype (items met hit · voorbeeld):')
    for (d,st,c),n in sorted(per_st.items()):
        print(f"  {ernst[c]:4} {c:4} {d} '{st[:48]}': {n} · {voorb[(d,st,c)]}")
    fail=any(tot[c] for c in codes if ernst[c]=='FAIL')
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
    fail = (_MC.rapport(3, [_it for _p in files for _it in json.load(open(_p))['items']]) > 0) or fail
    sys.path.insert(0, '/workspace/claude-merge/tools'); import gemiddelde_check as _GM      # Z-#855 (Didactiek 8 okt 16:15): gemiddelde-vragen; in G3 alleen gemeld (WARN), G3 is goedgekeurd
    _GM.rapport([_it for _p in files for _it in json.load(open(_p))['items']], os.path.dirname(os.path.abspath(__file__)), ernst='WARN (hier niet blokkerend)')
    print('\nG3 merge-notatie:', 'FAIL (zie merge-fixlijst.md; opgaven niet aangepast)' if fail else 'ALLES OK')
    sys.exit(1 if fail else 0)
