# 2207 — The 19 new config findings, with #2206 option 2b: what each is, and what to do

Escalations: #2207 (findings from `configmaint.validate` that are new since #2107 was
acknowledged) and #2206 option 2b (the low-config-density utilities). Status: for the researcher's
decision. Nothing changed yet.

Researcher, chat 2026-10-22 (verbatim): "2207 not ready for approval". #2207 gave counts only. This
file gives each finding, why its check exists, and a proposed action. Facts were checked 2026-10-22
against iba.db and the files.

## Summary

| Group | New findings | What they really are | Proposal | Kind |
|---|---|---|---|---|
| A. Escalation-file naming | 9 | Files in `iba/docs/archive/`. 20 of the check's 27 findings are archived files. | The check skips `archive/` folders; history is not renamed (rule 96) | Fix to a check |
| B. SQL scratch files | 2 | Your own untitled queries, 2026-10-14 | Name them, or archive them | Your files: your call |
| C. Rules with no control | 5 | Rules 76, 78, 81, 82, 97, each partially enforced | Count `partially_enforced` as having a control | Changes what #2206 option 2a counts |
| D. Utilities without config | 3 (12 with 2b) | Mixed: a retired script, a known non-compliance, false findings | Per row, table D | Mixed |

After A to D the check would show 0 new findings. These would remain: 4 orphan enums, 2 PS scripts
bypassing run.py, 7 live file-naming findings, and the 4 rules with no control at all. All of them
were acknowledged in #2107 or are tracked separately.

## A. Escalation-file naming: 9 new, all archived

**The check.** `find_escalation_file_naming_violations` enforces rule 64: an escalation's working
file starts with the escalation id.

**The new findings.** All 9 are in `iba/docs/archive/`, for example
`prose-management-iba-v1-20260822.md` (#784). They became findings when #2191 moved old docs into
archive. 20 of the check's 27 findings sit in an `archive/` folder.

**Why it is wrong to act on them.** An archived file is history, kept to be read deliberately
(rule 96). Renaming it changes history to satisfy a rule meant for live working files.

**Proposal A.** The check skips `archive/` folders. The 7 live findings stay. They were acknowledged
in #2107 and are the pre-#1007 backlog.

## B. Two untitled SQL scratch files

**The check.** `find_query_file_convention_violations` enforces rule 14: a kept query is named for
what it checks, and an answered one-off is archived.

| File | Content | Proposal |
|---|---|---|
| `scripts/SQLite/IBA_DB/Untitled-1.sqlite3-query` | `SELECT * FROM "cluster";` | Archive it: a one-off browse |
| `scripts/SQLite/IBA_DB/Untitled-2.sqlite3-query` | escalation joined to escalation_thread_item (id, type, item, note, status, value) | Keep it, renamed `escalation-thread-items.sqlite3-query` |

These are your files, so Claude changes nothing without your answer.

## C. Five rules newly listed as having no control

**The check.** `find_unenforced_behaviour_rules`, changed by #2206 option 2a. It lists rules
neither mechanically enforced nor context-delivered: `partially_enforced` (9),
`buildable_not_built` (3) and `deliberately_deferred` (1).

**The 5 new ones:**

| Rule | Name | Its partial control today |
|---|---|---|
| 76 | narrative-claim-register-kept-in-iba-db | `Narrative-Register.ps1` is the only writer |
| 78 | narrative-chapters-change-only-through-the-register | `Narrative-Register.ps1` (AddChapter/EditChapter) |
| 81 | session-compliance-restated-and-proved | The compliance start check and SC6 |
| 82 | session-close-blocks-commit-on-open-findings | `Session-Close.ps1` exits 3 |
| 97 | developer-mode-scope-and-conduct | The entry gate hook; `apply_logged` |

They appear now, not in #2107, because they were classified `partially_enforced` after #2107.

**What is not right.** A partially enforced rule has a control, so "no control" overstates it. All
13 also reach Claude at their point of use since #2209.

**Proposal C.** The list counts only `buildable_not_built` and `deliberately_deferred`: 4 rules (66,
60, 68 and 46), the real gaps.

## D. Utilities with no config reads (3 new; with 2b, all 12)

**The check.** `find_utility_config_density` enforces `governance.utility.config` (each utility is
config-driven). It counts `Cfg` method calls only.

| # | Utility | New? | Fact (checked 2026-10-22) | Proposal |
|---|---|---|---|---|
| 1 | scripts_apply_session_patch (`scripts/apply_session_patch.py`) | new | Its own purpose says INACTIVE since 2026-08-18 (#729, your ruling), yet `cfg_utility.inactive` is 0 and the file is live. #729 is no longer in the escalation table. | Apply the ruling: set inactive, move the file to `scripts/archive/` |
| 2 | scripts_backup_db_to_nas (`scripts/backup_db_to_nas.py`) | new | Marked NON-COMPLIANT, hardcoded constants (#648). #648 is no longer in the escalation table, so the item is tracked nowhere. | Raise a new task: move its constants into cfg_setting |
| 3 | taggingguidance (`iba/app/lib/taggingguidance.py`) | new | Reads cfg tables by SQL (2 references); the check does not see SQL reads | Covered by Question E |
| 4 | handlers_catalogue | | A 38-line adapter over cataloguewrite.py | Exempt: its callee holds the rules |
| 5 | lexicalenrich | | Used only by the `enrich` handler of step `lexical.enrich`, which you retired (#1753) | Retire it with that handler |
| 6 | lexicalscope | | Built for `lexical.run`, which is inactive | Retire it with that step, if nothing live imports it |
| 7 | clusterfamilyscan | | Candidate generation from strong_related (#1598) | Claude checks its literals; exempt if none are thresholds |
| 8 | clusterstatus | | Reads config by SQL (4 references) | Question E |
| 9 | recordingpass | | Reads config by SQL (12 references) | Question E |
| 10 | batchcontrol | | Reads config by SQL (3 references) | Question E |
| 11 | batchprogressreport | | A read-only report over run_batch | Exempt |
| 12 | observationenhancer | | Reads config by SQL (4 references) | Question E |

**Question E.** Should the check count SQL reads of `cfg_*` tables as config use? Claude
recommends yes. It is a defect in the check, fixed once, and it clears 5 false findings for good.

## Your decision

| Item | Approve / reject / revise | Comment |
|---|---|---|
| A: the naming check skips archive/ |  |  |
| B: archive Untitled-1; rename Untitled-2 |  |  |
| C: "no control" counts buildable and deferred only |  |  |
| D1: retire apply_session_patch (your 2026-08-18 ruling) |  |  |
| D2: new task for backup_db_to_nas constants |  |  |
| D4, D11: exempt |  |  |
| D5, D6: retire with their retired steps |  |  |
| D7: check literals, then exempt |  |  |
| E: the check counts SQL reads of cfg tables |  |  |
