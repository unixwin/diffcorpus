# diffcorpus — 统一差分语料包

把散落在审计/找茬/修复工作区里的差分测试语料整合为一个成形资产包。
每条用例是一个 shell 片段，runner 将它分别交给 **GNU bash 5.3.20（oracle）**
与目标 shell 以 `-c` 非交互运行，归一化后逐项比对 stdout / stderr / 退出码 / 超时。
期望不落金标，全部由 oracle 在运行时现场给出。

## 构成

| 分区 | 来源 | 数量 |
|---|---|---|
| `cases/` | audit-r1/r2（原 rubash-audit/mytests 的 cases.py + cases2.py） | 246 |
| `cases/` | hunt-r1（原 rubash-hunt-runs/2026-10-25-r1，case 语义 + job 控制） | 60 |
| `cases-gnu/`（默认不加载） | GNU bash 5.3 官方 tests/ 试点转换 | 6 / 全量 83 文件待定 |

主语料按领域分文件（29 个领域），逐例出处、原始类别与分节见 `MANIFEST.md` /
`manifest.json`；GNU 分区的逐文件盘点见 `gnu-tests-manifest.json`。
整合与校验结论见 `REPORT.md`。

## 跑法

```bash
cd ~/workspace/diffcorpus
# 对 rubash（任意二进制）：结果写 results-rubash.json
python3 runner.py --target rubash --rubash /path/to/rubash
# 对 niubash：results-niubash.json（NIUBASH 环境变量可覆盖路径）
python3 runner.py --target niubash
# oracle 自检（包健康度，应全过）：results-gnu.json
python3 runner.py --target gnu
# 只跑子集 / 带上 GNU 试点分区
python3 runner.py --target rubash --rubash /path/to/rubash --only pe01
python3 runner.py --target rubash --rubash /path/to/rubash --include-gnu --only gnu-
```

环境变量 `GNU_BASH` / `RUBASH` / `NIUBASH` 可覆盖二进制路径（与原 audit runner 同名同义）。
每例隔离临时目录、固定 `LC_ALL=C TZ=UTC PATH=/usr/bin:/bin HOME=<tmp>`、超时 8s；
stderr 归一化二进制路径/名、临时目录随机后缀与时间数值后比较（真实差异保留）。

失败标注：`gl08`、`ms10` 是已定谳的稳定失败集，输出记为 `FAIL(known-stable)` 并单列；
其余失败记为 NEW。退出码：无 NEW 失败为 0，否则为 1。

## 再生

```bash
python3 tools/import_sources.py    # 从三源重建 cases/ + manifest.json（脚本逐字保真）
python3 tools/gnu_inventory.py     # 重建 gnu-tests-manifest.json
python3 tools/convert_gnu.py       # 重建 cases-gnu/ 试点六条
python3 tools/build_manifest_md.py # 重建 MANIFEST.md
```
