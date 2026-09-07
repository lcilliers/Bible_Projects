# WA-M01-dir-002-subgroup-routing-applied-v1-20260516

**Phase 6 (v2_0):** Sub-group creation + term-to-sub-group placement + verse-to-sub-group routing
**Apply timestamp:** 2026-05-16 (Phase 6 directive)
**Loader:** [scripts/_apply_m01_phase6_subgroup_routing_20260516.py](../../scripts/_apply_m01_phase6_subgroup_routing_20260516.py)
**Source:** [WA-M01-subgroup-design-v1-20260516.md](WA-M01-subgroup-design-v1-20260516.md) (AI Phase 5 output)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §9

---

## Outcome

**8 sub-groups created · 106 mti_term_subgroup links · 1028 verse routings (690 mechanical + 338 cross-listing overrides).** Single transaction. Pre-conditions verified. Post-checks pass (H4=0, H6=0).

---

## Sub-group distribution

| Sub-group | Label | Terms | Verses (is_relevant) |
|---|---|---:|---:|
| M01-A | Reverential Fear / Fear of God as Governing Orientation | 13 | 329 |
| M01-B | Acute Fear and Alarm | 24 | 311 |
| M01-C | Terror as Overwhelming Force | 17 | 73 |
| M01-D | Dismay and Inner Collapse | 9 | 76 |
| M01-E | Trembling / Fear Made Somatic | 16 | 92 |
| M01-F | Anticipatory Dread and Anxiety | 10 | 42 |
| M01-G | Timidity and Cowardly Shrinking | 5 | 8 |
| M01-BOUNDARY | Boundary | 12 | 20 |

Total: 106 term-subgroup links (81 primary + 14 secondary cross-listings + 11 BOUNDARY supplements). Total verses routed: 951.

---

## Health checks

| Code | Count | Note |
|---|---:|---|
| H1 (vc with cluster_subgroup_id NULL) | 0 | every active M01 vc routed (incl. set-asides to their term's primary sub-group) |
| H2 (is_relevant=1 with group_id NULL) | 31 | Phase 7 (VCG design) work — expected |
| H4 (subgroup orphan: vc.cluster_subgroup_id without mti_term_subgroup link) | 0 | ✓ |
| H6 (term in cluster without mti_term_subgroup link) | 0 | ✓ |

---

## Operations executed

### Op A0 — Code-rename housekeeping

Soft-deleted DIR-20260515-002 sub-groups (created and then reset earlier) carried the canonical codes M01-A through M01-H + M01-BOUNDARY. The `cluster_subgroup` UNIQUE constraint `(cluster_code, subgroup_code)` applies regardless of `delete_flagged`, so we renamed those 9 rows by appending `_reset_v2_0_rerun_20260516` to free the canonical codes for the new design.

### Op A — INSERT 8 `cluster_subgroup` rows

| sort_order | subgroup_code | label |
|---:|---|---|
| 1 | M01-A | Reverential Fear / Fear of God as Governing Orientation |
| 2 | M01-B | Acute Fear and Alarm |
| 3 | M01-C | Terror as Overwhelming Force |
| 4 | M01-D | Dismay and Inner Collapse |
| 5 | M01-E | Trembling / Fear Made Somatic |
| 6 | M01-F | Anticipatory Dread and Anxiety |
| 7 | M01-G | Timidity and Cowardly Shrinking |
| 8 | M01-BOUNDARY | Boundary — Terms Held for Researcher Decision |

### Op B — INSERT 106 `mti_term_subgroup` rows

- 81 primary placements (one per active M01 term)
- 14 secondary placements (multi-faceted terms per AI §3)
- 11 BOUNDARY supplements

`placement_note` records `[primary]` or `[secondary]` per row, plus a back-link to DIR-20260516-002.

### Op C — UPDATE `verse_context.cluster_subgroup_id` for all active M01 vc rows

Routing logic per row:
1. If `(mti_term_id, reference)` matches a cross-listing entry in AI's §3: route to the cross-listing target.
2. Otherwise: route to the term's primary sub-group.

Result: 690 mechanical (term-primary) + 338 cross-listing overrides = **1028 vc rows updated**.

---

## CC interpretation calls (where AI's design needed CC judgment)

### 1. H3372H *ya.re-revere* (mti=1682) — missing from AI's §3 detail

AI listed H3372H as primary M01-A in §2's roster but did not detail it in §3 alongside H3372G (mti=298). H3372H has ~113 verses (per AI's earlier Phase 3 corpus). CC's default: place H3372H as primary M01-A + secondary M01-B, mirroring H3372G's pattern. AI did not supply the M01-B verse list for H3372H specifically; mechanical routing means **all H3372H verses land in M01-A** until a follow-up correction. Flag for AI's review.

### 2. *de.a.gah* (H1674, mti=107) — placement discrepancy in AI's design

