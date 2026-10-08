# G3-MKU-E02 — De weg op de plattegrond

Onze omschrijving: Route volgen/beschrijven met plattegrond; werkelijkheid↔kaart · in onze bank: 8 items

Claude-vragen gemapt: **109** in **8** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [plattegrond] Wat staat er in vak [vak]?

- Items: **44** · Claude-doelen: K4 (44) · regel: R23-plattegrond
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (88)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-054` (Claude K4, bank, niveau 3 → toepassen)
    - **Opgave:** Wat staat er in vak C1?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "C1", "wat": "hek"}, {"vak": "D2", "wat": "bal"}, {"vak": "B1", "wat": "boom"}, {"vak": "C2", "wat": "huis"}, {"vak": "B4", "wat": "vijver"}], "kolommen": 4, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) boom · B) hek · C) bal
    - **Antwoord:** hek  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G3-MKU-E02-claude-bank-057` (Claude K4, bank, niveau 3 → toepassen)
    - **Opgave:** Wat staat er in vak A2?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "A2", "wat": "hek"}, {"vak": "C4", "wat": "bal"}, {"vak": "D2", "wat": "boom"}, {"vak": "A1", "wat": "huis"}, {"vak": "B4", "wat": "vijver"}], "kolommen": 5, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) boom · B) huis · C) hek
    - **Antwoord:** hek  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst de letter van het vak. Zoek daarna het cijfer.
- **Hint 2 (te schrijven):** Volg vanaf de letter de hokjes recht door. Volg ook vanaf het cijfer de hokjes recht door. Waar die twee elkaar raken, is het vak. Kijk wat daar staat.
- **Ouderzin:** Je kind leest af wat er in een vak van een plattegrond staat (letter en cijfer).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfer fout` (goede letter, ander cijfer) → De letter klopt, maar het cijfer niet. Kijk nog eens naar het cijfer.  [nieuw]
  - `letter fout` (goed cijfer, andere letter) → Het cijfer klopt, maar de letter niet. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid (bijvoorbeeld het vak van de tweede letter met het cijfer van de eerste letter)) → Je hebt de letter en het cijfer omgedraaid. Zoek eerst de letter, dan het cijfer.  [nieuw]
  - `overig` (ander vak) → Dat is een ander vak. Zoek eerst de letter en daarna het cijfer.  [nieuw]
- Status: hints klaar

## Somtype 2: [plattegrond] In welk vak staat de/het [ding]?

- Items: **26** · Claude-doelen: K4 (26) · regel: R23-plattegrond
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): grafiek-verkeerd-afgelezen (52)
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-026` (Claude K4, bank, niveau 3 → toepassen)
    - **Opgave:** In welk vak staat het huis?
    - **Tekening:** `{"rijen": 4, "soort": "plattegrond", "dingen": [{"vak": "B1", "wat": "huis"}, {"vak": "D3", "wat": "vijver"}, {"vak": "C1", "wat": "put"}, {"vak": "B2", "wat": "vlag"}, {"vak": "C2", "wat": "bank"}], "kolommen": 4, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) D3 · B) B2 · C) B1
    - **Antwoord:** B1  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G3-MKU-E02-claude-bank-002` (Claude K4, bank, niveau 3 → toepassen)
    - **Opgave:** In welk vak staat de tent?
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "B2", "wat": "tent"}, {"vak": "D4", "wat": "school"}, {"vak": "D2", "wat": "hek"}, {"vak": "B1", "wat": "bal"}, {"vak": "B3", "wat": "boom"}], "kolommen": 5, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) D2 · B) B1 · C) B2
    - **Antwoord:** B2  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst het ding op de plattegrond.
