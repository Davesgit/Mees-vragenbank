#!/usr/bin/env python3
"""Schrijft hints/batch5.json (G8 batch 5: MEET-E03 #1–#9 (inhoud m³ → liter; MB/GB/TB/KB), MEET-E05 #1–#3 (getallenlijn en temperatuur
onder nul), MEET-E06 #1–#12 (vliegtijd en tijdzones) = 24 somtypes, 293 kale items).
8 okt 2026 (16:3x), Oefeningen. Formaat als make_batch4.py (kale items: rekenregels uit scripts/fout_regels.py, labelregels, geen letterlijke regels).
Data: live g8 (build 16:13:53/55). Lessen: hints/lessen_g8.md t/m les 307.
Analyse en checks: /workspace/g8work/b5/check.py op de zandbak /workspace/g8work/b5/sbx.sh (verse kopie van live).
Keuzes:
- Alleen regels die de motor leest (geen ONLEESBAAR): 'fout = een getal uit de vraag' eerst (ook de uitkomst van de rekenmachine zelf),
  dan 'antwoord + 1' (alleen 'nodig'; 'antwoord - 1' vuurt nooit, zie Oef-#490), 'een kommagetal', 'antwoord : 10' / '× 10'; 'andere fout' als laatste, met een
  tekst die ook klopt voor de Claude-sleutels die daar landen (b4/check rekent elke sleutel na).
- MEET-E06: de motor leest geen G8-kloktijd ('12.00 uur'); Claudes sleutels vangen labelregels per somtype (claudeDenkfout, les 270), met een
  tekst die voor elke sleutel onder dat label klopt (b5/check rekent elke tijd na). Geen kloktijden in de teksten (les 262, besluit kloktijden 15:46).
- MEET-E05: de motor rekent niet met getallen onder nul; Claudes sleutels hebben geen label. Wat geen rekenregel pakt (één ernaast onder nul,
  bij #3 ook 'min vergeten' en 'omhoog'), landt op 'andere fout', met een tekst die voor elke route klopt (datapunt).
- Geen cijfers, geen woorden van de [ding]/[plek]/[wie]-plekken (les 147), geen plekwoorden (les 193), geen 'zoveel' vooraan (les 197/272),
  geen kloktijden (les 262). H2 bij een kale som = de rekenstappen zonder uitkomst (les 144).
Na een sync nooit --force: correcties via hints/patch_batch5.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B5_OUT', f'{BASE}/hints/batch5.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch5.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch5.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch5.json bestaat al: patch in place (hints/patch_batch5.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
L = R   # letterlijke regel: 'regel' is de hele tekst van de foute optie
def CL(soort, label, tekst, sterker):
    """labelregel: Claudes sleutels met dit claudeDenkfout-label (geen motorregel die ze pakt, Oef-#490); vaste tekst zonder getallen, per sleutel nagerekend"""
    f = T(soort, f'Claudes sleutel: {label}', tekst, None, 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt (Oef-#490/#494); vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', label)
    f['tekstSterker'] = sterker; return f
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
E3, E5, E6 = "G8-MEET-E03", "G8-MEET-E05", "G8-MEET-E06"


# ================= MEET-E03 #1–#4: kubieke meter → liter (kaal) =================
H2_M3 = 'Doe het aantal kubieke meter keer duizend. Bij een kommagetal schuift de komma dan drie plekken op. Vul aan met nullen.'
FH_M3 = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat is het aantal kubieke meter. De vraag wil liters: hoeveel liter past er in één kubieke meter?', H2_M3),
         R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. In één kubieke meter past duizend liter, niet honderd.', H2_M3),
         R('nul te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel: er staat een nul te veel. In één kubieke meter past duizend liter.', H2_M3),
         ALG('Eén kubieke meter is duizend liter. Hoeveel liter is dan het aantal kubieke meter uit de vraag?', H2_M3)]
for n_ in (1, 2, 3, 4):
    E.append((E3, n_, 'Een kubieke meter is een kubus van een meter lang, een meter breed en een meter hoog. Daar past duizend liter in.', H2_M3,
              'Je kind rekent kubieke meters om naar liters: in één kubieke meter past duizend liter.', FH_M3))

# ================= MEET-E03 #5: filmpjes op een geheugenkaart (GB → MB, dan delen) =================
H2_KAART = 'Doe het aantal GB van de kaart keer duizend. Dan weet je hoeveel MB er op de kaart past. Deel dat door het aantal MB van één filmpje.'
E.append((E3, 5, 'Reken eerst de kaart om naar MB. Dan staan de kaart en het filmpje in dezelfde maat.', H2_KAART,
          'Je kind rekent eerst GB om naar MB (keer duizend) en deelt dan door de grootte van één filmpje.',
          [R('nul te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel. Tel de nullen nog eens na: hoeveel MB past er op de kaart?', H2_KAART),
           R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Tel de nullen nog eens na: hoeveel MB past er op de kaart?', H2_KAART),
           R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt hoeveel filmpjes er op de kaart passen.', H2_KAART),
           ALG('Reken eerst de kaart om naar MB: keer duizend. Deel dan door het aantal MB van één filmpje. Tel de nullen goed.', H2_KAART)]))

# ================= MEET-E03 #6–#9: TB → GB, MB → KB, GB → MB (de omrekening staat in de vraag) =================
for n_, groot, klein in ((6, 'TB', 'GB'), (7, 'MB', 'KB'), (8, 'GB', 'MB'), (9, 'GB', 'MB')):
    h2_ = f'Doe het aantal {groot} keer duizend: zet er drie nullen achter. Bij een kommagetal schuift de komma drie plekken op.'
    E.append((E3, n_, f'In de vraag staat hoeveel {klein} er in één {groot} gaan. Dat is duizend.', h2_,
              f'Je kind rekent {groot} om naar {klein}: keer duizend.',
              [R('getal uit de vraag', 'fout = een getal uit de vraag', f'Dat getal staat al in de vraag. Je zoekt hoeveel {klein} het is.', h2_),
               R('nul te weinig', 'fout = antwoord : 10', f'Dat is tien keer te weinig. Eén {groot} is duizend {klein}, niet honderd.', h2_),
               R('nul te veel', 'fout = antwoord × 10', f'Dat is tien keer te veel: er staat een nul te veel. Eén {groot} is duizend {klein}.', h2_),
               ALG(f'Eén {groot} is duizend {klein}. Hoeveel {klein} is dan het aantal {groot} uit de vraag?', h2_)]))

# ================= MEET-E05 #1: getal op de getallenlijn zetten (stip, kaal antwoord) =================
H2_LIJN = 'Staat er een min voor het getal? Ga dan vanaf de nul naar links. Zonder min ga je naar rechts. Tel de stappen.'
E.append((E5, 1, 'Getallen onder nul staan links van de nul. Getallen boven nul staan rechts van de nul.', H2_LIJN,
          'Je kind zet een getal op de getallenlijn: met een min ervoor links van de nul, zonder min rechts.',
          [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Kijk goed naar het teken voor het getal. Een min betekent: onder nul, links van de nul.', H2_LIJN),
           ALG('Kijk of er een min voor het getal staat. Met een min staat het links van de nul, zonder min rechts.', H2_LIJN)]))

# ================= MEET-E05 #2: van boven nul naar onder nul (kouder) =================
H2_T2 = 'Ga eerst omlaag tot nul. Tel hoeveel graden je daarna nog verder omlaag moet. Het wordt dat aantal graden onder nul: zet er een min voor.'
E.append((E5, 2, 'Kouder betekent: de temperatuur gaat omlaag op de thermometer.', H2_T2,
          'Je kind rekent met temperaturen onder nul: eerst omlaag tot 0, dan verder omlaag. Onder nul staat er een min voor het getal.',
          [R('warmer', 'fout = getal1 + getal2', 'Dat is warmer dan aan het begin. Kouder betekent omlaag op de thermometer.', H2_T2),
           R('min vergeten', 'fout = getal1 - getal2 of getal2 - getal1', 'Het wordt kouder dan nul. Onder nul zet je een min voor het getal.', H2_T2),
           R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt de temperatuur nadat het kouder is geworden.', H2_T2),
           ALG('Tel nog eens, graad voor graad: eerst omlaag tot nul, dan verder omlaag. Onder nul komt er een min voor het getal.', H2_T2)]))

# ================= MEET-E05 #3: van onder nul nog verder omlaag =================
H2_T3 = 'Tel de graden onder nul en de graden die het kouder wordt bij elkaar op. Zo ver onder nul kom je: zet er een min voor.'
E.append((E5, 3, 'Het is al onder nul. Kouder betekent: nog verder omlaag op de thermometer.', H2_T3,
          'Je kind rekent met temperaturen onder nul: van onder nul nog verder omlaag. Het antwoord krijgt een min ervoor.',
          [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt de temperatuur nadat het nog kouder is geworden.', H2_T3),
           ALG('Je begint onder nul en gaat nog verder omlaag. Dan blijf je onder nul: er komt een min voor het getal. Tel de graden nog eens na.', H2_T3)]))

# ================= MEET-E06: hoe laat landt het? (#1, #4, #11 met minuten; #8 hele uren) =================
H1_VL = 'Tel de duur van de vlucht op bij de vertrektijd: eerst de uren, dan de minuten.'
H2_VL = 'Doe eerst de hele uren van de vlucht erbij. Doe daarna de minuten erbij. Zestig minuten is een uur: kom je daarover, dan schuift de klok een uur door.'
OZ_VL = 'Je kind rekent uit hoe laat een vliegtuig landt: de uren en de minuten van de vlucht komen bij de vertrektijd.'
FH_VL = [CL('een uur te vroeg', 'tijd-als-kommagetal', 'Dat is een uur te vroeg. Tel de uren van de vlucht nog eens na, en kijk of de minuten samen over een heel uur gaan.', H2_VL),
         CL('minuten vergeten', 'klok-verkeerd-gelezen', 'Daar zitten alleen de hele uren van de vlucht in. De minuten van de vlucht moeten er ook nog bij.', H2_VL),
         ALG('Doe eerst de uren van de vlucht erbij, en dan de minuten. Zestig minuten is een uur.', H2_VL)]
for n_ in (1, 4, 11):
    E.append((E6, n_, H1_VL, H2_VL, OZ_VL, FH_VL))
H2_VL8 = 'Doe de uren van de vlucht erbij. De minuten blijven hetzelfde als bij vertrek.'
E.append((E6, 8, 'De vlucht duurt een aantal hele uren. Tel die op bij de vertrektijd.', H2_VL8, OZ_VL,
          [CL('een uur te vroeg', 'tijd-als-kommagetal', 'Dat is een uur te vroeg. Tel de uren van de vlucht nog eens na.', H2_VL8),
           CL('minuten veranderd', 'klok-verkeerd-gelezen', 'Dat is te vroeg. De vlucht duurt hele uren: de minuten blijven hetzelfde als bij vertrek.', H2_VL8),
           ALG('Doe de uren van de vlucht erbij. De minuten veranderen niet.', H2_VL8)]))

# ================= MEET-E06: tijdzones (later: #2, #5, #10; vroeger: #3, #6, #7, #9, #12) =================
def zone(later, minuten=True, nacht=False):
    h1 = ('Reken eerst uit hoe laat het thuis is als het vliegtuig aankomt. Op de plek van aankomst is het ' + ('later' if later else 'vroeger') + ' dan thuis.')
    duur = 'de uren en de minuten van de vlucht' if minuten else 'de uren van de vlucht'
    h2 = (f'Doe {duur} bij de vertrektijd: dat is de tijd thuis. ' + ('Doe het tijdsverschil daar nog bij.' if later else 'Haal het tijdsverschil daar nog vanaf.'))
    if nacht: h2 += (' Kom je voorbij middernacht? Dan begint de klok weer bij nul.' if later else ' Let op middernacht: ga je daar vooruit voorbij, dan begint de klok weer bij nul. Ga je terug voorbij middernacht, dan is het nog de avond ervoor.')
    oz = ('Je kind rekent met tijdzones: eerst de tijd thuis bij aankomst, dan het tijdsverschil ' + ('erbij (later).' if later else 'eraf (vroeger).'))
    fh = [CL('tijd thuis', 'tijd-als-kommagetal', 'Dat is de tijd thuis. Op de plek van aankomst is het ' + ('later: doe het tijdsverschil erbij.' if later else 'vroeger: haal het tijdsverschil eraf.'), h2),
          CL('verkeerde kant op', 'verkeerde-bewerking', ('Dat is vroeger dan thuis. Op de plek van aankomst is het juist later: het tijdsverschil komt erbij.' if later
                                                           else 'Dat is later dan thuis. Op de plek van aankomst is het juist vroeger: het tijdsverschil gaat eraf.'), h2),
          ALG('Reken eerst de tijd thuis uit. ' + ('Daar is het later, dus het tijdsverschil komt erbij.' if later else 'Daar is het vroeger, dus het tijdsverschil gaat eraf.'), h2)]
    return h1, h2, oz, fh
for n_, later, minuten, nacht in ((2, True, True, False), (5, True, False, True), (10, True, True, True),
                                  (3, False, True, False), (6, False, False, False), (7, False, True, False), (9, False, False, False), (12, False, True, True)):
    E.append((E6, n_) + zone(later, minuten, nacht))

# ---------------- schrijven ----------------
def reden(t):
    if re.search(r'\d', t): return 'tekst met getallen uit het item; nu een vaste tekst zonder cijfers (regel nagerekend), met eigen laag 2'
    if re.match(r'Je (hebt|telde|bent|noemde|vergat|deelde|nam|zit)\b', t): return 'zegt zeker wat het kind deed; nu een waardezin of een vraag (les 20/101/161), met eigen laag 2'
    return 'vervangen door een vaste tekst per regel, met eigen laag 2 (les 40)'
def sleutels(doel):
    t = open(f"{os.environ.get('DATA_BASE', BASE)}/somtypen/{doel}.md", encoding='utf-8').read()
    return {int(m[3]): (int(m[1]), m[2].strip(), m[4]) for m in
            re.finditer(r'^## Somtype (\d+): (.*)\n\n?- Sleutel: nrOrigineel \*\*(\d+)\*\* · somtypeOrigineel “(.*?)”', t, re.M)}
data = {}; S = []
for doel, nro, h1, h2, oz, fh in E:
    if doel not in data: data[doel] = json.load(open(f"{os.environ.get('DATA_BASE', BASE)}/data/per_doel/{doel}.json", encoding='utf-8'))['items']
    nr, kop, sto = sleutels(doel)[nro]
    st = {'doel': doel, 'nr': nr, 'somtype': kop, 'nrOrigineel': nro, 'somtypeOrigineel': sto, 'hint1': h1, 'hint2': h2, 'ouderzin': oz, 'foutHints': [dict(f) for f in fh]}
    cv = {}
    for it in data[doel]:
        if it['merge']['somtypeNrOrigineel'] != nro: continue
        dk = {x['fout']: x['denkfout'] for x in it['extraVelden'].get('claudeDenkfouten') or []}
        for f in it['extraVelden'].get('claudeFoutHints') or []:
            cv.setdefault(f['uitleg'], dk.get(f['fout']))
    if cv: st['claudeVervangen'] = [V(t, d, reden(t)) for t, d in cv.items()]
    S.append(st)
D = {'batch': 'batch5', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 5 = MEET-E03 #1–#9 + MEET-E05 #1–#3 + MEET-E06 #1–#12: kale items (inhoud en digitale maten; "
                "getallenlijn en temperatuur onder nul; vliegtijd en tijdzones)). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
