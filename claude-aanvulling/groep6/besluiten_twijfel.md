# Besluiten twijfelgevallen G6-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `data/twijfel.json` (188 items, categorie `breuken-plus-min`, build van 16.01 uur; een `twijfel_voor_didactiek.md` bestond nog niet) · Machineleesbaar: `besluiten_twijfel.json` (id → besluit/doel)

Referenties:
- SLO-tussendoelen (`leerlijn/rekenen-groep7/tussendoelen.txt`):
  - overzicht r. 1314: G6 'breuken aanvullen tot 1', G7 'gelijknamige breuken optellen en aftrekken';
  - eind G6 r. 3886 en 3994–3999;
  - eind G7 r. 4402.
- `SPINE_G6_v1.md` r. 212: 'Gelijknamige breuken +/− formeel, breuk ↔ decimaal, vereenvoudigen, rekenmachine → G7-GET-05'.
- Doelnotities en items: G6-GET-E09, G6-GET-M04, G6-VERH-E02 en E03, G7-GET-05 (+ claude-pilot).
- `data/geparkeerd_G7.json`: daar staan al 76 B7-items 'andere noemers of boven 1' in G7-GET-05.

Regels mechanisch op `opgave`; `besluiten_twijfel.json` past ze per id toe. Alle 188 ids zijn precies één keer gedekt (controle met script).

---

## Wat de doelen echt bevatten

- **G6-GET-E09** (voorstel van de merge): 'aanvullen tot 1 heel met dezelfde noemer (2/7 + 5/7 = 1): hoeveel stukjes missen er nog?' en breuk als operator.
  - Het optellen staat er alleen als controle in de fout-hints ('Tel na: 2/7 + 3/7 = 5/7').
  - Niet in dit doel: gelijknamig maken, vereenvoudigen.
  - Geen enkel twijfelitem heeft als uitkomst precies 1 (alle 188 uitkomsten zijn < 1). Er is dus geen item van het type 'aanvullen tot 1'.
- **G7-GET-05** ('Breuken + rekenmachine'): bevat al 'Reken uit: 2/7 + 3/7 = ?' (003) en 'Reken uit: 3/10 + 4/10 = ?' (pilot-003), plus vereenvoudigen. Dat sluit aan bij SLO eind G7: 'kan gelijknamige breuken optellen en aftrekken in contextsituaties en in formele rekentaal'.
- **G6-VERH-E02**: breuk als deel van een geheel, met plaatje ('Een reep heeft 8 gelijke stukjes. Tim eet 3 stukjes (gekleurd). Welk deel?'). Dat is de G6-manier om stukjes van dezelfde grootte te tellen (SLO G6 r. 3886: relatie stambreuk/niet-stambreuk met dezelfde noemer).

## 1. Kale sommen 'a/n + b/n =' en 'a/n − b/n =' — 176

**Besluit (split):**
- **G7-doel G7-GET-05 — 146 items:**
  - 62 optellen ('+'), alle niveau 1–2;
  - 84 aftrekken ('−'), alle niveau 3.
- **Schrappen — 30 items:**
  - **28 omgedraaide dubbels** (DUBBEL-OMGEDRAAID). Regel: '+' met dezelfde twee breuken in omgekeerde volgorde als een eerder item (laagste nr blijft). Voorbeeld: -003 '6/11 + 2/11' is een dubbel van -002 '2/11 + 6/11'; ook de afleiders (12/11, 9/11) zijn gelijk. In de json staat `duplicaatVan`.
  - **2 dubbels met de bank** (DUBBEL-BANK): -085 '3/10 + 4/10' (= G7-GET-05-claude-pilot 003) en -087 '4/10 + 3/10' (dezelfde som omgedraaid).

**Reden:**
- Formeel optellen en aftrekken van gelijknamige breuken is SLO eind G7. De spine van G6 zet het expliciet in G7-GET-05.
- G6 heeft alleen 'aanvullen tot 1' (E09). Daar valt geen enkel item onder, want geen uitkomst is 1.
- De merge zet de B7-items met andere noemers of boven 1 al in G7-GET-05. Dit houdt de lijn gelijk.

**Split op noemer** (gevraagd door Overzicht) in de G7-groep. Noemer 4: 2 · 5: 5 · 6: 3 · 7: 14 · 8: 13 · 9: 19 · 10: 17 · 11: 52 · 12: 21. Dit verandert het besluit niet: elke noemer gaat naar G7.

