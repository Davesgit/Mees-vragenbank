#!/usr/bin/env python3
"""Past de fout-hintregels van Oefeningen (hints/batch*.json: soort → regel → tekst) per item toe.
Regels gelden van boven naar beneden; de eerste die past, wint. Gebruikt door apply_hints.py.
Per item komt er uit:
  foutHints   concrete sleutels (fout getal / optietekst / vak) met kindtekst, zoals het exportformaat ze kent
  foutRegels  de geordende regels met een matcher (waarden / kleinerDan / vanaf / totEnMet / alles) voor invoer
              die niet als sleutel voorkomt; 'alles' = algemene zin
Basis is extraVelden.claudeFoutHints (door build_g3.py gezet), dus opnieuw draaien geeft hetzelfde resultaat."""
import re, difflib

def _int(v):
    v = str(v).strip()
    return int(v) if re.fullmatch(r'\d+', v) else None

def _nums(t):
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', t)
    return [int(x) for x in re.findall(r'(?<![\w:])\d+(?![\w:])', t)]

def _uur(v):
    m = re.fullmatch(r'(\d+)(?: uur|:00)', str(v).strip())
    return int(m.group(1)) if m else None

def _wrap(h): return (h - 1) % 12 + 1

class Ctx:
    def __init__(self, it):
        self.it = it; self.opg = (it['opgave'] or '').replace('\n', ' ')
        self.nums = _nums(self.opg); self.ans = str(it['antwoord']); self.a = _int(self.ans)
        self.jr = it['visual']['jsRender'] or {}
        self.g1 = self.nums[0] if self.nums else None; self.g2 = self.nums[1] if len(self.nums) > 1 else None
    def code(self, v):
        v = str(v)
        if re.fullmatch(r'[A-L][1-9]', v): return v
        for d in self.jr.get('dingen', []):
            if d['wat'] == v: return d['vak']
        return None

