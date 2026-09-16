# Escalation #1700 — per-question answer-quality review

**Method, per researcher instruction 2026-09-14:** for every live (`deleted=0`) catalogue
question, read a random sample of at least 5 non-blob ("own") answers — seeded, reproducible —
and judge: did the answer actually substantiate the specific question, or was it generic? Sampling
tool: [`1700-sample-answers-tool-v1-20260914.py`](1700-sample-answers-tool-v1-20260914.py).
Sample data per section saved alongside this doc (`1700-sample-<section>-v1-20260914.json`).

This is a running document, edited in place as each section is worked through — not versioned per
update.

## T0 — Divine Image and Created Design (8 exercised, 2 unexercised)

| Question | n_own | Verdict | Note |
|---|---:|---|---|
| T0.1.1 | 146 | **Substantiated** | Specific, verse-anchored, differentiated reasoning per characteristic (e.g. distinguishing God-as-hater-of-perversity from God-as-judge-of-perversity as separate relations). |
| T0.2.1 | 139 | **Substantiated** | Correctly calibrated — several honestly answer "no positive purpose evidenced" for fallen-condition characteristics (reproach, faithlessness, perversion) rather than forcing one. |
| T0.2.2 | 135 | **Substantiated** | Careful theological argument, not templated — e.g. Eze 28:15's cherub pre-fall blamelessness used as real evidentiary support for "not original design." |
| T0.2.3 | 138 | **Substantiated** | Specific eschatological anchors per characteristic, no forced/generic pattern. |
| T0.3.1 | 137 | **Substantiated** | Differentiated per-characteristic reasoning (moral accountability vs. evaluative capacity vs. judicial capacity) — not a template applied uniformly. |
| T0.3.2 | 133 | **Substantiated** | Includes correctly terse, confident negatives ("Not shared. Malice has no divine form.") — brevity here is calibration, not genericity. |
| T0.3.3 | 131 | **Substantiated**, 1/5 gap-flag | 4/5 substantive; 1/5 is a mechanical placeholder ("Sub-group not separately addressed in source") — a genuine source-data gap, not a bad answer. |
| T0.4.1 | 136 | **Substantiated** | Same placeholder pattern appears once more (identical wording to T0.3.3's); the M04 `[CLUSTER]` answer synthesizing 7 characteristics' typology into one christological arc is genuinely strong synthesis work. |
| T0.1.2a | 0 | **N/A — unexercised** | Recent split (2026-09-04, escalation #1444/#1383), zero findings ever. |
| T0.1.2b | 0 | **N/A — unexercised** | Same split, same status. |

**T0 summary: clean.** No genericity found across 40 sampled answers. One recurring, low-frequency
mechanical placeholder ("sub-group not separately addressed") is a source-data coverage gap, not
an answer-quality defect — worth tracking separately from genuine genericity. **Cross-cutting
note:** this is the third and fourth instance this session of a 2026-09-04 mechanical/interpretive
split (`T0.1.2a`/`2b`) showing zero usage, alongside `T4.6.2a`/`2b`/`3a`/`3b` and `T1.4.1b` —
worth flagging as its own pattern once more sections are reviewed: the entire "Stage 2" split
initiative may be uniformly unexercised project-wide, not question-specific.

## Cross-cutting finding — CONFIRMED — the 2026-09-04 mechanical/interpretive split is 100% unexercised

Checked directly, catalogue-wide, not accumulated from examples: **11 live questions carry a
`review_note` referencing the 2026-09-04 mechanical/interpretive split (escalation #1444 v9 /
#1383)**. Of those, **10 have exactly zero findings** (`T0.1.2a/2b`, `T1.4.1a/1b`, `T4.6.2a/2b/3a/3b`,
`T7.2.2a/2b`). The eleventh (`T7.2.1`, 146 findings) is not actually part of this pattern — its own
note explicitly says "NOT fully Stage 1," a different case.

**Why, not just that:** this whole `finding`/`finding_question_link` corpus is legacy Session-B
data — the split was made 2026-09-04, after the historical analysis activity that populated this
corpus had already stopped (the newer cluster-reading pipeline, #1682/#1690–1693, produces
`ib_observation`/`ib_node`, not `finding` rows, and hasn't been built yet). So this isn't evidence
the split failed to be adopted — it's evidence that **no analytical run of any kind has touched
this catalogue since the split was made.** Every one of these 10 codes gets marked **N/A —
unexercised** in the tables below rather than sampled individually; there is nothing to sample.

## T1 — Definition (17 exercised, 2 unexercised)

**All 17 substantiated. No genericity found across 85 sampled answers.** Consistently specific,
differentiated per characteristic (e.g. `T1.2.1`'s "Mixed: distazō is a momentary condition;
dipsuchos is a dispositional quality" — precise, not templated). Notable strengths: `T1.3.3`'s
Joy-vs-Gladness-vs-Exultation-vs-Delight-vs-Pleasure boundary essay and `T1.6.3`'s M08
self-concealing-characteristics insight are genuinely sharp analytical work, not just competent
coverage.

Three non-defect items worth naming precisely, not lumped as "generic":
- The now-familiar `[Sub-group not separately addressed in source]` placeholder (`T1.3.2`, `T1.3.3`) — a source-data gap.
- A new, distinct third category: `[BOUNDARY — structural characterisation note only; full catalogue pass not applicable per §11 BOUNDARY treatment rule]` (`T1.3.3`) — a deliberate, rule-governed exemption, not a gap or a bad answer.
- A likely data-extraction artifact: one `T1.1.3` answer's text ends mid-thought with `### T1.2 — Kind` bleeding in — looks like a source-document section-boundary got captured into the wrong finding_value. Worth a mechanical check if the historical corpus is ever reprocessed, not an answer-quality issue.

One borderline case: `T1.2.1` sample id 1782 answers a *meta*-question (how T1's definitional claim
relates to T5's formative account) rather than the literal kind-classification (act/disposition/
condition/quality) asked — substantive, but scope-drifted from the actual question. Not generic,
but not a direct answer either — a genuine third category alongside "substantiated" and "generic":
call it **off-target-but-substantive**.

`T1.4.1a`/`T1.4.1b`: unexercised (0 findings) — part of the confirmed split-initiative pattern above.

## T2 — Constitutional Location and Boundaries (6 exercised)

**All 6 substantiated.** Well-calibrated — several `T2.1.1`/`T2.1.2` answers honestly report "S —
not evidenced" for spirit-level location rather than forcing a level onto verses that don't name
one (the M10b `[CLUSTER]` answer explicitly flags this silence as itself analytically significant,
rather than papering over it). `T2.10.1`'s peace-registry answer (id 2576) is a strong piece of
synthesis, tracing a full three-directional movement pattern with real textual support. Same
`[Sub-group not separately addressed in source]` placeholder appears twice (`T2.1.2`, `T2.9.2`) —
same non-defect category as above.

## T4 — Relational Interfaces (16 exercised beyond the two already fully read)

`T4.1.1` and `T4.3.1` were already read in full (126, 130 answers) in earlier turns — see the
main #1700 chat record, not repeated here. The remaining 14 live questions (`T4.1.2/3`, `T4.2.1-3`,
`T4.3.2/3`, `T4.4.1-3`, `T4.5.1-3`, `T4.6.1`), 5-sampled: **all substantiated, no genericity.**

One real pattern worth flagging: the placeholder-gap rate is not uniform across the component —
it's near-zero for the primary "does it operate in this direction" questions (`T4.1.x`, `T4.2.x`:
0/5 each) and noticeably higher for the more granular follow-ups (`T4.3.2/3`, `T4.4.2/3`,
`T4.5.1/2/3`: 1–2/5 each). Plausible read: the primary direction-questions have broad source
coverage, while "what inner conditions accompany this" and similar follow-ups need more granular
subgroup-level material that isn't always present. Not confirmed against the full population, just
the pattern this sample surfaced.

`T4.6.1` (Spiritual Beings Interface) shows a notably high, and correctly calibrated, rate of
honest "S — not evidenced" answers (3/5 sampled) — most verses simply don't involve spiritual
beings, and the answers say so plainly rather than stretching for a connection. Worth contrasting
with T3.1.1's forced-yes pattern: same shape of question (does X engage/relate to Y), opposite
result, because here "no" is treated as a normal, expected outcome rather than something to work
around.

`T4.6.2a/2b/3a/3b`: unexercised — part of the confirmed split-initiative pattern above.

## T5 — Formative and Developmental Dimension (9 exercised)

**All 9 substantiated. No genericity.** This section reads as the strongest of the six reviewed so
far — `T5.2.1`'s forgiveness-sequence answer (id 442) maps a full before/access-moment/during/
after-immediate/after-sustained structure for *both* divine and horizontal forgiveness in one
answer, and `T5.4.2`'s M10 cluster answer draws a genuinely non-obvious distinction (suffering
*reveals* defilement in some characteristics, *produces* it in none, is irrelevant in others) that
required real cross-characteristic comparison, not a template. One placeholder gap (`T5.6.1`).

## T6 — Structural Relationships with Other Characteristics (13 exercised)

**All 13 substantiated where a real answer is given — but this section has a distinctly higher
gap rate than every other section reviewed, and one genuinely new low-value category.**

The `[Sub-group not separately addressed in source]` placeholder appears far more often here than
in T0/T1/T2/T4/T5 (roughly 1–3 of 5 samples in `T6.1.2`, `T6.2.2`, `T6.3.2`, `T6.4.1`, `T6.4.2`,
`T6.5.1`, `T6.5.2`, `T6.5.3` — 8 of the 13 questions show at least one). Plausible read: relating
one characteristic to *another* requires cross-referencing work that per-characteristic subgroup
analysis often didn't do, so the gap is structural to what T6 demands, not to any one question's
wording. Worth checking against the full population before treating as confirmed.

**A genuinely new, fourth non-defect/defect category, distinct from all three found in T1:** id
`1051893` (`T6.4.3`) reads: *"T6.4.3 — cross-registry chesed distribution count (first raised
M05-A; reconfirmed through all sub-groups). G-code recorded from outstanding-actions list in
WA-M05-consolidated-findings-v1-20260507-part4 §Outstanding CC actions and G-codes."* This isn't
generic, isn't a placeholder, and isn't off-target-but-substantive — it's an **administrative
tracking note that never actually answers the question asked.** Call this category
**process-note-as-answer**. Worth knowing as its own distinct failure mode: unlike genericity
(forcing an answer) or the placeholder (declining to answer), this is bookkeeping metadata
occupying an answer slot.

