#!/usr/bin/env python3
"""Check op de hints van de G5-merge (somtypen/G5-*.md). G5-versie (Overzicht, 1 okt 15:15) van g4/check_hints.py (Oefeningen, stand 15:05);
verschil met G4: keerdoelen G5 (×/: alleen in GET-V03, M05, M06, E07, E08, E09, MEET-E08, VERH-E02: daarbuiten FAIL), breuk n/m = FAIL
(G5: in woorden), kommagetal alleen bij geld (€3,50) en liter (0,5 L), 'afronden' mag (G5-GET-E02).
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
  WARN  (G5) een getal boven 1000 in een hint · FAIL (G5) getal vanaf 10.000 zonder punt
  FAIL  een Claude-tekst die vervangen is (claudeVervangen/claudeTekst) staat weer als kindtekst in de data (terugval, les G4 4b)
  WARN  het antwoord van een ander item van dit somtype staat in Hint 1/2 · een getal in Hint 1/2 (10, 20, 100 als anker = INFO; afrondcijfer 5 in 'Is het 5 of meer' = INFO, ronde 1b)
        · kommalijst van sommen ('3 + 4, 5 + 2') · een kleurnaam (de app laat kleuren misschien niet zien; het werkwoord 'kleuren' telt niet mee, G4-GET-M06).
  Per item (data/per_doel/<doel>.json, alle items van het somtype; dit is wat het kind ziet):
  FAIL  item zonder fout-hint · plaatshouder in een fout-hint · taal- en notatieregels hierboven op elke fout-hint (ook Claude per item)
        · een fout-hint die 'te veel' zegt bij een te laag antwoord, of 'te weinig'/'tel verder'/'tel door' bij een te hoog antwoord
        · het antwoord staat in de fout-hint.
  WARN  claudeUitleg staat in een kindtekst (controle.claudeUitlegInKindtekst).
  FAIL  (#48) een algemenere regel (antwoord ± n, bereik) vangt een sleutel vóór een preciezere regel (getallen uit de vraag, Claudes sleutel).
  FAIL  (#51) 'de tafel opzeggen' / 'de tafel van' in een kindtekst bij een context met (eet)tafels.
  FAIL  (#44) een somtype met een 'andere fout'-regel en een item zonder algemeneFoutHint; 'te veel'/'te weinig' die niet past bij de
        sleutel of bij de regel (vanaf / tot en met / kleiner dan / waarden), ook bij geld (in centen).
  FAIL  (#30) elk probleem in logs/hint_sleutels.json, een log die niet bij de somtype-indeling van data/gemapt.json hoort, of twee hint-entries op één kop (nooit stil samenvoegen).
  FAIL  (#34) een foute optie zonder eigen fout-hint (sleutel = de optie); (#23) de omgedraaide keersom van het antwoord als foute optie.
  FAIL  (fixlijst #18) 'Splits het tweede getal in honderdtallen' zonder '(als het die heeft)' terwijl een item een tweede getal onder de 100 heeft.
Somtypes zonder 'hints klaar' tellen als 'open'.
Gebruik: python3 check_hints.py [bestand.md ...]   (standaard alle somtypen/G5-*.md) · exit 1 bij FAIL.
"""
import re,sys,os,glob,json,collections
import sys as _sys113; _sys113.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'scripts', 'merge')); import klok113_check as _K113
BASE=os.path.dirname(os.path.abspath(__file__))
LETTER=re.compile(r"(?<![\w'’/.-])([A-D])(?![\w'’/-])")
KLOK=re.compile(r'(?<![\d:])\d{1,2}:\d{2}(?!\d)')
ENGELS=re.compile(r"\b(scaffold\w*|hints?|tip of the|step|count|next|answer|okay|oké|ok|cool|sorry|level|game|nice|wow|yes|please|great|good job|well done)\b",re.I)
ANKER={10,20,100}
MOEILIJK=re.compile(r'\b(kitten\w*|maanste\w*|ruimtepak\w*|schroef\w*|schroeven|zonnepane\w*|satelliet\w*|astronaut\w*|robot\w*|keeper\w*|\w*saurus\w*|zeshoek\w*|vijfhoek\w*|ruit|vermenigvuldig\w*|voertuig\w*|zaagsnede\w*|combinatie\w*|bewerking\w*)\b',re.I)
KEER_DOELEN={'G5-GET-V03','G5-GET-M05','G5-GET-M06','G5-GET-E07','G5-GET-E08','G5-GET-E09','G5-MEET-E08','G5-VERH-E02'}
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
      ("spelling 'uitgaan'",re.compile(r'\buit gaan\b',re.I)),("spelling 'bijkomen'/'bijkomt' (#90: ook 'bij komt', 'bij kom')",re.compile(r'\bbij kom(?:en|t)?\b',re.I)),
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
    if '÷' in txt: f.append("'÷' (G5: 'a : b')")
    if re.search(r'(?<![\d/])\d+/\d+(?![\d/])',txt): f.append("breuk n/m (G5: in woorden, 'de helft', 'een kwart')")
    if any(not (txt[:k.start()].endswith('€') or txt[k.end():].startswith(' L')) for k in re.finditer(r'(?<![\d,])\d+,\d+(?!\s*[+−×:-]\s*\d)',txt)) and not re.search(r'\d\s*[+−×-]\s*\d+\s*,\s*\d',txt): f.append("kommagetal buiten geld/liter")
    if doel.startswith('G5') and doel not in KEER_DOELEN and (re.search(r'[\d□#]\s*×\s*[\d□#]',txt) or re.search(r'[\d□]\s+:\s+[\d□]',KLOK.sub('',txt))): f.append("'×' of ':' buiten de ×/:-doelen (G5)")
    if re.search(r'\d\s?[²³]|\d\s?\^',txt): f.append("macht")
    if re.search(r'(?<![\d.,])\d\.\d{3}(?![\d.,])',txt): f.append("4-cijferig getal met punt")
    if re.search(r'(?<![\d.,])\d{5,}(?![\d,])',txt): f.append("getal vanaf 10.000 zonder punt")
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
def _waarde(v):
    """#44: heel getal, of een geldbedrag in centen ('€8,80' → 880, '€4' → 400); anders None."""
    v=str(v).strip()
    if re.fullmatch(r'\d+',v): return int(v)
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
        # #48 (Didactiek batch 3 #45): precieze regels vóór de algemene. Per sleutel: de eerste regel die hem vangt, mag niet algemener zijn
        # dan een latere regel die hem ook vangt (niveau 3 = getallen uit de vraag, 2 = antwoord ± getalN, Claudes sleutels tellen niet mee, 1 = antwoord ± vast getal of bereik)
        rs=it.get('foutRegels') or []
        def _niv(r):
            g=(r.get('regel') or '').lower(); mt=r.get('match') or {}
            if mt.get('alles') or g.startswith('andere fout'): return 0
            if g.startswith('claudes sleutel'): return None   # Claudes denkfouten zijn vaak gemengd (batch 4 #45) en soms bewust een vangnet ná 'te veel/te weinig': niet meegeteld
            if re.match(r'fout = antwoord [±+\-−] getal[12]\b',g): return 2
            if re.match(r'fout = antwoord [±+\-−] ?\d',g) or 'of meer' in g or any(k in mt for k in ('vanaf','totEnMet','kleinerDan')): return 1
            return 3
        def _vangt(r,v):
            mt=r.get('match') or {}
            if v in (mt.get('waarden') or []): return True
            x=_int(v)
            if x is None: return False
            return ('vanaf' in mt and isinstance(mt['vanaf'],int) and x>=mt['vanaf']) or ('totEnMet' in mt and isinstance(mt['totEnMet'],int) and x<=mt['totEnMet']) \
                or ('kleinerDan' in mt and isinstance(mt['kleinerDan'],int) and x<mt['kleinerDan'])
        for v in sorted({str(w) for r in rs for w in (r.get('match') or {}).get('waarden') or []} | {f['fout'] for f in fh}):
            hit=[r for r in rs if (_niv(r) or 0)>0 and _vangt(r,v)]
            if len(hit)>1 and _niv(hit[0])<max(_niv(r) for r in hit[1:]):
                beter=next(r for r in hit[1:] if _niv(r)>_niv(hit[0]))
                fails.append(f"{t} [{v}]: '{hit[0]['regel']}' vangt de sleutel vóór de preciezere '{beter['regel']}' (#48: precieze regels eerst)")
        # #51 (Didactiek batch 3 #48): bij een context met (eet)tafels geen 'tafel' als tafel van vermenigvuldiging in een kindtekst
        if re.search(r'\btafels?\b',it['opgave'] or '') and not re.search(r'\btafels? van \d',it['opgave'] or ''):
            kt=[it.get('hint') or '',it.get('sterkereHint') or '',it.get('algemeneFoutHint') or '']+[f.get('uitleg') or '' for f in fh]+[r.get('tekst') or '' for r in rs]
            for x in kt:
                if re.search(r'\b(?:de|een) tafel (?:op|van)\b|\btafel opzeggen\b|\bin de tafel\b|\btafels? van (?:\d|het|de)\b|\bstap(?:pen)? (?:hoger|lager|verder) in de tafel',x,re.I):
                    fails.append(f"{t}: 'tafel' in de betekenis van de tafel van vermenigvuldiging, in een context met tafels (#51): «{x[:90]}»")
        for f in fh:
            u=f.get('uitleg') or ''
            if 'TEKST NODIG' in u or not u.strip(): fails.append(f"{t} [{f['fout']}]: plaatshouder of lege tekst")
            for naam,rx in TAAL:
                if rx.search(u): fails.append(f"{t} [{f['fout']}]: {naam}")
            for x in regel_checks(u,doel): fails.append(f"{t} [{f['fout']}]: {x}")
            v=_waarde(f['fout']) if str(it['antwoord']).startswith('€') else _int(f['fout'])
            if a is not None and v is not None: fails+=_richting(t,a,v,u,f['fout'])
            if ans_hits(it['antwoord'],u): fails.append(f"{t} [{f['fout']}]: het antwoord ('{it['antwoord']}') staat in de fout-hint")
        f88,w88=check88(it,t,fh); fails+=f88; warns+=w88
        fails+=check90_91(it,t,fh)
        fails+=check104(it,t,fh)
        if (it.get('controle') or {}).get('claudeUitlegInKindtekst'): warns.append(f"{t}: claudeUitleg in kindtekst {it['controle']['claudeUitlegInKindtekst']}")
    return fails,warns