def compile_regel(regel, c):
    """-> dict(exact=set|None, pred=callable|None, alles=bool, beschrijving) of None als de regel niet te lezen is."""
    r = regel.lower().replace('−', '-').strip()
    a, g1, g2, n = c.a, c.g1, c.g2, c.nums
    E = lambda *vals: {'exact': {str(x) for x in vals if x is not None and (not isinstance(x, int) or x >= 0)}}
    if r.startswith('andere fout') or 'of een andere fout' in r or r.startswith('ander vak') or 'een andere vorm of kleur' in r or 'een klok met een ander uur' in r:
        return {'alles': True}
    if r.startswith('volgorde omgedraaid'): return E('|'.join(reversed(c.ans.split('|'))))
    if r.startswith('de minsom omgedraaid'):
        return {'pred': lambda v: bool(re.fullmatch(r'(\d+) - (\d+)', v.replace('−', '-'))) and int(re.findall(r'\d+', v)[0]) < int(re.findall(r'\d+', v)[1])}
    if r.startswith('de plussom'): return {'pred': lambda v: '+' in v}
    if r.startswith('de minsom'): return {'pred': lambda v: '−' in v or ' - ' in v}
    if r.startswith('de keersom'): return {'pred': lambda v: '×' in v}
    # MKU-K03 vormnamen
    if r.startswith('fout = vierkant bij een rechthoek'):
        return {'pred': lambda v: (v, c.ans) in (('vierkant', 'rechthoek'), ('rechthoek', 'vierkant'))}
    m = re.match(r'fout = (cirkel|driehoek|rechthoek|vierkant)\b(?: \(bij een (\w+) of (\w+)\))?', r)
    if m:
        bij = {m.group(2), m.group(3)} - {None}
        return {'pred': lambda v: v == m.group(1) and (not bij or c.ans in bij)}
    if r.startswith('fout = ruit, ster of zeshoek'): return {'pred': lambda v: v in ('ruit', 'ster', 'zeshoek')}
    # spiegelen (MKU-E03): de stip is niet verplaatst = het kind tikt het vak van de stip zelf
    if r.startswith('stip niet verplaatst') or r.startswith('fout = het vak van de stip') or r.startswith('fout = het oorspronkelijke vak'):
        return E(c.jr.get('stip')) if c.jr.get('stip') else None
    # plattegrond-vakken (onze afspraak: letter = rij, cijfer = kolom)
    if r.startswith('goede letter, ander cijfer'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[0] == ca[0] and cv != ca}
    if r.startswith('goed cijfer, andere letter'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[1:] == ca[1:] and cv != ca}
    if r.startswith('letter en cijfer omgedraaid'):
        def omg(v):
            cv, ca = c.code(v), c.code(c.ans)
            return bool(cv and ca) and cv == f'{chr(64 + int(ca[1:]))}{ord(ca[0]) - 64}' and cv != ca
        return {'pred': omg}
    # klok
    if r.startswith('fout = 12 uur'): return E('12 uur') if c.ans != '12 uur' else {'exact': set()}
    if r.startswith('fout = een uur te vroeg of te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h - 1)} uur', f'{_wrap(h + 1)} uur') if h else None
    if r.startswith('fout = een uur te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h + 1)}:00' if ':' in c.ans else f'{_wrap(h + 1)} uur') if h else None
    # letterlijke optie ('het smalle glas'): de regel is (een deel van) de tekst van de foute optie
    if not r.startswith('fout') and any(r in (o['tekst'] or '').lower() for o in c.it['opties'] or []):
        return {'pred': lambda v: r in v.lower(), 'letterlijk': r}
    # getallen
    if a is None and not n: return None
    if re.match(r'fout = getal1 \+ getal2', r): return E(g1 + g2) if g2 is not None else None
    if re.match(r'fout = getal1 - getal2 of getal2 - getal1', r) or r.startswith('fout = verschil van de getallen'):
        return E(abs(g1 - g2)) if g2 is not None else None
    if re.match(r'fout = getal2 - de eenheden van getal1', r): return E(g2 - g1 % 10) if g2 is not None else None
    if re.match(r'fout = getal1\b', r): return E(g1)
    if re.match(r'fout = getal2\b', r): return E(g2)
    if re.match(r'fout = getal \+ 10 of antwoord \+ 10', r): return E(g1 + 10, a + 10)
    if re.match(r'fout = getal - 10 of antwoord - 10', r): return E(g1 - 10, a - 10)
    if re.match(r'fout = getal \+ 1\b', r): return E(g1 + 1)
    if r.startswith('fout = getal + bekend deel'): return E(n[0] + n[-1])
    if r.startswith('fout = een getal uit de vraag'): return E(*n)
    if r.startswith('fout kleiner dan het kleinste getal'): m0 = min(n); return {'pred': lambda v: _int(v) is not None and _int(v) < m0, 'kleinerDan': m0}
    if r.startswith('fout kleiner dan het getal in de vraag'): return {'pred': lambda v: _int(v) is not None and _int(v) < g1, 'kleinerDan': g1}
    if r.startswith('fout = laatste getal van de rij'):
        m = re.search(r'((?:\d+|□)(?:, (?:\d+|□))+)', c.opg); seq = m.group(1).split(', ') if m else []
        i = seq.index('□') if '□' in seq else len(seq)
        return E(int(seq[i - 1])) if i > 0 else None
    if r.startswith('fout = het aantal in de tekening'): return E(c.jr.get('aantal'))
    if r.startswith('fout = het getal dat eraf gaat'):
        m = re.search(r'(\d+) − (\d+)', c.opg.split('.')[1] if '.' in c.opg else c.opg); return E(int(m.group(2))) if m else None
    if r.startswith('fout = het deel dat al in de plussom staat'):
        m = re.search(r'(\d+) \+ □', c.opg); return E(int(m.group(1))) if m else None
    if r.startswith('fout = het hele getal'):
        m = re.search(r'□ = (\d+)', c.opg) or re.search(r'hoeveel (\d+) −', c.opg) or re.search(r'ook: (\d+) −', c.opg)
        return E(int(m.group(1))) if m else None
    if r.startswith('fout = getal opgeteld in plaats van eraf'):
        m = re.search(r'hoeveel (\d+) − (\d+)', c.opg) or re.search(r'(\d+) − (\d+) = □', c.opg)
        return E(int(m.group(1)) + int(m.group(2))) if m else None
    if a is None: return None
    if r.startswith('fout = antwoord ± 1'): return E(a - 1, a + 1)
    if re.match(r'fout = antwoord \+ 9 of \+ 10', r): return E(a + 9, a + 10)
    m = re.match(r'fout = antwoord ([+-]) (\d+) of meer', r)
    if m:
        k = int(m.group(2))
        if m.group(1) == '+': return {'pred': lambda v: _int(v) is not None and _int(v) >= a + k, 'vanaf': a + k}
        return {'pred': lambda v: _int(v) is not None and _int(v) <= a - k, 'totEnMet': a - k}
    m = re.match(r'fout = antwoord ([+-]) (\d+)', r)
    if m: return E(a + int(m.group(2)) if m.group(1) == '+' else a - int(m.group(2)))
    if r.startswith('fout ligt 1 of 2 naast'): return E(a - 2, a - 1, a + 1, a + 2)
    if r.startswith('fout ligt 1 naast'): return E(a - 1, a + 1)
    if r.startswith('fout ligt 2 naast'): return E(a - 2, a + 2)
    return None

