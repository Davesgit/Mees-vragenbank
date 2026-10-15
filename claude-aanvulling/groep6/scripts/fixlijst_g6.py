#!/usr/bin/env python3
"""G6 merge-fixlijst (Oefeningen 19:56, #1–#7; besluiten Dave 19:58), uitgevoerd door Overzicht om 20:05.
Twee soorten aanpassingen:
  pas_entries_aan(somtypen)  hint-entries (in het geheugen, bij apply_hints; hints/batch1.json van Oefeningen blijft zoals hij is). Idempotent:
                             staat de regel al in de entry (omdat Oefeningen hem in patch_batch1 heeft overgenomen), dan gebeurt er niets.
     #1  E01 #1 (duizendtallen) en #4 (tienduizendtallen): 'het andere duizendtal/tienduizendtal naast getal1' (verkeerde kant) en 'getal1 afgerond
         op honderdtallen/duizendtallen' komen vóór 'antwoord ± 1000/± 10000'. Die regels krijgen nu de tekst 'één stap te ver' (zoals E01 #2, #5, #7).
     #4  M03 #1 (Zet 1,4 op de lijn): kommagetalregels van de motor, vóór 'een getal uit de vraag'.
     #6  M02 #2/#3: de Claudes-sleutelregels 'één erbij/eraf gedaan' → 'fout = getal2 + 1' (meer dan) en 'fout = getal2 − 1' (minder dan).
  bewerk(it)                 per item in build_g6 (vóór de hercontrole):
     #2  GET-M02 #5 item 212: 8787 (twee zevens) → 8785; assert: in elk item 'Hoeveel is de D in dit getal waard?' staat D precies één keer.
     #3  GET-M03 #2: Claude-sleutels die bij geen denkfout passen weg (002 '0,31'; 008 '0,11' en '1,00'); #150: 008 krijgt '10' (omgekeerd gedeeld,
         10 : 1); #151: Claude-kommasleutels in de vorm van de VORM-regel (#105): '0,10' → '0,1', '2,00' → '2'.
     #7  GET-M03 #1: visual.getallenlijn {van, tot, streepjePer, bron}. 0–2: 'Elk streepje is een tiende' (claudeUitleg). 0–10: niet in de data → app-eis.
Ronde 2 (Didactiek review-batch1 v1, 20:15; besluiten Dave 20:16):
     #152 E01 'Rond … af op …': geen middengetal (2500, 1050, 65.000) zolang de tekst 'niet afgerond' vraagt naar 'het dichtst bij'. De 26 items
          krijgen een getal dat geen midden is (zelfde id, zelfde plek), met een nul binnenin; E01 #2 komt boven 1017–1989 en E01 #1 (5 cijfers) en #4
          gaan naar 6 cijfers (#156e). Claudes sleutels gaan mee (het getal zelf, het andere buurgetal, antwoord ± stappen). Assert.
     #156d (besluit Dave 20:38): middengetal hangt af van de vraag. 'het dichtst bij' → geen middengetal; 'Rond … af op …' → 1 à 2 middengetallen
          en Hint 2 noemt '5 of meer → erboven'. Alle E01-afrond-somtypen vragen 'Rond … af op …': 5 van de 26 houden hun oude getal (TERUG156:
          #1 7500 en 10.500, #2 1050 en 1550, #4 65.000); #5/#7/#8 krijgen elk één middengetal (MIDDEN156: 2477→2450, 2265→2500, 4029→4025).
     #153 M03 #1: veld 'beoordeling' met banden (goed |x − a| < 0,05; één tiende ernaast 0,05 ≤ |x − a| < 0,15 met richting; sleutel |x − s| < 0,05);
          visual.getallenlijn.streepjesPerTiende = true (ook 0–10); de motor zet geen sleutel buiten [van, tot] (fout_regels). App-eis in README.
          De ± 0,1-teksten (onze eigen invoeging van #4) krijgen de tekst van Didactiek (V2).
     #154 M02 #2/#3: regels 'fout = getal2 ± getal1 × 10 / : 10 / × 100' (op de verkeerde plek), vóór 'andere fout'.
     #156 asserts M02 #1/#4/#5; M03 #1 item 024 'Zet 8' → 'Zet 8,6'; M02 #4/#5 opgaven zonder 'staat 8785 botten' (bewerk_na, na het somtype).
Log: logs/fixlijst_g6.json (schrijf_log)."""
import collections
import re, json, os
from fractions import Fraction
LOG = []
def _log(**k): LOG.append(k)

# ------------------------------------------------------------------ hint-entries
def _f(regel, soort, tekst): return {'regel': regel, 'soort': soort, 'tekst': tekst, 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst, besluit Dave 19:58)'}
AFR = {1: ('duizendtal', 'duizendtallen', 'honderdtallen', 'honderdtallen', 1000),
       4: ('tienduizendtal', 'tienduizendtallen', 'duizendtallen', 'duizendtallen', 10000)}
def _afronden(st, nr):
    eh, ehn, kleiner, cijfer, stap = AFR[nr]
    fh = st['foutHints']; regels = [f['regel'] for f in fh]
    if any(r.startswith(f'fout = het andere {eh} naast getal1') for r in regels): return
    i = next(k for k, f in enumerate(fh) if f['regel'] in (f'fout = antwoord + {stap}', f'fout = antwoord − {stap}'))
    nieuw = [_f(f'fout = het andere {eh} naast getal1', 'verkeerde kant',
                f'Dat is het {eh} aan de andere kant van het getal. Kijk naar het cijfer van de {cijfer if nr == 4 else "honderdtallen"}. '
                f'Is het vijf of meer, dan ga je naar het {eh} vlak erboven. Anders naar het {eh} vlak eronder.'),
             _f(f'fout = getal1 afgerond op {kleiner}', f'afgerond op {kleiner}',
                f'Je hebt afgerond op {kleiner}. Hier rond je af op {ehn}. Kijk naar het cijfer van de {cijfer}.')]   # S3 (Didactiek 20:15): geen 'het dichtst bij'
    fh[i:i] = nieuw
    for f in fh:
        if f['regel'] in (f'fout = antwoord + {stap}', f'fout = antwoord − {stap}'):
            oud = (f['soort'], f['tekst'])
            f['soort'] = 'één stap te ver (omhoog)' if '+' in f['regel'] else 'één stap te ver (omlaag)'
            f['tekst'] = f'Je gaat de goede kant op, maar één {eh} te ver. Kies het {eh} dat vlak naast het getal ligt.'
            f['door'] = 'Overzicht (G6-fixlijst #1): tekst zoals E01 #2/#5/#7'
            _log(punt=1, entry=f"{st['doel']} #{st['nr']}", regel=f['regel'], oud=oud, nieuw=(f['soort'], f['tekst']))
    _log(punt=1, entry=f"{st['doel']} #{st['nr']}", ingevoegd=[x['regel'] for x in nieuw], voor=f'antwoord ± {stap}')
def _m02(st, plus):
    fh = st['foutHints']; regel = 'fout = getal2 + 1' if plus else 'fout = getal2 − 1'
    if any(f['regel'] == regel for f in fh): return
    oud = [k for k, f in enumerate(fh) if f['regel'] in ('Claudes sleutel: eenheid-verkeerd-omgerekend', 'Claudes sleutel: plaatswaarde-verkeerd')]
    assert len(oud) == 2, (st['doel'], st['nr'], [f['regel'] for f in fh])
    eerste = fh[oud[0]]
    nieuw = _f(regel, eerste['soort'], eerste['tekst'])
    for k in reversed(oud): del fh[k]
    fh.insert(oud[0], nieuw)
    _log(punt=6, entry=f"{st['doel']} #{st['nr']}", weg=['Claudes sleutel: eenheid-verkeerd-omgerekend', 'Claudes sleutel: plaatswaarde-verkeerd'], nieuw=regel, soort=nieuw['soort'])
def _m03_1(st):
    fh = st['foutHints']
    if any(f['regel'].startswith('fout = het hele getal van het kommagetal') for f in fh): return
    i = next(k for k, f in enumerate(fh) if f['regel'].startswith('fout = een getal uit de vraag'))
    nieuw = [
        _f('fout = het hele getal van het kommagetal', 'alleen het hele getal',
           'Dat is alleen het hele getal. Het cijfer achter de komma zegt hoeveel tienden je nog verder gaat.'),
        _f('fout = de tienden als heel getal', 'cijfer achter de komma als heel getal',
           'Dat is het cijfer achter de komma, als heel getal. Zoek eerst het hele getal op de lijn: het cijfer vóór de komma. Ga dan zoveel tienden verder.'),
        _f('fout = de cijfers om de komma omgedraaid', 'cijfers omgedraaid',
           'Je hebt de cijfers omgedraaid. Het cijfer vóór de komma is het hele getal. Het cijfer achter de komma zegt hoeveel tienden je verder gaat.'),
        _f('fout = antwoord + 0,1', 'één tiende te ver', 'Bijna! Je bent één tiende te ver. Zet je stip een klein stukje terug. Tussen twee hele getallen zitten tien tienden.'),   # #153a (V2)
        _f('fout = antwoord − 0,1', 'één tiende te kort', 'Bijna! Je bent één tiende te kort. Zet je stip een klein stukje verder. Tussen twee hele getallen zitten tien tienden.')]   # #153a (V2)
    fh[i:i] = nieuw
    _log(punt=4, entry=f"{st['doel']} #{st['nr']}", ingevoegd=[x['regel'] for x in nieuw], voor='fout = een getal uit de vraag')
PLEK154 = {True: ('Je hebt er wel iets bijgedaan, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek komt er één bij?', '+'),
           False: ('Je hebt er wel iets afgehaald, maar op de verkeerde plek. Kijk naar het getal vooraan in de vraag. Bij welke plek gaat er één af?', '−')}
def _m02_154(st, plus):
    fh = st['foutHints']; tekst, t = PLEK154[plus]
    regels = [f'fout = getal2 {t} getal1 × 10', f'fout = getal2 {t} getal1 : 10', f'fout = getal2 {t} getal1 × 100']
    if any(f['regel'] in regels for f in fh): return
    i = next(k for k, f in enumerate(fh) if f['regel'] == 'andere fout')
    fh[i:i] = [_f(r, 'op de verkeerde plek', tekst) for r in regels]
    _log(punt=154, entry=f"{st['doel']} #{st['nr']}", ingevoegd=regels, voor='andere fout')
def pas_entries_aan(somtypen):
    for st in somtypen:
        k = (st['doel'], st.get('nrOrigineel'))
        if k in (('G6-GET-E01', 1), ('G6-GET-E01', 4)): _afronden(st, k[1])
        elif k == ('G6-GET-M02', 2): _m02(st, True); _m02_154(st, True)
        elif k == ('G6-GET-M02', 3): _m02(st, False); _m02_154(st, False)
        elif k == ('G6-GET-M03', 1): _m03_1(st)
        elif k == ('G6-GET-M05', 3): _m05_163(st); _m05_193(st)
        elif k == ('G6-GET-E03', 7): _e203(st)
        elif k == ('G6-GET-E03', 4): _e202(st)
        elif k == ('G6-GET-M04', 3): _e173(st)
        elif k in (('G6-GET-E06', 3), ('G6-GET-E06', 7)): _e198(st)
        elif k in (('G6-MEET-E03', 1), ('G6-MEET-E03', 3), ('G6-MEET-E03', 4)): _e176(st)
        elif k in (('G6-GET-E03', 1), ('G6-GET-E03', 5), ('G6-GET-E03', 8)): _e170(st)
        elif k == ('G6-GET-E06', 1): _e190(st)
        _e167(st); _e174(st)
        pas_entries_ronde7(st)                 # ronde 7 (Didactiek 2c/batch 4/3b, 22:13–22:14)
        pas_entries_ronde8(st)                 # ronde 8 (#219, #263)
        # _e192 (#192/#197) is weg: Oefeningen heeft de ouderzin in batch 2 zelf aangepast; de check (EVENVEEL, FIX6) blijft
    assert_tekst263(somtypen)              # #263: nergens een regel zonder tekst
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json.dump([x for x in LOG if x['punt'] in (1, 4, 6, 154) or (x['punt'] in (163, 167, 169, 170, 173, 174, 176, 186, 190, 192, 193, 198, 202, 203, 205, 206, 207, 209, 214, 215, 216, 219, 263) and 'entry' in x)], open(f'{base}/logs/fixlijst_g6_hints.json', 'w'), ensure_ascii=False, indent=1)
    return somtypen

# ------------------------------------------------------------------ items
ID212 = '7a24d769-98c6-4394-8d6d-1d67752fd3db'
M03_2 = {'1a6884df-0a21-4f42-af08-8fa4386ce023': ['0,31'], 'dc16980d-7396-4919-ac80-ee6449c4d603': ['0,11', '1,00']}
EXTRA_150 = {'dc16980d-7396-4919-ac80-ee6449c4d603': ('10', 'omgekeerd-gedeeld', 'Teller gedeeld door noemer, niet andersom.')}
WAARD = re.compile(r'staat (?:het getal )?(\d[\d.]*)[^.]*\. Hoeveel is de (\d) in dit getal waard\?')
def _vervang(o, a, b):
    if isinstance(o, str): return o.replace(a, b)
    if isinstance(o, list): return [_vervang(x, a, b) for x in o]
    if isinstance(o, dict): return {k: _vervang(v, a, b) for k, v in o.items()}
    return o
def _kg(t):
    m = re.fullmatch(r'(\d+),(\d+)', t)
    if not m: return t
    na = m.group(2).rstrip('0'); return f'{m.group(1)},{na}' if na else m.group(1)
def bewerk(it):
    cid = it['bron']['claudeId']; ex = it['extraVelden']
    # #2
    if cid == ID212 and '8787' in it['opgave']:
        oud = it['opgave']
        for k in ('opgave', 'opgaveStappen', 'antwoordDetail', 'extraVelden', 'kopExtra'):
            if k in it: it[k] = _vervang(it[k], '8787', '8785')
        _log(punt=2, id=it.get('id'), claudeId=cid, oud=oud, nieuw=it['opgave'], antwoord=it['antwoord'])
    if (m := WAARD.search(it['opgave'])):
        n = m.group(1).replace('.', '')
        assert n.count(m.group(2)) == 1, f"#2: in '{it['opgave']}' staat de {m.group(2)} {n.count(m.group(2))} keer"
    # #3 / #150 / #151
    if cid in M03_2:
        weg = set(M03_2[cid]); oud = [f['fout'] for f in ex.get('claudeFoutHints') or []]
        ex['claudeFoutHints'] = [f for f in ex.get('claudeFoutHints') or [] if f['fout'] not in weg]
        ex['claudeDenkfouten'] = [d for d in ex.get('claudeDenkfouten') or [] if d['fout'] not in weg]
        _log(punt=3, claudeId=cid, weg=sorted(weg), reden='past bij geen denkfout: teller achter de komma = het antwoord; omgekeerd gedeeld bij 1/10 = 10, niet 1,00')
        if cid in EXTRA_150:
            f_, dk, u = EXTRA_150[cid]
            ex['claudeFoutHints'].append({'stap': None, 'fout': f_, 'uitleg': u}); ex['claudeDenkfouten'].append({'fout': f_, 'denkfout': dk})
            _log(punt=150, claudeId=cid, erbij=f_, denkfout=dk, reden='omgekeerd gedeeld: 10 : 1 = 10 (Claude had 1,00); anders geen fout-hint')
    if it['merge']['doel'] == 'G6-GET-M03' and re.match(r'Een \S+ is \d+/\d+ meter lang\. Schrijf dat als kommagetal\.', it['opgave']):
        for lst in (ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or []):
            for f in lst:
                if _kg(f['fout']) != f['fout']: _log(punt=151, claudeId=cid, oud=f['fout'], nieuw=_kg(f['fout'])) if lst is ex.get('claudeFoutHints') else None; f['fout'] = _kg(f['fout'])
        fr = re.search(r'(\d+)/(\d+) meter', it['opgave']); t, n = int(fr.group(1)), int(fr.group(2))
        for f in ex.get('claudeDenkfouten') or []:
            v = Fraction(f['fout'].replace(',', '.'))
            assert v != Fraction(t, n), f"#3: sleutel {f['fout']} = het antwoord ({it['opgave']})"
            if f['denkfout'] == 'omgekeerd-gedeeld': assert abs(v - Fraction(n, t)) < Fraction(1, 100), f"#3: {f['fout']} is geen {n} : {t}"
            if f['denkfout'] == 'kommagetal-als-geheel': assert v == Fraction(f'0.{t}'), f"#3: {f['fout']} is geen 0,{t}"
    # #7
    if it['merge']['doel'] == 'G6-GET-M03' and (m := re.match(r'Zet (\d+(?:,\d)?) op de lijn van (\d+) tot (\d+)\.', it['opgave'])):
        van, tot = int(m.group(2)), int(m.group(3))
        tiende = 'streepje is een tiende' in (ex.get('claudeUitleg') or '')
        it['visual']['getallenlijn'] = {'van': van, 'tot': tot, 'streepjePer': '0,1' if tiende else None,
                                        'bron': "claudeUitleg: 'Elk streepje is een tiende'" if tiende else 'niet in de data (G6-fixlijst #7): app-eis, zie README'}
    fix152(it); fix153(it); asserts156(it)
    fix192(it)                                                   # #192 vóór het somtype: de kop wordt 'evenveel'
    fix162(it); fix163(it); fix165(it); fix166(it); fix167(it)      # ronde 3 (Oefeningen batch 2, Dave 21:07)
    fix194a(it); fix194b(it); fix190(it); fix195(it)              # Didactiek batch 2 (21:25)
    fix169(it); fix170(it); fix171(it); fix174(it)                # ronde 4 (Oefeningen batch 3, Dave 21:24)
    fix173(it); fix183(it); fix185(it); fix186(it); fix189(it); fix180(it)   # ronde 5 (Didactiek batch 3, 21:42)
    fix196(it); fix198(it); fix178(it)                            # ronde 5 (recheck 2b 21:42; Oefeningen batch 4 21:43)
    fix211(it); fix218(it); fix224(it)                            # ronde 7 (Didactiek batch 4 / 3b, 22:13–22:14)
    grens158(it)

# ------------------------------------------------------------------ ronde 2 (Didactiek 20:15, Dave 20:16)
import hashlib
def _h(x): return int(hashlib.sha256(x.encode()).hexdigest()[:12], 16)
def _fmt(n): return str(n) if n < 10000 else f'{n:,}'.replace(',', '.')
def _rond(n, s): return (n + s // 2) // s * s
def _binnennul(n): t = str(n); return any(t[i] == '0' and t[i + 1:].strip('0') for i in range(1, len(t)))
_B1 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'hints', 'batch1.json')
# #152 (besluit Dave 20:16) en #156d (besluit Dave 20:38): middengetallen hangen af van de vraag in de kindtekst.
#   - vraagt het somtype 'het dichtst bij' → geen middengetal (een middengetal ligt even dicht bij beide);
#   - vraagt het somtype 'Rond … af op …' → minstens één middengetal, en Hint 2 noemt de regel '5 of meer → erboven'.
#   Alle E01-afrond-somtypen (#1, #2, #4, #5, #7, #8) vragen 'Rond … af op …' (hints/batch1.json, Oefeningen 20:27). Daarom:
#   TERUG156: 1 à 2 middengetallen per somtype blijven het oude getal van vóór #152 (zelfde id); de andere 21 van de 26 houden hun #152-getal.
#   MIDDEN156: #5, #7 en #8 hadden nooit een middengetal (geen oud #152-getal); één item per somtype wordt een middengetal (zelfde id).
def vraag_e01(opgave):
    """'dichtst bij' als de opgave naar het dichtstbijzijnde getal vraagt, anders 'rond af' ('Rond … af op …')."""
    return 'dichtst bij' if re.search(r'dichtst ?bij', opgave or '', re.I) else 'rond af'
TERUG156 = {'06ec06fb-3de1-4c58-b27c-2b5072ad4a8c': 7500, '97974870-aee2-4b82-821d-fcc89e1bae82': 10500,    # E01 #1
            '3b1efd35-5e2f-462a-8b86-69562749038b': 1050, '45daa967-10ac-4275-a2f4-d52397cb9def': 1550,      # E01 #2
            '634e0b1c-68a9-49e2-a6e2-4ed8eead631d': 65000}                                                   # E01 #4
MIDDEN156 = {'4afd93f4-1976-414e-9744-a31356a864a7': (2477, 2450),    # E01 #5 item 011 (antwoord blijft 2500)
             '8bee0469-76af-4336-8f09-d1a24183ab8f': (2265, 2500),    # E01 #7 item 006 (antwoord 2000 → 3000; geen item met honderdtal ≥ 5)
             '5b0bad0e-0e9e-4745-8b80-98e823851ba4': (4029, 4025)}    # E01 #8 item 014 (antwoord blijft 4030)
STAP = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000, 'tienduizendtallen': 10000}
AFROND = re.compile(r'(?:Rond (\d[\d.]*)|precies (\d[\d.]*) .+?\. Rond dit aantal) af op (tientallen|honderdtallen|duizendtallen|tienduizendtallen)\.')
GEBRUIKT152 = set()
GROOT158 = 100000      # #158 (Dave 20:49, Didactiek trekt #156e in): de grens van G6 = regels_g6.GROOT (getallen tot 100.000); build_g6 checkt dat ze gelijk zijn
def _bereik(n, s, k):
    """#156e (blijft): E01 #2 (honderdtallen) breder dan 1017–1989. #158: geen 6 cijfers meer; 5 cijfers blijven 5 cijfers (10.000–99.999)."""
    if s == 100: return (2000, 9999) if k % 2 else (10000, 99999)
    if s == 1000: return (10000, 99999) if n >= 10000 else (2000, 9999)
    return (10000, 99999)
# #159c (Dave 20:49): niet elk #152-getal met een nul binnenin; de helft (11 van de 21) wel, de andere helft een gewoon getal (geen nul binnenin).
# Vaste lijst van de 21 #152-items (na #156d); de keuze is vast (hash per claudeId), niet afhankelijk van de volgorde in de build.
VERVANG152 = ('0da6da97-8b6f-4bed-82d7-e96f62836d0b', '2f76f4e6-19d3-4ca2-9b46-865f084dd427', '33db6d12-d2ff-4658-8043-8ab6823509f4', '3c699c4e-a601-4f76-85c0-b056b2d5452c',
              '43b0a74b-6025-4d94-9ca7-a9ca2c1e4bec', '45d9004a-e593-48c6-b3d6-647eabcccab6', '50da078f-c3a2-4a05-ae3d-1eef162cf95c', '6113d9f5-453b-4291-89a1-5288056855fc',
              '66793f14-6c28-4434-ab3a-78ed22d4a6a0', '6d7817c5-902f-4b04-903d-0496ea166568', '769fc728-397e-4fb5-b921-6191cf089cd5', '7db7fd36-aed7-412e-a26d-ceb70221bf2e',
              '8e86bd30-3306-4def-b09e-c88e99ff1a72', '9e47f026-dd4c-4ef9-a82d-c7f0ef561eeb', '9edb0cfb-b0ef-40aa-bbf7-e7778e523b70', 'a3e674d0-750f-44ef-8f7d-477d3fe71d19',
              'a7acf16c-2fa9-4640-bd0a-8bca7b98dd62', 'a9584d60-5085-4b69-b3b2-cb4bc9a999e5', 'b3708e5b-9d75-416c-96d0-2b123c685776', 'f4261723-9c68-45c1-8346-60aaf134279b',
              'fcb0ee10-5fe8-4d4b-9e8e-3a51bd51b24e')
