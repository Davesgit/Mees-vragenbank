#!/usr/bin/env python3
"""G6-regels voor de Claude-merge (1 okt 2026, Overzicht): mapping per item (classify_g6), G6-bewerkingen (bewerk_g6),
herverificatie op de bewerkte vorm (verify_g6) en notatiecheck (notatie_check_g6).
Wordt geïmporteerd door build_g6.py; schrijft zelf niets.
Grenzen (spine G6, exports/vragenbank_alles.json): hele getallen tot 100.000 (GET-M01/E01), +/− en ×/: tot 10.000 (GET-E04/E06),
×/: opbouw 1×2/3-cijferig en 2–3 : 1-cijferig (GET-M06), kommagetallen met 1–2 cijfers (GET-M03/E02), breuken: notatie, vergelijken,
maatverfijning, aanvullen en deel ván (GET-M04/E03/E09, VERH-E02). Wat G5 al kan → terug-G5 (g5/data/aanvulling_uit_g6.json);
procent, verhoudingsnotatie 'a : b' en schaal '1 : 100', inhoud in cm³, kommagetallen met 3 cijfers en sommen boven 10.000 → park-G7.
Notatie (besluit Dave): ':' is het deelteken; een verhouding schrijf je in G6 niet als '4 : 5' (dat is G7-VERH-03); ketensommen voluit."""
import re, copy
from fractions import Fraction as Fr

R5 = None; R4 = None            # gezet door build_g6.py (g5_basis/regels_g5.py en g4_basis_1435/regels_g4.py)

def ints(s):
    s = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1\2', str(s)); s = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1\2', s)
    return [int(x) for x in re.findall(r'(?<!\d)(?<!\d,)\d+(?!\d)(?!,\d)', s)]

def getallen(s):
    s = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1\2', str(s)); s = re.sub(r'(\d)\.(\d{3})(?!\d)', r'\1\2', s)
    return [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:,\d+)?', s)]

def mx(q):
    n = getallen(q['vraag']) + getallen(str(q['antwoord']).replace(',', '') if re.fullmatch(r'\d{1,3}(,\d{3})+', str(q['antwoord'])) else str(q['antwoord']))
    return max(n) if n else 0

def decimalen(s):
    return max([len(x) for x in re.findall(r'\d,(\d+)', str(s))] or [0])

def breuken(s):
    return [(int(a), int(b)) for a, b in re.findall(r'(?<![\d/])(\d+)/(\d+)(?![\d/])', str(s))]

def R(status, doel, regel, reden, cat=None, aanvulling=False):
    return dict(status=status, doel=doel, regel=regel, reden=reden, cat=cat, aanvulling=aanvulling)
G = lambda d, r, why: R('gemapt', d, r, why)
T = lambda d, r, why, cat: R('twijfel', d, r, why, cat)
P7 = lambda d, r, why: R('park-G7', d, r, why)
def T5(d, r, why): return R('terug-G5', d, r, why, aanvulling=d.startswith('G5'))

GROOT = 100000; REKEN = 10000

def g5_doel(q, regel, why):
    """te makkelijk voor G6: welk G5-doel? (G5-regels; geeft de G5-merge een G4-doel, dan blijft dat het voorstel)"""
    r = R5.classify_g5(q, None, R4) if R5 else {'status': 'niet'}
    if r['status'] in ('gemapt', 'twijfel') and (r['doel'] or '').startswith('G5'): return T5(r['doel'], regel, f"{why} → {r['doel']} ({r['reden']})")
    if r['status'] == 'terug-G4': return T5(r['doel'], regel, f"{why}; G5-regels zeggen zelfs {r['doel']} ({r['reden']})")
    return None

# ---------------------------------------------------------------- stap 2: mapping per item
def niveau180(breuken_, antwoord, uitleg=False):
    """G6 merge-fixlijst #180 (Didactiek batch 3, 21:42; aangescherpt 22:08): elke vergelijking van het antwoord met een andere breuk moet op G6-niveau kunnen.
    - kgv van de noemers ≤ 24 (dezelfde noemer of een noemer die een veelvoud is valt hieronder zolang de grootste noemer ≤ 24 is);
    - kgv > 24 mag alleen bij (a) 'dezelfde teller': de tellers zijn gelijk en beide noemers ≤ 20, of (b) 'vergelijken met ½': de een duidelijk onder ½ en
      de ander duidelijk boven ½, geen van beide precies ½, beide noemers ≤ 20. 'Duidelijk' (Didactiek 22:14, #221b): |breuk − ½| ≥ 1/20 en 2·teller ≠ noemer
      (7/16 en 9/20 mogen).
    - #221 (Didactiek 3b): geen noemer boven 20 in de keuze (ook niet bij kgv ≤ 24).
    -> (ok, reden) of met uitleg=True (ok, reden, [(breuk, geval)])."""
    from math import lcm
    from fractions import Fraction as _F
    ta, na = (int(x) for x in antwoord.split('/')); per = []
    if (gr := max(int(b_.split('/')[1]) for b_ in list(breuken_) + [antwoord])) > 20:
        r = (False, f'noemer {gr} > 20')
        return r + (per,) if uitleg else r
    duidelijk = lambda t, n: 2 * t != n and abs(_F(t, n) - _F(1, 2)) >= _F(1, 20)
    for b_ in breuken_:
        if b_ == antwoord: continue
        tb, nb = (int(x) for x in b_.split('/')); k = lcm(na, nb)
        if k <= 24: per.append((b_, 'kgv ≤ 24')); continue
        if ta == tb and na <= 20 and nb <= 20: per.append((b_, 'dezelfde teller')); continue
        d1, d2 = 2 * ta - na, 2 * tb - nb
        if d1 * d2 < 0 and duidelijk(ta, na) and duidelijk(tb, nb) and na <= 20 and nb <= 20: per.append((b_, 'vergelijken met ½')); continue
        r = (False, f'{antwoord} tegen {b_}: kgv {k}')
        return r + (per,) if uitleg else r
    return (True, '', per) if uitleg else (True, '')

