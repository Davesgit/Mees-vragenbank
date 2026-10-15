#!/usr/bin/env python3
"""Check V-#1081 andere kant op een uitvoer van zet_andere_kant.py. [MUT=..] [SNAP=1] python3 check_andere_kant.py <uit.json> [<concept-origineel.json>]
Per item in scope: elke Nee-waarde ≠ goed en ≠ elkaar; de nieuwe waarde ligt aan de kant die in 'kant' staat; L1 bij elke Nee-afleider noemt de
richting die klopt (te weinig ↔ lager dan goed, te veel ↔ hoger), geen cijfer, geen optieletter; bewering, antwoord, juisteOptie en de Ja-letter zijn
gelijk aan het origineel; rang-guard per somtype hooguit 2× dezelfde rang en minstens één afleider aan elke kant; SNAP van de nieuwe opties."""
import json, sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from andere_kant import *
MUT = os.environ.get('MUT', ''); F = []; SNAPF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snap_andere_kant.json')
D = json.load(open(sys.argv[1], encoding='utf-8')); O = json.load(open(sys.argv[2] if len(sys.argv) > 2 else '/workspace/claude-merge/r13/kritisch_concept_g6.json', encoding='utf-8'))
OI = {x['id']: x for x in O['items']}
XS = [x for x in D['items'] if (x['doelId'], x['somtypeNrOrigineel']) in SCOPE]
gez = [x for x in XS if 'oefeningen1081' in x]; x0 = gez[0] if gez else None
def opt(x, t): return next(o for o in x['opties'] if o['tekst'] == t)
if x0:
    n0 = x0['oefeningen1081']['andereKant']['nieuw']
    if MUT == 'M_kant':   # fout aan de verkeerde kant (zelfde tekst/denkfout), bv. 3× het goede getal
        t_ = re.sub(GETAL, str(goed(x0) * 3), n0, count=1); o_ = opt(x0, n0); o_['tekst'] = t_
        x0['conceptHints']['L1'][t_] = x0['conceptHints']['L1'].pop(n0); x0['denkfoutPerOptie'][t_] = x0['denkfoutPerOptie'].pop(n0); x0['oefeningen1081']['andereKant']['nieuw'] = t_
    if MUT == 'M_richting': x0['conceptHints']['L1'][n0] = re.sub(r'te (weinig|veel)', lambda m: 'te veel' if m.group(1) == 'weinig' else 'te weinig', x0['conceptHints']['L1'][n0])
    if MUT == 'M_cijfer': x0['conceptHints']['L1'][n0] += ' Haal er 10 af.'
    if MUT == 'M_letter': x0['conceptHints']['L1'][n0] += ' Kies dan B.'
    if MUT == 'M_botst':  o_ = opt(x0, n0); o_['tekst'] = re.sub(GETAL, str(goed(x0)), n0, count=1)
    if MUT == 'M_antwoord': x0['antwoord'] = x0['antwoord'] + ' '
xm = next((x for x in gez if x['doelId'] == 'G6-MEET-E03'), None); xv = next((x for x in gez if x['doelId'] == 'G6-VERH-E02'), None)
if MUT == 'M_vraag' and xm:      # afleider = de gegeven zijde (getal uit de vraag), tekst/denkfout 'tafelstap' blijft
    n_ = xm['oefeningen1081']['andereKant']['nieuw']; z_ = re.search(r'Eén zijde is (\d+) cm', xm['opgave']).group(1); t_ = re.sub(GETAL, z_, n_, count=1)
    opt(xm, n_)['tekst'] = t_; xm['conceptHints']['L1'][t_] = xm['conceptHints']['L1'].pop(n_); xm['denkfoutPerOptie'][t_] = xm['denkfoutPerOptie'].pop(n_); xm['oefeningen1081']['andereKant']['nieuw'] = t_
