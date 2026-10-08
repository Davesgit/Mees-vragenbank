# Twijfels batch 4 (MEET-E06, VBN-E01, VERH-E01). Oefeningen, 2026-10-01 15:36 (Amsterdam)

1. **De klok (MEET-E06, 15 somtypes): één vaste tekst per soort klok.**
   - Claudes tekst is overal dezelfde: 'Kijk eerst naar de kleine wijzer … Dan de grote wijzer: hoeveel minuten daarna?' (412 sleutels). 'Minuten' is geen G4-stof bij half en kwart. Daarom is die tekst vervangen.
   - fout_regels kent geen regel voor half of kwart. Een foute klok kan dus niet apart worden opgevangen als 'een uur te laat' (bij half vier de klok op half vijf) of als 'grote wijzer verkeerd'. Elke foute klok krijgt daarom de tekst 'andere klok', en die tekst noemt allebei de wijzers.
   - Voorstel aan Overzicht: merge-punt #38.
2. **Digitale tijd (#12–#17) noemt minuten** ('Achter de dubbele punt staat hoeveel minuten …'). Dat kan niet anders bij '1:30'.
   - Bij #12–#14 hebben de foute klokken soms '1:06', '1:03' of '2:09': de grote wijzer staat dan op 6, 3 of 9 minuten. Dat zijn geen G4-tijden. Zie #39.
3. **Klok zetten (#8, #10): Claudes teksten per item blijven** ('"half twaalf" is nog vóór twaalf uur. …'). Ze zijn goed. Er zijn twee kleine punten, maar een taalfix per item kan niet:
   - bij 071 en bij 'half één' staat 'vóór een uur' in plaats van 'vóór één uur';
   - de aanhalingstekens zijn dubbel.
   - Bij #9 is 'De kleine wijzer wijst naar de 7.' vervangen, want bij kwart over staat de kleine wijzer net voorbij het uur.
4. **Kalender (#3, #4): één vaste tekst.**
   - Claudes teksten zijn vervangen: 'maandgrens' en 'Je bent bijna klaar, …' zijn te vaag.
   - Alle 54 items gaan over het eind of het begin van de maand heen. Daarom kan de hint dat zeggen.
   - Er is geen regel voor datums (bijvoorbeeld 'gestopt bij de laatste dag van de maand' of 'een dag ernaast'). Zie #41.
5. **VBN-E01, tabel (#1–#3): één vaste tekst per somtype.** De foute opties zijn een andere cel, de som van een rij, de som van een kolom, of de som of het verschil van twee cellen.
   - Claudes 'Je hebt het andere stuk uitgerekend' klopt niet: het kind heeft opgeteld.
   - Er zijn geen regels die met de tabel rekenen. Zie #42.
   - De 'bijna'-regel (± 1 of 2) is weggelaten. Bij #2 en #3 vangt hij alleen toevallige getallen, bijvoorbeeld de som van een andere rij.
6. **VBN-E01, staafdiagram (#4, #5):**
   - 'één streepje te veel/te weinig' gebruikt de regel 'antwoord ± getal1'; getal1 is 2, uit 'Elk streepje is 2.'.
   - 'Streepjes geteld' (het antwoord is de helft) komt 27 keer voor bij #4 en 22 keer bij #5. Daar bestaat geen regel voor, dus het staat in de tekst van 'andere fout'. Zie #40.
   - De hints zeggen 'twee' in woorden en niet als cijfer, zodat de checker geen WARN geeft. Didactiek schreef 'Spring dan verder met 2'.
7. **VERH-E01:** dit somtype heeft maar 1 item. Claudes twee teksten blijven per item. Zie #44.
8. **MEET-E05 '(1 kg)':** dit staat er op verzoek van Didactiek (batch 3b). check_hints geeft 2 WARN ('getal 1 in de hint'). In MEET-E05 is 1 nergens het antwoord: de antwoorden zijn '30 kg' en 'Een pak suiker'. Het is dus een vals alarm, maar de checker is niet van mij. Een alternatief zonder cijfer is 'één kilo (kg)'.
