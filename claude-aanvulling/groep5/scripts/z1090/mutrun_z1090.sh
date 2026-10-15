#!/bin/bash
# mutanten Z-#1090 op een toegepaste zandbak ($1): elke mutant moet zijn eigen FAIL geven (verwacht_z1090.tsv) en geen andere soort FAIL; geen crash
D=$(dirname "$0"); mis=0
while IFS=$'\t' read -r m pat; do
  out=$(MUT=$m python3 -B $D/check_z1090.py "$1" 2>&1)
  if echo "$out" | rg -q "Traceback"; then echo "CRASH $m"; mis=$((mis+1))
  elif ! echo "$out" | rg -q -- "$pat"; then echo "MIS   $m"; echo "$out" | rg "^FAIL" | head -n 3; mis=$((mis+1))
  else n_eigen=$(echo "$out" | rg -c -- "$pat"); n_alle=$(echo "$out" | rg -c "^FAIL"); echo "ok    $m ($n_eigen eigen FAIL, $((n_alle-n_eigen)) andere)"; fi
done < $D/verwacht_z1090.tsv
echo "mutanten: $(wc -l < $D/verwacht_z1090.tsv), gemist $mis"
