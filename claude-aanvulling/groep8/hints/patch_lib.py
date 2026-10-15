#!/usr/bin/env python3
"""[G8-kopie (8 okt 2026, Oefeningen) van g7/hints/patch_lib.py; BASE = claude-merge/g8 (map van dit bestand)] Gedeelde patch-motor voor hints/patch_batch*.py (ronde 2b, 1 okt 2026, Oefeningen).
Patcht hints/batchN.json IN PLACE (na een sync/rebuild nooit make_batch*.py --force). Kiest entries op doel + nrOrigineel.
PATCH = [(doel, nrOrigineel, veld, wordt, waarom)], veld =
  'hint1' | 'hint2' | 'ouderzin' | 'foutHints' (hele lijst) | 'claudeVervangen' | ander veld van de entry
  ('fh', soort, {sleutel: waarde})   één fout-hint, gekozen op 'soort' (uniek in het somtype); waarde None = sleutel weghalen
  'kopNagekeken'                     kopGewijzigd opruimen zoals in G3: somtypeOrigineel := huidige kop,
                                     somtypeEerder += {kop: oude somtypeOrigineel, tot: datum}, kopNagekeken := datum
  'geenItems'                        markering {sinds, reden} voor een entry zonder items (wordt = dict)
  'nieuwEntry'                       nieuwe entry (wordt = dict met de basisvelden), alleen als (doel, nrOrigineel) er nog niet is (ronde 5c)
  'weg'                              entry weghalen (na samenvoegen van somtypes in een rebuild: één entry per somtype);
                                     idempotent (al weg = niets); gelogd als veld '(entry)' met was = de oude kop
Idempotent: alle patches worden op een kopie toegepast; daarna wordt per veld het verschil met de json gelogd (was → wordt)
in hints/wijzigingen_batchN.json. Patches op hetzelfde veld: de laatste wint (zo kan een latere ronde een eerdere overschrijven).
Optie APOSTROF=True: zet in alle kindteksten ’ om in ' (rechte apostrof, ronde 2b)."""
import json, os, copy, datetime
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIND = ('hint1', 'hint2', 'ouderzin')

