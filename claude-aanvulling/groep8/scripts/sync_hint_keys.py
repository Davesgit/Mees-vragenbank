#!/usr/bin/env python3
"""[G8-kopie 1 okt 18:15 van de G7-versie; BASE = claude-merge/g8.] G7 (kopie van g5/scripts/sync_hint_keys.py met #30, 1 okt 17:00; BASE = claude-merge/g7): houdt 'nr' en 'somtype' in hints/batch*.json gelijk aan de koppen in somtypen/<doel>.md na een nieuwe build.
Naar g3/scripts/sync_hint_keys.py (build 13:59), met de tip van Oefeningen: elk somtype heeft vanaf de eerste build
nrOrigineel + somtypeOrigineel (bevroren/somtype_nr_v1.json, sleutel doel#nrOrigineel).
Koppeling per hint-entry:
  1. op claudeId: de items die in de bevroren indeling onder (doel, nrOrigineel) zaten → de kop waar die nu staan;
  2. anders op de kop: items met merge.somtype of merge.somtypeOrigineel = somtypeOrigineel (of de 'somtype' uit de entry).
Een entry zonder nrOrigineel/somtypeOrigineel krijgt die van de items onder zijn huidige kop (eerste sync).
Wijkt de nieuwe kop af van somtypeOrigineel → 'kopGewijzigd' (apply_hints.py zet dan LET OP in de md).
Merge-fixlijst #30 (1 okt 16:55): vallen twee entries op dezelfde kop (samengevoegd somtype), dan blijven ze ongewijzigd en staat het
als probleem in logs/hint_sleutels.json; check_hints.py geeft dan FAIL. Nooit stil samenvoegen.
Rerunbaar. Gebruik: python3 scripts/sync_hint_keys.py"""
import json, re, glob, os, collections, datetime
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = {}
for p in sorted(glob.glob(f'{BASE}/bevroren/somtype_nr_v*.json')):
    SNAP[os.path.basename(p)[len('somtype_nr_'):-5]] = json.load(open(p))['sleutels']
items = json.load(open(f'{BASE}/data/gemapt.json'))['items']
def koppen(doel):
    p = f'{BASE}/somtypen/{doel}.md'
    if not os.path.exists(p): return {}
    return {m.group(2).strip(): int(m.group(1)) for m in re.finditer(r'^## Somtype (\d+): (.*)$', open(p, encoding='utf-8').read(), re.M)}
def bevroren_ids(doel, nro, kop):
    for v in sorted(SNAP, reverse=False):
        e = SNAP[v].get(f'{doel}#{nro}')
        if e and (kop is None or e['somtypeOrigineel'] == kop): return set(e['claudeIds']), v
    # build 8 okt (V-#820): een entry kan als somtypeOrigineel de opgeschoonde kop dragen (Oef-#488/kop_g8) i.p.v. de bevroren kop;
    # is doel#nrOrigineel in precies één bevroren versie bekend, dan is dat de sleutel (bevroren sleutels veranderen nooit)
    kand = [(v, SNAP[v][f'{doel}#{nro}']) for v in SNAP if f'{doel}#{nro}' in SNAP[v]]
    if kop is not None and len(kand) == 1: return set(kand[0][1]['claudeIds']), kand[0][0]
    return set(), None
