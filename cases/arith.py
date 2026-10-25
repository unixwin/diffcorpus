# diffcorpus domain: arith (20 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('ar01', 'arith', 'echo $((2**3**2)) $(( (2**3)**2 )) $((-2**2)) $((-(2**2)))'),
('ar02', 'arith', 'echo $((2#1010)) $((8#17)) $((16#ff)) $((36#z)) $((64#@)) $((64#_)) $((64#__)) 2>&1'),
('ar03', 'arith', 'echo $((9223372036854775807+1)) $((9223372036854775807*2)) $((-9223372036854775808/-1)) 2>&1; echo rc=$?'),
('ar04', 'arith', 'x=5; echo $((x++)) $x $((++x)) $x $((x--)) $x $((--x)) $x'),
('ar05', 'arith', 'x=0; y=$((x+=3, x*=2, x-1)); echo "$y $x"; z=$((1?10:20, 0?30:40)); echo $z'),
('ar06', 'arith', 'a=(10 20 30); i=1; echo $((a[i++])) $i $((a[i]+a[0])); echo $((a[1+1]))'),
('ar07', 'arith', 'echo $((5/2)) $((5%2)) $((-5/2)) $((-5%2)) $((5/-2)) $((5%-2))'),
('ar08', 'arith', 'echo $((1<<62)) $((1<<63)) $((-1>>1)) $((255>>4)) $((5&3)) $((5|3)) $((5^3)) $((~5))'),
('ar09', 'arith', 'x="  42  "; echo $((x)) $((x+1)); y=010; echo $((y)) $((10#$y)); z=08; echo $((z)) 2>&1; echo rc=$?'),
('ar10', 'arith', 'echo $((a=5)) $a; ((b+=2)) 2>&1; echo "b=$b rc=$?"; ((c++)) ; echo "c=$c"; ((c)) ; echo rc=$?'),
('ar11', 'arith', 'v=3; echo $((v>2?100:200)); echo $((!v)) $((!0)); s=$((3>2 && 2>1 || 0)); echo $s'),
('ar12', 'arith', 'echo $((16#FF + 2#10)); x=0x10; echo $((x)); y="2+3*4"; echo $((y)) $((y*2))'),
('ar13', 'arith', 'i=0; a=$((i++ + i++ + i++)); echo "$a $i"; j=5; echo $((j+=j-=2)) $j 2>&1'),
('ar14', 'arith', 'echo $((5/0)) 2>&1; echo rc=$?; echo $((5%0)) 2>&1; echo rc=$?; echo after'),
('ar15', 'arith', 'declare -i n; n="3+4"; echo $n; n=" 5 * 2 "; echo $n; n=abc; echo "n=$n rc=$?"'),
('ax01', 'arith', 'echo $((36#Z)) $((36#z)) $((37#A)) $((62#Z)) $((64#z)) $((64#+)) $((64#/)) 2>&1'),
('ax02', 'arith', 'echo $((1<<64)) $((1<<65)) $((8>>-1)) 2>&1; echo rc=$?; echo $((2**-1)) 2>&1; echo rc2=$?'),
('ax03', 'arith', 'x=1; echo $((x?y=10:y=20)) "x=$x y=$y"; a=(5); echo $((a[0]++)) ${a[0]} $((++a[0])); unset e; echo $((e)) $((e+1)); s=""; echo $((s)) 2>&1'),
('ax04', 'arith', 'v="abc"; echo $((v)) 2>&1; echo rc=$?; v="a1"; echo $((v)) 2>&1; arr=(3 4); echo $((arr)) $((arr[0]+arr[1])); echo $((arr[@])) 2>&1 | head -c 120; echo'),
('ax05', 'arith', 'echo $(( 010 + 0x10 + 10 )); w="0"; echo $((w?w:9)); (( q = 4 > 3 ? 11 : 22 )); echo q=$q; echo $(( - -5 )) $((!!5))'),
]
