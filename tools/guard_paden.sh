#!/bin/bash
# Guard r21: geen vaste paden in de tools (/workspace/, /tmp/, /home/, /cursor/). FAIL + exit 1 bij een treffer; exit 0 als schoon.
# Gebruik: guard_paden.sh [map] (standaard de map van dit script). Dit bestand zelf telt niet mee (het noemt de patronen).
D=${1:-$(cd "$(dirname "$0")" && pwd)}; P='/(work''space|t''mp|ho''me|cur''sor)/'
h=$(grep -nE "$P" "$D"/*.sh "$D"/*.py 2>/dev/null | grep -v "^$D/guard_paden.sh:")
if [ -n "$h" ]; then echo "$h" | sed 's/^/FAIL vast pad: /'; echo "guard_paden: FAIL $(echo "$h" | wc -l)"; exit 1; fi
echo "guard_paden: 0 vaste paden in $(ls "$D"/*.sh "$D"/*.py 2>/dev/null | wc -l) bestanden"
