# Pooling, Dimensions, and Segments — Consolidated Comparison

**Date:** 2026-04-09
**Purpose:** Consolidate thinking around the pool-based Session B model, compare it to the Dimension Review work completed to date, and assess how the programme has evolved.

---

## 1. The Original Pool Design (v5.5/v5.6, March 2026)

The pool system was designed to solve one problem: **words that share XREF terms need to be analysed together in Session B, because the shared terms create cross-word dependencies that are invisible when words are analysed in isolation.**

### 1.1 Pool Structure

16 pool IDs were defined in WA-Registry-Management-Guide v5.7 Section 7a:

| Category | Pools | Words | Processing Logic |
|---|---|---|---|
| Independent | `not-shared` | 17 | No XREF overlap. Analyse in any order. |
| Low sharing | `unconnected` | 47 | Below 15-term sharing threshold. Group by cluster. |
| Small semantic pools | `pool2` through `pool8` | 24 (7 pools of 2-11 words) | Coherent semantic families (suffering, zeal, mercy, justice, shame, surrender, holiness). |
| Pool 1 sub-pools | 6 sub-pools | 61 | Heavily shared. Ordered by bond strength: anger-pair (51 shared) down to isolates (gravitational grouping). |

**Total:** 149 words assigned to pools. The remaining 33 words are excluded (Phase 1 Excluded, zero terms).

### 1.2 The Pool Pipeline (as designed)

```
Stage 1: Verse Context → all 181 registries classified
    ↓
DataPrep: Claude AI classifies terms → PREANALYSIS patch per registry
    ↓
Pool Assembly Gate: ALL words in pool reach Pre-Analysis Complete
    ↓
Claude Code constructs: wa-pool-{pool_id}-analysis-{date}.json
    ↓
Session B Analysis: Claude AI reads pool dataset → narrative per word
    ↓
Extraction: per-word patches, final extracts, Session D pointers
```

### 1.3 Pool Analysis Dataset Contents

The pool dataset was specified to contain:
- Per-word block with OWNER terms, contextual groups, anchor verse **full text**
- XREF term profiles with anchor **references only** (no full verse text)
- Cross-word map showing shared terms
- span_strong_match confirmation flags

### 1.4 Key Design Assumptions

1. Session B DataPrep (term classification) must precede analysis
2. All words in a pool must be at Pre-Analysis Complete before assembly
3. The pool dataset is the **sole input** for Session B analysis
4. Analysis runs per-pool (simultaneous) or per-word within pool (sequential fallback)
5. Pool membership is not stored in the database — derived from RMG Section 7a

---

## 2. What Actually Happened — The Dimension Review Stage

Between Verse Context completion and Session B, a new stage emerged: **Dimension Review** (v1.1 through v1.9, April 2026). This stage was not in the original v5.5/v5.6 design.

### 2.1 What Dimension Review Does

- Reviews all 3,469 contextual meaning groups across 22 clusters
- Assigns dimensions (inner-being categories) to each group
- Assigns dominant_subject (GOD/HUMAN/OTHER_HUMAN/UNSEEN/NONE)
- Corrects group descriptions where quality problems are found
- Captures Session B findings and Session D pointers during review
- Stamps each registry and cluster with the instruction version used

### 2.2 Current State

| Metric | Count |
|---|---|
| Total dimension_index rows | 3,469 |
| CLAUDE_AI reviewed | 820 (23.6%) |
| KEYWORD_WEAK (unreviewed) | 1,850 (53.3%) |
| KEYWORD_STRONG (unreviewed) | 368 (10.6%) |
| UNCLASSIFIED | 285 (8.2%) |
| ROOT_INFERRED | 146 (4.2%) |
| Clusters stamped (C20, C21, C22) | 3 of 22 |
| Registries dim_review Complete | 16 of 182 (8.8%) |
| Verse context groups | 3,469 |
| Verse context records | 62,245 |

### 2.3 What Dimension Review Added to the Data

