# Besluiten twijfelgevallen G4-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `data/twijfel.json` (297 items, build van 14.17 uur) · Machineleesbaar: `besluiten_twijfel.json` (id → besluit/doel)

Referenties:
- SLO-tussendoelen eind G4 en eind G5 (`leerlijn/rekenen-groep7/tussendoelen.txt`, r. 3225–3830);
- `SPINE_G4_v1.md`;
- doelkoppen, notities en items in `rekenen-groep4/bank/` en `rekenen-groep5/bank/`;
- `data/geparkeerd_G5.json`, voor consistentie met wat de merge al naar G5 parkeert.

Alle regels gebruiken velden uit de JSON en zijn dus mechanisch toe te passen. `besluiten_twijfel.json` past ze per id toe. Het script controleert dat alle 297 ids precies één keer gedekt zijn.

---

## 1. Schaal (staafdiagram, 1 streep = 2 of 5) — 145

**Besluit (split op `visual.jsRender.cijfer_om`):**
- **G4-doel G4-VBN-E01 — 127 items.** Regel: `cijfer_om == 10`. Langs de as staat dus om de 10 een getal.
  - 1 streep = 2: 83 items (max 20/30/40).
  - 1 streep = 5: 44 items (max 30/50).
- **G5-doel G5-VBN-E01 — 18 items.** Regel: `cijfer_om == 25`. Alleen 0, 25 en 50 staan erbij, en 1 streep = 5 (max 50).

**Reden:**
- SLO eind G4: 'een eenvoudige tabel, beeld- en staafdiagram aflezen, interpreteren en er bewerkingen mee uitvoeren' (meer/minder). G4-VBN-E01 dekt dat.
- Staan er om de 10 getallen langs de as, dan is aflezen 'vanaf het getal verder springen met 2 of 5'. Dat is G4-stof (G4-GET-M01: springen met 2, 5 en 10), binnen 50.
- Staan alleen 0/25/50 erbij, dan moet het kind de schaal echt gebruiken (25 + 2×5, of 25 − 10). Dat is G5: SLO eind G5 'weet wat een legenda is'. De merge parkeert dezelfde Claude-sjablonen (G2) met grotere schalen al in G5-VBN-E01.

**Voorwaarden (G4):**
- De bestaande G4-bank gebruikt alleen 'elk ■ = 1'. Deze items zijn dus een uitbreiding: zet ze op niveau toepassen of kritisch, niet op basis.
- Leg bij het eerste gebruik kort uit: "Elk streepje is 2." (of 5). Zet dat boven de vraag.
- De getallen om de 10 moeten zichtbaar zijn in de tekening.
- Laat `getallenruimte` volgen uit `max`. Nu staat er vaak '0–10' of '0–20' bij een diagram tot 40 of 50.
- Hint-richting: "Zoek het getal vlak onder de staaf. Spring dan verder met 2."

**Voorbeelden:**
- G4: G4-VBN-E01-claude-bank-twijfel-001 (streep 2, max 40, 'meer dan'), -074 (streep 2, aflezen), -009 (streep 5).
- G5: -002, -012, -022.

## 2. Centen (munten tot €2) — 103

**Besluit:**
- **G4-doel G4-MEET-E07 — 52 items.** Alle M5-items, plus 1 M5-item zonder M8-tweeling.
  - 22 onder €1 (alleen centmunten);
  - 28 tussen €1 en €2;
  - 2 met een heel bedrag (€1/€2).
- **Schrappen — 51 items.** Regel: `bron.claudeDoel == "M8"` EN dezelfde muntenset (`jsRender.munten`) als een M5-item.
  - Elk M8-item heeft precies dezelfde tekening, vraag ("Hoeveel geld zie je?") en hetzelfde antwoord als een M5-item. Alleen de afleiders verschillen soms (in 17 gevallen zijn ze ook gelijk).
  - In de json staat bij elk zo'n item `duplicaatVan`.

**Reden:**
- SLO eind G4 noemt letterlijk: 'kan bedragen tot en met 2 euro op verschillende manieren samenstellen met munten'. Munten tellen tot €2 is dus G4. G4-MEET-E07 noemt in de kop '≤2€ munten'.
- De komma in geldbedragen ('weet wat de komma betekent in geldbedragen', € 7,05 > € 6,95) is SLO eind G5 (G5-GET-M03, G5-MEET-E07). De spine-zin 'geen centen-kern / geld-komma = G5' gaat over die komma, niet over de munten.

