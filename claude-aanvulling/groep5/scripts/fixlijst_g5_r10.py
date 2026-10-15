"""G5 ronde 10 (8 okt; Didactiek gate ronde 9, g5/gate-ronde9-didactiek.md). Uitgevoerd door Overzicht. Alles in het geheugen, in de build.
In fixlijst_g5_r7b.py (generator en wisselgeld): #360 (generator kopieert geldigeAntwoorden niet meer), #363, #365, #370, #371, #374 (≈ in de kale som).
Hier: #360 (geldigeAntwoorden opnieuw uit het antwoord), #361, #362, #366, guards_r10. In apply_hints.py: #369 en #374 (foutRegels zonder sleutel bij generator-items)."""
import re, sys, collections
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', '..', 'scripts', 'merge')); import geldig_check as GA
LOG10 = collections.defaultdict(list)
DOOR = 'Overzicht (G5 ronde 10, 8 okt)'

# ---- #361: VBN-E01 #2 'opgeteld'-optie boven 1000 → een sleutel met een regel (Didactiek: 'één staaf' of 'streepjes geteld')
OPT361 = {'G5-VBN-E01-claude-bank-028': ('1100', '1000', 'andere-deel-genomen', 'Dat is wat één staaf laat zien. De vraag is hoeveel meer het is.'),
          'G5-VBN-E01-claude-bank-056': ('1100', '800', 'andere-deel-genomen', 'Dat is wat één staaf laat zien. De vraag is hoeveel meer het is.'),
          'G5-VBN-E01-claude-bank-080': ('1150', '800', 'andere-deel-genomen', 'Dat is wat één staaf laat zien. De vraag is hoeveel meer het is.'),
          'G5-VBN-E01-claude-bank-099': ('1300', '1000', 'andere-deel-genomen', 'Dat is wat één staaf laat zien. De vraag is hoeveel meer het is.'),
          'G5-VBN-E01-claude-bank-102': ('1300', '7', 'streepjes-geteld', 'Je hebt de streepjes geteld. Elk streepje is meer dan één.')}
# ---- #362: het label (kop) van E05 #17 (nrOrigineel 32) zonder 'In een tabel', zoals de opgave na #329
KOP362 = ('In een tabel staat het aantal bezoekers van [plek]: ', 'Zoveel bezoekers kwamen er bij [plek]: ')
# ---- #373 (Didactiek, opgedragen door Overzicht 11:28): de opgave leest vlotter: 'Zoveel bezoekers kwamen er bij de kinderboerderij: maandag 45, …' (label idem)
OPG373 = re.compile(r'^Dit zijn de bezoekers van (.+?): ')
# ---- #366: de 9 driecijferige verhaalitems in E05 #27–#32 → toepassen (regel #327: 3 cijfers of onthouden/lenen, alleen omhoog)
NIVEAU366 = ['247', '322', '323', '324', '325', '394', '397', '398', '399']

# ---- Oef-#404 (Oefeningen, fixlijst G5 #404; Didactiek: goed, geen plicht; opgedragen door Overzicht 11:33): per-itemteksten in VBN-E03 als vraag
TEKST404 = {('G5-VBN-E03-claude-bank-012', '16 cm'): 'Is de plant bij 0 cm begonnen? Hij is nu al 6 cm hoog. Tel de groei daar nog bij.',
            ('G5-VBN-E03-claude-bank-013', '30 euro'): 'Was de spaarpot eerst leeg? Er zit nu al 12 euro in. Tel dat er nog bij.',
            ('G5-VBN-E03-claude-bank-023', '30'): 'Heb je voor het eerste vierkant 4 lucifers geteld? Voor elk vierkant erbij komen er 3 bij.'}
