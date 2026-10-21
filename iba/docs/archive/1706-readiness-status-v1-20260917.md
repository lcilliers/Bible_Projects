# Is #1706 ready to move to the final build — honest status, checked not assumed

**Continues #1706.** Per researcher question, 2026-09-17: *"Is 1711 now clean and can we move over
to 1706 for the final build. is all the preparatory work done."*

## `#1711` — confirmed clean, checked live

`state='completed'`, `next_action='approved'`. `#1693` (the recording pass design) is also
`completed`/`approved`. Both design-closed. **Design closed is not the same as built** — see §3.

## 1. Closed, confirmed, nothing further needed

- The 12 goal-derived dimensions (two independent derivations, converged) — `#1712`.
- The full catalogue realignment (`D1`–`D12`/`M0`/`X0`/`F0`, 97 live questions, all dimensioned and
  mechanism-tagged) — `#1712`.
- `T3`'s catalogue gap — closed via `D7.7`.
- The `T`-code numbering collision (catalogue tiers vs. role-classification clusters) — identified
  and eliminated by the renumbering.
- The tag taxonomy's own consolidation (`cross-cluster-significance`, `could-not-resolve`,
  hyphen-case standard) — registered live in `cfg_enum`.
- All 80 live clusters now have a science-extract file, reconciled against the current cluster
  scheme, not the stale May files — `#1706` (this thread).

## 2. Genuinely still open — narrowed, on challenge

Researcher, verbatim: *"what prevents you from completing all the preparatory work?"* Fair —
re-checked each of the original 6 against what was actually already on record. **3 of the 6 had
enough grounding to just resolve**, not real blockers I was waiting on:

- **Stage renaming, including `subgroup`** — RESOLVED. `subgroup` → `char-subgroup`, completing
  the scheme (`verse-reading`/`char-subgroup`/`char-reading`/`char-answers`/`char-synergy`).
  Applied live (`ib_observation` still 0 rows, safe). The `char-answers` baseline tag
  (`answered-no-flag`) drafted and registered in the same pass.
- **`needs_adjacent_verse_context` at `verse_meaning`** — RESOLVED. The checklist's own cross-cutting
  rule 5a already said this governs *every* flag-shaped observation "this pipeline" raises, not a
  `char-reading`-only rule. I'd left it listed as open despite the rule already answering it.
- **Including the unwired role-tags (`T2`/`T6`/`T10`–`T15`) from the first run** — RESOLVED,
  include them. The prose's own registry-construction principle: *"the cost of over-inclusion is
  visible and recoverable; the cost of silent omission is invisible and not recoverable."* `#1704`'s
  whole mission was uncovering exactly this kind of silent gap — starting narrower would risk
  repeating it. This is the programme's own stated bias, not a judgement call needing your voice.

**3 of the 6 are genuine** — checked, not just re-asserted:

1. **How rigidly the role-driven walk should be enforced at `verse_meaning`.** Not mine to resolve —
   `#1705`'s own closing words explicitly reserve it: *"I may revisit this judgement... will hold my
   judgement until we had some results out of the new pipeline."* That's a deliberate, stated
   deferral by you, not an oversight.
2. **`#729`** (cross-cluster co-occurrence script) reactivation — a resourcing/ownership call, not a
   content decision I have standing to make.
3. **`#1714`**'s sequencing relative to this build — a risk-tolerance call (build against known
   cluster anomalies vs. fix first) that's genuinely yours.

## 3. Not started at all — the actual build, regardless of §2

Design and data-grounding work is what today produced. **Zero of Phase C's execution code exists
yet:**
- The `verse_meaning` LLM-calling mechanism itself (adapting `lexicalenrichgenerate.py` to the new
  per-cluster, multi-question-answering shape).
- The recording pass (`#1693`'s own write logic) — designed, not coded.
- The new `cfg_step` registration `verse_meaning` (and the rest of the cluster-reading pipeline)
  needs — checked live earlier this session: nothing registered for any of process (b)/(c)/(d)/(e)
  either.
- Wiring a cluster's science-extract file into whichever stage actually answers `D9`/`D11`/`D12` as
  a live data input.
- The real FK on `ib_observation.question_code`/`ib_node.question_code` (deferred until the write
  path exists — it does now, in design; not yet built).
- Phase F — no cluster has been run through any stage, ever, under the current schema.

## Straight answer

`#1711` — clean. The catalogue/dimension/science-data grounding is done. Of the 6 items §2
originally listed, 3 were resolved on re-examination — I'd stopped short of deciding them out of
over-applied escalation caution, not genuine necessity. The remaining 3 are real: one you've
explicitly reserved for yourself, two are resourcing/sequencing calls that are legitimately yours.
§3 — the entire actual build — is still fully ahead regardless. Ready to move to writing code once
those 3 are settled.
