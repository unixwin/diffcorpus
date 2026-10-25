# diffcorpus 整合报告

日期：2026-10-25。落点：`~/workspace/diffcorpus/`（新建本地 git 仓，仅本地提交，未推送）。
oracle：GNU bash 5.3.20（`~/workspace/rubash-audit/gnu-bash-5.3.20/bin/bash`）。

## 1. 盘点（逐源）

| # | 来源 | 形态 | 数量 | 收编 | 说明 |
|---|---|---|---|---|---|
| S1 | `rubash-audit/mytests/`（cases.py 168 + cases2.py 78） | Python 元组表 `(id, 类别, 脚本)`，`-c` 差分，runner `--target rubash/niubash` | **246** | ✅ 246 | 审计第一/二轮原创语料；7 条用 `@@SELF@@` 占位 |
| S2 | `rubash-hunt-runs/2026-10-25-r1/`（cases_r1.py） | 同上元组形态，runner_r1（超时 8s、归一化较弱） | **60**（case 31 + job 29） | ✅ 60 | 找茬 r1 案头设计、oracle 单侧校验过 |
| S2' | `rubash-hunt-runs/2026-10-25-r2/` | 与 r1 **逐字节相同**的副本（md5 一致） | 0 新 | — | r2 只是借 r1 用例实测（60/60 SAME），不重复收编 |
| S3 | `rubash-hunt2/`（第二轮黑盒找茬，2026-10-24） | 独立 `.sh` 探针脚本（文件调用形态）+ 双跑产物（.rub.out/.err/.rc） | **405**（h1 词法/引用 52、h2 展开 70、h3 内建 54、h4 执行/控制流 118、h5 I/O/进程 62、h6 niu 产品面 49） | ❌ 本轮不收 | 见 §2 判定 |
| S4 | 修复簇单点矩阵：fix5 errpath `matrix.sh` 51 探针（金标式）、`matrix1520.py` 21 形（自定义调用模式差分）、errpath2 逐 issue 探针；fix4 dcl `z2-matrix.sh` 40 形（#1364）、sig `matrix.py`、lex `run-matrix.sh`、bf-* 探针等 | 单 issue 验证矩阵（金标或 duel 脚本） | ≥6 套具名矩阵 | ❌ 不收 | 内容已按回归规矩转成仓内带 issue 号回归测试；形态与本包 `-c` 现场差分协议不同（金标/文件调用/专用模式），硬转有语义漂移风险 |
| S5 | 修复簇克隆内含的 rubash 仓自有资产：`scripts/regression-catalog/cases/issue-*.sh`（46 份唯一）、`tests/regression/fixtures/*-matrix.sh` + `golden/*.gnu.out/.err` | 仓内回归资产 | — | ❌ 不收 | 本就在 rubash 仓内版本化，收编即重复 |
| S6 | mytests 附带 `probes-niu.sh` | niu 宿主面探针脚本（对照 niu 文档宣称） | 1 脚本 | ❌ 不收 | 宿主面、非引擎差分形态 |
| S7 | GNU bash 5.3 官方测试集 | `.tests` + `.right` 金标对 | 83 文件 | 🟡 试点 6 | 专节 §5 |

## 2. 收编判定（S3 hunt2 的 405 探针）

不收编，理由：①形态为**文件调用**探针，其汇总报告（CONSOLIDATED.md）明确注明部分分歧仅在脚本文件调用下触发，批量转 `-c` 语料会改变调用语义、违反「整合不改断言语义」；②405 条逐条人工复核调用前提（stdin/文件依赖/宿主面）是独立工程量，h6 的 49 条更是 niu 宿主面而非引擎面；③其 72 条发现（46 根因）已全部走 issue 并在修复时按规矩钉入仓内回归套件，行为资产未丢失。建议：若后续要收，按猎手面分批做「文件调用形态」的第二 runner 协议（脚本文件 + 合并流比对）再转，不要塞进 `-c` 协议。这与 §5 GNU 源的处置模式一致：先盘点 + 试点，全量转换另行裁定。

