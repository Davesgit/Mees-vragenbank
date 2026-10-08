"""#390-check (G6 merge-fixlijst #390, Didactiek gate ronde 9 deel B, les 115; gedeeld door check_merge_notatie G5–G8). Leest alleen.
FAIL: een fout-sleutel die gelijk is aan een getal uit de vraag en toch de ±1-regel of een tekst met 'Bijna!' krijgt.
Zo'n kind heeft geen rekenstap bijna goed gedaan, maar een getal uit de vraag overgenomen. De motor (fout_regels.in_vraag390) slaat die regels over.
#530 (eindcheck G5 r11): ook bedragen ('€4,75' = '€ 4,75' = '4,75'); vóór #530 sloeg de check '€' over."""
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
    """D-#416: de waarde van een sleutel (heel getal, kommagetal of breuk; n/n = 1); een eenheid erachter mag. None als het geen getal is.
    #530 (eindcheck G5 r11): ook bedragen: '€4,75', '€ 4,75' en '4,75' hebben dezelfde waarde (vóór #530 sloeg dit '€' over)."""
    v = str(v or '').strip().replace('\u00a0', ' ')
    v = re.sub(r'^€\s*', '', v)
    m = re.fullmatch(r'(' + _GETAL416 + r')(?:\s+[a-zA-Z]+)?', v)
    if not m: return None
    t = m.group(1); n, _, d = t.partition('/'); n = _F416(n.replace('.', '').replace(',', '.'))
    return n / int(d) if d else n
def vraag_waarden416(opg, los=True):
    """D-#416: alle getallen uit de vraag als waarde (ook kommagetallen en breuken), plus de losse hele getallen zoals vroeger.
    #530: los=False zonder die losse hele getallen (voor een bedrag: €4 is niet de 4 uit '€4,75')."""
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', (opg or '').replace('\n', ' '))
    w = {waarde416(x) for x in re.findall(r'(?<![\w:.,/])' + _GETAL416 + r'(?![\w:/]|[.,]\d)', t)}
    if los: w |= {_F416(int(x.replace('.', ''))) for x in re.findall(r'(?<![\w:.])(?:\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|\.\d)', t)}
    return {x for x in w if x is not None}
def vind(items):
    """D-#416: vergelijk op waarde (ook breuken en kommagetallen; n/n = 1), net als fout_regels.in_vraag390."""
    uit = []
    for it in items:
        n = vraag_waarden416(it.get('opgave')) | {_F416(x) for x in _nums((it.get('opgave') or '').replace('\n', ' '))}
        n_geld = vraag_waarden416(it.get('opgave'), los=False)      # #530: een bedrag alleen tegen de echte getallen uit de vraag
        for f in it.get('foutHints') or []:
            x = waarde416(f.get('fout'))
            if x is None or x not in (n_geld if str(f.get('fout')).strip().startswith('€') else n): continue
            r = (f.get('regel') or '').lower().replace('−', '-').strip()
            if PM1.match(r) or (f.get('uitleg') or '').lstrip().startswith('Bijna'):
                uit.append(f"{it.get('id')}: sleutel {f.get('fout')} staat in de vraag maar krijgt '{f.get('regel')}' / {(f.get('uitleg') or '')[:40]!r}")
    return uit
def rapport(items):
    uit = vind(items)
    print(f"\nBIJNA390 (#390: een getal uit de vraag krijgt nooit ±1 of 'Bijna!'): {len(uit)} (FAIL)")
    for x in uit[:20]: print('  FAIL BIJNA390', x)
    return len(uit)