def fix_r10(rows):
    idx = {it['id']: it for it in rows}
    for (i, w), t in TEKST404.items():
        ch = [x for x in idx[i]['extraVelden'].get('claudeFoutHints') or [] if x['fout'] == w]; assert len(ch) == 1 and 'vergeten' in ch[0]['uitleg'], ('Oef-#404', i, w)
        ch[0]['uitlegVoor404'] = ch[0]['uitleg']; ch[0]['uitleg'] = t; LOG10['404'].append((i, w))
    for i, (o, n, lab, u) in OPT361.items():
        it = idx[i]; tk = [x['tekst'] for x in it['opties']]
        assert o in tk and n not in tk and n != it['antwoord'], ('#361', i, tk)
        for x in it['opties']:
            if x['tekst'] == o: x['tekst'] = n
        it['optiesTekst'] = ' · '.join(f"{x['letter']}) {x['tekst']}" for x in it['opties'])
        ev = it['extraVelden']
        ev['claudeDenkfouten'] = [dict(d, fout=n, denkfout=lab, denkfoutVoor361=d['denkfout']) if d['fout'] == o else d for d in ev.get('claudeDenkfouten') or []]
        ev['claudeFoutHints'] = [dict(d, fout=n, uitleg=u) if d['fout'] == o else d for d in ev.get('claudeFoutHints') or []]
        ev['mergeFoutHints'] = [d for d in ev.get('mergeFoutHints') or [] if d['fout'] != o]
        it['foutHints'] = [f for f in it.get('foutHints') or [] if f['fout'] != o]
        it['merge']['optie361'] = {'oud': o, 'nieuw': n, 'label': lab, 'door': DOOR}; LOG10['361'].append((i, o, n))
    for it in rows:
        if it['merge'].get('doel') == 'G5-GET-E05' and (it['merge'].get('somtype') or '').startswith(KOP362[0]):
            it['merge']['kop362'] = {'oud': it['merge']['somtype']}; it['merge']['somtype'] = KOP362[1] + it['merge']['somtype'][len(KOP362[0]):]
            LOG10['362'].append(it['id'])
            o = it['opgave']; it['opgave'] = OPG373.sub(r'Zoveel bezoekers kwamen er bij \1: ', o); assert it['opgave'] != o, ('#373', it['id'], o)
            it['merge']['opgave373'] = {'oud': o}; LOG10['373'].append(it['id'])
    assert LOG10['362'] and len(LOG10['373']) == len(LOG10['362']), '#362/#373: geen items met de oude kop'
    for n in NIVEAU366:
        it = idx[f'G5-GET-E05-claude-bank-{n}']; s = it['extraVelden'].get('claudeKaleSom') or ''
        assert it['niveau'] == 'basis' and re.search(r'\d{3}', s), ('#366', it['id'], it['niveau'], s)
        it['niveau'] = 'toepassen'; it['niveauKind'] = 'Oefenen'; it['merge']['niveau366'] = {'oud': 'basis', 'som': s, 'waarom': 'drie cijfers (regel #327)'}
        LOG10['366'].append(it['id'])
    return LOG10

def geldig360(rows):
    """#360 (les 105/106): geldigeAntwoorden opnieuw uit het antwoord, bij elk G5-item dat het veld heeft (vormen als bij de G8→G5-items)."""
    for it in rows:
        if 'geldigeAntwoorden' not in it or it['geldigeAntwoorden'] is None: continue
        if not it['geldigeAntwoorden'] and '-merge-gen-' not in it['id']: continue
        nieuw = GA.vormen(it['antwoord'])
        if nieuw != it['geldigeAntwoorden']:
            LOG10['360'].append((it['id'], it['geldigeAntwoorden'], nieuw)); it['merge']['geldig360'] = {'oud': it['geldigeAntwoorden']}
        it['geldigeAntwoorden'] = nieuw

