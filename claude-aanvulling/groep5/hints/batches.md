# G5 Claude-merge: indeling in batches

Geschreven op 2026-10-01 om 16:00 (Amsterdam). Stand: rebuild van Overzicht om 15:58, met **131 somtypes en 4842 items**. Bij de opdracht stond 129/4818; de build van 15:25 had 130/4820. De rebuild van 15:58 heeft MEET-E06 één somtype erbij gegeven (nu 24) en VERH-E01 een tweede (nu 2).

**Bijgewerkt om 16:59:** de rebuilds van 16:39/16:40/16:55 gaven **121 somtypes en 4843 items** (fixlijst #20: E06 #4 in #3; #22: E07 #6–#17 → 2 somtypes). Batch 2 heeft nu 14 somtypes.

**Bijgewerkt om 16:20:** de rebuild van 16:13 gaf **132 somtypes en 4843 items**. Nieuw is VERH-E01 #3 ('Kleur drie kwart van de koekjes', 1 item, besluit drie kwart / fixlijst #3), in batch 6. Batch 1 en 2 veranderen daardoor niet.

- **Indeling:** in doelvolgorde, met ongeveer 20–25 somtypes per batch. Eén doel (één md-bestand) wordt nooit gesplitst.
- **GET-E08** heeft 0 somtypes. Er zijn alleen 8 twijfel-items (geld ×), zie `twijfel_voor_didactiek.md`.

| Batch | Doelen | Somtypes | Items | Stand |
|---|---|---|---|---|
| 1 | GET-E02 (4), GET-E04 (4), GET-E05 (19) | 27 | 522 | ronde 1b (16:20, Didactiek v1 'taal: fix') gepatcht via patch_batch1.py; ronde 1c (16:32, hercheck: 'niet het goede tiental' + 'precies in het midden') gepatcht; ronde 1d (17:20, #12: 'verkeerde kant' en 'één stap te ver' apart) gepatcht, review-batch1d.md |
| 2 | GET-E06 (3), GET-E07 (7), GET-M02 (3), GET-M03 (1) | 14 (was 25) | 1551 | ronde 2b (16:59, Didactiek v1 'taal: fix') gepatcht via patch_batch2.py: één entry per samengevoegd somtype (#20/#22), V1–V4, S1–S5 (S3 'andere fout' niet, #35); review-batch2b.md, fixlijst #29–#36; ronde 2c (17:20, hercheck: N1, Z1, Z2; S3_ANDERS blijft False) gepatcht, review-batch2c.md, fixlijst #44–#46; ronde 2d (17:25, dubbele 'aantal', 91/91) gepatcht, review-batch2d.md; recheck (17:35): 2c, 1d en 2d taal ok |
| 3 | GET-M04 (2), GET-M05 (12), GET-M06 (9) | 23 | 314 | hints klaar (16:59); ronde 3b (17:20, Didactiek v1 'taal: fix': V1, S1–S10, S12) gepatcht via patch_batch3.py, review-batch3b.md, fixlijst #47–#51; ronde 3c (17:36, recheck F1 M06 #7 + #66 M06 #9) gepatcht, review-batch3c.md, fixlijst #64–#67; **ronde 9 (8 okt, Oefeningen)**: #369, zie review-ronde9.md |
| 4 | MEET-E01 (5), MEET-E02 (2), MEET-E03 (1), MEET-E04 (4), MEET-E05 (3) | 15 | 553 | hints klaar (17:12); ronde 4b (17:39, Didactiek v1 'taal: fix': V1–V4, S1–S8; V5 → fixlijst #60) gepatcht via patch_batch4.py, review-batch4b.md, fixlijst #52–#63; ronde 4c (18:18, recheck 4b: #83 nagekeken, Z1 'pak melk') gepatcht, review-batch4c.md |
| 5 | MEET-E06 (24) | 24 | 1233 | hints klaar (17:48); ronde 5b (18:20–18:31, Didactiek v1 'taal: fix': V1, V2, S1–S4 + motorregels #68–#72; #88 0 FAIL/0 WARN) gepatcht via patch_batch5.py, review-batch5b.md; nog 39 Claude-sleutels op de algemene tekst; ronde 5c (18:50, #84: nieuw somtype nrOrigineel 26, nu #11, 20 generator-items, hints + 8 regels, per item nagerekend; datapunten #110/#111) via patch_batch5.py + patch_lib 'nieuwEntry', review-batch5c.md; ronde 5d (19:00, Didactiek recheck 4c/5b: V-a, V-b, V-c, Z1, #22 Hint 2; Z2 #84 bewust niet overgenomen) via patch_batch5.py, review-batch5d.md; ronde 5e (19:10, #103 'grote wijzer als uur gelezen' in 6 somtypes, niet in #4; MEET-E06 0 sleutels op de algemene tekst) review-batch5e.md; ronde 5e-2 (19:46, V-d #9 klok zetten + Z-a #84) review-batch5e.md |
| 6 | MEET-E07 (5), MKU-E02 (3), VBN-E01 (5), VBN-E03 (2), VERH-E01 (3) | 18 | 670 | hints klaar (18:04); ronde 6b (18:39, Didactiek v1 'taal: fix': V1–V3, S1, S2, S4–S8, S11; V4 via de motor #92) gepatcht via patch_batch6.py, review-batch6b.md, fixlijst #90–#99; ronde 6b-2 (19:00, Didactiek recheck-6b: 016 'zitten'; #105/#106/#109 in de data van Overzicht, check105.py) review-batch6c.md; ronde 5e: MKU #2/#3 Hint 1 begint bij 'Tel eerst' (#109); ronde 5e-2 (19:46): #117 'fout = de prijs' in MEET-E07 #2–#5 |
| 7 | GET-E05 #20–#32 (13), GET-E07 #18–#22 (5), GET-E09 #1–#2 (2) (G8→G5-aanvullingen, build 22:31:36) | 20 | 170 | hints klaar (22:55, Oefeningen): tekstSterker bij elke fout-hint (les 40, besluit #229), #253 057 letterlijk van Didactiek; ronde 7a (E05 #32 labels, E05 #23 'tiental te veel' als vraag) via patch_batch7.py; review-batch7.md, batch7_twijfels.md, check `/workspace/g5work/b7/check.py` FAIL 0; **ronde 9 (8 okt, Oefeningen)**: #350–#353, #362–#364, #367, #368, #372, zie review-ronde9.md |
| | **Totaal** | **141** | **5013** | |

## Opmerkingen
- **Batch 2** heeft veel items (GET-E06: 4 somtypes met 1060 items). Het aantal somtypes past wel. Daar zitten ook de G4-items met sprongen van 3/4 en de tafels van 8/12 die naar G5 zijn gegaan. Die controleer ik daar per item.
- **Batch 4** is klein (15). Als je dat liever hebt, kan MEET-E07 (5) erbij, zodat batch 6 dan 12 somtypes heeft.
- **× en :** komen in G5 alleen voor in GET-M05, M06, E07 (batch 2 en 3), MEET-E08 (niet in deze build) en VERH-E02 (niet in deze build). Daarbuiten geeft check_hints FAIL.
