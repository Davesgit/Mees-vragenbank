#!/usr/bin/env python3
"""Check op de hints van de G4-merge (somtypen/G4-*.md), 1 okt 2026 (Oefeningen, batch 1).
Basis: de G4-kopie van g3/check_hints.py die Overzicht om 14:15 neerzette (kopie: /tmp/g4_batch1_1419/check_hints.py),
uitgebreid met de G4-regels uit de opdracht en de lessen van Didactiek uit G3.
Per '## Somtype n' met 'Status: hints klaar':
  FAIL  Hint 1, Hint 2 of Ouderzin leeg; somtype zonder sleutel (nrOrigineel/somtypeOrigineel).
  FAIL  optieletter (A/B/C/D als los woord) in Hint 1, Hint 2, Ouderzin of een nieuwe fout-hint (de app husselt opties).
  FAIL  G4-notatie in alle kindteksten:
        ':' direct voor een getal, behalve 'a : b' (deelteken met spaties) en 'woord: getal' ('Reken uit: 4 × 7'); kloktijd u:mm = INFO
        '÷' · machten (², ³, ^) · '-' of '–' tussen getallen (moet '−') · 'x' of '*' als keerteken (moet '×')
        4-cijferig getal met punt (1.000) · een som met '=' die niet klopt (ook elke '=' in een kettingsom).
  INFO  '×' buiten de tafel-/keerdoelen (mag in G4).
  FAIL  Engelse woorden · moeilijke woorden (besluiten_twijfel.md + G4-fixes W5: robots, astronauten, dino-namen, keepers …;
        'vermenigvuldigen', 'voertuig', 'bewerking', 'afronden' …). 'spiegel' mag (G4-MKU-E05), 'patroon' mag.
  FAIL  taalregels Didactiek (over ALLE teksten in hints/batch*.json, ook Claude-fout-hints 'ok'):
        'tiental naast/ernaast' · 'er gaan/komen er weg/uit/bij' zonder getal · 'er komt/gaat bij/weg' zonder 'iets' ·
        scheidbare werkwoorden los geschreven ('terug gegaan', 'bij gedaan', 'op geteld' …) · 'isgelijkteken' ·
        'volle rij' als niet elk item van het somtype een volle rij heeft.
  FAIL  het antwoord van een voorbeeld staat in Hint 1 of Hint 2; een anker ('via/naar/tot 10') dat bij een ander item het antwoord is.
  FAIL  een Claude-tekst die vervangen is (claudeVervangen/claudeTekst) staat weer als kindtekst in de data (terugval)
  INFO  maat-anker zoals '(1 kg)' als het getal bij geen item (deel van) het antwoord is
  WARN  het antwoord van een ander item van dit somtype staat in Hint 1/2 · een getal in Hint 1/2 (10, 20, 100 als anker = INFO)
        · kommalijst van sommen ('3 + 4, 5 + 2') · een kleurnaam (de app laat kleuren misschien niet zien; het werkwoord 'kleuren' telt niet mee, G4-GET-M06).
  Per item (data/per_doel/<doel>.json, alle items van het somtype; dit is wat het kind ziet):
  FAIL  item zonder fout-hint · plaatshouder in een fout-hint · taal- en notatieregels hierboven op elke fout-hint (ook Claude per item)
        · een fout-hint die 'te veel' zegt bij een te laag antwoord, of 'te weinig'/'tel verder'/'tel door' bij een te hoog antwoord
        · het antwoord staat in de fout-hint.
  WARN  claudeUitleg staat in een kindtekst (controle.claudeUitlegInKindtekst).
Somtypes zonder 'hints klaar' tellen als 'open'.
Gebruik: python3 check_hints.py [bestand.md ...]   (standaard alle somtypen/G4-*.md) · exit 1 bij FAIL.
"""
import re,sys,os,glob,json
import sys as _sys113; _sys113.path.insert(0, '/workspace/claude-merge/tools'); import klok113_check as _K113
BASE=os.path.dirname(os.path.abspath(__file__))
LETTER=re.compile(r"(?<![\w'’/.-])([A-D])(?![\w'’/-])")
KLOK=re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
ENGELS=re.compile(r"\b(scaffold\w*|hints?|tip of the|step|count|next|answer|okay|oké|ok|cool|sorry|level|game|nice|wow|yes|please|great|good job|well done)\b",re.I)
ANKER={10,20,100}
MAAT_ANKER=re.compile(r' ?(?:kg|g|m|cm|L|liter)\b')   # '(1 kg)': maat-anker, alleen INFO als het getal bij geen item (deel van) het antwoord is (Didactiek b4 v1, 1.3)
MOEILIJK=re.compile(r'\b(kitten\w*|maanste\w*|ruimtepak\w*|schroef\w*|schroeven|zonnepane\w*|satelliet\w*|astronaut\w*|robot\w*|keeper\w*|\w*saurus\w*|zeshoek\w*|vijfhoek\w*|ruit|vermenigvuldig\w*|voertuig\w*|zaagsnede\w*|combinatie\w*|bewerking\w*|afrond\w*|naar boven af)\b',re.I)
KEER_DOELEN={'G4-GET-M06','G4-GET-E06','G4-GET-E07','G4-GET-E08','G4-GET-E09','G4-VERH-E03','G4-VERH-E04'}
# Alleen kleurnamen tellen (batch 3, 15:05): het werkwoord 'kleur/kleuren/gekleurd' hoort bij G4-GET-M06 (rooster kleuren) en is geen kleur.
KLEUR=re.compile(r'\b(rood|rode|blauw\w*|groen\w*|geel|gele|paars\w*|oranje|roze)\b',re.I)
def sections(p):
    cur=None; out=[]
    for l in open(p,encoding='utf-8').read().split("\n"):
        m=re.match(r'^## Somtype (\d+): (.*)$',l)
        if m: cur={"nr":int(m.group(1)),"somtype":m.group(2).strip(),"ant":[],"fh":[],"h1":None,"h2":None,"ouder":None,"status":None,"sleutel":None}; out.append(cur); continue
        if cur is not None and (mm:=re.match(r'^- Sleutel: nrOrigineel \*\*(\d+)\*\* · somtypeOrigineel “(.*)”',l)): cur["sleutel"]=(int(mm.group(1)),mm.group(2)); continue
        if l.startswith("## ") or l.startswith("---"): cur=None; continue
        if cur is None: continue
        if m:=re.match(r'^\s+- \*\*Antwoord:\*\*\s*(.*?)\s*(\(controle.*)?$',l): cur["ant"].append(m.group(1).strip())
        elif m:=re.match(r'^- \*\*Hint 1(?: \(te schrijven\))?:\*\*\s?(.*)$',l): cur["h1"]=m.group(1).strip()
        elif m:=re.match(r'^- \*\*Hint 2(?: \(te schrijven\))?:\*\*\s?(.*)$',l): cur["h2"]=m.group(1).strip()
        elif m:=re.match(r'^- \*\*Ouderzin:\*\*\s?(.*)$',l): cur["ouder"]=m.group(1).strip()
        elif m:=re.match(r'^\s+- (?:`[^`]*` )?\(.*?\) → (.*?)\s+\[(?:nieuw|Claude, taalfix)\]$',l): cur["fh"].append(m.group(1))
        elif m:=re.match(r'^- Status:\s*(.*)$',l): cur["status"]=m.group(1).strip()
    return out
