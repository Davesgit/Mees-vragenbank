#!/usr/bin/env python3
"""r13 L-R10b: kritisch-generator, ALS CONCEPT (Leerlijn-besluit B, 'Kritisch-vorm (generator)'). Schrijft NIETS in data/: de items staan in
r13/kritisch_concept_g6.json (+ .md) voor Didactiek (vorm, taal) en Oefeningen (hints, regels). Pas na hun akkoord gaan ze de build in.
Vorm: bewering van een kind met een echte denkfout + «Klopt dat?»; meerkeuze met 3 opties «Ja, dat klopt.» / «Nee, het is [goed].» / «Nee, het is [tweede fout].»;
goed antwoord op wisselende plek (A/B/C); per somtype 4 items: 3 beweringen fout (denkfouten om en om), 1 klopt. Geen ':' in opgave en opties.
Per somtype de denkfouten uit de tabel van het besluit. Niet gegenereerd (heeft het plaatje nodig): VBN-E02 #1–#3, GET-M03 #1 → Oefeningen/Website.
Gebruik: python3 r13/kritisch_concept.py  (deterministisch, seed 13)."""
import json, os, random, re, sys, collections
from fractions import Fraction as F
R13 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, R13); import lijst as LJ
NAMEN = ['Lisa', 'Tom', 'Kim', 'Ali', 'Sanne', 'Bram', 'Jet', 'Daan', 'Noor', 'Milan', 'Fleur', 'Sem']
def fmt(n):
    if isinstance(n, F):
        if n.denominator == 1: n = n.numerator
        else:
            s = f'{float(n):.3f}'.rstrip('0').rstrip('.'); return s.replace('.', ',')
    return f'{n:,}'.replace(',', '.') if n >= 10000 else str(n)
