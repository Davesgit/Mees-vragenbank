#!/usr/bin/env python3
"""Past de fout-hintregels van Oefeningen (hints/batch*.json: soort → regel → tekst) per item toe.
Regels gelden van boven naar beneden; de eerste die past, wint. Gebruikt door apply_hints.py.
Per item komt er uit:
  foutHints   concrete sleutels (fout getal / optietekst / vak) met kindtekst, zoals het exportformaat ze kent
  foutRegels  de geordende regels met een matcher (waarden / kleinerDan / vanaf / totEnMet / alles) voor invoer
              die niet als sleutel voorkomt; 'alles' = algemene zin
Basis is extraVelden.claudeFoutHints (door build_g3.py gezet), dus opnieuw draaien geeft hetzelfde resultaat.
Regeltypes erbij (1 okt, fixlijst G4 / besluit Dave), te gebruiken in hints/batch*.json als 'regel':
  fout = antwoord ± getal1   (ook: + getal1, - getal1, ± getal2 …)  bv. één groepje te veel of te weinig
  fout = eenheden als antwoord  (= de eenheden van het antwoord; ook 'fout = de eenheden van het antwoord')
  fout = eenheden van getal1 / getal2,  fout = getal1 × getal2  (Didactiek review batch 1 punt 6)
Nieuw 1 okt 16:00 (merge-fixlijst #48): een 'claude-taalfix' met een onleesbare regel en een vaste tekst (zonder '…') zet die tekst op de
  Claude-sleutels (claudeDenkfout); teksten met [getal1], [getal2], [antwoord] (of {getal1} …) worden per item ingevuld (vul_in).
Nieuw 1 okt 15:51 (merge-fixlijst #38, #40–#42):
  fout = klok een uur te laat / fout = klok een uur te vroeg   zelfde minuten, uur + 1 / − 1 (ook half, kwart; klokkenrij via jsRender.klokken)
  fout = grote wijzer verkeerd                                 het uur klopt, de minuten niet
  fout = antwoord gedeeld door getal1                          staafdiagram: streepjes geteld ('Elk streepje is 2.')
  fout = een dag ernaast                                       kalender: datum ± 1 dag
  fout = het andere tiental/honderdtal naast getal1           afronden: het andere buurtiental/-honderdtal (G5 #12; 166 → 160 als 170 goed is;
                                                               ook 'fout = het andere buurtiental' / 'het andere buurhonderdtal')
  fout = gestopt op de laatste dag van de maand               kalender: de laatste dag van de vroegste maand (#49, 1 okt 16:31)
  fout = gestopt op de eerste dag van de maand                kalender: de 1e van de latere maand (#49)
  fout = gestopt bij de laatste of eerste dag van de maand     (oud, blijft werken) beide datums
  fout = andere cel · fout = som van de rij · fout = som van de kolom · fout = som van twee cellen · fout = verschil van twee cellen
                                                               tabel (jsRender.rijen)
Nieuw 1 okt 17:00 (G5 merge-punten #29, #32, #33; Didactiek batch 2):
  fout = antwoord × 10 / fout = antwoord : 10          hele getallen: exact (nul te veel / nul vergeten); ': 10' alleen als het antwoord op 0
                                                      eindigt. Vanaf 10.000 beide vormen als sleutel (met en zonder punt, huisregel).
                                                      Bij een geldantwoord: het bedrag × 10 / : 10 (komma verschoven).
  fout = antwoord + 1 cent / - 1 cent / ± 1 cent       geld (#32, #19): bedrag in centen; ook 10 cent, €1 ('fout = antwoord ± €1').
  fout = antwoord + 10 cent / - 10 cent / ± 10 cent
  #35 (17:05): een regel met [getal1]/[getal2]/[antwoord] in de tekst voegt zijn sleutels toe, en op 'andere fout' wordt de ingevulde tekst de
  algemeneFoutHint (eerder None).
  Geldinvoer (#33): een geldsleutel raakt ook dezelfde invoer met of zonder €, met spaties, met of zonder ',00' en '8,8' voor '8,80'
  (geld_norm / _cent). '8.80' (punt) is GEEN geldbedrag: daar hoort een eigen tekst bij ('Bij geld schrijf je een komma.', zie
  GELD_PUNT = True, #33) / README). De app normaliseert de invoer op dezelfde manier vóór het opzoeken van de sleutel."""
import re, difflib

BEREIK_AFRONDEN = None     # G5: 1000 (merge-fixlijst #1/#13), gezet in scripts/apply_hints.py
GELD_PUNT = False          # G5: True (merge-punt #33), gezet in scripts/apply_hints.py
GELD_PUNT_TEKST = 'Bij geld schrijf je een komma.'
LIJN_BINNEN = False        # G5: True (merge-fixlijst #14: geen sleutel buiten de getallenlijn), gezet in scripts/apply_hints.py; G4 ongewijzigd

def _int(v):
    v = str(v).strip()
    return int(v) if re.fullmatch(r'\d+', v) else None

