#!/usr/bin/env python3
"""Patcht hints/batch1.json IN PLACE (G8 batch 1: GET-E02 #1–#11, GET-E03 #1–#5, GET-E04 #1–#8), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch1.json. Na een sync of rebuild nooit make_batch1.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch1.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt; review-batch1-didactiek.md, taal: fix; build 15:17:54, breukvorm in build 15:27:54) ----------
R1B = 'Ronde 1b (Oefeningen 8 okt; Didactiek review batch 1)'
E2, E3, E4 = 'G8-GET-E02', 'G8-GET-E03', 'G8-GET-E04'
def _fh(doel, nro, soort_, waarom, **upd): PATCH.append((doel, nro, ('fh', soort_, upd), None, waarom))
def _l2(doel, nro, oud, nieuw, waarom):
    """laag 2's die gelijk zijn aan de oude H2 (of een andere oude tekst) krijgen de nieuwe"""
    PATCH.append((doel, nro, 'foutHints', [dict(f, tekstSterker=nieuw) if f.get('tekstSterker') == oud else f for f in _fhs[(doel, nro)]], waarom))
import json as _json, os as _os
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch1.json'), encoding='utf-8'))
_S = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _B['somtypen']}
_fhs = {k_: [dict(f_) for f_ in v_['foutHints']] for k_, v_ in _S.items()}   # werkkopie: opeenvolgende wijzigingen per somtype in één lijst
def _zet(doel, nro, soort_, **upd):
    for f_ in _fhs[(doel, nro)]:
        if f_['soort'] == soort_: f_.update(upd)
def _weg(doel, nro, soort_): _fhs[(doel, nro)] = [f_ for f_ in _fhs[(doel, nro)] if f_['soort'] != soort_]
def _l2_vervang(doel, nro, oud, nieuw):
    for f_ in _fhs[(doel, nro)]:
        if f_.get('tekstSterker') == oud: f_['tekstSterker'] = nieuw

# V-#760 (besluit 1 okt 17:10, #170): gelijkwaardige breuken zijn goed (breukvorm in de build); regel 'niet vereenvoudigd' weg in E04 #3/#6
H2_E43_OUD = _S[(E4, 3)]['hint2']
H2_E43 = ('Doe teller keer teller en noemer keer noemer (de teller is het getal boven de streep, de noemer het getal onder de streep). '
          'Kan de breuk eenvoudiger? Dat mag, maar het hoeft niet.')
PATCH.append((E4, 3, 'hint2', H2_E43, R1B + ', V-#760: vereenvoudigen mag, hoeft niet'))
PATCH.append((E4, 3, 'ouderzin', 'Je kind rekent een deel van een deel uit (breuk keer breuk).', R1B + ', V-#760'))
for n_ in (3, 6): _weg(E4, n_, 'niet vereenvoudigd')
_l2_vervang(E4, 3, H2_E43_OUD, H2_E43)
# V-#761: 'niet van de hele taart' dekt twee routes (de rest, of de teller vergeten): L1 die op allebei past; L2 = H2
_zet(E4, 3, 'niet van de hele taart', tekst='Dat is nog niet het deel van de hele taart. Neem het deel ván wat er nog is: doe teller keer teller (boven de streep) en noemer keer noemer (onder de streep).')
# V-#762: 'alles opgeteld' dekt t+t/n+n én de goede teller over n·n
_zet(E4, 6, 'alles opgeteld', tekst='Maak eerst de noemers (onder de streep) gelijk. Tel dan alleen de tellers (boven de streep) op: de noemer blijft hetzelfde.')
# V-#763 (les 250/252/253): label-regel 'één te veel (label)' hernoemd naar 'noemer van het kleine stuk', eigen tekst zonder ±1.
#   Plaats: direct NA 'één te veel'. Vóór '±1' gezet (eerste poging, sandbox) pakte het label 'een-ernaast' ook de echte antwoord+1-sleutels
#   van 034/036/038 (3 bij antwoord 2): Claudes label dekt twee routes (les 252). Na '±1' krijgt de label-regel alleen wat #390 weigert:
#   de noemer van het kleine stuk (staat in de vraag) → 031 '4', 032 '2', 037 '2'.
for n_ in (5, 8):
    l_ = _fhs[(E4, n_)]; f_ = next((f for f in l_ if f['soort'] == 'één te veel (label)'), None)
    if f_ is None: continue   # al hernoemd (tweede run)
    f_ = dict(f_, soort='noemer van het kleine stuk',
              tekst='Zoveel kleine stukken passen er in een hele. Je verdeelt geen hele, alleen een deel ervan: hoe vaak past het kleine stuk dáárin?')
    l2_ = [f for f in l_ if f['soort'] != 'één te veel (label)']
    i_ = next(i for i, f in enumerate(l2_) if f['soort'] == 'één te veel')
    _fhs[(E4, n_)] = l2_[:i_ + 1] + [f_] + l2_[i_ + 1:]
