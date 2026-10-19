# V-#1144 (tooling, les 459) — check_z1121_v2.py, PATCH COPY op f2a880b (na-ronde-r19). Niet geplaatst. check_z1121.py (698c5008) blijft zoals hij is.
- APPLYLOG verplicht: ontbreekt / bestaat niet / onvolledig (geen 'G5-GET-M03: … bijgewerkt', 'G5-MEET-E07: …', 'items: …', 'ronde 10: …') /
  ouder dan hints/batch2.json of batch6.json → 'FAIL applylog …', 'check Z-#1121: FAIL 1 (totaal)', exit 2. Anders zoals v1 (exit 1 bij FAIL).
- Mutanten (mutrun_z1121_v2.sh, verwacht_z1121_v2.tsv: patroon + exitcode): de vijf van v1 (M_motor, M_letterlijk, M_tekst, M_teller, M_snap) en zes
  op de invoer: M_log (kopie van de log met een 'regel niet te lezen'-regel voor MEET-E07 erin → exit 1), M_geenlog, M_log_weg, M_log_leeg,
  M_log_kapot (alleen de eerste 3 regels), M_log_oud (mtime 10^7 s terug) → exit 2. De nep-FAIL van v1-M_log zit niet in v2.
- Snap: dezelfde snap_z1121.json (4e4d1617) als v1.
