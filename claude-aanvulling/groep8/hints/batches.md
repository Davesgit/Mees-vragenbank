# G8 hints: batches (Oefeningen)

Voorstel van de indeling in 9 batches staat bij Overzicht (8 okt). Stand per batch:

| Batch | Doelen | Somtypes / items | Status |
|---|---|---|---|
| 1 | GET-E02 #1–#11 (schatten, laatste cijfer), GET-E03 #1–#5 (rekenvolgorde), GET-E04 #1–#8 (breuken) | 24 / 317 | **geschreven 8 okt 15:04** (make_batch1.py → batch1.json; patch_batch1.py ronde 1 leeg). Zandbak: check_hints 24 klaar · 0 FAIL · 0 WARN; g8work/b1/check.py 317 items · 1304 sleutels · FAIL 0 · WARN 0 · INFO 112; 14 mutanten gevangen. Gesynct in build 15:27:54. Didactiek 15:23: taal fix → **ronde 1b geschreven** (patch_batch1.py, 39 wijzigingen / tweede run 0; zandbak op live 15:27:54: check_hints 49 klaar · 0 FAIL, merge-notatie OK, b1/check 317 items · 1214 sleutels · FAIL 0 · WARN 0, 23 mutanten 0 gemist). **Live** (build 15:35/15:36 draaide de patch; groen op een verse kopie van live om 15:43). |
| 2 | GET-E02 #12–#36 (meerkeuze met tekstopties: aanpak kiezen, controleren, fout vinden) | 25 / 25 | **geschreven 8 okt 15:17** (make_batch2.py → batch2.json; patch_batch2.py ronde 1 leeg, twee runs 0/0). Verse kopie van live: check_hints 49 klaar · 0 FAIL · 0 WARN; merge-notatie ALLES OK; g8work/b2/check.py 25 items · 50 sleutels · FAIL 0 · WARN 0 · INFO 4; 20 mutanten gevangen; b1/check blijft FAIL 0. Gesynct in build 15:27:54. Didactiek 15:35: taal fix → **ronde 1b** (V-#780/#782/#783, Z-#783/#784; 54 wijzigingen, tweede run 0), op live gezet om 15:43. Verse kopie: check_hints 0 FAIL · 0 WARN, b2/check FAIL 0 · WARN 0, 31 mutanten 0 gemist. |
| 3 | GET-E02 #37–#57 (aanpak kiezen/beoordelen, omrekening controleren, rest bij delen) + GET-V02 #1–#4 (gemiddelde) | 25 / 25 | **geschreven 8 okt 15:55** (make_batch3.py → batch3.json; patch_batch3.py ronde 1 leeg, twee runs 0/0). Verse kopie van live 15:53:56 + sync/apply: check_hints 74 klaar · 0 FAIL · 0 WARN; merge-notatie ALLES OK; g8work/b3/check.py 25 items · 50 sleutels · FAIL 0 · WARN 0 · INFO 31; 39 mutanten 0 gemist; b1/b2-check blijven FAIL 0. Wacht op sync (volgende G8-build) en review Didactiek (review-batch3.md). |
| 4–9 | zie voorstel bij Overzicht | | open |

Regels: na een sync nooit make_batchN.py --force; correcties alleen in patch_batchN.py (idempotent, tweede run 0). Lessen: lessen_g8.md.