UUR_WOORD = {1: 'één', 2: 'twee', 3: 'drie', 4: 'vier', 5: 'vijf', 6: 'zes', 7: 'zeven', 8: 'acht', 9: 'negen', 10: 'tien', 11: 'elf', 12: 'twaalf'}
def vul_in(tekst, c):
    """Vult sjabloonteksten per item in ('Bij [uur in woorden] uur … [uur als cijfer].'); None als het niet kan."""
    if '[uur in woorden]' not in tekst and '[uur als cijfer]' not in tekst: return None
    h = _uur(c.ans)
    if not h: return None
    return tekst.replace('[uur in woorden]', UUR_WOORD[h]).replace('[uur als cijfer]', str(h))

def per_item_tekst(regel, tekst):
    return 'tekst per item' in regel or '…' in tekst or '[plek]' in tekst or '[andere plek]' in tekst

PLACEHOLDER_STIP = '[TEKST NODIG (Oefeningen): stip niet verplaatst]'
def is_spiegel(it):
    jr = it['visual']['jsRender'] or {}
    return jr.get('soort') == 'vorm' and bool(jr.get('stip')) and bool(jr.get('as'))
def heeft_stipregel(st):
    return any(re.match(r'(stip niet verplaatst|fout = het vak van de stip|fout = het oorspronkelijke vak)', f['regel'].lower()) for f in st['foutHints'])

