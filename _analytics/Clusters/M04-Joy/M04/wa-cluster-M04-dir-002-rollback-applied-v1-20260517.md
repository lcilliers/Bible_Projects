# WA-M04-dir-002-rollback-applied-v1-20260517

**Rollback of Phase 6 (DIR-20260517-005)** — sub-group routing reversed
**Apply timestamp:** 2026-05-17T13:03:40Z
**Loader:** [scripts/_rollback_m04_phase6_20260517.py](../../../scripts/_rollback_m04_phase6_20260517.py)
**Rollback directive id:** `DIR-20260517-006`
**Reason:** Phase 5 mapping failed §8.6 distribution hard gate (M04-A held 81% of substantive corpus; threshold 40%)
**Validation report:** [WA-M04-phase5-distribution-validation-v1-20260517.md](WA-M04-phase5-distribution-validation-v1-20260517.md)

---

## Outcome

Phase 6 mechanically reversed. All Phase-6-created DB structures soft-deleted or NULL'd. Phase 4 outcomes (term transfers, status flip) preserved.

| Op (reverse) | Table | Rows | Direction |
|---|---|---:|---|
| C reverse | `verse_context.cluster_subgroup_id` | 1138 | SET NULL |
| B reverse | `mti_term_subgroup` | 86 | `delete_flagged=1` + audit note |
| A reverse | `cluster_subgroup` | 7 | `delete_flagged=1` + audit note |

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| R1 active M04 sub-groups | 0 | 0 ✓ |
| R2 active mti_term_subgroup rows for M04 | 0 | 0 ✓ |
| R3 vc rows with cluster_subgroup_id set | 0 | 0 ✓ |
| R4 cluster.status M04 | `Analysis - In Progress` (unchanged) | `Analysis - In Progress` ✓ |
| R5 active M04 terms | 58 | 58 ✓ |

## What survives the rollback

- **Phase 4 term transfers** (5 transfers: hēdonē→M28, tharseō×2→M23, ga.vah→M08, mar.ge.ah→M33) — preserved.
- **cluster.status M04** = `Analysis - In Progress` — preserved.
- **`mti_terms.cluster_code`** for the 58 active terms — unchanged.
- **`verse_context.is_relevant`** + **`analysis_note`** (Phase 1 + Phase 2 outputs) — untouched.
- **`verse_context.is_anchor`** (Phase 1 provisional anchors) — untouched (1138 vc rows still have their Phase 1 anchors).
- **86 inherited verse_context_groups** (pre-Phase-7 legacy structures) — never touched by Phase 6; still present, will be dissolved at Phase 8 when redo reaches that point.

## What is removed

- All 7 cluster_subgroup rows for M04 (M04-A through M04-F + M04-BOUNDARY) — soft-deleted with audit note.
- All 86 mti_term_subgroup placements — soft-deleted with audit note.
- All 1138 `verse_context.cluster_subgroup_id` values — set to NULL.

## Archived rejected outputs

AI's v1 Phase 5 and Phase 7 outputs are preserved for reference:

- `Sessions/Session_Clusters/M04/files phase 5 rejected v1/` — v1 sub-group design + mapping JSON + obslog + Phase 5 brief
- `Sessions/Session_Clusters/M04/files phase 7 rejected v1/` — v1 VCG design docs + creation JSON + cross-routing flags + Phase 7 brief

The analytical content in v1 (especially the 10 M04-A VCG distinctions) remains useful for register identification in the v2 redo. The structural design is what was rejected, not the analytical work underneath it.

## Next step

Phase 5 v2 redo brief: [WA-M04-phase5-brief-to-AI-v2-20260517.md](WA-M04-phase5-brief-to-AI-v2-20260517.md)

Key changes from v1:
1. Cites §8.6 distribution hard gate (40% threshold) explicitly
2. Names the 9 proposed register-splits within the Joy / Rejoicing family (~120v vertical, ~80v communal, ~60v deliverance, ~50v NT-Christ, ~25v paradoxical, ~40v inverted, ~30v eschatological, ~25v heart-joy, ~30v divine-joy)
3. Instructs AI to drop the 22 invalid vc_ids (15 M42 misinclusions + 7 phantoms) from v1
4. Expected output: 8–13 substantive sub-groups + M04-BOUNDARY (vs v1's 6 + BOUNDARY)
5. CC will run §8.6 validator on the new mapping JSON before approving Phase 6

## Provenance

- Phase 6 applied (now rolled back): [WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md](WA-M04-dir-002-subgroup-routing-applied-v1-20260517.md)
- Rollback script: [scripts/_rollback_m04_phase6_20260517.py](../../../scripts/_rollback_m04_phase6_20260517.py)
- Pre-rollback backup: `backups/bible_research_backup_20260517_*_DIR-20260517-006.db`
- Distribution gate codification: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_3-20260517.md` §8.6

---

*End of rollback report.*
