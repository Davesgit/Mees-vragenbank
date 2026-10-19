# r21/tools — padvrije tools (Oefeningen, 19 okt). Geen vaste paden; guard: `bash guard_paden.sh` (FAIL + exit 1 bij /workspace/, /tmp/, /home/, /cursor/).
Verplicht in de omgeving: REPO (git-repo van de vragenbank, alleen gelezen) en BASIS_COMMIT (commit of branch). Ontbreekt er één, is REPO geen repo of bestaat
de commit niet: 'FAIL instelling: …' en exit 2 (_repo.sh). De basis komt via git archive in een mktemp-map en gaat dan naar de doelmap.
- sbx_g8.sh <map>: G8-zandbak, HOOKS twee keer, sync/apply (log <map>/apply.log), check_hints, merge-notatie; groep8_voor = vóór de hooks.
- sbx_oef1070.sh <map>: sbx_g8 met zet_oef1070.py uit OEF1070_DIR, of uit de basis (groep8/scripts/oef1070, vanaf na-ronde-r20); geen van beide: exit 2.
- les457.sh <snapshot> <5|8> <scriptmap|-> "<hooks>": repo-snapshot + onze scriptmappen (zonder sbx/logs/groep*_voor), hooks twee keer, sync/apply
  (log <snapshot>.apply.log), check_hints (+ merge-notatie bij G8).
- g5checks.sh <snapshot>: alle G5-repo-checks op één regel per check; z1091 met BASIS_COMMIT=${Z1091_BASIS:-ec3a77e} en BASIS_REPO=$REPO.
