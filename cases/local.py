# diffcorpus domain: local (3 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('lc01', 'local', 'f() { local -; set -f; echo "in-opts:$-"; }; set +f; f; case $- in *f*) echo noglob-leaked;; *) echo noglob-ok;; esac'),
('lc02', 'local', 'f() { local x=$(false); echo "local-subst-rc=$?"; local y; y=$(false); echo "assign-rc=$?"; }; f'),
('lc03', 'local', 'break 2 2>&1; echo "break-outside=$?"; continue 2>&1; echo "cont-outside=$?"; for i in 1 2 3; do for j in a b; do break 2; done; echo "never-$i"; done; echo done'),
]
