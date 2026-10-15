#!/usr/bin/env python3
"""Z-#961 / les 360: generieke mutantenloper voor alle bN/runmut.sh.
Een mutant is pas 'ok' als er een NIEUWE FAIL-regel (t.o.v. de basis) komt die past op ZIJN verwachte melding (regex).
Verwachting: eerst bN/verwacht.tsv ('M_naam<TAB>regex'), anders de standaardtabel hieronder (op de naam). Geen verwachting = GEMIST.
Een crash (Traceback/Error) in de mutant = GEMIST (les 353).
Gebruik: python3 mutrun.py BDIR [--muts 'M_a M_b'] [--skip 'M_x M_y'] [--toon-alle] -- CHECK-ARGS…   (zonder --muts: ontdekt in check.py)"""
import os, re, subprocess, sys
a = sys.argv[1:]; i = a.index('--') if '--' in a else len(a); opts, cargs = a[:i], a[i + 1:]
BD = os.path.abspath(opts[0]); cargs = [os.path.abspath(x) if os.path.exists(x) else x for x in cargs]
def opt(n):
    return opts[opts.index(n) + 1].split() if n in opts else None
TOON = '--toon-alle' in opts
env0 = dict(os.environ, PYTHONDONTWRITEBYTECODE='1'); env0.pop('MUT', None); env0.pop('SNAP', None)
def draai(m=None):
    e = dict(env0); 
    if m: e['MUT'] = m
    r = subprocess.run([sys.executable, '-B', 'check.py', *cargs], cwd=BD, env=e, capture_output=True, text=True)
    return r.stdout + r.stderr
src = open(os.path.join(BD, 'check.py'), encoding='utf-8').read()
muts = opt('--muts') or sorted(set(re.findall(r"MUT == '(M_[A-Za-z0-9_]+)'", src)) | set(re.findall(r"'(M_[A-Za-z0-9_]+)': \((?:\(|\d)", src)) | set(re.findall(r"MUT in \(([^)]*)\)", src) and sum((re.findall(r"'(M_[A-Za-z0-9_]+)'", g) for g in re.findall(r"MUT in \(([^)]*)\)", src)), [])))
skip = set(opt('--skip') or [])
STANDAARD = [  # (naam-regex, verwachte-melding-regex): alleen generieke tekst-/structuurmutanten met een vaste guard
    (r'M_cijfer\d*$', r'cijfer'), (r'M_letter\d*$', r'optieletter'), (r'M_plek\d*$', r'plekwoord|les 193'), (r'M_zoveel$', r'(?i)zoveel'),
    (r'M_217[a-z]?$', r'les 217'), (r'M_231$', r'les 231'), (r'M_235[a-z]?$', r'les 235'), (r'M_ctx\d*$', r'les 147'),
    (r'M_moeilijk$', r'moeilijk woord'), (r'M_Bijna$', r"'Bijna'"), (r'M_woorden$', r'V-#764'), (r'M_L2$', r'geen laag 2'),
    (r'M_antw\d*$', r'(op|bij) het goede antwoord|= het antwoord'), (r'M_afl$', r'les 234'), (r'M_even$', r"'even veel'"), (r'M_hussel$', r'husselen'),
    (r'M_klokw$', r'les 262'), (r'M_onb$', r'heeft geen check'), (r'M_264[a-z0-9]*$', r'les 264'), (r'M_260[a-z]*$', r'les 260'),
    (r'M_824[a-z]*$', r'Z-#824'), (r'M_195$', r'les 195'), (r'M_306$', r'les 306'), (r'M_354$', r'les 354'),
]
V = {}
pv = os.path.join(BD, 'verwacht.tsv')
if os.path.exists(pv):
    for r_ in open(pv, encoding='utf-8'):
        if r_.strip() and not r_.startswith('#'): k_, v_ = r_.rstrip('\n').split('\t', 1); V[k_.strip()] = v_.strip()
def verwacht(m):
    if m in V: return V[m], 'tsv'
    for n_, v_ in STANDAARD:
        if re.match(n_, m): return v_, 'std'
    return None, None
basis = set(l for l in draai().splitlines() if l.startswith('FAIL'))
n = mis = 0; zonder = []
for m in muts:
    if m in skip: print(f'n.v.t. {m}'); continue
    n += 1; out = draai(m); rx, bron = verwacht(m)
    nieuw = sorted(set(l for l in out.splitlines() if l.startswith('FAIL')) - basis)
    if re.search(r'Traceback|Error\b', out): print(f'GEMIST {m}: crash: {[l for l in out.splitlines() if "Error" in l][-1:]}'); mis += 1; continue
    if not rx:
        print(f'GEMIST {m}: geen verwachting (verwacht.tsv); nieuw: {nieuw[:1]}'); mis += 1; zonder.append(m)
        if TOON:
            for l in nieuw: print('   ', l[:200])
        continue
    raak = [l for l in nieuw if re.search(rx, l)]
    if raak: print(f'ok {m} [{rx}]: {raak[0][:150]}')
    else: print(f'GEMIST {m}: verwacht /{rx}/, nieuw: {[l[:150] for l in nieuw[:2]]}'); mis += 1
    if TOON:
        for l in nieuw: print('   ', l[:200])
print(f'mutanten: {n}, gemist: {mis}' + (f' (zonder verwachting: {len(zonder)})' if zonder else ''))
sys.exit(1 if mis else 0)
