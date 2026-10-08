# Besluiten twijfelgevallen G8-merge (Claude-vragen) — Didactiek

Datum: 2026-10-01 · Bron: `data/twijfel.json` (1226 items in 8 categorieën, build 19.12 uur) en `twijfel_voor_didactiek.md` · Machineleesbaar: `besluiten_twijfel.json` (id → besluit, doelId en doelGroep, met nieuwe opgave, opties, antwoord, geldige antwoorden, fout-hints en hints per item) · Generator: `/workspace/g8did/besluiten.py`, check: `/workspace/g8did/check_besluiten.py`

Verwerkt: de antwoorden van Overzicht van 20.39 uur (doelId per verplaatst item; hints in G4–G7 zijn een voorstel; tekeneis voor de torens; badge «nieuw» voor geheugenomvang).

Referenties:
- SLO-tussendoelen (`leerlijn/rekenen-groep7/tussendoelen.txt`; eind G4 vanaf r. 3257, G5 r. 3516, G6 r. 3842, G7 r. 4223, G8 r. 4668, 1S r. 5083):
  - schatten: eind G4 r. 3293–3295 ('schattend optellen en aftrekken tot ten minste 100'); eind G5 r. 3586–3588 (tot ten minste 1000) en r. 3640–3641 ('schattend vermenigvuldigen onder ten minste 1000 … 8 x 39 is ongeveer 8 x 40'); eind G8 r. 4734–4736 en 4766–4768 (schattend rekenen 'en op basis daarvan eventueel nog een correctie toepassen'); 1S r. 5160–5163 ('door gegeven hele getallen af te ronden en er vervolgens berekeningen mee te maken … als controle voor rekenen met de rekenmachine en … als getallen in een context niet precies gegeven zijn') en r. 5273–5274 (controleren door te schatten).
  - temperatuur en negatieve getallen: eind G7 r. 4581–4582 (temperatuur onder 0 aflezen); eind G8 r. 4984–4986 ('doorziet de relatie tussen het meten van de temperatuur boven en onder nul met de getallenlijn (bv.: … als de temperatuur met 6 graden stijgt vanaf -5 dan is het dus 1 graad boven nul)').
  - inhoud: eind G7 r. 4561–4566 ('In een doos met een inhoud van 1 dm3 passen 1000 blokjes van 1 cm3'; 'inhoud van een balkvormig figuur … lengte x breedte x hoogte'); eind G8 r. 4968 ('doorziet het systeem van inhoudsmaten in het metrieke stelsel … toepassen bij herleiden'); 1S r. 5489–5490.
  - meetkunde: eind G6 r. 4174–4175 ('kan plaatsen of objecten op een kaart vinden en aanduiden met een rooster met coördinaten (bv.: De Domtoren ligt in vak C5.)') en r. 4186 ('kan een blokkenbouwsel construeren en hiervan een plattegrond met hoogtegetallen maken en omgekeerd'); eind G7 r. 4652 ('assenstelsel met positieve getallen').
  - verhoudingen en procenten eind G8: r. 4868–4869 (telling als verhouding), r. 4879–4881 (relatie niet direct zichtbaar), r. 4893–4894 (procent via breuk of kommagetal), r. 4899–4902 (toename en afname in procenten).
  - gegevens eind G8: r. 5064–5066 (aflezen, vergelijken, trends, voorspellen), r. 5076–5077 ('kritisch denken en redeneren over … de juistheid van conclusies'); gemiddelde eind G7 r. 4398 en 1S r. 5246.
  - eind G8 r. 4720: 'beheerst de doelen van groep 2 t/m 7, ook op het niveau van groep 8'.
- Kerndoelen rekenen-wiskunde 2025 (`leerlijn/rekenen-groep7/bronnen/kerndoelen-rw.txt`): PO kerndoel 11A r. 590–592 (grootheden, ook 'geheugenomvang'); PO 12A r. 613 (gemiddelde); kans in het VO: r. 375–379 en 393–394, VO 11B r. 882–884; modus en mediaan: VO 11A r. 860.
- `leerlijn/rekenen-groep8/SPINE_G8_v1.md` r. 222 ('Negatieve getallen buiten temperatuurcontext als apart getalsysteem' niet in G8), r. 223 ('Kansrekening formeel'), r. 226 (negatieve assen), r. 227 ('Mediaan/modus … niet als G8-einddoel'). Spine G6: G6-MKU-E01 'Kaart lezen: schaal, legenda, vakjes, windrichting', G6-MKU-E03 'Blokkenbouwsel ↔ plattegrond met hoogtegetallen'.
- Methodes: De wereld in getallen 5, kinddoelen groep 8 (Malmberg): blok 2 'Je leert bewerkingen schattend uitrekenen, in contexten waarbij het zinvol is om te schatten'; blok 7 'Je herhaalt het gemiddelde berekenen', 'Je oriënteert je op negatieve getallen', 'Je herhaalt het berekenen van het aantal blokken van een bepaalde afmeting, dat in een grotere doos past'. Kans, mediaan en modus staan niet in de kinddoelen van groep 8. Pluspunt groep 8 doet meer met negatieve getallen (ook kale sommen); wij volgen SLO en de spine. Blokkenbouwsels met hoogtegetallen zijn lessen voor groep 6 (bv. LessonUp groep 6: 'Ik kan op grond van hoogtegetallen bepalen uit hoeveel blokken een bouwsel bestaat').
- G8-bank (`exports/leermees-vragenbank-export/vragenbank_g8.json`), de gemapte G8-items (`data/per_doel/`) en de G7-besluiten (`g7/besluiten_twijfel.md/.json`) als precedent. Dubbelcontrole tegen de bank en de gemapte items.

Besluitwaarden in de json (zoals bij G7): `houden` (blijft in het voorgestelde doel, zoals het is), `verplaatsen` (alleen het doel verandert, de tekst blijft), `aanpassen` (opgave, opties of fout-hints veranderen; ook als het item daarbij naar een ander doel gaat, dan met de vlag `verplaatst`), `schrappen`, `buitenBasisschool` (niet nodig in deze 1226). Elk item heeft `doelId` en `doelGroep` van de bestemming; items voor G4–G7 hebben ook `aanvulling` (het vaste aanvullingsbestand van die groep, zoals `g7/data/aanvulling_uit_g8.json`) en `hintStatus` = voorstel: daar schrijft Oefeningen de definitieve hints. Alle 1226 ids zijn precies één keer gedekt (controle met script).