def _klokminuut(it):
    jr=(it.get('visual') or {}).get('jsRender') or {}
    if jr.get('soort')=='klok' and isinstance(jr.get('minuut'),int): return jr['minuut']
    if jr.get('soort')=='klokkenrij' and jr.get('labels') and it['antwoord'] in jr['labels']:
        return jr['klokken'][jr['labels'].index(it['antwoord'])].get('minuut')
    return None
def check88(it,t,fh):
    """merge-fixlijst #88 (Didactiek 18:15). (a) FAIL: 'de hele uren' zonder 'als die er zijn' terwijl er in dit item geen heel uur
    tussen de twee tijden zit (MEET-E06 #2/#15). (b) klok op 5 of 10 minuten over het hele uur: 'voorbij' zonder 'net' = WARN
    (#12/#14); 'net voorbij' bij een klok op half = FAIL."""
    fails=[];warns=[]
    kt=[('Hint 1',it.get('hint') or ''),('Hint 2',it.get('sterkereHint') or ''),('algemeneFoutHint',it.get('algemeneFoutHint') or '')]+[(f"fout {f['fout']}",f.get('uitleg') or '') for f in fh]
    o=re.sub(r'zoals \d{1,2}:\d{2}','',it['opgave'] or '')   # 'Typ de tijd, zoals 9:05' is geen tijd uit de som
    tt=[int(a)*60+int(b) for a,b in re.findall(r'(?<![\d:])(\d{1,2}):(\d{2})(?!\d)',o)]
    hele=None
    if len(tt)>=2: hele=tt[1]//60-(-(-tt[0]//60))
    elif len(tt)==1 and (m:=re.search(r'duurt (\d+) uur',o)): hele=int(m.group(1))
    elif len(tt)==1 and re.search(r'duurt \d+ minuten',o): hele=0
    for wat,x in kt:
        if hele is not None and hele<1 and re.search(r'\bde hele uren\b',x,re.I) and 'als die er zijn' not in x:
            fails.append(f"{t} [{wat}]: 'de hele uren' zonder 'als die er zijn', maar hier zit geen heel uur tussen (#88)")
    mn=_klokminuut(it)
    if mn is not None:
        for wat,x in kt:
            if mn in (5,10) and re.search(r'\bvoorbij\b',x) and not re.search(r'\bnet voorbij\b',x):
                warns.append(f"{t} [{wat}]: klok op {mn} minuten over: 'voorbij' zonder 'net' (#88)")
            if mn==30 and re.search(r'\bnet voorbij\b',x):
                fails.append(f"{t} [{wat}]: 'net voorbij' bij een klok op half (#88)")
    return fails,warns
