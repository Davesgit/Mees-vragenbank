#!/usr/bin/env python3
"""Maakt claude-merge/hints_todo.md: per groep en doel de somtypes zonder 'Status: hints klaar' (dezelfde telling als gN/check_hints.py),
met sleutel (nrOrigineel), aantal items en een voorbeelditem uit gN/data/per_doel. Alleen lezen, behalve hints_todo.md."""
import importlib.util, glob, os, json, collections, datetime
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'claude-aanvulling')  # repo: claude-aanvulling/groepN
out = []; tot = {}
for g in (4, 5, 6, 7, 8):
    B = f'{ROOT}/groep{g}'
    sp = importlib.util.spec_from_file_location(f'ch{g}', f'{B}/check_hints.py'); CH = importlib.util.module_from_spec(sp)
    import sys; sys.path.insert(0, B); sp.loader.exec_module(CH); sys.path.remove(B)
    rij = []; n_klaar = 0
    for p in sorted(glob.glob(f'{B}/somtypen/G{g}-*.md')):
        doel = os.path.basename(p)[:-3]
        per = f'{B}/data/per_doel/{doel}.json'; its = json.load(open(per))['items'] if os.path.exists(per) else []
        for s in CH.sections(p):
            if s['status'] == 'hints klaar': n_klaar += 1; continue
            xs = [i for i in its if i['merge']['somtype'] == s['somtype']]
            g8 = sum(1 for i in xs if i['merge'].get('uitG8') or '-claude-bank-naar-' in i['id'] or '-claude-bank-terug-' in i['id'])
            rij.append((doel, s, xs, g8))
    tot[g] = (n_klaar, len(rij), sum(len(x) for _, _, x, _ in rij))
    out += [f'## G{g} — {len(rij)} somtypes open · {tot[g][2]} items', '']
    for doel, R in groupby if False else []: pass
    per_doel = collections.OrderedDict()
    for r in rij: per_doel.setdefault(r[0], []).append(r)
    for doel, R in per_doel.items():
        out += [f'### {doel} — {len(R)} somtypes · {sum(len(x) for _, _, x, _ in R)} items', '',
                '| nr | sleutel (nrOrigineel) | somtype | items | waarvan G8-aanvulling | voorbeelditem |', '|---|---|---|---|---|---|']
        for _, s, xs, g8 in R:
            ex = xs[0] if xs else None
            vb = '—' if not ex else f"`{ex['id']}`: {ex['opgave'][:110].replace('|', '/')}{'…' if len(ex['opgave']) > 110 else ''} → **{str(ex['antwoord']).replace('|', '/')}**"
            out.append(f"| {s['nr']} | {s['sleutel'][0] if s['sleutel'] else '?'} | {s['somtype'][:90].replace('|', '/')} | {len(xs)} | {g8 or ''} | {vb} |")
        out.append('')
kop = ['# Hints nog te schrijven (somtypes zonder hints)', '',
       f"Gemaakt {datetime.datetime.now():%Y-%m-%d %H:%M} (Amsterdam) met `tools/maak_hints_todo.py`. De telling is dezelfde als `gN/check_hints.py`: een somtype zonder 'Status: hints klaar' telt als open.",
       "Elke entry in `hints/batch*.json` koppelt op **doel + nrOrigineel** (de sleutel hieronder), niet op het volgnummer. 'Waarvan G8-aanvulling' telt de items die uit de G8-pool kwamen (`aanvulling_uit_g8.json`, inclusief de 46 terug-G7).", '',
       '| groep | hints klaar | open somtypes | items in open somtypes |', '|---|---|---|---|'] + \
      [f'| G{g} | {k} | {o} | {n} |' for g, (k, o, n) in tot.items()] + ['']
open(f'{ROOT}/hints_todo.md', 'w').write('\n'.join(kop + out) + '\n')
print(tot)
