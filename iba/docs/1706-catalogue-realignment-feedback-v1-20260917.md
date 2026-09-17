# What the catalogue realignment changes about the #1706 build

**Feeds back from #1712 into #1706**, per researcher instruction, 2026-09-17: *"It looks like this
is now a firm foundation and that you can now go through the detail gap planning to see what need
to be fed back to 1706 to revisit the build."*

## 1. The most consequential change: `#1711`'s own catalogue linkage is stale

`#1711` decided `verse_meaning` answers **T1.1** and **T7.1**. Those codes no longer exist —
renumbered to **`M0.1.1`–`M0.1.3`** (Name and Naming) and **`M0.5.1`–`M0.5.10`** (Lexical and
Semantic Analysis), and reclassified as `M0` (lexical/textual evidence that *feeds* the 12
dimensions) rather than a dimension in its own right. This doesn't overturn `#1711`'s substance —
if anything it confirms the instinct (these are lexical-profile facts, not "understanding"
questions) — but the Phase C build plan's own catalogue-linkage section needs its codes corrected:
`verse_meaning` answers `M0.1`/`M0.5`, not `T1.1`/`T7.1`.

## 2. A real candidate addition to `verse_meaning`'s scope: `D7.7`

`D7.7.1` (the new operation-anchored/role-`T3` permeability question, authored this session) sits
naturally at the same per-cluster, pre-subgroup grain `verse_meaning` already operates at — role-`T3`
co-occurrence is verse-local, doesn't need subgroup formation to answer. Worth deciding whether
`verse_meaning` answers this too, alongside `M0.1`/`M0.5`, rather than leaving it to `char-reading`.
Not decided here — a real scope question for you.

## 3. A genuinely new build requirement: wiring the science-extract file

`D9.1.1`/`D9.2.1`/`D11.2.1`/`D12.1.1` (4 of the 9 new questions) all name the same real mechanism:
the per-cluster science-extract file at `Workflow/Sciences/science_files/`. This wasn't in `#1706`'s
original Phase A–G list at all — it's a new, concrete build item: whichever stage answers these
(most likely `char-answers`, matching the science-extract files' own stated purpose — *"the standing
reference for T7.3 prompt responses during Phase 8"*, i.e. the old characteristic-level answer
stage) needs to load that cluster's file as a data input. Separately, per your first question this
turn: the remaining ~40 of 85 clusters still need their own science-extract file produced before
this can run corpus-wide — see the chat reply for that.

## 4. The role-driven walk and the new `D7` structure line up well — worth noting, not just a gap

`D7` (permeability) now has 7 clean sub-components: `D7.1` Divine Extension, `D7.2`/`D7.3`
Interpersonal Extension/Uptake, `D7.4` Adversarial/Angelic, `D7.5` Origin and Source, `D7.6`
God-Relation Directionality, `D7.7` Operation-Anchored. This maps cleanly onto the role-driven
walk's own steps (`#1704` §2): `(b)(ii)` other-M-code relational+pointer ≈ `D7.5`; `(b)(iii)`
party-kind sweep ≈ `D7.1`–`D7.4`; `(b)(iv)` T3/action-word reading ≈ `D7.7` directly. The walk and
the catalogue were never actually in tension on substance — the catalogue just didn't have the
structure to receive the walk's output until now.

## 5. `F0`/`X0` confirm scope boundaries already decided, don't reopen them

`F0` (Faculty Engagement) is subgroup-level, per `#1701`/`#1704`'s own decision — not `verse_meaning`'s
or `char-reading`'s job. `X0` (cross-characteristic synthesis, the old `T6` tier) is synergy-stage —
not any single-characteristic stage's job. Neither changes anything already decided; this just
confirms the new structure doesn't quietly pull either back into scope somewhere it doesn't belong.

## 6. Still open, unrelated to this feedback

The `ib_observation.stage` rename (`verse-reading`/`char-reading`/`char-answers`/`char-synergy`) and
the `answer`-stage baseline tag from earlier this session remain open — this feedback doesn't touch
either, but §3's "which stage answers the science questions" would benefit from that naming being
settled first.
