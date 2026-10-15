"""Z-#1091 (Didactiek; incl. Oef-#1050, V-#1052): G5-teksten die het verschil als bedrag noemen → richting + waar kijken, geen bedrag.
Gedeeld door zet_z1091.py / check_z1091.py; per somtype een eigen map met snap en verwacht."""
import re
SCOPE = ('G5-GET-E02', 'G5-GET-E05', 'G5-GET-E07', 'G5-GET-M04', 'G5-GET-M05', 'G5-GET-M06', 'G5-MEET-E02', 'G5-MKU-E02', 'G5-VBN-E03', 'G5-MEET-E06', 'G5-MEET-E03', 'G5-VBN-E01', 'G5-VERH-E01')      # Oef-#1058 + les 450-scan      # Oef-#1055 (Didactiek 17:10b): klok, hokje, VBN-E03-foutreacties
# guard: bedrag + richtingwoord ('één te veel', 'één honderdtal te weinig', 'twee te veel', 'honderd te veel', 'één stap te ver', 'één ronde te ver', …)
BEDRAG = re.compile(r"\b(?:één|een|twee|drie|tien|honderd|duizend)(?: (?:hele )?(?:honderdtal|tiental|stap|stapje|ronde|bus|hokje|uur)(?: van \w+)?)? (?:te (?:veel|weinig|ver|vroeg|laat)|in de tafel)\b|\b[Ee]én stap (?:hoger|lager|verder)\b|\b[Hh]eb je er één dubbel\b|\bis er nog één nodig\b|\been uur te (?:ver|vroeg|laat)\b|\b(?:één|een) dag te (?:ver|kort|veel|weinig)\b|\bnog \S+ (?:\S+ )?(?:rij|stap|stappen) verder\b|\bGa na plek \d+\b|\bnog een (?:tafel|ronde) (?:meer|bij)\b|\b(?:één|een) (?:bus|stap|ronde|hokje)(?: van \d+)? te\b|\bje hebt er (?:één|een|twee) te\b|\b(?:één|een) (?:groepje|streepje|koekje|tafel|tiental|plek|getal)(?: te)? (?:veel|weinig|hoog|laag|ver|verder)\b|\bzestig minuten te (?:veel|weinig)\b|\b(?:lange|korte) (?:zijde|kant) te veel\b|\bwijzer (?:één|een) (?:streepje|getal) (?:verder|minder ver)\b", re.I)
# V-#1052: alleen deze per-item zin in VBN-E03 #1; de rest van VBN-E03 is een eigen datapunt (Oef-#1055)
V1052 = ('Dat is één ronde te ver.', 'Dat is te ver. Tel de rondes nog eens.')
# Oef-#1055: VBN-E03 per-item foutreacties (soort 'één stap ernaast (per item)'); de algemene werkwijze-hint #2 hint2 blijft (geen bedrag)
VBN = [V1052, ('Er komt nog een ronde bij.', 'Dat is niet ver genoeg. Tel de rondes nog eens.'),
       ('Je hebt één stap van 2 te ver gezet.', 'Je bent te ver gegaan.'), ('Je hebt één stap te ver gezet.', 'Je bent te ver gegaan.'),
       ('Je hebt een stap te ver gezet.', 'Je bent te ver gegaan.'), ('Je bent één stap te ver gegaan.', 'Je bent te ver gegaan.'),
       ('Je bent één bus te vroeg gestopt.', 'Je bent te vroeg gestopt.'), ('Ga daarna nog één rij verder.', 'Je bent te vroeg gestopt. Tel de rijen nog eens.'),
       ('Ga daarna nog één stap verder.', 'Je bent te vroeg gestopt. Tel de stappen nog eens.'), ('Er staat nog een tafel meer.', 'Je bent te vroeg gestopt. Tel de tafels nog eens.')]
