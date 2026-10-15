#!/usr/bin/env python3
"""r13 L-R10b: kritisch-generator, ALS CONCEPT (Leerlijn-besluit B, 'Kritisch-vorm (generator)'). Schrijft NIETS in data/: de items staan in
r13/kritisch_concept_g6.json (+ .md) voor Didactiek (vorm, taal) en Oefeningen (hints, regels). Pas na hun akkoord gaan ze de build in.
Vorm: bewering van een kind met een echte denkfout + «Klopt dat?»; meerkeuze met 3 opties «Ja, dat klopt.» / «Nee, het is [goed].» / «Nee, het is [tweede fout].»;
ronde 2 (Didactiek review-r13 §8): per somtype 2 waar + 2 fout op willekeurige nummers; 'Ja' en het goede 'Nee' even vaak op A/B/C (geschudde blokken), husselen: true;
afronden: bewering en beide Nee-opties veelvoud van de eenheid; directe rede «Noor zegt: "…" Klopt dat?» (nooit twee getallen naast elkaar); H1/H2/L1 als voorstel; guards + mutanten.
Per somtype de denkfouten uit de tabel van het besluit. Niet gegenereerd (heeft het plaatje nodig): VBN-E02 #1–#3, GET-M03 #1 → Oefeningen/Website.
Gebruik: python3 r13/kritisch_concept.py  (deterministisch, seed 13)."""
import json, os, random, re, sys, collections, itertools
from fractions import Fraction as F
R13 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, R13); import lijst as LJ
# Z-#1126 (15 okt): in de repo staat r13/g6/data niet; dan de G6-data uit claude-aanvulling/groep6/data. Het concept in de repo is mét hook
# (V-#1081, Didactiek 15 okt definitief op 1c76bc6) en wordt dan niet overschreven: uitvoer naar KRITISCH_UIT of een tijdelijke map.
G6DATA = f'{R13}/g6/data' if os.path.isdir(f'{R13}/g6/data') else os.path.join(R13, '..', 'groep6', 'data')
UIT = os.environ.get('KRITISCH_UIT') or (R13 if os.path.isdir(f'{R13}/g6/data') else __import__('tempfile').mkdtemp(prefix='kritisch_concept_'))
NAMEN = ['Lisa', 'Tom', 'Kim', 'Ali', 'Sanne', 'Bram', 'Jet', 'Daan', 'Noor', 'Milan', 'Fleur', 'Sem']
ZIJ = {'Lisa': 'Ze', 'Tom': 'Hij', 'Kim': 'Ze', 'Ali': 'Hij', 'Sanne': 'Ze', 'Bram': 'Hij', 'Jet': 'Ze', 'Daan': 'Hij', 'Noor': 'Ze', 'Milan': 'Hij', 'Fleur': 'Ze', 'Sem': 'Hij'}      # Z-#1081
OEF_KIEST = {('G6-GET-E04', 1), ('G6-MEET-E03', 2), ('G6-VERH-E02', 2)}      # V-#1081: geen natuurlijke fout aan de andere kant → Oefeningen kiest er een, anders buiten de set
def fmt(n):
    if isinstance(n, str): return n
    if isinstance(n, F):
        if n.denominator == 1: n = n.numerator
        else:
            s = f'{float(n):.3f}'.rstrip('0').rstrip('.'); return s.replace('.', ',')
    return f'{n:,}'.replace(',', '.') if n >= 10000 else str(n)
