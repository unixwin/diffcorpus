# diffcorpus domain: getopts (4 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('go01', 'getopts', 'while getopts "ab:c" opt; do echo "opt=$opt arg=[$OPTARG] ind=$OPTIND"; done; echo end\' '),
('go02', 'getopts', 'set -- -a -b val -x; while getopts "ab:" opt; do echo "o=$opt a=[$OPTARG]"; done; echo "rc=$? ind=$OPTIND rest=${@:$OPTIND}"'),
('go03', 'getopts', 'set -- -a; OPTIND=1; while getopts ":a" opt; do echo "o=$opt"; done; set -- -z; OPTIND=1; while getopts ":a" opt; do echo "silent-o=$opt arg=[$OPTARG]"; done'),
('go04', 'getopts', 'f() { local OPTIND=1; while getopts "xy" o; do echo "f-o=$o"; done; }; set -- -x -z; f "$@"; echo "outer-ind=$OPTIND"'),
]
