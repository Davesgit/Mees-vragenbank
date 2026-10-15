#!/usr/bin/env python3
"""Hook V-#1081 (Oefeningen 15 okt, VOORWAARDELIJK, niet geplaatst): fout aan de andere kant van het goede antwoord in het kritisch concept
L-R10b voor G6-GET-E04 #1, G6-MEET-E03 #2, G6-VERH-E02 #2 (OEF_KIEST in kritisch_concept.py).
Gebruik: python3 zet_andere_kant.py <kritisch_concept_g6.json> <uit.json>   (nooit in place op het concept van Overzicht)
Per somtype in 2 van de 4 items (het eerste ware en het eerste foute item) wordt één Nee-afleider vervangen door de fout aan de andere kant
(andere_kant.kandidaat); dan staat het goede getal 2× in het midden en 2× aan de rand (rang-guard V-#1081: hooguit 2× dezelfde rang).
Welke Nee: bij een fout item de Nee die niet het goede antwoord is; bij een waar item de Nee die het verst van het goede getal ligt.
Zelfde letter, zelfde bewering, zelfde antwoord. Voorwaardelijk per item: alleen als de opgave de verwachte vorm heeft en de waarde nieuw is (anders MELD, niets).
Idempotent: staat de waarde er al, dan 0 wijzigingen."""
import json, sys, os, re, copy, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from andere_kant import *
D = json.load(open(sys.argv[1], encoding='utf-8')); MELD, LOG = [], []
per = collections.defaultdict(list)
for x in D['items']:
    if (x['doelId'], x['somtypeNrOrigineel']) in SCOPE: per[(x['doelId'], x['somtypeNrOrigineel'])].append(x)
ALLE = os.environ.get('ANDERE_KANT_ALLE') == '1'      # alleen voor de mutant M_rang
for k_, xs in per.items():
    kies = xs if ALLE else [next(x for x in xs if x['beweringKlopt']), next(x for x in xs if not x['beweringKlopt'])]
    for x in kies:
        c = kandidaat(x)
        if not c: MELD.append(f"{x['id']}: vorm niet herkend, niets gezet"); continue
        v, kant, denk, l1 = c; T = goed(x)
        if any(o['tekst'].startswith('Nee') and w(o['tekst']) == v for o in x['opties']): continue      # al gezet
        nee = [o for o in x['opties'] if o['tekst'].startswith('Nee') and w(o['tekst']) != T]
        if v in {w(x['bewering']), T} or v <= 0: MELD.append(f"{x['id']}: {v} botst"); continue
        o = max(nee, key=lambda o: abs(w(o['tekst']) - T))
        oud = o['tekst']; nieuw = re.sub(GETAL, f'{v:,}'.replace(',', '.') if v >= 10000 else str(v), oud, count=1)
        x['denkfoutPerOptie'].pop(oud, None); x['denkfoutPerOptie'][nieuw] = denk
        L1 = x['conceptHints'].setdefault('L1', {}); L1.pop(oud, None); L1[nieuw] = l1
        o['tekst'] = nieuw
        x.setdefault('oefeningen1081', {})['andereKant'] = {'oud': oud, 'nieuw': nieuw, 'kant': kant, 'denkfout': denk}
        LOG.append(f"{x['id']}: {oud!r} → {nieuw!r} ({kant}, {denk})")
json.dump(D, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for m in MELD: print('MELD', m)
print(f"{len(LOG)} wijzigingen (V-#1081 andere kant)" + ''.join('\n  ' + l for l in LOG))
