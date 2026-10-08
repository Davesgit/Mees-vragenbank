# G7-VERH-04 — Breuk, procent en verhouding koppelen (Claude-pilot)

Status: Didactiek-af 2026-09-18. taal: ok. Parallel concept-track (Claude-pilot); geen merge over Didactiek-af zonder Overzicht.
Bron: Claude-pilot (Kwaliteit-tranche 5, 2026-09-18) — Didactiek taal: ok (parallel track). Zie reviews/claude-tranche5-2026-09-18.md.
Leerdoel-ID: G7-VERH-04
Groep: 7
Bron-slug: breuk-kommagetal-en-procent-omrekenen (Claude = 113/113 “Schrijf X in procenten”; 9× breuk→%, 104× decimaal→%, 0× verhouding, 0× omgekeerd; batch: max 2× “schrijf … in %”, rest %→decimaal / rij-koppel / verhaal / multi · geen “n% van n”)

## 001 · basis · kale · bron: var-omrekenen-g7-0005
- **Opgave:** Schrijf 1/5 als procent.
- **Antwoord:** 20% (accept: 20% / 20)
- **Hint:** 1/5 is één van vijf gelijke stukken van 100.
- **Sterkere hint:** 100 ÷ 5 = 20, dus 1/5 = 20%.
- **Fout-hints:** 5% → Je hebt de noemer als procent genomen; 1/5 van 100 is 20. · 15% → Geen optelling van 1 en 5. · 25% → Dat is 1/4; 1/5 is 20%.
- **Ouderzin:** Je kind zet de breuk 1/5 om naar 20%.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** laag

## 002 · basis · invullen · bron: var-omrekenen-g7-0031 (aangepast naar 0,25)
- **Opgave:** Vul in: 0,25 = ___ %.
- **Antwoord:** 25 (accept: 25 / 25%)
- **Hint:** Decimaal naar procent: vermenigvuldig met 100 (komma twee plaatsen naar rechts).
- **Sterkere hint:** 0,25 × 100 = 25, dus 25%.
- **Fout-hints:** 2,5 → Te weinig; komma twee plaatsen: 0,25 → 25. · 0,25 → Je hebt het decimaal overgenomen; maak er procenten van. · 250 → Te veel nullen; 0,25 × 100 = 25.
- **Ouderzin:** Je kind zet 0,25 om naar procenten.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** laag

## 003 · basis · invullen · bron: breuk-kommagetal-en-procent-omrekenen (herschreven verhouding→%)
- **Opgave:** 1:10 als deel:geheel = ___ %.
- **Antwoord:** 10 (accept: 10 / 10%)
- **Hint:** 1:10 betekent 1 deel van 10 = 1/10. Reken dat om naar procenten.
- **Sterkere hint:** 1/10 van 100 = 10, dus 10%.
- **Fout-hints:** 1 → Je hebt alleen het ‘1’-deel genomen; 1/10 van 100 is 10. · 100 → Dat is het hele; gevraagd is het deel. · 20 → Dat is 1:5; hier is 1:10 = 10%.
- **Ouderzin:** Je kind zet verhouding 1:10 om naar 10%.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** laag

## 004 · toepassen · meerkeuze · bron: breuk-kommagetal-en-procent-omrekenen (herschreven rij-koppel)
- **Opgave:** Welke rij notaties geeft allemaal hetzelfde deel aan?
- **Antwoord:** C
- **Opties:** A) 3/4 · 75% · 0,75 · 1:3 · B) 3/4 · 70% · 0,75 · 3:4 · C) 3/4 · 75% · 0,75 · 3:4 · D) 3/4 · 75% · 0,7 · 3:4
- **Hint:** Reken elke notatie om naar procenten of naar een breuk. Zoek de rij zonder vreemde eend.
- **Sterkere hint:** 3/4 = 75% = 0,75 = 3:4 (deel:geheel). Check per optie welk stukje niet klopt.
- **Fout-hints:** A → 1:3 is 1/3 ≈ 33%, niet 3/4. · B → 70% hoort niet bij 3/4 (dat is 75%). · D → 0,7 is 70%, niet 75% / 0,75.
- **Ouderzin:** Je kind herkent dat 3/4, 75%, 0,75 en 3:4 hetzelfde deel zijn.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** midden

