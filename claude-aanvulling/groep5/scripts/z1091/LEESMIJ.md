# z1091_v3 — PATCH COPY (niet geplaatst), basis 586d425 + r4; uit bevroren z1091_v2
- Oef-#1058: MEET-E06 #1 (grote wijzer één getal verder → verder/minder ver) en #6 (dag te ver/kort geteld → richting) ; check richting-dag (maandgrens) + M_dag6.
- Les 450-scan (scan_l450.py): resterende foutreactie-bedragen herschreven: GET-E05 tiental te hoog/laag, GET-M05 groepje, GET-M06 tafel,
  MEET-E02 lange/korte zijde, MEET-E06 zestig minuten / streepje / getal, VBN-E01 streepje (nieuw in SCOPE), VERH-E01 koekje (nieuw in SCOPE),
  VBN-E03 #2 item 003 «één plek te ver» (bron-hook zet_bron_1056, mutant M_plek). 'Bijna!' weg.
- Niet aangeraakt: werkwijzezinnen, coördinaten (plek N), r4 lenen/onthouden, 'een nul te veel' (Oef-#1059), extraVelden/claudeTekst/soort/waarom (herkomst; Oef-#1060).
- Snaps ververst: GET-E05 GET-M05 GET-M06 MEET-E02 MEET-E06 (+nieuw VBN-E01 VERH-E01).
- 17:35: basis 586d425 + r4 (c533d6f niet beschikbaar in de box). GET-E05 #7 leenH 'geleend'-sleutels (15) zeggen al 'Dat is te veel. …';
  nieuwe guard 'leen-bedrag' (alle lenen/onthouden-fout­teksten, geen bedrag) + mutant M_leenH.
## z1091_v4 (17:52, review Didactiek op 3d95866) — PATCH COPY op c533d6f (git archive uit /workspace/mees-z1090, alleen gelezen)
- V-#1136: MEERV in bedrag_lib ('kant' → 'kanten', 'zijde' → 'zijden'); check 'woord' (woordenlijst = basis-G5 + vervangzinnen, plus 'kantn'), mutant M_woord.
- V-#1137: VERH-E01 #1 'bijna' (± 1) gesplitst in 'één te veel' / 'één te weinig' → «Dat is te veel./te weinig. Reken het na: …»; check 'bijna-zonder-richting' (entry + item, alle somtypen), mutanten M_bijna, M_bijnaI.
- V-#1139 (les 455): «Dan is er nog een tafel nodig.» / «Voor wie overblijft, is nog een tafel nodig.» → «… zijn er meer tafels nodig.»; 'nog een/één … nodig' in BEDRAG; mutant M_nodig. G5-scan: 0 over.
- Z-#1138: cijfers uit vraag/antwoord blijven; geen wijziging.
## z1091_v5 (18:12, V-#1140 / les 456) — PATCH COPY op ec3a77e (main vóór de merge van v4; git archive uit /workspace/mees-z1090, alleen gelezen)
- Rechtgezet: v4 staat op ec3a77e (niet c533d6f); 93 mutanten in v4 (niet 98); GET-M06: 25 velden in 5 items (de '13 wijzigingen' van de hook zijn entryregels).
- check_z1091: groep5_voor uit <basis>/groep5_voor, anders BASIS_COMMIT → git archive (tijdelijke map), anders FAIL + exit 2. Mutant M_geenvoor (alle 13 somtypen).
- Draaien zoals Overzicht (repo zonder groep5_voor): BASIS_COMMIT=ec3a77e python3 check_z1091.py <somtype> <repo>.
