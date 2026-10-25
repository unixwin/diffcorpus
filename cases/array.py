# diffcorpus domain: array (15 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('arr01', 'array', 'a=(1 2 3); a+=(4 5); echo "${a[@]} ${#a[@]}"; a[10]=x; echo "${#a[@]} ${!a[@]}"'),
('arr02', 'array', 'a=(1 2 3 4); unset \'a[1]\'; echo "n=${#a[@]} idx=${!a[@]} vals=${a[@]}"; echo "[${a[1]}] [${a[-1]}] [${a[-4]}]"'),
('arr03', 'array', 'a=("a b" c "d  e"); printf \'<%s>\\n\' "${a[@]}"; printf \'<%s>\\n\' "${a[*]}"; IFS=,; printf \'<%s>\\n\' "${a[*]}"'),
('arr04', 'array', 'a=(0 1 2 3 4); echo "${a[@]:1:2}"; b=("${a[@]:2}"); echo "b=${b[@]} n=${#b[@]}"; echo "${a[@]: -2:1}"'),
('arr05', 'array', 'declare -A m; m[x]=1; m[y]=2; m[x]+=5; echo "${m[x]} ${m[y]} ${#m[@]}"; unset \'m[y]\'; echo "${#m[@]} [${m[y]:-gone}]"'),
('arr06', 'array', 'a=(1 2); a[-1]=last; echo "${a[@]}"; a[-5]=bad 2>&1; echo rc=$?; echo "${a[@]}"'),
('arr07', 'array', 'a=([3]=d [1]=b [0]=a); echo "${a[@]}"; echo "${a[*]}"; printf \'%s\\n\' "${!a[@]}"'),
('arr08', 'array', 's="x y z"; a=($s); echo "n=${#a[@]} ${a[@]}"; IFS=:; b=(p:q:r); c=(${b[0]}); echo "c=${c[@]}"'),
('arr09', 'array', 'a=(1 2 3); a=("${a[@]}" 4); echo "${a[@]}"; a=(); echo "n=${#a[@]} [${a[@]}]"; a[0]=only; echo "${a[@]} ${#a[@]}"'),
('arr10', 'array', 'declare -A m=([a]=1); echo "${m[a]:-d} ${m[missing]:-d}"; m["key with space"]=v; echo "${m[key with space]} ${#m[@]}"'),
('arr11', 'array', 'a=(one two); i=0; a[i++]=X; echo "${a[@]} i=$i"; a[++i]=Y; echo "${a[@]} i=$i"'),
('arr12', 'array', 'x=scalar; x+=(appended); echo "${x[@]} n=${#x[@]}"; y=scalar; y[1]=second; echo "${y[@]} idx=${!y[@]}"'),
('arr13', 'array', 'a=(1 2 3); unset a; echo "n=${#a[@]} [${a:-unset}]"; a[2]=only; echo "idx=${!a[@]} vals=${a[@]}"'),
('arr14', 'array', 'a=("a@b" "c*d"); printf \'[%s]\' "${a[@]@Q}"; echo; printf \'[%s]\' "${a[@]^^}"; echo'),
('arr15', 'array', 'IFS=/; a=(usr local bin); echo "${a[*]}"; echo "${a[@]}"; unset IFS; set -- "${a[@]}"; echo "argc=$# $1 $3"'),
]
