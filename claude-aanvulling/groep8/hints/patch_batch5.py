#!/usr/bin/env python3
"""Patcht hints/batch5.json IN PLACE (G8 batch 5: MEET-E03 #1–#9 + MEET-E05 #1–#3 + MEET-E06 #1–#12), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch5.json. Na een sync of rebuild nooit make_batch5.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch5.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~16:55): Oef-#494 (getallen onder nul) en Oef-#495 (afgekapt), build 16:45:31 ----------
# MEET-E05: de nieuwe motorregels met teken (teken vergeten / van nul af geteld / verkeerde richting / antwoord ± 1). Volgorde (les 318): de
# specifiekste ware tekst wint. 'Van nul af geteld' vóór '± 1' (bij een begin van 1 of −1 graad zijn ze gelijk); 'verkeerde richting' vóór
# 'getal uit de vraag' (#3: −4 °C, 8 kouder → 4). #1: 'teken vergeten' in plaats van 'getal uit de vraag' (die gaf alleen het getal zonder min;
# nu ook het omgekeerde teken bij een doel boven nul). #2 houdt 'warmer' (= verkeerde richting) en 'min vergeten' (= teken vergeten).
# MEET-E03 #5: 'een nul te weinig (afgekapt)' in plaats van 'antwoord : 10' (die werkte alleen als het antwoord op 0 eindigt).
# Eén foutHints-regel per somtype; de lijst wordt op regel opgebouwd, dus een tweede run geeft 0.
R1B = 'Ronde 1b (Oefeningen 8 okt; Oef-#494/#495 motorregels, build 16:45:31)'
E3, E5 = 'G8-MEET-E03', 'G8-MEET-E05'
import json as _json, os as _os
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch5.json'), encoding='utf-8'))
_S = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _B['somtypen']}
def _r(k_, soort, regel, tekst):
    f_ = N(soort, regel, tekst); f_['tekstSterker'] = _S[k_]['hint2']; return f_
def _lijst(k_, volgorde, nieuw):
    oud = {f_['regel']: f_ for f_ in _S[k_]['foutHints']}; nw = {f_['regel']: f_ for f_ in nieuw}
    return [nw[r_] if r_ in nw else oud[r_] for r_ in volgorde]
_NUL = 'Dat is alleen het aantal graden kouder, gerekend vanaf nul. Begin bij de temperatuur uit de vraag en ga vanaf daar omlaag.'
_fhs = {}
_fhs[(E5, 1)] = _lijst((E5, 1), ['fout = teken vergeten', 'andere fout'],
    [_r((E5, 1), 'teken vergeten', 'fout = teken vergeten', 'Kijk goed of er een min voor het getal staat. Met een min hoort het links van de nul, zonder min rechts.')])
_fhs[(E5, 2)] = _lijst((E5, 2), ['fout = getal1 + getal2', 'fout = getal1 - getal2 of getal2 - getal1', 'fout = van nul af geteld', 'fout = een getal uit de vraag', 'fout = antwoord ± 1', 'andere fout'],
    [_r((E5, 2), 'van nul af geteld', 'fout = van nul af geteld', _NUL),
     _r((E5, 2), 'één ernaast', 'fout = antwoord ± 1', 'Dat is één graad ernaast. Tel nog eens, graad voor graad: eerst omlaag tot nul, dan verder omlaag.')])
_fhs[(E5, 3)] = _lijst((E5, 3), ['fout = teken vergeten', 'fout = verkeerde richting', 'fout = van nul af geteld', 'fout = een getal uit de vraag', 'fout = antwoord ± 1', 'andere fout'],
    [_r((E5, 3), 'teken vergeten', 'fout = teken vergeten', 'Het was al onder nul en het wordt nog kouder. Dan blijf je onder nul: er hoort een min voor het getal.'),
     _r((E5, 3), 'verkeerde richting', 'fout = verkeerde richting', 'Dat is warmer dan aan het begin. Kouder betekent: nog verder omlaag op de thermometer.'),
     _r((E5, 3), 'van nul af geteld', 'fout = van nul af geteld', _NUL),
     _r((E5, 3), 'één ernaast', 'fout = antwoord ± 1', 'Dat is één graad ernaast. Tel de graden onder nul en de graden die het kouder wordt nog eens bij elkaar op.')])
_fhs[(E3, 5)] = _lijst((E3, 5), ['fout = antwoord × 10', 'fout = een nul te weinig (afgekapt)', 'fout = een getal uit de vraag', 'andere fout'],
    [_r((E3, 5), 'nul te weinig', 'fout = een nul te weinig (afgekapt)', 'Dat is ongeveer tien keer te weinig. Tel de nullen nog eens na: hoeveel MB past er op de kaart?')])
for k_, l_ in _fhs.items():
    if l_ != _S[k_]['foutHints']:
        PATCH.append((k_[0], k_[1], 'foutHints', l_, R1B + (': nul te weinig afgekapt (Oef-#495)' if k_[0] == E3 else ': rekenregels met teken (Oef-#494), specifiekste tekst eerst (les 318)')))

# ---------- Ronde 1c (Oefeningen 8 okt ~17:10): Didactiek review-batch5 (V-#900, V-#903, Z-#900, Z-#903, Z-#904) ----------
# Bouwt op de lijsten van ronde 1b (_fhs) en op de huidige batch5.json; een latere PATCH op hetzelfde veld wint (patch_lib), en de uitkomst
# is gelijk aan de json na de eerste run, dus een tweede run geeft 0.
# V-#900 (les 330): E03 #5 'afgekapt' noemt geen factor meer (007: 16 keer), en 'getal uit de vraag' komt vóór 'afgekapt' (007 '1' = '1 GB').
# V-#903 (les 332): E06 landing (#1/#4/#11): de grens van zestig minuten hoort erbij ('zestig minuten of meer'; 001, 006, 007, 011, 029).
# Z-#904: tijdzone-H2's met minuten (#2, #3, #7, #10, #12) noemen 'Zestig minuten is een uur.'; #12 de kortere tekst van Didactiek.
# Z-#900: E03 #1–#4 H1 legt het verband met 'm³'. Z-#903: 'van nul af geteld' scherper per somtype (E05 #2 boven nul, #3 al onder nul).
# L2 = H2 in deze somtypes (zoals in ronde 1); bij een nieuwe H2 krijgen de L2's die mee.
R1C = 'Ronde 1c (Oefeningen 8 okt; Didactiek review-batch5)'
E6 = 'G8-MEET-E06'
import copy as _copy
def _mk(k_, basis, per_regel=None, sterker=None, volgorde=None):
    l_ = _copy.deepcopy(basis)
    if volgorde: d_ = {f_['regel']: f_ for f_ in l_}; l_ = [d_[r_] for r_ in volgorde]
    for f_ in l_:
        if per_regel and f_['regel'] in per_regel: f_['tekst'] = per_regel[f_['regel']]
        if sterker: f_['tekstSterker'] = sterker
    return l_
_v1c = {}   # (doel, nr) -> (veld, wordt, waarom)
_v1c[(E3, 5, 'foutHints')] = (_mk((E3, 5), _fhs[(E3, 5)], {'fout = een nul te weinig (afgekapt)': 'Dan is er ergens een nul weggevallen. Tel de nullen nog eens na: hoeveel MB past er op de kaart, en hoeveel MB is één filmpje?'},
                               volgorde=['fout = antwoord × 10', 'fout = een getal uit de vraag', 'fout = een nul te weinig (afgekapt)', 'andere fout']),
                              "V-#900: 'afgekapt' zonder factor (les 330); 'getal uit de vraag' eerst (route-guard)")
_v1c[(E5, 2, 'foutHints')] = (_mk((E5, 2), _fhs[(E5, 2)], {'fout = van nul af geteld': 'Dat is alleen het aantal graden kouder, gerekend vanaf nul. Je begint boven nul: tel eerst de graden tot nul, en ga dan verder omlaag.'}),
                              "Z-#903: 'van nul af geteld' voor een begin boven nul")
_v1c[(E5, 3, 'foutHints')] = (_mk((E5, 3), _fhs[(E5, 3)], {'fout = van nul af geteld': 'Dat is alleen het aantal graden kouder, gerekend vanaf nul. Je begint al onder nul: tel de graden onder nul en de graden kouder bij elkaar op.'}),
                              "Z-#903: 'van nul af geteld' voor een begin onder nul")
_H2_LAND = 'Doe eerst de hele uren van de vlucht erbij. Doe daarna de minuten erbij. Zestig minuten is een uur: kom je op zestig minuten of meer, dan schuift de klok een uur door.'
_L1_VROEG = 'Dat is een uur te vroeg. Tel de uren van de vlucht nog eens na, en kijk of de minuten samen een heel uur of meer worden.'
for nr_ in (1, 4, 11):
    _v1c[(E6, nr_, 'hint2')] = (_H2_LAND, 'V-#903: de grens van zestig minuten (les 332)')
    _v1c[(E6, nr_, 'foutHints')] = (_mk((E6, nr_), _S[(E6, nr_)]['foutHints'], {'Claudes sleutel: tijd-als-kommagetal': _L1_VROEG}, sterker=_H2_LAND),
                                    "V-#903: L1 'een uur te vroeg' met 'of meer'; L2 = de nieuwe H2")
_H2_TZ = {2: 'Doe de uren en de minuten van de vlucht bij de vertrektijd: dat is de tijd thuis. Doe het tijdsverschil daar nog bij. Zestig minuten is een uur.',
          10: 'Doe de uren en de minuten van de vlucht bij de vertrektijd: dat is de tijd thuis. Doe het tijdsverschil daar nog bij. Kom je voorbij middernacht? Dan begint de klok weer bij nul. Zestig minuten is een uur.',
          3: 'Doe de uren en de minuten van de vlucht bij de vertrektijd: dat is de tijd thuis. Haal het tijdsverschil daar nog vanaf. Zestig minuten is een uur.',
          7: 'Doe de uren en de minuten van de vlucht bij de vertrektijd: dat is de tijd thuis. Haal het tijdsverschil daar nog vanaf. Zestig minuten is een uur.',
          12: 'Doe de vlucht bij de vertrektijd: dat is de tijd thuis. Haal het tijdsverschil eraf. Kom je na middernacht uit, dan begint de klok weer bij nul. Ga je terug voorbij middernacht, dan is het nog de avond ervoor. Zestig minuten is een uur.'}
for nr_, h2_ in _H2_TZ.items():
    _v1c[(E6, nr_, 'hint2')] = (h2_, "Z-#904: 'Zestig minuten is een uur.'" + (' (kortere H2 van Didactiek)' if nr_ == 12 else ''))
    _v1c[(E6, nr_, 'foutHints')] = (_mk((E6, nr_), _S[(E6, nr_)]['foutHints'], sterker=h2_), 'Z-#904: L2 = de nieuwe H2')
for nr_ in (1, 2, 3, 4):
    _v1c[(E3, nr_, 'hint1')] = ('Een kubieke meter (m³) is een kubus van een meter lang, een meter breed en een meter hoog. Daar past duizend liter in.', "Z-#900: H1 koppelt 'kubieke meter' aan 'm³'")
for (d_, n_, veld_), (w_, why_) in _v1c.items():
    if veld_ == 'foutHints' and (d_, n_) in _fhs: PATCH.append((d_, n_, veld_, w_, f'{R1C}: {why_}'))     # na de 1b-regel van dit somtype: deze wint
    elif _S[(d_, n_)].get(veld_) != w_: PATCH.append((d_, n_, veld_, w_, f'{R1C}: {why_}'))

# ---------- Ronde 1d (Oefeningen 8 okt ~17:20): Z-#930 (Didactiek recheck-batch5) ----------
# E06 #1/#4/#11 (landing): de H2 zegt ook wat er met de rest van de minuten gebeurt (002: 19.30 + 45 → 20.15, niet 20.75). Bij precies zestig
# blijft er 0 over (.00), dus waar voor elk item. L2 = H2 (zoals in ronde 1c). Komt na ronde 1c op hetzelfde veld, dus deze wint; tweede run 0.
R1D = 'Ronde 1d (Oefeningen 8 okt; Didactiek recheck-batch5)'
_H2_LAND_D = _H2_LAND + ' Wat boven de zestig overblijft, zijn de minuten.'
for nr_ in (1, 4, 11):
    PATCH.append((E6, nr_, 'hint2', _H2_LAND_D, f'{R1D}: Z-#930, de rest boven de zestig zijn de minuten'))
    PATCH.append((E6, nr_, 'foutHints', _mk((E6, nr_), _S[(E6, nr_)]['foutHints'], {'Claudes sleutel: tijd-als-kommagetal': _L1_VROEG}, sterker=_H2_LAND_D),
                  f'{R1D}: Z-#930, L2 = de nieuwe H2'))

if __name__ == '__main__':
    patch_lib.run(5, PATCH)
