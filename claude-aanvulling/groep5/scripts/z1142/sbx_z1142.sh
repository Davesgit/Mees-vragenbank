#!/bin/bash
# PATCH COPY: f67d28d (na-ronde-z1136; main nog niet gemerged) + Z-#1142 → $1; sync + apply + check_hints (hooks twee keer)
D=$(cd "$(dirname "$0")" && pwd); export SRC_COMMIT=${SRC_COMMIT:-cbc6d2f}   # V-#1141: basis via git archive uit deze repo (of SRC=<map>)
HOOKS="$D/zet_z1142.py" bash $D/../z1090/r4/sbx_r2.sh "$1"
