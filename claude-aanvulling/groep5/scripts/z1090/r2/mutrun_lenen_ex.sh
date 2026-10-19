#!/bin/bash
# r23 V-#1151 / Oef-#1077: nieuwe versie van mutrun_lenen.sh (ongewijzigd daar); enige verschil: exit 1 als er één mutant gemist is.
# mutanten check_lenen.py: $1 = toegepaste zandbak; elke mutant moet een FAIL geven die past op zijn patroon (verwacht_lenen.tsv); crash = gemist
D=$(cd "$(dirname "$0")" && pwd); mis=0; n=0
while IFS=$'\t' read -r m pat; do n=$((n+1)); out=$(MUT=$m python3 -B $D/check_lenen.py "$1" 2>&1)
  if echo "$out" | grep -q Traceback; then echo "MIS $m (crash)"; mis=$((mis+1)); elif echo "$out" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m"; echo "$out" | tail -2; mis=$((mis+1)); fi
done < $D/verwacht_lenen.tsv; echo "mutanten: $n, gemist $mis"
[ "${mis:-1}" = 0 ]
