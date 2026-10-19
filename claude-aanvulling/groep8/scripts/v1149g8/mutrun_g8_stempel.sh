#!/bin/bash
# mutanten check_g8_stempel.py (V-#1149 G8, r23): $1 = basis, APPLYLOG = G8-apply-log; exit 1 als er één gemist is (Oef-#1077).
D=$(cd "$(dirname "$0")" && pwd); B=$1; mis=0; n=0
[ -n "$APPLYLOG" ] || { echo "mutrun: zet APPLYLOG"; exit 2; }
while IFS=$'\t' read -r m pat; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_g8_stempel.py "$B" 2>&1); e=$?
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif [ "$e" = 1 ] && echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m (exit $e)"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_g8_stempel.tsv
echo "mutanten V-#1149 G8: $n, gemist $mis"
[ "$mis" = 0 ]
