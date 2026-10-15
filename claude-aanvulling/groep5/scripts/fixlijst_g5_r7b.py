"""G5 ronde 7b (Overzicht, 1 okt 23:30; Oefeningen G5 batch 7 twijfel 3 en 6, #329). Alleen in het geheugen: de hint-batches blijven zoals Oefeningen ze schreef.
- GET-E09: motorregels in plaats van Claudes labels ('wat het kost', 'één ding betaald', 'tweede stap vergeten'); de tekst blijft die van het label.
- GET-E05 #32: 'fout = antwoord − 10' en 'fout = een getal uit de vraag' (de motor leest nu ook een antwoord met eenheid, '230 bezoekers').
- #329: E05 #32 'In een tabel staat …' zonder tabel → opgave zonder tabel (ná het somtype, dus dezelfde hint-entry)."""
import re
LOG = []
DOOR = 'Overzicht (G5 ronde 7b, 1 okt 23:30)'
# (doel, nrOrigineel, Claude-regel) → motorregel (komt vóór de Claude-regel, met dezelfde tekst en laag 2)
MOTOR = {('G5-GET-E09', 1, 'Claudes sleutel: deel-vergeten-bij-splitsen'): 'fout = wat het kost (aantal × prijs)',
         ('G5-GET-E09', 1, 'Claudes sleutel: verkeerde-bewerking'): 'fout = één ding betaald (betaald − prijs)',
         ('G5-GET-E09', 2, 'Claudes sleutel: deel-vergeten-bij-splitsen'): 'fout = tweede stap vergeten (getal1 × getal2)',
         ('G5-GET-E05', 32, 'Claudes sleutel: tiental-ernaast'): 'fout = antwoord − 10',
         ('G5-GET-E05', 32, 'Claudes sleutel: getal-overgenomen'): 'fout = een getal uit de vraag'}
def pas_entries(entries):
    for st in entries:
        fh = st.get('foutHints') or []; uit = []
        for f in fh:
            m = MOTOR.get((st['doel'], st.get('nrOrigineel'), f['regel']))
            if m and not any(g['regel'] == m for g in fh):
                uit.append(dict(f, regel=m, bron='nieuw', door=DOOR, vervangtLabel=f['regel']))
                LOG.append({'entry': f"{st['doel']} #{st.get('nrOrigineel')}", 'motorregel': m, 'voor': f['regel']})
            uit.append(f)
        st['foutHints'] = uit
TABEL329 = re.compile(r'^In een tabel staat het aantal bezoekers van (.+?): ')
def fix329(rows):
    n = 0
    for it in rows:
        if it['merge'].get('doel') == 'G5-GET-E05' and TABEL329.match(it['opgave'] or '') and not (it['visual'].get('jsRender') or it['visual'].get('nodig')):
            o = it['opgave']; it['opgave'] = TABEL329.sub(r'Dit zijn de bezoekers van \1: ', o)
            it['merge']['opgave329'] = {'oud': o, 'waarom': "G5 #329: 'In een tabel staat' zonder tabel"}; n += 1
    for it in rows:
        assert not (it['merge'].get('doel') == 'G5-GET-E05' and 'In een tabel staat' in (it['opgave'] or '') and not it['visual'].get('jsRender')), ('#329', it['id'])
    return n


# ───────────── G5 ronde 9 (8 okt; Didactiek recheck r7b 1 okt 23:41, besluit Dave 23:41): #300 #301 #302 #321/#354 #322 #323 #324 #325 #326 #327 #235 ─────────────
# Alles in het geheugen, in de build (na AV8.laad en fix329). De hint-batches blijven zoals Oefeningen ze schreef; de sleutels gaan via de Claude-velden
# (claudeFoutHints/claudeDenkfouten) en de motorregels van de entries. guards_r7b draait vlak voor het schrijven en geeft FAIL (AssertionError).
import copy as _copy
from collections import defaultdict as _dd
LOG7B = _dd(list)
PRE = 'G5-GET-'
def _id(d, nr): return f'{PRE}{d}-claude-bank-naar-{nr}'
_NUM = lambda v: re.compile(r'(?<![\d,.])' + re.escape(str(v)) + r'(?![\d])')

def _opties_tekst(it):
    it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    if it.get('antwoordDetail'):
        goed = [o for o in it['opties'] if o['tekst'] == it['antwoord']]
        assert len(goed) == 1, ('MC: antwoord niet precies één keer in de opties', it['id'])
        it['antwoordDetail'] = dict(it['antwoordDetail'], juisteOptie=goed[0]['letter'], juisteOptieTekst=it['antwoord'])

