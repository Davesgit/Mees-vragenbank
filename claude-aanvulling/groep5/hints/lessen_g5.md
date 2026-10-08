# Lessen G5 (Didactiek, review-batch7-didactiek.md, 1 okt; ze gelden voor alle groepen)
Nummering van Didactiek (80–89). De lessen 1–67 staan in `g6/hints/lessen_batch2.md`.

80. **Een contextwoord in een hint past bij elk item,** of het nu om mensen of om dingen gaat (ding, ieder, iedereen, kinderen). Kijk per item van het somtype (#303, #304).
81. **De G5-grens (tot 1000) geldt ook voor de afleiders** die getoond worden, niet alleen voor de opgave en het antwoord (#302).
82. **Een schatitem komt niet goed uit als je op de verkeerde plaats afrondt.** Reken de uitkomst ook na met de andere afrondplaats (#301).
83. **Bij wisselgeld verschillen de kosten en het wisselgeld.** Anders is 'wat het kost' een foute route met het goede antwoord (#301).
84. **Een staphint noemt de grootste plaatswaarde die in de items voorkomt** (honderdtallen, tientallen, eenheden) (#305).
85. **'Ongeveer' gaat over de schatting, niet over de situatie.** Beschrijf de situatie in een hint feitelijk (#306).
86. **Betaal met het kleinste realistische briefje,** of één stap groter (#323).
87. **Bepaal het niveau op het aantal cijfers en op lenen of overschrijden,** en doe dat in elk somtype hetzelfde (#327).
88. **Elk open geld-item krijgt geldInvoer,** ook als het uit een andere groep komt (#300).
89. **Verwijs naar items met hun id.** `nr` is na het overnemen niet uniek per doel; ook het somtypenummer verschilt (data-somtype ↔ nrOrigineel) (#329).

## Lessen 100–104 (Didactiek recheck-ronde7b, G5 ronde 7c/9)
100. **Een algemene hint met een voorzetsel ('bij elk') moet passen bij het voorzetsel en werkwoord in álle opgaven** (in, op, krijgt). Twijfel je, kies dan een zin zonder voorzetsel, zoals «Overal komt evenveel» (#350).
101. **Een check op een verboden zin toetst het patroon,** een uitspraak over wat het kind deed, en niet alleen de letterlijke zin ('een stuk vergeten' én 'iets vergeten', #351).
102. **Een voorwaardelijke stap («als het … die heeft») noemt welk getal je bedoelt** (#352).
103. **Haal je een benoemde fout tijdelijk weg omdat een sleutel botst met een getal uit de vraag, zet dan een terugzet-actie vast bij dat datapunt** (#353 bij #325; teruggezet in ronde 9).
104. **Een build-stempel moet ook een hint-sync laten zien** (`hintsSyncOp`, `hintsBatches`, #355). Anders lijkt een recheck op 'dezelfde build' te gebeuren terwijl de teksten veranderd zijn.


## Lessen 105–109 (Didactiek gate ronde 9, G5)
105. **Een generator die een sjabloonitem kopieert, kopieert ook velden die van het antwoord afhangen** (`geldigeAntwoorden`). Leid elk zo'n veld opnieuw af, en laat een guard 'antwoord ∈ geldigeAntwoorden' de build stoppen (#360).
106. **Krijgt een item nieuwe getallen, dan gaat de herreken-guard over álle velden die het antwoord bevatten** (antwoord, geldigeAntwoorden, juisteOptieTekst, sleutels), niet alleen `antwoord`.
107. **Herschrijf je een opgave, loop dan ook de ouderzin en het somtype-label na.** Die staan in een ander bestand (de hint-entry of het label) en worden anders vergeten (#362: 'tabel').
108. **Elke uitzondering op een guard krijgt een geschreven reden** ('alleen GET', 'Meten tot 9000' #60). Zonder reden blijft dezelfde fout in een ander doel staan (#361).
109. **Wat je in een zelfcheck vindt, krijgt meteen een nummer in de fixlijst** (#364 stond zonder nummer in `review-batch7.md`).

*Lessen 90–99, 110–119 (G6) staan in `g6/hints/lessen_batch2.md`.*

## Lessen 120–124 (Didactiek recheck ronde 9 G5, builds 11:20:45 en 11:31:53; in ronde 10b toegepast)
120. **Toets een gedeeld tekstvoorstel per bewerking (+, −, ×).** «Rond beide getallen af» past bij plus en min, maar niet bij een keersom waarin je één getal afrondt (D-#403).
121. **Een guard die 'ongebruikte' regels weghaalt, moet het itemtype kennen.** Bij meerkeuze is een regel zonder optie dood; bij een open vraag vangt een bereikregel ('te veel', 'te weinig') juist elk getypt antwoord op.
122. **Verplaatst de motor een sleutel naar een andere soort, dan verhuizen de matchwaarden mee** (`foutRegels.match.waarden`). Kijk ook of het label waarop hij terugvalt feitelijk klopt.
123. **Een los-scan zoekt ook 'dan' en 'daarna' in de eerste zin**, niet alleen een zin die met 'Dan' begint. Draai hem over alle terugval-sleutels (`g6work/r10/los_l2.py`, D-#407).
124. **Elk team gebruikt zijn eigen nummerreeks**, ook voor een eigen vondst in de fixlijst. Oefeningen: Oef-#NNN onder #500; Didactiek: #500 en hoger.
