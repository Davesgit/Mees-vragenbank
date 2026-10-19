#!/usr/bin/env python3
"""Hook V-#1152 + V-#1153 (r24, Didactiek op Oef-#1078; PATCH COPY, niet geplaatst). python3 zet_v1152.py <basis>. Idempotent. Na V-#1150 (0290fe0).
De 8 maatvraag-somtypen (MEET-E01 #1–#4, MEET-E04 #2/#4, MEET-E05 #1/#3), hints/batch*.json, laag 1 (foutHints.tekst) wordt richting + vraag + opdracht,
zoals V-#1150 bij 'nul te veel':  «Dat is te <woord>. <hint1 van de entry> Reken daarmee opnieuw.»  (het richtingswoord blijft zoals het per entry was)
- V-#1152 (verplicht): 'nul vergeten' (68 sleutels). «er mist een nul» noemt het precieze verschil (sleutel = antwoord : 10; Z-#1091-patroon) en botst
  met «zet er twee nullen achter»; het feit en de methode gaan weg uit laag 1.
- V-#1153 (zacht): 'te weinig' (35) en 'te veel' (7): dezelfde vorm.
- 'het getal uit de som' en 'het getal uit de som (sleutel)' (77) blijven zoals ze zijn (uitzondering, Didactiek 19 okt); ook 'anders omgerekend
  (sleutel)' en 'andere fout' (geen sleutels bij de items) raakt de hook niet.
Laag 2: tekstSterker is leeg, dus de motor valt terug op hint2 van het somtype (feit + methode, Z-#1148). Stopt met MELD (niets gezet voor die entry)
als tekstSterker niet leeg is, hint1 niet de vraag is, of hint2 het feit niet heeft. De itemvelden volgen via sync_hint_keys + apply_hints."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import g5, schrijf
B = sys.argv[1]; G = g5(B); LOG, MELD = [], []
DOEL = {('G5-MEET-E01', 1), ('G5-MEET-E01', 2), ('G5-MEET-E01', 3), ('G5-MEET-E01', 4), ('G5-MEET-E04', 2), ('G5-MEET-E04', 4), ('G5-MEET-E05', 1), ('G5-MEET-E05', 3)}
TICKET = {'nul vergeten': 'V-#1152', 'te weinig': 'V-#1153', 'te veel': 'V-#1153'}
OPDR = 'Reken daarmee opnieuw.'
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        if (s['doel'], s['nrOrigineel']) not in DOEL: continue
        for f in s.get('foutHints') or []:
            if f['soort'] not in TICKET: continue
            pl = f"{TICKET[f['soort']]} {os.path.basename(P)} {s['doel']} #{s['nrOrigineel']} {f['soort']!r}"
            m = re.match(r'^Dat is te (groot|klein|veel|weinig)\b', f.get('tekst') or '')
            vr = s.get('hint1') or ''
            if not m: MELD.append(f"{pl}: geen richtingswoord vooraan: {f.get('tekst')!r}"); continue
            nieuw = f"Dat is te {m.group(1)}. {vr} {OPDR}"
            if f['tekst'] == nieuw: continue
            if f.get('tekstSterker'): MELD.append(f"{pl}: tekstSterker niet leeg, laag 2 is dan niet hint2"); continue
            if not re.fullmatch(r'Hoeveel \w+ gaan er in één \w+\?', vr): MELD.append(f"{pl}: hint1 is niet de vraag: {vr!r}"); continue
            if not re.search(r'\(\w+\) is (?:één|tien|honderd|duizend) \w+ \(\w+\)\.', s.get('hint2') or ''): MELD.append(f"{pl}: hint2 heeft het feit niet"); continue
            LOG.append(f"{pl}: «{f['tekst']}» → «{nieuw}»"); f['tekst'] = nieuw
    if len(LOG) > n0: schrijf(P, t, D)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (V-#1152 {sum('V-#1152' in l for l in LOG)}, V-#1153 {sum('V-#1153' in l for l in LOG)})" + ''.join('\n  ' + l for l in LOG))
sys.exit(1 if MELD else 0)
