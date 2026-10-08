# G3-MEET-E05 — Hele uren op de klok

Onze omschrijving: Tijd: weekdagen; hele uren analoog/digitaal; instrumenten · in onze bank: 8 items

Claude-vragen gemapt: **74** in **3** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: [klokkenrij] Welke klok wijst # uur aan?

- Items: **46** · Claude-doelen: M3 (46) · regel: R16-klok
- Getallenruimte: hele uren 1–12 · type: meerkeuze
- **Husselen: nee** (de opties zijn de labels van de klokken in de tekening) — geldt voor alle 46 items
- Denkfouten (Claude): klok-verkeerd-gelezen (92)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G3-MEET-E05-claude-bank-041` (Claude M3, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst 2 uur aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 12, "minuut": 0}, {"uur": 2, "minuut": 0}, {"uur": 3, "minuut": 0}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G3-MEET-E05-claude-bank-077` (Claude M3, bank, niveau 2 → toepassen)
    - **Opgave:** Welke klok wijst 8 uur aan?
    - **Tekening:** `{"soort": "klokkenrij", "klokken": [{"uur": 9, "minuut": 0}, {"uur": 8, "minuut": 0}, {"uur": 7, "minuut": 0}], "labels": ["A", "B", "C"]}`
    - **Opties:** A) A · B) B · C) C
    - **Husselen:** nee (de opties zijn de labels van de klokken in de tekening)
    - **Antwoord:** B  (controle: ok)
    - **Fout-hints (Claude):** A → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · C → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Bij een heel uur wijst de grote wijzer recht omhoog. Kijk dan naar de kleine wijzer.
- **Hint 2 (te schrijven):** Kijk bij elke klok waar de kleine wijzer naar wijst. Dat getal is het uur. Welke klok past bij het uur uit de vraag?
- **Ouderzin:** Je kind kiest de klok die een heel uur aanwijst.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `andere klok` (een klok met een ander uur) → Kijk naar de kleine wijzer van die klok. Wijst hij naar het uur uit de vraag?  [nieuw]
- Status: hints klaar

## Somtype 2: [klok] Hoe laat is het op deze klok?

- Items: **16** · Claude-doelen: M3 (16) · regel: R16-klok
- Getallenruimte: hele uren 1–12 · type: meerkeuze
- Denkfouten (Claude): klok-verkeerd-gelezen (32)
- Verschillende Claude-fout-hints: 1 (meest: “Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?”)
- Voorbeelden:
  - `G3-MEET-E05-claude-bank-038` (Claude M3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 2, "soort": "klok", "minuut": 0}`
    - **Opties:** A) 12 uur · B) 2 uur · C) 3 uur
    - **Antwoord:** 2 uur  (controle: ok)
    - **Fout-hints (Claude):** 12 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 3 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?
  - `G3-MEET-E05-claude-bank-037` (Claude M3, bank, niveau 2 → toepassen)
    - **Opgave:** Hoe laat is het op deze klok?
    - **Tekening:** `{"uur": 10, "soort": "klok", "minuut": 0}`
    - **Opties:** A) 10 uur · B) 12 uur · C) 11 uur
    - **Antwoord:** 10 uur  (controle: ok)
    - **Fout-hints (Claude):** 12 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna? · 11 uur → Kijk eerst naar de kleine wijzer: welk uur is het geweest? Dan de grote wijzer: hoeveel minuten daarna?

- **Hint 1 (te schrijven):** Kijk naar de kleine wijzer. Naar welk getal wijst hij?
- **Hint 2 (te schrijven):** De grote wijzer staat recht omhoog, dus het is een heel uur. De kleine wijzer wijst naar het uur.
- **Ouderzin:** Je kind leest een heel uur af op een klok met wijzers.
- **Fout-hints:** fout-hints Claude: vervangen — per soort fout, regels van boven naar beneden (de eerste die past):
  - `grote wijzer gelezen` (fout = 12 uur (en het antwoord is geen 12 uur)) → Je keek naar de grote wijzer. Het uur zie je aan de kleine wijzer.  [nieuw]
  - `uur ernaast` (fout = een uur te vroeg of te laat) → Kijk goed waar de kleine wijzer naar wijst. Wijst hij precies naar dat getal?  [nieuw]
- Status: hints klaar

## Somtype 3: [klok-zetten (wijzers slepen)] Zet de klok op [uur] uur.

- Items: **12** · Claude-doelen: M3 (12) · regel: R16-klok
- Getallenruimte: hele uren 1–12 · type: kale
- Denkfouten (Claude): klok-verkeerd-gelezen (12)
- Verschillende Claude-fout-hints: 12 (meest: “Bij negen uur wijst de kleine wijzer naar de 9.”)
- Voorbeelden:
  - `G3-MEET-E05-claude-bank-002` (Claude M3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet de klok op negen uur.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 9.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 10.00 uur → Bij negen uur wijst de kleine wijzer naar de 9.
    - **Uitleg (Claude):** De grote wijzer staat op de 12, de kleine wijzer wijst naar de 9.
  - `G3-MEET-E05-claude-bank-012` (Claude M3, gegenereerd, niveau 1 → basis)
    - **Opgave:** Zet de klok op acht uur.
    - **UI:** klok-zetten (wijzers slepen)
    - **Antwoord:** 8.00 uur  (controle: ok)
    - **Fout-hints (Claude):** 9.00 uur → Bij acht uur wijst de kleine wijzer naar de 8.
    - **Uitleg (Claude):** De grote wijzer staat op de 12, de kleine wijzer wijst naar de 8.

- **Hint 1 (te schrijven):** Bij een heel uur staat de grote wijzer recht omhoog.
- **Hint 2 (te schrijven):** Zet de grote wijzer recht omhoog. Draai daarna de kleine wijzer naar het getal van het uur.
- **Ouderzin:** Je kind zet de wijzers van een klok op een heel uur.
- **Fout-hints:** fout-hints Claude: taalfix — per soort fout, regels van boven naar beneden (de eerste die past):
  - (fout = een uur te laat (tekst per item)) → Bij [uur in woorden] uur wijst de kleine wijzer naar de [uur als cijfer].  [Claude, taalfix]
- Status: hints klaar
