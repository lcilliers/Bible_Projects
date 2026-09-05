# Session log — 2026-09-05

**Scope, one line:** Fixed a real, live data-integrity defect in Window 1's `verse_lexical` write
path (identity-stable CRUD redesign, escalation #1520) after the researcher judged the earlier
patch-shaped fix "not good enough"; fixed the `VerseLexical.ps1` ps-tools worksheet and wrote a
proper payload guide after the researcher hit a broken example and an undocumented payload format;
then, at the researcher's direction, built a full heuristic family-grouping pass over the M01-M47
lexicon (78 evidence-checked families, 87% coverage) and used it to rebuild the M-cluster taxonomy
itself (47 → 85 clusters, 41 renamed in place, 37 new) — closing escalation #1006 along the way.
Worked five escalation-backlog items to real completion or correct hand-off (#1520, #1506, #1006,
#738, #737), including catching and correcting two of my own mistakes on the record (a missed
instruction on #737, an overcorrected close on #738). Session ends at the researcher's initiative
to log and clean before starting #737's Window 2 realignment work next session.

## Escalations touched, by id, with outcome

- **#1520** (auto-raised, "11 item(s) need reconciliation" report-stop) — root-caused, not just
  patched: `write_readings_for_span`'s "soft-delete + insert on every run, even unchanged" write
  path silently orphaned `verse_lexical_note` rows on any Layer-1 rebuild. First fix (a same-verse
  precheck in `VerseLexical.ps1`, BUILD.md #234) was judged "not good enough" by the researcher —
  *"you have designed lexical findings system that seems to me to be highly inefficient... build a
  proper CRUD system with proper controls... no use for you to ask me to select between A or B."*
  Redesigned `write_readings_for_span` to be identity-stable (same pattern as `phenomenon_set`'s
  own in-place UPDATE, reused not invented): unchanged content → no write; changed content → real
  `UPDATE`, same id; genuinely-removed slot → real soft-delete, now counted as
  `removed_with_live_notes` rather than silently dangling. **Completed** (self-resolved,
  `ready_for_approval` not needed — self-correctable, verified live).
- **#1506** (`configmaint.propose`, already approved) — applied cleanly: `cfg_write_grant` for
  `lexical.enrich`/`passage` marked inactive, unused since #1451's verse-scoped redesign. →
  **completed**.
- **#1006** ("Cluster analysis framework") — reviewed and reported the cluster→sub-group "engine"
  on instruction: found there is no engine, only ~15 bespoke now-archived per-cluster load scripts;
  15 of 49 clusters ever got findings loaded, 36% of `cluster_finding` rows carry a
  `cluster_subgroup_id`. Follow-up found the real match for "loosely grouped strongs from the
  debate era": `lib/clusterassign.py`'s exact-gloss precedent matcher, still live. Demonstrated it
  against M08 live — real result, not hypothetical: only 13% clean match, confirming M08's own
  sub-groups are drawn on a per-verse interpretive dimension (seat of pride) a code-level tool
  cannot resolve. That finding launched the fresh, from-scratch family-grouping pass (below), which
  the researcher then used to rebuild the whole M-cluster taxonomy. → **ready_for_approval**
  (handed back with the historical-input-vs-fresh-design fork named, not decided unilaterally),
  overtaken in practice by the family-reallocation build itself.
- **#738** ("Cluster-Assignment Backfill Exceptions") — stale (2026-08-17 counts); closed in favour
  of a fresh `cluster.validate` run rather than acted on directly. → **closed**, superseded by
  #1523.
- **#1523** (auto-raised by that fresh `cluster.validate` run, current numbers 772/829) —
  researcher's own judgement recorded and left **open, in-progress**, not resolved: the exception is
  expected to wash out once the shared verses get analysed at the verse level under Window 2 —
  parked pending that, explicitly not abandoned.
- **#737** ("IBA Debate-Pipeline to research_db Migration (Gated)") — mishandled twice before
  landing right (see "My own errors" below): first correctly identified as gated with nothing
  actionable, but missed the researcher's own reopening instruction further down the same
  escalation's comment trail (Window 2 becomes the main focus, using the new M-cluster taxonomy as
  input; review previous Window 2 methods, align with the corrected window-2 thinking, deep-dive
  cleanout of old analysis findings; keep in progress, plan thoroughly first, do not close).
  Corrected once the researcher pointed it out directly. → **in-progress**, assigned to Claude,
  scoping question asked (start the review now vs. next session) — carried into next session per
  the researcher's own "log and clean first" instruction.

## Files created or changed

- `iba/app/lib/lexical.py` — `write_readings_for_span` rewritten identity-stable (`_CONTENT_FIELDS`,
  UPDATE-in-place for changed slots, no-op for unchanged, real soft-delete only for genuinely
  removed slots); `build_for_verse`/`build_for_range`/`build_for_verse_ids` count propagation
  (`inserted`/`updated`/`unchanged`/`removed`/`removed_with_live_notes`); module docstring rewritten.
- `iba/app/handlers/lexical.py` / `iba/app/handlers/raw.py` — message strings updated to the new
  count shape (would otherwise have thrown `KeyError` on next use — caught before it happened).
- `iba/app/handlers/reports.py` — `lexical_exceptions_report` gained a standing integrity section
  (dangling `verse_lexical_note` references, expected 0 always); `lexical_extract` gained a
  cluster-short-name column (computed at report time, exact-code join, not base-stripped).
- `iba/app/migration/add_verse_lexical_updated_at_v1_20260905.py` — new, one-off, additive
  (`verse_lexical.updated_at`, nullable) — replaces the old churn-for-a-timestamp reasoning.
- `iba/app/ps/VerseLexical.ps1` — `-SkipBuild`/`-ForceRebuild` (safe auto-detect default: build
  Layer 1 only if genuinely missing, never unconditionally); `-PassageFilter`/`-VerseFilter`/
  `-SurfaceFilter`/`-StrongFilter` added (found live: `report.lexical_extract` was in `-Step`'s own
  list with no way to actually supply its real parameters until these existed).
- `iba/docs/ps tools worksheet.xlsx` — `VerseLexical` tab rebuilt from one broken example row to 8
  real, individually-tested example rows covering every mode; new filter-param columns added.
- `iba/docs/lexical-enrich-payload-guide-v1-20260905.md` + `lexical-enrich-payload-example-rom-9-14-
  v1-20260905.json` — new: field-by-field payload guide + a real, already-tested worked example,
  because none existed and the researcher hit exactly that gap live.
- `iba/docs/1451-window1-layer2-verse-scoped-redesign-v1-20260905.md` — the verse-scoped Layer 2
  design record (researcher's own 4-question Q&A) from earlier in the session, referenced throughout.
- `iba/docs/1520-verse-lexical-crud-safety-review-v1-20260905.md` — full investigation, evidence,
  and resolution record for the CRUD redesign.
- `iba/app/migration/family_reallocation_v1_20260905.py` — new, one-off: 41 cluster renames, 37 new
  `cluster` rows (M48-M84), per-member `cluster_strong` corrections (609) and additions (1262), 45
  T2/T7/T8 reclassification inserts.
- `_analytics/clusters/m01-m47-family-grouping-iteration-v1-20260905.md` — full method record: the
  ordered-regex family-grouping technique (reused from `_apply_ib_char_family_grouping_v1_
  20260711.py`), two iteration rounds, every family quantified, the negation-prefix/spelling-gap
  findings, the crosswalk analysis, the researcher's own reallocation rule.
- `_analytics/clusters/m01-m47-strong-family-v1/v2/v3-20260905.csv`,
  `m01-m47-strong-surface-extract-v1-20260905.csv`, `m01-m47-surface-family-v1-20260905.csv` — the
  data trail, iteration by iteration.
- `_analytics/clusters/M08-Pride/wa-1006-cluster-subgroup-engine-review-v1-20260905.md` — #1006's
  review, plus the live M08 demonstration and the `clusterassign.py` discovery.
- Earlier-session (pre-compaction) migrations, now part of this same log: `iba/app/migration/
  add_adversarial_cluster_v1_20260905.py`, `add_negator_connective_partydivine_clusters_v1_
  20260905.py`, `add_party_human_angelic_clusters_v1_20260905.py`,
  `make_verse_lexical_note_passage_id_nullable_v1_20260905.py`,
  `rebuild_prose_section_fk_v1_20260905.py` (bible_research.db) — T4-T9 cluster builds and two
  schema fixes.
- `iba/app/BUILD.md` — #234 (VerseLexical auto-chain, superseded same day by #235), #235 (the CRUD
  redesign), #236 (the M-cluster rebuild) — plus earlier-session entries for the T4-T9 builds.
- `outputs/` — 8 superseded draft versions from the earlier 10-verse Layer 2 test work
  (`window1-10verse-verse_lexical*`, `window1-layer1-layer2-review*`, `window1-layer2-10verse-
  test*`) moved to `outputs/archive/` as this session's own close-out cleanup, per file-
  organisation-rules §2.3 (only the latest version stays in the active folder).
- **Database (not git-tracked):** `iba.db` — the CRUD redesign's schema/code changes plus their
  live corpus effect; the T4-T9 cluster builds; the 85-cluster family reallocation (`cluster` +38
  net rows, `cluster_strong` 609 corrected + 1262+45 inserted). `iba.db` backed up twice
  (pre-CRUD-redesign, pre-family-reallocation) under `backups/`.

## Decisions made

**Researcher's own decisions**, not self-correctable:
- Rejected the first #1520 fix outright and named the actual standard: *"you should know what a
  proper CRUD system with proper controls looks like... not [a] cop out."*
- Directed the family-grouping exercise's scope and stopping point twice: "approx 100 miscellaneous...
  about 100 groups... sounds manageable" (round-1/round-2 target), then, after seeing the crosswalk,
  the actual reallocation rule: *"keep the existing cluster numbers, but extend it to the full 80 or
  so... reallocations, reset the naming [are fine, can] fit the representative terms."*
- Directed the 47-item T2/T7/T8 reclassification scope ("place or names, persons... no inner being
  significance, body parts, devine etc... the remaining for now can be unassigned").
- Corrected two of my own escalation-handling mistakes directly (see below) rather than let them
  stand.
- Set #737's real instruction and scope (Window 2 becomes main focus, plan thoroughly first, do not
  close) — found in the escalation's own comment trail, not restated fresh in chat.

**My own judgement calls, made and documented at their own location**:
- T7 (not T2) is the wrong fit for "idol"/"idolatry" strongs despite the surface resemblance to
  "divine" — T7's own live definition is specifically the TRUE divine party (God/LORD/Christ); an
  idol is the opposite of that. Routed to T2 instead, with the reasoning stated plainly rather than
  forced into T7 for a superficial match.
- For the family→M-cluster crosswalk, used "largest family by member count wins the old number" as
  the tie-break rule — proposed before building, confirmed by the researcher, not decided silently.
- Left M10b/M10c (the same legacy anomaly the 2026-08-13 M10bc cluster review already flagged)
  completely untouched by the reallocation, on purpose — folding that separate, still-open decision
  into this migration would have been a design call riding on a different change's back.

**My own errors, caught and corrected on the record, not glossed over**:
- First #1520 fix (a same-verse precheck in one PS1 script) treated a symptom, not the root cause —
  named directly by the researcher, corrected same session with the actual identity-stable rewrite.
- On escalation #737: read the top-level gate note and my own prior comments, but missed the
  researcher's own reopening instruction sitting further down the same comment trail — moved the
  item to on-hold/Researcher (twice, compounding the error with a "correction" that was itself
  still wrong) before the researcher pointed out directly that they'd already reopened it to me.
  Found the missed text on the second read-through, corrected the assignment and state, and
  restated the instruction back to confirm understanding before proceeding.
- On escalation #738: closed it as superseded by a fresh #1523 without initially recognising that
  the fresh run's exception counts included 322 new touches from my own same-session family-
  reallocation work — caught and stated plainly in the close-out comment rather than presented as
  someone else's pre-existing number.

## Open items carried into the next session

1. **#737** — `in-progress`, assigned to Claude: Window 2 becomes the main focus of attention,
   using the new M01-M85 cluster taxonomy as input. Next step (not yet started): review the
   previous Window 2 methods and the 6 completed book debates (Daniel, Jonah, Joel, Obadiah, Micah,
   Hosea), align with the corrected Window 1/Window 2 model, deep-dive cleanout of the old analysis
   findings. Researcher's own instruction: plan thoroughly before executing; do not close this
   escalation.
2. **#1523** — `in-progress`, assigned to Researcher, deliberately parked: 772/829 cluster-
   assignment exceptions, expected to resolve via Window 2's own verse-level analysis rather than
   registry-promotion work done ahead of it.
3. **#1006** — `ready_for_approval`: the historical-input-vs-fresh-design fork for the old
   `cluster_finding`/`cluster_subgroup` corpus, effectively answered in practice by building fresh
   (the family reallocation) rather than reviving the old per-cluster load pattern — not yet
   explicitly closed out as such.
4. **Round-2 family-grouping candidates named but not built**: `glory-honor-splendor` (already
   built, since folded into the reallocation as M71), `fasting-piety-intercession` (also built, as
   M21's rename) — both already landed; genuinely still-open is whether a round-3 pass on the
   post-reallocation residual is wanted, or whether 331→post-reallocation-residual stands as-is
   pending Window 2's own verse-level pass making the question moot (per #1523's own parked
   rationale).
5. Session ending at the researcher's own initiative ("shall we do a session log and clean before
   starting work on 737") — not because #737 reached a natural stopping point; the scoping question
   asked at the end of the prior turn (start the Window 2 review now vs. next session) stands
   answered by this close-out itself: next session.

## Git state — this log's own completion trigger

- **Branch:** `main`, up to date with `origin/main`.
- **Commit:** `f416ffee` — "session 20260905: verse_lexical CRUD redesign (#1520 root-cause fix,
  identity-stable write path) + M-cluster taxonomy rebuild from heuristic family-grouping (47->85
  clusters, 41 renamed, escalation #1006 follow-up)" — 128 files changed, 108347 insertions(+),
  3452 deletions(-).
- **Push:** confirmed — `6bd7047d..f416ffee  main -> main` accepted by `origin`.
- **Post-push `git status`:** "Your branch is up to date with 'origin/main'." / "nothing to commit,
  working tree clean" — actual command output, not asserted.
