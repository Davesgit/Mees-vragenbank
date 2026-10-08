#!/usr/bin/env python3
"""Z-#525 (review G7 batch 1, Didactiek 8 okt): visual.nodig (en nietLiveZonderBeeld) is gelijk binnen elk somtype. WARN per somtype dat mengt.
Gebruik: rapport(items); geeft het aantal WARN terug."""
import collections
def rapport(items):
    m = collections.defaultdict(lambda: collections.defaultdict(list))
    for it in items:
        if it['merge'].get('status', 'gemapt') != 'gemapt': continue
        v = it.get('visual') or {}
        m[(it['merge']['doel'], it['merge'].get('somtypeNrOrigineel'))][(bool(v.get('nodig')), bool(v.get('nietLiveZonderBeeld')))].append(it['id'])
    uit = [(k, dict(v)) for k, v in sorted(m.items(), key=lambda x: str(x[0])) if len(v) > 1]
    print(f"\nVISUAL (Z-#525: visual.nodig/nietLiveZonderBeeld gelijk binnen een somtype): {len(uit)} (WARN)")
    for (d, nr), v in uit: print(f"  WARN VISUAL {d} #{nr}: " + ' · '.join(f"nodig={a}/nietLive={b}: {len(ids)} ({ids[0]})" for (a, b), ids in v.items()))
    return len(uit)
