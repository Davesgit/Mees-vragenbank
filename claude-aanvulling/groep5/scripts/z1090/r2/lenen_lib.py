"""Ronde 2 Z-#1090 (Oefeningen 15 okt 16:40): gedeelde regels voor lenen/onthouden per item (los van de motor uitgerekend)."""
import re
LEEN = re.compile(r'(gaat er (nog )?een tiental af|wordt het tiental één minder|[Hh]eb je (daar )?geleend|leen je)', re.I)      # uitleg 'lenen' (aftrekken)
ONTH_T0 = re.compile(r'over een heel tiental heen\W+(dan )?komt er een tiental bij', re.I)
ONTH_T = re.compile(r'tientallen die je onthoudt|onthouden tiental|eenheden (zijn |komen )?samen (op )?tien of meer|als ze samen (10|tien) of meer zijn, komt er een tiental bij|over een heel tiental heen\W+(dan )?komt er een tiental bij', re.I)
ONTH_H = re.compile(r'tientallen (zijn |komen )?samen (op )?tien of meer', re.I)
def getallen(opg):
    opg = re.sub(r'\(Typ [^)]*\)', '', opg or '')
    return [int(x.replace('.', '')) for x in re.findall(r'(?<![\d,])\d{1,3}(?:\.\d{3})+(?!\d|,\d)|(?<![\d,])\d+(?!\d|,\d)', opg)]
def ant(x):
    m = re.match(r'\s*(\d+)', str(x['antwoord'])); return int(m.group(1)) if m else None
def som(x):
    """('-', a, b) als a − b = antwoord; ('+', [termen]) als de getallen samen het antwoord zijn; anders None"""
    n, A = getallen(x.get('opgave')), ant(x)
    if A is None or len(n) < 2: return None
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j and n[i] - n[j] == A and ('−' in x['opgave'] or '-' in x['opgave'] or re.search(r'weg|af|verkocht|over|minder|naar huis|verschil', x['opgave'], re.I)): return ('-', n[i], n[j])
    if sum(n) == A: return ('+', n)
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == A: return ('+', [n[i], n[j]])
    return None
def leent(x, k=10):
    s = som(x); return None if not s or s[0] != '-' else (s[1] % k) < (s[2] % k)
def onthoudt(x, k=10):
    s = som(x); return None if not s or s[0] != '+' else sum(t % k for t in s[1]) >= k

SOORTEN = (('leen', LEEN, lambda x: leent(x, 10), 'fout = antwoord + 10', ' (geleend bij de tientallen)', ' (geleend)', 'Haal de tientallen nog eens af.'),
           ('onthT', ONTH_T, lambda x: onthoudt(x, 10), 'fout = antwoord − 10', ' (onthouden naar de tientallen)', ' (onthouden)', 'Tel de tientallen nog eens bij elkaar.'),
           ('onthH', ONTH_H, lambda x: onthoudt(x, 100), 'fout = antwoord − 100', ' (onthouden naar de honderdtallen)', ' (onthouden)', 'Tel de honderdtallen nog eens bij elkaar.'))
WEG = {'leen': [r'Ga je bij de eenheden over een heel tiental heen\? Dan gaat er nog een tiental af\.', r'Bij de eenheden ga je over een heel tiental heen: dan gaat er nog een tiental af\.',
                 r'Ga je bij de eenheden over een heel tiental heen, dan wordt het tiental één minder\.'],
       'onthT': [r'Zijn de eenheden samen tien of meer\? Dan (komt er een tiental|komen er tientallen) bij\.', r'De eenheden zijn samen tien of meer: dan komt er een tiental bij\.',
                 r'Ga je bij de eenheden over een heel tiental heen\? Dan komt er een tiental bij\.', r'Tel de eenheden nog eens: als ze samen (?:10|tien) of meer zijn, komt er een tiental bij\.'],
       'onthH': [r'De tientallen komen samen op tien of meer: dan komt er een honderdtal bij\.', r'Komen de tientallen samen op tien of meer\? Dan komt er een honderdtal bij\.(?: Vergeet dat niet\.)?']}
def zonder(t, naam):
    """t zonder de uitlegzin van lenen/onthouden; None als de zin geen bekende vorm heeft"""
    u = t
    for w in WEG[naam]: u = re.sub(r'\s*' + w, '', u)
    u = re.sub(r'\s+', ' ', u).strip()
    return None if dict((n, rx) for n, rx, *_ in SOORTEN)[naam].search(u) else u