def _pas_toe_kern(it, st, alle_cellen=None):
    """st = somtype-entry uit hints/batch*.json. Zet it['foutHints'], it['foutRegels'], it['foutHintsTekst']."""
    c = Ctx(it)
    claude = [dict(f) for f in it['extraVelden'].get('claudeFoutHints') or []]
    claude_txt = {f['fout']: f['uitleg'] for f in claude}
    vervangen = {v['claudeTekst'] for v in st.get('claudeVervangen', [])} | {f['claudeTekst'] for f in st['foutHints'] if f.get('claudeTekst')}
    merge = {m['fout']: m for m in it['extraVelden'].get('mergeFoutHints') or []}
    regels = []
    for f in st['foutHints']:
        comp = compile_regel(f['regel'], c)
        per_item = per_item_tekst(f['regel'], f['tekst'])
        if comp is None and f['bron'] in ('claude', 'claude-taalfix'):     # niet te lezen Claude-regel: houd Claudes eigen tekst per item
            dk = f.get('claudeDenkfout')
            keys = {k['fout'] for k in claude if not dk or any(d['fout'] == k['fout'] and d['denkfout'] == dk for d in it['extraVelden'].get('claudeDenkfouten') or [])}
            comp = {'exact': keys, 'claudeSleutels': True}; per_item = True
        regels.append((f, comp, per_item))
    # MKU-E03 spiegelen: 'stip niet verplaatst' gaat vóór de algemene regels; zonder tekst van Oefeningen een gemarkeerde plaatshouder
    it['controle']['foutHintPlaceholder'] = None
    if is_spiegel(it) and not heeft_stipregel(st):
        f = {'regel': 'stip niet verplaatst (fout = het vak van de stip)', 'soort': 'stip niet verplaatst', 'bron': 'merge-plaatshouder', 'tekst': PLACEHOLDER_STIP}
        regels.insert(0, (f, {'exact': {it['visual']['jsRender']['stip']}}, False))
        it['controle']['foutHintPlaceholder'] = ['stip niet verplaatst']
    # kandidaten
    if it['opties']: kand = [o['tekst'] for o in it['opties'] if o['tekst'] != c.ans]
    elif alle_cellen: kand = [v for v in alle_cellen if v != c.ans]
    else:
        kand = list(dict.fromkeys([k['fout'] for k in claude] + sorted({v for _, comp, pi in regels if comp and not pi for v in comp.get('exact', ())},
                                                                        key=lambda x: (_int(x) is None, _int(x) or 0, x))))
        kand = [v for v in kand if v != c.ans]
    out = []; ongebruikt = []
    for v in kand:
        hit = None
        for f, comp, per_item in regels:
            if comp is None: continue
            ok = comp.get('alles') or (v in comp.get('exact', ())) or (comp.get('pred') and comp['pred'](v))
            if not ok: continue
            if per_item and vul_in(f['tekst'], c):
                hit = {'fout': v, 'uitleg': vul_in(f['tekst'], c), 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f"{f['bron']} (per item)"}; break
            if per_item:
                if v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
                    hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': f['regel'], 'soort': f.get('soort'), 'bron': 'claude (per item)'}; break
                continue
            tekst = f['tekst']
            if ' / ' in tekst and f['bron'] in ('claude', 'claude-taalfix'):
                # twee teksten van Claude: neem de tekst die bij dit item hoort (bij een taalfix: die het meest lijkt op Claudes tekst)
                delen = tekst.split(' / ')
                ct = claude_txt.get(v)
                tekst = max(delen, key=lambda d: difflib.SequenceMatcher(None, d, ct).ratio()) if ct else delen[0]
            hit = {'fout': v, 'uitleg': tekst, 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron']}; break
        if hit is None and v in merge:
            m = merge[v]; hit = {'fout': v, 'uitleg': m['uitleg'], 'regel': m['regel'], 'soort': None, 'bron': 'merge'}
        if hit is None and v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
            hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': '(geen regel; Claude-tekst blijft)', 'soort': None, 'bron': 'claude (geen regel)'}
        if hit: hit['stap'] = None; out.append(hit)
        elif v in claude_txt: ongebruikt.append(v)
    regels_out = []
    for f, comp, per_item in regels:
        if comp is None: regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'tekst': f['tekst'], 'match': None, 'leesbaar': False}); continue
        mt = {}
        if comp.get('alles'): mt = {'alles': True}
        elif 'exact' in comp: mt = {'waarden': sorted(comp['exact'], key=lambda x: (_int(x) is None, _int(x) or 0, x))}
        for k in ('kleinerDan', 'vanaf', 'totEnMet'):
            if k in comp: mt = {k: comp[k]}
        if comp.get('pred') and not mt: mt = {'waarden': [h['fout'] for h in out if h['regel'] == f['regel']], 'opOpties': True}
        regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron'], 'tekst': None if per_item else f['tekst'], 'perItem': per_item, 'match': mt, 'leesbaar': True})
    it['foutHints'] = [{'stap': h['stap'], 'fout': h['fout'], 'uitleg': h['uitleg'], 'regel': h['regel'], 'soort': h['soort'], 'bron': h['bron']} for h in out]
    it['foutRegels'] = regels_out
    it['algemeneFoutHint'] = next((f['tekst'] for f, comp, pi in regels if comp and comp.get('alles') and not pi), None)
    it['foutHintsTekst'] = ' · '.join(f"{h['fout']} → {h['uitleg']}" for h in out) or None
    it['controle']['zonderFoutHints'] = not out
    it['controle']['foutHintsNietToegepast'] = ongebruikt
    return [f['regel'] for f, comp, _ in regels if comp is None]