## 3. 整合结果

- **总量 306 条，29 个领域**（`cases/<领域>.py`，每文件导出 `CASES` 元组表）。
- 领域分布：case 31、job 29、param 25、builtin 24、arith 20、glob 17、trap 17、array 15、misc 15、redir 12、status 10、func 10、ifs 8、quote 8、declare 8、env 8、subshell 6、pid 5、syntax 5、atrans 4、getopts 4、source 4、regex 4、unset 3、local 3、declarep 3、cd 3、meta 3、procsub 2。
- **去重**：全部 306 条做空白归一化脚本 MD5 两两比对（源内 + 跨源）+ 编号集合求交——**零编号冲突、零脚本重复、零合并**（MANIFEST 设映射节并注明为空）。话题相邻但测面不同者保留双方：如 mytests 附带使用 case 语句的 gl08/ms01–03/pid04/lc01、附带使用 wait 的 ps04/ps06/cg03，与 hunt 的 case/job 专测面不构成重复。
- **命名归一**：cases2.py 的第二批类别（param2/arith2/glob2/builtin2/misc2/env2/trap2）折入基础领域，原类别逐条保存在 MANIFEST 与 manifest.json `orig_category`。
- **保真**：导入后逐条与源元组做字节比对，306/306 一致（脚本断言零改动；`tools/import_sources.py` 可再生）。
- **MANIFEST**：`MANIFEST.md`（306 行逐例：编号/领域/原类别/测什么分节/oracle 期望来源/出处）+ `manifest.json`（含脚本 MD5 与源文件路径）。
- **runner**：统一入口 `runner.py`——沿用既有 `--target rubash|niubash` 口径与 `GNU_BASH/RUBASH/NIUBASH` 环境变量名、结果文件命名（results-<target>.json）；隔离临时目录、固定环境、stderr 归一化（取两代 runner 的强归一化集）；超时 8s（取 hunt 代，较 audit 代 5s 宽松，语义影响仅为慢用例容忍度）；失败集标注 `KNOWN_STABLE = {gl08, ms10}`，输出分 known-stable / new 两栏，有 new 失败退出码 1；`@@SELF@@` 替换保留；`--include-gnu` 时加载 GNU 试点分区。

## 3.1 平台适用性标注（MANIFEST 逐例字段）

背景：用户定调这批语料将来要在 Windows / Linux / macOS / Android 都跑，平台前提现在不标、将来全是返工。
故 MANIFEST 逐例增加 `platform` + `platform_rule`（命中规则）两字段，取值枚举：

| 取值 | 含义 |
|---|---|
| `all` | 纯内建语言语义，无平台前提 |
| `windows-ok` | 无 POSIX 独有机制；至多用到可移植前提（cwd 内文件、/dev/null、随包 coreutils 类工具），rubash + winuxcmd 在 Windows 上可满足 |
| `posix` | 隐含 POSIX 机制前提（信号、作业/进程控制、符号链接、进程身份、procsub fd、/dev/fd、/dev/tty） |
| `android-constrained` | 需要控制终端的作业控制（fg/bg/suspend）——Android 应用语境无控制终端 |
| `linux-only` | 依赖 Linux 特有面（/proc、/sys） |
| `unknown` | 仅凭内容无法判定前提 |

方法：内容规则分类器（`tools/platform_classify.py`，强信号才触发、按序首命中、逐例记录规则名），
辅以个案手判。规则序：/proc|/sys → linux-only；fg/bg/suspend → android-constrained；/dev/tty、ln -s、
kill/trap 真信号、set -m/wait/$!/jobs、$$/$PPID/BASHPID 身份语义、procsub 喂 fd → posix；
`exec n<&0`（stdin fd 复制语义，Windows 控制台映射存疑）→ unknown；
其余用到外部工具或 /dev/null 者 → windows-ok；纯内建 → all。

