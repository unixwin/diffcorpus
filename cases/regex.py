# diffcorpus domain: regex (4 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('rx01', 'regex', '[[ abc123 =~ ([a-z]+)([0-9]+) ]]; echo "${BASH_REMATCH[@]}"; [[ abc =~ (x)|(b) ]]; echo "alt:${BASH_REMATCH[@]} [1]=[${BASH_REMATCH[1]}] [2]=[${BASH_REMATCH[2]}]"; [[ "a b" =~ "a b" ]]; echo lit=$?; [[ "axb" =~ a.b ]]; echo dot=$?; [[ "axb" =~ "a.b" ]]; echo qdot=$?'),
('rx02', 'regex', 'declare -A m=([k]=v); [[ -v m[k] ]]; echo "vk=$?"; [[ -v m[no] ]]; echo "vno=$?"; a=(1); [[ -v a[0] ]]; echo "va0=$?"; [[ -v a[5] ]]; echo "va5=$?"; [[ -v PATH ]]; echo "vp=$?"'),
('rx03', 'regex', 'touch f1; ln -sf f1 link1; ln -sf broken-target-xyz broken1; [ -e broken1 ]; echo "e-broken=$?"; [ -L broken1 ]; echo "L=$?"; [ f1 -nt broken1 ]; echo "nt=$?"; [ missing -ot f1 ]; echo "ot-miss=$?"; [[ f1 -ef f1 ]]; echo "ef=$?"; [[ link1 -ef f1 ]]; echo "ef-link=$?"'),
('rx04', 'regex', '[[ B > a ]]; echo "B>a:$?"; [[ a < b ]]; echo "a<b:$?"; [[ abc == a* ]]; echo "pat:$?"; [[ abc == "a*" ]]; echo "qpat:$?"; shopt -s extglob; [[ abbc == a+(b)c ]]; echo "ext:$?"'),
]
