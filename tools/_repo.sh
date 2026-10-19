# r21 (Oefeningen): gedeeld stuk voor de tools. Geen vaste paden: REPO (git-repo, alleen gelezen) en BASIS_COMMIT komen uit de omgeving.
# haal_basis <doel> [paden…]: git archive $BASIS_COMMIT uit $REPO in een mktemp-map, dan naar <doel>. Fout in de instelling = exit 2.
fout2() { echo "FAIL instelling: $*" >&2; exit 2; }
[ -n "$REPO" ] || fout2 "REPO is niet gezet (REPO=<pad naar de git-repo van de vragenbank>)"
[ -n "$BASIS_COMMIT" ] || fout2 "BASIS_COMMIT is niet gezet (bv. BASIS_COMMIT=9f157d8 of een branch-tip)"
git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1 || fout2 "REPO=$REPO is geen git-repo"
git -C "$REPO" rev-parse --verify -q "$BASIS_COMMIT^{commit}" >/dev/null || fout2 "BASIS_COMMIT=$BASIS_COMMIT bestaat niet in $REPO"
haal_basis() { local doel=$1; shift; local t; t=$(mktemp -d); git -C "$REPO" archive "$BASIS_COMMIT" "$@" | tar -x -C "$t" || fout2 "git archive $BASIS_COMMIT mislukt"
  rm -rf "$doel"; mkdir -p "$(dirname "$doel")"; mv "$t" "$doel"; chmod -R u+w "$doel"; }
