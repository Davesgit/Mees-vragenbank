#!/usr/bin/env python3
"""Gedeelde haak voor de merge-checkers G3–G8: notatie van oppervlakte- en inhoudsmaten (besluit Didactiek, notatie_machten.md, 1 okt 18:00;
aangezet door Overzicht 18:00). Geldt voor de kindvelden (opgave, opgaveStappen, antwoord, opties, Hint 1 'hint', Hint 2 'sterkereHint',
algemeneFoutHint, fout-hints: sleutel + uitleg) en de ouderzin. Niet voor accept-lijsten en niet voor de bevroren Claude-velden (extraVelden).
Codes (§5 van notatie_machten.md):
  MACHT    cijfer + ²/³/⁴ of ^ (macht van een getal, VO-stof)                         FAIL in elke groep (zit ook al in de R-lijst van de checker)
  OPP2     eenheid + ²   G3–G5 FAIL · G6: cm², dm², m² ok, km²/hm²/dam²/mm² WARN (G7-stof) · G7–G8 ok
  INH3     eenheid + ³   G3–G6 FAIL · G7–G8 ok
  ASCII    'm2', 'cm3', 'm^2' (eenheid + 2/3 zonder superscript)                        FAIL in elke groep
  MENG     mengvorm 'vierkante cm', 'kubieke cm' (woord + afkorting)                    FAIL in elke groep
  WOORD    G3–G5: 'vierkante …meter', 'kubieke', 'kuub', 'hectare' WARN (buiten de leerlijn) · G6: 'kubieke'/'kuub'/'hectare' WARN · G7–G8 ok
  INTRO    G6 (cm², dm², m²) en G7 (cm³, dm³, m³, km², ha): een somtype met het symbool waar het woord in geen opgave, Hint 1 of Hint 2
           staat → WARN (per somtype)
  HA       G6: '3 ha' zonder 'hectare' in hetzelfde somtype → WARN (G7: via INTRO)
  ARE-AFK  'a' als afkorting van are ('4 a')                                            G6–G8 FAIL (schrijf 'are')
Gebruik in een checker:  import machten_check as MC; fail = MC.rapport(groep, items) > 0     (rapport print en geeft het aantal FAIL)
Los: python3 tools/machten_check.py <groep> <per_doel/*.json …>"""
import re, sys, json, collections

EENH = r'(?<![A-Za-zÀ-ÿ])(mm|cm|dm|dam|hm|km|m)'
P_OPP2 = re.compile(EENH + r'²')
P_INH3 = re.compile(EENH + r'³')
P_ASCII = re.compile(EENH + r'\^?[23](?![\d²³])')
P_MENG = re.compile(r'\b(vierkante|kubieke) (mm|cm|dm|dam|hm|km|m)\b', re.I)
P_MACHT = re.compile(r'\d\s?[²³⁴]|\d\s?\^')
P_WOORD_OPP = re.compile(r'\bvierkante (?:milli|centi|deci|deca|hecto|kilo)?meters?\b', re.I)
P_WOORD_INH = re.compile(r'\bkubieke\b|\bkuub\b', re.I)
P_HECT = re.compile(r'\bhectare\b', re.I)
P_HA = re.compile(r'\d\s?ha\b')
P_ARE = re.compile(r'\d\s?a\b(?![\'’-])')
WOORD = {'mm²': r'vierkante millimeter', 'cm²': r'vierkante centimeter', 'dm²': r'vierkante decimeter', 'm²': r'vierkante meter',
         'km²': r'vierkante kilometer', 'hm²': r'vierkante hectometer', 'dam²': r'vierkante decameter',
         'cm³': r'kubieke centimeter', 'dm³': r'kubieke decimeter', 'm³': r'kubieke meter|\bkuub', 'mm³': r'kubieke millimeter', 'ha': r'hectare'}
INTRO = {6: ('cm²', 'dm²', 'm²'), 7: ('cm³', 'dm³', 'm³', 'km²', 'ha')}

def velden(it):
    yield 'opgave', it.get('opgave') or ''
    for s in it.get('opgaveStappen') or []: yield 'opgave', s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    for o in it.get('opties') or []: yield 'opties', (o.get('tekst') or '') if isinstance(o, dict) else str(o)
    if not it.get('opties') and it.get('optiesTekst'): yield 'opties', it['optiesTekst']
    yield 'antwoord', str(it.get('antwoord') or '')
    yield 'hint1', it.get('hint') or ''
    yield 'hint2', it.get('sterkereHint') or ''
    yield 'algemeneFoutHint', it.get('algemeneFoutHint') or ''
    for f in it.get('foutHints') or []:
        yield 'fout-hint', str(f.get('fout') or ''); yield 'fout-hint', f.get('uitleg') or ''
    yield 'ouderzin', it.get('ouderzin') or ''

