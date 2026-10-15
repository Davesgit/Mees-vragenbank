#!/usr/bin/env python3
"""Check Z-#1090 op een toegepaste G5-kopie (na de r13-merge-hooks, zet_z1090, sync + apply). [MUT=..] [SNAP=1] python3 check_z1090.py <basis met g5>
Over ALLE G5-teksten (entries + items): geen bedrag-verschil ('(één) tiental/tien/tien cent/(één) euro/stapje van tien te veel/weinig'); per regel uit
logs/z1090_scope.json: richting per sleutel (te veel → sleutel > antwoord, te weinig → <), geen cijfer, 'Bijna' weg, zegt waar je moet kijken; muntvorm
('munten van tien cent') alleen als 10 in visual.jsRender.munten; SNAP per regel (soort, richting, aantal sleutels, tekst) in snap_z1090.json."""
import json, os, re, sys, glob
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; SNAPF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snap_z1090.json')
G5 = next(os.path.join(B, d) for d in ('g5', 'groep5', 'claude-aanvulling/groep5') if os.path.isdir(os.path.join(B, d)))
BEDRAG = re.compile(r'\b(?:(?:één|een) )?(?:stapje van tien|tiental|tien cent|tien|euro)\s+te\s+(?:veel|weinig)\b', re.I)
KIJK = re.compile(r'tiental|tientallen|eenheden|centen|euro|stukken|stapjes|munten|afgerond|getallen|verdeling|verdeel', re.I)
def waarde(s):
    s = str(s or '').strip(); m = re.search(r'(€\s?)?(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d+))?(\s*cent)?', s)
    if not m: return None
    v = int(m.group(2).replace('.', '')) + (int(m.group(3)) / 10 ** len(m.group(3)) if m.group(3) else 0)
    return v / 100 if m.group(4) and not m.group(1) else v
def foto(x):
    vis = x.get('visual') or {}; jr = (vis.get('jsRender') or {}) if isinstance(vis, dict) else {}
    return jr.get('munten') if jr.get('soort') == 'geld' and isinstance(jr.get('munten'), list) else None
_sp = os.path.join(G5, 'logs', 'z1090_scope.json'); SCOPE = json.load(open(_sp, encoding='utf-8')) if os.path.exists(_sp) else []   # zonder hook: alleen de guard
UITGESLOTEN = {('G5-GET-E05', 32, 'tiental te weinig'), ('G5-GET-E05', 32, 'tiental te veel')}      # Z-#1075 (zie zet_z1090)
SCOPE = [sc for sc in SCOPE if (sc['doel'], sc['nro'], sc['soort']) not in UITGESLOTEN]
ENT = {}
for p in sorted(glob.glob(os.path.join(G5, 'hints', 'batch*.json'))):
    for s in json.load(open(p, encoding='utf-8'))['somtypen']: ENT[(s['doel'], s['nrOrigineel'])] = s
ITEMS = {}
for p in sorted(glob.glob(os.path.join(G5, 'data', 'per_doel', '*.json'))):
    for x in json.load(open(p, encoding='utf-8'))['items']: ITEMS.setdefault((x['doelId'], x['merge'].get('somtypeNrOrigineel')), []).append(x)
T1040 = 'Dat is te weinig. Tel de tientallen nog eens bij elkaar.'      # Oef-#1040 (zet_oef1040): #17 'honderdtal vergeten' heet dan 'tiental te weinig'
HERNOEMD = {('G5-GET-E05', 17, 'honderdtal vergeten'): 'tiental te weinig'}
V1120 = (' (geleend)', ' (onthouden)')      # V-#1120 (zet_lenen): de regel is gesplitst per item; de uitlegtekst staat dan in de soort met dit achtervoegsel
def sleutels(sc): return [(x, k) for x in ITEMS.get((sc['doel'], sc['nro']), []) for k in x['foutHints'] if k['soort'] in {sc['soort'], sc['soort'] + ' (munt op de foto)'} | {sc['soort'] + e for e in V1120}]
S0 = next((sc for sc in SCOPE if sc['richting'] == 'weinig' and sleutels(sc)), None); x0, k0 = sleutels(S0)[0] if S0 else (None, None)
if MUT == 'M_richting': k0['uitleg'] = re.sub(r'^Dat is te weinig', 'Dat is te veel', k0['uitleg'])
if MUT == 'M_munt':     k0['uitleg'] = k0['uitleg'] + ' Kijk nog eens naar de munten van tien cent.'
if MUT == 'M_bedrag':   k0['uitleg'] = re.sub(r'^Dat is te weinig', 'Dat is één tiental te weinig', k0['uitleg'])
if MUT == 'M_cijfer':   k0['uitleg'] = k0['uitleg'] + ' Tel er 10 bij.'
if MUT == 'M_kijk':     k0['uitleg'] = 'Dat is te weinig.'
if MUT == 'M_entry':    next(f for f in ENT[(S0['doel'], S0['nro'])]['foutHints'] if f['soort'] == S0['soort'])['tekst'] = 'Bijna! Dat is tien te weinig.'
if MUT == 'M_snap':     next(f for f in ENT[(S0['doel'], S0['nro'])]['foutHints'] if f['soort'] == S0['soort'])['tekst'] += ' Reken goed.'
# guard over alle G5-teksten
for k_, s in ENT.items():
    for f in s['foutHints']:
        for kk in ('tekst', 'tekstSterker'):
            if BEDRAG.search(f.get(kk) or ''): F.append(f"Z-#1090 G5 entry {k_[0]} #{k_[1]} {f['soort']!r} [{kk}]: noemt het verschil: {(f.get(kk) or '')[:70]}")
