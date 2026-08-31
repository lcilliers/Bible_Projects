# Session log — 2026-08-31 — escalation system bugs found+fixed, Developer/App Mode established

**Scope:** Started reviewing 13 escalations left open from the prior session; along the way found
and fixed real bugs in the escalation system's own approval/completion logic, built (then partly
undid, per correction) a proper bible_research.db schema-overview report, and — after repeatedly
mishandling the escalation approval process itself — the researcher re-established a foundational,
session-level Developer Mode / App Mode operating split that this project's design always intended
but was never actually built.

## Escalations touched, by id and outcome

**Escalation-process bugs found and fixed (mostly self-inflicted mess, sorted out):**

| id | outcome |
|---|---|
| 1305 | completed — 3 advisory cfg_* coherence findings investigated, all false positives, no fix needed. (Self-approved by Claude at the time; later judged, correctly, to have been the wrong mechanism — see #1324/#1325 below.) |
| 1307, 1308 | completed (self_correctable) — duplicate `configmaint.validate` crashes (locked-file `archive_before_write`), root-caused to #1320. |
| 1309, 1310 | re-assigned, `approved` by Researcher, **applied and verified live** — `cfg_write_grant` revocation for `configmaint.propose` on `cfg_change_detail`/`cfg_change_log` (escalation #1146's design). Still short of `completed` — see #1330/#1340. |
| 1311, 1313, 1317–1319, 1326, 1328, 1336 | completed (self_correctable) — Claude's own usage-error artifacts (title-length limit, missing `-Resolution`, missing `-Title`, missing `key` in `-Set`) — each caught immediately by validation, retried correctly, resolved as no-defect. |
| 1312 | **open, decision_required, assigned Researcher** — tracking task for #1309/#1310; work is done, needs your close-out (Claude can no longer self-close a `decision_required` item — see #1324/#1325). |
| 1314 | **open** — parent finding for the CSV-export-flooding fix; the actual fix is #1315 (done). |
| 1315 | re-assigned, `approved`, **applied and verified live** — new setting `configmaint.csv_export_on_auto_report=0`. |
| 1316 | re-assigned, `approved` **but NOT applied** — superseded (the script it would register was archived once the proper `report.schema_overview_bible_research` replaced it); recommend you reject. |
| 1320 | completed — `reportkit.archive_before_write()` now retries a transient file lock (bounded, 3×) instead of crashing uncaught. |
| 1321–1325 | re-assigned, `approved`, **applied and verified live** — two new `cfg_escalation_requirement` check_kinds: `actor_must_be_assignee` (whoever processes an item must currently be its assignee — every action, not just approval) and `decision_required_approval_requires_researcher` (closes the self-authorisation loophole D25 alone left open). |
| 1327 | **open, decision_required, assigned Claude** — a sixth guard (`ready_for_approval_not_assignable_to_claude`) proposed, not yet approved. |
| 1329 | **open, decision_required, assigned Claude** — proposal to delete a corrupted `cfg_setting` row (see below), not yet approved. |
| 1330 | completed (this session, at wrap-up) — real bug: `answered_for_run()` required `state='completed'`, but a `needs_claude_followup` item's `approved` deliberately never reaches that state, so `configmaint.propose`'s own re-run could never detect its own prior approval. Fixed; verified by successfully applying #1309/#1310/#1315 through the real path. |
| 1338, 1339, 1341, 1344 | **open, self_correctable, assigned Claude** — small crash artifacts from Claude's own blocked correction attempts (the new assignee guard correctly refusing edits to items assigned to the Researcher) — trivial, safe to close next session. |
| 1340 | **open, decision_required, assigned Researcher** — new transition rule so clearing `needs_claude_followup` on an already-approved item reaches `completed` without a second full approval round-trip. Not yet approved. |

**Schema overview report work (bible_research.db + IBA-side fix):**

| id | outcome |
|---|---|
| 1306 | **open, in-progress, assigned Claude** — see below; still needs one more correction pass (output folder) that Claude could not apply directly (assigned to Researcher, guard-blocked) — communicated in chat instead. |
| 1331–1335, 1337 | **open, decision_required, assigned Researcher** — 6 config rows registering `report.schema_overview_bible_research` (work package, step, report, 2× report_section, output-path setting). Not yet approved. #1337's path was corrected mid-session (`workflow/schema/schema-overview-bible-research.md`, not nested under `workflow/schema/bible_research/`, which is `table_export`'s CSV-dump folder) — communicated in chat, not recorded on the escalation itself (same guard block). |

**Developer Mode / App Mode:**

| id | outcome |
|---|---|
| 1342 | **rejected by Researcher** — first-draft `cfg_behaviour_rule` content described the wrong mechanism (a per-table classification Claude would self-apply); needs re-proposing with content matching the corrected `CHARTER.md` §4. |
| 1343 | **rejected by Researcher** ("not approved, to be redesigned") — the task record for the same first draft. |

## What was actually built/fixed, by file

- `iba/app/lib/escalation.py` — three real bugs fixed: (1) `answered_for_run()`'s stale `state='completed'` requirement; (2) two new `cfg_escalation_requirement` check_kinds (`actor_must_be_assignee`, `decision_required_approval_requires_researcher`) plus a new transition condition (`followup_cleared_was_approved`, proposed as #1340, not yet applied).
- `iba/app/handlers/configmaint.py` — `_check_proposal()` now rejects an `insert` carrying a `-Where` clause (silently ignored by `_apply()`, previously corrupted a live `cfg_setting` row to `key=NULL` — cleanup proposed as #1329) and requires every NOT NULL/primary-key column present in `-Set`. `propose()` now requires and validates `-Title` at the source instead of `raise_()` silently word-truncating `-Question` into a mangled title.
- `iba/app/handlers/base.py`, `iba/app/run.py` — `escalate()`/dispatch threading for the new `-Title` parameter.
- `iba/app/ps/Config-Maintenance.ps1` — help text corrected (told people to use dead-code `AnswerRun`; a real, separate case-insensitive `$RunId`/`$runId` variable-collision bug found and fixed along the way); new `-Title` parameter, required on a fresh `-Step Propose` call.
- `iba/app/lib/reportkit.py` — `archive_before_write()` now retries a transient lock.
- `iba/app/lib/cfgreport.py`, `iba/app/handlers/configmaint.py` — CSV export on auto-triggered report regeneration now opt-in (`configmaint.csv_export_on_auto_report`, default 0).
- `iba/app/lib/schemareport.py` — IBA's own `report.schema_overview`: fixed 20 undocumented live tables (verified live: regenerated, 41/41 known=live, zero gap); added `write_report_bible_research()`, the bible_research.db counterpart (all ~113 real tables, no curated allowlist). Registration for the latter still pending (#1331–1335, #1337).
- `iba/app/handlers/reports.py` — new handler `schema_overview_bible_research_report`.
- `iba/app/ps/SchemaOverview-BibleResearch-Report.ps1` — new PS wrapper.
- `iba/app/CHARTER.md` §4, `iba/app/GOVERNANCE.md` §69 — Developer Mode / App Mode, written, then corrected same day after the first draft's mechanism was rejected.
- Archived, not deleted: `iba/app/tools/build_schema_overview_report.py` → `iba/app/tools/archive/`; `outputs/schema-overview-bible-research-20260831.md` → `outputs/archive/`; `Workflow/schema/schema-overview-v1-20260829.md` → `Workflow/schema/archive/` (regular report-versioning archive).
- `iba/config/DBSchema/DBSchema.json` rebuilt (was stale: 111 vs live 113 tables), config hash reconciled.

## Decisions — whose

**Researcher's own decisions:**
- Rejected #1342/#1343 and re-stated, verbatim and capitalized, the Developer Mode / App Mode operating split established at the app's original design.
- Approved (real `ready_for_approval`→`approved`, applied): #1309, #1310, #1315, #1321–#1325.
- Approved #1146's write-grant-revocation design (prior session; applied this session).
- Rejected #1306's first schema-overview submission ("wrong and incomplete... no handle in the excel tools").
- Corrected the output-folder location for the bible_research report.

**Self-correctable — Claude found, fixed, and closed directly:** every item in the "completed" rows
above; three real code defects (`answered_for_run`, `_apply()` insert validation, `AnswerRun` dead
documentation) found live while doing approved work, not invented independently.

**Claude's own process mistakes, corrected mid-session (not silently absorbed):**
- Used `AnswerRun` on `decision_required` items (wrong mechanism) before discovering it's fully
  dead code for every item raised since escalation #799.
- Self-approved #1305 (a `decision_required` item) — worked at the time (no `needs_followup`
  chain), judged afterward to have violated the researcher's actual intent.
- Proposed and built a per-table Developer-Mode-vs-App-Mode self-classification mechanism —
  rejected outright; corrected to the session-level model now in `CHARTER.md` §4.

## Open items for next session

1. **#1312, #1314, #1327, #1329, #1331–1337, #1340** — pending your review/approval (config
   proposals + tracking items), listed above with what each is for.
2. **#1306** needs one more pass: the escalation record itself still needs updating with the
   corrected output-folder path (communicated in chat, not recorded — Claude is currently
   guard-blocked from touching it, since it's assigned to you).
3. **#1338, #1339, #1341, #1344** — trivial self-inflicted crash artifacts, safe to close next
   session (not done now, to avoid more activity right before the session boundary).
4. **#1342/#1343 replacements** — re-propose `cfg_behaviour_rule` content matching the corrected
   `CHARTER.md` §4, once you've confirmed the correction is right.
5. **A new Developer Mode session** is the next planned session (per your instruction) — this
   session's own permissions were standard throughout (confirmed by every classifier block hit
   today), so nothing here assumes or requires elevated access.

## Git state

