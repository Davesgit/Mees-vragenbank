"""Z-#1092 (Oefeningen 15 okt): plekwoorden voor getallen in G5 (les 193) → rol. Gedeeld door zet_z1092 en check_z1092."""
import re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r4')); from lenen_lib import getallen, ant
PLEK = re.compile(r"\b(?:[Hh]et|van het|bij het) (?:eerste|tweede|derde)(?: ronde)? (?:getal|bedrag)\b|\bhet (?:eerste|tweede)(?= (?:af|naar|van|op|bedrag)\b|[.,?])|\bdan het tweede\b|\b(?:min|plus|in) het (?:tweede|eerste)\b", re.I)
UIT = ('G5-MEET-E06', 'G5-VBN-E03')
UIT_ENTRY = set()      # Oef-#1052 (Didactiek 17:02): ook het rooster krijgt een rolwoord; de les-193-uitzondering blijft alleen voor coördinaten
# rooster (Oef-#1052): vaste zin → rolzin, per entry; waar per item: zie rooster_ok()
ROOSTER = {
 ('G5-GET-M05', 5): [('Het eerste getal zegt hoeveel rijen je kleurt. Het tweede getal zegt hoeveel hokjes er in elke rij komen.',
                      'In de som staan het aantal rijen en hoeveel hokjes er in één rij staan: zoveel rijen, met in elke rij zoveel hokjes.')],
 ('G5-MEET-E03', 1): [('Het eerste getal is het aantal rijen, het tweede hoeveel hokjes er in elke rij komen.',
                       'Het aantal rijen keer hoeveel hokjes er in één rij staan, moet de oppervlakte zijn.')],
}
def rooster_ok(k, x):
    """M05 #5: de vraag 'a × b' en het antwoord 'a rijen van b hokjes' (rijen = eerste factor, de rolzin noemt de rol); MEET-E03 #1: oppervlakte A uit de
    vraag = het antwoord, en A is te schrijven als rijen × hokjes met beide ≥ 2 (een echte rechthoek)"""
    o, a = x.get('opgave') or '', str(x['antwoord'])
    if k == ('G5-GET-M05', 5):
        m, n = re.search(r'(\d+) × (\d+)', o), re.fullmatch(r'\s*(\d+) rijen van (\d+) hokjes\s*', a)
        return bool(m and n and m.groups() == n.groups())
    if k == ('G5-MEET-E03', 1):
        m, n = re.search(r'oppervlakte van (\d+) hokjes', o), re.search(r'rechthoek van (\d+) hokjes', a)
        return bool(m and n and m.group(1) == n.group(1) and any(int(m.group(1)) % r == 0 and 2 <= int(m.group(1)) // r for r in range(2, int(m.group(1)))))
    return False
def geld(s):
    m = re.search(r'€\s?(\d+)(?:,(\d{2}))?', s); return int(m.group(1)) * 100 + int(m.group(2) or 0) if m else None
def bedragen(opg): return [int(a) * 100 + int(b or 0) for a, b in re.findall(r'€\s?(\d+)(?:,(\d{2}))?', opg or '')]
def soort_item(x):
    """'aanvul' (□ in de som), 'min', 'plus', 'keer', 'geldmin', 'gedeeld' of None; en de twee getallen (in volgorde van de vraag)"""
    o = x.get('opgave') or ''
    if ('□' in o or '...' in o) and ':' in o:      # deelsom met hokje (M05 #2: '54 : 6 = □')
        n = getallen(o); a = ant(x)
        return ('gedeeld', n[:2]) if len(n) >= 2 and n[1] and a is not None and n[0] == n[1] * a else (None, n)
    if '□' in o or '...' in o: return 'aanvul', getallen(o)[:2]
    b = bedragen(o); A = geld(str(x['antwoord']))
    if len(b) >= 2 and A is not None:
        if b[0] - b[1] == A: return 'geldmin', b[:2]
        if b[0] + b[1] == A: return 'geldplus', b[:2]
    n = getallen(o); a = ant(x)
    if (m := re.fullmatch(r'\s*(\d+) [−-] (\d+)\s*', str(x['antwoord']))): return 'min', [int(m.group(1)), int(m.group(2))]      # 'welke som hoort erbij' (E05 #11)
    if len(n) >= 2 and 'ongeveer' in o and '−' in o and n[0] > n[1]: return 'min', n[:2]      # schatten (E05 #22/#31)
    if len(n) < 2 or a is None: return None, n
    if '×' in o or ' keer ' in o: return ('keer', n[:2]) if n[0] * n[1] == a else (None, n)
    if ':' in o and n[1] and n[0] // n[1] == a: return 'gedeeld', n[:2]
    if n[0] - n[1] == a: return 'min', n[:2]
    if n[0] + n[1] == a: return 'plus', n[:2]
    if n[0] * n[1] == a: return 'keer', n[:2]      # verhaalsom zonder ×-teken (E07 #8)
    return None, n
# vervangingen per soort som (volgorde telt). 'grootste/kleinste' is waar zodra de twee getallen verschillen (bij min altijd: a − b ≥ 0);
# de check rekent dat per item na. Bij aanvullen is het eerste getal 'het getal dat er al staat'.
ROL = {
 'aanvul': [(r'\b([Hh])et eerste getal\b', r'\1et getal dat er al staat')],
 'groot': [(r'\b([Hh])et tweede( ronde)? (getal|bedrag) van het eerste af\b', r'\1et kleinste\2 \3 van het grootste af'),
           (r'\b([Hh])et tweede van het eerste af\b', r'\1et kleinste van het grootste af'),
           (r'\b([Hh])et eerste( ronde)? (getal|bedrag)\b', r'\1et grootste\2 \3'), (r'\b([Hh])et tweede( ronde)? (getal|bedrag)\b', r'\1et kleinste\2 \3'),
           (r'\bhet tweede (naar|op)\b', r'het kleinste \1'), (r'\bvan het eerste\b(?= af\b|[.,])', 'van het grootste'), (r'\bdan het tweede\b', 'dan het kleinste'),
           (r'\b(min|plus|in) het (tweede|eerste)\b', lambda m: f"{m.group(1)} het {'kleinste' if m.group(2) == 'tweede' else 'grootste'}")],
}
def rolsoort(soorten):
    s = set(soorten)
    if s == {'aanvul'}: return 'aanvul'
    if s and s <= {'min', 'plus', 'keer', 'geldmin', 'geldplus', 'gedeeld'} and len(s) == 1: return 'groot'
    return None
def vervang(t, rs):
    for a, b in ROL[rs]: t = re.sub(a, b, t)
    return t
