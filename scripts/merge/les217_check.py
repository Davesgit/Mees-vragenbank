#!/usr/bin/env python3
"""[tools-kopie 8 okt 16:0x van g7work/huis_checks.py (Oefeningen), Z-#812: ook in de build-gate (check_hints G3–G8: G7/G8 FAIL, G3–G6 WARN).]
Gedeelde huisregel-checks voor alle G7-batches (Z-#741, les 243): elke b*/check.py roept les217() aan op zijn eigen hints/batchN.json.
Los te draaien over alle batches: python3 huis_checks.py [pad naar g7]  (standaard de zandbak; exit 1 bij FAIL).
les 217 (Z-#741, les 242): geen zin die een bewerking uitsluit. Herhaald optellen, kolommen optellen en 'erbij' zijn geldige routes;
een tekst mag een fout benoemen ('Heb je opgeteld?'), maar niet zeggen dat optellen nooit/niet mag. Bredere regex dan de oude frasenlijst:
ontkenning + optellen/erbij in beide volgordes ('tel je nooit iets op', 'Optellen mag niet', 'niet … erbij doen') en 'alleen delen/keer'.
Voorstel voor Overzicht: dezelfde regex in tools/ (huis_checks), zodat ook de build-gate hem draait."""
import json, re, sys, glob, os
UITSLUIT = re.compile(r"""(
    \b(tel|telt|tellen)\b[^.?!]{0,25}\b(niets|nooit|niet)\b[^.?!]{0,15}\bop\b            # tel je nooit iets op / je telt niets op
  | \b(niets|nooit|niet|geen)\b[^.?!]{0,25}\b(op\s?tellen|erbij\s(doen|tellen|optellen)|plus\sdoen)\b   # niet optellen / nooit erbij doen
  | \b(op\s?tellen|optellen|erbij\sdoen|plus)\b[^.?!]{0,15}\b(mag|kan|moet|hoeft)\s(je\s)?(hier\s)?(niet|nooit)\b      # optellen mag niet
  | \balleen\s(maar\s)?(keer|delen|gedeeld|vermenigvuldig\w*|maal)\b                         # alleen delen of keer
  | \bniet\som\serbij\b
  # Z-#812 (Didactiek recheck2-batch6): vijf gangbare bewoordingen die de oude regex miste
  | \b(niets|niet|nooit|geen)\b[^.?!]{0,25}\bop\s+te\s+tellen\b                                # je hoeft niets op te tellen
  | \b(optellen|plus)\b[^.?!]{0,15}\bis\s+(hier\s+)?(fout|verkeerd|niet\s+goed)\b             # optellen is hier fout
  | \bgeen\s+plus(som)?\b(?!teken)                                                            # gebruik geen plus / dit is geen plussom (niet: 'geen plusteken')
  | \ber\s+komt\s+niets\s+bij\b                                                              # er komt niets bij
)""", re.I | re.X)
# zelftest (Z-#812): python3 huis_checks.py --zelftest; elke FOUT-zin moet vallen, elke GOED-zin vrij blijven
ZELFTEST_FOUT = ['Bij een schaal tel je nooit iets op.', 'Optellen mag niet.', 'Je doet alleen delen of keer.', 'Je mag hier geen plus doen.',
                 'Tel nooit op bij een schaal.', 'Je telt hier niet op maar je doet keer.', 'Je hoeft niets op te tellen.', 'Optellen is hier fout.',
                 'Gebruik geen plus.', 'Er komt niets bij: het gaat om keer.', 'Dit is geen plussom.']
ZELFTEST_GOED = ['Heb je erbij opgeteld? Kijk nog eens naar de vraag.', 'Tel ze allebei nog eens.', "Achter 'op de' komt niet het deel, maar het totaal.",
                 'Het is geen plusteken.', 'Heb je opgeteld in plaats van keer gedaan?']
def zelftest():
    mis = [t for t in ZELFTEST_FOUT if not UITSLUIT.search(t)]; vals = [t for t in ZELFTEST_GOED if UITSLUIT.search(t)]
    return mis, vals
# toegestaan: een zin die zegt dat iets géén plusteken is, of 'niet één keer meer' zonder optellen (VERH-01 #7 H2, Didactiek 15:20 goed)
def teksten(st):
    yield 'hint1', st.get('hint1') or ''; yield 'hint2', st.get('hint2') or ''; yield 'ouderzin', st.get('ouderzin') or ''
    for f in st.get('foutHints') or []:
        for k in ('tekst', 'tekstSterker'): yield f"{f.get('soort') or f.get('regel') or '?'}/{k}", f.get(k) or ''
def les217(pad, extra=(), D=None):
    """FAIL-regels voor één batch: D = de batch in het geheugen van de check (zo zien mutanten op D het ook), anders de json op pad;
    extra: (doel, nro, veld, tekst) voor mutanten"""
    if not (isinstance(D, dict) and 'somtypen' in D): D = json.load(open(pad, encoding='utf-8'))
    uit = []
    rij = [(st['doel'], st['nrOrigineel'], v, t) for st in D['somtypen'] for v, t in teksten(st)] + list(extra)
    for doel, nro, v, t in rij:
        m = UITSLUIT.search(t)
        if m: uit.append(f"les 217 {doel} #{nro} {v}: sluit een bewerking uit («{m.group(0).strip()}»): {t[:80]}")
    return uit
def groep(root):
    """alle hints/batch*.json van één groep (pad naar gN) → lijst met treffers"""
    return [f for p in sorted(glob.glob(os.path.join(root, 'hints', 'batch*.json'))) for f in les217(p)]
if __name__ == '__main__':
    if '--zelftest' in sys.argv:
        mis, vals = zelftest()
        for t in mis: print('GEMIST', t)
        for t in vals: print('VALS ALARM', t)
        print(f'zelftest les 217: {len(ZELFTEST_FOUT) - len(mis)}/{len(ZELFTEST_FOUT)} gevangen, {len(vals)} vals alarm'); sys.exit(1 if mis or vals else 0)
    B = sys.argv[1] if len(sys.argv) > 1 else '/workspace/g7work/r9oef/sbx/g7'
    F = [f for p in sorted(glob.glob(f'{B}/hints/batch*.json')) for f in les217(p)]
    for f in F: print('FAIL', f)
    print(f'huis_checks G7 ({len(glob.glob(f"{B}/hints/batch*.json"))} batches): les 217 FAIL {len(F)}')
    sys.exit(1 if F else 0)
