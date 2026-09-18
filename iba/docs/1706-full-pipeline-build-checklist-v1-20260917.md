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

> **Correction, 2026-09-18:** this section as originally written (below, kept for the historical
> detail on the mechanism/defects found) described a run that was subsequently **wiped** the same
> day by `#1723`'s progressive-relational reset of `M67` (which reset Stage 1 *and* Stage 2 data
> together) — the session log itself (`SESSION-LOG-20260917-v2.md`) correctly recorded this as "not
> yet run" at close. Confirmed live before writing this correction: `M67` was at
> `ready_for_subgroup_allocation` with 0 live `cluster_subgroup` rows. **Re-run 2026-09-18, fresh
> Developer Mode session, escalation #1706 / BUILD.md #285**: 4 subgroups, 9/9 strongs placed, 0
> FLAG, `cluster.status` → `ready_for_reading`, $0.2183. The mechanism, defect-fixes, and design
> notes below are still accurate — only the specific "6 subgroups" run result was stale.

- ✅ Design closed (`#1690`, `#1691` §9 item 8 — the `stage='subgroup'` promotion decision).
- ✅ Tables exist (`cluster_subgroup`, `cluster_subgroup_strong`) — live schema checked, matches
  `#1690`'s DDL exactly.
- ✅ **`cfg_step`/`cfg_write_grant`/`cfg_method_rule` registered** (new work package
  `cluster-reading`; `register_cluster_subgroup_step_v1_20260917.py`).
- ✅ **Execution code built** (`lib/subgroupgenerate.py`, `lib/recordingpass.py:record_subgroups`,
  `handlers/cluster.py:subgroup`) — whole-cluster, one LLM call (never batched, rule (a) requires
  the full member-strong set read before any assignment).
