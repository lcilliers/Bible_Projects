# Session log — 2026-09-03 (standard session)

**Scope, one line:** Researcher critique of #1384's own `not_mechanically_checkable` audit —
"a rule delivered into Claude's session memory is compliant; the classification should say what
ensures it's followed, not just that code can't check it" — corrected by building a real mechanical
delivery-verification check (escalation #1388), which then surfaced a second, independent problem
the researcher caught live: Claude bare-reassigning finished decision_required items back to the
researcher instead of progressing them via `ready_for_approval` — fixed structurally, not just for
the 4 open items it was first caught on (escalation #1428).

## Escalations touched

| id | outcome this session |
|---|---|
| **#1388** | Raised. Design: `cfg_enum` value `context_delivered` replacing an asserted (never verified) `not_mechanically_checkable`; new `cfgquality.verify_behaviour_rule_delivery()`/`find_undelivered_conversational_rules()`. Hand-count of 8 gap rows corrected to the mechanically-verified 9 (rule 47 actually passes; rule 21 doesn't). All 33 resulting config changes proposed individually (specific Title/Question each, per researcher instruction), approved, applied, verified live (0 undelivered findings), `completed`. |
| **#1389–#1421** | 33 sub-proposals (1 `cfg_enum` insert + 32 `cfg_behaviour_rule.enforcement_status` flips, 9 also carrying a `source` fix). All approved, applied, individually closed (`needs_claude_followup` cleared) — this closure step was missed on the first pass and caught by the Stop hook, then fixed for all 33 in one pass. `completed`. |
| **#1384** | Updated: pointed at #1388 as the fix for the gap its own audit left open. Advanced to `ready_for_approval`, approved, follow-up cleared. `completed`. |
| **#1373** | Diagnosed the open question left at v4 (`rename` vs `add-and-retire` for a stale `cfg_enum` value) — confirmed via the code's own comment it was a documented rename. Filed 4 fixes (#1422–#1425), corrected to the proper `ready_for_approval` handoff shape after the researcher's #1428 correction, approved, `completed`. |
| **#1316** | Validated a 12-version saga — found the registered `cfg_utility` row pointed at a file already archived/deleted, superseded by escalation #1306's real report steps. Filed #1426, corrected to proper handoff shape, approved, `completed`. |
| **#1366**, **#1375** | Re-verified their prior applied fixes still hold live; corrected to proper handoff shape, approved, `completed`. |
| **#1422–#1426** | 4 `cfg_enum` fixes for #1373's coherence error + 1 `cfg_utility` deactivation for #1316. Approved, applied, verified (`configmaint.validate`'s coherence error confirmed gone), `completed`. |
| **#1428** | Raised: the bare-reassign-loop design flaw itself (researcher's verbatim correction quoted in full). New `cfg_escalation_requirement` check_kind built, tested twice (synthetic pre-approval, then live post-approval), `cfg_behaviour_rule` 63 rewritten and reclassified `mechanically_enforced`. `completed`. |
| **#1429, #1430, #1432** | The 3 config pieces of #1428's fix (`cfg_enum` value, `cfg_escalation_requirement` row, rule 63 rewrite). Approved, applied, verified, `completed`. |
| **#1427** | Auto-raised by `configmaint.validate`'s own advisory findings, carrying the researcher's live comment ("candidate cfgs coming back... check every orphan"). Investigated both questions directly: `cfg_behaviour_rule.enforcement_status`'s `cfg_column.expectation` was free prose instead of the real `enum.*` token (never structurally checked); two `candidate.*` settings were stale-active leftovers from the system's 2026-07-23 retraction. Filed #1434–#1436, `completed`. |
| **#1434–#1436** | The 3 fixes from #1427. Approved, applied, verified (`find_enum_violations()` returns 0), `completed`. |
| **#1383** | Pre-existing item (verse-lexical Window 1 enrichment, spawned from #1376). Researcher pushed back v3's objective as not capturing the actual instruction and possibly written without reading the full document chain. Not actioned this session (this session was fully consumed by #1388/#1428/#1427) — advanced to `ready_for_approval` with the open scoping question as its resolution (start the re-read-and-revise now vs. hold for a dedicated session), per #1428's own new rule that a genuine open question is a valid `ready_for_approval` payload. **Still open, carried forward.** |

## Files created or changed

**#1388 (delivery verification):** `iba/app/lib/cfgquality.py` (+2 functions —
`verify_behaviour_rule_delivery`, `find_undelivered_conversational_rules` — + `CLAUDE_MEMORY_DIR`
constant + regexes); `iba/app/handlers/configmaint.py` (findings dict +1); `iba/app/lib/cfgreport.py`
(findings list +1); 6 new memory files (`feedback_verify_db_state_before_acting`,
`feedback_confirm_output_exists_before_reporting_done`, `feedback_label_inferential_output_not_confirmed`,
`feedback_default_readonly_db_connections`, `feedback_dont_assume_which_database`,
`feedback_chat_items_become_escalations_same_turn` — written to the Claude Code memory directory,
**outside the git repo**, plus `MEMORY.md` index entries — not part of this commit); `iba/app/GOVERNANCE.md`
(§70, also backfilling #1384's own missed entry); `iba/app/BUILD.md` (#223);
`outputs/escalation/1388-behaviour-rule-delivery-fix-batch-v1-20260903.md` (the 33-change manifest);
`iba/app/db/iba.db` (`cfg_enum` +1 value; `cfg_behaviour_rule` 32 rows' `enforcement_status`
updated, 9 of those also `source`).

**#1428 (bare-reassign loop):** `iba/app/lib/escalation.py` (`_check_requirements()` +1 branch;
`update()`'s `"update"`-action requirements call extended to pass `next_action`/
`next_action_assigned_to`); `iba/app/GOVERNANCE.md` (§71); `iba/app/BUILD.md` (#224);
`iba/app/db/iba.db` (`cfg_enum` +1 value; `cfg_escalation_requirement` +1 row; `cfg_behaviour_rule`
id=63 rewritten).

**#1373/#1316 coherence + stale-registration fixes:** `iba/app/db/iba.db` (`cfg_enum`
`escalation_requirement_check_kind` +3 values, 1 retired; `cfg_utility` `schema_overview` row
deactivated).

**#1427 (orphan/candidate investigation):** `iba/app/db/iba.db` (`cfg_column.expectation` for
`cfg_behaviour_rule.enforcement_status` corrected to `enum.behaviour_rule_enforcement_status`;
`cfg_setting` `candidate.quality_report_path`/`candidate.load_report_path` deactivated).

