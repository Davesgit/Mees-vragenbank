# hints/ (G6) — nog leeg

Zelfde formaat als `g4/hints/batch*.json`. Neem per somtype `nrOrigineel` + `somtypeOrigineel` over uit de regel **Sleutel** in `somtypen/<doel>.md`.
Daarna: `python3 scripts/build_g6.py` (draait `sync_hint_keys.py` en `apply_hints.py`) en `python3 check_hints.py`.
Regeltypes voor fout-hints: zie `scripts/fout_regels.py`. Nieuw sinds G5: klokregels, kalender, tabel (`fout = andere cel`, `som van de rij/kolom`), `fout = antwoord gedeeld door getal1`, en teksten met `[getal1]`, `[getal2]`, `[antwoord]` die per item worden ingevuld.
G6-notatie in hints: ':' als deelteken mag, 'a : b' als verhouding niet (G7), ketensommen voluit ('… = 28 en 28 + 12 = 40'), geen procent, hoogstens 2 cijfers achter de komma.
