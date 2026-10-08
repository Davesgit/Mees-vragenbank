# Rekenen groep 7 — voortgangsbord

Laatst bijgewerkt: 2026-09-30 13:21 (Europe/Amsterdam)

## Af — G7 content-rond
- G7-VERH-01…05 — 40 **Didactiek-af** (taal: ok) — backup compact in `bank/_backup_compact/`
- G7-MEET-01…05 — 40 **Didactiek-af** (taal: ok) — backup compact in `bank/_backup_compact/`
- G7-VBN-01…05 — 40 **Didactiek-af** (taal: ok) — backup compact in `bank/_backup_compact/`
- G7-GET-01…05 — 40 **Didactiek-af** (taal: ok) — backup compact in `bank/_backup_compact/`
- G7-DENK-01…05 — 40 **uitgebreid naar vol G3-sjabloon (concept; wacht Didactiek)** — backup compact in `bank/_backup_compact/`

**Dubbele punt rechtgetrokken (2026-09-30 12:20, G8-regel, patch Didactiek):** 71 regels in 17 items van VERH-01 · VERH-03 · VERH-04 · DENK-02 ('1 op de n', verhoudingen in woorden, 'schaal 1 : n' met uitleg). Hercheck Didactiek 12:30: 1 verplichte regel (VERH-01-002 opgave, letterlijk verwerkt) + soft VERH-01-006 fout-hint 3/4 → DENK-02 · VERH-01 · VERH-03 · VERH-04 weer `Didactiek-af 2026-09-30. taal: ok.` Ook ':' + getal rechtgezet (Didactiek vraag b, nieuwe regel in check_dubbelepunt): DENK-03-003 fout-hint · VERH-03-002 sterkere hint · VERH-05-008 fout-hint stap 1 (status blijft 2026-09-18). Regel en controle in `bank/README.md` · `python3 /workspace/tools/check_dubbelepunt.py` ALLES OK.

**Deelteken en cues (2026-09-30 12:50, Overzicht):** '÷' → ' : ' in de live bank (63×, 12 bestanden; schaalitem VERH-03-004 voluit 'gedeeld door'); 13 MC-items zonder vorm- of lengte-cue (DENK-01/02/03 · MEET-05 · VBN-01/03/04/05 · VERH-05). Pilot-/draftbestanden niet aangeraakt.

**2026-09-30 13:05 (Didactiek 12:58, letterlijk):** DENK-03-003 stam en fout-hints (sleutel 3 blijft), VERH-05-008 fout-hintregel. Kettingsom-check: 0 fout.

**2026-09-30 13:21 (steekproef Didactiek 13:12, tekstfixes, statussen gelijk):** VBN-05-005 hint 1 zonder spoiler; GET-01 sterkere hint 'Stap 2:' / 'Stap 3:'; live Claude-bestand GET-01-claude.md '1.000' → '1000' (10 regels, accept en foutwaarde niet). Was → Wordt: `/workspace/reviews/steekproef-fixes-v1.md`.

**Totaal bank: ~200** (GET+MEET+VERH+VBN Didactiek-af; DENK concept/vol sjabloon)

## Open
- Didactiek-review G7-DENK-01…05 (nu concept/vol sjabloon)
- Volgende content-scope: wacht op Overzicht/Dave (G8 / andere groep / pauze)

## 2026-09-30 13:28 — Checkers op live claude-bestanden + notatie grote getallen (Overzicht 13:23)
- Checkers volgen nu build-bank.js (`tools/bankfiles.py`): G7-GET-01-claude.md en G7-GET-03-claude.md tellen mee. 1 treffer gefixt: GET-03-claude-008 (Sterkere hint, 'Bij stap 1: …' → 'Stap 1: …').
- Notatie ≥ 10.000 met punt: GET-01 001–003 · 005–008, GET-01-claude 006–008 (Antwoord), GET-03-001, MEET-01-001/005, MEET-03-002/003/005, DENK-03-007 (Getallenruimte). Statussen ongewijzigd.
- Nieuwe check: `tools/check_notatie.py` (WARN). Was → Wordt: `/workspace/reviews/G7-claude-notatie-v1.md`.

## 2026-09-30 13:32 — Didactiek 13:31 (taal: ok notatieronde)
- MEET-03-003 fout-hint: 10³ uitgeschreven als 10 × 10 × 10 = 1000 (machten = VO-stof). check_notatie waarschuwt nu ook voor machten. Statussen ongewijzigd.
