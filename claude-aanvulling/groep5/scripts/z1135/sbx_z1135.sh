#!/bin/bash
# PATCH COPY: ae59b04 (main) + Z-#1135 → $1; sync + apply + check_hints (hooks twee keer). Basis via git archive uit deze repo (SRC_COMMIT) of SRC=<map>.
D=$(cd "$(dirname "$0")" && pwd); export SRC_COMMIT=${SRC_COMMIT:-ae59b04}
HOOKS="$D/zet_z1135.py" bash $D/../z1090/r4/sbx_r2.sh "$1"