def br(f): return f'{f.numerator}/{f.denominator}'
def gen_afronden(stap, bereik, cijferplek, plek_naam, cijfer_naam):
    """Didactiek r13 §8: bewering én beide Nee-opties zijn veelvouden van de afrondeenheid (afgekapt; afgerond op de plek erboven), getallen uit het midden"""
    def g(r, extra=False):
        # V-#1081: in 1 van de 4 items (extra) is het goede antwoord zelf een veelvoud van de volgende eenheid (29.613 → 30.000); dan is de tweede fout
        # 'afgekapt op de plek erboven' (20.000), want afronden op de plek erboven geeft daar het goede antwoord
        while True:
            n = r.randint(*bereik)
            goed = (n + stap // 2) // stap * stap; f1 = n // stap * stap; f2 = (n + stap * 5) // (stap * 10) * (stap * 10); f3 = n // (stap * 10) * (stap * 10)
            if (n // cijferplek) % 10 >= 6 and bool(goed % (stap * 10) == 0) == extra and len({goed, f1, f3}) == 3: break
        fs = [(f1, 'afgekapt in plaats van afgerond')] + ([(f2, 'afgerond op een andere plek')] if f2 not in (goed, f1) else []) + ([(f3, 'afgekapt op de plek erboven')] if f3 not in (f1, f2) else [])
        return dict(ctx='', claim=lambda v: f'{fmt(n)} afgerond op {plek_naam} is {fmt(v)}.', goed=goed, eenheid_stap=stap,
                    fouten=fs,
                    h2=f'Kijk naar het cijfer van de {cijfer_naam}. Is dat 5 of meer, dan rond je naar boven af.',
                    l1={'afgekapt in plaats van afgerond': f'[naam] heeft de laatste cijfers weggelaten. Kijk naar de {cijfer_naam}: rond je dan naar boven of naar beneden af?',
                        'afgerond op een andere plek': f'Dat is afgerond op een andere plek. Op welke plek moest je afronden?',
                        'afgekapt op de plek erboven': f'Dat is afgekapt op een andere plek. Op welke plek moest je afronden, en is het cijfer erna 5 of meer?'})
    g.extra = True
    return g
def gen_noemer(r):
    b = r.choice([3, 4, 5, 6, 8]); a = r.randint(1, b - 1); k = r.choice([2, 3, 4]); c = b * k
    while F(a, b).denominator != b: a = r.randint(1, b - 1)
    return dict(ctx=f'[naam] schrijft {a}/{b} als een breuk met noemer {c}.', claim=lambda v: f'{a}/{b} is gelijk aan {v}.', goed=f'{a * k}/{c}',
                fouten=[(f'{a}/{c}', 'alleen de noemer veranderd'), (f'{a + c - b}/{c}', 'bij de teller hetzelfde opgeteld als bij de noemer'), (f'{a * k}/{b}', 'alleen de teller keer gedaan')],
                h2=f'Met welk getal doe je de noemer keer om {c} te krijgen? Doe met de teller hetzelfde.',
                l1={'alleen de noemer veranderd': 'Alleen de noemer is groter geworden. Wat moet je dan met de teller doen?',
                    'bij de teller hetzelfde opgeteld als bij de noemer': 'Je mag er niet hetzelfde bij optellen. Met welk getal doe je de noemer keer?',
                    'alleen de teller keer gedaan': 'Alleen de teller is keer gedaan. De noemer moet ook mee: welke noemer moest het worden?'})
def _kolom(x, y, vergeet_lenen=False):
    X, Y = str(x)[::-1], str(y).zfill(len(str(x)))[::-1]; uit = []; br_ = 0
    for p, q in zip(X, Y):
        p, q = int(p) - (0 if vergeet_lenen else br_), int(q)
        if p < q: uit.append(p + 10 - q); br_ = 1
        else: uit.append(p - q); br_ = 0
    return int(''.join(map(str, uit[::-1])))
def gen_aftrek(r):
    while True:
        x = r.randint(3, 8) * 1000 + r.choice([r.randint(1, 9), r.randint(1, 9) * 10 + r.randint(0, 9)]); y = r.randint(1200, x - 600)
        goed = x - y; f1 = int(''.join(str(abs(int(p) - int(q))) for p, q in zip(str(x), str(y).zfill(len(str(x)))))); f2 = _kolom(x, y, vergeet_lenen=True)
        if len({goed, f1, f2}) == 3 and f2 > 0: break
    return dict(ctx='', claim=lambda v: f'{x} − {y} = {v}.', goed=goed, fouten=[(f1, 'per kolom de kleinste van de grootste'), (f2, 'lenen vergeten (over de nul)')],
                h2='Reken van rechts naar links. Is het bovenste cijfer kleiner, dan leen je eerst.',
                l1={'per kolom de kleinste van de grootste': 'Er is per kolom het kleinste van het grootste afgehaald. Kijk welk getal bovenaan staat: moet je lenen?',
                    'lenen vergeten (over de nul)': 'Er is geleend, maar niet doorgegeven. Wat gebeurt er met het cijfer waar je van leent?'})
def gen_deel_van(euro):
    def g(r):
        while True:
            n = r.choice([4, 5, 6, 8]); t = r.randint(2, n - 1)
            if F(t, n).denominator != n: continue
            x = n * r.randint(3, 15 if euro else 10)
            if not euro and x > 120: continue
            goed, f1, f2 = x * t // n, x // t if x % t == 0 else None, x // n
            f3 = x * n // t if euro and x * n % t == 0 else None      # V-#1081 E09 #1: 5/3 van €75 = €125
            if f1 and len({goed, f1, f2}) == 3 and (not euro or (f3 and f3 not in (goed, f1, f2))): break
        e = '€' if euro else ''
        return dict(ctx='', claim=lambda v: f'{t}/{n} van {e}{x} is {v}.', goed=f'{e}{goed}', fouten=[(f'{e}{f1}', 'gedeeld door de teller in plaats van door de noemer'), (f'{e}{f2}', 'alleen één deel genomen')]
                    + ([(f'{e}{f3}', 'teller en noemer omgedraaid')] if f3 else []),
                    h2='Deel eerst door de noemer: hoeveel is één deel? Hoeveel delen heb je nodig?',
                    l1={'gedeeld door de teller in plaats van door de noemer': 'Er is gedeeld door de teller. Door welk getal deel je om één deel te krijgen?',
                        'alleen één deel genomen': 'Dat is één deel. Hoeveel delen heb je nodig?',
                        'teller en noemer omgedraaid': 'Teller en noemer zijn omgedraaid. Door welk getal deel je, en hoeveel delen neem je?'})
    return g
def gen_ttxtt(r):
    while True:
        x, y = r.randint(13, 39), r.randint(13, 29)
        if x % 10 and y % 10:
            goed = x * y; f1 = (x // 10 * 10) * (y // 10 * 10) + (x % 10) * (y % 10); f2 = x * (y // 10 * 10); f3 = (x + 5) // 10 * 10 * y
            if len({goed, f1, f2, f3}) == 4: break
    return dict(ctx='', claim=lambda v: f'{x} × {y} = {fmt(v)}.', goed=goed, fouten=[(f1, 'alleen tientallen × tientallen en eenheden × eenheden'), (f2, 'de eenheden van de tweede factor vergeten'),
                                                                                   (f3, 'afgerond en niet teruggerekend')],      # V-#1081: 30 × 26 = 780 (29 afgerond, niet terug)
                h2='Splits één getal in tientallen en eenheden. Doe beide delen keer het andere getal en tel op.',
                l1={'alleen tientallen × tientallen en eenheden × eenheden': 'Er missen twee stukken: de tientallen keer de eenheden. Maak alle vier de stukken.',
                    'de eenheden van de tweede factor vergeten': 'De eenheden van het tweede getal zijn vergeten. Reken die er ook bij.',
                    'afgerond en niet teruggerekend': 'Het eerste getal is afgerond, maar daarna niet teruggerekend. Hoeveel moet je er nog af of bij doen?'})
def gen_onthoud(r):
    while True:
        x, d = r.randint(213, 689), r.randint(3, 8)
        # V-#1083: wie het onthouden vergeet, schrijft per kolom alleen de eenheden op, maar de laatste (linker) kolom helemaal: 365 × 7 → 2125, niet 125
        goed = x * d; s_ = str(x); f1 = int(str(int(s_[0]) * d) + ''.join(str(int(c) * d % 10) for c in s_[1:])); f2 = (x // 10 * 10) * d; f3 = (x + 5) // 10 * 10 * d
        if len({goed, f1, f2, f3}) == 4 and x % 10: break
    return dict(ctx='', claim=lambda v: f'{x} × {d} = {fmt(v)}.', goed=goed, fouten=[(f1, 'onthouden vergeten'), (f2, 'de eenheden vergeten'), (f3, 'afgerond en niet teruggerekend')],
                h2='Reken van rechts naar links. Wat je onthoudt, tel je bij de volgende kolom op.',
                l1={'onthouden vergeten': 'Het onthouden is vergeten. Wat schrijf je op en wat neem je mee naar de volgende kolom?',
                    'de eenheden vergeten': 'De eenheden zijn niet meegerekend. Reken ook die keer het getal.',
                    'afgerond en niet teruggerekend': 'Het getal is afgerond, maar daarna niet teruggerekend. Hoeveel moet je er nog af of bij doen?'})
def gen_verander(r):
    while True:
        x = r.randint(12000, 88000); stap = r.choice([10, 100, 1000]); d = (x // stap) % 10
        if 1 <= d <= 8: break
    y = x + stap if r.random() < .5 else x - stap
    andere = {10: 100, 100: 1000, 1000: 100}[stap]; ander2 = {10: 1, 100: 10, 1000: 10000}[stap]      # V-#1081: plekwaarde aan de andere kant
    return dict(ctx=f'Het getal {fmt(x)} wordt {fmt(y)}.', claim=lambda v: f'Het getal verandert met {fmt(v)}.', goed=stap,
                fouten=[(andere, 'naar de verkeerde plek gekeken'), ((x // stap) % 10, 'het cijfer genomen in plaats van de waarde'), (ander2, 'naar de verkeerde plek gekeken (andere kant)')],
                h2='Zet de twee getallen onder elkaar. Welk cijfer is anders, en wat is de waarde van die plek?',
                l1={'naar de verkeerde plek gekeken': 'Kijk nog eens welk cijfer veranderd is. Op welke plek staat het?',
                    'naar de verkeerde plek gekeken (andere kant)': 'Kijk nog eens welk cijfer veranderd is. Op welke plek staat het?',
                    'het cijfer genomen in plaats van de waarde': 'Dat is het cijfer, niet de waarde. Hoeveel is één stap op die plek?'})
def gen_meer(teken):
    def g(r):
        while True:
            x = r.randint(12000, 88000); s = r.choice([10, 100, 1000])
            sg = 1 if teken == '+' else -1
            goed = x + sg * s; f1 = x + sg * (s * 10 if s < 1000 else s // 10); f2 = x + sg * (s // 10 if s > 10 else s * 100)
            if len({goed, f1, f2}) == 3: break
        w = 'meer' if teken == '+' else 'minder'
        return dict(ctx='', claim=lambda v: f'{fmt(s)} {w} dan {fmt(x)} is {fmt(v)}.', goed=goed, fouten=[(f1, 'op de verkeerde plek erbij of eraf'), (f2, 'op de verkeerde plek erbij of eraf (andere kant)')],
                    h2=f'Op welke plek verandert er iets als je {fmt(s)} {"erbij doet" if teken == "+" else "eraf haalt"}?',
                    l1={'op de verkeerde plek erbij of eraf': 'Dat is op een andere plek veranderd. Bij welke plek hoort ' + fmt(s) + '?',
                        'op de verkeerde plek erbij of eraf (andere kant)': 'Dat is op een andere plek veranderd. Bij welke plek hoort ' + fmt(s) + '?'})
    return g
FACTOR = {('cm', 'm'): F(1, 100), ('km', 'm'): 1000, ('m', 'mm'): 1000, ('hm', 'm'): 100, ('m', 'hm'): F(1, 100), ('km', 'hm'): 10, ('hm', 'km'): F(1, 10),
          ('L', 'cl'): 100, ('cl', 'L'): F(1, 100), ('L', 'ml'): 1000, ('L', 'dl'): 10, ('dl', 'L'): F(1, 10), ('dl', 'ml'): 100, ('ml', 'dl'): F(1, 100), ('kg', 'g'): 1000}
BANK_Q = {}      # V-#1082: startgetallen uit het oorspronkelijke G6-somtype (basis/toepassen), gevuld in main()
def gen_omreken(u, v, bank=()):
    """V-#1081: kandidaat-fouten aan beide kanten (buurmaat ×10 / :10, het getal overgenomen, de verkeerde kant op); main() kiest per item twee, zodat het
    goede getal per somtype hooguit 2× dezelfde rang heeft. V-#1082: startgetal uit het midden van de bank (geen «1 kg is 1000 g»), per somtype elk getal één keer.
    V-#1084: de L1 vraagt altijd vanaf de grote maat («Hoeveel cm is één m?»)."""
    f = F(FACTOR[(u, v)])
    groot, klein = (u, v) if f > 1 else (v, u)
    groter = 'tien keer te groot (factor van een buurmaat)'; kleiner = 'tien keer te klein (factor van een buurmaat)'; om = 'de verkeerde kant op gerekend'; over = 'het getal overgenomen'
    vraag = f'Hoeveel {klein} is één {groot}?'
    L1 = {groter: f'Dat is tien keer te veel. {vraag}', kleiner: f'Dat is tien keer te weinig. {vraag}',
          om: (f'Er is gedeeld in plaats van keer gedaan. Is een {u} groter of kleiner dan een {v}?' if f > 1 else f'Er is keer gedaan in plaats van gedeeld. Is een {u} groter of kleiner dan een {v}?'),
          over: f'Het getal is niet omgerekend. {vraag}'}
    qs = sorted(set(bank)); qs = qs[len(qs) // 5: len(qs) - len(qs) // 5] if len(qs) >= 8 else qs      # midden van de bank
    def g(r):
        for poging in range(400):
            q = r.choice(qs) if qs else r.randint(3, 40) * (f.denominator * 10 if f.denominator > 1 else 1)
            goed = q * f
            if goed.denominator != 1: continue
            fs, gezien = [], {goed}
            for w, l in [(goed * 10, groter), (goed / 10, kleiner), (q, over), (q / f, om)]:
                l = over if w == q else l
                if 10 % F(w).denominator == 0 and w not in gezien: fs.append((w, l)); gezien.add(w)      # hele getallen of één decimaal («300 ml is 0,3 dl»)
            if len(fs) >= 3: break
        return dict(ctx='', claim=lambda w: f'{fmt(q)} {u} is {w} {v}.', goed=fmt(int(goed)), fouten=[(fmt(F(w)), l) for w, l in fs], eenheid=v, sleutel=(q, u),
                    h2=f'Hoeveel {v} gaat er in één {u}? Reken daarmee.' if f >= 1 else f'Hoeveel {u} gaat er in één {v}? Reken daarmee.', l1=L1)
    return g
def gen_opp(r):
    while True:
        l, b = r.randint(4, 12), r.randint(2, 9)
        goed, f1, f2 = l * b, 2 * (l + b), l + b
        if len({goed, f1, f2}) == 3 and l != b: break
    return dict(ctx=f'Een rechthoek is {l} cm lang en {b} cm breed.', claim=lambda v: f'De oppervlakte is {v} cm².', goed=goed, fouten=[(f1, 'de omtrek uitgerekend'), (f2, 'lengte en breedte opgeteld')], eenheid='cm²',
                h2='Hoeveel vierkantjes van 1 cm² passen er in één rij? En hoeveel rijen zijn er?',
                l1={'de omtrek uitgerekend': 'Dat is de omtrek: de rand eromheen. De oppervlakte is wat erbinnen past.', 'lengte en breedte opgeteld': 'Lengte en breedte zijn opgeteld. Hoeveel rijen van vierkantjes passen erin?'})
def gen_zijde(r):
    while True:
        s, z = r.randint(3, 9), r.randint(4, 12); A = s * z
        goed, f1, f2 = z, A - s, A // 2
        if A % 2 == 0 and len({goed, f1, f2}) == 3: break
    return dict(ctx=f'Een rechthoek heeft een oppervlakte van {A} cm². Eén zijde is {s} cm.', claim=lambda v: f'De andere zijde is {v} cm.', goed=goed, eenheid='cm',
                fouten=[(f1, 'de zijde afgetrokken in plaats van gedeeld'), (f2, 'de oppervlakte gehalveerd')],
                h2='Welk getal keer de bekende zijde geeft de oppervlakte?',
                l1={'de zijde afgetrokken in plaats van gedeeld': 'Er is afgetrokken. De oppervlakte is lengte keer breedte: welke som past daarbij?', 'de oppervlakte gehalveerd': 'De oppervlakte is door twee gedeeld. Door welk getal moet je delen?'})
def gen_koekjes(r):
    while True:
        n = r.choice([3, 4, 5, 6]); t = r.randint(2, n - 1); K = n * r.randint(2, 5)
        goed, f1, f2 = K * t // n, t, K // n
        if F(t, n).denominator == n and len({goed, f1, f2}) == 3: break
    return dict(ctx='', claim=lambda v: f'{t}/{n} van {K} koekjes is {v} koekjes.', goed=goed, fouten=[(f1, 'de teller overgenomen'), (f2, 'alleen één deel genomen')], eenheid='koekjes',
                h2='Verdeel de koekjes eerst in gelijke groepjes. Hoeveel groepjes heb je nodig?',
                l1={'de teller overgenomen': 'Dat is de teller, niet het aantal koekjes. Hoeveel koekjes zitten er in één deel?', 'alleen één deel genomen': 'Dat is één deel. Hoeveel delen heb je nodig?'})
def gen_verdeel(r):
    while True:
        n = r.randint(3, 8); a = r.randint(2, n - 1)
        if F(a, n).denominator == n: break
    return dict(ctx=f'{a} taarten worden eerlijk verdeeld over {n} kinderen.', claim=lambda v: f'Elk kind krijgt {v} taart.', goed=f'{a}/{n}',
                fouten=[(f'{n}/{a}', 'teller en noemer omgedraaid'), (f'1/{n}', 'alleen naar het aantal kinderen gekeken'), ('1', 'elk kind een hele taart')], eenheid='taart',      # V-#1081
                h2='Wat wordt er verdeeld, en over hoeveel kinderen? Dat zijn de teller en de noemer.',
                l1={'teller en noemer omgedraaid': 'Teller en noemer zijn omgedraaid. Wat wordt er verdeeld: dat komt boven de streep.', 'alleen naar het aantal kinderen gekeken': 'Dat is wat een kind krijgt van één taart. Hoeveel taarten zijn er?',
                    'elk kind een hele taart': 'Er zijn minder taarten dan kinderen. Kan elk kind dan een hele taart krijgen?'})
GEN = {('G6-GET-E01', 1): gen_afronden(1000, (12000, 88000), 100, 'duizendtallen', 'honderdtallen'), ('G6-GET-E01', 2): gen_afronden(100, (1200, 8800), 10, 'honderdtallen', 'tientallen'),
       ('G6-GET-E03', 4): gen_noemer, ('G6-GET-E04', 1): gen_aftrek, ('G6-GET-E09', 1): gen_deel_van(True), ('G6-GET-E09', 2): gen_deel_van(False),
       ('G6-GET-M02', 1): gen_verander, ('G6-GET-M02', 2): gen_meer('+'), ('G6-GET-M02', 3): gen_meer('-'), ('G6-GET-M06', 1): gen_onthoud, ('G6-GET-E06', 1): gen_ttxtt,
       ('G6-MEET-E03', 1): gen_opp, ('G6-MEET-E03', 2): gen_zijde, ('G6-VERH-E02', 2): gen_koekjes, ('G6-VERH-E03', 1): gen_verdeel}
for (d, n, w) in LJ.R13_34:
    if d in ('G6-MEET-E01', 'G6-MEET-E04', 'G6-MEET-E05'): GEN[(d, n)] = None      # Regel M: maten uit de kop
NIET = {('G6-VBN-E02', 1): 'lijngrafiek nodig (bewering over een aflezing)', ('G6-VBN-E02', 2): 'lijngrafiek nodig', ('G6-VBN-E02', 3): 'lijngrafiek nodig (of schatten «meer of minder dan 200?»)',
        ('G6-GET-M03', 1): 'getallenlijn nodig'}
H1 = 'Reken het eerst zelf uit, zonder naar het antwoord van [naam] te kijken. Krijg je hetzelfde?'
L1_NEE_OP_WAAR = 'Reken het nog eens na. Wat krijg jij? Klopt dat met wat [naam] zegt?'
GETAL = r'€?\d+(?:[.,]\d+)*(?:/\d+)?'
def _getal_waarde(t):
    t = str(t).replace('€', '').strip()
    if '/' in t: a, b = t.split('/'); return F(int(a), int(b))
    return F(t.replace('.', '').replace(',', '.'))
def guards(items, gen_info):
    """Didactiek r13 §8 'Guards': waar-aandeel per doel 40–60 %; per letter X: P(goed | Ja op X) in [0,2; 0,6]; afronden: bewering en beide Nee-opties veelvoud
    van de afrondeenheid; geen twee getallen direct na elkaar in de bewering; per foute optie een L1; het ware item niet steeds op dezelfde plek; geen kloktijd-':'."""
    F_ = []
    per_doel = collections.defaultdict(lambda: [0, 0])
    for it in items: per_doel[it['doelId']][0] += it['beweringKlopt']; per_doel[it['doelId']][1] += 1
    for d, (w, n) in per_doel.items():
        if not 0.4 <= w / n <= 0.6: F_.append(f'waar-aandeel {d}: {w}/{n}')
    for X in 'ABC':
        ja = [it for it in items if it['opties']['ABC'.index(X)]['tekst'] == 'Ja, dat klopt.']
        if ja:
            p = sum(it['beweringKlopt'] for it in ja) / len(ja)
            if not 0.2 <= p <= 0.6: F_.append(f"P(goed | Ja op {X}) = {p:.2f} ({len(ja)} items)")
    plek = collections.Counter(int(it['id'].rsplit('-', 1)[1]) for it in items if it['beweringKlopt'])
    if len(plek) < 3: F_.append(f'het ware item staat op te weinig plekken: {dict(plek)}')
    for it in items:
        stap = gen_info.get(it['id'], {}).get('eenheid_stap')
        if stap:
            waarden = [it['bewering']] + [re.search(GETAL, o['tekst']).group(0) for o in it['opties'] if o['tekst'].startswith('Nee')]
            for w in waarden:
                if _getal_waarde(w) % stap: F_.append(f"{it['id']}: afrondvorm: {w} is geen veelvoud van {stap}")
        cl = it['claim']
        if re.search(rf'{GETAL}\s+{GETAL}', cl.replace(' × ', ' x ').replace(' − ', ' - ')): F_.append(f"{it['id']}: twee getallen direct na elkaar: {cl}")
        if re.search(r'\d\s*:\s*\d', it['opgave']): F_.append(f"{it['id']}: ':' tussen getallen")
        for o in it['opties']:
            if o['tekst'] != it['antwoord'] and not it['conceptHints']['L1'].get(o['tekst']): F_.append(f"{it['id']}: geen L1 bij foute optie {o['tekst']!r}")
        if len({o['tekst'] for o in it['opties']}) != 3: F_.append(f"{it['id']}: dubbele opties")
        bb = gen_info.get(it['id'], {}).get('bank')
        if bb and not bb[0] <= gen_info[it['id']]['q'] <= bb[1]: F_.append(f"{it['id']}: niveau: {gen_info[it['id']]['q']} buiten het bereik van het G6-somtype {bb}")
    F_ += rang_open(items)[0]
    som = collections.defaultdict(list)
    for it in items: som[(it['doelId'], it.get('somtypeNrOrigineel'))].append(it)
    for k_, its in som.items():      # V-#1082: elke som (getallen + context) per somtype één keer
        c = collections.Counter(som_sleutel(it) for it in its)
        for sl, n_ in c.items():
            if n_ > 1: F_.append(f"dubbele som {k_[0]} #{k_[1]}: {sl!r} {n_}×")
    return F_
def som_sleutel(it):
    t = it['opgave'].replace(it['claim'], '□'.join(it['claim'].rsplit(it['bewering'], 1)))
    return re.sub(r'\b(' + '|'.join(NAMEN + ['Ze', 'Hij']) + r')\b', 'X', t)
def rang_goed(it):
    """V-#1081: rang van het goede getal in {bewering, Nee, Nee}: 'klein', 'midden' of 'groot'"""
    nee = [re.search(GETAL, o['tekst']).group(0) for o in it['opties'] if o['tekst'].startswith('Nee')]
    goed = it['bewering'] if it['beweringKlopt'] else re.search(GETAL, it['antwoord']).group(0)
    w = sorted({_getal_waarde(x) for x in [it['bewering']] + nee})
    return ('klein', 'midden', 'groot')[w.index(_getal_waarde(goed))] if len(w) == 3 else '?'
def rang_open(items):
    """V-#1081-guard: per somtype hooguit 2 van de 4 goede getallen op dezelfde rang (bewering meegeteld). Somtypes in OEF_KIEST: open bij Oefeningen (geen FAIL)."""
    F_, open_ = [], []
    som = collections.defaultdict(list)
    for it in items: som[(it['doelId'], it.get('somtypeNrOrigineel'))].append(rang_goed(it))
    for k_, rs in som.items():
        c = collections.Counter(rs)
        if max(c.values()) > 2 or '?' in c: (open_ if k_ in OEF_KIEST else F_).append(f"rang {k_[0]} #{k_[1]}: {dict(c)}")
    return F_, open_
def kies_paren(xs, r):
    """V-#1081: kies per item twee van de kandidaat-fouten, zodat het goede getal per somtype hooguit 2× dezelfde rang heeft; liefst de eerste twee (vaste denkfouten)"""
    def rg(x, p):
        w = sorted({_getal_waarde(fmt(v) if isinstance(v, (int, F)) else v) for v in [x['goed'], x['fouten'][p[0]][0], x['fouten'][p[1]][0]]})
        return w.index(_getal_waarde(fmt(x['goed']) if isinstance(x['goed'], (int, F)) else x['goed'])) if len(w) == 3 else 9
    opties = [sorted(itertools.combinations(range(len(x['fouten'])), 2), key=lambda p: (p != (0, 1), max(p), sum(p))) for x in xs]
    beste = None
    for combo in itertools.product(*opties):
        c = collections.Counter(rg(x, p) for x, p in zip(xs, combo))
        sc = (max(c.values()) > 2 or 9 in c, sum(p != (0, 1) for p in combo), r.random())
        if beste is None or sc < beste[0]: beste = (sc, combo)
    return list(beste[1]), not beste[0][0]
def guard_mutanten():
    """les 321: de guards vuren op de oude conceptvorm (r13 983900d: waar steeds nr. 4, 'Ja' nooit op C bij fout, afronden 99.800, getallen naast elkaar)"""
    def it(i, klopt, ja, claim, bew='1', ops=None, stap=None):
        o = ops or ['Ja, dat klopt.', 'Nee, het is 2.', 'Nee, het is 3.']
        o = o[:]; o.remove('Ja, dat klopt.'); o.insert(ja, 'Ja, dat klopt.')
        a = 'Ja, dat klopt.' if klopt else next(x for x in o if x != 'Ja, dat klopt.')
        return {'id': f'MUT-{i}', 'doelId': 'MUT', 'beweringKlopt': klopt, 'opties': [{'letter': 'ABC'[k], 'tekst': t} for k, t in enumerate(o)], 'antwoord': a,
                'claim': claim, 'opgave': claim, 'bewering': bew, 'conceptHints': {'L1': {t: 'x' for t in o if t != a}}}, ({f'MUT-{i}': {'eenheid_stap': stap}} if stap else {})
    oud = [it(f'{s}-{k}', k == 4, [0, 1, 0, 1, 0][k], '4/5 van 80 20 is') for s in range(3) for k in (1, 2, 3, 4)]
    items = [x for x, _ in oud]; info = {}
    for _, i_ in oud: info.update(i_)
    F_ = guards(items, info)
    af, af_i = it('afr', False, 0, 'x', bew='99800', ops=['Ja, dat klopt.', 'Nee, het is 100.000.', 'Nee, het is 99.820.'], stap=1000)
    return {'waar-aandeel': any(x.startswith('waar-aandeel') for x in F_), 'Ja-op-letter': any(x.startswith('P(goed') for x in F_),
            'ware-plek': any(x.startswith('het ware item') for x in F_), 'getallen-naast-elkaar': any('twee getallen' in x for x in F_),
            'afrondvorm': any('afrondvorm' in x for x in guards([af], af_i)),
            'rang (V-#1081)': bool(rang_open([dict(it('r', False, 0, f'{fmt(q)} cm is {fmt(q // 100)} m.', bew=fmt(q * 10 // 100), ops=['Ja, dat klopt.', f'Nee, het is {fmt(q // 100)} m.', f'Nee, het is {fmt(q // 1000)} m.'])[0],
                                                     doelId='MUT-R', somtypeNrOrigineel=1, antwoord=f'Nee, het is {fmt(q // 100)} m.') for q in (41000, 30000, 28000, 15000)])[0]),
            'dubbele som (V-#1082)': any(x.startswith('dubbele som') for x in guards([dict(it(f'd{k}', False, 0, '2 kg is 200 g.', bew='200')[0], doelId='MUT-D', somtypeNrOrigineel=1, opgave='Noor zegt: "2 kg is 200 g." Klopt dat?') for k in (1, 2)], {})),
            'niveau (V-#1082)': any('niveau' in x for x in guards([it('n', False, 0, '1 kg is 100 g.', bew='100')[0]], {'MUT-n': {'q': 1, 'bank': (11, 28)}}))}
def main():
    r = random.Random(13); kop = {}
    G = json.load(open(f'{G6DATA}/gemapt.json'))['items']
    for it in G:
        if it['merge'].get('status') == 'gemapt':
            kop.setdefault((it['merge']['doel'], it['merge']['somtypeNrOrigineel']), it['merge']['somtype'])
            mq = re.fullmatch(r'([\d.]+) \w+ = □ \w+', it['opgave'].strip())
            if mq and it.get('niveau') in ('basis', 'toepassen'): BANK_Q.setdefault((it['merge']['doel'], it['merge']['somtypeNrOrigineel']), []).append(int(mq.group(1).replace('.', '')))
    items, niet, info, nm_i = [], [], {}, 0
    ja_waar, ja_fout, nee_goed = [], [], []      # geschudde blokken van 3 posities: 'Ja' en het goede 'Nee' even vaak op A, B en C
    def pak(lijst):
        if not lijst: blok = [0, 1, 2]; r.shuffle(blok); lijst.extend(blok)
        return lijst.pop()
    for d, n, w in LJ.R13_34:
        g = GEN.get((d, n))
        if (d, n) in NIET: niet.append({'somtype': f'{d} #{w} (nrO {n})', 'reden': NIET[(d, n)]}); continue
        if g is None:
            m = re.fullmatch(r'# (\w+) = □ (\w+)', kop[(d, n)]); g = gen_omreken(m.group(1), m.group(2), BANK_Q.get((d, n), ()))
        waar = set(r.sample(range(4), 2))      # §8: 2 waar + 2 fout per somtype, op willekeurige itemnummers
        bijz = r.randrange(4)      # V-#1081 afronden: één item met het veelvoud van de volgende eenheid als goed antwoord
        for poging in range(200):      # V-#1081: lukt de rangspreiding niet met deze 4 sommen, dan 4 nieuwe
            xs, gehad = [], set()
            for k in range(4):
                for _ in range(500):      # V-#1082: elke som per somtype één keer
                    x = g(r, extra=(k == bijz)) if getattr(g, 'extra', False) else g(r)
                    sl = x.get('sleutel') or (x['ctx'], x['claim']('□'))
                    if sl not in gehad: break
                gehad.add(sl); xs.append(x)
            paren, ok_ = kies_paren(xs, r)
            if ok_ or (d, n) in OEF_KIEST: break
        fout_ks = [k for k in range(4) if k not in waar]; fk_volg = [0, 1]; r.shuffle(fk_volg)      # V-#1081 (M02 #1): de twee foute beweringen komen uit verschillende denkfouten
        for k in range(4):
            x = dict(xs[k]); x['fouten'] = [xs[k]['fouten'][paren[k][0]], xs[k]['fouten'][paren[k][1]]]; e_ = x.get('eenheid')
            def T(v): return (fmt(v) if isinstance(v, (int, F)) else str(v)) + (f' {e_}' if e_ else '')
            def NEE(v):
                meer = e_ == 'koekjes' and str(v) != '1'
                return f"Nee, het {'zijn' if meer else 'is'} {T(v)}."
            naam = NAMEN[nm_i % len(NAMEN)]; nm_i += 1
            klopt = k in waar; goed = x['goed']; fouten = x['fouten']
            fk = r.randrange(2) if klopt else fk_volg[fout_ks.index(k)]      # welke denkfout de bewering is (fout item) of als eerste 'Nee' staat (waar item)
            bewering = goed if klopt else fouten[fk][0]
            if klopt:
                goed_optie = 'Ja, dat klopt.'; nee = [(NEE(fouten[0][0]), fouten[0][1]), (NEE(fouten[1][0]), fouten[1][1])]
                pj = pak(ja_waar); ops = [None] * 3; ops[pj] = goed_optie; rest = [i_ for i_ in range(3) if i_ != pj]; r.shuffle(rest)
                ops[rest[0]], ops[rest[1]] = nee[0][0], nee[1][0]
                L1 = {nee[0][0]: x['l1'][nee[0][1]], nee[1][0]: x['l1'][nee[1][1]]}
                dpo = {t_: dk for t_, dk in nee}
                # Z-#1080: 'Nee' op een waar item krijgt de L1 van die denkfout (het kind rekende zelf zo); niet meer 'Reken het nog eens na'
                L1 = {t_: v_.replace('[naam] heeft', 'Je hebt') for t_, v_ in L1.items()}
            else:
                goed_optie = NEE(goed); andere = fouten[1 - fk]
                if not ja_fout: blok = list(itertools.permutations(range(3))); r.shuffle(blok); ja_fout.extend(blok)      # alle 6 volgordes (Ja, goed-Nee, fout-Nee) even vaak
                pj, pg, pf = ja_fout.pop(); ops = [None] * 3; ops[pj] = 'Ja, dat klopt.'; ops[pg] = goed_optie; ops[pf] = NEE(andere[0])
                L1 = {'Ja, dat klopt.': x['l1'][fouten[fk][1]].replace('[naam]', naam), NEE(andere[0]): x['l1'][andere[1]].replace('[naam] heeft', 'Je hebt')}
                dpo = {'Ja, dat klopt.': f'de bewering geloofd ({fouten[fk][1]})', NEE(andere[0]): andere[1]}
            claim = x['claim'](fmt(bewering))
            ctx = x['ctx'].replace('[naam]', naam)
            opg = (ctx + ' ' if ctx else '') + f'{ZIJ[naam] if naam in ctx else naam} zegt: "{claim}" Klopt dat?'      # Z-#1081: «… Ze zegt: …»
            iid = f'{d}-r13-kritisch-{w:02d}-{k + 1}'
            if 'eenheid_stap' in x: info[iid] = {'eenheid_stap': x['eenheid_stap']}
            if BANK_Q.get((d, n)) and x.get('sleutel'): info[iid] = {'q': x['sleutel'][0], 'bank': (min(BANK_Q[(d, n)]), max(BANK_Q[(d, n)]))}
            items.append({'id': iid, 'status': 'concept (niet in data; wacht op Didactiek en Oefeningen)', 'doelId': d, 'somtypeNrOrigineel': n, 'weergaveNr': w,
                          'kop': kop.get((d, n)), 'niveau': 'kritisch', 'niveauKind': 'Uitdaging', 'type': 'meerkeuze', 'opgave': opg, 'claim': claim,
                          'bewering': fmt(bewering) if isinstance(bewering, (int, F)) else str(bewering),
                          'opties': [{'letter': 'ABC'[i_], 'tekst': o} for i_, o in enumerate(ops)], 'antwoord': goed_optie,
                          'antwoordDetail': {'juisteOptie': 'ABC'[ops.index(goed_optie)], 'juisteOptieTekst': goed_optie}, 'husselen': True,
                          'beweringKlopt': klopt, 'denkfoutPerOptie': dpo,
                          'conceptHints': {'status': 'voorstel Overzicht (Didactiek §8); Oefeningen schrijft de definitieve tekst', 'H1': H1.replace('[naam]', naam), 'H2': x['h2'],
                                           'L1': {t_: v_.replace('[naam]', naam) for t_, v_ in L1.items()}}})
    F_ = guards(items, info); M = guard_mutanten()
    assert not F_, F_
    assert all(M.values()), M
    kl = collections.Counter(it['antwoordDetail']['juisteOptie'] for it in items)
    ja = {X: (sum(1 for it in items if it['opties']['ABC'.index(X)]['tekst'] == 'Ja, dat klopt.' and it['beweringKlopt']), sum(1 for it in items if it['opties']['ABC'.index(X)]['tekst'] == 'Ja, dat klopt.')) for X in 'ABC'}
    stat = {'waar': sum(it['beweringKlopt'] for it in items), 'fout': sum(not it['beweringKlopt'] for it in items), 'goedeLetter': dict(sorted(kl.items())),
            'jaOpLetter (waar/alle)': ja, 'wareItemNummer': dict(sorted(collections.Counter(int(it['id'].rsplit('-', 1)[1]) for it in items if it['beweringKlopt']).items())),
            'guards': 'FAIL 0', 'guardMutanten': M}
    uit = {'uitleg': __doc__, 'aantal': len(items), 'somtypes': len({(i['doelId'], i['somtypeNrOrigineel']) for i in items}), 'statistiek': stat, 'nietGegenereerd': niet, 'items': items}
    json.dump(uit, open(f'{UIT}/kritisch_concept_g6.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    L = ['# r13 L-R10b: kritisch-items G6 (CONCEPT, niet in data)', '',
         f'{len(items)} items in {uit["somtypes"]} somtypes: per somtype 2 beweringen waar en 2 fout, op willekeurige itemnummers. Bron: `r13/kritisch_concept.py` (seed 13). Ronde 2 volgens Didactiek review-r13 §8.',
         '', f"**Statistiek:** waar {stat['waar']} · fout {stat['fout']} · goede letter {stat['goedeLetter']} · 'Ja' op A/B/C (waar/alle) {ja} · nummer van het ware item {stat['wareItemNummer']}.",
         f"**Guards** (§8): waar-aandeel per doel 40–60 %, P(goed | Ja op X) 0,2–0,6, afrondvorm, geen twee getallen naast elkaar, L1 bij elke foute optie, ware item op wisselende plek: FAIL 0. Guard-mutanten (oude conceptvorm): {M}.",
         '', 'Taalvorm: directe rede, «Noor zegt: "4/5 van 80 is 20." Klopt dat?»; «Nee, het zijn 6 koekjes.». husselen: true. Getallen uit het midden (afronden 12.000–88.000; omrekenen ≤ 2.000).',
         '', 'Niet gegenereerd: ' + '; '.join(f"{x['somtype']} ({x['reden']})" for x in niet) + '.', '',
         'Voor Oefeningen: H1 (alle somtypes), H2 per somtype en L1 per foute optie staan als voorstel in `conceptHints`; definitieve teksten en regels zijn van Oefeningen. Voor Didactiek: alternatief in twee stappen (eerst Ja/Nee, dan het getal typen; Leerlijn onduidelijk 6) staat open.', '']
    for i in items: L.append(f"- `{i['id']}` {i['opgave']} → **{i['antwoord']}** · opties: " + ' / '.join(o['tekst'] for o in i['opties']) + f" · H2: {i['conceptHints']['H2']}")
    open(f'{UIT}/kritisch_concept_g6.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(len(items), 'items,', uit['somtypes'], 'somtypes; niet:', len(niet)); print(json.dumps(stat, ensure_ascii=False))
if __name__ == '__main__': main()
