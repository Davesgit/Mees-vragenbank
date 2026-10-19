#!/usr/bin/env python3
"""Check Z-#1121 [v1b (r22: tempfile i.p.v. vast tijdelijk pad; verder gelijk aan check_z1121.py 698c5008)]. [MUT=..] [SNAP=1] [APPLYLOG=pad] python3 check_z1121_v1b.py <basis>   (zandbak of repo-snapshot)
- GET-M03 #1 / MEET-E07 #1: geen letterlijke regel '€<getal>' meer; precies één entry 'aantal munten' / 'aantal stuks geld' met
  'fout = het aantal munten', vooraan, met de oude tekst;
- motor: de G5-motor leest 'fout = het aantal munten' bij elk item (niet None) en geeft €<aantal stuks in jsRender.munten>, of niets als dat het antwoord is;
- per item: die sleutel staat er precies als €<aantal> een optie is en niet het antwoord, met de soort en tekst van de entry; nergens anders;
- APPLYLOG (als gegeven): geen 'regel niet te lezen' voor GET-M03/MEET-E07; SNAP van alle foutHints van de twee somtypen. Altijd FAIL N (totaal)."""
import json, os, re, sys, glob, importlib.util
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1090', 'r4')]
from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
DOEL = {('G5-GET-M03', 1): 'aantal munten', ('G5-MEET-E07', 1): 'aantal stuks geld'}
TEKST = {'aantal munten': 'Je hebt de munten geteld. De vraag is hoeveel geld het samen is. Kijk wat elke munt waard is.',
         'aantal stuks geld': 'Je hebt geteld hoeveel stukken geld er zijn. De vraag is hoeveel geld het samen is. Kijk wat elk stuk waard is.'}
REGEL = 'fout = het aantal munten'
mt = open(os.path.join(G, 'scripts', 'fout_regels.py'), encoding='utf-8').read()
if MUT == 'M_motor': mt = re.sub(r"    # Z-#1121:.*?\n(?=    # getallen\n)", '', mt, flags=re.S)
import tempfile as _tf; _fd, P_ = _tf.mkstemp(prefix=f"fout_regels_z1121_{os.getpid()}_", suffix='.py'); os.close(_fd); open(P_, 'w', encoding='utf-8').write(mt)      # r22: tempfile (TMPDIR) i.p.v. een vast pad
sys.path.insert(0, os.path.join(G, 'scripts')); sp = importlib.util.spec_from_file_location('fr_z1121', P_); FR = importlib.util.module_from_spec(sp); sp.loader.exec_module(FR); os.remove(P_)
ENT = {(s['doel'], s['nrOrigineel']): s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if (s['doel'], s['nrOrigineel']) in DOEL}
if MUT == 'M_letterlijk': ENT[('G5-MEET-E07', 1)]['foutHints'][0]['regel'] = '€3'
if MUT == 'M_tekst': ENT[('G5-GET-M03', 1)]['foutHints'][0]['tekst'] += ' Tel ze.'
if MUT == 'M_teller':
    x_ = next(x for x in I[('G5-MEET-E07', 1)] if any(h['soort'] == 'aantal stuks geld' for h in x['foutHints']))
    h_ = next(h for h in x_['foutHints'] if h['soort'] == 'aantal stuks geld'); h_['fout'] = '€4' if h_['fout'] != '€4' else '€3'
if MUT == 'M_snap': next(h for h in I[('G5-GET-M03', 1)][0]['foutHints'])['uitleg'] += ' Kijk goed.'
for k, so in DOEL.items():
    s = ENT.get(k)
    if not s: F.append(f"entry {k[0]} #{k[1]} ontbreekt"); continue
    for f in s['foutHints']:
        if re.fullmatch(r'\s*€\s*\d+(?:,\d+)?\s*', f['regel']): F.append(f"letterlijk {k[0]} #{k[1]} {f['soort']!r}: regel {f['regel']!r}")
    e_ = [i for i, f in enumerate(s['foutHints']) if f['soort'].startswith('aantal')]
    if [(s['foutHints'][i]['soort'], s['foutHints'][i]['regel']) for i in e_] != [(so, REGEL)] or e_ != [0]: F.append(f"entry {k[0]} #{k[1]}: niet precies één {so!r} '{REGEL}' vooraan: {[s['foutHints'][i]['soort'] for i in e_]}")
    elif s['foutHints'][0]['tekst'] != TEKST[so]: F.append(f"tekst {k[0]} #{k[1]} {so!r}: {s['foutHints'][0]['tekst'][:60]}")
n_k = n_i = 0
for k, so in DOEL.items():
    for x in I.get(k, []):
        n_i += 1; mu = ((x.get('visual') or {}).get('jsRender') or {}).get('munten') or []; w = f'€{len(mu)}'
        r = FR.compile_regel(REGEL, FR.Ctx(x))
        if r is None: F.append(f"motor {k[0]} {x['nr']}: '{REGEL}' niet te lezen"); continue
        verw = set() if FR.geld_norm(w) == FR.geld_norm(x['antwoord']) else {w}
        if set(r.get('exact') or ()) != verw: F.append(f"motor {k[0]} {x['nr']}: {sorted(r.get('exact') or ())} ≠ {sorted(verw)} ({len(mu)} stuks, antwoord {x['antwoord']})")
        opt = {o['tekst'] for o in x.get('opties') or []}; moet = w in opt and verw == {w}
        hs = [h for h in x['foutHints'] if h['soort'].startswith('aantal')]
        if moet: n_k += 1
        if [h['fout'] for h in hs] != ([w] if moet else []): F.append(f"item {k[0]} {x['nr']} ({len(mu)} stuks, antwoord {x['antwoord']}): {[h['fout'] for h in hs]} ≠ {[w] if moet else []}")
        for h in hs:
            if h['soort'] != so or h['uitleg'] != TEKST[so] or h['regel'] != REGEL: F.append(f"item {k[0]} {x['nr']} {h['fout']!r}: soort/tekst/regel {h['soort']!r} {h['regel']!r}")
AL = os.environ.get('APPLYLOG')
if AL:
    F += [f"applylog {l.strip()}" for l in open(AL, encoding='utf-8') if 'niet te lezen' in l and re.search(r'G5-(GET-M03|MEET-E07)\b', l)]
    if MUT == 'M_log': F.append("applylog LET OP regel niet te lezen in G5-MEET-E07: '€3' (mutant)")
SNAPF = os.path.join(D_, 'snap_z1121.json')
snap = {f"{k[0]}#{k[1]} {x['nr']}": [[h['fout'], h['soort'], h['uitleg'], h.get('uitlegSterker'), h['regel']] for h in x['foutHints']] for k in DOEL for x in I.get(k, [])}
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1121 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1121 ontbreekt')
print(f"INFO Z-#1121: {n_i} items (GET-M03 #1, MEET-E07 #1), motor nagekeken bij {n_i}, sleutel 'aantal' bij {n_k}; SNAP {len(snap)} items" + (f"; applylog {AL}" if AL else ''))
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1121: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