# Z-#763: 'één hele', 'Elke hele'
import re as _re
def _hele(t_): return _re.sub(r'\b(één|Elk|elk) heel\b', lambda m_: {'één': 'één hele', 'Elk': 'Elke hele', 'elk': 'elke hele'}[m_.group(1)], t_)
for n_ in (1, 4, 7):
    for k_ in ('hint1', 'hint2', 'ouderzin'): PATCH.append((E4, n_, k_, _hele(_S[(E4, n_)][k_]), R1B + ", Z-#763: 'één hele'"))
    for f_ in _fhs[(E4, n_)]:
        f_['tekst'] = _hele(f_['tekst'])
        if f_.get('tekstSterker'): f_['tekstSterker'] = _hele(f_['tekstSterker'])
    # Z-#770 (les G8-6): 'hele (label)' heeft geen sleutel ('hele overgenomen' pakt dezelfde waarden eerder) en zijn tekst klopt alleen voor die waarde: weg
    _weg(E4, n_, 'hele (label)')

# V-#764 (les 255): lengte (L1 ≤ 45 woorden, H2/L2 ≤ 55): eerst de aankondiging weg, regel in korte deelzinnen
PU = 'Je hebt precies gerekend, maar de vraag wil een schatting. '
RONDEN = {51: ('duizendtallen', 'honderdtallen'), 2: ('duizendtallen', 'honderdtallen'), 56: ('duizendtallen', 'honderdtallen'), 55: ('honderdtallen', 'tientallen')}
for n_, (op_, kijk_) in RONDEN.items():
    _zet(E2, n_, 'precies uitgerekend', tekst=PU + f'Rond allebei de getallen af op {op_}. Is het cijfer van de {kijk_} vijf of meer? Dan naar boven, anders naar beneden.')
    # Z-#760: dubbele aankondiging weg in de ±-L1's (de regel blijft)
    for f_ in _fhs[(E2, n_)]:
        f_['tekst'] = f_['tekst'].replace(' Kijk nog eens hoe je elk getal afrondt.', '')
REGEL_HT = 'Op honderdtallen: kijk naar de tientallen. Op tientallen: kijk naar de eenheden. Vijf of meer? Dan naar boven, anders naar beneden.'
H2_HT = ('Bij het getal dat op honderdtallen moet, kijk je naar de tientallen. Bij het getal dat op tientallen moet, kijk je naar de eenheden. '
         'Vijf of meer? Dan rond je naar boven af, anders naar beneden. Reken de cijfers zonder de nullen keer elkaar en zet alle nullen erachter.')
for n_ in (52, 3):
    oud_ = _S[(E2, n_)]['hint2']
    PATCH.append((E2, n_, 'hint2', H2_HT, R1B + ', V-#764: korter (Didactiek)'))
    _l2_vervang(E2, n_, oud_, H2_HT)
    _zet(E2, n_, 'precies uitgerekend', tekst=PU + 'Rond eerst af zoals de vraag zegt. ' + REGEL_HT)
    _zet(E2, n_, 'andere fout', tekst='Rond eerst af zoals de vraag zegt, en reken dan keer. ' + REGEL_HT)