Huisregels in alle nieuwe teksten (en nagekeken met de checkers, zie onderaan): 4 cijfers zonder punt en vanaf 10.000 met punt; geen machten van getallen (in G8 mogen cm² en cm³, `notatie_machten.md`); ':' alleen als gedeeld door; '−' als minteken; bij keersommen eerst het aantal groepen; geen Engelse woorden en geen vreemde contexten; geen optieletters in hints; kleur nooit het enige kenmerk; referentiematen volgens `referentiematen.json`; geen fout-hint die het antwoord verklapt.

---

## 1. `bouwsel-tellen` — 551 items · voorstel G8-MKU-V01

De Claude-tekenaar heeft twee soorten tekeningen. Die krijgen elk een eigen besluit.

**Besluit (split):**
- **151 volle balken** (`jsRender` soort `bouwsel`, {diep, hoog, breed}, antwoord = diep × hoog × breed, alle 151 goed): **aanpassen** en naar **G8-MEET-V01** (onderhoud inhoud eind G7). Opgave blijft. Fout-hints opnieuw per denkfout. Daarvan zijn **50 dubbel** (zelfde maten als een eerder item): die blijven, met nieuwe maten (G7-precedent: dubbels blijven met nieuwe getallen).
- **400 torenbouwsels** (`jsRender` soort `bouwvorm`, stapels): **aanpassen** en naar **G6-MKU-E03** (doelGroep 6, na de 8 canonieke items). Opgave verduidelijkt, fout-hints per denkfout, Hint 2 met de plattegrond met hoogtegetallen.
- Schrappen 0, buitenBasisschool 0. Totaal aangepast 551, waarvan naar ander doel 551 (naar G6: 400).

**Reden:**
- Blokjes in een volle balk tellen is inhoud = lengte × breedte × hoogte. SLO eind G7 r. 4561–4566: 'In een doos met een inhoud van 1 dm3 passen 1000 blokjes van 1 cm3' en 'kan de inhoud van een balkvormig figuur bepalen door gebruik te maken van de formule lengte x breedte x hoogte'. In G8 is dat onderhoud (r. 4720) en De wereld in getallen herhaalt het in groep 8 blok 7. G8-MKU-V01 gaat over kijklijnen en standpunt, daar hoort het niet. Niet terug naar G7: G7-MEET-03 heeft al 1360 van zulke items.
- Torens van blokjes tellen in een tekening is eind G6: r. 4186 'kan een blokkenbouwsel construeren en hiervan een plattegrond met hoogtegetallen maken en omgekeerd'. G8 heeft geen doel voor blokjes tellen. De G6-merge heeft geen MKU-items, dus dit vult een gat (Overzicht 20:39: 531 items in G6-MKU is goed).

**Regel (de json past hem per id toe):**
- Balk, fout-hints per afleider: diep + hoog + breed → 'Je telde de drie maten op. Het bouwwerk is vol. …' · alleen de buitenkant → 'Je telde alleen de blokjes die je aan de buitenkant ziet. …' · diep × breed → 'Dat is één laag. Er liggen {hoog} lagen op elkaar.' · één kant → 'Dat zijn de blokjes van één kant. …' · een laag te veel of te weinig → 'Je telde een laag te veel/te weinig. …' · de helft → 'Je telde maar de helft. …' · anders → 'Reken eerst uit hoeveel blokjes er in één laag liggen. Doe dat daarna keer het aantal lagen.' Hint 1 'Tel eerst hoeveel blokjes er in één laag liggen.' Hint 2 'Eén laag is {diep} rijen van {breed} blokjes. Hoeveel lagen liggen er op elkaar?'
- Balk-dubbels (50): het item met het laagste nummer houdt zijn maten; de andere krijgen nieuwe, nog niet gebruikte maten (2 tot en met 7, inhoud dicht bij het oude antwoord, hoogstens 180) en de opties [inhoud, één laag, drie maten opgeteld]; `duplicaatVan` wijst naar het eerste item.
- Torens: nieuwe opgave «Dit bouwwerk bestaat uit torens van blokjes. Elke toren staat op de grond, er zitten geen gaten onder. Hoeveel blokjes zijn er gebruikt?» (was «Er zitten geen gaten in dit bouwwerk. Hoeveel blokjes zijn er gebruikt?»; 'geen gaten' was onduidelijk). Fout-hints, in deze volgorde: volle balk (rijen × kolommen × hoogste toren) → 'Het bouwwerk is geen volle balk. …' · hoogste toren × aantal torens → 'Niet alle torens zijn even hoog. …' · aantal torens → 'Je telde het aantal torens. …' · vakjes van het grondvlak → 'Je telde de vakjes van het grondvlak. …' · 1 of 2 ernaast → 'Je zit er net naast. Tel toren voor toren …' · anders → 'Tel toren voor toren hoeveel blokjes er op elkaar staan. …'. Hint 1 'Tel per toren hoeveel blokjes er op elkaar staan. Tel daarna alles op.' Hint 2 'Kijk naar de plattegrond. In elk vakje staat hoeveel blokjes die toren hoog is. Tel de getallen op.'

**Tekeneis torens (Overzicht 20:39, per itemgroep; in de json als `visual.tekeneis` A of B):**
- G6-MKU-E03 toetst bouwsel ↔ plattegrond met hoogtegetallen, geen aanzichten. Daarom: schuin vooraanzicht (kijker schuin van voren en iets van boven), elk blokje met zichtbare randen, en géén los vooraanzicht of bovenaanzicht in de opgave. De plattegrond met hoogtegetallen (bovenaanzicht met in elk vakje het aantal blokjes, `visual.hint2Plaatje`) komt bij Hint 2.
- **Groep A (71 items):** in alle vier de schuine richtingen is elke torentop te zien. De app kiest de standaardrichting rechtsvoor.
- **Groep B (329 items):** niet in elke schuine richting is elke torentop te zien, vanaf rechtsvoor wel (kijker bij de laatste rij en de laatste kolom van `jsRender.stapels`). Die richting is verplicht; per item staat in `visual.verborgenTorentoppen` hoeveel torentoppen elke andere richting verbergt.
- Gecontroleerd: bij alle 400 is vanaf rechtsvoor geen torentop verborgen. Een schuine tekening kan toch dubbelzinnig blijven (een lage toren achter een hoge). Daarom staat de plattegrond met hoogtegetallen bij Hint 2.
- Dubbels torens: 0 met precies dezelfde stapels. 21 vormen zijn gelijk aan een eerdere vorm na draaien of spiegelen (`bijnaDubbelVan`). Die blijven: het kind ziet een andere tekening, al is het antwoord gelijk. Geen echt dubbel, dus geen `duplicaatVan`.

