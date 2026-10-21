# Cluster T-codes — which drive existing catalogue questions, which need new ones

**Origin:** researcher instruction, this chat turn: evaluate each cluster T-code, determine which
need exploratory questions, note which already support existing questions, and record the impact
on answer-stage LLM instructions. Builds directly on #1700's T0–T7 catalogue-quality review and
the T-code design work already live in #1605/#1606/#1607 — this document synthesizes, it does not
re-derive from scratch.

**Scope note, resolved before starting:** "T-code" is ambiguous across three unrelated live
schemes in this project — Verse Reading Technique (T1–T9), the observation-catalogue Tier
Catalogue (T0–T7, what #1700 has been reviewing), and the **cluster T-codes** (T2–T15, the
`cluster` table). Researcher confirmed this turn: **cluster T-codes** is what's meant here.

## 1. The 14 live cluster T-codes

| Code | Name | What it marks |
|---|---|---|
| T2 | Supplementary | Catch-all for codes not fitting elsewhere — NOT blanket-irrelevant (live rule `t2-supplementary-not-blanket-irrelevant`, #1598) |
| T3 | Operations | A strong considered a human operation/movement, not tied to one characteristic |
| T4 | Adversarial | Strong refers to Satan/the Devil |
| T5 | Negator | Grammatical negation (not/no) |
| T6 | Connective | Clause-linking word (causal/coordinating/purpose, kept as one bucket) |
| T7 | Party-Divine | Strong refers to God/the LORD/Christ |
| T8 | Party-Human | Strong refers to a human party |
| T9 | Party-Angelic | Strong refers to an angel/messenger |
| T10 | Places | Location/realm (heaven, Sheol, wilderness, etc.) |
| T11 | Corporate-Collective | Nation/people/tribe/city as an acting unit |
| T12 | Objects-Artifacts | Man-made object (idol, sword, altar) |
| T13 | Natural-World | Natural phenomenon/element/creature |
| T14 | Body-Parts | Body part with recognized figurative/theological weight |
| T15 | Calendar | Hebrew calendar month names |

## 2. Already mechanically wired to a catalogue question — confirmed, not inferred

**T7/T8/T4/T9 → `verse_lexical.party_kind`, live, populated (12,075 divine / 5,311 human / 496
non_human rows).** This is not a guess at intent — the researcher's own words, closing escalation
#1605 §5.2: *"there are a number of questions in the catalogue that is specifically around divine
impact on the char. by retaining party_kind as an additional focussed signal, it will immediately
escalate the divine questions into focus."* **T7 (`party_kind='divine'`) is explicitly designed to
drive T0.1/T4.1/T4.2** (God-relation, Divine Interface both directions). **T8
(`party_kind='human'`) drives T4.3/T4.4** (Human Interface Giving/Receiving) the same way.

**T4/T9 → `T4.6.2a`/`T4.6.3a`, designed but never actually run.** These two catalogue questions
(*"Does an adversarial-being code ever appear as an acting party..."* / *"...an angelic-being
code..."*) are, per their own `review_note`, the **mechanical Stage-1 half** of the T4.6
(Spiritual Beings Interface) split — meant to be answered by a direct lookup against `T4`/`T9`
cluster membership in the verse's spans, no LLM interpretation needed. Confirmed earlier in #1700:
**both have zero findings ever.** The mechanism (T4/T9 tagging) exists; the question exists; they
have simply never been connected in an actual run. This is the single most concrete, actionable
item in this whole review — wiring them together needs no new design, just execution.

**T5 → `verse_lexical.is_negator`, live, populated (8,527 rows).** Not tied to one catalogue
question — it's a cross-cutting polarity check relevant to *every* question that asks "does this
verse show X." Belongs in general answer-stage reading instructions, not a dedicated question.

## 3. Designed to matter, but the mechanism isn't built yet

**`role` (multi-valued, complete cluster-code membership per strong) — this is the real answer to
"how should T-codes impact the answer-stage LLM instructions," already specified, not yet built.**
Researcher's own instruction, escalation #1605 §1.0, verbatim: *"if it is a M-code it is likely to
be a char. if it has multiple M-codes, then the meaning of the word need to be resolved in Layer 2
by considering both options. if it is a M-code + T-code then there is tight connection which need
to be read in layer 2 together. if it is a T-code then the type of T-code has a material impact on
its treatment in Layer 2."* **Checked live today: `verse_lexical.role` still holds only
`'content'`/`'function'` (975,478 rows) — the OLD pre-redesign values.** The multi-valued
redesign from the 2026-09-09 proposal has not been applied. Until it is, none of the T-codes beyond
the five already wired via `party_kind`/`is_negator` can mechanically reach Layer 2 at all — the
LLM has no lexicon assist for them, full stop.

## 4. Genuine gaps — no mechanism, no dedicated question

**T6 (Connective) — confirmed gap, already flagged in #1605 §1.2, not yet actioned.** No
`is_connective` column exists (proposed, not built); zero references to `cluster_strong` anywhere
in the enrichment code. This matters directly for T6's own catalogue family
(`T6.2` Sequential Relationships, `T6.3` Causal and Constitutive Relationships) — a verse
containing a T6-tagged connective ("because," "therefore") is a natural, currently-unused trigger
for prioritizing exactly those questions. Recommend: build `is_connective` (same shape as
`is_negator`), and add an answer-stage instruction that its presence should prompt explicit
attention to `T6.2`/`T6.3` for that verse.

**T14 (Body-Parts) — the catalogue question already exists, the lexicon assist does not.**
`T2.1.1` explicitly lists *"a named body part"* as one of the constitutional levels to check, and
`T2.7.1` asks about body-link direction — but unlike T4/T5/T7/T8/T9, there is no denormalized
`verse_lexical` column surfacing T14 membership. The LLM currently has to notice body-part
references unaided. Recommend: same treatment as `is_connective` — a cheap boolean/lookup column,
not a new question (the question already exists and is good — see #1700's T2 review).

**T3 (Operations) — the deepest gap, and it connects directly to #1701.** No live catalogue
question treats a verse's *operation/movement* as the primary object of analysis — every T0–T7
question is framed as an attribute of one characteristic (exactly #1701's entity-vs-system
critique). T3 strongs are the base-data candidate for fixing this: a strong tagged Operations is
*already* flagged as "a human operation/movement, not tied to one cluster." There is a
`cluster_strong.operation` flag column, but it's confirmed dead — **not read anywhere** in
`iba/app/lib/*.py` or `iba/app/handlers/*.py`. Recommend: don't design this in isolation — fold
into #1701 when that's resumed, since "what does the operation itself do, independent of which
characteristic it sits near" is precisely the process-first question #1701 identified as missing.

**T10 (Places), T11 (Corporate-Collective), T12 (Objects-Artifacts), T13 (Natural-World) — no
mechanism, no dedicated question, not yet evaluated for whether one is needed.** These are
referent-identity classifications of the same *kind* as T7/T8/T9, but nothing in T0–T7 currently
asks "does this verse involve a place/collective/object/natural referent, and does that matter."
Whether that's a real gap needing a new question, or something `role`'s eventual complete
enumeration will surface well enough on its own (Layer 2 seeing "this strong is also T10" without
a dedicated question needing to ask for it), is a genuine open call — not decided here.

## 5. Not analytical dimensions — no question needed

**T2 (Supplementary)** — governed by its own live rule (`t2-supplementary-not-blanket-irrelevant`)
already: don't ignore blanket, but it's a residual bucket, not a signal to build a question around.
**T15 (Calendar)** — closed, non-analytic list; no plausible question.

## 6. What this means for answer-stage LLM instructions, concretely

1. **T7/T8 (`party_kind`) already work as designed** — no instruction change needed, but worth
   confirming the answer-stage prompt actually surfaces `party_kind` to the LLM per verse, not just
   that the column exists.
2. **T4/T9 → `T4.6.2a`/`T4.6.3a` should be connected** — the cheapest, most concrete fix available:
   these two questions can be answered mechanically, right now, without waiting on `role`.
3. **T5 (`is_negator`) should be a standing instruction** — "check polarity before asserting a
   verse shows X" — not a question, a reading discipline.
4. **T6/T14 need their lexicon-assist columns built** (`is_connective`, a T14 equivalent) before
   their corresponding questions (`T6.2/T6.3`, `T2.1.1/T2.7.1`) can be as reliably answered as the
   T7/T8-driven ones already are.
5. **`role`'s redesign is the actual long-term answer** to "how do T-codes generally inform Layer
   2" — until it's built, every T-code beyond the five already wired is invisible to the LLM at
   the mechanical level, regardless of how good the catalogue question wording is.
6. **T3 is not a standalone fix** — it's evidence for #1701, not a separate item.

Not decided here, flagged for the researcher: whether to raise T10–T13's "is a dedicated question
needed" as its own follow-on once `role` is built, or fold the whole set into #1701's eventual
resumption.
