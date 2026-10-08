# G7-VBN-01 — Tabellen aflezen (Claude-pilot)

Status: concept (parallel naast Didactiek-af; geen overwrite/merge zonder Overzicht)
Bron: Claude-pilot (Kwaliteit-tranche 6, 2026-09-18) — Nog geen Didactiek-gate. Bord=Tabellen/Grafieken; scope kan afwijken van canonieke VBN — geen merge. Zie reviews/claude-tranche6-2026-09-18.md.
Leerdoel-ID: G7-VBN-01
Groep: 7
Bron-slug: tabellen-en-staafdiagrammen-lezen (Claude = 159× “Hoeveel X?” zonder tabeldata in tekst · 80 tabel / 79 staaf-beeld; batch: kern = tabel in opgave · 1× staaf-brug · geen coördinaten/MEET-05)

## 001 · basis · kale · bron: var-tabel-g7-0001 (herschreven + tabeldata)
- **Opgave:** Tabel fruitverkoop (stuks):
  ```
         Ma   Di   Wo
  Appels  24   18   30
  Peren   16   22   14
  ```
  Hoeveel peren zijn er op dinsdag verkocht?
- **Antwoord:** 22
- **Hint:** Zoek de rij Peren en de kolom Di. Lees het getal op het kruispunt.
- **Sterkere hint:** Rij Peren → Ma 16, Di 22, Wo 14. Dus dinsdag = 22.
- **Fout-hints:** 18 → Dat is appels op dinsdag (andere rij). · 16 → Dat is peren op maandag (andere kolom). · 52 → Dat is het rijtotaal van peren; de vraag vraagt alleen dinsdag.
- **Ouderzin:** Je kind leest in een fruittabel de cel peren–dinsdag (22).
- **Getallenruimte:** tabel aflezen (cel)
- **Context:** laag

## 002 · basis · invullen · bron: var-tabel-g7-0002 (herschreven + tabeldata)
- **Opgave:** Zelfde fruittabel:
  ```
         Ma   Di   Wo
  Appels  24   18   30
  Peren   16   22   14
  ```
  Vul in: hoeveel appels zijn er in totaal verkocht? ___
- **Antwoord:** 72
- **Hint:** Tel alle getallen in de rij Appels bij elkaar op.
- **Sterkere hint:** 24 + 18 + 30. Stap voor stap: 24 + 18 = 42, plus 30 = …
- **Fout-hints:** 30 → Dat is alleen woensdag (grootste dag), niet het totaal. · 52 → Dat is het totaal van peren, niet van appels. · 42 → Je bent gestopt na Ma+Di; tel Wo erbij.
- **Ouderzin:** Je kind telt de rij appels op tot een weektotaal (72).
- **Getallenruimte:** tabel (rijtotaal)
- **Context:** laag

## 003 · basis · invullen · bron: var-tabel-g7-0003 (herschreven + tabeldata)
- **Opgave:** Zelfde fruittabel. Vul in: hoeveel peren meer op dinsdag dan op woensdag? ___
- **Antwoord:** 8
- **Hint:** Lees beide cellen en trek het kleinere van het grotere af.
- **Sterkere hint:** Dinsdag peren = 22, woensdag = 14. Verschil: 22 − 14.
- **Fout-hints:** 22 → Dat is alleen dinsdag; je moet het verschil met woensdag nemen. · 14 → Dat is alleen woensdag. · 6 → Verkeerd verschil; check 22 − 14.
- **Ouderzin:** Je kind berekent het verschil peren di−wo (8) uit de tabel.
- **Getallenruimte:** tabel (verschil twee cellen)
- **Context:** laag

## 004 · toepassen · meerkeuze · bron: tabellen-en-staafdiagrammen-lezen (herschreven max-dag)
- **Opgave:** Tabel huisdieren bij de dierenarts (aantal bezoeken):
  ```
          Ma   Di   Wo   Do
  Honden   12   20   15   18
  Katten   16   14   22   10
  ```
  Op welke dag kwamen de meeste honden?
- **Antwoord:** B
- **Opties:** A) Maandag · B) Dinsdag · C) Woensdag · D) Donderdag
- **Hint:** Kijk alleen naar de rij Honden. Welke kolom heeft het grootste getal?
- **Sterkere hint:** Honden: 12 · 20 · 15 · 18. Het grootste is 20 → dinsdag.
- **Fout-hints:** A → 12 is juist het kleinst bij honden. · C → 15 is midden; 22 is katten op woensdag (andere rij). · D → 18 is minder dan 20.
- **Ouderzin:** Je kind zoekt in de rij honden de dag met het hoogste getal (dinsdag).
- **Getallenruimte:** tabel (maximum in rij)
- **Context:** midden

