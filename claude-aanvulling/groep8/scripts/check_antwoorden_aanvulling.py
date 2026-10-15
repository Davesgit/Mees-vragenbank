#!/usr/bin/env python3
"""Onafhankelijke antwoordcheck van alle G8-aanvullingen in G4–G7 (data/aanvulling_uit_g8.json, ook de 46 terug-G7) — Dave 22:34.
Rekent per item het antwoord opnieuw uit (eigen parser per sjabloon, niet de build-controle) en per fout-sleutel:
  - sleutel ≠ antwoord, geen dubbele sleutels, bij meerkeuze: antwoord precies één keer in de opties en elke sleutel is een optie;
  - de bewering in de tekst klopt voor deze waarde (precies uitgerekend, verkeerde plek/kant afgerond, eindcijfer, 'Rond … af. a + b is c',
    'niet groter/kleiner dan', vak/letter/cijfer op de plattegrond, aantal torens/grondvlak/volle balk/net ernaast, enz.);
  - elke som 'a op b is/= c' in opgave en fout-hint is goed gerekend.
Een sleutel zonder herkenbare route (geen bewering die te toetsen is) telt als 'route onbekend' (LET OP, geen FOUT).
Alleen lezen; schrijft g8/antwoordcheck_aanvullingen.md. Draai vanuit claude-merge/g8."""
import json, re, collections, os
from fractions import Fraction as Fr
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(BASE)
OP = {'+': lambda a, b: a + b, '−': lambda a, b: a - b, '-': lambda a, b: a - b, '×': lambda a, b: a * b, ':': lambda a, b: Fr(a, b)}
def num(s):
    s = str(s).strip().replace('€', '').replace(' ', '')
    s = re.sub(r'\s*(bezoekers|wielen|ballen|bordjes|m²|meter|stuks?)$', '', s)
    if re.fullmatch(r'\d{1,3}(\.\d{3})+', s): s = s.replace('.', '')
    s = s.replace(',', '.')
    try: return Fr(s)
    except (ValueError, ZeroDivisionError): return None
def rnd(x, u): return (x + u // 2) // u * u
def ints(t): return [int(x.replace('.', '')) for x in re.findall(r'(?<![\d,])\d{1,3}(?:\.\d{3})+(?![\d,])|(?<![\d,])\d+(?![\d])', t)]
UNIT = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000}

def sommen_ok(t):
    """elke 'a op b is c' / 'a op b = c' in de tekst klopt (hele getallen, ook met €)."""
    fout = []
    for m in re.finditer(r'(€?\d[\d.,]*) ([+−×:]) (€?\d[\d.,]*) (?:is|=) (€?\d[\d.,]*)', t):
        a, b, c = num(m.group(1)), num(m.group(3)), num(m.group(4))
        if None in (a, b, c) or (m.group(2) == ':' and b == 0): continue
        if OP[m.group(2)](a, b) != c: fout.append(m.group(0))
    return fout

