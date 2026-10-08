"""Z-#782 (Didactiek G8 batch 2, 8 okt; les 243) + besluit kloktijden (Didactiek 15:46): een kloktijd schrijf je als '15.00 uur', niet met ':'.
FAIL, ook bij typ-invoer. Alleen items met `digitaleKlok: true` (een echte digitale klok in beeld of in de zin) worden overgeslagen.
Kijkt in de kindteksten: opgave, antwoord, opties, hint, sterkereHint, ouderzin, foutHints (uitleg/uitlegSterker), algemeneFoutHint;
Z-#1018: ook optiesTekst, foutHintsTekst, opgaveStappen, begripUitleg, sterkereHintMetPlaatje, appMoetTonen.
V-#1012: ook KLOKWOORD ('dubbele punt') en KLOKSLEUTEL ('h:mm' ook als 'h.mm').
Patroon \\b\\d{1,2}:\\d{2}\\b; 'schaal 1 : 100' (met spaties) en '1:100' na 'schaal' tellen niet.
Gebruik: import kloktijd_check as KT; n = KT.rapport(items, ernst='FAIL')."""
import re
KLOK = re.compile(r'(?<![\d:])(\d{1,2}):(\d{2})(?![\d:])')
def teksten(it):
    yield 'kop', (it.get('merge') or {}).get('somtype'); yield 'opgave', it.get('opgave'); yield 'antwoord', it.get('antwoord')
    for o in it.get('opties') or []: yield 'optie', o.get('tekst') if isinstance(o, dict) else o
    for k in ('hint', 'sterkereHint', 'ouderzin', 'algemeneFoutHint'):
        v = it.get(k)
        if isinstance(v, dict): v = ' '.join(str(x) for x in v.values() if isinstance(x, str))
        yield k, v
    for f in it.get('foutHints') or []:
        for k in ('uitleg', 'uitlegSterker'): yield 'foutHint', f.get(k)
    for f in it.get('foutRegels') or []:
        for k in ('tekst', 'tekstSterker'): yield 'foutRegel', f.get(k)
    # Z-#1018 (Didactiek r13): ook deze kindvelden
    for k in ('optiesTekst', 'foutHintsTekst', 'opgaveStappen', 'begripUitleg', 'sterkereHintMetPlaatje', 'appMoetTonen'):
        v = it.get(k)
        if isinstance(v, list): v = ' · '.join(x if isinstance(x, str) else ' '.join(str(y) for y in x.values() if isinstance(y, str)) if isinstance(x, dict) else str(x) for x in v)
        elif isinstance(v, dict): v = ' '.join(str(x) for x in v.values() if isinstance(x, str))
        yield k, v
def treffers(items):
    T = []
    for it in items:
        if it.get('digitaleKlok'): continue
        for veld, t in teksten(it):
            if not isinstance(t, str): continue
            if veld == 'kop':
                if '#:#' in t: T.append((it, f"{it['id']} [kop]: '#:#' in «{t[:70]}»")); break
                continue
            for m in KLOK.finditer(t):
                if veld == 'kop': continue
                if re.search(r'schaal\s*$', t[:m.start()], re.I): continue
                if int(m.group(1)) > 24 or int(m.group(2)) > 59: continue
                T.append((it, f"{it['id']} [{veld}]: {m.group(0)} in «{t[max(0, m.start() - 30):m.end() + 20]}»")); break
    return T
DUUR = re.compile(r'(\+|\bduurt|\bduurde|\bduur van)\s*(\d{1,2})[.:](\d{2})(?: uur)?(?![\d:])')
# Z-#951 (Didactiek, les 356): ook een duur zonder signaalwoord: 'Tel 5.45 uur bij … op', '2.30 uur onderweg', '1.20 uur later', 'een vlucht van 2.15 uur',
# 'in 1.20 uur', 'Na 1.20 uur …'. Een kloktijd ('om 9.30 uur', 'Het is 9.30 uur', 'van 8.10 uur tot 9.30 uur', 'Tel 2 uur bij 9.30 uur op') telt niet.
# 'na u.mm uur' is alleen een duur bij u ≤ 2 of als de tekst nog een andere tijd noemt (het beginpunt); 'Na 9.30 uur gaat de winkel dicht' blijft een kloktijd.
_T = r'(\d{1,2})[.:](\d{2})'
DUUR2 = [re.compile(r'\b[Tt]el ' + _T + r'(?: uur)? (?:erbij|bij)\b'),
         re.compile(_T + r' uur (?:later|eerder|onderweg|lang|vliegen|rijden|varen|fietsen|lopen|wandelen|reizen|bezig|nodig)\b'),
         re.compile(r'\b(?:vlucht|reis|rit|tocht|wandeling|film|treinreis|busreis|fietstocht) van ' + _T),
         re.compile(r'\b(?:[Ii]n|[Bb]innen) ' + _T + r' uur\b')]
