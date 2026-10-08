# G8-MEET-E03 — Inhoudsmaten en wat vergroten doet

Onze omschrijving: Inhoud: metriek-systeem; effect vergroten op inhoud · in onze bank: 8 items

Claude-vragen gemapt: **32** in **9** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v*.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: Een filmpje is # MB. De geheugenkaart is # GB (# GB = # MB). Hoeveel van die filmpjes passen erop?

- Sleutel: nrOrigineel **5** · somtypeOrigineel “Een filmpje is # MB. De geheugenkaart is # GB (# GB = # MB). Hoeveel van die filmpjes passen erop?” (koppeling: claudeId)
- Items: **16** · Claude-doelen: M29 (16) · regel: D8-GEHEUGEN-CONTEXT, D8-GEHEUGEN-DUBBEL-NIEUWE-GETALLEN
- Getallenruimte: 0–1.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 20 (meest: “Je hebt een nul te weinig. Zet eerst alles in MB. 16 GB is 16.000 MB.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-016` (Claude M29, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een filmpje is 400 MB. De geheugenkaart is 16 GB (1 GB = 1000 MB). Hoeveel van die filmpjes passen erop?
    - **Antwoord:** 40  (controle: n.v.t.)
    - **Fout-hints (Claude):** 4 → Zet eerst alles in MB: 16 GB = 16.000 MB. · 400 → 16.000 : 400, let op de nullen.
    - **Uitleg (Claude):** 16 GB = 16.000 MB. 16.000 : 400 = 40 foto's.
  - `G8-MEET-E03-claude-bank-007` (Claude M29, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een filmpje is 500 MB. De geheugenkaart is 8 GB (1 GB = 1000 MB). Hoeveel van die filmpjes passen erop?
    - **Antwoord:** 16  (controle: n.v.t.)
    - **Fout-hints (Claude):** 1 → Zet eerst alles in MB: 8 GB = 8000 MB. · 160 → 8000 : 500, let op de nullen.
    - **Uitleg (Claude):** 8 GB = 8000 MB. 8000 : 500 = 16 foto's.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 2: Een harde schijf heeft # TB. Hoeveel GB is dat? (# TB = # GB)

- Sleutel: nrOrigineel **6** · somtypeOrigineel “Een harde schijf heeft # TB. Hoeveel GB is dat? (# TB = # GB)” (koppeling: claudeId)
- Items: **5** · Claude-doelen: M29 (5) · regel: D8-GEHEUGEN-CONTEXT
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “1 TB is 1000 GB, niet 100.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-028` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een harde schijf heeft 3 TB. Hoeveel GB is dat? (1 TB = 1000 GB)
    - **Antwoord:** 3000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 300 → 1 TB is 1000 GB, niet 100. · 3.072.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 TB = 1000 GB, dus 3 TB = 3 × 1000 = 3000 GB.
  - `G8-MEET-E03-claude-bank-029` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een harde schijf heeft 32 TB. Hoeveel GB is dat? (1 TB = 1000 GB)
    - **Antwoord:** 32.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3200 → 1 TB is 1000 GB, niet 100. · 32.768.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 TB = 1000 GB, dus 32 TB = 32 × 1000 = 32.000 GB.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 3: Een foto is # MB. Hoeveel KB is dat? (# MB = # KB)

- Sleutel: nrOrigineel **7** · somtypeOrigineel “Een foto is # MB. Hoeveel KB is dat? (# MB = # KB)” (koppeling: claudeId)
- Items: **3** · Claude-doelen: M29 (3) · regel: D8-GEHEUGEN-CONTEXT
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “1 MB is 1000 KB, niet 100.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-023` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een foto is 8 MB. Hoeveel KB is dat? (1 MB = 1000 KB)
    - **Antwoord:** 8000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 800 → 1 MB is 1000 KB, niet 100. · 8.192.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 MB = 1000 KB, dus 8 MB = 8 × 1000 = 8000 KB.
  - `G8-MEET-E03-claude-bank-024` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een foto is 4 MB. Hoeveel KB is dat? (1 MB = 1000 KB)
    - **Antwoord:** 4000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 400 → 1 MB is 1000 KB, niet 100. · 4.096.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 MB = 1000 KB, dus 4 MB = 4 × 1000 = 4000 KB.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 4: Een geheugenkaart heeft # GB. Hoeveel MB is dat? (# GB = # MB)

- Sleutel: nrOrigineel **8** · somtypeOrigineel “Een geheugenkaart heeft # GB. Hoeveel MB is dat? (# GB = # MB)” (koppeling: claudeId)
- Items: **3** · Claude-doelen: M29 (3) · regel: D8-GEHEUGEN-FOUTSLEUTEL
- Getallenruimte: 0–10.000, 0–100.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “1 GB is 1000 MB, niet 100.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-026` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een geheugenkaart heeft 32 GB. Hoeveel MB is dat? (1 GB = 1000 MB)
    - **Antwoord:** 32.000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 3200 → 1 GB is 1000 MB, niet 100. · 32.768.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 GB = 1000 MB, dus 32 GB = 32 × 1000 = 32.000 MB.
  - `G8-MEET-E03-claude-bank-027` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een geheugenkaart heeft 8 GB. Hoeveel MB is dat? (1 GB = 1000 MB)
    - **Antwoord:** 8000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 800 → 1 GB is 1000 MB, niet 100. · 8.192.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 GB = 1000 MB, dus 8 GB = 8 × 1000 = 8000 MB.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 5: Een bak voor knopen heeft een inhoud van # [ding]. Hoeveel liter is dat?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “Een bak voor knopen heeft een inhoud van # [ding]. Hoeveel liter is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M25 (1) · regel: G8-M25-m3-liter
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een m³ is duizend liter, niet honderd.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-001` (Claude M25, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bak voor knopen heeft een inhoud van 3 m³. Hoeveel liter is dat?
    - **Antwoord:** 3000  (controle: ok)
    - **Fout-hints (Claude):** 300 → Een m³ is duizend liter, niet honderd. · 30.000 → Een nul te veel. 1 m³ = 1000 liter.
    - **Uitleg (Claude):** 1 m³ = 1000 liter. 3 × 1000 = 3000 liter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 6: Een bak voor tanden heeft een inhoud van # [ding]. Hoeveel liter is dat?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “Een bak voor tanden heeft een inhoud van # [ding]. Hoeveel liter is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M25 (1) · regel: G8-M25-m3-liter
- Getallenruimte: kommagetallen (1 cijfers achter de komma) · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een m³ is duizend liter, niet honderd.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-002` (Claude M25, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bak voor tanden heeft een inhoud van 1,5 m³. Hoeveel liter is dat?
    - **Antwoord:** 1500  (controle: ok)
    - **Fout-hints (Claude):** 150 → Een m³ is duizend liter, niet honderd. · 15.000 → Een nul te veel. 1 m³ = 1000 liter.
    - **Uitleg (Claude):** 1 m³ = 1000 liter. 1,5 × 1000 = 1500 liter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 7: Een bak voor truien heeft een inhoud van # [ding]. Hoeveel liter is dat?

- Sleutel: nrOrigineel **3** · somtypeOrigineel “Een bak voor truien heeft een inhoud van # [ding]. Hoeveel liter is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M25 (1) · regel: G8-M25-m3-liter
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een m³ is duizend liter, niet honderd.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-003` (Claude M25, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bak voor truien heeft een inhoud van 3 m³. Hoeveel liter is dat?
    - **Antwoord:** 3000  (controle: ok)
    - **Fout-hints (Claude):** 300 → Een m³ is duizend liter, niet honderd. · 30.000 → Een nul te veel. 1 m³ = 1000 liter.
    - **Uitleg (Claude):** 1 m³ = 1000 liter. 3 × 1000 = 3000 liter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 8: Een bak voor wortels heeft een inhoud van # [ding]. Hoeveel liter is dat?

- Sleutel: nrOrigineel **4** · somtypeOrigineel “Een bak voor wortels heeft een inhoud van # [ding]. Hoeveel liter is dat?” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M25 (1) · regel: G8-M25-m3-liter
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): eenheid-verkeerd-omgerekend (2)
- Verschillende Claude-fout-hints: 2 (meest: “Een m³ is duizend liter, niet honderd.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-004` (Claude M25, gegenereerd, niveau 2 → toepassen)
    - **Opgave:** Een bak voor wortels heeft een inhoud van 3 m³. Hoeveel liter is dat?
    - **Antwoord:** 3000  (controle: ok)
    - **Fout-hints (Claude):** 300 → Een m³ is duizend liter, niet honderd. · 30.000 → Een nul te veel. 1 m³ = 1000 liter.
    - **Uitleg (Claude):** 1 m³ = 1000 liter. 3 × 1000 = 3000 liter.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 

## Somtype 9: Een film is # GB. Hoeveel MB is dat? (# GB = # MB)

- Sleutel: nrOrigineel **9** · somtypeOrigineel “Een film is # GB. Hoeveel MB is dat? (# GB = # MB)” (koppeling: claudeId)
- Items: **1** · Claude-doelen: M29 (1) · regel: D8-GEHEUGEN-CONTEXT
- Getallenruimte: 0–10.000 · type: kale
- Denkfouten (Claude): —
- Verschillende Claude-fout-hints: 2 (meest: “1 GB is 1000 MB, niet 100.”)
- Voorbeelden:
  - `G8-MEET-E03-claude-bank-005` (Claude M29, gegenereerd, niveau 1 → basis)
    - **Opgave:** Een film is 3 GB. Hoeveel MB is dat? (1 GB = 1000 MB)
    - **Antwoord:** 3000  (controle: n.v.t.)
    - **Fout-hints (Claude):** 300 → 1 GB is 1000 MB, niet 100. · 3.072.000 → Eén stap: keer 1000.
    - **Uitleg (Claude):** 1 GB = 1000 MB, dus 3 GB = 3 × 1000 = 3000 MB.

- **Hint 1 (te schrijven):** 
- **Hint 2 (te schrijven):** 
