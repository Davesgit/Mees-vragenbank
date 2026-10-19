# Z-#1121 — 'aantal stuks geld' als leesbare regel. PATCH COPY op ae59b04 (main, G5-motor a00a0c4e); niet geplaatst.
Volgorde hooks: zet_motor_z1121.py, dan zet_z1121.py; daarna sync_hint_keys + apply_hints.
- Oorzaak: de motorregel #81 'fout = het aantal munten' bestond al, maar de motor bereikte hem bij geld tellen nooit: het antwoord '€2,60' is geen geheel
  getal en 'Hoeveel geld zie je?' heeft geen getallen, dus 'if a is None and not n: return None' stopte eerder. Daarom stonden er letterlijke regels '€3'/'€4'
  (apply.log: 'regel niet te lezen' GET-M03 22/18 items, MEET-E07 143/134 items).
- zet_motor_z1121.py: zet hetzelfde #81-blok vóór die regel (motor a00a0c4e → ac0a0c14; zie motor_z1121.diff).
- zet_z1121.py: GET-M03 #1 'aantal munten (3)/(4)' → 'aantal munten', MEET-E07 #1 'aantal stuks geld (3)/(4)' → 'aantal stuks geld'; regel
  'fout = het aantal munten', tekst ongewijzigd, vooraan (preciezer dan 'te veel geteld (50 cent) (op de foto)', #48).
- Uitkomst: sleutels gelijk aan ae59b04 (44 items: GET-M03 13, MEET-E07 31); alleen de soort zonder '(3)/(4)'; geen 'regel niet te lezen' meer voor deze twee.
- check_z1121.py (APPLYLOG=…/apply.log): motor per item, sleutel per item (€<aantal stukken> is een optie en niet het antwoord), entry, tekst, SNAP; 6 mutanten.
