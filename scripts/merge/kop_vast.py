"""Oef-#1001 (G8 batch 6): staat op een [ding]-plek van een kop in elk item van dat somtype hetzelfde woord (hectare, milliliter), dan hoort dat woord
vast in de kop. vast_woorden(items) → {(doel, kop): nieuwe kop}; alleen somtypes met minstens 2 items (bij één item is elke plek 'altijd hetzelfde')."""
import re, collections
def _pat(kop):
    kale = re.sub(r'^\[[^\]]+\]\s*', '', kop).replace(' ⏎ ', ' ')
    delen = re.split(r'(\[\w+\]|#)', kale); rx = ''; plekken = []
    for d in delen:
        if d == '#': rx += r'[\d.,]+'
        elif re.fullmatch(r'\[\w+\]', d): rx += '(.+?)'; plekken.append(d)
        else: rx += re.escape(d)
    return re.compile(rx), plekken
def vast_woorden(items, min_items=2):
    G = collections.defaultdict(list)
    for it in items: G[(it['merge'].get('doel'), it['merge'].get('somtype') or '')].append(it)
    uit = {}
    for (doel, kop), its in G.items():
        if '[ding]' not in kop or len(its) < min_items: continue
        rx, plekken = _pat(kop); ms = [rx.fullmatch(re.sub(r'\s+', ' ', it['opgave']).strip()) for it in its]
        if not all(ms): continue
        nieuw = kop; di = -1
        for i, pl in enumerate(plekken):
            if pl != '[ding]': continue
            di += 1; w = {m.group(i + 1) for m in ms}
            if len(w) == 1 and re.fullmatch(r'[^\W\d_]+', next(iter(w))):
                # vervang de di-de '[ding]' (die er nog staat) in de kop
                idx = [m.start() for m in re.finditer(r'\[ding\]', kop)][di]; vervang = next(iter(w))
                nieuw = nieuw[:idx + (len(nieuw) - len(kop))] + vervang + nieuw[idx + (len(nieuw) - len(kop)) + 6:]
        if nieuw != kop: uit[(doel, kop)] = nieuw
    return uit