def antwoord(it):
    o = it['opgave']; jr = it['visual'].get('jsRender') or {}
    if m := re.match(r'Hoeveel is (\d+) ([+−×]) (\d+) ongeveer\? Rond beide getallen af op (\w+) en reken dan uit\.$', o):
        u = UNIT[m.group(4)]; a, b = int(m.group(1)), int(m.group(3)); return OP[m.group(2)](rnd(a, u), rnd(b, u)), 'schatten met afspraak', dict(a=a, b=b, op=m.group(2), u=u)
    if m := re.match(r'(\d+) dozen met elk (\d+) [a-z]+\. Schat hoeveel dat ongeveer is: rond \2 af op (\w+) en reken dan uit\.$', o):
        n, x, u = int(m.group(1)), int(m.group(2)), UNIT[m.group(3)]; return n * rnd(x, u), 'schatten (één getal afronden)', dict(a=x, b=n, op='×', u=u, een=True)
    if m := re.match(r'Kijk zonder uit te rekenen\. Welk antwoord bij (\d+) ([+−×]) (\d+) kan kloppen\?$', o):
        a, b = int(m.group(1)), int(m.group(3)); return OP[m.group(2)](a, b), 'kan kloppen (MC)', dict(a=a, b=b, op=m.group(2))
    if m := re.search(r'maandag (\d+), dinsdag (\d+), woensdag (\d+) en donderdag (\d+)\. Hoeveel .* samen\?$', o):
        return sum(int(x) for x in m.groups()), 'tabel optellen', {}
    if (m := re.match(r'In welk vak staat (?:de|het) ([a-z]+)\?$', o)) and jr.get('soort') == 'plattegrond':
        v = [d['vak'] for d in jr['dingen'] if d['wat'] == m.group(1)]; return (v[0] if len(v) == 1 else None), 'plattegrond-vak', dict(ding=m.group(1), jr=jr)
    if (m := re.match(r'Wat staat er in vak ([A-L]\d+)\?$', o)) and jr.get('soort') == 'plattegrond':
        v = [d['wat'] for d in jr['dingen'] if d['vak'] == m.group(1)]; return (v[0] if len(v) == 1 else None), 'plattegrond-ding', dict(vak=m.group(1), jr=jr)
    if jr.get('soort') == 'bouwvorm':
        st = jr['stapels']; return sum(map(sum, st)), 'bouwwerk tellen', dict(st=st)
    if m := re.search(r'(\d+) [\wà-ÿ\' ]+? (?:kosten|kost) samen €(\d+(?:,\d\d?)?)\. Hoeveel kost één', o):
        return Fr(num(m.group(2))) / int(m.group(1)), 'samen → één (geld)', {}
    if m := re.search(r'koopt (\d+) .+? van €(\d+(?:,\d\d)?) per stuk en betaalt met €(\d+(?:,\d\d)?)\.', o):
        return num(m.group(3)) - int(m.group(1)) * num(m.group(2)), 'wisselgeld', {}
    if m := re.search(r'L-vormig .* rechthoek van (\d+) bij (\d+) meter en een rechthoek van (\d+) bij (\d+) meter', o):
        a, b, c, d = map(int, m.groups()); return a * b + c * d, 'L-vorm', dict(r=(a, b, c, d))
    if m := re.search(r'tuin van (\d+) bij (\d+) meter heeft een vierkante vijver van (\d+) bij (\d+) meter', o):
        a, b, c, d = map(int, m.groups()); return a * b - c * d, 'tuin min vijver', dict(r=(a, b, c, d))
    if m := re.search(r'(\d+) fietsen met (\d+) wielen en (\d+) fietsen met (\d+) wielen', o):
        a, b, c, d = map(int, m.groups()); return a * b + c * d, 'twee soorten', {}
    if m := re.search(r'wandeltocht van (\d+) km staan om de (\d+) meter bordjes, ook bij de start en de finish', o):
        km, s = map(int, m.groups()); return Fr(km * 1000, s) + 1, 'paaltjes (beide uiteinden)', dict(km=km, s=s)
    if m := re.search(r'(\d+) (?:dozen|kinderen) (?:met elk|hebben elk|nemen elk) (\d+) .*?(?:haalt er|plakken er samen|raken er samen|deelt er) (\d+)', o):
        a, b, c = map(int, m.groups()); return a * b - c, 'keer en eraf', {}
    if m := re.search(r'heeft (\d+) dozen met elk (\d+) [a-z]+\. Ze deelt er (\d+) uit', o):
        a, b, c = map(int, m.groups()); return a * b - c, 'keer en eraf', {}
    if m := re.search(r'(\d+) dozen met elk (\d+) [a-z]+\. Er worden er (\d+) (?:gebruikt|uitgedeeld|verkocht)', o):
        a, b, c = map(int, m.groups()); return a * b - c, 'keer en eraf', {}
    if m := re.search(r'(\d+) [a-z]+ worden eerlijk verdeeld over (\d+)', o): return Fr(int(m.group(1)), int(m.group(2))), 'eerlijk verdelen', {}
    if m := re.search(r'(\d+) (?:dozen|kratten|bladzijden|rijen|kinderen) (?:met elk|hebben elk) (\d+)|In (\d+) dozen zitten elk (\d+)', o):
        g = [int(x) for x in m.groups() if x]; return g[0] * g[1], 'keer (elk)', {}
    n = ints(o)
    if len(n) == 2 and re.search(r'Er (?:komen|komt) er \d+ bij|krijgt er \d+ bij', o): return n[0] + n[1], 'erbij', {}
    if len(n) == 2 and re.search(r'(?:gaan|gaat) er \d+ (?:weg|naar)|worden er \d+ verkocht|zijn er \d+ verkocht|geeft er \d+ weg', o): return n[0] - n[1], 'eraf', {}
    return None, 'geen sjabloon', {}

