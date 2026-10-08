# hints/ (G7) — nog leeg

Zelfde formaat als `g4/hints/batch*.json`. Neem per somtype `nrOrigineel` + `somtypeOrigineel` over uit de regel **Sleutel** in `somtypen/<doel>.md` (140 somtypen, bevroren in `bevroren/somtype_nr_v1.json`).
Daarna: `python3 scripts/build_g7.py` (draait `sync_hint_keys.py` en `apply_hints.py`) en `python3 check_hints.py`.
Regeltypes voor fout-hints: zie `scripts/fout_regels.py`. Daarin ook: klok, kalender (G4 #49: `fout = gestopt op de eerste/laatste dag van de maand`), tabel, `fout = het andere tiental/honderdtal naast getal1` (G5 #12), en teksten met `[getal1]`, `[getal2]`, `[antwoord]` die per item worden ingevuld.
G7-notatie in hints:
- ':' is het deelteken ('a : b'), nooit '÷'. 'a : b' mag ook voor verhouding en schaal ('schaal 1 : 100').
- Procent mag.
- Ketensommen voluit ('… = 28 en 28 + 12 = 40').
- Hoogstens 3 cijfers achter de komma.
- '−' als minteken, ook bij een negatief getal ('−4 graden').
- 4 cijfers zonder punt, vanaf 10.000 met punt.
- WARN bij een getal boven 1.000.000.

Let op bij GET-05: de Claude-fout-hints van de 123 Didactiek-items zijn al aangepast ('het geheel' in plaats van 'de taart', 'Tel de stukjes nog eens: a + b = ?').
Let op bij veel andere somtypen: de Claude-fout-hints zijn vaak algemeen en passen niet altijd. Een paar voorbeelden:
- 'Let op het teken: het is een keersom' bij inhoud → hoogte;
- 'Kijk goed naar de nullen' bij temperatuur;
- 'Wat wil je weten, en waar deel je dan door?' bij 'Zoek het verschil'.
Vervang die per somtype.

## Besluit-items (17:10)
- **G7-MEET-02 driehoek (#1 m², #2 cm²):** Hint 1 of 2 legt uit: 'basis × hoogte is de rechthoek eromheen; de driehoek is de helft daarvan' (Didactiek, `merge.hintEis`). Het plaatje toont de driehoek in de rechthoek met basis en hoogte. Antwoorden kunnen op ',5' eindigen (fout-sleutels '10,5', '31,5').
- **G7-VERH-04 #4–#6 (deel van het totaal):** het woord 'kans' niet gebruiken (besluit Dave). 'Zoveel op de zoveel' met 'de'. Niet eisen dat het kind vereenvoudigt: gelijkwaardige vormen staan in `antwoordDetail.geldigeAntwoorden`.
- **G7-GET-02 #1/#2 (grootst/kleinst):** meerkeuze. Bij 'kleinst' 'Welke is kleiner?'. De denkfout 'kommagetal-als-geheel' (langer = groter) geldt alleen voor de fout in `merge.decimalenMC.valkuilLangerIsGroter`.
- **G7-GET-04 gemiddelde:** 'het middelste getal', nooit 'mediaan'.
