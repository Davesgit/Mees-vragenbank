"""G5 merge-fixlijst #121 (besluit Dave 20:04): een foute route geeft niet het goede antwoord. Leest alleen. FAIL:
  VBN-E01 tabel 'Hoeveel X in totaal?': een andere rij of een kolom heeft dezelfde som als de gevraagde rij.
  VBN-E01 tabel 'Hoeveel X meer op D1 dan op D2?': dezelfde dagen in een andere rij, een ander paar dagen in de rij, of een cel = het antwoord.
  GET-M06 'N … eerlijk verdeeld over D …': het antwoord is D.
  Elke tabel: een waarde van een foutRegel (match.waarden) is het goede antwoord.
#123/#124 (Didactiek recheck-121, besluit Dave 20:46): elke foute optie komt echt uit de route van zijn sleutel (soort van de fout-hint).
  'Hoeveel X in totaal?': één getal = een cel · andere rij = de som van een andere rij · kolom opgeteld = een kolomsom ·
  niet alles opgeteld (één vergeten) = de rijsom min één cel van de gevraagde rij · niet alles opgeteld = een som van 2 of meer (niet alle)
  cellen van de gevraagde rij · afgetrokken = een verschil van twee cellen. Een kolomsom die geen cel is, krijgt 'kolom opgeteld' (#124).
  'Hoeveel X meer op D1 dan op D2?': één getal = een cel · som van de rij = de som van de gevraagde rij · opgeteld = de twee gevraagde
  cellen opgeteld · verkeerde getallen afgetrokken = een verschil van twee cellen, niet het gevraagde paar.
#125: GET-M06 'N … eerlijk verdeeld': de getallenruimte is minstens N."""
import json, glob, os, re, sys, itertools
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'scripts'))
from fixlijst_g5b import T3, T4, M64, _bots3, _bots4, _tab
def routecheck(it, T, namen, kol, o):
    """#123/#124: komt elke foute optie uit de route van zijn soort?"""
    R, C = len(T), len(T[0]); cel = {T[r][c] for r in range(R) for c in range(C)}
    RS = [sum(x) for x in T]; KS = [sum(T[r][c] for r in range(R)) for c in range(C)]
    vers = {abs(T[a][b] - T[x][y]) for (a, b), (x, y) in itertools.combinations([(r, c) for r in range(R) for c in range(C)], 2)}
    opties = {x['tekst'] for x in it.get('opties') or []} - {it['antwoord']}
    fout = []
    if (m := T3.match(o)) and m.group(1) in namen:
        ar = namen.index(m.group(1))
        deel = {sum(T[ar][c] for c in cs) for n in range(2, C) for cs in itertools.combinations(range(C), n)}
        route = {'één getal': cel, 'andere rij': {RS[r] for r in range(R) if r != ar}, 'kolom opgeteld': set(KS),
                 'niet alles opgeteld (één vergeten)': {RS[ar] - T[ar][c] for c in range(C)}, 'niet alles opgeteld': deel, 'afgetrokken': vers}
        for f in it.get('foutHints') or []:
            if f['fout'] not in opties or not re.fullmatch(r'\d+', f['fout']): continue
            v = int(f['fout'])
            if f['soort'] in route and v not in route[f['soort']]: fout.append(f"optie {v} heet '{f['soort']}' maar komt niet uit die route")
            if v in KS and v not in cel and f['soort'] != 'kolom opgeteld': fout.append(f"optie {v} is een kolomsom maar heet '{f['soort']}' (#124)")
    elif (m := T4.match(o)) and m.group(1) in namen and m.group(2) in kol and m.group(3) in kol:
        ar, d1, d2 = namen.index(m.group(1)), kol.index(m.group(2)), kol.index(m.group(3))
        paar = {(ar, d1), (ar, d2)}; P = [(r, c) for r in range(R) for c in range(C)]
        route = {'één getal': cel, 'som van de rij': {RS[ar]}, 'opgeteld': {T[ar][d1] + T[ar][d2]},
                 'verkeerde getallen afgetrokken': {abs(T[a][b] - T[x][y]) for (a, b), (x, y) in itertools.combinations(P, 2) if {(a, b), (x, y)} != paar}}
        for f in it.get('foutHints') or []:
            if f['fout'] not in opties or not re.fullmatch(r'\d+', f['fout']): continue
            v = int(f['fout'])
            if f['soort'] in route and v not in route[f['soort']]: fout.append(f"optie {v} heet '{f['soort']}' maar komt niet uit die route")
    return fout
def run():
    uit = []
    for p in glob.glob(os.path.join(BASE, 'data/per_doel/*.json')):
        for it in json.load(open(p))['items']:
            jr = (it.get('visual') or {}).get('jsRender') or {}; o = it.get('opgave') or ''
            if jr.get('soort') == 'tabel' and jr.get('rijen'):
                namen = [r['naam'] for r in jr['rijen']]; kol = list(jr.get('kolommen') or []); T = _tab(jr)
                if (m := T3.match(o)) and m.group(1) in namen: b = _bots3(T, namen.index(m.group(1)))
                elif (m := T4.match(o)) and m.group(1) in namen and m.group(2) in kol and m.group(3) in kol:
                    b = _bots4(T, namen.index(m.group(1)), kol.index(m.group(2)), kol.index(m.group(3)))
                else: b = []
                if b: uit.append(f"{it['id']}: foute route geeft het antwoord ({', '.join(b)})")
                uit += [f"{it['id']}: {x}" for x in routecheck(it, T, namen, kol, o)]
                for f in it.get('foutRegels') or []:
                    if it['antwoord'] in ((f.get('match') or {}).get('waarden') or []): uit.append(f"{it['id']}: regel '{f['regel']}' heeft het goede antwoord als waarde")
            if (m := M64.match(o)) and divmod(int(m.group(1)), int(m.group(3)))[0] == int(m.group(3)):
                uit.append(f"{it['id']}: antwoord = het getal waarover je verdeelt ({o})")
            if (m := M64.match(o)) and int(re.sub(r'\D', '', (it.get('getallenruimte') or '0').split('–')[-1]) or 0) < int(m.group(1)):
                uit.append(f"{it['id']}: getallenruimte {it.get('getallenruimte')} is kleiner dan {m.group(1)} (#125)")
    return uit
if __name__ == '__main__':
    u = run(); print(f'#121: {len(u)} (FAIL)'); [print(' ', x) for x in u]; sys.exit(1 if u else 0)
