# Session Log — 2026-09-18 (v3)

**Status: OPEN, paused at the researcher's own request.** `M49` is fully complete through the built
pipeline (`ready_for_observations`). `M83` is complete except subgroup A, which is deliberately left
blocked pending a real architecture decision (escalation #1767). Six further escalations
(#1766/#1767/#1768/#1769/#1770/#1771) are raised, documented, and sitting with the researcher —
nothing further is assigned to Claude. Session closed here at the researcher's own instruction
("walk away from it for a bit"), not because the work ran out.

**Scope:** Continuing the cluster-reading pipeline from `SESSION-LOG-20260918-v2.md`'s stopping
point — ran `M49` and `M83` through Stages 1–4, built the batch-run control mechanism (resume/skip,
crash safeguard, live progress monitor) the researcher asked for after two forced full-restarts,
extended `cluster.reading` to handle a member strong whose occurrence count exceeds the per-call
cap by splitting it by surface form, then ran a researcher-directed multi-angle data-quality audit
(completeness/quality/purpose/orphans/inconsistencies) that surfaced several more open design
questions. Interspersed throughout: live ad hoc SQL/schema investigation of researcher-spotted
anomalies in the raw data.

## 1. `M49` through the full built pipeline (Stages 1–4)

Ran `VerseReading.ps1` (Stage 1) → crashed on batch 7 of 20: `IntegrityError: UNIQUE constraint
failed: ib_node.observation_id, ib_node.seq`. Root-caused live: `recordingpass.py`'s
`aligned-superficial-edit` path (appends a new occurrence's `ib_node` row to an EXISTING
`observation_id` when a later batch's text aligns to an earlier batch's) restarted `seq` at 0/1 per
call instead of continuing from that `observation_id`'s own current max — collided across batches.
Fixed (`seq` now queried fresh as `COALESCE(MAX(seq),0)` for that path only), verified via a
synthetic reproduction of the exact collision, DB state confirmed clean before the fix (partial
batch writes never committed). Escalations #1754 (dispatcher-tied, auto-raised)/#1755 (manual
write-up) closed.

Mid-run, the researcher independently checked `verse_lexical` role compliance for M49 and flagged a
suspected staleness — batches stopped on request. Investigated: the researcher's own query lacked
`vl.deleted=0`, pulling in 222 pre-cluster-model legacy rows (`role='content'` placeholder) alongside
162 live ones; both directions of the live-row check (role contains M49 ⟺ strong is an active M49
member) came back clean. Confirmed as a false alarm, resumed. `M49` completed Stages 1–4 (all 5
subgroups `answer_complete`, `cluster.status → ready_for_observations`).

## 2. Batch-run control mechanism built (escalation #1756)

Researcher's own request, prompted directly by the two full restarts M49's Stage 1 needed (a crash,
then the stop-and-check above): a table recording each batch's start/end with a timestamp, usable
for resume/skip and live progress monitoring. Designed (table shape, resume/skip key, crash
safeguard, monitor mechanism) and put to the researcher for approval before building, since design
work is never self-correctable even after clear direction; approved, then built while M49's own
Stage 1 continued in the background (safe — Python doesn't hot-reload a running process's own
loaded code).

Built: `run_batch` table + full `cfg_table`/`cfg_column`/`cfg_enum`/`cfg_write_grant` registration;
`iba/app/lib/batchcontrol.py` (`start_batch`/`commit_batch`/`fail_batch`/`already_committed`/
`content_key` — content-hash-keyed, not run-id-scoped, so a new run can skip work a prior run
already committed); wired into all 4 live LLM-calling steps (`lexical.meaning`,
`cluster.subgroup`, `cluster.reading`, `cluster.answer`); new monitor `BatchProgress.ps1`
(`report.batch_progress`, `iba/app/lib/batchprogressreport.py`) with `-FilterRunId`/`-Step`/
`-SelectorKey` filters. Tested against synthetic data (skip, crash-detection, monitor accuracy) and
live end-to-end before use.

Found and fixed its own bug within minutes of shipping: `run_batch`'s
`UNIQUE(step, selector_key, batch_content_key)` constraint blocked a legitimate retry after a
transient DNS failure (the constraint didn't distinguish a failed attempt from a committed one).
Root-caused, recreated the table without the constraint (resume/skip was always meant to be
application-level, via `already_committed()`'s own `WHERE status='committed'` check), all 4
existing rows preserved and verified, fix reproduced synthetically before and after. Escalations
#1758/#1759 (dispatcher-tied, auto-raised) and #1760 (manual write-up) closed. Later, at the
researcher's own request, extended `BatchProgress.ps1`'s failure/committed lines to carry an
absolute timestamp alongside the existing elapsed duration (they only showed elapsed before).

## 3. `M83` through the pipeline — subgroup A deliberately left blocked

Ran Stage 1 (50 batches, $15.82) and Stage 2 (4 subgroups) cleanly. Subgroup A (`G2212` + `H1245`)
turned out to have **two** member strongs simultaneously over the per-call occurrence cap — a case
`MultipleOverCapStrongs` explicitly refuses (a clean `fail()`, not a crash) rather than guess at an
undesigned packing order. B, C, D all completed Stages 3–4.

Subgroup D (`H1875`, 164 occurrences) needed the single-strong-over-cap case, which the researcher
resolved with a precise rule this session (see below): built `_partition_occurrences_by_surface`
(groups occurrences by surface form, greedily packs whole surface-groups under the cap, never
splitting one surface across batches) and rewrote `cluster.reading`'s handler to loop over the
resulting packages using the same `batchcontrol` machinery as every other multi-batch step.
Simulated against real `H3034`/`H1875` data before writing any handler code (produced exactly the
"break in two"/"break in three" splits the researcher's own rule predicted), then verified live.
Escalation #1761 closed.

For subgroup A's two-simultaneously-over-cap case, the researcher proposed a genuinely better
structural fix rather than patching the single-strong logic further: a two-tier (map-reduce)
redesign of `cluster.reading` itself — batch a subgroup's full occurrence set by verse (Tier 1,
small properly-grounded reads), then synthesize the cross-strong view from Tier 1's own findings
(Tier 2, not the raw material) rather than one call trying to hold everything. Captured as
escalation #1767, explicitly **not built this session** at the researcher's own instruction — M83
subgroup A stays blocked until it lands; M49/M83/M67 will likely need re-reading once it does,
since it supersedes the current single-call Stage 3 design rather than just extending it.

## 4. Grounding-gap incident and the re-read mechanism gaps it exposed

M83 subgroup B's first `cluster.answer` run reported 38 of 52 battery questions "unanswered" —
investigated and found these were substantive, verse-citing answers the model simply never
converted into structured `occurrences`, so `recordingpass.py` correctly wrote them with zero
`ib_node` grounding (indistinguishable, as currently built, from a genuine "no evidence" finding).
Isolated to this one run (checked both clusters, nowhere else). A re-read fixed it, but exposed two
more real, previously-undiscovered gaps in the process:

- `cluster_subgroup.status='re_read_needed'` is a defined enum value with **zero transition logic
  anywhere** — no sanctioned way to reset a subgroup for a legitimate re-read. Required a manual
  one-off `UPDATE` to unblock.
- `batchcontrol`'s resume/skip (built this same session, §2) can't distinguish "recovering from a
  crash" from "deliberately re-doing already-committed good work" — both hit the identical
  content-key and get refused identically. Required manually invalidating the prior `committed`
  `run_batch` row (marked `failed` with a clear explanation, not deleted) to let the retry proceed.
- The re-read itself doesn't retract/supersede the prior bad observations — confirmed live: M83/B
  now carries 108 `char-answers` rows where ~52–70 would be expected, the original 38 ungrounded
  rows still present as orphaned dead weight alongside their proper replacements.

All of this, plus the researcher's own question ("what safeguards/integrity tests can we build to
catch this, not leave it for manual discovery") consolidated into escalation #1765 — including two
more real, pre-existing gaps found in the same investigation: the completeness checks
(`compute_strong_checks`/`compute_question_checks`) are genuinely code-computed but never actually
gate/escalate, only narrate into a message string (direct precedent in this codebase for the fix:
`reports.py`'s `_validation_outcome`, rebuilt 2026-07-30 for the identical defect elsewhere); and no
standing DB-wide audit of `ib_observation`/`ib_node` integrity exists at all (`configmaint.validate`/
`spine.check` don't touch either table). The researcher answered the "what happens to superseded
observations" sub-question directly: extend the already-existing but currently `synthesis`-stage-only
`ib_observation.supersedes_observation_id` column (self-referencing chain, already exists, zero
schema change needed) rather than true overwrite (would destroy provenance) or a new soft-delete
column. Direction approved, escalation #1765 closed with the build explicitly deferred (researcher
flagged being at ~89% of weekly usage this same session).

Also raised, same conversation: escalation #1766 (an app-wide bulk purge utility for soft-deleted
rows, the researcher's own request, distinct scope from #1765) — real design questions laid out
(FK safety, retention window, table scope, dry-run discipline), not built.

## 5. Multi-angle data-quality audit (researcher's own request)

Systematic sweep across completeness/quality/purpose/orphans/inconsistencies, one escalation per
genuine finding as instructed. Came back clean on: empty subgroup families, orphaned `ib_node`
strong references, stale `cluster_code` attribution vs. current `cluster_strong` membership,
`cluster.status`/subgroup-rollup consistency (checked every cluster past ordinal 2, not just this
session's own two), dangling `cluster_code` references, undetected exact-duplicate observations,
dead `run_batch` rows, and the D9.x/science-extract + D7.7.1 battery exclusions. Two genuine
findings raised: **#1769** (one observation with literal `obs_text='placeholder'`, past the
existing degenerate-text regex which only catches none/n-a/null patterns) and **#1770**
(`answered-no-flag` tag at 84.2% of all `char-answers` observations — flagged against direct
precedent, BUILD.md #283 already fixed a similar 77% situation once).

Separately, investigating a researcher-spotted anomaly (`G0189` looking like an "orphan" awaiting
its home cluster `M42`) led to tracing the front-loading mechanism precisely: the strong's real
home is `M41` (not M42), already correctly attributed via `_effective_cluster_code`, front-loaded by
M49's own Stage 1 pass touching the same verse for an unrelated reason. Quantified the scope live:
74 of 92 not-yet-processed clusters already carry front-loaded coverage — 1,390 observations across
557 strongs — a real discoverability gap (nothing distinguishes "analysed" from "has a front-loading
head start" at a glance), raised as escalation #1768 with a small, cheap report proposed as the fix.

Later, the researcher spotted `ib_observation.meaning_source` didn't look enum-governed while
browsing raw data. Confirmed: a real `cfg_enum` exists with exactly the 3 documented values, but
`recordingpass.py` has no write-time validation gate for it (unlike `tag`/`question_code`/
`obs_text`, which all have one) — 42 distinct free-text variants live in the data (separator/naming
inconsistency plus values that don't belong in this column's vocabulary at all). Raised as
escalation #1771.

Following up on #1770's own finding, the researcher's practical pivot-table workflow surfaced the
precise root cause: `charanswergenerate.py`'s prompt offers all 19 registered `tag` values but only
explains 3 of them, with `answered-no-flag` explicitly framed as the catch-all — the other 16
(including `cluster-pole-positive`/`cluster-pole-negative`, the most obvious candidate for actually
differentiating the 84% bucket) are named with zero guidance. Updated #1770 with the precise cause
and a concrete fix direction, moving it from "worth monitoring" to "actionable prompt fix."

## 6. Ad hoc SQL/data investigation (researcher's own live debugging)

Diagnosed a row-fan-out bug in the researcher's own exploratory query (`Untitled-1`): two strongs
(`G0691`/`G0692`/`H8220`, confirmed all three) carry simultaneous active `cluster_strong` membership
in both their own M-code and the `T2` role tag, and the query's `cluster_strong` join wasn't
restricted to `cluster_code LIKE 'M%'`, silently doubling ~335 of 758 result rows even though `cs.*`
wasn't in the SELECT list at all. Gave the precise fix. Separately confirmed the `window` column
(`wa_obs_question_catalogue`) holds clean data with no embedded quote characters, but was declared
unquoted in its own `ALTER TABLE` migration despite being a genuine SQLite keyword — works today
only because SQLite's parser is lenient in this position, confirmed via direct testing (bare,
`WHERE`-clause, and table-qualified forms all succeed unquoted) — flagged as a minor defensive-
cleanup item, not escalated formally (researcher didn't ask for a ticket on it).

## Escalations touched

- **#1754, #1755** — `ib_node` seq collision (§1). Self-correctable, closed.
- **#1756** — batch-run control mechanism (§2). Decision-required, researcher-approved design,
  built and closed.
- **#1757** — `ps tools worksheet.xlsx` drift, 6 missing tabs + 1 stale flag column found while
  registering `BatchProgress.ps1`'s own tab. Self-correctable, fixed live (backup taken first),
  closed.
- **#1758, #1759, #1760** — `run_batch`'s own UNIQUE-constraint bug (§2). Self-correctable, closed.
- **#1761** — M49/M83 over-cap strong, surface-split design (§3). Decision-required, researcher-
  approved across a multi-turn clarification, built and closed.
- **#1762** — transient bad-model-response (JSON formatting slip) during M83 subgroup D's reading.
  Self-correctable, retried, closed.
- **#1763, #1764** — M83 subgroup B re-read blocked by its own status precondition and by
  `batchcontrol`'s resume/skip (§4). Self-correctable (expected refusals, not bugs), closed.
- **#1765** — analytical corpus integrity, 4 gaps (§4). Decision-required; researcher answered the
  supersede-vs-overwrite question, direction approved, build deferred, closed.
- **#1766** — app-wide soft-delete purge utility (§4). Decision-required, **open**, assigned to
  researcher.
- **#1767** — two-tier `cluster.reading` redesign (§3). Decision-required, **open**, assigned to
  researcher — M83 subgroup A blocked on this.
- **#1768** — front-loaded observations discoverability gap (§5). Decision-required, **open**,
  assigned to researcher.
- **#1769** — placeholder/filler `obs_text` validation gap (§5). Decision-required, **open**,
  assigned to researcher.
- **#1770** — `answered-no-flag` tag dominance (§5). Decision-required, **open** (`in-progress`,
  root cause and fix direction added), assigned to researcher.
- **#1771** — `meaning_source` enum not enforced at write time (§5). Decision-required, **open**,
  assigned to researcher.

## Files created or changed

- `iba/app/lib/recordingpass.py` — `record_one_observation` seq fix (§1).
- `iba/app/migration/create_run_batch_table_v1_20260918.py`,
  `iba/app/migration/fix_run_batch_unique_constraint_v1_20260918.py` — new, both run live (§2).
- `iba/app/lib/batchcontrol.py`, `iba/app/lib/batchprogressreport.py`, `iba/app/ps/BatchProgress.ps1`
  — new (§2).
- `iba/app/handlers/lexical.py` (`meaning`), `iba/app/handlers/cluster.py` (`subgroup`/`reading`/
  `answer`), `iba/app/handlers/reports.py` (`batch_progress_report`) — `batchcontrol` integration
  (§2) and the surface-split multi-package loop (§3).
- `iba/app/lib/charreadinggenerate.py` — `_partition_occurrences_by_surface`,
  `MultipleOverCapStrongs`, `assemble_subgroup_packages` (§3).
- `iba/docs/ps tools worksheet.xlsx` — 6 new tabs + Index rows, `Config-Maintenance` `-Title` column
  inserted (§1 note above under #1757); `iba/docs/archive/ps tools worksheet-backup-pre-1756-
  20260918.xlsx` — new, pre-edit backup.
- `iba/app/BUILD.md` — entries #291–#296 (every fix/build above).
- `iba/app/db/iba.db` (not git-tracked) — `run_batch` table + full config registration; two manual
  one-off corrections during §4's re-read incident (M83/B `cluster_subgroup.status` reset,
  `run_batch` row invalidation), both explained inline at the time, not silent.
- `_analytics/lexical-extracts/lexical-llm-usage.csv` — real per-batch cost log, every live call
  this session.
- `iba/app/reports/batch-progress*.md` (+ `archive/`) — live monitor output, regenerated repeatedly
  through the session.
- `outputs/escalation/*.md`, `research/discovery/spine-check*.md` — session-start orientation +
  ad hoc escalation-history reads (verifying the #1761 overlay-mixup, among others).

## Decisions

**Researcher's own:** M83 pipeline authorization ("proceed as a continuing pipeline unless a major
issue"); the `run_batch` generic-vs-bespoke design call (§2); the surface-split packing rule
("if >100 in total, then break in two based on SURFACE," §3); the decision to leave M83 subgroup A
blocked rather than patch around it (§3); the supersede-via-existing-column direction (§4); the
instruction to raise-not-fix for both the two-tier redesign (§3) and the full audit sweep (§5).

**Self-correctable, closed by Claude directly:** the `ib_node` seq bug (§1), the `run_batch` UNIQUE-
constraint bug (§2), the `ps tools worksheet.xlsx` drift (§1 note), the status-precondition and
resume/skip refusals during the M83/B re-read (§4, both expected behavior working as designed, not
bugs — closed as such).

**Left for the researcher, not decided here:** all 6 currently-open escalations (#1766/#1767/#1768/
#1769/#1770/#1771) — genuine judgement calls (architecture direction, priority against the usage-
limit constraint, or content-vocabulary decisions) deliberately not made unilaterally.

## Open items for the next session

- **M83 subgroup A** — blocked on escalation #1767's two-tier redesign. Once that lands, M49/M67/
  M83 likely all need re-reading (the redesign supersedes the current single-call Stage 3, not just
  extends it).
- **Escalations #1766, #1767, #1768, #1769, #1770, #1771** — all `decision_required`, all sitting
  with the researcher, none built. #1770 now has a concrete fix direction (add explicit tag guidance
  to `charanswergenerate.py`'s prompt) if the researcher wants it prioritized.
- **M83 subgroup D's own smaller grounding gap** — 5 of 52 battery questions showed the same
  ungrounded-but-substantive pattern as B's incident (§4), at much lower severity; noted but not
  re-read this session, given the usage-limit context.
- **`wa_obs_question_catalogue.window`** — the column is declared unquoted in its own migration
  despite being a genuine SQLite keyword; works today only because SQLite's parser tolerates it in
  this position. Minor defensive-cleanup candidate, not escalated (researcher didn't request a
  ticket).
- Offered, not yet acted on: a durable reference document mapping the analytical value-chain
  (spine → Layer 1 role → Stage 1–4 → future synthesis) for the researcher's own future reference,
  since the running theme of several exchanges this session was difficulty holding the full model
  in mind at once.

## Git state

Branch `main`, commit `3cb8f70002caee5021eaab83a4ee6c914bd266fa`, pushed to `origin/main`
(`7baeb271..3cb8f700`). `git status` confirmed clean working tree, up to date with remote.

