#!/usr/bin/env python3
"""Check V-#1149 voor G8 (r23, laag; PATCH COPY). [MUT=..] APPLYLOG=<G8-apply-log> python3 check_g8_stempel.py <basis>
De G8-apply-log heeft precies één regel 'stempel V-#1149: hintsSyncOp=… commit=… batches=…'; hintsSyncOp = die in groep8/data/gemapt.json en in elk
per_doel-bestand; de batch-md5's = de md5's van de huidige groep8/hints/batch*.json. De wijzigtijd telt niet. Fout = FAIL + exit 1; instelling = exit 2.
Mutanten zetten de fout in de INVOER (tijdelijke kopieën): log zonder stempel, andere tijd, andere batch-md5, gewijzigde batch, per_doel met andere tijd."""
import glob, hashlib, json, os, re, shutil, sys, tempfile, atexit
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []
G = next((os.path.join(B, n) for n in ('claude-aanvulling/groep8', 'groep8', 'g8') if os.path.isdir(os.path.join(B, n))), None)
AL = os.environ.get('APPLYLOG')
if not G or not AL or not os.path.isfile(AL): print(f"FAIL instelling: basis met groep8 en APPLYLOG=<bestaand pad> nodig ({B}, {AL})"); sys.exit(2)
def tmpd(): d = tempfile.mkdtemp(prefix='v1149g8_'); atexit.register(shutil.rmtree, d, True); return d
LOG = open(AL, encoding='utf-8', errors='replace').read(); HD = os.path.join(G, 'hints'); PD = os.path.join(G, 'data', 'per_doel')
if MUT == 'M_weg': LOG = re.sub(r'^stempel V-#1149: .*\n', '', LOG, flags=re.M)
if MUT == 'M_tijd': LOG = re.sub(r'(hintsSyncOp=\S*?)(\d)(\+|Z| )', lambda m: m.group(1) + str((int(m.group(2)) + 1) % 10) + m.group(3), LOG, count=1)
if MUT == 'M_md5': LOG = re.sub(r'(batches=batch\d+\.json:)(\w)', lambda m: m.group(1) + ('0' if m.group(2) != '0' else '1'), LOG, count=1)
if MUT == 'M_batch':
    HD = os.path.join(tmpd(), 'hints'); shutil.copytree(os.path.join(G, 'hints'), HD); p = sorted(glob.glob(os.path.join(HD, 'batch*.json')))[0]; open(p, 'a').write('\n')
if MUT == 'M_perdoel':
    PD = os.path.join(tmpd(), 'per_doel'); shutil.copytree(os.path.join(G, 'data', 'per_doel'), PD); p = sorted(glob.glob(os.path.join(PD, '*.json')))[0]
    d = json.load(open(p, encoding='utf-8')); d['hintsSyncOp'] = '2099-01-01T00:00:00+02:00'; json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
st = re.findall(r'^stempel V-#1149: hintsSyncOp=(\S+) commit=(\S+) batches=(\S+)$', LOG, re.M)
if len(st) != 1: F.append(f"stempel: {len(st)} stempelregels in de G8-apply-log (verwacht 1)")
else:
    op, commit, bs = st[0]; SB = dict(x.split(':', 1) for x in bs.split(','))
    gm = json.load(open(os.path.join(G, 'data', 'gemapt.json'), encoding='utf-8')).get('hintsSyncOp')
    if op != gm: F.append(f"stempel: hintsSyncOp {op} ≠ data/gemapt.json {gm}")
    for p in sorted(glob.glob(os.path.join(PD, '*.json'))):
        v = json.load(open(p, encoding='utf-8')).get('hintsSyncOp')
        if v is not None and v != op: F.append(f"stempel: hintsSyncOp {op} ≠ per_doel/{os.path.basename(p)} {v}")
    NU = {os.path.basename(p): hashlib.md5(open(p, 'rb').read()).hexdigest()[:12] for p in sorted(glob.glob(os.path.join(HD, 'batch*.json')))}
    for b in sorted(set(SB) | set(NU)):
        if SB.get(b) != NU.get(b): F.append(f"stempel: hints/{b} stempel {SB.get(b)}, nu {NU.get(b)}")
    print(f"INFO V-#1149 G8: hintsSyncOp={op} commit={commit}, {len(SB)} batches")
for f in F[:20]: print('FAIL', f)
print(f"check V-#1149 G8: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