## 005 · toepassen · meerkeuze · bron: var-staaf-g7-0007 (brug staaf)
- **Opgave:** In een staafdiagram over fruit: bananen = 50, peren = 20, druiven = 80. Hoeveel bananen zijn er meer dan peren?
- **Antwoord:** A
- **Opties:** A) 30 · B) 50 · C) 20 · D) 70
- **Hint:** Trek het kleinere aantal van het grotere af.
- **Sterkere hint:** Bananen 50 minus peren 20.
- **Fout-hints:** B → 50 is het aantal bananen zelf, niet het verschil. · C → 20 is alleen peren. · D → Je hebt 50 + 20 gedaan; bij ‘meer dan’ trek je af.
- **Ouderzin:** Je kind leest twee staven en berekent het verschil bananen−peren (30).
- **Getallenruimte:** staafdiagram (brug; verschil)
- **Context:** midden

## 006 · toepassen · verhaal · bron: var-tabel-g7-0071 (herschreven + tabeldata)
- **Opgave:** De bibliotheek houdt bij hoeveel boeken er per dag uitgaan:
  ```
               Ma   Di   Wo   Do
  Strips       12    8   15   10
  Informatief   9   14   11    7
  ```
  Lisa vraagt: op welke dag gingen er in totaal de meeste boeken mee naar huis?
- **Antwoord:** woensdag (accept: woensdag / Wo / wo)
- **Hint:** Tel per dag strips + informatief. Vergelijk daarna de vier totalen.
- **Sterkere hint:** Ma 12+9=21 · Di 8+14=22 · Wo 15+11=26 · Do 10+7=17. Welke dag is het hoogst?
- **Fout-hints:** dinsdag → Di is 22; woensdag is hoger (26). · maandag → 21 is niet het hoogst. · donderdag → 17 is juist het laagst; 15 is alleen strips op woensdag, niet het dagtotaal.
- **Ouderzin:** Je kind telt per dag twee rijen op en kiest de topdag (woensdag).
- **Getallenruimte:** tabel (kolomtotaal + vergelijken)
- **Context:** midden

## 007 · toepassen · verhaal · bron: var-tabel-g7-0021 (herschreven + tabeldata)
- **Opgave:** De sportclub telt leden:
  ```
           Jongens  Meisjes
  Voetbal     28       12
  Hockey      15       22
  Tennis       9       18
  ```
  Hoeveel meer meisjes dan jongens doen aan hockey?
- **Antwoord:** 7
- **Hint:** Lees in de rij Hockey beide getallen en trek af.
- **Sterkere hint:** Hockey: meisjes 22, jongens 15. Verschil: 22 − 15.
- **Fout-hints:** 22 → Dat is alleen het aantal meisjes; de vraag vraagt het verschil. · 15 → Dat is alleen jongens. · 13 → Verkeerd verschil (misschien voetbal 28−15); blijf in de rij Hockey.
- **Ouderzin:** Je kind leest de hockey-rij en berekent meisjes−jongens (7).
- **Getallenruimte:** tabel (verschil in rij)
- **Context:** midden

## 008 · kritisch · multi · bron: tabellen-en-staafdiagrammen-lezen (herschreven multi)
- **Opgave:** Tabel museumbezoekers:
  ```
        Jan   Feb   Mrt
  Kind   40    35    55
  Volw.  80    60    85
  ```
  1. Hoeveel kinderen in februari?
  2. Hoeveel meer volwassenen in maart dan in januari?
  3. Hoeveel bezoekers in totaal in januari (kind + volw.)?
- **Antwoord:** 1) 35 · 2) 5 · 3) 120
- **Hint:** Stap 1: cel kind–feb. Stap 2: volw. mrt minus volw. jan. Stap 3: tel de januari-kolom op.
- **Sterkere hint:** Stap 1: kind-rij, feb = 35. Stap 2: 85 − 80 = 5. Stap 3: 40 + 80 = 120.
- **Fout-hints:** Stap 1 → 60 → Dat is volwassenen in feb (andere rij). · Stap 2 → 85 → Dat is alleen maart; je moet aftrekken van januari (80). · Stap 3 → 40 → Alleen kinderen; tel volwassenen erbij.
- **Ouderzin:** Je kind koppelt cel-aflezen, verschil en kolomtotaal in één museumtabel.
- **Getallenruimte:** tabel (cel + verschil + kolomtotaal)
- **Context:** midden