Before Dimension Review, each word had:
- Verse Context groups with descriptions and anchor/related/set-aside classification
- Automated keyword dimension labels (55% classified, 45% UNCLASSIFIED)
- No dominant_subject assignments
- No quality-checked descriptions

After Dimension Review (for completed clusters), each word has:
- CLAUDE_AI-confirmed dimension assignments
- dominant_subject on every group
- Quality-checked descriptions (Phase B.5 rewrites where needed)
- Session B findings flagging analytical questions for deep analysis
- Session D pointers flagging cross-registry synthesis questions

---

## 3. Session B Instruction v3 — The Per-Word Model

Session B Instruction v3 (2026-04-09) introduces a fundamentally different model from the pool-based design:

### 3.1 Key Differences from the Pool Model

| Aspect | Pool Model (v5.5/v5.6) | Per-Word Model (v3) |
|---|---|---|
| **Input** | Pool analysis dataset (multi-word JSON) | Complete word extract (single-word JSON) + Session C documents |
| **Unit of work** | Pool (2-51 words simultaneously) | Single word |
| **Prerequisites** | DataPrep + pool assembly gate | Session C documents completed first |
| **Pipeline position** | After DataPrep, before Extraction | After Session C, feeding back into it |
| **Outputs** | Narrative per word + patches | Verse annotations, language annotations, analytical brief, Session C v2 documents |
| **Analysis structure** | Unspecified (narrative production) | Five defined passes: Meaning, Divine Dimension, Verse Annotation, Somatic/Spirit-Soul-Body, Language Annotation |
| **XREF handling** | Simultaneous analysis via pool | XREF data present in complete extract but no simultaneous cross-word requirement |
| **Session C relationship** | Session B precedes Session C | Session B follows Session C and corrects it |

### 3.2 What the Per-Word Model Gains

1. **Self-contained:** Each word can be analysed independently with its complete extract
2. **Session C feedback loop:** Verse and language annotations feed directly back into published documents
3. **Structured analysis:** Five defined passes ensure consistent coverage (meaning, divine dimension, verse annotation, somatic evidence, language audit)
4. **Spirit-soul-body classification:** Formalised as a primary output
5. **No pool assembly gate:** No need to wait for all words in a pool to reach a status threshold

### 3.3 What the Per-Word Model Loses

1. **Simultaneous XREF visibility:** When analysing grace, you cannot simultaneously see how H2603A functions in its OWNER registry (mercy). The XREF data is in the extract but the full OWNER context is not.
2. **Cross-word pattern detection:** Pool analysis was designed to surface patterns that only become visible when related words are read together
3. **DataPrep gate:** No term classification step before analysis — Session B reads raw data

---

## 4. Clusters vs Pools vs Dimensions — How They Relate

The programme now has three overlapping grouping systems:

### 4.1 Clusters (C01-C22)

- **Purpose:** Group semantically related words for Dimension Review
- **Stored:** `word_registry.cluster_assignment`
- **Size:** 4-14 words per cluster
- **Used by:** Dimension Review (extract construction, review unit, stamps)
- **Status:** All 22 clusters assigned. 3 clusters fully reviewed (C20, C21, C22).

### 4.2 Pools (16 pool IDs)

- **Purpose:** Group words by XREF sharing for simultaneous Session B analysis
- **Stored:** Not in database — defined in RMG Section 7a
- **Size:** 2-47 words per pool
- **Used by:** Pool analysis dataset construction (not yet triggered)
- **Status:** Defined but not yet operationally used. No pool datasets constructed.

### 4.3 Dimensions (11 categories)

- **Purpose:** Classify contextual meaning groups by inner-being aspect
- **Stored:** `wa_dimension_index.dimension`
- **Scope:** Per-group (3,469 groups), not per-word
- **Used by:** Dimension Review, will inform Session B analysis
- **Status:** 820 of 3,469 groups reviewed (23.6%)

