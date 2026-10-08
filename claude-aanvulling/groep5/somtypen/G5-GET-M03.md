# G5-GET-M03 — Euro's met komma lezen

Onze omschrijving: Geld-decimalen: komma lezen/schrijven/vergelijken (€) · in onze bank: 8 items

Claude-vragen gemapt: **28** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [geld] Hoeveel [ding] zie je?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[geld] Hoeveel [ding] zie je?” (koppeling: claudeId)
- Items: **28** · Claude-doelen: M5 (28) · regel: D-CENT-1TOT2
- Getallenruimte: 0–2 euro (met komma) · type: meerkeuze
- Didactiek-besluit (G4-twijfel, 1 okt): 1–2 euro → “1 euro en N cent” — zie g4/besluiten_twijfel.md + besluit Dave
- Denkfouten (Claude): geld-verkeerd-geteld (31), getal-overgenomen (13), kommagetal-als-geheel (12)
- Verschillende Claude-fout-hints: 2 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op.”)
- Voorbeelden:
  - `G5-GET-M03-claude-bank-024` (Claude M5, bank, niveau 2 → basis)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [100, 5, 5]}`
    - **Opties:** A) €1 · B) €1,10 · C) €1,05
    - **Antwoord:** €1,10  (controle: ok)
    - **Fout-hints (Claude):** €1 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. · €1,05 → Leg de munten op volgorde van groot naar klein en tel ze één voor één op.
  - `G5-GET-M03-claude-bank-027` (Claude M5, bank, niveau 2 → basis)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [100, 20, 10, 5]}`
    - **Opties:** A) €36 · B) €4 · C) €1,35
    - **Antwoord:** €1,35  (controle: ok)
    - **Fout-hints (Claude):** €36 → Kijk goed naar elke munt. Is het een munt van cent of van euro? Tel dan alles op.

- **Hint 1 (te schrijven):** Begin bij de munt die het meest waard is.
- **Hint 2 (te schrijven):** Tel de andere munten er één voor één bij. Een euro is honderd cent.
- **Ouderzin:** Je kind telt munten tot twee euro bij elkaar.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `aantal munten (3)` (€3) → Je hebt de munten geteld. De vraag is hoeveel geld het samen is. Kijk wat elke munt waard is.  [nieuw]
  - `aantal munten (4)` (€4) → Je hebt de munten geteld. De vraag is hoeveel geld het samen is. Kijk wat elke munt waard is.  [nieuw]
  - `munten vergeten` (Claudes sleutel: geld-verkeerd-geteld) → Dat is te weinig. Leg de munten op volgorde van groot naar klein en tel ze één voor één op.  [Claude, taalfix]
  - `euro en cent door elkaar` (Claudes sleutel: kommagetal-als-geheel) → Dat is veel te veel. Kijk goed naar elke munt: is het een munt van cent of van euro? Honderd cent is één euro.  [Claude, taalfix]
  - `andere fout` (andere fout) → Leg de munten op volgorde van groot naar klein. Tel ze één voor één bij elkaar. Een euro is honderd cent.  [nieuw]
- Status: hints klaar
