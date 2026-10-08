#!/usr/bin/env python3
"""Gedeelde haak voor de merge-checkers G3–G8 (G5 merge-fixlijst #105, Didactiek 18:54, recheck-6b V-a).
FAIL als een waarde in antwoordOokGoed of geldInvoer (sleutel, accepteer, punt.voorbeeld) na normalisatie niet gelijk is aan het antwoord.
Normalisatie: € en spaties weg, punt = komma (punt.voorbeeld is juist de punt-vorm), ',00' en een slot-nul weg ('2,30' = '2,3' = '€2,30').
Alleen getallen en bedragen worden vergeleken. Een ook-goed-vorm die geen getal is ('een half', '1/2') slaat de haak over (die kan hij niet beoordelen).
Gebruik: import antwoordvormen_check as AV; n_fail = AV.rapport(items)"""
import re
from fractions import Fraction

def getal(v):
    s = str(v).strip().replace('\u00a0', ' ').replace('€', '').replace(' ', '')
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+(?:,\d+)?', s): s = s.replace('.', '')          # 1.250,50 (duizendtal-punt)
    s = s.replace(',', '.')
    if s.startswith('−'): s = '-' + s[1:]
    return Fraction(s) if re.fullmatch(r'-?\d+(?:\.\d+)?', s) else None

def controleer(items):
    uit = []
    for it in items:
        a = getal(it.get('antwoord'))
        if a is None: continue
        vormen = [('antwoordOokGoed', v) for v in it.get('antwoordOokGoed') or []]
        gi = it.get('geldInvoer') or {}
        if gi:
            vormen += [('geldInvoer.sleutel', gi.get('sleutel'))] + [('geldInvoer.accepteer', v) for v in gi.get('accepteer') or []]
            if (gi.get('punt') or {}).get('voorbeeld') is not None: vormen.append(('geldInvoer.punt.voorbeeld', gi['punt']['voorbeeld']))
        for veld, v in vormen:
            g = getal(str(v).replace('.', ',') if veld == 'geldInvoer.punt.voorbeeld' else v)
            if g is None and veld == 'antwoordOokGoed' and re.fullmatch(r'\d+\.\d+', str(v)): g = Fraction(str(v))
            if g is not None and g != a:
                uit.append(f"{it.get('id')}: {veld} '{v}' past niet bij antwoord '{it.get('antwoord')}'")
    return uit

def rapport(items):
    f = controleer(items)
    print(f"\nVORM (antwoordOokGoed/geldInvoer passen bij het antwoord, #105): {len(f)} (FAIL)")
    for x in f[:20]: print('  FAIL VORM', x)
    return len(f)
