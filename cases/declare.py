# diffcorpus domain: declare (8 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('dc01', 'declare', 'declare -l low="AbC"; echo "$low"; low="XyZ"; echo "$low"; declare -u up="aBc"; echo "$up"; declare -u up2; up2=q; echo "$up2"'),
('dc02', 'declare', 'declare -i n="010"; echo $n; n="0x10"; echo $n; declare -i bad="a+b"; echo "bad=$bad"'),
('dc03', 'declare', 'declare -r ro=1; ro=2; echo "rc=$? ro=$ro"; declare -r ro2; ro2=x 2>&1; echo "rc=$? ro2=[${ro2:-unset}]"'),
('dc04', 'declare', 'declare -a idx=(a b); declare -A as=([k]=v); echo "${idx[@]} ${as[k]}"; declare -p idx as 2>&1 | head -4'),
('dc05', 'declare', 'x=1; declare -i x; x="2+3"; echo $x; declare +i x; x="2+3"; echo "$x"'),
('dc06', 'declare', 'declare -n nr=target; target=hi; echo $nr; nr=bye; echo $target; declare -p nr'),
('dc07', 'declare', 'f() { declare -g gv=global-set; local lv=1; echo "in:$gv $lv"; }; f; echo "gv=$gv lv=[${lv:-unset}]"'),
('dc08', 'declare', 'declare -t traced() { echo traced-body; } 2>&1; traced 2>&1; echo rc=$?'),
]
