# Z-#1090 ronde 2: lenen/onthouden per item (V-#1120, Oef-#1045/#1046) + Oef-#1040. Voorwaardelijk, NIET geplaatst.
Basis: na-ronde-z1090 91155a2 (git archive → /workspace/g8work/rc_91155a2). Volgorde: zet_lenen.py → zet_oef1040.py → sync_hint_keys → apply_hints.
- zet_lenen.py <basis>: per fout-hint met een leen-/onthoudzin en een gemengd somtype: splitsen zoals G6-GET-E04 (motor #399/#392):
  '<soort> (geleend)' regel + ' (geleend bij de tientallen)' / '<soort> (onthouden)' regel + ' (onthouden naar de tientallen|honderdtallen)' met de
  oude tekst, daarna de gewone soort met «Dat is te veel. Haal de tientallen nog eens af.» / «Dat is te weinig. Tel de tientallen (honderdtallen) nog eens bij elkaar.»
- zet_oef1040.py <basis>: GET-E05 #17 'honderdtal vergeten' (− 10) → 'tiental te weinig' «Dat is te weinig. Tel de tientallen nog eens bij elkaar.»
- check_lenen.py <basis> [MUT=, SNAP=1]: per itemsleutel, los van de motor nagerekend (lenen_lib.som); SNAP per item snap_lenen.json.
- mutrun_lenen.sh <basis>: 6 mutanten (lenen zonder lenen, onthouden zonder onthouden ×2, 1040 ×2, SNAP).
- sbx_r2.sh <map>: PATCH COPY-zandbak (SRC=<git archive>, HOOKS="zet_lenen zet_oef1040").