**主语料分布（306）**：all **200**、windows-ok **65**、posix **38**、android-constrained **2**（jb20、jb21）、
linux-only **0**、unknown **1**（mf06，占 **0.33%**）。

- posix 38 的构成：作业/进程控制 30、信号语义 2（jb05、tr202）、符号链接 2（cd01、rx03）、
  进程身份 2（pid01、pid02）、procsub-fd 2（mf04、pr02）。抽查手判与规则命中一致。
- linux-only 为 0 是实测结果而非漏标：全 306 条无一引用 /proc、/sys、/dev/tty、
  mkfifo、chmod——这批语料的 POSIX 前提止步于机制层（信号/作业控制），未下沉到 Linux 特有面。
  将来在 Windows/Android 上跑，真正的移植面就是这 38 条 posix + 2 条 android-constrained，
  其余 265 条（all + windows-ok）无机制性障碍。
- unknown 仅 mf06 一条：`exec 3<&0; read -u 3 … < /dev/null` 同时押 stdin fd 复制与
  /dev/null 经 fd 读取两项语义，其 Windows 控制台映射是否等价无法从内容判定，留待真机实测裁定。

GNU 分区同法标注（逐文件 `platform` 字段，与收编分级并列）：posix 28、all 27、windows-ok 24、
android-constrained 4（history、histexp、complete、jobs——交互前提）、linux-only 0、unknown 0；
intl 单独标 posix（locale 前提）、dbg-support 两件标 posix（调试器构建前提）。

## 4. 校验（两跑 + 试点两跑）

校验对象与口径：

- 被测二进制：`~/workspace/rubash-150/integration/rubash/target/debug/rubash`（debug 构建）。
  其源码树 sha `1a526148f4a1c2161805d54b10e1d977f67f5ccb` 与校验时 GitHub master
  `ec279df1` 的 tree sha **逐字相等**（gh api 核实），即该二进制就是当前 master 内容的构建，
  无需另行构建——这也避开了当时 load≈10 的机器门控（构建门 load<7；本次零构建）。
- 环境：`env -i` 净化（剥 JARVIS_*）、`taskset -c 0` 绑核、runner 内串行。
- 结果文件：`results-validate-rubash.json` / `results-validate-gnu.json` /
  `results-validate-pilot-rubash.json` / `results-validate-pilot-gnu.json`（随仓提交）。

| 跑 | 总数 | 通过 | 失败集 |
|---|---|---|---|
| 主语料 × 当前 master | 306 | 304 | **{gl08, ms10}** |
| 主语料 × oracle 自检 | 306 | 306 | ∅ |
| GNU 试点 × 当前 master | 6 | 6 | ∅ |
| GNU 试点 × oracle 自检 | 6 | 6 | ∅ |

- **差异清单：零。** 主跑失败集与已定谳稳定集 {gl08, ms10} 精确吻合，无 new 失败；
  本轮高负载（load≈10）下亦无时序 flake 混入（ps06 等历史 flake 本轮均过）。
- hunt 的 60 条在新 master 上全过（其 r2 实测基线为旧 master b3269945，本轮等于在
  ec279df1 上补齐了这批的现行基线）。
- oracle 自检 306/306 证明包本身健康：每条用例对 oracle 确定性成立，失败只可能来自被测差异。
- `.right` 抽验：按 GNU 自家 harness 语义（文件调用、合并流）在临时目录实跑
  appendop/invert 两文件，oracle 输出与 `.right` **逐字节一致**（2/2），金标在本环境有效。
- 诚实标注：①被测为 debug 构建，历史稳定集本就以 debug 口径定谳，口径一致；
  ②GNU 试点六条按「低难度先行」挑选（见 §5），6/6 不代表 B 类全量难度。

## 5. GNU 官方测试集收编评估

