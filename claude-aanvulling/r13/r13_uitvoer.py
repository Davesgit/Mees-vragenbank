#!/usr/bin/env python3
"""r13 zelf (na-ronde-r13; Leerlijn-besluit BESLUIT_R9-4_R10_NIVEAUS.md, 8 okt 14:40; opdracht Dave/Overzicht 17:32 en 17:51).
Werkt op r13/g5 en r13/g6 (kopie van de goedgekeurde builds + kloktijdronde), nooit op live. Idempotent.
G5  L-R9-4a  speelvolgorde G5-GET-E07: delen-cluster #3 → #9, keer-cluster #8 → #10 → #5; weergavenummers blijven (D-#408).
             bevroren/speelvolgorde.json + per item merge.speelVolgorde (positie in de speelvolgorde van het doel).
    L-R9-4b  naar-002, naar-026 (#10) en naar-008 (#9) naar basis (3 items omlaag, gelijktrekken binnen het cluster).
    JO       juisteOptie/juisteOptieTekst gelijk aan het antwoord (2 items).
G6  L-R10a   niveau uit het kenmerk (r13/niveaus.py) voor de 34 somtypes; kritisch-items blijven kritisch; None = niveau blijft.
    L-R10c   VERH-E02 #4 (balk) en #3 (taart): alleen basis.
    L-R10d   dunne somtypes met één niveau (niet in de 37): kenmerk van het grote somtype van hetzelfde doel, als dat op álle items leesbaar is.
    L-R10e   extraVelden.niveauVoorlopig vervalt bij de hm/dl-somtypes (MEET-E01 nrO 8–11, MEET-E04 nrO 5–8).
    L-R10f   GET-E03 #1/#5/#8 naar park-G7: NIET (wacht op Dave).
    V-#851/#852  GET-E08 data met gelijke som (gemiddelde-check-didactiek.md): opgave, optelling in claudeUitleg en claudeKaleSom.
    N13-1/2  bordtitels VBN-E02 en MEET-E05.
    JO       juisteOptie (16 items).
    V-#1001 (Didactiek 18:35) G5-MEET-E07 #1: één afleider → 'totaal min het kleinste euro-stuk' (114 items, r13/v1001_g5_e07.json, letterlijk uit signalen-buiten-g8-didactiek.md).
    V-#1002 G4-GET-E06 018/020/024: claudeKaleSom = de som uit de opgave (3 × 9, 5 × 7, 4 × 8); 018-sleutel 30 = 10 × 3 (tafelbuur) blijft.
    Oef-#1021 G5-MEET-E06 1211: ander typ-voorbeeld (9.45), want 14.30 is de route 'tien minuten te laat'.
    Rapport: r13_rapport.json is een logboek per ronde (aanvullen); elke ronde ook als r13_rapport_<ronde>.json (R13_RONDE=naam).
    V-#1010 G6-GET-M04 019–030: optiesTekst opnieuw uit opties[] (12); nooit 'de deler'/'het deeltal' als afleider bij een breuk (assert).
    V-#1011 G6-GET-E08 008/011/012: Claudes sleutel 'hoogste getal' bij de nieuwe rij (10 → 11, 7 → 8, 8 → 10).
    V-#1003 G7-MEET-02 001/002/003/029/031/032: claudeKaleSom en claudeUitleg bij de nieuwe maten (ook in g7/scripts/besluiten_g7.py, zodat een G7-build het houdt).
Daarna per groep scripts/apply_hints.py (fout-regels per item opnieuw, per_doel uit gemapt). Rapport: r13/r13_rapport.json."""
import json, os, re, sys, glob, collections, subprocess, copy
R13 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, R13)
import niveaus as NV, lijst as LJ
NK = {'basis': 'Opwarmen', 'toepassen': 'Oefenen', 'kritisch': 'Uitdaging'}
VOLGORDE_E07 = [1, 2, 3, 9, 4, 6, 7, 8, 10, 5, 11]
NAAR_BASIS_G5 = {'G5-GET-E07-claude-bank-naar-002', 'G5-GET-E07-claude-bank-naar-026', 'G5-GET-E07-claude-bank-naar-008'}
E08 = {'004': ([6, 6, 3, 3, 7], [6, 7, 2, 3, 7]), '005': ([8, 3, 9, 5, 5], [9, 2, 9, 5, 5]), '006': ([4, 6, 12, 6, 12], [5, 6, 11, 6, 12]),
       '007': ([6, 7, 2, 8, 2], [7, 7, 1, 8, 2]), '008': ([9, 8, 10, 10, 8], [8, 8, 11, 10, 8]),
       '010': ([5, 6, 6, 7], [3, 7, 7, 7]), '011': ([6, 3, 7, 4], [6, 3, 8, 3]), '012': ([6, 8, 6, 8], [6, 10, 6, 6])}
