#!/bin/bash
# alle mutanten van b6/check.py via de generieke loper ../mutrun.py (Z-#961, les 360): elke mutant moet een NIEUWE FAIL-regel geven
# die past op zijn eigen verwachte melding (b6/verwacht.tsv of de standaardtabel in mutrun.py); crash = gemist. Mutanten: ontdekt in check.py.
_a=(); for x in "$@"; do if [ -e "$x" ]; then _a+=("$(realpath "$x")"); else _a+=("$x"); fi; done; set -- "${_a[@]}"   # Z-#932: relatieve paden absoluut vóór de cd
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
python3 -B ../mutrun.py "$PWD" -- "$@"
