#!/usr/bin/env bash
# r23 V-#1151 (Oefeningen, Oef-#1077): mutrun_all v2 = v1 (r22, 5fd20949) plus: elk mutantenscript moet zelf exit ≠ 0 geven als het een mutant mist
# (gemist > 0 of MIS/CRASH met exit 0 = FAIL 'exit 0 ondanks gemist'); ook runmut*.sh moet geregistreerd zijn; geen uitzondering voor de runners
# zelf (die staan als 'uit' in de lijst). r22: ALLE mutanten van de repo in één keer. Geen vaste paden.
# Gebruik: REPO=<git-repo, alleen gelezen> bash tools/mutrun_all_v2.sh <repo-snapshot>   (git archive + rondes; wordt niet beschreven)
# - kopie van de snapshot in mktemp; daar G5 en G8 sync_hint_keys + apply_hints (logs: $L5, $L8);
# - elke regel van tools/mutrun_all.tsv (naam, script t.o.v. de repo, bash-opdracht met $S $G5 $G8 $L5 $L8 $T $REPO) draait; geteld wordt
#   'mutanten…: N' en 'gemist N' (alle regels van de uitvoer); MIS/CRASH/Traceback of gemist > 0 of een exit ≠ 0 = GEMIST;
# - elk mutrun*.sh / runmut.sh in de snapshot moet in de lijst staan (actief, of 'uit' met reden); anders FAIL 'niet geregistreerd'.  (tools/mutrun_all.sh zelf telt niet mee.)
# Exit 0 = alles gevangen; 1 = minstens één gemist / niet geregistreerd; 2 = instelling.
set -u; D=$(cd "$(dirname "$0")" && pwd); B=${1:-}; LIJST=${MUTRUN_LIJST:-$D/mutrun_all.tsv}
fout2() { echo "FAIL instelling: $*"; exit 2; }
[ -n "$B" ] && [ -d "$B/claude-aanvulling/groep5" ] && [ -d "$B/claude-aanvulling/groep8" ] || fout2 "gebruik: REPO=<repo> mutrun_all.sh <repo-snapshot met claude-aanvulling/groep5 en groep8>"
[ -f "$LIJST" ] || fout2 "geen lijst $LIJST"
[ -n "${REPO:-}" ] && git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1 || fout2 "REPO is niet gezet of geen git-repo (nodig voor Z-#1091: BASIS_REPO)"
export REPO PYTHONDONTWRITEBYTECODE=1; unset MUT SNAP APPLYLOG
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT; export S=$W/s T=$W/t; cp -a "$B" "$S"; chmod -R u+w "$S"; mkdir -p "$T"
export G5=$S/claude-aanvulling/groep5 G8=$S/claude-aanvulling/groep8 L5=$W/g5.apply.log L8=$W/g8.apply.log
for g in 5 8; do G=$S/claude-aanvulling/groep$g; ( cd "$G" && python3 -B scripts/sync_hint_keys.py > "$W/g$g.sync.log" 2>&1 && python3 -B scripts/apply_hints.py > "$W/g$g.apply.log" 2>&1 ) || { echo "FAIL sync/apply G$g (zie log)"; tail -3 "$W/g$g.apply.log"; exit 1; }; done
fail=0; tot=0; mis=0; regs=$W/reg
while IFS=$'\t' read -r naam pad cmd; do
  case "$naam" in ''|'#'*) continue;; esac
  echo "$pad" >> "$regs"
  if [ "${cmd:0:3}" = uit ]; then echo "--- $naam: uit (${cmd#uit })"; continue; fi
  [ -f "$S/$pad" ] || { echo "FAIL $naam: $pad ontbreekt in de snapshot"; fail=$((fail+1)); continue; }
  out=$(cd "$S" && bash -c "$cmd" 2>&1); e=$?
  n=$(printf '%s\n' "$out" | grep -oE '^mutanten[^:]*: [0-9]+' | grep -oE '[0-9]+$' | awk '{s+=$1} END {print s+0}')
  g=$(printf '%s\n' "$out" | grep -oE 'gemist:? [0-9]+' | grep -oE '[0-9]+$' | awk '{s+=$1} END {print s+0}')
  k=$(printf '%s\n' "$out" | grep -cE '^(MIS|CRASH)|Traceback')
  tot=$((tot+n)); st=ok
  if { [ "$g" != 0 ] || [ "$k" != 0 ]; } && [ $e = 0 ]; then echo "FAIL $naam: exit 0 ondanks gemist $g / MIS-CRASH $k (Oef-#1077: het script moet exit ≠ 0 geven)"; fail=$((fail+1)); fi
  if [ "$n" = 0 ] || [ "$g" != 0 ] || [ "$k" != 0 ] || [ $e != 0 ]; then st=GEMIST; mis=$((mis+1)); printf '%s\n' "$out" | grep -E '^(MIS|CRASH)|Traceback|gemist' | head -5 | sed 's/^/    /'; fi
  echo "--- $naam: $n mutanten, gemist $g, MIS/crash $k, exit $e → $st"
done < "$LIJST"
while IFS= read -r f; do f=${f#./}; grep -qxF "$f" "$regs" || { echo "FAIL niet geregistreerd: $f (zet hem in $(basename "$LIJST"))"; fail=$((fail+1)); }; done < <(cd "$S" && find . \( -name 'mutrun*.sh' -o -name 'runmut*.sh' \) -not -path '*/__pycache__/*' | LC_ALL=C sort)
echo "mutrun_all v2: $tot mutanten; onderdelen gemist $mis; FAIL $fail"
[ $mis -eq 0 ] && [ $fail -eq 0 ]
