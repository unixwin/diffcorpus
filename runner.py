#!/usr/bin/env python3
"""diffcorpus unified differential runner.

Runs every case in cases/ against GNU bash 5.3.20 (the oracle) and a target
shell, comparing stdout/stderr/exit after normalisation. Expectations are
derived live from the oracle at run time; no stored goldens.

Usage:
  python3 runner.py --target rubash --rubash /path/to/rubash
  python3 runner.py --target niubash
  python3 runner.py --target gnu          # oracle self-check (package health)
  python3 runner.py --target rubash --only pe01

Env overrides: GNU_BASH, RUBASH, NIUBASH (same names as the original
rubash-audit runner). Writes results.json (no --target) or
results-<target>.json next to this file.

Failure annotation: KNOWN_STABLE ids are the adjudicated stable failure set
against current rubash master; they are reported as KNOWN, any other failure
as NEW. Exit code is 0 when there are no NEW failures, 1 otherwise.
"""
import importlib.util, json, os, re, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.expanduser("~/workspace/rubash-audit")
GNU = os.environ.get("GNU_BASH", f"{BASE}/gnu-bash-5.3.20/bin/bash")
RUB = os.environ.get("RUBASH", f"{BASE}/rubash/target/release/rubash")
NIU = os.environ.get("NIUBASH", f"{BASE}/niubash/target/release/niu")

KNOWN_STABLE = {"gl08", "ms10"}
TIMEOUT = 8


def load_all_cases(include_gnu=False):
    cases = []
    dirs = [os.path.join(HERE, "cases")]
    if include_gnu:
        dirs.append(os.path.join(HERE, "cases-gnu"))
    for cdir in dirs:
        if not os.path.isdir(cdir):
            continue
        for name in sorted(os.listdir(cdir)):
            if not name.endswith(".py") or name.startswith("__"):
                continue
            spec = importlib.util.spec_from_file_location(f"dc_{name[:-3]}", os.path.join(cdir, name))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            cases.extend(mod.CASES)
    ids = [c[0] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate case ids in package"
    return cases


def normalize(text, shell, tmp):
    if text is None:
        return ""
    out = text
    for pat in [shell, os.path.basename(shell), tmp]:
        if pat:
            out = out.replace(pat, "SHELL" if pat != tmp else "TMP")
    out = out.replace("rubash", "SHELL").replace("bash", "SHELL")
    out = re.sub(r"case-[A-Za-z0-9_]+", "case-X", out)
    out = re.sub(r"diffrun-[A-Za-z0-9_]+", "diffrun-X", out)
    out = re.sub(r"\d+m\d+\.\d+s", "TIME", out)
    out = re.sub(r"\b\d+\.\d{2}\b", "NUM", out)
    return out


def run_one(shell, script, tmp_root):
    work = tempfile.mkdtemp(prefix="case-", dir=tmp_root)
    home = os.path.join(work, "home")
    os.mkdir(home)
    s = script.replace("@@SELF@@", shell)
    env = {"LC_ALL": "C", "TZ": "UTC", "PATH": "/usr/bin:/bin", "HOME": home, "TERM": "dumb", "TMPDIR": work}
    try:
        p = subprocess.run([shell, "-c", s], cwd=work, env=env, capture_output=True, timeout=TIMEOUT)
        return {"stdout": normalize(p.stdout.decode("utf-8", errors="replace"), shell, work),
                "stderr": normalize(p.stderr.decode("utf-8", errors="replace"), shell, work),
                "exit": p.returncode, "timeout": False}
    except subprocess.TimeoutExpired as e:
        so = e.stdout.decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        se = e.stderr.decode(errors="replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
        return {"stdout": normalize(so, shell, work), "stderr": normalize(se, shell, work),
                "exit": None, "timeout": True}
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    args = sys.argv[1:]

    def opt(name, default=None):
        return args[args.index(name) + 1] if name in args else default

    target = opt("--target")
    gnu = opt("--gnu", GNU)
    if target == "niubash":
        rub, outname = NIU, "results-niubash.json"
    elif target == "gnu":
        rub, outname = gnu, "results-gnu.json"
    else:
        rub, outname = opt("--rubash", RUB), "results-rubash.json" if target else "results.json"
    only = opt("--only")
    outpath = opt("--out", os.path.join(HERE, outname))

    cases = load_all_cases(include_gnu="--include-gnu" in args)
    results = []
    tmp_root = tempfile.mkdtemp(prefix="diffrun-")
    npass = 0
    known_fail, new_fail = [], []
    for cid, cat, script in cases:
        if only and only not in cid and only not in cat:
            continue
        g = run_one(gnu, script, tmp_root)
        r = run_one(rub, script, tmp_root)
        same = (g["stdout"] == r["stdout"] and g["stderr"] == r["stderr"]
                and g["exit"] == r["exit"] and g["timeout"] == r["timeout"])
        if same:
            npass += 1
            tag = "PASS"
        elif cid in KNOWN_STABLE:
            known_fail.append(cid)
            tag = "FAIL(known-stable)"
        else:
            new_fail.append(cid)
            tag = "FAIL"
        results.append({"id": cid, "category": cat, "script": script, "pass": same,
                        "known_stable": (not same and cid in KNOWN_STABLE), "gnu": g, "rubash": r})
        print(f"{tag} {cid} ({cat})")
    shutil.rmtree(tmp_root, ignore_errors=True)
    nfail = len(known_fail) + len(new_fail)
    out = {"gnu": gnu, "rubash": rub, "total": len(results), "pass": npass, "fail": nfail,
           "known_stable_failures": known_fail, "new_failures": new_fail, "results": results}
    with open(outpath, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"TOTAL {len(results)} PASS {npass} FAIL {nfail} "
          f"(known-stable: {','.join(known_fail) or '-'}; new: {','.join(new_fail) or '-'})")
    return 1 if new_fail else 0


if __name__ == "__main__":
    sys.exit(main())
