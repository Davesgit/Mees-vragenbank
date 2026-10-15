#!/usr/bin/env python3
"""[G5-kopie van g4/scripts/apply_hints.py (1 okt 14:35); BASE = claude-merge/g5] Zet de hints uit hints/batch*.json in somtypen/<doel>.md (idempotent) én per item in data/ (stap 6, 1 okt 13:15).
md: per somtype ('## Somtype n') wordt het blok vanaf '- **Hint 1 (te schrijven):**' tot de volgende lege regel
vervangen door Hint 1, Hint 2, Ouderzin, Fout-hints en 'Status: hints klaar'.
Staat 'somtype' in de json, dan moet de kop '## Somtype n: …' in de md daar precies bij passen (anders stopt het script).
Na een nieuwe build_g3.py: eerst scripts/sync_hint_keys.py (zet nr/somtype in de json gelijk aan de nieuwe koppen);
build_g5.py doet dat zelf al en draait daarna dit script.
data: elk gemapt item van het somtype krijgt hint, sterkereHint, ouderzin en de fout-hintregels per item
(scripts/fout_regels.py; basis = extraVelden.claudeFoutHints, dus opnieuw draaien geeft hetzelfde).
Bron van waarheid = hints/batch*.json. Gebruik: python3 scripts/apply_hints.py [hints/batch1.json ...]
(zonder argumenten: alle batches; met argumenten: alleen die batches, de rest van de items blijft zoals hij was)."""
import json,re,sys,glob,os,collections
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import fout_regels
import koppeling_merge
fout_regels.BEREIK_AFRONDEN = 1000     # G5 rekent tot 1000: geen fout-sleutel 1100 bij afronden (merge-fixlijst #1/#13)
fout_regels.LIJN_BINNEN = True        # G5: geen fout-sleutel buiten de getallenlijn (merge-fixlijst #14)
fout_regels.GELD_PUNT = True           # merge-punt #33: punt in plaats van komma bij geld
fout_regels.KOLOM_VOOR_DEEL = True     # merge-fixlijst #124: kolomsom bij 'Hoeveel X in totaal?' krijgt de kolomtekst
BRON_TAG={'nieuw':'nieuw','claude':'Claude, ok','claude-taalfix':'Claude, taalfix'}

def hints_sync_stempel():
    """#355: hintsSyncOp = tijdstip van deze hint-sync (apply_hints); hintsBatches = de batchbestanden met een md5 van de inhoud."""
    import glob as _g, datetime as _dt
    nu=_dt.datetime.now().astimezone().isoformat(timespec='seconds')
    import hashlib as _h      # md5 van de inhoud: de sync schrijft de batches bij elke build opnieuw, dus de wijzigtijd zegt niets
    bs=[{'batch':os.path.basename(b),'md5':_h.md5(open(b,'rb').read()).hexdigest()[:12]} for b in sorted(_g.glob(f"{BASE}/hints/batch*.json"))]
    return {'hintsSyncOp':nu,'hintsBatches':bs}

def block(st):
    L=[f"- **Hint 1 (te schrijven):** {st['hint1']}",f"- **Hint 2 (te schrijven):** {st['hint2']}",f"- **Ouderzin:** {st['ouderzin']}"]
    fh=st['foutHints']
    onbekend=sorted({f['bron'] for f in fh}-set(BRON_TAG))
    if onbekend: sys.exit(f"{st['doel']} somtype {st['nr']}: onbekende bron {onbekend} in de fout-hints (bekend: {', '.join(BRON_TAG)})")
    if all(f['bron']=='claude' for f in fh):
        L.append("- **Fout-hints:** fout-hints Claude: ok")
    else:
        ok=[f for f in fh if f['bron']=='claude']; fix=[f for f in fh if f['bron']=='claude-taalfix']; nieuw=[f for f in fh if f['bron']=='nieuw']
        kop='deels ok' if ok else ('taalfix' if fix and not nieuw else 'vervangen')
        L.append(f"- **Fout-hints:** fout-hints Claude: {kop} — per soort fout, regels van boven naar beneden (de eerste die past):")
        for f in fh:
            soort=f"`{f['soort']}` " if f.get('soort') else ""
            L.append(f"  - {soort}({f['regel']}) → {f['tekst']}  [{BRON_TAG[f['bron']]}]")
    L.append("- Status: hints klaar")
    return L
