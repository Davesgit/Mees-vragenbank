"""Welke bankbestanden zijn live? Zoals build-bank.js (Website) het doet (Overzicht 2026-09-30 13:23):
- alle *.md in de bankmap zelf (geen submappen zoals drafts/ of _backup_compact/), behalve README.md;
- behalve bestanden met 'claude-pilot' in de naam;
- bestanden zonder items (zoals de gemergde *-claude-bijvul*.md en het overzicht G7-VBN.md) vallen weg.
Zo tellen in G7 ook G7-GET-01-claude.md en G7-GET-03-claude.md mee.
Gebruik: from bankfiles import live_files; live_files(7) of live_files(7, '/pad/naar/backup')."""
import os,re,glob
_BANK=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"bank")  # repo: bank/groepN (was /workspace/rekenen-groepN/bank)
ITEM=re.compile(r'^##\s+\d{3}\s*·',re.M)
def live_files(g,d=None):
    d=d or f"{_BANK}/groep{g}"
    out=[]
    for f in sorted(glob.glob(os.path.join(d,"*.md"))):
        b=os.path.basename(f)
        if b.lower()=="readme.md" or "claude-pilot" in b: continue
        if not ITEM.search(open(f,encoding="utf-8").read()): continue
        out.append(f)
    return out