if MUT == 'M_woord' and xv: n_ = xv['oefeningen1081']['andereKant']['nieuw']; xv['conceptHints']['L1'][n_] = xv['conceptHints']['L1'][n_].replace(verh_e02(xv)[3], 'appels')
if MUT == 'M_teller' and xv: xv['opgave'] = re.sub(r'"(\d+)/', '"1/', xv['opgave'], count=1); OI[xv['id']] = dict(OI[xv['id']], opgave=xv['opgave'])
for x in XS:
    T = goed(x); o0 = OI[x['id']]
    for k in ('bewering', 'antwoord', 'beweringKlopt', 'claim', 'opgave'):
        if x[k] != o0[k]: F.append(f"{x['id']}: {k} veranderd")
    if x['antwoordDetail']['juisteOptie'] != o0['antwoordDetail']['juisteOptie'] or [o['letter'] for o in x['opties'] if o['tekst'].startswith('Ja')] != [o['letter'] for o in o0['opties'] if o['tekst'].startswith('Ja')]:
        F.append(f"{x['id']}: letter van goed of Ja veranderd")
    nee = [w(o['tekst']) for o in x['opties'] if o['tekst'].startswith('Nee')]
    if len(set(nee + [w(x['bewering'])])) != 3: F.append(f"{x['id']}: waarden niet verschillend {nee} / {x['bewering']}")
    for o in x['opties']:
        if not o['tekst'].startswith('Nee') or w(o['tekst']) == T: continue
        l1 = (x['conceptHints'].get('L1') or {}).get(o['tekst'])
        if l1 is None: F.append(f"{x['id']}: geen L1 bij {o['tekst']!r}"); continue
        if 'oefeningen1081' in x and o['tekst'] == x['oefeningen1081']['andereKant']['nieuw']:
            v = w(o['tekst']); kant = x['oefeningen1081']['andereKant']['kant']
            if (kant == 'laag') != (v < T): F.append(f"{x['id']}: nieuwe waarde {v} ligt niet {kant} t.o.v. {T}")
            if ('te weinig' in l1) != (v < T) or ('te veel' in l1) != (v > T): F.append(f"{x['id']}: L1-richting klopt niet bij {v} (goed {T}): {l1[:50]}")
            if re.search(r'\d', l1): F.append(f"{x['id']}: cijfer in L1 (verklapt): {l1[:60]}")
            if re.search(r'\b[ABC]\b', l1) or re.search(r'optie', l1, re.I): F.append(f"{x['id']}: optieletter in L1: {l1[:60]}")
            if x['denkfoutPerOptie'].get(o['tekst']) != x['oefeningen1081']['andereKant']['denkfout']: F.append(f"{x['id']}: denkfout ontbreekt")
# Didactiek 15 okt: voorwaarden per item (ook in de SNAP)
VW = {}
for x in gez:
    nk = x['oefeningen1081']['andereKant']; v = w(nk['nieuw']); T = goed(x)
    if x['doelId'] == 'G6-MEET-E03':
        A, z = map(int, re.search(r'oppervlakte van (\d+) cm²\. Eén zijde is (\d+) cm', x['opgave']).groups())
        VW[x['id']] = {'nietUitDeVraag': v not in vraaggetallen(x), 'alleenTafelstap': v == T - 1 and v not in andere_routes_e03(A, z)}
    if x['doelId'] == 'G6-VERH-E02':
        n, q, a, woord = verh_e02(x); l1 = x['conceptHints']['L1'].get(nk['nieuw']) or ''
        VW[x['id']] = {'woord': woord, 'woordInL1': f' {woord} ' in f' {l1} ' and not re.search(r'\b(koekjes|appels|snoepjes|knikkers)\b', l1.replace(woord, '')), 'teller': n, 'tellerMinstens2': n >= 2, 'waarde': v == a * n}
    for k_, ok_ in VW.get(x['id'], {}).items():
        if ok_ is False: F.append(f"{x['id']}: voorwaarde {k_} klopt niet ({nk['nieuw']})")
# rang per somtype (zelfde regel als rang_goed/rang_open in kritisch_concept.py) + beide kanten
som = collections.defaultdict(list); kant = collections.defaultdict(set)
for x in XS:
    T = goed(x); ws = sorted({w(x['bewering'])} | {w(o['tekst']) for o in x['opties'] if o['tekst'].startswith('Nee')})
    som[(x['doelId'], x['somtypeNrOrigineel'])].append(('klein', 'midden', 'groot')[ws.index(T)] if len(ws) == 3 and T in ws else '?')
    for v in ws:
        if v != T: kant[(x['doelId'], x['somtypeNrOrigineel'])].add('laag' if v < T else 'hoog')
RANG = {f"{k[0]} #{k[1]}": dict(collections.Counter(v)) for k, v in som.items()}
for k, c in RANG.items():
    if max(c.values()) > 2 or '?' in c: F.append(f"rang {k}: {c}")
for k, s in kant.items():
    if s != {'laag', 'hoog'}: F.append(f"{k[0]} #{k[1]}: afleiders maar aan één kant {s}")
snap = {x['id']: sorted(o['tekst'] for o in x['opties']) + [x['conceptHints'].get('L1')] + ([VW[x['id']]] if x['id'] in VW else []) for x in XS}
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP {k}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
print('INFO rang', RANG)
for f in F[:30]: print('FAIL', f)
print(f"check V-#1081 andere kant: FAIL {len(F)}" + (f' (MUT={MUT})' if MUT else ''))
