# diffcorpus domain: syntax (5 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('sx01', 'syntax', "if true; then echo x' "),
('sx02', 'syntax', 'echo "unterminated\' '),
('sx03', 'syntax', '(( 1 + )) 2>&1; echo "rc=$?"; [[ a == ]] 2>&1; echo "rc2=$?"; echo alive'),
('sx04', 'syntax', 'for in 1 2; do echo x; done'),
('sx05', 'syntax', 'echo hi | | echo there'),
]
