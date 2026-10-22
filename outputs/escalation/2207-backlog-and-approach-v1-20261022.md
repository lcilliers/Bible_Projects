# 2207 — The remaining backlog and how it is being built

Escalation: #2207 (v17). Status: a working note for the researcher's question, 2026-10-22 (verbatim):
"what is the backlog you are checking and how are you approaching it". Nothing new is built here.

## What "the backlog" is

It is the set of `configmaint.validate` findings that #2207 must clear, under the method you approved
in v7 (`outputs/escalation/2207-fix-not-count-v1-20261022.md`, parts 1 to 3). It is not the
escalation list. The live list is section 0 of `outputs/configs/CONFIG-REPORT-v609-20261022.md`,
written this session by validate run RUN-20261022_053616_882-CONFIGMAINT. Every other category in
that section is at 0.

| # | Finding (live count) | What clears it | Source of the decision |
|---|---|---|---|
| 1 | 2 PS scripts call code directly, not through `iba/app/run.py`: `iba/app/ps/Behaviour.ps1`, `iba/app/ps/VerseMeta.ps1` | Each dispatches through run.py; their steps registered in `cfg_step` | fix-not-count part 2 |
| 2 | 7 utilities read no config | Per utility, below | your D answers (v4) |
| 3 | 13 behaviour rules not fully controlled | Each rule's control completed, or the rule reworded to what code can hold | your C answer (v4) |
| 4 | Part 1 not yet on | Validate keeps only errors; the advisory tier and its counts go | fix-not-count part 1 |

Done before this note: A, B, E and the orphan enums (v9, v12); the 7 file renames (commit 316cfe3d);
the 7 cfg rows that named them (this session, BUILD.md sec 381, v17); part 3, the failed-call trap
(v9).

### Item 2, the 7 utilities

| Utility | Fix | Your answer |
|---|---|---|
| `scripts/backup_db_to_nas.py` | Its constants (paths, retention) move to `cfg_setting` | D2 "it need fixing" |
| `iba/app/lib/batchprogressreport.py` | Retired with the batch monitoring; the batchcontrol calls come out of `iba/app/handlers/cluster.py` and `iba/app/handlers/lexical.py` | D4, D11 "scrap it" |
| `iba/app/lib/lexicalenrich.py`, `iba/app/lib/lexicalscope.py` | Retired with their retired steps | D5, D6 "another idea that never worked" |
| `iba/app/lib/clusterfamilyscan.py` | Its hardcoded thresholds move to `cfg_setting`; one file, not a system-wide check | D7 |
| `iba/app/lib/taggingguidance.py` | Its definitions move into config (v9) | D1 "must lead to a fix" |
| `iba/app/handlers/catalogue.py` | Not settled: give it its own config, or fold it into `cataloguewrite.py`. See decisions below. | D1 |

### Item 3, the 13 rules

| Rule | Status today |
|---|---|
| 74 open-threads-carried-as-escalations; 76 narrative-claim-register-kept-in-iba-db; 81 session-compliance-restated-and-proved; 82 session-close-blocks-commit-on-open-findings; 97 developer-mode-scope-and-conduct; 32 no-hedge-in-complete-records; 56 naming-shape; 58 archiving-trigger; 78 narrative-chapters-change-only-through-the-register | partially enforced |
| 66 cluster-label-must-track-membership; 60 tool-report-path-vs-deliverable-document; 68 stage1-corrections-only-via-real-rerun | buildable, not built |
| 46 test-plan-per-module-utility | deliberately deferred |

Each rule's `enforced_by` text says what part is missing. The work per rule is to read that text,
then either build the missing check or propose a rewording that code can hold. Rules 59 and 60 also
carry dated amendment notes in `source`, which rule 96 keeps out of a live home (#2207 v17). They
are settled with this item.

## How it is being built

1. **One item at a time, smallest first.** Order: item 1, then item 2, then item 3, then item 4
   last. Part 1 makes every remaining finding a hard error, so it goes on only when the backlog is
   clear; otherwise validate would fail on known items in the meantime (v8).
2. **Each item:**
   - read the live state first;
   - write one Developer Mode migration plus any code change;
   - test on a `dbsnapshot.copy_db` copy (dry run, apply, re-run, one synthetic bad case);
   - apply live, then re-run validate;
   - BUILD.md section, comment on #2207.
   The 7 renamed-path rows were done this way this session.
3. **No new decisions taken inline (rules 44, 105).** Where a fix needs a choice that the approved
   method does not make, the work stops and the choice comes to you. Each choice is listed below.
4. **Hand-over.** When all four items are done and validate is clean under part 1, #2207 goes to you
   as ready_for_approval, with the test results per item.

## Decisions that will come to you

These are the points where the approved method leaves a choice open. None is asked yet; each comes
with its evidence when its item is reached.

- **`iba/app/handlers/catalogue.py`:** give it its own config, or fold it into `cataloguewrite.py`.
- **Rules that code cannot check:** each proposed rewording, for approval (fix-not-count part 2).
- **Rule 46 (test plan per module), deliberately deferred:** your C answer says partial controls
  mean the work is unfinished. Whether "deferred" stays allowed, or the rule gets a control.
- **Retiring code:** retiring `lexicalenrich`, `lexicalscope` and the batch monitoring changes
  `iba/app/handlers/cluster.py` and `iba/app/handlers/lexical.py`. If removing the calls changes
  anything those handlers do beyond the monitoring, it stops and comes to you first.
