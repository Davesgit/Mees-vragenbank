# G8 hints: batches (Oefeningen)

Voorstel van de indeling in 9 batches staat bij Overzicht (8 okt). Stand per batch:

| Batch | Doelen | Somtypes / items | Status |
|---|---|---|---|
| 1 | GET-E02 #1–#11 (schatten, laatste cijfer), GET-E03 #1–#5 (rekenvolgorde), GET-E04 #1–#8 (breuken) | 24 / 317 | **geschreven 8 okt 15:04** (make_batch1.py → batch1.json; patch_batch1.py ronde 1 leeg). Zandbak: check_hints 24 klaar · 0 FAIL · 0 WARN; g8work/b1/check.py 317 items · 1304 sleutels · FAIL 0 · WARN 0 · INFO 112; 14 mutanten gevangen. Gesynct in build 15:27:54. Didactiek 15:23: taal fix → **ronde 1b geschreven** (patch_batch1.py, 39 wijzigingen / tweede run 0; zandbak op live 15:27:54: check_hints 49 klaar · 0 FAIL, merge-notatie OK, b1/check 317 items · 1214 sleutels · FAIL 0 · WARN 0, 23 mutanten 0 gemist). **Nog niet op live gezet:** wacht op de nieuwe G8-build van Overzicht, dan `g8work/b1r1b/resync.sh` (LIVE=1). |
| 2 | GET-E02 #12–#36 (meerkeuze met tekstopties: aanpak kiezen, controleren, fout vinden) | 25 / 25 | **geschreven 8 okt 15:17** (make_batch2.py → batch2.json; patch_batch2.py ronde 1 leeg, twee runs 0/0). Verse kopie van live: check_hints 49 klaar · 0 FAIL · 0 WARN; merge-notatie ALLES OK; g8work/b2/check.py 25 items · 50 sleutels · FAIL 0 · WARN 0 · INFO 4; 20 mutanten gevangen; b1/check blijft FAIL 0. Gesynct in build 15:27:54. Ronde 1b: V-#764/les 234/235-guards in b2/check (FAIL 0, 24 mutanten 0 gemist); geen tekst te lang, dus geen patch nodig. Doet mee in de hersync na de nieuwe build. Wacht op Didactiek. |
| 3–9 | zie voorstel bij Overzicht | | open |

Regels: na een sync nooit make_batchN.py --force; correcties alleen in patch_batchN.py (idempotent, tweede run 0). Lessen: lessen_g8.md.
