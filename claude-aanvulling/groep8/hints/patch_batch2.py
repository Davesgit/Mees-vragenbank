#!/usr/bin/env python3
"""Patcht hints/batch2.json IN PLACE (G8 batch 2: GET-E02 #12–#36), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch2.json. Na een sync of rebuild nooit make_batch2.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch2.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt 15:3x, Didactiek review-batch2 «taal: fix», build 15:27:54; data V-#781/V-#782 in build 15:35:14) ----------
# nummers hieronder: nrOrigineel (somtype-nr in de review = nrO + 7)
import json as _json, os as _os
R1B = 'ronde 1b (Didactiek review-batch2)'
E2 = 'G8-GET-E02'
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch2.json'), encoding='utf-8'))
_S = {s_['nrOrigineel']: s_ for s_ in _B['somtypen'] if s_['doel'] == E2}
_fhs = {k_: [dict(f_) for f_ in v_['foutHints']] for k_, v_ in _S.items()}
_fhs0 = _json.dumps(_fhs, sort_keys=True)
def _zet(nro, soort_, **upd):
    n_ = 0
    for f_ in _fhs[nro]:
        if f_['soort'] == soort_: f_.update(upd); n_ += 1
    return n_

# V-#780 (les 144/260): H2 beschreef de aanpak = het goede antwoord. Nieuwe H2 laat rekenen en elke optie narekenen.
# De oude H2 blijft laag 2 (tekstSterker) van de fout-hints: die is daar al gelijk aan de oude H2, dus alleen hint2 (en bij #16/#21 hint1) verandert.
H2_780 = {
    5: "Tel van de temperatuur van 's ochtends door tot die van 's middags: hoeveel graden is dat? Reken dan elke aanpak uit. Welke geeft precies dat getal?",
    7: 'Bedenk een voorbeeld: vier doelpunten en twee missers. Reken de score uit. Reken daarna elke aanpak uit met hetzelfde voorbeeld. Welke geeft dezelfde score?',
    9: 'Probeer elke aanpak met de tijden uit de vraag. Kun je elke stap uitvoeren zonder onder de nul te komen? En kom je uit op een reistijd die kan?',
    10: 'Reken de vierkante meters zelf uit: lengte keer breedte. Komt Fleur daarop uit? Kijk dan welke uitleg past bij wat zij wel uitrekende.',
    11: 'Denk aan rijen tegels. Hoeveel tegels passen er in één rij, en hoeveel rijen zijn er? Reken uit hoeveel tegels dat samen zijn. Welke aanpak geeft dat aantal?',
    12: 'Hoeveel meter hek is het echt? Tel alle zijden rondom bij elkaar op. Komt Joep daarop uit? Kijk dan welke uitleg past bij wat hij wel uitrekende.',
    14: 'Reken allebei uit: hoeveel euro gaat er af, en wat kost de jas daarna? Welk van die twee bedragen rekende Milou uit?',
    16: 'Reken het uit: hoeveel rijst is er voor één persoon, en hoeveel dan voor alle mensen waarvoor je kookt? Reken ook elke aanpak uit. Welke geeft hetzelfde?',
    18: 'Reken elke manier uit met de getallen van Eva. Bij welke manier zie je echt of haar antwoord goed is? Een goede controle laat ook een fout zien.',
    19: 'Een goede controle rekent anders dan de som zelf, en geeft een getal dat je kunt vergelijken. Reken elke manier uit met de getallen van Fenna. Welke manier doet dat?',
    20: 'Neem een paar getallen uit de tafel van dat getal, en een paar die er niet in zitten. Probeer elke manier uit. Welke manier klopt bij al die getallen?',
    21: 'Neem een paar even en een paar oneven getallen, ook grote. Probeer elke manier uit. Welke manier klopt bij al die getallen?',
    23: 'Bedenk een week waarin het niet elke dag even druk is. Telt elke manier elke dag mee, met het eigen aantal van die dag?',
    24: 'Bedenk een prijs, bijvoorbeeld honderd euro. Reken uit wat je met de korting nog betaalt. Reken elke manier uit met die prijs. Welke geeft hetzelfde?',
    25: 'Reken het uit: hoeveel leerlingen is één procent, en hoeveel is dan het procent uit de vraag? Reken ook elke manier uit. Welke geeft hetzelfde aantal leerlingen?',
    26: 'Eén kilogram is duizend gram. Reken elke stap na: klopt het omrekenen, en staan daarna allebei de getallen in dezelfde maat?',
    27: 'Elk uur fiets je even ver. Reken elke aanpak uit en doe de uitkomst keer het aantal uren. Bij welke aanpak kom je weer op alle kilometers uit?',
    28: 'Reken het uit: hoeveel koekjes krijgt ieder, en hoeveel blijven er over? Reken dan elke aanpak uit. Welke aanpak geeft allebei?',
    29: 'Vul in gedachten de dozen een voor een. Hoeveel worden er helemaal vol? Reken dan elke aanpak uit. Welke geeft hetzelfde aantal?',
}
H1_780 = {9: 'Een uur heeft zestig minuten, geen honderd. Let daarop bij elke aanpak.',
          14: 'Bij korting horen twee bedragen: wat eraf gaat, en wat je daarna nog betaalt.'}
for nro_, t_ in H2_780.items():
    # de oude H2 moet al laag 2 zijn van elke fout-hint (anders verdwijnt de aanpak-uitleg); bij een tweede run is hint2 al nieuw
    if _S[nro_]['hint2'] != t_: assert all(f_.get('tekstSterker') == _S[nro_]['hint2'] for f_ in _fhs[nro_]), ('L2 ≠ oude H2', nro_)
    PATCH.append((E2, nro_, 'hint2', t_, R1B + ', V-#780: H2 verklapte de aanpak (les 144/260); oude H2 blijft laag 2'))
for nro_, t_ in H1_780.items(): PATCH.append((E2, nro_, 'hint1', t_, R1B + ', V-#780: H1 verklapte/stuurde naar de aanpak'))

# V-#783 (les 261): #16 'minuten afgetrokken' werkt wel (lenen / min-minuten), alleen niet handig
_zet(9, 'minuten afgetrokken', tekst='De minuten bij aankomst zijn minder dan bij vertrek. Dan kom je onder de nul, en moet je een uur omwisselen voor zestig minuten. Dat kan, maar het is niet handig. Spring liever eerst naar het volgende hele uur.')

# V-#782 (les 195/264): #32 nieuwe afleider van Overzicht (build 15:35:14) 'Deel 100 door 40 en doe dat keer 15' (= 37,5; route: delen andersom).
# De oude regel ('Deel 15 door 100 en doe dat keer 40 procent') pakt niets meer (regels_onleesbaar): weg. L1 = Didactiek-voorstel (a) bij deze vervanger;
# L2 = de oude H2 (waar voor deze optie). H1 («van elke honderd») laat nu twee opties over (beide met 100): niet beslissend (les 264).
_fhs[25] = [f_ for f_ in _fhs[25] if f_['regel'] != 'Deel 15 door 100 en doe dat keer 40 procent']
L2_25 = _S[25]['foutHints'][-1]['tekstSterker']
if not any(f_['soort'] == 'honderd door het aantal gedeeld' for f_ in _fhs[25]):
    _fhs[25].insert(0, dict(N('honderd door het aantal gedeeld', 'Deel 100 door 40 en doe dat keer 15',
        'Dan deel je honderd door het aantal leerlingen. Hoeveel leerlingen is één procent: welk getal deel je door honderd?'), tekstSterker=L2_25))

# Z-#783: #13 'tien keer te groot': waarmee vergeleken
_zet(6, 'tien keer te groot', tekst="Dat is nog veel meer dan het antwoord van Bas. Rond de prijs af op hele euro's en doe dat keer het aantal: hoeveel euro is dat ongeveer?")

# Z-#784 (les 147/193): #27/#28 in de fout-hints het woord van de opties: 'het laatste cijfer' / 'het eerste cijfer'
def _cijf(t_):
    if not t_: return t_
    t_ = t_.replace('het cijfer helemaal rechts, bij de eenheden', 'het laatste cijfer, bij de eenheden')
    t_ = t_.replace('het cijfer helemaal rechts', 'het laatste cijfer, bij de eenheden')
    return t_.replace('Het cijfer helemaal links', 'Het eerste cijfer').replace('het cijfer helemaal links', 'het eerste cijfer')
for nro_ in (20, 21):
    for f_ in _fhs[nro_]: f_['tekst'] = _cijf(f_['tekst']); f_['tekstSterker'] = _cijf(f_.get('tekstSterker'))

for nro_ in sorted(_fhs):
    if _json.dumps(_fhs[nro_], sort_keys=True) != _json.dumps(_S[nro_]['foutHints'], sort_keys=True):
        PATCH.append((E2, nro_, 'foutHints', _fhs[nro_], R1B + ': V-#782/V-#783/Z-#783/Z-#784'))

# koppen nagekeken (build 15:35:14): #16 '# uur' (V-#781), #20/#21/#26/#32 zonder '[ding]' (Oef-#478), #27 'deelbaar door 5' (Z-#780), #29 'staafgrafiek' (Oef-#480)
for nro_ in (9, 13, 14, 19, 20, 22, 25):
    if _S[nro_].get('kopGewijzigd') or _S[nro_].get('kopNagekeken'): PATCH.append((E2, nro_, 'kopNagekeken', None, R1B + ': kop nagekeken (build 15:35:14), teksten passen'))

if __name__ == '__main__':
    patch_lib.run(2, PATCH)
