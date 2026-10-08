# G6 Claude-merge: indeling in batches

Geschreven op 2026-10-01 om 19:56 (Amsterdam). Stand: rebuild van Overzicht om 19:11 (`gegenereerdOp`), met **90 somtypen en 3.980 items**, 21 doelen.

- **Indeling:** per kerndoel. Eén doel (één md-bestand) wordt nooit gesplitst.
- **Werkwijze en tools als in G5:** `make_batchN.py` → `batchN.json`; `patch_batchN.py` (idempotent, `patch_lib.py` = kopie van G5) →
  `scripts/sync_hint_keys.py` → `scripts/apply_hints.py` → `check_hints.py`, `check_merge_notatie.py`, `logs/hint_sleutels.json`, de gedeelde checkers
  (`/workspace/tools/check_{notatie,optieletters,cues,dubbelepunt,ketensom}.py 6`), de refscan (`/workspace/g6work/refscan.py`) en een eigen check per item
  (`/workspace/g6work/bN/check.py`). Twijfels in `batchN_twijfels.md`, verslag in `review-batchN.md`, punten voor Overzicht in `../merge-fixlijst.md`.

| Batch | Kerndoel | Doelen | Somtypes | Items | Stand |
|---|---|---|---|---|---|
| 1 | Getallen: grote getallen | GET-M01 (2), GET-M02 (5), GET-E01 (8), GET-M03 (2) | 17 | 521 | hints klaar (19:56); taalpoort Didactiek v1 'taal: fix' (20:15); ronde 1b klaar (20:37), recheck Didactiek 20:50 in orde; **ronde 1c klaar (20:53; nagekeken op build 20:58:10)**: #158d ouderzin tot 100.000, #159a, #160 geen 'teller'. b1/check.py 0 FAIL; check_hints 0 FAIL · 0 WARN; review-batch1.md, review-batch1b.md, review-batch1c.md, lessen_batch2.md (1–15); **ronde 9 (8 okt, Oefeningen)**: Z-#393, zie review-ronde9.md |
| 2 | Getallen: bewerkingen | GET-E04 (8), GET-E06 (7), GET-M05 (3), GET-M06 (6), GET-E07 (2), GET-E08 (2) | 28 | 768 | taalpoort Didactiek 21:35 'taal: fix' → **ronde 2b klaar (21:29, build 21:22:09)**: #190c, #191, #193 (behalve M05 #3 met richting: motor, Overzicht); b2/check.py 0 FAIL · 0 bekend; review-batch2b.md; Overzicht: #190a, #192, #193 (motor M05 #3), #194, #195; **ronde 9 (8 okt, Oefeningen)**: Z-#384, V-#390, Z-#393/#395; Z-#392 wacht op de motor, zie review-ronde9.md |
| 3 | Getallen: breuken | GET-E03 (10), GET-M04 (4), GET-E09 (3) | 17 | 1778 | **hints klaar (21:22, build 21:15:08)**; b3/check.py 0 FAIL (13 motor/data: E03 #7 #169, M04 047 #171); check_hints 12 FAIL (alleen E03 #7 zonder sleutels, #169 Overzicht) · 0 WARN; review-batch3.md, batch3_twijfels.md; fixlijst #169–#175. Ronde 3b; **ronde 3c klaar (22:36, build 22:29:53)**: #205–#209, #220, #222 (+2 zinnen, #232), #225, #226; b3/check 0 FAIL. **Ronde 3d klaar (22:47)**: #250 H2 en algemene fout-hint E03 #2/#3 letterlijk uit recheck-ronde7-batch3-didactiek.md (#232 vervalt); pad250 66/66; lessen 37–40, 49–54.; **ronde 9 (8 okt, Oefeningen)**: V-#390, Z-#393; Z-#391 wacht op de motor, zie review-ronde9.md |
| 4 | Meten en meetkunde | MEET-E01 (7), MEET-E03 (4), MEET-E04 (4), MEET-E05 (2) | 17 | 666 | **hints klaar (21:41, build 21:32:51)**; b4/check.py 0 FAIL; check_hints 0 FAIL · 0 WARN; REF 0, INTRO 0 (#101); review-batch4.md, batch4_twijfels.md; fixlijst #176–#179; **ronde 4b klaar (22:36)**: #212–#216; b4/check 0 FAIL; #229 besloten (tekst = laag 1, tekstSterker = laag 2). **Ronde 4c (22:48)**: #262 tekstSterker 'zijde uit de vraag' E03 #2. 3d/4c taal: ok (recheck-ronde3d4c); **ronde 4d (23:2x)**: #291.; **ronde 9 (8 okt, Oefeningen)**: hm/dl-entries (8), zie review-ronde9.md |
| 5 | Verbanden en verhoudingen | VBN-E02 (3), VERH-E01 (1), VERH-E02 (5), VERH-E03 (2) | 11 | 247 | **hints klaar (22:36, build 22:29:53)**: ronde 5a + 5b (lessen 41–48); b5/check.py 0 FAIL, 192 MOTOR (lijngrafiekregels #219); check_hints 0 FAIL · 0 WARN; review-batch5.md, batch5_twijfels.md; fixlijst #219, #228–#231. Didactiek 'taal: fix' (build 22:54:03) → **ronde 5c klaar (23:08)**: V-#270/#272/#273, Z-#274/#275/#277–#279/#282/#283, 'tien per streepje' weg; lessen 60–67; review-batch5c.md; r5c_check (les 60) 0 FAIL.; **ronde 9 (8 okt, Oefeningen)**: V-#330, Z-#334, V-#380, zie review-ronde9.md |
| 6 | Meetkunde | MKU-E01 (4), MKU-E03 (1) | 5 | 531 | **hints klaar (22:55, build 22:29:53)**: ronde 6a; tekstSterker bij elke fout-hint (les 40); b6/check.py 0 FAIL, MOTOR 621 (torenregels #233); check_hints 0 FAIL · 0 WARN; review-batch6.md, batch6_twijfels.md; fixlijst #233–#235. Didactiek taal: fix → **ronde 6b klaar (23:30)**: #292–#298, #235-teksten; alle 800 torensleutels een eigen tekst; review-batch6b.md. |
| | **Totaal** | 23 doelen | **95** | **4511** | |

## Opmerkingen
- **Batch 3** heeft veel items (GET-E03 alleen al 1.124: ook vereenvoudigen en 'met noemer', zie README). Het aantal somtypes past wel.
- **#101 (symbool + woord in Hint 1):** geldt in batch 4 (MEET-E03, 4 somtypes: cm², m²). Batch 1 heeft geen symbolen.
- **'×' en ':'** mogen overal in G6; 'a : b' als verhouding niet (G7). Ketensommen voluit.
- De G5-items van MEET-E06 #1 (dagen tellen, 45–106 dagen) gaan naar G7, voor later; niet in deze batches.
