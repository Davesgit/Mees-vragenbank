# G3-MKU-K03 — Cirkel, driehoek, vierkant

Onze omschrijving: Cirkel/driehoek/vierkant/rechthoek benoemen & herkennen · in onze bank: 4 items

Claude-vragen gemapt: **11** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [figuur] Hoe heet deze [kleur] vorm?

- Items: **9** · Claude-doelen: K1 (9) · regel: R19-vormen
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (18)
- Verschillende Claude-fout-hints: 4 (meest: “Tel de hoeken. Een cirkel heeft geen hoeken.”)
- Voorbeelden:
  - `G3-MKU-K03-claude-bank-006` (Claude K1, gegenereerd, niveau 1 → basis)
    - **Opgave:** Hoe heet deze paarse vorm?
    - **Tekening:** `{"kleur": "#7a6ea8", "soort": "figuur", "figuur": "driehoek"}`
    - **Opties:** A) driehoek · B) rechthoek · C) cirkel
    - **Antwoord:** driehoek  (controle: ok)
    - **Fout-hints (Claude):** rechthoek → Tel de hoeken. Een rechthoek heeft er 4. · cirkel → Tel de hoeken. Een cirkel heeft geen hoeken.
    - **Uitleg (Claude):** Een driehoek heeft 3 hoeken en 3 zijden.
  - `G3-MKU-K03-claude-bank-001` (Claude K1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Hoe heet deze groene vorm?
    - **Tekening:** `{"kleur": "#4d8f6a", "soort": "figuur", "figuur": "rechthoek"}`
    - **Opties:** A) cirkel · B) rechthoek · C) vierkant
    - **Antwoord:** rechthoek  (controle: ok)
    - **Fout-hints (Claude):** vierkant → Tel de hoeken. Een vierkant heeft er 4. · cirkel → Tel de hoeken. Een cirkel heeft geen hoeken.
    - **Uitleg (Claude):** Een rechthoek heeft 4 hoeken en 4 zijden. Twee zijden zijn lang en twee zijn kort.

- **Hint 1 (te schrijven):** Heeft de vorm hoeken? Tel ze.
- **Hint 2 (te schrijven):** Is de vorm rond, zonder hoeken? Of tel je drie of vier hoeken? Bij vier hoeken kijk je ook of alle kanten even lang zijn.
- **Ouderzin:** Je kind herkent en benoemt cirkel, driehoek, vierkant en rechthoek.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = cirkel) → Tel de hoeken. Een cirkel heeft geen hoeken.  [Claude, ok]
  - (fout = driehoek) → Tel de hoeken. Een driehoek heeft er 3.  [Claude, ok]
  - (fout = rechthoek (bij een driehoek of cirkel)) → Tel de hoeken. Een rechthoek heeft er 4.  [Claude, ok]
  - `vierkant bij cirkel of driehoek` (fout = vierkant bij een cirkel of driehoek) → Tel de hoeken. Een vierkant heeft er 4.  [nieuw]
  - `vierkant of rechthoek` (fout = vierkant bij een rechthoek, of rechthoek bij een vierkant) → Allebei hebben ze vier hoeken. Bij een vierkant zijn alle kanten even lang. Kijk goed naar de kanten.  [nieuw]
  - `andere vorm` (fout = ruit, ster of zeshoek) → Kijk goed naar de hoeken en de kanten. Welke vorm uit de klas lijkt erop?  [nieuw]
- Status: hints klaar

## Somtype 2: [figuur] Hoeveel hoeken heeft deze vorm?

- Items: **2** · Claude-doelen: K1 (2) · regel: R19-vormen
- Getallenruimte: n.v.t. · type: kale
- Denkfouten (Claude): een-ernaast (4)
- Verschillende Claude-fout-hints: 2 (meest: “Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek.”)
- Voorbeelden:
  - `G3-MKU-K03-claude-bank-011` (Claude K1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Hoeveel hoeken heeft deze vorm?
    - **Tekening:** `{"kleur": "#d4a017", "soort": "figuur", "figuur": "vierkant"}`
    - **Antwoord:** 4  (controle: ok)
    - **Fout-hints (Claude):** 5 → Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek. · 3 → Je hebt een hoek overgeslagen. Ga de vorm rond en tel elke hoek één keer.
    - **Uitleg (Claude):** Dit is een vierkant. Een vierkant heeft 4 hoeken.
  - `G3-MKU-K03-claude-bank-010` (Claude K1, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Hoeveel hoeken heeft deze vorm?
    - **Tekening:** `{"kleur": "#4d8f6a", "soort": "figuur", "figuur": "driehoek"}`
    - **Antwoord:** 3  (controle: ok)
    - **Fout-hints (Claude):** 4 → Tel de punten waar twee zijden bij elkaar komen, en zet je vinger op elke hoek. · 2 → Je hebt een hoek overgeslagen. Ga de vorm rond en tel elke hoek één keer.
    - **Uitleg (Claude):** Dit is een driehoek. Een driehoek heeft 3 hoeken.

- **Hint 1 (te schrijven):** Een hoek is een punt waar twee kanten elkaar raken.
- **Hint 2 (te schrijven):** Zet je vinger op één hoek. Ga de vorm rond en tel elke hoek één keer. Stop als je weer bij het begin bent.
- **Ouderzin:** Je kind telt de hoeken van een vlakke vorm.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
