#!/bin/bash
# PATCH COPY: ae59b04 (main; Z-#1090 r4 en Oef-#1040 zitten er al in) + zet_z1092 → $1; sync + apply + check_hints (hooks twee keer; via ../r4/sbx_r2.sh).
# Basis via git archive uit deze repo (SRC_COMMIT) of SRC=<map>.
D=$(cd "$(dirname "$0")" && pwd); export SRC_COMMIT=${SRC_COMMIT:-ae59b04}
HOOKS="$D/zet_z1092.py" bash $D/../r4/sbx_r2.sh "$1"
