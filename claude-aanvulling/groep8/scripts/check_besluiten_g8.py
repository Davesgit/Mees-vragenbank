#!/usr/bin/env python3
"""Controle (1 okt, Dave 22:06): zijn de 1226 G8-twijfelbesluiten (besluiten_twijfel.json + Dave 20:56) in de data toegepast?
Zoekt elk besluit op twijfelId in G8 (gemapt, terug_G7, buiten) en in de aanvullingsbestanden van G4–G7, en in de gemapt.json van die groep.
Alleen lezen; draai vanuit claude-merge/g8."""
EXTRA = []
import json, csv, sys, collections, re, os
sys.path.insert(0, 'scripts'); import besluiten_g8 as BG
B = BG.laad()                                         # claudeId → besluit (met Dave-overrides)
n = lambda s: re.sub(r'\s+', ' ', str(s)).strip()
waar = {}                                             # twijfelId → [(bestand, item)]
def lees(pad, label):
    if not os.path.exists(pad): return
    d = json.load(open(pad)); its = d['items'] if isinstance(d, dict) else d
    for it in its:
        m = it.get('merge') or {}
        tid = (m.get('didactiekG8') or {}).get('twijfelId') or (m.get('uitG8') or {}).get('twijfelId')
        if tid: waar.setdefault(tid, []).append((label, it))
for naam in ('gemapt', 'terug_G7', 'buiten_basisschool'): lees(f'data/{naam}.json', f'G8/{naam}')
for g in (4, 5, 6, 7):
    lees(f'../g{g}/data/aanvulling_uit_g8.json', f'G{g}/aanvulling')
    lees(f'../g{g}/data/gemapt.json', f'G{g}/gemapt')
