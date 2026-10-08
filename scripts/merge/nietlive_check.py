"""V-#1030 (Didactiek hercheck b9 19:01:49, les 395): een item met visual.nodig zonder beeld (geen jsRender, geen svgBestanden) moet de vlag
visual.nietLiveZonderBeeld hebben, op de plek waar alle lezers kijken (build_g6, build_g3, check_fixlijst_g6, visual_somtype_check); een vlag op itemniveau
('nietLiveZonderBeeld' naast 'visual') leest niemand (FAIL).
Gebruik: import nietlive_check as NL; n = NL.rapport(items)."""
def treffers(items):
    T = []
    for it in items:
        v = it.get('visual') or {}
        if 'nietLiveZonderBeeld' in it: T.append(f"{it['id']}: nietLiveZonderBeeld op itemniveau (hoort in visual)")
        if v.get('nodig') and not (v.get('jsRender') or v.get('svgBestanden') or v.get('nietLiveZonderBeeld')): T.append(f"{it['id']}: visual.nodig zonder jsRender/svg en zonder visual.nietLiveZonderBeeld (niet speelbaar)")
    return T
MUTANTEN = [({'id': 'mut-V01-001', 'nietLiveZonderBeeld': True, 'visual': {'nodig': True, 'jsRender': None, 'svgBestanden': []}}, True),
            ({'id': 'mut-V01-001-fix', 'visual': {'nodig': True, 'jsRender': None, 'svgBestanden': [], 'nietLiveZonderBeeld': True}}, False),
            ({'id': 'mut-013', 'visual': {'nodig': True, 'jsRender': {'soort': 'lijngrafiek'}}}, False)]
def mutanten_ok(): return all(bool(treffers([i])) == v for i, v in MUTANTEN)
def rapport(items, toon=True, ernst='FAIL'):
    T = treffers(items)
    if toon:
        print(f"NIETLIVE (V-#1030: visual.nodig zonder beeld → visual.nietLiveZonderBeeld, niet op itemniveau): {len(T)} ({ernst}) · mutanten {sum(bool(treffers([i])) == v for i, v in MUTANTEN)}/{len(MUTANTEN)}")
        for x in T[:15]: print(f'  {ernst} NIETLIVE', x)
    return len(T) + (0 if mutanten_ok() else 1)