problemen = []; bezet = collections.defaultdict(list); vandaag = datetime.date.today().isoformat()
batches = sorted(glob.glob(f'{BASE}/hints/batch*.json'))
# merge-fixlijst #30 (Didactiek batch 2, 1 okt 16:50): nooit stil samenvoegen. Pas 1 rekent per entry de nieuwe kop uit; vallen twee
# of meer entries op dezelfde kop (een samengevoegd somtype), dan blijven die entries ONGEWIJZIGD en is het een probleem (check_hints: FAIL).
plan = []; geladen = {path: json.load(open(path, encoding='utf-8')) for path in batches}
for path in batches:
    data = geladen[path]; naam = os.path.basename(path)
    for st in data.get('somtypen', []):
        doel = st['doel']
        if 'somtypeOrigineel' not in st or 'nrOrigineel' not in st:
            bij = [it for it in items if it['merge']['doel'] == doel and it['merge']['somtype'] == st.get('somtype')] or \
                  [it for it in items if it['merge']['doel'] == doel and it['merge'].get('somtypeNr') == st.get('nr')]
            if not bij: problemen.append(f"{naam} {doel} nr {st.get('nr')}: geen items om nrOrigineel/somtypeOrigineel van over te nemen"); continue
            st['nrOrigineel'] = bij[0]['merge']['somtypeNrOrigineel']; st['somtypeOrigineel'] = bij[0]['merge']['somtypeOrigineel']
        ids, v = bevroren_ids(doel, st['nrOrigineel'], st['somtypeOrigineel'])
        nieuw = collections.Counter(it['merge']['somtype'] for it in items if it['bron']['claudeId'] in ids and it['merge']['doel'] == doel); hoe = 'claudeId'
        if not nieuw:
            nieuw = collections.Counter(it['merge']['somtype'] for it in items if it['merge']['doel'] == doel and
                                        (st['somtypeOrigineel'] in (it['merge']['somtype'], it['merge'].get('somtypeOrigineel')) or it['merge']['somtype'] == st.get('somtype'))); hoe = 'kop'
        if not nieuw: problemen.append(f"{naam} {doel} '{st['somtypeOrigineel']}': geen items meer met dit somtype"); continue
        kop = nieuw.most_common(1)[0][0]; K = koppen(doel)
        if len(nieuw) > 1: problemen.append(f"{naam} {doel} '{st['somtypeOrigineel']}': items verdeeld over {dict(nieuw)}; hints op '{kop}'")
        if kop not in K: problemen.append(f"{naam} {doel} '{kop}': kop niet in de md"); continue
        bezet[(doel, kop)].append(f"{naam}#{st['nrOrigineel']}")
        plan.append((path, st, kop, K[kop], hoe))
botsing = {k for k, w in bezet.items() if len(w) > 1}
for (doel, kop) in botsing:
    problemen.append(f"{doel} '{kop}': meer dan één hint-entry ({', '.join(bezet[(doel, kop)])}); NIET samengevoegd: de entries blijven op hun oude kop. "
                     f"Splits het somtype weer, of schrijf één nieuwe entry voor de samengevoegde kop.")
per_bestand = collections.defaultdict(int)
for path, doelst, kop, nr, hoe in plan:
    if (doelst['doel'], kop) in botsing: continue
    if doelst.get('somtype') != kop or doelst.get('nr') != nr: per_bestand[path] += 1
    if kop != doelst['somtypeOrigineel']:
        if (doelst.get('kopGewijzigd') or {}).get('naar') != kop: doelst['kopGewijzigd'] = {'van': doelst['somtypeOrigineel'], 'naar': kop, 'op': vandaag}
    else: doelst.pop('kopGewijzigd', None)
    doelst['somtype'] = kop; doelst['nr'] = nr; doelst['koppeling'] = hoe
for path in batches:
    json.dump(geladen[path], open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"{os.path.basename(path)}: {len(geladen[path].get('somtypen', []))} somtypes, {per_bestand[path]} sleutels bijgewerkt")
for p in problemen: print('LET OP', p)
if not batches: print('sync_hint_keys: nog geen hints/batch*.json (G8: alle somtypen open)')
import hashlib
indeling = hashlib.md5(json.dumps(sorted((it['bron']['claudeId'], it['merge']['doel'], it['merge']['somtype']) for it in items), ensure_ascii=False).encode()).hexdigest()
json.dump({'problemen': problemen, 'batches': [os.path.basename(b) for b in batches], 'indeling': indeling}, open(f'{BASE}/logs/hint_sleutels.json', 'w'), ensure_ascii=False, indent=1)
