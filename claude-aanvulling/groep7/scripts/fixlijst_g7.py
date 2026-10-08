#!/usr/bin/env python3
"""G7-fixlijst (Overzicht), review batch 1 van Didactiek (8 okt 2026, g7/review-batch1-didactiek.md).
- V-#516: DENK-03 nrO 7 (sap). 3 + 2 = 5 gaf het goede antwoord, en een pak van 2 L / een kan met 6 L klopt niet met de referentiematen.
  Nieuw: 3 flesjes van 3 dl, er gaat 2 dl uit. Antwoord 7 dl; afleiders 9 dl (stap twee vergeten) en 4 dl (3 + 3 − 2: opgeteld in plaats van keer).
  TODO Oefeningen: hint1/hint2/foutHints van de entry (batch1 DENK-03 nrO 7) noemen nog 'pakken' en 'liter', en de regels '6 liter'/'4 liter'
  moeten '9 dl'/'4 dl' worden. Tot dan geeft check_hints een FAIL op die entry (tijdelijk goed, opdracht 11:56).
- Z-#525: de somtypes 'welke tekening/som' in DENK-02 krijgen allemaal visual.nodig = True met nietLiveZonderBeeld (zoals #4/#9/#10/#13).
  #3 ('gekleurd'): komt er een tekening, markeer het groepje dan ook anders dan met kleur.
Schrijft zelf niets; build_g7.py roept pas_toe(it, slog) aan na FX21, vóór hercontrole en de somtype-indeling."""
import re
V516_ID = 'dc788280-ed3c-4f4b-96b9-0a8424c3baee'
TODO516 = ("TODO Oefeningen (V-#516, 8 okt): opgave omgebouwd naar 3 flesjes van 3 dl, 2 dl eruit (7 dl). Werk H1, H2, ouderzin en de fout-hints "
           "van batch1 DENK-03 nrO 7 bij: 'pakken'/'liter' → 'flesjes'/'dl', regels '6 liter' → '9 dl' en '4 liter' → '4 dl'.")
Z525_TEKENING = {('G7-DENK-02', 'Er zijn # kinderen op het schoolplein'), ('G7-DENK-02', 'Je koopt # zakjes knikkers')}
def _v516(it, slog):
    if it['bron'].get('claudeId') != V516_ID: return
    oud = it['opgave']
    assert oud.startswith('Je hebt 3 pakken sap van elk 2 liter'), oud
    it['opgave'] = 'Je hebt 3 flesjes sap van elk 3 dl. Stap 1: giet alles in een kan. Stap 2: giet er 2 dl uit. Hoeveel dl zit er nog in de kan?'
    it['opties'] = [{'letter': 'A', 'tekst': '4 dl'}, {'letter': 'B', 'tekst': '7 dl'}, {'letter': 'C', 'tekst': '9 dl'}]
    it['optiesTekst'] = 'A) 4 dl · B) 7 dl · C) 9 dl'
    it['antwoord'] = '7 dl'; it['antwoordDetail'] = {'juisteOptie': 'B', 'juisteOptieTekst': '7 dl'}
    fh = [{'stap': None, 'fout': '9 dl', 'uitleg': 'Na stap 1 zit dat erin. Maar stap 2 moet je ook nog uitvoeren.'},
          {'stap': None, 'fout': '4 dl', 'uitleg': 'Je hebt 3 en 3 opgeteld. Elk flesje heeft 3 dl, dus hoeveel keer 3 dl is dat?'}]
    it['foutHints'] = fh
    it['foutHintsTekst'] = ' · '.join(f"{f['fout']} → {f['uitleg']}" for f in fh)
    ev = it['extraVelden']
    ev['claudeUitleg'] = '3 flesjes van 3 dl is 9 dl. Daar gaat 2 dl af. Er blijft 7 dl in de kan.'
    ev['claudeFoutHints'] = [dict(f) for f in fh]
    ev['claudeDenkfouten'] = [{'fout': '9 dl', 'denkfout': None}, {'fout': '4 dl', 'denkfout': 'optellen-ipv-vermenigvuldigen'}]
    it['merge']['todoOefeningen'] = TODO516
    it['merge']['v516'] = {'opgaveOud': oud, 'antwoordOud': '5 liter', 'optiesOud': ['4 liter', '5 liter', '6 liter']}
    slog(it, 'G7-V516 (review batch 1 Didactiek): sap 3 × 3 dl − 2 dl = 7 dl (3 + 2 gaf het goede antwoord; pak 2 L / kan 6 L)', 'opgave', oud, it['opgave'])
