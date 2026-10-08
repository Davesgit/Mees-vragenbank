# hints/ (G5) — nog leeg

Zelfde formaat als `g4/hints/batch*.json`. Neem per somtype `nrOrigineel` + `somtypeOrigineel` over uit de regel **Sleutel** in `somtypen/<doel>.md`.
Daarna: `python3 scripts/build_g5.py` (draait `sync_hint_keys.py` en `apply_hints.py`) en `python3 check_hints.py`.
Regeltypes voor fout-hints: zie `scripts/fout_regels.py` (ook de nieuwe `fout = antwoord ± getal1` en `fout = eenheden als antwoord`).
