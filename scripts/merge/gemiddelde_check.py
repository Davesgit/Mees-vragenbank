"""Didactiek G8 batch 3 (V-#820/Z-#823, les 195): bij een gemiddelde-vraag mag het goede antwoord geen gegeven waarde uit de vraag zijn
(dan heeft wie de meest voorkomende of middelste waarde kiest toevallig goed), en het mag niet de middelste optie zijn terwijl de andere
opties onmogelijk zijn (buiten de kleinste en grootste gegeven waarde: een gemiddelde ligt daar altijd tussen). WARN.
Gebruik: import gemiddelde_check as GM; n = GM.rapport(items)."""
import re
def _getal(t):
    m = re.search(r'\d+(?:\.\d{3})*(?:,\d+)?', str(t or ''))
    return float(m.group(0).replace('.', '').replace(',', '.')) if m else None
def treffers(items):
    W = []
    for it in items:
        o = it.get('opgave') or ''
        if not re.search(r'\bgemiddeld(e)?\b', o, re.I) or re.search(r'gemiddeld \d', o): continue      # 'heeft gemiddeld 5' = gegeven gemiddelde
        if not re.fullmatch(r'\d+(?:\.\d{3})*(?:,\d+)?(?: [a-z]+)?', str(it.get('antwoord') or '').strip()): continue   # alleen een getal (met eenheid) als antwoord
        a = _getal(it.get('antwoord'))
        G = r'\d+(?:\.\d{3})*(?:,\d+)?(?: [a-z]+)?'
        lijst = re.search(rf'(?<!\d)(?<!\d,){G}(?:, {G})+ en {G}', o)          # een opsomming '6, 6, 3, 3 en 7' = de gegeven waarden (niet het aantal ervoor)
        bron = lijst.group(0) if lijst else o
        waarden = [float(x.replace('.', '').replace(',', '.')) for x in re.findall(r'(?<!\d)(?<!\d,)\d+(?:\.\d{3})*(?:,\d+)?(?!\d|,\d)', bron)]
        if a in waarden: W.append(f"{it['id']}: het gemiddelde {it['antwoord']} staat ook als gegeven waarde in de vraag"); continue
        ops = [_getal(x.get('tekst')) for x in it.get('opties') or []]
        if len(ops) >= 3 and None not in ops and waarden:
            lo, hi = min(waarden), max(waarden); rest = [x for x in ops if x != a]
            if sorted(ops)[len(ops) // 2] == a and all(x < lo or x > hi for x in rest):
                W.append(f"{it['id']}: het goede antwoord {it['antwoord']} is de middelste optie en de andere opties ({', '.join(str(x.get('tekst')) for x in it['opties'] if _getal(x.get('tekst')) != a)}) liggen buiten {lo:g}–{hi:g}")
    return W
def rapport(items, toon=True):
    W = treffers(items)
    if toon:
        print(f"\nGEMIDDELDE (V-#820/Z-#823: gemiddelde = gegeven waarde, of middelste optie met onmogelijke afleiders): {len(W)} (WARN)")
        for x in W[:10]: print('  WARN GEMIDDELDE', x)
    return len(W)
