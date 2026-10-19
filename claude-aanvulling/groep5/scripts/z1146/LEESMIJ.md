# Z-#1146 (Didactiek) — PATCH COPY op f2a880b (na-ronde-r19). Niet geplaatst.
- zet_z1146.py: G5 «Hoeveel keer zo klein is een <klein> als een <groot>?» / «Hoeveel keer zo groot is een <groot> als een <klein>?» →
  «Hoeveel <klein> gaat er in één <groot>?». 9 entryregels (batch4: MEET-E01 #1–#4, MEET-E04 #2/#4, MEET-E05 #1/#3; MEET-E01 #2 twee keer:
  'nul te veel' en 'nul vergeten', daar stond de 'zo groot'-vorm), 149 itemsleutels. Varianten: zie het rapport.
- check_z1146.py: oude vorm weg (G5 entry + item), maten uit één reeks, grote maat groter, beide maten in de opgave, aantallen per somtype, SNAP; 6 mutanten.
- ../z1135 (r20-versie): check_z1135.py kent de nieuwe kijkzin (KIJK2; mutanten M_eenheid/M_volgorde op de nieuwe vorm); snap_z1135.json ververst:
  alleen de 9 kijkzinnen (746398e8 is de V-#1145-ronde; deze ronde gaat uit van de repo-snap 4f51efb7 → 11d98fcf).