def guards_r10(rows):
    G = [r for r in rows if (r['merge'].get('doel') or '').startswith('G5-')]
    f = GA.vind(rows); assert not f, ('#360: antwoord niet in geldigeAntwoorden', f[:3])
    for it in G:
        d = it['merge']['doel']
        if not d.startswith('G5-MEET-'):      # #361/#302 over heel G5; uitzondering Meten: omrekenen (1 L = 1000 ml) geeft zelf antwoorden > 1000, grens daar 10.000 (#60)
            for o in it.get('opties') or []:
                v = re.sub(r'[€\s.]', '', o['tekst']).replace(',', '.')
                assert not (re.fullmatch(r'\d+(\.\d+)?', v) and float(v) > 1000), ('#361/#302 optie > 1000', it['id'], o['tekst'])
        assert not (d == 'G5-GET-E05' and 'In een tabel' in (it['merge'].get('somtype') or '') and not it['visual'].get('jsRender')), ('#362', it['id'])
        assert not (d == 'G5-GET-E05' and re.match(r'^(Dit zijn de bezoekers|In een tabel staat het aantal bezoekers)', it['opgave'] or '')), ('#373', it['id'])
        if it['merge'].get('gen235') and d == 'G5-GET-E05' and 'bezoekers' in it['opgave']:
            assert all(int(x) < 100 for x in re.findall(r'\d+', it['opgave'])), ('#363: dag ≥ 100', it['id'])
        m = re.match(r'^(\d+) × (\d+) ≈ (\d+) × (\d+)$', it['extraVelden'].get('claudeKaleSom') or '')
        if it['merge'].get('gen235') and d == 'G5-GET-E07':
            assert m, ('#374: kale som zonder ≈-stap', it['id'])
            ex, sch = int(m[1]) * int(m[2]), int(m[3]) * int(m[4]); assert abs(sch - ex) / ex < 0.10 and str(sch) == it['antwoord'], ('#370', it['id'])
        if d == 'G5-GET-E09' and re.search(r'met elk|elk \d', it['opgave'] or '') and (q := re.findall(r'\d+', it['opgave'])) and len(q) == 3 and str(int(q[0]) * int(q[1]) - int(q[2])) == it['antwoord']:
            a, b, k = map(int, q)      # #371: geen sleutel van E09 #2 is een getal uit de vraag
            for fh in it['extraVelden'].get('claudeFoutHints') or []:
                assert not (fh['fout'].isdigit() and int(fh['fout']) in (a, b, k)), ('#371/#325: sleutel = getal uit de vraag', it['id'], fh['fout'])
        if re.match(r'^\w+ koopt \d+ .+ betaalt met €100\.', it['opgave'] or ''):
            n, p = map(int, re.match(r'^\w+ koopt (\d+) .+? van €(\d+)', it['opgave']).groups()); assert n * p > 50, ('#365/#323: €100 terwijl €50 genoeg is', it['id'])
    LOG10['guards'].append({k: len(v) for k, v in LOG10.items() if k != 'guards'})
    return True

# ---- in apply_hints.py (na de hint-sync) ----
BIJNA369 = re.compile(r'^fout = (?:het )?antwoord ?[+\-−±] ?([2-9])(?![\d,])(?! ?cent)')
def pas_entries(entries):
    """#369: 'Bijna!' alleen bij één stap: weg bij een regel 'fout = antwoord ± N' met N ≥ 2 (M05 116 'twee te veel'). In het geheugen."""
    for st in entries:
        for f in st.get('foutHints') or []:
            if BIJNA369.match((f.get('regel') or '').lower()) and (f.get('tekst') or '').startswith('Bijna! '):
                f['tekst'] = f['tekst'][len('Bijna! '):]; f['tekst'] = f['tekst'][:1].upper() + f['tekst'][1:]
                LOG10['369'].append(f"{st['doel']} #{st.get('nrOrigineel')}: {f['regel']}")
def regels374(it):
    """#374: bij een generator-item geen foutRegels die naar een sleutel verwijzen die er niet is (lege waarden); 'andere fout' (alles) blijft."""
    # D-#405 (les 121): alleen bij meerkeuze (een regel zonder optie kan daar nooit vuren); een bereikregel (vanaf/totEnMet/kleinerDan) blijft altijd staan
    if '-merge-gen-' not in it['id'] or not it.get('opties'): return 0
    oud = it.get('foutRegels') or []
    leeft = lambda m: m.get('alles') or m.get('waarden') or any(k in m for k in ('vanaf', 'totEnMet', 'kleinerDan'))
    it['foutRegels'] = [r for r in oud if leeft(r.get('match') or {})]
    assert all(leeft(r.get('match') or {}) for r in it['foutRegels']), ('#374', it['id'])
    return len(oud) - len(it['foutRegels'])
