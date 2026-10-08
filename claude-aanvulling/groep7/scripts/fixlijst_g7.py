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

# ---- Review batch 3 Didactiek (builds 12:44:21 en 12:52:39; opdracht 12:55) -------------------------------------------------------------
# V-#607 (verplicht): GET-04 nrO 9 hetzelfde ding in beide zinnen; nrO 5 logische contexten (kilo bij iets wat je weegt, verdelen over iets dat
# kan krijgen) en 115 : 8 / 241 : 8 (duizendsten, V-#604) → delingen die op honderdsten uitkomen. Z-#609 (zacht): het goede antwoord was een
# getal uit de vraag: GET-04 nrO 5 '9 liter : 3 = 3' en GET-03 nrO 2 '1,2 − 0,6 = 0,6'. Alles nagerekend (eerst het hele getal, rest achter de komma).
# spec: (opgave, {oud: nieuw} voor antwoord en Claude-sleutels, {extraVelden-veld: waarde}, {Claude-sleutel: Claudes uitleg}, getallenruimte, nr)
V607 = {
    '34e916ac-94c0-41e8-975c-8bc1cea363b2': ('Een pakket weegt 6,3 kg. Hoeveel wegen 10 pakketten?', {}, {}, {}, None, 'V-#607'),
    '44c39ce2-9454-48f7-8f27-c4775c359ca3': ('Een pakket weegt 4,7 kg. Hoeveel wegen 5 pakketten?', {}, {}, {}, None, 'V-#607'),
    '94cab6bc-635d-4acc-a430-e967b0167dbb': ('Een pakket weegt 2,6 kg. Hoeveel wegen 3 pakketten?', {}, {}, {}, None, 'V-#607'),
    'a9b3dbe7-38c3-44f0-b11e-d1ec953b29d6': ('Een pakket weegt 3,9 kg. Hoeveel wegen 12 pakketten?', {}, {}, {}, None, 'V-#607'),
    '2f9c6bcd-6570-4851-b3d7-95c2cd82f102': ('114 kilo zand wordt eerlijk verdeeld over 8 zakken. Hoeveel kilo krijgt elke zak?', {'14,375': '14,25', '14': '14', '14,3': '14,2'},
        {'claudeKaleSom': '114 : 8', 'claudeUitleg': '8 × 14 = 112, blijft 2 over.\n2 : 8 = 0,25.\nSamen 14,25.', 'claudeThema': None},
        {'14': 'Er blijft 2 kilo over. Die verdeel je ook, in stukjes.', '14,2': 'De rest 2 is niet zomaar het cijfer achter de komma. Deel de rest ook door 8.'},
        'kommagetallen (2 cijfers achter de komma)', 'V-#607'),
    'b42049f4-e785-4306-9a98-ddd0d553be4b': ('242 kilo appels wordt eerlijk verdeeld over 8 kratten. Hoeveel kilo krijgt elke krat?', {'30,125': '30,25', '30': '30', '30,1': '30,2'},
        {'claudeKaleSom': '242 : 8', 'claudeUitleg': '8 × 30 = 240, blijft 2 over.\n2 : 8 = 0,25.\nSamen 30,25.', 'claudeThema': None},
        {'30': 'Er blijft 2 kilo over. Die verdeel je ook, in stukjes.', '30,2': 'De rest 2 is niet zomaar het cijfer achter de komma. Deel de rest ook door 8.'},
        'kommagetallen (2 cijfers achter de komma)', 'V-#607'),
    'b5096450-e218-4bc8-b9e3-9b97275fce3a': ('81 kilo aarde wordt eerlijk verdeeld over 4 bakken. Hoeveel kilo krijgt elke bak?', {}, {'claudeThema': None}, {}, None, 'V-#607'),
    '45395d2c-9299-4bac-b771-9ad3277c263e': ('8,4 liter water wordt eerlijk verdeeld over 6 flessen. Hoeveel liter krijgt elke fles?', {}, {'claudeThema': None}, {}, None, 'V-#607'),
    'a46cce53-ecd4-4108-823f-918585082315': ('7,6 liter water wordt eerlijk verdeeld over 4 emmers. Hoeveel liter krijgt elke emmer?', {}, {'claudeThema': None}, {}, None, 'V-#607'),
    'cbe2514c-b4ec-4b64-9c1e-e1f655f44240': ('4,5 liter limonade wordt eerlijk verdeeld over 3 kannen. Hoeveel liter krijgt elke kan?', {}, {'claudeThema': None}, {}, None, 'V-#607'),
    'cd78d15a-10b5-439c-aac2-264620ad32dd': ('18 liter water wordt eerlijk verdeeld over 3 drinkbakken. Hoeveel liter krijgt elke drinkbak?', {'3': '6', '30': '60', '4,0': '7'},
        {'claudeKaleSom': '18,0 : 3', 'claudeUitleg': 'Reken zonder komma: 180 : 3 = 60.\nZet de komma terug: 6,0.'},
        {'60': 'Komma terugzetten: het antwoord heeft één cijfer achter de komma.', '7': 'Controleer. 3 × jouw antwoord moet 18 zijn.'}, None, 'Z-#609'),
    'c88c4cd3-a8ee-4e6f-98f4-271088797d45': ('1,4 − 0,6 =', {'0,6': '0,8', '6': '8', '0,7': '0,9'}, {'claudeKaleSom': '1,4 − 0,6'}, {}, None, 'Z-#609'),
}
REDEN607 = {'V-#607': 'context klopte niet (hetzelfde ding / logische context; 115 : 8 en 241 : 8 → honderdsten), review batch 3 Didactiek',
            'Z-#609': 'het goede antwoord was een getal uit de vraag (review batch 3 Didactiek)'}
def _v607(it, slog):
    spec = V607.get(it['bron'].get('claudeId'))
    if not spec: return
    o_new, m, ev, cfh, gr, nr = spec; oud = it['opgave']
    it['opgave'] = o_new
    if m:
        assert it['antwoord'] in m, (it['id'], it['antwoord'])
        it['antwoord'] = m[it['antwoord']]
        if isinstance(it.get('antwoordDetail'), dict) and 'accept' in it['antwoordDetail']: it['antwoordDetail']['accept'] = [it['antwoord']]
        e = it['extraVelden']
        e['claudeFoutHints'] = [dict(f, fout=m.get(f['fout'], f['fout']), uitleg=cfh.get(m.get(f['fout'], f['fout']), f['uitleg'])) for f in e.get('claudeFoutHints') or []]
        e['claudeDenkfouten'] = [dict(d, fout=m.get(d['fout'], d['fout'])) for d in e.get('claudeDenkfouten') or []]
        it['foutHints'] = [dict(f, fout=m.get(f['fout'], f['fout'])) for f in it.get('foutHints') or []]
    for k, v in ev.items(): it['extraVelden'][k] = v
    if gr: it['getallenruimte'] = gr
    it['merge'][nr.replace('-#', '').lower()] = {'opgaveOud': oud, 'vervangen': m, 'reden': REDEN607[nr]}
    slog(it, f'G7-{nr}: ' + REDEN607[nr], 'opgave', oud, o_new)
