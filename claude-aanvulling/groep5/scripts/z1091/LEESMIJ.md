# Z-#1091 v2 (Didactiek 17:20): kopie van bevroren z1091 + Oef-#1056/#1057 + MEET-E03 #1-kleuren. Voorwaardelijk, NIET geplaatst.
Basis: 586d425 + r4. PATCH COPY: `bash sbx_z1091.sh <map>` = zet_lenen → zet_oef1040 (r4) → zet_bron_1056.py → 11 somtype-hooks → sync → apply → check_hints; hooks 2×.
- zet_bron_1056.py: VBN-E03 #2 item 007 in per_doel én gemapt: «Je bent te vroeg gestopt. Ga na plek 5 nog twee stappen verder.» → «Dat is niet ver genoeg. Tel de stappen nog eens.» (les 369: uitleg + foutHintsTekst + foutRegels meeveranderd).
- bedrag_lib: guard vangt elk bedrag/cijfer in 'nog … verder' en 'Ga na plek N'; Oef-#1057 alleen #7 terugtellen («te ver teruggeteld» / «niet ver genoeg teruggeteld. Tel de dagen nog eens.»).
- check: bronzin Oef-#1056 per item (M_verder); richting-dag Oef-#1057 (M_dag); MEET-E03 #1 'gekleurd' alleen als vraag/interactie/tekening kleurbaar rooster is (M_kleur) — geldt voor alle 10 items.
Ongewijzigd t.o.v. z1091: Oef-#1050/#1054/#1055, V-#1052. Open: #1/#6 «één dag te veel/weinig» en «te ver/kort geteld» (niet #7) — Oef-#1058.
