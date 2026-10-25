# diffcorpus domain: quote (8 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('q01', 'quote', 'echo "$(printf \'a\\n\\n\\n\')END"; echo "$(printf \'a\')END"; x=$(printf \'\\n\\n\'); echo "len=${#x}"'),
('q02', 'quote', 'echo \'a\'"\'"\'b\' "c\\"d" $\'e\\tf\' $\'g\\x41h\' $\'\\101\' '),
('q03', 'quote', 'v="a b"; echo $v | wc -w; echo "$v" | wc -w; for x in $v; do echo "[$x]"; done; for x in "$v"; do echo "<$x>"; done'),
('q04', 'quote', 'echo "$(echo "$(echo nested)")"; echo `echo \\`echo back\\``; x=$(cat <<EOF\nline1\nline2\nEOF\n); echo "$x"'),
('q05', 'quote', 'printf \'%s\\n\' "a\\\nb" \'c\\\nd\'; echo "e\\\nf"'),
('q06', 'quote', 's="*"; echo $s; echo "$s"; mkdir -p d && cd d && touch star; echo $s'),
('q07', 'quote', 'a="x"; echo "${a:-$(echo inner)}"; unset b; echo "${b:-$(echo inner2)}"; echo "$(false; echo st=$?)"'),
('q08', 'quote', "echo $'a\\ub' $'\\u0041\\U0001F600' 2>&1 | head -c 200; echo; echo $'\\e[31mX' | od -c | head -2"),
]
