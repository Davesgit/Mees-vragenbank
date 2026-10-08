#!/usr/bin/env python3
r"""Notatie van grote getallen G3–G8 (Overzicht 2026-09-30 13:23).
Regel: getallen van 4 cijfers zonder punt (1000, 4116), vanaf 10.000 met punt (10.000, 300.000, 1.005.000).
Deze check WAARSCHUWT (WARN) voor een getal van 5 of meer cijfers zonder punt in kindtekst:
Opgave (ook vervolgregels), Opties, Antwoord, Hint, Sterkere hint, de uitleg in Fout-hints en Ouderzin.
Niet meegeteld (invoer of meta):
  - accept-lijsten '(accept: …)' en de Invoer-regel: het kind mag beide vormen typen, dus daar staan ze bewust allebei;
  - de sleutel van een fout-hint (de foute invoer vóór '→', bij multi 'Stap n → waarde →', bij verslepen 'kaart → waarde →');
  - meta-regels (Status, Getallenruimte, Context, Husselen …);
  - kloktijden (12:30, 12.30), kommagetallen, breuken, jaartallen en postcodes (die hebben ≤ 4 cijfers of staan achter ':' '.' ',' '/').
Sinds Didactiek 13:31 ook MACHT (WARN): een cijfer direct gevolgd door ², ³ of ^ (10³, 5², 10^3) in kindtekst, ook in sleutels.
  Machten zijn VO-stof; schrijf uit als vermenigvuldiging ('10 × 10 × 10 = 1000'). Eenheden (cm², m², dm³, m³, cm³) mogen wel.
  Hercheck: rg -n --pcre2 '\d\s?[²³]|\d\^' rekenen-groep{3,4,5,6,7,8}/bank --max-depth 1 -g 'G*-*.md' -g '!*claude-pilot*'
BEWUST: items waar de ongepunte vorm de inhoud is (notatie-afleider, geplakt getal); staan hieronder met reden.
Welke bestanden: live zoals build-bank.js (tools/bankfiles.py), dus in G7 ook G7-GET-01/03-claude.md.
Gebruik: python3 check_notatie.py [groepnummers] [--strict]   (standaard 3 4 5 6 7 8).
Exit 0 (alleen WARN); met --strict exit 1 als er WARN is. $NOTATIE_BANK_G<n> = andere map (bv. backup).
Hercheck (rg, ruw; accept-lijsten en fout-hint-sleutels zelf wegdenken):
  rg -n --pcre2 '(?<![\d.,/:])\d{5,}(?!\d)' rekenen-groep{3,4,5,6,7,8}/bank/G*-*.md | rg -v 'claude-pilot|Getallenruimte'
"""
import re,os,sys
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from bankfiles import live_files
BEWUST={
 "G6-GET-M01-007":"notatie-item: opties 87.400 / 87,400 / 87400 / 87 400; de ongepunte optie is de afleider",
 "G5-GET-M04-004":"optie D beschrijft de plakfout ('Plak 520 en 40 aan elkaar tot 52040')",
}
KIND=("Opgave","Opties","Antwoord","Hint","Sterkere hint","Fout-hints","Ouderzin")
MACHT=re.compile(r'(?<![\d.,])\d+(?:[.,]\d+)?\s?[²³]|\d+\s?\^\s?\d+')
BIG=re.compile(r'(?<![\d.,/:])\d{5,}(?!\d)')
ACC=re.compile(r'\(accept:[^)]*\)|accept:[^)]*')
FIELD=re.compile(r'^- \*\*([^*]+?):\*\*\s?(.*)$')
def strip_keys(t):
    out=[]
    for seg in re.split(r'\s·\s',t):
        if '→' not in seg: out.append(seg); continue
        rest=seg.split('→',1)[1]
        m=re.match(r'\s*([^→.;!?]{1,30}?)\s*→(.*)$',rest)      # 2e sleuteldeel: 'Stap 2 → 240000 →', 'half miljoen → 100000 →'
        if m and re.match(r'\s*Stap\s*\d|\S',seg) and (re.match(r'\s*Stap\s*\d',seg) or re.fullmatch(r'[\d.,\s€%/a-z]+',m.group(1).strip())):
            rest=m.group(2)
        out.append(rest)
    return " · ".join(out)
def scan_file(f):
    name=os.path.basename(f)[:-3]; hits=[]; num=None; fld=None
    for ln,l in enumerate(open(f,encoding="utf-8").read().split("\n"),1):
        m=re.match(r'^##\s+(\d{3})\s*·',l)
        if m: num=m.group(1); fld=None; continue
        if num is None: continue
        fm=FIELD.match(l)
        if fm: fld,txt=fm.group(1).strip(),fm.group(2)
        elif l.startswith("  ") and fld: txt=l
        else: fld=None if l.startswith("#") else fld; continue
        if fld not in KIND: continue
        for h in MACHT.finditer(txt):
            hits.append((f"{name}-{num}",fld,"MACHT:"+h.group(),ln,os.path.basename(f)))
        t=ACC.sub('',txt)
        if fld=="Fout-hints": t=strip_keys(t)
        for h in BIG.finditer(t):
            hits.append((f"{name}-{num}" if not name.endswith("-claude") else f"{name}-{num}",fld,h.group(),ln,os.path.basename(f)))
    return hits
def scan(gs):
    warn=[];bew=[]
    for g in gs:
        d=os.environ.get(f"NOTATIE_BANK_G{g}")
        if not d and not os.path.isdir(f"{_BANK}/groep{g}"): continue
        for f in live_files(g,d):
            for h in scan_file(f):
                (bew if h[0] in BEWUST else warn).append((g,)+h)
    return warn,bew
if __name__=="__main__":
    args=[a for a in sys.argv[1:] if not a.startswith("--")]
    gs=[int(a) for a in args] or [3,4,5,6,7,8]
    warn,bew=scan(gs)
    for w in warn:
        if w[3].startswith("MACHT:"): print(f"WARN {w[1]} [{w[2]}] macht '{w[3][6:]}' (VO-stof; schrijf uit als vermenigvuldiging) → {w[5]}:{w[4]}")
        else: print(f"WARN {w[1]} [{w[2]}] '{w[3]}' zonder punt → {w[5]}:{w[4]}")
    for b in bew: print(f"BEWUST {b[1]} [{b[2]}] '{b[3]}' — {BEWUST[b[1]]}")
    for g in gs:
        n=sum(1 for w in warn if w[0]==g); print(f"G{g} notatie (≥5 cijfers met punt): {'ALLES OK' if n==0 else f'{n} WARN'} (incl. machten)")
    sys.exit(1 if (warn and "--strict" in sys.argv) else 0)
