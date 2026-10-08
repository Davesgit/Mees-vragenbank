# G3-MKU-E04 — Figuren vergelijken

Onze omschrijving: Verschillen tussen figuren; uitslagen bij eenvoudige ruimtelijke figuren · in onze bank: 8 items

Claude-vragen gemapt: **2** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [figuur] Hoeveel hoeken heeft deze vorm?

- Items: **2** · Claude-doelen: K1 (2) · regel: D-vormen (R19-vormen)
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): een-ernaast (4)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek.”)
- Voorbeelden:
  - `G3-MKU-E04-claude-bank-001` (Claude K1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Hoeveel hoeken heeft deze vorm?
    - **Tekening:** `{"kleur": "#d4a017", "soort": "figuur", "figuur": "zeshoek"}`
    - **Antwoord:** 6  (controle: ok)
    - **Fout-hints (Claude):** 7 → Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek. · 5 → Je hebt een hoek overgeslagen. Ga de vorm rond en tel elke hoek één keer.
    - **Uitleg (Claude):** Zet je vinger op elke hoek en tel. Deze vorm heeft 6 hoeken.
  - `G3-MKU-E04-claude-bank-002` (Claude K1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Hoeveel hoeken heeft deze vorm?
    - **Tekening:** `{"kleur": "#4d8f6a", "soort": "figuur", "figuur": "vijfhoek"}`
    - **Antwoord:** 5  (controle: ok)
    - **Fout-hints (Claude):** 6 → Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek. · 4 → Je hebt een hoek overgeslagen. Ga de vorm rond en tel elke hoek één keer.
    - **Uitleg (Claude):** Zet je vinger op elke hoek en tel. Deze vorm heeft 5 hoeken.

- **Hint 1 (te schrijven):** Zet je vinger op een hoek. Ga de vorm rond en tel elke hoek.
- **Hint 2 (te schrijven):** Begin bij een hoek die je goed onthoudt. Stop als je weer bij die hoek bent. Tel elke hoek maar één keer.
- **Ouderzin:** Je kind telt de hoeken van een vorm.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `een te veel` (fout = antwoord + 1) → Je hebt een hoek twee keer geteld. Zet je vinger op elke hoek en tel hem maar één keer.  [nieuw]
  - (fout = antwoord − 1) → Je hebt een hoek overgeslagen. Ga de vorm rond en tel elke hoek één keer.  [Claude, ok]
  - `andere fout` (andere fout) → Zet je vinger op een hoek. Ga de vorm rond en tel elke hoek één keer.  [nieuw]
- Status: hints klaar