TITELS = {'G6-VBN-E02': 'Beelddiagram, cirkeldiagram en lijngrafiek aflezen', 'G6-MEET-E05': 'Kilogram en gram vergelijken en omrekenen'}
HMDL = {('G6-MEET-E01', n) for n in (8, 9, 10, 11)} | {('G6-MEET-E04', n) for n in (5, 6, 7, 8)}
PARK_G7 = {('G6-GET-E03', 1), ('G6-GET-E03', 5), ('G6-GET-E03', 8)}

def zet_niveau(it, nv, log, reden):
    if it['niveau'] == nv: return
    log.append({'id': it['id'], 'van': it['niveau'], 'naar': nv, 'kenmerk': reden}); it['niveau'] = nv; it['niveauKind'] = NK[nv]

def juiste_optie(it, log):
    ad = it.get('antwoordDetail')
    if it.get('type') != 'meerkeuze' or not isinstance(ad, dict) or not ad.get('juisteOptie'): return
    ops = {o.get('letter'): o.get('tekst') for o in it.get('opties') or []}; a = str(it['antwoord'])
    if ops.get(ad['juisteOptie']) == a and ad.get('juisteOptieTekst', a) == a: return
    lt = [l for l, t in ops.items() if t == a]
    if len(lt) != 1: log.append({'id': it['id'], 'fout': f'antwoord {a!r} staat {len(lt)}× in de opties, niet hersteld'}); return
    log.append({'id': it['id'], 'van': [ad.get('juisteOptie'), ad.get('juisteOptieTekst')], 'naar': [lt[0], a]})
    ad['juisteOptie'] = lt[0]
    if 'juisteOptieTekst' in ad: ad['juisteOptieTekst'] = a

def vervang_diep(x, oud, nieuw):
    if isinstance(x, str): return x.replace(oud, nieuw)
    if isinstance(x, list): return [vervang_diep(v, oud, nieuw) for v in x]
    if isinstance(x, dict): return {k: vervang_diep(v, oud, nieuw) for k, v in x.items()}
    return x
def opsom(v): return ', '.join(map(str, v[:-1])) + ' en ' + str(v[-1])

def e08(it, log):
    m = re.fullmatch(r'G6-GET-E08-claude-bank-(\d{3})', it['id'])
    if not m or m.group(1) not in E08: return
    oud, nieuw = E08[m.group(1)]
    if sum(oud) != sum(nieuw): raise SystemExit(f'E08 {m.group(1)}: som verandert')
    if opsom(nieuw) in it['opgave']: return
    if opsom(oud) not in it['opgave']: log.append({'id': it['id'], 'fout': 'oude getallen niet in de opgave'}); return
    for k in ('opgave', 'opgaveStappen', 'extraVelden', 'visual', 'context', 'antwoordDetail'):
        if k in it:
            it[k] = vervang_diep(it[k], opsom(oud), opsom(nieuw)); it[k] = vervang_diep(it[k], ' + '.join(map(str, oud)), ' + '.join(map(str, nieuw)))
    log.append({'id': it['id'], 'van': oud, 'naar': nieuw, 'som': sum(nieuw), 'antwoord': it['antwoord']})