NA = re.compile(r'\b[Nn]a ' + _T + r' uur\b')
TIJD_ALG = re.compile(r'(?<![\d.,:])(\d{1,2})[.:](\d{2})(?![\d:])')
def _duur_match(t):
    m = DUUR.search(t)
    if m and int(m.group(3)) <= 59: return m
    for rx in DUUR2:
        m = rx.search(t)
        if m and int(m.group(2)) <= 59: return m
    m = NA.search(t)
    if m and int(m.group(2)) <= 59:
        ander = [x for x in TIJD_ALG.finditer(t) if x.start() != m.start(1)]
        if int(m.group(1)) <= 2 or ander: return m
    return None
def duur_treffers(items):
    """V-#904 (Didactiek G8 batch 5, les 331): een tijdsduur als kloktijd ('6.15 uur + 5.45 uur', 'duurt 1.30 uur') in een kindtekst of Claudes kindvelden (FAIL),
    ook bij digitaleKlok (een duur is nooit een kloktijd)."""
    T = []
    for it in items:
        ex = it.get('extraVelden') or {}
        velden = list(teksten(it)) + [(k, ex.get(k)) for k in ('claudeUitleg', 'claudeKaleSom')]
        for veld, t in velden:
            if isinstance(t, str) and (m := _duur_match(t)):
                T.append((it, f"{it['id']} [{veld}]: «{t[max(0, m.start() - 25):m.end() + 5]}»")); break
    return T
TIJD_ITEM = re.compile(r'(?<![\d.,:])\d{1,2}[.:]\d{2}(?: uur)?(?![\d:])')
def _tijd_item(it):
    return any(isinstance(t, str) and TIJD_ITEM.search(t) and ' uur' in t for t in [it.get('opgave'), it.get('antwoord')] + [o.get('tekst') if isinstance(o, dict) else o for o in it.get('opties') or []])
def dubbelepunt_treffers(items):
    """V-#1012 (Didactiek r13, les 387): na de notatiewissel ':' → '.' mag een kindtekst bij een tijd-item zonder digitaleKlok niet meer over 'de dubbele punt' praten (FAIL)."""
    T = []
    for it in items:
        if it.get('digitaleKlok') or not _tijd_item(it): continue
        for veld, t in teksten(it):
            if isinstance(t, str) and re.search(r'dubbele punt', t, re.I): T.append((it, f"{it['id']} [{veld}]: «{t[:90]}»")); break
    return T
def klokvorm_treffers(items):
    """V-#1012: een kloksleutel 'h:mm' in foutRegels.match.waarden (ook minuten ≥ 60, '12:85') moet er ook in de '.'-vorm staan ('12.85'), anders krijgt
    een kind dat volgens de instructie typt de fout-hint niet (FAIL; alleen items zonder digitaleKlok met een tijd)."""
    T = []
    for it in items:
        if it.get('digitaleKlok') or not _tijd_item(it): continue
        for r in it.get('foutRegels') or []:
            w = [str(x) for x in ((r.get('match') or {}).get('waarden') or [])]
            mis = [x for x in w if (m := re.fullmatch(r'(\d{1,2}):(\d{2})', x)) and f'{m.group(1)}.{m.group(2)}' not in w]
            if mis: T.append((it, f"{it['id']} [{r.get('regel')}]: alleen {mis[0]!r}, niet '{mis[0].replace(':', '.')}'")); break
    return T
