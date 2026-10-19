#!/bin/bash
# r23 V-#1151 / Oef-#1077: nieuwe versie van mutrun_z1142.sh (ongewijzigd daar); enige verschil: exit 1 als er één mutant gemist is.
# mutanten Z-#1142: $1 = basis; verwachte FAIL per mutant in verwacht_z1142.tsv
D=$(cd "$(dirname "$0")" && pwd); B=$1; mis=0; n=0
while IFS=$'\t' read -r m pat; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_z1142.py "$B" 2>&1)
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_z1142.tsv
echo "mutanten Z-#1142: $n, gemist $mis"
[ "${mis:-1}" = 0 ]
