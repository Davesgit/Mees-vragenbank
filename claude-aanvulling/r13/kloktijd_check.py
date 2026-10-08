"""Z-#782 (Didactiek G8 batch 2, 8 okt; les 243) + besluit kloktijden (Didactiek 15:46): een kloktijd schrijf je als '15.00 uur', niet met ':'.
FAIL, ook bij typ-invoer. Alleen items met `digitaleKlok: true` (een echte digitale klok in beeld of in de zin) worden overgeslagen.
Kijkt in de kindteksten: opgave, antwoord, opties, hint, sterkereHint, ouderzin, foutHints (uitleg/uitlegSterker), algemeneFoutHint.
Patroon \\b\\d{1,2}:\\d{2}\\b; 'schaal 1 : 100' (met spaties) en '1:100' na 'schaal' tellen niet.
Gebruik: import kloktijd_check as KT; n = KT.rapport(items, ernst='FAIL')."""
import re
KLOK = re.compile(r'(?<![\d:])(\d{1,2}):(\d{2})(?![\d:])')
def teksten(it):
    yield 'kop', (it.get('merge') or {}).get('somtype'); yield 'opgave', it.get('opgave'); yield 'antwoord', it.get('antwoord')
    for o in it.get('opties') or []: yield 'optie', o.get('tekst') if isinstance(o, dict) else o
    for k in ('hint', 'sterkereHint', 'ouderzin', 'algemeneFoutHint'):
        v = it.get(k)
        if isinstance(v, dict): v = ' '.join(str(x) for x in v.values() if isinstance(x, str))
        yield k, v
    for f in it.get('foutHints') or []:
        for k in ('uitleg', 'uitlegSterker'): yield 'foutHint', f.get(k)
    for f in it.get('foutRegels') or []:
        for k in ('tekst', 'tekstSterker'): yield 'foutRegel', f.get(k)
def treffers(items):
    T = []
    for it in items:
        if it.get('digitaleKlok'): continue
        for veld, t in teksten(it):
            if not isinstance(t, str): continue
            if veld == 'kop':
                if '#:#' in t: T.append((it, f"{it['id']} [kop]: '#:#' in «{t[:70]}»")); break
                continue
            for m in KLOK.finditer(t):
                if veld == 'kop': continue
                if re.search(r'schaal\s*$', t[:m.start()], re.I): continue
                if int(m.group(1)) > 24 or int(m.group(2)) > 59: continue
                T.append((it, f"{it['id']} [{veld}]: {m.group(0)} in «{t[max(0, m.start() - 30):m.end() + 20]}»")); break
    return T
def invoer(it):
    """typ-invoer van een tijd ('(Typ als 14:30.)'): de motor en de app lezen 'uu:mm'; omzetten vraagt eerst motorsteun → WARN, niet FAIL"""
    return '(Typ als' in (it.get('opgave') or '')
def rapport(items, ernst='FAIL', toon=True):
    T = treffers(items); F = [x for it, x in T]; W = []; D = sum(1 for it in items if it.get('digitaleKlok'))
    if toon:
        print(f"\nKLOKTIJD (Z-#782: kloktijd met ':' in een kindtekst; schrijf '15.00 uur'): {len(F)} ({ernst}) · overgeslagen met digitaleKlok: {D}")
        for x in F[:15]: print(f'  {ernst} KLOKTIJD', x)
        for x in W[:3]: print('  WARN KLOKTIJD-INVOER', x)
    return len(F)
