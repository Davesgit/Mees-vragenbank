#!/usr/bin/env python3
"""G5-fixlijst #21/#49 (FX21) voor G6/G7 (opdracht Dave 17:17): 'trainer'/'shirt' → 'kind'/'trui' in ALLE kindvelden én extraVelden
(claudeUitleg, claudeKaleSom, claudeFoutHints …), foutHintsTekst en optiesTekst: die kunnen zichtbaar worden. Zelfde patronen als
g5/scripts/fixlijst_g5.py (ENGELS, zonder de G5-itemregels). Schrijft zelf niets; aanroepen vóór de somtype-indeling."""
import re, json
ENGELS = [
    (r'kost een shirt (€\d+,\d\d)\b', r'kost een muts \1'), (r'\b(drie|twee|vier) shirts van €', r'\1 mutsen van €'),
    (r'\bshirts\b', 'truien'), (r'\bShirts\b', 'Truien'), (r'\bshirt\b', 'trui'), (r'\bShirt\b', 'Trui'),
    (r'Élke trainer\b', 'Élk kind'),
    (r'\b[Ee]lke trainer\b', lambda m: 'Elk kind' if m.group(0)[0] == 'E' else 'elk kind'),
    (r'\bDe trainers\b', 'De kinderen'), (r'\bde trainers\b', 'de kinderen'), (r'\bEen trainer\b', 'Een kind'), (r'\been trainer\b', 'een kind'),
    (r'\btrainers\b', 'kinderen'), (r'\btrainer\b', 'kind'), (r'\bTrainers\b', 'Kinderen'), (r'\bTrainer\b', 'Kind'),
]
def engels_weg(t):
    if not isinstance(t, str) or not t: return t
    for pat, rep in ENGELS: t = re.sub(pat, rep, t)
    return t
def _diep(v):
    if isinstance(v, str): return engels_weg(v)
    if isinstance(v, list): return [_diep(x) for x in v]
    if isinstance(v, dict): return {k: _diep(x) for k, x in v.items()}
    return v
VELDEN = ('opgave', 'opgaveStappen', 'hint', 'sterkereHint', 'algemeneFoutHint', 'foutHints', 'foutRegels', 'opties', 'optiesTekst',
          'foutHintsTekst', 'antwoordDetail', 'extraVelden', 'ouderzin')
def pas_toe(it, slog, label):
    n_ = 0
    for k in VELDEN:
        if k in it and it[k] is not None:
            n = _diep(it[k])
            if n != it[k]:
                slog(it, label, k, json.dumps(it[k], ensure_ascii=False)[:200], json.dumps(n, ensure_ascii=False)[:200]); it[k] = n; n_ += 1
    return n_
