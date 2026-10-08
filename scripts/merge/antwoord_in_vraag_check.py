#!/usr/bin/env python3
"""V-#560 (recheck G7 batch 1, Didactiek 8 okt): bij procent- en breukitems mag het goede antwoord geen getal uit de vraag zijn.
Wie dan 'een getal uit de vraag' overneemt (een echte denkfout), heeft het goed (bijv. 'Hoeveel procent is 9 van 30?' → 30%: n = N² : 100).
- procent: antwoord 'p%' en p (op waarde) staat als getal in de vraag (niet het getal vlak voor een '%' in de vraag: dat is al een procent);
  ook teller en noemer van een breuk in de vraag tellen mee ('Schrijf 4/20 in procenten.' → 20%);
- breuk: antwoord 'a/b' staat letterlijk als breuk in de vraag. Niet bij kies-vragen en plaatsvragen (het antwoord staat daar per opzet
  in de vraag): 'Kies uit …', 'Welke breuk is het grootst/kleinst', 'Zet a/b op de lijn …'.
- som (Z-#609, review G7 batch 3): de vraag heeft een som 'a ∘ b' (+ − × :) en het goede antwoord (heel of kommagetal) is a of b
  ('1,2 − 0,6 = 0,6', met een kommagetal); of een verdeelsom 'x … verdeeld over n …' met antwoord n ('9 liter … over 3 … = 3').
- verhouding (V-#703, review G7 batch 6): 'a : b = c : ?' met het antwoord a, b of c ('9 : 3 = 27 : ?' → 9).
FAIL (check_merge_notatie G5–G8). Gebruik: rapport(items) → aantal."""
import re
from fractions import Fraction as F
_GET = r'(?<![\w,./])(\d+(?:,\d+)?)(?![\w/]|[.,]\d)'
_KIES = re.compile(r'\bKies uit\b|het (grootst|kleinst)\b|\bop de (getallen)?lijn\b|^Zet \d+/\d+ ', re.I)
def _w(t): return F(t.replace(',', '.'))
INFO = []      # Z-#609: hele-getallen-som met het antwoord in de som ('4 : 2 = 2'): INFO, geen FAIL (G5 is goedgekeurd)
def treffers(items):
    del INFO[:]; uit = []
    for it in items:
        a = str(it.get('antwoord') or '').strip(); o = (it.get('opgave') or '').replace('\n', ' ')
        m = re.fullmatch(r'(\d+(?:,\d+)?)\s?%', a)
        if m:
            o2 = re.sub(r'\d+(?:,\d+)?\s?%', ' ', o)      # procenten in de vraag tellen niet als 'getal uit de vraag'
            getallen = {_w(x) for x in re.findall(_GET, o2)} | {_w(x) for b in re.findall(r'(?<![\d,])(\d+)/(\d+)(?![\d/])', o2) for x in b}
            if _w(m.group(1)) in getallen: uit.append((it['id'], o, a, 'procent'))
            continue
        # V-#703 (review G7 batch 6, les 215): verhouding 'a : b = c : ?' → het antwoord is geen getal uit de vraag
        mv = re.search(r'(?<![\d,])(\d+(?:,\d+)?) : (\d+(?:,\d+)?) = (\d+(?:,\d+)?) : \?', o)
        if mv and re.fullmatch(r'\d+(?:,\d+)?', a) and _w(a) in {_w(x) for x in mv.groups()}: uit.append((it['id'], o, a, 'verhouding')); continue
        g = re.fullmatch(r'\d+(?:,\d+)?', a)
        if g:
            w = _w(a); o3 = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', o); o3 = re.sub(r'\d{1,3}(?:\.\d{3})+', ' ', o3)      # geen kloktijd, geen duizendtal-punt
            ops = re.findall(r'(?<![\d,])(\d+(?:,\d+)?)\s*[+−×:x÷]\s*(\d+(?:,\d+)?)(?![\d,])', o3)
            hit = [(x, y) for x, y in ops if w in (_w(x), _w(y))]
            v = re.search(r'verdeeld over (\d+)', o3)
            if hit and (',' in a or any(',' in x + y for x, y in hit)): uit.append((it['id'], o, a, 'som')); continue
            if v and _w(v.group(1)) == w: uit.append((it['id'], o, a, 'som')); continue
            if hit and not re.search(r'^Op welk cijfer', o): INFO.append((it['id'], o, a, 'som (heel getal)'))
        m = re.fullmatch(r'(\d+)/(\d+)', a)
        if m and _KIES.search(o): continue
        if m and re.search(r'(?<![\d/])' + re.escape(a) + r'(?![\d/])', o): uit.append((it['id'], o, a, 'breuk'))
    return uit
def rapport(items):
    uit = treffers(items)
    print(f"\nANTWVRAAG (V-#560/Z-#609: procent/breuk/som, het goede antwoord is een getal uit de vraag): {len(uit)} (FAIL)")
    for x in uit[:30]: print('  FAIL ANTWVRAAG', *x)
    if INFO: print(f'  ({len(INFO)} INFO: som met hele getallen waar het antwoord in de som staat)')
    for x in INFO[:20]: print('  INFO ANTWVRAAG', *x)
    return len(uit)
