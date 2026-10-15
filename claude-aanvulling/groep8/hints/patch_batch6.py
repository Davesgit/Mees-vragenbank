#!/usr/bin/env python3
"""Patcht hints/batch6.json IN PLACE (G8 batch 6: MEET-E07, MEET-V01, VBN-E01, VBN-E03, VBN-E04 #1–#5 en #32–#37), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch6.json. Na een sync of rebuild nooit make_batch6.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch6.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~17:05): Didactiek review-batch6 (V-#890, V-#895, Z-#892, Z-#895) ----------
# Alleen teksten; de regels en hun volgorde blijven. De nieuwe lijst wordt op regel uit de huidige batch6.json opgebouwd (tekst/tekstSterker
# vervangen), dus een tweede run geeft 0. Z-#896 (kijkvraag als H1 bij VBN-E04 #1/#3/#5) wacht op V-#894 (data Overzicht), zie review-batch6.md.
R1B = 'Ronde 1b (Oefeningen 8 okt; Didactiek review-batch6)'
E7, V1, E04 = 'G8-MEET-E07', 'G8-MEET-V01', 'G8-VBN-E04'
import json as _json, os as _os, copy as _copy
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch6.json'), encoding='utf-8'))
_S = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _B['somtypen']}
def _tekst(k_, per_regel=None, sterker=None):
    """kopie van de foutHints van k_ met een nieuwe tekst per regel (per_regel) en/of een nieuwe laag 2 voor alle regels (sterker)"""
    l_ = _copy.deepcopy(_S[k_]['foutHints'])
    for f_ in l_:
        if per_regel and f_['regel'] in per_regel: f_['tekst'] = per_regel[f_['regel']]
        if sterker: f_['tekstSterker'] = sterker
    return l_
_L1_UREN = 'Dan deel je alleen door de hele uren. Het halve uur hoort er ook bij: deel door de hele tijd, met het halve uur erbij.'
_L2_ON = ('Een eerlijk onderzoek vraagt het aan kinderen die lijken op iedereen. Kinderen van een schaakclub kiezen vaak schaken, omdat ze daar '
          "al van houden. Zo'n groep heet eenzijdig.")
_H2_HD = ('In een staaf tel je de kinderen die dat dier hebben. Wat moet er gebeuren om samen meer te tellen dan er kinderen in de klas zitten? '
          'Kies de uitleg die dat kan verklaren zonder dat er iets fout is.')
_fhs = {}
for nr_ in (1, 3):   # V-#890: 'het hele aantal uur' leest als 'de hele uren' (precies de fout)
    _fhs[(E7, nr_)] = (_tekst((E7, nr_), {'Claudes sleutel: deel-vergeten-bij-splitsen': _L1_UREN}), "V-#890: L1 'alleen hele uren'")
_fhs[(V1, 3)] = (_tekst((V1, 3), {'15 bekers': 'Tel de nullen nog eens na, bij het omrekenen én bij het delen. Eén liter is duizend milliliter.'}),
                 "Z-#892: '15 bekers' ook uit 1500 : 100 (les 301)")
_fhs[(E04, 36)] = (_tekst((E04, 36), sterker=_L2_ON), "Z-#895: L2 koppelt aan de optie ('eenzijdig'; na een foute keuze, O1)")
for k_, (l_, w_) in _fhs.items():
    if l_ != _S[k_]['foutHints']: PATCH.append((k_[0], k_[1], 'foutHints', l_, f'{R1B}: {w_}'))
if _S[(E04, 35)]['hint2'] != _H2_HD:   # V-#895: de oude H2 'Kan iemand bij twee staven meetellen?' was het antwoord als vraag (les 260/300)
    PATCH.append((E04, 35, 'hint2', _H2_HD, f'{R1B}: V-#895, H2 verklapte het antwoord'))

# ---------- Ronde 1c (Oefeningen 8 okt ~17:10): Z-#896, kijkvraag als H1 bij VBN-E04 #1/#3/#5 (na V-#894 in build 17:03:20) ----------
_H1_KIJK = 'Wat toont het diagram: aantallen of percentages? En wat noemt de zin eronder?'
for nr_ in (1, 3, 5):
    if _S[(E04, nr_)]['hint1'] != _H1_KIJK: PATCH.append((E04, nr_, 'hint1', _H1_KIJK, 'Ronde 1c (Oefeningen 8 okt; Didactiek review-batch6): Z-#896, H1 als kijkvraag'))

# ---------- Ronde 1d (Oefeningen 8 okt ~17:20): Z-#920 (Didactiek recheck-batch6), H2 #35 zonder de Z-#824-uitzondering ----------
# De tekst van Didactiek deelt met het antwoord alleen 'kinderen' (staat in de vraag, les 147 TOEGESTAAN); 'hebben' en 'meer' zijn weg, dus de
# uitzondering Z824_OK in b6/check vervalt (les 340). Komt na ronde 1b op hetzelfde veld, dus deze wint; tweede run 0.
_H2_HD_D = ('Elke staaf telt de kinderen met dat dier. Wat moet er gebeuren om samen boven het aantal in de klas uit te komen? '
            'Kies de uitleg die dat kan verklaren zonder dat er iets fout is.')
PATCH.append((E04, 35, 'hint2', _H2_HD_D, "Ronde 1d (Oefeningen 8 okt; Didactiek recheck-batch6): Z-#920, H2 zonder 'hebben'/'meer' (les 340)"))

# ---------- Ronde 1e (Oefeningen 8 okt ~20:10): V-#1061 (Didactiek, verplicht), MEET-V01 #1 (nrO 2) 'drie kanten' ----------
# De oude tekst eindigde op 'dus er zitten ook blokjes binnenin': dat zegt 'te weinig geteld'. Bij 9 van de 33 sleutels ligt de waarde van drie
# kanten BOVEN het antwoord (009, 018, 026, 027, 035, 050, 080, 092, 093): randblokjes tel je dubbel. De nieuwe tekst (Didactiek) noemt geen
# richting en is waar voor alle 33 (lessen_g8: geen richting tenzij die voor elk item klopt). Alleen dat ene deel van de '/'-tekst; tweede run 0.
_DK_OUD = 'Dat zijn de blokjes van drie kanten samen: voorkant, zijkant en bovenkant. Het bouwwerk is vol, dus er zitten ook blokjes binnenin.'
_DK_NIEUW = ('Dat zijn de blokjes van drie kanten samen. Blokjes op een rand tel je zo twee of drie keer, en blokjes achter en onder zie je niet. '
             'Reken één laag uit en doe die keer het aantal lagen.')
# Eigen regel 'drie kanten' op de motorregel 'fout = drie vlakken' (Oef-#1000: diep × breed + breed × hoog + diep × hoog, nooit het antwoord), vóór
# de CL 'route van Claude'. Nodig omdat de CL per sleutel het '/'-deel kiest dat het meest lijkt op Claudes uitleg («…aan de buitenkant ziet. Het
# bouwwerk is vol, dus er zitten ook blokjes binnenin.»): met de nieuwe tekst won daar 'de drie maten bij elkaar opgeteld' (zandbak: 33 keer fout).
# Het deel in de CL-tekst wordt ook vervangen (b6/check leest de routeteksten daaruit; zo kan de oude tekst nergens meer terugkomen).
_l1e = [f_ for f_ in _copy.deepcopy(_S[(V1, 2)]['foutHints']) if f_['soort'] != 'drie kanten']
for f_ in _l1e:
    f_['tekst'] = ' / '.join(_DK_NIEUW if d_ == _DK_OUD else d_ for d_ in f_['tekst'].split(' / '))
    if f_.get('tekstSterker') == _DK_OUD: f_['tekstSterker'] = _DK_NIEUW
_cl1e = next(f_ for f_ in _l1e if f_['regel'].startswith('Claudes sleutels (alle)'))
_l1e.insert(_l1e.index(_cl1e), {'bron': 'nieuw', 'soort': 'drie kanten', 'claudeDenkfout': None, 'regel': 'fout = drie vlakken', 'tekst': _DK_NIEUW,
                                'tekstSterker': _cl1e.get('tekstSterker'), 'waarom': "V-#1061: eigen regel, zodat de CL-tekstkeuze (op gelijkenis) hem niet mist"})
if _l1e != _S[(V1, 2)]['foutHints']:
    PATCH.append((V1, 2, 'foutHints', _l1e, "Ronde 1e (Oefeningen 8 okt; Didactiek V-#1061): 'drie kanten' zonder richting ('binnenin' weg, waar voor alle 33)"))

if __name__ == '__main__':
    patch_lib.run(6, PATCH)
