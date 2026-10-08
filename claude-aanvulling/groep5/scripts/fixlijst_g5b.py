#!/usr/bin/env python3
"""G5 merge-fixlijst, batch 6 en Didactiek 18:15 (1 okt 2026, 18:30). Aanroep vanuit build_g5.py.
  per_item(it, q)   na FX5.pas_toe, vóór hercontrole:
     #75  MEET-E06 'Hoeveel dagen duurt het van # [maand] tot # [maand]?' (alle items) → status park-G7, voorstel G7-MEET-04
          (dagen tussen twee datums is G7). 'Het is # [maand]. Welke datum is het # dagen later/eerder?': blijft in G5 als
          hoogstens 21 dagen, precies één maandgrens en geen februari; anders → park-G6 (G6-MEET-E07, tijd en kalender). Gelogd.
     #85  klok op de minuut (klokkenrij 'Welke klok wijst h:mm aan?' en klok + digitale opties): het uur verschuift
          deterministisch (doeluur = 1 + md5(claudeId) % 12) in alle h:mm-teksten en in jsRender; uren blijven 1–12.
          Een paar klokkenrij-items (md5 % 6 == 0, doeluur ≤ 11) vragen de tijd in 24-uurs notatie (13:00–23:59);
          de klokken zelf tonen 1–12 en het antwoord (de letter) blijft gelijk.
     #86  12 tijditems met dieren (G5-ids 1188 … 1210) → 'De kinderen' / 'De spelers' (meervoud, werkwoorden blijven goed).
     #87  claudeUitleg zonder negatieve minuten (1195, 1197) en een kloppende uitleg bij 'vertrekken … duurt H uur en M minuten'
          (1204, 1208 kwamen niet uit op het antwoord). Generiek: elke claudeUitleg met '-N minuten' of een eindtijd ≠ antwoord.
  na_ids(rows, GESCHRAPT)  na de id-toekenning:
     #83  4 items die de basismaat verklappen (1 km, 1 m = mm, 1 L, 1 kg) → geschrapt ('Didactiek #83 basismaat verklapt').
  generator_84(sjabloon_item)  #84: nieuw somtype 'dagen tellen over één maandgrens' (≤ 31 dagen, geen februari, begindag niet mee)."""
import re, hashlib, json, datetime, copy, collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fout_regels as FR
LOG = collections.defaultdict(list)
MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
TIJD = re.compile(r'(?<![\d:,.])(\d{1,2}):(\d{2})(?![\d:])')
def h(s): return int(hashlib.md5(s.encode()).hexdigest(), 16)

# ------------------------------------------------------------------ #75
def _dagen_tussen(it):
    return re.fullmatch(r'Hoeveel dagen duurt het van \d+ \w+ tot \d+ \w+\?', it['opgave'].strip())
def _datum_pm(it):
    m = re.fullmatch(r'Het is (\d+) (\w+)\. Welke datum (?:is|was) het (\d+) dagen (later|eerder)\?', it['opgave'].strip())
    if not m or m.group(2) not in MAANDEN: return None
    a = datetime.date(2025, MAANDEN.index(m.group(2)) + 1, int(m.group(1))); n = int(m.group(3))
    b = a + datetime.timedelta(days=n if m.group(4) == 'later' else -n)
    grenzen = abs((b.year * 12 + b.month) - (a.year * 12 + a.month))
    return {'dagen': n, 'maandgrenzen': grenzen, 'februari': 2 in (a.month, b.month), 'binnen': n <= 21 and grenzen == 1 and 2 not in (a.month, b.month)}
def _park(it, st, doel, regel, reden):
    it['merge'].update(status=st, doel=None, voorstelDoel=doel, regel=regel, reden=reden); it['doelId'] = None
def fix75(it):
    m = it['merge']
    if (m.get('doel') or m.get('voorstelDoel')) != 'G5-MEET-E06' or m['status'] != 'gemapt': return
    if _dagen_tussen(it):
        _park(it, 'park-G7', 'G7-MEET-04', 'G5-FX75 dagen tussen twee datums',
              'merge-fixlijst #75 (Didactiek 18:15): dagen tellen tussen twee datums is G7; met de hints van batch 5 #1 naar de G7-pool')
        m['fixlijst75'] = 'park-G7'; LOG['75'].append({'claudeId': it['bron']['claudeId'], 'naar': 'park-G7 G7-MEET-04', 'opgave': it['opgave']}); return
    d = _datum_pm(it)
    if d is None: return
    m['fixlijst75'] = dict(d, besluit='blijft G5' if d['binnen'] else 'park-G6')
    if not d['binnen']:
        _park(it, 'park-G6', 'G6-MEET-E07', 'G5-FX75 datum buiten de G5-grens',
              f"merge-fixlijst #75: datum ± {d['dagen']} dagen, {d['maandgrenzen']} maandgrens(en){', februari' if d['februari'] else ''}; G5-grens is ≤ 21 dagen, precies één maandgrens, geen februari")
    LOG['75-datum'].append({'claudeId': it['bron']['claudeId'], **m['fixlijst75'], 'opgave': it['opgave']})

# ------------------------------------------------------------------ #85
def _klok_minuut(it):
    jr = it['visual']['jsRender'] or {}
    if (it['merge'].get('doel') or '') != 'G5-MEET-E06': return None
    if jr.get('soort') == 'klokkenrij' and (m := re.fullmatch(r'Welke klok wijst (\d{1,2}):(\d{2}) aan\?', it['opgave'])): return int(m.group(1))
    if jr.get('soort') == 'klok' and it['opties'] and re.fullmatch(r'\d{1,2}:\d{2}', str(it['antwoord'])): return int(str(it['antwoord']).split(':')[0])
    return None
def _wrap(u): return (u - 1) % 12 + 1
def _schuif(s, delta):
    if not isinstance(s, str): return s
    return TIJD.sub(lambda m: f"{_wrap(int(m.group(1)) + delta)}:{m.group(2)}" if 1 <= int(m.group(1)) <= 12 else m.group(0), s)
def _schuif_alles(x, delta):
    if isinstance(x, str): return _schuif(x, delta)
    if isinstance(x, list): return [_schuif_alles(v, delta) for v in x]
    if isinstance(x, dict): return {k: (_schuif_alles(v, delta) if k not in ('denkfout', 'denkfoutClaude', 'regel', 'soort', 'bron') else v) for k, v in x.items()}
    return x
SEEN85 = set()
def _schuif_klok(jr, delta):
    jr = copy.deepcopy(jr)
    for kl in jr.get('klokken', []) if jr.get('soort') == 'klokkenrij' else [jr]: kl['uur'] = _wrap(kl['uur'] + delta)
    return jr
def fix85(it):
    u = _klok_minuut(it)
    if u is None or it['merge']['status'] != 'gemapt': return
    cid = it['bron']['claudeId']; doel_u = 1 + h(cid) % 12
    voor = it['opgave'] if it['visual']['jsRender'].get('soort') == 'klokkenrij' else it['antwoord']
    for _ in range(12):                      # geen nieuwe dubbel (zelfde vraag, klokken en antwoord als een eerder verschoven item): volgend uur
        k = (_schuif(it['opgave'], doel_u - u), json.dumps(_schuif_klok(it['visual']['jsRender'], doel_u - u), sort_keys=True), _schuif(str(it['antwoord']), doel_u - u))
        if k not in SEEN85: break
        doel_u = doel_u % 12 + 1
    SEEN85.add(k); delta = doel_u - u
    if delta:
        for k in ('opgave', 'antwoord', 'opties', 'optiesTekst', 'antwoordDetail', 'foutHints', 'foutHintsTekst'): it[k] = _schuif_alles(it[k], delta)
        ev = it['extraVelden']
        for k in ('claudeKaleSom', 'claudeUitleg', 'claudeStrategie', 'claudeDenkfouten', 'claudeFoutHints', 'mergeFoutHints'):
            if k in ev: ev[k] = _schuif_alles(ev[k], delta)
        jr = it['visual']['jsRender']
        for kl in jr.get('klokken', []) if jr.get('soort') == 'klokkenrij' else [jr]:
            kl['uur'] = _wrap(kl['uur'] + delta)
    vier = False
    if it['visual']['jsRender'].get('soort') == 'klokkenrij' and h(cid + '#85-24') % 6 == 0 and doel_u <= 11:
        it['opgave'] = re.sub(r'wijst (\d{1,2}):', lambda m: f"wijst {int(m.group(1)) + 12}:", it['opgave']); vier = True
    na = it['opgave'] if it['visual']['jsRender'].get('soort') == 'klokkenrij' else it['antwoord']
    it['merge']['fixlijst85'] = {'uurVoor': u, 'uurNa': doel_u, 'delta': delta, 'notatie24': vier}
    LOG['85'].append({'claudeId': cid, 'voor': voor, 'na': na, 'delta': delta, 'notatie24': vier})
