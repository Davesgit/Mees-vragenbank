#!/usr/bin/env python3
"""Check op de hints van de G6-merge (somtypen/G6-*.md). G6-versie (Overzicht, 1 okt) van g5/check_hints.py, dat de G5-versie is van
g4/check_hints.py (Oefeningen, stand 15:05). Verschil met G5: '×' en 'a : b' (deelteken) mogen overal, breuken n/m mogen, kommagetallen
mogen (3 of meer cijfers achter de komma = FAIL: G7). Nieuw FAIL in G6: procent ('%', 'procent': G7), 'a : b' als verhouding of schaal
('schaal 1 : 100', besluit Dave: pas in G7 Verhoudingen) en een ketensom die doorrekent na '=' ('7 × 4 = 28 + 12': voluit
'7 × 4 = 28 en 28 + 12 = 40'). WARN bij een getal boven 100.000 (G6-bereik).
Origineel G4:
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
  WARN  (G6) een getal boven 100.000 in een hint · FAIL getal vanaf 10.000 zonder punt
  WARN  het antwoord van een ander item van dit somtype staat in Hint 1/2 · een getal in Hint 1/2 (10, 20, 100 als anker = INFO)
        · kommalijst van sommen ('3 + 4, 5 + 2') · een kleurnaam (de app laat kleuren misschien niet zien; het werkwoord 'kleuren' telt niet mee, G4-GET-M06).
  Per item (data/per_doel/<doel>.json, alle items van het somtype; dit is wat het kind ziet):
  FAIL  item zonder fout-hint · plaatshouder in een fout-hint · taal- en notatieregels hierboven op elke fout-hint (ook Claude per item)
        · een fout-hint die 'te veel' zegt bij een te laag antwoord, of 'te weinig'/'tel verder'/'tel door' bij een te hoog antwoord
        · het antwoord staat in de fout-hint.
  WARN  claudeUitleg staat in een kindtekst (controle.claudeUitlegInKindtekst).
Somtypes zonder 'hints klaar' tellen als 'open'.
Gebruik: python3 check_hints.py [bestand.md ...]   (standaard alle somtypen/G6-*.md) · exit 1 bij FAIL.
"""
import re,sys,os,glob,json,collections
import sys as _sys113; _sys113.path.insert(0, '/workspace/claude-merge/tools'); import klok113_check as _K113
BASE=os.path.dirname(os.path.abspath(__file__))
LETTER=re.compile(r"(?<![\w'’/.-])([A-D])(?![\w'’/-])")
KLOK=re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
ENGELS=re.compile(r"\b(scaffold\w*|hints?|tip of the|step|count|next|answer|okay|oké|ok|cool|sorry|level|game|nice|wow|yes|please|great|good job|well done)\b",re.I)
ANKER={10,20,100}
MOEILIJK=re.compile(r'\b(kitten\w*|maanste\w*|ruimtepak\w*|schroef\w*|schroeven|zonnepane\w*|satelliet\w*|astronaut\w*|robot\w*|keeper\w*|\w*saurus\w*|zeshoek\w*|vijfhoek\w*|ruit|vermenigvuldig\w*|voertuig\w*|zaagsnede\w*|combinatie\w*|bewerking\w*)\b',re.I)
VERH=re.compile(r'(verhouding|schaal|staat tot|mengen|mengsel)[^.?!]*\d\s*:\s*\d|\d\s*:\s*\d[^.?!]*(verhouding|schaal)',re.I)
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
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+',a):      # 204.245: ook als 204245 geschreven, en niet als deel van 1.204.245
        return any(re.search(rf'(?<![\d.,]){re.escape(v)}(?!\d|[.,]\d)',t) for v in (a,a.replace('.','')))
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
    if '÷' in txt: f.append("'÷' (G6: 'a : b')")
    if re.search(r'(?<![\d,])\d+,\d{3,}(?!\d)',txt): f.append("kommagetal met 3 of meer cijfers achter de komma (G7)")
    if re.search(r'%|\bprocent\b',txt,re.I): f.append("procent (G7)")
    if VERH.search(KLOK.sub('',txt)): f.append("'a : b' als verhouding of schaal (pas in G7)")
    if re.search(r'[\d□]\s*[+−×:]\s*[\d□]+\s*=\s*\d+\s*[+−×:]\s*[\d□]+\s*=',txt): f.append("ketensom niet voluit ('a × b = c en c + d = e')")
    if re.search(r'\d\s?[²³]|\d\s?\^',txt): f.append("macht")
    if re.search(r'(?<![\d.,])\d\.\d{3}(?!\d|[.,]\d)',txt): f.append("4-cijferig getal met punt")
    if re.search(r'(?<![\d.,])\d{5,}(?![\d,])',txt): f.append("getal vanaf 10.000 zonder punt")
    if re.search(r'[\d□]\s*[-–]\s*[\d□]',txt): f.append("'-' tussen getallen (moet '−')")
    if re.search(r'\d\s*[x*]\s*\d',txt): f.append("'x' of '*' als keerteken (moet '×')")
    if m:=ENGELS.search(txt): f.append(f"Engels woord '{m.group(1)}'")
    if m:=MOEILIJK.search(txt): f.append(f"moeilijk woord '{m.group(1)}'")
    f+=keten_fouten(txt)
    return f
