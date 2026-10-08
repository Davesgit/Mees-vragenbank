# G4-GET-E04 — Verhaaltjes met plus en min

Onze omschrijving: +/− ↔ context ≤100; strategieën (tiental, compenseren, analogie, inverse) · in onze bank: 8 items

Claude-vragen gemapt: **130** in **2** somtypen · twijfel (voorstel dit doel): **0**

Invoer voor het schrijven van hint 1 (`hint`) en hint 2 (`sterkereHint`) per somtype. Velden `hint`, `sterkereHint` en `ouderzin` zijn nog leeg.
Elk somtype heeft een vaste sleutel (nrOrigineel + somtypeOrigineel, bevroren/somtype_nr_v1.json): neem die over in hints/batch*.json, dan blijft de hint gekoppeld als de nummering of de kop verandert.
Bron: Leermees open vragenbank, CC BY-SA 4.0, leermees.nl · https://github.com/Davesgit/leermees-vragenbank @ 7da3257

## Somtype 1: In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **1** · somtypeOrigineel “In [plek] liggen # [ding]. Er gaan er # uit. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **67** · Claude-doelen: T9 (67) · regel: G07-welke-som
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): kleinste-van-grootste (67), verkeerde-bewerking (67)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G4-GET-E04-claude-bank-035` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de trommel liggen 39 ballen. Er gaan er 8 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 39 + 8 · B) 39 − 8 · C) 8 − 39
    - **Antwoord:** 39 − 8  (controle: ok)
    - **Fout-hints (Claude):** 39 + 8 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G4-GET-E04-claude-bank-050` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de zak liggen 57 appels. Er gaan er 3 uit. Welke som hoort bij dit verhaal?
    - **Opties:** A) 57 + 3 · B) 57 − 3 · C) 3 − 57
    - **Antwoord:** 57 − 3  (controle: ok)
    - **Fout-hints (Claude):** 57 + 3 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er gaan dingen uit, dus het worden er minder. Dat is een minsom. Zoek de som die begint bij het getal dat er eerst in lag.
- **Ouderzin:** Je kind kiest de minsom die past bij een verhaal tot 100 waarin er dingen uitgaan.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de minsom omgedraaid` (de minsom omgedraaid (klein getal min groot getal)) → Die som begint bij het verkeerde getal. Begin bij wat er eerst in lag. Daar gaan er een paar af.  [nieuw]
  - `de plussom` (de plussom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
- Status: hints klaar

## Somtype 2: In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?

- Sleutel: nrOrigineel **2** · somtypeOrigineel “In [plek] liggen # [ding]. Er komen er # bij. Welke som hoort bij dit verhaal?” (koppeling: claudeId)
- Items: **63** · Claude-doelen: T9 (63) · regel: G07-welke-som
- Getallenruimte: 0–100 · type: meerkeuze
- Denkfouten (Claude): verkeerde-bewerking (63), verkeerd-getal (63)
- Verschillende Claude-fout-hints: 1 (meest: “Lees de vraag nog eens: komt er iets bij, of gaat er iets af?”)
- Voorbeelden:
  - `G4-GET-E04-claude-bank-096` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de bak liggen 32 ballen. Er komen er 5 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 32 − 5 · B) 32 + 5 · C) 32 + 6
    - **Antwoord:** 32 + 5  (controle: ok)
    - **Fout-hints (Claude):** 32 − 5 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?
  - `G4-GET-E04-claude-bank-106` (Claude T9, bank, niveau 1 → basis)
    - **Opgave:** In de trommel liggen 43 appels. Er komen er 6 bij. Welke som hoort bij dit verhaal?
    - **Opties:** A) 43 − 6 · B) 43 + 7 · C) 43 + 6
    - **Antwoord:** 43 + 6  (controle: ok)
    - **Fout-hints (Claude):** 43 − 6 → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?

- **Hint 1 (te schrijven):** Lees het verhaal goed. Komen er dingen bij, of gaan er dingen uit?
- **Hint 2 (te schrijven):** Er komen dingen bij, dus het worden er meer. Dat is een plussom. Zoek de som met het getal dat er al lag en het getal dat erbij komt.
- **Ouderzin:** Je kind kiest de plussom die past bij een verhaal tot 100 waarin er dingen bijkomen.
- **Fout-hints:** fout-hints Claude: deels ok — per soort fout, regels van boven naar beneden (de eerste die past):
  - `de minsom` (de minsom) → Lees de vraag nog eens: komt er iets bij, of gaat er iets af?  [Claude, ok]
  - `ander getal erbij` (de plussom (afleider a + (b+1) of a + (b−1))) → Dat is wel een plussom. Maar één getal klopt niet. Hoeveel lagen er al? En hoeveel komen erbij?  [nieuw]
- Status: hints klaar
