"""Didactiek-besluiten op de 1226 G8-twijfelitems (g8/besluiten_twijfel.json/.md, build 19:12:04) + besluiten Dave (20:56).
laad()            twijfel-id → claudeId via bevroren/ids_v1.json; {claudeId: besluit}
classify(d)       status en doel voor build_g8: doelGroep 8 → 'gemapt'; G4–G7 → 'naar-G4' … 'naar-G7' (aanvulbestand van die groep); schrappen
bewerk(it, d, …)  opgave, opties, antwoord, geldige antwoorden, fout-hints, Hint 1/2 (voorstel), visual (torens: rechtsvoor), badge, duplicaatVan …
Dave 20:56: (1) knip schatten/kan-kloppen tot 100 → G4, tot 1000 → G5 (zo in de json); (2) 012 niet schrappen: staafdiagram, G8-VBN-V01;
(3) T1/T7/T8 passende contexten, T8 met '€'; (4) T1 en T8 → G5; (5) G8-GET-E02-001 → G5-GET-E07; tekstfout mediaan-item."""
import json, os, re, hashlib, copy
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(HERE)
P = f'{OUT}/besluiten_twijfel.json'
NAAR = {4: 'naar-G4', 5: 'naar-G5', 6: 'naar-G6', 7: 'naar-G7'}
DAVE = 'besluit Dave 20:56'

def laad():
    if not os.path.exists(P): return {}
    bes = json.load(open(P))['besluiten']
    I = json.load(open(f'{OUT}/bevroren/ids_v1.json')); cid = {v: k for k, v in I['ids'].items()}
    for k, vs in I.get('vorigeIds', {}).items(): cid.update({v: k for v in vs})
    out = {}
    for tid, b in bes.items():
        assert tid in cid, ('besluit voor een onbekend twijfel-id', tid)
        d = dict(b, twijfelId=tid, didactiek={'besluit': b['besluit'], 'doel': b['doel']}, dave=None)
        if tid.endswith('E04-claude-bank-twijfel-012'):      # Dave (2): niet schrappen, een echt staafdiagram, G8-VBN-V01
            d.update(besluit='aanpassen', doel='G8-VBN-V01', doelId='G8-VBN-V01', doelGroep=8, dave=f'{DAVE} (2): niet schrappen; echt staafdiagram, G8-VBN-V01')
        out[cid[tid]] = d
    assert len(out) == len(bes), (len(out), len(bes))
    return out

def classify(d):
    wie = f"Didactiek 1 okt (G8-twijfel {d['twijfelId']}): {d['subregel']}" + (f"; {d['dave']}" if d.get('dave') else '')
    if d['besluit'] == 'schrappen': return dict(status='schrappen', doel=None, regel=f"D8-{d['redencode']}", reden=wie, cat=None, aanvulling=False)
    g = d['doelGroep']; assert d['doelId'] == d['doel'] and d['doelId'].startswith(f'G{g}-'), ('doelId/doelGroep', d['twijfelId'], d['doelId'], g)
    return dict(status='gemapt' if g == 8 else NAAR[g], doel=d['doelId'], regel=f"D8-{d['redencode']}", reden=wie, cat=None, aanvulling=False)

def _opties(it, M, teksten, antwoord):
    it['type'] = 'meerkeuze'; it['opties'] = [{'letter': 'ABCDEF'[i], 'tekst': t} for i, t in enumerate(teksten)]
    it['antwoord'] = antwoord; M.herbouw_opties(it)

def _fouten(it, lijst, bron):
    """lijst = [{fout, uitleg, …}]. Zet foutHints en de Claude-basis (apply_hints rekent daarop); de oude als metadata in merge."""
    ex = it['extraVelden']
    it['merge'].setdefault('claudeFoutHintsVoorBesluit', [dict(f) for f in ex.get('claudeFoutHints') or []])
    fh = [{'stap': None, 'fout': f['fout'], 'uitleg': f['uitleg']} for f in lijst]
    it['foutHints'] = [dict(f, regel=bron, soort=f.get('hintSoort'), bron='didactiek') for f, x in zip(fh, lijst)]
    ex['claudeFoutHints'] = [dict(f) for f in fh]
    ex['claudeDenkfouten'] = [{'fout': x['fout'], 'denkfout': x['hintSoort']} for x in lijst if x.get('hintSoort')]