# V-#608 (verplicht): een opgave die met een kleine letter begint (GET-03 nrO 3/4: «de kleedkamer heeft …», de kop begon met [plek]) → hoofdletter.
def _v608(it, slog):
    o = it.get('opgave') or ''
    if o[:1].isalpha() and o[:1].islower():
        it['opgave'] = o[0].upper() + o[1:]; it['merge']['v608'] = True
        slog(it, 'G7-V608 (review batch 3 Didactiek): hoofdletter aan het begin van de vraag', 'opgave', o, it['opgave'])
_pas_toe_z576 = pas_toe
def pas_toe(it, slog):
    _pas_toe_z576(it, slog); _v607(it, slog); _v608(it, slog)

# ---- Oef-#443 (data, les 184; steering 13:08): MEET-03 #9/#10 «Een bak in het bos/nest/moeras …» en «Een doos voor poesjes/sterren …» passen
# niet bij inhoud. #9 (m³): een bak die zo groot kan zijn, naar de hoogte (≤ 1 m zandbak, ≤ 2 m aquarium, hoger container); een tweede item met
# dezelfde getallen krijgt de tweede vorm (geen dubbele vraag). #10 (cm³): sterren → knikkers, poesjes → blokjes. De kop blijft 'Een bak is …'.
V443_BAK = [(1, ('Een zandbak', 'Een vijver in het park')), (2, ('Een aquarium in de dierentuin', 'Een vijver in het park')),      # Z-#637: geen waterbak van 30 m³
            (99, ('Een container', 'Een opslagbak in de schuur'))]
V443_DOOS = {'sterren': 'knikkers', 'poesjes': 'blokjes', 'truien': 'kralen', 'eieren': 'krijtjes'}      # + V-#631 (review batch 4): trui en ei passen niet
_V443_GEZIEN = set()
def _v443(it, slog):
    o = it.get('opgave') or ''
    m = re.match(r'^Een bak (?:in|op) (?:de|het) [a-zà-ÿ]+ (is ([\d,]+) m lang, [\d,]+ m breed en ([\d,]+) m hoog\. Hoeveel m³ gaat erin\?)$', o)
    if m:
        h = float(m.group(3).replace(',', '.')); vormen = next(v for g, v in V443_BAK if h <= g)
        rest = m.group(1); nieuw = f'{vormen[0]} {rest}' if (vormen[0], rest) not in _V443_GEZIEN else f'{vormen[1]} {rest}'
        _V443_GEZIEN.add((nieuw.split(' is ')[0], rest))
    else:
        m = re.match(r'^Een doos voor (sterren|poesjes|truien|eieren) (is .* cm hoog\. Hoeveel cm³ past erin\?)$', o)
        if not m: return
        nieuw = f'Een doos voor {V443_DOOS[m.group(1)]} {m.group(2)}'
    if nieuw.startswith('Een vijver'): nieuw = re.sub(r' m hoog\. Hoeveel m³ gaat erin\?$', ' m diep. Hoeveel m³ water gaat erin?', nieuw)      # Z-#637
    it['opgave'] = nieuw; it['extraVelden']['claudeThema'] = None
    it['merge']['oef443'] = {'opgaveOud': o, 'reden': 'Oef-#443: context past bij inhoud (les 184)'}
    slog(it, 'G7-Oef-#443: logische context bij inhoud (aquarium, zandbak, container, doos voor knikkers)', 'opgave', o, nieuw)
# ---- Oef-#440 (data, steering 13:08): Claude-sleutels als '20,0' / '300,0' / '5,0' (MEET-03 #9, VERH-04 #3) worden het hele getal ('20');
# een sleutel die dan dubbel is, valt weg (de eerste blijft). Niet bij afronden ('… cijfer achter de komma'): daar hoort de vorm bij de vraag.
def _v440(it, slog):
    if re.search(r'achter de komma', it.get('opgave') or ''): return
    e = it['extraVelden']; oud = [d.get('fout') for d in e.get('claudeDenkfouten') or []] + [f.get('fout') for f in e.get('claudeFoutHints') or []]
    if not any(re.fullmatch(r'\d+,0+', str(k)) for k in oud): return
    for veld in ('claudeDenkfouten', 'claudeFoutHints'):
        lijst, gezien = [], set()
        for d in e.get(veld) or []:
            k = re.sub(r'^(\d+),0+$', r'\1', str(d.get('fout')))
            if k in gezien: continue
            gezien.add(k); lijst.append(dict(d, fout=k))
        if veld in e: e[veld] = lijst
    it['merge']['oef440'] = {'sleutelsOud': oud}
    slog(it, "G7-Oef-#440: Claude-sleutel 'n,0' → het hele getal", 'claudeSleutels', oud, [d.get('fout') for d in e.get('claudeDenkfouten') or []])

# ---- Review batch 4 Didactiek (build 13:13:00; opdracht 13:17) -----------------------------------------------------------------------------
from fractions import Fraction as _Fr
import json as _json, os as _os, random as _random, hashlib as _hashlib
def _zet(it, slog, code, reden, opgave, antwoord=None, denk=None, kale=None, uitleg=None, jr=None):
    """Zet opgave (en antwoord, Claude-sleutels als [(fout, denkfout, uitleg)], claudeKaleSom/claudeUitleg, visual.jsRender-velden) en logt het."""
    oud = {'opgave': it['opgave'], 'antwoord': it['antwoord'], 'sleutels': [d.get('fout') for d in it['extraVelden'].get('claudeDenkfouten') or []]}
    it['opgave'] = opgave
    if antwoord is not None:
        it['antwoord'] = antwoord
        if isinstance(it.get('antwoordDetail'), dict) and 'accept' in it['antwoordDetail']: it['antwoordDetail']['accept'] = [antwoord]
    e = it['extraVelden']
    if denk is not None:
        e['claudeDenkfouten'] = [{'fout': f, 'denkfout': d} for f, d, u in denk]
        e['claudeFoutHints'] = [{'stap': None, 'fout': f, 'uitleg': u} for f, d, u in denk]
        it['foutHints'] = []
    if kale is not None: e['claudeKaleSom'] = kale
    if uitleg is not None: e['claudeUitleg'] = uitleg
    if jr: it['visual']['jsRender'].update(jr)
    it['merge'][code] = dict(oud, reden=reden)
    slog(it, f'G7-{code}: {reden}', 'opgave', oud['opgave'], opgave)

# Z-#631 (MEET-02 nr 3, vijver): geen vijver van 2 × 2 (zijde + zijde = zijde × zijde); 3 × 3 of 5 × 5, niet 4 × 4.
Z631 = {'1ad67d67-b8f0-46d9-aed9-9a80e703235c': (6, 6, 3), '7bfbbf0b-9738-4339-ad9e-45d232aabcca': (12, 6, 5),
        '8c540a3d-62e4-418b-996b-3d1dd961cfcb': (9, 7, 3), '9d7f6cb3-0746-4dad-8d5e-a8f863604a8d': (9, 6, 5)}
