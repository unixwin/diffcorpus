# diffcorpus MANIFEST

统一差分语料包：**306 条**主语料（audit 246 + hunt-r1 60），按领域分置于 `cases/`；
另设 GNU 官方测试集独立分区（盘点全量 83 文件，试点已转 6 条于 `cases-gnu/`，默认不加载，`--include-gnu` 启用）。
每条用例的期望均由 runner 在运行时对 GNU bash 5.3.20 oracle 现场比对得出（无存储金标）；
脚本内容与来源逐字一致（导入保真校验见 REPORT.md）。

## 领域分布（主语料）

| 领域 | 条数 |
|---|---|
| case | 31 |
| job | 29 |
| param | 25 |
| builtin | 24 |
| arith | 20 |
| glob | 17 |
| trap | 17 |
| array | 15 |
| misc | 15 |
| redir | 12 |
| status | 10 |
| func | 10 |
| ifs | 8 |
| quote | 8 |
| declare | 8 |
| env | 8 |
| subshell | 6 |
| pid | 5 |
| syntax | 5 |
| atrans | 4 |
| getopts | 4 |
| source | 4 |
| regex | 4 |
| unset | 3 |
| local | 3 |
| declarep | 3 |
| cd | 3 |
| meta | 3 |
| procsub | 2 |

## 领域名归一映射（cases2.py 第二批类别 → 基础领域）

param2→param、arith2→arith、glob2→glob、builtin2→builtin、misc2→misc、env2→env、trap2→trap；
原始类别逐条保留在下表「原类别」列与 manifest.json 的 `orig_category` 字段。断言脚本零改动。

## 去重合并映射

无合并。方法：全部 306 条按空白归一化脚本 MD5 两两比对（源内、跨源）+ 编号集合求交，
结果为零编号冲突、零脚本重复（详见 REPORT.md 盘点节）。话题相邻但测面不同者（如 mytests 中
附带使用 case 语句的 gl08/ms01–03/pid04/lc01 与 hunt 的 case 语义面）不构成重复，各自保留。

## 逐例清单（主语料）

