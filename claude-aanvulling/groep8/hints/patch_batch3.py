#!/usr/bin/env python3
"""Patcht hints/batch3.json IN PLACE (G8 batch 3: GET-E02 #37–#57 + GET-V02 #1–#4), via hints/patch_lib.py.
Idempotent: een tweede run geeft 0 wijzigingen; log in hints/wijzigingen_batch3.json. Na een sync of rebuild nooit make_batch3.py --force:
correcties komen hier als PATCH-regels (doel, nrOrigineel, veld, wordt, waarom), één blok per ronde.
LET OP: de G8-build van Overzicht draait dit bestand mee; zet hier alleen wat live mag.
Daarna (zandbak of build): python3 scripts/sync_hint_keys.py && python3 scripts/apply_hints.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_lib
from patch_lib import N, C, T, V, huidig, voeg_in

PATCH = []
# ---------- Ronde 1 (Oefeningen 8 okt): eerste versie in make_batch3.py; nog geen correcties ----------

# ---------- Ronde 1b (Oefeningen 8 okt ~16:05; data Oef-#485–#488 in build 16:00:03) ----------
R1B = 'Ronde 1b (Oefeningen 8 okt; build 16:00:03, Oef-#485–#488)'
E2, V2 = 'G8-GET-E02', 'G8-GET-V02'
import json as _json, os as _os
_B = _json.load(open(_os.path.join(patch_lib.BASE, 'hints', 'batch3.json'), encoding='utf-8'))
_S = {(s_['doel'], s_['nrOrigineel']): s_ for s_ in _B['somtypen']}
_fhs = {k_: [dict(f_) for f_ in v_['foutHints']] for k_, v_ in _S.items()}
def _zet(doel, nro, soort_, **upd):
    for f_ in _fhs[(doel, nro)]:
        if f_['soort'] == soort_: f_.update(upd)
# Oef-#485/#486 (regels '22' en '6 km', live 16:02–16:0x) zijn vervallen: Overzicht nam V-#820/Z-#823 over (build 16:04:49). De regels en de H2 van #40 staan nu in ronde 1c.
# Oef-#488: koppen zonder [ding] op een werkwoord/voorzetsel: nagekeken, geen tekst leunt op de kop
for k_ in ((E2, 38), (E2, 39), (E2, 41), (E2, 42), (E2, 43), (E2, 45), (V2, 3)):
    if _S[k_].get('kopGewijzigd') or _S[k_].get('kopNagekeken'): PATCH.append((k_[0], k_[1], 'kopNagekeken', None, R1B + ': kop nagekeken (Oef-#488), teksten passen'))

# ---------- Ronde 1c (Oefeningen 8 okt ~16:10; review-batch3-didactiek V-#820/V-#821, Z-#821/#822/#823; data build 16:04:49) ----------
R1C = 'Ronde 1c (Oefeningen 8 okt; review-batch3-didactiek, build 16:04:49)'
# V-#820: V02 #3 = «Twaalf kinderen een 5, zes een 7, twee een 9», opties 6 / 7 / 120. '7' = elk cijfer één keer ((5 + 7 + 9) : 3), '120' = het totaal, niet gedeeld.
_zet(V2, 3, 'elk cijfer één keer', regel='7',   # '7' = (5 + 7 + 9) : 3 én (5 + 9) : 2: de L1 klopt voor allebei (elk cijfer even zwaar), noemt geen uitkomst
     tekst='Dan telt elk cijfer even zwaar mee. Maar het ene cijfer hebben veel meer kinderen dan het andere. Elk cijfer telt zo vaak mee als er kinderen zijn met dat cijfer.')
_zet(V2, 3, 'totaal', regel='120')
# Z-#823/#826: V02 #4 = «2 km, 7 km, 5 km en 2 km», opties 4 km / 16 km / 4,5 km. '4,5 km' = het midden van de kortste en de langste dag (L1 van Didactiek, Z-#823).
_zet(V2, 4, 'langste dag', soort='midden', regel='4,5 km',
     tekst='Dat ligt precies tussen de kortste en de langste dag. Bij een gemiddelde tellen alle dagen mee: tel ze op en deel door het aantal dagen.')
_zet(V2, 4, 'midden', regel='4,5 km')
# V-#821.2: E02 #40 (nrO 33) H2 deelt geen woorden meer met het goede antwoord (tekst van Didactiek)
PATCH.append((E2, 33, 'hint2', 'Probeer elke aanpak uit met een paar woorden, bijvoorbeeld kat, aap en boom. Staan de woorden na elke aanpak in de goede volgorde?', R1C + ', V-#821: H2 noemt het antwoord niet (les 260)'))
# Z-#821: E02 #44 (nrO 37) H2 met vijf gelijke cijfers, zonder rekenregel
PATCH.append((E2, 37, 'hint2', 'Probeer elke aanpak met vijf keer een zeven. Het gemiddelde daarvan is zeven. Welke aanpak komt op zeven uit?', R1C + ', Z-#821: geen rekenregel in H2'))
# Z-#822: H1 #45/#55 (nrO 38/48): ook bij #55 ligt het andere getal dicht bij een rond getal; L2 #55 'vlak bij een van de getallen'
for n_ in (38, 48):
    PATCH.append((E2, n_, 'hint1', 'Eén van de getallen ligt vlak bij een rond getal. Met een rond getal reken je makkelijker.', R1C + ', Z-#822'))
for f_ in _fhs[(E2, 48)]:
    if 'vlak bij het getal ligt' in (f_.get('tekstSterker') or ''): f_['tekstSterker'] = f_['tekstSterker'].replace('vlak bij het getal ligt', 'vlak bij een van de getallen ligt')

# ---------- Ronde 1d (Oefeningen 8 okt ~16:20; V-#850, g8/gemiddelde-check-didactiek.md) ----------
# V02 #2 (002) krijgt in de build van Overzicht een derde dag (210, 320, 280 → 270; afleiders 265 en 810). VOORWAARDELIJK: dit blok doet alleen
# iets als de data van item nrO 2 drie dagen heeft en de opties precies het midden van kleinste/grootste en het totaal zijn. Op de oude data
# (twee dagen, 40/300/600) verandert er niets.
R1D = 'Ronde 1d (Oefeningen 8 okt; V-#850 + Z-#840, gemiddelde-check-didactiek / recheck-batch3-didactiek)'
# Signaal 1: de per_doel-data van 002 heeft al drie dagen (opties = midden kleinste/grootste, goede antwoord, totaal).
# Signaal 2: build_g8.py (Overzicht, alleen gelezen) bevat de datafix V-#850 met de dag van 210 mensen. Nodig omdat de patches vóór de build
# draaien (zoals _build_g7.sh): zonder dit signaal zou de ronde pas in de build ná de nieuwe data meekomen.
def _v850_in_build():
    p_ = _os.path.join(patch_lib.BASE, 'scripts', 'build_g8.py')
    try: s_ = open(p_, encoding='utf-8').read()
    except OSError: return None
    return ('265 mensen', '810 mensen') if ('V-#850' in s_ and '210 mensen' in s_ and '270 mensen' in s_) else None
def _v02_nro2():
    import re as _re
    p_ = _os.path.join(patch_lib.BASE, 'data', 'per_doel', 'G8-GET-V02.json')
    if not _os.path.exists(p_): return None
    try: its_ = _json.load(open(p_, encoding='utf-8'))['items']
    except Exception: return None
    x_ = next((i_ for i_ in its_ if i_['merge'].get('somtypeNrOrigineel') == 2), None)
    if x_ is None: return None
    dagen_ = [int(v_) for v_ in _re.findall(r'(\d+) mensen', x_['opgave'])]
    ops_ = [o_['tekst'] for o_ in x_.get('opties') or []]
    if len(dagen_) != 3: return None
    mid_, tot_ = (min(dagen_) + max(dagen_)) / 2, sum(dagen_)
    if mid_ != int(mid_) or tot_ % 3: return None
    r_mid, r_tot, r_ant = f'{int(mid_)} mensen', f'{tot_} mensen', f'{tot_ // 3} mensen'
    if sorted(ops_) != sorted([r_mid, r_tot, r_ant]) or x_['antwoord'] != r_ant: return None
    return r_mid, r_tot
_v850 = _v02_nro2() or _v850_in_build()
if _v850:
    H2_V850 = 'Tel de aantallen van alle dagen bij elkaar op: dat is het totaal. Verdeel dat eerlijk: deel het totaal door het aantal dagen.'
    PATCH.append((V2, 2, 'hint2', H2_V850, R1D + ': drie dagen, H2 zegt alle dagen'))
    _zet(V2, 2, 'verschil', soort='midden van kleinste en grootste')
    _zet(V2, 2, 'midden van kleinste en grootste', regel=_v850[0],
         tekst='Je hebt alleen de kleinste en de grootste dag gebruikt. Bij gemiddeld per dag tellen alle dagen mee.',
         tekstSterker='Een gemiddelde per dag gebruikt elke dag. Tel de aantallen van alle dagen op en deel het totaal door het aantal dagen.')
    _zet(V2, 2, 'totaal', regel=_v850[1],
         tekst='Dat is het totaal van de drie dagen. Gemiddeld per dag is dat totaal eerlijk verdeeld over de dagen.',
         tekstSterker='Je hebt alle dagen opgeteld: dat is het totaal. Deel dat totaal nog door het aantal dagen.')
    _zet(V2, 2, 'andere fout', tekstSterker=H2_V850)

# Z-#840 (Didactiek, recheck b3): V02 #3 L1 bij '7' — drie cijfers, dus niet 'het ene … het andere' (les 301: waar voor elke route naar 7)
_zet(V2, 3, 'elk cijfer één keer',
     tekst='Dan telt elk cijfer even zwaar mee. Maar sommige cijfers komen veel vaker voor dan andere. Elk cijfer telt zo vaak mee als er kinderen zijn met dat cijfer.')

# ---------- afsluiting (alle rondes): foutHints één keer per somtype ----------
for k_, l_ in _fhs.items():
    if l_ != _S[k_]['foutHints']: PATCH.append((k_[0], k_[1], 'foutHints', l_, (R1D if k_ in ((V2, 2), (V2, 3)) else R1C) + ': letterlijke regels volgen de afleiders (V-#820/Z-#823/V-#850); Z-#822 L2 #55'))

if __name__ == '__main__':
    patch_lib.run(3, PATCH)