NUL152 = set(sorted(VERVANG152, key=lambda c: _h(f'{c}-159'))[:(len(VERVANG152) + 1) // 2])
def _nieuw152(cid, n, s):
    for k in range(1, 20000):
        x = _h(f'{cid}-152-{k}'); lo, hi = _bereik(n, s, x % 7)
        n2 = lo + (x >> 4) % (hi - lo + 1); r = _rond(n2, s); kl = s // 10
        if n2 % s == s // 2 or n2 % kl == 0 or r % (10 * s) == 0 or _rond(n2, kl) == r or n2 in GEBRUIKT152: continue
        if _binnennul(n2) != (cid in NUL152) or max(n2, r) > GROOT158: continue      # #159c: de helft met een nul binnenin · #158: tot 100.000
        return n2
    raise AssertionError(('#152 geen nieuw getal', cid))
def _sub_getal(o, oud, nieuw):
    if isinstance(o, str):
        for v in dict.fromkeys([_fmt(oud), str(oud)]): o = re.sub(rf'(?<![\d.,]){re.escape(v)}(?![\d]|[.,]\d)', _fmt(nieuw), o)
        return o
    if isinstance(o, list): return [_sub_getal(x, oud, nieuw) for x in o]
    if isinstance(o, dict): return {k: _sub_getal(v, oud, nieuw) for k, v in o.items()}
    return o
def _vervang152(it, n, n2, s):
    """Zet getal n in het item om naar n2 (opgave, antwoord, claudeKaleSom/-Uitleg, Claudes sleutels, getallenruimte). Geeft (oud, kaart)."""
    r, r2 = _rond(n, s), _rond(n2, s)
    ander, ander2 = (r - s if r > n else r + s), (r2 - s if r2 > n2 else r2 + s)
    oud = {'opgave': it['opgave'], 'antwoord': it['antwoord']}
    it['opgave'] = _sub_getal(it['opgave'], n, n2); it['antwoord'] = _fmt(r2)
    ex = it['extraVelden']; kaart = {}
    for k in ('claudeKaleSom', 'claudeUitleg'):
        if ex.get(k): ex[k] = _sub_getal(ex[k], n, n2)
    for lst in (ex.get('claudeDenkfouten') or [], ex.get('claudeFoutHints') or []):
        for f in list(lst):
            v = int(f['fout'].replace('.', '')) if re.fullmatch(r'\d[\d.]*', f['fout']) else None
            if v == n: w = n2
            elif v == ander: w = ander2
            elif v is not None and (v - r) % s == 0 and v != r: w = r2 + (v - r)
            else: w = None
            if w is None or w <= 0 or any(g is not f and g['fout'] == _fmt(w) for g in lst):   # geen 0 of minder, geen dubbele sleutel
                lst.remove(f); kaart[f['fout']] = None; continue
            kaart[f['fout']] = _fmt(w); f['fout'] = _fmt(w)
    it['getallenruimte'] = next((f'0–{_fmt(l)}' for l in (100, 1000, 10000, 100000, 1000000) if max(n2, r2) <= l), it['getallenruimte'])
    return oud, kaart
def fix152(it):
    if it['merge'].get('doel') != 'G6-GET-E01' or not (m := AFROND.search(it['opgave'] or '')): return
    n = int((m.group(1) or m.group(2)).replace('.', '')); s = STAP[m.group(3)]; cid = it['bron']['claudeId']
    vraag = vraag_e01(it['opgave']); midden = n % s == s // 2
    if midden and (vraag == 'dichtst bij' or cid not in TERUG156):          # #152: middengetal vervangen
        assert cid in VERVANG152, ('#159c: nieuw #152-item, VERVANG152 bijwerken', cid, it['opgave'])
        n2 = _nieuw152(cid, n, s); oud, kaart = _vervang152(it, n, n2, s)
        it['merge']['fixlijst152'] = {'voor': oud, 'reden': "middengetal vervangen (Didactiek V1, besluit Dave 20:16); #156d: 1 à 2 per somtype blijven (TERUG156)"}
        _log(punt=152, id=it.get('id'), claudeId=cid, oud=oud['opgave'], nieuw=it['opgave'], antwoord=[oud['antwoord'], it['antwoord']], sleutels=kaart)
        n = n2
    elif midden:                                                            # #156d: oud middengetal blijft (vraag 'rond af')
        assert TERUG156[cid] == n, ('#156d TERUG156: ander getal dan het oude #152-getal', cid, it['opgave'])
        it['merge']['fixlijst156d'] = {'middengetal': _fmt(n), 'reden': "'Rond … af op …': middengetal blijft, het oude getal van vóór #152 (besluit Dave 20:38)"}
        _log(punt='156d', id=it.get('id'), claudeId=cid, oud=it['opgave'], nieuw=it['opgave'], antwoord=[it['antwoord'], it['antwoord']], wat='middengetal blijft (oud #152-getal)')
    elif cid in MIDDEN156 and vraag == 'rond af':                          # #156d: nieuw middengetal (#5/#7/#8 hadden er geen)
        n0, n2 = MIDDEN156[cid]; assert n0 == n and n2 % s == s // 2 and n2 // (10 * s) == n // (10 * s), ('#156d MIDDEN156', cid, n, n2)
        oud, kaart = _vervang152(it, n, n2, s); r2 = _rond(n2, s)
        ex = it['extraVelden']
        if ex.get('claudeUitleg'):      # Claudes uitleg noemde de oude rest ('Kijk naar de rest: 77'); zelfde stijl, nieuwe getallen
            ex['claudeUitlegVoor156d'] = ex['claudeUitleg']
            ex['claudeUitleg'] = f"{_fmt(n2)} ligt tussen {_fmt(r2 - s)} en {_fmt(r2)}.\nKijk naar de rest: {_fmt(n2 % s)}. Dat is precies de helft van {_fmt(s)}, dus je rondt naar boven af: {_fmt(r2)}."
        it['merge']['fixlijst156d'] = {'voor': oud, 'middengetal': _fmt(n2), 'reden': "'Rond … af op …': minstens één middengetal per somtype (besluit Dave 20:38); geen oud #152-getal, dus dit item"}
        _log(punt='156d', id=it.get('id'), claudeId=cid, oud=oud['opgave'], nieuw=it['opgave'], antwoord=[oud['antwoord'], it['antwoord']], sleutels=kaart, wat='nieuw middengetal')
        n = n2
    GEBRUIKT152.add(n)
    if vraag == 'dichtst bij': assert n % s != s // 2, ("#152: middengetal bij 'het dichtst bij'", cid, it['opgave'])
    if n % s == s // 2: assert cid in TERUG156 or cid in MIDDEN156, ('#156d: middengetal buiten TERUG156/MIDDEN156', cid, it['opgave'])
    assert it['antwoord'] == _fmt(_rond(n, s)), ('#152 antwoord', cid, it['opgave'], it['antwoord'])
    assert max(n, _rond(n, s)) <= GROOT158, ('#158: getal of antwoord boven 100.000', cid, it['opgave'])
BEOORDELING153 = {'soort': 'banden', 'eenheid': 0.1,
                  'goed': {'afstandKleinerDan': 0.05, 'regel': '|x − antwoord| < 0,05'},
                  'eenTiendeErnaast': {'afstandVanaf': 0.05, 'afstandKleinerDan': 0.15, 'regel': '0,05 ≤ |x − antwoord| < 0,15', 'metRichting': True,
                                       'soorten': {'groter': 'één tiende te ver', 'kleiner': 'één tiende te kort'}},
                  'sleutel': {'afstandKleinerDan': 0.05, 'regel': '|x − sleutel| < 0,05 (de eerste sleutel die past)'},
                  'bron': 'G6 merge-fixlijst #153 (Didactiek 20:15, besluit Dave 20:16)'}
ID024 = 'Zet 8 op de lijn van 0 tot 10.'
def fix153(it):
    if it['merge'].get('doel') != 'G6-GET-M03' or not re.match(r'Zet \d+(?:,\d)? op de lijn van \d+ tot \d+\.', it['opgave'] or ''): return
    if it['opgave'] == ID024:     # #156f: een kommagetal, zoals de ouderzin zegt
        oud = it['opgave']; it['opgave'] = 'Zet 8,6 op de lijn van 0 tot 10.'; it['antwoord'] = '8,6'; ex = it['extraVelden']
        ex['claudeKaleSom'] = '8,6 op de lijn'; ex['claudeUitleg'] = 'Zoek eerst het hele getal: 8. Dan nog 6 tienden verder.'
        it['getallenruimte'] = 'kommagetallen (1 cijfers achter de komma)'
        _log(punt=156, id=it.get('id'), claudeId=it['bron']['claudeId'], oud=oud, nieuw=it['opgave'], antwoord=['8', '8,6'])
    assert re.match(r'Zet \d+,\d op de lijn', it['opgave']), ('#156f: geen kommagetal', it['opgave'])
    gl = it['visual']['getallenlijn']; gl['streepjePer'] = '0,1'; gl['streepjesPerTiende'] = True
    gl['bron'] = "G6 merge-fixlijst #153 (Dave 20:16): streepjes per tiende, ook bij 0–10" + (" (0–2: claudeUitleg 'Elk streepje is een tiende')" if gl['tot'] == 2 else '')
    it['beoordeling'] = json.loads(json.dumps(BEOORDELING153))
def asserts156(it):
    o = it['opgave'] or ''; d = it['merge'].get('doel')
    if d != 'G6-GET-M02': return
    if (m := WAARD.search(o)):        # (a) het cijfer is niet 0 en staat niet op de eenheden
        n = m.group(1).replace('.', ''); assert m.group(2) != '0' and n[-1] != m.group(2), ('#156a', o)
    if (m := re.fullmatch(r'(\d[\d.]*) wordt (\d[\d.]*)\. Met hoeveel verandert het getal\?', o)):   # (b) precies één cijfer ± 1, niet de eenheden
        a, b = m.group(1).replace('.', ''), m.group(2).replace('.', '')
        vs = [i for i in range(max(len(a), len(b))) if a.rjust(len(b), '0')[i] != b.rjust(len(a), '0')[i]]
        aa, bb = a.rjust(len(b), '0'), b.rjust(len(a), '0')
        assert len(a) == len(b) and len(vs) == 1 and abs(int(aa[vs[0]]) - int(bb[vs[0]])) == 1 and vs[0] != len(aa) - 1, ('#156b', o)
    if (m := re.search(r'staat op (\d[\d.]*)\b.*Er komt er één bij', o)):     # (c) het getal eindigt op 9
        assert m.group(1).replace('.', '').endswith('9'), ('#156c', o)
DING156 = re.compile(r'^Op het bord staat (\d[\d.]*) [a-zà-ÿ]+\. (Hoeveel is de \d in dit getal waard\?)$')
TELLER156 = re.compile(r"^De teller in (.+?) staat op (\d[\d.]*) ([a-zà-ÿ']+)\. (Er komt er één bij\. Op welk getal staat de teller nu\?)$")
def bewerk_na(it):
    """#156g, ná het somtype (zodat de koppeling aan de hint-entry blijft): 'Op het bord staat 8785 botten.' en 'De teller in het moeras staat op
    3999 eieren.' lezen raar. → 'Op het bord staat het getal 8785.' en 'In het moeras tel je eieren. De teller staat op 3999.'"""
    context164(it)                              # #164 (Oefeningen 21:10, Dave 21:07)
    na194_172(it)                               # #172 (Dave 21:24), #194 (Didactiek 21:25)
    na201(it)                                   # #201 (Didactiek batch 3, 21:42)
    na218(it); na227(it)                        # ronde 7 (#218 E03 #1 contexten, #227 E03 #5 zonder plaatje)
    na228_230(it); na251(it)                    # ronde 8 (#228 contexten, #230 komma/kleine letter, #251 niveau grootst/kleinst)
    o = it['opgave'] or ''; cid = it['bron']['claudeId']
    if it['merge'].get('doel') == 'G6-GET-E01': return context160(it)
    if it['merge'].get('doel') != 'G6-GET-M02': return
    if (m := DING156.match(o)): it['opgave'] = f'Op het bord staat het getal {m.group(1)}. {m.group(2)}'; punt = 156
    elif (m := TELLER156.match(o)) and cid in M02_160:      # #160: de letterlijke opgave van Didactiek (recheck-batch1b §3), zonder 'de teller'
        assert m.group(2) == M02_160[cid][0], ('#160: ander getal dan in de lijst', cid, o)
        it['opgave'] = M02_160[cid][1]; punt = 160
        assert re.search(rf'(?<![\d.]){re.escape(m.group(2))}(?!\d|\.\d)', it['opgave']) and m.group(2).replace('.', '').endswith('9'), ('#160/#156c', cid, it['opgave'])
    elif TELLER156.match(o): raise AssertionError(('#160: M02 #4-item zonder nieuwe opgave (M02_160 bijwerken)', cid, o))
    else: return
    it['merge']['opgaveVoor156'] = o
    _log(punt=punt, id=it.get('id'), claudeId=cid, oud=o, nieuw=it['opgave'])
    asserts156(it); grens158(it)
# #160 (Didactiek recheck-batch1b §3, besluit Dave 20:49): M02 #4 letterlijk de opgaven van Didactiek; het antwoord blijft hetzelfde.
M02_160 = {'0d7a78bc-cc7b-4480-ba44-c4365805c6fc': ('3999', 'In het museum waren vandaag 3999 bezoekers. Er komt er nog één bij. Hoeveel bezoekers zijn het nu?'),
           '10d61a31-9e7f-4e96-9c32-9ee54e1fb2ea': ('1599', 'Voor het concert zijn 1599 kaartjes verkocht. Er wordt er nog één verkocht. Hoeveel kaartjes zijn het nu?'),
           '50688d7e-6847-4960-b043-e3a5cb84155c': ('5299', 'Op de stappenteller van Sem staat 5299. Hij zet nog één stap. Wat staat er nu op de stappenteller?'),
           '559bf94e-869f-48f3-a297-4f237e407032': ('9199', 'In de bibliotheek staan 9199 boeken. Er komt er één bij. Hoeveel boeken zijn het nu?'),
           '77065757-359b-4a6d-b827-ba8d07748642': ('6399', 'Vandaag zijn 6399 fietsers over de brug gereden. Er komt er nog één bij. Hoeveel fietsers zijn het nu?'),
           '80ba330e-c79b-4211-9c3a-3a198fd10bc4': ('6699', 'Op het festival zijn 6699 bandjes uitgedeeld. Er komt er nog één bij. Hoeveel bandjes zijn het nu?'),
           '8fae5e6d-b0b5-45e6-8af3-c5b2c198f93e': ('8999', 'In de kantine zijn dit jaar 8999 broodjes verkocht. Er komt er nog één bij. Hoeveel broodjes zijn het nu?'),
           '9f82e4ec-1a4c-4899-b81d-ecc8232724a1': ('6699', 'In het zwembad waren deze maand 6699 zwemmers. Er komt er nog één bij. Hoeveel zwemmers zijn het nu?')}
# #160: E01 #5/#7/#8 een context waar zo'n aantal echt kan (bezoekers, kaartjes, stappen, boeken, munten); '{n}' = het getal van het item.
CONTEXT160 = {'1d39d92b-4a22-49b0-b6f3-74de3251c2f4': 'Bij de wedstrijd waren precies {n} toeschouwers.',             # #7 005
              '8bee0469-76af-4336-8f09-d1a24183ab8f': 'Voor het concert zijn precies {n} kaartjes verkocht.',          # #7 006
              'e0488799-a969-4a9f-809f-0be94e4c4193': 'Sem heeft deze week precies {n} stappen gezet.',                # #7 007
              'fbf46408-5af6-471c-94e9-e5bbf0f9dfd4': 'In de bibliotheek staan precies {n} boeken.',                   # #7 008
              '048098de-56ed-4b81-9d2d-67e913ae9ad1': 'Bij de wedstrijd waren precies {n} toeschouwers.',             # #5 009
              '23a08ce7-e87c-4291-8342-0be1f3dede8d': 'Het museum had deze maand precies {n} bezoekers.',             # #5 010
              '4afd93f4-1976-414e-9744-a31356a864a7': 'De bibliotheek heeft dit jaar precies {n} boeken uitgeleend.',   # #5 011
              '79731b22-ec47-4671-9549-767fbe586f17': 'Mila heeft deze week precies {n} stappen gezet.',               # #5 012
              '9578f8c2-eb01-4994-8c25-289e907ab141': 'Op het festival waren precies {n} bezoekers.',                  # #5 013
              '5b0bad0e-0e9e-4745-8b80-98e823851ba4': 'Vandaag zijn precies {n} fietsers over de brug gereden.',       # #8 014
              'e72e2432-f926-40a3-ad7a-fbb7a636e830': 'In de kantine zijn dit jaar precies {n} broodjes verkocht.',    # #8 015
              'f82ba53d-0138-4539-9fb4-0df03753f716': 'In de spaarpot van de school zitten precies {n} munten.'}       # #8 016
CTX = re.compile(r'^(?:In|Op|Bij) .+? zijn precies (\d[\d.]*) [a-zà-ÿ]+\. (Rond dit aantal af op (?:tientallen|honderdtallen|duizendtallen)\.)$')
def context160(it):
    o = it['opgave'] or ''; cid = it['bron']['claudeId']
    if not (m := CTX.match(o)): return
    assert cid in CONTEXT160, ('#160: E01-item met de oude context (CONTEXT160 bijwerken)', cid, o)
    it['opgave'] = CONTEXT160[cid].format(n=m.group(1)) + ' ' + m.group(2)
    it['merge']['opgaveVoor160'] = o
    _log(punt=160, id=it.get('id'), claudeId=cid, oud=o, nieuw=it['opgave'])
    assert AFROND.search(it['opgave']), ('#160: AFROND past niet meer', it['opgave'])
_G = re.compile(r'(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d,])|(?<![\d.,])\d+(?![\d.,]\d|\d)')
def getallen158(t): return [int(x.replace('.', '')) for x in _G.findall(str(t or ''))]
def grens158(it):
    """#158/#199: ná de fixlijst nog eens door de grens van G6 (regels_g6: hele getallen tot 100.000): geen getal of antwoord boven 100.000 in een
    G6-GET- of G6-MEET-item (opgave, opties, antwoord)."""
    if not (it['merge'].get('doel') or '').startswith(('G6-GET', 'G6-MEET')): return      # #199: ook MEET
    # Didactiek 21:25: alleen wat het kind ziet (opgave, opties) en het antwoord; fout-sleutels die nooit getoond worden mogen erboven (MEET-E01: 220.000 bij 22 km = □ m)
    m = max(getallen158(it['opgave']) + getallen158(it['antwoord']) + [x for o in it.get('opties') or [] for x in getallen158(o['tekst'])] + [0])
    assert m <= GROOT158, ('#158: getal boven 100.000 in een G6-GET- of G6-MEET-item (na de fixlijst)', it['bron']['claudeId'], it['opgave'], it['antwoord'])
def schrijf_log(out):
    json.dump(LOG, open(f'{out}/logs/fixlijst_g6.json', 'w'), ensure_ascii=False, indent=1)

# ------------------------------------------------------------------ ronde 3: Oefeningen batch 2 (#162–#167, fixlijst 21:10; besluiten Dave 21:07)
# #162 E07 #1 item 002 «3 truien van elk €998»: Claude rekende met '998 is bijna 900'. Opnieuw vanuit de echte som (998 is bijna 1000).
ID162 = '23bbdc97-e25d-405d-beb2-ee34e5388471'
def fix162(it):
    if it['bron']['claudeId'] != ID162: return
    m = re.match(r'(\d+) [a-zà-ÿ\']+ van elk €(\d+)\.', it['opgave']); n, p = int(m.group(1)), int(m.group(2))
    assert (n, p) == (3, 998) and it['antwoord'] == f'€{n * p}', ('#162: E07 002 is veranderd', it['opgave'], it['antwoord'])
    rond = -(-p // 100) * 100; d = rond - p                                   # 1000, 2
    nieuw = {'€2700': f'€{n * rond}', '€2991': f'€{n * rond - 2 * n * d}'}    # €3000 (stukje niet afgehaald), €2988 (te veel afgehaald: 3000 − 3 × 4)
    ex = it['extraVelden']; oud = {'claudeUitleg': ex.get('claudeUitleg'), 'sleutels': [f['fout'] for f in ex.get('claudeFoutHints') or []]}
    ex['claudeUitleg'] = f'{p} is bijna {rond}.\n{n} × {rond} = {n * rond}, dat is {n * d} te veel.\n{n * rond} − {n * d} = {n * p}.'
    tekst = {f'€{n * rond}': f'Je hebt met het ronde getal gerekend. Haal er nu {n} × {d} af.', f'€{n * rond - 2 * n * d}': 'Hoeveel heb je te veel gerekend? 3 keer het verschil.'}
    for lst in (ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], it['foutHints']):
        for f in lst:
            if f['fout'] in nieuw:
                f['fout'] = nieuw[f['fout']]
                if 'uitleg' in f and lst is ex.get('claudeFoutHints'): f['uitleg'] = tekst[f['fout']]
    ks = {f['fout'] for f in ex['claudeFoutHints']}
    assert ks == {'€3000', '€2988', '€1001'} and it['antwoord'] == '€2994', ('#162', ks)
    _log(punt=162, id=it.get('id'), claudeId=ID162, oud=oud, nieuw={'claudeUitleg': ex['claudeUitleg'], 'sleutels': sorted(ks)})

# #163 M05 #3 (sorteren: deelbaar of niet): motorregels 'één getal in het verkeerde vak' en 'vakken omgewisseld' (fout_regels.py); teksten van Oefeningen (fixlijst #163)
R163 = [('fout = één getal in het verkeerde vak', 'één getal in het verkeerde vak',
         'Eén getal staat in het verkeerde vak. Kijk bij elk getal: kun je het precies in groepjes van dat aantal verdelen, zonder dat er iets overblijft?'),
        ('fout = vakken omgewisseld', 'vakken omgewisseld', 'Je hebt de vakken omgewisseld. Bij deelbaar horen de getallen waarbij niets overblijft.')]
SORT163 = re.compile(r'^Sleep elk getal naar het goede vak: deelbaar door (\d+) of niet\.$')
# #193 (Didactiek 21:35, merge-fixlijst): 'verkeerde vak' met een richting, vóór de algemene regel van #163 (die blijft als vangnet)
R193 = [('fout = een deelbaar getal bij niet', 'deelbaar getal bij niet',
         'Bij niet deelbaar staat een getal dat je wél precies kunt verdelen in groepjes van dat aantal. Welk getal is dat?'),
        ('fout = een niet-deelbaar getal bij deelbaar', 'niet-deelbaar getal bij deelbaar',
         'Bij deelbaar staat een getal waarbij er iets overblijft. Welk getal is dat?')]
def _m05_193(st):
    fh = st['foutHints']
    if any(f['regel'] == R193[0][0] for f in fh): return          # Oefeningen heeft ze al in de entry
    i = next((k for k, f in enumerate(fh) if f['regel'] == R163[0][0]), next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh)))
    fh[i:i] = [{'regel': r, 'soort': s, 'tekst': t, 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #193, Didactiek 21:35; tekst Didactiek)'} for r, s, t in R193]
    _log(punt=193, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[r for r, _, _ in R193], voor=R163[0][0])
def _m05_163(st):
    fh = st['foutHints']
    if any(f['regel'] == R163[0][0] for f in fh): return          # Oefeningen heeft de regels zelf in de entry gezet
    i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
    fh[i:i] = [{'regel': r, 'soort': s, 'tekst': t, 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #163, besluit Dave 21:07; tekst Oefeningen)'} for r, s, t in R163]
    _log(punt=163, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[r for r, _, _ in R163], voor='andere fout')
def fix163(it):
    if it['merge'].get('doel') != 'G6-GET-M05' or not (m := SORT163.match(it['opgave'] or '')): return
    w = re.fullmatch(r'wel:([\d,]+)\|niet:([\d,]+)', str(it['antwoord'])); assert w, ('#163: geen sorteerantwoord', it['antwoord'])
    k = int(m.group(1)); wel, niet = [int(x) for x in w.group(1).split(',')], [int(x) for x in w.group(2).split(',')]
    assert all(x % k == 0 for x in wel) and all(x % k for x in niet), ('#163: indeling klopt niet', it['opgave'], it['antwoord'])
    assert max(wel + niet) <= 200
    if it.get('getallenruimte') != '0–200':
        _log(punt=163, id=it.get('id'), claudeId=it['bron']['claudeId'], veld='getallenruimte', oud=it.get('getallenruimte'), nieuw='0–200'); it['getallenruimte'] = '0–200'

# #165 E06 #5: twee keer 8 × 250. Item 002 (zelfde id) wordt 12 × 250 = 3000; Claudes sleutels opnieuw (nul-fout ×10/:10, opgeteld).
ID165 = 'fa542903-afa3-410c-989d-b9719436d0d2'
def fix165(it):
    if it['bron']['claudeId'] != ID165: return
    m = re.fullmatch(r'(\d+) dozen met (\d+) ([a-zà-ÿ\']+)\. Hoeveel \3\? Reken handig\.', it['opgave'])
    assert m and (m.group(1), m.group(2), it['antwoord']) == ('8', '250', '2000'), ('#165: E06 002 is veranderd', it['opgave'])
    n, p = 12, 250; a = n * p; oud = it['opgave']
    it['opgave'] = f'{n} dozen met {p} {m.group(3)}. Hoeveel {m.group(3)}? Reken handig.'; it['antwoord'] = str(a)
    ex = it['extraVelden']; ex['claudeKaleSom'] = f'{n} × {p}'; ex['claudeUitleg'] = f'{p} past mooi in 1000 (4 keer).\n{n} × {p} = {a}.'
    nw = {'200': str(a // 10), '20.000': f'{a * 10:,}'.replace(',', '.'), '20000': str(a * 10), '258': str(n + p)}
    for lst in (ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], it['foutHints'], ex.get('mergeFoutHints') or []):
        for f in lst:
            assert f['fout'] in nw, ('#165: onbekende sleutel', f['fout']); f['fout'] = nw[f['fout']]
    it['merge']['opgaveVoor165'] = oud
    _log(punt=165, id=it.get('id'), claudeId=ID165, oud=f'{oud} => 2000', nieuw=f"{it['opgave']} => {a}", sleutels=sorted({f['fout'] for f in ex['claudeFoutHints']}))

# #166 E04 #1/#2: claudeUitleg die niet bij het item past → verbeterd (de oude tekst staat in merge.claudeUitlegVoor166)
MIN166 = re.compile(r'(?:In|Op) .+? lagen (\d+) [a-zà-ÿ\']+\. Er zijn er (\d+) weggehaald\.')
PLUS166 = re.compile(r'(?:In|Op) .+? liggen (\d+) [a-zà-ÿ\']+, (?:in|op) .+? (\d+)\. Hoeveel zijn het er samen\? Reken onder elkaar\.')
def uitleg166(opg):
    if (m := MIN166.match(opg)):
        a, b = int(m.group(1)), int(m.group(2)); e1, e2, t1 = a % 10, b % 10, a // 10 % 10
        if e1 < e2:
            z = f'Bij de eenheden kun je {e1} − {e2} niet'
            z += (', en de tientallen zijn 0.\nLeen van de honderdtallen of duizendtallen: de nullen worden 9, en de kolom links ervan één minder.' if t1 == 0
                  else '.\nLeen één tiental: bij de eenheden komt er 10 bij, bij de tientallen staat er één minder.')
        else: z = f'Bij de eenheden: {e1} − {e2} = {e1 - e2}.\nGa zo door per kolom. Kun je een kolom niet, leen dan van de kolom links ervan.'
        return f'{z}\nUitkomst: {a - b}.'
    if (m := PLUS166.match(opg)):
        a, b = int(m.group(1)), int(m.group(2)); s = a % 10 + b % 10
        z = f'{a % 10} + {b % 10} = {s}, schrijf {s - 10}, onthoud 1.' if s >= 10 else f'{a % 10} + {b % 10} = {s}, schrijf {s}.'
        return f'Onder elkaar, van rechts naar links: {z}\nGa zo door per kolom. Uitkomst: {a + b}.'
def fix166(it):
    if it['merge'].get('doel') != 'G6-GET-E04' or not (u := uitleg166(it['opgave'] or '')): return
    ex = it['extraVelden']; oud = ex.get('claudeUitleg')
    if oud == u: return
    ex['claudeUitleg'] = u; it['merge']['claudeUitlegVoor166'] = oud
    _log(punt=166, id=it.get('id'), claudeId=it['bron']['claudeId'], opgave=it['opgave'], oud=oud, nieuw=u)

# #167 interne namen voor Claudes optie-labels (de kinderen zien ze niet; de export wordt leesbaar). Claudes label blijft in denkfoutClaude.
REN167 = {('G6-GET-E04', 3): {'geld-verkeerd-geteld': 'verkeerd-stukje', 'schatting-verkeerd': 'allebei-rond'},
          ('G6-GET-E04', 5): {'geld-verkeerd-geteld': 'verkeerd-stukje', 'schatting-verkeerd': 'allebei-rond'},
          ('G6-GET-E04', 4): {'komma-verschoven': 'eerste-getal-klopt-niet'},
          ('G6-GET-E04', 7): {'komma-verschoven': 'eerste-getal-klopt-niet'},
          ('G6-GET-E06', 2): {'geld-verkeerd-geteld': 'verkeerd-stukje', 'schatting-verkeerd': 'stukje-keer-het-ronde-getal'},
          ('G6-GET-E06', 4): {'komma-verschoven': 'tweede-getal-klopt-niet'}}
OPG167 = [('G6-GET-E04', re.compile(r'^Hoe reken je \d+ [+−] \d+ handig uit\?$'), (3, 5)), ('G6-GET-E04', re.compile(r'^Welke som is even ?veel als \d+ [+−] \d+\?$'), (4, 7)),
          ('G6-GET-E06', re.compile(r'^Hoe reken je \d+ × \d+ handig uit\?$'), (2,)), ('G6-GET-E06', re.compile(r'^Welke som is even ?veel als \d+ × \d+\?$'), (4,))]
def _e167(st):
    ren = REN167.get((st['doel'], st.get('nrOrigineel')))
    if not ren: return
    for f in st['foutHints']:
        if f.get('claudeDenkfout') in ren:
            o = f['claudeDenkfout']; f['claudeDenkfoutOrigineel'] = o; f['claudeDenkfout'] = ren[o]; f['regel'] = f'Claudes sleutel: {ren[o]}'
            _log(punt=167, entry=f"{st['doel']} #{st['nrOrigineel']}", oud=o, nieuw=ren[o])
def fix167(it):
    d = it['merge'].get('doel'); ren = {}
    for dd, rx, nrs in OPG167:
        if d == dd and rx.match(it['opgave'] or ''):
            for n in nrs: ren.update(REN167[(dd, n)])
    for dk in it['extraVelden'].get('claudeDenkfouten') or []:
        if dk['denkfout'] in ren: dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = ren[dk['denkfout']]
    for f in it['foutHints']:
        for o, n in ren.items(): f['regel'] = (f.get('regel') or '').replace(f'Claudes sleutel: {o}', f'Claudes sleutel: {n}') or f.get('regel')

# #164 contexten die bij het aantal passen (les 14, zoals #160). Alleen het verhaal verandert; getallen, antwoord en sleutels blijven. Keuze per item op hash.
def _k(it, lst, tag): return lst[_h(f"{it['bron']['claudeId']}-{tag}") % len(lst)]
LIG164 = [('het magazijn', 'schriften'), ('de drukkerij', 'folders'), ('de bouwmarkt', 'tegels'), ('het sorteercentrum', 'pakketten'), ('de bibliotheek', 'boeken'),
          ('het postkantoor', 'enveloppen'), ('de bouwmarkt', 'bakstenen'), ('de houthandel', 'planken'), ('het magazijn', 'dozen'), ('de drukkerij', 'kranten')]
TWEE164 = [('het magazijn', 'de winkel', 'schriften'), ('de bibliotheek', 'het depot', 'boeken'), ('het sorteercentrum', 'het postkantoor', 'pakketten'),
           ('de drukkerij', 'het magazijn', 'folders'), ('de bouwmarkt', 'het magazijn', 'tegels'), ('de ene loods', 'de andere loods', 'planken')]
ZIJN164 = [('de bibliotheek', 'het depot', 'boeken'), ('het magazijn', 'de winkel', 'schriften'), ('de fabriek', 'het magazijn', 'flessen'), ('het sorteercentrum', 'het postkantoor', 'pakketten')]
WEG164 = [('kaartjes', 'de voorverkoop'), ('flessen', 'het magazijn'), ('boeken', 'het depot van de bibliotheek'), ('pakketten', 'het sorteercentrum'),
          ('tegels', 'de bouwmarkt'), ('schriften', 'het magazijn'), ('folders', 'de drukkerij'), ('kranten', 'de drukkerij')]
RIJ164 = [('In de zaal', 'stoelen'), ('In de moestuin', 'plantjes'), ('In de boomgaard', 'appelbomen'), ('In de kas', 'tomatenplanten'),
          ('Op het bollenveld', 'tulpen'), ('Op de parkeerplaats', "auto's"), ('In het theater', 'stoelen'), ('In de sporthal', 'stoelen')]
DOOS164 = ['punaises', 'paperclips', 'elastiekjes', 'nietjes']
KIST164 = [('het magazijn', 'dozen', 'enveloppen'), ('de bouwmarkt', 'pallets', 'tegels'), ('de drukkerij', 'dozen', 'folders')]
VERK164 = ['kaartjes', 'loten', 'flessen water', 'kranten']
DAG164 = [('Een kippenboer', 'eieren'), ('Een fruitteler', 'appels'), ('Een recyclepunt', 'lege flessen'), ('Een tuinder', 'tomaten')]
PRIJS164 = {199: ['stoelen', 'tenten', 'steps'], 499: ['tablets', 'fietsen'], 998: ['fietsen', 'laptops']}
W = r"[a-zà-ÿ']+"
CTX164 = [  # (doel, regex, maak(m, it))
    ('G6-GET-E04', re.compile(rf'^(?:In|Op) .+? lagen (\d+) {W}\. Er zijn er (\d+) weggehaald\. Hoeveel {W} zijn er nog\?$'),
     lambda m, it: (lambda p, d: f'In {p} lagen {m.group(1)} {d}. Er zijn er {m.group(2)} weggehaald. Hoeveel {d} zijn er nog?')(*_k(it, LIG164, 164))),
    ('G6-GET-E04', re.compile(rf'^(?:In|Op) .+? liggen (\d+) {W}, (?:in|op) .+? (\d+)\. (Hoeveel zijn het er samen\? Reken onder elkaar\.)$'),
     lambda m, it: (lambda p, q, d: f'In {p} liggen {m.group(1)} {d}, in {q} {m.group(2)}. {m.group(3)}')(*_k(it, TWEE164, 164))),
    ('G6-GET-E04', re.compile(rf'^Er waren (\d+) {W} in .+?\. Nu zijn er nog (\d+)\. Hoeveel {W} zijn er weg\?$'),
     lambda m, it: (lambda d, p: f'Er waren {m.group(1)} {d} in {p}. Nu zijn er nog {m.group(2)}. Hoeveel {d} zijn er weg?')(*_k(it, WEG164, 164))),
    ('G6-GET-E04', re.compile(rf'^(?:In|Op) .+? zijn (\d+) {W} en (?:in|op) .+? (\d+)\. Hoeveel {W} zijn dat samen\?$'),
     lambda m, it: (lambda p, q, d: f'In {p} zijn {m.group(1)} {d} en in {q} {m.group(2)}. Hoeveel {d} zijn dat samen?')(*_k(it, ZIJN164, 164))),
    ('G6-GET-E06', re.compile(rf'^(?:In|Op) .+? staan (\d+) rijen met (\d+) {W}\. Hoeveel {W} zijn dat\?$'),
     lambda m, it: (lambda p, d: f'{p} staan {m.group(1)} rijen met {m.group(2)} {d}. Hoeveel {d} zijn dat?')(*_k(it, RIJ164, 164))),
    ('G6-GET-E06', re.compile(rf'^(\d+) dozen met (\d+) {W}\. Hoeveel {W}\? Reken handig\.$'),
     lambda m, it: (lambda d: f'{m.group(1)} dozen met {m.group(2)} {d}. Hoeveel {d}? Reken handig.')(DOOS164[0] if it['bron']['claudeId'] != ID165 else DOOS164[1])),
    ('G6-GET-E06', re.compile(rf'^(?:In|Op) .+? staan (\d+) {W} met elk (\d+) {W}\. Hoeveel {W} zijn dat\?$'),
     lambda m, it: (lambda p, b, d: f'In {p} staan {m.group(1)} {b} met elk {m.group(2)} {d}. Hoeveel {d} zijn dat?')(*_k(it, KIST164, 164))),
    ('G6-GET-M05', re.compile(rf'^Van (\d+) {W} worden er (\d+) verkocht\. (Hoeveel blijven er over\? Reken uit het hoofd\.)$'),
     lambda m, it: f'Van {m.group(1)} {_k(it, VERK164, 164)} worden er {m.group(2)} verkocht. {m.group(3)}'),
    ('G6-GET-M06', re.compile(rf'^Een {W} verzamelt elke dag (\d+) {W}\. Hoeveel {W} zijn dat in (\d+) dagen\?$'),
     lambda m, it: (lambda w, d: f'{w} verzamelt elke dag {m.group(1)} {d}. Hoeveel {d} zijn dat in {m.group(2)} dagen?')(*_k(it, DAG164, 164))),
    ('G6-GET-E07', re.compile(rf'^(\d+) {W} van elk €(\d+)\. (Hoeveel is dat samen\? Reken handig\.)$'),
     lambda m, it: f'{m.group(1)} {_k(it, PRIJS164[int(m.group(2))], 164)} van elk €{m.group(2)}. {m.group(3)}')]
def context164(it):
    d = it['merge'].get('doel'); o = it['opgave'] or ''
    for dd, rx, maak in CTX164:
        if d == dd and (m := rx.match(o)):
            n = maak(m, it)
            if n == o: return
            assert re.findall(r'\d+', n) == re.findall(r'\d+', o), ('#164: getallen veranderd', o, n)
            it['opgave'] = n; it['merge']['opgaveVoor164'] = o
            _log(punt=164, id=it.get('id'), claudeId=it['bron']['claudeId'], oud=o, nieuw=n); return

# ------------------------------------------------------------------ ronde 4: batch 3 breuken (Oefeningen 21:23, Dave 21:24) + Didactiek batch 2 (21:25)
import sys as _sys
_sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import breukvorm as BV
# #169 E03 #7: lijn van 0 tot 1 met streepjes per stuk (de noemer), beoordeling met banden (zoals #153) en de motorregel 'één stuk ernaast'
LIJN169 = re.compile(r'^Zet (\d+)/(\d+) op de lijn van 0 tot 1\.$')
R203 = [('fout = een stuk te ver', 'een stuk te ver', 'Bijna! Je bent één stuk te ver. Tel vanaf nul de stukken nog eens.'),
        ('fout = een stuk te kort', 'een stuk te kort', 'Bijna! Je bent één stuk te kort. Tel vanaf nul de stukken nog eens.')]      # #203 (besluit Oefeningen 21:59); tekst = voorstel Didactiek #186
R169 = ('fout = één stuk ernaast', 'één stuk ernaast', 'Bijna! Dat is één stuk ernaast. Tel vanaf nul de stukken nog eens.')
def beoordeling169(n):
    return {'soort': 'banden', 'eenheid': f'1/{n}', 'eenheidWaarde': round(1 / n, 6),
            'goed': {'afstandKleinerDan': round(0.5 / n, 6), 'regel': '|x − antwoord| < een half stuk (1/(2 × noemer))'},
            'eenStukErnaast': {'afstandVanaf': round(0.5 / n, 6), 'afstandKleinerDan': round(1.5 / n, 6), 'regel': 'een half stuk ≤ |x − antwoord| < anderhalf stuk', 'metRichting': True,
                               'soorten': {'groter': 'een stuk te ver', 'kleiner': 'een stuk te kort'}, 'regelMotor': {'groter': R203[0][0], 'kleiner': R203[1][0]}},      # #203
            'sleutel': {'afstandKleinerDan': round(0.5 / n, 6), 'regel': '|x − sleutel| < een half stuk (de eerste sleutel die past)'},
            'gelijkwaardig': 'de plek telt: 2/4, 3/6 en 1/2 zijn dezelfde plek', 'bron': 'G6 merge-fixlijst #169 (Oefeningen 21:23, besluit Dave 21:24; zoals #153)'}
def fix169(it):
    if it['merge'].get('doel') != 'G6-GET-E03' or not (m := LIJN169.match(it['opgave'] or '')): return
    t, n = int(m.group(1)), int(m.group(2)); assert 0 < t <= n and it['antwoord'] == f'{t}/{n}', ('#169', it['opgave'], it['antwoord'])
    it['visual']['getallenlijn'] = {'van': 0, 'tot': 1, 'streepjes': n, 'streepjePer': f'1/{n}', 'getallenBijStreepjes': ['0', '1'],
                                    'bron': 'G6 merge-fixlijst #169 (Dave 21:24): streepjes per stuk (de noemer); alleen 0 en 1 staan erbij'}
    it['visual']['nodig'] = True
    it['beoordeling'] = beoordeling169(n)
    _log(punt=169, claudeId=it['bron']['claudeId'], opgave=it['opgave'], streepjes=n)
def _e169(st):
    fh = st['foutHints']
    if any(f['regel'] == R169[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
    fh[i:i] = [{'regel': R169[0], 'soort': R169[1], 'tekst': R169[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #169, besluit Dave 21:24; tekst Oefeningen)'}]
    _log(punt=169, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R169[0]], voor='andere fout')
# #170: een even grote breuk is goed (tools/breukvorm.py), behalve bij een gevraagde vorm; daar de regel 'gelijkwaardig maar niet zo eenvoudig mogelijk'
R170 = ('fout = gelijkwaardig maar niet zo eenvoudig mogelijk', 'nog niet eenvoudigst',
        'Die breuk is even groot, maar nog niet zo eenvoudig mogelijk. Kun je de teller en de noemer nog eens door hetzelfde getal delen?')
def fix170(it):
    if BV.pas_toe(it): _log(punt=170, claudeId=it['bron']['claudeId'], doel=it['merge'].get('doel'), antwoord=it['antwoord'], ookGoed=it['antwoordOokGoed'][:4])
def _e170(st):
    fh = st['foutHints']
    if any(f['regel'] == R170[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
    fh[i:i] = [{'regel': R170[0], 'soort': R170[1], 'tekst': R170[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #170, besluit Dave 21:24; tekst Oefeningen)'}]
    _log(punt=170, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R170[0]], voor='andere fout')
# #171 M04 #4: het voorbeeld in de opgave is nooit het antwoord (antwoorden: 1/8, 1/5, 2/5, 4/5, 7/8, 1/10, 2/3, 4/10) → '3/7' (noemer 7 komt niet voor)
VB171 = ['3/7', '5/9', '4/11']
STUK171 = re.compile(r"(?:delen|snijden) een [a-zà-ÿ' ]+? in (\d+) gelijke stukken\..*Typ een breuk, zoals (\d+/\d+)\.")      # ook 'reep chocola' (#187)
def fix171(it):
    """#171/#187: één vast voorbeeld (3/7), behalve als dat het antwoord, een even grote breuk of een sleutel is (Didactiek #187: voorbeeld ∉ {antwoord, ookGoed, sleutels})."""
    if it['merge'].get('doel') != 'G6-GET-M04' or not (m := STUK171.search(it['opgave'] or '')): return
    n = int(m.group(1)); a = BV.waarde(it['antwoord']); e = re.search(r'eet er (\d+) op', it['opgave'])
    verboden = {a} | {BV.waarde(x) for x in it.get('antwoordOokGoed') or []} | {BV.waarde(d['fout']) for d in it['extraVelden'].get('claudeDenkfouten') or []}
    if e:
        e = int(e.group(1)); verboden |= {BV.waarde(f'{n}/{e}'), BV.waarde(f'{n - e}/{n}')} | ({BV.waarde(f'{e}/{n - e}')} if n > e else set())
    vb = next(v for v in VB171 if BV.waarde(v) not in verboden)
    oud = it['opgave']; it['opgave'] = oud.replace(f'zoals {m.group(2)}.', f'zoals {vb}.')
    assert BV.waarde(vb) not in verboden and vb not in it['opgave'].split('zoals')[0], ('#171/#187: het voorbeeld is een antwoord of sleutel', it['opgave'])
    if it['opgave'] != oud: _log(punt=171, claudeId=it['bron']['claudeId'], oud=oud, nieuw=it['opgave'])
# #174 leesbare labels (zoals #167); het nieuwe label = de soort van Oefeningen; Claudes label blijft in denkfoutClaude / claudeDenkfoutOrigineel
REN174 = {('G6-GET-E03', 1): {'teller-en-noemer-optellen': 'nog-niet-eenvoudigst'},
          ('G6-GET-E03', 2): {'grotere-noemer-is-groter': 'een-andere-breuk'}, ('G6-GET-E03', 3): {'grotere-noemer-is-groter': 'een-andere-breuk'},
          ('G6-GET-E03', 4): {'omgekeerd-gedeeld': 'teller-klopt-niet'},
          ('G6-GET-E03', 8): {'teller-en-noemer-optellen': 'een-van-de-twee-gedeeld'},
          ('G6-GET-M04', 4): {'teller-en-noemer-optellen': 'getallen-op-de-verkeerde-plek'},
          ('G6-GET-E09', 3): {'deel-vergeten-bij-splitsen': 'niet-verdeeld'}}
OPG174 = [('G6-GET-E03', re.compile(r'^Schrijf \d+/\d+ zo eenvoudig mogelijk\.$'), 1), ('G6-GET-E03', re.compile(r'^Welke breuk is het grootst\?'), 2),
          ('G6-GET-E03', re.compile(r'^Welke breuk is het kleinst\?'), 3), ('G6-GET-E03', re.compile(r'^Schrijf \d+/\d+ met noemer \d+\.$'), 4),
          ('G6-GET-E03', re.compile(r'^\d+/\d+ van de .+ heeft een .+\. Schrijf die breuk zo eenvoudig mogelijk\.$'), 8),
          ('G6-GET-M04', re.compile(r'delen een .+ in \d+ gelijke stukken'), 4), ('G6-GET-E09', re.compile(r' krijgt \d+/\d+ van \d+ '), 3)]
def _e174(st):
    ren = REN174.get((st['doel'], st.get('nrOrigineel')))
    for f in st['foutHints'] if ren else []:
        if f.get('claudeDenkfout') in ren:
            o = f['claudeDenkfout']; f['claudeDenkfoutOrigineel'] = o; f['claudeDenkfout'] = ren[o]; f['regel'] = f'Claudes sleutel: {ren[o]}'
            _log(punt=174, entry=f"{st['doel']} #{st['nrOrigineel']}", oud=o, nieuw=ren[o])
def fix174(it):
    d = it['merge'].get('doel'); ren = {}
    for dd, rx, n in OPG174:
        if d == dd and rx.search(it['opgave'] or ''): ren.update(REN174[(dd, n)])
    for dk in it['extraVelden'].get('claudeDenkfouten') or []:
        if dk['denkfout'] in ren: dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = ren[dk['denkfout']]
# #190 (Didactiek 21:25) E06 #1: 37 sleutels zijn getal1 × (de cijfers van getal2 opgeteld), geen 'stuk vergeten'. Eigen regel en label vóór de Claude-regel.
R190 = ('fout = getal1 × (som van de cijfers van getal2)', 'cijfers van het tweede getal opgeteld',
        'Je hebt de cijfers van het tweede getal bij elkaar opgeteld. Zo reken je niet keer het hele getal. Splits het eerste getal in tientallen en eenheden, en doe elk stuk keer het hele tweede getal.')
LAB190 = 'cijfers-van-getal2-opgeteld'
KEER190 = re.compile(r'^(\d+) × (\d+) =$')
def fix190(it):
    if it['merge'].get('doel') != 'G6-GET-E06' or not (m := KEER190.match(it['opgave'] or '')): return
    a, b = int(m.group(1)), int(m.group(2)); v = str(a * sum(int(x) for x in str(b))); n = 0
    if b % 10 == 0 or is196(b): return      # × 40 → × 4 is 'nul vergeten'; × 19 → × 10 is 'stuk vergeten' (#196)
    for dk in it['extraVelden'].get('claudeDenkfouten') or []:
        if dk['fout'].replace('.', '') == v and dk['denkfout'] != LAB190: dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = LAB190; n += 1
    if n: _log(punt=190, claudeId=it['bron']['claudeId'], opgave=it['opgave'], sleutel=v)
def _e190(st):
    fh = st['foutHints']
    if any(f['regel'] == R190[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f.get('claudeDenkfout') == 'deel-vergeten-bij-splitsen'), next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh)))
    fh[i:i] = [{'regel': R190[0], 'soort': R190[1], 'tekst': R190[2], 'bron': 'nieuw',
                'door': 'Overzicht (G6-fixlijst #190a, Didactiek 21:25); tekst Oefeningen (#190b, merge-fixlijst)'}]
    _log(punt=190, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R190[0]], voor='Claudes sleutel: deel-vergeten-bij-splitsen')
# #192 (Didactiek 21:25): 'even veel' → 'evenveel' (opgave; de kop van het somtype volgt)
def _e192(st):
    """#192 ook in de entry (in het geheugen): de ouderzin en de hintteksten zeggen 'die even veel is'. Herkomst (somtypeOrigineel, 'van') blijft."""
    wat = []
    for k, v in list(st.items()):
        if k not in ('somtypeOrigineel', 'van') and isinstance(v, str) and 'even veel' in v: st[k] = v.replace('die even veel is', 'met dezelfde uitkomst').replace('even veel', 'evenveel'); wat.append(k)      # #197: tekst Didactiek, Oefeningen past aan
    for f in st.get('foutHints') or []:
        if 'even veel' in (f.get('tekst') or ''): f['tekst'] = f['tekst'].replace('even veel', 'evenveel'); wat.append(f"fout-hint '{f['regel']}'")
    if wat: _log(punt=192, entry=f"{st['doel']} #{st['nrOrigineel']}", velden=wat, oud='even veel', nieuw='evenveel')
def fix192(it):
    if 'even veel' in (it['opgave'] or ''):
        oud = it['opgave']; it['opgave'] = oud.replace('even veel', 'evenveel')
        for k in ('claudeKaleSom',):
            if isinstance(it['extraVelden'].get(k), str): it['extraVelden'][k] = it['extraVelden'][k].replace('even veel', 'evenveel')
        _log(punt=192, claudeId=it['bron']['claudeId'], oud=oud, nieuw=it['opgave'])
# #194a E04 #5: het getal dat eraf gaat ligt binnen 10 van een honderdtal (022–026, 030); de opties volgen hun label
HANDIG194 = re.compile(r'^Hoe reken je (\d+) − (\d+) handig uit\?$')
def _som(e): return eval(e.replace('−', '-'))
def fix194a(it):
    if it['merge'].get('doel') != 'G6-GET-E04' or not (m := HANDIG194.match(it['opgave'] or '')): return
    a, b = int(m.group(1)), int(m.group(2)); H = int(re.match(r'\d+ − (\d+)', it['antwoord']).group(1))
    if abs(b - H) <= 10: return
    d = 1 + _h(f"{it['bron']['claudeId']}-194") % 9; plus = b < H; b2 = H - d if plus else H + d
    goed = f'{a} − {H} {"+" if plus else "−"} {d}'; ra = (a + 50) // 100 * 100; ra_d = abs(a - ra)
    ex = it['extraVelden']; lab = {x['fout']: x['denkfout'] for x in ex.get('claudeDenkfouten') or []}
    nieuw = {}
    for o in it['opties']:
        t = o['tekst']
        if t == it['antwoord']: nieuw[t] = goed; continue
        l = lab[t]
        if l == 'verkeerde-bewerking': nieuw[t] = f'{a} − {H} {"−" if plus else "+"} {d}'
        elif l == 'allebei-rond': nieuw[t] = f'{ra} − {H} {"+" if plus else "−"} {d}'
        elif l == 'verkeerd-stukje': nieuw[t] = t if t.endswith('+ 100') or t.endswith('− 100') else f'{a} − {H} {"+" if plus else "−"} {ra_d if ra_d not in (0, d) else d + 1}'
        else: raise AssertionError(('#194a: onbekend label', l, t))
    vals = list(nieuw.values()); assert len(set(vals)) == len(vals) and _som(goed) == a - b2 and all(_som(v) != a - b2 for v in vals if v != goed), ('#194a', nieuw)
    oud = (it['opgave'], it['antwoord'], [o['tekst'] for o in it['opties']])
    it['opgave'] = f'Hoe reken je {a} − {b2} handig uit?'; it['antwoord'] = goed
    for o in it['opties']: o['tekst'] = nieuw[o['tekst']]
    it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    for lst in (ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], it['foutHints'], ex.get('mergeFoutHints') or []):
        for f in lst:
            if f['fout'] in nieuw: f['fout'] = nieuw[f['fout']]
    if isinstance(ex.get('claudeKaleSom'), str): ex['claudeKaleSom'] = it['opgave']
    _log(punt=194, claudeId=it['bron']['claudeId'], oud=f'{oud[0]} => {oud[1]} | {oud[2]}', nieuw=f"{it['opgave']} => {goed} | {[o['tekst'] for o in it['opties']]}")
# #194b E08: het antwoord (gemiddelde) staat in hooguit 1 op de 3 items in het lijstje (001–005 krijgen een ander lijstje met hetzelfde gemiddelde)
GEM194 = re.compile(r'^(\d+ [a-zà-ÿ\']+ verzamelden [a-zà-ÿ\']+)\. ((?:\d+, )+\d+)\. (Hoeveel .+ gemiddeld .+\?)$')
def fix194b(it):
    if it['merge'].get('doel') != 'G6-GET-E08' or not (m := GEM194.match(it['opgave'] or '')): return
    xs = [int(x) for x in m.group(2).split(', ')]; g = int(it['antwoord']); assert sum(xs) == g * len(xs), ('#194b', it['opgave'])
    if g not in xs or it['bron']['claudeId'] not in GEM194_IDS: return
    ys = list(xs); oud_max = max(xs)
    while g in ys:      # het gemiddelde één omhoog, een ander getal één omlaag (of andersom); som en gemiddelde blijven gelijk
        i = ys.index(g); j = next(k for k in range(len(ys)) if ys[k] != g)
        if ys[j] - 1 != g: ys[i] += 1; ys[j] -= 1
        else: ys[i] -= 1; ys[j] += 1
    assert sum(ys) == sum(xs) and g not in ys and min(ys) > 0, ('#194b', xs, ys)
    oud = it['opgave']; it['opgave'] = f"{m.group(1)}. {', '.join(map(str, ys))}. {m.group(3)}"
    ex = it['extraVelden']; mx = {str(oud_max): str(max(ys))} if max(ys) != oud_max else {}
    for lst in (ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], it['foutHints'], ex.get('mergeFoutHints') or []):
        for f in lst:
            if f['fout'] in mx: f['fout'] = mx[f['fout']]
    ex['claudeUitleg'] = f"Tel alles op: {' + '.join(map(str, ys))} = {sum(ys)}.\nDeel door het aantal: {sum(ys)} : {len(ys)} = {g}."
    ex['claudeKaleSom'] = f"({' + '.join(map(str, ys))}) : {len(ys)}"
    _log(punt=194, claudeId=it['bron']['claudeId'], oud=oud, nieuw=it['opgave'])
GEM194_IDS = {'0e72f120-0662-4245-86be-239de5b86759', '5d04a29e-602a-4013-8b57-5154c52bd38f', '6c420ade-0553-4c84-b50d-04e83c03400d', '7e3c0c4d-32f5-479c-9303-d80aea3779e4', 'c6757da3-7439-4b5b-a1b6-9b121c1a4d59'}      # gevuld hieronder: de eerste vijf met het antwoord in de lijst (001–005); 008 en 010 houden het (2 van de 12)
# (bewerk_na) #194b-zin, #194c E06 #6, #194d M05 #1, #172 E03 #6/#8 en E09 #3
ZIN194 = re.compile(r'^(\d+ [a-zà-ÿ\']+ verzamelden [a-zà-ÿ\']+)\. ((?:\d+, )+)(\d+)\. (Hoeveel .+\?)$')
DING194 = ['kaartjes', 'stickers', 'knikkers', 'potloden']
DING172 = [('de kinderen in de klas', 'een fiets'), ('de kinderen in de klas', 'een huisdier'), ('de kinderen in de groep', 'een zwemdiploma'), ('de kinderen op het schoolplein', 'een pet')]
DUBBEL172 = {'cd8fbcc2-000e-463e-be41-c669c527fabb': 'een pizza', 'fa120a82-9db7-44a0-8fb9-094c429c730b': 'een taart',      # E03 036, 039
             '33c1fe38-0bb5-4e39-9ba7-f1d60c61eaa8': 'een reep chocola', '9f8defa2-c652-47bd-aed1-cb7a1b4a751f': 'een pizza'}       # E03 029, 034
KRIJG172 = ['knikkers', 'stickers', 'kaartjes', 'snoepjes']
def na194_172(it):
    d = it['merge'].get('doel'); o = it['opgave'] or ''; n = o; p = None
    if d == 'G6-GET-E08' and (m := ZIN194.match(o)):
        n = f"{m.group(1)}. Ze hadden er {m.group(2)[:-2]} en {m.group(3)}. {m.group(4)}"; p = 194
    elif d == 'G6-GET-E06' and 'Ze gaan eerlijk over' in o: n = o.replace('Ze gaan eerlijk over', 'Ze worden eerlijk verdeeld over'); p = 194
    elif d == 'G6-GET-M05' and (m := re.search(r'Welk aantal ([a-zà-ÿ\']+) kun je precies verdelen in groepjes van', o)):
        n = o.replace(f'Welk aantal {m.group(1)} ', f"Welk aantal {_k(it, DING194, 194)} "); p = 194
    elif d == 'G6-GET-E03' and (m := re.match(r'^(\d+/\d+) van (?:de|het|een) [a-zà-ÿ\']+ is evenveel als \?/(\d+)\. (Welk getal hoort op het vraagteken\?)$', o)):
        n = f'{m.group(1)} = ?/{m.group(2)}. {m.group(3)}'; p = 172
        if (r := DUBBEL172.get(it['bron']['claudeId'])):      # kaal zou deze vier een dubbel maken van 025/031/026/033: ze houden een passende context
            n = f"{m.group(1)} van {r} is evenveel als ?/{m.group(2)}. {m.group(3)}"
    elif d == 'G6-GET-E03' and (m := re.match(r'^(\d+/\d+) van de .+? heeft een .+?\. (Schrijf die breuk zo eenvoudig mogelijk\.)$', o)):
        w, x = _k(it, DING172, 172); n = f'{m.group(1)} van {w} heeft {x}. {m.group(2)}'; p = 172
    elif d == 'G6-GET-E09' and (m := re.match(r'^(?:Een|De) [a-zà-ÿ\']+ krijgt (\d+/\d+) van (\d+) [a-zà-ÿ\']+\. Hoeveel [a-zà-ÿ\']+ is dat\?$', o)):
        naam = _k(it, ['Noor', 'Sem', 'Mila', 'Daan', 'Lotte', 'Ayoub'], 172); x = _k(it, KRIJG172, '172b')
        n = f'{naam} krijgt {m.group(1)} van {m.group(2)} {x}. Hoeveel {x} is dat?'; p = 172
    if n != o:
        assert re.findall(r'\d+', n) == re.findall(r'\d+', o), ('#172/#194: getallen veranderd', o, n)
        it['opgave'] = n; it['merge'][f'opgaveVoor{p}'] = o; _log(punt=p, claudeId=it['bron']['claudeId'], oud=o, nieuw=n)
# #195 (Didactiek 21:25): M05 #3 sorteren: de app vergelijkt per vak als verzameling; 2 of meer verkeerd = 'andere fout'
BEOORDELING195 = {'soort': 'sorteren', 'perVakAlsVerzameling': True, 'volgordeBinnenVakTeltNiet': True,
                  'eenGetalVerkeerd': "sleutels 'fout = een deelbaar getal bij niet' en 'fout = een niet-deelbaar getal bij deelbaar' (#193); vangnet 'fout = één getal in het verkeerde vak' (#163)", 'vakkenOmgewisseld': "sleutel 'fout = vakken omgewisseld'",
                  'tweeOfMeerVerkeerd': 'andere fout (algemeneFoutHint)', 'bron': 'G6 merge-fixlijst #195 (Didactiek 21:25, besluit Dave 21:25); app-eis in README'}
def fix195(it):
    if it['merge'].get('doel') == 'G6-GET-M05' and SORT163.match(it['opgave'] or ''): it['beoordeling'] = json.loads(json.dumps(BEOORDELING195))

# ======================= ronde 5: Didactiek batch 3 (21:42, #173/#180/#183/#185/#186/#189/#201), recheck 2b (21:42, #196–#199), Oefeningen batch 4 (21:43, #176–#179)
# #173 M04 #3: 'het deeltal'/'de deler' zijn verdedigbaar goed (1/8 = 1 : 8) → 'de uitkomst'. Teller en noemer verwisseld blijft de hoofdsleutel.
HEET173 = re.compile(r'^Hoe heet de (\d+) in (\d+)/(\d+)\?$')
R173 = ('de uitkomst', 'uitkomst gekozen', 'De uitkomst krijg je pas als je iets uitrekent. Dit getal staat in de breuk zelf. Kijk waar het staat: boven of onder de streep? Hoe heet het getal op die plek?')
def fix173(it):
    if it['merge'].get('doel') != 'G6-GET-M04' or not HEET173.match(it['opgave'] or ''): return
    goed = it['antwoord']; assert goed in ('de teller', 'de noemer'), ('#173', it['opgave'], goed)
    wissel = 'de noemer' if goed == 'de teller' else 'de teller'
    oud = [o['tekst'] for o in it['opties']]
    it['opties'] = [{'letter': l, 'tekst': t} for l, t in zip('ABC', (goed, wissel, 'de uitkomst'))]      # volgorde van Didactiek (batch 3, #173)
    ex = it['extraVelden']
    for dk in ex.get('claudeDenkfouten') or []:
        if dk['fout'] in ('het deeltal', 'de deler'): dk['foutClaude'] = dk['fout']; dk['fout'] = 'de uitkomst'; dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = 'uitkomst-gekozen'
        elif dk['fout'] == wissel and dk['denkfout'] != 'teller-en-noemer-verwisseld': dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = 'teller-en-noemer-verwisseld'
    for fh in ex.get('claudeFoutHints') or []:
        if fh.get('fout') in ('het deeltal', 'de deler'): fh['foutClaude'] = fh['fout']; fh['fout'] = 'de uitkomst'; fh['uitleg'] = R173[2]
    _log(punt=173, claudeId=it['bron']['claudeId'], opgave=it['opgave'], oud=oud, nieuw=[o['tekst'] for o in it['opties']])
def _e173(st):
    fh = st['foutHints']; weg = [f['regel'] for f in fh if f['regel'] in ('het deeltal', 'de deler')]
    st['foutHints'] = fh = [f for f in fh if f['regel'] not in ('het deeltal', 'de deler')]      # die opties bestaan niet meer (Didactiek: 'de hints deeltal/deler gekozen vervallen')
    nieuw = []
    if not any(f['regel'] == R173[0] for f in fh):
        i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
        fh[i:i] = [{'regel': R173[0], 'soort': R173[1], 'tekst': R173[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #173, Didactiek batch 3 21:42); tekst = voorstel Didactiek, Oefeningen schrijft de definitieve'}]; nieuw = [R173[0]]
    if weg or nieuw: _log(punt=173, entry=f"{st['doel']} #{st['nrOrigineel']}", weg=weg, ingevoegd=nieuw)

# #180 E03 #2/#3: alleen vergelijkingen op G6-niveau (zelfde teller/noemer, noemer een veelvoud, kgv ≤ 24, of met de helft); de rest naar G7 (regels_g6 → park-G7, G7-GET-05)
KIES180 = re.compile(r'^Welke breuk is het (grootst|kleinst)\? Kies uit (.+)\.$')
def fix180(it):
    """Bewaker in de build: wat in G6 blijft, moet per vergelijking met het antwoord op G6-niveau te beslissen zijn (regels_g6.niveau180)."""
    if it['merge'].get('doel') != 'G6-GET-E03' or not (m := KIES180.match(it['opgave'] or '')): return
    import regels_g6 as R6
    br = re.findall(r'\d+/\d+', m.group(2)); ok, why = R6.niveau180(br, it['antwoord'])
    assert ok, ('#180: vergelijking boven G6-niveau in G6-GET-E03', it['bron']['claudeId'], it['opgave'], why)
    assert max(int(b.split('/')[1]) for b in br) <= 20, ('#221: noemer boven 20 in G6-GET-E03 grootst/kleinst', it['bron']['claudeId'], it['opgave'])

# #183 M04 #2: 'Er blijft ook nog een stuk over.' klopt niet bij 2–5 stukken
def fix183(it):
    o = it['opgave'] or ''
    if it['merge'].get('doel') == 'G6-GET-M04' and 'Er blijft ook nog een stuk over.' in o:
        m = re.search(r"\d+/\d+ (pizza|taart)\b", o); ding = {'pizza': "pizza's", 'taart': 'taarten'}[m.group(1)] if m else "pizza's"
        it['opgave'] = o.replace('Er blijft ook nog een stuk over.', f'Niet alle stukken passen in hele {ding}.'); _log(punt=183, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'])

# #185 M04 #4: «Welk deel van de [pizza] is dat?» en 'snijden' in plaats van 'delen' (na #171)
DEEL185 = re.compile(r"\bdelen een ([a-zà-ÿ' ]+?) in (\d+) gelijke stukken\.")
def fix185(it):
    o = it['opgave'] or ''
    if it['merge'].get('doel') != 'G6-GET-M04' or not (m := DEEL185.search(o)) or 'Welk deel is dat?' not in o: return
    n = DEEL185.sub(lambda x: f'snijden een {x.group(1)} in {x.group(2)} gelijke stukken.', o).replace('Welk deel is dat?', f'Welk deel van de {m.group(1)} is dat?')
    it['opgave'] = n; _log(punt=185, claudeId=it['bron']['claudeId'], oud=o, nieuw=n)

# #186 E03 #7: motorregel 'tellen vanaf 1 in plaats van 0' (één stuk te kort), vlag vereistTekening (pas live met een getekende lijn)
R186 = ('fout = tellen vanaf 1 in plaats van 0', 'tellen vanaf 1 in plaats van 0', 'Bijna! Je bent één stuk te kort. Tel vanaf nul de stukken nog eens.')
def fix186(it):
    if it['merge'].get('doel') != 'G6-GET-E03' or not LIJN169.match(it['opgave'] or ''): return
    it['vereistTekening'] = True
    _log(punt=186, claudeId=it['bron']['claudeId'], vereistTekening=True)
def _e186(st):
    fh = st['foutHints']
    if any(f['regel'] == R186[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f['regel'] == R169[0]), next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh)))
    fh[i:i] = [{'regel': R186[0], 'soort': R186[1], 'tekst': R186[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #186, Didactiek batch 3 21:42); tekst = voorstel Didactiek, Oefeningen schrijft de definitieve'}]
    _log(punt=186, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R186[0]], voor=R169[0])

# #189 E09 #3 602: 4/8 van 32 → 3/8 van 32 (antwoord 12; 'wat overblijft' was het antwoord). Zelfde id.
ID189 = '3c47ff4a-88f9-4426-b8de-572f4b7e70a6'
def fix189(it):
    if it['bron']['claudeId'] != ID189: return
    o = it['opgave']; assert '4/8 van 32' in o and it['antwoord'] == '16', ('#189: 602 is veranderd', o, it['antwoord'])
    it['opgave'] = o.replace('4/8 van 32', '3/8 van 32'); it['antwoord'] = '12'
    ex = it['extraVelden']; ex['claudeKaleSom'] = '3/8 × 32'; ex['claudeUitleg'] = '3/8 × 32 = 3 × 32 : 8.\n32 : 8 = 4, keer 3 = 12.'
    ex['claudeDenkfouten'] = [{'fout': '4', 'denkfout': 'niet-verdeeld', 'denkfoutClaude': 'deel-vergeten-bij-splitsen'}, {'fout': '96', 'denkfout': 'niet-verdeeld', 'denkfoutClaude': 'deel-vergeten-bij-splitsen'}]
    ex['claudeFoutHints'] = [{'stap': None, 'fout': '4', 'uitleg': 'Dat is 1/8. Vermenigvuldig nog met 3.'}, {'stap': None, 'fout': '96', 'uitleg': 'Je bent het delen door de noemer vergeten.'}]
    _log(punt=189, claudeId=ID189, oud=o, nieuw=it['opgave'], antwoord='16 → 12')

# #201 E03 #5: een hele zin in plaats van «4/20 van de wortels.» (bewerk_na)
ZIN201 = {'wortels': 'van de wortels in de zak is al op', 'knopen': 'van de knopen in het doosje is blauw', 'stickers': 'van de stickers in het album is al geplakt',
          'eieren': 'van de eieren in de doos is al gebruikt', 'sterren': 'van de sterren op het blad is al gekleurd', 'pionnen': 'van de pionnen op het bord is wit',
          'noten': 'van de noten in de schaal is al op', 'ballen': 'van de ballen in de bak is geel', 'blaadjes': 'van de blaadjes aan de plant is al geel',
          'veren': 'van de knikkers in de zak is rood', 'tanden': 'van de tegels op het plein is grijs'}      # veren/tanden: geen passende context (#164/#172)
LOS201 = re.compile(r'^(\d+/\d+) van de ([a-zà-ÿ]+)\. (Schrijf (?:deze|die) breuk zo eenvoudig mogelijk\.)$')
def na201(it):
    o = it['opgave'] or ''
    if it['merge'].get('doel') == 'G6-GET-E03' and (m := LOS201.match(o)):
        z = ZIN201.get(m.group(2)); assert z, ('#201: geen zin voor', m.group(2))
        it['opgave'] = f'{m.group(1)} {z}. {m.group(3).replace("deze breuk", "die breuk")}'; it['merge']['zin201'] = True; _log(punt=201, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'])

# #196 E06 #1: bij getal2 = 19 is getal1 × cijfersom = getal1 × 10, het eerste stuk van de goede route → 'stuk vergeten' (de motor slaat #190 dan over)
def is196(b): return b >= 10 and sum(int(x) for x in str(b)) == b // 10 * 10
def fix196(it):
    if it['merge'].get('doel') != 'G6-GET-E06' or not (m := KEER190.match(it['opgave'] or '')): return
    a, b = int(m.group(1)), int(m.group(2))
    if not is196(b): return
    v = str(a * (b // 10 * 10)); dks = it['extraVelden'].setdefault('claudeDenkfouten', [])
    d = next((x for x in dks if x['fout'].replace('.', '') == v), None)
    if d is None:
        dks.append({'fout': v, 'denkfout': 'deel-vergeten-bij-splitsen', 'door': 'Overzicht #196 (Didactiek 21:42): getal1 × de tientallen van getal2'})
        it['extraVelden'].setdefault('claudeFoutHints', []).append({'stap': None, 'fout': v, 'uitleg': f'Je bent een stuk vergeten. Doe ook {a} × {b % 10} en tel het erbij.', 'door': 'Overzicht #196'}); hoe = 'erbij'
    elif d['denkfout'] == LAB190: d['denkfout'] = d.pop('denkfoutClaude', 'deel-vergeten-bij-splitsen'); hoe = 'terug naar stuk vergeten'
    else: hoe = 'had al stuk vergeten'
    _log(punt=196, claudeId=it['bron']['claudeId'], opgave=it['opgave'], sleutel=v, hoe=hoe)

# #198 E06 #3/#7: 'eenheden niet keer gedaan' (30 × 27 → 600 + 7 = 607; 15 × 485 → 4850 + 5)
R198 = ('fout = getal1 × tientallen(getal2) + eenheden(getal2)', 'eenheden niet keer gedaan',
        'Je hebt de eenheden er alleen bij gezet. Doe ook de eenheden keer het andere getal, en tel daarna alle stukken op.')
LAB198 = 'eenheden-niet-keer-gedaan'
KEER198 = re.compile(r"^In (?:de|het) [a-zà-ÿ]+ staan (\d+) (?:rijen|kisten|dozen) met (?:elk )?(\d+) [a-zà-ÿ']+\. Hoeveel [a-zà-ÿ']+ zijn dat\?$")      # E06 #3/#7 (vóór #164)
def waarden198(g1, g2):      # #210: niet als antwoord − waarde een deelproduct is (dan blijft het 'stuk vergeten')
    return {v for v in (y * (x // 10 * 10) + x % 10 for x, y in ((g2, g1), (g1, g2)) if 10 <= x < 100 and x % 10) if g1 * g2 - v not in _FR.deelproducten(g1, g2)}
def fix198(it):
    if it['merge'].get('doel') != 'G6-GET-E06' or not (m := KEER198.match(it['opgave'] or '')): return
    ns = [int(m.group(1)), int(m.group(2))]
    vs = {str(v) for v in waarden198(ns[0], ns[1])}; n = 0
    for dk in it['extraVelden'].get('claudeDenkfouten') or []:
        if dk['fout'].replace('.', '') in vs and dk['denkfout'] == 'deel-vergeten-bij-splitsen': dk['denkfoutClaude'] = dk['denkfout']; dk['denkfout'] = LAB198; n += 1
    if n: _log(punt=198, claudeId=it['bron']['claudeId'], opgave=it['opgave'], sleutels=sorted(vs))
def _e198(st):
    fh = st['foutHints']
    if any(f['regel'] == R198[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f.get('claudeDenkfout') == 'deel-vergeten-bij-splitsen'), next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh)))
    fh[i:i] = [{'regel': R198[0], 'soort': R198[1], 'tekst': R198[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #198, Didactiek 21:42); tekst = voorstel Didactiek (#198b), Oefeningen schrijft de definitieve'}]
    _log(punt=198, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R198[0]], voor='Claudes sleutel: deel-vergeten-bij-splitsen')

# #176 MEET-E03 #1/#3/#4: omtrek in plaats van oppervlakte en oppervlakte verdubbeld, vóór de Claude-regel (teksten Oefeningen, fixlijst 21:43)
R176 = [('fout = (getal1 + getal2) × 2', 'omtrek in plaats van oppervlakte', 'Dat is de omtrek: de lengte van de rand eromheen. De oppervlakte is wat erbinnen zit: reken de lengte keer de breedte.'),
        ('fout = antwoord × 2', 'oppervlakte verdubbeld', 'Je hebt de oppervlakte verdubbeld. De lengte keer de breedte is al de hele oppervlakte.')]
def _e176(st):
    fh = st['foutHints']
    if any(f['regel'] == R176[0][0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f.get('claudeDenkfout') == 'omtrek-oppervlakte-verwisseld'), next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh)))
    fh[i:i] = [{'regel': r, 'soort': s, 'tekst': t, 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #176, Oefeningen 21:43; tekst Oefeningen)'} for r, s, t in R176]
    _log(punt=176, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[r for r, _, _ in R176], voor='Claudes sleutel: omtrek-oppervlakte-verwisseld')

# #178 MEET-E01 #6: 'een andere 5,2 kg' → 'een ander' (het pakket); MEET-E03 #3: geen vlot bij de vallei. #177/#179: info (log).
INFO177 = [(204, 'info van Oefeningen (21:59), geen actie'), (177, '× 2, : 2 en × 3 bij omrekenen krijgen geen eigen regel (Overzicht 21:31); die sleutels vallen op de algemene tekst per somtype'),
           (179, 'MEET-E01 #7 (strook, 2 meerkeuze-items): sleutels hangen aan het label, per item nagerekend; geen letterlijke optieregels')]
def fix178(it):
    global INFO177
    if INFO177:
        for p, t in INFO177: _log(punt=p, info=t)
        INFO177 = []
    o = it['opgave'] or ''; n = o; d = it['merge'].get('doel')
    if d == 'G6-MEET-E01': n = re.sub(r'^(Een (?:pakket|boek|blik|zakje|kistje|pak)\b.*?, een) andere (?=\d)', r'\1 ander ', n)
    if d == 'G6-MEET-E03': n = n.replace('Bij de vallei ligt een vlot van', 'Bij de schuur ligt een tuin van')
    if n != o: it['opgave'] = n; _log(punt=178, claudeId=it['bron']['claudeId'], oud=o, nieuw=n)

# #203 (besluit Oefeningen 21:59) E03 #7: twee regels 'een stuk te ver' (t + 1) en 'een stuk te kort' (t − 1); 'tellen vanaf 1' (#186) en 'één stuk ernaast' (#169) vallen weg
def _e203(st):
    fh = st['foutHints']; weg = [f['regel'] for f in fh if f['regel'] in (R169[0], R186[0])]
    st['foutHints'] = fh = [f for f in fh if f['regel'] not in (R169[0], R186[0])]
    nieuw = [x for x in R203 if not any(f['regel'] == x[0] for f in fh)]
    i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
    fh[i:i] = [{'regel': r, 'soort': s_, 'tekst': t, 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #203, besluit Oefeningen 21:59); tekst = voorstel Didactiek (#186), Oefeningen schrijft de definitieve'} for r, s_, t in nieuw]
    if weg or nieuw: _log(punt=203, entry=f"{st['doel']} #{st['nrOrigineel']}", weg=weg, ingevoegd=[r for r, _, _ in nieuw])
# #202 (Oefeningen 21:59) E03 #4: een even grote breuk met een andere noemer, alleen waar de vraag een noemer noemt (past bij #170: daar is de vorm gevraagd)
R202 = ('fout = even grote breuk met een andere noemer', 'even groot, andere noemer',
        'Die breuk is even groot, maar hij heeft niet de noemer uit de vraag. Hoeveel keer zo groot is die noemer? Doe de teller ook zoveel keer.')
def _e202(st):
    fh = st['foutHints']
    if any(f['regel'] == R202[0] for f in fh): return
    i = next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
    fh[i:i] = [{'regel': R202[0], 'soort': R202[1], 'tekst': R202[2], 'bron': 'nieuw', 'door': 'Overzicht (G6-fixlijst #202, Oefeningen 21:59; tekst Oefeningen)'}]
    _log(punt=202, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[R202[0]], voor='andere fout')

# ------------------------------------------------------------------ ronde 7: Didactiek recheck 2c, batch 4 (meten) en recheck 3b (22:13–22:14)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('fout_regels_g6', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fout_regels.py'))
_FR = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_FR)      # de G6-motor (niet een fout_regels uit g5_basis/ op sys.path)
DOOR7 = 'Overzicht (G6-fixlijst ronde 7, Didactiek 22:13/22:14)'
def _ph(soort): return f'[TEKST NODIG (Oefeningen): {soort}]'
def _voor(fh, pred, default_andere=True):
    i = next((k for k, f in enumerate(fh) if pred(f)), None)
    return i if i is not None else next((k for k, f in enumerate(fh) if f['regel'] == 'andere fout'), len(fh))
# #215 (zacht, besluit Dave): 'anders omgerekend' = het aantal nullen als factor; tekst = voorstel Didactiek (per item), Oefeningen schrijft de definitieve
R215 = [('fout = getal1 keer het aantal nullen van de factor', 'aantal nullen als factor (keer)',
         'Je hebt keer [nullen] gedaan. [Factor] heeft [nullen] nullen, maar je doet keer [factor]: schrijf er [nullen] nullen achter.'),
        ('fout = getal1 gedeeld door het aantal nullen van de factor', 'aantal nullen als factor (delen)',
         'Je hebt door [nullen] gedeeld. [Factor] heeft [nullen] nullen, maar je deelt door [factor]: haal er [nullen] nullen af.')]
def _e215(st):
    fh = st['foutHints']
    if (st['doel'], st.get('nrOrigineel')) == ('G6-MEET-E01', 7): return      # #263: niet in E01 #7
    if not any(f.get('claudeDenkfout') == 'eenheid-verkeerd-omgerekend' for f in fh) or any(f['regel'] == R215[0][0] for f in fh): return
    i = _voor(fh, lambda f: f.get('claudeDenkfout') == 'eenheid-verkeerd-omgerekend')
    fh[i:i] = [{'regel': r, 'soort': s_, 'tekst': t, 'bron': 'nieuw', 'door': f'{DOOR7} #215; tekst = voorstel Didactiek, Oefeningen schrijft de definitieve'} for r, s_, t in R215]
    _log(punt=215, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=[r for r, _, _ in R215], voor='Claudes sleutel: eenheid-verkeerd-omgerekend')
# #214 (verplicht): E03 #2 'fout = getal2' (de zijde uit de vraag) vóór ± 1 — Oefeningen heeft hem in batch4 (22:18); anders een plaatshouder
# #216 (zacht): ± 1 krijgt 'Bijna!' alleen bij een antwoord van 10 of meer (motor: '(antwoord vanaf 10)' / '(antwoord onder 10)')
def _e214_216(st):
    fh = st['foutHints']
    if not any(f['regel'] == 'fout = getal2' for f in fh):
        i = _voor(fh, lambda f: f['regel'] in ('fout = antwoord + 1', 'fout = antwoord − 1'))
        fh[i:i] = [{'regel': 'fout = getal2', 'soort': 'zijde uit de vraag', 'tekst': _ph('zijde uit de vraag'), 'bron': 'nieuw', 'door': f'{DOOR7} #214 (plaatshouder)'}]
        _log(punt=214, entry=f"{st['doel']} #{st['nrOrigineel']}", ingevoegd=['fout = getal2'], tekst='plaatshouder')
    else:
        # #229a (Oefeningen 4b): robuust als de entry ± 1 al gesplitst heeft ('… (antwoord vanaf 10)'): vergelijk op de basisregel
        k = next(k for k, f in enumerate(fh) if f['regel'] == 'fout = getal2')
        js = [k_ for k_, f in enumerate(fh) if _basisregel(f['regel']) in ('fout = antwoord + 1', 'fout = antwoord − 1')]
        assert js, ('#214/#229a: geen regel ± 1 in de entry', st['doel'])
        assert k < min(js), ('#214: zijde uit de vraag staat niet vóór ± 1', st['doel'])
        _log(punt=214, entry=f"{st['doel']} #{st['nrOrigineel']}", info='Oefeningen batch4 (22:18) heeft de regel al vóór ± 1, met tekst')
    nieuw = []
    for f in fh:
        if f['regel'] in ('fout = antwoord + 1', 'fout = antwoord − 1'):      # (al gesplitst: '… (antwoord vanaf 10)' blijft zoals hij is, #229a)
            t = re.sub(r'^Bijna! ', '', f['tekst'])
            nieuw += [dict(f, regel=f"{f['regel']} (antwoord vanaf 10)", tekst=f'Bijna! {t}', door=f'{DOOR7} #216; tekst Oefeningen'),
                      dict(f, regel=f"{f['regel']} (antwoord onder 10)", tekst=t, door=f'{DOOR7} #216; tekst Oefeningen')]
        else: nieuw.append(f)
    if len(nieuw) != len(fh): st['foutHints'] = nieuw; _log(punt=216, entry=f"{st['doel']} #{st['nrOrigineel']}", gesplitst=['fout = antwoord + 1', 'fout = antwoord − 1'])
# #205 (verplicht): E09 #2 'één stuk' vóór 'getal uit de vraag'; E09 #3 een eigen regel 'één stuk' (plaatshouder) vóór 'getal uit de vraag'
R205 = ('fout = één stuk (het aantal : de noemer)', 'één stuk')
def _e205(st):
    fh = st['foutHints']; nr = st.get('nrOrigineel')
    g = next((k for k, f in enumerate(fh) if f['regel'] == 'fout = een getal uit de vraag'), None)
    if nr == 2:
        k = next((k for k, f in enumerate(fh) if f.get('claudeDenkfout') == 'deel-vergeten-bij-splitsen'), None)
        if g is not None and k is not None and k > g:
            f = fh.pop(k); fh.insert(g, f); _log(punt=205, entry=f"{st['doel']} #2", verplaatst=f['regel'], voor='fout = een getal uit de vraag')
        # niet elk 'één stuk' heeft Claudes label: ook de motorregel, met de tekst van Oefeningen bij 'één stuk' in deze entry, vóór 'getal uit de vraag'
        if not any(f['regel'] == R205[0] for f in fh):
            g = next((k for k, f in enumerate(fh) if f['regel'] == 'fout = een getal uit de vraag'), len(fh))
            tk = next((f['tekst'] for f in fh if f.get('claudeDenkfout') == 'deel-vergeten-bij-splitsen'), None) or _ph('één stuk')
            fh.insert(g, {'regel': R205[0], 'soort': R205[1], 'tekst': tk, 'bron': 'nieuw', 'door': f'{DOOR7} #205; tekst Oefeningen (één stuk, E09 #2)'})
            _log(punt=205, entry=f"{st['doel']} #2", ingevoegd=[R205[0]], voor='fout = een getal uit de vraag', tekst='Oefeningen (één stuk)')
    elif nr == 3 and not any(f['regel'] == R205[0] for f in fh):
        i = g if g is not None else _voor(fh, lambda f: False)
        fh.insert(i, {'regel': R205[0], 'soort': R205[1], 'tekst': _ph('één stuk'), 'bron': 'nieuw', 'door': f'{DOOR7} #205 (plaatshouder; Oefeningen schrijft de tekst)'})
        _log(punt=205, entry=f"{st['doel']} #3", ingevoegd=[R205[0]], voor='fout = een getal uit de vraag', tekst='plaatshouder')
# #206 (verplicht): E03 #6 de factor vóór 'teller overgenomen' en 'getal uit de vraag'
R206 = ('fout = de factor (nieuwe noemer : oude noemer)', 'de factor')
def _e206(st):
    fh = st['foutHints']
    if any(f['regel'] == R206[0] for f in fh): return
    i = _voor(fh, lambda f: f['regel'] in ('fout = getal1', 'fout = een getal uit de vraag'))
    fh.insert(i, {'regel': R206[0], 'soort': R206[1], 'tekst': _ph('de factor'), 'bron': 'nieuw', 'door': f'{DOOR7} #206 (plaatshouder; Oefeningen schrijft de tekst)'})
    _log(punt=206, entry=f"{st['doel']} #6", ingevoegd=[R206[0]], voor='fout = getal1 (teller overgenomen)', tekst='plaatshouder')
# #207 (verplicht): M04 #2 de rest en 'steeds een hele pizza eraf' (j ≥ 2) vóór ± 1
R207 = [('fout = de rest van getal1 : getal2', 'de rest'), ('fout = getal1 − j × getal2 (j ≥ 2)', 'steeds een hele eraf')]
def _e207(st):
    fh = st['foutHints']
    if any(f['regel'] == R207[0][0] for f in fh): return
    i = _voor(fh, lambda f: f['regel'] in ('fout = antwoord + 1', 'fout = antwoord − 1'))
    fh[i:i] = [{'regel': r, 'soort': s_, 'tekst': _ph(s_), 'bron': 'nieuw', 'door': f'{DOOR7} #207 (plaatshouder; Oefeningen schrijft de tekst)'} for r, s_ in R207]
    _log(punt=207, entry=f"{st['doel']} #2", ingevoegd=[r for r, _ in R207], voor='fout = antwoord ± 1', tekst='plaatshouder')
# #209 (Oefeningen; nodig na #221: nu ook items met dezelfde teller of noemer): ouderzin E03 grootst/kleinst
def _e209(st):
    w = 'grootste' if st.get('nrOrigineel') == 2 else 'kleinste'; z = f'Je kind zoekt de {w} van drie breuken.'
    if st.get('ouderzin') != z: _log(punt=209, entry=f"{st['doel']} #{st['nrOrigineel']}", oud=st.get('ouderzin'), nieuw=z); st['ouderzin'] = z

def pas_entries_ronde7(st):
    k = (st['doel'], st.get('nrOrigineel'))
    if st['doel'] in ('G6-MEET-E01', 'G6-MEET-E04', 'G6-MEET-E05'): _e215(st)
    if k == ('G6-MEET-E03', 2): _e214_216(st)
    if k in (('G6-GET-E09', 2), ('G6-GET-E09', 3)): _e205(st)
    if k == ('G6-GET-E03', 6): _e206(st)
    if k == ('G6-GET-M04', 2): _e207(st)
    if k in (('G6-GET-E03', 2), ('G6-GET-E03', 3)): _e209(st)

# ---- items
# #221 (verplicht): E03 grootst/kleinst. 814: 1/22 → 1/12 (noemer ≤ 20). Aanvullen met een opbouw (zelfde noemer → zelfde teller → veelvoud → ½),
# het antwoord op elke plek. Bron: #180-items die anders naar G7 gingen (zelfde claudeId; vaste keuze per hash), vóór de indeling (voor_classify221).
ID814 = '6568bf92-8f23-447f-86d8-fe0547d5b3e6'
NIEUW221 = {'kleinst': [('zelfde noemer', 1, '2/5, 4/5 of 1/5', '1/5'), ('zelfde noemer', 1, '3/7, 5/7 of 6/7', '3/7'), ('zelfde noemer', 1, '5/8, 3/8 of 7/8', '3/8'),
                        ('zelfde noemer', 1, '4/9, 7/9 of 2/9', '2/9'), ('zelfde noemer', 1, '3/10, 7/10 of 9/10', '3/10'), ('zelfde noemer', 1, '8/11, 5/11 of 9/11', '5/11'),
                        ('zelfde teller', 2, '2/3, 2/9 of 2/5', '2/9'), ('zelfde teller', 2, '3/10, 3/4 of 3/7', '3/10'), ('zelfde teller', 2, '1/4, 1/6 of 1/12', '1/12'),
                        ('zelfde teller', 2, '5/6, 5/9 of 5/7', '5/9'), ('veelvoud', 2, '3/4, 5/8 of 7/8', '5/8'), ('veelvoud', 2, '2/3, 5/6 of 7/12', '7/12'),
                        ('veelvoud', 2, '2/5, 1/4 of 3/10', '1/4'), ('veelvoud', 2, '9/16, 5/8 of 3/4', '9/16'), ('helft', 3, '3/7, 5/9 of 7/12', '3/7'),
                        ('helft', 3, '8/13, 4/11 of 13/20', '4/11'), ('helft', 3, '5/8, 7/11 of 2/9', '2/9'), ('helft', 3, '9/14, 5/17 of 12/19', '5/17')],
            'grootst': [('zelfde noemer', 1, '3/5, 4/5 of 2/5', '4/5'), ('zelfde noemer', 1, '7/9, 4/9 of 5/9', '7/9'), ('zelfde noemer', 1, '3/8, 1/8 of 7/8', '7/8'),
                        ('zelfde noemer', 1, '7/12, 5/12 of 11/12', '11/12'), ('zelfde teller', 2, '2/7, 2/3 of 2/9', '2/3'), ('zelfde teller', 2, '4/5, 4/9 of 4/7', '4/5')]}
RAW221 = re.compile(r'^Welke breuk is het (grootst|kleinst): (.+)\?$')
_KEUS221 = None
def _keus221(V):
    """vaste keuze: per soort de #180-items met de kleinste hash (claudeId), zoveel als NIEUW221 vraagt."""
    import regels_g6 as R6
    out = {}
    for w in ('kleinst', 'grootst'):
        kand = sorted((q for q in V if q['doel'] == 'B5' and (m := RAW221.match(q['vraag'])) and m.group(1) == w and q['id'] != ID814
                       and not R6.niveau180(re.findall(r'\d+/\d+', m.group(2)), str(q['antwoord']).strip())[0]), key=lambda q: _h(f"{q['id']}-221"))
        for q, nieuw in zip(kand, NIEUW221[w]): out[q['id']] = (w, nieuw)
        assert len(kand) >= len(NIEUW221[w]), ('#221: te weinig #180-items', w)
    return out
def voor_classify221(q, V):
    """vóór de indeling (build_g6): 814 krijgt 1/12 in plaats van 1/22; de gekozen #180-items krijgen een G6-vergelijking. Geeft een kopie (of q zelf)."""
    global _KEUS221
    if _KEUS221 is None: _KEUS221 = _keus221(V)
    from fractions import Fraction as Fr
    if q['id'] == ID814:
        assert q['vraag'] == 'Welke breuk is het grootst: 1/22, 1/2 of 2/5?' and q['antwoord'] == '1/2', ('#221: 814 is veranderd', q['vraag'])
        n = dict(q, vraag='Welke breuk is het grootst: 1/12, 1/2 of 2/5?', fouten=[dict(f, antwoord='1/12' if f['antwoord'] == '1/22' else f['antwoord']) for f in q['fouten']])
        _log(punt=221, claudeId=q['id'], oud=q['vraag'], nieuw=n['vraag'], waarom='noemer 22 > 20 (Didactiek 3b V-#221a)'); return n
    if q['id'] not in _KEUS221: return q
    w, (soort, niv, lijst, ant) = _KEUS221[q['id']]
    br = re.findall(r'\d+/\d+', lijst); val = [Fr(b) for b in br]
    best = (max if w == 'grootst' else min)(val)
    assert len(br) == 3 and len(set(val)) == 3 and br[val.index(best)] == ant and max(int(b.split('/')[1]) for b in br) <= 20, ('#221 lijst', lijst, ant)
    dk = q['fouten'][0]['denkfout'] if q['fouten'] else 'grotere-noemer-is-groter'; hint = q['fouten'][0]['hint'] if q['fouten'] else ''
    n = dict(q, vraag=f'Welke breuk is het {w}: {lijst}?', antwoord=ant, niveau=niv,
             fouten=[{'antwoord': b, 'hint': hint, 'denkfout': dk} for b in br if b != ant])
    _log(punt=221, claudeId=q['id'], oud=q['vraag'], nieuw=n['vraag'], antwoord=f"{q['antwoord']} → {ant}", soort=soort, niveau=niv)
    return n

# #211 (verplicht): MEET-E03 #1 285 (6 × 3: omtrek = oppervlakte = 18) → 7 × 3; bewaker 2 × (l + b) ≠ l × b in E03 #1/#3/#4
ID285 = None      # op opgave: 'Een rechthoek is 6 cm lang en 3 cm breed.'
RECHT211 = re.compile(r'(\d+) (cm|meter) lang en (\d+) (?:cm|meter) breed')
def fix211(it):
    if it['merge'].get('doel') != 'G6-MEET-E03': return
    o = it['opgave'] or ''
    if o.startswith('Een rechthoek is 6 cm lang en 3 cm breed.') and it['antwoord'] == '18':
        ex = it['extraVelden']; it['opgave'] = o.replace('6 cm lang', '7 cm lang'); it['antwoord'] = '21'
        for k in ('claudeKaleSom', 'claudeUitleg'):
            if ex.get(k): ex[k] = ex[k].replace('6 × 3', '7 × 3').replace('6 x 3', '7 x 3').replace('= 18', '= 21')
        kaart = {'24': '28', '12': '14'}      # Claudes 'een-ernaast' = antwoord ± l of ± b: 18 + 6 → 21 + 7, 18 − 6 → 21 − 7
        for lst in (ex.get('claudeDenkfouten') or [], ex.get('claudeFoutHints') or []):
            for f in lst: f['fout'] = kaart.get(f['fout'], f['fout'])
        _log(punt=211, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'], antwoord='18 → 21', sleutels=kaart)
    if (m := RECHT211.search(it['opgave'] or '')) and re.fullmatch(r'\d+', str(it['antwoord'])) and int(it['antwoord']) == int(m.group(1)) * int(m.group(3)):
        l, b = int(m.group(1)), int(m.group(3))
        assert 2 * (l + b) != l * b, ('#211: omtrek = oppervlakte (een foute route geeft het goede antwoord)', it['bron']['claudeId'], it['opgave'])

# #218 (zacht): E01 #7 «Hoeveel meter is dat samen?»; E01 #6 een Claude-sleutel met een nul aan het eind ('3,80') ook zonder ('3,8');
# E03 #1 (253 × één kaal sjabloon) meer contexten (alleen cm: H1 noemt cm²), ná het somtype (bewerk_na), vaste keuze per hash
DING218 = [None, None, None, 'Een foto', 'Een tegel', 'Een kaart', 'Een sticker', 'Een placemat', 'Een spelbord', 'Een etiket', 'Een vlaggetje']
def fix218(it):
    d = it['merge'].get('doel'); o = it['opgave'] or ''; n = o
    if d == 'G6-MEET-E01':
        n = re.sub(r' Hoeveel meter is die (?:hele )?strook\?$', ' Hoeveel meter is dat samen?', n)
        if re.match(r'Een (?:pakket|boek|blik|zakje|kistje|pak)\b.*weegt [\d,]+ kg', o):
            ex = it['extraVelden']
            for naam in ('claudeFoutHints', 'claudeDenkfouten'):
                lst = ex.get(naam) or []
                for f in list(lst):
                    if re.fullmatch(r'\d+,\d*0', f['fout']) and (k := _kg(f['fout'])) != f['fout'] and not any(g['fout'] == k for g in lst):
                        lst.append(dict(f, fout=k))
                        if naam == 'claudeFoutHints': _log(punt=218, claudeId=it['bron']['claudeId'], sleutel=f['fout'], ookSleutel=k)
    if n != o: it['opgave'] = n; _log(punt=218, claudeId=it['bron']['claudeId'], oud=o, nieuw=n)
def na218(it):
    o = it['opgave'] or ''
    if it['merge'].get('doel') != 'G6-MEET-E03' or not (m := re.fullmatch(r'Een rechthoek is (\d+) cm lang en (\d+) cm breed\. Hoeveel cm² is de oppervlakte\?', o)): return
    l, b = int(m.group(1)), int(m.group(2)); ding, was = ding260(it['bron']['claudeId'], l, b)      # #260: de context past bij de maat
    if was: _log(punt=260, claudeId=it['bron']['claudeId'], maat=f'{l} × {b}', was=was, nu=ding or 'Een rechthoek (kaal)')
    assert ding != 'Een placemat' and MAAT260[ding](l, b), ('#260', ding, l, b)
    if ding is None: return
    it['opgave'] = f'{ding} is een rechthoek van {m.group(1)} cm lang en {m.group(2)} cm breed. Hoeveel cm² is de oppervlakte?'
    _log(punt=218, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'])

# #224 (zacht): E09 #3 602 (na #189, 3/8 van 32): 'wat overblijft' = 32 − 12 = 20 (Claudes label verkeerde-bewerking, zoals de andere items)
def fix224(it):
    if it['bron']['claudeId'] != ID189: return
    ex = it['extraVelden']
    if not any(d['fout'] == '20' for d in ex['claudeDenkfouten']):
        ex['claudeDenkfouten'].append({'fout': '20', 'denkfout': 'verkeerde-bewerking'})
        ex['claudeFoutHints'].append({'stap': None, 'fout': '20', 'uitleg': 'Dat is wat er overblijft.'})
        _log(punt=224, claudeId=ID189, erbij='20', denkfout='verkeerde-bewerking (wat overblijft: 32 − 12)')

# #227 (zacht): E03 #5 staat op zichzelf (na #201): geen 'visual nodig' en geen nietLiveZonderBeeld meer. Doc: komt er toch een plaatje, dan niet alleen kleur.
def na227(it):
    if it['merge'].get('doel') != 'G6-GET-E03' or not it['merge'].get('zin201'): return
    v = it['visual']
    if v.get('nodig') or v.get('nietLiveZonderBeeld'):
        it['visual'] = dict(v, nodig=False, toelichting=None, nietLiveZonderBeeld=False, eisAlsErEenPlaatjeKomt='kleur is niet het enige kenmerk (les 11; #227)')
        _log(punt=227, claudeId=it['bron']['claudeId'], visual='nodig → False, nietLiveZonderBeeld weg')

# #217 (zacht): bordtitels in de merge-data en de doc (het canonieke bord/de spine: via Oefeningen/Leerlijn)
BORD217 = {'G6-MEET-E01': 'Kilometer, meter, centimeter en millimeter omrekenen', 'G6-MEET-E04': 'Liter, centiliter en milliliter omrekenen',
           'G6-MEET-E05': 'Kilo en gram omrekenen'}

# ================================================================== ronde 8 (Oefeningen 4b/3c/batch 5 #219, #228–#231; Didactiek ronde 7 + 4b #260–#263;
# Didactiek batch 3 #251; besluiten Dave 22:39–22:44). Uitgevoerd door Overzicht.
DOOR8 = 'Overzicht (G6-fixlijst ronde 8, Dave 22:39–22:44)'
_BASIS = re.compile(r'\s*\(antwoord (?:vanaf|onder) \d+\)\s*$')
def _basisregel(r): return _BASIS.sub('', r)
# #219 (Oefeningen batch 5, besluit Dave): de lijngrafiekregels staan in de motor (fout_regels._lijn219); 'fout = antwoord : 10' gaat eruit
def _e219(st):
    fh = st['foutHints']; weg = [f for f in fh if f['regel'] == 'fout = antwoord : 10']
    if weg:
        st['foutHints'] = [f for f in fh if f['regel'] != 'fout = antwoord : 10']
        _log(punt=219, entry=f"{st['doel']} #{st['nrOrigineel']}", weg=['fout = antwoord : 10'], waarom="streepjes geteld gaat nu via 'fout = antwoord : perstreep' (perstreep uit visual.jsRender)")
# #263 (Didactiek ronde 7 + 4b): de nullenregels (R215) horen niet in MEET-E01 #7 (strook: getal1 is de eerste afstand in km, 0 treffers, tekst None)
def _e263(st):
    fh = st['foutHints']; r215 = {r for r, _, _ in R215}
    if any(f['regel'] in r215 for f in fh):
        st['foutHints'] = [f for f in fh if f['regel'] not in r215]
        _log(punt=263, entry=f"{st['doel']} #{st['nrOrigineel']}", weg=sorted(r215))
def pas_entries_ronde8(st):
    k = (st['doel'], st.get('nrOrigineel'))
    if st['doel'] == 'G6-VBN-E02': _e219(st)
    if k == ('G6-MEET-E01', 7): _e263(st)
def assert_tekst263(somtypen):
    """#263 / les 39: nergens een regel met tekst None, leeg of een plaatshouder van Overzicht."""
    for st in somtypen:
        for f in st['foutHints']:
            t = f.get('tekst')
            assert t and t.strip() and t.strip().lower() != 'none' and not t.startswith('[TEKST NODIG'), ('#263: regel zonder tekst', st['doel'], st.get('nrOrigineel'), f['regel'])

# #228 (Oefeningen batch 5, Leerlijn-data): contexten die niet kloppen. Vervanging per claudeId in opgave, claudeUitleg en Claudes fout-hints.
CTX228 = {
    '1aa245af': [('2 knikkers', "2 pannenkoeken"), ('een knoop', 'een pannenkoek'), ('2/4 knoop', '2/4 pannenkoek'), ('2 knikkers, niet één', '2 pannenkoeken, niet één'), ('elke knoop', 'elke pannenkoek')],   # VERH-E03 #1 003
    '3aae86ec': [("3 tanden worden eerlijk verdeeld over 8 dino's", "3 pizza's worden eerlijk verdeeld over 8 kinderen"), ('een tand krijgt elke dino', 'een pizza krijgt elk kind'),
                 ('Elke dino krijgt 3/8 tand', 'Elk kind krijgt 3/8 pizza'), ('Er zijn 3 tanden', "Er zijn 3 pizza's"), ('Elke dino krijgt van elke tand', 'Elk kind krijgt van elke pizza')],   # 005
    '4aac4127': [('een poesje', 'een noot'), ('3/8 poesje', '3/8 noot'), ('elk poesje', 'elke noot')],      # 006 (noten)
    '84ebfc50': [('een poesje', 'een vis'), ('4/5 poesje', '4/5 vis'), ('elk poesje', 'elke vis')],        # 009 (vissen)
    'f5dd4802': [('een stap', 'een ei'), ('4/8 stap', '4/8 ei'), ('elke stap', 'elk ei')],                  # 016 (eieren)
    'ffad26c3': [('een wortel', 'een noot'), ('4/8 wortel', '4/8 noot'), ('elke wortel', 'elke noot')],     # 017 (noten)
    '00c31a3e': [('In het stadion liggen 354 pionnen', 'In de sporthal liggen 354 pionnen')],              # VERH-E02 #4 001
    '91252201': [('Op de kinderboerderij liggen 186 eieren', 'In de klas liggen 186 knikkers'), ('groene eieren', 'groene knikkers')],   # VERH-E02 #4 002
}
# #230: Claudes sleutels met een punt → komma (VERH-E02 #4); 'Een kwart' → kleine letter (VERH-E02 #3 021, zoals de regels en 023)
KOMMA230 = {'91252201': ('37.2', '37,2'), 'b8113228': ('62.4', '62,4')}
KLEIN230 = {'199e2627': [('Een kwart', 'een kwart'), ('Een derde', 'een derde'), ('Drie hele stroken', 'drie hele stroken')]}
def _overal(it, paren):
    ex = it['extraVelden']; n = 0
    for a, b in paren:
        for k in ('opgave', 'antwoord', 'optiesTekst'):
            if isinstance(it.get(k), str) and a in it[k]: it[k] = it[k].replace(a, b); n += 1
        for o in it.get('opties') or []:
            if a in o['tekst']: o['tekst'] = o['tekst'].replace(a, b); n += 1
        for k in ('claudeUitleg', 'claudeKaleSom'):
            if isinstance(ex.get(k), str) and a in ex[k]: ex[k] = ex[k].replace(a, b); n += 1
        for lst, veld in (('claudeFoutHints', 'uitleg'), ('claudeFoutHints', 'fout'), ('claudeDenkfouten', 'fout')):
            for f in ex.get(lst) or []:
                if isinstance(f.get(veld), str) and a in f[veld]: f[veld] = f[veld].replace(a, b); n += 1
    return n
def na228_230(it):
    cid = it['bron']['claudeId'][:8]; d = it['merge'].get('doel')
    if d not in ('G6-VERH-E02', 'G6-VERH-E03'): return
    if cid in CTX228:
        o = it['opgave']; n = _overal(it, CTX228[cid]); assert n and it['opgave'] != o, ('#228: vervanging niet gelukt', cid, o)
        _log(punt=228, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'], vervangen=n)
    if cid in KOMMA230:
        a, b = KOMMA230[cid]; n = _overal(it, [(a, b)]); assert n >= 2, ('#230: sleutel niet gevonden', cid, a)
        _log(punt=230, claudeId=it['bron']['claudeId'], sleutel=f'{a} → {b}')
    if cid in KLEIN230:
        n = _overal(it, KLEIN230[cid]); assert n, ('#230: optie niet gevonden', cid)
        _log(punt=230, claudeId=it['bron']['claudeId'], opties=[f'{a} → {b}' for a, b in KLEIN230[cid]], vervangen=n)
    if d == 'G6-VERH-E02':
        for o in it.get('opties') or []:
            assert not re.match(r'(Een|De|Drie|Twee|Vier) (kwart|derde|helft|vierde|vijfde|zesde|achtste|tiende|twaalfde|zestiende|hele)\b', o['tekst']), ('#230: optie met hoofdletter', it['bron']['claudeId'], o['tekst'])
    for x in (it['extraVelden'].get('claudeFoutHints') or []):
        assert not re.fullmatch(r'\d+\.\d+', x['fout']), ('#230: sleutel met punt', it['bron']['claudeId'], x['fout'])

# #260 (Didactiek ronde 7 + 4b, verplicht): MEET-E03 #1 de context past bij de maat. Keuze per hash (DING218); voldoet het ding niet aan zijn
# maatvoorwaarde (of is het de placemat), dan per hash 'rechthoek', 'tegel' of 'etiket'. l = lengte, b = breedte (cm).
MAAT260 = {'Een foto': lambda l, b: b >= 3 and l <= 4 * b, 'Een kaart': lambda l, b: b >= 4, 'Een sticker': lambda l, b: l <= 15,
           'Een spelbord': lambda l, b: b >= 10, 'Een vlaggetje': lambda l, b: l <= 5 * b, 'Een tegel': lambda l, b: True, 'Een etiket': lambda l, b: True, None: lambda l, b: True}
TERUG260 = [None, 'Een tegel', 'Een etiket']
def ding260(cid, l, b):
    ding = DING218[_h(f"{cid}-218") % len(DING218)]
    if ding == 'Een placemat' or not MAAT260[ding](l, b): return TERUG260[_h(f"{cid}-260") % len(TERUG260)], ding
    return ding, None

# #251 (Didactiek batch 3) met de correctie van Dave (22:44): drie niveaus bij grootst/kleinst (GET-E03 #2/#3), op de zwaarste route die het kind echt nodig heeft.
# Route tussen twee breuken: 1 = zelfde noemer of zelfde teller; 2 = de ene noemer een veelvoud van de andere, of de ½-stap (ze liggen aan weerskanten van ½,
# of een van beide is ½); 3 = een gemeenschappelijke noemer. Het kind moet elke andere breuk uitschakelen: direct tegen het antwoord, of via een derde breuk
# (dan telt de zwaarste van de twee stappen). Het niveau is het zwaarste van die uitschakelingen.
NIVEAU251 = {1: ('basis', 'Opwarmen'), 2: ('toepassen', 'Oefenen'), 3: ('kritisch', 'Uitdaging')}
ROUTE251 = {1: 'zelfde noemer of zelfde teller', 2: 'veelvoud of ½', 3: 'gemeenschappelijke noemer'}
VRAAG251 = re.compile(r'^Welke breuk is het (grootst|kleinst)\? Kies uit (\d+/\d+), (\d+/\d+) of (\d+/\d+)\.$')
def _stap251(p, q):
    from fractions import Fraction as Fr
    (tp, np_), (tq, nq) = p, q
    if np_ == nq or tp == tq: return 1
    if np_ % nq == 0 or nq % np_ == 0: return 2
    h = Fr(1, 2); fp, fq = Fr(tp, np_), Fr(tq, nq)
    if fp == h or fq == h or (fp - h) * (fq - h) < 0: return 2
    return 3
def niveau251(br, ant):
    """x uitschakelen: direct tegen het antwoord, of via y die tussen x en het antwoord ligt (x < y bij grootst; x > y bij kleinst is dan hetzelfde
    als: y ligt dichter bij het antwoord). De volgorde maakt niet uit voor grootst/kleinst: y moet 'beter' zijn dan x."""
    from fractions import Fraction as Fr
    p = [tuple(map(int, b.split('/'))) for b in br]; a = p[br.index(ant)]; rest = [x for x in p if x != a]
    val = lambda q: Fr(q[0], q[1]); grootst = all(val(a) > val(x) for x in rest)
    beter = lambda y, x: val(y) > val(x) if grootst else val(y) < val(x)
    kost = [min([_stap251(a, x)] + [max(_stap251(x, y), _stap251(y, a)) for y in rest if y != x and beter(y, x)]) for x in rest]
    return max(kost)
def na251(it):
    if it['merge'].get('doel') != 'G6-GET-E03' or not (m := VRAAG251.match(it['opgave'] or '')): return
    br = [m.group(2), m.group(3), m.group(4)]; ant = str(it['antwoord']).strip()
    assert ant in br, ('#251: antwoord niet in de opties', it['opgave'], ant)
    n = niveau251(br, ant); oud = (it['niveau'], it['niveauKind'], it['extraVelden'].get('claudeNiveau'))
    it['niveau'], it['niveauKind'] = NIVEAU251[n]
    it['merge']['niveau251'] = {'niveau': n, 'route': ROUTE251[n], 'voor': {'niveau': oud[0], 'niveauKind': oud[1], 'claudeNiveau': oud[2]}}
    _log(punt=251, claudeId=it['bron']['claudeId'], opgave=it['opgave'], niveau=n, route=ROUTE251[n], oud=list(oud), soort=m.group(1))

# #261 (Didactiek ronde 7 + 4b, besluit Dave: doen): bordtitels in de merge-data. E01 #6 (kg) blijft in E01 tot Leerlijn beslist.
BORD261 = {'G6-MEET-E01': 'Lengtematen omrekenen en maten met een komma optellen', 'G6-MEET-E05': 'Kilogram en gram omrekenen',
           'G6-MEET-E03': 'Oppervlakte uitrekenen in cm² en m²'}
BORD217 = dict(BORD217, **BORD261)      # #261 vervangt de titels van #217 voor E01/E05 en voegt E03 toe (E04 blijft)

# ================================================================== ronde 8b (Didactiek batch 5 #271–#283, build 22:54:03; batch 6 #292–#299, apply 23:06:47;
# recheck 3d/4c #252/#254; Leerlijn-besluit #217/#261; besluiten Dave 22:59 en 23:09). Uitgevoerd door Overzicht.
import copy as _copy
DOOR8B = 'Overzicht (G6-fixlijst ronde 8b, Dave 22:59/23:09)'
def _fb(regel, soort, tekst, sterker=None, bron='Didactiek'):
    return {'regel': regel, 'soort': soort, 'tekst': tekst, 'tekstSterker': sterker, 'bron': 'nieuw', 'door': DOOR8B, 'tekstBron': bron}

# #271 (verplicht): VERH-E01 #1 'hetzelfde erbij' vóór de Claude-regels. Tekst = die van 'opgeteld' in de entry (Oefeningen heeft #272 al verwerkt).
R271 = ('fout = y1 + (x2 − x1)', 'fout = y1 + x2')
def _e271(st):
    fh = st['foutHints']
    if any(f['regel'] in R271 for f in fh): return
    opg = next(f for f in fh if f['regel'] == 'Claudes sleutel: optellen-ipv-vermenigvuldigen')
    nieuw = [dict(_fb(r, 'opgeteld', opg['tekst'], opg.get('tekstSterker'), 'tekst van de entry (Oefeningen, #272)')) for r in R271]
    st['foutHints'] = nieuw + fh
    _log(punt=271, entry=f"{st['doel']} #{st['nrOrigineel']}", nieuw=list(R271), waarom="'hetzelfde erbij' (les 32/61) vóór de Claude-regels")

# #274 (zacht): VBN-E02 #3 'de waarde van één maand' vóór 'streepjes geteld' (fout = antwoord : perstreep). Tekst van Didactiek (vraag, want 10 van de 32 zijn ook het aantal streepjes).
R274 = _fb('fout = de waarde van één maand', 'één maand',
           'Is dat het aantal van één maand? De vraag gaat over alle maanden samen. Tel de aantallen van alle maanden bij elkaar op.')
def _e274(st):
    fh = st['foutHints']
    if any(f['regel'] == R274['regel'] for f in fh): return
    i = next(i for i, f in enumerate(fh) if f['regel'].startswith('fout = antwoord : perstreep'))
    st['foutHints'] = fh[:i] + [dict(R274)] + fh[i:]
    _log(punt=274, entry=f"{st['doel']} #{st['nrOrigineel']}", nieuw=R274['regel'], voor=fh[i]['regel'])

# #296 (verplicht): torenregels MKU-E03 in de volgorde van Didactiek; 'een toren dubbel' (het antwoord plus één toren) weg; nieuw 'elke toren één te veel'.
R296 = _fb('fout = het antwoord plus het aantal torens', 'elke toren één te veel',
           'Heb je bij elke toren één blokje te veel geteld? Tel bij elke toren van het onderste tot het bovenste blokje.',
           'Kijk naar één toren. Het onderste blokje staat op de grond, de grond zelf telt niet. Tel zo elke toren.')
VOLGORDE296 = ['fout = het aantal torens', 'fout = de hoogste toren keer het aantal torens', 'fout = de hoogste toren keer het aantal vakjes van de grond',
               'fout = het antwoord plus het aantal torens', 'fout = het antwoord min één toren']
def _e296(st):
    fh = st['foutHints']; weg = [f['regel'] for f in fh if f['regel'] == 'fout = het antwoord plus één toren']
    fh = [f for f in fh if f['regel'] != 'fout = het antwoord plus één toren']
    if not any(f['regel'] == R296['regel'] for f in fh): fh.append(dict(R296))
    toren = {f['regel']: f for f in fh if f['regel'] in VOLGORDE296}
    assert set(toren) == set(VOLGORDE296), ('#296: torenregel ontbreekt', sorted(set(VOLGORDE296) - set(toren)))
    st['foutHints'] = [toren[r] for r in VOLGORDE296] + [f for f in fh if f['regel'] not in toren]
    _log(punt=296, entry=f"{st['doel']} #{st['nrOrigineel']}", weg=weg, volgorde=VOLGORDE296)

R275C = _fb('fout = het getal net boven de stip', 'getal net boven de stip',
            'Dat is het getal langs de zijkant net boven de stip. Zoek het getal op of net onder de stip en tel de streepjes verder tot de stip.')
def _e275c(st):
    fh = st['foutHints']
    if any(f['regel'] == R275C['regel'] for f in fh): return
    i = next(i for i, f in enumerate(fh) if f['regel'] == 'fout = het getal onder de stip') + 1
    st['foutHints'] = fh[:i] + [dict(R275C)] + fh[i:]
    _log(punt='275c', entry=f"{st['doel']} #{st['nrOrigineel']}", nieuw=R275C['regel'], na='fout = het getal onder de stip')
_pas_entries_ronde8_oud = pas_entries_ronde8
def pas_entries_ronde8(st):
    _pas_entries_ronde8_oud(st)
    k = (st['doel'], st.get('nrOrigineel'))
    if k == ('G6-VERH-E01', 1): _e271(st)
    if k == ('G6-VBN-E02', 3): _e274(st)
    if st['doel'] == 'G6-MKU-E03': _e296(st)
    if k == ('G6-VBN-E02', 2): _e275c(st)

# ------------------------------------------------------------------ Leerlijn-besluit #217/#261 (canoniek): E01 #6 → MEET-E05, bordtitels = de spine
KOP_E01_6 = 'Een pakket weegt # kg, een ander # kg. Hoeveel kg wegen ze samen?'
VERHUIS261 = {('G6-MEET-E01', KOP_E01_6): 'G6-MEET-E05'}
BORD261 = {'G6-MEET-E01': 'Lengtematen omrekenen, ook met komma', 'G6-MEET-E03': 'Oppervlakte uitrekenen in cm², dm² en m²',
           'G6-MEET-E04': 'Liter omrekenen naar dl, cl en ml', 'G6-MEET-E05': 'Kilo en gram vergelijken en omrekenen'}
BORD217 = dict(BORD217, **BORD261)
def na_verhuis261(it):
    d = it['merge'].get('doel'); naar = VERHUIS261.get((d, it['merge'].get('somtype')))
    if not naar: return
    it['merge']['doel'] = naar; it['doelId'] = naar
    it['merge']['verhuisd261'] = {'van': d, 'naar': naar, 'besluit': 'Leerlijn #217/#261 (canoniek): kg met komma optellen hoort bij MEET-E05'}
    _log(punt=261, claudeId=it['bron']['claudeId'], verhuisd=f'{d} → {naar}')

# ------------------------------------------------------------------ #276 (zacht): VBN-E02 grafiekdata
import json as _json276, os as _os276
TABEL276 = _json276.load(open(_os276.path.join(_os276.path.dirname(_os276.path.dirname(_os276.path.abspath(__file__))), 'bevroren', 'vbn276_streepjes_v1.json')))['tabel']
TITEL276 = {'bezoekers': 'Bezoekers per maand', 'boeken': 'Geleende boeken per maand', 'broodjes': 'Verkochte broodjes per maand', 'kaartjes': 'Verkochte kaartjes per maand'}
BIJ276 = re.compile(r'^Hoeveel (\w+) kwamen er bij van (\w+) naar (\w+)\?$')
DING276 = re.compile(r'^Hoeveel (\w+) ')
def _fam276(opg, pts, ps, co, nr):
    v = [w for _, w in pts]; o = opg.lower()
    g = [i for _, i in sorted((o.find(n), i) for i, (n, _) in enumerate(pts) if re.search(rf'\b{n}\b', o))]
    tot = sum(v); b = min(g) if g else 0
    A = v[max(g)] - v[min(g)] if nr == 1 else (v[g[0]] if nr == 2 else tot)
    F = {}
    if nr == 1: F['som2'] = v[g[0]] + v[g[1]]; F['tweede'] = v[max(g)]
    if A % ps == 0: F['A:ps'] = A // ps
    if nr == 3:
        for i in range(len(v)): F[f'tot+m{i}'] = tot + v[i]
        for i in range(len(v)): F[f'tot-m{i}'] = tot - v[i]
        F['eerste+laatste'] = v[0] + v[-1]; F['tot-eerste-laatste'] = tot - v[0] - v[-1]
    if nr == 2: F['onder'] = v[g[0]] // co * co
    for k in (1, -1): F[f'A{k:+d}ps'] = A + k * ps
    for i in range(len(v)):
        if i != b or nr == 3: F[f'maand{i - b:+d}'] = v[i]
    for k in (2, -2): F[f'A{k:+d}ps'] = A + k * ps
    F['A+co'] = A + co; F['A-co'] = A - co
    return A, F
VOORKEUR276 = {(2, 'klok-verkeerd-gelezen'): 'maand'}
def _kies276(F, x, nr, denk):
    c = [k for k, w in F.items() if w == x]
    if not c: return None
    pref = VOORKEUR276.get((nr, denk))
    if pref: c = sorted(c, key=lambda k: not k.startswith(pref))
    return c[0]
def _zet_exact(it, oud_nieuw):
    """Vervang hele waarden (geen stukjes tekst) in antwoord, opties, sleutels en Claudes velden."""
    f = lambda v: oud_nieuw.get(v, v) if isinstance(v, str) else v
    it['antwoord'] = f(it['antwoord'])
    for o in it.get('opties') or []: o['tekst'] = f(o['tekst'])
    if it.get('opties'): it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    ad = it.get('antwoordDetail') or {}
    if 'juisteOptieTekst' in ad: ad['juisteOptieTekst'] = f(ad['juisteOptieTekst'])
    ex = it['extraVelden']
    for lst in (it.get('foutHints') or [], ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], ex.get('mergeFoutHints') or []):
        for x in lst:
            if isinstance(x, dict) and 'fout' in x: x['fout'] = f(x['fout'])
    c = it.get('controle') or {}
    if c.get('verwacht') is not None and str(c['verwacht']) in oud_nieuw: c['verwacht'] = oud_nieuw[str(c['verwacht'])]
def na276(it):
    if it['merge'].get('doel') != 'G6-VBN-E02': return
    jr = it['visual']['jsRender']; o0 = it['opgave'] or ''
    nr = 1 if BIJ276.match(o0) else 3 if 'alle maanden samen' in o0 else 2 if re.match(r'^Hoeveel \w+ waren er in \w+\?$', o0) else None
    assert nr, ('#276: onbekende vraag', it['bron']['claudeId'], o0)
    cid = it['bron']['claudeId']; ps, co = jr['perstreep'], jr['cijfer_om']; oud_pts = [(p['naam'], p['waarde']) for p in jr['punten']]
    A0, F0 = _fam276(it['opgave'], oud_pts, ps, co, nr); assert str(A0) == str(it['antwoord']), ('#276: antwoord klopt niet met de grafiek', cid)
    sleutels = [(d['fout'], d['denkfout'], _kies276(F0, int(d['fout']), nr, d['denkfout'])) for d in it['extraVelden'].get('claudeDenkfouten') or []]
    opg = it['opgave']
    if nr == 1 and (m := BIJ276.match(opg)): opg = f'Hoeveel {m.group(1)} waren er in {m.group(3)} meer dan in {m.group(2)}?'
    o = opg.lower(); g = sorted(i for i, (n, _) in enumerate(oud_pts) if re.search(rf'\b{n}\b', o))
    STAP = [1, 1, 2, 3, 3, 4, 5, -1, -2, 0]
    for poging in range(3000):      # ronde 9: meer pogingen voor een vast aantal streepjes (#276); de eerste geslaagde poging blijft dezelfde
        h = _h(f'{cid}-276-{poging}'); n = len(oud_pts)
        k = [1 + h % (4 + 2 * (poging // 20))]; hh = h // 97
        for i in range(1, n):
            k.append(k[-1] + STAP[hh % len(STAP)]); hh //= len(STAP)
        if nr == 1:      # de stap tussen de twee maanden uit de vraag: 1–5 streepjes, gelijk verdeeld over de items (#276)
            t332 = TABEL276.get(cid, 'oud')      # ronde 9 (#276 gelijk verdelen, #332): bevroren/vbn276_streepjes_v1.json
            want = (1 + _h(f'{cid}-276a-{poging // 20}') % 5) if t332 == 'oud' else t332; d = want - (k[g[1]] - k[g[0]])
            k = k[:g[1]] + [x + d for x in k[g[1]:]]
        if min(k) < 1 or max(k) > 20: continue
        stappen = [k[i + 1] - k[i] for i in range(n - 1)]
        if len(set(stappen)) < 2 or stappen.count(2) == len(stappen): continue
        pts = [(nm, x * ps) for (nm, _), x in zip(oud_pts, k)]
        A, F = _fam276(opg, pts, ps, co, nr)
        if A <= 0: continue
        if nr == 1 and A in (pts[g[0]][1], pts[g[1]][1]): continue      # #332 (les 92): het antwoord is nooit de waarde van een maand uit de vraag
        nieuw = {}
        for fout, denk, fam in sleutels:
            if fam is None or fam not in F: break
            nieuw[fout] = str(F[fam])
        else:
            w = list(nieuw.values())
            if len(set(w)) == len(w) and str(A) not in w and all(int(x) > 0 for x in w): break
    else: raise AssertionError(('#276: geen grafiek gevonden', cid))
    oud_ans = str(it['antwoord'])
    jr['punten'] = [{'naam': nm, 'waarde': x} for nm, x in pts]
    mx = -(-max(x for _, x in pts) // co) * co; jr['maxVoor276'] = jr.get('max'); jr['max'] = mx
    ding = DING276.match(opg).group(1); jr['titel'] = TITEL276[ding]
    it['merge']['grafiek276'] = {'oud': {'punten': oud_pts, 'max': jr['maxVoor276'], 'antwoord': oud_ans, 'opgave': it['opgave']},
                                 'sleutels': {f: {'familie': fam, 'nieuw': nieuw[f]} for f, _, fam in sleutels}, 'stappenInStreepjes': stappen}
    _zet_exact(it, dict({oud_ans: str(A)}, **nieuw))
    assert str(it['antwoord']) == str(A), ('#276', cid)
    it['opgave'] = opg
    if nr == 1:      # #332/V-#330: de maand die eerst in de vraag staat heeft het grootste aantal; het antwoord is geen maand uit de vraag
        gv = [w for _, _, w in sorted((opg.lower().find(nm), nm, w) for nm, w in pts if re.search(rf'\b{nm}\b', opg.lower()))]
        assert len(gv) == 2 and gv[0] > gv[1] and A not in gv, ('#332/V-#330', cid, opg, pts)
        it['merge']['grafiek276']['streepjes'] = A // ps; it['merge']['grafiek276']['tabel332'] = TABEL276.get(cid, 'oud')
    _log(punt=276, claudeId=cid, nr=nr, stappen=stappen, antwoord=A, max=mx, titel=jr['titel'])

# ------------------------------------------------------------------ #278/#228-bewaker (VERH-E03 #1) en #280 (VERH-E01 €/L, VERH-E02 #4 contexten)
VERDEEL278 = re.compile(r"^(\d+) (.+?) worden eerlijk verdeeld over (\d+) (.+?)\. Welk deel van een (.+?) krijgt (elke?) (.+?)\?$")
NIET278 = {'kaartjes', 'stickers', 'ballen', 'truien', 'noten', 'eieren'}
ENK278 = {'botten': 'bot', 'blaadjes': 'blaadje', 'pannenkoeken': 'pannenkoek', 'kaartjes': 'kaartje', "pizza's": 'pizza', 'noten': 'noot', 'stickers': 'sticker',
          'vissen': 'vis', 'ballen': 'bal', 'truien': 'trui', 'eieren': 'ei', 'wafels': 'wafel', 'taarten': 'taart', 'broden': 'brood', 'wortels': 'wortel',
          'appels': 'appel', 'repen chocola': 'reep chocola'}
ELK278 = {'bot': 'elk', 'blaadje': 'elk', 'kaartje': 'elk', 'ei': 'elk', 'brood': 'elk', 'kind': 'elk', 'konijn': 'elk'}
# Didactiek Z-#278 en V-#228: pizza, pannenkoek, reep chocola, taart, brood of wafel; 006/017 volgens het voorstel van V-#228.
NIEUW278 = {'2e0a4c42': ('wafels', 'kinderen', 'kind'), '4aac4127': ('wortels', 'konijnen', 'konijn'), '78a65d26': ('repen chocola', 'kinderen', 'kind'),
            'c6c19826': ("pizza's", 'kinderen', 'kind'), 'cdf0d298': ('taarten', 'kinderen', 'kind'), 'e2b83196': ('broden', 'kinderen', 'kind'),
            'f28d3727': ('wafels', 'kinderen', 'kind'), 'f5dd4802': ('pannenkoeken', 'kinderen', 'kind'), 'ffad26c3': ('appels', 'eekhoorns', 'eekhoorn')}      # sleutel = claudeId[:8] (004, 006, 007, 012, 013, 014, 015, 016, 017)
WIE_MV = {'dino': "dino's", 'kind': 'kinderen', 'eekhoorn': 'eekhoorns', 'pinguïn': 'pinguïns', 'poes': 'poezen', 'speler': 'spelers', 'konijn': 'konijnen'}
def _elk(w, hoofd=False): e = ELK278.get(w, 'elke'); return e.capitalize() if hoofd else e
def na278(it):
    if it['merge'].get('doel') != 'G6-VERH-E03' or not (m := VERDEEL278.match(it['opgave'] or '')): return
    t, mv, n, wmv, ev, _e, wev = m.groups()
    if mv in NIET278:
        k = it['bron']['claudeId'][:8]; assert k in NIEUW278, ('#278: ding dat je niet kunt verdelen zonder vervanging', it['bron']['claudeId'], it['opgave'])
        nmv, nwmv, nwev = NIEUW278[k]; nev = ENK278[nmv]
        paren = [(f'{t} {mv} worden', f'{t} {nmv} worden'), (f'over {n} {wmv}.', f'over {n} {nwmv}.'), (f'van een {ev} krijgt {_elk(wev)} {wev}?', f'van een {nev} krijgt {_elk(nwev)} {nwev}?'),
                 (f'{_elk(wev, True)} {wev} krijgt {t}/{n} {ev}.', f'{_elk(nwev, True)} {nwev} krijgt {t}/{n} {nev}.'), (f'Er zijn {t} {mv}, niet één.', f'Er zijn {t} {nmv}, niet één.'),
                 (f'{_elk(wev, True)} {wev} krijgt van {_elk(ev)} {ev} een', f'{_elk(nwev, True)} {nwev} krijgt van {_elk(nev)} {nev} een')]
        o = it['opgave']; cnt = _overal(it, paren)
        assert it['opgave'] != o and cnt >= 4, ('#278: vervanging niet gelukt', it['bron']['claudeId'], o, cnt)
        it['merge']['context278'] = {'oud': o, 'nieuw': it['opgave']}
        _log(punt=278, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'], vervangen=cnt)
    m = VERDEEL278.match(it['opgave']); t, mv, n, wmv, ev, e, wev = m.groups()
    # bewaker V-#228 (les 63): het ding in 'Welk deel van een X' is het enkelvoud van wat er verdeeld wordt, en dat kun je verdelen; wie klopt ook
    assert ENK278.get(mv) == ev and mv not in NIET278, ('#228/#278 W9-bewaker', it['bron']['claudeId'], it['opgave'])
    assert WIE_MV.get(wev) == wmv and e == _elk(wev), ('#228 W9-bewaker (wie)', it['bron']['claudeId'], it['opgave'])
EURO280 = re.compile(r'(?<![\w€])(\d+(?:,\d+)?) euro\b'); LITER280 = re.compile(r'(?<![\w])(\d+(?:,\d+)?) liter\b')
def _overal_re(it, rx, rep):
    ex = it['extraVelden']; n = 0
    def sub(s):
        nonlocal n
        s2, k = rx.subn(rep, s); n += k; return s2
    for k in ('opgave', 'antwoord', 'optiesTekst'):
        if isinstance(it.get(k), str): it[k] = sub(it[k])
    for o in it.get('opties') or []: o['tekst'] = sub(o['tekst'])
    ad = it.get('antwoordDetail') or {}
    if isinstance(ad.get('juisteOptieTekst'), str): ad['juisteOptieTekst'] = sub(ad['juisteOptieTekst'])
    for k in ('claudeUitleg', 'claudeKaleSom'):
        if isinstance(ex.get(k), str): ex[k] = sub(ex[k])
    for lst in (it.get('foutHints') or [], ex.get('claudeFoutHints') or [], ex.get('claudeDenkfouten') or [], ex.get('mergeFoutHints') or []):
        for f in lst:
            for veld in ('fout', 'uitleg'):
                if isinstance(f, dict) and isinstance(f.get(veld), str): f[veld] = sub(f[veld])
    return n
CTX280 = {'00c31a3e': ('Op de camping staan 354 tenten. 1/6 ervan is nieuw. Hoeveel nieuwe tenten zijn er?', [('níét groen', 'níét nieuw')]),
          '91252201': ('Een bakker bakt 186 broodjes. 5/6 ervan is verkocht. Hoeveel broodjes zijn verkocht?', []),
          'b8113228': ('In een doos zitten 312 knikkers. 5/6 ervan is van glas. Hoeveel knikkers zijn van glas?', [])}
def na280(it):
    d = it['merge'].get('doel')
    if d == 'G6-VERH-E01':
        n = _overal_re(it, EURO280, r'€\1') + _overal_re(it, LITER280, r'\1 L')
        if n: _log(punt=280, claudeId=it['bron']['claudeId'], notatie=n)
        for veld in (it['opgave'], it['antwoord'], *[o['tekst'] for o in it.get('opties') or []]):
            assert not EURO280.search(veld) and not LITER280.search(veld), ('#280: euro/liter niet in G6-notatie', it['bron']['claudeId'], veld)
    cid = it['bron']['claudeId'][:8]
    if d == 'G6-VERH-E02' and cid in CTX280:
        o = it['opgave']; nieuw, paren = CTX280[cid]
        assert re.search(r'\b(354|186|312)\b', o), ('#280', cid, o)
        it['opgave'] = nieuw; _overal(it, paren); it['merge']['context280'] = {'oud': o, 'nieuw': nieuw}
        _log(punt=280, claudeId=it['bron']['claudeId'], oud=o, nieuw=nieuw)
    if d == 'G6-VERH-E02': assert 'knopen in het huis' not in (it['opgave'] or ''), ('#280', cid)

# ------------------------------------------------------------------ #254 (852) en #290 (kleinst nooit ½)
def na254(it):
    if it['opgave'] != 'Welke breuk is het grootst? Kies uit 2/5, 2/11 of 3/10.': return
    o = it['opgave']; it['opgave'] = 'Welke breuk is het grootst? Kies uit 3/8, 3/10 of 1/4.'
    _zet_exact(it, {'2/5': '3/8', '2/11': '1/4'})
    import sys as _s; _s.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import breukvorm as _BV
    it['antwoordOokGoed'] = [x for x in (it.get('antwoordOokGoed') or []) if x not in _BV.gelijk('2/5')]; _BV.pas_toe(it)
    assert it['antwoord'] == '3/8' and {f['fout'] for f in it['foutHints']} == {'3/10', '1/4'}, ('#254', it['foutHints'])
    it['merge']['opgave254'] = {'oud': o, 'nieuw': it['opgave'], 'waarom': 'paar 2/11–3/10 had kgv 110 (Didactiek #254)'}
    _log(punt=254, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'])
def assert290(it):
    if it['merge'].get('doel') == 'G6-GET-E03' and (m := VRAAG251.match(it['opgave'] or '')) and m.group(1) == 'kleinst':
        assert str(it['antwoord']).strip() != '1/2', ('#290: kleinst met antwoord ½', it['bron']['claudeId'], it['opgave'])

# ------------------------------------------------------------------ #299 (zacht): MKU-E03 drie niveaus; #295 (README/app): H2 met plattegrond pas live met het plaatje
def _achter299(st):
    """Torens die vanaf rechtsvoor (kijker bij de laatste rij en de laatste kolom) achter een hogere toren staan: er staat een hogere toren
    direct ervoor (r+1, c), ernaast aan de kijkerkant (r, c+1) of schuin ervoor (r+1, c+1)."""
    R, C = len(st), max(len(x) for x in st); h = lambda r, c: st[r][c] if r < R and c < len(st[r]) else 0
    return sum(1 for r in range(R) for c in range(len(st[r])) if st[r][c] > 0 and max(h(r + 1, c), h(r, c + 1), h(r + 1, c + 1)) > st[r][c])
NIVEAU299 = {1: ('basis', 'Opwarmen'), 2: ('toepassen', 'Oefenen'), 3: ('kritisch', 'Uitdaging')}
H2_295 = ('Bij deze hint zie je het bouwwerk van boven, als plattegrond. In elk vakje staat hoeveel blokjes daar op elkaar staan. '
          'Ook de blokjes die je in de tekening niet ziet, tellen mee. Een leeg vakje heeft geen toren. Tel alle getallen bij elkaar op.')
def na299_295(it):
    if it['merge'].get('doel') != 'G6-MKU-E03': return
    st = (it['visual']['jsRender'] or {}).get('stapels')
    if not isinstance(st, list): return
    hs = [x for r in st for x in r if x > 0]; tot, hoog, achter = sum(hs), max(hs), _achter299(st)
    n = 1 if tot <= 20 and hoog <= 3 and achter < 3 else (3 if tot >= 38 or (it['visual'].get('tekeneis') == 'B' and achter >= 3) else 2)      # #344: basis alleen met < 3 torens achter een hogere
    oud = (it['niveau'], it['niveauKind']); it['niveau'], it['niveauKind'] = NIVEAU299[n]
    it['merge']['niveau299'] = {'niveau': n, 'blokjes': tot, 'hoogsteToren': hoog, 'torensAchterHoger': achter, 'tekeneis': it['visual'].get('tekeneis'), 'voor': list(oud)}

_bewerk_na_oud = bewerk_na
def bewerk_na(it):
    na254(it)                                   # ronde 8b: #254 (852) vóór #251 (niveau)
    _bewerk_na_oud(it)
    na278(it); na280(it); na276(it); assert290(it); na299_295(it); na_verhuis261(it)

# ------------------------------------------------------------------ #252 (recheck 3d/4c): antwoordplek bij 'kleinst' gelijk verdelen (na alle items, vóór de dubbelcheck)
def na252(rows):
    its = sorted([it for it in rows if it['merge'].get('doel') == 'G6-GET-E03' and (m := VRAAG251.match(it['opgave'] or '')) and m.group(1) == 'kleinst'], key=lambda x: x['id'])
    n = len(its); quota = [n // 3 + (1 if i < n % 3 else 0) for i in range(3)]; plek = {}
    for it in its:
        m = VRAAG251.match(it['opgave']); br = [m.group(2), m.group(3), m.group(4)]; plek[it['id']] = (br, br.index(str(it['antwoord'])))
    tel = [0, 0, 0]; weg = []
    for it in its:
        br, p = plek[it['id']]
        if tel[p] < quota[p]: tel[p] += 1
        else: weg.append(it)
    for it in weg:
        br, p = plek[it['id']]; q = next(i for i in range(3) if tel[i] < quota[i]); tel[q] += 1
        ant = br[p]; rest = [b for b in br if b != ant]; nw = rest[:q] + [ant] + rest[q:]
        o = it['opgave']; it['opgave'] = f"Welke breuk is het kleinst? Kies uit {nw[0]}, {nw[1]} of {nw[2]}."
        it['merge']['antwoordplek252'] = {'oud': o, 'van': p + 1, 'naar': q + 1}
        _log(punt=252, id=it['id'], oud=o, nieuw=it['opgave'])
    uit = collections.Counter(list(VRAAG251.match(it['opgave']).groups()[1:]).index(str(it['antwoord'])) for it in its)
    assert len(uit) == 3 and max(uit.values()) - min(uit.values()) <= 1, ('#252: plekken niet gelijk verdeeld', uit)
    return [uit[0], uit[1], uit[2]]
def na_alle(rows):
    """ronde 8b: stappen over alle items (na de bevroren ids en de aanvulling uit G8, vóór de dubbelcheck)."""
    _log(punt=252, plekken=na252(rows))
    for it in rows:
        if not it['merge'].get('niveau299'): na299_295(it)      # #299: MKU-E03 komt uit de aanvulling uit G8 (geen bewerk_na)
    assert callable(globals().get('aanvul231')), '#231/#281: aanvul231 ontbreekt in fixlijst_g6.py (box-storing 1 okt); nooit stil overslaan'
    for it in rows: na235(it)      # ronde 9 #235: ook de MKU-E01-items uit de aanvulling uit G8 (die krijgen geen bewerk_na)
    rows += aanvul231(rows)
    rows += laad321(rows)      # ronde 9: G5-GET-E07 #6 (TT × TT schatten) → G6-GET-E06 (#321/#354)
    guards_r9(rows)
    return rows

# ================================================================== ronde 9 (8 okt; Didactiek recheck-ronde5c V-#331, Z-#332/#333, recheck-ronde4d6b Z-#344, #231/#281, #235, #276, #321/#354)
# Uitgevoerd door Overzicht. Alles in de build; guards_r9 geeft FAIL (AssertionError) en stopt de build.
from fractions import Fraction as _Fr
DOOR9 = 'Overzicht (G6-fixlijst ronde 9, 8 okt)'

# ---- #333 (motor + entries): VBN-E02 #1 'de andere maand uit de vraag' vóór ± één streepje; VBN-E02 #3 'de som van een deel van de maanden'
TEKST330 = ('Dat is het aantal van één maand uit de vraag. De vraag is hoeveel meer het in de ene maand was dan in de andere. '
            'Haal het kleinste aantal van het grootste aantal af.')      # Didactiek V-#330 (recheck-ronde5c), voor 'de tweede maand' én 'de andere maand'
def _e333(st):
    fh = st['foutHints']; k = (st['doel'], st.get('nrOrigineel'))
    if k == ('G6-VBN-E02', 1) and not any(f['regel'] == 'fout = de andere maand uit de vraag' for f in fh):
        i = next(i for i, f in enumerate(fh) if f['regel'] == 'fout = de tweede maand uit de vraag') + 1
        nieuw = dict(_fb('fout = de andere maand uit de vraag', 'de andere maand (regel)', TEKST330, None, 'Didactiek V-#330/Z-#333 (recheck-ronde5c)'), door=DOOR9)
        st['foutHints'] = fh[:i] + [nieuw] + fh[i:]
        _log(punt=333, entry='G6-VBN-E02 #1', nieuw=nieuw['regel'], na='fout = de tweede maand uit de vraag')
    if k == ('G6-VBN-E02', 3) and not any(f['regel'] == 'fout = de som van een deel van de maanden' for f in fh):
        bron = next(f for f in fh if f.get('soort') == 'een paar maanden')
        i = next(i for i, f in enumerate(fh) if f['regel'] == 'andere fout')
        nieuw = dict(_fb('fout = de som van een deel van de maanden', 'een paar maanden (regel)', bron['tekst'], bron.get('tekstSterker'), "tekst van 'een paar maanden' in de entry (Oefeningen)"), door=DOOR9)
        st['foutHints'] = fh[:i] + [nieuw] + fh[i:]
        _log(punt=333, entry='G6-VBN-E02 #3', nieuw=nieuw['regel'], voor='andere fout')
_pas_entries_ronde8_r8b = pas_entries_ronde8
def pas_entries_ronde8(st):
    _pas_entries_ronde8_r8b(st)
    _e333(st)

# ---- #276 (bordtitel in de merge-data): geen beelddiagram/cirkeldiagram; het canonieke bord (rekenen-groep6/bank) is voor Leerlijn
BORD276 = {'G6-VBN-E02': 'Lijngrafiek aflezen'}
BORD217 = dict(BORD217, **BORD276)

# ---- #235 (G6, besluit Didactiek): MKU-E01 #3 (vak G#) en #4 (vak H#) zijn #1 met een vaste letter → samen onder #1 (hints/koppeling_merge.json)
KOP235 = {'[plattegrond] Wat staat er in vak G#?': '[plattegrond] Wat staat er in vak [vak]?', '[plattegrond] Wat staat er in vak H#?': '[plattegrond] Wat staat er in vak [vak]?'}
def na235(it):
    if it['merge'].get('doel') != 'G6-MKU-E01' or it['merge'].get('somtype') not in KOP235: return
    oud = it['merge']['somtype']; it['merge']['somtype'] = KOP235[oud]
    it['merge']['samengevoegd235'] = {'van': oud, 'naar': it['merge']['somtype'], 'besluit': 'Didactiek batch 6 #235; de entries van #1, #3 en #4 zijn gelijk (koppeling_merge.json)'}
    _log(punt=235, claudeId=it['bron']['claudeId'], van=oud)

# ---- #331 (verplicht): VERH-E01 #1, nieuwe getallen voor 001–004 (Didactiek V-#331, letterlijk); daarna de guard voor beide routes en elk vakje
def _claude9(it, sleutels):
    ev = it['extraVelden']; sl = [(str(v), lab, u) for v, lab, u in sleutels]
    assert len({v for v, _, _ in sl}) == len(sl) and str(it['antwoord']) not in {v for v, _, _ in sl}, ('sleutels dubbel of = antwoord', it.get('id'), sl)
    ev['claudeFoutHints'] = [{'stap': None, 'fout': v, 'uitleg': u} for v, _, u in sl]
    ev['claudeDenkfouten'] = [{'fout': v, 'denkfout': lab} for v, lab, _ in sl if lab]
    ev['mergeFoutHints'] = []
    it['foutHints'] = [{'stap': None, 'fout': v, 'uitleg': u} for v, _, u in sl]
def _mc9(it, opties):
    it['opties'] = [{'letter': 'ABCD'[i], 'tekst': t} for i, t in enumerate(opties)]
    it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    goed = [o for o in it['opties'] if o['tekst'] == it['antwoord']]; assert len(goed) == 1, ('MC', it.get('id'), opties)
    it['antwoordDetail'] = dict(it.get('antwoordDetail') or {}, juisteOptie=goed[0]['letter'], juisteOptieTekst=it['antwoord'])
U_OPG = 'Heb je er iets bij opgeteld? Kijk hoeveel keer zo groot het aantal in de vraag is.'
U_VAK = 'Ben je al bij het vakje uit de vraag? Ga verder in de tabel.'
U_GET = 'Dat getal staat al in de vraag. Reken uit wat er bij het vakje uit de vraag hoort.'
NIEUW331 = {   # claudeId[:8]: (oud stuk, nieuw stuk, antwoord, opties in volgorde, sleutels [(waarde, Claude-label)], uitleg)
    '63102a04': (('bij 8 kg appels',), ('bij 10 kg appels',), '€15', ['€6', '€15', '€11'], [('€11', 'optellen-ipv-vermenigvuldigen'), ('€6', 'verhoudingstabel-verkeerd')],
                 'Van 2 kg naar 10 kg is 5 keer zoveel. Dan wordt de prijs ook 5 keer zo hoog. 5 × €3 is €15.'),
    '78d2c8c5': (('betaal je €6.',), ('betaal je €4.',), '€8', ['€8', '€7', '€4'], [('€7', 'optellen-ipv-vermenigvuldigen'), ('€4', 'getal-overgenomen')],
                 'Van 3 broden naar 6 broden is keer 2. In de tabel doe je met de prijs hetzelfde. Dus €4 keer 2 is €8.'),
    '99f70279': (('kun je 3 glazen',), ('kun je 4 glazen',), '24 glazen', ['24 glazen', '10 glazen', '4 glazen'], [('10 glazen', 'optellen-ipv-vermenigvuldigen'), ('4 glazen', 'getal-overgenomen')],
                 'Elk pak geeft 4 glazen. Bij 6 pakken doe je 6 × 4. Dat zijn 24 glazen.'),
    'e5a7d298': (('1 fles is 2 L.',), ('1 fles is 3 L.',), '15 L', ['15 L', '8 L', '5 L'], [('8 L', 'optellen-ipv-vermenigvuldigen'), ('5 L', 'getal-overgenomen')],
                 'In de tabel staat 1 fles bij 3 L. Bij 5 flessen doe je 5 × 3. Dat is 15 L.')}
U_LAB = {'optellen-ipv-vermenigvuldigen': U_OPG, 'verhoudingstabel-verkeerd': U_VAK, 'getal-overgenomen': U_GET}
def na331(it):
    if it['merge'].get('doel') != 'G6-VERH-E01' or (k := it['bron']['claudeId'][:8]) not in NIEUW331: return
    oud_s, nieuw_s, ans, opties, sl, uitleg = NIEUW331[k]; o = it['opgave']
    for a, b in zip(oud_s, nieuw_s): assert a in it['opgave'], ('#331', k, it['opgave']); it['opgave'] = it['opgave'].replace(a, b)
    oud_ans = it['antwoord']; it['antwoord'] = ans; _mc9(it, opties)
    _claude9(it, [(v, lab, U_LAB[lab]) for v, lab in sl]); it['extraVelden']['claudeUitleg'] = uitleg
    if it.get('controle', {}).get('verwacht') is not None: it['controle']['verwacht'] = ans
    it['merge']['getallen331'] = {'oud': {'opgave': o, 'antwoord': oud_ans}, 'nieuw': {'opgave': it['opgave'], 'antwoord': ans}, 'door': 'Didactiek V-#331 (recheck-ronde5c)'}
    _log(punt=331, claudeId=it['bron']['claudeId'], oud=o, nieuw=it['opgave'], antwoord=f'{oud_ans} → {ans}')

_bewerk_na_r8b = bewerk_na
def bewerk_na(it):
    _bewerk_na_r8b(it)
    na235(it); na331(it)

# ---- guard #331 (V-#331, les 90): voor elk item van VERH-E01 #1 en elke route in de regel, en elk vakje van de tabel
NUM331 = re.compile(r'\d+(?:,\d+)?')
def _waarde(t):
    m = re.search(r'\d+(?:,\d+)?', str(t)); return _Fr(m.group(0).replace(',', '.')) if m else None
def verh331(it):
    """-> (x1, y1, x2, antwoord, vakjes, routes) zoals de motor de getallen leest (de eerste drie getallen van de opgave)."""
    n = [_Fr(x.replace(',', '.')) for x in NUM331.findall(it['opgave'])][:3]
    x1, y1, x2 = n; r = y1 / x1; ans = _waarde(it['antwoord'])
    xs = {1} | set(range(int(min(x1, x2)), int(max(x1, x2)) + 1))
    vak = {r * x for x in xs if (r * x * 100).denominator == 1}
    routes = {'y1 + (x2 − x1)': y1 + (x2 - x1), 'y1 + x2': y1 + x2} if x2 > x1 else {}
    return x1, y1, x2, ans, vak, routes
def guard331(G, kop1):
    tel = 0
    for it in G:
        if it['merge'].get('doel') != 'G6-VERH-E01' or it['merge'].get('somtype') != kop1: continue
        x1, y1, x2, ans, vak, routes = verh331(it); tel += 1
        assert ans == y1 * x2 / x1, ('#331: antwoord past niet bij de tabel', it['id'], it['opgave'], it['antwoord'])
        assert x2 > x1, ('#331: terug in de tabel (x2 < x1) vraagt een regel \'eraf\'; die bestaat nog niet', it['id'])
        for naam, v in routes.items():
            assert v != ans, ('#331: optellen geeft het goede antwoord', it['id'], naam, v)
            assert v not in vak, ('#331: optellen geeft een goed vakje van de tabel', it['id'], naam, v, sorted(vak))
        for d in it['extraVelden'].get('claudeDenkfouten') or []:
            if d['denkfout'] == 'optellen-ipv-vermenigvuldigen': assert _waarde(d['fout']) in routes.values(), ('#331: opgeteld-sleutel is geen optelroute', it['id'], d['fout'])
    return tel

# ---- #231/#281 (Didactiek: aanvullen, niet samenvoegen): VERH-E01 #1 tot 15, VERH-E02 #3 tot 10 (beide richtingen), VERH-E02 #4 tot 10. Geen schaal.
GEN231_E01 = [   # (opgave met {x1} {y1} {x2}, x1, y1, x2, eenheid ('€' of ' woord'), opgeteld-route, derde optie ('vak', x) of ('getal',))
    ('Voor {x1} pannenkoeken heb je {y1} eieren nodig. Je zet dat in een verhoudingstabel. Hoeveel eieren heb je nodig voor {x2} pannenkoeken?', 4, 2, 12, ' eieren', 1, ('vak', 8)),
    ('{x1} schriften kosten €{y1}. Je zet dat in een verhoudingstabel. Wat hoort er in het vakje bij {x2} schriften?', 3, 4, 9, '€', 1, ('vak', 6)),
    ('In {x1} doos zitten {y1} eieren. Je zet dat in een verhoudingstabel. Hoeveel eieren zitten er in {x2} dozen?', 1, 6, 5, ' eieren', 2, ('getal',)),
    ('Met {x1} pak sap kun je {y1} glazen inschenken. Je zet dat in een verhoudingstabel. Hoeveel glazen krijg je van {x2} pakken?', 1, 5, 4, ' glazen', 1, ('vak', 3)),
    ('Voor {x1} glazen limonade heb je {y1} citroenen nodig. Je zet dat in een verhoudingstabel. Hoeveel citroenen heb je nodig voor {x2} glazen limonade?', 4, 3, 12, ' citroenen', 1, ('vak', 8)),
    ('{x1} kaartjes voor het zwembad kosten €{y1}. Je zet dat in een verhoudingstabel. Wat kosten {x2} kaartjes?', 2, 5, 6, '€', 1, ('vak', 4)),
    ('Voor {x1} taarten heb je {y1} appels nodig. Je zet dat in een verhoudingstabel. Hoeveel appels heb je nodig voor {x2} taarten?', 2, 5, 8, ' appels', 1, ('vak', 4)),
    ('{x1} emmer is {y1} L. Je zet dat in een verhoudingstabel. Hoeveel liter is {x2} van die emmers?', 1, 10, 6, ' L', 2, ('vak', 3)),      # ronde 10b Z-#511: een emmer is ongeveer 10 L (was 4 L)
    ('Voor {x1} kinderen heb je {y1} broden nodig. Je zet dat in een verhoudingstabel. Hoeveel broden heb je nodig voor {x2} kinderen?', 4, 3, 8, ' broden', 1, ('getal',)),
    ('In {x1} zak zitten {y1} knikkers. Je zet dat in een verhoudingstabel. Hoeveel knikkers zitten er in {x2} zakken?', 1, 8, 5, ' knikkers', 2, ('getal',)),
    ('{x1} pakken melk kosten €{y1}. Je zet dat in een verhoudingstabel. Wat hoort er in het vakje bij {x2} pakken melk?', 3, 2, 12, '€', 1, ('vak', 6))]
GEN231_STROOK = [   # (opgave, antwoord, [afleiders met hun Claude-label], niveau). Afleiders zijn de letterlijke regels van de entry ('een derde', '3 hokjes' …),
    # alleen waar hun tekst bij de vraag past; een helft-afleider zonder eigen regel krijgt 'andere fout' (de tekst daarvan klopt).
    ('Je hebt een strook van 9 hokjes. Je kleurt er 3 in. Welk deel van de strook is gekleurd?', 'een derde', [('drie hele stroken', 'getal-overgenomen'), ('de helft', 'deel-van-geheel-verkeerd')], 'basis'),
    ('Je hebt een strook van 15 hokjes. Je kleurt er 3 in. Welk deel van de strook is gekleurd?', 'een vijfde', [('een derde', 'deel-van-geheel-verkeerd'), ('drie hele stroken', 'getal-overgenomen')], 'toepassen'),
    ('Je hebt een strook van 18 hokjes. Je kleurt er 3 in. Welk deel van de strook is gekleurd?', 'een zesde', [('een derde', 'deel-van-geheel-verkeerd'), ('de helft', 'deel-van-geheel-verkeerd')], 'toepassen'),
    ('Van de 30 kinderen in de klas heeft een derde een huisdier. Je tekent een strook van 30 hokjes. Hoeveel hokjes kleur je?', '10 hokjes', [('3 hokjes', 'getal-overgenomen'), ('15 hokjes', 'andere-deel-genomen')], 'basis'),
    ('Van de 12 appels in de fruitmand is een kwart rood. Je tekent een strook van 12 hokjes. Hoeveel hokjes kleur je?', '3 hokjes', [('4 hokjes', 'getal-overgenomen'), ('6 hokjes', 'andere-deel-genomen')], 'basis'),
    ('Van de 28 kinderen op het plein speelt een kwart tikkertje. Je tekent een strook van 28 hokjes. Hoeveel hokjes kleur je?', '7 hokjes', [('4 hokjes', 'getal-overgenomen'), ('14 hokjes', 'andere-deel-genomen')], 'toepassen')]
STROOK_OK = {'drie hele stroken': lambda o: 'Je kleurt er 3 in' in o, 'een derde': lambda o: 'Welk deel' in o, 'een zestiende': lambda o: 'Welk deel' in o, 'de helft': lambda o: 'Welk deel' in o,
             '3 hokjes': lambda o: 'een derde' in o, '4 hokjes': lambda o: 'een kwart' in o, '12 hokjes': lambda o: 'een derde' in o and 'strook van 24' in o,
             '10 hokjes': lambda o: 'een kwart' in o and 'strook van 20' in o}
GEN231_DEEL = [   # (opgave, N, teller, noemer)
    ('Op het schoolfeest zijn 180 kinderen. 2/5 ervan doet mee aan de spelletjes. Hoeveel kinderen doen mee aan de spelletjes?', 180, 2, 5),
    ('In de bibliotheek staan 420 boeken. 1/3 ervan is een prentenboek. Hoeveel prentenboeken zijn er?', 420, 1, 3),
    ('Een boer heeft 350 kippen. 3/5 ervan is bruin. Hoeveel kippen zijn bruin?', 350, 3, 5),
    ('In het zwembad zwemmen 96 kinderen. 1/4 ervan heeft een zwembandje. Hoeveel kinderen hebben een zwembandje?', 96, 1, 4),
    ('Op schoolreis gaan 150 kinderen mee. 4/5 ervan neemt een rugzak mee. Hoeveel kinderen nemen een rugzak mee?', 150, 4, 5),
    ('Een bakker bakt 240 koekjes. 5/6 ervan heeft chocola. Hoeveel koekjes hebben chocola?', 240, 5, 6),
    ('In de klas liggen 120 potloden. 2/5 ervan is rood. Hoeveel potloden zijn rood?', 120, 2, 5)]
def _komma(x):
    x = _Fr(x); return str(int(x)) if x.denominator == 1 else (f'{float(x):.1f}'.replace('.', ',') if (x * 10).denominator == 1 else None)
def _fmt9(v, eenheid): v = int(v); return f'€{v}' if eenheid == '€' else f'{v}{eenheid}'
def _gen9(sjab, nr, cid, opgave, antwoord, niveau, reden):
    it = _copy.deepcopy(sjab); d = it['merge']['doel']
    it['id'] = f'{d}-merge-gen-{nr:03d}'; it['nr'] = f'{nr:03d}'; it['opgave'] = opgave; it['antwoord'] = antwoord
    it['niveau'] = niveau; it['niveauKind'] = {'basis': 'Opwarmen', 'toepassen': 'Oefenen'}.get(niveau, it['niveauKind'])
    it['bronVariant'] = f'merge-generator:G6-r9-#231:{cid}'
    it['bron'] = {'bestand': 'scripts/fixlijst_g6.py', 'type': 'merge-generator', 'claudeId': cid, 'claudeDoel': 'merge-generator G6 ronde 9 (#231/#281)', 'claudeDoelTitel': 'geen Claude-item',
                  'claudeGroep': None, 'claudeBron': None, 'claudeVersie': None, 'generator': 'G6-r9 #231/#281 (dunne VERH-somtypen aanvullen, Didactiek recheck-ronde5c)',
                  'sjabloonClaudeId': sjab['bron'].get('claudeId'), 'sjabloonId': sjab['id']}
    it['licentie'] = dict(it['licentie'], gewijzigd=True, wijzigingen=[f"G6-r9 #231 generator (vorm naar het sjabloon {sjab['id']})"])
    it['merge'] = {k: v for k, v in it['merge'].items() if k in ('status', 'doel', 'voorstelDoel', 'somtype', 'duplicaatVan')}
    it['merge'].update(regel='G6-r9 #231 generator', reden=reden, gen231={'sjabloon': sjab['id']})
    it['controle'] = dict(it['controle'], antwoord='ok', verwacht=antwoord, methode='G6-r9 #231 generator (nagerekend in fixlijst_g6.py)',
                          claudeVorm={'antwoord': None, 'verwacht': None, 'methode': 'geen Claude-item'}, foutAntwoordGelijkAanGoed=False)
    it['extraVelden'].update(claudeStrategie=None, claudeThema=None, niveauVoorlopig=True, claudeKaleSom=None)
    return it
def aanvul231(rows):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    def sjab(d, cid8): return next(r for r in G if r['merge'].get('doel') == d and r['bron'].get('claudeId', '').startswith(cid8))
    uit = []; nr = collections.Counter(int(r['id'].rsplit('-', 1)[1]) for r in rows if '-merge-gen-' in r['id'] and False)
    teller = collections.defaultdict(int)
    def nieuw(s, cid, o, a, nv, reden):
        d = s['merge']['doel']; teller[d] += 1; it = _gen9(s, teller[d], cid, o, a, nv, reden); uit.append(it); return it
    s1 = sjab('G6-VERH-E01', '63102a04')
    for i, (t, x1, y1, x2, e, route, derde) in enumerate(GEN231_E01, 1):
        ans = _Fr(y1 * x2, x1); assert ans.denominator == 1 and ans <= 100, ('#231 E01', t)
        opg = y1 + (x2 - x1) if route == 1 else y1 + x2
        d3, lab3 = ((_Fr(y1 * derde[1], x1), 'verhoudingstabel-verkeerd') if derde[0] == 'vak' else (_Fr(y1), 'getal-overgenomen'))
        assert d3.denominator == 1, ('#231 E01 derde', t)
        it = nieuw(s1, f'g6-r9-gen231-verh-e01-{i:02d}', t.format(x1=x1, y1=y1, x2=x2), _fmt9(ans, e), 'basis' if x1 == 1 else 'toepassen', '#231/#281: VERH-E01 #1 aangevuld tot 15 (Didactiek recheck-ronde5c)')
        f = lambda v: _fmt9(v, e)
        it['extraVelden']['claudeUitleg'] = f'Van {x1} naar {x2} is {_Fr(x2, x1)} keer zoveel. Het andere getal ook: {f(y1)} × {_Fr(x2, x1)} = {f(ans)}.' if x1 > 1 else f'{x2} × {f(y1)} = {f(ans)}.'
        _claude9(it, [(f(opg), 'optellen-ipv-vermenigvuldigen', U_OPG), (f(d3), lab3, U_VAK if lab3 == 'verhoudingstabel-verkeerd' else U_GET)])
        _mc9(it, [[f(ans), f(opg), f(d3)], [f(d3), f(ans), f(opg)], [f(opg), f(d3), f(ans)]][i % 3])
    s3 = sjab('G6-VERH-E02', '199e2627')
    for i, (o, a, afl, nv) in enumerate(GEN231_STROOK, 1):
        for v, _ in afl:
            if v in STROOK_OK: assert STROOK_OK[v](o), ('#231 strook: de tekst van de letterlijke regel past niet bij de vraag', o, v)
        it = nieuw(s3, f'g6-r9-gen231-verh-e02-3-{i:02d}', o, a, nv, '#231/#281: VERH-E02 #3 aangevuld tot 10, in twee richtingen (Didactiek recheck-ronde5c)')
        it['extraVelden']['claudeUitleg'] = None
        _claude9(it, [(v, lab, 'Verdeel de strook in gelijke stukken.') for v, lab in afl])
        _mc9(it, [[a, afl[0][0], afl[1][0]], [afl[0][0], a, afl[1][0]], [afl[0][0], afl[1][0], a]][i % 3])
    s4 = sjab('G6-VERH-E02', '00c31a3e')
    for i, (o, N, t, n) in enumerate(GEN231_DEEL, 1):
        assert N % n == 0; stuk = N // n; ans = stuk * t
        sl = []
        if t > 1: sl.append((stuk, 'deel-vergeten-bij-splitsen', 'Dat is één gelijk stuk.'))
        if t > 1 and (w := _komma(_Fr(N, t))) and _Fr(N, t) not in (stuk, ans, N): sl.append((w, 'omgekeerd-gedeeld', 'Deel door de noemer, niet door de teller.'))
        if N - ans not in (stuk, ans): sl.append((N - ans, 'verkeerde-bewerking', 'Dat is wat er overblijft.'))
        it = nieuw(s4, f'g6-r9-gen231-verh-e02-4-{i:02d}', o, str(ans), 'basis' if t == 1 else 'toepassen', '#231/#281: VERH-E02 #4 aangevuld tot 10 (Didactiek recheck-ronde5c)')
        it['extraVelden']['claudeUitleg'] = f'Eerst 1/{n}: {N} : {n} = {stuk}.\nDan {t} keer: {t} × {stuk} = {ans}.'
        it['extraVelden']['claudeKaleSom'] = f'{t}/{n} van {N}'
        _claude9(it, sl)
    for it in uit: _log(punt=231, id=it['id'], opgave=it['opgave'], antwoord=it['antwoord'])
    return uit

# ---- #321/#354 (besluit Dave 1 okt 23:41): G5-GET-E07 #6 'TT × TT schatten' → G6-GET-E06 (de G6-bank: ×/: tot 10.000, ook schattend; 2-cijferig × 2-cijferig met een rond getal)
G5_PARK = '/workspace/claude-merge/g5/data/geparkeerd_G6.json'
def is321(p5): return bool((p5 or {}).get('merge', {}).get('besluit321'))
def laad321(rows):
    import json as _j
    P = sorted((x for x in _j.load(open(G5_PARK))['items'] if is321(x)), key=lambda x: x['id'])
    assert len(P) == 10, ('#321: verwacht 10 items van G5-GET-E07 #6 in g5/data/geparkeerd_G6.json', len(P))
    uit = []
    for i, p in enumerate(P, 1):
        it = _copy.deepcopy(p); g5id = it['id']
        it['id'] = f'G6-GET-E06-claude-bank-uitg5-{i:03d}'; it['nr'] = f'uitg5-{i:03d}'; it['doelId'] = 'G6-GET-E06'
        it['merge'].update(status='gemapt', doel='G6-GET-E06', voorstelDoel=None, somtype=p['merge']['besluit321']['somtypeG5'],
                           regel='G6-r9 #321 (uit G5)', reden='#321/#354: TT × TT schatten is G6-stof (besluit Dave 1 okt 23:41)', uitG5={'id': g5id, 'besluit': p['merge']['besluit321']})
        for k in ('somtypeNr', 'somtypeNrOrigineel', 'somtypeOrigineel', 'hints', 'duplicaatVan'): it['merge'].pop(k, None)
        it['getallenruimte'] = '0–10.000'; it['niveau'] = 'toepassen'; it['niveauKind'] = 'Oefenen'
        it['merge']['niveau321'] = {'oud': p['niveau'], 'waarom': 'twee getallen afronden en daarna een keersom met nullen (Didactiek #321: minstens toepassen); recheck in G6 volgt'}
        it['hint'] = None; it['sterkereHint'] = None; it['ouderzin'] = None
        uit.append(it); _log(punt=321, id=it['id'], uitG5=g5id, opgave=it['opgave'])
    return uit

def guards_r9(rows):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    ids = [r['id'] for r in rows]; assert len(ids) == len(set(ids)), ('ids dubbel', sorted({i for i in ids if ids.count(i) > 1})[:5])
    kop1 = next(r['merge']['somtype'] for r in G if r['bron'].get('claudeId', '').startswith('63102a04'))
    kop3 = next(r['merge']['somtype'] for r in G if r['bron'].get('claudeId', '').startswith('199e2627'))
    kop4 = next(r['merge']['somtype'] for r in G if r['bron'].get('claudeId', '').startswith('00c31a3e'))
    n1 = guard331(G, kop1)
    tel = collections.Counter((r['merge']['doel'], r['merge']['somtype']) for r in G)
    assert 12 <= n1 == tel[('G6-VERH-E01', kop1)] <= 15, ('#231: VERH-E01 #1 niet 12–15 items', n1)
    assert tel[('G6-VERH-E02', kop3)] >= 9, ('#231: VERH-E02 #3 nog dun', tel[('G6-VERH-E02', kop3)])
    assert tel[('G6-VERH-E02', kop4)] >= 9, ('#231: VERH-E02 #4 nog dun', tel[('G6-VERH-E02', kop4)])
    richting = collections.Counter('deel' if 'Welk deel' in r['opgave'] else 'hokjes' for r in G if (r['merge']['doel'], r['merge']['somtype']) == ('G6-VERH-E02', kop3))
    assert min(richting.values()) >= 4 and len(richting) == 2, ('#231: VERH-E02 #3 niet in twee richtingen', dict(richting))
    for r in G:
        if r['merge']['doel'] in ('G6-VERH-E01', 'G6-VERH-E02', 'G6-VERH-E03'): assert 'schaal' not in (r['opgave'] or '').lower(), ('#231: geen schaal', r['id'])
    st = collections.Counter(r['merge']['grafiek276']['streepjes'] for r in G if r['merge'].get('doel') == 'G6-VBN-E02' and (r['merge'].get('grafiek276') or {}).get('streepjes'))
    assert sorted(st) == [1, 2, 3, 4, 5] and max(st.values()) - min(st.values()) <= 1, ('#276: VBN-E02 #1 niet gelijk verdeeld over 1–5 streepjes', dict(st))
    assert sum(1 for r in G if r['merge'].get('doel') == 'G6-GET-E06' and r['merge'].get('uitG5')) == 10, '#321'
    assert not any(r['merge'].get('doel') == 'G6-MKU-E01' and r['merge'].get('somtype') in KOP235 for r in G), '#235'
    _log(punt='r9-guards', verh_e01_1=n1, streepjes=dict(st))

# ================================================================== ronde 10 (8 okt; Didactiek gate ronde 9 deel A en B: V-#380, Z-#381, Z-#382, Z-#383, V-#390, hm/dl)
# Uitgevoerd door Overzicht. #380 en #390 zitten in de motor (fout_regels.py: lett_past/lett_guard, _regels_r10, in_vraag390/is_pm1_390), gelijk in G5–G8.
DOOR10 = 'Overzicht (G6-fixlijst ronde 10, 8 okt)'

# ---- #381 (Z-#381, les 112): VBN-E02 #1, plek van het antwoord tussen de opties (kleinste/middelste/grootste) gelijk verdeeld.
# Een sleutel die groter is dan het antwoord ('de tweede maand', 'opgeteld', '+ één streepje') wordt een kleinere ('streepjes geteld' A : perstreep,
# 'één streepje te weinig' A − perstreep), met het label dat bij de motorregel hoort; de Claude-tekst van de oude sleutel vervalt (die past niet meer).
KLEIN381 = (('A:ps', 'streepjes-geteld'), ('A-1ps', 'een-streepje-te-weinig'))
GROOT381 = ('A+1ps', 'som2', 'tweede')      # volgorde: eerst de zwakste route vervangen, 'de tweede maand' (V-#330) het langst houden
def _plek381(it):
    A = int(it['antwoord']); ks = [int(o['tekst']) for o in it['opties'] if o['tekst'] != it['antwoord']]
    return ('klein', 'midden', 'groot')[sum(k < A for k in ks)]
def na381(rows):
    its = sorted((r for r in rows if r['merge'].get('status') == 'gemapt' and r['merge'].get('doel') == 'G6-VBN-E02' and ' meer dan ' in (r['opgave'] or '')),
                 key=lambda r: _h(f"{r['bron']['claudeId']}-381"))
    if not its: return 0
    def vervang(it, naar_klein):
        A = int(it['antwoord']); ps = it['visual']['jsRender']['perstreep']; sl = it['merge']['grafiek276']['sleutels']
        fam = {v['nieuw']: v['familie'] for v in sl.values()}; huidig = [o['tekst'] for o in it['opties'] if o['tekst'] != it['antwoord']]
        groot = sorted((w for w in huidig if int(w) > A), key=lambda w: GROOT381.index(fam.get(w)) if fam.get(w) in GROOT381 else -1)
        if not groot: return False
        kand = {'A:ps': A // ps if A % ps == 0 else None, 'A-1ps': A - ps}
        for f, lab in KLEIN381:
            w = kand[f]
            if w and 0 < w < A and str(w) not in huidig:
                oud = groot[0]; _zet_exact(it, {oud: str(w)}); ev = it['extraVelden']
                for d in ev.get('claudeDenkfouten') or []:
                    if d['fout'] == str(w): d.update(denkfout=lab, denkfoutVoor381=fam.get(oud))
                ev['claudeFoutHints'] = [x for x in ev.get('claudeFoutHints') or [] if x['fout'] != str(w)]
                rec0 = it['merge'].get('antwoordplek381') or {}
                it['merge']['antwoordplek381'] = {'van': rec0.get('van'), 'oud': {'waarde': oud, 'familie': fam.get(oud)}, 'nieuw': {'waarde': str(w), 'familie': f}, 'door': DOOR10}
                return True
        return False
    # minimaal aantal wijzigingen: klein → midden, daarna midden → groot (elk één sleutel), tot elke plek len/3 heeft (rest: midden, dan groot)
    n = len(its); want = {'klein': n // 3, 'midden': n // 3 + (n % 3 >= 1), 'groot': n // 3 + (n % 3 >= 2)}
    for van, naar in (('klein', 'midden'), ('midden', 'groot')):
        for it in its:
            plek = collections.Counter(_plek381(r) for r in its)
            if _plek381(it) != van: continue
            if naar == 'midden' and plek[van] <= want[van]: break
            if naar == 'groot' and plek['groot'] >= want['groot']: break
            if vervang(it, True):
                rec = it['merge']['antwoordplek381']; rec['van'] = van if not rec.get('van') else rec['van']; rec['naar'] = _plek381(it)
                _log(punt=381, id=it['id'], van=van, naar=_plek381(it), sleutel=rec)
    plek = collections.Counter(_plek381(r) for r in its)
    assert max(plek.values()) - min(plek.values()) <= 1 and len(plek) == 3, ('#381: plek van het antwoord niet gelijk verdeeld', dict(plek))
    return dict(plek)

# ---- #382 (Z-#382, les 48/114): VERH-E01 #1 drie items met een tussenstap via een vakje (geen hele factor), niveau kritisch.
GEN382 = [   # (opgave, x1, y1, x2, eenheid, tussenvakje x)
    ('{x1} kaartjes kosten €{y1}. Je zet dat in een verhoudingstabel. Wat kosten {x2} kaartjes?', 4, 6, 6, '€', 2),
    ('Voor {x1} pannenkoeken heb je {y1} eieren nodig. Je zet dat in een verhoudingstabel. Hoeveel eieren heb je nodig voor {x2} pannenkoeken?', 6, 4, 9, ' eieren', 3),
    ('{x1} schriften kosten €{y1}. Je zet dat in een verhoudingstabel. Wat hoort er in het vakje bij {x2} schriften?', 6, 9, 10, '€', 2)]
def aanvul382(rows):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    s1 = next(r for r in G if r['merge'].get('doel') == 'G6-VERH-E01' and r['bron'].get('claudeId', '').startswith('63102a04'))
    nr0 = max(int(r['id'].rsplit('-', 1)[1]) for r in rows if r['id'].startswith('G6-VERH-E01-merge-gen-'))
    uit = []
    for i, (t, x1, y1, x2, e, xv) in enumerate(GEN382, 1):
        ans = _Fr(y1 * x2, x1); tv = _Fr(y1 * xv, x1); opg = y1 + (x2 - x1)
        assert ans.denominator == 1 and tv.denominator == 1 and (x2 % x1) and xv < x1 and x1 % xv == 0 and x2 % xv == 0, ('#382: geen tussenstap via een vakje', t)
        it = _gen9(s1, nr0 + i, f'g6-r10-gen382-verh-e01-{i:02d}', t.format(x1=x1, y1=y1, x2=x2), _fmt9(ans, e), 'kritisch', '#382: VERH-E01 #1 met een tussenstap via een vakje (Didactiek gate ronde 9 deel A)')
        it['niveauKind'] = 'Uitdaging'; it['bronVariant'] = f'merge-generator:G6-r10-#382:{it["bron"]["claudeId"]}'
        it['bron'].update(claudeDoel='merge-generator G6 ronde 10 (#382)', generator='G6-r10 #382 (VERH-E01 tussenstap, Didactiek gate ronde 9 deel A)')
        it['merge'].update(regel='G6-r10 #382 generator', gen382={'sjabloon': s1['id'], 'tussenvakje': xv}); it['merge'].pop('gen231', None)
        f = lambda v: _fmt9(v, e)
        it['extraVelden']['claudeUitleg'] = f'Van {x1} naar {xv} is delen door {x1 // xv}: {f(y1)} : {x1 // xv} = {f(tv)}.\nVan {xv} naar {x2} is keer {x2 // xv}: {f(tv)} × {x2 // xv} = {f(ans)}.'
        _claude9(it, [(f(opg), 'optellen-ipv-vermenigvuldigen', U_OPG), (f(tv), 'verhoudingstabel-verkeerd', U_VAK)])
        _mc9(it, [[f(ans), f(opg), f(tv)], [f(tv), f(ans), f(opg)], [f(opg), f(tv), f(ans)]][i % 3])
        uit.append(it); _log(punt=382, id=it['id'], opgave=it['opgave'], antwoord=it['antwoord'])
    return uit

# ---- #383 (Z-#383): GET-E06 #8 (uit G5): sleutels die niet uit een afrondroute komen → wel een afrondroute
SLEUTEL383 = {'G6-GET-E06-claude-bank-uitg5-001': ('800', '600', '18 × 54: 10 × 60 (18 de verkeerde kant op afgerond)'),
              'G6-GET-E06-claude-bank-uitg5-005': ('900', '1000', '44 × 19: 50 × 20 (44 de verkeerde kant op afgerond)')}
def na383(rows):
    n = 0
    for it in rows:
        if it['id'] in SLEUTEL383:
            o, w, waarom = SLEUTEL383[it['id']]; ev = it['extraVelden']
            assert any(x['fout'] == o for x in ev.get('claudeFoutHints') or []) and str(it['antwoord']) != w, ('#383', it['id'])
            for k in ('claudeFoutHints', 'claudeDenkfouten', 'mergeFoutHints'):
                for x in ev.get(k) or []:
                    if x['fout'] == o: x['fout'] = w
            for x in it.get('foutHints') or []:
                if x['fout'] == o: x['fout'] = w
            it['merge']['sleutel383'] = {'oud': o, 'nieuw': w, 'route': waarom, 'door': DOOR10}; n += 1; _log(punt=383, id=it['id'], oud=o, nieuw=w)
    assert n == 2, ('#383', n)
    return n

# ---- hm/dl (Leerlijn #217/#261, SLO; entries van Oefeningen in hints/patch_batch4.py HMDL, koppeling op de kop): 8 somtypes × 8 items
HMDL10 = {('G6-MEET-E01', '# hm = □ m'): (100, True, [3, 7, 12, 25, 40, 58, 64, 90]), ('G6-MEET-E01', '# m = □ hm'): (100, False, [400, 900, 1200, 2500, 3600, 5000, 7300, 8800]),
          ('G6-MEET-E01', '# km = □ hm'): (10, True, [2, 5, 8, 13, 24, 37, 46, 75]), ('G6-MEET-E01', '# hm = □ km'): (10, False, [30, 60, 90, 120, 250, 380, 470, 640]),
          ('G6-MEET-E04', '# L = □ dl'): (10, True, [2, 4, 7, 9, 15, 23, 36, 48]), ('G6-MEET-E04', '# dl = □ L'): (10, False, [20, 50, 80, 110, 160, 240, 350, 470]),
          ('G6-MEET-E04', '# dl = □ ml'): (100, True, [2, 3, 5, 8, 12, 25, 40, 64]), ('G6-MEET-E04', '# ml = □ dl'): (100, False, [300, 600, 900, 1400, 2000, 3500, 4200, 7600])}
def _punt10(n): return f'{n:,}'.replace(',', '.') if n >= 10000 else str(n)
def aanvul_hmdl(rows):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    sj = {d: next(r for r in sorted(G, key=lambda r: r['id']) if r['merge'].get('doel') == d and r['merge'].get('somtypeNrOrigineel', 1) == 1 and r['type'] != 'meerkeuze' and re.fullmatch(r'[\d.]+ \w+ = □ \w+', r['opgave'] or ''))
          for d in ('G6-MEET-E01', 'G6-MEET-E04')}
    teller = collections.Counter(int(r['id'].rsplit('-', 1)[1]) for r in rows if '-merge-gen-' in r['id'] and r['merge'].get('doel') in sj)
    nxt = {d: max([int(r['id'].rsplit('-', 1)[1]) for r in rows if r['id'].startswith(f'{d}-merge-gen-')] or [0]) for d in sj}
    uit = []
    for (d, kop), (F, keer, xs) in HMDL10.items():
        van, naar = re.match(r'# (\w+) = □ (\w+)', kop).groups()
        for j, x in enumerate(xs, 1):
            a = x * F if keer else x // F; assert keer or x % F == 0
            nxt[d] += 1; o = kop.replace('#', _punt10(x), 1)
            it = _gen9(sj[d], nxt[d], f'g6-r10-hmdl-{van}-{naar}-{j:02d}', o, _punt10(a), 'toepassen', f'hm/dl (Leerlijn #217/#261): {kop}')
            it['bronVariant'] = f'merge-generator:G6-r10-hmdl:{it["bron"]["claudeId"]}'
            it['bron'].update(claudeDoel='merge-generator G6 ronde 10 (hm/dl)', generator='G6-r10 hm/dl (entries Oefeningen ronde 9, patch_batch4.py HMDL)')
            it['merge'].update(somtype=kop, regel='G6-r10 hm/dl generator', genHmdl={'sjabloon': sj[d]['id'], 'factor': F, 'keer': keer}); it['merge'].pop('gen231', None)
            it['getallenruimte'] = sj[d].get('getallenruimte'); it['type'] = sj[d]['type']; it['opties'] = []; it['optiesTekst'] = None
            for k in ('geldigeAntwoorden', 'antwoordOokGoed'):
                if it.get(k): it[k] = []
            ev = it['extraVelden']; ev['claudeKaleSom'] = o
            ev['claudeUitleg'] = f'1 {van} = {F} {naar}, dus {_punt10(x)} × {F} = {_punt10(a)}.' if keer else f'{F} {van} = 1 {naar}, dus {_punt10(x)} : {F} = {_punt10(a)}.'
            sl = [(_punt10(x), None, 'Je hebt het getal niet omgerekend.')]
            for w in (a * 10, a // 10 if a % 10 == 0 else None):
                if w and w not in (a, x) and _punt10(w) not in [s[0] for s in sl]: sl.append((_punt10(w), None, 'Kijk goed hoeveel nullen erbij of eraf moeten.'))
            _claude9(it, sl); ev['claudeDenkfouten'] = []
            uit.append(it); _log(punt='hmdl', id=it['id'], opgave=o, antwoord=it['antwoord'])
    return uit

_na_alle_r9 = na_alle
def na_alle(rows):
    rows = _na_alle_r9(rows)
    rows += aanvul382(rows)
    na383(rows)
    rows += aanvul_hmdl(rows)
    plek = na381(rows)
    guards_r10(rows, plek)
    return rows

def guards_r10(rows, plek):
    G = [r for r in rows if r['merge'].get('status') == 'gemapt']
    ids = [r['id'] for r in rows]; assert len(ids) == len(set(ids)), ('ids dubbel', sorted({i for i in ids if ids.count(i) > 1})[:5])
    kop1 = next(r['merge']['somtype'] for r in G if r['bron'].get('claudeId', '').startswith('63102a04'))
    n1 = guard331(G, kop1); assert 12 <= n1 <= 18, ('#231/#382: VERH-E01 #1 niet 12–18 items', n1)
    assert sum(1 for r in G if r['merge'].get('gen382') and r['niveau'] == 'kritisch' and r['merge']['somtype'] == kop1) == 3, '#382: drie kritische tussenstap-items'
    import sys as _s10, os as _o10; _s10.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import geldig_check as _GA
    f = _GA.vind(G); assert not f, ('#360: antwoord niet in geldigeAntwoorden', f[:3])
    hm = collections.Counter((r['merge']['doel'], r['merge']['somtype']) for r in G if r['merge'].get('genHmdl'))
    assert len(hm) == 8 and min(hm.values()) >= 8, ('hm/dl: 8 somtypes met elk 8 items', dict(hm))
    for r in G:
        if r['merge'].get('genHmdl'):
            x, a = [int(v.replace('.', '')) for v in re.findall(r'[\d.]+', r['opgave'])[:1]] + [int(r['antwoord'].replace('.', ''))]
            F, keer = r['merge']['genHmdl']['factor'], r['merge']['genHmdl']['keer']
            assert (a == x * F) if keer else (a * F == x), ('hm/dl: antwoord klopt niet', r['id'])
            assert all(not re.fullmatch(r'\d{5,}', v) for v in re.findall(r'\d+', r['opgave'] + ' ' + r['antwoord'])), ('hm/dl: getal vanaf 10.000 zonder punt', r['id'])
    _log(punt='r10-guards', verh_e01_1=n1, plek381=plek, hmdl=sum(hm.values()))

# ======================= ronde 10b (8 okt 11:28; Oefeningen ronde 9 → fixlijst #396–#402, besluit Overzicht #398) =======================
DOOR10B = 'Overzicht (G6 ronde 10b, 8 okt 11:28)'
# ---- #401: GET-E06 #8 uitg5-007 (12 × 18) en uitg5-010 (18 × 13): beide de verkeerde kant op afronden gaf ook het goede antwoord (les 32/82).
# Nieuwe getallen; elke foute route (één of beide getallen de verkeerde kant op) geeft een ander getal dan het antwoord. Guard #301 over G6-GET-E06.
NIEUW401 = {'G6-GET-E06-claude-bank-uitg5-007': (12, 28), 'G6-GET-E06-claude-bank-uitg5-010': (16, 23)}
SCHAT301 = re.compile(r'^Hoeveel is (\d+) × (\d+) ongeveer\? Rond beide getallen af op tientallen')
def _rond10(x): return (x + 5) // 10 * 10
def _fout10(x): return x // 10 * 10 if _rond10(x) > x else x // 10 * 10 + 10      # de verkeerde kant op
def routes301(a, b):
    """-> (goed, {foute route: waarde}) bij 'rond beide getallen af op tientallen'."""
    ra, rb, fa, fb = _rond10(a), _rond10(b), _fout10(a), _fout10(b)
    return ra * rb, {'eerste verkeerd': fa * rb, 'tweede verkeerd': ra * fb, 'beide verkeerd': fa * fb}
def na401(rows):
    import sys as _s, os as _o; _s.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import geldig_check as _GA
    n = 0
    for it in rows:
        if it['id'] not in NIEUW401: continue
        a, b = NIEUW401[it['id']]; m = SCHAT301.match(it['opgave']); assert m, ('#401', it['id'], it['opgave'])
        oud = (int(m.group(1)), int(m.group(2))); goed, fout = routes301(a, b)
        assert a % 10 and b % 10 and goed not in fout.values() and a * b != goed, ('#401: nieuwe getallen', it['id'], a, b, fout)
        it['opgave'] = it['opgave'].replace(f'{oud[0]} × {oud[1]}', f'{a} × {b}', 1); it['antwoord'] = str(goed)
        if 'geldigeAntwoorden' in it: it['geldigeAntwoorden'] = _GA.vormen(it['antwoord'])
        ev = it['extraVelden']; ev['claudeKaleSom'] = f'Hoeveel is {a} × {b} ongeveer?'
        tekst = 'Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.'
        sl = []
        for w in (fout['eerste verkeerd'], fout['tweede verkeerd'], fout['beide verkeerd']):
            if str(w) not in sl and w != goed: sl.append(str(w))
        ev['claudeFoutHints'] = [{'stap': None, 'fout': w, 'uitleg': tekst} for w in sl]
        ev['claudeDenkfouten'] = []; ev['mergeFoutHints'] = []; it['foutHints'] = []
        it['merge']['getallen401'] = {'oud': f'{oud[0]} × {oud[1]}', 'nieuw': f'{a} × {b}', 'antwoord': goed, 'sleutels': sl, 'door': DOOR10B}
        _log(punt=401, id=it['id'], oud=f'{oud[0]} × {oud[1]}', nieuw=f'{a} × {b} ≈ {goed}', sleutels=sl); n += 1
    assert n == 2, ('#401', n)
# ---- #385: VERH-E02 #3 gen-001 (3 van 9 hokjes): afleider 'een negende' (het aantal hokjes als noemer) in plaats van 'de helft'
def na385(rows):
    it = next(r for r in rows if r['id'] == 'G6-VERH-E02-merge-gen-001')
    tk = [o['tekst'] for o in it['opties']]; assert 'de helft' in tk and 'een negende' not in tk and it['antwoord'] == 'een derde', ('#385', tk)
    for o in it['opties']:
        if o['tekst'] == 'de helft': o['tekst'] = 'een negende'
    if it.get('optiesTekst'): it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
    ev = it['extraVelden']
    for k in ('claudeDenkfouten', 'claudeFoutHints', 'mergeFoutHints'):
        for x in ev.get(k) or []:
            if x['fout'] == 'de helft': x['fout'] = 'een negende'
    it['foutHints'] = [f for f in it.get('foutHints') or [] if f['fout'] != 'de helft']
    it['merge']['afleider385'] = {'oud': 'de helft', 'nieuw': 'een negende', 'door': DOOR10B}; _log(punt=385, id=it['id'], oud='de helft', nieuw='een negende')
def guards_r10b(rows):
    n = 0
    for it in rows:
        if it['merge'].get('doel') != 'G6-GET-E06' or not (m := SCHAT301.match(it['opgave'] or '')): continue
        goed, fout = routes301(int(m.group(1)), int(m.group(2))); n += 1
        assert it['antwoord'].replace('.', '') == str(goed), ('#301 (G6-GET-E06): antwoord ≠ beide afgerond', it['id'], it['antwoord'], goed)
        assert goed not in fout.values(), ('#301/#401 (G6-GET-E06): een foute afrondroute geeft het goede antwoord', it['id'], fout)
    it = next(r for r in rows if r['id'] == 'G6-VERH-E02-merge-gen-001'); assert 'de helft' not in [o['tekst'] for o in it['opties']], '#385'
    _log(punt='r10b-guards', schat301=n)
# ---- D-#419 (b): contextitems bij hm en dl (voorstel_hm_dl_r9.md: hardloopbaan in hm, glas in dl). Het eerste getal is het getal dat je omrekent
# (de regels 'niet omgerekend' = getal1 en × 10 / : 10 gelden dan ook hier). Niveau: toepassen zoals de kale items (besluit Leerlijn, #394/#419c).
CTX419 = [('G6-MEET-E01', '# hm = □ m', 4, 'Een hardloopbaan is 4 hm lang. Hoeveel meter is dat?'),
          ('G6-MEET-E01', '# hm = □ m', 6, 'Sam fietst 6 hm naar school. Hoeveel meter fietst Sam?'),
          ('G6-MEET-E01', '# m = □ hm', 800, 'Een wandelroute in het park is 800 m lang. Hoeveel hectometer is dat?'),
          ('G6-MEET-E01', '# km = □ hm', 3, 'Een fietstocht is 3 km lang. Hoeveel hectometer is dat?'),
          ('G6-MEET-E04', '# L = □ dl', 2, 'In een kan zit 2 L limonade. Hoeveel deciliter is dat?'),
          ('G6-MEET-E04', '# dl = □ L', 100, 'In een emmer gaat 100 dl water. Hoeveel liter is dat?'),      # V-#510: een emmer is ongeveer 10 L (referentiematen inhoud-emmer)
          ('G6-MEET-E04', '# dl = □ ml', 2, 'In een glas gaat 2 dl melk. Hoeveel milliliter is dat?'),
          ('G6-MEET-E04', '# ml = □ dl', 200, 'In een pakje zit 200 ml sap. Hoeveel deciliter is dat?')]
def aanvul_ctx419(rows):
    uit = []
    for d, kop, x, o in CTX419:
        sj = next(r for r in sorted(rows, key=lambda r: r['id']) if r['merge'].get('genHmdl') and r['merge']['somtype'] == kop)
        F, keer = sj['merge']['genHmdl']['factor'], sj['merge']['genHmdl']['keer']; van, naar = re.match(r'# (\w+) = □ (\w+)', kop).groups()
        a = x * F if keer else x // F; assert keer or x % F == 0
        n = max(int(r['id'].rsplit('-', 1)[1]) for r in rows + uit if r['id'].startswith(f'{d}-merge-gen-')) + 1
        it = _copy.deepcopy(sj); it['id'] = f'{d}-merge-gen-{n:03d}'; it['nr'] = f'merge-gen-{n:03d}'
        it['opgave'] = o; it['antwoord'] = str(a); it['bron'] = dict(sj['bron'], claudeId=f"g6-r10-ctx419-{van}-{naar}-{x}")
        it['bronVariant'] = f"merge-generator:G6-r10-ctx419:{it['bron']['claudeId']}"
        it['merge'] = dict(sj['merge'], genHmdl=dict(sj['merge']['genHmdl'], context419=True), regel='G6-r10 hm/dl contextitem (D-#419)')
        it['context'] = 'midden'      # Z-#512: een korte context, net als de strook-items
        ev = it['extraVelden']; ev['claudeKaleSom'] = f'{x} {van} = □ {naar}'
        ev['claudeUitleg'] = f'1 {van} = {F} {naar}, dus {x} × {F} = {a}.' if keer else f'{F} {van} = 1 {naar}, dus {x} : {F} = {a}.'
        sl = [(str(x), None, 'Je hebt het getal niet omgerekend.')]
        for w in (a * 10, a // 10 if a % 10 == 0 else None):
            if w and w not in (a, x) and str(w) not in [q[0] for q in sl]: sl.append((str(w), None, 'Kijk goed hoeveel nullen erbij of eraf moeten.'))
        _claude9(it, sl); ev['claudeDenkfouten'] = []; it['foutHints'] = []
        uit.append(it); _log(punt=419, id=it['id'], opgave=o, antwoord=it['antwoord'])
    for it in uit:      # guard: antwoord klopt, eerste getal = het getal dat je omrekent, eenheid uit de kop staat in de vraag
        F, keer = it['merge']['genHmdl']['factor'], it['merge']['genHmdl']['keer']; x = int(re.findall(r'\d+', it['opgave'])[0]); a = int(it['antwoord'])
        assert (a == x * F) if keer else (a * F == x), ('D-#419', it['id'])
    return uit
_na_alle_r10 = na_alle
def na_alle(rows):
    rows = _na_alle_r10(rows)      # de uitg5- en gen-items bestaan pas na ronde 9
    na401(rows); na385(rows)
    rows += aanvul_ctx419(rows)
    guards_r10b(rows)
    return rows
# ---- #400 (in de entries, in het geheugen): laag 2 van Oefeningen bij 'getal net boven de stip' (VBN-E02 #2) en 'een paar maanden (regel)' (VBN-E02 #3)
L2_400 = {'fout = het getal net boven de stip': 'Leg je vinger op de stip en schuif recht naar de getallen langs de zijkant. Begin bij het getal op of net onder je vinger en tel vanaf daar de streepjes omhoog tot de stip.',
          'fout = de som van een deel van de maanden': 'Wijs de maanden onder de grafiek één voor één aan. Lees bij elke maand het aantal af en schrijf het op. Tel daarna alle getallen op.'}
R275C['tekstSterker'] = L2_400['fout = het getal net boven de stip']
_pas_entries_aan_r10 = pas_entries_aan
def pas_entries_aan(somtypen):
    _pas_entries_aan_r10(somtypen)
    n = collections.Counter()
    for st in somtypen:
        if st.get('doel') != 'G6-VBN-E02': continue
        for f in st['foutHints']:
            if f['regel'] in L2_400 and f.get('tekstSterker') != L2_400[f['regel']]:
                f['tekstSterker'] = L2_400[f['regel']]; n[f['regel']] += 1
    assert all(f.get('tekstSterker') for st in somtypen if st.get('doel') == 'G6-VBN-E02' for f in st['foutHints'] if f['regel'] in L2_400), '#400: laag 2 ontbreekt'
    _log(punt=400, entries=dict(n))
# ---- #532 (eindcheck G6 r11, verplicht; opdracht 12:01): GET-E04 #2/#8 'honderd te veel' bij een overdracht via een 9 (069: 5138 + 4269, 078: 5556 + 2448).
# De motor rekent de echte overdracht naar de honderdtallen uit ('(met|zonder) overdracht naar de honderdtallen', fout_regels.py). In de entry (in het
# geheugen) komen twee regels vóór de gewone 'fout = antwoord + 100'; die blijft als terugval met de voorwaardelijke tekst van Didactiek.
# TODO Oefeningen (#532): de teksten hieronder nalopen of vervangen; het voorstel van Didactiek staat bij de terugval.
T532_MET = ('Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. '
            'Dat komt op tien of meer. Dan neem je precies één mee naar de honderdtallen, niet meer.')
T532_ZONDER = ('Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. '
               'Dat blijft onder de tien. Dan neem je niets mee naar de honderdtallen.')
T532_TERUG = ('Dat is honderd te veel. Tel de honderdtallen nog eens. Tel de tientallen samen, met de één die je misschien al meenam. '
              'Is dat tien of meer? Dan neem je precies één mee naar de honderdtallen, anders niets.')
_pas_entries_aan_r10b = pas_entries_aan
def pas_entries_aan(somtypen):
    """#532: de twee overdrachtsregels staan sinds ronde 11 woordelijk in de entry van Oefeningen (batch2 E04 #2/#8); de stap in het geheugen is weg
    (opdracht 12:10). Hier alleen nog een controle dat ze er staan; guard532 (FIX6) pint de tekst bij 069/078."""
    _pas_entries_aan_r10b(somtypen)
    for st in somtypen:
        if st.get('doel') == 'G6-GET-E04' and st.get('nrOrigineel') in (2, 8):
            rs = [f['regel'] for f in st['foutHints']]
            assert all(f'fout = antwoord + 100 ({w} overdracht naar de honderdtallen)' in rs for w in ('met', 'zonder')), f"#532: overdrachtsregels ontbreken in GET-E04 #{st['nrOrigineel']}"
    _log(punt=532, entries='in de entry van Oefeningen (geen stap in het geheugen meer)')
def guard532(rows):
    """#532/#550 (eindcheck r11b, les 157): reken bij ELKE sleutel 'honderd te veel' en 'tien te veel' in GET-E04 (plussom getal1 + getal2 = antwoord) de
    overdracht na en eis de regel en de tekst die daarbij horen (uit de entry van Oefeningen):
      sleutel = antwoord + 100 → '(met overdracht …)' als getal1 mod 100 + getal2 mod 100 ≥ 100, anders '(zonder overdracht …)';
      sleutel = antwoord + 10  → 'fout = antwoord + 10' (bij de eenheden komt nooit iets binnen; de tekst is voorwaardelijk en klopt altijd).
    Geeft een lijst met fouten (leeg = goed). Mutatietest: zie check_fixlijst_g6.py (#550)."""
    import glob as _g, json as _j, os as _o, sys as _s
    _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); import fout_regels as _FR
    base = _o.path.dirname(_o.path.dirname(_o.path.abspath(__file__)))
    tekst = {}
    for p in _g.glob(f'{base}/hints/batch*.json'):
        for st in _j.load(open(p))['somtypen']:
            if st['doel'] == 'G6-GET-E04': tekst.update({(st['nrOrigineel'], f['regel']): f['tekst'] for f in st['foutHints']})
    fout, n = [], 0
    for it in rows:
        if it.get('merge', {}).get('doel') != 'G6-GET-E04': continue
        nro = it['merge'].get('somtypeNrOrigineel')
        c = _FR.Ctx(it)
        if c.g1 is None or c.g2 is None or c.a is None or c.g1 + c.g2 != c.a: continue
        for f in it.get('foutHints') or []:
            try: k = int(str(f['fout']).replace('.', ''))
            except ValueError: continue
            if k == c.a + 100:
                w = 'met' if (c.g1 % 100) + (c.g2 % 100) >= 100 else 'zonder'
                r = f'fout = antwoord + 100 ({w} overdracht naar de honderdtallen)'
            elif k == c.a + 10: r = 'fout = antwoord + 10'
            else: continue
            if (nro, r) not in tekst: continue      # somtype zonder deze regel (geen plussom-entry)
            n += 1
            if f.get('regel') != r or f.get('uitleg') != tekst[(nro, r)]:
                fout.append(f"#550: {it['id']} ({it['opgave'][:40]}…) sleutel {f['fout']}: verwacht '{r}' met de tekst daarvan, kreeg '{f.get('regel')}' / {str(f.get('uitleg'))[:60]!r}")
    guard532.gecontroleerd = n
    return fout

# r13 N13-1/N13-2 (na-ronde-r13, Overzicht 8 okt): bordtitels van het samengevoegde VBN-E02 en van MEET-E05. Vervangt #217/#261/#276 voor deze twee doelen.
# Let op (#276): de VBN-E02-titel noemt beeld- en cirkeldiagram; die somtype-plekken (N13-3) wachten nog op Oefeningen.
BORD_N13 = {'G6-VBN-E02': 'Beelddiagram, cirkeldiagram en lijngrafiek aflezen', 'G6-MEET-E05': 'Kilogram en gram vergelijken en omrekenen'}
BORD261 = dict(BORD261, **{k: v for k, v in BORD_N13.items() if k in BORD261})
BORD276 = dict(BORD276, **{k: v for k, v in BORD_N13.items() if k in BORD276})
BORD217 = dict(BORD217, **BORD_N13)
