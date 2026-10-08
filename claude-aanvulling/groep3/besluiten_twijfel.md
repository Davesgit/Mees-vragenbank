# Besluiten twijfelgevallen G3-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `data/twijfel.json` (276 items) · Machineleesbaar: `besluiten_twijfel.json` (id → besluit/doel)
Referentie: SLO-tussendoelen eind G3/G4 (`leerlijn/rekenen-groep7/tussendoelen.txt`), `SPINE_G3_v1.md`, doelkoppen en notities in `rekenen-groep3/bank/` en `rekenen-groep4/bank/`.

**Afwijking van de lijst van Overzicht:** de JSON (`merge.regel`) groepeert anders.
- 'getallenlijn 4' is R06-getallenlijn (3) plus R03-precies-tussen (1).
- Er is één extra groep, R27-vergelijken ('dikker', 1 item), die niet in de lijst van Overzicht staat. Die lijst telt op tot 275; de JSON heeft er 276.

Alle regels hieronder kunnen mechanisch worden toegepast op velden in de JSON. `besluiten_twijfel.json` past ze per id al toe.

---

## 1. Spiegelen (R21-spiegelen) — 110

**Besluit (split):**
- **G3-doel G3-MKU-E03 — 27 items.**
  - Regel: `visual.jsRender.as == "verticaal"` EN `kolommen <= 7` EN `rijen <= 5`.
  - Kenmerken: verticale lijn, klein rooster (6–7 × 4–5) en de stip 1 vak van de lijn. Het gaat om alle 22 items met claudeDoel K3, plus 5 items met K6 en een rooster van 7×5 van hetzelfde type.
- **G4-doel G4-MKU-E05 — 83 items.** Dit is de rest:
  - een horizontale lijn (34);
  - een groter rooster (8 kolommen of 6+ rijen);
  - of de stip 2 vakken van de lijn (12).

**Reden:**
- 'Spiegelbeeld van een patroon' is SLO eind G4, en G4-MKU-E05 dekt precies dat.
- In G3 staat alleen vouwwerk (G3-MKU-E03: vouwlijn, 'waar komt de ster na vouwen'). Daarom gaat alleen het eenvoudigste type naar G3, als vouwopdracht over een verticale lijn.

**Voorwaarden:**
- Visual verplicht (tekenaar `jsRender` soort "vorm").
- G3:
  - Herschrijf als vouwtaal: "Vouw het blad dicht over de rode lijn. Waar komt de stip?"
  - Niet 'spiegel'.
  - Het kind tikt op het vak en kiest geen code (E1/D1).
- G4:
  - In de notitie bij E05 staat 'géén formele spiegelassen-coördinaten'. Laat het kind daarom ook hier liefst op het vak tikken. Alleen de vakcode als optie (D1/E1/F1) is te formeel.
- Alle 110 antwoorden zijn nagerekend op as/stip/asplek en kloppen.

**Voorbeelden:**
- G3: G3-MKU-E03-claude-bank-twijfel-022, -014, -013.
- G4: G3-MKU-E03-claude-bank-twijfel-102, -058, -081.

## 2. Sprongen (R05-sprongen) — 66

**Besluit (split):** de stap volgt uit de getallenrij in `opgave` (verschil tussen opeenvolgende getallen; □ = `antwoord`).
- **G3-doel G3-GET-M01 — 30 items.** Stap +2, alle getallen even, ≤20 (bv. 6, 8, 10, □, 14).
- **G4-doel G4-GET-M01 — 36 items:**
  - stap −2, even (25);
  - stap ±2 vanaf een oneven getal (3: 3-5-7-9, 5-7-9-11, 9-7-5-3);
  - stap ±3 (2);
  - stap ±4 (6).

**Reden:**
- SLO eind G3: telrij verder/terug en 'tellen met sprongen' (bij handig tellen). Tellen met tweetallen ≤20 is G3-kern.
- SLO eind G4 en de spine zetten 'sprongen van 2, 5 en 10' (ook terug) in G4. G4-GET-M01 heeft al rijen ≤20 (bv. 16, 18, 20) en terugspringen.
- Sprongen van 3/4 en oneven rijen zijn tafelvoorbereiding of uitbreiding.

