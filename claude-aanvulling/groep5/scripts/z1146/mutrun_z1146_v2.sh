#!/bin/bash
# mutanten Z-#1146 v2 (r22, na Z-#1147): $1 = basis; verwachte FAIL per mutant in verwacht_z1146_v2.tsv
D=$(cd "$(dirname "$0")" && pwd); B=$1; mis=0; n=0
while IFS=$'\t' read -r m pat; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_z1146_v2.py "$B" 2>&1)
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_z1146_v2.tsv
echo "mutanten Z-#1146: $n, gemist $mis"
