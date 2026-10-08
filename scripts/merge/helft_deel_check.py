"""Les 247 (Didactiek review G7 VERH-04 #4/#7, Z-#748): bij 'welk deel'-items mogen het deel en de rest niet even groot zijn.
Anders krijgt ook het kind dat de verkeerde groep telt het goede antwoord. WARN als het goede antwoord 'k op de n' is met 2k = n.
Gebruik: import helft_deel_check as HD; n_warn = HD.rapport(items)."""
import re
P = re.compile(r'(\d+) op de (\d+)')
def treffers(items):
    W = []
    for it in items:
        m = P.fullmatch(str(it.get('antwoord') or '').strip())
        if m and 2 * int(m.group(1)) == int(m.group(2)): W.append(f"{it['id']}: «{it['antwoord']}» — {(it.get('opgave') or '')[:80]}")
    return W
def rapport(items, toon=True):
    W = treffers(items)
    if toon:
        print(f"\nHELFT (les 247, Z-#748: 'welk deel' met een goed deel dat precies de helft is; de andere groep geeft hetzelfde antwoord): {len(W)} (WARN)")
        for x in W[:15]: print('  WARN HELFT', x)
    return len(W)
