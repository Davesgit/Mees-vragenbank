# G3-VBN-E03 — Patronen zien en doorzetten

Onze omschrijving: Patroon in figuren zien/voortzetten; kritisch over fout in patroon · in onze bank: 8 items

Claude-vragen gemapt: **24** in **1** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [figurenrij] Kijk goed naar de rij. Welke vorm komt op de lege plek?

- Items: **24** · Claude-doelen: K2 (24) · regel: R20-patroon-figuren
- Getallenruimte: n.v.t. · type: meerkeuze
- Denkfouten (Claude): None (48)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk welk stukje zich steeds herhaalt en zeg de rij hardop. Wat komt er dan?”)
- Voorbeelden:
  - `G3-VBN-E03-claude-bank-002` (Claude K2, gegenereerd, niveau 1 → basis)
    - **Opgave:** Kijk goed naar de rij. Welke vorm komt op de lege plek?
    - **Tekening:** `{"leeg": 7, "soort": "figurenrij", "figuren": [{"kleur": "#e07b39", "figuur": "cirkel"}, {"kleur": "#3b6ea5", "figuur": "rechthoek"}, {"kleur": "#e07b39", "figuur": "cirkel"}, {"kleur": "#3b6ea5", "figuur": "rechthoek"}, {"kleur": "#e07b39", "figuur": "cirkel"}, {"kleur": "#3b6ea5", "figuur": "rechthoek"}, {"kleur": "#e07b39", "figuur": "cirkel"}]}`
    - **Opties:** A) blauwe rechthoek · B) oranje cirkel · C) paars vierkant
    - **Antwoord:** blauwe rechthoek  (controle: ok)
    - **Fout-hints (Claude):** oranje cirkel → Kijk welk stukje zich steeds herhaalt en zeg de rij hardop. Wat komt er dan? · paars vierkant → Kijk welk stukje zich steeds herhaalt en zeg de rij hardop. Wat komt er dan?
    - **Uitleg (Claude):** Steeds komt hetzelfde terug: oranje cirkel, blauwe rechthoek. Na oranje cirkel komt blauwe rechthoek.
  - `G3-VBN-E03-claude-bank-012` (Claude K2, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Kijk goed naar de rij. Welke vorm komt op de lege plek?
    - **Tekening:** `{"leeg": 7, "soort": "figurenrij", "figuren": [{"kleur": "#e07b39", "figuur": "vierkant"}, {"kleur": "#e07b39", "figuur": "vierkant"}, {"kleur": "#d4a017", "figuur": "cirkel"}, {"kleur": "#e07b39", "figuur": "vierkant"}, {"kleur": "#e07b39", "figuur": "vierkant"}, {"kleur": "#d4a017", "figuur": "cirkel"}, {"kleur": "#e07b39", "figuur": "vierkant"}]}`
    - **Opties:** A) oranje vierkant · B) gele cirkel · C) paarse rechthoek
    - **Antwoord:** oranje vierkant  (controle: ok)
    - **Fout-hints (Claude):** gele cirkel → Kijk welk stukje zich steeds herhaalt en zeg de rij hardop. Wat komt er dan? · paarse rechthoek → Kijk welk stukje zich steeds herhaalt en zeg de rij hardop. Wat komt er dan?
    - **Uitleg (Claude):** Steeds komt hetzelfde terug: oranje vierkant, oranje vierkant, gele cirkel. Na oranje vierkant komt oranje vierkant.

- **Hint 1 (te schrijven):** Welk stukje komt steeds terug?
- **Hint 2 (te schrijven):** Zeg de rij hardop, vorm voor vorm en kleur voor kleur. Wijs het stukje aan dat steeds terugkomt. Wat hoort er dan op de lege plek?
- **Ouderzin:** Je kind zet een rij vormen voort die steeds hetzelfde stukje herhaalt.
- **Fout-hints:** fout-hints Claude: ok
- Status: hints klaar
