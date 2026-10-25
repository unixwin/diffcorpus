#!/usr/bin/env python3
"""Render MANIFEST.md from manifest.json + gnu-tests-manifest.json."""
import json, os
from collections import Counter, OrderedDict

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(PKG, "manifest.json"), encoding="utf-8") as f:
    man = json.load(f)
cases = man["cases"]

lines = []
lines.append("# diffcorpus MANIFEST")
lines.append("")
lines.append(f"统一差分语料包：**{man['total']} 条**主语料（audit 246 + hunt-r1 60），按领域分置于 `cases/`；")
lines.append("另设 GNU 官方测试集独立分区（盘点全量 83 文件，试点已转 6 条于 `cases-gnu/`，默认不加载，`--include-gnu` 启用）。")
lines.append("每条用例的期望均由 runner 在运行时对 GNU bash 5.3.20 oracle 现场比对得出（无存储金标）；")
lines.append("脚本内容与来源逐字一致（导入保真校验见 REPORT.md）。")
lines.append("")
lines.append("## 领域分布（主语料）")
lines.append("")
lines.append("| 领域 | 条数 |")
lines.append("|---|---|")
for d, n in Counter(c["domain"] for c in cases).most_common():
    lines.append(f"| {d} | {n} |")
lines.append("")
lines.append("## 领域名归一映射（cases2.py 第二批类别 → 基础领域）")
lines.append("")
lines.append("param2→param、arith2→arith、glob2→glob、builtin2→builtin、misc2→misc、env2→env、trap2→trap；")
lines.append("原始类别逐条保留在下表「原类别」列与 manifest.json 的 `orig_category` 字段。断言脚本零改动。")
lines.append("")
lines.append("## 去重合并映射")
lines.append("")
lines.append("无合并。方法：全部 306 条按空白归一化脚本 MD5 两两比对（源内、跨源）+ 编号集合求交，")
lines.append("结果为零编号冲突、零脚本重复（详见 REPORT.md 盘点节）。话题相邻但测面不同者（如 mytests 中")
lines.append("附带使用 case 语句的 gl08/ms01–03/pid04/lc01 与 hunt 的 case 语义面）不构成重复，各自保留。")
lines.append("")
pcount = Counter(c.get("platform", "unknown") for c in cases)
lines.append("## 平台适用性分布（主语料）")
lines.append("")
lines.append("逐例标注该例隐含的平台前提，枚举：linux-only / posix / windows-ok / android-constrained / all，")
lines.append("拿不准标 unknown。判定方法（内容规则 + 个别手判）与逐例命中规则见 REPORT.md §3.1 与")
lines.append("manifest.json 的 `platform` / `platform_rule` 字段；分类器在 `tools/platform_classify.py`，可再生。")
lines.append("")
lines.append("| 平台 | 条数 |")
lines.append("|---|---|")
for p in ["all", "windows-ok", "posix", "android-constrained", "linux-only", "unknown"]:
    if pcount.get(p):
        lines.append(f"| {p} | {pcount[p]} |")
lines.append("")
lines.append("## 逐例清单（主语料）")
lines.append("")
lines.append("| 编号 | 领域 | 原类别 | 平台 | 测什么（来源文件分节） | oracle 期望来源 | 出处 |")
lines.append("|---|---|---|---|---|---|---|")
for c in cases:
    sec = c["section"].replace("|", "/")
    lines.append(f"| {c['id']} | {c['domain']} | {c['orig_category']} | {c.get('platform', 'unknown')} | {sec} | GNU bash 5.3.20 现场差分 | {c['source']}（{os.path.basename(c['source_file'])}） |")
lines.append("")
lines.append("## GNU 官方测试集分区")
lines.append("")
gpath = os.path.join(PKG, "gnu-tests-manifest.json")
if os.path.exists(gpath):
    with open(gpath, encoding="utf-8") as f:
        g = json.load(f)
    cnt = Counter(e["class"] for e in g["entries"])
    lines.append(f"来源：GNU bash 5.3 官方 tests/（oracle 作者自带），共 {g['files']} 个 .tests 文件；")
    lines.append(f"收编分级 A（可直接转）{cnt['A']} / B（转换器处理后可转）{cnt['B']} / C（前提不满足，标注排除）{cnt['C']}。")
    lines.append("逐文件分级、标记与理由见 `gnu-tests-manifest.json`；评估全文见 REPORT.md「GNU 官方测试集收编评估」。")
    lines.append("")
    lines.append("试点已转（cases-gnu/，编号 gnu-<name>）：")
    lines.append("")
    for e in g["entries"]:
        if e.get("pilot"):
            lines.append(f"- `gnu-{e['name']}` ← tests/{e['name']}.tests（{e['lines']} 行，.right {e['right_lines']} 行，变换：{'; '.join(e.get('pilot_transforms', []))}）")
    lines.append("")
with open(os.path.join(PKG, "MANIFEST.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")
print(f"MANIFEST.md written: {man['total']} case rows")