def typvoorbeeld_treffers(items):
    """Oef-#1021 (les 234-achtig): het voorbeeld in «(Typ als 14.30.)» mag niet het antwoord of een fout-sleutel van het item zijn; wie het voorbeeld overtypt,
    krijgt anders 'goed' of een fout-hint die niet over het voorbeeld gaat (FAIL)."""
    T = []
    for it in items:
        m = re.search(r'\(Typ als (\d{1,2})[.:](\d{2})\.\)', it.get('opgave') or '')
        if not m: continue
        h, mi = m.groups(); vormen = {f'{h}.{mi}', f'{h}.{mi} uur', f'{h}:{mi}'}
        sleutels = {w for f in it.get('foutRegels') or [] for w in ((f.get('match') or {}).get('waarden') or [])}
        goed = {str(it.get('antwoord'))} | set(it.get('geldigeAntwoorden') or [])
        if vormen & sleutels: T.append((it, f"{it['id']}: voorbeeld '{h}.{mi}' is een fout-sleutel ({sorted(vormen & sleutels)})"))
        if vormen & goed: T.append((it, f"{it['id']}: voorbeeld '{h}.{mi}' is het goede antwoord"))
    # V-#1080 (Didactiek r13, G7-MEET-04 021–044): ook «(Typ … bijvoorbeeld X.)» in elke typ-instructie (G3–G8). X (ook met '-'/'−' gewisseld) is geen
    # antwoord, geen fout-sleutel en geen optie; anders leest de motor het voorbeeld als 'getal uit de vraag' of krijgt wie het overtypt 'goed'.
    for it in items:
        m = re.search(r'\((?:Typ|typ)\b[^()]*?\bbijvoorbeeld ([^()]+?)\.?\)', it.get('opgave') or '')
        if not m: continue
        x = m.group(1).strip(); vormen = {x, x.replace('−', '-'), x.replace('-', '−')}
        sleutels = {str(w) for f in it.get('foutRegels') or [] for w in ((f.get('match') or {}).get('waarden') or [])} | {str(f.get('fout')) for f in it.get('foutHints') or []}
        goed = {str(it.get('antwoord'))} | {str(g) for g in it.get('geldigeAntwoorden') or []} | {str(o.get('tekst')) for o in it.get('opties') or []}
        if vormen & sleutels: T.append((it, f"{it['id']}: voorbeeld 'bijvoorbeeld {x}' is een fout-sleutel ({sorted(vormen & sleutels)})"))
        elif vormen & goed: T.append((it, f"{it['id']}: voorbeeld 'bijvoorbeeld {x}' is het goede antwoord of een optie"))
    return T
def typvoorbeeld_mutant_ok():
    it = {'id': 'mut-1211', 'opgave': 'De kinderen vertrekken om 12.55 uur. De reis duurt 1 uur en 25 minuten. Hoe laat komen ze aan? (Typ als 14.30.)', 'antwoord': '14.20 uur',
          'foutRegels': [{'match': {'waarden': ['14.30 uur', '14.30', '14:30']}}]}
    ok = bool(typvoorbeeld_treffers([it])) and not typvoorbeeld_treffers([dict(it, opgave=it['opgave'].replace('14.30.)', '9.45.)'))])
    # V-#1080: G7-MEET-04 021-vorm: «bijvoorbeeld −3» is een sleutel ('getal uit de vraag') → FAIL; met «bijvoorbeeld −20» niet
    b = {'id': 'mut-1080', 'opgave': "Het is 3 graden in de tuin. 's Nachts daalt de temperatuur 11 graden. Hoeveel graden is het dan? (Typ een min voor een getal onder nul, bijvoorbeeld −3.)",
         'antwoord': '−8', 'foutHints': [{'fout': '−3'}, {'fout': '-3'}, {'fout': '8'}], 'foutRegels': [{'match': {'waarden': ['−3', '-3']}}]}
    return ok and bool(typvoorbeeld_treffers([b])) and not typvoorbeeld_treffers([dict(b, opgave=b['opgave'].replace('−3.)', '−20.)'))])
def invoer(it):
    """typ-invoer van een tijd ('(Typ als 14:30.)'): de motor en de app lezen 'uu:mm'; omzetten vraagt eerst motorsteun → WARN, niet FAIL"""
    return '(Typ als' in (it.get('opgave') or '')
