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
import json, re, csv, collections, subprocess, os, sys, math, datetime, hashlib
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(HERE)
G3, G4, G5, G6, G7 = (f'/workspace/claude-merge/g{n}' for n in (3, 4, 5, 6, 7))
sys.path.insert(0, f'{HERE}/g7_basis')
import build_g7 as B7                     # laadt de hele G7-keten (alleen functies; B7.main wordt nooit aangeroepen)
M, B3, R4, R5, R6, R7, BG7, FX21 = B7.M, B7.B3, B7.R4, B7.R5, B7.R6, B7.R7, B7.BG7, B7.FX21
V, CDOEL, CREDIT, COMMIT, EXP = B3.V, B3.CDOEL, B3.CREDIT, B3.COMMIT, B3.EXP
R, G, T = R7.R, R7.G, R7.T
OURS = {d['id']: {'bordtitel': d['bordtitel'], 'korteNaam': d['korteNaam'], 'domein': d['domein'], 'aantalItems': d['aantalItems']}
        for g in EXP['groepen'] if g['groep'] == 8 for dm in g['domeinen'] for d in dm['doelen']}
import besluiten_g8 as BG8                 # Didactiek-besluiten op de 1226 G8-twijfelitems + Dave 20:56
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
        hercontrole_g8(it, q)
        it['licentie']['wijzigingen'] = sorted({f['soort'] for f in B3.FIXLOG if f['id'] == q['id']}); it['licentie']['gewijzigd'] = True
        it['merge']['somtype'] = BG7.somtype(it) or B7.somtype_g7(it)
        rows.append(it)
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
    for g, G_ in ((4, G4), (5, G5), (6, G6), (7, G7)):
        its = naar[g] + (aanv if g == 7 else [])
        if g != 7 and not BESLUIT_G8: continue          # zonder besluitenbestand: niets nieuws voor G4–G6 (de uitkomst blijft gelijk)
        json.dump(dict(meta, uitleg=(f'Claude-items uit de G8-pool voor G{g}: besluiten Didactiek (g8/besluiten_twijfel.json) en Dave 20:56. ' if g != 7 else
                                     'Claude-items uit de G8-pool voor G7: terug-G7 met een passend G7-doel en besluiten Didactiek/Dave 20:56. ') +
                       f'build_g{g} leest dit bestand (tools/aanvulling_g8.py): de items komen achter de bestaande items, met merge.voorstelDoel als doelId. Ids hier zijn G8-ids (merge.uitG8.g8Id in G{g}).',
                       aantal=len(its), perDoel=dict(collections.Counter(r['merge']['voorstelDoel'] for r in its)), items=sorted(its, key=lambda x: x['id'])),
                  open(f'{G_}/data/aanvulling_uit_g8.json', 'w'), ensure_ascii=False, indent=1)
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
    twijfel_md(cats, bui, t7)
    for sc in ('sync_hint_keys.py', 'apply_hints.py'):
        subprocess.run([sys.executable, f'{HERE}/{sc}'], check=True)
    return rows, gem, twf, t7, bui, stats

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
    rows, gem, twf, t7, bui, stats = main()
    print('pool', stats['pool'], '(G7-park', stats['g7ParkInPool'], 'van', stats['g7ParkTotaal'], ') | rows', len(rows), 'gemapt', len(gem), 'twijfel', len(twf), 'terug-G7', len(t7),
          '(aanvulling G7', stats['aanvullingG7'], ') buiten', len(bui), '| al in G3–G7', stats['alInG3G7']['totaal'], '| geen regel', stats['geenRegel'], '| geschrapt', stats['geschrapt'])
    print('controle', stats['controle']); print('naar groep', stats['naarGroep'])
