#!/usr/bin/env python3
"""Check Z-#1147 v3 (r23, na V-#1150: laag 1 van de 9 maatvraag-entries is alleen richting + vraag + «Reken daarmee opnieuw.»; alleen de snap is nieuw (snap_z1147_v3.json), de toetsen en aantallen zijn gelijk aan v2. v2: (r22, na Z-#1148: entry 9 → 17, md 9 → 17, item-hint 0 → 77, want hint1 van de 8 maatvragen is nu «Hoeveel … gaan er in één …?»; verder gelijk aan v1). [MUT=..] [SNAP=1] python3 check_z1147.py <basis> (na sync_hint_keys + apply_hints). Altijd FAIL N (totaal); exit 1 bij FAIL.
- nergens meer 'gaat er in' in G5: entries (alle kindvelden), items (data/per_doel en data/gemapt.json, elk tekstveld), somtypen/*.md;
- aantallen 'gaan er in één' in de vijf maatvragen: entry 9, items 384 (uitleg 149, foutHintsTekst 149, foutRegels 86), md 9;
- SNAP: per veld de tekst met 'gaan er in' + md5 van alle andere G5-tekstvelden (zo verandert er verder niets)."""
import glob, hashlib, json, os, re, sys, collections
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import g5
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B)
OUD = re.compile(r'\bgaat er in\b', re.I); NW = re.compile(r'Hoeveel (?:centimeter|millimeter|meter|milliliter|gram) gaan er in één (?:meter|kilometer|liter|kilogram)\?')
ENT = [(os.path.basename(p), s) for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen']]
PD = {os.path.basename(p): json.load(open(p, encoding='utf-8'))['items'] for p in sorted(glob.glob(os.path.join(G, 'data', 'per_doel', '*.json')))}
GM = json.load(open(os.path.join(G, 'data', 'gemapt.json'), encoding='utf-8'))['items']
MD = {os.path.basename(p): open(p, encoding='utf-8').read() for p in sorted(glob.glob(os.path.join(G, 'somtypen', '*.md')))}
# mutanten: de fout in de INVOER (de ingelezen data), nooit in de check zelf
def eerste(lst, veld='uitleg'):
    for x in lst:
        for h in x.get('foutHints') or []:
            if NW.search(h.get(veld) or ''): return h
if MUT == 'M_entry': f_ = next(f for _, s in ENT for f in s['foutHints'] if NW.search(f['tekst'])); f_['tekst'] = f_['tekst'].replace('gaan er in', 'gaat er in')
if MUT == 'M_item': h_ = eerste(PD['G5-MEET-E05.json']); h_['uitleg'] = h_['uitleg'].replace('gaan er in', 'gaat er in')
if MUT == 'M_gemapt': x_ = next(x for x in GM if NW.search(x.get('foutHintsTekst') or '')); x_['foutHintsTekst'] = x_['foutHintsTekst'].replace('gaan er in', 'gaat er in', 1)
if MUT == 'M_regel': r_ = next(r for x in GM for r in x.get('foutRegels') or [] if NW.search(r.get('tekst') or '')); r_['tekst'] = r_['tekst'].replace('gaan er in', 'gaat er in')
if MUT == 'M_md': k_ = next(k for k in MD if NW.search(MD[k])); MD[k_] = MD[k_].replace('gaan er in', 'gaat er in', 1)
if MUT == 'M_aantal': x_ = next(x for x in PD['G5-MEET-E01.json'] if any(NW.search(h.get('uitleg') or '') for h in x['foutHints'])); x_['foutHints'] = [h for h in x_['foutHints'] if not NW.search(h.get('uitleg') or '')]
if MUT == 'M_rest': x_ = next(x for x in PD['G5-GET-E02.json'] if x.get('hint')); x_['hint'] += ' Kijk goed.'
def strs(o, pad=''):
    if isinstance(o, dict):
        for k, v in sorted(o.items()): yield from strs(v, f'{pad}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from strs(v, f'{pad}[{i}]')
    elif isinstance(o, str): yield pad, o
KIND = ('hint1', 'hint2', 'ouderzin', 'algemeneFoutHint')
n = collections.Counter(); snap = {}; rest = hashlib.md5()
for b, s in ENT:
    for o, v, w in [(s, k, k) for k in KIND] + [(f, k, f"{f['soort']}|{f['regel']}|{k}") for f in s['foutHints'] for k in ('tekst', 'tekstSterker')]:
        t = o.get(v)
        if not isinstance(t, str): continue
        sl = f"entry {b} {s['doel']}#{s['nrOrigineel']} {w}"
        if OUD.search(t): F.append(f"oud {sl}: {t[:70]}")
        if NW.search(t): n['entry'] += len(NW.findall(t)); snap[sl] = t
        else: rest.update(f'{sl}\0{t}\0'.encode())
for naam, its in [(f'per_doel/{k}', v) for k, v in PD.items()] + [('gemapt', GM)]:
    for x in its:
        for p, t in strs(x):
            sl = f"{naam} {x['id']}{p}"
            if OUD.search(t): F.append(f"oud {sl}: {t[:70]}")
            if NW.search(t):
                c = len(NW.findall(t)); snap[sl] = t
                if naam == 'gemapt': n[re.sub(r'\[\d+\]', '[]', p).split('.')[1] if p.count('.') == 1 else re.sub(r'\[\d+\]', '[]', p)] += c
            elif naam != 'gemapt' and re.search(r'\.(hint|sterkereHint|uitleg|uitlegSterker|foutHintsTekst|ouderzin|opgave)$', p): rest.update(f'{sl}\0{t}\0'.encode())
for k, t in MD.items():
    if OUD.search(t): F.append(f"oud md {k}: {OUD.search(t).group(0)}")
    n['md'] += len(NW.findall(t))
VERW = {'entry': 17, 'md': 17, 'hint': 77, '.foutHints[].uitleg': 149, 'foutHintsTekst': 149, '.foutRegels[].tekst': 86}
for k in sorted(set(VERW) | set(n)):
    if n[k] != VERW.get(k, 0): F.append(f"aantal {k}: {n[k]} keer 'gaan er in één', verwacht {VERW.get(k, 0)}")
snap['rest (md5 van de andere tekstvelden)'] = rest.hexdigest()
SNAPF = os.path.join(D_, 'snap_z1147_v3.json')
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] += ' Kijk goed.'
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1147 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1147 ontbreekt')
print(f"INFO Z-#1147: entry {n['entry']}, md {n['md']}, gemapt {n['.foutHints[].uitleg'] + n['foutHintsTekst'] + n['.foutRegels[].tekst']} ('gaan er in één'); SNAP {len(snap)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1147: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
