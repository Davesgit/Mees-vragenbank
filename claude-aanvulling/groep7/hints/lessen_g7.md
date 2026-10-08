# Lessen G7 (Oefeningen)

Dit bestand begint bij les 144. Alle eerdere lessen gelden ook voor G7:
- lessen 1–119, 125–140 en 150–155: `/workspace/claude-merge/g6/hints/lessen_batch2.md`;
- lessen 120–124 en 135–140 en 150–155: `/workspace/claude-merge/g5/hints/lessen_g5.md`.
De nummers volgen die van Didactiek (G7 review batch 1, `g7/review-batch1-didactiek.md`).

## Lessen 144–149 (Didactiek review G7 batch 1, 8 okt; in ronde 1b toegepast)
144. **Test H1 en H2 met de opties ernaast.** Blijft er zonder rekenen maar één optie over, dan geeft de hint het antwoord weg. Bij 'welke tekening/som' is het begrip uitleggen al het antwoord: laat H2 de situatie uitrekenen en elke optie narekenen. Toets: `g7work/b1b/verklap.py` (kenmerken uit H1 en H1+H2 tegen de opties; een woord dat letterlijk in de vraag staat, telt niet; de oude teksten van DENK-02 #3/#4/#8/#9/#10 vallen erop door, de nieuwe niet).
145. **Reken bij een som in twee stappen ook de denkfouten samen na** (de foute bewerking én de tweede stap vergeten). Kleine getallen geven toevallige treffers op het goede antwoord (3 + 2 = 5 = 3 × 2 − 1; 2⁴ = 4 × 4).
146. **Kan één afleider uit meer dan één route komen, dan past laag 1 bij elke route** (12 = 3 × 4 = 3 + 4 + 5; 10 = het streepje = 20 − 10). Schrijf alle routes op, of kies getallen waarbij de routes uit elkaar gaan (datapunt voor Overzicht).
147. **Bij één item per somtype zet je de woorden van het item vast met een vlag en een guard.** `"contextgebonden": {"woorden": […], "aanname": "…"}` in de entry; de guard (`g7work/b1/check.py` + `g7work/b1b/context.py`) eist één item per gevlagde entry, elk vlagwoord in de opgave, en elk woord uit de opgave dat niet vast in de kop staat, in de vlag. Let het meest op een [ding] die het begrip zelf is ('omtrek').
148. **Zeg pas 'geen route' na een vast rijtje:** een stap of dag vergeten, de groei maar één keer, 'meer dan de eerste' in plaats van 'meer dan de vorige', verwisseld, alles opgeteld. Bij '11 dl' gaf dat twee routes.
149. **Toets een context ook op de verpakking** (pak, kan, doos, flesje): 'een pak sap van 2 liter', 'een kan met 6 liter' en 'een eierdoos van 8' kloppen niet met de referentiematen. En: hebben de live data de hints nog niet, review dan de gesyncte en toegepaste stand in een zandbak, en schrijf de build erbij.