V1001 = json.load(open(f'{R13}/v1001_g5_e07.json', encoding='utf-8'))['items']
TE_WEINIG = {'uitleg': 'Dat is te weinig. Leg het geld op volgorde van groot naar klein en tel het één voor één op.', 'uitlegSterker': 'Tel de rest er één voor één bij. Een euro is honderd cent.',
             'laag2': 'terugval hint2 (somtype)', 'regel': 'Claudes sleutel: geld-verkeerd-geteld', 'soort': 'te weinig geteld', 'bron': 'claude-taalfix'}
CLAUDE_TE_WEINIG = 'Leg de munten op volgorde van groot naar klein en tel ze één voor één op.'
def v1001(it, log):
    m = re.fullmatch(r'G5-MEET-E07-claude-bank-(\d{3})', it['id'])
    if not m or m.group(1) not in V1001: return
    r = V1001[m.group(1)]; ops = [o['tekst'] for o in it['opties']]
    if r['nieuw'] in ops and r['eruit'] not in ops: return      # al gedaan
    if ops != r['optiesNu'] or it['antwoord'] != r['antwoord']: raise SystemExit(f"V-#1001 {it['id']}: opties {ops} ≠ lijst {r['optiesNu']}")
    mu = (it.get('visual') or {}).get('jsRender', {}).get('munten') or []
    if round(float(r['nieuw'][1:].replace(',', '.')) * 100) != sum(mu) - min(x for x in mu if x >= 100): raise SystemExit(f"V-#1001 {it['id']}: nieuw ≠ totaal min kleinste euro-stuk")
    it['opties'] = [dict(o, tekst=r['nieuw']) if o['tekst'] == r['eruit'] else o for o in it['opties']]
    if it.get('optiesTekst'): it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    ex = it['extraVelden']
    ex['claudeDenkfouten'] = [d for d in ex.get('claudeDenkfouten') or [] if d.get('fout') != r['eruit']] + [{'fout': r['nieuw'], 'denkfout': 'geld-verkeerd-geteld'}]
    ex['claudeFoutHints'] = [f for f in ex.get('claudeFoutHints') or [] if f.get('fout') != r['eruit']] + [{'stap': None, 'fout': r['nieuw'], 'uitleg': CLAUDE_TE_WEINIG}]
    it['foutHints'] = [f for f in it.get('foutHints') or [] if f.get('fout') != r['eruit']] + [dict(TE_WEINIG, stap=None, fout=r['nieuw'])]
    log.append({'id': it['id'], 'eruit': f"{r['eruit']} ({r['eruitLabel']})", 'nieuw': r['nieuw']})
V1002 = {'G4-GET-E06-claude-bank-018': ('3 × 10', '3 × 9'), 'G4-GET-E06-claude-bank-020': ('5 × 10', '5 × 7'), 'G4-GET-E06-claude-bank-024': ('4 × 10', '4 × 8')}
V1003 = {'001': (7, 6), '002': (18, 5), '003': (14, 9), '029': (7, 10), '031': (9, 8), '032': (13, 6)}

def v1010(it, log):
    """V-#1010 (Didactiek r13, les 386): optiesTekst = de weergave van opties[] (GET-M04 019–030 spraken elkaar tegen); 'de deler'/'het deeltal' nooit als afleider bij een breuk"""
    if not it.get('opties'): return
    ops = it['opties']; a = str(it['antwoord'])
    if re.search(r'\bin \d+/\d+\?', it['opgave']) and any(o['tekst'] in ('de deler', 'het deeltal') and o['tekst'] != a for o in ops):
        raise SystemExit(f"V-#1010 {it['id']}: 'de deler'/'het deeltal' als afleider in opties[]")
    w = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in ops)
    if it.get('optiesTekst') != w and it['merge'].get('doel') == 'G6-GET-M04':
        log.append({'id': it['id'], 'van': it.get('optiesTekst'), 'naar': w}); it['optiesTekst'] = w
