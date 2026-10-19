#!/bin/bash
# mutanten check_v1150_v2.py (r24, V-#1152/V-#1153): $1 = basis (na sync + apply); verwachte FAIL per mutant in verwacht_v1150_v2.tsv. Oef-#1077: exit 1 als er één gemist is.
D=$(cd "$(dirname "$0")" && pwd); B=$1; mis=0; n=0
[ -d "$B" ] || { echo "mutrun: geen basis"; exit 2; }
while IFS=$'\t' read -r m pat; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_v1150_v2.py "$B" 2>&1); e=$?
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif [ "$e" != 0 ] && echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m (exit $e)"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_v1150_v2.tsv
echo "mutanten check_v1150_v2: $n, gemist $mis"
[ "$mis" = 0 ]