**Voorwaarden (G7):**
- Breuken in cijfers met schuine streep ('3/4'), het minteken '−' en 'Typ een breuk.' zoals de merge al doet.
- Bij de kale sommen hoeft geen plaatje. Een breukenstrook als hint mag.
- **Fout-hints herschrijven:**
  - Alle 176 kale items noemen 'de taart' ('De noemer zegt in hoeveel stukken de taart is verdeeld'), terwijl er geen taart is. Maak daarvan 'het geheel'.
  - In 180 fout-hints krijgt een fout met de **goede** noemer (bv. 9/11 bij 2/11 + 6/11) toch de noemer-hint. Dat zijn rekenfouten in de teller. Gebruik dan: "Tel de stukjes nog eens: 2 + 6 = ?". De noemer-hint alleen bij een fout met een andere noemer (bv. 8/22).
- Geen uitkomst hoeft vereenvoudigd te worden (geen enkele kale uitkomst is vereenvoudigbaar). Laat de app toch ook een gelijkwaardige breuk goed rekenen. Dat past bij G7-GET-05, dat vereenvoudigen kent.

**Voorbeelden:**
- G7: G6-GET-E09-claude-bank-twijfel-001 ('2/4 + 1/4'), -002, -093 ('3/4 − 2/4').
- Schrappen: -003, -085.

## 2. Taartverhalen 'Welk deel is samen op?' — 12

**Besluit (split):**
- **G6-doel G6-VERH-E02 — 10 items**, met als voorwaarde een plaatje. Regel: `opgave` bevat 'taart'.
- **Schrappen — 2 items** (DUBBEL-VERHAAL): -182 (konijn) en -184 (dino). Ze hebben dezelfde breuken en hetzelfde verhaal als -179 (2/4 + 1/4); alleen het dier verschilt.

**Reden:**
- Met een taart in n gelijke stukken, waarbij de twee delen een eigen kleur hebben, telt het kind stukjes van dezelfde grootte en noemt het deel ('5 van de 6 stukjes = 5/6'). Dat is G6-VERH-E02 (breuk = deel van een geheel, gelijke stukken), en het past bij SLO G6 r. 3886.
- Het is géén formele optelling. Alle noemers zijn 4 t/m 10.

**Voorwaarden:**
- **Plaatje verplicht**: een taart of cirkel in n gelijke stukken, de twee delen in twee kleuren. Zonder plaatje is het een formele optelling en gaat het item naar G7-GET-05.
- **Niet vereenvoudigen**: -178 (4/6), -181 (6/8) en -185 (2/4) hebben een vereenvoudigbare uitkomst.
  - Het antwoord blijft het aantal stukjes (4/6).
  - De app accepteert ook 2/3, 3/4 en 1/2, maar vraagt er niet om. Vereenvoudigen is G7.
- **Taal:**
  - 'Een speler eet 5/10 van een taart' (-188) wordt 'Een kind eet …'.
  - Bij 'dino' (-184 valt al weg, -185 en -186 blijven) liever een kind of dier uit het dagelijks leven, zoals in G4-fix W5.
- Fout-hints: 'Samen op betekent optellen, niet aftrekken' en 'Je hebt 3 stukken, maar van welke grootte?' blijven.

**Voorbeelden:** G6-GET-E09-claude-bank-twijfel-177, -179, -183 (G6) · -182 (schrappen).

---

## Samenvatting

| Groep | Aantal | G6 | G7 | Schrappen |
|---|---:|---:|---:|---:|
| Kaal optellen | 92 | 0 | 62 (GET-05) | 30 (28 omgedraaid, 2 bank) |
| Kaal aftrekken | 84 | 0 | 84 (GET-05) | 0 |
| Taartverhaal | 12 | 10 (VERH-E02) | 0 | 2 |
| **Totaal** | **188** | **10** | **146** | **32** |

## Open vragen voor Dave/Overzicht
1. **Scheve noemerverdeling:** 52 van de 146 G7-items hebben noemer 11 (elfden), en dat is geen 'veel voorkomende breuk'. Begrenzen in de app, of de helft schrappen? Didactisch is het niet fout.
2. **Omgedraaide dubbels:** ik schrap ze (28), net als de M8-tweelingen in G4. Wil Overzicht ze toch houden als 'wissel'-oefening, dan kan dat via `duplicaatVan`.
3. **Gevolg voor de G6-bank:** G6-GET-E09 krijgt uit deze lijst niets. Moeten er voor E09 nog Claude-items 'aanvullen tot 1' gezocht worden, bijvoorbeeld uit de G7-park met uitkomst 1 heel?
