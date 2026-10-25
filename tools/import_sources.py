#!/usr/bin/env python3
"""Import differential case sources into the unified diffcorpus package.

Sources (read-only, never modified):
  A. ~/workspace/rubash-audit/mytests/cases.py + cases2.py   (246 cases, audit round 1+2)
  B. ~/workspace/rubash-hunt-runs/2026-10-25-r1/cases_r1.py  (60 cases, hunt r1; r2 copies are byte-identical)

Output: cases/<domain>.py modules exporting CASES = [(id, domain, script), ...]
plus manifest.json (per-case provenance) next to this package root.

Assertion scripts are copied byte-for-byte from the source tuples; the only
normalisation is the domain label: second-batch categories in cases2.py
(param2/arith2/glob2/builtin2/misc2/env2/trap2) fold into their base domain,
with the original category preserved in manifest.json as orig_category.
"""
import ast, hashlib, json, os, re, sys
from collections import OrderedDict

HOME = os.path.expanduser("~")
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCES = [
    ("audit-r1", f"{HOME}/workspace/rubash-audit/mytests/cases.py"),
    ("audit-r2", f"{HOME}/workspace/rubash-audit/mytests/cases2.py"),
    ("hunt-r1", f"{HOME}/workspace/rubash-hunt-runs/2026-10-25-r1/cases_r1.py"),
]

FOLD = {"param2": "param", "arith2": "arith", "glob2": "glob",
        "builtin2": "builtin", "misc2": "misc", "env2": "env", "trap2": "trap"}

FILE_HEADERS = ("Original differential cases", "Each entry:", "Round 2:",
                "Differential hunt round", "Faces:", "Each entry",
                "against GNU", "are NEVER", "equality tests")


def sections_of(path):
    """Map case id -> the section comment in effect where its tuple starts."""
    sec = {}
    current = ""
    tuple_re = re.compile(r'^\("([A-Za-z0-9]+)",\s*"([A-Za-z0-9]+)",')
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("#"):
                text = s.lstrip("#").strip().strip("-").strip()
                if text and not any(text.startswith(h) for h in FILE_HEADERS):
                    current = text
                continue
            m = tuple_re.match(s)
            if m:
                sec[m.group(1)] = current
    return sec


def load_cases(path):
    """Extract the CASES list literal from a source module without importing it."""
    with open(path, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=path)
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "").startswith("CASES"):
            return [tuple(x) for x in ast.literal_eval(node.value)]
    raise SystemExit(f"no CASES* assignment in {path}")


def main():
    by_domain = OrderedDict()
    manifest = []
    seen_ids = {}
    for tag, path in SOURCES:
        sec = sections_of(path)
        for cid, cat, script in load_cases(path):
            if cid in seen_ids:
                raise SystemExit(f"duplicate id {cid}: {seen_ids[cid]} vs {tag}")
            seen_ids[cid] = tag
            domain = FOLD.get(cat, cat)
            by_domain.setdefault(domain, []).append((cid, domain, script))
            manifest.append({
                "id": cid,
                "domain": domain,
                "orig_category": cat,
                "section": sec.get(cid, ""),
                "source": tag,
                "source_file": os.path.relpath(path, HOME),
                "script_md5": hashlib.md5(re.sub(r"\s+", " ", script).strip().encode()).hexdigest(),
                "oracle": "GNU bash 5.3.20 live differential (runner derives expectation from oracle at run time)",
                "merged_from": [],
            })
    for domain, cases in by_domain.items():
        out = os.path.join(PKG, "cases", f"{domain}.py")
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# diffcorpus domain: {domain} ({len(cases)} cases)\n")
            f.write("# Imported by tools/import_sources.py; scripts are byte-identical to their sources.\n")
            f.write("CASES = [\n")
            for cid, dom, script in cases:
                f.write(f"({cid!r}, {dom!r}, {script!r}),\n")
            f.write("]\n")
    with open(os.path.join(PKG, "manifest.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"total": len(manifest), "cases": manifest}, f, ensure_ascii=False, indent=1)
    print(f"imported {len(manifest)} cases into {len(by_domain)} domains")
    for d, cs in by_domain.items():
        print(f"  {d}: {len(cs)}")


if __name__ == "__main__":
    main()