def _vervang_waarden(it, kaart, weg=()):
    """Zet sleutelwaarden om (oud → nieuw) in de Claude-velden, foutHints en opties; 'weg': sleutels die niet meer kloppen."""
    ev = it['extraVelden']
    def s(x):
        if not isinstance(x, str): return x
        for o, n in kaart.items(): x = x.replace(str(o), str(n)) if str(o).startswith('€') else _NUM(o).sub(str(n), x)
        return x
    it['foutHints'] = [dict(f, fout=s(f['fout']), uitleg=s(f.get('uitleg'))) for f in it.get('foutHints') or [] if f['fout'] not in weg]
    for k in ('claudeDenkfouten', 'claudeFoutHints', 'mergeFoutHints'):
        if ev.get(k): ev[k] = [dict(f, fout=s(f['fout']), **({'uitleg': s(f.get('uitleg'))} if 'uitleg' in f else {})) for f in ev[k] if f['fout'] not in weg]
    if it.get('opties'):
        for o in it['opties']: o['tekst'] = s(o['tekst'])
        _opties_tekst(it)

def _claude(it, sleutels):
    """sleutels: [(waarde, label|None, uitleg)] → claudeFoutHints/claudeDenkfouten (label None = 'Claudes sleutel (zonder label)')."""
    ev = it['extraVelden']; sl = [(str(v), lab, u) for v, lab, u in sleutels]
    assert len({v for v, _, _ in sl}) == len(sl) and str(it['antwoord']) not in {v for v, _, _ in sl}, ('sleutels dubbel of = antwoord', it['id'], sl)
    ev['claudeFoutHints'] = [{'stap': None, 'fout': v, 'uitleg': u} for v, _, u in sl]
    ev['claudeDenkfouten'] = [{'fout': v, 'denkfout': lab} for v, lab, _ in sl if lab]
    ev['mergeFoutHints'] = []
    it['foutHints'] = [{'stap': None, 'fout': v, 'uitleg': u} for v, _, u in sl]

# #302: opties > 1000 → een kleiner getal met dezelfde denkfout (orde van grootte: het antwoord : 10)
OPT302 = {('E05', '066'): ('6970', '70'), ('E05', '058'): ('4830', '48'), ('E05', '067'): ('8830', '88'), ('E05', '072'): ('2630', '26'),
          ('E05', '074'): ('1062', '6'), ('E05', '077'): ('3350', '33'), ('E05', '076'): ('4070', '40'),
          ('E07', '031'): ('8050', '80'), ('E07', '036'): ('7350', '73'), ('E07', '038'): ('3450', '34'), ('E07', '053'): ('7860', '78')}
