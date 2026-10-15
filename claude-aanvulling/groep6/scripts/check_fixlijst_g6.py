#!/usr/bin/env python3
"""Check op de G6-fixlijst (#1, #2, #3, #4, #6), op data/gemapt.json. Leest alleen. Exit 1 bij een fout.
 #1 E01 #1/#4: het buurgetal aan de andere kant heet 'verkeerde kant'; 'één stap te ver' is nooit dat buurgetal.
 #2 'Hoeveel is de D in dit getal waard?': D staat precies één keer in het getal.
 #3 M03 #2: geen sleutel gelijk aan het antwoord; elke sleutel past bij zijn denkfout (0,teller of noemer : teller).
 #4 M03 #1: elk item heeft een fout-hint; geen sleutel heeft de waarde van het antwoord.
 #6 M02 #2/#3: 'één erbij gedaan' = getal2 + 1 en 'één eraf gehaald' = getal2 − 1.
 Ronde 2 (Didactiek 20:15, Dave 20:16):
 #152 E01 'Rond … af op …': geen middengetal zolang een E01-entry 'het dichtst bij' zegt; het antwoord is goed afgerond (half naar boven).
      #156d (besluit Dave 20:38): de vraag in de kindtekst beslist. 'het dichtst bij' → FAIL bij een middengetal; 'Rond … af op …' → FAIL bij
      0 middengetallen, bij meer dan 2 (besluit: 1 à 2), en als Hint 2 de regel '5 of meer → erboven' niet noemt. INFO: per somtype vraag + aantal.
 #153 M03 #1: veld beoordeling (banden), streepjesPerTiende = true, geen sleutel buiten [van, tot].
 #154 M02 #2/#3: 'op de verkeerde plek' = getal2 ± getal1 × 10, getal1 : 10 of getal1 × 100.
 #158 (Dave 20:49): FAIL bij een getal of antwoord boven 100.000 in een G6-GET-item (grens regels_g6), ook ná de fixlijst.
 #159b: FAIL als een afrond-somtype van E01 geen middengetal heeft, en als 'dichtst' voorkomt in de kindtekst (hint-entry of item) van een somtype
      met een middengetal.
 #160: FAIL bij 'teller' in een opgave van M02 #4, en bij een E01 #5/#7/#8-opgave met de oude context ('In [plek] zijn precies # [ding]').
 #162 E07 #1: sleutels uit de echte som (998 is bijna 1000). #163 M05 #3: fout-hints (sorteerregels) en getallenruimte 0–200.
 #164 geen context die niet bij het aantal past (E04, E06, M05, M06, E07). #165 E06 #5: geen twee keer dezelfde som. #166 E04 #1/#2: claudeUitleg past bij het item.
 #167 E04/E06: geen Claude-labels komma-verschoven/geld-verkeerd-geteld/schatting-verkeerd meer.
 #156 M02 #5: het cijfer is niet 0 en staat niet op de eenheden; M02 #1: één cijfer ± 1, niet de eenheden; M02 #4: eindigt op 9; M03 #1: kommagetal."""
