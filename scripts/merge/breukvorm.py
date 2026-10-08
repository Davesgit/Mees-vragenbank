"""Gedeelde VORM-regel voor breuken (G6 merge-fixlijst #170, besluit Dave 21:24; ook G7).
Een even grote breuk geldt als goed (antwoordOokGoed + breukGelijkwaardigGoed = True), BEHALVE als de opgave een vorm vraagt:
'zo eenvoudig mogelijk', 'met noemer N' of '?/N'. Een breuk op de getallenlijn ('op de lijn van') beoordeelt de app op de plek (beoordeling,
#169), daar is geen lijst nodig. De motor (fout_regels.pas_toe) maakt bij breukGelijkwaardigGoed geen sleutel die een even grote breuk is.
ook-goed: de eenvoudigste vorm, de veelvouden daarvan met een noemer tot en met 100, en bij een breuk groter dan 1 ook het gemengde getal.
Gebruik: import breukvorm as BV; BV.pas_toe(it) (in de build, vóór de hints) en n_fail = BV.rapport(items) (in check_merge_notatie)."""
import re
from fractions import Fraction
BREUK = re.compile(r'(?:(\d+) )?(\d+)/(\d+)')
VORM = re.compile(r'zo eenvoudig mogelijk|zo eenvoudig mogelijke|met noemer \d+|\?/\d+', re.I)
LIJN = re.compile(r'op de lijn van', re.I)
def waarde(v):
    m = BREUK.fullmatch(str(v).strip())
    if not m or int(m.group(3)) == 0: return None
    return int(m.group(1) or 0) + Fraction(int(m.group(2)), int(m.group(3)))
def soort(it):
    """'vorm' (de vorm wordt gevraagd), 'lijn', 'waarde' (een even grote breuk is goed) of None (geen breukantwoord)."""
    a = str(it.get('antwoord') or '')
    if not BREUK.fullmatch(a.strip()) or it.get('type') not in ('kale', None): return None
    o = it.get('opgave') or ''
    if VORM.search(o): return 'vorm'
    if LIJN.search(o): return 'lijn'
    return 'waarde'
def gelijk(a):
    w = waarde(a); out = []
    if w is None or w <= 0: return out
    for k in range(1, 101):
        if (w.denominator * k) > 100: break
        x = f'{w.numerator * k}/{w.denominator * k}'
        if x != a: out.append(x)
    if w > 1 and w.denominator > 1:
        g, r = divmod(w.numerator, w.denominator); out.append(f'{g} {r}/{w.denominator}')
    return out
def pas_toe(it):
    if soort(it) != 'waarde': return False
    ook = [x for x in (it.get('antwoordOokGoed') or []) if x not in gelijk(it['antwoord'])] + gelijk(it['antwoord'])
    it['antwoordOokGoed'] = ook; it['breukGelijkwaardigGoed'] = True
    it['merge']['breukvorm170'] = 'een even grote breuk is goed (antwoordOokGoed)'
    return True
def rapport(items, toon=True):
    F = []
    for it in items:
        s = soort(it); a = str(it.get('antwoord') or ''); ook = it.get('antwoordOokGoed') or []
        if s == 'waarde':
            mist = [x for x in gelijk(a)[:3] if x not in ook]
            if not it.get('breukGelijkwaardigGoed') or mist: F.append(f"{it['id']}: een even grote breuk telt niet als goed ({a}; mist {mist[:3]})")
            fa = waarde(a)
            for f in it.get('foutHints') or []:
                if waarde(f['fout']) == fa: F.append(f"{it['id']}: fout-sleutel {f['fout']} is even groot als het antwoord {a}")
        elif s in ('vorm', 'lijn'):
            if it.get('breukGelijkwaardigGoed') or any(waarde(x) == waarde(a) and x != a for x in ook):
                F.append(f"{it['id']}: de opgave vraagt een vorm ('{(VORM.search(it['opgave']) or LIJN.search(it['opgave'])).group(0)}'), maar een even grote breuk staat bij ook goed")
    if toon:
        print(f"\nBREUKVORM (#170: even grote breuk goed, behalve bij 'zo eenvoudig mogelijk' / 'met noemer N' / '?/N'): {len(F)} (FAIL)")
        for x in F[:15]: print('  FAIL BREUKVORM', x)
    return len(F)