def _z525(it, slog):
    if it['merge'].get('doel') != 'G7-DENK-02' and it['doelId'] != 'G7-DENK-02': return
    o = re.sub(r'\d+', '#', it['opgave'])
    if not any(o.startswith(p) for d, p in Z525_TEKENING): return
    v = it['visual']
    if v.get('nodig') and v.get('nietLiveZonderBeeld'): return
    nv = dict(v, nodig=True, nietLiveZonderBeeld=True,
              toelichting='de vraag verwijst naar een tekening (welke tekening/som); zonder tekening niet live (Z-#525, zoals DENK-02 #4/#9/#10/#13)')
    if 'gekleurd' in ' '.join(x['tekst'] for x in it['opties'] or []):
        nv['eisAlsErEenPlaatjeKomt'] = 'het gekozen groepje niet alleen met kleur markeren: ook omcirkelen of arceren (les 11; Z-#525)'
    it['visual'] = nv
    slog(it, 'G7-Z525 (review batch 1 Didactiek): visual.nodig gelijk binnen de welke-tekening/som-somtypes van DENK-02', 'visual.nodig', str(v.get('nodig')), 'True')
def pas_toe(it, slog):
    _v516(it, slog); _z525(it, slog)

# ---- V-#560 (recheck batch 1 Didactiek, verplicht vóór de hint-batch van VERH-02/VERH-04; opdracht 12:24) --------------------------------
# Procentitems waar het goede antwoord gelijk is aan de noemer uit de vraag (n = N² : 100): wie de noemer overneemt, heeft het goed.
# De voorstellen van Didactiek (6/30, 12/40, 3/20, 20/50, 14/40) staan al als ander item in de bank (de G7-bank heeft 0 dubbele opgaven per doel),
# dus vergelijkbare paren die nog niet bestaan, met dezelfde N waar het kan en waar mogelijk hetzelfde antwoord. Afleiders uit dezelfde denkfouten
# als het oude item (claudeDenkfouten): andere deel = 100 − p, nul-fout = p : 10 (of × 10), getal overgenomen = n, omgekeerd gedeeld = N : n × 100.
# Elk paar nagerekend met tools/routes_check.py: geen route op het goede antwoord, en het antwoord is geen getal uit de vraag (ANTWVRAAG-check).
# Ook (zelfde regel, gevonden met de nieuwe check): 6 typitems in GET-05 #3 'a/n − b/n' met a = 2b: het afgetrokken stuk is het goede antwoord.
V560 = {      # claudeId: (opgave, {oud: nieuw} voor antwoord en opties, nieuwe denkfout-sleutels)
    '2a76c00a-b2ba-4bbc-8e40-caea2a1fb9f0': ('Hoeveel procent is 24 van 30?', {'30%': '80%', '70%': '20%', '3%': '8%'}),          # VERH-02 bank-814 (was 9 van 30)
    '8b2b0723-9c8d-441c-a213-4f6ea73d89a2': ('Hoeveel procent is 28 van 40?', {'40%': '70%', '4%': '7%', '16%': '28%'}),          # VERH-02 bank-897 (was 16 van 40)
    'ef987199-c0f5-440d-913a-98c02a4b4f74': ('Hoeveel procent is 14 van 20?', {'20%': '70%', '80%': '30%', '2%': '7%'}),          # VERH-02 bank-983 (was 4 van 20)
    '36577967-034b-4139-8d05-9070b20ded44': ('Schrijf 3/15 in procenten.', {'20%': '20%', '4%': '3%', '2%': '2%'}),               # VERH-04 bank-040 (was 4/20)
    '6c22fa5e-4ebb-41eb-91c0-61a122df1c79': ('Schrijf 9/45 in procenten.', {'50%': '20%', '200%': '500%', '500%': '200%'}),       # VERH-04 bank-064 (was 25/50)
    'b984782d-103b-4235-a32d-a70ccfa6e3d6': ('Schrijf 14/35 in procenten.', {'40%': '40%', '250%': '250%', '400%': '400%'}),      # VERH-04 bank-101 (was 16/40)
    # GET-05 #3 (typen): a/n − b/n met a = 2b → b één groter of kleiner (199: twee groter); sleutels 'noemers opgeteld' (a − b)/2n en 'erbij gedaan' (a + b)/n
    '1594b165-3094-47b9-85c5-f96eeecd9c43': ('Reken uit: 6/8 − 4/8 = ? Typ een breuk.', {'3/8': '2/8', '3/16': '2/16', '9/8': '10/8'}),
    '438a6c6b-ea80-4c1f-b189-ef6aad350c4c': ('Reken uit: 6/10 − 2/10 = ? Typ een breuk.', {'3/10': '4/10', '3/20': '4/20', '18/10': '8/10'}),
    '56b59828-0e45-4772-982a-7ffc423bf9ed': ('Reken uit: 8/11 − 6/11 = ? Typ een breuk.', {'4/11': '2/11', '4/22': '2/22', '5/11': '14/11'}),      # niet 8/11 − 5/11: dat is bank-229 (dubbel) en dan schuift de elfden-spreiding
    '58d84320-c0cf-4171-9cff-1001d1a7cd12': ('Reken uit: 10/12 − 6/12 = ? Typ een breuk.', {'5/12': '4/12', '6/12': '4/24', '15/12': '16/12'}),
    'b5c34a41-d9a4-4a01-a49c-9c6f2d106235': ('Reken uit: 8/9 − 5/9 = ? Typ een breuk.', {'4/9': '3/9', '3/9': '3/18', '12/9': '13/9'}),
    'e5748898-6f21-4d23-81d7-78dec5fc52fa': ('Reken uit: 6/7 − 4/7 = ? Typ een breuk.', {'3/7': '2/7', '3/14': '2/14', '2/7': '10/7'}),
}
# Vaste teksten zonder getallen voor de GET-05-sleutels (uit de items zelf): 'Tel de stukjes nog eens: 6 − 3 = ?' noemde de oude getallen.
T560_NOEMER = 'De noemer zegt in hoeveel stukken het geheel is verdeeld. Die verandert niet als je stukken bij elkaar doet.'
T560_ERBIJ = 'Lees de vraag nog eens: komt er iets bij, of gaat er iets af?'
def _v560(it, slog):
    spec = V560.get(it['bron'].get('claudeId'))
    if not spec: return
    o_new, m = spec; oud = it['opgave']
    typ = '−' in o_new
    assert it['antwoord'] in m, (it['id'], it['antwoord'])
    it['opgave'] = o_new
    it['antwoord'] = m[it['antwoord']]
    if it.get('opties'):
        for o in it['opties']: o['tekst'] = m.get(o['tekst'], o['tekst'])
        it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
        if it.get('antwoordDetail'): it['antwoordDetail']['juisteOptieTekst'] = it['antwoord']
    if typ:
        a = it['antwoord']; n_ = a.split('/')[1]
        fh = [{'stap': None, 'fout': k, 'uitleg': T560_NOEMER if k.split('/')[1] != n_ else T560_ERBIJ} for k in m.values() if k != a]
        it['antwoordOokGoed'] = []
        if isinstance(it.get('antwoordDetail'), dict) and 'accept' in it['antwoordDetail']: it['antwoordDetail']['accept'] = [a]
        it['extraVelden']['claudeKaleSom'] = o_new.replace('Reken uit: ', '').replace(' = ? Typ een breuk.', '')
        it['extraVelden']['claudeDenkfouten'] = [{'fout': f['fout'], 'denkfout': 'teller-en-noemer-optellen' if f['uitleg'] == T560_NOEMER else 'verkeerde-bewerking'} for f in fh]
    else:
        fh = [dict(f, fout=m.get(f['fout'], f['fout'])) for f in it['foutHints']]
        it['extraVelden']['claudeDenkfouten'] = [dict(d, fout=m.get(d['fout'], d['fout'])) for d in it['extraVelden'].get('claudeDenkfouten') or []]
    it['foutHints'] = fh
    it['foutHintsTekst'] = ' · '.join(f"{f['fout']} → {f['uitleg']}" for f in fh) or None
    it['extraVelden']['claudeFoutHints'] = [dict(f) for f in fh]
    it['merge']['v560'] = {'opgaveOud': oud, 'vervangen': m, 'reden': "V-#560: het goede antwoord was een getal uit de vraag"}
    slog(it, 'G7-V560 (recheck batch 1 Didactiek): goed antwoord was een getal uit de vraag; nieuwe getallen en afleiders', 'opgave', oud, o_new)
