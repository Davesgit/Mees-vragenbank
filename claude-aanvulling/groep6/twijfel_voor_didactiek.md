# G6 Claude-merge — twijfel voor Didactiek

Geschreven door Overzicht op 1 okt 2026 (Amsterdam). Dit bestand had er bij de build van 16:01 al moeten zijn; het is nu achteraf gemaakt. Het legt de twijfellijst vast, en wat ermee gebeurd is.

## Stand: 0 twijfel (rebuild 1 okt 16:17)

Alle 188 twijfelitems zijn beslist door Didactiek (`besluiten_twijfel.md/.json`) en Dave (16:11). `data/twijfel.json` is leeg.

## De twijfellijst (build 16:01)

**Categorie `breuken-plus-min` (188 items: B7 104, B8 84).** Gelijknamige breuken optellen of aftrekken, uitkomst < 1. Bijvoorbeeld '2/4 + 1/4 =' en 'Een konijn eet 1/5 van een taart en een ander konijn eet 1/5. Welk deel is samen op?'.
- Vraag aan Didactiek: hoort dit in G6 (GET-E09 'aanvullen tot 1', of GET-E03) of pas in G7 (GET-05)? De G6-spine noemt optellen van breuken niet.
- Voorstel van de merge: G6-GET-E09.

## Besluit en verwerking

| Besluit | Aantal | Verwerkt in |
|---|---|---|
| **G7-GET-05** (kale sommen 'a/n ± b/n'; SLO eind G7) | 146 | park-G7 → G7-build: gemapt in G7-GET-05. Bij de G7-build zijn de elfden begrensd (zie onder). |
| **G6-VERH-E02**, alleen met plaatje (taartverhalen) | 10 | gemapt in G6-VERH-E02 (somtype #5). Het taartbeeld staat in `jsRender {'soort': 'taart', 'delen': n, 'kleurdelen': [a, b]}` en de items zijn `nietLiveZonderBeeld`. |
| Schrappen (Didactiek) | 32 | Dave: alleen 4 echt geschrapt; de 28 andere blijven (zie onder). |
| · omgedraaide dubbels (DUBBEL-OMGEDRAAID) | 28 | **Besluit Dave:** ze blijven, als oefening in wisselen, met `duplicaatVan` op het origineel (`merge.wisselOefening`). Ze gaan mee naar G7-GET-05. |
| · al in de G7-bank (DUBBEL-BANK: -085, -087) | 2 | geschrapt (`logs/geschrapt.csv`, 'Didactiek: DUBBEL-BANK'). |
| · dubbel verhaal (DUBBEL-VERHAAL: -182, -184) | 2 | geschrapt ('Didactiek: DUBBEL-VERHAAL'). |

**Voorwaarden van Didactiek (`scripts/besluiten_g6.py`, ook in de G7-build):**
- Breuken in cijfers, '−' als minteken, 'Typ een breuk.'
- In de fout-hints wordt 'de taart' → 'het geheel'.
- Bij een telfout in de teller: 'Tel de stukjes nog eens.'
- Geen vereenvoudiging nodig: de app moet een gelijkwaardige breuk ook goed rekenen (1/2, 2/3, 3/4). Dit is een caveat voor de app.
- -188: 'Een kind eet'. Overal wordt 'dino' een kind of een gewoon dier.

**Elfden (besluit Dave):** van de 52 sommen met noemer 11 (binnen de 146) blijven er hoogstens 12, gespreid over de somtypen. In de G7-build: 6 plus en 6 min. De andere 40 en de 11 omgedraaide elfden-dubbels zijn geschrapt met de reden 'elfden begrensd' (`g7/logs/geschrapt.csv`, 51 regels).

**G6-GET-E09 ('aanvullen tot 1', breuk als operator):** gezocht in de G7-park en de G7-pool.
- Breuk als operator: 12 items gevonden ('… krijgt a/b van N …', Claude-doel B14). Die zijn opgenomen in G6-GET-E09 (somtype #3).
- 'Aanvullen tot 1': geen enkel Claude-item gevonden. Geen van de 188 twijfelitems heeft precies 1 als uitkomst.

## Open voor Didactiek
Niets uit de G6-merge. Wel de nieuwe G7-twijfel, zie `g7/twijfel_voor_didactiek.md`.
