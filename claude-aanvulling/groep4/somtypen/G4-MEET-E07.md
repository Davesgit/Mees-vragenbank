# G4-MEET-E07 — Betalen tot honderd euro

Onze omschrijving: Geld: alle munten/briefjes; ≤2€ met munten; ≤100€ samenstellen/inwisselen · in onze bank: 8 items

Claude-vragen gemapt: **24** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [geld] Hoeveel [ding] zie je? — met centen

- Sleutel: nrOrigineel **1** · somtypeOrigineel “[geld] Hoeveel [ding] zie je? — met centen” (koppeling: claudeId)
- Items: **24** · Claude-doelen: M5 (24) · regel: D-CENT-ONDER1, D-CENT-HEEL
- Getallenruimte: 0–2 euro (munten, zonder komma) · type: meerkeuze
- **Visual: nodig** (24 items): Claude-tekenaar: soort “geld”; tekening verplicht: munten op ware kleur en grootte (Didactiek §2)
- Merge-fixlijst: #32 geld als €N (11), #32 €101 → €3 (1)
- Didactiek-besluit (G4-twijfel, 1 okt): hele euro (€1/€2), onder 1 euro → “N cent” — zie besluiten_twijfel.md
- Uitleg bij het eerste gebruik (kindtekst, veld begripUitleg): “100 cent is 1 euro.”
- Denkfouten (Claude): geld-verkeerd-geteld (32), kommagetal-als-geheel (9), getal-overgenomen (7)
- Verschillende Claude-fout-hints: 3 (meest: “Leg de munten op volgorde van groot naar klein en tel ze één voor één op.”)
- Voorbeelden:
  - `G4-MEET-E07-claude-bank-009` (Claude M5, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [10, 5, 5]}`
    - **Opties:** A) €20 · B) 10 cent · C) 20 cent
    - **Antwoord:** 20 cent  (controle: ok)
    - **Fout-hints (Claude):** 10 cent → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. · €20 → Kijk goed naar elke munt. Is het een munt van cent of van euro? Tel dan alles op.
  - `G4-MEET-E07-claude-bank-020` (Claude M5, bank, niveau 2 → toepassen)
    - **Opgave:** Hoeveel geld zie je?
    - **Tekening:** `{"soort": "geld", "munten": [20, 20, 5]}`
    - **Opties:** A) 40 cent · B) 45 cent · C) €45
    - **Antwoord:** 45 cent  (controle: ok)
    - **Fout-hints (Claude):** 40 cent → Leg de munten op volgorde van groot naar klein en tel ze één voor één op. · €45 → Kijk goed naar elke munt. Is het een munt van cent of van euro? Tel dan alles op.

- **Hint 1 (te schrijven):** Kijk bij elke munt of het een munt van cent of van euro is.
- **Hint 2 (te schrijven):** Begin bij de grootste munt. Tel de andere munten er één voor één bij.
- **Ouderzin:** Je kind telt munten bij elkaar op, ook munten van cent.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `aantal munten (€3)` (€3) → Je hebt de munten geteld. De vraag is hoeveel geld het samen is. Kijk wat elke munt waard is.  [nieuw]
  - `aantal munten (€4)` (€4) → Je hebt de munten geteld. De vraag is hoeveel geld het samen is. Kijk wat elke munt waard is.  [nieuw]
  - `cent en euro door elkaar` (cent als euro geteld (tekst per item)) → Kijk goed naar elke munt. Is het een munt van cent of van euro? Tel dan alles op.  [Claude, ok]
  - `verkeerd geteld` (verkeerd geteld (tekst per item)) → Leg de munten op volgorde van groot naar klein en tel ze één voor één op.  [Claude, ok]
  - `andere fout` (andere fout) → Begin bij de grootste munt. Tel de andere munten er één voor één bij. Kijk goed: cent of euro?  [nieuw]
- Status: hints klaar