**Voorwaarden:**
- G3:
  - De opgave moet expliciet zeggen: "Tel met sprongen van 2."
  - Dat is nodig omdat de bestaande M01-items stappen van 1 gebruiken. Hun fout-hints noemen 'stappen van 2' zelfs fout.
- Beide groepen:
  - Haal het woord 'patroon' weg.
  - Vervang moeilijke of Engelse woorden: kittens, ruimtepakken, maanstenen, schroeven.
  - Voorbeeld: "Tel met sprongen van 2. 2, 4, 6, 8, □".

**Voorbeelden:**
- G3: G3-GET-M01-claude-bank-twijfel-038, -030, -003.
- G4: -057 (−2), -005 (oneven), -010 (−4).

## 3. Routes op een rooster (R22-route) — 36

**Besluit (split):**
- **G3-doel G3-MKU-E02 — 27 items.** De route volgen en het vak vinden. Regel: `opgave` bevat níet "Welke route" ("In welk vak kom je uit?" of "Tik op het vak").
- **G4-doel G4-MKU-E01 — 9 items.** Regel: `opgave` bevat "Welke route". Het kind kiest uit drie zinnen als "Eerst 2 hokjes naar rechts, dan 1 hokje naar beneden."

**Reden:**
- Een route van twee stappen volgen op een plattegrond is SLO eind G3 en G3-MKU-E02. Ook stappen van 4–5 hokjes zijn telbaar voor G3.
- Een route in woorden kiezen of beschrijven is de kern van G4-MKU-E01. Drie lange optiezinnen zijn bovendien te veel leeswerk voor een kind van 6–7.

**Voorwaarden:**
- Visual verplicht (jsRender "plattegrond").
- G3:
  - Gebruik korte zinnen: "Je staat bij de school. Loop 2 hokjes naar rechts. Loop dan 1 hokje naar beneden. Waar kom je?"
  - Het kind tikt op het vak.
- **Let op, verschillende vakcodes:**
  - Claude: letter = kolom, cijfer = rij, en rij 1 staat ónder ('beneden' = lager cijfer).
  - De bestaande G3-MKU-E02: letter = rij (A boven), cijfer = kolom.
  - Kies één afspraak per bank, of laat de codes weg en werk met tikken.
- **Datafout:** in G3-MKU-E02-claude-bank-twijfel-014 staat optie C1 twee keer (C1 · C4 · C1). Vervang de tweede door F1 (alleen de tweede stap gezet).

**Voorbeelden:**
- G3: G3-MKU-E02-claude-bank-twijfel-004, -013, -025.
- G4: -019, -024, -020.

## 4. Puzzels (R25-puzzel) — 21

**Besluit (split per id; regel = de id-lijst hieronder):**
- **G3 — 8 items:**
  - **G3-GET-E03** (5):
    - -002 en -003: plek in de rij, van voren/van achteren;
    - -011 en -012: knippen en stukken;
    - -016: hek en palen.
  - **G3-GET-E06** (1): -013, hoeveel sprongen van 2 van 0 naar 10.
  - **G3-GET-M06** (1): -007, '+5 = 12'.
  - **G3-GET-M05** (1): -020, samen 10 en 2 verschil.
- **G4 — 10 items:**
  - **G4-GET-E08** (3): -009 en -010 (delen met rest), -014 (sprongen van 3 van 3 naar 15).
  - **G4-GET-E09** (3): -005 (poten), -018 (wielen), -015 (zaagtijd).
  - **G4-GET-E06** (2): -001 (boterhammen), -008 (truien en broeken).
  - **G4-GET-E05** (1): -006 (samen 15 en 3 meer).
  - **G4-VERH-E01** (1): -017 (balans: 1 appel = 2 pruimen).
- **Schrappen — 3 items:** -004 en -021 (handdrukken), -019 (toernooi).