# ---- Dave (2): 012 krijgt een echt staafdiagram (visual-spec) en gaat naar G8-VBN-V01
def _012(it, M, slog):
    o = it['opgave']; m = re.findall(r'bij (maandag|dinsdag|woensdag) (\d+) boeken', o)
    assert len(m) == 3 and it['antwoord'] == 'Woensdag', ('012', o)
    it['merge']['opgaveVoorBesluit'] = o
    it['opgave'] = 'In het staafdiagram zie je hoeveel boeken er op maandag, dinsdag en woensdag zijn geleend. Op welke dag zijn de meeste boeken geleend?'
    hoog = max(int(w) for _, w in m)
    it['visual'] = {'nodig': True, 'asciiSchets': False, 'svgBestanden': [],
                    'toelichting': "Verplicht (Dave 20:56): een staafdiagram met drie staven (maandag, dinsdag, woensdag), de as met de getallen om de 1 en een streepje per boek; de getallen staan niet in de tekst. Kleur is niet het enige kenmerk: onder elke staaf staat de dag.",
                    'jsRender': {'soort': 'staafdiagram', 'staven': [{'naam': d, 'waarde': int(w)} for d, w in m], 'max': hoog + (5 - hoog % 5 if hoog % 5 else 0), 'perstreep': 1, 'cijfer_om': 5}}
    _fouten(it, [{'fout': 'Maandag', 'uitleg': 'Kijk naar de hoogste staaf. Op welke dag hoort die?', 'hintSoort': 'niet-de-hoogste-staaf'},
                 {'fout': 'Dinsdag', 'uitleg': 'Dat is de laagste staaf. Je zoekt de dag met de meeste boeken: de hoogste staaf.', 'hintSoort': 'laagste-staaf'}], 'Dave 20:56 (2)')
    it['hint'] = 'Zoek de hoogste staaf.'; it['sterkereHint'] = 'Lees onder de hoogste staaf welke dag het is.'
    it['merge']['hintStatus'] = 'voorstel Overzicht (Dave 20:56); Oefeningen schrijft de definitieve hints'

def bewerk(it, d, M, slog):
    it['merge']['didactiekG8'] = {k: d[k] for k in ('twijfelId', 'groep', 'regel', 'subregel', 'redencode', 'didactiek', 'dave', 'flags', 'hintStatus', 'aanvulling') if k in d}
    if d.get('dave') and 'twijfel-012' in d['twijfelId']: return _012(it, M, slog)
    if d['besluit'] in ('houden', 'verplaatsen'):
        if d.get('geldigeAntwoorden'): it['geldigeAntwoorden'] = list(d['geldigeAntwoorden'])
        return
    if d.get('nieuweOpgave'):
        if d.get('origineleOpgave') and re.sub(r'\s+', ' ', d['origineleOpgave']).strip() != re.sub(r'\s+', ' ', it['opgave']).strip():
            it['merge']['didactiekG8']['opgaveAfwijking'] = {'besluit': d['origineleOpgave'], 'build': it['opgave']}
        it['merge']['opgaveVoorBesluit'] = it['opgave']; slog(it, 'D8 nieuwe opgave (Didactiek)', 'opgave', it['opgave'], d['nieuweOpgave']); it['opgave'] = d['nieuweOpgave']
    if d.get('nieuweJsRender'):     # balk-dubbels: nieuwe maten
        it['merge']['jsRenderVoorBesluit'] = it['visual'].get('jsRender'); it['visual']['jsRender'] = dict(d['nieuweJsRender'])
    if d.get('nieuweOpties'):
        _opties(it, M, list(d['nieuweOpties']), d.get('nieuwAntwoord') or it['antwoord'])
    elif d.get('nieuwAntwoord'):
        it['merge']['antwoordVoorBesluit'] = it['antwoord']; it['antwoord'] = d['nieuwAntwoord']
    if d.get('nieuwType') == 'invullen': it['type'] = 'kale'; it['opties'] = None; M.herbouw_opties(it)
    elif d.get('nieuwType') == 'meerkeuze': it['type'] = 'meerkeuze'
    if d.get('husselen') is not None: it['husselen'] = bool(d['husselen'])
    if d.get('invulAchter'): it['invulAchter'] = d['invulAchter']
    if d.get('afspraak'): it['merge']['afrondAfspraak'] = d['afspraak']
    if d.get('geldigeAntwoorden'): it['geldigeAntwoorden'] = list(d['geldigeAntwoorden']) + [x for x in d.get('ookGoedBijOpenVorm') or [] if it['type'] == 'kale']
    if d.get('nieuweFoutHints') is not None: _fouten(it, d['nieuweFoutHints'], f"Didactiek G8 ({d['redencode']})")
    if d.get('nieuweHint1'): it['hint'] = d['nieuweHint1']
    if d.get('nieuweHint2'): it['sterkereHint'] = d['nieuweHint2']
    it['merge']['hintStatus'] = d.get('hintStatus')
    v = d.get('visual') or {}
    if v:
        nv = dict(it['visual'] or {}); nv['nodig'] = bool(v.get('nodig', True)); nv['toelichting'] = v.get('eis') or nv.get('toelichting')
        for k in ('tekeneis', 'verborgenTorentoppen', 'hint2Plaatje'):
            if k in v: nv[k] = v[k]
        if v.get('tekeneis') in ('A', 'B'):      # Dave 20:56: torens schuin van voren; B (329) verplicht rechtsvoor, A (71) rechtsvoor als standaard
            nv['kijkrichting'] = 'rechtsvoor'; nv['kijkrichtingVerplicht'] = v['tekeneis'] == 'B'
        it['visual'] = nv
    if d.get('badge'): it['badge'] = d['badge']
    if d.get('bijnaDubbelVan'): it['merge']['bijnaDubbelVanTwijfel'] = d['bijnaDubbelVan']
    if d.get('duplicaatVan'): it['merge']['duplicaatVanTwijfel'] = d['duplicaatVan']
    if d.get('vervangenAfleiders'): it['merge']['didactiekG8']['vervangenAfleiders'] = d['vervangenAfleiders']
    if d.get('wijzigingen'): it['merge']['didactiekG8']['wijzigingen'] = d['wijzigingen']