def br(f): return f'{f.numerator}/{f.denominator}'
def gen_afronden(stap, bereik, cijferplek, plek_naam, fout2_stap):
    def g(r):
        while True:
            n = r.randint(*bereik)
            if (n // cijferplek) % 10 >= 6 and n % fout2_stap: break
        goed = (n + stap // 2) // stap * stap; f1 = n // stap * stap; f2 = (n + fout2_stap // 2) // fout2_stap * fout2_stap
        return dict(zin=lambda nm, v: f'{nm} rondt {fmt(n)} af op {plek_naam} en krijgt {fmt(v)}. Klopt dat?', goed=goed, fouten=[(f1, 'afgekapt in plaats van afgerond'), (f2, f'afgerond op een andere plek ({ {10: "tientallen", 100: "honderdtallen"}[fout2_stap] })')])
    return g
def gen_noemer(r):
    b = r.choice([3, 4, 5, 6, 7, 8]); a = r.randint(1, b - 1); k = r.choice([3, 4]); c = b * k
    goed = f'{a * k}/{c}'; f1 = f'{a}/{c}'; f2 = f'{a + c - b}/{c}'
    return dict(zin=lambda nm, v: f'{nm} schrijft {a}/{b} met noemer {c} als {v}. Klopt dat?', goed=goed, fouten=[(f1, 'alleen de noemer veranderd'), (f2, 'bij de teller hetzelfde opgeteld als bij de noemer')])
def _kolom(x, y, vergeet_lenen=False):
    X, Y = str(x)[::-1], str(y).zfill(len(str(x)))[::-1]; uit = []; br_ = 0
    for p, q in zip(X, Y):
        p, q = int(p) - (0 if vergeet_lenen else br_), int(q)
        if p < q: uit.append(p + 10 - q); br_ = 1
        else: uit.append(p - q); br_ = 0
    return int(''.join(map(str, uit[::-1])))
def gen_aftrek(r):
    while True:
        x = r.choice([r.randint(2, 9) * 1000 + r.randint(1, 9), r.randint(2, 9) * 1000 + r.randint(1, 9) * 10 + r.randint(0, 9)]); y = r.randint(1000, x - 500)
        goed = x - y; f1 = int(''.join(str(abs(int(p) - int(q))) for p, q in zip(str(x), str(y).zfill(len(str(x)))))); f2 = _kolom(x, y, vergeet_lenen=True)
        if len({goed, f1, f2}) == 3 and f2 > 0: break
    return dict(zin=lambda nm, v: f'{nm} rekent {x} − {y} = {v}. Klopt dat?', goed=goed, fouten=[(f1, 'per kolom de kleinste van de grootste'), (f2, 'lenen vergeten (over de nul)')])
def gen_deel_van(euro):
    def g(r):
        while True:
            n = r.choice([4, 5, 6, 8]); t = r.randint(2, n - 1)
            if F(t, n).denominator != n: continue
            x = n * t * r.randint(1, 6 if euro else 4)
            if not euro and x > 200: continue
            goed, f1, f2 = x * t // n, x // t, x // n
            if len({goed, f1, f2}) == 3: break
        e = '€' if euro else ''
        return dict(zin=lambda nm, v: f'{nm} zegt dat {t}/{n} van {e}{x} {v} is. Klopt dat?', goed=f'{e}{goed}', fouten=[(f'{e}{f1}', 'gedeeld door de teller in plaats van door de noemer'), (f'{e}{f2}', 'alleen één deel genomen')])
    return g
def gen_ttxtt(r):
    while True:
        x, y = r.randint(13, 49), r.randint(13, 49)
        if x % 10 and y % 10:
            goed = x * y; f1 = (x // 10 * 10) * (y // 10 * 10) + (x % 10) * (y % 10); f2 = x * (y // 10 * 10)
            if len({goed, f1, f2}) == 3: break
    return dict(zin=lambda nm, v: f'{nm} rekent {x} × {y} = {fmt(v)}. Klopt dat?', goed=goed, fouten=[(f1, 'alleen tientallen × tientallen en eenheden × eenheden'), (f2, 'de eenheden van de tweede factor vergeten')])
def gen_onthoud(r):
    while True:
        x, d = r.randint(213, 989), r.randint(3, 9)
        goed = x * d; f1 = int(''.join(str(int(c) * d % 10) for c in str(x))); f2 = (x // 10 * 10) * d
        if len({goed, f1, f2}) == 3 and x % 10: break
    return dict(zin=lambda nm, v: f'{nm} rekent {x} × {d} = {fmt(v)}. Klopt dat?', goed=goed, fouten=[(f1, 'onthouden vergeten'), (f2, 'de eenheden vergeten')])
def gen_verander(r):
    while True:
        x = r.randint(10000, 99999); stap = r.choice([10, 100, 1000]); d = (x // stap) % 10
        if 1 <= d <= 8: break
    y = x + stap if r.random() < .5 else x - stap
    andere = {10: 100, 100: 1000, 1000: 100}[stap]
    return dict(zin=lambda nm, v: f'{fmt(x)} wordt {fmt(y)}. {nm} zegt dat het getal verandert met {fmt(v)}. Klopt dat?', goed=stap,
                fouten=[(andere, 'naar de verkeerde plek gekeken'), ((x // stap) % 10, 'het cijfer genomen in plaats van de waarde')])
def gen_meer(teken):
    def g(r):
        while True:
            x = r.randint(12000, 98000); s = r.choice([10, 100, 1000])
            goed = x + s if teken == '+' else x - s; f1 = x + (s * 10 if s < 1000 else s // 10) * (1 if teken == '+' else -1); f2 = x + (s // 10 if s > 10 else s * 100) * (1 if teken == '+' else -1)
            if len({goed, f1, f2}) == 3: break
        w = 'meer' if teken == '+' else 'minder'
        return dict(zin=lambda nm, v: (f'{nm} telt {fmt(s)} op bij {fmt(x)} en krijgt {fmt(v)}. Klopt dat?' if teken == '+' else f'{nm} haalt {fmt(s)} af van {fmt(x)} en krijgt {fmt(v)}. Klopt dat?'), goed=goed, fouten=[(f1, 'op de verkeerde plek erbij/eraf'), (f2, 'op de verkeerde plek erbij/eraf (andere plek)')])
    return g
FACTOR = {('cm', 'm'): F(1, 100), ('km', 'm'): 1000, ('m', 'mm'): 1000, ('hm', 'm'): 100, ('m', 'hm'): F(1, 100), ('km', 'hm'): 10, ('hm', 'km'): F(1, 10),
          ('L', 'cl'): 100, ('cl', 'L'): F(1, 100), ('L', 'ml'): 1000, ('L', 'dl'): 10, ('dl', 'L'): F(1, 10), ('dl', 'ml'): 100, ('ml', 'dl'): F(1, 100), ('kg', 'g'): 1000}
def gen_omreken(u, v):
    f = F(FACTOR[(u, v)])
    def g(r):
        while True:
            q = r.randint(2, 40) * (f.denominator * 10 if f.denominator > 1 else 1)
            goed, f1, f2 = q * f, q * f * 10, q * f / 10
            if f2.denominator == 1 and len({goed, f1, f2}) == 3: break
        return dict(zin=lambda nm, w: f'{nm} zegt dat {fmt(q)} {u} gelijk is aan {w} {v}. Klopt dat?', goed=fmt(goed), fouten=[(fmt(f1), 'factor van een buurmaat (tien keer te groot)'), (fmt(f2), 'factor van een buurmaat (tien keer te klein)')], eenheid=v)
    return g
def gen_opp(r):
    while True:
        l, b = r.randint(3, 12), r.randint(2, 9)
        goed, f1, f2 = l * b, 2 * (l + b), l + b
        if len({goed, f1, f2}) == 3 and l != b: break
    return dict(zin=lambda nm, v: f'{nm} zegt dat een rechthoek van {l} cm bij {b} cm {v} cm² is. Klopt dat?', goed=goed, fouten=[(f1, 'de omtrek uitgerekend'), (f2, 'lengte en breedte opgeteld')], eenheid='cm²')
def gen_zijde(r):
    while True:
        s, z = r.randint(3, 9), r.randint(4, 15); A = s * z
        goed, f1, f2 = z, A - s, A // 2
        if A % 2 == 0 and len({goed, f1, f2}) == 3: break
    return dict(zin=lambda nm, v: f'De oppervlakte van een rechthoek is {A} cm². Eén zijde is {s} cm. {nm} zegt dat de andere zijde {v} cm is. Klopt dat?', goed=goed, fouten=[(f1, 'de zijde afgetrokken in plaats van gedeeld'), (f2, 'de oppervlakte door 2 gedeeld')], eenheid='cm')
def gen_koekjes(r):
    while True:
        n = r.choice([3, 4, 5, 6]); t = r.randint(2, n - 1); K = n * r.randint(2, 4)
        goed, f1, f2 = K * t // n, t, K // n
        if F(t, n).denominator == n and len({goed, f1, f2}) == 3: break
    return dict(zin=lambda nm, v: f'Er zijn {K} koekjes. {nm} zegt dat {t}/{n} van de koekjes {v} koekjes zijn. Klopt dat?', goed=goed, fouten=[(f1, 'de teller overgenomen'), (f2, 'alleen één deel genomen')], eenheid='koekjes')
def gen_verdeel(r):
    while True:
        n = r.randint(3, 8); a = r.randint(2, n - 1)
        if F(a, n).denominator == n: break
    return dict(zin=lambda nm, v: f'{a} taarten worden eerlijk verdeeld over {n} kinderen. {nm} zegt dat elk kind {v} taart krijgt. Klopt dat?', goed=f'{a}/{n}', fouten=[(f'{n}/{a}', 'teller en noemer omgedraaid'), (f'1/{n}', 'alleen naar het aantal kinderen gekeken')], eenheid='taart')
GEN = {('G6-GET-E01', 1): gen_afronden(1000, (10000, 99999), 100, 'duizendtallen', 100), ('G6-GET-E01', 2): gen_afronden(100, (1000, 9999), 10, 'honderdtallen', 10),
       ('G6-GET-E03', 4): gen_noemer, ('G6-GET-E04', 1): gen_aftrek, ('G6-GET-E09', 1): gen_deel_van(True), ('G6-GET-E09', 2): gen_deel_van(False),
       ('G6-GET-M02', 1): gen_verander, ('G6-GET-M02', 2): gen_meer('+'), ('G6-GET-M02', 3): gen_meer('-'), ('G6-GET-M06', 1): gen_onthoud, ('G6-GET-E06', 1): gen_ttxtt,
       ('G6-MEET-E03', 1): gen_opp, ('G6-MEET-E03', 2): gen_zijde, ('G6-VERH-E02', 2): gen_koekjes, ('G6-VERH-E03', 1): gen_verdeel}
for (d, n, w) in LJ.R13_34:
    if d in ('G6-MEET-E01', 'G6-MEET-E04', 'G6-MEET-E05'): GEN[(d, n)] = None      # Regel M: maten uit de kop
NIET = {('G6-VBN-E02', 1): 'lijngrafiek nodig (bewering over een aflezing)', ('G6-VBN-E02', 2): 'lijngrafiek nodig', ('G6-VBN-E02', 3): 'lijngrafiek nodig (of schatten «meer of minder dan 200?»)',
        ('G6-GET-M03', 1): 'getallenlijn nodig'}
def main():
    r = random.Random(13); kop = {}
    G = json.load(open(f'{R13}/g6/data/gemapt.json'))['items']
    for it in G:
        if it['merge'].get('status') == 'gemapt': kop.setdefault((it['merge']['doel'], it['merge']['somtypeNrOrigineel']), it['merge']['somtype'])
    items, niet, nm_i, pos_i = [], [], 0, 0
    for d, n, w in LJ.R13_34:
        g = GEN.get((d, n))
        if (d, n) in NIET: niet.append({'somtype': f'{d} #{w} (nrO {n})', 'reden': NIET[(d, n)]}); continue
        if g is None:
            m = re.fullmatch(r'# (\w+) = □ (\w+)', kop[(d, n)]); g = gen_omreken(m.group(1), m.group(2))
        for k in range(4):
            x = g(r); e_ = x.get('eenheid'); T = lambda v: (fmt(v) if isinstance(v, (int, F)) else str(v)) + (f' {e_}' if e_ else '')
            goed = x['goed']; fouten = x['fouten']; naam = NAMEN[nm_i % len(NAMEN)]; nm_i += 1
            klopt = k == 3; bewering = goed if klopt else fouten[k % 2][0]
            andere = fouten[1 - k % 2][0] if not klopt else None
            if klopt: fout_opties = [(f'Nee, het is {T(fouten[0][0])}.', fouten[0][1]), (f'Nee, het is {T(fouten[1][0])}.', fouten[1][1])]; goed_optie = 'Ja, dat klopt.'
            else: fout_opties = [('Ja, dat klopt.', f'de bewering geloofd ({fouten[k % 2][1]})'), (f'Nee, het is {T(andere)}.', fouten[1 - k % 2][1])]; goed_optie = f'Nee, het is {T(goed)}.'
            p = pos_i % 3; pos_i += 1; ops = [o for o, _ in fout_opties]; ops.insert(p, goed_optie)
            opg = x['zin'](naam, bewering)
            assert ':' not in opg and not any(':' in o for o in ops), opg
            assert len(set(ops)) == 3, ops
            items.append({'id': f'{d}-r13-kritisch-{w:02d}-{k + 1}', 'status': 'concept (niet in data; wacht op Didactiek en Oefeningen)', 'doelId': d, 'somtypeNrOrigineel': n, 'weergaveNr': w,
                          'kop': kop.get((d, n)), 'niveau': 'kritisch', 'niveauKind': 'Uitdaging', 'type': 'meerkeuze', 'opgave': opg,
                          'opties': [{'letter': 'ABC'[i], 'tekst': o} for i, o in enumerate(ops)], 'antwoord': goed_optie,
                          'antwoordDetail': {'juisteOptie': 'ABC'[p], 'juisteOptieTekst': goed_optie}, 'husselen': False,
                          'beweringKlopt': klopt, 'denkfoutPerOptie': {o: dk for o, dk in fout_opties}})
    uit = {'uitleg': __doc__, 'aantal': len(items), 'somtypes': len({(i['doelId'], i['somtypeNrOrigineel']) for i in items}), 'nietGegenereerd': niet, 'items': items}
    json.dump(uit, open(f'{R13}/kritisch_concept_g6.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    L = ['# r13 L-R10b: kritisch-items G6 (CONCEPT, niet in data)', '', f'{len(items)} items in {uit["somtypes"]} somtypes (4 per somtype: 3 beweringen fout, 1 klopt; goed antwoord wisselt A/B/C). Bron: `r13/kritisch_concept.py` (seed 13).',
         'Niet gegenereerd: ' + '; '.join(f"{x['somtype']} ({x['reden']})" for x in niet) + '.', '', 'Nodig vóór de build: Didactiek (vorm/taal, ook de app-weergave ja/nee + getal, onduidelijk 6), Oefeningen (H1/H2 en een regel per foute optie).', '']
    for i in items: L.append(f"- `{i['id']}` {i['opgave']} → **{i['antwoord']}** · opties: " + ' / '.join(o['tekst'] for o in i['opties']))
    open(f'{R13}/kritisch_concept_g6.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(len(items), 'items,', uit['somtypes'], 'somtypes; niet:', len(niet))
if __name__ == '__main__': main()