VBN_RE = [(r'Ga na plek (\d+) nog (?:één|een|twee|drie) stappen? verder\.', r'Tel de stappen na plek \1 nog eens.'), (r'Je bent (?:één|een) plek te ver gegaan\.', 'Je bent te ver gegaan.')]      # VBN-E03 #2 007 (foutreactie)
REGELS = [   # (patroon, vervanging); volgorde telt
 (r'^Bijna! ', ''),                                                           # 'Bijna!' zegt: het scheelt maar een beetje (bedrag)
 (r'\bDat is er (?:één|een|twee) te (veel|weinig)\.', r'Dat zijn er te \1.'),
 (r'\bDat is (?:één|een|twee|tien|honderd)(?: (?:honderdtal|tiental|stapje van tien))? te (veel|weinig|ver)\.', r'Dat is te \1.'),   # Oef-#1050: 'één honderdtal te veel'
 (r'\bmaar (?:één|een) (?:honderdtal|tiental) te ver\.', 'maar te ver.'),
 (r'\bDat is (?:één|een) stap te ver in de tafel\.', 'Je bent te ver gegaan in de tafel.'),
 (r'\bDat is (?:één|een) stap te weinig in de tafel\.', 'Je bent niet ver genoeg gegaan in de tafel.'),
 (r'\bDan zit er in elk groepje (?:één|een) te (veel|weinig)\.', r'Dan zitten er in elk groepje te \1.'),
 (r'\b[Ee]én stap hoger in de tafel kom je boven het totaal uit\.', 'Met jouw antwoord kom je in de tafel boven het totaal uit.'),
 (r'\bJe bent (?:één|een) dag te ver teruggeteld\.', 'Je bent te ver teruggeteld.'),      # Oef-#1057 (Didactiek 17:20), alleen #7 (terugtellen)
 (r'\bJe bent (?:één|een) dag te kort teruggeteld\.', 'Je bent niet ver genoeg teruggeteld. Tel de dagen nog eens.'),
 (r'\bJe bent (?:één|een) dag te ver geteld\.', 'Je bent te ver geteld.'),      # Oef-#1058 (Didactiek 17:28): #6 vooruit tellen
 (r'\bJe bent (?:één|een) dag te kort geteld\.', 'Je bent niet ver genoeg geteld.'),
 (r'\bDat is (?:één|een) dag te (veel|weinig)\.', r'Dat is te \1. Tel de dagen nog eens.'),
 (r'\bDat is (?:één|een) groepje te (veel|weinig)\.', r'Dat zijn er te \1. Lees nog eens hoeveel groepjes het zijn.'),
 (r'\bDat is (?:één|een) streepje te (veel|weinig)\.', r'Dat is te \1. Tel de streepjes nog eens.'),
 (r'\bDat is (?:één|een) koekje te (veel|weinig)\.', r'Dat is te \1. Tel de koekjes nog eens.'),
 (r'\bDat is (?:één|een) tafel te weinig\.', 'Dat is te weinig. Tel de tafels nog eens.'),
 (r'\bJe zit (?:één|een) tiental te (hoog|laag)\.', lambda m: f"Dat is te {'veel' if m.group(1)=='hoog' else 'weinig'}. Kijk goed naar de tientallen."),
 (r'\bJe hebt een (lange|korte) (zijde|kant) te veel geteld\.', r'Je hebt een \1 \2 dubbel geteld. Tel de \2n nog eens.'),
 (r'\bJe bent (?:één|een) plek te ver gegaan\.', 'Je bent te ver gegaan.'),
 (r'\bDat is zestig minuten te (veel|weinig): een heel uur\.', r'Dat is te \1. Kijk naar de hele uren.'),
 (r'\bBij die tijd staat de grote wijzer (?:één|een) streepje verder\.', 'Bij die tijd staat de grote wijzer verder.'),
 (r'\bBij die tijd staat de grote wijzer (?:één|een) streepje minder ver\.', 'Bij die tijd staat de grote wijzer minder ver.'),
 (r'\bBij die tijd staat de grote wijzer (?:één|een) getal verder\.', 'Bij die tijd staat de grote wijzer verder.'),
 (r'\bBij die tijd staat de grote wijzer (?:één|een) getal minder ver\.', 'Bij die tijd staat de grote wijzer minder ver.'),
 (r'\bstaat de grote wijzer (?:één|een) getal verder\.', 'staat de grote wijzer verder.'),      # Oef-#1058: #1
 (r'\bVoor wie overblijft, is er nog één nodig\.', 'Ook wie overblijft, moet mee.'),
 (r'\bHeb je er één dubbel geteld\?', 'Heb je iets dubbel geteld?'),
 (r'\bje hebt er (?:één|een) te (veel|weinig)\.', r'je hebt er te \1.'),
 (r'\bstaat de kleine wijzer een uur te (ver|vroeg)\.', r'staat de kleine wijzer te \1.'),      # Oef-#1055 klok: alleen de wijzer die echt fout is (check per item)
 (r'\bDat is een uur te (vroeg|laat)\b', r'Dat is te \1'),
 (r'\bDe kleine wijzer staat een uur te (ver|vroeg)\.', r'De kleine wijzer staat te \1.'),
 (r'\bJe hebt één hokje te veel gekleurd\.', 'Je hebt te veel hokjes gekleurd.'),
 (r'\bDan is er nog één nodig\.', 'Dan heb je er meer nodig.'),
]
# waar kijken: een bedrag met eenheid verdwijnt; staat de eenheid niet meer in de tekst, dan komt er een kijkzin bij
KIJK = {'honderdtal': 'Kijk goed naar de honderdtallen.', 'tiental': 'Kijk goed naar de tientallen.'}
def herschrijf(t, doel):
    if not isinstance(t, str): return t
    if doel == 'G5-VBN-E03':
        for a, b in VBN: t = t.replace(a, b)
        for a, b in VBN_RE: t = re.sub(a, b, t)
        return t
    u = t
    for a, b in REGELS:
        n = re.sub(a, b, u)
        if n != u:
            for e, z in KIJK.items():
                if re.search(rf'\b{e}\b', u) and not re.search(rf'\b{e}', n): n = n.rstrip() + ' ' + z
        u = n
    return u
HOOG = re.compile(r'\bte ver (?:terug)?geteld\b|\bte laat\b|\bte (veel|ver|groot|hoog)\b|\bkom je (?:in de tafel )?boven het totaal\b|\bdubbel\b')
LAAG = re.compile(r'\bniet ver genoeg (?:terug)?geteld\b|\bte vroeg\b|\bte (weinig|klein|laag)\b|\bniet ver genoeg\b|\bniet alle\b|\bdie je niet ziet\b|\bkom je onder het totaal\b|\bmoet mee\b')
def tijd(s):
    m = re.fullmatch(r'\s*(\d{1,2})[.:](\d{2})\s*uur\s*', str(s)); return (int(m.group(1)) % 12) * 60 + int(m.group(2)) if m else None
def getal(s):
    m = re.search(r'-?\d[\d.]*(?:,\d+)?', str(s)); 
    try: return float(m.group(0).replace('.', '').replace(',', '.')) if m else None
    except ValueError: return None