def apply(path):
    data=json.load(open(path)); per={}
    for st in data['somtypen']:
        if koppeling_merge.speciaal(st): continue      # #75/#79 (hints/koppeling_merge.json): niet in de md, niet op items
        per.setdefault(st['doel'],{})[st['nr']]=st
    for doel,sts in per.items():
        p=f"{BASE}/somtypen/{doel}.md"; L=open(p,encoding='utf-8').read().split("\n"); out=[]; i=0; cur=None
        while i<len(L):
            m=re.match(r'^## Somtype (\d+):',L[i])
            if m: cur=int(m.group(1))
            if L[i].startswith("## ") and not m: cur=None
            if m and cur in sts and sts[cur].get('somtype') and m.string.split(': ',1)[1].strip()!=sts[cur]['somtype']:
                sys.exit(f"{doel} somtype {cur}: kop in de md past niet bij de json ('{sts[cur]['somtype'][:50]}'); draai eerst scripts/sync_hint_keys.py")
            if cur in sts and L[i].startswith("- **Hint 1 (te schrijven):**"):
                j=i
                while j<len(L) and L[j].strip()!="" and not L[j].startswith("## "): j+=1
                out+=block(sts[cur])
                if sts[cur].get('kopGewijzigd'):
                    kg=sts[cur]['kopGewijzigd']; out.insert(len(out)-1,f"- **LET OP kop gewijzigd** ({kg['op']}): de hints zijn geschreven voor '{kg['van']}'. Nakijken of ze nog passen.")
                if sts[cur]['somtype'].startswith('[vorm] Vouw') and not fout_regels.heeft_stipregel(sts[cur]):
                    out.insert(len(out)-1,f"  - `stip niet verplaatst` (fout = het vak van de stip) → {fout_regels.PLACEHOLDER_STIP}  [merge, plaatshouder]")
                i=j; cur=None; continue
            out.append(L[i]); i+=1
        open(p,"w",encoding='utf-8').write("\n".join(out))
        print(f"{doel}: {len(sts)} somtypen bijgewerkt")
    return [st for st in data['somtypen'] if not koppeling_merge.speciaal(st)]
def cellen(it):
    jr=it['visual']['jsRender'] or {}
    if not it['merge'].get('vakAfspraak') or it['opties']: return None
    return [f"{chr(64+r)}{c}" for r in range(1,jr['rijen']+1) for c in range(1,jr['kolommen']+1)]
def uitleg_lek(it):
    """claudeUitleg blijft intern (merge-fixlijst 12): de merge kopieert het nergens heen. Deze controle meldt alleen
    een zin uit claudeUitleg die toch in hint, sterkereHint, ouderzin of een fout-hint staat (dan komt hij uit de
    hint-batch zelf); er wordt niets weggehaald, Oefeningen beslist."""
    ex=it['extraVelden']; u=' '.join(x for x in (ex.get('claudeUitleg'),ex.get('claudeUitlegOudeVakcode')) if x)
    zinnen=[z.strip() for z in re.split(r'(?<=[.?!])\s+',u) if len(z.strip())>=20]
    velden=[k for k in ('hint','sterkereHint','ouderzin') if it.get(k) and any(z in it[k] for z in zinnen)]
    velden+=[f"foutHint {f['fout']}" for f in it['foutHints'] if any(z in (f.get('uitleg') or '') for z in zinnen)]
    it['controle']['claudeUitlegInKindtekst']=velden or None
    return bool(velden)
