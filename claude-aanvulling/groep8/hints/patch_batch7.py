#!/usr/bin/env python3
"""Patcht hints/batch7.json IN PLACE (G8 batch 7: VBN-E04 #6–#31), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch7.json. Na een sync of rebuild nooit make_batch7.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch7.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~17:30): Didactiek review-batch7 (V-#940–#943, Z-#941, Z-#942, Z-#944; Z-#943 voorwaardelijk) ----------
# Teksten per veld of per fout-hint (soort); een tweede run geeft 0. V-#944/V-#945/V-#946/Z-#945 zijn data van Overzicht (build_g8.py achter
# tools/g8_b7_vlag): de regels en teksten blijven daarbij waar (de letterlijke regels staan op foute opties die niet veranderen), alleen SNAP (b7/check).
R1B = 'Ronde 1b (Oefeningen 8 okt; Didactiek review-batch7)'
E04 = 'G8-VBN-E04'
import json as _json, os as _os
def _veld(nro, veld, wordt, waarom): PATCH.append((E04, nro, veld, wordt, f'{R1B}: {waarom}'))
def _fh(nro, soort, waarom, **upd): PATCH.append((E04, nro, ('fh', soort, upd), None, f'{R1B}: {waarom}'))
# Verplicht
_veld(8, 'hint2', 'De staaf stopt halverwege twee getallen op de as. Welk getal ligt precies in het midden van die twee? Kies de optie die daar het dichtst bij ligt.',
      "V-#940: de opgave zegt 'precies tussen' (les 351)")
_veld(11, 'hint2', 'Stel je een taart voor die schuin voor je staat. Welk stuk neemt in de tekening de meeste ruimte in? Past dat bij de percentages?',
      'V-#941: de H2 sprak de conclusie uit (les 350)')
_veld(27, 'hint2', 'Stel dat beide lijnen van onderaan tot halverwege hun as stijgen. Hoeveel is dat bij de ene as, en hoeveel bij de andere?',
      'V-#942: de H2 sprak de conclusie uit (les 350)')
_veld(25, 'hint1', 'Wat toont een cirkeldiagram: aantallen of percentages? En wat wordt er gevraagd?', 'V-#943: H1 als kijkvraag (zoals Z-#896)')
# Zacht
_veld(13, 'hint1', 'Wanneer gaan beide lijnen omhoog? Wat is er in die maanden anders?', 'Z-#941: H1 en H2 omgedraaid')
_veld(13, 'hint2', 'Stijgen twee lijnen tegelijk, dan kan er één reden zijn voor beide. Welke reden past bij de maanden waarin ze stijgen?', 'Z-#941: H1 en H2 omgedraaid')
_veld(23, 'hint2', 'Begint de as niet bij nul, dan zie je van elke staaf alleen het stuk boven het begingetal. Stel dat de ene staaf maar een klein beetje hoger is dan de andere. Hoe ziet dat er dan uit?',
      "Z-#942: zonder 'verschillen' (les 264 op de H2)")
_L2_7 = 'Het getal bij de as is niet het echte aantal. Het tekstje bij de as zegt keer hoeveel je het getal moet doen: keer duizend.'
for _s in ('getal van de as', 'keer honderd', 'andere fout'): _fh(7, _s, 'Z-#944: L2-taal', tekstSterker=_L2_7)
_fh(14, 'getallen fout', 'Z-#944: L1-taal', tekst='De getallen zelf kunnen best kloppen. Denk aan de maanden die er niet bij staan.')
_L2_18 = 'Afronden verbergt kleine verschillen. Twee staven die na afronden gelijk zijn, kunnen bij verschillende getallen horen.'
for _s in ('alleen omhoog', 'precies gelijk', 'andere fout'): _fh(18, _s, 'Z-#944: L2-taal', tekstSterker=_L2_18)
_fh(20, 'opgeteld', "Z-#944: '16' dubbelzinnig met 'groep 8'",
    tekst='Dat is het aantal plaatjes plus het getal bij één plaatje. Elk plaatje staat voor een heel groepje: doe keer.')
_veld(21, 'hint1', 'Een half plaatje staat voor de helft van wat één plaatje betekent.', "Z-#944: 'plaatje' in plaats van 'tekening'")
_L2_21 = 'Tel de volle plaatjes keer wat één plaatje betekent. Een half plaatje telt voor de helft. Tel alles bij elkaar op.'
for _s in ('halve als volle', 'plaatjes geteld', 'andere fout'): _fh(21, _s, "Z-#944: 'plaatje' ook in de L2 (zoals de rest van het somtype)", tekstSterker=_L2_21)
_L2_28 = 'Een handjevol uit één klas zegt weinig over de hele school. Je moet er veel meer vragen, uit verschillende klassen.'
for _s in ('allemaal rekenen', 'één klas', 'andere fout'): _fh(28, _s, "Z-#944: 'klassen' (opgave en opties zeggen 'klas')", tekstSterker=_L2_28)
_fh(28, 'één klas', "Z-#944: 'klassen'", tekst='Denk aan de andere klassen. Zouden die precies hetzelfde kiezen?')
# Z-#943 (VOORWAARDELIJK, samen met Overzichts Oef-#1004: één hondje voor 6 honden, 21; afleiders 24 en 4): alleen als de data van #21 dat al heeft.
# Signaal: data/per_doel/G8-VBN-E04.json (de build schrijft de data in fase 1, vóór de patches in fase 3).
# Ronde 1c (Z-#960, 8 okt ~17:45): de schakelaar werkt twee kanten op. Nieuwe data (21/24/4) → regel '24 honden' + L1 'Dat is het aantal plaatjes …';
# oude data (14/16/4, Overzichts b7-vlag terug) → regel '16 honden' + de oude L1 uit make_batch7 (waar door toeval, les 342/354);
# andere data → niets (b7/check en check_hints vallen dan op). Elke stand is idempotent; getoetst in vier standen (les 361).
def _hond_stand():
    p_ = _os.path.join(patch_lib.BASE, 'data', 'per_doel', f'{E04}.json')
    try: its_ = _json.load(open(p_, encoding='utf-8'))['items']
    except Exception: return None
    x_ = [i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == 21]
    if len(x_) != 1: return None
    st_ = (x_[0]['antwoord'], sorted(o_['tekst'] for o_ in x_[0].get('opties') or []))
    if st_ == ('21 honden', ['21 honden', '24 honden', '4 honden']): return 'nieuw'
    if st_ == ('14 honden', ['14 honden', '16 honden', '4 honden']): return 'oud'
    return None
_STAND21 = _hond_stand()
if _STAND21 == 'nieuw':
    _fh(21, 'halve als volle', "Z-#943: één hondje voor 6 honden; 'halve als volle' is nu 24", regel='24 honden')
    _fh(21, 'plaatjes geteld', "Z-#943: '4' is alleen nog het aantal plaatjes (les 354)",
        tekst='Dat is het aantal plaatjes. Eén plaatje staat voor meer dan één: reken uit wat alle plaatjes samen betekenen.')
elif _STAND21 == 'oud':
    _fh(21, 'halve als volle', "Z-#960: b7-data terug (één hondje voor 4); 'halve als volle' is weer 16", regel='16 honden')
    _fh(21, 'plaatjes geteld', "Z-#960: b7-data terug; 4 is weer het aantal plaatjes én wat één plaatje betekent (oude L1)",
        tekst='Dat getal is het aantal plaatjes, en ook wat één plaatje betekent. Reken uit wat alle plaatjes samen betekenen.')

if __name__ == '__main__':
    patch_lib.run(7, PATCH)
