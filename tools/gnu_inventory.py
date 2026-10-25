#!/usr/bin/env python3
"""Inventory of the GNU bash 5.3 official test suite (oracle's own tests).

Source (read-only): ~/workspace/rubash-audit/build-gnu/bash-5.3/tests/
Emits gnu-tests-manifest.json next to the package root and prints class counts.

Harness contract (from run-* scripts): ${THIS_SH} ./X.tests > out 2>&1, then
diff out X.right. I.e. GNU's own check is a merged-stream (stdout+stderr)
golden diff; exit code is not compared. Our package protocol (separate
stdout/stderr/exit, live oracle) is stricter; conversion notes live in
REPORT.md.

Classes (name + content markers; heuristics documented in REPORT.md):
  C = excluded/annotated for now (premise missing or interactive/harness-bound)
  B = convertible with converter work (THIS_SH/.sub/fixtures/recho helpers)
  A = directly convertible (self-contained, deterministic)
"""
import json, os, re

HOME = os.path.expanduser("~")
TESTS = f"{HOME}/workspace/rubash-audit/build-gnu/bash-5.3/tests"
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# name-based class C: premise not satisfiable in our -c differential protocol
CLASS_C = {
    "dbg-support": "needs a debugger-enabled bash build (oracle build lacks it)",
    "dbg-support2": "needs a debugger-enabled bash build (oracle build lacks it)",
    "intl": "dedicated locale suite; needs specific locales installed",
    "history": "interactive history/readline premise",
    "histexp": "interactive history expansion premise",
    "complete": "interactive completion/readline premise",
    "jobs": "interactive job control (fg/bg/suspend, tty)",
    "invocation": "startup-file/login-shell harness premise",
    "rsh": "restricted-shell invocation harness premise",
}

# rough topic overlap with the package's 29 domains (by GNU file topic)
OVERLAP = {
    "array": "array", "assoc": "array", "appendop": "array", "quotearray": "array",
    "arith": "arith", "arith-for": "arith",
    "exp": "param", "more-exp": "param", "new-exp": "param", "rhs-exp": "param",
    "strip": "param", "tilde": "param", "tilde2": "param", "dynvar": "param",
    "vredir": "param", "varenv": "env", "nquote": "quote", "nquote1": "quote",
    "nquote2": "quote", "nquote3": "quote", "nquote4": "quote", "nquote5": "quote",
    "iquote": "quote", "quote": "quote", "casemod": "param", "case": "case",
    "glob": "glob", "globstar": "glob", "glob-bracket": "glob", "extglob": "glob",
    "extglob2": "glob", "extglob3": "glob", "posixpat": "glob",
    "redir": "redir", "heredoc": "redir", "herestr": "redir",
    "builtins": "builtin", "attr": "declare", "exportfunc": "func", "func": "func",
    "getopts": "getopts", "trap": "trap", "set-e": "trap", "cond": "builtin",
    "test": "builtin", "printf": "builtin", "read": "builtin", "mapfile": "builtin",
    "type": "builtin", "dstack": "cd", "dstack2": "cd", "alias": "builtin",
    "comsub": "quote", "comsub2": "quote", "comsub-eof": "quote",
    "procsub": "procsub", "coproc": "procsub", "lastpipe": "status",
    "ifs": "ifs", "parser": "syntax", "errors": "syntax", "precedence": "misc",
    "invert": "status", "shopt": "builtin", "set-x": "misc", "nameref": "func",
    "braces": "param",
}


def markers(text):
    return {
        "this_sh": len(re.findall(r"THIS_SH", text)),
        "recho": len(re.findall(r"\b[rz]echo\b", text)),
        "locale": bool(re.search(r"\b(LC_ALL|LC_[A-Z]+|LANG)=", text)),
        "tty": bool(re.search(r"/dev/tty|/dev/pt", text)),
        "subs": sorted(set(re.findall(r"([A-Za-z0-9_-]+\.sub)\b", text))),
        "fixtures": sorted(set(re.findall(r"([A-Za-z0-9_-]+\.(?:in|in1|in2|list|data))\b", text))),
        "bash_tstout": "BASH_TSTOUT" in text,
    }


def main():
    entries = []
    for name in sorted(os.listdir(TESTS)):
        if not name.endswith(".tests"):
            continue
        base = name[:-len(".tests")]
        with open(os.path.join(TESTS, name), encoding="utf-8", errors="replace") as f:
            text = f.read()
        right_path = os.path.join(TESTS, base + ".right")
        has_right = os.path.exists(right_path)
        right_lines = 0
        if has_right:
            with open(right_path, encoding="utf-8", errors="replace") as f:
                right_lines = sum(1 for _ in f)
        m = markers(text)
        if base in CLASS_C:
            cls, why = "C", CLASS_C[base]
        elif m["tty"]:
            cls, why = "C", "references /dev/tty or pty"
        elif m["this_sh"] or m["subs"] or m["fixtures"] or m["recho"] or m["bash_tstout"]:
            cls, why = "B", "needs converter transforms (THIS_SH/.sub/fixtures/recho/PATH helpers)"
        else:
            cls, why = "A", "self-contained"
        if m["locale"] and cls != "C":
            why += "; touches locale vars (class kept, locale sensitivity annotated)"
        entries.append({
            "name": base, "lines": text.count("\n") + 1, "has_right": has_right,
            "right_lines": right_lines, "class": cls, "class_reason": why,
            "markers": m, "overlap_domain": OVERLAP.get(base, ""),
            "pilot": False,
        })
    out = {"source": "GNU bash 5.3 official tests (build-gnu/bash-5.3/tests)",
           "oracle": "GNU bash 5.3.20", "files": len(entries), "entries": entries}
    with open(os.path.join(PKG, "gnu-tests-manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    from collections import Counter
    print("files:", len(entries), Counter(e["class"] for e in entries))
    print("no-right:", [e["name"] for e in entries if not e["has_right"]])
    print("A:", [e["name"] for e in entries if e["class"] == "A"])
    print("C:", [e["name"] for e in entries if e["class"] == "C"])


if __name__ == "__main__":
    main()
