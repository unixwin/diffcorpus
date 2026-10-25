# diffcorpus domain: cd (3 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('cd01', 'cd', 'mkdir -p real && ln -s real linkdir; cd linkdir; echo "logical=$PWD"; pwd -P; cd -P .; echo "physical=$PWD"; cd ..; pwd'),
('cd02', 'cd', 'mkdir -p one two; pushd one >/dev/null; pushd ../two >/dev/null; echo "stack:"; dirs -p; popd >/dev/null; pwd; popd >/dev/null; pwd; pushd 2>&1; echo "pushd-noargs-rc=$?"'),
('cd03', 'cd', 'cd "" 2>&1; echo "rc=$?"; unset OLDPWD; cd - 2>&1; echo "rc2=$?"; CDPATH=/nonexistent-xyz; mkdir -p subdir; cd subdir; echo "cdpath=$PWD"'),
]
