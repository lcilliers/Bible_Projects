# Session log — Term-anchor reset (clustering pivot)

**Date:** 2026-05-04
**Researcher:** le Roux Cilliers
**AI roles:** Claude Code (CC) — exploratory scripts, vector builds, clustering, validation
**Status:** Exploratory — no DB writes; no patches applied; pipeline architecture under reconsideration
**Pre-context:** Continues from session of 2026-05-03 (verse-context audit, empty-registry merges, POS-noise set-aside, brief-meaning-router prototype). Prior session ended at 20:14 with the cost concern: "using the API for the entire corpus is prohibitively expensive — I will give it more thought tomorrow."
**Background motivation:** [research/notes/program reset.md](../../research/notes/program%20reset.md) — registry-driven analysis judged unreliable; pipeline must shift from registry → terms-and-verses as primary, with registry's role diminished after term/verse identification.

---

## 1. Researcher direction (chronological)

The researcher steered the day through a series of progressively sharper pivots. Quoting the load-bearing prompts:

| Time | Pivot |
|---|---|
| 04:10 | "we are over engineering. the first objective is to group all the verses with similar meaning together. so all we need is a very brief, in plain English, for — what does the verse say." |
| 04:54 | "the count of owner term-verse and unique verse reference is not the same. Can you check." |
| 04:59 | "for determining the brief verse context we must look at all the spans. so the pairing is verse text : included spans. wrong_face should be irrelevant." |
| 05:12 | "why do you need a per term set aside decision?" — pushed CC away from per-term routing toward per-verse routing. |
| 05:59 | "the dimension review step also goes — fundamentally dimensions created noise, built on wrong assumptions." |
| 06:07 | Volume challenge surfaced: full corpus through the API is prohibitive. |
| **06:13** | **Core pivot:** "the registry is potentially misleading as a grouping driver. The registry was a method of collating all the terms… should we try to group the terms instead." |
| 06:27 | Direction set: build a term-vector from term data; build a term-verse-span vector; cluster on these. |
| 06:51 | "do not use the verse_context_group at all in this clustering — these groups have shown to be limited and incomplete in value." |
| 06:56 | Weighting design: shared root = primary cluster signal; shared gloss = primary; Mounce = cross-cluster bridge indicator (either-or); meaning = differentiator within cluster. |
| 07:08 | "positive/negative of the same characteristic may need to be in the same cluster… let go of the registry relationship in our clustering — it is proven that the registry is not help, it is a distraction." |
| 09:47 | Cross-language probe: "does all the greek cluster overlap with hebrew clusters, and if not, why not." |
| 10:58 | Coverage probe: "check how many verses in T1 terms has no group associated with it (not yet classified)." |

The cumulative effect: **registry-as-driver, dimension-review, and verse_context_group are all dropped from the new clustering pipeline.** Terms become the unit of analysis; verses provide meaning evidence; registries retain residual surface-only role.

## 2. What was built

All artefacts are exploratory (`scripts/_exploratory_*_20260504.py`) writing to `outputs/markdown/`. **No DB writes, no patches.**

### 2.1 Brief-router prototypes (early-morning, before the registry pivot)

Per-verse classifier replaces per-term-pair classifier. `wrong_face` field dropped. Smoke + manual tests on Sonnet 4.6.

| Script | Output |
|---|---|
| `_exploratory_unclassified_sample_v1` | [unclassified-sample-100-pairs-20260504.json](../../outputs/markdown/unclassified-sample-100-pairs-20260504.json) |
| `_exploratory_unclassified_concentrated_sample_v1` | [unclassified-sample-100-pairs-H3045-20260504.json](../../outputs/markdown/unclassified-sample-100-pairs-H3045-20260504.json) |
| `_exploratory_unclassified_verse_sample_v1` | 50-verse samples for H3034, H4191 |
| `_exploratory_brief_meaning_router_v1` | [brief-meaning-router-results-claude-sonnet-4-6-20260504.md](../../outputs/markdown/brief-meaning-router-results-claude-sonnet-4-6-20260504.md) |
| `_exploratory_brief_verse_router_v1` | [brief-verse-router-results-claude-sonnet-4-6-20260504.md](../../outputs/markdown/brief-verse-router-results-claude-sonnet-4-6-20260504.md) |
| `_exploratory_thin_verse_router_v1` | [thin-verse-router-results-claude-sonnet-4-6-20260504.md](../../outputs/markdown/thin-verse-router-results-claude-sonnet-4-6-20260504.md) (+ H3034, H4191 spot-checks) |

