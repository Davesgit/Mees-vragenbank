#!/usr/bin/env python3
"""r13 zelf (na-ronde-r13; Leerlijn-besluit BESLUIT_R9-4_R10_NIVEAUS.md, 8 okt 14:40; opdracht Dave/Overzicht 17:32 en 17:51).
Werkt op r13/g5 en r13/g6 (kopie van de goedgekeurde builds + kloktijdronde), nooit op live. Idempotent.
G5  L-R9-4a  speelvolgorde G5-GET-E07: delen-cluster #3 → #9, keer-cluster #8 → #10 → #5; weergavenummers blijven (D-#408).
             bevroren/speelvolgorde.json + per item merge.speelVolgorde (positie in de speelvolgorde van het doel).
    L-R9-4b  naar-002, naar-026 (#10) en naar-008 (#9) naar basis (3 items omlaag, gelijktrekken binnen het cluster).
    JO       juisteOptie/juisteOptieTekst gelijk aan het antwoord (2 items).
G6  L-R10a   niveau uit het kenmerk (r13/niveaus.py) voor de 34 somtypes; kritisch-items blijven kritisch; None = niveau blijft.
    L-R10c   VERH-E02 #4 (balk) en #3 (taart): alleen basis.
    L-R10d   dunne somtypes met één niveau (niet in de 37): kenmerk van het grote somtype van hetzelfde doel, als dat op álle items leesbaar is.
    L-R10e   extraVelden.niveauVoorlopig vervalt bij de hm/dl-somtypes (MEET-E01 nrO 8–11, MEET-E04 nrO 5–8).
    L-R10f   GET-E03 #1/#5/#8 naar park-G7: NIET (wacht op Dave).
    V-#851/#852  GET-E08 data met gelijke som (gemiddelde-check-didactiek.md): opgave, optelling in claudeUitleg en claudeKaleSom.
    N13-1/2  bordtitels VBN-E02 en MEET-E05.
    JO       juisteOptie (16 items).
Daarna per groep scripts/apply_hints.py (fout-regels per item opnieuw, per_doel uit gemapt). Rapport: r13/r13_rapport.json."""
import json, os, re, sys, glob, collections, subprocess, copy
R13 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, R13)
import niveaus as NV, lijst as LJ
NK = {'basis': 'Opwarmen', 'toepassen': 'Oefenen', 'kritisch': 'Uitdaging'}
VOLGORDE_E07 = [1, 2, 3, 9, 4, 6, 7, 8, 10, 5, 11]
NAAR_BASIS_G5 = {'G5-GET-E07-claude-bank-naar-002', 'G5-GET-E07-claude-bank-naar-026', 'G5-GET-E07-claude-bank-naar-008'}
E08 = {'004': ([6, 6, 3, 3, 7], [6, 7, 2, 3, 7]), '005': ([8, 3, 9, 5, 5], [9, 2, 9, 5, 5]), '006': ([4, 6, 12, 6, 12], [5, 6, 11, 6, 12]),
       '007': ([6, 7, 2, 8, 2], [7, 7, 1, 8, 2]), '008': ([9, 8, 10, 10, 8], [8, 8, 11, 10, 8]),
       '010': ([5, 6, 6, 7], [3, 7, 7, 7]), '011': ([6, 3, 7, 4], [6, 3, 8, 3]), '012': ([6, 8, 6, 8], [6, 10, 6, 6])}
TITELS = {'G6-VBN-E02': 'Beelddiagram, cirkeldiagram en lijngrafiek aflezen', 'G6-MEET-E05': 'Kilogram en gram vergelijken en omrekenen'}
HMDL = {('G6-MEET-E01', n) for n in (8, 9, 10, 11)} | {('G6-MEET-E04', n) for n in (5, 6, 7, 8)}
PARK_G7 = {('G6-GET-E03', 1), ('G6-GET-E03', 5), ('G6-GET-E03', 8)}

def zet_niveau(it, nv, log, reden):
    if it['niveau'] == nv: return
    log.append({'id': it['id'], 'van': it['niveau'], 'naar': nv, 'kenmerk': reden}); it['niveau'] = nv; it['niveauKind'] = NK[nv]

