"""Les 250 / Oef-#484 (Didactiek G8 batch 1, V-#763-vervolg): een fout-hint met een ±1-tekst ('Dat is één … te veel/te weinig')
op een sleutel die een getal uit de vraag is (ook teller/noemer van een breuk). De motor weigert ±1 op een getal uit de vraag (#390),
dus de tekst beschrijft een route die het kind niet nam: zoek de benoemde route. WARN (in g8work/b1/check.py is het FAIL).
Gebruik: import les250_check as L250; n_warn = L250.rapport(items)."""
import re
PM1 = re.compile(r'(Dat is )?één \w+ te (veel|weinig)')
def treffers(items):
    W = []
    for it in items:
        getallen = set(re.findall(r'\d+', (it.get('opgave') or '').replace('.', '')))
        for fh in it.get('foutHints') or []:
            k = str(fh.get('fout') or '').replace('.', '').strip()
            if k.isdigit() and k in getallen and PM1.match(fh.get('uitleg') or ''):
                W.append(f"{it['id']} sleutel {fh.get('fout')}: ±1-tekst «{(fh.get('uitleg') or '')[:50]}» op een getal uit de vraag (#390)")
    return W
def rapport(items, toon=True):
    W = treffers(items)
    if toon:
        print(f"\nLES250 (Oef-#484: ±1-tekst op een sleutel die een getal uit de vraag is; de motor geeft daar nooit ±1): {len(W)} (WARN)")
        for x in W[:10]: print('  WARN LES250', x)
    return len(W)