def classify_g6(q, park5=None):
    t, Bd = q['vraag'], (q.get('beeld') or {}); soort, vorm, cd = Bd.get('soort'), q['vorm'], q['doel']
    a = str(q['antwoord']); n = ints(t); M = mx(q)

    # --- getallen tot 100.000 (C11)
    if cd == 'C11':
        if M > GROOT: return P7('G7-GET-01', 'G6-G01-grote-getallen', f'getal boven 100.000 ({int(M):,}): G7-GET-01 (tot 1 miljoen)'.replace(',', '.'))
        if re.search(r'Rond \S+ af op', t): return G('G6-GET-E01', 'G6-G02-afronden', 'afronden tot 100.000 (G6-GET-E01)')
        if vorm == 'getallenlijn': return G('G6-GET-E01', 'G6-G03-getallenlijn', 'getal op de getallenlijn tot 100.000 (G6-GET-E01: ordenen)')
        if re.search(r'grootste getal|kleinste getal|grootst|kleinst', t): return G('G6-GET-E01', 'G6-G04-vergelijken', 'getallen vergelijken tot 100.000 (G6-GET-E01)')
        if re.search(r'wordt \S+\. Met hoeveel verandert', t) or re.search(r'Hoeveel is de \d in dit getal waard', t):
            return G('G6-GET-M02', 'G6-G05-positiewaarde', 'positiewaarde tot tienduizendtallen (G6-GET-M02)')
        if re.search(r'\d+ (meer|minder) dan', t) or 'Er komt er één bij' in t:
            return G('G6-GET-M02', 'G6-G06-sprongen', 'sprongen en telrij tot 100.000 (G6-GET-M02)')
        return G('G6-GET-M01', 'G6-G07-lezen', 'getallen tot 100.000 lezen en schrijven (G6-GET-M01)')

    # --- cijferen
    if cd == 'C12':
        if M <= 1000: return g5_doel(q, 'G6-C01-cijferend-plus', 'optellen onder elkaar tot 1000 (kolom/cijferen staat in G5-GET-E05)') or T5('G5-GET-E05', 'G6-C01-cijferend-plus', 'optellen tot 1000: G5-GET-E05')
        return G('G6-GET-E04', 'G6-C01-cijferend-plus', 'cijferend optellen tot 10.000 (G6-GET-E04)') if M <= REKEN else P7('G7-GET-03', 'G6-C01-cijferend-plus', 'boven 10.000: G7-GET-03')
    if cd in ('C13', 'C14'):
        if M <= 1000: return g5_doel(q, 'G6-C02-cijferend-min', 'aftrekken tot 1000') or T5('G5-GET-E05', 'G6-C02-cijferend-min', 'aftrekken tot 1000: G5-GET-E05')
        if M <= REKEN: return G('G6-GET-E04', 'G6-C02-cijferend-min', 'aftrekken tot 10.000' + (' (lenen over een nul)' if cd == 'C14' else '') + ' (G6-GET-E04)')
        return P7('G7-GET-03', 'G6-C02-cijferend-min', f'aftrekken boven 10.000 (tot {int(M):,}): G7-GET-03'.replace(',', '.'))
    if cd == 'C15':
        if M <= REKEN: return G('G6-GET-E06', 'G6-C03-keer-2x2', '2-cijferig × 2-cijferig tot 10.000 (G6-GET-E06)')
        return P7('G7-GET-04', 'G6-C03-keer-2x2', 'product boven 10.000: G7-GET-04')
    if cd == 'C16':
        d = n[1] if len(n) > 1 else 0
        if n and n[0] <= 1000 and d <= 9: return G('G6-GET-M06', 'G6-C04-delen-happen', f'{n[0]} : {d}: 3-cijferig gedeeld door 1-cijferig, met happen (G6-GET-M06: opbouw)')
        return G('G6-GET-E06', 'G6-C04-delen-happen', 'delen tot 10.000 (G6-GET-E06)') if M <= REKEN else P7('G7-GET-04', 'G6-C04-delen-happen', 'boven 10.000')
    if cd == 'C17': return G('G6-GET-M05', 'G6-C05-deelbaar', 'deelbaar door 2, 3, 4, 5, 9 of 10: deeltafels uit je hoofd (G6-GET-M05)')

    # --- breuken
    if cd == 'B1':
        if vorm == 'balk' or re.search(r'Kleur \d+/\d+', t): return G('G6-VERH-E02', 'G6-B01-deel-geheel', 'een breuk van een balk kleuren: breuk als deel van een geheel (G6-VERH-E02)')
        return G('G6-GET-M04', 'G6-B02-notatie', 'welk deel? antwoord als breuk: teller en noemer (G6-GET-M04)')
    if cd == 'B2':
        if re.match(r'Hoeveel is \d+/\d+ van', t): return G('G6-GET-E09', 'G6-B03-deel-van', 'a/b ván een getal of bedrag: breuk als operator (G6-GET-E09)')
        return G('G6-VERH-E02', 'G6-B04-deel-hoeveelheid', 'breuk als deel van een hoeveelheid of geheel (G6-VERH-E02)')
    if cd == 'B3': return G('G6-GET-E03', 'G6-B05-gelijkwaardig', 'gelijkwaardige breuken: maatverfijning (G6-GET-E03)')
    if cd == 'B5':
        if (m := re.search(r'(grootst|kleinst)', t)) and len(f := re.findall(r'\d+/\d+', t)) >= 2 and re.fullmatch(r'\d+/\d+', a.strip()):
            ok, why = niveau180(f, a.strip())
            if not ok: return P7('G7-GET-05', 'G6-B06-vergelijken-niveau180', f'breuken vergelijken met gelijknamig maken boven G6-niveau ({why}): G7-GET-05 (Didactiek batch 3, #180)')
        return G('G6-GET-E03', 'G6-B06-vergelijken', 'breuken vergelijken, ordenen, op de getallenlijn (G6-GET-E03)')
    if cd == 'B6':
        if re.search(r'met noemer \d+', t): return G('G6-GET-E03', 'G6-B07-noemer', 'breuk met een andere noemer schrijven: maatverfijning (G6-GET-E03)')
        return P7('G7-GET-05', 'G6-B08-plus-ongelijk', 'breuken met verschillende noemers optellen: G7-GET-05')
    if cd in ('B7', 'B8'):
        f = breuken(t)
        if len(f) >= 2 and len({b for _, b in f}) == 1:
            tot = Fr(f[0][0], f[0][1]) + (Fr(f[1][0], f[1][1]) if cd == 'B7' else -Fr(f[1][0], f[1][1]))
            if 0 <= tot <= 1:
                return T('G6-GET-E09', 'G6-B09-plus-min-gelijk', 'breuken met dezelfde noemer optellen/aftrekken (uitkomst ≤ 1): staat niet letterlijk in de G6-spine; het dichtst bij is GET-E09 (aanvullen tot 1)', 'breuken-plus-min')
        return P7('G7-GET-05', 'G6-B08-plus-ongelijk', 'breuken optellen/aftrekken met andere noemers of boven 1: G7-GET-05')
    if cd == 'B9': return G('G6-GET-E03', 'G6-B10-vereenvoudigen', 'breuk zo eenvoudig mogelijk: maatverfijning andersom (G6-GET-E03)')
    if cd == 'B10': return G('G6-GET-M04', 'G6-B11-gemengd', 'gemengde getallen en samengestelde breuken (G6-GET-M04)')
    if cd == 'B11': return G('G6-GET-M03', 'G6-B12-breuk-komma', 'breuk als kommagetal (tienden, honderdsten) en op de lijn (G6-GET-M03)')
    if cd == 'B14' and re.search(r'\d+/\d+ (?:deel )?van (?:de |het |een )?(?:€ ?)?\d', t):     # Dave 16:11: uit de G7-pool naar G6-GET-E09
        return G('G6-GET-E09', 'G6-B14-operator', 'a/b ván een hoeveelheid: breuk als operator (G6-GET-E09; Claude zette dit in G7 B14)')
    if cd == 'B18': return G('G6-VERH-E03', 'G6-B13-breuk-deling', 'eerlijk verdelen: de breuk als deling (G6-VERH-E03)')

    # --- kommagetallen (G5-park)
    if cd == 'B4':
        if decimalen(t) > 2: return P7('G7-GET-02', 'G6-K01-komma-3', f'kommagetallen met {decimalen(t)} cijfers achter de komma: G7-GET-02 (t/m 3 decimalen)')
        return G('G6-GET-M03', 'G6-K02-komma-vergelijken', 'kommagetallen (1–2 cijfers) vergelijken (G6-GET-M03)')
    if cd == 'B12':
        if vorm == 'getallenlijn': return G('G6-GET-M03', 'G6-K03-komma-lijn', 'kommagetal op de getallenlijn (G6-GET-M03)')
        if re.search(r'Rond af op één cijfer achter de komma', t): return P7('G7-GET-02', 'G6-K01-komma-3', 'afronden van 3 cijfers achter de komma: G7-GET-02')
        if 'kg' in t: return G('G6-MEET-E01', 'G6-K04-meetgetal', 'meetgetallen met komma optellen (G6-MEET-E01)') if decimalen(t) <= 2 else P7('G7-MEET-03', 'G6-K04-meetgetal', '3 decimalen')
        if '€' in t: return G('G6-GET-V02', 'G6-K05-geld', "euro's met komma: plus en min (G6-GET-V02)")
        return P7('G7-GET-03', 'G6-K06-komma-plusmin', 'kommagetallen optellen/aftrekken zonder geld: G7-GET-03 (G6-GET-E02 is splitsen, niet rekenen)')

    # --- procent, inhoud, schaal, oppervlakte
    if cd == 'V1': return P7('G7-VERH-02', 'G6-V01-procent', 'procent: G7-VERH-02 (de G6-spine heeft geen procent)')
    if cd == 'M17': return G('G6-MEET-E03', 'G6-M01-oppervlakte', 'oppervlakte rechthoek met de formule l × b (G6-MEET-E03)') if M <= REKEN else P7('G7-MEET-02', 'G6-M01-oppervlakte', 'groot')
    if cd == 'M18': return P7('G7-MEET-03', 'G6-M02-inhoud-cm3', 'inhoud in kubieke cm (l × b × h): G7-MEET-03; de G6-spine heeft alleen L/dl/cl (MEET-E04)')
    if cd == 'M19': return P7('G7-VERH-03', 'G6-M03-schaal', "schaal in de notatie '1 : 100' = verhoudingsnotatie: G7-VERH-03 (besluit Dave: 'a : b' als verhouding pas in G7)")

    # --- maten (G5-park)
    m = re.match(r'(?:Vul in: )?([\d.]+) (km|hm|dam|m|dm|cm|mm|L|l|dl|cl|ml|kg|g) = (?:□|\.\.\.) (km|hm|dam|m|dm|cm|mm|L|l|dl|cl|ml|kg|g)\b', t)
    if m and cd in ('M9', 'M11', 'M12', 'M13', 'M20'):
        e1, e2 = m.group(2), m.group(3); big = M
        lengte = {'km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'}; inhoud = {'L', 'l', 'dl', 'cl', 'ml'}
        if e1 in lengte: d6, d7 = 'G6-MEET-E01', 'G7-MEET-01'
        elif e1 in inhoud: d6, d7 = 'G6-MEET-E04', 'G7-MEET-03'
        else: d6, d7 = 'G6-MEET-E05', 'G7-MEET-03'
        if big > GROOT: return P7(d7, 'G6-M04-herleiden', f'{m.group(1)} {e1} = □ {e2}: boven 100.000 ({d7})')
        return G(d6, 'G6-M04-herleiden', f'{e1} ↔ {e2} herleiden ({d6})')

    # --- getallen, sommen (G5-park C7/T9/C10)
    if cd == 'C10':
        if M > GROOT: return P7('G7-GET-01', 'G6-G02-afronden', 'boven 100.000')
        return G('G6-GET-E01', 'G6-G02-afronden', 'afronden van getallen boven 1000 (G6-GET-E01)')
    if cd in ('C7', 'T9', 'D5-6', 'D5-9', 'C9', 'C8'):
        mm = re.fullmatch(r'(\d+) × (\d+) =', t.strip())
        x, y = (int(mm.group(1)), int(mm.group(2))) if mm else ((n[0], n[1]) if len(n) >= 2 else (0, 0))
        p = int(a) if a.isdigit() else x * y
        if ':' in a or ' : ' in t or 'eerlijk' in t:
            return G('G6-GET-E06', 'G6-C06-deel', 'delen boven 1000 (G6-GET-E06)') if M <= REKEN else P7('G7-GET-04', 'G6-C06-deel', 'boven 10.000')
        if p > REKEN: return P7('G7-GET-04', 'G6-C07-keer', f'product {p} boven 10.000: G7-GET-04')
        if min(x, y) <= 9: return G('G6-GET-M06', 'G6-C07-keer', f'{x} × {y}: 1-cijferig keer 2/3-cijferig tot 10.000 (G6-GET-M06: opbouw)')
        return G('G6-GET-E06', 'G6-C07-keer', 'keer tot 10.000 (G6-GET-E06)')

    # --- meetkunde, grafieken, gemiddelde
    if cd == 'K10': return G('G6-MKU-E01', 'G6-R01-kijklijn', 'kijklijn op de kaart met vakjes (G6-MKU-E01: roostercoördinaten)')
    if cd == 'G3':
        if soort == 'lijngrafiek': return G('G6-VBN-E02', 'G6-D01-lijngrafiek', 'lijngrafiek aflezen (G6-VBN-E02)')
        if 'Tabel van' in t and M <= 100: return g5_doel(q, 'G6-D02-tabel', 'tabel aflezen met kleine getallen') or T5('G5-VBN-E01', 'G6-D02-tabel', 'tabel aflezen (G5-VBN-E01)')
        return G('G6-VBN-E02', 'G6-D03-grafiek', 'grafiek of diagram aflezen (G6-VBN-E02)')
    if cd == 'G4': return G('G6-GET-E08', 'G6-D04-gemiddelde', 'gemiddelde in een eenvoudige situatie (G6-GET-E08)')

    # --- handig rekenen, wiskundetaal, denkwerk
    if cd == 'T10':
        if re.search(r'Reken uit het hoofd', t): return G('G6-GET-M05', 'G6-T01-hoofd', 'ronde getallen tot 10.000 uit het hoofd (G6-GET-M05)')
        if mk := re.search(r'^(\d+) [\wà-ÿ]+ (?:met|van elk) (€ ?)?(\d+)\b', t):
            x, y = int(mk.group(1)), int(mk.group(3))
            if mk.group(2): return G('G6-GET-E07', 'G6-T03-handig-keerdeel', f'{x} × €{y} handig (G6-GET-E07: keer met euro’s)')
            if x * y <= 1000: return T5('G5-GET-E07', 'G6-T03-handig-keerdeel', f'{x} × {y} handig uitrekenen: strategieën tot 1000 (G5-GET-E07)')
            return G('G6-GET-E06', 'G6-T03-handig-keerdeel', 'handig keer tot 10.000 (G6-GET-E06: strategieën)')
        mm = re.search(r'(\d+) ([+\-−×:]) (\d+)', t)
        if mm:
            x, op, y = int(mm.group(1)), mm.group(2), int(mm.group(3))
            if op in '+-−':
                if max(x, y, x + y) <= 1000: return T5('G5-GET-E05', 'G6-T02-handig-plusmin', f'{x} {op} {y} handig uitrekenen: strategieën tot 1000 (G5-GET-E05)')
                return G('G6-GET-E04', 'G6-T02-handig-plusmin', 'handig optellen/aftrekken tot 10.000 (G6-GET-E04: strategieën)')
            pr = x * y if op == '×' else x
            if pr <= 1000: return T5('G5-GET-E07', 'G6-T03-handig-keerdeel', f'{x} {op} {y} handig uitrekenen: strategieën tot 1000 (G5-GET-E07)')
            return G('G6-GET-E06', 'G6-T03-handig-keerdeel', 'handig keer/delen tot 10.000 (G6-GET-E06: strategieën)')
    if cd == 'W2':
        if re.search(r'\bteller\b|\bnoemer\b', t + ' ' + a): return G('G6-GET-M04', 'G6-W01-teller-noemer', 'teller en noemer benoemen (G6-GET-M04)')
        return P7('G7-DENK-04', 'G6-W02-wiskundetaal', 'wiskundewoorden (verschil, quotiënt, term, product): G7-DENK-04')
    if cd == 'W4':
        if re.search(r'verhoudingstabel|In een tabel staat', t): return G('G6-VERH-E01', 'G6-W03-schema-tabel', 'situatie in een verhoudingstabel (G6-VERH-E01)')
        if re.search(r'strook', t) and re.search(r'\bkm\b|meter', t): return G('G6-MEET-E01', 'G6-W04-schema-strook', 'afstanden in km en m als één strook: km ↔ m (G6-MEET-E01)')
        if re.search(r'strook', t): return G('G6-VERH-E02', 'G6-W04-schema-strook', 'situatie als strook: deel van een geheel (G6-VERH-E02)')
        return P7('G7-DENK-02', 'G6-W05-schema', 'een situatie in een schema of som zetten: G7-DENK-02 (modelleren)')
    if cd == 'W5': return P7('G7-DENK-03', 'G6-W06-stappen', 'een stappenreeks (algoritme) volgen: G7-DENK-03')

    # --- G5-park met voorstel (vangnet)
    if park5: return G(park5['merge']['voorstelDoel'], 'G6-X01-g5-voorstel', f"voorstel van de G5-merge ({park5['merge']['reden']})")
    return R('niet', None, 'G6-X99', 'geen G6-regel van toepassing')

