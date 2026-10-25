# diffcorpus domain: status (10 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('ps01', 'status', 'false | true; echo "a=$?"; set -o pipefail; false | true; echo "b=$?"; true | false; echo "c=$?"; set +o pipefail; echo "pf=${PIPESTATUS[@]}"'),
('ps02', 'status', '! false; echo $?; ! true; echo $?; ! false | false; echo "st=$? pipes=${PIPESTATUS[@]}"'),
('ps03', 'status', 'false && echo yes || echo no; echo $?; true && echo yes2; echo $?; false; echo $?; true; echo $?'),
('ps04', 'status', 'sleep 0.05 & p=$!; wait $p; echo "wait=$?"; false & wait $!; echo "waitfalse=$?"; wait 99999 2>&1; echo "waitbad=$?"'),
('ps05', 'status', '(exit 42); echo "sub=$?"; bash -c \'exit 7\' 2>/dev/null || true; "@@SELF@@" -c \'exit 7\'; echo "self=$?"'),
('ps06', 'status', 'false & true & wait -n; echo "wn=$?"; sleep 0.01 & wait -n $! 2>&1; echo "wnp=$?"'),
('ps07', 'status', 'echo hi | read l; echo "l=[$l] ps=${PIPESTATUS[@]}"; echo hi | { read l; echo "inpipe=[$l]"; }; { echo a; echo b; } | wc -l'),
('ps08', 'status', 'cmd() { return 3; }; cmd; echo $?; cmd | cat; echo "pipest=${PIPESTATUS[0]}"; ! cmd; echo "neg=$?"'),
('ps09', 'status', 'set -e; false; echo reached; echo "outer rc=$?"'),
('ps10', 'status', '{ false; echo "inbrace rc=$?"; }; echo out; ( false ); echo "paren rc=$?"'),
]