def verify96(it):
    """#96: 'Je koopt drie … Ze kosten €a en €b en €c. Je betaalt met €B.' → B − (a + b + c)."""
    m = re.fullmatch(r'Je koopt drie [a-zà-ÿ ]+\. Ze kosten (€\d+,\d\d) en (€\d+,\d\d) en (€\d+,\d\d)\. Je betaalt met €(\d+)\. Hoeveel krijg je terug\?', it['opgave'])
    if not m: return None
    v = int(m.group(4)) * 100 - sum(_c(x) for x in m.group(1, 2, 3))
    try: ok = _c(it['antwoord']) == v
    except Exception: ok = False
    return ('ok' if ok else 'FOUT', _e(v), 'G5-#96 drie prijzen, teruggeven')
def verify85(it):
    """klokkenrij met 24-uurs vraag: de juiste klok toont h − 12. Voor andere items None. (Roept eerst verify96 aan.)"""
    v96 = verify96(it)
    if v96: return v96
    jr = it['visual']['jsRender'] or {}
    if jr.get('soort') != 'klokkenrij' or not (m := re.fullmatch(r'Welke klok wijst (\d{1,2}):(\d{2}) aan\?', it['opgave'])): return None
    uu, mm = int(m.group(1)), int(m.group(2))
    if uu <= 12: return None
    goed = [jr['labels'][i] for i, k in enumerate(jr['klokken']) if (k['uur'], k['minuut']) == (uu - 12, mm)]
    return ('ok' if goed == [it['antwoord']] else 'FOUT', ','.join(goed), 'G5-#85 klokkenrij 24-uurs (klok toont h − 12)')

# ------------------------------------------------------------------ #86 / #87
NR86 = [1188, 1191, 1194, 1195, 1197, 1199, 1201, 1203, 1204, 1205, 1208, 1210]
DIER = r"(?:poezen|konijnen|dino's|pinguïns|eekhoorns)"
def _ids86():
    D = json.load(open('/workspace/claude-merge/g5/bevroren/ids_v1.json'))['ids']; inv = {v: k for k, v in D.items()}
    return {inv[f'G5-MEET-E06-claude-bank-{n}']: (n, ['De kinderen', 'De spelers'][i % 2]) for i, n in enumerate(NR86)}
IDS86 = _ids86()
def _tekst(x, f):
    if isinstance(x, str): return f(x)
    if isinstance(x, list): return [_tekst(v, f) for v in x]
    if isinstance(x, dict): return {k: _tekst(v, f) for k, v in x.items()}
    return x
def fix86(it):
    cid = it['bron']['claudeId']
    if cid not in IDS86: return
    n, wie = IDS86[cid]; voor = it['opgave']
    f = lambda s: re.sub(rf"\b[Dd]e {DIER}", lambda m: wie if m.group(0)[0] == 'D' else wie.lower(), s)
    for k in ('opgave', 'foutHints', 'foutHintsTekst'): it[k] = _tekst(it[k], f)
    for k in ('claudeKaleSom', 'claudeUitleg', 'claudeFoutHints'):
        if k in it['extraVelden']: it['extraVelden'][k] = _tekst(it['extraVelden'][k], f)
    it['merge']['fixlijst86'] = wie; LOG['86'].append({'nr': n, 'claudeId': cid, 'voor': voor, 'na': it['opgave']})
def _min(t): a, b = t.split(':'); return int(a) * 60 + int(b)
def _tijd(m): return f"{m // 60}:{m % 60:02d}"
def fix87(it):
    ev = it['extraVelden']; u = ev.get('claudeUitleg')
    if not u or (it['merge'].get('doel') or it['merge'].get('voorstelDoel')) != 'G5-MEET-E06': return
    o = it['opgave']; nieuw = None
    if (m := re.search(r'beginnen om (\d{1,2}:\d{2}) en zijn klaar om (\d{1,2}:\d{2})', o)) and re.search(r'-\d+ minuten', u):
        a, b = _min(m.group(1)), _min(m.group(2))
        if a // 60 == b // 60: nieuw = f"Van {m.group(1)} tot {m.group(2)} is {b - a} minuten. Je gaat niet over het hele uur heen."
    elif (m := re.search(r'vertrekken om (\d{1,2}:\d{2})\. De reis duurt (\d+) uur en (\d+) minuten', o)):
        tt = [_min(t) for t in re.findall(r'\d{1,2}:\d{2}', u)]
        if tt and (_tijd(tt[-1]) != str(it['antwoord']) or any(b < a for a, b in zip(tt, tt[1:]))):   # eindtijd fout of de tijd loopt terug (1204, 1208)
            t1 = _min(m.group(1)) + 60 * int(m.group(2))
            nieuw = f"Tel eerst {m.group(2)} uur erbij: {_tijd(t1)}.\nNog {m.group(3)} minuten verder: {_tijd(t1 + int(m.group(3)))}."
            if _tijd(t1 + int(m.group(3))) != str(it['antwoord']): nieuw = None
    if nieuw:
        ev['claudeUitleg'] = nieuw; it['merge']['fixlijst87'] = True
        LOG['87'].append({'claudeId': it['bron']['claudeId'], 'opgave': o, 'voor': u, 'na': nieuw})

# ------------------------------------------------------------------ #78
def _neg(x): return str(x).strip().startswith(('-', '−'))
def fix78(it):
    """Een fout-sleutel onder nul bij een antwoord dat niet onder nul is (geld: '-0,07' bij €0,03) kan een kind niet intypen: weg uit
    claudeDenkfouten, claudeFoutHints, mergeFoutHints en foutHints."""
    if _neg(it['antwoord']): return
    ev = it['extraVelden']; weg = set()
    for k in ('claudeDenkfouten', 'claudeFoutHints', 'mergeFoutHints'):
        if ev.get(k): weg |= {str(d['fout']) for d in ev[k] if _neg(d.get('fout', ''))}; ev[k] = [d for d in ev[k] if not _neg(d.get('fout', ''))]
    weg |= {str(f['fout']) for f in it['foutHints'] if _neg(f['fout'])}; it['foutHints'] = [f for f in it['foutHints'] if not _neg(f['fout'])]
    if weg: it['merge']['fixlijst78'] = sorted(weg); LOG['78'].append({'claudeId': it['bron']['claudeId'], 'opgave': it['opgave'], 'weg': sorted(weg)})

# ------------------------------------------------------------------ #79
def kop79(it, kop):
    """G5-MEET-E07 'Je koopt drie zakken noten van …' (frozen #5, 1 item) is hetzelfde somtype als #3 'Je koopt drie [ding] van …'."""
    if it['merge'].get('doel') == 'G5-MEET-E07' and re.match(r'^Je koopt drie [a-zà-ÿ\[\] ]+?\. Ze kosten', kop):    # #96: nieuwe zin
        k2 = re.sub(r'^Je koopt drie [a-zà-ÿ\[\] ]+?\. Ze kosten', 'Je koopt drie [ding]. Ze kosten', kop)
        if 'zakken noten' in it['opgave']:
            it['merge']['fixlijst79'] = 'samengevoegd in nrOrigineel 3'; LOG['79'].append({'claudeId': it['bron']['claudeId'], 'kopVoor': kop, 'kopNa': k2})
        return k2
    if it['merge'].get('doel') == 'G5-MEET-E07' and (k2 := re.sub(r'^Je koopt drie zakken noten van', 'Je koopt drie [ding] van', kop)) != kop:
        it['merge']['fixlijst79'] = 'samengevoegd in nrOrigineel 3'; LOG['79'].append({'claudeId': it['bron']['claudeId'], 'kopVoor': kop, 'kopNa': k2}); return k2
    return kop


