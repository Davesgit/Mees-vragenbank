# Z-#1136 zichtbare resten — PATCH COPY (niet geplaatst) op 122822e (main, met Z-#1091 v4); git archive uit /workspace/mees-z1090, alleen gelezen
- zet_z1136.py: GET-E06 #1/#2 'centen ernaast' → 4 soorten (± 1 cent: laatste cijfer achter de komma; ± 10 cent: eerste cijfer), richting per item via de sleutel;
  geen muntvorm (geen jsRender.munten in GET-E06). GET-M06 #3/#6 'nog een hele ronde' → «Daar kun je nog verder mee verdelen.»
- MEET-E07 #3–#5: kindteksten noemen al geen bedrag (alleen soortlabels); geen wijziging, wel guard + mutant M_euro. MEET-E06 #15: al zonder bedrag sinds v4 («Kijk naar de hele uren.»).
- check_z1136.py (richting/plek per item, bijna, bedrag, SNAP), verwacht_z1136.tsv (6 mutanten), scan_z1136.py (les 450).
- Draaien: bash sbx_z1136.sh <map>; python3 check_z1136.py <map>; bash mutrun_z1136.sh <map>.
## V-#1141 (18:31): bedrag_lib uit ../z1091; altijd 'FAIL N (totaal)' (vóór de hook: 1322, niet 30); naast Z-#1142: sleutel zonder komma met «die mis je nog» is goed, 'hele euro'-soorten in snap_z1142.