# r13 kloktijdronde (8 okt): overgenomen uit g8/scripts/fout_regels.py
# Kloktijden (besluit Didactiek 8 okt 15:46): de motor rekent intern met 'h:mm'. Heeft een item zijn tijd in de huisvorm ('14.30 uur' als antwoord of
# optie, of '(Typ als 14.30.)'), dan gaan een kopie van het item en van de hint-entry eerst naar 'h:mm'; daarna gaan foutHints, foutRegels en
# algemeneFoutHint terug naar de huisvorm: sleutel '14.30 uur', in teksten '14.30 uur' (na 'Typ als' zonder 'uur'), foutRegels.match.waarden in alle
# drie de vormen ('14.30 uur', '14.30', '14:30'). Een regel mag dus in beide vormen staan. Items met digitaleKlok: true en items zonder tijd in de
# huisvorm gaan ongewijzigd door de motor. KLOK_PUNT = False zet dit uit.
KLOK_PUNT = True
import copy as _copy_klok
_KP = re.compile(r'(?<![\d.,:])(\d{1,2})\.(\d{2})(?: uur)?(?![\d])')
_KD = re.compile(r'(?<![\d:.,])(\d{1,2}):(\d{2})(?![\d:])')
_KSKIP = {'bron', 'licentie', 'controle', 'merge', 'id', 'bronVariant', 'jsRender', 'husselPlan'}
def _klok_ok(h, m): return int(h) <= 24 and int(m) <= 59
def _klok_heeft_punt(it):
    if it.get('digitaleKlok'): return False
    w = [str(it.get('antwoord') or '')] + [str(o.get('tekst')) for o in it.get('opties') or []]
    return any(re.fullmatch(r'\s*\d{1,2}\.\d{2} uur\s*', x) for x in w) or bool(re.search(r'\(Typ als \d{1,2}\.\d{2}\.\)', it.get('opgave') or ''))
def _klok_naar_dubbelepunt(o):
    if isinstance(o, dict): return {k: (v if k in _KSKIP else _klok_naar_dubbelepunt(v)) for k, v in o.items()}
    if isinstance(o, list): return [_klok_naar_dubbelepunt(v) for v in o]
    if isinstance(o, str): return _KP.sub(lambda m: f'{m.group(1)}:{m.group(2)}' if _klok_ok(m.group(1), m.group(2)) else m.group(0), o)
    return o
def _klok_tekst(t):
    def r(m):
        h, mi = m.group(1), m.group(2)
        if not _klok_ok(h, mi): return m.group(0)
        voor, na = t[:m.start()], t[m.end():]
        if re.search(r'(Typ als|zoals)\s*$', voor): return f'{h}.{mi}'
        return f'{h}.{mi}' if na.startswith(' uur') else f'{h}.{mi} uur'
    return _KD.sub(r, t)
def _klok_vormen(w):
    m = re.fullmatch(r'\s*(\d{1,2})[:.](\d{2})(?: uur)?\s*', str(w))
    if not m or int(m.group(1)) > 24: return [w]      # V-#1012 (Didactiek r13, les 387): ook een foutsleutel met minuten ≥ 60 ('12:85') in alle drie de vormen, want een kind typt volgens de instructie '12.85'
    return [f'{m.group(1)}.{m.group(2)} uur', f'{m.group(1)}.{m.group(2)}', f'{m.group(1)}:{m.group(2)}']
def _klok_naar_punt(o, k=None):
    if isinstance(o, dict): return {kk: _klok_naar_punt(v, kk) for kk, v in o.items()}
    if isinstance(o, list):
        if k == 'waarden': return list(dict.fromkeys(x for w in o for x in (_klok_vormen(w) if isinstance(w, str) else [w])))
        return [_klok_naar_punt(v) for v in o]
    if isinstance(o, str): return _klok_tekst(o)
    return o
def pas_toe(it, st, alle_cellen=None):
    if not (KLOK_PUNT and _klok_heeft_punt(it)): return _pas_toe_kern(it, st, alle_cellen)
    a, e = _klok_naar_dubbelepunt(it), _klok_naar_dubbelepunt(st)
    oud = {k: _copy_klok.deepcopy(a.get(k)) for k in a}
    regels = {json_klok(r2): r1 for r1, r2 in zip(_regels_van(st), _regels_van(e))}
    terug = _pas_toe_kern(a, e, alle_cellen)
    for k in a:
        if k not in oud or a[k] != oud[k]: it[k] = _klok_naar_punt(a[k], k)
    return [regels.get(json_klok(r), r) for r in terug] if isinstance(terug, list) else terug
def _regels_van(st): return [f.get('regel') for f in st.get('foutHints') or []]
def json_klok(r): return r if isinstance(r, str) else repr(r)