def koppel_ids(rows, oud_ids):
    """bijnaDubbelVan / duplicaatVan (twijfel-ids van Didactiek) → de nieuwe ids; duplicaatVan als item-veld (niet merge.duplicaatVan: dat is de dubbel-schrapper)."""
    nieuw = {it['bron']['claudeId']: it['id'] for it in rows}; t2c = {v: k for k, v in oud_ids.items()}
    I = json.load(open(f'{OUT}/bevroren/ids_v1.json'))      # ook de vorige ids: na een rebuild heten de twijfel-items anders
    for k, vs in I.get('vorigeIds', {}).items(): t2c.update({v: k for v in vs})
    for it in rows:
        for k, veld in (('bijnaDubbelVanTwijfel', 'bijnaDubbelVan'), ('duplicaatVanTwijfel', 'duplicaatVan')):
            if (w := it['merge'].get(k)): it[veld] = nieuw.get(t2c.get(w), w)      # bv. 'bank G8-MEET-E05' blijft zoals Didactiek het schreef
            if w and '-claude-bank-' in w: assert it[veld] != w, ('koppel_ids: twijfel-id niet gevonden', it['id'], w)

# ---- Dave (3)/(4): terug-G7 T1, T7, T8 met passende contexten; T1 en T8 → G5
NAMEN = [('Noor', 'ze'), ('Sem', 'hij'), ('Mila', 'ze'), ('Daan', 'hij'), ('Lotte', 'ze'), ('Ayoub', 'hij'), ('Fenna', 'ze'), ('Milan', 'hij')]
def _k(it, n): return int(hashlib.md5(it['bron']['claudeId'].encode()).hexdigest(), 16) % n
def _i(it): return int(re.search(r'(\d+)$', it['id']).group(1)) if it.get('id') else _k(it, 97)
KEER = ['{n} kinderen hebben elk {m} knikkers. Hoeveel knikkers zijn dat samen?', 'In {n} dozen zitten elk {m} potloden. Hoeveel potloden zijn dat samen?',
        'Een boer heeft {n} kratten met elk {m} appels. Hoeveel appels zijn dat samen?', 'In de zaal staan {n} rijen met elk {m} stoelen. Hoeveel stoelen zijn dat samen?',
        'Een album heeft {n} bladzijden met elk {m} stickers. Hoeveel stickers zijn dat samen?', 'In {n} pakken zitten elk {m} koekjes. Hoeveel koekjes zijn dat samen?',
        '{n} klassen gaan op schoolreis. In elke klas zitten {m} kinderen. Hoeveel kinderen gaan er mee?', 'In {n} zakken zitten elk {m} snoepjes. Hoeveel snoepjes zijn dat samen?']
