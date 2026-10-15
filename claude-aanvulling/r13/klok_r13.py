#!/usr/bin/env python3
"""r13 kloktijdronde G3–G5 (besluit Didactiek 8 okt 15:46; steering Dave 16:09). Werkt op r13/g{3,4,5} (kopie van de goedgekeurde builds), nooit op live.
- echte digitale klok (kop '(opties digitaal)' / '(tijd digitaal)' met een tijd met ':') → digitaleKlok: true, verder niets;
- elders: tijd in lopende tekst '9.50 uur' (tools/kloktijd_fix.zet_om, typ_erbij=True: open vraag met een tijd als antwoord krijgt '(Typ als 14.30.)'
  en geldigeAntwoorden '14.30 uur' / '14.30' / '14:30'); klok-zetten (wijzers slepen): antwoord '9.00 uur' + geldigeAntwoorden met de 'h:mm' die de app
  doorgeeft; antwoordDetail.invoer/invoerUitleg (app-protocol) blijven zoals ze waren;
- dezelfde omzetting in hints/batch*.json (hint1, hint2, ouderzin, foutHints tekst/tekstSterker) en somtypen/*.md (kop en tekst), behalve bij digitale somtypes;
- daarna scripts/sync_hint_keys.py (koppen veranderen).
Gebruik: python3 r13/klok_r13.py 3 4 5  → rapport per groep (json in r13/klok_rapport.json)."""
import sys, os, json, glob, re, copy, subprocess, random
sys.path.insert(0, '/workspace/claude-merge/tools'); import kloktijd_fix as KF, kloktijd_check as KT
R13 = os.path.dirname(os.path.abspath(__file__))
DIGI = re.compile(r'\((opties|tijd) digitaal\)')
def omzet(it, tel):
    if KF.digitaal(it):
        if not it.get('digitaleKlok'): it['digitaleKlok'] = True; tel['vlag'] += 1
        return
    ad = it.get('antwoordDetail'); bewaar = {k: ad[k] for k in ('invoer', 'invoerUitleg') if isinstance(ad, dict) and k in ad}
    klokzet = (it.get('merge') or {}).get('somtype', '').startswith('[klok-zetten')
    oud_kop = (it.get('merge') or {}).get('somtype')
    n = KF.zet_om(it, typ_erbij=True)
    if isinstance(it.get('antwoordDetail'), dict): it['antwoordDetail'].update(bewaar)      # zet_om maakt een nieuw dict: app-protocol (invoer/invoerUitleg) terugzetten
    if klokzet and re.fullmatch(r'\d{1,2}\.\d{2} uur', str(it.get('antwoord'))):
        ga = KF._lijst(list(it.get('geldigeAntwoorden') or []) + [it['antwoord']])
        if it.get('geldigeAntwoorden') != ga: it['geldigeAntwoorden'] = ga
    if n: tel['items'] += 1; tel['tijden'] += n
    if (it.get('merge') or {}).get('somtype') != oud_kop: tel['koppen'][oud_kop] = it['merge']['somtype']
def tekst_entry(st):
    if DIGI.search(st.get('somtype') or '') or DIGI.search(st.get('somtypeOrigineel') or ''): return 0
    n = 0
    for k in ('hint1', 'hint2', 'ouderzin', 'algemeneFoutHint'):
        if isinstance(st.get(k), str): st[k], c = KF.tekst(st[k]); n += c
    for f in st.get('foutHints') or []:
        for k in ('tekst', 'tekstSterker'):
            if isinstance(f.get(k), str): f[k], c = KF.tekst(f[k]); n += c
    return n
def md(p, koppen):
    s = open(p, encoding='utf-8').read(); delen = re.split(r'(?m)^(?=## Somtype \d+: )', s); n = 0; uit = []
    for d in delen:
        m = re.match(r'## Somtype (\d+): (.*)\n', d)
        if not m: uit.append(d); continue
        kop = m.group(2).strip()
        if DIGI.search(kop): uit.append(d); continue
        rest = d[m.end():]; t, c = KF.tekst(rest); n += c
        uit.append(f'## Somtype {m.group(1)}: {koppen.get(kop, kop)}\n' + t)
    open(p, 'w', encoding='utf-8').write(''.join(uit)); return n
def groep(g):
    B = f'{R13}/g{g}'; tel = {'vlag': 0, 'items': 0, 'tijden': 0, 'koppen': {}}
    perdoel = {}
    for p in sorted(glob.glob(f'{B}/data/per_doel/*.json')):
        d = json.load(open(p))
        for it in d['items']: omzet(it, tel)
        json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1); perdoel.update({it['id']: it for it in d['items']})
    t2 = {'vlag': 0, 'items': 0, 'tijden': 0, 'koppen': {}}
    for naam in ('gemapt.json',):
        p = f'{B}/data/{naam}'; d = json.load(open(p))
        for i, it in enumerate(d['items']):
            if it['id'] in perdoel: d['items'][i] = copy.deepcopy(perdoel[it['id']])      # zelfde item als in per_doel (die is na apply_hints)
            else: omzet(it, t2)
        json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
    nb = 0
    for p in sorted(glob.glob(f'{B}/hints/batch*.json')):
        d = json.load(open(p)); nb += sum(tekst_entry(st) for st in d.get('somtypen', [])); json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    nm = sum(md(p, tel['koppen']) for p in sorted(glob.glob(f'{B}/somtypen/*.md')))
    r = subprocess.run([sys.executable, '-B', f'{B}/scripts/sync_hint_keys.py'], capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    items = list(perdoel.values()); kt = KT.treffers(items)
    rnd = random.Random(13); omgezet = [it for it in items if it.get('geldigeAntwoorden') and any(':' in x for x in it['geldigeAntwoorden']) or it.get('digitaleKlok')]
    steek = rnd.sample(omgezet, min(10, len(omgezet)))
    return {'groep': f'G{g}', 'digitaleKlok': tel['vlag'], 'itemsOmgezet': tel['items'], 'tijdenOmgezet': tel['tijden'], 'koppenGewijzigd': len(tel['koppen']),
            'batchTeksten': nb, 'mdTijden': nm, 'sync': r.stdout.strip().splitlines()[-6:] + r.stderr.strip().splitlines()[-3:], 'KLOKTIJD': len(kt), 'kloktijdVoorbeelden': [x for _, x in kt[:5]],
            'steekproef': [{'id': it['id'], 'digitaleKlok': bool(it.get('digitaleKlok')), 'opgave': it['opgave'][:110], 'antwoord': it['antwoord'], 'geldigeAntwoorden': it.get('geldigeAntwoorden')} for it in steek],
            'koppen': tel['koppen']}
if __name__ == '__main__':
    R = [groep(int(g)) for g in sys.argv[1:]]
    json.dump(R, open(f'{R13}/klok_rapport.json', 'w'), ensure_ascii=False, indent=1)
    for r in R: print(r['groep'], {k: v for k, v in r.items() if k not in ('steekproef', 'koppen', 'kloktijdVoorbeelden')})
