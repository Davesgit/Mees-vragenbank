"""#390-check (G6 merge-fixlijst #390, Didactiek gate ronde 9 deel B, les 115; gedeeld door check_merge_notatie G5–G8). Leest alleen.
FAIL: een fout-sleutel die gelijk is aan een getal uit de vraag en toch de ±1-regel of een tekst met 'Bijna!' krijgt.
Zo'n kind heeft geen rekenstap bijna goed gedaan, maar een getal uit de vraag overgenomen. De motor (fout_regels.in_vraag390) slaat die regels over."""
import re
PM1 = re.compile(r'^fout = (?:het )?antwoord ?(?:±|\+|-|−) ?1(?![\d,])(?! ?cent)')
def _nums(t):
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', t or '')
    return {int(x.replace('.', '')) for x in re.findall(r'(?<![\w:.])(?:\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|\.\d)', t)}
def _int(v):
    v = str(v).strip(); return int(v.replace('.', '')) if re.fullmatch(r'\d{1,3}(?:\.\d{3})+|\d+', v) else None
from fractions import Fraction as _F416
_GETAL416 = r'(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?(?:/\d+)?'
def waarde416(v):
    """D-#416: de waarde van een sleutel (heel getal, kommagetal of breuk; n/n = 1). None bij geld (€) of geen getal; een eenheid erachter mag."""
    v = str(v or '').strip()
    if v.startswith('€'): return None
    m = re.fullmatch(r'(' + _GETAL416 + r')(?:\s+[a-zA-Z]+)?', v)
    if not m: return None
    t = m.group(1); n, _, d = t.partition('/'); n = _F416(n.replace('.', '').replace(',', '.'))
    return n / int(d) if d else n
def vraag_waarden416(opg):
    """D-#416: alle getallen uit de vraag als waarde (ook kommagetallen en breuken), plus de losse hele getallen zoals vroeger."""
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', (opg or '').replace('\n', ' '))
    w = {waarde416(x) for x in re.findall(r'(?<![\w:.,/])' + _GETAL416 + r'(?![\w:/]|[.,]\d)', t)}
    w |= {_F416(int(x.replace('.', ''))) for x in re.findall(r'(?<![\w:.])(?:\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|\.\d)', t)}
    return {x for x in w if x is not None}
def vind(items):
    """D-#416: vergelijk op waarde (ook breuken en kommagetallen; n/n = 1), net als fout_regels.in_vraag390."""
    uit = []
    for it in items:
        n = vraag_waarden416(it.get('opgave')) | {_F416(x) for x in _nums((it.get('opgave') or '').replace('\n', ' '))}
        for f in it.get('foutHints') or []:
            x = waarde416(f.get('fout'))
            if x is None or x not in n: continue
            r = (f.get('regel') or '').lower().replace('−', '-').strip()
            if PM1.match(r) or (f.get('uitleg') or '').lstrip().startswith('Bijna'):
                uit.append(f"{it.get('id')}: sleutel {f.get('fout')} staat in de vraag maar krijgt '{f.get('regel')}' / {(f.get('uitleg') or '')[:40]!r}")
    return uit
def rapport(items):
    uit = vind(items)
    print(f"\nBIJNA390 (#390: een getal uit de vraag krijgt nooit ±1 of 'Bijna!'): {len(uit)} (FAIL)")
    for x in uit[:20]: print('  FAIL BIJNA390', x)
    return len(uit)
