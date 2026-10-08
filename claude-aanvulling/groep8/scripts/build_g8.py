#!/usr/bin/env python3
"""G8-merge van de Claude-vragenbank (stap 1–3), 1 okt 2026 (opdracht Overzicht, stap 3). Sjabloon = G7-merge
(kopie in scripts/g7_basis/: build_g7.py, regels_g7.py, besluiten_g7.py, fx21.py, met de keten g6_basis/g5_basis/g4_basis_1435/).
Stap 1  pool: alle items van de 20 Claude-G8-doelen (rekenleerweg groep 8) + de items die de G7-merge voor G8 parkeerde
        (g7/data/geparkeerd_G8.json, 688); zonder wat al in G3–G7 zit (gemapt, geschrapt, twijfel, terug) → 'al in G3–G7' (alleen geteld).
Stap 2  per item (classify_g8): gemapt (G8-doel) / twijfel (voorstel G8-doel + vraag aan Didactiek) / terug-G7 (te makkelijk;
        met een passend G7-doel ook in g7/data/aanvulling_uit_g8.json) / buiten-basisschool (machten, wortels, negatief × negatief,
        letters als getal, modus, mediaan: data/buiten_basisschool.json).
Stap 2b bewerkingen: G3- t/m G7-regels (zoals de G7-build) + FX21 (Engelse woorden) + G8-regels (bewerk_g8: het-woorden, '€ 40,-' → '€40')
        + herverificatie (verify_g8 voor haakjes, procenten, rente, maten, tijdzones, rekenmachine; daarna de G7-keten).
Ontdubbelen: zelfde doel + opgave + tekening + opties + antwoord. Zelfde opgave als onze G8-bank (export) → merge.zelfdeOpgaveAlsOnzeBank.
Stap 3  somtypen per G8-doel (somtypen/G8-*.md) met vaste sleutels (bevroren/somtype_nr_v1.json + aanvullingen), twijfellijst.
Leest alleen: claude-bank-src, claude-merge/g3–g7, exports. Schrijft in claude-merge/g8 en g7/data/aanvulling_uit_g8.json.
Gebruik: python3 scripts/build_g8.py"""
import json, re, csv, collections, subprocess, os, sys, math, datetime, hashlib, glob
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(HERE)
G3, G4, G5, G6, G7 = (f'/workspace/claude-merge/g{n}' for n in (3, 4, 5, 6, 7))
AANV_UIT = os.environ.get('G8_AANV_UIT') or f'{OUT}/logs/aanvulling_uit_g8'      # Z-#962 (les 363): g{4..7}/data/aanvulling_uit_g8.json eerst hier; scripts/bouw_veilig.py zet ze om
sys.path.insert(0, f'{HERE}/g7_basis')
import build_g7 as B7                     # laadt de hele G7-keten (alleen functies; B7.main wordt nooit aangeroepen)
M, B3, R4, R5, R6, R7, BG7, FX21 = B7.M, B7.B3, B7.R4, B7.R5, B7.R6, B7.R7, B7.BG7, B7.FX21
V, CDOEL, CREDIT, COMMIT, EXP = B3.V, B3.CDOEL, B3.CREDIT, B3.COMMIT, B3.EXP
R, G, T = R7.R, R7.G, R7.T
OURS = {d['id']: {'bordtitel': d['bordtitel'], 'korteNaam': d['korteNaam'], 'domein': d['domein'], 'aantalItems': d['aantalItems']}
        for g in EXP['groepen'] if g['groep'] == 8 for dm in g['domeinen'] for d in dm['doelen']}
import besluiten_g8 as BG8                 # Didactiek-besluiten op de 1226 G8-twijfelitems + Dave 20:56
sys.path.insert(0, "/workspace/claude-merge/tools"); import breukvorm as BV, kloktijd_fix as KF, e05_routes as ER, bouwsel_routes as BR, kop_vast as KV, g8_b7_vlag as B7VLAG, eindcijfer_check as EC      # (B7VLAG: b7-data pas na patch_batch7 1b) V-#760 (Didactiek G8 batch 1, 8 okt): even grote breuk telt als goed (#170, Dave 21:24)
BESLUIT_G8 = BG8.laad()
_I8 = json.load(open(f'{OUT}/bevroren/ids_v1.json'))      # Dave 20:56 (5): ook via vorigeIds (het item kreeg in G5 een naar-id; anders valt de regel stil weg)
E02_001 = next((c for c, i in _I8['ids'].items() if i == 'G8-GET-E02-claude-bank-001'), None) or next((c for c, vs in _I8.get('vorigeIds', {}).items() if 'G8-GET-E02-claude-bank-001' in vs), None)
assert E02_001 == '096456c8-d6f2-4354-88a3-12ab5fd051e4', ('E02-001 (4 × 198) niet gevonden', E02_001)
G7D = {d['id']: d['bordtitel'] for g in EXP['groepen'] if g['groep'] == 7 for dm in g['domeinen'] for d in dm['doelen']}

# ---------------------------------------------------------------- stap 1: pool
KANDIDAAT = [c for c, d in CDOEL.items() if d['groep'] == 8]
gebruikt = {}
for naam, p in (('G3', G3), ('G4', G4), ('G5', G5), ('G6', G6), ('G7', G7)):
    for it in json.load(open(f'{p}/data/gemapt.json'))['items']:
        if it['merge'].get('uitG8'): continue      # aanvulling uit G8 (g{N}/data/aanvulling_uit_g8.json): blijft in de G8-pool, anders valt hij hier weg
        gebruikt.setdefault(it['bron']['claudeId'], f'gemapt in {naam}')
    for r in csv.DictReader(open(f'{p}/logs/geschrapt.csv')):
        if '-claude-bank-naar-' in r.get('id', '') or ('-claude-bank-terug-' in r.get('id', '') and r['id'].startswith(f'{naam}-')): continue      # dubbel van een aanvulling uit G8 in die groep
        gebruikt.setdefault(r['claudeId'], f"geschrapt in {naam} ({r['groep']})")
    tw = json.load(open(f'{p}/data/twijfel.json'))
    for it in tw.get('items', []) + [x for c in tw.get('categorieen', {}).values() for x in c['items']]: gebruikt.setdefault(it['bron']['claudeId'], f'twijfel in {naam}')
for p, f, w in ((G4, 'terug_G3', 'terug-G3 in G4'), (G5, 'terug_G4', 'terug-G4 in G5'), (G6, 'terug_G5', 'terug-G5 in G6'), (G7, 'terug_G6', 'terug-G6 in G7')):
    for it in json.load(open(f'{p}/data/{f}.json'))['items']: gebruikt.setdefault(it['bron']['claudeId'], w)
G7PARK = {it['bron']['claudeId']: it for it in json.load(open(f'{G7}/data/geparkeerd_G8.json'))['items']}
EXP8 = json.load(open('/workspace/exports/leermees-vragenbank-export/vragenbank_g8.json'))
ONZE_G8 = {(d['id'], re.sub(r'\s+', ' ', it['opgave']).strip()): it['id'] for dm in EXP8['domeinen'] for d in dm['doelen'] for it in d['items']}
PILOT8 = {B7.pnorm(it['opgave']): it['id'] for dm in EXP8['domeinen'] for d in dm['doelen'] for cv in d.get('claudeVarianten') or [] for it in cv['items']}

# ---------------------------------------------------------------- stap 2: mapping
def T7(d, r, why, aanv): return R('terug-G7', d, r, why, aanvulling=aanv)
def BUITEN(r, why): return R('buiten-basisschool', 'G8-BUITEN', r, why)
def buiten(t):
    if re.search(r'\d\s?[²³]|\^|\bmacht\b|kwadraat|wortel van|vierkantswortel|worteltrekken|√', t) and not re.search(r'\b(?:c|d)?m[²³]|km²|m³|cm³|dm³', t): return 'machten of wortels'
    if re.search(r'(?:−|-)\d+\s*[×x·]\s*(?:−|-)\d+|\(−\d+\)\s*[×x:]\s*\(−\d+\)', t): return 'negatief × negatief'
    if re.search(r'\b[a-z]\s*=\s*\d|\b\d\s*[a-z]\s*[+−-]|\bx\s*[+−-]\s*\d', t): return 'letters als getal (algebra)'
    if re.search(r'\bmodus\b|\bmediaan\b|vaakst voorkomt', t): return 'modus/mediaan'
    return None
def classify_g8(q, p7):
    t = q['vraag']; cd = q['doel']
    b = buiten(t)
    if b: return BUITEN('G8-X-buiten', f'{b}: hoort niet in de basisschool (SLO eind G8; besluit G7 over mediaan en deel-van-geheel)')
    if p7:
        vd = p7['merge']['voorstelDoel']
        if cd == 'C20' and re.search(r'Welk getal ligt \d+ lager dan', t):
            return T(vd, 'G8-P02-negatief-zonder-context', 'negatief getal zonder context (getallenlijn of temperatuur)', 'negatief-zonder-context')
        return G(vd, 'G8-P00-park-G7', f'uit de G7-park (voorstel {vd}, regel {p7["merge"]["regel"]})')
    if cd == 'T1': return T7('G7-DENK-02', 'G8-T1-door-elkaar', 'verhaaltje met één bewerking (getallen tot 1000): niveau G5–G7, geen G8-doel', False)
    if cd == 'T2': return G('G8-GET-E03', 'G8-T2-haakjes', 'samengestelde som met haakjes en voorrang (G8-GET-E03)')
    if cd == 'T3':
        if re.search(r'Op welk cijfer eindigt', t): return G('G8-GET-E02', 'G8-T3-laatste-cijfer', 'controleren met het laatste cijfer (G8-GET-E02: procedures kritisch beoordelen)')
        if re.search(r'[Rr]ond (?:\S+|beide getallen) af op', t): return G('G8-GET-E02', 'G8-T3-schatten-afspraak', 'schatten met een afrondafspraak (G8-GET-E02)')
        if re.search(r'Kijk zonder uit te rekenen', t):
            if q.get('opties'): return G('G8-GET-E02', 'G8-T3-kan-kloppen', 'schattend controleren met keuzes (G8-GET-E02)')
            return T('G8-GET-E02', 'G8-T3-kan-kloppen', "'Welk antwoord kan kloppen?' zonder keuzes: het kind moet precies rekenen", 'kan-kloppen-zonder-opties')
        return T('G8-GET-E02', 'G8-T3-ongeveer', "'Hoeveel is … ongeveer?' zonder afspraak hoe je afrondt: meer antwoorden zijn goed", 'schatten-zonder-afspraak')
    if cd == 'T4': return G('G8-GET-E05', 'G8-T4-rekenmachine', 'rekenmachine-uitkomst interpreteren (naar boven afronden, rest) (G8-GET-E05)')
    if cd == 'T5': return G('G8-VERH-E05', 'G8-T5-procent-erbij', 'procent erbij of eraf, oud ↔ nieuw (G8-VERH-E05)')
    if cd == 'T6':
        if 'rente krijgt' in t: return G('G8-VERH-E04', 'G8-T6-rente', 'rente = procent van een bedrag (G8-VERH-E04)')
        return G('G8-VERH-E05', 'G8-T6-na-een-jaar', 'bedrag na een jaar = procent erbij (G8-VERH-E05)')
    if cd == 'T7': return T7('G7-GET-04', 'G8-T7-prijs-per-stuk', 'prijs per stuk: kommagetal delen door een heel getal (G7-GET-04)', True)
    if cd == 'M24': return T7('G7-MEET-02', 'G8-M24-samengesteld', 'oppervlakte van samengestelde rechthoeken (G7-MEET-02)', True)
    if cd == 'M25':
        if 'hectare' in t: return G('G8-MEET-V01', 'G8-M25-hectare', 'hectare ↔ m² (G8-MEET-V01: oppervlaktematen herhalen)')
        if 'm³' in t: return G('G8-MEET-E03', 'G8-M25-m3-liter', 'm³ ↔ liter (G8-MEET-E03: inhoud als systeem)')
        return G('G8-MEET-E01', 'G8-M25-km', 'km ↔ m met komma (G8-MEET-E01: lengte als systeem)')
    if cd == 'M26': return G('G8-MEET-E06', 'G8-M26-tijdzones', 'vluchttijd en tijdzones (G8-MEET-E06)')
    if cd == 'M29': return T('G8-MEET-E03', 'G8-M29-geheugen', 'geheugenomvang (MB/GB/TB): geen SLO-doel', 'geheugenomvang')
    if cd == 'K7':
        if re.search(r'Zet de stip op \(', t): return G('G8-VBN-V01', 'G8-K7-coordinaten', 'coördinaten (x, y) (G8-VBN-V01)')
        return T('G8-VBN-V01', 'G8-K7-vakcode', "vakcode op een plattegrond ('Wat staat er in vak E2?'): niveau G4–G6", 'vakcode-plattegrond')
    if cd == 'K8': return T('G8-MKU-V01', 'G8-K8-bouwsel', 'blokjes tellen in een bouwsel: geen G8-doel (MKU-V01 is kijklijnen/standpunt)', 'bouwsel-tellen')
    if cd in ('G8', 'G13'): return G('G8-VBN-E04', f'G8-{cd}-kritisch', 'kritisch kijken naar grafieken en conclusies (G8-VBN-E04)')
    if cd == 'G9':
        if re.search(r'zonder kijken|\bkans\b', t): return T('G8-VBN-E04', 'G8-G9-kans', 'kans (G7: Didactiek zette kans bij G7-VERH-04)', 'kans')
        return T('G8-VBN-E04', 'G8-G9-statistiek', 'gemengde statistiekvragen (sommige zijn gewone sommen)', 'statistiek-gemengd')
    if cd == 'T8': return T7('G7-DENK-03', 'G8-T8-meerstaps', 'meerstapssom met getallen tot 100: niveau G5–G7', False)
    if cd == 'T9': return T7('G7-DENK-02', 'G8-T9-welke-som', "'Welke som hoort bij dit verhaal?' met getallen tot 250: niveau G3–G5", False)
    if cd in ('W3', 'W6'): return G('G8-GET-E02', f'G8-{cd}-aanpak', 'je aanpak kiezen en controleren (G8-GET-E02)')
    return R('niet', None, None, None)

# ---------------------------------------------------------------- stap 2b: G8-bewerkingen en controle
HET = r'(?:ei|bot|varenblad|ruimtepak|shirt|kaartje|zonnepaneel|ruimteschip|potje|boek|flesje|bord|geld|huis)'
DIER = r"(?:dino|poes|konijn|pinguïn|eekhoorn)"
NAMEN8 = [('Sanne', 'ze'), ('Daan', 'hij'), ('Noor', 'ze'), ('Milan', 'hij'), ('Fatima', 'ze'), ('Bram', 'hij')]
def _naam8(it): return NAMEN8[int(hashlib.md5(it['bron']['claudeId'].encode()).hexdigest(), 16) % len(NAMEN8)]
def _snel8(m):
    v = Fr(_bedrag(m.group(1))) / _bedrag(m.group(2))
    return ('Een fietser' if v <= 25 else 'Een bus') + f' legt {m.group(1)} km af in {m.group(2)} uur'
# G8-R9 (toegepast op opgave, opties, claude-velden en hints van het item): dieren die sparen, rijden of taart eten → mensen
CONTEXT_G8 = [
    (rf'\bEen {DIER} zet (€\d+) op een spaarrekening', lambda it: lambda m: f"{_naam8(it)[0]} zet {m.group(1)} op een spaarrekening"),
    (r'\bkrijgt hij na één jaar\b', lambda it: (lambda m: f"krijgt {_naam8(it)[1]} na één jaar") if it.get('_dier8') else (lambda m: m.group(0))),
    (rf'\bEen {DIER} legt (\d+(?:,\d+)?) km af in (\d+(?:,\d+)?) uur', _snel8),
    (rf'\bEen {DIER} loopt\b', 'Een wandelaar loopt'),
    (rf'\b[Ee]en {DIER} eet\b', 'een kind eet'),
    (rf'\been andere? {DIER}\b', 'een ander kind'),
    (rf'\bEen {DIER} heeft (\d+) miljoen \w+ verzameld', r'In een land wonen \1 miljoen mensen'),
    (rf'\bEen {DIER} reist\b', 'Een auto rijdt'),
    (r'\bJe spaart voor poesjes\b', 'Je spaart voor een fiets'),
    (r'\bWat kost het poesje nu\?', 'Wat kost de knuffel nu?'),
]
def bewerk_g8(it, slog):
    def f(s):
        if not isinstance(s, str): return s
        s2 = re.sub(rf'\b([Dd])e ({HET})\b', lambda m: ('Het' if m.group(1) == 'D' else 'het') + ' ' + m.group(2), s)
        def _eur(m):
            n = m.group(1).replace('.', ''); return '€' + (n if int(n) < 10000 else m.group(1))
        s2 = re.sub(r'€ ?(\d{1,3}(?:\.\d{3})+|\d+),-', _eur, s2); s2 = re.sub(r'€ (\d)', r'€\1', s2)
        s2 = re.sub(r'€(\d)\.(\d{3})(?!\d)(?!,\d)', r'€\1\2', s2)          # €1.500 → €1500 (geen punt onder 10.000)
        for pat, door in CONTEXT_G8:                                         # G8-R9: geen dieren als mensen (zoals G5 #86)
            s2 = re.sub(pat, door(it) if getattr(door, '__name__', '') == '<lambda>' else door, s2)
        s2 = re.sub(r'(^|[.?!] )een kind eet', lambda m: m.group(1) + 'Een kind eet', s2)
        return s2
    voor = it['opgave']
    it['_dier8'] = bool(re.search(rf'Een {DIER} zet', voor))
    it['opgave'] = f(it['opgave'])
    # B15 (delen door een breuk): geen dieren of dingen 'in stukken verdelen' (poesjes, pionnen, stenen) → repen chocola
    m = re.match(r'^(\d+(?:/\d+)?) ([a-zà-ÿ]+) (worden|wordt)( in stukken van \d+/\d+ verdeeld| verdeeld in stukken van \d+/\d+)\.', it['opgave'])
    if m and m.group(2) not in ('wortels', 'wortel', 'pizza', "pizza's", 'taarten', 'taart', 'repen', 'reep', 'broden', 'brood'):
        een = m.group(3) == 'wordt' or m.group(1) == '1'
        keuze = [('reep chocola', 'repen chocola'), ('pizza', "pizza's"), ('pannenkoek', 'pannenkoeken'), ('stokbrood', 'stokbroden')]
        enk, mv = keuze[int(hashlib.md5(it['bron']['claudeId'].encode()).hexdigest(), 16) % len(keuze)]
        it['opgave'] = it['opgave'].replace(f"{m.group(1)} {m.group(2)} {m.group(3)}", f"{m.group(1)} {enk if een else mv} {'wordt' if een else 'worden'}", 1)
        it['merge']['g8Context'] = f"B15: '{m.group(2)}' → '{enk if een else mv}' (niets levends of onbreekbaars in stukken verdelen)"
    for o in it['opties'] or []: o['tekst'] = f(o['tekst'])
    ev = it['extraVelden']
    for k in ('claudeUitleg', 'claudeKaleSom', 'claudeStrategie'): ev[k] = f(ev.get(k)) if k in ev else ev.get(k)
    for fh in ev.get('claudeFoutHints') or []: fh['uitleg'] = f(fh.get('uitleg'))
    for k in ('hint', 'sterkereHint', 'antwoordDetail'): it[k] = f(it.get(k))
    for fh in it.get('foutHints') or []:
        for k in list(fh):
            if isinstance(fh[k], str): fh[k] = f(fh[k])
    it.pop('_dier8', None)
    if it['opgave'] != voor: B3.FIXLOG.append({'id': it['bron']['claudeId'], 'soort': 'G8-R8/R9 het-woord/€-notatie/context', 'veld': 'opgave', 'voor': voor, 'na': it['opgave']})

def _num(s):
    s = str(s).replace('€', '').replace(' ', '').replace('.', '').replace(',', '.')
    m = re.match(r'^-?\d+(?:\.\d+)?', s); return Fr(m.group(0)) if m else None