def fmt(v):
    if isinstance(v, str): return v
    v = Fr(v)
    return str(v.numerator) if v.denominator == 1 else None
def gelijk(s, v):
    if isinstance(v, str): return str(s).strip() == v
    x = num(s); return x is not None and x == Fr(v)

def sleutel(it, f, v, soort, ctx):
    """-> ('ok'|'FOUT'|'route?', uitleg)"""
    t = f['uitleg'] or ''; x = num(f['fout']); o = it['opgave']
    if gelijk(f['fout'], v): return 'FOUT', 'sleutel = het goede antwoord'
    if (s_ := sommen_ok(t)): return 'FOUT', f'som in de tekst klopt niet: {s_}'
    if soort.startswith('schatten'):
        a, b, op, u = ctx['a'], ctx['b'], ctx['op'], ctx['u']
        if t.startswith(('Dat is het precieze antwoord', 'Precies uitgerekend')): return ('ok', 'precies') if x == OP[op](a, b) else ('FOUT', f'is niet het precieze antwoord {OP[op](a, b)}')
        if t.startswith('Kijk goed op welke plek'):
            alt = {OP[op](rnd(a, w), rnd(b, w)) for w in (10, 100, 1000) if w != u}
            alt |= {OP[op](rnd(a, w1), rnd(b, w2)) for w1 in (u, u * 10) for w2 in (u, u * 10)} - {OP[op](rnd(a, u), rnd(b, u))}  # één van beide op de plek ernaast
            if x not in alt and x in {OP[op](rnd(a, u), b), OP[op](a, rnd(b, u))}: return 'LET', f'sleutel = één getal niet afgerond ({x}); de tekst gaat over de plek van afronden (afronden op de andere plek geeft hier het goede antwoord)'
            return ('ok', 'andere plek') if x in alt else ('FOUT', f'geen afronding op een andere plek ({sorted(alt)})')
        if t.startswith('Kijk naar het cijfer achter de plek'):
            ra = {(a // u) * u, (a // u + 1) * u}; rb = {(b // u) * u, (b // u + 1) * u}
            alt = {OP[op](p, q) for p in ra for q in rb} - {OP[op](rnd(a, u), rnd(b, u))}
            return ('ok', 'verkeerde kant afgerond') if x in alt else ('FOUT', f'geen afronding naar de verkeerde kant ({sorted(alt)})')
        if '× 4: tel de nullen' in t or 'tel de nullen goed' in t: return ('ok', 'nul vergeten') if x * 10 == v or x == v * 10 else ('FOUT', 'geen nul verschil')
        if 'dat is een keersom' in t: return ('ok', 'opgeteld i.p.v. keer') if x == rnd(a, u) + b else ('route?', '')
        if t.startswith('Schatten is rekenen met ronde getallen'): return ('ok' if x != v else 'FOUT', 'algemeen')
        return 'route?', ''
    if soort == 'kan kloppen (MC)':
        a, b, op = ctx['a'], ctx['b'], ctx['op']
        if m := re.search(r'De uitkomst van (\d+) ([+−×]) (\d+) eindigt op (\d)\. Eindigt (\d+) daarop\?', t):
            ok = OP[m.group(2)](int(m.group(1)), int(m.group(3))) % 10 == int(m.group(4)) and int(m.group(5)) % 10 != int(m.group(4)) and m.group(5) == f['fout'] and (int(m.group(1)), int(m.group(3))) == (a, b)
            return ('ok', 'eindcijfer') if ok else ('FOUT', 'bewering over het eindcijfer klopt niet')
        if m := re.search(r'Rond eerst af\. (\d+) ([+−×]) (\d+) is (\d+)\. Ligt (\d+) daar dichtbij\?', t):
            p, q, r = int(m.group(1)), int(m.group(3)), int(m.group(4))
            ok = p in {rnd(a, 10), rnd(a, 100)} and q in {rnd(b, 10), rnd(b, 100), b} and OP[m.group(2)](p, q) == r and abs(x - r) > abs(Fr(v) - r) and abs(x - r) >= Fr(r) / 5
            return ('ok', 'ver van de schatting') if ok else ('FOUT', f'schatting {p} {m.group(2)} {q} = {r} of afstand klopt niet')
        if m := re.search(r'Rond (allebei|\d+) naar (boven|beneden) af(?: en (\d+) naar (boven|beneden))?\. (\d+) ([+−×]) (\d+) is (\d+)\. De uitkomst kan dus niet (groter|kleiner) zijn dan (\d+), en (\d+) is (groter|kleiner)\.', t):
            r = int(m.group(8)); ok = OP[m.group(6)](int(m.group(5)), int(m.group(7))) == r and int(m.group(10)) == r and int(m.group(11)) == x
            ok = ok and ((m.group(9) == 'groter' and x > r >= v) or (m.group(9) == 'kleiner' and x < r <= v))
            return ('ok', 'grens van de schatting') if ok else ('FOUT', 'grens-bewering klopt niet')
        if 'dat is te veel' in t: return ('ok', 'product te groot') if x > v else ('FOUT', '')
        if t in ('Erbij is optellen.', 'Weg is aftrekken.', 'Eerlijk verdelen is delen.', 'Elk evenveel en samen: dat is keer.'):
            alt = {OP[k](a, b) for k in '+−×'} | ({Fr(a, b)} if b else set())
            return ('ok', 'andere bewerking') if x in alt and x != v else ('FOUT', 'geen andere bewerking')
        if t.startswith(('Tel de tientallen', 'Kijk of je moest lenen')): return ('ok', 'tiental ernaast') if abs(x - v) in (10, 100) else ('FOUT', f'verschil {x - v}')
        if m := re.search(r'Je vergat (\d+) × (\d+)', t): return ('ok', 'deelproduct vergeten') if v - x == int(m.group(1)) * int(m.group(2)) else ('FOUT', 'deelproduct klopt niet')
        return 'route?', ''
    if soort == 'tabel optellen':
        if 'hoort bij één dag' in t: return ('ok', 'één dag') if str(int(x)) in o else ('FOUT', '')
        if t.startswith('Tel de getallen nog een keer'): return ('ok', 'tiental ernaast') if abs(x - v) == 10 else ('FOUT', '')
        return 'route?', ''
    if soort == 'plattegrond-vak':
        jr = ctx['jr']; d = {g['wat']: g['vak'] for g in jr['dingen']}; k = f['fout']; a_ = v
        if m := re.search(r'In vak ([A-L]\d+) staat (?:de|het) ([a-z]+)\. Zoek eerst (?:de|het) ([a-z]+)', t):
            return ('ok', 'ander ding') if m.group(1) == k and d.get(m.group(2)) == k and m.group(3) == ctx['ding'] else ('FOUT', 'vak/ding klopt niet')
        if t.startswith('De letter klopt'): return ('ok', 'letter goed') if k[0] == a_[0] and k[1:] != a_[1:] else ('FOUT', 'letter niet gelijk')
        if t.startswith('Het cijfer klopt'): return ('ok', 'cijfer goed') if k[1:] == a_[1:] and k[0] != a_[0] else ('FOUT', 'cijfer niet gelijk')
        if m := re.search(r'staat in de goede (kolom|rij), maar in een andere (rij|kolom)\. Kijk bij vak ([A-L]\d+)', t):
            ok = m.group(3) == k and ((m.group(1) == 'kolom' and k[0] == a_[0] and k[1:] != a_[1:]) or (m.group(1) == 'rij' and k[1:] == a_[1:] and k[0] != a_[0]))
            return ('ok', f'goede {m.group(1)}') if ok else ('FOUT', 'kolom/rij-bewering klopt niet')
        if m := re.search(r'staat in vak ([A-L]\d+)\. Zoek bij vak ([A-L]\d+)', t):
            return ('ok', 'letter en cijfer omgedraaid/ander vak') if m.group(1) == a_ and m.group(2) == k else ('FOUT', 'vakken in de tekst kloppen niet')
        return 'route?', ''
    if soort == 'plattegrond-ding':
        d = {g['wat']: g['vak'] for g in ctx['jr']['dingen']}; V = ctx['vak']; k = f['fout']; w = d.get(k)
        if w is None: return 'FOUT', f'{k} staat niet op de plattegrond'
        if m := re.search(r'^(?:De|Het) ([a-z]+) staat in de goede (rij|kolom), maar in een andere (kolom|rij)\. Kijk bij vak ([A-L]\d+)', t):
            ok = m.group(1) == k and m.group(4) == V and ((m.group(2) == 'kolom' and w[0] == V[0] and w[1:] != V[1:]) or (m.group(2) == 'rij' and w[1:] == V[1:] and w[0] != V[0]))
            return ('ok', f'goede {m.group(2)}') if ok else ('FOUT', f'{k} staat in {w}: kolom/rij-bewering klopt niet')
        if m := re.search(r'^(?:De|Het) ([a-z]+) staat in vak ([A-L]\d+)\. Zoek bij vak ([A-L]\d+)', t):
            return ('ok', 'ander ding') if m.group(1) == k and m.group(2) == w and m.group(3) == V and w != V else ('FOUT', 'vakken in de tekst kloppen niet')
        return 'route?', ''
    if soort == 'bouwwerk tellen':
        st = ctx['st']; torens = sum(1 for r in st for h in r if h); grond = len(st) * len(st[0]); hmax = max(h for r in st for h in r)
        if t.startswith('Je telde het aantal torens'): return ('ok', 'aantal torens') if x == torens else ('FOUT', f'aantal torens is {torens}')
        if t.startswith('Je telde de vakjes van het grondvlak'): return ('ok', 'grondvlak') if x == grond else ('FOUT', f'grondvlak is {grond}')
        if t.startswith('Het bouwwerk is geen volle balk'): return ('ok', 'volle balk') if x == grond * hmax else ('FOUT', f'volle balk is {grond * hmax}')
        if t.startswith('Je zit er net naast'): return ('ok', 'net ernaast') if abs(x - v) == 1 else (('LET', f"'net naast' bij verschil {x - v}") if abs(x - v) == 2 else ('FOUT', f'verschil {x - v}'))
        if t.startswith('Niet alle torens zijn even hoog'): return ('ok', 'torens × hoogste') if x == torens * hmax else ('route?', '')
        if t.startswith('Tel toren voor toren'): return ('ok' if x > 0 else 'FOUT', 'algemeen (te weinig/te veel geteld)')
        return 'route?', ''
    # T-items en terug-G7: herken de route uit de getallen in de opgave
    n = ints(o); money = '€' in o
    if soort == 'L-vorm' or soort == 'tuin min vijver':
        a, b, c, d = ctx['r']
        routes = {a * b: 'één rechthoek', (a + c) * (b + d): 'grote rechthoek', a + b + c + d: 'alles opgeteld', a * b + c * d: 'goed', a * b - c: 'vijver als zijde', a * b + c * d * (1 if soort == 'L-vorm' else 1): ''}
        if soort == 'tuin min vijver': routes.update({a * b: 'vijver niet eraf', a * b - c: 'vijver als zijde (niet c × d)', a * b + c * d: 'vijver erbij'})
        r = routes.get(int(x)) if x is not None and x.denominator == 1 else None
        return ('ok', r) if r and r != 'goed' else ('route?', '')
    cand = {}
    for i_, p in enumerate(n):
        cand.setdefault(Fr(p), 'getal uit de vraag')
        for q in n[i_ + 1:]:
            cand.setdefault(Fr(p + q), 'opgeteld'); cand.setdefault(Fr(abs(p - q)), 'afgehaald'); cand.setdefault(Fr(p * q), 'keer')
            if q: cand.setdefault(Fr(p, q), 'gedeeld'); cand.setdefault(Fr(p * 10, q), 'komma verschoven')
    if len(n) >= 3: cand.setdefault(Fr(n[0] * n[1]), 'tussenstap'); cand.setdefault(Fr(n[0] * n[1] + n[2]), 'erbij i.p.v. eraf')
    if money and (m := re.search(r'€(\d+(?:,\d\d)?)', o)):
        T = num(m.group(1))
        if n: cand.setdefault(T / n[0] * 10, 'komma verschoven'); cand.setdefault(T - n[0] if False else T - Fr(n[0]), 'afgehaald')
        cand.setdefault(Fr(v) * 10, 'komma verschoven'); cand.setdefault(Fr(v) / 10, 'komma verschoven')
    if soort == 'paaltjes (beide uiteinden)': cand.setdefault(Fr(v) - 1, 'start vergeten'); cand.setdefault(Fr(ctx['km'] * 1000 // ctx['s']) if False else Fr(v) - 1, 'start vergeten')
    if soort == 'wisselgeld' and (m := re.search(r'koopt (\d+) .+? van €(\d+(?:,\d\d)?) per stuk en betaalt met €(\d+(?:,\d\d)?)', o)):
        k, p, b = int(m.group(1)), num(m.group(2)), num(m.group(3))
        cand.update({k * p: 'alleen de prijs samen', b - p: 'één stuk', b - (k - 1) * p: 'één stuk te weinig', b - (k + 1) * p: 'één stuk te veel', k * p - b: 'omgedraaid'})
    if t.startswith(('Tel de tientallen', 'Kijk of je moest lenen')): return ('ok', 'tiental ernaast') if abs(x - v) in (10, 100) else ('FOUT', f'verschil {x - v}')
    if m := re.search(r'^(\d+) × (\d+) = (\d+), dat is te veel', t):
        ok = int(m.group(2)) == x and int(m.group(3)) > max(n); return ('ok', 'product groter dan het totaal') if ok else ('FOUT', 'te-veel-bewering klopt niet')
    if m := re.search(r'^Je vergat (\d+) × (\d+)\.', t): return ('ok', 'deelproduct vergeten') if v - x == int(m.group(1)) * int(m.group(2)) else ('FOUT', 'deelproduct klopt niet')
    if t.startswith('Elk evenveel') and len(n) >= 3: return ('ok', 'opgeteld i.p.v. keer') if x == n[0] + n[1] - n[2] else ('FOUT', '')
    if (m := re.search(r'^(\d+) keer €(\d+): vermenigvuldigen', t)) and soort == 'wisselgeld':
        b = num(re.search(r'betaalt met €(\d+(?:,\d\d)?)', o).group(1)); return ('ok', 'opgeteld i.p.v. keer') if x == b - int(m.group(1)) - int(m.group(2)) else ('FOUT', '')
    if soort == 'twee soorten' and t.startswith('Reken beide soorten'): return ('ok', 'alle fietsen met evenveel wielen') if x == (n[0] + n[2]) * n[1] else ('route?', '')
    if soort == 'paaltjes (beide uiteinden)' and 'om naar meters' in t: return 'LET', f'route van {f["fout"]} niet te herleiden (12 : 500 en 12 000 : 500 geven geen 6)'
    if x in cand: return 'ok', cand[x]
    return 'route?', ''

ZE = {'Fenna', 'Lotte', 'Mila', 'Noor', 'Emma', 'Sara', 'Lisa', 'Julia', 'Zoë', 'Anna', 'Fleur', 'Yara'}
HIJ = {'Ayoub', 'Daan', 'Milan', 'Sem', 'Luuk', 'Bram', 'Tim', 'Noah', 'Finn', 'Daniel'}
def tekstcontext(o, t):
    """tekst van de fout-hint past niet bij de context van de opgave (woord, aantal, hij/ze)."""
    w = []
    if m := re.search(r'Het zijn (\d+) ([a-zë]+):', t):
        if m.group(2) not in o: w.append(f"'{m.group(2)}' staat niet in de opgave")
        if (mm := re.search(r'koopt (\d+) ', o)) and mm.group(1) != m.group(1): w.append(f'aantal {m.group(1)} ≠ {mm.group(1)} in de opgave')
    naam = (re.match(r'([A-Z][a-zë]+) ', o) or [None, None])[1]
    if re.search(r'\bhij\b', t) and naam in ZE: w.append(f"'hij' bij {naam}")
    if re.search(r'\bze\b', t) and naam in HIJ: w.append(f"'ze' bij {naam}")
    if 'hele zak' in t and 'zak' not in o: w.append("'de hele zak' staat niet in de opgave")
    if mv := re.search(r'is (\d+) × \1 m², niet \1 m²', t): q = int(mv.group(1)); w.append(f"'{q} × {q} m²' zonder uitkomst; duidelijker: '{q} × {q} = {q * q} m²'")
    if re.search(r'fietsen met 3 wielen', o): w.append('fietsen met 3 wielen (driewielers?) is een vreemde context')
    return w

def main():
    rows = []; per = collections.defaultdict(collections.Counter); fouten = []; onbekend = []; geen = []; let = []; tekst = []
    for g in (4, 5, 6, 7):
        for it in json.load(open(f'{ROOT}/g{g}/data/aanvulling_uit_g8.json'))['items']:
            d = it['merge'].get('voorstelDoel') or it['merge'].get('doel'); v, soort, ctx = antwoord(it); a = it['antwoord']; P = per[(f'G{g}', d)]; P['items'] += 1
            if v is None: geen.append((it['id'], it['opgave'], a)); P['geen sjabloon'] += 1; continue
            if not gelijk(a, v) and not (isinstance(v, Fr) and v.denominator != 1 and gelijk(a, v)):
                fouten.append((it['id'], 'ANTWOORD', f"{it['opgave']} → {a}, nagerekend {fmt(v) or float(v)}")); P['antwoord FOUT'] += 1
            else: P['antwoord ok'] += 1
            jr = it['visual'].get('jsRender') or {}
            if jr.get('soort') == 'plattegrond':
                vv = [g_['vak'] for g_ in jr['dingen']]; ww = [g_['wat'] for g_ in jr['dingen']]
                if len(set(vv)) != len(vv) or len(set(ww)) != len(ww): fouten.append((it['id'], 'PLATTEGROND', 'dubbel vak of ding'))
                for q in vv:
                    if not (ord(q[0]) - 64 <= jr['kolommen'] and 1 <= int(q[1:]) <= jr['rijen']): fouten.append((it['id'], 'PLATTEGROND', f'{q} buiten {jr["kolommen"]}×{jr["rijen"]}'))
            for s_ in sommen_ok(it['opgave']): fouten.append((it['id'], 'OPGAVE', s_))
            ks = [f['fout'] for f in it['foutHints']]
            if len(ks) != len(set(ks)): fouten.append((it['id'], 'DUBBEL', str(ks)))
            if it['type'] == 'meerkeuze':
                op = [o_['tekst'] for o_ in it['opties'] or []]
                if sum(gelijk(o_, v) for o_ in op) != 1: fouten.append((it['id'], 'OPTIES', f'goed antwoord {sum(gelijk(o_, v) for o_ in op)}× in {op}'))
                if len(op) != len(set(op)): fouten.append((it['id'], 'OPTIES', f'dubbele optie {op}'))
                for k in ks:
                    if k not in op: fouten.append((it['id'], 'SLEUTEL', f'{k} is geen optie'))
            for f in it['foutHints']:
                for w_ in tekstcontext(it['opgave'], f['uitleg'] or ''): tekst.append((it['id'], f['fout'], w_, f['uitleg'][:80]))
                r, w = sleutel(it, f, v, soort, ctx); P[f'sleutel {r}'] += 1
                if r == 'FOUT': fouten.append((it['id'], 'SLEUTEL', f"{f['fout']}: {w} («{f['uitleg'][:90]}»)"))
                if r == 'LET': let.append((it['id'], f['fout'], w, f['uitleg'][:80]))
                if r == 'route?': onbekend.append((it['id'], f['fout'], f['uitleg'][:100], it['opgave'][:90]))
            rows.append(it)
    out = ['# Antwoordcheck G8-aanvullingen (G4–G7)', '',
           f"Gedraaid: `g8/scripts/check_antwoorden_aanvulling.py` (alleen lezen) op `g4–g7/data/aanvulling_uit_g8.json`. Elk antwoord is opnieuw uitgerekend met een eigen parser per sjabloon, dus niet met de build-controle. Elke fout-sleutel is nagerekend tegen de bewering in de fout-hint.", '',
           f"**Totaal:** {sum(p['items'] for p in per.values())} items · antwoord FOUT {sum(p['antwoord FOUT'] for p in per.values())} · zonder sjabloon {len(geen)} · sleutels {sum(p['sleutel ok'] + p['sleutel FOUT'] + p['sleutel LET'] + p['sleutel route?'] for p in per.values())} (ok {sum(p['sleutel ok'] for p in per.values())} · FOUT {sum(p['sleutel FOUT'] for p in per.values())} · LET OP {len(let)} · route onbekend {len(onbekend)}) · tekst past niet bij context {len(tekst)} · FOUT-regels totaal {len(fouten)}", '',
           '| groep | doel | items | antwoord ok | antwoord FOUT | sleutels ok | sleutels FOUT | LET OP | route onbekend |', '|---|---|---|---|---|---|---|---|---|']
    for (g, d), p in sorted(per.items()):
        out.append(f"| {g} | {d} | {p['items']} | {p['antwoord ok']} | {p['antwoord FOUT']} | {p['sleutel ok']} | {p['sleutel FOUT']} | {p['sleutel LET']} | {p['sleutel route?']} |")
    out += ['', '## FOUT', ''] + ([f'- {i} [{k}] {w}' for i, k, w in fouten] or ['Geen.'])
    out += ['', '## LET OP (sleutel klopt, maar de tekst past niet precies)', ''] + ([f'- {i} sleutel {k}: {w} («{u}»)' for i, k, w, u in let] or ['Geen.'])
    out += ['', '## Tekst past niet bij de context (geen rekenfout)', '', f'{len(tekst)} fout-hints, {len({i for i, *_ in tekst})} items.', ''] + [f'- {i} sleutel {k}: {w} («{u}»)' for i, k, w, u in tekst]
    out += ['', '## Zonder sjabloon (antwoord niet automatisch nagerekend)', ''] + ([f'- {i}: {o} → {a}' for i, o, a in geen] or ['Geen.'])
    out += ['', '## Route onbekend (sleutel ≠ antwoord, maar de denkfout is niet automatisch te toetsen)', ''] + ([f'- {i} sleutel {k}: «{u}» ({o})' for i, k, u, o in onbekend] or ['Geen.'])
    open(f'{BASE}/antwoordcheck_aanvullingen.md', 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))
main()
