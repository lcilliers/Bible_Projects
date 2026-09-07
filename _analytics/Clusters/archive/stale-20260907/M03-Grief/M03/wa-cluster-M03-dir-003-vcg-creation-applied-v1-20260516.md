# WA-M03-dir-003-vcg-creation-applied-v1-20260516

**Phase 7 (v2_2):** VCG creation, vcg_term linking, verse routing, anchor designation
**Apply timestamp:** 2026-05-17T04:07:36Z
**Loader:** [scripts/_apply_m03_phase7_vcg_creation_20260516.py](../../../scripts/_apply_m03_phase7_vcg_creation_20260516.py)
**Directive id:** `DIR-20260516-017`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §10
**Source design:** [files phase 7/](files%20phase%207/) (8 per-sub-group VCG design docs + creation JSON + cross-routing flags)
**Validation report:** [WA-M03-phase7-validation-v1-20260516.md](WA-M03-phase7-validation-v1-20260516.md)

---

## Outcome

**25 VCGs inserted · 108 vcg_term links · 690 verses routed · 25 + 56 anchors.**

All three post-checks PASS (H2 group_id coverage, H3 vcg_term coverage, R4 anchor coverage). `cluster.status` unchanged at `Analysis - In Progress`.

## VCGs created (25 total)

| Sub-group | VCGs | Verses routed (primary) | Anchors set |
|---|---:|---:|---:|
| M03-A Weeping and Tears | 5 | 170 | 5 |
| M03-B Mourning and Lamentation | 4 | 117 | 4 |
| M03-C Sorrow and Inner Grief | 3 | 46 | 3 |
| M03-D Anguish and Distress | 5 | 105 | 5 |
| M03-E Groaning and Sighing | 3 | 31 | 3 |
| M03-F Pain and Inner Ache | 3 | 36 | 3 |
| M03-G Bitterness of Soul | 1 | 8 | 1 |
| M03-BOUNDARY (aggregating) | 1 | 177 | 1 |
| **TOTAL** | **25** | **690** | **25** |

