# Full pipeline build checklist — verse-reading through char-synergy

**No, not an accurate one existed** — the original `#1706` proposal's build-action-list (§6) is
from 2026-09-15, before today's dimension realignment, catalogue restructuring, science extracts,
cluster fixes, and the actual `verse-reading` execution build; my own readiness doc from earlier
today is stale too (written before `lexical.meaning` existed). This is the real one, checked
against live `cfg_step`/table state just now, not assumed. **Keep this updated as work lands** —
it goes stale the same way the others did if it isn't.

Legend: ✅ done and verified live · 🔶 partial / pending a specific named thing · ❌ not started.

---

## Stage 0 — base data (prerequisite to everything below)

- ✅ Verse/span/strong spine clean (`spine.check`, 0 FATAL).
- ✅ Layer 1 (`verse_lexical`) rebuilt corpus-wide, `role` JSON array live.
- ✅ `cluster`/`cluster_strong` (M-codes + role-`T`-codes) populated; anomaly sweep run and fixed
  (`#1714`).

## Stage 1 — `verse-reading` (`lexical.meaning`)

- ✅ Design closed (`#1711`).
- ✅ `cfg_step`/`cfg_method_rule`/`cfg_write_grant` registered.
- ✅ Execution code built (`versereadinggenerate.py`, `handlers/lexical.py:meaning`).
- ✅ **PS entry point built** (`VerseReading.ps1`) — this step had none until now (`cfg_behaviour_rule`
  `every-interactive-module-needs-ps-script`).
- ✅ **`M67` — first full cluster run, complete, 2026-09-17.** 35/35 verses, all 9 member strongs
  covered, 140 observations, `cluster.status` advanced to `ready_for_subgroup_allocation`.
  Real, found-live infra bug fixed on the way: 7 of `M67`'s 9 member strongs (+2 in `M60`) had
  **stale Layer 1 `role`** — `cluster_strong` rows added by `#1714`'s anomaly fix landed *after*
  the corpus-wide Layer 1 rebuild, and nothing re-syncs `role` when that happens for a cluster
  still at ordinal 2. Fixed by re-running `lexical.build` for the 37 affected book/chapter pairs;
  verified live. Escalation `#1719` (open — asks whether a structural resync hook is needed, or
  the window was narrow enough not to bother; not decided unilaterally).
- 🔶 Minor quality finding, same run (folded into `#1719`): ~3% of observations (4/140) show
  `question_code` format drift (`D7.7` instead of `D7.7.1`; literal string `"none"` instead of
  JSON `null`) — no live FK yet to catch it (deferred by design), now evidenced in real data.
  Everything else sampled reads as coherent, specific, correctly-scoped content.
- ❌ **79 of 80 clusters still have no `verse-reading` pass.** 1 of 80 now complete.
- ❌ Science-extract file wiring for `D9`/`D11`/`D12` — those questions aren't in this stage's
  scope (it answers `M0.1`/`M0.5`/`D7.7` only) — **open: which stage answers them is not yet
  decided**, see Stage 4.

## Stage 2 — `char-subgroup` (process b, subgroup formation)

- ✅ Design closed (`#1690`, `#1691` §9 item 8 — the `stage='subgroup'` promotion decision).
- ✅ Tables exist (`cluster_subgroup`, `cluster_subgroup_strong`) — live schema checked, matches
  `#1690`'s DDL exactly.
- ✅ **`cfg_step`/`cfg_write_grant`/`cfg_method_rule` registered** (new work package
  `cluster-reading`; `register_cluster_subgroup_step_v1_20260917.py`).
- ✅ **Execution code built** (`lib/subgroupgenerate.py`, `lib/recordingpass.py:record_subgroups`,
  `handlers/cluster.py:subgroup`) — whole-cluster, one LLM call (never batched, rule (a) requires
  the full member-strong set read before any assignment).
- ✅ **PS entry point built** (`ClusterSubgroup.ps1`).
- ✅ **`M67` — first real run, complete, 2026-09-17.** 6 subgroups, 9/9 strongs placed (0 FLAG),
  0 unresolved anchor verses, `cluster.status` → `ready_for_reading`. Quality-checked, not just
  run: groupings are genuinely meaning-based (correctly separated 3 distinct "negative pole"
  flavors — general idleness/G0692, disorderly-conduct/G0812, timid-reluctance/G3636 — rather than
  lumping all idle-adjacent words together); anchor verses are well-chosen (e.g. `Eccl.10.18`
  picked for the "slack hands causing decay" subgroup — a precise match to its own label, not a
  generic pick); labels are genuine descriptive phrases, not word lists; 3 of 6 subgroups are
  correctly-accepted singletons (rule (e)).
- ✅ **Precondition + re-run guards verified live**: refuses to run against a cluster not at
  `ready_for_subgroup_allocation` (tested: M67 correctly refused post-allocation); refuses to
  duplicate an already-allocated cluster (`recordingpass.SubgroupWriteError`, untested against a
  second real cluster yet but the same code path the precondition-refusal test exercised).