_pas_toe_v516 = pas_toe
def pas_toe(it, slog):
    _pas_toe_v516(it, slog); _v560(it, slog)

# ---- Oef-#428 (Oefeningen ronde 1c, les 145): toevallige treffers op het goede antwoord in DENK-03 → nieuwe getallen (Oefeningen' voorstel) ------
# nrO 4: 16 = 4 × 4 (en 1 verdubbeld 4 keer) → begin bij 3: 3, 6, 12, 24, 48; afleiders 24 (een keer te weinig) en 11 (steeds twee erbij: 3 + 4 × 2).
# nrO 10: 9 = 5 + 4 (en 8 + 5 − 4) → schrift 3 euro: 8 + 5 − 3 = 10; afleiders 13 (stap twee vergeten) en 16 (prijs erbij opgeteld).
# De regels '8'/'9' en '17' in batch 1 schrijft Oefeningen daarna om (tot dan lezen ze niet: ONLEESBAAR-WARN).
# ---- Oef-#430: DENK-03 nrO 21 de stappen in de vraag nummeren (de hints zeggen 'het begingetal nemen is stap één') -------------------------------
V428 = {
    '04f95b4f-49bf-4663-80cd-1d60d1e149e7': ('Je begint bij 3 en verdubbelt het getal 4 keer. Welk getal krijg je dan?', {'16': '48', '8': '24', '9': '11'},
        'Je krijgt na elke stap 6, 12, 24 en 48. Dat zijn vier verdubbelingen. De uitkomst is 48.', 'Oef-#428'),
    'f8815a62-0b52-4d14-acb7-4e116f859a65': ('Je hebt 8 euro gespaard. Stap 1: je krijgt 5 euro zakgeld. Stap 2: je koopt een schrift van 3 euro. Hoeveel euro heb je dan?',
        {'9 euro': '10 euro', '17 euro': '16 euro', '13 euro': '13 euro'},
        '8 euro plus 5 euro is 13 euro. Daar gaat 3 euro af voor het schrift. Je houdt 10 euro over.', 'Oef-#428'),
    'f09a96ba-3747-48d8-8951-e3ef8e7ffb74': ('Stap 1: neem 30. Stap 2: haal er 6 af. Stap 3: deel door 4. Stap 4: tel er 10 bij op. Iemand schreef na elke stap het getal op: 30, 24, 8, 18. Bij welke stap ging het mis?',
        {}, None, 'Oef-#430'),      # + Z-#581 (review batch 2 Didactiek): 'Iemand schreef na elke stap het getal op: …'
    # ---- Review batch 2 Didactiek (build 12:32:32, taal: fix; zachte datapunten voor Overzicht) ----
    # Z-#574 nrO 16: interpunctie van de kop gelijk ('Recept. Stap 1: pak …').
    '720ec254-5639-4e75-9fd0-ade0214bade0': ('Recept. Stap 1: pak 3 glazen. Stap 2: pers voor elk glas 2 sinaasappels. Hoeveel sinaasappels pers je?', {}, None, 'Z-#574'),
    # Z-#575 nrO 24: 20 g boter per koekje is fors → 12 koekjes 60 g, 36 koekjes, bewering 120 g; goed 180 g (×3), afleiders ×2 en 60 : 3.
    '09707010-7042-4310-bbcc-e52a7774e6cf': ('Voor 12 koekjes gebruik je 60 g boter. Je wilt 36 koekjes bakken. Iemand zegt dat je dan 120 g boter nodig hebt. Klopt dat?',
        {'Nee, het moet 360 g zijn': 'Nee, het moet 180 g zijn', 'Ja, 240 g klopt': 'Ja, 120 g klopt', 'Nee, het moet 40 g zijn': 'Nee, het moet 20 g zijn'},
        '36 koekjes is 3 keer zoveel als 12 koekjes. Dus neem je ook 3 keer 60 g boter. Dat is 180 g.', 'Z-#575'),
}
REDEN428 = {'Oef-#428': 'toevallige treffer op het goede antwoord (nieuwe getallen van Oefeningen)',
            'Oef-#430': "stappen in de vraag genummerd (Oef-#430) en 'Iemand schreef na elke stap het getal op' (Z-#581)",
            'Z-#574': "interpunctie kop gelijk: 'Recept. Stap 1: pak …' (review batch 2 Didactiek)",
            'Z-#575': '20 g boter per koekje was fors: 12 koekjes 60 g → 36 koekjes 180 g (review batch 2 Didactiek)'}
