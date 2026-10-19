#!/usr/bin/env python3
"""Check Z-#1121 [v3, r22 ronde 4 (V-#1149, les 460): vergelijkt op de STEMPEL in de apply-log i.p.v. op de wijzigtijd; ronde 1: tempfile i.p.v. vast
tijdelijk pad; verder gelijk aan check_z1121_v2.py e008af30], versie 2 (V-#1144, les 459). [MUT=..] [SNAP=1] APPLYLOG=pad python3 check_z1121_v3.py <basis>   (zandbak of repo-snapshot)
V-#1144: APPLYLOG is verplicht. Ontbreekt de variabele, bestaat het bestand niet, is het geen volledige apply_hints-uitvoer (de regels
'G5-GET-M03: … somtypen bijgewerkt', 'G5-MEET-E07: …', 'items: …', de stempelregel 'stempel V-#1149: …' en de slotregel 'ronde 10: …') of hoort de
stempel niet bij deze basis (V-#1149: hintsSyncOp ≠ die in data/gemapt.json, of de batch-md5's ≠ de md5's van de huidige hints/batch*.json; de
wijzigtijd telt NIET meer: de sync schrijft de batches bij elke build opnieuw, git archive/checkout zet nieuwe tijden),
dan: FAIL applylog …, 'check Z-#1121: FAIL 1 (totaal)' en exit 2; niets anders wordt nagekeken. Mutanten M_log* zetten de fout in de INVOER
(een tijdelijke kopie van de log met een fout erin, een leeg of afgekapt bestand, een pad dat niet bestaat, geen APPLYLOG); geen nep-FAIL in de uitvoer.
V-#1149: M_stempel_* zetten de fout ook in de invoer: een logkopie zonder stempel, met een andere hintsSyncOp of een andere batch-md5; M_batch_ander
leest een tijdelijke kopie van hints/ met één gewijzigde batch, M_data_ander een kopie van data/gemapt.json met een latere hintsSyncOp.
M_log_oud (log 115 dagen oud) en M_touch (kopie van hints/ met alle batches nu aangeraakt, inhoud gelijk) moeten juist SLAGEN (FAIL 0, exit 0).
- GET-M03 #1 / MEET-E07 #1: geen letterlijke regel '€<getal>' meer; precies één entry 'aantal munten' / 'aantal stuks geld' met
  'fout = het aantal munten', vooraan, met de oude tekst;
- motor: de G5-motor leest 'fout = het aantal munten' bij elk item (niet None) en geeft €<aantal stuks in jsRender.munten>, of niets als dat het antwoord is;
- per item: die sleutel staat er precies als €<aantal> een optie is en niet het antwoord, met de soort en tekst van de entry; nergens anders;
- APPLYLOG (verplicht): geen 'regel niet te lezen' voor GET-M03/MEET-E07; SNAP van alle foutHints van de twee somtypen. Altijd FAIL N (totaal)."""
import json, os, re, sys, glob, importlib.util
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(D_, '..', 'z1090', 'r4')]
from g5pad import *
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B)
import tempfile, time, atexit, shutil
def _tmpd(pre):      # r22 R4: tijdelijke mappen van de mutanten worden na afloop opgeruimd
    d = tempfile.mkdtemp(prefix=pre); atexit.register(shutil.rmtree, d, True); return d
def stop(r):
    print(f"FAIL applylog {r}"); print("check Z-#1121: FAIL 1 (totaal)" + (f' (MUT={MUT})' if MUT else '')); sys.exit(2)
AL = os.environ.get('APPLYLOG') if MUT != 'M_geenlog' else None
if AL and MUT.startswith('M_log'):      # V-#1144: de fout in de invoer: een tijdelijke kopie (of een pad dat niet bestaat)
    src = open(AL, encoding='utf-8').read() if os.path.isfile(AL) else ''
    tmp = os.path.join(_tmpd('v1144_'), 'apply.log')
    if MUT == 'M_log': open(tmp, 'w', encoding='utf-8').write(src.replace('\nitems: ', "\nLET OP regel niet te lezen in G5-MEET-E07: '€3' (143 items)\nitems: ", 1))
    elif MUT == 'M_log_leeg': open(tmp, 'w').close()
    elif MUT == 'M_log_kapot': open(tmp, 'w', encoding='utf-8').write(''.join(src.splitlines(True)[:3]))
    elif MUT == 'M_log_oud': open(tmp, 'w', encoding='utf-8').write(src); os.utime(tmp, (time.time() - 10 ** 7,) * 2)
    elif MUT == 'M_log_weg': tmp += '.weg'
    AL = tmp
