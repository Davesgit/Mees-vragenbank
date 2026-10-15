# z1091_v3 — PATCH COPY (niet geplaatst), basis 586d425 + r4; uit bevroren z1091_v2
- Oef-#1058: MEET-E06 #1 (grote wijzer één getal verder → verder/minder ver) en #6 (dag te ver/kort geteld → richting) ; check richting-dag (maandgrens) + M_dag6.
- Les 450-scan (scan_l450.py): resterende foutreactie-bedragen herschreven: GET-E05 tiental te hoog/laag, GET-M05 groepje, GET-M06 tafel,
  MEET-E02 lange/korte zijde, MEET-E06 zestig minuten / streepje / getal, VBN-E01 streepje (nieuw in SCOPE), VERH-E01 koekje (nieuw in SCOPE),
  VBN-E03 #2 item 003 «één plek te ver» (bron-hook zet_bron_1056, mutant M_plek). 'Bijna!' weg.
- Niet aangeraakt: werkwijzezinnen, coördinaten (plek N), r4 lenen/onthouden, 'een nul te veel' (Oef-#1059), extraVelden/claudeTekst/soort/waarom (herkomst; Oef-#1060).
- Snaps ververst: GET-E05 GET-M05 GET-M06 MEET-E02 MEET-E06 (+nieuw VBN-E01 VERH-E01).
- 17:35: basis 586d425 + r4 (c533d6f niet beschikbaar in de box). GET-E05 #7 leenH 'geleend'-sleutels (15) zeggen al 'Dat is te veel. …';
  nieuwe guard 'leen-bedrag' (alle lenen/onthouden-fout­teksten, geen bedrag) + mutant M_leenH.
