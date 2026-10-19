#!/usr/bin/env python3
"""Hook Z-#1121 motor (VOORWAARDELIJK, niet geplaatst; G5-motor a00a0c4e → zie LEESMIJ). python3 zet_motor_z1121.py <basis>. Idempotent.
De G5-motorregel #81 'fout = het aantal munten' (het aantal munten en briefjes in jsRender.munten als euro's) werd nooit gelezen bij geld tellen:
het antwoord ('€2,60') is geen geheel getal en 'Hoeveel geld zie je?' heeft geen getallen, dus de motor stopte eerder bij
'if a is None and not n: return None'. Dit zet de #81-regel vóór die regel (zelfde code); de oude plek blijft staan (wordt dan niet meer bereikt)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'z1090', 'r4')); from g5pad import g5
P = os.path.join(g5(sys.argv[1]), 'scripts', 'fout_regels.py'); t = open(P, encoding='utf-8').read()
OUD = "    # getallen\n    if a is None and not n: return None\n"
NIEUW = ("    # Z-#1121: #81 'fout = het aantal munten' vóór de getallen-regel: bij geld tellen is het antwoord geen geheel getal en heeft de opgave geen getallen\n"
         "    if r.startswith('fout = het aantal munten'):\n"
         "        mu = c.jr.get('munten') if c.jr.get('soort') == 'geld' else None\n"
         "        if not mu: return {'exact': set()}\n"
         "        k_ = geld(len(mu) * 100)\n"
         "        return E(k_) if geld_norm(k_) != geld_norm(c.ans) else {'exact': set()}\n")
if NIEUW in t: print(f"{sys.argv[1]}: 0 wijzigingen (Z-#1121 motor)"); sys.exit(0)
assert t.count(OUD) == 1, 'ankerregel niet (precies één keer) gevonden'
open(P, 'w', encoding='utf-8').write(t.replace(OUD, NIEUW + OUD))
print(f"{sys.argv[1]}: 1 wijzigingen (Z-#1121 motor)\n  scripts/fout_regels.py: #81 'fout = het aantal munten' vóór 'if a is None and not n'")
