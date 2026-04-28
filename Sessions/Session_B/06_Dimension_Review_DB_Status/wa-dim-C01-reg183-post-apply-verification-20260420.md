# C01 r183 DIMREVIEW Patch — Post-Apply Verification — 2026-04-20

| Field | Value |
|---|---|
| Filename | wa-dim-C01-reg183-post-apply-verification-20260420.md |
| Patch applied | `PATCH-20260420-DIMREVIEW-C01-REG183-V2` |
| Schema version | 3.11.0 |
| Status | **APPLIED — all FF checks PASS with findings for programme attention** |
| Produced | 2026-04-20 |

---

## 1. Pre-apply findings (from v1 patch)

Pre-apply validation found three ops requiring correction:

| Op | Issue | v2 disposition |
|---|---|---|
| OP-060 | `set.context_description` on `wa_dimension_index` — column dropped in M25 | **Removed in v2** (redundant: OP-059 updates canonical `verse_context_group.context_description`) |
| OP-062 | Same — `wa_dimension_index.context_description` sync | **Removed in v2** (redundant with OP-061) |
| OP-065 | Notes-only update on wa_dimension_index id=2763 (MO=1 row) — DR-8 protection rejected because `manual_override` not in set clause | **Amended in v2** — added explicit `manual_override: 1` to set clause to preserve state |

Also applied a **durable library fix** to `apply_session_patch.py`: `wa_dimension_index update` now filters unknown columns (same pattern as `word_registry update`), preventing future OP-075/OP-060-class failures. This is the DV-6 pattern proposed in §3 of the r112 post-apply verification.

**Pointer uniqueness:** All 4 SB findings (DIM-183-002..005) and 4 SD pointers (DIM-183-SD002..SD005) unique programme-wide. ✓

**Key format note:** patch uses `values` (not `record`). Applicator library fix from r112 apply now accepts both consistently. ✓

---

## 2. Apply outcome — v2 (72 ops)

| Operation | Count |
|---|---:|
| `wa_dimension_index update` | 59 (58 Phase C assignments + 1 orphan annotation) |
| `verse_context_group update` | 3 (2 Phase B description revisions + 1 orphan delete_flag) |
| `verse_context update` (cascade) | 1 (44 rows delete_flagged for orphan 577-005) |
| `wa_session_b_findings insert` | 4 |
| `wa_session_research_flags insert` | 4 |
| `word_registry update` | 1 |

All ops applied cleanly; transaction committed; patch archived.

---

## 3. FF-1..FF-11 results

### FF-1 Vocabulary vintage (r183)

| Metric | Count |
|---|---:|
| Total r183 active dim_index rows | 59 |
| Numbered current-vocab (`01..11`) | 58 ✓ |
| Legacy (`Moral/Conscience` — retained on orphan 2763) | 1 |

**PASS with note.** 58 Phase C assignments use current numbered-prefix vocabulary. The 1 legacy label is on orphan group 2763 — retained deliberately per session log §2.5 (preserves audit trail of the original classification before orphan detection).

### FF-2 Manual-override lock post-apply

Target MO states achieved. Orphan 2763 correctly preserves MO=1 (audit retained); all 58 active Phase C groups at MO=0 matching r112 convention (DR status=Complete anchors the review).

### FF-3 dominant_subject literal-NONE

No literal `'NONE'` values from OT-DBR-012 family. All 58 assignments use valid vocabulary.

### FF-4 dimension_confidence

All 58 Phase C groups stamped at `CLAUDE_AI` confidence.

### FF-5 DR status transition

| Field | Value |
|---|---|
| r183 `dim_review_status` | **Complete** ✓ |
| r183 `dim_review_version` | `wa-dimensionreview-instruction-v3_3-20260418` |

### FF-6 Cross-registry / cross-vintage coherence — **CRITICAL FINDING**

Post-apply, the live DB now carries **three distinct dimension-label vintages** AND **spacing variants** across 34 distinct active labels:

