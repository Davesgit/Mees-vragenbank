"""geldigeAntwoorden-check (G5 merge-fixlijst #360, Didactiek gate ronde 9, les 105/106; gedeeld door check_merge_notatie G5–G8). Leest alleen.
FAIL: een item met een niet-lege lijst geldigeAntwoorden waarin het antwoord niet staat. De checker van de app gebruikt die vaste lijst:
zo zou het goede antwoord fout gerekend worden en een fout antwoord goed (G5 E05 gen-013: 229 tegenover '230')."""
import re

def vormen(ans):
    """De lijst zoals de G8→G5-items hem hebben: het antwoord, en bij een heel getal vanaf 1000 ook de vorm met punt ('1000', '1.000')."""
    a = str(ans); uit = [a]
    if re.fullmatch(r'\d{4,}', a): uit.append(f'{int(a):,}'.replace(',', '.'))
    elif re.fullmatch(r'\d{1,3}(\.\d{3})+', a): uit.append(a.replace('.', ''))
    return uit

def vind(items):
    return [f"{it.get('id')}: antwoord {it.get('antwoord')!r} niet in geldigeAntwoorden {it['geldigeAntwoorden'][:4]}"
            for it in items if it.get('geldigeAntwoorden') and str(it.get('antwoord')) not in [str(x) for x in it['geldigeAntwoorden']]]

def rapport(items):
    uit = vind(items)
    print(f"\nGELDIG (#360: het antwoord staat niet in geldigeAntwoorden): {len(uit)} (FAIL)")
    for x in uit[:20]: print('  FAIL GELDIG', x)
    return len(uit)