_ITEMS={}
def items_van(doel,somtype):
    if doel not in _ITEMS:
        p=f"{BASE}/data/per_doel/{doel}.json"
        _ITEMS[doel]=json.load(open(p,encoding='utf-8'))['items'] if os.path.exists(p) else []
    return [it for it in _ITEMS[doel] if it['merge']['somtype']==somtype]
def item_answers(doel,somtype): return [it['antwoord'] for it in items_van(doel,somtype)]
def norm(s): return re.sub(r'\s+',' ',s.replace('−','-')).strip()
def ans_hits(ant,txt):
    t=norm(txt); a=norm(str(ant))
    if re.fullmatch(r'\d+',a): return bool(re.search(rf'(?<![\d.,]){a}(?!\d|[.,]\d)',t))
    if '|' in a: return a.replace('|',' ') in t or ', '.join(a.split('|')) in t
    return len(a)>2 and a in t
TAAL=[("'tiental naast/ernaast' (klopt vaak niet; zeg 'te veel' of 'te weinig')",re.compile(r'tiental (?:er)?naast',re.I)),
      ("'er gaan/komen er …' zonder getal ('Er gaan dingen weg')",re.compile(r'\b[Ee]r (?:gaan|komen|gaat|komt) er (?:weg|uit|bij|af|eraf|erbij)\b')),
      ("'er komt/gaat …' zonder 'iets' ('Er komt iets bij')",re.compile(r'\b[Ee]r (?:komt|gaat) (?:bij|weg|uit|af)\b')),
      ("spelling scheidbaar werkwoord (aan elkaar: 'teruggegaan', 'bijgedaan', 'opgeteld')",re.compile(r'\b(?:terug|bij|weg|af|door|op|uit|mee|om|over) ge(?:teld|daan|gaan|haald|komen|sprongen|draaid|zet|legd)\b',re.I)),
      ("#102: 'erbij'/'eraf' + werkwoord los ('erbij geteld', 'eraf gehaald'; niet 'erbijgeteld')",re.compile(r'\ber(?:bij|af)ge(?:teld|daan|gaan|haald|komen|sprongen|draaid|zet|legd)\b',re.I)),
      ("spelling 'uitgaan'",re.compile(r'\buit gaan\b',re.I)),("spelling 'bijkomen'",re.compile(r'\bbij komen\b',re.I)),
      ("'isgelijkteken' (niet 'is-teken', 'is gelijk teken', 'gelijkteken')",re.compile(r'is-teken|is gelijk ?-?teken|is-gelijk-?teken|isgelijk-teken|(?<!is)gelijkteken',re.I))]