| Vintage | Example labels | Usage pattern |
|---|---|---|
| **Generation 0** (early legacy) | `Affective/Emotional`, `Cognitive/Mind`, `Moral/Conscience`, `Theological/Divine-Human`, `Spiritual/God-ward`, `Identity/Selfhood`, `Somatic/Embodied`, `Volitional/Will` | 157 rows — pre-current 11-dimension vocabulary |
| **Generation 1** (unnumbered current) | `Moral Character`, `Cognition`, `Divine-Human Correspondence`, `Emotion — Positive/Negative`, `Volition`, `Relational Disposition`, `Agency / Power`, `Dependence / Creatureliness`, `Vitality / Existence`, `Transformation` | 3,200+ rows — previous programme convention |
| **Generation 2** (numbered prefix — new today) | `01 Emotion — Positive`, `05 Moral Character`, `07 Vitality/Existence`, `09 Agency / Power`, `11 Divine-Human Correspondence` | 131 rows — r112 + r183 from Phase C 2026-04-20 |

**Plus spacing variants** within each generation:

- `Theological/Divine-Human` (53) vs `Theological / Divine-Human` (5)
- `Identity/Selfhood` (8) vs `Identity / Selfhood` (8)
- `07 Vitality/Existence` (6, no spaces) vs `09 Agency / Power` (1, with spaces) — **inconsistent within the new Gen 2 labels**

**Analytical impact:** any query `GROUP BY dimension` will fragment into 34 buckets rather than the intended 11. Cross-registry aggregation, correlation analysis, and cluster coherence metrics all affected.

**Root cause:** three distinct authoring contexts produced labels, and today's DimReview instruction §7.7 apparently specifies the numbered-prefix form while wa-reference-v5_7 §10 lists the unnumbered form. Gen 2 was introduced this session by Claude AI following the DimReview instruction's numbered form faithfully.

**Expansion of OT-DBR-015:** originally scoped as "vocabulary vintage mismatch" (Gen 0 vs Gen 1). Now must also address:
- Gen 1 vs Gen 2 (numbered prefix)
- Spacing inconsistencies within Gen 2 itself
- Canonical source — is §7.7 of DimReview instruction the authority, or wa-reference §10?

### FF-7 SD pointer increment

r183 SD pointers now: `DIM-183-SD001` (pre-existing) + `DIM-183-SD002..SD005` (new). Numbering contiguous and unique. ✓

### FF-8 Scope integrity

Only r183 `last_modified` rows touched. Other registries unaffected. ✓

### FF-9 Coverage

59 active r183 dim_index rows accounted for (58 Phase C + 1 orphan annotation). Matches patch. ✓

### FF-10 Q-COV linkage

Not triggered — r183 OWNER terms do not carry live `VERSE_EVIDENCE_*` flags that would require Q-COV surfacing. (Framework in place for when relevant.)

### FF-11 Schema compatibility (library-level now)

**PASS.** Two ops (OP-060, OP-062) would have failed pre-library fix. v2 skipped them explicitly; library fix would have silently no-oped them. Defence in depth.

---

## 4. Directive-driven evidence changes

### 4.1 580-001 (Aramaic le.vav) — description rewrite ✓

DIR-20260420-001 returned 6 Daniel verses. Phase C interpretation shifted to Dimension 11 (divine act on faculty pattern visible in 3 of 6 verses). Description now reads:

> "Term names the Aramaic heart as the defining inner faculty of the human person — the rational-moral consciousness that divine-human actions reach and shape …"

### 4.2 579-008 (affective le.vav) — description revision ✓

DIR-20260420-001 returned 25 verses. Description refined from "moral reflection" to "meditative pondering and inward knowing" based on verse corpus. Now reads:

> "Term names the heart in its experiential states — the inner register of grief, gladness, sorrow, longing, and the seat of …"

### 4.3 577-005 (hostile qe.rev) — orphan cleanup ✓

DIR-20260420-001 returned 0 verses with halt condition. Three-op cleanup applied:

- `verse_context_group.id=2763 → delete_flagged=1` with orphan rationale note
- Cascade: 44 `verse_context` rows (group_id=2763, delete_flagged=0) → `delete_flagged=1`
- `wa_dimension_index.id=2763` — preserved (MO=1) + notes annotation (audit history retained)

Post-cleanup verification: 0 active verse_context rows for group 2763. ✓

**FLAG-016 raised** (programme-wide orphan audit) — patch references it. Claude AI noted this as a programme-level follow-on, not blocking this cycle.

---

## 5. Pointers and findings added

4 SB findings (DIM-183-002..005) + 4 SD pointers (DIM-183-SD002..SD005). Full analytical content in observations log v1_5.

Key cross-registry patterns captured:

