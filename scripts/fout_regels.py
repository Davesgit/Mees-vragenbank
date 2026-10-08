#!/usr/bin/env python3
"""Past de fout-hintregels van Oefeningen (hints/batch*.json: soort → regel → tekst) per item toe.
Regels gelden van boven naar beneden; de eerste die past, wint. Gebruikt door apply_hints.py.
Nieuw 8 okt 12:4x (G7 batch 2, Oef-#421/#422/#429): norm421 = één notatie voor letterlijke regels en opties ('−'/'-'/'–' als minteken, 'euro'/'€');
  'de deelsom omgedraaid' = de deling met deeltal en deler omgewisseld (antwoord 'a : b' → optie 'b : a'; antwoord getal → b/a).
  Oef-#437: KOMMA437 (G7/G8) leest '8,4' als één getal; Oef-#436: 'fout = antwoord ± 0,1 / ± 0,01' ook bij een heel antwoord (vraag met kommagetal);
  Oef-#444: Claudes sleutels met '-' worden '−' en de labelregel vergelijkt genormaliseerd (G7/G8).
  Z-#616: 'fout = getal1/getal2' als bedrag bij een geldvraag (G7/G8). Z-#633: 'fout = de bodem (l × b)', zeker, vóór '± 1'.
  Z-#607: 'fout = decimaal-nul weggelaten' ('2' bij 2,0 als de vraag om cijfers achter de komma vraagt; 'Bijna!' mag).
  Oef-#453: 'fout = kommagetal met procentteken', 'fout = getallen achter elkaar (als %)'; #445-regels ook bij 'D/G' en tien keer zonder deel (alleen KOMMA437).
  Oef-#445: 'fout = het deel zelf (als %)' / 'fout = geheel min deel' (procent-vragen 'D van G', antwoord met '%').
  Oef-#442: 'fout = de som van de getallen' / 'fout = het middelste getal (op grootte)' (gemiddelde; alleen als de waarde zo uitkomt).
  Oef-#440: met KOMMA437 telt een antwoord '8,0' als 8, een sleutel '8,0' past op regelwaarde 8, en 'antwoord × 10 / : 10' werkt ook bij een kommagetal (1,1 → 11 / 0,11). Oef-#434: 'fout = het cijfer op de plek ernaast' (plaatswaarde: de cijfers links en rechts van de gevraagde plaats).
Per item komt er uit:
  foutHints   concrete sleutels (fout getal / optietekst / vak) met kindtekst, zoals het exportformaat ze kent
  foutRegels  de geordende regels met een matcher (waarden / kleinerDan / vanaf / totEnMet / alles) voor invoer
              die niet als sleutel voorkomt; 'alles' = algemene zin
Basis is extraVelden.claudeFoutHints (door build_g3.py gezet), dus opnieuw draaien geeft hetzelfde resultaat.
Regeltypes erbij (1 okt, fixlijst G4 / besluit Dave), te gebruiken in hints/batch*.json als 'regel':
  fout = antwoord ± getal1   (ook: + getal1, - getal1, ± getal2 …)  bv. één groepje te veel of te weinig
  fout = eenheden als antwoord  (= de eenheden van het antwoord; ook 'fout = de eenheden van het antwoord')
  fout = eenheden van getal1 / getal2,  fout = getal1 × getal2  (Didactiek review batch 1 punt 6)
Nieuw 1 okt 16:00 (merge-fixlijst #48): een 'claude-taalfix' met een onleesbare regel en een vaste tekst (zonder '…') zet die tekst op de
  Claude-sleutels (claudeDenkfout); teksten met [getal1], [getal2], [antwoord] (of {getal1} …) worden per item ingevuld (vul_in).
Nieuw 1 okt 15:51 (merge-fixlijst #38, #40–#42):
  fout = klok een uur te laat / fout = klok een uur te vroeg   zelfde minuten, uur + 1 / − 1 (ook half, kwart; klokkenrij via jsRender.klokken)
  fout = grote wijzer verkeerd                                 het uur klopt, de minuten niet
  fout = antwoord gedeeld door getal1                          staafdiagram: streepjes geteld ('Elk streepje is 2.')
  fout = een dag ernaast                                       kalender: datum ± 1 dag
  fout = het andere tiental/honderdtal naast getal1           afronden: het andere buurtiental/-honderdtal (G5 #12; 166 → 160 als 170 goed is;
                                                               ook 'fout = het andere buurtiental' / 'het andere buurhonderdtal')
  fout = gestopt op de laatste dag van de maand               kalender: de laatste dag van de vroegste maand (#49, 1 okt 16:31)
  fout = gestopt op de eerste dag van de maand                kalender: de 1e van de latere maand (#49)
  fout = gestopt bij de laatste of eerste dag van de maand     (oud, blijft werken) beide datums
  fout = andere cel · fout = som van de rij · fout = som van de kolom · fout = som van twee cellen · fout = verschil van twee cellen
                                                               tabel (jsRender.rijen)
Nieuw 1 okt 17:00 (G5 merge-punten #29, #32, #33; Didactiek batch 2):
  fout = antwoord × 10 / fout = antwoord : 10          hele getallen: exact (nul te veel / nul vergeten); ': 10' alleen als het antwoord op 0
                                                      eindigt. Vanaf 10.000 beide vormen als sleutel (met en zonder punt, huisregel).
                                                      Bij een geldantwoord: het bedrag × 10 / : 10 (komma verschoven).
  fout = antwoord + 1 cent / - 1 cent / ± 1 cent       geld (#32, #19): bedrag in centen; ook 10 cent, €1 ('fout = antwoord ± €1').
  fout = antwoord + 10 cent / - 10 cent / ± 10 cent
  #35 (17:05): een regel met [getal1]/[getal2]/[antwoord] in de tekst voegt zijn sleutels toe, en op 'andere fout' wordt de ingevulde tekst de
  algemeneFoutHint (eerder None).
  Geldinvoer (#33): een geldsleutel raakt ook dezelfde invoer met of zonder €, met spaties, met of zonder ',00' en '8,8' voor '8,80'
  (geld_norm / _cent). '8.80' (punt) is GEEN geldbedrag: daar hoort een eigen tekst bij ('Bij geld schrijf je een komma.', zie
  GELD_PUNT = True, #33) / README). De app normaliseert de invoer op dezelfde manier vóór het opzoeken van de sleutel.
Nieuw 1 okt 17:45 (G5 fixlijst #60, #62, #64; Didactiek review batch 4 en recheck 2c/1d/3b):
  getallen met een punt als duizendtal-scheider ('10.000') zijn één getal (_int, _nums); elke sleutel van 5 of meer cijfers staat in
  beide vormen ('10000' en '10.000'). De app moet allebei accepteren (of de invoer normaliseren: punt tussen groepjes van 3 weg).
  fout = getal1 afgerond op tientallen     afronden op honderdtallen, maar op tientallen gedaan (alleen als ≠ getal1 en ≠ antwoord) (#64)
  fout = één streepje ernaast              maatbeker (jsRender): antwoord ± perstreep, binnen 0–max (#62)
  fout = streepjes als 1 geteld            maatbeker: het getal eronder + het aantal streepjes als losse ml (700 bij 100 per streep → 502) (#62)
Nieuw 1 okt 17:58 (G5 fixlijst #68–#72):
  kloktijd in woorden wordt gelezen: 'vijf over 5', 'tien voor half 11', 'vijf over half acht' (uur als cijfer of woord) (#68)
  na 12 uur (antwoord 13:00 of later): de klokregels geven sleutels in 24 uur ('14:05') en raken ook de 12-uursvorm (#69)
  fout = klok een minuut / vijf minuten / tien minuten / een kwartier te laat (of te vroeg)    met richting (#70)
  fout = een dag later / fout = een dag eerder                kalender ± 1 dag apart (#70)
  fout = datum later dan het antwoord / fout = datum eerder dan het antwoord   elke latere/eerdere datum (ook 'een latere datum') (#70)
  fout = over en voor verwisseld     minuten 60 − m; bij ≤ 15 min het uur ervoor, bij ≥ 45 min het uur erna (tien voor 2 ↔ tien over 2) (#72)
  #71: een Claude-regel (onleesbaar, claudeDenkfout) raakt ook een per item hersplitste denkfout (denkfoutClaude = dat label), zolang de
  entry nog geen eigen regel voor het nieuwe label heeft.
Nieuw 1 okt 18:20 (G5 fixlijst #76, #77, #81, #82; batch 6):
  fout = een andere staaf          staafdiagram: de waarde van elke andere staaf (jsRender.staven) (#76)
  fout = het getal onder de top     staafdiagram: het antwoord naar beneden afgerond op cijfer_om, als dat ≠ antwoord (#76)
  fout = een kwart / de helft / drie kwart van getal1    per item uitgerekend, alleen als het een heel getal is (#77)
  fout = het aantal munten          geld tellen: het aantal munten en briefjes als euro's (len(jsRender.munten)) (#81)
  #82: valt een sleutel bij een tabel (jsRender.rijen) onder meer dan één regel, dan gaat de precieze regel voor: de regel met de
  kleinste set sleutels; bij gelijke grootte de volgorde in de entry. De andere regels staan in foutHints[].ookRegels.
  #92 (1 okt 18:45, Didactiek batch 6 V4): bij een tabel eerst treden: cel → som van de gevraagde rij → som van de gevraagde kolom →
  twee cellen/rij min één/Claudes sleutels → som van een andere rij of kolom → andere fout; #82 alleen binnen een trede.
  #93: 'fout = het getal vlak onder de top' (ook 'net onder de top') = 'het getal onder de top' (alleen als de top niet op een getal staat).
  #94: staafdiagram: is de sleutel de waarde van een staaf uit de vraag, dan gaan de staafregels vóór de rest (zeker vóór onzeker).
Nieuw 1 okt 19:05 (G5 fixlijst #103, #104; Didactiek recheck 4c/5b):
  fout = grote wijzer als uur gelezen   een heel uur met als uur de minuten : 5 (12 bij 0): 'vijf over 4' → '1 uur', 'tien over half 7' → '8 uur',
                                        klokkenrij tien over → de klok 2:00 (#103). Geen sleutel als de minuten geen veelvoud van 5 zijn.
  '(24 uur)' / '(12 uur)' achter een klokregel: de regel geldt alleen bij items met (zonder) een tijd van 13:00 of later (#104a).
  #104b: een klokregel die bij een digitaal antwoord vóór 13:00 (12:55) op 13:00 of later uitkomt, geeft bij een open vraag met een
  digitale tijd in de opgave beide vormen ('13:05' en '1:05'). De drempel kijkt naar de sleutel, niet naar het antwoord.
Nieuw 1 okt 19:10 (G5 fixlijst #106, Oefeningen 19:06):
  fout = de prijs     geld: elk bedrag in de opgave dat iets kost (niet 'betaalt met €…' of 'hebt €…'), ≠ antwoord. Gaat in de volgorde
                      vóór 'antwoord ± 10 cent' en '± €1' (zeker vóór onzeker), ook als de entry hem later zet; de andere staan in ookRegels.
Nieuw 1 okt 20:05 (G6 merge-fixlijst #1, #4, #6; besluiten Dave 19:58):
  fout = het andere duizendtal naast getal1 / het andere tienduizendtal naast getal1   afronden op duizend- of tienduizendtallen: het
                                      buurduizendtal aan de andere kant (stap uit de regel; bij 'tiental/honderdtal' uit de opgave, nu ook
                                      'duizendtal'/'tienduizendtal'). Zet hem in de entry vóór 'antwoord ± 1000' / '± 10.000' (#1).
  fout = getal1 afgerond op honderdtallen / duizendtallen (en tientallen, #64)   op de verkeerde eenheid afgerond (alleen als ≠ getal1 en ≠ antwoord)
  fout = getal2 + 1 / getal2 - 1 / getal2 ± 1 (ook getal1)   het kind deed er één bij of af in plaats van honderd of duizend (#6). Gebruik de
                                      richting die bij de denkfout past ('meer dan' → + 1, 'minder dan' → − 1).
  Kommagetal-antwoorden (#4; Nederlandse komma, vormen zoals de VORM-regel #105: punt = komma, slot-nullen weg):
  fout = antwoord ± 0,1 (ook + / −, en 0,01 …)       één tiende (honderdste) ernaast; sleutel '1,3' / '1,5', invoer '1.3' en '1,30' raken hem ook
  fout = het hele getal van het kommagetal          1 bij 1,4 (ook 0 bij 0,7)
  fout = de tienden als heel getal                  4 bij 1,4 (75 bij 0,75); niet als dat gelijk is aan het hele getal
  fout = de cijfers om de komma omgedraaid          4,1 bij 1,4 (alleen één cijfer voor en achter de komma; niet als het al een andere sleutel is)
  Bij een antwoord zonder komma geven deze vier regels geen sleutel.
G6 fixlijst #154: fout = getal2 ± getal1 × 10 / getal1 : 10 / getal1 × 100 (op de verkeerde plek). #153: geen sleutel buiten visual.getallenlijn [van, tot].
G6 fixlijst ronde 7 (Didactiek 2c/batch 4/3b, 22:13–22:14): #210 'eenheden niet keer gedaan' (#198) en 'cijfers opgeteld' (#190) slaan een waarde over als
  antwoord − waarde een deelproduct is (deelproducten); #215 fout = getal1 keer/gedeeld door het aantal nullen van de factor (100/1000; tekst met [nullen],
  [factor], [Factor]); #205 fout = één stuk (het aantal : de noemer); #206 fout = de factor (nieuwe noemer : oude noemer); #207 fout = de rest van getal1 : getal2
  en fout = getal1 − j × getal2 (j ≥ 2); #216 '(antwoord vanaf N)' / '(antwoord onder N)' achter een regel; #223 ANTWOORD_UIT_WAARDEN (G6).
G5 fixlijst #121 (Dave 20:04): bij een tabel (jsRender soort 'tabel', VBN-E01) haalt de motor het goede antwoord uit de waarden van elke regel
  (assert); die regels namen de goede rij of cel mee."""
import re, difflib

BEREIK_AFRONDEN = None     # G5: 1000 (merge-fixlijst #1/#13), gezet in scripts/apply_hints.py
GELD_PUNT = False          # G5: True (merge-punt #33), gezet in scripts/apply_hints.py
KOLOM_VOOR_DEEL = False    # G5: True (merge-fixlijst #124), gezet in scripts/apply_hints.py: bij 'Hoeveel X in totaal?' wint een kolomsom van 'twee cellen'/Claudes sleutel
GELD_PUNT_TEKST = 'Bij geld schrijf je een komma.'
ANTWOORD_UIT_WAARDEN = False   # G6: True (merge-fixlijst #223, Didactiek 3b): het goede antwoord nooit in foutRegels.match.waarden, ook buiten tabellen (assert)
KOMMA437 = False           # Oef-#437: kommagetal in de vraag als één getal; True in G7/G8 (apply_hints); G5/G6 blijven gelijk (goedgekeurd)
NEG494 = False             # Oef-#494 (G8 batch 5, MEET-E05): getallen onder nul ('−9', '-9') lezen; True in G7/G8 (apply_hints); G5/G6 blijven gelijk
LIJN_BINNEN = False        # G5: True (merge-fixlijst #14: geen sleutel buiten de getallenlijn), gezet in scripts/apply_hints.py; G4 ongewijzigd

def _int(v):
    """Geheel getal; ook met punt als duizendtal-scheider ('10.000' → 10000, G5 fixlijst #60). Geen kommagetal."""
    v = str(v).strip()
    if re.fullmatch(r'\d{1,3}(?:\.\d{3})+', v): return int(v.replace('.', ''))
    return int(v) if re.fullmatch(r'\d+', v) else None

from fractions import Fraction
def _dec(v):
    """#4 (G6): kommagetal → Fraction, zoals de VORM-regel (#105): komma of punt als decimaalteken, slot-nullen tellen niet ('1,40' = '1.4' = '1,4').
    Hele getallen ook ('8' → 8). Geen duizendtal-punt bij kommagetallen. None als het geen getal is."""
    t = str(v).strip().replace(' ', '')
    if re.fullmatch(r'\d+(?:[.,]\d+)?', t): return Fraction(t.replace(',', '.'))
    return None
def _kg(x):
    """Fraction → huisvorm met Nederlandse komma, zonder slot-nullen ('1,3', '2', '0,05')."""
    if x.denominator == 1: return str(x.numerator)
    for k in range(1, 7):
        if (x * 10 ** k).denominator == 1:
            q = x * 10 ** k; s_ = str(q.numerator).rjust(k + 1, '0'); return f"{s_[:-k]},{s_[-k:]}"
    return None
def _vormen(v):
    """G5 fixlijst #60: een sleutel van 5 of meer cijfers in beide vormen ('10000' en '10.000'); de app accepteert allebei."""
    n = _int(v)
    return list(dict.fromkeys([str(v)] + _punt(n))) if n is not None and n >= 10000 else [str(v)]

def _cent(v):
    """Geldbedrag → centen (#19/#33): '€21,95', '€ 21,95', '21,95', '€3', '3', '€3,00', '8,8' → 2195 / 300 / 880. Geen punt als komma
    ('8.80' → None); een punt als duizendtal-scheider alleen in de vorm 1.250,00. None als het geen bedrag is."""
    v = str(v).strip().replace('\u00a0', ' ')
    m = re.fullmatch(r'€?\s*(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d{1,2}))?(?:\s*euro)?', v, re.I)      # ook '4,75 euro' (normalisatie 'euro', 8 okt)
    if not m: return None
    e = int(m.group(1).replace('.', '')); c = m.group(2)
    return e * 100 + (int(c.ljust(2, '0')) if c else 0)

