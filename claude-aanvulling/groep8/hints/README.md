# hints/ (G8): Oefeningen

Zelfde formaat en werkwijze als `g7/hints/` (en `g4/hints/`). Opgezet op 8 okt 2026 (Oefeningen) voor G8 batch 1.
- **Koppeling:** per somtype `nrOrigineel` + `somtypeOrigineel` uit de regel **Sleutel** in `somtypen/<doel>.md`. `nr` en `somtype` houdt `scripts/sync_hint_keys.py` bij.
- **Bouwen en syncen (Overzicht):** `python3 scripts/build_g8.py` bouwt de data en draait zelf `sync_hint_keys.py` en `apply_hints.py` over alle `hints/batch*.json` (glob). Daarna `python3 check_hints.py` en `python3 check_merge_notatie.py`.
- **Motor:** `scripts/fout_regels.py` (gelijk aan die van G7, met laag 2 per fout-hint: `tekstSterker`). Regels van boven naar beneden; de eerste die past, wint. 'claude-taalfix' met `Claudes sleutel: <label>` = een vaste tekst op Claudes sleutels met dat label.
- **Schrijven:** `make_batchN.py` alleen voor de eerste versie; het weigert zodra `batchN.json` gesynct is ('koppeling'/'kopGewijzigd'). Daarna alleen `patch_batchN.py` (via `patch_lib.py`, idempotent, log in `wijzigingen_batchN.json`). Nooit `make_batchN.py --force` na een sync.
- **Checks van Oefeningen:** `/workspace/g8work/bN/check.py` (per sleutel de winnende regel en of laag 1 en laag 2 kloppen, tekstbewakers, mutanten) op een zandbak (`/workspace/g8work/bN/sbx.sh`: kopie van live g8 + de batch, dan sync, apply, check_hints, check_merge_notatie).
- **Lessen:** `lessen_g8.md` (G8-bankregels voor hints en verwijzing naar alle G4–G7-lessen). Indeling: `batches.md`.
