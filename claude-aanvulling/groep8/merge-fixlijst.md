# G8 merge-fixlijst

Aangemaakt door Oefeningen (8 okt 2026) voor G8 hints batch 1 (er was nog geen G8-fixlijst). Elk team schrijft in een eigen sectie. Nummering Oefeningen: Oef-#NNN (gedeelde reeks met G4/G7; Oef-#460–#463 in g4, #464–#466 in g7).

## Oefeningen: G8 batch 1 (GET-E02, GET-E03, GET-E04), 8 okt

| # | Voor | Wat | Status |
|---|---|---|---|
| Oef-#467 | Overzicht (data) | GET-E02 meerkeuze #5/#9 (nrO 54/57): juisteOptie A in 27 van 27 items (alle meerkeuze in E02: A 43 · B 15 · C 15 van 73). husselen staat aan, maar de G8-regel 'geen letter > 45%' faalt in de data. | **✓ Overzicht 15:17 (build 15:17:54):** build_g8.py (blok Oef-#467, na het ontdubbelen): per kop (× en +) op claudeId gesorteerd en om de beurt op A/B/C; de andere opties houden hun volgorde, letters en optiesTekst opnieuw, log 'Oef-#467' in licentie.wijzigingen. #5 (nrO 54) A 7 · B 6 · C 6, #9 (nrO 57) A 3 · B 3 · C 2; alle meerkeuze GET-E02 A 26 · B 24 · C 23 van 73. 17 items andere volgorde, geen opgave/antwoord/kop veranderd. Sleutels op de optietekst, dus ongewijzigd; sync/apply in de build gedraaid. |
| Oef-#468 | Overzicht (data, les 129/232) | GET-E02 open schatten: verkeerd afronden (de omgedraaide regel of één getal de verkeerde kant op) geeft toch het antwoord: #2 24 van 30, #6 9, #7 6, #3 5, #8 4, #4 3. | open |
| Oef-#469 | Overzicht (data, les 195) | GET-E02 #1 (laatste cijfer van a × b): 6 items waar een foute route het goede antwoord geeft: begincijfer = eindcijfer bij 19 × 17, 42 × 6, 49 × 7, 119 × 27, 147 × 35; plus = keer (eindcijfer) bij 112 × 12. | open |
| Oef-#470 | Didactiek/Overzicht | GET-E04 #3: 4 van 6 antwoorden zijn vereenvoudigd (2/6, 3/15, 3/12, 2/12 als niet-eenvoudige vorm) zonder geldigeAntwoorden. Is 'zo eenvoudig mogelijk' een eis (dan in de vraag zetten), of tellen gelijkwaardige breuken als goed? | open |
| Oef-#471 | Overzicht (data, les 147) | Vreemde contexten: GET-E02 #8 (schelpen in een nest, stenen in huis, pakken in de klas …), #11 ('dozen met elk 497 tanden'). | open |
| Oef-#472 | Overzicht/Leerlijn (koppen) | Koppen zonder 'kan'/'ongeveer' en met '[ding]' (zoals G4 Oef-#463). | open |
| Oef-#473 | Overzicht (data, les 206/231) | GET-E02 #5/#9: in meerdere items ligt de vijf-of-meer-schatting dichter bij een afleider dan bij het antwoord; de hints sturen daarom niet naar schatten maar naar eindcijfer + grenzen. | open |
| Oef-#474 | Overzicht (motor) | Geen regel voor 'half afgerond' (één getal afgerond); 'fout = antwoord + 1' maakt geen sleutel als de waarde ook in de vraag staat (E04 #5/#8, opgevangen met Claudes label 'een-ernaast'). | **uitgesteld (Overzicht 15:18), niet veilig in deze ronde:** fout_regels.py is byte-gelijk in G5–G8; een nieuwe regel moet achter een eigen vlag die alleen apply_hints van G8 aanzet (niet KOMMA437, want die staat ook in G7 aan). (1) 'half afgerond': nodig is een spec van Oefeningen: welk getal (getal1 / getal2 / beide varianten als twee sleutels), en vóór of na 'precies uitgerekend'? (2) '+ 1 in de vraag': die sleutel wordt bewust onderdrukt (#390, les 115: een overgenomen getal uit de vraag is geen 'Bijna'). Dat opheffen alleen voor G8 E04 #5/#8 kan met dezelfde vlag, maar Claudes label 'een-ernaast' vangt het nu al op. Voorstel: regel 'fout = getal1 half afgerond / getal2 half afgerond' + vlag G8_474; daarna motor_regressie G5–G7 = 0 als gate. |
| Oef-#475 | Overzicht/Leerlijn | GET-E02 #3 en #10 zijn dezelfde opgavevorm in twee somtypes. | open |