These remained valid as a verse-classification mechanism, but their downstream consumer changed at 06:13 (registry-keyed grouping → cluster-keyed grouping).

### 2.2 Term-vector construction

Three vector spaces built, one term per row, OWNER terms only (~2,491 aligned):

| Space | Script | Output |
|---|---|---|
| Usage (verse-occurrence pattern) | `_exploratory_term_usage_vector_v1` | `term-usage-vectors-20260504.npz` + `.meta.json` |
| Semantic (gloss + meaning text, sentence-transformer) | `_exploratory_term_semantic_vector_v1` | `term-semantic-vectors-20260504.npz` + `.meta.json` |
| Semantic-weighted (root family + Mounce bridges + gloss + meaning, weighted per researcher direction at 06:56) | `_exploratory_term_semantic_vector_weighted_v1` | `term-semantic-weighted-vectors-20260504.npz` + `.meta.json` |
| Co-occurrence (terms sharing a verse — verse-span vector, per 06:51) | `_exploratory_term_cooccurrence_vector_v1` | `term-cooccurrence-vectors-20260504.npz` + `.meta.json` |

Smoke/test variants: `term-semantic-smoke-20260504.npz`, `term-usage-smoke-20260504.npz`.
Mounce bridge enumeration (NT cross-cluster signal): `term-mounce-bridges-20260504.json`.

### 2.3 Cluster assessment — registry vs cluster alignment

[term-cluster-assessment-20260504.md](../../outputs/markdown/term-cluster-assessment-20260504.md) (+ co-occurrence and weighted variants) compared 12 runs: {semantic, usage, combined} × k ∈ {40, 80, 120, 180}.

**Headline finding:** at the best granularity (`combined__k120`), registries dominate their own cluster only **50.6%** of the time on average; **76 of 120 clusters cross-cut 3+ registries with no dominant home**. Worst-aligned registries — R151 sorrow (13.0%), R051 distress (14.1%), R187 strength (14.2%), R140 seeking (16.7%), R173 will (17.9%) — show the registry structure systematically miscuts the data. Best-aligned (small, single-anchor registries: R065 generosity, R164 truthfulness, R029 contentment) hit 100% but on tiny term counts. Quantitative confirmation of the researcher's 06:13 hypothesis.

### 2.4 Clustering iterations

Six successive cluster designs, each correcting the previous:

| Variant | Script | Notable change |
|---|---|---|
| loci-split | `_exploratory_term_loci_split_cluster_v1` | Inner-being seat terms separated from characteristic terms |
| 3-way | `_exploratory_term_3way_cluster_v1` | LOCUS / CHARACTERISTIC / OTHER buckets |
| 4-way v1 | `_exploratory_term_4way_cluster_v1` | LOCUS / HEBREW / GREEK / HDBSCAN-cross-language |
| 4-way v2 | `_exploratory_term_4way_cluster_v2` | Bucket boundaries tightened; qualifiers split |
| 5-way v1 | `_exploratory_term_5way_cluster_v1` | Qualifier bucket added (adverb/intensifier); separated from primary clustering |
| 5-way v2 | `_exploratory_term_5way_cluster_v2` | Final pre-anchor structure; bucket-summary + qualifier exports |

Cluster-quality assessment: [term-cluster-quality-v2-20260504-summary.md](../../outputs/markdown/term-cluster-quality-v2-20260504-summary.md) (per-language Hebrew + Greek breakdowns).

### 2.5 Cross-language probe

[term-clusters-crosslang-20260504.md](../../outputs/markdown/term-clusters-crosslang-20260504.md) — answers researcher's 09:47 question. Not all Greek clusters overlap Hebrew clusters; documented bridges and language-specific clusters (NT-only theological vocabulary that has no OT semantic counterpart).

