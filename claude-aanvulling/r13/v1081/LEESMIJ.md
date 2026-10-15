# V-#1081 andere kant (Oefeningen 15 okt) — voorwaardelijke hook voor het kritisch concept L-R10b, NIET geplaatst

Bron (alleen gelezen): /workspace/claude-merge/r13/kritisch_concept_g6.json (md5 3c46f7c2). Uitvoer: uit.json (kopie).
`python3 zet_andere_kant.py <concept.json> <uit.json>` → `python3 check_andere_kant.py <uit.json> [<origineel>]` → `./mutrun_andere_kant.sh <uit.json>` (8 mutanten).

- G6-GET-E04 #1 (afleiders hoog): laag = bij het lenen twee keer afgehaald bij het cijfer waar je van leent (goed − 10^(kolom+1)).
  L1: «Dat is te weinig. Kijk naar het cijfer waar je van leent: hoeveel gaat daar af? Reken na: jouw uitkomst plus het getal dat je eraf haalt, moet het getal zijn waar je vanaf haalt.»
- G6-MEET-E03 #2 (afleiders hoog): laag = in de tafel van de bekende zijde één stap te vroeg gestopt (goed − 1).
  L1: «Dat is te weinig. Tel nog eens in de tafel van de bekende zijde. Reken na: jouw zijde keer de bekende zijde moet precies de oppervlakte zijn.»
- G6-VERH-E02 #2 (afleiders laag): hoog = keer de teller, niet door de noemer gedeeld (aantal × teller).
  L1: «Dat is te veel: dat zijn meer koekjes dan er zijn. Verdeel de koekjes eerst in gelijke groepjes; de noemer zegt hoeveel groepjes.»
Per somtype gezet in 2 van de 4 items (eerste ware + eerste foute): rang 2× midden + 2× rand. In alle 4 = 4× midden = FAIL (mutant M_rang).
Bewering, antwoord, letters van goed en Ja blijven gelijk; vervangen wordt een Nee-afleider (fout item: de andere fout; waar item: de verste).