DEEL = ['{t} knikkers worden eerlijk verdeeld over {d} kinderen. Hoeveel knikkers krijgt elk kind?', '{t} potloden worden eerlijk verdeeld over {d} groepjes. Hoeveel potloden krijgt elk groepje?',
        '{t} kinderen worden eerlijk verdeeld over {d} groepen. Hoeveel kinderen komen er in elke groep?', '{t} boeken worden eerlijk verdeeld over {d} planken. Hoeveel boeken komen er op elke plank?',
        '{t} appels worden eerlijk verdeeld over {d} kratten. Hoeveel appels gaan er in elke krat?', '{t} kaartjes worden eerlijk verdeeld over {d} klassen. Hoeveel kaartjes krijgt elke klas?',
        '{t} stickers worden eerlijk verdeeld over {d} kinderen. Hoeveel stickers krijgt elk kind?', '{t} stoelen worden eerlijk verdeeld over {d} rijen. Hoeveel stoelen komen er in elke rij?']
MIN = ['In de bibliotheek staan {t} boeken. Er worden er {k} uitgeleend. Hoeveel boeken staan er nog?', 'Op het schoolplein staan {t} kinderen. Er gaan er {k} naar binnen. Hoeveel kinderen staan er nog buiten?',
       'In de winkel liggen {t} appels. Er worden er {k} verkocht. Hoeveel appels liggen er nog?', 'In de sporthal zitten {t} mensen. Er gaan er {k} naar huis. Hoeveel mensen zitten er nog?',
       'Voor de voorstelling zijn er {t} kaartjes. Er zijn er {k} verkocht. Hoeveel kaartjes zijn er nog over?', 'Sem heeft {t} stickers. Hij geeft er {k} weg. Hoeveel stickers heeft hij nog?',
       'In de kantine liggen {t} broodjes. Er worden er {k} verkocht. Hoeveel broodjes liggen er nog?', 'Op de camping staan {t} tenten. Er gaan er {k} weg. Hoeveel tenten staan er nog?']
PLUS = ['In de bibliotheek staan {t} boeken. Er komen er {k} bij. Hoeveel boeken zijn het nu?', 'Mila heeft {t} stickers. Ze krijgt er {k} bij. Hoeveel stickers heeft ze nu?',
        'In de zaal zitten {t} mensen. Er komen er {k} bij. Hoeveel mensen zitten er nu?', 'De school heeft {t} leerlingen. Er komen er {k} bij. Hoeveel leerlingen zijn het nu?',
        "Op de parkeerplaats staan {t} auto's. Er komen er {k} bij. Hoeveel auto's staan er nu?", "In het fotoalbum zitten {t} foto's. Er komen er {k} bij. Hoeveel foto's zijn het nu?",
        'In de winkel liggen {t} appels. Er komen er {k} bij. Hoeveel appels liggen er nu?', 'Op de camping staan {t} tenten. Er komen er {k} bij. Hoeveel tenten staan er nu?']
MEER = ['{n} kinderen nemen elk {m} knikkers mee naar school. Ze raken er samen {k} kwijt. Hoeveel knikkers hebben ze nog?',
        'De juf heeft {n} dozen met elk {m} potloden. Ze deelt er {k} uit. Hoeveel potloden heeft ze nog?',
        'Een boer heeft {n} kratten met elk {m} appels. Hij verkoopt er {k}. Hoeveel appels heeft hij nog?',
        'In de kast staan {n} dozen met elk {m} stiften. Er worden er {k} gebruikt. Hoeveel stiften liggen er nog in de kast?',
        '{n} kinderen hebben elk {m} stickers. Ze plakken er samen {k} in een album. Hoeveel stickers hebben ze nog los?']
def _prijs_dingen(c):      # (meervoud, enkelvoud) die bij de prijs per stuk passen (Dave 20:56: geen poesjes, veren of een ei van €8,80)
    if c < 200: return [('ijsjes', 'ijsje'), ('pennen', 'pen'), ('pakken melk', 'pak melk')]
    if c < 400: return [('schriften', 'schrift'), ('pennen', 'pen'), ('kaartjes voor de bus', 'kaartje voor de bus')]
    if c < 600: return [('kaartjes voor het zwembad', 'kaartje voor het zwembad'), ('schriften', 'schrift'), ('ballen', 'bal')]
    return [('boeken', 'boek'), ('puzzels', 'puzzel'), ('kaartjes voor de bioscoop', 'kaartje voor de bioscoop')]