- ✅ **`placement_note` vs `observations` — corrected, researcher caught the real issue live**:
  the "undesigned mechanism" framing was wrong; the LLM simply wasn't asked for `observations`
  directly (no `tag` vocabulary given), so it had nowhere to put substantive claims except
  `placement_note`. Fixed: LLM now outputs a real `observations` array (same shape/tags as Stage
  1), captured via the same `recordingpass.record_batch`, `stage='char-subgroup'`. `placement_note`
  is now strictly placement rationale only.
- ✅ **Two more real defects found and root-fixed redoing `M67`**: `cluster_subgroup`/
  `cluster_subgroup_strong`'s `UNIQUE` constraints didn't exclude soft-deleted rows (now partial
  indexes, matching `verse_lexical`'s own established convention); `record_batch` discarded the
  actual unresolved-occurrence reasons, keeping only a count (now surfaced in the run's own
  message, not just a number).
- **1 of 80 clusters allocated** (`M67`, redone clean with the corrected mechanism: 4 subgroups,
  9/9 strongs, 0 FLAG); 79 still at `ready_for_subgroup_allocation` or earlier.

## Stage 3 — `char-reading` (process c, per-subgroup reading)

- ✅ Design substantially closed (`#1682`'s process spec; checklist rules 1–14).
- 🔶 **Role-driven-walk enforcement rigidity — genuinely pending your own reserved judgement**
  (`#1704`/`#1705` tension, explicitly deferred by you until real pipeline results exist).
- ❌ `cfg_step` — not registered.
- ❌ Execution code — does not exist.
- ❌ Writing the forced-walk requirement into `#1682`'s own spec as a structural requirement
  (checklist rule 14's own outstanding item) — not done, blocked on the item above.

## Stage 4 — `char-answers` (process d, per-subgroup catalogue Q&A)

- ✅ Design substantially closed (`#1682` §4A; checklist §3).
- 🔶 `char-answers` baseline tag (`answered-no-flag`) drafted, never exercised against real data.
- ❌ `cfg_step` — not registered.
- ❌ Execution code — does not exist.
- ❌ **Science-extract file wiring for `D9`/`D11`/`D12` — the most likely home** (the files'
  own purpose statement: *"the standing reference for T7.3 prompt responses during Phase 8"*, the
  old name for this same grain) — not decided or built.

## Stage 5 — `char-synergy` (process e, cross-cluster synthesis)

- ❌ **Design itself is not closed** — `#1695` (`Design: cluster-reading synergy stage`) is still
  `in-progress`/`review`; `#1698` (cross-cluster `cluster_code` gap) is `in-progress`/`revise` —
  checked live, neither is `completed`.
- ❌ `cfg_step` — not registered.
- ❌ Execution code — does not exist.
- This stage is furthest behind of all five — not just unbuilt, not yet fully *designed*.

## Shared / cross-cutting infrastructure

- ✅ **Recording pass (`recordingpass.py`) — built, stage-agnostic, validated.** Takes `stage` as
  a parameter; already works for any of the 5 stages above, not `verse-reading`-specific. This is
  real, reusable progress toward Stages 2–5, not just Stage 1.
- ✅ Tag taxonomy (`D1`–`D12`/`M0`/`X0`/`F0`) registered, catalogue fully realigned (97 live
  questions).
- ✅ All 80 clusters have a science-extract file (content exists; wiring into a stage does not).
- 🔶 `#729` (cross-cluster co-occurrence mechanism, needed for `M47`/some `D7` sub-questions) —
  needs fresh scoping against the live `iba.db` schema, unowned.
- 🔶 `narrativegenerate.py`'s likely-shared extended-thinking bug — flagged (`#1717`), not fixed.
- ✅ **Old Layer 2 (`verse_lexical_note`/`lexical.enrich`/`lexical.run`) fully retired**, confirmed
  live — a prior session's retirement was incomplete (`lexical.run`, a second live entry point
  onto the same old mechanism, was untouched); fixed and verified `lexical.run` now refuses to
  dispatch. See `#1719`, BUILD.md #275.
- ✅ **Pre-`verse-reading` Layer 1 freshness gate built** (`lib/lexical.py:
  stale_role_strongs_for_cluster`, wired into `handlers/lexical.py:meaning`) — hard-stops a
  cluster's verse-reading run if any member strong's `role` doesn't reflect current
  `cluster_strong` membership, the exact `M67`/`M60` failure mode, now structurally prevented
  rather than relying on manual checking. `#1719`, BUILD.md #275.

---

## The honest one-line summary

**2 of 5 pipeline stages now have execution code and a PS entry point, both proven end-to-end on
`M67`** (verse-reading: 35/35 verses; char-subgroup: 6 subgroups, 9/9 strongs, cluster.status now
`ready_for_reading`). Stages 3–4 are designed but have zero execution code and zero `cfg_step`
registration. Stage 5 isn't even fully designed yet. The recording pass and the base
data/catalogue layer underneath all five stages are genuinely solid and reusable — that part of
today's work carries forward to every stage, not just the ones built. One real infra bug
(Layer 1/`cluster_strong` staleness) was found and fixed running `M67` for real — see `#1719`. A
second real gap (`cluster.gloss`, wrong grain entirely) was found doing unrelated validation and
removed — see `#1720`.
