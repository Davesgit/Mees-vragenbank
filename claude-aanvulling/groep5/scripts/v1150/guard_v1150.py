#!/usr/bin/env python3
"""Guard V-#1150 (r23, les 461): toetst het CRITERIUM, geen snapshot. [MUT=..] python3 guard_v1150.py <basis>   (na sync_hint_keys + apply_hints)
Bereik: elke G5-foutHint (per_doel) die uit één van de 9 maatvraag-entries komt (doel, nrOrigineel, soort: zie BEREIK) of die «Hoeveel … gaan/gaat
er in één …?» in laag 1 heeft. Laag 1 (uitleg) moet zijn: richtingszin + vraag + opdracht, en verder niets:
- richtingszin «Dat is te groot.» / «Dat is te klein.»: groot ⇔ de foute sleutel > het antwoord, klein ⇔ <; per soort: 'nul te veel' = groot,
  'nul vergeten' = klein (het richtingswoord blijft zoals het per entry was);
- vraag = precies de hint 1 van het item («Hoeveel <klein> gaan er in één <groot>?», 'gaan'; Z-#1148 houdt die bij de opgave);
- opdracht = één zin, zonder getalwoord voor de factor (tien/honderd/duizend), zonder cijfers, zonder 'nul'/'nullen', zonder ' is ' (geen feit);
- in heel laag 1: geen feitzin («Eén meter is honderd centimeter», «Honderd centimeter is één meter»), geen getalwoord voor de factor, geen cijfers.
Eén FAIL-regel per foutHint (alle redenen samen). Op 9561db9 (vóór V-#1150): FAIL 149. Exit 1 bij FAIL. Mutanten: zie verwacht_guard_v1150.tsv."""
import json, os, re, sys
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(D_, '..', 'z1090', 'r4')); from g5pad import g5, items
BEREIK = {('G5-MEET-E01', 1, 'nul te veel'), ('G5-MEET-E01', 2, 'nul te veel'), ('G5-MEET-E01', 2, 'nul vergeten'), ('G5-MEET-E01', 3, 'nul te veel'),
          ('G5-MEET-E01', 4, 'nul te veel'), ('G5-MEET-E04', 2, 'nul te veel'), ('G5-MEET-E04', 4, 'nul te veel'), ('G5-MEET-E05', 1, 'nul te veel'),
          ('G5-MEET-E05', 3, 'nul te veel')}
RICHT = {'nul te veel': 'groot', 'nul vergeten': 'klein'}
VRAAG = re.compile(r'Hoeveel \w+ ga(?:at|an) er in één \w+\?')
L1 = re.compile(r'^Dat is te (groot|klein)\. (Hoeveel \w+ gaan er in één \w+\?) ([A-Z][^.?!:;]*\.)$')
FACTOR = re.compile(r'\b(?:tien|honderd|duizend)\b|\d|\bnull?en?\b', re.I)
FEIT = re.compile(r'\b(?:[eé]én|een|tien|honderd|duizend) (?:kilo|centi|milli)?(?:meter|liter|gram)\b(?: \(\w+\))? is (?:[eé]én|een|tien|honderd|duizend)\b', re.I)
def getal(s):
    try: return float(str(s).replace('.', '').replace(',', '.').split()[0])
    except Exception: return None
def in_bereik(x, h):
    return (x['doelId'], x['merge'].get('somtypeNrOrigineel'), h['soort']) in BEREIK or bool(VRAAG.search(h.get('uitleg') or ''))
