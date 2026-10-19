#!/usr/bin/env python3
"""Check Z-#1092 op een G5-kopie (379fab1 + r2 + zet_z1092, sync + apply). [MUT=..] [SNAP=1] python3 check_z1092.py <basis>
Guard (G5-zuster van M_1036c, les 193): geen plekwoord voor een getal ('het eerste/tweede getal', 'van het eerste af', …) in een G5-tekst die geen
vaste volgorde heeft (niet MEET-E06, VBN-E03, rooster M05 #5 / MEET-E03 #1): entry hint1/hint2/tekst/tekstSterker en item uitleg/uitlegSterker.
Rol per item: staat er 'het grootste/kleinste getal' (of bedrag), dan verschillen de twee getallen van dat item en is bij min/gedeeld het eerste het
grootste; 'het getal dat er al staat' alleen bij een aanvulsom. SNAP per item (snap_z1092.json): soort som, de twee getallen, de rolzinnen."""
import json, os, re, sys, glob
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D_); sys.path.insert(0, os.path.join(D_, '..', 'r4'))
from plek_lib import *; from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); G = g5(B); I = items(G); F = []; SNAPF = os.path.join(D_, 'snap_z1092.json')
ENT = {}
for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    for s in json.load(open(p, encoding='utf-8'))['somtypen']: ENT[(s['doel'], s['nrOrigineel'])] = s
def uit(k): return k[0] in UIT or k in UIT_ENTRY
ROLW = re.compile(r'het aantal rijen|hoeveel hokjes er in één rij|het (grootste|kleinste)( ronde)? (getal|bedrag)|het getal dat er al staat|van het grootste af|het kleinste (?:naar|op|van)\b')
if MUT == 'M_1092c': next(k for x in I[('G5-GET-E05', 2)] for k in x['foutHints'])['uitleg'] = 'Kijk naar het eerste getal.'
if MUT == 'M_rooster': x_ = I[('G5-GET-M05', 5)][0]; x_['antwoord'] = re.sub(r'(\d+) rijen van (\d+)', r'\2 rijen van \1', x_['antwoord'])
if MUT == 'M_1052c': ENT[('G5-MEET-E03', 1)]['hint2'] += ' Het eerste getal is het aantal rijen.'
if MUT == 'M_entry': ENT[('G5-GET-E05', 3)]['hint1'] += ' Haal het tweede getal van het eerste af.'
if MUT == 'M_rol':   x_ = I[('G5-GET-E05', 3)][0]; n_ = getallen(x_['opgave']); x_['opgave'] = x_['opgave'].replace(str(n_[0]), '§').replace(str(n_[1]), str(n_[0])).replace('§', str(n_[1]))
if MUT == 'M_aanvul': ENT[('G5-GET-E05', 2)]['hint1'] += ' Begin bij het getal dat er al staat.'
if MUT == 'M_snap':  x_, k_, v_ = next((x, k, v) for xs in I.values() for x in xs for k in x['foutHints'] for v in ('uitleg', 'uitlegSterker') if ROLW.search(k.get(v) or '')); k_[v_] = ROLW.sub(lambda m: m.group(0).upper(), k_[v_], count=1)
n_e = n_i = 0; GEEN = []
for k_, s in ENT.items():
    if not k_[0].startswith('G5-') or uit(k_): continue
    for o, v in [(s, 'hint1'), (s, 'hint2')] + [(f, kk) for f in s['foutHints'] for kk in ('tekst', 'tekstSterker')]:
        t = o.get(v) or ''; n_e += 1
        if PLEK.search(t): F.append(f"les 193 G5 {k_[0]} #{k_[1]} [{o.get('soort', v)}|{v}]: plekwoord voor een getal: {t[:80]}")
        if k_ in ROOSTER and any(b_ in t for _, b_ in ROOSTER[k_]):      # Oef-#1052: rolzin rooster waar per item
            for x in I.get(k_, []):
                if not rooster_ok(k_, x): F.append(f"Oef-#1052 {k_[0]} #{k_[1]} {x['nr']}: rolzin rooster klopt niet met vraag/antwoord ({x['opgave'][:40]} → {x['antwoord']})")
            continue
        if ROLW.search(t):
            its = I.get(k_, [])
            if its and all(soort_item(x)[0] is None for x in its): GEEN.append(f'{k_[0]} #{k_[1]}'); its = []
            for x in its:
                so, n = soort_item(x)
                if 'getal dat er al staat' in t and so != 'aanvul': F.append(f"Z-#1092 {k_[0]} #{k_[1]} {x['nr']}: 'het getal dat er al staat' maar geen aanvulsom")
                if re.search(r'grootste|kleinste', t) and (so in (None, 'aanvul') or len(n) < 2 or n[0] == n[1] or (so in ('min', 'geldmin', 'gedeeld') and n[0] < n[1])):
                    F.append(f"Z-#1092 {k_[0]} #{k_[1]} {x['nr']}: rol 'grootste/kleinste' klopt niet ({so}, {n[:2]}): {t[:60]}")
snap = {}
for k_, xs in I.items():
    if not k_[0].startswith('G5-') or uit(k_): continue
    for x in xs:
        for k in x['foutHints']:
            for v in ('uitleg', 'uitlegSterker'):
                t = k.get(v) or ''; n_i += 1
                if PLEK.search(t): F.append(f"les 193 G5 {k_[0]} #{k_[1]} {x['nr']} sleutel {k['fout']!r} [{v}]: plekwoord voor een getal: {t[:80]}")
        rz = sorted({z for k in x['foutHints'] for v in ('uitleg', 'uitlegSterker') for z in re.split(r'(?<=[.?!])\s+', k.get(v) or '') if ROLW.search(z)})
        if rz: so, n = soort_item(x); snap[f"{k_[0]}#{k_[1]} {x['nr']}"] = [so, n[:2], rz]
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1092 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)][:20]
print(f"INFO rol niet na te rekenen (geen som uit de vraag te halen): {sorted(set(GEEN))}")
print(f"INFO {n_e} entryteksten en {n_i} itemteksten nagekeken; {len(snap)} items met een rolzin in de SNAP")
for f in F[:40]: print('FAIL', f)
print(f"check Z-#1092: FAIL {len(F)}" + (f' (MUT={MUT})' if MUT else ''))
