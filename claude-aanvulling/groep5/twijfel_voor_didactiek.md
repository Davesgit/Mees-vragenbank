# G5-twijfel voor Didactiek (9 items)

Uit de G5-merge (`claude-merge/g5/data/twijfel.json`, build 1 okt 15:25). Per item: de tekst, het antwoord, de fout-hints van Claude (open antwoord, geen opties) en het voorstel van de merge. De items staan nu niet in G5 en niet in de G6-pool, ze wachten op dit besluit.

## 1. Geld keer een getal, precies uitrekenen (8 items)

**Vraag aan Didactiek:** de spine van G5-GET-E08 zegt 'schattend × met geld'. Deze items vragen het precieze bedrag (€2,94 × 4). Horen ze in G5-GET-E08, of pas in G6-GET-E07 (× met geld)?

**Voorstel merge:** G5-GET-E08, op niveau *toepassen*. De aanpak in de uitleg ('euro's en centen apart, dan samen') is G5-rekenen, en de vermenigvuldigers zijn klein (2, 3 of 4). Item 004 gaat niet over de euro heen (93 cent) en is de makkelijkste, dus op *basis*. Vindt Didactiek precies uitrekenen te zwaar voor G5, dan gaan alle 8 naar G6-GET-E07. Een tussenvorm kan ook: eerst een schatvraag ('Is €10 genoeg?'), dan het precieze bedrag.

| # | id | tekst | antwoord | centen samen | voorstel |
|---|---|---|---|---|---|
| 1 | `G5-GET-E08-claude-bank-twijfel-001` | Eén wortel kost €3,94. Je koopt er 2. Hoeveel betaal je? | €7,88 | 188 cent (boven de euro) | G5-GET-E08, toepassen |
| 2 | `G5-GET-E08-claude-bank-twijfel-002` | Eén sticker kost €2,94. Je koopt er 4. Hoeveel betaal je? | €11,76 | 376 cent (boven de euro) | G5-GET-E08, toepassen |
| 3 | `G5-GET-E08-claude-bank-twijfel-003` | Eén bal kost €1,34. Je koopt er 4. Hoeveel betaal je? | €5,36 | 136 cent (boven de euro) | G5-GET-E08, toepassen |
| 4 | `G5-GET-E08-claude-bank-twijfel-004` | Eén bal kost €2,31. Je koopt er 3. Hoeveel betaal je? | €6,93 | 93 cent (niet over de euro) | G5-GET-E08, basis |
| 5 | `G5-GET-E08-claude-bank-twijfel-005` | Eén sticker kost €2,42. Je koopt er 4. Hoeveel betaal je? | €9,68 | 168 cent (boven de euro) | G5-GET-E08, toepassen |
| 6 | `G5-GET-E08-claude-bank-twijfel-006` | Eén schrift kost €2,74. Je koopt er 4. Hoeveel betaal je? | €10,96 | 296 cent (boven de euro) | G5-GET-E08, toepassen |
| 7 | `G5-GET-E08-claude-bank-twijfel-007` | Eén pen kost €3,26. Je koopt er 4. Hoeveel betaal je? | €13,04 | 104 cent (boven de euro) | G5-GET-E08, toepassen |
| 8 | `G5-GET-E08-claude-bank-twijfel-008` | Eén zak noten kost €2,71. Je koopt er 4. Hoeveel betaal je? | €10,84 | 284 cent (boven de euro) | G5-GET-E08, toepassen |

Fout-hints van Claude (bij elk item dezelfde drie soorten):
- prijs + aantal (€3,94 + 2 = €5,94): 'Je koopt 2 keer hetzelfde. Dat is 2 keer de prijs, niet de prijs plus 2.'
- alleen de euro's keer het aantal, centen één keer (€6,94): 'De centen moet je ook keer het aantal doen, niet één keer meetellen.'
- een euro te veel (€8,88): 'Komen de centen samen boven de 100? Alleen dan gaat er een euro bij.'

Uitleg van Claude (voorbeeld 001): 'Reken de euro's en de centen apart. 2 × €3 = €6. 2 × 94 cent = 188 cent. Samen €7,88.'

## 2. Drie kwart van een hoeveelheid (1 item)

**Vraag aan Didactiek:** de SLO-doelen voor eind G5 noemen 'een kwart'. Drie kwart is een stap verder. Hoort dit in G5-VERH-E01 of pas in G6-VERH-E02 (breuk, deel van)?

- `G5-VERH-E01-claude-bank-twijfel-001`: **Er zijn 8 koekjes. Kleur drie kwart van de koekjes.** Antwoord: **6** (kleuren; de app telt de gekleurde koekjes).
- Foute optie met hint: '2': '2 is maar één deel. Je hebt 3 delen nodig.'
- Uitleg van Claude: 'Eerst 8 : 4 = 2, dat is één deel. Dan 3 delen: 3 × 2 = 6.'
- **Voorstel merge:** G5-VERH-E01, op niveau *uitdaging* (kritisch), want de stap '8 : 4 = 2, dan 3 × 2' gebruikt alleen het kwart en een G5-tafel. Kiest Didactiek voor later, dan gaat het naar G6-VERH-E02 (breuk deel van), en daar past het op basis.

## Wat er na het besluit gebeurt
- G5: het besluit gaat in `regels_g5.py` (zoals de G4-besluiten in `besluiten_g4.py`). Daarna een nieuwe build; de ids zijn bevroren.
- Kiest Didactiek voor G6, dan gaan de items naar de G6-pool. Bij de G6-merge van 1 okt zitten ze daar nog niet in.
