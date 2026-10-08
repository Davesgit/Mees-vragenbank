#!/usr/bin/env python3
"""Gedeelde haak (G4/G5 merges; G5 merge-fixlijst #107, Didactiek recheck-6b V-c, 1 okt 18:54).
WARN als een fout-hint bij een meerkeuze-item met een maat als antwoord ('20 cm') het getal én de eenheid van het goede antwoord noemt,
in cijfers of in woorden ('20 cm', '20 centimeter', 'twintig centimeter'). Dan verklapt de hint het antwoord.
Gebruik: import verklapper_check as VK; n_warn = VK.rapport(items)"""
import re
EENHEID = {'mm': 'millimeter', 'cm': 'centimeter', 'dm': 'decimeter', 'm': 'meter', 'km': 'kilometer', 'g': 'gram', 'kg': 'kilo(?:gram)?',
           'ml': 'milliliter', 'cl': 'centiliter', 'dl': 'deciliter', 'l': 'liter'}
EEN = ['nul', 'één|een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf', 'dertien', 'veertien', 'vijftien',
       'zestien', 'zeventien', 'achttien', 'negentien']
TIEN = {20: 'twintig', 30: 'dertig', 40: 'veertig', 50: 'vijftig', 60: 'zestig', 70: 'zeventig', 80: 'tachtig', 90: 'negentig', 100: 'honderd'}
def woord(n):
    if n < 20: return EEN[n]
    if n in TIEN: return TIEN[n]
    if n < 100:
        e = EEN[n % 10].split('|')[-1]; t = TIEN[n // 10 * 10]
        return f"{e}(?:ën|en){t}"
    return None
def controleer(items):
    uit = []
    for it in items:
        if not it.get('opties'): continue
        m = re.fullmatch(r'(\d+) ?(mm|cm|dm|m|km|g|kg|ml|cl|dl|l|L)', str(it.get('antwoord') or '').strip())
        if not m: continue
        n, e = int(m.group(1)), m.group(2).lower()
        w = woord(n); getal = rf'(?:{n}' + (rf'|{w}' if w else '') + ')'
        rx = re.compile(rf'(?<![\d,]){getal} ?(?:{re.escape(m.group(2))}|{EENHEID[e]})\b', re.I)
        for f in it.get('foutHints') or []:
            if rx.search(f.get('uitleg') or ''):
                uit.append(f"{it.get('id')}: fout-hint bij '{f.get('fout')}' noemt het antwoord '{it['antwoord']}': «{(f.get('uitleg') or '')[:90]}»")
    return uit
def rapport(items):
    w = controleer(items)
    print(f"\nVERKLAP (fout-hint noemt het goede antwoord, getal + eenheid, #107): {len(w)} (WARN)")
    for x in w[:20]: print('  WARN VERKLAP', x)
    return len(w)