### 2.6 Final term-anchor build

`_exploratory_term_anchor_build_v1_20260504.py` produces the canonical structure published as [outputs/markdown/wa-term-anchor-20260504.json](../../outputs/markdown/wa-term-anchor-20260504.json) with three companion reports:

- [wa-term-anchor-20260504-summary.md](../../outputs/markdown/wa-term-anchor-20260504-summary.md)
- [wa-term-anchor-20260504-clusters.md](../../outputs/markdown/wa-term-anchor-20260504-clusters.md)
- [wa-term-anchor-20260504-flags.md](../../outputs/markdown/wa-term-anchor-20260504-flags.md)

**Bucket distribution:**

| Bucket | Count | Role |
|---|---|---|
| T1 | 1,752 | Primary characteristics — drove clustering |
| T2 | 491 | Secondary characteristics — attached to T1 cluster via co-occurrence |
| FLAG | 24 | Borderline — manual review required |
| LOCUS | 0 | (clustered separately in earlier loci-split step; folded into T1 by final build) |
| EXTRACTION-NOISE | 37 | Physical object — excluded |
| QUALIFIER | 0 | Adverb/intensifier — excluded from primary clustering |

**Total anchored OWNER terms:** 2,491.
**Cluster catalogue:** Hebrew **55** clusters (`H001`…`H055`), Greek **33** clusters (`G001`…`G033`).
**Cluster ID format:** terms carry `cluster_id` (anchor) and `cluster_label` (top theme words). T2 terms additionally carry `attachment_affinity`. T1 = drives cluster centroid; T2 = inherits cluster from a T1 neighbour.

### 2.7 FLAG-bucket contents (24 terms — researcher review needed)

Three theme groups:

1. **Beloved family** — `dod` (×3 sub-entries H1730G/H/I), `yadid` (H3039A), `agapētos` (G0027) — straddle attribute-of-person vs. theological-affection.
2. **Judgment family** — `din`/`mishpat`/`shaphat`/`shephet` (Hebrew) and `krinō`/`krisis` (Greek) — judicial-act vs. inner-being-state ambiguity.
3. **Theological-anchor terms** — `berit`/`diathēkē` (covenant), `shem`/`onoma` (name), `proskuneō`/`proskunētēs` (worship), `christos`. Researcher-decision needed on whether these belong to a cluster or sit outside.

Plus four singletons: `arekh` (slow, C15), `gadal` (to magnify, C75), `qashah` (to harden, C15), `sēippim` (disquietings, C32).

### 2.8 Validation pass

[wa-term-anchor-validate-20260504.md](../../outputs/markdown/wa-term-anchor-validate-20260504.md) (+ JSON).

**Cluster quality (T1-only) — Hebrew:**

| Quality | Top-level (k=55) | After recursive sub-clustering |
|---|---|---|
| TIGHT | 13 | 28 |
| MODERATE | 33 | 51 |
| LOOSE | 9 | 0 |
| FREQUENCY-ARTIFACT | 0 | 0 |

**Cluster quality (T1-only) — Greek:**

| Quality | Top-level (k=33) | After recursive sub-clustering |
|---|---|---|
| TIGHT | 4 | 13 |
| MODERATE | 19 | 42 |
| LOOSE | 10 | 0 |
| FREQUENCY-ARTIFACT | 0 | 0 |

All LOOSE clusters resolve cleanly under recursive sub-clustering — i.e. the LOOSE label was a granularity artefact, not a structural defect.

**Verse coverage:**

- T1 (verse, term) pairs total: **32,840**
- Already classified: **25,943** (79.0%)
- **UNCLASSIFIED: 6,897 (21.0%)** spread across 5,753 distinct verses (32.4% of the 17,739 distinct T1-bearing verses contain at least one unclassified pair)

**Top unclassified workload (per cluster):**

