#!/usr/bin/env python3
"""Schrijft hints/batch9.json (G8 batch 9: VERH-E05 #1–#21, VBN-V01 #1–#5 = 26 somtypes, 70 items): procent erbij (prijs stijgt, rente,
met hoeveel procent gestegen/gedaald) en grafieken lezen (rooster, lijngrafiek, cirkeldiagram, as, staafdiagram).
8 okt 2026 (18:3x), Oefeningen. Formaat als make_batch8.py. Data: live g8 (build 18:20:30). Lessen: hints/lessen_g8.md t/m les 374.
Analyse en checks: /workspace/g8work/b9/check.py op een verse kopie van live (sbx_build.sh met OVERLAY).
Keuzes:
- VERH-E05: de koppen zijn gesplitst (laatste zelfstandig naamwoord en de namen bij rente zijn geen [..]-plek, 'zak noten'; datapunten Oef-#1014–#1016):
  één tekstset per soort som, gedeeld door alle gesplitste koppen; geen woorden uit die koppen (les 147, kopwoorden van somtypes met dezelfde H1/H2).
- Claudes sleutels hebben een '€' bij een antwoord zonder '€' (Oef-#1006/#1017): labelregels (Oef-#490) met een tekst die voor elke sleutel van dat
  label waar is. Bij 'Vorig jaar … nu …' pakt de motorregel 'verschil van de getallen' het verschil (eigen tekst), de labelregel de rest.
- Meerkeuze (E05 #21, V01 #2–#5): per foute optie een letterlijke regel (G8-2). V01 #1 (rooster): Claudes sleutels zonder label (omgewisseld).
- Geen cijfers, geen woorden van de [..]-plekken (les 147), geen plekwoorden (les 193), geen 'even veel' (#192), geen 'ongeveer' (vormcue, les 372),
  verklaptoets meerkeuze (les 260/264 op H1 én H2, Z-#824), les 350 (H2 spreekt de conclusie niet uit), les 351 (woorden van de opgave).
Na een sync nooit --force: correcties via hints/patch_batch9.py."""
import json, re, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.environ.get('B9_OUT', f'{BASE}/hints/batch9.json')
if os.path.exists(OUT):
    t = open(OUT, encoding='utf-8').read()
    if '"koppeling"' in t or '"kopGewijzigd"' in t:
        sys.exit('hints/batch9.json is gesynct (koppeling/kopGewijzigd): patch in place met hints/patch_batch9.py, nooit --force.')
    if '--force' not in sys.argv:
        sys.exit('hints/batch9.json bestaat al: patch in place (hints/patch_batch9.py), of --force als er nog geen sync is geweest.')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import N, T, V

E = []  # (doel, nrOrigineel, hint1, hint2, ouderzin, foutHints)
def R(soort, regel, tekst, sterker):
    f = N(soort, regel, tekst); f['tekstSterker'] = sterker; return f
def CL(soort, label, tekst, sterker, regel=None):
    """labelregel: Claudes sleutels met dit claudeDenkfout-label (label None: alle sleutels van Claude); vaste tekst zonder getallen, per sleutel nagerekend"""
    f = T(soort, regel or f'Claudes sleutel: {label}', tekst, None, 'Claudes sleutels met dit label: geen motorregel die ze allemaal pakt (Oef-#490/#494); vaste tekst zonder getallen, per sleutel nagerekend, met eigen laag 2', label)
    f['tekstSterker'] = sterker; return f
def ALG(tekst, sterker):
    return R('andere fout', 'andere fout', tekst, sterker)
def LT(soort, optie, tekst, sterker):
    """letterlijke regel: de hele tekst van de foute optie (G8-2)"""
    return R(soort, optie, tekst, sterker)
E05, V01 = "G8-VERH-E05", "G8-VBN-V01"
def ST(doel, nr, h1, h2, oz, fh):
    E.append((doel, nr, h1, h2, oz, fh))

# ---- VERH-E05 #1, #18 (zak noten): met hoeveel procent is de prijs gestegen (antwoord zonder '€', sleutels met '€') ----
H2 = 'Haal de oude prijs van de nieuwe prijs af: zoveel euro komt erbij. De oude prijs is honderd procent. Hoeveel procent is dan het bedrag dat erbij komt?'
for nr in (1, 18): ST(E05, nr, 'Hoeveel euro komt er bij de prijs? Welk deel van de oude prijs is dat?', H2,
                      'Je kind rekent uit met hoeveel procent een prijs is gestegen.',
                      [CL('nog geen procent van de oude prijs', 'procent-verkeerde-basis', 'Dat is nog geen procent van de oude prijs. De oude prijs is honderd procent: hoeveel procent komt erbij?', H2),
                       ALG('Hoeveel euro komt erbij? De oude prijs is honderd procent: hoeveel procent is dat bedrag?', H2)])
