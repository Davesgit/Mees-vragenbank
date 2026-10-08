import re,glob,sys,os
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
files=sorted(glob.glob(_BANK+"/groep6/G6-*.md"))
req=["Opgave","Antwoord","Hint","Sterkere hint","Fout-hints","Ouderzin","Getallenruimte","Context"]
types={"kale","invullen","meerkeuze","verslepen","multi"}
lvl={1:"basis",2:"basis",3:"basis",4:"toepassen",5:"toepassen",6:"toepassen",7:"kritisch",8:"kritisch"}
eng=re.compile(r"\b(the|and|with|is not|tomatoes|answer|hint:|click|drag|choose)\b",re.I)
ok=True; vis=[]
for f in files:
    s=open(f).read(); name=f.split("/")[-1]
    hdr=s.split("\n## ")[0]
    if not re.search(r"^Status: (concept|Didactiek-af \d{4}-\d{2}-\d{2}\.( taal: ok\.)?)\s*$",hdr,re.M): print(name,"header: Status ongeldig"); ok=False
    for h in ["Bordtitel:","Leerdoel-ID: "+name[:-3],"Groep: 6","Label:","Bron: SPINE_G6_v1","Notitie:"]:
        if h not in hdr: print(name,"header mist",h); ok=False
    items=re.split(r"\n(?=## \d{3} · )",s)[1:]
    if len(items)!=8: print(name,"items",len(items)); ok=False
    for it in items:
        m=re.match(r"## (\d{3}) · (\w+) · (\w+)",it); n=int(m.group(1).strip())
        if m.group(2)!=lvl[n]: print(name,n,"niveau",m.group(2)); ok=False
        if m.group(3) not in types: print(name,n,"type",m.group(3)); ok=False
        for r in req:
            if f"- **{r}:**" not in it: print(name,n,"mist",r); ok=False
        if m.group(3)=="meerkeuze":
            if "- **Opties:**" not in it: print(name,n,"geen opties"); ok=False
            ans=re.search(r"\*\*Antwoord:\*\* ([A-D])\s*$",it,re.M)
            opts=re.findall(r"(?:^|· )([A-D])\)",re.search(r"\*\*Opties:\*\*(.*)",it).group(1).strip())
            if not ans or opts!=["A","B","C","D"][:len(opts)] or ans.group(1) not in opts: print(name,n,"mc probleem",opts); ok=False
            fh=re.search(r"\*\*Fout-hints:\*\*(.*)",it).group(1)
            wrong=[o for o in opts if o!=ans.group(1)]
            for w in wrong:
                if not re.search(rf"(^|· ){w} →",fh.strip()): print(name,n,"fout-hint mist voor",w); ok=False
        if m.group(3)=="verslepen" and "Kaartjes:" in it:
            kaart=[k.strip().split(" (")[0] for k in re.search(r"Kaartjes: (.*)",it).group(1).split("·")]
            kaart=[k.strip() for k in kaart]
            fh=re.search(r"\*\*Fout-hints:\*\*(.*)",it).group(1)
            for part in fh.split(" · "):
                bits=[b.strip() for b in part.split("→")]
                if len(bits)>=3 and bits[1] not in kaart: print(name,n,"fout-hint niet bereikbaar:",bits[1],kaart); ok=False
        if "- **Visual:** ja" in it: vis.append(f"{name[:-3]}-{m.group(1)}")
    if n!=8: ok=False
    if "sub" and "M05" in name:
        sf=re.findall(r"\*\*Subfocus:\*\* (.+)",s); print(name,"subfocus",{x:sf.count(x) for x in set(sf)})
    kritmulti=[it for it in items if re.match(r"## 00[78] · kritisch · multi",it)]
    if not kritmulti: print(name,"geen multi bij kritisch"); ok=False
    low=s.lower()
    for bad in ["analogie","procent","%","miljoen","negatie"]:
        if bad in low: print(name,"verboden:",bad); ok=False
    for mm in eng.finditer(s): print(name,"engels?",mm.group(0), s[max(0,mm.start()-30):mm.end()+30].replace("\n"," ")); ok=False
    BEWUST_FOUT={"6,125","4,100","7,100","6,120"}  # bewust foute bedragen/fout-sleutels (V02, E07), zie notatieregel README
    if "M01" not in name:
        for mm in re.finditer(r"\d,\d{3}\b",s):
            if mm.group(0) not in BEWUST_FOUT: print(name,"3 cijfers na de komma (niet op uitzonderingslijst):",mm.group(0)); ok=False
    # --- extra checks (batch 2) ---
    WL={"87400","22000517"}
    for ln_no,ln in enumerate(s.split("\n"),1):
        core=re.sub(r"\(accept:[^)]*\)","",ln)
        core=re.sub(r"\d{4}-\d{2}-\d{2}","",core)
        for mm in re.finditer(r"(?<![\d.,])\d\.\d{3}(?!\d)(?!\.\d)",core):
            print(name,ln_no,"notatie: 4 cijfers met punt:",mm.group(0)); ok=False
        for mm in re.finditer(r"(?<![\d.,])\d{5,}(?![\d,])",core):
            if mm.group(0) not in WL: print(name,ln_no,"notatie: 5+ cijfers zonder punt:",mm.group(0)); ok=False
        if re.search(r"Tel na:[^·\n]*×",ln): print(name,ln_no,"'Tel na' bij keer-controle -> 'Reken na'"); ok=False
        kind=re.match(r"- \*\*(Opgave|Opties|Hint|Sterkere hint|Fout-hints):\*\*",ln) or ln.startswith("  ")
        if kind and re.search(r"invulveld",ln,re.I): print(name,ln_no,"invulveld-meta in kindtekst"); ok=False
        if kind and re.search(r"(?<![\d/])\d \d+/\d+",core): print(name,ln_no,"gemengd getal zonder vaste spatie"); ok=False
        if re.match(r"- \*\*(Antwoord|Opties):\*\*",ln) and re.search(r"\d,\d{3}\b",core) and "M01" not in name: print(name,ln_no,"3 cijfers na de komma in antwoord/opties"); ok=False
    print(name,len(items),"items")