**Voorbeelden:**
- 001 (balk 6 × 5 × 4, antwoord 120): fout-hint bij 15 was «Let op het teken: het is een keersom. …» → «Je telde de drie maten op. Het bouwwerk is vol. Reken eerst uit hoeveel blokjes er in één laag liggen, en dan voor alle lagen samen.»; bij 60 → «Je telde maar de helft. …».
- 013 (balk 3 × 3 × 4 = 004): nieuwe maten 2 × 3 × 7, opties 42 · 14 · 12, antwoord 42.
- 161 (torens, antwoord 44): fout-hint bij 45 «Niet alle torens zijn even hoog. Tel elke toren apart en tel de aantallen daarna op.»; bij 9 «Je telde het aantal torens. …».

**Voorwaarden:** de balktekening laat alle drie de maten telbaar zien; voor de torens geldt de tekeneis hierboven. Overzicht laat een steekproef van de torentekeningen nakijken na het tekenen.

---

## 2. `negatief-zonder-context` — 217 items · G8-MEET-E05

**Besluit:** **aanpassen — 217 items** in G8-MEET-E05: de kale vraag krijgt een temperatuurcontext. Schrappen 0, ander doel 0.

**Reden:** kaal rekenen met negatieve getallen is geen G8-doel (spine r. 222). Temperatuur boven en onder nul met de getallenlijn wel: SLO eind G8 r. 4984–4986 ('doorziet de relatie tussen het meten van de temperatuur boven en onder nul met de getallenlijn'). De wereld in getallen 5, groep 8 blok 7: 'Je oriënteert je op negatieve getallen'. Vorm zoals bank G8-MEET-E05-003. Alle 217 antwoorden waren goed (getallen −4 tot 12, stappen 3 tot 19, antwoorden −23 tot −1).

**Regel:**
- a ≥ 0: «Welk getal ligt {n} lager dan {a}?» → «Het is {a} °C. Het wordt {n} graden kouder. Hoe koud is het dan, in °C?»
- a < 0: → «Het is {a} °C. Dat is {|a|} graden onder nul. Het wordt {n} graden kouder. Hoe koud is het dan, in °C?»
- Invulveld met '°C' erachter. Geldige antwoorden (vaste lijst): «−9», «-9», «−9 °C», «-9 °C».
- Fout-hints: a + n → 'Kouder betekent omlaag op de thermometer. Jij ging omhoog.' · zonder minteken → 'Kijk waar je uitkomt: boven of onder nul? Onder nul schrijf je een − voor het getal.' · 1 ernaast → 'Je zit er 1 naast. Tel op de thermometer nog eens, één streepje per graad. Ga eerst naar 0 en dan verder omlaag.' · anders → 'Begin op de thermometer bij {a} °C en ga {n} streepjes omlaag.' (De Claude-hint «Kijk goed naar de nullen. Reken eerst de tafelsom …» paste bij geen enkel item.)
- Hint 1 'Kouder is omlaag op de thermometer.' Hint 2 (a > 0) 'Ga eerst naar 0. Hoeveel graden moet je daarna nog omlaag?', (a ≤ 0) 'Je bent al onder nul. Kouder is nog verder omlaag. Tel de streepjes op de thermometer.'
- 8 items hadden na de context dezelfde som als de bank (2 °C en 7 kouder · −2 °C en 5 kouder · −4 °C en 3 kouder): die krijgen een andere stap (eerste vrije n), met `duplicaatVan` 'bank G8-MEET-E05'.

**Voorbeelden:** 001 «Welk getal ligt 16 lager dan 7?» → «Het is 7 °C. Het wordt 16 graden kouder. Hoe koud is het dan, in °C?» (−9). 150 «Welk getal ligt 15 lager dan −3?» → «Het is −3 °C. Dat is 3 graden onder nul. Het wordt 15 graden kouder. Hoe koud is het dan, in °C?» (−18). 145 «… 7 lager dan 2» (gelijk aan bank 003) → «Het is 2 °C. Het wordt 20 graden kouder. …» (−18).

**Voorwaarden:** aanbevolen plaatje bij Hint 2: een staande thermometer van −25 °C tot 15 °C, een streepje per graad, een getal per 5 graden.

---

## 3. `schatten-zonder-afspraak` — 180 items · voorstel G8-GET-E02

**Besluit:** **aanpassen — 180 items**: elke vraag krijgt een afrondafspraak. Daarna per getallenruimte (HOOFDREKENGRENS, zie regel):
- 109 blijven in **G8-GET-E02** (getallenruimte boven 1000);
- 41 naar **G5-GET-E05** (plus en min, getallen en uitkomst tot 1000);
- 10 naar **G5-GET-E07** (keer, onder 1000);
- 20 naar **G4-GET-E05** (plus en min tot 100).
Waarvan naar andere groep: 71. Schrappen 0.

**Reden:**
- Zonder afspraak zijn meer antwoorden goed (84 + 87 is 'ongeveer' 170, maar ook 200). Met de afspraak in de vraag heeft het item één goed antwoord, zoals de gemapte G8-GET-E02-items 022–029 en 052–059 en bank G8-GET-E02-001. SLO 1S r. 5160–5163: 'door gegeven hele getallen af te ronden en er vervolgens berekeningen mee te maken'.
- Schatten moet een functie hebben: 1S r. 5162–5163 (als controle en als getallen niet precies gegeven zijn); De wereld in getallen groep 8: 'in contexten waarbij het zinvol is om te schatten'. Bij 16 + 31 rekent een kind in groep 8 sneller precies dan dat het schat. Zulke items horen bij het doel waar schatten met die getallen nieuw is: eind G4 r. 3293–3295 (tot 100), eind G5 r. 3586–3588 (plus en min tot 1000) en r. 3640–3641 (keer onder 1000). De G4-merge heeft in G4-GET-E05 maar 1 item, de G5-merge heeft geen schatitems: dit vult een gat.
- Boven 1000 blijft het G8: eind G8 r. 4734–4736 en 4766–4768 (schatten met hele getallen, met correctie); de afspraak is de basisstap daarvoor.

