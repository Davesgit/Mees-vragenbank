#!/usr/bin/env python3
"""Hook Z-#1090 ronde 2 (Didactiek 15 okt 16:40 + Oef-#1045/#1046; VOORWAARDELIJK, niet geplaatst; na Z-#1090 op na-ronde-z1090):
een uitleg over lenen («Dan gaat er nog een tiental af») of onthouden («De eenheden zijn samen tien of meer», «De tientallen komen samen op tien
of meer») alleen bij items waar dat echt gebeurt. Per fout-hint met zo'n uitleg (tekst of tekstSterker) en de bijbehorende regel
('fout = antwoord + 10' lenen; '− 10' onthouden naar de tientallen; '− 100' naar de honderdtallen):
- elk item klopt → niets;
- gemengd → splitsen zoals G6-GET-E04 (motor #399/#392): eerst soort '<soort> (geleend|onthouden)' met regel + '(geleend bij de tientallen)' /
  '(onthouden naar de tientallen|honderdtallen)' en de oude tekst; daarna de gewone soort met de tekst zonder die uitleg, en waar nodig
  «Haal de tientallen nog eens af.» / «Tel de tientallen (honderdtallen) nog eens bij elkaar.» (waar je moet kijken, geen bedrag);
- geen enkel item klopt → alleen de tekst zonder de uitleg.
Een vorm die het niet kent → MELD, niets. Idempotent (na het splitsen staat de uitleg alleen nog in de '(geleend|onthouden)'-soort met suffix)."""
import json, os, sys, glob, re, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g5pad import *; from lenen_lib import *
B = sys.argv[1]; G = g5(B); I = items(G); LOG, MELD, SCOPE = [], [], []
KIJK = re.compile(r'tiental|tientallen|eenheden|honderdtal|honderdtallen|getallen', re.I)
def norm(r): return r.replace('-', '−').strip()
for P in sorted(glob.glob(os.path.join(G, 'hints', 'batch*.json'))):
    t = open(P, encoding='utf-8').read(); D = json.loads(t); n0 = len(LOG)
    for s in D['somtypen']:
        its = I.get((s['doel'], s['nrOrigineel']), []); uit = []
        for f in s['foutHints']:
            soort_n = next(((n, rx, fn, rg, suf, ext, kijk) for n, rx, fn, rg, suf, ext, kijk in SOORTEN
                            if any(rx.search(f.get(v) or '') for v in ('tekst', 'tekstSterker'))), None)
            if not soort_n or not s['doel'].startswith('G5-GET'): uit.append(f); continue
            n, rx, fn, rg, suf, ext, kijk = soort_n
            if norm(f['regel']).endswith(suf): uit.append(f); continue          # al gesplitst
            xs = [x for x in its if any(k['soort'] == f['soort'] for k in x['foutHints'])]
            waar = [fn(x) for x in xs]
            if xs and all(w is True for w in waar): uit.append(f); continue      # klopt bij elk item (ook bij een andere regel, bv. #32 Claudes sleutel)
            if norm(f['regel']) != rg:
                MELD.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']!r}: uitleg '{n}' bij regel {f['regel']!r}: niet gezet"); uit.append(f); continue
            if xs and all(w is True for w in waar): uit.append(f); continue
            g = copy.deepcopy(f); ok = True
            for v in ('tekst', 'tekstSterker'):
                if isinstance(g.get(v), str) and rx.search(g[v]):
                    z = zonder(g[v], n)
                    if z is None: ok = False; break
                    rich = 'veel' if '+' in rg else 'weinig'
                    if v == 'tekst': z = re.sub(r'^Dat is (?:één|een) (?:honderdtal|tiental) te (veel|weinig)\.', r'Dat is te \1.', z)      # r4 (a): geen bedrag in de 'zonder'-tekst
                    if v == 'tekst' and not z.startswith('Dat is'):      # r3: 'Dat is één honderdtal te veel.' blijft staan (bedrag: Z-#1091)
                     z = f'Dat is te {rich}. ' + z
                    if not KIJK.search(re.sub(r'^Dat is [^.]*\.', '', z)): z = (z + ' ' + kijk).strip()
                    g[v] = re.sub(r'\s+', ' ', z).strip()
            if not ok: MELD.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']!r}: uitleg in een onbekende vorm: niet gezet"); uit.append(f); continue
            met = sum(w is True for w in waar)
            if met:
                a = dict(copy.deepcopy(f), soort=f['soort'] + ext, regel=f['regel'] + suf)
                uit += [a, g]
            else: uit.append(g)
            SCOPE.append({'doel': s['doel'], 'nro': s['nrOrigineel'], 'soort': f['soort'], 'uitleg': n, 'met': met, 'zonder': len(xs) - met, 'nieuweTekst': g.get('tekst'), 'nieuwSterker': g.get('tekstSterker')})
            LOG.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']!r} ({n}): {met} met, {len(xs) - met} zonder → {'gesplitst' if met else 'alleen tekst'}: {g.get('tekst')!r}")
        # Oef-#1049 (Didactiek 15 okt): geen cijfer in een leen-/onthoudzin: '10 of meer' → 'tien of meer' (alleen in fout-hints met zo'n zin)
        for f in uit:
            for v in ('tekst', 'tekstSterker'):
                t_ = f.get(v)
                if isinstance(t_, str) and any(rx.search(t_) for _, rx, *_r in SOORTEN) and re.search(r'samen 10{1,2} of meer', t_):
                    f[v] = t_.replace('samen 100 of meer', 'samen honderd of meer').replace('samen 10 of meer', 'samen tien of meer'); LOG.append(f"{s['doel']} #{s['nrOrigineel']} {f['soort']!r} [{v}]: cijfer → woord (Oef-#1049/V-#1130)")
        s['foutHints'] = uit
    if len(LOG) > n0: schrijf(P, t, D)
if SCOPE: json.dump(SCOPE, open(os.path.join(G, 'logs', 'z1090_lenen_scope.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for m in MELD: print('MELD', m)
print(f"{B}: {len(LOG)} wijzigingen (Z-#1090 lenen/onthouden)" + ''.join('\n  ' + l for l in LOG))
