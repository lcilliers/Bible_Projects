# Prose management (#829/#831/#832/#835) — clean current-state assessment

> Written after #829/#831/#832/#835 were all rejected (superseded) per researcher instruction, on
> the grounds that the escalation history was unreadable. **This document does not use that
> history as its source.** It uses `iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`
> (the last, self-contained, researcher-approved consolidated proposal) as a checklist, and checks
> every item against `iba.db`/`bible_research.db`/the actual code live, today (2026-08-26). Where a
> claim below is a live number or a live schema fact, it was queried fresh for this document, not
> carried over from any prior report.

## Headline finding

**The core #829 build is not unfinished or incoherent — it is fully built, tested, and documented.**
Every one of v9 §9's 12 build steps was verified live against the database and code in this pass,
and every one matches the spec exactly. The record of the build is legible and complete:
`BUILD.md` §176 (build log + live test results), `GOVERNANCE.md` §53 (design record),
`USER-GUIDE.md` §13d (usage). The escalation *thread* (#829, 26 versions) was hard to navigate
because it kept accumulating cross-references and audit findings for two more days after the build
actually completed — not because the build itself is in doubt.

**What's genuinely still open is narrow:** one real piece of design work never started (§3 below),
plus a handful of already-made decisions that are correctly waiting on future scope, not stuck.

---

## 1. What v9 specified vs. what's live — checked item by item

| v9 §9 step | Spec | Live check | Result |
|---|---|---|---|
| 1 | `cfg_prose` table + 4 rows | Queried `cfg_prose` directly | ✅ Exact match — all 4 keys (`chapter_names`, `book_stage_map`, `search_default_limit`, `edit_file_dir`), correct values and `use` text |
| 2 | `cfg_column` — fill 4 blank `prose_section_type` cols + correct 4 `prose_section` citation cols | Queried `cfg_column` for all 8 | ✅ All 8 filled, wording matches v9 §5 verbatim; the 3 stale `prose_section` rows (`supersedes_id`/`superseded_by_id`/`source_file`) confirmed `inactive=1`, no action needed (matches v9 §1.3d) |
| 3 | `cfg_enum` — 5 new groups (status/author/source_stage/lifecycle_tag/book_label) | Queried all 5 | ✅ Exact match — 4+3+11+4+4 = 26 rows, all present |
| 4 | `cfg_status_flow`, `entity='prose_section'`, 4 rows | Queried | ✅ Exact match |
| 5 | `cfg_behaviour_rule` — 2 rows (author-gate, two-patch-ordering) + 1 (flag-trigger obligation) | Queried `rule_key LIKE '%prose%'` | ✅ All 3 present, matching text |
| 6 | `cfg_write_grant` — 3 new rows (`prose_section`, `prose_section_type`, `prose_flag`→`wa_data_quality_flags`) | Queried | ✅ All 3 present (plus the pre-existing `cfg_prose_chapter`/`cfg_prose_concept`/`cfg_prose` self-registration grants) |
| 7 | `cfg_work_package` `prose` + 5 `cfg_step` rows | Queried | ✅ Exact match — `prose.extract`/`.search`/`.export_chapter`/`.import_chapter`/`.flag`, all `inactive=0` |
| 8 | Reactivate 4 original scripts | Queried `cfg_utility` | ✅ All 4 `inactive=0`, superseded-pointer `purpose` text in place |
| 9 | Code: drop `CHAPTER_EDIT_OUT_DIR` hardcode, fix `_DEFAULT_BOOK_STAGE_MAP` | Read `prosestore.py` directly | ✅ `edit_file_dir(cfg)` reads `cfg_prose` live; the module constant survives only as an explicit Python-level fallback default (by design, documented in its own docstring); both call sites (`run_export_chapter`/`run_import_chapter`) confirmed to pass the config-driven path, not the constant |
| 10 | D3/D4/D5 — build only if approved | Checked live `PRAGMA foreign_key_list` on all 3 tables | ✅ Correctly **not** built — `prose_section_finding_link` still points at `wa_session_b_findings` (not `finding`), `prose_section_dimension_link` FK unchanged, `prose_section.cluster_code` has no FK to `cluster` — matches v9's decision that all three stay deferred |
| 11 | `docs/prose-store-architecture.md` → superseded banner | Read the file | ✅ Present, correct pointer table to every new config home |
| 12 | `GOVERNANCE.md`/`BUILD.md`/`USER-GUIDE.md` updates | Read all three | ✅ `GOVERNANCE.md` §53, `BUILD.md` §176 (with a real live test log, not just an assertion), `USER-GUIDE.md` §13d all present |

**Test plan (v9 §10)** — `BUILD.md` §176 records live dispatcher-level tests (not just the Python
functions): `Extract` (both real books + an invalid book, correctly rejected), `Search`, 
`ExportChapter`/`ImportChapter` (including catching and fixing a real bug along the way — `-Input`
collided with a PowerShell automatic variable, renamed `-InputFile`), `Flag` (valid + invalid flag
code), and a clean `configmaint.validate` run at the end. This is a genuine test log with concrete
results, not an asserted "tested, trust me."

## 2. #832's own items — live-checked, not re-derived from its history

| Item | v9/#832 claim | Live check today | Status |
|---|---|---|---|
| `version` type-mismatch | Resolved by #836 | N/A — not re-checked, #836 is a separate closed/built escalation | Resolved |
| `word_count=0` on 25 rows | Backfilled 2026-08-26 | `SELECT COUNT(*) FROM prose_section WHERE word_count=0` → **0** | ✅ Confirmed fixed |
| `approved_at` 87% NULL | Left NULL by agreement, documented as unrecoverable | `status='approved' AND approved_at IS NULL` → **729 of 863** approved rows | ✅ Matches the agreed (not fixed, deliberately) disposition |
| `cluster_code`/`characteristic_id`/`cluster_subgroup_id` — no FK, belong in a future Concordance index table | Decision made, not built | 175/949, 124/949, 0/949 populated; no FK on any (checked §1 row 10 above) | ✅ Decision stands, correctly unbuilt — Concordance (book 5) doesn't exist yet |

**Nothing here is actually stuck or ambiguous.** Items 1–3 are done; items 4–5 are a made decision
waiting on a future book that hasn't been scoped, not an open question.

## 3. The one real gap — #831 was never actually designed

This is the substantive finding. Reading #831's own history in isolation (not cross-referenced
against #829's real build timeline) shows what actually happened:

- **v1** (2026-08-23): scope raised — design the *operational rules* for creating/editing prose
  (creation modes, the two-patch trigger, delete-behaviour, verse-linking) — explicitly building on
  #829's storage layer.
- **v2–v4**: three rounds of pure cross-referencing — dependencies on #833 (flag mechanism), #836
  (record-change-log discipline), #854 (enum validation gap) were registered, but no design work
  happened.
- **v5** (2026-08-26, 15:30): **explicitly declared itself blocked**, reasoning: *"#829 is still
  in-progress, next_action=review, sitting with you, not yet approved/built... designing the add/edit
  operational rules now would mean designing against a storage layer that could still change under
  it."*

**That stated reason was factually wrong at the time it was written.** #829's storage layer was
built and tested live on **2026-08-24** (`BUILD.md` §176, confirmed §1 above) — two full days
*before* #831 v5 claimed it wasn't. #829's *escalation record* kept its `state=in-progress`/
`next_action=review` metadata because the thread kept accumulating further audit rounds (v10–v26:
re-verification passes, #851's authority-gap fix, #855/#854 tooling gaps, a self-approval
correction) — none of which touched the storage layer itself, but none of which closed the
escalation's own status either. **#831 was reading #829's stale escalation metadata as if it were
the real build state, instead of checking `BUILD.md` directly.** This is very likely the actual
mechanism behind "impossible to assess what was done vs. undecided" — the escalation tracker and
the real build state drifted apart, and every thread that cross-referenced #829 inherited that
drift.

**Net result: #831's actual design work — the rules governing *when* and *by what process* a prose
section gets created or edited — has not been started.** Nothing to build against is missing any
more (the storage layer has been ready since 2026-08-24); this is a clean, unblocked design task.

## 4. #835 — angle (a) built, angle (b) genuinely not started

- **Angle (a)** (`prose.flag` — raise one flag instance): built and live-tested as part of #829's
  own build (`cfg_step` row confirmed §1 row 7; live test in `BUILD.md` §176 raised and cleaned up a
  real row). `wa_data_quality_flags` currently holds **0 rows** (the test row was deleted after
  confirming it worked) — nothing outstanding to raise right now, no queued terminology-change flags
  waiting.
- **Angle (b)** (propose → approve → apply a fix against a raised flag): design captured in v9 §12.4
  but explicitly not built — parked "until prose editing comes into action." Given §3 above, that
  condition is essentially now — angle (b) is naturally the second half of whatever #831 designs
  for the edit path, not a separate independent task.

## 5. What's actually outstanding, in one list

1. **Design the prose add/edit operational rules** — the real content of old #831. Nothing blocking
   it any more.
2. **Angle (b) of the flag-fix workflow** — old #835's real remaining content. Reasonably scoped
   together with #1, since both concern the edit path.
3. **D10** (`book_stage_map` vs. `book_label` 1-row disagreement) — deferred to "the prose edit
   stage" by explicit researcher instruction 2026-08-24. If #1 is being designed now, this is the
   moment to either resolve it or explicitly re-defer it again.
4. **D3/D4/D5** (citation columns → future Concordance index table) — no action needed until the
   Concordance (book 5) itself is scoped. Not a task, just a standing pointer.

Nothing else from the four rejected escalations needs re-litigating — §1's table confirms the rest
is genuinely done.

---

*No escalation raised from this document yet — filed for review first, per instruction.*
