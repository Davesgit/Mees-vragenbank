# Z-#1092: rol i.p.v. plekwoord in G5 (les 193). Voorwaardelijk, NIET geplaatst. PATCH COPY op ae59b04 (main; Z-#1090 r4 + Oef-#1040 zitten erin).
Rebase van r13/z1090/z1092 (zet b66a70cb / plek_lib 35c0cfb7 / check 86b63203 op 379fab1 + r2): alleen de importmap ../r2 → ../r4; logica gelijk.
`bash sbx_z1092.sh <map>` = PATCH COPY: git archive ae59b04 (of SRC=<map>) → zet_z1092 (twee keer) → sync → apply → check_hints.
- zet_z1092.py: 'het eerste/tweede getal|bedrag' → 'het grootste/kleinste …' (min/plus/keer/gedeeld/geld; per item: twee getallen verschillend,
  bij min/gedeeld eerste = grootste) of 'het getal dat er al staat' (aanvulsom □). Niet: MEET-E06, VBN-E03. 115 wijzigingen, 0 MELD, tweede run 0.
- Oef-#1052: rooster GET-M05 #5 [hint1] / MEET-E03 #1 [hint2] krijgen een rolzin (het aantal rijen, hoeveel hokjes er in één rij staan), waar per item (rooster_ok).
- check_z1092.py: guard op entry- en itemteksten, rol per item, SNAP per item (snap_z1092.json, gelijk aan r13: 546483fd). Mutanten 7/7.
- ../snap_z1090.json ververst in deze ronde: alleen de 4 rolwissels GET-E05 #1 / GET-M04 #2 'tiental te veel/weinig' ('het eerste getal' →
  'het getal dat er al staat'); de rest is de repo-snap a9bb1254 (ook GET-E05 #17, dat check_z1090 via Oef-#1040/HERNOEMD al accepteert). check_z1090 FAIL 0.
