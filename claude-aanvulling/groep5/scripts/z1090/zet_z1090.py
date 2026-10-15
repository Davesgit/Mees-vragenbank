#!/usr/bin/env python3
"""Hook Z-#1090 (zacht, Didactiek 20:28) — APARTE RONDE NA DE r13-MERGE (niet ervoor). NIET door Oefeningen geplaatst.
G5: fout-hints die het precieze verschil noemen («Dat is één tiental te weinig», «tien te veel», «tien cent te veel», «één euro te veel», «één stapje
van tien te weinig») verklappen het antwoord. Nieuw: alleen de richting en waar je moet kijken: «Dat is te weinig. <rest van de tekst>», met 'Let op de
tientallen.' (of 'Tel de centen nog eens na.' / 'Tel de hele euro's nog eens.') als de rest nergens zegt waar je moet kijken. 'Bijna!' valt weg.
Geld: «Kijk nog eens naar de munten van tien cent.» alleen als die munt op de foto ligt (visual.jsRender.munten) en de motor de binding van Z-#1076 heeft:
dan splitst de regel in '(op de foto)' (muntvorm) en '(niet op de foto)' (neutraal); anders neutraal.
Voorwaardelijk per regel: de richting wordt per item nagerekend op de sleutels van die soort (één sleutel de verkeerde kant op = regel niet gezet + MELD).
Idempotent (de oude vorm staat er daarna niet meer). Gebruik: python3 zet_z1090.py [basis met g5/groep5] [--droog]"""
import json, os, re, sys, glob, copy
A = [x for x in sys.argv[1:] if not x.startswith('--')]; B = A[0] if A else '.'; DROOG = '--droog' in sys.argv
G5 = next(os.path.join(B, n) for n in ('claude-aanvulling/groep5', 'groep5', 'g5') if os.path.isdir(os.path.join(B, n)))
START = re.compile(r'^(?:Bijna! )?Dat is (?:(?:één|een) )?(stapje van tien|tiental|tien cent|tien|euro) te (veel|weinig)\.\s*(.*)$')
KIJK = re.compile(r'tiental|tientallen|eenheden|centen|euro|stukken|stapjes|munten|afgerond|getallen|verdeling|verdeel', re.I)
LOOK = {'stapje van tien': 'Let op de tientallen.', 'tiental': 'Let op de tientallen.', 'tien': 'Let op de tientallen.', 'tien cent': 'Tel de centen nog eens na.', 'euro': "Tel de hele euro's nog eens."}
MUNT = 'Kijk nog eens naar de munten van tien cent.'
def waarde(s):
    s = str(s or '').strip(); m = re.search(r'(€\s?)?(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d+))?(\s*cent)?', s)
    if not m: return None
    v = int(m.group(2).replace('.', '')) + (int(m.group(3)) / 10 ** len(m.group(3)) if m.group(3) else 0)
    return v / 100 if m.group(4) and not m.group(1) else v
def foto(x):
    vis = x.get('visual') or {}; jr = (vis.get('jsRender') or {}) if isinstance(vis, dict) else {}
    return jr.get('munten') if jr.get('soort') == 'geld' and isinstance(jr.get('munten'), list) else None
ITEMS = {}
for p in glob.glob(os.path.join(G5, 'data', 'per_doel', '*.json')):
    for x in json.load(open(p, encoding='utf-8'))['items']: ITEMS.setdefault((x['doelId'], x['merge'].get('somtypeNrOrigineel')), []).append(x)
GEBONDEN = '_munten_foto1076' in open(os.path.join(G5, 'scripts', 'fout_regels.py'), encoding='utf-8').read()
LOG, MELD, SCOPE = [], [], []
def nieuw(seg, soort, its):
    m = START.match(seg)
    if not m: return seg, None
    wat, rich, rest = m.groups()
    fout = [(x['nr'], k['fout']) for x in its for k in x['foutHints'] if k['soort'] == soort and waarde(k['fout']) is not None and waarde(x['antwoord']) is not None
            and ((waarde(k['fout']) <= waarde(x['antwoord'])) if rich == 'veel' else (waarde(k['fout']) >= waarde(x['antwoord'])))]
    if fout: MELD.append(f"{soort}: richting '{rich}' klopt niet bij {fout[:4]}; niet gezet"); return seg, None
    rest = rest.strip()
    if not KIJK.search(rest): rest = (LOOK[wat] + ' ' + rest).strip()
    return f'Dat is te {rich}. {rest}'.strip(), (wat, rich)
for P in sorted(glob.glob(os.path.join(G5, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        its = ITEMS.get((s['doel'], s['nrOrigineel']), []); uit = []
        for f in s['foutHints']:
            g = copy.deepcopy(f); info = None
            for k in ('tekst', 'tekstSterker'):
                if isinstance(g.get(k), str):
                    segs = [nieuw(z, f['soort'], its) for z in g[k].split(' / ')]
                    g[k] = ' / '.join(z for z, _ in segs); info = info or next((i for _, i in segs if i), None)
            if info:
                SCOPE.append({'doel': s['doel'], 'nro': s['nrOrigineel'], 'soort': f['soort'], 'wat': info[0], 'richting': info[1], 'sleutels': sum(k['soort'] == f['soort'] for x in its for k in x['foutHints'])})
                m10 = re.fullmatch(r'fout = antwoord ([+\-−]) 10 cent', f['regel'].strip())
                if info[0] == 'tien cent' and m10 and GEBONDEN and any(10 in (foto(x) or []) for x in its):
                    g1 = dict(g, soort=f['soort'] + ' (munt op de foto)', regel=f['regel'] + ' (op de foto)', tekst=f'Dat is te {info[1]}. {MUNT}')
                    g2 = dict(g, regel=f['regel'] + ' (niet op de foto)')
                    uit += [g1, g2]; LOG.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']}: gesplitst (munt op de foto / niet)"); continue
                LOG.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']}: {f['tekst'][:60]!r} → {g['tekst'][:70]!r}")
            uit.append(g)
        s['foutHints'] = uit
    if len(LOG) > n0 and not DROOG:
        nt = json.dumps(D, ensure_ascii=False, indent=1); open(P, 'w', encoding='utf-8').write(nt + ('\n' if t.endswith('\n') and not nt.endswith('\n') else ''))
if SCOPE and not DROOG: json.dump(SCOPE, open(os.path.join(G5, 'logs', 'z1090_scope.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1090; {sum(s['sleutels'] for s in SCOPE)} sleutels op {len(SCOPE)} regels){' [droog]' if DROOG else ''}" + ''.join('\n  ' + l for l in LOG))
