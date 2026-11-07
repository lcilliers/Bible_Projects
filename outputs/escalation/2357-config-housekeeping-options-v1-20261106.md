# #2357 config housekeeping: what each finding is and the options

Source: `outputs/configs/CONFIG-REPORT-v706-20261106.md` section 0 (live validate run RUN-20261106_183155_872-CONFIGMAINT). Coherence passes; these are advisory. Nothing has been changed. Evidence below is from reading the code and `cfg_setting` this session; the reading of intent behind each is inferential (B:4).

The 17 unenforced behaviour rules (items 8 to 24) are a standing baseline, the same 17 fingerprints in every run since 2026-11-01, each with its own `enforced_by` reason. They are not housekeeping and are left out here.

## Orphan settings (items 1 to 3): no code reads them

| # | setting | what it says | found in | options |
|---|---|---|---|---|
| 1 | `reading.whole_cluster_reading_start` | a cluster scope starts with an overview of its subgroups | only the archived migration `iba/app/migration/archive/config_alignment_2268_v1_20261024.py` | A keep, it records a rule as config and is not a code parameter. B retire (inactive=1). C wire a reader into the reading process (a build). |
| 2 | `glossary.currency_check` | glossary terms to check for currency; its `use` says the check is build B10 | only the archived migration `config_alignment_2268_v1_20261024.py` | A keep until build B10 exists. B retire. C build B10 (a build). |
| 3 | `ollama.max_codes_per_call` (8) | most codes of one surface judged in one call | only the archived migration `iba/app/migration/archive/surface_pair_verdict_2354_v1_20261102.py` | A keep, the judge port #2366 is expected to read it (inferential). B retire. |

## Low config density (items 4 and 5)

| # | module | what it is | options |
|---|---|---|---|
| 4 | `iba/app/lib/noderesolve.py` | no `cfg.` call of its own | A mark `cfg_utility.config_exempt=1` if it has no tunable value. B move its constants into config (a build). |
| 5 | `iba/app/lib/surfacebase.py` | no `cfg.` call of its own | same as 4 |

Unresolved: I did not read either module in full, so whether either holds a real tunable value is not established.

## Hand-rolled versioning (item 6)

`iba/app/lib/narrativeregister.py` builds `<stem>-vN-YYYYMMDD.md` itself (line 959) and parses it with its own pattern (line 350). The register owns narrative chapter files and their version bookkeeping, so this may be deliberate. Options: A accept as legitimate. B route it through `filingkit.versioned_path()` (a code change to the module that governs narrative chapters; B:78 applies).

## PS/worksheet drift (item 7)

`Node-Resolve.ps1` has no tab in `ps tools worksheet.xlsx`. Option: A add its tab through the app's worksheet tool. This is the one item with a single plain fix and no judgement in it.

## Decision

| item | decision (A / B / C) | note |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
