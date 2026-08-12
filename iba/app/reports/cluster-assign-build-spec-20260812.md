# Build spec — cluster-assignment module (executable version of v3's plan)

> Written before coding, per standing instruction: save planning to files, record progress to
> files, so a power failure has a recovery point. Rationale/history lives in
> `backfill-cluster-triage-plan-v2/v3-20260812.md` — this file is the concrete, ordered thing being
> built, kept current as work proceeds. Researcher has pre-authorised this build; individual
> `configmaint.propose` rows are self-approved as they're raised, per instruction — reviewed as a
> whole once built, not gated step by step.

## Design simplification made while grounding this against the dispatcher (`run.py`)

Traced how escalation actually works: only a **top-level dispatched handler's** returned `Outcome`
gets routed to `escalation` by `run.py` — a nested library call can't escalate on its own. Rather
than thread escalation-handling through every call site (`backfill_meaning_for`, new-word's
`raw.write`, the DB-wide sweep), **all exception-shape reporting concentrates in one place:
`cluster.validate`**, mirroring `lexicon.validate` exactly (read-only, DB-wide, escalates once if
findings exist, Approve/Reject/Revise). `strong.reconcile()` itself stays a small, pure function —
classify, decide, promote-or-leave — never escalates, never silently resolves an exception shape
(just declines to promote and leaves the code visible to the next `cluster.validate` run). This also
answers Q2.4.1's "one-time vs standing" split for free: the *first* `cluster.validate` run naturally
reports the full historical backlog (nothing's been reconciled yet); once the researcher resolves it,
later runs report clean, and anything new is visibly "happening again" — no separate one-off/standing
code paths needed, it falls out of how a periodic validate-and-escalate check already works
everywhere else in this app.

## Components, in build order

1. **`lib/clusterassign.py`** — mechanical precedent matcher. `match_precedent(cfg, strong_row) ->
   (cluster_code, rationale) | None`. P1 (exact gloss match to an existing labelled `cluster_strong`
   row) + P2 (exact gloss match to `cluster.gloss`'s list), HIGH-confidence only. Reuses the session
   log's own pitfalls: exclude `FLAG`'s gloss list from voting; token/stem match with word
   boundaries, not substring. Config-driven: match thresholds/excluded-cluster-list as `cfg_setting`
   rows, not literals in code.
2. **`lib/strongreconcile.py`** — `reconcile(ctx, code) -> dict`. Classify (lookup, else mechanical
   match) → exception check (flag only, never silently resolve) → promote-or-leave. Promotion reuses
   `raw.verses_one()` and `lexical.build_for_verse_ids()` unchanged — no new fetch mechanism.
3. **`handlers/cluster.py`** — `cluster.assign` (DB-wide sweep, calls `reconcile()` per unclassified
   strong) + `cluster.validate` (read-only coverage/exception report, escalates, same shape as
   `lexicon.validate`).
4. **Wiring**: `raw.py:backfill_meaning_for()` calls `reconcile()` for each newly-backfilled code;
   new-word chain calls `reconcile()` for each of the word's own codes (point c — absorbs what the
   `receive` rebuild was scoped to wire in, per v3 §c).
5. **Config**: new work package `cluster-assign` (steps `cluster.assign`/`cluster.validate`, both
   `kind=operations`... `cluster.validate` more likely `kind=utility`, matching `lexicon.validate`'s
   own classification — checked at registration time); `cfg_write_grant` (`strong.reconcile` →
   `strong` for the origin flip; reuses `call3_strong`/`lexical.build`'s existing grants for
   verse/span/lexical writes, `cluster.assign` → `cluster_strong`); `cfg_on_fail` (`cluster.validate`'s
   escalate condition → `pause-continue`); `cfg_setting` rows for the matcher's tunables.
6. **`ps/Cluster-Assign.ps1`** — `-Step Assign|Validate`, same shape as `Lexicon-Parse.ps1`.
7. **Test forwards**: a fresh/synthetic promotion scenario end-to-end. **Test backward**: re-run
   `cluster.validate` and spot-check `blindness`/`Suffering`/the six debated books are unaffected or
   correctly reported, not silently altered.
8. **BUILD.md** new numbered section; this file kept updated as a running progress log alongside it.

## Progress log

- 2026-08-12 — spec written, starting build.
- 2026-08-12 — `lib/clusterassign.py`, `lib/strongreconcile.py`, `handlers/cluster.py` built.
  `raw.py` wired at both surfacing points (`backfill_meaning_for()`, new-word ordinal 7). All
  modules import-clean.
- 2026-08-12 — 16 `configmaint.propose` rows applied, self-approved per standing authorisation (see
  BUILD.md §107 for the itemised list). One round-trip on a real coherence-check catch
  (`cfg_setting.value` needed JSON-quoting for a path string) — fixed, reapplied clean.
  `ps/Cluster-Assign.ps1` built.
- 2026-08-12 — **first live run, `cluster.validate`**: 10,972/15,293 unclassified; 428 no-word
  exceptions; 481 sibling-conflict exceptions. Escalated cleanly
  (`RUN-20260812_155001_294-CLUSTER-ASSIGN`), report at `iba/app/reports/cluster-assign-v1-
  20260812.md`. **Left open for the researcher** — a data-content decision, not covered by the
  config pre-authorisation.
- 2026-08-12 — **first live run, `cluster.assign`**: 1,410 new mechanical classifications written
  (`cluster_strong` 4,398 → 5,808); **0 promotions**. Traced why: every promotion candidate hit the
  no-word exception first — `backfill`-origin codes structurally almost never carry their own
  `word_registry` link, so exception 1 is the dominant outcome for a non-T2 `backfill` code, not the
  rare case the name implies. Backward check clean: `blindness`, the six debated books' `hib` count,
  and `word_registry`/`strong` totals all unchanged; zero destructive side effects.
- 2026-08-12 — BUILD.md §107 written. Build complete as scoped; real-scale finding (no-word
  exception dominance) surfaced to the researcher rather than resolved unilaterally — see BUILD.md
  §107 "Left open."