| 编号 | 领域 | 原类别 | 测什么（来源文件分节） | oracle 期望来源 | 出处 |
|---|---|---|---|---|---|
| pe01 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe02 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe03 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe04 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe05 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe06 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe07 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe08 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe09 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe10 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe11 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe12 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe13 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe14 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe15 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe16 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe17 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe18 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe19 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pe20 | param | param | parameter expansion | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar01 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar02 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar03 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar04 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar05 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar06 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar07 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar08 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar09 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar10 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar11 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar12 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar13 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar14 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ar15 | arith | arith | arithmetic | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr01 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr02 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr03 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr04 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr05 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr06 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr07 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr08 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr09 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr10 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr11 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr12 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr13 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr14 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| arr15 | array | array | arrays | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs01 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs02 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs03 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs04 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs05 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs06 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs07 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ifs08 | ifs | ifs | IFS / splitting | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl01 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl02 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl03 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl04 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl05 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl06 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl07 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl08 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl09 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl10 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl11 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| gl12 | glob | glob | glob / extglob | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q01 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q02 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q03 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q04 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q05 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q06 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q07 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| q08 | quote | quote | quoting / cmdsubst | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd01 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd02 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd03 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd04 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd05 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd06 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd07 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd08 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd09 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd10 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd11 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| rd12 | redir | redir | redirection | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps01 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps02 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps03 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps04 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps05 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps06 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps07 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps08 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps09 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ps10 | status | status | pipeline / status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn01 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn02 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn03 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn04 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn05 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn06 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn07 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn08 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn09 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| fn10 | func | func | functions / scope / nameref | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts01 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts02 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts03 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts04 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts05 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts06 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts07 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts08 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts09 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts10 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts11 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ts12 | trap | trap | trap / set | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi01 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi02 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi03 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi04 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi05 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi06 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi07 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi08 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi09 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi10 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi11 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi12 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi13 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi14 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| bi15 | builtin | builtin | builtins | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc01 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc02 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc03 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc04 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc05 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc06 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc07 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| dc08 | declare | declare | declare attributes | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms01 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms02 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms03 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms04 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms05 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms06 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms07 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms08 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms09 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| ms10 | misc | misc | case / misc status | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb01 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb02 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb03 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb04 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb05 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| sb06 | subshell | subshell | subshell isolation | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| en01 | env | env | startup / env | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| en02 | env | env | startup / env | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| en03 | env | env | startup / env | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| en04 | env | env | startup / env | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| en05 | env | env | startup / env | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pr01 | procsub | procsub | process substitution | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pr02 | procsub | procsub | process substitution | GNU bash 5.3.20 现场差分 | audit-r1（cases.py） |
| pid01 | pid | pid | pid / identity semantics (boolean structure, not raw pids) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pid02 | pid | pid | pid / identity semantics (boolean structure, not raw pids) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pid03 | pid | pid | pid / identity semantics (boolean structure, not raw pids) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pid04 | pid | pid | pid / identity semantics (boolean structure, not raw pids) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pid05 | pid | pid | pid / identity semantics (boolean structure, not raw pids) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| at01 | atrans | atrans | @ transforms round 2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| at02 | atrans | atrans | @ transforms round 2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| at03 | atrans | atrans | @ transforms round 2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| at04 | atrans | atrans | @ transforms round 2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| un01 | unset | unset | unset / nameref semantics | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| un02 | unset | unset | unset / nameref semantics | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| un03 | unset | unset | unset / nameref semantics | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| lc01 | local | local | local options / dyn scope extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| lc02 | local | local | local options / dyn scope extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| lc03 | local | local | local options / dyn scope extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| go01 | getopts | getopts | getopts | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| go02 | getopts | getopts | getopts | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| go03 | getopts | getopts | getopts | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| go04 | getopts | getopts | getopts | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| so01 | source | source | source / exec -a etc | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| so02 | source | source | source / exec -a etc | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| so03 | source | source | source / exec -a etc | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| so04 | source | source | source / exec -a etc | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| tr201 | trap | trap2 | trap inheritance | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| tr202 | trap | trap2 | trap inheritance | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| tr203 | trap | trap2 | trap inheritance | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| tr204 | trap | trap2 | trap inheritance | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| tr205 | trap | trap2 | trap inheritance | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf01 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf02 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf03 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf04 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf05 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| mf06 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pf201 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pf202 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| pf203 | builtin | builtin2 | mapfile/read extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| rx01 | regex | regex | regex / [[ ]] extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| rx02 | regex | regex | regex / [[ ]] extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| rx03 | regex | regex | regex / [[ ]] extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| rx04 | regex | regex | regex / [[ ]] extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| gb201 | glob | glob2 | glob round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| gb202 | glob | glob2 | glob round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| gb203 | glob | glob2 | glob round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| gb204 | glob | glob2 | glob round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| gb205 | glob | glob2 | glob round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| dp01 | declarep | declarep | declare -p formats | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| dp02 | declarep | declarep | declare -p formats | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| dp03 | declarep | declarep | declare -p formats | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ax01 | arith | arith2 | arith round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ax02 | arith | arith2 | arith round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ax03 | arith | arith2 | arith round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ax04 | arith | arith2 | arith round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ax05 | arith | arith2 | arith round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| px01 | param | param2 | param round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| px02 | param | param2 | param round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| px03 | param | param2 | param round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| px04 | param | param2 | param round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| px05 | param | param2 | param round2 | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cd01 | cd | cd | cd/pushd/pwd | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cd02 | cd | cd | cd/pushd/pwd | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cd03 | cd | cd | cd/pushd/pwd | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cg01 | misc | misc2 | compgen/kill/jobs extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cg02 | misc | misc2 | compgen/kill/jobs extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cg03 | misc | misc2 | compgen/kill/jobs extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cg04 | misc | misc2 | compgen/kill/jobs extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| cg05 | misc | misc2 | compgen/kill/jobs extras | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| sx01 | syntax | syntax | syntax / parse errors (exit code focus) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| sx02 | syntax | syntax | syntax / parse errors (exit code focus) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| sx03 | syntax | syntax | syntax / parse errors (exit code focus) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| sx04 | syntax | syntax | syntax / parse errors (exit code focus) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| sx05 | syntax | syntax | syntax / parse errors (exit code focus) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| meta01 | meta | meta | $_ / FUNCNAME / caller / LINENO | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| meta02 | meta | meta | $_ / FUNCNAME / caller / LINENO | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| meta03 | meta | meta | $_ / FUNCNAME / caller / LINENO | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| env201 | env | env2 | time/ulimit/umask symbolic (non-exact values) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| env202 | env | env2 | time/ulimit/umask symbolic (non-exact values) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| env203 | env | env2 | time/ulimit/umask symbolic (non-exact values) | GNU bash 5.3.20 现场差分 | audit-r2（cases2.py） |
| ca01 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca02 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca03 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca04 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca05 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca06 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca07 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca08 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca09 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca10 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca11 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca12 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca13 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca13b | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca14 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca15 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca16 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca17 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca18 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca19 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca20 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca21 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca22 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca23 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca24 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca25 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca26 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca27 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca28 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca29 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| ca30 | case | case | A. case | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb01 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb02 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb03 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb04 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb05 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb06 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb07 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb08 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb09 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb10 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb11 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb12 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb13 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb14 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb15 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb16 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb17 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb18 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb19 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb20 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb21 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb22 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb23 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb24 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb25 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb26 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb27 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb28 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |
| jb29 | job | job | B. job control / wait | GNU bash 5.3.20 现场差分 | hunt-r1（cases_r1.py） |

## GNU 官方测试集分区

来源：GNU bash 5.3 官方 tests/（oracle 作者自带），共 83 个 .tests 文件；
收编分级 A（可直接转）13 / B（转换器处理后可转）58 / C（前提不满足，标注排除）12。
逐文件分级、标记与理由见 `gnu-tests-manifest.json`；评估全文见 REPORT.md「GNU 官方测试集收编评估」。

试点已转（cases-gnu/，编号 gnu-<name>）：

- `gnu-appendop` ← tests/appendop.tests（101 行，.right 28 行，变换：keep file whole (GPL header comments are inert); inline appendop1.sub as subshell; inline appendop2.sub as subshell）
- `gnu-casemod` ← tests/casemod.tests（130 行，.right 49 行，变换：keep file whole (GPL header comments are inert)）
- `gnu-herestr` ← tests/herestr.tests（81 行，.right 38 行，变换：keep file whole (GPL header comments are inert); inline herestr1.sub as subshell）
- `gnu-invert` ← tests/invert.tests（33 行，.right 10 行，变换：keep file whole (GPL header comments are inert)）
- `gnu-set-x` ← tests/set-x.tests（44 行，.right 72 行，变换：keep file whole (GPL header comments are inert); inline set-x1.sub as subshell; inline set-x2.sub as subshell）
- `gnu-strip` ← tests/strip.tests（36 行，.right 12 行，变换：keep file whole (GPL header comments are inert)）

