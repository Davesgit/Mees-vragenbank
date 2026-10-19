"""G8-paden voor de r20-hooks en checks (Oefeningen). g8(B): B is een repo-kopie (met claude-aanvulling/groep8) of de groep8-map zelf."""
import json, os, glob
def g8(B):
    for p in (os.path.join(B, 'claude-aanvulling', 'groep8'), B):
        if os.path.isdir(os.path.join(p, 'hints')) and os.path.isdir(os.path.join(p, 'data', 'per_doel')): return p
    raise SystemExit(f'geen groep8 in {B}')
def items(G):
    I = {}
    for P in sorted(glob.glob(os.path.join(G, 'data', 'per_doel', 'G8-*.json'))):
        D = json.load(open(P, encoding='utf-8')); its = D['items'] if isinstance(D, dict) else D
        for x in its: I.setdefault(x['doelId'], []).append(x)
    return I
def entries(G):
    return [(P, s) for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(P, encoding='utf-8'))['somtypen']]
def schrijf(P, oud, D):
    """schrijf D terug in het formaat van de oude tekst (indent en eind-newline zoals oud)"""
    for ind in (1, 2, 0, None, 4):
        if json.dumps(json.loads(oud), ensure_ascii=False, indent=ind) == oud.rstrip('\n'): break
    else: raise SystemExit(f'{P}: formaat niet herkend; niets geschreven')
    open(P, 'w', encoding='utf-8').write(json.dumps(D, ensure_ascii=False, indent=ind) + ('\n' if oud.endswith('\n') else ''))