| Cluster | Lang | Label | Unclassified pairs | Distinct verses |
|---|---|---|---|---|
| H028 | H | turn/aside/angry | 937 | 883 |
| H019 | H | truth/rule/delight | 502 | 497 |
| H034 | H | height/pride/majesty | 479 | 361 |
| H036 | H | sin/consecrate/desire | 467 | 462 |
| H048 | H | strengthen/strength/strong | 310 | 304 |
| H050 | H | enemy/thought/hostile | 307 | 286 |
| G029 | G | praise/slave/call | 245 | 235 |
| H023 | H | faithfulness/boast/song | 231 | 222 |
| H026 | H | sick/abomination/guilty | 204 | 190 |
| H009 | H | knowledge/understanding/meditation | 200 | 200 |

This is the work-list for the verse-classifier (the brief-router prototypes from §2.1 are the candidate engine for clearing it).

## 3. Pipeline implications (proposed, not yet adopted)

The day's work converges on the structure sketched in `research/notes/program reset.md`. Concretely:

- **Registry retains** surface role (collate Strong's anchored to inner-being words), then **steps aside**.
- **Clustering** by term, on **semantic-weighted + co-occurrence** vectors, with bucket separation (T1 / T2 / FLAG / EXTRACTION-NOISE / QUALIFIER). 88 leaf-clusters total (55 H + 33 G).
- **Verse classification** runs **per verse** (not per term-pair), produces **brief plain-English meaning + unresolved-interpretation pointers**. The `verse_context_group` table is **not** consulted for clustering and is judged unreliable as input.
- **Dimensions / dimension-review** are dropped — flagged by the researcher as noise built on wrong assumptions.
- **Volume mitigation:** classify per verse not per term-pair (32,840 pairs collapse to 17,739 distinct verses, of which only 5,753 still need classification = ~17% of the original term-pair volume).

**Status of these proposals:** all exploratory, no instruction docs updated, no DB writes, no patches. A formal redesign of Session B (and likely Session A and the verse-context pipeline) is the next decision point.

## 4. Open items / next session entry points

1. **FLAG-bucket review (24 terms)** — researcher-decision required on the three theme groups in §2.7.
2. **Unclassified-pair backlog (6,897 pairs / 5,753 verses)** — clear via brief-verse-router on the verse-grouped form. Top-10 clusters in §2.8 carry 73% of the volume.
3. **Recursive sub-cluster freeze** — the validate pass sub-clustered Hebrew T1 to 79 leaves and Greek T1 to 55 leaves. Researcher decision: keep the recursive structure as the canonical clustering, or stop at the 55+33 top-level?
4. **Cost model** — the 2026-05-03 20:14 cost concern is still unresolved. Per-verse classification + per-cluster prompts cuts volume substantially but a budget plan has not been built.
5. **Schema/migration impact** — none of today's structures exist in the DB. Whether `cluster_id` becomes a first-class column on `mti_terms` (or a sibling table) is open.
6. **Docs not yet updated** — `wa-sessionb-analysis-readiness`, `wa-sessionb-analysis-output`, `wa-versecontext-instruction`, `wa-registry-management-guide` all still describe the registry-driven pipeline. None of them reflect the term-anchor model.

## 5. Files produced today

**Scripts (all `scripts/_exploratory_*_20260504.py`, read-only, no DB writes):**
unclassified_sample_v1 · unclassified_concentrated_sample_v1 · unclassified_verse_sample_v1 · brief_meaning_router_v1 · brief_verse_router_v1 · thin_verse_router_v1 · term_usage_vector_v1 · term_semantic_vector_v1 · term_semantic_vector_weighted_v1 · term_cooccurrence_vector_v1 · term_cluster_assessment_v1 · term_loci_split_cluster_v1 · term_4way_cluster_v1 · term_4way_cluster_v2 · term_5way_cluster_v1 · term_5way_cluster_v2 · term_cluster_quality_v1 · term_cluster_quality_v2 · term_cluster_crosslang_v1 · term_anchor_build_v1 · term_anchor_validate_v1.

**Outputs:** all `outputs/markdown/*-20260504.{md,json,npz,meta.json}` — see `git status` after this session log is committed.

---

**Session log version:** v1
**Created:** 2026-05-04 (post-session, reconstructed from transcript `0d41cb24-79b1-4e0f-9ed8-483f94c8ba5e.jsonl`)
