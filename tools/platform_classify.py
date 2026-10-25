#!/usr/bin/env python3
"""Platform-applicability classifier for diffcorpus cases.

Assigns one enum value per case from script content, first matching rule
wins, and records which rule fired (auditability over precision). The
labels describe the case's *implicit platform premises*:

  linux-only           needs Linux-specific surfaces (/proc, /sys)
  posix                needs POSIX mechanisms (signals, job control,
                       symlinks, /dev/fd, process identity, procsub fds)
  windows-ok           no POSIX-only mechanism; at most portable premises
                       (files in cwd, /dev/null, bundled coreutils-class
                       utilities) that rubash + winuxcmd satisfy on Windows
  android-constrained  needs a controlling terminal (fg/bg/suspend),
                       which Android app contexts do not provide
  all                  builtins-only language semantics, no premise
  unknown              premise genuinely doubtful from content alone

Rules are deliberately conservative: strong signals only, in the order
below. Hand-adjudicated exceptions are listed in REPORT.md.
"""
import re

EXT_UTILS = {
    "grep", "sed", "awk", "sort", "tr", "cat", "ls", "od", "head", "tail",
    "wc", "cut", "find", "xargs", "date", "stat", "mkdir", "rmdir", "touch",
    "cp", "mv", "rm", "ln", "basename", "dirname", "mktemp", "uniq", "paste",
    "join", "comm", "diff", "tee", "env", "printenv", "seq", "expr", "sleep",
}

RULES = [
    ("linux-only", "procfs/sysfs path",
     re.compile(r"/proc\b|/sys/")),
    ("android-constrained", "controlling-terminal job control (fg/bg/suspend)",
     re.compile(r"(^|[;&|]\s*)(fg|bg|suspend)\b")),
    ("posix", "/dev/tty premise",
     re.compile(r"/dev/tty")),
    ("posix", "symlink creation (ln -s)",
     re.compile(r"\bln\s+-\w*s")),
    ("posix", "signal semantics (kill/trap on real signals)",
     re.compile(r"\bkill\s+-[A-Z0-9]|\btrap\b[^;]*\b(SIG)?(STOP|CONT|CHLD|USR1|USR2|WINCH|HUP|TERM|PIPE|ALRM)\b")),
    ("posix", "/dev/fd fd filesystem",
     re.compile(r"/dev/fd")),
    ("posix", "job/process control (set -m, wait, $!, jobs)",
     re.compile(r"set\s+-[a-z]*m\b|\bwait\b|\$!|(^|[;&|]\s*)jobs\b")),
    ("posix", "process identity semantics ($$, $PPID, BASHPID)",
     re.compile(r"\$\$|\$PPID|\bBASHPID\b")),
    ("posix", "procsub-fed file descriptor",
     re.compile(r"\bexec\s+\d*[<>][^;]*<\(")),
    ("unknown", "stdin fd duplication semantics (exec n<&0)",
     re.compile(r"\bexec\s+\d+<&0")),
]


def classify_platform(script):
    """Return (platform, rule) for a case script."""
    for value, rule, pat in RULES:
        if pat.search(script):
            return value, rule
    words = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", script))
    if words & EXT_UTILS or "/dev/null" in script:
        return "windows-ok", "portable premises only (cwd files, /dev/null, bundled utilities)"
    return "all", "builtins-only language semantics"