**Reden:**
- G3:
  - Plek-in-de-rij-vragen passen bij E03 (betekenis van getallen: de 5e tegenover hoeveel).
  - Telpuzzels met 'één meer of één minder' passen bij kritisch redeneren ≤20.
  - De drie andere G3-items zijn in feite gewone G3-stof: sprongen tellen, aanvullen ≤20 en splitsen van 10.
- G4:
  - Delen met rest is G4-GET-E08 (informeel, ook niet-opgaand).
  - Meerstaps-× en + is G4-GET-E09.
  - Combinaties als herhaald optellen past bij E06.
  - 'Dubbel zoveel' past bij VERH-E01.
- Schrappen: combinatoriek (handdrukken, iedereen tegen iedereen) komt in geen G3- of G4-doel voor. De valkuil van dubbel tellen is te moeilijk.

**Voorwaarden:**
- Overal een plaatje: de rij kinderen, het touw/de strook, het hek, de getallenlijn, de sets.
- -016: de zin "Bij elk uiteinde van een vak staat een paal" is te zwaar voor G3. Het plaatje moet het werk doen.
- -020: kort maken: "Twee getallen. Samen 10. Het ene is 2 meer."

**Voorbeelden:** G3-GET-E03-claude-bank-twijfel-002 (G3), -010 (G4), -004 (schrappen).

## 5. Rijen kleuren met ×-teken (R24-rooster-keer) — 12

**Besluit (split):** product = rijen × hokjes uit `opgave` ("Kleur a rijen van b hokjes").
- **G3-doel G3-GET-E06 — 10 items.** Product ≤ 20.
- **G4-doel G4-GET-M06 — 2 items.** Product > 20: -006 (5×5) en -008 (4×6).

**Reden:**
- SLO eind G3: × onder 20 via handig tellen 'per rij of groepje'. G3-GET-E06 is informeel, zonder ×-teken.
- Het ×-teken kennen en noteren is SLO eind G4 (G4-GET-M06). Producten boven 20 vallen ook buiten de getallenruimte van G3.

**Voorwaarden:**
- G3:
  - Schrap de zin "Dat is a × b."
  - Vervang die door "Hoeveel hokjes kleur je? 3 + 3 + 3 + 3 + 3 = □" (herhaald optellen).
- Antwoordformaat:
  - `antwoord` staat als 'kolommen x rijen' (bv. '2x5' bij "5 rijen van 2"). Dat is andersom dan de NL-notatie 5 × 2.
  - Toon die string nooit aan het kind.
  - De checker moet de rooster-vorm controleren.
- Visual: een kleurbaar rooster.

**Voorbeelden:**
- G3: G3-GET-E06-claude-bank-twijfel-009, -002, -007.
- G4: -006, -008.

## 6. Tien plus enen (R08-tientallen) — 10

**Besluit:** G3-doel G3-GET-M02, alle 10.

**Reden:** de tienstructuur ≤20 ('een tien en losse') is G3-kern. G3-GET-M02 doet dit al met 'twee volle handen en 3 losse'. G4-GET-M02 gaat over groepen van tien tot 100.

**Voorwaarden:**
- Er is een interactieve tienstaaf/blokjes-visual nodig. Is die er niet, dan als invulsom: "18 = 1 tienstaaf en □ losse blokjes".
- **-001 ('Leg 20 met een tienstaaf en losse blokjes')** is dubbelzinnig: één staaf + 10 losse, of twee staven. Herschrijf als "Leg 20 met tienstaven."

**Voorbeelden:** G3-GET-M02-claude-bank-twijfel-003, -007, -001.

## 7. Splitsen (R09-splits-kaal) — 7

**Besluit:** G3-doel G3-GET-M06, alle 7 ('13 is 10 en □' t/m 19).

**Reden:** splitsen in 10 en enen ≤20 is de voorbereiding op 'via 10' (G3-GET-M06, SLO eind G3 +/− tot 20 via 10). Pas de tientallige splitsing tot 100 is G4.

**Voorwaarden:** liefst met tienstaaf of rekenrek als steun. De taal is kort genoeg.

**Voorbeelden:** G3-GET-M06-claude-bank-twijfel-001, -005, -006.

