#!/bin/bash
# mutanten V-#1081 andere kant: $1 = uitvoer van zet_andere_kant.py, $2 = het concept zonder hook (origineel); elke mutant moet zijn eigen FAIL geven (verwacht_andere_kant.tsv)
D=$(cd "$(dirname "$0")" && pwd); U=$(realpath "$1"); [ -n "$2" ] || { echo "gebruik: $0 <uit.json> <concept zonder hook> (Oef-#1051; bv. git show b7e4794:claude-aanvulling/r13/kritisch_concept_g6.json)"; exit 2; }; O=$(realpath "$2"); mis=0; n=0; T=$(mktemp -d)
while IFS=$'\t' read -r m pat; do
  n=$((n+1))
  case $m in
    M_snap) python3 -c "import json,sys;d=json.load(open('$U'));x=next(x for x in d['items'] if 'oefeningen1081' in x);x['conceptHints']['H2']+=' ';k=x['oefeningen1081']['andereKant']['nieuw'];x['conceptHints']['L1'][k]+=' Kijk goed.';json.dump(d,open('$T/s.json','w'),ensure_ascii=False)"; out=$(python3 -B $D/check_andere_kant.py $T/s.json $O 2>&1);;
    M_rang) ANDERE_KANT_ALLE=1 python3 -B $D/zet_andere_kant.py $O $T/r.json >/dev/null; out=$(python3 -B $D/check_andere_kant.py $T/r.json $O 2>&1);;
    *) out=$(MUT=$m python3 -B $D/check_andere_kant.py "$U" $O 2>&1);;
  esac
  if echo "$out" | grep -qE "Traceback"; then echo "MIS $m (crash)"; mis=$((mis+1))
  elif echo "$out" | grep -E "^FAIL" | grep -qE "$pat"; then echo "ok  $m"; else echo "MIS $m"; echo "$out" | tail -3; mis=$((mis+1)); fi
done < $D/verwacht_andere_kant.tsv
rm -rf $T; echo "mutanten: $n, gemist $mis"