Plus **56 R4-fallback provisional anchors** (per-term anchors for terms whose AI-designated VCG anchors didn't cover them).

## Reconciliation applied (per validation report)

### Invalid placements dropped (3)

| VCG | vc_id | Reason |
|---|---:|---|
| M03-D-VCG-01 | 1492 | Hallucination — does not exist in DB |
| M03-D-VCG-04 | 65109 | Job 38:23 tsar — set-aside (is_relevant=0) |
| M03-D-VCG-05 | 96 | Rom 1:18 orgē — M02 cluster, not M03 |

### Missing verses added (8)

| vc_id | Reference | Strong's | Sub-group → VCG |
|---:|---|---|---|
| 54599 | Jer 3:21 | be.khi | M03-A → M03-A-VCG-02 |
| 18529 | Est 6:12 | a.vel | M03-B → M03-B-VCG-01 |
| 29990 | Mic 1:8 | sa.phad | M03-B → M03-B-VCG-02 |
| 12781 | Isa 8:22 | tsu.qah | M03-BOUNDARY → M03-BOUNDARY-VCG-01 |
| 12782 | Pro 1:27 | tsu.qah | M03-BOUNDARY → M03-BOUNDARY-VCG-01 |
| 28984 | Psa 142:2 | si.ach | M03-BOUNDARY → M03-BOUNDARY-VCG-01 |
| 91 | Luk 2:48 | odunaō | M03-D → M03-D-VCG-05 |
| 1359 | Jon 2:2 | tsa.rah | M03-D → M03-D-VCG-01 |

### Dual-membership resolutions (6)

| vc_id | Reference | Primary VCG | Secondary VCG | Rationale |
|---:|---|---|---|---|
| 29992 | Zec 12:12 | M03-B-VCG-03 | M03-B-VCG-04 | OT divine-agency mourning > NT register |
| 38169 | Job 30:31 | M03-B-VCG-01 | M03-B-VCG-02 | Personal mourning rite > communal catastrophe |
| 54598 | Isa 65:19 | M03-A-VCG-05 | M03-A-VCG-03 | Eschatological end-of-weeping definitionally |
| 65106 | Job 7:11 | M03-D-VCG-02 | M03-D-VCG-01 | Anchor of VCG-02 — anchor must be primary member |
| 65175 | Zep 1:15 | M03-D-VCG-04 | M03-D-VCG-01 | "day of distress" — prophetic-oracle register |
| 144 | 2Cor 2:4 | M03-D-VCG-05 | M03-D-VCG-02 | Anchor of VCG-05 (NT anguish) — anchor must be primary member |

### Intra-VCG duplicate collapse (2)

| vc_id | Reference | VCG | Action |
|---:|---|---|---|
| 18501 | Neh 1:4 | M03-B-VCG-02 | Listed twice in same VCG; collapsed to one |
| 65102 | 2Sa 24:14 | M03-D-VCG-03 | Listed twice in same VCG; collapsed to one |

### Legacy (vr, mti) duplicate soft-delete (1)

| vc_id (deleted) | vc_id (kept) | Reference | Term | Reason |
|---:|---:|---|---|---|
| 1201 | 1186 | Hab 1:3 | a.mal (H5999, BOUNDARY) | Same `(verse_record_id, mti_term_id)` tuple appeared twice in vc. vc=1186 carries `is_anchor=1` + `notes='dual-context'`; vc=1201 soft-deleted to permit single-VCG primary routing under v2_2. |

Inherited DB has 1 other M03 `(vr, mti)` duplicate (already known); soft-delete brings is_relevant active count from 691 → 690.

## Operations applied (single transaction, DIR-20260516-017)

| Op | Table | Rows | Detail |
|---|---|---:|---|
| 0 | `verse_context` | 1 UPDATE | Legacy (vr,mti) dup soft-delete (vc=1201) |
| A | `verse_context_group` | 25 INSERT | 25 new VCGs, all `delete_flagged=0` |
| B | `vcg_term` | 108 INSERT | One per (VCG, term) pair derived from primary member set |
| C | `verse_context.group_id` | 690 UPDATE | Primary VCG routing; 6 verses also receive dual-membership note in `verse_context.notes` |
| D | `verse_context.is_anchor` | 118 RESET + 25 SET | All prior M03 anchors reset; 25 AI-designated VCG anchors set |
| D.1 | `verse_context.is_anchor` | 56 SET | R4 fallback — first canonical-order verse per uncovered term |

## Post-checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| H2 is_relevant=1 verses without group_id | 0 | 0 ✓ |
| H3 vc.mti_term_id not in its VCG's term set | 0 | 0 ✓ |
| R4 terms with is_relevant verses but no anchor | 0 | 0 ✓ |

## State summary

- **Active is_relevant M03 vc rows:** 690 (was 691; minus the 1 soft-deleted legacy dup)
- **VCGs (new, active):** 25 across 8 sub-groups
- **Inherited VCGs (still present, awaiting Phase 8 dissolution):** 101 (referenced by 0 active vc rows now — all M03 vc routing repointed at the new VCGs)
- **Anchors (active):** 25 VCG-level + 56 per-term R4 fallback = 81 total `is_anchor=1` rows for M03
- **Dual-memberships recorded in `verse_context.notes`:** 6
- **`cluster.status M03`:** unchanged at `Analysis - In Progress`

## Provenance

- AI Phase 7 design (8 docs + JSON): [files phase 7/](files%20phase%207/)
- Validation report: [WA-M03-phase7-validation-v1-20260516.md](WA-M03-phase7-validation-v1-20260516.md)
- Apply script: [scripts/_apply_m03_phase7_vcg_creation_20260516.py](../../../scripts/_apply_m03_phase7_vcg_creation_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260517_*_DIR-20260516-017.db`
- Phase 6 applied: [WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md](WA-M03-dir-002-subgroup-routing-applied-v1-20260516.md)

---

## Next step — Phase 8 (CC: VCG dissolution; no AI involvement)

CC will:

1. Generate inherited-VCG comparison report — for each of the 101 inherited M03 VCGs, list its terms and verses alongside the new VCG(s) that now own those verses.
2. Apply Phase 8 directive: soft-delete the 101 inherited VCGs (`verse_context_group.delete_flagged=1`) and their `vcg_term` rows.
3. Generate Phase 9 input — catalogue prompts per VCG for AI's question-answering.

*End of applied report.*
