#!/usr/bin/env python3
"""Check V-#1150 v2 (r24: V-#1152 + V-#1153, les 462). Nieuwe versie van check_v1150.py (r23, ongewijzigd). [MUT=..] [SNAP=1] python3 check_v1150_v2.py <basis>
(na sync_hint_keys + apply_hints). Altijd FAIL N (totaal); exit 1 bij FAIL. Bereik: ALLE sleutels (foutHints) van de items van de 8 maatvraag-somtypen.
- laag 1: guard_v1150_v2 (het criterium; uitzondering 'het getal uit de som' (sleutel) = vaste entrytekst);
- laag 2 per item, voor ELKE sleutel in het bereik (ook de uitzondering): uitlegSterker bevat het FEIT met de juiste factor en de METHODE in de richting
  van de opgave (groot → klein: 'keer N' + 'zet er z nullen achter'; klein → groot: 'door N' + 'haal er z nullen af'); laag2 = terugval hint2 of tekstSterker;
- afgeleide velden: foutHintsTekst bevat «<fout> → <uitleg>» (per_doel én gemapt.json); foutRegels[].tekst van de soort = de entrytekst;
- entries: elke entry met sleutels (SLEUTELS, 31 combinaties doel/nr/soort) voldoet aan hetzelfde criterium; somtypen/*.md toont dezelfde tekst;
- elke combinatie in SLEUTELS heeft nog sleutels bij de items (geen soort stil weg); SNAP van laag 1 en laag 2 per sleutel (naast het criterium)."""
import glob, json, os, re, sys, math, collections
D_ = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [D_, os.path.join(D_, '..', 'z1090', 'r4')]
from g5pad import g5, items; import guard_v1150_v2 as GV
B = sys.argv[1]; MUT = os.environ.get('MUT', ''); F = []; G = g5(B); I = items(G)
MAAT = {'kilometer': ('l', 1000000, 'km'), 'meter': ('l', 1000, 'm'), 'centimeter': ('l', 10, 'cm'), 'millimeter': ('l', 1, 'mm'), 'liter': ('v', 1000, 'L'), 'milliliter': ('v', 1, 'ml'), 'kilogram': ('m', 1000, 'kg'), 'gram': ('m', 1, 'g')}
SLEUTELS = {('G5-MEET-E01', 1, 'het getal uit de som'), ('G5-MEET-E01', 1, 'nul te veel'), ('G5-MEET-E01', 1, 'nul vergeten'), ('G5-MEET-E01', 1, 'te weinig'), ('G5-MEET-E01', 2, 'het getal uit de som'), ('G5-MEET-E01', 2, 'het getal uit de som (sleutel)'), ('G5-MEET-E01', 2, 'nul te veel'), ('G5-MEET-E01', 2, 'nul vergeten'), ('G5-MEET-E01', 2, 'te veel'), ('G5-MEET-E01', 3, 'het getal uit de som'), ('G5-MEET-E01', 3, 'nul te veel'), ('G5-MEET-E01', 3, 'nul vergeten'), ('G5-MEET-E01', 3, 'te weinig'), ('G5-MEET-E01', 4, 'het getal uit de som'), ('G5-MEET-E01', 4, 'nul te veel'), ('G5-MEET-E01', 4, 'nul vergeten'), ('G5-MEET-E01', 4, 'te weinig'), ('G5-MEET-E04', 2, 'het getal uit de som'), ('G5-MEET-E04', 2, 'nul te veel'), ('G5-MEET-E04', 2, 'nul vergeten'), ('G5-MEET-E04', 2, 'te weinig'), ('G5-MEET-E04', 4, 'het getal uit de som'), ('G5-MEET-E04', 4, 'nul te veel'), ('G5-MEET-E04', 4, 'nul vergeten'), ('G5-MEET-E05', 1, 'het getal uit de som'), ('G5-MEET-E05', 1, 'nul te veel'), ('G5-MEET-E05', 1, 'nul vergeten'), ('G5-MEET-E05', 1, 'te weinig'), ('G5-MEET-E05', 3, 'het getal uit de som'), ('G5-MEET-E05', 3, 'nul te veel'), ('G5-MEET-E05', 3, 'nul vergeten')}
TAL = {10: 'tien', 100: 'honderd', 1000: 'duizend'}; NUL = {1: 'één', 2: 'twee', 3: 'drie'}
if MUT.startswith('M_g_'): GV.mutant(I, 'M_' + MUT[4:])      # de guard-mutanten, via de check
ENT_ = {(s['doel'], s['nrOrigineel']): s for p in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))) for s in json.load(open(p, encoding='utf-8'))['somtypen'] if s['doel'].startswith('G5-')}
def h_(doel, nr, soort): return next((x, h) for x in sorted(I[(doel, nr)], key=lambda x: x['nr']) for h in x['foutHints'] if h['soort'] == soort)
if MUT == 'M_l2_feit': x, h = h_('G5-MEET-E01', 3, 'nul te veel'); h['uitlegSterker'] = re.sub(r'^[^.]*\.\s*', '', h['uitlegSterker'])
if MUT == 'M_l2_factor': x, h = h_('G5-MEET-E04', 2, 'nul te veel'); h['uitlegSterker'] = h['uitlegSterker'].replace('is duizend milliliter', 'is honderd milliliter', 1)
if MUT == 'M_l2_methode': x, h = h_('G5-MEET-E01', 2, 'nul vergeten'); h['uitlegSterker'] = h['uitlegSterker'].replace('door honderd', 'keer honderd')
if MUT == 'M_l2_nullen': x, h = h_('G5-MEET-E05', 1, 'nul te veel'); h['uitlegSterker'] = h['uitlegSterker'].replace('drie nullen', 'twee nullen')
if MUT == 'M_tekst': x, h = h_('G5-MEET-E01', 4, 'nul te veel'); x['foutHintsTekst'] = x['foutHintsTekst'].replace('Reken daarmee opnieuw.', 'Eén meter is duizend millimeter.', 1)
if MUT == 'M_regel': x, h = h_('G5-MEET-E05', 3, 'nul te veel'); next(r for r in x['foutRegels'] if r['soort'] == 'nul te veel')['tekst'] += ' Zet er drie nullen achter.'
if MUT == 'M_l2_nulverg': x, h = h_('G5-MEET-E01', 1, 'nul vergeten'); h['uitlegSterker'] = re.sub(r'^[^.]*\.\s*', '', h['uitlegSterker'])
if MUT == 'M_l2_teweinig': x, h = h_('G5-MEET-E05', 1, 'te weinig'); h['uitlegSterker'] = h['uitlegSterker'].replace('keer duizend', 'door duizend')
if MUT == 'M_l2_uitz': x, h = h_('G5-MEET-E01', 3, 'het getal uit de som'); h['uitlegSterker'] = h['uitlegSterker'].replace('drie nullen', 'twee nullen')
if MUT == 'M_nulverg_entry': next(f for f in ENT_[('G5-MEET-E04', 2)]['foutHints'] if f['soort'] == 'nul vergeten')['tekst'] = 'Dat is te weinig: er mist een nul. Eén liter is duizend milliliter: zet er drie nullen achter.'
if MUT == 'M_weg': I[('G5-MEET-E04', 4)] = [dict(x, foutHints=[h for h in x['foutHints'] if h['soort'] != 'nul te veel']) for x in I[('G5-MEET-E04', 4)]]
n, FG = GV.guard(I); F += FG
ENT = ENT_
if MUT == 'M_entry': next(f for f in ENT[('G5-MEET-E01', 1)]['foutHints'] if f['soort'] == 'nul te veel')['tekst'] = 'Dat is te groot. Hoeveel centimeter gaan er in één meter? Eén meter is honderd centimeter: zet er twee nullen achter.'
ETEKST = {}
for (d, nr, so) in sorted(SLEUTELS):
    s = ENT.get((d, nr)); f = next((f for f in (s or {}).get('foutHints', []) if f['soort'] == so), None)
    if not f: F.append(f"entry {d} #{nr} {so!r} ontbreekt"); continue
    ETEKST[(d, nr, so)] = f['tekst']; nep = {'doelId': d, 'merge': {'somtypeNrOrigineel': nr}, 'hint': s.get('hint1'), 'antwoord': None}
    r = GV.beoordeel(nep, {'soort': so, 'uitleg': f['tekst'], 'fout': None})
    if r: F.append(f"entry {d} #{nr} {so!r}: {'; '.join(r)} — «{f['tekst'][:90]}»")
