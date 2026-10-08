# G8-VERH-E05 — Hoeveel procent erbij of eraf?

Onze omschrijving: % toename/afname/winst/verlies (ook >100%, lastige getallen + RM) · in onze bank: 8 items

Claude-vragen gemapt: **54** in **5** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een [ding] kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een [ding] kostte €# en kost nu €#. Met hoeveel procent is de prijs gestegen?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: T5 (16) · regel: G8-T5-procent-erbij
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (45)
- Verschillende Claude-fout-hints: 2 (meest: “Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat?”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-017` (Claude T5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een kaartje kostte €60 en kost nu €72. Met hoeveel procent is de prijs gestegen?
    - **Antwoord:** 20  (controle: ok)
    - **Fout-hints (Claude):** €12 → Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat? · €17 → Reken de stijging uit ten opzichte van de oude prijs, niet de nieuwe.
    - **Uitleg (Claude):** De stijging is 72 − 60 = 12. 12 van 60 is 20%.
  - `G8-VERH-E05-claude-bank-014` (Claude T5, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een spel kostte €80 en kost nu €92. Met hoeveel procent is de prijs gestegen?
    - **Antwoord:** 15  (controle: ok)
    - **Fout-hints (Claude):** €8 → Dat is de stijging in euro's. Hoeveel procent van de oude prijs is dat? · €9 → Reken de stijging uit ten opzichte van de oude prijs, niet de nieuwe.
    - **Uitleg (Claude):** De stijging is 92 − 80 = 12. 12 van 80 is 15%.

- **Hint 1 (te schrijven):** Hoeveel euro komt er bij de prijs? Welk deel van de oude prijs is dat?
- **Hint 2 (te schrijven):** Haal de oude prijs van de nieuwe prijs af: zoveel euro komt erbij. De oude prijs is honderd procent. Hoeveel procent is dan het bedrag dat erbij komt?
- **Ouderzin:** Je kind rekent uit met hoeveel procent een prijs is gestegen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `nog geen procent van de oude prijs` (Claudes sleutel: procent-verkeerde-basis) → Vergelijk met de oude prijs: die is honderd procent. Hoeveel euro komt erbij, en hoeveel procent van de oude prijs is dat?  [Claude, taalfix]
  - `andere fout` (andere fout) → Hoeveel euro komt erbij? De oude prijs is honderd procent: hoeveel procent is dat bedrag?  [nieuw]
- Status: hints klaar

## Somtype 2: Een [ding] kostte €#. De prijs stijgt met #%. Wat kost [ding] nu?

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een [ding] kostte €#. De prijs stijgt met #%. Wat kost het ei nu?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: T5 (16) · regel: G8-T5-procent-erbij
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (16), procent-verkeerde-basis (16), verkeerde-bewerking (15)
- Verschillende Claude-fout-hints: 15 (meest: “Dat is alleen de stijging. Tel hem op bij de oude prijs.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-030` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een rugzak kostte €40. De prijs stijgt met 10%. Wat kost de rugzak nu?
    - **Antwoord:** 44  (controle: ok)
    - **Fout-hints (Claude):** €4 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €36 → De prijs stijgt: erbij, niet eraf. · €50 → 10% is een deel van €40, niet €10.
    - **Uitleg (Claude):** 10% van 40 = 4. Erbij: 40 + 4 = €44.
  - `G8-VERH-E05-claude-bank-022` (Claude T5, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een knuffel kostte €40. De prijs stijgt met 5%. Wat kost de knuffel nu?
    - **Antwoord:** 42  (controle: ok)
    - **Fout-hints (Claude):** €2 → Dat is alleen de stijging. Tel hem op bij de oude prijs. · €38 → De prijs stijgt: erbij, niet eraf. · €45 → 5% is een deel van €40, niet €5.
    - **Uitleg (Claude):** 5% van 40 = 2. Erbij: 40 + 2 = €42.

- **Hint 1 (te schrijven):** De prijs stijgt: er komt een deel van de oude prijs bij. Hoeveel euro is dat procent van de oude prijs?
- **Hint 2 (te schrijven):** Deel de oude prijs door honderd: dat is één procent. Doe dat keer het procent: zoveel komt er bij de prijs. Tel dat op bij de oude prijs.
- **Ouderzin:** Je kind rekent uit wat iets kost als de prijs met een procent stijgt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen wat erbij komt` (Claudes sleutel: andere-deel-genomen) → Dat is alleen wat erbij komt. Gevraagd is wat het nu kost: tel het op bij de oude prijs.  [Claude, taalfix]
  - `eraf` (Claudes sleutel: verkeerde-bewerking) → De prijs stijgt: wat erbij komt, tel je op bij de oude prijs. Haal het er niet af.  [Claude, taalfix]
  - `procent als euro` (Claudes sleutel: procent-verkeerde-basis) → Zo komt het getal van het procent erbij als euro's. Hoeveel euro is dat procent van de oude prijs?  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken uit hoeveel euro het procent van de oude prijs is. Tel dat op bij de oude prijs.  [nieuw]
- Status: hints klaar

## Somtype 3: [wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “[wie] zet €# op een spaarrekening met #% rente per jaar. Hoeveel staat er na één jaar op de rekening?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: T6 (16) · regel: G8-T6-na-een-jaar
- Getallenruimte: procenten met € · type: kale
- Denkfouten (Claude): andere-deel-genomen (16), komma-verschoven (16), verkeerde-bewerking (16)
- Verschillende Claude-fout-hints: 9 (meest: “Dat is alleen de rente. Tel hem op bij het spaargeld.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-003` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Daan zet €1000 op een spaarrekening met 5% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 1050  (controle: ok)
    - **Fout-hints (Claude):** €50 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €1500 → 1% van 1000 is 10. · €950 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 5% van 1000 = €50. Erbij: 1000 + 50 = €1050.
  - `G8-VERH-E05-claude-bank-040` (Claude T6, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sanne zet €200 op een spaarrekening met 3% rente per jaar. Hoeveel staat er na één jaar op de rekening?
    - **Antwoord:** 206  (controle: ok)
    - **Fout-hints (Claude):** €6 → Dat is alleen de rente. Tel hem op bij het spaargeld. · €260 → 1% van 200 is 2. · €194 → Rente komt erbij, niet eraf.
    - **Uitleg (Claude):** Rente: 3% van 200 = €6. Erbij: 200 + 6 = €206.

- **Hint 1 (te schrijven):** Procent betekent: zoveel van de honderd. Hoeveel euro rente komt er in één jaar bij?
- **Hint 2 (te schrijven):** Deel het bedrag door honderd: dat is één procent. Doe dat keer het procent: dat is de rente. Tel de rente op bij het bedrag dat er al op stond.
- **Ouderzin:** Je kind rekent uit hoeveel geld er na een jaar met rente op de rekening staat.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `alleen de rente` (Claudes sleutel: andere-deel-genomen) → Dat is alleen de rente. Gevraagd is wat er na één jaar in totaal op de rekening staat.  [Claude, taalfix]
  - `tien keer te veel rente` (Claudes sleutel: komma-verschoven) → Zo komt er tien keer te veel rente bij. Eén procent is het bedrag gedeeld door honderd. Doe dat keer het procent.  [Claude, taalfix]
  - `rente eraf` (Claudes sleutel: verkeerde-bewerking) → Rente krijg je erbij. Na een jaar staat er dus meer op de rekening dan eerst.  [Claude, taalfix]
  - `andere fout` (andere fout) → Reken eerst de rente uit. Tel die op bij het bedrag dat er al op stond.  [nieuw]
- Status: hints klaar

## Somtype 4: Vorig jaar waren er # [ding], nu #. Met hoeveel procent is dat gestegen?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Vorig jaar waren er # [ding], nu #. Met hoeveel procent is dat gestegen?” (koppeling: claudeId)
- Items: **5** · Claude-doelen: T5 (5) · regel: G8-T5-procent-erbij
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): procent-verkeerde-basis (14)
- Verschillende Claude-fout-hints: 5 (meest: “Vergelijk met het oude aantal (100%), niet met het nieuwe.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-044` (Claude T5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Vorig jaar waren er 20 eieren, nu 30. Met hoeveel procent is dat gestegen?
    - **Antwoord:** 50  (controle: ok)
    - **Fout-hints (Claude):** 10 → 10 is de toename in aantal. De vraag is hoeveel procent dat van 20 is. · 33 → Vergelijk met het oude aantal (100%), niet met het nieuwe.
    - **Uitleg (Claude):** Erbij gekomen: 30 − 20 = 10. Dat vergelijk je met het oude aantal: 10 van 20 is 50%.
  - `G8-VERH-E05-claude-bank-041` (Claude T5, gegenereerd, niveau 3 → toepassen)
    - **Opgave:** Vorig jaar waren er 40 wortels, nu 44. Met hoeveel procent is dat gestegen?
    - **Antwoord:** 10  (controle: ok)
    - **Fout-hints (Claude):** 4 → 4 is de toename in aantal. De vraag is hoeveel procent dat van 40 is. · 9 → Vergelijk met het oude aantal (100%), niet met het nieuwe.
    - **Uitleg (Claude):** Erbij gekomen: 44 − 40 = 4. Dat vergelijk je met het oude aantal: 4 van 40 is 10%.

- **Hint 1 (te schrijven):** Hoeveel zijn er nu meer dan vorig jaar? Welk deel van het oude aantal is dat?
- **Hint 2 (te schrijven):** Haal het oude aantal van het nieuwe aantal af: zoveel zijn er nu meer. Het oude aantal is honderd procent. Hoeveel procent is dan dat verschil?
- **Ouderzin:** Je kind rekent uit met hoeveel procent een aantal is gestegen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verschil` (fout = verschil van de getallen) → Dat is hoeveel er nu meer zijn, nog geen procent. Hoeveel procent van het oude aantal is dat?  [nieuw]
  - `nieuwe aantal als basis` (Claudes sleutel: procent-verkeerde-basis) → Vergelijk met het oude aantal: dat is honderd procent, niet het nieuwe aantal.  [Claude, taalfix]
  - `andere fout` (andere fout) → Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?  [nieuw]
- Status: hints klaar

## Somtype 5: Een winkel verkoopt in de eerste week # [ding] en in de tweede week # [ding]. Met hoeveel procent is de verkoop gedaald?

- Sleutel: nrOrigineel **21** · somtypeOrigineel “Een winkel verkoopt in week # [ding] broden en in week # [ding] broden. Met hoeveel procent is de verkoop gedaald?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: G9 (1) · regel: D8-STAT-NAAR-VERH
- Getallenruimte: 0–1.000 · type: meerkeuze
- Denkfouten (Claude): getal-overgenomen (1), procent-verkeerde-basis (1)
- Verschillende Claude-fout-hints: 2 (meest: “20 is het verschil in broden. Je moet dat verschil nog vergelijken met het beginaantal.”)
- Voorbeelden:
  - `G8-VERH-E05-claude-bank-054` (Claude G9, ai, niveau 3 → toepassen)
    - **Opgave:** Een winkel verkoopt in de eerste week 60 broden en in de tweede week 48 broden. Met hoeveel procent is de verkoop gedaald?
    - **Opties:** A) 12 procent · B) 20 procent · C) 25 procent
    - **Antwoord:** 20 procent  (controle: n.v.t.)
    - **Fout-hints (Claude):** 20 procent → 20 is het verschil in broden. Je moet dat verschil nog vergelijken met het beginaantal. · 40 procent → Je vergelijkt met het nieuwe aantal. Bij een daling reken je met het begingetal.
    - **Uitleg (Claude):** Het verschil is 60 − 48 = 12 broden. Je vergelijkt 12 met het begingetal 60. 12 van de 60 is 20 procent.

- **Hint 1 (te schrijven):** Hoeveel minder is er verkocht? Het aantal van het begin is honderd procent.
- **Hint 2 (te schrijven):** Haal het nieuwe aantal van het oude aantal af: zoveel minder is het. Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?
- **Ouderzin:** Je kind rekent uit met hoeveel procent een aantal is gedaald.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verschil als procent` (12 procent) → Dat is het verschil in aantal, nog geen procent. Hoeveel procent van het oude aantal is dat?  [nieuw]
  - `nieuwe aantal als basis` (25 procent) → Zo vergelijk je met het nieuwe aantal. Bij een daling is het oude aantal honderd procent.  [nieuw]
  - `andere fout` (andere fout) → Het oude aantal is honderd procent. Hoeveel procent is het verschil daarvan?  [nieuw]
- **LET OP kop gewijzigd** (2026-10-08): de hints zijn geschreven voor 'Een winkel verkoopt in week # [ding] broden en in week # [ding] broden. Met hoeveel procent is de verkoop gedaald?'. Nakijken of ze nog passen.
- Status: hints klaar
