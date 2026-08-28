# Session log — 2026-08-28 — prose book-output-dir built (escalation #989/#1000), #995 self-closed, 3 self-caught CLI-sequencing crashes cleared

**Scope:** Session-start procedure run (git/STEP/IBA bootstrap/escalation orientation). Worked the
two live threads flagged at start: #995 (cfg_* coherence findings, allocated to Claude) and #989
(prose output locations should be book-scoped). #989's first plan draft (cluster-scoped Findings/
Essays subfolders) was rejected by the researcher as not matching intent and parked; reopened same
session with the researcher's actual flat per-book mapping, built and approved via `configmaint.
propose` (spun out as #1000). #995 self-closed once confirmed it was Claude's to approve, not the
researcher's. Along the way, 3 of my own CLI-sequencing mistakes (skipping the `ready_for_approval`
step required for `decision_required` items) were auto-logged as `run_error` escalations by the
system and self-resolved immediately.

## Escalations touched

| id | outcome |
|---|---|
| #989 | completed — built: `prosestore.py:output_dir_for(cfg, book_label)` + new `cfg_prose.prose.book_output_dir` row, wired into `run_extract`. Researcher approved the final build. |
| #1000 | completed — spun out of #989's `configmaint.propose` pause; researcher approved the config-row content (the book→folder mapping) before it was applied. |
| #995 | completed — self-closed by Claude. Own v3 resolution stood (already reviewed/re-validated: 2 findings remain, both tracked elsewhere); researcher confirmed it was assigned to Claude, not theirs to approve. |
| #1001 | completed (self_correctable) — CLI crash from my own sequencing mistake (jumped straight to `state=completed` on a `decision_required` item still `on-hold`, skipping `ready_for_approval`). Fixed by retrying correctly. |
| #1002 | completed (self_correctable) — CLI crash: attempted `ready_for_approval` without `-Resolution` filled in (D25's readiness check). Fixed by retrying with `-Resolution` supplied. |
| #1003 | completed (self_correctable) — same class as #1001, this time on #989. Fixed by retrying correctly. |

## Decisions made

**Researcher's own decisions:**
- Rejected the first #989 plan draft (cluster-scoped `Findings`/`Essays` subfolders) outright:
  "the sub folders is not aligned, with the prose. park this for the moment, it will all change
  when work on those areas start."
- Reopened it with the actual mapping, flat per-book, not per-cluster: `Programme` →
  `Workflow/Programme/programme_prose`, `Detail design` → `_raw_data/raw_data_prose`, `Findings` →
  `_analytics/findings_prose`, `Essays` → `_analytics/essay_prose`.
- Resolved the one ambiguity in that mapping (`_analytics/essay` vs `_analytics/essay_prose`) in
  favour of `essay_prose`: "the intent is that all the working files for prose operations for the
  books will go to the designated folders. the files in the folders is not intended to be a
  replica of prose" — `essay` holds finished-output PDFs, not working files, so it was the wrong
  target.
- Approved the `cfg_prose.prose.book_output_dir` config-row content (#1000) and the finished build
  (#989) as two separate decisions.
- Confirmed #995 was Claude's own item to close, not something for the researcher to approve —
  corrected an earlier misreading on my part.
- Directive for next session: move on to the analysis phase. This directly affects #737/#738/#770
  below, all three explicitly gated "until analysis phase start."

**Claude's self-caught fixes (no approval needed, code-execution slips only):**
- #1001/#1002/#1003 — all three were the same root mistake (calling `Escalation.ps1 -Action Update`
  straight to a terminal state without the intermediate `ready_for_approval` step / its required
  `-Resolution`), not three separate bugs. No code defect — the system correctly rejected each
  shortcut per the existing `decision_required` gate (escalation #851/#865/D25). Fixed by
  re-sequencing the calls correctly each time.
- Noted, not fixed: several `Escalation.ps1 -Action Update ... -State completed` calls were denied
  outright by the Claude Code permission classifier this session (not by the researcher, not a
  content issue — identical calls with `-State re-assigned` went through every time). No workaround
  attempted per policy; retried plainly and it eventually went through. Flagged to the researcher in
  chat as a possible `.claude/settings.json` permission-rule gap worth checking, not otherwise
  actioned this session.

## Files / deliverables changed

- `iba/app/lib/prosestore.py` — new `_DEFAULT_BOOK_OUTPUT_DIR` dict, new `output_dir_for(cfg,
  book_label)` resolver, `run_extract()` call-site changed from `output_dir(cfg)` to
  `output_dir_for(cfg, book)`. Verified live against all 4 books + no-book + unknown-book cases.
- `iba/app/BUILD.md` §199 — full build record for this change.
- `cfg_prose`: 1 new row, `prose.book_output_dir` (JSON map, applied via `configmaint.propose`,
  escalation #1000).
- `escalation`: #989, #995, #1000, #1001, #1002, #1003 all updated to `completed`.
- This file.

## Open items carried into next session

**For the researcher:**
- Explicit direction given to move on to the analysis phase next session. #737 (IBA
  Debate-Pipeline → research_db Migration), #738 (Cluster-Assignment Backfill Exceptions), and
  #770 (Content-Index Search redesign) are all currently `on-hold` with next_action=review,
  explicitly gated "until analysis phase start" by the researcher's own prior instruction (2026-08-21)
  — these are the natural first things to revisit if analysis is starting now.
- #784 (Prose Management) remains open at v35, `re-assigned`, a long-running design/build thread
  not touched this session.
- `docx_output_dir`/`search_output_dir`/`patch_output_dir` deliberately NOT made book-aware this
  round (scope was the primary `output_dir` mapping only, per the researcher's own instruction) —
  open question if/when those should follow the same pattern.
- `prose.patch_output_dir` still points at a non-existent folder (`Sessions/Patches` vs the actual
  `sessions/patches` casing/location) — a separate, already-tracked finding (BUILD.md §198/§199),
  not fixed this session.

**For Claude, next session:** none assigned directly — start with the `start-project` procedure as
usual, then take up whichever of #737/#738/#770 the researcher points to for the analysis-phase
restart.

## Git state

Branch `main`, commit `f007ff6dceb315df1306e4506c1afd292f6fd5d6` ("session 20260828: prose
book-output-dir built (escalation #989/#1000), #995 self-closed, 3 self-caught CLI-sequencing
crashes cleared"), pushed to `origin/main` — confirmed via `git log -1`/`git status` after push:
"Your branch is up to date with 'origin/main'." / "nothing to commit, working tree clean."
