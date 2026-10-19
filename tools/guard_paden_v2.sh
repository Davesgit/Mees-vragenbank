#!/usr/bin/env bash
# Guard r22 (Oefeningen, Oef-#1077): geen vaste paden in UITVOERBARE code van de HELE repo.
# Gebruik: bash tools/guard_paden_v2.sh [repo-map]   (standaard: de repo van dit script)
# - Zoekt in *.py *.sh *.js *.mjs *.ts naar een absoluut pad onder de vier verboden wortels (zie PAT; ook zonder slash erna, bv. een
#   string die alleen de wortel is). Documentatie (*.md, *.txt, *.tsv, *.json, *.csv, *.diff, *.patch) telt niet: dat zijn verslagen, niet uitgevoerd.
# - Elke treffer moet in tools/guard_paden_v2_uitz.tsv staan (bestand <TAB> ERE op de regel <TAB> reden). Anders FAIL.
# - Uitzondering zonder treffer = WARN (verouderd). Exit 0 = schoon, 1 = FAIL, 2 = instelling (map of lijst ontbreekt).
set -u
D=$(cd "$(dirname "$0")" && pwd)
R=${1:-$(cd "$D/.." && pwd)}
U=${GUARD_UITZ:-$D/guard_paden_v2_uitz.tsv}
[ -d "$R" ] || { echo "FAIL instelling: geen map $R"; exit 2; }
[ -f "$U" ] || { echo "FAIL instelling: geen uitzonderingenlijst $U"; exit 2; }
W='work''space|t''mp|ho''me|cur''sor'
PAT="(^|[^A-Za-z0-9_.~-])/($W)([^A-Za-z0-9_-]|\$)"
cd "$R" || exit 2
treffers=$(grep -rnIE "$PAT" --include='*.py' --include='*.sh' --include='*.js' --include='*.mjs' --include='*.ts' . | sed 's|^\./||' | LC_ALL=C sort)
fail=0; uitz=0; gebruikt=$(mktemp); trap 'rm -f "$gebruikt"' EXIT
while IFS= read -r t; do
  [ -n "$t" ] || continue
  f=${t%%:*}; rest=${t#*:}; regel=${rest#*:}; ok=
  while IFS=$'\t' read -r uf ure ureden; do
    case "$uf" in ''|'#'*) continue;; esac
    if [ "$uf" = "$f" ] && printf '%s\n' "$regel" | grep -qE -- "$ure"; then ok=1; printf '%s\t%s\n' "$uf" "$ure" >> "$gebruikt"; break; fi
  done < "$U"
  if [ -n "$ok" ]; then uitz=$((uitz+1)); else echo "FAIL vast pad: ${t:0:220}"; fail=$((fail+1)); fi
done <<< "$treffers"
while IFS=$'\t' read -r uf ure ureden; do
  case "$uf" in ''|'#'*) continue;; esac
  grep -qxF -- "$(printf '%s\t%s' "$uf" "$ure")" "$gebruikt" || echo "WARN uitzondering zonder treffer: $uf  /$ure/"
done < "$U"
echo "guard_paden_v2: $R — FAIL $fail, uitzonderingen geraakt $uitz"
[ $fail -eq 0 ] && { echo "OK geen vaste paden buiten de uitzonderingen"; exit 0; } || exit 1
