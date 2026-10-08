#!/usr/bin/env python3
"""Check op de hints van de G3-pilot (somtypen/G3-*.md), 2026-10-01.
Per '## Somtype n' met 'Status: hints klaar':
  FAIL  Hint 1 of Hint 2 leeg (ook als Ouderzin ontbreekt).
  FAIL  optieletter (A/B/C/D als los woord) in Hint 1, Hint 2, Ouderzin of een nieuwe fout-hint (de app husselt opties).
  FAIL  ':' direct gevolgd door een getal of som ('Via 10: 9 + 1'); schrijf 'Eerst naar 10. 9 + 1 = 10.'
  FAIL  '×' of 'x' tussen getallen (G3 schrijft herhaald optellen: 3 + 3 + 3; Didactiek 2026-10-01).
  FAIL  moeilijke woorden uit besluiten_twijfel.md (kittens, maanstenen, spiegelen, ruit, zeshoek …); 'patroon' mag.
  FAIL  taalregels Didactiek v1, over ALLE teksten in hints/batch*.json (ook Claude-fout-hints 'ok'):
        'tiental naast' · 'er gaan/komen er weg/uit/bij' zonder getal · 'er komt/gaat bij/weg' zonder 'iets' ·
        spelling 'terug gegaan', 'uit gaan', 'bij komen', 'bij gedaan', 'is-teken' ·
        'volle rij' als niet elk item van het somtype minstens één volle rij heeft (jsRender aantal ≥ perrij; anders INFO).
  FAIL  '÷', machten (cijfer + ², ³ of ^), 4-cijferig getal met punt (1.000), Engelse woorden (Scaffold …).
  FAIL  het antwoord van een voorbeeld staat in Hint 1 of Hint 2 (getal als los getal, of de hele antwoordtekst).
  WARN  het antwoord van een ander item van dit somtype (uit data/per_doel/<doel>.json) staat in Hint 1/2.
  WARN  een getal in Hint 1/2 (hints moeten voor elke vraag werken; 10, 20 en 100 als ankers zijn INFO).
  WARN  keten met twee keer '=' of een kommalijst van sommen ('3 + 4, 5 + 2'); G3 schrijft 'en' tussen sommen.
Somtypes zonder 'hints klaar' tellen als 'open'.
Gebruik: python3 check_hints.py [bestand.md ...]   (standaard alle somtypen/G3-*.md) · exit 1 bij FAIL.
"""
import re,sys,os,glob,json
BASE=os.path.dirname(os.path.abspath(__file__))
LETTER=re.compile(r"(?<![\w'’/.-])([A-D])(?![\w'’/-])")
DUBBEL=re.compile(r':\s*(?:€\s?)?\d')
ENGELS=re.compile(r'\b(scaffold\w*|hint|tip of the|step|count|next|answer)\b',re.I)
ANKER={10,20,100}
MOEILIJK=re.compile(r'\b(kitten\w*|maanste\w*|ruimtepak\w*|schroef\w*|schroeven|spiegel\w*|zeshoek\w*|vijfhoek\w*|ruit)\b',re.I)   # Didactiek besluiten_twijfel.md; 'patroon' mag (Didactiek b3 Z6: G3-bank gebruikt het)
def sections(p):
    cur=None; out=[]
    for l in open(p,encoding='utf-8').read().split("\n"):
        m=re.match(r'^## Somtype (\d+): (.*)$',l)
        if m: cur={"nr":int(m.group(1)),"somtype":m.group(2).strip(),"ant":[],"fh":[],"h1":None,"h2":None,"ouder":None,"status":None}; out.append(cur); continue
        if l.startswith("## ") or l.startswith("---"): cur=None; continue
        if cur is None: continue
        if m:=re.match(r'^\s+- \*\*Antwoord:\*\*\s*(.*?)\s*(\(controle.*)?$',l): cur["ant"].append(m.group(1).strip())
        elif m:=re.match(r'^- \*\*Hint 1(?: \(te schrijven\))?:\*\*\s?(.*)$',l): cur["h1"]=m.group(1).strip()
        elif m:=re.match(r'^- \*\*Hint 2(?: \(te schrijven\))?:\*\*\s?(.*)$',l): cur["h2"]=m.group(1).strip()
        elif m:=re.match(r'^- \*\*Ouderzin:\*\*\s?(.*)$',l): cur["ouder"]=m.group(1).strip()
        elif m:=re.match(r'^\s+- (?:`[^`]*` )?\(.*?\) → (.*?)\s+\[(?:nieuw|Claude, taalfix)\]$',l): cur["fh"].append(m.group(1))
        elif m:=re.match(r'^- Status:\s*(.*)$',l): cur["status"]=m.group(1).strip()
    return out