gesch = {r['claudeId'] for r in csv.DictReader(open('logs/geschrapt.csv'))}
per = collections.defaultdict(collections.Counter); mis = collections.defaultdict(list); extra = collections.Counter()
for cid, d in B.items():
    tid, cat, bes, g = d['twijfelId'], d['groep'], d['besluit'], d.get('doelGroep'); plekken = waar.get(tid, []); p = []; ok_ = collections.Counter()
    if bes == 'schrappen':
        if plekken: p.append('staat nog in ' + ', '.join(l for l, _ in plekken))
        elif cid not in gesch: p.append('niet in geschrapt.csv')
    else:
        verwacht = ['G8/gemapt'] if g == 8 else [f'G{g}/aanvulling', f'G{g}/gemapt']
        labels = [l for l, _ in plekken]
        if sorted(labels) != sorted(verwacht): p.append(f'plek {labels} ≠ {verwacht}')
        for l, it in plekken:
            m = it['merge']; doel = it.get('doelId') or m.get('doel') or m.get('voorstelDoel')
            if doel != d['doelId']: p.append(f'{l}: doel {doel} ≠ {d["doelId"]}')
            if g == 8 and m.get('status') != 'gemapt': p.append(f'{l}: status {m.get("status")}')
            if g != 8 and l.endswith('aanvulling') and m.get('status') != f'naar-G{g}': p.append(f'{l}: status {m.get("status")}')
            if bes == 'aanpassen':
                na = d.get('nieuwAntwoord')
                if na is not None and n(it['antwoord']) != n(na): p.append(f"{l}: antwoord {it['antwoord']} ≠ {na}")
                if d.get('nieuweOpties') and sorted(n(o['tekst']) for o in it['opties'] or []) != sorted(n(x) for x in d['nieuweOpties']): p.append(f'{l}: opties')
                no = d.get('nieuweOpgave')
                if tid.endswith('E04-claude-bank-twijfel-012'): no = 'In het staafdiagram zie je hoeveel boeken er op maandag, dinsdag en woensdag zijn geleend. Op welke dag zijn de meeste boeken geleend?'
                if no and n(it['opgave']) != n(no): p.append(f"{l}: opgave «{it['opgave'][:60]}» ≠ «{no[:60]}»")
                if d.get('nieuweFoutHints') and not tid.endswith('E04-claude-bank-twijfel-012'):
                    f1 = sorted(n(f['fout']) for f in d['nieuweFoutHints']); f2 = sorted(n(f['fout']) for f in it.get('foutHints') or [])
                    # Heeft het item hints van de doelgroep (merge.hints, bv. G5 batch 7 van 22:55), dan voegen de motorregels sleutels toe: de sleutels van
                    # het besluit moeten er dan in zitten (deelverzameling); zonder hints moeten ze precies gelijk zijn.
                    if (it.get('merge') or {}).get('hints'):
                        if not set(f1) <= set(f2): p.append(f'{l}: foutHints {f2} missen {sorted(set(f1) - set(f2))} (besluit {f1})')
                        elif f1 != f2: EXTRA.append((tid, l, sorted(set(f2) - set(f1))))
                    elif f1 != f2: p.append(f'{l}: foutHints {f2} ≠ {f1}')
            if d.get('geldigeAntwoorden') and not set(map(n, d['geldigeAntwoorden'])) <= set(map(n, it.get('geldigeAntwoorden') or [])): p.append(f'{l}: geldigeAntwoorden')
            te = (d.get('visual') or {}).get('tekeneis'); v = it.get('visual') or {}
            if te in ('A', 'B'):
                if v.get('kijkrichting') != 'rechtsvoor' or bool(v.get('kijkrichtingVerplicht')) != (te == 'B'): p.append(f'{l}: kijkrichting {te}')
                else: ok_[f'tekeneis {te} rechtsvoor' + (' + verplicht' if te == 'B' else '')] += 1
            if d.get('badge'):
                if it.get('badge') != d['badge'] or doel != 'G8-MEET-E03': p.append(f'{l}: badge')
                else: ok_[f"badge '{d['badge']}' in G8-MEET-E03"] += 1
            if d.get('bijnaDubbelVan'):
                if m.get('bijnaDubbelVanTwijfel') != d['bijnaDubbelVan']: p.append(f'{l}: bijnaDubbelVan')
                else: ok_['bijnaDubbelVan'] += 1
            if d.get('duplicaatVan'):
                if m.get('duplicaatVanTwijfel') != d['duplicaatVan']: p.append(f'{l}: duplicaatVan')
                else: ok_['duplicaatVan'] += 1
            if re.search(r'\bkans', json.dumps(it, ensure_ascii=False), re.I): p.append(f'{l}: woord kans')
            if tid.endswith('E04-claude-bank-twijfel-012'):
                if doel != 'G8-VBN-V01' or (v.get('jsRender') or {}).get('soort') != 'staafdiagram': p.append(f'{l}: 012 geen staafdiagram/G8-VBN-V01')
                else: ok_['012 staafdiagram in G8-VBN-V01'] += 1
    for k in set(ok_): extra[k] += 1
    per[cat][bes] += 1
    if p: mis[cat].append((tid, bes, p))
# losse eisen (Dave 20:56 (5)): G8-GET-E02-001 (4 × 198) → G5-GET-E07
e7 = [it for it in json.load(open('../g5/data/aanvulling_uit_g8.json'))['items'] if 'Dave 20:56 (5)' in (it['merge'].get('reden') or '')]
e7ok = len(e7) == 1 and e7[0]['merge'].get('voorstelDoel') == 'G5-GET-E07' and '198' in e7[0]['opgave']
print('E02-001 → G5-GET-E07:', 'ok' if e7ok else 'FOUT', [(it['opgave'], it['antwoord']) for it in e7])
print('totaal besluiten', len(B), '· gevonden in data', sum(1 for d in B.values() if waar.get(d['twijfelId'])))
for cat in per: print(f"{cat}: {dict(per[cat])} · {sum(per[cat].values())} · ontbreekt/fout {len(mis[cat])}")
for k, v in sorted(extra.items()): print('  ok:', k, v)
for cat, l in mis.items():
    for x in l[:10]: print('   PROBLEEM', cat, x)
print('INFO extra sleutels door de hints van de doelgroep (geen probleem):', len(EXTRA))
print('PROBLEMEN', sum(len(l) for l in mis.values()) + (0 if e7ok else 1))
