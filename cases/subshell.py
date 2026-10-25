# diffcorpus domain: subshell (6 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('sb01', 'subshell', 'x=1; ( x=2; echo "in:$x" ); echo "out:$x"; y=$(x=3; echo $x); echo "y=$y x=$x"; cd /; pwd; cd - >/dev/null; pwd | tail -c 20'),
('sb02', 'subshell', 'a=(1 2); ( a+=(3); echo "in:${a[@]}" ); echo "out:${a[@]}"; ( shopt -s nullglob ); shopt nullglob'),
('sb03', 'subshell', "trap 'echo MAIN-EXIT' EXIT; ( trap - EXIT; echo sub-no-trap ); echo main-continues"),
('sb04', 'subshell', 'f() { echo fn; }; x=$(f); echo $x; ( f ); echo rc=$?'),
('sb05', 'subshell', 'i=0; echo a b c | while read w; do i=$((i+1)); done; echo "pipe-i=$i"; while read w; do i=$((i+1)); done <<< "x y"; echo "redir-i=$i"'),
('sb06', 'subshell', 'shopt -s lastpipe; echo a b | read w1 w2; echo "w=[$w1][$w2]" 2>&1; jobs'),
]
