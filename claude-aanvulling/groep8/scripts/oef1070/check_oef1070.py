#!/usr/bin/env python3
"""Check Oef-#1070 (G8). [MUT=..] [SNAP=1] python3 check_oef1070.py <basis>   (zandbak of repo-snapshot). Altijd FAIL N (totaal); exit 1 bij FAIL.
- G8-GET-M01 / G8-MEET-E03: geen 'tien keer te veel/weinig', geen 'er staat een nul te veel' / 'er mist een nul' meer (entry-tekst en item-uitleg);
- per item: «Dat is tien keer te groot.» alleen als sleutel = antwoord × 10, «… te klein.» alleen als sleutel × 10 = antwoord; aantallen 48 / 64;
- guard afgekapt: een sleutel die geen precieze factor tien is (256 → 25, 32 → 3, 128 → 12, 64 → 6) noemt nooit 'tien keer' (Oef-#1070-uitzondering);
- 'duizend keer te weinig' (GET-M01, 7 sleutels) ongewijzigd; SNAP van alle foutHints van de twee doelen (snap_oef1070.json)."""
import json, os, re, sys
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D_); from g8pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g8(B); I = items(G)
DOEL = ('G8-GET-M01', 'G8-MEET-E03'); VERW = {'G8-GET-M01': 48, 'G8-MEET-E03': 64}
OUD = re.compile(r'tien keer te (?:veel|weinig)|er staat een nul te veel|er mist een nul', re.I)
GROOT, KLEIN = 'Dat is tien keer te groot.', 'Dat is tien keer te klein.'
DUIZEND = 'Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.'
def num(v):
    v = str(v).strip()
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', v): v = v.replace('.', '')
    if re.fullmatch(r'\d+(?:,\d+)?', v): return round(float(v.replace(',', '.')) * 1000)      # in duizendsten (kommagetal)
    return None
ENT = [s for _, s in entries(G) if s['doel'] in DOEL]
XS = [x for d in DOEL for x in I.get(d, [])]
def eerste(pred): return next(h for x in XS for h in x['foutHints'] if pred(x, h))
if MUT == 'M_veel': h_ = eerste(lambda x, h: h['uitleg'].startswith(GROOT)); h_['uitleg'] = h_['uitleg'].replace(GROOT, 'Dat is tien keer te veel.')
if MUT == 'M_entry': f_ = next(f for s in ENT for f in s['foutHints'] if f['tekst'].startswith(KLEIN)); f_['tekst'] = f_['tekst'].replace(KLEIN, 'Dat is tien keer te klein: er mist een nul.')
if MUT == 'M_richting': h_ = eerste(lambda x, h: h['uitleg'].startswith(KLEIN)); h_['uitleg'] = h_['uitleg'].replace(KLEIN, GROOT)
if MUT == 'M_afgekapt': h_ = eerste(lambda x, h: str(x['antwoord']) == '256' and h['fout'] == '25'); h_['uitleg'] = KLEIN + ' ' + h_['uitleg']
if MUT == 'M_duizend': h_ = eerste(lambda x, h: h['uitleg'].startswith('Dat is duizend keer')); h_['uitleg'] = h_['uitleg'].replace('duizend keer te weinig', 'duizend keer te klein')
if MUT == 'M_aantal': x_ = next(x for x in XS if x['doelId'] == 'G8-GET-M01'); x_['foutHints'] = [h for h in x_['foutHints'] if not h['uitleg'].startswith(GROOT)]
for s in ENT:
    for f in s['foutHints']:
        for v in ('tekst', 'tekstSterker'):
            if OUD.search(f.get(v) or ''): F.append(f"oud {s['doel']} #{s['nrOrigineel']} {f['soort']!r} [{v}]: {f[v][:70]}")
n = {d: 0 for d in DOEL}; afg = []; n_d = 0
for x in XS:
    a = num(x['antwoord'])
    for h in x['foutHints']:
        u = (h.get('uitleg') or '') + ' ' + (h.get('uitlegSterker') or ''); v = num(h['fout'])
        if OUD.search(u): F.append(f"oud {x['doelId']} {x['nr']} sleutel {h['fout']!r}: {u.strip()[:70]}")
        if a is not None and v is not None and v * 10 != a and v != a * 10 and v < a and 'nul te weinig' in h['soort']:
            afg.append(f"{x['antwoord']}→{h['fout']}")
            if 'tien keer' in u: F.append(f"afgekapt {x['doelId']} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): geen factor tien, toch 'tien keer': {u.strip()[:60]}")
        if h['uitleg'].startswith('Dat is duizend keer'):
            n_d += 1
            if h['uitleg'] != DUIZEND: F.append(f"duizend {x['doelId']} {x['nr']} sleutel {h['fout']!r}: {h['uitleg'][:70]}")
        if 'tien keer' not in u: continue
        if h['uitleg'].startswith(GROOT): ok = a is not None and v == a * 10
        elif h['uitleg'].startswith(KLEIN): ok = a is not None and v is not None and v * 10 == a
        else: F.append(f"vorm {x['doelId']} {x['nr']} sleutel {h['fout']!r}: 'tien keer' maar niet «{GROOT}»/«{KLEIN}»: {h['uitleg'][:60]}"); continue
        n[x['doelId']] += 1
        if not ok: F.append(f"richting {x['doelId']} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {h['uitleg'][:40]}")
for d in DOEL:
    if n[d] != VERW[d]: F.append(f"aantal {d}: {n[d]} sleutels met 'tien keer', verwacht {VERW[d]}")
if n_d != 7: F.append(f"duizend: {n_d} sleutels 'duizend keer te weinig', verwacht 7")
if sorted(afg) != sorted(['256→25', '32→3', '128→12', '64→6', '64→6']): F.append(f"afgekapt: lijst {sorted(afg)} ≠ de 5 bekende (256→25, 32→3, 128→12, 64→6 twee keer)")
SNAPF = os.path.join(D_, 'snap_oef1070.json')
snap = {f"{x['doelId']} {x['nr']}": [[h['fout'], h['soort'], h['uitleg'], h.get('uitlegSterker')] for h in x['foutHints']] for x in XS}
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = snap[k_][1:]
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Oef-#1070 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP Oef-#1070 ontbreekt')
print(f"INFO Oef-#1070: {len(XS)} items; 'tien keer' GET-M01 {n['G8-GET-M01']}, MEET-E03 {n['G8-MEET-E03']}; duizend {n_d}; afgekapt (geen 'tien keer') {sorted(afg)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Oef-#1070: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