来源：`~/workspace/rubash-audit/build-gnu/bash-5.3/tests/`（oracle 作者自带，GPL-3-or-later）。

### 5.1 清点

- `.tests` **83** 个文件、共 13,575 行；`.right` **87** 个、约 14.5k 行；`.sub` 片段 **451** 个；
  `run-*` 驱动脚本 88 个；另有 `*.in` 输入夹具、misc/ 等。
- 配对：82/83 有同名 `.right`；唯一例外 `precedence.tests` 的金标在 `prec.right`
  （由 run-precedence 驱动）。5 个「孤儿」`.right`（array2/dollar/exec/input/prec）均由
  run-* 以别名驱动，非缺失。
- 每 `.tests` 文件是**多断言脚本**（echo 标记分隔的几十个子检查），与我们的一例一断言
  粒度不同：收编粒度定为**一文件一条**（整文件差分），子断言级拆分留待全量转换时评估。

### 5.2 `.right` 形态与差分口径对接

GNU 自家协议（run-* 原文）：`${THIS_SH} ./X.tests > out 2>&1; diff out X.right`——
**stdout+stderr 合并成一条流**与金标文本 diff，**不比退出码**。
我们的协议：stdout/stderr **分开**比 + 退出码比 + oracle 现场生成期望（无金标）。
对接方式（试点已验证可行）：

1. 转换后沿用我们的协议（更严）：文件整体作为 `-c` 脚本在两壳跑，分开比三通道。
   通道分离会放大差异面（如 set -x 的 trace 在 stderr 的逐字比对），试点 set-x 已过，
   说明当前 master 在该面与 oracle 一致；后续文件若因通道分离出失败，属**协议性差异**
   需逐条裁定（差异可能真实，也可能是合并流原本掩盖的交错顺序差），不得为过而改断言。
2. `.right` 不进 runner，作**溯源与 oracle 侧抽验**用：manifest 逐文件记录其 MD5 与行数；
   本轮已抽验 2 文件与 oracle 实跑逐字节吻合（§4）。
3. 转换三变换（`tools/convert_gnu.py`，仅格式）：
   文件整体保留（含 GPL 头注释，注释在 `-c` 下惰性）；
   `${THIS_SH} ./X.sub` 行 → 子 shell 内联 `( X.sub 内容 )`（保持子进程隔离与输出顺序）；
   其余 `${THIS_SH}` → `@@SELF@@`（runner 替换为被测二进制，正是 THIS_SH 的角色）。

### 5.3 环境前提分级（逐文件在 gnu-tests-manifest.json）

启发式（文件名 + 内容标记）分三级，**A 13 / B 58 / C 12**：

- **C（标注排除，12）**：dbg-support、dbg-support2（需启用调试器的构建，本机 oracle 构建
  无此支持）、intl（专用 locale 套件，需装特定 locale）、history、histexp、complete
  （交互/readline 前提）、jobs（tty 作业控制、fg/bg）、invocation（启动文件 harness）、
  rsh（受限 shell 调用 harness）、errors、exportfunc、test（含 /dev/tty 引用）。
- **B（转换器处理后可转，58）**：含 THIS_SH 引用（59 文件）、`.sub` 依赖（55 文件）、
  recho/zecho 辅助命令（24 文件——C 语言辅助二进制在 GNU 构建树内，转换时须把其目录
  注入 PATH 或改写调用）、输入夹具 `*.in`（须随例物化到工作目录）、BASH_TSTOUT 引用等。
  现转换器已处理 THIS_SH 与 `.sub` 内联两项；夹具物化与 recho PATH 是全量转换前要补的两项。
- **A（可直接转，13）**：casemod、coproc、cprint、dstack、dstack2、extglob2、extglob3、
  ifs-posix、invert、posixexp2、posixpat、precedence（金标在 prec.right）、strip。