# ---------------------------------------------------------------- stap 2b: G6-bewerkingen (na de G3-, G4- en G5-regels)
KETEN2 = re.compile(r'(?<![\d,.])(\d[\d.,]*) ([+−×:]) (\d[\d.,]*) = (\d[\d.,]*) ([+−×:]) (\d[\d.,]*) = (\d[\d.,]*)')

def _zet(it, veld, nieuw, slog, soort):
    oud = it[veld]
    if oud != nieuw: slog(it, soort, veld, oud, nieuw); it[veld] = nieuw

KIES = re.compile(r'^(Welke? (?:breuk|getal|kommagetal|bedrag) is het (?:grootst|kleinst))\. ((?:[\d/.,€]+, )+[\d/.,€]+ of [\d/.,€]+)\?$')
def bewerk_g6(it, q, M3, log, slog):
    if m := KIES.match(it['opgave']):     # G3-N1 maakte van 'kleinst: 3/4, …?' 'kleinst. 3/4, …?'
        _zet(it, 'opgave', f'{m.group(1)}? Kies uit {m.group(2)}.', slog, 'G6-N2 keuzelijst na de vraag (\'Kies uit …\')')
    ex = it['extraVelden']; o = it['opgave']
    # 4 cijfers zonder punt, ook vóór een zinseinde ('er 8.265.'): de G3-regel F2b sloeg die over
    M3.sub_all(it, 'G6-F2c 4 cijfers zonder punt (ook aan het eind van een zin)', r'(?<![\d.,€])(\d)\.(\d{3})(?!\d|[.,]\d)', r'\1\2', log)
    for veld in ('antwoord',):
        if isinstance(it[veld], str) and re.fullmatch(r'\d\.\d{3}', it[veld]): _zet(it, veld, it[veld].replace('.', ''), slog, 'G6-F2c 4 cijfers zonder punt (ook aan het eind van een zin)')
    for f in it['foutHints']:
        if isinstance(f['fout'], str) and re.fullmatch(r'\d\.\d{3}', f['fout']): f['fout'] = f['fout'].replace('.', '')
    o = it['opgave']
    # 'verdelen in groepjes van 10: 150, 154, 144, 156?' (':' na een getal leest als deelteken) → keuzelijst eerst
    if m := re.fullmatch(r'Welk aantal ([\wà-ÿ]+) kun je precies verdelen in groepjes van (\d+): ((?:\d+, )+)(\d+)\? Typ dat getal\.', o):
        _zet(it, 'opgave', f'Je kunt kiezen uit {m.group(3)[:-2]} en {m.group(4)}. Welk aantal {m.group(1)} kun je precies verdelen in groepjes van {m.group(2)}? Typ dat getal.', slog, "G6-N4 keuzelijst vóór de vraag (geen ':' na een getal)"); o = it['opgave']
    # 'een andere konijn' → 'een ander konijn' (het-woord)
    M3.sub_all(it, "G6-F1 'een ander' bij een het-woord", r'\b([Ee]en) andere (?=(?:konijn|kind|paard|schaap|varken|kalf|hert|dier|\w+je)\b)', r'\1 ander ', log); o = it['opgave']
    # liter = L ook na □ ('22.000 cl = □ l'), zoals N10 na een getal
    M3.sub_all(it, 'G6-N3 liter = L (ook na □)', r'(?<=[□\d]) l\b', ' L', log); o = it['opgave']
    # 'Kleur 1/3 deel van de koekjes' → 'Kleur 1/3 van de koekjes'
    M3.sub_all(it, "G6-W3 'Kleur 1/3 deel van' → 'Kleur 1/3 van'", r'\b(Kleur \d+/\d+) deel van\b', r'\1 van', log, {'opgave'}); o = it['opgave']
    # gemengd getal van dingen ('3 2/8 stappen. Hoeveel 8-de delen…') → kale omzetting
    if m := re.fullmatch(r'(\d+) (\d+)/(\d+) [\wà-ÿ\'’-]+\. Hoeveel [\wà-ÿ-]+ (?:delen )?zijn dat in totaal\? \(Typ alleen de teller van \?/(\d+)\.\)', o):
        _zet(it, 'opgave', f'{m.group(1)} {m.group(2)}/{m.group(3)} = ?/{m.group(4)}. Welk getal hoort op het vraagteken?', slog, 'G6-W4 gemengd getal zonder rare dingen (3 2/8 stappen)'); o = it['opgave']
    # '15/4 stappen. Hoeveel hele stappen…' → pizza (een breuk van iets dat je kunt verdelen)
    if m := re.fullmatch(r'(\d+)/(\d+) [\wà-ÿ\'’-]+\. Hoeveel hele [\wà-ÿ\'’-]+ zijn dat, met nog iets over\? Typ het hele getal\.', o):
        x, y = int(m.group(1)), int(m.group(2))
        _zet(it, 'opgave', f"Je hebt {x}/{y} pizza. Hoeveel hele pizza's zijn dat?" + (' Er blijft ook nog een stuk over.' if x % y else '') + " Typ alleen het aantal hele pizza's.", slog, "G6-W5 breuk groter dan 1: pizza's in plaats van rare dingen"); o = it['opgave']
    # '3/5 van een vis is hetzelfde als een deelsom' → 'De breuk 3/5 is hetzelfde als een deelsom'
    if m := re.match(r'(\d+/\d+) van een [\wà-ÿ\'’-]+ is hetzelfde als een deelsom\.', o):
        _zet(it, 'opgave', 'De breuk ' + m.group(1) + o[m.end() - len(' is hetzelfde als een deelsom.'):], slog, "G6-W6 breuk als deling zonder ding ('3/5 van een vis')"); o = it['opgave']
    # 'In een verhoudingstabel staat. 2 kg appels kost 3 euro.' (G3-N1 maakte van ':' een punt)
    if m := re.match(r'In een (verhoudingstabel|tabel) staat\. (.+?\.) ', o):
        _zet(it, 'opgave', f'{m.group(2)[0].upper()}{m.group(2)[1:]} Je zet dat in een {m.group(1)}. ' + o[m.end():], slog, "G6-W7 'In een tabel staat. …' → '… Je zet dat in een tabel.'"); o = it['opgave']
    # kijklijn: 'kijkt recht naar rechts' → 'kijkt naar rechts' (zoals G4-fixlijst #33)
    M3.sub_all(it, 'G6-W1 kijkt naar rechts (zoals G4 #33)', r'\bkijkt recht naar\b', 'kijkt naar', log); o = it['opgave']
    # notatie_machten.md (Didactiek 18:00, N1; Overzicht 18:05): G6 schrijft cm², dm² en m² als symbool; de mengvorm 'vierkante cm' is overal FAIL.
    # 'vierkante cm' → 'cm²' (385 × in MEET-E03) en 'vierkante meter' → 'm²' (4 ×), net als G7-W1. Het woord komt één keer per somtype in Hint 1 (Oefeningen).
    M3.sub_all(it, "G6-W8 'vierkante cm/meter' → 'cm²/m²' (notatie_machten.md)", r'\bvierkante (cm|centimeter|dm|decimeter|m|meter)s?\b',
               lambda m: {'cm': 'cm²', 'centimeter': 'cm²', 'dm': 'dm²', 'decimeter': 'dm²', 'm': 'm²', 'meter': 'm²'}[m.group(1)], log); o = it['opgave']
    # B9: 'Vereenvoudig 4/6.' → zelfde zin als de B3-items
    m = re.fullmatch(r'Vereenvoudig (\d+/\d+)\.', o)
    if m: _zet(it, 'opgave', f'Schrijf {m.group(1)} zo eenvoudig mogelijk.', slog, "G6-W2 'Vereenvoudig' → 'Schrijf … zo eenvoudig mogelijk'"); o = it['opgave']
    # B3: in de 'niet'-lijst staat een 'wel'-breuk (Claude-datafout, G5-park G6-GET-E03 033/035/036)
    m = re.search(r'hetzelfde als (\d+)/(\d+)\?', o); a = str(it['antwoord'])
    if m and (mm := re.fullmatch(r'wel:([\d/,]+)\|niet:([\d/,]+)', a)):
        doelw = Fr(int(m.group(1)), int(m.group(2)))
        wel, niet = mm.group(1).split(','), mm.group(2).split(',')
        bezet = set(wel) | set(niet); niet2 = []
        for x in niet:
            t_, n_ = map(int, x.split('/'))
            if Fr(t_, n_) == doelw:
                k = next(f'{t_ + d}/{n_}' for d in (1, -1, 2, 3) if t_ + d > 0 and f'{t_ + d}/{n_}' not in bezet and Fr(t_ + d, n_) != doelw)
                bezet.add(k); niet2.append(k)
            else: niet2.append(x)
        if niet2 != niet:
            nieuw = f"wel:{','.join(wel)}|niet:{','.join(niet2)}"
            slog(it, "G6-D1 'niet'-lijst zonder 'wel'-breuk (Claude-datafout; teller ± 1, zelfde noemer)", 'antwoord', a, nieuw); it['antwoord'] = nieuw
            it['merge']['g6Fix'] = {'punt': 'FOUT G6-GET-E03', 'was': a, 'wat': "'wel'-breuk uit de 'niet'-lijst, vervangen door een breuk met dezelfde noemer die niet gelijk is"}
    # ketensommen voluit: '7 × 4 = 28 + 12 = 40' → '7 × 4 = 28 en 28 + 12 = 40'
    def keten(s): return KETEN2.sub(lambda k: f'{k.group(1)} {k.group(2)} {k.group(3)} = {k.group(4)} en {k.group(4)} {k.group(5)} {k.group(6)} = {k.group(7)}', s)
    for f in it['foutHints']:
        u = f['uitleg'] or ''; n2 = keten(u)
        if n2 != u: slog(it, 'G6-N1 ketensom voluit', 'foutHints.uitleg', u, n2); f['uitleg'] = n2
    for op in it['opties'] or []:
        n2 = keten(op['tekst'])
        if n2 != op['tekst']: slog(it, 'G6-N1 ketensom voluit', 'opties', op['tekst'], n2); op['tekst'] = n2
    n2 = keten(it['opgave'])
    if n2 != it['opgave']: _zet(it, 'opgave', n2, slog, 'G6-N1 ketensom voluit')
    if it['opties']: M3.herbouw_opties(it)
    ex['claudeFoutHints'] = copy.deepcopy(it['foutHints'])
    it['foutHintsTekst'] = ' · '.join(f"{x['fout']} → {x['uitleg']}" for x in it['foutHints']) or None

