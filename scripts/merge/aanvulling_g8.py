"""Aanvulling uit G8 (besluiten Didactiek g8/besluiten_twijfel.json + Dave 20:56): de G8-build schrijft g{N}/data/aanvulling_uit_g8.json
(items die naar G4–G7 gaan: naar-G4 … naar-G7, en terug-G7). De build van groep N neemt ze hiermee op als gemapt item.
- Het id blijft het G8-id (al in de naamruimte van het doel: G5-GET-E07-claude-bank-naar-009, G7-GET-04-claude-bank-terug-001); het staat
  bevroren in g8/bevroren/ids_v1.json.
- merge.uitG8 = herkomst (status/regel in G8, besluit Didactiek). gebruikt-lijsten van hogere groepen en van G8 slaan deze items over
  (anders valt een item na de volgende G8-build uit de G8-pool en daarmee uit de aanvulling).
- Geen bestand = geen items: de build blijft dan gelijk.
Gebruik (in build_gN.py, na de bevroren ids en vóór het ontdubbelen):  rows += AV8.laad(N, OUT, OURS, somtype_functie, bestaande_ids)"""
import json, os, copy
TAG = '-claude-bank-naar-'
# T1/T7/T8 (Dave 20:56 (3)): de nieuwe contexten wisselen per item (namen, dingen); één somtype per soort som, anders krijgt Oefeningen
# tientallen somtypes met dezelfde hints. contextSoort zet g8/scripts/besluiten_g8.context_terug.
KOP = {'keer': 'Verhaalsom keer: # groepjes met elk # [ding]. Hoeveel samen?',
       'delen': 'Verhaalsom delen: # [ding] eerlijk verdeeld over # [ding]. Hoeveel elk?',
       'plus': 'Verhaalsom plus: # [ding], er komen er # bij. Hoeveel nu?',
       'min': 'Verhaalsom min: # [ding], er gaan er # weg. Hoeveel nog?',
       'prijs per stuk': 'Prijs per stuk: # [ding] kosten samen €#. Hoeveel kost één?',
       'meerstaps': 'Twee stappen: # keer # [ding], daarna # eraf. Hoeveel nog?',
       'wisselgeld': 'Wisselgeld: [wie] koopt # [ding] van €# per stuk en betaalt met €#. Hoeveel terug?'}
def is_uit_g8(it): return bool((it.get('merge') or {}).get('uitG8'))
def laad(groep, OUT, OURS, somtype, bestaand=()):
    p = f'{OUT}/data/aanvulling_uit_g8.json'
    if not os.path.exists(p): return []
    D = json.load(open(p)); out = []; bestaand = set(bestaand)
    for x in D['items']:
        it = copy.deepcopy(x); m = it['merge']
        doel = m.get('voorstelDoel') or m.get('doel')
        assert doel and doel.startswith(f'G{groep}-') and doel in OURS, ('aanvulling uit G8: doel past niet bij de groep', groep, it['id'], doel)
        assert it['id'].startswith(f'{doel}-claude-bank-'), ('aanvulling uit G8: id niet in de naamruimte van het doel', it['id'], doel)
        assert it['id'] not in bestaand, ('aanvulling uit G8: id bestaat al in de groep', it['id'])
        d8 = m.get('didactiekG8') or {}
        m['uitG8'] = {'g8Status': m['status'], 'g8Regel': m.get('regel'), 'twijfelId': d8.get('twijfelId'),
                      'besluit': (d8.get('didactiek') or {}).get('besluit'), 'hintStatus': d8.get('hintStatus') or m.get('hintStatus'),
                      'bestand': 'data/aanvulling_uit_g8.json', 'g8Build': D.get('gegenereerdOp')}
        m['status'] = 'gemapt'; m['doel'] = doel; it['doelId'] = doel; m.pop('voorstelDoel', None); m['duplicaatVan'] = None
        m['somtypeG8'] = m.get('somtype'); m['somtype'] = KOP[m['contextSoort']] if m.get('contextSoort') else somtype(it)
        out.append(it); bestaand.add(it['id'])
    return out