def juiste_optie(it, log):
    ad = it.get('antwoordDetail')
    if it.get('type') != 'meerkeuze' or not isinstance(ad, dict) or not ad.get('juisteOptie'): return
    ops = {o.get('letter'): o.get('tekst') for o in it.get('opties') or []}; a = str(it['antwoord'])
    if ops.get(ad['juisteOptie']) == a and ad.get('juisteOptieTekst', a) == a: return
    lt = [l for l, t in ops.items() if t == a]
    if len(lt) != 1: log.append({'id': it['id'], 'fout': f'antwoord {a!r} staat {len(lt)}× in de opties, niet hersteld'}); return
    log.append({'id': it['id'], 'van': [ad.get('juisteOptie'), ad.get('juisteOptieTekst')], 'naar': [lt[0], a]})
    ad['juisteOptie'] = lt[0]
    if 'juisteOptieTekst' in ad: ad['juisteOptieTekst'] = a

def vervang_diep(x, oud, nieuw):
    if isinstance(x, str): return x.replace(oud, nieuw)
    if isinstance(x, list): return [vervang_diep(v, oud, nieuw) for v in x]
    if isinstance(x, dict): return {k: vervang_diep(v, oud, nieuw) for k, v in x.items()}
    return x
def opsom(v): return ', '.join(map(str, v[:-1])) + ' en ' + str(v[-1])

def e08(it, log):
    m = re.fullmatch(r'G6-GET-E08-claude-bank-(\d{3})', it['id'])
    if not m or m.group(1) not in E08: return
    oud, nieuw = E08[m.group(1)]
    if sum(oud) != sum(nieuw): raise SystemExit(f'E08 {m.group(1)}: som verandert')
    if opsom(nieuw) in it['opgave']: return
    if opsom(oud) not in it['opgave']: log.append({'id': it['id'], 'fout': 'oude getallen niet in de opgave'}); return
    for k in ('opgave', 'opgaveStappen', 'extraVelden', 'visual', 'context', 'antwoordDetail'):
        if k in it:
            it[k] = vervang_diep(it[k], opsom(oud), opsom(nieuw)); it[k] = vervang_diep(it[k], ' + '.join(map(str, oud)), ' + '.join(map(str, nieuw)))
    log.append({'id': it['id'], 'van': oud, 'naar': nieuw, 'som': sum(nieuw), 'antwoord': it['antwoord']})