def item_answers(doel,somtype):
    p=f"{BASE}/data/per_doel/{doel}.json"
    if not os.path.exists(p): return []
    return [it['antwoord'] for it in json.load(open(p,encoding='utf-8'))['items'] if it['merge']['somtype']==somtype]
def norm(s): return re.sub(r'\s+',' ',s.replace('−','-')).strip()
def ans_hits(ant,txt):
    t=norm(txt); a=norm(ant)
    if re.fullmatch(r'\d+',a): return bool(re.search(rf'(?<![\d.,]){a}(?!\d|[.,]\d)',t))
    if '|' in a: return a.replace('|',' ') in t or ', '.join(a.split('|')) in t
    return len(a)>2 and a in t
TAAL=[("'tiental naast' (klopt vaak niet; 'Dat is veel te ver.')",re.compile(r'tiental naast',re.I)),
      ("'er gaan/komen er …' zonder getal ('Er gaan dingen weg')",re.compile(r'\b[Ee]r (?:gaan|komen|gaat|komt) er (?:weg|uit|bij|af|eraf|erbij)\b')),
      ("'er komt/gaat …' zonder 'iets' ('Er komt iets bij')",re.compile(r'\b[Ee]r (?:komt|gaat) (?:bij|weg|uit|af)\b')),
      ("spelling 'teruggegaan'",re.compile(r'terug gegaan',re.I)),("spelling 'uitgaan'",re.compile(r'\buit gaan\b',re.I)),
      ("spelling 'bijkomen'",re.compile(r'\bbij komen\b',re.I)),("spelling 'bijgedaan'",re.compile(r'\bbij gedaan\b',re.I)),
      ("'isgelijkteken' (niet 'is-teken')",re.compile(r'is-teken',re.I))]
def volle_rij_ok(doel,somtype):
    p=f"{BASE}/data/per_doel/{doel}.json"
    if not os.path.exists(p): return False
    its=[it for it in json.load(open(p,encoding='utf-8'))['items'] if it['merge']['somtype']==somtype]
    def ok(it):
        jr=((it.get('visual') or {}).get('jsRender') or {})
        return isinstance(jr.get('aantal'),int) and isinstance(jr.get('perrij'),int) and jr['aantal']>=jr['perrij']
    return bool(its) and all(ok(it) for it in its)
def json_taal():
    fails=[];info=[]
    for p in sorted(glob.glob(f"{BASE}/hints/batch*.json")):
        for st in json.load(open(p,encoding='utf-8'))['somtypen']:
            tag=f"{st['doel']} somtype {st['nr']}"
            if not st.get('somtype'):
                md=f"{BASE}/somtypen/{st['doel']}.md"
                st['somtype']=next((x['somtype'] for x in sections(md) if x['nr']==st['nr']),None) if os.path.exists(md) else None
            velden=[("Hint 1",st['hint1']),("Hint 2",st['hint2']),("Ouderzin",st['ouderzin'])]+[(f"fout-hint {f['bron']}",f['tekst']) for f in st['foutHints']]
            for lab,txt in velden:
                for naam,rx in TAAL:
                    if rx.search(txt or ''): fails.append(f"{tag} [{lab}]: {naam}")
                if re.search(r'volle rij',txt or '',re.I):
                    (info if volle_rij_ok(st['doel'],st.get('somtype')) else fails).append(f"{tag} [{lab}]: 'volle rij'"+(" (elk item heeft een volle rij)" if volle_rij_ok(st['doel'],st.get('somtype')) else " maar niet elk item heeft een volle rij"))
    return fails,info
