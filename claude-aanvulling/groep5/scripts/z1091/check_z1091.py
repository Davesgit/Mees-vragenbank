#!/usr/bin/env python3
"""Check Z-#1091 per somtype. [MUT=..] [SNAP=1] python3 check_z1091.py <somtype> <basis>  (snap/verwacht in ./<somtype>/)
- guard/weggever: geen bedrag ('één te veel', 'één honderdtal …', 'twee te …', 'één stap …', 'één ronde te ver') in entry- of itemteksten van het somtype
  (VBN-E03: alleen de V-#1052-zin);
- richting per item: zegt de itemtekst te veel/te ver (omhoog) dan ligt de waarde boven het antwoord, te weinig/niet ver genoeg (omlaag) eronder;
- SNAP per regel (doel#nr soort → tekst, tekstSterker)."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [D_, os.path.join(D_, '..', 'z1090', 'r4')]
from bedrag_lib import *; from g5pad import *
DOEL, B = sys.argv[1], sys.argv[2]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
SNAPF = os.path.join(D_, DOEL.replace('G5-', ''), 'snap.json')
ENT0 = [s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'] == DOEL]
ENT = [s for s in ENT0 if DOEL != 'G5-MEET-E03' or s['nrOrigineel'] == 1]
XS = [(k, x) for k, xs in I.items() if k[0] == DOEL and (DOEL != 'G5-MEET-E03' or k[1] == 1) for x in xs]
def guard(t): return bool(BEDRAG.search(t))
if MUT == 'M_dag': x_, h_ = next((x, h) for x in I[('G5-MEET-E06', 7)] for h in x['foutHints'] if 'teruggeteld' in (h.get('uitleg') or '')); h_['uitleg'] = 'Je bent te ver teruggeteld.' if 'niet ver genoeg' in h_['uitleg'] else 'Je bent niet ver genoeg teruggeteld.'      # Oef-#1057
if MUT == 'M_dag6': x_, h_ = next((x, h) for x in I[('G5-MEET-E06', 6)] for h in x['foutHints'] if re.search(r'(te ver|niet ver genoeg) geteld', h.get('uitleg') or '')); h_['uitleg'] = 'Je bent te ver geteld.' if 'niet ver genoeg' in h_['uitleg'] else 'Je bent niet ver genoeg geteld.'      # Oef-#1058
if MUT == 'M_nodig' and DOEL == 'G5-GET-M06': next(f for s in ENT if s['nrOrigineel'] == 7 for f in [s] if f.get('hint2'))['hint2'] += ' Dan is er nog een tafel nodig.'
if MUT == 'M_bedrag':
    f_ = next(f for s in ENT for f in s['foutHints'] if f.get('tekst')); f_['tekst'] = ('Dat is één ronde te ver. ' if DOEL == 'G5-VBN-E03' else 'Dat is één te veel. ') + f_['tekst']
if MUT == 'M_item':
    h_ = next(h for _, x in XS for h in x['foutHints'] if h.get('uitleg')); h_['uitleg'] = (V1052[0] + ' ' if DOEL == 'G5-VBN-E03' else 'Dat is twee te weinig. ') + h_['uitleg']
if MUT == 'M_snap':      # een regel die in de SNAP staat
    _ks = set(json.load(open(SNAPF, encoding='utf-8'))) if os.path.exists(SNAPF) else set()
    f_ = next(f for s in ENT for f in s['foutHints'] if f"{s['doel']}#{s['nrOrigineel']} {f['soort']}" in _ks and f.get('tekst')); f_['tekst'] += ' Kijk goed.'
for s in ENT:
    for f in [s] + s['foutHints']:
        for v in (('hint1', 'hint2') if f is s else ('tekst', 'tekstSterker')):
            if guard(f.get(v) or ''): F.append(f"bedrag {DOEL} #{s['nrOrigineel']} {f.get('soort', '-')!r} [{v}]: {f[v][:80]}")
n_r = geen = 0
for (d, n), x in XS:
    a = getal(x['antwoord'])
    for h in x['foutHints']:
        t = (h.get('uitleg') or '') + ' ' + (h.get('uitlegSterker') or '')
        if guard(t): F.append(f"weggever {d} #{n} {x['nr']} sleutel {h['fout']!r}: {t.strip()[:80]}")
        if DOEL == 'G5-MEET-E06' and re.search(r'wijzer|terug|\b(januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december)\b', t + ' ' + str(h['fout'])):
            if re.search(r'(terug)?geteld\b', t) and re.search(r'te ver (terug)?geteld|niet ver genoeg (terug)?geteld', t) and re.search(r'\b(\d+)\s+\w+\s*$', str(h['fout'])) and re.search(r'\b(\d+)\s+\w+\s*$', str(x['antwoord'])):      # Oef-#1057: dag terugtellen, richting per item
                _M = 'januari februari maart april mei juni juli augustus september oktober november december'.split()
                def _o(v):
                    m = re.search(r'\b(\d+)\s+(\w+)\s*$', str(v)); return (_M.index(m.group(2)) if m.group(2) in _M else 0) * 40 + int(m.group(1))      # maandgrens telt mee
                vd, ad = _o(h['fout']), _o(x['antwoord'])
                terug_ = 'teruggeteld' in t; ver_ = bool(re.search(r'te ver (terug)?geteld', t))
                if (ver_ and not ((vd < ad) if terug_ else (vd > ad))) or (not ver_ and not ((vd > ad) if terug_ else (vd < ad))):
                    F.append(f"richting-dag {DOEL} #{n} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {t.strip()[:60]}")
            continue      # klok: klokcheck; datum/terugtellen verder: geen getalrichting
        if DOEL == 'G5-VBN-E03' and n != 1: continue      # rijen die ook kunnen dalen (#2): 'te ver' gaat over stappen, niet over de waarde      # klokken: zie de klokcheck (12.40 → 1.40 is 'te ver')
        v = getal(h['fout']); so = h.get('soort') or ''
        if DOEL == 'G5-MEET-E06' and tijd(h['fout']) is not None and tijd(x['antwoord']) is not None:      # klok rond: 1.55 is later dan 12.55
            dt = (tijd(h['fout']) - tijd(x['antwoord'])) % 720; v, a = (1.0, 0.0) if 0 < dt < 360 else (-1.0, 0.0) if dt else (0.0, 0.0)
        else: a = getal(x['antwoord'])
        hi, lo = bool(HOOG.search(t)) or '(omhoog)' in so, bool(LAAG.search(t)) or '(omlaag)' in so
        if '(omlaag)' in so: hi = False
        if '(omhoog)' in so: lo = False
        if a is None or v is None or hi == lo: geen += 1; continue
        if MUT == 'M_richting' and n_r == 0: hi, lo = lo, hi      # mutant: de eerste nagekeken sleutel zegt de andere kant op
        n_r += 1
        if (hi and not v > a) or (lo and not v < a): F.append(f"richting {d} #{n} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): tekst zegt {'te veel' if hi else 'te weinig'}: {t.strip()[:70]}")
# Oef-#1056 (les 369): de bronzin en alle afgeleide velden van het item moeten meeveranderen; guard: geen bedrag of cijfer in 'nog … verder'
NOGV = re.compile(r'nog \S+ (?:\S+ )?(?:rij|rijen|stap|stappen|plek|plekken) verder|Ga na plek \d+')
if MUT == 'M_plek': next(x for x in I[('G5-VBN-E03', 2)] if x['id'].endswith('-003'))['foutHints'][-1]['uitleg'] = 'Je bent één plek te ver gegaan.'      # les 450-scan
if MUT == 'M_verder': I[('G5-VBN-E03', 2)][0]['foutHints'][-1]['uitleg'] = 'Ga nog 3 stappen verder.'
if DOEL == 'G5-VBN-E03':
    for x in I.get(('G5-VBN-E03', 2), []):
        s_ = json.dumps(x, ensure_ascii=False)
        if NOGV.search(s_): F.append(f"bronzin Oef-#1056 {x['id']}: {NOGV.search(s_).group(0)}")
        k_ = json.dumps({k: x.get(k) for k in ('foutHints', 'foutHintsTekst', 'foutRegels', 'algemeneFoutHint')}, ensure_ascii=False)      # kindteksten; extraVelden = herkomst (Oef-#1059)
        if BEDRAG.search(k_): F.append(f"weggever G5-VBN-E03 #2 {x['id']} (bron, les 450): {BEDRAG.search(k_).group(0)}")
# MEET-E03 #1: 'gekleurd' alleen als het kind echt kleurt (vraag, interactie, tekening)
if DOEL == 'G5-MEET-E03':
    if MUT == 'M_kleur': XS[0][1]['opgave'] = XS[0][1]['opgave'].replace('Kleur', 'Teken', 1)
    for (d, n), x in XS:
        kleurt = x['opgave'].startswith('Kleur') and 'aantikken' in str(x.get('ui')) and ((x.get('visual') or {}).get('jsRender') or {}).get('soort') == 'rooster'
        for h in x['foutHints']:
            if 'gekleurd' in (h.get('uitleg') or '') and not kleurt: F.append(f"kleuren MEET-E03 #1 {x['nr']} sleutel {h['fout']!r}: tekst zegt 'gekleurd' maar het kind kleurt niet")
# Oef-#1055 klok: een tekst die een wijzer fout noemt, noemt de wijzer die bij dat item echt fout is (kleine = ander uur, zelfde minuten; grote = zelfde uur)
def klok(x, f):
    vis = x.get('visual') or {}; jr = (vis.get('jsRender') or {}) if isinstance(vis, dict) else {}
    if jr.get('soort') == 'klokkenrij':
        L = jr.get('labels') or []; K = jr.get('klokken') or []
        def t(l): return (K[L.index(l)]['uur'] % 12, K[L.index(l)]['minuut']) if l in L else None
        return t(f), t(str(x['antwoord']).strip())
    def p(v):
        m = re.match(r'\s*(\d+)[.:](\d+)', str(v)); return (int(m.group(1)) % 12, int(m.group(2))) if m else None
    return p(f), p(x['antwoord'])
n_k = 0
if DOEL == 'G5-MEET-E06':
    if MUT == 'M_wijzer':
        x_, h_ = next((x, h) for _, x in XS for h in x['foutHints'] if 'kleine wijzer te' in (h.get('uitleg') or ''))
        h_['uitleg'] = h_['uitleg'].replace('de kleine wijzer te', 'de grote wijzer te').replace('De grote wijzer klopt wel', 'De kleine wijzer klopt wel')
    for (d, n), x in XS:
        for h in x['foutHints']:
            t = h.get('uitleg') or ''
            kl, gr = re.search(r'kleine wijzer (staat )?(te|niet|verkeerd)', t), re.search(r'grote wijzer (staat )?(te|niet|verkeerd)', t)
            if not (kl or gr): continue
            a_, b_ = klok(x, h['fout'])
            if a_ is None or b_ is None: F.append(f"klok {d} #{n} {x['nr']} sleutel {h['fout']!r}: tijd niet te lezen"); continue
            n_k += 1
            if kl and not (a_[0] != b_[0] and a_[1] == b_[1]): F.append(f"klok {d} #{n} {x['nr']} sleutel {h['fout']!r}: tekst noemt de kleine wijzer, maar {a_} vs {b_}")
            if gr and not (a_[0] == b_[0] and a_[1] != b_[1]): F.append(f"klok {d} #{n} {x['nr']} sleutel {h['fout']!r}: tekst noemt de grote wijzer, maar {a_} vs {b_}")
            if kl and re.search(r'te (ver|laat)', t) and (a_[0] - b_[0]) % 12 != 1: F.append(f"klok-richting {d} #{n} {x['nr']} sleutel {h['fout']!r}: te ver, maar {a_} vs {b_}")
            if kl and re.search(r'te vroeg', t) and (b_[0] - a_[0]) % 12 != 1: F.append(f"klok-richting {d} #{n} {x['nr']} sleutel {h['fout']!r}: te vroeg, maar {a_} vs {b_}")
# V-#1137: waar 'Bijna!' weg is, begint de tekst met een richting (entry én item; basis = groep5_voor van dezelfde zandbak)
RICHT0 = re.compile(r'^(Dat is (?:er )?te (?:veel|weinig|ver)|Dat zijn er te (?:veel|weinig)|Je bent (?:te ver|niet ver genoeg)|Je bent te vroeg)\b')
VOOR = os.path.join(B, 'groep5_voor')
n_b = 0
if os.path.isdir(VOOR):
    V0 = {}
    for p in sorted(glob.glob(os.path.join(VOOR, 'hints', 'batch*.json'))):
        for s in json.load(open(p, encoding='utf-8'))['somtypen']:
            for f in s['foutHints']: V0[(s['doel'], s['nrOrigineel'], f['soort'])] = f.get('tekst') or ''
    if MUT == 'M_bijna':
        f_ = next(f for s in ENT for f in s['foutHints'] if (V0.get((s['doel'], s['nrOrigineel'], f['soort'])) or V0.get((s['doel'], s['nrOrigineel'], 'bijna')) or '').startswith('Bijna!'))
        f_['tekst'] = RICHT0.sub('', f_['tekst']).lstrip('. ') or 'Reken het na.'
    for s in ENT:
        for f in s['foutHints']:
            b0 = V0.get((s['doel'], s['nrOrigineel'], f['soort']))
            if b0 is None and f['soort'] in ('één te veel', 'één te weinig'): b0 = V0.get((s['doel'], s['nrOrigineel'], 'bijna'))
            if not (b0 or '').startswith('Bijna!') or (f.get('tekst') or '').startswith('Bijna!'): continue
            n_b += 1
            if not RICHT0.search(f.get('tekst') or ''): F.append(f"bijna-zonder-richting {DOEL} #{s['nrOrigineel']} {f['soort']!r}: {(f.get('tekst') or '')[:70]}")
    if MUT == 'M_bijnaI':
        h_ = next(h for (d, n), x in XS for h in x['foutHints'] if (V0.get((d, n, h.get('soort'))) or V0.get((d, n, 'bijna')) or '').startswith('Bijna!') and h.get('soort') != 'bijna'); h_['uitleg'] = RICHT0.sub('', h_['uitleg']).lstrip('. ')
    for (d, n), x in XS:
        for h in x['foutHints']:
            so = h.get('soort') or ''; b0 = V0.get((d, n, so))
            if b0 is None and so in ('één te veel', 'één te weinig'): b0 = V0.get((d, n, 'bijna'))
            if not (b0 or '').startswith('Bijna!') or (h.get('uitleg') or '').startswith('Bijna!'): continue
            n_b += 1
            if not RICHT0.search(h.get('uitleg') or ''): F.append(f"bijna-zonder-richting {d} #{n} {x['nr']} sleutel {h['fout']!r}: {(h.get('uitleg') or '')[:70]}")
# V-#1136: geen kapotte woorden: elk woord in de kindteksten van dit somtype staat in de woordenlijst (basis-G5 + vervangzinnen)
WRD = re.compile(r"[A-Za-zÀ-ÿ]+")
WL = set()
if os.path.isdir(VOOR):
    for p in glob.glob(os.path.join(VOOR, 'hints', 'batch*.json')) + glob.glob(os.path.join(VOOR, 'data', 'per_doel', '*.json')):
        WL |= {w.lower() for w in WRD.findall(open(p, encoding='utf-8').read())}
    WL |= {w.lower() for a, b in REGELS if isinstance(b, str) for w in WRD.findall(b)} | {w.lower() for v in MEERV.values() for w in [v]}
if MUT == 'M_woord': next(f for s in ENT for f in s['foutHints'] if f.get('tekst'))['tekst'] += ' Tel de kantn nog eens.'
n_w = 0
if WL:
    for s in ENT:
        for f in [s] + s['foutHints']:
            for v in (('hint1', 'hint2') if f is s else ('tekst', 'tekstSterker')):
                for w in WRD.findall(f.get(v) or ''):
                    n_w += 1
                    if w.lower() not in WL or w.lower() == 'kantn': F.append(f"woord {DOEL} #{s['nrOrigineel']} {f.get('soort', '-')!r} [{v}]: {w!r} niet in de woordenlijst")
    for _, x in XS:
        for h in x['foutHints']:
            for w in WRD.findall((h.get('uitleg') or '') + ' ' + (h.get('uitlegSterker') or '')):
                if w.lower() not in WL or w.lower() == 'kantn': F.append(f"woord {DOEL} {x['nr']} sleutel {h['fout']!r}: {w!r} niet in de woordenlijst"); break
# V-#1139 / les 455: 'nog een/één … nodig' zit in BEDRAG (guard hierboven); mutant zet de oude zin terug
# Didactiek 17:35 (Oef-#1050 op de 'met'-sleutels): geen lenen/onthouden-fouttekst noemt een bedrag (GET-E05 #7 leenH: 'Dat is te veel.' + rest)
LEENW = re.compile(r'geleend|lenen|leen|onthoud|onthouden|over een heel (honderdtal|tiental)', re.I)
n_l = 0
if MUT == 'M_leenH' and DOEL == 'G5-GET-E05':
    h_ = next(h for x in I[('G5-GET-E05', 7)] for h in x['foutHints'] if 'geleend' in (h.get('soort') or '')); h_['uitleg'] = 'Dat is één honderdtal te veel. ' + h_['uitleg'].replace('Dat is te veel. ', '', 1)
for (d, n), x in XS:
    for h in x['foutHints']:
        t = ' '.join(h.get(v) or '' for v in ('uitleg', 'uitlegSterker'))
        if LEENW.search(t + ' ' + (h.get('soort') or '') + ' ' + str(h.get('regel'))):
            n_l += 1
            if guard(t): F.append(f"leen-bedrag {d} #{n} {x['nr']} sleutel {h['fout']!r} ({h.get('soort')}): {t.strip()[:70]}")
snap = {f"{s['doel']}#{s['nrOrigineel']} {f['soort']}": [f.get('tekst'), f.get('tekstSterker')] for s in ENT for f in s['foutHints']
        if any(re.search(r'\bte (veel|weinig|ver)\b|niet ver genoeg|dubbel|moet mee|boven het totaal|rondes', f.get(v) or '') for v in ('tekst', 'tekstSterker'))}
if os.environ.get('SNAP') == '1': os.makedirs(os.path.dirname(SNAPF), exist_ok=True); json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1091 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)][:20]
print(f"INFO {DOEL}: {len(ENT)} entries, {len(XS)} items; richting nagekeken bij {n_r} sleutels, {geen} zonder eenduidig richtingwoord/getal; SNAP {len(snap)} regels; leen/onthoud-teksten {n_l}; bijna→richting {n_b}; woorden {n_w}" + (f'; klok nagekeken bij {n_k} sleutels' if DOEL == 'G5-MEET-E06' else ''))
for f in F[:30]: print('FAIL', f)
print(f"check Z-#1091 {DOEL}: FAIL {len(F)}" + (f' (MUT={MUT})' if MUT else ''))