def geld(cent):
    """Centen → huisnotatie: €4 · €8,80 · €1.250,50 (geen ',00', komma, punt vanaf 1000 euro alleen bij 5+ cijfers volgens huisregel)."""
    e, c = divmod(int(cent), 100)
    es = f'{e:,}'.replace(',', '.') if e >= 10000 else str(e)
    return f'€{es}' if c == 0 else f'€{es},{c:02d}'

def geld_norm(v):
    """#33: genormaliseerde geldsleutel ('8,80' / '€ 8,8' / '€8,80' → '€8,80'; '€4,00' → '€4'); None als het geen bedrag is."""
    k = _cent(v); return geld(k) if k is not None else None

def _punt(x):
    """Huisregel: vanaf 10.000 met punt (beide vormen zijn sleutel)."""
    return [str(x)] + ([f'{x:,}'.replace(',', '.')] if x >= 10000 else [])

def _nums(t):
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', t)
    # G5 fixlijst #60: '10.000' is één getal (punt als duizendtal-scheider), niet 10 en 0
    # Oef-#437 (G7 batch 3): een decimale komma tussen cijfers is één getal ('8,4' → 42/5, als Fraction), niet 8 en 4. Een komma met een spatie
    # erachter blijft een opsommingsteken ('8, 4'); een rij zonder spaties ('3,5,7') blijft drie hele getallen.
    INT = r'(?:\d{1,3}(?:\.\d{3})+|\d+)'
    if not KOMMA437: return [int(x.replace('.', '')) for x in re.findall(r'(?<![\w:.])' + INT + r'(?![\w:]|\.\d)', t)]      # zoals vóór #437
    uit = []
    for m in re.finditer(r'(?<![\w:.,])(' + INT + r',\d+)(?!,\d)(?![\w:]|\.\d)|(?<![\w:.])(' + INT + r')(?![\w:]|\.\d)', t):
        if m.group(1):
            n_, _, d_ = m.group(1).partition(','); x = Fraction(int(n_.replace('.', ''))) + Fraction(int(d_), 10 ** len(d_))
            uit.append(int(x) if x.denominator == 1 else x)
        else: uit.append(int(m.group(2).replace('.', '')))
    return uit

def _uur(v):
    m = re.fullmatch(r'(\d+)(?: uur|:00)', str(v).strip())
    return int(m.group(1)) if m else None

def _wrap(h): return (h - 1) % 12 + 1