def regel_checks(txt):
    f=[]
    if m:=LETTER.search(txt): f.append(f"optieletter '{m.group(1)}'")
    if m:=DUBBEL.search(txt): f.append(f"':' + getal ('{txt[max(0,m.start()-12):m.end()+6]}')")
    if '÷' in txt: f.append("'÷'")
    if re.search(r'\d\s?[²³]|\d\s?\^',txt): f.append("macht")
    if re.search(r'(?<![\d.,])\d\.\d{3}(?![\d.,])',txt): f.append("4-cijferig getal met punt")
    if m:=ENGELS.search(txt): f.append(f"Engels woord '{m.group(1)}'")
    if m:=MOEILIJK.search(txt): f.append(f"moeilijk woord '{m.group(1)}' (besluiten_twijfel.md)")
    if re.search(r'×|\d\s*[x*]\s*\d',txt): f.append("'×' (G3: herhaald optellen, geen keerteken)")
    return f
def check(files):
    fails=[];warns=[];info=[];n_klaar=n_open=0
    for p in files:
        doel=os.path.basename(p)[:-3]
        for s in sections(p):
            tag=f"{doel} somtype {s['nr']}"
            if s['status']!="hints klaar": n_open+=1; continue
            n_klaar+=1
            for k,lab in (("h1","Hint 1"),("h2","Hint 2"),("ouder","Ouderzin")):
                if not s[k]: fails.append(f"{tag}: {lab} leeg")
            velden=[("Hint 1",s['h1'] or ""),("Hint 2",s['h2'] or ""),("Ouderzin",s['ouder'] or "")]+[("nieuwe fout-hint",x) for x in s['fh']]
            for lab,txt in velden:
                for x in regel_checks(txt): fails.append(f"{tag} [{lab}]: {x}")
                if re.search(r'=[^=.!?]*=',txt): warns.append(f"{tag} [{lab}]: keten met twee keer '='")
                if re.search(r'\d\s*[+−×-]\s*\d+\s*,\s*\d',txt): warns.append(f"{tag} [{lab}]: kommalijst van sommen (G3: 'en')")
            for lab,txt in velden[:2]:
                for a in s['ant']:
                    if ans_hits(a,txt): fails.append(f"{tag} [{lab}]: antwoord van een voorbeeld ('{a}') staat in de hint")
                andere={a for a in item_answers(doel,s['somtype']) if a not in s['ant'] and ans_hits(a,txt)}
                anker={a for a in andere if a.isdigit() and int(a) in ANKER and re.search(rf'\b(?:naar|tot|bij|via|de|op) {a}\b',txt)}
                for a in sorted(anker): info.append(f"{tag} [{lab}]: anker {a} ('naar/tot/via {a}') is ook het antwoord van een ander item")
                andere-=anker
                if andere: warns.append(f"{tag} [{lab}]: antwoord van ander item ({', '.join(sorted(andere))}) staat in de hint")
                for g in re.findall(r'(?<![\d.,])(?<!op een )\d+(?!\d|[.,]\d)',txt):
                    (info if int(g) in ANKER else warns).append(f"{tag} [{lab}]: getal {g} in de hint")
                for g in re.findall(r'op een (\d)\b',txt):   # eindcijfer ('Eindigt het getal op een 9?'), Didactiek 2026-10-01
                    info.append(f"{tag} [{lab}]: eindcijfer {g} in de hint")
    f2,i2=json_taal(); fails+=f2; info+=i2
    return fails,warns,info,n_klaar,n_open
if __name__=="__main__":
    files=sys.argv[1:] or sorted(glob.glob(f"{BASE}/somtypen/G3-*.md"))
    fails,warns,info,k,o=check(files)
    for x in fails: print("FAIL",x)
    for x in warns: print("WARN",x)
    for x in info: print("INFO",x)
    # Oef-#484 (les 250, 8 okt): ±1-tekst op een sleutel die een getal uit de vraag is (WARN, alle groepen)
    import json as _j250, glob as _g250, os as _o250, sys as _s250; _s250.path.insert(0, '/workspace/claude-merge/tools'); import les250_check as _L250
    for _w in _L250.treffers([_it for _p in sorted(_g250.glob(_o250.path.join(_o250.path.dirname(_o250.path.abspath(__file__)), 'data', 'per_doel', '*.json'))) for _it in _j250.load(open(_p))['items']]):
        warns.append('LES250 ' + _w); print('WARN LES250', _w)
    print(f"Somtypen: {k} hints klaar · {o} open · {len(fails)} FAIL · {len(warns)} WARN · {len(info)} INFO (anker 10/20/100, eindcijfer, volle rij gecheckt) · {'ALLES OK' if not fails else 'FAIL'}")
    sys.exit(1 if fails else 0)
