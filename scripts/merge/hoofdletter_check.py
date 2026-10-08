#!/usr/bin/env python3
"""V-#608 (review G7 batch 3, Didactiek 8 okt; les 184): een vraagzin begint met een hoofdletter. FAIL (check_merge_notatie G5–G8) als de opgave,
of een zin erin na '. ', '? ' of '! ', met een kleine letter begint. Niet: een getal of teken vooraan ('3,5 cm …', '€4 …', '… '), een eenheid of
afkorting vlak na een punt-getal ('ca.', 'bijv.', 'enz.'), en tekst na een dubbele punt. Gebruik: rapport(items) → aantal."""
import re
AFK = r'(?:ca|bijv|enz|o\.a|d\.w\.z|m\.a\.w|nr|blz)\.'
def treffers(items):
    uit = []
    for it in items:
        o = (it.get('opgave') or '').replace('\n', ' ').strip()
        if not o: continue
        if o[0].isalpha() and o[0].islower(): uit.append((it['id'], 'begin', o[:70])); continue
        for m in re.finditer(r'(?<!\.\.)(?<!…)([.?!])\s+([a-zà-öø-ÿ])', o):      # niet na '...' (invulplek: '= ... m')
            voor = o[:m.start() + 1]
            if re.search(r'\b' + AFK + r'$', voor) or re.search(r'\d\.$', voor): continue
            uit.append((it['id'], 'zin', o[max(0, m.start() - 30):m.end() + 30])); break
    return uit
def rapport(items):
    uit = treffers(items)
    print(f"\nHOOFDLETTER (V-#608: een vraagzin begint met een kleine letter): {len(uit)} (FAIL)")
    for x in uit[:30]: print('  FAIL HOOFDLETTER', *x)
    return len(uit)