def _cent(s): m = re.fullmatch(r'€(\d+)(?:,(\d{2}))?', s); return int(m.group(1)) * 100 + int(m.group(2) or 0)
GEBRUIKT_CTX = set()
CTX_MAP, CUR = {}, [None]
def _kies(lijst, i, maak):
    """Dezelfde bronopgave krijgt dezelfde nieuwe tekst (zodat een echte dubbel een dubbel blijft); verschillende bronopgaven nooit dezelfde."""
    if CUR[0] in CTX_MAP: return CTX_MAP[CUR[0]]
    t = _kies2(lijst, i, maak); CTX_MAP[CUR[0]] = t; return t
def _kies2(lijst, i, maak):
    for k in range(len(lijst)):
        t = maak(lijst[(i + k) % len(lijst)])
        if t not in GEBRUIKT_CTX: GEBRUIKT_CTX.add(t); return t
    raise AssertionError(('context_terug: alle contexten al gebruikt', lijst[0]))
def context_terug(it, slog):
    """T1/T7/T8 (terug-G7): passende contexten; getallen en antwoord blijven, T8-wisselgeld krijgt '€'. Geeft het G5-doel bij T1/T8."""
    r = it['merge'].get('regel'); o = it['opgave']; i = _i(it); nieuw = doel = soort = None
    CUR[0] = (r, o, str(it['antwoord']))
    if r == 'G8-T1-door-elkaar':
        if m := re.fullmatch(r"(\d+) [a-zà-ÿ']+ hebben elk (\d+) [a-zà-ÿ']+\. Hoeveel [a-zà-ÿ']+ is dat samen\?", o): nieuw = _kies(KEER, i, lambda x: x.format(n=m.group(1), m=m.group(2))); doel = 'G5-GET-E07'; soort = 'keer'
        elif m := re.fullmatch(r"(\d+) [a-zà-ÿ']+ worden eerlijk verdeeld over (\d+) [a-zà-ÿ']+\. Hoeveel krijgt (?:elke|elk) [a-zà-ÿ']+\?", o): nieuw = _kies(DEEL, i, lambda x: x.format(t=m.group(1), d=m.group(2))); doel = 'G5-GET-E07'; soort = 'delen'
        elif m := re.fullmatch(r"(?:In|Op) .+? liggen (\d+) [a-zà-ÿ']+\. Er gaan er (\d+) weg\. Hoeveel blijven er over\?", o): nieuw = _kies(MIN, i, lambda x: x.format(t=m.group(1), k=m.group(2))); doel = 'G5-GET-E05'; soort = 'min'
        elif m := re.fullmatch(r"(?:In|Op) .+? liggen (\d+) [a-zà-ÿ']+\. Er komen er (\d+) bij\. Hoeveel zijn het er nu\?", o): nieuw = _kies(PLUS, i, lambda x: x.format(t=m.group(1), k=m.group(2))); doel = 'G5-GET-E05'; soort = 'plus'
    elif r == 'G8-T7-prijs-per-stuk':
        if m := re.fullmatch(r"(\d+) [a-zà-ÿ']+ kosten samen (€[\d,]+)\. Hoeveel kost één [a-zà-ÿ']+\?", o):
            soort = 'prijs per stuk'; nieuw = _kies(_prijs_dingen(_cent(it['antwoord'])), i, lambda x: f'{m.group(1)} {x[0]} kosten samen {m.group(2)}. Hoeveel kost één {x[1]}?')
    elif r == 'G8-T8-meerstaps':
        doel = 'G5-GET-E09'
        if m := re.fullmatch(r"(\d+) [a-zà-ÿ']+ brengen elk (\d+) [a-zà-ÿ']+ naar .+?\. Daarna worden er (\d+) weggehaald\. Hoeveel [a-zà-ÿ']+ liggen er nog\?", o):
            soort = 'meerstaps'; nieuw = _kies(MEER, i, lambda x: x.format(n=m.group(1), m=m.group(2), k=m.group(3)))
        elif m := re.fullmatch(r"Een [a-zà-ÿ']+ koopt (\d+) [a-zà-ÿ']+ van €(\d+) per stuk en betaalt met €(\d+)\. Hoeveel krijgt hij terug\?", o):
            naam, zij = NAMEN[i % 8]; soort = 'wisselgeld'
            nieuw = _kies(_prijs_dingen(int(m.group(2)) * 100), i, lambda x: f'{naam} koopt {m.group(1)} {x[0]} van €{m.group(2)} per stuk en betaalt met €{m.group(3)}. Hoeveel geld krijgt {zij} terug?')
            if not str(it['antwoord']).startswith('€'):
                it['merge']['antwoordVoorBesluit'] = it['antwoord']; it['antwoord'] = '€' + str(it['antwoord'])
    else: return None
    assert nieuw, ('context_terug: patroon onbekend', r, o)
    it['merge']['opgaveVoorContext'] = o; it['opgave'] = nieuw; it['merge']['contextSoort'] = soort
    slog(it, f"D8 context {r} ({DAVE} (3))", 'opgave', o, nieuw)
    return doel