AI's §2 M01-B roster includes de.a.gah (line in §2.2 "Note: fobeō, fobos, ya.re, pa.chad all have substantial verses in this sub-group" + earlier general listing); AI's §4 explicit single-sg table places de.a.gah primary in **M01-F** (Anticipatory Dread and Anxiety). The §4 placement is more analytically defensible (de.a.gah is the chronic-worry register). CC followed §4 — placed primary M01-F.

### 3. *me.go.rah* (H4034, mti=273) and *me.gu.rah* (H4035, mti=272) — placement

AI's §2 M01-A roster lists both. AI's §4 placement table puts both at **M01-F primary**. CC followed §4 (consistent with the "fears as anxieties" register of these noun forms).

### 4. *ya.gor*-noun (H3016, mti=276) — placement

AI's §2 M01-B roster lists this term. AI's §4 places it primary M01-B. CC followed.

### 5. *ya.gor*-verb (H3025, mti=296) — placement

AI's §2 M01-B roster lists this; AI's §4 places it primary **M01-F**. CC followed §4.

### 6. *cha.ra.dah* (H2731, mti=309) — multiple secondary

AI lists primary M01-E + secondaries M01-D + M01-G. CC inserted 3 mti_term_subgroup rows.

### 7. Verse-level cross-listings — 18 references didn't match active vc rows

These references appear in AI's §3 but didn't resolve to active vc rows in DB for the named mti:

| mti | Reference | Intended target |
|---|---|---|
| 1681 (H3373) | 2Ki 17:36 / 17:37 / 17:38 / 17:39 / 17:40 | M01-B |
| 829 (H6343) | Isa 33:14 · Isa 44:8 · Isa 44:11 · Jer 36:16 · Jer 36:24 · Jer 33:9 | M01-B |
| 829 (H6343) | Job 23:15 · Pro 3:24 · Isa 51:13 · Psa 78:53 · Isa 60:5 | M01-F |
| 291 (H6342) | Jer 30:5 | M01-B |

Likely causes: the verse uses a different M01 term (pa.chad-verb vs pa.chad-noun; or another fear root); the reference doesn't have a vc row for that mti in the cluster; or AI's reference is slightly off. These 18 rows fall back to term-primary placement (mechanical default). Flag for Phase 7 review.

### 8. Deu 32:27 *gur* — divine inner state, not human

AI noted: "God refrains from full destruction of Israel partly out of dread of how enemies would misinterpret it; this inner apprehension about enemy pride shapes his restrained judgment." This is the divine inner life, not a human inner state — outside programme scope.

CC routed Deu 32:27 / gur to M01-A primary per the mechanical default (gur's primary placement). **Researcher to decide:** should this vc row be set-aside (`is_relevant=0` + `set_aside_reason` populated)? Not changed in this directive.

---

## Reset audit trail

The earlier DIR-20260515-002 created 9 sub-groups (M01-A through M01-H + M01-BOUNDARY). Those were soft-deleted by the v2_0 rerun reset. To free the canonical sub-group codes for this new directive, CC renamed the 9 soft-deleted rows to append `_reset_v2_0_rerun_20260516`. Old structure remains queryable via `delete_flagged=1` filter; new structure uses the canonical codes.

---

## Tables not touched

| Table | Modified? |
|---|---|
| `cluster` | NO (status stays `Analysis - In Progress` per v2_0 §2.6) |
| `verse_context_group` | NO (Phase 7 work) |
| `vcg_term` | NO (Phase 7 work) |
| `verse_context.group_id`, `is_anchor`, etc. | NO (only `cluster_subgroup_id` updated) |
| `cluster_finding` | NO |
| `wa_session_b_findings` | NO |

---

## Next step — AI Phase 7 (VCG design within sub-groups)

Per v2_0 §10. Input: [Sessions/Session_Clusters/M01/wa-cluster-M01-subgroup-meanings-v1-20260516.md](wa-cluster-M01-subgroup-meanings-v1-20260516.md) — per-sub-group verse-and-meaning report with the new sub-group structure applied.

AI clusters the meanings within each sub-group into VCGs (verse-context groups), designates an anchor verse per VCG, and surfaces dual-membership verses. CC applies the new VCG structure in Phase 7 directive.

The 31 P-status (is_relevant + group_id IS NULL) verses will be assigned to new VCGs in Phase 7.
The 116 inherited VCGs remain in DB unchanged — Phase 8 will dissolve them via the comparison report.

---

## Provenance

- Directive script: [scripts/_apply_m01_phase6_subgroup_routing_20260516.py](../../scripts/_apply_m01_phase6_subgroup_routing_20260516.py)
- AI design: [WA-M01-subgroup-design-v1-20260516.md](WA-M01-subgroup-design-v1-20260516.md)
- Phase 5 brief: [WA-M01-phase5-brief-to-AI-v1-20260516.md](WA-M01-phase5-brief-to-AI-v1-20260516.md)
- Phase 4 applied: [WA-M01-dir-001-term-transfer-applied-v1-20260516.md](WA-M01-dir-001-term-transfer-applied-v1-20260516.md)
- Pre-apply backup: `backups/bible_research_backup_*_DIR-20260516-002.db`