def apply_items(entries, batchnaam):
    import fixlijst_g5_r7b as R7B; R7B.pas_entries(entries)      # G5 ronde 7b: motorregels E09 en E05 #32 in plaats van Claudes labels (in het geheugen)
    import fixlijst_g5_r10 as R10; R10.pas_entries(entries)      # G5 ronde 10 #369: 'Bijna!' alleen bij één stap
    gp=f"{BASE}/data/gemapt.json"; G=json.load(open(gp,encoding='utf-8'))
    import hashlib as _hl; _md5=lambda x:_hl.md5(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:12]; _voor=_md5(G['items'])      # #553
    idx=collections.defaultdict(list)
    for it in G['items']: idx[(it['merge']['doel'],it['merge']['somtype'])].append(it)
    stats=collections.Counter(); onleesbaar=collections.Counter()
    _onl=collections.Counter(); _nit=collections.Counter()      # regel niet te lezen per entry (check_hints: WARN als hij bij geen enkel item leest; 8 okt)
    for st in entries:
        its=idx.get((st['doel'],st.get('somtype')),[])
        if not its: stats['somtype zonder items']+=1; continue
        for it in its:
            it['hint']=st['hint1']; it['sterkereHint']=st['hint2']; it['ouderzin']=st['ouderzin']
            it['merge']['hints']={'batch':batchnaam.get(id(st)),'nr':st['nr'],'somtype':st['somtype']}
            for r in fout_regels.pas_toe(it,st,cellen(it)): onleesbaar[(st['doel'],r)]+=1; _onl[(st['doel'],st.get('nrOrigineel'),r)]+=1
            _nit[(st['doel'],st.get('nrOrigineel'))]+=1
            stats['foutRegels weg (#374)']+=R10.regels374(it)
            if uitleg_lek(it): stats['claudeUitleg in kindtekst']+=1
            stats['items']+=1
            if it['controle']['zonderFoutHints']: stats['items zonder fout-hint']+=1
    # #355 (Didactiek r7b, 8 okt): eigen tijdstempel voor de hint-sync; gegenereerdOp blijft de buildtijd
    _sync=hints_sync_stempel(); _na=_md5(G['items'])
    # #553 (eindcheck r11b): elke schrijfactie krijgt een stempel. geschrevenOp = nu; gegenereerdOp (buildtijd) blijft van de build. In logs/schrijflog.jsonl
    # staat per schrijfactie de buildtijd, of de items echt veranderd zijn (md5 vóór/na), en of het binnen een build gebeurde of los (apply_hints apart).
    import datetime as _dtm
    _bt=G.get('gegenereerdOp'); _los=True
    try: _los=(_dtm.datetime.fromisoformat(_sync['hintsSyncOp'])-_dtm.datetime.fromisoformat(_bt.replace('+0200','+02:00'))).total_seconds()>300
    except Exception: pass
    _sync.update(geschrevenOp=_sync['hintsSyncOp'], geschrevenDoor='apply_hints (los, zonder nieuwe build)' if _los else 'build (apply_hints)', itemsGewijzigdBijSchrijven=_voor!=_na)
    with open(f"{BASE}/logs/schrijflog.jsonl",'a',encoding='utf-8') as _f:
        _f.write(json.dumps({'geschrevenOp':_sync['hintsSyncOp'],'door':_sync['geschrevenDoor'],'gegenereerdOp':_bt,'itemsMd5Voor':_voor,'itemsMd5Na':_na,'itemsGewijzigd':_voor!=_na},ensure_ascii=False)+'\n')
    G.update(_sync)
    json.dump(G,open(gp,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    perdoel=collections.defaultdict(list)
    for it in G['items']: perdoel[it['merge']['doel']].append(it)
    for doel,its in perdoel.items():
        p=f"{BASE}/data/per_doel/{doel}.json"
        if os.path.exists(p):
            D=json.load(open(p,encoding='utf-8')); D['items']=sorted(its,key=lambda x:x['id']); D['aantal']=len(its); D.update(_sync)
            json.dump(D,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f"items: {stats['items']} met hints · {stats['items zonder fout-hint']} zonder fout-hint · {stats['somtype zonder items']} somtype-entries zonder items · claudeUitleg in kindtekst: {stats['claudeUitleg in kindtekst']}")
    for (d,r),n in onleesbaar.items(): print(f"LET OP regel niet te lezen in {d}: '{r}' ({n} items)")
    json.dump({'uitleg':'Per hint-entry de regels die de motor bij een item niet kon lezen (fout_regels.pas_toe). check_hints: WARN als een regel bij geen enkel item van het somtype te lezen is.',
               'regels':[{'doel':d,'nrOrigineel':n,'regel':r,'itemsNietTeLezen':k,'items':_nit[(d,n)]} for (d,n,r),k in sorted(_onl.items(),key=str)]},
              open(f"{BASE}/logs/regels_onleesbaar.json",'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f"ronde 10: #374 foutRegels zonder sleutel weg bij generator-items: {stats['foutRegels weg (#374)']} · #369 'Bijna!' weg: {len(R10.LOG10['369'])} regel(s) {R10.LOG10['369']}")
    return stats,onleesbaar
if __name__=="__main__":
    paths=sys.argv[1:] or sorted(glob.glob(f"{BASE}/hints/batch*.json"))
    if not paths: print("apply_hints: nog geen hints/batch*.json — niets toe te passen"); sys.exit(0)
    alle=[]; naam={}
    for p in paths:
        for st in apply(p): alle.append(st); naam[id(st)]=os.path.basename(p)
    apply_items(alle,naam)
