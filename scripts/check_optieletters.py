#!/usr/bin/env python3
"""Gedeelde bankcheck G3–G8 (Overzicht/Website, 2026-09-30).

Regel 1 — geen optieletters in kindtekst van hints.
  De app husselt meerkeuze-opties. Daarom mogen Hint, Sterkere hint, Fout-hints (de tekst ná de sleutel)
  en Ouderzin niet naar een optieletter (A/B/C/D) verwijzen. Verwijs naar de inhoud van de optie.
  - De sleutel van een fout-hint ('B → …', 'Stap 2 → …', 'C → A → B → …' bij ordenen) is metadata.
  - Uitzondering (tekening-label): een letter die in de Opgave zelf als label staat (strook A, pijltje C,
    beker B, kolom D, punt B op de plattegrond, 'A B C |' bij spiegelen …) is inhoud en mag.
  - Formule-variabelen naast '×' (bijv. 2 × B voor breedte) tellen niet mee.
Regel 2 — Husselen.
  Een meerkeuze-item waarvan de opties vastzitten aan labels in de tekening moet '- **Husselen:** nee'
  hebben (build → shuffle:false). Dat is zo als (a) een optie alleen een label is ('A) strook A', 'B) Doos B',
  'C) C'), of (b) de tekening in de Opgave zelf regels 'A) …', 'B) …' heeft die met de optieletters samenvallen.
  Ook (c): een optie noemt zelf een letter die in de Opgave een label is ('C) Nee, B heeft …', 'A) Beker A …'),
  anders botsen label en optieletter na husselen. Meerkeuze zonder Opties-veld (keuzes A) B) C) in de Opgave) telt mee.
  'Husselen:' accepteert alleen de waarde 'nee'.
Regel 3 — WARN (geen FAIL): getal van ≥5 cijfers zonder punt in kindtekst (4 cijfers zonder punt, vanaf 10.000 met punt);
  accept-lijsten, Invoer en fout-hint-sleutels tellen niet mee. Ook WARN: macht (cijfer + ², ³ of ^). Logica en uitzonderingen: tools/check_notatie.py.
Gebruik: python3 check_optieletters.py [groepnummers ...]   (standaard alle banken G3–G8 die bestaan); exit 1 bij FAIL.
"""
import re,glob,sys,os
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
FIELDS=("Hint","Sterkere hint","Fout-hints","Ouderzin")
BARE=re.compile(r"(?<![\w°/.,'’-])([A-D])(?![\w'’/-])")
def files_for(g):
    return [f for f in sorted(glob.glob(f"{_BANK}/groep{g}/*.md")) if not f.endswith("README.md")]
def items(s):
    return re.split(r"(?m)^(?=## \d{3} )",s)[1:]
def fields(it):
    return {m.group(1):m.group(2) for m in re.finditer(r"(?m)^- \*\*([^*]+):\*\* ?(.*(?:\n(?!- \*\*|## ).*)*)",it)}
def is_mc(d,it=""):
    return "Opties" in d or bool(re.match(r"## \d{3} · [^\n]*\bmeerkeuze\b",it))
def option_segments(d):
    segs=re.split(r"(?:^|\s·\s|\n\s*(?:- )?)(?=[A-D]\))",d.get("Opties",""))
    out={}
    for sg in segs:
        m=re.match(r"([A-D])\)\s*(.*)",sg.strip(),re.S)
        if m: out[m.group(1)]=m.group(2).strip()
    return out
def needs_no_shuffle(d,it=""):
    if not is_mc(d,it): return None
    for L,t in option_segments(d).items():
        if re.fullmatch(r"(?:[\wÀ-ÿ-]+ )?[A-D]\.?",t): return f"optie {L}) '{t}' is een tekening-label"
    if re.search(r"(?m)^\s*[A-D]\) ",d.get("Opgave","")): return "tekening/keuzes in de Opgave hebben labels A) B) … gelijk aan de optieletters"
    lab=opgave_labels(d)
    for L,t in option_segments(d).items():
        hit=sorted(set(BARE.findall(t))&lab)
        if hit: return f"optie {L}) noemt tekening-label {'/'.join(hit)} (botst met optieletters bij husselen)"
    return None
