#!/usr/bin/env python3
"""Deelteken- en dubbelepuntregel G4–G8 (Didactiek/Overzicht 2026-09-30).
':' is in G4–G8 het deelteken, altijd kaal met een spatie aan beide kanten: 'a : b' (als operator ook ': 2', zoals '× 2').
Verboden (hele bestand, dus ook header/notitie):
  - '÷' (sinds 2026-09-30 12:50 overal vervangen door ' : '); alleen in '(accept: …)' mag het, want dat is wat het kind zelf typt
  - n:m zonder spaties (oude verhoudingsnotatie '1:4'); uitzondering: kloktijden uu:mm in G4–G6 en in G7-MEET-04 ('23:40')
  - oude termen: deel:geheel · a:b · 1:n · schaalverhouding
  - ':' direct na een schaalgetal ('schaal 1 : 50: …')
  - ':' als verhouding ('verhouding 3 : 4'): een verhouding staat in woorden ('3 tot 4', '1 op de 4')
G4–G8 (kindtekst; G7/G8 sinds 12:32, G4–G6 sinds 2026-09-30 12:56):
  - regel (c): geen gewone ':' direct na een getal en gevolgd door een getal, %, € of som ('groepjes van 6: 6+6' leest als 6 : 6),
    behalve na het label 'Stap n:' / 'rij n:' / 'Rij n:' / 'week n:' / 'Week n:' aan het begin van een regel of zin
    (Didactiek 13:06; 'Stap n:' midden in een zin telt sinds 13:12 wél: 'Na stap 1: 3 blokjes' → 'Na stap 1 zijn er 3 blokjes.').
    G3 (sinds 13:06): alleen regel (c); G3 kent de deelteken-regels niet. Schrijf een zin ('groepjes van 6. Je telt 6 + 6 = 12.') of zet een punt of komma.
  - INFO (geen FAIL, besluit Didactiek 13:06), alleen G4–G6: woord (alleen letters, nooit een cijfer) + ': ' + getal ('Reken uit: 4 × 7', 'Vul in: 5 × □', 'Tel: 6 + 6'). Dat telt de checker alleen:
    het zijn er honderden, en in ordenen-opgaven heeft de app de ': ' vóór de lijst nodig
    (leermees-prototype-v1/order-cards.js: 'Lijst = na de laatste ": "'). WOORD_OK = uitzonderingen die ook bij een latere FAIL-regel blijven staan.
Alleen G7 en G8 (kindtekst):
  - in een item met 'schaal 1 :' is ':' alleen schaalnotatie; delen staat daar voluit ('gedeeld door')
Alleen G7: elk schaalitem heeft 'Dat betekent: 1 cm op de kaart/tekening is n cm in het echt.' in de opgave
  (G8: zelfde regels in /workspace/rekenen-groep8/check_bank.py).
Live bestanden zoals build-bank.js (tools/bankfiles.py; G7: ook G7-GET-01/03-claude.md). G8: $G8_BANK mag een preview zijn. $DP_BANK_G<n> = andere map (bv. backup).
Gebruik: python3 check_dubbelepunt.py [groepnummers]   (standaard 3 4 5 6 7 8; G3 alleen regel (c)) · --selftest = voorbeelden · exit 1 bij FAIL.
Hercheck-patroon voor Didactiek (rg, G4–G8, 0 treffers verwacht; kloktijden eruit filteren):
  rg -n '÷|\\b\\d+:\\d|deel ?: ?geheel|schaalverhouding|verhouding\\w* \\d+ ?: ?\\d|schaal 1 : [\\d.]+:' rekenen-groep{4,5,6,7,8}/bank/G*-*.md
"""
import re,sys,glob,os
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from bankfiles import live_files   # live zoals build-bank.js (ook G7-GET-01/03-claude.md)
META=re.compile(r'^- \*\*(Getallenruimte|Context|Visual|Husselen|Rekenmachine|Invoer):')
KLOK=re.compile(r'\b\d{1,2}:\d{2}\b')
ALLE=[("'÷' (gebruik ' : ')",re.compile(r'÷')),
      ('n:m zonder spaties',re.compile(r'\b\d+:\d')),
      ('oude term',re.compile(r'deel ?: ?geheel|\ba:b\b|\b1:n\b|1:…|schaalverhouding',re.I)),
      ("gewone ':' direct na schaalgetal",re.compile(r'schaal 1 : [\d.]+:',re.I)),
      ("':' als verhouding (schrijf '3 tot 4' of '1 op de 4')",re.compile(r'verhouding\w*\s+(?:van\s+)?\d+\s*:\s*\d',re.I))]
DP_GETAL=("':' direct na een getal en gevolgd door getal/%/€ (regel c, Didactiek 2026-09-30)",re.compile(r'\d+%?: [€−-]?\d',re.I))
DP_WOORD=re.compile(r"(?<![Ss]tap )\b[^\W\d_](?:[^\W\d_]|[’'])*: [€−-]?\d")   # alleen letters vóór de ':' (nooit een cijfer)
LABEL=re.compile(r'(^\s*(?:-\s+)?|[.!?;…]\s+)((?:[Ss]tap|[Rr]ij|[Ww]eek) \d+):')   # label aan begin van regel/zin (Didactiek 13:06; 'Stap n:' ook alleen daar sinds 13:12)
def unlabel(t): return LABEL.sub(lambda m:m.group(1)+m.group(2)+' ⟨label⟩',t)
WOORD_OK={  # Didactiek-tekst letterlijk (12:58); valt nu niet onder een FAIL-regel, staat hier voor als de woordregel ooit FAIL wordt
 "G7-VERH-05-008":"fout-hint Stap 3 'vergelijk het deel: 70% is minder dan 75%' (tekst Didactiek)"}
