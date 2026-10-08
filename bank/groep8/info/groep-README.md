# Rekenen groep 8 — oefeningenbank

Oefeningenbank voor LeerMees groep 8 (leeftijd ~11–12 jaar), volle G6-diepte en hetzelfde itemsjabloon als de G5/G6-bank. Bron: `SPINE_G8_v1` (37 IDs) en `BORDTITELS_G8.md` in `/workspace/leerlijn/rekenen-groep8/`. Pad bank: `/workspace/rekenen-groep8/bank/` (bestand = leerdoel-ID). **37/37 IDs · 296 items** geschreven · **37/37 Didactiek-af** · **G8-tekstgate compleet (2026-09-30 12:32)**:
- Wave B1 batch 1 (GET M01–M05, GET-E04, VERH-E01, VERH-E04): `Didactiek-af 2026-09-30. taal: ok.`
- Wave B2 batch 2 (VERH-E02, E03, E05, E06, GET-E01, E02, E03, E05): `Didactiek-af 2026-09-30. taal: ok.`
- Wave B3 batch 3 (MEET-V01, MEET-E01 t/m E07): `Didactiek-af 2026-09-30. taal: ok.`
- Wave B4 batch 4 (GET-V01–V03, VERH-V01, MKU-V01, MKU-E01–E03): `Didactiek-af 2026-09-30. taal: ok.` (hercheck 12:30)
- Wave B5 batch 5 (VBN-V01, VBN-E01–E04): `Didactiek-af 2026-09-30. taal: ok.` (v1 12:30, soft verwerkt)

Zie `VOORTGANG.md` en `bank/README.md` (bankregels: ':' = 'gedeeld door' · schaalregel · vaktermen-check · Rekenmachine-vlag · generator).

- Checker: `python3 check_bank.py` (G6-checker aangepast aan G8, met schaalregel en vaktermen-check; draait de gedeelde `/workspace/tools/check_optieletters.py` mee; `G8_BANK=/tmp/g8_gen_preview` voor de preview).
- Cue-check: `python3 /workspace/tools/check_cues.py 8` (ook in `check_bank.py`).
- Nareken-scripts: `python3 /workspace/tools/g8_b1_nareken.py` · `g8_b2_nareken.py` · `g8_b3_nareken.py` · `g8_b4_nareken.py` · `g8_b5_nareken.py`.
- Generator: `/workspace/tools/g8/` = bron van de bankbestanden. `python3 gen.py` = alleen preview (`/tmp/g8_gen_preview/`) · `--check` = preview vergelijken met de bank · `--write` = naar de bank. Wijzig in de generator, nooit alleen in de bank.

Laatst bijgewerkt: 2026-09-30 13:21 (Europe/Amsterdam).
