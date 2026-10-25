# diffcorpus domain: source (4 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('so01', 'source', 'printf \'echo "sourced arg=[$1]"; return 5\\n\' > lib.sh; set -- orig; . ./lib.sh larg; echo "src-rc=$? args-after=$@"; source ./lib.sh 2>&1 | head -1'),
('so02', 'source', '. ./nonexist.sh 2>&1; echo "rc=$?"; PATH= . ./lib2.sh 2>&1; echo "rc2=$?"'),
('so03', 'source', 'exec -a customargv "@@SELF@@" -c \'echo zero=$0\' '),
('so04', 'source', 'printf \'echo in-exec\\n\' > run.sh; "@@SELF@@" -c \'exec -c /usr/bin/env\' 2>&1 | grep -c . ; echo "pipec=${PIPESTATUS[0]}"'),
]