for k_, its in ITEMS.items():
    for x in its:
        for k in x['foutHints']:
            for kk in ('uitleg', 'uitlegSterker'):
                if BEDRAG.search(k.get(kk) or ''): F.append(f"Z-#1090 G5 {x['doelId']} #{k_[1]} {x['nr']} sleutel {k['fout']!r} [{kk}]: noemt het verschil: {(k.get(kk) or '')[:70]}")
            if 'munten van tien cent' in (k.get('uitleg') or '') and 10 not in (foto(x) or []):
                F.append(f"Z-#1090 G5 {x['doelId']} #{k_[1]} {x['nr']} sleutel {k['fout']!r}: muntvorm 'tien cent' maar die munt ligt niet op de foto")
# per regel
snap = {}
for sc in SCOPE:
    h_ = HERNOEMD.get((sc['doel'], sc['nro'], sc['soort']))
    if h_ and not any(f['soort'] == sc['soort'] for f in ENT[(sc['doel'], sc['nro'])]['foutHints']) and any(f['soort'] == h_ and f['tekst'] == T1040 for f in ENT[(sc['doel'], sc['nro'])]['foutHints']):
        HERN_OK = True; sc = dict(sc, soort=h_, _snapsleutel=f"{sc['doel']}#{sc['nro']} {sc['soort']}")
    kk = sleutels(sc); e = ENT[(sc['doel'], sc['nro'])]; fe = next((f for f in e['foutHints'] if f['soort'] == sc['soort']), None)
    fs = next((f for f in e['foutHints'] for x_ in V1120 if f['soort'] == sc['soort'] + x_), None)      # V-#1120: SNAP blijft de uitlegtekst van Z-#1090
    snap[sc.get('_snapsleutel') or f"{sc['doel']}#{sc['nro']} {sc['soort']}"] = [sc['richting'], len(kk), (fs or fe) and (fs or fe)['tekst']]
    for x, k in kk:
        u = k.get('uitleg') or ''; a, v = waarde(x['antwoord']), waarde(k['fout'])
        if a is not None and v is not None and ((u.startswith('Dat is te veel') and v <= a) or (u.startswith('Dat is te weinig') and v >= a)):
            F.append(f"Z-#1090 {x['doelId']} #{sc['nro']} {x['nr']} sleutel {k['fout']!r}: richting klopt niet (antwoord {x['antwoord']}): {u[:50]}")
        if re.search(r'\d', u): F.append(f"Z-#1090 {x['doelId']} #{sc['nro']} {x['nr']} sleutel {k['fout']!r}: cijfer in de tekst (verklapt)")
        if not KIJK.search(u): F.append(f"Z-#1090 {x['doelId']} #{sc['nro']} {x['nr']} sleutel {k['fout']!r}: zegt niet waar je moet kijken: {u[:50]}")
        if re.search(r'\bBijna\b', u): F.append(f"Z-#1090 {x['doelId']} #{sc['nro']} {x['nr']} sleutel {k['fout']!r}: 'Bijna' (zegt dat het verschil klein is)")
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    oud = {k: v for k, v in json.load(open(SNAPF, encoding='utf-8')).items() if not any(k == f'{d}#{n} {so}' for d, n, so in UITGESLOTEN)}
    for (d_, n_, so_) in HERNOEMD:
        k_ = f'{d_}#{n_} {so_}'
        if k_ in oud and k_ in snap and snap[k_][2] == T1040: oud[k_] = [oud[k_][0], oud[k_][1], T1040]      # Oef-#1040 gezet: zelfde richting en sleutels, nieuwe tekst
    F += [f"SNAP Z-#1090 {k}: {oud.get(k)} → {snap.get(k)}" for k in sorted(set(oud) | set(snap)) if oud.get(k) != snap.get(k)]
print(f"INFO {len(SCOPE)} regels, {sum(v[1] for v in snap.values())} sleutels (veel {sum(v[1] for v in snap.values() if v[0] == 'veel')}, weinig {sum(v[1] for v in snap.values() if v[0] == 'weinig')})")
for f in F[:40]: print('FAIL', f)
print(f'check Z-#1090: FAIL {len(F)}' + (f' (MUT={MUT})' if MUT else ''))
