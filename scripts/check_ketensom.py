#!/usr/bin/env python3
"""Kettingsommen G3–G8 (Didactiek 2026-09-30 12:56).
Verboden: een keten 'a op b = c op d = e' die wiskundig niet klopt, zoals '5 × 8 = 40 − 10 = 30' (5 × 8 is geen 30).
Schrijf twee zinnen: '5 × 8 = 40. Dan 40 − 10 = 30.' Of twee regels. Gebruik geen '·' als scheider tussen sommen.
Sinds 13:12 ook MISLEIDEND (FAIL): een tussenstap die van links naar rechts gelezen niet klopt, zoals '9 × 6 = 60 − 6 = 54'
('9 × 6 = 60'). Schrijf de volledige vorm '9 × 6 = 10 × 6 − 6 = 60 − 6 = 54', of in G3/G4 twee zinnen ('Eerst 10 × 6 = 60. Dan 60 − 6 = 54.').
Regel: begint een deel met een kaal getal n en dan + of −, dan moet n een tussenuitkomst zijn van het deel ervoor (van links naar rechts).
Keer- en deelstappen met gelijke waarde ('3600 : 60 = 360 : 6', '40 × 20 = 4 × 2 × 10 × 10') vallen daar niet onder.
In orde (geen melding): ketens waarin alle delen even veel zijn en elke tussenstap klopt ('3 + 4 = 7 = 7', '9 + 7 = 9 + 1 + 6 = 10 + 6',
'0,5 = 1/2 = 50%', '1 : 100 = 1/100 = 0,01 = 1%').
Patroon: minstens drie delen met '=' ertussen en in een middendeel een som (getal [+ − - × x * : /] getal), ook met spaties.
Elke keten wordt uitgerekend: ':' en '/' = delen, '%' = /100, '€' wordt genegeerd, komma = decimaal, punt = duizendtal.
Niet meegeteld: '(accept: …)' (invoervarianten met '/' als scheider), kloktijden, meta-regels (Getallenruimte …),
'1 op de 5 = …' (begint bij een woord) en gemengde getallen ('8/3 = 2 2/3').
BEWUST_FOUT: items waar de foute keten de opdracht is (fout zoeken, foute afleiders); die staan hieronder, met reden.
Gebruik: python3 check_ketensom.py [groepnummers]   (standaard 3 4 5 6 7 8) · exit 1 bij FAIL.
$KETEN_BANK_G<n> = andere map (bv. backup); G8 volgt ook $G8_BANK.
Hercheck (rg, ruwe zoekvraag; daarna zelf uitrekenen):
  rg -n --pcre2 '= ?€?\\d[\\d.,/]*%? ?[+−×:x*/-] ?€?\\d[\\d.,/]*%? ?=' rekenen-groep{3,4,5,6,7,8}/bank/G*-*.md
"""
import re,glob,os,sys
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from bankfiles import live_files   # live zoals build-bank.js (ook G7-GET-01/03-claude.md)
from fractions import Fraction
BEWUST_FOUT={
 "G5-GET-E09-007":"opgave: Sam rekent fout ('8 × 25 + 40 = 8 × 65 = 520'); het kind zoekt de fout",
 "G8-VERH-E06-004":"MC 'In welke rij is alles even veel?': afleiders A, C en D zijn bewust foute rijen",
}
NUM=r'(?:€\s?)?\d+(?:\.\d{3})*(?:,\d+)?(?:/\d+)?%?'
OP=r'\s*[+−×:x*/\-]\s*'
SEG=rf'{NUM}(?:{OP}{NUM})*'
CHAIN=re.compile(rf'(?<![\w,./])(?<!de )({SEG}(?:\s*=\s*{SEG}){{2,}})(?!\d|,\d)(?!\s\d+/\d)')
SOM=re.compile(rf'\d{OP}(?:€\s?)?\d')
def val(seg):
    s=seg.replace('€','').replace(' ','')
    s=re.sub(r'(\d)\.(\d{3})(?!\d)',r'\1\2',s); s=re.sub(r'(\d)\.(\d{3})(?!\d)',r'\1\2',s)
    s=re.sub(r'(\d+(?:,\d+)?)%',r'(\1/100)',s)
    s=s.replace(',','.').replace('−','-').replace('×','*').replace('x','*').replace(':','/')
    s=re.sub(r'(\d+(?:\.\d+)?)',lambda m:f'Fraction("{m.group(1)}")',s)
    return eval(s,{"Fraction":Fraction})