def volle_rij_ok(doel,somtype):
    its=items_van(doel,somtype)
    def ok(it):
        jr=((it.get('visual') or {}).get('jsRender') or {})
        return isinstance(jr.get('aantal'),int) and isinstance(jr.get('perrij'),int) and jr['aantal']>=jr['perrij']
    return bool(its) and all(ok(it) for it in its)
def _patroon(t):
    t=(t or '').strip()
    if len(re.sub(r'[…\s.]','',t))<15: return None
    return re.compile(re.escape(t).replace(re.escape('…'),'.+?').replace('…','.+?')+r'$')
def terugval():
    """FAIL als een Claude-tekst die vervangen is (claudeVervangen / claudeTekst) weer als kindtekst in de data staat (ronde 4b: M05 #4)."""
    fails=[]; pat={}
    for p in sorted(glob.glob(f"{BASE}/hints/batch*.json")):
        for st in json.load(open(p,encoding='utf-8'))['somtypen']:
            huidig={f['tekst'] for f in st['foutHints']}|{st.get('hint1'),st.get('hint2'),st.get('ouderzin')}
            oud={v.get('claudeTekst') for v in st.get('claudeVervangen') or []}|{f.get('claudeTekst') for f in st['foutHints']}
            pat[(st['doel'],st['nrOrigineel'])]=[(t,r) for t in oud-huidig-{None} if (r:=_patroon(t))]
    for f in sorted(glob.glob(f"{BASE}/data/per_doel/*.json")):
        for it in json.load(open(f,encoding='utf-8'))['items']:
            P=pat.get((it['merge']['doel'],it['merge'].get('somtypeNrOrigineel')))
            if not P: continue
            teksten=[('hint',it.get('hint')),('sterkereHint',it.get('sterkereHint'))]+[(f"fout {h['fout']}",h['uitleg']) for h in it.get('foutHints') or []]
            for lab,txt in teksten:
                for t,r in P:
                    if txt and r.match(txt.strip()): fails.append(f"{it['merge']['doel']} #{it['merge']['somtypeNrOrigineel']} item {it['nr']} [{lab}]: vervangen Claude-tekst staat terug ('{txt[:60]}')")
    return fails
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
                    vr=volle_rij_ok(st['doel'],st.get('somtype'))
                    (info if vr else fails).append(f"{tag} [{lab}]: 'volle rij'"+(" (elk item heeft een volle rij)" if vr else " maar niet elk item heeft een volle rij"))
    return fails,info
# --- rekenen: elke '=' moet kloppen ---
NUM=r'\d+(?:,\d+)?'
EXPR=rf'{NUM}(?:\s*[+−×:-]\s*{NUM})*'
KETEN=re.compile(rf'(?<![\d,□])({EXPR})((?:\s*=\s*{EXPR})+)(?![\d,]|\s*[+−×:-]\s*\d)')
def evalueer(e):
    e=e.replace('−','-').replace('×','*').replace(':','/').replace(',','.')
    if not re.fullmatch(r'[\d.\s+\-*/]+',e): return None
    try: return eval(e)
    except Exception: return None
def keten_fouten(txt):
    out=[]
    t=KLOK.sub(' ',txt)
    for m in KETEN.finditer(t):
        if re.search(r'[□#\d]\s*[+−×:-]\s*$',t[:m.start()]): continue   # deel van een som met □ ('□ × 2 = 6')
        delen=[m.group(1)]+re.split(r'\s*=\s*',m.group(2).strip())[1:]
        waarden=[evalueer(d) for d in delen]
        if None in waarden: continue
        if any(abs(w-waarden[0])>1e-9 for w in waarden): out.append(f"som klopt niet: '{m.group(0).strip()}'")
    return out
