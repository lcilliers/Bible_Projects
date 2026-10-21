# Split word-level and relational Stage 1 steps — build plan

Escalation #1860. Approved v3 (researcher, verbatim): "proceed with split. Ensure that you comply
with every aspect of governance, and properly validate that steps taken is complete and achieve the
objective. The object is that the word observations is run corpus wide for all verses, and that the
observations quality is correct for the relational phase. worse result would be that relational
quality is compromised and the base data must in any case be included for relational phase to be
successful."

Concrete plan already on record in #1860 v1 context (5 parts). This document fixes the exact
implementation shape before touching code/config.

## Scope split

- `lexical.meaning` (existing step, narrowed): word-level only — `M0.1.*`, `M0.5.*` (incl. `M0.5.11`).
- `lexical.relational` (new step, ordinal 7, same work package `verse-lexical`, handler
  `iba.app.handlers.lexical:relational`, scope=cluster): `M0.6.5`, `M0.6.6`, `D7.7.1`, `M0.7.*`,
  `M0.8.1`.
- Both write `ib_observation`/`ib_node` with `stage='verse-reading'` (unchanged) — the split is a
  cfg_step/handler split, not a new analytical stage; `stage1coverage`'s combined completeness
  checks (used by `clusterstatus`) keep working across both without change to that value.

## Readiness gate (part 3)

`lexical.relational` refuses to run — hard stop, same shape as `lexical.build`'s stale-role check
and `lexical.readiness`'s FATAL stop, not a silent per-verse skip — until every M-code word in the
requested verse scope has a committed (non-withdrawn) `ib_observation` row with
`stage='verse-reading'` and `question_code LIKE 'M0.1%' OR 'M0.5%'`. New helper
`stage1coverage.missing_word_level_coverage(conn, verse_ids)` returns the (verse, strong) gaps; a
non-empty result fails the run with a sample and a "run lexical.meaning for these verses first"
message. Operational consequence (intended, matches the researcher's stated objective): word-level
coverage must be built out corpus-wide before relational is run at all for a given verse.

## Grounding (part 4, corrected by the researcher's approval caveat)

Claude's v1 draft proposed relational reading COMMITTED word-level `ib_observation` rows *instead*
of raw `meaning_sources_by_strong` lexicon text. The researcher's approval explicitly overrides
that: "the base data must in any case be included for relational phase to be successful." Relational
therefore gets **both**: `word_level_findings_by_verse` (committed M0.1/M0.5 `ib_observation.obs_text`
for that exact verse+strong, the span-grounded finding) **and** `meaning_sources_by_strong` (the raw
lexicon, unchanged) — the committed findings are the primary grounding, the raw sources stay
available as the same complementary evidence every other stage already reads
(`read-3-sources-complementary`).

## Code split (part 5)

- `iba/app/lib/stage1coverage.py`: `_wired_question_codes`/`expected_nodes`/`validate_coverage`/
  `fully_covered_verse_ids` gain a `family` parameter (`'word_level'` | `'relational'`), each
  filtering to its own question-code subset. New `missing_word_level_coverage()` for the readiness
  gate.
- `iba/app/lib/versereadinggenerate.py`: `assemble_batch_package` splits into
  `assemble_word_level_batch_package` and `assemble_relational_batch_package`, sharing existing
  helpers (`_meaning_sources`, `_role_word`, `_prior_relational_context`, `_prior_network_context`,
  `_verse_cluster_agnostic_coverage`). New `_word_level_findings()` helper for relational grounding.
  Two `_instructions` builders (word-level / relational), sharing the tag-guidance and boundary
  text blocks.
- `iba/app/handlers/lexical.py`: `meaning()` narrows to word-level only (drops the D7.7.1/M0.6.x/
  M0.7/M0.8.1 catalogue query, elevation-candidate wiring moves to `relational()`). New
  `relational()` mirrors `meaning()`'s batch/cost/resume/coverage-validation structure, adds the
  readiness gate as its first check, and **moves** the `cluster.status`
  `t_cluster_assignment_completed -> ready_for_subgroup_allocation` transition check here (it's the
  true final stage of verse-reading now, not `meaning()`).

## Config layer

Applied via a one-off migration script (matches established project precedent for a
researcher-approved multi-row config build — see `iba/app/migration/*` history), not 15 individual
`Config-Maintenance.ps1 -Step Propose` cycles: `iba/app/migration/
split_lexical_meaning_word_relational_v1_20260923.py`.

- `cfg_step`: update `lexical.meaning.does` (word-level-only); insert `lexical.relational`
  (ordinal 7).
- `cfg_write_grant`: insert 3 rows for `lexical.relational` (`ib_observation`, `ib_node`,
  `run_batch`), mirroring `lexical.meaning`'s grants.
- `cfg_method_rule`: duplicate the 9 cross-cutting rules onto `step='lexical.relational'`
  (`read-3-sources-complementary`, `role-list-includes-unwired-tags`, `per-cluster-scope-not-
  subgroup`, `needs-adjacent-verse-context-applies-here`, `cost-bounded-small-batches`,
  `strongs-reassigned-detection`, `concise-and-verse-specific-obs-text`, `translit-never-
  without-gloss`, `span-grounded-not-generic`); retext `answers-M0.1-M0.5-D7.7` on
  `lexical.meaning` to word-level only; add a new relational-scoped catalogue-linkage rule on
  `lexical.relational`; **move** `cluster-status-2to3-transition-verse-reading-complete` from
  `lexical.meaning` to `lexical.relational`; add `grounds-on-committed-word-level-observations`
  (part 4) on `lexical.relational`.
- `cfg_setting`: insert `lexical.relational_max_verses_per_batch` = 1 (mirrors
  `lexical.meaning_max_verses_per_batch`'s current value; all other `lexical.llm_*` settings are
  already generic across steps, reused as-is).

## Validation before declaring this ready for corpus-wide use

1. Structural: both steps run `-Preview` clean against a small live cluster.
2. Live, tiny scope (1-2 verses, real API cost, same pattern as every prior live test this
   session): confirm `lexical.relational` actually refuses to run against verses with no word-level
   coverage yet (readiness gate fires), then confirm it runs clean once `lexical.meaning` has been
   run for those verses, and that `stage1coverage.validate_coverage(family='relational')` shows 0
   missing/unexpected for that scope.
3. Corpus-wide execution (word-level for all verses, per the researcher's stated objective) is a
   separate, larger cost decision — same pattern as every prior full-cluster/full-corpus backfill
   this session (M67, M49) — reported back for a go-ahead, not run unattended as part of this build.
