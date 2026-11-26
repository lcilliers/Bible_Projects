# Session log 2026-11-26: Developer Mode, #2637 done-test and failure log

Session id: `1dc61df3-3564-4325-94ae-0a36c7540ce9` (Developer Mode, declared at start; compliance file `Logs/compliance/COMPLIANCE-20261126-1dc61df3.md`).

## 1. Scope

2026-11-26, Developer Mode. The researcher's challenge on the boast run (#2637: the read commands had been reported encoded and tested, yet needed 37 manual interventions) was answered. The done-test was put into governance (rule 138). A build plan for every read routine from grouping to 3.2 was written and approved, and the first unit of it (failure trapping) was built, tested on a copy and applied live.

## 2. Escalations

- #2637 v4 to v11: updated, in-progress. v4: the researcher's challenge recorded and Claude's account of the narrow claims. v5 and v6: plan handed over for approval (v6 corrects B2). v7: approved by the researcher with comments; G3 decided. v8: build started. v9: X5 and X8 built. v10: X4 sized and designed. v11: the researcher's messages in full and the close.
- #2619, #2620, #2621, #2628: untouched; acknowledged at each stop (#2621 and #2628 are built inside #2637).

## 3. Files

- `iba/app/migration/archive/encode_2637_done_test_v1_20261126.py` (new; applied and archived): cfg_behaviour_rule 138.
- `iba/app/migration/archive/encode_2637_failure_log_v1_20261126.py` (new; applied and archived): read_failure, cfg_on_fail refused routing, write grants.
- `iba/app/lib/readcommands.py`: `ReadNext`.
- `iba/app/handlers/collectionbuild.py`: ReadNext as ok; the `_logged` decorator and `_log_failure`.
- `iba/app/tools/temp_2637_failure_log_test_run.py` (new): 11 cases.
- `iba/app/BUILD.md`: entries 598 and 599.
- `iba/app/USER-GUIDE.md`: refusals kept in read_failure; ReadWords wording.
- `iba/docs/project-map.md`: read_failure and rule 138.
- `outputs/escalation/2637-build-plan-v3-20261126.md` (new; v1 and v2 in `outputs/escalation/archive/`).
- `outputs/escalation/2637-known-failures-catalogue-v1-20261126.md` (new).
- `outputs/escalation/2637-escalation-history-v1-20261126.md` (tool report).
- `Logs/compliance/COMPLIANCE-20261126-1dc61df3.md` (new).

## 4. Decisions

- Researcher: a read routine is complete only after an unaided run on a copy passes (cfg_behaviour_rule 138; `iba/app/migration/archive/encode_2637_done_test_v1_20261126.py`).
- Researcher: the plan approved with comments, covering all routines to 3.2, anticipation from past failures and error trapping for learning (#2637 v7; `outputs/escalation/2637-build-plan-v3-20261126.md`).
- Researcher: G3, a qualifier's occurrences may be nodes of a 3.1 qualification where the reading judges it bears on the working; none forced, none dropped without its reason (#2637 v7).
- Researcher: close and continue X4 in a fresh Developer Mode session (#2637 v11).
- Claude, from config: B2 is answered by GP-01 and GP-04 (#2637 v6).
- Claude, from config: C4, merge on the same meaning, conformed under B:98 (#2637 v6).
- Claude, self-correctable fix: refusals of the 19 read and record steps routed to report-continue and kept in read_failure (cfg_on_fail; `iba/app/BUILD.md` entry 599).

## 5. Open items

- #2637 (Claude): continue in Developer Mode with X4 (rule keys, 557 message fragments; design on #2637 v10), then X9, X3, X1, X2 per routine, X6, X7 and the B:138 runs.
- #2621, #2628 (Claude): built within #2637.
- #2620 (Claude): boast reading resumes in a standard session after the #2637 routines pass.
- #2619 (Claude): on hold.
- #2529, #2530 (Researcher): on hold.

## 6. Git

- Branch: `main`.
- Commit: `c1b3df7d` (session 20261126: Developer Mode -- #2637 done-test as rule 138, build plan v3 and known-failures catalogue, read refusals kept in read_failure (no escalation), session log).
- Push: first attempt failed (`Could not resolve host: github.com`); retried: `f52dac6c..c1b3df7d  main -> main` to `https://github.com/lcilliers/Bible_Projects.git`.
- Not committed: `iba/app/db/archive/iba-pre-rollback-thought-rerun-20261125.db` and `iba/app/db/archive/iba-restore-point-20261124T152322Z.db` (each about 1 GB, left by an earlier session; over GitHub's file limit).