### 4.4 The Overlap

Clusters and pools do not align:
- Pool 1 sub-pools span multiple clusters (e.g., `pool1-power-axis` includes words from C08, C20)
- Small pools sometimes align with clusters (e.g., `pool3-zeal` maps roughly to C07 words)
- `not-shared` and `unconnected` words are spread across all 22 clusters

Dimension Review works at the cluster level. Pool assembly works at the pool level. A word can be dimension-reviewed (cluster complete) but not pool-ready (other pool members not yet at Pre-Analysis Complete).

---

## 5. Where We Are Now — Assessment

### 5.1 Programme State

| Stage | Status |
|---|---|
| Phase 1 (extraction) | Complete — 182 registries |
| Verse Context | Complete — 182 registries, 62,245 records |
| Dimension Review | 8.8% — 16 registries, 3 clusters (C20-C22) |
| DataPrep | Not started — 0 registries at Pre-Analysis Complete |
| Pool Assembly | Not triggered — no pools ready |
| Session B | 1 registry (grace, Reg 68) at Analysis Complete |
| Session C | Not started |
| Session D | Not started |

### 5.2 The Grace Experiment

Grace (Reg 68) has reached Analysis Complete via Session B Instruction v3 — the per-word model. This bypassed:
- DataPrep (no PREANALYSIS patch)
- Pool assembly (grace is in pool `not-shared` or `unconnected` — independent anyway)
- Dimension Review for C17 (grace's cluster is not yet reviewed)

This works because grace is an independent word with no critical XREF dependencies. The per-word model is viable for `not-shared` words.

### 5.3 Questions for Decision

1. **Does the pool model still apply?** For the 17 `not-shared` words and 47 `unconnected` words (64 total), the per-word model works. For the 85 pool-connected words (pools 1-8), simultaneous analysis may still be valuable. But Session B v3's per-word model doesn't require it.

2. **Is DataPrep still needed?** Session B v3 reads the complete extract directly. The DataPrep step (term classification → PREANALYSIS patch) was designed to prepare data for the pool analysis dataset. If Session B reads the complete extract instead, DataPrep may be redundant — or it may need to be folded into the five-pass structure.

3. **Should Dimension Review complete before Session B?** Grace was analysed without its cluster's Dimension Review. The dimension data enriches the extract but isn't gated. The question is whether Session B quality suffers without reviewed dimensions.

4. **What happens to pool-connected words?** For `pool4-mercy` (compassion + mercy), analysing mercy without simultaneously seeing compassion's OWNER data loses the XREF context. The complete extract includes XREF terms but not their OWNER-side verse context. A pool-level extract or a paired extract may still be needed.

5. **How do clusters, pools, and the per-word model coexist?** One possibility: Dimension Review continues at the cluster level (it works well), Session B runs per-word for independent words, and pool-connected words get a supplementary cross-word briefing document alongside their complete extract.

---

## 6. Observations

### 6.1 What the Dimension Review Proved

The cluster-based Dimension Review stage has been productive:
- It surfaces analytical questions (Session B findings) before Session B begins
- It corrects group descriptions that would mislead Session B analysis
- It assigns dimensions that give Session B a structural framework
- The observations log / patch session model (v1.8+) works efficiently

### 6.2 What Session B v3 Proved

The grace experiment showed that:
- The five-pass structure produces specific, structured output (not just narrative)
- Spirit-soul-body classification can be done per-word with high confidence when data is rich
- Verse and language annotations are a concrete, useful output format
- The complete extract provides sufficient data for independent words

### 6.3 What Remains Untested

- Session B on a pool-connected word (e.g., mercy without compassion context)
- Session B on a word with completed Dimension Review vs without
- The value of DataPrep term classification as a pre-step vs folding it into Session B Pass 1
- Session C production (which Session B v3 assumes already exists)

---

*Produced by Claude Code — 2026-04-09. For researcher review and decision on pipeline adjustments.*
