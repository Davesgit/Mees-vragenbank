"""Didactiek-besluit kloktijden (8 okt 15:46): in lopende tekst (kop, opgave, opties, hints, uitleg, antwoordtekst) staat een tijd als
'14.30 uur' / '3.00 uur', nooit met ':' (en nooit ':' samen met 'uur'). ':' mag alleen bij een item dat expliciet een digitale klok laat
zien; zo'n item krijgt `digitaleKlok: true` (wordt hier overgeslagen). Typ-invoer: '14.30', '14:30' en '14.30 uur' zijn dezelfde tijd
(geldigeAntwoorden en foutRegels.match.waarden krijgen alle drie de vormen); de instructie wordt «(Typ als 14.30.)».
Z-#843 (Didactiek 16:17): alleen kindteksten: kop (merge.somtype), opgave, opgaveStappen, opties, optiesTekst, antwoord, antwoordDetail,
geldigeAntwoorden, hint, sterkereHint, ouderzin, foutHints (fout/uitleg/uitlegSterker/laag2), foutHintsTekst, foutRegels (tekst/tekstSterker/
match.waarden), algemeneFoutHint en Claudes kindvelden in extraVelden (claudeUitleg, claudeKaleSom, claudeHint*, claudeFoutHints fout/uitleg,
claudeDenkfouten fout). Bronmetadata (merge.reden, visual.toelichting, foutHints.regel, bron, licentie, somtypeOrigineel …) blijft zoals hij is.
geldigeAntwoorden staat bovenaan het item (zoals in de rest van de bank; README: `geldigeAntwoorden`), niet in antwoordDetail.
Gebruik: import kloktijd_fix as KF; n = KF.zet_om(item)  → aantal omgezette tijden (0 = niets veranderd).
         KF.digitaal(item) → True als het item een digitale klok laat zien (kop '(opties digitaal)' / '(tijd digitaal)' en een tijd met ':')."""
import re
TIJD = re.compile(r'(?<![\d:.,])(\d{1,2}):(\d{2})(?![\d:])')
KOP = re.compile(r'#:#(?: uur)?')
TYP_OUD = re.compile(r'Typ de tijd,? zoals \d{1,2}[:.]\d{2}\.?')
TYP = '(Typ als 14.30.)'
def _ok(h, m): return int(h) <= 24 and int(m) <= 59
def tekst(t):
    """lopende tekst: '9:50 uur' → '9.50 uur', '9:50' → '9.50 uur', na 'Typ als'/'zoals' → '9.50' (instructie zonder 'uur');
    'Typ de tijd, zoals 9:05.' → '(Typ als 14.30.)'"""
    n = [0]
    if TYP_OUD.search(t): t = TYP_OUD.sub(TYP, t); n[0] += 1
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
def _istijd(w): return isinstance(w, str) and (TIJD.search(w) or re.fullmatch(r'\d{1,2}\.\d{2} uur', w))
def _lijst(v):
    out = []
    for w in v:
        for x in (varianten(w) if _istijd(w) else [w]):
            if x not in out: out.append(x)
    return out
TOP = ('opgave', 'opgaveStappen', 'opties', 'optiesTekst', 'antwoord', 'antwoordDetail', 'hint', 'sterkereHint', 'ouderzin', 'foutHintsTekst', 'algemeneFoutHint')
FH = ('fout', 'uitleg', 'uitlegSterker', 'laag2')
FR = ('tekst', 'tekstSterker')
def digitaal(it):
    k = (it.get('merge') or {}).get('somtype') or ''
    if not re.search(r'\((opties|tijd) digitaal\)', k): return False
    w = [it.get('opgave') or '', str(it.get('antwoord') or '')] + [str(o.get('tekst')) for o in it.get('opties') or []]
    return any(TIJD.search(x) for x in w)
def zet_om(it, typ_erbij=False):
    """typ_erbij=True (G3–G5, r13): een open vraag met een tijd als antwoord zonder instructie krijgt ' (Typ als 14.30.)' achter de opgave."""
    if it.get('digitaleKlok'): return 0
    n = [0]
    def s(v):
        if isinstance(v, str):
            t, c = tekst(v); n[0] += c; return t
        if isinstance(v, list): return [s(x) for x in v]
        if isinstance(v, dict): return {k: (s(x) if k not in ('letter', 'juisteOptie') else x) for k, x in v.items()}
        return v
    for k in TOP:
        if k in it and it[k] is not None: it[k] = s(it[k])
    for f in it.get('foutHints') or []:
        for k in FH:
            if isinstance(f.get(k), str): f[k] = s(f[k])
    for f in it.get('foutRegels') or []:
        for k in FR:
            if isinstance(f.get(k), str): f[k] = s(f[k])
        m = f.get('match')
        if isinstance(m, dict) and isinstance(m.get('waarden'), list) and any(_istijd(w) for w in m['waarden']):
            m['waarden'] = _lijst(m['waarden']); n[0] += 1
    ex = it.get('extraVelden') or {}
    for k in list(ex):
        if not k.startswith('claude'): continue
        v = ex[k]
        if isinstance(v, str): ex[k] = s(v)
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for kk in ('fout', 'uitleg', 'tekst'):
                        if isinstance(d.get(kk), str): d[kk] = s(d[kk])
                elif isinstance(d, str): pass
    if isinstance(it.get('geldigeAntwoorden'), list) and any(_istijd(w) for w in it['geldigeAntwoorden']):
        it['geldigeAntwoorden'] = _lijst(it['geldigeAntwoorden']); n[0] += 1
    m = it.get('merge') or {}
    if isinstance(m.get('somtype'), str) and ('#:#' in m['somtype'] or TYP_OUD.search(m['somtype']) or re.search(r'Typ de tijd,? zoals #:#\.?', m['somtype'])):
        k = re.sub(r'Typ de tijd,? zoals #:#\.?', TYP, m['somtype']); k = re.sub(r'(Typ als|zoals) #:#', r'\1 #.#', k); m['somtype'] = KOP.sub('#.# uur', k)
    # typ-invoer: het antwoord is een tijd → geldigeAntwoorden (bovenaan het item) met alle drie de vormen
    if it.get('type') != 'meerkeuze' and re.fullmatch(r'\d{1,2}\.\d{2} uur', str(it.get('antwoord'))) and not (it.get('merge') or {}).get('somtype', '').startswith('[klok-zetten'):
        if typ_erbij and 'Typ als' not in (it.get('opgave') or ''):
            it['opgave'] = it['opgave'].rstrip() + ' ' + TYP; n[0] += 1
            if isinstance(m.get('somtype'), str) and 'Typ als' not in m['somtype']: m['somtype'] = m['somtype'].rstrip() + ' ' + TYP
        ad = it.get('antwoordDetail')
        oud = list(it.get('geldigeAntwoorden') or []) + (list(ad.pop('geldigeAntwoorden')) if isinstance(ad, dict) and 'geldigeAntwoorden' in ad else [])
        it['geldigeAntwoorden'] = _lijst(oud + [it['antwoord']])
    return n[0]
