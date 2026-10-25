# diffcorpus domain: declarep (3 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('dp01', 'declarep', 'v="a b"; declare -p v; arr=(1 "x y" \'\'); declare -p arr; declare -A m=([k]="v v"); declare -p m; declare -i n=5; declare -p n; declare -n r=v; declare -p r'),
('dp02', 'declarep', 'export EX="line1\nline2"; declare -x | grep \'^declare -x EX=\' ; echo "---"; f() { echo body; }; declare -f f; declare -F f'),
('dp03', 'declarep', 'readonly ROA=(a b); declare -p ROA; declare -r s=x; s=y 2>&1; echo "rc=$? s=$s"; declare -p s'),
]
