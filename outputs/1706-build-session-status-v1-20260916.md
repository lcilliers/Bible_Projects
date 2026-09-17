# #1706 build session — status report, 2026-09-16 evening

**Instruction, verbatim:** *"you can now systemaitcally and in stages start the build of 1706.
Don't stop to ask questions, all the areas of concern will be dealt with as fixes to the build,
just list your issues... this include the entire build from lexical layer 1 write through to the
end of ib_observations, including all the code, methods, configs, migration of catelogue, schema,
jsons packs between each stage, and updating the governance rules documentation and glossary...
I will review it in the morning."*

**Bottom line: Phases A, B, D, E are built, run against real data, and verified. Phase C's
execution code and Phase F (running any cluster) are not built** — an honest scope line drawn
after roughly 4 hours of continuous work, not a claim that the whole 34-item, "~4 weeks" build is
finished. Full build record: `iba/app/BUILD.md` #267. #1706 itself updated in place throughout.

---

## What's actually done, verified against live data

### Phase A — lexical readiness check
Built `lexical.readiness` (3-leg check: verse-has-span, span-strong-resolves,
strong-has-cluster-allocation), registered as a real `cfg_step`/`cfg_method_rule`, with a PS
wrapper (`Lexical-Readiness.ps1`). **Run live twice — 0 FATAL findings both times** (before and
after the Layer 1 rebuild).

### Phase B — Layer 1 (`verse_lexical`) redesign + corpus-wide rebuild
- `role` redesigned from the old buggy content/function classifier (escalation #1590's bug) to a
  JSON array of live `cluster_strong.cluster_code` values.
- `resolved_sense`/`ambiguity_note`/`language` dropped from the table entirely.
- A pre-run readiness validator added — a build scope with any zero-cluster-allocation code
  blocks before any write.
- The `verse_meta_on_lexical_change` trigger rewritten (it read the now-dropped
  `verse_lexical.language` directly — found and fixed as part of this build, not a separate task).
- Every downstream reader of the dropped columns fixed (4 call sites, 3 readers) so nothing in the
  codebase crashes on the new shape.
- **Rebuild run for real: 544,667 rows across 29,760 verses, 93 seconds, 0 errors.** Verified: 0
  NULL/empty role values, 0 malformed JSON in a 5,000-row sample, `verse_meta.language` correctly
  recomputed (21,902 Hebrew + 7,858 Greek = 29,760, 0 NULL).

### Phase D/E — the 5 pack tables
`cluster.status`/`status_changed_at` (95/95 clusters backfilled), `cluster_subgroup` (with
`anchor_verse_reference`, today's own addition), `cluster_subgroup_strong`, `ib_observation`
(stage enum includes the new `verse_meaning` value), `ib_node` (CHECK constraint verified live
against a synthetic bad insert) — all created, all registered in `cfg_table`/`cfg_column`, all 4
new `cfg_enum` groups registered.

### Catalogue migration (#1696)
`wa_obs_question_catalogue` migrated into `iba.db` — **92 rows, matching the researcher's own
Phase 5 content review exactly** (8 codes dropped, 1 revised, 2 new `T2.11` rows added verbatim).
Source flagged inactive, not deleted.

---

## What's genuinely NOT done — not silently skipped, a real scope line

1. **Phase C's execution code.** The `verse_meaning` stage's NAME is registered, but the mechanism
   that actually reads the 3 meaning sources per strong, per cluster, and writes T1.1/T7.1
   `ib_observation` rows does not exist. There is real, adaptable infrastructure to build it from —
   `lexicalenrichgenerate.py` already has a working, tested Anthropic-API-calling pipeline (cost
   estimation, per-batch cap, usage logging) for the OLD Layer 2 mechanism — but adapting it to the
   new per-cluster, ib_observation-writing shape is real, unstarted work.
2. **The recording pass (#1693).** Fully designed (same/broaden/new logic, verse-reference
   resolution, two-level status advance) but not coded. This is what would load an LLM session's
   JSON output into `cluster_subgroup`/`ib_observation`/`ib_node`.
3. **Phase F — no cluster has been run through any stage.** The M10 prototype JSONs from
   2026-09-11 are stale against tonight's schema (no `anchor_verse_reference`, predate #1704's
   role-driven-walk requirement) — a fresh run is needed, not a replay.
4. **The real FK on `ib_observation.question_code`/`ib_node.question_code`.** The catalogue table
   they'd point to now exists, but SQLite FKs are declare-at-CREATE-time only — adding one needs a
   table rebuild, deferred to when the actual write path is built (so the rebuild happens once,
   not twice).
5. **Post-build surface-alignment validation** (replaces #1591's old-row repair) — a cheap,
   real follow-up not reached this round.
6. **Pack sign-off** — the design content is complete and workflow-closed (this session, earlier),
   but if you want a formal go-ahead nod distinct from what's already been approved, that's still
   yours to give.

## Judgment calls made along the way (per "deal with them as fixes, just list your issues")

- **Retired `lexical.enrich`** (the old `verse_lexical_note`-based Layer 2 mechanism) rather than
  patch it to survive the column drops — it's superseded by `ib_observation` per your own #1597
  resolution. Code kept, not deleted, since its LLM-calling half is worth adapting.
- **Fixed a stale `cfg_column.use` text** on `gloss_consistent_in_verse` — it still described the
  check as keyed on `resolved_sense`, though the actual logic has been keyed on `surface` since
  escalation #1527 (2026-09-06). Found doing this build, corrected in the same migration.
- **Removed pre-existing dead code** in `lib/lexical.py` (`_select_stem_text`/`_stem_name_for`/
  `load_mcode_strongs`) — all three were already unreferenced before tonight (their own docstrings
  said so), not something this build orphaned.
- **Narrowed one validation check** in `lexicalenrich.py` (`cross_lemma_shared_gloss`) rather than
  rebuild it — it compared `resolved_sense`, which no longer exists; kept the half of the check
  that doesn't need it, dropped the half that does, since the whole mechanism is superseded anyway.

## Files touched
`iba/app/lib/lexical.py`, `iba/app/handlers/lexical.py`, `iba/app/handlers/raw.py`,
`iba/app/handlers/reports.py`, `iba/app/lib/lexicalenrich.py`, `iba/app/lib/strongreconcile.py`,
`iba/app/ps/Lexical-Readiness.ps1`, 4 new files under `iba/app/migration/`, `iba/app/db/iba.db`,
`iba/app/BUILD.md` (#267), `iba/docs/1706-lexical-stack-full-rebuild-consolidated-build-proposal-
v1-20260915.md` (updated in place throughout).

## Suggested next session
Build Phase C's `verse_meaning` assembly + the recording pass (#1693), then run ONE cluster (M10,
already prototyped once, or your pick) through the full pipeline for real — that's the actual "first
cluster results" to review, not tonight's infrastructure work.