# ------------------------------------------------------------------ batch 6 Didactiek 18:31 (review-batch6-didactiek-v1.md)
BIJKOMT = re.compile(r"(\b(?:er|wat|hoeveel|of)\b[^.?!]{0,50}?)\bbij (kom(?:t|en))\b")
def fix_bijkomt(it):
    """V1/#90: 'bij komt' in een bijzin → 'bijkomt' (scheidbaar werkwoord aan elkaar), in de opgave en de Claude-velden.
    Teksten uit de hints (hint1/algemene fout-hint) doet Oefeningen."""
    ev = it['extraVelden']; n = 0
    def f(x):
        nonlocal n
        y = BIJKOMT.sub(lambda m: f"{m.group(1)}bij{m.group(2)}", x)
        y = y.replace('hetzelfde getal bijkomt of dat', 'hetzelfde getal bijkomt, of dat')     # V1, 006
        if y != x: n += 1
        return y
    it['opgave'] = f(it['opgave'])
    for k in ('claudeUitleg', 'claudeKaleSom', 'claudeStrategie'):
        if isinstance(ev.get(k), str): ev[k] = f(ev[k])
    for fh in ev.get('claudeFoutHints') or []:
        if isinstance(fh.get('uitleg'), str): fh['uitleg'] = f(fh['uitleg'])
    if n: it['merge']['fixlijst90'] = n; LOG['90'].append({'claudeId': it['bron']['claudeId'], 'velden': n})

def _c(s): e, c_ = str(s).replace('€', '').split(','); return int(e) * 100 + int(c_)
def _e(c_): return f'€{c_ // 100},{c_ % 100:02d}'
# #96 (S9/S10): MEET-E07 #3 'Je koopt drie …' en #4 'Een … kost … Je betaalt met …': prijzen die bij het ding passen, een kortere
# zin zonder lijstkomma's tussen kommagetallen, totaal nooit op hele euro's (S10: anders breekt 'tot de volgende hele euro').
# Sleutel = claudeId van het item; waarden = (ding, prijzen in cent, betaald in euro). De Claude-sleutels gaan mee (zelfde relatie).
NIEUW96_3 = {   # oude prijzen (zoals in de opgave) → (ding, nieuwe prijzen, betaald)
    ('gummen', '€1,29, €4,11 en €2,04'): ('gummen', (85, 120, 65), 5),
    ('knikkers', '€4,31, €1,95 en €2,73'): ('knikkers', (35, 60, 40), 2),     # #112: was (35, 60, 45) → antwoord €0,60 = de prijs van één knikker
    ('pionnen', '€3,14, €4,28 en €2,32'): ('pionnen', (115, 90, 125), 5),
    ('knuffels', '€3,13, €3,02 en €4,01'): ('knuffels', (695, 450, 725), 20),
    ('stickers', '€3,60, €1,67 en €4,70'): ('stickers', (45, 30, 15), 1),
    ('gummen', '€3,98, €4,54 en €4,31'): ('gummen', (75, 110, 95), 5),
    ('mutsen', '€3,40, €4,23 en €2,57'): ('mutsen', (850, 695, 975), 30),
    ('zakken noten', '€1,61, €3,54 en €2,41'): ('zakken noten', (249, 185, 320), 10),
}
NIEUW96_4 = {   # (ding, oude prijs) → (nieuwe prijs, betaald)
    ('trui', '€15,36'): (1495, 20), ('bal', '€7,50'): (750, 10), ('schrift', '€11,40'): (235, 5), ('wortel', '€15,46'): None,   # → meloen €2,15 (#106; was €2,45 = antwoord − 10 cent)
}
def _sleutels_mee(it, oud, nieuw):
    """oud/nieuw = dict(totaal, betaald, antwoord) in cent. Elke Claude-sleutel houdt zijn relatie: totaal → totaal,
    betaald + totaal → betaald + totaal, anders antwoord + verschil."""
    def m(k):
        try: x = _c(k)
        except Exception: return k
        if x == oud['totaal']: return _e(nieuw['totaal'])
        if x == oud['betaald'] + oud['totaal']: return _e(nieuw['betaald'] + nieuw['totaal'])
        y = nieuw['antwoord'] + (x - oud['antwoord'])
        return _e(y) if y > 0 else None        # geen sleutel €0 of onder nul (#78)
    ev = it['extraVelden']; kaart = {}
    for k in ('claudeDenkfouten', 'claudeFoutHints', 'mergeFoutHints'):
        uit = []
        for d in ev.get(k) or []:
            nk = m(d['fout']); kaart[d['fout']] = nk
            if nk is not None and nk != _e(nieuw['antwoord']): uit.append(dict(d, fout=nk))
        if k in ev: ev[k] = uit
    it['foutHints'] = []      # apply_hints zet ze opnieuw uit de entry (motor) en de Claude-sleutels
    return kaart
