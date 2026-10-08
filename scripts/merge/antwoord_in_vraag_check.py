#!/usr/bin/env python3
"""V-#560 (recheck G7 batch 1, Didactiek 8 okt): bij procent- en breukitems mag het goede antwoord geen getal uit de vraag zijn.
Wie dan 'een getal uit de vraag' overneemt (een echte denkfout), heeft het goed (bijv. 'Hoeveel procent is 9 van 30?' → 30%: n = N² : 100).
- procent: antwoord 'p%' en p (op waarde) staat als getal in de vraag (niet het getal vlak voor een '%' in de vraag: dat is al een procent);
  ook teller en noemer van een breuk in de vraag tellen mee ('Schrijf 4/20 in procenten.' → 20%);
- breuk: antwoord 'a/b' staat letterlijk als breuk in de vraag. Niet bij kies-vragen en plaatsvragen (het antwoord staat daar per opzet
  in de vraag): 'Kies uit …', 'Welke breuk is het grootst/kleinst', 'Zet a/b op de lijn …'.
FAIL (check_merge_notatie G5–G8). Gebruik: rapport(items) → aantal."""
import re
from fractions import Fraction as F
_GET = r'(?<![\w,./])(\d+(?:,\d+)?)(?![\w/]|[.,]\d)'
_KIES = re.compile(r'\bKies uit\b|het (grootst|kleinst)\b|\bop de (getallen)?lijn\b|^Zet \d+/\d+ ', re.I)
def _w(t): return F(t.replace(',', '.'))
def treffers(items):
    uit = []
    for it in items:
        a = str(it.get('antwoord') or '').strip(); o = (it.get('opgave') or '').replace('\n', ' ')
        m = re.fullmatch(r'(\d+(?:,\d+)?)\s?%', a)
        if m:
            o2 = re.sub(r'\d+(?:,\d+)?\s?%', ' ', o)      # procenten in de vraag tellen niet als 'getal uit de vraag'
            getallen = {_w(x) for x in re.findall(_GET, o2)} | {_w(x) for b in re.findall(r'(?<![\d,])(\d+)/(\d+)(?![\d/])', o2) for x in b}
            if _w(m.group(1)) in getallen: uit.append((it['id'], o, a, 'procent'))
            continue
        m = re.fullmatch(r'(\d+)/(\d+)', a)
        if m and _KIES.search(o): continue
        if m and re.search(r'(?<![\d/])' + re.escape(a) + r'(?![\d/])', o): uit.append((it['id'], o, a, 'breuk'))
    return uit
def rapport(items):
    uit = treffers(items)
    print(f"\nANTWVRAAG (V-#560: procent/breuk, het goede antwoord is een getal uit de vraag): {len(uit)} (FAIL)")
    for x in uit[:30]: print('  FAIL ANTWVRAAG', *x)
    return len(uit)