TE_HOOG=re.compile(r'\bte veel\b|\bte hoog\b|\bte ver naar rechts\b|\bte groot\b',re.I)
TE_LAAG=re.compile(r'\bte weinig\b|\bte laag\b|\btel (?:nog )?(?:verder|door)\b|\bverder tellen\b|\bdoortellen\b|\bte ver naar links\b|\bte klein\b',re.I)
GETAL=r'\d{1,3}(?:\.\d{3})+|\d+'      # ook getallen met punt (10.000, 99.999): de itemchecks rekenen ermee (Dave 20:38 #2; de grens blijft 100.000, Dave 20:49)
def _int(v):
    v=str(v).strip(); return int(v.replace('.','')) if re.fullmatch(GETAL,v) else None
def _waarde(v):
    """#44: heel getal, of een geldbedrag in centen ('€8,80' → 880, '€4' → 400); anders None."""
    v=str(v).strip()
    if re.fullmatch(GETAL,v): return int(v.replace('.',''))
    m=re.fullmatch(r'€\s?(\d+)(?:,(\d{1,2}))?',v)
    return int(m.group(1))*100+(int(m.group(2).ljust(2,'0')) if m.group(2) else 0) if m else None
def _richting(t,a,v,u,wat):
    out=[]
    if v<a and TE_HOOG.search(u) and not TE_LAAG.search(u): out.append(f"{t} [{wat}]: zegt 'te veel', maar de fout is lager dan het antwoord")
    if v>a and TE_LAAG.search(u) and not TE_HOOG.search(u): out.append(f"{t} [{wat}]: zegt 'te weinig/tel verder', maar de fout is hoger dan het antwoord")
    return out
def item_checks(doel,somtype,tag):
    fails=[];warns=[]
    for it in items_van(doel,somtype):
        t=f"{tag} item {it['nr']}"
        fh=it.get('foutHints') or []
        warns+=_K113.check113(it,t,fh,items_van(doel,somtype))      # #113 (Didactiek 19:42): kijkt naar alle tijden van het somtype; INFO via _K113.pop_info()
        if not fh: fails.append(f"{t}: geen fout-hint")
        a=_waarde(it['antwoord']) if str(it['antwoord']).startswith('€') else _int(it['antwoord'])
        # #44: 'andere fout'-regel zonder algemeneFoutHint
        if any((r.get('match') or {}).get('alles') for r in it.get('foutRegels') or []) and not it.get('algemeneFoutHint'):
            fails.append(f"{t}: het somtype heeft een 'andere fout'-regel, maar het item heeft geen algemeneFoutHint")
        # #44: richting bij de regels zelf (vanaf / totEnMet / kleinerDan / waarden), ook voor invoer die geen sleutel is
        if a is not None:
            # de regels gelden van boven naar beneden: een waarde die een hogere regel al vangt, telt bij een lagere regel niet mee
            def gevangen(x, hoger):
                for mh in hoger:
                    if mh.get('alles'): return True
                    if 'vanaf' in mh and isinstance(mh['vanaf'],int) and x>=mh['vanaf']: return True
                    if 'totEnMet' in mh and isinstance(mh['totEnMet'],int) and x<=mh['totEnMet']: return True
                    if 'kleinerDan' in mh and isinstance(mh['kleinerDan'],int) and x<mh['kleinerDan']: return True
                    if x in mh.get('_w',()): return True
                return False
            hoger=[]
            for r in it.get('foutRegels') or []:
                mt=dict(r.get('match') or {}); u=r.get('tekst') or ''
                ww=[(w,_waarde(w) if str(it['antwoord']).startswith('€') else _int(w)) for w in mt.get('waarden') or []]
                mt['_w']={vw for _,vw in ww if vw is not None}
                if ww: mt_w=[(w,vw) for w,vw in ww if vw is not None and not gevangen(vw,hoger)]
                else: mt_w=[]
                hoger.append(mt)
                if 'vanaf' in mt and isinstance(mt['vanaf'],int) and mt['vanaf']>a: fails+=_richting(t,a,mt['vanaf'],u,f"regel '{r['regel']}'")
                for k in ('totEnMet','kleinerDan'):
                    if k in mt and isinstance(mt[k],int) and mt[k]<=a: fails+=_richting(t,a,mt[k] if mt[k]<a else a-1,u,f"regel '{r['regel']}'")
                for w,vw in mt_w:
                    if vw!=a: fails+=_richting(t,a,vw,u,f"regel '{r['regel']}' {w}")
        for f in fh:
            u=f.get('uitleg') or ''
            if 'TEKST NODIG' in u or not u.strip(): fails.append(f"{t} [{f['fout']}]: plaatshouder of lege tekst")
            for naam,rx in TAAL:
                if rx.search(u): fails.append(f"{t} [{f['fout']}]: {naam}")
            for x in regel_checks(u,doel): fails.append(f"{t} [{f['fout']}]: {x}")
            v=_waarde(f['fout']) if str(it['antwoord']).startswith('€') else _int(f['fout'])
            if a is not None and v is not None: fails+=_richting(t,a,v,u,f['fout'])
            if ans_hits(it['antwoord'],u): fails.append(f"{t} [{f['fout']}]: het antwoord ('{it['antwoord']}') staat in de fout-hint")
        if (it.get('controle') or {}).get('claudeUitlegInKindtekst'): warns.append(f"{t}: claudeUitleg in kindtekst {it['controle']['claudeUitlegInKindtekst']}")
    return fails,warns
