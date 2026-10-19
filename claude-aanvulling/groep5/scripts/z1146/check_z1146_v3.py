#!/usr/bin/env python3
"""Check Z-#1146 v3 (r22, na Z-#1148: entryregels 9 → 17, want hint1 van de 8 maatvragen is nu de vraag; verder gelijk aan v2. Na Z-#1147: «Hoeveel <maat> gaan er in één <maat>?»; «gaat er in» = FAIL oud; snap_z1146_v3.json). [MUT=..] [SNAP=1] python3 check_z1146.py <basis>. Altijd FAIL N (totaal); exit 1 bij FAIL.
- nergens in G5 (entry hint1/hint2/tekst/tekstSterker, item hint/sterkereHint/uitleg/uitlegSterker) nog «Hoeveel keer zo klein/groot is een <maat> als een <maat>?»;
- elke «Hoeveel <maat> gaan er in één <maat>?»: twee maten uit één reeks, de tweede groter; bij een item staan beide als afkorting in de opgave;
- aantallen: 9 entryregels, 149 itemsleutels (MEET-E01 #1 62, #2 13, #3 16, #4 16; MEET-E04 #2 16, #4 4; MEET-E05 #1 16, #3 6); SNAP per sleutel."""
import json, os, re, sys, glob, collections
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
MAAT = {'kilometer': ('l', 1000000, 'km'), 'meter': ('l', 1000, 'm'), 'centimeter': ('l', 10, 'cm'), 'millimeter': ('l', 1, 'mm'), 'liter': ('v', 1000, 'L'), 'milliliter': ('v', 1, 'ml'), 'kilogram': ('m', 1000, 'kg'), 'gram': ('m', 1, 'g')}
OUD = re.compile(r'[Hh]oeveel keer zo (?:klein|groot) is een (\w+) als een (\w+)\?'); NW = re.compile(r'Hoeveel (\w+) gaan er in één (\w+)\?')
VERW = {('G5-MEET-E01', 1): 62, ('G5-MEET-E01', 2): 13, ('G5-MEET-E01', 3): 16, ('G5-MEET-E01', 4): 16, ('G5-MEET-E04', 2): 16, ('G5-MEET-E04', 4): 4, ('G5-MEET-E05', 1): 16, ('G5-MEET-E05', 3): 6}
ENT = [s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen']]
def hz(k, f): return next(h for x in I[k] for h in x['foutHints'] if f in (h.get('uitleg') or ''))
if MUT == 'M_oud': h_ = hz(('G5-MEET-E05', 1), 'Hoeveel gram gaan er in één kilogram?'); h_['uitleg'] = h_['uitleg'].replace('Hoeveel gram gaan er in één kilogram?', 'Hoeveel keer zo klein is een gram als een kilogram?')
if MUT == 'M_entry': f_ = next(f for s in ENT if s['doel'] == 'G5-MEET-E01' and s['nrOrigineel'] == 2 for f in s['foutHints'] if 'gaan er in één' in f['tekst']); f_['tekst'] = f_['tekst'].replace('Hoeveel centimeter gaan er in één meter?', 'Hoeveel keer zo groot is een meter als een centimeter?')
if MUT == 'M_omgekeerd': h_ = hz(('G5-MEET-E01', 3), 'Hoeveel meter gaan er in één kilometer?'); h_['uitleg'] = h_['uitleg'].replace('Hoeveel meter gaan er in één kilometer?', 'Hoeveel kilometer gaan er in één meter?')
if MUT == 'M_opgave': h_ = hz(('G5-MEET-E04', 2), 'Hoeveel milliliter gaan er in één liter?'); h_['uitleg'] = h_['uitleg'].replace('Hoeveel milliliter gaan er in één liter?', 'Hoeveel gram gaan er in één kilogram?')
if MUT == 'M_gaat': h_ = hz(('G5-MEET-E01', 3), 'Hoeveel meter gaan er in één kilometer?'); h_['uitleg'] = h_['uitleg'].replace('gaan er in', 'gaat er in')
if MUT == 'M_aantal': x_ = I[('G5-MEET-E01', 2)][0]; x_['foutHints'] = [h for h in x_['foutHints'] if 'gaan er in één' not in (h.get('uitleg') or '')]
def zin(plek, t, opg=None):
    if OUD.search(t): F.append(f"oud {plek}: {OUD.search(t).group(0)}")
    if re.search(r'\bgaat er in\b', t): F.append(f"oud {plek}: 'gaat er in' (Z-#1147)")
    for m in NW.finditer(t):
        kl, gr = m.groups()
        if kl not in MAAT or gr not in MAAT or MAAT[kl][0] != MAAT[gr][0]: F.append(f"maat {plek}: {m.group(0)}"); continue
        if not MAAT[gr][1] > MAAT[kl][1]: F.append(f"omgekeerd {plek}: {m.group(0)}")
        if opg is not None:
            toks = set(re.findall(r'\b(km|cm|mm|ml|kg|m|L|g)\b', opg))
            if not {MAAT[kl][2], MAAT[gr][2]} <= toks: F.append(f"opgave {plek}: {m.group(0)} past niet bij {opg[:50]!r}")
    return len(NW.findall(t))
n_e = 0
for s in ENT:
    for o, v in [(s, 'hint1'), (s, 'hint2')] + [(f, k) for f in s['foutHints'] for k in ('tekst', 'tekstSterker')]:
        n_e += zin(f"{s['doel']} #{s['nrOrigineel']} {o.get('soort', '-')!r} [{v}]", o.get(v) or '')
n = collections.Counter(); snap = {}
for k, xs in I.items():
    for x in xs:
        for v in ('hint', 'sterkereHint', 'algemeneFoutHint'): zin(f"{k[0]} #{k[1]} {x['nr']} [{v}]", str(x.get(v) or ''), x['opgave'])
        for h in x['foutHints']:
            for v in ('uitleg', 'uitlegSterker'):
                c = zin(f"{k[0]} #{k[1]} {x['nr']} sleutel {h['fout']!r} [{v}]", h.get(v) or '', x['opgave'])
                if c: n[k] += 1; snap[f"{k[0]}#{k[1]} {x['nr']} {h['fout']}"] = [h['soort'], h[v]]
for k in sorted(set(VERW) | set(n)):
    if n[k] != VERW.get(k, 0): F.append(f"aantal {k[0]} #{k[1]}: {n[k]} sleutels met 'gaan er in één', verwacht {VERW.get(k, 0)}")
if n_e != 17: F.append(f"aantal entry: {n_e} entryregels met 'gaan er in één', verwacht 17")
SNAPF = os.path.join(D_, 'snap_z1146_v3.json')
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0], snap[k_][1] + ' Kijk goed.']
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1146 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1146 ontbreekt')
print(f"INFO Z-#1146: {n_e} entryregels, {sum(n.values())} itemsleutels met 'gaan er in één'; SNAP {len(snap)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1146: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
