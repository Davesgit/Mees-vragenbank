"""V-#902 (Didactiek G8 batch 5, 16:58): na '1' (ook '−1') komt het enkelvoud: '1 stap', '1 graad', niet '1 stappen' / '1 graden' (FAIL).
Kijkt in de kindteksten (opgave, antwoord, opties, hints, ouderzin, fout-hints, algemeneFoutHint, kop) en Claudes kindvelden (claudeUitleg, claudeKaleSom,
claudeHint*, claudeFoutHints uitleg). '1,5 meter', '21 graden' en '0,1 liter' tellen niet. Gebruik: import enkelvoud_check as EV1; EV1.rapport(items)."""
import re, sys
MV = {'stappen': 'stap', 'graden': 'graad', 'uren': 'uur', 'minuten': 'minuut', 'seconden': 'seconde', 'dagen': 'dag', 'weken': 'week', 'maanden': 'maand',
      'jaren': 'jaar', 'meters': 'meter', 'kilometers': 'kilometer', 'centimeters': 'centimeter', 'millimeters': 'millimeter', 'liters': 'liter', "kilo's": 'kilo',
      'blokjes': 'blokje', 'kinderen': 'kind', 'bekers': 'beker', 'flesjes': 'flesje', 'busjes': 'busje', 'kratten': 'krat', 'appels': 'appel', 'punten': 'punt',
      'hokjes': 'hokje', 'streepjes': 'streepje', 'vakjes': 'vakje', 'stukken': 'stuk', 'stukjes': 'stukje', 'filmpjes': 'filmpje', "foto's": 'foto',
      'lagen': 'laag', 'rijen': 'rij', 'tientallen': 'tiental', 'honderdtallen': 'honderdtal', 'duizendtallen': 'duizendtal', 'boeken': 'boek', 'mensen': 'mens'}
RX = re.compile(r"(?<![\d.,])([−-]?1) (" + '|'.join(re.escape(k) for k in sorted(MV, key=len, reverse=True)) + r")\b")
def teksten(it):
    yield 'kop', (it.get('merge') or {}).get('somtype')
    for k in ('opgave', 'antwoord', 'hint', 'sterkereHint', 'ouderzin', 'algemeneFoutHint', 'foutHintsTekst'): yield k, it.get(k)
    for o in it.get('opties') or []: yield 'optie', o.get('tekst') if isinstance(o, dict) else o
    for f in it.get('foutHints') or []:
        for k in ('uitleg', 'uitlegSterker'): yield 'foutHint', f.get(k)
    ex = it.get('extraVelden') or {}
    for k, v in ex.items():
        if k in ('claudeUitleg', 'claudeKaleSom') or k.startswith('claudeHint'): yield k, v
    for d in ex.get('claudeFoutHints') or []: yield 'claudeFoutHints', d.get('uitleg') if isinstance(d, dict) else None
def fouten_item(it):
    F = []
    for veld, t in teksten(it):
        if not isinstance(t, str): continue
        for m in RX.finditer(t):
            if veld == 'kop' and m.group(1).endswith('#'): continue
            F.append(f"[{veld}] «{m.group(0)}» → «{m.group(1)} {MV[m.group(2)]}»")
    return F
def rapport(items, toon=True, ernst='FAIL'):
    F = [f"{it['id']}: {'; '.join(f)}" for it in items if (f := fouten_item(it))]
    if toon:
        print(f"\nENKELVOUD (V-#902: na 1 het enkelvoud, '1 stap'/'1 graad'): {len(F)} ({ernst})")
        for x in F[:15]: print(f'  {ernst} ENKELVOUD', x)
    return len(F)
MUTANTEN = [('1 stappen', {'id': 'm', 'opgave': 'x', 'extraVelden': {'claudeUitleg': 'Ga 1 stappen naar rechts.'}}, True),
            ('1 stap', {'id': 'm', 'opgave': 'Ga 1 stap naar rechts.'}, False), ('1,5 meters', {'id': 'm', 'opgave': 'Het is 1,5 meters.'}, False),
            ('−1 graden', {'id': 'm', 'opgave': 'Het is −1 graden.'}, True), ('21 graden', {'id': 'm', 'opgave': 'Het is 21 graden.'}, False)]
if __name__ == '__main__' and '--mutanten' in sys.argv:
    ok = sum(bool(fouten_item(i)) == v for _, i, v in MUTANTEN); print(f'mutanten ENKELVOUD: {ok}/{len(MUTANTEN)}'); sys.exit(0 if ok == len(MUTANTEN) else 1)
