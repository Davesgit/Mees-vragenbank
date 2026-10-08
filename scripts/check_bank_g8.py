"""check_bank.py — G8-bank (afgeleid van G6, aangepast aan G8-niveau: %, miljoen/miljard en 3 cijfers na de komma zijn stof).
Draait ook de gedeelde optieletter/Husselen-check (/workspace/tools/check_optieletters.py)."""
import re,glob,sys,os
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
BANKDIR=os.environ.get("G8_BANK",_BANK+"/groep8")  # G8_BANK=/tmp/g8_gen_preview om een preview te checken
files=sorted(glob.glob(os.path.join(BANKDIR,"G8-*.md")))
req=["Opgave","Antwoord","Hint","Sterkere hint","Fout-hints","Ouderzin","Getallenruimte","Context"]
types={"kale","invullen","meerkeuze","verslepen","multi"}
lvl={1:"basis",2:"basis",3:"basis",4:"toepassen",5:"toepassen",6:"toepassen",7:"kritisch",8:"kritisch"}
eng=re.compile(r"\b(the|and|with|is not|tomatoes|answer|hint:|click|drag|choose)\b",re.I)
ok=True; vis=[]; rmlist=[]
DP_GETAL=re.compile(r"\d%?: [€−]?\d")  # zie (c) in de schaalregel
for f in files:
    s=open(f).read(); name=f.split("/")[-1]
    hdr=s.split("\n## ")[0]
    if not re.search(r"^Status: (concept|Didactiek-af \d{4}-\d{2}-\d{2}\.( taal: ok\.)?)\s*$",hdr,re.M): print(name,"header: Status ongeldig"); ok=False
    for h in ["Bordtitel:","Leerdoel-ID: "+name[:-3],"Groep: 8","Label:","Bron: SPINE_G8_v1","Notitie:"]:
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
        # Rekenmachine-vlag: alleen 'ja', en altijd samen met de zin in de opgave (besluit Overzicht 2026-09-30)
        rmv=re.findall(r"^- \*\*Rekenmachine:\*\* (.*)$",it,re.M)
        opg=re.search(r"- \*\*Opgave:\*\*(.*?)\n- \*\*Antwoord:",it,re.S)
        zin=bool(opg) and "Je mag de rekenmachine gebruiken" in opg.group(1)
        if any(v.strip()!="ja" for v in rmv): print(name,m.group(1),"Rekenmachine-vlag moet 'ja' zijn:",rmv); ok=False
        if bool(rmv)!=zin: print(name,m.group(1),"Rekenmachine-vlag en zin 'Je mag de rekenmachine gebruiken' horen samen (vlag:",bool(rmv),"zin:",zin,")"); ok=False
        if rmv: rmlist.append(f"{name[:-3]}-{m.group(1)}")
    if n!=8: ok=False
    kritmulti=[it for it in items if re.match(r"## 00[78] · kritisch · multi",it)]
    if not kritmulti: print(name,"geen multi bij kritisch"); ok=False
    low=s.lower()
    for bad in ["analogie","negatie","strategie"]:
        if bad in low: print(name,"verboden:",bad); ok=False
    for mm in eng.finditer(s): print(name,"engels?",mm.group(0), s[max(0,mm.start()-30):mm.end()+30].replace("\n"," ")); ok=False
    BEWUST_FOUT={"5,0308","4,5007","14,0868","21,7875"}  # bewust foute waarden (afleider / schermwaarde 'achter elkaar ingetikt') met 4 cijfers na de komma, zie bank/README.md
    for mm in re.finditer(r"(?<![\d.])\d+,\d{4,}\b",s):
        if mm.group(0) not in BEWUST_FOUT: print(name,"4+ cijfers na de komma (niet op uitzonderingslijst):",mm.group(0)); ok=False
    # --- extra checks (batch 2) ---
    WL=set()
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
        if re.match(r"- \*\*Antwoord:\*\*",ln) and re.search(r"\d,\d{4,}\b",core): print(name,ln_no,"4+ cijfers na de komma in antwoord"); ok=False
    # Schaalregel (Didactiek-voorstel, besluit 2026-09-30): in items met 'schaal' in de kindtekst is ':' alleen schaalnotatie
    # ('schaal 1 : n', of '1 : n' direct na 'schaal'); ':' als deelteken moet daar voluit ('deel door' / 'gedeeld door').
    for it in items:
        num=it[3:6]
        kt="\n".join(l for l in it.split("\n") if re.match(r"- \*\*(Opgave|Opties|Antwoord|Hint|Sterkere hint|Fout-hints|Ouderzin):\*\*",l) or l.startswith("  "))
        # (c) Didactiek 2026-09-30 (vraag b): geen gewone ':' direct gevolgd door een getal, %, € of som
        #     ('van 60: 60 : 4', 'van de 100: 1'). Wel: ':' + woord, 'Stap n:' en 'schaal 1 : n'.
        for mm in DP_GETAL.finditer(kt):
            if re.search(r"\bstap \d+$",kt[max(0,mm.start()-8):mm.start()+1],re.I): continue
            print(name,num,"':' direct gevolgd door getal/%/€ (lees als deelteken):",kt[max(0,mm.start()-30):mm.end()+20].replace("\n"," ")); ok=False
        if not re.search(r"\bschaal",kt,re.I): continue
        # (a) gespatieerde ':' — links moet 'schaal 1' staan (overlappend zoeken, zodat '1 : 25.000 : 5' ook gevonden wordt)
        for mm in re.finditer(r"(?=(\S+) : (\S+))",kt):
            L,R=mm.group(1),mm.group(2); st=mm.start()
            ctx=kt[max(0,st-30):st+len(L)+len(R)+13].replace("\n"," ")
            if not (L=="1" and re.search(r"\bschaal $",kt[max(0,st-7):st],re.I)):
                print(name,num,"schaalregel: ':' niet direct na 'schaal 1':",ctx); ok=False
            elif not re.fullmatch(r"\d+(?:\.\d{3})*[.,;)?]?",R):
                print(name,num,"schaalregel: rare schaalnoemer / ':' direct na het schaalgetal:",ctx); ok=False
        # (b) uitbreiding 2026-09-30 (Didactiek, VERH-E03-006): geen ':' direct ná een getal ('schaal 1 : 25.000: …'),
        #     behalve 'Stap n:' in hints en genummerde stappen
        for mm in re.finditer(r"(\d[\d.]*):(?!\d)",kt):
            pre=kt[max(0,mm.start()-5):mm.start()]
            if re.search(r"Stap $",pre): continue
            ctx=kt[max(0,mm.start()-30):mm.end()+15].replace("\n"," ")
            print(name,num,"schaalregel: ':' direct na een getal (lijkt op deelteken):",ctx); ok=False
    print(name,len(items),"items")
