"""doelId-check (G5 merge-fixlijst #122, Didactiek 20:04; gedeeld door check_merge_notatie G3–G8). Leest alleen.
FAIL: een item in data/per_doel/<doel>.json zonder doelId (null of leeg), een doelId dat niet gelijk is aan het doelId van het
bestand, of een merge.doel dat afwijkt van het doelId. Aanleiding: de 20 generatoritems van #84 (G5-MEET-E06-merge-gen-001 t/m 020)
hadden doelId null, omdat het sjabloon een geparkeerd item was."""
import json, os

def vind(files):
    uit = []
    for p in files:
        d = json.load(open(p)); fd = d.get('doelId') if isinstance(d, dict) else None
        for it in (d.get('items') or []):
            i = it.get('id'); di = it.get('doelId'); md = (it.get('merge') or {}).get('doel')
            if not di: uit.append(f"{i}: geen doelId (bestand {os.path.basename(p)}, doel {fd})")
            elif fd and di != fd: uit.append(f"{i}: doelId {di} ≠ bestand {fd}")
            elif md and md != di: uit.append(f"{i}: merge.doel {md} ≠ doelId {di}")
    return uit

def rapport(files):
    uit = vind(files)
    print(f"\nDOELID (item zonder doelId of met een ander doelId dan het bestand, #122): {len(uit)} (FAIL)")
    for x in uit[:20]: print('  FAIL DOELID', x)
    return len(uit)
