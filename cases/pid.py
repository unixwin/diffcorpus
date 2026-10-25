# diffcorpus domain: pid (5 cases)
# Imported by tools/import_sources.py; scripts are byte-identical to their sources.
CASES = [
('pid01', 'pid', 'if [ $$ -eq $BASHPID ]; then echo main-eq; else echo main-ne; fi; ( if [ $$ -eq $BASHPID ]; then echo sub-eq; else echo sub-ne; fi ); x=$(if [ $$ -eq $BASHPID ]; then echo cmd-eq; else echo cmd-ne; fi); echo $x'),
('pid02', 'pid', 'echo "ppid-of-sub:"; ( if [ $PPID -eq $$ ]; then echo ppid-is-mainpid; else echo ppid-other; fi )'),
('pid03', 'pid', 'RANDOM=42; echo "$RANDOM $RANDOM $RANDOM"; RANDOM=42; echo "$RANDOM $RANDOM"'),
('pid04', 'pid', 'case $SRANDOM in \'\'|*[!0-9]*) echo srand-nonnumeric;; *) echo srand-numeric;; esac; SRANDOM=7; a=$SRANDOM; b=$SRANDOM; if [ "$a" = "$b" ]; then echo same; else echo diff; fi; if [ ${#EPOCHSECONDS} -eq 10 ]; then echo epoch10; fi; case $EPOCHREALTIME in *.*) echo realtime-dot;; *) echo realtime-nodot;; esac'),
('pid05', 'pid', 'SECONDS=100; echo $SECONDS; ( SECONDS=5; echo "sub-sec=$SECONDS" ); echo "main-sec=$SECONDS"; UID=$UID 2>&1; echo "uidrc=$?"'),
]
