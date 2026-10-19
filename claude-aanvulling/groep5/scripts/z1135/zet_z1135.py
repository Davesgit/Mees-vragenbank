#!/usr/bin/env python3
"""Hook Z-#1135 (Didactiek; VOORWAARDELIJK, niet geplaatst). python3 zet_z1135.py <basis>. Idempotent.
'een nul te veel' (GET-E07 #5/#9, MEET-E01 #1–#4, MEET-E04 #2/#4, MEET-E05 #1/#3) → richting + waar kijken, met de eenheden van het somtype:
  groot → klein (m → cm): «Dat is te groot. Hoeveel keer zo klein is een centimeter als een meter?» (de methodezin erachter blijft);
  klein → groot (cm → m): «Dat is te groot/te klein. Hoeveel keer zo groot is een meter als een centimeter?»;
  GET-E07: «Dat is te veel. Tel de nullen in de som nog eens: hoeveel horen er achter je antwoord?»
Niet aangeraakt: 'nul vergeten' met «er mist een nul» (het kind is een nul vergeten; Didactiek: laten staan)."""
import json, os, sys, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
EENH = {('G5-MEET-E01', 1): ('meter', 'centimeter', 'af'), ('G5-MEET-E01', 2): ('centimeter', 'meter', 'op'), ('G5-MEET-E01', 3): ('kilometer', 'meter', 'af'),
        ('G5-MEET-E01', 4): ('meter', 'millimeter', 'af'), ('G5-MEET-E04', 2): ('liter', 'milliliter', 'af'), ('G5-MEET-E04', 4): ('liter', 'milliliter', 'af'),
        ('G5-MEET-E05', 1): ('kilogram', 'gram', 'af'), ('G5-MEET-E05', 3): ('kilogram', 'gram', 'af')}
def kijk(k):
    van, naar, r = EENH[k]
    return f'Hoeveel keer zo klein is een {naar} als een {van}?' if r == 'af' else f'Hoeveel keer zo groot is een {naar} als een {van}?'
VERV = {'Dat is te veel: er staat een nul te veel achter.': 'groot', 'Dat is te veel: er staat nog een nul te veel achter.': 'groot',
        'Dat is te weinig: je hebt een nul te veel weggehaald.': 'klein'}
GET7 = {'Dat is te veel: er staat een nul te veel achter.': 'Dat is te veel. Tel de nullen in de som nog eens: hoeveel horen er achter je antwoord?',
        'Dat is te veel. Staat er een nul te veel achter?': 'Dat is te veel. Tel de nullen in de som nog eens: hoeveel horen er achter je antwoord?'}
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        k = (s['doel'], s['nrOrigineel'])
        for f in s['foutHints']:
            for v in ('tekst', 'tekstSterker'):
                x = f.get(v) or ''; nw = x
                if k[0] == 'G5-GET-E07' and k[1] in (5, 9):
                    for a, b in GET7.items(): nw = nw.replace(a, b)
                elif k in EENH:
                    for a, r in VERV.items(): nw = nw.replace(a, f'Dat is te {r}. {kijk(k)}')
                if nw != x: f[v] = nw; LOG.append(f"{k[0]} #{k[1]} {f['soort']!r} [{v}]: {nw[:100]}")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1135)" + ''.join('\n  ' + l for l in LOG))
