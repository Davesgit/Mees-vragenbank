# Z-#1090 ronde 2: lenen/onthouden per item (V-#1120, Oef-#1045/#1046) + Oef-#1040. Voorwaardelijk, NIET geplaatst.
Basis: na-ronde-z1090 91155a2 (git archive → /workspace/g8work/rc_91155a2). Volgorde: zet_lenen.py → zet_oef1040.py → sync_hint_keys → apply_hints.
- zet_lenen.py <basis>: per fout-hint met een leen-/onthoudzin en een gemengd somtype: splitsen zoals G6-GET-E04 (motor #399/#392):
  '<soort> (geleend)' regel + ' (geleend bij de tientallen)' / '<soort> (onthouden)' regel + ' (onthouden naar de tientallen|honderdtallen)' met de
  oude tekst, daarna de gewone soort met «Dat is te veel. Haal de tientallen nog eens af.» / «Dat is te weinig. Tel de tientallen (honderdtallen) nog eens bij elkaar.»
- zet_oef1040.py <basis>: GET-E05 #17 'honderdtal vergeten' (− 10) → 'tiental te weinig' «Dat is te weinig. Tel de tientallen nog eens bij elkaar.»
- check_lenen.py <basis> [MUT=, SNAP=1]: per itemsleutel, los van de motor nagerekend (lenen_lib.som); SNAP per item snap_lenen.json.
- mutrun_lenen.sh <basis>: 6 mutanten (lenen zonder lenen, onthouden zonder onthouden ×2, 1040 ×2, SNAP).
- sbx_r2.sh <map>: PATCH COPY-zandbak (SRC=<git archive>, HOOKS="zet_lenen zet_oef1040").

## r3 (V-#1130, Didactiek 15 okt 17:07; kopie van r2, bovenop 586d425)
- lenen_lib: ONTH_H kent ook «Tel de tientallen nog eens: als ze samen 100/honderd of meer zijn, komt er een honderdtal bij.»; les 450: nieuwe soort
  'leenH' («over een heel honderdtal heen: dan gaat er nog een honderdtal af», regel 'fout = antwoord + 100', '(geleend bij de honderdtallen)').
- zet_lenen: '100 of meer' → 'honderd of meer' (tegenhanger Oef-#1049); splitst per item; 'zonder'-tekst krijgt altijd een kijkzin.
- check_lenen: mutanten M_honderd, M_cijfer100, M_leenH. inventaris_l450.py <basis>: alle vormen vs wat de guard ziet.
- Draaien: SRC=/workspace/g8work/rc_586d425 bash sbx_r2.sh <map>

## r4 (Overzicht 17:10b; kopie van r3, bovenop 586d425)
- (a) leenH #7: de 14 'zonder'-sleutels krijgen «Dat is te veel. Haal de honderdtallen nog eens af.» (geen bedrag); check: 'bedrag in zonder-tekst', mutant M_bedragH.
- (b) LEEN_H ziet ook E05 #10 hint2 «Bij de tientallen ga je over een heel honderdtal heen. Ga eerst terug …» (tekst blijft; waar bij 18/18 items).
- les 450 op 586d425: 22 vormen / 34 entryteksten / 899 itemteksten; guard ziet 17 / 34 / 899 (de 5 vormen zijn tweede helften van tweezinsvormen).
