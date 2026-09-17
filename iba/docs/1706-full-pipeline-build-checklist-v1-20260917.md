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
- ✅ Validated live — 14 real observations, `M67`, 0 unresolved occurrences.
- 🔶 **`M67` itself is 4 of 35 verses** — not a full cluster run yet, your open question from
  earlier.
- ❌ **No cluster has a complete `verse-reading` pass.** Zero clusters done, 1 of 80 started.
- ❌ Science-extract file wiring for `D9`/`D11`/`D12` — those questions aren't in this stage's
  scope (it answers `M0.1`/`M0.5`/`D7.7` only) — **open: which stage answers them is not yet
  decided**, see Stage 4.

## Stage 2 — `char-subgroup` (process b, subgroup formation)

- ✅ Design closed (`#1690`, `#1691` §9 item 8 — the `stage='subgroup'` promotion decision).
- ✅ Tables exist (`cluster_subgroup`, `cluster_subgroup_strong`).
- ❌ **`cfg_step` — not registered.** Checked live, confirmed.
- ❌ **Execution code — does not exist.**
- ❌ The `placement_note`-promotion mechanism (telling "just a bookkeeping reason" from "also a
  genuine observation" apart) — still undesigned (`#1693` §2's own open item, never closed).
- **0 live rows in either table.**

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

---

## The honest one-line summary

**1 of 5 pipeline stages has execution code, tested against 1 of 80 clusters, 11% of that one
cluster's verses.** Stages 2–4 are designed but have zero execution code and zero `cfg_step`
registration. Stage 5 isn't even fully designed yet. The recording pass and the base data/catalogue
layer underneath all five stages are genuinely solid and reusable — that part of today's work
carries forward to every stage, not just the one that's built.