def _cent(v):
    """Geldbedrag → centen (#19/#33): '€21,95', '€ 21,95', '21,95', '€3', '3', '€3,00', '8,8' → 2195 / 300 / 880. Geen punt als komma
    ('8.80' → None); een punt als duizendtal-scheider alleen in de vorm 1.250,00. None als het geen bedrag is."""
    v = str(v).strip().replace('\u00a0', ' ')
    m = re.fullmatch(r'€?\s*(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d{1,2}))?', v)
    if not m: return None
    e = int(m.group(1).replace('.', '')); c = m.group(2)
    return e * 100 + (int(c.ljust(2, '0')) if c else 0)

def geld(cent):
    """Centen → huisnotatie: €4 · €8,80 · €1.250,50 (geen ',00', komma, punt vanaf 1000 euro alleen bij 5+ cijfers volgens huisregel)."""
    e, c = divmod(int(cent), 100)
    es = f'{e:,}'.replace(',', '.') if e >= 10000 else str(e)
    return f'€{es}' if c == 0 else f'€{es},{c:02d}'

def geld_norm(v):
    """#33: genormaliseerde geldsleutel ('8,80' / '€ 8,8' / '€8,80' → '€8,80'; '€4,00' → '€4'); None als het geen bedrag is."""
    k = _cent(v); return geld(k) if k is not None else None

def _punt(x):
    """Huisregel: vanaf 10.000 met punt (beide vormen zijn sleutel)."""
    return [str(x)] + ([f'{x:,}'.replace(',', '.')] if x >= 10000 else [])

def _nums(t):
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', t)
    return [int(x) for x in re.findall(r'(?<![\w:])\d+(?![\w:])', t)]

def _uur(v):
    m = re.fullmatch(r'(\d+)(?: uur|:00)', str(v).strip())
    return int(m.group(1)) if m else None

def _wrap(h): return (h - 1) % 12 + 1

def _tijd(v, c):
    """(uur 1–12, minuut) uit een kloklabel (klokkenrij), 'h:mm', 'h uur', 'half h', 'kwart over h' of 'kwart voor h'."""
    v = str(v).strip(); jr = c.jr
    if jr.get('soort') == 'klokkenrij' and v in (jr.get('labels') or []):
        k = jr['klokken'][jr['labels'].index(v)]; return (_wrap(k['uur']), k['minuut'])
    if m := re.fullmatch(r'(\d{1,2}):(\d{2})', v): return (_wrap(int(m.group(1))), int(m.group(2)))
    if m := re.fullmatch(r'(\d{1,2}) uur', v): return (_wrap(int(m.group(1))), 0)
    if m := re.fullmatch(r'half (\d{1,2})', v): return (_wrap(int(m.group(1)) - 1), 30)
    if m := re.fullmatch(r'kwart over (\d{1,2})', v): return (_wrap(int(m.group(1))), 15)
    if m := re.fullmatch(r'kwart voor (\d{1,2})', v): return (_wrap(int(m.group(1)) - 1), 45)
    return None

MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
DAGEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def _datum(v):
    m = re.fullmatch(r'(\d{1,2}) ([a-z]+)', str(v).strip())
    return (int(m.group(1)), MAANDEN.index(m.group(2))) if m and m.group(2) in MAANDEN else None
def _dag_erbij(d, k):
    dag, mi = d; dag += k
    while dag > DAGEN[mi]: dag -= DAGEN[mi]; mi = (mi + 1) % 12
    while dag < 1: mi = (mi - 1) % 12; dag += DAGEN[mi]
    return f'{dag} {MAANDEN[mi]}'

class Ctx:
    def __init__(self, it):
        self.it = it; self.opg = (it['opgave'] or '').replace('\n', ' ')
        self.nums = _nums(self.opg); self.ans = str(it['antwoord']); self.a = _int(self.ans)
        self.jr = it['visual']['jsRender'] or {}
        self.g1 = self.nums[0] if self.nums else None; self.g2 = self.nums[1] if len(self.nums) > 1 else None
        self.ac = _cent(self.ans) if self.ans.startswith('€') else None      # geldantwoord in centen (#19/#32/#33)
    def code(self, v):
        v = str(v)
        if re.fullmatch(r'[A-L][1-9]', v): return v
        for d in self.jr.get('dingen', []):
            if d['wat'] == v: return d['vak']
        return None

