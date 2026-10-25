# diffcorpus domain: glob (17 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('gl01', 'glob', 'mkdir -p d && cd d && touch a.txt b.txt c.md .hidden && echo *.txt && echo * && echo .* && shopt -s dotglob && echo *'),
('gl02', 'glob', 'mkdir -p d && cd d && touch f1 f2 f10 fa; echo f[0-9] && echo f[!0-9] && echo f[^0-9] && shopt -s globasciiranges; echo f[a-z]'),
('gl03', 'glob', 'shopt -s extglob\nmkdir -p d && cd d && touch ab aab abb acb\necho a*(b)\necho a+(b)\necho a?(b)\necho a@(b|c)b\necho a!(b)'),
('gl04', 'glob', 'mkdir -p d/sub/deep && cd d && touch top sub/mid sub/deep/low; shopt -s globstar; echo ** && echo **/*.txt 2>/dev/null; touch x.txt sub/y.txt; echo **/*.txt'),
('gl05', 'glob', 'mkdir -p d && cd d && touch A.TXT b.txt; shopt -s nocaseglob; echo *.txt; echo *.TXT; shopt -u nocaseglob; echo *.TXT'),
('gl06', 'glob', 'echo nomatch*.xyz; shopt -s nullglob; echo "pre nomatch*.xyz post"; echo "n=$(echo nomatch*.xyz | wc -w)"; shopt -s failglob; echo nomatch*.xyz 2>&1; echo rc=$?'),
('gl07', 'glob', 'mkdir -p d && cd d && touch "a b" "a  b" axb; echo a*b; printf \'<%s>\\n\' a?b; echo [[:space:]]* 2>/dev/null | head -c 100; echo'),
('gl08', 'glob', 'v="abc123"\neval \'case $v in +([a-z])+([0-9])) echo m1;; *) echo no;; esac\' 2>&1; echo "pre-extglob-rc=$?"\nshopt -s extglob\ncase $v in +([a-z])+([0-9])) echo m2;; *) echo no2;; esac'),
('gl09', 'glob', 'mkdir -p d && cd d && touch ab abc abd; echo a[b-d]; echo a[!b-d]; echo a[]] 2>&1; touch \']x\' ; echo []""]* 2>/dev/null; echo done'),
('gl10', 'glob', 'p="a/b/c.txt"; echo "${p##*/} ${p%/*}"; mkdir -p d/e && cd d && echo */ && echo e/../e'),
('gl11', 'glob', 'shopt -s extglob nullglob\nmkdir -p d && cd d && touch foo.txt foo.md bar.txt\necho *.@(txt|md)\necho !(bar).txt\necho *(foo|bar).*'),
('gl12', 'glob', 'mkdir -p d && cd d && touch {1..3}.txt; echo {a,b}{1,2}; echo {01..03} {z..x} {a..c}{1..2}; echo x{,y,}z'),
('gb201', 'glob', 'mkdir -p d && cd d && touch x.txt y.md sub_note; GLOBIGNORE="*.txt"; echo *; unset GLOBIGNORE; echo *.txt; echo */ 2>&1'),
('gb202', 'glob', 'mkdir -p onlydir && touch plainfile; echo */; echo */. 2>/dev/null | head -c 60; echo; mkdir -p a/b/c; echo a/**/c; shopt -s globstar; echo a/**/c; echo a/**'),
('gb203', 'glob', 'touch ab ac; echo {a..e..2} {5..1..2} {01..5..2} {a,b{1,2}}; v={x,y}; echo $v; echo pre{A,B,}post'),
('gb204', 'glob', 'echo ~; echo ~+; echo ~- 2>&1; olddir=$OLDPWD; x=~/sub; echo "tildeassign-prefix-ok"; p=:/path:~; echo "p=[$p]"; a=a:~; echo "a=[$a]"'),
('gb205', 'glob', "mkdir -p d && cd d && touch '[abc]' 'star*file' 'q?file'; echo \\[abc\\]; echo 'star*file'; printf '<%s>\\n' *"),
]