def rapport(items, ernst='FAIL', toon=True):
    T = treffers(items); F = [x for it, x in T]; W = []; D = sum(1 for it in items if it.get('digitaleKlok')); DU = [x for it, x in duur_treffers(items)]
    if toon:
        print(f"\nKLOKTIJD (Z-#782: kloktijd met ':' in een kindtekst; schrijf '15.00 uur'): {len(F)} ({ernst}) · overgeslagen met digitaleKlok: {D}")
        for x in F[:15]: print(f'  {ernst} KLOKTIJD', x)
        for x in W[:3]: print('  WARN KLOKTIJD-INVOER', x)
        print(f"TIJDSDUUR (V-#904: een duur als kloktijd, '6.15 uur + 5.45 uur'; schrijf '5 uur en 45 minuten'): {len(DU)} ({ernst})")
        for x in DU[:10]: print(f'  {ernst} TIJDSDUUR', x)
    DP = [x for it, x in dubbelepunt_treffers(items)]; KV = [x for it, x in klokvorm_treffers(items)]
    if toon:
        print(f"KLOKWOORD (V-#1012: 'dubbele punt' in een kindtekst bij een tijd zonder digitaleKlok): {len(DP)} ({ernst})")
        for x in DP[:8]: print(f'  {ernst} KLOKWOORD', x)
        print(f"KLOKSLEUTEL (V-#1012: kloksleutel 'h:mm' ook in de '.'-vorm, ook bij minuten ≥ 60): {len(KV)} ({ernst})")
        for x in KV[:8]: print(f'  {ernst} KLOKSLEUTEL', x)
        print(f"  mutanten tijdsduur {mutanten()}/{len(MUTANTEN)} · V-#1012 {mutanten1012()}/2")
    TV = [x for it, x in typvoorbeeld_treffers(items)]
    if toon:
        print(f"TYPVOORBEELD (Oef-#1021: het voorbeeld in '(Typ als …)' is geen antwoord en geen fout-sleutel): {len(TV)} ({ernst}) · mutant {'ok' if typvoorbeeld_mutant_ok() else 'MIS'}")
        for x in TV[:8]: print(f'  {ernst} TYPVOORBEELD', x)
    return len(F) + len(DU) + len(DP) + len(KV) + len(TV)

# les 348: de tijdsduur-check herkent zowel de '.'- als de ':'-notatie
MUTANTEN = [('8:10 + 1:20', True), ('8.10 uur + 1.20 uur', True), ('De reis duurt 1:20.', True), ('duurt 1.20 uur', True), ('duurde 0:45', True),
            ('8.10 uur + 1 uur en 20 minuten', False), ('Van 8.10 uur tot 9.30 uur', False), ('9.30 uur − 8.10 uur', False),
            # Z-#951 (les 356): zonder signaalwoord
            ('Tel 5.45 uur bij 6.15 uur op.', True), ('Na 1.20 uur komen ze aan.', True), ('Je bent 2.30 uur onderweg.', True), ('1.20 uur later is het 9.30 uur.', True),
            ('Het is een vlucht van 2.15 uur.', True), ('Ze vertrekken om 8.10 uur. Na 3.20 uur komen ze aan.', True), ('In 1:20 uur rijd je naar oma.', True),
            ('Om 9.30 uur begint de les.', False), ('Het is 9.30 uur.', False), ('Na 9.30 uur gaat de winkel dicht.', False), ('Tel 2 uur bij 9.30 uur op.', False),
            ('De les begint om 8.30 uur en duurt 45 minuten.', False)]
def mutanten():
    """aantal mutanten dat goed gaat (moet len(MUTANTEN) zijn)"""
    mk = lambda t: {'id': 'mut', 'opgave': t, 'extraVelden': {}, 'antwoord': 'x'}
    return sum(bool(duur_treffers([mk(t)])) == verwacht for t, verwacht in MUTANTEN)

def mutanten1012():
    """V-#1012: oud G5-MEET-E06 1200 (tekst 'dubbele punt', sleutel alleen '12:85') → beide guards vuren"""
    it = {'id': 'mut-1200', 'opgave': 'Het is 12.25 uur. Hoe laat is het 1 uur en 10 minuten later?', 'antwoord': '13.35 uur', 'extraVelden': {},
          'foutHints': [{'fout': '12:85', 'uitleg': 'Zestig minuten of meer kan niet achter de dubbele punt.'}],
          'foutRegels': [{'regel': 'overloop', 'tekst': 'Zestig minuten of meer kan niet achter de dubbele punt.', 'match': {'waarden': ['12:85']}}]}
    return int(bool(dubbelepunt_treffers([it]))) + int(bool(klokvorm_treffers([it])))
def alle_mutanten_ok(): return mutanten() == len(MUTANTEN) and mutanten1012() == 2 and typvoorbeeld_mutant_ok()
