#!/usr/bin/env python3
"""G7-fixlijst (Overzicht), review batch 1 van Didactiek (8 okt 2026, g7/review-batch1-didactiek.md).
- V-#516: DENK-03 nrO 7 (sap). 3 + 2 = 5 gaf het goede antwoord, en een pak van 2 L / een kan met 6 L klopt niet met de referentiematen.
  Nieuw: 3 flesjes van 3 dl, er gaat 2 dl uit. Antwoord 7 dl; afleiders 9 dl (stap twee vergeten) en 4 dl (3 + 3 − 2: opgeteld in plaats van keer).
  TODO Oefeningen: hint1/hint2/foutHints van de entry (batch1 DENK-03 nrO 7) noemen nog 'pakken' en 'liter', en de regels '6 liter'/'4 liter'
  moeten '9 dl'/'4 dl' worden. Tot dan geeft check_hints een FAIL op die entry (tijdelijk goed, opdracht 11:56).
- Z-#525: de somtypes 'welke tekening/som' in DENK-02 krijgen allemaal visual.nodig = True met nietLiveZonderBeeld (zoals #4/#9/#10/#13).
  #3 ('gekleurd'): komt er een tekening, markeer het groepje dan ook anders dan met kleur.
Schrijft zelf niets; build_g7.py roept pas_toe(it, slog) aan na FX21, vóór hercontrole en de somtype-indeling."""
import re
V516_ID = 'dc788280-ed3c-4f4b-96b9-0a8424c3baee'
TODO516 = ("TODO Oefeningen (V-#516, 8 okt): opgave omgebouwd naar 3 flesjes van 3 dl, 2 dl eruit (7 dl). Werk H1, H2, ouderzin en de fout-hints "
           "van batch1 DENK-03 nrO 7 bij: 'pakken'/'liter' → 'flesjes'/'dl', regels '6 liter' → '9 dl' en '4 liter' → '4 dl'.")
Z525_TEKENING = {('G7-DENK-02', 'Er zijn # kinderen op het schoolplein'), ('G7-DENK-02', 'Je koopt # zakjes knikkers')}
def _v516(it, slog):
    if it['bron'].get('claudeId') != V516_ID: return
    oud = it['opgave']
    assert oud.startswith('Je hebt 3 pakken sap van elk 2 liter'), oud
    it['opgave'] = 'Je hebt 3 flesjes sap van elk 3 dl. Stap 1: giet alles in een kan. Stap 2: giet er 2 dl uit. Hoeveel dl zit er nog in de kan?'
    it['opties'] = [{'letter': 'A', 'tekst': '4 dl'}, {'letter': 'B', 'tekst': '7 dl'}, {'letter': 'C', 'tekst': '9 dl'}]
    it['optiesTekst'] = 'A) 4 dl · B) 7 dl · C) 9 dl'
    it['antwoord'] = '7 dl'; it['antwoordDetail'] = {'juisteOptie': 'B', 'juisteOptieTekst': '7 dl'}
    fh = [{'stap': None, 'fout': '9 dl', 'uitleg': 'Na stap 1 zit dat erin. Maar stap 2 moet je ook nog uitvoeren.'},
          {'stap': None, 'fout': '4 dl', 'uitleg': 'Je hebt 3 en 3 opgeteld. Elk flesje heeft 3 dl, dus hoeveel keer 3 dl is dat?'}]
    it['foutHints'] = fh
    it['foutHintsTekst'] = ' · '.join(f"{f['fout']} → {f['uitleg']}" for f in fh)
    ev = it['extraVelden']
    ev['claudeUitleg'] = '3 flesjes van 3 dl is 9 dl. Daar gaat 2 dl af. Er blijft 7 dl in de kan.'
    ev['claudeFoutHints'] = [dict(f) for f in fh]
    ev['claudeDenkfouten'] = [{'fout': '9 dl', 'denkfout': None}, {'fout': '4 dl', 'denkfout': 'optellen-ipv-vermenigvuldigen'}]
    it['merge']['todoOefeningen'] = TODO516
    it['merge']['v516'] = {'opgaveOud': oud, 'antwoordOud': '5 liter', 'optiesOud': ['4 liter', '5 liter', '6 liter']}
    slog(it, 'G7-V516 (review batch 1 Didactiek): sap 3 × 3 dl − 2 dl = 7 dl (3 + 2 gaf het goede antwoord; pak 2 L / kan 6 L)', 'opgave', oud, it['opgave'])
def _z525(it, slog):
    if it['merge'].get('doel') != 'G7-DENK-02' and it['doelId'] != 'G7-DENK-02': return
    o = re.sub(r'\d+', '#', it['opgave'])
    if not any(o.startswith(p) for d, p in Z525_TEKENING): return
    v = it['visual']
    if v.get('nodig') and v.get('nietLiveZonderBeeld'): return
    nv = dict(v, nodig=True, nietLiveZonderBeeld=True,
              toelichting='de vraag verwijst naar een tekening (welke tekening/som); zonder tekening niet live (Z-#525, zoals DENK-02 #4/#9/#10/#13)')
    if 'gekleurd' in ' '.join(x['tekst'] for x in it['opties'] or []):
        nv['eisAlsErEenPlaatjeKomt'] = 'het gekozen groepje niet alleen met kleur markeren: ook omcirkelen of arceren (les 11; Z-#525)'
    it['visual'] = nv
    slog(it, 'G7-Z525 (review batch 1 Didactiek): visual.nodig gelijk binnen de welke-tekening/som-somtypes van DENK-02', 'visual.nodig', str(v.get('nodig')), 'True')
def pas_toe(it, slog):
    _v516(it, slog); _z525(it, slog)
