# SESSION LOG — 2026-08-11/12 — power-failure recovery; morphless-span bug re-fixed and swept; report-export governance gaps found and fixed; `strong.origin` (word/backfill) split; cluster model fully adopted into IBA (T2/T3, LLM allocation + prior reassignments)

Recovered from a power failure mid-session, then executed the resulting plan end-to-end. Spans two
calendar dates (started 2026-08-11, closed 2026-08-12) as one continuous unit of work — grouped
here by thread, not by clock time.

## 1. Recovery (plan mode)

Power failed mid-session. The interrupted session's plan-mode file
(`first-raw-data-vivid-fairy.md`, answering BUILD.md §101 Fork (b) — raw-data-integrity vs.
completed analysis) survived intact on disk. Verified nothing was lost before doing anything else:
`git status` clean, no `SESSION-LOG-20260811-*` for the interrupted thread (it never reached its
own close step), the plan file itself read as complete, not truncated. Adopted in full into a new
plan file, then extended through several rounds of researcher direction:

- **T2 precedent researched** — the old project's `01c-T2-treatment-and-API-governance.md`
  (canonical, 2026-06-17): T2 is a POS-split spectrum (content vs. grammatical), not a disposable
  noise bin, corroborated by earlier memory findings the researcher had to correct once already.
- **`receive`'s 2026-08-10 rollback re-litigated.** Researcher's own review: the "79%
  high-frequency-code noise" framing overstated it — investigating those seeds surfaced a real,
  previously-unadopted category (physical-action/perception verbs: see/eyes/give/take/walk/run/
  arm) that legitimately bears on the inner being but can't be filtered at `raw.discover` time,
  only per verse-occurrence. Working thesis: discovery-time exclusion is only valid for what's
  decidable without verse context (grammatical particles, proper nouns) — everything else has to
  be decided downstream.
- **Filter re-triage**: T2-style POS exclusion and proper-noun exclusion → `raw.discover`-safe,
  config-driven. F1–F5 (lexical-family) → safe for its own narrow purpose, not a general filter.
  GR-PROG-007 and the physical/action category → downstream only.
- **Cluster-model adoption approved** — Fork (a) merged into Fork (b)'s plan. Sequenced alongside
  the rows 5–7 lexical build spec, not before/after.
- **Span-regex bug flagged for inclusion** — traced full history (found 2026-07-25, fixed
  2026-08-10 during `receive`'s build, reverted the same day by `receive`'s rollback, confirmed
  still live). Ramifications laid out before acting: `blindness` (built after the rollback) is
  exposed too; the debated-book corpus (Dan/Jonah/Joel/Obad/Micah/Hosea) predates the only window
  the fix was ever live, so all of it was built under the bug.
- **`raw-complete` redefined** (researcher, verbatim): "raw complete can only be signed off when
  the lexicals of the underlying verses have been completed... for the strong(s) involved with a
  word" — in place, not a new downstream status. All 178 existing `raw-complete` words are back in
  scope for re-checking, not grandfathered.
- Plan approved; any analytic work touched by any of this "will be revisited... nothing to worry
  about" (researcher) — not a blocker on anything below.

## 2. Morphless-span bug — re-derived, corpus-validated, re-fixed, swept (BUILD.md §102)

Not a blind re-apply of the 2026-08-10 fix — its exact regex string was unrecoverable (the
rollback erased the `cfg_change_detail` row too). Re-derived from BUILD.md's description and
**tested against the full live corpus before proposing anything** — caught a real problem a naive
re-implementation would have shipped: a bare "make morph optional" regex silently drops the morph
VALUE on ~370,000 already-working spans (classic greedy-backtracking trap). Scanned every
content-span tag corpus-wide to enumerate the real attribute shapes (4, not 2 — `var` can precede
`morph`) before finalising. Zero regressions, zero missing spans, confirmed against the historical
824-verse/1,077-span/24-code figures exactly.

Applied via `configmaint.propose` (escalations 599/600): `cfg_setting step.span_html` fixed;
`cfg_write_grant migration→span` re-added. Backfill migration (`backfill_morphless_span_fix_
20260810.py`, confirmed by reading it that it live-rescans every verse, not a stored list — safe
to reuse as-is) dry-run matched exactly, applied: 13,268 soft-deleted, 14,345 inserted. Re-scanned
clean: 0 verses differ from a fresh parse.

