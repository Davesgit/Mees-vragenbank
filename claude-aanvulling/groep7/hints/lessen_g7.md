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

## O1. Begripsvraag 'Hoe heet …?': H2 noemt de familie van namen, niet welke plek welke naam heeft (G7 batch 2, DENK-04; eigen les van Oefeningen, eerst als '156' genummerd, nu O1 omdat Didactiek 156–165 heeft)
Bij 'Hoe heet de 8 in 130 − 8 = 122?' is de koppeling plek → naam het antwoord zelf. H1 laat het kind de plek zoeken (vooraan, achter het teken,
achter het isgelijkteken); H2 zegt welke namen bij deze somsoort horen en welke bij een andere ('Bij een minsom horen de namen aftrektal,
aftrekker en verschil. Term en som horen bij een plussom.'). Dan blijven er twee opties over en moet het kind nog kiezen (les 144). De volledige
koppeling staat pas in laag 2 van een fout-hint, na twee foute keuzes. Geen naam met lidwoord in H2 ('de som'): check_hints ziet dat als het
antwoord van een ander item.

## O2. Een nieuwe batch kan gesynct zijn voordat je eigen checks klaar zijn (G7 batch 2; eigen les van Oefeningen, eerst '157', nu O2)
De build van Overzicht nam batch2.json mee (sync: koppeling) terwijl de eerste versie nog in de checks zat. Vanaf dat moment nooit meer
make_batchN.py --force: de verbeteringen van na de sync staan als 'Ronde 1a' in patch_batchN.py, met een diff tegen de make-uitvoer
(0 verschil) als bewijs dat er niets verloren ging.

## Lessen 156–165 (Didactiek: G5/G6 eindcheck r11b en G7 recheck batch 1, 8 okt)
- **156.** Een regel die je in een entry zet, geldt voor elk item van het somtype, niet alleen voor de gemelde sleutels. Tel na de build hoeveel sleutels hij echt maakt (G5: 3 gemeld, 482 gemaakt) en lees de tekst tegen alle items.
- **157.** Een guard die vaste items pint, beschermt alleen die items. Hangt een tekst af van een voorwaarde, laat de guard die voorwaarde dan bij elke sleutel narekenen. Test dat met een mutant op een ander item.
- **158.** Toets een check op een verboden bewering ook met omschrijvingen: een andere zinsgrens, synoniemen, een afgekorte vorm. Niet alleen met de letterlijke zin waar de fout ooit stond. (G7: de kleur-guard in b1/check vangt 'gekleurd', 'kleur er één', 'rode'.)
- **159.** Een zelftest die stil overslaat als zijn tabel ontbreekt, is geen test. Laat hem melden dat hij niet gedraaid heeft.
- **160.** Een routetool vindt combinaties van getallen, geen denkfouten. Vraag bij elke melding eerst 'doet een kind van groep 7 dit echt?', voordat je een tekst herschrijft. Anders wordt een gerichte tekst vaag voor een route die niemand neemt (G7 ronde 1c: '4 + 3', '2 × 2', '4 × 4', '3 + 3 × 2' waren artefacten).
- **161.** Een laag 1 die iets zegt over de waarde («Dat is wat er na stap één …») is waar voor elke route naar die waarde: de veiligste vorm bij meerdere echte routes. Een vraag naar de bewerking («Heb je … opgeteld?») is gerichter, maar alleen goed als er één echte route is.
- **162.** Bij procenten is 'een getal uit de vraag = het goede antwoord' voorspelbaar: n van N geeft N% precies als n = N² : 100 (4/20, 9/30, 16/40, 25/50). Zoek bij elk procent-somtype op die vorm, niet alleen op toeval.
- **163.** Een melding 'a × a' of 'getal uit de vraag' op het goede antwoord is pas een probleem als het een fóute route is. Bij 4/25 = 16% (×4) of bij het aflezen van een schaal is het de goede route.
- **164.** Noem bij elke check de stand van de hint-sync én die van de build. De hint-sync kan verder zijn dan de build (batch1.json kwam vier minuten na de build 12:16:26); beoordeel de build en zeg wat er nog niet in zit.
- **165.** Kijk bij een gesplitst somtype naar nrOrigineel én het kopnummer. Het rad van VERH-04 is nrO 7 maar kop 6 in het md-bestand. Leg het nummer vast als nrOrigineel (de hints hangen daaraan), en zeg in elke opdracht welk nummer bedoeld is.

## Lessen 166–170 (Didactiek: G7 review batch 2, build 12:32:32, 8 okt)
- **166.** Vraagt een item 'bij welke stap', dan horen de stapnummers in de vraag («Stap 1: neem 30. Stap 2: …»). Een hint kan een telafspraak die het kind niet kent niet repareren: de fout valt al bij de eerste poging (V-#570, DENK-03 nrO 21).
- **167.** Noem een getal via zijn stap of zijn rol: 'het getal van de min-stap', 'het begingetal', 'het getal dat in die stap staat', 'het getal waar de vraag over gaat'. Niet 'het laatste getal' of 'het getal uit de vraag': bij een bewering (Lisa zegt 20) of een hele som in de vraag wijst dat naar een ander getal (V-#571, Z-#571, Z-#580). Guard: g7work/b2/check.py.
- **168.** 'andere fout' met een tekst voor één route mag als tussenstap, als die route bij elk item nagerekend is en vastgepind met een assert (DENK-04 #5 '8 : 328' tot Oef-#429). Zodra de motorregel er is, verhuizen beide lagen ernaar en krijgt 'andere fout' weer een algemene tekst.
- **169.** Een getal uit de vraag in woorden ('keer twee', 'door twee') is een verkapt cijfer: het klopt voor het item van nu en niet voor het volgende. Maak het algemeen, of vlag het. Vaste getallen mogen wel: verdubbelen = keer twee, dubbel vouwen, duizend meter, stapnamen, de structuur van de kop (twee reeksen, vier stappen). Guard met een lijst nagekeken uitzonderingen: g7work/b2/check.py.
- **170.** Maak 'som' als naam herkenbaar naast minsom en plussom: «de naam som», «De namen term en som horen bij een plussom» (Z-#578). Anders leest «Hoort de som bij een minsom?» als een vraag over de hele som.

## Lessen 171–174 (Didactiek: recheck G7 batch 1 en 2, 8 okt)
- **171.** Lees een zoek-en-vervang van een lange frase daarna terug als zin. Een lange naam ('het getal waar de vraag over gaat') midden in een zin geeft 'gaat … gaat' of een losgeraakt 'aan'. Zet zo'n naam aan het eind van de zin (Z-#588).
- **172.** Een guard met een woordenlijst vangt alleen wat in de lijst staat. Doe de mutatietest ook met een mutant buiten de lijst ('vijfhonderd', 'het getal uit de vraag' buiten DENK-04) en schrijf op welke gaten bewust zijn (Z-#590; g7work/b2/check.py leest nu ook samengestelde getalwoorden).
- **173.** Bij 'n keer verdubbelen of halveren' hoort de lineaire denkfout ('vier keer verdubbelen = keer acht') in het vaste rijtje van les 148. Hij valt vaak samen met 'een keer te weinig' (Z-#585).
- **174.** Een laag 1 die per eenheid redeneert ('hoe vaak past … in één kilometer') neemt aan dat het mooi uitkomt. Behandel dat als een aanname (les 147/169): vlaggen, of laten rekenen met de hele hoeveelheid (Z-#587).

## Lessen 180–185 (Didactiek: review G7 batch 3, builds 12:44:21/12:52:39, 8 okt)
- **180.** Een vraag in laag 1 is ook een bewering over het item: ze veronderstelt dat de stap bestaat. Tel per sleutel in hoeveel items die stap echt bestaat. Is dat een minderheid, schrijf de voorwaarde dan uit: «Kwamen de honderdsten op tien of meer? Dan …, anders niets.» (V-#601)
- **181.** Volg bij een H2 of laag 2 die een algoritme beschrijft het algoritme per item tot het eind: verder lenen over een nul (V-#600), duizendsten (V-#604), een nul bijzetten (V-#605), een nul ervoor en slotnullen weg bij omrekenen (batch 4 ronde 1b). Guards: g7work/b3/guards3b.py, g7work/b4/check.py.
- **182.** 'Het middelste getal', 'het bovenste', 'het getal vooraan' en 'de tweede rechthoek' zijn omschrijvingen naar plek. Zeg 'van klein naar groot', 'het grootste' of de rol (V-#606, Z-#600, Z-#602). In een kolomsom blijft 'het bovenste cijfer' de vaste term.
- **183.** Zoek vóór het schrijven naar items zonder het kenmerk van het somtype (tafelsommen zonder komma, een vraag zonder komma bij omrekenen, een bak zonder kommamaat). Die geven teksten die niet passen en uitzonderingen (V-#603). Een regel zonder één sleutel gaat eruit of wordt benoemd als vangnet (Z-#612).
- **184.** Lees in een taalgate ook de opgave zelf: hoofdletter aan het begin, en of [ding] en [wie] samen een vraag maken. De checks op hints zien dat niet (V-#607, V-#608).
- **185.** Hangt een tekst aan lenen of onthouden in één kolom, gebruik dan de voorwaarde die de motor al heeft ('(geleend bij de duizendtallen)') en test de verdeling in een zandbak (V-#602: 10/6).
- **186.** Een terugverwijzing ('dat cijfer', 'die plek') in een stappenplan gaat naar het laatst genoemde woord van die soort. Zijn er twee cijfers genoemd (jouw cijfer, het cijfer ervoor), noem dan voluit welk cijfer je bedoelt. Toets door de verkeerde lezing als algoritme over alle items te draaien (les 181) en tel hoeveel items misgaan (V-#615: 23 items).
- **187.** Een motorregel die een getal uit de vraag teruggeeft, moet het in de notatie van het antwoord geven (€, twee decimalen, eenheid); anders matcht de sleutel nooit en wint een oudere regel. Tel per regel ook «sleutel == verwachte string», niet alleen de waarde (Z-#616).
- **188.** Een tekstguard op een frase is hoofdletterongevoelig, en de mutatietest zet die frase ook aan het begin van een zin (Z-#619).
- **189.** Bij aftrekken met kommagetallen ontstaan de meeste nullen pas bij het aanvullen («zet er nullen achter»): 22 van de 23 gevallen. Een guard op 'lenen bij een nul' rekent met de aangevulde getallen, niet met de getallen zoals ze in de opgave staan (Z-#618).
- **190.** Een vuistregel die alleen onder een voorwaarde klopt ('grotere noemer, kleinere stukken' alleen bij gelijke tellers) verklapt het antwoord in een eenzijdige dataset. Toets op alle items of de regel het antwoord geeft zonder rekenen, en kijk of er tegenvoorbeelden zijn (V-#630).
- **191.** Een laag 1 die een stap aanwijst ('reken de tellers na') moet kloppen voor elke sleutel onder het label. Tel per sleutel welke stap echt fout ging; een labelnaam dekt vaak meer routes (V-#632).
- **192.** Les 181 geldt ook voor breuk → kommagetal (5/100 = 0,05): de guard dekt elk somtype met een komma-algoritme (V-#633).
- **193.** Een guard op plekwoorden toetst het woord zelf (eerste, tweede, laatste, bovenste …), geen vaste zin (V-#634).
- **194.** De build kan tijdens een gate verschuiven. Vergelijk vóór het rapport de items van de batch met de live build en test bij een verschil opnieuw op een verse snapshot.
- **195.** Toevallige treffer: zet ook de som en het verschil van de gegeven getallen tegen het antwoord (2 + 2 = 2 × 2). Met de foute route is het kind dan toch goed.
- **196.** Als een nieuwe build tijdens een recheck verschijnt, vergelijk dan eerst de mtimes van de patchbestanden met de hint-sync. Zijn de patches ouder, dan zitten ze in de build en hoef je niet zelf te syncen. Bevestig het met een motor-replay (0 verschillen) en noem de stand van zowel de build als de hint-sync. (Didactiek recheck-batch3-4, 8 okt 13:50)
- **197.** Lees bij elke 'zoveel …'-zin waar 'zoveel' naar terugwijst. Na «Doe A keer B: zoveel …» wijst het naar het product. Klopt dat niet met wat volgt (lagen in plaats van inhoud), dan leert de tekst een fout begrip, ook als het kind toch het goede getal uitrekent. (Didactiek recheck-batch3-4, 8 okt 13:50)
- **198.** Doe de mutatietest van een guard op een vuistregel ook met een omschrijving van dezelfde regel ('hoe groter de noemer, hoe kleiner …', 'kies de grootste noemer'). Een guard op vaste frasen vangt alleen de frasen die we al kenden (les 193 voor regels in plaats van woorden). (Didactiek recheck-batch3-4, 8 okt 13:50)
- **199.** Tegenvoorbeelden toevoegen is niet genoeg. Tel ook hoe vaak de foute truc nog 'goed' oplevert. Bij meer dan twee derde blijft de truc lonen, ook als geen tekst hem meer noemt. (Didactiek recheck-batch3-4, 8 okt 13:50)
- **200.** Volg een komma-algoritme ook vóór de komma. 'Zoveel cijfers achter de komma' zegt niets over de nul ervoor. Bij antwoorden onder één moet het stappenplan of de app die nul afdekken. (Didactiek recheck-batch3-4, 8 okt 13:50)
- **201.** Een laag die van een zustersomtype is overgenomen, kan in het andere somtype de verkeerde kant op rekenen ('tel ze op' terwijl het totaal gegeven is). Lees elke laag per somtype na met een item ernaast. (Didactiek review-batch5, 8 okt; daar nr. 200)
- **202.** Een labelregel die door een omweg nu niets pakt, wordt actief zodra de motorfix landt. Keur zijn tekst nu al per sleutel. Een check op de waarde vangt een verkeerde instructie niet: toets ook 'volg de tekst: kom je op het antwoord?'. (Didactiek review-batch5, 8 okt; daar nr. 201)
- **203.** Les 181 geldt ook voor procent-stukken: 'tien procent, helft, kwart' maakt geen 5% of 15%. Toets per item of het procent met de genoemde stukken te maken is. (Didactiek review-batch5, 8 okt; daar nr. 202)
- **204.** Een voorbeeld in de vraagzin ('bijvoorbeeld −3') kan bij één item het antwoord zijn. Zet het voorbeeld tegen elk antwoord. (Didactiek review-batch5, 8 okt; daar nr. 203)
- **205.** Bij 'grootste/hoogste' in meerkeuze: controleer de data op gelijke maxima. Een tweede goede optie maakt een afleider goed en zijn laag 1 onwaar. (Didactiek review-batch5, 8 okt; daar nr. 204)
- **206.** Afleiders 'antwoord ± stap' maken de middelste optie altijd goed. Toets ook waar het antwoord op grootte tussen de opties staat (les 190). (Didactiek review-batch5, 8 okt; daar nr. 205)
- **207.** Een voorbeeld in een hint dat gelijk is aan een afleider, stuurt naar die afleider. Leg de voorbeelden uit de hints naast de opties (les 144). (Didactiek review-batch5, 8 okt; daar nr. 206)
- **208.** Referentiematen gelden ook voor temperatuur: binnen is het rond twintig graden, niet onder nul. (Didactiek review-batch5, 8 okt; daar nr. 207)

## Lessen 209–223 (Didactiek recheck-batch4-5 en review-batch6, 8 okt) en 230–232 (Didactiek G4 review-batch5, 8 okt; algemeen)
- **209.** Een guard op een woord ('gelijk') is hoofdletterongevoelig en dekt alle velden die het kind ziet (H1, H2, laag 1, laag 2), met herformuleringen ('hetzelfde', 'evenveel', 'even groot', 'net zo groot'). (recheck-batch4-5)
- **210.** Ook een hint die afleiders uitsluit kan verklappen ('geen plus en geen keer' laat één optie over): tel na H1 + H2 welke opties er overblijven. (recheck-batch4-5)
- **211.** Draai de check op toevallige treffers (les 195) op alle somtypes met dezelfde vraagvorm, ook die met een bedrag. (recheck-batch4-5)
- **212.** Bouw woordlijsten voor guards uit de data of op de stam van het woord (groot/grot-, klein-, hoog/hoger, minder, waard), niet als vaste lijst. (recheck-batch4-5)
- **213.** Verandert de motor voor een andere batch: regressie met de oude en de nieuwe motor op dezelfde items. (recheck-batch4-5)
- **214.** Een notatie-opdracht ('één cijfer achter de komma') werkt in beide richtingen: is '2' fout bij 2,0, dan is '2,00' het ook. (recheck-batch4-5)
- **215.** «Dat getal staat al in de vraag» is onwaar als het antwoord zelf een getal uit de vraag is: zet elk antwoord tegen de getallen uit de vraag (les 162). (review-batch6)
- **216.** Een ±-regel kan samenvallen met de bekende misvatting van het domein (additief bij verhoudingen: b + c − a = antwoord ± b): tel per ±-regel ook de misvattingen na. (review-batch6)
- **217.** Een zin die een bewerking uitsluit ('je telt niets op', 'alleen keer') is ook bij een schaal onwaar: herhaald optellen en kolommen optellen zijn geldige routes. Guard erop. (review-batch6)
- **218.** Een getal met een spatie als duizendtalscheiding ('100 000') ontsnapt aan een check op `\d{5,}`: toets ook `\d \d{3}`. (review-batch6)
- **219.** Lees de vraagzin op tegenspraak met wat er gevraagd wordt ('wordt k keer zo groot' + 'hoeveel keer zo groot wordt de oppervlakte' steunt de afleider k). (review-batch6)
- **220.** Zet ook de tussenuitkomsten van een rekenvoorbeeld in een hint tegen de afleiders (duizend : 10 = honderd ↔ 'schaal 1 : 100'). (review-batch6)
- **221.** Een build kan sleutels terugzetten en zo een WACHT-reden laten verlopen: draai de batch-check op elke nieuwe build vóór het oordeel, en laat een WACHT zijn reden toetsen, niet alleen tellen. (review-batch6)
- **222.** Eén Claude-label kan meerdere routes dekken ('verhoudingstabel-verkeerd': additief, b × c, ± prijs van één, prijs ± verschil in aantal): tel de routes per label vóór een labelregel; meer dan één route = een vraagtekst of regels op waarde. (review-batch6; zie ook G8-1)
- **223.** 'Alle mutanten gevangen' zegt alleen iets over bestaande checks: voeg per gate-bevinding een mutant toe. (review-batch6)
- **230.** Bij een voorwaardelijke hint ('Blijven er twee over?') tel je per item hoeveel opties er na H1 echt overblijven. (G4 review-batch5)
- **231.** Een fout-hint die naar een andere strategie verwijst ('Schat eerst …') loop je per item na met die strategie, tegen de opties. (G4 review-batch5)
- **232.** Of de omgedraaide afrondregel ('minder dan vijf omhoog') zichtbaar wordt, hangt af van de kant van de vijf waar de eenheden liggen: bij plus valt hij weg als ze aan verschillende kanten liggen, bij min als ze aan dezelfde kant liggen (aanvulling op les 129). (G4 review-batch5)
- **233.** Na een wijziging (nieuwe data, vervangen afleiders, een strengere regel) kijk je of de randgevallen er nog in zitten, zoals een item met en zonder overgang. Zit een randgeval waar een tekst over gaat er niet meer in, dan toetst de check die tekst niet meer. (Didactiek 8 okt, G4)
- **234.** Zijn er afleiders vervangen, tel dan de verklap-test opnieuw (hoeveel opties blijven er na H1 over, en na H1 + H2?). Houd een snapshot van de opties bij die faalt als de opties veranderen. (Didactiek 8 okt, G4)
- **235.** Voeg je hergebruikte tekstblokken samen, lees de hele hint daarna opnieuw: geen zin twee keer, geen twee aankondigingen achter elkaar. (Didactiek 8 okt, G4 Z-#730)
- **240.** Een nieuwe motorregel maakt sleutels in elk item, niet alleen in het item waarvoor hij kwam (293 sleutels tegen 1 geattesteerde). Tel wat hij maakt (les 156/157) en toets de nieuwe route ook tegen elk antwoord (les 195). (recheck-batch6)
- **241.** Vervangende data kan nieuwe toevallige treffers maken (bank-318/620). Draai les 195 ook op de vervangers voordat je ze goedkeurt. (recheck-batch6)
- **242.** Een guard die op één beginfrase of een frasenlijst leunt, vangt alleen die vorm. Toets elke guard met eigen mutanten in een andere bewoording (bij les 223). (recheck-batch6; D216a/b, D217a–c)
- **243.** Een huisregel-guard die alleen in de check van één batch staat, dekt de andere batches niet. Huisregels horen in de gedeelde check (/workspace/g7work/huis_checks.py). (recheck-batch6, Z-#741)
- **244.** Een H2 die H1 als vraag herhaalt, is geen sterkere laag. H2 geeft altijd een stap meer dan H1. (recheck-batch6, Z-#742)
