#!/bin/bash
# PATCH COPY: c533d6f (r4) (zet_lenen, zet_oef1040) + Z-#1091 per somtype ($2 = somtype-mappen, standaard alle) → $1; sync + apply + check_hints
D=$(cd "$(dirname "$0")" && pwd); export SRC=${SRC:-/workspace/g8work/rc_c533d6f}
H="$D/zet_bron_1056.py"; for m in ${2:-GET-E02 GET-E05 GET-E07 GET-M04 GET-M05 GET-M06 MEET-E02 MKU-E02 VBN-E03 MEET-E06 MEET-E03 VBN-E01 VERH-E01}; do H="$H $D/$m/zet.py"; done
HOOKS="zet_lenen zet_oef1040 $H" bash /workspace/g8work/r13/z1090/r4/sbx_r2.sh "$1"
