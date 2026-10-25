# diffcorpus domain: func (10 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('fn01', 'func', 'x=global; f() { local x=local; echo "in:$x"; }; f; echo "out:$x"; g() { x=changed; }; g; echo "after-g:$x"'),
('fn02', 'func', 'declare -n ref; f() { local -n r=$1; r=via-ref; }; v=orig; f v; echo "$v"; declare -n self=self; echo "self=[$self]" 2>&1; echo rc=$?'),
('fn03', 'func', 'declare -n a=b; declare -n b=a; echo "$a" 2>&1; echo rc=$?; echo alive'),
('fn04', 'func', 'f() { local v=outer; g; }; g() { echo "g-sees:$v"; v=modified; }; v=global; f; echo "final:$v"'),
('fn05', 'func', 'f() { return; }; f; echo "ret-empty=$?"; false; f2() { return; }; f2; echo "ret2=$?"; g() { return 257; }; g; echo "ret257=$?"'),
('fn06', 'func', 'f() { local -i n=5; n+=3; echo $n; local arr=(a b); echo "${arr[@]} ${#arr[@]}"; }; f; echo "arr-out=[${arr:-none}]"'),
('fn07', 'func', 'f() ( x=subshell; echo "in:$x" ); x=main; f; echo "out:$x"; h() { echo "h"; }; h >f.txt; cat f.txt'),
('fn08', 'func', 'declare -n r=arr; arr=(1 2 3); echo "${r[@]} ${r[1]}"; r[1]=X; echo "${arr[@]}"; r+=(4); echo "${arr[@]}"'),
('fn09', 'func', 'f() { shift; echo "args:$@ n=$# first=$1"; }; f a b c; f x; set -- p q; f "$@"'),
('fn10', 'func', 'f() { local v; echo "v=[${v:-unset}]"; v=set; }; u=outer; f; echo "u=$u"'),
]
