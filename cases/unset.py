# diffcorpus domain: unset (3 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('un01', 'unset', 'declare -n r=t; t=val; unset r; echo "t=[${t:-gone}] r-set:${r:+yes}"; declare -n r2=t2; t2=v2; unset -n r2; echo "t2=[${t2:-gone}]"'),
('un02', 'unset', 'f() { echo fbody; }; unset -f f; type f 2>&1; echo rc=$?; v=1; unset -v v; echo "v=[${v:-gone}]"; unset -v nonexist_xyz; echo "unrc=$?"'),
('un03', 'unset', 'declare -n r=t; t=v; unset -n t 2>&1; echo rc=$?; echo "t=[${t:-gone}] r=[$r]"'),
]
