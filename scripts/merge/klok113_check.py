#!/usr/bin/env python3
"""Gedeelde regel voor check_hints G4–G8 (G5 merge-fixlijst #113). Besluit Didactiek 19:42 (vervangt de regel van 19:15).
Kijkt naar de tijden van ALLE klokitems van het somtype (opgave + antwoord, in woorden of u:mm), niet alleen naar het item zelf.
  WARN (1) een tekst met 'net voorbij' in een somtype dat ook tijden heeft met half, '… over half', '… voor half', kwart voor of '… voor'.
  WARN (2) een tekst somt tijdsoorten op ('bij vijf over en tien over …') en mist een tijdsoort die wel in het somtype voorkomt.
       Een opsomming die eindigt op '…' (zoals in een Ouderzin: 'vijf over, tien over, tien voor half …') is bedoeld als niet volledig: INFO.
  INFO 'net voorbij' in een kloksomtype met alleen tijden zonder half/voor (heel uur, vijf over, tien over, kwart over).
Aanvulling Overzicht 19:46: er wordt per zin gekeken.
  - Komt 'net voorbij' in een zin die begint met 'Anders', na een voorwaarde in dezelfde tekst zoals «Hoor je 'half' of 'voor'?», dan is het in orde (INFO), ook in een gemengd somtype.
  - Kwart over, vijf over en tien over zonder half zijn nooit een WARN. Dat geldt als de zin met 'net voorbij' alleen zulke tijden noemt, of als de tijd van het item zelf vijf/tien/kwart over is (bij een fout-hint of algemeneFoutHint). Dan wordt het INFO.
Teksten: per item de fout-hints (uitleg) en de algemeneFoutHint; per somtype Hint 1, Hint 2 en Ouderzin uit somtypen/<doel>.md.
Aanscherping G5 merge-fixlijst #120 (Didactiek 20:04, besluit Dave):
  (1) 'net voorbij' in een zin met alleen vijf/tien over (zonder half) is INFO, behalve als het item zelf (fout-hint, algemeneFoutHint) of het
      somtype (Hint 1/Hint 2/Ouderzin) een tijd heeft op vijf of tien over half (35/40 minuten): dan WARN (#120-1). Kwart over blijft INFO.
  (2) De uitzondering voor een opsomming die eindigt op '…' geldt alleen voor de Ouderzin. In een fout-hint, algemeneFoutHint of Hint 1/2
      is zo'n opsomming die een tijdsoort mist een WARN (#113-2).
  (3) 'Anders … net voorbij' is alleen INFO als de voorwaarde «Hoor je 'half' of 'voor'?» in de zin direct ervóór staat (i − 1), of in
      zin i − 2 met een zin 'Dan …' daartussen (i − 1). Die tweede vorm is nodig voor de goedgekeurde V-d-tekst («Hoor je 'half' of 'voor'
      in de tijd? Dan staat hij nog vóór het uur uit de tijd. Anders staat hij net voorbij dat uur.»); letterlijk alleen i − 1 zou die WARN geven.
In check_hints: item_checks roept check113(it, t, fh, items) aan (WARN terug, INFO in een buffer); check() roept
check113_somtype(tag, s, items) aan en pakt de INFO-buffer met pop_info()."""
import re
GETAL = {'een':1,'één':1,'twee':2,'drie':3,'vier':4,'vijf':5,'zes':6,'zeven':7,'acht':8,'negen':9,'tien':10,'elf':11,'twaalf':12}
U = r'(?:\d{1,2}|' + '|'.join(GETAL) + r')'
WOORD = [  # (regex, minuut)
    (rf'\bvijf over half {U}\b', 35), (rf'\btien over half {U}\b', 40), (rf'\bvijf voor half {U}\b', 25), (rf'\btien voor half {U}\b', 20),
    (rf'\bkwart over {U}\b', 15), (rf'\bkwart voor {U}\b', 45), (rf'\bvijf over {U}\b', 5), (rf'\btien over {U}\b', 10),
    (rf'\bvijf voor {U}\b', 55), (rf'\btien voor {U}\b', 50), (rf'(?<!over )(?<!voor )\bhalf {U}\b', 30), (rf'\b{U} uur\b', 0)]
DIGI = re.compile(r'\b(\d{1,2}):(\d{2})\b')
NAAM = {0:'heel uur',5:'vijf over',10:'tien over',15:'kwart over',20:'tien voor half',25:'vijf voor half',30:'half',
        35:'vijf over half',40:'tien over half',45:'kwart voor',50:'tien voor',55:'vijf voor'}
def groep(m):   # grove tijdsoort voor regel 1
    if m == 0 or m < 15: return 'over'
    if m == 15: return 'kwart over'
    if m < 30: return 'voor half'
    if m == 30: return 'half'
    if m < 45: return 'over half'
    if m == 45: return 'kwart voor'
    return 'voor'
MET_HALF_VOOR = {'half', 'over half', 'voor half', 'kwart voor', 'voor'}
NV = re.compile(r'\bnet voorbij\b', re.I)
T = r'(?:(?:vijf|tien) (?:over|voor) half|(?:vijf|tien|kwart) (?:over|voor)|half|(?:het )?hele uur|(?:een )?heel uur)'
OPSOM = re.compile(rf'\b({T})((?:\s*(?:,\s*(?:en |of )?|en |of )\s*{T}\b)+)(\s*…)?', re.I)
def _minuten(txt):
    out = set(); low = (txt or '').lower()
    for u, mm in DIGI.findall(low):
        if int(u) <= 24 and int(mm) < 60: out.add(int(mm))
    for r, m in WOORD:
        if re.search(r, low): out.add(m)
    return out