def check104(it,t,fh):
    """merge-fixlijst #104a (Didactiek 18:54, V-c): vraagt het item naar een tijd van 13:00 of later (antwoord of digitale tijd in de opgave),
    dan moet een kloktekst over 'het uur vóór de dubbele punt' ook bij 13–23 kloppen: FAIL als er dan geen 'twaalf' (eraf) in de tekst staat."""
    o=re.sub(r'zoals \d{1,2}:\d{2}','',it['opgave'] or '')
    uren=[int(h) for h in re.findall(r'(?<![\d:])(\d{1,2}):\d{2}(?!\d)',o+' '+str(it.get('antwoord') or ''))]
    if not any(13<=h<=23 for h in uren): return []
    kt=[('Hint 1',it.get('hint') or ''),('Hint 2',it.get('sterkereHint') or ''),('algemeneFoutHint',it.get('algemeneFoutHint') or '')]+[(f"fout {f['fout']}",f.get('uitleg') or '') for f in fh]
    return [f"{t} [{wat}]: tijd van 13 uur of later, maar de tekst over 'het uur vóór de dubbele punt' zegt niet dat er twaalf af moet (#104a)"
            for wat,x in kt if re.search(r'vóór de dubbele punt',x,re.I) and not re.search(r'\btwaalf\b',x,re.I)]
