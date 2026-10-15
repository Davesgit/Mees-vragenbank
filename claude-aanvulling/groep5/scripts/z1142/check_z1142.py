#!/usr/bin/env python3
"""Check Z-#1142. [MUT=..] [SNAP=1] python3 check_z1142.py <basis>   (basis = zandbak of repo-snapshot met claude-aanvulling/groep5)
- motor: fout_regels kent '(sleutel hele euro)' (anders vallen de sleutels terug op de komma-tekst);
- GET-E06 #1/#2 per sleutel 'centen te …': sleutel zonder komma ⇔ soort '(10 cent, hele euro)' ⇔ tekst «Kijk goed naar de centen: die mis je nog.»;
  nooit «achter de komma» bij een sleutel zonder komma; richting: te veel ⇔ sleutel > antwoord;
- SNAP van de zes centen-soorten. Drukt altijd het TOTAAL aantal FAIL af (V-#1141)."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1090', 'r4')]
from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
motor = open(os.path.join(G, 'scripts', 'fout_regels.py'), encoding='utf-8').read()
if MUT == 'M_motor': motor = motor.replace('Z-#1142', 'Z-#0000')
if 'Z-#1142' not in motor or '(sleutel (hele euro|met centen)' not in motor: F.append('motor fout_regels.py zonder Z-#1142 (sleutel hele euro)')
def cent(v):
    m = re.fullmatch(r'\s*€?\s*(\d+)(?:,(\d{1,2}))?\s*', str(v)); return int(m.group(1)) * 100 + int((m.group(2) or '0').ljust(2, '0')) if m else None
X = [(k, x) for k in (('G5-GET-E06', 1), ('G5-GET-E06', 2)) for x in I.get(k, [])]
H = [(k, x, h) for k, x in X for h in x['foutHints'] if h['soort'].startswith('centen te')]
if MUT == 'M_komma': h_ = next(h for _, _, h in H if ',' not in h['fout']); h_['uitleg'] = h_['uitleg'].replace('Kijk goed naar de centen: die mis je nog.', 'Kijk goed naar het eerste cijfer achter de komma: reken de centen nog eens na.')
if MUT == 'M_heel': h_ = next(h for _, _, h in H if ',' in h['fout'] and '(10 cent)' in h['soort']); h_['soort'] = h_['soort'][:-1] + ', hele euro)'
if MUT == 'M_richting': h_ = next(h for _, _, h in H if ',' not in h['fout'] and 'te veel' in h['uitleg']); h_['uitleg'] = h_['uitleg'].replace('te veel', 'te weinig', 1)
heel = n = 0
for (d, nr), x, h in H:
    n += 1; t = h.get('uitleg') or ''; zk = ',' not in h['fout']; heel += zk; a, v = cent(x['antwoord']), cent(h['fout'])
    if zk != h['soort'].endswith('hele euro)'): F.append(f"soort {d} #{nr} {x['nr']} sleutel {h['fout']!r}: {h['soort']!r}")
    if zk and ('achter de komma' in t or 'die mis je nog' not in t): F.append(f"komma {d} #{nr} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {t[:70]}")
    if not zk and 'die mis je nog' in t: F.append(f"heel {d} #{nr} {x['nr']} sleutel {h['fout']!r}: {t[:70]}")
    if a is None or v is None or not ((t.startswith('Dat is te veel') and v > a) or (t.startswith('Dat is te weinig') and v < a)): F.append(f"richting {d} #{nr} {x['nr']} sleutel {h['fout']!r} (antwoord {x['antwoord']}): {t[:50]}")
ENT = [s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'] == 'G5-GET-E06']
snap = {f"{s['doel']}#{s['nrOrigineel']} {f['soort']}": [f.get('regel'), f.get('tekst')] for s in ENT for f in s['foutHints'] if f['soort'].startswith('centen te')}
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0], snap[k_][1] + ' Kijk goed.']
SNAPF = os.path.join(D_, 'snap_z1142.json')
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1142 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1142 ontbreekt')
print(f"INFO Z-#1142: {len(X)} items, {n} centen-sleutels, waarvan {heel} zonder komma; SNAP {len(snap)} regels")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1142: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
