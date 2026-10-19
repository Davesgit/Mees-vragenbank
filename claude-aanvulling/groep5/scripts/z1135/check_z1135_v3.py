#!/usr/bin/env python3
"""Check Z-#1135 v3 (r23, na V-#1150: laag 1 van de 9 maatvraag-entries is alleen richting + vraag + «Reken daarmee opnieuw.»; alleen de snap is nieuw (snap_z1135_v3.json), de toetsen en aantallen zijn gelijk aan v2. v2: (r22, na Z-#1147: kijkzin «Hoeveel … gaan er in één …?»; «gaan er in» = FAIL oud; snap_z1135_v3.json). Basis r20-versie ( ook de Z-#1146-kijkzin «Hoeveel <kleine maat> gaan er in één <grote maat>?»; mutanten M_eenheid/M_volgorde op die vorm). [MUT=..] [SNAP=1] python3 check_z1135.py <basis>   (zandbak of repo-snapshot)
- geen 'nul te veel' (ook 'een nul te veel weggehaald') in entry- en itemteksten van GET-E07, MEET-E01, MEET-E04, MEET-E05;
- per item: 'te groot'/'te veel' ⇔ sleutel > antwoord, 'te klein'/'te weinig' ⇔ sleutel < antwoord (soorten 'nul te veel', 'nul vergeten', GET-E07 'te veel');
- eenheden: de twee maten in de kijkzin staan als afkorting in de opgave van dat item, in de goede volgorde (van → naar);
- 'nul vergeten' met «er mist een nul» blijft zoals hij was (vergeleken met SNAP_VERGETEN); SNAP van de gewijzigde soorten. Altijd FAIL N (totaal)."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1090', 'r4')]
from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
DOELEN = ('G5-GET-E07', 'G5-MEET-E01', 'G5-MEET-E04', 'G5-MEET-E05')
NUL = re.compile(r'\bnul te (?:veel|weinig)\b', re.I)
AFK = {'meter': 'm', 'centimeter': 'cm', 'millimeter': 'mm', 'kilometer': 'km', 'liter': 'L', 'milliliter': 'ml', 'kilogram': 'kg', 'gram': 'g'}
KIJK = re.compile(r'Hoeveel keer zo (klein|groot) is een (\w+) als een (\w+)\?')
KIJK2 = re.compile(r'Hoeveel (\w+) gaan er in één (\w+)\?')      # Z-#1146 (r20): «Hoeveel centimeter gaan er in één meter?»
ENT = [s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'] in DOELEN]
XS = [((d, n), x) for (d, n), xs in I.items() if d in DOELEN for x in xs]
GROOTTE = {'km': 1000000, 'm': 1000, 'cm': 10, 'mm': 1, 'L': 1000, 'ml': 1, 'kg': 1000, 'g': 1}
def num_f(e): return GROOTTE[e]
def num(v):
    m = re.fullmatch(r'\s*(\d{1,3}(?:\.\d{3})+|\d+)\s*(?:[a-zA-Z]+)?\s*', str(v)); return int(m.group(1).replace('.', '')) if m else None
if MUT == 'M_nul': f_ = next(f for s in ENT for f in s['foutHints'] if f['soort'] == 'nul te veel'); f_['tekst'] = 'Dat is te veel: er staat een nul te veel achter. ' + f_['tekst']
if MUT == 'M_richting': h_ = next(h for _, x in XS for h in x['foutHints'] if h['soort'] == 'nul te veel' and 'te groot' in h['uitleg']); h_['uitleg'] = h_['uitleg'].replace('te groot', 'te klein', 1)
if MUT == 'M_eenheid': h_ = next(h for (k, x) in XS if k[0] == 'G5-MEET-E01' for h in x['foutHints'] if 'Hoeveel centimeter gaan er in één meter?' in h['uitleg']); h_['uitleg'] = h_['uitleg'].replace('Hoeveel centimeter gaan', 'Hoeveel millimeter gaan')
if MUT == 'M_volgorde': h_ = next(h for (k, x) in XS if k == ('G5-MEET-E01', 1) for h in x['foutHints'] if 'Hoeveel centimeter gaan er in één meter?' in h['uitleg']); h_['uitleg'] = h_['uitleg'].replace('Hoeveel centimeter gaan er in één meter?', 'Hoeveel meter gaan er in één centimeter?')
if MUT == 'M_gaat': h_ = next(h for (k, x) in XS if k == ('G5-MEET-E05', 1) for h in x['foutHints'] if 'gaan er in' in h['uitleg']); h_['uitleg'] = h_['uitleg'].replace('gaan er in', 'gaat er in')
if MUT == 'M_vergeten': f_ = next(f for s in ENT for f in s['foutHints'] if f['soort'] == 'nul vergeten' and 'er mist een nul' in f['tekst']); f_['tekst'] = f_['tekst'].replace('er mist een nul', 'het is te klein')
for s in ENT:
    for f in [s] + s['foutHints']:
        for v in (('hint1', 'hint2') if f is s else ('tekst', 'tekstSterker')):
            if NUL.search(f.get(v) or ''): F.append(f"nul {s['doel']} #{s['nrOrigineel']} {f.get('soort', '-')!r} [{v}]: {(f.get(v) or '')[:70]}")
n_r = n_e = 0; geen_v = set()
for (d, n), x in XS:
    a = num(x['antwoord'])
    for h in x['foutHints']:
        t = (h.get('uitleg') or '') + ' ' + (h.get('uitlegSterker') or '')
        if NUL.search(t): F.append(f"nul {d} #{n} {x['nr']} sleutel {h['fout']!r}: {t.strip()[:70]}")
        if re.search(r'\bgaat er in\b', t): F.append(f"oud {d} #{n} {x['nr']} sleutel {h['fout']!r}: 'gaat er in' (Z-#1147: 'gaan er in')")
        if not (h['soort'] in ('nul te veel', 'nul vergeten') or (d == 'G5-GET-E07' and 'Tel de nullen in de som' in t)): continue
        v = num(h['fout']); hi = bool(re.search(r'\bte (groot|veel)\b', t)); lo = bool(re.search(r'\bte (klein|weinig)\b', t)) or 'er mist een nul' in t
        if hi == lo and h['soort'] == 'nul vergeten': geen_v.add(f'{d} #{n}'); continue      # buiten Z-#1135 (bv. GET-E07 #22 «Tel de nullen van het ronde getal goed mee.»)
        if a is None or v is None or hi == lo: F.append(f"richting {d} #{n} {x['nr']} sleutel {h['fout']!r}: geen eenduidige richting of getal"); continue
        n_r += 1
        if (hi and not v > a) or (lo and not v < a): F.append(f"richting {d} #{n} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {t.strip()[:60]}")
        m = KIJK.search(t); m2 = KIJK2.search(t)
        if m2:      # Z-#1146: kleine maat, grote maat; allebei als afkorting in de opgave, de grote groter dan de kleine
            n_e += 1; kl, gr = m2.groups(); toks = re.findall(r'\b(km|cm|mm|ml|kg|m|L|g)\b', x['opgave'])
            if kl not in AFK or gr not in AFK or sorted(toks[:2]) != sorted([AFK[kl], AFK[gr]]): F.append(f"eenheid {d} #{n} {x['nr']} sleutel {h['fout']!r}: '{kl} in één {gr}' past niet bij de opgave {x['opgave'][:40]!r}")
            elif not num_f(AFK[gr]) > num_f(AFK[kl]): F.append(f"eenheid {d} #{n} {x['nr']}: 'hoeveel {kl} in één {gr}' is omgekeerd")
        elif m:
            n_e += 1; r_, naar, van = m.groups(); toks = re.findall(r'\b(km|cm|mm|ml|kg|m|L|g)\b', x['opgave'])
            if naar not in AFK or van not in AFK or toks[:2] != [AFK[van], AFK[naar]]: F.append(f"eenheid {d} #{n} {x['nr']} sleutel {h['fout']!r}: '{van} → {naar}' past niet bij de opgave {x['opgave'][:40]!r}")
            elif r_ != ('klein' if num_f(AFK[van]) > num_f(AFK[naar]) else 'groot'): F.append(f"eenheid {d} #{n} {x['nr']}: 'zo {r_}' klopt niet voor {van} → {naar}")
        elif d != 'G5-GET-E07' and h['soort'] != 'nul vergeten': F.append(f"kijkzin {d} #{n} {x['nr']} sleutel {h['fout']!r}: geen 'Hoeveel keer zo … is een … als een …?'")
SNAPF = os.path.join(D_, 'snap_z1135_v3.json')
snap = {f"{s['doel']}#{s['nrOrigineel']} {f['soort']}": [f.get('tekst'), f.get('tekstSterker')] for s in ENT for f in s['foutHints'] if f['soort'] in ('nul te veel', 'nul vergeten') or (s['doel'] == 'G5-GET-E07' and f['soort'] == 'te veel')}
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0] + ' Kijk goed.', snap[k_][1]]
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1135 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1135 ontbreekt')
print(f"INFO Z-#1135: {len(ENT)} entries, {len(XS)} items; richting nagekeken bij {n_r} sleutels, eenheden bij {n_e}; SNAP {len(snap)} regels; 'nul vergeten' zonder richtingwoord (buiten Z-#1135): {sorted(geen_v)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1135: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