def opgave_labels(d):
    return set(BARE.findall(d.get("Opgave","")))
def strip_keys(txt):
    """Haal de sleutel van elk fout-hint-segment af ('B → ', 'Stap 2 → 18 → ', 'C → A → B → ', 'B eerst → ');
    alleen de kindtekst blijft over. Sleuteldelen zijn korte stukjes vóór een '→'."""
    out=[]
    for sg in re.split(r" · (?=[^·]*?→)",txt.strip()):
        if " → " in sg:
            sg=sg.split(" → ",1)[1]
            while True:
                m=re.match(r"([^→]{1,15}?) → ",sg)
                if not m or len(m.group(1).split())>3: break
                sg=sg[m.end():]
        out.append(sg)
    return " · ".join(out)
def letter_hits(text,allowed=frozenset()):
    hits=[]
    for m in BARE.finditer(text):
        if m.group(1) in allowed: continue
        before=text[max(0,m.start()-3):m.start()]; after=text[m.end():m.end()+3]
        if before.endswith("× ") or after.startswith(" ×"): continue
        hits.append((m.group(1),text[max(0,m.start()-35):m.end()+35].replace("\n"," ")))
    return hits
def scan(groups=(3,4,5,6,7),verbose=True):
    fails=[]; husselen=[]
    for g in groups:
        for f in files_for(g):
            name=os.path.basename(f)[:-3]
            for it in items(open(f).read()):
                num=it[3:6]; d=fields(it)
                hm=re.findall(r"(?m)^- \*\*Husselen:\*\* ?(.*)$",it)
                for v in hm:
                    if v.strip()!="nee": fails.append((g,name,num,"Husselen",f"alleen 'nee' toegestaan, gevonden: '{v.strip()}'"))
                if hm and all(v.strip()=="nee" for v in hm): husselen.append(f"{name}-{num}")
                why=needs_no_shuffle(d,it)
                if why and not hm: fails.append((g,name,num,"Husselen",why+" → '- **Husselen:** nee' ontbreekt"))
                if hm and not is_mc(d,it): fails.append((g,name,num,"Husselen","Husselen hoort alleen bij meerkeuze"))
                allowed=opgave_labels(d)
                for fld in FIELDS:
                    if fld not in d: continue
                    txt=strip_keys(d[fld]) if fld=="Fout-hints" else d[fld]
                    for L,ctx in letter_hits(txt,allowed):
                        fails.append((g,name,num,fld,f"optieletter '{L}': …{ctx}…"))
    if verbose:
        for x in fails: print(f"FAIL {x[1]}-{x[2]} [{x[3]}] {x[4]}")
        print(f"Husselen: nee ({len(husselen)}) ->"," ".join(husselen) or "-")
    return fails,husselen
if __name__=="__main__":
    gs=[int(a) for a in sys.argv[1:]] or [g for g in (3,4,5,6,7,8) if os.path.isdir(f"{_BANK}/groep{g}")]
    fails,_=scan(gs)
    for g in gs:
        n=sum(1 for x in fails if x[0]==g); print(f"G{g} optieletters/husselen: {'ALLES OK' if n==0 else f'{n} FAIL'}")
    # Regel 3 (WARN, Overzicht 13:23): ≥5 cijfers zonder punt in kindtekst → zie tools/check_notatie.py
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import check_notatie
    warn,_=check_notatie.scan(gs)
    for w in warn: print(f"WARN notatie {w[1]} [{w[2]}] " + (f"macht '{w[3][6:]}' (VO-stof, uitschrijven)" if w[3].startswith("MACHT:") else f"'{w[3]}' zonder punt (vanaf 10.000 met punt)") + f" → {w[5]}:{w[4]}")
    print(f"Notatie (≥5 cijfers met punt, WARN): {'ALLES OK' if not warn else f'{len(warn)} WARN'}")
    sys.exit(1 if fails else 0)