def dubbelepunt(txt):
    t=KLOK.sub('', txt)
    for m in re.finditer(r':(\s*)(?:€\s?)?\d',t):
        voor=t[:m.start()]; sp=m.group(1)
        if sp==' ' and re.search(r'\d $',voor): continue          # 'a : b' (deelteken)
        if sp==' ' and re.search(r'[A-Za-zÀ-ÿ)]$',voor): continue   # 'Reken uit: 4 × 7'
        return t[max(0,m.start()-12):m.end()+6]
    return None
def regel_checks(txt,doel=''):
    f=[]
    if m:=LETTER.search(txt): f.append(f"optieletter '{m.group(1)}'")
    if (d:=dubbelepunt(txt)): f.append(f"':' + getal ('{d}')")
    if '÷' in txt: f.append("'÷' (G4: 'a : b')")
    if re.search(r'\d\s?[²³]|\d\s?\^',txt): f.append("macht")
    if re.search(r'(?<![\d.,])\d\.\d{3}(?![\d.,])',txt): f.append("4-cijferig getal met punt")
    if re.search(r'[\d□]\s*[-–]\s*[\d□]',txt): f.append("'-' tussen getallen (moet '−')")
    if re.search(r'\d\s*[x*]\s*\d',txt): f.append("'x' of '*' als keerteken (moet '×')")
    if m:=ENGELS.search(txt): f.append(f"Engels woord '{m.group(1)}'")
    if m:=MOEILIJK.search(txt): f.append(f"moeilijk woord '{m.group(1)}'")
    f+=keten_fouten(txt)
    return f
TE_HOOG=re.compile(r'\bte veel\b|\bte hoog\b|\bte ver naar rechts\b|\bte groot\b',re.I)
TE_LAAG=re.compile(r'\bte weinig\b|\bte laag\b|\btel (?:nog )?(?:verder|door)\b|\bverder tellen\b|\bdoortellen\b|\bte ver naar links\b|\bte klein\b',re.I)
def _int(v):
    v=str(v).strip(); return int(v) if re.fullmatch(r'\d+',v) else None
def item_checks(doel,somtype,tag):
    fails=[];warns=[]
    for it in items_van(doel,somtype):
        t=f"{tag} item {it['nr']}"
        fh=it.get('foutHints') or []
        warns+=_K113.check113(it,t,fh,items_van(doel,somtype))      # #113 (Didactiek 19:42): kijkt naar alle tijden van het somtype; INFO via _K113.pop_info()
        if not fh: fails.append(f"{t}: geen fout-hint")
        a=_int(it['antwoord'])
        for f in fh:
            u=f.get('uitleg') or ''
            if 'TEKST NODIG' in u or not u.strip(): fails.append(f"{t} [{f['fout']}]: plaatshouder of lege tekst")
            for naam,rx in TAAL:
                if rx.search(u): fails.append(f"{t} [{f['fout']}]: {naam}")
            for x in regel_checks(u,doel): fails.append(f"{t} [{f['fout']}]: {x}")
            v=_int(f['fout'])
            if a is not None and v is not None:
                if v<a and TE_HOOG.search(u) and not TE_LAAG.search(u): fails.append(f"{t} [{f['fout']}]: zegt 'te veel', maar {v} is lager dan het antwoord")
                if v>a and TE_LAAG.search(u) and not TE_HOOG.search(u): fails.append(f"{t} [{f['fout']}]: zegt 'te weinig/tel verder', maar {v} is hoger dan het antwoord")
            if ans_hits(it['antwoord'],u): fails.append(f"{t} [{f['fout']}]: het antwoord ('{it['antwoord']}') staat in de fout-hint")
        if (it.get('controle') or {}).get('claudeUitlegInKindtekst'): warns.append(f"{t}: claudeUitleg in kindtekst {it['controle']['claudeUitlegInKindtekst']}")
    return fails,warns
