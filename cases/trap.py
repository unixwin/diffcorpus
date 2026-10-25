# diffcorpus domain: trap (17 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('ts01', 'trap', "trap 'echo EXIT-TRAP' EXIT; echo body"),
('ts02', 'trap', "( trap 'echo SUB-EXIT' EXIT; echo in-sub ); echo after-sub"),
('ts03', 'trap', "trap 'echo ERRTRAP rc=$?' ERR; false; echo after-false; true; echo end"),
('ts04', 'trap', 'set -e; f() { false; echo in-f; }; f; echo "reached rc=$?"'),
('ts05', 'trap', 'set -e; if false; then echo a; fi; echo if-ok; false || echo or-ok; ! false; echo bang-ok; x=$(false); echo "assign-sub rc=$?"'),
('ts06', 'trap', 'set -u; echo "empty-arr:"; a=(); echo "a=[${a[@]}] n=${#a[@]}"; set --; echo "pos=[$@] n=$#"; echo "${undef:-def}"'),
('ts07', 'trap', 'set -u; echo "${a[@]}" 2>&1; echo rc=$?; echo "${undef}" 2>&1; echo rc=$?'),
('ts08', 'trap', "trap -p EXIT; trap 'echo X' EXIT; trap -p EXIT; trap -- 'echo Y' ERR; trap -p"),
('ts09', 'trap', "f() { trap 'echo RETURN-TRAP' RETURN; echo in-f; }; f; echo after"),
('ts10', 'trap', 'count=0; trap \'count=$((count+1))\' DEBUG; echo one; echo two; echo "debug-count=$count"'),
('ts11', 'trap', 'set -o | grep -E \'errexit|nounset|pipefail\'; shopt -q nullglob; echo "nullglob-q=$?"; shopt nullglob dotglob'),
('ts12', 'trap', 'SHELLOPTS=; echo "shellopts=$SHELLOPTS"; set -f; echo "after-f:$SHELLOPTS" | head -c 200; echo; set +f'),
('tr201', 'trap', 'set -E; trap \'echo ERR-IN\' ERR; f() { false; echo f-after; }; f; echo main-after; ( trap -p ERR ); x=$(false; echo incmd); echo "x=$x"'),
('tr202', 'trap', "trap 'echo USR1-GOT; ' USR1; kill -USR1 $$; echo after-signal; trap - USR1; kill -USR1 $$ 2>&1; echo should-not-reach"),
('tr203', 'trap', "trap 'echo DEBUG-HIT' DEBUG; set -T; f() { echo fbody; }; f; trap - DEBUG; echo end"),
('tr204', 'trap', "f() { trap 'echo F-RETURN' RETURN; echo body; ( echo subshell ); echo tail; }; f; echo out"),
('tr205', 'trap', 'echo "errtrap-set:"; trap -p ERR; set -E; trap \'true\' ERR; ( trap -p ERR ); f() { trap -p ERR; }; f'),
]
