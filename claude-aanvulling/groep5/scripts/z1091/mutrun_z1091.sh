#!/bin/bash
# mutanten Z-#1091 per somtype: $1 = somtype-map (bv. GET-M05), $2 = basis; verwachte FAIL per mutant in <map>/verwacht.tsv
D=$(cd "$(dirname "$0")" && pwd); M=$1; B=$2; mis=0; n=0
while IFS=$'\t' read -r m pat; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_z1091.py G5-$M "$B" 2>&1)
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/$M/verwacht.tsv
echo "mutanten $M: $n, gemist $mis"