**Debated-books cross-check: zero overlap.** None of the 824 affected verses fall in Daniel/Jonah/
Joel/Obadiah/Micah/Hosea — the completed HIB/phenomenon/operation work on those six books was not
built on this specific gap (book-prefix counts sanity-checked first, so this is a genuine zero).
`verse_lexical` for the 824 touched verses NOT yet rebuilt — deliberately deferred into the rows
5–7 build spec (still queued, §6 below), since spans changing doesn't propagate downstream
automatically today.

## 3. Cluster tables bootstrapped and seeded from the old project (BUILD.md §103)

New tables `cluster` (49-row taxonomy) and `cluster_strong` (the link — deliberately no FK/
dependency on `word_strong`/`word_registry`), bootstrap-direct (new tables, `configmaint.propose`
can't create them). Seeded from a **fresh live query against `bible_research.db`**, not the
17-day-old Fork (a) CSV checkpoint: 2,801 `cluster_strong` rows, covering 2,709 of IBA's (then)
15,293 `strong` rows.

## 4. Report-export governance gaps found and fixed

Two separate researcher-caught findings, same thread:

- **Real gaps in `cfg_report_csv_table`** across the registered report steps — checked every
  report's actual code (not just the config), corrected two false positives from an initial
  whole-file-grep pass along the way (`report.word`/`passage.validate` were actually fine).
  Confirmed and fixed 4 real gaps via `configmaint.propose`: `report.strong_meaning` (missing
  `strong`/`strong_lexicon`), `report.span_analysis` (missing `verse`), `lexicon.validate`
  (missing `strong`/`strong_lexicon`), `report.registry` (missing `word_strong`). Re-ran all
  affected reports; verified the new CSVs land in `reports/export/` via the archive-on-regenerate
  mechanism (confirmed live: old versions correctly moved to `archive/`).
- **My own governance violation, self-caught after being challenged.** The cluster CSVs (§3's
  output) were written by a raw ad hoc Python script straight into `iba/app/reports/`, bypassing
  `reportkit`/`cfg_report_csv_table` entirely — exactly the shortcut `governance.
  rules_must_be_config_driven` exists to prevent. Fixed properly, not patched around (§5 below).

(Separately: `report.registry`'s regenerated `word_strong.csv` briefly went missing from
`export/` — traced to the researcher's own manual archive sweep of the whole export folder
catching a file freshly regenerated minutes earlier, not a bug in the fix; re-ran the report to
restore it.)

## 5. `strong.origin` ('word' | 'backfill') — the real cluster-relevance boundary (BUILD.md §104)

Researcher: `strong` holds two fundamentally different kinds of row, and cluster/meaning-relevance
work had been conflating them. Traced the actual source of the ~11,800 `strong` rows with no
`word_strong` link (a live open question from earlier in the day) precisely: `raw.backfill_meaning`
(`handlers/raw.py:backfill_meaning_for()`) — a book-scoped completeness sweep, independent of any
word — confirmed via direct overlap check (11,835/11,837 = 99.98% exactly explained, not assumed).

Added `strong.origin` (bootstrap-direct ALTER TABLE), one-time-classified against live
`word_strong` linkage (3,456 'word' / 11,837 'backfill'). Fixed the actual write path
(`handlers/raw.py:detail_one()` — confirmed the only place anything writes to `strong`) to stamp
origin at creation and upgrade 'backfill'→'word' (sticky, never the reverse) when a code is later
legitimately claimed by a word. Caught and fixed a real bug in that upgrade path before it shipped:
`Db.upsert()` is dedup-only, would have silently no-op'd — switched to a direct `update()`.

**This corrected the actual cluster-allocation scope**: rescoped to `origin='word'` only, the real
gap was **1,612**, not the 12,584 figure quoted earlier in the day (which wrongly included every
backfill-origin code — never in scope for cluster mapping at all).

**`report.cluster` built** as the proper replacement for §4's ad hoc script — `lib/clusterreport.
py`, wired into `handlers/reports.py`, registered via `configmaint.propose` (6 rows: `cfg_setting`/
`cfg_work_package`/`cfg_step`/`cfg_report`/`cfg_report_csv_table`×3), own `Cluster-Report.ps1`. Ran
end-to-end, verified correct output; the 3 superseded ad hoc CSVs archived (moved, not deleted).

## 6. LLM-assisted cluster allocation processed (BUILD.md §105, §106)

Researcher ran the allocation round themselves (a separate chat, per the established Claude AI /
Claude Code role split), using `report.cluster`'s own three CSVs as the input package as discussed
in advance. Two batches came back, both validated rigorously before writing anything (exact-set
cross-checks against the live gap list, cluster-code validity, internal tally consistency, live-DB
field-fidelity checks — every check passed clean on both files, 0 discrepancies):

- **`wa-global-t3-cluster-record-v1_0` + `wa-global-cluster-alloc-final-v1_3`** — new cluster `T3`
  ("Operations" — human operations/movements not tied to one inner-being cluster; directly closes
  the physical-action-verb category §1 identified) + 1,612 assignments, exactly the word-origin gap
  set. Additions only. `cluster_strong` extended first with the source file's own evidence schema
  (`confidence`/`operation`/`alt_clusters`/`review_flag`/`rationale`) rather than discarding it on
  write — 574 rows carry `review_flag=1`. Applied: gap now zero.
- **`wa-global-prior-reassignments-v1_1`** — the third companion file, referenced in `v1_3`'s own
  metadata but not initially provided; asked for, then supplied. 218 `(strong, from_cluster) →
  to_cluster` moves revising the *original* 2,801 old-system-migration rows (not the additions
  above). 15 within-file duplicate targets (multi-cluster strongs moving both a T2 and a FLAG
  instance to T3) deduplicated correctly. Applied via the codebase's standing "supersede, never
  overwrite in place" convention: 218 soft-deleted, 203 new rows inserted.

**Final state: `cluster_strong` = 4,398 active rows** (2,801 − 218 + 1,612 + 203, reconciles
exactly). The word-origin cluster-relevance gap that opened this whole thread is fully closed.

## Left open, not silently dropped

- **`lexicon.validate` escalation still paused** (`RUN-20260811_172851_742`) — 6 minor coverage
  gaps (2 missing LSJ parses, 2 missing Mounce parses, 2 unfetched `strong_related`), surfaced
  incidentally by re-running the report for §4, unrelated to anything else this session. Awaiting
  researcher decision (Approve as known state / Reject to action).
- **Filter re-triage build** — the config-driven T2-grammatical + proper-noun exclusion at
  `raw.discover`, approved in principle in §1, not yet built.
- **`receive` rebuild** — decided in §1 (fresh rebuild, not rollback-undo), not yet executed.
- **Rows 5–7 build spec** (parsed-meaning completeness gate, verse-scoped `verse_lexical` rebuild
  trigger, downstream provenance/fingerprinting) — deliberately last in sequence, depends on
  everything above being stable first. Now that the cluster/span/report threads are closed, this
  is next.
- **`raw-complete` redefinition** — decided in §1, depends on rows 5–7 existing before it can be
  wired into `raw.write`/`validation.py` and the 178 existing words re-checked.

## Files touched (this session)

**New code:** `iba/app/lib/clusterreport.py`; `iba/app/migration/bootstrap_cluster_tables_
20260811.py`, `bootstrap_strong_origin_column_20260811.py`, `bootstrap_cluster_strong_evidence_
columns_20260812.py`, `apply_cluster_alloc_v1_3_20260812.py`, `apply_prior_reassignments_v1_1_
20260812.py`; `iba/app/ps/Cluster-Report.ps1`.

**Modified code:** `iba/app/handlers/raw.py` (`detail_one()` origin parameter + sticky-upgrade
logic; `detail()`/`backfill_meaning_for()` call sites); `iba/app/handlers/reports.py`
(`cluster_report` + import).

**Schema:** `cluster`, `cluster_strong` (new tables); `strong.origin` (new column);
`cluster_strong` +5 evidence columns. All bootstrap-direct.

**Config, via `configmaint.propose`** (escalations 597→614 across this session): `step.span_html`
fix; `cfg_write_grant migration→span`; `cfg_report_csv_table` ×4 gap fixes; `report.cluster`'s full
registration (6 rows).

**Data:** `span` (13,268 soft-deleted / 14,345 inserted); `strong.origin` backfilled (15,293 rows);
`cluster` (+50 rows: 49 migrated + T3); `cluster_strong` (2,801 seeded → 4,398 final, net of the
allocation + reassignment batches above).

**Source files processed (researcher-provided):** `iba/docs/cluster assignment process/
wa-global-t3-cluster-record-v1_0-20260811.json`, `wa-global-cluster-alloc-final-v1_3-20260811.
json`, `wa-global-prior-reassignments-v1_1-20260811.json`.

## Next

Filter re-triage → rows 5–7 build → `raw-complete` redefinition + 178-word re-check, in that
order, per §1's sequencing. `lexicon.validate` escalation awaiting a quick researcher decision
first (low-stakes, not blocking the above).
