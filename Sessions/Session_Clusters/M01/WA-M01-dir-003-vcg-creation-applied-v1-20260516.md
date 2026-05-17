# WA-M01-dir-003-vcg-creation-applied-v1-20260516

**Phase 7 (v2_0):** VCG creation, verse-to-VCG routing, anchor designation
**Apply timestamp:** 2026-05-16 (Phase 7 directive)
**Loader:** [scripts/_apply_m01_phase7_vcg_creation_20260516.py](../../scripts/_apply_m01_phase7_vcg_creation_20260516.py)
**Source:** [WA-M01-vcg-design-v1-20260516.md](files%20vcg%20phase%207/WA-M01-vcg-design-v1-20260516.md) + [WA-M01-vcg-creation-v1-20260516.json](files%20vcg%20phase%207/WA-M01-vcg-creation-v1-20260516.json) (AI Phase 7) + [WA-M01-vcg-missing-verse-assignments-v1-20260516.json](files%20vcg%20phase%207/WA-M01-vcg-missing-verse-assignments-v1-20260516.json) (CC's API completion of 109 missing verses)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §10–11

---

## Outcome

**36 new VCGs created · 193 vcg_term links · 941 verses routed to new VCGs · 89 anchors set · 4 set-asides applied · 6 duplicate vc rows soft-deleted.** Single transaction. All health checks pass (H1=0, H2=0, H3=0, H4=0).

---

## Per-VCG distribution

| Sub-group | VCGs | Verses (total) | Anchors |
|---|---:|---:|---:|
| M01-A | 7 | 333 | 11 |
| M01-B | 6 | 273 | 19 |
| M01-C | 5 | 75 | 15 |
| M01-D | 5 | 78 | 9 |
| M01-E | 6 | 98 | 17 |
| M01-F | 5 | 58 | 8 |
| M01-G | 1 | 8 | 3 |
| M01-BOUNDARY | 1 | 18 | 7 |
| **Total** | **36** | **941** | **89** |

(Verse counts include dual-membership representations; distinct vc rows = 941.)

The 89 anchors break down as: 36 AI-designated (one per VCG) + 53 provisional anchors set by CC per R4 fallback rule (see §"Provisional anchors").

---

## Operations executed

### Op pre-A — Duplicate vc row soft-deletion (6 pairs)

DB contains 6 duplicate `verse_context` rows for M01 cluster terms — same `(verse_record_id, mti_term_id, cluster_subgroup_id)` tuple, both active, just different `group_id`. All 6 are for H3372H *ya.re-revere* (mti=1682):

| Kept vc_id | Soft-deleted vc_id | Reference |
|---:|---:|---|
| 4268 | 4954 | 2Ki 17:7 |
| 4209 | 4260 | Lev 19:32 |
| 4210 | 4261 | Lev 25:17 |
| 4211 | 4262 | Lev 25:36 |
| 4212 | 4263 | Lev 25:43 |
| 4257 | 4258 | Mal 2:5 |

The higher vc_id of each pair was soft-deleted with `delete_flagged=1` and an audit note. Both rows had identical Pass A `analysis_note` (no analytical content lost). Rule: keep the lower (older) id; soft-delete the duplicate.

This resolves a UNIQUE constraint collision that would otherwise have blocked Op C when both duplicates routed to the same VCG.

### Op A — INSERT 36 `verse_context_group` rows

One row per AI-designed VCG; `group_code` normalized to canonical `M01-X-VCG-NN` form (AI returned some assignments without the `VCG-` infix — normalized on merge). `context_description` from AI's design. `notes` includes the directive id and sub-group reference.

### Op B — INSERT 193 `vcg_term` rows

For each VCG, derived term set from member verses (one `vcg_term` row per (VCG, term) pair). 193 total links across the 36 VCGs.

### Op C — UPDATE `verse_context.group_id` for 941 rows

- 838 from AI's original design
- 109 from CC's missing-verse API assignment (Sonnet 4.6 atomic-per-row classification of high-corpus-overflow gaps)
- 1 from cross-routing flag (vc_id=15211 → M01-B-VCG-03, AI flagged but didn't include in JSON; CC added)
- Minus 6 duplicate vc rows (soft-deleted in Op pre-A; their group_id stays at the old inherited value, will be orphaned when Phase 8 dissolves inherited VCGs)

Total = 941 active vc rows routed.

### Op C.1 — Dual-membership notes (32 verses)

AI listed 32 vc_ids in multiple VCGs (legitimate dual-membership cases — verses whose meanings straddle two VCGs within the same or across sub-groups). The schema is single-FK on `verse_context.group_id`, so:

- **Primary VCG** = first VCG in sub-group iteration order (A → B → ... → BOUNDARY). The verse's `group_id` is set to the primary.
- **Secondary VCG(s)** recorded in `verse_context.notes` with prefix `{directive} dual-membership: primary=<code> secondary=[<list>]`.

Within-VCG duplicates (vc_id=15104 twice in M01-B-VCG-03; vc_id=64532 twice in M01-E-VCG-04) — treated as data errors not dual-membership; deduplicated.

### Op D — Anchor designation

1. **Reset:** All existing `is_anchor=1` rows in M01 cluster set to `is_anchor=0` (164 rows reset — these were inherited anchors from before Phase 7).
2. **Set:** Each of the 36 VCGs' designated anchor verse set to `is_anchor=1` (36 anchors set).

### Op D.1 — R4 fallback: provisional anchors per term (53 added)

AI's design designates one anchor per VCG (36 anchors). Many VCGs span multiple terms; the anchor belongs to ONE term per VCG, leaving the other terms in that VCG without an anchor. The applier's R4 rule requires **every term with `is_relevant=1` verses to have ≥1 anchor**.

For each term with relevant verses but no anchor after Op D, CC designated the term's **first canonical-order is_relevant verse** as a provisional anchor (same rule as Phase 1 §4.4). 53 terms received provisional anchors; the `notes` field of each provisional-anchor row records the audit text.

**Resulting anchor distribution:** 36 AI-designated VCG anchors + 53 provisional per-term anchors = 89 total.

### Op E — Set-asides (4 verses)

Per AI's cross-routing flags doc + researcher confirmation (all 4 approved):

| vc_id | Reference | Term | Reason |
|---:|---|---|---|
| 14968 | Deu 32:27 | H1481C gur | God's inner apprehension about enemy pride shaping his restrained judgment — divine inner life, not human inner being |
| 1846 | Eze 16:43 | H7264 ra.gaz | Inner fury aroused in God by Israel's unfaithfulness — divine inner state, not human fear-trembling |
| 64529 | Job 39:16 | H6343 pa.chad | Ostrich's lack of fear toward her young — animal instinct, not human inner being |
| 13958 | Job 25:2 | H6343 pa.chad | Dread as attribute of God's dominion — intrinsic quality of divine sovereign majesty, not human emotion |

Each row updated: `is_relevant=0`, `set_aside_reason` populated, `group_id=NULL`, `is_anchor=0`, audit note appended.

---

## Health checks (post-apply)

| Code | Count | Status |
|---|---:|---|
| H1 (active vc with cluster_subgroup_id NULL) | 0 | ✓ |
| H2 (is_relevant=1 with group_id NULL) | 0 | ✓ |
| H3 (vc mti not in vcg term set) | 0 | ✓ |
| H4 (vc.cluster_subgroup_id without mti_term_subgroup link) | 0 | ✓ |
| R4 (terms with is_relevant but no anchor) | 0 | ✓ |

All checks pass.

---

## State summary

| Item | Count |
|---|---:|
| Active M01 terms | 81 |
| Active sub-groups | 8 |
| **New VCGs (Phase 7)** | **36** |
| **Inherited VCGs (still in DB, to be dissolved Phase 8)** | **151** (sub-clusters of M01 terms via `vcg_term`) — count includes both new + inherited; new=36, inherited=115 |
| Active is_relevant verses | 947 (was 951; 4 set-aside) |
| Active vc rows routed to new VCGs | 941 |
| Anchors total | 89 |
| Set-asides total in M01 | 81 (76 inherited + 1 Act 7:11 + 4 just added) |

---

## Notes flagged for follow-up

1. **53 provisional anchors set by CC** — these are "first canonical verse per anchorless term" placeholders. Analytically defensible but not AI-curated. AI's Phase 7 design left 53 terms without anchors because their verses scattered into VCGs anchored by other terms. CC's fallback is the v2_0 §4.4 provisional-anchor rule. Researcher may want to revisit at Phase 12 closure to choose more representative anchor verses for these 53 terms.

2. **6 duplicate vc rows soft-deleted** — H3372H ya.re-revere had 6 pairs with identical (vr_id, mti_id) but different inherited group_ids. The higher-id row of each pair was soft-deleted (kept the lower, older row). Part of the OT-DBR-009 family of dedup issues. No analytical content lost.

3. **151 VCGs touching M01 — 36 new + 115 inherited.** Phase 8 dissolution comparison report will identify which inherited VCGs to soft-delete after researcher review.

4. **32 dual-membership rows** — primary VCG set; secondary recorded in `verse_context.notes`. If the schema later supports m:n verse-to-VCG, these can be expanded.

---

## Tables not touched

| Table | Modified? |
|---|---|
| `cluster.status` | NO — stays `Analysis - In Progress` per v2_0 §2.6 |
| `cluster_subgroup` | NO (Phase 6 work) |
| `mti_term_subgroup` | NO (Phase 6 work) |
| `cluster_finding` | NO (Phase 9/11 work) |
| `wa_session_b_findings` | NO |
| `wa_session_research_flags` | NO |
| Inherited `verse_context_group` rows | NO (Phase 8 dissolves them with researcher gate) |

---

## Next step — Phase 8 (VCG dissolution comparison report)

CC will:

1. Capture a pre-Phase-7 routing snapshot... actually too late — apply already changed the routing. The dissolution comparison can still proceed using `vcg_term → mti_terms → cluster_code` to identify inherited VCGs vs new (created by DIR-20260516-003).
2. Generate the dissolution comparison report (researcher-facing) via `_generate_vcg_dissolution_comparison_v1_*.py` — needs the new-VCG-min-id boundary as input.
3. Researcher reviews + approves dissolution dispositions.
4. CC applies the dissolution directive (soft-delete inherited VCGs + their vcg_term rows).

After Phase 8: AI Phase 9 (catalogue prompts) on the new VCG structure.

---

## Provenance

- AI design: [files vcg phase 7/WA-M01-vcg-design-v1-20260516.md](files%20vcg%20phase%207/WA-M01-vcg-design-v1-20260516.md)
- AI creation JSON: [files vcg phase 7/WA-M01-vcg-creation-v1-20260516.json](files%20vcg%20phase%207/WA-M01-vcg-creation-v1-20260516.json)
- AI cross-routing flags: [files vcg phase 7/WA-M01-phase7-cross-routing-flags-v1-20260516.md](files%20vcg%20phase%207/WA-M01-phase7-cross-routing-flags-v1-20260516.md)
- CC missing-verse API assignment: [files vcg phase 7/WA-M01-vcg-missing-verse-assignments-v1-20260516.json](files%20vcg%20phase%207/WA-M01-vcg-missing-verse-assignments-v1-20260516.json)
- Apply script: [scripts/_apply_m01_phase7_vcg_creation_20260516.py](../../scripts/_apply_m01_phase7_vcg_creation_20260516.py)
- Phase 7 brief: [WA-M01-phase7-brief-to-AI-v1-20260516.md](WA-M01-phase7-brief-to-AI-v1-20260516.md)
- Pre-apply backup: `backups/bible_research_backup_*_DIR-20260516-003.db`
