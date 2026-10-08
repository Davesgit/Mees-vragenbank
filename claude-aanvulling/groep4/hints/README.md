# hints/ (G4) — nog leeg

Schrijf hints per somtype in `hints/batch1.json`, `batch2.json`, … (zelfde formaat als G3 `hints/batch4.json`):

```json
{"batch": "batch1", "geschreven": "2026-10-..", "uitleg": "...", "somtypen": [
  {"doel": "G4-GET-E03", "nr": 1, "somtype": "<kop uit de md>",
   "nrOrigineel": 1, "somtypeOrigineel": "<somtypeOrigineel uit de regel 'Sleutel' in de md>",
   "hint1": "...", "hint2": "...", "ouderzin": "...",
   "foutHints": [{"bron": "nieuw", "soort": "bijna", "claudeDenkfout": null, "regel": "fout ligt 1 naast het antwoord", "tekst": "..."}]}
]}
```

- Neem `nrOrigineel` + `somtypeOrigineel` over uit de regel **Sleutel** in `somtypen/<doel>.md`. Hints blijven gekoppeld als de
  nummering of de kop later verandert. `sync_hint_keys.py` koppelt eerst op claudeId (`bevroren/somtype_nr_v1.json`), daarna op de kop.
- Daarna: `python3 scripts/build_g4.py`. Die draait zelf `sync_hint_keys.py` en `apply_hints.py`. Controleer met `python3 check_hints.py`.
