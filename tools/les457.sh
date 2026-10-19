#!/bin/bash
# Les 457 (r21, padvrij): repo-snapshot = git archive $BASIS_COMMIT uit $REPO (beide verplicht, anders exit 2) + onze scriptmappen, zonder sbx/logs/groep*_voor.
# $1 = snapshotpad, $2 = groep (5 of 8), $3 = map met <sub>/ (komt in groep<N>/scripts/<sub>; leeg/'-' = niets erover), $4 = hooks (t.o.v. groep<N>/scripts).
# Hooks twee keer, dan sync_hint_keys + apply_hints (log: $1.apply.log), check_hints (+ merge-notatie bij G8).
set -e; export PYTHONDONTWRITEBYTECODE=1; T=$(cd "$(dirname "$0")" && pwd); . "$T/_repo.sh"
S=$1; N=$2; SCR=$3; HK=$4; [ -n "$S" ] && [[ "$N" =~ ^[58]$ ]] || fout2 "gebruik: les457.sh <snapshot> <5|8> <scriptmap|-> \"<hooks>\""
haal_basis "$S"; G=$S/claude-aanvulling/groep$N
shopt -s nullglob; if [ -n "$SCR" ] && [ "$SCR" != - ]; then [ -d "$SCR" ] || fout2 "scriptmap $SCR bestaat niet"
  for d in "$SCR"/*/; do n=$(basename "$d"); rm -rf "$G/scripts/$n"; cp -a "$d" "$G/scripts/$n"; find "$G/scripts/$n" -depth \( -name sbx -o -name '__pycache__' -o -name 'groep*_voor' \) -exec rm -rf {} + ; find "$G/scripts/$n" -name '*.log' -delete; done; fi
chmod -R u+w "$G/scripts"; cd $G
for h in $HK; do python3 -B scripts/$h "$S" | grep -v "^  " || true; done; echo "-- tweede run (snapshot):"; for h in $HK; do python3 -B scripts/$h "$S" | grep -v "^  " || true; done
python3 -B scripts/sync_hint_keys.py > $S.sync.log 2>&1; python3 -B scripts/apply_hints.py > $S.apply.log 2>&1
echo -n "snapshot check_hints: "; python3 -B check_hints.py 2>&1 | grep "^Somtypen" | tail -1
[ "$N" = 8 ] && python3 -B check_merge_notatie.py 2>&1 | tail -1
[ -n "$(find $S -name 'groep*_voor' -o -name sbx)" ] && echo "LET OP: groep*_voor/sbx in snapshot" || echo "snapshot zonder groep*_voor/sbx: ok"
