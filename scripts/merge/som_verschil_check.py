"""Les 195/241 (Didactiek recheck G7 batch 6, Z-#744): bij 'Vul in. a : b = c : ?' mag het antwoord geen getal uit de vraag zijn,
en ook niet de som of het verschil van twee getallen uit de vraag (dan is een kind dat optelt of aftrekt toevallig goed). WARN.
Gebruik: import som_verschil_check as SV; n_warn = SV.rapport(items)."""
import re
P = re.compile(r'Vul in\. (\d+) : (\d+) = (\d+) : \?')
def treffers(items):
    W = []
    for it in items:
        m = P.fullmatch(it.get('opgave') or '')
        if not m or not str(it.get('antwoord')).isdigit(): continue
        a, b, c = map(int, m.groups()); ans = int(it['antwoord'])
        naam = {a: 'a', b: 'b', c: 'c', a + b: 'a+b', a + c: 'a+c', b + c: 'b+c', abs(c - b): '|c−b|', abs(c - a): '|c−a|', abs(a - b): '|a−b|'}
        if ans in naam: W.append(f"{it['id']}: {a} : {b} = {c} : ? → {ans} = {naam[ans]}")
    return W
def rapport(items, toon=True):
    W = treffers(items)
    if toon:
        print(f"\nSOMVERSCHIL (les 195/241, Z-#744: 'a : b = c : ?' met als antwoord een getal uit de vraag of de som/het verschil van twee): {len(W)} (WARN)")
        for x in W[:15]: print('  WARN SOMVERSCHIL', x)
    return len(W)