def _z631(it, slog):
    if it['bron'].get('claudeId') not in Z631: return
    l, b, z = Z631[it['bron']['claudeId']]; t = l * b; v = z * z; a = t - v
    assert z + z != v and a > 0 and a not in (t, t - z, t + v)
    _zet(it, slog, 'z631', 'Z-#631: vijver van 2 × 2 → %d × %d (review batch 4)' % (z, z),
         f'Een tuin van {l} bij {b} meter heeft een vierkante vijver van {z} bij {z} meter. Hoeveel m² gras is er?', str(a),
         [(str(t), 'deel-vergeten-bij-splitsen', 'De vijver is geen gras. Haal die eraf.'),
          (str(t - z), 'omtrek-oppervlakte-verwisseld', f'De vijver is {z} × {z} m², niet {z} m².'),
          (str(t + v), 'verkeerde-bewerking', 'De vijver gaat eraf, niet erbij.')],
         f'{l} × {b} − {z} × {z}', f'Hele tuin: {l} × {b} = {t} m².\nVijver: {z} × {z} = {v} m².\nGras: {t} − {v} = {a} m².')

# Z-#632 (MEET-02 nr 1, driehoek): 6 × 3 (basis + hoogte = 9 = het antwoord) → 6 × 9; 4 × 3 ('twee erbij' 14 = omtrek) → 4 × 6.
# (Didactiek noemde 6 × 5 en 3 × 6: 6 × 5 is 014 met basis en hoogte omgedraaid, en bij 3 × 6 is basis + hoogte = 9 = het antwoord.)
Z632 = {'2f4a9a88-9e60-463a-9b20-dd611e43370e': (6, 9), '0956141f-77ae-4de4-bae3-e6b733342af1': (4, 6)}
def _z632(it, slog):
    if it['bron'].get('claudeId') not in Z632: return
    bs, h = Z632[it['bron']['claudeId']]; r = bs * h; a = r // 2
    assert r % 2 == 0 and bs + h != a and r + 2 != 2 * (bs + h)
    o = re.sub(r'basis van \d+ m en een hoogte van \d+ m', f'basis van {bs} m en een hoogte van {h} m', it['opgave'])
    _zet(it, slog, 'z632', f'Z-#632: driehoek {bs} × {h} (geen toevallige treffer, review batch 4)', o, str(a),
         [(str(r), 'omtrek-oppervlakte-verwisseld', 'Dat is de oppervlakte van de rechthoek eromheen. Een driehoek is de helft: deel door 2.'),
          (str(bs + h), 'optellen-ipv-vermenigvuldigen', 'Oppervlakte is vermenigvuldigen: basis × hoogte, en dan delen door 2.'),
          (str(r + 2), 'verkeerde-bewerking', 'Delen door 2, niet optellen.')],
         f'{bs} × {h} : 2', f'Oppervlakte driehoek = basis × hoogte : 2 = {bs} × {h} : 2 = {r} : 2 = {a} m².', {'basis': bs, 'hoogte': h})

# Z-#633 (MEET-03 nr 1): 30 cm³ op een bodem van 2 × 3 (lengte + breedte = 5 = de hoogte) → 78 / 84 cm³ (hoogte 13 / 14).
# Geen treffer met l + b, l × b, l of b, ook niet ± 1.
Z633 = {'f12b64a0-579a-490d-a491-025a91f1b573': (2, 3, 13), 'c772577a-643a-4743-953b-3b7044d90e49': (3, 2, 14)}
def _z633(it, slog):
    if it['bron'].get('claudeId') not in Z633: return
    l, b, h = Z633[it['bron']['claudeId']]; v = l * b * h
    assert not ({l + b, l * b, l, b} & {h - 1, h, h + 1})
    _zet(it, slog, 'z633', f'Z-#633: {v} cm³ op {l} × {b} (hoogte {h}, review batch 4)',
         f'Een balk heeft een inhoud van {v} cm³. De bodem is {l} bij {b} cm. Hoe hoog is de balk in cm?', str(h),
         [(str(l + b), 'optellen-ipv-vermenigvuldigen', 'De bodem is lengte keer breedte, niet plus.'),
          (str(h + 1), 'een-ernaast', f'Controleer: {l} × {b} × jouw antwoord moet {v} zijn.')],
         f'{v} : ({l} × {b})', f'Bodem: {l} × {b} = {l * b} cm².\n{v} : {l * b} = {h}.\nDe balk is {h} cm hoog.')

# Z-#635 (MEET-02 nr 2): een L-vormig hok van 31–84 m² → een L-vormige tuin.
def _z635(it, slog):
    o = it.get('opgave') or ''
    if not o.startswith('Een L-vormig hok bestaat uit'): return
    n = o.replace('Een L-vormig hok bestaat uit', 'Een L-vormige tuin bestaat uit').replace('Hoeveel m² is het hok?', 'Hoeveel m² is de tuin?')
    assert n != o and 'hok' not in n
    _zet(it, slog, 'z635', 'Z-#635: L-vormig hok → L-vormige tuin (review batch 4)', n)

# Z-#636 (GET-05 nr 7): botten, noten en sterren zijn niet blauw → kralen, knikkers, ballonnen.
Z636 = {'0a74a14b-7c5a-4dc7-9cfc-0d1c551b1e14': ('botten', 'kralen'), '569b7672-9dc8-4a7d-a71b-9e3c75204d22': ('botten', 'knikkers'),
        'a873e473-4743-4fc8-a906-d310968de19c': ('noten', 'ballonnen'), 'ffe61033-c48b-43c2-bfd6-f5e923e033fd': ('sterren', 'kralen')}
def _z636(it, slog):
    if it['bron'].get('claudeId') not in Z636: return
    a, b = Z636[it['bron']['claudeId']]; assert f' van de {a} is blauw' in it['opgave'], it['opgave']
    it['extraVelden']['claudeThema'] = None
    _zet(it, slog, 'z636', f'Z-#636: {a} → {b} (review batch 4)', it['opgave'].replace(f' van de {a} is', f' van de {b} is'))

# VERH-04 nrO 3 (steering 13:17): «50% van de poesjes is kapot» / «75% van de stappen is kapot» → lampjes / ballonnen. Antwoord blijft (50 : 100 = 0,5; 75 : 100 = 0,75).
V04K = {'34723c79-a658-468a-a1b1-54be025835d2': ('poesjes', 'lampjes'), 'e778d3b5-9e6c-474b-a2ad-f318366a6501': ('stappen', 'ballonnen')}
def _v04k(it, slog):
    if it['bron'].get('claudeId') not in V04K: return
    a, b = V04K[it['bron']['claudeId']]; assert f'van de {a} is kapot' in it['opgave'], it['opgave']
    p = int(re.match(r'(\d+)%', it['opgave']).group(1)); assert _Fr(it['antwoord'].replace(',', '.')) == _Fr(p, 100)
    it['extraVelden']['claudeThema'] = None
    _zet(it, slog, 'kapot', f'VERH-04 nrO 3: {a} → {b} (logische context, steering 13:17)', it['opgave'].replace(f'van de {a} is', f'van de {b} is'))