import json, re, os, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def d(v): t = str(v).replace('.', '').replace(',', '.'); return Fraction(t) if re.fullmatch(r'\d+(\.\d+)?', t) else None
def run():
    G = json.load(open(f'{BASE}/data/gemapt.json'))['items']; F = []
    for it in G:
        k = (it['merge']['doel'], it['merge'].get('somtypeNrOrigineel')); fh = it['foutHints']; t = it['id']
        if k in (('G6-GET-E01', 1), ('G6-GET-E01', 4)):
            stap = 1000 if k[1] == 1 else 10000
            g1 = int(re.search(r'Rond ([\d.]+)', it['opgave']).group(1).replace('.', '')); a = int(str(it['antwoord']).replace('.', ''))
            o = g1 // stap * stap; ander = o if a == o + stap else o + stap
            for f in fh:
                v = d(f['fout'])
                if v == ander and f['soort'] != 'verkeerde kant': F.append(f"#1 {t}: {f['fout']} is het andere buurgetal maar heet '{f['soort']}'")
                if f['soort'] == 'verkeerde kant' and v != ander: F.append(f"#1 {t}: {f['fout']} heet 'verkeerde kant' maar is het buurgetal niet")
        if (m := re.search(r'staat (?:het getal )?(\d[\d.]*)[^.]*\. Hoeveel is de (\d) in dit getal waard\?', it['opgave'])):
            if m.group(1).replace('.', '').count(m.group(2)) != 1: F.append(f"#2 {t}: de {m.group(2)} staat niet precies één keer in {m.group(1)}")
        if k == ('G6-GET-M03', 2):
            tn = re.search(r'(\d+)/(\d+) meter', it['opgave']); te, no = int(tn.group(1)), int(tn.group(2))
            for f in fh:
                v = d(f['fout'])
                if v == Fraction(te, no): F.append(f"#3 {t}: sleutel {f['fout']} = het antwoord")
                ok = v == Fraction(f'0.{te}') or (v is not None and abs(v - Fraction(no, te)) < Fraction(1, 100))
                if not ok: F.append(f"#3 {t}: sleutel {f['fout']} past bij geen denkfout")
        if k == ('G6-GET-M03', 1):
            if not fh: F.append(f"#4 {t}: geen fout-hint")
            for f in fh:
                if d(f['fout']) == d(it['antwoord']): F.append(f"#4 {t}: sleutel {f['fout']} = het antwoord")
        if k in (('G6-GET-M02', 2), ('G6-GET-M02', 3)):
            g2 = int(re.findall(r'[\d.]+(?=\?)', it['opgave'])[0].replace('.', ''))
            for f in fh:
                if f['soort'] in ('één erbij gedaan', 'één eraf gehaald') and d(f['fout']) != g2 + (1 if k[1] == 2 else -1):
                    F.append(f"#6 {t}: {f['fout']} heet '{f['soort']}' maar is geen getal2 {'+' if k[1] == 2 else '−'} 1")
    # ---- ronde 2
    import fixlijst_g6 as FX
    INFO.clear(); VRAAG.clear(); midden = {}
    for it in G:
        o = it['opgave']; t = it['id']; fh = it['foutHints']; k = (it['merge']['doel'], it['merge'].get('somtypeNrOrigineel'))
        if it['merge']['doel'] == 'G6-GET-E01' and (m := FX.AFROND.search(o)):
            n = int((m.group(1) or m.group(2)).replace('.', '')); s_ = FX.STAP[m.group(3)]
            midden.setdefault(k, 0); midden[k] += n % s_ == s_ // 2
            vr = FX.vraag_e01(o); VRAAG.setdefault(k, set()).add(vr)
            if vr == 'dichtst bij' and n % s_ == s_ // 2: F.append(f"#152 {t}: middengetal {o} bij 'het dichtst bij'")
            if it['antwoord'] != FX._fmt(FX._rond(n, s_)): F.append(f"#152 {t}: antwoord {it['antwoord']} is niet {o} goed afgerond")
        if k == ('G6-GET-M03', 1):
            gl = it['visual'].get('getallenlijn') or {}
            if not it.get('beoordeling') or it['beoordeling'].get('soort') != 'banden': F.append(f"#153 {t}: geen beoordeling met banden")
            if gl.get('streepjesPerTiende') is not True: F.append(f"#153 {t}: streepjesPerTiende is niet true")
            for f in fh:
                if d(f['fout']) is not None and not (gl['van'] <= d(f['fout']) <= gl['tot']): F.append(f"#153 {t}: sleutel {f['fout']} buiten de lijn {gl['van']}–{gl['tot']}")
            if not re.match(r'Zet \d+,\d op de lijn', o): F.append(f"#156 {t}: geen kommagetal: {o}")
        if k in (('G6-GET-M02', 2), ('G6-GET-M02', 3)):
            g1 = int(re.search(r'is ([\d.]+) (?:meer|minder)', o).group(1).replace('.', '')); g2 = int(re.findall(r'[\d.]+(?=\?)', o)[0].replace('.', ''))
            tk = 1 if k[1] == 2 else -1; ok = {g2 + tk * x for x in (g1 * 10, g1 // 10 if g1 % 10 == 0 else None, g1 * 100) if x}
            for f in fh:
                if f['soort'] == 'op de verkeerde plek' and d(f['fout']) not in ok: F.append(f"#154 {t}: {f['fout']} heet 'op de verkeerde plek' maar past niet")
        try: FX.asserts156(it)
        except AssertionError as e: F.append(f"#156 {t}: {e}")
    for it in G:      # #158
        if (it['merge']['doel'] or '').startswith(('G6-GET', 'G6-MEET')):      # #199: ook MEET
            m = max(FX.getallen158(it['opgave']) + FX.getallen158(it['antwoord']) + [x for o in it.get('opties') or [] for x in FX.getallen158(o['tekst'])] + [0])      # getoond + antwoord (Didactiek 21:25)
            if m > FX.GROOT158: F.append(f"#158 {it['id']}: getal {m} boven 100.000 ({it['opgave'][:60]} → {it['antwoord']})")
        k = (it['merge']['doel'], it['merge'].get('somtypeNrOrigineel'))
        if k == ('G6-GET-M02', 4) and re.search(r'\bteller\b', it['opgave'], re.I): F.append(f"#160 {it['id']}: 'teller' in de opgave: {it['opgave']}")
        if it['merge']['doel'] == 'G6-GET-E01' and FX.CTX.match(it['opgave']): F.append(f"#160 {it['id']}: oude context: {it['opgave']}")
    H2 = {}
    for b in sorted(glob.glob(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'hints', 'batch*.json'))):
        for st in json.load(open(b, encoding='utf-8'))['somtypen']:
            if st['doel'] == 'G6-GET-E01': H2[('G6-GET-E01', st.get('nrOrigineel', st['nr']))] = st
    for k, n in sorted(midden.items(), key=str):
        vr = VRAAG[k]
        if len(vr) > 1: F.append(f"#156d {k[0]} #{k[1]}: items vragen verschillend ({', '.join(sorted(vr))})"); continue
        vr = next(iter(vr)); st = H2.get(k) or {}
        if vr == 'rond af':
            if not n: F.append(f"#156d {k[0]} #{k[1]}: 'Rond … af op …' maar geen middengetal")
            if n > 2: F.append(f"#156d {k[0]} #{k[1]}: {n} middengetallen (besluit: 1 à 2)")
            if not re.search(r'5 of meer, dan rond je af naar het \w+ erboven', st.get('hint2') or ''): F.append(f"#156d {k[0]} #{k[1]}: Hint 2 noemt de regel '5 of meer → erboven' niet")
        if n:      # #159b: geen 'dichtst' in een somtype met een middengetal
            teksten = [('Hint 1', st.get('hint1')), ('Hint 2', st.get('hint2')), ('Ouderzin', st.get('ouderzin'))] + [(f"entry '{f.get('soort')}'", f['tekst']) for f in st.get('foutHints') or []]
            for it in G:
                if (it['merge']['doel'], it['merge'].get('somtypeNrOrigineel')) == k:
                    teksten += [(f"{it['id'][-3:]} '{f.get('soort')}'", f.get('uitleg')) for f in it.get('foutHints') or []] + [(f"{it['id'][-3:]} algemeneFoutHint", it.get('algemeneFoutHint'))]
            raak = sorted({lab.split(' ')[0] if lab[:3].isdigit() else lab for lab, t in teksten if re.search(r'dichtst', t or '', re.I)})
            if raak: F.append(f"#159b {k[0]} #{k[1]}: 'dichtst' in een somtype met een middengetal ({', '.join(raak[:6])}{' …' if len(raak) > 6 else ''})")
        INFO.append(f"#156d {k[0]} #{k[1]}: vraag '{vr}', {n} middengetal(len)")
    F += ronde3(G)
    F += ronde4(G)
    F += ronde5(G)
    return F
OUD164 = re.compile(      # ('eieren' mag: «Een kippenboer verzamelt elke dag 400 eieren»; het nest met 4055 eieren is weg)
    r'\b(botten|blaadjes|poesjes|veren|tanden|stappen|noten|pionnen|knopen|stenen|wortels|vissen|truien|stickers|dennenappels|schelpen|zakken|pakken|ballen)\b')
def ronde3(G):
    import fixlijst_g6 as FX
    """#162–#167 (Oefeningen batch 2, Dave 21:07)."""
    F = []; som = {}
    for it in G:
        d = it['merge']['doel']; k = (d, it['merge'].get('somtypeNrOrigineel')); t = it['id']; ex = it['extraVelden']; o = it['opgave'] or ''
        if k == ('G6-GET-E07', 1):      # #162: sleutels uit de echte som
            m = re.match(r'(\d+) .+? van elk €(\d+)\.', o); n, p = int(m.group(1)), int(m.group(2)); r = -(-p // 100) * 100
            ks = {f['fout'] for f in it['foutHints']}
            if f'€{n * p}' != it['antwoord']: F.append(f"#162 {t}: antwoord {it['antwoord']} ≠ €{n * p}")
            for f in it['foutHints']:
                if f['soort'] == 'stukje niet afgehaald' and f['fout'] != f'€{n * r}': F.append(f"#162 {t}: 'stukje niet afgehaald' = {f['fout']}, verwacht €{n * r}")
                if f['soort'] == 'te veel afgehaald' and f['fout'] != f'€{n * r - 2 * n * (r - p)}': F.append(f"#162 {t}: 'te veel afgehaald' = {f['fout']}")
            if f'bijna {r}.' not in (ex.get('claudeUitleg') or '') or ' -' in (ex.get('claudeUitleg') or ''): F.append(f"#162 {t}: claudeUitleg past niet: {ex.get('claudeUitleg')!r}")
        if k == ('G6-GET-M05', 3):      # #163
            if not it['foutHints']: F.append(f"#163 {t}: geen fout-hint")
            if it.get('getallenruimte') != '0–200': F.append(f"#163 {t}: getallenruimte {it.get('getallenruimte')!r}")
        if d in ('G6-GET-E04', 'G6-GET-E06', 'G6-GET-M05', 'G6-GET-M06', 'G6-GET-E07') and any(rx.match(it['merge'].get('opgaveVoor164') or o) for dd, rx, _ in FX.CTX164 if dd == d):
            if OUD164.search(o): F.append(f"#164 {t}: context past niet bij het aantal: {o}")
        if k == ('G6-GET-E06', 5):      # #165
            ks_ = ex.get('claudeKaleSom')
            if ks_ in som: F.append(f"#165 {t}: dezelfde som als {som[ks_]} ({ks_})")
            som[ks_] = t
        if d == 'G6-GET-E04' and (u := FX.uitleg166(o)) and (ex.get('claudeUitleg') or u) != u: F.append(f"#166 {t}: claudeUitleg past niet bij het item")
        if d in ('G6-GET-E04', 'G6-GET-E06'):    # #167
            lab = {dk['denkfout'] for dk in ex.get('claudeDenkfouten') or []} | {f.get('regel') for f in it['foutHints']}
            if any(re.search(r'komma-verschoven|geld-verkeerd-geteld|schatting-verkeerd', x or '') for x in lab): F.append(f"#167 {t}: nog een Claude-label ({sorted(x for x in lab if x)})")
    INFO.append(f"#162–#167: {len(F)} FAIL")
    return F
def ronde4(G):
    """#169–#172, #174 (Oefeningen batch 3, Dave 21:24) en #190–#195 (Didactiek batch 2, 21:25/21:35)."""
    import fixlijst_g6 as FX
    sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'tools')); import breukvorm as BV
    F = []; e190 = set(); e08 = [0, 0]; groot_sleutel = 0; n190 = 0; n171 = {}
    for it in G:
        d = it['merge']['doel']; k = (d, it['merge'].get('somtypeNrOrigineel')); t = it['id']; o = it['opgave'] or ''; fh = it['foutHints']
        getoond = set(FX.getallen158(o)) | {x for op in it.get('opties') or [] for x in FX.getallen158(op['tekst'])}
        if (d or '').startswith('G6-GET'):
            groot_sleutel += sum(1 for f in fh for x in FX.getallen158(f['fout']) if x > FX.GROOT158 and x not in getoond)
        if re.search(r'\beven veel\b', o + ' ' + ' '.join(op['tekst'] for op in it.get('opties') or [])): F.append(f"#192 {t}: 'even veel': {o}")
        if k == ('G6-GET-E06', 1) and (m := FX.KEER190.match(o)):      # #190
            a, b = int(m.group(1)), int(m.group(2)); v = str(a * sum(int(x) for x in str(b)))
            if any(dk['denkfout'] == FX.LAB190 for dk in it['extraVelden'].get('claudeDenkfouten') or []): e190.add(t[-3:])      # Claudes 'stuk vergeten' dat de cijfersom is
            for f in fh:
                if f['fout'].replace('.', '') == v and b % 10 and not FX.is196(b) and f['soort'] != 'cijfers van het tweede getal opgeteld': F.append(f"#190 {t}: {v} heet '{f['soort']}'")
                if f['soort'] == 'cijfers van het tweede getal opgeteld': n190 += 1
        if k == ('G6-GET-M05', 3):      # #193/#195
            w = re.fullmatch(r'wel:([\d,]+)\|niet:([\d,]+)', it['antwoord']); wel, niet = set(w.group(1).split(',')), set(w.group(2).split(','))
            for f in fh:
                x = re.fullmatch(r'wel:([\d,]*)\|niet:([\d,]*)', f['fout']); fw, fn = set(x.group(1).split(',')) - {''}, set(x.group(2).split(',')) - {''}
                verw = 'deelbaar getal bij niet' if len(fw) == len(wel) - 1 and fw < wel else 'niet-deelbaar getal bij deelbaar' if len(fw) == len(wel) + 1 and wel < fw else 'vakken omgewisseld' if (fw, fn) == (niet, wel) else None
                if f['soort'] != verw: F.append(f"#193 {t}: {f['fout']} heet '{f['soort']}', verwacht '{verw}'")
            b = it.get('beoordeling') or {}
            if not (b.get('perVakAlsVerzameling') and b.get('volgordeBinnenVakTeltNiet') and 'andere fout' in b.get('tweeOfMeerVerkeerd', '')): F.append(f"#195 {t}: beoordeling ontbreekt of klopt niet")
        if d == 'G6-GET-E04' and (m := FX.HANDIG194.match(o)):      # #194a
            b = int(m.group(2)); H = (b + 50) // 100 * 100
            if abs(b - H) > 10: F.append(f"#194 {t}: {b} ligt niet binnen 10 van een honderdtal")
            if _som(it['antwoord']) != int(m.group(1)) - b: F.append(f"#194 {t}: antwoord {it['antwoord']} ≠ {int(m.group(1)) - b}")
            for op in it.get('opties') or []:
                if op['tekst'] != it['antwoord'] and _som(op['tekst']) == int(m.group(1)) - b: F.append(f"#194 {t}: optie {op['tekst']} is ook goed")
        if d == 'G6-GET-E08' and (m := re.match(r'^\d+ [a-zà-ÿ\']+ verzamelden [a-zà-ÿ\']+\. Ze hadden er ((?:\d+, )+\d+) en (\d+)\. ', o)):      # #194b
            xs = [int(x) for x in m.group(1).split(', ')] + [int(m.group(2))]; e08[0] += 1
            if str(sum(xs) / len(xs)).removesuffix('.0') != str(it['antwoord']): F.append(f"#194 {t}: gemiddelde {sum(xs) / len(xs)} ≠ {it['antwoord']}")
            if int(it['antwoord']) in xs: e08[1] += 1
        elif d == 'G6-GET-E08' and re.search(r'verzamelden .*\. \d+, \d+', o): F.append(f"#194 {t}: lijstje is geen zin: {o}")
        if d == 'G6-GET-E06' and 'Ze gaan eerlijk over' in o: F.append(f"#194 {t}: oude zin: {o}")
        if d == 'G6-GET-M05' and re.search(r'\btanden\b', o): F.append(f"#194 {t}: tanden: {o}")
        if k == ('G6-GET-E03', 7):      # #169
            b = it.get('beoordeling') or {}
            m169 = FX.LIJN169.match(o); buren = [x for x in ((int(m169.group(1)) - 1, int(m169.group(1)) + 1) if m169 else ()) if 0 < x < int(m169.group(2))]      # #398: een buur op 0 of n/n is een eindpunt
            if b.get('soort') != 'banden' or (buren and not any(f['soort'] in ('een stuk te ver', 'een stuk te kort') for f in fh)): F.append(f"#169 {t}: geen banden of geen 'een stuk te ver/te kort'")      # #203: de namen van Oefeningen
        if k == ('G6-GET-E03', 6) and ' van ' in o and it['bron']['claudeId'] not in FX.DUBBEL172: F.append(f"#172 {t}: nog een context: {o}")
        if d == 'G6-GET-M04' and (m := FX.STUK171.search(o)):      # #171/#187
            vb = BV.waarde(m.group(2)); n171[m.group(2)] = n171.get(m.group(2), 0) + 1
            if vb == BV.waarde(it['antwoord']) or vb in {BV.waarde(x) for x in it.get('antwoordOokGoed') or []} or vb in {BV.waarde(f['fout']) for f in fh}: F.append(f"#171 {t}: het voorbeeld is een antwoord of sleutel: {o}")
        elif d == 'G6-GET-M04' and 'zoals' in o and 'Typ een breuk' in o: F.append(f"#187 {t}: voorbeeld niet herkend: {o}")
    VERW = VERW190 - set('005 009 021 036 041 072 084 102 104 108 124 156 179 194 198 204 215 219 225'.split())      # #196: × 19 blijft 'stuk vergeten'
    if e190 != VERW: F.append(f"#190: {len(e190)} items met de cijfersom-sleutel, verwacht {len(VERW)}; extra {sorted(e190 - VERW)}, mist {sorted(VERW - e190)}")
    if e08[0] and e08[1] * 3 > e08[0]: F.append(f"#194: E08 antwoord in het lijstje bij {e08[1]} van {e08[0]} (meer dan 1 op 3)")
    INFO.append(f"#169–#195: {len(F)} FAIL · E06 #1 Claude-label → cijfers-van-getal2-opgeteld in {len(e190)} items, motor-sleutels 'cijfers van het tweede getal opgeteld' {n190} · E08 antwoord in het lijstje {e08[1]}/{e08[0]} · "
                f"fout-sleutels boven 100.000 die nooit getoond worden (mogen, Didactiek 21:25): {groot_sleutel} · voorbeelden M04 #4 {n171}")
    return F