**Voorwaarden (G4):**
- Notatie zonder komma, in antwoord én opties:
  - onder €1: "45 cent";
  - van €1 tot €2: "1 euro en 20 cent";
  - heel bedrag: "€1" of "€2".
- Afleiders als '€40' voor 40 cent worden "40 euro". Die denkfout (euro of cent) is nuttig om te houden.
- Leg bij het eerste gebruik uit: "100 cent is 1 euro."
- Bankconventie: G4, G5 en G6 schrijven '€20' en '€1,50' zonder spatie (0 keer '€ 1'). De vorm "1 euro en 20 cent" komt al voor in de G5-bank.
- Haal uit de fout-hints de tweede zin "Bij teruggeven: vul aan vanaf de prijs …" weg (bij 79 items). Hier wordt niets teruggegeven.
- Tekening verplicht (munten op ware kleur en grootte).
- Optioneel: de M8-afleiders (zoals '€4' = aantal munten, of '€81') kunnen als extra afleider naar het M5-item.

**Voorbeelden:**
- G4: G4-MEET-E07-claude-bank-twijfel-004 (40 cent), -001 (1 euro en 80 cent), -009 (heel bedrag).
- Schrappen: -072 (tweeling van -001), -053.

## 3. Deelteken ':' in verdeelverhalen — 41

**Besluit:** G5-doel G5-GET-M06, alle 41. Het teken blijft staan.

**Reden:**
- De opdracht is "Welke som hoort bij dit verhaal?", met de opties a : b, a × b en b : a. Die vraag toetst alleen de formele deelsom.
- Dat is SLO eind G5: 'kent het deelteken ':' … kan dit lezen, noteren' en 'kan bij een contextsituatie een formele deling geven'. In G4 is delen informeel (SLO: 'op informele manieren oplossen'), en de notitie bij G4-GET-E08 zegt 'geen formeel deelteken-algoritme'.
- De G4-bank gebruikt ':' alleen in 5 sterkere hints (E08-005, E08-007, E09-006, VERH-E02-006, VERH-E03-003), nooit in een opgave, optie of antwoord.
- Herschrijven in woorden ("60 gedeeld door 5") blijft een formele deelsom. Herschrijven naar "Hoeveel per kist?" maakt er een ander item van.
- De merge parkeert de deelsommen boven 100 van hetzelfde sjabloon al in G5-GET-M06 (51 items).

**Voorwaarden (G5):**
- Leg bij het eerste gebruik uit: "':' betekent gedeeld door."
- De notatie a : b met spaties voldoet aan onze regel: ':' is hier het deelteken, geen label.
- De fout-hint "Zet het in een verhoudingstabel" (Claude T9, groep 8) moet weg. Vervang die door bijvoorbeeld "Wat verdeel je? Dat getal komt vóór het deelteken."
- Getallen ≤100, ook 48 : 12, 55 : 11, 98 : 7, 84 : 6 en 78 : 6. Uitrekenen hoeft niet, dus dat is prima voor G5.

**Voorbeelden:** G4-GET-E08-claude-bank-twijfel-001, -020, -033.

## 4. Begrippen (ribben, vlakken, hoekpunten) — 6

**Besluit (split op `opgave`):**
- **G4-doel G4-MKU-E03 — 3 items.** De opgave bevat "vlakken":
  - -002 balk (6);
  - -005 kubus (6);
  - -006 piramide (5).
- **G5-doel G5-MKU-E02 — 3 items.** De opgave bevat "ribben" of "hoekpunten":
  - -001 ribben balk (12);
  - -004 ribben kubus (12);
  - -003 hoekpunten kubus (8).