# E02 #4 (nrO 53): zelfde vorm, op tientallen (onder de maat houden, les 255)
_zet(E2, 53, 'precies uitgerekend', tekst=PU + 'Rond allebei de getallen af op tientallen. Zijn de eenheden vijf of meer? Dan naar boven, anders naar beneden.')
# E02 #11 (nrO 4): V-#764 + Z-#762 (één getal afgerond)
H2_E11_OUD = _S[(E2, 4)]['hint2']
H2_E11 = ("Rond het getal af op honderdtallen: kijk naar de tientallen. Vijf of meer? Dan naar boven, anders naar beneden. "
          "Er staat 'met elk': reken het aantal keer het afgeronde getal. Reken zonder de nullen en zet de nullen van het afgeronde getal erachter.")
PATCH.append((E2, 4, 'hint2', H2_E11, R1B + ', V-#764 en Z-#762: korter, één afgerond getal'))
_l2_vervang(E2, 4, H2_E11_OUD, H2_E11)
_zet(E2, 4, 'precies uitgerekend', tekst=PU + 'Rond het getal af op honderdtallen: kijk naar de tientallen. Vijf of meer? Dan naar boven, anders naar beneden.')
NUL_E11 = 'Tel de nullen van het afgeronde getal. Zoveel nullen komen achter de uitkomst zonder nullen.'
for so_ in ('nul te veel', 'nul te weinig'): _zet(E2, 4, so_, tekstSterker=NUL_E11)
# Z-#761: E02 #7 (nrO 56) naar grootte (in alle items is het eerste getal het grootste; data-guard in g8work/b1/check.py)
def _groot(t_): return t_.replace('Haal daarna het afgeronde getal achter het minteken van het andere afgeronde getal af.', 'Haal daarna het kleinere afgeronde getal van het grotere af.')
PATCH.append((E2, 56, 'hint2', _groot(_S[(E2, 56)]['hint2']), R1B + ', Z-#761: naar grootte'))
for f_ in _fhs[(E2, 56)]:
    if f_.get('tekstSterker'): f_['tekstSterker'] = _groot(f_['tekstSterker'])
# Z-#764: E03 #2 'volgorde' L1 past op beide routes (a gedeeld door de som, en delen overgeslagen)
_zet(E3, 2, 'volgorde', tekst='Delen gaat vóór optellen: reken eerst de deelsom uit, en tel daarna het getal achter het plusteken erbij.')
# koppen E02 #5/#9 (nrO 54/57) gewijzigd in de build ('kan kloppen', zonder [ding]): hints passen erbij
for n_ in (54, 57): PATCH.append((E2, n_, 'kopNagekeken', None, R1B + ': kop nagekeken (build 15:27:54)'))

# ---------- Ronde 1c (Oefeningen 8 okt ~16:00; Didactiek recheck-batch1 «taal: ok», zachte punten Z-#790/Z-#791) ----------
R1C = 'Ronde 1c (Oefeningen 8 okt; recheck-batch1-didactiek)'
# Z-#791 (les 197/272): E04 #5/#8 'noemer van het kleine stuk': eerst zeggen wat het getal ís, dan pas 'zoveel' (tekst van Didactiek, 35 woorden)
for n_ in (5, 8):
    _zet(E4, n_, 'noemer van het kleine stuk', tekst='Dat is de noemer van het kleine stuk (het getal onder de streep): zoveel kleine stukken passen er in een hele. '
         'Je verdeelt geen hele, alleen een deel ervan: hoe vaak past het kleine stuk dáárin?')
# Z-#790 (les 271): E02 #11 (nrO 4): drie L2's waren een kopie van de óúde H2 ('alle nullen van de afgeronde getallen', meervoud) → de nieuwe H2;
# en de optionele L1 van 'andere fout' (Didactiek): enkelvoud, onder de grens
for so_ in ('precies uitgerekend', 'opgeteld', 'andere fout'): _zet(E2, 4, so_, tekstSterker=H2_E11)
_zet(E2, 4, 'andere fout', tekst='Rond eerst af zoals de vraag zegt, en reken dan keer. Rond het getal af op honderdtallen: kijk naar de tientallen. Vijf of meer? Dan naar boven, anders naar beneden.')

for k_, l_ in _fhs.items():
    if l_ != _S[k_]['foutHints']: PATCH.append((k_[0], k_[1], 'foutHints', l_, R1B + ': V-#760–#764, Z-#760–#764, Z-#770; ' + R1C + ': Z-#790/Z-#791'))

if __name__ == '__main__':
    patch_lib.run(1, PATCH)
