#!/usr/bin/env python3
"""Schrijft hints/batch4.json (G8 batch 4: GET-E05 #1–#16 (rekenmachine-uitkomst in een verhaal: hoeveel nodig / hoeveel over),
GET-M01 #1–#5 (grote getallen: waarde van een cijfer, 'n miljoen' als getal), MEET-E01 #1–#2 (km → m) = 23 somtypes, 141 kale items).
8 okt 2026 (16:1x), Oefeningen. Formaat als make_batch1.py (kale items: rekenregels uit scripts/fout_regels.py, geen letterlijke regels).
Data: live g8 (build 16:06:27). Lessen: hints/lessen_g8.md t/m les 290.
Analyse en checks: /workspace/g8work/b4/check.py op de zandbak /workspace/g8work/b4/sbx.sh (verse kopie van live).
Keuzes:
- Alleen regels die de motor leest (geen ONLEESBAAR): 'fout = een getal uit de vraag' eerst (ook de uitkomst van de rekenmachine zelf),
  dan 'antwoord + 1' (alleen 'nodig'; 'antwoord - 1' vuurt nooit, zie Oef-#490), 'een kommagetal', 'antwoord : 10' / '× 10'; 'andere fout' als laatste, met een
  tekst die ook klopt voor de Claude-sleutels die daar landen (b4/check rekent elke sleutel na).
- E05: de motor kent geen regel voor het hele getal van de rekenmachine-uitkomst (en #390 houdt 'antwoord - 1' tegen), de cijfers achter de
  komma, de rest, 'hele getal + rest' of 'per stuk − rest'. Claudes sleutels daarvan vangen labelregels (claudeDenkfout, na de rekenregels,
  les 270) met een tekst die voor elke route onder dat label klopt; wat een kind anders typt, landt op 'andere fout' (datapunt Oef-#490).
- Geen cijfers, geen woorden van de [ding]/[plek]/[wie]-plekken (les 147), geen plekwoorden (les 193), geen 'zoveel' vooraan (les 197/272),
  geen kloktijden (les 262; batch 4 heeft er geen). H2 bij een kale som = de rekenstappen zonder uitkomst (les 144).
Na een sync nooit --force: correcties via hints/patch_batch4.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B4_OUT', f'{BASE}/hints/batch4.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch4.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch4.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch4.json bestaat al: patch in place (hints/patch_batch4.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
L = R   # letterlijke regel: 'regel' is de hele tekst van de foute optie
def CL(soort, label, tekst, sterker):
    """labelregel: Claudes sleutels met dit claudeDenkfout-label (geen motorregel die ze pakt, Oef-#490); vaste tekst zonder getallen, per sleutel nagerekend"""
    f = T(soort, f'Claudes sleutel: {label}', tekst, None, 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt (Oef-#490); vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', label)
    f['tekstSterker'] = sterker; return f
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
E5, M1, ME1 = "G8-GET-E05", "G8-GET-M01", "G8-MEET-E01"


# ================= GET-E05 rekenmachine-uitkomst in een verhaal (kaal) =================
H1_E5 = 'Op de rekenmachine staat een kommagetal. Het getal voor de komma zegt hoeveel er helemaal vol raken.'
# 'Hoeveel … zijn er nodig?' (naar boven afronden): nrO 1–6, 8, 10
H2_N = ('Staat er na de komma nog iets? Dan blijft er wat over dat nog nergens in zit. Ook dat moet ergens in: '
        'dan heb je er één meer nodig dan het getal voor de komma.')
OZ_N = 'Je kind leest de uitkomst van de rekenmachine in een verhaal. Blijft er iets over, dan is er nog één nodig: naar boven afronden.'
# 'fout = antwoord - 1' geeft hier nooit een sleutel: het hele getal van de rekenmachine-uitkomst telt in de motor als getal uit de vraag (#390,
# in_vraag390 met los=True), en 'een getal uit de vraag' pakt het niet (KOMMA437). Claudes sleutels vangen we met labelregels (CL); kind-invoer buiten Claudes sleutels landt op 'andere fout' (datapunt Oef-#490).
FH_N = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt hoeveel je er nodig hebt, zodat alles erin past.', H2_N),
        R('één te veel', 'fout = antwoord + 1', 'Dat is er één te veel. Reken het na: past alles ook in één minder?', H2_N),
        # labelregels ná 'één te veel' (Claude labelt ook echte één-te-veel-sleutels 'rest-vergeten', les 270); ze vallen niet onder #390 (geen ±1, geen 'Bijna')
        CL('rest nog niet erin', 'rest-vergeten', 'Na de volle blijft er nog wat over. Dat past samen in nog één. Hoeveel heb je er dan nodig?', H2_N),
        CL('wat overblijft', 'andere-deel-genomen', 'Dat is wat er overblijft na de volle. De vraag wil weten hoeveel je er nodig hebt, zodat alles erin past.', H2_N),
        R('kommagetal', 'fout = een kommagetal', 'Je zoekt een aantal, en dat is een heel getal. Kijk naar het getal voor de komma, en naar wat er na de komma staat.', H2_N),
        ALG('Het getal voor de komma zegt hoeveel er helemaal vol raken. Blijft er dan nog wat over? Ook dat moet ergens in. Hoeveel heb je er dan nodig?', H2_N)]
for n_ in (1, 2, 3, 4, 5, 6, 8, 10):
    E.append((E5, n_, H1_E5, H2_N, OZ_N, FH_N))
# '… gaan weg. Hoeveel blijven er over?' (de rest): nrO 7, 9, 11–16
H2_O = ('Doe het getal voor de komma keer het aantal dat er in één past: zoveel gaan er weg. '
        'Haal dat van het totaal af. Wat overblijft, is het antwoord.')
OZ_O = 'Je kind leest de uitkomst van de rekenmachine in een verhaal: de volle gaan weg, en het rekent uit hoeveel er nog over zijn.'
FH_O = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt hoeveel er overblijven als alle volle weg zijn.', H2_O),
        CL('aangevuld', 'andere-deel-genomen', 'Dat is wat er nog bij moet om er nog één vol te maken. De vraag wil weten hoeveel er overblijven.', H2_O),
        CL('getal van de rekenmachine', 'kommagetal-als-geheel', 'Dat getal zie je op de rekenmachine, maar het is niet wat er overblijft. Wat overblijft, reken je uit: haal de volle van het totaal af.', H2_O),
        R('kommagetal', 'fout = een kommagetal', 'Er blijft een aantal over, en dat is een heel getal. Wat er na de komma staat, is niet dat aantal. Reken het uit met het getal voor de komma.', H2_O),
        ALG('Hoeveel gaan er in alle volle samen? Haal dat van het totaal af: wat blijft er over?', H2_O)]
for n_ in (7, 9, 11, 12, 13, 14, 15, 16):
    E.append((E5, n_, H1_E5, H2_O, OZ_O, FH_O))

# ================= GET-M01 grote getallen (kaal) =================
H2_P = 'Tel hoeveel cijfers er na dat cijfer komen. Schrijf het cijfer op met evenveel nullen erachter.'
E.append((M1, 1, 'Hoeveel een cijfer waard is, hangt af van de plek in het getal: eenheden, tientallen, honderdtallen, enzovoort.', H2_P,
          'Je kind zoekt wat één cijfer in een groot getal waard is: dat cijfer met een nul voor elke plek die erna komt.',
          [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Je zoekt wat dat ene cijfer waard is, op de plek waar het staat.', H2_P),
           R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig: er mist een nul. Tel nog eens hoeveel cijfers er na dat cijfer komen.', H2_P),
           R('nul te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel: er staat een nul te veel. Tel nog eens hoeveel cijfers er na dat cijfer komen.', H2_P),
           ALG('Tel hoeveel cijfers er na dat cijfer komen. Evenveel nullen komen erachter.', H2_P)]))
H2_M = 'Een miljoen heeft zes nullen. Schrijf het getal uit de vraag op, en zet er zes nullen achter.'
FH_M = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat getal staat al in de vraag. Er staat miljoen achter: hoeveel nullen horen daarbij?', H2_M),
        R('nul te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig: er mist een nul. Een miljoen heeft zes nullen.', H2_M),
        R('nul te veel', 'fout = antwoord × 10', 'Dat is tien keer te veel: er staat een nul te veel. Een miljoen heeft zes nullen.', H2_M),
        CL('duizend keer te weinig', 'nul-fout-tientallen', 'Dat is duizend keer te weinig. Een miljoen is duizend keer duizend: dat zijn zes nullen.', H2_M),
        ALG('Een miljoen is duizend keer duizend: dat zijn zes nullen. Hoeveel nullen heeft jouw getal?', H2_M)]