# Z-#630 (GET-05 nr 1/2 = nrO 6/7, grootst/kleinst): in alle 318 items was het antwoord de breuk met de kleinste (grootst) of grootste
# (kleinst) noemer. Elk derde item (op id, bevroren/z630_ids.json, 105 items) wordt nieuw: gelijke tellers (daar klopt de noemer-regel)
# en items waar de noemer-truc het foute antwoord geeft (grootst: de breuk met de grootste noemer is het grootst; kleinst: die met de
# kleinste noemer is het kleinst); een derde gelijke tellers, twee derde noemer-truc fout. Zelfde noemerbereik als het oude item; echte breuken, geen gelijke waarden of noemers, verschil ≥ 1/24.
_Z630 = _json.load(open(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'bevroren', 'z630_ids.json')))['items']
_Z630_GEZIEN = set()
# Z-#651 (review batch 5): nog 89 items (bevroren/z651_ids.json) als tegenvoorbeeld, zodat de noemer-truc in ongeveer de helft werkt
_Z630.update(_json.load(open(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'bevroren', 'z651_ids.json')))['items'])
def _z630_maak(cid, grootst, soort, nmax):
    rnd = _random.Random(int(_hashlib.md5(cid.encode()).hexdigest()[:8], 16))
    for _ in range(5000):
        ns = sorted(rnd.sample(range(3, nmax + 1), 3))
        if soort == 'gelijke tellers':
            t = rnd.randint(1, ns[0] - 1); fr = [(t, n) for n in ns]
        else:
            fr = [(rnd.randint(1, n - 1), n) for n in ns]
        w = [_Fr(a, b) for a, b in fr]
        if len(set(w)) < 3 or any(_Fr(a, b).denominator != b for a, b in fr if soort != 'gelijke tellers'): continue
        if min(abs(x - y) for x in w for y in w if x != y) < _Fr(1, 24): continue
        doel = max(w) if grootst else min(w); i = w.index(doel)
        if soort == 'gelijke tellers': ok = i == (0 if grootst else 2)
        else: ok = i == (2 if grootst else 0) and fr[1][0] != fr[i][0]
        if not ok: continue
        rnd.shuffle(fr)
        o = f"Welke breuk is het {'grootst' if grootst else 'kleinst'}? Kies uit {fr[0][0]}/{fr[0][1]}, {fr[1][0]}/{fr[1][1]} of {fr[2][0]}/{fr[2][1]}."
        if o in _Z630_GEZIEN: continue
        _Z630_GEZIEN.add(o); return o, f'{doel.numerator}/{doel.denominator}' if (doel.numerator, doel.denominator) in fr else None, fr
    raise AssertionError(('Z-#630 geen item', cid))
def _z630(it, slog):
    spec = _Z630.get(it['bron'].get('claudeId'))
    if not spec: return
    m = re.match(r'^Welke breuk is het (grootst|kleinst)\? Kies uit (\d+)/(\d+), (\d+)/(\d+) of (\d+)/(\d+)\.$', it['opgave'])
    assert m and m.group(1) == spec['vraag'], (it['id'], it['opgave'])
    grootst = spec['vraag'] == 'grootst'; nmax = max(int(m.group(k)) for k in (3, 5, 7))
    o, ans, fr = _z630_maak(it['bron']['claudeId'], grootst, spec['type'], nmax)
    w = {f'{a}/{b}': _Fr(a, b) for a, b in fr}
    ans = max(w, key=w.get) if grootst else min(w, key=w.get)      # het antwoord zoals het in de vraag staat (nagerekend)
    gelijk = spec['type'] == 'gelijke tellers'
    if gelijk:
        u = 'De tellers zijn gelijk. Hoe groter de noemer, hoe kleiner de stukken.'; dk = 'grotere-noemer-is-groter'
    else:
        u = 'Kijk niet alleen naar de noemer, maar ook naar de teller. Vergelijk met een half, of maak de noemers gelijk.'; dk = 'alleen-noemer-vergeleken'
    _zet(it, slog, 'z630', f"Z-#630: {spec['type']} (review batch 4)", o, ans, [(k, dk, u) for k in w if k != ans])
    it['merge']['z630']['soort'] = spec['type']


# ---- Open punten batch 1 (Oef-#431/#432/#433, Z-#521/#525) en GET-04 nrO 8 (opdracht 13:29) ----------------------------------------------
def _opties(it, slog, code, reden, opgave, opties, goed, denk, uitleg=None):
    """Meerkeuze: opgave, opties (lijst teksten, letters A, B, C …), goed = tekst van de juiste optie; denk = [(fout, denkfout, uitleg)]."""
    assert goed in opties and len(set(opties)) == len(opties)
    _zet(it, slog, code, reden, opgave, goed, denk, uitleg=uitleg)
    it['opties'] = [{'letter': chr(65 + k), 'tekst': t} for k, t in enumerate(opties)]
    it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    L = next(o['letter'] for o in it['opties'] if o['tekst'] == goed)
    it['antwoordDetail'] = dict(it.get('antwoordDetail') or {}, juisteOptie=L, juisteOptieTekst=goed)
def _r5(it, slog):
    cid = it['bron'].get('claudeId') or ''; o = it.get('opgave') or ''
    if cid.startswith('c564f424') and 'sportveld' in o:      # Oef-#433/Z-#521: DENK-02 #2, een sportveld van 20 bij 10 m is klein → speelveld (getallen blijven)
        _zet(it, slog, 'oef433', 'Oef-#433 (Z-#521): sportveld → speelveld (20 bij 10 m)', o.replace('Een sportveld is', 'Een speelveld is'))
    elif cid.startswith('77fa6bb3') and 'gekleurd' in it.get('optiesTekst', ''):      # Oef-#432 (Z-#525): DENK-02 #3 opties zonder kleur
        op = ['3 groepjes van 6, één groepje omcirkeld', '3 groepjes van 6, alle groepjes omcirkeld', '2 groepjes van 9, één groepje omcirkeld']
        _opties(it, slog, 'oef432', "Oef-#432 (Z-#525): 'gekleurd' → 'omcirkeld' in de opties", o, op, op[0],
                [(op[1], 'deel-van-geheel-verkeerd', 'Een derde betekent dat maar één van de gelijke groepjes telt.'),
                 (op[2], 'deel-van-geheel-verkeerd', 'Bij een derde teken je drie even grote groepjes, niet twee.')],
                'Bij een derde verdeel je 18 kinderen in 3 gelijke groepjes. Elk groepje heeft 6 kinderen. Eén groepje speelt bij de zandbak.')
    elif cid.startswith('236d9cca') and '8 eieren' in o:      # Oef-#433/Z-#521: DENK-02 #9, een eierdoos heeft 6 eieren
        op = ['5 + 6 = 11', '6 − 5 = 1', '5 × 6 = 30']; assert 5 * 6 == 30 and 5 + 6 == 11 and 6 - 5 == 1
        _opties(it, slog, 'oef433', 'Oef-#433 (Z-#521): eierdoos van 8 → 6 eieren', o.replace('8 eieren', '6 eieren'), op, op[2],
                [(op[0], 'optellen-ipv-vermenigvuldigen', 'In elke doos zitten evenveel eieren. Dan tel je niet één keer op, maar steeds hetzelfde aantal erbij.'),
                 (op[1], 'verkeerde-bewerking', 'Je haalt niets weg. Je hebt juist meerdere dozen met eieren samen.')],
                'Er zijn 5 dozen met elk 6 eieren. Dat is 6 + 6 + 6 + 6 + 6, en dat is hetzelfde als 5 × 6. Samen zijn dat 30 eieren.')
    elif cid.startswith('d4ceaeff') and 'steeds 5 meter' in o:      # Oef-#433/Z-#521: DENK-02 #12, lantaarnpalen staan geen 5 m uit elkaar → 20 m
        op = ['120 meter', '140 meter', '100 meter']; assert 6 * 20 == 120 and 7 * 20 == 140 and 5 * 20 == 100
        _opties(it, slog, 'oef433', 'Oef-#433 (Z-#521): lantaarnpalen 5 m → 20 m uit elkaar (7 palen: 6 × 20 = 120)', o.replace('steeds 5 meter', 'steeds 20 meter'), op, op[0],
                [(op[1], 'een-ernaast', 'Teken de palen als streepjes en tel de tussenruimtes. Dat zijn er minder dan het aantal palen.'),
                 (op[2], 'een-ernaast', 'Tel de tussenruimtes in je tekening nog eens na.')],
                'Bij 7 palen op een rij zitten 6 tussenruimtes. Elke tussenruimte is 20 meter. 6 × 20 is 120 meter.')
    elif cid.startswith('1df3773f') and 'poesje' in o:      # GET-04 nrO 8: een poesje weegt geen 3,3 gram → knikker
        n = o.replace('Eén poesje weegt', 'Eén knikker weegt').replace('100 poesjes', '100 knikkers'); assert 'poes' not in n
        e = it['extraVelden']; e['claudeThema'] = None
        e['claudeFoutHints'] = [dict(f, uitleg=f['uitleg'].replace('poesjes', 'knikkers')) for f in e.get('claudeFoutHints') or []]
        _zet(it, slog, 'knikker', 'GET-04 nrO 8: een poesje van 3,3 gram → een knikker (logische context)', n)
