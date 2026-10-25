# diffcorpus domain: env (8 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('en01', 'env', 'echo "opts=$-"; "@@SELF@@" -c \'echo inner-opts=$-\' '),
('en02', 'env', 'env -i "@@SELF@@" -c \'echo "PATH=[$PATH]"; echo "IFS-set:${IFS:+yes}"; echo "optind=$OPTIND"\' '),
('en03', 'env', 'export FOO=bar; "@@SELF@@" -c \'echo child:$FOO\'; BASH_ENV=/dev/null "@@SELF@@" -c \'echo ok\' '),
('en04', 'env', 'echo "versinfo=${BASH_VERSINFO[*]}"; echo "mach=[$MACHTYPE] host=[$HOSTTYPE] ostype=[$OSTYPE]"'),
('en05', 'env', 'umask 077; "@@SELF@@" -c \'umask\'; umask'),
('env201', 'env', 'umask -S; umask 027; umask -S; umask 022; u=$(ulimit -Sn); h=$(ulimit -Hn); if [ "$u" -le "$h" ]; then echo nofile-soft-le-hard; fi; ulimit -a | grep -c . '),
('env202', 'env', 'printf \'%s\' "$IFS" | od -An -c | tr -s \' \'; unset IFS; s="a b\\tc"; set -- $s; echo "unsetIFS-split n=$#"; IFS=\' \'; s2="x  y"; set -- $s2; echo "spaceIFS n=$#"'),
('env203', 'env', 'echo "groups-n=${#GROUPS[@]} first-group-set:${GROUPS[0]:+yes}"; echo "uid-set:${UID:+yes} euid-set:${EUID:+yes}"; echo "hostname-len=${#HOSTNAME}"'),
]
