#!/bin/bash
# Repo-checks G5 op een les-457-snapshot $1 (apply-log $1.apply.log). Alleen lezen. REPO verplicht (z1091 haalt zijn basis Z1091_BASIS, standaard
# ec3a77e, uit REPO); BASIS_COMMIT verplicht (alleen voor _repo.sh-controle). Één regel per check.
T=$(cd "$(dirname "$0")" && pwd); . "$T/_repo.sh"; S=$1; [ -d "$S/claude-aanvulling/groep5" ] || fout2 "geen snapshot: $S"
cd $S/claude-aanvulling/groep5; export PYTHONDONTWRITEBYTECODE=1; L=$S.apply.log
for c in z1090/check_z1090 z1090/r4/check_lenen z1090/z1092/check_z1092 z1135/check_z1135 z1136/check_z1136 z1142/check_z1142 v1145/check_v1145 z1146/check_z1146 z1121/check_z1121 z1121/check_z1121_v2; do
  [ -f scripts/$c.py ] && { echo -n "$c: "; APPLYLOG=$L python3 -B scripts/$c.py $S 2>&1 | tail -1; }; done
echo -n "check_v1012: "; python3 -B scripts/check_v1012.py $PWD 2>&1 | tail -1
echo -n "z1091: "; for d in $(ls -d scripts/z1091/*/ | xargs -n1 basename); do echo -n "$d $(BASIS_COMMIT=${Z1091_BASIS:-ec3a77e} BASIS_REPO=$REPO python3 -B scripts/z1091/check_z1091.py G5-$d $S 2>&1 | tail -1 | grep -oE 'FAIL [0-9]+|Error.*') · "; done; echo
echo -n "check_merge_notatie: "; python3 -B check_merge_notatie.py 2>&1 | tail -1
