import os, glob, json
def g5(B): return next(os.path.join(B, n) for n in ('claude-aanvulling/groep5', 'groep5', 'g5') if os.path.isdir(os.path.join(B, n)))
def items(G):
    I = {}
    for p in glob.glob(os.path.join(G, 'data', 'per_doel', '*.json')):
        for x in json.load(open(p, encoding='utf-8'))['items']: I.setdefault((x['doelId'], x['merge'].get('somtypeNrOrigineel')), []).append(x)
    return I
def schrijf(P, t, D):
    nt = json.dumps(D, ensure_ascii=False, indent=1); open(P, 'w', encoding='utf-8').write(nt + ('\n' if t.endswith('\n') and not nt.endswith('\n') else ''))