V1011 = {'008': ('10', '11'), '011': ('7', '8'), '012': ('8', '10')}      # V-#1011 (les 385): Claudes 'hoogste getal'-sleutel wees naar de oude rij
def v1011(it, log):
    m = re.fullmatch(r'G6-GET-E08-claude-bank-(\d{3})', it['id'] or '')
    if not m or m.group(1) not in V1011: return
    oud, nw = V1011[m.group(1)]; ex = it['extraVelden']
    getallen = [int(x) for x in re.findall(r'\d+', it['opgave'].split('Ze hadden er ')[1].split('.')[0])]
    assert max(getallen) == int(nw), (it['id'], getallen)
    n = 0
    for k in ('claudeDenkfouten', 'claudeFoutHints'):
        for d in ex.get(k) or []:
            if d.get('fout') == oud: d['fout'] = nw; n += 1
    if n: log.append({'id': it['id'], 'van': oud, 'naar': nw, 'velden': n})

OEF1021 = {'G5-MEET-E06-claude-bank-1211': ('(Typ als 14.30.)', '(Typ als 9.45.)')}      # Oef-#1021: het voorbeeld 14.30 = de route 'tien minuten te laat' (antwoord 14.20 uur)
def oef1021(it, log):
    """Oef-#1021 (Oefeningen 18:47, les 234-achtig): bij 1211 is de foutsleutel '14.30 uur' (route 'tien minuten te laat', 14.20 + 10 min; ook Claudes afleider) precies het
    voorbeeld «(Typ als 14.30.)»: wie het voorbeeld overtypt krijgt 'De minuten kloppen niet'. Alleen de Claude-afleider wisselen helpt niet: de motorroute maakt 14.30
    toch. Daarom een ander voorbeeld in de instructie (9.45), nagerekend tegen alle routes van het item (13:80, 13.20, 15.20, 14.30, 14.10) en het antwoord."""
    if it['id'] not in OEF1021: return
    oud, nw = OEF1021[it['id']]
    if oud in it['opgave']:
        it['opgave'] = it['opgave'].replace(oud, nw); log.append({'id': it['id'], 'van': oud, 'naar': nw})
# V-#1050–#1055 (Didactiek 8 okt 19:35, g8/signalen-buiten-g8-didactiek.md 'Vormcue 50% (19:17)', les 405): per somtype één afleider vervangen door een echte
# denkfout aan de andere kant van het goede antwoord (data letterlijk uit de tabel). Per item nagerekend (route-assert), ≠ antwoord, ≠ andere optie.
# Claude-sleutel: 'weg' = de oude sleutel vervalt, de motorregel kent de nieuwe waarde (V-#1051 'verschil van twee cellen', V-#1054 'maand dubbel');
# (label, tekst) = Claude-sleutel op de nieuwe waarde: V-#1050 'geld-verkeerd-geteld' (regel 'verkeerd geteld (tekst per item)' geeft Claudes tekst), V-#1052 'een-ernaast'
# met de nieuwe tekst (wint pas op gelijkenis als Oefeningen de tekst in de regel zet), V-#1053 'tiental-te-veel' en V-#1055 'keer-getal-uit-de-vraag' (Oef-#1027:
# eigen label, geen motorregel in de goedgekeurde G6-motor) → tot Oefeningen een regel schrijft de tekst van 'andere fout'.
V1052_T = {'011': 'Controleer of je bij plek 12 of bij plek 13 bent uitgekomen.', '019': 'Controleer of je 9 of 10 zakjes hebt geteld.', '024': 'Reken na bij welke ronde 105 punten horen. Dat is één ronde te veel.'}
V1050_T = 'Leg de munten op volgorde van groot naar klein en tel ze één voor één op.'      # bestaande Claude-tekst bij 'verkeerd geteld' (regel 'tekst per item'); Didactiek: klopt ook voor te veel
V1053_T = 'Dat is tien te veel. Tel de getallen nog eens op. Let goed op de tientallen: tel je het tiental dat je onthoudt maar één keer mee?'      # voorstel Didactiek; Oefeningen schrijft de regel 'fout = antwoord + 10'
V1055_T = 'Heb je het getal keer het aantal uit de vraag gedaan? Dat klopt alleen als het eerste aantal 1 is. Hoeveel keer zo groot is het aantal in de vraag als het aantal dat je al weet?'
def _munt(it): return min((it.get('visual') or {}).get('jsRender', {}).get('munten') or [0])
def _rij(it, ding): return next(r_['waarden'] for r_ in it['visual']['jsRender']['rijen'] if r_['naam'] == ding)
def _maanden(it): return [p_['waarde'] for p_ in it['visual']['jsRender']['punten']]
def _cent(t): return int(re.fullmatch(r'(\d+) cent', t).group(1))
def _getal(t): return int(re.sub(r'[^\d]', '', t))
VC105X = {}
for n_, (e_, nw_) in {'003': ('50 cent', '85 cent'), '004': ('40 cent', '60 cent'), '006': ('50 cent', '65 cent'), '007': ('70 cent', '80 cent'), '008': ('50 cent', '80 cent'), '009': ('10 cent', '25 cent'),
                      '010': ('50 cent', '90 cent'), '012': ('20 cent', '40 cent'), '014': ('50 cent', '75 cent'), '015': ('20 cent', '35 cent'), '018': ('50 cent', '90 cent')}.items():
    VC105X[f'G4-MEET-E07-claude-bank-{n_}'] = ('V-#1050', e_, nw_, lambda it, v: _cent(v) == _cent(it['antwoord']) + _munt(it), ('geld-verkeerd-geteld', V1050_T))      # munt dubbel geteld = antwoord + kleinste munt
