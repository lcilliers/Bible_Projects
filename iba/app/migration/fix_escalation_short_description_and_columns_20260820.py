"""fix_escalation_short_description_and_columns_20260820.py — one-off data repair, escalation #759.

Researcher, 2026-08-20: "the short_description for all the item created by you or the system does
not comply with the column specs. ... It should not be longer than 60 characters, and be a short
description of item -- like a title. ... you need to use the text columns correctly. Comment - what
needs to be done or the error message; Context - the context to understand to point and make
choices; resolution = what have been done to solve or complete the issue (it is not just the
decision like 'approved'."

Confirmed live (escalation #759): 18 of the 23 post-redesign escalation rows (id 736-758) had a
short_description over 100 characters (max 516) — full paragraphs, not a title — because
raise_new()/raise_() store -Question verbatim with no length/shape check, and every finding this
session was front-loaded into short_description instead of context/comment.

`update()` deliberately excludes short_description from its editable fields (plan v3 §3:
short_description is IMMUTABLE after Raise, corrected by superseding — never edited in place). That
policy is right for the NORMAL workflow (a party correcting their own mistaken title mid-thread) but
this is a one-off structural repair directed by the researcher, not a normal transaction — so this
script writes directly, the same way `escalation.py`'s own `_snapshot()` does (new
`escalation_history` row, `escalation` updated to match, single commit), but allows changing
short_description, which `_snapshot()`'s caller (`update()`) never does. The OLD history rows are
untouched — every prior version stays exactly as it was written, preserving the append-only
guarantee `escalation_history` exists for (escalation #715's whole reason for existing). This is a
new version ON TOP, clearly marked as a data-repair correction, not a rewrite of history.

#753 (the umbrella tracking item) is deliberately excluded — its short_description is already a
real 29-character title, and its comment/context are a genuine researcher-authored running thread,
not a Claude-authored finding-dump; rewriting it would lose the thread it's meant to hold.

Run: python -m iba.app.migration.fix_escalation_short_description_and_columns_20260820
"""

from __future__ import annotations

import datetime

from ..lib.cfg import Cfg
from ..lib.db import Db

_NOW = lambda: datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

_COLS = ("run_id", "source", "at_step", "type", "short_description", "context", "comment", "tried",
        "state", "next_action", "next_action_assigned_to", "originator", "resolution",
        "related_activity", "raised_at", "answered_at")

_REPAIR_NOTE = ("[data corrected 2026-08-20, escalation #759: short_description reshaped to a "
               "<=60-char title; prior full text redistributed into context (background) / "
               "comment (what needs to be done) / resolution (what was actually done) per the "
               "researcher's column-spec correction. No prior escalation_history row altered.]")

