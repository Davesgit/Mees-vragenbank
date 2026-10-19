#!/bin/bash
# Oef-#1070 op een G8-zandbak (r21, padvrij): sbx_g8.sh met HOOKS = zet_oef1070.py uit OEF1070_DIR (map met de Oef-#1070-scripts);
# zonder OEF1070_DIR die uit de basis zelf (groep8/scripts/oef1070, bv. op na-ronde-r20). Geen van beide: exit 2.
set -e; T=$(cd "$(dirname "$0")" && pwd); . "$T/_repo.sh"; R=$1; [ -n "$R" ] || fout2 "zandbakmap ontbreekt (sbx_oef1070.sh <map>)"
if [ -n "$OEF1070_DIR" ]; then Z="$OEF1070_DIR/zet_oef1070.py"; [ -f "$Z" ] || fout2 "OEF1070_DIR=$OEF1070_DIR heeft geen zet_oef1070.py"
else git -C "$REPO" cat-file -e "$BASIS_COMMIT:claude-aanvulling/groep8/scripts/oef1070/zet_oef1070.py" 2>/dev/null || fout2 "geen OEF1070_DIR en $BASIS_COMMIT heeft geen groep8/scripts/oef1070"
     Z="$R/claude-aanvulling/groep8/scripts/oef1070/zet_oef1070.py"; fi
HOOKS="$Z" bash "$T/sbx_g8.sh" "$R"