def fix96(it):
    if it['merge'].get('doel') != 'G5-MEET-E07': return
    o = it['opgave']
    m = re.fullmatch(r'Je koopt drie ([a-zà-ÿ ]+?) van (€\d+,\d\d, €\d+,\d\d en €\d+,\d\d)\. Je betaalt met €(\d+)\. Hoeveel krijg je terug\?', o)
    if m and (m.group(1), m.group(2)) in NIEUW96_3:
        ding, pr, bet = NIEUW96_3[(m.group(1), m.group(2))]
        oud_pr = [_c(x) for x in re.findall(r'€\d+,\d\d', m.group(2))]; ob = int(m.group(3)) * 100
        oud = {'totaal': sum(oud_pr), 'betaald': ob, 'antwoord': ob - sum(oud_pr)}
        tot = sum(pr); nieuw = {'totaal': tot, 'betaald': bet * 100, 'antwoord': bet * 100 - tot}
        assert tot % 100 and 0 < nieuw['antwoord'], (ding, pr, bet)
        it['opgave'] = f"Je koopt drie {ding}. Ze kosten {_e(pr[0])} en {_e(pr[1])} en {_e(pr[2])}. Je betaalt met €{bet}. Hoeveel krijg je terug?"
        assert abs(nieuw['antwoord'] - tot) != 10, (ding, pr, bet)          # #106 (ook in #3)
        # #112 (Oefeningen 19:06): het antwoord is nooit de prijs van één ding, en ook niet de prijs ± 10 cent (#106: dan krijgt de prijs 'Bijna!')
        assert all(abs(nieuw['antwoord'] - p_) not in (0, 10) for p_ in pr), ('#112', ding, pr, bet)
        it['antwoord'] = _e(nieuw['antwoord'])
        it['extraVelden']['claudeKaleSom'] = f"{bet} − ({_e(pr[0])[1:]} + {_e(pr[1])[1:]} + {_e(pr[2])[1:]})"
        it['extraVelden']['claudeUitleg'] = (f"Eerst optellen: {_e(pr[0])[1:]} + {_e(pr[1])[1:]} + {_e(pr[2])[1:]} = {_e(tot)[1:]}.\n"
                                             f"Dan aanvullen tot {bet}: {_e(nieuw['antwoord'])[1:]}.")
    else:
        m = re.fullmatch(r'Een ([a-zà-ÿ]+) kost (€\d+,\d\d)\. Je betaalt met €(\d+)\. Hoeveel krijg je terug\?', o)
        if not (m and (m.group(1), m.group(2)) in NIEUW96_4): return
        v = NIEUW96_4[(m.group(1), m.group(2))]
        ding = m.group(1)
        if v is None: ding, v = 'meloen', (215, 5)          # een wortel van €15,46 kan niet; #106: niet €2,45 (= antwoord − 10 cent)
        prijs, bet = v; op = _c(m.group(2)); ob = int(m.group(3)) * 100
        oud = {'totaal': op, 'betaald': ob, 'antwoord': ob - op}; nieuw = {'totaal': prijs, 'betaald': bet * 100, 'antwoord': bet * 100 - prijs}
        if (ding, prijs, bet * 100) == (m.group(1), op, ob): return
        assert abs(nieuw['antwoord'] - prijs) not in (0, 10), (ding, prijs, bet)      # #106/#112: de prijs is geen antwoord en geen sleutel '± 10 cent'
        it['opgave'] = f"Een {ding} kost {_e(prijs)}. Je betaalt met €{bet}. Hoeveel krijg je terug?"; it['antwoord'] = _e(nieuw['antwoord'])
        it['extraVelden']['claudeKaleSom'] = f"{bet} − {_e(prijs)[1:]}"
        heel = -(-prijs // 100) * 100
        it['extraVelden']['claudeUitleg'] = (f"Vul aan tot het volgende hele bedrag.\nVan {_e(prijs)} naar €{heel // 100} is {heel - prijs} cent.\n"
                                             f"Van €{heel // 100} naar €{bet} is €{bet - heel // 100}.\nSamen: {_e(nieuw['antwoord'])}.")
    if isinstance(it.get('antwoordDetail'), dict): it['antwoordDetail'] = None if not it['opties'] else it['antwoordDetail']
    kaart = _sleutels_mee(it, oud, nieuw)
    # #105: bedragen in de Claude-uitleg van de fout-hints (intern) mee met de nieuwe opgave; goede invoer opnieuw uit het antwoord
    bed = {oud['totaal']: nieuw['totaal'], oud['antwoord']: nieuw['antwoord'], oud['betaald'] + oud['totaal']: nieuw['betaald'] + nieuw['totaal']}
    bed.update({_c(k): _c(v) for k, v in kaart.items() if v is not None and _c(k) is not None and _c(k) not in bed})
    def _bedr(t):
        return re.sub(r'€?(\d+),(\d\d)\b', lambda mm: (_e(bed[x]) if mm.group(0).startswith('€') else _e(bed[x])[1:]) if (x := int(mm.group(1)) * 100 + int(mm.group(2))) in bed else mm.group(0), t)
    for fh in it['extraVelden'].get('claudeFoutHints') or []:
        if fh.get('uitleg'): fh['uitleg'] = _bedr(fh['uitleg'])
    it['extraVelden']['claudeVeldenNa96'] = 'claudeKaleSom, claudeUitleg en de bedragen in claudeFoutHints zijn bijgewerkt naar de nieuwe opgave (#105)'
    antwoordvormen(it)
    it['merge']['fixlijst96'] = {'opgaveVoor': o, 'sleutels': kaart}
    LOG['96'].append({'claudeId': it['bron']['claudeId'], 'voor': o, 'na': it['opgave'], 'antwoord': it['antwoord'], 'sleutels': kaart})

def antwoordvormen(it):
    """#105: antwoordOokGoed en geldInvoer altijd uit het huidige antwoord (regel #33 en N14). Aanroepen na elke wijziging van het antwoord."""
    a = FR._cent(it['antwoord']) if str(it['antwoord']).startswith('€') else None
    if a is None: return
    e, c = divmod(a, 100); kaal = FR.geld(a)[1:]
    if 'antwoordOokGoed' in it: it['antwoordOokGoed'] = [kaal] + ([kaal.replace(',', '.')] if ',' in kaal else [])
    if it.get('geldInvoer'):
        acc = [FR.geld(a), kaal, f'€ {kaal}', f'€{e},{c:02d}', f'{e},{c:02d}', f'€ {e},{c:02d}'] + ([f'€{e},{c // 10}', f'{e},{c // 10}'] if c % 10 == 0 and c else [])
        it['geldInvoer'] = dict(it['geldInvoer'], sleutel=FR.geld(a), accepteer=list(dict.fromkeys(acc)), punt=dict(it['geldInvoer'].get('punt') or {}, voorbeeld=f'{e}.{c:02d}'))

def fix98(it):
    """S3/#98: VERH-E01 #1 'In het nest liggen 76 botten. Een kwart ervan is groen.' → knikkers in een doos. Teksten in de hints
    noemen 'botten': die past Oefeningen aan."""
    if it['merge'].get('doel') != 'G5-VERH-E01' or not re.match(r'In het nest liggen \d+ botten\. Een kwart ervan is groen\.', it['opgave']): return
    voor = it['opgave']; f = lambda x: x.replace('In het nest liggen', 'In de doos zitten').replace('groene botten', 'groene knikkers').replace('botten', 'knikkers') if isinstance(x, str) else x
    it['opgave'] = f(it['opgave']); ev = it['extraVelden']
    for k in ('claudeUitleg', 'claudeKaleSom', 'claudeStrategie'): ev[k] = f(ev.get(k)) if k in ev else ev.get(k)
    for fh in ev.get('claudeFoutHints') or []: fh['uitleg'] = f(fh.get('uitleg'))
    it['merge']['fixlijst98'] = True; LOG['98'].append({'claudeId': it['bron']['claudeId'], 'voor': voor, 'na': it['opgave']})

OPGAVE99 = {   # S8 (#99): VBN-E03 016 en 022 taal; 019 was een keersom, nu een patroon (zelfde antwoord 54)
    'Op een muur liggen tegels in rijen. In rij 1 liggen 5 tegels, in rij 2 tien tegels en in rij 3 vijftien tegels. Hoeveel tegels liggen er in rij 9?':
        'Op een muur zitten tegels in rijen. In rij 1 zitten 5 tegels, in rij 2 tien tegels en in rij 3 vijftien tegels. Hoeveel tegels zitten er in rij 9?',
    'Bij 1 tafel passen er 4 stoelen. Bij elke tafel erbij komen er 4 stoelen bij. Hoeveel stoelen passen er bij 15 tafels?':
        'Bij 1 tafel passen er 4 stoelen. Bij elke extra tafel komen er 4 stoelen bij. Hoeveel stoelen passen er bij 15 tafels?',
    'In elk zakje zitten 6 knikkers. Hoeveel knikkers zitten er in 9 zakjes?':
        'In zakje 1 zitten 6 knikkers, in zakje 2 twaalf knikkers en in zakje 3 achttien knikkers. Zo gaat het verder. Hoeveel knikkers zitten er in zakje 9?',
}
def fix99(it):
    if it['merge'].get('doel') != 'G5-VBN-E03' or it['opgave'] not in OPGAVE99: return
    voor = it['opgave']; it['opgave'] = OPGAVE99[voor]
    it['merge']['fixlijst99'] = True; LOG['99'].append({'claudeId': it['bron']['claudeId'], 'voor': voor, 'na': it['opgave']})

def fix109(it):
    """#109 (Didactiek 18:54, zacht §1.4): (a) MKU-E02 #2/#3: de opgave legt 'vlak' uit vóór 'ribbe';
    (b) VBN-E03 016: de Claude-fout-hint zegt 'liggen', de opgave sinds #99 'zitten'."""
    d = it['merge'].get('doel')
    zin = 'Een ribbe is de rand waar twee vlakken tegen elkaar zitten.'
    if d == 'G5-MKU-E02' and it['opgave'].startswith(zin):
        voor = it['opgave']; it['opgave'] = 'Een vlak is een platte kant van de figuur. ' + voor
        it['merge']['fixlijst109'] = 'vlak vóór ribbe'; LOG['109'].append({'claudeId': it['bron']['claudeId'], 'voor': voor, 'na': it['opgave']})
    if d == 'G5-VBN-E03' and re.search(r'\bzitten\b', it['opgave']):
        for k in ('claudeFoutHints',):
            for fh in it['extraVelden'].get(k) or []:
                if 'In elke rij liggen steeds' in (fh.get('uitleg') or ''):
                    fh['uitleg'] = fh['uitleg'].replace('In elke rij liggen steeds', 'In elke rij zitten steeds')
                    it['merge']['fixlijst109'] = "'liggen' → 'zitten' in de Claude-fout-hint"; LOG['109'].append({'claudeId': it['bron']['claudeId'], 'fout': fh['fout']})
        for fh in it.get('foutHints') or []:
            if 'In elke rij liggen steeds' in (fh.get('uitleg') or ''): fh['uitleg'] = fh['uitleg'].replace('In elke rij liggen steeds', 'In elke rij zitten steeds')

# #118 (Didactiek 19:16, besluit Overzicht): MEET-E07 #2 'Je hebt dit geld. Je koopt iets van €#. Hoeveel houd je over?' — het antwoord
# is nooit de prijs en ook niet de prijs ± 10 cent (zoals #106/#112 bij #3 en #4). claudeId → (munten in cent, opties, {oude sleutel: nieuwe}).
NIEUW118 = {
    'd7c38406-85ac-4e25-a932-fbbc26fe5eec': ([200, 100, 50], ['€2,50', '€2', '€4,50'], {'€3': '€4,50', '€0,50': '€2'}),        # 287: €1 = de prijs (voorstel Didactiek)
    'cb2ee233-121e-4bce-acbc-18a7f4fecdc0': ([100, 50, 50, 20], ['€120', '€3,20', '€1,20'], {'€2,90': '€3,20', '€90': '€120'}),  # 282: €0,90 = prijs − 10 cent
}
def fix118(it):
    m = re.fullmatch(r'Je hebt dit geld\. Je koopt iets van (€\d+(?:,\d\d)?)\. Hoeveel houd je over\?', it['opgave'] or '')
    if it['merge'].get('doel') != 'G5-MEET-E07' or not m: return
    cid = it['bron']['claudeId']
    if cid in NIEUW118:
        munten, opties, kaart = NIEUW118[cid]; jr = it['visual']['jsRender']
        voor = {'munten': list(jr['munten']), 'antwoord': it['antwoord'], 'opties': [o['tekst'] for o in it['opties']]}
        jr['munten'] = list(munten)
        it['antwoord'] = _e(sum(munten) - FR._cent(m.group(1)))
        it['opties'] = [{'letter': 'ABC'[k], 'tekst': t} for k, t in enumerate(opties)]
        it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
        ev = it['extraVelden']
        for k in ('claudeDenkfouten', 'claudeFoutHints'):
            for d in ev.get(k) or []: d['fout'] = kaart.get(d['fout'], d['fout'])
        for f in it.get('foutHints') or []: f['fout'] = kaart.get(f['fout'], f['fout'])
        ev['claudeVeldenNa118'] = 'munten, antwoord, opties en de Claude-sleutels (claudeDenkfouten/claudeFoutHints) bijgewerkt (#118)'
        antwoordvormen(it)
        it['merge']['fixlijst118'] = {'voor': voor, 'sleutels': kaart}
        LOG['118'].append({'claudeId': cid, 'voor': voor, 'na': {'munten': munten, 'antwoord': it['antwoord'], 'opties': opties}})
    p_, a_ = FR._cent(m.group(1)), FR._cent(it['antwoord'])
    assert sum(it['visual']['jsRender']['munten']) - p_ == a_, ('#118 som', cid)
    assert abs(a_ - p_) not in (0, 10), ('#118: antwoord = prijs of prijs ± 10 cent', cid, it['opgave'], it['antwoord'])
    assert it['antwoord'] in [o['tekst'] for o in it['opties']], ('#118 antwoord niet in de opties', cid)

# ------------------------------------------------------------------ #121 (besluit Dave 20:04, advies Didactiek recheck-g5-eind §4)
# Een foute route mag niet het goede antwoord geven. Vervangen (zelfde id, zelfde plek): VBN-E01 tabel #3 (totaal van een rij: geen andere rij
# en geen kolom met dezelfde som), tabel #4 (verschil tussen twee dagen: niet dezelfde dagen in een andere rij, geen ander paar dagen in dezelfde
# rij, geen cel gelijk aan het antwoord) en GET-M06 #4 (verdelen met rest: het antwoord is niet het getal waarover je verdeelt).
# De asserts gelden voor elk item van die somtypen. De kleinere gevallen (M05 #2, M06 #5/#7, E06 #2, VBN-E01 #1 staaf) blijven en staan in de log.
POOL121 = [35, 60, 85, 110, 125, 150, 175, 190, 215, 250]
T3 = re.compile(r'^Hoeveel (\S+) in totaal\?$'); T4 = re.compile(r'^Hoeveel (\S+) meer op (\S+) dan op (\S+)\?$')
M64 = re.compile(r'^(\d+) (.+?) worden eerlijk verdeeld over (\d+) (.+?)\. Hoeveel krijgt (.+?)\? \(De rest blijft over\.\)$')
def _tab(jr): return [list(r['waarden']) for r in jr['rijen']]
def _bots3(T, ar):
    A = sum(T[ar]); b = [f'rij {r}' for r in range(len(T)) if r != ar and sum(T[r]) == A]
    return b + [f'kolom {c}' for c in range(len(T[0])) if sum(T[r][c] for r in range(len(T))) == A]
def _bots4(T, ar, d1, d2):
    A = T[ar][d1] - T[ar][d2]; b = [f'rij {r}' for r in range(len(T)) if r != ar and abs(T[r][d1] - T[r][d2]) == A]
    cs = [c for c in range(len(T[0]))]
    b += [f'dagen {x}/{y}' for i, x in enumerate(cs) for y in cs[i + 1:] if {x, y} != {d1, d2} and abs(T[ar][x] - T[ar][y]) == A]
    return b + [f'cel {r}/{c}' for r in range(len(T)) for c in cs if T[r][c] == A]
def _routes(T, ar, vaste):
    R = len(T); C = len(T[0]); cel = [(r, c) for r in range(R) for c in range(C)]
    out = [('cel', p) for p in cel] + [('rij', r) for r in range(R)] + [('kol', c) for c in range(C)]
    out += [('rijmin', ar, c) for c in range(C)] + [(k, p, q) for k in ('som2', 'vers2') for i, p in enumerate(cel) for q in cel[i + 1:]]
    import itertools
    out += [('deel', ar, cs) for n in range(2, C) for cs in itertools.combinations(range(C), n)]
    vast = lambda x: sum(1 for p in (x[1:] if x[0] in ('cel', 'som2', 'vers2') else []) if p in vaste)
    return sorted(out, key=lambda x: -vast(x))
def _eval(rt, T):
    k = rt[0]
    if k == 'cel': return T[rt[1][0]][rt[1][1]]
    if k == 'rij': return sum(T[rt[1]])
    if k == 'kol': return sum(r[rt[1]] for r in T)
    if k == 'rijmin': return sum(T[rt[1]]) - T[rt[1]][rt[2]]
    if k == 'som2': return T[rt[1][0]][rt[1][1]] + T[rt[2][0]][rt[2][1]]
    if k == 'vers2': return abs(T[rt[1][0]][rt[1][1]] - T[rt[2][0]][rt[2][1]])
    if k == 'deel': return sum(T[rt[1]][c] for c in rt[2])
# Volgorde = de volgorde van de regels in batch6.json (#3: som van de rij, som van de kolom, andere cel, som van twee cellen, Claudes sleutel
# 'één vergeten', verschil van twee cellen; #4: andere cel, som van de rij, som van twee cellen, verschil van twee cellen). De motor geeft een
# foute optie de soort van de eerste regel die past; met dezelfde volgorde houdt elke nieuwe optie de soort van de oude optie.
PRIO121 = {3: ('rij', 'kol', 'cel', 'som2', 'rijmin', 'vers2', 'deel'), 4: ('cel', 'rij', 'som2', 'vers2', 'kol', 'rijmin', 'deel')}
def _route_van(v, soort, T, ar, vaste):
    """De route die een foute optie maakt, met een vaste voorrang (niet afhankelijk van een vorige build): eerst routes met de gevraagde
    rij/cellen, dan de soort route in de volgorde van PRIO121 (= de volgorde van de regels van de motor)."""
    alle = _routes(T, ar, vaste)
    for kind in PRIO121[soort]:
        for rt in alle:
            if rt[0] == kind and (kind not in ('rij',) or True) and _eval(rt, T) == v: return rt
    return None
def _label121(v, soort, T, ar, d):
    """Zoals de motor (fout_regels._tabel_trede + volgorde van de regels in batch6.json) de soort van een foute optie kiest:
    de regel met de laagste (trede, plaats). Trede: andere cel 0; som van de gevraagde rij 1, andere rij 4; som van een gevraagde kolom 2,
    andere kolom 4; som/verschil van twee cellen en Claudes sleutel 3; andere fout 9."""
    R, C = len(T), len(T[0]); cel = [T[r][c] for r in range(R) for c in range(C)]
    rs = [sum(x) for x in T]; ks = [sum(T[r][c] for r in range(R)) for c in range(C)]
    p2 = {cel[i] + cel[j] for i in range(len(cel)) for j in range(i + 1, len(cel))}; v2 = {abs(cel[i] - cel[j]) for i in range(len(cel)) for j in range(i + 1, len(cel))}
    gk = {ks[c] for c in d} if d else set()
    regels = ([('rij', v in rs, 1 if v == rs[ar] else 4), ('kol', v in ks, 2 if v in gk else 4), ('cel', v in cel, 0), ('som2', v in p2, 3),
               ('rijmin', v in {rs[ar] - T[ar][c] for c in range(C)}, 3), ('vers2', v in v2, 3)] if soort == 3 else
              [('cel', v in cel, 0), ('rij', v in rs, 1 if v == rs[ar] else 4), ('som2', v in p2, 3), ('vers2', v in v2, 3)])
    pas = [(t, i, k) for i, (k, ok, t) in enumerate(regels) if ok]
    return min(pas)[2] if pas else 'andere fout'
def _kaart(it, kaart):
    ev = it['extraVelden']
    for k in ('claudeDenkfouten', 'claudeFoutHints'):
        for d in ev.get(k) or []: d['fout'] = kaart.get(d['fout'], d['fout'])
    for o in it['opties'] or []: o['tekst'] = kaart.get(o['tekst'], o['tekst'])
    it['optiesTekst'] = ' · '.join(f"{o['letter']}) {o['tekst']}" for o in it['opties'])
def fix121_tabel(it):
    if it['merge'].get('doel') != 'G5-VBN-E01': return
    jr = it['visual']['jsRender'] or {}
    if jr.get('soort') != 'tabel': return
    o = it['opgave']; namen = [r['naam'] for r in jr['rijen']]; kol = list(jr['kolommen'])
    if (m := T3.match(o)) and m.group(1) in namen: soort, ar, d = 3, namen.index(m.group(1)), None
    elif (m := T4.match(o)) and m.group(1) in namen and m.group(2) in kol and m.group(3) in kol:
        soort, ar, d = 4, namen.index(m.group(1)), (kol.index(m.group(2)), kol.index(m.group(3)))
    else: return
    T = _tab(jr); cid = it['bron']['claudeId']
    bots = _bots3(T, ar) if soort == 3 else _bots4(T, ar, *d)
    if bots:
        A = int(it['antwoord']); vaste = {(ar, c) for c in range(len(T[0]))} if soort == 3 else {(ar, d[0]), (ar, d[1])}
        fout = [x['tekst'] for x in it['opties'] if x['tekst'] != it['antwoord']]
        routes = {v: _route_van(int(v), soort, T, ar, vaste) for v in fout}
        assert all(routes.values()), ('#121 geen route voor een foute optie', cid, routes)
        k = 0
        while True:
            k += 1; assert k < 5000, ('#121 geen nieuwe tabel gevonden', cid)
            x = h(f'{cid}-121-{k}'); N = [list(r) for r in T]
            for r in range(len(N)):
                vrij = [c for c in range(len(N[0])) if (r, c) not in vaste]
                if not vrij: continue
                keuze = [v for v in POOL121 if v not in [N[r][c] for c in range(len(N[0])) if (r, c) in vaste]]
                y = x; perm = []
                while len(perm) < len(vrij):
                    y = h(f'{y}'); kand = keuze[y % len(keuze)]
                    if kand not in perm: perm.append(kand)
                for c, v in zip(vrij, perm): N[r][c] = v
                x = h(f'{x}-{r}')
            if (_bots3(N, ar) if soort == 3 else _bots4(N, ar, *d)): continue
            nieuw = {v: str(_eval(routes[v], N)) for v in fout}
            vals = list(nieuw.values())
            if len(set(vals)) != len(vals) or str(A) in vals or any(int(v) <= 0 for v in vals): continue
            if any(_label121(int(nieuw[v]), soort, N, ar, d) != _label121(int(v), soort, T, ar, d) for v in fout): continue   # zelfde soort als de oude optie
            break
        # #123 (Didactiek recheck-121 V-121a, besluit Dave 20:46): de zoektocht hierboven blijft zoals hij was (dezelfde tabellen), maar een optie
        # 'één vergeten' (Claudes denkfout deel-vergeten-bij-splitsen) is de rijsom min één cel van de GEVRAAGDE rij. Die rij verandert niet,
        # dus de oude waarde blijft (en niet een som van twee willekeurige cellen uit de nieuwe tabel).
        if soort == 3:
            dk = {x['fout']: x['denkfout'] for x in it['extraVelden'].get('claudeDenkfouten') or []}
            rm = {sum(T[ar]) - T[ar][c]: c for c in range(len(T[0]))}
            for v in fout:
                if dk.get(v) == 'deel-vergeten-bij-splitsen' and int(v) in rm and nieuw[v] != v:
                    LOG['123'].append({'id': it.get('id'), 'claudeId': cid, 'opgave': o, 'optie': [nieuw[v], v], 'route': f'rij − cel {rm[int(v)]}'})
                    nieuw[v] = v; routes[v] = ('rijmin', ar, rm[int(v)])
            vals = list(nieuw.values()); RS = [sum(x) for x in N]; KS = [sum(x[c] for x in N) for c in range(len(N[0]))]
            assert len(set(vals)) == len(vals) and str(A) not in vals, ('#123: dubbele optie of het antwoord', cid, nieuw)
            for v in fout:
                if routes[v][0] == 'rijmin':
                    w = int(nieuw[v]); assert w not in RS and w not in KS and all(w not in x for x in N), ('#123: één vergeten botst met de nieuwe tabel', cid, w)
        voor = {'tabel': T, 'opties': [x['tekst'] for x in it['opties']]}
        for r, rij in zip(jr['rijen'], N): r['waarden'] = rij
        _kaart(it, {v: n for v, n in nieuw.items() if v != n})
        it['merge']['fixlijst121'] = {'voor': voor, 'botsing': bots, 'routes': {v: list(map(str, routes[v])) for v in fout}}
        LOG['121'].append({'id': it.get('id'), 'claudeId': cid, 'somtype': f'VBN-E01 #{soort}', 'opgave': o, 'antwoord': it['antwoord'], 'botsing': bots,
                           'voor': voor, 'na': {'tabel': N, 'opties': [x['tekst'] for x in it['opties']]}})
    T = _tab(jr)
    assert not (_bots3(T, ar) if soort == 3 else _bots4(T, ar, *d)), ('#121: een foute route geeft het goede antwoord', cid, o)
    if soort == 3:      # #123: in elk item is 'één vergeten' de rijsom min één cel van de gevraagde rij
        for x in it['extraVelden'].get('claudeDenkfouten') or []:
            if x['denkfout'] == 'deel-vergeten-bij-splitsen' and x['fout'] in [y['tekst'] for y in it['opties']]:
                assert int(x['fout']) in {sum(T[ar]) - T[ar][c] for c in range(len(T[0]))}, ('#123: één vergeten is geen rij − één cel', cid, x['fout'])
    assert (sum(T[ar]) if soort == 3 else T[ar][d[0]] - T[ar][d[1]]) == int(it['antwoord']), ('#121 antwoord', cid)
def fix121_verdelen(it):
    if it['merge'].get('doel') != 'G5-GET-M06' or not (m := M64.match(it['opgave'] or '')): return
    n, dd = int(m.group(1)), int(m.group(3)); q, r = divmod(n, dd); cid = it['bron']['claudeId']
    if q == dd:
        k = 0
        while True:
            k += 1; assert k < 500, ('#121 M06 geen nieuw getal', cid)
            x = h(f'{cid}-121-{k}'); q2 = 2 + x % 9; r2 = 1 + (x >> 8) % (dd - 1) if dd > 1 else 0; n2 = q2 * dd + r2
            sleutels = [q2 + 1, r2, n2 - dd, n2 * dd, dd]
            if q2 == dd or r2 == 0 or len(set(sleutels)) != 5 or q2 in sleutels or n2 in GEBRUIKT121.get(dd, set()) or n2 > 100: continue
            break
        oud = it['opgave']; kaart = {str(q + 1): str(q2 + 1), str(r): str(r2)}
        it['opgave'] = M64.sub(lambda m_: f"{n2} {m_.group(2)} worden eerlijk verdeeld over {dd} {m_.group(4)}. Hoeveel krijgt {m_.group(5)}? (De rest blijft over.)", oud)
        it['antwoord'] = str(q2); ev = it['extraVelden']
        ev['claudeKaleSom'] = f'{n2} : {dd} = __ rest {r2}'
        ev['claudeUitleg'] = f'Zoek in de tafel van {dd}: {dd} × {q2} = {dd * q2} past nog, {dd} × {q2 + 1} = {dd * (q2 + 1)} niet.\nDus {q2}, rest {r2}.'
        for kk in ('claudeDenkfouten', 'claudeFoutHints'):
            for f in ev.get(kk) or []: f['fout'] = kaart.get(f['fout'], f['fout'])
        it['merge']['fixlijst121'] = {'voor': {'opgave': oud, 'antwoord': str(q)}}
        bov = int(re.sub(r'\D', '', (it.get('getallenruimte') or '0').split('–')[-1]) or 0)
        if bov < n2:      # #125 (Didactiek recheck-121): '0–20' van het oude item past niet bij 33 of 38
            it['merge']['fixlijst121']['getallenruimteVoor'] = it.get('getallenruimte'); it['getallenruimte'] = '0–100'
            LOG['125'].append({'claudeId': cid, 'opgave': it['opgave'], 'getallenruimte': [it['merge']['fixlijst121']['getallenruimteVoor'], '0–100']})
        LOG['121'].append({'id': it.get('id'), 'claudeId': cid, 'somtype': 'GET-M06 #4', 'opgave': oud, 'nieuw': it['opgave'], 'antwoord': [str(q), str(q2)], 'sleutels': kaart})
        n, q, r = n2, q2, r2
    GEBRUIKT121.setdefault(dd, set()).add(n)
    bov = int(re.sub(r'\D', '', (it.get('getallenruimte') or '0').split('–')[-1]) or 0)
    assert bov >= n, ('#125: getallenruimte kleiner dan het totaal', cid, it['opgave'], it.get('getallenruimte'))
    assert q != dd, ('#121: antwoord = het getal waarover je verdeelt', cid, it['opgave'])
GEBRUIKT121 = {}
KLEIN121 = {   # §4 van recheck-g5-eind: laten staan, wel loggen (besluit Dave 20:04)
    'GET-M05 #2 (de deler overnemen is goed: 4 : 2, 49 : 7)': ['073', '085'], 'GET-M06 #5 (64 : 8 = 8)': ['011'], 'GET-M06 #7 (58/59 kinderen, 8 per tafel → 8)': ['002', '003'],
    'GET-E06 #2 (€4,80 − €2,40: het tweede getal overnemen is goed)': ['601'], "VBN-E01 #1 staaf (antwoord = 'Elk streepje is …')": ['115', '144', '158', '161', '166', '174']}
LOG['121-laten-staan'] = [{'waar': k, 'items': v} for k, v in KLEIN121.items()]

def per_item(it, q):
    fix75(it); fix85(it); fix86(it); fix87(it); fix78(it); fix_bijkomt(it); fix96(it); fix98(it); fix99(it); fix109(it); fix118(it); fix121_tabel(it); fix121_verdelen(it)

# ------------------------------------------------------------------ #83
WEG83 = {'G5-MEET-E01-claude-bank-017': r'\b1 km\b', 'G5-MEET-E01-claude-bank-058': r'\b1 m\b', 'G5-MEET-E04-claude-bank-003': r'\b1 [lL]\b|1 liter', 'G5-MEET-E05-claude-bank-005': r'\b1 kg\b'}
def na_ids(rows, GESCHRAPT):
    weg = []
    for r in rows:
        if r['id'] in WEG83:
            tekst = ' '.join([r['opgave']] + [o['tekst'] for o in r['opties'] or []])
            if not re.search(WEG83[r['id']], tekst): raise SystemExit(f"#83: {r['id']} verklapt de basismaat niet ({r['opgave'][:60]}); id verschoven? controleer WEG83")
            weg.append(r)
            GESCHRAPT.append({'claudeId': r['bron']['claudeId'], 'id': r['id'], 'groep': 'Didactiek #83 basismaat verklapt', 'subregel': 'merge-fixlijst #83',
                              'doel': r['merge']['doel'] or r['merge']['voorstelDoel'], 'vraag': r['opgave']})
            LOG['83'].append({'id': r['id'], 'opgave': r['opgave']})
    if len(weg) != len(WEG83): raise SystemExit(f"#83: {len(weg)} van {len(WEG83)} items gevonden")
    return [r for r in rows if r not in weg]

# ------------------------------------------------------------------ #84
KOP84 = 'Hoeveel dagen duurt het van # [maand] tot # [maand]? — één maandgrens (generator #84)'
def generator_84(sjabloon, n=20):
    """Deterministisch: begin in maart–november (geen februari), eind in de volgende maand (precies één maandgrens, geen jaargrens),
    hoogstens 31 dagen, de begindag telt niet mee: antwoord = (eind − begin).days."""
    def kandidaten(zaad):
        k = 0
        while True:
            k += 1; x = h(f'{zaad}-{k}')
            m1 = 3 + x % 9                                  # 3..11
            dim = (datetime.date(2025, m1 + 1, 1) - datetime.date(2025, m1, 1)).days
            d1 = 1 + (x >> 8) % dim; d2 = 1 + (x >> 16) % 28
            a, b = datetime.date(2025, m1, d1), datetime.date(2025, m1 + 1, d2); n_d = (b - a).days
            if not (2 <= n_d <= 31) or (b.year * 12 + b.month) - (a.year * 12 + a.month) != 1: continue
            yield (m1, d1, d2, n_d)
    # #110 (Oefeningen 19:06): geen item waarin het verschil van de dagnummers gelijk is aan het antwoord (16 nov → 1 dec: 16 − 1 = 15 = 15 dagen;
    # dan helpt 'dagnummers aftrekken' toevallig). Zo'n item krijgt (op dezelfde plaats en met hetzelfde claudeId) de eerste goede
    # kandidaat uit een eigen reeks ('g5-gen84-v110'). De andere items blijven precies gelijk.
    slecht = lambda p: abs(p[2] - p[1]) == p[3]
    # #151 (besluit Dave 19:14): geen twee sleutels van een item op hetzelfde getal. De sleutels zijn de regels van de entry (#11):
    # getal1 − getal2 (afgetrokken), getal2 (alleen de nieuwe maand), antwoord − getal2 (alleen de eerste maand), antwoord ± 1.
    def sleutels(p):
        m1, d1, d2, n_d = p; dim = (datetime.date(2025, m1 + 1, 1) - datetime.date(2025, m1, 1)).days
        return [abs(d2 - d1), d2, dim - d1, n_d - 1, n_d + 1]
    def schoon(p): ks = sleutels(p); return len(set(ks)) == len(ks)
    # #114 (Didactiek 19:15, vervangt #111): het eerste stuk is minstens 2 dagen (de begindag ligt minstens 2 dagen vóór het eind van de
    # maand), en geen fout-sleutel is gelijk aan het antwoord (30 juni → 26 juli: 'alleen de nieuwe maand' = 26 = het antwoord).
    def eerste_stuk(p): m1, d1 = p[0], p[1]; return (datetime.date(2025, m1 + 1, 1) - datetime.date(2025, m1, 1)).days - d1
    def goed114(p): return eerste_stuk(p) >= 2 and p[3] not in sleutels(p)
    def vervanger_ok(p): ks = sleutels(p); return schoon(p) and goed114(p) and min(ks) >= 1
    plan = []; g = kandidaten('g5-gen84')
    while len(plan) < n:
        p = next(g)
        if all(q[:3] != p[:3] for q in plan): plan.append(p)
    vervang = kandidaten('g5-gen84-v110')
    for j, p in enumerate(plan):
        if slecht(p) or not schoon(p) or not goed114(p):
            while True:
                q = next(vervang)
                if not slecht(q) and vervanger_ok(q) and all(r[:3] != q[:3] for r in plan): break
            LOG['110' if slecht(p) else '151' if not schoon(p) else '114'].append({'claudeId': f'g5-gen84-{j + 1:02d}', 'was': f'{p[1]} {MAANDEN[p[0] - 1]} → {p[2]} {MAANDEN[p[0]]} ({p[3]} dagen)',
                               'wordt': f'{q[1]} {MAANDEN[q[0] - 1]} → {q[2]} {MAANDEN[q[0]]} ({q[3]} dagen)'})
            plan[j] = q
    # Oef-#427 (na-ronde G5, Oefeningen 8 okt): geen begindag die gelijk is aan antwoord ± 1 (gen-001: 24 oktober → 18 november, 25 dagen; '24' is
    # de begindag én 'één dag te weinig', en #390 slaat die over → 'andere fout'). Eigen reeks ('g5-gen84-v427'), zodat de eerdere vervangers
    # (#110/#151/#114) en de andere items precies gelijk blijven; de vervanger heeft ook geen begindag op een andere sleutel.
    v427 = kandidaten('g5-gen84-v427')
    for j, p in enumerate(plan):
        if p[1] in (p[3] - 1, p[3] + 1):
            while True:
                q = next(v427)
                if not slecht(q) and vervanger_ok(q) and q[1] not in (q[3] - 1, q[3] + 1) and q[1] not in sleutels(q) and all(r[:3] != q[:3] for r in plan): break
            LOG.setdefault('427', []).append({'claudeId': f'g5-gen84-{j + 1:02d}', 'was': f'{p[1]} {MAANDEN[p[0] - 1]} → {p[2]} {MAANDEN[p[0]]} ({p[3]} dagen)',
                                             'wordt': f'{q[1]} {MAANDEN[q[0] - 1]} → {q[2]} {MAANDEN[q[0]]} ({q[3]} dagen)'})
            plan[j] = q
    assert not any(p[1] in (p[3] - 1, p[3] + 1) for p in plan), 'Oef-#427: begindag = antwoord ± 1'
    assert not any(slecht(p) for p in plan), '#110: verschil van de dagnummers = antwoord'
    assert all(schoon(p) for p in plan), '#151: twee sleutels van een item op hetzelfde getal'
    assert all(eerste_stuk(p) >= 2 for p in plan), '#114: het eerste stuk is korter dan 2 dagen'
    assert all(p[3] not in sleutels(p) for p in plan), '#114: een fout-sleutel is gelijk aan het antwoord'
    uit = []; i = 0
    for m1, d1, d2, n_d in plan:
        i += 1; it = copy.deepcopy(sjabloon); cid = f'g5-gen84-{i:02d}'
        it['opgave'] = f'Hoeveel dagen duurt het van {d1} {MAANDEN[m1 - 1]} tot {d2} {MAANDEN[m1]}?'; it['antwoord'] = str(n_d)
        it['hint'] = None; it['sterkereHint'] = None; it['ouderzin'] = None; it['foutHints'] = []; it['foutHintsTekst'] = None
        ev = it['extraVelden']
        for kk in list(ev):
            if kk.startswith('claude'): ev[kk] = [] if isinstance(ev[kk], list) else None
        ev['mergeFoutHints'] = []; ev['niveauVoorlopig'] = True
        it['bronVariant'] = f'merge-generator:G5-#84:{cid}'
        it['bron'] = {'bestand': 'scripts/fixlijst_g5b.py', 'type': 'merge-generator', 'claudeId': cid, 'claudeDoel': 'merge-generator #84', 'claudeDoelTitel': 'geen Claude-item',
                      'claudeGroep': None, 'claudeBron': None, 'claudeVersie': None, 'generator': 'G5-#84 (merge-fixlijst #84, Didactiek 18:15)',
                      'sjabloonClaudeId': sjabloon['bron']['claudeId']}
        it['licentie'] = dict(it['licentie'], gewijzigd=True, wijzigingen=['G5-#84 generator (vorm naar het sjabloon van #1)'])
        it['merge'] = {'status': 'gemapt', 'doel': 'G5-MEET-E06', 'voorstelDoel': None, 'regel': 'G5-FX84 generator',
                       'reden': 'merge-fixlijst #84: nieuw somtype in G5, dagen tellen over precies één maandgrens (≤ 31 dagen, geen februari, begindag niet mee)',
                       'somtype': KOP84, 'nieuwSomtype84': True, '_k': None}
        it['merge'].pop('_k'); it['_k'] = (m1, d1, d2)
        it['doelId'] = 'G5-MEET-E06'                       # #122 (Didactiek 20:04): het sjabloon is een geparkeerd item met doelId null
        it['controle'] = {'antwoord': 'ok', 'verwacht': str(n_d), 'methode': 'G5-#84 generator (datetime, begindag niet mee)', 'mcAntwoordInOpties': None,
                          'dubbeleOptie': False, 'foutAntwoordGelijkAanGoed': False, 'notatie': [], 'claudeUitlegInKindtekst': None,
                          'claudeVorm': {'antwoord': None, 'verwacht': None, 'methode': 'geen Claude-item'}}
        uit.append(it); LOG['84'].append({'claudeId': cid, 'opgave': it['opgave'], 'antwoord': it['antwoord']})
    for it in uit: it.pop('_k')
    return uit

def schrijf_log(path):
    json.dump({'uitleg': 'Log van scripts/fixlijst_g5b.py (merge-fixlijst #75, #83–#87; 1 okt 18:30). Elke build opnieuw.',
               'aantallen': {k: len(v) for k, v in LOG.items()}, **{k: v for k, v in LOG.items()}}, open(path, 'w'), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------------------------------------------------------
# #100 (Oefeningen 18:42, bij #73): MEET-E06 'Zet de klok op …' (invoer 'h:mm') — per soort tijd ten minste 5 items.
# Soorten: vijf/tien over · vijf/tien voor · rond half (vijf/tien voor/over half) · kwart over/voor · half.
# De 7 Claude-items blijven; de generator vult aan tot 5 per soort. Vorm, hints en antwoordDetail (#73) komen van het sjabloon
# (een #23-item); de sleutels maakt de motor (fout_regels: 'klok een uur te laat', 'grote wijzer verkeerd').
UREN = ['één', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf']
def klok_tijd(tekst):
    """'tien voor half zes' → '5:20' (12-uursklok, 0 → 12). None als de tekst geen kloktijd is."""
    m = re.fullmatch(r'(?:(vijf|tien|kwart) (over|voor) )?(half )?(\w+)', tekst)
    if not m or m.group(4) not in UREN: return None
    u = UREN.index(m.group(4)) + 1; mn = 0
    if m.group(3): u -= 1; mn = 30
    if m.group(1):
        d = {'vijf': 5, 'tien': 10, 'kwart': 15}[m.group(1)]
        if m.group(1) == 'kwart' and m.group(3): return None
        mn += d if m.group(2) == 'over' else -d
        if mn < 0: u -= 1; mn += 60
    elif not m.group(3): return None                      # alleen 'X uur' doen we hier niet
    u = (u - 1) % 12 + 1
    return f'{u}:{mn:02d}'
def soort100(tekst):
    if re.match(r'(vijf|tien) (over|voor) half ', tekst): return 'rond half'
    if re.match(r'(vijf|tien) over ', tekst): return 'vijf/tien over'
    if re.match(r'(vijf|tien) voor ', tekst): return 'vijf/tien voor'
    if tekst.startswith('kwart '): return 'kwart over/voor'
    if tekst.startswith('half '): return 'half'
    return None
VORMEN100 = {'vijf/tien over': ['vijf over', 'tien over'], 'vijf/tien voor': ['vijf voor', 'tien voor'],
             'rond half': ['vijf voor half', 'tien voor half', 'vijf over half', 'tien over half'],
             'kwart over/voor': ['kwart over', 'kwart voor'], 'half': ['half']}
def generator_100(rows, minimum=5):
    bestaand = [r for r in rows if r['merge'].get('doel') == 'G5-MEET-E06' and r['merge']['status'] == 'gemapt'
                and re.fullmatch(r'Zet de klok op (.+)\.', r['opgave'])]
    if not bestaand: return []
    sjabloon = min(bestaand, key=lambda r: r['bron']['claudeId'])
    teksten = {re.fullmatch(r'Zet de klok op (.+)\.', r['opgave']).group(1) for r in bestaand}
    tel = collections.Counter(soort100(t) for t in teksten)
    uit = []; k = 0; i = 0
    for soort, vormen in VORMEN100.items():
        while tel[soort] < minimum:
            k += 1; x = h(f'g5-gen100-{soort}-{k}')
            t = f"{vormen[x % len(vormen)]} {UREN[(x >> 8) % 12]}".replace('half half', 'half')
            if t in teksten: continue
            tijd = klok_tijd(t); assert tijd and soort100(t) == soort, t
            teksten.add(t); tel[soort] += 1; i += 1; cid = f'g5-gen100-{i:02d}'
            it = copy.deepcopy(sjabloon)
            it['opgave'] = f'Zet de klok op {t}.'; it['antwoord'] = tijd
            it['foutHints'] = []; it['foutHintsTekst'] = None
            ev = it['extraVelden']
            for kk in list(ev):
                if kk.startswith('claude'): ev[kk] = [] if isinstance(ev[kk], list) else None
            ev['mergeFoutHints'] = []; ev['niveauVoorlopig'] = True
            it['bronVariant'] = f'merge-generator:G5-#100:{cid}'
            it['bron'] = {'bestand': 'scripts/fixlijst_g5b.py', 'type': 'merge-generator', 'claudeId': cid, 'claudeDoel': 'merge-generator #100',
                          'claudeDoelTitel': 'geen Claude-item', 'claudeGroep': None, 'claudeBron': None, 'claudeVersie': None,
                          'generator': 'G5-#100 (merge-fixlijst #100, Oefeningen 18:42; bij #73)', 'sjabloonClaudeId': sjabloon['bron']['claudeId']}
            it['licentie'] = dict(it['licentie'], gewijzigd=True, wijzigingen=['G5-#100 generator (vorm naar het sjabloon van klok zetten #23)'])
            m = it['merge']
            for kk in ('fixlijst85', 'fixlijst86', 'fixlijst87', 'duplicaatVan', 'vorigId', 'somtypeNr'): m.pop(kk, None)
            m.update({'regel': 'G5-FX100 generator', 'reden': f'merge-fixlijst #100: klok zetten, soort \'{soort}\' aangevuld tot {minimum} items', 'generator100': soort})
            it['controle'] = {'antwoord': 'ok', 'verwacht': tijd, 'methode': 'G5-#100 generator (tijd in woorden → h:mm, 12-uursklok)', 'mcAntwoordInOpties': None,
                              'dubbeleOptie': False, 'foutAntwoordGelijkAanGoed': False, 'notatie': [], 'claudeUitlegInKindtekst': None,
                              'claudeVorm': {'antwoord': None, 'verwacht': None, 'methode': 'geen Claude-item'}}
            uit.append(it); LOG['100'].append({'claudeId': cid, 'soort': soort, 'opgave': it['opgave'], 'antwoord': tijd})
    # nakijken: ook de 7 Claude-items moeten met klok_tijd kloppen
    for r in bestaand:
        t = re.fullmatch(r'Zet de klok op (.+)\.', r['opgave']).group(1)
        if klok_tijd(t) != r['antwoord']: LOG['100-afwijkend'].append({'id': r['bron']['claudeId'], 'opgave': r['opgave'], 'antwoord': r['antwoord'], 'verwacht': klok_tijd(t)})
    return uit
