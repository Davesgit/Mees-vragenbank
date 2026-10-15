#!/bin/bash
# PATCH COPY: 122822e (main, met Z-#1091 v4) + Z-#1136 → $1; sync + apply + check_hints (hooks twee keer)
D=$(cd "$(dirname "$0")" && pwd); export SRC_COMMIT=${SRC_COMMIT:-122822e}   # V-#1141: basis via git archive uit deze repo (of SRC=<map>)
HOOKS="$D/zet_z1136.py" bash $D/../z1090/r4/sbx_r2.sh "$1"