def _bedrag(s): return Fr(s.replace('.', '').replace(',', '.'))
def verify_g8(it):
    o = it['opgave'].replace('\n', ' '); a = _num(it['antwoord'])
    def uit(v, methode):
        if v is None: return None
        return ('ok' if a is not None and a == v else 'FOUT', str(v), methode)
    if (m := re.fullmatch(r'Reken uit[:.]? ([\d ()+−×:\-]+?)(?: = \?)?', o.strip())):
        e = m.group(1).replace('×', '*').replace('−', '-').replace(':', '/')
        try: v = Fr(eval(re.sub(r'(\d+)', r'Fr(\1)', e), {'Fr': Fr}))
        except Exception: return None
        return uit(v, 'G8 haakjes/voorrang')
    E = r'€ ?(\d+(?:[.,]\d+)?)(?:,-)?'
    if (m := re.search(rf'kostte {E} en kost nu {E}\. Met hoeveel procent is de prijs (gestegen|gedaald)', o)):
        x, y = _bedrag(m.group(1)), _bedrag(m.group(2)); return uit(abs(y - x) / x * 100, 'G8 procent erbij/eraf')
    if (m := re.search(rf'kostte {E}\. De prijs (stijgt|daalt) met (\d+)%', o)):
        x = _bedrag(m.group(1)); p = int(m.group(3)); return uit(x * (100 + (p if m.group(2) == 'stijgt' else -p)) / 100, 'G8 prijs na procent')
    if (m := re.search(rf'zet {E} op een spaarrekening met (\d+(?:,\d+)?)% rente per jaar\. Hoeveel (rente krijgt|staat er)', o)):
        x = _bedrag(m.group(1)); p = _bedrag(m.group(2)); return uit(x * p / 100 if m.group(3) == 'rente krijgt' else x * (100 + p) / 100, 'G8 rente')
    if (m := re.search(r'(\d+(?:,\d+)?) km\. Hoeveel meter', o)): return uit(_bedrag(m.group(1)) * 1000, 'G8 km → m')
    if (m := re.search(r'(\d+(?:,\d+)?) m³\. Hoeveel liter', o)): return uit(_bedrag(m.group(1)) * 1000, 'G8 m³ → L')
    if (m := re.search(r'(\d+(?:,\d+)?) hectare\. Hoeveel m²', o)): return uit(_bedrag(m.group(1)) * 10000, 'G8 ha → m²')
    if (m := re.search(r'vertrekt om (\d{1,2}):(\d{2}).*?De vlucht duurt (\d+) uur(?: en (\d+) minuten)?\.(?: Op de plek van aankomst is het (\d+) uur (vroeger|later) dan thuis\.)?', o)):
        t = int(m.group(1)) * 60 + int(m.group(2)) + int(m.group(3)) * 60 + int(m.group(4) or 0)
        if m.group(5): t += (1 if m.group(6) == 'later' else -1) * int(m.group(5)) * 60
        t %= 24 * 60; v = f'{t // 60}:{t % 60:02d}'
        return ('ok' if str(it['antwoord']).strip() == v else 'FOUT', v, 'G8 tijdzones')
    if (m := re.search(r'Rond (\d+) af op honderdtallen en (\d+) op tientallen', o)):
        r_ = lambda x, k: (x + k // 2) // k * k
        return uit(Fr(r_(int(m.group(1)), 100) * r_(int(m.group(2)), 10)), 'G8 schatten met afrondafspraak')
    if re.search(r'gemiddeld per dag', o) and len(d_ := re.findall(r'op (?:maan|dins|woens|donder|vrij|zater|zon)dag (\d+)', o)) >= 2:
        return uit(Fr(sum(map(int, d_)), len(d_)), 'G8 gemiddelde per dag')
    K_ = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000}
    r2 = lambda x, k: (x + k // 2) // k * k
    if (m := re.search(r'(\d+) dozen met elk (\d+) [a-zà-ÿ]+\. Schat hoeveel dat ongeveer is: rond (\d+) af op (\w+) en reken dan uit', o)) and m.group(4) in K_:
        x, y, z = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return uit(Fr(r2(x, K_[m.group(4)]) * y if z == x else x * r2(y, K_[m.group(4)])), 'G8 schatten met afrondafspraak')
    if (m := re.search(r'liggen (\d+) [a-zà-ÿ]+ en er komen (\d+) bij\. Schat het totaal: rond beide getallen af op (\w+) en tel op', o)) and m.group(3) in K_:
        k = K_[m.group(3)]; return uit(Fr(r2(int(m.group(1)), k) + r2(int(m.group(2)), k)), 'G8 schatten met afrondafspraak')
    if (m := re.fullmatch(r'Op welk cijfer eindigt (\d+) × (\d+)\?', o.strip())): return uit(Fr(int(m.group(1)) * int(m.group(2)) % 10), 'G8 laatste cijfer')
    N_ = lambda x: int(x.replace('.', ''))
    if (m := re.search(r'schaal (?:van een kaart is )?1 : ([\d.]+)\.? .*?op de kaart (\d+(?:,\d+)?) cm uit elkaar\. Hoeveel km', o)):
        return uit(_bedrag(m.group(2)) * N_(m.group(1)) / 100000, 'G8 schaal kaart → km')
    if (m := re.search(r'schaal (?:van een kaart is )?1 : ([\d.]+)\.? .*?in het echt (\d+(?:,\d+)?) km uit elkaar\. Hoeveel cm', o)):
        return uit(_bedrag(m.group(2)) * 100000 / N_(m.group(1)), 'G8 schaal km → kaart')
    if (m := re.search(r'schaal 1 : ([\d.]+) is de afstand .*? (\d+(?:,\d+)?) cm\. Hoeveel meter', o)):
        return uit(_bedrag(m.group(2)) * N_(m.group(1)) / 100, 'G8 schaal kaart → m')
    if (m := re.search(rf'kost na (\d+)% korting {E}\. Wat was de prijs vóór de korting', o)):
        return uit(_bedrag(m.group(2)) * 100 / (100 - int(m.group(1))), 'G8 prijs vóór korting')
    if (m := re.search(r'Vorig jaar waren er (\d+) [a-zà-ÿ]+, nu (\d+)\. Met hoeveel procent is dat (gestegen|gedaald)', o)):
        x, y = int(m.group(1)), int(m.group(2)); return uit(Fr(abs(y - x) * 100, x), 'G8 procent erbij/eraf')
    if (m := re.match(r'(\d+)(?:/(\d+))? .*?(?:in stukken van|in bekers van|verdeeld in stukken van) (\d+)/(\d+)', o)):
        x = Fr(int(m.group(1)), int(m.group(2) or 1)); return uit(x / Fr(int(m.group(3)), int(m.group(4))), 'G8 delen door een breuk')
    if (m := re.search(r'Een spaartabel: week (\d+) → €(\d+), week (\d+) → €(\d+), week (\d+) → €(\d+)\. Wat staat er bij week (\d+)\?', o)):
        w0, b0, w1, b1 = (int(m.group(k)) for k in (1, 2, 3, 4)); st_ = Fr(b1 - b0, w1 - w0)
        return uit(b0 + st_ * (int(m.group(7)) - w0), 'G8 spaartabel (vaste stap)')
    if (m := re.search(r'In een (\w+) passen (\d+) (\w+)\. Er zijn (\d+) \3\.', o)):
        per, n = int(m.group(2)), int(m.group(4))
        if 'blijven er over' in o: return uit(Fr(n % per), 'G8 rekenmachine: rest')
        if 'nodig' in o: return uit(Fr(math.ceil(n / per)), 'G8 rekenmachine: naar boven afronden')
    return None
def hercontrole_g8(it, q):
    c = it['controle']; c['claudeVorm'] = {'antwoord': c['antwoord'], 'verwacht': c['verwacht'], 'methode': c['methode']}
    v = verify_g8(it)
    if v is None: v = BG7.verify(it)
    if v is None: v = R7.verify_g7(it, q)
    if v is None: v = R6.verify_g6(it, q)
    if v is None: v = R5.verify_g5(it, q)
    if v is None: v = R4.verify_g4(it, q)
    if v is None: v = M.verify2(it)
    if v is None:
        opts = [o['tekst'] for o in it['opties']] if it['opties'] else None
        v = B3.verify(q, it['opgave'].replace('□', '__').replace('\n', ' '), it['antwoord'], opts)
    c['antwoord'], c['verwacht'], c['methode'] = v[0], v[1], v[2]
    opts = [o['tekst'] for o in it['opties']] if it['opties'] else None
    c['mcAntwoordInOpties'] = (it['antwoord'] in opts) if opts else None
    c['dubbeleOptie'] = bool(opts) and len(set(opts)) != len(opts)
    c['foutAntwoordGelijkAanGoed'] = any(f['fout'] == it['antwoord'] for f in it['foutHints'])
    c['notatie'] = R7.notatie_check_g7(it)
    u = ' '.join(x for x in (it['extraVelden'].get('claudeUitleg'), it['extraVelden'].get('claudeUitlegOudeVakcode')) if x)
    zinnen = [z.strip() for z in re.split(r'(?<=[.?!])\s+', u) if len(z.strip()) >= 20]
    kind = [it['opgave']] + [o['tekst'] for o in it['opties'] or []] + [f['uitleg'] or '' for f in it['foutHints']]
    c['claudeUitlegInKindtekst'] = any(z in k for z in zinnen for k in kind) or None

ST_TAG = {'gemapt': 'claude-bank', 'twijfel': 'claude-bank-twijfel', 'terug-G7': 'claude-bank-terug', 'buiten-basisschool': 'claude-bank-buiten',
          'naar-G4': 'claude-bank-naar', 'naar-G5': 'claude-bank-naar', 'naar-G6': 'claude-bank-naar', 'naar-G7': 'claude-bank-naar'}
TWIJFELVRAAG = {
    'schatten-zonder-afspraak': "'Hoeveel is 34 − 22 ongeveer?' zonder afspraak hoe je afrondt: een afrondafspraak in de vraag zetten (zoals 'Rond af op tientallen') en dan G8-GET-E02, of schrappen?",
    'kan-kloppen-zonder-opties': "'Kijk zonder uit te rekenen. Welk antwoord bij 25 × 5 kan kloppen?' is open (geen keuzes): drie keuzes erbij maken (G8-GET-E02) of schrappen?",
    'negatief-zonder-context': "'Welk getal ligt 7 lager dan 1?' (217 items, uit de G7-park): G8-MEET-E05 gaat over temperatuur en de getallenlijn. Zo laten (kaal, met getallenlijn), in een temperatuurcontext zetten, of schrappen?",
    'vakcode-plattegrond': "'Wat staat er in vak E2?' (plattegrond met vakcodes) is G4–G6-niveau. Terug naar een lagere groep, of schrappen? (G8-VBN-V01 gaat over coördinaten (x, y).)",
    'bouwsel-tellen': "Blokjes tellen in een bouwsel ('Dit bouwwerk is helemaal vol …', 551 items): er is geen G8-doel voor. G7/G6 (ruimtelijk), G8-MKU-V01, of schrappen?",
    'geheugenomvang': "Geheugenomvang (MB/GB/TB, foto's op een kaart): geen SLO-doel. G8-MEET-E03 (maten als systeem), G8-GET-E05, of schrappen?",
    'kans': "Kans ('Je pakt zonder kijken …'): in G7 zette Didactiek kans bij G7-VERH-04 (breuk). In G8 ook (G8-VERH-E01: telling ↔ breuk ↔ %), of buiten de basisschool?",
    'statistiek-gemengd': "Claude-doel G9 'Statistiek' is gemengd (verschil, uitschieter, gemiddelde, gewone keersommen). Per item: G8-VBN-E01/E04, lager, of schrappen?",
}

def main():
    for p in ('data/per_doel', 'somtypen', 'logs', 'bevroren', 'hints'): os.makedirs(f'{OUT}/{p}', exist_ok=True)
    for d in ('data/per_doel', 'somtypen'):
        for f in os.listdir(f'{OUT}/{d}'): os.remove(f'{OUT}/{d}/{f}')
    pool, al, al_reden, niet = [], collections.Counter(), collections.Counter(), collections.Counter()
    for q in V:
        if q['doel'] not in KANDIDAAT and q['id'] not in G7PARK: continue
        if q['id'] in gebruikt: al[q['doel']] += 1; al_reden[gebruikt[q['id']]] += 1; continue
        pool.append(q)
    rows, GESCHRAPT, onbekend = [], [], []
    mlog, slog = B3.mlog, B3.slog
    for q in pool:
        p7 = G7PARK.get(q['id'])
        r = classify_g8(q, p7)
        if r['status'] == 'niet': onbekend.append(q); niet[q['doel']] += 1; continue
        d8 = BESLUIT_G8.get(q['id'])
        if d8:      # Didactiek-besluit (g8/besluiten_twijfel.json)
            assert r['status'] == 'twijfel', ('besluit voor een item dat geen twijfel is', q['id'], r['status'])
            r = BG8.classify(d8)
            if r['status'] == 'schrappen':
                GESCHRAPT.append({'claudeId': q['id'], 'id': None, 'groep': f"Didactiek: {d8['redencode']}", 'subregel': d8['subregel'], 'doel': d8['voorstelDoel'], 'vraag': q['vraag']}); continue
        elif BESLUIT_G8 and q['id'] == E02_001:      # Dave 20:56 (5): G8-GET-E02-001 (4 × 198) → G5-GET-E07
            assert r['status'] == 'gemapt' and r['doel'] == 'G8-GET-E02', r
            r = dict(r, status='naar-G5', doel='G5-GET-E07', reden=r['reden'] + '; besluit Dave 20:56 (5): getallen en uitkomst onder 1000 → G5-GET-E07')
        st, doel = r['status'], r['doel']
        it = B3.convert(q, 'gemapt' if st == 'gemapt' else st, doel, r['regel'], r['reden'])
        it['merge']['status'] = st
        if st != 'gemapt': it['doelId'] = None; it['merge']['doel'] = None; it['merge']['voorstelDoel'] = doel
        if r['cat']: it['merge']['twijfelCategorie'] = r['cat']
        if r['aanvulling']: it['merge']['aanvullingG7'] = True
        if p7: it['merge']['g7Park'] = {'id': p7['id'], 'voorstelDoel': p7['merge']['voorstelDoel'], 'regel': p7['merge']['regel']}
        it['bron']['claudeGroep'] = CDOEL[q['doel']]['groep']
        M.bewerk(it, mlog, slog)
        R4.bewerk_g4(it, q, M, mlog, slog)
        it['getallenruimte'] = B7.getallenruimte(it, q)
        R5.bewerk_g5(it, q, M, mlog, slog)
        R6.bewerk_g6(it, q, M, mlog, slog)
        R7.bewerk_g7(it, q, M, mlog, slog, None)
        BG7.algemeen(it, M, slog, None)
        FX21.pas_toe(it, slog, "G8-FX21 (G5-fixlijst #21/#49): Engelse woorden vervangen, ook in extraVelden")
        bewerk_g8(it, slog)
        if d8: BG8.bewerk(it, d8, M, slog)
        if BESLUIT_G8 and st == 'terug-G7' and (d5 := BG8.context_terug(it, slog)):      # Dave 20:56 (3)/(4): T1/T8 → G5
            it['merge']['status'] = 'naar-G5'; it['merge']['voorstelDoel'] = d5; it['merge']['reden'] += f"; besluit Dave 20:56 (4): naar G5 ({d5})"
        if BESLUIT_G8 and st == 'buiten-basisschool': BG8.mediaan_tekst(it, slog)
        if BESLUIT_G8: BG8.zonder_kans(it, slog)      # Dave 22:06 (1): geen 'kans' in G8
        if it['merge']['status'] == 'gemapt': fix_g8(it, slog)      # alleen G8-items: de aanvulling voor G4–G7 blijft gelijk (goedgekeurde builds)
        if it['merge']['status'] == 'gemapt' and BV.pas_toe(it): slog(it, 'G8-BV170 (G6-fixlijst #170, Dave 21:24; V-#760): even grote breuk telt als goed (antwoordOokGoed), behalve als de opgave een vorm vraagt', 'antwoordOokGoed', None, it['antwoordOokGoed'][:6])
        hercontrole_g8(it, q)
        it['licentie']['wijzigingen'] = sorted({f['soort'] for f in B3.FIXLOG if f['id'] == q['id']}); it['licentie']['gewijzigd'] = True
        it['merge']['somtype'] = kop_g8(BG7.somtype(it) or B7.somtype_g7(it))
        if (pl_ := it.pop('_plek496', None)):      # Oef-#496: de kop volgt de oude indeling (somtypes blijven gelijk, geen nieuw bevroren somtype)
            it['merge']['somtype'] = re.sub(r'uit (?:Amsterdam|Rotterdam|Eindhoven|Groningen|Maastricht)\.', 'uit ' + (PLEK496[pl_] if pl_ in ('de school', 'de klas', 'het huis') else '[plek]') + '.', it['merge']['somtype'], count=1)
        if it['merge']['status'] == 'gemapt' and (n_kt := KF.zet_om(it)):      # besluit kloktijden (Didactiek 8 okt 15:46): '14.30 uur', typ-invoer '(Typ als 14.30.)'
            slog(it, f"G8-KLOK (besluit Didactiek 15:46): kloktijd als '14.30 uur', geen ':' ({n_kt} tijden; typ-invoer: geldigeAntwoorden 14.30 uur / 14.30 / 14:30)", 'opgave', None, it['opgave'][:80])
        rows.append(it)
    # Oef-#1001 (G8 batch 6): staat op een [ding]-plek in elk item van het somtype hetzelfde woord (hectare, milliliter, erbij), dan staat dat woord vast in de kop
    # (tools/kop_vast.py). Alleen de doelen van batch 6 (MEET-E07, MEET-V01, VBN-E01, VBN-E03, VBN-E04); de goedgekeurde batches 1–5 houden hun koppen.
    K1001 = KV.vast_woorden([r for r in rows if r['merge']['status'] == 'gemapt' and r['merge'].get('doel') in KOP1001_DOELEN], min_items=1)
    for r in rows:
        k_ = (r['merge'].get('doel'), r['merge'].get('somtype'))
        if r['merge']['status'] == 'gemapt' and k_ in K1001:
            slog(r, 'Oef-#1001: vast woord op een [ding]-plek in de kop', 'somtype', k_[1], K1001[k_]); r['merge']['somtype'] = K1001[k_]
    # V-#946/Z-#945 (Didactiek b7): de koppen volgen de opgave ('(× #)', kop tussen aanhalingstekens)
    for r in rows:
        if B7VLAG.ACTIEF and r['merge']['status'] == 'gemapt' and r['merge'].get('doel') == 'G8-VBN-E04':
            k_ = r['merge'].get('somtype', ''); k2 = k_.replace('zijn de staven samen # hoog', 'tellen de staven samen op tot #').replace('aantal bezoekers (x #)', 'aantal bezoekers (× #)').replace('staat: Het aantal bezoekers is verdubbeld. De staaf', 'staat: "Het aantal bezoekers is verdubbeld." De staaf')
            if k2 != k_: r['merge']['somtype'] = k2; slog(r, 'V-#946/Z-#945: kop volgt de opgave', 'somtype', k_, k2)
    # Oef-#1004 (b7, #21): nieuwe somtype-template uit merge-fixlijst.md ('[plek]' vangt 'Bij het asiel' niet; '[ding]' viel op 'hele'/'half'); na Oef-#1001, zodat [ding] blijft
    for r in rows:
        if B7VLAG.ACTIEF and r['merge']['status'] == 'gemapt' and r['merge'].get('somtype', '').startswith('In een plaatjesgrafiek staat één hondje voor # [ding]. In [plek] staan # [ding] hondjes en # [ding] hondje.'):
            k_ = r['merge']['somtype']; r['merge']['somtype'] = 'In een plaatjesgrafiek staat één hondje voor # [ding]. [Plek] staan # hele hondjes en # half hondje. Hoeveel [ding] zijn dat?'
            slog(r, 'Oef-#1004: somtype-template', 'somtype', k_, r['merge']['somtype'])
    # Fase 1 (V-#1020/#1021/Z-#1022): E05-koppen blijven die van build 18:20:30 (hint-entries batch9 per oude kop); één kop pas met G8_KOP1014=1
    if os.environ.get('G8_KOP1014', '1') != '1':
        for r in rows:
            c8_ = r['bron']['claudeId'][:8]
            if r['merge']['status'] == 'gemapt' and r['merge'].get('doel') == 'G8-VERH-E05' and c8_ in KOPPIN_E05 and r['merge']['somtype'] != KOPPIN_E05[c8_]['kop']:
                slog(r, 'fase 1: kop van build 18:20:30 blijft (V-#1020)', 'somtype', r['merge']['somtype'], KOPPIN_E05[c8_]['kop']); r['merge']['somtype'] = KOPPIN_E05[c8_]['kop']
    # ids (bevroren)
    idp = f'{OUT}/bevroren/ids_v1.json'
    oud = json.load(open(idp))['ids'] if os.path.exists(idp) else {}
    perdoel = collections.defaultdict(list)
    for it in rows: perdoel[(it['merge']['status'], it['merge']['doel'] or it['merge']['voorstelDoel'] or 'G8-X')].append(it)
    for (st, key), its in sorted(perdoel.items()):
        its.sort(key=lambda x: (x['merge']['somtype'], x['bron']['claudeDoel'], x['bron']['claudeId']))
        pref = f"{key}-{ST_TAG[st]}-"; eigen = lambda o: o.startswith(pref) and o[len(pref):].isdigit()
        nxt = max((int(oud[it['bron']['claudeId']][len(pref):]) for it in its if eigen(oud.get(it['bron']['claudeId'], ''))), default=0)
        for it in its:
            o = oud.get(it['bron']['claudeId'], '')
            if eigen(o): it['id'] = o
            else:
                nxt += 1; it['id'] = f'{pref}{nxt:03d}'
                if o: it['merge']['vorigId'] = o
            it['nr'] = it['id'][len(pref):]
    D = json.load(open(idp)) if os.path.exists(idp) else {'uitleg': 'Bevroren item-ids G8-merge (eerste build 1 okt 2026). Bestaande ids blijven; nieuwe items krijgen het volgende vrije nummer.', 'ids': {}}
    for it in rows:      # vorige ids bewaren (twijfel-ids van de besluiten blijven zo vindbaar na een nieuwe build)
        if it['merge'].get('vorigId'):
            vs = D.setdefault('vorigeIds', {}).setdefault(it['bron']['claudeId'], [])
            if it['merge']['vorigId'] not in vs: vs.append(it['merge']['vorigId'])
    D['ids'].update({it['bron']['claudeId']: it['id'] for it in rows}); json.dump(D, open(idp, 'w'), ensure_ascii=False, indent=1)
    BG8.koppel_ids(rows, oud)      # bijnaDubbelVan / duplicaatVan van Didactiek (twijfel-ids) → nieuwe ids
    # dubbels
    seen = {}
    for it in sorted(rows, key=lambda x: x['id']):
        k = (it['merge']['status'], it['merge']['doel'] or it['merge']['voorstelDoel'], it['opgave'], json.dumps(it['visual']['jsRender'], sort_keys=True), it['optiesTekst'], it['antwoord'])
        it['merge']['duplicaatVan'] = seen.get(k); seen.setdefault(k, it['id'])
        d = it['merge']['doel']; o = re.sub(r'\s+', ' ', it['opgave']).strip()
        if d and (d, o) in ONZE_G8: it['merge']['zelfdeOpgaveAlsOnzeBank'] = ONZE_G8[(d, o)]
        if B7.pnorm(it['opgave']) in PILOT8: it['merge']['lijktOpPilot'] = PILOT8[B7.pnorm(it['opgave'])]
    weg = [r for r in rows if r['merge']['duplicaatVan']]
    for r in weg: GESCHRAPT.append({'claudeId': r['bron']['claudeId'], 'id': r['id'], 'groep': 'dubbel', 'subregel': f"dubbel van {r['merge']['duplicaatVan']}", 'doel': r['merge']['doel'] or r['merge']['voorstelDoel'], 'vraag': r['opgave']})
    rows = [r for r in rows if r not in weg]
    # Oef-#467 (8 okt): GET-E02 'Kijk zonder uit te rekenen. Welk antwoord bij a × b / a + b kan kloppen?': de goede optie stond in 27 van 27 items op A.
    # Per kop (× en +) op claudeId gesorteerd en om de beurt op A, B, C gezet; de andere opties houden hun volgorde. Letters en optiesTekst opnieuw.
    # Fout-hints gaan op de tekst van de optie (niet op de letter), dus de sleutels blijven gelijk; de sync/apply hieronder zet ze opnieuw.
    _k467 = re.compile(r'Kijk zonder uit te rekenen\. Welk antwoord bij .+ ([×+]) .+ kan kloppen\?')
    _g467 = collections.defaultdict(list)
    for r in rows:
        m_ = _k467.fullmatch(r['opgave'])
        if r['merge']['doel'] == 'G8-GET-E02' and r['type'] == 'meerkeuze' and m_ and r['antwoord'] in [o['tekst'] for o in r['opties']]:
            _g467[m_.group(1)].append(r)
    for _op, _its in _g467.items():
        for _i, r in enumerate(sorted(_its, key=lambda x: x['bron']['claudeId'])):
            teksten = [o['tekst'] for o in r['opties']]; rest = [t for t in teksten if t != r['antwoord']]; pos = _i % len(teksten)
            nieuw = rest[:pos] + [r['antwoord']] + rest[pos:]
            if nieuw != teksten:
                r['opties'] = [{'letter': 'ABCDEF'[j], 'tekst': t} for j, t in enumerate(nieuw)]
                r['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in r['opties'])
                slog(r, 'Oef-#467 goede optie verdeeld over A/B/C', 'opties', ' · '.join(teksten), r['optiesTekst'])
                ad_ = r.get('antwoordDetail')
                if isinstance(ad_, dict) and 'juisteOptie' in ad_: ad_['juisteOptie'] = r['opties'][pos]['letter']; ad_['juisteOptieTekst'] = r['antwoord']
                r['licentie']['wijzigingen'] = sorted(set(r['licentie']['wijzigingen']) | {'Oef-#467 goede optie verdeeld over A/B/C'})
    gem = [r for r in rows if r['merge']['status'] == 'gemapt']; twf = [r for r in rows if r['merge']['status'] == 'twijfel']
    t7 = [r for r in rows if r['merge']['status'] == 'terug-G7']; bui = [r for r in rows if r['merge']['status'] == 'buiten-basisschool']
    aanv = [r for r in t7 if r['merge'].get('aanvullingG7')]
    naar = {g: [r for r in rows if r['merge']['status'] == f'naar-G{g}'] for g in (4, 5, 6, 7)}
    nu = subprocess.check_output(['date', '+%Y-%m-%dT%H:%M:%S%z']).decode().strip()
    meta = {'schema': 'leermees-vragenbank-export/v1 + merge/controle/licentie (claude-merge g8)', 'bron': CREDIT, 'gegenereerdOp': nu,
            'g7Basis': 'g7/scripts 1 okt 18:15 (kopie in scripts/g7_basis/, met g6_basis/g5_basis/g4_basis_1435/)'}
    B7.OUT, B7.OURS, B7.TWIJFELVRAAG = OUT, OURS, TWIJFELVRAAG
    eerste = not os.path.exists(f'{OUT}/bevroren/somtype_nr_v1.json')
    snap = B7.somtype_nummers(gem)
    if eerste:
        p = f'{OUT}/bevroren/somtype_nr_v1.json'; S = json.load(open(p)); S['uitleg'] = S['uitleg'].replace('G7', 'G8'); json.dump(S, open(p, 'w'), ensure_ascii=False, indent=1)
    for name, data, uitleg in (('gemapt', gem, None), ('terug_G7', t7, 'Claude-items uit de G8-pool die te makkelijk zijn voor G8 (terug-G7, voorstelDoel = G7-doel).'),
                               ('buiten_basisschool', bui, 'Claude-items die niet in de basisschool horen (machten, wortels, negatief × negatief, letters als getal, modus, mediaan). Niet gebruiken.')):
        json.dump(dict(meta, **({'uitleg': uitleg} if uitleg else {}), aantal=len(data), items=sorted(data, key=lambda x: x['id'])), open(f'{OUT}/data/{name}.json', 'w'), ensure_ascii=False, indent=1)
    # vaste route G8 → G4–G7 (Dave 20:38 #3 / 20:56): g{N}/data/aanvulling_uit_g8.json; build_gN leest hem in (tools/aanvulling_g8.py)
    os.makedirs(AANV_UIT, exist_ok=True)
    for g, G_ in ((4, G4), (5, G5), (6, G6), (7, G7)):
        its = naar[g] + (aanv if g == 7 else [])
        if g != 7 and not BESLUIT_G8: continue          # zonder besluitenbestand: niets nieuws voor G4–G6 (de uitkomst blijft gelijk)
        json.dump(dict(meta, uitleg=(f'Claude-items uit de G8-pool voor G{g}: besluiten Didactiek (g8/besluiten_twijfel.json) en Dave 20:56. ' if g != 7 else
                                     'Claude-items uit de G8-pool voor G7: terug-G7 met een passend G7-doel en besluiten Didactiek/Dave 20:56. ') +
                       f'build_g{g} leest dit bestand (tools/aanvulling_g8.py): de items komen achter de bestaande items, met merge.voorstelDoel als doelId. Ids hier zijn G8-ids (merge.uitG8.g8Id in G{g}).',
                       aantal=len(its), perDoel=dict(collections.Counter(r['merge']['voorstelDoel'] for r in its)), items=sorted(its, key=lambda x: x['id'])),
                  open(f'{AANV_UIT}/g{g}.json', 'w'), ensure_ascii=False, indent=1)      # Z-#962: nooit direct live; bouw_veilig zet hem na controle om
    cats = collections.defaultdict(list)
    for r in twf: cats[r['merge']['twijfelCategorie']].append(r)
    json.dump(dict(meta, aantal=len(twf), categorieen={c: {'aantal': len(v), 'voorstelDoelen': dict(collections.Counter(r['merge']['voorstelDoel'] for r in v)),
               'redenen': dict(collections.Counter(r['merge']['reden'] for r in v)), 'vraag': TWIJFELVRAAG.get(c, ''), 'items': sorted(v, key=lambda x: x['id'])}
               for c, v in sorted(cats.items(), key=lambda x: -len(x[1]))}), open(f'{OUT}/data/twijfel.json', 'w'), ensure_ascii=False, indent=1)
    for doel in sorted(OURS):
        its = [r for r in gem if r['merge']['doel'] == doel]
        if its: json.dump(dict(meta, doelId=doel, bordtitel=OURS[doel]['bordtitel'], aantal=len(its), items=sorted(its, key=lambda x: x['id'])), open(f'{OUT}/data/per_doel/{doel}.json', 'w'), ensure_ascii=False, indent=1)
    with open(f'{OUT}/logs/geschrapt.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['claudeId', 'id', 'groep', 'subregel', 'doel', 'vraag']); w.writeheader(); w.writerows(GESCHRAPT)
    with open(f'{OUT}/logs/fixes.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'soort', 'veld', 'voor', 'na']); w.writeheader(); w.writerows(B3.FIXLOG)
    with open(f'{OUT}/logs/antwoordcontrole.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['id', 'claudeId', 'status', 'doel', 'controle', 'methode', 'antwoord', 'verwacht', 'opgave'])
        for r in rows: c = r['controle']; w.writerow([r['id'], r['bron']['claudeId'], r['merge']['status'], r['merge']['doel'] or r['merge']['voorstelDoel'], c['antwoord'], c['methode'], r['antwoord'], c['verwacht'], r['opgave']])
    if onbekend: json.dump([{'id': q['id'], 'doel': q['doel'], 'vraag': q['vraag']} for q in onbekend], open(f'{OUT}/logs/geen_regel.json', 'w'), ensure_ascii=False, indent=1)
    perdoel_tel = collections.defaultdict(collections.Counter)
    for r in rows: perdoel_tel[r['merge']['doel'] or r['merge']['voorstelDoel'] or '—'][r['merge']['status']] += 1
    stats = {'gegenereerdOp': nu, 'kandidaatDoelen': KANDIDAAT, 'pool': len(pool), 'g7ParkInPool': sum(1 for q in pool if q['id'] in G7PARK), 'g7ParkTotaal': len(G7PARK),
             'alInG3G7': {'totaal': sum(al.values()), 'perClaudeDoel': dict(al), 'reden': dict(al_reden)}, 'geenRegel': dict(niet),
             'perStatus': dict(collections.Counter(r['merge']['status'] for r in rows)), 'aanvullingG7': len(aanv),
             'naarGroep': {f'G{g}': dict(collections.Counter(r['merge']['voorstelDoel'] for r in naar[g])) for g in naar},
             'besluitenG8': bool(BESLUIT_G8),
             'geschrapt': dict(collections.Counter(g['groep'] for g in GESCHRAPT)), 'perDoel': {k: dict(v) for k, v in sorted(perdoel_tel.items())},
             'perClaudeDoel': {cd: dict(collections.Counter(r['merge']['status'] for r in rows if r['bron']['claudeDoel'] == cd)) for cd in sorted({r['bron']['claudeDoel'] for r in rows})},
             'twijfelCategorieen': {c: len(v) for c, v in cats.items()},
             'buitenBasisschool': dict(collections.Counter(r['merge']['reden'].split(':')[0] for r in bui)),
             'controle': {f'{a}|{b}': n for (a, b), n in collections.Counter((r['merge']['status'], r['controle']['antwoord']) for r in rows).items()},
             'controleMethode': dict(collections.Counter(r['controle']['methode'] for r in gem).most_common(25)),
             'notatie': {f'{a}|{b}': n for (a, b), n in collections.Counter((r['merge']['status'], h) for r in rows for h in r['controle']['notatie']).items()},
             'zelfdeOpgaveAlsOnzeG8': sum(1 for r in gem if r['merge'].get('zelfdeOpgaveAlsOnzeBank')), 'lijktOpPilot': sum(1 for r in rows if r['merge'].get('lijktOpPilot'))}
    json.dump(stats, open(f'{OUT}/logs/stats.json', 'w'), ensure_ascii=False, indent=1)
    B7.write_somtypen(gem, twf, snap)
    for f in os.listdir(f'{OUT}/somtypen'):
        p = f'{OUT}/somtypen/{f}'; s = open(p).read()
        open(p, 'w').write(s.replace('onze G7-bank', 'onze G8-bank').replace('Uit de G6-park', 'Uit de G6-park (n.v.t.)').replace('Lijkt op een G7-pilot', 'Lijkt op een G8-pilot'))
    p = f'{OUT}/somtypen/G8-VERH-E06.md'; s = open(p).read(); k_ = '## Somtype 1: Schrijf # in procenten.\n'
    if k_ in s and 'Z-#1063' not in s:      # Z-#1063 (Didactiek, bij V-#1060): marge 0
        s = s.replace(k_, k_ + "\n> **Z-#1063 (vormcue, marge 0):** dit somtype heeft maar twee eerlijke posities voor het goede antwoord: middelste en grootste. Kleinste kan niet met een echte denkfout: alleen 'komma drie plekken' ligt boven het antwoord. Na V-#1060 staat het op 0 / 48 / 48 (kleinste / middelste / grootste). Een nieuw item moet middelste en grootste op 1 : 1 houden, anders vuurt de vormcue-regel (> 50 %, p < 0,01). Guard: `check_merge_notatie` Z-#1063. 'Nooit de kleinste' blijft om deze reden INFO.\n", 1)
        open(p, 'w').write(s)
    twijfel_md(cats, bui, t7)
    # Oef-#493 (G8 batch 5): vaste volgorde voor patchrondes die van de data afhangen. 1 data (hierboven) → 2 sync → 3 alle hints/patch_batch*.py
    # (idempotent; ze zien de nieuwe koppen en items) → 4 opnieuw sync (een patch kan een kop of nrOrigineel raken) → 5 apply. Elke fase staat met tijd in
    # logs/build_fase.json, en een patch ziet de fase in de omgevingsvariabele G8_BUILD_FASE ('na-sync-1'); buiten de build is die leeg.
    fase = {'build': nu, 'fasen': []}
    def _fase(naam):
        fase['fasen'].append({'fase': naam, 'op': subprocess.check_output(['date', '+%Y-%m-%dT%H:%M:%S%z']).decode().strip()})
        json.dump(fase, open(f'{OUT}/logs/build_fase.json', 'w'), ensure_ascii=False, indent=1)
    _fase('1 data geschreven')
    subprocess.run([sys.executable, '-B', f'{HERE}/sync_hint_keys.py'], check=True); _fase('2 sync')
    env = dict(os.environ, G8_BUILD_FASE='na-sync-1', PYTHONDONTWRITEBYTECODE='1')
    pb = sorted(glob.glob(f'{OUT}/hints/patch_batch*.py'), key=lambda x: int(re.search(r'patch_batch(\d+)', x).group(1)))
    for p_ in pb: subprocess.run([sys.executable, '-B', p_], check=True, env=env, cwd=OUT)
    _fase('3 patches: ' + ', '.join(os.path.basename(x) for x in pb))
    subprocess.run([sys.executable, '-B', f'{HERE}/sync_hint_keys.py'], check=True); _fase('4 sync opnieuw')
    subprocess.run([sys.executable, '-B', f'{HERE}/apply_hints.py'], check=True); _fase('5 apply')
    return rows, gem, twf, t7, bui, stats

OEF476 = True       # V-#782 (= Oef-#476, Didactiek batch 2): afleider 'Deel 100 door 40 en doe dat keer 15'; Oefeningen schrijft regel en H1
def fix_g8(r, slog):
    """Itemfixes G8 (8 okt): Z-#766, Z-#767, Z-#768, Oef-#476, Oef-#480. Per item, vóór BV.pas_toe, de hercontrole en de kop."""
    # Z-#766 (Didactiek G8 batch 1, 8 okt): E04 #3 bank-039 (1/3, 1/2) en bank-044 (2/4, 1/3): 1/2 − 1/3 = 1/6 = het antwoord (aftrekken gaf toevallig goed).
    # Nieuwe breuken, niet al in E04 #3, zelfde routes: teller+teller/noemer+noemer, de overgebleven breuk. Aftrekken geeft nu iets anders.
    # E03 #4 bank-038: 35 − 4 × 7 = 7, het antwoord stond in de vraag → 40 − 4 × 7 = 12 (zelfde routes: van links naar rechts 252, plus i.p.v. keer 40 − (4 + 7) = 29).
    R8_766 = {'13482195': (('1/3', '1/2'), ('1/5', '1/2', '1/10'), [('2/7', 'teller-en-noemer-optellen'), ('1/5', 'deel-vergeten-bij-splitsen')]),
              'db461856': (('2/4', '1/3'), ('4/5', '1/3', '4/15'), [('5/8', 'teller-en-noemer-optellen'), ('1/15', 'deel-vergeten-bij-splitsen'), ('4/5', 'deel-vergeten-bij-splitsen')])}
    if True:
        c8 = (r['bron'].get('claudeId') or '')[:8]; o = r['opgave']
        if c8 in R8_766:
            (a0, b0), (a, b, ans), sl = R8_766[c8]
            assert o == f'Er is nog {a0} taart. Een kind eet daar {b0} deel van. Welk deel van de hele taart is dat? Typ een breuk.', (r['id'], o)
            ta, na = map(int, a.split('/')); tb, nb = map(int, b.split('/'))
            r['opgave'] = f'Er is nog {a} taart. Een kind eet daar {b} deel van. Welk deel van de hele taart is dat? Typ een breuk.'; r['antwoord'] = ans
            ex = r['extraVelden']; ex['claudeDenkfouten'] = [{'fout': f, 'denkfout': d} for f, d in sl]
            ex['claudeFoutHints'] = [{'stap': None, 'fout': f, 'uitleg': None} for f, d in sl]
            ex['claudeKaleSom'] = f'{b} × {a}'
            ex['claudeUitleg'] = f'Deel van een deel: vermenigvuldig tellers en noemers.\n{tb} × {ta} = {tb * ta}, {nb} × {na} = {nb * na}.\nDus {ans}.'
            r['foutHints'] = []; BV.pas_toe(r)
            slog(r, 'Z-#766: aftrekken gaf toevallig het antwoord (1/2 − 1/3 = 1/6)', 'opgave', o, r['opgave'])
        if c8 == '574c9352' and o == 'Reken uit. 35 − 4 × 7':
            r['opgave'] = 'Reken uit. 40 − 4 × 7'; r['antwoord'] = '12' if isinstance(r['antwoord'], str) else 12
            ex = r['extraVelden']; ex['claudeDenkfouten'] = [{'fout': '252', 'denkfout': 'verkeerde-bewerking'}, {'fout': '29', 'denkfout': 'optellen-ipv-vermenigvuldigen'}]
            ex['claudeFoutHints'] = [{'stap': None, 'fout': '252', 'uitleg': 'Keer gaat vóór min. Eerst de keersom, dan pas aftrekken.'},
                                     {'stap': None, 'fout': '29', 'uitleg': 'Er staat een keerteken: eerst vermenigvuldigen, dan pas aftrekken.'}]
            ex['claudeKaleSom'] = '40 − 4 × 7'; ex['claudeUitleg'] = 'Eerst vermenigvuldigen: 4 × 7 = 28. Dan 40 − 28 = 12.'
            slog(r, 'Z-#766: het antwoord stond in de vraag (35 − 4 × 7 = 7)', 'opgave', o, r['opgave'])
    # Z-#767 (Didactiek G8 batch 1): elk open antwoord met een duizendpunt heeft ook de vorm zonder punt in geldigeAntwoorden
    # (E02 #2/#3/#4/#6/#7 hadden die lijst al; #8/#10/#11 niet, o.a. 054 '10.000').
    if True:
        a = str(r['antwoord'])
        if r['type'] in ('kale', None) and re.fullmatch(r'\d{1,3}(?:\.\d{3})+', a):
            g = list(r.get('geldigeAntwoorden') or [])
            for x in (a, a.replace('.', '')):
                if x not in g: g.append(x)
            if g != (r.get('geldigeAntwoorden') or []): slog(r, 'Z-#767: geldigeAntwoorden met en zonder duizendpunt', 'geldigeAntwoorden', r.get('geldigeAntwoorden'), g)
            r['geldigeAntwoorden'] = g
    # Z-#768 (Didactiek G8 batch 1, Oef-#471): contexten die niet kloppen (E02 #8 en #11).
    R8_768 = {'64e96cb9': ('tanden', 'knikkers'), 'aff44739': ('In het nest liggen 2640 schelpen', 'Op het strand liggen 2640 schelpen'),
              'd26ecfc9': ('In het huis liggen 2509 stenen', 'Op de bouwplaats liggen 2509 stenen'), 'd045f9e8': ('In de klas liggen 2220 pakken', 'In het magazijn liggen 2220 pakken'),
              'bf70ae98': ('In het stadion liggen 2137 stickers', 'In de winkel liggen 2137 stickers')}
    if True:
        c8 = (r['bron'].get('claudeId') or '')[:8]
        if c8 in R8_768 and R8_768[c8][0] in r['opgave']:
            a, b = R8_768[c8]; o = r['opgave']; r['opgave'] = o.replace(a, b)
            for k in ('claudeUitleg', 'claudeKaleSom'):
                if isinstance(r['extraVelden'].get(k), str): r['extraVelden'][k] = r['extraVelden'][k].replace(a, b)
            slog(r, 'Z-#768: context die niet klopt', 'opgave', o, r['opgave'])
    # Oef-#476 / V-#782 (8 okt): GET-E02 #32 (bank-033) afleider 'Deel 15 door 100 en doe dat keer 40 procent' gaf hetzelfde getal (6) als het antwoord → 'Deel 100 door 40 en doe dat keer 15' (noemt ook honderd, les 234).
    # Oef-#480: GET-E02 #29 (bank-030) 'In een grafiek' → 'In een staafgrafiek' (de opties gaan over staven).
    if True:
        c8 = (r['bron'].get('claudeId') or '')[:8]
        if c8 == '5617ea49' and OEF476:      # wacht op de literal-regel van Oefeningen in patch_batch2 (anders ONLEESBAAR-WARN)
            oud, nieuw = 'Deel 15 door 100 en doe dat keer 40 procent', 'Deel 100 door 40 en doe dat keer 15'
            if any(o_['tekst'] == oud for o_ in r['opties']):
                voor = r['optiesTekst']
                for o_ in r['opties']:
                    if o_['tekst'] == oud: o_['tekst'] = nieuw
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                ex = r['extraVelden']
                for d_ in ex.get('claudeDenkfouten') or []:
                    if d_['fout'] == oud: d_['fout'] = nieuw; d_['denkfout'] = 'verkeerde-bewerking'
                for h_ in ex.get('claudeFoutHints') or []:
                    if h_['fout'] == oud: h_['fout'] = nieuw; h_['uitleg'] = 'Dan deel je honderd door het aantal leerlingen. Hoeveel leerlingen is één procent: welk getal deel je door honderd?'
                slog(r, 'Oef-#476: afleider gaf hetzelfde getal als het antwoord', 'opties', voor, r['optiesTekst'])
        # V-#781 (Didactiek G8 batch 2): #16 kloktijden zonder ':' ('14.35 uur'); meerkeuze, dus geen geldigeAntwoorden nodig
        if c8 == '3d1a93e4' and '14:35' in r['opgave']:
            vv = [('14:35', '14.35 uur'), ('16:10', '16.10 uur'), ('15:00', '15.00 uur')]
            def kl(t):
                for a_, b_ in vv: t = t.replace(a_, b_)
                return t
            o = r['opgave']; r['opgave'] = kl(o); r['antwoord'] = kl(r['antwoord'])
            for o_ in r['opties']: o_['tekst'] = kl(o_['tekst'])
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            ad_ = r.get('antwoordDetail')
            if isinstance(ad_, dict) and ad_.get('juisteOptieTekst'): ad_['juisteOptieTekst'] = kl(ad_['juisteOptieTekst'])
            ex = r['extraVelden']
            for k in ('claudeUitleg', 'claudeKaleSom'):
                if isinstance(ex.get(k), str): ex[k] = kl(ex[k])
            for d_ in ex.get('claudeDenkfouten') or []: d_['fout'] = kl(d_['fout'])
            for h_ in ex.get('claudeFoutHints') or []: h_['fout'] = kl(h_['fout']); h_['uitleg'] = kl(h_['uitleg']) if isinstance(h_.get('uitleg'), str) else h_.get('uitleg')
            slog(r, "V-#781: kloktijden als '14.35 uur' (geen ':')", 'opgave', o, r['opgave'])
        # V-#820 (Didactiek batch 3, vervangt Oef-#485): V02 #3 — 12 × 5, 6 × 7, 2 × 9 → (60 + 42 + 18) : 20 = 6; meest 5, midden 5; 6 is geen gegeven cijfer. Opties 6 · 7 · 120.
        if c8 == '0f2334ef' and 'Tien kinderen hebben een 7' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('Tien kinderen hebben een 7, vijf kinderen een 8 en vijf kinderen een 6.', 'Twaalf kinderen hebben een 5, zes kinderen een 7 en twee kinderen een 9.')
            assert r['opgave'] != o, 'V-#820'
            r['opties'] = [{'letter': L_, 'tekst': t_} for L_, t_ in zip('ABC', ['6', '7', '120'])]; r['antwoord'] = '6'
            if 'geldigeAntwoorden' in r: r['geldigeAntwoorden'] = ['6']
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoordDetail'] = dict(r.get('antwoordDetail') or {}, juisteOptie='A', juisteOptieTekst='6')
            ex = r['extraVelden']; ex['claudeUitleg'] = 'Twaalf kinderen hebben samen 60 punten, zes kinderen samen 42 en twee kinderen samen 18. Bij elkaar is dat 120. Je deelt door 20 kinderen: 120 : 20 = 6. Het gemiddelde cijfer is 6.'
            ex['claudeDenkfouten'] = [{'fout': '120', 'denkfout': 'deel-vergeten-bij-splitsen'}, {'fout': '7', 'denkfout': None}]
            ex['claudeFoutHints'] = [{'stap': None, 'fout': '120', 'uitleg': None}, {'stap': None, 'fout': '7', 'uitleg': None}]
            slog(r, 'V-#820: gemiddelde 6 is geen gegeven cijfer, ≠ meest voorkomend (5) en ≠ middelste (5)', 'opgave', o, r['opgave'])
        # Z-#823 + Z-#826 (Didactiek batch 3, vervangt Oef-#486): V02 #4 — «… naar school: 2 km, 7 km, 5 km en 2 km.» → 16 : 4 = 4 km; opties 4 km · 16 km · 4,5 km
        if c8 == 'd9572e3d' and '3 km, 5 km, 4 km en 4 km' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('naar school. 3 km, 5 km, 4 km en 4 km.', 'naar school: 2 km, 7 km, 5 km en 2 km.')
            assert r['opgave'] != o, 'Z-#823'
            r['opties'] = [{'letter': L_, 'tekst': t_} for L_, t_ in zip('ABC', ['4 km', '16 km', '4,5 km'])]; r['antwoord'] = '4 km'
            if 'geldigeAntwoorden' in r: r['geldigeAntwoorden'] = ['4 km']
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoordDetail'] = dict(r.get('antwoordDetail') or {}, juisteOptie='A', juisteOptieTekst='4 km')
            ex = r['extraVelden']; ex['claudeUitleg'] = 'Je telt de afstanden op: 2 + 7 + 5 + 2 = 16. Daarna deel je door 4 dagen: 16 : 4 = 4. Het gemiddelde is 4 km per dag.'
            ex['claudeDenkfouten'] = [{'fout': '16 km', 'denkfout': 'deel-vergeten-bij-splitsen'}, {'fout': '4,5 km', 'denkfout': None}]
            ex['claudeFoutHints'] = [{'stap': None, 'fout': '16 km', 'uitleg': None}, {'stap': None, 'fout': '4,5 km', 'uitleg': None}]
            slog(r, 'Z-#823/Z-#826: 2, 7, 5, 2 km (gemiddelde 4 is geen gegeven afstand); afstanden als zin', 'opgave', o, r['opgave'])
        # V-#850 (Didactiek 8 okt 16:15, g8/gemiddelde-check-didactiek.md, les 305): V02 #2 had twee waarden (midden = gemiddelde): een derde dag erbij.
        # 210 + 320 + 280 = 810, 810 : 3 = 270; routes: midden (210 + 320) : 2 = 265 (afleider), totaal 810 (afleider), : 2 = 405, mediaan 280, middelste genoemde 320, geen modus.
        if c8 == '22716c04' and 'op zaterdag 320 mensen en op zondag 280 mensen' in r['opgave']:
            o = r['opgave']
            r['opgave'] = 'In een zwembad zwommen op vrijdag 210 mensen, op zaterdag 320 mensen en op zondag 280 mensen. Hoeveel mensen zwommen er in die drie dagen gemiddeld per dag?'
            w850 = [210, 320, 280]; assert sum(w850) == 810 and sum(w850) % 3 == 0 and sum(w850) // 3 == 270 and 270 not in w850 and (min(w850) + max(w850)) / 2 == 265
            assert sorted(w850)[1] != 270 and w850[1] != 270, 'V-#850: een route geeft het antwoord'
            nieuw850 = {'40 mensen': '265 mensen', '300 mensen': '270 mensen', '600 mensen': '810 mensen'}
            for o_ in r['opties']: o_['tekst'] = nieuw850.get(o_['tekst'], o_['tekst'])
            assert sorted(o_['tekst'] for o_ in r['opties']) == ['265 mensen', '270 mensen', '810 mensen'], 'V-#850 opties'
            r['antwoord'] = '270 mensen'
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoordDetail'] = dict(r.get('antwoordDetail') or {}, juisteOptie=next(o_['letter'] for o_ in r['opties'] if o_['tekst'] == '270 mensen'), juisteOptieTekst='270 mensen')
            if 'geldigeAntwoorden' in r: r['geldigeAntwoorden'] = ['270 mensen']
            ex = r['extraVelden']; ex['claudeUitleg'] = 'Je telt op: 210 + 320 + 280 = 810. Daarna deel je door 3 dagen: 810 : 3 = 270. Gemiddeld zwommen er 270 mensen per dag.'
            ex['claudeDenkfouten'] = [{'fout': '810 mensen', 'denkfout': 'deel-vergeten-bij-splitsen'}, {'fout': '265 mensen', 'denkfout': 'midden-van-uitersten'}]
            ex['claudeFoutHints'] = [{'stap': None, 'fout': '810 mensen', 'uitleg': None}, {'stap': None, 'fout': '265 mensen', 'uitleg': None}]
            slog(r, 'V-#850: derde dag erbij (210, 320, 280 → 270); afleiders 265 (midden van kleinste en grootste) en 810 (totaal)', 'opgave', o, r['opgave'])
        # Oef-#492 (batch 4, les 147): M01 #1 004 '2.242.000' had de gevraagde 2 drie keer → 2.418.000 (de 2 één keer); insecten in het stadion/de klas → bos/vallei
        if c8 == '8a49e4f4' and '2.242.000' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('In het stadion leven 2.242.000 insecten', 'In het bos leven 2.418.000 insecten')
            assert r['opgave'] != o and r['opgave'].count('2') == 2, 'Oef-#492 004'      # de 2 in het getal en de 2 in de vraag
            ex = r['extraVelden']
            if ex.get('claudeUitleg'): ex['claudeUitleg'] = ex['claudeUitleg'].replace('2.242.000', '2.418.000').replace('2 miljoen 242.000', '2 miljoen 418.000')
            slog(r, "Oef-#492: '2.242.000' (de 2 drie keer) → '2.418.000'; insecten in het stadion → in het bos", 'opgave', o, r['opgave'])
        if c8 == 'd7511a09' and r['opgave'].startswith('In de klas leven'):
            o = r['opgave']; r['opgave'] = o.replace('In de klas leven', 'In de vallei leven', 1)
            slog(r, 'Oef-#492: insecten in de klas → in de vallei (les 147)', 'opgave', o, r['opgave'])
        # Oef-#496 (batch 5): vreemde contexten. MEET-E03 #1–#4 'Een bak voor knopen …' (3 m³) → een echte bak met water; MEET-E06 'Een vliegtuig vertrekt … uit de dierentuin'
        # → uit een stad (de kop met 'uit de school/klas/het huis' wordt 'uit Eindhoven/Rotterdam/Groningen', zie KOP478; de koppen blijven verschillend).
        B496 = {'ad7cab10': ('Een bak voor knopen', 'Een vijver'), '126f27ed': ('Een bak voor tanden', 'Een watertank'),
                '46c13eb4': ('Een bak voor truien', 'Een regenput'), '56326cb6': ('Een bak voor wortels', 'Een opblaaszwembad')}
        if c8 in B496 and r['opgave'].startswith(B496[c8][0]):
            o = r['opgave']; r['opgave'] = o.replace(B496[c8][0], B496[c8][1], 1)
            slog(r, "Oef-#496: vreemde context (een bak voor knopen van 3 m³) → een bak met water", 'opgave', o, r['opgave'])
        if (m_ := re.match(r'Een vliegtuig vertrekt om \S+ (?:uur )?uit (de dierentuin|het museum|het bos|de kantine|het stadion|de kleedkamer|de vallei|het nest|het veld|de schuur|de school|de klas|het huis)\.', r['opgave'])):
            o = r['opgave']; stad = PLEK496[m_.group(1)]
            r['opgave'] = o[:m_.start(1)] + stad + o[m_.end(1):]
            r['_plek496'] = m_.group(1)      # voor de kop (zie main): [plek] blijft [plek]; de koppen met 'de school/klas/het huis' krijgen hun stad
            slog(r, f"Oef-#496: vliegtuig uit {m_.group(1)} → uit {stad}", 'opgave', o, r['opgave'])
        # Oef-#496: '1 graden' → '1 graad' (MEET-E05, 17 items), in de opgave en in Claudes uitleg
        if re.search(r'(?<![\d,.])1 graden\b', r['opgave'] + ' ' + str(r['extraVelden'].get('claudeUitleg') or '')):
            o = r['opgave']; r['opgave'] = re.sub(r'(?<![\d,.])1 graden\b', '1 graad', o)
            ex = r['extraVelden']
            if isinstance(ex.get('claudeUitleg'), str): ex['claudeUitleg'] = re.sub(r'(?<![\d,.])1 graden\b', '1 graad', ex['claudeUitleg'])
            slog(r, "Oef-#496: '1 graden' → '1 graad'", 'opgave', o, r['opgave'])
        # Oef-#497 (batch 5): MEET-E05 #1 'Zet −5 op de getallenlijn' heeft geen getallenlijn in jsRender → niet live zonder beeld (heel het somtype, Z-#525)
        if re.fullmatch(r'Zet [−-]?\d+ op de getallenlijn\.', r['opgave']) and not (r['visual'].get('jsRender') or {}).get('soort'):
            if not r['visual'].get('nietLiveZonderBeeld'):
                r['visual']['nietLiveZonderBeeld'] = True
                slog(r, 'Oef-#497: stip op een getallenlijn zonder gedefinieerde lijn → visual.nietLiveZonderBeeld', 'visual', None, 'nietLiveZonderBeeld')
        # V-#870 / Z-#871 / V-#871a-b (Didactiek batch 4, 16:35; les 315/316): GET-E05 rekenmachine-verhalen waarin een foute route het goede antwoord geeft
        # (rest 1 of 2 bij 'nodig', ',5' bij 'over', antwoord = per stuk, rest = antwoord), 2 per stuk, of een busje met meer dan 8 kinderen → nieuwe getallen uit
        # de generator (tools/e05_routes.genereer: zelfde context en somtype, per stuk uit een redelijke verzameling, totaal dicht bij het oude). Claudes sleutels
        # gaan mee per denkfout (kommagetal-als-geheel / rest-vergeten = het hele getal; andere-deel-genomen = de rest ('nodig') of per stuk − rest ('over')).
        # V-#910 (hercheck 17:11): per somtype (bak × soort) hoogstens 2 items met hetzelfde antwoord / hele getal op de rekenmachine (E05_TEL); busjes 5–15
        if r['merge'].get('doel') == 'G8-GET-E05' and (L_ := ER.lees(r['opgave'])):
            tel_ = E05_TEL.setdefault((L_['bak'], L_['soort']), {'antwoord': collections.Counter(), 'heel': collections.Counter()})
            if not ER.fouten_item(r) and ER.past_spreiding(L_['p'], L_['T'], L_['soort'], tel_):
                tel_['antwoord'][ER.antwoord(L_['p'], L_['T'], L_['soort'])] += 1; tel_['heel'][L_['T'] // L_['p']] += 1; L_ = None
        else: L_ = None
        if L_:
            vk_ = E05_VOORKEUR.get(c8)      # Z-#950 (Didactiek): de door Didactiek nagerekende getallen eerst, als ze door filter en spreiding komen
            if vk_ and (L_['bak'],) + vk_ not in E05_BEZET and not ER.fouten(*vk_, L_['soort'], L_['bak']) and ER.past_spreiding(*vk_, L_['soort'], tel_): p_, T_ = vk_
            else: p_, T_ = ER.genereer(L_['bak'], L_['p'], L_['T'], L_['soort'], seed=int(c8, 16), bezet=E05_BEZET, tel=tel_)
            E05_BEZET.add((L_['bak'], p_, T_)); tel_['antwoord'][ER.antwoord(p_, T_, L_['soort'])] += 1; tel_['heel'][T_ // p_] += 1
            o = r['opgave']; a_ = ER.antwoord(p_, T_, L_['soort']); heel_, rest_ = divmod(T_, p_)
            r['opgave'] = f"In een {L_['bak']} passen {p_} {L_['ding']}. Er zijn {T_} {L_['ding']}. Op de rekenmachine staat {ER.scherm(T_, p_)}. {L_['staart']}"
            r['antwoord'] = str(a_)
            ex = r['extraVelden']; route_ = {'kommagetal-als-geheel': heel_, 'rest-vergeten': heel_, 'andere-deel-genomen': rest_ if L_['soort'] == 'nodig' else p_ - rest_}
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                L2 = []; gezien = set()
                for i_, d_ in enumerate(ex.get(k_) or []):
                    lab = d_.get('denkfout') or ((ex.get('claudeDenkfouten') or [{}] * (i_ + 1))[i_] if i_ < len(ex.get('claudeDenkfouten') or []) else {}).get('denkfout')
                    v_ = route_.get(lab)
                    if v_ is None or v_ == a_ or v_ in gezien: continue
                    gezien.add(v_); L2.append(dict(d_, fout=str(v_)))
                if ex.get(k_) is not None: ex[k_] = L2
            assert not ER.fouten_item(r), ('V-#870: nieuw E05-item haalt het filter niet', r['id'], ER.fouten_item(r))
            slog(r, f"V-#870/Z-#871/V-#871: E05 nieuwe getallen (generator, filter tools/e05_routes): {L_['p']} per {L_['bak']}, {L_['T']} → {p_}, {T_}; antwoord {a_}", 'opgave', o, r['opgave'])
        # V-#871c (Didactiek batch 4): M01 #3–#5 'Een kind heeft # miljoen … verzameld' → een fabriek / verkocht in Nederland (koppen in KOP478)
        M871 = [(r'^Een kind heeft (\d+) miljoen (stickers|knikkers) verzameld\.', r'Een fabriek maakt in een jaar \1 miljoen \2.'),
                (r'^Een kind heeft (\d+) miljoen truien verzameld\.', r'In Nederland worden in een jaar \1 miljoen truien verkocht.')]
        for a871, b871 in M871:
            if re.match(a871, r['opgave']):
                o = r['opgave']; r['opgave'] = re.sub(a871, b871, o, count=1)
                slog(r, 'V-#871c: geen kind dat miljoenen verzamelt (fabriek / verkocht in Nederland)', 'opgave', o, r['opgave'])
        # Z-#872: M01 #1 002 'In het nest leven 8.601.000 insecten' → 'in het park'
        if c8 == '3458e1fb' and r['opgave'].startswith('In het nest leven'):
            o = r['opgave']; r['opgave'] = o.replace('In het nest leven', 'In het park leven', 1); slog(r, "Z-#872: insecten in het nest → in het park", 'opgave', o, r['opgave'])
        # Z-#873: MEET-E01 003 (8 km, geen komma): claudeUitleg zonder '8,0 km' en zonder de kommazin
        if c8 == '0f4cc9f9' and '8,0 km' in str(r['extraVelden'].get('claudeUitleg') or ''):
            r['extraVelden']['claudeUitleg'] = '1 km = 1000 m.\n8 km = 8000 m.'; slog(r, "Z-#873: claudeUitleg '8,0 km' → '8 km'", 'claudeUitleg', '8,0 km', '8 km')
        # ---------- G8 batch 5, review Didactiek (16:58): V-#901, V-#902, Z-#902, Z-#905 (V-#904 zit in tools/kloktijd_fix: een duur is geen kloktijd) ----------
        # V-#901: E03 #5 filmpjes (Oef-#496): claudeUitleg opnieuw uit de getallen van het item ('foto's' → 'filmpjes'; bij 008/014/020 stond de uitleg van een ander item)
        if (m_ := re.match(r'Een filmpje is (\d+) MB\. De geheugenkaart is (\d+) GB \(1 GB = 1000 MB\)\.', r['opgave'])) and isinstance(r['extraVelden'].get('claudeUitleg'), str):
            mb_, gb_ = int(m_.group(1)), int(m_.group(2)); tot_ = gb_ * 1000; nl_ = lambda x: f'{x:,}'.replace(',', '.') if x >= 10000 else str(x)
            assert tot_ % mb_ == 0 and str(tot_ // mb_) == str(r['antwoord']), ('V-#901', c8, r['antwoord'])
            o = r['extraVelden']['claudeUitleg']; r['extraVelden']['claudeUitleg'] = f'{gb_} GB = {nl_(tot_)} MB.\n{nl_(tot_)} : {mb_} = {tot_ // mb_} filmpjes.'
            if o != r['extraVelden']['claudeUitleg']: slog(r, "V-#901: claudeUitleg uit de getallen van het item ('foto's' → 'filmpjes')", 'claudeUitleg', o, r['extraVelden']['claudeUitleg'])
            ks_ = r['extraVelden'].get('claudeKaleSom')
            if isinstance(ks_, str) and ks_ != f'{gb_} GB : {mb_} MB':      # V-#901 (17:07): bij 008/014/020 hoorde de kale som bij een ander item
                assert re.fullmatch(r'\d+ GB : \d+ MB', ks_), ('V-#901 kale som', c8, ks_)
                r['extraVelden']['claudeKaleSom'] = f'{gb_} GB : {mb_} MB'; slog(r, 'V-#901: claudeKaleSom uit de getallen van het item', 'claudeKaleSom', ks_, r['extraVelden']['claudeKaleSom'])
        # V-#902 (E05 bank-004) en Z-#902: '1 stappen' → '1 stap'; bij een stip rechts van 0 begint de uitleg met de kant van de vraag
        if r['merge'].get('doel') == 'G8-MEET-E05' and isinstance(r['extraVelden'].get('claudeUitleg'), str):
            o = r['extraVelden']['claudeUitleg']; u_ = re.sub(r'(?<![\d,.])1 stappen\b', '1 stap', o)
            if u_.startswith('Links van 0 staan de getallen onder nul.') and 'naar rechts' in u_ and 'naar links' not in u_:
                u_ = u_.replace('Links van 0 staan de getallen onder nul.', 'Rechts van 0 staan de getallen boven nul.', 1)
            if u_ != o: r['extraVelden']['claudeUitleg'] = u_; slog(r, "V-#902/Z-#902: '1 stap'; rechts van 0 = boven nul", 'claudeUitleg', o, u_)
        # Z-#905 (Didactiek batch 5, les 316): geloofwaardige vlucht bij het tijdsverschil. 023: 4 uur vliegen met 8 uur verschil → 9 uur vliegen, 3 uur later (antwoord blijft 1.45 uur);
        # 015: 5 uur en 30 minuten met 6 uur verschil → 3 uur later (19.30 uur). Claudes sleutels gaan mee (tijd thuis, verkeerde kant op).
        Z905 = {'ff798e6c': [(r'duurt 4 uur\.', 'duurt 9 uur.'), (r'\b8 uur later', '3 uur later'), (r'\+ 8\b', '+ 3'), (r'\+ 4([:.])00', r'+ 9\g<1>00'),
                             (r'(?<![\d.:])17([:.])45', r'22\g<1>45'), (r'(?<![\d.:])9([:.])45', r'19\g<1>45')],
                '78096f07': [(r'\b6 uur later', '3 uur later'), (r'\+ 6\b', '+ 3'), (r'(?<![\d.:])22([:.])30', r'19\g<1>30'), (r'(?<![\d.:])10([:.])30', r'13\g<1>30')]}
        if c8 in Z905 and r['opgave'].startswith('Een vliegtuig vertrekt'):
            def _z905(v):
                if isinstance(v, str):
                    for a9, b9 in Z905[c8]: v = re.sub(a9, b9, v)
                    return v
                if isinstance(v, list): return [_z905(x) for x in v]
                if isinstance(v, dict): return {k: _z905(x) for k, x in v.items()}
                return v
            o = r['opgave']
            for k_ in ('opgave', 'antwoord', 'geldigeAntwoorden', 'antwoordDetail'):
                if r.get(k_) is not None: r[k_] = _z905(r[k_])
            for k_ in [k for k in r['extraVelden'] if k.startswith('claude')]: r['extraVelden'][k_] = _z905(r['extraVelden'][k_])
            assert re.search(r'(1[:.]45|19[:.]30)', str(r['antwoord'])), ('Z-#905', c8, r['antwoord'])
            slog(r, 'Z-#905: geloofwaardige vluchtduur bij het tijdsverschil', 'opgave', o, r['opgave'])
        # ---------- G8 batch 6 (Oefeningen 16:50 + Didactiek review-batch6 16:54) ----------
        # Oef-#498: MEET-E07 Claude-sleutels met een punt als komma ('147.5') → '147,5'; dubbel daarna → weg
        if r['merge'].get('doel') == 'G8-MEET-E07':
            ex = r['extraVelden']
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                if not ex.get(k_): continue
                L_ = []; gezien = set(); voor = [d_.get('fout') for d_ in ex[k_]]
                for d_ in ex[k_]:
                    f_ = str(d_.get('fout'))
                    if re.fullmatch(r'\d+\.\d{1,2}', f_): d_ = dict(d_, fout=f_.replace('.', ','))
                    if d_.get('fout') in gezien: continue
                    gezien.add(d_.get('fout')); L_.append(d_)
                if [d_.get('fout') for d_ in L_] != voor: ex[k_] = L_; slog(r, "Oef-#498: Claude-sleutel met punt als komma → komma ('147.5' → '147,5')", k_, str(voor), str([d_.get('fout') for d_ in L_]))
        # Oef-#499 (zoals G7 Oef-#448): VBN-E03 spaarsommen, het antwoord met € zoals de sleutels ('158' → '€158')
        if r['merge'].get('doel') == 'G8-VBN-E03' and re.fullmatch(r'\d+', str(r['antwoord'])) and '€' in r['opgave']:
            oud = r['antwoord']; r['antwoord'] = f'€{oud}'
            if isinstance(r.get('antwoordDetail'), dict) and 'accept' in r['antwoordDetail']: r['antwoordDetail']['accept'] = [r['antwoord']]
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [r['antwoord'] if g_ == oud else g_ for g_ in r['geldigeAntwoorden']]
            r['merge']['oef499'] = {'antwoord': oud, 'reden': 'Oef-#499: antwoord met € zoals de sleutels (G7 Oef-#448)'}
            slog(r, 'Oef-#499: antwoord met € (zoals G7 #448)', 'antwoord', oud, r['antwoord'])
        # V-#891 (Didactiek batch 6, twijfel 3; Oef-#1000, les 306): MEET-V01 #2 vol bouwwerk waarin 'drie kanten' (d·b + b·h + d·h) het antwoord gaf → maten van
        # Didactiek (diep × hoog × breed). Het antwoord blijft op zijn plek; elke afleider volgt dezelfde route als ervoor (nagerekend in tools/bouwsel_routes).
        V891 = {'06886f5b': ((3, 4, 3), {'11': '10', '42': '45'}), '0e749130': ((4, 3, 3), {'11': '10', '26': '24'}), '291b2b8b': ((3, 3, 4), {'11': '10', '12': '12'}),
                '9ae14b9d': ((3, 4, 3), {'42': '45', '26': '24'}), 'dd2aa399': ((3, 4, 3), {'24': '27', '26': '24'}), 'f57656e1': ((3, 3, 4), {'11': '10', '26': '24'}),
                '3e70fde2': ((3, 2, 5), {'10': '10', '23': '22'}), '970b9a33': ((2, 3, 5), {'23': '22', '10': '10'}), 'a20c582f': ((3, 5, 2), {'24': '24', '40': '36'}),
                '63bc1070': ((2, 7, 2), {'18': '24', '19': '22'})}
        if c8 in V891 and (r['visual'].get('jsRender') or {}).get('soort') == 'bouwsel':
            (d_, h_, b_), om = V891[c8]; jr = r['visual']['jsRender']; od, oh, ob = jr['diep'], jr['hoog'], jr['breed']
            R_oud, R_nw = BR.routes(od, oh, ob), BR.routes(d_, h_, b_); a_oud, a_ = str(r['antwoord']), str(d_ * h_ * b_)
            for vo, vn in om.items():      # dezelfde route: de oude afleider is een route op de oude maten, de nieuwe dezelfde route op de nieuwe
                assert any(str(R_oud[k]) == vo and str(R_nw[k]) == vn for k in R_oud), ('V-#891 route', c8, vo, vn)
            assert not BR.fouten(d_, h_, b_) and set(om) | {a_oud} == {o_['tekst'] for o_ in r['opties']}, ('V-#891', c8)
            jr.update(diep=d_, hoog=h_, breed=b_)
            om = dict(om, **{a_oud: a_})
            for o_ in r['opties']: o_['tekst'] = om[o_['tekst']]
            r['antwoord'] = a_; r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            if isinstance(r.get('antwoordDetail'), dict): r['antwoordDetail']['juisteOptieTekst'] = a_; r['antwoordDetail']['juisteOptie'] = next(o_['letter'] for o_ in r['opties'] if o_['tekst'] == a_)
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [a_]
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                if r['extraVelden'].get(k_): r['extraVelden'][k_] = [dict(x_, fout=om.get(str(x_.get('fout')), x_.get('fout'))) for x_ in r['extraVelden'][k_]]
            assert len({o_['tekst'] for o_ in r['opties']}) == 3 and a_ in {o_['tekst'] for o_ in r['opties']}
            slog(r, f"V-#891: bouwwerk {od}×{oh}×{ob} → {d_}×{h_}×{b_} (drie kanten gaf het antwoord); antwoord {a_oud} → {a_}, afleiders zelfde route", 'jsRender', f'{od}×{oh}×{ob}', f'{d_}×{h_}×{b_}')
        # V-#892 / Z-#897 (Didactiek batch 6): VBN-E03 zinloze spaardoelen → een step (€92), een skateboard (€104), voetbalschoenen (€113)
        D892 = {'074d14f9': ('Je spaart voor stappen.', 'Je spaart voor een step.'), '3acd96dc': ('Je spaart voor sterren.', 'Je spaart voor een skateboard.'),
                'c68ab442': ('Je spaart voor ballen.', 'Je spaart voor voetbalschoenen.')}
        if c8 in D892 and r['opgave'].startswith(D892[c8][0]):
            o = r['opgave']; r['opgave'] = o.replace(*D892[c8], 1); slog(r, 'V-#892/Z-#897: logisch spaardoel', 'opgave', o, r['opgave'])
        # Z-#893 (Didactiek batch 6, les 316): MEET-E07 007 het kind gaat niet zelf 80 km per uur
        if c8 == 'c74c6871' and r['opgave'].startswith('Een kind reist 2,5 uur met 80 km per uur.'):
            o = r['opgave']; r['opgave'] = o.replace('Een kind reist 2,5 uur met 80 km per uur.', 'Een kind reist 2,5 uur met de trein. De trein rijdt 80 km per uur.', 1)
            slog(r, 'Z-#893: de trein rijdt 80 km per uur, niet het kind', 'opgave', o, r['opgave'])
        # V-#893 (Didactiek batch 6, twijfel 5; Oef-#1002): VBN-E04 de beslissende staaf niet op een half streepje (som blijft 100); claudeUitleg mee
        V893 = {'5c275a7f': ({'fiets': 60, 'lopend': 20, 'auto': 5, 'bus': 15}, [('Fiets is 55%', 'Fiets is 60%')]),
                'b8a10f32': ({'fiets': 20, 'lopend': 10, 'auto': 10, 'bus': 60}, [('Bus is 55%', 'Bus is 60%')]),
                'b8408150': ({'hond': 60, 'kat': 20, 'konijn': 20, 'vis': 0}, [('Hond is 55%', 'Hond is 60%')]),
                '6d7f8d4f': ({'water': 30, 'melk': 30, 'sap': 10, 'niets': 30}, [('25% + 30% = 55%', '30% + 30% = 60%')]),
                }
        if B7VLAG.ACTIEF:      # V-#945 (Didactiek b7, vervangt Oef-#1003; les 326/352): #30 029 hond 25 + kat 15 (aflezing 30/40/50) → hond 30 + kat 10 = 40, één streepje onder 50; 'Nee' blijft
            V893['346c5527'] = ({'hond': 30, 'kat': 10, 'konijn': 15, 'vis': 45}, [('25% + 15% = 40%', '30% + 10% = 40%')])
        if c8 in V893 and (r['visual'].get('jsRender') or {}).get('soort') == 'staafdiagram':
            nw, uit = V893[c8]; st_ = r['visual']['jsRender']['staven']; voor = {x_['naam']: x_['waarde'] for x_ in st_}
            assert set(voor) == set(nw) and sum(nw.values()) == 100, ('V-#893', c8, voor)
            for x_ in st_: x_['waarde'] = nw[x_['naam']]
            ex = r['extraVelden']
            for a8, b8 in uit:
                if isinstance(ex.get('claudeUitleg'), str): ex['claudeUitleg'] = ex['claudeUitleg'].replace(a8, b8)
            slog(r, 'V-#893: beslissende staaf op een heel streepje', 'jsRender', str(voor), str(nw))
        # V-#894 (Didactiek batch 6): '"N kinderen kozen X." Klopt dat?' → N past bij een heel totaal (het percentage blijft); 'Dat kun je hier niet zien' blijft
        V894 = {'58a665be': ('"12 kinderen kozen vis."', '"9 kinderen kozen vis."'), '9c184aad': ('"15 kinderen kozen hond."', '"9 kinderen kozen hond."'),
                '86455544': ('"15 kinderen kozen tekenen."', '"7 kinderen kozen tekenen."'), 'b87af28e': ('"15 kinderen kozen rekenen."', '"11 kinderen kozen rekenen."'),
                'dcef0009': ('"12 kinderen kozen niets."', '"14 kinderen kozen niets."')}
        if c8 in V894 and V894[c8][0] in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace(*V894[c8], 1); slog(r, 'V-#894: het aantal past bij een heel totaal', 'opgave', o, r['opgave'])
        # Oef-#1004 (b7, VBN-E04 #21 016): één hondje voor 6 honden i.p.v. 4, zodat het aantal plaatjes (4) en de waarde van een plaatje niet gelijk zijn.
        # 3 hele + 1 half = 3 × 6 + 3 = 21; afleiders 24 (half als heel) en 4 (plaatjes geteld). De kop (nieuwe template) zet kop_1004 na Oef-#1001.
        if B7VLAG.ACTIEF and c8 == 'dbb037fa' and 'één hondje voor 4 honden' in r['opgave']:      # ook Z-#943 (Didactiek b7)
            o = r['opgave']; r['opgave'] = o.replace('één hondje voor 4 honden', 'één hondje voor 6 honden', 1)
            W1004 = {'14 honden': '21 honden', '16 honden': '24 honden'}
            for o_ in r['opties']: o_['tekst'] = W1004.get(o_['tekst'], o_['tekst'])
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoord'] = W1004.get(r['antwoord'], r['antwoord'])
            ad = r.get('antwoordDetail') or {}
            if ad.get('juisteOptieTekst') in W1004: ad['juisteOptieTekst'] = W1004[ad['juisteOptieTekst']]
            ex = r['extraVelden']
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in ex.get(k_) or []: d_['fout'] = W1004.get(d_.get('fout'), d_.get('fout'))
            ex['claudeUitleg'] = 'Drie hele hondjes zijn 3 keer 6, dus 18 honden. Een half hondje is de helft van 6, dus 3 honden. Samen zijn dat 21 honden.'
            assert r['antwoord'] == '21 honden' and sorted(o_['tekst'] for o_ in r['opties']) == ['21 honden', '24 honden', '4 honden'], ('Oef-#1004', r['opties'])
            slog(r, 'Oef-#1004: één hondje voor 6 honden (aantal plaatjes ≠ waarde van een plaatje); 21, afleiders 24/4', 'opgave', o, r['opgave'])
        # V-#944 (Didactiek b7, les 316/320): #24 019 klas B 40% van 30 kinderen (niet 40): A = 10, B = 12; 'percentages vergeleken' blijft A, 'evenveel' fout
        if B7VLAG.ACTIEF and c8 == 'ce8e8841' and 'kiest 40% van de 40 kinderen' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('kiest 40% van de 40 kinderen', 'kiest 40% van de 30 kinderen', 1)
            W944 = {'Klas B, want dat zijn 16 kinderen.': 'Klas B, want dat zijn 12 kinderen.'}
            for o_ in r['opties']: o_['tekst'] = W944.get(o_['tekst'], o_['tekst'])
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoord'] = W944.get(r['antwoord'], r['antwoord'])
            if (ad := r.get('antwoordDetail') or {}).get('juisteOptieTekst') in W944: ad['juisteOptieTekst'] = W944[ad['juisteOptieTekst']]
            ex = r['extraVelden']
            if isinstance(ex.get('claudeUitleg'), str): ex['claudeUitleg'] = ex['claudeUitleg'].replace('40% van 40 is 16 kinderen', '40% van 30 is 12 kinderen')
            assert r['antwoord'] == 'Klas B, want dat zijn 12 kinderen.' and '12 kinderen' in ex['claudeUitleg'], ('V-#944', r['antwoord'])
            slog(r, 'V-#944: klas B 40% van 30 kinderen (redelijke klas); antwoord 12 kinderen', 'opgave', o, r['opgave'])
        # V-#946 (Didactiek b7): #7 002 '(x 1000)' → '(× 1000)' (kop volgt in de kop-pass)
        if B7VLAG.ACTIEF and c8 == '1df867a7' and '(x 1000)' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('(x 1000)', '(× 1000)'); slog(r, "V-#946: keerteken '×'", 'opgave', o, r['opgave'])
        # Z-#945 (Didactiek b7, data-taal): #9 kop tussen aanhalingstekens; #16 zonder 'juist' (verraadt de verrassing); #19/#22 'lijkt voor/bij … te staan/horen'
        Z945 = {'d7a5da92': [('opgave', 'staat: Het aantal bezoekers is verdubbeld. De staaf', 'staat: "Het aantal bezoekers is verdubbeld." De staaf')],
                '710da02d': [('optie', 'Het aantal wordt juist groter.', 'Het aantal wordt groter.')],
                'd921591b': [('optie', 'Het grote plaatje lijkt veel meer stuks.', 'Het grote plaatje lijkt voor veel meer stuks te staan.')],
                'eb4ee883': [('optie', 'De brede staaf lijkt een groter aantal.', 'De brede staaf lijkt bij een groter aantal te horen.')]}
        if B7VLAG.ACTIEF and c8 in Z945:
            for veld_, a9, b9 in Z945[c8]:
                if veld_ == 'opgave' and a9 in r['opgave']:
                    o = r['opgave']; r['opgave'] = o.replace(a9, b9, 1); slog(r, 'Z-#945: data-taal b7', 'opgave', o, r['opgave'])
                elif veld_ == 'optie' and any(o_['tekst'] == a9 for o_ in r['opties']):
                    for o_ in r['opties']:
                        if o_['tekst'] == a9: o_['tekst'] = b9
                    r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                    if r['antwoord'] == a9: r['antwoord'] = b9
                    if (ad := r.get('antwoordDetail') or {}).get('juisteOptieTekst') == a9: ad['juisteOptieTekst'] = b9
                    for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                        for d_ in r['extraVelden'].get(k_) or []:
                            if d_.get('fout') == a9: d_['fout'] = b9
                    slog(r, 'Z-#945: data-taal b7', 'opties', a9, b9)
        # Z-#765 (Didactiek b1; filter tools/eindcijfer_check.py, nieuwe factoren uit EC.zoek): E02 #1 «Op welk cijfer eindigt a × b?» — het eindcijfer is niet
        # het begincijfer of het tientallencijfer van het product en niet (u1 + u2) mod 10. Zelfde eenheden waar het kan (antwoord en eenheid-routes gelijk);
        # 064 kan dat niet (2 + 2 = 4 = 2 × 2): 112 × 14 = 1568 → 8. Claudes sleutel 'getal-overgenomen' volgt het cijfer op dezelfde plek; een sleutel = antwoord valt weg.
        Z765 = {'0521e250': ((19, 17), (29, 17)), '134ef787': ((112, 12), (112, 14)), '1a909be3': ((19, 7), (29, 7)), '2aa05195': ((42, 6), (32, 6)),
                '52efae1d': ((43, 8), (33, 8)), '6478ec2b': ((15, 17), (15, 27)), '906b269a': ((49, 7), (39, 7)), '95c4251c': ((16, 9), (26, 9)),
                '962eb1b9': ((119, 27), (109, 27)), 'a2e9ba40': ((59, 3), (69, 3)), 'eb64ee33': ((147, 35), (137, 35))}
        Z975 = {'061aa7b2': ((14, 16), (14, 17)), '2aa05195': ((32, 6), (27, 6)), '5f936e21': ((161, 27), (159, 27)), '61eadfa8': ((203, 31), (203, 29)),
                '73f927aa': ((14, 6), (17, 6)), 'a08ac8d5': ((126, 32), (126, 27)), 'ceb54cf1': ((44, 6), (43, 6)), 'ecb0c2b6': ((21, 3), (18, 3)), 'ecda39ad': ((51, 7), (59, 7))}
        if c8 in Z765 and EC.lees(r) == Z765[c8][0]:
            (a0, b0), (a1, b1) = Z765[c8]; o = r['opgave']; r['opgave'] = f'Op welk cijfer eindigt {a1} × {b1}?'; ant = str(a1 * b1 % 10); r['antwoord'] = ant
            if isinstance(r.get('antwoordDetail'), dict):
                for k_, v_ in list(r['antwoordDetail'].items()):
                    if isinstance(v_, str) and v_ == str(a0 * b0 % 10): r['antwoordDetail'][k_] = ant
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [ant]
            ex = r['extraVelden']
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                L2 = []; gezien = set()
                for i_, d_ in enumerate(ex.get(k_) or []):
                    lab = d_.get('denkfout') or ((ex.get('claudeDenkfouten') or [])[i_].get('denkfout') if i_ < len(ex.get('claudeDenkfouten') or []) else None)
                    v_ = d_.get('fout')
                    if lab == 'getal-overgenomen' and v_:      # het cijfer op dezelfde plek in de nieuwe factoren (eerst a, dan b; van links)
                        for x0, x1 in ((str(a0), str(a1)), (str(b0), str(b1))):
                            if v_ in x0 and len(x0) == len(x1): v_ = x1[x0.index(v_)]; break
                    if v_ == ant or v_ in gezien: continue
                    gezien.add(v_); L2.append(dict(d_, fout=v_))
                if ex.get(k_) is not None: ex[k_] = L2
            if isinstance(ex.get('claudeKaleSom'), str) and EC.RX.match(ex['claudeKaleSom'].strip()): ex['claudeKaleSom'] = r['opgave']      # V-#975: kale som = de nieuwe opgave
            assert not EC.fouten(a1, b1) or c8 in Z975, ('Z-#765', c8)
            slog(r, f'Z-#765: geen foute route op het eindcijfer ({a0} × {b0} → {a1} × {b1}, antwoord {ant})', 'opgave', o, r['opgave'])
        # Z-#975 (Didactiek b8 deel A, les 306): het antwoord is niet het eenheidscijfer van een factor (behalve 5 × oneven); filter in EC.fouten.
        # 9 items (062, 070, 082, 083, 086, 097, 102, 109, 110), nieuwe factoren met evenveel cijfers, geen eenheid 0/1/5, antwoorden 2–8 (spreiding 7–8 per cijfer).
        # Claudes sleutels volgen hun label: plaatswaarde-verkeerd = de eenheid van dezelfde factor, optellen = (u1 + u2) mod 10, een-ernaast = antwoord ± 1,
        # getal-overgenomen = het cijfer op dezelfde plek. Een sleutel = antwoord valt weg. V-#975: de kale som gaat mee.
        if c8 in Z975 and EC.lees(r) == Z975[c8][0]:
            (a0, b0), (a1, b1) = Z975[c8]; o = r['opgave']; ant0 = str(a0 * b0 % 10); ant = str(a1 * b1 % 10)
            r['opgave'] = f'Op welk cijfer eindigt {a1} × {b1}?'; r['antwoord'] = ant
            if isinstance(r.get('antwoordDetail'), dict):
                for k_, v_ in list(r['antwoordDetail'].items()):
                    if isinstance(v_, str) and v_ == ant0: r['antwoordDetail'][k_] = ant
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [ant]
            ex = r['extraVelden']
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                L2 = []; gezien = set()
                for i_, d_ in enumerate(ex.get(k_) or []):
                    lab = d_.get('denkfout') or ((ex.get('claudeDenkfouten') or [])[i_].get('denkfout') if i_ < len(ex.get('claudeDenkfouten') or []) else None)
                    v_ = str(d_.get('fout'))
                    # dezelfde route als bij de oude factoren (de route bepaalt de sleutel, niet het label): eerst de route die het label noemt
                    R975 = [('optellen', lambda a, b: (a % 10 + b % 10) % 10), ('begincijfer', lambda a, b: int(str(a * b)[0])),
                            ('tientallen', lambda a, b: int(str(a * b)[-2]) if a * b >= 10 else None),
                            ('eenheid a', lambda a, b: a % 10), ('eenheid b', lambda a, b: b % 10),
                            ('a − 1', lambda a, b: (a - 1) * b % 10), ('a + 1', lambda a, b: (a + 1) * b % 10), ('b − 1', lambda a, b: a * (b - 1) % 10), ('b + 1', lambda a, b: a * (b + 1) % 10)]
                    voorkeur = {'optellen-ipv-vermenigvuldigen': ['optellen'], 'plaatswaarde-verkeerd': ['eenheid a', 'eenheid b'], 'getal-overgenomen': ['begincijfer', 'tientallen', 'eenheid a', 'eenheid b'],
                                'een-ernaast': ['a − 1', 'a + 1', 'b − 1', 'b + 1']}.get(lab, [])
                    volg = sorted(R975, key=lambda t: (t[0] not in voorkeur, voorkeur.index(t[0]) if t[0] in voorkeur else 0))
                    for n_, f_ in volg:
                        if v_.isdigit() and f_(a0, b0) is not None and str(f_(a0, b0)) == v_ and f_(a1, b1) is not None: v_ = str(f_(a1, b1)); break
                    else:
                        for x0, x1 in ((str(a0), str(a1)), (str(b0), str(b1))):
                            if v_ in x0 and len(x0) == len(x1): v_ = x1[x0.index(v_)]; break
                    if v_ == ant or v_ in gezien: continue
                    gezien.add(v_); L2.append(dict(d_, fout=v_))
                if ex.get(k_) is not None: ex[k_] = L2
            if isinstance(ex.get('claudeKaleSom'), str) and EC.RX.match(ex['claudeKaleSom'].strip()): ex['claudeKaleSom'] = r['opgave']
            assert not EC.fouten(a1, b1), ('Z-#975', c8, EC.fouten(a1, b1))
            slog(r, f'Z-#975: antwoord niet het eenheidscijfer van een factor ({a0} × {b0} → {a1} × {b1}, antwoord {ant})', 'opgave', o, r['opgave'])
        # Z-#766 rest (Didactiek b1): E03 #2 026/030 «Reken uit. a : b + c» — a − b (026: 12 − 3 = 9) en a − c (030: 16 − 4 = 12) gaven het antwoord.
        # Nieuw: 026 15 : 3 + 6 = 11 (a − b 12, a − c 9, b + c 9, a + c 21, a + b 18, a : b 5); 030 18 : 2 + 5 = 14 (a − b 16, a − c 13, a + c 23, b + c 7, a : b 9).
        # Claudes sleutel 'eerst optellen/niet delen' = a + c gaat mee (17 → 21, 20 → 23).
        # Z-#976 (Didactiek b8 deel A, les 335): 026 gaf antwoord 11 (4 van de 12 items) → 20 : 4 + 7 = 12 (routes 16, 13, 11, 27, 24, 5 vrij; 20 : 11 niet heel); sleutel a + c = 27
        Z766 = {'69623976': ('Reken uit. 12 : 3 + 5', 'Reken uit. 20 : 4 + 7', '9', '12', {'17': '27'}, 'Eerst delen: 20 : 4 = 5. Dan 5 + 7 = 12.'),
                'adc711dd': ('Reken uit. 16 : 2 + 4', 'Reken uit. 18 : 2 + 5', '12', '14', {'20': '23'}, 'Eerst delen: 18 : 2 = 9. Dan 9 + 5 = 14.')}
        if c8 in Z766 and r['opgave'] == Z766[c8][0]:
            o0, o1, a0_, a1_, km, ui = Z766[c8]; r['opgave'] = o1; r['antwoord'] = a1_
            if isinstance(r.get('antwoordDetail'), dict):
                for k_, v_ in list(r['antwoordDetail'].items()):
                    if v_ == a0_: r['antwoordDetail'][k_] = a1_
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [a1_]
            ex = r['extraVelden']; ex['claudeUitleg'] = ui
            if isinstance(ex.get('claudeKaleSom'), str) and ex['claudeKaleSom'].strip(): ex['claudeKaleSom'] = o1.replace('Reken uit. ', '') + f' = {a1_}'
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in ex.get(k_) or []: d_['fout'] = km.get(d_.get('fout'), d_.get('fout'))
            slog(r, 'Z-#766/Z-#976: E03 #2 geen route (a − b, a − c) op het antwoord' + ('; antwoord 12 (spreiding)' if c8 == '69623976' else ''), 'opgave', o0, o1)
        # Z-#1042 (Didactiek hercheck b9 19:16:15, zacht; les 402): dubbele items na het samenvoegen van de koppen → per groep andere getallen, routes nagerekend (assert).
        # E04 #1 012/013/018 (25% korting, €60): 013 → €36 (48), 018 → €48 (64). Routes: de nieuwe prijs, procent van de nieuwe prijs erbij (na × 125/100) ≠ het antwoord.
        if r['merge'].get('doel') == 'G8-VERH-E04' and c8 in Z1042_E04:
            mz_ = re.search(r'kost na (\d+)% korting €(\d+)\.', r['opgave'])
            if mz_ and int(mz_.group(2)) != Z1042_E04[c8]:
                p_, y0_, y_ = int(mz_.group(1)), int(mz_.group(2)), Z1042_E04[c8]; a_ = Fr(y_ * 100, 100 - p_); pv_ = Fr(y_ * (100 + p_), 100)
                assert a_.denominator == 1 and pv_.denominator == 1 and len({int(a_), int(pv_), y_}) == 3, (c8, a_, pv_)
                a0_ = str(r['antwoord']); a_ = str(int(a_)); o0_ = r['opgave']
                r['opgave'] = o0_[:mz_.start()] + f'kost na {p_}% korting €{y_}.' + o0_[mz_.end():]; r['antwoord'] = a_
                if isinstance(r.get('antwoordDetail'), dict):
                    for k_, v_ in list(r['antwoordDetail'].items()):
                        if str(v_) == a0_: r['antwoordDetail'][k_] = a_
                ex = r['extraVelden']; lab_ = {d_.get('fout'): d_.get('denkfout') for d_ in ex.get('claudeDenkfouten') or []}
                for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                    for d_ in ex.get(k_) or []:
                        if (d_.get('denkfout') or lab_.get(d_.get('fout'))) == 'getal-overgenomen': d_['fout'] = str(y_)
                        if k_ == 'claudeFoutHints': d_['uitleg'] = (d_.get('uitleg') or '').replace(f'€{y0_}', f'€{y_}')
                assert sum(1 for d_ in ex.get('claudeDenkfouten') or [] if d_.get('denkfout') == 'getal-overgenomen' and d_['fout'] == str(y_)) == 1, (c8, 'Z-#1042: sleutel nieuwe prijs')
                ex['claudeKaleSom'] = f'na {p_}% korting €{y_}, was?'
                ex['claudeUitleg'] = f'€{y_} is {100 - p_}% van de oude prijs.\n1% is {y_} : {100 - p_} = ' + f'{y_ / (100 - p_):.2f}'.replace('.', ',') + f', dus 100% is €{a_}.'
                slog(r, 'Z-#1042: dubbel item (E04 #1) → andere getallen', 'opgave', o0_, r['opgave'])
        # Oef-#1006/#1007/#1009 (b8, VERH-E04 #1–#7): Claudes sleutels zonder '€' (zoals het antwoord; geldigeAntwoorden met en zonder '€'),
        # 'procent-verkeerde-basis' exact (na × (100 + p) / 100: 57,60 i.p.v. €58), en geloofwaardige prijzen bij #1 (les 147).
        if r['merge'].get('doel') == 'G8-VERH-E04' and re.fullmatch(r'\d+(?:,\d+)?', str(r['antwoord'])) and re.search(r'kost na \d+% korting €\d+\. Wat was de prijs vóór de korting\?|zet €\d+ op een spaarrekening met \d+% rente per jaar\.', r['opgave']):      # #1–#7 (somtypeNrOrigineel staat hier nog niet)
            ex = r['extraVelden']; mk_ = re.search(r'kost na (\d+)% korting €(\d+)\.', r['opgave'])
            def _eu(v):
                v = round(v, 2); return str(int(v)) if v == int(v) else f'{v:.2f}'.replace('.', ',')
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for i_, d_ in enumerate(ex.get(k_) or []):
                    v_ = d_.get('fout'); lab = d_.get('denkfout') or ((ex.get('claudeDenkfouten') or [])[i_].get('denkfout') if i_ < len(ex.get('claudeDenkfouten') or []) else None)
                    if isinstance(v_, str) and v_.startswith('€'): v_ = v_[1:].strip()
                    if mk_ and lab == 'procent-verkeerde-basis': v_ = _eu(int(mk_.group(2)) * (100 + int(mk_.group(1))) / 100)
                    if v_ != d_.get('fout'): slog(r, "Oef-#1006/#1007: Claude-sleutel zonder '€' en exact", 'claudeSleutel', d_.get('fout'), v_)
                    d_['fout'] = v_
            a_ = str(r['antwoord']); ga_ = [a_, f'€{a_}', f'€ {a_}', f'{a_} euro'] + ([f'€{a_},00', f'{a_},00'] if re.fullmatch(r'\d+', a_) else [])      # Z-#982 (G5 #300): ook '€60,00' en '60,00'
            for d_ in list(ex.get('claudeDenkfouten') or []):      # Z-#982: '57,60' ook als '57,6'
                v_ = str(d_.get('fout'))
                if re.fullmatch(r'\d+,\d0', v_) and not any(x_.get('fout') == v_[:-1] for x_ in ex['claudeDenkfouten']):
                    ex['claudeDenkfouten'].append(dict(d_, fout=v_[:-1])); slog(r, "Z-#982: sleutel ook zonder nul achteraan", 'claudeSleutel', v_, v_[:-1])
            if r.get('geldigeAntwoorden') != ga_: r['geldigeAntwoorden'] = ga_
            P1009 = {'03d597d7': ('ei', 'fietshelm'), '566b2d98': ('wortel', 'skateboard'), '844212d8': ('knikker', 'koptelefoon'), '8c16deab': ('pion', 'fiets'),
                     '930b3b0d': ('sticker', 'bordspel'), 'e07869da': ('sticker', 'tent'), '95ee6319': ('bot', 'telefoon'), '3025592c': ('vis', 'aquarium'),
                     '5b3d9b42': ('schrift', 'rugzak'), 'd19d8dde': ('bot', 'hondenmand')}      # 013 schrift €80 en 018 bot €80 ook (zelfde les 147)
            if c8 in P1009 and r['opgave'].startswith(f'Een {P1009[c8][0]} kost'):
                o = r['opgave']; r['opgave'] = o.replace(f'Een {P1009[c8][0]} kost', f'Een {P1009[c8][1]} kost', 1); slog(r, 'Oef-#1009: geloofwaardige prijs (ander ding)', 'opgave', o, r['opgave'])
        # Oef-#1010 (b8, les 306): VERH-E04 #8 032: 150 − 60 = 90 (geheel min het procent) gaf het antwoord; '100 kinderen' had geen route.
        # Nieuw: 200 kinderen, 30 procent → 60. Routes: procent als aantal 30, geheel min het procent 170, een tiende 20, de rest (70%) 140 — alle ≠ 60.
        # Afleiders: '30 kinderen' (procent als aantal, Claude 'getal-overgenomen') en '170 kinderen' (geheel min het procent).
        if c8 == '86d4eb05' and r['opgave'].startswith('Van de 150 kinderen op school komt 60 procent'):
            o = r['opgave']; r['opgave'] = 'Van de 200 kinderen op school komt 30 procent met de fiets. Hoeveel kinderen komen er met de fiets?'
            W10 = {'90 kinderen': '60 kinderen', '60 kinderen': '30 kinderen', '100 kinderen': '170 kinderen'}
            for o_ in r['opties']: o_['tekst'] = W10.get(o_['tekst'], o_['tekst'])
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoord'] = '60 kinderen'
            if isinstance(r.get('antwoordDetail'), dict) and r['antwoordDetail'].get('juisteOptieTekst') in W10: r['antwoordDetail']['juisteOptieTekst'] = W10[r['antwoordDetail']['juisteOptieTekst']]
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = ['60 kinderen']
            ex = r['extraVelden']; ex['claudeUitleg'] = '10 procent van 200 is 20 kinderen. 30 procent is dan 3 × 20 = 60. Dus 60 kinderen komen met de fiets.'
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in ex.get(k_) or []: d_['fout'] = W10.get(d_.get('fout'), d_.get('fout'))
            assert sorted(o_['tekst'] for o_ in r['opties']) == ['170 kinderen', '30 kinderen', '60 kinderen'], r['opties']
            slog(r, 'Oef-#1010: geen foute route op het antwoord; elke afleider een route (200, 30% → 60; 30 / 170)', 'opgave', o, r['opgave'])
        # ---- b8 ronde 2 (Didactiek review-batch8a/8b, 8 okt 17:53/17:55; data letterlijk uit de rapporten) ----
        ex = r['extraVelden']
        def _sleutels(km, fh=None):
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in ex.get(k_) or []: d_['fout'] = km.get(d_.get('fout'), d_.get('fout'))
            for f_ in ex.get('claudeFoutHints') or []:
                if fh and f_.get('fout') in fh: f_['uitleg'] = fh[f_['fout']]
        # V-#970 (les 365): E03 #8 218 en #11 229 geen 1 : 100.000 bij een km-vraag ('getal overnemen' gaf goed); 229 ook niet 'de klas … van de school'
        V970 = {'5b63f67f': ('Op een kaart met schaal 1 : 100.000 is het moeras 9 cm van het museum.', 'Op een kaart met schaal 1 : 200.000 is het meer 9 cm van de stad.', 9, 18),
                '8dfe4ef4': ('Op een kaart met schaal 1 : 100.000 is de klas 9 cm van de school.', 'Op een kaart met schaal 1 : 200.000 is het pretpark 4 cm van de school.', 4, 8)}
        if c8 in V970 and r['opgave'].startswith(V970[c8][0]):
            v0, v1, cm, km = V970[c8]; o = r['opgave']; r['opgave'] = o.replace(v0, v1, 1); a0_ = str(r['antwoord']); r['antwoord'] = str(km)
            ex['claudeUitleg'] = f'1 cm op de kaart is 200.000 cm = 2000 m = 2 km in het echt.\n{cm} × 2 = {km} km.'
            ex['claudeKaleSom'] = f'{cm} cm bij 1 : 200.000 → km'
            _sleutels({f'{a0_}000': f'{km * 1000:,}'.replace(',', '.') if km * 1000 >= 10000 else str(km * 1000), f'{a0_}0': str(km * 10)},
                      {str(km * 10): 'Een nul te veel. 1 cm is hier 2 km.'})
            assert str(cm) != r['antwoord'] and r['antwoord'] == str(cm * 2), ('V-#970', c8)
            slog(r, 'V-#970: schaal 1 : 200.000 (getal overnemen geeft niet meer het antwoord)', 'opgave', o, r['opgave'])
        # V-#972 (les 147/316/366): E03 #7 plekparen die bij een kaart en bij de afstand passen; getallen blijven
        P972 = {'het stadion naar de kleedkamer 8 cm': 'het station naar het stadion 8 cm', 'het museum naar het moeras 5 cm': 'de camping naar het strand 5 cm',
                'de vallei naar het nest 8 cm': 'het dorp naar de stad 8 cm', 'het stadion naar het veld 7 cm': 'de boerderij naar het meer 7 cm',
                'de schuur naar de dierentuin 9 cm': 'de school naar het zwembad 9 cm', 'de schuur naar de dierentuin 6 cm': 'de haven naar de vuurtoren 6 cm',
                'de schuur naar de dierentuin 2 cm': 'de bakker naar de bibliotheek 2 cm', 'de kantine naar de kleedkamer 3 cm': 'de kerk naar het plein 3 cm'}
        if r['merge'].get('doel', '').endswith('VERH-E03') or r['opgave'].startswith('Op een kaart met schaal'):
            for p0, p1 in P972.items():
                if f'is de afstand van {p0}. Hoeveel meter' in r['opgave']:
                    o = r['opgave']; r['opgave'] = o.replace(p0, p1, 1); slog(r, 'V-#972: plekpaar past bij een kaart en bij de afstand', 'opgave', o, r['opgave']); break
            # Z-#970: #10 'van de klas naar het huis' → 'van school naar huis' (kop volgt)
            if 'is de afstand van de klas naar het huis' in r['opgave']:
                o = r['opgave']; r['opgave'] = o.replace('is de afstand van de klas naar het huis', 'is de afstand van school naar huis', 1); slog(r, "Z-#970: 'van school naar huis'", 'opgave', o, r['opgave'])
        # V-#983 (les 316): E04 #6 020 zak noten €150 → na 25% korting €6 → 8; sleutels 6 (nieuwe prijs) en 7,50 (procent van de nieuwe prijs)
        # Z-#980: minder 50%-items in E04 #1 (route 'nieuwe prijs × 2'): 006 40% €36 → 60 (36 / 50,40), 008 30% €140 → 200 (140 / 182), 014 40% €48 → 80 (48 / 67,20)
        K980 = {'baceb1c1': ('na 50% korting €75.', 25, 6, '8', '7,50', 'V-#983'), '03d597d7': ('na 50% korting €30.', 40, 36, '60', '50,40', 'Z-#980'),
                '16e6400d': ('na 50% korting €100.', 30, 140, '200', '182', 'Z-#980'), '844212d8': ('na 50% korting €40.', 40, 48, '80', '67,20', 'Z-#980')}
        if c8 in K980 and K980[c8][0] in r['opgave']:
            k0, pct, na, ant, vb, pnt = K980[c8]; o = r['opgave']; r['opgave'] = o.replace(k0, f'na {pct}% korting €{na}.', 1); a0_ = str(r['antwoord']); r['antwoord'] = ant
            r['geldigeAntwoorden'] = [ant, f'€{ant}', f'€ {ant}', f'{ant} euro']
            een = f'{na / (100 - pct):.2f}'.replace('.', ',')
            ex['claudeUitleg'] = f'€{na} is {100 - pct}% van de oude prijs.\n1% is {na} : {100 - pct} = {een}, dus 100% is €{ant}.'
            ex['claudeKaleSom'] = f'na {pct}% korting €{na}, was?'
            for d_ in ex.get('claudeDenkfouten') or []:
                d_['fout'] = {'procent-verkeerde-basis': vb, 'getal-overgenomen': str(na)}.get(d_.get('denkfout'), d_.get('fout'))
            lab_ = {d_.get('fout'): d_.get('denkfout') for d_ in ex.get('claudeDenkfouten') or []}
            for i_, f_ in enumerate(ex.get('claudeFoutHints') or []):
                lb_ = (ex.get('claudeDenkfouten') or [{}] * (i_ + 1))[i_].get('denkfout') if i_ < len(ex.get('claudeDenkfouten') or []) else None
                if lb_ == 'procent-verkeerde-basis': f_['fout'] = vb; f_['uitleg'] = f'De {pct}% ging van de óude prijs af, niet van €{na}. €{na} is {100 - pct}%.'
                elif lb_ == 'getal-overgenomen': f_['fout'] = str(na)
            assert int(ant) * (100 - pct) == na * 100 and str(na * 2) != ant, (pnt, c8)
            slog(r, f'{pnt}: {pct}% korting, €{na} → {ant} (geen 50%-route, redelijke prijs)', 'opgave', o, r['opgave'])
        # Z-#985: rente 'Een kind … hij' → 'het'; b6 041 de goede optie preciezer
        if os.environ.get('G8_Z985_RENTE', '1') == '1' and re.match(r'Een kind zet €\d+ op een spaarrekening met \d+% rente per jaar\. Hoeveel rente krijgt hij na één jaar\?', r['opgave']):
            o = r['opgave']; r['opgave'] = o.replace('Hoeveel rente krijgt hij na', 'Hoeveel rente krijgt het na', 1); slog(r, "Z-#985: 'Een kind … het'", 'opgave', o, r['opgave'])
        if c8 == '77e26e67':
            oud_, nw_ = 'Sommige kinderen hebben meer dan één huisdier', 'Sommige kinderen hebben meer dan één soort huisdier'
            if any(o_['tekst'] == oud_ for o_ in r['opties']):
                for o_ in r['opties']:
                    if o_['tekst'] == oud_: o_['tekst'] = nw_
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                if r['antwoord'] == oud_: r['antwoord'] = nw_
                if isinstance(r.get('antwoordDetail'), dict) and r['antwoordDetail'].get('juisteOptieTekst') == oud_: r['antwoordDetail']['juisteOptieTekst'] = nw_
                if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [nw_ if g_ == oud_ else g_ for g_ in r['geldigeAntwoorden']]
                slog(r, "Z-#985: 'meer dan één soort huisdier'", 'antwoord', oud_, nw_)
        # Z-#981 (V01 001): 40 van de 200 → 60 van de 200 = 30 procent; opties 60 / 3 / 30 procent
        if r['opgave'].startswith('Bij een enquête zeggen 40 van de 200 kinderen') and r['antwoord'] == '20 procent':
            o = r['opgave']; r['opgave'] = o.replace('zeggen 40 van de 200 kinderen', 'zeggen 60 van de 200 kinderen', 1)
            W981 = {'40 procent': '60 procent', '2 procent': '3 procent', '20 procent': '30 procent'}
            for o_ in r['opties']: o_['tekst'] = W981.get(o_['tekst'], o_['tekst'])
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            r['antwoord'] = '30 procent'
            if isinstance(r.get('antwoordDetail'), dict): r['antwoordDetail']['juisteOptieTekst'] = W981.get(r['antwoordDetail'].get('juisteOptieTekst'), r['antwoordDetail'].get('juisteOptieTekst'))
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [W981.get(g_, g_) for g_ in r['geldigeAntwoorden']]
            ex['claudeUitleg'] = 'Je vergelijkt 60 met 200. 60 van de 200 is hetzelfde als 30 van de 100. Dus het is 30 procent.'
            _sleutels(W981, {'60 procent': 'Het getal 60 is het aantal kinderen en nog geen percentage. Vergelijk het met 200.'})
            slog(r, 'Z-#981: 60 van de 200 = 30 procent (200 : 10 = 20 was het antwoord)', 'opgave', o, r['opgave'])
        # V-#984 (les 372): E06 #1/#2 vormcue weg; data in bevroren/v984_e06_v1.json (sleutel claudeId[:8])
        if c8 in V984 and r['opgave'] == V984[c8]['oud']:
            t_ = V984[c8]; o = r['opgave']; r['opgave'] = t_['opgave']; r['antwoord'] = t_['antwoord']
            r['opties'] = [{**(r['opties'][i_] if i_ < len(r['opties']) else {}), 'letter': 'ABC'[i_], 'tekst': x_} for i_, x_ in enumerate(t_['opties'])]
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            if isinstance(r.get('antwoordDetail'), dict): r['antwoordDetail'].update(juisteOptie='ABC'[t_['opties'].index(t_['antwoord'])], juisteOptieTekst=t_['antwoord'])
            if r.get('geldigeAntwoorden'): r['geldigeAntwoorden'] = [t_['antwoord']]
            ex['claudeDenkfouten'] = [dict(d_) for d_ in t_['denkfouten']]; ex['claudeFoutHints'] = [dict(f_) for f_ in t_['foutHints']]
            slog(r, 'V-#984: geen vormcue (aantal decimalen/lengte)', 'opgave', o, r['opgave'])
        # V-#1000 (Didactiek b8-hercheck 18:20:30, E06 #2): goede antwoord was in alle 7 items de grootste optie; in 4 items wordt de afleider ': 10' → '× 10' (zelfde plek)
        if c8 in V1000 and r['opgave'] == V1000[c8][0]:
            _, oud_, nw_ = V1000[c8]
            if any(o_['tekst'] == oud_ for o_ in r['opties']):
                r['opties'] = [dict(o_, tekst=nw_) if o_['tekst'] == oud_ else o_ for o_ in r['opties']]
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                for d_ in ex.get('claudeDenkfouten') or []:
                    if d_.get('fout') == oud_: d_['fout'] = nw_
                for f_ in ex.get('claudeFoutHints') or []:
                    if f_.get('fout') == oud_: f_.update(fout=nw_, uitleg='Dat is tien keer te groot. Reken de noemer om naar honderd en doe met de teller precies hetzelfde.')
                slog(r, "V-#1000: afleider ': 10' → '× 10'", 'opties', oud_, nw_)
        # V-#1060 (Didactiek G8-hercheck ec0acc1, verplicht; besluit 19:57 één regel voor alle posities): E06 #1 goed = middelste 49/96. Precies één item:
        # 005 «Schrijf 0,925 in procenten.» afleider '925%' (komma drie plekken) → '9,25%' (komma één plek), zelfde plek; Claude-sleutel komma-verschoven gaat mee.
        # Daarna kleinste 0 · middelste 48 · grootste 48 (Z-#1063: marge 0, niet nog een item wisselen: 47/49 = FAIL).
        if c8 == '066e5862' and r['opgave'] == 'Schrijf 0,925 in procenten.' and any(o_['tekst'] == '925%' for o_ in r['opties']):
            assert str(r['antwoord']) == '92,5%' and '9,25%' not in [o_['tekst'] for o_ in r['opties']], ('V-#1060', r['antwoord'], r['opties'])
            r['opties'] = [dict(o_, tekst='9,25%') if o_['tekst'] == '925%' else o_ for o_ in r['opties']]
            r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in ex.get(k_) or []:
                    if d_.get('fout') == '925%': d_['fout'] = '9,25%'
            slog(r, "V-#1060: afleider '925%' → '9,25%' (komma één plek in plaats van drie)", 'opties', '925%', '9,25%')
        # V-#1032 (Didactiek hercheck b8 19:01:49, Z-#1034 → verplicht; les 398): MEET-V01 #1 goed = grootste in 94/151; in 25 items de 'som'-afleider (d + h + b)
        # → 'een laag te veel' d·b·(h+1) (zelfde plek). Per item nagerekend: nieuwe afleider ≠ antwoord en ≠ andere opties (assert); grootste → 69/151.
        if c8 in V1032 and ((r.get('visual') or {}).get('jsRender') or {}).get('soort') == 'bouwsel':
            jr_ = r['visual']['jsRender']; D_, H_, B_ = jr_['diep'], jr_['hoog'], jr_['breed']; som_, nw_ = D_ + H_ + B_, D_ * B_ * (H_ + 1)
            ops_ = [o_['tekst'] for o_ in r['opties']]
            if str(som_) in ops_:
                assert (V1032[c8] == (som_, nw_)) and str(nw_) not in ops_ and nw_ != D_ * H_ * B_ and str(D_ * H_ * B_) == str(r['antwoord']), (c8, som_, nw_, ops_)
                r['opties'] = [dict(o_, tekst=str(nw_)) if o_['tekst'] == str(som_) else o_ for o_ in r['opties']]
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                for f_ in ex.get('claudeFoutHints') or []:
                    if f_.get('fout') == str(som_): f_.update(fout=str(nw_), uitleg='Dat is een laag te veel. Tel nog eens hoeveel lagen er op elkaar liggen.')
                for d_ in ex.get('claudeDenkfouten') or []:
                    if d_.get('fout') == str(som_): d_['fout'] = str(nw_)
                slog(r, "V-#1032: afleider 'som' → 'een laag te veel' (b·d·(h+1))", 'opties', str(som_), str(nw_))
        # Z-#1042 (zacht, les 402): E05 #2 022/024/028 (€40 + 5%) en 023/026 (€20 + 10%), E05 #3 038/040 (€200, 3%) → andere getallen (E05 #1 013/034 gaat via Z1020).
        # Elke Claude-sleutel volgt zijn eigen route (op label); assert: de oude sleutels waren precies die routes, en geen route = het nieuwe antwoord.
        if r['merge'].get('doel') == 'G8-VERH-E05' and c8 in Z1042_E05:
            o0_ = r['opgave']; x1_, p1_ = Z1042_E05[c8]; ex = r['extraVelden']; kz_ = lambda v: str(v or '').lstrip('€').strip()
            m2_ = re.search(r'kostte €(\d+)\. De prijs stijgt met (\d+)%\.', o0_); m3_ = re.search(r'zet €(\d+) op een spaarrekening met (\d+)% rente per jaar\.', o0_)
            mz_ = m2_ or m3_; x0_, p0_ = int(mz_.group(1)), int(mz_.group(2))
            if (x0_, p0_) != (x1_, p1_):
                def rt_(x, p):
                    d = Fr(x * p, 100); assert d.denominator == 1, (c8, x, p); d = int(d)
                    return (x + d, {'andere-deel-genomen': d, 'verkeerde-bewerking': x - d, 'procent-verkeerde-basis': x + p}) if m2_ else (x + d, {'andere-deel-genomen': d, 'verkeerde-bewerking': x - d, 'komma-verschoven': x + 10 * d})
                a0_, R0_ = rt_(x0_, p0_); a1_, R1_ = rt_(x1_, p1_)
                assert str(a0_) == kz_(r['antwoord']) and a1_ not in R1_.values() and len(set(R1_.values())) == 3 and a1_ not in (x1_, p1_), (c8, a1_, R1_)
                for d_ in ex.get('claudeDenkfouten') or []: assert kz_(d_.get('fout')) == str(R0_[d_['denkfout']]), (c8, 'Z-#1042: oude sleutel ≠ route', d_)
                lab_ = {kz_(d_.get('fout')): d_['denkfout'] for d_ in ex.get('claudeDenkfouten') or []}
                euro_ = lambda oud, nw: ('€' + nw) if str(oud).startswith('€') else nw
                for d_ in ex.get('claudeDenkfouten') or []: d_['fout'] = euro_(d_['fout'], str(R1_[d_['denkfout']]))
                for f_ in ex.get('claudeFoutHints') or []:
                    f_['fout'] = euro_(f_['fout'], str(R1_[lab_[kz_(f_.get('fout'))]]))
                    f_['uitleg'] = (f_.get('uitleg') or '').replace(f'{p0_}% is een deel van €{x0_}, niet €{p0_}.', f'{p1_}% is een deel van €{x1_}, niet €{p1_}.').replace(f'1% van {x0_} is {x0_ // 100}.', f'1% van {x1_} is ' + f'{x1_ / 100:g}'.replace('.', ',') + '.')
                n_ = o0_[:mz_.start()] + (f'kostte €{x1_}. De prijs stijgt met {p1_}%.' if m2_ else f'zet €{x1_} op een spaarrekening met {p1_}% rente per jaar.') + o0_[mz_.end():]
                r['opgave'] = n_; o0a_ = r['antwoord']; r['antwoord'] = euro_(r['antwoord'], str(a1_))
                if isinstance(r.get('antwoordDetail'), dict):
                    for k_, v_ in list(r['antwoordDetail'].items()):
                        if str(v_) == str(o0a_): r['antwoordDetail'][k_] = r['antwoord']
                d1_ = R1_['andere-deel-genomen']
                ex['claudeKaleSom'] = f'{x1_} + {p1_}%'
                ex['claudeUitleg'] = (f'{p1_}% van {x1_} = {d1_}.\nErbij: {x1_} + {d1_} = €{a1_}.' if m2_ else f'Rente: {p1_}% van {x1_} = €{d1_}.\nErbij: {x1_} + {d1_} = €{a1_}.')
                slog(r, 'Z-#1042: dubbel item (E05 #2/#3) → andere getallen', 'opgave', o0_, n_)
        # V-#1040 (Didactiek hercheck b8 19:16:15, verplicht; les 400): na V-#1032 is goed = middelste in 78/151 → in 018/026/035/080 de lage afleider → een route boven
        # het antwoord (goed wordt de kleinste), met een Claude-tekst die al bestaat (Claude-sleutel fout + routetekst, zoals V-#1032).
        # Assert per item: de oude waarde staat erin, de nieuwe waarde is precies die route en geen andere route, ≠ het antwoord, ≠ een andere optie.
        if c8 in V1040 and ((r.get('visual') or {}).get('jsRender') or {}).get('soort') == 'bouwsel':
            jr_ = r['visual']['jsRender']; D_, H_, B_ = jr_['diep'], jr_['hoog'], jr_['breed']; oud_, route_ = V1040[c8]
            R_ = BR.routes(D_, H_, B_); nw_ = R_[route_]; ops_ = [o_['tekst'] for o_ in r['opties']]
            if str(oud_) in ops_:
                assert [k_ for k_, v_ in R_.items() if v_ == nw_] == [route_] and nw_ != D_ * H_ * B_ and str(nw_) not in ops_ and str(D_ * H_ * B_) == str(r['antwoord']), (c8, oud_, route_, nw_, ops_)
                r['opties'] = [dict(o_, tekst=str(nw_)) if o_['tekst'] == str(oud_) else o_ for o_ in r['opties']]
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                tk_ = {'laag te veel': 'Je telde een laag te veel. Tel nog eens hoeveel lagen er op elkaar liggen.', 'laag te weinig': 'Je telde een laag te weinig. Tel nog eens hoeveel lagen er op elkaar liggen.',
                       'drie kanten': 'Dat zijn de blokjes van drie kanten samen. Blokjes op een rand tel je zo twee of drie keer, en blokjes achter en onder zie je niet. Reken één laag uit en doe die keer het aantal lagen.'}[route_]      # Oef-#1030: tekst van V-#1061 (geen richting; 'binnenin' weg)
                for f_ in ex.get('claudeFoutHints') or []:
                    if f_.get('fout') == str(oud_): f_.update(fout=str(nw_), uitleg=tk_)
                for d_ in ex.get('claudeDenkfouten') or []:
                    if d_.get('fout') == str(oud_): d_['fout'] = str(nw_)
                assert any(f_.get('fout') == str(nw_) for f_ in ex.get('claudeFoutHints') or []), (c8, 'V-#1040: Claude-sleutel niet gevonden')
                slog(r, f"V-#1040: lage afleider → '{route_}'", 'opties', str(oud_), str(nw_))
        # b9-datapunten (Oefeningen 8 okt, Oef-#1014–#1020) + Didactiek review-batch9 (V-#1020–#1027, Z-#1021/#1022/#1024)
        if r['merge'].get('doel') == 'G8-VERH-E05':
            o = r['opgave']; nr_ = KOPPIN_E05.get(r['bron']['claudeId'][:8], {}).get('id', '')[-3:]      # ids komen later; de bevroren kop-pin kent het id
            # V-#1021 (les 306): 012/015 toevallige treffers (antwoord = getal uit de vraag) → nieuwe getallen; routes nagerekend (012: 10, 20, 125, 40, 50 ≠ 25; 015: 6, 16,7, 120, 30, 36 ≠ 20)
            if nr_ in V1021 and o == V1021[nr_]['oud']:
                t_ = V1021[nr_]; r['opgave'] = t_['opgave']; r['antwoord'] = t_['antwoord']
                ex['claudeDenkfouten'] = [dict(d_, fout=k_) for d_, k_ in zip(ex['claudeDenkfouten'], t_['sleutels'])]
                ex['claudeFoutHints'] = [dict(f_, fout=k_) for f_, k_ in zip(ex['claudeFoutHints'], t_['sleutels'])]
                ex['claudeKaleSom'] = t_['kaleSom']; ex['claudeUitleg'] = t_['uitleg']; slog(r, 'V-#1021: geen getal uit de vraag als antwoord', 'opgave', o, r['opgave']); o = r['opgave']
            # V-#1020 (les 147/316/370): geloofwaardige dingen (getallen gelijk), de vraag noemt hetzelfde ding als de opgave
            if nr_ in V1020 and (m_ := re.match(r'Een (.+?) kostte €', o)):
                nw_ = V1020[nr_]; lw_ = 'het' if nw_ in HET1020 else 'de'
                n_ = 'Een ' + nw_ + o[m_.end(1):]
                n_ = re.sub(r'Wat kost (?:de|het) [^?]+? nu\?$', f'Wat kost {lw_} {nw_} nu?', n_)
                if n_ != o: r['opgave'] = n_; slog(r, 'V-#1020: geloofwaardig ding, dezelfde naam in de vraag', 'opgave', o, n_); o = n_
            # Z-#1022: 'Een speler zet €… op een spaarrekening' → 'Een kind' (geen verhaal; geen voornaamwoord in de zin)
            if o.startswith('Een speler zet €') and 'spaarrekening' in o:
                r['opgave'] = o.replace('Een speler zet', 'Een kind zet', 1); slog(r, "Z-#1022: 'Een kind'", 'opgave', o, r['opgave']); o = r['opgave']
            # V-#1023 (les 372): 054 heel antwoord, geen telwoorden, geen 'ongeveer' (routes: verschil 12, nieuwe basis 25, getallen 60/48 ≠ 20)
            if o.startswith('Een winkel verkoopt in week 1 zeventig broden en in week 2 vijftig broden.'):
                r['opgave'] = 'Een winkel verkoopt in de eerste week 60 broden en in de tweede week 48 broden. Met hoeveel procent is de verkoop gedaald?'
                r['opties'] = [{**r['opties'][i_], 'letter': 'ABC'[i_], 'tekst': t_} for i_, t_ in enumerate(['12 procent', '20 procent', '25 procent'])]
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                r['antwoord'] = '20 procent'; r['husselen'] = True; r['geldigeAntwoorden'] = ['20 procent']
                if isinstance(r.get('antwoordDetail'), dict): r['antwoordDetail'].update(juisteOptie='B', juisteOptieTekst='20 procent')
                ex['claudeDenkfouten'] = [{'fout': '12 procent', 'denkfout': 'getal-overgenomen'}, {'fout': '25 procent', 'denkfout': 'procent-verkeerde-basis'}]
                ex['claudeFoutHints'] = [{'stap': None, 'fout': '12 procent', 'uitleg': '12 is het verschil in broden. Je moet dat verschil nog vergelijken met het beginaantal.'},
                                         {'stap': None, 'fout': '25 procent', 'uitleg': 'Je vergelijkt met het nieuwe aantal. Bij een daling reken je met het begingetal.'}]
                ex['claudeUitleg'] = 'Het verschil is 60 − 48 = 12 broden. Je vergelijkt 12 met het begingetal 60. 12 van de 60 is 20 procent.'
                slog(r, "V-#1023: heel antwoord, cijfers, geen 'ongeveer'", 'opgave', o, r['opgave']); o = r['opgave']
            # Z-#1020 (Didactiek review-batch9, zacht; data-voorbereiding achter de vlag G8_Z1020=1, gaat mee in de volgende build): spreiding en dubbele items in E05 #1/#3.
            # Alleen de nieuwe prijs/het nieuwe aantal verandert; routes per item nagerekend (assert): verschil, nieuwe basis, nieuw/oud × 100, de twee getallen ≠ het antwoord.
            if os.environ.get('G8_Z1020', '1') == '1' and (c8z_ := r['bron']['claudeId'][:8]) in Z1020:
                mz_ = re.search(r'kostte €(\d+) en kost nu €(\d+)\.|waren er (\d+) (\w+), nu (\d+)\.', o)
                x_, y0_ = (int(mz_.group(1)), int(mz_.group(2))) if mz_.group(1) else (int(mz_.group(3)), int(mz_.group(5)))
                y_ = Z1020[c8z_]
                if y0_ != y_:
                    p_ = Fr((y_ - x_) * 100, x_); assert p_.denominator == 1, c8z_; p_ = int(p_); d0_, d_ = y0_ - x_, y_ - x_
                    nb0_, nb_ = round(Fr(d0_ * 100, y0_)), round(Fr(d_ * 100, y_))
                    routes_ = {d_, round(Fr(d_ * 100, y_)), y_ * 100 // x_, x_, y_}
                    assert p_ not in routes_, (c8z_, p_, routes_)
                    n_ = o[:mz_.start()] + (f'kostte €{x_} en kost nu €{y_}.' if mz_.group(1) else f'waren er {x_} {mz_.group(4)}, nu {y_}.') + o[mz_.end():]
                    slog(r, 'Z-#1020: spreiding/dubbel (E05 #1/#3)', 'opgave', o, n_); r['opgave'] = n_; o = n_; a0_ = r['antwoord']; r['antwoord'] = str(p_)
                    km_ = {str(d0_): str(d_), str(nb0_): str(nb_)}
                    kz_ = lambda v: str(v or '').lstrip('€').strip()      # vóór V-#1026 staan de E05-sleutels nog met '€'
                    ex['claudeDenkfouten'] = [dict(dz_, fout=km_[kz_(dz_.get('fout'))]) for dz_ in ex.get('claudeDenkfouten') or [] if kz_(dz_.get('fout')) in km_]      # kommavormen komen hieronder opnieuw (Z-#1021)
                    ex['claudeFoutHints'] = [dict(fz_, fout=km_[kz_(fz_.get('fout'))], uitleg=re.sub(rf'^{d0_} ', f'{d_} ', fz_.get('uitleg') or '')) for fz_ in ex.get('claudeFoutHints') or [] if kz_(fz_.get('fout')) in km_]
                    assert len(ex['claudeDenkfouten']) >= 2, (c8z_, 'Z-#1020: Claude-sleutels niet gevonden')
                    ex['claudeKaleSom'] = (ex.get('claudeKaleSom') or '').replace(f'naar {y0_}', f'naar {y_}')
                    ex['claudeUitleg'] = (f'De stijging is {y_} − {x_} = {d_}.\n{d_} van {x_} is {p_}%.' if mz_.group(1) else f'Erbij gekomen: {y_} − {x_} = {d_}.\nDat vergelijk je met het oude aantal: {d_} van {x_} is {p_}%.')
                    slog(r, 'Z-#1020: antwoord en Claude-velden bij de nieuwe getallen', 'antwoord', a0_, r['antwoord'])
            # V-#1026 (Oef-#1017; zoals Oef-#1006 bij E04): sleutels zonder '€'; geldigeAntwoorden met en zonder '€' (bedrag) of met '%'/'procent' (procent)
            # Z-#1021: een afgeronde 'nieuwe basis'-sleutel ('33' = 33,3) krijgt ook de kommavorm als sleutel
            if re.fullmatch(r'\d+(?:,\d+)?', str(r['antwoord'])):
                for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                    for d_ in ex.get(k_) or []:
                        v_ = d_.get('fout')
                        if isinstance(v_, str) and v_.startswith('€'): d_['fout'] = v_[1:].strip(); slog(r, "V-#1026: Claude-sleutel zonder '€'", 'claudeSleutel', v_, d_['fout'])
                a_ = str(r['antwoord'])
                if 'Met hoeveel procent' in o:
                    ga_ = [a_, f'{a_}%', f'{a_} %', f'{a_} procent']
                    mg_ = re.search(r'kostte €(\d+) en kost nu €(\d+)\.|waren er (\d+) \w+, nu (\d+)\.', o)
                    if mg_:
                        x_, y_ = (int(mg_.group(1)), int(mg_.group(2))) if mg_.group(1) else (int(mg_.group(3)), int(mg_.group(4)))
                        ex_ = Fr(abs(y_ - x_) * 100, y_)
                        for d_ in list(ex.get('claudeDenkfouten') or []):
                            if ex_.denominator != 1 and re.fullmatch(r'\d+', str(d_.get('fout'))) and int(d_['fout']) == round(ex_):
                                kv_ = f'{float(ex_):.1f}'.replace('.', ',')
                                if kv_.endswith(',0'): continue      # 13,04 → '13,0' is geen kommavorm van een afgeronde sleutel
                                if not any(x2.get('fout') == kv_ for x2 in ex['claudeDenkfouten']): ex['claudeDenkfouten'].append(dict(d_, fout=kv_)); slog(r, 'Z-#1021: afgeronde sleutel ook met komma', 'claudeSleutel', d_['fout'], kv_)
                        # Oef-#1026 (Oef-#1024, les 397): een CL-regel leest alleen claudeFoutHints; de kommavorm krijgt daar dezelfde uitleg als zijn afgeronde vorm,
                        # zodat '33,3' op dezelfde regel en tekst komt als '33' (nagebootst door Oefeningen, hook g8work/zet_1024.py: 17/17)
                        cf_ = ex.get('claudeFoutHints') or []
                        for d_ in ex.get('claudeDenkfouten') or []:
                            kv_ = str(d_.get('fout') or '')
                            if not re.fullmatch(r'\d+,\d+', kv_) or any(str(c_.get('fout') or '').lstrip('€') == kv_ for c_ in cf_): continue
                            r_ = str(int(Fr(kv_.replace(',', '.')) + Fr(1, 2)))
                            bron_ = next((c_ for c_ in cf_ if str(c_.get('fout') or '').lstrip('€') == r_), None)
                            if bron_: cf_.append(dict(bron_, fout=kv_)); slog(r, 'Oef-#1026: kommasleutel ook in claudeFoutHints (uitleg van de afgeronde vorm)', 'claudeFoutHints', r_, kv_)
                        if cf_: ex['claudeFoutHints'] = cf_
                else: ga_ = [a_, f'€{a_}', f'€ {a_}', f'{a_} euro']
                if r.get('geldigeAntwoorden') != ga_: r['geldigeAntwoorden'] = ga_
        if r['merge'].get('doel') == 'G8-VBN-V01':
            # V-#1025 (les 390; Oef-#1019): rooster #1 niet live zonder assenstelsel-renderer; antwoord in de notatie van de opgave '(x, y)', invoer ook '(x,y)', 'x,y', 'x, y'
            if (m_ := re.fullmatch(r'Zet de stip op \((\d+), (\d+)\)\.', r['opgave'])):
                x_, y_ = m_.groups(); a0 = r['antwoord']; r['antwoord'] = f'({x_}, {y_})'
                r['geldigeAntwoorden'] = [f'({x_}, {y_})', f'({x_},{y_})', f'{x_},{y_}', f'{x_}, {y_}']
                r.pop('nietLiveZonderBeeld', None)      # V-#1030 (les 395): de vlag hoort in visual, daar kijken alle lezers
                if not r.setdefault('visual', {}).get('nietLiveZonderBeeld'): r['visual']['nietLiveZonderBeeld'] = True
                ex['claudeDenkfouten'] = [d_ for d_ in ex.get('claudeDenkfouten') or [] if d_.get('fout') not in r['geldigeAntwoorden']]
                if x_ != y_ and not any(d_.get('fout') == f'{y_},{x_}' for d_ in ex['claudeDenkfouten']): ex['claudeDenkfouten'].append({'fout': f'{y_},{x_}', 'denkfout': 'omgewisseld'})
                # '1' bij (1, 0) (alleen één getal) is een fout-sleutel via de motorregel 'fout = een getal uit de vraag' (Oefeningen, b9 r1b); geen Claude-sleutel,
                # want de CL-regel van V01 #1 geeft elke Claude-sleutel de tekst 'omgewisseld'
                ex['claudeDenkfouten'] = [d_ for d_ in ex['claudeDenkfouten'] if not (re.fullmatch(r'\d+', str(d_.get('fout'))) and d_.get('denkfout') != 'omgewisseld')]
                if a0 != r['antwoord']: slog(r, "V-#1025: antwoord '(x, y)', niet live zonder plaatje", 'antwoord', a0, r['antwoord'])
            # V-#1025: 013 lijngrafiek-renderdata (vorm G6-VBN-E02)
            if r['opgave'].startswith('In de lijngrafiek zie je de temperatuur op een dag, van 8.00 uur tot 16.00 uur.') and not (r.get('visual') or {}).get('jsRender'):
                r.setdefault('visual', {})['jsRender'] = {'soort': 'lijngrafiek', 'titel': 'Temperatuur op een dag', 'punten': [{'naam': '8.00 uur', 'waarde': 12}, {'naam': '12.00 uur', 'waarde': 18}, {'naam': '16.00 uur', 'waarde': 15}], 'max': 20, 'perstreep': 2, 'cijfer_om': 2}
                slog(r, 'V-#1025: renderdata lijngrafiek', 'visual', None, 'jsRender lijngrafiek')
            # V-#1027 (Oef-#1020): uitleg 014 over sporten
            if 'welke sport' in r['opgave'] and 'blauw' in (ex.get('claudeUitleg') or ''):
                u_ = ex['claudeUitleg']; ex['claudeUitleg'] = 'De helft van de cirkel is voetbal. De helft van 24 is 12. Dus 12 kinderen kiezen voetbal.'; slog(r, 'V-#1027: uitleg bij de sportnamen', 'claudeUitleg', u_, ex['claudeUitleg'])
            for f_ in ex.get('claudeFoutHints') or []:
                if f_.get('fout') == 'De temperatuur daalt met 6 graden' and f_.get('uitleg', '').startswith('Je begon bij 8.00 uur'):
                    u_ = f_['uitleg']; f_['uitleg'] = 'Lees de temperatuur af om 12.00 uur en om 16.00 uur. Het verschil tussen die twee is wat er verandert.'; slog(r, "Oef-#1020: tekst bij 'daalt met 6 graden'", 'claudeFoutHint', u_, f_['uitleg'])
            # Z-#1024: V01 #4 «Hoeveel is dat?» → «Bij welk getal staat de staaf?»
            if r['opgave'].startswith('In een grafiek loopt de as met stappen van') and r['opgave'].endswith('Hoeveel is dat?'):
                o = r['opgave']; r['opgave'] = o[:-len('Hoeveel is dat?')] + 'Bij welk getal staat de staaf?'; slog(r, 'Z-#1024: vraag', 'opgave', o, r['opgave'])
        # Oef-#1007/#1008 (b8, VERH-E06 #3 001): sleutels '1,3' → '1,25' (12,5 : 10) en '12.5' → '12,5'; logische context (rotte appels i.p.v. kapotte vissen)
        if c8 == 'c7db8f20' and r['opgave'].startswith('12,5% van de vissen is kapot.'):
            o = r['opgave']; r['opgave'] = o.replace('12,5% van de vissen is kapot.', '12,5% van de appels in de kist is rot.', 1)
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                for d_ in r['extraVelden'].get(k_) or []: d_['fout'] = {'1,3': '1,25', '12.5': '12,5'}.get(d_.get('fout'), d_.get('fout'))
            slog(r, "Oef-#1007/#1008: sleutels 1,25 en 12,5; logische context", 'opgave', o, r['opgave'])
        # Oef-#1011 (b8, VERH-E02 001): claudeUitleg 'Eén pet' → 'Eén pak sap'; en in alle G8-Claude-uitleg 'x' tussen getallen → '×'
        if c8 == '6cc5501f' and 'Eén pet kost' in (r['extraVelden'].get('claudeUitleg') or ''):
            r['extraVelden']['claudeUitleg'] = r['extraVelden']['claudeUitleg'].replace('Eén pet kost', 'Eén pak sap kost'); slog(r, "Oef-#1011: 'pak sap'", 'claudeUitleg', 'pet', 'pak sap')
        for k_ in ('claudeUitleg', 'claudeKaleSom'):
            u_ = r['extraVelden'].get(k_)
            if isinstance(u_, str) and re.search(r'\d ?x ?\d', u_):
                r['extraVelden'][k_] = re.sub(r'(\d) ?x ?(\d)', r'\1 × \2', u_); slog(r, "Oef-#1011: '×' in Claudes uitleg", k_, u_[:60], r['extraVelden'][k_][:60])
        # Z-#931 (Didactiek, zacht; G8 MEET-E03 #1–#4): m³ → liter, geldigeAntwoorden met en zonder punt en met de gevraagde eenheid (liter)
        if (m_ := re.fullmatch(r'Een [\w ]+ heeft een inhoud van [\d,]+ m³\. Hoeveel liter is dat\?', r['opgave'])) and re.fullmatch(r'\d{4,6}', str(r['antwoord'])) and not r.get('geldigeAntwoorden'):
            a_ = str(r['antwoord']); pt_ = f'{int(a_):,}'.replace(',', '.')      # Z-#953: ook '3000 l', '3.000 liter', '3.000 l' (en 'L')
            r['geldigeAntwoorden'] = [a_, pt_, f'{a_} liter', f'{pt_} liter', f'{a_} l', f'{pt_} l', f'{a_} L', f'{pt_} L']
            slog(r, 'Z-#931/Z-#953: geldigeAntwoorden (met/zonder punt, met eenheid liter/l/L)', 'geldigeAntwoorden', None, r['geldigeAntwoorden'])
        # Z-#894 (Didactiek batch 6, zacht): VBN-E04 #35 «zijn de staven samen 30 hoog» → «tellen de staven samen op tot 30» (kop volgt in de kop-pass)
        if c8 == '77e26e67' and 'zijn de staven samen 30 hoog' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('zijn de staven samen 30 hoog', 'tellen de staven samen op tot 30', 1); slog(r, "Z-#894: 'tellen de staven samen op tot 30'", 'opgave', o, r['opgave'])
        # Z-#825 (Didactiek batch 3): #55 'staartsom' → 'som onder elkaar'
        if c8 == '5a2c100b' and 'met een staartsom onder elkaar' in r['opgave']:
            o = r['opgave']; r['opgave'] = o.replace('met een staartsom onder elkaar', 'met een som onder elkaar')
            slog(r, "Z-#825: 'staartsom' → 'som onder elkaar'", 'opgave', o, r['opgave'])
        # Oef-#487 (batch 3): E02 #40 'de eerste naam' was dubbelzinnig (bovenste naam in de lijst) → 'de naam die in het alfabet vooraan komt'
        if c8 == '43a76b21':
            oud, nieuw = 'Zoek steeds de eerste naam en zet die apart', 'Zoek steeds de naam die in het alfabet vooraan komt en zet die apart'
            if any(o_['tekst'] == oud for o_ in r['opties']):
                for o_ in r['opties']:
                    if o_['tekst'] == oud: o_['tekst'] = nieuw
                r['optiesTekst'] = ' · '.join(f"{o_['letter']}) {o_['tekst']}" for o_ in r['opties'])
                if r['antwoord'] == oud: r['antwoord'] = nieuw
                ad_ = r.get('antwoordDetail')
                if isinstance(ad_, dict) and ad_.get('juisteOptieTekst') == oud: ad_['juisteOptieTekst'] = nieuw
                slog(r, "Oef-#487: 'de eerste naam' → 'de naam die in het alfabet vooraan komt'", 'antwoord', oud, nieuw)
        # Oef-#482 (Didactiek Z-#764, Oefeningen akkoord 15:58): E03 #2 'Reken uit. a : b + c' — Claudes komma-sleutels a : (b + c) weg; '7,0' → '7'
        if re.fullmatch(r'Reken uit\. \d+ : \d+ \+ \d+', r['opgave']):
            ex = r['extraVelden']; voor = [d_['fout'] for d_ in ex.get('claudeDenkfouten') or []]
            for k_ in ('claudeDenkfouten', 'claudeFoutHints'):
                L_ = []
                for d_ in ex.get(k_) or []:
                    f_ = str(d_.get('fout'))
                    if re.fullmatch(r'\d+,0', f_): d_['fout'] = f_[:-2]
                    elif re.fullmatch(r'\d+,\d+', f_): continue
                    L_.append(d_)
                if ex.get(k_) is not None: ex[k_] = L_
            na = [d_['fout'] for d_ in ex.get('claudeDenkfouten') or []]
            if na != voor: slog(r, "Oef-#482: komma-sleutel weg ('7,0' → '7')", 'claudeDenkfouten', str(voor), str(na))
        # Z-#781 (Didactiek G8 batch 2): #12 'Tel … bij elkaar op' is alleen fout zolang de ochtendtemperatuur niet onder nul is (data-guard)
        m_ = re.match(r"'s Ochtends is het (\S+) graden", r['opgave'])
        if m_: assert not m_.group(1).startswith(('−', '-')), ('Z-#781: ochtendtemperatuur onder nul', r['id'])
        if c8 == '1c755b40' and r['opgave'].startswith('In een grafiek staat'):
            o = r['opgave']; r['opgave'] = o.replace('In een grafiek staat', 'In een staafgrafiek staat', 1); slog(r, "Oef-#480: 'staafgrafiek' (de opties gaan over staven)", 'opgave', o, r['opgave'])

# Oef-#472 / #478 (G8 batch 1/2, 8 okt; zoals G4 Z-#726): de kop-generator maakte van 'kan' en van werkwoorden een '[ding]'.
KOP478 = [(r'^(Kijk zonder uit te rekenen\. Welk antwoord bij # [×+−:] #) \[ding\] kloppen\?$', r'\1 kan kloppen?'),
          (r'nu €# \[ding\]\.', 'nu €# kost.'), (r'^Een jas van €# \[ding\] # procent', 'Een jas van €# gaat # procent'),
          (r'= # \[ding\]\. Hoe kan', '= # uitgerekend. Hoe kan'), (r'^Hoe zie je of een getal deelbaar is door #\?$', 'Hoe zie je of een getal deelbaar is door 5?'),  # Z-#780
          (r'^In groep # \[ding\] # \[ding\]\.', 'In groep # zitten # leerlingen.'),
          (r'^De trein vertrekt om # uur en komt aan om # uur\.', 'De trein vertrekt om #.# uur en komt aan om #.# uur.'),
          # Oef-#488 (batch 3): [ding] op een werkwoord of voorzetsel
          (r'moet # × # \[ding\]', 'moet # × # uitrekenen'), (r'# − # \[ding\] elkaar uitgerekend', '# − # onder elkaar uitgerekend'),
          (r'# × # \[ding\] te doen', '# × # apart te doen'), (r'^In groep # \[ding\] # \[ding\] een cijfer', 'In groep # hebben # kinderen een cijfer'),
          (r'staartsom onder elkaar', 'som onder elkaar'),
          # Oef-#491 (batch 4): 'miljoen' hoort in het vaste deel, niet op een [ding]-plek (M01 #2–#5); de E05-slotvraag noemt het [ding] ('Hoeveel potjes blijven er over?')
          (r'^In een land wonen # \[ding\] mensen\.', 'In een land wonen # miljoen mensen.'), (r'^\[wie\] heeft # \[ding\] (\w+) verzameld\.', r'[wie] heeft # miljoen \1 verzameld.'),
          (r'(De volle \w+ gaan weg\.) Hoeveel blijven er over\?$', r'\1 Hoeveel [ding] blijven er over?')]  # V-#781: '14.35' werd één '#'
PLEK496 = {'de dierentuin': 'Amsterdam', 'het museum': 'Rotterdam', 'het bos': 'Eindhoven', 'de kantine': 'Maastricht', 'het stadion': 'Groningen',
           'de kleedkamer': 'Amsterdam', 'de vallei': 'Rotterdam', 'het nest': 'Eindhoven', 'het veld': 'Maastricht', 'de schuur': 'Groningen',
           'de school': 'Eindhoven', 'de klas': 'Rotterdam', 'het huis': 'Groningen'}
KOP478 += [  # Oef-#496 (batch 5)
          (r'^Een bak voor knopen heeft een inhoud van # \[ding\]\.', 'Een vijver heeft een inhoud van # m³.'),
          (r'^Een bak voor tanden heeft een inhoud van # \[ding\]\.', 'Een watertank heeft een inhoud van # m³.'),
          (r'^Een bak voor truien heeft een inhoud van # \[ding\]\.', 'Een regenput heeft een inhoud van # m³.'),
          (r'^Een bak voor wortels heeft een inhoud van # \[ding\]\.', 'Een opblaaszwembad heeft een inhoud van # m³.'),
          (r'^(Een vliegtuig vertrekt om \S+(?: uur)? uit) de school\.', r'\1 Eindhoven.'), (r'^(Een vliegtuig vertrekt om \S+(?: uur)? uit) de klas\.', r'\1 Rotterdam.'),
          (r'^(Een vliegtuig vertrekt om \S+(?: uur)? uit) het huis\.', r'\1 Groningen.')]
E05_BEZET = set()
V1020 = {'004': 'koptelefoon', '005': 'jas', '006': 'trui', '007': 'step', '008': 'rugzak', '009': 'skateboard', '010': 'spijkerbroek', '011': 'sporttas', '014': 'spel',
         '015': 'boek', '016': 'tent', '017': 'kaartje', '018': 'trui', '034': 'bordspel', '019': 'jas', '020': 'step', '021': 'koptelefoon', '024': 'bal', '025': 'sporttas',
         '026': 'boek', '027': 'spel', '029': 'tent', '030': 'rugzak', '031': 'skateboard', '032': 'fiets', '035': 'telefoon'}      # V-#1020 (review-batch9-didactiek.md, vervangtabel; 012/013/022/023/028/033 blijven)
HET1020 = {'skateboard', 'spel', 'boek', 'bordspel', 'kaartje'}
V1021 = {'012': {'oud': 'Een bal kostte €20 en kost nu €25. Met hoeveel procent is de prijs gestegen?', 'opgave': 'Een bal kostte €40 en kost nu €50. Met hoeveel procent is de prijs gestegen?',
                 'antwoord': '25', 'sleutels': ['10', '20'], 'kaleSom': 'van 40 naar 50 = +__%', 'uitleg': 'De stijging is 50 − 40 = 10.\n10 van 40 is 25%.'},
         '015': {'oud': 'Een ei kostte €20 en kost nu €24. Met hoeveel procent is de prijs gestegen?', 'opgave': 'Een ei kostte €30 en kost nu €36. Met hoeveel procent is de prijs gestegen?',
                 'antwoord': '20', 'sleutels': ['6', '17'], 'kaleSom': 'van 30 naar 36 = +__%', 'uitleg': 'De stijging is 36 − 30 = 6.\n6 van 30 is 20%.'}}      # V-#1021; 'ei' → 'boek' via V1020
Z1020 = {'9a772298': 92, 'db8f17ef': 168, 'ebb7cc5c': 78, '5a73879c': 60, 'ee1a0072': 70}      # + Z-#1042: 034 (bordspel) €40→€70 (75%), was dubbel met 013      # Z-#1020: 014 €80→€92 (15%), 016 €120→€168 (40%), 018 €60→€78 (30%), 043 50→60 (20%)
KOPPIN_E05 = json.load(open(os.path.join(os.path.dirname(HERE), 'bevroren', 'kop_e05_fase1.json'), encoding='utf-8'))['items']
V1040 = {'1a8192c9': (7, 'laag te veel'), '272c995d': (24, 'laag te veel'), '2a4533b9': (7, 'drie kanten'), '7b4f6289': (9, 'drie kanten')}      # V-#1040: MEET-V01 #1 018/026/035/080
# Z-#1044 (zacht) niet gedaan: bij 062 (2×7×2) is 32 de enige route boven het antwoord 28 ('laag te veel' = 'drie kanten'); elke andere route ligt eronder
# (24, 22, 14, 11, 4), dan wordt goed de grootste (70 > 69, b6 Z-#891 FAIL). Twee routes op 32 blijven dus staan (tekst 'laag te veel' is waar).
Z1042_E04 = {'5b3d9b42': 36, 'd19d8dde': 48}      # Z-#1042: E04 #1 013 (rugzak) €60 → €36 (48), 018 (hondenmand) €60 → €48 (64)
Z1042_E05 = {'28734363': (60, 5), '19567cbf': (50, 20), '8cbb8ff1': (30, 10), 'fa7305ab': (500, 3)}      # Z-#1042: E05 #2 024 bal €60 + 5% (63), 028 trui €50 + 20% (60), 026 boek €30 + 10% (33); E05 #3 040 Sanne €500, 3% (515)
V1032 = {'023be4f1': (15, 144), '0e717574': (13, 100), '0e749130': (10, 48), '0f7cd32b': (15, 140), '15f71b96': (13, 90), '197e0468': (12, 56), '1dddba65': (14, 108),
         '2432ac03': (15, 150), '291b2b8b': (10, 48), '298cd898': (13, 84), '29c3bd48': (13, 84), '3449ddfd': (13, 100), '38f2d9c6': (10, 45), '397449da': (11, 60),
         '3e70fde2': (10, 45), '3efc947b': (11, 42), '41023e89': (16, 147), '5153c129': (14, 120), '54171e5e': (15, 144), '5626d9b4': (11, 32), '58c0842d': (9, 30),
         '5abd2ce6': (17, 216), '6831cb91': (13, 96), '699f2c0b': (16, 168), '6ac8c567': (12, 56)}      # V-#1032: MEET-V01 #1 005–071 (kandidatenlijst Didactiek), c8 → (som, laag te veel)
V1000 = {'7ed68c70': ('Schrijf 7/20 in procenten.', '3,5%', '350%'), 'ab56131e': ('Schrijf 13/50 in procenten.', '2,6%', '260%'),      # V-#1000 (E06 #2)
         'ce8f7a73': ('Schrijf 11/20 in procenten.', '5,5%', '550%'), 'd44aa1d9': ('Schrijf 18/25 in procenten.', '7,2%', '720%')}
V984 = json.load(open(os.path.join(os.path.dirname(HERE), 'bevroren', 'v984_e06_v1.json'), encoding='utf-8'))['items']      # V-#984 (b8 deel B)
E05_TEL = {}
E05_VOORKEUR = {'b446e342': (8, 39)}      # Z-#950: 031 39 kinderen, busje van 8 → 5 busjes, rest 7 (Didactiek, recheck b4)
KOP1001_DOELEN = {'G8-MEET-E07', 'G8-MEET-V01', 'G8-VBN-E01', 'G8-VBN-E03', 'G8-VBN-E04'}
KOP478 += [  # V-#871c (Didactiek batch 4)
          (r'^\[wie\] heeft # miljoen (stickers|knikkers) verzameld\.', r'Een fabriek maakt in een jaar # miljoen \1.'),
          (r'^\[wie\] heeft # miljoen truien verzameld\.', 'In Nederland worden in een jaar # miljoen truien verkocht.'),
          (r'^Een fabriek maakt in een jaar # \[ding\] (stickers|knikkers)\.', r'Een fabriek maakt in een jaar # miljoen \1.'),
          (r'^In Nederland worden in een jaar # \[ding\] truien verkocht\.', 'In Nederland worden in een jaar # miljoen truien verkocht.')]
PLEK972 = r'(?:het station|het stadion|de camping|het strand|het dorp|de stad|de boerderij|het meer|de school|het zwembad|de haven|de vuurtoren|de bakker|de bibliotheek|de kerk|het plein|\[plek\])'
KOP478 += [(r'^(Op een kaart met schaal # : # is de afstand van )' + PLEK972 + r' naar ' + PLEK972 + r'( # cm\. Hoeveel meter is dat in het echt\?)$', r'\1[plek] naar [plek]\2')]      # V-#972: kop blijft '[plek] naar [plek]'; Z-#985-rente staat uit (G8_Z985_RENTE=1) tot Oefeningen de data-eis van b8/check E04 #2 aanpast
KOP478 += [(r'^(\[wie\] zet €# op een spaarrekening met #% rente per jaar\. Hoeveel \[ding\] krijgt) het( na één jaar\?)$', r'\1 hij\2')]      # Z-#985 (G8_Z985_RENTE=1): 'Een kind … het' (6 items), 'Een speler … hij' (024/027) blijft; één kop in fase 1, zodat 024/027 hun hints houden
# Oef-#1014/#1015/#1016 (één kop voor prijsstijging, rente-namen, 'zak noten'): NIET in deze build. De kopregels laten batch9 #1/#18, #5–#17/#20,
# #2/#4/#9/#10/#21 en batch8 #1/#6 op één kop vallen; sync_hint_keys voegt nooit stil samen (#30) → apply_hints stopt. Eerst één hint-entry per
# samengevoegde kop (Oefeningen, patch_batch8/9), dan deze regels aanzetten (G8_KOP1014=1):
if os.environ.get('G8_KOP1014', '1') == '1':
    KOP478 = [(r'^Een zak noten (kost|kostte) ', r'Een [ding] \1 ')] + KOP478
    KOP478 += [(r'^(Een \[ding\] kostte €#\. De prijs stijgt met #%\. Wat kost) (?:de|het) [^?]+?( nu\?)$', r'\1 [ding]\2'),
               (r'^(?:Daan|Milan|Sanne|Fatima) (zet €# op een spaarrekening met #% rente per jaar\. Hoeveel staat er na één jaar op de rekening\?)$', r'[wie] \1')]
KOP478 += [(r'^(In een grafiek loopt de as met stappen van #\. De staaf van groep #) \[ding\] (precies tussen)', r'\1 staat \2'),      # Oef-#1020: 'staat' is geen [ding]
           (r'^(Een winkel verkoopt in week #) (?:#|\[ding\]) (broden en in week #) (?:#|\[ding\]) (broden\.)', r'\1 # \2 # \3')]      # Oef-#1018
def kop_g8(s):
    for a, b in KOP478: s = re.sub(a, b, s)
    return s

def twijfel_md(cats, bui, t7):
    out = ['# G8-merge: twijfel voor Didactiek (build ' + datetime.datetime.now().strftime('%d-%m %H:%M') + ')', '',
           'Per categorie: aantal, voorstel, de vraag en voorbeelden. Volledige items: data/twijfel.json. Besluit per categorie (of per item) graag terug in een besluitenbestand, zoals bij G7.', '']
    for c, v in sorted(cats.items(), key=lambda x: -len(x[1])):
        out += [f"## {c} ({len(v)})", '', f"Voorstel-doel: {', '.join(f'{k} ({n})' for k, n in collections.Counter(r['merge']['voorstelDoel'] for r in v).items())}", '',
                f"**Vraag:** {TWIJFELVRAAG.get(c, '')}", '', 'Voorbeelden:']
        for r in B3.voorbeelden(v)[:4]: out.append(f"- `{r['id']}` {r['opgave'][:140]} → {r['antwoord']}")
        out.append('')
    out += [f"## Ter info: buiten de basisschool ({len(bui)})", '']
    for k, n in collections.Counter(r['merge']['reden'].split(':')[0] for r in bui).items(): out.append(f'- {k}: {n}')
    out += ['', f"## Ter info: terug naar G7 ({len(t7)})", '']
    for k, n in collections.Counter((r['merge']['voorstelDoel'], r['merge']['regel'], bool(r['merge'].get('aanvullingG7'))) for r in t7).items():
        out.append(f"- {k[0]} ({G7D.get(k[0], '')}), regel {k[1]}: {n}" + (' · ook in g7/data/aanvulling_uit_g8.json' if k[2] else ''))
    open(f'{OUT}/twijfel_voor_didactiek.md', 'w').write('\n'.join(out) + '\n')

if __name__ == '__main__':
    if os.environ.get('G8_STAGING') != '1':      # Oefeningen 17:27 (lege map): bouw nooit direct op live; scripts/bouw_veilig.py bouwt in een kopie en zet daarna atomair om
        sys.path.insert(0, HERE); import bouw_veilig; sys.exit(bouw_veilig.main())
    rows, gem, twf, t7, bui, stats = main()
    print('pool', stats['pool'], '(G7-park', stats['g7ParkInPool'], 'van', stats['g7ParkTotaal'], ') | rows', len(rows), 'gemapt', len(gem), 'twijfel', len(twf), 'terug-G7', len(t7),
          '(aanvulling G7', stats['aanvullingG7'], ') buiten', len(bui), '| al in G3–G7', stats['alInG3G7']['totaal'], '| geen regel', stats['geenRegel'], '| geschrapt', stats['geschrapt'])
    print('controle', stats['controle']); print('naar groep', stats['naarGroep'])
