#!/bin/bash
# PATCH COPY: 122822e (main, met Z-#1091 v4) + Z-#1136 → $1; sync + apply + check_hints (hooks twee keer)
D=$(cd "$(dirname "$0")" && pwd); export SRC=${SRC:-/workspace/g8work/rc_122822e}
HOOKS="$D/zet_z1136.py" bash /workspace/g8work/r13/z1090/r4/sbx_r2.sh "$1"