print("Visual: ja ->",vis)

# --- extra checks (batch 4 / Overzicht): MC-spreiding, MC-consistentie, komma-rijtjes ---
from collections import Counter,OrderedDict
def _fields(it):
    return {m.group(1):m.group(2) for m in re.finditer(r"(?m)^- \*\*([^*]+):\*\* ?(.*)",it)}
def _toks(t):
    t=t.lower()
    nums=set(re.findall(r"\d+(?:[.,/]\d+)*",t))
    words=set(w for w in re.findall(r"[a-zà-ÿ]{4,}",t) if w not in {"want","niet","maar","heeft","hebben","zijn","dat","deze","meer","minder","klopt","allebei"})
    return nums|words
mc_seq=[]; per_id=OrderedDict(); warns=[]
HEUR_OK={"VERH-E03-007"}  # heuristiek vals alarm, handmatig gecontroleerd
for f in files:
    s_=open(f).read(); nm=f.split("/")[-1][3:-3]
    for it in re.split(r"\n(?=## \d{3} · )",s_)[1:]:
        m=re.match(r"## (\d{3}) · (\w+) · (\w+)",it)
        if m.group(3)!="meerkeuze": continue
        d=_fields(it); ans=d.get("Antwoord","").strip()
        opts=OrderedDict(re.findall(r"(?:^|· )([A-D])\) (.*?)(?= · [A-D]\) |$)",d.get("Opties","").strip()))
        mc_seq.append((nm,m.group(1),ans)); per_id.setdefault(nm,[]).append(ans)
        # (b) consistentie: genoemde letters bestaan, geen fout-hint op het goede antwoord, fout-hint past bij optie-inhoud
        keys=re.findall(r"(?:^|· )([A-Z]) → ",d.get("Fout-hints","").strip())
        for k in keys:
            if k not in opts: print(nm,m.group(1),"MC: fout-hint noemt letter die niet bestaat:",k); ok=False
        if ans in keys: print(nm,m.group(1),"MC: fout-hint op het goede antwoord",ans); ok=False
        segs=dict(re.findall(r"(?:^|· )([A-D]) → (.*?)(?= · [A-D] → |$)",d.get("Fout-hints","").strip()))
        for k,txt in segs.items():
            if k not in opts: continue
            ht=_toks(txt); sc={L:len(_toks(o)&ht) for L,o in opts.items()}
            best=max(sc.values())
            if f"{nm}-{m.group(1)}" in HEUR_OK: continue
            if sc[k]==0 and best>=3 and len(_toks(opts[k]))>=3 and [L for L in sc if sc[L]==best]!=[ans]:
                warns.append(f"{nm}-{m.group(1)} fout-hint {k} lijkt eerder bij optie {max(sc,key=sc.get)} te horen")
        for fld in ("Hint","Sterkere hint"):
            if re.search(r"\b(optie|opties) [A-D]\b",d.get(fld,"")): print(nm,m.group(1),f"MC: {fld} noemt een optieletter (controleer na herordenen)"); ok=False