def symbolen(t):
    s = {m.group(1) + '²' for m in P_OPP2.finditer(t)} | {m.group(1) + '³' for m in P_INH3.finditer(t)}
    if P_HA.search(t): s.add('ha')
    return s

def controleer(groep, items):
    """-> lijst (ernst, code, item-id, veld, fragment) en per-somtype INTRO-warns"""
    out = []; per_st = collections.defaultdict(lambda: {'sym': set(), 'woord': '', 'ids': [], 'doel': ''})
    def hit(ernst, code, it, veld, t, m):
        out.append((ernst, code, it.get('id'), veld, t[max(0, m.start() - 30):m.end() + 15].replace('\n', ' ')))
    for it in items:
        st = (it.get('merge') or {}).get('somtype', '?'); doel = (it.get('merge') or {}).get('doel') or it.get('doelId') or ''
        S = per_st[(doel, st)]; S['ids'].append(it.get('id')); S['doel'] = doel
        for veld, t in velden(it):
            if not t: continue
            if veld in ('opgave', 'hint1', 'hint2'): S['woord'] += ' ' + t
            S['sym'] |= symbolen(t) if veld != 'ouderzin' else set()
            if m := P_MACHT.search(t): hit('FAIL', 'MACHT', it, veld, t, m)
            if m := P_ASCII.search(t): hit('FAIL', 'ASCII', it, veld, t, m)
            if m := P_MENG.search(t): hit('FAIL', 'MENG', it, veld, t, m)
            for m in P_OPP2.finditer(t):
                if groep <= 5: hit('FAIL', 'OPP2', it, veld, t, m); break
                if groep == 6 and m.group(1) not in ('cm', 'dm', 'm'): hit('WARN', 'OPP2', it, veld, t, m); break
            if groep <= 6 and (m := P_INH3.search(t)): hit('FAIL', 'INH3', it, veld, t, m)
            if groep >= 6 and (m := P_ARE.search(t)): hit('FAIL', 'ARE-AFK', it, veld, t, m)
            if groep <= 5:
                for P in (P_WOORD_OPP, P_WOORD_INH, P_HECT):
                    if m := P.search(t): hit('WARN', 'WOORD', it, veld, t, m); break
            elif groep == 6:
                for P in (P_WOORD_INH, P_HECT):
                    if m := P.search(t): hit('WARN', 'WOORD', it, veld, t, m); break
    intro = []
    for (doel, st), S in per_st.items():
        for sym in sorted(S['sym']):
            if sym in INTRO.get(groep, ()) and not re.search(WOORD[sym], S['woord'], re.I):
                intro.append(('WARN', 'INTRO', doel, st, sym, len(S['ids'])))
        if groep == 6 and 'ha' in S['sym'] and not re.search('hectare', S['woord'], re.I):
            intro.append(('WARN', 'HA', doel, st, 'ha', len(S['ids'])))
    return out, intro

def rapport(groep, items, max_regels=12):
    out, intro = controleer(groep, items)
    tel = collections.Counter((e, c) for e, c, *_ in out); ti = collections.Counter((e, c) for e, c, *_ in intro)
    codes = ['MACHT', 'OPP2', 'INH3', 'ASCII', 'MENG', 'WOORD', 'ARE-AFK']
    print(f"\nMAAT (notatie_machten.md, G{groep}): " + ' · '.join(f"{c} {sum(n for (e, k), n in tel.items() if k == c)}" for c in codes) +
          f" · INTRO {ti[('WARN', 'INTRO')]} somtypes · HA {ti[('WARN', 'HA')]}  (FAIL {sum(n for (e, _), n in tel.items() if e == 'FAIL')}, "
          f"WARN {sum(n for (e, _), n in tel.items() if e == 'WARN') + sum(ti.values())})")
    gezien = collections.Counter()
    for e, c, iid, veld, frag in out:
        gezien[c] += 1
        if gezien[c] <= max_regels: print(f"  {e} {c} {iid} [{veld}] …{frag}…")
    for e, c, doel, st, sym, n in sorted(intro)[:40]:
        print(f"  {e} {c} {doel} '{st[:60]}' ({n} items): {sym} zonder '{WOORD[sym].split('|')[0]}' in opgave/Hint 1/Hint 2")
    return sum(n for (e, _), n in tel.items() if e == 'FAIL')

if __name__ == '__main__':
    g = int(sys.argv[1]); its = [it for p in sys.argv[2:] for it in json.load(open(p))['items']]
    sys.exit(1 if rapport(g, its) else 0)