def _r5_av8(it, slog):
    cid = it['bron'].get('claudeId') or ''; o = it.get('opgave') or ''
    if cid.startswith('8f22bb4c') and 'fietsen met 3 wielen' in o:      # Oef-#433/Z-#521: DENK-02 #14, fietsen met 3 wielen → bakfietsen (getallen blijven)
        e = it['extraVelden']; e['claudeUitleg'] = (e.get('claudeUitleg') or '').replace('3 fietsen met 3 wielen', '3 bakfietsen met 3 wielen')
        _zet(it, slog, 'oef433', 'Oef-#433 (Z-#521): fietsen met 3 wielen → bakfietsen', o.replace('3 fietsen met 3 wielen', '3 bakfietsen met 3 wielen'))
_pas_toe_v608 = pas_toe
def pas_toe(it, slog):
    _pas_toe_v608(it, slog); _v443(it, slog); _v440(it, slog)
    _z630(it, slog); _z631(it, slog); _z632(it, slog); _z633(it, slog); _z635(it, slog); _z636(it, slog); _v04k(it, slog); _r5(it, slog)
def pas_toe_av8(it, slog):
    """Review batch 4 voor de aanvulling uit G8 (MEET-02 'claude-bank-terug-…', AV8.laad na de gewone pas_toe): Z-#631 en Z-#635, vóór de kop."""
    if 'z631' not in it['merge']: _z631(it, slog)
    if 'z635' not in it['merge']: _z635(it, slog)
    if 'oef433' not in it['merge']: _r5_av8(it, slog)

