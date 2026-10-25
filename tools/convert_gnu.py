#!/usr/bin/env python3
"""Convert GNU bash 5.3 official test files into diffcorpus cases (pilot).

Conversion rules (format only; assertion content is never edited):
  1. The .tests file is kept whole, including its GPL header comment block
     (comments are inert under -c; this preserves both byte-fidelity and
     the FSF license notice — see REPORT.md for the licensing note).
  2. A line of the exact form  ${THIS_SH} ./<name>.sub  is replaced by the
     .sub file's content wrapped in a subshell:  ( <content> )
     Rationale: GNU runs the .sub as a child script of the shell under test
     (fresh process, no state leaks back); a subshell gives the same
     isolation and stdout ordering under our single -c invocation.
  3. Any remaining ${THIS_SH} / $THIS_SH becomes @@SELF@@, which runner.py
     substitutes with the binary under test (THIS_SH's exact role).

Output: cases-gnu/<name>.py with CASES = [("gnu-<name>", "gnu", script)].
Each conversion is recorded in gnu-tests-manifest.json (pilot: true,
transforms list, right_md5 of the paired .right golden).
"""
import hashlib, json, os, re, sys

HOME = os.path.expanduser("~")
TESTS = f"{HOME}/workspace/rubash-audit/build-gnu/bash-5.3/tests"
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PILOT = ["invert", "strip", "casemod", "herestr", "appendop", "set-x"]

SUB_LINE = re.compile(r"^\s*\$\{THIS_SH\}\s+\./([A-Za-z0-9_-]+\.sub)\s*$")


def convert(name):
    with open(os.path.join(TESTS, name + ".tests"), encoding="utf-8", errors="replace") as f:
        raw = f.read()
    transforms = ["keep file whole (GPL header comments are inert)"]
    body = raw.rstrip("\n")
    out_lines = []
    for line in body.split("\n"):
        m = SUB_LINE.match(line)
        if m:
            sub = m.group(1)
            with open(os.path.join(TESTS, sub), encoding="utf-8", errors="replace") as f:
                content = f.read().rstrip("\n")
            out_lines.append("( " + content.replace("\n", "\n") + "\n)")
            transforms.append(f"inline {sub} as subshell")
        else:
            out_lines.append(line)
    script = "\n".join(out_lines)
    if "THIS_SH" in script:
        script = script.replace("${THIS_SH}", "@@SELF@@").replace("$THIS_SH", "@@SELF@@")
        transforms.append("THIS_SH -> @@SELF@@")
    right = os.path.join(TESTS, name + ".right")
    right_md5 = None
    if os.path.exists(right):
        with open(right, "rb") as f:
            right_md5 = hashlib.md5(f.read()).hexdigest()
    return script, transforms, right_md5


def main():
    os.makedirs(os.path.join(PKG, "cases-gnu"), exist_ok=True)
    man_path = os.path.join(PKG, "gnu-tests-manifest.json")
    with open(man_path, encoding="utf-8") as f:
        man = json.load(f)
    by_name = {e["name"]: e for e in man["entries"]}
    for name in PILOT:
        script, transforms, right_md5 = convert(name)
        out = os.path.join(PKG, "cases-gnu", f"{name}.py")
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# diffcorpus GNU pilot case: gnu-{name} (from GNU bash 5.3 tests/{name}.tests)\n")
            f.write("# Converted by tools/convert_gnu.py; see gnu-tests-manifest.json for provenance.\n")
            f.write(f"CASES = [\n('gnu-{name}', 'gnu', {script!r}),\n]\n")
        e = by_name[name]
        e["pilot"] = True
        e["pilot_case_id"] = f"gnu-{name}"
        e["pilot_transforms"] = transforms
        e["right_md5"] = right_md5
        print(f"gnu-{name}: {len(script)} chars, transforms: {transforms}")
    with open(man_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