md = {p: open(p, encoding='utf-8').read() for p in glob.glob(os.path.join(G, 'somtypen', 'G5-MEET-E0*.md'))}
for (d, nr, so), t in sorted(ETEKST.items()):
    if not any(f"`{so}` (" in m and f") → {t}  [" in m for m in md.values()): F.append(f"md {d} #{nr} {so!r}: de entrytekst staat niet in somtypen/{d}.md")
GM = {x['id']: x for x in json.load(open(os.path.join(G, 'data', 'gemapt.json'), encoding='utf-8'))['items'] if x['merge'].get('doel', '').startswith('G5-MEET-E0')}
cnt = collections.Counter(); snap = {}
for k in sorted(I, key=str):
    for x in sorted(I[k], key=lambda x: x['nr']):
        for h in x.get('foutHints') or []:
            if not GV.in_bereik(x, h): continue
            pl = f"{x['doelId']} #{k[1]} {x['nr']} {h['soort']!r} {h.get('fout')!r}"; cnt[(x['doelId'], k[1], h['soort'])] += 1
            snap[pl] = [h.get('uitleg'), h.get('uitlegSterker')]; sh = h.get('uitlegSterker') or ''
            m = re.match(r'^Hoeveel (\w+) gaan er in één (\w+)\?$', x.get('hint') or ''); toks = re.findall(r'\b(km|cm|mm|ml|kg|m|L|g)\b', x['opgave'])
            if h.get('laag2') not in ('terugval hint2 (somtype)', 'tekstSterker'): F.append(f"laag2 {pl}: laag2 = {h.get('laag2')!r}")
            if not m or m.group(1) not in MAAT or m.group(2) not in MAAT or len(toks) < 2: F.append(f"laag2 {pl}: hint 1 / opgave niet te lezen ({x.get('hint')!r}, {x['opgave']!r})"); continue
            kl, gr = m.groups(); N = MAAT[gr][1] // MAAT[kl][1]; tal = TAL.get(N)
            if not tal: F.append(f"laag2 {pl}: factor {N}?"); continue
            z = round(math.log10(N))
            if not re.search(rf'(?:Eén {gr} \({MAAT[gr][2]}\) is {tal} {kl} \({MAAT[kl][2]}\)|{tal.capitalize()} {kl} \({MAAT[kl][2]}\) is één {gr} \({MAAT[gr][2]}\))\.', sh): F.append(f"laag2 feit {pl}: geen «Eén {gr} ({MAAT[gr][2]}) is {tal} {kl} ({MAAT[kl][2]}).»: {sh[:80]}")
            meth = (rf'keer {tal}\b', rf'zet er {NUL[z]} nullen achter') if toks[0] == MAAT[gr][2] else (rf'door {tal}\b', rf'haal er {NUL[z]} nullen af')
            if not all(re.search(p, sh) for p in meth): F.append(f"laag2 methode {pl}: verwacht {' + '.join(meth)} ({toks[0]} → {toks[1]}): {sh[:80]}")
            seg = f"{h.get('fout')} → {h.get('uitleg')}"
            if seg not in (x.get('foutHintsTekst') or ''): F.append(f"foutHintsTekst {pl}: «{seg[:60]}» ontbreekt (per_doel)")
            g = GM.get(x['id'])
            if not g or seg not in (g.get('foutHintsTekst') or ''): F.append(f"foutHintsTekst {pl}: «{seg[:60]}» ontbreekt (gemapt.json)")
        for r in x.get('foutRegels') or []:
            e = ETEKST.get((x['doelId'], k[1], r['soort']))
            if e is not None and r.get('tekst') != e: F.append(f"foutRegels {x['doelId']} #{k[1]} {x['nr']} {r['soort']!r}: tekst ≠ entrytekst: {str(r.get('tekst'))[:70]}")