- locale 敏感标注：13 个文件在脚本内设置 LC_*/LANG（dstack、dynvar、errors、extglob、
  glob、glob-bracket、globstar、histexp、intl、posixpat、printf、quotearray、redir）；
  非 C 级者保留分级但在 manifest 里标注 locale 敏感——我们 runner 固定 LC_ALL=C，
  这类文件在 C locale 下的行为子集仍可差分，但其多 locale 面在本包协议下测不到，属已知盲区。

### 5.4 与 mytests 246 的重叠估计

- 话题映射：83 文件中 **67** 个可映射到本包既有 29 领域（逐文件映射在 manifest 的
  `overlap_domain`）；话题重叠高但**粒度与深度互补**：246 条是广度一例一断言，
  GNU 是单面深挖（一文件几十个子检查、共 13.6k 行），同话题下 GNU 的边界覆盖远厚于我们。
- GNU 独有、我们基本空白的面：**posix 模式族**（posix2/posixexp/posixexp2/posixpipe/
  ifs-posix/comsub-posix/posixpat 共 7 文件）、invocation/启动语义、errors 的诊断文案面、
  printf/read 的深水区。交互族（complete/histexp/history）是协议性盲区（C 级）。
- 结论：重叠是「同面不同深」，收编不产生语义重复；它把差分资产从「广度 306」补成「广度 + 深度」。

### 5.5 试点结果与全量转换成本

- 试点 6 条（invert、strip、casemod = A 级；herestr、appendop、set-x = B 级含 .sub 内联）：
  对当前 master **6/6**、oracle 自检 **6/6**。管线（库存 → 转换 → 分区加载 → 双跑）全程打通。
- 全量转换的真实成本不在转换器（再补夹具物化 + recho PATH 两项即可覆盖 B 级），
  而在**失败分诊**：每转一个文件，被测若出差异须逐条裁定是真分歧还是协议性差异
  （通道分离/文件调用语义差），这是按文件计的人工裁定量。建议次序：A 级 13 个先行
  （预期低分诊量），B 级按话题分批（先与在修面相关的 array/param/glob 批），C 级维持排除。
- ⚠️ **许可证**：`.tests/.right` 为 FSF 版权、GPL-3-or-later。试点转换刻意保留了文件头
  的 GPL 注释块；但若将来把 cases-gnu 分区**发布**（推任何远端），须按 GPL 要求附
  COPYING 与来源说明——落点裁定（§6）前该分区只留本地。

## 6. 落点建议（供主会话转用户裁定）

| 选项 | 利 | 弊 |
|---|---|---|
| A. 独立仓（如 unixwin/diffcorpus，与 shellbench 同模式） | 多目标资产（rubash/niubash/GNU/未来 shell）定位干净；GNU 分区的 GPL 义务可独立承载；版本节奏自有 | 多一个仓要维护 |
| B. rubash 仓 `tests/diffcorpus/` | 与引擎同仓、CI 就近 | 语料同时服务 niubash 与他壳，归属别扭；GPL 分区混入引擎仓增加许可证面 |
| C. 维持工作区本地包 | 零成本 | 无版本备份、无协作面，资产易失 |

**推荐 A**：本包与 shellbench 是同类「跨壳资产」（一个测性能、一个测行为），独立成仓
与既有先例一致；GNU 分区待许可证文本补齐后再随仓发布或单独剔除。在用户裁定前，
本包只在本地提交、不推送。

## 7. 包内文件

- `cases/` 29 个领域模块（306 条）、`cases-gnu/` 试点 6 模块
- `runner.py` 统一入口；`MANIFEST.md` / `manifest.json` / `gnu-tests-manifest.json`
  （逐例含平台适用性 `platform` / `platform_rule` 字段，见 §3.1）
- `tools/` 五个再生脚本（import_sources / gnu_inventory / convert_gnu / build_manifest_md / platform_classify）
- `results-validate-*.json` 四份校验原始结果、`validate.log`
- 本报告