- ✅ **PS entry point built** (`ClusterSubgroup.ps1`).
- ✅ **`M67` — first real run, 2026-09-17** (superseded by the `#1723` reset, then **re-run clean
  2026-09-18** — see correction note above): 4 subgroups, 9/9 strongs placed (0 FLAG),
  `cluster.status` → `ready_for_reading`. Quality-checked, not just run: groupings are genuinely
  meaning-based (idleness-as-state vs. duty-based dereliction vs. earnest diligence vs. the lone
  Aramaic administrative-thoroughness term kept correctly separate); labels are genuine descriptive
  phrases, not word lists.
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
- ✅ **Role-driven-walk enforcement rigidity — RESOLVED, not a gate.** Corrected 2026-09-18: this
  line previously cited `#1704`/`#1705` as still pending (stale — both were `completed`/`closed`
  2026-09-15/16, and the enforcement question itself was separately resolved 2026-09-17, recorded
  at `#1706` v32, not either of those two). Resolution: no structural/mechanical role-walk
  enforcement; direction is question-driven catalogue expansion instead — confirmed live, already
  built (`#1723`'s `M0.6.5`) and already exercised in `verse-reading`'s and `char-subgroup`'s own
  live `M67` runs. Full record: `1706-role-driven-walk-consolidated-status-v1-20260917.md` §5
  header note.
- ✅ **`cfg_step`/`cfg_write_grant`/`cfg_method_rule` registered** (`cluster-reading` work package,
  same as Stage 2; `register_cluster_reading_step_v1_20260918.py`, 12 rules — checklist rule 14's
  forced-walk explicitly NOT encoded, recorded as retired).
- ✅ **Real, previously-missing gap fixed on the way**: `#1690` §3a's own `allocated`→
  `ready_for_reading` subgroup-status transition was designed but never built (all 4 of `M67`'s
  Stage-2 subgroups sat at `allocated` since 2026-09-17). Root-fixed in Stage 2's own handler
  (`clusterstatus.advance_subgroups_after_allocation`), not patched as a one-off on `M67` alone.
- ✅ **Execution code built** (`lib/charreadinggenerate.py`, `handlers/cluster.py:reading`) — one
  LLM call per subgroup (never batched, checklist rule 1), given the subgroup's full corpus-wide
  occurrence lists (no sampling) plus Stage 1/2's own observations as grounding. Per-strong
  completeness (checklist rule 10) is code-computed after the write, not LLM-self-reported — an
  improvement on the original 2026-09-11 spec, consistent with the established never-trust-the-
  model discipline.
- ✅ **PS entry point built** (`ClusterSubgroup.ps1`'s sibling, `CharReading.ps1`).
- ✅ **`M67` — all 4 subgroups run live, complete, 2026-09-18.** 26 observations
  (`difference-inference` 12, `tightly-related` 9, `no-direct-connection` 5), full per-strong
  traceability confirmed on every subgroup, $0.3518 total spend, all 4 → `ready_for_answer`.
  Quality-checked: `G0691`/`G0692` correctly identified as cognates (`tightly-related`) while
  `H8220` (different language family) correctly kept `no-direct-connection`; a genuine
  "morph-reviewed, no distinction found" negative result was recorded, not silence. One transient
  first-call JSON-formatting failure (escalation #1726, self-correctable) — confirmed not
  truncation (2,478 of 40,000 output tokens used), an identical retry succeeded clean, no code
  change needed.
- **1 of 80 clusters' subgroups read** (`M67`, all 4); every other cluster's subgroups still at
  `allocated` (Stage 2 not yet run) or earlier.

## Stage 4 — `char-answers` (process d, per-subgroup catalogue Q&A)

- ✅ Design substantially closed (`#1682` §4A; checklist §3).
- ✅ `char-answers` baseline tag (`answered-no-flag`) now exercised against real data (259
  observations, all 4 of `M67`'s subgroups).
- ✅ **`cfg_step`/`cfg_write_grant`/`cfg_method_rule` registered**
  (`register_cluster_answer_step_v1_20260918.py`, 7 rules).
- ✅ **Execution code built** (`lib/charanswergenerate.py`, `handlers/cluster.py:answer`) — one
  LLM call per subgroup, answering the catalogue's characteristic-grain battery (52 live
  questions — see exclusions below) against Stage 1/2/3's own accumulated evidence. Multiple
  distinct slants under the same `question_code`, using the EXISTING recording-pass same/broaden/
  new mechanism, no bespoke "slants" structure needed.
- ✅ **Battery scope deliberately narrowed, both exclusions already-documented gaps**: `D7.7.1`
  excluded (already Stage 1's own territory despite carrying the same scope label — a noted
  discrepancy, not silently resolved). Science-extract-dependent questions (`D9.1.1`/`D9.2.1`/
  `D11.2.1`/`D12.1.1`) excluded — wiring genuinely not decided/built, per this same doc's prior
  note (kept below for provenance). `cross_family_or_cluster_flags` (checklist §3 rule 5)
  deliberately not built — its own tag value still unchosen, not this build's call to invent.
- ✅ **Two real gaps found and root-fixed in `recordingpass.py` itself** (shared by all 4 live
  stages): (1) a genuine whole-subgroup NEGATIVE finding with no verse citation was being silently
  discarded, identically to a real bad-citation failure — confirmed live, first run lost 10 of 52
  answers this way; fixed, `M67_A` re-run clean, all 52/52 landed. (2) `ib_node.strong` was always
  written from the observation's own outer `strong`, never the per-occurrence one — invisible for
  Stages 1–3, load-bearing for this stage's new `strong: null`-with-per-occurrence-strong shape;
  fixed before the first live call. See `BUILD.md` #288 for full detail.
- ✅ **A third real gap found before this stage's build even started**:
  `needs_adjacent_verse_context` (named by every stage's own prompt/rules since Stage 1) was never
  actually registered in `cfg_enum` — 0 live rows, would have been silently rejected the first time
  any stage's LLM genuinely tried to raise it. Fixed standalone
  (`register_needs_adjacent_verse_context_tag_v1_20260918.py`) before Stage 4 needed it for real.
- ✅ **PS entry point built** (`CharAnswer.ps1`).
- ✅ **`M67` — all 4 subgroups run live, complete, 2026-09-18.** 259 observations, all 52/52
  battery questions answered on every subgroup (completeness computed by code via `ib_node`
  strong-citation, not LLM-self-reported), $1.48 total spend (including the pre-fix partial
  `M67_A` run, superseded by a clean re-run). Multiple-slants confirmed working: `D2.1.1` (M67_A)
  produced 4 distinct per-strong slants under one question_code.
- ❌ Science-extract file wiring for `D9`/`D11`/`D12` — the most likely home (the files'
  own purpose statement: *"the standing reference for T7.3 prompt responses during Phase 8"*, the
  old name for this same grain) — not decided or built; a real, still-open follow-on increment,
  not part of this build's scope.

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

**4 of 5 pipeline stages now have execution code and a PS entry point, all proven end-to-end on
`M67`** (verse-reading: rebuilt under the `#1723` progressive-relational redesign, 304 valid
observations; char-subgroup: re-run 2026-09-18 after the reset wiped the 2026-09-17 run, 4
subgroups, 9/9 strongs; char-reading: built and run 2026-09-18, all 4 subgroups, 26 observations,
$0.3518 total; char-answers: built and run 2026-09-18, all 4 subgroups, 259 observations, all 52/52
battery questions answered, $1.48 total, all → `answer_complete`). Stage 5 is the only one left —
zero execution code and not even fully designed yet (`#1695`/`#1698` still open). The recording
pass and the base data/catalogue layer underneath all five stages are genuinely solid and
reusable — that part of today's work carries forward to every stage, not just the ones built. One
real infra bug (Layer 1/`cluster_strong` staleness) was found and fixed running `M67` for real —
see `#1719`. A second real gap (`cluster.gloss`, wrong grain entirely) was found doing unrelated
validation and removed — see `#1720`. A third (`cluster_subgroup.status` never advancing past
`allocated`) was found and fixed building Stage 3 — see `BUILD.md` #287. A fourth and fifth
(occurrence-less negative findings silently discarded; `ib_node.strong` never carrying the
per-occurrence value) plus a sixth cross-cutting gap (`needs_adjacent_verse_context` never
registered) were found and fixed building Stage 4 — see `BUILD.md` #288.