ADD=re.compile(r'\s*([+−\-])\s*')
def terms(seg):
    '''optel-termen van links naar rechts: [(teken, term), …]'''
    parts=ADD.split(seg.strip()); out=[('+',parts[0])]
    for i in range(1,len(parts),2): out.append((parts[i],parts[i+1]))
    return out
def tussenstap_ok(L,R):
    '''Didactiek 13:12: een tussenstap moet van links naar rechts kloppen. Begint R met een kaal getal n en dan + of −
    (zoals '60 − 6'), dan moet n een tussenuitkomst van L zijn (van links naar rechts opgeteld): '9 × 6 = 60 − 6' faalt
    (9 × 6 is geen 60), '10 × 6 − 6 = 60 − 6' en '9 + 1 + 6 = 10 + 6' kloppen.'''
    tr=terms(R)
    if len(tr)<2 or not re.fullmatch(NUM,tr[0][1].strip()): return True
    n=val(tr[0][1]); acc=None
    for sign,t in terms(L):
        v=val(t); acc=v if acc is None else (acc+v if sign=='+' else acc-v)
        if acc==n: return True
    return False
def files(g):
    d=os.environ.get(f"KETEN_BANK_G{g}") or (os.environ.get("G8_BANK",_BANK+"/groep8") if g==8 else f"{_BANK}/groep{g}")
    return live_files(g,d)   # live zoals build-bank.js (G7: ook G7-GET-01/03-claude.md; zonder items en *claude-pilot* niet)
def scan(g):
    out=[]
    for p in files(g):
        name=os.path.basename(p)[:-3]; cur='hdr'
        for l in open(p).read().split('\n'):
            m=re.match(r'## (\d{3}) ·',l)
            if m: cur=m.group(1)
            if re.match(r'- \*\*(Getallenruimte|Context|Visual|Husselen|Rekenmachine|Invoer):',l): continue
            ll=re.sub(r'\(accept:[^)]*\)','(accept)',l); ll=re.sub(r'\b\d{1,2}:\d{2}\b','uu.mm',ll)
            for m in CHAIN.finditer(ll):
                segs=re.split(r'\s*=\s*',m.group(1))
                if not any(SOM.search(s) for s in segs[1:-1]): continue
                iid=f"{name}-{cur}"
                try: vals=[val(s) for s in segs]
                except Exception: out.append((iid,'ONLEESBAAR',m.group(1))); continue
                if len(set(vals))>1: out.append((iid,'BEWUST' if iid in BEWUST_FOUT else 'FOUT',m.group(1)))
                elif not all(tussenstap_ok(segs[i-1],segs[i]) for i in range(1,len(segs))):
                    out.append((iid,'BEWUST' if iid in BEWUST_FOUT else 'MISLEIDEND',m.group(1)))
                else: out.append((iid,'ok',m.group(1)))
    return out
if __name__=='__main__':
    gs=[int(x) for x in sys.argv[1:]] or [3,4,5,6,7,8]; bad=False
    for g in gs:
        r=scan(g); f=[x for x in r if x[1] in ('FOUT','ONLEESBAAR','MISLEIDEND')]
        for x in f: print(f"G{g} {x[0]} {x[1]}: {x[2]}  → " + ("splits: '… = c. Dan c … = e.'" if x[1]=='FOUT' else "volledige vorm: '9 × 6 = 10 × 6 − 6 = 60 − 6 = 54' (of twee zinnen)"))
        nb=sum(x[1]=='BEWUST' for x in r); nok=sum(x[1]=='ok' for x in r)
        print(f"G{g} kettingsommen: {len(f)} fout/misleidend · {nok} kloppend (in orde) · {nb} bewust fout (BEWUST_FOUT) · {'ALLES OK' if not f else 'FAIL'}")
        bad|=bool(f)
    sys.exit(1 if bad else 0)