for n_, (e_, nw_, ding) in {'280': ('760', '130', 'appels'), '282': ('620', '90', 'stiften'), '283': ('585', '125', 'vogels')}.items():
    VC105X[f'G5-VBN-E01-claude-bank-{n_}'] = ('V-#1051', e_, nw_, (lambda d: lambda it, v: int(v) < int(it['antwoord']) and any(a - b == int(v) for a in _rij(it, d) for b in _rij(it, d)))(ding), 'weg')      # verschil van twee cellen in de rij
for n_, (e_, nw_, stap) in {'011': ('33', '39', 3), '019': ('48', '60', 6), '024': ('95', '105', 5)}.items():
    VC105X[f'G5-VBN-E03-claude-bank-{n_}'] = ('V-#1052', e_, nw_, (lambda st: lambda it, v: int(v) == int(it['antwoord']) + st)(stap), ('een-ernaast', V1052_T[n_]))      # één stap te ver
for n_, (e_, nw_) in {'012': ('240 bezoekers', '260 bezoekers'), '014': ('200 bezoekers', '220 bezoekers'), '016': ('310 bezoekers', '330 bezoekers'), '018': ('160 bezoekers', '180 bezoekers')}.items():
    VC105X[f'G5-GET-E05-merge-gen-{n_}'] = ('V-#1053', e_, nw_, lambda it, v: _getal(v) == _getal(it['antwoord']) + 10, ('tiental-te-veel', V1053_T))      # tiental te veel
for n_, (e_, nw_) in {'121': ('55', '160'), '122': ('60', '300'), '123': ('60', '125'), '124': ('10', '85'), '125': ('100', '210')}.items():
    VC105X[f'G6-VBN-E02-claude-bank-{n_}'] = ('V-#1054', e_, nw_, lambda it, v: int(v) - int(it['antwoord']) in _maanden(it), 'weg')      # alle maanden samen plus één maand
for i_, (e_, nw_) in {'G6-VERH-E01-claude-bank-001': ('€6', '€30'), 'G6-VERH-E01-claude-bank-002': ('€4', '€24'), 'G6-VERH-E01-merge-gen-006': ('€10', '€30'), 'G6-VERH-E01-merge-gen-014': ('€3', '€90')}.items():
    VC105X[i_] = ('V-#1055', e_, nw_, lambda it, v: (lambda m: m and int(m.group(2)) * int(m.group(3)) == _getal(v))(re.search(r'(\d+) [^€]*?€(\d+)\..*?(?:bij|kosten) (\d+) ', it['opgave'])), ('keer-getal-uit-de-vraag', V1055_T))      # y1 × x2
