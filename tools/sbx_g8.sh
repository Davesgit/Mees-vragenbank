#!/bin/bash
# PATCH COPY G8 (r21, padvrij): REPO + BASIS_COMMIT (verplicht, anders exit 2) → git archive in mktemp → $1; groep8_voor = kopie vóór de hooks.
# HOOKS (paden) twee keer; dan in groep8: sync_hint_keys, apply_hints (log $1/apply.log), check_hints, check_merge_notatie.
set -e; export PYTHONDONTWRITEBYTECODE=1; T=$(cd "$(dirname "$0")" && pwd); . "$T/_repo.sh"
R=$1; [ -n "$R" ] || fout2 "zandbakmap ontbreekt (sbx_g8.sh <map>)"
haal_basis "$R" claude-aanvulling scripts; cp -a "$R/claude-aanvulling/groep8" "$R/groep8_voor"
for h in $HOOKS; do python3 -B $h "$R"; done; echo "-- tweede run:"; for h in $HOOKS; do python3 -B $h "$R" | grep -v "^  " || true; done
cd "$R/claude-aanvulling/groep8"; python3 -B scripts/sync_hint_keys.py > "$R/sync.log" 2>&1; python3 -B scripts/apply_hints.py > "$R/apply.log" 2>&1
echo -n "g8 check_hints: "; python3 -B check_hints.py 2>&1 | grep "^Somtypen" | tail -1; python3 -B check_merge_notatie.py 2>&1 | tail -1
