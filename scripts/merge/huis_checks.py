#!/usr/bin/env python3
"""Gedeelde extra checks voor check_hints.py (G5–G8), eindcheck G6 r11 van Didactiek (8 okt 2026).
- KEERDELEN (#540, les 138): een kindtekst met 'verhoudingstabel' en 'met keer en delen' of 'doe je keer' in één zin = FAIL. In een verhoudingstabel
  mag je ook kolommen optellen (les 62, #272). Over alle somtypes: de hint-entries (hints/batch*.json) én de items (data/gemapt.json).
- LETT (#543): vaste testtabel voor de letterlijke regels (fout_regels.lett_past en lett_guard; LETT_VOOR/LETT_NA, #380/#411/#506). Wijkt de motor af
  van de tabel, dan FAIL (check_hints) en stopt de build (assert_lett, aangeroepen vanuit fout_regels bij het laden)."""
import json, glob, os, re
# #551 (eindcheck r11b, les 158): ook omschrijvingen ('vermenigvuldigen en delen', 'keer en gedeeld door', 'keer- en deelsommen', 'keer of delen')
# en de bewering verdeeld over twee zinnen ('verhoudingstabel' in de ene zin, de bewering in dezelfde of de volgende zin).
_KD = re.compile(r'met keer en delen|doe je keer|keer\s*(?:en|of)\s*(?:delen|deel|gedeeld door)|vermenigvuldig\w*\s+(?:en|of)\s+(?:delen|deel)|keer-\s*(?:en|of)\s*deel(?:sommen)?|keersommen\s+(?:en|of)\s+deelsommen', re.I)
def _zinnen(t): return [z for z in re.split(r'(?<=[.?!])\s+', t or '') if z]
def _kd(t):
    zs = _zinnen(t); uit = []
    for i, z in enumerate(zs):
        if 'verhoudingstabel' not in z.lower(): continue
        for w in zs[i:i + 2]:
            if _KD.search(w): uit.append(z if w is z else f'{z} {w}'); break
    return uit
def keerdelen(base):
    uit = []
    for p in sorted(glob.glob(f'{base}/hints/batch*.json')):
        for e in json.load(open(p)).get('somtypen', []):
            ts = [e.get('hint1'), e.get('hint2'), e.get('ouderzin'), e.get('algemeneFoutHint')] + [x for f in e.get('foutHints', []) for x in (f.get('tekst'), f.get('tekstSterker'))]
            for z in (z for t in ts for z in _kd(t)): uit.append(f"KEERDELEN (#540) {os.path.basename(p)} {e.get('doel')} #{e.get('nrOrigineel')}: «{z}»")
    g = f'{base}/data/gemapt.json'
    if os.path.exists(g):
        gezien = set()
        for it in json.load(open(g))['items']:
            ts = [it.get('hint'), it.get('sterkereHint'), it.get('ouderzin'), it.get('algemeneFoutHint')] + [x for f in it.get('foutHints') or [] for x in (f.get('uitleg'), f.get('uitlegSterker'))]
            for z in (z for t in ts for z in _kd(t)):
                k = (it['merge'].get('doel'), it['merge'].get('somtypeNrOrigineel'), z)
                if k not in gezien: gezien.add(k); uit.append(f"KEERDELEN (#540) item {it['id']} ({k[0]} #{k[1]}): «{z}»")
    return uit
# #543: (regel, optietekst, verwacht). 37 gevallen: de 37 van de eindcheck G6 r11 (#506) plus de randgevallen uit de eindcheck G5 r11.
LETT_TABEL = [
    ('4 hokjes', '4 hokjes', True), ('4 hokjes', 'ruim 4 hokjes', True), ('3 hokjes', '(3 hokjes)', True), ('4 hokjes', '14 hokjes of 4 hokjes', True),
    ('4 hokjes', '14 hokjes', False), ('4 hokjes', '44 hokjes', False), ('4 hokjes', '4,5 hokjes', False), ('4 hokjes', '0,4 hokjes', False),
    ('4 hokjes', '1.4 hokjes', False), ('4 hokjes', '€4 hokjes', False), ('4 hokjes', '1/4 hokjes', False), ('4 hokjes', '−4 hokjes', False),
    ('4 hokjes', '-4 hokjes', False), ('4 hokjes', '– 4 hokjes', False), ('4 hokjes', '− 4 hokjes', False), ('4 hokjes', '-  4 hokjes', False),
    ('4 hokjes', '- 4 hokjes', False), ('4 hokjes', '8 − 4 hokjes', False), ('4 hokjes', '24 − 4 hokjes', False), ('4', '4/5', False),
    ('4', '14', False), ('4', '44', False), ('4', '4,5', False), ('4', '0,4', False), ('4', '1.4', False), ('4', '−4', False),
    ('1/4', '1/4', True), ('3/4', '3/4 deel', True), ('10.000', '10.000', True), ('a4', 'a4', True),
    ('2 cm', '2 cm²', False), ('2 cm', '2 cm', True),
    ('€3', '€3', True), ('€3', '€3,50', False), ('€3', '3', False),
    ('het smalle glas', 'het smalle glas', True), ('het smalle glas', 'het brede glas', False),
]
def lett_afwijkingen(FR):
    uit = []
    if getattr(FR, 'LETT_TABEL_543', None) is not None and list(FR.LETT_TABEL_543) != LETT_TABEL:      # #552: de tabel in de motor is dezelfde
        uit.append('LETT (#552) de testtabel in fout_regels.py (LETT_TABEL_543) wijkt af van tools/huis_checks.LETT_TABEL')
    for r, v, verwacht in LETT_TABEL:
        a, b = FR.lett_past(r.lower(), v), FR.lett_guard(r, v)
        if a != verwacht or b != verwacht: uit.append(f"LETT (#543) regel {r!r} op {v!r}: verwacht {'past' if verwacht else 'past niet'}, lett_past={a}, lett_guard={b}")
    return uit
def motor_map(base):
    """Didactiek 19:57: zoekvolgorde voor de motor. Eerst <groep>/scripts (claude-merge, G3–G6 in de repo); anders de repo-motor
    scripts/fout_regels.py twee mappen hoger (claude-aanvulling/groep7 → scripts/, G7 heeft geen eigen kopie). Geen motorkopie."""
    for d in (os.path.join(base, 'scripts'), os.path.join(base, '..', '..', 'scripts')):
        if os.path.isfile(os.path.join(d, 'fout_regels.py')): return os.path.abspath(d)
    raise FileNotFoundError(f'fout_regels.py niet gevonden in {base}/scripts of in de repo-map scripts/')
def extra_fails(base):
    import sys
    sys.path.insert(0, motor_map(base)); import fout_regels as FR
    return keerdelen(base) + lett_afwijkingen(FR)
# ONLEESBAAR (opdracht 12:15): een regel die de motor bij geen enkel item van zijn somtype kan lezen (logs/regels_onleesbaar.json, geschreven door
# apply_hints) = WARN. Zo'n regel geeft nooit een sleutel; de foute opties vallen dan stil op 'andere fout' (zoals '6 liter' na V-#516 in G7).
def onleesbaar(base):
    p = f'{base}/logs/regels_onleesbaar.json'
    if not os.path.exists(p): return []
    return [f"ONLEESBAAR {x['doel']} #{x['nrOrigineel']}: regel '{x['regel']}' is bij geen van de {x['items']} items te lezen (geeft nooit een sleutel)"
            for x in json.load(open(p))['regels'] if x['items'] and x['itemsNietTeLezen'] >= x['items']]
def extra_warns(base): return onleesbaar(base)
