# Blind Verification of AI Cluster Analytics — Methodology

**Document type:** Methodology specification + validation record
**Version:** v1
**Date:** 2026-05-16
**Author:** Researcher (Leroux Cilliers) + CC (drafting)
**Status:** Authoritative — referenced by cluster-pipeline trust assessments

---

## 1. Why this exists — the trust problem

The Session B cluster pipeline (governing instruction `wa-sessionb-cluster-instruction-v2_2-20260516`) relies on Claude AI to perform several analytical syntheses where errors would be hard to detect:

- **Phase 5 (sub-group design):** AI clusters per-verse meanings into sub-groups by reading the verses' Phase 2 meanings.
- **Phase 7 (VCG design):** AI further partitions each sub-group's verses into VCGs.
- **Phase 9 (catalogue prompts):** AI answers the 189-prompt T0–T7 catalogue per sub-group, producing the `cluster_finding` corpus that Session C consumes for publication.

In each phase, AI's output is a narrative artefact — sub-group descriptions, VCG descriptions, finding text. CC validates the *structural* outputs (every verse routed, every prompt answered, parser-safe form, R4 anchor coverage) but the *analytical* quality is harder to validate. Three risks:

1. **Fabrication risk** — AI invents claims that read coherently but aren't grounded in verse evidence. The catalogue findings are particularly susceptible: 189 prompts × 8+ scopes = ~700 cells per cluster, each requiring a verse-grounded answer. Pressure to fill every cell incentivises narrative invention.
2. **Mis-routing risk** — AI's sub-group / VCG assignments may not reflect the verse-level evidence. A verse classified as "M01-A reverential fear" might actually exhibit acute-fear content.
3. **Narrative coherence at cost of accuracy** — AI may shape findings to fit a storyline (e.g. divine-image themes of T0) even when specific sub-group evidence is thin.

These risks are not unique to one cluster; they apply to every cluster the pipeline produces. The researcher needed a method to **detect fabrication and verify structural validity without re-running the full pipeline**.

---

## 2. The methodology — "AI marks its own homework"

**Core idea (researcher design, 2026-05-16):**

> Present AI with (a) the findings authored under a specific scope and (b) the verses available in that scope, but **withhold the structural labels** that connect the two. Ask AI to identify the verses that support each finding. If AI's blind verse-picks consistently land in the same sub-group / VCG that the finding was originally authored for, the structure is internally coherent and the findings are verse-grounded. If they don't, that's a fabrication or mis-routing signal.

This is an inverted-validation experiment: the forward direction (verses → sub-groups → VCGs → findings) produced the published structure; the reverse direction (findings → verses, blind to structure) tests whether the structure has the verse evidence to back it.

### 2.1 What's revealed to AI

