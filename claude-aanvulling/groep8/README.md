# G8 Claude-merge (1 okt 2026, stap 1–3; build 18:54)

Dit is de G8-merge van de Claude-vragenbank (`/workspace/claude-bank-src`, CC BY-SA 4.0) naar LeerMees. De aanpak is dezelfde als bij G4–G7. `scripts/build_g8.py` hergebruikt `g7/scripts/build_g7.py` (conversie, ids, somtypen, dubbels, controleketen G3–G7) en legt de G8-regels erbovenop.
- **Gelezen** wordt alleen uit `claude-bank-src`, `claude-merge/g3`–`g7` en `exports/`. De G8-bank en de pilots worden alleen gelezen via `exports/leermees-vragenbank-export/vragenbank_g8.json`.
- **Geschreven** wordt in deze map en in `g7/data/aanvulling_uit_g8.json`. De canonieke `rekenen-groepN/bank/` is niet aangeraakt.
- **Sleutels zijn bevroren:** `bevroren/ids_v1.json` en `bevroren/somtype_nr_v1.json` (189 somtypen). Ze zijn schoon opnieuw gemaakt om 18:53, omdat er nog geen hints waren. De proefversies staan in `_backup/g8_bevroren_1853/`. Een rerun is stabiel: dezelfde inhoud op de tijdstempel na.
- **Motor:** `scripts/fout_regels.py` is gelijk aan die van G5 (met #92/#93/#94), en die is weer gelijk aan G6 en G7.

## Draaien
```
python3 scripts/build_g8.py        # bouwt alles en draait zelf sync_hint_keys.py + apply_hints.py
python3 check_merge_notatie.py     # nu ALLES OK
python3 check_hints.py             # alle 189 somtypen 'open' (nog geen hints) — ALLES OK
```

## Pool en stand
- **Stand 8 okt 15:53 (build 15:53:56):** ronde 1b batch 1 en 2 (Oefeningen): check_hints 49 klaar · 174 open · 0 FAIL · 0 WARN; b1/b2 FAIL 0.
- **Stand 8 okt 15:36 (build 15:36:15):** Didactiek batch 2: V-#781 (#16 kloktijden '14.35 uur'), V-#782 (#32 afleider 'Deel 100 door 40 en doe dat keer 15'), Z-#780 (kop 'deelbaar door 5'), Z-#781 (guard ochtendtemperatuur ≥ 0), Z-#782 (KLOKTIJD-check, FAIL; typ-invoer MEET-E06 WARN). check_hints 49 klaar · 174 open · 0 FAIL · 1 WARN (wacht op de regel van Oefeningen voor #32).
- **Stand 8 okt 15:27 (build 15:27:54):** hints batch 1 en 2 (49 somtypes): check_hints 49 klaar · 174 open · 0 FAIL · 0 WARN. Even grote breuken tellen als goed (V-#760, breukvorm), Z-#766/#767/#768 en Oef-#472/#478/#480 verwerkt. Zie merge-fixlijst.md.
- **Stand 8 okt 15:17 (build 15:17:54):** hints batch 1 (GET-E02 #1–#11, GET-E03 #1–#5, GET-E04 #1–#8; 24 somtypes, 317 items) staat erin: check_hints 24 klaar · 199 open · 0 FAIL · 0 WARN, merge-notatie ALLES OK. Oef-#467: bij 'Welk antwoord … kan kloppen?' (GET-E02 #5/#9) staat de goede optie nu om de beurt op A/B/C. Zie merge-fixlijst.md.
- De pool bestaat uit de Claude-items van de G8-doelen (T1, T2, T3, T4, T5, T6, T7, M24, M25, M26, M29, K7, K8, G8, G9, G13, T8, T9, W3, W6) plus de 688 items die G7 voor G8 parkeerde (`g7/data/geparkeerd_G8.json`), alle 688 in de pool.
- Wat al in G3–G7 zit, gaat niet mee: 536 items, allemaal T9.
- **Pool 2249 → gemapt 908 · twijfel 1226 · terug-G7 110 (waarvan 46 met een G7-doel in `g7/data/aanvulling_uit_g8.json`) · buiten-basisschool 1.** Geschrapt: {'dubbel': 4}.
- Controle: {'gemapt|ok': 772, 'gemapt|n.v.t.': 136, 'twijfel|ok': 337, 'twijfel|n.v.t.': 889, 'buiten-basisschool|n.v.t.': 1, 'terug-G7|n.v.t.': 78, 'terug-G7|ok': 32}. **0 FOUT.** De 136 'n.v.t.' bij gemapt zijn vooral meerkeuze-redeneringen (W3/W6, G8/G13), C22 en K7. Daar is geen automatische som.
- Gemapt per doel: G8-GET-E02 119, G8-GET-E03 64, G8-GET-E04 45, G8-GET-E05 125, G8-GET-M01 12, G8-MEET-E01 4, G8-MEET-E03 4, G8-MEET-E05 12, G8-MEET-E06 32, G8-MEET-E07 7, G8-MEET-V01 3, G8-VBN-E03 12, G8-VBN-E04 40, G8-VBN-V01 12, G8-VERH-E03 229, G8-VERH-E04 31, G8-VERH-E05 53, G8-VERH-E06 104.
- Terug-G7 per doel: G7-DENK-02 32, G7-DENK-03 32, G7-GET-04 31, G7-MEET-02 15.

## Bestemmingen (classify_g8)
| status | betekenis | bestand |
|---|---|---|
| gemapt | in een G8-doel | `data/gemapt.json`, `data/per_doel/G8-*.json`, `somtypen/G8-*.md` |
| twijfel | Didactiek beslist (per categorie) | `data/twijfel.json`, `twijfel_voor_didactiek.md` |
| terug-G7 | niveau G5–G7, geen G8-doel | `data/terug_G7.json` (met een G7-doel ook in `g7/data/aanvulling_uit_g8.json`) |
| buiten-basisschool | machten, wortels, negatief × negatief, letters als getal, modus/mediaan (SLO eind G8; besluit kans/mediaan G7) | `data/buiten_basisschool.json` |

## Twijfel voor Didactiek (1226)
- bouwsel-tellen: 551
- negatief-zonder-context: 217
- schatten-zonder-afspraak: 180
- vakcode-plattegrond: 131
- kan-kloppen-zonder-opties: 96
- geheugenomvang: 28
- statistiek-gemengd: 22
- kans: 1

De vraag per categorie, met een voorstel en voorbeelden, staat in `twijfel_voor_didactiek.md`.

## Eigen bewerkingen in G8 (logs/fixes.csv)
- **G8-R8 notatie:** 'de' wordt 'het' bij het-woorden. Bedragen: '€ 40,-' wordt '€40', '€1.500,-' en '€1.500' worden '€1500' (geen punt onder 10.000, zoals de PUNT-regel). Dit geldt in de opgave, de opties, de Claude-velden en de hints van het item.
- **G8-R9 context (zoals G5 #86):** dieren die sparen, reizen of taart eten worden mensen. 'Een dino/poes/konijn/pinguïn zet €… op een spaarrekening' wordt een naam (Sanne, Daan, Noor, Milan, Fatima of Bram, vast per claudeId), met 'hij' of 'ze' erbij. 'Een dino legt 60 km af in 1,5 uur' wordt 'Een fietser' (≤ 25 km/u) of 'Een bus'. Een eekhoorn die 'reist' wordt 'Een auto rijdt'. Wie loopt, wordt 'Een wandelaar'. 'Een dino eet' wordt 'Een kind eet'. '… miljoen botten/vissen/noten verzameld' wordt 'In een land wonen … miljoen mensen'. 'Je spaart voor poesjes' wordt 'voor een fiets'. 'Wat kost het poesje nu?' bij een knuffel wordt 'Wat kost de knuffel nu?' (dat was een Claude-fout). De huisdieren-grafieken blijven zoals ze zijn.
- **B15 delen door een breuk:** 'stenen, pionnen, poesjes … worden in stukken van 1/4 verdeeld' wordt reep chocola, pizza, pannenkoek of stokbrood (vast per claudeId). Wortels, pizza's, taarten en broden blijven staan. Daardoor kwamen er 3 dubbels bij (4 in totaal).
- **Controle (verify_g8):** haakjes en voorrang, procent erbij/eraf en prijs vóór korting, rente, schaal (kaart ↔ km/m), tijdzones, rekenmachine (naar boven afronden, rest), laatste cijfer, schatten met een afrondafspraak, delen door een breuk, spaartabel, gemiddelde per dag en eenheden (km → m, m³ → L, ha → m²). Daarna volgt de keten G7 → G3.
- **Schatten:** met een afrondafspraak in de vraag ('rond 12 af op honderdtallen', 'rond beide getallen af op duizendtallen') is het item gemapt in G8-GET-E02 (12 items). Zonder afspraak ('Hoeveel is 34 − 22 ongeveer?') is het twijfel.

## Open
- Hints: alle 189 somtypen zijn nog 'open' (Oefeningen).
- Twijfel: 1226 items in 8 categorieën (Didactiek).
- Contexten die nog vreemd zijn, maar niet fout: 'In het nest liggen 2640 schelpen', 'dozen met tanden'. Ze zijn niet aangepast.