def hint_koppeling():
    """merge-fixlijst #30 (Didactiek batch 2, 1 okt 16:50): FAIL bij elk probleem in logs/hint_sleutels.json, bij een log die ouder is dan
    data/gemapt.json (sync niet gedraaid), en (los van de log) bij twee of meer hint-entries op dezelfde kop of een entry waarvan nr/kop niet in de md staat."""
    fails=[]; lp=f"{BASE}/logs/hint_sleutels.json"; gp=f"{BASE}/data/gemapt.json"
    if not os.path.exists(lp): return ["hint-koppeling: logs/hint_sleutels.json ontbreekt (draai scripts/sync_hint_keys.py)"]
    import hashlib
    L=json.load(open(lp)); its=json.load(open(gp))['items']
    nu=hashlib.md5(json.dumps(sorted((it['bron']['claudeId'],it['merge']['doel'],it['merge']['somtype']) for it in its),ensure_ascii=False).encode()).hexdigest()
    if L.get('indeling')!=nu: fails.append("hint-koppeling: logs/hint_sleutels.json hoort niet bij de somtype-indeling in data/gemapt.json (draai scripts/sync_hint_keys.py na de build)")
    for x in L.get('problemen',[]): fails.append(f"hint-koppeling (logs/hint_sleutels.json): {x}")
    per=collections.defaultdict(list); alle_e=[]
    import sys as _s; _s.path.insert(0,f"{BASE}/scripts"); import koppeling_merge as KM      # ronde 9 (#235)
    for b in sorted(glob.glob(f"{BASE}/hints/batch*.json")):
        for st in json.load(open(b,encoding='utf-8')).get('somtypen',[]):
            alle_e.append(st)
            if KM.speciaal(st): continue      # samengevoegd (hints/koppeling_merge.json)
            per[(st['doel'],st.get('somtype'))].append(f"{os.path.basename(b)}#{st.get('nrOrigineel')}")
            mp=f"{BASE}/somtypen/{st['doel']}.md"
            K={m.group(2).strip():int(m.group(1)) for m in re.finditer(r'^## Somtype (\d+): (.*)$',open(mp,encoding='utf-8').read(),re.M)} if os.path.exists(mp) else {}
            if K.get(st.get('somtype'))!=st.get('nr'): fails.append(f"hint-koppeling: {os.path.basename(b)} {st['doel']} nr {st.get('nr')} '{st.get('somtype')}' staat zo niet in somtypen/{st['doel']}.md")
    kp,_ki=KM.controleer(alle_e); fails+=[f"hint-koppeling (koppeling_merge.json): {x}" for x in kp]
    for (d,k),w in per.items():
        if len(w)>1: fails.append(f"hint-koppeling: {d} '{k}': {len(w)} hint-entries ({', '.join(w)}); nooit stil samenvoegen")
    return fails
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
                if KLOK.search(txt): info.append(f"{tag} [{lab}]: kloktijd '{KLOK.search(txt).group(0)}'")
                if re.search(r'\d\s*[+−×-]\s*\d+\s*,\s*\d',txt): warns.append(f"{tag} [{lab}]: kommalijst van sommen (schrijf 'en')")
                if m:=KLEUR.search(txt): warns.append(f"{tag} [{lab}]: kleur '{m.group(1)}' (de app laat kleuren misschien niet zien)")
                if re.search(r'=[^=.!?]*=',txt): info.append(f"{tag} [{lab}]: kettingsom (elke '=' nagerekend)")
                for g in re.findall(r'(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d,])|(?<![\d.,])\d{4,}(?![\d.,])',txt):
                    if int(g.replace('.',''))>100000: warns.append(f"{tag} [{lab}]: getal {g} boven het G6-bereik (tot 100.000)")
            alle=item_answers(doel,s['somtype'])
            for lab,txt in velden[:2]:
                for a in s['ant']:
                    if ans_hits(a,txt): fails.append(f"{tag} [{lab}]: antwoord van een voorbeeld ('{a}') staat in de hint")
                andere={a for a in alle if a not in s['ant'] and ans_hits(a,txt)}
                anker={a for a in andere if _int(a) is not None and _int(a) in ANKER and re.search(rf'\b(?:naar|tot|bij|via|de|op) {re.escape(str(a))}\b',txt)}
                for a in sorted(anker): fails.append(f"{tag} [{lab}]: anker {a} ('naar/tot/via {a}') is bij een ander item het antwoord")
                andere-=anker
                if andere: warns.append(f"{tag} [{lab}]: antwoord van ander item ({', '.join(sorted(map(str,andere)))}) staat in de hint")
                for g in re.findall(r'(?<![\d.,])(?<!op een )(?:\d{1,3}(?:\.\d{3})+|\d+)(?!\d|[.,]\d)',txt):   # ook getallen met punt (10.000 … 100.000)
                    # G5 ronde 1b (Didactiek S1), overgenomen in G6–G8 (G6-fixlijst #5, besluit Dave 19:58): het afrondcijfer 5 in 'Is het 5 of meer'
                    # is een cijfer, geen getal (WARN alleen als 5 ergens het antwoord is)
                    if g=='5' and re.search(r'\bIs het 5 of meer\b',txt) and '5' not in {str(a) for a in alle}:
                        info.append(f"{tag} [{lab}]: afrondcijfer 5 ('Is het 5 of meer')"); continue
                    # G6 merge-fixlijst #157 (Oefeningen 20:27, letterlijke tekst van Didactiek S6): een drempel 'meer dan 1' en een getal in een
                    # voorbeeldzin 'Zo is …' zijn INFO, als het getal geen antwoord is en in geen antwoord van het somtype voorkomt
                    _alle_t = {str(a).replace('.', '') for a in alle}
                    if g=='1' and re.search(r'\b(?:meer|minder|groter|kleiner) dan 1\b',txt) and '1' not in _alle_t:
                        info.append(f"{tag} [{lab}]: drempel 1 ('meer dan 1', #157)"); continue
                    if any(re.search(rf'(?<![\d.,]){re.escape(g)}(?![\d]|[.,]\d)', z) for z in re.findall(r'\bZo is [^.!?]*(?:[.!?](?=\s|$)|$)', txt)) and not any(g.replace('.', '') in a for a in _alle_t):
                        info.append(f"{tag} [{lab}]: getal {g} in een neutraal voorbeeld ('Zo is …', #157)"); continue
                    (info if int(g.replace('.', '')) in ANKER else warns).append(f"{tag} [{lab}]: getal {g} in de hint")
                for g in re.findall(r'op een (\d)\b',txt):
                    info.append(f"{tag} [{lab}]: eindcijfer {g} in de hint")
            f2,w2=item_checks(doel,s['somtype'],tag); fails+=f2; warns+=w2; info+=_K113.pop_info()
            w3,i3=_K113.check113_somtype(tag,s,items_van(doel,s['somtype'])); warns+=w3; info+=i3   # #113 Hint 1/2/Ouderzin
    f2,i2=json_taal(); fails+=f2; info+=i2
    fails+=hint_koppeling()       # #30 (G5 1 okt 17:00): nooit stil samenvoegen
    return fails,warns,info,n_klaar,n_open
if __name__=="__main__":
    files=sys.argv[1:] or sorted(glob.glob(f"{BASE}/somtypen/G6-*.md"))
    fails,warns,info,k,o=check(files)
    for x in fails: print("FAIL",x)
    for x in warns: print("WARN",x)
    for x in info: print("INFO",x)
    print(f"Somtypen: {k} hints klaar · {o} open · {len(fails)} FAIL · {len(warns)} WARN · {len(info)} INFO · {'ALLES OK' if not fails else 'FAIL'}")
    sys.exit(1 if fails else 0)