**Auto-regenerated artefacts** (not hand-edited): `outputs/configs/CONFIG-REPORT-v370/v371-*.md` +
archived predecessor, `Workflow/schema/archive/*-20260903-081205.csv` (33 files, one per live
`cfg_*` table — a full schema snapshot triggered by the volume of config writes this session),
`outputs/escalation/escalation-list-v48-20260903.md` + archived predecessor.

## Decisions made

**Researcher's own decisions, this chat:** the `not_mechanically_checkable` classification was
wrong to treat "compliance can't be checked" and "delivery isn't verified" as the same thing, and
demanded a real mechanical fix, not a data-only correction (#1388, quoted verbatim in the
escalation). Approved all 33 resulting proposals individually, each with its own specific
resolution as instructed ("I will deal with the collection of approvals in waiting"). Caught and
named the bare-reassign-to-Researcher loop directly, quoted verbatim, explicitly rejecting "just a
correction of the open items" in favour of a structural config fix (#1428). Raised the orphan/
candidate questions live on #1427 rather than approving it as a generic notice. Pushed back #1383's
v3 objective as not reflecting the actual instruction, asked directly whether the full document
chain had been read.

**Claude self-corrected (execution fixes against already-approved direction), not glossed over:**
(1) a first pass through `escalation.update()`'s Python API reported all 33 `ready_for_approval`
writes as successful but never called `Db.close()` (which commits) — silently rolled back; caught
by checking the live table directly, not trusted from the printed messages. (2) The 33 escalation
*records* themselves were left with `needs_claude_followup=1` after their underlying config
changes were applied — the Stop hook caught this; fixed for all 33. (3) A `memory <slug>` regex
consumed text across the `source`/`enforced_by` boundary under `re.IGNORECASE`, producing false
negatives — caught testing against real DB rows, not just the synthetic case. (4) After building
the bare-reassign fix, immediately reproduced the exact same mistake on #1373/#1316/#1366/#1375 a
second time by writing "reassigning to you" in a comment without actually calling
`next_action_assigned_to="Researcher"` in that same update — caught by checking the live DB, fixed
explicitly, and folded into the mechanical fix so it can't recur silently again.

## Open items carried into next session

1. **#1383 (verse-lexical Window 1 enrichment)** — awaiting the researcher's decision: start the
   document re-read-and-revise now as a focused pass, or hold for a dedicated session. Not
   resumed this session.
2. Everything else in the escalation backlog predating this session (#737/#738/#770/#784/#1006/
   #1022/#1376/#1378/#1385/#1386/#1387 and the wider on-hold set) — untouched, unchanged, still
   exactly where the session-start orientation found them.

## Git state