- **Hint 2 (te schrijven):** Ga vanaf het ding recht naar de rand met de letters. Ga daarna recht naar de rand met de cijfers. Eerst de letter, dan het cijfer.
- **Ouderzin:** Je kind zoekt in welk vak van een plattegrond iets staat (letter en cijfer).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfer fout` (goede letter, ander cijfer) → De letter klopt, maar het cijfer niet. Kijk nog eens naar het cijfer.  [nieuw]
  - `letter fout` (goed cijfer, andere letter) → Het cijfer klopt, maar de letter niet. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid (bijvoorbeeld het vak van de tweede letter met het cijfer van de eerste letter)) → Je hebt de letter en het cijfer omgedraaid. Zoek eerst de letter, dan het cijfer.  [nieuw]
  - `overig` (ander vak) → Dat is een ander vak. Zoek eerst de letter en daarna het cijfer.  [nieuw]
- Status: hints klaar

## Somtype 3: [plattegrond] Tik op vak [vak] van de plattegrond.

- Items: **12** · Claude-doelen: K4 (12) · regel: R23-plattegrond
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): —
- Claude-fout-hints: geen
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-072` (Claude K4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tik op vak A2 van de plattegrond.
    - **Tekening:** `{"soort": "plattegrond", "rijen": 4, "kolommen": 5, "dingen": [], "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)", "rasterAangenomen": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** A2  (controle: ok)
    - **Fout-hints (Claude):** —
  - `G3-MKU-E02-claude-bank-082` (Claude K4, gegenereerd, niveau 1 → basis)
    - **Opgave:** Tik op vak A1 van de plattegrond.
    - **Tekening:** `{"soort": "plattegrond", "rijen": 4, "kolommen": 5, "dingen": [], "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)", "rasterAangenomen": true}`
    - **UI:** vak(ken) aantikken op rooster
    - **Antwoord:** A1  (controle: ok)
    - **Fout-hints (Claude):** —

- **Hint 1 (te schrijven):** Zoek eerst de letter. Zoek daarna het cijfer.
- **Hint 2 (te schrijven):** Volg vanaf de letter de hokjes recht door. Volg ook vanaf het cijfer de hokjes recht door. Tik op het vak waar die twee elkaar raken.
- **Ouderzin:** Je kind tikt het goede vak aan op een plattegrond (letter en cijfer).
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `cijfer fout` (goede letter, ander cijfer) → De letter klopt, maar het cijfer niet. Kijk nog eens naar het cijfer.  [nieuw]
  - `letter fout` (goed cijfer, andere letter) → Het cijfer klopt, maar de letter niet. Kijk nog eens naar de letter.  [nieuw]
  - `omgedraaid` (letter en cijfer omgedraaid (bijvoorbeeld het vak van de tweede letter met het cijfer van de eerste letter)) → Je hebt de letter en het cijfer omgedraaid. Zoek eerst de letter, dan het cijfer.  [nieuw]
  - `overig` (ander vak) → Dat is een ander vak. Zoek eerst de letter en daarna het cijfer.  [nieuw]
- Status: hints klaar

## Somtype 4: [plattegrond] Je staat bij de [ding]. Loop # hokjes naar [richting]. Loop dan # hokje naar [richting]. Waar kom je? Tik op het vak.

- Items: **9** · Claude-doelen: K9 (9) · regel: D-routes (R22-route)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (15)
- Verschillende Claude-fout-hints: 3 (meest: “Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag.”)
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-091` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de school. Loop 2 hokjes naar rechts. Loop dan 1 hokje naar beneden. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "D3", "wat": "school"}, {"vak": "E5", "wat": "bank"}, {"vak": "D5", "wat": "vijver", "afleider": true}, {"vak": "C5", "wat": "put", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** E5  (controle: ok)
    - **Fout-hints (Claude):** D5 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · E3 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.
  - `G3-MKU-E02-claude-bank-094` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de tent. Loop 2 hokjes naar links. Loop dan 1 hokje naar beneden. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "A4", "wat": "tent"}, {"vak": "B2", "wat": "vijver"}, {"vak": "A2", "wat": "bank", "afleider": true}, {"vak": "B6", "wat": "put", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** B2  (controle: ok)
    - **Fout-hints (Claude):** A2 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · B4 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.

- **Hint 1 (te schrijven):** Zet je vinger op de plek waar je staat. Loop de eerste stap, hokje voor hokje.
- **Hint 2 (te schrijven):** Loop daarna de tweede stap. Tel de hokjes hardop. Tik op het vak waar je uitkomt.
- **Ouderzin:** Je kind volgt een route van twee stappen op een plattegrond en tikt aan waar het uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opzij geteld fout` (goede letter, ander cijfer) → Naar boven of naar beneden klopt. Heb je de stap opzij ook gedaan, en de goede kant op? Tel de hokjes naar links of naar rechts nog eens.  [nieuw]
  - `boven of beneden fout` (goed cijfer, andere letter) → Opzij klopt. Heb je de stap naar boven of naar beneden ook gedaan, en de goede kant op? Tel die hokjes nog eens.  [nieuw]
  - `ander vak` (ander vak) → Begin opnieuw bij de plek waar je staat. Loop eerst de ene stap en dan de andere, hokje voor hokje.  [nieuw]
- Status: hints klaar

## Somtype 5: [plattegrond] Je staat bij de [ding]. Loop # hokjes naar [richting]. Loop dan # hokjes naar [richting]. Waar kom je? Tik op het vak.

- Items: **9** · Claude-doelen: K9 (9) · regel: D-routes (R22-route)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (13)
- Verschillende Claude-fout-hints: 3 (meest: “Je hebt alleen de stap opzij gedaan. Daarna ga je nog omhoog of omlaag.”)
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-103` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vijver. Loop 2 hokjes naar links. Loop dan 3 hokjes naar boven. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "D3", "wat": "vijver"}, {"vak": "A1", "wat": "bal"}, {"vak": "D1", "wat": "fiets", "afleider": true}, {"vak": "A5", "wat": "schommel", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** A1  (controle: ok)
    - **Fout-hints (Claude):** D1 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · A3 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.
  - `G3-MKU-E02-claude-bank-104` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vlag. Loop 2 hokjes naar links. Loop dan 2 hokjes naar boven. Waar kom je? Tik op het vak.
    - **Tekening:** `{"soort": "plattegrond", "rijen": 5, "kolommen": 6, "dingen": [{"vak": "E6", "wat": "vlag"}, {"vak": "E4", "wat": "schommel", "afleider": true}, {"vak": "C6", "wat": "zandbak", "afleider": true}, {"vak": "B4", "wat": "boom", "afleider": true}], "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)", "rasterAangenomen": true}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** C4  (controle: ok)
    - **Fout-hints (Claude):** E4 → Je hebt alleen de stap opzij gedaan. Daarna ga je nog omhoog of omlaag.

- **Hint 1 (te schrijven):** Zet je vinger op de plek waar je staat. Loop de eerste stap, hokje voor hokje.
- **Hint 2 (te schrijven):** Loop daarna de tweede stap. Tel de hokjes hardop. Tik op het vak waar je uitkomt.
- **Ouderzin:** Je kind volgt een route van twee stappen op een plattegrond en tikt aan waar het uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opzij geteld fout` (goede letter, ander cijfer) → Naar boven of naar beneden klopt. Heb je de stap opzij ook gedaan, en de goede kant op? Tel de hokjes naar links of naar rechts nog eens.  [nieuw]
  - `boven of beneden fout` (goed cijfer, andere letter) → Opzij klopt. Heb je de stap naar boven of naar beneden ook gedaan, en de goede kant op? Tel die hokjes nog eens.  [nieuw]
  - `ander vak` (ander vak) → Begin opnieuw bij de plek waar je staat. Loop eerst de ene stap en dan de andere, hokje voor hokje.  [nieuw]
- Status: hints klaar

## Somtype 6: [plattegrond] Je staat bij de [ding]. Loop # hokje naar [richting]. Loop dan # hokjes naar [richting]. Waar kom je? Tik op het vak.

- Items: **4** · Claude-doelen: K9 (4) · regel: D-routes (R22-route)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (6)
- Verschillende Claude-fout-hints: 3 (meest: “Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag.”)
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-089` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de put. Loop 1 hokje naar links. Loop dan 4 hokjes naar boven. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "E3", "wat": "put"}, {"vak": "A2", "wat": "boom"}, {"vak": "E2", "wat": "tent", "afleider": true}, {"vak": "A4", "wat": "vijver", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** A2  (controle: ok)
    - **Fout-hints (Claude):** E2 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · A3 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.
  - `G3-MKU-E02-claude-bank-088` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vlag. Loop 1 hokje naar rechts. Loop dan 3 hokjes naar beneden. Waar kom je? Tik op het vak.
    - **Tekening:** `{"soort": "plattegrond", "rijen": 5, "kolommen": 6, "dingen": [{"vak": "A3", "wat": "vlag"}, {"vak": "A4", "wat": "bank", "afleider": true}, {"vak": "D2", "wat": "put", "afleider": true}, {"vak": "D3", "wat": "bal", "afleider": true}], "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)", "rasterAangenomen": true}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** D4  (controle: ok)
    - **Fout-hints (Claude):** A4 → Je hebt alleen de stap opzij gedaan. Daarna ga je nog omhoog of omlaag.

- **Hint 1 (te schrijven):** Zet je vinger op de plek waar je staat. Loop de eerste stap, hokje voor hokje.
- **Hint 2 (te schrijven):** Loop daarna de tweede stap. Tel de hokjes hardop. Tik op het vak waar je uitkomt.
- **Ouderzin:** Je kind volgt een route van twee stappen op een plattegrond en tikt aan waar het uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opzij geteld fout` (goede letter, ander cijfer) → Naar boven of naar beneden klopt. Heb je de stap opzij ook gedaan, en de goede kant op? Tel de hokjes naar links of naar rechts nog eens.  [nieuw]
  - `boven of beneden fout` (goed cijfer, andere letter) → Opzij klopt. Heb je de stap naar boven of naar beneden ook gedaan, en de goede kant op? Tel die hokjes nog eens.  [nieuw]
  - `ander vak` (ander vak) → Begin opnieuw bij de plek waar je staat. Loop eerst de ene stap en dan de andere, hokje voor hokje.  [nieuw]
- Status: hints klaar

## Somtype 7: [plattegrond] Je staat bij de [ding]. Loop # hokje naar [richting]. Loop dan # hokje naar [richting]. Waar kom je? Tik op het vak.

- Items: **3** · Claude-doelen: K9 (3) · regel: D-routes (R22-route)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (4)
- Verschillende Claude-fout-hints: 3 (meest: “Je hebt alleen de stap opzij gedaan. Daarna ga je nog omhoog of omlaag.”)
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-083` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de school. Loop 1 hokje naar links. Loop dan 1 hokje naar boven. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "B4", "wat": "school"}, {"vak": "A3", "wat": "boom"}, {"vak": "B3", "wat": "vijver", "afleider": true}, {"vak": "C3", "wat": "bank", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** A3  (controle: ok)
    - **Fout-hints (Claude):** B3 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · A4 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.
  - `G3-MKU-E02-claude-bank-085` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de vlag. Loop 1 hokje naar rechts. Loop dan 1 hokje naar boven. Waar kom je? Tik op het vak.
    - **Tekening:** `{"soort": "plattegrond", "rijen": 5, "kolommen": 6, "dingen": [{"vak": "D5", "wat": "vlag"}, {"vak": "D6", "wat": "boom", "afleider": true}, {"vak": "E6", "wat": "huis", "afleider": true}, {"vak": "C4", "wat": "school", "afleider": true}], "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)", "rasterAangenomen": true}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** C6  (controle: ok)
    - **Fout-hints (Claude):** D6 → Je hebt alleen de stap opzij gedaan. Daarna ga je nog omhoog of omlaag.

- **Hint 1 (te schrijven):** Zet je vinger op de plek waar je staat. Loop de eerste stap, hokje voor hokje.
- **Hint 2 (te schrijven):** Loop daarna de tweede stap. Tel de hokjes hardop. Tik op het vak waar je uitkomt.
- **Ouderzin:** Je kind volgt een route van twee stappen op een plattegrond en tikt aan waar het uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opzij geteld fout` (goede letter, ander cijfer) → Naar boven of naar beneden klopt. Heb je de stap opzij ook gedaan, en de goede kant op? Tel de hokjes naar links of naar rechts nog eens.  [nieuw]
  - `boven of beneden fout` (goed cijfer, andere letter) → Opzij klopt. Heb je de stap naar boven of naar beneden ook gedaan, en de goede kant op? Tel die hokjes nog eens.  [nieuw]
  - `ander vak` (ander vak) → Begin opnieuw bij de plek waar je staat. Loop eerst de ene stap en dan de andere, hokje voor hokje.  [nieuw]
- Status: hints klaar

## Somtype 8: [plattegrond] Je staat bij het [ding]. Loop # hokjes naar [richting]. Loop dan # hokjes naar [richting]. Waar kom je? Tik op het vak.

- Items: **2** · Claude-doelen: K9 (2) · regel: D-routes (R22-route)
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): deel-vergeten-bij-splitsen (4)
- Verschillende Claude-fout-hints: 2 (meest: “Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag.”)
- Voorbeelden:
  - `G3-MKU-E02-claude-bank-109` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij het huis. Loop 2 hokjes naar rechts. Loop dan 2 hokjes naar beneden. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "A2", "wat": "huis"}, {"vak": "C4", "wat": "bank"}, {"vak": "A4", "wat": "put", "afleider": true}, {"vak": "C2", "wat": "bal", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** C4  (controle: ok)
    - **Fout-hints (Claude):** A4 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · C2 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.
  - `G3-MKU-E02-claude-bank-108` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij het huis. Loop 3 hokjes naar links. Loop dan 3 hokjes naar beneden. Waar kom je? Tik op het vak.
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "B6", "wat": "huis"}, {"vak": "E3", "wat": "tent"}, {"vak": "B3", "wat": "put", "afleider": true}, {"vak": "E6", "wat": "bal", "afleider": true}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **UI:** vak aantikken (geen code kiezen)
    - **Antwoord:** E3  (controle: ok)
    - **Fout-hints (Claude):** B3 → Je hebt alleen de eerste stap gedaan. Ga daarna nog omhoog of omlaag. · E6 → Je hebt alleen omhoog of omlaag gelopen. Vergeet de stap opzij niet.

- **Hint 1 (te schrijven):** Zet je vinger op de plek waar je staat. Loop de eerste stap, hokje voor hokje.
- **Hint 2 (te schrijven):** Loop daarna de tweede stap. Tel de hokjes hardop. Tik op het vak waar je uitkomt.
- **Ouderzin:** Je kind volgt een route van twee stappen op een plattegrond en tikt aan waar het uitkomt.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `opzij geteld fout` (goede letter, ander cijfer) → Naar boven of naar beneden klopt. Heb je de stap opzij ook gedaan, en de goede kant op? Tel de hokjes naar links of naar rechts nog eens.  [nieuw]
  - `boven of beneden fout` (goed cijfer, andere letter) → Opzij klopt. Heb je de stap naar boven of naar beneden ook gedaan, en de goede kant op? Tel die hokjes nog eens.  [nieuw]
  - `ander vak` (ander vak) → Begin opnieuw bij de plek waar je staat. Loop eerst de ene stap en dan de andere, hokje voor hokje.  [nieuw]
- Status: hints klaar
