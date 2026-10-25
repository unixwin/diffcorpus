# diffcorpus domain: redir (12 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('rd01', 'redir', 'echo out >f.txt 2>e.txt; cat f.txt; echo "rc=$?"; exec 3>f2.txt; echo to3 >&3; exec 3>&-; cat f2.txt'),
('rd02', 'redir', 'echo hi 2>&1 1>/dev/null; echo hi 1>/dev/null 2>&1; (echo err >&2; echo out) 2>f.txt 1>g.txt; echo "f=$(cat f.txt) g=$(cat g.txt)"'),
('rd03', 'redir', 'read x <<< "herestring"; echo "$x"; read y <<EOF\n\tnope\n\t\ttabbed\nEOF\nprintf \'<%s>\\n\' "$y"; cat <<-EOF\n\t\tstrip\n\tEOF'),
('rd04', 'redir', 'set -C; echo a >f; echo b >f 2>&1; echo rc=$?; echo b >>f; cat f; set +C; echo c >f; cat f'),
('rd05', 'redir', 'echo data <>f.txt; cat f.txt; { read l <&0; } <f.txt; echo "$l"; exec 3<>rw.txt; printf \'X\' >&3; exec 3>&-; cat rw.txt'),
('rd06', 'redir', '> only.txt; echo rc=$?; ls -l only.txt | awk \'{print $5}\'; x=1 >assign.txt; echo "x=$x"; cat assign.txt'),
('rd07', 'redir', 'f() { echo in-func; }; f >out.txt; cat out.txt; VAR=temp echo "$VAR"; echo "after:[$VAR]"; VAR=temp f; echo "after-func:[$VAR]"'),
('rd08', 'redir', 'declare -r RO=1; RO=2 >redir.txt 2>err.txt; echo rc=$?; cat err.txt; cat redir.txt'),
('rd09', 'redir', 'cat < nonexist 2>&1; echo rc=$?; echo hi > /nonexistent-dir-xyz/f 2>&1; echo rc=$?; echo still-alive'),
('rd10', 'redir', 'echo first >f; echo second >&1 >>f 2>&1; cat f; (echo a; echo b >&2) >both.txt 2>&1; cat both.txt'),
('rd11', 'redir', 'while read l; do echo "[$l]"; done <<\'QEOF\'\n$notexpanded\n\\back\nQEOF\nwhile read l; do echo "<$l>"; done <<EOF\n$((6*7))\nEOF'),
('rd12', 'redir', 'exec 3>&1; echo captured >&3; r=$(echo inner 3>&-); echo "r=$r"; echo done 3>&-'),
]
