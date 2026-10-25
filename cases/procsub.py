# diffcorpus domain: procsub (2 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('pr01', 'procsub', 'diff <(printf \'a\\nb\\n\') <(printf \'a\\nc\\n\'); echo "diff-rc=$?"; cat <(echo hello); echo "cat-rc=$?"'),
('pr02', 'procsub', 'while read l; do echo "[$l]"; done < <(printf \'1\\n2\\n\'); exec 3< <(printf \'from-proc\'); read -u 3 l; echo "fd3=$l"; exec 3<&-'),
]
