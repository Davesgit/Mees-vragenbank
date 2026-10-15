# Z-#1142 — PATCH COPY (niet geplaatst) op f67d28d (na-ronde-z1136; main had de merge om 18:31 nog niet: main = 122822e)
- zet_z1142.py: (a) fout_regels.compile_regel: '(sleutel hele euro)' / '(sleutel met centen)' achter een regel; (b) GET-E06 #1/#2: soort
  'centen te veel/weinig (10 cent, hele euro)' (regel '… (sleutel hele euro)') vóór de 10-cent-soort: «Dat is te veel/te weinig. Kijk goed naar de centen: die mis je nog.»
  71 sleutels (36 te veel, 35 te weinig); ±1 cent en sleutels met komma ongewijzigd; totaal 4189 sleutels blijft.
- check_z1142.py (motor, soort/komma/heel/richting per sleutel, SNAP, totaal FAIL), verwacht_z1142.tsv (5 mutanten), mutrun_z1142.sh, sbx_z1142.sh.
- Les 457: getest op een repo-snapshot (git archive f67d28d + scripts/z1091, z1136, z1142; geen sbx/groep5_voor) en op een git-clone (BASIS_REPO via rev-parse).
