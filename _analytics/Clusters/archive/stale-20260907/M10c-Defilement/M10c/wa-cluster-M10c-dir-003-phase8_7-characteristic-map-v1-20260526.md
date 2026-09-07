# Directive — M10c Phase 8.7 characteristic mapping

**Directive ID:** `wa-cluster-M10c-dir-003-phase8_7-characteristic-map-v1-20260526`
**Cluster:** M10c — Defilement and Impurity
**Phase:** 8.7 (characteristic mapping)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_9-20260526` §11B
**Issued:** 2026-05-26
**Applied:** 2026-05-26T08:12:02Z

## §1 Required-inputs declaration

| # | Type | Path | Version |
|---|---|---|---|
| 1 | Instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` | v2_9 |
| 2 | Global rules | `Workflow/Global_rules/wa-global-rules-all-v2_8.md` | v2_8 |
| 3 | Phase 5 design (characteristic identification) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-design-v1_0-20260526.md` | v1_0 |
| 4 | Phase 5 validation report (CC) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase5-validation-v1-20260526.md` | v1 |
| 5 | Phase 6 obslog | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-obslog-phase6-v1-20260526.md` | v1 |
| 6 | Phase 7 obslog (with VCG structure + R4 anchor handling) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-obslog-phase7-v1-20260526.md` | v1 |
| 7 | Phase 3 verdicts (cross-register flags) | `Sessions/Session_Clusters/M10c/wa-cluster-M10c-phase3-constitution-verdicts-v1_0-20260526.md` | v1_0 |

**No AI step.** Under v2_8/v2_9 §8.0 (characteristic-as-objective), Phase 8.7 reduces to CC-side confirmation when the Phase 5 design already declared the characteristics. M10c-A vs M10c-B is the only volume-split per §8.6; all other sub-groups map 1:1 to a characteristic.

## §2 Out-of-scope

- New sub-groups, new VCGs, or new term placements (forbidden at Phase 8.7 per §11B.2)
- Phase 9 findings authoring
- Cross-cluster relationship analytics (deferred to Phase 9 T6)

## §3 Pre-decisions

**Characteristic map (4 chars, 5 subgroup links):**

| char_seq | short_name | sub-groups | is_partial | Mapping pattern |
|---:|---|---|---|---|
| 1 | Ritual defilement-state | M10c-A + M10c-B | 0 (both) | §8.6 volume-split |
| 2 | Moral-inner defilement-state | M10c-C | 0 | 1:1 |
| 3 | Corporate/covenantal defilement | M10c-D | 0 | 1:1 |
| 4 | Defilement by external spiritual agency | M10c-E | 0 | 1:1 |

**Rationale for M:N on char 1:** the AI's Phase 5 design declared one characteristic ("Ritual defilement-state") split into two sub-groups (M10c-A bodily-contact, M10c-B categorical/classificatory) because combined ritual register would be 133V/263V = 50.6% — breaches the §8.6 distribution gate (40% cap = 105V). Both sub-groups *fully* serve characteristic 1 in different mechanisms (mechanism-vs-verdict axis), so `is_partial=0` for both. The split is volume-driven, not register-partitioning.

**Carry-forward observations (4 rows):**

| char | sub-group | type | title |
|---:|---|---|---|
| 1 | (cluster) | SPLIT_DESIGN_RATIONALE | Ritual-defilement characteristic volume-split per §8.6 (M10c-A vs M10c-B) |
| 4 | M10c-E | INTEGRATION_NOTE | Unclean-spirit register cross-cluster signal to M27 (cosmic-evil agents) |
| 3 | M10c-D | INTEGRATION_NOTE | Ezekiel idolatry sub-corpus within M10c-D — cross-cluster signal to M10b |
| 2 | M10c-C | INTEGRATION_NOTE | Moral-inner register cross-cluster signals (M10, M11, M29, M08, M09) |

## §4 Operations (single transaction)

| Op | Target | Rows | Effect |
|---|---|---:|---|
| A | `characteristic` | 4 INSERT | char_seq 1–4 with full definition |
| B | `characteristic_subgroup` | 5 INSERT | 1:2 for char 1 (M10c-A + M10c-B); 1:1 for chars 2/3/4 |
| C | `cluster_observation` | 4 INSERT | 1 SPLIT_DESIGN_RATIONALE + 3 INTEGRATION_NOTE; all status=`open`, target_phase=`phase_9_findings` |

Source: `scripts/_apply_m10c_phase8_7_characteristic_map_20260526.py`. Backup: `backups/bible_research_backup_20260526_081202_M10c-phase8_7-characteristic-map.db`.

## §5 Post-checks (all PASS)

- 4 characteristic rows for M10c
- 5 characteristic_subgroup links
- All 5 sub-groups bound to at least one characteristic
- 4 cluster_observation rows with status=`open`, target_phase=`phase_9_findings`

## §6 Result

**APPLIED.** Cluster state remains `Analysis - In Progress`. Phase 9 (catalogue findings) is the next analytical step — will fire one batch per characteristic (4 batches: CHAR-1 Ritual, CHAR-2 Moral-inner, CHAR-3 Corporate/covenantal, CHAR-4 External spiritual agency) plus a final cluster-synthesis batch.
