# M38 Salvation — Pre-Analysis Observations

**Cluster:** M38 Salvation
**Status:** Not started (pre-Phase A)
**Date:** 2026-05-28
**Purpose:** Capture what stands out in the cluster's data state BEFORE Phase A runs, so observations are on the record and not retro-fitted to fit later patterns.

---

## Data state

| Aspect | State |
|---|---|
| mti_terms assigned (cluster_code='M38') | 13 active (4 delete_flagged) |
| Active verses across all 13 terms | 355 |
| Verses with Pass A keywords | 0 (Pass A not yet run) |
| verse_context records | 320 (some terms have gaps) |
| Legacy VC groups present | Yes, 1-3 per term (registry-level, pre-v3_0) |
| cluster_subgroup_id population | 0 (Phase B not started) |

---

## The 13 terms in detail

| Strongs | Translit | Gloss | Lang | Active verses | Owning registry | vc_status |
|---|---|---|---|---:|---|---|
| **Salvation-vocabulary register (6 terms, 241 verses)** ||||||
| G4982 | sōzō | to save | Greek | 99 | 187 strength | not_done |
| G4990 | sōtēr | savior | Greek | 24 | 196 power | not_done |
| G4991 | soteria | salvation | Greek | 43 | 187 strength | not_done |
| G4992 | sōtērion | saving | Greek | 5 | 196 power | not_done |
| H3444 | ye.shu.ah | salvation | Hebrew | 22 | 39 debauchery | not_done |
| H6299 | pa.dah | to ransom | Hebrew | 48 | 52 division | not_done |
| **Propitiation/atonement register (5 terms, 101 verses)** ||||||
| G2433 | hilaskomai | to propitiate | Greek | 2 | 111 mercy | to_revise |
| G2434 | hilasmos | propitiation | Greek | 2 | 111 mercy | to_revise |
| G2435 | hilastērios | propitiation | Greek | 2 | 111 mercy | to_revise |
| G2436 | hileōs | propitious/gracious | Greek | 2 | 111 mercy | to_revise |
| H3722B | ka.phar | to cover | Hebrew | 93 | 111 mercy | to_revise |
| **Free-gift register (2 terms, 13 verses)** ||||||
| G1431 | dōrea | free gift | Greek | 11 | 180 yielding | not_done |
| G1434 | dōrēma | free gift | Greek | 2 | 180 yielding | not_done |

---

## Things that stand out

### 1. The cluster is heterogeneous

The 13 terms split into three distinct semantic registers — salvation, atonement, free gift — that are theologically related but operationally distinct in the biblical material. The cluster name "Salvation" describes the first register; whether the second and third should remain in M38, or be re-located, is a Phase B constitution decision that should not be assumed in either direction.

**What this means for Phase A:** Pass A will be run uniformly across all 355 verses, but the keyword emergence will likely show three different keyword footprints. Phase B will need to decide whether one cluster with three characteristics is the right form, or whether two of the registers should be carved off.

### 2. Volume is heavily imbalanced

Two terms dominate:
- sōzō (G4982): 99 verses (28% of cluster)
- ka.phar (H3722B): 93 verses (26% of cluster)

Together these two are 54% of the cluster. The remaining 11 terms share 163 verses; six of them have ≤5 verses each. The volume pressure of sōzō + ka.phar will be strong; the cluster's design must resist letting these two terms over-determine the cluster's meaning.

### 3. Owning-registry words don't match cluster theme

The mti_terms gather salvation-meaning Strong's numbers from registries whose English names are "debauchery", "division", "mercy", "yielding", "strength", "power". This is the term-anchor methodology working — terms cluster by their own semantic field rather than by the English-word registry that originally extracted them. Worth noting because the registry/cluster mismatch could otherwise look like a data integrity issue.

### 4. The propitiation set has prior VC work flagged `to_revise`

All five hilask-/ka.phar terms have `vc_status='to_revise'`. The owning registry (111 mercy) has `session_b_status='Analysis Complete'`. This means the propitiation set was previously analysed under registry 111 mercy and is now flagged for revision in its new cluster context (M38). The prior VC group structure may or may not be useful as input to the M38 Phase A; this needs deliberate handling.

### 5. The free-gift set is small enough that its presence in M38 deserves scrutiny

13 verses across 2 terms (dōrea, dōrēma) is a small footprint. In NT use, dōrea sometimes does name the gift of salvation (Eph 2:8 in the broader passage), but it is also used for spiritual gifts, the Holy Spirit's giving, and general giving. Whether these 13 verses actually evidence salvation-meaning, or have been pulled into M38 because the surface translation overlapped, is a Phase A question.

### 6. Data gaps to resolve

- sōzō: 99 active verses, 94 vc records — 5 verses without classification
- pa.dah: 48 active verses, 32 vc records — 16 verses without classification
- ka.phar: 93 active verses, 81 vc records — 12 verses without classification

These gaps should be investigated. They may indicate legacy classification incomplete, or verses added after the last VC pass. Phase A coverage must include them.

### 7. No verses currently have keywords (Pass A not done)

The new v3_0 schema includes a `keywords` field on verse_context. Across all 13 M38 terms, this field is empty. Pass A will produce these per-verse keywords alongside the meanings. This is the foundational Phase A output and must be done before any Phase B work.

---

## Methodological discipline reminders for the work that follows

These are written here so they can be referenced during Phase A and Phase B rather than discovered in retrospect.

**From [feedback_two_governing_principles]:**
- Verse meaning is the data and rules all analytics
- All observations however disjointed must be recorded in the DB

**Bias-watch (this batch):**
- Do not assume the three semantic registers integrate into one coherent salvation-theology
- Do not let the dominance of sōzō + ka.phar override what the smaller-volume terms evidence
- If Phase D findings refuse a single integrating frame, the Phase E essay refuses one too
- The cluster name "Salvation" is provisional — the data may show that a different name is more accurate

**Specific questions to revisit at Phase B:**
- Do the 13 free-gift verses actually evidence salvation, or general gift?
- Should the propitiation set form its own characteristic, or be folded into a broader salvation-mechanism characteristic?
- Is sōzō functionally one term or are there multiple sōzō-senses (rescue/heal/save-eschatologically)?
- The Hebrew/Greek balance: 7 Greek terms vs 3 Hebrew terms with a 4th (H3722B) being the largest Hebrew. Does this evidence anything about how the OT and NT register the salvation domain differently?

**Hold open:**
- The user's intuition that previous essays felt "pressurised into findings that do not really exist" — particularly around the imposed integration template. Apply that discipline here.

---

*Pre-analysis v1 — 2026-05-28. To be referenced during M38 Phase A and onwards. Update if observations change.*
