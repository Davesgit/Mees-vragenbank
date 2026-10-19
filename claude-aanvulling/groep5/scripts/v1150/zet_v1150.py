#!/usr/bin/env python3
"""Hook V-#1150 (r23, Didactiek; PATCH COPY, niet geplaatst). python3 zet_v1150.py <basis>. Idempotent. Na Z-#1148 (9561db9).
G5 maatvragen, batch4: de 9 entry-foutHints met «Hoeveel X gaan er in één Y?» in laag 1 (MEET-E01 #1 #2(2×) #3 #4, MEET-E04 #2 #4, MEET-E05 #1 #3).
Laag 1 (tekst) wordt alleen: <richtingszin zoals hij per entry was> + de vraag + «Reken daarmee opnieuw.» Het feit («Eén meter is honderd centimeter»)
en de methode («zet er twee nullen achter») gaan eruit; die staan in laag 2: tekstSterker is leeg, dus de motor valt terug op hint2 van het somtype
(«Eén meter (m) is honderd centimeter (cm). Doe het aantal meter keer honderd: zet er twee nullen achter.», Z-#1148). De itemvelden (foutHints.uitleg,
foutHintsTekst, foutRegels.tekst; 149 + 149 + 86) en somtypen/*.md volgen via sync_hint_keys + apply_hints.
Stopt met MELD (niets gezet voor die entry) als tekstSterker niet leeg is, of hint2 het feit niet heeft: dan zou het feit verdwijnen."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import g5, schrijf
B = sys.argv[1]; G = g5(B); LOG, MELD = [], []
OPDR = 'Reken daarmee opnieuw.'
RE = re.compile(r'^(Dat is te (?:groot|klein)\.) (Hoeveel \w+ gaan er in één \w+\?)(?: (.*))?$')
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        for f in s.get('foutHints') or []:
            m = RE.match(f.get('tekst') or '')
            if not m or m.group(3) == OPDR: continue
            pl = f"{os.path.basename(P)} {s['doel']} #{s['nrOrigineel']} {f['soort']!r}"
            if f.get('tekstSterker'): MELD.append(f"{pl}: tekstSterker niet leeg, laag 2 is dan niet hint2"); continue
            if not re.search(r'\(\w+\) is (?:één|tien|honderd|duizend) \w+ \(\w+\)\.', s.get('hint2') or ''): MELD.append(f"{pl}: hint2 heeft het feit niet: {s.get('hint2')!r}"); continue
            nieuw = f"{m.group(1)} {m.group(2)} {OPDR}"; LOG.append(f"{pl}: «{f['tekst']}» → «{nieuw}»"); f['tekst'] = nieuw
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (V-#1150)" + ''.join('\n  ' + l for l in LOG))
sys.exit(1 if MELD else 0)