# ---------------------------------------------------------------- herverificatie op de bewerkte vorm
def _num(s):
    s = str(s).strip().replace('.', '').replace('−', '-')
    return int(s) if re.fullmatch(r'-?\d+', s) else None

def verify_g6(it, q):
    v = _verify_g6(it, q)
    return v if v is None or not isinstance(v[1], Fr) else (v[0], f'{v[1].numerator}/{v[1].denominator}' if v[1].denominator != 1 else str(v[1].numerator), v[2])

def _verify_g6(it, q):
    t = it['opgave'].replace('\n', ' '); a = str(it['antwoord'])
    def res(exp, meth):
        if exp is None: return ('n.v.t.', None, meth)
        ok = str(exp) == a or (isinstance(exp, int) and _num(a) == exp) or (isinstance(exp, Fr) and re.fullmatch(r'\d+/\d+', a) and Fr(a) == exp and a == f'{exp.numerator}/{exp.denominator}')
        return ('ok' if ok else 'FOUT', exp, meth)
    # gelijkwaardige breuken slepen (wel/niet) — de oude G3-check las dit als 'ordenen' (vals alarm bij 034)
    if (m := re.search(r'hetzelfde als (\d+)/(\d+)\?', t)) and (mm := re.fullmatch(r'wel:([\d/,]+)\|niet:([\d/,]+)', a)):
        d = Fr(int(m.group(1)), int(m.group(2)))
        wel_ok = all(Fr(x) == d for x in mm.group(1).split(',')); niet_ok = all(Fr(x) != d for x in mm.group(2).split(','))
        return ('ok' if wel_ok and niet_ok else 'FOUT', f'wel = {d}, niet ≠ {d}', 'gelijkwaardige breuken: wel/niet' + ('' if niet_ok else " ('wel'-breuk in de 'niet'-lijst)") + ('' if wel_ok else " (een 'wel'-breuk klopt niet)"))
    if (m := re.search(r'deelbaar door (\d+) of niet', t)) and (mm := re.fullmatch(r'wel:([\d,]+)\|niet:([\d,]+)', a)):
        k = int(m.group(1)); ok = all(int(x) % k == 0 for x in mm.group(1).split(',')) and all(int(x) % k for x in mm.group(2).split(','))
        return ('ok' if ok else 'FOUT', f'wel deelbaar door {k}', 'deelbaar: wel/niet')
    if m := re.search(r'precies verdelen in groepjes van (\d+): ([\d, ]+)\?', t):
        k = int(m.group(1)); c = [int(x) for x in m.group(2).split(', ') if int(x) % k == 0]
        return res(c[0] if len(c) == 1 else None, 'deelbaar (één getal)')
    if m := re.search(r'Je kunt kiezen uit ([\d, ]+) en (\d+)\. Welk aantal [\wà-ÿ]+ kun je precies verdelen in groepjes van (\d+)\?', t):
        k = int(m.group(3)); c = [int(x) for x in m.group(1).split(', ') + [m.group(2)] if int(x) % k == 0]
        return res(c[0] if len(c) == 1 else None, 'deelbaar (één getal)')
    # breuken
    if m := re.fullmatch(r'(?:Reken uit: )?(\d+)/(\d+) ([+−-]) (\d+)/(\d+) =(?: \?)?(?: Typ een breuk\.)?', t.strip()):
        x, y = Fr(int(m.group(1)), int(m.group(2))), Fr(int(m.group(4)), int(m.group(5)))
        r = x + y if m.group(3) == '+' else x - y
        if int(m.group(2)) == int(m.group(5)) and re.fullmatch(r'\d+/\d+', a):   # gelijknamig: antwoord met dezelfde noemer of vereenvoudigd
            return ('ok' if Fr(a) == r else 'FOUT', r, 'breuken plus/min (zelfde noemer)')
        return res(r, 'breuken plus/min')
    if m := re.search(r'eet (\d+)/(\d+) van een \w+(?: en)?,? een andere? \w+(?: eet)? (\d+)/(\d+)\. Welk deel is samen op', t):
        r = Fr(int(m.group(1)), int(m.group(2))) + Fr(int(m.group(3)), int(m.group(4)))
        return ('ok' if re.fullmatch(r'\d+/\d+', a) and Fr(a) == r else 'FOUT', r, 'samen op (breuken)')
    if m := re.search(r'Schrijf (\d+)/(\d+) met noemer (\d+)', t):
        x = Fr(int(m.group(1)), int(m.group(2))); n_ = int(m.group(3)); return res(f'{x * n_}/{n_}' if (x * n_).denominator == 1 else None, 'andere noemer')
    if m := re.search(r'(\d+)/(\d+)(?: van de \w+)?[^.]*?\. Schrijf (?:deze|die) breuk zo eenvoudig mogelijk|Schrijf (\d+)/(\d+) zo eenvoudig mogelijk', t):
        x = Fr(int(m.group(1) or m.group(3)), int(m.group(2) or m.group(4))); return res(f'{x.numerator}/{x.denominator}', 'zo eenvoudig mogelijk')
    if m := re.search(r'(\d+)/(\d+) van (?:de|het|een) [\wà-ÿ]+ is evenveel als \?/(\d+)', t):
        x = Fr(int(m.group(1)), int(m.group(2))) * int(m.group(3)); return res(int(x) if x.denominator == 1 else None, 'gelijkwaardig: teller zoeken')
    if m := re.search(r'Welke breuk is het (grootst|kleinst): ((?:\d+/\d+(?:, | of )?)+)\?', t):
        fr = [Fr(x) for x in re.findall(r'\d+/\d+', m.group(2))]; best = max(fr) if m.group(1) == 'grootst' else min(fr)
        lab = next(x for x in re.findall(r'\d+/\d+', m.group(2)) if Fr(x) == best); return res(lab, 'breuken vergelijken')
    if m := re.match(r'Hoeveel is (\d+)/(\d+) van (€?)([\d.,]+)\?', t):
        f_ = Fr(int(m.group(1)), int(m.group(2)))
        if m.group(3):
            c = R5.cent(m.group(4)); v = c * f_; return res(R5.geld(int(v)) if v.denominator == 1 else None, 'breuk van een bedrag')
        v = int(m.group(4).replace('.', '')) * f_; return res(int(v) if v.denominator == 1 else None, 'breuk van een getal')
    if m := re.search(r'krijgt (\d+)/(\d+) van (\d+) [\wà-ÿ]+\. Hoeveel', t):
        v = int(m.group(3)) * Fr(int(m.group(1)), int(m.group(2))); return res(int(v) if v.denominator == 1 else None, 'breuk van een hoeveelheid (operator)')
    if m := re.search(r'liggen ([\d.]+) [\wà-ÿ]+\. (\d+)/(\d+) ervan is', t):
        v = int(m.group(1).replace('.', '')) * Fr(int(m.group(2)), int(m.group(3))); return res(int(v) if v.denominator == 1 else None, 'deel van een hoeveelheid')
    if m := re.search(r'Er zijn (\d+) koekjes\. Kleur (\d+)/(\d+)', t):
        v = int(m.group(1)) * Fr(int(m.group(2)), int(m.group(3))); return res(int(v) if v.denominator == 1 else None, 'koekjes kleuren')
    if m := re.search(r'Kleur (\d+)/(\d+) (?:deel )?van de balk', t): return res(int(m.group(1)), 'balk kleuren (stukken)')
    if m := re.search(r'in (\d+) gelijke stukken\. .* eet er (\d+) op\. Welk deel', t):
        return res(f'{m.group(2)}/{m.group(1)}', 'welk deel (breuk)')
    if m := re.search(r'(\d+) (\d+)/(\d+) [\wà-ÿ]+\. Hoeveel [\w-]+ (?:delen )?zijn dat in totaal\? \(Typ alleen de teller van \?/(\d+)', t):
        return res(int(m.group(1)) * int(m.group(3)) + int(m.group(2)), 'gemengd → teller')
    if m := re.fullmatch(r'(\d+) (\d+)/(\d+) = \?/(\d+)\. Welk getal hoort op het vraagteken\?', t):
        return res(int(m.group(1)) * int(m.group(3)) + int(m.group(2)) if m.group(3) == m.group(4) else None, 'gemengd → teller')
    if m := re.search(r'Je hebt (\d+)/(\d+) pizza\. Hoeveel hele pizza', t): return res(int(m.group(1)) // int(m.group(2)), 'samengesteld → helen')
    if m := re.search(r'De breuk (\d+)/(\d+) is hetzelfde als een deelsom\. Welke\? \d+ : (?:__|□)', t): return res(int(m.group(2)), 'breuk als deling (deler)')
    if m := re.search(r'(\d+)/(\d+) [\wà-ÿ]+\. Hoeveel hele [\wà-ÿ]+ zijn dat', t): return res(int(m.group(1)) // int(m.group(2)), 'samengesteld → helen')
    if m := re.search(r'is (\d+)/(\d+) meter lang\. Schrijf dat als kommagetal', t):
        v = Fr(int(m.group(1)), int(m.group(2))); s = f'{float(v):.2f}'.rstrip('0').rstrip('.').replace('.', ','); return res(s if v * 100 == int(v * 100) else None, 'breuk → kommagetal')
    if m := re.search(r'(\d+) [\wà-ÿ]+ worden eerlijk verdeeld over (\d+) [\wà-ÿ\'’-]+\. Welk deel van een', t): return res(f'{m.group(1)}/{m.group(2)}', 'breuk als deling')
    if m := re.search(r'(\d+)/(\d+) van een [\wà-ÿ]+ is hetzelfde als een deelsom\. Welke\? \d+ : (?:__|□)', t): return res(int(m.group(2)), 'breuk als deling (deler)')
    if m := re.search(r'Zet (\d+/\d+|\d+,\d+|\d{1,3}(?:\.\d{3})+|\d+) op de (?:getallen)?lijn', t): return res(m.group(1), 'getallenlijn')
    if m := re.search(r'Welke? (?:breuk|getal|kommagetal) is het (grootst|kleinst)\? Kies uit (.+)\.$', t):
        lab = re.findall(r'\d+/\d+|[\d.,]+\d', m.group(2))
        val = [Fr(x) if '/' in x else Fr(x.replace('.', '').replace(',', '.')) for x in lab]
        best = max(val) if m.group(1) == 'grootst' else min(val)
        return res(lab[val.index(best)] if val.count(best) == 1 else None, 'grootste/kleinste kiezen')
    if (m := re.search(r'Zet de (breuken|getallen|kommagetallen) op volgorde van (klein naar groot|groot naar klein)', t)) and '|' in a:
        lab = a.split('|')
        try: val = [Fr(x) if '/' in x else Fr(x.replace('.', '').replace(',', '.')) for x in lab]
        except (ValueError, ZeroDivisionError): return None
        goed = sorted(val, reverse=m.group(2) == 'groot naar klein')
        opts = [o['tekst'] for o in it['opties']] if it['opties'] else None
        return ('ok' if val == goed and len(set(val)) == len(val) and (not opts or sorted(opts) == sorted(lab)) else 'FOUT', '|'.join(lab[val.index(v)] for v in goed), 'ordenen (op waarde)')
    js = (it['visual'] or {}).get('jsRender') or {}
    if js.get('soort') in ('lijngrafiek', 'staafgrafiek', 'staafdiagram') and js.get('punten'):
        P = {p_['naam']: p_['waarde'] for p_ in js['punten']}
        if m := re.search(r'waren er in (\w+)\?', t):
            return res(P.get(m.group(1)), 'grafiek aflezen')
        if re.search(r'in alle maanden samen', t): return res(sum(P.values()), 'grafiek: totaal')
        if m := re.search(r'(kwamen er bij|gingen er af|minder) van (\w+) naar (\w+)', t):
            if m.group(2) in P and m.group(3) in P: return res(abs(P[m.group(3)] - P[m.group(2)]), 'grafiek: verschil')
    if m := re.fullmatch(r'([\d.,]+) (ml|cl|dl|l|L) = (?:□|__) (ml|cl|dl|l|L)', t.strip()):
        F = {'ml': 1, 'cl': 10, 'dl': 100, 'l': 1000, 'L': 1000}
        v = Fr(m.group(1).replace('.', '').replace(',', '.')) * F[m.group(2)] / F[m.group(3)]
        s_ = (str(v.numerator) if v.denominator == 1 else f'{float(v):g}'.replace('.', ','))
        return ('ok' if a.replace('.', '') == s_.replace('.', '') else 'FOUT', s_, 'inhoudsmaten omrekenen')
    def ev(e):
        e = e.replace('.', '').replace('×', '*').replace('−', '-').replace(':', '/').replace('€', '')
        return Fr(eval(e, {'__builtins__': {}})) if re.fullmatch(r'[\d+\-*/ ()]+', e) else None
    if (m := re.search(r'Hoe reken je (.+) handig uit\?', t)) or (m := re.search(r'Welke som is even ?veel als (.+)\?', t)):
        try: x, y = ev(m.group(1)), ev(a)
        except (SyntaxError, ZeroDivisionError): x = y = None
        if x is not None and y is not None: return ('ok' if x == y and a.strip() != m.group(1).strip() else 'FOUT', str(x), 'handig rekenen (zelfde uitkomst)')
    if m := re.search(r'^(\d+) [\wà-ÿ]+ (?:met|van elk) (€ ?)?(\d+)\b', t):
        v = int(m.group(1)) * int(m.group(3)); return res(R5.geld(v * 100) if m.group(2) else v, 'handig keer (context)')
    if m := re.search(r'Hoe heet de (\d+) in (\d+)/(\d+)\?', t):
        w = 'de teller' if m.group(1) == m.group(2) and m.group(1) != m.group(3) else 'de noemer' if m.group(1) == m.group(3) and m.group(1) != m.group(2) else None
        return res(w, 'teller/noemer')
    if m := re.search(r'(\d+) [\wà-ÿ]+ (?:en verdeelt ze )?eerlijk over (\d+) [\wà-ÿ\'’-]+\..*hoeveel blijven er over\?', t):
        n_, d_ = int(m.group(1)), int(m.group(2)); g = [int(x) for x in re.findall(r'\d+', a)]
        return ('ok' if g == [n_ // d_, n_ % d_] else 'FOUT', f'{n_ // d_}, {n_ % d_} over', 'verdelen met rest')
    if m := re.search(r'Je hebt (\d+) [\wà-ÿ ]+\. Je knipt elke [\wà-ÿ]+ in (\d+) stukken', t):
        v = int(m.group(1)) * int(m.group(2)); g = re.match(r'\d+', a)
        return ('ok' if g and int(g.group()) == v else 'FOUT', v, 'knippen (keer)')
    # getallen tot 100.000
    if m := re.search(r'([\d.]+) wordt ([\d.]+)\. Met hoeveel verandert', t): return res(abs(_num(m.group(2)) - _num(m.group(1))), 'verschil (positiewaarde)')
    if m := re.search(r'Welk getal is ([\d.]+) (meer|minder) dan ([\d.]+)\?', t):
        v = _num(m.group(3)) + (_num(m.group(1)) if m.group(2) == 'meer' else -_num(m.group(1))); return res(v, 'meer/minder dan')
    if m := re.search(r'Rond ([\d.]+) af op (tientallen|honderdtallen|duizendtallen|tienduizendtallen)', t):
        v = _num(m.group(1)); s = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000, 'tienduizendtallen': 10000}[m.group(2)]; return res((v + s // 2) // s * s, 'afronden')
    if m := re.search(r'Rond dit aantal af op (tientallen|honderdtallen|duizendtallen)', t):
        v = _num(re.search(r'precies ([\d.]+)', t).group(1)); s = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000}[m.group(1)]; return res((v + s // 2) // s * s, 'afronden')
    if m := re.search(r'staat ([\d.]+) [\wà-ÿ]+\. Hoeveel is de (\d) in dit getal waard', t):
        s = m.group(1).replace('.', ''); i = s.find(m.group(2)); return res(int(m.group(2)) * 10 ** (len(s) - i - 1) if s.count(m.group(2)) == 1 else None, 'cijferwaarde')
    if m := re.search(r'staat op ([\d.]+) [\wà-ÿ]+\. Er komt er één bij', t): return res(_num(m.group(1)) + 1, 'één erbij')
    if m := re.search(r'liggen ([\d.]+) [\wà-ÿ]+\. In (?:de|het) [\wà-ÿ]+ liggen er ([\d.]+)\. Typ het grootste getal', t): return res(max(_num(m.group(1)), _num(m.group(2))), 'grootste')
    # cijferen in context
    if m := re.search(r'liggen ([\d.]+) [\wà-ÿ]+, in (?:de|het) [\wà-ÿ]+ ([\d.]+)\. Hoeveel zijn het er samen', t): return res(_num(m.group(1)) + _num(m.group(2)), 'samen')
    if m := re.search(r'Er waren ([\d.]+) [\wà-ÿ]+ in (?:de|het) [\wà-ÿ]+\. Nu zijn er nog ([\d.]+)\.', t): return res(_num(m.group(1)) - _num(m.group(2)), 'weg (−)')
    if m := re.search(r'heeft ([\d.]+) [\wà-ÿ]+, (?:de|het) [\wà-ÿ]+ heeft er ([\d.]+)\. Hoeveel meer', t): return res(_num(m.group(1)) - _num(m.group(2)), 'hoeveel meer')
    if m := re.search(r'lagen ([\d.]+) [\wà-ÿ]+\. Er zijn er ([\d.]+) weggehaald', t): return res(_num(m.group(1)) - _num(m.group(2)), 'weggehaald (−)')
    if m := re.search(r'staan (\d+) rijen met (\d+) [\wà-ÿ]+\. Hoeveel', t): return res(int(m.group(1)) * int(m.group(2)), 'rijen × aantal')
    if m := re.search(r'([\d.]+) [\wà-ÿ\'’-]+ worden eerlijk verdeeld over (\d+) [\wà-ÿ\'’-]+\. Hoeveel [\wà-ÿ]+ krijgt', t):
        x, y = _num(m.group(1)), int(m.group(2)); return res(x // y if x % y == 0 else None, 'verdelen')
    if m := re.search(r'Van ([\d.]+) [\wà-ÿ]+ worden er ([\d.]+) verkocht', t): return res(_num(m.group(1)) - _num(m.group(2)), 'uit het hoofd (−)')
    # oppervlakte, gemiddelde
    if m := re.search(r'is (\d+) cm lang en (\d+) cm breed\. Hoeveel vierkante cm', t): return res(int(m.group(1)) * int(m.group(2)), 'oppervlakte l × b')
    if m := re.search(r'oppervlakte van een rechthoek is (\d+) vierkante cm\. Eén zijde is (\d+) cm', t):
        x, y = int(m.group(1)), int(m.group(2)); return res(x // y if x % y == 0 else None, 'oppervlakte → zijde')
    if m := re.search(r'van (\d+) meter lang en (\d+) meter breed\. Hoeveel vierkante meter', t): return res(int(m.group(1)) * int(m.group(2)), 'oppervlakte (m²)')
    if m := re.search(r'verzamelden [\wà-ÿ]+[:.] ([\d, ]+)\. Hoeveel [\wà-ÿ]+ is dat gemiddeld', t):
        v = [int(x) for x in m.group(1).split(', ')]; s = sum(v); return res(s // len(v) if s % len(v) == 0 else None, 'gemiddelde')
    # kale sommen tot 10.000
    if m := re.fullmatch(r'([\d.]+) ([+−×:]) ([\d.]+) =', t.strip()):
        x, op, y = _num(m.group(1)), m.group(2), _num(m.group(3))
        if x is not None and y is not None:
            return res({'+': x + y, '−': x - y, '×': x * y, ':': (x // y if y and x % y == 0 else None)}[op], 'kale som')
    return None

# ---------------------------------------------------------------- notatie (G6)
KLOKTIJD = re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
DP_RX = re.compile(r'(?<![\d□]\s)(?<![\d□]):\s*[\d□#€]')
VERHOUDING = re.compile(r'(verhouding|schaal|staat tot|mengen|mengsel)[^.?!]*\d\s*:\s*\d|\d\s*:\s*\d[^.?!]*(verhouding|schaal)', re.I)
def notatie_check_g6(it):
    hits = []
    a = str(it['antwoord'])
    txt = [it['opgave'] or ''] + [o['tekst'] for o in it['opties'] or []] + [f['uitleg'] or '' for f in it['foutHints']] + ([] if re.fullmatch(r'wel:[^|]*\|niet:.*', a) else [a])   # sleepvak-sleutel is geen kindtekst
    for s in txt:
        s2 = KLOKTIJD.sub('', s)
        if DP_RX.search(s2): hits.append('DP')
        if re.search(r'[\d□#]\s*[-–]\s*[\d□#]', s): hits.append('MIN')
        if re.search(r'(?<![\d.,])\d\.\d{3}(?!\d|[.,]\d)', s): hits.append('PUNT4')
        if re.search(r'(?<![\d.,:/])\d{5,}(?![\d.,:/])', s): hits.append('PUNT5')
        if 'Één' in s: hits.append('EEN')
        if re.search(r'€\s\d|€\s?\d+,-|€\s?\d+,00\b', s): hits.append('GELD')
        if re.search(r'(?<![\d,])\d+,\d{3,}(?!\d)', s): hits.append('KOMMA3')
        if re.search(r'[\d□] l\b', s): hits.append('LITER')
        if '÷' in s: hits.append('DEELTEKEN÷')
        if re.search(r'%|\bprocent\b', s, re.I): hits.append('PROCENT')
        if VERHOUDING.search(s2): hits.append('VERH')
        if KETEN2.search(s): hits.append('KETEN')
    return sorted(set(hits))
