# G4-MKU-E01 — Route op de kaart beschrijven

Onze omschrijving: Route op kaart beschrijven (rechts/vooruit/…) · in onze bank: 8 items

Claude-vragen gemapt: **9** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [plattegrond] Je staat bij de [ding]. Welke route brengt je bij de [ding]?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[plattegrond] Je staat bij de [ding]. Welke route brengt je bij de [ding]?” (koppeling: claudeId)
- Items: **9** · Claude-doelen: K9 (9) · regel: D-routes
- Vakafspraak: letter = rij (A boven), cijfer = kolom (1 links)
- Getallenruimte: n.v.t. · type: meerkeuze
- **Visual: nodig** (9 items): Claude-tekenaar: soort “plattegrond” (parameters in jsRender)
- Denkfouten (Claude): None (18)
- Verschillende Claude-fout-hints: 2 (meest: “Kijk naar de richting: welke kant is rechts op de kaart, en welke kant is boven?”)
- Voorbeelden:
  - `G4-MKU-E01-claude-bank-004` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de tent. Welke route brengt je bij de put?
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "D3", "wat": "tent"}, {"vak": "E5", "wat": "put"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) Eerst 2 hokjes naar rechts, dan 1 hokje naar beneden. · B) Eerst 2 hokjes naar links, dan 1 hokje naar boven. · C) Eerst 1 hokje naar rechts, dan 2 hokjes naar beneden.
    - **Antwoord:** Eerst 2 hokjes naar rechts, dan 1 hokje naar beneden.  (controle: ok)
    - **Fout-hints (Claude):** Eerst 2 hokjes naar links, dan 1 hokje naar boven. → Kijk naar de richting: welke kant is rechts op de kaart, en welke kant is boven? · Eerst 1 hokje naar rechts, dan 2 hokjes naar beneden. → Je hebt de aantallen verwisseld. Tel de hokjes opzij en de hokjes omhoog apart.
  - `G4-MKU-E01-claude-bank-008` (Claude K9, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Je staat bij de boom. Welke route brengt je bij de vijver?
    - **Tekening:** `{"rijen": 5, "soort": "plattegrond", "dingen": [{"vak": "E2", "wat": "boom"}, {"vak": "A1", "wat": "vijver"}], "kolommen": 6, "vakAfspraak": "letter = rij (A boven), cijfer = kolom (1 links)"}`
    - **Opties:** A) Eerst 1 hokje naar rechts, dan 4 hokjes naar beneden. · B) Eerst 4 hokjes naar links, dan 1 hokje naar boven. · C) Eerst 1 hokje naar links, dan 4 hokjes naar boven.
    - **Antwoord:** Eerst 1 hokje naar links, dan 4 hokjes naar boven.  (controle: ok)
    - **Fout-hints (Claude):** Eerst 1 hokje naar rechts, dan 4 hokjes naar beneden. → Kijk naar de richting: welke kant is rechts op de kaart, en welke kant is boven? · Eerst 4 hokjes naar links, dan 1 hokje naar boven. → Je hebt de aantallen verwisseld. Tel de hokjes opzij en de hokjes omhoog apart.

- **Hint 1 (te schrijven):** Zoek waar je staat en waar je heen moet. Moet je naar links of naar rechts? En naar boven of naar beneden?
- **Hint 2 (te schrijven):** Tel de hokjes opzij. Tel daarna de hokjes naar boven of beneden. Welke route past daarbij?
- **Ouderzin:** Je kind kiest de route tussen twee plekken op een plattegrond met hokjes.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `verkeerde richting` (verkeerde richting (tekst per item)) → Kijk naar de richting: welke kant is rechts op de kaart, en welke kant is boven? (tekst per item)  [Claude, ok]
  - `aantallen verwisseld` (andere fout) → Kijk goed hoeveel hokjes je opzij gaat en hoeveel naar boven of beneden. Tel die twee apart.  [nieuw]
- Status: hints klaar