def mediaan_tekst(it, slog):
    o = it['opgave']; n = re.sub(r'(het middelste getal), dus het middelste getal\?', r'\1?', o)
    if n != o: it['opgave'] = n; slog(it, f'D8 tekstfout mediaan-item ({DAVE})', 'opgave', o, n)

# Dave 22:06 (1): geen 'kans' in G8. Het item van Didactiek KANS-NAAR-DEEL vraagt nu 'welk deel van de knikkers'; regelnaam, uitleg en strategie
# gebruiken die woorden. Het besluit blijft herkenbaar aan twijfelId; de oorspronkelijke codes staan in besluiten_twijfel.json en de log.
KANS_WEG = {'KANS-NAAR-DEEL': 'DEEL-VAN-DE-KNIKKERS', 'G8-G9-kans': 'G8-G9-deel-van-de-knikkers'}
KANS_RX = re.compile(r'\bkans', re.I)
def zonder_kans(it, slog):
    m = it['merge']; dg = m.get('didactiekG8') or {}
    for f in it.get('foutHints') or []:
        for kk in ('regel', 'soort', 'bron'):
            if isinstance(f.get(kk), str):
                for k, v in KANS_WEG.items(): f[kk] = f[kk].replace(k, v)
    if m.get('regel'):
        for k, v in KANS_WEG.items(): m['regel'] = m['regel'].replace(k, v)
    if dg.get('redencode') in KANS_WEG: dg['redencode'] = KANS_WEG[dg['redencode']]
    if dg.get('regel') in KANS_WEG: dg['regel'] = KANS_WEG[dg['regel']]
    if dg.get('groep') == 'kans': dg['groep'] = 'deel van de knikkers'
    ex = it['extraVelden']
    if KANS_RX.search(ex.get('claudeStrategie') or ''):
        slog(it, 'D8 deel van de knikkers (Dave 22:06)', 'claudeStrategie', ex['claudeStrategie'], 'deel van de knikkers tellen'); ex['claudeStrategie'] = 'deel van de knikkers tellen'
    if KANS_RX.search(ex.get('claudeUitleg') or ''):
        m_ = re.match(r'^Er liggen (\d+) rode, (\d+) blauwe en (\d+) groene knikkers?\.', ex['claudeUitleg'])
        assert m_, ('kans in claudeUitleg, niet herkend', it['id'] if 'id' in it else it['bron']['claudeId'], ex['claudeUitleg'])
        r, b, g = (int(x) for x in m_.groups()); n = f'Er liggen {r} rode, {b} blauwe en {g} groene knikker{"s" if g != 1 else ""}. Samen zijn dat {r + b + g} knikkers. Daarvan zijn er {r} rood. Dus {r} op de {r + b + g} knikkers is rood.'
        slog(it, 'D8 deel van de knikkers (Dave 22:06)', 'claudeUitleg', ex['claudeUitleg'], n); ex['claudeUitleg'] = n
    if KANS_RX.search(m.get('opgaveVoorBesluit') or ''):
        slog(it, 'D8 deel van de knikkers (Dave 22:06): oude opgave alleen in de log', 'opgaveVoorBesluit', m['opgaveVoorBesluit'], None); m.pop('opgaveVoorBesluit')
    rest = [p for p, x in _strings(it) if KANS_RX.search(x)]
    assert not rest, ("'kans' staat nog in een G8-item (Dave 22:06)", it['bron']['claudeId'], rest)
def _strings(x, p=''):
    if isinstance(x, dict):
        for k, v in x.items(): yield from _strings(v, f'{p}.{k}')
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from _strings(v, f'{p}[{i}]')
    elif isinstance(x, str): yield p, x
