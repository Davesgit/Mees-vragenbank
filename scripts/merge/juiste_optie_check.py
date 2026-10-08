"""antwoordDetail.juisteOptie(Tekst) moet bij de opties passen: de letter van de optie met de tekst van het antwoord (FAIL).
Aanleiding: G8 Oef-#467 (8 okt) verdeelde de goede optie over A/B/C, maar liet antwoordDetail.juisteOptie op 'A' staan (17 items, build 15:17:54).
Gebruik: import juiste_optie_check as JO; n_fail = JO.rapport(items)."""
def fouten(items):
    F = []
    for it in items:
        ad = it.get('antwoordDetail') or {}
        if it.get('type') != 'meerkeuze' or not isinstance(ad, dict) or not ad.get('juisteOptie'): continue
        ops = {o.get('letter'): o.get('tekst') for o in it.get('opties') or []}
        goed = ad.get('juisteOptieTekst') or str(it.get('antwoord'))
        if ops.get(ad['juisteOptie']) != goed or (ad.get('juisteOptieTekst') and ad['juisteOptieTekst'] != str(it.get('antwoord'))):
            F.append(f"{it['id']}: juisteOptie {ad['juisteOptie']} = {ops.get(ad['juisteOptie'])!r}, antwoord {it.get('antwoord')!r}")
    return F
def rapport(items, toon=True):
    F = fouten(items)
    if toon:
        print(f"\nJUISTE-OPTIE (antwoordDetail.juisteOptie past bij de opties): {len(F)} (FAIL)")
        for x in F[:15]: print('  FAIL JUISTE-OPTIE', x)
    return len(F)
