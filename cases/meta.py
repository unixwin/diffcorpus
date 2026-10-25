# diffcorpus domain: meta (3 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('meta01', 'meta', 'echo first-arg; echo "underscore=[$_]"; printf x y; echo "u2=[$_]"; f() { echo "fn=${FUNCNAME[0]} src=${BASH_SOURCE[0]} line=$LINENO"; g; }; g() { echo "g-caller:"; caller 0; }; f'),
('meta02', 'meta', 'printf \'f() { echo "src-line=$LINENO fn=${FUNCNAME[0]}"; }\\nf\\n\' > s.sh; . ./s.sh; echo "LINENO-main=$LINENO"'),
('meta03', 'meta', 'set -- a b; echo "star=$* at=$@ zero=$0 nine=${9:-none}"; shift 5 2>&1; echo "shift-rc=$? n=$#"; shift 0; echo "shift0=$?"'),
]
