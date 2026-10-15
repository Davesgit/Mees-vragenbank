#!/usr/bin/env python3
"""Hook Z-#1136 (zichtbare resten; VOORWAARDELIJK, niet geplaatst). python3 zet_z1136.py <basis>. Idempotent.
- GET-E06 #1/#2 'centen ernaast' («Bijna! De centen kloppen net niet.», Claudes sleutel ±1/±10 cent) → vier soorten met leesbare regel
  (fout = antwoord ± 1 cent / ± 10 cent), tekst met richting + waar kijken, richting per item via de sleutel. Geen muntvorm: geen foto (jsRender.munten) in GET-E06.
- GET-M06 #3/#6 'nog een ronde': «Daar past nog een hele ronde bij: iedereen kan er nog één krijgen.» → zonder bedrag."""
import json, os, sys, glob, copy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import *
B = sys.argv[1]; G = g5(B); LOG = []
CENT = [('centen te veel (1 cent)', 'fout = antwoord + 1 cent', 'Dat is te veel. Kijk goed naar het laatste cijfer achter de komma: reken de centen nog eens na.'),
        ('centen te weinig (1 cent)', 'fout = antwoord − 1 cent', 'Dat is te weinig. Kijk goed naar het laatste cijfer achter de komma: reken de centen nog eens na.'),
        ('centen te veel (10 cent)', 'fout = antwoord + 10 cent', 'Dat is te veel. Kijk goed naar het eerste cijfer achter de komma: reken de centen nog eens na.'),
        ('centen te weinig (10 cent)', 'fout = antwoord − 10 cent', 'Dat is te weinig. Kijk goed naar het eerste cijfer achter de komma: reken de centen nog eens na.')]
RONDE = ('Daar past nog een hele ronde bij: iedereen kan er nog één krijgen.', 'Daar kun je nog verder mee verdelen.')
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if s['doel'] == 'G5-GET-E06' and s['nrOrigineel'] in (1, 2):
            i = next((i for i, f in enumerate(s['foutHints']) if f['soort'] == 'centen ernaast'), None)
            if i is not None:
                f = s['foutHints'][i]
                nw = [{k: v for k, v in dict(copy.deepcopy(f), soort=so, regel=rg, tekst=tx, bron='nieuw').items() if k not in ('claudeDenkfout', 'claudeTekst', 'waarom')} for so, rg, tx in CENT]
                s['foutHints'][i:i + 1] = nw; LOG.append(f"G5-GET-E06 #{s['nrOrigineel']} 'centen ernaast' → 4 soorten (± 1 cent / ± 10 cent)")
        if s['doel'] == 'G5-GET-M06':
            for f in s['foutHints']:
                for v in ('tekst', 'tekstSterker'):
                    if RONDE[0] in (f.get(v) or ''): f[v] = f[v].replace(*RONDE); LOG.append(f"G5-GET-M06 #{s['nrOrigineel']} {f['soort']!r} [{v}]: hele ronde → zonder bedrag")
    if len(LOG) > n0: schrijf(P, t, D)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1136)" + ''.join('\n  ' + l for l in LOG))