print("Visual: ja ->",vis)
print("Rekenmachine: ja ->",rmlist)

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
HEUR_OK=set()  # heuristiek vals alarm, handmatig gecontroleerd
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
# Gedeelde regel voor G3–G8, zie /workspace/tools/check_optieletters.py (daar ook uitleg whitelist tekening-labels).
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from check_optieletters import scan as _ol_scan
_ol_fails,_ol_hus=_ol_scan([8],verbose=False)
for _g,_nm,_num,_fld,_msg in _ol_fails: print(f"{_nm}-{_num} [{_fld}] {_msg}"); ok=False
print(f"Husselen: nee ({len(_ol_hus)}) ->"," ".join(_ol_hus) or "-")
# --- vakterm-check (Didactiek batch 4, 2026-09-30): elke vakterm die in de kindtekst van een item staat
# (Opgave · Opties · Hint · Sterkere hint · Fout-hints) moet in datzelfde item uitgelegd zijn: óf met een vaste
# uitlegfrase (VAKTERM[...][1]) ergens in het item, óf met '(' direct na / vlak vóór de term, óf 'term:' (bv. 'cilinder: rond'). 'term is …' telt bewust niet (vals: 'de diagonalen zijn ook …').
# Uitleg in de Ouderzin telt niet. Heuristiek: vals alarm kan in VAKTERM_OK (item-ID) met reden.
VAKTERM={
 "teller":(r"tellers?",r"boven de streep"),
 "noemer":(r"noemers?",r"onder de streep"),
 "gelijknamig":(r"gelijknamig\w*",r"dezelfde noemer"),
 "diagonaal":(r"diagona(?:al|len)",r"hoek naar (?:de )?hoek|van een hoek naar"),
 "spiegellijn":(r"spiegellijn(?:en)?",r"spiegelen in een lijn|lijn waarin je"),
 "lijnsymmetrie":(r"lijnsymmetri\w*",r"spiegel(?:en|t|) (?:je )?in een lijn"),
 "puntsymmetrie":(r"puntsymmetri\w*",r"halve draai"),
 "kijklijn":(r"kijklijn(?:en)?",r"rechte lijn van"),
 "windroos":(r"windroos",r"8 (?:wind)?richtingen"),
 "ribbe":(r"ribben?",r"\(randen?\)"),
 "maquette":(r"maquettes?",r"klein model"),
 "bouwplaat":(r"bouwpla(?:at|ten)",r"vlakke tekening"),
 "cilinder":(r"cilinders?",r"cilinder: rond"),
 "bovenaanzicht":(r"bovenaanzicht",r"tekening van boven"),
 "gemiddelde":(r"gemiddelde",r"tel alles op en deel"),
 "m³":(r"m³",r"kubieke meter"),
 "dm³":(r"dm³",r"kubieke decimeter|1 dm bij 1 dm|dm³ is 1 liter|liter = 1 dm³"),
 "cm³":(r"cm³",r"kubieke centimeter|1 cm bij 1 cm bij 1 cm"),
 "hm":(r"hm",r"hectometer"),"dam":(r"dam",r"decameter"),"hg":(r"hg",r"hectogram"),
 "dg":(r"dg",r"decigram"),"cg":(r"cg",r"centigram"),"cl":(r"cl",r"centiliter"),
 "hectare":(r"hectares?",r"100 m bij 100 m|10\.000 m²"),
 "decennium":(r"decenni(?:um|a)",r"10 jaar"),"kwartaal":(r"kwarta(?:al|len)",r"3 maanden"),
 "etmaal":(r"etmaal",r"24 uur"),
 # VBN (batch 5)
 "assenstelsel":(r"assenstelsels?",r"twee assen"),
 "x-as":(r"x-as",r"horizontale as"),"y-as":(r"y-as",r"verticale as"),
 "coördinaten":(r"coördina(?:at|ten)",r"eerst hoever naar rechts"),
 "oorsprong":(r"oorsprong",r"\(0, 0\)"),
 "legenda":(r"legenda",r"uitleg van de (?:kleuren|plaatjes)|uitlegt wat de kleuren"),
 "lijngrafiek":(r"lijngrafieke?n?",r"met een lijn verbonden"),
 "staafdiagram":(r"staafdiagramm?e?n?",r"staaf per"),
 "cirkeldiagram":(r"cirkeldiagramm?e?n?",r"cirkel verdeeld in stukken"),
 "beelddiagram":(r"beelddiagramm?e?n?",r"plaatje staat voor|1 plaatje is"),
 "trend":(r"trends?",r"richting waarin iets verandert"),
 "turven":(r"turven|turft|turfde",r"met streepjes"),
 "rekenregel":(r"rekenregels?",r"regel die zegt"),
 "regelmaat":(r"regelmaat",r"steeds op dezelfde manier"),
}
VAKTERM_OK={  # "G8-XXX-NNN": "reden" — leeg sinds 2026-09-30 12:3x (MEET-E03-001/003/006 · MEET-E06-008 letterlijk gefikst volgens Didactiek)
}
def _kidtext(it):
    out=[]
    for m in re.finditer(r"(?m)^- \*\*([^*]+):\*\* ?(.*(?:\n(?!- \*\*|## ).*)*)",it):
        if m.group(1) in ("Opgave","Opties","Hint","Sterkere hint","Fout-hints"): out.append(m.group(2))
    return "\n".join(out)