def vormcue105x(it, log):
    if it['id'] not in VC105X: return
    vnr, eruit, nieuw, route, claude = VC105X[it['id']]; ops = [o['tekst'] for o in it['opties']]
    if nieuw in ops and eruit not in ops: return      # al gedaan (idempotent)
    if eruit not in ops or nieuw in ops or nieuw == it['antwoord']: raise SystemExit(f"{vnr} {it['id']}: opties {ops} passen niet bij {eruit} → {nieuw}")
    if not route(it, nieuw): raise SystemExit(f"{vnr} {it['id']}: {nieuw} is niet de route")
    it['opties'] = [dict(o, tekst=nieuw) if o['tekst'] == eruit else o for o in it['opties']]
    if it.get('optiesTekst'): it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    if isinstance(it.get('antwoordDetail'), dict) and it['antwoordDetail'].get('juisteOptie'):
        it['antwoordDetail']['juisteOptie'] = next(o['letter'] for o in it['opties'] if o['tekst'] == it['antwoord'])
    ex = it['extraVelden']
    ex['claudeDenkfouten'] = [d for d in ex.get('claudeDenkfouten') or [] if d.get('fout') != eruit]
    ex['claudeFoutHints'] = [f for f in ex.get('claudeFoutHints') or [] if f.get('fout') != eruit]
    it['foutHints'] = [f for f in it.get('foutHints') or [] if f.get('fout') != eruit]      # apply bouwt ze opnieuw
    if claude != 'weg':
        lab, tekst = claude
        ex['claudeDenkfouten'].append({'fout': nieuw, 'denkfout': lab}); ex['claudeFoutHints'].append({'stap': None, 'fout': nieuw, 'uitleg': tekst})
    log.append({'id': it['id'], 'punt': vnr, 'eruit': eruit, 'nieuw': nieuw, 'claudeSleutel': 'vervalt (motorregel)' if claude == 'weg' else claude[0]})