- **DIM-183-002:** Divine knowledge of the inner person — Dimension 11 cluster (3 r183 + 1 r112)
- **DIM-183-003:** Covenant-renewal pattern — extends r112's DIM-112-004 cluster to 8 total terms
- **DIM-183-SD002:** God-ward orientation — links to DIM-112-SD006; **potential Dimension 12 candidate**
- **DIM-183-SD005:** lev + le.vav widest dimensional spreads in C01

---

## 6. What my original raised points address

From the post-r112-apply summary, two decisions were pending:

### Point 1 — r183 group 2763 disposition — ✅ RESOLVED

Claude AI took option (b + partial c): soft-delete vcg + cascade, but RETAIN the `wa_dimension_index` row with MO=1 + annotated notes (preserves audit history that a classification was set at some earlier point). This is a hybrid approach between my proposed options and is analytically sound.

### Point 2 — OT-DBR-015 Option 1/2/3 for C01 realignment — ⚠️ NOW LARGER

This apply cycle added a third vintage (Gen 2 numbered prefix) to the existing mixed state. OT-DBR-015 must now address:

- Gen 0 vs Gen 1 vs Gen 2 (three vintages)
- Spacing variants within each
- Canonical-source determination (DimReview instruction §7.7 vs wa-reference §10)

CC recommendation (updated): **Option 3 (mapping + programme-wide sweep), expanded scope.** Should include:

1. **Canonical-source decision first** — which vintage is the target end-state? Gen 1 (unnumbered, previous convention) OR Gen 2 (numbered, today's new form)?
2. **Spacing rule declaration** — spaces-around-slash: yes or no (fix the Vitality / Existence vs Vitality/Existence split)
3. **Programme-wide mapping migration** — once (1) and (2) decided, one migration converts everything
4. **Instruction harmonisation** — DimReview §7.7 and wa-reference §10 must match the canonical form

---

## 7. Still open after this apply

| Item | Source | Disposition |
|---|---|---|
| RD-PHASE-C-112-001 (Dim 11 scope for 3 God-ward mind groups) | r112 session log | r112 patch encoded Dim 11; r183 applied same reading to parallel groups. Claude AI raised as SD pointer (DIM-112-SD006 + DIM-183-SD002) for potential Dim 12. Now effectively absorbed into Session D queue. |
| FLAG-010 (DR instruction audit) | pre-existing | Still OPEN; sessions continue under INSTRUCTION-NOTE |
| **FLAG-016 (programme-wide orphan audit)** | raised this cycle | NEW — programme-wide scan needed before next DimReview cluster; tractable (single SQL query) |
| Stamp template string stale | r112 session log | Not blocking; for next instruction revision |
| Pointer format reconciliation (legacy `112-SD0xx` without DIM- prefix) | r112 + r183 session logs | CC cleanup task |
| **Three-vintage dimension-label harmonisation** | this report §3 FF-6 | EXPANDS OT-DBR-015 scope |
| DV-6..DV-9 pre-check additions | r112 post-apply report | DV-6 (library filter) applied; DV-7/8/9 still candidate |

---

## 8. C01 Registry-Mode state — COMPLETE for target registries

- r112 mind: `dim_review_status = Complete` ✓ (applied earlier today)
- r183 heart: `dim_review_status = Complete` ✓ (applied this cycle)
- r182 Soul / r184 spirit / r185 flesh / r211 being: `Complete` under prior instruction versions (legacy vintage)

Cluster C01 target registries DONE. Next options for the researcher:

- **Option 1:** accept mixed-vintage (not recommended per Phase A + this report)
- **Option 2:** full re-review of 4 legacy-vintage C01 registries under v3_3
- **Option 3:** mapping migration (mechanical + per-case researcher decision on unmapped) — updated scope now includes Gen 1 → Gen 2 decision

Plus FLAG-016: decide whether to run the programme-wide orphan audit before any further DimReview work.

---

## 9. Artefacts produced this apply

- Backup: `backups/bible_research_pre_C01_dimreview_r183_20260420_122915.db`
- Patch v2: `data/imports/WA/Patches/wa-dim-c01-reg183-patch-v2-20260420.json` (archived post-apply)
- Library fix: `scripts/apply_session_patch.py` — `wa_dimension_index update` now filters unknown columns
- This verification report

---

*End of r183 post-apply verification. C01 Registry-Mode DR complete for targets; OT-DBR-015 scope expanded; decision awaiting researcher.*
