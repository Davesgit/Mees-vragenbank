"""V-#1081 (Oefeningen 15 okt): fout aan de andere kant voor E04 #1, MEET-E03 #2, VERH-E02 #2 (kritisch concept L-R10b). Gedeelde rekenregels."""
import re
GETAL = r'\d+(?:\.\d{3})*'
def w(s): return int(re.search(GETAL, s).group(0).replace('.', ''))
def goed(x): return w(x['bewering']) if x['beweringKlopt'] else w(x['antwoord'])
def _lenen(a, b):
    """kolommen (0 = eenheden) waar geleend wordt bij a − b"""
    k, l, uit = 0, 0, []
    while a // 10 ** k or b // 10 ** k:
        t, o = (a // 10 ** k) % 10 - l, (b // 10 ** k) % 10
        l = 1 if t < o else 0
        if l: uit.append(k)
        k += 1
    return uit
def kandidaat(x):
    """(waarde, kant, denkfout, L1-tekst) of None"""
    T = goed(x); d = x['doelId']; s = x['somtypeNrOrigineel']
    if (d, s) == ('G6-GET-E04', 1):
        m = re.search(r'"(\d+) − (\d+) = ', x['opgave']); a, b = int(m.group(1)), int(m.group(2))
        L = _lenen(a, b)
        if a - b != T or not L: return None
        v = T - 10 ** (L[0] + 1)
        return (v, 'laag', 'bij het lenen twee keer afgehaald bij het cijfer waar je van leent',
                'Dat is te weinig. Kijk naar het cijfer waar je van leent: hoeveel gaat daar af? Reken na: jouw uitkomst plus het getal dat je eraf haalt, moet het getal zijn waar je vanaf haalt.')
    if (d, s) == ('G6-MEET-E03', 2):
        m = re.search(r'oppervlakte van (\d+) cm²\. Eén zijde is (\d+) cm', x['opgave']); A, z = int(m.group(1)), int(m.group(2))
        if A != T * z or T < 2: return None
        return (T - 1, 'laag', 'in de tafel van de bekende zijde één stap te vroeg gestopt',
                'Dat is te weinig. Tel nog eens in de tafel van de bekende zijde. Reken na: jouw zijde keer de bekende zijde moet precies de oppervlakte zijn.')
    if (d, s) == ('G6-VERH-E02', 2):
        m = re.search(r'"(\d+)/(\d+) van (\d+) koekjes', x['opgave']); n, q, a = map(int, m.groups())
        if a * n % q or a * n // q != T or n < 2: return None
        return (a * n, 'hoog', 'keer de teller gedaan en niet door de noemer gedeeld',
                'Dat is te veel: dat zijn meer koekjes dan er zijn. Verdeel de koekjes eerst in gelijke groepjes; de noemer zegt hoeveel groepjes.')
    return None
SCOPE = {('G6-GET-E04', 1), ('G6-MEET-E03', 2), ('G6-VERH-E02', 2)}