## 005 · toepassen · meerkeuze · bron: breuk-kommagetal-en-procent-omrekenen (herschreven %→breuk)
- **Opgave:** Welke breuk is gelijk aan 40%?
- **Antwoord:** B
- **Opties:** A) 1/4 · B) 2/5 · C) 4/5 · D) 1/40
- **Hint:** Procent → breuk: schrijf als …/100 en vereenvoudig, of gebruik de koppeltabel.
- **Sterkere hint:** 40% = 40/100. Deel teller en noemer door 20: 2/5.
- **Fout-hints:** A → 1/4 = 25%, niet 40%. · C → 4/5 = 80%; dat is het dubbele van 40%. · D → Je hebt ‘40’ in de noemer gezet; 40% is 40/100 = 2/5.
- **Ouderzin:** Je kind koppelt 40% aan de breuk 2/5.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** midden

## 006 · toepassen · verhaal · bron: breuk-kommagetal-en-procent-omrekenen (herschreven verhaal)
- **Opgave:** Op een taart staat: “¾ van de taart is verkocht.” Hoeveel procent van de taart is dat?
- **Antwoord:** 75% (accept: 75% / 75)
- **Hint:** 3/4 is driekwart. Hoeveel procent is driekwart van 100?
- **Sterkere hint:** 1/4 = 25%, dus 3/4 = 3 × 25% = 75%.
- **Fout-hints:** 34% → Breuk is geen ‘vierendertig’. · 25% → Dat is één kwart (1/4); hier zijn driekwart verkocht. · 3% → Je hebt de teller als procent genomen.
- **Ouderzin:** Je kind zet ‘¾ van de taart’ om naar 75%.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** midden

## 007 · toepassen · verhaal · bron: breuk-kommagetal-en-procent-omrekenen (herschreven verhaal)
- **Opgave:** In de klas is 60% van de leerlingen lid van de bibliotheek. Schrijf dat deel als decimaal.
- **Antwoord:** 0,6 (accept: 0,6 / 0.6 / 0,60)
- **Hint:** Procent naar decimaal: deel door 100 (komma twee plaatsen naar links).
- **Sterkere hint:** 60% = 60/100 = 0,60. Zo kort mogelijk: 0,6.
- **Fout-hints:** 60 → Je hebt het percentage overgenomen; maak er een decimaal van. · 6 → Komma te ver naar links (of te weinig nullen). · 0,06 → Komma één plaats te ver; 60% = 0,60.
- **Ouderzin:** Je kind zet 60% om naar het decimaal 0,6.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** midden

## 008 · kritisch · multi · bron: breuk-kommagetal-en-procent-omrekenen (herschreven multi)
- **Opgave:**
  1. Schrijf 2:5 (deel:geheel) als breuk.
  2. Schrijf datzelfde deel als procent.
  3. Schrijf datzelfde deel als decimaal.
- **Antwoord:** 1) 2/5 · 2) 40% (accept: 40% / 40) · 3) 0,4 (accept: 0,4 / 0.4 / 0,40)
- **Hint:** Stap 1: deel over geheel. Stap 2: … van 100. Stap 3: procent ÷ 100 (komma twee plaatsen).
- **Sterkere hint:** 2:5 = 2/5 = 40% = 0,4.
- **Fout-hints:** Stap 1 → 5/2 → Deel:geheel omdraaien geeft 5/2; het is 2/5. · Stap 2 → 5% of 25% → Noemer ≠ procent; 2/5 van 100 = 40. · Stap 3 → 0,04 of 4 → 40% = 0,40 = 0,4 (komma twee plaatsen).
- **Ouderzin:** Je kind zet 2:5 om naar breuk, procent en decimaal.
- **Getallenruimte:** koppeltabel breuk/%/verhouding/decimaal
- **Context:** midden
