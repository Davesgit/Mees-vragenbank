#!/usr/bin/env python3
"""Check Z-#1148 (r22). [MUT=..] [SNAP=1] python3 check_z1148.py <basis> (na sync_hint_keys + apply_hints). Altijd FAIL N (totaal); exit 1 bij FAIL.
- geen G5-hint1 meer die met een feitzin begint («Eén meter (m) is …» / «Honderd centimeter (cm) is één meter (m).»);
- de 8 maatvraag-entries (MEET-E01 #1–#4, MEET-E04 #2/#4, MEET-E05 #1/#3): hint1 = precies «Hoeveel <klein> gaan er in één <groot>?»;
- per item van die somtypen: hint = die vraag; beide maten als afkorting in de opgave, de grote groter; sterkereHint bevat het FEIT (Eén groot is N klein,
  of N klein is één groot, met de juiste N) én de METHODE in de richting van de opgave (groot → klein: 'keer N' + 'zet er z nullen achter';
  klein → groot: 'door N' + 'haal er z nullen af'; z = aantal nullen van N); SNAP van hint/sterkereHint per item en hint1/hint2 per entry."""
import glob, json, os, re, sys, collections, math
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import g5, items
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
MAAT = {'kilometer': ('l', 1000000, 'km'), 'meter': ('l', 1000, 'm'), 'centimeter': ('l', 10, 'cm'), 'millimeter': ('l', 1, 'mm'), 'liter': ('v', 1000, 'L'), 'milliliter': ('v', 1, 'ml'), 'kilogram': ('m', 1000, 'kg'), 'gram': ('m', 1, 'g')}
TAL = {10: 'tien', 100: 'honderd', 1000: 'duizend'}; NUL = {1: 'één', 2: 'twee', 3: 'drie'}; AFK = {v[2]: k for k, v in MAAT.items()}
DOEL = {('G5-MEET-E01', 1), ('G5-MEET-E01', 2), ('G5-MEET-E01', 3), ('G5-MEET-E01', 4), ('G5-MEET-E04', 2), ('G5-MEET-E04', 4), ('G5-MEET-E05', 1), ('G5-MEET-E05', 3)}
FEIT1 = re.compile(r'^(?:Eén|Een|Tien|Honderd|Duizend) \w+ \(\w+\) is ', re.I); VR = re.compile(r'^Hoeveel (\w+) gaan er in één (\w+)\?$')
ENT = {(s['doel'], s['nrOrigineel']): s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'].startswith('G5-')}
X = {k: sorted(I.get(k, []), key=lambda x: x['nr']) for k in DOEL}
if MUT == 'M_entry': ENT[('G5-MEET-E05', 1)]['hint1'] = 'Eén kilogram (kg) is duizend gram (g). Hoeveel kilogram zijn het?'
if MUT == 'M_feit_h1': X[('G5-MEET-E01', 1)][0]['hint'] = 'Eén meter (m) is honderd centimeter (cm). ' + X[('G5-MEET-E01', 1)][0]['hint']
if MUT == 'M_vraag': X[('G5-MEET-E04', 2)][0]['hint'] = 'Hoeveel gram gaan er in één kilogram?'
if MUT == 'M_omgekeerd': X[('G5-MEET-E01', 3)][0]['hint'] = 'Hoeveel kilometer gaan er in één meter?'
if MUT == 'M_feit_weg': x_ = X[('G5-MEET-E01', 2)][0]; x_['sterkereHint'] = re.sub(r'^[^.]*\(\w+\) is één \w+ \(\w+\)\.\s*', '', x_['sterkereHint'])
if MUT == 'M_feit_getal': x_ = X[('G5-MEET-E01', 4)][0]; x_['sterkereHint'] = x_['sterkereHint'].replace('is duizend millimeter', 'is honderd millimeter', 1)
if MUT == 'M_methode': x_ = X[('G5-MEET-E05', 3)][0]; x_['sterkereHint'] = x_['sterkereHint'].replace('keer duizend', 'door duizend')
if MUT == 'M_nullen': x_ = X[('G5-MEET-E04', 4)][0]; x_['sterkereHint'] = x_['sterkereHint'].replace('drie nullen', 'twee nullen')
for k, s in sorted(ENT.items()):
    if FEIT1.match(s.get('hint1') or ''): F.append(f"entry {k[0]} #{k[1]}: hint1 begint nog met een feitzin: {s['hint1'][:60]}")
    if k in DOEL and not VR.match(s.get('hint1') or ''): F.append(f"entry {k[0]} #{k[1]}: hint1 is niet alleen «Hoeveel … gaan er in één …?»: {s.get('hint1', '')[:60]}")
n = collections.Counter(); snap = {}
for k in sorted(DOEL):
    if not X[k]: F.append(f"items {k[0]} #{k[1]}: geen"); continue
    for x in X[k]:
        pl = f"{k[0]} #{k[1]} {x['nr']}"; h, sh = x.get('hint') or '', x.get('sterkereHint') or ''; n[k] += 1
        snap[pl] = [h, sh]; m = VR.match(h); toks = re.findall(r'\b(km|cm|mm|ml|kg|m|L|g)\b', x['opgave'])
        if FEIT1.match(h) or not m: F.append(f"hint {pl}: niet alleen de vraag: {h[:70]}"); continue
        kl, gr = m.groups()
        if kl not in MAAT or gr not in MAAT or MAAT[kl][0] != MAAT[gr][0] or len(toks) < 2 or sorted(toks[:2]) != sorted([MAAT[kl][2], MAAT[gr][2]]): F.append(f"maat {pl}: '{kl} in één {gr}' past niet bij {x['opgave'][:40]!r}"); continue
        if not MAAT[gr][1] > MAAT[kl][1]: F.append(f"omgekeerd {pl}: 'hoeveel {kl} in één {gr}'"); continue
        N = MAAT[gr][1] // MAAT[kl][1]; z = round(math.log10(N)); tal = TAL[N]
        feit = re.search(rf'(?:Eén {gr} \({MAAT[gr][2]}\) is {tal} {kl} \({MAAT[kl][2]}\)|{tal.capitalize()} {kl} \({MAAT[kl][2]}\) is één {gr} \({MAAT[gr][2]}\))\.', sh)
        if not feit: F.append(f"feit {pl}: geen «Eén {gr} ({MAAT[gr][2]}) is {tal} {kl} ({MAAT[kl][2]}).» in de sterkere hint: {sh[:70]}")
        groot_naar_klein = toks[0] == MAAT[gr][2]
        meth = (rf'keer {tal}\b', rf'zet er {NUL[z]} nullen achter') if groot_naar_klein else (rf'door {tal}\b', rf'haal er {NUL[z]} nullen af')
        if not all(re.search(p, sh) for p in meth): F.append(f"methode {pl}: verwacht {' + '.join(meth)} ({toks[0]} → {toks[1]}): {sh[:80]}")
for k in sorted(DOEL): snap[f"entry {k[0]} #{k[1]}"] = [ENT.get(k, {}).get('hint1'), ENT.get(k, {}).get('hint2')]
SNAPF = os.path.join(D_, 'snap_z1148.json')
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0], snap[k_][1] + ' Kijk goed.']
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1148 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1148 ontbreekt')
print(f"INFO Z-#1148: {len(DOEL)} entries, {sum(n.values())} items ({', '.join(f'{k[0][3:]} #{k[1]} {v}' for k, v in sorted(n.items()))}); SNAP {len(snap)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1148: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