**Reden:**
- G4-MKU-E04 (SLO: recht/schuin/hoek/punt; kubus, balk, bol en cilinder benoemen) noemt geen ribben of vlakken.
- Vlakken tellen sluit wel aan bij G4-MKU-E03 (bouwplaten kubus/balk/piramide). De bank zegt daar al 'balk = doos met zes vlakken'.
- Ribben en hoekpunten tellen, ook de verborgen, is geen G4-tussendoel. Het past bij G5-MKU-E02 (bouwplaat: 'welke randen plakken tegen elkaar'; een ribbe is zo'n plakrand).

**Voorwaarden:**
- Leg de termen kort uit:
  - vlak = "een platte kant";
  - ribbe = "de rand waar twee vlakken tegen elkaar zitten";
  - hoekpunt = "een punt waar randen samenkomen".
- Een tekening met doorzichtige of gestippelde achterkant is verplicht, want de vraag zegt 'tel ook wat je niet ziet'.
- -006: de tekening moet een vierkant grondvlak laten zien, anders klopt 5 niet.

**Voorbeelden:** G4-MKU-E04-claude-bank-twijfel-002 (G4), -006 (G4), -001 (G5).

## 5. Vormnaam piramide — 1

**Besluit:** G4-doel G4-MKU-E03 (G4-MKU-E04-claude-bank-twijfel-007).

**Reden:**
- De naam piramide staat niet in G4-MKU-E04. Die doelkop noemt alleen kubus, balk, bol en cilinder, en de merge-fix W4 haalt piramide daar weg als afleider.
- Wel noemt SLO eind G4 bij bouwplaten 'zoals een kubus, balk, piramide'. De G4-bank gebruikt de naam al in E03 (opties bol, kubus, piramide, cilinder). Herkennen past dus bij E03.
- Het volledige benoemen van vormen hoort bij SLO eind G6 (G6-MKU-E04).

**Voorwaarden:**
- Tekening verplicht.
- De hint 'denk aan een tent met een punt' is goed.

## 6. Puzzel (trap) — 1

**Besluit:** G4-doel G4-GET-E09 (G4-GET-E09-claude-bank-twijfel-001).

**Reden:** eerst tel je de trappen tussen de verdiepingen (2, niet 3), dan reken je 2 × 12 in context. Dat is een meerstapsvraag ≤100 met een denkstap, en die kern dekt G4-GET-E09 ('combinaties van bewerkingen in context ≤100').

**Voorwaarden:**
- Een tekening van drie verdiepingen met twee trappen.
- Leg 'treden' uit: "de stapjes van een trap".
- Schrijf "van de 1e naar de 3e verdieping". Let op: kinderen tellen de begane grond soms mee.
- Er is geen automatische antwoordcontrole (`controle.antwoord` = n.v.t.). Handmatig gecontroleerd: 24 klopt.

---

## Samenvatting

| Categorie | Aantal | G4 | G5 | Schrappen |
|---|---:|---:|---:|---:|
| Schaal | 145 | 127 (VBN-E01) | 18 (VBN-E01) | 0 |
| Centen | 103 | 52 (MEET-E07) | 0 | 51 (dubbel) |
| Deelteken | 41 | 0 | 41 (GET-M06) | 0 |
| Begrippen | 6 | 3 (MKU-E03) | 3 (MKU-E02) | 0 |
| Vormnaam | 1 | 1 (MKU-E03) | 0 | 0 |
| Puzzel | 1 | 1 (GET-E09) | 0 | 0 |
| **Totaal** | **297** | **184** | **62** | **51** |

**Huisregels:**
- Alle getallen zijn ≤100: geen punt-notatie en geen machten nodig.
- Geld zonder spatie, zoals in de bank ('€1,50'). In G4 zonder komma (zie §2).
- Termen bij het eerste gebruik uitleggen: streepje-waarde, cent, ':', vlak, ribbe, hoekpunt, treden.

**Datacheck:**
- Geen dubbele opties en geen antwoorden die niet in de opties staan.
- `controle.antwoord` is 'ok' bij 296 items en 'n.v.t.' bij 1 (de trappuzzel, nagerekend).

## Open vragen voor Dave/Overzicht

1. **Centen-notatie:** de SLO legt de komma pas in G5. Als je in G4 tóch '€1,20' wilt (zoals op prijskaartjes), gaan de 28 items van 1–2 euro beter naar G5-GET-M03 (komma lezen). Dan blijven er 24 in G4.
2. **Schaal:** in G4 komen nu 127 items met streepje-waarde 2/5 bij een bank die tot nu toe alleen '■ = 1' kende. Dat is veel. Je kunt het aantal in de app begrenzen, of alleen streep 2 nemen (83) en streep 5 (44) ook naar G5.
3. **Ribben en hoekpunten:** zijn geen expliciet SLO-tussendoel in G4 of G5. Ik koos G5-MKU-E02 (plakranden). Schrappen kan ook (3 items).
4. **Centen M8-tweelingen:** het M5-item blijft staan. Wil je liever de M8-afleiders, dan kan dat per paar via `duplicaatVan`.
