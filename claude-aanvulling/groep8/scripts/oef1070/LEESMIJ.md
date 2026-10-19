# Oef-#1070 (G8, akkoord Overzicht 19 okt) — PATCH COPY op f2a880b (na-ronde-r19; main ae59b04 heeft de r19-merge nog niet). Niet geplaatst.
`bash sbx_oef1070.sh <map>`: git archive f2a880b → zet_oef1070 (twee keer) → sync_hint_keys → apply_hints → check_hints → check_merge_notatie.
- zet_oef1070.py (batch4 GET-M01 #1–#5, batch5 MEET-E03 #1–#9; 27 entryregels, veld 'tekst'):
  «Dat is tien keer te veel[: er staat een nul te veel].» → «Dat is tien keer te groot.»; «Dat is tien keer te weinig[: er mist een nul].» → «Dat is tien keer te klein.»;
  de zin erachter blijft. 112 sleutels: GET-M01 48, MEET-E03 64. Sleutels, soort en regel ongewijzigd; G8-motor 0d5393e8 ongewijzigd.
- Niet: 'duizend keer te weinig' (GET-M01, 7 sleutels); MEET-E03 #5 'nul te weinig' (afgekapt) «Dan is er ergens een nul weggevallen. …» (14 sleutels,
  waarvan 5 geen factor tien: 256→25, 32→3, 128→12, 64→6 twee keer).
- check_oef1070.py: oude vormen weg, richting per sleutel, aantallen 48/64, guard afgekapt, duizend ongewijzigd, SNAP; 7 mutanten (mutrun_oef1070.sh).
- g8pad.py: eigen padhulp (g8(), items(), entries(), schrijf() in het formaat van het bestand).