for b in sorted(SLEUTELS):
    if not cnt[b]: F.append(f"bereik {b[0]} #{b[1]} {b[2]!r}: geen enkele foutHint bij de items (stil weg?)")
SNAPF = os.path.join(D_, 'snap_v1150_v2.json')
if MUT == 'M_snap': k_ = sorted(snap)[0]; snap[k_] = [snap[k_][0], (snap[k_][1] or '') + ' Kijk goed.']
if os.environ.get('SNAP') == '1': json.dump(snap, open(SNAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
elif os.path.exists(SNAPF):
    o = json.load(open(SNAPF, encoding='utf-8')); F += [f"SNAP V-#1150 v2 {k}" for k in sorted(set(o) | set(snap)) if o.get(k) != snap.get(k)]
else: F.append('SNAP V-#1150 v2 ontbreekt')
print(f"INFO V-#1150 v2: {n} foutHints in bereik, {len(ETEKST)} entries ({len(SLEUTELS)} combinaties doel/nr/soort, uitzondering {sum(v for b, v in cnt.items() if b[2].startswith('het getal uit de som'))}); SNAP {len(snap)}")
for f in F[:30]: print('FAIL', f)
if len(F) > 30: print(f"… {len(F) - 30} FAIL-regels niet getoond")
print(f"check V-#1150 v2: FAIL {len(F)} (totaal)" + (f' (MUT={MUT})' if MUT else ''))
sys.exit(1 if F else 0)