SCHAT = re.compile(r'^Hoeveel is (\d+) ([+−×]) (\d+) ongeveer\? Rond beide getallen af op (tientallen|honderdtallen) en reken dan uit\.$')
def _rond(x, s): return (x + s // 2) // s * s
def _reken(a, op, b): return a + b if op == '+' else a - b if op == '−' else a * b
def _schat(a, op, b, s): return _reken(_rond(a, s), op, _rond(b, s))
# #301 (afronden op de andere plaats geeft hetzelfde), #322 (verborgen sleutel boven 1000), #326 (geen term die al rond is). (oud) → (nieuw)
# Elk nieuw paar houdt de eigenschap van het somtype (met/zonder overschrijding van het tiental); de build controleert dat de kop gelijk blijft.
SCHAT301 = {('E05', '022'): ((20, 81), (34, 52), '#301/#326'), ('E05', '034'): ((887, 194), (887, 246), '#301'), ('E05', '001'): ((131, 370), (131, 362), '#301'),
            ('E05', '019'): ((28, 74), (38, 76), '#301'), ('E05', '027'): ((40, 84), (43, 84), '#326'), ('E05', '015'): ((20, 85), (62, 85), '#326'),
            ('E05', '018'): ((80, 78), (83, 76), '#326'), ('E05', '020'): ((60, 75), (63, 75), '#326'), ('E05', '030'): ((40, 76), (47, 71), '#326'),
            ('E05', '010'): ((110, 880), (113, 780), '#322'), ('E05', '008'): ((194, 776), (194, 667), '#322'),
            ('E07', '021'): ((20, 48), (23, 48), '#326'), ('E07', '022'): ((30, 19), (31, 19), '#326')}
def _anders(a, op, b, s):
    """'anders afgerond': bij + en − afronden op de andere plaats; bij × één getal de verkeerde kant op (het kleinste getal naar beneden, het grootste naar beneden)."""
    if op != '×': return _schat(a, op, b, 100 if s == 10 else 10)
    return _rond(a, 10) * (b // 10 * 10) if _rond(b, 10) != b // 10 * 10 else (a // 10 * 10) * _rond(b, 10)
def _schat_item(it, a, op, b, s):
    plek = 'tientallen' if s == 10 else 'honderdtallen'; ans = _schat(a, op, b, s); ex = _reken(a, op, b); an = _anders(a, op, b, s)
    it['opgave'] = f'Hoeveel is {a} {op} {b} ongeveer? Rond beide getallen af op {plek} en reken dan uit.'; it['antwoord'] = str(ans)
    ev = it['extraVelden']; ev['claudeKaleSom'] = f'Hoeveel is {a} {op} {b} ongeveer?'
    ev['claudeUitleg'] = f'{a} wordt {_rond(a, s)} en {b} wordt {_rond(b, s)}.\n{_rond(a, s)} {op} {_rond(b, s)} = {ans}.'
    sl = [(ex, None, f'{ex} is het precieze antwoord. De vraag is hoeveel het ongeveer is. Rond eerst af op {plek}.')]
    if an not in (ans, ex, ans + s, ans - s) and 0 <= an <= (1000 if op != '×' else 10000):
        sl.append((an, None, f'Rond af op {plek}, zoals de vraag zegt. Reken daarna uit met de ronde getallen.'))
    _claude(it, sl); return ans, ex, an
TEKST324 = {('E05', '045'): ('Op het schoolplein staan 928 kinderen. Er gaan er 195 naar binnen. Hoeveel kinderen staan er nog buiten?',
                             'Op het sportfeest zijn 928 kinderen. Er gaan er 195 naar huis. Hoeveel kinderen zijn er nog op het sportfeest?'),
            ('E05', '048'): ('In de bibliotheek staan 125 boeken.', 'In de klassenbibliotheek staan 125 boeken.'),
            ('E07', '057'): ('vissen', 'knikkers'), ('E07', '056'): ('8 kratten met elk 19 appels', '8 zakken met elk 19 appels')}
# #325: E09 #2 'opgeteld' (a + b − k) = een getal uit de vraag → k één kleiner
TWEESTAP325 = {('E09', '002'): ('Ze raken er samen 6 kwijt.', 'Ze raken er samen 5 kwijt.', 6, 8, 5), ('E09', '016'): ('Er worden er 5 gebruikt.', 'Er worden er 3 gebruikt.', 6, 5, 3)}      # ronde 10 #371: 3 (niet 4): 'stappen door elkaar' 6 × (5 − 4) = 6 was een getal uit de vraag
TWEESTAP = re.compile(r'(\d+)\D+?(\d+)\D+?(\d+)')
def _tweestap_sleutels(a, b, k):
    sl = {'deel-vergeten-bij-splitsen': a * b, 'optellen-ipv-vermenigvuldigen': a + b - k}
    if b > k and a * (b - k) not in (a * b - k,): sl['verkeerde-bewerking'] = a * (b - k)
    return sl
TWEESTAP_UITLEG = {'deel-vergeten-bij-splitsen': 'Dat is hoeveel het er samen zijn. Er gaan er nog een paar weg.',
                   'verkeerde-bewerking': 'Reken eerst uit hoeveel het er samen zijn. Haal er daarna af wat weggaat.',
                   'optellen-ipv-vermenigvuldigen': 'Het is steeds evenveel: dat is een keersom.'}
WISSEL = re.compile(r'^(\w+) koopt (\d+) (.+?) van €(\d+) per stuk en betaalt met €(\d+)\. Hoeveel geld krijgt (hij|ze) terug\?$')
BILJET = (10, 20, 50, 100)
EURO_ACC = "met en zonder €, met spaties, met en zonder ',00'; komma, geen punt"
def _wissel_sleutels(n, p, B): return {'ans': B - n * p, 'kost': n * p, 'een': B - p, 'opgeteld': B - (n + p)}
def _wissel_ok(n, p, B):
    w = _wissel_sleutels(n, p, B); v = list(w.values())
    return w['ans'] > 0 and min(v) > 0 and len(set(v)) == len(v)
WISSEL_LAB = {'deel-vergeten-bij-splitsen': 'kost', 'verkeerde-bewerking': 'een', 'optellen-ipv-vermenigvuldigen': 'opgeteld'}
WISSEL_UITLEG = {'kost': 'Dat is wat alles samen kost. Haal het van het geld waarmee je betaalt.', 'een': 'Je hebt de prijs van één ding eraf gehaald.',
                 'opgeteld': 'Je hebt het aantal en de prijs opgeteld. Elk ding kost evenveel: dat is een keersom.'}

def _som327(it):
    o = it['opgave'] or ''
    m = re.search(r'bij (\d+) ([+−]) (\d+) kan kloppen', o) or re.match(r'^(\d+) ([+−]) (\d+)$', it['extraVelden'].get('claudeKaleSom') or '')
    return (int(m[1]), m[2], int(m[3])) if m else None
def niveau327(a, op, b):
    """Didactiek #327: toepassen bij een getal van drie cijfers of bij onthouden/lenen in een kolom; anders basis."""
    if max(a, b) >= 100: return 'toepassen'
    if op == '+': brug = a % 10 + b % 10 >= 10 or a // 10 % 10 + b // 10 % 10 + (a % 10 + b % 10 >= 10) >= 10
    else: brug = a % 10 < b % 10
    return 'toepassen' if brug else 'basis'

# ─── #235: dunne somtypen aanvullen tot ≥ 8 items (generator, vorm naar het sjabloon van een item van hetzelfde somtype) ───
GEN30 = [(642, 287), (813, 456), (924, 268), (731, 495), (560, 184)]                 # E05 nrO 30: kan kloppen, − met overschrijding
GEN31 = [(734, 268), (582, 247), (913, 386), (461, 135), (825, 459), (670, 314)]     # E05 nrO 31: schatten −, honderdtallen, met overschrijding
GEN32 = [   # ronde 10 #363 (Didactiek gate r9): gen-015/016 met getallen onder 100 per dag, zoals het sjabloon 053
         ('het zwembad', (64, 57, 83, 46)), ('de speeltuin', (38, 75, 69, 47)), ('de bibliotheek', (56, 49, 67, 38)), ('het museum', (48, 63, 57, 39)),
         ('de dierentuin', (86, 74, 92, 68)), ('de ijsbaan', (87, 65, 78, 59)), ('de sporthal', (47, 36, 58, 29))]
GEN22 = [(3, 'dozen', 297, 'kralen'), (2, 'dozen', 412, 'spijkers'), (4, 'dozen', 189, 'snoepjes'), (5, 'dozen', 104, 'potloden'),      # altijd dozen: de vaste tekst
         (2, 'dozen', 396, 'stickers'), (3, 'dozen', 213, 'knopen'), (4, 'dozen', 208, 'servetten')]      # ronde 10 #370: 248 → 208 (schatting 800 ligt dichtbij 832)                                 # zegt 'In elke doos …'
GEN2 = [('4 kinderen hebben elk 9 kaartjes. Ze geven er samen 6 weg. Hoeveel kaartjes hebben ze nog?', 4, 9, 6),
        ('5 kinderen plukken elk 8 appels. Ze eten er samen 6 op. Hoeveel appels hebben ze nog?', 5, 8, 6),
        ('In de gymzaal liggen 7 netten met elk 6 ballen. Er gaan er 9 lek. Hoeveel ballen zijn er nog heel?', 7, 6, 9)]
WEEK = ('maandag', 'dinsdag', 'woensdag', 'donderdag')

def _gen_item(sjab, nr, cid, opgave, antwoord, niveau=None):
    it = _copy.deepcopy(sjab); d = it['merge']['doel']
    it['id'] = f'{d}-merge-gen-{nr:03d}'; it['nr'] = f'{nr:03d}'; it['opgave'] = opgave; it['antwoord'] = antwoord
    if 'geldigeAntwoorden' in it: it['geldigeAntwoorden'] = []      # ronde 10 #360: niet van het sjabloon; fixlijst_g5_r10.geldig360 leidt de lijst af uit het antwoord
    if niveau: it['niveau'] = niveau; it['niveauKind'] = 'Oefenen' if niveau == 'toepassen' else it['niveauKind']
    it['bronVariant'] = f'merge-generator:G5-r9-#235:{cid}'
    it['bron'] = {'bestand': 'scripts/fixlijst_g5_r7b.py', 'type': 'merge-generator', 'claudeId': cid, 'claudeDoel': 'merge-generator G5 ronde 9 (#235)',
                  'claudeDoelTitel': 'geen Claude-item', 'claudeGroep': None, 'claudeBron': None, 'claudeVersie': None,
                  'generator': 'G5-r9 #235 (dunne somtypen aanvullen, Didactiek recheck r7b)', 'sjabloonClaudeId': sjab['bron'].get('claudeId'), 'sjabloonId': sjab['id']}
    it['licentie'] = dict(it['licentie'], gewijzigd=True, wijzigingen=[f"G5-r9 #235 generator (vorm naar het sjabloon {sjab['id']})"])
    it['merge'] = {k: v for k, v in it['merge'].items() if k in ('status', 'doel', 'voorstelDoel', 'somtype', 'duplicaatVan')}
    it['merge'].update(regel='G5-r9 #235 generator', reden=f"#235: dun somtype aangevuld (sjabloon {sjab['id']})", gen235={'sjabloon': sjab['id']})
    it['controle'] = dict(it['controle'], antwoord='ok', verwacht=antwoord, methode='G5-r9 #235 generator (nagerekend in fixlijst_g5_r7b.py)',
                          claudeVorm={'antwoord': None, 'verwacht': None, 'methode': 'geen Claude-item'}, foutAntwoordGelijkAanGoed=False)
    it.get('extraVelden', {}).update(claudeStrategie=None, claudeThema=None, niveauVoorlopig=True)
    return it

def _mc(it, opties):
    """opties in vaste volgorde (de app husselt); A, B, C."""
    it['opties'] = [{'letter': 'ABCD'[i], 'tekst': t} for i, t in enumerate(opties)]; _opties_tekst(it)

def kop_nro(rows, doel, nro):
    """De huidige kop van somtype (doel, nrOrigineel): via de claudeIds van de bevroren indeling (bevroren/somtype_nr_v*.json), zoals sync_hint_keys."""
    import glob, os, json, collections
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in sorted(glob.glob(f'{base}/bevroren/somtype_nr_v*.json')):
        e = json.load(open(p))['sleutels'].get(f'{doel}#{nro}')
        if e:
            ids = set(e['claudeIds']); c = collections.Counter(r['merge']['somtype'] for r in rows if r['bron'].get('claudeId') in ids and r['merge'].get('doel') == doel)
            assert len(c) == 1, ('kop_nro', doel, nro, dict(c)); return next(iter(c))
    raise AssertionError(('kop_nro: geen bevroren somtype', doel, nro))

def generator_235(rows, kop):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    sj = lambda d, s: min((r for r in G if r['merge']['doel'] == d and r['merge']['somtype'] == s), key=lambda r: r['id'])
    kop_van = lambda d, nrO: kop_nro(rows, d, nrO)
    uit = []; teller = _dd(int)
    def nieuw(sjab, cid, opgave, antwoord, niveau=None):
        d = sjab['merge']['doel']; teller[d] += 1; it = _gen_item(sjab, teller[d], cid, opgave, antwoord, niveau); uit.append(it); return it
    # E05 nrO 30: kan kloppen (−, met overschrijding): goed, buiten de grens (boven- of ondergrens), ander laatste cijfer
    s30 = sj('G5-GET-E05', kop_van('G5-GET-E05', 30))
    for i, (a, b) in enumerate(GEN30, 1):
        ans = a - b; bov = _rond(a + 50, 100) - b // 100 * 100; ond = a // 100 * 100 - _rond(b + 50, 100)
        if ans + 100 > bov: grens, gl = ans + 100, 'bovengrens'
        else: assert ans - 100 < ond and ans >= 100, ('#235 E05 30', a, b); grens, gl = ans - 100, 'ondergrens'
        lc = ans + 2 if i % 2 else ans - 2
        it = nieuw(s30, f'g5-r9-gen235-e05-30-{i:02d}', f'Kijk zonder uit te rekenen. Welk antwoord bij {a} − {b} kan kloppen?', str(ans), 'toepassen')
        it['extraVelden']['claudeKaleSom'] = it['opgave']; it['extraVelden']['claudeUitleg'] = None
        _claude(it, [(grens, gl, f'Rond af en reken uit. {grens} kan niet kloppen.'), (lc, 'laatste-cijfer', f'Kijk naar de laatste cijfers: {a % 10} − {b % 10}. Op welk cijfer moet de uitkomst eindigen?')])
        _mc(it, [str(ans), str(grens), str(lc)] if i % 2 else [str(lc), str(ans), str(grens)])
    # E05 nrO 31: schatten −, honderdtallen, met overschrijding
    s31 = sj('G5-GET-E05', kop_van('G5-GET-E05', 31))
    for i, (a, b) in enumerate(GEN31, 1):
        it = nieuw(s31, f'g5-r9-gen235-e05-31-{i:02d}', '', '')
        _schat_item(it, a, '−', b, 100)
    # E05 nrO 32: bezoekers van vier dagen samen (opgave zonder tabel, #329)
    s32 = sj('G5-GET-E05', kop_van('G5-GET-E05', 32))
    for i, (plek, w) in enumerate(GEN32, 1):
        ans = sum(w); dag = max(w)
        o = f"Dit zijn de bezoekers van {plek}: {', '.join(f'{d} {x}' for d, x in zip(WEEK[:3], w[:3]))} en {WEEK[3]} {w[3]}. Hoeveel bezoekers waren er in die vier dagen samen?"
        it = nieuw(s32, f'g5-r9-gen235-e05-32-{i:02d}', o, f'{ans} bezoekers', 'toepassen')
        ev = it['extraVelden']; ev['claudeKaleSom'] = ' + '.join(map(str, w)); ev['claudeUitleg'] = f"{' + '.join(map(str, w))} = {ans}."
        _claude(it, [(f'{ans - 10} bezoekers', 'tiental-ernaast', 'Dat is tien te weinig. Let goed op de tientallen.'), (f'{dag} bezoekers', 'getal-overgenomen', 'Dat is het getal van één dag.')])
        _mc(it, [[f'{ans - 10} bezoekers', f'{dag} bezoekers', f'{ans} bezoekers'], [f'{ans} bezoekers', f'{ans - 10} bezoekers', f'{dag} bezoekers'], [f'{dag} bezoekers', f'{ans} bezoekers', f'{ans - 10} bezoekers']][i % 3])
        it['merge'].pop('opgave329', None)
        it['merge']['gen235']['kop'] = "vast: het somtype van het sjabloon (de kop wordt berekend vóór #329 'Dit zijn de bezoekers'; [plek] kent alleen de plekken uit Claude)"
    # E07 nrO 22: n bakken met elk x dingen, rond x af op honderdtallen
    s22 = sj('G5-GET-E07', kop_van('G5-GET-E07', 22))
    for i, (n, bak, x, ding) in enumerate(GEN22, 1):
        r = _rond(x, 100); ans = n * r; ex = n * x; opg = n + r
        assert opg not in (n, x, ans, ex, ans // 10) and ex <= 1000 and ans <= 1000, ('#235 E07 22', n, x)
        assert abs(ans - ex) / ex < 0.10, ('#370: de schatting ligt niet dichtbij (≥ 10 %)', n, x, ans, ex)
        it = nieuw(s22, f'g5-r9-gen235-e07-22-{i:02d}', f'{n} {bak} met elk {x} {ding}. Schat hoeveel dat ongeveer is: rond {x} af op honderdtallen en reken dan uit.', str(ans))
        ev = it['extraVelden']; ev['claudeKaleSom'] = f'{x} × {n} ≈ {r} × {n}'; ev['claudeUitleg'] = f'{x} is ongeveer {r}.\n{n} × {r} = {ans}.'      # #374: met de ≈-stap, zoals het sjabloon
        _claude(it, [(ex, 'verkeerde-bewerking', f'{ex} is precies uitgerekend. Rond eerst af.'), (ans // 10, 'nul-fout-tientallen', 'Tel de nullen goed mee.'),
                     (opg, 'optellen-ipv-vermenigvuldigen', 'Je hebt opgeteld. In elke doos zitten er evenveel: dat is een keersom.')])
    # E09 nrO 2: twee stappen, eerst een keersom en dan eraf
    s2 = sj('G5-GET-E09', kop_van('G5-GET-E09', 2))
    for i, (o, a, b, k) in enumerate(GEN2, 1):
        ans = a * b - k; sl = _tweestap_sleutels(a, b, k)
        assert sl['optellen-ipv-vermenigvuldigen'] not in (a, b, k) and sl['optellen-ipv-vermenigvuldigen'] > 0, ('#235/#325 E09 2', o)
        it = nieuw(s2, f'g5-r9-gen235-e09-02-{i:02d}', o, str(ans), 'toepassen')
        ev = it['extraVelden']; ev['claudeKaleSom'] = f'{a} × {b} − {k}'; ev['claudeUitleg'] = f'Stap 1: {a} × {b} = {a * b}.\nStap 2: {a * b} − {k} = {ans}.'
        _claude(it, [(v, lab, TWEESTAP_UITLEG[lab]) for lab, v in sl.items()])
        it['merge']['gen235']['kop'] = 'vast: het somtype van het sjabloon (een vaste kop per somtype, niet uit de opgave te berekenen)'
    for it in uit:
        assert 'kop' in it['merge']['gen235'] or kop(it) == it['merge']['somtype'], ('#235: kop van het gegenereerde item ≠ somtype van het sjabloon', it['id'], kop(it), it['merge']['somtype'])
        LOG7B['235'].append((it['id'], it['merge']['doel'], it['opgave'], it['antwoord']))
    return uit

def fix_r7b(rows, kop):
    """kop(it): somtype opnieuw berekenen; na elke getalwijziging moet de kop gelijk blijven (zelfde hint-entry)."""
    idx = {it['id']: it for it in rows}
    # #302
    for (d, nr), (o, n) in OPT302.items():
        it = idx[_id(d, nr)]; assert any(x['tekst'] == o for x in it['opties']) and not any(x['tekst'] == n for x in it['opties']), ('#302', it['id'])
        _vervang_waarden(it, {o: n}); it['merge']['r7b302'] = {'oud': o, 'nieuw': n}; LOG7B['302'].append((it['id'], o, n))
    # #301 / #322 / #326: schatten met andere getallen
    for (d, nr), ((a0, b0), (a1, b1), pt) in SCHAT301.items():
        it = idx[_id(d, nr)]; m = SCHAT.match(it['opgave']); assert m and (int(m[1]), int(m[3])) == (a0, b0), ('#301', it['id'], it['opgave'])
        k0 = kop(it); oud = it['antwoord']; s = 10 if m[4] == 'tientallen' else 100
        ans, ex, an = _schat_item(it, a1, m[2], b1, s)
        assert kop(it) == k0 == it['merge']['somtype'], ('#301: het somtype verandert door de nieuwe getallen', it['id'], k0, kop(it))
        it['merge']['r7b301'] = {'punt': pt, 'oud': f'{a0} {m[2]} {b0} ≈ {oud}', 'nieuw': f'{a1} {m[2]} {b1} ≈ {ans}', 'precies': ex, 'andersAfgerond': an}
        LOG7B['301'].append((it['id'], pt, f'{a0} {m[2]} {b0} → {a1} {m[2]} {b1}', oud, str(ans)))
    # #324
    for (d, nr), (o, n) in TEKST324.items():
        it = idx[_id(d, nr)]; assert o in it['opgave'], ('#324', it['id'])
        f = lambda x: x.replace(o, n) if isinstance(x, str) else x
        it['opgave'] = f(it['opgave']); ev = it['extraVelden']
        for k in ('claudeKaleSom', 'claudeUitleg'): ev[k] = f(ev.get(k))
        it['merge']['r7b324'] = {'oud': o, 'nieuw': n}; LOG7B['324'].append((it['id'], o, n))
    # #325
    for (d, nr), (o, n, a, b, k) in TWEESTAP325.items():
        it = idx[_id(d, nr)]; assert o in it['opgave'] and it['antwoord'] == str(a * b - int(re.search(r'\d+', o)[0])), ('#325', it['id'])
        k0 = kop(it); oud = it['antwoord']; ans = a * b - k
        it['opgave'] = it['opgave'].replace(o, n); it['antwoord'] = str(ans); ev = it['extraVelden']
        ev['claudeKaleSom'] = f'{a} × {b} − {k}'; ev['claudeUitleg'] = f'Stap 1: {a} × {b} = {a * b}.\nStap 2: {a * b} − {k} = {ans}.'
        _claude(it, [(v, lab, TWEESTAP_UITLEG[lab]) for lab, v in _tweestap_sleutels(a, b, k).items()])
        assert kop(it) == k0, ('#325 kop', it['id'])
        it['merge']['r7b325'] = {'oud': f'{o} = {oud}', 'nieuw': f'{n} = {ans}'}; LOG7B['325'].append((it['id'], o, n, f'{oud} → {ans}'))
    # #301 (032) + #323 + #300: wisselgeld
    for it in rows:
        if (it['merge'].get('doel') or '') != 'G5-GET-E09': continue
        m = WISSEL.match(it['opgave'] or '')
        if not m: continue
        wie, n, ding, p, B = m[1], int(m[2]), m[3], int(m[4]), int(m[5]); n0, B0 = n, B
        if it['id'] == _id('E09', '032'): n = 4                                   # #301: 5 × €5 = €25 = het wisselgeld
        if it['id'] == _id('E09', '024'): n = 6                                   # ronde 10 #365 (Daves wens bij #323): 6 × €5, betalen met €50, €20 terug
        kost = n * p
        if B == 100:                                                              # #323: het kleinste biljet boven de kosten, anders één stap groter
            for x in [x for x in BILJET if x > kost][:2]:
                if _wissel_ok(n, p, x): B = x; break
        assert _wissel_ok(n, p, B), ('#301/#323 wisselgeld', it['id'], n, p, B)
        if (n, B) != (n0, B0):
            k0 = kop(it); w = _wissel_sleutels(n, p, B)
            it['opgave'] = f'{wie} koopt {n} {ding} van €{p} per stuk en betaalt met €{B}. Hoeveel geld krijgt {m[6]} terug?'
            it['antwoord'] = f"€{w['ans']}"; ev = it['extraVelden']
            ev['claudeKaleSom'] = f'{B} − {n} × {p}'; ev['claudeUitleg'] = f"Stap 1: {n} × €{p} = €{w['kost']}.\nStap 2: €{B} − €{w['kost']} = €{w['ans']} terug."
            _claude(it, [(f'€{w[sl]}', lab, WISSEL_UITLEG[sl]) for lab, sl in WISSEL_LAB.items()])
            assert kop(it) == k0, ('#323 kop', it['id'])
            it['merge']['r7b323'] = {'punt': '#365' if it['id'] == _id('E09', '024') else '#301' if n != n0 else '#323', 'oud': f'{n0} × €{p}, betaalt €{B0}', 'nieuw': f'{n} × €{p}, betaalt €{B}'}
            LOG7B['365' if it['id'] == _id('E09', '024') else '323' if n == n0 else '301'].append((it['id'], f'{n0} × €{p}, €{B0} → {n} × €{p}, €{B}'))
        if it['type'] != 'meerkeuze':                                             # #300: open geldvraag → geldInvoer (standaardlijst #33/#105)
            it['geldInvoer'] = {'sleutel': it['antwoord'], 'accepteer': [], 'regel': EURO_ACC, 'punt': {'voorbeeld': '', 'tekst': 'Bij geld schrijf je een komma.'}, 'merge': '#300'}
            it['antwoordOokGoed'] = []
            import fixlijst_g5b as _FX5B; _FX5B.antwoordvormen(it); LOG7B['300'].append(it['id'])
    # #321/#354: E07 #6 (TT × TT schatten) → G6-GET-E06 (besluit Dave 23:41; doel volgens de G6-bank: schattend ×, 2-cijferig × 2-cijferig met een rond getal)
    for it in rows:
        if (it['merge'].get('doel') == 'G5-GET-E07' and it['merge'].get('status') == 'gemapt' and SCHAT.match(it['opgave'] or '') and ' × ' in it['opgave']):
            it['merge']['besluit321'] = {'door': 'Dave 1 okt 23:41 (#321/#354), doel G6-GET-E06 (ronde 9, 8 okt)', 'van': 'G5-GET-E07 #6 (nrOrigineel 19)', 'naar': 'G6-GET-E06',
                                         'somtypeG5': it['merge']['somtype']}
            it['merge'].update(status='park-G6', doel=None, voorstelDoel='G6-GET-E06'); it['doelId'] = None
            LOG7B['321'].append(it['id'])
    assert len(LOG7B['321']) == 10, ('#321', len(LOG7B['321']))
    # #235: dunne somtypen aanvullen
    rows += generator_235(rows, kop)
    # #327: niveau E05 (kan kloppen, kale sommen) naar cijfers en lenen/onthouden; schatten niet. Alleen omhoog.
    for it in rows:
        if it['merge'].get('doel') != 'G5-GET-E05' or it['merge'].get('status') != 'gemapt' or SCHAT.match(it['opgave'] or ''): continue
        if not (it['id'].startswith(PRE + 'E05-claude-bank-naar-') or it['merge'].get('gen235')): continue      # #327 gaat over de G8→G5-items (kan kloppen, verhaal)
        s = _som327(it)
        if not s: continue
        nv = niveau327(*s)
        if nv == 'toepassen' and it['niveau'] == 'basis':
            it['niveau'] = 'toepassen'; it['niveauKind'] = 'Oefenen'; it['merge']['niveau327'] = {'oud': 'basis', 'som': f'{s[0]} {s[1]} {s[2]}', 'waarom': 'drie cijfers' if max(s[0], s[2]) >= 100 else 'onthouden/lenen'}
            LOG7B['327'].append(it['id'])
    return LOG7B

def guards_r7b(rows):
    """Vlak voor het schrijven, op alle gemapte G5-items. AssertionError = FAIL (de build stopt)."""
    G = [r for r in rows if r['merge'].get('status') == 'gemapt' and (r['merge'].get('doel') or '').startswith('G5-')]
    k_e09_2 = kop_nro(rows, 'G5-GET-E09', 2); k_e05_20 = kop_nro(rows, 'G5-GET-E05', 20)
    ids = [r['id'] for r in rows]; assert len(ids) == len(set(ids)), ('ids dubbel', [i for i in ids if ids.count(i) > 1][:5])
    for it in G:
        for o in (it.get('opties') or []) if it['merge']['doel'].startswith('G5-GET-') else []:      # #302 (getallen tot 1000; ml en staafsommen in MEET/VBN mogen erboven)
            v = re.sub(r'[€\s.]', '', o['tekst']).replace(',', '.')
            assert not (re.fullmatch(r'\d+(\.\d+)?', v) and float(v) > 1000), ('#302 optie > 1000', it['id'], o['tekst'])
        m = SCHAT.match(it['opgave'] or '')                       # #301a / #322 / #326
        if m:
            a, op, b = int(m[1]), m[2], int(m[3]); s = 10 if m[4] == 'tientallen' else 100
            assert str(_schat(a, op, b, s)) == it['antwoord'], ('#301 schatting klopt niet', it['id'])
            if op != '×': assert _anders(a, op, b, s) != int(it['antwoord']), ('#301a afronden op de andere plaats geeft het goede antwoord', it['id'], it['opgave'])
            if op == '+' and it['merge']['doel'] == 'G5-GET-E05': assert int(it['antwoord']) + s <= 1000, ('#322 sleutel antwoord + stap boven 1000', it['id'])
            if op == '+' and s == 10 and it['merge']['somtype'] == k_e05_20: assert a % 10 and b % 10, ('#326 een term is al rond', it['id'])
        m = WISSEL.match(it['opgave'] or '')                      # #301b + #300 + #323
        if m:
            n, p, B = int(m[2]), int(m[4]), int(m[5])
            assert _wissel_ok(n, p, B) and it['antwoord'] == f'€{B - n * p}', ('#301b wisselgeld = kosten of sleutelbotsing', it['id'])
            assert it['type'] == 'meerkeuze' or len((it.get('geldInvoer') or {}).get('accepteer') or []) >= 3, ('#300 geen geldInvoer', it['id'])
            assert B in [x for x in BILJET if x > n * p][:2], ('#323 te groot biljet', it['id'], B)
        if it['merge']['doel'] == 'G5-GET-E09' and it['merge']['somtype'] == k_e09_2:      # #325
            q = re.findall(r'\d+', it['opgave']); a, b, k = map(int, q[:3]); opg = a + b - k
            assert opg not in (a, b, k) and str(a * b - k) == it['antwoord'], ('#325 opgeteld = getal uit de vraag', it['id'])
        assert not it['merge'].get('besluit321'), ('#321 nog in G5', it['id'])
    import collections as _c
    tel = _c.Counter((r['merge']['doel'], r['merge'].get('somtype')) for r in G)
    for d, s in {(r['merge']['doel'], r['merge']['somtype']) for r in G if r['merge'].get('gen235')}:
        assert tel[(d, s)] >= 8, ('#235 somtype nog dun', d, s, tel[(d, s)])
    return True