# ---------- Review batch 5 (Didactiek, build 13:48:53) ----------
# Z-#668 (Oef-#446): Claudes kommagetal-sleutels met een punt ('4.4', '6.7') in huisnotatie met een komma ('4,4'). Een punt met precies drie
# cijfers erachter is een duizendtal-punt en blijft. Balk kleuren (VERH-01 nrO 2, balk van twintig stukjes): halve stukjes kun je niet kleuren,
# dus geen sleutel '7.5'/'2.5'/'0.5': 75% → 70% en 25% → 100% (route 'elk stukje tien procent' komt dan op hele stukjes: 7 en 10);
# bij 5% bestaat zo'n route op hele stukjes niet en de entry heeft geen andere regel: dat item (fe3199aa) is geschrapt (build_g7, geschrapt_review5.json).
Z668_BALK = {'752ab991-37a9-42ec-8d56-b01775701a17': 70, 'bdd229da-3899-4842-92f8-47217067ac91': 100}
def _z668(it, slog):
    e = it['extraVelden']; cid = it['bron'].get('claudeId')
    if cid in Z668_BALK:
        p = Z668_BALK[cid]
        if p is None:
            weg = [d['fout'] for d in e.get('claudeDenkfouten') or [] if re.fullmatch(r'\d+\.\d', str(d.get('fout')))]
            _zet(it, slog, 'z668', f"Z-#668: sleutel {weg} (half stukje) vervalt (review batch 5)", it['opgave'], denk=[])
        else:
            n = p // 5
            _zet(it, slog, 'z668', f'Z-#668: {it["opgave"]} → {p}% (hele stukjes, review batch 5)', f'Kleur {p}% van de balk.', str(n),
                 [(str(p // 10), None, 'Elk stukje is 5%, niet 10%.')], f'{p}% van de balk',
                 f'De hele balk is 100%. Elk stukje is 5%. {p}% is {n} stukjes.')
        return
    for veld in ('claudeDenkfouten', 'claudeFoutHints'):
        for d in e.get(veld) or []:
            f = d.get('fout')
            if isinstance(f, str) and re.fullmatch(r'\d+\.\d{1,2}', f.strip()):
                d['fout'] = f.strip().replace('.', ',')
                if veld == 'claudeDenkfouten': slog(it, f"G7-z668: Z-#668 sleutel '{f}' → '{d['fout']}' (huisnotatie)", 'sleutel', f, d['fout'])
_pas_toe_r5 = pas_toe
def pas_toe(it, slog):
    _pas_toe_r5(it, slog); _z668(it, slog)
_pas_toe_av8_r5 = pas_toe_av8
def pas_toe_av8(it, slog):
    _pas_toe_av8_r5(it, slog)
    if 'z668' not in it['merge']: _z668(it, slog)

# ---------- Review batch 5 (Didactiek), verplicht: V-#664, V-#665, V-#666, V-#667; met Oef-#447/#448/#449/#450 en Z-#666 (#7) ----------
def _vervang(it, paren):
    """Woordvervanging in opgave, claudeKaleSom, claudeUitleg en Claudes uitleg per sleutel; geeft de nieuwe opgave."""
    e = it['extraVelden']; o = it['opgave']
    for a, b in paren:
        o = o.replace(a, b)
        for k in ('claudeKaleSom', 'claudeUitleg'):
            if e.get(k): e[k] = e[k].replace(a, b)
        for d in e.get('claudeFoutHints') or []:
            if d.get('uitleg'): d['uitleg'] = d['uitleg'].replace(a, b)
    return o
# V-#666: MEET-04 nrO 3/5, vorst binnen → buiten (de kop houdt 'in [plek]')
RV5_BINNEN = re.compile(r'\bin (?:de|het) (kantine|huis|school|kleedkamer|museum|gymzaal|klas)\b')
RV5_BUITEN = ['in het bos', 'in het park', 'in de tuin', 'in het veld']
# V-#666: VERH-02 #4/#5 dingen die rood of kapot kunnen zijn
RV5_DING = {'228f70eb': [('In het museum liggen 40 tanden', 'In de klas liggen 40 ballonnen'), ('rode tanden', 'rode ballonnen')],
            '19f864f1': [('In het nest zijn 240 tanden', 'In de winkel zijn 240 kopjes'), ('Hoeveel tanden', 'Hoeveel kopjes')],
            '5670f46b': [('60 vissen', '60 emmers'), ('Hoeveel vissen', 'Hoeveel emmers')],
            'bc3decfc': [('In de vallei zijn 300 blaadjes', 'In de kantine zijn 300 bekers'), ('Hoeveel blaadjes', 'Hoeveel bekers')],
            'ed5e3069': [('In de vallei zijn 160 eieren', 'In de winkel zijn 160 vazen'), ('Hoeveel eieren', 'Hoeveel vazen')]}
# V-#666 + Z-#666: VERH-02 #7 echte prijzen, geen 50% korting (korting = nieuwe prijs): (ding, prijs, procent)
RV5_KORTING = {'9f46abc6': ('jas', 60, 25), 'ba1753a9': ('jas', 70, 30), 'eaf0a004': ('puzzel', 20, 25)}
# V-#665 (Oef-#447): VBN-04 #2 één uniek hoogste getal: (index in de tabel, nieuwe waarde)
RV5_STAAF = {'8816e526': (4, 35), '53fcafc4': (4, 20)}
def _rv5(it, slog):
    cid = it['bron'].get('claudeId') or ''; c8 = cid[:8]; o = it['opgave']; e = it['extraVelden']; doel = it.get('doelId') or ''
    if RV5_AAN == 'staaf' and c8 not in RV5_STAAF: return
    # V-#664: MEET-04 #3 bank-044, antwoord −3 = het voorbeeld in de vraagzin → 5 en 9, antwoord −4
    if c8 == 'ffa8a0a1':
        o = o.replace('daalt de temperatuur 8 graden', 'daalt de temperatuur 9 graden')
        _zet(it, slog, 'v664', 'V-#664: 5 − 8 → 5 − 9 (antwoord −3 was het voorbeeld in de vraag, review batch 5)', o, '−4',
             [('4', 'teken-vergeten', 'Je komt onder nul: het antwoord heeft een min ervoor.'), ('−5', 'een-ernaast', 'Van 5 naar 0 is 5 graden, dan nog 4.')],
             '5 − 9 graden', 'Van 5 naar 0 is 5 graden. Dan nog 4 graden verder onder nul: −4.')
        o = it['opgave']
    if 'graden' in o and RV5_BINNEN.search(o):
        b = RV5_BUITEN[int(_hashlib.md5(cid.encode()).hexdigest(), 16) % len(RV5_BUITEN)]
        n = RV5_BINNEN.sub(b, o)
        if 'v664' in it['merge']: it['opgave'] = n; it['merge']['v664']['reden'] += f'; V-#666: {RV5_BINNEN.search(o).group(0)} → {b}'
        else: _zet(it, slog, 'v666', f'V-#666: vorst binnen ({RV5_BINNEN.search(o).group(0)}) → {b} (review batch 5)', n)
    if c8 in RV5_DING:
        _zet(it, slog, 'v666', 'V-#666: ' + ', '.join(f'{a} → {b}' for a, b in RV5_DING[c8][:1]) + ' (review batch 5)', _vervang(it, RV5_DING[c8]))
    if c8 in RV5_KORTING:
        d, p, k = RV5_KORTING[c8]; kort = p * k // 100; a = p - kort
        assert p * k % 100 == 0 and kort != a
        denk = [(f'€{kort}', 'verkeerde-bewerking', f'{kort} is de korting. De vraag is wat je nog betaalt.')]
        if p - k > 0: denk.append((f'€{p - k}', 'procent-verkeerde-basis', f'{k}% is niet {k} euro. Reken eerst uit hoeveel {k}% van {p} is.'))
        denk.append((f'€{p + kort}', 'verkeerde-bewerking', 'Korting gaat eraf, niet erbij.'))
        _zet(it, slog, 'v666', f'V-#666/Z-#666: {o.split(".")[0]} met {re.search(r"(\d+)% korting", o).group(1)}% → een {d} van €{p} met {k}% (review batch 5)',
             f"Een {d} kost €{p}. Er is {k}% korting. Wat is de nieuwe prijs in euro's?", f'€{a}', denk, f'€{p} met {k}% korting',
             f'Korting: {k}% van {p} = {kort}.\nNieuwe prijs: {p} − {kort} = €{a}.')
        o = it['opgave']
    # Oef-#448: VERH-02 #7 'Wat is de nieuwe prijs in euro's?': het antwoord met €, zoals de sleutels ('56' → '€56')
    if re.fullmatch(r"Een \w+ kost €\d+\. Er is \d+% korting\. Wat is de nieuwe prijs in euro's\?", it['opgave']) and re.fullmatch(r'\d+', str(it['antwoord'])):
        oud = it['antwoord']; it['antwoord'] = f'€{oud}'
        if isinstance(it.get('antwoordDetail'), dict) and 'accept' in it['antwoordDetail']: it['antwoordDetail']['accept'] = [it['antwoord']]
        it['merge']['oef448'] = {'antwoord': oud, 'reden': "Oef-#448: antwoord met € zoals de sleutels"}
        slog(it, "G7-oef448: Oef-#448 antwoord met €", 'antwoord', oud, it['antwoord'])
    # V-#665 (Oef-#447): gelijke hoogste staaf → één uniek hoogste getal
    if c8 in RV5_STAAF:
        ix, w = RV5_STAAF[c8]; jr = it['visual']['jsRender']; rij = list(jr['rijen'][0]['waarden']); naam = jr['kolommen'][ix + 1]; oudw = rij[ix]
        rij[ix] = w; assert rij.count(max(rij)) == 1 and rij.index(max(rij)) != ix
        _vervang(it, [(f'{naam} heeft {oudw}.', f'{naam} heeft {w}.')])
        _zet(it, slog, 'v665', f'V-#665: {naam} {oudw} → {w} (één hoogste staaf, review batch 5)', it['opgave'],
             kale='hoogste van ' + ', '.join(map(str, rij)), jr={'rijen': [dict(jr['rijen'][0], waarden=rij)]})
    # V-#667 (Oef-#449): balk kleuren, het aantal stukjes in jsRender (VERH-01 #2: 20, VERH-01 #1: 10, VBN-04 #1: 10)
    if it.get('ui') == 'balk kleuren':
        n = 20 if re.fullmatch(r'Kleur \d+% van de balk\.', it['opgave']) else 10
        if it['opgave'].startswith('Tabel:'):
            st = int(re.search(r'stukje van de balk is (\d+)', it['opgave']).group(1))
            assert max(map(int, re.findall(r'\b[a-z]{2,4} (\d+)', it['opgave']))) <= n * st, it['id']
        it['visual']['jsRender'] = {'soort': 'balk', 'delen': n, 'kleurbaar': True}      # zelfde vorm als G5 (regels_g5: balk kleuren)
        it['merge']['v667'] = {'reden': f'V-#667: balk van {n} stukjes in jsRender'}
    # Oef-#450: VBN-04 #1 bank-010/011, Claudes sleutel '10' zonder route → weg (de motorroutes '± 1' en 'getal uit de vraag' blijven)
    if c8 in ('d6bcfbf3', 'ee214c17'):
        denk = [(d['fout'], d['denkfout'], next((h['uitleg'] for h in e.get('claudeFoutHints') or [] if h['fout'] == d['fout']), None))
                for d in e.get('claudeDenkfouten') or [] if d['fout'] != '10']
        _zet(it, slog, 'oef450', "Oef-#450: sleutel '10' zonder route weg", it['opgave'], denk=denk)
_pas_toe_z668 = pas_toe
def pas_toe(it, slog):
    _pas_toe_z668(it, slog)
    if RV5_AAN: _rv5(it, slog)
RV5_AAN = True      # 'staaf' = alleen V-#665 (zo gebouwd om 14:07:01) voor de build van Oefeningen' rondes (14:05); daarna weer aan

# ---------- Oef-#451 + Z-#665 + Z-#666 (#6): toevallige treffers in VERH-02 #1/#3/#6 (review batch 5) ----------
# #1 'Hoeveel is p% van g?': geen route (het procent, het hele getal, getal min procent, som) geeft het antwoord; 'x% van 100' (antwoord = het
#   procent, Z-#665) krijgt een ander geheel. Het procent blijft; het geheel wordt het eerste veelvoud van tien uit V451_G dat past en nog niet bestaat.
# #3 'Hoeveel procent is d van g?': zelfde antwoord, andere getallen zonder treffer (geheel min deel, som). #6: bij 10% is omgekeerd delen (g : d)
#   altijd tien → ander procent. Claudes sleutels worden per label opnieuw uitgerekend; opties (#3) ook.
# Het nieuwe geheel (vast, uitgezocht op build 14:12:17): veelvoud van tien, ≠ het procent, geen treffer, nog niet als 'p% van g' in G7.
V451_1 = {'0ce65488': 290, '24782b7c': 70, '37bb170d': 450, '55705678': 450, '949909a8': 450, 'aa4ab169': 70, 'd344eab0': 460, 'e9aa4f72': 460, 'fa1da4e1': 70}
V451_3 = {'76caf17f': (7, 35), 'ae3eaf5c': (4, 16), 'fc3c63ae': (30, 50)}
V451_6 = {'9cf999e3': (300, 60), 'bb88d650': (20, 3)}
def _kg(x):
    """Fraction → huisvorm met komma ('2', '1,5', '0,25'); alleen eindige decimalen."""
    x = _Fr(x)
    if x.denominator == 1: return str(x.numerator)
    t = f'{float(x):.6f}'.rstrip('0').rstrip('.'); assert _Fr(t) == x, x
    return t.replace('.', ',')
def _v451(it, slog):
    cid = it['bron'].get('claudeId') or ''; c8 = cid[:8]; o = it['opgave']; e = it['extraVelden']
    if it.get('doelId') != 'G7-VERH-02' and not (it.get('merge') or {}).get('doel') == 'G7-VERH-02': return
    uitleg = {d['denkfout']: h.get('uitleg') for d in e.get('claudeDenkfouten') or [] for h in e.get('claudeFoutHints') or [] if h.get('fout') == d.get('fout')}
    if c8 in V451_1:
        p, g0 = map(int, re.fullmatch(r'Hoeveel is (\d+)% van (\d+)\?', o).groups()); a0 = p * g0 // 100
        g = V451_1[c8]; a = p * g // 100
        assert p * g % 100 == 0 and a not in (p, g, g - p, g + p) and g != p
        denk = []
        for d in e.get('claudeDenkfouten') or []:
            dk = d['denkfout']; oud = _Fr(d['fout'].replace(',', '.')) if re.fullmatch(r'\d+(?:,\d+)?', d['fout']) else None
            if dk == 'getal-overgenomen': denk.append((str(g), dk, uitleg.get(dk)))
            elif dk == 'nul-fout-tientallen' and oud is not None:      # ': 10' alleen als het een heel getal blijft (anders '× 10')
                v = _Fr(a * 10) if oud > a0 or a % 10 else _Fr(a, 10)
                if _kg(v) not in [x[0] for x in denk]: denk.append((_kg(v), dk, uitleg.get(dk)))
        _zet(it, slog, 'oef451', f'Oef-#451/Z-#665: {p}% van {g0} → {p}% van {g} (toevallige treffer, review batch 5)', f'Hoeveel is {p}% van {g}?', str(a), denk,
             f'{p}% van {g}', f'10% van {g} is {_kg(_Fr(g, 10))}.\n{p}% is {_kg(_Fr(p, 10))} × {_kg(_Fr(g, 10))} = {a}.')
    elif c8 in V451_3:
        d, g = V451_3[c8]; a = 100 * d // g; a0 = int(str(it['antwoord']).rstrip('%'))
        assert 100 * d % g == 0 and a == a0 and a not in (d, g - d, d + g, 100 - a)
        waarde = {'getal-overgenomen': _Fr(d), 'andere-deel-genomen': _Fr(100 - a), 'verhoudingstabel-verkeerd': _Fr(g - d)}
        denk = []
        for k in e.get('claudeDenkfouten') or []:
            dk = k['denkfout']; oud = _Fr(k['fout'].rstrip('%').replace(',', '.'))
            v = waarde.get(dk) if dk != 'nul-fout-tientallen' else (_Fr(a * 10) if oud > a0 else _Fr(a, 10))
            if v is not None: denk.append((f'{_kg(v)}%', dk, uitleg.get(dk)))
        opgave = f'Hoeveel procent is {d} van {g}?'; opties = [x[0] for x in denk]
        opties.insert(int(_hashlib.md5(cid.encode()).hexdigest(), 16) % (len(opties) + 1), f'{a}%')
        _opties(it, slog, 'oef451', f'Oef-#451: {o} → {opgave} (toevallige treffer, review batch 5)', opgave, opties, f'{a}%', denk,
                f'Het geheel {g} is 100%.\n{d} van {g} is {d} : {g} = {a} van de 100, dus {a}%.')
    elif c8 in V451_6:
        g, d = V451_6[c8]; a = _Fr(100 * d, g); assert a.denominator == 1 and _Fr(g, d) != a and d != a and g - d != a; a = int(a)
        ding = re.search(r'een (\w+)\. Hoeveel procent', o).group(1); wie = re.search(r'Van de \d+ (\S+)', o).group(1)
        denk = [(str(d), 'procent-verkeerde-basis', f'{d} is het aantal, niet het percentage. Zet het om naar per 100.'),
                (str(g - d), 'verkeerde-bewerking', 'Dat is het aantal zonder. Zet om naar per 100.')]
        f = _Fr(100, g)
        _zet(it, slog, 'z666', f'Z-#666: {d} van {g} (omgekeerd delen gaf ook het antwoord, review batch 5)',
             f'Van de {g} {wie} hebben er {d} een {ding}. Hoeveel procent is dat?', str(a), denk, f'{d} van de {g} = ? %',
             f'Maak er 100 van: {g} → 100 is keer {_kg(f)}.\n{d} × {_kg(f)} = {a}. Dus {a}%.' if f.denominator == 1 else f'Maak er 100 van: {g} → 100 is : {_kg(1 / f)}.\n{d} : {_kg(1 / f)} = {a}. Dus {a}%.')
_pas_toe_rv5 = pas_toe
def pas_toe(it, slog):
    _pas_toe_rv5(it, slog); _v451(it, slog)

# ---------- Z-#667 (review batch 5): vuistregels in eenzijdige data ----------
# VBN-04 #3 'Tot welk getal moet de as minstens lopen?': opties waren altijd antwoord − 10 / antwoord / antwoord + 10 (de middelste is goed).
#   Nu bij 2 items antwoord / + 10 / + 20 (goed = de kleinste) en bij 2 items − 20 / − 10 / antwoord (goed = de grootste); 4 blijven zo.
#   '± 20' heeft nog geen eigen regel in de entry (valt op 'andere fout'; voorstel aan Oefeningen: 'twee tientallen te hoog/te laag').
Z667_AS = {'1d984894': (10, 20), 'c52c0729': (10, 20), '2191ae42': (-20, -10), '82ed1ecf': (-20, -10)}
# VERH-01 #1 'Een pot heeft N [ding]. Kleur p% ervan. Elk stukje is M [ding].': altijd tien stukjes (antwoord = procent : 10). Nu bij 5 van de
#   12 items een ander stukje: 5% (twintig stukjes), 20% (vijf) of 25% (vier); jsRender 'delen' = N : M.
Z667_POT = {'720d77a4': (70, 10), '8a1b2ca5': (40, 60), 'a8e37577': (20, 25), 'f3561f23': (60, 40), 'ea724bfc': (75, 100)}
def _z667(it, slog):
    cid = it['bron'].get('claudeId') or ''; c8 = cid[:8]; o = it['opgave']
    if c8 in Z667_AS:
        a = int(it['antwoord']); d1, d2 = Z667_AS[c8]
        t = {d: ('Deze as is langer dan nodig. Welk tiental zit het dichtst boven het grootste getal?' if d > 0 else
                 'Kijk naar het grootste getal in de tabel: past die staaf nog op deze as?') for d in (d1, d2)}
        denk = [(str(a + d), 'grafiek-verkeerd-afgelezen', t[d]) for d in (d1, d2)]
        mx = max(it['visual']['jsRender']['rijen'][0]['waarden']); assert all(a + d > 0 and (d > 0 or a + d < mx) for d in (d1, d2))
        opties = sorted([str(a)] + [x[0] for x in denk], key=int)
        _opties(it, slog, 'z667', f"Z-#667: opties {'antwoord, +10, +20' if d1 > 0 else '−20, −10, antwoord'} (niet altijd de middelste, review batch 5)", o, opties, str(a), denk)
    m = re.fullmatch(r'Een pot heeft (\d+) (\w+)\. Kleur (\d+)% ervan\. Elk stukje is (\d+) \w+\.', o)
    if m and c8 in Z667_POT:
        n, ding = int(m.group(1)), m.group(2); p, st = Z667_POT[c8]; v = n * p // 100; a = v // st
        assert n * p % 100 == 0 and v % st == 0 and n % st == 0 and a != p // 10
        _zet(it, slog, 'z667', f'Z-#667: {p}% van {n}, stukje {st} ({n // st} stukjes; antwoord niet procent : 10, review batch 5)',
             f'Een pot heeft {n} {ding}. Kleur {p}% ervan. Elk stukje is {st} {ding}.', str(a), [], f'{p}% van {n}',
             f'{p}% van {n} is {v}. Elk stukje is {st}, dus {v} : {st} = {a} stukjes.')
    if m and it.get('ui') == 'balk kleuren':      # V-#667 met Z-#667: het aantal stukjes is N : M (ook bij de items die blijven: tien)
        m2 = re.fullmatch(r'Een pot heeft (\d+) \w+\. Kleur \d+% ervan\. Elk stukje is (\d+) \w+\.', it['opgave'])
        it['visual']['jsRender'] = {'soort': 'balk', 'delen': int(m2.group(1)) // int(m2.group(2)), 'kleurbaar': True}
_pas_toe_v451 = pas_toe
def pas_toe(it, slog):
    _pas_toe_v451(it, slog); _z667(it, slog)

# ---------- Z-#664 (review batch 5, deel Overzicht): VERH-01 #4 (nrO 4) opties «… keer zo klein» ----------
# Didactiek: «keer zo klein» kan beter «keer kleiner» of «Het echte voorwerp is … keer zo groot». Gekozen: de tweede vorm, en alle drie de opties
# met hetzelfde begin (anders valt het goede antwoord op door zijn andere zinsbouw). Alleen bank-002 (752cd1e4) heeft deze opties; #5 niet.
# De literal-regels in de entry gaan mee (patch_batch5, blok Z-#664); hun teksten blijven.
Z664 = {'De tekening is 100 keer zo klein': 'Het echte voorwerp is 100 keer zo groot',
        'De tekening is 2 keer zo klein': 'Het echte voorwerp is 2 keer zo groot',
        'De tekening is net zo groot als het echte voorwerp': 'Het echte voorwerp is net zo groot als de tekening'}
def _z664(it, slog):
    if not (it['bron'].get('claudeId') or '').startswith('752cd1e4'): return
    e = it['extraVelden']; u = {h['fout']: h.get('uitleg') for h in e.get('claudeFoutHints') or []}
    denk = [(Z664.get(d['fout'], d['fout']), d.get('denkfout'), u.get(d['fout'])) for d in e.get('claudeDenkfouten') or []]
    opties = [Z664.get(o['tekst'], o['tekst']) for o in it['opties']]
    _opties(it, slog, 'z664', "Z-#664: opties «keer zo klein» → «Het echte voorwerp is … keer zo groot» (review batch 5)", it['opgave'], opties,
            Z664.get(it['antwoord'], it['antwoord']), denk)
_pas_toe_z667 = pas_toe
def pas_toe(it, slog):
    _pas_toe_z667(it, slog); _z664(it, slog)

# ---------- Oef-#452: VERH-03, Claudes sleutels die niet in claudeFoutHints staan ----------
# Oorzaak (geen kapotte koppeling): de G4-regel D12b (regels_g4, ONGEPAST_G4) laat Claude-fout-hints met de sjabloontekst «Maak een
# verhoudingstabel. …» altijd vallen, en «Dat getal staat al in de som. …» als de vraag geen rekenteken heeft. Met de tekst verdween ook de
# sleutel uit claudeFoutHints (de basis van apply_hints), terwijl claudeDenkfouten hem houdt. In VERH-03 (verhoudingen) is dat juist de goede
# route. Herstel voor G7-VERH-03: de ontbrekende sleutels terug in claudeFoutHints, zonder Claudes sjabloontekst (uitleg None): de labelregels
# en motorregels van de entry pakken ze; zonder passende regel vallen ze op 'andere fout' (Oefeningen kan dan regels maken).
def _v452(it, slog):
    if it.get('doelId') not in ('G7-VERH-03', 'G7-VERH-04'): return   # Oef-#453: VERH-04 heeft dezelfde oorzaak ('32%', '0,7%')
    e = it['extraVelden']; n = lambda x: re.sub(r'^\s*[-–]', '−', str(x or ''))
    ks = {n(h.get('fout')) for h in e.get('claudeFoutHints') or []}
    terug = [d['fout'] for d in e.get('claudeDenkfouten') or [] if n(d.get('fout')) not in ks and d.get('fout') != it['antwoord']]
    if not terug: return
    e['claudeFoutHints'] = (e.get('claudeFoutHints') or []) + [{'stap': None, 'fout': k, 'uitleg': None} for k in dict.fromkeys(terug)]
    it['merge']['oef452'] = {'terug': terug, 'reden': "Oef-#452: sleutel(s) terug in claudeFoutHints (vielen weg met de G4-sjabloontekst, D12b)"}
_pas_toe_z664 = pas_toe
def pas_toe(it, slog):
    _pas_toe_z664(it, slog); _v452(it, slog)
