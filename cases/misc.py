# diffcorpus domain: misc (15 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('ms01', 'misc', 'x=b; case $x in a) echo A;; b) echo B; fallthrough-placeholder;; esac'),
('ms02', 'misc', 'case abc in a*) echo 1 ;& b*) echo 2 ;;& *c) echo 3 ;;& *) echo 4 ;; esac'),
('ms03', 'misc', 'case x in esac 2>&1; echo rc=$?; :; echo colon=$?; true false; echo tf=$?; > /dev/null; echo redir-only=$?; v=1; echo assign-only=$?'),
('ms04', 'misc', 'echo "before"; exit 3'),
('ms05', 'misc', 'unset -v PATH 2>&1; echo rc=$?; echo hi 2>&1 | head -1'),
('ms06', 'misc', 'a=1 b=2; echo "$a $b"; a+=x; echo $a; ((a+=1)) 2>&1; echo "a=$a rc=$?"'),
('ms07', 'misc', 'echo "${HOME} ${PWD##*/}"; cd /; echo $PWD; cd - >/dev/null; echo back'),
('ms08', 'misc', "{ time -p true; } 2>tf.txt; sort tf.txt; echo ---; { time true; } 2>tg.txt; grep -o 'real\\|user\\|sys' tg.txt | sort | uniq -c"),
('ms09', 'misc', 'echo $((RANDOM==RANDOM)); set -o posix 2>&1 | head -1; echo $-; echo $_ 2>&1 | head -1'),
('ms10', 'misc', "compgen -A builtin | sort | head -5; compgen -A keyword | wc -l; compgen -v | grep -c '^BASH' "),
('cg01', 'misc', "compgen -W 'aa ab ba' -- a; echo ---; compgen -W 'x y z' -P PRE- -S -SUF; compgen -A variable | grep -E '^(PWD|HOME)$' | sort"),
('cg02', 'misc', 'kill -l 9; kill -l KILL 2>&1; echo rc=$?; kill -l | head -c 100; echo; kill -l 999 2>&1; echo rc2=$?'),
('cg03', 'misc', 'sleep 0.2 & j=$!; jobs | sed -E \'s/[0-9]+/N/g\'; jobs -l | sed -E \'s/[0-9]+/N/g\' | head -2; wait $j; jobs; echo "after-jobs-empty"'),
('cg04', 'misc', 'hash -p /bin/echo myecho; myecho via-hash-path; hash | head -3; type myecho; hash -d myecho; type myecho 2>&1; echo rc=$?'),
('cg05', 'misc', "alias myal='echo aliased'; alias -p | grep myal; unalias myal; alias myal 2>&1; echo rc=$?; shopt -s expand_aliases; alias e2='echo E2'; e2"),
]