INFO={}
UITLEG=re.compile(r'betekent: 1 cm op de (kaart|tekening|plattegrond) is [\d.]+ cm in het echt',re.I)
KIND=re.compile(r'^(- \*\*(Opgave|Opties|Antwoord|Hint|Sterkere hint|Fout-hints|Ouderzin):\*\*|  )')
def files(g):
    d=os.environ.get(f"DP_BANK_G{g}") or (os.environ.get("G8_BANK",_BANK+"/groep8") if g==8 else f"{_BANK}/groep{g}")
    return live_files(g,d)   # live zoals build-bank.js (G7: ook G7-GET-01/03-claude.md; zonder items en *claude-pilot* niet)
def check(g):
    fails=[]
    for p in files(g):
        name=os.path.basename(p); parts=re.split(r'\n(?=## \d{3})',open(p).read())
        for it in parts:
            num=it[3:6] if it.startswith('## ') else 'hdr'
            for l in it.split('\n'):
                if META.match(l): continue
                ll=re.sub(r'\(accept:[^)]*\)','(accept)',l)   # wat het kind zelf typt: ÷ · : · / mag
                if g in (3,4,5,6) or name=='G7-MEET-04.md': ll=KLOK.sub('uu.mm',ll)
                for label,rx in (ALLE if g!=3 else []):   # G3: alleen regel (c)
                    m=rx.search(ll)
                    if m: fails.append(f'{name} {num} {label}: …{ll[max(0,m.start()-30):m.end()+30]}…')
                if num!='hdr' and KIND.match(l):
                    lk=unlabel(re.sub(r'^- \*\*[\w -]+:\*\*','',ll))
                    m=DP_GETAL[1].search(lk)
                    if m: fails.append(f'{name} {num} {DP_GETAL[0]}: …{lk[max(0,m.start()-30):m.end()+30]}…')
                    if g in (4,5,6) and f"{name[:-3]}-{num}" not in WOORD_OK:
                        for w in DP_WOORD.finditer(lk): INFO.setdefault(g,[]).append(w.group(0).split(':')[0])
            if g in (7,8) and num!='hdr' and re.search(r'schaal 1 : ',it,re.I):
                kt='\n'.join(l for l in it.split('\n') if KIND.match(l))
                for m in re.finditer(r'(?=(\S+) : (\S+))',kt):
                    if not (m.group(1)=='1' and re.search(r'\bschaal $',kt[max(0,m.start()-7):m.start()],re.I)):
                        fails.append(f"{name} {num} ':' in schaalitem niet direct na 'schaal 1' (delen hier voluit): …{kt[max(0,m.start()-25):m.start()+25]}…".replace('\n',' '))
                if g==7:
                    opg='\n'.join(l for l in it.split('\n') if l.startswith('- **Opgave:**') or l.startswith('  '))
                    if not UITLEG.search(opg): fails.append(f"{name} {num} schaal zonder uitleg 'Dat betekent: 1 cm op de kaart/tekening is n cm in het echt' in de opgave")
    return fails
def selftest():
    '''Voorbeelden: FAIL = regel (c); INFO = woord + ': ' + getal (telling); - = niets.'''
    cases=[("groepjes van 6: 6+6","FAIL"),("73: 7 en 3","FAIL"),("€1,50: 1 euro","FAIL"),("25%: 1","FAIL"),("16 over 2: −4","FAIL"),
           ("Stap 1: 3 + 4","-"),("Na stap 1: 3 blokjes","FAIL"),("Kijk. Stap 2: 5","-"),("  - stap 3: 4","-"),("rij 1: 7 · 14","-"),("  - Rij 2: 5 · 10","-"),("Kijk. Week 1: 5 cm","-"),
           ("week 3: 8 cm","-"),("in rij 1: 7","FAIL"),("de 4e week 2: 8","FAIL"),
           ("Reken uit: 4 × 7","INFO"),("Tel: 6 + 6","INFO"),("euro’s: 5","INFO"),("B2: 3","FAIL"),("x1: 4","FAIL"),("(3, 5): 3","-"),
           ("Vul in: □","-"),("12 : 4 = 3","-"),("om 10:30 uur","-"),("schaal 1 : 100","-")]
    bad=0
    for t,want in cases:
        l=unlabel(KLOK.sub('uu.mm',t)); got='FAIL' if DP_GETAL[1].search(l) else ('INFO' if DP_WOORD.search(l) else '-')
        ok=got==want or (want=='FAIL?' and got in('FAIL','-'))
        bad+=not ok; print(f"{'ok ' if ok else 'XX '} {t!r:28} verwacht {want:5} kreeg {got}")
    print('selftest', 'ALLES OK' if not bad else f'{bad} FOUT'); return 1 if bad else 0
if __name__=='__main__':
    args=sys.argv[1:]
    if args==['--selftest']: sys.exit(selftest())
    if args and not args[0].isdigit():   # oud gebruik: pad naar G7-bank
        os.environ["DP_BANK_G7"]=args[0]; args=['7']
    gs=[int(a) for a in args] or [3,4,5,6,7,8]
    bad=0
    for g in gs:
        fl=check(g); bad+=len(fl)
        for x in fl: print(f'G{g} {x}')
        print(f"G{g} dubbele punt/deelteken/schaal: {'ALLES OK' if not fl else f'{len(fl)} FAIL'}")
        if g in INFO:
            from collections import Counter
            top=', '.join(f"'{w}:' {n}" for w,n in Counter(INFO[g]).most_common(6))
            print(f"G{g} INFO woord + ': ' + getal: {len(INFO[g])} (geen FAIL; vaakst: {top})")
    sys.exit(1 if bad else 0)