def run(n, PATCH, APOSTROF=False):
    P = f'{BASE}/hints/batch{n}.json'; LOG = f'{BASE}/hints/wijzigingen_batch{n}.json'
    D = json.load(open(P, encoding='utf-8')); oud = copy.deepcopy(D)
    log = json.load(open(LOG, encoding='utf-8')) if os.path.exists(LOG) else []
    nu = datetime.datetime.now().strftime('%H:%M'); vandaag = datetime.date.today().isoformat()
    waarom_van = {}; n_weg = 0
    def entry(doel, nro):
        st = [s for s in D['somtypen'] if s['doel'] == doel and s['nrOrigineel'] == nro]
        assert len(st) == 1, (doel, nro, len(st)); return st[0]
    for doel, nro, veld, wordt, waarom in PATCH:
        if veld == 'nieuwEntry':
            # ronde 5c (#84): een nieuwe entry voor een nieuw somtype (generator), alleen als hij er nog niet is (idempotent).
            # wordt = de basisvelden (doel, nrOrigineel, somtypeOrigineel …); de teksten komen uit de patches erna.
            if not any(s['doel'] == doel and s['nrOrigineel'] == nro for s in D['somtypen']):
                D['somtypen'].append(copy.deepcopy(wordt))
                log.append({'tijd': nu, 'doel': doel, 'nrOrigineel': nro, 'veld': '(entry)', 'was': None, 'wordt': wordt.get('somtypeOrigineel'), 'waarom': waarom}); n_weg += 1
            continue
        if veld == 'weg':
            for s in [s for s in D['somtypen'] if s['doel'] == doel and s['nrOrigineel'] == nro]:
                D['somtypen'].remove(s)
                log.append({'tijd': nu, 'doel': doel, 'nrOrigineel': nro, 'veld': '(entry)', 'was': s.get('somtypeOrigineel'), 'wordt': None, 'waarom': waarom}); n_weg += 1
            continue
        st = entry(doel, nro)
        if isinstance(veld, tuple):
            _, soort, upd = veld
            fh = [f for f in st['foutHints'] if f['soort'] == soort]
            assert len(fh) == 1, (doel, nro, soort, len(fh))
            for k, v in upd.items():
                if v is None: fh[0].pop(k, None)
                else: fh[0][k] = v
                waarom_van[(doel, nro, f'foutHint[{soort}].{k}')] = waarom
        elif veld == 'kopNagekeken':
            kg = st.get('kopGewijzigd')
            if kg:
                assert kg['naar'] == st['somtype'], (doel, nro, kg, st['somtype'])
                st.setdefault('somtypeEerder', []).append({'kop': st['somtypeOrigineel'], 'tot': vandaag})
                st['somtypeOrigineel'] = st['somtype']; st['kopNagekeken'] = vandaag; st.pop('kopGewijzigd')
            for k in ('somtypeOrigineel', 'somtypeEerder', 'kopNagekeken', 'kopGewijzigd'): waarom_van[(doel, nro, k)] = waarom
        else:
            st[veld] = wordt; waarom_van[(doel, nro, veld)] = waarom
    if APOSTROF:
        for st in D['somtypen']:
            for k in KIND:
                if '’' in st[k]: st[k] = st[k].replace('’', "'"); waarom_van.setdefault((st['doel'], st['nrOrigineel'], k), "rechte apostrof (ronde 2b)")
            for f in st['foutHints']:
                if '’' in f['tekst']:
                    f['tekst'] = f['tekst'].replace('’', "'"); waarom_van.setdefault((st['doel'], st['nrOrigineel'], f"foutHint[{f['soort']}].tekst"), "rechte apostrof (ronde 2b)")
    # verschil loggen
    oud_per = {(s['doel'], s['nrOrigineel']): s for s in oud['somtypen']}
    n_w = n_weg   # weggehaalde entries staan al in de log
    for sn in D['somtypen']:
        key = (sn['doel'], sn['nrOrigineel']); so = oud_per.get(key) or {'foutHints': []}   # nieuwEntry: alles is nieuw
        for k in sorted(set(so) | set(sn)):
            if k == 'foutHints' and (key + ('foutHints',)) not in waarom_van:
                fo = {f['soort']: f for f in so['foutHints']}; fn = {f['soort']: f for f in sn['foutHints']}
                for s in fn:
                    for kk in sorted(set(fo.get(s, {})) | set(fn[s])):
                        a, b = fo.get(s, {}).get(kk), fn[s].get(kk)
                        if a != b:
                            log.append({'tijd': nu, 'doel': key[0], 'nrOrigineel': key[1], 'veld': f'foutHint[{s}].{kk}', 'was': a, 'wordt': b,
                                        'waarom': waarom_van.get(key + (f'foutHint[{s}].{kk}',), '')}); n_w += 1
                continue
            if so.get(k) != sn.get(k):
                log.append({'tijd': nu, 'doel': key[0], 'nrOrigineel': key[1], 'veld': k, 'was': so.get(k), 'wordt': sn.get(k),
                            'waarom': waarom_van.get(key + (k,), '')}); n_w += 1
    # ronde 9 (8 okt, Didactiek gate G5): alleen wegschrijven als er iets veranderd is, anders krijgt elke batch een nieuwe mtime bij gelijke md5
    if D != oud or n_w:
        json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(log, open(LOG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'batch{n}.json: {n_w} wijzigingen (log: {len(log)})')
    return n_w

# ---- helpers voor patch-scripts (ronde 2b) ----
def N(soort, regel, tekst, claudeTekst=None, waarom=None):
    f = {'bron': 'nieuw', 'soort': soort, 'claudeDenkfout': None, 'regel': regel, 'tekst': tekst}
    if claudeTekst: f.update(claudeTekst=claudeTekst, waarom=waarom)
    return f
def C(soort, regel, tekst, dk=None):
    return {'bron': 'claude', 'soort': soort, 'claudeDenkfout': dk, 'regel': regel, 'tekst': tekst}
def T(soort, regel, tekst, claudeTekst, waarom, dk=None):
    return {'bron': 'claude-taalfix', 'soort': soort, 'claudeDenkfout': dk, 'regel': regel, 'tekst': tekst, 'claudeTekst': claudeTekst, 'waarom': waarom}
def V(claudeTekst, dk, waarom):
    return {'claudeTekst': claudeTekst, 'claudeDenkfout': dk, 'waarom': waarom}
def huidig(n, doel, nro, veld='foutHints'):
    """kopie van een veld uit de huidige batchN.json (om lijsten idempotent aan te vullen)"""
    D = json.load(open(f'{BASE}/hints/batch{n}.json', encoding='utf-8'))
    return copy.deepcopy(next(s for s in D['somtypen'] if s['doel'] == doel and s['nrOrigineel'] == nro).get(veld))
def voeg_in(lijst, na_soort, nieuw):
    """idempotent: haal eerdere versies (zelfde soort) weg en zet de nieuwe na 'na_soort' (None = vooraan)."""
    soorten = {f['soort'] for f in nieuw}; lijst = [f for f in lijst if f['soort'] not in soorten]
    i = 0 if na_soort is None else next(j for j, f in enumerate(lijst) if f['soort'] == na_soort) + 1
    return lijst[:i] + nieuw + lijst[i:]
