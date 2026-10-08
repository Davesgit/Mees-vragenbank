"""'even veel' in de betekenis 'evenveel' (Didactiek 21:25, G6-fixlijst #192): FAIL in alles wat kind of ouder ziet.
check_merge_notatie R/EVEN kijkt naar opgave, opties, antwoord en uitleg; dit kijkt ook naar ouderzin, hints, fout-hintteksten en de kop van het somtype.
Herkomstvelden (somtypeOrigineel, extraVelden.claude*, bron, *Voor*, 'van') tellen niet: die bewaren de tekst van de bron."""
import json, re
EVEN = re.compile(r'\b[Ee]ven veel\b')
HERKOMST = re.compile(r'^(somtypeOrigineel|bron|van|oud|claude.*|.*Voor\d*.*|.*Claude)$')
def _walk(x, pad, uit):
    if isinstance(x, dict):
        for k, v in x.items():
            if not HERKOMST.match(k): _walk(v, f'{pad}.{k}', uit)
    elif isinstance(x, list):
        for v in x: _walk(v, f'{pad}[]', uit)
    elif isinstance(x, str) and EVEN.search(x): uit.append((pad, x))
def rapport(items, toon=True):
    F = []
    for it in items:
        uit = []; _walk({k: v for k, v in it.items() if k != 'extraVelden'}, '', uit)
        F += [f"{it.get('id')} {p}: «{t[:90]}»" for p, t in uit]
    if toon:
        print(f"\nEVENVEEL ('even veel' → 'evenveel', ook ouderzin/hints/kop, #192): {len(F)} (FAIL)")
        for x in F[:15]: print('  FAIL EVENVEEL', x)
    return len(F)
