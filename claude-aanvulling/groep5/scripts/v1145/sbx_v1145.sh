#!/bin/bash
# PATCH COPY: f2a880b (na-ronde-r19) + V-#1145 → $1; sync + apply + check_hints (hooks twee keer; via ../z1090/r4/sbx_r2.sh). SRC_COMMIT of SRC=<map>.
D=$(cd "$(dirname "$0")" && pwd); export SRC_COMMIT=${SRC_COMMIT:-f2a880b}
HOOKS="$D/zet_v1145.py" bash $D/../z1090/r4/sbx_r2.sh "$1"
