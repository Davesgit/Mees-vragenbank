# Review na-ronde-r13 (G3–G6) · Didactiek · 8 okt 2026

**Getoetst:** branch `na-ronde-r13` @ `983900d` (commit 18:18:22, repo `/workspace/mees-vragenbank`). Het oude stand-punt is merge-base `482a19f`.
- Werkwijze: read-only, met `git archive` naar `/workspace/r13work/snap` (983900d) en `/workspace/r13work/base` (482a19f). Geen checkout of worktree. De repo is niet aangeraakt: `git status` is schoon.
- `tools/` is gekopieerd naar de snapshot. Ontbrekende scripts komen uit de r13-werkmap (zie Z-#1010). Bytecode stond uit. Er bleef geen `__pycache__` achter.
- **Stempels (snapshot):**

  | Groep | gegenereerdOp | hintsSyncOp |
  |---|---|---|
  | G3 | 01-10 13:58:16 | – |
  | G4 | 08-10 15:46:18 | – |
  | G5 | 12:47:18 | 18:12:31 |
  | G6 | 12:11:42 | 18:12:40 |

- **Eindcontrole 18:36:57:** de branch staat nog op `983900d`.
  - `main` staat nu op `a3d45ec`, niet meer op 482a19f.
  - In `claude-merge/r13` staat sinds 18:35:01 een nieuw `v1001_g5_e07.json`. Dat zit niet in de commit en is niet beoordeeld.

## 1 · Commits

| Commit | Beweerd | Gevonden |
|---|---|---|
| 846ce30 | kloktijdronde G3–G5 | ✓ digitaleKlok G3 0 / G4 12 / G5 234.<br>✓ '.uur' G3 12 / G4 18 / G5 504 items (= MEET-E06 489 + VBN-E03 15; de 234 items met alleen de vlag zijn apart geteld).<br>✓ «(Typ als 14.30.)» bij 232 items, alle open tijd-antwoorden in 3 vormen.<br>✓ klok_motorcheck G3 12/12, G4 18/18, G5 258/258. |
| 9f52d61 | groep6 terug, G3-check repo-relatief | ✓ |
| a6aa9b1 | les 348 TIJDSDUUR '.' en ':' | ✓ 8/8 mutanten |
| 967c707 | (Overzicht: tijdsduur-check) | ✗ Alleen de G6-stempels terug. De tijdsduur-check zit in a6aa9b1 en 0532139 (Z-#1011). |
| 0532139 | Z-#951 zonder signaalwoord | ✓ 20/20 mutanten. De oude guard a6aa9b1 mist 7 van de 20 → de nieuwe guard is falsifieerbaar. |
| 983900d | G5 speelvolgorde 504 / 3 → basis / JO 2; G6 680 + L-R10d 4 + L-R10e 72 / E08 8 / JO 16 / N13-1/2 | ✓ alle tellingen (§3).<br>Niet gemeld: 464 G5-MEET-E06 `merge.hints`-sleutels (sync na de kloktijdronde).<br>`BORD_N13`/`fixlijst_g6.py` staat **niet** in de repo (Z-#1010). |

## 2 · Kloktijd G3–G6

- **Resten zelf gezocht.** Gekeken naar ':' en '.' zonder 'uur', in alle stringvelden en in hints/somtypen.
  - ':' staat alleen bij items met digitaleKlok, in interne velden (`foutRegels.match.waarden`, `rijGroep`, `beoordeling.bron`) en in `geldigeAntwoorden`/`antwoordDetail.invoer`.
  - '.' zonder 'uur' komt alleen voor in de motorwaarden en bij geld-invoer ('3.50').
- **TIJDSDUUR.** 0 in G3–G7, ook bij een duur zonder signaalwoord.
  - Duurvragen in G5 vragen naar minuten («Hoeveel minuten duurde het?» → 80). De reisduur staat er als «1 uur en 20 minuten».
- **digitaleKlok.** De vlag staat bij «Welke klok wijst 23:08 aan?» en bij «Hoe laat is het op deze klok?» met digitale opties. Akkoord: daar is het omzetten van analoog naar digitaal het doel.
- **Twee echte resten in G5 (V-#1012):**
  - **De tekst noemt nog de dubbele punt.** De overloop-L1 in MEET-E06 1200–1211 zegt «Zestig minuten of meer kan niet achter de **dubbele punt**.»
  - **De foutsleutel staat alleen in de ':'-vorm** ('12:85'). `_klok_vormen` laat minuten ≥ 60 ongemoeid. Een kind dat volgens de instructie '12.85' typt, krijgt deze L1 niet: `lett_past('12:85','12.85')` = False.

## 3 · G5 en G6

- **G5 L-R9-4a, speelvolgorde.**
  - De volgorde 1, 2, 3, 9, 4, 6, 7, 8, 10, 5, 11 (weergavenummers) staat in `bevroren/speelvolgorde.json` en bij alle 504 items.
  - Delen-cluster #3 → #9 en keer-cluster #8 → #10 → #5 kloppen met Leerlijn A2.
- **G5 L-R9-4b.** naar-002 (3 × 13 = 39), naar-026 (6 × 12 = 72) en naar-008 (98 gedeeld door 7 = 14) staan op basis.
  - Dat is logisch: het past bij de basisitems 84, 90 en 98 in #3 en #8.
- **G5 juisteOptie.** MEET-E07 282 (€2,20 − €1 = €1,20) en 287 (€3,50 − €1 = €2,50): nagerekend op `jsRender.munten`. ✓
- **G6 juisteOptie.** GET-E04 022–030 ✓: alle 7 handige routes nagerekend.
  - **GET-M04 021–029: ✗.** `opties[]` en `optiesTekst` spreken elkaar tegen bij 019–030 (12 items).
  - De fix zet de letter op `opties[]`. Volgens `optiesTekst` is A nu «de deler» (V-#1010).
  - VERH-E02 021: alleen de hoofdletter. ✓
- **G6 GET-E08 (V-#851/#852).** Alle 8 rijen kloppen met het voorstel. De som en het antwoord blijven gelijk. Geen enkele foute route (mediaan, modus, midden, middelste genoemde, gegeven waarde) geeft nog het goede antwoord. De oude rij komt nergens meer voor.
  - GEMIDDELDE-guard: oud 7 FAIL · 8 WARN → nu 0.
  - **Maar bij 011:** Claudes vaste sleutel '7' was het oude hoogste getal. Die krijgt nu de L1 «Dat is alles samen. Deel dat nog door het aantal.», en dat klopt niet: samen is 20 (V-#1011).
- **G6-niveaus (les 337).** Er zijn 684 niveaus veranderd:
  - 680 via L-R10a: 663 van toepassen → basis, plus 17 van basis → toepassen (VERH-E03 #1);
  - 4 via L-R10d (MEET-E01 nrO 4/5, MEET-E04 nrO 4, MEET-E05 nrO 2, allemaal «20.000 … = □ …» → 20);
  - verdeling per doel: GET-E01 48 · E03 43 · E06 17 · E09 111 · M02 200 · M03 12 · M06 31 · MEET-E01 36 · E03 75 · E04 51 · E05 11 · VBN-E02 30 · VERH-E02 2 · VERH-E03 17.
  - Alle overgangen zijn nagerekend tegen base. Er zijn geen wijzigingen buiten het rapport.
  - L-R10e: 72 = 36 hm-items (MEET-E01) + 36 dl-items (MEET-E04).
  - De spreiding is gelijk aan Leerlijns 'Nu' in 33 van de 34 somtypes. De uitzondering is GET-E09 #2 met 40/153 in plaats van 49/144.
  - In de steekproef (2 per somtype) was elk niveau plausibel volgens het kenmerk en SLO.
  - De 9 items bij GET-E09 #2 (96 gedeeld door 8 = 12, 70 gedeeld door 5 = 14, enz.) staan op toepassen. Dat is verdedigbaar, want het toepassen-kenmerk noemt 'delen buiten de tafels' (Z-#1013).
- **Titels.** «Beelddiagram, cirkeldiagram en lijngrafiek aflezen» en «Kilogram en gram vergelijken en omrekenen» staan in per_doel. De taal is goed. Zie Z-#1014 voor de inhoud.

## 4 · Checks en mutanten op de branch

- **check_hints G3–G6:** 0 FAIL (G3 1 WARN, G4 3, G5 2, G6 3).
- **check_merge_notatie G3–G6:** ALLES OK. Voor G5/G6 lukt dat pas na het aanvullen van de 4 ontbrekende scripts (Z-#1010).
- **Les 321 (guard faalt op oude data):**

  | Guard | Oude data / oude versie | Nu |
  |---|---|---|
  | KLOKTIJD | G3 12 · G4 48 · G5 1101 | 0 |
  | TIJDSDUUR | G3–G6 hebben geen duur-data. Bewijs via de 20 mutanten (oude guard 7 fout); op de repo-G8 32 treffers | – |
  | JUISTE-OPTIE | G5 2 · G6 16 | 0, maar blind voor `optiesTekst` |
  | GEMIDDELDE | G6 7 FAIL | 0 |

- **Niet bedraad:** KLOKTIJD, TIJDSDUUR en JUISTE-OPTIE draaien in **geen enkele** check van G3–G6, alleen in r13-scripts (V-#1013). Ook voor niveaus en speelVolgorde is er geen guard (Z-#1012).

## 5 · Verdict per groep

| Groep | Verdict | Waarom |
|---|---|---|
| **G3** | **taal: ok (voorlopig)** | Inhoud ok. Wordt definitief zodra V-#1013 de guard in de G3-check zet. |
| **G4** | **taal: ok (voorlopig)** | Idem. |
| **G5** | **taal: fix** | V-#1012, V-#1013 |
| **G6** | **taal: fix** | V-#1010, V-#1011, V-#1013 |

## 6 · Verplicht

- **V-#1010 · G6 · Overzicht.** GET-M04 019–030 (12 items): `optiesTekst` ≠ `opties[]`.
  - Gevolg na de JO-fix: «A) de deler» in `optiesTekst` is als goed gemarkeerd.
  - **Vervang** `optiesTekst` door de weergave van `opties[]`. Voorbeeld 021: «A) de noemer · B) de teller · C) de uitkomst».
  - Neem «de deler» en «het deeltal» nooit als afleider. Een breuk is ook een deling: in 4/10 is 10 echt de deler, dus die optie is ook goed.
  - **Guard:** `juiste_optie_check` eist ook `optiesTekst` = de weergave van `opties[]` (FAIL). Mutant: de huidige 019–030 → 12 FAIL.
- **V-#1011 · G6 · Overzicht.** GET-E08 011: zet in `extraVelden.claudeDenkfouten`/`claudeFoutHints` de sleutel **'7' → '8'** (hoogste getal van 6, 3, 8, 3).
  - Doe ter wille van de consistentie hetzelfde bij 008 ('10' → '11') en 012 ('8' → '10'). Draai daarna apply.
  - **Guard:** een L1 «Dat is alles samen…» alleen als de fout gelijk is aan de som van de rij. Mutant: 011 nu → FAIL.
- **V-#1012 · G5 · Oefeningen (tekst), Overzicht (motor).** MEET-E06 1200–1211, `hints/batch5.json` r. 1175 en 1324.
  - **Tekst wordt:** «Achter de punt staan de minuten. Dat kunnen er niet zestig of meer zijn: een uur heeft zestig minuten. Dan komt er een uur bij.»
  - **Motor:** `_klok_vormen` maakt ook bij minuten ≥ 60 de drie vormen ('12.85 uur', '12.85', '12:85').
  - **Guard:** «dubbele punt» in een kindtekst zonder digitaleKlok = FAIL, en elke h:mm-waarde ook in de '.'-vorm. Mutant: 1200 nu.
- **V-#1013 · G3–G6 · Overzicht.** Zet `kloktijd_check` (KLOKTIJD + TIJDSDUUR) en `juiste_optie_check` als FAIL in check_merge_notatie G3–G6, net als in G7/G8.
  - Nu meldt «FAIL 0» de huisregel niet, en een rebuild brengt ':' stil terug.

## 7 · Zacht

- **Z-#1010 · Overzicht.** Deze scripts staan niet in de repo:
  - groep5/scripts/`check_121.py` en `check_generator_sleutels.py`;
  - groep6/scripts/`check_fixlijst_g6.py` en `fixlijst_g6.py` (`BORD_N13`).

  Daardoor crashen check_merge_notatie G5/G6 op de branch, en ook op main. Committen of de import opvangen met een duidelijke melding.
- **Z-#1011 · Overzicht.** Commitbeschrijving:
  - de tijdsduur-check is a6aa9b1 + 0532139, niet 967c707;
  - meld de 464 hint-sleutels in 983900d.
- **Z-#1012 · Overzicht.** Build-assert voor niveau = `classificeer()` (None overslaan) voor de 34 somtypes, en `merge.speelVolgorde` = `bevroren/speelvolgorde.json`. Nu moet `r13_uitvoer.py` na elke build met de hand opnieuw draaien.
- **Z-#1013 · Leerlijn.** Bevestig de strenge lezing bij GET-E09 #2 (9 items toepassen, telling 40/153). Twijfelgeval: 150 (3/5 van 100, één deel = 20).
- **Z-#1014 · Leerlijn/Overzicht.** De titel N13-1 noemt beeld- en cirkeldiagram, maar VBN-E02 heeft tot N13-3 alleen lijngrafiek-items.
  - Zet de titel pas live samen met N13-3. Of de guard #276 eist dan ≥ 1 item van dat soort.
- **Z-#1015 · Leerlijn.** Speelvolgorde E07: #11 «rond tiental» (7 × 30) is makkelijker dan #8 «splitsen», maar komt als laatste.
  - Overweeg #11 → #8 → #10 → #5.
  - Signaal: #1 «# × # =» (328 items) staat helemaal op toepassen en opent het doel.
- **Z-#1016 · Overzicht.** GEMIDDELDE in G6 van WARN naar FAIL, nu E08 opgelost is.
- **Z-#1017 · Oefeningen.** G3 klok-zetten: het antwoord '3.00 uur' bij «Zet de klok op drie uur». Toon in G3 «drie uur» als het antwoord zichtbaar is. De drie geldige vormen blijven.
- **Z-#1018 · Overzicht.** `kloktijd_check.teksten` slaat deze velden over: optiesTekst, foutHintsTekst, opgaveStappen, begripUitleg, sterkereHintMetPlaatje en appMoetTonen. Nu staan daar geen resten, maar neem ze op.
- **Z-#1019 · Overzicht, buiten scope.** De repo-G8 (main en branch) heeft 32 TIJDSDUUR-treffers in `claudeKaleSom` («6.15 uur + 5.45 uur»). De live g8 heeft er 0. Repo G8 bijwerken.

**Open, niet beoordeeld:** N13-3 (Oefeningen), L-R10f (Dave), L-R9-4c (optioneel).

## 8 · Advies over het concept kritisch-generator G6 (L-R10b, niet in de data)

- **Rekenwerk:** alle 120 items nagerekend → 0 fout. Er staat geen ':' in.
- **Balans:** 30 waar, 90 fout (25 %).
  - Leerlijns zin «ongeveer de helft is fout, een kleiner deel klopt» is dubbelzinnig. Advies: **2 waar + 2 fout per somtype (60/60)**, en minstens 40 % waar. Anders leert een kind dat «Klopt dat?» bijna altijd «Nee» is.
- **Raadbaar uit het patroon:**
  1. Het ware item is altijd nr. 4 van een somtype.
  2. In de foute items staat «Ja» nooit op C (A 60×, B 30×). Dus «Ja» op C is altijd goed, en «Ja» op B betekent dat het goede antwoord A is. Een kind dat alleen naar de posities kijkt, haalt 70/120 (58 %) zonder te rekenen. Met gokken is dat 33 %.
  3. Bij afronden is in 6 van de 8 items maar één Nee-optie een veelvoud van 1000 of 100. In 2 items is de bewering zelf geen veelvoud (99.800 bij duizendtallen). Dan verklapt de vorm het antwoord.
- **Taal:**
  - Twee getallen staan direct na elkaar: «4/5 van 80 20 is», «€72 €24 is», «8 cm 36 cm² is». Maak er directe rede van: «Noor zegt: "4/5 van 80 is 20." Klopt dat?».
  - «Nee, het is 6 koekjes.» → «Nee, het zijn 6 koekjes.»
  - De rest is helder.
- **Niveau:** kritisch vraagt om redeneren. Gebruik daarom geen extra zware getallen (99.818 → 100.000, 25.000 cl). Ook de onrealistische 11.000 cm uit Leerlijns signaal hoort er niet in. Kies getallen uit het midden van basis/toepassen, zodat de denkfout centraal staat.
- **Leert de uitleg iets?** Nog niet. Er is geen L1, H1 of H2 en geen uitleg; alleen het interne `denkfoutPerOptie`. Voorstel:
  - **H1** (alle somtypes): «Reken het eerst zelf uit, zonder naar het antwoord van [naam] te kijken. Krijg je hetzelfde?»
  - **L1 bij «Ja» op een fout item:** noem de denkfout, niet het antwoord. Bijvoorbeeld bij afronden: «Lisa heeft de laatste cijfers weggelaten. Kijk naar het honderdtal: rond je dan naar boven of naar beneden af?»
  - **L1 bij een foute «Nee, het is …»:** per denkfout, uit `denkfoutPerOptie`.
  - **L1 bij «Nee» op een waar item:** «Reken het nog eens na. Wat krijg jij? Klopt dat met wat [naam] zegt?»
  - **H2 per somtype:** zet de denkstap klaar, zonder conclusie (les 350).
- **Concreet voor de generator:**
  - Waar-items op willekeurige itemnummers.
  - `husselen: true`, of per somtype elk optietype (Ja / goed-Nee / fout-Nee) even vaak op A, B en C.
  - Bij afronden zijn de bewering en beide Nee-opties veelvouden van de afrondeenheid. Voorbeeld: 43.948 → bewering 43.000, opties 44.000 / 40.000.
  - **Guards:**
    - waar-aandeel per doel 40–60 %;
    - per letter X: P(goed | Ja op X) tussen 0,2 en 0,6;
    - de afrond-vormregel hierboven;
    - geen twee getallen direct na elkaar in de bewering;
    - per foute optie een L1.
  - **Alternatief** (Leerlijn onduidelijk 6): in twee stappen, eerst Ja/Nee en dan het goede getal typen. Dan valt er niets te raden uit de posities.

## Lessen

- **385.** Bij een reparatie met gelijke som (les 307) ook Claudes vaste sleutels nalopen. Een sleutel die naar een waarde uit de oude rij wees (bijvoorbeeld het hoogste getal) rekent zichzelf niet opnieuw uit. Hij valt terug op Claudes label en kan een L1 krijgen die niet klopt (E08 011).
- **386.** Een juisteOptie-fix legt `opties[]` én `optiesTekst` naast elkaar. Twee optiebronnen kunnen elk een andere letter 'goed' maken (M04 019–030).
- **387.** Na een notatiewissel (':' → '.') ook nalopen:
  - de woorden over het teken ('dubbele punt');
  - de foutsleutels buiten de geldige tijden (minuten ≥ 60), want die gaan niet mee in de omzetting.
- **388.** Een guard die alleen in een rondescript draait, is geen guard. Hij hoort als FAIL in de vaste groepscheck.
- **389.** Meet bij waar/fout-items ook de plek van «Ja» en het nummer van het ware item. Een vast patroon is raadbaar, ook als de goede letter netjes over A, B en C verdeeld is.

## Oefeningen · V-#1012 en zacht (8 okt, 18:47)

**V-#1012 (tekst + guard), geplaatst 18:46:50.** `hints/batch5.json` r. 1175 en 1324 (G5-MEET-E06 nrO 21 en 23, soort 'zestig minuten of meer'), in `claude-merge/r13/g5` én in de worktree `claude-aanvulling/groep5` (na-ronde-r13 983900d, niet gecommit). Beide bestanden md5 `001c81b1…` (was `e4049e33…`). Backup `/tmp/r13_g5_batch5_voor_v1012_184650.tgz`.
- L1 is nu «Achter de punt staan de minuten. Dat kunnen er niet zestig of meer zijn: een uur heeft zestig minuten. Dan komt er een uur bij.» (25 woorden). 'waarom' vermeldt V-#1012.
- L2 hoeft niet mee: het is de H2 van het somtype («Ga je over het hele uur heen? …» / «Komen de minuten op zestig of meer? …»). Daarin staat geen dubbele punt en geen ':'.
- Patch `g8work/r13/patch_r13_v1012.py` is idempotent (2 wijzigingen, daarna 0). Hij assert dat geen tekstSterker 'dubbele punt' noemt.
- **Vormen (voorwaardelijk):** de motor van Overzicht (`fout_regels.py` 18:40:06, alleen in `claude-merge/r13/g5`; in de worktree nog niet) maakt van de 8 sleutels de drie vormen, bijvoorbeeld 1200 `['12.85 uur', '12.85', '12:85']`. De check eist dan alle drie (FAIL). Zonder die motor geeft hij INFO «wacht op de motor», en een puntvorm in de waarden geeft FAIL. Beide standen zijn getest (sandbox-kopie en worktree-kopie).
- **Guard** `g8work/r13/check_v1012.py <g5-map>`:
  - «dubbele punt» in een kindtekst zonder digitaleKlok = FAIL. Dat geldt voor hint, H2, L1, L2, algemeneFoutHint, foutHintsTekst, optiesTekst, sterkereHintMetPlaatje en appMoetTonen (ook de velden van Z-#1018).
  - Elke h:mm-waarde moet ook in de '.'-vorm staan (836 waarden).
  - Elke overloopsleutel moet echt de overloop zijn (uur − 1, minuten + 60, ≥ 60) en in de waarden van zijn regel staan.
  - L1 mag hooguit 45 woorden hebben, plus SNAP (les 234) van de sleutels.
  - Les 321: op de oude stand geeft de guard 16 FAIL, waaronder 1200.
- **Mutanten 8/8 gevangen**, op beide standen:
  - de oude tekst (1200);
  - 'dubbele punt' in een hint;
  - **puntvorm '12.85' buiten de waarden**;
  - een ontbrekende vorm;
  - een verkeerde overloop ('17:65');
  - meer dan 45 woorden;
  - een gewijzigde Claude-sleutel (SNAP);
  - een h:mm-waarde zonder '.'-vorm (VBN-E03 014).
- **Kopie na plaatsing** (OVERLAY leeg): check_hints 139 · 0 FAIL · 2 WARN (dezelfde als vooraf). merge-notatie G5 ALLES OK. check_v1012 FAIL 0. De apply-log is gelijk aan vooraf.
- Na apply staat 'dubbele punt' nog alleen bij de 234 digitaleKlok-items. Dat is akkoord volgens §2. In G4 MEET-E06 komt het alleen voor bij 12 digitaleKlok-items.
- **Voor Overzicht:**
  - batch5.json committen op na-ronde-r13 en de motor (`fout_regels.py`) meenemen naar de worktree. De live per_doel krijgt de tekst pas bij jullie apply.
  - Les 388: zet `check_v1012` (of de twee regels ervan) als FAIL in de vaste G5-check, samen met V-#1013.

**Zacht (wat van ons is):**
- **Z-#1017** is geen hinttekst. Onze G3-teksten noemen de tijd al in woorden («Bij drie uur wijst de kleine wijzer naar de 3»), en in G3 MEET-E05 staat in geen enkele kindtekst een cijfertijd. '3.00 uur' is het veld `antwoord` (motor/data). Datapunt **Oef-#1022 → Overzicht**: een weergaveveld voor G3, bijvoorbeeld `antwoordTekst` = `claudeKaleSom` («drie uur»). `geldigeAntwoorden` blijft zoals het is.
- Datapunt **Oef-#1021 → Overzicht/Leerlijn:** bij 1211 is de afleider 'tien minuten te laat' = '14.30 uur' precies het voorbeeld «(Typ als 14.30.)». Een kind dat het voorbeeld overtypt, krijgt «De minuten kloppen niet…». Dit is het enige geval in G3–G6 (232 Typ-als-items in G5). Advies: een ander voorbeeld bij 1211.
- De eerder gemelde ontbrekende ')' bij 1207/1208/1211 staat nu goed. Niets te doen.
- Z-#1010–#1016, #1018 en #1019 zijn van Overzicht/Leerlijn. Z-#1018 is wel al afgedekt in onze guard.
