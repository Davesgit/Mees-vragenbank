#!/usr/bin/env python3
"""Patcht hints/batch4.json IN PLACE (G8 batch 4: GET-E05 #1–#16 + GET-M01 #1–#5 + MEET-E01 #1–#2), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch4.json. Na een sync of rebuild nooit make_batch4.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch4.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~16:35): Oef-#490 — de motorregels van Overzicht in plaats van de labelregels ----------
# Per route de rekenregel uit scripts/fout_regels.py (Oef-#490, ná de zekere regels, geen ±1, dus #390 blijft heel). De labelregel blijft alleen
# als vangnet voor Claude-sleutels die de rekenregel niet pakt, en staat erna (les 270). Teksten: zelfde inhoud als de labeltekst, nu per route.
R1B = 'Ronde 1b (Oefeningen 8 okt; Oef-#490 motorregels, build 16:25:38)'
E5, M1, ME1 = 'G8-GET-E05', 'G8-GET-M01', 'G8-MEET-E01'
import json as _json, os as _os
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch4.json'), encoding='utf-8'))
_S = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _B['somtypen']}
def _r(k_, soort, regel, tekst):
    f_ = N(soort, regel, tekst); f_['tekstSterker'] = _S[k_]['hint2']; return f_
def _lijst(k_, volgorde, nieuw):
    """nieuwe lijst: bestaande entries op regel (stabiel bij een tweede run), nieuwe rekenregels ertussen; volgorde = regels of nieuwe entries"""
    oud = {f_['regel']: f_ for f_ in _S[k_]['foutHints']}; nw = {f_['regel']: f_ for f_ in nieuw}
    return [nw[r_] if r_ in nw else oud[r_] for r_ in volgorde]
_fhs = {}
for n_ in (1, 2, 3, 4, 5, 6, 8, 10):      # 'Hoeveel … zijn er nodig?'
    k_ = (E5, n_)
    _fhs[k_] = _lijst(k_, ['fout = een getal uit de vraag', 'fout = antwoord + 1', 'fout = het hele getal van het kommagetal uit de vraag', 'fout = hele getal + rest',
                           'fout = de rest van getal2 : getal1', 'fout = een kommagetal', 'Claudes sleutel: rest-vergeten', 'Claudes sleutel: andere-deel-genomen', 'andere fout'],
        [_r(k_, 'alleen de volle', 'fout = het hele getal van het kommagetal uit de vraag', 'Dat zijn alleen de volle. Daarna blijft er nog wat over, en dat moet ook ergens in. Hoeveel heb je er dan nodig?'),
         _r(k_, 'volle en rest opgeteld', 'fout = hele getal + rest', 'Dat is het aantal volle plus wat er overblijft. Wat overblijft, past samen in nog één. Hoeveel heb je er dan nodig?'),
         _r(k_, 'de rest', 'fout = de rest van getal2 : getal1', 'Dat is wat er overblijft na de volle. De vraag wil weten hoeveel je er nodig hebt, zodat alles erin past.')])
for n_ in (7, 9, 11, 12, 13, 14, 15, 16):  # '… gaan weg. Hoeveel blijven er over?'
    k_ = (E5, n_)
    _fhs[k_] = _lijst(k_, ['fout = een getal uit de vraag', 'fout = getal1 − antwoord', 'fout = het hele getal van het kommagetal uit de vraag', 'fout = de cijfers achter de komma uit de vraag',
                           'fout = een kommagetal', 'Claudes sleutel: andere-deel-genomen', 'Claudes sleutel: kommagetal-als-geheel', 'andere fout'],
        [_r(k_, 'per stuk min wat overblijft', 'fout = getal1 − antwoord', 'Dat is wat er nog bij moet om er nog één vol te maken. De vraag wil weten hoeveel er overblijven.'),
         _r(k_, 'het aantal volle', 'fout = het hele getal van het kommagetal uit de vraag', 'Dat is het aantal volle: dat getal staat voor de komma. De vraag wil weten hoeveel er overblijven als die weg zijn.'),
         _r(k_, 'cijfers achter de komma', 'fout = de cijfers achter de komma uit de vraag', 'Dat getal staat na de komma, maar het is niet wat er overblijft. Wat overblijft, reken je uit: haal de volle van het totaal af.')])
for n_ in (2, 3, 4, 5):                    # 'n miljoen' als getal
    k_ = (M1, n_)
    _fhs[k_] = _lijst(k_, ['fout = een getal uit de vraag', 'fout = antwoord : 10', 'fout = antwoord × 10', 'fout = antwoord : 1000', 'Claudes sleutel: nul-fout-tientallen', 'andere fout'],
        [_r(k_, 'duizend in plaats van miljoen', 'fout = antwoord : 1000', 'Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.')])
for n_ in (1, 2):                          # km → m
    k_ = (ME1, n_)
    _fhs[k_] = _lijst(k_, ['fout = een getal uit de vraag', 'fout = antwoord : 10', 'fout = antwoord : 100', 'Claudes sleutel: kommagetal-als-geheel', 'andere fout'],
        [_r(k_, 'keer tien gedaan', 'fout = antwoord : 100', 'Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.')])

# ---------- Ronde 1c (Oefeningen 8 okt ~16:45): Z-#870 (Didactiek review-batch4, les 318) ----------
# E05 'nodig' en 'over': 'kommagetal' vóór 'getal uit de vraag'. De waarde van de rekenmachine (het enige kommagetal in de vraag) krijgt dan de
# kommagetal-tekst ('een aantal is een heel getal'), niet 'staat al in de vraag'. Geen ±1-regel betrokken (#390 blijft heel); de hele getallen uit
# de vraag houden 'getal uit de vraag'. Werkt op de lijsten van ronde 1b, vóór het wegschrijven (één foutHints-regel per somtype: idempotent).
R1C = 'Ronde 1c (Oefeningen 8 okt; Z-#870 Didactiek review-batch4)'
for k_, l_ in _fhs.items():
    if k_[0] != E5: continue
    rg_ = [f_['regel'] for f_ in l_]; i_v, i_k = rg_.index('fout = een getal uit de vraag'), rg_.index('fout = een kommagetal')
    if i_k > i_v: l_.insert(i_v, l_.pop(i_k))
for k_, l_ in _fhs.items():
    if l_ != _S[k_]['foutHints']:
        PATCH.append((k_[0], k_[1], 'foutHints', l_, R1B + ': rekenregels Oef-#490 vóór de labelregels; labelregel blijft vangnet' + ('; ' + R1C + ': kommagetal vóór getal uit de vraag' if k_[0] == E5 else '')))

if __name__ == '__main__':
    patch_lib.run(4, PATCH)