def _tijd(v, c):
    """(uur 1–12, minuut) uit een kloklabel (klokkenrij), 'h:mm', 'h uur', 'half h', 'kwart over h' of 'kwart voor h'."""
    v = str(v).strip(); jr = c.jr
    if jr.get('soort') == 'klokkenrij' and v in (jr.get('labels') or []):
        k = jr['klokken'][jr['labels'].index(v)]; return (_wrap(k['uur']), k['minuut'])
    if m := re.fullmatch(r'(\d{1,2}):(\d{2})', v): return (_wrap(int(m.group(1))), int(m.group(2)))
    if m := re.fullmatch(r'(\d{1,2}) uur', v): return (_wrap(int(m.group(1))), 0)
    if m := re.fullmatch(r'half (\d{1,2})', v): return (_wrap(int(m.group(1)) - 1), 30)
    if m := re.fullmatch(r'kwart over (\d{1,2})', v): return (_wrap(int(m.group(1))), 15)
    if m := re.fullmatch(r'kwart voor (\d{1,2})', v): return (_wrap(int(m.group(1)) - 1), 45)
    # G5 fixlijst #68: 'vijf over 5', 'tien voor 5', 'vijf over half 7', 'tien voor half 11' (ook met uurwoord: 'vijf over vijf')
    if m := re.fullmatch(r'(vijf|tien) (over|voor) (half )?(\d{1,2}|' + '|'.join(UUR_NUM) + r')', v):
        h = int(m.group(4)) if m.group(4).isdigit() else UUR_NUM[m.group(4)]; d = 5 if m.group(1) == 'vijf' else 10
        basis = (h - 1) * 60 + 30 if m.group(3) else h * 60          # minuten vanaf 0:00 (12-uursklok)
        t = basis + (d if m.group(2) == 'over' else -d)
        return (_wrap((t // 60) % 12), t % 60)
    return None

def _t24(v):
    """G5 fixlijst #69: 'hh:mm' met een uur van 13 of later → minuten vanaf 0:00 (24 uur); anders None."""
    m = re.fullmatch(r'(\d{1,2}):(\d{2})', str(v).strip())
    return int(m.group(1)) * 60 + int(m.group(2)) if m and 13 <= int(m.group(1)) <= 23 else None

def _schuif(ans, ta, delta, c=None):
    """(exacte sleutels, doeltijd 12 uur) voor 'antwoord + delta minuten'. Digitaal antwoord: sleutel 'h:mm'; boven 12 uur in 24 uur (#69).
    #104b (Didactiek 18:54): de drempel kijkt naar de SLEUTEL, niet naar het antwoord. Komt een sleutel van een digitaal antwoord vóór 13:00
    (12:55 + 10 min) op 13:00 of later uit, en is het een open vraag met een digitale tijd in de opgave (een reis), dan krijgt hij de
    24-uursvorm ('13:05') én de 12-uursvorm ('1:05'). De pred raakt altijd beide vormen."""
    t = ((ta[0] % 12) * 60 + ta[1] + delta) % 720; doel_t = (_wrap(t // 60), t % 60)
    t24 = _t24(ans); ex = set()
    if t24 is not None: x = (t24 + delta) % 1440; ex = {f'{x // 60}:{x % 60:02d}'}
    elif m := re.fullmatch(r'(\d{1,2}):(\d{2})', str(ans).strip()):
        ex = {f'{doel_t[0]}:{doel_t[1]:02d}'}
        x = int(m.group(1)) * 60 + int(m.group(2)) + delta
        if c is not None and 13 * 60 <= x < 24 * 60 and not c.it.get('opties') and re.search(r'\b\d{1,2}:\d{2}\b', c.opg):
            ex.add(f'{x // 60}:{x % 60:02d}')
    return ex, doel_t

def _is24(c):
    """#104a: het item vraagt naar een tijd van 13:00 of later (antwoord of digitale tijd in de opgave)."""
    if _t24(c.ans) is not None: return True
    return any(13 <= int(h) <= 23 for h in re.findall(r'\b(\d{1,2}):\d{2}\b', c.opg))

UUR_NUM = {'één': 1, 'een': 1, 'twee': 2, 'drie': 3, 'vier': 4, 'vijf': 5, 'zes': 6, 'zeven': 7, 'acht': 8, 'negen': 9, 'tien': 10, 'elf': 11, 'twaalf': 12}
MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
DAGEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def _datum(v):
    m = re.fullmatch(r'(\d{1,2}) ([a-z]+)', str(v).strip())
    return (int(m.group(1)), MAANDEN.index(m.group(2))) if m and m.group(2) in MAANDEN else None
def _dag_erbij(d, k):
    dag, mi = d; dag += k
    while dag > DAGEN[mi]: dag -= DAGEN[mi]; mi = (mi + 1) % 12
    while dag < 1: mi = (mi - 1) % 12; dag += DAGEN[mi]
    return f'{dag} {MAANDEN[mi]}'

_SINT494 = re.compile(r'\s*([−\-–])?\s?(\d+)(?:\s?°C|\s+graden)?\s*')
def _sint494(v):
    """Oef-#494: geheel getal met teken ('−9', '-9', '−9 °C', '9') → int; None als het geen (geheel) getal is."""
    m = _SINT494.fullmatch(str(v)) if v is not None else None
    if not m: return None
    return -int(m.group(2)) if m.group(1) else int(m.group(2))
def _sfmt494(x):
    """huisnotatie: −9 (min-teken U+2212), 9"""
    return f'−{-x}' if x < 0 else str(x)
def _snums494(t):
    """Oef-#494: de hele getallen uit de vraag mét teken. Een minteken telt alleen als teken als het direct vóór het getal staat
    (geen spatie ertussen) en er geen cijfer vlak voor staat ('Het is −3 °C' → −3; '8 − 3' blijft 8 en 3)."""
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', t)
    uit = []
    for m in re.finditer(r'(?<![\w:.,])((?<![\d\s])[−\-–]|(?<=\s)[−\-–]|^[−\-–])?(\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|[.,]\d)', t):
        x = int(m.group(2).replace('.', ''))
        uit.append(-x if m.group(1) else x)
    return uit
def _neg_vormen494(w):
    """'−9' → ['−9', '-9'] (beide mintekens zijn een sleutel)"""
    w = str(w); return [w, '-' + w[1:]] if w.startswith('−') else [w]

class Ctx:
    def __init__(self, it):
        self.it = it; self.opg = (it['opgave'] or '').replace('\n', ' ')
        self.nums = _nums(self.opg); self.ans = str(it['antwoord']); self.a = _int(self.ans)
        self.jr = it['visual']['jsRender'] or {}
        self.g1 = self.nums[0] if self.nums else None; self.g2 = self.nums[1] if len(self.nums) > 1 else None
        self.ac = _cent(self.ans) if self.ans.startswith('€') else None      # geldantwoord in centen (#19/#32/#33)
        self.d = _dec(self.ans) if re.fullmatch(r'\d+,\d+', self.ans.strip()) else None    # G6 #4: kommagetal-antwoord (alleen met komma)
        # G6 merge-fixlijst ronde 8 (Oefeningen, G5 batch 7 twijfel 6): een antwoord met een eenheid ('230 bezoekers', '18 glazen', '10 L').
        # Het getal telt als antwoord; de motor zet de eenheid weer achter elke waarde (zie compile_regel). Geld (€) en kommagetallen niet.
        self.eenheid = None
        if self.a is None and (q := re.fullmatch(r'(\d+) ([A-Za-zà-ÿ²³]+(?: [a-zà-ÿ]+)?)', self.ans.strip())):
            self.a = int(q.group(1)); self.eenheid = q.group(2)
        # Oef-#440 (G7 MEET-03 #9, met KOMMA437): een antwoord '8,0' / '300,0' heeft de waarde van het hele getal (8 / 300); regels als
        # 'fout = antwoord × 10' lezen het dan (sleutel '80'). G5/G6 (zonder KOMMA437) blijven gelijk.
        if KOMMA437 and self.a is None and (q := re.fullmatch(r'(\d+),0+', self.ans.strip())): self.a = int(q.group(1))
        # Oef-#494 (G7/G8, met NEG494): een item met een getal onder nul (in het antwoord of in de vraag) rekent met teken: het antwoord en
        # de vraaggetallen zijn dan '−9' / −3. Andere items blijven precies zoals ze waren.
        self.an = _sint494(self.ans) if NEG494 else None
        self.neg = False
        if NEG494:
            sn = _snums494(self.opg)
            self.neg = (self.an is not None and self.an < 0) or any(x < 0 for x in sn)
            if self.neg:
                if self.a is None and self.an is not None: self.a = self.an
                # getal1/getal2 blijven zonder teken (zoals vóór #494: 'fout = getal1 − getal2' is juist de route 'teken genegeerd'); de getallen onder nul
                # komen erbij als vraaggetal ('−4' is ook een getal uit de vraag). De routes met teken staan in de #494-regels (start = eerste getal mét teken).
                self.nums = list(dict.fromkeys(self.nums + [x for x in sn if x < 0]))
    def code(self, v):
        v = str(v)
        if re.fullmatch(r'[A-L][1-9]', v): return v
        for d in self.jr.get('dingen', []):
            if d['wat'] == v: return d['vak']
        return None

def _delen(x):
    """plaatswaarde-delen van een heel getal: 485 → [400, 80, 5] (nullen weg)."""
    t = str(x); return [int(c) * 10 ** (len(t) - 1 - i) for i, c in enumerate(t) if c != '0']
def deelproducten(g1, g2):
    """G6 merge-fixlijst #210 (Didactiek 2c): alle deelproducten van g1 × g2 bij splitsen: elk deel × elk deel, en een heel getal × een deel van het andere."""
    if g1 is None or g2 is None: return set()
    d1, d2 = _delen(g1), _delen(g2)
    return {p * q for p in d1 for q in d2} | {g1 * q for q in d2} | {p * g2 for p in d1}
NUL_WOORD = {2: 'twee', 3: 'drie'}; FACTOR_WOORD = {100: 'honderd', 1000: 'duizend'}
def _factor215(c):
    """#215: omrekenen met 100 of 1000: (factor, keer?) uit getal1 en het antwoord, anders None."""
    if c.g1 is None or c.a is None: return None
    for f in (100, 1000):
        if c.a == c.g1 * f: return (f, True)
        if c.a * f == c.g1: return (f, False)
    return None

def _breuk(v):
    from fractions import Fraction
    v = str(v).strip(); m = re.fullmatch(r'(?:(\d+) )?(\d+)/(\d+)', v)
    if not m or int(m.group(3)) == 0: return None
    return int(m.group(1) or 0) + Fraction(int(m.group(2)), int(m.group(3)))

def _lijn219(r, c):
    """G6 merge-fixlijst #219 (Oefeningen batch 5, Dave 22:39): regels bij een lijngrafiek (VBN-E02). Gegevens uit visual.jsRender:
    punten [{naam, waarde}], perstreep (waarde van één streepje) en cijfer_om (om de hoeveel er een getal langs de zijkant staat).
    De genoemde maanden staan in de volgorde van de vraag. None = geen lijngrafiekregel (de gewone regels gaan verder)."""
    jr = c.jr; pts = [(str(q.get('naam', '')).lower(), q.get('waarde')) for q in jr.get('punten') or [] if isinstance(q, dict) and isinstance(q.get('waarde'), int)]
    ps = jr.get('perstreep') if isinstance(jr.get('perstreep'), int) else None; co = jr.get('cijfer_om') if isinstance(jr.get('cijfer_om'), int) else None
    o = c.opg.lower(); genoemd = sorted((o.find(n), n, w) for n, w in pts if n and re.search(rf'\b{re.escape(n)}\b', o))
    W = lambda *v: {'exact': {str(x) for x in v if isinstance(x, int) and x >= 0}}
    if r.startswith('fout = de tweede maand uit de vraag'):      # #276: de latere maand in de tijd (de vraag noemt die nu eerst: 'in april meer dan in maart')
        if len(genoemd) < 2: return {'exact': set()}
        volg = [n for n, _ in pts]; return W(max(genoemd, key=lambda g: volg.index(g[1]))[2])
    if r.startswith('fout = de andere maand uit de vraag'):      # #333 (Didactiek r8 V-#330): de vroegere maand in de tijd (het kleinste aantal uit de vraag)
        if len(genoemd) < 2: return {'exact': set()}
        volg = [n for n, _ in pts]; return W(min(genoemd, key=lambda g: volg.index(g[1]))[2])
    if r.startswith('fout = de som van een deel van de maanden'):      # #333 (Didactiek r8): VBN-E02 #3, een paar maanden opgeteld (2 t/m n−2 maanden)
        from itertools import combinations
        ws = [w for _, w in pts]; return W(*{sum(cb) for k in range(2, len(ws) - 1) for cb in combinations(ws, k)})
    if r.startswith('fout = de waarde van één maand'): return W(*{w for _, w in pts})      # #274 (Didactiek batch 5): VBN-E02 #3
    if r.startswith('fout = een andere maand'):
        if len(genoemd) != 1: return {'exact': set()}
        return W(*[w for n, w in pts if n != genoemd[0][1]])
    if r.startswith('fout = het getal onder de stip'):
        if len(genoemd) != 1 or not co: return {'exact': set()}
        w = genoemd[0][2]; x = (w // co) * co
        return W(x) if x != w else {'exact': set()}
    if r.startswith('fout = het getal net boven de stip'):      # #275c (Didactiek batch 5): het getal langs de zijkant net boven de stip
        if len(genoemd) != 1 or not co: return {'exact': set()}
        w = genoemd[0][2]; x = -(-w // co) * co
        return W(x) if x != w else {'exact': set()}
    if r.startswith('fout = alle maanden samen min één maand') or r.startswith('fout = alle maanden samen plus één maand'):
        tot = sum(w for _, w in pts); plus = 'plus' in r
        return W(*[tot + w if plus else tot - w for _, w in pts])
    m = re.match(r'fout = antwoord (:|\+|-) perstreep', r)
    if m:
        if not ps or c.a is None: return {'exact': set()}
        if m.group(1) == ':': return W(c.a // ps) if ps > 1 and c.a % ps == 0 else {'exact': set()}
        return W(c.a + ps if m.group(1) == '+' else c.a - ps)
    return None

def compile_regel(regel, c):
    """Zie _compile_regel. G6 ronde 8: bij een antwoord met een eenheid krijgt elke hele-getalwaarde die eenheid erachter ('220' → '220 bezoekers');
    de kale vorm blijft ook staan (een kind kan de eenheid weglaten)."""
    res = _compile_regel(regel, c)
    if res and getattr(c, 'eenheid', None) and res.get('exact'):
        res = dict(res); res['exact'] = set(res['exact']) | {f'{v} {c.eenheid}' for v in res['exact'] if re.fullmatch(r'\d+', str(v))}
    return res

_PM1_390 = re.compile(r'^fout = (?:het )?antwoord ?(?:±|\+|-|−) ?1(?![\d,])(?! ?cent)')
def is_pm1_390(f):
    """G6 merge-fixlijst #390 (Didactiek gate ronde 9 deel B, les 115): een ±1-regel (fout = antwoord ± 1, + 1, − 1) of een tekst met 'Bijna!'."""
    r = (f.get('regel') or '').lower().replace('−', '-').replace('\u2013', '-').strip()
    return bool(_PM1_390.match(r)) or (f.get('tekst') or '').lstrip().startswith('Bijna')
from fractions import Fraction as _F416
_GETAL416 = r'(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?(?:/\d+)?'
def waarde416(v):
    """D-#416: de waarde van een sleutel (heel getal, kommagetal of breuk; n/n = 1); een eenheid erachter mag. None als het geen getal is.
    #530 (eindcheck G5 r11): ook bedragen: '€4,75', '€ 4,75' en '4,75' hebben dezelfde waarde (vóór #530 sloeg dit '€' over)."""
    v = str(v or '').strip().replace('\u00a0', ' ')
    v = re.sub(r'^€\s*', '', v)
    m = re.fullmatch(r'(' + _GETAL416 + r')(?:\s+[a-zA-Z]+)?', v)
    if not m: return None
    t = m.group(1); n, _, d = t.partition('/'); n = _F416(n.replace('.', '').replace(',', '.'))
    return n / int(d) if d else n
def vraag_waarden416(opg, los=True):
    """D-#416: alle getallen uit de vraag als waarde (ook kommagetallen en breuken), plus de losse hele getallen zoals vroeger.
    #530: los=False zonder die losse hele getallen (voor een bedrag: €4 is niet de 4 uit '€4,75')."""
    t = re.sub(r'(?<!\d)\d{1,2}:\d{2}(?!\d)', ' ', (opg or '').replace('\n', ' '))
    w = {waarde416(x) for x in re.findall(r'(?<![\w:.,/])' + _GETAL416 + r'(?![\w:/]|[.,]\d)', t)}
    if los and KOMMA437:      # Oef-#490 (G7/G8): de losse hele getallen met dezelfde kommalogica als KOMMA437: '14' en '84' uit '14,84' tellen niet als vraaggetal
        w |= {_F416(int(x.replace('.', ''))) for x in re.findall(r'(?<![\w:.,])(?:\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|[.,]\d)', t)}
    elif los: w |= {_F416(int(x.replace('.', ''))) for x in re.findall(r'(?<![\w:.])(?:\d{1,3}(?:\.\d{3})+|\d+)(?![\w:]|\.\d)', t)}
    return {x for x in w if x is not None}
def in_vraag390(v, c):
    """#390/D-#416: is de sleutel op waarde gelijk aan een getal uit de vraag (ook breuken en kommagetallen: 2/2 = 1)? Dan valt hij terug op 'getal uit de vraag'
    (of een andere benoemde regel)."""
    x = waarde416(v)
    if x is not None and str(v).strip().startswith('€'): return x in vraag_waarden416(c.opg, los=False)      # #530: bedrag op waarde
    return x is not None and (x in vraag_waarden416(c.opg) or (x.denominator == 1 and int(x) in set(c.nums)))
_RX607 = re.compile(r'\b[Rr]ond\w*\b.*?\bop (?:één|een|twee|drie|1|2|3) cijfers? achter de komma')
def d607(c):
    """Z-#607: de vormen met minder slotnullen en dezelfde waarde, als de vraag om cijfers achter de komma vraagt ('2,0' → {'2'}; '3,50' → {'3,5'}; '4,00' → {'4', '4,0'})."""
    a = str(c.ans).strip()
    m = re.fullmatch(r'(\d+),(\d*?)(0+)', a)
    if not m or not _RX607.search(c.opg or ''): return set()
    heel, vast, nul = m.groups()
    return {(f'{heel},{vast}{nul[:k]}' if vast or k else heel) for k in range(len(nul))}
def norm421(t, geld=True):
    """Oef-#421/#422 (8 okt): één notatie voor de hele motor. Minteken: '–' (en-streep) en '-' tussen getallen of spaties → '−';
    geld: '4,75 euro' / '3 euro' → '€4,75' / '€3' en '€ 3' → '€3'. Woorden met een streepje ('rood-wit') blijven zoals ze zijn."""
    t = str(t or '').replace('\u00a0', ' ').replace('\u2013', '−')
    t = re.sub(r'(?<=[\d\s)])-(?=[\s\d(])', '−', t)
    if not geld: return t      # een regel zonder '€' ('16') leest '16 euro' zoals vroeger: alleen het minteken gelijk
    t = re.sub(r'(?<![\w,.])(\d+(?:,\d{1,2})?)\s?euro\b', r'€\1', t, flags=re.I)
    return re.sub(r'€\s+(?=\d)', '€', t)
def lett_past(r, v):
    """G6 merge-fixlijst #380: past de letterlijke regel r (kleine letters) op de optietekst v? '€…' exact; met een cijfer: het hele getal
    met een woordgrens ('4 hokjes' niet in '14 hokjes' of '4,5 hokjes'); zonder cijfer: een stukje tekst."""
    r = norm421(r).lower(); v = norm421(v, geld=r.startswith('€')).lower()      # Oef-#421/#422 (geld alleen als de regel een bedrag is)
    if r.startswith('€'): return v == r
    if re.search(r'\d', r): return _lett_tok(r, v)
    return r in v
LETT_VOOR, LETT_NA = r'(?<![\w,.€/\-−–])', r'(?![\w/]|[,.]\d)'      # #411: ook geen minteken ervoor ('4 hokjes' nooit in '−4 hokjes')
def _lett_tok(r, v):
    """#411/#506: de letterlijke regel r als één token in v: geen letter, cijfer, komma, punt, €, / of minteken ervoor (ook niet een minteken
    met een spatie: '− 4 hokjes' is een aftreksom) en geen letter, cijfer, / of decimaal erachter. Vergelijking én guard gebruiken dit."""
    for m in re.finditer(re.escape(r), v):
        voor = v[:m.start()]
        if re.search(LETT_VOOR + r'$', voor) is None or re.search(r'[\-−–]\s+$', voor): continue
        if re.match(LETT_NA, v[m.end():]) is None: continue
        return True
    return False
def lett_guard(r, v):
    """#380/#411/#506-guard: dezelfde tokenisering als lett_past (niet strenger: '1/4' op '1/4', '10.000' op '10.000' en 'a4' op 'a4' passen). Assert in pas_toe."""
    r = norm421(r).lower(); v = norm421(v, geld=r.startswith('€')).lower()      # Oef-#421/#422 (geld alleen als de regel een bedrag is)
    if r.startswith('€'): return v == r
    return _lett_tok(r, v) if re.search(r'\d', r) else r in v
_HELFT_STROOK = re.compile(r'strook van (\d+) hokjes')
def _regels_r10(r, c):
    """G6 merge-fixlijst ronde 10 (#380): 'fout = de helft van het aantal hokjes' (VERH-E02 strook, Hoeveel-hokjes-vragen). None = geen regel van deze ronde."""
    if r.startswith('fout = de helft van het aantal hokjes'):
        m = _HELFT_STROOK.search(c.opg)
        if not m or int(m.group(1)) % 2 or not re.search(r'hoeveel hokjes', c.opg, re.I): return {'exact': set()}
        h = int(m.group(1)) // 2
        return {'exact': {f'{h} hokjes', str(h)}}
    # #398 (besluit Overzicht 11:28, voorstel Oefeningen): op de lijn van 0 tot 1 een eindpunt aangeklikt (0, 1 of n/n), niet het antwoord.
    # Staat in de entry vóór de stuk-regels (#203); geen ±1-regel, dus de #390-guard slaat hem niet over.
    if r.startswith('fout = een eindpunt van de lijn'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip())
        if not m or not (0 < int(m.group(1)) < int(m.group(2))): return {'exact': set()}
        n_ = int(m.group(2)); return {'exact': {'0', '1', f'{n_}/{n_}'}}
    return None

def _regels_r8(r, c):
    """G6 merge-fixlijst ronde 8: nieuwe motorregels. None = geen regel van deze ronde."""
    a = c.a
    E = lambda *vals: {'exact': {str(x) for x in vals if isinstance(x, int) and x >= 0}}
    G = lambda *cents: {'exact': {geld(x) for x in cents if x >= 0}, 'pred': lambda v, cs=set(cents): _cent(v) in cs}
    # #233 (Oefeningen batch 6, MKU-E03): torens van blokjes uit jsRender.stapels; alleen als het antwoord het totaal aantal blokjes is
    if r.startswith(('fout = het antwoord min één toren', 'fout = het antwoord plus één toren', 'fout = het antwoord plus het aantal torens', 'fout = het aantal torens', 'fout = de hoogste toren keer')):
        st = c.jr.get('stapels') if c.jr.get('soort') == 'bouwvorm' else None
        if not isinstance(st, list): return {'exact': set()}
        hs = [h for rij in st for h in rij if isinstance(h, int) and h > 0]
        if not hs or a != sum(hs): return {'exact': set()}
        if r.startswith('fout = het antwoord min één toren'): return E(*{a - h for h in hs})
        if r.startswith('fout = het antwoord plus het aantal torens'): return E(a + len(hs))      # #296: elke toren één te veel
        if r.startswith('fout = het antwoord plus één toren'): return E(*{a + h for h in hs})
        if r.startswith('fout = het aantal torens'): return E(len(hs))
        if r.startswith('fout = de hoogste toren keer het aantal torens'): return E(max(hs) * len(hs))
        if r.startswith('fout = de hoogste toren keer het aantal vakjes van de grond'): return E(max(hs) * len(st) * max(len(x) for x in st))
        return None
    # #271 (Didactiek batch 5, les 32/61): verhoudingstabel 'x1 → y1, wat hoort bij x2?': hetzelfde erbij doen
    if r.startswith('fout = y1 + (x2 - x1)') or r.startswith('fout = y1 + x2'):
        if len(c.nums) < 3: return {'exact': set()}
        x1, y1, x2 = c.nums[:3]
        if x2 <= x1: return {'exact': set()}      # alleen 'erbij' (x2 groter); terug in de tabel is 'eraf' en past niet bij de tekst 'opgeteld'
        v = y1 + (x2 - x1) if '(x2 - x1)' in r else y1 + x2
        if c.ac is not None: return G(v * 100)
        return E(v)
    # #277 (Didactiek batch 5, VERH-E02 #5): alleen het aantal stukken getypt (x/1); de app leest een kale '5' als 5/1
    if r.startswith('fout = de stukken samen met noemer één'):
        b = _breuk(c.ans)
        if b is None or b >= 1 or b.denominator == 1: return {'exact': set()}
        t = int(re.fullmatch(r'(\d+)/(\d+)', c.ans.strip()).group(1)) if re.fullmatch(r'(\d+)/(\d+)', c.ans.strip()) else None
        return {'exact': {f'{t}/1', str(t)}} if t else {'exact': set()}
    # G5 GET-E09 (Oefeningen G5 batch 7 twijfel 3): wisselgeld 'n [ding] van €p per stuk, betaalt met €B' en 'n × m, daarna k eraf'
    if r.startswith('fout = wat het kost') or r.startswith('fout = één ding betaald'):
        q = re.search(r'(\d+) [^.?]*? van (€\s?\d+(?:,\d{2})?) per stuk[^.?]*? betaalt met (€\s?\d+(?:,\d{2})?)', c.opg)
        if not q or c.ac is None: return {'exact': set()}
        n, p, b = int(q.group(1)), _cent(q.group(2)), _cent(q.group(3))
        if p is None or b is None or b - n * p != c.ac: return {'exact': set()}
        return G(n * p) if r.startswith('fout = wat het kost') else G(b - p)
    if r.startswith('fout = tweede stap vergeten'):
        if len(c.nums) < 3 or a is None or c.nums[0] * c.nums[1] - c.nums[2] != a: return {'exact': set()}
        return E(c.nums[0] * c.nums[1])
    return None

def _compile_regel(regel, c):
    """-> dict(exact=set|None, pred=callable|None, alles=bool, beschrijving) of None als de regel niet te lezen is.
    #104a: een klokregel met '(24 uur)' of '(12 uur)' aan het eind geldt alleen bij items met (of zonder) een tijd van 13:00 of later
    ('fout = klok een uur te laat (24 uur)'). Zo kan een entry voor die items een eigen tekst hebben ('eerst twaalf eraf'), vóór de gewone regel."""
    rr = regel.lower().strip()
    if (q := re.search(r'\s*\((24|12) uur\)$', rr)):
        if (q.group(1) == '24') != _is24(c): return {'exact': set()}
        regel = re.sub(r'\s*\((?:24|12) uur\)\s*$', '', regel, flags=re.I)
    # G6 merge-fixlijst #216 (Didactiek batch 4): '(antwoord vanaf 10)' / '(antwoord onder 10)' achter een regel: de regel geldt alleen bij zo'n antwoord
    if (q := re.search(r'\s*\(antwoord (vanaf|onder) (\d+)\)\s*$', regel, re.I)):
        if c.a is None or ((c.a >= int(q.group(2))) != (q.group(1).lower() == 'vanaf')): return {'exact': set()}
        regel = regel[:q.start()]
    # #399/#392 (ronde 10): '(geleend bij de tientallen)' / '(onthouden naar de honderdtallen)' achter 'fout = antwoord ± 10/100/1000':
    # de regel geldt alleen als er in die kolom echt geleend (getal1 − getal2) of onthouden (getal1 + getal2) wordt; anders de gewone regel daarna.
    if (q := re.search(r'\s*\((geleend bij|onthouden naar) de (tientallen|honderdtallen|duizendtallen)\)\s*$', regel, re.I)):
        k = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000}[q.group(2).lower()]
        regel = regel[:q.start()]; rq = regel.lower().replace('−', '-').replace('\u2013', '-').strip()
        m_ = re.fullmatch(r'fout = antwoord ([+-]) (\d+)', rq)
        if not m_ or int(m_.group(2)) != k or c.g1 is None or c.g2 is None or c.a is None: return {'exact': set()}
        geleend = q.group(1).lower().startswith('geleend')
        if geleend: ok = m_.group(1) == '+' and c.g1 - c.g2 == c.a and (c.g1 % k) < (c.g2 % k)
        else: ok = m_.group(1) == '-' and c.g1 + c.g2 == c.a and (c.g1 % k) + (c.g2 % k) >= k
        if not ok: return {'exact': set()}
    # #532 (eindcheck G6 r11, les 140): '(met overdracht naar de honderdtallen)' / '(zonder overdracht naar de …)' achter 'fout = antwoord ± k' bij een
    # plussom (getal1 + getal2 = antwoord): de motor rekent de echte overdracht naar die kolom uit, inclusief een één die al meekwam
    # (getal1 mod k + getal2 mod k ≥ k; 5138 + 4269: 38 + 69 = 107 → met). Zo kiest de motor de tekst met of zonder 'er gaat er een mee'.
    if (q := re.search(r'\s*\((met|zonder) overdracht naar de (tientallen|honderdtallen|duizendtallen)\)\s*$', regel, re.I)):
        k = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000}[q.group(2).lower()]
        regel = regel[:q.start()]; rq = regel.lower().replace('−', '-').replace('\u2013', '-').strip()
        m_ = re.fullmatch(r'fout = antwoord ([+-]) (\d+)', rq)
        if not m_ or int(m_.group(2)) != k or c.g1 is None or c.g2 is None or c.a is None or c.g1 + c.g2 != c.a: return {'exact': set()}
        if ((c.g1 % k) + (c.g2 % k) >= k) != (q.group(1).lower() == 'met'): return {'exact': set()}
    r_lett = regel.strip()      # Oef-#421/#422: de letterlijke regel met zijn eigen minteken (norm421 maakt er '−' van)
    r = regel.lower().replace('−', '-').replace('\u2013', '-').strip()
    a, g1, g2, n = c.a, c.g1, c.g2, c.nums
    if c.jr.get('soort') == 'lijngrafiek' and (r219 := _lijn219(r, c)) is not None: return r219      # G6 merge-fixlijst #219: lijngrafiek (VBN-E02)
    if (r8 := _regels_r8(r, c)) is not None: return r8      # G6 merge-fixlijst ronde 8: #233, #271, G5 GET-E09
    if (r10 := _regels_r10(r, c)) is not None: return r10   # G6 merge-fixlijst ronde 10: #380 helft van de strook
    E = lambda *vals: {'exact': {(_kg(x) if isinstance(x, Fraction) else str(x)) for x in vals if x is not None and (not isinstance(x, (int, Fraction)) or x >= 0) and not (isinstance(x, Fraction) and _kg(x) is None)}}      # Oef-#437: kommagetal als '8,4'
    if getattr(c, 'neg', False):      # Oef-#494: in een item met getallen onder nul mag een sleutel onder nul ('−9'); hele getallen met teken
        E = lambda *vals: {'exact': {(_sfmt494(x) if isinstance(x, int) else _kg(x) if isinstance(x, Fraction) else str(x)) for x in vals if x is not None
                                     and (isinstance(x, int) or not isinstance(x, Fraction) or (x >= 0 and _kg(x) is not None))}}
    # Oef-#494 (G7/G8): de routes bij getallen onder nul. start = het eerste getal uit de vraag (met teken, _snums494), verandering = antwoord − start.
    #   teken vergeten      = het antwoord met het andere teken (−9 → 9; 3 → −3)
    #   van nul af geteld   = alleen de verandering, vanaf 0 (7 °C, 16 graden kouder → −16)
    #   verkeerde richting  = de verandering de andere kant op (7 °C, 16 graden kouder → 23)
    if r.startswith(('fout = teken vergeten', 'fout = het teken vergeten', 'fout = min vergeten', 'fout = minteken vergeten')):
        an = getattr(c, 'an', None)
        return {'exact': set(_neg_vormen494(_sfmt494(-an)))} if NEG494 and an else {'exact': set()}
    if r.startswith(('fout = van nul af geteld', 'fout = vanaf nul geteld', 'fout = verkeerde richting')):
        an = getattr(c, 'an', None); sn = _snums494(c.opg) if NEG494 else []
        if not NEG494 or an is None or not sn or sn[0] == 0: return {'exact': set()}
        d_ = an - sn[0]; w_ = d_ if 'nul' in r else sn[0] - d_
        return {'exact': set(_neg_vormen494(_sfmt494(w_)))} if d_ and w_ != an else {'exact': set()}
    # Oef-#1000 (G8 batch 6, MEET-V01 #2): routes bij een vol bouwwerk van blokjes (jsRender soort 'bouwsel': diep, hoog, breed; antwoord = diep × hoog × breed).
    #   de maten opgeteld (optellen in plaats van keer)  = diep + hoog + breed
    #   twee maten keer elkaar (twee zijden in plaats van drie) = elk product van twee maten (voorkant, zijkant, bovenkant)
    #   één vlak (de oppervlakte van één vlak, één laag) = diep × breed (de bovenkant; de lagen vergeten)
    #   drie vlakken (de blokjes van drie kanten)        = diep × breed + breed × hoog + diep × hoog
    # Alleen als het antwoord echt diep × hoog × breed is; een waarde gelijk aan het antwoord geeft nooit een sleutel (les 306).
    if r.startswith(('fout = de maten opgeteld', 'fout = maten opgeteld', 'fout = optellen in plaats van keer', 'fout = twee maten keer elkaar', 'fout = twee zijden in plaats van drie',
                     'fout = één vlak', 'fout = de oppervlakte van één vlak', 'fout = drie vlakken')):
        jr_ = c.jr if c.jr.get('soort') == 'bouwsel' else {}
        d_, h_, b_ = (jr_.get(k) for k in ('diep', 'hoog', 'breed'))
        if not all(isinstance(x, int) and x > 0 for x in (d_, h_, b_)) or a != d_ * h_ * b_: return {'exact': set()}
        if 'opgeteld' in r or 'optellen' in r: w_ = {d_ + h_ + b_}
        elif 'twee' in r: w_ = {d_ * h_, d_ * b_, h_ * b_}
        elif 'drie vlakken' in r: w_ = {d_ * b_ + b_ * h_ + d_ * h_}
        else: w_ = {d_ * b_}
        return {'exact': {str(x) for x in w_ if x != a}}
    if r.startswith('andere fout') or 'of een andere fout' in r or r.startswith('ander vak') or 'een andere vorm of kleur' in r or 'een klok met een ander uur' in r:
        return {'alles': True}
    if r.startswith('volgorde omgedraaid'): return E('|'.join(reversed(c.ans.split('|'))))
    # Oef-#490 (G8 batch 4, GET-E05/M01/MEET-E01; 8 okt): de routes bij een uitkomst van de rekenmachine in een verhaal (getal1 = per stuk, getal2 = het totaal,
    # het kommagetal in de vraag = de uitkomst op de rekenmachine). Geen ±1-regels, dus #390 laat ze heel. Elke regel geeft alleen een sleutel als hij uitkomt.
    if r.startswith('fout = het hele getal van het kommagetal uit de vraag'):
        m_ = re.search(r'(?<![\d.,])(\d+),(\d+)(?![\d,])', c.opg); return E(int(m_.group(1))) if m_ else {'exact': set()}
    if r.startswith('fout = de cijfers achter de komma uit de vraag'):
        m_ = re.search(r'(?<![\d.,])(\d+),(\d+)(?![\d,])', c.opg); return E(int(m_.group(2))) if m_ else {'exact': set()}
    # Oef-#495 (G8 batch 5, MEET-E03 #5): een nul te weinig bij een deling (GB × 100 i.p.v. × 1000, dan gedeeld): het antwoord : 10, afgekapt (256 → 25, 16 → 1)
    if r.startswith(('fout = een nul te weinig (afgekapt)', 'fout = antwoord : 10 (afgekapt)')):
        return E(a // 10) if isinstance(a, int) and a >= 10 else {'exact': set()}
    if r.startswith('fout = de rest van getal2 : getal1'):
        return E(g2 % g1) if isinstance(g1, int) and isinstance(g2, int) and g1 and g2 % g1 else {'exact': set()}
    if r.startswith('fout = hele getal + rest'):
        return E(g2 // g1 + g2 % g1) if isinstance(g1, int) and isinstance(g2, int) and g1 and g2 % g1 else {'exact': set()}
    if re.match(r'fout = getal1 [-−] antwoord', r):
        return E(g1 - a) if isinstance(g1, int) and a is not None and 0 < g1 - a != a else {'exact': set()}
    if (m_ := re.match(r'fout = (?:het )?antwoord (×|x|\*|:|÷|/) ?(100|1000|1\.000)\b', r)):
        k_ = int(m_.group(2).replace('.', ''))
        if a is None: return {'exact': set()}
        if m_.group(1) in ('×', 'x', '*'): return {'exact': set(_vormen(a * k_))}
        return {'exact': set(_vormen(a // k_))} if a % k_ == 0 and a // k_ else {'exact': set()}
    # G6 merge-fixlijst #169 (Dave 21:24): breuk op de lijn van 0 tot 1, één stuk (1/noemer) ernaast; 0 heet '0', niet voorbij de lijn
    if r.startswith('fout = één stuk ernaast'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip())
        if not m: return {'exact': set()}
        t, n = int(m.group(1)), int(m.group(2))
        return E(*[('0' if x == 0 else f'{x}/{n}') for x in (t - 1, t + 1) if 0 <= x <= n])
    # G6 merge-fixlijst #203 (besluit Oefeningen 21:59): op de lijn een stuk te ver (t + 1) of een stuk te kort (t − 1); 0 heet '0', niet voorbij 1
    if r.startswith('fout = een stuk te ver') or r.startswith('fout = een stuk te kort'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip())
        if not m: return {'exact': set()}
        t, n = int(m.group(1)), int(m.group(2)); x = t + 1 if r.startswith('fout = een stuk te ver') else t - 1
        return E('0' if x == 0 else f'{x}/{n}') if 0 <= x <= n else {'exact': set()}
    # G6 merge-fixlijst #202 (Oefeningen 21:59): een even grote breuk met een andere noemer, alleen als de vraag een noemer noemt ('met noemer N', '?/N')
    if r.startswith('fout = even grote breuk met een andere noemer'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip()); q = re.search(r'met noemer (\d+)|\?/(\d+)', c.opg)
        if not m or not q: return {'exact': set()}
        from fractions import Fraction as _Fr202
        f = _Fr202(int(m.group(1)), int(m.group(2))); N = int(q.group(1) or q.group(2))
        return E(*[f'{f.numerator * k}/{f.denominator * k}' for k in range(1, 11) if f.denominator * k != N])
    # (#203: 'tellen vanaf 1' geeft geen eigen waarde, het is 'een stuk te kort'; de regel blijft leesbaar maar staat in geen entry meer)
    # G6 merge-fixlijst #186 (Didactiek batch 3, 21:42): op de lijn vanaf 1 geteld in plaats van vanaf 0 → één stuk te kort
    if r.startswith('fout = tellen vanaf 1 in plaats van 0'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip())
        if not m or int(m.group(1)) < 1: return {'exact': set()}
        t, n = int(m.group(1)), int(m.group(2))
        return E('0' if t == 1 else f'{t - 1}/{n}')
    # G6 merge-fixlijst #198 (Didactiek 21:42): de eenheden er alleen bij gezet (30 × 27 → 600 + 7 = 607), en omgekeerd; niet bij een rond getal (dan is het een goed deelproduct)
    if r.startswith('fout = getal1 × tientallen(getal2) + eenheden(getal2)'):
        if g1 is None or g2 is None: return {'exact': set()}
        # #210 (Didactiek 2c): niet als antwoord − waarde een deelproduct is (425 bij 21 × 25: 525 − 425 = 20 × 5): dan is het ook 'stuk vergeten'
        dp = deelproducten(g1, g2)
        return E(*[v for v in (y * (x // 10 * 10) + x % 10 for x, y in ((g2, g1), (g1, g2)) if 10 <= x < 100 and x % 10) if g1 * g2 - v not in dp])
    # G6 merge-fixlijst #176 (Oefeningen 21:43): oppervlakte — de omtrek berekend, of de oppervlakte verdubbeld
    if r.startswith('fout = (getal1 + getal2) × 2'):
        return E((g1 + g2) * 2) if g1 is not None and g2 is not None else {'exact': set()}
    if r.startswith('fout = antwoord × 2'):
        return E(a * 2) if a is not None else {'exact': set()}
    # G6 merge-fixlijst #170: een even grote breuk die niet zo eenvoudig mogelijk is (alleen waar de vorm gevraagd wordt)
    if r.startswith('fout = gelijkwaardig maar niet zo eenvoudig mogelijk'):
        m = re.fullmatch(r'(\d+)/(\d+)', c.ans.strip())
        if not m: return {'exact': set()}
        t, n = int(m.group(1)), int(m.group(2))
        return E(*[f'{t * k}/{n * k}' for k in range(2, 11)])
    # G6 merge-fixlijst #190 (Didactiek 21:25): getal1 × (de cijfers van getal2 bij elkaar opgeteld), bv. 25 × 37 → 25 × 10 = 250
    if r.startswith('fout = getal1 × (som van de cijfers van getal2)') or r.startswith('fout = getal1 × de cijfers van getal2 opgeteld'):
        if g1 is None or g2 is None or g2 < 10 or g2 % 10 == 0: return {'exact': set()}      # bij 40 is 4 'nul vergeten'
        if sum(int(x) for x in str(g2)) == g2 // 10 * 10: return {'exact': set()}      # #196: bij 19 is × 10 het eerste stuk van de goede route ('stuk vergeten')
        v = g1 * sum(int(x) for x in str(g2))
        return E(v) if g1 * g2 - v not in deelproducten(g1, g2) else {'exact': set()}      # #210: zelfde check als bij #198
    # G6 merge-fixlijst #163 (besluit Dave 21:07): sorteren in twee vakken ('wel:…|niet:…', M05 #3 deelbaar of niet)
    # G6 merge-fixlijst #193 (Didactiek 21:35): 'één getal in het verkeerde vak' met een richting
    if r.startswith('fout = een deelbaar getal bij niet') or r.startswith('fout = een niet-deelbaar getal bij deelbaar') or \
       r.startswith('fout = één getal in het verkeerde vak') or r.startswith('fout = vakken omgewisseld'):
        m = re.fullmatch(r'wel:([^|]*)\|niet:([^|]*)', c.ans.strip())
        if not m: return {'exact': set()}
        wel, niet = [x for x in m.group(1).split(',') if x], [x for x in m.group(2).split(',') if x]
        vak = lambda w, n: f"wel:{','.join(sorted(w))}|niet:{','.join(sorted(n))}"
        if r.startswith('fout = vakken omgewisseld'): return E(vak(niet, wel))
        naar_niet = [vak([y for y in wel if y != x], niet + [x]) for x in wel]      # een deelbaar getal bij niet
        naar_wel = [vak(wel + [x], [y for y in niet if y != x]) for x in niet]       # een niet-deelbaar getal bij deelbaar
        if r.startswith('fout = een deelbaar getal bij niet'): return E(*naar_niet)
        if r.startswith('fout = een niet-deelbaar getal bij deelbaar'): return E(*naar_wel)
        return E(*(naar_niet + naar_wel))
    if r.startswith('de minsom omgedraaid'):
        return {'pred': lambda v: bool(re.fullmatch(r'(\d+) - (\d+)', norm421(v).replace('−', '-'))) and int(re.findall(r'\d+', v)[0]) < int(re.findall(r'\d+', v)[1])}
    if r.startswith('de deelsom omgedraaid'):
        # Oef-#429 (G7 DENK-04 #5, '8 : 328'): alleen de deling met deeltal en deler omgewisseld. Antwoord 'a : b' → optie 'b : a';
        # antwoord een getal en de vraag noemt 'a : b' → wat het kind dan opschrijft: b : a als breuk of kommagetal (b/a, '0,…').
        def _deel(t):
            m_ = re.fullmatch(r'\s*(\d+(?:,\d+)?)\s*[:÷]\s*(\d+(?:,\d+)?)\s*', str(t or ''))
            return (m_.group(1), m_.group(2)) if m_ else None
        da = _deel(c.ans)
        if da: return {'pred': lambda v: _deel(v) == (da[1], da[0]) and da[0] != da[1]}
        mq = re.search(r'(\d+)\s*[:÷]\s*(\d+)', c.opg)
        if mq and c.a is not None and int(mq.group(2)) and int(mq.group(1)) == c.a * int(mq.group(2)) and int(mq.group(1)) != int(mq.group(2)):
            from fractions import Fraction as _Fq
            w = _Fq(int(mq.group(2)), int(mq.group(1)))
            return {'pred': lambda v: waarde416(v) == w}
        return {'exact': set()}
    if r.startswith('de plussom'): return {'pred': lambda v: '+' in v}
    if r.startswith('de minsom'): return {'pred': lambda v: '−' in norm421(v)}      # Oef-#421: '−', ' - ' en '–'
    if r.startswith('de keersom'): return {'pred': lambda v: '×' in v}
    # MKU-K03 vormnamen
    if r.startswith('fout = vierkant bij een rechthoek'):
        return {'pred': lambda v: (v, c.ans) in (('vierkant', 'rechthoek'), ('rechthoek', 'vierkant'))}
    m = re.match(r'fout = (cirkel|driehoek|rechthoek|vierkant)\b(?: \(bij een (\w+) of (\w+)\))?', r)
    if m:
        bij = {m.group(2), m.group(3)} - {None}
        return {'pred': lambda v: v == m.group(1) and (not bij or c.ans in bij)}
    if r.startswith('fout = ruit, ster of zeshoek'): return {'pred': lambda v: v in ('ruit', 'ster', 'zeshoek')}
    # spiegelen (MKU-E03): de stip is niet verplaatst = het kind tikt het vak van de stip zelf
    if r.startswith('stip niet verplaatst') or r.startswith('fout = het vak van de stip') or r.startswith('fout = het oorspronkelijke vak'):
        return E(c.jr.get('stip')) if c.jr.get('stip') else None
    # plattegrond-vakken (G6 merge-fixlijst #234: de letter is de kolom, het cijfer de rij; 'B3' = kolom B, rij 3. Alleen dit commentaar is aangepast, de logica niet)
    if r.startswith('goede letter, ander cijfer'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[0] == ca[0] and cv != ca}
    if r.startswith('goed cijfer, andere letter'):
        return {'pred': lambda v: (cv := c.code(v)) and (ca := c.code(c.ans)) and cv[1:] == ca[1:] and cv != ca}
    if r.startswith('letter en cijfer omgedraaid'):
        def omg(v):
            cv, ca = c.code(v), c.code(c.ans)
            return bool(cv and ca) and cv == f'{chr(64 + int(ca[1:]))}{ord(ca[0]) - 64}' and cv != ca
        return {'pred': omg}
    # klok
    if r.startswith('fout = 12 uur'): return E('12 uur') if c.ans != '12 uur' else {'exact': set()}
    if r.startswith('fout = een uur te vroeg of te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h - 1)} uur', f'{_wrap(h + 1)} uur') if h else None
    if r.startswith('fout = een uur te laat'):
        h = _uur(c.ans); return E(f'{_wrap(h + 1)}:00' if ':' in c.ans else f'{_wrap(h + 1)} uur') if h else None
    # klok met half en kwart (#38): leest de klok uit de klokkenrij of de tekst
    if r.startswith('fout = klok een uur te laat') or r.startswith('fout = klok een uur te vroeg'):
        ta = _tijd(c.ans, c)
        if not ta: return None
        ex, doel_t = _schuif(c.ans, ta, 60 if 'te laat' in r else -60, c)      # #69: boven 12 uur de sleutel in 24 uur; pred: beide vormen
        return {'exact': ex, 'pred': lambda v: _tijd(v, c) == doel_t}
    # G5 fixlijst #70: klok een minuut / vijf / tien minuten / een kwartier te vroeg of te laat
    if m := re.match(r'fout = klok (een|één|1|vijf|5|tien|10|een kwartier|15) (?:minuut |minuten )?te (vroeg|laat)', r):
        ta = _tijd(c.ans, c)
        if not ta: return None
        d = {'een': 1, 'één': 1, '1': 1, 'vijf': 5, '5': 5, 'tien': 10, '10': 10, 'een kwartier': 15, '15': 15}[m.group(1)]
        ex, doel_t = _schuif(c.ans, ta, d if m.group(2) == 'laat' else -d, c)
        return {'exact': ex, 'pred': lambda v: _tijd(v, c) == doel_t}
    # G5 fixlijst #72: 'over' en 'voor' verwisseld (tien voor 2 bij tien over 2; tien over half 3 bij tien voor half 3)
    if r.startswith('fout = over en voor verwisseld'):
        ta = _tijd(c.ans, c)
        if not ta or ta[1] in (0, 30): return {'exact': set()} if ta else None
        h, mi = ta; nh = h - 1 if mi <= 15 else h + 1 if mi >= 45 else h; doel_t = (_wrap(nh), 60 - mi)
        d = ((doel_t[0] % 12) * 60 + doel_t[1]) - ((h % 12) * 60 + mi)
        ex, _ = _schuif(c.ans, ta, d, c)
        return {'exact': ex, 'pred': lambda v: _tijd(v, c) == doel_t}
    # G5 fixlijst #103 (Didactiek 18:54): de grote wijzer als uur gelezen → een heel uur, uur = minuten : 5 (12 bij 0)
    if r.startswith('fout = grote wijzer als uur gelezen'):
        ta = _tijd(c.ans, c)
        if not ta: return None
        if ta[1] % 5: return {'exact': set()}
        doel_t = (_wrap(ta[1] // 5 or 12), 0)
        if doel_t == ta: return {'exact': set()}
        ans = c.ans.strip()
        if re.fullmatch(r'\d{1,2}:\d{2}', ans): ex = {f'{doel_t[0]}:00'}
        elif re.fullmatch(r'[A-L]', ans): ex = set()                       # klokkenrij: de pred zoekt de klok
        else: ex = {f'{doel_t[0]} uur'}
        return {'exact': ex, 'pred': lambda v: _tijd(v, c) == doel_t}
    if r.startswith('fout = grote wijzer verkeerd'):
        ta = _tijd(c.ans, c)
        if not ta: return None
        h_ = _t24(c.ans) // 60 if _t24(c.ans) is not None else ta[0]          # #69: boven 12 uur het uur in 24 uur
        ex = {f'{h_}:{m:02d}' for m in (0, 15, 30, 45) if m != ta[1]} if re.fullmatch(r'\d{1,2}:\d{2}', c.ans) else set()
        return {'exact': ex, 'pred': lambda v: (t := _tijd(v, c)) is not None and t[0] == ta[0] and t[1] != ta[1]}
    # afronden (G5 merge-fixlijst #12, Didactiek v1): het andere buurtiental/-honderdtal van getal1 (166 → 160 als 170 goed is)
    # G6 fixlijst #1 (Dave 19:58): ook het andere duizendtal / tienduizendtal (stap uit de regel; bij 'tiental/honderdtal' ook uit de opgave)
    if r.startswith(('fout = het andere tiental/honderdtal naast getal1', 'fout = het andere buurtiental', 'fout = het andere buurhonderdtal', 'fout = het andere tiental', 'fout = het andere honderdtal',
                     'fout = het andere duizendtal', 'fout = het andere tienduizendtal', 'fout = het andere buurduizendtal', 'fout = het andere buurtienduizendtal')):
        if g1 is None or a is None: return None
        if 'tienduizendtal' in r: stap = 10000
        elif 'duizendtal' in r: stap = 1000
        elif 'tiental/' in r and re.search(r'tienduizendtal', c.opg): stap = 10000
        elif 'tiental/' in r and re.search(r'duizendtal', c.opg): stap = 1000
        else: stap = 100 if ('honderdtal' in r and 'tiental/' not in r) or re.search(r'honderdtal', c.opg) else 10
        onder = g1 // stap * stap; boven = onder + stap
        if g1 == onder: return {'exact': set()}
        return E(onder if a == boven else boven if a == onder else None)
    # kalender (#41)
    # G5 fixlijst #70: richting bij datums (een dag later/eerder apart; elke latere/eerdere datum)
    if r.startswith(('fout = een dag later', 'fout = een dag eerder')):
        da = _datum(c.ans); return E(_dag_erbij(da, 1 if 'later' in r else -1)) if da else None
    if r.startswith(('fout = datum later dan het antwoord', 'fout = datum eerder dan het antwoord', 'fout = een latere datum', 'fout = een eerdere datum')):
        da = _datum(c.ans)
        if not da: return None
        dnr = lambda d: sum(DAGEN[:d[1]]) + d[0]; later = 'later' in r
        return {'pred': lambda v: (dv := _datum(v)) is not None and dv != da and ((dnr(dv) > dnr(da)) if later else (dnr(dv) < dnr(da)))}
    if r.startswith('fout = een dag ernaast'):
        da = _datum(c.ans); return E(_dag_erbij(da, -1), _dag_erbij(da, 1)) if da else None
    # #49 (Didactiek 4cd): twee regels, elk met een eigen tekst; de oude gecombineerde regel blijft werken (beide datums)
    if r.startswith(('fout = gestopt bij de laatste of eerste dag van de maand', 'fout = gestopt op de laatste dag van de maand', 'fout = gestopt op de eerste dag van de maand')):
        ds = re.search(r'Het is (\d{1,2} [a-z]+)\.', c.opg); da = _datum(c.ans); d0 = _datum(ds.group(1)) if ds else None
        if not (da and d0) or da[1] == d0[1]: return {'exact': set()} if da and d0 else None
        vroeg, laat = (d0, da) if 'later' in c.opg else (da, d0)
        laatste, eerste = f'{DAGEN[vroeg[1]]} {MAANDEN[vroeg[1]]}', f'1 {MAANDEN[laat[1]]}'
        if r.startswith('fout = gestopt op de laatste dag'): return E(laatste)
        if r.startswith('fout = gestopt op de eerste dag'): return E(eerste)
        return E(laatste, eerste)
    # tabel (#42): uit jsRender.rijen
    if c.jr.get('soort') == 'tabel' and c.jr.get('rijen') and r.startswith(('fout = andere cel', 'fout = som van de rij', 'fout = som van de kolom', 'fout = som van twee cellen', 'fout = verschil van twee cellen')):
        rijen = [x['waarden'] for x in c.jr['rijen']]; cellen = [v for rij in rijen for v in rij]
        if r.startswith('fout = andere cel'): return E(*cellen)
        if r.startswith('fout = som van de rij'): return E(*[sum(rij) for rij in rijen])
        if r.startswith('fout = som van de kolom'): return E(*[sum(col) for col in zip(*rijen)])
        paren = [(x, y) for i, x in enumerate(cellen) for y in cellen[i + 1:]]
        if r.startswith('fout = som van twee cellen'): return E(*[x + y for x, y in paren])
        return E(*[abs(x - y) for x, y in paren])
    # letterlijke optie ('het smalle glas'): de regel is (een deel van) de tekst van de foute optie
    if not r.startswith('fout'): r = norm421(r_lett).lower()   # fixlijst #32 + Oef-#421/#422: regel '3 euro' leest ook '€3'; '−', '-' en '–' zijn één minteken
    if not r.startswith('fout') and any(r in norm421(o['tekst'], geld=r.startswith('€')).lower() for o in c.it['opties'] or []):
        # G6 merge-fixlijst #380 (Didactiek gate ronde 9 deel A, les 110): een letterlijke regel met een getal matcht alleen het hele getal
        # (woordgrens): '4 hokjes' pakt niet meer '14 hokjes'. Zonder getal blijft het een stukje tekst ('het smalle glas'); '€3' is exact.
        if not any(lett_past(r, o['tekst']) for o in c.it['opties'] or []): return {'exact': set(), 'letterlijk': r}
        return {'pred': lambda v: lett_past(r, v), 'letterlijk': r}
    # merge-punt #29: antwoord × 10 / : 10 (exact); bij geld het bedrag × 10 / : 10
    m = re.match(r'fout = (?:het )?antwoord (×|x|\*|:|÷|/) ?10\b', r)
    if m:
        keer = m.group(1) in ('×', 'x', '*')
        if c.ac is not None:
            if keer: return {'exact': {geld(c.ac * 10)}, 'pred': lambda v: _cent(v) == c.ac * 10}
            return ({'exact': {geld(c.ac // 10)}, 'pred': lambda v: _cent(v) == c.ac // 10} if c.ac % 10 == 0 else {'exact': set()})
        if a is None and KOMMA437 and c.d is not None:      # Oef-#440 (G7/G8): kommagetal-antwoord: de komma één plek verschoven (1,1 → 11 / 0,11)
            w440 = c.d * 10 if keer else c.d / 10
            return {'exact': {_kg(w440)}, 'pred': lambda v: _dec(v) == w440}
        if a is None: return None
        if keer: return {'exact': set(_punt(a * 10))}
        if a % 10 == 0 and a >= 10: return {'exact': set(_punt(a // 10))}
        if KOMMA437 and a >= 1:      # Z-#973 (Didactiek b8 deel A): G7/G8: ': 10' bij een heel antwoord dat niet op 0 eindigt = kommagetal (14 → '1,4'), 'tien keer te weinig'
            w973 = Fraction(a, 10); return {'exact': {_kg(w973)}, 'pred': lambda v: _dec(v) == w973}
        return {'exact': set()}
    # G5 fixlijst #106 (Oefeningen 19:06): het kind typt de prijs in. Sleutel = elk bedrag in de opgave dat iets kost (niet het bedrag
    # waarmee je betaalt of dat je hebt), als het ≠ antwoord. In pas_toe gaat deze regel vóór 'antwoord ± 10 cent / ± €1' (zeker vóór onzeker).
    # Oef-#426 (#530, eindcheck G5 r11): 'fout = het bedrag dat eraf gaat': bij een minsom met geld het tweede bedrag, op waarde ('€4,75', '€ 4,75',
    # '4,75', '4,75 euro'), alleen als het ≠ antwoord en eerste − tweede = antwoord. Minteken '−', '-' of '–'.
    # Oef-#442 (Z-#603, gemiddelde GET-04 nrO 6): 'fout = de som van de getallen' (niet gedeeld) en 'fout = het middelste getal (op grootte)'.
    # De rij is de langste reeks getallen met ', ' of ' en ' ertussen ('6, 13, 3, 15, 18'). Alleen een sleutel als de waarde echt zo uitkomt:
    # som/middelste ≠ antwoord, middelste alleen bij een oneven aantal (bij even: geen sleutel). Geen rij van minstens 3 getallen → geen sleutel.
    # Z-#633 (G7 MEET-03 #1): 'fout = de bodem (l × b)': het kind gaf de oppervlakte van de bodem ('De bodem is 2 bij 3 cm' → 6), ≠ antwoord.
    # Zeker (de maten staan in de vraag): in pas_toe gaat hij vóór de onzekere regels als 'antwoord ± 1', ook als de entry hem later zet.
    # Oef-#445 (G7 VERH-02 nrO 3, 'Hoeveel procent is 36 van 75?', antwoord '48%'): de motor leest '%'. Twee regels, alleen als het antwoord op '%'
    # eindigt en de vraag 'D van G' heeft (D = het deel, G = het geheel): 'fout = het deel zelf (als %)' → 'D%' (het deel overgenomen) en
    # 'fout = geheel min deel' → '(G − D)%'. Geen sleutel als de waarde ≤ 0 is of gelijk aan het antwoord. Sleutel met en zonder spatie voor '%'.
    # Ook 'fout = tien keer het procent (als %)': antwoord × 10 of : 10 met '%' ('48%' → '480%', '4,8%'). De drie regels vallen nooit samen:
    # het deel zelf gaat voor, geheel min deel vervalt als het het deel is, tien keer vervalt als het het deel of geheel min deel is.
    # Oef-#453 (alleen KOMMA437, G7/G8): 'fout = kommagetal met procentteken': het kommagetal uit de vraag met een '%' erachter
    # ('Schrijf 0,7 in procenten.', antwoord '70%' → '0,7%'). Alleen als het antwoord op '%' eindigt en de vraag een kommagetal heeft.
    if r.startswith('fout = kommagetal met procentteken'):
        if not KOMMA437 or not re.fullmatch(r'\d+(?:,\d+)?\s?%', c.ans.strip()): return {'exact': set()}
        k453 = [x for x in re.findall(r'(?<![\d,.])(\d+,\d+)(?![\d,.])', c.opg)]
        w453 = {f'{x}%' for x in k453} | {f'{x} %' for x in k453}
        return {'exact': {x for x in w453 if x.replace(' ', '') != c.ans.strip().replace(' ', '')}}
    # Oef-#453 (alleen KOMMA437, G7/G8): 'fout = getallen achter elkaar (als %)': de eerste twee hele getallen uit de vraag aan elkaar met '%'
    # ('1 op de 4 lootjes', antwoord '25%' → '14%'). Alleen als het antwoord op '%' eindigt.
    if r.startswith('fout = getallen achter elkaar (als %)'):
        if not KOMMA437 or not re.fullmatch(r'\d+(?:,\d+)?\s?%', c.ans.strip()): return {'exact': set()}
        g453 = re.findall(r'(?<![\d,.])(\d+)(?![\d,.])', c.opg)
        if len(g453) < 2: return {'exact': set()}
        w453 = g453[0] + g453[1]
        return {'exact': set() if w453 == re.sub(r'\s?%', '', c.ans.strip()) else {f'{w453}%', f'{w453} %'}}
    if r.startswith('fout = het deel zelf (als %)') or r.startswith('fout = geheel min deel') or r.startswith('fout = tien keer het procent (als %)'):
        m445 = re.search(r'(?<![\d,.])(\d+) van (?:de |het )?(\d+)(?![\d,.])', c.opg)
        # Oef-#453 (alleen KOMMA437, dus G7/G8): ook een breuk 'D/G' ('Schrijf 32/50 in procenten.'); 'tien keer het procent' ook zonder deel
        if not m445 and KOMMA437: m445 = re.search(r'(?<![\d,./])(\d+)/(\d+)(?![\d,./])', c.opg)
        a445 = re.fullmatch(r'(\d+)\s?%', c.ans.strip())
        if not a445: return {'exact': set()}
        if not m445 and not (KOMMA437 and r.startswith('fout = tien keer het procent')): return {'exact': set()}
        a445 = Fraction(int(a445.group(1)))
        d445, g445 = (Fraction(int(m445.group(1))), Fraction(int(m445.group(2)))) if m445 else (None, None)
        if r.startswith('fout = het deel zelf'): w445 = {d445}
        elif r.startswith('fout = geheel min deel'): w445 = {g445 - d445} - {d445}
        else: w445 = {a445 * 10, a445 / 10} - ({d445, g445 - d445} if m445 else set())
        w445 = {_kg(x) for x in w445 if x > 0 and x != a445}
        return {'exact': {f'{x}%' for x in w445} | {f'{x} %' for x in w445}}
    # Z-#607 (Didactiek-besluit 8 okt, GET-02 'Rond af op één cijfer achter de komma', antwoord 2,0): vraagt de opgave een aantal cijfers achter
    # de komma, dan is '2' bij 2,0 niet goed (uitzondering op 'slotnul telt niet', README). 'fout = decimaal-nul weggelaten' geeft de kortere vormen
    # met dezelfde waarde ('2,0' → '2'; '3,50' → '3,5'); alleen als de vraag om cijfers achter de komma vraagt en het antwoord op 0 eindigt.
    if r.startswith('fout = decimaal-nul weggelaten'):
        return {'exact': d607(c), 'z607': True}
    if r.startswith('fout = de bodem'):
        mb = re.search(r'bodem (?:is|van) (\d+(?:,\d+)?) (?:cm |m )?(?:bij|×|x) (\d+(?:,\d+)?)', c.opg)
        if not mb: return {'exact': set()}
        vb = Fraction(mb.group(1).replace(',', '.')) * Fraction(mb.group(2).replace(',', '.'))
        if _dec(c.ans) == vb: return {'exact': set()}
        return {'exact': {_kg(vb)}, 'pred': lambda v: _dec(v) == vb, 'zeker': True}
    if r.startswith('fout = de som van de getallen') or r.startswith('fout = het middelste getal'):
        rijen = [re.findall(r'\d+(?:,\d+)?', x.group(0)) for x in re.finditer(r'\d+(?:,\d+)?(?:(?:, | en )\d+(?:,\d+)?)+', c.opg)]
        rij = max(rijen, key=len) if rijen else []
        if len(rij) < 3: return {'exact': set()}
        w442 = [Fraction(x.replace(',', '.')) for x in rij]
        if r.startswith('fout = de som'): v442 = sum(w442)
        else:
            if len(w442) % 2 == 0: return {'exact': set()}
            v442 = sorted(w442)[len(w442) // 2]
        k442 = _kg(v442)
        if k442 is None or _dec(k442) == _dec(c.ans): return {'exact': set()}
        return {'exact': {k442}, 'pred': lambda v: _dec(v) == v442}
    if r.startswith('fout = het bedrag dat eraf gaat'):
        BED = r'(€\s?\d+(?:,\d{1,2})?|\d+(?:,\d{1,2})?\s?euro\b|\d+,\d{2})'
        m426 = re.search(BED + r'\s*[−\-–]\s*' + BED, c.opg.replace('\u00a0', ' '), re.I)
        if not m426: return {'exact': set()}
        a1, a2 = _cent(m426.group(1)), _cent(m426.group(2)); ans = c.ac if c.ac is not None else _cent(c.ans)
        if a1 is None or a2 is None or ans is None or a2 == ans or a1 - a2 != ans: return {'exact': set()}
        return {'exact': {geld(a2)} if c.ac is not None else {geld(a2)[1:]}, 'pred': lambda v, _a=a2: _cent(v) == _a}
    if r.startswith('fout = de prijs'):
        if c.ac is None: return None
        o_ = re.sub(r'(?:betaalt|betaal|hebt|heb) (?:met |nog )?€\s?\d+(?:,\d\d)?', '', c.opg)
        pr = {x for x in (_cent(b) for b in re.findall(r'€\s?\d+(?:,\d\d)?', o_)) if x is not None and x != c.ac}
        return {'exact': {geld(x) for x in pr}, 'pred': lambda v: _cent(v) in pr, 'prijs': True}
    # merge-punten #19/#32: geld ± 1 cent, ± 10 cent, ± €1 (sleutels in huisnotatie; de invoer wordt genormaliseerd, #33)
    m = re.match(r'fout = antwoord (±|\+|-) (?:(\d+) cent|€ ?(\d+))\b', r)
    if m:
        if c.ac is None: return None
        d = int(m.group(2)) if m.group(2) else int(m.group(3)) * 100
        doel = ([c.ac - d] if m.group(1) in ('±', '-') and c.ac - d >= 0 else []) + ([c.ac + d] if m.group(1) in ('±', '+') else [])
        return {'exact': {geld(x) for x in doel}, 'pred': lambda v: _cent(v) in doel}
    # getallen
    if a is None and not n: return None
    # G6 merge-fixlijst #215 (Didactiek batch 4): omrekenen met het aantal nullen als factor (km → m × 3, cm → m : 2)
    if r.startswith('fout = getal1 keer het aantal nullen van de factor') or r.startswith('fout = getal1 gedeeld door het aantal nullen van de factor'):
        fk = _factor215(c)
        if not fk or fk[1] != r.startswith('fout = getal1 keer'): return {'exact': set()}
        k = len(str(fk[0])) - 1
        if fk[1]: return E(g1 * k)
        return E(g1 // k) if g1 % k == 0 else {'exact': set()}
    # G6 merge-fixlijst #205 (Didactiek 3b): breuk van een aantal ('3/8 van 32'): één stuk = het aantal : de noemer (niet als de teller 1 is: dan is dat het antwoord)
    if r.startswith('fout = één stuk (het aantal : de noemer)'):
        m = re.search(r'(\d+)/(\d+) van (?:de |het )?(€ ?)?(\d+(?:,\d\d)?)(?![\d,])', c.opg)
        if not m: return {'exact': set()}
        t, nn = int(m.group(1)), int(m.group(2))
        if t == 1: return {'exact': set()}
        if m.group(3):      # geld: in centen
            ct = _cent('€' + m.group(4)); return {'exact': {geld(ct // nn)}, 'pred': lambda v: _cent(v) == ct // nn} if ct is not None and ct % nn == 0 else {'exact': set()}
        tot = int(m.group(4)) if m.group(4).isdigit() else None
        return E(tot // nn) if tot is not None and tot % nn == 0 else {'exact': set()}
    # G6 merge-fixlijst #206 (Didactiek 3b): '2/4 … is evenveel als ?/16': de factor (nieuwe noemer : oude noemer)
    if r.startswith('fout = de factor (nieuwe noemer : oude noemer)'):
        m = re.search(r'(\d+)/(\d+)\b.*?\?/(\d+)', c.opg)
        if not m: return {'exact': set()}
        n1, n2 = int(m.group(2)), int(m.group(3))
        return E(n2 // n1) if n2 % n1 == 0 and n2 > n1 else {'exact': set()}
    # G6 merge-fixlijst #207 (Didactiek 3b): breuk > 1 in hele pizza's: de rest (stukken die overblijven) en 'steeds een hele eraf' (teller − j × noemer, j ≥ 2)
    if r.startswith('fout = de rest van getal1 : getal2'):
        return E(g1 % g2) if g2 and g1 % g2 else {'exact': set()}
    if r.startswith('fout = getal1 − j × getal2 (j ≥ 2)') or r.startswith('fout = getal1 - j × getal2 (j ≥ 2)'):
        if not g2: return {'exact': set()}
        return E(*[g1 - j * g2 for j in range(2, g1 // g2 + 1) if g1 - j * g2 > 0 and g1 - j * g2 != g1 % g2])
    if re.match(r'fout = getal1 \+ getal2', r): return E(g1 + g2) if g2 is not None else None
    # G5 fixlijst #50: elk ander kommagetal (de deling uitgerekend, '6,5' bij 52 : 8) – na 'quotiënt,rest' zetten
    if re.match(r'fout = een kommagetal\b', r):
        ex_ = set()
        if g2 and g1 % g2 and (g1 * 100) % g2 == 0: ex_ = {f'{g1 / g2:.2f}'.rstrip('0').replace('.', ',')}
        return {'exact': ex_, 'pred': lambda v: bool(re.fullmatch(r'\d+,\d+', str(v).strip()))}
    # G5 fixlijst #50 (Didactiek batch 3 #47): 'quotiënt,rest' = de rest achter een komma geschreven ('9,18' bij 243 : 25 = 9 rest 18)
    if re.match(r'fout = quotiënt,rest\b', r):
        if not (g2 and g1 % g2): return {'exact': set()}
        q_, r_ = divmod(g1, g2); k_ = f'{q_},{r_}'
        return {'exact': {k_}, 'pred': lambda v, k_=k_: str(v).replace(' ', '') == k_}
    if re.match(r'fout = getal1 - getal2 of getal2 - getal1', r) or r.startswith('fout = verschil van de getallen'):
        return E(abs(g1 - g2)) if g2 is not None else None
    if re.match(r'fout = getal2 - de eenheden van getal1', r): return E(g2 - g1 % 10) if g2 is not None else None
    # nieuw 1 okt (fixlijst G4, besluit Dave): keersom van de twee getallen; eenheden van een getal
    if re.match(r'fout = getal1 [×x\*] getal2', r): return E(g1 * g2) if g2 is not None else None
    m = re.match(r'fout = (?:de )?eenheden van getal([12])', r)
    if m: g = g1 if m.group(1) == '1' else g2; return E(g % 10) if g is not None else None
    # G5 fixlijst #64 (Didactiek recheck 2c/1d/3b): afronden op honderdtallen, maar het kind rondde af op tientallen
    # (alleen als dat iets anders is dan het getal zelf en het goede antwoord). Volgorde: na 'verkeerde kant', vóór 'één stap te ver'.
    # G6 fixlijst #1 (Dave 19:58): ook afgerond op honderdtallen / duizendtallen (Rond af op duizendtallen → op honderdtallen gedaan)
    if m := re.match(r'fout = getal1 afgerond op (tientallen|honderdtallen|duizendtallen|tienduizendtallen)', r):
        if g1 is None: return None
        u_ = {'tientallen': 10, 'honderdtallen': 100, 'duizendtallen': 1000, 'tienduizendtallen': 10000}[m.group(1)]
        t_ = (g1 + u_ // 2) // u_ * u_
        return E(t_) if t_ not in (g1, a) else {'exact': set()}
    # G5 fixlijst #62 (Didactiek batch 4): maatbeker (jsRender soort 'maatbeker': tot, perstreep, cijfer_om, max)
    if c.jr.get('soort') == 'maatbeker' and r.startswith(('fout = één streepje ernaast', 'fout = een streepje ernaast', 'fout = streepjes als 1 geteld')):
        tot, ps, co, mx = c.jr.get('tot'), c.jr.get('perstreep'), c.jr.get('cijfer_om'), c.jr.get('max')
        if not all(isinstance(x, int) and x > 0 for x in (tot, ps, co)): return {'exact': set()}
        if 'ernaast' in r: return E(*[x for x in (tot - ps, tot + ps) if x >= 0 and (not mx or x <= mx)])
        basis = tot // co * co; k = (tot - basis) // ps          # het getal eronder + het aantal streepjes als losse ml
        return E(basis + k) if ps > 1 and k > 0 and basis + k != tot else {'exact': set()}
    # G5 fixlijst #76 (batch 6): staafdiagram (jsRender.staven, cijfer_om): de waarde van een andere staaf, en het getal vlak onder de top
    if c.jr.get('soort') == 'staafdiagram' and r.startswith(('fout = een andere staaf', 'fout = andere staaf')):
        return E(*[st_['waarde'] for st_ in c.jr.get('staven') or [] if isinstance(st_, dict) and isinstance(st_.get('waarde'), int) and st_['waarde'] != a])
    if c.jr.get('soort') == 'staafdiagram' and r.startswith(('fout = het getal onder de top', 'fout = het getal vlak onder de top', 'fout = net onder de top', 'fout = het getal net onder de top')):   # #93: zelfde regel, ook zo genoemd
        co = c.jr.get('cijfer_om')
        if not (isinstance(co, int) and co > 0 and a is not None): return {'exact': set()}
        o_ = a // co * co
        return E(o_) if o_ != a else {'exact': set()}
    # #77 (batch 6): breukdelen van getal1, per item uitgerekend (alleen als het een heel getal is)
    m = re.match(r'fout = (een kwart|één kwart|de helft|drie kwart) van getal1', r)
    if m:
        if g1 is None: return None
        t_, n_ = {'een kwart': (1, 4), 'één kwart': (1, 4), 'de helft': (1, 2), 'drie kwart': (3, 4)}[m.group(1)]
        return E(g1 * t_ // n_) if g1 * t_ % n_ == 0 and g1 * t_ // n_ != a else {'exact': set()}
    # #81 (batch 6): geld tellen: het aantal munten en briefjes als euro's (jsRender.munten)
    if r.startswith('fout = het aantal munten'):
        mu = c.jr.get('munten') if c.jr.get('soort') == 'geld' else None
        if not mu: return {'exact': set()}
        k_ = geld(len(mu) * 100)
        return E(k_) if geld_norm(k_) != geld_norm(c.ans) else {'exact': set()}
    # G6 fixlijst #6 (Dave 19:58): 'getal2 ± 1' in plaats van 'antwoord − 99': het kind deed er één bij/af in plaats van honderd of duizend
    if m := re.match(r'fout = getal([12]) (±|\+|-) (\d+)\b(?![,.]\d)', r):
        g = g1 if m.group(1) == '1' else g2
        if g is None: return None
        k = int(m.group(3))
        return E(*([g + k] if m.group(2) in ('±', '+') else []), *([g - k] if m.group(2) in ('±', '-') and g - k >= 0 else []))
    # G6 fixlijst #154 (Didactiek 20:15): op de verkeerde plek: getal2 ± getal1 × 10 / : 10 / × 100 ('100 meer dan 22.969' → 23.969, 22.979, 32.969)
    if m := re.match(r'fout = getal2 ([+−-]) getal1 ([×:]) (10|100)\b', r):
        if g1 is None or g2 is None: return None
        k = int(m.group(3)); st_ = g1 * k if m.group(2) == '×' else (g1 // k if g1 % k == 0 else None)
        if st_ is None: return {'exact': set()}
        return E(g2 + st_) if m.group(1) == '+' else (E(g2 - st_) if g2 - st_ >= 0 else {'exact': set()})
    # Z-#616 (G7/G8, met KOMMA437): bij een geldantwoord is 'fout = getal1 / getal2' een bedrag als het getal in de vraag een bedrag is
    # ('€28', '€45,60', niet '28' / '45,6'); dan raakt de sleutel ook '€58' van 'antwoord × 10' en wint hij door zijn plek in de entry.
    if KOMMA437 and c.ac is not None and (m616 := re.fullmatch(r'fout = getal([12])', r.strip())):
        g616 = g1 if m616.group(1) == '1' else g2
        bedr616 = {_cent(x) for x in re.findall(r'€\s?\d+(?:\.\d{3})*(?:,\d{1,2})?', c.opg)}
        if g616 is not None and (g616 * 100).denominator == 1 and int(g616 * 100) in bedr616 and int(g616 * 100) != c.ac:
            k616 = int(g616 * 100); return {'exact': {geld(k616)}, 'pred': lambda v: _cent(v) == k616}
    if re.match(r'fout = getal1\b', r): return E(g1)
    if re.match(r'fout = getal2\b', r): return E(g2)
    if re.match(r'fout = getal \+ 10 of antwoord \+ 10', r): return E(g1 + 10, a + 10)
    if re.match(r'fout = getal - 10 of antwoord - 10', r): return E(g1 - 10, a - 10)
    if re.match(r'fout = getal \+ 1\b', r): return E(g1 + 1)
    if r.startswith('fout = getal + bekend deel'): return E(n[0] + n[-1])
    # Oef-#434 (G7 GET-01 #7): 'Welk cijfer staat op de plaats van de tienduizendtallen in 736.125?' → de cijfers op de plaats links en rechts
    # ernaast (7 en 6), niet het goede cijfer. Het getal is het langste getal in de vraag; alleen bij een antwoord van één cijfer.
    if r.startswith(('fout = het cijfer op de plek ernaast', 'fout = het cijfer op de plaats ernaast')):
        PL = ['eenheden', 'tientallen', 'honderdtallen', 'duizendtallen', 'tienduizendtallen', 'honderdduizendtallen', 'miljoenen']
        q = re.search(r'(?:plaats|plek) van de (\w+)', c.opg.lower()); gs = re.findall(r'\d{1,3}(?:\.\d{3})+|\d+', c.opg)
        if not q or q.group(1) not in PL or not gs or not re.fullmatch(r'\d', c.ans.strip()): return {'exact': set()}
        cf = max(gs, key=lambda x: len(x.replace('.', ''))).replace('.', ''); i = len(cf) - 1 - PL.index(q.group(1))
        if not 0 <= i < len(cf) or cf[i] != c.ans.strip(): return {'exact': set()}
        return E(*[cf[j] for j in (i - 1, i + 1) if 0 <= j < len(cf) and cf[j] != c.ans.strip()])
    if r.startswith('fout = stip op de lijn van nul'):      # Oef-#1023 (G8 VBN-V01 #1): antwoord '(x, y)' → sleutels 'x,0' en '0,y' (stip op een as), nooit de goede stip zelf
        m_ = re.fullmatch(r'\((\d+), ?(\d+)\)', c.ans.strip())
        if not m_: return {'exact': set()}
        x_, y_ = m_.groups(); goed_ = {f'{x_},{y_}', f'{x_}, {y_}', f'({x_},{y_})', f'({x_}, {y_})'}
        return {'exact': {k_ for k_ in (f'{x_},0', f'0,{y_}') if k_ not in goed_}}
    if r.startswith('fout = een getal uit de vraag'): return E(*[x for x in n if not (isinstance(x, Fraction) and _kg(x) == c.ans.strip())])      # #437: een kommagetal = het antwoord is geen fout
    if r.startswith('fout kleiner dan het kleinste getal'): m0 = min(n); return {'pred': lambda v: _int(v) is not None and _int(v) < m0, 'kleinerDan': m0}
    if r.startswith('fout kleiner dan het getal in de vraag'): return {'pred': lambda v: _int(v) is not None and _int(v) < g1, 'kleinerDan': g1}
    if r.startswith('fout = laatste getal van de rij'):
        m = re.search(r'((?:\d+|□)(?:, (?:\d+|□))+)', c.opg); seq = m.group(1).split(', ') if m else []
        i = seq.index('□') if '□' in seq else len(seq)
        return E(int(seq[i - 1])) if i > 0 else None
    if r.startswith('fout = het aantal in de tekening'): return E(c.jr.get('aantal'))
    if r.startswith('fout = het getal dat eraf gaat'):
        m = re.search(r'(\d+) − (\d+)', c.opg.split('.')[1] if '.' in c.opg else c.opg); return E(int(m.group(2))) if m else None
    if r.startswith('fout = het deel dat al in de plussom staat'):
        m = re.search(r'(\d+) \+ □', c.opg); return E(int(m.group(1))) if m else None
    # G6 fixlijst #4 (Dave 19:58): regels bij een kommagetal-antwoord (1,4); sleutels met komma, zonder slot-nullen; invoer zoals VORM (#105)
    if m := re.match(r'fout = antwoord (±|\+|-) (\d+,\d+)', r):
        d_ = c.d
        if d_ is None and re.fullmatch(r'\d+', c.ans.strip()) and re.search(r'\d,\d', c.opg): d_ = Fraction(int(c.ans.strip()))      # Oef-#436: ook bij een heel antwoord, als de vraag kommagetallen heeft ('4,6 + 0,4 = 5' → '4,9' en '5,1')
        if d_ is None: return {'exact': set()} if _dec(c.ans) is not None else None
        x_ = _dec(m.group(2)); doel = ([d_ - x_] if m.group(1) in ('±', '-') and d_ - x_ >= 0 else []) + ([d_ + x_] if m.group(1) in ('±', '+') else [])
        return {'exact': {_kg(y) for y in doel}, 'pred': lambda v: _dec(v) in doel}
    if r.startswith(('fout = het hele getal van het kommagetal', 'fout = de tienden als heel getal', 'fout = de cijfers om de komma omgedraaid')):
        if c.d is None: return {'exact': set()} if _dec(c.ans) is not None else None
        voor, na = c.ans.strip().split(',')
        heel, tiend = int(voor), int(na)
        if r.startswith('fout = het hele getal'): doel = [Fraction(heel)]
        elif r.startswith('fout = de tienden'): doel = [Fraction(tiend)] if tiend != heel else []
        else:
            om = _dec(f'{na},{voor}') if len(voor) == 1 and len(na) == 1 else None
            doel = [om] if om is not None and om not in (c.d, Fraction(heel), Fraction(tiend)) else []
        doel = [y for y in doel if y != c.d]
        return {'exact': {_kg(y) for y in doel}, 'pred': lambda v: _dec(v) in doel}
    if r.startswith('fout = het hele getal'):
        m = re.search(r'□ = (\d+)', c.opg) or re.search(r'hoeveel (\d+) −', c.opg) or re.search(r'ook: (\d+) −', c.opg)
        return E(int(m.group(1))) if m else None
    if r.startswith('fout = getal opgeteld in plaats van eraf'):
        m = re.search(r'hoeveel (\d+) − (\d+)', c.opg) or re.search(r'(\d+) − (\d+) = □', c.opg)
        return E(int(m.group(1)) + int(m.group(2))) if m else None
    if a is None: return None
    # nieuw 1 okt (fixlijst G4, besluit Dave): 'antwoord ± getal1' (één groepje te veel/te weinig) en 'eenheden als antwoord'
    m = re.match(r'fout = antwoord (±|\+|-) getal([12])', r)
    if m:
        g = g1 if m.group(2) == '1' else g2
        if g is None: return None
        return E(*([a - g] if m.group(1) in ('±', '-') else []), *([a + g] if m.group(1) in ('±', '+') else []))
    if re.match(r'fout = (?:de )?eenheden (?:als antwoord|van het antwoord)', r) or r.startswith('eenheden als antwoord'):
        return E(a % 10) if a >= 10 else {'exact': set()}
    if r.startswith('fout = antwoord gedeeld door getal1'):      # #40 staafdiagram: streepjes geteld
        return E(a // g1) if g1 and a % g1 == 0 else {'exact': set()}
    if r.startswith('fout = antwoord ± 1'): return E(a - 1, a + 1)
    if re.match(r'fout = antwoord \+ 9 of \+ 10', r): return E(a + 9, a + 10)
    m = re.match(r'fout = antwoord ([+-]) (\d+) of meer', r)
    if m:
        k = int(m.group(2))
        if m.group(1) == '+': return {'pred': lambda v: _int(v) is not None and _int(v) >= a + k, 'vanaf': a + k}
        return {'pred': lambda v: _int(v) is not None and _int(v) <= a - k, 'totEnMet': a - k}
    m = re.match(r'fout = antwoord ([+-]) (\d+)', r)
    if m: return E(a + int(m.group(2)) if m.group(1) == '+' else a - int(m.group(2)))
    if r.startswith('fout ligt 1 of 2 naast'): return E(a - 2, a - 1, a + 1, a + 2)
    if r.startswith('fout ligt 1 naast'): return E(a - 1, a + 1)
    if r.startswith('fout ligt 2 naast'): return E(a - 2, a + 2)
    return None

PLAATS = re.compile(r'[\[{](getal1|getal2|antwoord|uur in woorden|uur als cijfer|nullen|factor|Factor)[\]}]')
UUR_WOORD = {1: 'één', 2: 'twee', 3: 'drie', 4: 'vier', 5: 'vijf', 6: 'zes', 7: 'zeven', 8: 'acht', 9: 'negen', 10: 'tien', 11: 'elf', 12: 'twaalf'}
def vul_in(tekst, c):
    """Vult sjabloonteksten per item in: [uur in woorden], [uur als cijfer] en (fixlijst #48) [getal1], [getal2], [antwoord]
    (ook met {…}: '{getal1}'). getal1/getal2 = eerste/tweede getal in de vraag. None als er niets in te vullen valt of een waarde ontbreekt."""
    if not PLAATS.search(tekst): return None
    h = _uur(c.ans)
    waarden = {'getal1': c.g1, 'getal2': c.g2, 'antwoord': c.ans, 'uur in woorden': UUR_WOORD.get(h) if h else None, 'uur als cijfer': h}
    fk = _factor215(c) if re.search(r'[\[{](nullen|factor|Factor)[\]}]', tekst) else None      # #215
    waarden.update(nullen=NUL_WOORD.get(len(str(fk[0])) - 1) if fk else None, factor=FACTOR_WOORD.get(fk[0]) if fk else None,
                   Factor=FACTOR_WOORD.get(fk[0]).capitalize() if fk else None)
    if any(waarden[m.group(1)] is None for m in PLAATS.finditer(tekst)): return None
    return PLAATS.sub(lambda m: str(waarden[m.group(1)]), tekst)

def per_item_tekst(regel, tekst):
    return 'tekst per item' in regel or '…' in tekst or '[plek]' in tekst or '[andere plek]' in tekst or bool(PLAATS.search(tekst))

PLACEHOLDER_STIP = '[TEKST NODIG (Oefeningen): stip niet verplaatst]'
def is_spiegel(it):
    jr = it['visual']['jsRender'] or {}
    return jr.get('soort') == 'vorm' and bool(jr.get('stip')) and bool(jr.get('as'))
def heeft_stipregel(st):
    return any(re.match(r'(stip niet verplaatst|fout = het vak van de stip|fout = het oorspronkelijke vak)', f['regel'].lower()) for f in st['foutHints'])

def _gevraagd(c):
    """#92: de rij(en) en kolom(men) van de tabel die in de vraag genoemd worden (namen uit jsRender.rijen[].naam en kolommen)."""
    rijen = [x for x in c.jr.get('rijen') or [] if isinstance(x, dict)]; kol = list(c.jr.get('kolommen') or [])
    noem = lambda n: bool(n) and bool(re.search(rf"\b{re.escape(str(n))}\b", c.opg, re.I))
    ri = [i for i, x in enumerate(rijen) if noem(x.get('naam'))]; kj = [j for j, k in enumerate(kol) if noem(k)]
    w = [x['waarden'] for x in rijen]
    return ({sum(w[i]) for i in ri}, {sum(rw[j] for rw in w if j < len(rw)) for j in kj})
def _tabel_trede(f, v, c):
    r = f['regel'].lower(); x = _int(v)
    if r.startswith('andere fout') or r.startswith('fout = alles'): return 9
    if r.startswith('fout = andere cel'): return 0
    rs, ks = _gevraagd(c)
    if r.startswith('fout = som van de rij'): return 1 if x in rs else 4
    # G5 merge-fixlijst #124 (Didactiek recheck-121): de vraag noemt een rij en geen kolom ('Hoeveel boten in totaal?'). Een kolomsom is dan de
    # route 'kolom opgeteld' (de volgorde van de regels in de entry), ook als dezelfde waarde toevallig een som van twee cellen of Claudes sleutel is.
    if r.startswith('fout = som van de kolom'): return 2 if x in ks or (KOLOM_VOOR_DEEL and rs and not ks) else 4
    return 3

def _pas_toe_kern(it, st, alle_cellen=None):
    """st = somtype-entry uit hints/batch*.json. Zet it['foutHints'], it['foutRegels'], it['foutHintsTekst']."""
    c = Ctx(it)
    claude = [dict(f) for f in it['extraVelden'].get('claudeFoutHints') or []]
    # Oef-#444 (G7/G8, met KOMMA437): Claudes sleutels in huisnotatie: '-3' (koppelteken) in claudeFoutHints wordt '−3', zoals in claudeDenkfouten
    # en in de opties; de labelregel vergelijkt beide kanten met dezelfde normalisatie (norm421 zonder geld).
    def _n444(x):      # ook een minteken vooraan ('-3', '–3' → '−3'); norm421 doet alleen '-' tussen getallen of spaties
        return re.sub(r'^\s*[-–](?=\s?\d)', '−', norm421(x, geld=False)) if KOMMA437 and isinstance(x, str) else x
    if KOMMA437: claude = [dict(f, fout=_n444(f.get('fout'))) for f in claude]
    claude_txt = {f['fout']: f['uitleg'] for f in claude}
    vervangen = {v['claudeTekst'] for v in st.get('claudeVervangen', [])} | {f['claudeTekst'] for f in st['foutHints'] if f.get('claudeTekst')}
    merge = {m['fout']: m for m in it['extraVelden'].get('mergeFoutHints') or []}
    regels = []
    for f in st['foutHints']:
        comp = compile_regel(f['regel'], c)
        per_item = per_item_tekst(f['regel'], f['tekst'])
        if comp is None and f['bron'] in ('claude', 'claude-taalfix'):     # niet te lezen Claude-regel: op de Claude-sleutels (claudeDenkfout)
            dk = f.get('claudeDenkfout')
            # G5 fixlijst #71: een per item hersplitste denkfout (denkfoutClaude = Claudes label) valt onder de oude Claude-regel zolang
            # de entry nog geen regel voor het nieuwe label heeft (dan verdwijnt er geen sleutel); daarna onder de nieuwe regel
            eigen = {g.get('claudeDenkfout') for g in st['foutHints'] if g.get('claudeDenkfout')}
            keys = {k['fout'] for k in claude if not dk or any(_n444(d['fout']) == k['fout'] and (d['denkfout'] == dk or (d.get('denkfoutClaude') == dk and d['denkfout'] not in eigen))
                                                                for d in it['extraVelden'].get('claudeDenkfouten') or [])}
            comp = {'exact': keys, 'claudeSleutels': True}
            # fixlijst #48 (1): een taalfix met een vaste tekst (zonder '…') zet die vaste tekst op de Claude-sleutels; anders Claudes tekst per item
            per_item = f['bron'] == 'claude' or per_item

        if comp and comp.get('exact'): comp['exact'] = {w for x in comp['exact'] for w in _vormen(x)}     # #60: '10000' én '10.000'
        if c.neg and comp and comp.get('exact'):      # Oef-#494: '−9' én '-9'; het antwoord zelf (met teken) is nooit een regelwaarde
            comp['exact'] = {w for x in comp['exact'] for w in _neg_vormen494(x) if c.an is None or not str(w).lstrip().startswith(('−', '-', '–')) or _sint494(w) != c.an}
        # G5 fixlijst #121 (Dave 20:04): bij een tabel (VBN-E01) is een regelwaarde nooit het goede antwoord (de motor nam de goede rij of cel mee)
        if comp and comp.get('exact') and c.jr.get('soort') == 'tabel':
            comp['exact'] = {w for w in comp['exact'] if w != c.ans and (c.a is None or _int(w) != c.a)}
            assert c.ans not in comp['exact'], ('#121: regelwaarde = het goede antwoord', it.get('id'), f['regel'])
        # G6 merge-fixlijst #223 (Didactiek 3b): ook buiten tabellen nooit het goede antwoord in de waarden van een regel (ANTWOORD_UIT_WAARDEN, G6)
        if ANTWOORD_UIT_WAARDEN and comp and comp.get('exact'):
            comp['exact'] = {w for w in comp['exact'] if w != c.ans and (c.a is None or _int(w) != c.a) and (c.d is None or _dec(w) != c.d)}
            assert c.ans not in comp['exact'], ('#223: regelwaarde = het goede antwoord', it.get('id'), f['regel'])
        regels.append((f, comp, per_item))
    # MKU-E03 spiegelen: 'stip niet verplaatst' gaat vóór de algemene regels; zonder tekst van Oefeningen een gemarkeerde plaatshouder
    it['controle']['foutHintPlaceholder'] = None
    if is_spiegel(it) and not heeft_stipregel(st):
        f = {'regel': 'stip niet verplaatst (fout = het vak van de stip)', 'soort': 'stip niet verplaatst', 'bron': 'merge-plaatshouder', 'tekst': PLACEHOLDER_STIP}
        regels.insert(0, (f, {'exact': {it['visual']['jsRender']['stip']}}, False))
        it['controle']['foutHintPlaceholder'] = ['stip niet verplaatst']
    # kandidaten
    if it['opties']: kand = [o['tekst'] for o in it['opties'] if o['tekst'] != c.ans]
    elif alle_cellen: kand = [v for v in alle_cellen if v != c.ans]
    else:
        # merge-punt #35b: een leesbare regel met een ingevulde [getal]-tekst voegt ook zijn sleutels toe (niet alleen Claudes sleutels)
        kand = list(dict.fromkeys([k['fout'] for k in claude] + sorted({v for f, comp, pi in regels if comp and (not pi or (not comp.get('claudeSleutels') and vul_in(f['tekst'], c))) for v in comp.get('exact', ())},
                                                                        key=lambda x: (_int(x) is None, _int(x) or 0, x))))
        kand = list(dict.fromkeys(w for v in kand for w in _vormen(v)))         # #60: sleutels ≥ 10.000 in beide vormen
        z607 = {v for f, comp, pi in regels if comp and comp.get('z607') for v in comp.get('exact', ())}      # Z-#607: '2' bij 2,0 blijft een sleutel
        kand = [v for v in kand if v != c.ans and (v in z607 or ((c.a is None or _int(v) != c.a) and (c.d is None or _dec(v) != c.d)))]   # G6 #4: '1,40' = '1,4'
        if c.neg: kand = [v for v in kand if _sint494(v) is None or _sint494(v) != c.an]      # Oef-#494: '-9' is het antwoord '−9'
        # G5 merge-fixlijst #14: geen fout-sleutel buiten de getallenlijn (je kunt hem niet aantikken)
        if LIJN_BINNEN and c.jr.get('soort') == 'getallenlijn' and isinstance(c.jr.get('van'), int) and isinstance(c.jr.get('tot'), int):
            kand = [v for v in kand if _int(v) is None or c.jr['van'] <= _int(v) <= c.jr['tot']]
        # G6 merge-fixlijst #153 (Didactiek 20:15): geen sleutel buiten de lijn van visual.getallenlijn (ook kommagetallen: 4,1 op 0–2)
        _gl = (it.get('visual') or {}).get('getallenlijn') or {}
        if isinstance(_gl.get('van'), int) and isinstance(_gl.get('tot'), int):
            kand = [v for v in kand if _dec(v) is None or _gl['van'] <= _dec(v) <= _gl['tot']]
        # G5 merge-fixlijst #1/#13: geen fout-sleutel boven het bereik bij afronden (BEREIK_AFRONDEN, gezet door apply_hints van de groep)
        if BEREIK_AFRONDEN and re.match(r'Rond \d', c.opg):
            kand = [v for v in kand if _int(v) is None or _int(v) <= BEREIK_AFRONDEN]
    # merge-punt #33 (GELD_PUNT, opt-in per groep): een geldbedrag met een punt in plaats van een komma ('8.80') krijgt
    # 'Bij geld schrijf je een komma.' (eerste regel; sleutels '8.80' en '€8.80' bij open geldvragen)
    if GELD_PUNT and c.ac is not None and not it['opties'] and c.ac % 100:
        e, ct = divmod(c.ac, 100); pk = [f'{e}.{ct:02d}', f'€{e}.{ct:02d}'] + ([f'{e}.{ct // 10}', f'€{e}.{ct // 10}'] if ct % 10 == 0 else [])
        fp = {'regel': 'fout = punt in plaats van komma (geld)', 'soort': 'punt in plaats van komma', 'bron': 'merge (#33)', 'tekst': GELD_PUNT_TEKST}
        regels.insert(0, (fp, {'exact': set(pk), 'pred': lambda v: bool(re.fullmatch(r'€?\s*\d+\.\d{1,2}', str(v).strip()))}, False))
        kand = kand + [k for k in pk if k not in kand]
    # G6 merge-fixlijst #170 (Dave 21:24): geldt een even grote breuk als goed (breukGelijkwaardigGoed), dan is geen sleutel een even grote breuk
    if it.get('breukGelijkwaardigGoed') and (fa := _breuk(c.ans)) is not None:
        kand = [v for v in kand if _breuk(v) != fa]
    out = []; ongebruikt = []
    tabel = c.jr.get('soort') == 'tabel'
    staaf_vraag = {st_['waarde'] for st_ in c.jr.get('staven') or [] if c.jr.get('soort') == 'staafdiagram' and isinstance(st_, dict)
                   and isinstance(st_.get('waarde'), int) and st_.get('naam') and re.search(rf"\b{re.escape(str(st_['naam']))}\b", c.opg, re.I)}
    def _past(comp, v):
        if bool(comp) and bool(comp.get('alles') or (v in comp.get('exact', ())) or (comp.get('pred') and comp['pred'](v))): return True
        # Oef-#440 (met KOMMA437): een sleutel '8,0' / '300,0' heeft de waarde van het hele getal: hij past op een regelwaarde '8' / '300'
        return bool(KOMMA437 and comp and (q_ := re.fullmatch(r'(\d+),0+', str(v).strip())) and q_.group(1) in comp.get('exact', ()))
    for v in kand:
        hit = None; volgorde = regels; ook = []; gedwongen = set()
        if tabel:
            # G5 fixlijst #82: bij een tabel gaat de precieze regel voor (kleinste set sleutels; pred daarna; 'alles' als laatste;
            # bij gelijke grootte de volgorde in de entry). De andere regels die ook passen, staan in ookRegels.
            pas = [(i, x) for i, x in enumerate(regels) if _past(x[1], v)]
            # #92 (Didactiek batch 6 V4): eerst de cel, dan de som van de GEVRAAGDE rij, dan de som van de GEVRAAGDE kolom, dan
            # 'rij min één'/twee cellen/Claudes sleutels, dan de som van een andere rij of kolom, en 'andere fout' als laatste.
            # Pas binnen dezelfde trede telt #82 (kleinste set, entry-volgorde).
            rang = lambda ix: (_tabel_trede(ix[1][0], v, c), 2 if ix[1][1].get('alles') else 1 if 'exact' not in ix[1][1] else 0, len(ix[1][1].get('exact', ())), ix[0])
            pas.sort(key=rang); volgorde = [x for _, x in pas] + [x for x in regels if not _past(x[1], v)]
            ook = [x[0]['regel'] for _, x in pas[1:] if not x[1].get('alles')]
        elif staaf_vraag and _int(v) in staaf_vraag:
            # #94 (Didactiek batch 6 S5): de sleutel is de waarde van een staaf uit de vraag. Dat is zeker; 'streepjes geteld' is
            # een gok. De staafregels (soort of regel met 'staaf') gaan dan voor, de rest houdt de volgorde van de entry.
            # Een Claude-sleutelregel met 'staaf' in de soort ('één staaf') telt ook mee als Claude deze sleutel anders labelde:
            # de waarde ís een staaf uit de vraag, dus de staaftekst klopt zeker.
            zeker = [x for x in regels if x[1] and not x[1].get('alles') and (_past(x[1], v) or x[1].get('claudeSleutels'))
                     and 'staaf' in f"{x[0].get('soort') or ''} {x[0]['regel']}".lower()]
            if zeker:
                gedwongen = {id(x[0]) for x in zeker}
                volgorde = zeker + [x for x in regels if x not in zeker]
                ook = [x[0]['regel'] for x in regels if x not in zeker and x[1] and not x[1].get('alles') and _past(x[1], v)]
        if not tabel:
            # #106: 'fout = de prijs' is zeker (het bedrag staat in de opgave) en gaat vóór de onzekere geldregels ('± 10 cent', '± €1')
            zp = [x for x in volgorde if x[1] and (x[1].get('prijs') or x[1].get('zeker')) and _past(x[1], v)]      # Z-#633: ook 'zeker' (de bodem)
            if zp:
                volgorde = zp + [x for x in volgorde if x not in zp]
                ook = ook + [x[0]['regel'] for x in regels if x not in zp and x[1] and not x[1].get('alles') and _past(x[1], v)]
        z607v = [x for x in regels if x[1] and x[1].get('z607') and v in x[1].get('exact', ())]
        if z607v: volgorde = z607v; ook = []      # Z-#607: de waarde is het antwoord, alleen de eigen regel past
        uit_vraag = in_vraag390(v, c)
        staaf_alle = {st_['waarde'] for st_ in c.jr.get('staven') or [] if isinstance(st_, dict) and isinstance(st_.get('waarde'), int)} if c.jr.get('soort') == 'staafdiagram' else None
        for f, comp, per_item in volgorde:
            if comp is None: continue
            if uit_vraag and is_pm1_390(f) and not comp.get('z607'): continue      # Z-#607: 'Bijna!' mag bij decimaal-nul (geen getal uit de vraag)      # G6 merge-fixlijst #390: een getal uit de vraag krijgt nooit ±1 of 'Bijna!'
            if staaf_alle is not None and (f.get('soort') or '').lower().startswith('andere staaf') and _int(v) not in staaf_alle: continue      # G5 D-#404: 'andere staaf' alleen bij een staafwaarde
            ok = _past(comp, v) or id(f) in gedwongen      # #94
            if not ok: continue
            if per_item and vul_in(f['tekst'], c):
                hit = {'fout': v, 'uitleg': vul_in(f['tekst'], c), 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f"{f['bron']} (per item)", '_f': f}; break
            if per_item:
                if v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
                    hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': f['regel'], 'soort': f.get('soort'), 'bron': 'claude (per item)', '_f': f}; break
                continue
            tekst = f['tekst']
            if ' / ' in tekst and f['bron'] in ('claude', 'claude-taalfix'):
                # twee teksten van Claude: neem de tekst die bij dit item hoort (bij een taalfix: die het meest lijkt op Claudes tekst)
                delen = tekst.split(' / ')
                ct = claude_txt.get(v)
                tekst = max(delen, key=lambda d: difflib.SequenceMatcher(None, d, ct).ratio()) if ct else delen[0]
            assert not comp.get('letterlijk') or lett_guard(comp['letterlijk'], v), ('#380: letterlijke regel past niet op het hele getal', it.get('id'), f['regel'], v)
            hit = {'fout': v, 'uitleg': tekst, 'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron'], '_f': f}; break
        if hit is None and v in merge:
            m = merge[v]; hit = {'fout': v, 'uitleg': m['uitleg'], 'regel': m['regel'], 'soort': None, 'bron': 'merge'}
        if hit is None and v in claude_txt and claude_txt[v] and claude_txt[v] not in vervangen:
            hit = {'fout': v, 'uitleg': claude_txt[v], 'regel': '(geen regel; Claude-tekst blijft)', 'soort': None, 'bron': 'claude (geen regel)'}
        if hit and ook and hit['regel'] in [x[0]['regel'] for x in regels]: hit['ookRegels'] = [r_ for r_ in ook if r_ != hit['regel']] or None
        if hit and c.jr.get('soort') == 'tabel' and (hit.get('soort') or '').lower().startswith(('andere rij', 'andere cel')):      # G5 #502 (les 137)
            _rij = [r_.get('waarden') or [] for r_ in c.jr.get('rijen') or [] if isinstance(r_, dict)]
            _cel = {x for w_ in _rij for x in w_ if isinstance(x, int)}
            _tot = {sum(w_) for w_ in _rij if all(isinstance(x, int) for x in w_)} | {sum(k_) for k_ in zip(*_rij) if all(isinstance(x, int) for x in k_)}
            _ok = _int(v) in (_tot if (hit.get('soort') or '').lower().startswith('andere rij') else _cel)
            assert _ok, ("#502: 'andere rij'/'andere cel' zonder rij of cel met die waarde", it.get('id'), v, hit.get('soort'))
        if hit and staaf_alle is not None and (hit.get('soort') or '').lower().startswith('andere staaf'):
            assert _int(v) in staaf_alle, ("D-#404: 'andere staaf' zonder staaf met die waarde", it.get('id'), v)
        if hit: hit['stap'] = None; out.append(hit)
        elif v in claude_txt: ongebruikt.append(v)
    regels_out = []
    hit_regel = {}
    for h in out:
        for w in _vormen(h['fout']): hit_regel[w] = h['regel']
    for f, comp, per_item in regels:
        if comp is None: regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'tekst': f['tekst'], 'match': None, 'leesbaar': False}); continue
        mt = {}
        if comp.get('alles'): mt = {'alles': True}
        elif 'exact' in comp:
            # G5 D-#406 (les 122): een sleutel staat alleen in de waarden van de regel die hem echt kreeg (ook na #390/#404 of een gedwongen staafregel)
            w_ = {x for x in comp['exact'] if x not in hit_regel or hit_regel[x] == f['regel']} | {k for k, r_ in hit_regel.items() if r_ == f['regel']}
            mt = {'waarden': sorted(w_, key=lambda x: (_int(x) is None, _int(x) or 0, x))}
        for k in ('kleinerDan', 'vanaf', 'totEnMet'):
            if k in comp: mt = {k: comp[k]}
        if comp.get('pred') and not mt: mt = {'waarden': [h['fout'] for h in out if h['regel'] == f['regel']], 'opOpties': True}
        # G6 #263 / les 39: nooit 'tekst: None' in de data. Een per-item-regel zonder in te vullen plaatshouder houdt de tekst van de entry
        # (bij Claudes sleutels krijgt elke sleutel toch Claudes eigen tekst); met een plaatshouder die niet in te vullen is: None (FIX6 meldt dat).
        _t = (vul_in(f['tekst'], c) or (None if PLAATS.search(f['tekst']) else f['tekst'])) if per_item else f['tekst']
        regels_out.append({'regel': f['regel'], 'soort': f.get('soort'), 'bron': f['bron'], 'tekst': _t,
                           'tekstSterker': ((vul_in(f['tekstSterker'], c) or f['tekstSterker']) if f.get('tekstSterker') and per_item_tekst(f['regel'], f['tekstSterker']) else f.get('tekstSterker')),      # #229
                           'perItem': per_item, 'match': mt, 'leesbaar': True})
    # G6 merge-fixlijst #229 (besluit Dave 22:39; motor in G5–G8 gelijk): elke fout-hint heeft twee lagen. 'uitleg' (= tekst van de regel) is laag 1,
    # na de eerste keer fout. 'uitlegSterker' is laag 2, na de tweede keer fout (Mees: hint 1, opnieuw, hint 2, opnieuw, denkfout-uitleg).
    # laag 2 = tekstSterker van de regel (per item ingevuld als dat moet); ontbreekt die, dan de algemene laag-2-hint van het somtype (hint2 = sterkereHint).
    # De teksten komen van Oefeningen (#262); de motor schrijft zelf geen tekst.
    h2 = st.get('hint2')
    for h in out:
        f = h.pop('_f', None); ts = (f or {}).get('tekstSterker')
        if ts and per_item_tekst(f['regel'], ts): ts = vul_in(ts, c) or (None if PLAATS.search(ts) else ts)
        h['uitlegSterker'] = ts or h2; h['laag2'] = 'tekstSterker' if ts else ('terugval hint2 (somtype)' if h2 else None)
    it['foutHints'] = [dict({'stap': h['stap'], 'fout': h['fout'], 'uitleg': h['uitleg'], 'uitlegSterker': h['uitlegSterker'], 'laag2': h['laag2'], 'regel': h['regel'], 'soort': h['soort'], 'bron': h['bron']}, **({'ookRegels': h['ookRegels']} if h.get('ookRegels') else {})) for h in out]
    it['foutRegels'] = regels_out
    for r_ in regels_out:      # D-#406-guard: geen sleutel in de waarden van een andere regel dan die hem kreeg
        for w in (r_.get('match') or {}).get('waarden') or []:
            assert w not in hit_regel or hit_regel[w] == r_['regel'], ('D-#406: sleutel in de waarden van een andere regel', it.get('id'), w, r_['regel'], hit_regel[w])
    # merge-punt #35a: 'andere fout' met [getal1]/[getal2]/[antwoord] → de per item ingevulde tekst (viel eerder weg: None)
    it['algemeneFoutHint'] = next(((vul_in(f['tekst'], c) if pi else f['tekst']) for f, comp, pi in regels if comp and comp.get('alles') and (not pi or vul_in(f['tekst'], c))), None)
    it['foutHintsTekst'] = ' · '.join(f"{h['fout']} → {h['uitleg']}" for h in out) or None
    it['controle']['zonderFoutHints'] = not out
    it['controle']['foutHintsNietToegepast'] = ongebruikt
    return [f['regel'] for f, comp, _ in regels if comp is None]

# #543/#552 (eindcheck G6 r11 en r11b): het gedrag van lett_past/lett_guard ligt vast in deze testtabel (37 gevallen). De tabel staat in de motor zelf,
# zodat de zelftest overal draait, ook in een kopie buiten de merge-werkplek (de repo). tools/huis_checks.LETT_TABEL moet gelijk zijn (check_hints FAIL).
# Wijkt het gedrag af, dan stopt het laden van de motor (en dus de build).
LETT_TABEL_543 = [
    ('4 hokjes', '4 hokjes', True), ('4 hokjes', 'ruim 4 hokjes', True), ('3 hokjes', '(3 hokjes)', True), ('4 hokjes', '14 hokjes of 4 hokjes', True),
    ('4 hokjes', '14 hokjes', False), ('4 hokjes', '44 hokjes', False), ('4 hokjes', '4,5 hokjes', False), ('4 hokjes', '0,4 hokjes', False),
    ('4 hokjes', '1.4 hokjes', False), ('4 hokjes', '€4 hokjes', False), ('4 hokjes', '1/4 hokjes', False), ('4 hokjes', '−4 hokjes', False),
    ('4 hokjes', '-4 hokjes', False), ('4 hokjes', '– 4 hokjes', False), ('4 hokjes', '− 4 hokjes', False), ('4 hokjes', '-  4 hokjes', False),
    ('4 hokjes', '- 4 hokjes', False), ('4 hokjes', '8 − 4 hokjes', False), ('4 hokjes', '24 − 4 hokjes', False), ('4', '4/5', False),
    ('4', '14', False), ('4', '44', False), ('4', '4,5', False), ('4', '0,4', False), ('4', '1.4', False), ('4', '−4', False),
    ('1/4', '1/4', True), ('3/4', '3/4 deel', True), ('10.000', '10.000', True), ('a4', 'a4', True),
    ('2 cm', '2 cm²', False), ('2 cm', '2 cm', True),
    ('€3', '€3', True), ('€3', '€3,50', False), ('€3', '3', False),
    ('het smalle glas', 'het smalle glas', True), ('het smalle glas', 'het brede glas', False),
]
def _zelftest543():
    _af = []
    for r, v, verwacht in LETT_TABEL_543:
        a, b = lett_past(r.lower(), v), lett_guard(r, v)
        if a != verwacht or b != verwacht: _af.append(f"regel {r!r} op {v!r}: verwacht {'past' if verwacht else 'past niet'}, lett_past={a}, lett_guard={b}")
    assert not _af, '#543: lett_past/lett_guard wijkt af van de testtabel:\n' + '\n'.join(_af)
    return len(LETT_TABEL_543)
_zelftest543()
def _zelftest421():
    """Oef-#421/#422 (8 okt): minteken en euro gelijk in letterlijke regels; '16' leest '16 euro' nog (geen '€' in de regel); woorden met '-' blijven."""
    for r, v, ok in (('27 − 40', '27 - 40', True), ('27 - 40', '27 – 40', True), ('€3', '3 euro', True), ('3 euro', '€ 3', True), ('16', '16 euro', True),
                     ('4 hokjes', '− 4 hokjes', False), ('rood-wit', 'rood-wit', True), ('€3', '€13', False)):
        assert lett_past(r, v) == ok, ('#421', r, v)
_zelftest421()

# Kloktijden (besluit Didactiek 8 okt 15:46): de motor rekent intern met 'h:mm'. Heeft een item zijn tijd in de huisvorm ('14.30 uur' als antwoord of
# optie, of '(Typ als 14.30.)'), dan gaan een kopie van het item en van de hint-entry eerst naar 'h:mm'; daarna gaan foutHints, foutRegels en
# algemeneFoutHint terug naar de huisvorm: sleutel '14.30 uur', in teksten '14.30 uur' (na 'Typ als' zonder 'uur'), foutRegels.match.waarden in alle
# drie de vormen ('14.30 uur', '14.30', '14:30'). Een regel mag dus in beide vormen staan. Items met digitaleKlok: true en items zonder tijd in de
# huisvorm gaan ongewijzigd door de motor. KLOK_PUNT = False zet dit uit.
KLOK_PUNT = True
import copy as _copy_klok
_KP = re.compile(r'(?<![\d.,:])(\d{1,2})\.(\d{2})(?: uur)?(?![\d])')
_KD = re.compile(r'(?<![\d:.,])(\d{1,2}):(\d{2})(?![\d:])')
_KSKIP = {'bron', 'licentie', 'controle', 'merge', 'id', 'bronVariant', 'jsRender', 'husselPlan'}
def _klok_ok(h, m): return int(h) <= 24 and int(m) <= 59
def _klok_heeft_punt(it):
    if it.get('digitaleKlok'): return False
    w = [str(it.get('antwoord') or '')] + [str(o.get('tekst')) for o in it.get('opties') or []]
    return any(re.fullmatch(r'\s*\d{1,2}\.\d{2} uur\s*', x) for x in w) or bool(re.search(r'\(Typ als \d{1,2}\.\d{2}\.\)', it.get('opgave') or ''))
def _klok_naar_dubbelepunt(o):
    if isinstance(o, dict): return {k: (v if k in _KSKIP else _klok_naar_dubbelepunt(v)) for k, v in o.items()}
    if isinstance(o, list): return [_klok_naar_dubbelepunt(v) for v in o]
    if isinstance(o, str): return _KP.sub(lambda m: f'{m.group(1)}:{m.group(2)}' if _klok_ok(m.group(1), m.group(2)) else m.group(0), o)
    return o
def _klok_tekst(t):
    def r(m):
        h, mi = m.group(1), m.group(2)
        if not _klok_ok(h, mi): return m.group(0)
        voor, na = t[:m.start()], t[m.end():]
        if re.search(r'(Typ als|zoals)\s*$', voor): return f'{h}.{mi}'
        return f'{h}.{mi}' if na.startswith(' uur') else f'{h}.{mi} uur'
    return _KD.sub(r, t)
def _klok_vormen(w):
    m = re.fullmatch(r'\s*(\d{1,2})[:.](\d{2})(?: uur)?\s*', str(w))
    if not m or not _klok_ok(*m.groups()): return [w]
    return [f'{m.group(1)}.{m.group(2)} uur', f'{m.group(1)}.{m.group(2)}', f'{m.group(1)}:{m.group(2)}']
def _klok_naar_punt(o, k=None):
    if isinstance(o, dict): return {kk: _klok_naar_punt(v, kk) for kk, v in o.items()}
    if isinstance(o, list):
        if k == 'waarden': return list(dict.fromkeys(x for w in o for x in (_klok_vormen(w) if isinstance(w, str) else [w])))
        return [_klok_naar_punt(v) for v in o]
    if isinstance(o, str): return _klok_tekst(o)
    return o
def pas_toe(it, st, alle_cellen=None):
    if not (KLOK_PUNT and _klok_heeft_punt(it)): return _pas_toe_kern(it, st, alle_cellen)
    a, e = _klok_naar_dubbelepunt(it), _klok_naar_dubbelepunt(st)
    oud = {k: _copy_klok.deepcopy(a.get(k)) for k in a}
    regels = {json_klok(r2): r1 for r1, r2 in zip(_regels_van(st), _regels_van(e))}
    terug = _pas_toe_kern(a, e, alle_cellen)
    for k in a:
        if k not in oud or a[k] != oud[k]: it[k] = _klok_naar_punt(a[k], k)
    return [regels.get(json_klok(r), r) for r in terug] if isinstance(terug, list) else terug
def _regels_van(st): return [f.get('regel') for f in st.get('foutHints') or []]
def json_klok(r): return r if isinstance(r, str) else repr(r)