def laad(g): p = f'{R13}/g{g}/data/gemapt.json'; return p, json.load(open(p, encoding='utf-8'))
def schrijf(p, G): json.dump(G, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
def apply(g):
    r = subprocess.run([sys.executable, '-B', f'{R13}/g{g}/scripts/apply_hints.py'], capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    if r.returncode: raise SystemExit(f'G{g} apply_hints faalt:\n{r.stderr[-2000:]}')
    return r.stdout.strip().splitlines()[-4:]

def g5():
    p, G = laad(5); R = {'L-R9-4a': [], 'L-R9-4b': [], 'JO': []}
    for it in G['items']:
        m = it['merge']
        if m.get('status') != 'gemapt': continue
        if m['doel'] == 'G5-GET-E07':
            pos = VOLGORDE_E07.index(m['somtypeNr']) + 1
            if m.get('speelVolgorde') != pos: m['speelVolgorde'] = pos; R['L-R9-4a'].append(it['id'])
        if it['id'] in NAAR_BASIS_G5: zet_niveau(it, 'basis', R['L-R9-4b'], 'L-R9-4b: uitkomst/deeltal 2 cijfers, gelijk aan het cluster')
        juiste_optie(it, R['JO'])
    schrijf(p, G)
    json.dump({'uitleg': 'L-R9-4a (Leerlijn-besluit A, 8 okt 14:40): speel- en progressievolgorde per doel, als lijst van weergavenummers (bevroren/somtype_weergave_nr.json). '
               'Geen hernummering (D-#408). Per item staat de positie in merge.speelVolgorde. Delen-cluster #3 → #9, keer-cluster #8 → #10 → #5.',
               'volgorde': {'G5-GET-E07': VOLGORDE_E07}}, open(f'{R13}/g5/bevroren/speelvolgorde.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    R['apply'] = apply(5); R['L-R9-4a'] = len(R['L-R9-4a']); return R

def g6():
    p, G = laad(6); R = {'L-R10a': [], 'L-R10a_geenKenmerk': collections.Counter(), 'L-R10c': [], 'L-R10d': [], 'L-R10d_niet': [], 'L-R10e': [], 'V-#851/#852': [], 'JO': [], 'fouten': []}
    vast = {(d, n) for d, n, _ in LJ.R13_34}; basis = {(d, n) for d, n, _ in LJ.R13_BASIS}
    groep = collections.defaultdict(list)
    for it in G['items']:
        if it['merge'].get('status') == 'gemapt': groep[(it['merge']['doel'], it['merge']['somtypeNrOrigineel'])].append(it)
    for key, its in groep.items():
        for it in its:
            e08(it, R['V-#851/#852']); juiste_optie(it, R['JO'])
            if key in vast and it['niveau'] != 'kritisch':
                try: nv, k = NV.classificeer(it, *key)
                except Exception as e: nv, k = None, f'niet te lezen ({type(e).__name__})'
                if nv: zet_niveau(it, nv, R['L-R10a'], k)
                else: R['L-R10a_geenKenmerk'][f'{key[0]} nrO {key[1]}: {k}'] += 1
            if key in basis and it['niveau'] != 'kritisch': zet_niveau(it, 'basis', R['L-R10c'], 'alleen basis (besluit B)')
            if key in HMDL and (it.get('extraVelden') or {}).get('niveauVoorlopig'):
                it['extraVelden']['niveauVoorlopig'] = False; R['L-R10e'].append(it['id'])
    # L-R10d: dunne somtypes met één niveau, niet in de 37 en niet in park-G7
    groot = {}
    for d, n, _ in LJ.R13_34:
        if d not in groot or len(groep[(d, n)]) > len(groep[groot[d]]): groot[d] = (d, n)
    for key, its in sorted(groep.items()):
        if key in vast or key in basis or key in PARK_G7 or key[0] == 'G6-GET-E08': continue
        if len({i['niveau'] for i in its}) != 1: continue
        if key[0] not in groot: R['L-R10d_niet'].append(f'{key[0]} nrO {key[1]} ({len(its)}): geen groot somtype met kenmerk in dit doel'); continue
        uit = []
        for it in its:
            try: uit.append(NV.classificeer(it, *groot[key[0]]))
            except Exception: uit.append((None, 'andere vorm'))
        if any(nv is None for nv, _ in uit) or any(it['niveau'] == 'kritisch' for it in its):
            R['L-R10d_niet'].append(f'{key[0]} nrO {key[1]} ({len(its)}): kenmerk van nrO {groot[key[0]][1]} niet op alle items te lezen'); continue
        for it, (nv, k) in zip(its, uit): zet_niveau(it, nv, R['L-R10d'], f'L-R10d via nrO {groot[key[0]][1]}: {k}')
    schrijf(p, G)
    R['apply'] = apply(6)
    for doel, t in TITELS.items():
        pd = f'{R13}/g6/data/per_doel/{doel}.json'; D = json.load(open(pd, encoding='utf-8'))
        if D.get('bordtitel') != t: R.setdefault('N13', []).append({'doel': doel, 'van': D.get('bordtitel'), 'naar': t}); D['bordtitel'] = t
        json.dump(D, open(pd, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    R['L-R10a_geenKenmerk'] = dict(R['L-R10a_geenKenmerk'])
    return R

def spreiding():
    G = json.load(open(f'{R13}/g6/data/gemapt.json'))['items']; c = collections.defaultdict(collections.Counter)
    for it in G:
        if it['merge'].get('status') == 'gemapt': c[(it['merge']['doel'], it['merge']['somtypeNrOrigineel'])][it['niveau']] += 1
    uit = []
    for d, n, w in LJ.R13_34:
        k = c[(d, n)]; tot = sum(k.values())
        uit.append({'somtype': f'{d} #{w} (nrO {n})', 'b': k['basis'], 't': k['toepassen'], 'k': k['kritisch'], 'n': tot,
                    'tekort': [nv for nv in ('basis', 'toepassen', 'kritisch') if k[nv] < 3], 'boven60': [nv for nv in k if k[nv] > 0.6 * tot]})
    return uit

if __name__ == '__main__':
    R = {'G5': g5(), 'G6': g6()}; R['G6']['spreiding'] = spreiding()
    json.dump(R, open(f'{R13}/r13_rapport.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    for g in ('G5', 'G6'):
        print(g, {k: (len(v) if isinstance(v, list) else v) for k, v in R[g].items() if k not in ('spreiding',)})