# id -> (short_description, comment, context, resolution_or_None_to_leave_unchanged)
FIXES: dict[int, tuple[str, str, str | None, str | None]] = {
 736: ("Filing/consolidation: main project vs IBA reports",
       "Think through filing between main project and IBA -- phase-related work filed together, "
       "not split across branches; topic reports must not dump into the general one-off folder. "
       "Also resolves the deferred governance.oneoff_report_dir CSV row.",
       "Carried over from escalations_old #650 at the 2026-08-19 redesign cutover -- was on-hold, "
       "dependent on a deeper review of the statement of affairs. Reference: "
       "outputs/markdown/iba-table-review-response-v1-20260816.md",
       None),
 737: ("Move IBA debate-pipeline tables to research_db (GATED)",
       "Move the debate work currently in IBA (passage/phenomenon/operation/hib tables) to "
       "research_db -- it's part of findings (governance.scope_research_db), not process-control/"
       "base data (governance.scope_iba_db). GATED: do not start until the IBA design audit is "
       "complete.",
       "Carried over from escalations_old #654 -- was on-hold, hold until work on the analytic "
       "phase is restarted. Reference: Workflow/Chat_responses/Additional configs",
       None),
 738: ("Cluster-assignment exceptions: 746 no-link, 825 sibling",
       "746 strong(s) carry a non-T2 cluster with no word_registry link; 825 backfill strong(s) "
       "have an already-active or already-clustered sibling. Needs your review/decision.",
       "Full detail: iba/app/reports/cluster-assign-v2-20260817.md. Carried over from "
       "escalations_old #668 -- was on-hold: backfill strongs (not T2/T3) may not be linked to "
       "words yet; analytics will identify individual backfills to pull into the registry, rather "
       "than bulk-importing them.",
       None),
 739: ("Prose ch.4-6 need realignment to 2026-08-15 architecture",
       "Read chapters 4-6 (Data architecture / Data integrity & governance / Instruction corpus) "
       "plus the root README against live GOVERNANCE.md/CLAUDE.md/the actual DB split; identify "
       "what's stale; revise or supersede.",
       "cfg_prose_chapter status='not_yet_aligned' for these 3 chapters -- content likely predates "
       "the 2026-08-15 iba.db/bible_research.db architecture correction. Carried over from "
       "escalations_old #725 -- was in-progress, next_action=approve: 'I would not be surprised to "
       "find discrepancies between what is set in prose, and what is still lingering and "
       "inconsistent in the governance and claude.' Reference: "
       "iba/app/reports/gr-prog-001-prose-canonical-authority-plan-20260818.md",
       None),
 740: ("configmaint.validate: 2 orphan configs found (advisory)",
       "advisory only -- acknowledged during escalation-redesign live testing, no action taken.",
       "cfg_* is structurally coherent overall. 2 orphans: cfg_setting 'database.iba.path' and "
       "'database.bible_research.path' (key not found together with a cfg.setting(...) call in "
       "any one file). Full detail: iba/app/config/CONFIG-REPORT-v126-20260820.md.",
       "Acknowledged as advisory during live testing of the escalation redesign -- no orphan-"
       "config fix applied, no further action taken on this run."),
 741: ("Smoke test: new manual raise/update flow",
       "Smoke test of the new manual raise/update flow -- confirm ready_for_approval lands on "
       "re-assigned per priority rule 5, test an actual assignee change.",
       None,
       None),   # resolution already good, leave as-is
 742: ("Smoke test: approved-without-resolution negative case",
       "Second smoke test, for a clean approved-without-resolution negative test.",
       None,
       "Smoke test cleanup -- withdrawn, purpose served."),
 743: ("Escalation.ps1 had no PS wrapper for manual verbs",
       "Escalation.ps1 has no PS wrapper for the new manual verbs (raise_new/update) -- only "
       "List/AnswerRun (dispatcher-tied) exposed. Manual items only reachable via 'python -m "
       "iba.app.lib.escalation raise|update' directly.",
       "Self-closing per the researcher's standing rule: Claude may complete its own "
       "straightforward, fully-recorded fixes. Verified live end to end via the actual .ps1 file, "
       "not just python -m.",
       None),
 744: ("GOVERNANCE.md/USER-GUIDE.md still describe old shape",
       "GOVERNANCE.md and USER-GUIDE.md still describe the pre-redesign single-vocabulary "
       "escalation shape almost everywhere -- only the registry.create-specific passages were "
       "corrected (BUILD.md sec153). A full documentation pass covering the two-vocabulary model, "
       "escalation_history, and the new Raise/Update transaction shapes is still owed.",
       "Self-closing per the researcher's standing rule. Verified structurally (section headers, "
       "table formatting) after the rewrite.",
       None),
 745: ("cfg_write_grant missing row for escalation_history",
       "cfg_write_grant has no row for escalation_history at all (writer='escalation'/'run' only "
       "cover the 'escalation' table) -- every write to escalation_history currently bypasses the "
       "grant check entirely, ungoverned.",
       "Found live 2026-08-20 while compiling the escalation list, not caught during build/"
       "testing. Self-closing per the researcher's standing rule (2026-08-19): Claude may complete "
       "its own straightforward, fully-recorded fixes. Verified live -- both grant rows now "
       "present, both code paths check both tables, real write tested clean.",
       None),
 746: ("cfg_escalation rule table is stale post-redesign",
       "cfg_escalation (the rule table governing escalation.py itself, 7 rows) still describes the "
       "pre-redesign single-table mechanism -- duplicate_suppression/chat_routing/"
       "document_reference_grouping etc. need review against the new raise_new/update split.",
       "Also contains a known-stale row: module_blocking.enforced_by still reads 'not yet wired' "
       "though it has been live in run.py since escalation #646 (2026-08-17) -- found during the "
       "mechanics investigation (iba/docs/escalation-system-mechanics-20260818.md), never fixed.",
       None),
 747: ("write_history_report() built but never wired to a CLI",
       "write_history_report() (the per-item deep-history report, plan v3 sec5b -- follows "
       "related_activity/supersede links across items) exists as a function in lib/escalation.py "
       "but has no CLI verb in main() and no Escalation.ps1 action -- built, never wired to an "
       "entry point.",
       "Closed alongside #743 -- same PS-wrapper build covered both. Verified live -- see #743's "
       "resolution.",
       None),
 748: ("#735's 2 orphan-config findings never resolved",
       "The 2 orphan-config findings from escalation #735 (raised during live verification of the "
       "redesign, 2026-08-20) were never resolved. Re-run configmaint.validate under the live new "
       "system to raise a fresh, properly-tracked replacement.",
       "#735 is now frozen, unanswered, in escalations_old -- the v2 cutover only carried over the "
       "4 items named explicitly (#650/#654/#668/#725), not #735.",
       None),
 749: ("Old #677 design gap confirmed superseded -- formal close",
       "escalations_old #677 (the reassign-discards-in-progress design gap) was confirmed by the "
       "researcher as superseded by this redesign ('is now superceded with this work complete').",
       "Was deliberately left un-closed in escalations_old at cutover time, pending the redesign "
       "actually landing live. It now has -- this is the formal closure note the researcher's "
       "confirmation was waiting on.",
       None),
 750: ("Dead cfg_write_grant row: writer=run, table=escalation",
       "run.py's 3 direct escalation writes were replaced by esc_raise() calls (BUILD.md sec154), "
       "which always check under writer='escalation', not 'run'. cfg.may_write('run') is only "
       "checked for validation_result/run now, never escalation -- proceed to complete this work.",
       "Confirmed by grep. Found while fixing #745, not yet acted on.",
       None),
 751: ("Verified #745's fix -- grant now correctly checked",
       "Self-test of the _grant_both fix, closing immediately.",
       None,
       "Verified #745's fix live: cfg_write_grant now correctly checked for both 'escalation' and "
       "'escalation_history' on write."),
 752: ("PS wrapper live test: Raise/Update/History (#743/#747)",
       "Verifying the new manual verbs work end to end through the PS front door, not just the "
       "Python CLI.",
       None,
       "Confirmed live: Escalation.ps1 -Action Raise/Update/History all work correctly through the "
       "actual PS front door."),
 754: ("Escalation.ps1 -Comment positional-binding bug",
       "Missing dash before -Comment let PowerShell silently bind the bare token to -RunId/"
       "-Decision instead of erroring -- confusing ValidateSet failure pointed at the wrong "
       "parameter.",
       "Root cause: Escalation.ps1 used default [CmdletBinding()] positional binding across all 16 "
       "params. A missing leading '-' before -Comment (e.g. `...-State in-progress comment \"long "
       "text\"`) caused PowerShell to silently bind the bare token 'comment' to -RunId (position 2, "
       "first unbound) and the actual comment text to -Decision (position 3), which then failed "
       "ValidateSet with a confusing error pointing at -Decision. Separately: because the error was "
       "a PS parameter-binding terminating error thrown before the script ever called into "
       "iba.app.lib.escalation, it never reached the escalation DB on its own -- no mechanism auto-"
       "captures a PS-side terminating error as an escalation row (see #754/#755 finding 2).",
       "Fixed: added PositionalBinding=$false to Escalation.ps1's CmdletBinding. Verified: (1) the "
       "exact failing command now throws a clear \"A positional parameter cannot be found that "
       "accepts argument 'comment'.\" pointing at the actual bad token, instead of corrupting "
       "-Decision; (2) normal named-parameter usage (-Action History -Id 753) still works "
       "unchanged; (3) grepped all iba/app/ps/*.ps1 callers -- every existing invocation uses named "
       "parameters only, none rely on positional args; (4) re-ran the researcher's original "
       "-Action Update -Id 753 command with -Comment corrected -- landed clean as v2. Second fix, "
       "same root cause: USER-GUIDE.md sec4.6's -Action Update synopsis documented the trailing "
       "argument as a bare '[comment text]' instead of '[-Comment ...]' -- corrected, and the "
       "missing '[-Context ...]' flag added alongside it."),
 755: ("Escalation config review: 4 gaps found (#753)",
       "Config review requested in #753 v2, report-only -- no changes made yet. Full report: "
       "iba/docs/escalation-config-review-v1-20260820.md. Section 5 proposes 4 concrete config "
       "changes for your decision.",
       "Findings: (1) cfg_status_flow exists exactly for entity/status/set_by ownership but has "
       "ZERO escalation rows -- the plan v3 sec3 state-transition table lives only in Python/the "
       "plan doc. (2) cfg_enum escalation_next_action merges the dispatcher-tied and manual "
       "vocabularies the design says must stay separate; the dispatcher-tied path doesn't even "
       "consult the enum (hardcodes its own tuple), Escalation.ps1 hardcodes a third copy; also a "
       "duplicate ordinal and a skipped one. (3) The escalation module's two reports are the ONLY "
       "reports in the app that bypass reportkit.render_scaffold()/cfg_report entirely, and aren't "
       "named in cfgquality.REPORT_STEPS so this can never be caught automatically. (4) "
       "cfg_write_grant(writer=escalation, table_name=word_registry) is an orphan. Cross-"
       "referenced, not re-raised: #746, #748, #750.",
       None),
 756: ("Retire orphan cfg_write_grant: escalation->word_registry",
       "cfg_write_grant(writer=escalation, table_name=word_registry) is an orphan -- grepped the "
       "whole codebase, escalation.py never writes word_registry and no other module checks "
       "may_write('escalation') against word_registry. Retiring (inactive=1) rather than deleting, "
       "for provenance.",
       None,   # leave the operational {table/op/where/set} JSON context untouched -- load-bearing
       None),
 757: ("C: drive at 0 bytes free -- found live during #755 test",
       "Copying iba.db to a scratch temp folder for a synthetic-DB test corrupted mid-copy with "
       "\"No space left on device\" -- the C: drive was at 475G/475G used, 0 bytes free. A "
       "0-free-space condition risks corrupting any in-progress write on the drive, including "
       "iba.db/bible_research.db on a live write.",
       "Deleted my own ~15GB of scratch test-DB copies immediately (safe, my own throwaway "
       "artifacts) -- brought it to 461G/475G used, 15G free (97%), but that's my cleanup, not a "
       "fix for the other ~461GB. Not investigated further -- finding/clearing ~461GB across the "
       "whole drive needed your direction on what's safe to delete.",
       None),   # resolution already good, leave as-is
 758: ("content_index ~63% of iba.db's 7.5GB, needs exclusions",
       "content_index (14.1M rows) is the large majority of iba.db's 7.5GB. Two folders never "
       "added to cfg_content_index_exclude now dominate: iba/app/verse-analysis/** (31.8%) and "
       "Sessions/Session_Clusters/** (31.6%) -- same failure mode already fixed once for "
       "programme_prose (2026-08-17). Needs your decision on scope before excluding.",
       "DB itself: 7.5GB, freelist_count=0 -- real data, not reclaimable. content_index: "
       "14,118,338 rows, 14x the next-biggest table. Raw text payload ~3.45GB before its 3 "
       "indexes. 76% of rows are key_type=gloss; top gloss values are ordinary English words "
       "coinciding with Strong's glosses (sense: 152,430 lines; word: 101,985; which: 71,830), not "
       "caught by the existing conjunction-only stoplist. iba/app/verse-analysis/**: 4,487,358 "
       "rows across 303 files. Sessions/Session_Clusters/**: 4,460,980 rows. "
       "ContentIndex-SizeProfile.ps1 already exists for pre-decision review.",
       None),
 759: ("escalation.short_description violates its own column spec",
       "short_description across the 23 post-redesign items averages 247 characters (max 516) -- "
       "full paragraphs, not a label/title. Needs a raise-time length/shape check going forward, "
       "and a decision on whether any residually-imperfect rows are left as historical fact.",
       "cfg_column spec: 'label/title -- what this item is about'. By source: claude-authored avg "
       "275 chars (11 rows), configmaint(system)-authored avg 320.5 (2 rows), researcher-authored "
       "avg 199.6 (8 rows). Root cause: raise_new()/raise_() store -Question verbatim with no "
       "length/shape check at write time. This data-repair pass (migration/"
       "fix_escalation_short_description_and_columns_20260820.py) corrects the 22 other affected "
       "rows' current state; the raise-time guardrail itself is still open, tracked here.",
       None),
}