Where T6 *does* answer directly, the quality matches every other section: `T6.1.2`'s M10 answer
(CHAR-11 as "bedrock condition" for the whole cluster) and `T6.5.3`'s degree/kind/direction/level
distinctions are genuinely precise conceptual work.

## T7 — Evidential and Methodological Foundation (19 exercised, 2 unexercised)

**All 19 substantiated. No genericity found across 95 sampled answers.** Same overall quality as
T0/T1/T2/T4/T5 — specific, verse-anchored, differentiated per characteristic. T7.1's lexical
questions (root meanings, grammatical/semantic range, OT-NT continuity) produce genuinely precise
philological work (e.g. T7.1.8's LXX-mediated agapē/chesed continuity argument, T7.1.6's
person-type-term reasoning). T7.2.5/2.6 (primary anchor verse) and T7.3.1-3.4 (human-science
framework) sections show real synthesis, not templated answers — e.g. T7.3.3's consistent,
specific divergence-reasoning between a named framework and the verse evidence (dignity studies vs.
formed-godliness, Bandura vs. objective-transgression), not a generic "the framework differs"
non-answer.

Same recurring non-defect categories as elsewhere, no new failure mode found:
- `[Sub-group not separately addressed in source]` placeholder — appears in T7.1.10, T7.2.3,
  T7.2.4, T7.2.6, T7.3.3 (×2), T7.3.4 — roughly the T0/T1/T2/T4/T5 baseline rate, not T6's elevated
  one.