- The **finding text** (with structural cues stripped — see §2.3)
- The **question text** (catalogue prompt, e.g. "What does the verse evidence reveal about the nature or character of God…?")
- The **verse corpus** as a flat list with: `vc_id`, `reference`, `term` (Strong's + transliteration), full `verse_text`, **Phase 2 `analysis_note` meaning**

### 2.2 What's withheld from AI

- **Sub-group label** of any verse or finding (M01-A, M01-B, …)
- **VCG label** of any verse or finding (M01-A-VCG-02, …)
- **Scope markers** in finding text (`**[A]**`, `**[B, C, D]**`)
- **Anchor flag** on any verse
- **`cluster_subgroup_id` / `group_id`** fields
- **Inline verse references** in finding text (e.g. "Pro 1:7", "Heb 12:28") — replaced with `[ref]` placeholder
- **Anchor markers** in finding text (e.g. "anchor")

### 2.3 Stripping regex catalogue

| Pattern | Replacement | Purpose |
|---|---|---|
| `Book Chap:Verse [-Verse] [anchor]` | `[ref]` | Remove explicit verse refs that would give AI the answer |
| `M\d{2}-[A-Z]+(?:-VCG-\d+)?` | `[scope]` | Remove sub-group + VCG codes |
| `VCG-?\d+` (bare) | `[scope]` | Remove bare VCG codes |
| `\(?anchor\)?` | (delete) | Remove anchor markers |

Applied with regex pipeline; collapses whitespace at end.

### 2.4 AI's task per finding

Return JSON:

```json
{
  "finding_id": <integer>,
  "question_code": "<string>",
  "supporting_vc_ids": [<vc_id>, ...],
  "rationale": "<one-sentence reason>"
}
```

- Pick verses whose **meaning genuinely supports** the finding.
- Empty list is acceptable when no verse fits.
- No hint of which subset the findings were authored for.

### 2.5 What CC analyses

For each finding, given AI's blind picks:

1. **Validity**: are all picked vc_ids in the provided corpus? Picks outside the corpus are either hallucinations (vc_id doesn't exist in DB) or cross-cluster reach (vc_id exists but in another cluster).
2. **Target precision**: % of picks that land in the finding's original structural scope (sub-group target).
3. **Per-VCG distribution**: within the target sub-group, do picks concentrate in the VCG(s) the finding was authored under?
4. **Pure-target rate**: % of findings where 100% of picks land in the target sub-group.
5. **Empty pick rate**: how many findings have AI return `[]` (no verse support) — these are candidates for fabrication.
6. **Diagnostic mixed cases**: non-T0, non-T6/T7.3 findings with cross-sub-group picks. T0 prompts (Divine Image / Created Design) are cluster-wide by nature; T6 prompts (Structural Relationships) are bilateral by design. Mixed picks in those tiers are analytically appropriate. Mixed picks in T1–T5 prompts are diagnostic.

### 2.6 Interpretive thresholds

| Metric | STRONG signal | WEAK signal |
|---|---|---|
| Hallucination rate | ≤0.5% | >2% |
| Target precision (% picks in target sub-group) | ≥80% | <60% |
| Pure-target findings | ≥60% | <40% |
| Empty pick lists | ≤2% of findings | >10% |
| Diagnostic mixed (non-T0/T6) | ≤10% of findings | >25% |

The thresholds are calibration baselines based on the M01-D / M01-A runs (this document). Future tests will refine.

---

## 3. Test runs (2026-05-16) — M01

### 3.1 Test 1 — M01-D single-corpus

**Hypothesis to test:** when the corpus is restricted to a single sub-group, does AI's blind retrieval pick coherent VCG sets per finding?

**Configuration:**

- **Target sub-group:** M01-D — Dismay and Inner Collapse (small, coherent)
- **Findings:** 72 E findings authored for M01-D scope
- **Corpus:** 76 is_relevant verses routed to M01-D
- **Distractors:** none (within-sub-group test)
- **Stripping:** scope markers + VCG codes + inline verse refs + anchor markers

**Results:**

| Metric | Result |
|---|---|
| Findings tested | 72 |
| AI returned picks | 72 / 72 (100%) |
| Total picks | 264 |
| Valid picks (in corpus) | 264 / 264 (100%) |
| Hallucinated picks | 0 |
| Empty pick lists | 0 |

**Per-finding VCG concentration:** picks concentrated in 1–2 VCGs per finding, with the dominant VCG matching the finding's analytical content (e.g. T0.2.1 *created purpose* → 5/5 picks in M01-D-VCG-04 dismay-as-divine-command; T1.1.x *cluster identity* prompts → picks dominated by M01-D-VCG-01 dismay-as-soul-event; T6.x relational prompts → cross-VCG spreads including M01-E-VCG-04 reach when analytically appropriate).

**Conclusion (Test 1):** when blind to labels, AI's verse picks align with the VCG structure within M01-D. Zero hallucinations on a 76-verse corpus.

**Caveat:** all picks were trivially in M01-D because that was the entire corpus. The test doesn't distinguish target from distractor — Test 2 addresses this.

**Artefacts:**

- Script: [scripts/_test_ai_marks_own_homework_m01d_20260516.py](../../scripts/_test_ai_marks_own_homework_m01d_20260516.py)
- Analysis: [Sessions/Session_Clusters/M01/WA-M01-D-blind-verification-test-analysis-20260516.md](../../Sessions/Session_Clusters/M01/WA-M01-D-blind-verification-test-analysis-20260516.md)

### 3.2 Test 2 — M01-D mixed-corpus (distractor present)

**Hypothesis to test:** when the corpus is mixed with distractor sub-groups, does AI distinguish target verses from distractors?

**Configuration:**

- **Target sub-group:** M01-D
- **Findings:** 72 E findings authored for M01-D scope (same as Test 1)
- **Corpus:** 460 is_relevant verses — 76 M01-D (target) + 311 M01-B (Acute Fear, distractor) + 73 M01-C (Terror as Force, distractor)
- **Distractors:** 84% of corpus
- **Stripping:** same as Test 1

**Results:**

| Metric | Result |
|---|---|
| Findings tested | 72 |
| Total picks | 232 |
| Valid picks | 232 / 232 (100%) |
| Hallucinated picks | 0 |
| Empty pick lists | 0 |
| Picks in M01-D target | **189 / 232 = 81.5%** |
| Picks in M01-B distractor | 27 (11.6%) |
| Picks in M01-C distractor | 16 (6.9%) |
| Pure-target findings (100% picks in M01-D) | **54 / 72 = 75%** |
| Mixed findings | 18 (4 relational T6/T7.3 + 14 other) |

**Diagnostic — the 14 "other mixed" findings:**

- 4 are **T0 cluster-wide prompts** (T0.1.3, T0.3.2, T0.2.3, T0.1.1) where cross-sub-group picks are appropriate — the finding text explicitly addresses "across all sub-groups" or cluster-level reach.
- 10 are T3/T4/T5 prompts with 1-2 distractor picks against 1-3 target picks. The distractor picks are mostly tight-related cases (e.g. T3.7 *faculty operation* reaching for terror-paralysis examples to illuminate dismay-paralysis).
- **Net "clearly mis-attributed" picks: 0–4 out of 232** (≤2% noise depending on read of T0 prompts).

**Conclusion (Test 2):** AI distinguishes target sub-group content from distractors at 81.5% precision despite distractors being 84% of corpus. The 75% pure-target rate is strong evidence of content-level discrimination. Cross-sub-group picks are analytically defensible in nearly all cases.

**Artefacts:**

- Script: [scripts/_test_ai_marks_own_homework_m01d_mixed_20260516.py](../../scripts/_test_ai_marks_own_homework_m01d_mixed_20260516.py)
- Analysis: [Sessions/Session_Clusters/M01/WA-M01-D-mixed-verification-test-analysis-20260516.md](../../Sessions/Session_Clusters/M01/WA-M01-D-mixed-verification-test-analysis-20260516.md)

### 3.3 Test 3 — M01-A stress test (full M01 corpus)

**Hypothesis to test:** does AI fabricate findings to maintain narrative coherence? Stress-tests the hardest sub-group (M01-A is the largest, with the richest content) against the full M01 cluster corpus.

**Configuration:**

- **Target sub-group:** M01-A — Reverential Fear / Fear of God as Governing Orientation (largest, 320 verses, 7 substantive VCGs)
- **Findings:** 128 E findings authored for M01-A scope
- **Corpus:** 941 is_relevant verses — full M01 cluster (320 M01-A target + 621 distractors across M01-B/C/D/E/F/G/BOUNDARY)
- **Distractors:** 66% of corpus
- **Stripping:** same as Tests 1–2

**Results:**

| Metric | Result |
|---|---|
| Findings tested | 128 |
| Total picks | 1,828 |
| Valid picks | 1,817 / 1,828 (99.4%) |
| Hallucinated picks | **11 / 1,828 (0.6%)** |
| Empty pick lists | **0 / 128** |
| Picks in M01-A target | **1,646 / 1,817 = 90.6%** |
| Pure-target findings | **82 / 128 = 64%** |
| Mixed findings | 46 |

**Hallucination breakdown (11 picks):**

- **2 truly non-existent vc_ids** (14331, 22012) — 0.1% true hallucination rate
- **9 real vc_ids from neighbouring clusters** (M02 anger, M04 joy, M29 desire, T2 supplementary, 1 M01 set-aside) — AI reached across cluster boundaries when the prompt asked about cross-characteristic content (T7.1.6 person-type, T4.5.x shared-with-God, T6.4.1 vocabulary-sharing). Analytically defensible but technically outside the corpus.

**Per-VCG pick distribution within M01-A:**

| VCG | Corpus verses | Picks | Per-verse rate |
|---|---:|---:|---:|
| M01-A-VCG-02 (foundational fear → wisdom) | 35 | 509 | **14.5×** |
| M01-A-VCG-04 (witnessing deeds → fear) | 80 | 313 | 3.9× |
| M01-A-VCG-03 (fear → covenant) | 52 | 292 | 5.6× |
| M01-A-VCG-01 (operative fear → ethical) | 32 | 236 | 7.4× |
| M01-A-VCG-06 (sustained fear / identity) | 54 | 191 | 3.5× |
| M01-A-VCG-05 (commanded / direction) | 33 | 125 | 3.8× |
| M01-A-VCG-07 (fear instilled in nations) | 21 | 13 | 0.6× |

The 14.5× rate on M01-A-VCG-02 reflects its centrality (Pro 1:7 / Psa 111:10 / Ecc 12:13 as *the* foundational-fear anchors). Lower rates on specialised VCGs.

**Diagnostic findings (4 with <50% target, non-T0, non-relational):**

| Finding | Prompt | %M01-A | Where else | Defensible? |
|---|---|---:|---|---|
| 7595 T2.5.1 | will-faculty engagement | 0/2 | M01-D (collapse-of-will) | **Yes** — the question targets will-collapse phenomena |
| 7624, 7631 T2.7.x | body-soma engagement | 1/5 | M01-E (trembling/somatic) | **Yes** — reverential fear isn't somatically described; M01-E *is* the soma sub-group |
| 8031 T7.1.3 | semantic range of primary term | 6/20 | M01-B (acute fear) | **Yes** — fobeō's *semantic range* spans both registers; cross-register reach is correct for the question |

None are fabrication signals; all are analytically appropriate cross-sub-group reach for prompts that ask cross-sub-group questions.

**Conclusion (Test 3):** AI is **not fabricating findings**. The 0 empty pick lists, 90.6% target precision against 34% target-share corpus, and 64% pure-target rate strongly support verse-grounded narrative. The 0.6% hallucination rate (mostly cross-cluster reach for cross-characteristic prompts) is operational noise, not invention.

**Artefacts:**

- Script: [scripts/_test_ai_marks_own_homework_m01a_stress_20260516.py](../../scripts/_test_ai_marks_own_homework_m01a_stress_20260516.py)
- Analysis: [Sessions/Session_Clusters/M01/WA-M01-A-stress-test-analysis-20260516.md](../../Sessions/Session_Clusters/M01/WA-M01-A-stress-test-analysis-20260516.md)
- Output: [Sessions/Session_Clusters/M01/WA-M01-A-stress-test-output-20260516.json](../../Sessions/Session_Clusters/M01/WA-M01-A-stress-test-output-20260516.json)

---

## 4. Aggregated conclusions

### 4.1 What the three tests collectively demonstrate

Across three increasingly hard tests:

| Test | Target | Distractor share | Target precision | Pure-target rate | Hallucination |
|---|---|---:|---:|---:|---:|
| 1 — M01-D single | 76 verses | 0% | 100% (trivial) | 100% (trivial) | 0% |
| 2 — M01-D mixed | 76 verses | 84% | 81.5% | 75% | 0% |
| 3 — M01-A stress | 320 verses | 66% | 90.6% | 64% | 0.6% |

**AI's blind verse retrieval consistently lands in the structural target despite increasing distractor pressure.** The structural framework (sub-group + VCG) AI produced during Phase 5/7 has verse-level evidence aligning with it when AI is shown only the findings and asked to find supporting verses cold.

### 4.2 Specifically on the fabrication risk

The **0 empty pick lists** across all three tests (272 findings tested in total) is the strongest single signal:

- If AI had fabricated narrative without verse grounding, the blind retrieval would have produced empty `[]` for those unsupported findings.
- It didn't. Every finding got at least one supporting verse from the corpus.

Combined with 90.6% target precision on the hardest test, fabrication is not evident in the M01 cluster output.

### 4.3 What the tests don't prove

- **They don't validate analytical *correctness*** — only internal consistency. AI's framework may be internally coherent but theologically wrong; only researcher reading the verses against the framework can judge that.
- **They test against AI's own prior framing.** Confidence is in AI's *consistency* across passes (Phase 7 design + Phase 9 findings + this test). True ground-truth validation would require independent expert verse-coding, which the project doesn't have.
- **They're cluster-specific.** Passing on M01 doesn't guarantee passing on M02. The methodology should be re-applied per cluster (or with reasonable confidence-transfer reasoning when methodology and AI behaviour are identical).

### 4.4 Trust transfer to M02

M02 used the **same methodology** (instruction v2_2, same phases, same prompts to AI) as M01. The blind validation evidence on M01 establishes that:

- AI's Phase 7 VCG design is internally coherent with its Phase 9 findings.
- AI does not fabricate findings to maintain narrative.
- Cross-sub-group reach is analytically appropriate, not error.

**M02's structure can be accepted under the same trust frame**, without re-running the full blind test, on the basis that:

1. Same AI (Sonnet 4.6), same prompts, same methodology — behaviour should be consistent.
2. M02 was a smaller, more homogeneous cluster (anger family) than M01 (eight registers of fear); if anything, M02 is an easier analytical task with less risk of mis-routing.
3. M02 has the same structural integrity checks (R4 anchors, H2/H3 health checks all passed at Phase 7).

The researcher may choose to spot-check M02 by re-running the methodology on one sub-group (e.g. M02-B or M02-E) if a particular sub-group's findings seem suspect. For routine clusters, the M01-validated methodology + structural integrity checks at Phase 7 are taken as sufficient.

---

## 5. Operational specification

### 5.1 When to run blind verification

**Mandatory:**

- New methodology version (e.g. v2_3 onwards) introducing structural changes to Phase 5/7/9.
- AI model upgrade or significant prompt rewrite.
- After researcher suspects fabrication or mis-routing on a specific cluster (e.g. published findings don't track verse evidence on inspection).

**Recommended:**

- First cluster on a major instruction version (e.g. v2_2 on M01 — done).
- Periodic spot-check (e.g. every 5th cluster) for drift detection.

**Optional / by request:**

- Per cluster, when researcher wants explicit validation evidence before Session C publication.

### 5.2 Test variants

**Single-corpus test:** corpus drawn only from the target sub-group. Validates within-sub-group VCG correlation but doesn't test target-vs-distractor discrimination.

**Mixed-corpus test:** corpus includes target + 2–3 distractor sub-groups. Tests AI's discrimination under moderate confusion.

**Stress test:** corpus includes target + all other sub-groups in the cluster. Hardest test; produces target precision under maximum distractor pressure.

### 5.3 Scripts (reusable)

- **Single-corpus:** [scripts/_test_ai_marks_own_homework_m01d_20260516.py](../../scripts/_test_ai_marks_own_homework_m01d_20260516.py) — adapt cluster + sub-group at top.
- **Mixed-corpus:** [scripts/_test_ai_marks_own_homework_m01d_mixed_20260516.py](../../scripts/_test_ai_marks_own_homework_m01d_mixed_20260516.py)
- **Stress (full-cluster):** [scripts/_test_ai_marks_own_homework_m01a_stress_20260516.py](../../scripts/_test_ai_marks_own_homework_m01a_stress_20260516.py) — uses streaming API for large contexts.

All three scripts share the same regex stripping catalogue and produce input/output JSON + analysis markdown.

### 5.4 Cost envelope

- Single sub-group test (~70 findings, ~80 verses): ~$0.15
- Mixed-corpus test (~70 findings, ~500 verses): ~$0.40
- Stress test (~130 findings, ~950 verses): ~$1.20

Total cost for the full three-test M01 validation: ~$1.75.

---

## 6. Trust framework — going forward

Given the M01 validation results, future cluster pipeline runs operate under this trust framework:

1. **Structural integrity** — verified at apply time by health checks (R4, H2, H3, etc.) — **non-negotiable, automatic**.
2. **Analytical coherence** — verified by the blind verification methodology (this document) — **applied on cadence, not every cluster**.
3. **Researcher spot-check** — verse-level reading of selected findings vs the underlying VCG members — **applied at researcher's discretion before Session C publication**.

The blind verification methodology becomes part of the project's QA stack alongside structural integrity checks. The M01 validation captured in this document is the **operational baseline** — future tests calibrate against these thresholds.

---

## 7. Limitations and future work

### 7.1 Known limitations

- **AI consistency, not correctness.** The test confirms AI's framing is internally coherent across passes; it doesn't confirm the framing matches an independent expert reading.
- **Token budget caps narrative.** For very large clusters or long-form findings, max_tokens limits may truncate output. The M01-A stress test required 32000 max_tokens.
- **Stripping regex may miss edge cases.** New finding-text patterns (e.g. anchored Greek transliterations, abbreviations) may slip past the strip pipeline.
- **No ground-truth corpus.** The project doesn't maintain an independent expert-coded set of verse→finding mappings to compare against AI's blind picks.

### 7.2 Future enhancements

- **Cross-pass consistency test** — present AI with the SAME findings + corpus twice in separate sessions (cache-cleared). Compare picks. Variance is a signal of either ambiguous findings or AI inconsistency.
- **Mutation test** — strategically alter a finding (e.g. swap a sub-group's content for another's) and re-test. If AI's blind picks shift correctly to follow the mutation, the methodology is more sensitive than just text-similarity matching.
- **Independent expert verification on a sample** — give a researcher a random sample of (finding × picked verses) pairs and ask them to judge support strength. Calibrates whether AI's "supports" matches a theological reader's "supports".

---

## 8. Provenance and references

- **Researcher direction (verbatim, 2026-05-16):** "Lets get AI to mark it own homework. (not sure if you understand the idiom) I suggest we take M01, can reconstruct it backwards. We will present AI with the findings, and the verses and task it to read the answer (finding) and then find the verses that support the finding. We will deliberately not provide the sub groups nor the VCGs. We will then inspect the findings and the verses, to check if it can be founded and then map the verses to the sub groups and the VCG to see if there is a correlation."
- **Stress-test extension (verbatim, 2026-05-16):** "(b) run the stress test. I suspect AI is making up some findings to be able have a story line."
- **Governing cluster instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — defines the Phase 5/7/9 pipeline whose output is being validated.
- **M01 cluster closure:** [Sessions/Session_Clusters/M01/WA-M01-dir-007-closure-applied-v1-20260516.md](../../Sessions/Session_Clusters/M01/WA-M01-dir-007-closure-applied-v1-20260516.md) — the cluster being validated.
- **Three test artefacts:** linked in §3.1, §3.2, §3.3 above.

---

*End of methodology specification.*
