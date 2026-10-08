#!/usr/bin/env python3
"""Gedeelde haak voor de merge-checkers G3–G8 (G5 fixlijst #63, Didactiek review batch 4, 1 okt 2026).
Bestaat /workspace/claude-merge/referentiematen.json, dan worden de kindteksten van elk item (opgave, antwoord, opties, hints, fout-hints)
erlangs gelegd: een referentiemaat met een getal + eenheid buiten het bereik in het bestand = WARN (geen FAIL). Bestaat het bestand niet,
dan doet de haak niets (en zegt dat één keer).
Formaat (Didactiek, referentiematen.json van 17:44): een lijst met per maat o.a. id, maat, kindzin, nietGebruiken, en
  checkPatronen (regex: een foute referentie → WARN REF) en checkPatronenZacht (regex: twijfelachtig → WARN REF-zacht), regexVlaggen ('iu').
  (Een oud voorstel-formaat {"maten": [{woorden, eenheid, min, max}]} werkt ook nog.)
Gebruik: from referentiematen_check import controleer; warns = controleer(items)  →  lijst met tekstregels."""
import json, os, re
PAD = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'referentiematen.json')

def _teksten(it):
    ex = it.get('extraVelden') or {}
    t = [it.get('opgave') or '', str(it.get('antwoord') or ''), it.get('hint') or '', it.get('sterkereHint') or '', it.get('ouderzin') or '',
         it.get('algemeneFoutHint') or '', ex.get('claudeUitleg') or '', ex.get('claudeStrategie') or '']
    t += [o.get('tekst') or '' for o in it.get('opties') or []] + [f.get('uitleg') or '' for f in it.get('foutHints') or []]
    return ' · '.join(str(x).replace('\n', ' ') for x in t)

def _getal(s): return float(s.replace('.', '').replace(',', '.')) if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', s) else float(s.replace(',', '.'))

def _vlag(v): return (re.I if 'i' in (v or '') else 0)

def laad(pad=PAD):
    """None als het bestand er niet is; anders lijst (soort, id, patroon, beschrijving) of het oude min/max-formaat."""
    if not os.path.exists(pad): return None
    d = json.load(open(pad, encoding='utf-8'))
    if isinstance(d, dict): return [('bereik', m) for m in d.get('maten', [])]
    out = []
    for m in d:
        for soort, k in (('REF', 'checkPatronen'), ('REF-zacht', 'checkPatronenZacht')):
            for pt in m.get(k) or []:
                try: out.append(('patroon', (soort, m.get('id'), re.compile(pt, _vlag(m.get('regexVlaggen'))), m.get('kindzin'))))
                except re.error as e: out.append(('fout', (m.get('id'), pt, str(e))))
    return out

def controleer(items, pad=PAD):
    regels = laad(pad)
    if regels is None: return None          # geen bestand: haak staat klaar, niets te doen
    warns = [f"REF-onleesbaar {r[0]}: patroon «{r[1][:60]}» ({r[2]})" for s, r in regels if s == 'fout']
    for it in items:
        txt = _teksten(it)
        for s, r in regels:
            if s == 'patroon':
                soort, rid, pat, kz = r
                if (m := pat.search(txt)): warns.append(f"{soort} {it.get('id')} [{rid}]: «{m.group(0)[:70]}» (goed: {(kz or '')[:70]})")
            elif s == 'bereik':
                for w in r.get('woorden') or [r['wat']]:
                    if not re.search(rf'\b{re.escape(w)}\b', txt, re.I): continue
                    for g in re.finditer(rf'(\d+(?:[.,]\d+)?)\s?{re.escape(r["eenheid"])}\b', txt):
                        v = _getal(g.group(1))
                        if not (r.get('min', float('-inf')) <= v <= r.get('max', float('inf'))):
                            warns.append(f"REF {it.get('id')}: '{w}' met {g.group(0)} (referentie {r.get('min')}–{r.get('max')} {r['eenheid']})")
                    break
    return warns