**Regel:**
- HOOFDREKENGRENS (fix 20:38): getallenruimte = het grootste van de twee getallen en de precieze uitkomst. Plus en min: tot en met 100 → G4-GET-E05; tot en met 1000 → G5-GET-E05; anders G8-GET-E02. Keer: onder 1000 → G5-GET-E07; anders G8-GET-E02.
- De afspraak is de afronding die precies het Claude-antwoord geeft (bij alle 180 gevonden): «Rond beide getallen af op {tientallen|honderdtallen|duizendtallen} en reken dan uit.» · «Rond {a} af op X en {b} op Y, en reken dan uit.» · bij een factor van één cijfer «Rond {a} af op X en reken dan uit.». De zin komt achter de vraag.
- Fout-hints per fout: de precieze uitkomst → 'Dat is het precieze antwoord. Hier maak je een schatting. Rond eerst af zoals in de vraag staat.' · de uitkomst bij een verkeerde afrondrichting → 'Kijk naar het cijfer achter de plek waarop je afrondt. Is het 5 of meer, dan rond je naar boven af. Anders rond je naar beneden af.' · de uitkomst bij afronden op een andere plek → 'Kijk goed op welke plek je moet afronden. De vraag zegt dat je op {X} afrondt.' · anders → 'Schatten is rekenen met ronde getallen. Rond eerst af zoals in de vraag staat, en reken dan.' (De Claude-hint 'elk naar het dichtstbijzijnde ronde getal' paste niet bij een afspraak.)
- Hint 1 'Rond eerst af zoals in de vraag staat.' Hint 2 'Kijk naar het cijfer achter de plek waarop je afrondt. Reken daarna met de ronde getallen.' Geldige antwoorden: vanaf 1000 beide vormen (12.000 en 12000; 4 cijfers zonder punt).
- Dubbelcontrole binnen de categorie en tegen de gemapte G8-GET-E02-sommen: 0 dubbels.

**Voorbeelden:** 006 «Hoeveel is 16 + 31 ongeveer?» → «… Rond beide getallen af op tientallen en reken dan uit.» (50, G4-GET-E05). 001 «Hoeveel is 84 + 87 ongeveer?» → idem (170, G5-GET-E05; fout 200 → 'Kijk goed op welke plek je moet afronden. De vraag zegt dat je op tientallen afrondt.'). 101 «Hoeveel is 18 × 54 ongeveer?» → «… Rond beide getallen af op tientallen …» (1000, G5-GET-E07). 091 «Hoeveel is 189 × 61 ongeveer?» → «… Rond 189 af op honderdtallen en 61 op tientallen, en reken dan uit.» (12.000, G8). 004 «Hoeveel is 4250 + 7642 ongeveer?» → «… Rond beide getallen af op duizendtallen …» (12.000, G8).

**Voorwaarden:** in G4 en G5 zijn de hints een voorstel (Oefeningen schrijft ze daar).

---

## 4. `vakcode-plattegrond` — 131 items · voorstel G8-VBN-V01

**Besluit:** **aanpassen — 131 items** en naar **G6-MKU-E01** (doelGroep 6, na de 8 canonieke items). Fout-hints erbij (er waren er 0). Schrappen 0.

**Reden:** een vak aanwijzen met een letter en een cijfer ('In welk vak staat de bank?') is eind G6: r. 4174–4175 'kan plaatsen of objecten op een kaart vinden en aanduiden met een rooster met coördinaten (bv.: De Domtoren ligt in vak C5.)'; ook 1S r. 5609–5610. Het G8-doel G8-VBN-V01 is het assenstelsel met (x, y) (eind G7 r. 4652), dat is iets anders. Alle 131 antwoorden en keuzes nagekeken tegen `jsRender.dingen`, ook de 12 met 'controle n.v.t.' (kolom G en H): 131 goed. Dubbels (zelfde plattegrond en zelfde vraag): 0.

**Regel:**
- 'Wat staat er in vak X?': afleider in dezelfde kolom → '{De/Het ding} staat in de goede kolom, maar in een andere rij. Kijk bij vak X goed naar het cijfer naast de rij.' · in dezelfde rij → '… in de goede rij, maar in een andere kolom. Kijk bij vak X goed naar de letter boven de kolom.' · ergens anders → '{De/Het ding} staat in vak Y. Zoek bij vak X eerst de kolom met die letter, dan de rij met dat cijfer. Waar ze elkaar raken, is het vak.' · niet op de kaart → '… staat niet op deze plattegrond. …'
- 'In welk vak staat …?': zelfde letter → 'De letter klopt. Kijk nog eens naar het cijfer naast de rij waarin … staat.' · zelfde cijfer → 'Het cijfer klopt. Kijk nog eens naar de letter boven de kolom …' · anders → 'In vak Y staat … / Vak Y is leeg. Zoek eerst …, en kijk dan naar de letter erboven en het cijfer ernaast.'
- Lidwoord: 'het' bij hek en huis, anders 'de'. Geen losse letters in de hints (de optieletter-check vangt losse A–D; we noemen altijd het hele vak, zoals 'vak C5').
- Hint 1 'Zoek de letter boven de kolom en het cijfer naast de rij.' Hint 2 'Waar de kolom en de rij elkaar raken, is het vak.'

**Voorbeeld:** 050 «Wat staat er in vak G1?» (tent; keuzes tent · bal · hek): bij bal «De bal staat in de goede rij, maar in een andere kolom. Kijk bij vak G1 goed naar de letter boven de kolom.»; bij hek «Het hek staat in de goede kolom, maar in een andere rij. …».

