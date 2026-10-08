#!/usr/bin/env python3
"""Cue-check meerkeuze G3–G8 (Didactiek S7 batch 5 · Overzicht 2026-09-30).
Doel: het goede antwoord mag niet opvallen door vorm of lengte.
Per MC-item met Opties (A–D) en een sleutelletter:
  JN-VORM   als één optie met 'Ja'/'Nee' begint, moeten alle opties dat doen, en altijd met een komma ('Ja, …' / 'Nee, …').
  JN-CUE    de goede optie is de enige met die vorm (enige Ja/Nee, enige met 'Ja:'/'Nee:'/'Nee —' …, of de enige 'Ja' tussen 'Nee'-opties en andersom).
  LANG      de goede optie is duidelijk de langste: ≥ 8 tekens én ≥ 25% langer dan de langste afleider.
Per bank: hoe vaak de goede optie (strikt) de langste is, tegenover de kans bij toeval (som van 1/k).
  LANG-BANK als dat aandeel meer dan 1,5 × de toevalskans is (en minstens 3 items meer).
Live bestanden zoals build-bank.js (tools/bankfiles.py; G7: ook G7-GET-01/03-claude.md). G8: $G8_BANK mag een preview zijn. $CUES_BANK_G<n> = andere map (bv. een backup, voor een telling vóór/na).
Gebruik: python3 check_cues.py [groepnummers] [--quiet]   · exit 1 bij een WARN."""
import re,glob,os,sys
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from check_optieletters import items,fields,option_segments
from bankfiles import live_files
JN=re.compile(r"^(Ja|Nee)\b\s*([,:;—–.-])?")
def bank_files(g):
    d=os.environ.get(f"CUES_BANK_G{g}") or (os.environ.get("G8_BANK",_BANK+"/groep8") if g==8 else f"{_BANK}/groep{g}")
    return live_files(g,d)   # live zoals build-bank.js (G7: ook G7-GET-01/03-claude.md)
def clean(t): return re.sub(r"\s+"," ",t).strip().rstrip(".")
def form(t):
    m=JN.match(t); return (m.group(1),m.group(2) or "") if m else None
def mc_items(g):
    for f in bank_files(g):
        name=os.path.basename(f)[:-3]
        for it in items(open(f).read()):
            d=fields(it); opts=option_segments(d)
            a=re.match(r"\s*([A-D])\b",d.get("Antwoord",""))
            if len(opts)<2 or not a or a.group(1) not in opts: continue
            yield f"{name}-{it[3:6]}",a.group(1),{k:clean(v) for k,v in opts.items()}
def scan(g):
    warns=[]; n=0; longest=0; chance=0.0; jn_items=0; jn_cue=0; lang=0
    for iid,ans,opts in mc_items(g):
        n+=1; c=opts[ans]; others=[v for k,v in opts.items() if k!=ans]
        L=len(c); M=max(len(v) for v in others)
        if L>M: longest+=1
        chance+=1/len(opts)
        if L>M and L-M>=8 and L>=1.25*M: lang+=1; warns.append(f"LANG {iid}: goede optie {L} tekens, langste afleider {M}")
        fs={k:form(v) for k,v in opts.items()}
        if any(fs.values()):
            jn_items+=1
            if not all(fs.values()): warns.append(f"JN-VORM {iid}: niet alle opties beginnen met Ja/Nee")
            bad=[k for k,v in fs.items() if v and v[1]!=","]
            if bad: warns.append(f"JN-VORM {iid}: 'Ja/Nee' zonder komma bij {'/'.join(bad)}")
            if all(fs.values()) and len(opts)>=3 and sum(1 for v in fs.values() if v[0]==fs[ans][0])==1:
                jn_cue+=1; warns.append(f"JN-CUE {iid}: goede optie is de enige die met '{fs[ans][0]}' begint")
            sig=lambda v:(v is not None, v[1] if v else None)
            if fs[ans] and all(sig(fs[k])!=sig(fs[ans]) for k in opts if k!=ans):
                jn_cue+=1; warns.append(f"JN-CUE {iid}: goede optie is de enige met vorm '{fs[ans][0]}{fs[ans][1]}'")
    if n and longest/n>1.5*chance/n and longest-chance>=3:
        warns.append(f"LANG-BANK G{g}: goede optie is de langste in {longest}/{n} ({longest/n:.0%}), toeval ≈ {chance/n:.0%}")
    return dict(n=n,longest=longest,chance=chance,jn_items=jn_items,jn_cue=jn_cue,lang=lang),warns
if __name__=="__main__":
    gs=[int(a) for a in sys.argv[1:] if a.isdigit()] or [3,4,5,6,7,8]
    tot=0
    for g in gs:
        st,w=scan(g); tot+=len(w)
        if "--quiet" not in sys.argv:
            for x in w: print("WARN",x)
        print(f"G{g} cues: MC {st['n']} · goede optie langste {st['longest']} ({st['longest']/max(1,st['n']):.0%}, toeval ≈ {st['chance']/max(1,st['n']):.0%}) · duidelijk langste {st['lang']} · Ja/Nee-items {st['jn_items']} · Ja/Nee-cue {st['jn_cue']} · {'ALLES OK' if not w else f'{len(w)} WARN'}")
    sys.exit(1 if tot else 0)