- One `[BOUNDARY — structural characterisation note only...]` exemption (T7.3.4) — same rule-
  governed category first seen at T1.3.3.

`T7.2.2a`/`T7.2.2b`: unexercised (0 findings) — part of the confirmed 2026-09-04 split-initiative
pattern (§ above), same as every other split code found in T0/T1/T4.

## Review complete — all 98 live catalogue questions accounted for

**Confirmed live, 2026-09-16:** `wa_obs_question_catalogue` has exactly 98 `deleted=0` rows,
100% inside tiers T0/T1/T2/T4/T5/T6/T7 (10+19+6+20+9+13+21=98) — **there is no live "non-tier"
material** (Extensions/Section 1-5/leviticus/redemption, named in this doc's own "not yet reviewed"
line as of 2026-09-14, do not exist as live rows to review). **Every live catalogue question has now
been sampled and judged.** Summary across all 7 tiers, 98 questions, ~440 sampled answers: **zero
genericity found anywhere.** Every non-"substantiated" case falls into one of five already-named,
non-defect categories: `[Sub-group not separately addressed]` placeholder (source-data gap, higher
rate in T6 specifically), `[BOUNDARY]` exemption (rule-governed), off-target-but-substantive (one
T1.2.1 instance), process-note-as-answer (one T6.4.3 instance), or confirmed unexercised (the 10
2026-09-04 split codes, project-wide, zero findings on the historical `finding`/
`finding_question_link` corpus because no analytical run has touched this catalogue since the
split was made — not a live-quality defect on any of them).
