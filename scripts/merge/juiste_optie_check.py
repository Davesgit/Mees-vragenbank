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
def weergave(it): return ' · '.join(f"{o.get('letter')}) {o.get('tekst')}" for o in it.get('opties') or [])
def tekst_fouten(items):
    """V-#1010 (Didactiek r13, les 386): optiesTekst moet de weergave van opties[] zijn ('A) … · B) … · C) …'); twee optiebronnen kunnen elk een andere letter goed maken (FAIL).
    Ook: bij 'Hoe heet de 4 in 4/10?' zijn 'de deler' en 'het deeltal' nooit een afleider (een breuk is ook een deling, dus die optie is ook goed) (FAIL)."""
    F = []
    for it in items:
        if not it.get('opties'): continue
        if it.get('optiesTekst') and it['optiesTekst'] != weergave(it):
            F.append(f"{it['id']}: optiesTekst {it['optiesTekst']!r} ≠ opties[] {weergave(it)!r}")
        if __import__('re').search(r'\bin \d+/\d+\?', it.get('opgave') or ''):
            for o in it['opties']:
                if o.get('tekst') in ('de deler', 'het deeltal') and o.get('tekst') != str(it.get('antwoord')): F.append(f"{it['id']}: afleider {o['tekst']!r} is bij een breuk ook goed")
            for t in __import__('re').findall(r'[A-C]\) ([^·]+?)(?= · |$)', it.get('optiesTekst') or ''):
                if t in ('de deler', 'het deeltal') and t != str(it.get('antwoord')): F.append(f"{it['id']}: afleider {t!r} in optiesTekst is bij een breuk ook goed")
    return F
def _mut_m04(ot):
    return {'id': 'mut-M04-021', 'type': 'meerkeuze', 'opgave': 'Hoe heet de 10 in 4/10?', 'antwoord': 'de noemer', 'optiesTekst': ot, 'antwoordDetail': {'juisteOptie': 'A'},
            'opties': [{'letter': 'A', 'tekst': 'de noemer'}, {'letter': 'B', 'tekst': 'de teller'}, {'letter': 'C', 'tekst': 'de uitkomst'}]}
MUTANTEN = [('oud G6-GET-M04 021 (optiesTekst «A) de deler»)', _mut_m04('A) de deler · B) de teller · C) de noemer'), True),
            ('nieuw 021', _mut_m04('A) de noemer · B) de teller · C) de uitkomst'), False),
            ('juisteOptie B bij antwoord op A', dict(_mut_m04('A) de noemer · B) de teller · C) de uitkomst'), antwoordDetail={'juisteOptie': 'B'}), True)]
def mutanten_ok(): return all(bool(fouten([i]) + tekst_fouten([i])) == v for _, i, v in MUTANTEN)
def rapport(items, toon=True):
    n = _rapport(items, toon); T = tekst_fouten(items)
    if toon:
        print(f"OPTIESTEKST (V-#1010: optiesTekst = weergave van opties[]; geen 'de deler'/'het deeltal' als afleider bij een breuk): {len(T)} (FAIL) · mutanten {sum(bool(fouten([i]) + tekst_fouten([i])) == v for _, i, v in MUTANTEN)}/{len(MUTANTEN)}")
        for x in T[:15]: print('  FAIL OPTIESTEKST', x)
    return n + len(T) + (0 if mutanten_ok() else 1)
def _rapport(items, toon=True):
    F = fouten(items)
    if toon:
        print(f"\nJUISTE-OPTIE (antwoordDetail.juisteOptie past bij de opties): {len(F)} (FAIL)")
        for x in F[:15]: print('  FAIL JUISTE-OPTIE', x)
    return len(F)