BIJKOMT_RX=re.compile(r"\b(?:er|wat|hoeveel|of)\b[^.?!]{0,50}\bbij kom(?:t|en)\b",re.I)
def check90_91(it,t,fh):
    """merge-fixlijst #90 (Didactiek batch 6 V1): 'bij komt' in een bijzin = FAIL (moet 'bijkomt'). #91 (V2): bij teruggeven een tekst
    met 'en dan verder' of 'Tel daarna de hele euro's' zonder 'Ben je er dan nog niet?', terwijl in dit item het betaalde geld
    al de volgende hele euro is (er komt na het aanvullen niets meer bij) = FAIL."""
    fails=[]
    kt=[('Hint 1',it.get('hint') or ''),('Hint 2',it.get('sterkereHint') or ''),('algemeneFoutHint',it.get('algemeneFoutHint') or '')]+[(f"fout {f['fout']}",f.get('uitleg') or '') for f in fh]
    for wat,x in kt:
        if BIJKOMT_RX.search(x): fails.append(f"{t} [{wat}]: 'bij komt/bij komen' in een bijzin; schrijf 'bijkomt/bijkomen' (#90)")
    o=it['opgave'] or ''
    if (mb:=re.search(r'Je betaalt met €(\d+)',o)) and 'terug' in o:
        pr=[int(a)*100+int(b) for a,b in re.findall(r'€(\d+),(\d\d)',o.split('Je betaalt')[0])]
        if pr and -(-sum(pr)//100)*100==int(mb.group(1))*100:
            for wat,x in kt:
                if re.search(r"en dan verder|Tel daarna de hele euro's",x) and 'Ben je er dan nog niet?' not in x:
                    fails.append(f"{t} [{wat}]: 'de hele euro's' terwijl het betaalde geld al de volgende hele euro is (#91)")
    return fails
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
    import sys as _s; _s.path.insert(0,f"{BASE}/scripts"); import koppeling_merge as KM
    for b in sorted(glob.glob(f"{BASE}/hints/batch*.json")):
        for st in json.load(open(b,encoding='utf-8')).get('somtypen',[]):
            if KM.speciaal(st): alle_e.append(st); continue      # #75/#79: samengevoegd/geparkeerd (hints/koppeling_merge.json)
            alle_e.append(st)
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
                    if int(g.replace('.',''))>1000: warns.append(f"{tag} [{lab}]: getal {g} boven het G5-bereik (tot 1000)")
            alle=item_answers(doel,s['somtype'])
            for lab,txt in velden[:2]:
                for a in s['ant']:
                    if ans_hits(a,txt): fails.append(f"{tag} [{lab}]: antwoord van een voorbeeld ('{a}') staat in de hint")
                andere={a for a in alle if a not in s['ant'] and ans_hits(a,txt)}
                anker={a for a in andere if str(a).isdigit() and int(a) in ANKER and re.search(rf'\b(?:naar|tot|bij|via|de|op) {a}\b',txt)}
                for a in sorted(anker): fails.append(f"{tag} [{lab}]: anker {a} ('naar/tot/via {a}') is bij een ander item het antwoord")
                andere-=anker
                if andere: warns.append(f"{tag} [{lab}]: antwoord van ander item ({', '.join(sorted(map(str,andere)))}) staat in de hint")
                for g in re.findall(r'(?<![\d.,])(?<!op een )\d+(?!\d|[.,]\d)',txt):
                    # G5 ronde 1b (Didactiek S1): het afrondcijfer 5 in 'Is het 5 of meer' is een cijfer, geen getal (WARN alleen als 5 ergens het antwoord is)
                    if g=='5' and re.search(r'\bIs het 5 of meer\b',txt) and '5' not in {str(a) for a in alle}:
                        info.append(f"{tag} [{lab}]: afrondcijfer 5 ('Is het 5 of meer')"); continue
                    (info if int(g) in ANKER else warns).append(f"{tag} [{lab}]: getal {g} in de hint")
                for g in re.findall(r'op een (\d)\b',txt):
                    info.append(f"{tag} [{lab}]: eindcijfer {g} in de hint")
            # merge-fixlijst #18: 'Splits het tweede getal in honderdtallen …' alleen als elk item een tweede getal ≥ 100 heeft
            for lab,txt in velden:
                if re.search(r'[Ss]plits het tweede getal in honderdtallen(?! \(als het die heeft\))',txt):
                    klein=[it['nr'] for it in items_van(doel,s['somtype']) if len(re.findall(r'\d+',re.sub(r'(?<=\d)\.(?=\d{3})','',it['opgave'])))>1 and int(re.findall(r'\d+',re.sub(r'(?<=\d)\.(?=\d{3})','',it['opgave']))[1])<100]
                    if klein: fails.append(f"{tag} [{lab}]: 'Splits het tweede getal in honderdtallen', maar het tweede getal is onder de 100 (items {', '.join(klein[:5])}{' …' if len(klein)>5 else ''}); schrijf 'honderdtallen (als het die heeft)' (fixlijst #18)")
            f2,w2=item_checks(doel,s['somtype'],tag); fails+=f2; warns+=w2; info+=_K113.pop_info()
            w3,i3=_K113.check113_somtype(tag,s,items_van(doel,s['somtype'])); warns+=w3; info+=i3   # #113 Hint 1/2/Ouderzin
            # merge-punt #34: elke foute optie heeft een eigen fout-hint (sleutel = de optie), geen 'andere fout'
            for it in items_van(doel,s['somtype']):
                if it.get('opties'):
                    sl={str(f['fout']):f.get('uitleg') for f in it['foutHints']}
                    fout_o=[str(o['tekst']) for o in it['opties'] if str(o['tekst'])!=str(it['antwoord'])]
                    mis=[o for o in fout_o if o not in sl]
                    if mis: fails.append(f"{tag} item {it['nr']}: foute optie zonder eigen fout-hint: {', '.join(mis)}")
                    # #23/#34: de omgedraaide keersom van het antwoord is nooit een (foute) optie: dan zijn er twee goed
                    if (mk:=re.fullmatch(r'(\d+) × (\d+)',str(it['antwoord']))) and f"{mk.group(2)} × {mk.group(1)}" in fout_o and mk.group(1)!=mk.group(2):
                        fails.append(f"{tag} item {it['nr']}: de omgedraaide keersom {mk.group(2)} × {mk.group(1)} staat als foute optie")
    f2,i2=json_taal(); fails+=f2; info+=i2
    fails+=terugval()
    fails+=hint_koppeling()
    return fails,warns,info,n_klaar,n_open
if __name__=="__main__":
    files=sys.argv[1:] or sorted(glob.glob(f"{BASE}/somtypen/G5-*.md"))
    fails,warns,info,k,o=check(files)
    sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'scripts', 'merge')); import huis_checks as _HC      # #540 KEERDELEN + #543 LETT-testtabel (eindcheck G6 r11)
    fails = list(fails) + _HC.extra_fails(os.path.dirname(os.path.abspath(__file__)))
    warns = list(warns) + _HC.extra_warns(os.path.dirname(os.path.abspath(__file__)))      # ONLEESBAAR: regel bij geen enkel item te lezen (8 okt)
    for x in fails: print("FAIL",x)
    for x in warns: print("WARN",x)
    for x in info: print("INFO",x)
    # Oef-#484 (les 250, 8 okt): ±1-tekst op een sleutel die een getal uit de vraag is (WARN, alle groepen)
    import json as _j250, glob as _g250, os as _o250, sys as _s250; _s250.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'scripts', 'merge')); import les250_check as _L250
    for _w in _L250.treffers([_it for _p in sorted(_g250.glob(_o250.path.join(_o250.path.dirname(_o250.path.abspath(__file__)), 'data', 'per_doel', '*.json'))) for _it in _j250.load(open(_p))['items']]):
        warns.append('LES250 ' + _w); print('WARN LES250', _w)
    # Z-#812 (Didactiek, 8 okt): les 217 (geen zin die een bewerking uitsluit) in de build-gate (WARN in G5)
    import les217_check as _L217
    _m217, _v217 = _L217.zelftest()      # Oef-#489: zelftest (Z-#812/Z-#824) hoort groen te zijn, anders FAIL
    if _m217 or _v217: fails.append(f'les 217 zelftest: {len(_m217)} gemist, {len(_v217)} vals alarm'); print('FAIL les 217 zelftest', _m217, _v217)
    for _w in _L217.groep(_o250.path.dirname(_o250.path.abspath(__file__))): warns.append(_w); print('WARN', _w)
    print(f"Somtypen: {k} hints klaar · {o} open · {len(fails)} FAIL · {len(warns)} WARN · {len(info)} INFO · {'ALLES OK' if not fails else 'FAIL'}")
    sys.exit(1 if fails else 0)