VERW190 = set('008 016 018 022 024 030 031 034 043 053 062 072 076 081 089 104 108 112 113 120 128 129 150 151 154 172 174 176 178 181 186 196 209 211 223 226 228'.split())
def _som(e): return eval(e.replace('−', '-').replace('.', ''))
def ronde5(G):
    """#173/#176/#178/#180/#183/#185/#186/#189/#196–#199/#201 (Didactiek batch 3 en recheck 2b 21:42, Oefeningen batch 4 21:43)."""
    import fixlijst_g6 as FX, regels_g6 as R6
    sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import evenveel_check as EV
    F = []; n = collections.Counter(); kgv = 0; e196 = {}
    from math import lcm
    for it in G:
        d = it['merge']['doel']; k = (d, it['merge'].get('somtypeNrOrigineel')); t = it['id']; o = it['opgave'] or ''; fh = it['foutHints']
        if k == ('G6-GET-M04', 3):      # #173
            m = FX.HEET173.match(o); goed = it['antwoord']; wissel = 'de noemer' if goed == 'de teller' else 'de teller'
            if [x['tekst'] for x in it['opties']] != [goed, wissel, 'de uitkomst']: F.append(f"#173 {t}: opties {[x['tekst'] for x in it['opties']]}")
            if not fh or fh[0]['fout'] != wissel: F.append(f"#173 {t}: de hoofdsleutel is niet '{wissel}' ({[(f['soort'], f['fout']) for f in fh]})")
            if not any(f['fout'] == 'de uitkomst' for f in fh): F.append(f"#173 {t}: geen sleutel 'de uitkomst'")
        if (m := FX.KIES180.match(o)) and d == 'G6-GET-E03':      # #180
            br = re.findall(r'\d+/\d+', m.group(2)); ok, why, per = R6.niveau180(br, it['antwoord'], uitleg=True); n['180 blijft'] += 1
            if not ok: F.append(f"#180 {t}: boven G6-niveau: {why}")
            ta_, na_ = (int(x) for x in it['antwoord'].split('/'))
            for b_, geval in per:      # één assert per geval waarin het kgv boven de 24 mag (Didactiek 22:08)
                tb_, nb_ = (int(x) for x in b_.split('/')); kg = lcm(na_, nb_); n[f'180 {geval}'] += 1
                if geval == 'kgv ≤ 24' and kg > 24: F.append(f"#180 {t}: {it['antwoord']}/{b_} kgv {kg} > 24")
                if geval == 'dezelfde teller' and not (ta_ == tb_ and na_ <= 20 and nb_ <= 20): F.append(f"#180 {t}: 'dezelfde teller' klopt niet ({it['antwoord']} tegen {b_})")
                if geval == 'vergelijken met ½':
                    d1, d2 = 2 * ta_ - na_, 2 * tb_ - nb_; from fractions import Fraction as _F1
                    dl = lambda t_, n_: 2 * t_ != n_ and abs(_F1(t_, n_) - _F1(1, 2)) >= _F1(1, 20)      # Didactiek 22:14: |breuk − ½| ≥ 1/20 en 2·teller ≠ noemer
                    if not (d1 * d2 < 0 and dl(ta_, na_) and dl(tb_, nb_) and na_ <= 20 and nb_ <= 20): F.append(f"#180 {t}: 'vergelijken met ½' klopt niet ({it['antwoord']} tegen {b_})")
            ta, na = (int(x) for x in it['antwoord'].split('/'))
            kgv = max([kgv] + [lcm(na, int(b.split('/')[1])) for b in br if b != it['antwoord'] and int(b.split('/')[0]) != ta and lcm(na, int(b.split('/')[1])) <= 24])
        if d == 'G6-GET-M04' and 'Er blijft ook nog een stuk over' in o: F.append(f"#183 {t}: {o}")
        if d == 'G6-GET-M04' and (re.search(r'\bdelen een\b', o) or 'Welk deel is dat?' in o): F.append(f"#185 {t}: {o}")
        if k == ('G6-GET-E03', 7):      # #186
            if it.get('vereistTekening') is not True: F.append(f"#186 {t}: geen vereistTekening")
            m = FX.LIJN169.match(o); tt, nn = int(m.group(1)), int(m.group(2))      # #203: een stuk te ver (t + 1) en te kort (t − 1)
            verw = {('0' if x == 0 else f'{x}/{nn}'): z for x, z in ((tt + 1, 'een stuk te ver'), (tt - 1, 'een stuk te kort')) if 0 <= x <= nn}
            gek = {f['fout']: f['soort'] for f in fh}      # #398 (ronde 10, besluit Overzicht): de eindpunten 0, 1 en n/n krijgen 'begin of eind van de lijn' (vóór de stuk-regels, tekst Z-#391)
            verw.update({x: 'begin of eind van de lijn' for x in ('0', '1', f'{nn}/{nn}') if x != it['antwoord']})
            if gek != verw: F.append(f"#203 {t}: sleutels {[(f['soort'], f['fout']) for f in fh]}, verwacht {verw}")
            if (it.get('beoordeling') or {}).get('eenStukErnaast', {}).get('soorten') != {'groter': 'een stuk te ver', 'kleiner': 'een stuk te kort'}: F.append(f"#203 {t}: namen in beoordeling")
        if k == ('G6-GET-E03', 4) and (q := re.search(r'met noemer (\d+)|\?/(\d+)', o)):      # #202
            N = int(q.group(1) or q.group(2)); a_ = d(it['antwoord']) if False else None
            from fractions import Fraction as _F
            fa = _F(*map(int, it['antwoord'].split('/')))
            for f in fh:
                if f['soort'] == FX.R202[1]:
                    n['202'] += 1
                    tf, nf = map(int, f['fout'].split('/'))
                    if _F(tf, nf) != fa or nf == N: F.append(f"#202 {t}: sleutel {f['fout']} past niet (antwoord {it['antwoord']}, noemer {N})")
        if it['bron']['claudeId'] == FX.ID189:
            n['189'] += 1
            if (o, it['antwoord']) != ('Sem krijgt 3/8 van 32 knikkers. Hoeveel knikkers is dat?', '12'): F.append(f"#189 {t}: {o} → {it['antwoord']}")
            if any(f['fout'] == '12' for f in fh) or any(f['fout'] == '20' and f['soort'] == 'wat overblijft' and False for f in fh): F.append(f"#189 {t}: sleutel = antwoord")
        if d == 'G6-GET-E03' and FX.LOS201.match(o): F.append(f"#201 {t}: losse zin: {o}")
        if k == ('G6-GET-E06', 1) and (m := FX.KEER190.match(o)) and FX.is196(int(m.group(2))):      # #196
            v = str(int(m.group(1)) * (int(m.group(2)) // 10 * 10)); s = [f['soort'] for f in fh if f['fout'].replace('.', '') == v]; e196[t[-3:]] = s
            if s != ['stuk vergeten']: F.append(f"#196 {t}: {v} heet {s}, verwacht 'stuk vergeten'")
        if d == 'G6-GET-E06':      # #198
            for f in fh:
                if f['soort'] == FX.R198[1]: n['198 sleutels'] += 1; n[f'198 {k[1]}'] += 1
        if d == 'G6-MEET-E03':      # #176
            for f in fh:
                if f['soort'] in (FX.R176[0][1], FX.R176[1][1]): n[f"176 {f['soort']}"] += 1
                if f['soort'] == 'omtrek of verdubbeld': n['176 nog Claude-label'] += 1
        if d == 'G6-MEET-E01' and re.search(r'\bEen pakket\b.*\been andere \d', o): F.append(f"#178 {t}: {o}")
        if 'vallei ligt een vlot' in o: F.append(f"#178 {t}: {o}")
    exp196 = set('005 009 021 036 041 072 084 102 104 108 124 156 179 194 198 204 215 219 225'.split())
    if set(e196) != exp196: F.append(f"#196: items met getal2 = 19 {sorted(e196)} ≠ lijst Didactiek (extra {sorted(set(e196) - exp196)}, mist {sorted(exp196 - set(e196))})")
    if n['189'] != 1: F.append(f"#189: E09 602 {n['189']} keer gevonden")
    nev = EV.rapport(G, toon=False)
    if nev: F.append(f"#192/#197: 'even veel' nog {nev} keer in een tekstveld (ook ouderzin/hints)")
    INFO.append(f"ronde 5: {len(F)} FAIL · #180 blijft {n['180 blijft']} (grootste kgv in een kgv-vergelijking {kgv}; vergelijkingen: kgv ≤ 24 {n['180 kgv ≤ 24']}, dezelfde teller {n['180 dezelfde teller']}, met ½ {n['180 vergelijken met ½']}) · #196 {len(e196)} items 'stuk vergeten' · "
                f"#198 {n['198 sleutels']} sleutels (E06 #3 {n['198 3']}, #7 {n['198 7']}) · #202 {n['202']} sleutels · #176 omtrek {n['176 omtrek in plaats van oppervlakte']}, verdubbeld {n['176 oppervlakte verdubbeld']}, nog Claude-label {n['176 nog Claude-label']}")
    return F + ronde7(G) + ronde8(G) + ronde9(G)

def ronde7(G):
    """ronde 7 (Didactiek recheck 2c, batch 4, recheck 3b; 22:13–22:14): #210 #211 #214–#218 #221 #223 #224 #227 (+ plaatshouders #205–#207)."""
    import fixlijst_g6 as FX, regels_g6 as R6
    FR = FX._FR
    from fractions import Fraction as Fr
    F = []; n = collections.Counter(); pos = collections.defaultdict(set); soort221 = collections.defaultdict(collections.Counter)
    for it in G:
        d = it['merge']['doel']; k = (d, it['merge'].get('somtypeNrOrigineel')); t = it['id']; o = it['opgave'] or ''; fh = it['foutHints']; a = it['antwoord']
        n['plaatshouders'] += sum('TEKST NODIG' in (f['uitleg'] or '') for f in fh)
        for r in it.get('foutRegels') or []:      # #223
            if a in ((r.get('match') or {}).get('waarden') or []): F.append(f"#223 {t}: antwoord {a} in de waarden van '{r['regel']}'")
        if (m := FX.KIES180.match(o)) and d == 'G6-GET-E03':      # #221
            w = m.group(1); br = re.findall(r'\d+/\d+', m.group(2)); n[f'221 {w}'] += 1; pos[w].add(br.index(a) + 1)
            if max(int(b.split('/')[1]) for b in br) > 20: F.append(f"#221 {t}: noemer > 20 ({o})")
            sn = 'zelfde noemer' if len({b.split('/')[1] for b in br}) == 1 else 'zelfde teller' if len({b.split('/')[0] for b in br}) == 1 else None
            if not sn:
                _, _, per = R6.niveau180(br, a, uitleg=True); sn = 'met ½' if any(g == 'vergelijken met ½' for _, g in per) else 'zelfde teller' if any(g == 'dezelfde teller' for _, g in per) else 'kgv ≤ 24 (veelvoud)'
            soort221[w][sn] += 1
        if k in (('G6-GET-E06', 3), ('G6-GET-E06', 7), ('G6-GET-E06', 1)) and (m := re.findall(r'\d+', o)) and len(m) >= 2:      # #210
            g1, g2 = int(m[0]), int(m[1]); dp = FR.deelproducten(g1, g2); av = int(a.replace('.', ''))
            for f in fh:
                if f['soort'] in (FX.R198[1], 'cijfers van het tweede getal opgeteld') and av - int(f['fout'].replace('.', '')) in dp: F.append(f"#210 {t}: {f['fout']} heet '{f['soort']}', maar antwoord − waarde is een deelproduct")
                if f['soort'] == FX.R198[1]: n['210 eenheden niet keer gedaan'] += 1
                if f['soort'] == 'cijfers van het tweede getal opgeteld': n['210 cijfers opgeteld'] += 1
            if t.endswith('E06-claude-bank-267'):
                s425 = [f['soort'] for f in fh if f['fout'] == '425']; n['210 267'] = 1
                if s425 != ['stuk vergeten']: F.append(f"#210 {t}: 425 heet {s425}, verwacht 'stuk vergeten'")
        if d == 'G6-MEET-E03':
            if (m := FX.RECHT211.search(o)) and re.fullmatch(r'\d+', a) and int(a) == int(m.group(1)) * int(m.group(3)):      # #211
                l, b = int(m.group(1)), int(m.group(3)); n['211 rechthoeken'] += 1
                if 2 * (l + b) == l * b: F.append(f"#211 {t}: omtrek = oppervlakte ({o})")
            if t.endswith('E03-claude-bank-285') and not (o.endswith('7 cm lang en 3 cm breed. Hoeveel cm² is de oppervlakte?') and a == '21'): F.append(f"#211 {t}: {o} → {a}")
            if k[1] == 1: n['218 e03 ' + o.split(' is ')[0]] += 1
        if k == ('G6-MEET-E03', 2) and (m := re.findall(r'\d+', o)):      # #214 / #216
            n['214 items'] += 1; g2 = m[1]
            s2 = [f['soort'] for f in fh if f['fout'] == g2]
            if g2 != a and s2 != ['zijde uit de vraag']: F.append(f"#214 {t}: {g2} heet {s2}")
            if g2 != a: n['214 sleutels'] += 1
            for f in fh:
                if (f['uitleg'] or '').startswith('Bijna!'):
                    n['216 Bijna'] += 1
                    if int(a) < 10: F.append(f"#216 {t}: 'Bijna!' bij antwoord {a}")
        if d in ('G6-MEET-E01', 'G6-MEET-E04', 'G6-MEET-E05'):      # #215
            for f in fh:
                if f['soort'] in (FX.R215[0][1], FX.R215[1][1]): n['215 nullen als factor'] += 1
                if f['soort'] == 'anders omgerekend': n['215 nog anders omgerekend'] += 1
                if '[' in (f['uitleg'] or '') and 'TEKST NODIG' not in f['uitleg']: F.append(f"#215 {t}: niet ingevuld: {f['uitleg']}")
        if k in (('G6-GET-E09', 2), ('G6-GET-E09', 3)) and (m := re.search(r'(\d+)/(\d+) van (?:de |het )?€?(\d+)\b', o)):      # #205
            tt, nn, tot = map(int, m.groups())
            if tt != 1 and tot % nn == 0:
                s1 = [f['soort'] for f in fh if f['fout'].lstrip('€') in (str(tot // nn),) or FR.geld_norm(f['fout']) == FR.geld_norm(f'€{tot // nn}')]
                if any(x == 'getal uit de vraag' for x in s1): F.append(f"#205 {t}: één stuk ({tot // nn}) heet 'getal uit de vraag'")
                if s1: n['205 één stuk'] += 1
        if k == ('G6-GET-E03', 6) and (m := re.search(r'(\d+)/(\d+)\b.*?\?/(\d+)', o)) and int(m.group(3)) % int(m.group(2)) == 0:      # #206
            fc = str(int(m.group(3)) // int(m.group(2))); s6 = [f['soort'] for f in fh if f['fout'] == fc]
            if fc != a and s6 and s6 != ['de factor']: F.append(f"#206 {t}: factor {fc} heet {s6}")
            if s6 == ['de factor']: n['206 factor'] += 1
        if k == ('G6-GET-M04', 2) and (m := re.findall(r'\d+', o)):      # #207
            g1, g2 = int(m[0]), int(m[1])
            for f in fh:
                v = int(f['fout']) if f['fout'].isdigit() else None
                if v is not None and g1 % g2 and g1 // g2 >= 2 and v == g1 % g2 and f['soort'] != 'de rest': F.append(f"#207 {t}: rest {v} heet {f['soort']}")
                if f['soort'] in ('de rest', 'steeds een hele eraf'): n[f"207 {f['soort']}"] += 1
                if f['soort'] in ('de rest', 'steeds een hele eraf') and (f['uitleg'] or '').startswith('Bijna!'): F.append(f"#207 {t}: Bijna! bij {f['soort']}")
        if it['bron']['claudeId'] == FX.ID189:      # #224
            w = [r for r in it['foutRegels'] if r.get('soort') == 'wat overblijft']
            if not w or (w[0]['match'] or {}).get('waarden') != ['20']: F.append(f"#224 {t}: 'wat overblijft' = {[(r['match'] or {}).get('waarden') for r in w]}")
        if it['merge'].get('zin201'):      # #227
            n['227'] += 1
            if it['visual'].get('nodig') or it['visual'].get('nietLiveZonderBeeld'): F.append(f"#227 {t}: visual nog nodig")
        if k == ('G6-MEET-E01', 7):      # #218
            n['218 strook'] += 1
            if not o.endswith('Hoeveel meter is dat samen?'): F.append(f"#218 {t}: {o}")
        if t.endswith('MEET-E01-claude-bank-114') and not {'3,80', '3,8'} <= {f['fout'] for f in fh}: F.append(f"#218 {t}: sleutels {[f['fout'] for f in fh]}")
    for w in ('kleinst', 'grootst'):
        if n[f'221 {w}'] < 25: F.append(f"#221 {w}: {n[f'221 {w}']} items (verwacht minstens 25)")
        if pos[w] != {1, 2, 3}: F.append(f"#221 {w}: antwoord niet op elke plek ({sorted(pos[w])})")
        if not soort221[w]['zelfde noemer']: F.append(f"#221 {w}: geen item met dezelfde noemer")
    if n['210 267'] != 1: F.append('#210: E06 267 niet gevonden')
    if n['214 items'] != 132: F.append(f"#214: {n['214 items']} items in MEET-E03 #2 (verwacht 132)")
    if n['227'] != 16: F.append(f"#227: {n['227']} items in E03 #5 (verwacht 16)")
    for dl, tl in FX.BORD217.items():      # #217
        pd = json.load(open(f'{BASE}/data/per_doel/{dl}.json'))
        if pd['bordtitel'] != tl or not pd.get('bordtitelBank'): F.append(f"#217 {dl}: bordtitel {pd['bordtitel']}")
    ctx = sorted((k_[8:], v) for k_, v in n.items() if k_.startswith('218 e03 '))
    INFO.append(f"ronde 7: {len(F)} FAIL · #221 kleinst {n['221 kleinst']} {dict(soort221['kleinst'])} · grootst {n['221 grootst']} {dict(soort221['grootst'])} · "
                f"#210 'eenheden niet keer gedaan' {n['210 eenheden niet keer gedaan']} sleutels, 'cijfers opgeteld' {n['210 cijfers opgeteld']} · #211 {n['211 rechthoeken']} rechthoeken nagekeken · "
                f"#214 {n['214 sleutels']} sleutels 'zijde uit de vraag' in {n['214 items']} items · #216 'Bijna!' {n['216 Bijna']} (alle bij antwoord ≥ 10) · "
                f"#215 {n['215 nullen als factor']} sleutels, nog 'anders omgerekend' {n['215 nog anders omgerekend']} · #205 één stuk {n['205 één stuk']} items · #206 {n['206 factor']} · "
                f"#207 rest {n['207 de rest']}, steeds een hele eraf {n['207 steeds een hele eraf']} · #227 {n['227']} · #218 strook {n['218 strook']}, E03 #1 contexten {ctx} · "
                f"plaatshouders (TEKST NODIG, Oefeningen) {n['plaatshouders']} sleutels")
    return F
INFO = []; VRAAG = {}

def ronde8(G):
    """ronde 8 (Dave 22:39–22:44): #219 lijngrafiek, #228/#230 contexten en notatie, #229 twee lagen, #251 niveau, #260 context bij de maat,
    #261 bordtitels, #263 geen regel zonder tekst. Telt ook (INFO8) de sleutels zonder tekstSterker (laag 2 = terugval op hint2)."""
    import fixlijst_g6 as FX
    F = []; n = collections.Counter(); kruis = collections.Counter()
    for it in G:
        d = it['merge']['doel']; k = (d, it['merge'].get('somtypeNrOrigineel')); t = it['id']; o = it['opgave'] or ''; fh = it['foutHints']
        for f in fh:      # #229: elke fout-hint heeft twee lagen
            n['229 sleutels'] += 1; n[f"229 laag2 {f.get('laag2')}"] += 1
            if 'uitlegSterker' not in f: F.append(f"#229 {t}: fout-hint {f['fout']} zonder uitlegSterker")
            elif it.get('hint') and not f['uitlegSterker']: F.append(f"#229 {t}: fout-hint {f['fout']}: laag 2 leeg")
        for r in it.get('foutRegels') or []:      # #263
            if r.get('leesbaar') and (r.get('tekst') is None or str(r.get('tekst')).strip() in ('', 'None')): F.append(f"#263 {t}: regel '{r['regel']}' zonder tekst")
            if k == ('G6-MEET-E01', 7) and 'nullen van de factor' in r['regel']: F.append(f"#263 {t}: nullenregel in E01 #7")
            if d == 'G6-VBN-E02' and r['regel'] == 'fout = antwoord : 10': F.append(f"#219 {t}: 'fout = antwoord : 10' staat er nog")
        if d == 'G6-VBN-E02':      # #219: elke regelsleutel op waarde nagerekend uit jsRender
            jr = it['visual']['jsRender'] or {}; pts = {p['naam'].lower(): p['waarde'] for p in jr.get('punten') or []}; ps = jr.get('perstreep'); co = jr.get('cijfer_om')
            gen = [m_ for m_ in sorted(pts, key=lambda x: o.lower().find(x)) if re.search(rf'\b{m_}\b', o.lower())]; a = int(it['antwoord'])
            for f in fh:
                v = int(f['fout']) if re.fullmatch(r'\d+', f['fout']) else None; r = f['regel']; n['219 sleutels'] += 1
                volg = list(pts); verw = {'fout = de tweede maand uit de vraag': {pts[max(gen, key=volg.index)]} if len(gen) > 1 else set(),      # #276: de latere maand
                        'fout = antwoord : perstreep': {a // ps} if ps and a % ps == 0 else set(),
                        'fout = antwoord + perstreep': {a + ps}, 'fout = antwoord − perstreep': {a - ps},
                        'fout = een andere maand': {w for m_, w in pts.items() if gen and m_ != gen[0]}, 'fout = het getal onder de stip': {pts[gen[0]] // co * co} if gen and co else set(),
                        'fout = alle maanden samen min één maand': {sum(pts.values()) - w for w in pts.values()}, 'fout = alle maanden samen plus één maand': {sum(pts.values()) + w for w in pts.values()},
                        'fout = de andere maand uit de vraag': {pts[min(gen, key=volg.index)]} if len(gen) > 1 else set(),      # ronde 9 (#333)
                        'fout = de som van een deel van de maanden': {sum(c_) for k_ in range(2, len(pts) - 1) for c_ in __import__('itertools').combinations(list(pts.values()), k_)}}.get(r)
                if verw is not None:
                    n[f'219 regel {r}'] += 1
                    if v not in verw: F.append(f"#219 {t}: {f['fout']} heet '{r}', verwacht {sorted(verw)}")
                if v == a: F.append(f"#219 {t}: sleutel = antwoord")
        if d == 'G6-MEET-E03' and (m := re.fullmatch(r'(?:(Een [a-z]+) is een rechthoek van|Een rechthoek is) (\d+) cm lang en (\d+) cm breed\. Hoeveel cm² is de oppervlakte\?', o)):      # #260
            ding = m.group(1); l, b = int(m.group(2)), int(m.group(3)); n[f'260 {ding or "rechthoek"}'] += 1
            if ding == 'Een placemat': F.append(f"#260 {t}: placemat")
            elif ding not in FX.MAAT260 or not FX.MAAT260[ding](l, b): F.append(f"#260 {t}: {ding} van {l} × {b} past niet bij de maat")
        if d in ('G6-VERH-E02', 'G6-VERH-E03'):      # #228/#230
            for w in ('poesje', 'knoop krijgt', 'een stap', 'stadion', 'groene eieren', "8 dino's. Welk deel van een tand"):
                if w in o: F.append(f"#228 {t}: '{w}' in de opgave")
            for x in [it['antwoord']] + [q['tekst'] for q in it.get('opties') or []] + [f['fout'] for f in fh]:
                if re.fullmatch(r'\d+\.\d{1,2}', str(x)) or re.match(r'(Een|De|Drie) (kwart|derde|helft|hele)\b', str(x)): F.append(f"#230 {t}: '{x}'")
        if d == 'G6-GET-E03' and (m := FX.VRAAG251.match(o)):      # #251
            br = [m.group(2), m.group(3), m.group(4)]; nv = FX.niveau251(br, it['antwoord'])
            kruis[(m.group(1), FX.ROUTE251[nv], it['niveau'])] += 1
            if (it['niveau'], it['niveauKind']) != FX.NIVEAU251[nv] or (it['merge'].get('niveau251') or {}).get('niveau') != nv: F.append(f"#251 {t}: niveau {it['niveau']} past niet bij route {FX.ROUTE251[nv]}")
    for dl, tl in FX.BORD261.items():      # #261
        pd = json.load(open(f'{BASE}/data/per_doel/{dl}.json'))
        if pd.get('bordtitel') != tl: F.append(f"#261 {dl}: bordtitel '{pd.get('bordtitel')}'")
    INFO8.clear(); INFO8.update(n); INFO8.update({f'251 {k_}': v_ for k_, v_ in kruis.items()})
    return F
INFO8 = collections.Counter()

def ronde9(G):
    """ronde 9 (8 okt): #331 guard op de data (opgeteld nooit het antwoord of een goed vakje), #231 aantallen, #276 bordtitel en streepjes, #332, #333, #321, #235."""
    import fixlijst_g6 as FX
    F = []; tel = collections.Counter()
    kop1 = next((it['merge']['somtype'] for it in G if it['bron'].get('claudeId', '').startswith('63102a04')), None)
    for it in G:
        d = it['merge']['doel']; t = it['id']; fh = it['foutHints']
        tel[(d, it['merge']['somtype'])] += 1
        if d == 'G6-VERH-E01' and it['merge']['somtype'] == kop1:      # V-#331 / les 90
            x1, y1, x2, ans, vak, routes = FX.verh331(it)
            if ans != y1 * x2 / x1: F.append(f"#331 {t}: antwoord past niet bij de tabel")
            if x2 < x1: F.append(f"#331 {t}: terug in de tabel zonder regel 'eraf'")
            for naam, v in routes.items():
                if v == ans or v in vak: F.append(f"#331 {t}: route {naam} = {v} is het antwoord of een goed vakje")
            for f in fh:
                if f.get('soort') == 'opgeteld' and (FX._waarde(f['fout']) in vak or FX._waarde(f['fout']) == ans): F.append(f"#331 {t}: opgeteld-sleutel {f['fout']} is een goed vakje")
        if d == 'G6-VBN-E02':
            jr = it['visual']['jsRender'] or {}; pts = [(p['naam'].lower(), p['waarde']) for p in jr.get('punten') or []]; o = it['opgave'].lower()
            gen = [w for _, _, w in sorted((o.find(n), n, w) for n, w in pts if re.search(rf'\b{n}\b', o))]
            if ' meer dan ' in o:      # #332 / V-#330
                if len(gen) != 2 or not gen[0] > gen[1]: F.append(f"#332 {t}: de eerste maand uit de vraag is niet de grootste")
                if int(it['antwoord']) in gen: F.append(f"#332 {t}: antwoord = de waarde van een maand uit de vraag")
                for f in fh:
                    if f['fout'].isdigit() and int(f['fout']) in gen and f['regel'] not in ('fout = de tweede maand uit de vraag', 'fout = de andere maand uit de vraag', 'Claudes sleutel: getal-overgenomen'):
                        F.append(f"#333 {t}: {f['fout']} is een maand uit de vraag maar heet '{f['soort']}'")
            if 'alle maanden samen' in o:
                ws = [w for _, w in pts]; deel = {sum(c_) for k_ in range(2, len(ws) - 1) for c_ in __import__('itertools').combinations(ws, k_)}
                for f in fh:
                    if f['regel'] == 'andere fout' and f['fout'].isdigit() and int(f['fout']) in deel: F.append(f"#333 {t}: {f['fout']} is een som van een paar maanden maar heet 'andere fout'")
        if d == 'G6-GET-E06' and it['merge'].get('uitG5'):
            if not it.get('hint') or not it.get('sterkereHint') or not it.get('ouderzin'): F.append(f"#321 {t}: zonder H1/H2/ouderzin")
            if not fh: F.append(f"#321 {t}: zonder fout-hints")
        if d == 'G6-MKU-E01' and it['merge']['somtype'] in FX.KOP235: F.append(f"#235 {t}: nog onder '{it['merge']['somtype']}'")
    for (d, k), n in tel.items():
        if d in ('G6-VERH-E01', 'G6-VERH-E02') and k == kop1 and not 12 <= n <= 18: F.append(f"#231/#382 VERH-E01 #1: {n} items (12–18)")
    for dl, tl in FX.BORD276.items():
        pd = json.load(open(f'{BASE}/data/per_doel/{dl}.json'))
        if pd.get('bordtitel') != tl: F.append(f"#276 {dl}: bordtitel '{pd.get('bordtitel')}'")
        if re.search(r'beelddiagram|cirkeldiagram', pd.get('bordtitel') or '', re.I) and pd.get('bordtitel') != getattr(FX, 'BORD_N13', {}).get(dl): F.append(f"#276 {dl}: bordtitel noemt beeld-/cirkeldiagram")      # r13 N13-1: bewust (lege plekken N13-3 wachten op Oefeningen)
    st = collections.Counter(int(it['antwoord']) // it['visual']['jsRender']['perstreep'] for it in G if it['merge']['doel'] == 'G6-VBN-E02' and ' meer dan ' in it['opgave'])
    if st and (sorted(st) != [1, 2, 3, 4, 5] or max(st.values()) - min(st.values()) > 1): F.append(f"#276 VBN-E02 #1: streepjes niet gelijk verdeeld {dict(st)}")
    INFO9.clear(); INFO9.update({'276 streepjes ' + str(k): v for k, v in st.items()})
    # #532 (eindcheck G6 r11): GET-E04 069/078 'honderd te veel' met overdracht via een 9 → de tekst met overdracht
    import fixlijst_g6 as _FL532, copy as _cp532
    F += _FL532.guard532(G)
    INFO.append(f"#550 'honderd/tien te veel' nagerekend: {_FL532.guard532.gecontroleerd} sleutels")
    # #550 mutatietest: verwissel bij een item met overdracht (066 als die er is) de tekst met die zonder overdracht; de guard moet dat vangen
    _m = _cp532.deepcopy([it for it in G if it['merge'].get('doel') == 'G6-GET-E04'])
    _doel = next((it for it in _m if it['id'].endswith('-066')), None) or next((it for it in _m if any('(met overdracht' in (f.get('regel') or '') for f in it['foutHints'])), None)
    if _doel:
        _fm = next(f for f in _doel['foutHints'] if '(met overdracht' in (f.get('regel') or ''))
        _fz = next((f for it in _m for f in it['foutHints'] if '(zonder overdracht' in (f.get('regel') or '')), None)
        if _fz: _fm['uitleg'] = _fz['uitleg']
        if not _fz or not any(_doel['id'] in x for x in _FL532.guard532(_m)): F.append(f"#550 mutatietest: een verwisselde tekst bij {_doel['id']} wordt niet gevangen")
    return F
INFO9 = collections.Counter()

if __name__ == '__main__':
    F = run(); print(f"FIX6 (G6-fixlijst #1–#6 na de build): {len(F)} (FAIL)")
    for x in F[:20]: print('  FAIL FIX6', x)
    for x in INFO: print('  INFO FIX6', x)
    for k, v in sorted(INFO9.items()): print('  INFO FIX6', k, v)
    sys.exit(1 if F else 0)