def rapport_opslaan(R, ronde):
    """r13_rapport.json is een logboek per ronde (aanvullen, niet overschrijven); elke ronde ook los als r13_rapport_<ronde>.json"""
    import datetime
    p = f'{R13}/r13_rapport.json'; oud = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    if 'rondes' not in oud: oud = {'uitleg': 'Logboek van r13_uitvoer.py, één entry per ronde (de tellingen zijn per ronde: wat die ronde veranderde; idempotent, dus 0 = stond al goed).', 'rondes': ([{'ronde': 'voor-logboek', 'R': oud}] if oud else [])}
    entry = {'ronde': ronde, 'tijd': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'R': R}
    oud['rondes'].append(entry)
    json.dump(oud, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    json.dump(entry, open(f'{R13}/r13_rapport_{ronde}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)

def laad(g): p = f'{R13}/g{g}/data/gemapt.json'; return p, json.load(open(p, encoding='utf-8'))
def schrijf(p, G): json.dump(G, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
def apply(g):
    r = subprocess.run([sys.executable, '-B', f'{R13}/g{g}/scripts/apply_hints.py'], capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    if r.returncode: raise SystemExit(f'G{g} apply_hints faalt:\n{r.stderr[-2000:]}')
    return r.stdout.strip().splitlines()[-4:]

def g5():
    p, G = laad(5); R = {'L-R9-4a': [], 'L-R9-4b': [], 'JO': [], 'V-#1001': [], 'Oef-#1021': [], 'V-#1050–#1055': []}
    for it in G['items']:
        m = it['merge']
        if m.get('status') != 'gemapt': continue
        if m['doel'] == 'G5-GET-E07':
            pos = VOLGORDE_E07.index(m['somtypeNr']) + 1
            if m.get('speelVolgorde') != pos: m['speelVolgorde'] = pos; R['L-R9-4a'].append(it['id'])
        if it['id'] in NAAR_BASIS_G5: zet_niveau(it, 'basis', R['L-R9-4b'], 'L-R9-4b: uitkomst/deeltal 2 cijfers, gelijk aan het cluster')
        v1001(it, R['V-#1001']); oef1021(it, R['Oef-#1021']); vormcue105x(it, R['V-#1050–#1055'])
        juiste_optie(it, R['JO'])
    schrijf(p, G)
    json.dump({'uitleg': 'L-R9-4a (Leerlijn-besluit A, 8 okt 14:40): speel- en progressievolgorde per doel, als lijst van weergavenummers (bevroren/somtype_weergave_nr.json). '
               'Geen hernummering (D-#408). Per item staat de positie in merge.speelVolgorde. Delen-cluster #3 → #9, keer-cluster #8 → #10 → #5.',
               'volgorde': {'G5-GET-E07': VOLGORDE_E07}}, open(f'{R13}/g5/bevroren/speelvolgorde.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    R['apply'] = apply(5); R['L-R9-4a'] = len(R['L-R9-4a']); return R

def g6():
    p, G = laad(6); R = {'L-R10a': [], 'L-R10a_geenKenmerk': collections.Counter(), 'L-R10c': [], 'L-R10d': [], 'L-R10d_niet': [], 'L-R10e': [], 'V-#851/#852': [], 'JO': [], 'V-#1010': [], 'V-#1011': [], 'V-#1050–#1055': [], 'fouten': []}
    vast = {(d, n) for d, n, _ in LJ.R13_34}; basis = {(d, n) for d, n, _ in LJ.R13_BASIS}
    groep = collections.defaultdict(list)
    for it in G['items']:
        if it['merge'].get('status') == 'gemapt': groep[(it['merge']['doel'], it['merge']['somtypeNrOrigineel'])].append(it)
    for key, its in groep.items():
        for it in its:
            e08(it, R['V-#851/#852']); juiste_optie(it, R['JO']); v1010(it, R['V-#1010']); v1011(it, R['V-#1011']); vormcue105x(it, R['V-#1050–#1055'])
            if key in vast and it['niveau'] != 'kritisch':
                try: nv, k = NV.classificeer(it, *key)
                except Exception as e: nv, k = None, f'niet te lezen ({type(e).__name__})'
                if nv: zet_niveau(it, nv, R['L-R10a'], k)
                else: R['L-R10a_geenKenmerk'][f'{key[0]} nrO {key[1]}: {k}'] += 1
            if key in basis and it['niveau'] != 'kritisch': zet_niveau(it, 'basis', R['L-R10c'], 'alleen basis (besluit B)')
            if key in HMDL and (it.get('extraVelden') or {}).get('niveauVoorlopig'):
                it['extraVelden']['niveauVoorlopig'] = False; R['L-R10e'].append(it['id'])
    # L-R10d: dunne somtypes met één niveau, niet in de 37 en niet in park-G7
    groot = {}
    for d, n, _ in LJ.R13_34:
        if d not in groot or len(groep[(d, n)]) > len(groep[groot[d]]): groot[d] = (d, n)
    for key, its in sorted(groep.items()):
        if key in vast or key in basis or key in PARK_G7 or key[0] == 'G6-GET-E08': continue
        if len({i['niveau'] for i in its}) != 1: continue
        if key[0] not in groot: R['L-R10d_niet'].append(f'{key[0]} nrO {key[1]} ({len(its)}): geen groot somtype met kenmerk in dit doel'); continue
        uit = []
        for it in its:
            try: uit.append(NV.classificeer(it, *groot[key[0]]))
            except Exception: uit.append((None, 'andere vorm'))
        if any(nv is None for nv, _ in uit) or any(it['niveau'] == 'kritisch' for it in its):
            R['L-R10d_niet'].append(f'{key[0]} nrO {key[1]} ({len(its)}): kenmerk van nrO {groot[key[0]][1]} niet op alle items te lezen'); continue
        for it, (nv, k) in zip(its, uit): zet_niveau(it, nv, R['L-R10d'], f'L-R10d via nrO {groot[key[0]][1]}: {k}')
    schrijf(p, G)
    R['apply'] = apply(6)
    for doel, t in TITELS.items():
        pd = f'{R13}/g6/data/per_doel/{doel}.json'; D = json.load(open(pd, encoding='utf-8'))
        if D.get('bordtitel') != t: R.setdefault('N13', []).append({'doel': doel, 'van': D.get('bordtitel'), 'naar': t}); D['bordtitel'] = t
        json.dump(D, open(pd, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    R['L-R10a_geenKenmerk'] = dict(R['L-R10a_geenKenmerk'])
    return R

def g4():
    p, G = laad(4); R = {'V-#1002': [], 'V-#1050–#1055': []}
    for it in G['items']:
        vormcue105x(it, R['V-#1050–#1055'])
        if it['id'] in V1002:
            oud, nw = V1002[it['id']]; ex = it['extraVelden']
            if ex.get('claudeKaleSom') == oud: ex['claudeKaleSom'] = nw; R['V-#1002'].append({'id': it['id'], 'van': oud, 'naar': nw})
            elif ex.get('claudeKaleSom') != nw: raise SystemExit(f"V-#1002 {it['id']}: kale som {ex.get('claudeKaleSom')!r}")
            if it['id'].endswith('-018'):      # sleutel 30 = 10 × 3: één stap hoger in de tafel van 3 (route 'tafelbuur'), blijft
                assert any(d.get('fout') == '30' and d.get('denkfout') == 'tafelbuur' for d in ex.get('claudeDenkfouten') or [])
                R['018-sleutel-30'] = 'blijft: route tafelbuur (10 × 3, een stap hoger in de tafel van 3)'
    schrijf(p, G); R['apply'] = apply(4); return R

def g7():
    p, G = laad(7); R = {'V-#1003': []}
    for it in G['items']:
        m = re.fullmatch(r'G7-MEET-02-claude-bank-(\d{3})', it['id'])
        if not m or m.group(1) not in V1003: continue
        b, h = V1003[m.group(1)]
        if not re.search(rf'basis van {b} m en een hoogte van {h} m\b', it['opgave']): raise SystemExit(f"V-#1003 {it['id']}: maten passen niet: {it['opgave']}")
        a = b * h // 2 if b * h % 2 == 0 else None
        assert a is not None and it['antwoord'] == str(a), it['id']
        ex = it['extraVelden']; nks = f'{b} × {h} : 2'; nu = f'Oppervlakte driehoek = basis × hoogte : 2 = {b} × {h} : 2 = {b * h} : 2 = {a} m².'
        if (ex.get('claudeKaleSom'), ex.get('claudeUitleg')) != (nks, nu):
            R['V-#1003'].append({'id': it['id'], 'van': [ex.get('claudeKaleSom'), ex.get('claudeUitleg')], 'naar': [nks, nu]}); ex['claudeKaleSom'] = nks; ex['claudeUitleg'] = nu
    schrijf(p, G); R['apply'] = apply(7); return R

def spreiding():
    G = json.load(open(f'{R13}/g6/data/gemapt.json'))['items']; c = collections.defaultdict(collections.Counter)
    for it in G:
        if it['merge'].get('status') == 'gemapt': c[(it['merge']['doel'], it['merge']['somtypeNrOrigineel'])][it['niveau']] += 1
    uit = []
    for d, n, w in LJ.R13_34:
        k = c[(d, n)]; tot = sum(k.values())
        uit.append({'somtype': f'{d} #{w} (nrO {n})', 'b': k['basis'], 't': k['toepassen'], 'k': k['kritisch'], 'n': tot,
                    'tekort': [nv for nv in ('basis', 'toepassen', 'kritisch') if k[nv] < 3], 'boven60': [nv for nv in k if k[nv] > 0.6 * tot]})
    return uit

if __name__ == '__main__':
    R = {'G4': g4(), 'G5': g5(), 'G6': g6(), 'G7': g7()}; R['G6']['spreiding'] = spreiding()
    rapport_opslaan(R, os.environ.get('R13_RONDE') or __import__('datetime').datetime.now().strftime('%H%M%S'))
    for g in ('G4', 'G5', 'G6', 'G7'):
        print(g, {k: (len(v) if isinstance(v, list) else v) for k, v in R[g].items() if k not in ('spreiding',)})
