#!/bin/bash
# mutanten check_z1121_v3 (V-#1144 + V-#1149, r22 ronde 4; ook mutanten die moeten SLAGEN: patroon op de slotregel, exit 0): $1 = basis, APPLYLOG = de apply-log van die basis; per mutant: FAIL-patroon én exitcode (verwacht_z1121_v3.tsv)
D=$(cd "$(dirname "$0")" && pwd); B=$1; mis=0; n=0
[ -n "$APPLYLOG" ] || { echo "mutrun: zet APPLYLOG"; exit 2; }
while IFS=$'\t' read -r m pat ec; do
  n=$((n+1)); out=$(MUT=$m python3 -B $D/check_z1121_v3.py "$B" 2>&1); e=$?
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif echo "$out" | grep -E "^(FAIL|check Z-#1121: FAIL)" | grep -qE "$pat" && [ "$e" = "$ec" ]; then echo "ok  $m (exit $e)"; else echo "MIS $m (exit $e, verwacht $ec)"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_z1121_v3.tsv
echo "mutanten Z-#1121 v3: $n, gemist $mis"