# ---- VERH-E05 #3: vorig jaar # [ding], nu #: met hoeveel procent gestegen ----
H2 = 'Haal het oude aantal van het nieuwe aantal af: zoveel zijn er nu meer. Het oude aantal is honderd procent. Hoeveel procent is dan dat verschil?'
ST(E05, 3, 'Hoeveel zijn er nu meer dan vorig jaar? Welk deel van het oude aantal is dat?', H2,
   'Je kind rekent uit met hoeveel procent een aantal is gestegen.',
   [R('verschil', 'fout = verschil van de getallen', 'Dat is hoeveel er nu meer zijn, nog geen procent. Hoeveel procent van het oude aantal is dat?', H2),
    CL('nieuwe aantal als basis', 'procent-verkeerde-basis', 'Vergelijk met het oude aantal: dat is honderd procent, niet het nieuwe aantal.', H2),
    ALG('Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?', H2)])
# ---- VERH-E05 #2, #4, #9, #10, #20: rente, hoeveel staat er na één jaar op de rekening ----
H2 = 'Deel het bedrag door honderd: dat is één procent. Doe dat keer het procent: dat is de rente. Tel de rente op bij het bedrag dat er al op stond.'
R_FH = [CL('alleen de rente', 'andere-deel-genomen', 'Dat is alleen de rente. Gevraagd is wat er na één jaar in totaal op de rekening staat.', H2),
        CL('tien keer te veel rente', 'komma-verschoven', 'Zo komt er tien keer te veel rente bij. Eén procent is het bedrag gedeeld door honderd. Doe dat keer het procent.', H2),
        CL('rente eraf', 'verkeerde-bewerking', 'Rente krijg je erbij. Na een jaar staat er dus meer op de rekening dan eerst.', H2),
        ALG('Reken eerst de rente uit. Tel die op bij het bedrag dat er al op stond.', H2)]
for nr in (2, 4, 9, 10, 20): ST(E05, nr, 'Procent betekent: zoveel van de honderd. Hoeveel euro rente komt er in één jaar bij?', H2,
                                'Je kind rekent uit hoeveel geld er na een jaar met rente op de rekening staat.', R_FH)
# ---- VERH-E05 #5–#17, #19: de prijs stijgt met #%, wat kost het nu ----
H2 = 'Deel de oude prijs door honderd: dat is één procent. Doe dat keer het procent: zoveel komt er bij de prijs. Tel dat op bij de oude prijs.'
P_FH = [CL('alleen wat erbij komt', 'andere-deel-genomen', 'Dat is alleen wat erbij komt. Gevraagd is wat het nu kost: tel het op bij de oude prijs.', H2),
        CL('eraf', 'verkeerde-bewerking', 'De prijs stijgt: wat erbij komt, tel je op bij de oude prijs. Haal het er niet af.', H2),
        CL('procent als euro', 'procent-verkeerde-basis', "Zo komt het getal van het procent erbij als euro's. Hoeveel euro is dat procent van de oude prijs?", H2),
        ALG('Reken uit hoeveel euro het procent van de oude prijs is. Tel dat op bij de oude prijs.', H2)]
for nr in list(range(5, 18)) + [19]:
    if nr in (9, 10): continue
    ST(E05, nr, 'De prijs stijgt: er komt een deel van de oude prijs bij. Hoeveel euro is dat procent van de oude prijs?', H2,
       'Je kind rekent uit wat iets kost als de prijs met een procent stijgt.', P_FH)
# ---- VERH-E05 #21 (054): met hoeveel procent is de verkoop gedaald, meerkeuze ----
H2 = 'Haal het nieuwe aantal van het oude aantal af: zoveel minder is het. Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?'
ST(E05, 21, 'Hoeveel minder is er verkocht? Het aantal van het begin is honderd procent.', H2,
   'Je kind rekent uit met hoeveel procent een aantal is gedaald.',
   [LT('verschil als procent', '20 procent', 'Dat is het verschil in aantal, nog geen procent. Hoeveel procent van het oude aantal is dat?', H2),
    LT('nieuwe aantal als basis', '40 procent', 'Zo vergelijk je met het nieuwe aantal. Bij een daling is het oude aantal honderd procent.', H2),
    ALG('Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?', H2)])

# ---- VBN-V01 #1: zet de stip op (#, #) in een rooster ----
H2 = 'Begin bij nul. Het getal vóór de komma zegt hoeveel stappen je opzij gaat, naar rechts. Het getal na de komma zegt hoeveel stappen je daarna omhoog gaat. Zet daar de stip.'
ST(V01, 1, 'Bij de stip horen twee getallen tussen haakjes. Welk getal hoort bij opzij, en welk bij omhoog?', H2,
   'Je kind zet een punt in een rooster met twee getallen tussen haakjes.',
   [CL('omgewisseld', None, 'Daar staan de twee getallen omgewisseld. Het getal vóór de komma gaat opzij, het getal na de komma omhoog.', H2,
       regel='Claudes sleutel: getallen omgewisseld'),
    ALG('Ga opzij zoveel als het getal vóór de komma. Ga dan omhoog zoveel als het getal na de komma.', H2)])