vk_hits=[]
for f in files:
    s_=open(f).read(); nm=f.split("/")[-1][:-3]
    for it in re.split(r"\n(?=## \d{3} · )",s_)[1:]:
        num=it[3:6]; kt=_kidtext(it)
        for term,(tre,expl) in VAKTERM.items():
            occ=list(re.finditer(rf"(?<![\w/]){tre}(?![\w/])",kt,re.I))
            if not occ or f"{nm}-{num}" in VAKTERM_OK: continue
            if re.search(expl,kt,re.I): continue
            if any(re.match(r"\s*(\(|:)",kt[o.end():o.end()+12]) or "(" in kt[max(0,o.start()-6):o.start()] for o in occ): continue
            o=occ[0]; vk_hits.append(f"{nm}-{num} vakterm '{term}' zonder uitleg in het item: …{kt[max(0,o.start()-35):o.end()+25]}…".replace("\n"," "))
for h in vk_hits: print(h); ok=False
print("Vaktermen-check:",len(vk_hits),"treffers ·",len(VAKTERM_OK),"items op VAKTERM_OK (af, ter beslissing):"," ".join(VAKTERM_OK))
for w in warns: print("WARN",w)
jn=[]
for f in files:
    t=open(f).read(); m8=re.search(r"## 008 · kritisch · multi(.*?)(?=\n## |\Z)",t,re.S)
    a=re.search(r"\*\*Antwoord:\*\*.*?3\) (Ja|Nee|ja|nee)",m8.group(1)) if m8 else None
    jn.append((f.split("/")[-1][3:-3],a.group(1).lower() if a else "?"))
print("008-3 ja/nee:"," · ".join(f"{a} {b}" for a,b in jn))
if any(b=="?" for _,b in jn): print("008-3: geen ja/nee gevonden"); ok=False
# Cue-check (Didactiek S7 batch 5, 2026-09-30): goede optie niet herkenbaar aan Ja/Nee-vorm of lengte (gedeeld: /workspace/tools/check_cues.py)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import check_cues
_cst,_cw=check_cues.scan(8)
for _w in _cw: print("CUE",_w); ok=False
print(f"Cues: goede optie langste {_cst['longest']}/{_cst['n']} (toeval ≈ {_cst['chance']/max(1,_cst['n']):.0%}) · Ja/Nee-cue {_cst['jn_cue']} · duidelijk langste {_cst['lang']}")
# Kettingsommen (Didactiek 2026-09-30 12:56; gedeeld: /workspace/tools/check_ketensom.py)
import check_ketensom
_kt=check_ketensom.scan(8)
for _x in _kt:
    if _x[1] in ("FOUT","ONLEESBAAR"): print(f"{_x[0]} kettingsom klopt niet: {_x[2]} (splits in twee zinnen)"); ok=False
print(f"Kettingsommen: {sum(x[1] in ('FOUT','ONLEESBAAR') for x in _kt)} fout · {sum(x[1]=='ok' for x in _kt)} kloppend · {sum(x[1]=='BEWUST' for x in _kt)} bewust fout")
print("ALLES OK" if ok else "PROBLEMEN")
