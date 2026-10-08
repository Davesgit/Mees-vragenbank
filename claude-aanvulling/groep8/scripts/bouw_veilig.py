#!/usr/bin/env python3
"""Veilige G8-build (Oefeningen 17:27: live data/per_doel en somtypen stonden leeg vanaf 17:20:58).
Oorzaak: build_g8.py leegt bij de start data/per_doel/ en somtypen/ (os.remove per bestand) en schrijft ze pas ~40 s later opnieuw;
een onderbroken build (17:20:38, na 20 s gestopt) liet ze leeg tot de volgende build (17:24:12). Ook een gewone build had dat gat.
Nu: build_g8.py (en elke aanroep `python3 scripts/build_g8.py`) bouwt in een tijdelijke kopie (claude-merge/.g8_bouw_*/g8, zelfde schijf),
inclusief sync → patches → sync → apply. Pas als de build slaagt én data/per_doel en somtypen gevuld zijn (zelfde aantal als live, elk bestand
niet leeg, per_doel geldige JSON met items), gaat elk gewijzigd bestand met os.replace (atomair per bestand) naar live; bestanden die de
build weghaalde gaan daarna weg. Live staat zo nooit leeg of half geschreven. Mislukt de build, dan blijft live ongemoeid.
Een bestand dat tijdens de build op live veranderde (bijv. een nieuwe patch van Oefeningen) wordt niet overschreven: dat meldt 'CONFLICT'
(de build gebruikte dan de oude versie; draai opnieuw).
Na afloop: controle dat live data/per_doel en somtypen elk N (nu 23) gevulde bestanden hebben.
Z-#962 (Didactiek, les 363): ook g4–g7/data/aanvulling_uit_g8.json gaan niet meer direct live. De build schrijft ze in de bouwkopie
(logs/aanvulling_uit_g8/g{N}.json, G8_AANV_UIT); na een geslaagde build en controle (geldige JSON, items-lijst, aantal = len(items)) gaat elk
bestand met os.replace naar live, met dezelfde CONFLICT-regel. G4–G7 zijn goedgekeurde builds: zolang AANVULLING_NAAR_LIVE uit staat
(standaard; aan met G8_AANVULLING_LIVE=1) blijft een aanvulling waarvan de items verschillen van live ongewijzigd en meldt de wrapper het
verschil (aantal items, eerste ids); gelijke items = niets te doen. Live wordt dus nooit leeg, half of na een mislukte build geschreven."""
import os, sys, shutil, subprocess, tempfile, hashlib, json, glob
LIVE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEG_TOEGESTAAN = ('data/per_doel/', 'somtypen/')
MERGE = os.path.dirname(LIVE)
AANV_LIVE = {g: f'{MERGE}/g{g}/data/aanvulling_uit_g8.json' for g in (4, 5, 6, 7)}
AANVULLING_NAAR_LIVE = os.environ.get('G8_AANVULLING_LIVE') == '1'
def _sleutel(it): return json.dumps(it, sort_keys=True, ensure_ascii=False)
def aanvulling(BOUW, start_md5):
    """Z-#962: (ok, meldingen)"""
    M = []; ok = True
    for g, live in AANV_LIVE.items():
        st = f'{BOUW}/logs/aanvulling_uit_g8/g{g}.json'
        try:
            d = json.load(open(st)); its = d['items']; assert isinstance(its, list) and d.get('aantal') == len(its)
        except Exception as e:
            M.append(f'G{g}: bouwbestand ongeldig ({e}); live ongemoeid'); ok = False; continue
        try: oud = json.load(open(live))['items']
        except Exception: oud = None
        if oud is not None and [_sleutel(x) for x in oud] == [_sleutel(x) for x in its]: M.append(f'G{g}: {len(its)} items, gelijk aan live'); continue
        nu = _md5(live) if os.path.exists(live) else None
        anders = [x['id'] for x, y in zip(its, oud or []) if _sleutel(x) != _sleutel(y)] if oud is not None else []
        tekst = f'G{g}: {len(its)} items, {len(anders) + abs(len(its) - len(oud or []))} anders dan live (bijv. {anders[:3]})'
        if not AANVULLING_NAAR_LIVE: M.append(tekst + ' → live behouden (goedgekeurde build; G8_AANVULLING_LIVE=1 zet hem om)'); continue
        if nu != start_md5.get(g): M.append(tekst + ' → CONFLICT: live veranderde tijdens de build, niet overschreven'); ok = False; continue
        t = live + '.bouw_tmp'; shutil.copy2(st, t); os.replace(t, live); M.append(tekst + ' → atomair naar live')
    return ok, M
