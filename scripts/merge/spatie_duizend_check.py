#!/usr/bin/env python3
"""V-#705 (review G7 batch 6, Didactiek 8 okt, les 218): een spatie als duizendtalscheiding ('100 000', '1 000') is FAIL.
Huisregel: vanaf 10.000 met een punt ('100.000'). Kijkt in opgave, antwoord, opties, H1/H2, ouderzin, fout-hints, Claudes uitleg en
Claudes fout-hints. Gebruik: rapport(items) → aantal (check_merge_notatie G4–G8)."""
import re
RX = re.compile(r'(?<![\d,.])\d{1,3}(?: \d{3})+(?![\d,])')
def _velden(it):
    e = it.get('extraVelden') or {}
    yield 'opgave', it.get('opgave') or ''
    yield 'antwoord', str(it.get('antwoord') or '')
    yield 'opties', it.get('optiesTekst') or ''
    for k in ('hint', 'sterkereHint', 'ouderzin', 'algemeneFoutHint'): yield k, it.get(k) or ''
    for f in it.get('foutHints') or []: yield 'foutHints', (f.get('tekst') or f.get('uitleg') or '')
    yield 'claudeUitleg', e.get('claudeUitleg') or ''
    for f in e.get('claudeFoutHints') or []: yield 'claudeFoutHints', f.get('uitleg') or ''
def fouten(items):
    out = []
    for it in items:
        for k, v in _velden(it):
            if not isinstance(v, str): continue
            for m in RX.finditer(v): out.append((it.get('id'), k, m.group(0)))
    return out
def rapport(items):
    f = fouten(items)
    print(f"\nV-#705 spatie als duizendtalscheiding: {len(f)} (FAIL)")
    for x in f: print('  FAIL V-#705 %s [%s]: %r (schrijf met een punt)' % x)
    return len(f)

def bestanden(root):
    """Oef-#481 (8 okt): ook de hintteksten buiten de items: hints/batch*.json (alle tekstvelden, ook claudeTekst) en somtypen/*.md (oude Claude-fout-hints)."""
    import glob, json, os
    out = []
    def walk(o, pad, f):
        if isinstance(o, dict):
            for k, v in o.items(): walk(v, f'{pad}.{k}', f)
        elif isinstance(o, list):
            for n, v in enumerate(o): walk(v, f'{pad}[{n}]', f)
        elif isinstance(o, str):
            for m in RX.finditer(o): out.append((os.path.relpath(f, root), pad[-60:], m.group(0)))
    for f in sorted(glob.glob(os.path.join(root, 'hints', 'batch*.json'))): walk(json.load(open(f)), '', f)
    for f in sorted(glob.glob(os.path.join(root, 'somtypen', '*.md'))):
        for n, regel in enumerate(open(f), 1):
            for m in RX.finditer(regel): out.append((os.path.relpath(f, root), f'r.{n}', m.group(0)))
    return out
def rapport_bestanden(root):
    f = bestanden(root)
    print(f"\nV-#705/Oef-#481 spatie als duizendtalscheiding in hints/batch*.json en somtypen/*.md: {len(f)} (FAIL)")
    for x in f[:15]: print('  FAIL V-#705 %s [%s]: %r (schrijf met een punt)' % x)
    return len(f)