**Voorwaarden:** letters boven de kolommen, cijfers naast de rijen; elk ding als plaatje mét het woord erbij (kleur nooit het enige kenmerk). Hints in G6 zijn een voorstel.

---

## 5. `kan-kloppen-zonder-opties` — 96 items · voorstel G8-GET-E02

**Besluit:** **aanpassen — 96 items**: van open vraag naar echte meerkeuze met 3 keuzes. Daarna dezelfde HOOFDREKENGRENS als bij 3:
- 27 blijven in **G8-GET-E02**;
- 24 naar **G5-GET-E05**, 29 naar **G5-GET-E07**, 16 naar **G4-GET-E05**.
Waarvan naar andere groep: 69. Schrappen 0.

**Reden:** 'Kijk zonder uit te rekenen. Welk antwoord … kan kloppen?' zonder keuzes is een gewone rekensom. Met keuzes toetst het schattend controleren: SLO eind G8 r. 4734–4736 ('kan beredeneren of de werkelijke uitkomst (veel) groter of kleiner is dan de geschatte uitkomst'), 1S r. 5273–5274 (controleren door te schatten), eind G5 r. 3586–3588 (zelfde zin, tot 1000). Echte meerkeuze zoals Dave bij G7 (punt 5): de keuzes in het optieveld.

**Regel:**
- Opties: het goede antwoord en de 2 Claude-denkfouten (`extraVelden.claudeDenkfouten`), gehusseld. Elke afleider moet zonder uitrekenen uit te sluiten zijn: een ander laatste cijfer, of buiten de grenzen (beide getallen naar beneden en naar boven afronden op tientallen, bij getallen vanaf 100 op honderdtallen). Lukt dat niet, dan een vervangende afleider (eerst antwoord × 10, dan antwoord + 10 tientallen of honderdtallen): 25 afleiders vervangen (`vervangenAfleiders` per item).
- Fout-hint per afleider (`hintSoort`): ver weg (minstens 2 keer zo groot of hoogstens de helft) → 'Rond eerst af. {a′} {op} {b′} is {schatting}. Ligt {fout} daar dichtbij?' · boven de bovengrens → 'Rond allebei naar boven af. {..} + {..} is {grens}. De uitkomst kan dus niet groter zijn dan {grens}, en {fout} is groter.' (bij min: de eerste naar boven, de tweede naar beneden; bij keer: het grote getal naar boven) · onder de ondergrens → idem met 'naar beneden' en 'niet kleiner' · zelfde grootte, ander laatste cijfer → 'Kijk naar het laatste cijfer. De uitkomst van {a} {op} {b} eindigt op {d}. Eindigt {fout} daarop?'. Geen dubbele punt, geen optieletters.
- Verdeling: 73 ver weg · 45 bovengrens · 15 ondergrens · 59 laatste cijfer.
- Hint 1 'Rond de getallen af en kijk welk antwoord in de buurt ligt.' Hint 2 'Kijk ook naar het laatste cijfer van de uitkomst.' Dubbels: 0.

**Voorbeelden:** 185 «… bij 39 + 35 kan kloppen?» → keuzes 74 · 84 · 4 (G4-GET-E05); bij 84 «Rond allebei naar boven af. 40 + 40 is 80. De uitkomst kan dus niet groter zijn dan 80, en 84 is groter.»; bij 4 «Rond eerst af. 40 + 40 is 80. Ligt 4 daar dichtbij?». 181 «… bij 737 + 776 …» → 1513 · 2513 · 1511 (G8); bij 1511 «Kijk naar het laatste cijfer. De uitkomst van 737 + 776 eindigt op 3. Eindigt 1511 daarop?». 212 «… bij 25 × 5 …» → 125 · 225 · 30 (G5-GET-E07).

---

## 6. `geheugenomvang` — 28 items · G8-MEET-E03 · badge «nieuw»

**Besluit:** **aanpassen — 28 items** in G8-MEET-E03, met `badge: 'nieuw'` (Overzicht 20:39: nieuw kerndoel vanaf augustus 2026). Schrappen 0.

**Reden:** geheugenomvang staat in kerndoel 11A van 2025 (r. 590–592: '… temperatuur en geheugenomvang'), niet in de tussendoelen van 2017. Het rekenwerk is herleiden met stappen van 1000 (KB → MB → GB → TB), zoals bij inhoudsmaten (eind G8 r. 4968: 'doorziet het systeem van inhoudsmaten … toepassen bij herleiden'; 1S r. 5468 voorvoegsels). Daarom bij G8-MEET-E03 (maten als systeem), zonder eigen doel. De contexten waren vreemd ('Een foto van de botten is 800 MB') en de tweede fout-sleutel kwam uit rekenen met 1024 (3.072.000), wat in de les niet voorkomt.

**Regel:**
- 001–016: «Een foto van de {x} is {m} MB. De geheugenkaart is {g} GB. Hoeveel van die foto's passen erop?» → «Een filmpje is {m} MB. De geheugenkaart is {g} GB (1 GB = 1000 MB). Hoeveel van die filmpjes passen erop?». Fout-hints: een nul te weinig → 'Je hebt een nul te weinig. Zet eerst alles in MB. {g} GB is {g·1000} MB.'; een nul te veel → 'Je hebt een nul te veel. Reken {g·1000} : {m} en let goed op de nullen.'
- Na het weghalen van de context waren 3 items gelijk aan een eerder item: 012 (= 004) → 800 MB en 32 GB (40) · 013 (= 006) → 200 MB en 64 GB (320) · 014 (= 009) → 100 MB en 16 GB (160); met `duplicaatVan`.
- 017: «Een geheugenkaart heeft 3 GB.» → «Een film is 3 GB.»; 018–020 blijven («Een geheugenkaart heeft {n} GB»). 021–023: «Een geheugenkaart heeft {n} MB.» → «Een foto is {n} MB.». 024–028: «Een geheugenkaart heeft {n} TB.» → «Een harde schijf heeft {n} TB.».
- 017–028 fout-sleutel {n}·1024·1000 → {n}·10.000 met 'Keer 1000 betekent drie nullen erbij, niet vier.'; de sleutel {n}·100 houdt '1 GB is 1000 MB, niet 100.'
- Hint 1 'Zet eerst alles in MB.' / '1 {grote maat} is 1000 {kleine maat}.' Hint 2 '{g} GB is {g} keer 1000 MB. Hoe vaak past {m} MB daarin?' / 'Keer 1000 betekent drie nullen erbij.'