# ---- VBN-V01 #2 (013): lijngrafiek, wat gebeurt er tussen twee tijden, meerkeuze ----
H2 = 'Lees de temperatuur af bij de tijd waar het stuk begint en bij de tijd waar het stopt. Hoeveel graden is het verschil? Kijk ook of de lijn omhoog of omlaag gaat.'
ST(V01, 2, 'Zoek op de lijn de twee tijden uit de vraag. Gaat de lijn daartussen omhoog of omlaag?', H2,
   'Je kind leest in een lijngrafiek af hoe de temperatuur verandert.',
   [LT('omhoog in plaats van omlaag', 'De temperatuur stijgt met 3 graden', 'Kijk of de lijn tussen die twee tijden omhoog of omlaag gaat.', H2),
    LT('verschil van een ander stuk', 'De temperatuur daalt met 6 graden', 'Dat verschil hoort bij een ander stuk van de lijn. Lees de temperatuur af bij de twee tijden uit de vraag.', H2),
    ALG('Lees de temperatuur af bij de twee tijden uit de vraag. Gaat de lijn omhoog of omlaag?', H2)])
# ---- VBN-V01 #3 (014): cirkeldiagram, hoeveel kiezen voetbal, meerkeuze ----
H2 = 'Voetbal is de helft van de cirkel. Neem de helft van het aantal in de klas.'
ST(V01, 3, 'Welk deel van de cirkel hoort bij voetbal?', H2,
   'Je kind rekent met een cirkeldiagram uit hoeveel een deel van de klas is.',
   [LT('een kwart', '6 kinderen', 'Dat hoort bij een kwart van de klas. Voetbal is de helft: dat is meer dan een kwart.', H2),
    LT('drie gelijke stukken', '8 kinderen', 'Zo deel je de klas in drie gelijke stukken. Maar de stukken van de cirkel verschillen in grootte.', H2),
    ALG('Welk deel van de cirkel is voetbal? Neem dat deel van de hele klas.', H2)])
# ---- VBN-V01 #4 (015): as met stappen, precies tussen twee getallen, meerkeuze ----
H2 = 'Hoeveel is het van het kleinste getal tot het grootste? Neem daar de helft van. Tel die helft op bij het kleinste getal.'
ST(V01, 4, 'Precies tussen twee getallen ligt het getal in het midden.', H2,
   'Je kind leest op een as een getal af dat precies tussen twee streepjes ligt.',
   [LT('niet in het midden', '65', 'Dat ligt niet precies in het midden. Hoe groot is de stap van het kleinste getal naar het grootste? Neem daar de helft van.', H2),
    LT('opgeteld', '140', 'Dat zijn de twee getallen samen. Het getal dat je zoekt, ligt tussen die twee in.', H2),
    ALG('Welk getal ligt precies in het midden van de twee getallen?', H2)])
# ---- VBN-V01 #5 (016): staafdiagram, op welke dag de meeste boeken, meerkeuze ----
H2 = 'Vergelijk de staven: welke komt het hoogst? Lees af bij welke dag die staaf hoort.'
ST(V01, 5, 'Zoek de hoogste staaf.', H2,
   'Je kind leest in een staafdiagram af waar het meeste bij hoort.',
   [LT('niet de hoogste staaf', 'Maandag', 'Die staaf is niet de hoogste. Welke staaf komt het hoogst? Bij welke dag hoort die?', H2),
    LT('de laagste staaf', 'Dinsdag', 'Dat is de laagste staaf. De meeste boeken horen bij de hoogste staaf.', H2),
    ALG('Zoek de hoogste staaf. Bij welke dag hoort die?', H2)])
# ---------------- schrijven ----------------
def reden(t):
    if re.search(r'\d', t): return 'tekst met getallen uit het item; nu een vaste tekst zonder cijfers (regel nagerekend), met eigen laag 2'
    if re.match(r'Je (hebt|telde|bent|noemde|vergat|deelde|nam|zit|begon)\b', t): return 'zegt zeker wat het kind deed; nu een waardezin of een vraag (les 20/101/161), met eigen laag 2'
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
D = {'batch': 'batch9', 'geschreven': '2026-10-08',
     'uitleg': ("Hints per somtype (G8-merge, batch 9 = VERH-E05/VBN-V01: procent erbij, gestegen/gedaald, grafieken lezen). Formaat als g7/hints/batch*.json. Koppeling: nrOrigineel + somtypeOrigineel (regel 'Sleutel' in somtypen/<doel>.md); "
                "'nr' en 'somtype' houdt scripts/sync_hint_keys.py bij. foutHints: rekenregels uit scripts/fout_regels.py met een vaste tekst, laag 1 'tekst' "
                "en laag 2 'tekstSterker'; 'andere fout' als laatste."),
     'somtypen': S}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{OUT}: {len(S)} somtypes, {sum(len(s["foutHints"]) for s in S)} fout-hints, {sum(len(s.get("claudeVervangen", [])) for s in S)} claudeVervangen')