# G6 Z-#511 (Didactiek slotcheck r10 deel B): hoeveelheid bij emmer, glas en bad omgerekend naar liter; WARN buiten de bandbreedte.
# Bandbreedte uit referentiematen.json (veld 'bandLiter': [min, max] bij inhoud-emmer/-glas/-bad) of anders deze standaard.
BAND511 = {'emmer': ('inhoud-emmer', 5, 15), 'glas': ('inhoud-glas', 0.15, 0.3), 'bad': ('inhoud-bad', 100, 200)}
LITER511 = {'l': 1, 'liter': 1, 'dl': 0.1, 'deciliter': 0.1, 'cl': 0.01, 'centiliter': 0.01, 'ml': 0.001, 'milliliter': 0.001}
def inhoud511(items, pad=PAD):
    band = {}
    try: R = json.load(open(pad, encoding='utf-8'))
    except Exception: R = []
    rid = {r.get('id'): r for r in R if isinstance(r, dict)} if isinstance(R, list) else {}
    for w, (i, lo, hi) in BAND511.items():
        b = (rid.get(i) or {}).get('bandLiter'); band[w] = (b[0], b[1]) if isinstance(b, list) and len(b) == 2 else (lo, hi)
    warns = []
    for it in items:
        for zin in re.split(r'(?<=[.?!])\s+|\n', it.get('opgave') or ''):
            ws = [(m.start(), m.group(1).lower()) for m in re.finditer(r'\b(emmer|glas|bad)\b', zin, re.I)]
            qs = [(m.start(), _getal(m.group(1)) * LITER511[m.group(2).lower()], m.group(0)) for m in re.finditer(r'(\d+(?:[.,]\d+)?)\s?(L|liter|dl|deciliter|cl|centiliter|ml|milliliter)\b', zin, re.I)]
            for pos, w in ws:
                if not qs: continue
                _, liter, t = min(qs, key=lambda q: abs(q[0] - pos)); lo, hi = band[w]
                if not (lo <= liter <= hi): warns.append(f"REF-inhoud {it.get('id')}: '{w}' met {t} = {liter:g} L (referentie {lo:g}–{hi:g} L)")
    return warns

def rapport(items, pad=PAD, max_regels=30):
    """Print het REF-blok voor een checker. checkPatronen = FAIL, checkPatronenZacht = WARN (besluit 1 okt 17:50).
    Geeft het aantal FAIL terug (de checker zet daarmee zijn eindoordeel)."""
    w = controleer(items, pad)
    if w is None:
        print(f"\nREF (referentiematen, #63): {os.path.basename(pad)} bestaat niet → overgeslagen (haak staat klaar)"); return 0
    w = w + inhoud511(items, pad)
    hard = [x for x in w if x.startswith('REF ')]; zacht = [x for x in w if x.startswith(('REF-zacht', 'REF-inhoud'))]; rest = [x for x in w if x not in hard and x not in zacht]
    print(f"\nREF (referentiematen.json, #63): {len(hard)} FAIL (checkPatronen) · {len(zacht)} WARN (checkPatronenZacht + inhoud emmer/glas/bad #511) · {len(rest)} onleesbaar patroon (WARN)")
    for x in hard[:max_regels]: print('  FAIL', x)
    for x in (zacht + rest)[:max_regels]: print('  WARN', x)
    return len(hard)

def banken(groepen=(3, 4, 5, 6, 7, 8), pad=PAD):
    """Alleen-lezen rapport over de canonieke banken (/workspace/rekenen-groepN/bank/*.md): per regel van het bestand. Schrijft niets."""
    import glob
    regels = laad(pad) or []; n = 0
    for g in groepen:
        for f in sorted(glob.glob(f'/workspace/rekenen-groep{g}/bank/*.md')):
            for i, regel in enumerate(open(f, encoding='utf-8'), 1):
                for s, r in regels:
                    if s == 'patroon' and (m := r[2].search(regel)):
                        n += 1; print(f"  {'FAIL' if r[0] == 'REF' else 'WARN'} G{g} {os.path.basename(f)}:{i} [{r[1]}] «{m.group(0)[:70]}»")
    print(f'canonieke banken (alleen lezen): {n} treffers')

if __name__ == '__main__':
    import sys
    if '--banken' in sys.argv: banken()
