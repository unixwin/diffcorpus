# diffcorpus domain: ifs (8 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('ifs01', 'ifs', 'IFS=:; s="a::b:"; set -- $s; echo "n=$# [$1][$2][$3][$4]"; s=":a::"; set -- $s; echo "n=$# [$1][$2][$3]"'),
('ifs02', 'ifs', 'IFS=; s="a b  c"; set -- $s; echo "n=$# [$1]"; IFS=" "; set -- $s; echo "n=$# [$1][$2][$3]"'),
('ifs03', 'ifs', 's="  a  b  "; set -- $s; echo "n=$# [$1][$2]"; IFS=-; s="--a--b--"; set -- $s; echo "n=$# [$1][$2][$3][$4]"'),
('ifs04', 'ifs', 'a=(x y); IFS=,; echo "star=${a[*]}"; v="p,q"; echo "${v//,/ }"; read -ra r <<< "1,2,3"; echo "r=${r[@]}"'),
('ifs05', 'ifs', 'printf \'a\\t b\\n\' | { IFS= read -r l; printf \'<%s>\\n\' "$l"; }; printf \'  x  \\n\' | { IFS= read -r l; printf \'<%s>\\n\' "$l"; }'),
('ifs06', 'ifs', 's="aXbXXc"; IFS=X; set -- $s; echo "n=$# [$1][$2][$3][$4]"'),
('ifs07', 'ifs', 'arr=(a b c); local_ifs=$IFS; IFS=\'\'; echo "${arr[*]}"; IFS=$local_ifs; join="${arr[*]}"; echo "$join"'),
('ifs08', 'ifs', 's=$\'a\\tb\\nc\'; set -- $s; echo "n=$# [$1][$2][$3]"; IFS=$\'\\n\'; set -- $s; echo "n=$# [$1][$2]"'),
]