**Voorbeelden:** 001 → «Een filmpje is 800 MB. De geheugenkaart is 16 GB (1 GB = 1000 MB). Hoeveel van die filmpjes passen erop?» (20). 021 → «Een foto is 3 MB. Hoeveel KB is dat? (1 MB = 1000 KB)» (3000; fout 30.000). 024 → «Een harde schijf heeft 3 TB. Hoeveel GB is dat? (1 TB = 1000 GB)» (3000).

---

## 7. `statistiek-gemengd` — 22 items · voorstel G8-VBN-E04

**Besluit (per item):** houden 3 · verplaatsen 11 · aanpassen 7 · schrappen 1. Waarvan naar ander doel 18 (naar andere groep 4).

**Reden:** de categorie mengt echte G8-gegevensvragen met procent, gemiddelde, maten en gewone sommen. Elk item gaat naar het doel van zijn rekenkern. Per item:

| nr | besluit | doel | reden (kort) | wijziging |
|---|---|---|---|---|
| 001 | verplaatsen | G8-VERH-V01 | procent als deel van 200: eind G7 r. 4495/4499, onderhoud | — |
| 002 | aanpassen | G8-VBN-V01 | cirkeldiagram aflezen: eind G7, onderhoud; kleur niet als enig kenmerk | kleuren → sporten (voetbal, hockey, tennis); fout-hints aangepast |
| 003 | aanpassen | G8-GET-V02 | gemiddelde terugrekenen: 1S r. 5246, eind G7 r. 4398 | fout-hint bij 1,6: «… door te vermenigvuldigen, niet door te delen» → «… met keer, niet met delen» |
| 004 | houden | G8-VBN-E04 | kritisch over een diagram: eind G8 r. 5076–5077 | — |
| 005 | aanpassen | G8-VBN-V01 | lijngrafiek aflezen: eind G7 r. 4645–4652, onderhoud | lijngrafiek verplicht (8.00 uur 12 °C · 12.00 uur 18 °C · 16.00 uur 15 °C), getallen uit de tekst |
| 006 | verplaatsen | G8-MEET-V01 | liter → milliliter en delen: maten eind G7, onderhoud | — |
| 007 | verplaatsen | G8-VBN-E01 | trend voorspellen: eind G8 r. 5064–5066 | — |
| 008 | verplaatsen | G8-VERH-E05 | procent afname: eind G8 r. 4899–4902 | — |
| 010 | verplaatsen | G8-VBN-V01 | as aflezen tussen streepjes: eind G7, onderhoud | — |
| 011 | aanpassen | G7-DENK-03 | meerstapssom (7 × 24 − 18), zoals regel G8-T8-meerstaps | «De kind haalt» → «Noor haalt» |
| 012 | schrappen | — | grootste van drie getallen kiezen: groep 3/4-niveau (G7 kans-023) | — |
| 013 | verplaatsen | G5-GET-E05 | 45 + 38 + 92 + 55: optellen tot 1000, eind G5 r. 3586 | — |
| 014 | aanpassen | G8-VERH-E02 | verhouding 3 → 5, niet direct zichtbaar: eind G8 r. 4879–4881 | «4,5 euro» → «€4,50»; opties «6,5 euro · 22,5 euro · 7,5 euro» → «€6,50 · €22,50 · €7,50»; «diezelfde» → «die»; fout-hint 'vermenigvuldigd' → 'keer 5' |
| 015 | verplaatsen | G8-GET-V02 | gemiddelde: 1S r. 5246 | — |
| 016 | aanpassen | G8-GET-V02 | modus (VO 11A r. 860; spine r. 227) → gemiddelde, zoals G7 | 'Welk cijfer komt het vaakst voor?' → 'Wat is het gemiddelde cijfer?'; opties 7 · 140 · 21 |
| 017 | verplaatsen | G8-GET-V02 | gemiddelde: 1S r. 5246 | — |
| 018 | verplaatsen | G7-DENK-02 | twee tafelsommen in een verhaal, zoals regel G8-T1-door-elkaar | — |
| 019 | verplaatsen | G7-DENK-03 | meerstapssom (km → m, delen, plus 1) | — |
| 020 | houden | G8-VBN-E04 | kritisch over een conclusie: eind G8 r. 5076–5077 | — |
| 021 | houden | G8-VBN-E04 | kritisch over gegevens: eind G8 r. 5076–5077 | — |
| 022 | verplaatsen | G8-VERH-E04 | 60 procent van 150: eind G8 r. 4893–4894 | — |
| 023 | aanpassen | G8-VBN-E01 | verschil grootste en kleinste: eind G8 r. 5064 | opsomming met komma's → met ' · ' |

