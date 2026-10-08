"""Didactiek-besluit kloktijden (8 okt 15:46): in lopende tekst (kop, opgave, opties, hints, uitleg, antwoordtekst) staat een tijd als
'14.30 uur' / '3.00 uur', nooit met ':' (en nooit ':' samen met 'uur'). ':' mag alleen bij een item dat expliciet een digitale klok laat
zien; zo'n item krijgt `digitaleKlok: true` (wordt hier overgeslagen). Typ-invoer: '14.30', '14:30' en '14.30 uur' zijn dezelfde tijd
(geldigeAntwoorden en foutRegels.match.waarden krijgen alle drie de vormen); de instructie wordt «(Typ als 14.30.)».
Gebruik: import kloktijd_fix as KF; n = KF.zet_om(item)  → aantal omgezette tijden (0 = niets veranderd)."""
import re
TIJD = re.compile(r'(?<![\d:.,])(\d{1,2}):(\d{2})(?![\d:])')
KOP = re.compile(r'#:#(?: uur)?')
SKIP = {'bron', 'licentie', 'controle', 'merge', 'id', 'bronVariant', 'invoer', 'invoerUitleg', 'jsRender', 'husselPlan'}
LIJST_VARIANT = {'geldigeAntwoorden', 'accept', 'waarden'}
def _ok(h, m): return int(h) <= 24 and int(m) <= 59
def tekst(t):
    """lopende tekst: '9:50 uur' → '9.50 uur', '9:50' → '9.50 uur', na 'Typ als'/'zoals' → '9.50' (instructie zonder 'uur')"""
    n = [0]
    def r(m):
        h, mi = m.group(1), m.group(2)
        if not _ok(h, mi): return m.group(0)
        voor, na = t[:m.start()], t[m.end():]
        if re.search(r'schaal\s*$', voor, re.I): return m.group(0)
        n[0] += 1
        if re.search(r'(Typ als|zoals|Typ de tijd als)\s*$', voor): return f'{h}.{mi}'
        if na.startswith(' uur'): return f'{h}.{mi}'
        return f'{h}.{mi} uur'
    return TIJD.sub(r, t), n[0]
def varianten(w):
    """'14:30' / '14.30' / '14.30 uur' → alle drie"""
    m = re.fullmatch(r'\s*(\d{1,2})[:.](\d{2})(?: uur)?\s*', str(w))
    if not m or not _ok(*m.groups()): return [w]
    h, mi = m.groups(); return [f'{h}.{mi} uur', f'{h}.{mi}', f'{h}:{mi}']
def _lijst(v):
    out = []
    for w in v:
        for x in (varianten(w) if isinstance(w, str) and TIJD.search(w) or (isinstance(w, str) and re.fullmatch(r'\d{1,2}\.\d{2} uur', w)) else [w]):
            if x not in out: out.append(x)
    return out
def zet_om(it):
    if it.get('digitaleKlok'): return 0
    n = [0]
    def walk(o):
        if isinstance(o, dict):
            for k in list(o):
                v = o[k]
                if k in SKIP: continue
                if k in LIJST_VARIANT and isinstance(v, list) and any(isinstance(w, str) and TIJD.search(w) for w in v):
                    o[k] = _lijst(v); n[0] += 1; continue
                if isinstance(v, str):
                    t, c = tekst(v)
                    if c: o[k] = t; n[0] += c
                else: walk(v)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                if isinstance(v, str):
                    t, c = tekst(v)
                    if c: o[i] = t; n[0] += c
                else: walk(v)
    walk(it)
    m = it.get('merge') or {}
    for k in ('somtype', 'somtypeOrigineel'):
        if isinstance(m.get(k), str) and '#:#' in m[k]:
            m[k] = re.sub(r'(Typ als|zoals) #:#', r'\1 #.#', m[k]); m[k] = KOP.sub('#.# uur', m[k])
    # typ-invoer: het antwoord is een tijd → geldigeAntwoorden met alle drie de vormen
    if n[0] and it.get('type') != 'meerkeuze' and re.fullmatch(r'\d{1,2}\.\d{2} uur', str(it.get('antwoord'))):
        ad = it.get('antwoordDetail')
        if not isinstance(ad, dict): ad = it['antwoordDetail'] = {}
        ad['geldigeAntwoorden'] = _lijst((ad.get('geldigeAntwoorden') or []) + [it['antwoord']])
    return n[0]