def _is_klok(it): return 'klok' in (it.get('opgave') or '').lower()
_CACHE = {}
def somtype_minuten(items):
    k = id(items[0]) if items else None, len(items)
    if k not in _CACHE:
        s = set()
        for it in items:
            if _is_klok(it): s |= _minuten(f"{it.get('opgave') or ''} {it.get('antwoord') or ''}")
        _CACHE[k] = s
    return _CACHE[k]
_INFO = []
def pop_info():
    global _INFO
    x, _INFO = _INFO, []; return x
ZIN = re.compile(r'(?<=[.!?])\s+')
VOORWAARDE = re.compile(r"\bhoor je\b[^.?!]*'half'[^.?!]*'voor'|\bhoor je\b[^.?!]*'voor'[^.?!]*'half'", re.I)
ZONDER_HALF = re.compile(r'\b(?:vijf|tien|kwart) over\b(?! half)', re.I)
MET_HALF = re.compile(r'\bhalf\b|\bvoor\b', re.I)
OVER_HALF = {35, 40}
VIJFTIEN_OVER = re.compile(r'\b(?:vijf|tien) over\b(?! half)', re.I)
def _voorwaarde_ervoor(zinnen, i):
    if i >= 1 and VOORWAARDE.search(zinnen[i - 1]): return True
    return i >= 2 and zinnen[i - 1].lstrip().lower().startswith('dan ') and bool(VOORWAARDE.search(zinnen[i - 2]))
def _tekst(txt, wie, mins, warns, info, eigen=None, ouder=False):
    if not txt: return
    groepen = {groep(m) for m in mins}
    hv = sorted(groepen & MET_HALF_VOOR)
    zinnen = ZIN.split(txt.strip())
    for i, z in enumerate(zinnen):
        if not NV.search(z): continue
        if not hv: info.append(f"{wie}: 'net voorbij' bij alleen tijden '{', '.join(sorted(groepen))}' (#113, mag)"); continue
        if z.lstrip().lower().startswith('anders') and _voorwaarde_ervoor(zinnen, i):
            info.append(f"{wie}: 'net voorbij' na 'Anders' achter de voorwaarde 'half'/'voor' (#113, mag)"); continue
        if ZONDER_HALF.search(z) and not MET_HALF.search(ZONDER_HALF.sub('', z)):
            ref = eigen if eigen is not None else mins          # #120-1: het item zelf (fout-hint) of het somtype (hint)
            if VIJFTIEN_OVER.search(z) and ref & OVER_HALF:
                warns.append(f"{wie}: 'net voorbij' in een zin over '{VIJFTIEN_OVER.search(z).group(0)}', terwijl {'het item' if eigen is not None else 'het somtype'} '{', '.join(NAAM[m] for m in sorted(ref & OVER_HALF))}' heeft (#120-1)"); continue
            info.append(f"{wie}: 'net voorbij' in een zin over '{ZONDER_HALF.search(z).group(0)}' (#113, mag)"); continue
        if eigen is not None and eigen and all(m in (5, 10, 15) for m in eigen):
            info.append(f"{wie}: 'net voorbij' bij een item op '{', '.join(NAAM[m] for m in sorted(eigen))}' (#113, mag)"); continue
        warns.append(f"{wie}: 'net voorbij' in een somtype met ook tijden '{', '.join(hv)}' (#113-1)")
    for m in OPSOM.finditer(txt):
        genoemd = {x.lower().replace('het ', '').replace('een ', '').replace('heel uur', 'hele uur') for x in re.findall(T, m.group(0), re.I)}
        genoemd = {('heel uur' if g == 'hele uur' else g) for g in genoemd}
        mist = sorted({NAAM[x] for x in mins if x in NAAM} - genoemd)
        if not mist: continue
        msg = f"{wie}: opsomming '{m.group(0).strip()}' mist '{', '.join(mist)}' uit het somtype"
        open_ = bool(m.group(3)) and ouder                 # #120-2: '…' telt alleen in de Ouderzin
        (info if open_ else warns).append(msg + (" (eindigt op '…' in de Ouderzin, #113)" if open_ else " (eindigt op '…', maar niet in de Ouderzin, #120-2)" if m.group(3) else " (#113-2)"))
def _alg(it):
    a = it.get('algemeneFoutHint') or ''
    return (a.get('uitleg') or a.get('tekst') or '') if isinstance(a, dict) else a
def check113(it, t, fh, items=None):
    items = items if items is not None else [it]
    if not _is_klok(it): return []
    mins = somtype_minuten(items)
    if not mins: return []
    warns = []
    eigen = _minuten(f"{it.get('opgave') or ''} {it.get('antwoord') or ''}")
    for f in fh: _tekst(f.get('uitleg') or '', f"{t} [fout {f.get('fout')}]", mins, warns, _INFO, eigen)
    _tekst(_alg(it), f"{t} [algemeneFoutHint]", mins, warns, _INFO, eigen)
    return warns
def check113_somtype(tag, s, items):
    if not any(_is_klok(i) for i in items): return [], []
    mins = somtype_minuten(items)
    warns, info = [], []
    if mins:
        for lab, k in (('Hint 1', 'h1'), ('Hint 2', 'h2'), ('Ouderzin', 'ouder')): _tekst(s.get(k) or '', f"{tag} [{lab}]", mins, warns, info, ouder=(k == 'ouder'))
    return warns, info
