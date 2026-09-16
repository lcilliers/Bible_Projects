# Catalogue content decisions — researcher review of Phase 5, 2026-09-16

Researcher decisions against each of Phase 5's 8 items, verbatim references throughout. These are
**content changes to the live catalogue** — like `T2.11` (#1701), none written to `bible_research.db`
directly; all fold into **#1696's migration script** as drops/edits/additions to the insert set,
per the standing "don't touch research_db further" instruction this session.

## 1. Purpose-clause-detection (T0.2.1) — **APPROVED, option B**

New Layer 2 `note_type` (e.g. `purpose_clause`), LLM-judged at reading time — same shape as
`chain`/`connective`. Build item: register in `cfg_enum`/`cfg_method_rule` once the reading-stage
process design reaches this (not urgent, no live consumer blocked on it).

## 2. Post-occurrence/characteristic-level sequence (T1.5, T1.6, T5.2, T5.5) — **APPROVED, option C**

Extend `chain`'s existing detection across a family's occurrences (a reading-stage observation),
not new infrastructure. Same status as item 1 — designed, not yet built, no urgency.

## 3. Future-orientation marker (T5.6, T0.4) — **APPROVED, option B — CONFLICT, unresolved**

Lexical-marker list + `morph_code` tense as secondary confirmation. **Its only two consumers
(T5.6, T0.4) are dropped by items 5/6 below** — flagged back to the researcher, not resolved here:
build anyway (anticipating T5.6's replacement questions, "next round," will need the same signal),
or hold until that replacement content exists.

## 4. Genre/contextual-setting (T7.2.2a, T7.2.2b, T7.2.4) — **RETIRE, option C**

Researcher, verbatim: *"genre cannot be determined from a verse reading. Not sure if genre add any
real difference for inner being interpretation."* All three question codes **dropped from the live
catalogue** — not migrated by #1696 (excluded from its insert set, not carried into `iba.db` at
all). Consistent with the existing #1608 ruling (genre already excluded from lexical reading).

## 5. Typological-link (T0.4) — **DROP**

Researcher, verbatim: *"drop T0.4.1, T0.4.2, T0.4.3. Not adding value to characteristic debate."*
**Checked live: only `T0.4.1` exists** (4.2/4.3 were never live rows). `T0.4.1` dropped — not
migrated by #1696.

## 6. T3-operation-surfacing (T5.1, T5.3) — **APPROVED, option C, with scope**

Researcher, verbatim: *"select option C, with questions T5.4, T5.5, T5.6, T5.7 dropped. the[y] will
be replaced with other questions (will provide these in next round)."* **Checked live: T5.4/T5.5/
T5.6 carry 4 questions total** (`T5.4.1`, `T5.4.2`, `T5.5.1`, `T5.6.1`) — **`T5.7` doesn't exist in
the live catalogue**, nothing to drop there. All 4 existing questions **dropped from #1696's
migration**, pending the researcher's replacement content next round. `T5.6`'s drop is the source
of item 3's conflict above.

**Not yet designed here** — option C itself (a structural T5 reframe, subject-as-process not
subject-as-characteristic) is the researcher's own upcoming work ("next round"), not designed in
this document.

## 7. Constitutional-level vocabulary (T2.1) — **CORRECTED, real mechanism identified**

Researcher, verbatim: *"spirit soul body is not an T code, it is M47 and therefore should be
evident from the verse if it a word in the verse. the T2.1 questions are very relevant and there
should be an event around multi M-code where one of the codes are M47."* **Verified live: `M47`
("Inner Seat") exists** — heart/soul/spirit/inward-parts, 38 strongs (`lev`/`kardia`/`nephesh`/
`ruach`/etc.). This is **not** the T-code gap Phase 5 (and Phase 2's event 13) assumed — it's an
existing M-code, already classifiable by the standard `cluster_strong` mechanism, no new referent
code needed.

**Corrected mechanism:** T2.1 is answered by **the same cross-characteristic co-occurrence event as
T5.4/T6.1/T6.2/T6.3** (Phase 2 event 4 — `_assess_cross_cluster_cooccurrence.py`, #729, built once,
inactive since 2026-08-18) — reactivated, with a specific filter/highlight for verses where **M47
co-occurs with the verse's other M-code(s)**. `T2.1` is **kept live**, its own genuine gap resolved
without inventing new infrastructure. Phase 2 event 13 ("constitutional-level vocabulary
detection") and Phase 5 item 7's own framework are both superseded by this — see corrections below.

## 8. `idiom` (feeds T7.1.3) — **APPROVED, option B, plus a question-text expansion**

Researcher, verbatim: *"option B and the question must be expanded to prompt for idiom, analogy and
other implied meaning."* `idiom` matched to T7.1.3, **and T7.1.3's own text is revised**:

- **Current (live, `bible_research.db`):** *"What is the semantic range of the primary term —
  across what breadth of meaning does it operate?"*
- **Revised, for #1696's migration insert:** *"What is the semantic range of the primary term —
  across what breadth of meaning does it operate, including any idiomatic, analogical, or otherwise
  implied meaning carried by its use in combination with other terms?"*

Not written to `bible_research.db` — the revised text supersedes the old for #1696's insert, same
pattern as every other content change here. **General wording-quality pass explicitly parked** —
researcher, verbatim: *"there is room for improvement of the questions wording. not for this
chat."*

---

## Net effect on #1696's migration scope

- **Drop from the insert (7 question codes):** `T0.4.1`, `T5.4.1`, `T5.4.2`, `T5.5.1`, `T5.6.1`,
  `T7.2.2a`, `T7.2.2b`, `T7.2.4` — 8 codes total (corrected count).
- **Add (already tracked, #1701):** `T2.11.1`, `T2.11.2`.
- **Text revision (1 code):** `T7.1.3`.
- **Net row count:** 98 (original) − 8 (dropped) + 2 (`T2.11`) = **92 rows**, not 100 — corrects the
  running total from the last session update (#1696 v11 said 100, now 92).