## 8. Overige vormen (R19-vormen) — 9

**Besluit (split):**
- **G3-doel G3-MKU-E04 — 2 items.** Regel: `opgave` begint met "Hoeveel hoeken" (-008 zeshoek, -009 vijfhoek).
- **Schrappen — 7 items.** "Hoe heet deze … vorm?" met de antwoorden ruit, vijfhoek, zeshoek, ster (2) en ovaal (2).

**Reden:**
- G3 (SLO, G3-MKU-K03) kent alleen cirkel/driehoek/vierkant/rechthoek. G4-MKU-E04 voegt 'hoek' toe, maar geen nieuwe vlakke vormnamen.
- Ruit, vijfhoek en zeshoek zijn latere stof. Ster en ovaal zijn geen leerlijnfiguren, en daar kies je alleen door wegstrepen.
- Hoeken tellen (≤6) zonder de naam past bij 'verschillen tussen figuren' (G3-MKU-E04 telt al kanten).

**Voorwaarden:** visual met duidelijke hoeken. Noem in de vraag en de feedback geen 'zeshoek' of 'vijfhoek'.

**Voorbeelden:** G3-MKU-K03-claude-bank-twijfel-008 (G3), -005 en -002 (schrappen).

## 9. Getallenlijn (R06-getallenlijn 3 + R03-precies-tussen 1) — 4

**Besluit:** G3-doel G3-GET-E02, alle 4.

**Reden:** getallen ≤20 op de getallenlijn plaatsen en 'precies tussen' (dichtbij/verder) is SLO eind G3 en de kern van G3-GET-E02.

**Voorwaarden:**
- Visual verplicht: lijn 0–20 met streepjes, waarbij 0/10/20 benoemd zijn. Het kind tikt.
- Voor -001 ('precies tussen 12 en 20'): een lijn met 12 en 20 gemarkeerd.

**Voorbeelden:** G3-GET-E02-claude-bank-twijfel-004, -002, -001.

## 10. Vergelijken 'dikker' (R27-vergelijken) — 1

**Besluit:** G3-doel G3-MEET-K01.

**Reden:** 'dik, dikker' staat in SLO eind G3 bij lengte. G3-MEET-K01 gaat over lengtebegrippen en vergelijken.

**Voorwaarden:** schrijf 'dik boek' in plaats van 'woordenboek', met een plaatje.

**Voorbeeld:** G3-MEET-K01-claude-bank-twijfel-001.

---

## Samenvatting

| Groep | Aantal | G3 | G4 | Schrappen |
|---|---:|---:|---:|---:|
| Spiegelen | 110 | 27 | 83 | 0 |
| Sprongen | 66 | 30 | 36 | 0 |
| Routes op rooster | 36 | 27 | 9 | 0 |
| Puzzels | 21 | 8 | 10 | 3 |
| Rijen kleuren met × | 12 | 10 | 2 | 0 |
| Tien plus enen | 10 | 10 | 0 | 0 |
| Overige vormen | 9 | 2 | 0 | 7 |
| Splitsen | 7 | 7 | 0 | 0 |
| Getallenlijn (R06 + R03) | 4 | 4 | 0 | 0 |
| Vergelijken 'dikker' (R27) | 1 | 1 | 0 | 0 |
| **Totaal** | **276** | **126** | **140** | **10** |

**Grootste twijfels:**
1. **Sprongen −2 (25 items).** Ik koos G4 (spine en SLO: sprongen in G4). Je kunt ze ook in G3-GET-M01 zetten met de zin "Tel terug met sprongen van 2". Dan wordt het G3 55 / G4 11.
2. **Spiegelen.** De G3-grens (verticaal, ≤7×5) is streng gehouden, omdat 'spiegelbeeld' formeel G4-stof is. In G3 alleen als vouwopdracht.
3. **Routes.** De vakcodes werken anders dan in de bestaande G3-bank (zie §3).

**Datafout:** G3-MKU-E02-claude-bank-twijfel-014 heeft een dubbele optie. Er zijn verder geen dubbele opties of antwoorden die niet in de opties staan.