def check(files):
    fails=[];warns=[];info=[];n_klaar=n_open=0
    for p in files:
        doel=os.path.basename(p)[:-3]
        for s in sections(p):
            tag=f"{doel} somtype {s['nr']}"
            if not s['sleutel']: fails.append(f"{tag}: geen sleutel (nrOrigineel/somtypeOrigineel)")
            if s['status']!="hints klaar": n_open+=1; continue
            n_klaar+=1
            for k,lab in (("h1","Hint 1"),("h2","Hint 2"),("ouder","Ouderzin")):
                if not s[k]: fails.append(f"{tag}: {lab} leeg")
            velden=[("Hint 1",s['h1'] or ""),("Hint 2",s['h2'] or ""),("Ouderzin",s['ouder'] or "")]+[("nieuwe fout-hint",x) for x in s['fh']]
            for lab,txt in velden:
                for x in regel_checks(txt,doel): fails.append(f"{tag} [{lab}]: {x}")
                if re.search(r'×',txt) and doel not in KEER_DOELEN: info.append(f"{tag} [{lab}]: '×' buiten een keerdoel (mag in G4)")
                if KLOK.search(txt): info.append(f"{tag} [{lab}]: kloktijd '{KLOK.search(txt).group(0)}'")
                if re.search(r'\d\s*[+−×-]\s*\d+\s*,\s*\d',txt): warns.append(f"{tag} [{lab}]: kommalijst van sommen (schrijf 'en')")
                if m:=KLEUR.search(txt): warns.append(f"{tag} [{lab}]: kleur '{m.group(1)}' (de app laat kleuren misschien niet zien)")
                if re.search(r'=[^=.!?]*=',txt): info.append(f"{tag} [{lab}]: kettingsom (elke '=' nagerekend)")
            alle=item_answers(doel,s['somtype'])
            for lab,txt in velden[:2]:
                for a in s['ant']:
                    if ans_hits(a,txt): fails.append(f"{tag} [{lab}]: antwoord van een voorbeeld ('{a}') staat in de hint")
                andere={a for a in alle if a not in s['ant'] and ans_hits(a,txt)}
                anker={a for a in andere if str(a).isdigit() and int(a) in ANKER and re.search(rf'\b(?:naar|tot|bij|via|de|op) {a}\b',txt)}
                for a in sorted(anker): fails.append(f"{tag} [{lab}]: anker {a} ('naar/tot/via {a}') is bij een ander item het antwoord")
                andere-=anker
                if andere: warns.append(f"{tag} [{lab}]: antwoord van ander item ({', '.join(sorted(map(str,andere)))}) staat in de hint")
                ant_getallen={int(x) for a in alle for x in re.findall(r'\d+',str(a))}
                for m in re.finditer(r'(?<![\d.,])(?<!op een )(\d+)(?!\d|[.,]\d)',txt):
                    g=m.group(1)
                    if int(g) in ANKER: info.append(f"{tag} [{lab}]: getal {g} in de hint")
                    elif MAAT_ANKER.match(txt,m.end()) and int(g) not in ant_getallen: info.append(f"{tag} [{lab}]: maat-anker '{g}{MAAT_ANKER.match(txt,m.end()).group(0)}' (nooit (deel van) het antwoord)")
                    else: warns.append(f"{tag} [{lab}]: getal {g} in de hint")
                for g in re.findall(r'op een (\d)\b',txt):
                    info.append(f"{tag} [{lab}]: eindcijfer {g} in de hint")
            f2,w2=item_checks(doel,s['somtype'],tag); fails+=f2; warns+=w2; info+=_K113.pop_info()
            w3,i3=_K113.check113_somtype(tag,s,items_van(doel,s['somtype'])); warns+=w3; info+=i3   # #113 Hint 1/2/Ouderzin
    f2,i2=json_taal(); fails+=f2; info+=i2
    fails+=terugval()
    return fails,warns,info,n_klaar,n_open
if __name__=="__main__":
    files=sys.argv[1:] or sorted(glob.glob(f"{BASE}/somtypen/G4-*.md"))
    fails,warns,info,k,o=check(files)
    for x in fails: print("FAIL",x)
    for x in warns: print("WARN",x)
    for x in info: print("INFO",x)
    # Oef-#484 (les 250, 8 okt): ±1-tekst op een sleutel die een getal uit de vraag is (WARN, alle groepen)
    import json as _j250, glob as _g250, os as _o250, sys as _s250; _s250.path.insert(0, '/workspace/claude-merge/tools'); import les250_check as _L250
    for _w in _L250.treffers([_it for _p in sorted(_g250.glob(_o250.path.join(_o250.path.dirname(_o250.path.abspath(__file__)), 'data', 'per_doel', '*.json'))) for _it in _j250.load(open(_p))['items']]):
        warns.append('LES250 ' + _w); print('WARN LES250', _w)
    print(f"Somtypen: {k} hints klaar · {o} open · {len(fails)} FAIL · {len(warns)} WARN · {len(info)} INFO · {'ALLES OK' if not fails else 'FAIL'}")
    sys.exit(1 if fails else 0)