def compile_regel(regel, c):
    """-> dict(exact=set|None, pred=callable|None, alles=bool, beschrijving) of None als de regel niet te lezen is."""
    r = regel.lower().replace('−', '-').strip()
    a, g1, g2, n = c.a, c.g1, c.g2, c.nums
    E = lambda *vals: {'exact': {str(x) for x in vals if x is not None and (not isinstance(x, int) or x >= 0)}}
    if r.startswith('andere fout') or 'of een andere fout' in r or r.startswith('ander vak') or 'een andere vorm of kleur' in r or 'een klok met een ander uur' in r:
        return {'alles': True}
    if r.startswith('volgorde omgedraaid'): return E('|'.join(reversed(c.ans.split('|'))))
    if r.startswith('de minsom omgedraaid'):
        return {'pred': lambda v: bool(re.fullmatch(r'(\d+) - (\d+)', v.replace('−', '-'))) and int(re.findall(r'\d+', v)[0]) < int(re.findall(r'\d+', v)[1])}
    if r.startswith('de plussom'): return {'pred': lambda v: '+' in v}
    if r.startswith('de minsom'): return {'pred': lambda v: '−' in v or ' - ' in v}
    if r.startswith('de keersom'): return {'pred': lambda v: '×' in v}
    # MKU-K03 vormnamen
    if r.startswith('fout = vierkant bij een rechthoek'):
        return {'pred': lambda v: (v, c.ans) in (('vierkant', 'rechthoek'), ('rechthoek', 'vierkant'))}
    m = re.match(r'fout = (cirkel|driehoek|rechthoek|vierkant)\b(?: \(bij een (\w+) of (\w+)\))?', r)
    if m:
        bij = {m.group(2), m.group(3)} - {None}
        return {'pred': lambda v: v == m.group(1) and (not bij or c.ans in bij)}
    if r.startswith('fout = ruit, ster of zeshoek'): return {'pred': lambda v: v in ('ruit', 'ster', 'zeshoek')}
    # spiegelen (MKU-E03): de stip is niet verplaatst = het kind tikt het vak van de stip zelf
    if r.startswith('stip niet verplaatst') or r.startswith('fout = het vak van de stip') or r.startswith('fout = het oorspronkelijke vak'):
        return E(c.jr.get('stip')) if c.jr.get('stip') else None
    # plattegrond-vakken (onze afspraak: letter = rij, cijfer = kolom)
    if r.startswith('goede letter, ander cijfer'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[0] == ca[0] and cv != ca}
    if r.startswith('goed cijfer, andere letter'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[1:] == ca[1:] and cv != ca}
    if r.startswith('letter en cijfer omgedraaid'):
        def omg(v):
            cv, ca = c.code(v), c.code(c.ans)
            return bool(cv and ca) and cv == f'{chr(64 + int(ca[1:]))}{ord(ca[0]) - 64}' and cv != ca
        return {'pred': omg}
    # klok
    if r.startswith('fout = 12 uur'): return E('12 uur') if c.ans != '12 uur' else {'exact': set()}
    if r.startswith('fout = een uur te vroeg of te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h - 1)} uur', f'{_wrap(h + 1)} uur') if h else None
    if r.startswith('fout = een uur te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h + 1)}:00' if ':' in c.ans else f'{_wrap(h + 1)} uur') if h else None
    # klok met half en kwart (#38): leest de klok uit de klokkenrij of de tekst
    if r.startswith('fout = klok een uur te laat') or r.startswith('fout = klok een uur te vroeg'):
        ta = _tijd(c.ans, c)
        if not ta: return None
        k = 1 if 'te laat' in r else -1; doel_t = (_wrap(ta[0] + k), ta[1])
        ex = {f'{doel_t[0]}:{doel_t[1]:02d}'} if re.fullmatch(r'\d{1,2}:\d{2}', c.ans) else set()
        return {'exact': ex, 'pred': lambda v: _tijd(v, c) == doel_t}
    if r.startswith('fout = grote wijzer verkeerd'):
        ta = _tijd(c.ans, c)
        if not ta: return None
        ex = {f'{ta[0]}:{m:02d}' for m in (0, 15, 30, 45) if m != ta[1]} if re.fullmatch(r'\d{1,2}:\d{2}', c.ans) else set()
        return {'exact': ex, 'pred': lambda v: (t := _tijd(v, c)) is not None and t[0] == ta[0] and t[1] != ta[1]}
    # afronden (G5 merge-fixlijst #12, Didactiek v1): het andere buurtiental/-honderdtal van getal1 (166 → 160 als 170 goed is)
    if r.startswith(('fout = het andere tiental/honderdtal naast getal1', 'fout = het andere buurtiental', 'fout = het andere buurhonderdtal', 'fout = het andere tiental', 'fout = het andere honderdtal')):
        if g1 is None or a is None: return None
        stap = 100 if ('honderdtal' in r and 'tiental/' not in r) or re.search(r'honderdtal', c.opg) else 10
        onder = g1 // stap * stap; boven = onder + stap
        if g1 == onder: return {'exact': set()}
        return E(onder if a == boven else boven if a == onder else None)
    # kalender (#41)
    if r.startswith('fout = een dag ernaast'):
        da = _datum(c.ans); return E(_dag_erbij(da, -1), _dag_erbij(da, 1)) if da else None
    # #49 (Didactiek 4cd): twee regels, elk met een eigen tekst; de oude gecombineerde regel blijft werken (beide datums)
    if r.startswith(('fout = gestopt bij de laatste of eerste dag van de maand', 'fout = gestopt op de laatste dag van de maand', 'fout = gestopt op de eerste dag van de maand')):
        ds = re.search(r'Het is (\d{1,2} [a-z]+)\.', c.opg); da = _datum(c.ans); d0 = _datum(ds.group(1)) if ds else None
        if not (da and d0) or da[1] == d0[1]: return {'exact': set()} if da and d0 else None
        vroeg, laat = (d0, da) if 'later' in c.opg else (da, d0)
        laatste, eerste = f'{DAGEN[vroeg[1]]} {MAANDEN[vroeg[1]]}', f'1 {MAANDEN[laat[1]]}'
        if r.startswith('fout = gestopt op de laatste dag'): return E(laatste)
        if r.startswith('fout = gestopt op de eerste dag'): return E(eerste)
        return E(laatste, eerste)
    # tabel (#42): uit jsRender.rijen
    if c.jr.get('soort') == 'tabel' and c.jr.get('rijen') and r.startswith(('fout = andere cel', 'fout = som van de rij', 'fout = som van de kolom', 'fout = som van twee cellen', 'fout = verschil van twee cellen')):
        rijen = [x['waarden'] for x in c.jr['rijen']]; cellen = [v for rij in rijen for v in rij]
        if r.startswith('fout = andere cel'): return E(*cellen)
        if r.startswith('fout = som van de rij'): return E(*[sum(rij) for rij in rijen])
        if r.startswith('fout = som van de kolom'): return E(*[sum(col) for col in zip(*rijen)])
        paren = [(x, y) for i, x in enumerate(cellen) for y in cellen[i + 1:]]
        if r.startswith('fout = som van twee cellen'): return E(*[x + y for x, y in paren])
        return E(*[abs(x - y) for x, y in paren])
    # letterlijke optie ('het smalle glas'): de regel is (een deel van) de tekst van de foute optie
    if not r.startswith('fout'): r = re.sub(r'\b(\d+) euro\b', r'€\1', r)   # fixlijst #32: G4-geld als €N; regel '3 euro' leest ook '€3'
    if not r.startswith('fout') and any(r in (o['tekst'] or '').lower() for o in c.it['opties'] or []):
        return {'pred': (lambda v: v.lower() == r) if r.startswith('€') else (lambda v: r in v.lower()), 'letterlijk': r}   # '€3' niet in '€30'
    # merge-punt #29: antwoord × 10 / : 10 (exact); bij geld het bedrag × 10 / : 10
    m = re.match(r'fout = (?:het )?antwoord (×|x|\*|:|÷|/) ?10\b', r)
    if m:
        keer = m.group(1) in ('×', 'x', '*')
        if c.ac is not None:
            if keer: return {'exact': {geld(c.ac * 10)}, 'pred': lambda v: _cent(v) == c.ac * 10}
            return ({'exact': {geld(c.ac // 10)}, 'pred': lambda v: _cent(v) == c.ac // 10} if c.ac % 10 == 0 else {'exact': set()})
        if a is None: return None
        if keer: return {'exact': set(_punt(a * 10))}
        return {'exact': set(_punt(a // 10))} if a % 10 == 0 and a >= 10 else {'exact': set()}
    # merge-punten #19/#32: geld ± 1 cent, ± 10 cent, ± €1 (sleutels in huisnotatie; de invoer wordt genormaliseerd, #33)
    m = re.match(r'fout = antwoord (±|\+|-) (?:(\d+) cent|€ ?(\d+))\b', r)
    if m:
        d = int(m.group(2)) if m.group(2) else int(m.group(3)) * 100
        if c.ac is None and (q_ := re.fullmatch(r'(\d+) cent', c.ans.strip())):      # Oef-#1028 (Oefeningen 19:43, hook zet_motor1028.py; V-#1050): 'fout = antwoord ± c cent' ook bij een antwoord in centen
            ac_ = int(q_.group(1)); dl_ = ([ac_ - d] if m.group(1) in ('±', '-') and ac_ - d >= 0 else []) + ([ac_ + d] if m.group(1) in ('±', '+') else [])
            cc_ = lambda v: int(w_.group(1)) if (w_ := re.fullmatch(r'(\d+) cent', str(v).strip())) else _cent(v)
            return {'exact': {f'{x} cent' if x < 100 else geld(x) for x in dl_}, 'pred': lambda v: cc_(v) in dl_}
        if c.ac is None: return None
        doel = ([c.ac - d] if m.group(1) in ('±', '-') and c.ac - d >= 0 else []) + ([c.ac + d] if m.group(1) in ('±', '+') else [])
        return {'exact': {geld(x) for x in doel}, 'pred': lambda v: _cent(v) in doel}
    # getallen
    if a is None and not n: return None
    if re.match(r'fout = getal1 \+ getal2', r): return E(g1 + g2) if g2 is not None else None
    if re.match(r'fout = getal1 - getal2 of getal2 - getal1', r) or r.startswith('fout = verschil van de getallen'):
        return E(abs(g1 - g2)) if g2 is not None else None
    if re.match(r'fout = getal2 - de eenheden van getal1', r): return E(g2 - g1 % 10) if g2 is not None else None
    # nieuw 1 okt (fixlijst G4, besluit Dave): keersom van de twee getallen; eenheden van een getal
    if re.match(r'fout = getal1 [×x\*] getal2', r): return E(g1 * g2) if g2 is not None else None
    m = re.match(r'fout = (?:de )?eenheden van getal([12])', r)
    if m: g = g1 if m.group(1) == '1' else g2; return E(g % 10) if g is not None else None
    if re.match(r'fout = getal1\b', r): return E(g1)
    if re.match(r'fout = getal2\b', r): return E(g2)
    if re.match(r'fout = getal \+ 10 of antwoord \+ 10', r): return E(g1 + 10, a + 10)
    if re.match(r'fout = getal - 10 of antwoord - 10', r): return E(g1 - 10, a - 10)
    if re.match(r'fout = getal \+ 1\b', r): return E(g1 + 1)
    if r.startswith('fout = getal + bekend deel'): return E(n[0] + n[-1])
    if r.startswith('fout = een getal uit de vraag'): return E(*n)
    if r.startswith('fout kleiner dan het kleinste getal'): m0 = min(n); return {'pred': lambda v: _int(v) is not None and _int(v) < m0, 'kleinerDan': m0}
    if r.startswith('fout kleiner dan het getal in de vraag'): return {'pred': lambda v: _int(v) is not None and _int(v) < g1, 'kleinerDan': g1}
    if r.startswith('fout = laatste getal van de rij'):
        m = re.search(r'((?:\d+|□)(?:, (?:\d+|□))+)', c.opg); seq = m.group(1).split(', ') if m else []
        i = seq.index('□') if '□' in seq else len(seq)
        return E(int(seq[i - 1])) if i > 0 else None
    if r.startswith('fout = het aantal in de tekening'): return E(c.jr.get('aantal'))
    if r.startswith('fout = het getal dat eraf gaat'):
        m = re.search(r'(\d+) − (\d+)', c.opg.split('.')[1] if '.' in c.opg else c.opg); return E(int(m.group(2))) if m else None
    if r.startswith('fout = het deel dat al in de plussom staat'):
        m = re.search(r'(\d+) \+ □', c.opg); return E(int(m.group(1))) if m else None
    if r.startswith('fout = het hele getal'):
        m = re.search(r'□ = (\d+)', c.opg) or re.search(r'hoeveel (\d+) −', c.opg) or re.search(r'ook: (\d+) −', c.opg)
        return E(int(m.group(1))) if m else None
    if r.startswith('fout = getal opgeteld in plaats van eraf'):
        m = re.search(r'hoeveel (\d+) − (\d+)', c.opg) or re.search(r'(\d+) − (\d+) = □', c.opg)
        return E(int(m.group(1)) + int(m.group(2))) if m else None
    if a is None: return None
    # nieuw 1 okt (fixlijst G4, besluit Dave): 'antwoord ± getal1' (één groepje te veel/te weinig) en 'eenheden als antwoord'
    m = re.match(r'fout = antwoord (±|\+|-) getal([12])', r)
    if m:
        g = g1 if m.group(2) == '1' else g2
        if g is None: return None
        return E(*([a - g] if m.group(1) in ('±', '-') else []), *([a + g] if m.group(1) in ('±', '+') else []))
    if re.match(r'fout = (?:de )?eenheden (?:als antwoord|van het antwoord)', r) or r.startswith('eenheden als antwoord'):
        return E(a % 10) if a >= 10 else {'exact': set()}
    if r.startswith('fout = antwoord gedeeld door getal1'):      # #40 staafdiagram: streepjes geteld
        return E(a // g1) if g1 and a % g1 == 0 else {'exact': set()}
    if r.startswith('fout = antwoord ± 1'): return E(a - 1, a + 1)
    if re.match(r'fout = antwoord \+ 9 of \+ 10', r): return E(a + 9, a + 10)
    m = re.match(r'fout = antwoord ([+-]) (\d+) of meer', r)
    if m:
        k = int(m.group(2))
        if m.group(1) == '+': return {'pred': lambda v: _int(v) is not None and _int(v) >= a + k, 'vanaf': a + k}
        return {'pred': lambda v: _int(v) is not None and _int(v) <= a - k, 'totEnMet': a - k}
    m = re.match(r'fout = antwoord ([+-]) (\d+)', r)
    if m: return E(a + int(m.group(2)) if m.group(1) == '+' else a - int(m.group(2)))
    if r.startswith('fout ligt 1 of 2 naast'): return E(a - 2, a - 1, a + 1, a + 2)
    if r.startswith('fout ligt 1 naast'): return E(a - 1, a + 1)
    if r.startswith('fout ligt 2 naast'): return E(a - 2, a + 2)
    return None

PLAATS = re.compile(r'[\[{](getal1|getal2|antwoord|uur in woorden|uur als cijfer)[\]}]')
UUR_WOORD = {1: 'één', 2: 'twee', 3: 'drie', 4: 'vier', 5: 'vijf', 6: 'zes', 7: 'zeven', 8: 'acht', 9: 'negen', 10: 'tien', 11: 'elf', 12: 'twaalf'}
def vul_in(tekst, c):
    """Vult sjabloonteksten per item in: [uur in woorden], [uur als cijfer] en (fixlijst #48) [getal1], [getal2], [antwoord]
    (ook met {…}: '{getal1}'). getal1/getal2 = eerste/tweede getal in de vraag. None als er niets in te vullen valt of een waarde ontbreekt."""
    if not PLAATS.search(tekst): return None
    h = _uur(c.ans)
    waarden = {'getal1': c.g1, 'getal2': c.g2, 'antwoord': c.ans, 'uur in woorden': UUR_WOORD.get(h) if h else None, 'uur als cijfer': h}
    if any(waarden[m.group(1)] is None for m in PLAATS.finditer(tekst)): return None
    return PLAATS.sub(lambda m: str(waarden[m.group(1)]), tekst)

def per_item_tekst(regel, tekst):
    return 'tekst per item' in regel or '…' in tekst or '[plek]' in tekst or '[andere plek]' in tekst or bool(PLAATS.search(tekst))

PLACEHOLDER_STIP = '[TEKST NODIG (Oefeningen): stip niet verplaatst]'
def is_spiegel(it):
    jr = it['visual']['jsRender'] or {}
    return jr.get('soort') == 'vorm' and bool(jr.get('stip')) and bool(jr.get('as'))
def heeft_stipregel(st):
    return any(re.match(r'(stip niet verplaatst|fout = het vak van de stip|fout = het oorspronkelijke vak)', f['regel'].lower()) for f in st['foutHints'])

def _pas_toe_kern(it, st, alle_cellen=None):
    """st = somtype-entry uit hints/batch*.json. Zet it['foutHints'], it['foutRegels'], it['foutHintsTekst']."""
    c = Ctx(it)
    claude = [dict(f) for f in it['extraVelden'].get('claudeFoutHints') or []]
    claude_txt = {f['fout']: f['uitleg'] for f in claude}
    vervangen = {v['claudeTekst'] for v in st.get('claudeVervangen', [])} | {f['claudeTekst'] for f in st['foutHints'] if f.get('claudeTekst')}
    merge = {m['fout']: m for m in it['extraVelden'].get('mergeFoutHints') or []}
    regels = []
    for f in st['foutHints']:
        comp = compile_regel(f['regel'], c)
        per_item = per_item_tekst(f['regel'], f['tekst'])
        if comp is None and f['bron'] in ('claude', 'claude-taalfix'):     # niet te lezen Claude-regel: op de Claude-sleutels (claudeDenkfout)
            dk = f.get('claudeDenkfout')
            keys = {k['fout'] for k in claude if not dk or any(d['fout'] == k['fout'] and d['denkfout'] == dk for d in it['extraVelden'].get('claudeDenkfouten') or [])}
            comp = {'exact': keys, 'claudeSleutels': True}
            # fixlijst #48 (1): een taalfix met een vaste tekst (zonder '…') zet die vaste tekst op de Claude-sleutels; anders Claudes tekst per item
            per_item = f['bron'] == 'claude' or per_item

        regels.append((f, comp, per_item))
    # MKU-E03 spiegelen: 'stip niet verplaatst' gaat vóór de algemene regels; zonder tekst van Oefeningen een gemarkeerde plaatshouder
    it['controle']['foutHintPlaceholder'] = None
    if is_spiegel(it) and not heeft_stipregel(st):
        f = {'regel': 'stip niet verplaatst (fout = het vak van de stip)', 'soort': 'stip niet verplaatst', 'bron': 'merge-plaatshouder', 'tekst': PLACEHOLDER_STIP}
        regels.insert(0, (f, {'exact': {it['visual']['jsRender']['stip']}}, False))
        it['controle']['foutHintPlaceholder'] = ['stip niet verplaatst']
    # kandidaten
    if it['opties']: kand = [o['tekst'] for o in it['opties'] if o['tekst'] != c.ans]
    elif alle_cellen: kand = [v for v in alle_cellen if v != c.ans]
    else:
        # merge-punt #35b: een leesbare regel met een ingevulde [getal]-tekst voegt ook zijn sleutels toe (niet alleen Claudes sleutels)
        kand = list(dict.fromkeys([k['fout'] for k in claude] + sorted({v for f, comp, pi in regels if comp and (not pi or (not comp.get('claudeSleutels') and vul_in(f['tekst'], c))) for v in comp.get('exact', ())},
                                                                        key=lambda x: (_int(x) is None, _int(x) or 0, x))))
        kand = [v for v in kand if v != c.ans]
        # G5 merge-fixlijst #14: geen fout-sleutel buiten de getallenlijn (je kunt hem niet aantikken)
        if LIJN_BINNEN and c.jr.get('soort') == 'getallenlijn' and isinstance(c.jr.get('van'), int) and isinstance(c.jr.get('tot'), int):
            kand = [v for v in kand if _int(v) is None or c.jr['van'] <= _int(v) <= c.jr['tot']]
        # G5 merge-fixlijst #1/#13: geen fout-sleutel boven het bereik bij afronden (BEREIK_AFRONDEN, gezet door apply_hints van de groep)
        if BEREIK_AFRONDEN and re.match(r'Rond \d', c.opg):
            kand = [v for v in kand if _int(v) is None or _int(v) <= BEREIK_AFRONDEN]
    # merge-punt #33 (GELD_PUNT, opt-in per groep): een geldbedrag met een punt in plaats van een komma ('8.80') krijgt
    # 'Bij geld schrijf je een komma.' (eerste regel; sleutels '8.80' en '€8.80' bij open geldvragen)
    if GELD_PUNT and c.ac is not None and not it['opties'] and c.ac % 100:
        e, ct = divmod(c.ac, 100); pk = [f'{e}.{ct:02d}', f'€{e}.{ct:02d}'] + ([f'{e}.{ct // 10}', f'€{e}.{ct // 10}'] if ct % 10 == 0 else [])
        fp = {'regel': 'fout = punt in plaats van komma (geld)', 'soort': 'punt in plaats van komma', 'bron': 'merge (#33)', 'tekst': GELD_PUNT_TEKST}
        regels.insert(0, (fp, {'exact': set(pk), 'pred': lambda v: bool(re.fullmatch(r'€?\s*\d+\.\d{1,2}', str(v).strip()))}, False))
        kand = kand + [k for k in pk if k not in kand]
    out = []; ongebruikt = []
    for v in kand:
        hit = None
        for f, comp, per_item in regels:
            if comp is None: continue
            ok = comp.get('alles') or (v in comp.get('exact', ())) or (comp.get('pred') and comp['pred'](v))
            if not ok: continue
            if per_item and vul_in(f['tekst'], c):
                hit = {'fout': v, 'uitleg': vul_in(f['tekst'], c), 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f"{f['bron']} (per item)"}; break
            if per_item:
                if v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
                    hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': f['regel'], 'soort': f.get('soort'), 'bron': 'claude (per item)'}; break
                continue
            tekst = f['tekst']
            if ' / ' in tekst and f['bron'] in ('claude', 'claude-taalfix'):
                # twee teksten van Claude: neem de tekst die bij dit item hoort (bij een taalfix: die het meest lijkt op Claudes tekst)
                delen = tekst.split(' / ')
                ct = claude_txt.get(v)
                tekst = max(delen, key=lambda d: difflib.SequenceMatcher(None, d, ct).ratio()) if ct else delen[0]
            hit = {'fout': v, 'uitleg': tekst, 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron']}; break
        if hit is None and v in merge:
            m = merge[v]; hit = {'fout': v, 'uitleg': m['uitleg'], 'regel': m['regel'], 'soort': None, 'bron': 'merge'}
        if hit is None and v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
            hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': '(geen regel; Claude-tekst blijft)', 'soort': None, 'bron': 'claude (geen regel)'}
        if hit: hit['stap'] = None; out.append(hit)
        elif v in claude_txt: ongebruikt.append(v)
    regels_out = []
    for f, comp, per_item in regels:
        if comp is None: regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'tekst': f['tekst'], 'match': None, 'leesbaar': False}); continue
        mt = {}
        if comp.get('alles'): mt = {'alles': True}
        elif 'exact' in comp: mt = {'waarden': sorted(comp['exact'], key=lambda x: (_int(x) is None, _int(x) or 0, x))}
        for k in ('kleinerDan', 'vanaf', 'totEnMet'):
            if k in comp: mt = {k: comp[k]}
        if comp.get('pred') and not mt: mt = {'waarden': [h['fout'] for h in out if h['regel'] == f['regel']], 'opOpties': True}
        regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron'], 'tekst': (vul_in(f['tekst'], c) if per_item else f['tekst']), 'perItem': per_item, 'match': mt, 'leesbaar': True})
    it['foutHints'] = [{'stap': h['stap'], 'fout': h['fout'], 'uitleg': h['uitleg'], 'regel': h['regel'], 'soort': h['soort'], 'bron': h['bron']} for h in out]
    it['foutRegels'] = regels_out
    # merge-punt #35a: 'andere fout' met [getal1]/[getal2]/[antwoord] → de per item ingevulde tekst (viel eerder weg: None)
    it['algemeneFoutHint'] = next(((vul_in(f['tekst'], c) if pi else f['tekst']) for f, comp, pi in regels if comp and comp.get('alles') and (not pi or vul_in(f['tekst'], c))), None)
    it['foutHintsTekst'] = ' · '.join(f"{h['fout']} → {h['uitleg']}" for h in out) or None
    it['controle']['zonderFoutHints'] = not out
    it['controle']['foutHintsNietToegepast'] = ongebruikt
    return [f['regel'] for f, comp, _ in regels if comp is None]

# r13 kloktijdronde (8 okt): overgenomen uit g8/scripts/fout_regels.py
# Kloktijden (besluit Didactiek 8 okt 15:46): de motor rekent intern met 'h:mm'. Heeft een item zijn tijd in de huisvorm ('14.30 uur' als antwoord of
# optie, of '(Typ als 14.30.)'), dan gaan een kopie van het item en van de hint-entry eerst naar 'h:mm'; daarna gaan foutHints, foutRegels en
# algemeneFoutHint terug naar de huisvorm: sleutel '14.30 uur', in teksten '14.30 uur' (na 'Typ als' zonder 'uur'), foutRegels.match.waarden in alle
# drie de vormen ('14.30 uur', '14.30', '14:30'). Een regel mag dus in beide vormen staan. Items met digitaleKlok: true en items zonder tijd in de
# huisvorm gaan ongewijzigd door de motor. KLOK_PUNT = False zet dit uit.
KLOK_PUNT = True
import copy as _copy_klok
_KP = re.compile(r'(?<![\d.,:])(\d{1,2})\.(\d{2})(?: uur)?(?![\d])')
_KD = re.compile(r'(?<![\d:.,])(\d{1,2}):(\d{2})(?![\d:])')
_KSKIP = {'bron', 'licentie', 'controle', 'merge', 'id', 'bronVariant', 'jsRender', 'husselPlan'}
def _klok_ok(h, m): return int(h) <= 24 and int(m) <= 59
def _klok_heeft_punt(it):
    if it.get('digitaleKlok'): return False
    w = [str(it.get('antwoord') or '')] + [str(o.get('tekst')) for o in it.get('opties') or []]
    return any(re.fullmatch(r'\s*\d{1,2}\.\d{2} uur\s*', x) for x in w) or bool(re.search(r'\(Typ als \d{1,2}\.\d{2}\.\)', it.get('opgave') or ''))
def _klok_naar_dubbelepunt(o):
    if isinstance(o, dict): return {k: (v if k in _KSKIP else _klok_naar_dubbelepunt(v)) for k, v in o.items()}
    if isinstance(o, list): return [_klok_naar_dubbelepunt(v) for v in o]
    if isinstance(o, str): return _KP.sub(lambda m: f'{m.group(1)}:{m.group(2)}' if _klok_ok(m.group(1), m.group(2)) else m.group(0), o)
    return o
def _klok_tekst(t):
    def r(m):
        h, mi = m.group(1), m.group(2)
        if not _klok_ok(h, mi): return m.group(0)
        voor, na = t[:m.start()], t[m.end():]
        if re.search(r'(Typ als|zoals)\s*$', voor): return f'{h}.{mi}'
        return f'{h}.{mi}' if na.startswith(' uur') else f'{h}.{mi} uur'
    return _KD.sub(r, t)
def _klok_vormen(w):
    m = re.fullmatch(r'\s*(\d{1,2})[:.](\d{2})(?: uur)?\s*', str(w))
    if not m or int(m.group(1)) > 24: return [w]      # V-#1012 (Didactiek r13, les 387): ook een foutsleutel met minuten ≥ 60 ('12:85') in alle drie de vormen, want een kind typt volgens de instructie '12.85'
    return [f'{m.group(1)}.{m.group(2)} uur', f'{m.group(1)}.{m.group(2)}', f'{m.group(1)}:{m.group(2)}']
def _klok_naar_punt(o, k=None):
    if isinstance(o, dict): return {kk: _klok_naar_punt(v, kk) for kk, v in o.items()}
    if isinstance(o, list):
        if k == 'waarden': return list(dict.fromkeys(x for w in o for x in (_klok_vormen(w) if isinstance(w, str) else [w])))
        return [_klok_naar_punt(v) for v in o]
    if isinstance(o, str): return _klok_tekst(o)
    return o
def pas_toe(it, st, alle_cellen=None):
    if not (KLOK_PUNT and _klok_heeft_punt(it)): return _pas_toe_kern(it, st, alle_cellen)
    a, e = _klok_naar_dubbelepunt(it), _klok_naar_dubbelepunt(st)
    oud = {k: _copy_klok.deepcopy(a.get(k)) for k in a}
    regels = {json_klok(r2): r1 for r1, r2 in zip(_regels_van(st), _regels_van(e))}
    terug = _pas_toe_kern(a, e, alle_cellen)
    for k in a:
        if k not in oud or a[k] != oud[k]: it[k] = _klok_naar_punt(a[k], k)
    return [regels.get(json_klok(r), r) for r in terug] if isinstance(terug, list) else terug
def _regels_van(st): return [f.get('regel') for f in st.get('foutHints') or []]
def json_klok(r): return r if isinstance(r, str) else repr(r)