# Z-#576: DENK-03 bank-014 en bank-023 zijn alleen tekst (stappen uitrekenen); Claudes 'Visual: nodig' klopt niet → visual niet nodig, wel live.
Z576 = {'935f210d-6ff4-4362-ab7b-c5784ac6765e', 'cf0a8dab-76a2-4ca5-ba5e-f5b459951525'}
def _z576(it, slog):
    if it['bron'].get('claudeId') not in Z576: return
    v = it.setdefault('visual', {}); oud = v.get('nodig')
    v['nodig'] = False; v.pop('nietLiveZonderBeeld', None)
    v['toelichting'] = "Z-#576 (review batch 2 Didactiek): alleen tekst (stappen uitrekenen); Claudes 'Visual: nodig' klopte niet"
    it['merge']['z576'] = True
    slog(it, 'G7-Z576 (review batch 2 Didactiek): visual niet nodig, tekstitem', 'visual.nodig', str(oud), 'False')
def _v428(it, slog):
    spec = V428.get(it['bron'].get('claudeId'))
    if not spec: return
    o_new, m, uitleg, nr = spec; oud = it['opgave']
    it['opgave'] = o_new
    if m:
        assert it['antwoord'] in m, (it['id'], it['antwoord'])
        it['antwoord'] = m[it['antwoord']]
        for o in it['opties']: o['tekst'] = m.get(o['tekst'], o['tekst'])
        it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
        it['antwoordDetail']['juisteOptieTekst'] = it['antwoord']
        fh = [dict(f, fout=m.get(f['fout'], f['fout'])) for f in it['foutHints']]
        it['foutHints'] = fh
        it['foutHintsTekst'] = ' · '.join(f"{f['fout']} → {f['uitleg']}" for f in fh) or None
        it['extraVelden']['claudeFoutHints'] = [dict(f, fout=m.get(f['fout'], f['fout'])) for f in it['extraVelden'].get('claudeFoutHints') or []]
        it['extraVelden']['claudeDenkfouten'] = [dict(d, fout=m.get(d['fout'], d['fout'])) for d in it['extraVelden'].get('claudeDenkfouten') or []]
    if uitleg: it['extraVelden']['claudeUitleg'] = uitleg
    k = nr.replace('Oef-#', 'oef').replace('Z-#', 'z')
    it['merge'][k] = {'opgaveOud': oud, 'vervangen': m, 'reden': REDEN428[nr]}
    slog(it, f'G7-{nr}: ' + REDEN428[nr], 'opgave', oud, o_new)
_pas_toe_v560 = pas_toe
def pas_toe(it, slog):
    _pas_toe_v560(it, slog); _v428(it, slog); _z576(it, slog)
