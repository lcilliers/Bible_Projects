# WA-M04-dir-004-vcg-creation-applied-v2-20260517

**Phase 7 v2 (post-resubmission)** — VCG creation + vcg_term linking + verse routing + anchor designation
**Apply timestamp:** 2026-05-17T16:54:02Z
**Loader:** [scripts/_apply_m04_phase7_vcg_creation_v2_20260517.py](../../../scripts/_apply_m04_phase7_vcg_creation_v2_20260517.py)
**Directive id:** `DIR-20260517-008`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_4-20260517 §10 (with §10.7 staged-write-out + §10.8 no-sampling checklist + §10.9 CC validation)
**Source design:** [files phase 7/](files%20phase%207/) — 10 per-sub-group design docs + creation JSON + obslog

---

## Outcome

**30 VCGs inserted · 110 vcg_term links · 1135 verses routed · 30 + 39 anchors.**

All 3 post-checks PASS. All 5 §10.9 pre-apply checks passed (verified before apply). `cluster.status` unchanged at `Analysis - In Progress`.

## VCGs created (30 across 11 sub-groups)

| Sub-group | VCGs | Verses routed |
|---|---:|---:|
| M04-A Exultation in YHWH | 3 | 84 |
| **M04-B** Communal and Festive Rejoicing | **6** | **273** (33.5% — biggest substantive) |
| M04-C NT Joy in Christ and the Spirit | 5 | 143 |
| M04-D Shared Communal Rejoicing | 1 | 10 |
| M04-E Promised and Eschatological Joy | 2 | 35 |
| M04-F Cheerfulness Under Adversity | 1 | 4 |
| M04-G Delight in God's Word, Law, Wisdom | 2 | 26 |
| M04-H Volitional Delight | 4 | 133 (was 136; 3 legacy dups soft-deleted) |
| M04-I Wonder at God's Marvellous Works | 3 | 77 |
| M04-J Pleasantness and Relational Delight | 2 | 28 |
| M04-BOUNDARY (aggregating) | 1 | 322 |
| **TOTAL** | **30** | **1135** |

Plus **39 R4-fallback provisional anchors** for terms whose AI-designated VCG anchors didn't cover them.

## §10.9 pre-apply validation (all clean — v1's disasters fully fixed)

| Check | v1 result | v2 result |
|---|---|---|
| Phantom / cross-cluster vc_ids | 22 | **0** ✓ |
| Coverage gaps | 287 verses in M04-A | **0** ✓ |
| Cross-sub-group leaks | 0 | **0** ✓ |
| Anchor-not-in-members | 1 (M03-D-VCG-05) | **0** ✓ |
| Cross-VCG duplicates | 35 (intra-M04-A) | **0** ✓ |
| Per-sub-group sums | M04-A 169/661 (mismatch) | **all 11 match** ✓ |
| Total verses (JSON vs DB) | 686/1138 (43% short) | **1138/1138** ✓ |

§10.7 staged write-out + §10.8 no-sampling checklist worked as designed.

## Legacy (vr, mti) duplicate soft-deletes (3)

Three pairs of cha.phets (H2654A) vc rows shared the same `(verse_record_id, mti_term_id)` tuple. Under v2 single-VCG primary routing, both rows in each pair can't UPDATE to the same group_id (UNIQUE constraint). Kept the lower vc_id; soft-deleted the higher.

| vc_id (soft-deleted) | vc_id (kept) | Reference | Term | VCG |
|---:|---:|---|---|---|
| 9456 | 9412 | Isa 65:12 | cha.phets H2654A | M04-H-VCG-04 |
| 9457 | 9420 | Mal 2:17 | cha.phets H2654A | M04-H-VCG-04 |
| 9428 | 9400 | Psa 112:1 | cha.phets H2654A | M04-H-VCG-03 |

Same pattern as M03's Hab 1:3 a.mal legacy dup handling.

Effective routing count: **1135 active vc rows** (was 1138; minus 3 soft-deleted dups).

## Operations applied (single transaction)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| 0 | `verse_context` | 3 UPDATE | Legacy (vr,mti) dup soft-deletes |
| A | `verse_context_group` | 30 INSERT | 30 new VCGs |
| B | `vcg_term` | 110 INSERT | One per (VCG, term) pair derived from primary member set |
| C | `verse_context.group_id` | 1135 UPDATE | Mechanical per JSON `verses` arrays |
| D | `verse_context.is_anchor` | 121 RESET + 30 SET | All prior M04 anchors reset; 30 AI-designated VCG anchors set |
| D.1 | `verse_context.is_anchor` | 39 SET | R4 fallback per-term provisional anchors |

## Post-checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| H2 is_relevant=1 verses without group_id | 0 | 0 ✓ |
| H3 vc.mti_term_id not in its VCG's term set | 0 | 0 ✓ |
| R4 terms with is_relevant verses but no anchor | 0 | 0 ✓ |

## Brief compliance notes

- **§10.7 staged write-out**: AI wrote 10 of 11 per-sub-group design docs (missing M04-A; the JSON has M04-A's full content). Doc-on-disk count short by 1 file but analytical completeness 100% in the JSON. The §10.7 expectation is the per-sub-group write — minor deviation noted; not a re-submit trigger because all data is present in the JSON.
- **§10.8 no-sampling checklist**: every item passed. `verses` field used (not `key_verses`), complete arrays, sums match, every anchor in members, no duplicates, no invented/cross-cluster vc_ids, BOUNDARY-VCG-01 has all 322 BOUNDARY verses.

## State summary (post-Phase 7 v2)

- **Active cluster_finding rows for M04**: 0 (Phase 11 not run yet)
- **Active VCGs for M04**: 30 (new) + 86 inherited (to be dissolved at Phase 8) = 116 total
- **Active is_relevant M04 vc rows**: 1135 (was 1138; minus 3 legacy dups soft-deleted)
- **Anchors active**: 30 VCG-level + 39 R4 fallback = 69 `is_anchor=1` rows for M04
- **`cluster.status M04`**: `Analysis - In Progress`

## Provenance

- AI Phase 7 v2 design (10 docs + JSON): [files phase 7/](files%20phase%207/)
- Phase 7 v2 brief: [WA-M04-phase7-brief-to-AI-v2-20260517.md](WA-M04-phase7-brief-to-AI-v2-20260517.md)
- Apply script: [scripts/_apply_m04_phase7_vcg_creation_v2_20260517.py](../../../scripts/_apply_m04_phase7_vcg_creation_v2_20260517.py)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260517-008.db`
- Phase 6 v2 applied: [WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md](WA-M04-dir-003-subgroup-routing-applied-v2-20260517.md)
- v1 rejected outputs (Phase 5 + Phase 7): [files phase 5 rejected v1/](files%20phase%205%20rejected%20v1/) + [files phase 7 rejected v1/](files%20phase%207%20rejected%20v1/)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_4-20260517.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_4-20260517.md)

---

## Next step — Phase 8 (CC: dissolve 86 inherited VCGs)

CC will soft-delete the 86 inherited verse_context_groups for M04 terms + their vcg_term rows. No AI involvement.

*End of applied report.*