def beoordeel(x, h):
    u = h.get('uitleg') or ''; r = []
    if FEIT.search(u): r.append('feitzin in laag 1')
    m = L1.match(u)
    if not m: r.append('niet precies richtingszin + vraag + opdracht')
    else:
        rw, vr, op = m.groups()
        if RICHT.get(h['soort']) and rw != RICHT[h['soort']]: r.append(f"richting 'te {rw}' ≠ soort {h['soort']!r}")
        a, f = getal(x.get('antwoord')), getal(h.get('fout'))
        if a is not None and f is not None and (f > a) != (rw == 'groot'): r.append(f"richting 'te {rw}' klopt niet: sleutel {h.get('fout')} vs antwoord {x.get('antwoord')}")
        if vr != (x.get('hint') or ''): r.append(f"vraag ≠ hint 1 van het item ({x.get('hint')!r})")
        if FACTOR.search(op) or ' is ' in f' {op} ': r.append(f"opdracht noemt factor/getal/feit: {op!r}")
    if not m and FACTOR.search(VRAAG.sub('', u)): r.append('getalwoord/cijfer/nullen voor de factor in laag 1')
    return r
def guard(I, MUT=''):
    F = []; n = 0
    for k in sorted(I, key=str):
        for x in sorted(I[k], key=lambda x: x['nr']):
            for h in x.get('foutHints') or []:
                if not in_bereik(x, h): continue
                n += 1; r = beoordeel(x, h)
                if r: F.append(f"laag1 {x['doelId']} #{k[1]} {x['nr']} {h['soort']!r} {h.get('fout')!r}: {'; '.join(r)} — «{(h.get('uitleg') or '')[:90]}»")
    return n, F
def mutant(I, MUT):
    """De fout in de INVOER: één foutHint (of hint) van een item wordt veranderd vóór de toets."""
    def h_(doel, nr, soort):
        return next((x, h) for x in sorted(I[(doel, nr)], key=lambda x: x['nr']) for h in x['foutHints'] if h['soort'] == soort)
    if MUT == 'M_feit': x, h = h_('G5-MEET-E01', 1, 'nul te veel'); h['uitleg'] = h['uitleg'].replace(' Reken', ' Eén meter is honderd centimeter. Reken')
    if MUT == 'M_feit_achter': x, h = h_('G5-MEET-E05', 1, 'nul te veel'); h['uitleg'] += ' Eén kilogram is duizend gram.'
    if MUT == 'M_factor': x, h = h_('G5-MEET-E01', 3, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Reken met duizend opnieuw.')
    if MUT == 'M_cijfer': x, h = h_('G5-MEET-E04', 2, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Reken met 1000 opnieuw.')
    if MUT == 'M_nullen': x, h = h_('G5-MEET-E01', 4, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Reken daarmee opnieuw.', 'Zet er nullen achter.')
    if MUT == 'M_geen_opdracht': x, h = h_('G5-MEET-E04', 4, 'nul te veel'); h['uitleg'] = h['uitleg'].replace(' Reken daarmee opnieuw.', '')
    if MUT == 'M_richting': x, h = h_('G5-MEET-E01', 2, 'nul vergeten'); h['uitleg'] = h['uitleg'].replace('te klein', 'te groot')
    if MUT == 'M_vraag': x, h = h_('G5-MEET-E05', 3, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('Hoeveel gram gaan er in één kilogram?', 'Hoeveel kilogram gaan er in één gram?')
    if MUT == 'M_gaat': x, h = h_('G5-MEET-E01', 2, 'nul te veel'); h['uitleg'] = h['uitleg'].replace('gaan er in', 'gaat er in')
    if MUT == 'M_oud': x, h = h_('G5-MEET-E01', 1, 'nul te veel'); h['uitleg'] = 'Dat is te groot. Hoeveel centimeter gaan er in één meter? Eén meter is honderd centimeter: zet er twee nullen achter.'
    if MUT == 'M_zonder_vraag': x, h = h_('G5-MEET-E01', 3, 'nul te veel'); h['uitleg'] = 'Dat is te groot. Eén kilometer is duizend meter.'
if __name__ == '__main__':
    B = sys.argv[1]; MUT = os.environ.get('MUT', ''); I = items(g5(B))
    if MUT: mutant(I, MUT)
    n, F = guard(I)
    print(f"INFO guard V-#1150: {n} foutHints in bereik (9 entries)")
    for f in F[:40]: print('FAIL', f)
    if len(F) > 40: print(f"… {len(F) - 40} FAIL-regels niet getoond")
    print(f"guard V-#1150: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
    sys.exit(1 if F else 0)