# (a) spreiding
tot=Counter(a for _,_,a in mc_seq); N=sum(tot.values())
print("MC goede letter bank-breed:",dict(sorted(tot.items())),f"(n={N})")
for L,c in tot.items():
    if N and c/N>0.45: print(f"MC-spreiding: letter {L} is {c}/{N} = {c/N:.0%} (> 45%)"); ok=False
for nm,lst in per_id.items():
    if len(lst)>=2 and len(set(lst))==1: print(nm,"MC-spreiding: alle MC's hebben letter",lst[0]); ok=False
print("MC per ID:"," ".join(f"{nm}:{''.join(l)}" for nm,l in per_id.items()))
run=1
for i in range(1,len(mc_seq)):
    run=run+1 if mc_seq[i][2]==mc_seq[i-1][2] else 1
    if run==4: warns.append(f"reeks van 4x letter {mc_seq[i][2]} t/m {mc_seq[i][0]}-{mc_seq[i][1]}")
# (c) komma-rijtjes 'getal, getal, getal' in kind- en oudertekst (decimale komma zonder spatie telt niet)
TOK=r"€?\d+(?:[.,]\d+)?(?:/\d+)?(?: ?(?:°C|[a-zA-Z²]{1,6}))?"
rij=re.compile(rf"(?<![\w,]){TOK}, {TOK}, {TOK}")
TOKB=r"€?\d+(?:[.,]\d+)?(?:/\d+)?"
rij2=re.compile(rf"(?<![\w,]){TOKB}, {TOKB}(?:, {TOKB})* (?:en|of) {TOKB}(?![\w/]| ?[a-z]{{1,6}}\b(?<!\ben)(?<!\bof)(?<!\bvan)(?<!\btot))")
for f in files:
    for ln_no,ln in enumerate(open(f).read().split("\n"),1):
        if not (re.match(r"- \*\*(Opgave|Opties|Hint|Sterkere hint|Fout-hints|Ouderzin|Antwoord):\*\*",ln) or re.match(r"\s+(\d\.|- |\S)",ln)): continue
        core=re.sub(r"\(accept:[^)]*\)|\(rubric:[^)]*\)","",ln)
        for mm in list(rij.finditer(core))+list(rij2.finditer(core)):
            print(f.split("/")[-1],ln_no,"komma-rijtje (gebruik ' · '):",mm.group(0)); ok=False
# --- extra check (Overzicht/Website 2026-09-30): geen optieletters in hint-kindtekst + Husselen ---
# Gedeelde regel voor G3–G7, zie /workspace/tools/check_optieletters.py (daar ook uitleg whitelist tekening-labels).
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from check_optieletters import scan as _ol_scan
_ol_fails,_ol_hus=_ol_scan([6],verbose=False)
for _g,_nm,_num,_fld,_msg in _ol_fails: print(f"{_nm}-{_num} [{_fld}] {_msg}"); ok=False
print(f"Husselen: nee ({len(_ol_hus)}) ->"," ".join(_ol_hus) or "-")
for w in warns: print("WARN",w)
print("ALLES OK" if ok else "PROBLEMEN")