## Oefeningen: G8 batch 2 (GET-E02 #12–#36), 8 okt

| # | Voor | Wat | Status |
|---|---|---|---|
| Oef-#476 | Overzicht (data, les 195) | GET-E02 #32 (nrO 25, «15 procent van 40 leerlingen»): de afleider 'Deel 15 door 100 en doe dat keer 40 procent' geeft hetzelfde getal (6) als het antwoord; alleen het woord 'procent' maakt hem fout. Een kind dat goed rekent, kan hem terecht goed vinden. Voorstel: een afleider met een ander getal (bijv. 'Deel 40 door 15'). De hint wijst nu op het woord procent. | open |
| Oef-#477 | Overzicht (data) | Afleiders zonder Claude-label (claudeDenkfout leeg): GET-E02 #21 (nrO 14) 'De jas kost nu €35' en #26 (nrO 19) 'De som nog een keer precies zo uitrekenen'. €35 = €60 − 25: het procent als euro's afgetrokken (een echte route; de hint noemt 'het procent is geen bedrag in euro'). Het goede nieuwe bedrag (€45) staat niet in de opties. | open |
| Oef-#478 | Overzicht/Leerlijn (koppen, zoals Oef-#472) | '[ding]' op de plek van een werkwoord: #20 'nu €# [ding]' (kost), #21 '€# [ding] # procent' (gaat) en 'nu €# [ding]' (kost), #26 '= # [ding]' (uitgerekend), #32 'In groep # [ding] # [ding]' (zitten, leerlingen). | open |
| Oef-#479 | Overzicht/Leerlijn | GET-E02 #12–#36: 25 somtypes met elk één item, tekstopties met getallen. De hints zijn per item: elke foute optie heeft een letterlijke regel (de hele optietekst). Komt er een item bij, dan vallen de foute opties op 'andere fout' (b2/check WARN), en teksten die op het item leunen, kloppen misschien niet meer: #20 'deelbaar door #' (alleen de tafel van vijf), #26 (gram onder de duizend), #27 (naar één uur), #11 (tegels van één vierkante meter), #6 (antwoord van Bas boven de honderd euro), #15 (twee keer zoveel personen). check.py bewaakt die feiten (data-guards, mutanten M_d9/M_d20/M_d26/M_d27). | open |
| Oef-#480 | Overzicht (data) | GET-E02 #29 (nrO 22): de kop zegt «In een grafiek staat de temperatuur per dag» (zonder beeld), het antwoord en de afleiders gaan over een staaf. Temperatuur per dag staat meestal in een lijngrafiek; 'staafgrafiek' in de kop maakt het eenduidig (zoals #30). | open |

Meerkeuze-spreiding batch 2: het goede antwoord staat op plek A 9 · B 10 · C 6 van 25 (36 %, onder de 45 %); husselen staat bij alle 25 aan.

Nummering: volgende vrije Oef-#481.

Na build 15:17:54 (Overzicht, 8 okt): batch1.json (24 somtypes, 317 items) gesynct en toegepast: check_hints **24 klaar · 199 open · 0 FAIL · 0 WARN**, check_merge_notatie ALLES OK, g8work/b1/check.py op live 317 items · 1304 sleutels · FAIL 0 · WARN 0 · INFO 112. batch2.json (Oefeningen, 15:14, nog niet gemeld) is bewust buiten deze build gehouden en ongewijzigd teruggezet (geen sync). De volgende build_g8.py neemt hem wél mee.
De build schrijft ook g4–g7/data/aanvulling_uit_g8.json: de items waren gelijk (alleen de tijdstempel anders), dus de oude bestanden zijn teruggezet. G4–G7 zijn niet geraakt.
Oef-#468, #469, #471, #473 (data GET-E02) en #475 (dubbele vorm #3/#10) staan nog open voor een volgende G8-dataronde. #470 is een vraag voor Didactiek ('zo eenvoudig mogelijk' als eis of gelijkwaardige breuken goed). #472 (koppen met 'kan'/'ongeveer', zonder '[ding]') gaat samen met G4 Z-#726: de kop-generator maakt van 'kan' een '[ding]' («Welk antwoord bij # × # [ding] kloppen?»).