def _current(db: Db, escalation_id: int) -> dict:
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    return dict(rows[0])


def main() -> None:
    cfg = Cfg()
    db = Db(cfg)
    if "escalation" not in cfg.may_write("escalation") or "escalation_history" not in cfg.may_write("escalation"):
        raise PermissionError("write-grant violation: 'escalation' may not write escalation/escalation_history")

    fixed = 0
    for eid, (new_sd, new_comment, new_context, new_resolution) in sorted(FIXES.items()):
        assert len(new_sd) <= 60, f"#{eid}: new short_description is {len(new_sd)} chars, over 60: {new_sd!r}"
        cur = _current(db, eid)
        merged = dict(cur)
        merged["short_description"] = new_sd
        merged["comment"] = f"{new_comment}\n\n{_REPAIR_NOTE}"
        if new_context is not None:
            merged["context"] = new_context
        if new_resolution is not None:
            merged["resolution"] = new_resolution
        merged["version"] = cur["version"] + 1
        merged["originator"] = "Claude"
        merged["answered_at"] = _NOW()

        db.write("escalation_history", {"escalation_id": eid, "version": merged["version"],
                                        **{k: merged[k] for k in _COLS}})
        db.update("escalation", {"id": eid}, version=merged["version"],
                 **{k: merged[k] for k in _COLS})
        fixed += 1
        print(f"  #{eid} v{merged['version']}: {new_sd!r} ({len(new_sd)} chars)")

    db.close()
    cfg.close()
    print(f"\n{fixed} rows corrected. #753 deliberately left untouched (see module docstring).")


if __name__ == "__main__":
    main()
