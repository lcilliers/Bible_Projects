# 2207 — Item 2: five utility fixes that need your decision

Escalation: #2207. Status: decision sought. Researcher, 2026-10-22 (verbatim): "Continue #2207 with
item 2: the 7 utilities with no config."

Item 2 covers the 7 utilities that validate reports as reading no config
(`outputs/configs/CONFIG-REPORT-v610-20261022.md`, section 0).

**Being built now, as you approved (v4 D4/D5/D11, v7, v9):**
- the batch monitoring is scrapped: `iba/app/lib/batchprogressreport.py`,
  `iba/app/ps/BatchProgress.ps1`, step `report.batch_progress`;
- `iba/app/lib/lexicalenrich.py` is retired, with the handlers of its two retired steps;
- the `iba/app/lib/taggingguidance.py` definitions move into config.

The rest, below, cannot be done as tabled. Checking the live code showed facts the approved table did
not have, and each fix now needs a choice. Nothing below is built.

## 1. `iba/app/lib/lexicalscope.py` — the table said retire it; three live steps use it

**What was found:** it turns a cluster, word, strong list or verse list into verse ids. Live callers:
- step `lexical.meaning` (`iba/app/handlers/lexical.py` `meaning`);
- step `lexical.relational` (`relational`);
- step `cluster.subgroup` (`iba/app/handlers/cluster.py` `subgroup`);
- `iba/app/lib/clusterstatus.py` (`resolve_strongs`).

All four steps are active (`cfg_step.inactive=0`). It is pure SQL over `span`, `cluster_strong` and
`word_strong`, with no literal that is a setting.

Retiring it would break those steps. Your D6 answer ("sadly another idea that never worked") was
given against my description, which named it as part of the retired `lexical.run` path. That
description was wrong.

| Option | Effect |
|---|---|
| a. Keep it; mark it `config_exempt` with the reason "pure SQL resolver, nothing to configure" | The finding clears; nothing changes in behaviour |
| b. Keep it; move its table names into config | A change for the sake of the check, with no settings of value |
| c. Retire it with the three steps that depend on it | Ends `lexical.meaning`, `lexical.relational` and `cluster.subgroup` (study stages, on hold) |

Claude recommends **a**: the module has no real setting.

Decision: ____  Comment: ____

## 2. `iba/app/lib/batchcontrol.py` — not only monitoring

**What was found:** the table said the batch monitoring is scrapped and the batchcontrol calls come
out of `iba/app/handlers/cluster.py` and `iba/app/handlers/lexical.py`. But batchcontrol is also
the guard that skips a batch already committed (`already_committed`). That stops a re-run from
paying again for LLM calls already made. It is used by five live LLM steps: `lexical.meaning`,
`lexical.relational`, `cluster.subgroup`, `cluster.reading` and `cluster.answer`. It writes
`run_batch`.

The monitoring itself (the `report.batch_progress` report over `run_batch`) is scrapped now.

| Option | Effect |
|---|---|
| a. Keep batchcontrol as the skip-and-cost guard; only the progress report goes | No double spend on a re-run; `run_batch` stays as the guard's record |
| b. Remove batchcontrol too | Every re-run of those five steps calls the model again for work already done |

Claude recommends **a**. batchcontrol reads config already, so it is not one of the 7.

Decision: ____  Comment: ____

## 3. `iba/app/handlers/catalogue.py` — the table left a choice open

**What was found:** 38 lines. It checks `-ObsId` and `-Set`, then calls
`iba/app/lib/cataloguewrite.py`, which does the write. It has no literal that is a setting.

| Option | Effect |
|---|---|
| a. Mark it `config_exempt`: "thin step wrapper; the logic is in lib/cataloguewrite.py" (as `handlers/compliance.py` already is) | The finding clears; no code change |
| b. Fold its checks into `cataloguewrite.py` and point step `obs_catalogue.update` at a function there | One file fewer; cataloguewrite then imports the handler contract |
| c. Give it its own config | Nothing in it to configure |

Your D1 answer says a utility without config is a violation that needs a fix, not a count. Option a
is an exemption, so Claude does not pick it unasked. Claude recommends **a** all the same: the
wrapper has nothing to configure, and the same exemption is already in use.

Decision: ____  Comment: ____

## 4. `iba/app/lib/clusterfamilyscan.py` — no thresholds, and nothing runs it

**What was found:**
- No threshold: the only literals are the excluded cluster codes (`T2`, `T3`, `FLAG`) and the
  proper-noun morph patterns.
- No caller: no step, no PS script, no import. It is run only as `python -m`, which rules 41 and 43
  forbid.
- It was a candidate-finding aid for #1598, which is completed (v43, 2026-09-11).

| Option | Effect |
|---|---|
| a. Retire it to archive/ | The finding clears; the aid is gone (re-buildable from git if needed) |
| b. Keep it: a step, a PS script, and the excluded codes into `cfg_setting` | A registered tool for cluster-reallocation candidates (a study tool, on hold) |

Claude recommends **a**: it served a completed escalation and has no caller.

Decision: ____  Comment: ____

## 5. `scripts/backup_db_to_nas.py` — moving its constants into config adds a risk

**What was found:**
- The backup is working: both nightly runs report OK on 2026-10-21
  (`C:\Users\lerouxc\nas_mirror_logs\status_dbbackup.txt`, `status_dbbackup_iba.txt`).
- Its constants are the source path, the NAS target, the log name, the three retention tiers, the
  minimum sizes and the local status folder.
- Moving them into `cfg_setting` means every backup must first read `iba.db`. That includes the
  backup of `iba.db` itself. If `iba.db` cannot be opened, the backup that should protect it fails
  too.

| Option | Effect |
|---|---|
| a. Constants into `cfg_setting`; if `iba.db` cannot be read, the backup uses the built-in values and logs that it did | Config governs it; the backup still runs when iba.db is broken |
| b. Constants into `cfg_setting`, no fallback | Simplest; a broken iba.db stops both backups |
| c. Keep the constants in the script; mark it `config_exempt` with the reason "backup must not depend on the database it protects" | No dependency; the rule-of-config exception is stated |

Claude recommends **a**.

Decision: ____  Comment: ____
