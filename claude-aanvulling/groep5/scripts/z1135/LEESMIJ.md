# Z-#1135 'een nul te veel' — PATCH COPY (niet geplaatst) op ae59b04 (main)
- zet_z1135.py (13 entryregels): 175 plekken (GET-E07 17, MEET-E01 112, MEET-E04 22, MEET-E05 24) → 0.
  MEET: «Dat is te groot. Hoeveel keer zo klein is een centimeter als een meter?» (groot → klein) / «Dat is te groot|te klein. Hoeveel keer zo groot is een
  meter als een centimeter?» (MEET-E01 #2, cm → m); de methodezin erachter blijft. GET-E07 #5/#9: «Dat is te veel. Tel de nullen in de som nog eens: hoeveel horen er achter je antwoord?»
- Niet aangeraakt: 'nul vergeten' «er mist een nul» (9 entryregels, 81 items; het kind is een nul vergeten) en GET-E07 #22 «Tel de nullen van het ronde getal goed mee.».
- z1091/GET-E07/snap.json ververst: alleen GET-E07 #5/#9 'nul te veel' en 'te veel'.
- check_z1135.py (nul, richting per sleutel, eenheden per item uit de opgave, kijkzin, SNAP + 'nul vergeten' ongewijzigd), 6 mutanten.
- G8 (alleen voorstel, niet gewijzigd): zie het rapport (Oef-#1069).