def _md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def _alle(root):
    R = {}
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x != '__pycache__']
        for f in fs:
            if f.endswith('.pyc'): continue
            p = os.path.join(d, f); R[os.path.relpath(p, root)] = _md5(p)
    return R
def controle(root, n_verwacht=None):
    """(ok, melding): data/per_doel/*.json en somtypen/*.md gevuld"""
    pd = sorted(glob.glob(f'{root}/data/per_doel/*.json')); st = sorted(glob.glob(f'{root}/somtypen/*.md')); F = []
    for p in pd:
        try:
            d = json.load(open(p))
            if not d.get('items'): F.append(f'{os.path.basename(p)}: geen items')
        except Exception as e: F.append(f'{os.path.basename(p)}: {e}')
    F += [f'{os.path.basename(p)}: leeg' for p in st if os.path.getsize(p) == 0]
    if not pd or not st: F.append(f'per_doel {len(pd)} / somtypen {len(st)} bestanden')
    if n_verwacht is not None and (len(pd), len(st)) != n_verwacht: F.append(f'aantal per_doel/somtypen {len(pd)}/{len(st)}, verwacht {n_verwacht[0]}/{n_verwacht[1]}')
    return not F, f'per_doel {len(pd)} · somtypen {len(st)}' + (' · ' + '; '.join(F[:5]) if F else ' · alle gevuld')
def main():
    n_live = (len(glob.glob(f'{LIVE}/data/per_doel/*.json')), len(glob.glob(f'{LIVE}/somtypen/*.md')))
    tmp = tempfile.mkdtemp(prefix='.g8_bouw_', dir=os.path.dirname(LIVE)); BOUW = os.path.join(tmp, 'g8')
    try:
        shutil.copytree(LIVE, BOUW, symlinks=True, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        start = _alle(BOUW); aanv_start = {g: (_md5(p) if os.path.exists(p) else None) for g, p in AANV_LIVE.items()}
        env = dict(os.environ, G8_STAGING='1', PYTHONDONTWRITEBYTECODE='1', G8_AANV_UIT=os.path.join(BOUW, 'logs', 'aanvulling_uit_g8'))
        r = subprocess.run([sys.executable, '-B', os.path.join(BOUW, 'scripts', 'build_g8.py')] + sys.argv[1:], env=env, cwd=BOUW)
        if r.returncode:
            print(f'BOUW-VEILIG: build mislukt (exit {r.returncode}); live ongemoeid'); return r.returncode
        ok, m = controle(BOUW, n_live if n_live[0] and n_live[1] else None)
        print('BOUW-VEILIG controle bouwmap:', m)
        if not ok: print('BOUW-VEILIG: bouwmap niet compleet; live ongemoeid'); return 3
        for g in AANV_LIVE:      # Z-#962: eerst alle aanvullingen controleren, pas daarna iets omzetten
            try: d_ = json.load(open(f'{BOUW}/logs/aanvulling_uit_g8/g{g}.json')); assert isinstance(d_['items'], list) and d_.get('aantal') == len(d_['items'])
            except Exception as e: print(f'BOUW-VEILIG: aanvulling G{g} ongeldig ({e}); live ongemoeid'); return 3
        eind = _alle(BOUW); nu_live = _alle(LIVE); n_w = n_c = n_d = 0
        for rel, h in sorted(eind.items()):
            if start.get(rel) == h: continue
            if nu_live.get(rel) != start.get(rel): print('BOUW-VEILIG CONFLICT (live veranderde tijdens de build, niet overschreven):', rel); n_c += 1; continue
            doel = os.path.join(LIVE, rel); os.makedirs(os.path.dirname(doel), exist_ok=True)
            t = doel + '.bouw_tmp'; shutil.copy2(os.path.join(BOUW, rel), t); os.replace(t, doel); n_w += 1
        for rel in sorted(set(start) - set(eind)):
            if rel.startswith(WEG_TOEGESTAAN) and nu_live.get(rel) == start[rel] and os.path.exists(os.path.join(LIVE, rel)):
                os.remove(os.path.join(LIVE, rel)); n_d += 1
        ok3, m3 = aanvulling(BOUW, aanv_start)
        for x in m3: print('BOUW-VEILIG aanvulling', x)
        ok2, m2 = controle(LIVE, n_live if n_live[0] and n_live[1] else None)
        print(f'BOUW-VEILIG: {n_w} bestanden atomair naar live, {n_d} weg, {n_c} conflict · live: {m2}')
        return 0 if ok2 and ok3 and not n_c else 4
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
if __name__ == '__main__':
    sys.exit(main())