**Nieuwe teksten (letterlijk):**
- 002: «Een cirkeldiagram over sport in de klas is voor de helft blauw, voor een kwart rood en voor een kwart geel. Er zitten 24 kinderen in de klas. Hoeveel kinderen horen bij het blauwe deel?» → «In een cirkeldiagram staat welke sport de kinderen van een klas het liefst doen. De helft kiest voetbal, een kwart kiest hockey en een kwart kiest tennis. Er zitten 24 kinderen in de klas. Hoeveel kinderen kiezen voetbal?»
- 005: «Een lijngrafiek laat de temperatuur zien. Om 8 uur is het 12 graden, om 12 uur 18 graden en om 16 uur 15 graden. Wat gebeurt er tussen 12 uur en 16 uur?» → «In de lijngrafiek zie je de temperatuur op een dag, van 8.00 uur tot 16.00 uur. Wat gebeurt er met de temperatuur tussen 12.00 uur en 16.00 uur?»
- 011: «In een sportzaal staan 7 dozen met elk 24 ballen. De kind haalt er 18 ballen uit. Hoeveel ballen blijven er over?» → «In een sportzaal staan 7 dozen met elk 24 ballen. Noor haalt er 18 ballen uit. Hoeveel ballen blijven er over?»
- 014: «In een winkel kosten 3 pakken sap samen 4,5 euro. Hoeveel kosten 5 van diezelfde pakken sap?» → «In een winkel kosten 3 pakken sap samen €4,50. Hoeveel kosten 5 van die pakken sap?» · opties €6,50 · €22,50 · €7,50, antwoord €7,50
- 016: «In groep 8 hebben 20 kinderen een cijfer voor een toets. Tien kinderen hebben een 7, vijf kinderen een 8 en vijf kinderen een 6. Welk cijfer komt het vaakst voor?» → «In groep 8 hebben 20 kinderen een cijfer voor een toets. Tien kinderen hebben een 7, vijf kinderen een 8 en vijf kinderen een 6. Wat is het gemiddelde cijfer?» · opties 7 · 140 · 21, antwoord 7
- 023: «Vijf kinderen sprongen ver. 2,1 m, 2,4 m, 2 m, 2,3 m en 2,2 m. Wat is het verschil tussen de verste en de kortste sprong?» → «Vijf kinderen sprongen ver. Dit zijn hun sprongen: 2,1 m · 2,4 m · 2 m · 2,3 m · 2,2 m. Wat is het verschil tussen de verste en de kortste sprong?»
- 003: fout-hint bij 1,6 knikkers «Bij een gemiddelde reken je terug door te vermenigvuldigen, niet door te delen.» → «Bij een gemiddelde reken je terug met keer, niet met delen.» ('vermenigvuldigen' staat op de lijst moeilijke woorden van check_hints; daarom is 003 nu `aanpassen`, in het concept was het `verplaatsen`).

**Bronnen per groep:** gemiddelde → G8-GET-V02 (1S r. 5246; eind G7 r. 4398; De wereld in getallen groep 8 blok 7). Kritisch over data → G8-VBN-E04 (eind G8 r. 5076–5077). Trend en vergelijken → G8-VBN-E01 (r. 5064–5066). Procent → G8-VERH-V01/E04/E05 (r. 4495/4499, 4893–4894, 4899–4902). Verhouding → G8-VERH-E02 (r. 4879–4881). Modus → gemiddelde (VO 11A r. 860; spine r. 227; G7 MEDIAAN-NAAR-GEMIDDELDE). 012 schrappen: geen diagram, alleen het grootste van drie getallen kiezen (groep 3/4-niveau; G7-precedent kans-023).

---

## 8. `kans` — 1 item · voorstel G8-VBN-E04

**Besluit:** **aanpassen — 1 item** (009) en naar **G8-VERH-E01**. Niet buitenBasisschool.

**Reden:** kans is VO-stof (kerndoelen r. 375–379, 393–394; VO 11B r. 882–884; spine r. 223), en Dave haalde 'kans' bij G7 uit de banken (16:59, punt 3). Met een gegeven totaal (10 knikkers) is de rekenkern 'deel van een totaal': SLO eind G8 r. 4868–4869 'kan een telling verwoorden en noteren als verhouding (bv.: Bij zes van de vierentwintig … 1 op de 4, of 1/4 deel, of 25%)'. Zelfde regel als G7 KANS-NAAR-DEEL.

**Nieuw:** «In een bak zitten 6 rode, 3 blauwe en 1 groene knikker. Je pakt zonder kijken één knikker. Op welke kleur heb je de meeste kans?» → «In een bak zitten 6 rode, 3 blauwe en 1 groene knikker. Welk deel van de knikkers is rood?» · opties 6 op de 10 · 6 op de 4 · 3 op de 10 · antwoord 6 op de 10 · geldig ['6 op de 10'] (bij een open vorm ook 3 op de 5, 6/10, 3/5, 60%) · fout-hints: 6 op de 4 → 'Je zette 6 tegenover de andere knikkers. Tel alle knikkers in de bak, dus ook de 6.'; 3 op de 10 → 'Kijk nog eens welke knikkers de vraag bedoelt. Hoeveel zijn het er?' (geen kleurwoord in de hints). Het woord 'kans' staat nergens meer in het item (ENG-check).

**Voorwaarde:** komt er een plaatje, dan knikkers met een letter (R, B, G) of patroon, niet alleen kleur.

---

## Steekproef: 110 items terug naar G7 en 1 buiten de basisschool

Alle 111 antwoorden nagerekend: goed. Oordeel per regel:

- **G8-M24-samengesteld → G7-MEET-02 (15): eens.** Oppervlakte van samengestelde rechthoekige figuren is eind G7 (r. 4552 'oppervlakte van driehoeken en rechthoekige veelhoeken', voorbeeld L-vormige woonkamer). Wel: 'een hok van 84 m²' is vreemd → tuin of terras; en een L-vorm-plaatje met de maten is nodig.
- **G8-T7-prijs-per-stuk → G7-GET-04 (31): niveau eens, contexten niet.** Poesjes, tanden, blaadjes en noten kopen voor €8,50 per stuk, een ei van €8,80, veren: vreemd. Ze staan al in `g7/data/aanvulling_uit_g8.json`; daar moet de context nog gerepareerd worden (bv. schriften, pennen, kaartjes voor het zwembad).
- **G8-T1-door-elkaar → G7-DENK-02 (32): deels oneens.** Het zijn sommen in één stap tot 1000 (bv. '6 poezen hebben elk 38 balletjes', 6 × 38 = 228): dat is G5-niveau (keer onder 1000), geen G7. Voorstel: naar G5 (bv. G5-GET-E07-oefenstof of het G5-doel voor keersommen in context) of in G7 alleen als onderhoud. Ook vreemde contexten: dino's met botten en tanden, 'nest met 804 blaadjes', 'truien in de kantine'.
- **G8-T8-meerstaps → G7-DENK-03 (32): deels oneens.** De stappen zijn goed G7-DENK-03, maar de getallen zijn G5-niveau. Dieren die dingen kopen (dino, konijn, pinguïn, poes, eekhoorn) zijn een vreemde context, en 'hij' voor 'een kind' kan beter met een naam. De antwoorden missen '€' ('44' in plaats van '€44'), anders dan bij T7: gelijk trekken.
- **buiten-basisschool 001 (mediaan van 6 getallen, 7,5): eens.** Het is de mediaan (VO 11A r. 860; spine r. 227). Herschrijven als gemiddelde gaat niet mooi: 4 + 6 + 7 + 8 + 9 + 10 = 44, en 44 : 6 is geen heel getal. Tekstfout voor de log: 'Wat is het middelste getal, dus het middelste getal?'.