if AL and MUT.startswith('M_stempel'):  # V-#1149: logkopie met een fout in de stempelregel
    src = open(AL, encoding='utf-8').read() if os.path.isfile(AL) else ''; tmp = os.path.join(_tmpd('v1149_'), 'apply.log')
    if MUT == 'M_stempel_weg': src = re.sub(r'^stempel V-#1149: .*\n', '', src, flags=re.M)
    elif MUT == 'M_stempel_tijd': src = re.sub(r'(hintsSyncOp=\S*?)(\d)(\+|Z| )', lambda m: m.group(1) + str((int(m.group(2)) + 1) % 10) + m.group(3), src, count=1)
    elif MUT == 'M_stempel_batch': src = re.sub(r'(batch6\.json:)(\w)', lambda m: m.group(1) + ('0' if m.group(2) != '0' else '1'), src, count=1)
    open(tmp, 'w', encoding='utf-8').write(src); AL = tmp
import shutil
HD = os.path.join(G, 'hints'); GM = os.path.join(G, 'data', 'gemapt.json')
if MUT in ('M_batch_ander', 'M_touch'):     # V-#1149: tijdelijke kopie van hints/ (de invoer), niet de basis zelf
    HD = os.path.join(_tmpd('v1149_'), 'hints'); shutil.copytree(os.path.join(G, 'hints'), HD)
    if MUT == 'M_batch_ander': open(os.path.join(HD, 'batch6.json'), 'a', encoding='utf-8').write('\n')
    else: [os.utime(p, None) for p in glob.glob(os.path.join(HD, 'batch*.json'))]
if MUT == 'M_data_ander':
    d_ = json.load(open(GM, encoding='utf-8')); d_['hintsSyncOp'] = '2099-01-01T00:00:00+02:00'
    GM = os.path.join(_tmpd('v1149_'), 'gemapt.json'); json.dump(d_, open(GM, 'w', encoding='utf-8'), ensure_ascii=False)
if not AL: stop("ontbreekt: zet APPLYLOG=<pad naar de uitvoer van apply_hints.py van deze basis> (V-#1144; zonder log kan 'regel niet te lezen' niet nagekeken worden)")
if not os.path.isfile(AL): stop(f"bestaat niet: {AL}")
LOGT = open(AL, encoding='utf-8', errors='replace').read()
for pat, wat in ((r'^G5-GET-M03: \d+ somtypen bijgewerkt$', 'G5-GET-M03'), (r'^G5-MEET-E07: \d+ somtypen bijgewerkt$', 'G5-MEET-E07'), (r'^items: \d+ met hints', "'items: …'"), (r'^stempel V-#1149: hintsSyncOp=\S+ commit=\S+ batches=\S+$', "stempelregel 'stempel V-#1149: …' (apply_hints van vóór V-#1149?)"), (r'^ronde 10: ', "slotregel 'ronde 10: …'")):
    if not re.search(pat, LOGT, re.M): stop(f"onvolledig of kapot: {AL} mist {wat} (geen volledige uitvoer van apply_hints.py)")
import hashlib      # V-#1149: stempel i.p.v. wijzigtijd
_st = re.findall(r'^stempel V-#1149: hintsSyncOp=(\S+) commit=(\S+) batches=(\S+)$', LOGT, re.M)
if len(_st) != 1: stop(f"onvolledig of kapot: {AL} heeft {len(_st)} stempelregels (verwacht 1)")
ST_OP, ST_COMMIT, _sb = _st[0]; ST_B = dict(x.split(':', 1) for x in _sb.split(','))
try: GM_OP = json.load(open(GM, encoding='utf-8')).get('hintsSyncOp')
except Exception as e: stop(f"data/gemapt.json niet te lezen ({type(e).__name__})")
if ST_OP != GM_OP: stop(f"hoort niet bij deze data: stempel hintsSyncOp={ST_OP}, data/gemapt.json {GM_OP} (een andere apply schreef de data; apply_hints.py opnieuw draaien en die log geven)")
NU_B = {os.path.basename(p): hashlib.md5(open(p, 'rb').read()).hexdigest()[:12] for p in sorted(glob.glob(os.path.join(HD, 'batch*.json')))}
for b_ in sorted(set(ST_B) | set(NU_B)):
    if ST_B.get(b_) != NU_B.get(b_): stop(f"hoort niet bij deze batches: hints/{b_} stempel {ST_B.get(b_)}, nu {NU_B.get(b_)} (batch gewijzigd na de apply; apply_hints.py opnieuw draaien)")
I = items(G)
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
F += [f"applylog {l.strip()}" for l in LOGT.splitlines() if 'niet te lezen' in l and re.search(r'G5-(GET-M03|MEET-E07)\b', l)]
SNAPF = os.path.join(D_, 'snap_z1121.json')
snap = {f"{k[0]}#{k[1]} {x['nr']}": [[h['fout'], h['soort'], h['uitleg'], h.get('uitlegSterker'), h['regel']] for h in x['foutHints']] for k in DOEL for x in I.get(k, [])}
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP Z-#1121 {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
else: F.append('SNAP Z-#1121 ontbreekt')
print(f"INFO Z-#1121: {n_i} items (GET-M03 #1, MEET-E07 #1), motor nagekeken bij {n_i}, sleutel 'aantal' bij {n_k}; SNAP {len(snap)} items" + f"; applylog {AL}; stempel hintsSyncOp={ST_OP} commit={ST_COMMIT}, {len(ST_B)} batches = data en hints/")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check Z-#1121: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
