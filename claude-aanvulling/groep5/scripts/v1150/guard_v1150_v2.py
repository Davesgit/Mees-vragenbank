#!/usr/bin/env python3
"""Guard V-#1150 v2 (r24, les 462: een laagregel geldt voor ALLE sleutels van een somtype). Nieuwe versie van guard_v1150.py (r23, ongewijzigd).
Toetst het CRITERIUM, geen snapshot. [MUT=..] python3 guard_v1150_v2.py <basis>   (na sync_hint_keys + apply_hints)
Bereik: ELKE foutHint (sleutel) van de items van de 8 maatvraag-somtypen (MEET-E01 #1–#4, MEET-E04 #2/#4, MEET-E05 #1/#3), plus elke G5-foutHint met
«Hoeveel … gaan/gaat er in één …?» in laag 1. Laag 1 (uitleg) = richtingszin + vraag + opdracht, en verder niets:
- richtingszin «Dat is te groot/klein/veel/weinig.»: groot/veel ⇔ sleutel > antwoord, klein/weinig ⇔ sleutel < antwoord; per soort:
  'nul te veel' = groot, 'nul vergeten' = klein of weinig (het woord zoals het per entry was), 'te veel' = veel, 'te weinig' = weinig;
- vraag = precies hint 1 van het item; opdracht = één zin zonder getalwoord voor de factor, cijfers, 'nul(len)' of ' is ' (geen feit);
- in heel laag 1 geen feitzin («Eén meter is honderd centimeter»), geen getalwoord/cijfers voor de factor.
UITZONDERING (expliciet, Didactiek 19 okt): 'het getal uit de som' en 'het getal uit de som (sleutel)' (77 sleutels) blijven zoals ze zijn: de sleutel
is het getal uit de opgave zelf, de tekst noemt welke maat groter is en hoeveel nullen erbij/eraf; die tekst is geen laagfeit maar de denkfout. Voor die
soorten toetst de guard dat laag 1 PRECIES de vaste entrytekst hieronder is (UITZ; 14 entries). Een andere soort in het bereik = FAIL (geen laagregel).
Eén FAIL-regel per foutHint. Op 0290fe0 (vóór r24): FAIL 110 (68 'nul vergeten', 35 'te weinig', 7 'te veel'); na r24: FAIL 0. Exit 1 bij FAIL."""
import json, os, re, sys
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import g5, items
DOEL = {('G5-MEET-E01', 1), ('G5-MEET-E01', 2), ('G5-MEET-E01', 3), ('G5-MEET-E01', 4), ('G5-MEET-E04', 2), ('G5-MEET-E04', 4), ('G5-MEET-E05', 1), ('G5-MEET-E05', 3)}
RICHT = {'nul te veel': {'groot'}, 'nul vergeten': {'klein', 'weinig'}, 'te veel': {'veel'}, 'te weinig': {'weinig'}}
UITZ = {('G5-MEET-E01', 1, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een centimeter is kleiner dan een meter, dus het worden er meer. Zet er twee nullen achter.',
        ('G5-MEET-E01', 1, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een centimeter is kleiner dan een meter, dus het worden er meer. Zet er twee nullen achter.',
        ('G5-MEET-E01', 2, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een meter is groter dan een centimeter, dus het worden er minder. Haal er twee nullen af.',
        ('G5-MEET-E01', 2, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een meter is groter dan een centimeter, dus het worden er minder. Haal er twee nullen af.',
        ('G5-MEET-E01', 3, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een meter is kleiner dan een kilometer, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E01', 3, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een meter is kleiner dan een kilometer, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E01', 4, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een millimeter is kleiner dan een meter, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E01', 4, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een millimeter is kleiner dan een meter, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E04', 2, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E04', 2, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E04', 4, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een milliliter is kleiner dan een liter, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E05', 1, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E05', 1, 'het getal uit de som (sleutel)'): 'Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.',
        ('G5-MEET-E05', 3, 'het getal uit de som'): 'Je hebt het getal uit de som overgenomen. Een gram is kleiner dan een kilogram, dus het worden er meer. Zet er drie nullen achter.'}
VRAAG = re.compile(r'Hoeveel \w+ ga(?:at|an) er in één \w+\?')
L1 = re.compile(r'^Dat is te (groot|klein|veel|weinig)\. (Hoeveel \w+ gaan er in één \w+\?) ([A-Z][^.?!:;]*\.)$')
FACTOR = re.compile(r'\b(?:tien|honderd|duizend)\b|\d|\bnul(?:len)?\b', re.I)
FEIT = re.compile(r'\b(?:[eé]én|een|tien|honderd|duizend) (?:kilo|centi|milli)?(?:meter|liter|gram)\b(?: \(\w+\))? is (?:[eé]én|een|tien|honderd|duizend)\b', re.I)
def getal(s):
    try: return float(str(s).replace('.', '').replace(',', '.').split()[0])
    except Exception: return None
def in_bereik(x, h): return (x['doelId'], x['merge'].get('somtypeNrOrigineel')) in DOEL or bool(VRAAG.search(h.get('uitleg') or ''))
def beoordeel(x, h):
    u = h.get('uitleg') or ''; r = []; k = (x['doelId'], x['merge'].get('somtypeNrOrigineel'), h['soort'])
    if h['soort'].startswith('het getal uit de som'):
        if k not in UITZ: r.append('uitzondering zonder vaste entrytekst')
        elif u != UITZ[k]: r.append('uitzondering gewijzigd (moet de vaste entrytekst blijven)')
        return r
    if h['soort'] not in RICHT: r.append(f"soort {h['soort']!r} heeft geen laagregel (nieuwe sleutelsoort?)")
    if FEIT.search(u): r.append('feitzin in laag 1')
    m = L1.match(u)
    if not m: r.append('niet precies richtingszin + vraag + opdracht')
    else:
        rw, vr, op = m.groups()
        if h['soort'] in RICHT and rw not in RICHT[h['soort']]: r.append(f"richting 'te {rw}' past niet bij soort {h['soort']!r}")
        a, f = getal(x.get('antwoord')), getal(h.get('fout'))
        if a is not None and f is not None and (f > a) != (rw in ('groot', 'veel')): r.append(f"richting 'te {rw}' klopt niet: sleutel {h.get('fout')} vs antwoord {x.get('antwoord')}")
        if vr != (x.get('hint') or ''): r.append(f"vraag ≠ hint 1 van het item ({x.get('hint')!r})")
        if FACTOR.search(op) or ' is ' in f' {op} ': r.append(f"opdracht noemt factor/getal/feit: {op!r}")
    if not m and FACTOR.search(VRAAG.sub('', u)): r.append('getalwoord/cijfer/nullen voor de factor in laag 1')
    return r
def guard(I):
    F = []; n = 0
    for k in sorted(I, key=str):
        for x in sorted(I[k], key=lambda x: x['nr']):
            for h in x.get('foutHints') or []:
                if not in_bereik(x, h): continue
                n += 1; r = beoordeel(x, h)
                if r: F.append(f"laag1 {x['doelId']} #{k[1]} {x['nr']} {h['soort']!r} {h.get('fout')!r}: {'; '.join(r)} — «{(h.get('uitleg') or '')[:90]}»")
    return n, F
def mutant(I, MUT):
    """De fout in de INVOER: één foutHint van een item wordt veranderd vóór de toets."""
    def h_(doel, nr, soort): return next((x, h) for x in sorted(I[(doel, nr)], key=lambda x: x['nr']) for h in x['foutHints'] if h['soort'] == soort)
    if MUT == 'M_feit': x, h = h_('G5-MEET-E01', 1, 'nul te veel'); h['uitleg'] = h['uitleg'].replace(' Reken', ' Eén meter is honderd centimeter. Reken')
    if MUT == 'M_factor': x, h = h_('G5-MEET-E01', 3, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Reken met duizend opnieuw.')
    if MUT == 'M_vraag': x, h = h_('G5-MEET-E05', 3, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Hoeveel gram gaan er in één kilogram?', 'Hoeveel kilogram gaan er in één gram?')
    if MUT == 'M_nulverg_oud': x, h = h_('G5-MEET-E04', 2, 'nul vergeten'); h['uitleg'] = 'Dat is te weinig: er mist een nul. Eén liter is duizend milliliter: zet er drie nullen achter.'
    if MUT == 'M_nulverg_mist': x, h = h_('G5-MEET-E01', 3, 'nul vergeten'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Er mist een nul.')
    if MUT == 'M_teweinig_feit': x, h = h_('G5-MEET-E05', 1, 'te weinig'); h['uitleg'] = 'Dat is te weinig. Eén kilogram is duizend gram. Doe het aantal kilogram keer duizend.'
    if MUT == 'M_teveel_richting': x, h = h_('G5-MEET-E01', 2, 'te veel'); h['uitleg'] = h['uitleg'].replace('te veel', 'te weinig')
    if MUT == 'M_teveel_methode': x, h = h_('G5-MEET-E01', 2, 'te veel'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Deel het aantal centimeter door honderd.')
    if MUT == 'M_uitz': x, h = h_('G5-MEET-E01', 1, 'het getal uit de som'); h['uitleg'] = 'Dat is te weinig. Hoeveel centimeter gaan er in één meter? Reken daarmee opnieuw.'
    if MUT == 'M_uitz_sleutel': x, h = h_('G5-MEET-E01', 2, 'het getal uit de som (sleutel)'); h['uitleg'] += ' Kijk goed.'
    if MUT == 'M_soort': x, h = h_('G5-MEET-E04', 2, 'te weinig'); h['soort'] = 'te weinig (nieuw)'
if __name__ == '__main__':
    B = sys.argv[1]; MUT = os.environ.get('MUT', ''); I = items(g5(B))
    if MUT: mutant(I, MUT)
    n, F = guard(I)
    print(f"INFO guard V-#1150 v2: {n} foutHints in bereik (8 somtypen, alle sleutels; uitzondering 'het getal uit de som': {sum(1 for k in I if k in DOEL for x in I[k] for h in x['foutHints'] if h['soort'].startswith('het getal uit de som'))})")
    for f in F[:40]: print('FAIL', f)
    if len(F) > 40: print(f"… {len(F) - 40} FAIL-regels niet getoond")
    print(f"guard V-#1150 v2: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
    sys.exit(1 if F else 0)
