#!/bin/bash
# r23 V-#1151 (Oefeningen): G5-repo-checks op een les-457-snapshot $1 (apply-log $1.apply.log, of APPLYLOG=<pad>). Alleen lezen. Nieuwe versie van
# g5checks.sh (ongewijzigd): de LIJST komt uit de ACTIEVE regels van tools/mutrun_all.tsv (of MUTRUN_LIJST): per actieve regel onder
# claude-aanvulling/groep5/ de check(s) die dat mutantenscript aanroept (check_*.py / guard_*.py in zijn map). 'uit'-regels vallen weg.
# Vast erbij (geen mutantenscript): check_hints, check_merge_notatie, scripts/check_v1012.py. z1091: per somtypemap (zoals g5checks.sh).
# Eén regel per check: 'ok' of 'FAIL'. FAIL = een regel die met 'FAIL' begint, 'FAIL N', 'N FAIL' of 'N (FAIL)' met N > 0, Traceback/Error, of exit ≠ 0.
# Exit 0 = alles ok; 1 = minstens één FAIL; 2 = instelling (geen snapshot/lijst/log, REPO/BASIS_COMMIT, zie _repo.sh).
T=$(cd "$(dirname "$0")" && pwd); . "$T/_repo.sh"; S=${1:-}; [ -n "$S" ] && [ -d "$S/claude-aanvulling/groep5" ] || fout2 "geen snapshot: '$S'"
S=$(cd "$S" && pwd); LIJST=${MUTRUN_LIJST:-$S/tools/mutrun_all.tsv}; [ -f "$LIJST" ] || fout2 "geen lijst $LIJST"
L=${APPLYLOG:-$S.apply.log}; [ -f "$L" ] || fout2 "geen apply-log $L (les457.sh schrijft <snapshot>.apply.log)"
G=$S/claude-aanvulling/groep5; cd "$G"; export PYTHONDONTWRITEBYTECODE=1; nf=0; nc=0
oordeel() {   # $1 = naam, $2 = uitvoer, $3 = exit
  local s; s=$(printf '%s\n' "$2" | grep -vE '^\s*$' | tail -1 | cut -c1-150); nc=$((nc+1))
  if [ "$3" != 0 ] || printf '%s\n' "$2" | grep -qE 'Traceback|^[A-Za-z]*Error\b' || printf '%s\n' "$2" | grep -qE '^FAIL\b|\bFAIL [1-9]|\b[1-9][0-9]* FAIL\b|\b[1-9][0-9]* \(FAIL\)'; then
    echo "FAIL $1 [exit $3]: $s"; nf=$((nf+1)); else echo "ok   $1: $s"; fi; }
# de checks uit de actieve regels
CH=$(awk -F'\t' '!/^#/ && NF >= 3 && $3 !~ /^uit / && $2 ~ /^claude-aanvulling\/groep5\// {print $2}' "$LIJST" | while read -r p; do
  [ -f "$S/$p" ] || { echo "ONTBREEKT:$p"; continue; }
  for c in $(grep -oE '\b(check|guard)_[A-Za-z0-9_]+\.py\b' "$S/$p" | sort -u); do d=$(dirname "${p#claude-aanvulling/groep5/}"); [ -f "$d/$c" ] && echo "$d/$c" || echo "ONTBREEKT:$d/$c"; done; done | awk '!z[$0]++')
[ -n "$CH" ] || fout2 "geen actieve G5-regels in $LIJST"
for c in $CH; do
  case "$c" in ONTBREEKT:*) echo "FAIL ${c#ONTBREEKT:}: bestaat niet in de snapshot"; nf=$((nf+1)); nc=$((nc+1)); continue;; esac
  if [ "$(basename "$c")" = check_z1091.py ]; then
    for d in $(ls -d "$(dirname "$c")"/*/ | xargs -n1 basename | grep -v __pycache__); do
      o=$(BASIS_COMMIT=${Z1091_BASIS:-ec3a77e} BASIS_REPO=$REPO python3 -B "$c" "G5-$d" "$S" 2>&1); oordeel "$c G5-$d" "$o" $?; done; continue; fi
  o=$(APPLYLOG=$L python3 -B "$c" "$S" 2>&1); oordeel "$c" "$o" $?
done
o=$(python3 -B check_hints.py 2>&1); e=$?; printf '%s\n' "$o" | grep -q 'ALLES OK' || e=${e/#0/1}; oordeel "check_hints (vast)" "$(printf '%s\n' "$o" | grep '^Somtypen' | tail -1)" $e
o=$(python3 -B check_merge_notatie.py 2>&1); oordeel "check_merge_notatie (vast)" "$o" $?
o=$(python3 -B scripts/check_v1012.py "$G" 2>&1); oordeel "scripts/check_v1012.py (vast)" "$o" $?
echo "g5checks v2: $nc checks, FAIL $nf (lijst: $(basename "$LIJST"))"
[ $nf = 0 ]
