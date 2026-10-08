# G6-GET-M05 — Ronde getallen en deeltafels uit je hoofd

Onze omschrijving: +/− ±10.000 (ronde getallen + analogie); deeltafels uit hoofd · in onze bank: 8 items

Claude-vragen gemapt: **40** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Je kunt kiezen uit [getallen]. Welk aantal [ding] kun je precies verdelen in groepjes van #? Typ dat getal.

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Je kunt kiezen uit [getallen]. Welk aantal [ding] kun je precies verdelen in groepjes van #? Typ dat getal.” (koppeling: claudeId)
- Items: **32** · Claude-doelen: C17 (32) · regel: G6-C05-deelbaar
- Getallenruimte: 0–1.000, 0–100 · type: kale
- Denkfouten (Claude): rest-vergeten (96)
- Verschillende Claude-fout-hints: 92 (meest: “19 : 2 komt niet precies uit: er blijft 1 over. Gebruik de regel: eindigt op 0, 2, 4, 6 of 8.”)
- Voorbeelden:
  - `G6-GET-M05-claude-bank-027` (Claude C17, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je kunt kiezen uit 34, 33, 36 en 27. Welk aantal kaartjes kun je precies verdelen in groepjes van 4? Typ dat getal.
    - **Antwoord:** 36  (controle: ok)
    - **Fout-hints (Claude):** 34 → 34 : 4 komt niet precies uit: er blijft 2 over. Gebruik de regel: de laatste twee cijfers zijn deelbaar door 4. · 27 → 27 : 4 komt niet precies uit: er blijft 3 over. Gebruik de regel: de laatste twee cijfers zijn deelbaar door 4. · 33 → 33 : 4 komt niet precies uit: er blijft 1 over. Gebruik de regel: de laatste twee cijfers zijn deelbaar door 4.
    - **Uitleg (Claude):** Deelbaar door 4: de laatste twee cijfers zijn deelbaar door 4. 36 : 4 = 9, dat klopt precies.
  - `G6-GET-M05-claude-bank-010` (Claude C17, gegenereerd, niveau 1 → basis)
    - **Opgave:** Je kunt kiezen uit 220, 211, 212 en 225. Welk aantal potloden kun je precies verdelen in groepjes van 10? Typ dat getal.
    - **Antwoord:** 220  (controle: ok)
    - **Fout-hints (Claude):** 211 → 211 : 10 komt niet precies uit: er blijft 1 over. Gebruik de regel: eindigt op 0. · 212 → 212 : 10 komt niet precies uit: er blijft 2 over. Gebruik de regel: eindigt op 0. · 225 → 225 : 10 komt niet precies uit: er blijft 5 over. Gebruik de regel: eindigt op 0.
    - **Uitleg (Claude):** Deelbaar door 10: eindigt op 0. 220 : 10 = 22, dat klopt precies.

- **Hint 1 (te schrijven):** Je zoekt het getal dat je precies kunt verdelen in groepjes van dat aantal, zonder dat er iets overblijft.
- **Hint 2 (te schrijven):** Bij groepjes van twee, vijf of tien kun je naar het laatste cijfer kijken. Bij twee: is het laatste cijfer even? Bij vijf: is het een nul of een vijf? Bij tien: is het een nul? Bij andere groepjes reken je het na met de tafel. Is het getal te groot voor de tafel? Haal er dan steeds tien groepjes af. Staat het getal dat je dan hebt in de tafel? Dan kun je het precies verdelen.
- **Ouderzin:** Je kind zoekt welk getal precies deelbaar is door een getal, zonder dat er iets overblijft.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `blijft iets over` (Claudes sleutel: rest-vergeten) → Dat getal kun je niet precies verdelen: er blijft iets over. Reken het na en probeer de andere getallen.  [Claude, taalfix]
  - `andere fout` (andere fout) → Typ een van de getallen uit de vraag: het getal dat je precies kunt verdelen in groepjes, zonder dat er iets overblijft.  [nieuw]
- Status: hints klaar

## Somtype 2: Van # [ding] worden er # verkocht. Hoeveel blijven er over? Reken uit het hoofd.

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Van # [ding] worden er # verkocht. Hoeveel blijven er over? Reken uit het hoofd.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: T10 (4) · regel: G6-T01-hoofd
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): tiental-ernaast (4), verkeerde-bewerking (4), nul-fout-tientallen (4)
- Verschillende Claude-fout-hints: 3 (meest: “Tel in honderdtallen: hoeveel honderdtallen blijven er over?”)
- Voorbeelden:
  - `G6-GET-M05-claude-bank-036` (Claude T10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Van 5000 flessen water worden er 900 verkocht. Hoeveel blijven er over? Reken uit het hoofd.
    - **Antwoord:** 4100  (controle: ok)
    - **Fout-hints (Claude):** 4000 → Tel in honderdtallen: hoeveel honderdtallen blijven er over? · 5900 → Verkocht betekent weg: aftrekken. · 410 → Let op de nullen. Een duizendtal is tien honderdtallen.
    - **Uitleg (Claude):** Denk in honderdtallen: 50 − 9 = 41 honderdtallen. Dus 4100.
  - `G6-GET-M05-claude-bank-033` (Claude T10, gegenereerd, niveau 1 → basis)
    - **Opgave:** Van 4000 kranten worden er 400 verkocht. Hoeveel blijven er over? Reken uit het hoofd.
    - **Antwoord:** 3600  (controle: ok)
    - **Fout-hints (Claude):** 3500 → Tel in honderdtallen: hoeveel honderdtallen blijven er over? · 4400 → Verkocht betekent weg: aftrekken. · 360 → Let op de nullen. Een duizendtal is tien honderdtallen.
    - **Uitleg (Claude):** Denk in honderdtallen: 40 − 4 = 36 honderdtallen. Dus 3600.

- **Hint 1 (te schrijven):** Er worden er verkocht: dat is een minsom.
- **Hint 2 (te schrijven):** Reken met honderdtallen. Hoeveel honderdtallen zijn het eerst? Hoeveel honderdtallen gaan er af?
- **Ouderzin:** Je kind rekent uit het hoofd een minsom met ronde honderdtallen en duizendtallen.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opgeteld` (fout = getal1 + getal2) → Je hebt de getallen opgeteld. Wat er verkocht wordt, gaat eraf: dat is een minsom.  [nieuw]
  - `nul vergeten` (fout = antwoord : 10) → Dat is tien keer te weinig. Ben je een nul vergeten?  [nieuw]
  - `honderd te weinig` (fout = antwoord − 100) → Dat is honderd te weinig. Tel de honderdtallen nog eens na.  [nieuw]
  - `honderd te veel` (fout = antwoord + 100) → Dat is honderd te veel. Tel de honderdtallen nog eens na.  [nieuw]
  - `andere fout` (andere fout) → Reken met honderdtallen: hoeveel honderdtallen zijn het eerst, en hoeveel gaan er af? Zet daarna de nullen terug.  [nieuw]
- Status: hints klaar

## Somtype 3: [kaartjes op volgorde slepen] Sleep elk getal naar het goede vak: deelbaar door # of niet.

- Sleutel: nrOrigineel **3** · somtypeOrigineel “[kaartjes op volgorde slepen] Sleep elk getal naar het goede vak: deelbaar door # of niet.” (koppeling: claudeId)
- Items: **4** · Claude-doelen: C17 (4) · regel: G6-C05-deelbaar
- Getallenruimte: 0–200 · type: ordenen
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G6-GET-M05-claude-bank-037` (Claude C17, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sleep elk getal naar het goede vak: deelbaar door 9 of niet.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** wel:153,36,90|niet:17,50,58  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Deelbaar door 9 betekent: je kunt het getal precies verdelen in 9 gelijke groepjes, zonder rest.
  - `G6-GET-M05-claude-bank-040` (Claude C17, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Sleep elk getal naar het goede vak: deelbaar door 4 of niet.
    - **UI:** kaartjes op volgorde slepen
    - **Antwoord:** wel:36,72,8|niet:31,70,74  (controle: ok)
    - **Fout-hints (Claude):** —
    - **Uitleg (Claude):** Deelbaar door 4 betekent: je kunt het getal precies verdelen in 4 gelijke groepjes, zonder rest.

- **Hint 1 (te schrijven):** Kun je het getal precies verdelen in groepjes van dat aantal, zonder dat er iets overblijft? Dan is het deelbaar.
- **Hint 2 (te schrijven):** Bij twee, vijf of tien kun je naar het laatste cijfer kijken. Bij andere getallen reken je het na met de tafel. Is het getal te groot voor de tafel? Haal er dan steeds tien groepjes af. Staat het getal dat je dan hebt in de tafel? Dan is het deelbaar.
- **Ouderzin:** Je kind sorteert getallen: deelbaar door een getal of niet.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `deelbaar getal bij niet` (fout = een deelbaar getal bij niet) → Bij niet deelbaar staat een getal dat je wél precies kunt verdelen in groepjes van dat aantal. Welk getal is dat?  [nieuw]
  - `niet-deelbaar getal bij deelbaar` (fout = een niet-deelbaar getal bij deelbaar) → Bij deelbaar staat een getal waarbij er iets overblijft. Welk getal is dat?  [nieuw]
  - `één getal in het verkeerde vak` (fout = één getal in het verkeerde vak) → Eén getal staat in het verkeerde vak. Kijk bij elk getal: kun je het precies in groepjes van dat aantal verdelen, zonder dat er iets overblijft?  [nieuw]
  - `vakken omgewisseld` (fout = vakken omgewisseld) → Je hebt de vakken omgewisseld. Bij deelbaar horen de getallen waarbij niets overblijft.  [nieuw]
  - `andere fout` (andere fout) → Kijk bij elk getal: kun je het precies verdelen in groepjes van dat aantal? Dan hoort het bij deelbaar. Blijft er iets over? Dan niet.  [nieuw]
- Status: hints klaar
