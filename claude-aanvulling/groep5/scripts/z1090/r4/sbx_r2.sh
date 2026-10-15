#!/bin/bash
# PATCH COPY-zandbak ronde 2 Z-#1090 (Oef-#1040, lenen/onthouden, Z-#1092) bovenop na-ronde-z1090. $1 = map; SRC = uitgepakte commit
# (`git archive`, standaard rc_91155a2). Indeling als de repo (claude-aanvulling/groep5 + scripts/merge). sync/apply + imports uit
# claude-merge/r13/g5/scripts (alleen gelezen, alleen wat de repo niet heeft). Hooks twee keer; sync + apply + check_hints.
set -e; export PYTHONDONTWRITEBYTECODE=1; unset OVERLAY; D=$(cd "$(dirname "$0")" && pwd); R=$1
# V-#1141: geen live paden; zonder SRC een git archive van SRC_COMMIT (standaard HEAD) uit deze repo
if [ -z "$SRC" ]; then TOP=$(git -C "$D" rev-parse --show-toplevel); SRC=$(mktemp -d); git -C "$TOP" archive ${SRC_COMMIT:-HEAD} claude-aanvulling/groep5 scripts | tar -x -C "$SRC"; fi
G=$R/claude-aanvulling/groep5
rm -rf "$R"; mkdir -p $R/claude-aanvulling; cp -a $SRC/claude-aanvulling/groep5 $G; cp -a $SRC/scripts $R/scripts
cd $G; python3 -B scripts/sync_hint_keys.py > $R/sync0.log 2>&1; python3 -B scripts/apply_hints.py > $R/apply0.log 2>&1
cp -a $G $R/groep5_voor
for h in ${HOOKS:-zet_lenen zet_oef1040}; do python3 -B $([[ $h == /* ]] && echo $h || echo $D/$h.py) $R; done
echo "-- tweede run:"; for h in ${HOOKS:-zet_lenen zet_oef1040}; do python3 -B $([[ $h == /* ]] && echo $h || echo $D/$h.py) $R | rg -v "^  "; done
python3 -B scripts/sync_hint_keys.py > $R/sync.log 2>&1; python3 -B scripts/apply_hints.py > $R/apply.log 2>&1
echo -n "g5 check_hints: "; python3 -B check_hints.py > $R/check_hints.log 2>&1 || true; rg "^Somtypen" $R/check_hints.log | tail -n 1
