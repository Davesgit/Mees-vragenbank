# Besluiten twijfelgevallen G5-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `twijfel_voor_didactiek.md` en `data/twijfel.json` (9 items, build van 15.25 uur) · Machineleesbaar: `besluiten_twijfel_didactiek.json` (id → besluit/doel)

Referenties:
- SLO-tussendoelen eind G5 en eind G6 (`leerlijn/rekenen-groep7/tussendoelen.txt`: G5 r. 3645–3650 en 3673–3676; G6 r. 3984–3987 en 3994–3999);
- de G5-bank: G5-GET-E08, G5-GET-E04, G5-VERH-E01;
- de G6-bank: G6-GET-E07, G6-GET-E09.

---

## 1. Geld keer een getal, precies uitrekenen (geld-keer) — 8

**Besluit:** ander doel, **G6-GET-E07**, alle 8.
- Niveaus: -004 op *basis*, want de centen gaan niet over de euro (3 × 31 = 93 cent). De andere 7 op *toepassen*.

**Reden:**
- SLO eind G5 noemt bij geld en vermenigvuldigen alleen 'schattend vermenigvuldigen met eenvoudige decimale getallen (geldbedragen)' (8 × € 49,95 ≈ 8 × € 50).
- Pas SLO eind G6 vraagt 'in contextsituaties vermenigvuldigen met geldbedragen met twee cijfers achter de komma (bv.: 3 tandenborstels van € 2,25)'. Deze 8 items doen precies dat.
- De G5-bank houdt die lijn aan. In de notitie bij G5-GET-E08 staat: schattend ×, 'schatting ≠ exacte som (exact mag in sterkere hint/controle)'.
- G6-GET-E07 dekt exact én schattend. De aanpak daar is 'via centen of splitsen in euro's en centen' met een vermenigvuldiger van één cijfer. Dat is precies de uitleg van Claude.
- De getallen zelf passen wel binnen G5: tafels van 2, 3 en 4, centen tot 376, totaal tot €13,04. Het doel is dus niet te zwaar om te rekenen; de reden is dat de SLO precies rekenen met geld in G6 zet.

**Voorwaarden (G6):**
- Geldnotatie zoals in de bank: '€3,94' en '€7,88', zonder spatie en met komma.
- Maak de context realistisch. 'Eén wortel kost €3,94' en 'één sticker €2,94/€2,42' zijn vreemd duur. Gebruik liever bijvoorbeeld 'een zak wortels' of 'een stickervel'. Getallen en antwoorden blijven gelijk.
- De Claude-fout-hints mogen blijven: prijs + aantal, centen maar één keer, een euro te veel. Ze passen bij de keer-controles van E07 ('Reken na: …').
- Optioneel: de tussenvorm uit het voorstel (eerst 'Is €10 genoeg?') als tweede stap. Dat hoeft niet, want E07 heeft al aparte schat-items.

**Ids:** G5-GET-E08-claude-bank-twijfel-001 t/m -008.

## 2. Drie kwart van een hoeveelheid (drie-kwart) — 1

**Besluit:** behouden in **G5-VERH-E01**, op niveau *kritisch* (uitdaging), zoals voorgesteld (G5-VERH-E01-claude-bank-twijfel-001: 8 koekjes, kleur drie kwart → 6).

**Reden:**
- SLO eind G5: 'een kwart van een hoeveelheid' (een kwart van 20 kinderen).
- Drie kwart als begrip zit al in de G5-bank:
  - G5-GET-E04 ordent 'een kwart → een half → drie kwart → heel' en zegt 'drie volle vakjes van vier = drie kwart';
  - G5-VERH-E01 gebruikt het in fout-hints ('15 → Dat is drie kwart van 20', '12 → Dat is drie kwart').
- De stap 'een kwart van 8 = 2, dan 3 keer' vraagt alleen een kwart en een G5-tafel. De breuk als operator met breuknotatie ('3/4 deel van 120 liter') is SLO eind G6 en G6-GET-E09. Dit item heeft geen notatie en een klein aantal, dus G5 kritisch is passend.

**Voorwaarden:**
- 'Drie kwart' in woorden, géén '3/4'. Volgens de notitie bij VERH-E01 is breuknotatie geen leerdoel.
- De tekening (soort 'groepjes', 8, kleurbaar) toont de koekjes liefst in 2 rijen van 4 of in 4 groepjes van 2, zodat de vier gelijke delen zichtbaar zijn.
- Het kind kleurt 6 koekjes en de app telt ze.
- Zet de rekenstap van Claude ('8 : 4 = 2') niet in de opgave, alleen in de hint.
- De fout-hint '2 → dat is maar één deel' blijft.

---

## Samenvatting

| Categorie | Aantal | Behouden (G5) | Ander doel | Schrappen |
|---|---:|---:|---:|---:|
| Geld keer een getal | 8 | 0 | 8 (G6-GET-E07) | 0 |
| Drie kwart | 1 | 1 (G5-VERH-E01) | 0 | 0 |
| **Totaal** | **9** | **1** | **8** | **0** |

## Open vragen
1. De 8 geld-items gaan naar de G6-pool. Moet de G6-merge (build van 16.01 uur) ze nog opnemen in G6-GET-E07? Volgens de G5-twijfellijst zitten ze daar nu niet in.
2. Wil Dave in G5 tóch een precieze geldvraag, als uitdaging? Dan kan alleen -004 (geen euro erbij) in G5-GET-E08 blijven, met eerst een schatvraag. Mijn advies is nee, voor een zuivere G5/G6-grens.
