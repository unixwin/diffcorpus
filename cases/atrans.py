# diffcorpus domain: atrans (4 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('at01', 'atrans', 'declare -A m=([a]=1 [b]=2); o=${m@k}; echo "k=[$o]"; a=(x y); echo "arrk=[${a@k}]"; v=hi; echo "a-flag=[${v@a}]"; declare -i n=3; echo "n-flag=[${n@a}]"; declare -r r=1; echo "r-flag=[${r@a}]"'),
('at02', 'atrans', 'pre_a=1; pre_b=2; other=3; echo "names:${!pre_@}"; echo "names2:${!pre_*}"; v=pre_a; echo "${!v@a}" 2>&1'),
('at03', 'atrans', 's="hello world"; echo "${s@u}"; echo "${s@L}"; t="ABC"; echo "${t@u}|${t@L}"; echo "${s@E}"; p=\'a\\nb\'; echo "${p@P}"'),
('at04', 'atrans', 'name="arr[1]"; arr=(zero one two); echo "${!name}"; name2="arr"; echo "${!name2[@]}"; idx="arr[2]"; echo "${!idx}"'),
]