---

## Samenvatting

| categorie | items | houden | verplaatst | aangepast | geschrapt | buitenBasisschool | waarvan naar ander doel | waarvan naar andere groep |
|---|---|---|---|---|---|---|---|---|
| bouwsel-tellen | 551 | 0 | 0 | 551 | 0 | 0 | 551 | 400 |
| negatief-zonder-context | 217 | 0 | 0 | 217 | 0 | 0 | 0 | 0 |
| schatten-zonder-afspraak | 180 | 0 | 0 | 180 | 0 | 0 | 71 | 71 |
| vakcode-plattegrond | 131 | 0 | 0 | 131 | 0 | 0 | 131 | 131 |
| kan-kloppen-zonder-opties | 96 | 0 | 0 | 96 | 0 | 0 | 69 | 69 |
| geheugenomvang | 28 | 0 | 0 | 28 | 0 | 0 | 0 | 0 |
| statistiek-gemengd | 22 | 3 | 11 | 7 | 1 | 0 | 18 | 4 |
| kans | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| **totaal** | **1226** | **3** | **11** | **1211** | **1** | **0** | **841** | **675** |

Naar andere groep: G4 36 · G5 105 · G6 531 · G7 3 (G4-GET-E05 36; G5-GET-E05 66; G5-GET-E07 39; G6-MKU-E03 400; G6-MKU-E01 131; G7-DENK-02 1; G7-DENK-03 2). In G8 blijven 550 items.

**Wijzigingen ten opzichte van het eerste concept (vóór de herstart van de box):** (1) labels volgens het G7-precedent: een verplaatst item met nieuwe tekst is `aanpassen` met de vlag `verplaatst` (verplaatst van 113 naar 11); (2) de G5-grens voor plus en min is nu 'getallen en uitkomst tot 1000' (er gaan meer items naar G5-GET-E05: schatten 18 → 41, kan-kloppen 8 → 24; in G8 blijven schatten 109 in plaats van 132 en kan-kloppen 27 in plaats van 43); (3) 003 aanpassen (moeilijk woord in een fout-hint); (4) kan-kloppen: bij een afleider die net buiten de grens ligt (bv. 84 bij 39 + 35) een grens-hint in plaats van 'Ligt 84 daar dichtbij?', want 84 ligt wél dicht bij 80; (5) schatten: een eigen fout-hint voor afronden op de verkeerde plek; (6) geheugen 014 kreeg 100 MB en 16 GB; (7) vakcode-hints zonder losse letters; (8) kans-hints zonder kleurwoord; (9) antwoorden Overzicht 20:39 verwerkt (doelId, aanvulling, hintStatus, tekeneis, badge).

**Bijvangst (geen twijfelitem):** het gemapte G8-GET-E02-001 «4 dozen met elk 198 vissen. Schat …» heeft getallen en uitkomst onder 1000 (4 × 198 = 792): volgens dezelfde grens G5-niveau (G5-GET-E07). 002–004 zitten boven 1000 en blijven G8. De context 'tanden' (002) is vreemd.

## Controle

```
sleutel-hint: {'nagerekend': 2418}
items 1226 · uniek 1226 · zelfde set als twijfel.json: True · besluiten {'aanpassen': 1211, 'verplaatsen': 11, 'houden': 3, 'schrappen': 1} · som 1226
gecheckt: 1225 items (zonder de geschrapte), velden opgave/opties/antwoord/fout-hints/Hint 1/Hint 2
FAIL: geen
WARN: LEGE-HINT 42
INFO: KLEURWOORD 1
  INFO KLEURWOORD: G8-VBN-E04-claude-bank-twijfel-009 [opgave] 'rode'
RESULTAAT: ALLES OK
```

Gecheckt over alle kindteksten van elk item zoals het na het besluit wordt (opgave, opties, antwoord, fout-hints, Hint 1, Hint 2): de R-lijst van `check_merge_notatie.py` (DP, MIN, NEG, XSTER, DEELT, MACHT, SOM, KETEN, PUNT, GELD, EEN, KOMMA4, LITER), ENG ('trainer', 'shirt', 'kans', 'mediaan'), `check_hints.regel_checks` (optieletter, Engels, moeilijke woorden, ':' + getal, notatie), de taalregels, 'te veel/te weinig' in de goede richting, antwoord in een hint, `referentiematen_check` en daarnaast alle checkPatronen en checkPatronenZacht van `referentiematen.json` met de vlaggen iu, `machten_check` per bestemmingsgroep (G8: ² en ³ mogen), `verklapper_check`, `antwoordvormen_check` (geldige antwoorden passen bij het antwoord), antwoord in de opties, elke sleutel in de opties, en per hintsoort nagerekend of de sleutel bij de hint past (2418 sleutels). WARN LEGE-HINT: de 21 statistiek-items hebben geen eigen Hint 1/Hint 2; die komen van het somtype in het bestemmingsdoel. INFO: 'rode' in de opgave van 009 is een woord in de tekst, geen kleur als enig kenmerk.

## Open vragen voor Overzicht

1. **HOOFDREKENGRENS:** is de knip 'getallen en uitkomst tot 100 → G4, tot 1000 → G5, anders G8' goed? Hij stuurt 140 schat- en kan-kloppen-items naar G4/G5 en laat er 136 in G8. Alternatief: alles in G8 houden en alleen de afspraak toevoegen.
2. **012 schrappen** (grootste van drie getallen kiezen, zonder diagram): akkoord, of liever een echt staafdiagram erbij en dan naar G8-VBN-V01?
3. **Contexten in de terug-G7-items:** wie repareert T1, T7 en T8 (dino's, poesjes kopen, veren, '€' ontbreekt bij T8)? T7 staat al in `g7/data/aanvulling_uit_g8.json`.
4. **T1 en T8 zijn G5-niveau:** blijven ze in G7-DENK-02/03 (als onderhoud), of gaan ze naar G5?
5. **Bijvangst G8-GET-E02-001** (gemapt, schatten onder 1000): ook naar G5-GET-E07, of in G8 laten?