for n_ in (2, 3, 4, 5):
    E.append((M1, n_, 'Een miljoen is duizend keer duizend.', H2_M, 'Je kind schrijft een aantal miljoen als getal: het getal met zes nullen erachter.', FH_M))

# ================= MEET-E01 kilometer → meter (kaal) =================
H2_K = 'Doe het aantal kilometer keer duizend. Bij een kommagetal schuift de komma dan drie plekken op. Vul aan met nullen.'
FH_K = [R('getal uit de vraag', 'fout = een getal uit de vraag', 'Dat is het getal in kilometer. De vraag wil meters: hoeveel meter is één kilometer?', H2_K),
        R('tien keer te weinig', 'fout = antwoord : 10', 'Dat is tien keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.', H2_K),
        CL('honderd keer te weinig', 'kommagetal-als-geheel', 'Dat is honderd keer te weinig. Eén kilometer is duizend meter: doe het aantal kilometer keer duizend.', H2_K),
        ALG('Eén kilometer is duizend meter. Hoeveel meter is dan het aantal kilometer uit de vraag?', H2_K)]
for n_ in (1, 2):
    E.append((ME1, n_, 'Een kilometer is duizend meter.', H2_K, 'Je kind rekent kilometer om naar meter: keer duizend.', FH_K))

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
D = {'batch': 'batch4', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 4 = GET-E05 #1–#16 + GET-M01 #1–#5 + MEET-E01 #1–#2: kale items (rekenmachine-uitkomst in een verhaal; "
                "grote getallen; km → m)). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
